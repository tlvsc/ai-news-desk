#!/usr/bin/env python3
"""AI News Desk V1 workflow, Claude lane. One run = one edition. Resumable, fail-closed, approval pauses.

    python run_v1.py --edition 2026-09-27                      run every stage from where it stopped
    python run_v1.py --edition 2026-09-27 --llm dry --fixture tests/fixtures/pool_320.jsonl --approve-all
    python run_v1.py --edition 2026-09-27 --approve s10_cards_copy   record Rafael's approval and continue
    python run_v1.py --edition 2026-09-27 --from s12 --to s14        run a range; --only s09 runs one stage
    python run_v1.py --edition 2026-09-27 --override pool_gate_min_300="Rafael 27 Sep: short day, proceed"

Exit codes: 0 done, 1 error, 2 a gate failed (read V1_script_report.md), 3 approval needed (read approvals/*.pending.md),
4 external step pending (wrong machine or missing tool; read the stage's *_PENDING.md).
Stages: s01 collect, s02 digest, s03 dedupe, s04 classify, s05 gates, s06 report, s07 bulletin, s08 bigger picture,
s09 cards select, s10 cards copy [approval], s11 cards render [PC], s12 headlines select [approval], s13 headlines fill,
s14 validate, s15 comfy [approval, PC], s16 stitch [approval, PC], s17 store.
"""
from __future__ import annotations

import argparse
import datetime as dt
import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.common import RC_APPROVAL, RC_EXTERNAL, RC_GATE, load_context, log, setup_logging  # noqa: E402

STAGES = ["s01_collect", "s02_digest", "s03_dedupe", "s04_classify", "s05_gates", "s06_report", "s07_bulletin",
          "s08_bigger_picture", "s09_cards_select", "s10_cards_copy", "s11_cards_render", "s12_headlines_select",
          "s13_headlines_fill", "s14_validate", "s15_comfy", "s16_stitch", "s17_store"]
# per-stage extra arguments taken from the orchestrator's own options
PASS = {"s01_collect": ["fixture", "extra", "no_articles"], "s05_gates": ["override", "major_news_file"],
        "s09_cards_select": ["allow_short"], "s11_cards_render": ["verify_only"], "s13_headlines_fill": ["template"],
        "s14_validate": ["comfy_url"], "s15_comfy": ["inventory_only", "max_hours"]}


def resolve(name: str) -> str:
    m = [s for s in STAGES if s == name or s.startswith(name + "_") or s.startswith(name)]
    if len(m) != 1:
        sys.exit(f"unknown or ambiguous stage {name!r}; stages: {', '.join(STAGES)}")
    return m[0]


def extra_for(stage: str, args) -> list[str]:
    out = []
    for key in PASS.get(stage, []):
        val = getattr(args, key, None)
        flag = "--" + key.replace("_", "-")
        if val in (None, False, "", []):
            continue
        if val is True:
            out.append(flag)
        elif isinstance(val, list):
            for v in val:
                out += [flag, str(v)]
        else:
            out += [flag, str(val)]
    return out


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--edition", default="today")
    p.add_argument("--config")
    p.add_argument("--llm", choices=["live", "dry", "manual"])
    p.add_argument("--from", dest="from_", metavar="STAGE")
    p.add_argument("--to", metavar="STAGE")
    p.add_argument("--only", metavar="STAGE")
    p.add_argument("--skip", action="append", default=[], metavar="STAGE")
    p.add_argument("--force", action="store_true", help="re-run stages already marked done")
    p.add_argument("--approve", action="append", default=[], metavar="STAGE", help="record Rafael's approval for a paused stage")
    p.add_argument("--approve-all", action="store_true", help="TEST RUNS ONLY: skip every approval pause")
    p.add_argument("--run-description", default="", help="one line for V1_script_report.md (Workflow Monitor)")
    p.add_argument("--verbose", action="store_true")
    # pass-through options
    p.add_argument("--fixture"), p.add_argument("--extra"), p.add_argument("--no-articles", action="store_true")
    p.add_argument("--override", action="append", default=[]), p.add_argument("--major-news-file")
    p.add_argument("--allow-short", default=""), p.add_argument("--verify-only", action="store_true")
    p.add_argument("--template"), p.add_argument("--comfy-url", default="")
    p.add_argument("--inventory-only", action="store_true"), p.add_argument("--max-hours", type=float)
    args = p.parse_args()
    ctx = load_context(args.edition, args.config, args.llm)
    setup_logging(ctx.run_dir, args.verbose)
    ctx.auto_approve = bool(args.approve_all)
    if ctx.auto_approve and ctx.llm_mode == "live":
        log.warning("--approve-all with live LLM: every pause is skipped. Never use this for a real edition.")
    for a in args.approve:
        stage = resolve(a)
        flag = ctx.approvals / f"{stage}.approved"
        flag.write_text(f"approved by Rafael via run_v1.py --approve at {dt.datetime.now().isoformat(timespec='seconds')}\n", encoding="utf-8")
        log.info("approval recorded: %s", flag)
    st = ctx.state()
    if args.run_description or "run" not in st:
        st["run"] = {"description": args.run_description or st.get("run", {}).get("description", ""), "llm_mode": ctx.llm_mode,
                     "started": st.get("run", {}).get("started") or dt.datetime.now().isoformat(timespec="seconds"), "lane": ctx.lane}
        from lib.common import save_json
        save_json(ctx.state_path, st)
        if args.run_description:
            ctx.report_append("run", f"{args.run_description}\nLLM mode: {ctx.llm_mode}. Window: {ctx.window_start} to {ctx.window_end}.")
    if args.only:
        todo = [resolve(args.only)]
    else:
        start = STAGES.index(resolve(args.from_)) if args.from_ else 0
        end = STAGES.index(resolve(args.to)) if args.to else len(STAGES) - 1
        todo = STAGES[start:end + 1]
    skip = {resolve(s) for s in args.skip}
    for stage in todo:
        if stage in skip:
            log.info("== %s skipped (--skip)", stage)
            continue
        status = ctx.state()["stages"].get(stage, {}).get("status")
        if status == "done" and not args.force and not args.only:
            log.info("== %s already done, skipping (use --force to redo)", stage)
            continue
        log.info("== %s", stage)
        mod = importlib.import_module(f"stages.{stage}")
        try:
            rc = int(mod.run(ctx, extra_for(stage, args)) or 0)
        except Exception as exc:  # noqa: BLE001 - a stage crash is recorded, then the run stops
            log.exception("%s crashed: %s", stage, exc)
            ctx.report_append(stage, f"CRASHED: {type(exc).__name__}: {exc}")
            ctx.set_stage(stage, "crashed", error=str(exc)[:300])
            return 1
        if rc == 0:
            continue
        if rc == RC_GATE:
            log.error("STOPPED at %s: a gate failed. Read %s", stage, ctx.run_dir / "V1_script_report.md")
        elif rc == RC_APPROVAL:
            log.warning("PAUSED at %s: Rafael's approval needed. Read %s then run --approve %s", stage, ctx.approvals / f"{stage}.pending.md", stage)
        elif rc == RC_EXTERNAL:
            log.warning("PAUSED at %s: this step runs on another machine or needs a tool. See the stage's *_PENDING.md or the log.", stage)
        else:
            log.error("STOPPED at %s with exit %s", stage, rc)
        return rc
    log.info("run complete for %s. Report: %s", ctx.edition.isoformat(), ctx.run_dir / "V1_script_report.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
