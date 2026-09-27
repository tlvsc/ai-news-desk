"""s04_classify: category, importance 1 to 10, verification status and one-line why-it-matters for every retained
event. Cheap model, batched, on digests only. Code enforces the label bands and the 11-category taxonomy.

Input: work/events.jsonl   Output: work/ranked.jsonl
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.common import log, read_jsonl, stage_main, write_jsonl  # noqa: E402
from lib.llm_client import LLMClient, batched  # noqa: E402


def run(ctx, extra_args=None) -> int:
    events = read_jsonl(ctx.work / "events.jsonl")
    if not events:
        log.error("no events.jsonl; run s03 first")
        return 1
    retained = [e for e in events if e["disposition"] == "RETAINED EVENT ID"]
    llm = LLMClient(ctx)
    size = ctx.config["llm"]["batch_sizes"].get("classify", 40)
    cats = [{"key": c["key"], "name": c["name"]} for c in ctx.category_order()]
    result = {}
    for batch in batched(retained, size):
        payload = {"categories": cats,
                   "scoring_rules": ["AI News Desk is an AI news channel, not a business channel: a large dollar figure alone never makes a story important.",
                                     "10 = CRITICAL: changes what AI can do, or affects many people, or a major government decision. 8-9 = HIGH. 6-7 = MEDIUM. 1-5 = WATCHLIST.",
                                     "Robotics means a robot or autonomous machine doing something, not a policy or a funding round about robots.",
                                     "verification: CONFIRMED (primary source or official), REPORTED (credible outlet, attributed), PRELIMINARY (early, unconfirmed), DISPUTED."],
                   "events": [{"id": e["id"], "headline": e["headline"], "summary": e["summary"], "key_facts": e["key_facts"],
                               "sources": e["sources"], "category_guess": e.get("category_guess"), "fun": e.get("fun", False)}
                              for e in batch]}
        reply = llm.call("cheap", "classify", payload, stage="s04_classify")
        for c in reply.get("classified", []):
            result[c["id"]] = c
    valid = {c["key"] for c in ctx.category_order()}
    out = []
    for e in retained:
        c = result.get(e["id"], {})
        score = int(c.get("importance") or 5)
        score = max(1, min(10, score))
        key = c.get("category") if c.get("category") in valid else ctx.category_key_from_name(c.get("category") or e.get("category_guess") or "")
        if e.get("fun") and key != "FUN" and score < 8:
            key = "FUN"
        cat = ctx.category_by_key(key)
        row = dict(e)
        row.update({"category": key, "category_name": cat["name"] if cat else key, "subcategory": c.get("subcategory", ""),
                    "importance": score, "label": ctx.importance_label(score),
                    "verification": c.get("verification") if c.get("verification") in ctx.categories["verification_statuses"] else "REPORTED",
                    "why_it_matters": c.get("why_it_matters", ""), "big_name": bool(c.get("big_name"))})
        out.append(row)
    out.sort(key=lambda r: (-r["importance"], [c["key"] for c in ctx.category_order()].index(r["category"]), r["id"]))
    write_jsonl(ctx.work / "ranked.jsonl", out)
    counts = {}
    for r in out:
        counts[r["label"]] = counts.get(r["label"], 0) + 1
    ctx.report_append("s04 classify", f"{len(out)} events classified: {counts}. Categories: "
                                      + ", ".join(f"{k}={sum(1 for r in out if r['category']==k)}" for k in valid))
    ctx.set_stage("s04_classify", "done", classified=len(out), **{k.lower(): v for k, v in counts.items()})
    return 0


if __name__ == "__main__":
    stage_main(run, __doc__)
