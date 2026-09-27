"""s07_bulletin: 25 to 30 articles from the Full Report only (18 Sep gate F), in the approved category order,
rewritten under the plain language law with the 26 Sep source-to-script meaning check. Mid model, two calls.

Input: work/report_items.json   Output: reports/<date> — Daily Bulletin.md, work/bulletin.json
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.common import load_json, log, save_json, stage_main, update_checkpoint  # noqa: E402
from lib.llm_client import LLMClient  # noqa: E402


def select(ctx, items: list[dict]) -> list[dict]:
    g = ctx.config["gates"]
    order = [c["key"] for c in ctx.category_order()]
    crit = [i for i in items if i["importance"] >= 10]
    high = [i for i in items if 8 <= i["importance"] < 10]
    med = [i for i in items if 6 <= i["importance"] < 8]
    chosen = crit + high
    # breadth: at least one per category where a medium exists
    have = {i["category"] for i in chosen}
    for m in sorted(med, key=lambda x: -x["importance"]):
        if m["category"] not in have and len(chosen) < g["bulletin_max"]:
            chosen.append(m)
            have.add(m["category"])
    for m in sorted(med, key=lambda x: -x["importance"]):
        if len(chosen) >= g["bulletin_min"]:
            break
        if m not in chosen:
            chosen.append(m)
    chosen = sorted(chosen, key=lambda x: -x["importance"])[: g["bulletin_max"]]
    crit = [i for i in chosen if i["importance"] >= 10]
    rest = sorted([i for i in chosen if i["importance"] < 10], key=lambda i: (order.index(i["category"]), -i["importance"]))
    return crit + rest


def run(ctx, extra_args=None) -> int:
    rep = load_json(ctx.work / "report_items.json", default={})
    items = rep.get("items", [])
    if not items:
        log.error("no report_items.json; run s06 first")
        return 1
    g = ctx.config["gates"]
    chosen = select(ctx, items)
    if not (g["bulletin_min"] <= len(chosen) <= g["bulletin_max"]):
        ctx.set_gate("bulletin_gate", "FAIL", f"{len(chosen)} items")
        ctx.report_append("s07 bulletin", f"BULLETIN GATE FAILED: {len(chosen)} items, need {g['bulletin_min']} to {g['bulletin_max']}.")
        ctx.set_stage("s07_bulletin", "failed", count=len(chosen))
        return 2
    llm = LLMClient(ctx)
    payload = {"law": "AIND plain language law v1: headline is a full spoken sentence; body is two sentences: what happened, then why it matters or the honest doubt; no jargon; numbers translated unless the number is the story; lead non-market stories with the deed, not the money; unfamiliar companies get a short title.",
               "items": [{"id": i["id"], "n": i["n"], "headline": i["headline"], "summary": i["summary"], "key_facts": i["key_facts"],
                          "category": i["category_name"], "source": i["source"], "verification": i["verification"]} for i in chosen]}
    reply = llm.call("mid", "bulletin_copy", payload, stage="s07_bulletin")
    copy = {c["id"]: c for c in reply.get("items", [])}
    check = llm.call("mid", "meaning_check", {"items": [{"id": i["id"], "source_facts": i["key_facts"] + [i["summary"]],
                                                          "written": copy.get(i["id"], {})} for i in chosen]}, stage="s07_bulletin")
    results = {r["id"]: r for r in check.get("results", [])}
    out, failed = [], []
    for i in chosen:
        c = copy.get(i["id"], {})
        r = results.get(i["id"], {"result": "UNVERIFIED"})
        row = dict(i)
        row.update({"bulletin_headline": c.get("headline") or i["headline"], "bulletin_body": c.get("body") or i["summary"],
                    "meaning_check": r.get("result", "UNVERIFIED"), "meaning_note": r.get("note", "")})
        out.append(row)  # failing rows stay in the bulletin flagged DRAFT for Rafael
        if row["meaning_check"] != "PASS":
            failed.append(row)
    counts = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0}
    for r in out:
        counts[r["label"]] = counts.get(r["label"], 0) + 1
    lines = [f"# {ctx.edition.isoformat()} — Daily Bulletin", "",
             f"Edition: {ctx.edition.isoformat()}. Source: derived only from the same edition's Daily Global AI Intelligence Report. Item numbers refer to that report. No new research.",
             f"Bulletin count: {len(out)} (gate: {g['bulletin_min']} to {g['bulletin_max']}). Critical: {counts.get('CRITICAL',0)}. High: {counts.get('HIGH',0)}. Medium: {counts.get('MEDIUM',0)}.",
             "Private production draft; not approved for publication.", ""]
    section = None
    for r in out:
        sec = "Critical" if r["importance"] >= 10 else r["category_name"]
        if sec != section:
            section = sec
            lines += [f"## {section}", ""]
        flag = "" if r["meaning_check"] == "PASS" else f"  (DRAFT: meaning check {r['meaning_check']} {r['meaning_note']})"
        lines += [f"### {r['n']}. {r['bulletin_headline']}{flag}", "", r["bulletin_body"], "",
                  f"Full Report item {r['n']} | {r['category_name']} | Score {r['importance']}/10 | {r['verification']} | {r['source']}", ""]
    (ctx.reports / f"{ctx.edition.isoformat()} — Daily Bulletin.md").write_text("\n".join(lines), encoding="utf-8")
    save_json(ctx.work / "bulletin.json", {"edition": ctx.edition.isoformat(), "count": len(out), "items": out})
    ctx.set_gate("bulletin_gate", "PASS", f"{len(out)} items, {len(failed)} meaning-check drafts")
    update_checkpoint(ctx, {"bulletin_count": len(out)}, {"bulletin_gate": "PASS"})
    ctx.report_append("s07 bulletin", f"{len(out)} bulletin items ({counts}); {len(failed)} kept as drafts after the meaning check.")
    ctx.set_stage("s07_bulletin", "done", count=len(out), drafts=len(failed))
    return 0


if __name__ == "__main__":
    stage_main(run, __doc__)
