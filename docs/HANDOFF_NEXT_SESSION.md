# AI News Desk — Session Handoff

Last updated: 2026-09-27, written immediately after an automatic context compaction.
Previous handoff (2026-08-14, episode 1) is kept as `HANDOFF_NEXT_SESSION_old.md`.

## Why this handoff exists

The cloud session that ran the 27 Sep scan and started the V1 workflow build was
compacted by the system mid-build. Rafi's standing rule: on compaction, stop, say so,
write the handoff, open a new chat. This file is that handoff. Nothing after the
compaction point was built; the work in progress is committed as-is, untested.

What was lost by compaction: the verbatim earlier conversation (replaced by a
generated recap), including the exact wording of my findings report and of the
helper-agent hand-backs. What survived: every file listed below, the scan documents
in `docs/scan_2026-09-27/`, the Drive mirror notes, and Rafi's four decisions.

## Rafi's decisions in this session (binding)

1. "Your folder" = Google Drive `claude_files_only`. The finished package is saved
   there as the authority copy, as individual text files, never zipped.
2. Route B: build and test in this git repo (branch `claude/epic-cray-meivo9`), then
   a Claude Code local session on the i9 runs the PC-only stages (collect from
   publishers, ComfyUI, ffmpeg stitch).
3. LLM engine for the pipeline: Claude Code subagents on Rafi's subscription via the
   headless CLI. Tiers: haiku = cheap, sonnet = mid, opus = strong.
4. Test-run outputs go to a local PC folder only. No Drive writes during testing
   (`drive.upload_enabled` is false in the config).

Scope reminders from Rafi's opening message: V1 workflow only (not V2, not V1.1);
one independent script per process; avoid LLM calls unless a field truly needs one;
plan for the fewest tokens; everything lives in the Claude folder so it can be tested
separately from the ChatGPT lane. Live V1 ChatGPT prompts, automations and files
must not be touched.

## What exists now (all under `v1_workflow/`, committed, py_compile clean, NOT run)

Config
- `config/v1_config.json` — lane VL1, Asia/Jerusalem, 09:00 window, gates
  (pool ≥300, report 50–150, bulletin 25–30, cards 15, headlines core 8–9,
  dedupe history 30 days), llm modes and batch sizes, headlines settings
  (4.4 syllables/s, approved ending, Comfy URL and output dir, ffmpeg, subtitle
  font and margins), cards settings, drive ids with upload disabled.
- `config/categories.json` — 11 categories in the 23 Sep order with keys
  POL MKT SEC ENE ROB MOD RES LAW HEA SOC FUN, card slots (MKT 3, others 1),
  aliases, verification statuses, dispositions.
- `config/sources_v1.json` — 55 sources SRC-V1-001..055 with feed hints.

Library
- `lib/common.py` — paths, logging, json/jsonl io, `rename_old` (house rule 3),
  date helpers (D-M-YY, "FRI 11 SEP 2026", reporting window), `RunContext`
  (run folder mirroring the Drive product tree, state.json, gates, category order,
  importance labels, V1_script_report.md append), `stage_main` argparse wrapper,
  text normalisation and jaccard.
- `lib/llm_client.py` — `LLMClient.call(tier, prompt_name, payload, stage)` with
  modes live (headless `claude -p --bare --model … --output-format json
  --max-turns 1 --disallowedTools *`), dry (deterministic stand-ins), manual
  (request/reply files for a subagent). Cache by sha256, usage log to
  `work/llm_log.jsonl`, one JSON-only retry. `batched()` helper.
- `lib/llm_dry.py` — the reply contracts each prompt must satisfy: p_digest,
  p_dedupe_pairs, p_classify, p_report_story, p_analysis, p_bulletin_copy,
  p_meaning_check, p_bigger_picture, p_cards_copy, p_headlines_copy, p_editorial_qa.
- `lib/syllables.py` — override table merged from Drive `syl.py` and the 26 Sep fill
  script, `count`, `box_seconds` (syllables / 4.4, two decimals, no rounding up).

Stages written (s01–s08)
- `s01_collect.py` — urllib RSS/Atom/HTML collector, per-source terminal status
  strings, `work/raw_pool.jsonl` and `work/source_ledger.json`. Cannot run in the
  cloud container (publisher sites unreachable); has `--fixture` for tests.
- `s02_digest.py` — cheap-tier digests, drops raw text. `work/digests.jsonl`.
- `s03_dedupe.py` — union-find on url and jaccard, cheap-tier pair check for the
  0.30–0.55 band, 30-day history match. `work/events.jsonl`, `work/pool_dispositions.jsonl`.
- `s04_classify.py` — cheap-tier category, importance, verification. `work/ranked.jsonl`.
- `s05_gates.py` — zero-LLM checkpoint (`run-checkpoint.json`, `major-news-gate.md`),
  fail-closed exit 2, `--override gate=reason`.
- `s06_report.py` — Full Report in master-prompt story format, daily-pool.md,
  history append, strong-tier analysis once.
- `s07_bulletin.py` — 25–30 items, mid-tier copy plus meaning check.
  KNOWN BUG, line 70: a stray `out.append(row) if … else None` after line 69
  double-appends failing rows. Intent: failing rows stay in `out` flagged DRAFT
  and are also counted in `failed`. Replace lines 69–70 with
  `out.append(row)` and `if row["meaning_check"] != "PASS": failed.append(row)`.
- `s08_bigger_picture.py` — strong-tier, one call, spoken line 44–53 syllables.

## What is NOT built yet (in build order)

1. `llm/prompts/*.md` for: digest, dedupe_pairs, classify, report_story, analysis,
   bulletin_copy, meaning_check, bigger_picture, cards_copy, headlines_copy,
   editorial_qa. Contracts must match `lib/llm_dry.py` exactly.
2. `stages/s09_cards_select.py` — code only: cover, criticals spend category slots,
   category order with slot counts, market max 3 including criticals, robotics and
   fun required, "More in the full report" 3–4, The Bigger Picture, closing = 15.
3. `stages/s10_cards_copy.py` — mid "cards_copy" + "meaning_check" →
   `cards/supportive files/cards_D-M-YY_copy.json`.
4. `stages/s11_cards_render.py` — wrapper that writes edition.json and
   content_lock.json and calls a registered renderer (aind_cards.py lives only inside
   the 4.4 MB Drive zip, id 13Ic8tAb_IgWFUTWgrzmC0eLp4OxCzk3V); otherwise stops with
   instructions.
5. `stages/s12_headlines_select.py` — 12 slots, mid "headlines_copy", syllable loop
   to 7–9 s per story, meaning check → `Headlines_D-M-YY_selection.md` and
   `headlines_D-M-YY_pack.json`.
6. `stages/s13_headlines_fill.py` — generalised from Drive `fill_headlines_26-9-26.py`:
   slot k nodes 100k+12 script, +13 seconds, +21 base save, +35 upscale save;
   widgets_values and widgets_values_named mirrored; group titles; MarkdownNote 9990;
   new workflow id; node 11 steps 6; twelve-slot table; stale-word scan;
   `extra.aind_headlines` pack.
7. `stages/s14_validate.py` — wraps a vendored copy of Drive `validate_delivery.py`
   (`--headlines`) with a provenance note.
8. `stages/s15_comfy.py` (PC) — queue API-format graph at 127.0.0.1:8188, poll
   /history, never queue twice, clip inventory from E:/ComfyUI/output/video.
9. `stages/s16_stitch.py` (PC) — ffmpeg per Section D2: crop 4 px each side to
   1080x1920, libx264 high fast CRF 17 30 fps yuv420p, AAC 192k 48k, −14 LUFS
   −2 dBTP, `.ass` subtitles with PlayResX 1080 / PlayResY 1920, Instrument Sans,
   40% black box, source credit; `.srt` alongside; QA json. Approval pause before burn.
10. `stages/s17_store.py` — local `storage_manifest_YYYY-MM-DD.json` and
    `drive_upload_plan.json`; Drive upload stays disabled in test.
11. `run_v1.py` orchestrator — `--edition --from --to --llm live|dry|manual
    --approve <stage> --override --force --run-description`; state.json resume;
    approval pauses exit 3 with `approvals/<stage>.pending.md`; exit codes
    0 ok, 2 gate failed, 3 approval needed.
12. `tests/` — syllables, dedupe, cards select, gates, fill with a synthetic
    template, collector parse with an RSS fixture, end-to-end dry run with about
    320 synthetic items. Run them in the cloud; fix the s07 bug first.
13. `RUN_V1.cmd` (double-click, verifies python actually runs, stdlib only) and
    `v1_workflow/README.md`.
14. Update `CLAUDE.md` rule list if Rafi gives new workflow instructions; commit and
    push to `claude/epic-cray-meivo9`; then save the package to Drive
    `claude_files_only/v1_workflow/` as individual files and report evidence
    (file ids, sizes).
15. Route B second half: Rafi opens Claude Code local on the i9 for s01, s15, s16
    verification and copies `aind_v1.py`, the stitcher and the Comfy launcher into
    the repo (they are PC-only today, not on Drive).

## Environment facts the next session needs

- Cloud container: no ffmpeg, cannot reach publisher sites or the OpenAI API; can
  reach api.anthropic.com, GitHub, PyPI. Python 3.11, Node 22, Claude CLI present
  and verified for headless calls (about 28K cached context overhead per call).
- Drive MCP returns 5 items per page whatever pageSize says; follow nextPageToken.
- PC paths: `C:\Users\erans\OneDrive\Documents\ChatGPT\Codex\daily_data_generated\YYYY-MM-DD\`,
  `E:\ComfyUI\output\video`, ComfyUI Desktop "ComfyUI refael", RTX 3090.
- Scan outputs and the Drive mirror index: `docs/scan_2026-09-27/`.

## Mistakes recorded this session

1. Helper-agent files: I decoded and removed `.b64` files a mirror agent was still
   using, which produced four empty files. Prevention: never touch files a helper is
   writing; never overwrite a non-empty target. Recorded in
   `docs/scan_2026-09-27/FINDINGS.md` section 9.
2. Compaction with uncommitted work: I let the context grow to the compaction point
   with the whole `v1_workflow/` build uncommitted and no handoff written.
   Prevention: commit after every batch of files; write or refresh this handoff at
   every natural checkpoint, not only at the end. Fix location: CLAUDE.md rule 14
   (added in this commit).
