"""Step 1. Set the reporting window and collect dated candidates per category from Google News RSS.

    python collect.py --workdir W --edition 2026-09-29 [--end 2026-09-29T06:23Z] [--hours 30]
                      [--yesterday W/yesterday_pool.csv]

Writes W/run.json (edition and window, read by every later step), W/candidates/cand_NN.json,
and W/yesterday_pool_titles.txt when yesterday's pool is given (the curators' exclusion list).
"""
import argparse, json, re, subprocess, urllib.parse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
import xml.etree.ElementTree as ET

from common import load_pool_file, parse_utc

Q = {
    1: ["AI model release", "new LLM", "OpenAI GPT model", "Google Gemini model", "Anthropic Claude model",
        "open-weight AI model", "DeepSeek OR Qwen OR Mistral OR Llama model", "AI video generation model",
        "AI image model", "AI reasoning model"],
    2: ["AI agent launch", "ChatGPT new feature", "AI assistant app launch", "AI browser", "Microsoft Copilot feature",
        "Gemini app feature", "AI coding agent", "enterprise AI agents", "AI shopping", "AI app update"],
    3: ["open source AI release", "AI developer tools", "AI API developers", "Hugging Face", "GitHub Copilot",
        "AI framework open source", "MCP server", "vibe coding tool", "AI dataset released", "local LLM"],
    4: ["AI study researchers", "AI research paper", "AI benchmark results", "scientists use AI", "machine learning study",
        "AI for science", "AI mathematics", "AI protein OR biology model", "AI climate model", "AI researchers find"],
    5: ["Altman said AI", "Jensen Huang says", "Hinton AI warns", "Musk says AI", "Zuckerberg AI said",
        "Dario Amodei", "Nadella AI said", "Pichai AI said", "CEO says artificial intelligence", "AI interview podcast says"],
    6: ["AI startup raises", "AI funding round", "acquires AI startup", "AI partnership deal", "AI Series A OR Series B",
        "AI IPO", "AI company valuation billion", "AI startup acquisition", "AI executive hires OR departs", "AI startup launches"],
    7: ["AI stocks", "Nvidia stock", "AI bubble", "AI capex spending", "AI valuation investors", "tech stocks AI week",
        "AI earnings", "AI debt bonds", "AI trade investors", "analyst AI stock upgrade"],
    8: ["AI chip", "Nvidia GPU", "TSMC", "HBM memory", "semiconductor AI", "AMD AI chip", "Intel AI chip",
        "Broadcom AI", "SK Hynix OR Samsung chip", "custom AI chip ASIC"],
    9: ["AI data center", "data center power grid", "data center energy", "hyperscale data center", "Stargate data center",
        "data center opposition", "data center nuclear", "neocloud CoreWeave OR Nebius", "data center water", "data center construction"],
    10: ["AI healthcare", "AI hospital", "AI drug discovery", "AI diagnosis", "medical AI FDA", "AI health study",
         "AI radiology OR imaging", "AI patients doctors", "biotech AI", "AI clinical"],
    11: ["humanoid robot", "robotaxi", "Waymo", "autonomous vehicle", "robotics AI", "AI drone", "Tesla Optimus",
         "warehouse robots", "self-driving", "robot startup"],
    12: ["AI cybersecurity", "AI security vulnerability", "deepfake scam", "AI safety", "prompt injection",
         "AI hackers", "OpenAI agents websites", "AI data breach", "AI alignment", "AI privacy"],
    13: ["AI regulation", "AI law", "AI bill", "AI lawsuit", "AI copyright", "AI export controls", "Pentagon AI",
         "EU AI Act", "US China AI", "AI policy government"],
    14: ["AI jobs", "AI schools students", "AI teachers", "Hollywood AI", "AI music artists", "AI workers layoffs",
         "AI survey poll", "AI companion", "AI journalism news", "AI society"],
    15: ["quantum computing", "quantum computer", "qubit", "quantum error correction", "neuromorphic computing",
         "IonQ OR D-Wave OR Rigetti", "quantum startup", "quantum research", "post-quantum", "photonic computing"],
    16: ["AI funny", "AI fail", "viral AI video", "AI hilarious", "robot fail", "AI weird", "chatbot bizarre",
         "AI prank", "AI meme", "AI gone wrong"],
}


def fetch(q):
    url = "https://news.google.com/rss/search?" + urllib.parse.urlencode(
        {"q": f"{q} when:2d", "hl": "en-US", "gl": "US", "ceid": "US:en"})
    r = subprocess.run(["curl", "-s", "-m", "20", "-A", "Mozilla/5.0", url], capture_output=True)
    items = []
    try:
        root = ET.fromstring(r.stdout)
    except ET.ParseError:
        return q, items
    for it in root.iter("item"):
        src = it.find("source")
        try:
            dt = parsedate_to_datetime(it.findtext("pubDate")).astimezone(timezone.utc)
        except Exception:
            continue
        title = it.findtext("title") or ""
        sname = src.text if src is not None else ""
        if sname and title.endswith(" - " + sname):
            title = title[: -len(" - " + sname)]
        items.append({"title": title.strip(), "source": sname, "source_url": src.get("url") if src is not None else "",
                      "link": it.findtext("link"), "published": dt.strftime("%Y-%m-%dT%H:%MZ"), "_dt": dt, "query": q})
    return q, items


def norm(t):
    return " ".join(re.findall(r"[a-z0-9]+", t.lower()))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--workdir', required=True)
    ap.add_argument('--edition', required=True, help='edition date YYYY-MM-DD')
    ap.add_argument('--end', help='window end, ISO UTC (default: now)')
    ap.add_argument('--hours', type=int, default=30)
    ap.add_argument('--yesterday', help="yesterday's pool, CSV or JSON")
    a = ap.parse_args()
    W = Path(a.workdir); (W / 'candidates').mkdir(parents=True, exist_ok=True)
    end = parse_utc(a.end) if a.end else datetime.now(timezone.utc).replace(second=0, microsecond=0)
    start = end - timedelta(hours=a.hours)
    run = {"edition": a.edition, "start": start.strftime("%Y-%m-%dT%H:%MZ"), "end": end.strftime("%Y-%m-%dT%H:%MZ"),
           "hours": a.hours, "yesterday": str(Path(a.yesterday).resolve()) if a.yesterday else None}
    (W / 'run.json').write_text(json.dumps(run, indent=1))

    if a.yesterday:
        y = load_pool_file(a.yesterday)
        (W / 'yesterday_pool_titles.txt').write_text(
            ''.join(f"{x['item_id']} | {x['title']}\n" for x in y), encoding='utf-8')
        print('yesterday titles', len(y))
    else:
        (W / 'yesterday_pool_titles.txt').write_text('', encoding='utf-8')
        print('WARNING: no yesterday pool given; repeats of yesterday cannot be excluded')

    jobs = [(cid, q) for cid, qs in Q.items() for q in qs]
    with ThreadPoolExecutor(12) as ex:
        results = list(ex.map(lambda j: (j[0],) + fetch(j[1]), jobs))
    summary = {}
    for cid in Q:
        seen, keep = set(), []
        for c, q, items in results:
            if c != cid:
                continue
            for it in items:
                if not (start <= it["_dt"] <= end):
                    continue
                k = norm(it["title"])[:80]
                if k in seen:
                    continue
                seen.add(k)
                it.pop("_dt")
                keep.append(it)
        keep.sort(key=lambda x: x["published"], reverse=True)
        (W / 'candidates' / f"cand_{cid:02d}.json").write_text(json.dumps(keep, indent=1, ensure_ascii=False))
        summary[cid] = len(keep)
    print("window", run['start'], "to", run['end'])
    print(summary, "total", sum(summary.values()))


if __name__ == "__main__":
    main()
