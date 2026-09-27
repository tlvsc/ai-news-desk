"""s11_cards_render: render the 15 cards from the approved copy, then verify them byte by byte. Zero LLM.

The renderer itself is not in this repo: the registered ChatGPT package (aind_cards.py, Drive zip
13Ic8tAb_IgWFUTWgrzmC0eLp4OxCzk3V) or a Claude-lane renderer runs on Rafael's PC. This stage writes the
renderer inputs (edition.json, content_lock.json), runs cards.renderer_command when configured, and always
verifies what is in cards/: exactly 15 PNG at 1080x1920 with the D-M-YY_Ixx_lane names plus one combined image.

Exit 4 = external step pending (no renderer configured or files not there yet); instructions in cards/supportive files/RENDER_PENDING.md.
"""
from __future__ import annotations

import datetime as dt
import shlex
import struct
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.common import RC_EXTERNAL, load_json, log, save_json, sha256_file, stage_main  # noqa: E402


def png_size(path: Path) -> tuple[int, int] | None:
    with path.open("rb") as fh:
        head = fh.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return struct.unpack(">II", head[16:24])


def verify(ctx, copy: dict) -> dict:
    expected = [c["file"] for c in copy["cards"]]
    rows, missing, bad = [], [], []
    for name in expected:
        p = ctx.cards / name
        if not p.exists():
            missing.append(name)
            continue
        size = png_size(p)
        ok = size == (1080, 1920)
        if not ok:
            bad.append(f"{name}: {size}")
        rows.append({"name": name, "bytes": p.stat().st_size, "sha256": sha256_file(p), "size": list(size) if size else None, "ok": ok})
    combined = sorted(ctx.cards.glob(f"cards_{ctx.short}_combined*"))
    extra = [p.name for p in ctx.cards.iterdir() if p.is_file() and p.name not in expected and p not in combined]
    return {"edition": ctx.edition.isoformat(), "checked_at": dt.datetime.now().isoformat(timespec="seconds"),
            "expected": len(expected), "present": len(rows), "missing": missing, "wrong_size": bad,
            "combined": [{"name": c.name, "bytes": c.stat().st_size, "sha256": sha256_file(c)} for c in combined],
            "extra_files_in_cards": extra, "cards": rows,
            "result": "PASS" if not missing and not bad and combined and not extra else "FAIL"}


def run(ctx, extra_args=None) -> int:
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--verify-only", action="store_true", help="skip the renderer, only check cards/")
    args = p.parse_args(extra_args or [])
    copy_path = ctx.cards_sup / f"cards_{ctx.short}_copy.json"
    copy = load_json(copy_path, default={})
    if not copy.get("cards"):
        log.error("no approved copy at %s; run s10 first", copy_path)
        return 1
    if "approved" not in copy.get("status", ""):
        log.error("copy is not approved yet (status: %s); approve s10 first", copy.get("status"))
        return 3
    cfg = ctx.config["cards"]
    edition = {"edition": ctx.edition.isoformat(), "short": ctx.short, "lane": ctx.lane, "date_title": ctx.title_date,
               "date_long": copy["date_long"], "out_dir": str(ctx.cards), "fonts_dir": cfg.get("fonts_dir", ""),
               "previous_cover_png": cfg.get("previous_cover_png", ""), "notice": copy["notice"], "cards": copy["cards"]}
    ed_path = ctx.cards_sup / "edition.json"
    save_json(ed_path, edition)
    save_json(ctx.cards_sup / "content_lock.json", {"copy_file": copy_path.name, "copy_sha256": sha256_file(copy_path),
                                                    "edition_sha256": sha256_file(ed_path), "locked_at": dt.datetime.now().isoformat(timespec="seconds"),
                                                    "rule": "render only from this copy; any copy change re-locks and re-renders"})
    cmd = cfg.get("renderer_command", "")
    if cmd and not args.verify_only:
        cmd = cmd.format(edition_json=str(ed_path), out_dir=str(ctx.cards), renderer_dir=cfg.get("renderer_package_dir", ""),
                         short=ctx.short, lane=ctx.lane, edition=ctx.edition.isoformat())
        log.info("running renderer: %s", cmd)
        proc = subprocess.run(shlex.split(cmd, posix=sys.platform != "win32"), capture_output=True, text=True, encoding="utf-8", errors="replace")
        (ctx.cards_sup / "render.log").write_text(f"$ {cmd}\nexit {proc.returncode}\n\n{proc.stdout}\n{proc.stderr}", encoding="utf-8")
        if proc.returncode != 0:
            log.error("renderer failed (exit %s); see cards/supportive files/render.log", proc.returncode)
    check = verify(ctx, copy)
    save_json(ctx.cards_sup / f"cards_{ctx.short}_render_check.json", check)
    if check["result"] == "PASS":
        ctx.set_gate("cards_render", "PASS", f"{check['present']} cards, combined {len(check['combined'])}")
        ctx.report_append("s11 cards render", f"{check['present']} PNG verified at 1080x1920, combined image {[c['name'] for c in check['combined']]}.")
        ctx.set_stage("s11_cards_render", "done", present=check["present"])
        return 0
    inst = [f"# RENDER PENDING — cards_{ctx.short}", "",
            "This machine has not produced the card PNGs yet. On the production PC:", "",
            f"1. Renderer input: `{ed_path}` (approved copy, locked by content_lock.json).",
            f"2. Output folder: `{ctx.cards}`. Names must be exactly: " + ", ".join(c["file"] for c in copy["cards"][:2]) + " ... " + copy["cards"][-1]["file"],
            f"3. Plus one combined image named cards_{ctx.short}_combined_{ctx.lane}.jpg (or .png).",
            "4. Set cards.renderer_command in config/v1_config.json to run the renderer automatically next time, e.g.",
            '   "python \\"{renderer_dir}/aind_cards.py\\" --edition \\"{edition_json}\\" --out \\"{out_dir}\\""',
            f"5. Re-run: python run_v1.py --edition {ctx.edition.isoformat()} --from s11", "",
            f"Current check: missing {len(check['missing'])}, wrong size {check['wrong_size']}, combined {len(check['combined'])}, extra files {check['extra_files_in_cards']}."]
    (ctx.cards_sup / "RENDER_PENDING.md").write_text("\n".join(inst) + "\n", encoding="utf-8")
    ctx.report_append("s11 cards render", f"EXTERNAL STEP PENDING: {len(check['missing'])} of {check['expected']} cards missing; see cards/supportive files/RENDER_PENDING.md")
    ctx.set_stage("s11_cards_render", "external_pending", missing=len(check["missing"]))
    return RC_EXTERNAL


if __name__ == "__main__":
    stage_main(run, __doc__)
