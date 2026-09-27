"""s05_gates: the machine-readable checkpoint and the fail-closed law (18 Sep 2026, section I and J).
Zero LLM. Counts come from saved files, never from narrative.

Inputs: work/source_ledger.json, work/raw_pool.jsonl, work/events.jsonl, work/ranked.jsonl,
        work/major_news_list.json (optional: [{"title","url","date"}] gathered by web search or by Rafael)
Output: reports/supportive files/run-checkpoint.json, reports/supportive files/major-news-gate.md
Exit 2 when a hard gate fails and no recorded override exists (--override name=reason).
"""
from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.common import jaccard, load_json, log, read_jsonl, save_json, stage_main, tokens  # noqa: E402

HARD = ("source_fetch_gate", "pool_gate_min_300", "major_news_miss_gate")


def compute(ctx, overrides: dict) -> tuple[dict, str]:
    ledger = load_json(ctx.work / "source_ledger.json", default={})
    raw = read_jsonl(ctx.work / "raw_pool.jsonl")
    events = read_jsonl(ctx.work / "events.jsonl")
    ranked = read_jsonl(ctx.work / "ranked.jsonl")
    g = ctx.config["gates"]
    pool_candidates = sum(1 for r in raw if r["window_check"] != "OUT OF WINDOW")
    retained = [e for e in events if e["disposition"] == "RETAINED EVENT ID"]
    src_ok = ledger and ledger.get("sources_pending_count", 1) == 0 and ledger.get("sources_failed_count", 1) == 0 \
        and ledger.get("sources_incomplete_count", 1) == 0
    # major-news miss gate
    mn_path = ctx.work / "major_news_list.json"
    mn_md = ["# Major-news miss gate, edition " + ctx.edition.isoformat(), ""]
    missing = []
    if mn_path.exists():
        top = load_json(mn_path)
        sigs = [(e, tokens(e["headline"] + " " + e.get("summary", ""))) for e in events]
        for item in top:
            t = tokens(item.get("title", "") + " " + item.get("summary", ""))
            best = max(((jaccard(t, s), e) for e, s in sigs), key=lambda x: x[0], default=(0, None))
            status = "IN_POOL" if best[0] >= 0.35 else "MISSING"
            mn_md.append(f"| {item.get('title','')[:90]} | {status} | {best[1]['id'] if best[1] and status=='IN_POOL' else ''} | {round(best[0],2)} |")
            if status == "MISSING":
                missing.append(item)
        mn_result = "PASS" if not missing else "FAIL"
        mn_md.insert(2, f"Compared {len(top)} major stories against {len(events)} events. Result: {mn_result}. Missing: {len(missing)}.")
        mn_md.insert(3, "\n| story | status | event | score |\n|---|---|---|---|")
    else:
        mn_result = "NOT RUN"
        mn_md.append("No work/major_news_list.json supplied. Gather the day's top AI stories (web search or Rafael) and re-run s05.")
    cp = {"edition": ctx.edition.isoformat(),
          "reporting_window": f"{ctx.window_start.isoformat()}/{ctx.window_end.isoformat()}",
          "run_identity": f"AI News Desk V1 workflow, Claude lane ({ctx.lane}), test run",
          "written_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%MZ"),
          "registry_source_count": ledger.get("registry_source_count", 0),
          "sources_fetched_terminal_count": ledger.get("sources_fetched_terminal_count", 0),
          "sources_checked_success_count": ledger.get("sources_checked_success_count", 0),
          "sources_failed_count": ledger.get("sources_failed_count", 0),
          "sources_incomplete_count": ledger.get("sources_incomplete_count", 0),
          "sources_pending_count": ledger.get("sources_pending_count", 0),
          "pool_candidate_count": pool_candidates, "pool_rejected_count": sum(1 for r in raw if r["window_check"] == "OUT OF WINDOW"),
          "unique_event_count": len(retained), "full_report_count": None, "bulletin_count": None,
          "cards_planned_count": None, "headlines_core_count": None, "major_news_miss_gate": mn_result,
          "major_news_missing": [m.get("title") for m in missing],
          "stages": {"source_fetch_gate": "PASS" if src_ok else "FAIL",
                     "pool_gate_min_300": "PASS" if pool_candidates >= g["pool_min"] else "FAIL",
                     "dedup_unique_event_gate": "PASS" if retained else "FAIL",
                     "major_news_miss_gate": mn_result,
                     "full_report_gate_50_150": "NOT RUN", "bulletin_gate": "NOT RUN",
                     "cards_selection_gate": "NOT RUN", "headlines_selection_gate": "NOT RUN"},
          "overrides": overrides, "counts_source": "Computed from work/*.jsonl and source_ledger.json, not from narrative claims."}
    return cp, "\n".join(mn_md) + "\n"


def run(ctx, extra_args=None) -> int:
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--override", action="append", default=[], help="gate=reason (recorded, Rafael's decision)")
    p.add_argument("--major-news-file", help="copy this json to work/major_news_list.json first")
    args = p.parse_args(extra_args or [])
    if args.major_news_file:
        save_json(ctx.work / "major_news_list.json", load_json(args.major_news_file))
    overrides = dict(o.split("=", 1) for o in args.override if "=" in o)
    cp, md = compute(ctx, overrides)
    save_json(ctx.reports_sup / "run-checkpoint.json", cp)
    (ctx.reports_sup / "major-news-gate.md").write_text(md, encoding="utf-8")
    failed = [k for k in HARD if cp["stages"][k] != "PASS" and k not in overrides]
    for k, v in cp["stages"].items():
        ctx.set_gate(k, v, overrides.get(k, ""))
    ctx.report_append("s05 gates", "\n".join(f"- {k}: {v}" + (f" (override: {overrides[k]})" if k in overrides else "")
                                             for k, v in cp["stages"].items() if v != "NOT RUN" or k in HARD)
                      + f"\n- pool candidates {cp['pool_candidate_count']} (min {ctx.config['gates']['pool_min']}), unique events {cp['unique_event_count']}")
    if failed:
        log.error("FAIL-CLOSED: %s. Record the blocker; do not produce downstream products. Rafael may override with --override gate=reason", failed)
        ctx.set_stage("s05_gates", "failed", failed=failed)
        return 2
    ctx.set_stage("s05_gates", "done", overrides=overrides)
    return 0


if __name__ == "__main__":
    stage_main(run, __doc__)
