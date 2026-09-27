"""s08_bigger_picture: The Bigger Picture (approved names, 12 Sep 2026) from the bulletin only. Strong model, one call,
small input. Produces the full analysis doc, the card copy and the spoken reel line (44 to 53 syllables).

Input: work/bulletin.json   Output: reports/the bigger picture_<date>.md, work/bigger_picture.json
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.common import load_json, log, save_json, stage_main  # noqa: E402
from lib.llm_client import LLMClient  # noqa: E402
from lib.syllables import count  # noqa: E402


def run(ctx, extra_args=None) -> int:
    bul = load_json(ctx.work / "bulletin.json", default={})
    if not bul.get("items"):
        log.error("no bulletin.json; run s07 first")
        return 1
    cfg = ctx.config["cards"]
    lo, hi = ctx.config["headlines"]["bigger_picture_syllables"]
    llm = LLMClient(ctx)
    payload = {"corner_name": cfg["analysis_corner"], "full_name": f"{cfg['analysis_corner']} — Daily AI Analysis",
               "description": "What today’s developments could mean for technology, business and everyday life.",
               "opening": cfg["analysis_opening"], "spoken_syllables": [lo, hi],
               "rules": ["Desk judgement, clearly separated from reported facts; cite report item numbers.",
                         "No investment recommendation, price target or buy/sell language.", "Plain language law applies."],
               "items": [{"n": i["n"], "headline": i["bulletin_headline"], "body": i["bulletin_body"], "category": i["category_name"],
                          "key_facts": i["key_facts"][:3]} for i in bul["items"]]}
    reply = llm.call("strong", "bigger_picture", payload, stage="s08_bigger_picture")
    spoken = reply.get("spoken", "")
    syl = count(spoken)
    note = "" if lo <= syl <= hi else f"spoken line is {syl} syllables, outside {lo} to {hi}; s12 will ask for a rewrite"
    doc = ["# " + payload["full_name"], "", payload["description"], "",
           f"Edition: {ctx.edition.isoformat()}. Source: derived only from the same edition's Daily Bulletin and Full Report. Private production draft; not approved for publication. Not investment advice.",
           "", payload["opening"], "", reply.get("full_markdown", "").strip(), ""]
    (ctx.reports / f"the bigger picture_{ctx.edition.isoformat()}.md").write_text("\n".join(doc), encoding="utf-8")
    save_json(ctx.work / "bigger_picture.json", {"edition": ctx.edition.isoformat(), "head": reply.get("head", ""),
                                                 "card_body": reply.get("card_body", ""), "items": reply.get("items", []),
                                                 "spoken": spoken, "spoken_syllables": syl, "report_refs": reply.get("report_refs", []),
                                                 "note": note})
    ctx.report_append("s08 bigger picture", f"written; spoken line {syl} syllables. {note}")
    ctx.set_stage("s08_bigger_picture", "done", syllables=syl)
    return 0


if __name__ == "__main__":
    stage_main(run, __doc__)
