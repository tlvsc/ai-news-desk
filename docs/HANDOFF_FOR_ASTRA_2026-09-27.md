# Handoff for Astra (ChatGPT lane) — review of the Claude-lane V1 workflow package

Written 2026-09-27 by the Claude cloud session for Rafael's ChatGPT assistant. Purpose: give you everything needed to
make a complete, independent review of the code, scripts and workflow that the Claude lane built today, and to report
findings to Rafael in a form he can act on. This file is self-contained: the full source of every file is in the
appendix at the end. Nothing here changes the live V1 ChatGPT-lane run; it is a parallel package under test.

## 1. Context in short

- Project: AI News Desk, V1 daily chain (55 sources → pool → Full Report → Bulletin → The Bigger Picture → 15 cards →
  Headlines reel → storage). The live V1 runs in the ChatGPT lane (your lane) and must not be touched.
- The Claude lane was asked by Rafael to build a Claude Code script for the whole V1 workflow, one independent script
  per process, using a model only where a field truly needs it, planned for the fewest tokens, built in the Claude
  folder so it can be tested separately from ChatGPT. V1 only, not V2, not V1.1.
- Rafael's decisions in that session, now CLAUDE.md rules 15 to 19 of the repository: the package lives in the git
  repository folder `v1_workflow/` while it is built and tested; its authority copy goes to Drive `claude_files_only`
  as individual text files after it is finished and verified; Route B: the cloud builds and tests what it can, a Claude
  Code local session on Rafael's i9 runs the PC-only stages; model calls go through Claude Code headless subagents on
  Rafael's subscription (Haiku cheap, Sonnet mid, Opus strong), code does everything else; test runs write to a local
  PC folder only, no Drive writes; the live ChatGPT-lane V1 prompts, automations and files are never edited.
- Where the code is: GitHub repository tlvsc/ai-news-desk, branch `claude/epic-cray-meivo9`, folder `v1_workflow/`.
  Scan documents from the same morning: `docs/scan_2026-09-27/` (FINDINGS.md, drive tree, scripts index, handoff
  digest). Session handoff: `docs/HANDOFF_NEXT_SESSION.md`. House rules: `CLAUDE.md` at the repository root.

## 2. Standing rules the review must respect

1. No deletions anywhere; superseded files are renamed `*_old` (CLAUDE.md rule 3).
2. Media stays out of git; clips, masters and logo masters live on Drive (rule 9).
3. Branding is added in post with ffmpeg, never generated (rule 10).
4. Subtitles are burned from `.ass` with PlayResX 1080 and PlayResY 1920, never straight from `.srt` (rule 11).
5. The subtitle approval pause before burning is not optional (rule 12).
6. Scripts must be double-clickable and self-installing on Windows 10 22H2; check that a tool runs, not that it
   exists; python.exe may be the Microsoft Store stub (rule 13).
7. Evidence before done: real numbers, not summaries (rule 5). Claude cannot see rendered output (rule 7).
8. Content is never invented; anchor scripts, episode copy and names come from Rafael or source material (rule 6).
9. Nobody publishes; Rafael approves publication. Never run a live token-spending run or a ComfyUI generation as part
   of this review without Rafael's explicit go.
10. Editorial blueprints that the code implements, all on Drive under AI_News_Desk / Blueprint_Library:
    Cards_Master_Rules_Structure.txt (Sections 2 and 3: deck order, slots, money cap, lead with the deed, closing text),
    Headlines_Master_Rules_Structure.txt (Sections A to E: 12 slots, spoken introduction, seconds = syllables / 4.4 to
    two decimals with no rounding up, fill laws, stitch and subtitle rules, storage), the 18 Sep hard gates (every
    source terminal status, pool ≥ 300, report 50 to 150, bulletin 25 to 30, cards exactly 15, headlines 8 to 9 core,
    machine-readable checkpoint, fail-closed), the Decision Log category order of 23 Sep (critical first, then
    Politics, Market, Security, Energy, Robotics, Models, Research, Ethics and law, Health, Society, Fun), the AIND
    plain language law v1 and the 26 Sep source-to-script meaning check, AIND_daily_storage_rules.txt.

## 3. What was built

Layout of `v1_workflow/`:

    run_v1.py            orchestrator: --edition, --from/--to/--only, --llm live|dry|manual, --approve <stage>,
                         --approve-all (tests only), --override gate=reason, --force, --skip, --run-description
    RUN_V1.cmd           Windows double-click launcher; verifies Python 3.11+ actually runs, then runs run_v1.py
    config/              v1_config.json (paths, gates, models, batch sizes, headlines and cards settings, drive ids
                         with upload disabled), categories.json (11 categories, slots, aliases), sources_v1.json
                         (55 sources SRC-V1-001..055), headlines_comfy_prompt.txt ({symbol} and {script} placeholders)
    lib/common.py        RunContext (run folder mirroring the Drive product tree, state.json, gates, category order,
                         importance labels, V1_script_report.md), dates (D-M-YY, "FRI 11 SEP 2026", 09:00 window),
                         require_approval (pause files), update_checkpoint, exit codes 0 ok / 2 gate / 3 approval / 4 external
    lib/llm_client.py    one batched call per model use: live (claude -p --bare --model X --output-format json
                         --max-turns 1 --disallowedTools *), dry (deterministic stand-ins), manual (request files);
                         sha256 cache, usage and cost log work/llm_log.jsonl, one JSON-only retry
    lib/llm_dry.py       the reply contract of every prompt (the shapes stages expect)
    lib/syllables.py     override table merged from Drive syl.py and the 26 Sep fill script; count, audit, box_seconds
    llm/prompts/*.md     eleven instruction files: digest, dedupe_pairs, classify, report_story, analysis,
                         bulletin_copy, meaning_check, bigger_picture, cards_copy, headlines_copy, editorial_qa
    stages/s01..s17      one script per process (table below)
    vendor/              verbatim copy of your validate_delivery.py QA tool (s14 calls it; s13 writes its schema)
    tests/               unit tests, synthetic pool and template generators, end-to-end dry runner
    runs/<date>/         one run: state.json, V1_script_report.md, approvals/, work/, reports/, cards/, Headlines/

Stages (model tier in brackets; "PC" = needs Rafael's machine; "pause" = waits for Rafael):

| stage | tier | does | stops |
|---|---|---|---|
| s01_collect | none | RSS/Atom/HTML per source, article text once, terminal status strings, raw_pool.jsonl, source_ledger.json | |
| s02_digest | cheap | raw text → headline, summary, key_facts, entities, event_date, fun, category_guess | |
| s03_dedupe | cheap, pairs only | url match, jaccard ≥ 0.55 with shared entity → same event; 0.30..0.55 pairs to the model, capped at 240 most similar; 30-day history → PREVIOUSLY COVERED | |
| s04_classify | cheap | category, subcategory, importance 1..10, verification, why_it_matters, big_name | |
| s05_gates | none | run-checkpoint.json, major-news-gate.md, hard gates fail closed | exit 2 |
| s06_report | mid, strong once | Full Report in master-prompt story format, daily-pool.md, history append | exit 2 if < 50 |
| s07_bulletin | mid | 25..30 items, plain language, meaning check (failing rows kept flagged DRAFT) | exit 2 |
| s08_bigger_picture | strong once | analysis doc, card copy, spoken line 44..53 syllables | |
| s09_cards_select | none | paper-first deck: cover, criticals spend slots, category order, market ≤ 3, fun last, teaser 3..4, Bigger Picture, closing = 15 | exit 2 |
| s10_cards_copy | mid | card copy + meaning check, flags (two sentences, money lead) | pause |
| s11_cards_render | none | edition.json + content_lock.json, runs cards.renderer_command, verifies 15 PNG 1080x1920 + combined | PC, exit 4 |
| s12_headlines_select | mid | 7 stories in deck order, fun, teaser from the teaser card only, Bigger Picture; rewrite loop on syllables and digits; meaning check; pack + selection.md | pause, exit 2 if core ∉ 8..9 |
| s13_headlines_fill | none | fills nodes 100k+12/+13/+21/+35 by id, modes, group titles, note 9990, new id; extra.aind_headlines in your QA tool's schema; receipt | exit 2 on check failure |
| s14_validate | none | your validate_delivery.py --headlines --prompt, plus pack↔JSON consistency | exit 2 |
| s15_comfy | none | UI→API conversion via /object_info, POST /prompt, poll /history, clip inventory with your check_headlines_clips | pause, PC, exit 4 |
| s16_stitch | none | source manifest, .srt + .ass (PlayRes 1080x1920, Instrument Sans, 40% black box, credits), pause, then ffmpeg crop/concat/subtitles/loudnorm, ffprobe numbers, frames | pause, PC, exit 4 |
| s17_store | none | storage_manifest_<date>.json, drive_upload_plan.json, LLM totals | |

## 4. Evidence from the tests (dry mode, zero tokens, synthetic data)

| check | result |
|---|---|
| unit tests | 11 of 11 OK (syllable formula and five known lines from the 25 Sep sheet, dates, url normalisation, gates fail closed and override, deck rules, template fill, caption timing) |
| pool candidates (gate 300) | 330 |
| unique events / Full Report stories | 164 / 150 |
| Bulletin | 30 |
| cards planned | 15, market 3 of 3, fun last |
| Headlines core clips | 9; validate_delivery.py --headlines PASS on the filled synthetic template |
| checkpoint gates | all eight PASS |
| model calls per edition | 41: digest 9, dedupe pairs 4, classify 5, report stories 13, analysis 1, bulletin 1, meaning checks 3, bigger picture 1, cards copy 1, headlines 3 |
| exit codes | s01..s11 → 4 (no renderer here), s12..s14 → 0, s15 → 4 (no ComfyUI), s16 → 4 (no ffmpeg), s17 → 0 |

Not verified anywhere yet: live model replies against the prompts; the collector against the real publisher sites;
the card renderer command; ComfyUI queueing (UI→API conversion untested against the real node set); the ffmpeg chain
and loudness on real clips. Known limits: caption timing in s16 is proportional by syllables per clip, not word-level;
dry-mode text is synthetic and must never reach an edition; the synthetic pool is self-similar so dedupe reports
thousands of pairs kept separate.

Mistakes recorded by the Claude session: (1) helper-agent files overwritten during the Drive mirror; (2) context
compaction with uncommitted work, now CLAUDE.md rule 14; (3) first dedupe pass made 333 model calls, fixed to 4;
(4) a project rule (rule 20, dry run before live) was added without Rafael's say-so; keeping or removing it is his call.

## 5. Your review brief

Goal: an independent, complete review of the code, scripts and workflow, against the blueprints above and against
what Rafael actually asked for. Report to Rafael, not to the Claude session.

Review in this order and cover every point:

1. Editorial correctness. Does s09 implement Cards Master Section 2 exactly (criticals spend their category slot,
   category order, market cap including criticals, fun last, teaser only from uncarded items, big release rule)? Does
   s12 implement Headlines Section A (slots 2..8 stories in deck order, 9 fun, 10 teaser from the teaser card only,
   11 Bigger Picture 44..53 syllables, 12 stored ending) and Section B (spoken introduction rotating, numbers as words,
   seconds = syllables / 4.4 to two decimals)? Does s06 match the master prompt's report format and header lines?
   Does s07 select 25..30 correctly and handle meaning-check failures the way Rafael wants (kept as DRAFT)?
2. Gates and fail-closed law (18 Sep). Are all counts computed from saved files, never narrative? Are hard gates
   really closed? Is the override recorded? Is the checkpoint schema what your lane writes?
3. Token strategy. Is raw text really read once? Are batch sizes sane? Which calls could be removed or merged?
   Are the prompts tight, unambiguous, and do their reply contracts match lib/llm_dry.py exactly? Would Haiku reliably
   return the JSON shapes asked for? Any place where a strong model is used where a cheap one would do, or the reverse?
4. Headlines fill and QA schema. Compare s13 with the 26 Sep fill script (Drive claude_files_only,
   fill_headlines_26-9-26.py) and with your validate_delivery.py: does extra.aind_headlines carry every field your tool
   checks (references, syllable_audit tokenisation, intro, generation_prompt, story ids)? Does the cue line for
   Anthropic and NVIDIA satisfy your tool's cue rule? Is the prompt built from Headlines_prompt_for_comfy_json.txt with
   only the two placeholders filled?
5. s15 ComfyUI. Is the UI→API conversion sound (widgets_values_named first, positional fallback with the
   control_after_generate skip, bypassed nodes excluded, links resolved)? What will break on the real 202-node template
   with the Spectrum node? Is "never queue twice" enforced correctly? Is the clip inventory root right (prefixes start
   with video/)?
6. s16 stitch. Check the ffmpeg filter chain against Headlines Section D (crop 4 px each side to 1080x1920, 30 fps,
   yuv420p, libx264 high preset fast CRF 17, AAC 192k 48 kHz, −14 LUFS / −2 dBTP), the .ass header (PlayRes, 40 percent
   black box, two lines max, credit style), Windows path escaping inside filter strings, the date overlay, and the
   evidence written to the QA json. Say what is missing versus the blueprint (for example word-level timing).
7. Windows and self-install (rule 13). RUN_V1.cmd: does it really detect the Store stub, stale PATH, missing Python?
   Are there any non-stdlib imports anywhere? Any Linux-only assumptions (strftime %-d, path separators, shlex posix)?
8. Robustness. Resume logic in run_v1.py and state.json; what happens on a crash mid-stage; idempotency of every stage
   when re-run; file overwrite behaviour (rename_old) versus rule 3; approvals folder semantics; exit codes.
9. Collector. Feed discovery, date parsing, window check, per-source terminal statuses, politeness and timeouts, what
   counts as FAILED versus INCOMPLETE; risk of a source silently returning zero in-window items.
10. Dedupe thresholds. jaccard 0.55 auto-merge with the entity guard, 0.30 floor, cap 240, history window: where will
    it over-merge or under-merge on real news, and what cheap improvement would you make?
11. Tests. What the unit and end-to-end tests do not cover; which tests you would add before the first live day.
12. Safety. Subprocess and HTTP calls (claude CLI, ffmpeg, ComfyUI on 127.0.0.1 only), no secrets in files, no writes
    outside the run folder, Drive upload disabled by default.

How to report: numbered findings, most severe first; each with severity (blocker / should fix / nice to have), the
file and function, what is wrong, evidence, and a paste-ready fix (a diff or the replacement lines). Do not rewrite
the package wholesale; keep every fix minimal and inside the same file layout. Flag any conflict between the code and
a blueprint, a Rafael decision, or a house rule, citing where the rule lives. Never run a live token run or a ComfyUI
generation as part of the review. Put questions for Rafael in one batched list at the end, as tappable numbered
options.

How to get and run the code: clone the repository branch, or use the appendix below (every file, in order, with its
path as heading). Zero-token proof on any machine with Python 3.11+: inside `v1_workflow`, run
`python -m unittest tests.test_units -v` and `python tests/e2e_dry.py`.

---

# Appendix: full source of v1_workflow (as committed on 2026-09-27)

Generated files left out: tests/fixtures/pool_320.jsonl and tests/fixtures/template_synthetic.json (recreate them with
tests/make_fixture.py and tests/make_template.py).


## v1_workflow/README.md

```markdown
# AI News Desk V1 workflow, Claude lane

One double-click (or one command) runs the V1 chain for one edition: collect, digest, dedupe, classify, gates,
Full Report, Bulletin, The Bigger Picture, cards, Headlines reel, storage manifest. Every process is its own
script in `stages/`, resumable from `runs/<date>/state.json`. Code does everything that does not need a model;
the few model calls go through Claude Code headless subagents on Rafael's subscription and are logged with tokens
and cost. Nothing here touches the live ChatGPT-lane V1 files (CLAUDE.md rule 19).

## Run

    RUN_V1.cmd                                   Windows: checks Python actually runs, then today's edition
    python run_v1.py --edition 2026-09-27        any machine with Python 3.11+
    python run_v1.py --edition 2026-09-27 --approve s10_cards_copy      record an approval, continue
    python run_v1.py --edition 2026-09-27 --from s12 --to s14           run a range
    python run_v1.py --edition 2026-09-27 --only s09 --force            redo one stage

Exit codes: 0 done, 1 error, 2 a gate failed (fail-closed; read `V1_script_report.md`), 3 approval needed
(read `approvals/<stage>.pending.md`), 4 external step pending (needs the production PC or a tool).

## Stages

| stage | model | what | pauses |
|---|---|---|---|
| s01_collect | none | 55 sources, RSS/Atom/HTML, article text once, terminal status per source | |
| s02_digest | cheap | raw text to tiny records (headline, summary, key facts) | |
| s03_dedupe | cheap (pairs only) | same-event grouping, 30 day history | |
| s04_classify | cheap | category, importance 1 to 10, verification | |
| s05_gates | none | run-checkpoint.json, fail-closed hard gates, major-news miss gate | exit 2 |
| s06_report | mid + strong once | Full Report (50 to 150), daily-pool.md | |
| s07_bulletin | mid | 25 to 30 items, plain language, meaning check | |
| s08_bigger_picture | strong once | analysis corner, card copy, spoken line 44 to 53 syllables | |
| s09_cards_select | none | paper-first deck of 15 (criticals spend slots, category order, fun last) | |
| s10_cards_copy | mid | card copy + meaning check | Rafael approves |
| s11_cards_render | none | renderer inputs, runs `cards.renderer_command`, verifies 15 PNG 1080x1920 | PC |
| s12_headlines_select | mid | 12 slots, spoken intros, syllables / 4.4, meaning check | Rafael approves |
| s13_headlines_fill | none | fills the Comfy master template by node id, mirror and stale checks | |
| s14_validate | none | vendored Drive QA tool + pack consistency | exit 2 on FAIL |
| s15_comfy | none | queue on local ComfyUI, wait, clip inventory with ffprobe | Rafael's go, PC |
| s16_stitch | none | .ass (PlayRes 1080x1920) + .srt, then ffmpeg encode, loudness, frames, QA json | Rafael approves subtitles, PC |
| s17_store | none | storage manifest, Drive upload plan (no upload in test) | |

## LLM modes

`--llm live` runs `claude -p --bare --model <haiku|sonnet|opus> --output-format json --max-turns 1` per batch.
`--llm dry` uses deterministic stand-ins (`lib/llm_dry.py`) so the whole chain runs with zero tokens.
`--llm manual` writes request files to `work/llm_requests/` for a subagent to answer into `work/llm_replies/`.
Usage and cost per call: `work/llm_log.jsonl`; totals in the storage manifest.

## Folders

    config/      v1_config.json (paths, gates, models), categories.json, sources_v1.json, headlines_comfy_prompt.txt
    lib/         common.py (run context, dates, approvals), llm_client.py, llm_dry.py, syllables.py
    llm/prompts/ one instruction file per model call; reply shapes match lib/llm_dry.py
    stages/      s01 to s17
    vendor/      validate_delivery.py, the Drive QA tool (verbatim copy, see vendor/README.md)
    tests/       unit tests, synthetic pool and template, end-to-end dry runner
    runs/<date>/ one run: state.json, V1_script_report.md, approvals/, work/, reports/, cards/, Headlines/

## Tests

    python -m unittest tests.test_units -v
    python tests/e2e_dry.py            whole chain, dry LLM, synthetic 330-item pool and synthetic template

## Before the first real run on the PC

1. `config/v1_config.json`: set `headlines.comfy_template` (local copy of the master template), `headlines.opening_clip`,
   `headlines.ending_clip`, `headlines.date_overlay_png`, `headlines.fonts_dir`, `cards.renderer_command`.
2. Check the two reference poses in the template, then set `headlines.reference_images_visually_verified` to true.
3. Claude Code CLI installed and logged in (`claude --version`), ffmpeg and ffprobe on PATH, ComfyUI open for s15.
4. Test runs keep `drive.upload_enabled` false. Drive uploads are a separate, approved step.
```

## v1_workflow/RUN_V1.cmd

```bat
@echo off
setlocal EnableExtensions
rem AI News Desk V1 workflow (Claude lane). Double-click to run today's edition.
rem House rule 13: check that Python RUNS (the Microsoft Store stub only opens the Store), never that it merely exists.
cd /d "%~dp0"
set "PY="
for %%C in ("py -3" "python" "python3") do (
  if not defined PY (
    %%~C -c "import sys; sys.exit(0 if sys.version_info >= (3, 11) else 1)" >nul 2>&1
    if not errorlevel 1 set "PY=%%~C"
  )
)
if not defined PY (
  echo.
  echo Python 3.11 or newer was not found, or python.exe is the Microsoft Store stub.
  echo Install it from https://www.python.org/downloads/windows/  and tick "Add python.exe to PATH".
  echo After installing, close this window and double-click RUN_V1.cmd again (PATH is stale until then).
  start "" https://www.python.org/downloads/windows/
  pause
  exit /b 1
)
echo Using: %PY%
%PY% -c "import sys; print('Python', sys.version.split()[0])"
echo.
echo Nothing else is installed: the workflow uses the Python standard library only.
echo LLM stages call the Claude Code CLI (claude) on Rafael's subscription; ffmpeg and ComfyUI are used only by s15 and s16.
echo.
set "ARGS=%*"
if "%ARGS%"=="" set "ARGS=--edition today --run-description "double-click run""
%PY% run_v1.py %ARGS%
set "RC=%errorlevel%"
echo.
if "%RC%"=="0" echo DONE. Read runs\^<date^>\V1_script_report.md for the evidence.
if "%RC%"=="2" echo STOPPED: a gate failed. Read runs\^<date^>\V1_script_report.md. Rafael may override with --override gate=reason.
if "%RC%"=="3" echo PAUSED: approval needed. Read runs\^<date^>\approvals\*.pending.md then run: RUN_V1.cmd --edition ^<date^> --approve ^<stage^>
if "%RC%"=="4" echo PAUSED: this step needs the production PC or a tool (ComfyUI, ffmpeg, the card renderer). See the *_PENDING.md file named in the log.
if "%RC%"=="1" echo ERROR: see runs\^<date^>\work\run.log
pause
exit /b %RC%
```

## v1_workflow/run_v1.py

```python
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
```

## v1_workflow/.gitignore

```text
runs/
history/
__pycache__/
*.pyc
```

## v1_workflow/config/v1_config.json

```json
{
  "_comment": "AI News Desk V1 workflow config. Edit paths for the machine that runs it. Nothing here changes live V1 (ChatGPT lane).",
  "lane": "VL1",
  "timezone": "Asia/Jerusalem",
  "window_hour": 9,
  "local_root": "./runs",
  "history_root": "./history",
  "products": {
    "cards": "cards",
    "headlines": "Headlines",
    "reports": "reports",
    "supportive": "supportive files"
  },
  "gates": {
    "pool_min": 300,
    "report_min": 50,
    "report_max": 150,
    "bulletin_min": 25,
    "bulletin_max": 30,
    "cards_count": 15,
    "headlines_core_min": 8,
    "headlines_core_max": 9,
    "dedupe_history_days": 30,
    "previously_covered_days": 7
  },
  "collector": {
    "timeout_seconds": 20,
    "retries": 2,
    "per_domain_delay_seconds": 1.5,
    "max_items_per_source": 80,
    "article_text_chars": 2500,
    "user_agent": "AINewsDesk-V1-collector/1.0 (+contact: AI.news.desk.il@gmail.com)"
  },
  "llm": {
    "mode": "live",
    "cli": "claude",
    "models": {
      "cheap": "haiku",
      "mid": "sonnet",
      "strong": "opus"
    },
    "effort": {
      "cheap": "low",
      "mid": "medium",
      "strong": "high"
    },
    "batch_sizes": {
      "digest": 40,
      "classify": 40,
      "dedupe_pairs": 60,
      "report": 12,
      "copy": 20
    },
    "max_retries": 1,
    "timeout_seconds": 600,
    "max_dedupe_pairs": 240
  },
  "headlines": {
    "syllables_per_second": 4.4,
    "story_target_syllables": 35,
    "story_box_min": 7.0,
    "story_box_max": 9.0,
    "bigger_picture_syllables": [
      44,
      53
    ],
    "content_target_seconds": 90,
    "template_json": "",
    "prompt_file": "",
    "approved_ending": "Those were today's headlines in ninety seconds. For more detailed coverage, read our daily news cards. Thank you for tuning in, and we'll see you tomorrow.",
    "opening_clip": "",
    "ending_clip": "",
    "date_overlay_png": "",
    "comfy_url": "http://127.0.0.1:8188",
    "comfy_output_dir": "E:/ComfyUI/output/video",
    "ffmpeg": "ffmpeg",
    "ffprobe": "ffprobe",
    "subtitle_font": "Instrument Sans",
    "subtitle_size": 52,
    "subtitle_margin_v": 380,
    "credit_font": "Red Hat Mono",
    "credit_size": 30,
    "credit_margin_v": 300,
    "pronunciation_cues": {
      "Anthropic": "an-thropic",
      "NVIDIA": "N-vidia"
    },
    "reference_images_visually_verified": false,
    "comfy_template": "",
    "comfy_output_root": ""
  },
  "cards": {
    "renderer_package_dir": "",
    "previous_cover_png": "",
    "fonts_dir": "",
    "closing_head": "Like, follow and share.",
    "closing_body": "That was today’s headlines in cards. Soon, subscribers and followers will get access to our full daily report and industry analysis helping investors understand the bigger picture behind AI developments.\n\nIf this adds value to your day, share it with someone who should know. Thank you, and see you tomorrow.",
    "teaser_title": "More in the full report",
    "teaser_closing_line": "Want the whole picture every morning?",
    "analysis_corner": "The Bigger Picture",
    "analysis_opening": "And for the bigger picture…",
    "notice": "General news and commentary.\nNot financial advice.",
    "renderer_command": ""
  },
  "drive": {
    "daily_root_id": "1nzOWXclWAExDQ6WqQ2C9DmSkM3rrqLYx",
    "claude_test_root_id": "",
    "upload_enabled": false
  },
  "_keys": {
    "headlines.comfy_template": "local path of Aind_headlines_comfy_Master_workflow_template.json (Drive ID 1iGUq1LtGtVm1toPhDTqhWOC4qIjIe2xV)",
    "headlines.comfy_output_root": "ComfyUI output root; empty = parent of comfy_output_dir (prefixes start with video/)",
    "headlines.reference_images_visually_verified": "Rafael sets true after checking the two reference poses in the template; the QA tool requires it",
    "headlines.pronunciation_cues": "real name -> spoken cue line added to the Comfy prompt (15 Sep rule)",
    "cards.renderer_command": "command with {edition_json} {out_dir} {renderer_dir} placeholders; empty = render pending on the PC",
    "llm.max_dedupe_pairs": "most similar ambiguous pairs sent to the cheap model per run (240 = 4 calls of 60); the rest stay separate"
  }
}
```

## v1_workflow/config/categories.json

```json
{
  "_comment": "Rafael-approved V1 general order of categories, 23 September 2026 (Decision Log). Critical stories lead regardless of category. cards_slots = default slot plan from the AIMD LV1 skill (13 Sep): total 13 story slots + cover + teaser + Bigger Picture + closing = 15 with market capped at 3 including criticals. Fun is always the last story.",
  "order": [
    {"key": "POL", "name": "Politics and government of AI", "cards_slots": 1, "aliases": ["politics", "government", "policy", "geopolitics", "defense", "sovereign"]},
    {"key": "MKT", "name": "Market, industry and finance", "cards_slots": 3, "aliases": ["market", "industry", "finance", "stocks", "funding", "earnings", "companies", "startups"]},
    {"key": "SEC", "name": "Security and cyber", "cards_slots": 1, "aliases": ["security", "cyber", "cybersecurity", "safety", "privacy", "fraud", "attack"]},
    {"key": "ENE", "name": "Energy and infrastructure", "cards_slots": 1, "aliases": ["energy", "infrastructure", "data center", "data centre", "chips", "hardware", "power", "grid", "semiconductor"]},
    {"key": "ROB", "name": "Robotics", "cards_slots": 1, "aliases": ["robotics", "robot", "humanoid", "autonomous", "drone", "self-driving", "driverless"]},
    {"key": "MOD", "name": "Models and tools", "cards_slots": 1, "aliases": ["models", "tools", "agents", "products", "apps", "open source", "developer", "benchmark", "release"]},
    {"key": "RES", "name": "Research and science", "cards_slots": 1, "aliases": ["research", "science", "paper", "study", "physics", "biology", "chemistry", "materials"]},
    {"key": "LAW", "name": "Ethics and law", "cards_slots": 1, "aliases": ["ethics", "law", "court", "lawsuit", "copyright", "regulation", "antitrust", "liability"]},
    {"key": "HEA", "name": "Health", "cards_slots": 1, "aliases": ["health", "healthcare", "medical", "hospital", "drug", "biotech", "patients"]},
    {"key": "SOC", "name": "Society and education", "cards_slots": 1, "aliases": ["society", "education", "jobs", "schools", "universities", "culture", "media", "misinformation"]},
    {"key": "FUN", "name": "Fun and humour", "cards_slots": 1, "aliases": ["fun", "humour", "humor", "viral", "quirky", "gaming", "entertainment"]}
  ],
  "market_max_including_criticals": 3,
  "min_non_business_stories": 3,
  "robotics_required": true,
  "fun_required": true,
  "importance_labels": {"10": "CRITICAL", "8": "HIGH", "6": "MEDIUM", "1": "WATCHLIST"},
  "verification_statuses": ["CONFIRMED", "REPORTED", "PRELIMINARY", "DISPUTED"],
  "dispositions": ["RETAINED EVENT ID", "DUPLICATE OF", "PREVIOUSLY COVERED", "OUT OF WINDOW", "UNVERIFIED", "LOW MATERIALITY", "HELD FOR REVIEW", "NOT AI-RELEVANT"]
}
```

## v1_workflow/config/sources_v1.json

```json
{
  "_comment": "V1 source registry: the 'five per category source list' sheet in 00 - PROJECT OS (23 Sep 2026), 55 sources. feed_url is a discovery hint only; s01_collect verifies each route and records a terminal status per source. Collector access was never tested by the sheet author.",
  "registry_name": "five per category source list",
  "registry_drive_id": "1AEEnJnZE56IqENyEymuwkmiEFDqr6eIbsYVh1Pz3xxI",
  "sources": [
    {"id": "SRC-V1-001", "category": "POL", "name": "Reuters", "url": "https://www.reuters.com/technology/", "feed_url": null},
    {"id": "SRC-V1-002", "category": "POL", "name": "Associated Press", "url": "https://apnews.com/technology", "feed_url": null},
    {"id": "SRC-V1-003", "category": "POL", "name": "POLITICO", "url": "https://www.politico.eu/section/technology/", "feed_url": "https://www.politico.eu/section/technology/feed/"},
    {"id": "SRC-V1-004", "category": "POL", "name": "Financial Times", "url": "https://www.ft.com/artificial-intelligence", "feed_url": "https://www.ft.com/artificial-intelligence?format=rss"},
    {"id": "SRC-V1-005", "category": "POL", "name": "South China Morning Post", "url": "https://www.scmp.com/tech", "feed_url": "https://www.scmp.com/rss/36/feed"},
    {"id": "SRC-V1-006", "category": "MKT", "name": "Reuters Business", "url": "https://www.reuters.com/business/", "feed_url": null},
    {"id": "SRC-V1-007", "category": "MKT", "name": "Bloomberg", "url": "https://www.bloomberg.com/technology", "feed_url": null},
    {"id": "SRC-V1-008", "category": "MKT", "name": "Financial Times", "url": "https://www.ft.com/artificial-intelligence", "feed_url": "https://www.ft.com/artificial-intelligence?format=rss"},
    {"id": "SRC-V1-009", "category": "MKT", "name": "Wall Street Journal", "url": "https://www.wsj.com/tech/ai", "feed_url": null},
    {"id": "SRC-V1-010", "category": "MKT", "name": "Yicai Global", "url": "https://www.yicaiglobal.com/", "feed_url": null},
    {"id": "SRC-V1-011", "category": "SEC", "name": "BleepingComputer", "url": "https://www.bleepingcomputer.com/", "feed_url": "https://www.bleepingcomputer.com/feed/"},
    {"id": "SRC-V1-012", "category": "SEC", "name": "Dark Reading", "url": "https://www.darkreading.com/", "feed_url": "https://www.darkreading.com/rss.xml"},
    {"id": "SRC-V1-013", "category": "SEC", "name": "The Record", "url": "https://therecord.media/", "feed_url": "https://therecord.media/feed"},
    {"id": "SRC-V1-014", "category": "SEC", "name": "SecurityWeek", "url": "https://www.securityweek.com/", "feed_url": "https://www.securityweek.com/feed/"},
    {"id": "SRC-V1-015", "category": "SEC", "name": "Krebs on Security", "url": "https://krebsonsecurity.com/", "feed_url": "https://krebsonsecurity.com/feed/"},
    {"id": "SRC-V1-016", "category": "ENE", "name": "Data Center Dynamics", "url": "https://www.datacenterdynamics.com/", "feed_url": "https://www.datacenterdynamics.com/en/rss/"},
    {"id": "SRC-V1-017", "category": "ENE", "name": "Data Center Frontier", "url": "https://www.datacenterfrontier.com/", "feed_url": "https://www.datacenterfrontier.com/rss"},
    {"id": "SRC-V1-018", "category": "ENE", "name": "Utility Dive", "url": "https://www.utilitydive.com/", "feed_url": "https://www.utilitydive.com/feeds/news/"},
    {"id": "SRC-V1-019", "category": "ENE", "name": "Canary Media", "url": "https://www.canarymedia.com/", "feed_url": "https://www.canarymedia.com/rss"},
    {"id": "SRC-V1-020", "category": "ENE", "name": "SemiAnalysis", "url": "https://semianalysis.com/", "feed_url": "https://semianalysis.com/feed/"},
    {"id": "SRC-V1-021", "category": "ROB", "name": "The Robot Report", "url": "https://www.therobotreport.com/", "feed_url": "https://www.therobotreport.com/feed/"},
    {"id": "SRC-V1-022", "category": "ROB", "name": "IEEE Spectrum", "url": "https://spectrum.ieee.org/", "feed_url": "https://spectrum.ieee.org/feeds/feed.rss"},
    {"id": "SRC-V1-023", "category": "ROB", "name": "Robotics 24/7", "url": "https://www.robotics247.com/", "feed_url": "https://www.robotics247.com/rss/news"},
    {"id": "SRC-V1-024", "category": "ROB", "name": "Robotics & Automation News", "url": "https://roboticsandautomationnews.com/", "feed_url": "https://roboticsandautomationnews.com/feed/"},
    {"id": "SRC-V1-025", "category": "ROB", "name": "Live Science Robotics", "url": "https://www.livescience.com/technology/robotics", "feed_url": "https://www.livescience.com/feeds/all"},
    {"id": "SRC-V1-026", "category": "MOD", "name": "TechCrunch", "url": "https://techcrunch.com/", "feed_url": "https://techcrunch.com/category/artificial-intelligence/feed/"},
    {"id": "SRC-V1-027", "category": "MOD", "name": "The Verge", "url": "https://www.theverge.com/", "feed_url": "https://www.theverge.com/rss/ai-artificial-intelligence/index.xml"},
    {"id": "SRC-V1-028", "category": "MOD", "name": "Ars Technica", "url": "https://arstechnica.com/", "feed_url": "https://feeds.arstechnica.com/arstechnica/technology-lab"},
    {"id": "SRC-V1-029", "category": "MOD", "name": "VentureBeat", "url": "https://venturebeat.com/", "feed_url": "https://venturebeat.com/category/ai/feed/"},
    {"id": "SRC-V1-030", "category": "MOD", "name": "The Decoder", "url": "https://the-decoder.com/", "feed_url": "https://the-decoder.com/feed/"},
    {"id": "SRC-V1-031", "category": "RES", "name": "Nature News", "url": "https://www.nature.com/news", "feed_url": "https://www.nature.com/nature.rss"},
    {"id": "SRC-V1-032", "category": "RES", "name": "Science", "url": "https://www.science.org/news", "feed_url": "https://www.science.org/rss/news_current.xml"},
    {"id": "SRC-V1-033", "category": "RES", "name": "MIT Technology Review", "url": "https://www.technologyreview.com/", "feed_url": "https://www.technologyreview.com/feed/"},
    {"id": "SRC-V1-034", "category": "RES", "name": "New Scientist", "url": "https://www.newscientist.com/", "feed_url": "https://www.newscientist.com/subject/technology/feed/"},
    {"id": "SRC-V1-035", "category": "RES", "name": "Science News", "url": "https://www.sciencenews.org/", "feed_url": "https://www.sciencenews.org/feed"},
    {"id": "SRC-V1-036", "category": "LAW", "name": "Reuters Legal", "url": "https://www.reuters.com/legal/", "feed_url": null},
    {"id": "SRC-V1-037", "category": "LAW", "name": "MLex", "url": "https://www.mlex.com/mlex/artificial-intelligence", "feed_url": null},
    {"id": "SRC-V1-038", "category": "LAW", "name": "Law360", "url": "https://www.law360.com/", "feed_url": null},
    {"id": "SRC-V1-039", "category": "LAW", "name": "Lawfare", "url": "https://www.lawfaremedia.org/topics/artificial-intelligence", "feed_url": "https://www.lawfaremedia.org/feeds/all.rss"},
    {"id": "SRC-V1-040", "category": "LAW", "name": "AlgorithmWatch", "url": "https://algorithmwatch.org/en/", "feed_url": "https://algorithmwatch.org/en/feed/"},
    {"id": "SRC-V1-041", "category": "HEA", "name": "STAT", "url": "https://www.statnews.com/topic/artificial-intelligence/", "feed_url": "https://www.statnews.com/feed/"},
    {"id": "SRC-V1-042", "category": "HEA", "name": "Fierce Healthcare", "url": "https://www.fiercehealthcare.com/", "feed_url": "https://www.fiercehealthcare.com/rss/xml"},
    {"id": "SRC-V1-043", "category": "HEA", "name": "Healthcare IT News", "url": "https://www.healthcareitnews.com/", "feed_url": "https://www.healthcareitnews.com/home/feed"},
    {"id": "SRC-V1-044", "category": "HEA", "name": "MobiHealthNews", "url": "https://www.mobihealthnews.com/", "feed_url": "https://www.mobihealthnews.com/feed"},
    {"id": "SRC-V1-045", "category": "HEA", "name": "MedTech Dive", "url": "https://www.medtechdive.com/", "feed_url": "https://www.medtechdive.com/feeds/news/"},
    {"id": "SRC-V1-046", "category": "SOC", "name": "The Guardian Technology", "url": "https://www.theguardian.com/technology", "feed_url": "https://www.theguardian.com/technology/artificialintelligenceai/rss"},
    {"id": "SRC-V1-047", "category": "SOC", "name": "Rest of World", "url": "https://restofworld.org/", "feed_url": "https://restofworld.org/feed/latest/"},
    {"id": "SRC-V1-048", "category": "SOC", "name": "Education Week", "url": "https://www.edweek.org/", "feed_url": "https://www.edweek.org/feed"},
    {"id": "SRC-V1-049", "category": "SOC", "name": "Inside Higher Ed", "url": "https://www.insidehighered.com/", "feed_url": "https://www.insidehighered.com/rss.xml"},
    {"id": "SRC-V1-050", "category": "SOC", "name": "WIRED", "url": "https://www.wired.com/tag/artificial-intelligence/", "feed_url": "https://www.wired.com/feed/tag/ai/latest/rss"},
    {"id": "SRC-V1-051", "category": "FUN", "name": "AI Weirdness", "url": "https://www.aiweirdness.com/", "feed_url": "https://www.aiweirdness.com/rss/"},
    {"id": "SRC-V1-052", "category": "FUN", "name": "IEEE Spectrum Video Friday", "url": "https://spectrum.ieee.org/", "feed_url": "https://spectrum.ieee.org/feeds/topic/robotics.rss"},
    {"id": "SRC-V1-053", "category": "FUN", "name": "Gizmodo", "url": "https://gizmodo.com/tech/artificial-intelligence", "feed_url": "https://gizmodo.com/feed"},
    {"id": "SRC-V1-054", "category": "FUN", "name": "Engadget", "url": "https://www.engadget.com/category/ai/", "feed_url": "https://www.engadget.com/rss.xml"},
    {"id": "SRC-V1-055", "category": "FUN", "name": "PC Gamer", "url": "https://www.pcgamer.com/", "feed_url": "https://www.pcgamer.com/rss/"}
  ]
}
```

## v1_workflow/config/headlines_comfy_prompt.txt

```text
A photorealistic television news anchor speaks directly to camera in a modern broadcast studio. The anchor and studio remain exactly as the reference start frame: same man, bald head, trimmed styled beard, dark navy suit, white shirt, dark tie, seated at the curved desk on the left of the frame, same lighting, same navy-blue-and-cyan newsroom, same rear displays. The glass hologram panel on the right of the frame stays in place and the logo 
<0.5s> logo on blue holographic screen change slowly and shows {symbol}. No people, no faces. No readable text, no letters, no numbers, no company names or logos, no flags, no dates. <for 5 seconds>, then goes back to start point with the  same logo as started. <0.5 second> At same time The anchor says exactly, in natural English, warm articulate authoritative news presenter tone, clear and easy to understand and with hands, body and head movements that fits the context: "{script}" at the end of the sentence he puts his hands on the table and move back to the same position he started <reference image 01>. 
He holds steady professional news energy. He stays the same person in one continuous stable broadcast. In the final second he settles and rests his hands together on the desk. 
Static camera, locked framing, no camera movement. Natural subtle head and hand movement only. Accurate lip synchronization to the spoken words. Natural eyes, natural skin. 
Audio: the anchor's voice only, with quiet professional studio ambience. No music. 
Exclusions: no captions, no subtitles, no lower thirds, no ticker, no on-screen text, no date, no logo redesign, no second person, no camera shake, no zoom, no cuts, no scene change, no morphing, no plastic skin, no hollow eyes.
```

## v1_workflow/lib/common.py

```python
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
        self.auto_approve = False  # set by run_v1.py --approve-all for dry test runs only

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


RC_OK, RC_GATE, RC_APPROVAL, RC_EXTERNAL = 0, 2, 3, 4  # stage exit codes


def require_approval(ctx, stage: str, title: str, body_md: str) -> bool:
    """Rafael's approval pause (house rules 4 and 12). Always refreshes approvals/<stage>.pending.md; returns True only
    when approvals/<stage>.approved exists, or when ctx.auto_approve is set for a dry test run."""
    ctx.approvals.mkdir(parents=True, exist_ok=True)
    flag = ctx.approvals / f"{stage}.approved"
    pending = ctx.approvals / f"{stage}.pending.md"
    pending.write_text(f"# APPROVAL NEEDED: {title}\n\nEdition {ctx.edition.isoformat()}. Read the draft below. To approve, run\n\n"
                       f"    python run_v1.py --edition {ctx.edition.isoformat()} --approve {stage}\n\n"
                       f"which creates {flag.name} in the approvals folder, then re-run. Nothing downstream runs before that.\n\n"
                       f"{body_md.rstrip()}\n", encoding="utf-8")
    if getattr(ctx, "auto_approve", False):
        log.warning("%s: auto-approved (test run only, never for a real edition)", stage)
        return True
    return flag.exists()


def update_checkpoint(ctx, fields: dict | None = None, stages: dict | None = None) -> None:
    """Patch reports/supportive files/run-checkpoint.json written by s05 with later counts and gate results."""
    path = ctx.reports_sup / "run-checkpoint.json"
    cp = load_json(path, default={"edition": ctx.edition.isoformat(), "stages": {}})
    cp.update(fields or {})
    cp.setdefault("stages", {}).update(stages or {})
    save_json(path, cp)


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
```

## v1_workflow/lib/llm_client.py

````python
"""LLM access for the V1 workflow: Claude Code in headless print mode on Rafael's subscription.

Design (26 Sep 2026 handoff, Model Setup Comparison 25 Sep):
  * Every call is ONE batch over compact records. Raw article text is read once, in s02, and never again.
  * Three tiers: cheap (digest, classify, duplicate pairs), mid (writing copy), strong (analysis, final QA).
  * Every call is logged with tokens and cost to work/llm_log.jsonl so the daily budget is measured, not guessed.
  * Modes: live = run `claude -p`; dry = deterministic placeholders so the whole pipeline can be exercised without
    tokens; manual = write the request to work/llm_requests/ and stop, for a Claude Code session to answer
    with a subagent and drop the reply in work/llm_replies/.
The model receives only the prompt file plus the JSON payload. It gets no tools and one turn.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import time
from pathlib import Path

from .common import PKG_ROOT, log

PROMPTS_DIR = PKG_ROOT / "llm" / "prompts"
SYSTEM_PROMPT = ("You are a precise newsroom assistant for AI News Desk. You receive one instruction file and one JSON "
                 "payload. Follow the instruction file exactly. Reply with JSON only: no prose, no markdown fences, "
                 "no explanations. Never invent a link, date, number, quote or fact that is not in the payload.")


class LLMError(RuntimeError):
    pass


class LLMClient:
    def __init__(self, ctx, mode: str | None = None):
        self.ctx = ctx
        self.cfg = ctx.config.get("llm", {})
        self.mode = mode or ctx.llm_mode or "live"
        self.log_path = ctx.work / "llm_log.jsonl"
        self.req_dir = ctx.work / "llm_requests"
        self.rep_dir = ctx.work / "llm_replies"

    # ------------------------------------------------------------------ public
    def call(self, tier: str, prompt_name: str, payload, *, stage: str, expect: str = "object"):
        """Return parsed JSON (object or list). Raises LLMError after retries."""
        prompt_text = (PROMPTS_DIR / f"{prompt_name}.md").read_text(encoding="utf-8")
        body = prompt_text.rstrip() + "\n\nPAYLOAD (JSON):\n" + json.dumps(payload, ensure_ascii=False)
        key = hashlib.sha256(body.encode("utf-8")).hexdigest()[:16]
        cached = self._cached(key)
        if cached is not None:
            log.info("llm %s/%s: cached reply %s", stage, prompt_name, key)
            return cached
        if self.mode == "dry":
            from . import llm_dry
            reply = llm_dry.answer(prompt_name, payload)
            self._log(stage, prompt_name, tier, "dry", key, {}, 0.0)
            return reply
        if self.mode == "manual":
            self.req_dir.mkdir(parents=True, exist_ok=True)
            req = self.req_dir / f"{stage}_{prompt_name}_{key}.md"
            req.write_text(SYSTEM_PROMPT + "\n\n" + body, encoding="utf-8")
            reply_path = self.rep_dir / f"{stage}_{prompt_name}_{key}.json"
            if reply_path.exists():
                return self._parse(reply_path.read_text(encoding="utf-8"), expect)
            raise LLMError(f"MANUAL MODE: answer the request in {req} with a {tier} subagent and save the JSON reply "
                           f"to {reply_path}, then re-run the stage.")
        return self._live(tier, prompt_name, body, key, stage, expect)

    # ------------------------------------------------------------------ live
    def _live(self, tier, prompt_name, body, key, stage, expect):
        model = self.cfg.get("models", {}).get(tier, tier)
        effort = self.cfg.get("effort", {}).get(tier)
        exe = shutil.which(self.cfg.get("cli", "claude")) or shutil.which("claude.cmd") or self.cfg.get("cli", "claude")
        cmd = [exe, "-p", "--bare", "--model", model, "--output-format", "json", "--max-turns", "1",
               "--system-prompt", SYSTEM_PROMPT, "--disallowedTools", "*"]
        if effort:
            cmd += ["--effort", effort]
        attempts = 1 + int(self.cfg.get("max_retries", 1))
        last_err = None
        for attempt in range(1, attempts + 1):
            t0 = time.time()
            try:
                proc = subprocess.run(cmd, input=body, text=True, capture_output=True,
                                      timeout=int(self.cfg.get("timeout_seconds", 600)), encoding="utf-8")
            except (subprocess.TimeoutExpired, FileNotFoundError) as exc:
                last_err = f"{type(exc).__name__}: {exc}"
                log.warning("llm %s attempt %d failed: %s", prompt_name, attempt, last_err)
                continue
            if proc.returncode != 0:
                last_err = f"exit {proc.returncode}: {proc.stderr[-800:]}"
                log.warning("llm %s attempt %d failed: %s", prompt_name, attempt, last_err)
                continue
            try:
                envelope = json.loads(proc.stdout)
            except json.JSONDecodeError:
                envelope = {"result": proc.stdout}
            usage = envelope.get("usage", {})
            cost = float(envelope.get("total_cost_usd", 0.0) or 0.0)
            text = envelope.get("result", "") if isinstance(envelope, dict) else str(envelope)
            self._log(stage, prompt_name, tier, model, key, usage, cost, seconds=round(time.time() - t0, 1))
            try:
                parsed = self._parse(text, expect)
            except LLMError as exc:
                last_err = str(exc)
                log.warning("llm %s attempt %d: bad JSON (%s)", prompt_name, attempt, last_err[:200])
                body = body + "\n\nYour previous reply was not valid JSON. Reply with the JSON only."
                continue
            self._store(key, parsed)
            return parsed
        raise LLMError(f"{stage}/{prompt_name}: no valid reply after {attempts} attempts: {last_err}")

    # ------------------------------------------------------------------ helpers
    @staticmethod
    def _parse(text: str, expect: str):
        t = text.strip()
        t = re.sub(r"^```(?:json)?\s*|\s*```$", "", t, flags=re.S)
        start = t.find("[") if expect == "list" else t.find("{")
        end = t.rfind("]") if expect == "list" else t.rfind("}")
        if start < 0 or end < 0:
            raise LLMError("no JSON found in reply")
        try:
            return json.loads(t[start:end + 1])
        except json.JSONDecodeError as exc:
            raise LLMError(f"invalid JSON: {exc}") from exc

    def _cache_path(self, key: str) -> Path:
        return self.ctx.work / "llm_cache" / f"{key}.json"

    def _cached(self, key: str):
        p = self._cache_path(key)
        if p.exists():
            return json.loads(p.read_text(encoding="utf-8"))
        return None

    def _store(self, key: str, parsed) -> None:
        p = self._cache_path(key)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(parsed, ensure_ascii=False), encoding="utf-8")

    def _log(self, stage, prompt_name, tier, model, key, usage, cost, seconds=0.0):
        row = {"at": time.strftime("%Y-%m-%dT%H:%M:%S"), "stage": stage, "prompt": prompt_name, "tier": tier,
               "model": model, "key": key, "seconds": seconds, "cost_usd": cost,
               "input_tokens": usage.get("input_tokens"), "output_tokens": usage.get("output_tokens"),
               "cache_read": usage.get("cache_read_input_tokens"), "cache_create": usage.get("cache_creation_input_tokens")}
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        with self.log_path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(row) + "\n")

    def summary(self) -> dict:
        rows = []
        if self.log_path.exists():
            rows = [json.loads(l) for l in self.log_path.read_text(encoding="utf-8").splitlines() if l.strip()]
        out = {"calls": len(rows), "cost_usd": round(sum(r.get("cost_usd") or 0 for r in rows), 4),
               "input_tokens": sum(r.get("input_tokens") or 0 for r in rows),
               "output_tokens": sum(r.get("output_tokens") or 0 for r in rows),
               "cache_read": sum(r.get("cache_read") or 0 for r in rows), "by_model": {}}
        for r in rows:
            m = out["by_model"].setdefault(r.get("model"), {"calls": 0, "cost_usd": 0.0})
            m["calls"] += 1
            m["cost_usd"] = round(m["cost_usd"] + (r.get("cost_usd") or 0), 4)
        return out


def batched(items: list, size: int):
    for i in range(0, len(items), max(1, size)):
        yield items[i:i + size]
````

## v1_workflow/lib/llm_dry.py

```python
"""Deterministic stand-ins for every LLM prompt, so the pipeline can be tested end to end with zero tokens.

The output shapes here ARE the contract each stage expects from the real model. Keep them in step with
llm/prompts/*.md. Content is obviously synthetic (marked DRY) and must never reach a real edition.
"""
from __future__ import annotations

import hashlib
import re

CATS = ["Politics and government of AI", "Market, industry and finance", "Security and cyber",
        "Energy and infrastructure", "Robotics", "Models and tools", "Research and science", "Ethics and law",
        "Health", "Society and education", "Fun and humour"]
KEYS = ["POL", "MKT", "SEC", "ENE", "ROB", "MOD", "RES", "LAW", "HEA", "SOC", "FUN"]


def _h(s: str, mod: int) -> int:
    return int(hashlib.md5(s.encode("utf-8")).hexdigest(), 16) % mod


def _sentences(text: str, n: int) -> str:
    parts = [p.strip() for p in re.split(r"(?<=[.!?])\s+", (text or "").strip()) if p.strip()]
    return " ".join(parts[:n]) if parts else "DRY summary."


def answer(prompt_name: str, payload):
    fn = globals().get("p_" + prompt_name)
    if fn is None:
        raise ValueError(f"no dry answer for prompt {prompt_name}")
    return fn(payload)


def p_digest(payload):
    out = []
    for it in payload["items"]:
        text = it.get("text") or it.get("title", "")
        cat = it.get("category_hint") or KEYS[_h(it["id"], len(KEYS))]
        out.append({"id": it["id"], "headline": it.get("title", "")[:140],
                    "summary": _sentences(text, 2)[:400], "key_facts": [_sentences(text, 1)[:160], "DRY fact"],
                    "entities": [w for w in re.findall(r"\b[A-Z][a-zA-Z]{3,}\b", it.get("title", ""))][:4],
                    "event_date": it.get("published", "")[:10], "ai_relevant": True, "fun": cat == "FUN",
                    "category_guess": cat})
    return {"digests": out}


def p_dedupe_pairs(payload):
    def caps(t):
        return set(re.findall(r"\b[A-Z][a-zA-Z]{2,}\b", t or ""))
    return {"pairs": [{"a": p["a"], "b": p["b"],
                       "same_event": p.get("similarity", 0) >= 0.5 and bool(caps(p.get("a_headline", "")) & caps(p.get("b_headline", ""))),
                       "reason": "DRY: similarity plus a shared name"} for p in payload["pairs"]]}


def p_classify(payload):
    out = []
    for ev in payload["events"]:
        key = ev.get("category_guess") or KEYS[_h(ev["id"], len(KEYS))]
        h = _h(ev["id"] + "s", 24)
        score = 10 if h == 0 else 9 if h < 4 else 8 if h < 8 else 7 if h < 14 else 6 if h < 19 else 5  # 10 is rare, as in life
        if ev.get("fun"):
            key, score = "FUN", min(score, 7)
        out.append({"id": ev["id"], "category": key, "subcategory": "DRY topic", "importance": score,
                    "label": "CRITICAL" if score >= 10 else "HIGH" if score >= 8 else "MEDIUM" if score >= 6 else "WATCHLIST",
                    "verification": "REPORTED", "why_it_matters": "DRY reason it matters.",
                    "big_name": _h(ev["id"] + "b", 5) == 0})
    return {"classified": out}


def p_report_story(payload):
    return {"stories": [{"id": ev["id"], "headline": ev["headline"], "importance_reason": "DRY reason and affected parties.",
                         "summary": _sentences(ev.get("summary", ""), 2) or "DRY summary."} for ev in payload["events"]]}


def p_analysis(payload):
    return {"analysis_markdown": "## Forward-looking analysis\n\nDRY analysis placeholder: assumptions, probabilities and "
                                 "scenarios would appear here, derived only from the listed items.\n"}


def p_bulletin_copy(payload):
    return {"items": [{"id": it["id"], "headline": it["headline"].rstrip(".") + ".",
                       "body": "DRY sentence one about what happened. DRY sentence two about why it matters."}
                      for it in payload["items"]]}


def p_meaning_check(payload):
    return {"results": [{"id": it["id"], "result": "PASS", "missing": [], "unsupported": [], "note": "DRY"}
                        for it in payload["items"]]}


def p_bigger_picture(payload):
    return {"head": "DRY: the bigger picture headline.", "card_body": "DRY card body sentence one. DRY sentence two.",
            "items": ["DRY item one (report items 1, 2)", "DRY item two (report items 3)"],
            "spoken": "And for the bigger picture, DRY spoken analysis line that runs roughly forty eight syllables in total for the reel.",
            "full_markdown": "# The Bigger Picture — Daily AI Analysis\n\nDRY analysis body.\n", "report_refs": [1, 2, 3]}


def p_cards_copy(payload):
    out = []
    for it in payload["items"]:
        out.append({"id": it["id"], "head": it["headline"].rstrip(".") + ".",
                    "body": "DRY sentence one says what happened. DRY sentence two says why it matters.",
                    "cat": f"{it.get('category_name', 'Models and tools')} / DRY", "src": (it.get("source") or "SOURCE").upper(),
                    "pill": it.get("verification", "REPORTED")})
    teaser = [{"id": t["id"], "head": t["headline"].rstrip(".") + ".", "cat": t.get("category_name", "")} for t in payload.get("teaser", [])]
    return {"cards": out, "teaser": teaser}


def p_headlines_copy(payload):
    out = []
    for it in payload["items"]:
        intro = {"story": "In the news.", "fun": "And a lighter story.", "teaser": "Also in the full report:",
                 "bigger_picture": "And for the bigger picture:"}.get(it["kind"], "")
        head = it.get("headline") or " and ".join(t["headline"].rstrip(".") for t in it.get("teaser_items", [])[:2]) or "DRY item"
        base = f"{intro} {head.rstrip('.')}. DRY second clause of the spoken line."
        if it.get("fix"):
            base = f"{intro} {head.rstrip('.')[:60]}. DRY rewrite to fit the box."
        if it["kind"] == "bigger_picture":
            base = f"{intro} DRY spoken analysis, money keeps flowing while power delays and debt test the build-out, and the question of who is responsible grows."
        out.append({"id": it["id"], "script": base, "symbol": "a simple glowing icon, simple text-free symbol"})
    return {"items": out}


def p_editorial_qa(payload):
    return {"status": "APPROVED", "checks": [{"name": "facts", "result": "PASS", "note": "DRY"}], "corrections": []}
```

## v1_workflow/lib/syllables.py

```python
"""Syllable counting for Headlines box timing (Headlines_Master_Rules_Structure.txt, Section B item 1a).

seconds = syllables / 4.4, written to two decimals, no rounding up, no hold allowance.
The override table merges syl.py (Headlines scripts folder, 25 Sep 2026) and the 26 Sep fill script.
Add a word to OVR when a pronunciation check shows the heuristic is wrong; never guess boxes from words per second.
"""
import re

OVR = {
    "ai": 2, "a.i.": 2, "ai's": 2, "xi": 1, "jinping": 2, "akamai": 3, "anthropic": 3, "salesforce's": 3,
    "salesforce": 2, "oracle": 3, "waymo's": 2, "waymo": 2, "alphafold": 3, "deepmind's": 2, "netflix's": 3,
    "wonka": 2, "gene": 1, "wilder's": 2, "ghoulish": 2, "deepseek's": 2, "deepseek": 2, "mexico": 3,
    "pipeline": 2, "twenty-seven": 3, "seventy": 3, "eighty-two": 3, "hijack": 2, "customer": 3, "database": 3,
    "prepare": 2, "pandemic": 3, "attorneys": 3, "general": 3, "overriding": 4, "states'": 1, "reviewer": 3,
    "ghoulishly": 3, "structures": 2, "flaws": 1, "fixed": 1, "leader": 2, "control": 2, "specific": 3,
    "offered": 2, "president": 3, "nations": 2, "billion": 2, "dollar": 2, "computing": 3, "company": 3,
    "shares": 1, "jumped": 1, "percent": 2, "researchers": 3, "showed": 1, "hidden": 2, "agents": 2, "steal": 1,
    "warned": 1, "delay": 2, "payments": 2, "center": 2, "because": 2, "slipped": 1, "driverless": 3, "driven": 2,
    "hundred": 2, "million": 2, "miles": 1, "injury": 3, "crashes": 2, "drivers": 2, "protein": 2, "virus": 2,
    "thousand": 2, "predicted": 3, "pairs": 1, "scientists": 3, "twenty-six": 3, "asked": 1, "congress": 2,
    "regulate": 3, "without": 2, "own": 1, "laws": 1, "critics": 2, "panned": 1, "uses": 2, "copy": 2, "voice": 1,
    "called": 1, "also": 2, "full": 1, "report": 2, "revenue": 3, "tops": 1, "factory": 3, "robots": 2, "record": 2,
    "five": 1, "bigger": 2, "picture": 2, "money": 2, "keeps": 1, "flowing": 2, "power": 2, "delays": 2,
    "costlier": 3, "debt": 1, "testing": 2, "eleven": 3, "point": 1, "six": 1, "seven-year": 3, "deal": 1, "rent": 1,
    "cloud": 1, "whose": 1, "about": 2, "twenty": 2, "white": 1, "house": 1, "models": 2, "british": 2, "testers": 2,
    "holds": 1, "new": 1, "hit": 1, "us": 2, "openai": 4, "ftc": 3, "qwen": 1, "skydio": 3, "skydios": 3, "nethack": 2,
    "microsoft": 3, "copilot": 3, "autopilot": 4, "gigawatts": 3, "capacity": 4, "operating": 4, "companies": 3,
    "politics": 3, "appeals": 2, "pentagons": 3, "defense": 2, "systems": 2, "reportedly": 4, "earlier": 3,
    "dozens": 2, "outside": 2, "computer": 3, "months": 1, "analysts": 3, "expansion": 3, "centres": 2, "launches": 2,
    "patrol": 2, "catches": 2, "returns": 2, "rebuilt": 2, "around": 2, "working": 2, "youre": 1, "science": 2,
    "particle": 3, "physics": 2, "calculation": 4, "human": 2, "reaching": 2, "physicists": 3, "federal": 3,
    "commission": 3, "independent": 4, "actors": 2, "cannot": 2, "lighter": 2, "gamings": 2, "games": 1,
    "hardest": 2, "attempt": 2, "alibabas": 4, "ninety": 2, "states": 1, "prices": 2, "risen": 2, "blacklist": 2,
    "broke": 1, "groups": 1, "those": 1, "research": 2, "nvidia": 3, "google": 2, "meta": 2, "apple": 2,
    "amazon": 3, "tesla": 2, "huawei": 3, "alibaba": 4, "tiktok": 2, "chatgpt": 4, "gemini": 3, "claude": 1,
    "headlines": 2, "ninety": 2, "seconds": 2, "coverage": 3, "tomorrow": 3, "tuning": 2,
}


def word_syllables(token: str) -> int:
    x = token.lower().strip(".,:;!?\"'()[]")
    if not x:
        return 0
    if x in OVR:
        return OVR[x]
    if x.endswith("s") and x[:-1] in OVR:  # possessive or plural of a listed word: Salesforce's -> 3, Waymo's -> 2
        return OVR[x[:-1]] + (1 if x[:-1].endswith(("s", "x", "z", "ch", "sh", "ce", "ge")) else 0)
    if "-" in x:
        return sum(word_syllables(p) for p in x.split("-"))
    if x.isupper() and len(x) <= 4 and token.isupper():
        return len(x)
    if len(x) > 3 and x.endswith("s") and not x.endswith(("ss", "us", "is", "ies", "oes")):
        stem = x[:-1]
        if not (x.endswith("es") and stem[:-1].endswith(("s", "x", "z", "ch", "sh", "g", "c"))):
            x = stem  # plural or third person: rules -> rule, makes -> make; changes and places keep the spoken -es
    v = re.findall(r"[aeiouy]+", x)
    n = len(v)
    syllabic_le = x.endswith("le") and len(x) > 2 and x[-3] not in "aeiou"  # table, little: yes; rule, mile: no
    if x.endswith("e") and n > 1 and not (x.endswith(("ee", "ye")) or syllabic_le):
        n -= 1
    if x.endswith("ed") and not x.endswith(("ted", "ded")) and n > 1:
        n -= 1
    return max(1, n)


def count(text: str, cues: dict | None = None) -> int:
    """Count syllables of a complete spoken line. cues maps a written token to its spoken form."""
    t = text
    for cue, real in (cues or {}).items():
        t = t.replace(cue, real)
    t = t.replace("'", "").replace("’", "")
    total = 0
    for token in re.findall(r"[A-Za-z][A-Za-z'\-]*|\d+", t):
        if token.isdigit():
            total += number_syllables(int(token))
        else:
            total += word_syllables(token)
    return total


def number_syllables(n: int) -> int:
    """Rough spoken length of a digit string; scripts should spell numbers as words (Section B item 3)."""
    if n < 20:
        return 1 if n in (0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12) else 2
    if n < 100:
        return 2 if n % 10 == 0 else 3
    return 3 + number_syllables(n % 100)


def box_seconds(syllables: int, rate: float = 4.4) -> float:
    """Clip duration = syllables / 4.4, two decimals, no rounding up (35 syllables = 7.95 s)."""
    return round(syllables / rate, 2)


def audit(text: str, cues: dict | None = None) -> list[tuple[str, int]]:
    """Word by word audit, for the pack's syllable_audit field."""
    t = text
    for cue, real in (cues or {}).items():
        t = t.replace(cue, real)
    t = t.replace("'", "").replace("’", "")
    return [(tok, number_syllables(int(tok)) if tok.isdigit() else word_syllables(tok))
            for tok in re.findall(r"[A-Za-z][A-Za-z'\-]*|\d+", t)]
```

## v1_workflow/llm/prompts/analysis.md

```markdown
# analysis (strong tier)

Task: write the FORWARD-LOOKING ANALYSIS section of the Daily Global AI Intelligence Report from the numbered items in PAYLOAD.items (headline, label, category only). PAYLOAD.previous_analyses holds excerpts of recent editions so you do not repeat yesterday's framing.

Rules
- Desk judgement, clearly separated from reported facts. Cite item numbers in brackets like [12] after each claim that rests on an item.
- Structure in markdown: three to five short themed sections with a bold heading each, then a section "Probabilities" with three to six one-line scenarios, each with a rough probability in words (likely, possible, unlikely) and the items that support it, then a section "What to watch" with three to five bullets.
- No investment recommendation, no price target, no buy or sell language. Not financial advice.
- Plain language, short sentences, at most 450 words in total.
- Do not introduce facts that are not in the items.

Output JSON exactly:
{"analysis_markdown": "..."}
```

## v1_workflow/llm/prompts/bigger_picture.md

```markdown
# bigger_picture (strong tier)

Task: write The Bigger Picture, the daily analysis corner, from PAYLOAD.items (the Daily Bulletin) only. Names, description and opening words are in PAYLOAD. Follow PAYLOAD.rules.

Produce
- head: the analysis headline for the card, one sentence, at most 90 characters.
- card_body: two sentences for the card: the pattern you see today, then what it could mean for technology, business or everyday life.
- items: two to four one-line desk observations, each ending with the report item numbers it rests on in brackets, like "(report items 3, 12)".
- spoken: the reel narration for the Bigger Picture clip. It MUST start with the exact opening words in PAYLOAD.opening (without the ellipsis, followed by a comma), be one or two sentences, and run between PAYLOAD.spoken_syllables[0] and PAYLOAD.spoken_syllables[1] syllables. Numbers as words. Plain language.
- full_markdown: the full analysis document body in markdown: three to five short paragraphs with bold lead-ins, then a "Why it matters" list, citing report item numbers in brackets. At most 400 words.
- report_refs: the list of report item numbers used.

Desk judgement, clearly separated from reported facts. No investment advice, no price targets.

Output JSON exactly:
{"head": "...", "card_body": "...", "items": ["..."], "spoken": "...", "full_markdown": "...", "report_refs": [1, 2]}
```

## v1_workflow/llm/prompts/bulletin_copy.md

```markdown
# bulletin_copy (mid tier)

Task: rewrite every item in PAYLOAD.items as a Daily Bulletin entry under PAYLOAD.law (the AIND plain language law).

For each item
- headline: one complete spoken sentence a newsreader could say, ending with a period. Name the actor. Unfamiliar companies get a short title ("robot brain startup Skild"). Non-market stories lead with the deed, not the money.
- body: exactly two sentences. Sentence one: what happened, with the key number or name. Sentence two: why it matters, or the honest doubt.
- Only facts in headline, summary and key_facts. Never add a fact. Keep verification wording ("reportedly", "says") when the item is REPORTED or PRELIMINARY.
- No jargon, no hype words, no acronyms without the plain meaning.

Output JSON exactly:
{"items": [{"id": "...", "headline": "...", "body": "..."}]}
```

## v1_workflow/llm/prompts/cards_copy.md

```markdown
# cards_copy (mid tier)

Task: write the card copy for every story in PAYLOAD.items and the teaser lines in PAYLOAD.teaser, under PAYLOAD.law and PAYLOAD.rules (Cards Master Section 3).

For each story card
- head: one complete sentence, at most 110 characters, ending with a period. Names the actor and the deed. Non-market cards never open with money; funding, revenue and valuation stay out of the head and the first body sentence.
- body: exactly two sentences, at most 260 characters together: what happened with the key number or name, then why it matters or the honest doubt.
- cat: the category line "Category / two-word topic", for example "Robotics / Warehouse robots".
- src: the source name in capitals, as given in the item, for example "REUTERS".
- pill: copy the item's verification status exactly (CONFIRMED, REPORTED, PRELIMINARY or DISPUTED).

For each teaser line
- head: one line, at most 90 characters, a complete sentence ending with a period.
- cat: the category name.

Only facts from headline, summary and key_facts. Unfamiliar companies get a short title. Plain words, no jargon.

Output JSON exactly:
{"cards": [{"id": "...", "head": "...", "body": "...", "cat": "...", "src": "...", "pill": "REPORTED"}],
 "teaser": [{"id": "...", "head": "...", "cat": "..."}]}
```

## v1_workflow/llm/prompts/classify.md

```markdown
# classify (cheap tier)

Task: for every event in PAYLOAD.events assign a category, an importance score, a verification status and one line on why it matters. Use PAYLOAD.categories and PAYLOAD.scoring_rules.

Rules
- category: one key from PAYLOAD.categories. Robotics means a robot or autonomous machine doing something. Policy about robots is POL; money about robots is MKT.
- subcategory: two to four words.
- importance: integer 1 to 10. 10 only when the event changes what AI can do, affects many people, or is a major government or court decision. A big dollar figure alone is never a 10. 8 to 9 for major company, model or policy news. 6 to 7 for solid news of interest to one audience. 1 to 5 for minor or incremental items.
- label: CRITICAL for 10, HIGH for 8 to 9, MEDIUM for 6 to 7, WATCHLIST for 1 to 5.
- verification: CONFIRMED when a primary or official source is among the sources; REPORTED for credible attributed reporting; PRELIMINARY for early or single-source claims; DISPUTED when sources conflict.
- why_it_matters: one plain sentence, at most 25 words, no jargon.
- big_name: true when the actor is a major AI company, a national government or a global institution.

Output JSON exactly:
{"classified": [{"id": "...", "category": "MOD", "subcategory": "...", "importance": 7, "label": "MEDIUM", "verification": "REPORTED", "why_it_matters": "...", "big_name": false}]}
```

## v1_workflow/llm/prompts/dedupe_pairs.md

```markdown
# dedupe_pairs (cheap tier)

Task: for each pair of digests decide whether both describe the SAME news event (same actor, same action, same day), not merely the same topic or company.

Same event examples: two outlets reporting one product launch; a press release and an article about it.
Different event examples: two different lawsuits against the same company; a funding round and a product launch by the same startup; a follow-up development a day later that adds a new decision.

For every pair in PAYLOAD.pairs return a and b unchanged, same_event true or false, and a reason of at most 12 words.

Output JSON exactly:
{"pairs": [{"a": "...", "b": "...", "same_event": true, "reason": "..."}]}
```

## v1_workflow/llm/prompts/digest.md

```markdown
# digest (cheap tier)

Task: turn each collected article into a tiny factual record. This is the only time the raw text is read, so capture every concrete fact now.

For every item in PAYLOAD.items return one digest with the same id.

Rules
- headline: one factual line, at most 140 characters, present tense, no clickbait, no source name.
- summary: one or two complete sentences, at most 400 characters, only facts present in the text or title.
- key_facts: two to five short strings. Each carries a concrete fact: a number, a name, a date, a place, a decision. Copy numbers exactly as written.
- entities: up to four organisation or product names that appear in the text.
- event_date: the date the event happened if the text states it, as YYYY-MM-DD, otherwise "".
- ai_relevant: false when the article is not about artificial intelligence, machine learning, robotics driven by AI, AI chips, AI policy or AI companies.
- fun: true only for light, quirky or humorous stories.
- category_guess: one key from POL, MKT, SEC, ENE, ROB, MOD, RES, LAW, HEA, SOC, FUN. Use category_hint only when the text agrees with it.
- If text is empty, digest from the title alone and keep key_facts to what the title states.
- Never add facts, never guess numbers, never merge two items.

Output JSON exactly:
{"digests": [{"id": "...", "headline": "...", "summary": "...", "key_facts": ["..."], "entities": ["..."], "event_date": "", "ai_relevant": true, "fun": false, "category_guess": "MOD"}]}
```

## v1_workflow/llm/prompts/editorial_qa.md

```markdown
# editorial_qa (strong tier)

Task: the final editorial check of a product (cards copy or Headlines scripts) in PAYLOAD.product against its source items in PAYLOAD.sources and the rules in PAYLOAD.rules.

Check, one result per check
- facts: every claim is supported by the sources; numbers, actors and dates match.
- certainty: reported or preliminary items are not stated as certain.
- language: plain language law: no jargon, short sentences, numbers as words in spoken scripts.
- structure: the order and count follow the rules given.
- money: non-market items lead with the deed, not the money.

status: APPROVED when every check passes; CHANGES when any check fails. corrections: one entry per failing item with id, field, problem and a proposed corrected text (only from the sources).

Output JSON exactly:
{"status": "APPROVED", "checks": [{"name": "facts", "result": "PASS", "note": "..."}], "corrections": [{"id": "...", "field": "...", "problem": "...", "proposed": "..."}]}
```

## v1_workflow/llm/prompts/headlines_copy.md

```markdown
# headlines_copy (mid tier)

Task: write the spoken narration for the Headlines reel clips in PAYLOAD.items, plus a text-free screen symbol for each. Follow PAYLOAD.rules.

Every item has kind: story, fun, teaser or bigger_picture, a target syllable count and an allowed range.

Narration rules
- story and fun: start with a short natural spoken introduction suited to the subject ("In robotics.", "Now the money.", "And a lighter one."). Rotate wording; never reuse an introduction listed in PAYLOAD.previous_intros. Then one or two sentences with the deed first, the key fact, and the actor named. About 35 syllables including the introduction; stay inside the range.
- teaser: starts with "Also in the full report:" or "More in today's full report." then names two or three of the teaser_items as short clauses. Never a story that already has a clip.
- bigger_picture: starts with the exact words "And for the bigger picture," then one or two sentences of desk analysis from the given head, summary and key_facts. Between 44 and 53 syllables.
- Numbers as spoken words ("twelve billion dollars", "twenty twenty-seven"), never digits. Say percent, not the sign.
- Plain language, no jargon, unfamiliar companies get a short title, no hype.
- Only facts in the item. Never add a fact.
- When an item carries "fix", rewrite the current_script to solve the stated problem and keep everything else.

Symbol rules (the hologram pane shows it instead of the logo)
- A simple glowing icon that fits the story, ending with "simple text-free symbol". No people, no faces, no letters, no numbers, no flags, no logos, no dates.

Output JSON exactly:
{"items": [{"id": "C02", "script": "...", "symbol": "..."}]}
```

## v1_workflow/llm/prompts/meaning_check.md

```markdown
# meaning_check (mid tier)

Task: the 26 September source-to-script meaning check. For every item in PAYLOAD.items compare the written copy (PAYLOAD.items[].written, any fields) against the source facts (PAYLOAD.items[].source_facts).

Decide
- PASS: every claim in the written copy is supported by the source facts and nothing important was dropped or reversed.
- FAIL: the copy states something the facts do not support, reverses a meaning, drops the central fact, or turns a report into a certainty.
- UNVERIFIED: the facts are too thin to judge.

Report
- missing: important source facts the copy dropped (short strings, may be empty).
- unsupported: claims in the copy that the facts do not support (short strings, may be empty).
- note: at most 20 words.

Be strict about numbers, actors, dates and causality. Wording differences are fine.

Output JSON exactly:
{"results": [{"id": "...", "result": "PASS", "missing": [], "unsupported": [], "note": "..."}]}
```

## v1_workflow/llm/prompts/report_story.md

```markdown
# report_story (mid tier)

Task: write the Full Report story block for every event in PAYLOAD.events, in the Daily Global AI Intelligence Report format.

For each event
- headline: one line, factual, specific, present tense, at most 120 characters. Name the actor. No source name, no question marks.
- importance_reason: at most 25 words: who is affected and why this matters now. Fits after "Importance: LABEL —".
- summary: one or two complete sentences that give the new facts with their numbers, names and context. Do not repeat the headline. Do not speculate. Only facts in key_facts and summary.

Plain language: short words, no jargon, no hype. Numbers as written in the facts.

Output JSON exactly:
{"stories": [{"id": "...", "headline": "...", "importance_reason": "...", "summary": "..."}]}
```

## v1_workflow/stages/s01_collect.py

```python
"""s01_collect: fetch every registered V1 source for the reporting window. Zero LLM. PC only (needs the open web).

Implements the 18 Sep 2026 SOURCE FETCH GATE: every Source ID ends with one evidence-backed terminal status,
  CHECKED — CANDIDATE(S) FOUND [n] | CHECKED — NO QUALIFYING ITEM | FAILED/UNAVAILABLE [reason] | INCOMPLETE COVERAGE [reason]
Nothing is invented. Items outside the window are kept with OUT OF WINDOW so the pool shows they were seen.
Outputs: work/raw_pool.jsonl, work/source_ledger.json, a section in V1_script_report.md.

Run alone:  python stages/s01_collect.py --edition 2026-09-27 [--fixture path.jsonl] [--extra work/extra_items.jsonl]
"""
from __future__ import annotations

import datetime as dt
import email.utils
import html
import re
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urljoin, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.common import (log, norm_text, norm_url, read_jsonl, save_json, stage_main, write_jsonl)  # noqa: E402

FEED_GUESSES = ["/feed/", "/feed", "/rss", "/rss.xml", "/feed.xml", "/atom.xml", "/index.xml", "/feeds/all"]
TAG_RE = re.compile(r"<[^>]+>")
SCRIPT_RE = re.compile(r"<(script|style|noscript|svg|nav|footer|header)[^>]*>.*?</\1>", re.S | re.I)
P_RE = re.compile(r"<p[^>]*>(.*?)</p>", re.S | re.I)
A_RE = re.compile(r"<a[^>]+href=[\"']([^\"']+)[\"'][^>]*>(.*?)</a>", re.S | re.I)
ALT_RE = re.compile(r"<link[^>]+type=[\"']application/(?:rss|atom)\+xml[\"'][^>]*href=[\"']([^\"']+)[\"']", re.I)
ALT_RE2 = re.compile(r"<link[^>]+href=[\"']([^\"']+)[\"'][^>]*type=[\"']application/(?:rss|atom)\+xml[\"']", re.I)


class Fetcher:
    def __init__(self, cfg: dict):
        self.timeout = cfg.get("timeout_seconds", 20)
        self.retries = cfg.get("retries", 2)
        self.delay = cfg.get("per_domain_delay_seconds", 1.5)
        self.ua = cfg.get("user_agent", "AINewsDesk-V1-collector/1.0")
        self.last: dict[str, float] = {}

    def get(self, url: str) -> tuple[bytes | None, str]:
        host = urlsplit(url).netloc
        wait = self.delay - (time.time() - self.last.get(host, 0))
        if wait > 0:
            time.sleep(wait)
        err = ""
        for attempt in range(self.retries + 1):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": self.ua, "Accept": "*/*"})
                with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                    data = resp.read()
                self.last[host] = time.time()
                return data, ""
            except urllib.error.HTTPError as exc:
                err = f"HTTP {exc.code}"
                if exc.code in (401, 403, 404, 410, 451):
                    break
            except Exception as exc:  # noqa: BLE001
                err = f"{type(exc).__name__}: {str(exc)[:120]}"
            time.sleep(1 + attempt)
        self.last[host] = time.time()
        return None, err


def parse_date(text: str | None) -> dt.datetime | None:
    if not text:
        return None
    text = text.strip()
    try:
        d = email.utils.parsedate_to_datetime(text)
        if d.tzinfo is None:
            d = d.replace(tzinfo=dt.timezone.utc)
        return d
    except (TypeError, ValueError):
        pass
    try:
        d = dt.datetime.fromisoformat(text.replace("Z", "+00:00"))
        if d.tzinfo is None:
            d = d.replace(tzinfo=dt.timezone.utc)
        return d
    except ValueError:
        return None


def strip_html(s: str) -> str:
    return norm_text(html.unescape(TAG_RE.sub(" ", s or "")))


def parse_feed(data: bytes) -> list[dict]:
    """RSS 2.0 or Atom, namespace tolerant. Returns title, link, published, summary."""
    try:
        root = ET.fromstring(data)
    except ET.ParseError:
        return []
    items = []

    def local(tag):
        return tag.split("}")[-1].lower()

    for el in root.iter():
        if local(el.tag) not in ("item", "entry"):
            continue
        rec = {"title": "", "link": "", "published": None, "summary": ""}
        for ch in el:
            t = local(ch.tag)
            txt = (ch.text or "").strip()
            if t == "title":
                rec["title"] = strip_html(txt)
            elif t == "link":
                href = ch.attrib.get("href") or txt
                if href and (not rec["link"] or ch.attrib.get("rel", "alternate") == "alternate"):
                    rec["link"] = href.strip()
            elif t in ("pubdate", "published", "updated", "date") and not rec["published"]:
                rec["published"] = txt
            elif t in ("description", "summary", "content", "encoded") and not rec["summary"]:
                rec["summary"] = strip_html(txt)[:600]
        if rec["title"] and rec["link"]:
            items.append(rec)
    return items


def discover_feed(fetcher: Fetcher, page_url: str) -> tuple[str | None, bytes | None]:
    data, err = fetcher.get(page_url)
    if data:
        text = data.decode("utf-8", "ignore")
        for rx in (ALT_RE, ALT_RE2):
            m = rx.search(text)
            if m:
                feed = urljoin(page_url, html.unescape(m.group(1)))
                fdata, _ = fetcher.get(feed)
                if fdata and parse_feed(fdata):
                    return feed, fdata
    base = page_url.rstrip("/")
    for guess in FEED_GUESSES:
        fdata, _ = fetcher.get(base + guess)
        if fdata and parse_feed(fdata):
            return base + guess, fdata
    return None, data


def html_links(page_url: str, data: bytes) -> list[dict]:
    """Fallback when no feed exists: article-looking links on the section page, date unknown."""
    text = SCRIPT_RE.sub(" ", data.decode("utf-8", "ignore"))
    host = urlsplit(page_url).netloc.replace("www.", "")
    seen, out = set(), []
    for href, inner in A_RE.findall(text):
        title = strip_html(inner)
        url = urljoin(page_url, html.unescape(href))
        if len(title) < 28 or urlsplit(url).netloc.replace("www.", "") != host:
            continue
        if url in seen or len(urlsplit(url).path.strip("/").split("/")) < 2:
            continue
        seen.add(url)
        out.append({"title": title, "link": url, "published": None, "summary": ""})
    return out


def article_text(fetcher: Fetcher, url: str, limit: int) -> tuple[str, str]:
    data, err = fetcher.get(url)
    if not data:
        return "", err or "no data"
    text = SCRIPT_RE.sub(" ", data.decode("utf-8", "ignore"))
    paras = [strip_html(p) for p in P_RE.findall(text)]
    paras = [p for p in paras if len(p) > 60]
    body = " ".join(paras)
    return body[:limit], "" if body else "no paragraphs"


def run(ctx, extra_args=None) -> int:
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--fixture", help="jsonl of pre-collected items instead of the network (tests)")
    p.add_argument("--extra", help="jsonl of manually supplied items (web search hits, Rafael additions)")
    p.add_argument("--no-articles", action="store_true", help="skip article body fetch (feeds only)")
    args = p.parse_args(extra_args or [])
    ccfg = ctx.config.get("collector", {})
    fetcher = Fetcher(ccfg)
    sources = ctx.sources["sources"]
    start, end = ctx.window_start, ctx.window_end
    ledger, pool = [], []
    nid = 0

    def add(rec, src):
        nonlocal nid
        nid += 1
        pub = parse_date(rec.get("published"))
        if pub is None:
            window = "UNVERIFIED DATE"
        elif start <= pub < end:
            window = "IN WINDOW"
        else:
            window = "OUT OF WINDOW"
        pool.append({"id": f"RAW-{ctx.edition.strftime('%Y%m%d')}-{nid:04d}", "source_id": src["id"],
                     "source_name": src["name"], "category_hint": src.get("category"), "title": rec["title"],
                     "url": rec["link"], "url_norm": norm_url(rec["link"]),
                     "published": pub.isoformat() if pub else None, "window_check": window,
                     "summary": rec.get("summary", ""), "text": rec.get("text", ""), "fetch_status": rec.get("fetch_status", "")})
        return window

    fixture = {}
    if args.fixture:
        for row in read_jsonl(args.fixture):
            fixture.setdefault(row.get("source_id", "*"), []).append(row)

    for src in sources:
        t0 = time.time()
        entry = {"id": src["id"], "name": src["name"], "category": src.get("category"), "route": None, "status": "",
                 "in_window": 0, "out_of_window": 0, "unverified": 0, "error": ""}
        items, route, err = [], None, ""
        if fixture:
            items = fixture.get(src["id"], []) + ([] if src["id"] in fixture else fixture.get("*", []))
            route = "fixture"
        else:
            feed = src.get("feed_url")
            if feed:
                fdata, err = fetcher.get(feed)
                if fdata:
                    items = parse_feed(fdata)
                    route = feed if items else None
            if not items:
                feed2, page = discover_feed(fetcher, src["url"])
                if feed2:
                    fdata, _ = fetcher.get(feed2)
                    items, route = parse_feed(fdata or b""), feed2
                elif page:
                    items, route = html_links(src["url"], page), src["url"] + " (html links, no dates)"
                else:
                    err = err or "page unreachable"
        items = items[: ccfg.get("max_items_per_source", 80)]
        for rec in items:
            w = add(rec, src)
            entry["in_window" if w == "IN WINDOW" else "out_of_window" if w == "OUT OF WINDOW" else "unverified"] += 1
        entry["route"] = route
        if not items and err:
            entry["status"] = f"FAILED/UNAVAILABLE [{err}]"
        elif not items:
            entry["status"] = "INCOMPLETE COVERAGE [route returned no items]"
        elif route and "html links" in route:
            entry["status"] = f"INCOMPLETE COVERAGE [no feed; {len(items)} undated links from section page]"
        elif entry["in_window"]:
            entry["status"] = f"CHECKED — CANDIDATE(S) FOUND [{entry['in_window']}]"
        else:
            entry["status"] = "CHECKED — NO QUALIFYING ITEM"
        entry["seconds"] = round(time.time() - t0, 1)
        ledger.append(entry)
        log.info("%s %-28s %s", src["id"], src["name"][:28], entry["status"])

    if args.extra:
        for row in read_jsonl(args.extra):
            add({"title": row.get("title", ""), "link": row.get("url") or row.get("link", ""),
                 "published": row.get("published"), "summary": row.get("summary", ""), "text": row.get("text", "")},
                {"id": row.get("source_id", "SRC-EXTRA"), "name": row.get("source_name", "manual"), "category": row.get("category_hint")})

    if not args.no_articles and not fixture:
        limit = ccfg.get("article_text_chars", 2500)
        for rec in pool:
            if rec["window_check"] == "OUT OF WINDOW" or rec.get("text"):
                continue
            body, ferr = article_text(fetcher, rec["url"], limit)
            rec["text"], rec["fetch_status"] = body or rec.get("summary", ""), ferr or "ok"

    write_jsonl(ctx.work / "raw_pool.jsonl", pool)
    checked = sum(1 for e in ledger if e["status"].startswith("CHECKED"))
    failed = sum(1 for e in ledger if e["status"].startswith("FAILED"))
    incomplete = sum(1 for e in ledger if e["status"].startswith("INCOMPLETE"))
    summary = {"edition": ctx.edition.isoformat(), "window": [start.isoformat(), end.isoformat()],
               "registry_source_count": len(sources), "sources_fetched_terminal_count": len(ledger),
               "sources_checked_success_count": checked, "sources_failed_count": failed,
               "sources_incomplete_count": incomplete, "sources_pending_count": len(sources) - len(ledger),
               "raw_records": len(pool), "in_window": sum(1 for r in pool if r["window_check"] == "IN WINDOW"),
               "sources": ledger}
    save_json(ctx.work / "source_ledger.json", summary)
    ctx.report_append("s01 collect", f"registry {len(sources)}, checked {checked}, failed {failed}, incomplete {incomplete}; "
                                     f"raw records {len(pool)} ({summary['in_window']} in window).")
    ctx.set_stage("s01_collect", "done", raw_records=len(pool), checked=checked, failed=failed, incomplete=incomplete)
    return 0


if __name__ == "__main__":
    stage_main(run, __doc__)
```

## v1_workflow/stages/s02_digest.py

```python
"""s02_digest: read every raw article ONCE and reduce it to a tiny record (cheap model, batched).

This is the only stage that ever sees raw article text. Everything downstream works on digests.
Input:  work/raw_pool.jsonl        Output: work/digests.jsonl (raw fields minus text, plus digest fields)
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.common import log, read_jsonl, stage_main, write_jsonl  # noqa: E402
from lib.llm_client import LLMClient, batched  # noqa: E402


def run(ctx, extra_args=None) -> int:
    raw = read_jsonl(ctx.work / "raw_pool.jsonl")
    if not raw:
        log.error("no raw_pool.jsonl; run s01 first")
        return 1
    todo = [r for r in raw if r["window_check"] != "OUT OF WINDOW"]
    llm = LLMClient(ctx)
    size = ctx.config["llm"]["batch_sizes"].get("digest", 40)
    by_id = {}
    for batch in batched(todo, size):
        payload = {"edition": ctx.edition.isoformat(), "window": [ctx.window_start.isoformat(), ctx.window_end.isoformat()],
                   "items": [{"id": r["id"], "title": r["title"], "source": r["source_name"], "published": r.get("published"),
                              "url": r["url"], "category_hint": r.get("category_hint"),
                              "text": (r.get("text") or r.get("summary") or "")[: ctx.config["collector"].get("article_text_chars", 2500)]}
                             for r in batch]}
        reply = llm.call("cheap", "digest", payload, stage="s02_digest")
        for d in reply.get("digests", []):
            by_id[d["id"]] = d
    out = []
    missing = 0
    for r in raw:
        rec = {k: v for k, v in r.items() if k != "text"}
        d = by_id.get(r["id"])
        if r["window_check"] == "OUT OF WINDOW":
            rec["disposition"] = "OUT OF WINDOW"
        elif d is None:
            missing += 1
            rec["disposition"] = "HELD FOR REVIEW"
            rec["digest_note"] = "no digest returned"
        else:
            rec.update({"headline": d.get("headline") or r["title"], "summary": d.get("summary", ""),
                        "key_facts": d.get("key_facts", []), "entities": d.get("entities", []),
                        "event_date": d.get("event_date"), "fun": bool(d.get("fun")),
                        "category_guess": d.get("category_guess") or r.get("category_hint")})
            rec["disposition"] = "PENDING" if d.get("ai_relevant", True) else "NOT AI-RELEVANT"
        out.append(rec)
    write_jsonl(ctx.work / "digests.jsonl", out)
    pending = sum(1 for o in out if o["disposition"] == "PENDING")
    ctx.report_append("s02 digest", f"{len(todo)} items digested in batches of {size}; {pending} AI-relevant pending, "
                                    f"{missing} without digest (held). LLM so far: {llm.summary()}")
    ctx.set_stage("s02_digest", "done", digested=len(todo), pending=pending, missing=missing)
    return 0


if __name__ == "__main__":
    stage_main(run, __doc__)
```

## v1_workflow/stages/s03_dedupe.py

```python
"""s03_dedupe: cluster pool records into events and give EVERY record a disposition. Code first, model only for
ambiguous pairs (cheap, batched). Nothing disappears silently (18 Sep gate C).

Input:  work/digests.jsonl, history/events_history.jsonl (previous editions)
Output: work/events.jsonl (one per retained event), work/pool_dispositions.jsonl (every raw record)
Dispositions: RETAINED EVENT ID | DUPLICATE OF | PREVIOUSLY COVERED | OUT OF WINDOW | UNVERIFIED | LOW MATERIALITY |
              HELD FOR REVIEW | NOT AI-RELEVANT
"""
from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.common import jaccard, log, read_jsonl, stage_main, tokens, write_jsonl  # noqa: E402
from lib.llm_client import LLMClient, batched  # noqa: E402

SAME = 0.55      # at or above: same event, no model needed
MAYBE = 0.30     # between MAYBE and SAME: ask the cheap model
HISTORY = 0.50   # match against previous editions


class UnionFind:
    def __init__(self, ids):
        self.p = {i: i for i in ids}

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[max(ra, rb)] = min(ra, rb)


def run(ctx, extra_args=None) -> int:
    recs = read_jsonl(ctx.work / "digests.jsonl")
    if not recs:
        log.error("no digests.jsonl; run s02 first")
        return 1
    active = [r for r in recs if r.get("disposition") == "PENDING"]
    sig = {r["id"]: tokens((r.get("headline") or r["title"]) + " " + (r.get("summary") or "")) for r in active}
    uf = UnionFind([r["id"] for r in active])
    by_url = {}
    maybe = []
    for r in active:
        by_url.setdefault(r["url_norm"], []).append(r["id"])
    for ids in by_url.values():
        for other in ids[1:]:
            uf.union(ids[0], other)
    ents = {r["id"]: {e.lower() for e in (r.get("entities") or []) if e} for r in active}
    for i, a in enumerate(active):
        for b in active[i + 1:]:
            s = jaccard(sig[a["id"]], sig[b["id"]])
            if s < MAYBE:
                continue
            # two different actors doing the same kind of deed read alike: auto-merge only when an entity is shared;
            # a pair with known, disjoint entities is a different event and never reaches the model (token rule).
            ea, eb = ents[a["id"]], ents[b["id"]]
            shared_actor = not ea or not eb or bool(ea & eb)
            if s >= SAME and shared_actor:
                uf.union(a["id"], b["id"])
            elif shared_actor or s >= SAME:
                maybe.append((a, b, round(s, 2)))
    # ambiguous pairs: cheap model, only when a pair is not already in one cluster
    llm = LLMClient(ctx)
    pairs = sorted((x for x in maybe if uf.find(x[0]["id"]) != uf.find(x[1]["id"])), key=lambda x: -x[2])
    cap = int(ctx.config["llm"].get("max_dedupe_pairs", 240))
    undecided = len(pairs) - cap if len(pairs) > cap else 0
    pairs = pairs[:cap]  # the least similar leftovers stay separate events, recorded below
    size = ctx.config["llm"]["batch_sizes"].get("dedupe_pairs", 60)
    decided = 0
    for batch in batched(pairs, size):
        payload = {"pairs": [{"a": a["id"], "b": b["id"], "similarity": s,
                              "a_headline": a.get("headline") or a["title"], "a_summary": a.get("summary", ""),
                              "b_headline": b.get("headline") or b["title"], "b_summary": b.get("summary", "")}
                             for a, b, s in batch]}
        reply = llm.call("cheap", "dedupe_pairs", payload, stage="s03_dedupe")
        for res in reply.get("pairs", []):
            if res.get("same_event"):
                uf.union(res["a"], res["b"])
                decided += 1
    # clusters -> events
    clusters: dict[str, list[dict]] = {}
    for r in active:
        clusters.setdefault(uf.find(r["id"]), []).append(r)
    history = load_history(ctx)
    hist_sig = [(h, tokens(h.get("headline", "") + " " + h.get("summary", ""))) for h in history]
    events, dispositions = [], {}
    n = 0
    for root, members in clusters.items():
        members.sort(key=lambda m: (m.get("published") or "9999", m["id"]))
        primary = members[0]
        n += 1
        eid = f"EVT-{ctx.edition.strftime('%Y%m%d')}-{n:04d}"
        facts, seen = [], set()
        for m in members:
            for f in m.get("key_facts", []):
                if f and f.lower() not in seen:
                    seen.add(f.lower())
                    facts.append(f)
        merged = tokens((primary.get("headline") or primary["title"]) + " " + (primary.get("summary") or ""))
        prior = max(((jaccard(merged, hs), h) for h, hs in hist_sig), key=lambda x: x[0], default=(0, None))
        ev = {"id": eid, "headline": primary.get("headline") or primary["title"], "summary": primary.get("summary", ""),
              "key_facts": facts[:6], "entities": primary.get("entities", []), "published": primary.get("published"),
              "event_date": primary.get("event_date"), "primary_source": primary["source_name"], "primary_url": primary["url"],
              "sources": sorted({m["source_name"] for m in members}), "member_ids": [m["id"] for m in members],
              "urls": [m["url"] for m in members], "category_guess": primary.get("category_guess"),
              "fun": any(m.get("fun") for m in members), "window_check": primary["window_check"],
              "prior_match": {"score": round(prior[0], 2), "edition": prior[1].get("edition"), "headline": prior[1].get("headline")}
              if prior[1] and prior[0] >= HISTORY else None}
        if ev["prior_match"]:
            ev["disposition"] = "PREVIOUSLY COVERED"
        elif primary["window_check"] == "UNVERIFIED DATE":
            ev["disposition"] = "UNVERIFIED"
        else:
            ev["disposition"] = "RETAINED EVENT ID"
        events.append(ev)
        for i, m in enumerate(members):
            dispositions[m["id"]] = ev["disposition"] if i == 0 else f"DUPLICATE OF {eid}"
            if i == 0:
                dispositions[m["id"]] = f"{ev['disposition']} {eid}" if ev["disposition"] == "RETAINED EVENT ID" else ev["disposition"]
    rows = []
    for r in recs:
        d = dispositions.get(r["id"], r.get("disposition", "HELD FOR REVIEW"))
        rows.append({"id": r["id"], "title": r["title"], "source": r["source_name"], "url": r["url"],
                     "published": r.get("published"), "window_check": r["window_check"], "disposition": d})
    write_jsonl(ctx.work / "events.jsonl", events)
    write_jsonl(ctx.work / "pool_dispositions.jsonl", rows)
    retained = sum(1 for e in events if e["disposition"] == "RETAINED EVENT ID")
    ctx.report_append("s03 dedupe", f"{len(active)} pending records -> {len(events)} events ({retained} retained, "
                                    f"{sum(1 for e in events if e['disposition']=='PREVIOUSLY COVERED')} previously covered, "
                                    f"{sum(1 for e in events if e['disposition']=='UNVERIFIED')} unverified date). "
                                    f"{len(pairs)} ambiguous pairs sent to the cheap model in {-(-len(pairs) // max(1, size))} calls, {decided} merged; "
                                    f"{undecided} less similar pairs kept separate without a call (cap {cap}).")
    ctx.set_stage("s03_dedupe", "done", events=len(events), retained=retained, llm_pairs=len(pairs), undecided_pairs=undecided)
    return 0


def load_history(ctx) -> list[dict]:
    path = ctx.history / "events_history.jsonl"
    days = ctx.config["gates"].get("dedupe_history_days", 30)
    cutoff = (ctx.edition - dt.timedelta(days=days)).isoformat()
    return [h for h in read_jsonl(path) if h.get("edition", "") >= cutoff and h.get("edition") != ctx.edition.isoformat()]


if __name__ == "__main__":
    stage_main(run, __doc__)
```

## v1_workflow/stages/s04_classify.py

```python
"""s04_classify: category, importance 1 to 10, verification status and one-line why-it-matters for every retained
event. Cheap model, batched, on digests only. Code enforces the label bands and the 11-category taxonomy.

Input: work/events.jsonl   Output: work/ranked.jsonl
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.common import log, read_jsonl, stage_main, write_jsonl  # noqa: E402
from lib.llm_client import LLMClient, batched  # noqa: E402


def run(ctx, extra_args=None) -> int:
    events = read_jsonl(ctx.work / "events.jsonl")
    if not events:
        log.error("no events.jsonl; run s03 first")
        return 1
    retained = [e for e in events if e["disposition"] == "RETAINED EVENT ID"]
    llm = LLMClient(ctx)
    size = ctx.config["llm"]["batch_sizes"].get("classify", 40)
    cats = [{"key": c["key"], "name": c["name"]} for c in ctx.category_order()]
    result = {}
    for batch in batched(retained, size):
        payload = {"categories": cats,
                   "scoring_rules": ["AI News Desk is an AI news channel, not a business channel: a large dollar figure alone never makes a story important.",
                                     "10 = CRITICAL: changes what AI can do, or affects many people, or a major government decision. 8-9 = HIGH. 6-7 = MEDIUM. 1-5 = WATCHLIST.",
                                     "Robotics means a robot or autonomous machine doing something, not a policy or a funding round about robots.",
                                     "verification: CONFIRMED (primary source or official), REPORTED (credible outlet, attributed), PRELIMINARY (early, unconfirmed), DISPUTED."],
                   "events": [{"id": e["id"], "headline": e["headline"], "summary": e["summary"], "key_facts": e["key_facts"],
                               "sources": e["sources"], "category_guess": e.get("category_guess"), "fun": e.get("fun", False)}
                              for e in batch]}
        reply = llm.call("cheap", "classify", payload, stage="s04_classify")
        for c in reply.get("classified", []):
            result[c["id"]] = c
    valid = {c["key"] for c in ctx.category_order()}
    out = []
    for e in retained:
        c = result.get(e["id"], {})
        score = int(c.get("importance") or 5)
        score = max(1, min(10, score))
        key = c.get("category") if c.get("category") in valid else ctx.category_key_from_name(c.get("category") or e.get("category_guess") or "")
        if e.get("fun") and key != "FUN" and score < 8:
            key = "FUN"
        cat = ctx.category_by_key(key)
        row = dict(e)
        row.update({"category": key, "category_name": cat["name"] if cat else key, "subcategory": c.get("subcategory", ""),
                    "importance": score, "label": ctx.importance_label(score),
                    "verification": c.get("verification") if c.get("verification") in ctx.categories["verification_statuses"] else "REPORTED",
                    "why_it_matters": c.get("why_it_matters", ""), "big_name": bool(c.get("big_name"))})
        out.append(row)
    out.sort(key=lambda r: (-r["importance"], [c["key"] for c in ctx.category_order()].index(r["category"]), r["id"]))
    write_jsonl(ctx.work / "ranked.jsonl", out)
    counts = {}
    for r in out:
        counts[r["label"]] = counts.get(r["label"], 0) + 1
    ctx.report_append("s04 classify", f"{len(out)} events classified: {counts}. Categories: "
                                      + ", ".join(f"{k}={sum(1 for r in out if r['category']==k)}" for k in valid))
    ctx.set_stage("s04_classify", "done", classified=len(out), **{k.lower(): v for k, v in counts.items()})
    return 0


if __name__ == "__main__":
    stage_main(run, __doc__)
```

## v1_workflow/stages/s05_gates.py

```python
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
```

## v1_workflow/stages/s06_report.py

```python
"""s06_report: the Daily Global AI Intelligence Report in the master prompt's story format, plus daily-pool.md.
Mid model writes story blocks from digests in batches; strong model writes the forward-looking analysis once,
from headlines and importance lines only (never the full text). Category order: Decision Log 23 Sep 2026.

Inputs: work/ranked.jsonl, work/pool_dispositions.jsonl, work/raw_pool.jsonl, work/source_ledger.json
Outputs: reports/<date> — Daily Global AI Intelligence Report.md, reports/supportive files/daily-pool.md,
         work/report_items.json (item numbers used by cards, bulletin and headlines)
"""
from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.common import load_json, log, read_jsonl, save_json, stage_main, update_checkpoint  # noqa: E402
from lib.llm_client import LLMClient, batched  # noqa: E402

SEP = "─" * 20


def select(ctx, ranked: list[dict]) -> list[dict]:
    g = ctx.config["gates"]
    order = [c["key"] for c in ctx.category_order()]
    pool = sorted(ranked, key=lambda r: (-r["importance"], order.index(r["category"]), r["id"]))
    chosen = pool[: g["report_max"]]
    crit = [r for r in chosen if r["importance"] >= 10]
    rest = [r for r in chosen if r["importance"] < 10]
    rest.sort(key=lambda r: (order.index(r["category"]), -r["importance"], r["id"]))
    return crit + rest


def run(ctx, extra_args=None) -> int:
    ranked = read_jsonl(ctx.work / "ranked.jsonl")
    if not ranked:
        log.error("no ranked.jsonl; run s04 first")
        return 1
    g = ctx.config["gates"]
    items = select(ctx, ranked)
    if len(items) < g["report_min"]:
        ctx.set_gate("full_report_gate_50_150", "FAIL", f"{len(items)} events below minimum {g['report_min']}")
        ctx.report_append("s06 report", f"FULL REPORT GATE FAILED: {len(items)} unique events, minimum {g['report_min']}. Stopped.")
        ctx.set_stage("s06_report", "failed", count=len(items))
        return 2
    llm = LLMClient(ctx)
    written = {}
    for batch in batched(items, ctx.config["llm"]["batch_sizes"].get("report", 12)):
        payload = {"format": "headline, importance reason, summary (one or two complete sentences with the new facts, numbers, context; do not repeat the headline)",
                   "events": [{"id": e["id"], "headline": e["headline"], "summary": e["summary"], "key_facts": e["key_facts"],
                               "label": e["label"], "category": e["category_name"], "why_it_matters": e.get("why_it_matters", ""),
                               "sources": e["sources"]} for e in batch]}
        reply = llm.call("mid", "report_story", payload, stage="s06_report")
        for s in reply.get("stories", []):
            written[s["id"]] = s
    # assemble
    ledger = load_json(ctx.work / "source_ledger.json", default={})
    disp = read_jsonl(ctx.work / "pool_dispositions.jsonl")
    n_dup = sum(1 for d in disp if d["disposition"].startswith("DUPLICATE"))
    n_prev = sum(1 for d in disp if d["disposition"].startswith("PREVIOUSLY"))
    crit = sum(1 for e in items if e["importance"] >= 10)
    high = sum(1 for e in items if 8 <= e["importance"] < 10)
    header = [f"*Daily Global AI Intelligence Report*", f"*Daily report date:* {ctx.edition.strftime('%-d %B %Y') if sys.platform != 'win32' else ctx.edition.strftime('%d %B %Y')}",
              f"*Weekly briefing:* AI News Desk V1 workflow, Claude lane test run (not the ChatGPT scheduled task)",
              f"*Coverage period:* {ctx.window_start.strftime('%d %b %Y %H:%M')} to {ctx.window_end.strftime('%d %b %Y %H:%M')} {ctx.config['timezone']}",
              f"*Candidates collected:* {sum(1 for d in disp if d['window_check'] != 'OUT OF WINDOW')}",
              f"*Same-day duplicates removed:* {n_dup}", f"*Previously covered stories removed:* {n_prev}",
              f"*Material updates included:* 0", f"*Final unique stories (total unique items found):* {len(items)}",
              f"*Critical items:* {crit}", f"*High-priority items:* {high}",
              f"*Major coverage groups searched:* {ledger.get('sources_checked_success_count', 0)} of {ledger.get('registry_source_count', 0)} registered sources checked",
              ""]
    if len(items) < 100:
        header.append(f"*Reason fewer than 100 stories were included:* {len(items)} unique verified events survived deduplication for this window.")
        header.append("")
    lines = header
    numbered = []
    n = 0
    section = None
    for e in items:
        sec = "Critical AI Developments" if e["importance"] >= 10 else e["category_name"]
        if sec != section:
            section = sec
            lines += [f"*{section}*", ""]
        n += 1
        s = written.get(e["id"], {})
        e_out = {"n": n, "id": e["id"], "headline": s.get("headline") or e["headline"], "label": e["label"], "category": e["category"],
                 "category_name": e["category_name"], "importance": e["importance"], "summary": s.get("summary") or e["summary"],
                 "importance_reason": s.get("importance_reason") or e.get("why_it_matters", ""), "source": e["primary_source"],
                 "url": e["primary_url"], "key_facts": e["key_facts"], "verification": e["verification"], "fun": e.get("fun", False),
                 "big_name": e.get("big_name", False)}
        numbered.append(e_out)
        lines += [f"*{n}. {e_out['headline']}*", f"*Importance:* {e_out['label']} — {e_out['importance_reason']}",
                  f"*Source:* {e_out['source']}", f"*Summary:* {e_out['summary']}", f"*Full article:* {e_out['url']}", SEP, ""]
    # forward-looking analysis (strong model, small input)
    payload = {"edition": ctx.edition.isoformat(),
               "items": [{"n": x["n"], "headline": x["headline"], "label": x["label"], "category": x["category_name"]} for x in numbered],
               "previous_analyses": recent_analyses(ctx)}
    analysis = llm.call("strong", "analysis", payload, stage="s06_report").get("analysis_markdown", "")
    lines += ["", "*FORWARD-LOOKING ANALYSIS: PROBABILITIES, OUTCOMES, WHAT MAY HAPPEN NEXT*", "", analysis.strip(), "",
              "END OF REPORT", ""]
    path = ctx.reports / f"{ctx.edition.isoformat()} — Daily Global AI Intelligence Report.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    save_json(ctx.work / "report_items.json", {"edition": ctx.edition.isoformat(), "count": len(numbered), "items": numbered})
    write_daily_pool(ctx, disp, ranked)
    # history for future dedupe
    hist = ctx.history / "events_history.jsonl"
    hist.parent.mkdir(parents=True, exist_ok=True)
    existing = {h.get("id") for h in read_jsonl(hist)}
    with hist.open("a", encoding="utf-8") as fh:
        for x in numbered:
            if x["id"] not in existing:
                fh.write(__import__("json").dumps({"id": x["id"], "edition": ctx.edition.isoformat(), "headline": x["headline"],
                                                   "summary": x["summary"], "url": x["url"]}, ensure_ascii=False) + "\n")
    ctx.set_gate("full_report_gate_50_150", "PASS", f"{len(numbered)} stories")
    update_checkpoint(ctx, {"full_report_count": len(numbered)}, {"full_report_gate_50_150": "PASS"})
    ctx.report_append("s06 report", f"Full Report written: {path.name}, {len(numbered)} stories ({crit} critical, {high} high). "
                                    f"daily-pool.md written. LLM so far: {llm.summary()}")
    ctx.set_stage("s06_report", "done", count=len(numbered), path=str(path))
    return 0


def recent_analyses(ctx) -> list[dict]:
    """Headings of previous editions' analyses if the run folders exist locally (max 14 days)."""
    out = []
    for i in range(1, 15):
        d = ctx.edition - dt.timedelta(days=i)
        f = ctx.local_root / d.isoformat() / "reports" / f"{d.isoformat()} — Daily Global AI Intelligence Report.md"
        if f.exists():
            text = f.read_text(encoding="utf-8")
            if "FORWARD-LOOKING ANALYSIS" in text:
                out.append({"edition": d.isoformat(), "excerpt": text.split("FORWARD-LOOKING ANALYSIS", 1)[1][:1200]})
    return out


def write_daily_pool(ctx, disp: list[dict], ranked: list[dict]) -> None:
    """daily-pool.md per AIND_daily_storage_rules.txt: every record, its outcome and reason, grouped for reading."""
    by_id = {r["id"]: r for r in ranked}
    lines = [f"# Daily Pool — {ctx.edition.isoformat()}", "", f"Edition date: {ctx.edition.isoformat()}",
             f"Reporting window: {ctx.window_start.strftime('%Y-%m-%d %H:%M')} to {ctx.window_end.strftime('%Y-%m-%d %H:%M')}",
             f"Timezone: {ctx.config['timezone']}", f"Run identity: AI News Desk V1 workflow, Claude lane ({ctx.lane}), test run",
             f"Last updated: {dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}", "Status: Complete", "",
             "## Part 1. Retained events by category (importance order)", ""]
    for c in ctx.category_order():
        rows = [r for r in ranked if r["category"] == c["key"]]
        if not rows:
            lines += [f"### {c['name']}", "", "searched, no qualifying result", ""]
            continue
        lines += [f"### {c['name']} ({len(rows)})", ""]
        for r in sorted(rows, key=lambda x: -x["importance"]):
            lines += [f"- {r['id']} [{r['importance']}/10 {r['label']}] {r['headline']} — {r['primary_source']} — {r['primary_url']}"]
        lines.append("")
    lines += ["## Part 2. Every collected record and its disposition", "", "| id | disposition | window | source | title | url |", "|---|---|---|---|---|---|"]
    for d in disp:
        lines.append(f"| {d['id']} | {d['disposition']} | {d['window_check']} | {d['source']} | {d['title'][:90].replace('|','/')} | {d['url']} |")
    lines.append("")
    (ctx.reports_sup / "daily-pool.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    stage_main(run, __doc__)
```

## v1_workflow/stages/s07_bulletin.py

```python
"""s07_bulletin: 25 to 30 articles from the Full Report only (18 Sep gate F), in the approved category order,
rewritten under the plain language law with the 26 Sep source-to-script meaning check. Mid model, two calls.

Input: work/report_items.json   Output: reports/<date> — Daily Bulletin.md, work/bulletin.json
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.common import load_json, log, save_json, stage_main, update_checkpoint  # noqa: E402
from lib.llm_client import LLMClient  # noqa: E402


def select(ctx, items: list[dict]) -> list[dict]:
    g = ctx.config["gates"]
    order = [c["key"] for c in ctx.category_order()]
    crit = [i for i in items if i["importance"] >= 10]
    high = [i for i in items if 8 <= i["importance"] < 10]
    med = [i for i in items if 6 <= i["importance"] < 8]
    chosen = crit + high
    # breadth: at least one per category where a medium exists
    have = {i["category"] for i in chosen}
    for m in sorted(med, key=lambda x: -x["importance"]):
        if m["category"] not in have and len(chosen) < g["bulletin_max"]:
            chosen.append(m)
            have.add(m["category"])
    for m in sorted(med, key=lambda x: -x["importance"]):
        if len(chosen) >= g["bulletin_min"]:
            break
        if m not in chosen:
            chosen.append(m)
    chosen = sorted(chosen, key=lambda x: -x["importance"])[: g["bulletin_max"]]
    crit = [i for i in chosen if i["importance"] >= 10]
    rest = sorted([i for i in chosen if i["importance"] < 10], key=lambda i: (order.index(i["category"]), -i["importance"]))
    return crit + rest


def run(ctx, extra_args=None) -> int:
    rep = load_json(ctx.work / "report_items.json", default={})
    items = rep.get("items", [])
    if not items:
        log.error("no report_items.json; run s06 first")
        return 1
    g = ctx.config["gates"]
    chosen = select(ctx, items)
    if not (g["bulletin_min"] <= len(chosen) <= g["bulletin_max"]):
        ctx.set_gate("bulletin_gate", "FAIL", f"{len(chosen)} items")
        ctx.report_append("s07 bulletin", f"BULLETIN GATE FAILED: {len(chosen)} items, need {g['bulletin_min']} to {g['bulletin_max']}.")
        ctx.set_stage("s07_bulletin", "failed", count=len(chosen))
        return 2
    llm = LLMClient(ctx)
    payload = {"law": "AIND plain language law v1: headline is a full spoken sentence; body is two sentences: what happened, then why it matters or the honest doubt; no jargon; numbers translated unless the number is the story; lead non-market stories with the deed, not the money; unfamiliar companies get a short title.",
               "items": [{"id": i["id"], "n": i["n"], "headline": i["headline"], "summary": i["summary"], "key_facts": i["key_facts"],
                          "category": i["category_name"], "source": i["source"], "verification": i["verification"]} for i in chosen]}
    reply = llm.call("mid", "bulletin_copy", payload, stage="s07_bulletin")
    copy = {c["id"]: c for c in reply.get("items", [])}
    check = llm.call("mid", "meaning_check", {"items": [{"id": i["id"], "source_facts": i["key_facts"] + [i["summary"]],
                                                          "written": copy.get(i["id"], {})} for i in chosen]}, stage="s07_bulletin")
    results = {r["id"]: r for r in check.get("results", [])}
    out, failed = [], []
    for i in chosen:
        c = copy.get(i["id"], {})
        r = results.get(i["id"], {"result": "UNVERIFIED"})
        row = dict(i)
        row.update({"bulletin_headline": c.get("headline") or i["headline"], "bulletin_body": c.get("body") or i["summary"],
                    "meaning_check": r.get("result", "UNVERIFIED"), "meaning_note": r.get("note", "")})
        out.append(row)  # failing rows stay in the bulletin flagged DRAFT for Rafael
        if row["meaning_check"] != "PASS":
            failed.append(row)
    counts = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0}
    for r in out:
        counts[r["label"]] = counts.get(r["label"], 0) + 1
    lines = [f"# {ctx.edition.isoformat()} — Daily Bulletin", "",
             f"Edition: {ctx.edition.isoformat()}. Source: derived only from the same edition's Daily Global AI Intelligence Report. Item numbers refer to that report. No new research.",
             f"Bulletin count: {len(out)} (gate: {g['bulletin_min']} to {g['bulletin_max']}). Critical: {counts.get('CRITICAL',0)}. High: {counts.get('HIGH',0)}. Medium: {counts.get('MEDIUM',0)}.",
             "Private production draft; not approved for publication.", ""]
    section = None
    for r in out:
        sec = "Critical" if r["importance"] >= 10 else r["category_name"]
        if sec != section:
            section = sec
            lines += [f"## {section}", ""]
        flag = "" if r["meaning_check"] == "PASS" else f"  (DRAFT: meaning check {r['meaning_check']} {r['meaning_note']})"
        lines += [f"### {r['n']}. {r['bulletin_headline']}{flag}", "", r["bulletin_body"], "",
                  f"Full Report item {r['n']} | {r['category_name']} | Score {r['importance']}/10 | {r['verification']} | {r['source']}", ""]
    (ctx.reports / f"{ctx.edition.isoformat()} — Daily Bulletin.md").write_text("\n".join(lines), encoding="utf-8")
    save_json(ctx.work / "bulletin.json", {"edition": ctx.edition.isoformat(), "count": len(out), "items": out})
    ctx.set_gate("bulletin_gate", "PASS", f"{len(out)} items, {len(failed)} meaning-check drafts")
    update_checkpoint(ctx, {"bulletin_count": len(out)}, {"bulletin_gate": "PASS"})
    ctx.report_append("s07 bulletin", f"{len(out)} bulletin items ({counts}); {len(failed)} kept as drafts after the meaning check.")
    ctx.set_stage("s07_bulletin", "done", count=len(out), drafts=len(failed))
    return 0


if __name__ == "__main__":
    stage_main(run, __doc__)
```

## v1_workflow/stages/s08_bigger_picture.py

```python
"""s08_bigger_picture: The Bigger Picture (approved names, 12 Sep 2026) from the bulletin only. Strong model, one call,
small input. Produces the full analysis doc, the card copy and the spoken reel line (44 to 53 syllables).

Input: work/bulletin.json   Output: reports/the bigger picture_<date>.md, work/bigger_picture.json
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.common import load_json, log, save_json, stage_main  # noqa: E402
from lib.llm_client import LLMClient  # noqa: E402
from lib.syllables import count  # noqa: E402


def run(ctx, extra_args=None) -> int:
    bul = load_json(ctx.work / "bulletin.json", default={})
    if not bul.get("items"):
        log.error("no bulletin.json; run s07 first")
        return 1
    cfg = ctx.config["cards"]
    lo, hi = ctx.config["headlines"]["bigger_picture_syllables"]
    llm = LLMClient(ctx)
    payload = {"corner_name": cfg["analysis_corner"], "full_name": f"{cfg['analysis_corner']} — Daily AI Analysis",
               "description": "What today’s developments could mean for technology, business and everyday life.",
               "opening": cfg["analysis_opening"], "spoken_syllables": [lo, hi],
               "rules": ["Desk judgement, clearly separated from reported facts; cite report item numbers.",
                         "No investment recommendation, price target or buy/sell language.", "Plain language law applies."],
               "items": [{"n": i["n"], "headline": i["bulletin_headline"], "body": i["bulletin_body"], "category": i["category_name"],
                          "key_facts": i["key_facts"][:3]} for i in bul["items"]]}
    reply = llm.call("strong", "bigger_picture", payload, stage="s08_bigger_picture")
    spoken = reply.get("spoken", "")
    syl = count(spoken)
    note = "" if lo <= syl <= hi else f"spoken line is {syl} syllables, outside {lo} to {hi}; s12 will ask for a rewrite"
    doc = ["# " + payload["full_name"], "", payload["description"], "",
           f"Edition: {ctx.edition.isoformat()}. Source: derived only from the same edition's Daily Bulletin and Full Report. Private production draft; not approved for publication. Not investment advice.",
           "", payload["opening"], "", reply.get("full_markdown", "").strip(), ""]
    (ctx.reports / f"the bigger picture_{ctx.edition.isoformat()}.md").write_text("\n".join(doc), encoding="utf-8")
    save_json(ctx.work / "bigger_picture.json", {"edition": ctx.edition.isoformat(), "head": reply.get("head", ""),
                                                 "card_body": reply.get("card_body", ""), "items": reply.get("items", []),
                                                 "spoken": spoken, "spoken_syllables": syl, "report_refs": reply.get("report_refs", []),
                                                 "note": note})
    ctx.report_append("s08 bigger picture", f"written; spoken line {syl} syllables. {note}")
    ctx.set_stage("s08_bigger_picture", "done", syllables=syl)
    return 0


if __name__ == "__main__":
    stage_main(run, __doc__)
```

## v1_workflow/stages/s09_cards_select.py

```python
"""s09_cards_select: the paper-first deck list (Cards Master Section 2, category order of 23 Sep 2026). Zero LLM.

Card 1 cover; every critical (a critical spends its category's slot); then the category order with its slot counts,
highest score fills a slot; market at most 3 story cards including criticals; robotics and fun normally required;
fun is always the last story card; then "More in the full report" (3 to 4 uncarded headlines), The Bigger Picture,
closing. Exactly gates.cards_count cards (15). Departures are recorded, never silent.

Input: work/report_items.json, work/bigger_picture.json
Output: work/cards_selection.json, cards/supportive files/cards_<D-M-YY>_selection.md
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.common import load_json, log, save_json, stage_main, update_checkpoint  # noqa: E402

MONEY = ("$", "billion", "million", "funding", "valuation", "revenue", "raises", "raised")


def select(ctx, items: list[dict], notes: list[str]) -> tuple[list[dict], list[dict]]:
    cats = ctx.categories
    g = ctx.config["gates"]
    order = ctx.category_order()
    keys = [c["key"] for c in order]
    story_slots = g["cards_count"] - 4  # cover, teaser, bigger picture, closing
    slots = {c["key"]: c["cards_slots"] for c in order}
    mkt_max = cats.get("market_max_including_criticals", 3)
    chosen: list[dict] = []
    used: set[str] = set()

    def mkt_count() -> int:
        return sum(1 for i in chosen if i["category"] == "MKT")

    def take(it: dict, why: str) -> None:
        chosen.append(dict(it, pick_reason=why))
        used.add(it["id"])
        slots[it["category"]] = max(0, slots.get(it["category"], 0) - 1)

    def room() -> int:
        return story_slots - reserve - len(chosen)

    # fun: reserved for the last story card
    fun_pool = [i for i in items if i["category"] == "FUN" or i.get("fun")]
    fun = max(fun_pool, key=lambda i: (i["importance"], -i["n"]), default=None)
    reserve = 1 if fun else 0
    if not fun and cats.get("fun_required"):
        notes.append("Fun: the report has no fun story; the fun slot is released to the next category. Notify Rafael.")
    fun_id = fun["id"] if fun else None

    # 1. criticals, score order, each spends its category slot
    crit = sorted([i for i in items if i["importance"] >= 10 and i["id"] != fun_id],
                  key=lambda i: (-i["importance"], keys.index(i["category"]), i["n"]))
    left_out = []
    for it in crit:
        if room() <= 0:
            left_out.append(it["n"])
            continue
        if it["category"] == "MKT" and mkt_count() >= mkt_max:
            notes.append(f"Critical item {it['n']} (market) left out: money cap of {mkt_max} story cards reached.")
            continue
        take(it, f"critical, spends the {it['category_name']} slot")

    if left_out:
        notes.append(f"{len(left_out)} critical items left out because the deck is full: items {left_out}. Rafael decides.")

    # 2. big release rule (10 Sep): a major release from a big company takes the first slot after the criticals
    big = [i for i in items if i["id"] not in used and i["category"] == "MOD" and i.get("big_name") and i["importance"] >= 8]
    if big and room() > 0 and slots["MOD"] > 0:
        take(max(big, key=lambda i: (i["importance"], -i["n"])), "big release rule: first slot after the criticals")
        notes.append("Big release rule applied (10 Sep): noted for the handoff.")

    # 3. category order with slot counts, highest score fills a slot (MEDIUM or better first)
    for c in order:
        if c["key"] == "FUN":
            continue
        pool = sorted([i for i in items if i["id"] not in used and i["category"] == c["key"] and i["importance"] >= 6],
                      key=lambda i: (-i["importance"], i["n"]))
        while slots[c["key"]] > 0 and pool and room() > 0:
            if c["key"] == "MKT" and mkt_count() >= mkt_max:
                break
            take(pool.pop(0), f"{c['name']} slot")

    # 4. still short: strongest remaining stories regardless of slot plan (money cap still holds)
    if room() > 0:
        rest = sorted([i for i in items if i["id"] not in used and i["id"] != fun_id],
                      key=lambda i: (-i["importance"], keys.index(i["category"]), i["n"]))
        for it in rest:
            if room() <= 0:
                break
            if it["category"] == "MKT" and mkt_count() >= mkt_max:
                continue
            take(it, "fill: strongest remaining story after the slot plan")
        if rest:
            notes.append("The category slot plan did not fill the deck; remaining slots were filled by score.")
    if fun:
        take(fun, "fun, always the last story card")

    # checks
    if cats.get("robotics_required") and not any(i["category"] == "ROB" for i in chosen):
        notes.append("Robotics: no robotics story carded (none in the report at MEDIUM or better). Notify Rafael.")
    non_biz = sum(1 for i in chosen if i["category"] != "MKT")
    if non_biz < cats.get("min_non_business_stories", 3):
        notes.append(f"Only {non_biz} non-market story cards; the deck reads money heavy. Notify Rafael.")
    for i in chosen:
        if i["category"] != "MKT" and any(w in i["headline"].lower() for w in MONEY):
            notes.append(f"Item {i['n']} ({i['category_name']}): headline mentions money; the copy stage must lead with the deed.")

    def sort_key(i: dict):
        if i["id"] == fun_id:
            return (3, 0, 0, i["n"])
        if i["pick_reason"].startswith("critical"):
            return (0, -i["importance"], keys.index(i["category"]), i["n"])
        if i["pick_reason"].startswith("big release"):
            return (1, 0, 0, i["n"])
        return (2, keys.index(i["category"]), -i["importance"], i["n"])
    chosen.sort(key=sort_key)

    # teaser: 3 to 4 uncarded headlines, distinct categories first, strongest first
    left = sorted([i for i in items if i["id"] not in used], key=lambda i: (-i["importance"], i["n"]))
    teaser, seen = [], set()
    for i in left:
        if i["category"] in seen:
            continue
        teaser.append(i)
        seen.add(i["category"])
        if len(teaser) == 4:
            break
    for i in left:
        if len(teaser) >= 3:
            break
        if i not in teaser:
            teaser.append(i)
    return chosen, teaser


def run(ctx, extra_args=None) -> int:
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--allow-short", default="", help="reason (Rafael's) to accept a deck with fewer than cards_count cards")
    args = p.parse_args(extra_args or [])
    rep = load_json(ctx.work / "report_items.json", default={})
    items = rep.get("items", [])
    if not items:
        log.error("no report_items.json; run s06 first")
        return 1
    bp = load_json(ctx.work / "bigger_picture.json", default={})
    if not bp.get("head"):
        log.error("no bigger_picture.json; run s08 first")
        return 1
    g = ctx.config["gates"]
    notes: list[str] = []
    chosen, teaser = select(ctx, items, notes)
    deck = [{"kind": "cover"}]
    for it in chosen:
        deck.append({"kind": "story", "item_n": it["n"], "event_id": it["id"], "category": it["category"],
                     "category_name": it["category_name"], "headline": it["headline"], "importance": it["importance"],
                     "label": it["label"], "verification": it["verification"], "source": it["source"], "url": it["url"],
                     "pick_reason": it["pick_reason"]})
    deck.append({"kind": "teaser", "title": ctx.config["cards"]["teaser_title"],
                 "items": [{"item_n": t["n"], "event_id": t["id"], "headline": t["headline"], "category": t["category"],
                            "category_name": t["category_name"]} for t in teaser]})
    deck.append({"kind": "bigger_picture", "head": bp["head"], "report_refs": bp.get("report_refs", [])})
    deck.append({"kind": "closing"})
    for k, d in enumerate(deck, 1):
        d["order"] = k
        d["id"] = f"I{k:02d}"
        d["file"] = f"cards_{ctx.short}_I{k:02d}_{ctx.lane}.png"
    mkt = sum(1 for d in deck if d["kind"] == "story" and d["category"] == "MKT")
    ok = len(deck) == g["cards_count"]
    if not ok and not args.allow_short:
        ctx.set_gate("cards_selection_gate", "FAIL", f"{len(deck)} cards planned, need {g['cards_count']}")
        ctx.report_append("s09 cards select", f"CARDS SELECTION GATE FAILED: {len(deck)} cards, need {g['cards_count']}. "
                                              f"Re-run with --allow-short \"reason\" only on Rafael's word.\n" + "\n".join(f"- {n}" for n in notes))
        ctx.set_stage("s09_cards_select", "failed", count=len(deck))
        return 2
    if not ok:
        notes.append(f"Deck accepted short at {len(deck)} cards on Rafael's word: {args.allow_short}")
    sel = {"edition": ctx.edition.isoformat(), "short": ctx.short, "lane": ctx.lane, "count": len(deck),
           "story_cards": len(chosen), "market_cards": mkt, "deck": deck, "notes": notes, "status": "planned, not rendered, not approved"}
    save_json(ctx.work / "cards_selection.json", sel)
    lines = [f"# cards_{ctx.short} — selection (paper-first list, Cards Master Section 2)", "",
             f"Edition {ctx.edition.isoformat()}. Source: the Full Report only. Order: criticals by score, then the 23 Sep category order, fun last.",
             f"Cards: {len(deck)}. Story cards: {len(chosen)}. Market cards including criticals: {mkt} (cap {ctx.categories.get('market_max_including_criticals', 3)}).",
             "Not rendered, not approved for publication.", ""]
    for d in deck:
        if d["kind"] == "story":
            lines.append(f"{d['order']:>2}. {d['id']}  [{d['label']} {d['importance']}/10] {d['category_name']} — item {d['item_n']}: {d['headline']}  ({d['pick_reason']})")
        elif d["kind"] == "teaser":
            lines.append(f"{d['order']:>2}. {d['id']}  {d['title']}: " + "; ".join(f"item {t['item_n']} {t['category_name']}" for t in d["items"]))
        elif d["kind"] == "bigger_picture":
            lines.append(f"{d['order']:>2}. {d['id']}  The Bigger Picture: {d['head']}")
        else:
            lines.append(f"{d['order']:>2}. {d['id']}  {d['kind']}")
    if notes:
        lines += ["", "## Notes for Rafael", ""] + [f"- {n}" for n in notes]
    (ctx.cards_sup / f"cards_{ctx.short}_selection.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    ctx.set_gate("cards_selection_gate", "PASS", f"{len(deck)} cards, {mkt} market")
    update_checkpoint(ctx, {"cards_planned_count": len(deck)}, {"cards_selection_gate": "PASS"})
    ctx.report_append("s09 cards select", f"{len(deck)} cards planned ({len(chosen)} stories, {mkt} market). Teaser items: "
                                          f"{[t['n'] for t in teaser]}.\n" + "\n".join(f"- {n}" for n in notes))
    ctx.set_stage("s09_cards_select", "done", count=len(deck), stories=len(chosen), market=mkt)
    return 0


if __name__ == "__main__":
    stage_main(run, __doc__)
```

## v1_workflow/stages/s10_cards_copy.py

```python
"""s10_cards_copy: the card copy for the planned deck. Mid model writes story and teaser copy in one batch
(or a few), then the meaning check. Code fills cover, The Bigger Picture and closing from config and s08.
Ends with Rafael's approval pause (house rule 4): exit 3 until approvals/s10_cards_copy.approved exists.

Input: work/cards_selection.json, work/report_items.json, work/bigger_picture.json
Output: cards/supportive files/cards_<D-M-YY>_copy.json and cards_<D-M-YY>_copy.md
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.common import RC_APPROVAL, load_json, log, long_date, require_approval, save_json, stage_main  # noqa: E402
from lib.llm_client import LLMClient, batched  # noqa: E402

LAW = ("AIND plain language law v1: head is one full spoken sentence ending with a period; body is exactly two "
       "sentences, what happened then why it matters or the honest doubt; no jargon; numbers translated unless the "
       "number is the story; non-market cards lead with the deed, never the money; unfamiliar companies get a short title.")
MONEY = re.compile(r"\$|\b(billion|million|funding|valuation|revenue|raises|raised|shares|stock)\b", re.I)


def sentences(text: str) -> int:
    return len([s for s in re.split(r"(?<=[.!?])\s+", (text or "").strip()) if s])


def run(ctx, extra_args=None) -> int:
    sel = load_json(ctx.work / "cards_selection.json", default={})
    rep = load_json(ctx.work / "report_items.json", default={})
    bp = load_json(ctx.work / "bigger_picture.json", default={})
    if not sel.get("deck") or not rep.get("items"):
        log.error("need cards_selection.json and report_items.json; run s06 to s09 first")
        return 1
    by_n = {i["n"]: i for i in rep["items"]}
    cfg = ctx.config["cards"]
    llm = LLMClient(ctx)
    stories = [d for d in sel["deck"] if d["kind"] == "story"]
    teaser_card = next(d for d in sel["deck"] if d["kind"] == "teaser")
    written, tlines = {}, {}
    size = ctx.config["llm"]["batch_sizes"].get("copy", 20)
    for k, batch in enumerate(batched(stories, size)):
        payload = {"law": LAW, "rules": ["Cards Master Section 3: lead with the deed; unfamiliar companies titled; "
                                         "keep the verification wording; category line 'Category / topic'."],
                   "items": [{"id": d["id"], "n": d["item_n"], "headline": by_n[d["item_n"]]["headline"],
                              "summary": by_n[d["item_n"]]["summary"], "key_facts": by_n[d["item_n"]]["key_facts"],
                              "category_name": d["category_name"], "source": d["source"], "verification": d["verification"],
                              "importance": d["importance"], "label": d["label"]} for d in batch],
                   "teaser": [{"id": f"T{t['item_n']}", "n": t["item_n"], "headline": t["headline"], "category_name": t["category_name"]}
                              for t in teaser_card["items"]] if k == 0 else []}
        reply = llm.call("mid", "cards_copy", payload, stage="s10_cards_copy")
        for c in reply.get("cards", []):
            written[c["id"]] = c
        for t in reply.get("teaser", []):
            tlines[t["id"]] = t
    check = llm.call("mid", "meaning_check", {"items": [
        {"id": d["id"], "source_facts": by_n[d["item_n"]]["key_facts"] + [by_n[d["item_n"]]["summary"]],
         "written": {"head": written.get(d["id"], {}).get("head", ""), "body": written.get(d["id"], {}).get("body", "")}}
        for d in stories]}, stage="s10_cards_copy")
    results = {r["id"]: r for r in check.get("results", [])}
    flags: list[str] = []
    cards = []
    for d in sel["deck"]:
        base = {"order": d["order"], "id": d["id"], "file": d["file"], "kind": d["kind"]}
        if d["kind"] == "cover":
            base.update({"title": "TODAY IN AI", "subtitle": "in cards", "date": long_date(ctx.edition), "date_title": ctx.title_date})
        elif d["kind"] == "story":
            w = written.get(d["id"], {})
            r = results.get(d["id"], {"result": "UNVERIFIED", "note": "no check result"})
            src = by_n[d["item_n"]]
            head = w.get("head") or src["headline"].rstrip(".") + "."
            body = w.get("body") or src["summary"]
            base.update({"head": head, "body": body, "cat": w.get("cat") or f"{d['category_name']} / {src.get('subcategory') or 'today'}",
                         "src": (w.get("src") or d["source"] or "SOURCE").upper(), "pill": d["verification"], "item_n": d["item_n"],
                         "url": d["url"], "category": d["category"], "category_name": d["category_name"], "importance": d["importance"],
                         "meaning_check": r.get("result", "UNVERIFIED"), "meaning_note": r.get("note", "")})
            if r.get("result") != "PASS":
                flags.append(f"{d['id']} item {d['item_n']}: meaning check {r.get('result')}: {r.get('note', '')} {r.get('unsupported', '')}")
            if sentences(body) != 2:
                flags.append(f"{d['id']}: body has {sentences(body)} sentences, the law says two.")
            if d["category"] != "MKT" and MONEY.search(head):
                flags.append(f"{d['id']}: non-market head mentions money; lead with the deed.")
        elif d["kind"] == "teaser":
            lines = []
            for t in d["items"]:
                tl = tlines.get(f"T{t['item_n']}", {})
                lines.append({"item_n": t["item_n"], "head": tl.get("head") or t["headline"].rstrip(".") + ".",
                              "cat": tl.get("cat") or t["category_name"]})
            base.update({"title": d["title"], "lines": lines, "closing_line": cfg["teaser_closing_line"],
                         "src": "DAILY GLOBAL AI INTELLIGENCE REPORT"})
        elif d["kind"] == "bigger_picture":
            base.update({"opening": cfg["analysis_opening"], "head": bp["head"], "body": bp.get("card_body", ""),
                         "items": bp.get("items", []), "pill": "DESK VIEW", "src": "AI NEWS DESK", "cat": f"{cfg['analysis_corner']} / Desk view",
                         "report_refs": bp.get("report_refs", [])})
        else:
            base.update({"head": cfg["closing_head"], "body": cfg["closing_body"]})
        cards.append(base)
    out = {"edition": ctx.edition.isoformat(), "short": ctx.short, "lane": ctx.lane, "date_title": ctx.title_date,
           "date_long": long_date(ctx.edition), "notice": cfg["notice"], "count": len(cards), "cards": cards, "flags": flags,
           "status": "draft copy; pending Rafael's approval; not rendered; not approved for publication"}
    path = ctx.cards_sup / f"cards_{ctx.short}_copy.json"
    save_json(path, out)
    md = [f"# cards_{ctx.short} — copy (draft)", "", f"Edition {ctx.edition.isoformat()}. {len(cards)} cards. Source: Full Report only.", ""]
    for c in cards:
        md.append(f"## {c['id']}  {c['kind']}")
        if c["kind"] == "story":
            md += [f"**{c['head']}**", "", c["body"], "", f"{c['cat']} | {c['src']} | {c['pill']} | report item {c['item_n']} | meaning check {c['meaning_check']}", ""]
        elif c["kind"] == "teaser":
            md += [f"**{c['title']}**", ""] + [f"- {l['head']}  ({l['cat']}, item {l['item_n']})" for l in c["lines"]] + ["", c["closing_line"], ""]
        elif c["kind"] == "bigger_picture":
            md += [c["opening"], f"**{c['head']}**", "", c["body"], ""] + [f"- {i}" for i in c["items"]] + ["", f"{c['pill']} | {c['src']}", ""]
        elif c["kind"] == "cover":
            md += [f"{c['title']} {c['subtitle']} — {c['date']}", ""]
        else:
            md += [f"**{c['head']}**", "", c["body"], ""]
    if flags:
        md += ["## Flags", ""] + [f"- {f}" for f in flags] + [""]
    text = "\n".join(md)
    (ctx.cards_sup / f"cards_{ctx.short}_copy.md").write_text(text, encoding="utf-8")
    ctx.report_append("s10 cards copy", f"copy written for {len(cards)} cards; {len(flags)} flags. LLM so far: {llm.summary()}")
    if not require_approval(ctx, "s10_cards_copy", "card copy review before rendering", text):
        ctx.set_stage("s10_cards_copy", "awaiting_approval", flags=len(flags))
        log.warning("APPROVAL NEEDED: read %s", ctx.approvals / "s10_cards_copy.pending.md")
        return RC_APPROVAL
    out["status"] = "copy approved by Rafael (approvals/s10_cards_copy.approved); not rendered; not approved for publication"
    save_json(path, out)
    ctx.set_stage("s10_cards_copy", "done", flags=len(flags), approved=True)
    return 0


if __name__ == "__main__":
    stage_main(run, __doc__)
```

## v1_workflow/stages/s11_cards_render.py

```python
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
```

## v1_workflow/stages/s12_headlines_select.py

```python
"""s12_headlines_select: the reel is the deck in miniature (Headlines blueprint V9.2, Section A, 25 Sep 2026).
Slot 1 stored intro (bypass); slots 2 to 8 seven story clips from the deck in deck order; 9 fun; 10 teaser from the
"More in the full report" card only; 11 The Bigger Picture (44 to 53 syllables); 12 stored ending (bypass).
Mid model writes the spoken lines with a rotating spoken introduction; code counts syllables (seconds = syllables / 4.4,
two decimals, no rounding up), loops for rewrites, checks digits, runs the meaning check. Ends with Rafael's spoken-copy
approval pause (exit 3).

Input: work/cards_selection.json, work/report_items.json, work/bigger_picture.json
Output: Headlines/supportive files/Headlines_<D-M-YY>_selection.md, headlines_<D-M-YY>_pack.json
"""
from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.common import RC_APPROVAL, load_json, log, require_approval, save_json, stage_main, update_checkpoint  # noqa: E402
from lib.llm_client import LLMClient  # noqa: E402
from lib.syllables import box_seconds, count  # noqa: E402

RULES = ["Every story and fun clip starts with a short natural spoken introduction suited to its subject; rotate wording, never yesterday's.",
         "Plain language law: short words, deed before money, unfamiliar companies get a short title, numbers as spoken words.",
         "Stories about 35 syllables (7 to 9 seconds at 4.4 syllables per second); The Bigger Picture 44 to 53 syllables.",
         "The teaser uses only the 'More in the full report' items, never a story that has its own clip.",
         "Only facts from the item. Never add a fact. Keep 'reportedly' or 'says' for REPORTED and PRELIMINARY items."]


def pick_core(deck_stories: list[dict], n: int, notes: list[str]) -> list[dict]:
    """Strongest n stories by score, keep robotics and one of law/research/society when present, then deck order."""
    ranked = sorted(deck_stories, key=lambda d: (-d["importance"], d["order"]))
    core = ranked[:n]
    def ensure(pred, name):
        nonlocal core
        if any(pred(d) for d in core):
            return
        cand = next((d for d in ranked if pred(d) and d not in core), None)
        if cand is None:
            notes.append(f"{name}: no such story in the deck.")
            return
        drop = next((d for d in reversed(core) if d["importance"] < 10 and not pred(d)), None)
        if drop is None:
            return
        core[core.index(drop)] = cand
        notes.append(f"{name}: swapped in item {cand['item_n']} for item {drop['item_n']} (blueprint Section A item 3).")
    ensure(lambda d: d["category"] == "ROB", "Robotics retained")
    ensure(lambda d: d["category"] in ("LAW", "RES", "SOC"), "Law, research or society included")
    return sorted(core, key=lambda d: d["order"])


def previous_intros(ctx) -> list[str]:
    out = []
    for i in range(1, 4):
        d = ctx.edition - dt.timedelta(days=i)
        f = ctx.local_root / d.isoformat() / ctx.config["products"]["headlines"] / ctx.config["products"]["supportive"] / f"headlines_{d.day}-{d.month}-{d.year % 100:02d}_pack.json"
        if f.exists():
            for s in load_json(f).get("slots", []):
                if s.get("script"):
                    out.append(s["script"].split(".")[0].split(",")[0].strip())
    return out


def run(ctx, extra_args=None) -> int:
    sel = load_json(ctx.work / "cards_selection.json", default={})
    rep = load_json(ctx.work / "report_items.json", default={})
    bp = load_json(ctx.work / "bigger_picture.json", default={})
    if not sel.get("deck") or not rep.get("items") or not bp.get("spoken"):
        log.error("need cards_selection.json, report_items.json and bigger_picture.json; run s06 to s09 first")
        return 1
    hcfg = ctx.config["headlines"]
    g = ctx.config["gates"]
    by_n = {i["n"]: i for i in rep["items"]}
    notes: list[str] = []
    stories = [d for d in sel["deck"] if d["kind"] == "story" and d["category"] != "FUN"]
    fun = next((d for d in sel["deck"] if d["kind"] == "story" and d["category"] == "FUN"), None)
    teaser_card = next(d for d in sel["deck"] if d["kind"] == "teaser")
    core = pick_core(stories, 7, notes)
    if len(core) < 7:
        notes.append(f"Only {len(core)} story clips available from the deck.")
    lo_s, hi_s = int(hcfg["story_box_min"] * hcfg["syllables_per_second"]), int(hcfg["story_box_max"] * hcfg["syllables_per_second"])
    lo_b, hi_b = hcfg["bigger_picture_syllables"]
    cues = {}  # scripts are written with normal spelling; s13 adds the spoken-cue line to the prompt
    cue_map = hcfg.get("pronunciation_cues", {})
    items = []
    slot = 2
    slot_meta = {}
    for d in core:
        src = by_n[d["item_n"]]
        items.append({"id": f"C{slot:02d}", "kind": "story", "headline": src["headline"], "summary": src["summary"], "key_facts": src["key_facts"],
                      "category_name": d["category_name"], "source": d["source"], "verification": d["verification"],
                      "target_syllables": hcfg["story_target_syllables"], "range": [lo_s, hi_s]})
        slot_meta[f"C{slot:02d}"] = d
        slot += 1
    fun_slot = 9
    if fun:
        src = by_n[fun["item_n"]]
        items.append({"id": "C09", "kind": "fun", "headline": src["headline"], "summary": src["summary"], "key_facts": src["key_facts"],
                      "category_name": "Fun", "source": fun["source"], "verification": fun["verification"],
                      "target_syllables": hcfg["story_target_syllables"], "range": [lo_s, hi_s]})
        slot_meta["C09"] = fun
    else:
        notes.append("Fun slot 9 bypassed: no fun card in the deck. Notify Rafael.")
    items.append({"id": "C10", "kind": "teaser", "teaser_items": [{"headline": t["headline"], "category_name": t["category_name"]} for t in teaser_card["items"]],
                  "target_syllables": hcfg["story_target_syllables"], "range": [lo_s, hi_s]})
    items.append({"id": "C11", "kind": "bigger_picture", "headline": bp["head"], "summary": bp.get("card_body", ""), "key_facts": bp.get("items", []),
                  "current_spoken": bp["spoken"], "opening": ctx.config["cards"]["analysis_opening"].replace("…", ""), "range": [lo_b, hi_b],
                  "target_syllables": (lo_b + hi_b) // 2})
    llm = LLMClient(ctx)
    reply = llm.call("mid", "headlines_copy", {"rules": RULES, "previous_intros": previous_intros(ctx), "items": items}, stage="s12_headlines_select")
    scripts = {r["id"]: r for r in reply.get("items", [])}
    ranges = {it["id"]: it["range"] for it in items}

    def problems(sid: str) -> list[str]:
        s = scripts.get(sid, {}).get("script", "")
        out = []
        n = count(s, cues)
        lo, hi = ranges[sid]
        if not s:
            out.append("empty script")
        if n < lo:
            out.append(f"too short: {n} syllables, need {lo} to {hi}")
        if n > hi:
            out.append(f"too long: {n} syllables, need {lo} to {hi}")
        if re.search(r"\d", s):
            out.append("contains digits; every number must be spoken words")
        if sid == "C11" and not s.lower().startswith("and for the bigger picture"):
            out.append("must start with 'And for the bigger picture,'")
        return out

    for round_no in range(1, 3):
        fixes = [dict(it, fix={"current_script": scripts.get(it["id"], {}).get("script", ""),
                               "current_syllables": count(scripts.get(it["id"], {}).get("script", ""), cues),
                               "problem": "; ".join(problems(it["id"]))}) for it in items if problems(it["id"])]
        if not fixes:
            break
        log.info("rewrite round %d for %s", round_no, [f["id"] for f in fixes])
        rep2 = llm.call("mid", "headlines_copy", {"rules": RULES, "previous_intros": previous_intros(ctx), "items": fixes}, stage="s12_headlines_select")
        for r in rep2.get("items", []):
            scripts[r["id"]] = r
    check = llm.call("mid", "meaning_check", {"items": [
        {"id": it["id"], "source_facts": it["key_facts"] + [it["summary"]], "written": {"script": scripts.get(it["id"], {}).get("script", "")}}
        for it in items if it["kind"] in ("story", "fun")]}, stage="s12_headlines_select")
    results = {r["id"]: r for r in check.get("results", [])}
    slots = [{"slot": 1, "kind": "intro", "state": "bypass", "title": "stored intro, date composited in post"}]
    total = 0.0
    for it in items:
        sid = it["id"]
        s = scripts.get(sid, {})
        script = s.get("script", "")
        n = count(script, cues)
        box = box_seconds(n, hcfg["syllables_per_second"])
        probs = problems(sid)
        row = {"slot": int(sid[1:]), "kind": it["kind"], "category": it.get("category_name", "The Bigger Picture" if it["kind"] == "bigger_picture" else "Teaser"),
               "symbol": s.get("symbol", "the AI News Desk logo on the blue holographic screen, unchanged"), "script": script,
               "syllables": n, "box_seconds": box, "problems": probs}
        if sid in slot_meta:
            d = slot_meta[sid]
            row.update({"item": d["item_n"], "story_id": d["event_id"], "source": d["source"], "source_url": d["url"], "card": d["id"],
                        "meaning_check": results.get(sid, {}).get("result", "UNVERIFIED"), "meaning_note": results.get(sid, {}).get("note", "")})
        elif it["kind"] == "teaser":
            row.update({"source": "AI NEWS DESK", "items": [t["item_n"] for t in teaser_card["items"]],
                        "story_ids": [t["event_id"] for t in teaser_card["items"]], "card": teaser_card["id"]})
        else:
            row.update({"source": "AI NEWS DESK", "report_refs": bp.get("report_refs", [])})
        if probs:
            notes.append(f"{sid}: still outside the rules after two rewrites: {'; '.join(probs)}. Rafael decides.")
        slots.append(row)
        total += box
    if not fun:
        slots.append({"slot": 9, "kind": "fun", "state": "bypass", "title": "no fun story today"})
    slots.append({"slot": 12, "kind": "ending", "state": "bypass", "title": "stored approved ending"})
    slots.sort(key=lambda r: r["slot"])
    core_count = sum(1 for r in slots if 2 <= r["slot"] <= 10 and r.get("state") != "bypass")
    pack = {"edition": ctx.edition.isoformat(), "date_title": ctx.title_date, "lane": ctx.lane,
            "prompt_file": "config/headlines_comfy_prompt.txt (Headlines_prompt_for_comfy_json, Rafael 26 Sep 2026)",
            "cues": cue_map, "rate_syllables_per_second": hcfg["syllables_per_second"], "floor_seconds": 0, "hold_seconds": 0,
            "slots": slots, "ending": hcfg["approved_ending"],
            "bigger_picture": {"state": "render", "category": "The Bigger Picture", "regenerate": True,
                               "script": next(r["script"] for r in slots if r["slot"] == 11)},
            "content_seconds_excluding_open_close": round(total, 2), "core_count": core_count,
            "card_story_ids": [d["event_id"] for d in sel["deck"] if d["kind"] == "story"],
            "card_teaser_story_ids": [t["event_id"] for t in teaser_card["items"]],
            "review_status": "PENDING Rafael's spoken-copy review (approvals/s12_headlines_select)",
            "source_check": "scripts derived from the Full Report items named per slot; meaning check results recorded per slot",
            "generation_authorized": False, "notes": notes}
    save_json(ctx.headlines_sup / f"headlines_{ctx.short}_pack.json", pack)
    md = [f"# Headlines_{ctx.short} — Selection and Script (not generated)", "",
          f"Edition {ctx.edition.isoformat()}. Source: the cards deck cards_{ctx.short}_selection.md, which comes from the Full Report. No new research. Stories keep deck order.",
          "Structure (Rafael, 25 Sep 2026): slots 2 to 8 seven news stories, 9 fun, 10 teaser, 11 The Bigger Picture; slot 1 stored intro, slot 12 approved ending.",
          f"Timing: seconds = syllables / {hcfg['syllables_per_second']}, two decimals, no rounding. Content excluding opening and ending: {total:.1f} s.",
          "Not generated, not QA-checked, not approved for publication.", ""]
    for r in slots:
        if r.get("state") == "bypass":
            md += [f"## Slot {r['slot']} — {r['kind']}: {r['title']}", ""]
            continue
        md += [f"## Slot {r['slot']} — {r['category']}" + (f" (item {r['item']})" if r.get("item") else ""),
               f"Script: \"{r['script']}\"", f"Syllables: {r['syllables']}. Box: {r['box_seconds']:.2f} s. Symbol: {r['symbol']}"]
        if r.get("meaning_check"):
            md.append(f"Meaning check: {r['meaning_check']} {r.get('meaning_note', '')}")
        if r["problems"]:
            md.append("PROBLEMS: " + "; ".join(r["problems"]))
        md.append("")
    if notes:
        md += ["## Notes for Rafael", ""] + [f"- {n}" for n in notes] + [""]
    text = "\n".join(md)
    (ctx.headlines_sup / f"Headlines_{ctx.short}_selection.md").write_text(text, encoding="utf-8")
    gate = "PASS" if g["headlines_core_min"] <= core_count <= g["headlines_core_max"] else "FAIL"
    ctx.set_gate("headlines_selection_gate", gate, f"{core_count} core clips")
    update_checkpoint(ctx, {"headlines_core_count": core_count}, {"headlines_selection_gate": gate})
    ctx.report_append("s12 headlines select", f"{core_count} core clips, {total:.1f} s content; {len(notes)} notes. LLM so far: {llm.summary()}")
    if gate == "FAIL":
        ctx.set_stage("s12_headlines_select", "failed", core=core_count)
        return 2
    if not require_approval(ctx, "s12_headlines_select", "spoken-copy review before the Comfy JSON is built", text):
        ctx.set_stage("s12_headlines_select", "awaiting_approval", core=core_count)
        return RC_APPROVAL
    pack["review_status"] = "Approved by Rafael (approvals/s12_headlines_select.approved)"
    save_json(ctx.headlines_sup / f"headlines_{ctx.short}_pack.json", pack)
    ctx.set_stage("s12_headlines_select", "done", core=core_count, seconds=round(total, 1))
    return 0


if __name__ == "__main__":
    stage_main(run, __doc__)
```

## v1_workflow/stages/s13_headlines_fill.py

```python
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
from lib.syllables import box_seconds, count, word_syllables  # noqa: E402

AUDIT_RE = re.compile(r"[A-Za-z]+(?:['-][A-Za-z]+)*")


def syllable_audit(text: str) -> list[dict]:
    """Word list in the QA tool's tokenisation (vendor/validate_delivery.py), one syllable count per word."""
    return [{"word": w, "syllables": max(1, word_syllables(w.replace("'", "")))} for w in AUDIT_RE.findall(text)]


def cue_line(script: str, cues: dict) -> str:
    """15 Sep rule: a pronunciation cue line for brand names the script mentions, e.g. Anthropic -> an-thropic."""
    hits = [f'say "{real}" as "{cue}"' for real, cue in cues.items() if re.search(r"\b" + re.escape(real) + r"\b", script, re.I)]
    return ("\nPronunciation: " + "; ".join(hits) + ".") if hits else ""

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


def fill(wf: dict, pack: dict, prompt_tpl: str, template_sha: str, refs_verified: bool = False) -> tuple[dict, list[tuple], list[str]]:
    orig = cp.deepcopy(wf)
    qa_slots = []
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
            audit = syllable_audit(slot["script"])
            syl = sum(a["syllables"] for a in audit)
            box = box_seconds(syl, pack["rate_syllables_per_second"])
            prompt = prompt_tpl.replace("{symbol}", slot["symbol"].rstrip(".")).replace("{script}", slot["script"]) + cue_line(slot["script"], cues)
            intro = re.split(r"(?<=[.,:!?])\s", slot["script"], 1)[0]
            qa_slots.append({"slot": s, "kind": slot["kind"], "title": slot.get("category", slot["kind"]), "narration": slot["script"],
                             "generation_prompt": prompt, "intro": intro, "syllable_audit": audit, "estimated_syllables": syl,
                             "seconds": box, "story_id": slot.get("story_id"), "story_ids": slot.get("story_ids", []),
                             "symbol": slot.get("symbol"), "item": slot.get("item")})
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
    refs = [{"node_id": nid, "filename": nodes[nid]["widgets_values"][0], "visually_verified": refs_verified, "role": role}
            for nid, role in ((6, "boundary_hands_on_table"), (7, "secondary_gesture")) if nid in nodes]
    wf["extra"]["aind_headlines"] = {  # schema of vendor/validate_delivery.py validate_headlines()
        "edition": pack["edition"], "date_title": pack["date_title"], "lane": lane, "timing_decision_confirmed": True,
        "syllables_per_second": pack["rate_syllables_per_second"], "timing_formula": "syllables / 4.4",
        "boundary_hold_duration_is_flexible": True, "unresolved_issues": [], "references": refs,
        "slots": qa_slots, "card_story_ids": pack.get("card_story_ids", []), "card_teaser_story_ids": pack.get("card_teaser_story_ids", []),
        "review_status": pack["review_status"], "generation_authorized": bool(pack.get("generation_authorized"))}
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
            assert nodes[base + 13]["widgets_values"][0] == round(sum(a["syllables"] for a in syllable_audit(row["script"])) / pack["rate_syllables_per_second"], 2)
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
        wf, table, checks = fill(wf, pack, PROMPT_FILE.read_text(encoding="utf-8"), template_sha,
                                 bool(ctx.config["headlines"].get("reference_images_visually_verified")))
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
```

## v1_workflow/stages/s14_validate.py

```python
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
```

## v1_workflow/stages/s15_comfy.py

```python
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
```

## v1_workflow/stages/s16_stitch.py

```python
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
```

## v1_workflow/stages/s17_store.py

```python
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
```

## v1_workflow/vendor/README.md

```markdown
# vendor

`validate_delivery.py` is a verbatim copy (plus a four-line provenance header) of the ChatGPT-lane QA tool
`AIMD_LV1_Adverts_Automation_Skill_V1_validate_delivery.py` from Drive, mirrored 27 September 2026.
It validates a filled Headlines workflow JSON (`--headlines`), a clip inventory (`--clips-dir`) and a Drive
storage manifest (`--manifest --inventory`). The Drive file is the authority; re-copy it when it changes.
```

## v1_workflow/vendor/validate_delivery.py

```python
# VENDORED COPY. Origin: Google Drive, AI_News_Desk / Blueprint_Library, file
# "AIMD_LV1_Adverts_Automation_Skill_V1_validate_delivery.py" (ChatGPT lane QA tool, 26 Sep 2026 state),
# mirrored 27 Sep 2026 by the Claude lane into v1_workflow/vendor. Unchanged apart from this header.
# s14_validate.py calls it as a subprocess; the Drive file stays the authority. Re-copy when Drive changes.

"""Validate AIND's product folders and the exact current card delivery, without publishing."""
import argparse, hashlib, json, struct, math, re, urllib.request
from pathlib import Path
from datetime import date

def validate(manifest, inventory, cards_dir=None):
    cards = manifest['products']['cards']
    entries = cards['ordered_files']
    assert len(entries) == 15, 'Current card set must contain exactly 15 cards'
    assert len({x['id'] for x in entries}) == 15, 'Duplicate card IDs'
    assert cards['format'] == [1080, 1920], 'Unexpected card format'
    assert [x['order'] for x in entries] == list(range(1, 16)), 'Invalid card order'
    lane = cards.get('producing_lane')
    assert lane in ('VL1', 'VL2'), 'Record the actual producing workflow lane'
    edition = date.fromisoformat(manifest['edition'])
    short_date = f'{edition.day}-{edition.month}-{edition.year % 100:02d}'
    for entry in entries:
        expected_name = f"cards_{short_date}_I{entry['order']:02d}_{lane}.png"
        assert entry['name'] == expected_name, 'Incorrect card filename order, lane or extra version suffix'
    combined = cards['combined_image']
    assert combined['id'] not in {x['id'] for x in entries}, 'Combined image is not a carousel card'
    children = inventory[cards['folder_id']]
    files = [x for x in children if x['file_or_folder'] != 'folder']
    assert {x['id'] for x in files} == {x['id'] for x in entries} | {combined['id']}, 'Extra/missing current card output'
    expected = {x['id']: x for x in entries + [combined]}
    for actual in files:
        item = expected[actual['id']]
        assert actual['title'] == item['name'], 'Filename changed'
        assert int(actual['size']) == item['bytes'], 'Remote size mismatch'
    root = inventory[manifest['daily_folder']['id']]
    assert {x['id'] for x in root if x['file_or_folder'] == 'folder'} == {p['folder_id'] for p in manifest['products'].values()}, 'Unexpected date-root folder'
    assert {x['id'] for x in root if x['file_or_folder'] != 'folder'} == {manifest['manifest_id']}, 'Loose files in date root'
    actual_files = [f for children in inventory.values() for f in children if f['file_or_folder'] != 'folder']
    assert len(actual_files) == len({f['id'] for f in actual_files}), 'Duplicate file identities in delivery tree'
    recorded = manifest['files'] + manifest['source_documents']
    assert {f['id'] for f in actual_files} == {f['id'] for f in recorded} | {manifest['manifest_id']}, 'Unrecorded or missing file'
    for item in recorded:
        matches = [f for f in inventory[item['parent_id']] if f['id'] == item['id']]
        assert len(matches) == 1, 'Wrong parent for ' + item.get('name', item.get('title', item['id']))
        assert matches[0]['title'] == item.get('name', item.get('title')), 'Recorded filename mismatch'
        if item.get('bytes') is not None and matches[0].get('size') is not None:
            assert int(matches[0]['size']) == item['bytes'], 'Recorded byte-size mismatch'
    if cards_dir:
        for item in entries + [combined]:
            data = (Path(cards_dir) / item['name']).read_bytes()
            assert hashlib.sha256(data).hexdigest() == item['sha256'], 'Local card bytes changed'
            if item in entries:
                assert data[:8] == b'\x89PNG\r\n\x1a\n', 'Not a PNG'
                assert list(struct.unpack('>II', data[16:24])) == [1080, 1920], 'Wrong PNG dimensions'
    return {'storage_validation': 'PASS', 'current_cards': 15, 'combined_images': 1,
            'publication_status': cards['publication_status'], 'publication_approval_inferred': False}

def headlines_seconds(syllables):
    """Headlines_Master_Rules_Structure.txt Section B item 1a: seconds = syllables / 4.4, written to two decimals.

    No rounding up to a half second and no added time (Rafael, 25 Sep 2026).
    Pose holds are flexible instructions and never additional duration inputs.
    """
    if type(syllables) is not int or syllables <= 0:
        raise ValueError('Syllable count must be a positive integer')
    return round(syllables / 4.4, 2)


def blueprint_prompt(prompt_text):
    """Headlines_prompt_for_comfy_json.txt (folder Headlines_prompt_for_comfy_json): the only copy of the generation prompt."""
    b2 = prompt_text.strip()
    if b2.count('<article content>') != 2 or '"<article content>"' not in b2:
        raise ValueError('The prompt file must hold exactly two <article content> placeholders, the second one quoted')
    return b2


def validate_headlines(workflow, schema=None, b2=None):
    """Check a reviewed Headlines build; never queue, rewrite, or approve media."""
    errors = []
    def require(condition, message):
        if not condition:
            errors.append(message)
    nodes = {n['id']: n for n in workflow['nodes']}
    pack = workflow.get('extra', {}).get('aind_headlines')
    if not pack:
        raise ValueError('Missing single-source Headlines pack: extra.aind_headlines')
    # Check the current submission graph, never historical attempt snapshots.
    run = workflow.get('extra', {}).get('aind_run', {})
    current_api = run.get('api_graph', {})
    if 'api_graph' in run:
        require(isinstance(current_api, dict) and bool(current_api), 'Current API graph is empty or invalid')
    if not isinstance(current_api, dict):
        current_api = {}
    def require_api_value(nid, key, expected):
        api_node = current_api.get(str(nid), {})
        inputs = api_node.get('inputs', {}) if isinstance(api_node, dict) else {}
        require(isinstance(inputs, dict) and key in inputs and inputs[key] == expected,
                f'Node {nid}: current API {key} differs from executable UI')
    for nid, key, index in ((6, 'image', 0), (7, 'image', 0), (8, 'audio', 0),
                            (9, 'noise_seed', 0), (10, 'sampler_name', 0),
                            (11, 'scheduler', 0), (11, 'steps', 1), (11, 'denoise', 2),
                            (26, 'noise_seed', 0)):
        if str(nid) in current_api:
            require_api_value(nid, key, nodes[nid]['widgets_values'][index])
    require(len(nodes) == len(workflow['nodes']), 'Duplicate node IDs')
    require(pack.get('edition') is not None, 'Missing edition')
    require(pack.get('timing_decision_confirmed') is True, 'Missing acknowledged boundary rule')
    rate = pack.get('syllables_per_second')
    require(rate == 4.4, 'Timing must use 4.4 syllables/second')
    require(pack.get('timing_formula') == 'syllables / 4.4', 'Rules file Section B item 1a timing formula missing or changed')
    require(pack.get('boundary_hold_duration_is_flexible') is True, 'Boundary pose must not impose exact hold deadlines')
    require(not pack.get('unresolved_issues'), 'Unresolved build issues remain')
    require(nodes[11]['widgets_values'] == ['simple', 6, 1], 'Incorrect base scheduler')
    require(nodes[11]['widgets_values_named'].get('steps') == 6, 'Hidden steps differ')
    require(nodes[9]['widgets_values'][0] == 1060749754396562, 'Anchor seed changed')
    require(nodes[26]['widgets_values'][0] == 1060749754396562, 'Upscale seed changed')
    require(nodes[2]['widgets_values'][1] == 1, 'LoRA strength changed')
    require(nodes[10]['widgets_values'][0] == 'euler', 'Base sampler changed')
    require(nodes[22]['mode'] == 4, 'SigmaShift must remain bypassed')
    require(nodes[29]['widgets_values'][1:3] == [1088, 1920], 'Upscale size changed')
    expected_refs = pack.get('references', [])
    require(len(expected_refs) == 2, 'Exactly two reviewed image references required')
    for ref in expected_refs:
        node = nodes[ref['node_id']]
        require(node['widgets_values'][0] == ref['filename'], 'Reference filename mismatch')
        require(node['widgets_values_named'].get('image') == ref['filename'], 'Hidden reference mismatch')
        require(ref.get('visually_verified') is True, 'Reference pose has not been visually reviewed')
    if expected_refs:
        require(expected_refs[0].get('role') == 'boundary_hands_on_table', 'Picture 1 must define settled hands-on-table pose')
        require(expected_refs[-1].get('role') == 'secondary_gesture', 'Picture 2 must be the reviewed secondary pose')
    links = {link[0]: link for link in workflow['links']}
    require(len(links) == len(workflow['links']), 'Duplicate link IDs')
    for link in workflow['links']:
        lid, source, output, target, inp, _ = link
        require(source in nodes and target in nodes, 'Broken graph endpoint')
        if source in nodes and target in nodes:
            require(output < len(nodes[source].get('outputs', [])), 'Broken output slot')
            require(inp < len(nodes[target].get('inputs', [])), 'Broken input slot')
            if inp < len(nodes[target].get('inputs', [])):
                require(nodes[target]['inputs'][inp].get('link') == lid, 'Input/link disagreement')
            if output < len(nodes[source].get('outputs', [])):
                require(lid in (nodes[source]['outputs'][output].get('links') or []), 'Output/link disagreement')
    slots = pack.get('slots', [])
    active = {row['slot'] for row in slots}
    require(len(active) == len(slots), 'Duplicate story slots')
    require(active.issubset(set(range(2, 12))), 'Unexpected generated slot')
    table = []
    for row in slots:
        slot = row['slot']; base = slot * 100
        prompt = nodes[base + 12]['widgets_values'][0]
        seconds = nodes[base + 13]['widgets_values'][0]
        speech = row['narration']
        require(row.get('generation_prompt') == prompt, f'Slot {slot}: pack prompt differs from executable prompt')
        # A base-only or single-clip API graph is valid; check every included clip.
        if any(str(base + part) in current_api for part in (12, 13, 17, 21, 35)):
            require_api_value(base + 12, 'value', prompt)
            require_api_value(base + 13, 'value', seconds)
        for brand, cue in (('Anthropic', 'an-thropic'), ('NVIDIA', 'N-vidia')):
            spoken = re.search(r'\b' + re.escape(brand) + r'\b', speech, re.IGNORECASE) is not None
            has_cue = re.search(r'\b' + re.escape(cue) + r'\b', prompt, re.IGNORECASE) is not None
            require(not has_cue or spoken, f'Slot {slot}: unused pronunciation cue for {brand}')
            require(not spoken or has_cue, f'Slot {slot}: missing approved pronunciation cue for {brand}')
        intro = row.get('intro', '')
        require(bool(intro) and speech.startswith(intro), f'Slot {slot}: spoken introduction missing')
        require('"' + speech + '"' in prompt, f'Slot {slot}: narration differs from pack')
        audit = row.get('syllable_audit', [])
        tokens = re.findall(r"[A-Za-z]+(?:['-][A-Za-z]+)*", speech)
        require([x['word'] for x in audit] == tokens, f'Slot {slot}: syllable audit omits/changes words')
        require(all(type(x.get('syllables')) is int and x['syllables'] > 0 for x in audit), f'Slot {slot}: invalid syllables')
        count = sum(x['syllables'] for x in audit)
        require(count == row.get('estimated_syllables'), f'Slot {slot}: syllable total mismatch')
        if count > 0:
            expected = headlines_seconds(count)
            require(seconds == expected == row.get('seconds'), f'Slot {slot}: duration differs from established formula for the complete narration')
        require(nodes[base + 12].get('widgets_values_named', {}).get('value') == prompt, f'Slot {slot}: hidden prompt mismatch')
        require(nodes[base + 13].get('widgets_values_named', {}).get('value') == seconds, f'Slot {slot}: hidden duration mismatch')
        for part in (21, 35):
            save = nodes[base + part]
            require(save['widgets_values'][0] == save.get('widgets_values_named', {}).get('filename_prefix'), f'Slot {slot}: hidden output mismatch')
            if str(base + part) in current_api:
                require_api_value(base + part, 'filename_prefix', save['widgets_values'][0])
        require(nodes[base + 15]['widgets_values'][1:3] == [544, 960], f'Slot {slot}: base size changed')
        require(nodes[base + 21]['mode'] == 0, f'Slot {slot}: base output inactive')
        require(nodes[base + 35]['mode'] == 0, f'Slot {slot}: upscale output must be on (rules file, Rafael 25 Sep 2026)')
        if b2 is not None:
            # The prompt must be Headlines_prompt_for_comfy_json.txt with only its two placeholders filled (plus an optional cue line).
            head_b2, rest = b2.split('<article content>', 1)
            mid_b2, tail_b2 = rest.split('"<article content>"', 1)
            require(prompt.startswith(head_b2) and mid_b2 in prompt and ('"' + speech + '"' + tail_b2) in prompt,
                    f'Slot {slot}: prompt is not Headlines_prompt_for_comfy_json.txt')
        require('guaranteed identical' not in prompt.lower(), f'Slot {slot}: unsupported endpoint guarantee')
        table.append({'slot': slot, 'syllables': count, 'seconds': seconds, 'title': row['title']})
    spectrum = [n for n in nodes.values() if n.get('type') == 'SpectrumApplyMiniMaxH3']
    require(len(spectrum) == 1 and spectrum[0]['mode'] == 0, 'SpectrumApplyMiniMaxH3 node missing or not on')
    for row in slots:
        guider = nodes.get(row['slot'] * 100 + 16, {})
        model_in = [i.get('link') for i in guider.get('inputs', []) if i.get('name') == 'model']
        require(bool(spectrum) and model_in and model_in[0] in (spectrum[0]['outputs'][0].get('links') or []),
                f"Slot {row['slot']}: guider model does not come from the Spectrum node")
    for slot in set(range(1, 13)) - active:
        require(all(n['mode'] == 4 for n in nodes.values() if n['id'] // 100 == slot), f'Slot {slot}: inactive branch not bypassed')
    story_ids = {x.get('story_id') for x in slots if x.get('kind') == 'story'}
    for row in slots:
        if row.get('kind') == 'teaser':
            ids = set(row.get('story_ids', []))
            require(ids.issubset(set(pack.get('card_teaser_story_ids', []))), 'Teaser contains non-teaser card items')
            require(not ids.intersection(story_ids | set(pack.get('card_story_ids', []))), 'Teaser repeats story/card items')
    if schema is not None:
        for nid, key in ((1, 'unet_name'), (2, 'lora_name'), (3, 'clip_name'), (4, 'vae_name'), (5, 'vae_name'), (6, 'image'), (7, 'image'), (8, 'audio'), (29, 'model_name')):
            node = nodes[nid]
            definition = schema.get(node['type'], {}).get('input', {}).get('required', {}).get(key)
            choices = None
            if definition:
                choices = definition[0] if isinstance(definition[0], list) else definition[1].get('options')
            require(choices is not None and node['widgets_values'][0] in choices, f'Node {nid}: required file absent from live backend')
    if errors:
        raise ValueError('\n'.join(errors))
    return {'headlines_json': 'PASS', 'live_assets': 'PASS' if schema is not None else 'UNVERIFIED',
            'slots': table, 'content_box_seconds': sum(x['seconds'] for x in table),
            'rendered_speech_and_picture': 'NOT_TESTED', 'generation_authorized': False}



def check_headlines_clips(workflow, clips_dir, ffprobe='ffprobe', ffmpeg='ffmpeg'):
    """Read-only media inventory from enabled save nodes in the supplied workflow.
    Caller resolves the current Drive workflow/rules first and obtains permission
    for this particular local output directory. No history, queue or JSON writes.
    """
    import subprocess
    from pathlib import PurePosixPath
    root = Path(clips_dir).resolve(strict=True)
    if not root.is_dir():
        raise ValueError('--clips-dir must be an existing directory')
    nodes = workflow.get('nodes', [])
    if len({n['id'] for n in nodes}) != len(nodes):
        raise ValueError('Duplicate workflow node IDs')
    expected = []
    prefix_keys = set()
    for node in nodes:
        nid = node.get('id')
        if type(nid) is not int or not 1 <= nid // 100 <= 12:
            continue
        part = nid % 100
        if part not in (21, 35) or node.get('mode', 0) != 0:
            continue
        values = node.get('widgets_values', [])
        prefix = values[0] if values else None
        if not isinstance(prefix, str) or not prefix.strip():
            raise ValueError(f'Enabled save node {nid} has no filename prefix')
        named = node.get('widgets_values_named', {})
        if 'filename_prefix' in named and named['filename_prefix'] != prefix:
            raise ValueError(f'Save node {nid}: visible and hidden prefixes disagree')
        rel = PurePosixPath(prefix.replace('\\', '/'))
        if rel.is_absolute() or '..' in rel.parts or ':' in prefix:
            raise ValueError(f'Save node {nid}: prefix must stay inside the approved output directory')
        key = str(rel).casefold()
        if key in prefix_keys:
            raise ValueError(f'Duplicate enabled output prefix: {prefix}')
        prefix_keys.add(key)
        dims = [544, 960] if part == 21 else [1088, 1920]
        expected.append({'clip_id': f'C{nid // 100:02d}', 'node_id': nid,
                         'resolution': dims, 'filename_prefix': prefix,
                         'relative_prefix': rel})
    if not expected:
        raise ValueError('No enabled Headlines save nodes found; expected nodes ending in 21/35')
    report = []
    inspected = {}
    for item in sorted(expected, key=lambda x: x['node_id']):
        rel = item.pop('relative_prefix')
        folder = root.joinpath(*rel.parts[:-1]).resolve()
        try:
            folder.relative_to(root)
        except ValueError:
            raise ValueError('Output prefix resolves outside the approved output directory')
        matcher = re.compile(re.escape(rel.name) + r'(?:_[0-9]+_?)?\.mp4$', re.IGNORECASE)
        candidates = sorted((f for f in folder.iterdir() if f.is_file() and matcher.fullmatch(f.name)),
                            key=lambda f: f.name) if folder.is_dir() else []
        results = []
        for path in candidates:
            resolved = path.resolve()
            try:
                resolved.relative_to(root)
            except ValueError:
                raise ValueError('Output file resolves outside the approved output directory')
            if resolved not in inspected:
                result = {'path': str(path), 'bytes': path.stat().st_size}
                try:
                    if result['bytes'] <= 48:
                        raise ValueError('Empty or incomplete file (48 bytes or smaller)')
                    probe = subprocess.run(
                        [ffprobe, '-v', 'error', '-show_streams', '-show_format', '-of', 'json', str(path)],
                        capture_output=True, text=True, check=False)
                    if probe.returncode != 0:
                        raise ValueError('ffprobe failed: ' + probe.stderr.strip()[:600])
                    metadata = json.loads(probe.stdout)
                    video = next((s for s in metadata.get('streams', []) if s.get('codec_type') == 'video'), None)
                    audio = [s for s in metadata.get('streams', []) if s.get('codec_type') == 'audio']
                    if not video:
                        raise ValueError('No video stream')
                    result['resolution'] = [video.get('width'), video.get('height')]
                    result['duration_seconds'] = float(video.get('duration') or metadata.get('format', {}).get('duration') or 0)
                    if result['duration_seconds'] <= 0:
                        raise ValueError('No positive video duration')
                    if not audio:
                        raise ValueError('No audio stream in generated speech clip')
                    decode = subprocess.run(
                        [ffmpeg, '-nostdin', '-v', 'error', '-xerror', '-i', str(path),
                         '-map', '0:v:0', '-map', '0:a:0', '-f', 'null', '-'],
                        capture_output=True, text=True, check=False)
                    if decode.returncode != 0 or decode.stderr.strip():
                        raise ValueError('Full decode failed: ' + decode.stderr.strip()[:600])
                    digest = hashlib.sha256()
                    with path.open('rb') as stream:
                        for block in iter(lambda: stream.read(1024 * 1024), b''):
                            digest.update(block)
                    result['sha256'] = digest.hexdigest()
                    result['full_decode'] = 'PASS'
                except (ValueError, OSError) as exc:
                    result['error'] = str(exc)
                    result['full_decode'] = 'FAIL'
                inspected[resolved] = result
            result = dict(inspected[resolved])
            if not result.get('error') and result.get('resolution') != item['resolution']:
                result['error'] = 'Decoded resolution differs from this enabled output'
            result['usable_media'] = not bool(result.get('error'))
            results.append(result)
        valid = [r for r in results if r['usable_media']]
        item['status'] = ('AVAILABLE' if len(valid) == 1 else 'AMBIGUOUS' if len(valid) > 1
                          else 'INVALID' if candidates else 'MISSING')
        item['candidates'] = results
        report.append(item)
    return {
        'clip_inventory': 'PASS' if all(x['status'] == 'AVAILABLE' for x in report) else 'INCOMPLETE',
        'expected_outputs': len(report),
        'expected_clip_ids': sorted({x['clip_id'] for x in report}),
        'available_outputs': sum(x['status'] == 'AVAILABLE' for x in report),
        'missing': [x['clip_id'] + ':' + str(x['resolution'][0]) for x in report if x['status'] == 'MISSING'],
        'invalid': [x['clip_id'] + ':' + str(x['resolution'][0]) for x in report if x['status'] == 'INVALID'],
        'ambiguous': [x['clip_id'] + ':' + str(x['resolution'][0]) for x in report if x['status'] == 'AMBIGUOUS'],
        'outputs': report,
        'scope': 'Enabled outputs only; unrelated files cannot satisfy a missing expected output',
        'story_identity_and_generation_provenance': 'UNVERIFIED - compare existing source manifest and generation record',
        'rendered_speech_and_lip_sync': 'NOT_TESTED',
        'files_written': 0, 'generation_queued': False
    }


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--manifest')
    p.add_argument('--inventory', help='Fresh recursive Drive folder listing keyed by folder ID')
    p.add_argument('--cards-dir')
    p.add_argument('--headlines', help='Read-only Headlines workflow validation')
    p.add_argument('--prompt', help='Local copy of Headlines_prompt_for_comfy_json.txt (prompt check)')
    p.add_argument('--comfy-url', help='Existing local ComfyUI backend for asset/schema checks')
    p.add_argument('--clips-dir', help='Read only the explicitly approved output directory; compare enabled workflow outputs')
    p.add_argument('--ffprobe', default='ffprobe', help='Existing ffprobe executable')
    p.add_argument('--ffmpeg', default='ffmpeg', help='Existing ffmpeg executable')
    args = p.parse_args()
    if args.clips_dir and not args.headlines:
        p.error('--clips-dir requires the current --headlines workflow')
    if args.clips_dir:
        try:
            workflow = json.loads(Path(args.headlines).read_text(encoding='utf-8-sig'))
            result = check_headlines_clips(workflow, args.clips_dir, args.ffprobe, args.ffmpeg)
            print(json.dumps(result, indent=2))
        except (ValueError, KeyError, TypeError, OSError) as exc:
            p.exit(1, 'Clip inventory FAILED: ' + str(exc) + '\n')
        raise SystemExit(0 if result['clip_inventory'] == 'PASS' else 1)
    if args.headlines:
        schema = None
        if args.comfy_url:
            if not re.fullmatch(r'http://(?:127\.0\.0\.1|localhost):[0-9]+', args.comfy_url.rstrip('/')):
                p.error('--comfy-url must identify the local backend')
            with urllib.request.urlopen(args.comfy_url.rstrip('/') + '/object_info', timeout=20) as response:
                schema = json.load(response)
        try:
            print(json.dumps(validate_headlines(json.loads(Path(args.headlines).read_text(encoding='utf-8-sig')), schema,
                                                blueprint_prompt(Path(args.prompt).read_text(encoding='utf-8-sig')) if args.prompt else None), indent=2))
        except (ValueError, KeyError, TypeError) as exc:
            p.exit(1, 'Headlines validation FAILED: ' + str(exc) + '\n')
        raise SystemExit(0)
    if not args.manifest or not args.inventory:
        p.error('Use --headlines, or both --manifest and --inventory')
    print(json.dumps(validate(json.loads(Path(args.manifest).read_text(encoding='utf-8')),
                              json.loads(Path(args.inventory).read_text(encoding='utf-8')), args.cards_dir)))
```

## v1_workflow/tests/test_units.py

```python
"""Unit tests, standard library only:  python -m unittest tests.test_units -v"""
from __future__ import annotations

import datetime as dt
import json
import sys
import tempfile
import unittest
from pathlib import Path

PKG = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PKG))
from lib import syllables  # noqa: E402
from lib.common import RunContext, jaccard, load_json, norm_url, reporting_window, short_date, title_date, tokens  # noqa: E402
from stages import s05_gates, s09_cards_select, s13_headlines_fill, s16_stitch  # noqa: E402


def ctx_in(tmp: Path, **over) -> RunContext:
    cfg = load_json(PKG / "config" / "v1_config.json")
    cfg["local_root"] = str(tmp / "runs")
    cfg["history_root"] = str(tmp / "history")
    cfg.update(over)
    c = RunContext(dt.date(2026, 9, 27), cfg, llm_mode="dry")
    c.ensure_dirs()
    return c


class Syllables(unittest.TestCase):
    def test_formula(self):
        self.assertEqual(syllables.box_seconds(35), 7.95)
        self.assertEqual(syllables.box_seconds(37), 8.41)

    def test_known_lines(self):
        # Headlines_25-9-26_selection.md, counted by Rafael's script with its word list
        known = [("China's Xi told Trump the two countries should be partners, not rivals, and must keep AI under human control. He offered no specific rules.", 35),
                 ("Anthropic signed a nearly twelve billion dollar deal to rent computing power from cloud company Akamai, whose shares jumped about twenty percent.", 37),
                 ("Researchers showed that poisoned entries in a web form could hijack Salesforce's AI agents and steal customer data. Salesforce fixed the flaws.", 35),
                 ("Oracle may delay payments on its New Mexico AI data center, as the gas pipeline to power it slipped to twenty twenty-seven.", 36),
                 ("Waymo says its driverless cars, after two hundred seventy million miles, had eighty-two percent fewer injury crashes than humans.", 35)]
        for line, n in known:
            self.assertEqual(syllables.count(line), n, line)

    def test_audit_matches_count(self):
        line = "Anthropic signed a nearly twelve billion dollar deal with cloud company Akamai."
        self.assertEqual(sum(s for _, s in syllables.audit(line)), syllables.count(line))


class Dates(unittest.TestCase):
    def test_names(self):
        self.assertEqual(short_date(dt.date(2026, 9, 26)), "26-9-26")
        self.assertEqual(title_date(dt.date(2026, 9, 11)), "FRI 11 SEP 2026")

    def test_window(self):
        a, b = reporting_window(dt.date(2026, 9, 27), "Asia/Jerusalem", 9)
        self.assertEqual((b - a).total_seconds(), 86400)
        self.assertEqual(b.hour, 9)


class Text(unittest.TestCase):
    def test_norm_url(self):
        self.assertEqual(norm_url("https://www.Example.com/a/b/?utm_source=x&id=3#frag"), "https://example.com/a/b?id=3")

    def test_jaccard(self):
        self.assertGreaterEqual(jaccard(tokens("Halcyon releases frontier model"), tokens("Halcyon has released a frontier model")), 0.5)


class Gates(unittest.TestCase):
    def test_pool_gate_fails_closed(self):
        with tempfile.TemporaryDirectory() as d:
            ctx = ctx_in(Path(d))
            (ctx.work / "raw_pool.jsonl").write_text("".join(json.dumps({"id": f"R{i}", "window_check": "IN WINDOW"}) + "\n" for i in range(120)), encoding="utf-8")
            (ctx.work / "events.jsonl").write_text(json.dumps({"id": "E1", "disposition": "RETAINED EVENT ID", "headline": "x", "summary": ""}) + "\n", encoding="utf-8")
            cp, _ = s05_gates.compute(ctx, {})
            self.assertEqual(cp["stages"]["pool_gate_min_300"], "FAIL")
            self.assertEqual(cp["stages"]["source_fetch_gate"], "FAIL")
            self.assertEqual(cp["major_news_miss_gate"], "NOT RUN")
            self.assertEqual(s05_gates.run(ctx, []), 2)
            self.assertEqual(s05_gates.run(ctx, ["--override", "pool_gate_min_300=test", "--override", "source_fetch_gate=test", "--override", "major_news_miss_gate=test"]), 0)


def items(n=60):
    cats = ["POL", "MKT", "SEC", "ENE", "ROB", "MOD", "RES", "LAW", "HEA", "SOC", "FUN"]
    names = {"POL": "Politics and government of AI", "MKT": "Market, industry and finance", "SEC": "Security and cyber", "ENE": "Energy and infrastructure",
             "ROB": "Robotics", "MOD": "Models and tools", "RES": "Research and science", "LAW": "Ethics and law", "HEA": "Health",
             "SOC": "Society and education", "FUN": "Fun and humour"}
    out = []
    for i in range(1, n + 1):
        c = cats[i % 11]
        imp = 10 if i in (1, 2, 3) else 9 if i < 20 else 7 if i < 45 else 4
        if i in (1, 2):
            c = "MKT"
        out.append({"n": i, "id": f"EVT-{i}", "headline": f"Story {i} {c}", "label": "CRITICAL" if imp == 10 else "HIGH" if imp >= 8 else "MEDIUM" if imp >= 6 else "WATCHLIST",
                    "category": c, "category_name": names[c], "importance": imp, "summary": "s", "key_facts": ["f"], "verification": "REPORTED",
                    "source": "Src", "url": "https://x/1", "fun": c == "FUN", "big_name": i == 5})
    return out


class CardsSelect(unittest.TestCase):
    def test_deck_rules(self):
        with tempfile.TemporaryDirectory() as d:
            ctx = ctx_in(Path(d))
            notes = []
            chosen, teaser = s09_cards_select.select(ctx, items(), notes)
            self.assertEqual(len(chosen), 11)
            self.assertTrue(all(c["importance"] >= 10 for c in chosen[:3]) or chosen[0]["importance"] >= 10)
            self.assertEqual(chosen[-1]["category"], "FUN")
            self.assertLessEqual(sum(1 for c in chosen if c["category"] == "MKT"), 3)
            self.assertTrue(any(c["category"] == "ROB" for c in chosen))
            self.assertTrue(3 <= len(teaser) <= 4)
            self.assertFalse({t["id"] for t in teaser} & {c["id"] for c in chosen})
            order = [c["category"] for c in chosen if c["importance"] < 10 and c["category"] != "FUN" and not c["pick_reason"].startswith("big")]
            keys = ["POL", "MKT", "SEC", "ENE", "ROB", "MOD", "RES", "LAW", "HEA", "SOC"]
            self.assertEqual(order, sorted(order, key=keys.index))


class Fill(unittest.TestCase):
    def test_fill_synthetic_template(self):
        wf = json.loads((PKG / "tests" / "fixtures" / "template_synthetic.json").read_text(encoding="utf-8"))
        pack = {"edition": "2026-09-27", "date_title": "SUN 27 SEP 2026", "lane": "VL1", "cues": {"Anthropic": "an-thropic"},
                "rate_syllables_per_second": 4.4, "prompt_file": "x", "review_status": "Approved by Rafael (test)", "source_check": "test",
                "slots": [{"slot": 1, "kind": "intro", "state": "bypass", "title": "stored intro"},
                          {"slot": 2, "kind": "story", "category": "Politics", "story_id": "EVT-1", "symbol": "a gavel, simple text-free symbol",
                           "script": "In politics. Anthropic says the ban cost it billions of dollars this year."},
                          {"slot": 3, "kind": "teaser", "category": "Teaser", "story_ids": ["EVT-9"], "symbol": "logo",
                           "script": "Also in the full report: two more stories and a robot that folds laundry."}]
                         + [{"slot": s, "kind": "story", "state": "bypass", "title": "unused"} for s in range(4, 13)],
                "card_story_ids": ["EVT-1"], "card_teaser_story_ids": ["EVT-9"]}
        prompt = (PKG / "config" / "headlines_comfy_prompt.txt").read_text(encoding="utf-8")
        out, table, checks = s13_headlines_fill.fill(wf, pack, prompt, "sha", refs_verified=True)
        nodes = {n["id"]: n for n in out["nodes"]}
        self.assertEqual(nodes[213]["widgets_values"][0], round(syllables.count(pack["slots"][1]["script"]) / 4.4, 2))
        self.assertIn('"In politics. Anthropic says', nodes[212]["widgets_values"][0])
        self.assertIn("an-thropic", nodes[212]["widgets_values"][0])
        self.assertEqual(nodes[221]["widgets_values"][0], "video/headlines_27-9-26_C02_VL1_544")
        self.assertEqual(nodes[435]["mode"], 4)
        self.assertEqual(nodes[212]["mode"], 0)
        self.assertEqual(sum(1 for t in table if t[1] == "ACTIVE"), 2)
        self.assertTrue(any("mirror: all agree" in c for c in checks))
        qa = out["extra"]["aind_headlines"]
        self.assertEqual([s["slot"] for s in qa["slots"]], [2, 3])
        self.assertTrue(qa["slots"][0]["narration"].startswith(qa["slots"][0]["intro"]))


class Captions(unittest.TestCase):
    def test_events_inside_clip(self):
        ev = s16_stitch.caption_events("In robotics. A drone takes off from a robot arm, flies its patrol, and is caught by the arm on the way back.", 10.0, 8.0)
        self.assertTrue(ev)
        self.assertGreaterEqual(ev[0][0], 10.0)
        self.assertLessEqual(ev[-1][1], 18.0)
        for a, b, text in ev:
            self.assertLess(a, b)
            self.assertLessEqual(text.count("\\N"), 1)


if __name__ == "__main__":
    unittest.main()
```

## v1_workflow/tests/make_fixture.py

```python
"""Deterministic synthetic pool for the dry end-to-end test: ~330 items over the 55 registered sources, with
same-event duplicates across sources, a few out-of-window items, fun items and obvious 'critical' items.
Content is nonsense on purpose (house rule 6: never invent real news); it only exercises the code paths.

    python tests/make_fixture.py [--edition 2026-09-27] [--out tests/fixtures/pool_320.jsonl]
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import random
import zlib
import sys
import zoneinfo
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.common import load_json, SOURCES_PATH  # noqa: E402

ACTORS = {"POL": ["the European Commission", "the White House", "Britain's AI Safety Institute", "India's IT ministry", "the Pentagon"],
          "MKT": ["chipmaker Nervo", "cloud company Skyvault", "startup Quillbot Labs", "Orbital Semiconductor", "investment firm Pelican Capital"],
          "SEC": ["security firm Redshield", "researchers at Tallgrass University", "the cyber agency CERT-Nord", "Bluefin Bank", "vendor Lockstep"],
          "ENE": ["utility Northgrid", "data centre builder Kilnworks", "Solaris Power", "the grid operator Meshline", "Cobalt Energy"],
          "ROB": ["robot maker Ferrous Dynamics", "warehouse firm Cartwell", "drone company Skyhook", "Kestrel Robotics", "farm robot startup Sprout"],
          "MOD": ["model lab Halcyon", "the open source group Lattice", "assistant maker Pendant", "Vertex Labs", "toolmaker Quarry"],
          "RES": ["scientists at Meridian Institute", "a team at Coastal University", "the Alder Lab", "researchers at Pinegrove", "the Brightwater Observatory"],
          "LAW": ["a federal court in Ohio", "the Dutch data authority", "authors' group Inkwell", "the competition regulator", "a Tokyo district court"],
          "HEA": ["hospital group Larkspur Health", "the drug agency", "clinic chain Wellmark", "biotech Cellara", "a Boston hospital"],
          "SOC": ["the teachers' union Chalkline", "the city of Bremen", "newspaper The Daily Tide", "a Kenyan school network", "the film guild"],
          "FUN": ["a hobbyist in Leeds", "a cat named Turbo", "a village bakery", "a retired accountant", "a chess club in Lima"]}
DEEDS = {"POL": ["published new rules for AI in elections", "delayed the AI act deadline by six months", "signed an AI safety pact with twelve countries", "ordered agencies to list every AI system they use"],
         "MKT": ["raised three hundred million dollars at a four billion valuation", "reported quarterly AI revenue of two billion dollars", "bought a rival for one point two billion", "cut prices of its AI chips by thirty percent"],
         "SEC": ["found a flaw that lets chatbots leak customer records", "warned that AI written phishing rose eighty percent", "patched an agent that could be hijacked through a web form", "traced a data theft to a poisoned model file"],
         "ENE": ["switched on a two gigawatt data centre campus", "said AI demand will double power use by twenty thirty", "paused a data centre over water limits", "signed a deal for one gigawatt of solar for AI servers"],
         "ROB": ["showed a robot that folds laundry from one demonstration", "put two hundred humanoid robots to work in a car plant", "flew a drone that lands on a moving truck", "sold its first robot that picks strawberries at night"],
         "MOD": ["released a model that runs on a phone and beats last year's best", "opened its agent tool to every developer for free", "added a voice mode that speaks forty languages", "launched a coding assistant that fixes its own bugs"],
         "RES": ["used AI to predict a protein shape in one minute", "trained a model that spots earthquakes ten seconds earlier", "found AI can read ancient scrolls without unrolling them", "showed a model that solves olympiad geometry"],
         "LAW": ["ruled that AI output cannot be copyrighted", "fined a chatbot maker four million euros over data use", "sued a model lab over training on books", "ordered an AI company to delete a voice clone"],
         "HEA": ["approved an AI tool that reads chest scans", "found AI cut missed cancers by twenty percent in a trial", "started using AI to write discharge notes", "paused an AI triage tool after errors"],
         "SOC": ["banned AI homework helpers in exams", "gave every pupil an AI tutor", "found half of students use AI weekly", "warned that AI fake videos spread before a vote"],
         "FUN": ["taught an AI to bark at the mail carrier", "won a bake-off with an AI written recipe", "used a chatbot to name every pigeon in the square", "beat a robot at table tennis after nine tries"]}
CRITICAL = [("MOD", "model lab Halcyon", "released a frontier model that plans a week of work on its own, in a change that affects every office"),
            ("POL", "the White House", "signed an executive order that requires licences for every large AI model"),
            ("SEC", "the cyber agency CERT-Nord", "said an AI worm infected banks in nine countries overnight")]


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--edition", default="2026-09-27")
    p.add_argument("--out", default=str(Path(__file__).parent / "fixtures" / "pool_320.jsonl"))
    p.add_argument("--major", default=str(Path(__file__).parent / "fixtures" / "major_news_list.json"))
    a = p.parse_args()
    rnd = random.Random(20260927)
    edition = dt.date.fromisoformat(a.edition)
    tz = zoneinfo.ZoneInfo("Asia/Jerusalem")
    end = dt.datetime(edition.year, edition.month, edition.day, 9, 0, tzinfo=tz)
    sources = load_json(SOURCES_PATH)["sources"] if isinstance(load_json(SOURCES_PATH), dict) else load_json(SOURCES_PATH)
    rows, events, n = [], [], 0
    by_cat: dict[str, list] = {}
    for s in sources:
        by_cat.setdefault(s.get("category", "MOD"), []).append(s)
    # critical events, each reported by three sources in the category and one elsewhere
    for k, (cat, actor, deed) in enumerate(CRITICAL):
        title = f"{actor[0].upper() + actor[1:]} {deed}"
        events.append({"cat": cat, "title": title, "actor": actor, "deed": deed, "n_sources": 4, "crit": True})
    for cat, srcs in by_cat.items():
        for i in range(9):
            actor = rnd.choice(ACTORS.get(cat, ACTORS["MOD"]))
            deed = rnd.choice(DEEDS.get(cat, DEEDS["MOD"]))
            detail = rnd.choice(["in Berlin", "for hospitals", "after a two year test", "with a rival", "in a court filing", "at its annual event",
                                 "for farmers", "across Asia", "with government money", "despite protests", "for the first time", "in a leaked memo"])
            title = f"{actor[0].upper() + actor[1:]} {deed} {detail} ({cat.lower()} {i})"
            events.append({"cat": cat, "title": title, "actor": actor, "deed": deed, "n_sources": 1 + (1 if i % 3 == 0 else 0) + (1 if i % 5 == 0 else 0), "crit": False})
    for e in events:
        pool = by_cat.get(e["cat"], sources)
        picked = rnd.sample(pool, min(e["n_sources"], len(pool)))
        if e["n_sources"] > len(pool):
            picked += rnd.sample(sources, e["n_sources"] - len(pool))
        for j, src in enumerate(picked):
            n += 1
            hours = rnd.uniform(0.5, 23.5)
            pub = end - dt.timedelta(hours=hours)
            variant = e["title"] if j == 0 else e["title"].replace(" (", ", sources say (") if j == 1 else e["title"].replace(e["actor"][0].upper() + e["actor"][1:], e["actor"][0].upper() + e["actor"][1:] + " has", 1)
            text = (f"{variant}. The announcement came on {pub.strftime('%d %B')} and named {e['actor']} as the actor. "
                    f"Officials said the number involved was {rnd.choice(['two hundred', 'fifty', 'one thousand', 'twelve'])} and that more details follow next week. "
                    f"Critics questioned the timing.")
            rows.append({"source_id": src["id"], "title": variant, "link": f"https://{src['url'].split('/')[2]}/story/{n}-{zlib.crc32(e['title'].encode()) % 100000}",
                         "published": pub.isoformat(), "summary": text[:200], "text": text, "fun": e["cat"] == "FUN"})
    # filler: unique minor items so every source has items and the pool passes 300
    while len(rows) < 330:
        src = rnd.choice(sources)
        cat = src.get("category", "MOD")
        n += 1
        actor = rnd.choice(ACTORS.get(cat, ACTORS["MOD"]))
        deed = rnd.choice(DEEDS.get(cat, DEEDS["MOD"]))
        pub = end - dt.timedelta(hours=rnd.uniform(0.5, 23.5))
        title = f"{actor[0].upper() + actor[1:]} {deed} in a smaller update {n}"
        text = f"{title}. A short note published on {pub.strftime('%d %B')} with a figure of {rnd.randint(2, 90)} percent. It is a minor item."
        rows.append({"source_id": src["id"], "title": title, "link": f"https://{src['url'].split('/')[2]}/note/{n}", "published": pub.isoformat(),
                     "summary": text[:160], "text": text, "fun": cat == "FUN"})
    # out-of-window items
    for i in range(12):
        src = rnd.choice(sources)
        n += 1
        pub = end - dt.timedelta(days=rnd.randint(2, 9))
        rows.append({"source_id": src["id"], "title": f"Old item {n} about AI from last week", "link": f"https://{src['url'].split('/')[2]}/old/{n}",
                     "published": pub.isoformat(), "summary": "old", "text": "Old item, outside the window.", "fun": False})
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    major = [{"title": e["title"], "url": "", "date": edition.isoformat()} for e in events[:3]] + [{"title": events[10]["title"], "url": "", "date": edition.isoformat()}]
    Path(a.major).write_text(json.dumps(major, indent=1), encoding="utf-8")
    print(f"wrote {len(rows)} rows to {out} ({len(events)} events, {sum(1 for r in rows if r['title'].startswith('Old'))} out of window); major list {len(major)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

## v1_workflow/tests/make_template.py

```python
"""Synthetic ComfyUI master template with the node-id pattern of the real one (slot k owns 100k..100k+99; script +12,
seconds +13, base save +21, upscale save +35) and every field the QA tool (vendor/validate_delivery.py) inspects.
It is NOT the production template (Drive ID 1iGUq1LtGtVm1toPhDTqhWOC4qIjIe2xV); it only lets s13 and s14 run here.

    python tests/make_template.py [--out tests/fixtures/template_synthetic.json]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SEED = 1060749754396562


def node(nid, typ, widgets=None, named=None, inputs=None, outputs=None, mode=0, title=None):
    return {"id": nid, "type": typ, "title": title or typ, "mode": mode, "pos": [0, 0], "size": [200, 100],
            "inputs": inputs or [], "outputs": outputs or [], "widgets_values": widgets or [],
            **({"widgets_values_named": named} if named is not None else {})}


def build() -> dict:
    nodes, links = [], []
    lid = [0]

    def link(src, src_slot, dst, dst_slot, typ="*"):
        lid[0] += 1
        links.append([lid[0], src, src_slot, dst, dst_slot, typ])
        return lid[0]

    def out(names):
        return [{"name": n, "type": n, "links": []} for n in names]

    def inp(names):
        return [{"name": n, "type": n, "link": None} for n in names]

    nodes += [node(1, "UNETLoader", ["minimax_h3.safetensors", "default"], {"unet_name": "minimax_h3.safetensors", "weight_dtype": "default"}, outputs=out(["MODEL"])),
              node(2, "LoraLoaderModelOnly", ["h3_turbo.safetensors", 1], {"lora_name": "h3_turbo.safetensors", "strength_model": 1}, inputs=inp(["model"]), outputs=out(["MODEL"])),
              node(3, "CLIPLoader", ["clip.safetensors", "minimax"], {"clip_name": "clip.safetensors", "type": "minimax"}, outputs=out(["CLIP"])),
              node(4, "VAELoader", ["vae.safetensors"], {"vae_name": "vae.safetensors"}, outputs=out(["VAE"])),
              node(5, "VAELoader", ["vae_audio.safetensors"], {"vae_name": "vae_audio.safetensors"}, outputs=out(["VAE"])),
              node(6, "LoadImage", ["ref01_hands_on_table.png", "image"], {"image": "ref01_hands_on_table.png", "upload": "image"}, outputs=out(["IMAGE", "MASK"])),
              node(7, "LoadImage", ["ref01_hands_on_table.png", "image"], {"image": "ref01_hands_on_table.png", "upload": "image"}, outputs=out(["IMAGE", "MASK"])),
              node(8, "LoadAudio", ["voice_sample.wav", None, None], {"audio": "voice_sample.wav"}, outputs=out(["AUDIO"])),
              node(9, "RandomNoise", [SEED, "fixed"], {"noise_seed": SEED}, outputs=out(["NOISE"])),
              node(10, "KSamplerSelect", ["euler"], {"sampler_name": "euler"}, outputs=out(["SAMPLER"])),
              node(11, "BasicScheduler", ["simple", 6, 1], {"scheduler": "simple", "steps": 6, "denoise": 1}, inputs=inp(["model"]), outputs=out(["SIGMAS"])),
              node(22, "SigmaShift", [3.0], {"shift": 3.0}, inputs=inp(["model"]), outputs=out(["MODEL"]), mode=4),
              node(26, "RandomNoise", [SEED, "fixed"], {"noise_seed": SEED}, outputs=out(["NOISE"])),
              node(29, "UpscaleSettings", ["mmh3_upscale.safetensors", 1088, 1920], {"model_name": "mmh3_upscale.safetensors", "width": 1088, "height": 1920}, outputs=out(["UPSCALE"])),
              node(30, "SpectrumApplyMiniMaxH3", [True], {"enabled": True}, inputs=inp(["model"]), outputs=out(["MODEL"]))]
    by = {n["id"]: n for n in nodes}
    l = link(1, 0, 2, 0, "MODEL"); by[2]["inputs"][0]["link"] = l; by[1]["outputs"][0]["links"].append(l)
    l = link(2, 0, 30, 0, "MODEL"); by[30]["inputs"][0]["link"] = l; by[2]["outputs"][0]["links"].append(l)
    l = link(2, 0, 11, 0, "MODEL"); by[11]["inputs"][0]["link"] = l; by[2]["outputs"][0]["links"].append(l)
    l = link(2, 0, 22, 0, "MODEL"); by[22]["inputs"][0]["link"] = l; by[2]["outputs"][0]["links"].append(l)
    groups = []
    for s in range(1, 13):
        b = s * 100
        mode = 4 if s in (1, 12) else 0
        sn = [node(b + 12, "PrimitiveStringMultiline", [""], {"value": ""}, outputs=out(["STRING"]), mode=mode, title=f"C{s:02d} script"),
              node(b + 13, "PrimitiveFloat", [0.0], {"value": 0.0}, outputs=out(["FLOAT"]), mode=mode, title=f"C{s:02d} seconds"),
              node(b + 15, "EmptyMiniMaxLatent", ["x", 544, 960, 1], {"mode": "x", "width": 544, "height": 960, "batch": 1}, outputs=out(["LATENT"]), mode=mode),
              node(b + 16, "BasicGuider", [], {}, inputs=inp(["model", "conditioning"]), outputs=out(["GUIDER"]), mode=mode),
              node(b + 17, "SamplerCustomAdvanced", [], {}, inputs=inp(["noise", "guider", "sampler", "sigmas", "latent_image"]), outputs=out(["LATENT", "LATENT"]), mode=mode),
              node(b + 21, "SaveVideo", ["video/slot"], {"filename_prefix": "video/slot"}, inputs=inp(["video"]), mode=mode),
              node(b + 32, "MiniMaxUpscale", [], {}, inputs=inp(["latent", "settings"]), outputs=out(["LATENT"]), mode=mode),
              node(b + 35, "SaveVideo", ["video/slot_1088"], {"filename_prefix": "video/slot_1088"}, inputs=inp(["video"]), mode=mode)]
        nodes += sn
        for n in sn:
            by[n["id"]] = n
        l = link(30, 0, b + 16, 0, "MODEL"); by[b + 16]["inputs"][0]["link"] = l; by[30]["outputs"][0]["links"].append(l)
        l = link(b + 16, 0, b + 17, 1, "GUIDER"); by[b + 17]["inputs"][1]["link"] = l; by[b + 16]["outputs"][0]["links"].append(l)
        l = link(b + 15, 0, b + 17, 4, "LATENT"); by[b + 17]["inputs"][4]["link"] = l; by[b + 15]["outputs"][0]["links"].append(l)
        l = link(b + 17, 0, b + 32, 0, "LATENT"); by[b + 32]["inputs"][0]["link"] = l; by[b + 17]["outputs"][0]["links"].append(l)
        l = link(29, 0, b + 32, 1, "UPSCALE"); by[b + 32]["inputs"][1]["link"] = l; by[29]["outputs"][0]["links"].append(l)
        groups.append({"title": f"CLIP {s:02d}", "bounding": [0, s * 400, 1200, 380]})
    nodes += [node(9990, "MarkdownNote", ["template note"], {"text": "template note"}),
              node(9991, "Note", ["protected note"], None)]
    return {"id": "00000000-0000-0000-0000-000000000000", "revision": 0, "last_node_id": 9991, "last_link_id": lid[0],
            "nodes": nodes, "links": links, "groups": groups, "config": {}, "extra": {}, "version": 0.4}


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--out", default=str(Path(__file__).parent / "fixtures" / "template_synthetic.json"))
    a = p.parse_args()
    wf = build()
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(wf, indent=1), encoding="utf-8")
    print(f"wrote {a.out}: {len(wf['nodes'])} nodes, {len(wf['links'])} links")
```

## v1_workflow/tests/e2e_dry.py

```python
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
```
