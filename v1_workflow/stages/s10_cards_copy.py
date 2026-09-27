"""s10_cards_copy: the card copy for the planned deck. Mid model writes story and teaser copy in one batch
(or a few), then the meaning check. Code fills cover, The Bigger Picture and closing from config and s08.
Ends with Rafael's approval pause (house rule 4): exit 3 until approvals/s10_cards_copy.approved exists.

Input: work/cards_selection.json, work/report_items.json, work/bigger_picture.json
Output: cards/supportive files/cards_<D-M-YY>_copy.json and cards_<D-M-YY>_copy.md
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.common import RC_APPROVAL, load_json, log, long_date, require_approval, save_json, stage_main  # noqa: E402
from lib.llm_client import LLMClient, batched  # noqa: E402

LAW = ("AIND plain language law v1: head is one full spoken sentence ending with a period; body is exactly two "
       "sentences, what happened then why it matters or the honest doubt; no jargon; numbers translated unless the "
       "number is the story; non-market cards lead with the deed, never the money; unfamiliar companies get a short title.")
MONEY = re.compile(r"\$|\b(billion|million|funding|valuation|revenue|raises|raised|shares|stock)\b", re.I)


def sentences(text: str) -> int:
    return len([s for s in re.split(r"(?<=[.!?])\s+", (text or "").strip()) if s])


def run(ctx, extra_args=None) -> int:
    sel = load_json(ctx.work / "cards_selection.json", default={})
    rep = load_json(ctx.work / "report_items.json", default={})
    bp = load_json(ctx.work / "bigger_picture.json", default={})
    if not sel.get("deck") or not rep.get("items"):
        log.error("need cards_selection.json and report_items.json; run s06 to s09 first")
        return 1
    by_n = {i["n"]: i for i in rep["items"]}
    cfg = ctx.config["cards"]
    llm = LLMClient(ctx)
    stories = [d for d in sel["deck"] if d["kind"] == "story"]
    teaser_card = next(d for d in sel["deck"] if d["kind"] == "teaser")
    written, tlines = {}, {}
    size = ctx.config["llm"]["batch_sizes"].get("copy", 20)
    for k, batch in enumerate(batched(stories, size)):
        payload = {"law": LAW, "rules": ["Cards Master Section 3: lead with the deed; unfamiliar companies titled; "
                                         "keep the verification wording; category line 'Category / topic'."],
                   "items": [{"id": d["id"], "n": d["item_n"], "headline": by_n[d["item_n"]]["headline"],
                              "summary": by_n[d["item_n"]]["summary"], "key_facts": by_n[d["item_n"]]["key_facts"],
                              "category_name": d["category_name"], "source": d["source"], "verification": d["verification"],
                              "importance": d["importance"], "label": d["label"]} for d in batch],
                   "teaser": [{"id": f"T{t['item_n']}", "n": t["item_n"], "headline": t["headline"], "category_name": t["category_name"]}
                              for t in teaser_card["items"]] if k == 0 else []}
        reply = llm.call("mid", "cards_copy", payload, stage="s10_cards_copy")
        for c in reply.get("cards", []):
            written[c["id"]] = c
        for t in reply.get("teaser", []):
            tlines[t["id"]] = t
    check = llm.call("mid", "meaning_check", {"items": [
        {"id": d["id"], "source_facts": by_n[d["item_n"]]["key_facts"] + [by_n[d["item_n"]]["summary"]],
         "written": {"head": written.get(d["id"], {}).get("head", ""), "body": written.get(d["id"], {}).get("body", "")}}
        for d in stories]}, stage="s10_cards_copy")
    results = {r["id"]: r for r in check.get("results", [])}
    flags: list[str] = []
    cards = []
    for d in sel["deck"]:
        base = {"order": d["order"], "id": d["id"], "file": d["file"], "kind": d["kind"]}
        if d["kind"] == "cover":
            base.update({"title": "TODAY IN AI", "subtitle": "in cards", "date": long_date(ctx.edition), "date_title": ctx.title_date})
        elif d["kind"] == "story":
            w = written.get(d["id"], {})
            r = results.get(d["id"], {"result": "UNVERIFIED", "note": "no check result"})
            src = by_n[d["item_n"]]
            head = w.get("head") or src["headline"].rstrip(".") + "."
            body = w.get("body") or src["summary"]
            base.update({"head": head, "body": body, "cat": w.get("cat") or f"{d['category_name']} / {src.get('subcategory') or 'today'}",
                         "src": (w.get("src") or d["source"] or "SOURCE").upper(), "pill": d["verification"], "item_n": d["item_n"],
                         "url": d["url"], "category": d["category"], "category_name": d["category_name"], "importance": d["importance"],
                         "meaning_check": r.get("result", "UNVERIFIED"), "meaning_note": r.get("note", "")})
            if r.get("result") != "PASS":
                flags.append(f"{d['id']} item {d['item_n']}: meaning check {r.get('result')}: {r.get('note', '')} {r.get('unsupported', '')}")
            if sentences(body) != 2:
                flags.append(f"{d['id']}: body has {sentences(body)} sentences, the law says two.")
            if d["category"] != "MKT" and MONEY.search(head):
                flags.append(f"{d['id']}: non-market head mentions money; lead with the deed.")
        elif d["kind"] == "teaser":
            lines = []
            for t in d["items"]:
                tl = tlines.get(f"T{t['item_n']}", {})
                lines.append({"item_n": t["item_n"], "head": tl.get("head") or t["headline"].rstrip(".") + ".",
                              "cat": tl.get("cat") or t["category_name"]})
            base.update({"title": d["title"], "lines": lines, "closing_line": cfg["teaser_closing_line"],
                         "src": "DAILY GLOBAL AI INTELLIGENCE REPORT"})
        elif d["kind"] == "bigger_picture":
            base.update({"opening": cfg["analysis_opening"], "head": bp["head"], "body": bp.get("card_body", ""),
                         "items": bp.get("items", []), "pill": "DESK VIEW", "src": "AI NEWS DESK", "cat": f"{cfg['analysis_corner']} / Desk view",
                         "report_refs": bp.get("report_refs", [])})
        else:
            base.update({"head": cfg["closing_head"], "body": cfg["closing_body"]})
        cards.append(base)
    out = {"edition": ctx.edition.isoformat(), "short": ctx.short, "lane": ctx.lane, "date_title": ctx.title_date,
           "date_long": long_date(ctx.edition), "notice": cfg["notice"], "count": len(cards), "cards": cards, "flags": flags,
           "status": "draft copy; pending Rafael's approval; not rendered; not approved for publication"}
    path = ctx.cards_sup / f"cards_{ctx.short}_copy.json"
    save_json(path, out)
    md = [f"# cards_{ctx.short} — copy (draft)", "", f"Edition {ctx.edition.isoformat()}. {len(cards)} cards. Source: Full Report only.", ""]
    for c in cards:
        md.append(f"## {c['id']}  {c['kind']}")
        if c["kind"] == "story":
            md += [f"**{c['head']}**", "", c["body"], "", f"{c['cat']} | {c['src']} | {c['pill']} | report item {c['item_n']} | meaning check {c['meaning_check']}", ""]
        elif c["kind"] == "teaser":
            md += [f"**{c['title']}**", ""] + [f"- {l['head']}  ({l['cat']}, item {l['item_n']})" for l in c["lines"]] + ["", c["closing_line"], ""]
        elif c["kind"] == "bigger_picture":
            md += [c["opening"], f"**{c['head']}**", "", c["body"], ""] + [f"- {i}" for i in c["items"]] + ["", f"{c['pill']} | {c['src']}", ""]
        elif c["kind"] == "cover":
            md += [f"{c['title']} {c['subtitle']} — {c['date']}", ""]
        else:
            md += [f"**{c['head']}**", "", c["body"], ""]
    if flags:
        md += ["## Flags", ""] + [f"- {f}" for f in flags] + [""]
    text = "\n".join(md)
    (ctx.cards_sup / f"cards_{ctx.short}_copy.md").write_text(text, encoding="utf-8")
    ctx.report_append("s10 cards copy", f"copy written for {len(cards)} cards; {len(flags)} flags. LLM so far: {llm.summary()}")
    if not require_approval(ctx, "s10_cards_copy", "card copy review before rendering", text):
        ctx.set_stage("s10_cards_copy", "awaiting_approval", flags=len(flags))
        log.warning("APPROVAL NEEDED: read %s", ctx.approvals / "s10_cards_copy.pending.md")
        return RC_APPROVAL
    out["status"] = "copy approved by Rafael (approvals/s10_cards_copy.approved); not rendered; not approved for publication"
    save_json(path, out)
    ctx.set_stage("s10_cards_copy", "done", flags=len(flags), approved=True)
    return 0


if __name__ == "__main__":
    stage_main(run, __doc__)
