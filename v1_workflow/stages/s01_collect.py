"""s01_collect: fetch every registered V1 source for the reporting window. Zero LLM. PC only (needs the open web).

Implements the 18 Sep 2026 SOURCE FETCH GATE: every Source ID ends with one evidence-backed terminal status,
  CHECKED — CANDIDATE(S) FOUND [n] | CHECKED — NO QUALIFYING ITEM | FAILED/UNAVAILABLE [reason] | INCOMPLETE COVERAGE [reason]
Nothing is invented. Items outside the window are kept with OUT OF WINDOW so the pool shows they were seen.
Outputs: work/raw_pool.jsonl, work/source_ledger.json, a section in V1_script_report.md.

Run alone:  python stages/s01_collect.py --edition 2026-09-27 [--fixture path.jsonl] [--extra work/extra_items.jsonl]
"""
from __future__ import annotations

import datetime as dt
import email.utils
import html
import re
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urljoin, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.common import (log, norm_text, norm_url, read_jsonl, save_json, stage_main, write_jsonl)  # noqa: E402

FEED_GUESSES = ["/feed/", "/feed", "/rss", "/rss.xml", "/feed.xml", "/atom.xml", "/index.xml", "/feeds/all"]
TAG_RE = re.compile(r"<[^>]+>")
SCRIPT_RE = re.compile(r"<(script|style|noscript|svg|nav|footer|header)[^>]*>.*?</\1>", re.S | re.I)
P_RE = re.compile(r"<p[^>]*>(.*?)</p>", re.S | re.I)
A_RE = re.compile(r"<a[^>]+href=[\"']([^\"']+)[\"'][^>]*>(.*?)</a>", re.S | re.I)
ALT_RE = re.compile(r"<link[^>]+type=[\"']application/(?:rss|atom)\+xml[\"'][^>]*href=[\"']([^\"']+)[\"']", re.I)
ALT_RE2 = re.compile(r"<link[^>]+href=[\"']([^\"']+)[\"'][^>]*type=[\"']application/(?:rss|atom)\+xml[\"']", re.I)


class Fetcher:
    def __init__(self, cfg: dict):
        self.timeout = cfg.get("timeout_seconds", 20)
        self.retries = cfg.get("retries", 2)
        self.delay = cfg.get("per_domain_delay_seconds", 1.5)
        self.ua = cfg.get("user_agent", "AINewsDesk-V1-collector/1.0")
        self.last: dict[str, float] = {}

    def get(self, url: str) -> tuple[bytes | None, str]:
        host = urlsplit(url).netloc
        wait = self.delay - (time.time() - self.last.get(host, 0))
        if wait > 0:
            time.sleep(wait)
        err = ""
        for attempt in range(self.retries + 1):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": self.ua, "Accept": "*/*"})
                with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                    data = resp.read()
                self.last[host] = time.time()
                return data, ""
            except urllib.error.HTTPError as exc:
                err = f"HTTP {exc.code}"
                if exc.code in (401, 403, 404, 410, 451):
                    break
            except Exception as exc:  # noqa: BLE001
                err = f"{type(exc).__name__}: {str(exc)[:120]}"
            time.sleep(1 + attempt)
        self.last[host] = time.time()
        return None, err


def parse_date(text: str | None) -> dt.datetime | None:
    if not text:
        return None
    text = text.strip()
    try:
        d = email.utils.parsedate_to_datetime(text)
        if d.tzinfo is None:
            d = d.replace(tzinfo=dt.timezone.utc)
        return d
    except (TypeError, ValueError):
        pass
    try:
        d = dt.datetime.fromisoformat(text.replace("Z", "+00:00"))
        if d.tzinfo is None:
            d = d.replace(tzinfo=dt.timezone.utc)
        return d
    except ValueError:
        return None


def strip_html(s: str) -> str:
    return norm_text(html.unescape(TAG_RE.sub(" ", s or "")))


def parse_feed(data: bytes) -> list[dict]:
    """RSS 2.0 or Atom, namespace tolerant. Returns title, link, published, summary."""
    try:
        root = ET.fromstring(data)
    except ET.ParseError:
        return []
    items = []

    def local(tag):
        return tag.split("}")[-1].lower()

    for el in root.iter():
        if local(el.tag) not in ("item", "entry"):
            continue
        rec = {"title": "", "link": "", "published": None, "summary": ""}
        for ch in el:
            t = local(ch.tag)
            txt = (ch.text or "").strip()
            if t == "title":
                rec["title"] = strip_html(txt)
            elif t == "link":
                href = ch.attrib.get("href") or txt
                if href and (not rec["link"] or ch.attrib.get("rel", "alternate") == "alternate"):
                    rec["link"] = href.strip()
            elif t in ("pubdate", "published", "updated", "date") and not rec["published"]:
                rec["published"] = txt
            elif t in ("description", "summary", "content", "encoded") and not rec["summary"]:
                rec["summary"] = strip_html(txt)[:600]
        if rec["title"] and rec["link"]:
            items.append(rec)
    return items


def discover_feed(fetcher: Fetcher, page_url: str) -> tuple[str | None, bytes | None]:
    data, err = fetcher.get(page_url)
    if data:
        text = data.decode("utf-8", "ignore")
        for rx in (ALT_RE, ALT_RE2):
            m = rx.search(text)
            if m:
                feed = urljoin(page_url, html.unescape(m.group(1)))
                fdata, _ = fetcher.get(feed)
                if fdata and parse_feed(fdata):
                    return feed, fdata
    base = page_url.rstrip("/")
    for guess in FEED_GUESSES:
        fdata, _ = fetcher.get(base + guess)
        if fdata and parse_feed(fdata):
            return base + guess, fdata
    return None, data


def html_links(page_url: str, data: bytes) -> list[dict]:
    """Fallback when no feed exists: article-looking links on the section page, date unknown."""
    text = SCRIPT_RE.sub(" ", data.decode("utf-8", "ignore"))
    host = urlsplit(page_url).netloc.replace("www.", "")
    seen, out = set(), []
    for href, inner in A_RE.findall(text):
        title = strip_html(inner)
        url = urljoin(page_url, html.unescape(href))
        if len(title) < 28 or urlsplit(url).netloc.replace("www.", "") != host:
            continue
        if url in seen or len(urlsplit(url).path.strip("/").split("/")) < 2:
            continue
        seen.add(url)
        out.append({"title": title, "link": url, "published": None, "summary": ""})
    return out


def article_text(fetcher: Fetcher, url: str, limit: int) -> tuple[str, str]:
    data, err = fetcher.get(url)
    if not data:
        return "", err or "no data"
    text = SCRIPT_RE.sub(" ", data.decode("utf-8", "ignore"))
    paras = [strip_html(p) for p in P_RE.findall(text)]
    paras = [p for p in paras if len(p) > 60]
    body = " ".join(paras)
    return body[:limit], "" if body else "no paragraphs"


def run(ctx, extra_args=None) -> int:
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--fixture", help="jsonl of pre-collected items instead of the network (tests)")
    p.add_argument("--extra", help="jsonl of manually supplied items (web search hits, Rafael additions)")
    p.add_argument("--no-articles", action="store_true", help="skip article body fetch (feeds only)")
    args = p.parse_args(extra_args or [])
    ccfg = ctx.config.get("collector", {})
    fetcher = Fetcher(ccfg)
    sources = ctx.sources["sources"]
    start, end = ctx.window_start, ctx.window_end
    ledger, pool = [], []
    nid = 0

    def add(rec, src):
        nonlocal nid
        nid += 1
        pub = parse_date(rec.get("published"))
        if pub is None:
            window = "UNVERIFIED DATE"
        elif start <= pub < end:
            window = "IN WINDOW"
        else:
            window = "OUT OF WINDOW"
        pool.append({"id": f"RAW-{ctx.edition.strftime('%Y%m%d')}-{nid:04d}", "source_id": src["id"],
                     "source_name": src["name"], "category_hint": src.get("category"), "title": rec["title"],
                     "url": rec["link"], "url_norm": norm_url(rec["link"]),
                     "published": pub.isoformat() if pub else None, "window_check": window,
                     "summary": rec.get("summary", ""), "text": rec.get("text", ""), "fetch_status": rec.get("fetch_status", "")})
        return window

    fixture = {}
    if args.fixture:
        for row in read_jsonl(args.fixture):
            fixture.setdefault(row.get("source_id", "*"), []).append(row)

    for src in sources:
        t0 = time.time()
        entry = {"id": src["id"], "name": src["name"], "category": src.get("category"), "route": None, "status": "",
                 "in_window": 0, "out_of_window": 0, "unverified": 0, "error": ""}
        items, route, err = [], None, ""
        if fixture:
            items = fixture.get(src["id"], []) + ([] if src["id"] in fixture else fixture.get("*", []))
            route = "fixture"
        else:
            feed = src.get("feed_url")
            if feed:
                fdata, err = fetcher.get(feed)
                if fdata:
                    items = parse_feed(fdata)
                    route = feed if items else None
            if not items:
                feed2, page = discover_feed(fetcher, src["url"])
                if feed2:
                    fdata, _ = fetcher.get(feed2)
                    items, route = parse_feed(fdata or b""), feed2
                elif page:
                    items, route = html_links(src["url"], page), src["url"] + " (html links, no dates)"
                else:
                    err = err or "page unreachable"
        items = items[: ccfg.get("max_items_per_source", 80)]
        for rec in items:
            w = add(rec, src)
            entry["in_window" if w == "IN WINDOW" else "out_of_window" if w == "OUT OF WINDOW" else "unverified"] += 1
        entry["route"] = route
        if not items and err:
            entry["status"] = f"FAILED/UNAVAILABLE [{err}]"
        elif not items:
            entry["status"] = "INCOMPLETE COVERAGE [route returned no items]"
        elif route and "html links" in route:
            entry["status"] = f"INCOMPLETE COVERAGE [no feed; {len(items)} undated links from section page]"
        elif entry["in_window"]:
            entry["status"] = f"CHECKED — CANDIDATE(S) FOUND [{entry['in_window']}]"
        else:
            entry["status"] = "CHECKED — NO QUALIFYING ITEM"
        entry["seconds"] = round(time.time() - t0, 1)
        ledger.append(entry)
        log.info("%s %-28s %s", src["id"], src["name"][:28], entry["status"])

    if args.extra:
        for row in read_jsonl(args.extra):
            add({"title": row.get("title", ""), "link": row.get("url") or row.get("link", ""),
                 "published": row.get("published"), "summary": row.get("summary", ""), "text": row.get("text", "")},
                {"id": row.get("source_id", "SRC-EXTRA"), "name": row.get("source_name", "manual"), "category": row.get("category_hint")})

    if not args.no_articles and not fixture:
        limit = ccfg.get("article_text_chars", 2500)
        for rec in pool:
            if rec["window_check"] == "OUT OF WINDOW" or rec.get("text"):
                continue
            body, ferr = article_text(fetcher, rec["url"], limit)
            rec["text"], rec["fetch_status"] = body or rec.get("summary", ""), ferr or "ok"

    write_jsonl(ctx.work / "raw_pool.jsonl", pool)
    checked = sum(1 for e in ledger if e["status"].startswith("CHECKED"))
    failed = sum(1 for e in ledger if e["status"].startswith("FAILED"))
    incomplete = sum(1 for e in ledger if e["status"].startswith("INCOMPLETE"))
    summary = {"edition": ctx.edition.isoformat(), "window": [start.isoformat(), end.isoformat()],
               "registry_source_count": len(sources), "sources_fetched_terminal_count": len(ledger),
               "sources_checked_success_count": checked, "sources_failed_count": failed,
               "sources_incomplete_count": incomplete, "sources_pending_count": len(sources) - len(ledger),
               "raw_records": len(pool), "in_window": sum(1 for r in pool if r["window_check"] == "IN WINDOW"),
               "sources": ledger}
    save_json(ctx.work / "source_ledger.json", summary)
    ctx.report_append("s01 collect", f"registry {len(sources)}, checked {checked}, failed {failed}, incomplete {incomplete}; "
                                     f"raw records {len(pool)} ({summary['in_window']} in window).")
    ctx.set_stage("s01_collect", "done", raw_records=len(pool), checked=checked, failed=failed, incomplete=incomplete)
    return 0


if __name__ == "__main__":
    stage_main(run, __doc__)
