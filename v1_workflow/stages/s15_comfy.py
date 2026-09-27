"""s15_comfy (PC only): queue the validated Headlines workflow on the local ComfyUI, wait, inventory the clips.
Zero LLM. Needs Rafael's generation "go" (approvals/s15_comfy.approved) and never queues the same edition twice:
the generation record in the pack is the lock.

The UI workflow is converted to the API graph with the server's /object_info (widgets_values_named first, positional
fallback), bypassed nodes are left out, the graph is stored in extra.aind_run.api_graph (what the QA tool checks).
Then POST /prompt, poll /history/<id>, and run the QA tool's clip inventory (vendor/validate_delivery.py) with ffprobe.

Output: Headlines/supportive files/headlines_<D-M-YY>_api.json, generation record in the pack,
        Headlines_<D-M-YY>_clip_inventory.json. Exit 4 when ComfyUI is not reachable (wrong machine).
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import sys
import time
import urllib.error
import urllib.request
import uuid
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.common import PKG_ROOT, RC_APPROVAL, RC_EXTERNAL, load_json, log, require_approval, save_json, stage_main  # noqa: E402

WIDGET_TYPES = {"INT", "FLOAT", "STRING", "BOOLEAN"}
FRONTEND_ONLY = {"MarkdownNote", "Note", "PrimitiveNode", "Reroute"}
CONTROL_VALUES = {"fixed", "increment", "decrement", "randomize"}


def http(url: str, data: dict | None = None, timeout: int = 30):
    req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8") if data is not None else None,
                                 headers={"Content-Type": "application/json"} if data is not None else {})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def ui_to_api(wf: dict, object_info: dict) -> dict:
    nodes = {n["id"]: n for n in wf["nodes"]}
    links = {l[0]: l for l in wf.get("links", [])}
    api = {}
    for n in wf["nodes"]:
        if n.get("mode", 0) != 0 or n["type"] in FRONTEND_ONLY:
            continue
        info = object_info.get(n["type"])
        if info is None:
            raise ValueError(f"node {n['id']} type {n['type']} is unknown to this ComfyUI (missing custom node?)")
        spec = {}
        for section in ("required", "optional"):
            spec.update(info.get("input", {}).get(section, {}))
        inputs, linked = {}, set()
        for inp in n.get("inputs", []):
            if inp.get("link") is None:
                continue
            l = links[inp["link"]]
            if nodes[l[1]].get("mode", 0) != 0:
                raise ValueError(f"node {n['id']} takes input from bypassed node {l[1]}")
            inputs[inp["name"]] = [str(l[1]), l[2]]
            linked.add(inp["name"])
        widget_names = [k for k, v in spec.items() if k not in linked and (isinstance(v[0], list) or v[0] in WIDGET_TYPES)]
        named = n.get("widgets_values_named")
        wv = list(n.get("widgets_values", []))
        if isinstance(named, dict) and all(k in named for k in widget_names):
            for k in widget_names:
                inputs[k] = named[k]
        else:
            i = 0
            for k in widget_names:
                if i >= len(wv):
                    break
                inputs[k] = wv[i]
                i += 1
                if spec[k][0] == "INT" and k in ("seed", "noise_seed") and i < len(wv) and wv[i] in CONTROL_VALUES:
                    i += 1
        api[str(n["id"])] = {"class_type": n["type"], "inputs": inputs, "_meta": {"title": n.get("title", n["type"])}}
    return api


def run(ctx, extra_args=None) -> int:
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--inventory-only", action="store_true", help="skip queueing; only inventory the output folder")
    p.add_argument("--max-hours", type=float, default=3.0)
    args = p.parse_args(extra_args or [])
    hcfg = ctx.config["headlines"]
    pack_path = ctx.headlines_sup / f"headlines_{ctx.short}_pack.json"
    wf_path = ctx.headlines_sup / f"headlines_{ctx.short}_{ctx.lane}.json"
    pack = load_json(pack_path, default={})
    val = load_json(ctx.headlines_sup / f"headlines_{ctx.short}_validation.json", default={})
    if not pack or not wf_path.exists():
        log.error("need pack and filled JSON; run s12 to s14 first")
        return 1
    if val.get("result") != "PASS":
        log.error("s14 validation is not PASS; not queueing")
        return 2
    url = hcfg["comfy_url"].rstrip("/")
    out_root = Path(hcfg.get("comfy_output_root") or Path(hcfg["comfy_output_dir"]).parent)
    record = pack.get("generation_record", {})
    if not args.inventory_only and record.get("state") != "accepted":
        summary = "\n".join(f"- C{s['slot']:02d} {s.get('category','')}: {s['box_seconds']:.2f} s — {s['script']}"
                            for s in pack["slots"] if s.get("script"))
        if not require_approval(ctx, "s15_comfy", "generation go for ComfyUI (GPU time, MiniMax H3)", summary):
            ctx.set_stage("s15_comfy", "awaiting_approval")
            return RC_APPROVAL
        try:
            object_info = http(f"{url}/object_info", timeout=60)
        except (urllib.error.URLError, OSError) as exc:
            log.error("ComfyUI not reachable at %s (%s). Run this stage on the production PC with ComfyUI open.", url, exc)
            ctx.set_stage("s15_comfy", "external_pending", reason=str(exc))
            return RC_EXTERNAL
        wf = load_json(wf_path)
        api = ui_to_api(wf, object_info)
        api_path = ctx.headlines_sup / f"headlines_{ctx.short}_api.json"
        save_json(api_path, api)
        client_id = str(uuid.uuid4())
        wf.setdefault("extra", {})["aind_run"] = {"api_graph": api, "client_id": client_id,
                                                  "prepared_at": dt.datetime.now(dt.timezone.utc).isoformat()}
        wf_path.write_text(json.dumps(wf, ensure_ascii=False, indent=2), encoding="utf-8")
        resp = http(f"{url}/prompt", {"prompt": api, "client_id": client_id}, timeout=120)
        record = {"state": "accepted" if not resp.get("node_errors") else "rejected", "client_id": client_id,
                  "ui_sha256": hashlib.sha256(wf_path.read_bytes()).hexdigest(), "api_sha256": hashlib.sha256(api_path.read_bytes()).hexdigest(),
                  "clip_ids": [f"C{s['slot']:02d}" for s in pack["slots"] if s.get("script")],
                  "prepared_at": wf["extra"]["aind_run"]["prepared_at"], "prompt_id": resp.get("prompt_id"), "response": resp}
        pack["generation_record"] = record
        pack["generation_authorized"] = True
        save_json(pack_path, pack)
        ctx.report_append("s15 comfy", f"queued prompt {resp.get('prompt_id')} number {resp.get('number')}; node_errors: {resp.get('node_errors')}")
        if record["state"] != "accepted":
            log.error("ComfyUI rejected the graph: %s", resp.get("node_errors"))
            ctx.set_stage("s15_comfy", "failed", node_errors=resp.get("node_errors"))
            return 2
    if record.get("prompt_id") and not args.inventory_only:
        deadline = time.time() + args.max_hours * 3600
        log.info("waiting for prompt %s (up to %.1f h)", record["prompt_id"], args.max_hours)
        while time.time() < deadline:
            try:
                hist = http(f"{url}/history/{record['prompt_id']}", timeout=60)
            except (urllib.error.URLError, OSError) as exc:
                log.warning("history poll failed: %s", exc)
                hist = {}
            entry = hist.get(record["prompt_id"])
            if entry and (entry.get("status", {}).get("completed") or entry.get("outputs")):
                status = entry.get("status", {})
                record["finished_status"] = status.get("status_str", "completed")
                record["finished_at"] = dt.datetime.now(dt.timezone.utc).isoformat()
                pack["generation_record"] = record
                save_json(pack_path, pack)
                if status.get("status_str") == "error":
                    log.error("ComfyUI reported an error: %s", status)
                    ctx.set_stage("s15_comfy", "failed", status=status)
                    return 2
                break
            time.sleep(30)
        else:
            log.error("timed out waiting for ComfyUI; re-run with --inventory-only later")
            return RC_EXTERNAL
    # inventory with the QA tool's function (read-only, ffprobe + full decode)
    sys.path.insert(0, str(PKG_ROOT / "vendor"))
    from validate_delivery import check_headlines_clips  # noqa: E402
    wf = load_json(wf_path)
    try:
        inv = check_headlines_clips(wf, str(out_root), hcfg.get("ffprobe", "ffprobe"), hcfg.get("ffmpeg", "ffmpeg"))
    except (ValueError, OSError) as exc:
        log.error("clip inventory failed: %s", exc)
        ctx.set_stage("s15_comfy", "failed", error=str(exc))
        return 2
    inv["edition"] = ctx.edition.isoformat()
    inv["generation_record"] = record
    save_json(ctx.headlines_sup / f"Headlines_{ctx.short}_clip_inventory.json", inv)
    ctx.report_append("s15 comfy", f"clip inventory {inv['clip_inventory']}: {inv['available_outputs']} of {inv['expected_outputs']} outputs; "
                                   f"missing {inv['missing']}, invalid {inv['invalid']}, ambiguous {inv['ambiguous']}")
    if inv["clip_inventory"] != "PASS":
        ctx.set_stage("s15_comfy", "incomplete", missing=inv["missing"], ambiguous=inv["ambiguous"])
        return 2
    ctx.set_stage("s15_comfy", "done", outputs=inv["available_outputs"])
    return 0


if __name__ == "__main__":
    stage_main(run, __doc__)
