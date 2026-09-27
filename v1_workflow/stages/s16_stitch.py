"""s16_stitch (PC only): the Headlines reel from the hash-verified 1088x1920 clips (blueprint Section D).
Zero LLM, zero Python dependencies; needs ffmpeg and ffprobe on the machine.

Phase A (always): probe every clip, write the source manifest, build the subtitle files (.srt for reading, .ass with
PlayResX 1080 / PlayResY 1920, Instrument Sans, 40 percent black box, source credit line) and the transcript for
Rafael. STOP for approval (house rule 12): exit 3 until approvals/s16_stitch.approved exists.
Phase B (approved): crop 4 px each side to 1080x1920, 30 fps, concat, burn the .ass, loudness -14 LUFS / -2 dBTP,
libx264 high preset fast CRF 17 yuv420p, AAC 192k 48 kHz, faststart. Then ffprobe the result, measure loudness,
export three frames for Rafael's eyes (house rule 7) and write Headlines_<D-M-YY>_QA.json with the real numbers.

Input: Headlines_<D-M-YY>_clip_inventory.json, headlines_<D-M-YY>_pack.json, config headlines.opening_clip / ending_clip / date_overlay_png
Output: Headlines/Headlines_<D-M-YY>.mp4 + .srt + .ass, Headlines/supportive files/Headlines_<D-M-YY>_source_manifest.json, _QA.json, frames
"""
from __future__ import annotations

import datetime as dt
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.common import RC_APPROVAL, RC_EXTERNAL, load_json, log, rename_old, require_approval, save_json, sha256_file, stage_main  # noqa: E402
from lib.syllables import count  # noqa: E402

CREDIT = {"teaser": "DAILY GLOBAL AI INTELLIGENCE REPORT", "bigger_picture": "AI NEWS DESK"}


def probe(ffprobe: str, path: Path) -> dict:
    proc = subprocess.run([ffprobe, "-v", "error", "-show_streams", "-show_format", "-of", "json", str(path)],
                          capture_output=True, text=True, encoding="utf-8", errors="replace")
    if proc.returncode != 0:
        raise RuntimeError(f"ffprobe failed on {path.name}: {proc.stderr.strip()[:300]}")
    meta = json.loads(proc.stdout)
    v = next((s for s in meta["streams"] if s["codec_type"] == "video"), None)
    a = [s for s in meta["streams"] if s["codec_type"] == "audio"]
    if not v:
        raise RuntimeError(f"{path.name}: no video stream")
    dur = float(v.get("duration") or meta.get("format", {}).get("duration") or 0)
    return {"width": v.get("width"), "height": v.get("height"), "duration": dur, "fps": v.get("r_frame_rate"),
            "nb_frames": int(v["nb_frames"]) if str(v.get("nb_frames", "")).isdigit() else None, "audio": bool(a)}


def ff_path(p: Path) -> str:
    """Escape a path for use inside an ffmpeg filter string (Windows drive colons and backslashes)."""
    s = str(p).replace("\\", "/")
    return s.replace(":", "\\:").replace("'", "\\'")


def srt_time(t: float) -> str:
    ms = int(round(t * 1000))
    return f"{ms//3600000:02d}:{ms%3600000//60000:02d}:{ms%60000//1000:02d},{ms%1000:03d}"


def ass_time(t: float) -> str:
    cs = int(round(t * 100))
    return f"{cs//360000}:{cs%360000//6000:02d}:{cs%6000//100:02d}.{cs%100:02d}"


def caption_events(text: str, start: float, duration: float, max_chars: int = 34) -> list[tuple[float, float, str]]:
    """Split a spoken line into two-line captions and spread them over the clip in proportion to syllables."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        if len(cur) + len(w) + 1 > max_chars and cur:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    chunks = ["\\N".join(lines[i:i + 2]) for i in range(0, len(lines), 2)]
    weights = [max(1, count(c.replace("\\N", " "))) for c in chunks]
    total = sum(weights)
    lead, tail = 0.25, 0.35
    span = max(0.5, duration - lead - tail)
    t = start + lead
    out = []
    for c, w in zip(chunks, weights):
        d = span * w / total
        out.append((t, t + d - 0.02, c))
        t += d
    return out


def build_subtitles(ctx, rows: list[dict]) -> tuple[str, str, str]:
    h = ctx.config["headlines"]
    srt, ass_ev, transcript = [], [], []
    k = 0
    for r in rows:
        if not r.get("narration"):
            continue
        for a, b, c in caption_events(r["narration"], r["start"], r["duration"]):
            k += 1
            srt += [str(k), f"{srt_time(a)} --> {srt_time(b)}", c.replace("\\N", "\n"), ""]
            ass_ev.append(f"Dialogue: 0,{ass_time(a)},{ass_time(b)},Default,,0,0,0,,{c}")
        if r.get("credit"):
            ass_ev.append(f"Dialogue: 0,{ass_time(r['start'] + 0.25)},{ass_time(r['start'] + r['duration'] - 0.25)},Credit,,0,0,0,,SOURCE: {r['credit']}")
        transcript.append(f"[{r['id']}] {r['start']:.2f}s +{r['duration']:.2f}s  {r['narration']}" + (f"  (credit: {r['credit']})" if r.get("credit") else ""))
    ass = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: 1080", "PlayResY: 1920", "WrapStyle: 0", "ScaledBorderAndShadow: yes", "",
           "[V4+ Styles]", "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
           f"Style: Default,{h['subtitle_font']},{h['subtitle_size']},&H00FFFFFF,&H00FFFFFF,&H99000000,&H99000000,0,0,0,0,100,100,0,0,3,14,0,2,60,60,{h['subtitle_margin_v']},1",
           f"Style: Credit,{h['credit_font']},{h['credit_size']},&H00E6E6E6,&H00FFFFFF,&H99000000,&H99000000,0,0,0,0,100,100,1,0,3,8,0,2,60,60,{h['credit_margin_v']},1",
           "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"] + ass_ev
    return "\n".join(srt), "\n".join(ass) + "\n", "\n".join(transcript)


def run(ctx, extra_args=None) -> int:
    h = ctx.config["headlines"]
    ffmpeg, ffprobe = h.get("ffmpeg", "ffmpeg"), h.get("ffprobe", "ffprobe")
    if not shutil.which(ffmpeg) or not shutil.which(ffprobe):
        log.error("ffmpeg/ffprobe not found (%s, %s). Run this stage on the production PC.", ffmpeg, ffprobe)
        ctx.set_stage("s16_stitch", "external_pending", reason="ffmpeg missing")
        return RC_EXTERNAL
    inv = load_json(ctx.headlines_sup / f"Headlines_{ctx.short}_clip_inventory.json", default={})
    pack = load_json(ctx.headlines_sup / f"headlines_{ctx.short}_pack.json", default={})
    if inv.get("clip_inventory") != "PASS" or not pack:
        log.error("need a PASS clip inventory and the pack; run s15 first")
        return 1
    by_slot = {s["slot"]: s for s in pack["slots"]}
    clips = {}
    for o in inv["outputs"]:
        if o["resolution"] == [1088, 1920] and o["status"] == "AVAILABLE":
            c = next(c for c in o["candidates"] if c["usable_media"])
            clips[o["clip_id"]] = c
    rows = []
    if h.get("opening_clip"):
        rows.append({"id": "opening", "file": h["opening_clip"], "narration": "", "credit": "", "sources": [], "origin": "stored opening (permanent asset)"})
    for slot in range(2, 12):
        cid = f"C{slot:02d}"
        if cid not in clips:
            continue
        s = by_slot[slot]
        credit = CREDIT.get(s["kind"], (s.get("source") or "").upper())
        rows.append({"id": cid, "file": clips[cid]["path"], "sha256": clips[cid]["sha256"], "narration": s["script"], "caption_text": s["script"],
                     "sources": [s.get("source", "")], "credit": credit, "kind": s["kind"]})
    if h.get("ending_clip"):
        rows.append({"id": "ending", "file": h["ending_clip"], "narration": "", "credit": "", "sources": [], "origin": "stored approved ending (15 Sep 2026)"})
    t = 0.0
    problems = []
    for r in rows:
        p = Path(r["file"])
        if not p.exists():
            problems.append(f"{r['id']}: file missing {p}")
            continue
        m = probe(ffprobe, p)
        r.update({"probe": m, "start": round(t, 3), "duration": round(m["duration"], 3)})
        r.setdefault("sha256", sha256_file(p))
        if (m["width"], m["height"]) not in ((1088, 1920), (1080, 1920)):
            problems.append(f"{r['id']}: size {m['width']}x{m['height']}")
        if not m["audio"]:
            problems.append(f"{r['id']}: no audio stream")
        t += m["duration"]
    if h.get("date_overlay_png") and rows and rows[0]["id"] == "opening":
        op = Path(h["date_overlay_png"])
        rows[0]["date_overlay"] = {"file": str(op), "sha256": sha256_file(op) if op.exists() else None, "edition": ctx.edition.isoformat(),
                                   "observed_text": ctx.title_date, "reviewer": "PENDING Rafael's eyes (house rule 7)"}
        if not op.exists():
            problems.append(f"date overlay missing: {op}")
    manifest_path = ctx.headlines_sup / f"Headlines_{ctx.short}_source_manifest.json"
    save_json(manifest_path, rows)
    if problems:
        log.error("source problems: %s", problems)
        ctx.report_append("s16 stitch", "SOURCE PROBLEMS:\n" + "\n".join(f"- {x}" for x in problems))
        ctx.set_stage("s16_stitch", "failed", problems=problems)
        return 2
    srt, ass, transcript = build_subtitles(ctx, rows)
    out_mp4 = ctx.headlines / f"Headlines_{ctx.short}.mp4"
    (ctx.headlines / f"Headlines_{ctx.short}.srt").write_text(srt, encoding="utf-8")
    ass_path = ctx.headlines / f"Headlines_{ctx.short}.ass"
    ass_path.write_text(ass, encoding="utf-8")
    body = (f"Reel plan: {len(rows)} clips, {t:.2f} s total. Subtitle canvas 1080x1920 (.ass), font {h['subtitle_font']} {h['subtitle_size']}.\n"
            f"Caption timing is proportional by syllables per clip (no word-level transcription on this machine).\n\n{transcript}")
    if not require_approval(ctx, "s16_stitch", "subtitle transcript check before burning (house rule 12)", body):
        ctx.report_append("s16 stitch", "phase A done; awaiting Rafael's subtitle approval.\n" + transcript)
        ctx.set_stage("s16_stitch", "awaiting_approval", clips=len(rows), seconds=round(t, 2))
        return RC_APPROVAL
    # phase B: encode
    inputs, fc, vlabels, alabels = [], [], [], []
    for i, r in enumerate(rows):
        inputs += ["-i", r["file"]]
        crop = "crop=1080:1920:4:0," if r["probe"]["width"] == 1088 else ""
        fc.append(f"[{i}:v]{crop}fps=30,setsar=1,format=yuv420p[v{i}]")
        fc.append(f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo[a{i}]")
        vlabels.append(f"[v{i}]")
        alabels.append(f"[a{i}]")
    n = len(rows)
    if rows[0].get("date_overlay") and Path(rows[0]["date_overlay"]["file"]).exists():
        inputs += ["-i", rows[0]["date_overlay"]["file"]]
        fc.append(f"[v0][{n}:v]overlay=0:0:format=auto[v0d]")
        vlabels[0] = "[v0d]"
    fc.append("".join(f"{v}{a}" for v, a in zip(vlabels, alabels)) + f"concat=n={n}:v=1:a=1[vc][ac]")
    fonts = f":fontsdir='{ff_path(Path(h['fonts_dir']))}'" if h.get("fonts_dir") else ""
    fc.append(f"[vc]subtitles='{ff_path(ass_path)}'{fonts}[vs]")
    fc.append("[ac]loudnorm=I=-14:TP=-2:LRA=11[af]")
    rename_old(out_mp4)
    cmd = [ffmpeg, "-y", "-nostdin", "-hide_banner", *inputs, "-filter_complex", ";".join(fc), "-map", "[vs]", "-map", "[af]",
           "-c:v", "libx264", "-profile:v", "high", "-preset", "fast", "-crf", "17", "-r", "30", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", str(out_mp4)]
    (ctx.headlines_sup / f"Headlines_{ctx.short}_ffmpeg_cmd.txt").write_text(" ".join(f'"{c}"' if " " in c else c for c in cmd), encoding="utf-8")
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    (ctx.headlines_sup / f"Headlines_{ctx.short}_ffmpeg.log").write_text(proc.stderr, encoding="utf-8")
    if proc.returncode != 0 or not out_mp4.exists():
        log.error("ffmpeg failed (exit %s); see the log in supportive files", proc.returncode)
        ctx.set_stage("s16_stitch", "failed", exit=proc.returncode)
        return 2
    # evidence (house rule 5)
    m = probe(ffprobe, out_mp4)
    pk = subprocess.run([ffprobe, "-v", "error", "-select_streams", "v:0", "-count_packets", "-show_entries", "stream=nb_read_packets", "-of", "csv=p=0", str(out_mp4)],
                        capture_output=True, text=True)
    frames = int(pk.stdout.strip()) if pk.stdout.strip().isdigit() else None
    ln = subprocess.run([ffmpeg, "-nostdin", "-hide_banner", "-i", str(out_mp4), "-af", "loudnorm=I=-14:TP=-2:LRA=11:print_format=json", "-f", "null", "-"],
                        capture_output=True, text=True, encoding="utf-8", errors="replace")
    mt = re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", ln.stderr, re.S)
    loud = json.loads(mt.group(0)) if mt else {}
    frames_dir = ctx.headlines_sup / "frames"
    frames_dir.mkdir(exist_ok=True)
    shots = []
    for name, at in (("start", 1.0), ("middle", m["duration"] / 2), ("end", max(0.0, m["duration"] - 1.0))):
        fp = frames_dir / f"Headlines_{ctx.short}_{name}.png"
        subprocess.run([ffmpeg, "-y", "-nostdin", "-hide_banner", "-loglevel", "error", "-ss", f"{at:.2f}", "-i", str(out_mp4), "-frames:v", "1", str(fp)])
        shots.append(str(fp))
    qa = {"edition": ctx.edition.isoformat(), "file": out_mp4.name, "bytes": out_mp4.stat().st_size, "sha256": sha256_file(out_mp4),
          "duration_seconds": m["duration"], "expected_seconds": round(t, 3), "width": m["width"], "height": m["height"], "fps": m["fps"],
          "video_packets": frames, "audio": m["audio"], "measured_integrated_lufs": loud.get("input_i"), "measured_true_peak_dbtp": loud.get("input_tp"),
          "subtitles": {"ass": ass_path.name, "play_res": [1080, 1920], "font": h["subtitle_font"], "size": h["subtitle_size"], "box_opacity": "40 percent black"},
          "frames_for_visual_check": shots, "visual_check": "PENDING Rafael (house rule 7)", "encoded_at": dt.datetime.now().isoformat(timespec="seconds"),
          "publication_status": "not approved"}
    save_json(ctx.headlines_sup / f"Headlines_{ctx.short}_QA.json", qa)
    ctx.report_append("s16 stitch", f"{out_mp4.name}: {qa['duration_seconds']:.2f} s (expected {t:.2f}), {qa['width']}x{qa['height']}, "
                                    f"video packets {frames}, loudness {loud.get('input_i')} LUFS / TP {loud.get('input_tp')} dBTP, "
                                    f"{qa['bytes']} bytes. Frames for Rafael: {shots}")
    ctx.set_gate("headlines_render", "PASS" if abs(qa["duration_seconds"] - t) < 0.5 else "CHECK", f"{qa['duration_seconds']:.2f}s")
    ctx.set_stage("s16_stitch", "done", seconds=qa["duration_seconds"])
    return 0


if __name__ == "__main__":
    stage_main(run, __doc__)
