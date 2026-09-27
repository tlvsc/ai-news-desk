"""s02_digest: read every raw article ONCE and reduce it to a tiny record (cheap model, batched).

This is the only stage that ever sees raw article text. Everything downstream works on digests.
Input:  work/raw_pool.jsonl        Output: work/digests.jsonl (raw fields minus text, plus digest fields)
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.common import log, read_jsonl, stage_main, write_jsonl  # noqa: E402
from lib.llm_client import LLMClient, batched  # noqa: E402


def run(ctx, extra_args=None) -> int:
    raw = read_jsonl(ctx.work / "raw_pool.jsonl")
    if not raw:
        log.error("no raw_pool.jsonl; run s01 first")
        return 1
    todo = [r for r in raw if r["window_check"] != "OUT OF WINDOW"]
    llm = LLMClient(ctx)
    size = ctx.config["llm"]["batch_sizes"].get("digest", 40)
    by_id = {}
    for batch in batched(todo, size):
        payload = {"edition": ctx.edition.isoformat(), "window": [ctx.window_start.isoformat(), ctx.window_end.isoformat()],
                   "items": [{"id": r["id"], "title": r["title"], "source": r["source_name"], "published": r.get("published"),
                              "url": r["url"], "category_hint": r.get("category_hint"),
                              "text": (r.get("text") or r.get("summary") or "")[: ctx.config["collector"].get("article_text_chars", 2500)]}
                             for r in batch]}
        reply = llm.call("cheap", "digest", payload, stage="s02_digest")
        for d in reply.get("digests", []):
            by_id[d["id"]] = d
    out = []
    missing = 0
    for r in raw:
        rec = {k: v for k, v in r.items() if k != "text"}
        d = by_id.get(r["id"])
        if r["window_check"] == "OUT OF WINDOW":
            rec["disposition"] = "OUT OF WINDOW"
        elif d is None:
            missing += 1
            rec["disposition"] = "HELD FOR REVIEW"
            rec["digest_note"] = "no digest returned"
        else:
            rec.update({"headline": d.get("headline") or r["title"], "summary": d.get("summary", ""),
                        "key_facts": d.get("key_facts", []), "entities": d.get("entities", []),
                        "event_date": d.get("event_date"), "fun": bool(d.get("fun")),
                        "category_guess": d.get("category_guess") or r.get("category_hint")})
            rec["disposition"] = "PENDING" if d.get("ai_relevant", True) else "NOT AI-RELEVANT"
        out.append(rec)
    write_jsonl(ctx.work / "digests.jsonl", out)
    pending = sum(1 for o in out if o["disposition"] == "PENDING")
    ctx.report_append("s02 digest", f"{len(todo)} items digested in batches of {size}; {pending} AI-relevant pending, "
                                    f"{missing} without digest (held). LLM so far: {llm.summary()}")
    ctx.set_stage("s02_digest", "done", digested=len(todo), pending=pending, missing=missing)
    return 0


if __name__ == "__main__":
    stage_main(run, __doc__)
