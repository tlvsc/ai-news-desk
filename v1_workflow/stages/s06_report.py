"""s06_report: the Daily Global AI Intelligence Report in the master prompt's story format, plus daily-pool.md.
Mid model writes story blocks from digests in batches; strong model writes the forward-looking analysis once,
from headlines and importance lines only (never the full text). Category order: Decision Log 23 Sep 2026.

Inputs: work/ranked.jsonl, work/pool_dispositions.jsonl, work/raw_pool.jsonl, work/source_ledger.json
Outputs: reports/<date> — Daily Global AI Intelligence Report.md, reports/supportive files/daily-pool.md,
         work/report_items.json (item numbers used by cards, bulletin and headlines)
"""
from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.common import load_json, log, read_jsonl, save_json, stage_main  # noqa: E402
from lib.llm_client import LLMClient, batched  # noqa: E402

SEP = "─" * 20


def select(ctx, ranked: list[dict]) -> list[dict]:
    g = ctx.config["gates"]
    order = [c["key"] for c in ctx.category_order()]
    pool = sorted(ranked, key=lambda r: (-r["importance"], order.index(r["category"]), r["id"]))
    chosen = pool[: g["report_max"]]
    crit = [r for r in chosen if r["importance"] >= 10]
    rest = [r for r in chosen if r["importance"] < 10]
    rest.sort(key=lambda r: (order.index(r["category"]), -r["importance"], r["id"]))
    return crit + rest


def run(ctx, extra_args=None) -> int:
    ranked = read_jsonl(ctx.work / "ranked.jsonl")
    if not ranked:
        log.error("no ranked.jsonl; run s04 first")
        return 1
    g = ctx.config["gates"]
    items = select(ctx, ranked)
    if len(items) < g["report_min"]:
        ctx.set_gate("full_report_gate_50_150", "FAIL", f"{len(items)} events below minimum {g['report_min']}")
        ctx.report_append("s06 report", f"FULL REPORT GATE FAILED: {len(items)} unique events, minimum {g['report_min']}. Stopped.")
        ctx.set_stage("s06_report", "failed", count=len(items))
        return 2
    llm = LLMClient(ctx)
    written = {}
    for batch in batched(items, ctx.config["llm"]["batch_sizes"].get("report", 12)):
        payload = {"format": "headline, importance reason, summary (one or two complete sentences with the new facts, numbers, context; do not repeat the headline)",
                   "events": [{"id": e["id"], "headline": e["headline"], "summary": e["summary"], "key_facts": e["key_facts"],
                               "label": e["label"], "category": e["category_name"], "why_it_matters": e.get("why_it_matters", ""),
                               "sources": e["sources"]} for e in batch]}
        reply = llm.call("mid", "report_story", payload, stage="s06_report")
        for s in reply.get("stories", []):
            written[s["id"]] = s
    # assemble
    ledger = load_json(ctx.work / "source_ledger.json", default={})
    disp = read_jsonl(ctx.work / "pool_dispositions.jsonl")
    n_dup = sum(1 for d in disp if d["disposition"].startswith("DUPLICATE"))
    n_prev = sum(1 for d in disp if d["disposition"].startswith("PREVIOUSLY"))
    crit = sum(1 for e in items if e["importance"] >= 10)
    high = sum(1 for e in items if 8 <= e["importance"] < 10)
    header = [f"*Daily Global AI Intelligence Report*", f"*Daily report date:* {ctx.edition.strftime('%-d %B %Y') if sys.platform != 'win32' else ctx.edition.strftime('%d %B %Y')}",
              f"*Weekly briefing:* AI News Desk V1 workflow, Claude lane test run (not the ChatGPT scheduled task)",
              f"*Coverage period:* {ctx.window_start.strftime('%d %b %Y %H:%M')} to {ctx.window_end.strftime('%d %b %Y %H:%M')} {ctx.config['timezone']}",
              f"*Candidates collected:* {sum(1 for d in disp if d['window_check'] != 'OUT OF WINDOW')}",
              f"*Same-day duplicates removed:* {n_dup}", f"*Previously covered stories removed:* {n_prev}",
              f"*Material updates included:* 0", f"*Final unique stories (total unique items found):* {len(items)}",
              f"*Critical items:* {crit}", f"*High-priority items:* {high}",
              f"*Major coverage groups searched:* {ledger.get('sources_checked_success_count', 0)} of {ledger.get('registry_source_count', 0)} registered sources checked",
              ""]
    if len(items) < 100:
        header.append(f"*Reason fewer than 100 stories were included:* {len(items)} unique verified events survived deduplication for this window.")
        header.append("")
    lines = header
    numbered = []
    n = 0
    section = None
    for e in items:
        sec = "Critical AI Developments" if e["importance"] >= 10 else e["category_name"]
        if sec != section:
            section = sec
            lines += [f"*{section}*", ""]
        n += 1
        s = written.get(e["id"], {})
        e_out = {"n": n, "id": e["id"], "headline": s.get("headline") or e["headline"], "label": e["label"], "category": e["category"],
                 "category_name": e["category_name"], "importance": e["importance"], "summary": s.get("summary") or e["summary"],
                 "importance_reason": s.get("importance_reason") or e.get("why_it_matters", ""), "source": e["primary_source"],
                 "url": e["primary_url"], "key_facts": e["key_facts"], "verification": e["verification"], "fun": e.get("fun", False),
                 "big_name": e.get("big_name", False)}
        numbered.append(e_out)
        lines += [f"*{n}. {e_out['headline']}*", f"*Importance:* {e_out['label']} — {e_out['importance_reason']}",
                  f"*Source:* {e_out['source']}", f"*Summary:* {e_out['summary']}", f"*Full article:* {e_out['url']}", SEP, ""]
    # forward-looking analysis (strong model, small input)
    payload = {"edition": ctx.edition.isoformat(),
               "items": [{"n": x["n"], "headline": x["headline"], "label": x["label"], "category": x["category_name"]} for x in numbered],
               "previous_analyses": recent_analyses(ctx)}
    analysis = llm.call("strong", "analysis", payload, stage="s06_report").get("analysis_markdown", "")
    lines += ["", "*FORWARD-LOOKING ANALYSIS: PROBABILITIES, OUTCOMES, WHAT MAY HAPPEN NEXT*", "", analysis.strip(), "",
              "END OF REPORT", ""]
    path = ctx.reports / f"{ctx.edition.isoformat()} — Daily Global AI Intelligence Report.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    save_json(ctx.work / "report_items.json", {"edition": ctx.edition.isoformat(), "count": len(numbered), "items": numbered})
    write_daily_pool(ctx, disp, ranked)
    # history for future dedupe
    hist = ctx.history / "events_history.jsonl"
    hist.parent.mkdir(parents=True, exist_ok=True)
    existing = {h.get("id") for h in read_jsonl(hist)}
    with hist.open("a", encoding="utf-8") as fh:
        for x in numbered:
            if x["id"] not in existing:
                fh.write(__import__("json").dumps({"id": x["id"], "edition": ctx.edition.isoformat(), "headline": x["headline"],
                                                   "summary": x["summary"], "url": x["url"]}, ensure_ascii=False) + "\n")
    ctx.set_gate("full_report_gate_50_150", "PASS", f"{len(numbered)} stories")
    ctx.report_append("s06 report", f"Full Report written: {path.name}, {len(numbered)} stories ({crit} critical, {high} high). "
                                    f"daily-pool.md written. LLM so far: {llm.summary()}")
    ctx.set_stage("s06_report", "done", count=len(numbered), path=str(path))
    return 0


def recent_analyses(ctx) -> list[dict]:
    """Headings of previous editions' analyses if the run folders exist locally (max 14 days)."""
    out = []
    for i in range(1, 15):
        d = ctx.edition - dt.timedelta(days=i)
        f = ctx.local_root / d.isoformat() / "reports" / f"{d.isoformat()} — Daily Global AI Intelligence Report.md"
        if f.exists():
            text = f.read_text(encoding="utf-8")
            if "FORWARD-LOOKING ANALYSIS" in text:
                out.append({"edition": d.isoformat(), "excerpt": text.split("FORWARD-LOOKING ANALYSIS", 1)[1][:1200]})
    return out


def write_daily_pool(ctx, disp: list[dict], ranked: list[dict]) -> None:
    """daily-pool.md per AIND_daily_storage_rules.txt: every record, its outcome and reason, grouped for reading."""
    by_id = {r["id"]: r for r in ranked}
    lines = [f"# Daily Pool — {ctx.edition.isoformat()}", "", f"Edition date: {ctx.edition.isoformat()}",
             f"Reporting window: {ctx.window_start.strftime('%Y-%m-%d %H:%M')} to {ctx.window_end.strftime('%Y-%m-%d %H:%M')}",
             f"Timezone: {ctx.config['timezone']}", f"Run identity: AI News Desk V1 workflow, Claude lane ({ctx.lane}), test run",
             f"Last updated: {dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}", "Status: Complete", "",
             "## Part 1. Retained events by category (importance order)", ""]
    for c in ctx.category_order():
        rows = [r for r in ranked if r["category"] == c["key"]]
        if not rows:
            lines += [f"### {c['name']}", "", "searched, no qualifying result", ""]
            continue
        lines += [f"### {c['name']} ({len(rows)})", ""]
        for r in sorted(rows, key=lambda x: -x["importance"]):
            lines += [f"- {r['id']} [{r['importance']}/10 {r['label']}] {r['headline']} — {r['primary_source']} — {r['primary_url']}"]
        lines.append("")
    lines += ["## Part 2. Every collected record and its disposition", "", "| id | disposition | window | source | title | url |", "|---|---|---|---|---|---|"]
    for d in disp:
        lines.append(f"| {d['id']} | {d['disposition']} | {d['window_check']} | {d['source']} | {d['title'][:90].replace('|','/')} | {d['url']} |")
    lines.append("")
    (ctx.reports_sup / "daily-pool.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    stage_main(run, __doc__)
