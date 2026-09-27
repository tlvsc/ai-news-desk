"""End-to-end dry run: every stage that can run on this machine, zero tokens, synthetic pool and template.
Writes into a temporary local_root (never the real runs/ folder) and prints the evidence table (house rule 5).

    python tests/e2e_dry.py            keeps the temp folder and prints its path
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

PKG = Path(__file__).resolve().parent.parent
EDITION = "2026-09-27"


def sh(*args: str) -> int:
    print("$", " ".join(args))
    return subprocess.call([sys.executable, str(PKG / "run_v1.py"), *args], cwd=str(PKG))


def main() -> int:
    tmp = Path(tempfile.mkdtemp(prefix="aind_v1_e2e_"))
    subprocess.check_call([sys.executable, str(PKG / "tests" / "make_fixture.py"), "--edition", EDITION], cwd=str(PKG))
    subprocess.check_call([sys.executable, str(PKG / "tests" / "make_template.py")], cwd=str(PKG))
    cfg = json.loads((PKG / "config" / "v1_config.json").read_text(encoding="utf-8"))
    cfg["local_root"] = str(tmp / "runs")
    cfg["history_root"] = str(tmp / "history")
    cfg["llm"]["mode"] = "dry"
    cfg["headlines"]["comfy_template"] = str(PKG / "tests" / "fixtures" / "template_synthetic.json")
    cfg["headlines"]["reference_images_visually_verified"] = True  # test only: the QA tool demands it
    cfg_path = tmp / "test_config.json"
    cfg_path.write_text(json.dumps(cfg, indent=1), encoding="utf-8")
    base = ["--edition", EDITION, "--config", str(cfg_path), "--llm", "dry", "--approve-all"]
    fixture = str(PKG / "tests" / "fixtures" / "pool_320.jsonl")
    major = str(PKG / "tests" / "fixtures" / "major_news_list.json")
    results = {}
    results["s01-s11"] = sh(*base, "--fixture", fixture, "--major-news-file", major, "--run-description", "e2e dry test")
    results["s12-s14"] = sh(*base, "--from", "s12", "--to", "s14")
    results["s15"] = sh(*base, "--only", "s15")
    results["s16"] = sh(*base, "--only", "s16")
    results["s17"] = sh(*base, "--only", "s17")
    run = tmp / "runs" / EDITION
    try:
        return evidence(run, results)
    except (FileNotFoundError, KeyError) as exc:
        print(json.dumps({"exit codes": results, "run_dir": str(run), "evidence_error": repr(exc)}, indent=1))
        print("E2E FAIL")
        return 1


def evidence(run: Path, results: dict) -> int:
    cp = json.loads((run / "reports" / "supportive files" / "run-checkpoint.json").read_text(encoding="utf-8"))
    st = json.loads((run / "state.json").read_text(encoding="utf-8"))
    short = "27-9-26"
    ev = {"exit codes (expected s01-s11=4 render pending, s12-s14=0, s15=4, s16=4, s17=0)": results,
          "pool_candidate_count (>=300)": cp["pool_candidate_count"], "unique_event_count": cp["unique_event_count"],
          "full_report_count (50-150)": cp["full_report_count"], "bulletin_count (25-30)": cp["bulletin_count"],
          "cards_planned_count (15)": cp["cards_planned_count"], "headlines_core_count (8-9)": cp["headlines_core_count"],
          "gates": {k: v for k, v in cp["stages"].items()}, "major_news_miss_gate": cp["major_news_miss_gate"],
          "stages": {k: v["status"] for k, v in st["stages"].items()},
          "files": sorted(str(p.relative_to(run)) for p in run.rglob("*") if p.is_file() and "work" not in p.parts and "llm_cache" not in p.parts),
          "llm_log_rows": sum(1 for _ in (run / "work" / "llm_log.jsonl").open(encoding="utf-8")) if (run / "work" / "llm_log.jsonl").exists() else 0,
          "validation": json.loads((run / "Headlines" / "supportive files" / f"headlines_{short}_validation.json").read_text(encoding="utf-8"))["result"],
          "run_dir": str(run)}
    print(json.dumps(ev, indent=1, ensure_ascii=False))
    ok = (results == {"s01-s11": 4, "s12-s14": 0, "s15": 4, "s16": 4, "s17": 0} and cp["pool_candidate_count"] >= 300
          and 50 <= cp["full_report_count"] <= 150 and 25 <= cp["bulletin_count"] <= 30 and cp["cards_planned_count"] == 15
          and 8 <= cp["headlines_core_count"] <= 9 and ev["validation"] == "PASS")
    print("E2E", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
