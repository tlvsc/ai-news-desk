"""s13_headlines_fill: fill the ComfyUI master workflow template from the approved pack. Zero LLM.
Generalised from Drive claude_files_only/fill_headlines_26-9-26.py (Section C of the Headlines blueprint).

Changes ONLY: slot scripts (node 100k+12), seconds (+13), output prefixes (+21, +35), slot modes, group titles,
MarkdownNote 9990, workflow id. Never LoRA, steps, seed, references, voice, links or node count. Nodes are found
by id (slot k owns 100k..100k+99), never by canvas position. Prints and saves the twelve-slot table, the config line,
the mirror check and the stale-word scan. Output is never overwritten: an existing file is renamed *_old first.

Input: Headlines/supportive files/headlines_<D-M-YY>_pack.json, the template (--template or headlines.comfy_template)
Output: Headlines/supportive files/headlines_<D-M-YY>_<lane>.json, headlines_<D-M-YY>_fill_receipt.md
"""
from __future__ import annotations

import copy as cp
import hashlib
import json
import re
import sys
import uuid
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.common import PKG_ROOT, load_json, log, rename_old, stage_main  # noqa: E402
from lib.syllables import box_seconds, count  # noqa: E402

PROMPT_FILE = PKG_ROOT / "config" / "headlines_comfy_prompt.txt"
NAMED_KEY = {"PrimitiveStringMultiline": "value", "PrimitiveFloat": "value", "SaveVideo": "filename_prefix", "MarkdownNote": "text"}


def set_widget(node: dict, idx: int, value):
    old = node["widgets_values"][idx]
    node["widgets_values"][idx] = value
    named = node.get("widgets_values_named")
    if isinstance(named, dict):
        key = NAMED_KEY.get(node["type"])
        if idx == 0 and key in named:
            named[key] = value
        else:
            for k, v in named.items():
                if v == old:
                    named[k] = value
    return old


def fill(wf: dict, pack: dict, prompt_tpl: str, template_sha: str) -> tuple[dict, list[tuple], list[str]]:
    orig = cp.deepcopy(wf)
    nodes = {n["id"]: n for n in wf["nodes"]}
    date, edition, lane = pack["date_title"], pack_short(pack), pack["lane"]
    cues = pack.get("cues", {})
    table, old_scripts = [], []
    for slot in pack["slots"]:
        s = slot["slot"]
        ids = {o: nodes.get(s * 100 + o) for o in (12, 13, 21, 35)}
        if any(v is None for v in ids.values()):
            raise AssertionError(f"slot {s}: template lacks nodes {[s*100+o for o,v in ids.items() if v is None]}")
        active = slot.get("state") != "bypass" and bool(slot.get("script"))
        for n in wf["nodes"]:
            if s * 100 <= n["id"] < s * 100 + 100:
                n["mode"] = 0 if active else 4
        if active:
            syl = count(slot["script"], cues)
            box = box_seconds(syl, pack["rate_syllables_per_second"])
            prompt = prompt_tpl.replace("{symbol}", slot["symbol"].rstrip(".")).replace("{script}", slot["script"])
            old_scripts.append(set_widget(ids[12], 0, prompt))
            set_widget(ids[13], 0, box)
            set_widget(ids[21], 0, f"video/headlines_{edition}_C{s:02d}_{lane}_544")
            set_widget(ids[35], 0, f"video/headlines_{edition}_C{s:02d}_{lane}_1088")
            name = slot.get("category", slot["kind"])
        else:
            syl, box = 0, 0.0
            old_scripts.append(set_widget(ids[12], 0, ""))
            set_widget(ids[13], 0, 0.0)
            set_widget(ids[21], 0, "")
            set_widget(ids[35], 0, "")
            name = slot.get("title", "bypassed")
        for n in ids.values():
            n["title"] = f"{date} C{s:02d} {name}"
        for gr in wf.get("groups", []):
            if re.search(rf"\bCLIP\s*0*{s}\b", gr.get("title", ""), re.I):
                gr["title"] = f"{date} CLIP {s:02d} {name} {box:.2f}s" if active else f"{date} CLIP {s:02d} BYPASSED"
        table.append((s, "ACTIVE" if active else "BYPASS", box, syl, slot["kind"], name))
    wf["id"] = str(uuid.uuid4())
    wf.setdefault("extra", {})["aind_fill"] = {"edition": pack["edition"], "template_sha256": template_sha,
                                               "blueprint": "Headlines_Master_Rules_Structure.txt", "prompt_file": pack["prompt_file"],
                                               "review_status": pack["review_status"], "source_check": pack["source_check"],
                                               "generation_authorized": bool(pack.get("generation_authorized")),
                                               "bigger_picture": pack.get("bigger_picture", {})}
    wf["extra"]["aind_headlines"] = {k: pack[k] for k in ("edition", "date_title", "lane", "slots")}
    if 9990 in nodes:
        note = f"{date} Headlines fill (Claude lane {lane}). Slots: " + "; ".join(f"C{t[0]:02d} {t[5]} {t[2]:.2f}s" for t in table)
        note += "\nC01 and C12 reuse the stored opening and approved ending.\n" + pack["review_status"] + "\n" + pack["source_check"]
        set_widget(nodes[9990], 0, note)
    # protections (blueprint Section C)
    checks: list[str] = []
    original = {n["id"]: n for n in orig["nodes"]}
    protected = [n["id"] for n in orig["nodes"] if n["id"] < 100 or n["id"] == 9991]
    assert all(nodes[i] == original[i] for i in protected), "Protected configuration changed"
    assert wf["links"] == orig["links"] and len(wf["nodes"]) == len(orig["nodes"]), "Topology changed"
    if 11 in nodes and isinstance(nodes[11].get("widgets_values_named"), dict) and "steps" in nodes[11]["widgets_values_named"]:
        assert nodes[11]["widgets_values"][1] == nodes[11]["widgets_values_named"]["steps"] == 6, "steps must stay 6 and mirrored"
        checks.append("steps 6 mirrored")
    if 6 in nodes and 7 in nodes:
        assert nodes[6]["widgets_values"][0] == nodes[7]["widgets_values"][0], "Reference images differ"
        checks.append("reference images agree")
    links = {l[0]: l for l in wf["links"]}
    spectrum = next((n for n in wf["nodes"] if n.get("type") == "SpectrumApplyMiniMaxH3"), None)
    if spectrum is not None:
        assert spectrum["mode"] == 0 and spectrum["widgets_values"][0] is True, "Spectrum node must be enabled"
        assert links[spectrum["inputs"][0]["link"]][1] == 2, "Spectrum input must follow LoRA"
        checks.append(f"Spectrum connected and enabled (node {spectrum['id']})")
    else:
        checks.append("SPECTRUM MISSING: use the master template that carries the Spectrum node (25 Sep 2026)")
    for row in pack["slots"]:
        base = row["slot"] * 100
        active = row.get("state") != "bypass" and bool(row.get("script"))
        assert all(n["mode"] == (0 if active else 4) for n in wf["nodes"] if base <= n["id"] < base + 100), f"slot {row['slot']} mode mismatch"
        if active:
            if spectrum is not None and (base + 16) in nodes:
                guider = next(i["link"] for i in nodes[base + 16]["inputs"] if i["name"] == "model")
                assert links[guider][1] == spectrum["id"], f"slot {row['slot']}: generation bypasses Spectrum"
            if (base + 32) in nodes:
                latent = next(i["link"] for i in nodes[base + 32]["inputs"] if i["name"] == "latent")
                assert links[latent][1] == base + 17, f"slot {row['slot']}: upscale must follow the generated latent"
            assert nodes[base + 13]["widgets_values"][0] == round(count(row["script"], cues) / pack["rate_syllables_per_second"], 2)
            assert "hands, body and head movements" in nodes[base + 12]["widgets_values"][0]
            assert "<reference image 01>" in nodes[base + 12]["widgets_values"][0]
        for offset, key in ((12, "value"), (13, "value"), (21, "filename_prefix"), (35, "filename_prefix")):
            node = nodes[base + offset]
            if isinstance(node.get("widgets_values_named"), dict):
                assert node["widgets_values_named"][key] == node["widgets_values"][0], f"node {base+offset}: visible/named mismatch"
    bad = [n["id"] for n in wf["nodes"] if isinstance(n.get("widgets_values_named"), dict) and n.get("widgets_values")
           and not all(v in n["widgets_values"] for v in n["widgets_values_named"].values() if isinstance(v, (str, int, float)))]
    checks.append("mirror: all agree" if not bad else f"MIRROR MISMATCH on nodes {bad}")
    dump = json.dumps(wf, ensure_ascii=False)
    stale = sorted({w for o in old_scripts if o for w in re.findall(r'"([^"]{20,})"', o) if w in dump and w not in json.dumps(pack)})
    checks.append("stale words: none" if not stale else f"OLD SCRIPT TEXT STILL PRESENT: {stale[:3]}")
    return wf, table, checks


def pack_short(pack: dict) -> str:
    y, m, d = pack["edition"].split("-")
    return f"{int(d)}-{int(m)}-{y[2:]}"


def run(ctx, extra_args=None) -> int:
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--template", default=ctx.config["headlines"].get("comfy_template", ""))
    args = p.parse_args(extra_args or [])
    pack_path = ctx.headlines_sup / f"headlines_{ctx.short}_pack.json"
    pack = load_json(pack_path, default={})
    if not pack.get("slots"):
        log.error("no pack at %s; run s12 first", pack_path)
        return 1
    if "Approved" not in pack.get("review_status", ""):
        log.error("pack not approved (review_status: %s); approve s12 first", pack.get("review_status"))
        return 3
    if not args.template or not Path(args.template).exists():
        log.error("template not found: %r. Set headlines.comfy_template in config (Drive ID 1iGUq1LtGtVm1toPhDTqhWOC4qIjIe2xV) or pass --template", args.template)
        return 4
    tpl = Path(args.template)
    wf = json.loads(tpl.read_text(encoding="utf-8"))
    template_sha = hashlib.sha256(tpl.read_bytes()).hexdigest()
    n_nodes, n_links = len(wf["nodes"]), len(wf.get("links", []))
    try:
        wf, table, checks = fill(wf, pack, PROMPT_FILE.read_text(encoding="utf-8"), template_sha)
    except AssertionError as exc:
        log.error("FILL CHECK FAILED: %s", exc)
        ctx.report_append("s13 headlines fill", f"FAILED: {exc}")
        ctx.set_stage("s13_headlines_fill", "failed", error=str(exc))
        return 2
    out = ctx.headlines_sup / f"headlines_{ctx.short}_{ctx.lane}.json"
    old = rename_old(out)
    out.write_text(json.dumps(wf, ensure_ascii=False, indent=2), encoding="utf-8")
    n11 = next((n for n in wf["nodes"] if n["id"] == 11), None)
    steps = n11["widgets_values"][1] if n11 else "?"
    lora = next((n["widgets_values"][0] for n in wf["nodes"] if "lora" in n.get("type", "").lower()), "?")
    seed = next((v for n in wf["nodes"] for v in n.get("widgets_values", []) if v == 1060749754396562), "NOT FOUND")
    gen = sum(t[2] for t in table if t[1] == "ACTIVE")
    lines = [f"# headlines_{ctx.short} fill receipt", "", f"WRITTEN {out.name}" + (f" (previous renamed {old.name})" if old else ""),
             f"template {tpl.name} sha256 {template_sha[:16]}…; nodes {len(wf['nodes'])} (template {n_nodes}), links {len(wf['links'])} (template {n_links})",
             f"CONFIG lora={lora} steps={steps} seed={seed}", "", "SLOT  STATE   BOX   SYL  KIND            NAME"]
    lines += [f"C{t[0]:02d}   {t[1]:6} {t[2]:6.2f} {t[3]:4d}  {t[4]:15} {t[5]}" for t in table]
    lines += [f"TOTAL generated {gen:.1f}s over {sum(1 for t in table if t[1]=='ACTIVE')} boxes", ""] + [f"- {c}" for c in checks]
    lines += ["", f"generation_authorized: {pack.get('generation_authorized')} (s15 asks Rafael before queueing)"]
    text = "\n".join(lines) + "\n"
    (ctx.headlines_sup / f"headlines_{ctx.short}_fill_receipt.md").write_text(text, encoding="utf-8")
    print(text)
    ctx.report_append("s13 headlines fill", text)
    ctx.set_stage("s13_headlines_fill", "done", output=str(out), generated_seconds=round(gen, 1))
    return 0


if __name__ == "__main__":
    stage_main(run, __doc__)
