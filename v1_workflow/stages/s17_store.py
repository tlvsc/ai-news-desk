"""s17_store: the storage manifest and the Drive upload plan. Zero LLM. Writes locally only.
Drive upload happens only when drive.upload_enabled is true AND Rafael approves (approvals/s17_store.approved);
in test runs it is a plan file. Storage layout: AIND_daily_storage_rules.txt (date root, products, supportive files).

Output: runs/<date>/storage_manifest_<date>.json, runs/<date>/drive_upload_plan.json, final section of V1_script_report.md
"""
from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.common import load_json, log, read_jsonl, rename_old, save_json, sha256_file, stage_main  # noqa: E402


def listing(root: Path, rel_base: Path) -> list[dict]:
    out = []
    if not root.exists():
        return out
    for p in sorted(root.rglob("*")):
        if p.is_file() and not p.name.endswith("_old") and "frames" not in p.parts:
            out.append({"name": p.name, "rel": str(p.relative_to(rel_base)).replace("\\", "/"), "bytes": p.stat().st_size, "sha256": sha256_file(p)})
    return out


def run(ctx, extra_args=None) -> int:
    st = ctx.state()
    copy = load_json(ctx.cards_sup / f"cards_{ctx.short}_copy.json", default={})
    render = load_json(ctx.cards_sup / f"cards_{ctx.short}_render_check.json", default={})
    qa = load_json(ctx.headlines_sup / f"Headlines_{ctx.short}_QA.json", default={})
    llm_rows = read_jsonl(ctx.work / "llm_log.jsonl")
    llm = {"calls": len(llm_rows), "cost_usd": round(sum(r.get("cost_usd") or 0 for r in llm_rows), 4),
           "input_tokens": sum(r.get("input_tokens") or 0 for r in llm_rows), "output_tokens": sum(r.get("output_tokens") or 0 for r in llm_rows),
           "cache_read": sum(r.get("cache_read") or 0 for r in llm_rows),
           "by_prompt": {}}
    for r in llm_rows:
        b = llm["by_prompt"].setdefault(r["prompt"], {"calls": 0, "cost_usd": 0.0, "model": r.get("model")})
        b["calls"] += 1
        b["cost_usd"] = round(b["cost_usd"] + (r.get("cost_usd") or 0), 4)
    cards_files = [c for c in render.get("cards", [])] if render else []
    manifest = {"edition": ctx.edition.isoformat(), "producing_lane": f"{ctx.lane} (Claude lane, V1 workflow script)",
                "written": dt.datetime.now().isoformat(timespec="seconds"),
                "status": "LOCAL ONLY. Test run; nothing uploaded to Drive." if not ctx.config["drive"].get("upload_enabled") else "local, upload planned",
                "presentation_order": "Decision Log, General order of categories, 23 Sep 2026: critical first, then " + ", ".join(c["key"] for c in ctx.category_order()),
                "daily_folder": {"local": str(ctx.run_dir), "drive_parent_id": ctx.config["drive"].get("daily_root_id", ""), "drive_name": ctx.edition.isoformat()},
                "products": {
                    "reports": {"folder": ctx.config["products"]["reports"], "files": listing(ctx.reports, ctx.run_dir)},
                    "cards": {"folder": ctx.config["products"]["cards"], "format": [1080, 1920], "producing_lane": ctx.lane,
                              "ordered_files": [{"order": i + 1, "id": f["sha256"][:16], "name": f["name"], "bytes": f["bytes"], "sha256": f["sha256"]} for i, f in enumerate(cards_files)],
                              "combined_image": (render.get("combined") or [{}])[0], "publication_status": "not approved",
                              "cards_order": [f"{c['id']} {c['kind']}" + (f" {c.get('category','')} item {c.get('item_n')}" if c["kind"] == "story" else "") for c in copy.get("cards", [])],
                              "supportive_files": listing(ctx.cards_sup, ctx.run_dir)},
                    "Headlines": {"folder": ctx.config["products"]["headlines"], "files": listing(ctx.headlines, ctx.run_dir),
                                  "qa": {k: qa.get(k) for k in ("duration_seconds", "width", "height", "measured_integrated_lufs", "measured_true_peak_dbtp", "sha256")} if qa else "not stitched on this machine",
                                  "supportive_files": listing(ctx.headlines_sup, ctx.run_dir)}},
                "gates": st.get("gates", {}), "stages": {k: v.get("status") for k, v in st.get("stages", {}).items()},
                "llm_usage": llm, "qa_status": "internal checks only; publishing QA not run; not approved for publication"}
    mp = ctx.run_dir / f"storage_manifest_{ctx.edition.isoformat()}.json"
    rename_old(mp)
    save_json(mp, manifest)
    plan = []
    for prod, key in (("reports", "reports"), ("cards", "cards"), ("Headlines", "headlines")):
        for f in manifest["products"][prod].get("files", []) + manifest["products"][prod].get("supportive_files", []) + \
                [dict(x, rel=f"{ctx.config['products']['cards']}/{x['name']}") for x in manifest["products"][prod].get("ordered_files", [])]:
            plan.append({"local": str(ctx.run_dir / f["rel"]), "drive_path": f"{ctx.edition.isoformat()}/{f['rel']}", "bytes": f["bytes"], "sha256": f["sha256"]})
    plan.append({"local": str(mp), "drive_path": f"{ctx.edition.isoformat()}/{mp.name}", "bytes": mp.stat().st_size, "sha256": sha256_file(mp)})
    save_json(ctx.run_dir / "drive_upload_plan.json", {"edition": ctx.edition.isoformat(), "drive_parent_id": ctx.config["drive"].get("daily_root_id", ""),
                                                       "upload_enabled": bool(ctx.config["drive"].get("upload_enabled")), "rule": "never overwrite; superseded files renamed *_old; Rafael approves first",
                                                       "files": plan})
    ctx.report_append("s17 store", f"storage manifest {mp.name}: {len(plan)} files planned for {ctx.edition.isoformat()}/ (upload_enabled={bool(ctx.config['drive'].get('upload_enabled'))}). "
                                   f"LLM: {llm['calls']} calls, {llm['input_tokens']} in / {llm['output_tokens']} out tokens, cache read {llm['cache_read']}, cost {llm['cost_usd']} USD.")
    ctx.set_stage("s17_store", "done", files=len(plan), llm_calls=llm["calls"], cost_usd=llm["cost_usd"])
    log.info("done: %s", mp)
    return 0


if __name__ == "__main__":
    stage_main(run, __doc__)
