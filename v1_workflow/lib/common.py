"""Shared helpers for the AI News Desk V1 workflow.

One run = one edition date. Every stage reads and writes files inside the run folder, so any stage can be
re-run alone. Nothing here calls a model.

Run folder layout (mirrors the Drive product structure so s17 can upload without renaming):
  runs/YYYY-MM-DD/
    state.json                  stage status, hashes, timestamps
    V1_script_report.md         human readable run report (Workflow Monitor extends this file)
    work/                       intermediate records (jsonl) and llm_log.jsonl
    approvals/                  <stage>.pending.md / <stage>.approved
    reports/  reports/supportive files/
    cards/    cards/supportive files/
    Headlines/ Headlines/supportive files/
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import logging
import os
import re
import sys
import zoneinfo
from pathlib import Path

PKG_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = PKG_ROOT / "config" / "v1_config.json"
CATEGORIES_PATH = PKG_ROOT / "config" / "categories.json"
SOURCES_PATH = PKG_ROOT / "config" / "sources_v1.json"

log = logging.getLogger("aind.v1")


def setup_logging(run_dir: Path | None = None, verbose: bool = False) -> None:
    handlers = [logging.StreamHandler(sys.stdout)]
    if run_dir is not None:
        (run_dir / "work").mkdir(parents=True, exist_ok=True)
        handlers.append(logging.FileHandler(run_dir / "work" / "run.log", encoding="utf-8"))
    logging.basicConfig(level=logging.DEBUG if verbose else logging.INFO,
                        format="%(asctime)s %(levelname)s %(message)s", handlers=handlers, force=True)


def load_json(path: Path | str, default=None):
    p = Path(path)
    if not p.exists():
        if default is not None:
            return default
        raise FileNotFoundError(p)
    return json.loads(p.read_text(encoding="utf-8-sig"))


def save_json(path: Path | str, data, *, overwrite: bool = True) -> Path:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists() and not overwrite:
        raise FileExistsError(f"{p} exists; superseded files are renamed, never overwritten silently")
    p.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    return p


def read_jsonl(path: Path | str) -> list[dict]:
    p = Path(path)
    if not p.exists():
        return []
    out = []
    with p.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


def write_jsonl(path: Path | str, rows) -> Path:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    return p


def sha256_file(path: Path | str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def rename_old(path: Path) -> Path | None:
    """House rule 3: superseded files are renamed *_old, never removed."""
    if not path.exists():
        return None
    base, suffix = path.stem, path.suffix
    candidate = path.with_name(f"{base}_old{suffix}")
    n = 2
    while candidate.exists():
        candidate = path.with_name(f"{base}_old{n}{suffix}")
        n += 1
    path.rename(candidate)
    return candidate


# ----------------------------------------------------------------------------- dates

DAYS = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
MONTHS = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]


def short_date(edition: dt.date) -> str:
    """Filename date, Rafael's 13 Sep rule: D-M-YY, e.g. 26-9-26."""
    return f"{edition.day}-{edition.month}-{edition.year % 100:02d}"


def title_date(edition: dt.date) -> str:
    """Comfy title and card header date, e.g. FRI 11 SEP 2026."""
    return f"{DAYS[edition.weekday()]} {edition.day} {MONTHS[edition.month - 1]} {edition.year}"


def long_date(edition: dt.date) -> str:
    return edition.strftime("%A %-d %B %Y").upper() if os.name != "nt" else edition.strftime("%A %#d %B %Y").upper()


def reporting_window(edition: dt.date, tz_name: str, hour: int) -> tuple[dt.datetime, dt.datetime]:
    """09:00 the day before to 09:00 on the edition date, Asia/Jerusalem."""
    tz = zoneinfo.ZoneInfo(tz_name)
    end = dt.datetime(edition.year, edition.month, edition.day, hour, 0, tzinfo=tz)
    return end - dt.timedelta(days=1), end


def parse_edition(text: str | None, tz_name: str) -> dt.date:
    if not text or text == "today":
        return dt.datetime.now(zoneinfo.ZoneInfo(tz_name)).date()
    return dt.date.fromisoformat(text)


# ----------------------------------------------------------------------------- run context

class RunContext:
    """Everything a stage needs. Built once by the orchestrator or by a stage run alone."""

    def __init__(self, edition: dt.date, config: dict, package_root: Path = PKG_ROOT, llm_mode: str | None = None):
        self.edition = edition
        self.config = config
        self.package_root = package_root
        self.categories = load_json(CATEGORIES_PATH)
        self.sources = load_json(SOURCES_PATH)
        root = Path(config.get("local_root", "./runs"))
        if not root.is_absolute():
            root = package_root / root
        self.local_root = root
        self.run_dir = root / edition.isoformat()
        self.work = self.run_dir / "work"
        self.approvals = self.run_dir / "approvals"
        p = config["products"]
        self.reports = self.run_dir / p["reports"]
        self.reports_sup = self.reports / p["supportive"]
        self.cards = self.run_dir / p["cards"]
        self.cards_sup = self.cards / p["supportive"]
        self.headlines = self.run_dir / p["headlines"]
        self.headlines_sup = self.headlines / p["supportive"]
        hist = Path(config.get("history_root", "./history"))
        self.history = hist if hist.is_absolute() else package_root / hist
        self.llm_mode = llm_mode or config.get("llm", {}).get("mode", "live")
        self.window_start, self.window_end = reporting_window(edition, config["timezone"], config["window_hour"])
        self.short = short_date(edition)
        self.title_date = title_date(edition)
        self.lane = config.get("lane", "VL1")

    def ensure_dirs(self) -> None:
        for d in (self.work, self.approvals, self.reports_sup, self.cards_sup, self.headlines_sup, self.history):
            d.mkdir(parents=True, exist_ok=True)

    # state -------------------------------------------------------------
    @property
    def state_path(self) -> Path:
        return self.run_dir / "state.json"

    def state(self) -> dict:
        return load_json(self.state_path, default={"edition": self.edition.isoformat(), "stages": {}, "gates": {}})

    def set_stage(self, stage: str, status: str, **info) -> None:
        st = self.state()
        entry = st["stages"].get(stage, {})
        entry.update({"status": status, "at": dt.datetime.now().isoformat(timespec="seconds"), **info})
        st["stages"][stage] = entry
        save_json(self.state_path, st)

    def set_gate(self, name: str, result: str, detail: str = "") -> None:
        st = self.state()
        st["gates"][name] = {"result": result, "detail": detail, "at": dt.datetime.now().isoformat(timespec="seconds")}
        save_json(self.state_path, st)

    # products ----------------------------------------------------------
    def product_name(self, product: str, suffix: str) -> str:
        """cards_26-9-26_I01_VL1.png, Headlines_26-9-26.mp4, headlines_26-9-26_pack.json ..."""
        return f"{product}_{self.short}{suffix}"

    def category_order(self) -> list[dict]:
        return self.categories["order"]

    def category_by_key(self, key: str) -> dict | None:
        return next((c for c in self.categories["order"] if c["key"] == key), None)

    def category_key_from_name(self, name: str) -> str:
        n = (name or "").lower()
        for c in self.categories["order"]:
            if c["name"].lower() == n or c["key"].lower() == n:
                return c["key"]
        for c in self.categories["order"]:
            if any(a in n for a in c["aliases"]):
                return c["key"]
        return "MOD"

    def importance_label(self, score: int) -> str:
        if score >= 10:
            return "CRITICAL"
        if score >= 8:
            return "HIGH"
        if score >= 6:
            return "MEDIUM"
        return "WATCHLIST"

    # report ------------------------------------------------------------
    def report_append(self, heading: str, body: str) -> None:
        """Append a section to V1_script_report.md; never rewrite earlier sections."""
        path = self.run_dir / "V1_script_report.md"
        stamp = dt.datetime.now().isoformat(timespec="seconds")
        with path.open("a", encoding="utf-8") as fh:
            if path.stat().st_size == 0:
                fh.write(f"# V1 script report, edition {self.edition.isoformat()}\n\n")
            fh.write(f"## {heading}  ({stamp})\n\n{body.rstrip()}\n\n")


def load_context(edition_text: str | None = None, config_path: Path | str | None = None,
                 llm_mode: str | None = None) -> RunContext:
    config = load_json(config_path or CONFIG_PATH)
    edition = parse_edition(edition_text, config["timezone"])
    ctx = RunContext(edition, config, llm_mode=llm_mode)
    ctx.ensure_dirs()
    return ctx


def stage_main(stage_fn, description: str):
    """Standard CLI for a stage run on its own: python stages/sNN_x.py --edition YYYY-MM-DD"""
    import argparse
    p = argparse.ArgumentParser(description=description)
    p.add_argument("--edition", default="today")
    p.add_argument("--config", default=None)
    p.add_argument("--llm", default=None, choices=["live", "dry", "manual"])
    p.add_argument("--verbose", action="store_true")
    args, extra = p.parse_known_args()
    ctx = load_context(args.edition, args.config, args.llm)
    setup_logging(ctx.run_dir, args.verbose)
    rc = stage_fn(ctx, extra)
    sys.exit(int(rc or 0))


# ----------------------------------------------------------------------------- text helpers

_WS = re.compile(r"\s+")


def norm_text(s: str) -> str:
    return _WS.sub(" ", (s or "")).strip()


def norm_url(url: str) -> str:
    """Canonical URL for exact duplicate detection: lowercase host, no tracking params, no fragment."""
    from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode
    try:
        u = urlsplit(url.strip())
    except ValueError:
        return url.strip()
    q = [(k, v) for k, v in parse_qsl(u.query, keep_blank_values=False)
         if not k.lower().startswith(("utm_", "fbclid", "gclid", "ref", "cmpid", "ncid", "srnd"))]
    path = u.path.rstrip("/") or "/"
    return urlunsplit((u.scheme.lower() or "https", u.netloc.lower().replace("www.", ""), path, urlencode(q), ""))


STOP = set("a an the and or of to in on for with by at from as is are was were be been this that these those it its "
           "into over after before about than then their his her they them he she we you our your not no new says said "
           "will would could can may might up out off more most also just".split())


def tokens(s: str) -> set[str]:
    return {t for t in re.findall(r"[a-z0-9]+", (s or "").lower()) if t not in STOP and len(t) > 2}


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)
