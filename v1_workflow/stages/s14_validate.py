"""s14_validate: read-only QA of the filled Headlines workflow with the registered QA tool
(vendor/validate_delivery.py --headlines, the ChatGPT-lane validator) plus the pack-to-JSON consistency check.
Zero LLM. Never queues, never rewrites the JSON.

Input: Headlines/supportive files/headlines_<D-M-YY>_<lane>.json and headlines_<D-M-YY>_pack.json
Output: Headlines/supportive files/headlines_<D-M-YY>_validation.json. Exit 2 on FAIL.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.common import PKG_ROOT, load_json, log, save_json, stage_main  # noqa: E402

VALIDATOR = PKG_ROOT / "vendor" / "validate_delivery.py"


def blueprint_prompt_copy(ctx) -> Path:
    """The QA tool expects the Drive prompt with <article content> placeholders; ours uses {symbol} and {script}."""
    text = (PKG_ROOT / "config" / "headlines_comfy_prompt.txt").read_text(encoding="utf-8")
    text = text.replace("{symbol}", "<article content>").replace('"{script}"', '"<article content>"')
    out = ctx.work / "Headlines_prompt_for_comfy_json.txt"
    out.write_text(text, encoding="utf-8")
    return out


def consistency(wf: dict, pack: dict) -> list[str]:
    errors = []
    nodes = {n["id"]: n for n in wf["nodes"]}
    for row in pack["slots"]:
        s = row["slot"]
        active = row.get("state") != "bypass" and bool(row.get("script"))
        n12, n13 = nodes.get(s * 100 + 12), nodes.get(s * 100 + 13)
        if not n12 or not n13:
            errors.append(f"slot {s}: nodes missing in JSON")
            continue
        if active:
            if f'"{row["script"]}"' not in n12["widgets_values"][0]:
                errors.append(f"slot {s}: script in JSON differs from the pack")
            if n13["mode"] != 0:
                errors.append(f"slot {s}: active in pack but bypassed in JSON")
        elif n12["mode"] != 4:
            errors.append(f"slot {s}: bypassed in pack but active in JSON")
    if wf.get("extra", {}).get("aind_headlines", {}).get("edition") != pack["edition"]:
        errors.append("extra.aind_headlines edition differs from the pack")
    return errors


def run(ctx, extra_args=None) -> int:
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--comfy-url", default="", help="local ComfyUI backend for live asset checks (PC only)")
    args = p.parse_args(extra_args or [])
    wf_path = ctx.headlines_sup / f"headlines_{ctx.short}_{ctx.lane}.json"
    pack = load_json(ctx.headlines_sup / f"headlines_{ctx.short}_pack.json", default={})
    if not wf_path.exists() or not pack:
        log.error("need the filled JSON and the pack; run s12 and s13 first")
        return 1
    wf = load_json(wf_path)
    own = consistency(wf, pack)
    cmd = [sys.executable, str(VALIDATOR), "--headlines", str(wf_path), "--prompt", str(blueprint_prompt_copy(ctx))]
    if args.comfy_url:
        cmd += ["--comfy-url", args.comfy_url]
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    tool = {"exit": proc.returncode, "stdout": proc.stdout.strip(), "stderr": proc.stderr.strip()}
    try:
        tool["result"] = json.loads(proc.stdout) if proc.returncode == 0 else None
    except json.JSONDecodeError:
        tool["result"] = None
    result = {"edition": ctx.edition.isoformat(), "workflow": wf_path.name, "consistency_errors": own,
              "qa_tool": VALIDATOR.name, "qa_tool_exit": proc.returncode, "qa_tool_result": tool["result"],
              "qa_tool_errors": (proc.stderr or proc.stdout).strip() if proc.returncode != 0 else "",
              "result": "PASS" if proc.returncode == 0 and not own else "FAIL"}
    save_json(ctx.headlines_sup / f"headlines_{ctx.short}_validation.json", result)
    body = f"consistency errors: {len(own)}; QA tool exit {proc.returncode}."
    if own:
        body += "\n" + "\n".join(f"- {e}" for e in own)
    if proc.returncode != 0:
        body += "\nQA tool said:\n" + result["qa_tool_errors"][:3000]
    ctx.report_append("s14 validate", body)
    ctx.set_gate("headlines_json_validation", result["result"], body[:200])
    ctx.set_stage("s14_validate", "done" if result["result"] == "PASS" else "failed")
    if result["result"] != "PASS":
        log.error("VALIDATION FAILED:\n%s", body)
        return 2
    log.info("validation PASS: %s", tool["result"])
    return 0


if __name__ == "__main__":
    stage_main(run, __doc__)
