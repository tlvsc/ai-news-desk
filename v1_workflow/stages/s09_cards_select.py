"""s09_cards_select: the paper-first deck list (Cards Master Section 2, category order of 23 Sep 2026). Zero LLM.

Card 1 cover; every critical (a critical spends its category's slot); then the category order with its slot counts,
highest score fills a slot; market at most 3 story cards including criticals; robotics and fun normally required;
fun is always the last story card; then "More in the full report" (3 to 4 uncarded headlines), The Bigger Picture,
closing. Exactly gates.cards_count cards (15). Departures are recorded, never silent.

Input: work/report_items.json, work/bigger_picture.json
Output: work/cards_selection.json, cards/supportive files/cards_<D-M-YY>_selection.md
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.common import load_json, log, save_json, stage_main, update_checkpoint  # noqa: E402

MONEY = ("$", "billion", "million", "funding", "valuation", "revenue", "raises", "raised")


def select(ctx, items: list[dict], notes: list[str]) -> tuple[list[dict], list[dict]]:
    cats = ctx.categories
    g = ctx.config["gates"]
    order = ctx.category_order()
    keys = [c["key"] for c in order]
    story_slots = g["cards_count"] - 4  # cover, teaser, bigger picture, closing
    slots = {c["key"]: c["cards_slots"] for c in order}
    mkt_max = cats.get("market_max_including_criticals", 3)
    chosen: list[dict] = []
    used: set[str] = set()

    def mkt_count() -> int:
        return sum(1 for i in chosen if i["category"] == "MKT")

    def take(it: dict, why: str) -> None:
        chosen.append(dict(it, pick_reason=why))
        used.add(it["id"])
        slots[it["category"]] = max(0, slots.get(it["category"], 0) - 1)

    def room() -> int:
        return story_slots - reserve - len(chosen)

    # fun: reserved for the last story card
    fun_pool = [i for i in items if i["category"] == "FUN" or i.get("fun")]
    fun = max(fun_pool, key=lambda i: (i["importance"], -i["n"]), default=None)
    reserve = 1 if fun else 0
    if not fun and cats.get("fun_required"):
        notes.append("Fun: the report has no fun story; the fun slot is released to the next category. Notify Rafael.")
    fun_id = fun["id"] if fun else None

    # 1. criticals, score order, each spends its category slot
    crit = sorted([i for i in items if i["importance"] >= 10 and i["id"] != fun_id],
                  key=lambda i: (-i["importance"], keys.index(i["category"]), i["n"]))
    left_out = []
    for it in crit:
        if room() <= 0:
            left_out.append(it["n"])
            continue
        if it["category"] == "MKT" and mkt_count() >= mkt_max:
            notes.append(f"Critical item {it['n']} (market) left out: money cap of {mkt_max} story cards reached.")
            continue
        take(it, f"critical, spends the {it['category_name']} slot")

    if left_out:
        notes.append(f"{len(left_out)} critical items left out because the deck is full: items {left_out}. Rafael decides.")

    # 2. big release rule (10 Sep): a major release from a big company takes the first slot after the criticals
    big = [i for i in items if i["id"] not in used and i["category"] == "MOD" and i.get("big_name") and i["importance"] >= 8]
    if big and room() > 0 and slots["MOD"] > 0:
        take(max(big, key=lambda i: (i["importance"], -i["n"])), "big release rule: first slot after the criticals")
        notes.append("Big release rule applied (10 Sep): noted for the handoff.")

    # 3. category order with slot counts, highest score fills a slot (MEDIUM or better first)
    for c in order:
        if c["key"] == "FUN":
            continue
        pool = sorted([i for i in items if i["id"] not in used and i["category"] == c["key"] and i["importance"] >= 6],
                      key=lambda i: (-i["importance"], i["n"]))
        while slots[c["key"]] > 0 and pool and room() > 0:
            if c["key"] == "MKT" and mkt_count() >= mkt_max:
                break
            take(pool.pop(0), f"{c['name']} slot")

    # 4. still short: strongest remaining stories regardless of slot plan (money cap still holds)
    if room() > 0:
        rest = sorted([i for i in items if i["id"] not in used and i["id"] != fun_id],
                      key=lambda i: (-i["importance"], keys.index(i["category"]), i["n"]))
        for it in rest:
            if room() <= 0:
                break
            if it["category"] == "MKT" and mkt_count() >= mkt_max:
                continue
            take(it, "fill: strongest remaining story after the slot plan")
        if rest:
            notes.append("The category slot plan did not fill the deck; remaining slots were filled by score.")
    if fun:
        take(fun, "fun, always the last story card")

    # checks
    if cats.get("robotics_required") and not any(i["category"] == "ROB" for i in chosen):
        notes.append("Robotics: no robotics story carded (none in the report at MEDIUM or better). Notify Rafael.")
    non_biz = sum(1 for i in chosen if i["category"] != "MKT")
    if non_biz < cats.get("min_non_business_stories", 3):
        notes.append(f"Only {non_biz} non-market story cards; the deck reads money heavy. Notify Rafael.")
    for i in chosen:
        if i["category"] != "MKT" and any(w in i["headline"].lower() for w in MONEY):
            notes.append(f"Item {i['n']} ({i['category_name']}): headline mentions money; the copy stage must lead with the deed.")

    def sort_key(i: dict):
        if i["id"] == fun_id:
            return (3, 0, 0, i["n"])
        if i["pick_reason"].startswith("critical"):
            return (0, -i["importance"], keys.index(i["category"]), i["n"])
        if i["pick_reason"].startswith("big release"):
            return (1, 0, 0, i["n"])
        return (2, keys.index(i["category"]), -i["importance"], i["n"])
    chosen.sort(key=sort_key)

    # teaser: 3 to 4 uncarded headlines, distinct categories first, strongest first
    left = sorted([i for i in items if i["id"] not in used], key=lambda i: (-i["importance"], i["n"]))
    teaser, seen = [], set()
    for i in left:
        if i["category"] in seen:
            continue
        teaser.append(i)
        seen.add(i["category"])
        if len(teaser) == 4:
            break
    for i in left:
        if len(teaser) >= 3:
            break
        if i not in teaser:
            teaser.append(i)
    return chosen, teaser


def run(ctx, extra_args=None) -> int:
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--allow-short", default="", help="reason (Rafael's) to accept a deck with fewer than cards_count cards")
    args = p.parse_args(extra_args or [])
    rep = load_json(ctx.work / "report_items.json", default={})
    items = rep.get("items", [])
    if not items:
        log.error("no report_items.json; run s06 first")
        return 1
    bp = load_json(ctx.work / "bigger_picture.json", default={})
    if not bp.get("head"):
        log.error("no bigger_picture.json; run s08 first")
        return 1
    g = ctx.config["gates"]
    notes: list[str] = []
    chosen, teaser = select(ctx, items, notes)
    deck = [{"kind": "cover"}]
    for it in chosen:
        deck.append({"kind": "story", "item_n": it["n"], "event_id": it["id"], "category": it["category"],
                     "category_name": it["category_name"], "headline": it["headline"], "importance": it["importance"],
                     "label": it["label"], "verification": it["verification"], "source": it["source"], "url": it["url"],
                     "pick_reason": it["pick_reason"]})
    deck.append({"kind": "teaser", "title": ctx.config["cards"]["teaser_title"],
                 "items": [{"item_n": t["n"], "event_id": t["id"], "headline": t["headline"], "category": t["category"],
                            "category_name": t["category_name"]} for t in teaser]})
    deck.append({"kind": "bigger_picture", "head": bp["head"], "report_refs": bp.get("report_refs", [])})
    deck.append({"kind": "closing"})
    for k, d in enumerate(deck, 1):
        d["order"] = k
        d["id"] = f"I{k:02d}"
        d["file"] = f"cards_{ctx.short}_I{k:02d}_{ctx.lane}.png"
    mkt = sum(1 for d in deck if d["kind"] == "story" and d["category"] == "MKT")
    ok = len(deck) == g["cards_count"]
    if not ok and not args.allow_short:
        ctx.set_gate("cards_selection_gate", "FAIL", f"{len(deck)} cards planned, need {g['cards_count']}")
        ctx.report_append("s09 cards select", f"CARDS SELECTION GATE FAILED: {len(deck)} cards, need {g['cards_count']}. "
                                              f"Re-run with --allow-short \"reason\" only on Rafael's word.\n" + "\n".join(f"- {n}" for n in notes))
        ctx.set_stage("s09_cards_select", "failed", count=len(deck))
        return 2
    if not ok:
        notes.append(f"Deck accepted short at {len(deck)} cards on Rafael's word: {args.allow_short}")
    sel = {"edition": ctx.edition.isoformat(), "short": ctx.short, "lane": ctx.lane, "count": len(deck),
           "story_cards": len(chosen), "market_cards": mkt, "deck": deck, "notes": notes, "status": "planned, not rendered, not approved"}
    save_json(ctx.work / "cards_selection.json", sel)
    lines = [f"# cards_{ctx.short} — selection (paper-first list, Cards Master Section 2)", "",
             f"Edition {ctx.edition.isoformat()}. Source: the Full Report only. Order: criticals by score, then the 23 Sep category order, fun last.",
             f"Cards: {len(deck)}. Story cards: {len(chosen)}. Market cards including criticals: {mkt} (cap {ctx.categories.get('market_max_including_criticals', 3)}).",
             "Not rendered, not approved for publication.", ""]
    for d in deck:
        if d["kind"] == "story":
            lines.append(f"{d['order']:>2}. {d['id']}  [{d['label']} {d['importance']}/10] {d['category_name']} — item {d['item_n']}: {d['headline']}  ({d['pick_reason']})")
        elif d["kind"] == "teaser":
            lines.append(f"{d['order']:>2}. {d['id']}  {d['title']}: " + "; ".join(f"item {t['item_n']} {t['category_name']}" for t in d["items"]))
        elif d["kind"] == "bigger_picture":
            lines.append(f"{d['order']:>2}. {d['id']}  The Bigger Picture: {d['head']}")
        else:
            lines.append(f"{d['order']:>2}. {d['id']}  {d['kind']}")
    if notes:
        lines += ["", "## Notes for Rafael", ""] + [f"- {n}" for n in notes]
    (ctx.cards_sup / f"cards_{ctx.short}_selection.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    ctx.set_gate("cards_selection_gate", "PASS", f"{len(deck)} cards, {mkt} market")
    update_checkpoint(ctx, {"cards_planned_count": len(deck)}, {"cards_selection_gate": "PASS"})
    ctx.report_append("s09 cards select", f"{len(deck)} cards planned ({len(chosen)} stories, {mkt} market). Teaser items: "
                                          f"{[t['n'] for t in teaser]}.\n" + "\n".join(f"- {n}" for n in notes))
    ctx.set_stage("s09_cards_select", "done", count=len(deck), stories=len(chosen), market=mkt)
    return 0


if __name__ == "__main__":
    stage_main(run, __doc__)
