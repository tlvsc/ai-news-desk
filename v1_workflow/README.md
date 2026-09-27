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
