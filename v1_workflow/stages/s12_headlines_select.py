"""s12_headlines_select: the reel is the deck in miniature (Headlines blueprint V9.2, Section A, 25 Sep 2026).
Slot 1 stored intro (bypass); slots 2 to 8 seven story clips from the deck in deck order; 9 fun; 10 teaser from the
"More in the full report" card only; 11 The Bigger Picture (44 to 53 syllables); 12 stored ending (bypass).
Mid model writes the spoken lines with a rotating spoken introduction; code counts syllables (seconds = syllables / 4.4,
two decimals, no rounding up), loops for rewrites, checks digits, runs the meaning check. Ends with Rafael's spoken-copy
approval pause (exit 3).

Input: work/cards_selection.json, work/report_items.json, work/bigger_picture.json
Output: Headlines/supportive files/Headlines_<D-M-YY>_selection.md, headlines_<D-M-YY>_pack.json
"""
from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.common import RC_APPROVAL, load_json, log, require_approval, save_json, stage_main, update_checkpoint  # noqa: E402
from lib.llm_client import LLMClient  # noqa: E402
from lib.syllables import box_seconds, count  # noqa: E402

RULES = ["Every story and fun clip starts with a short natural spoken introduction suited to its subject; rotate wording, never yesterday's.",
         "Plain language law: short words, deed before money, unfamiliar companies get a short title, numbers as spoken words.",
         "Stories about 35 syllables (7 to 9 seconds at 4.4 syllables per second); The Bigger Picture 44 to 53 syllables.",
         "The teaser uses only the 'More in the full report' items, never a story that has its own clip.",
         "Only facts from the item. Never add a fact. Keep 'reportedly' or 'says' for REPORTED and PRELIMINARY items."]


def pick_core(deck_stories: list[dict], n: int, notes: list[str]) -> list[dict]:
    """Strongest n stories by score, keep robotics and one of law/research/society when present, then deck order."""
    ranked = sorted(deck_stories, key=lambda d: (-d["importance"], d["order"]))
    core = ranked[:n]
    def ensure(pred, name):
        nonlocal core
        if any(pred(d) for d in core):
            return
        cand = next((d for d in ranked if pred(d) and d not in core), None)
        if cand is None:
            notes.append(f"{name}: no such story in the deck.")
            return
        drop = next((d for d in reversed(core) if d["importance"] < 10 and not pred(d)), None)
        if drop is None:
            return
        core[core.index(drop)] = cand
        notes.append(f"{name}: swapped in item {cand['item_n']} for item {drop['item_n']} (blueprint Section A item 3).")
    ensure(lambda d: d["category"] == "ROB", "Robotics retained")
    ensure(lambda d: d["category"] in ("LAW", "RES", "SOC"), "Law, research or society included")
    return sorted(core, key=lambda d: d["order"])


def previous_intros(ctx) -> list[str]:
    out = []
    for i in range(1, 4):
        d = ctx.edition - dt.timedelta(days=i)
        f = ctx.local_root / d.isoformat() / ctx.config["products"]["headlines"] / ctx.config["products"]["supportive"] / f"headlines_{d.day}-{d.month}-{d.year % 100:02d}_pack.json"
        if f.exists():
            for s in load_json(f).get("slots", []):
                if s.get("script"):
                    out.append(s["script"].split(".")[0].split(",")[0].strip())
    return out


def run(ctx, extra_args=None) -> int:
    sel = load_json(ctx.work / "cards_selection.json", default={})
    rep = load_json(ctx.work / "report_items.json", default={})
    bp = load_json(ctx.work / "bigger_picture.json", default={})
    if not sel.get("deck") or not rep.get("items") or not bp.get("spoken"):
        log.error("need cards_selection.json, report_items.json and bigger_picture.json; run s06 to s09 first")
        return 1
    hcfg = ctx.config["headlines"]
    g = ctx.config["gates"]
    by_n = {i["n"]: i for i in rep["items"]}
    notes: list[str] = []
    stories = [d for d in sel["deck"] if d["kind"] == "story" and d["category"] != "FUN"]
    fun = next((d for d in sel["deck"] if d["kind"] == "story" and d["category"] == "FUN"), None)
    teaser_card = next(d for d in sel["deck"] if d["kind"] == "teaser")
    core = pick_core(stories, 7, notes)
    if len(core) < 7:
        notes.append(f"Only {len(core)} story clips available from the deck.")
    lo_s, hi_s = int(hcfg["story_box_min"] * hcfg["syllables_per_second"]), int(hcfg["story_box_max"] * hcfg["syllables_per_second"])
    lo_b, hi_b = hcfg["bigger_picture_syllables"]
    cues = hcfg.get("pronunciation_cues", {})
    items = []
    slot = 2
    slot_meta = {}
    for d in core:
        src = by_n[d["item_n"]]
        items.append({"id": f"C{slot:02d}", "kind": "story", "headline": src["headline"], "summary": src["summary"], "key_facts": src["key_facts"],
                      "category_name": d["category_name"], "source": d["source"], "verification": d["verification"],
                      "target_syllables": hcfg["story_target_syllables"], "range": [lo_s, hi_s]})
        slot_meta[f"C{slot:02d}"] = d
        slot += 1
    fun_slot = 9
    if fun:
        src = by_n[fun["item_n"]]
        items.append({"id": "C09", "kind": "fun", "headline": src["headline"], "summary": src["summary"], "key_facts": src["key_facts"],
                      "category_name": "Fun", "source": fun["source"], "verification": fun["verification"],
                      "target_syllables": hcfg["story_target_syllables"], "range": [lo_s, hi_s]})
        slot_meta["C09"] = fun
    else:
        notes.append("Fun slot 9 bypassed: no fun card in the deck. Notify Rafael.")
    items.append({"id": "C10", "kind": "teaser", "teaser_items": [{"headline": t["headline"], "category_name": t["category_name"]} for t in teaser_card["items"]],
                  "target_syllables": hcfg["story_target_syllables"], "range": [lo_s, hi_s]})
    items.append({"id": "C11", "kind": "bigger_picture", "headline": bp["head"], "summary": bp.get("card_body", ""), "key_facts": bp.get("items", []),
                  "current_spoken": bp["spoken"], "opening": ctx.config["cards"]["analysis_opening"].replace("…", ""), "range": [lo_b, hi_b],
                  "target_syllables": (lo_b + hi_b) // 2})
    llm = LLMClient(ctx)
    reply = llm.call("mid", "headlines_copy", {"rules": RULES, "previous_intros": previous_intros(ctx), "items": items}, stage="s12_headlines_select")
    scripts = {r["id"]: r for r in reply.get("items", [])}
    ranges = {it["id"]: it["range"] for it in items}

    def problems(sid: str) -> list[str]:
        s = scripts.get(sid, {}).get("script", "")
        out = []
        n = count(s, cues)
        lo, hi = ranges[sid]
        if not s:
            out.append("empty script")
        if n < lo:
            out.append(f"too short: {n} syllables, need {lo} to {hi}")
        if n > hi:
            out.append(f"too long: {n} syllables, need {lo} to {hi}")
        if re.search(r"\d", s):
            out.append("contains digits; every number must be spoken words")
        if sid == "C11" and not s.lower().startswith("and for the bigger picture"):
            out.append("must start with 'And for the bigger picture,'")
        return out

    for round_no in range(1, 3):
        fixes = [dict(it, fix={"current_script": scripts.get(it["id"], {}).get("script", ""),
                               "current_syllables": count(scripts.get(it["id"], {}).get("script", ""), cues),
                               "problem": "; ".join(problems(it["id"]))}) for it in items if problems(it["id"])]
        if not fixes:
            break
        log.info("rewrite round %d for %s", round_no, [f["id"] for f in fixes])
        rep2 = llm.call("mid", "headlines_copy", {"rules": RULES, "previous_intros": previous_intros(ctx), "items": fixes}, stage="s12_headlines_select")
        for r in rep2.get("items", []):
            scripts[r["id"]] = r
    check = llm.call("mid", "meaning_check", {"items": [
        {"id": it["id"], "source_facts": it["key_facts"] + [it["summary"]], "written": {"script": scripts.get(it["id"], {}).get("script", "")}}
        for it in items if it["kind"] in ("story", "fun")]}, stage="s12_headlines_select")
    results = {r["id"]: r for r in check.get("results", [])}
    slots = [{"slot": 1, "kind": "intro", "state": "bypass", "title": "stored intro, date composited in post"}]
    total = 0.0
    for it in items:
        sid = it["id"]
        s = scripts.get(sid, {})
        script = s.get("script", "")
        n = count(script, cues)
        box = box_seconds(n, hcfg["syllables_per_second"])
        probs = problems(sid)
        row = {"slot": int(sid[1:]), "kind": it["kind"], "category": it.get("category_name", "The Bigger Picture" if it["kind"] == "bigger_picture" else "Teaser"),
               "symbol": s.get("symbol", "the AI News Desk logo on the blue holographic screen, unchanged"), "script": script,
               "syllables": n, "box_seconds": box, "problems": probs}
        if sid in slot_meta:
            d = slot_meta[sid]
            row.update({"item": d["item_n"], "source": d["source"], "source_url": d["url"], "card": d["id"],
                        "meaning_check": results.get(sid, {}).get("result", "UNVERIFIED"), "meaning_note": results.get(sid, {}).get("note", "")})
        elif it["kind"] == "teaser":
            row.update({"source": "AI NEWS DESK", "items": [t["item_n"] for t in teaser_card["items"]], "card": teaser_card["id"]})
        else:
            row.update({"source": "AI NEWS DESK", "report_refs": bp.get("report_refs", [])})
        if probs:
            notes.append(f"{sid}: still outside the rules after two rewrites: {'; '.join(probs)}. Rafael decides.")
        slots.append(row)
        total += box
    if not fun:
        slots.append({"slot": 9, "kind": "fun", "state": "bypass", "title": "no fun story today"})
    slots.append({"slot": 12, "kind": "ending", "state": "bypass", "title": "stored approved ending"})
    slots.sort(key=lambda r: r["slot"])
    core_count = sum(1 for r in slots if 2 <= r["slot"] <= 10 and r.get("state") != "bypass")
    pack = {"edition": ctx.edition.isoformat(), "date_title": ctx.title_date, "lane": ctx.lane,
            "prompt_file": "config/headlines_comfy_prompt.txt (Headlines_prompt_for_comfy_json, Rafael 26 Sep 2026)",
            "cues": cues, "rate_syllables_per_second": hcfg["syllables_per_second"], "floor_seconds": 0, "hold_seconds": 0,
            "slots": slots, "ending": hcfg["approved_ending"],
            "bigger_picture": {"state": "render", "category": "The Bigger Picture", "regenerate": True,
                               "script": next(r["script"] for r in slots if r["slot"] == 11)},
            "content_seconds_excluding_open_close": round(total, 2), "core_count": core_count,
            "review_status": "PENDING Rafael's spoken-copy review (approvals/s12_headlines_select)",
            "source_check": "scripts derived from the Full Report items named per slot; meaning check results recorded per slot",
            "generation_authorized": False, "notes": notes}
    save_json(ctx.headlines_sup / f"headlines_{ctx.short}_pack.json", pack)
    md = [f"# Headlines_{ctx.short} — Selection and Script (not generated)", "",
          f"Edition {ctx.edition.isoformat()}. Source: the cards deck cards_{ctx.short}_selection.md, which comes from the Full Report. No new research. Stories keep deck order.",
          "Structure (Rafael, 25 Sep 2026): slots 2 to 8 seven news stories, 9 fun, 10 teaser, 11 The Bigger Picture; slot 1 stored intro, slot 12 approved ending.",
          f"Timing: seconds = syllables / {hcfg['syllables_per_second']}, two decimals, no rounding. Content excluding opening and ending: {total:.1f} s.",
          "Not generated, not QA-checked, not approved for publication.", ""]
    for r in slots:
        if r.get("state") == "bypass":
            md += [f"## Slot {r['slot']} — {r['kind']}: {r['title']}", ""]
            continue
        md += [f"## Slot {r['slot']} — {r['category']}" + (f" (item {r['item']})" if r.get("item") else ""),
               f"Script: \"{r['script']}\"", f"Syllables: {r['syllables']}. Box: {r['box_seconds']:.2f} s. Symbol: {r['symbol']}"]
        if r.get("meaning_check"):
            md.append(f"Meaning check: {r['meaning_check']} {r.get('meaning_note', '')}")
        if r["problems"]:
            md.append("PROBLEMS: " + "; ".join(r["problems"]))
        md.append("")
    if notes:
        md += ["## Notes for Rafael", ""] + [f"- {n}" for n in notes] + [""]
    text = "\n".join(md)
    (ctx.headlines_sup / f"Headlines_{ctx.short}_selection.md").write_text(text, encoding="utf-8")
    gate = "PASS" if g["headlines_core_min"] <= core_count <= g["headlines_core_max"] else "FAIL"
    ctx.set_gate("headlines_selection_gate", gate, f"{core_count} core clips")
    update_checkpoint(ctx, {"headlines_core_count": core_count}, {"headlines_selection_gate": gate})
    ctx.report_append("s12 headlines select", f"{core_count} core clips, {total:.1f} s content; {len(notes)} notes. LLM so far: {llm.summary()}")
    if gate == "FAIL":
        ctx.set_stage("s12_headlines_select", "failed", core=core_count)
        return 2
    if not require_approval(ctx, "s12_headlines_select", "spoken-copy review before the Comfy JSON is built", text):
        ctx.set_stage("s12_headlines_select", "awaiting_approval", core=core_count)
        return RC_APPROVAL
    pack["review_status"] = "Approved by Rafael (approvals/s12_headlines_select.approved)"
    save_json(ctx.headlines_sup / f"headlines_{ctx.short}_pack.json", pack)
    ctx.set_stage("s12_headlines_select", "done", core=core_count, seconds=round(total, 1))
    return 0


if __name__ == "__main__":
    stage_main(run, __doc__)
