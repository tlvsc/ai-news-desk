# AI News Desk — Session Handoff

Last updated: 2026-09-27, end of the build session (Rafi approved continuing after the compaction).
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

## State at the end of the session

The V1 workflow package is built and tested in `v1_workflow/` (branch `claude/epic-cray-meivo9`). Everything that
can run in the cloud has run; the three PC-only stages stop with exit 4 and written instructions.

Evidence, dry end-to-end run (`python tests/e2e_dry.py`, synthetic 342-row pool, synthetic Comfy template, zero tokens):

| check | result |
|---|---|
| unit tests (`python -m unittest tests.test_units`) | 11 of 11 OK |
| pool candidates (gate 300) | 330 |
| unique events / Full Report stories (gate 50 to 150) | 164 / 150 |
| Bulletin (gate 25 to 30) | 30 |
| cards planned (gate 15) | 15, market 3 of 3 cap, fun last |
| Headlines core clips (gate 8 to 9) | 9; QA tool (vendored validate_delivery.py) PASS |
| all eight checkpoint gates | PASS |
| model calls per edition (dry) | 41: digest 9, dedupe pairs 4, classify 5, report 13, analysis 1, bulletin 1, meaning checks 3, bigger picture 1, cards copy 1, headlines 3 |
| exit codes | s01 to s11 → 4 (card renderer not on this machine), s12 to s14 → 0, s15 → 4 (no ComfyUI), s16 → 4 (no ffmpeg), s17 → 0 |

Not verified anywhere yet: live LLM replies (only the headless CLI call itself was verified earlier), the real
collector against publisher sites, the card renderer command, ComfyUI queueing (UI to API conversion), ffmpeg
stitch and loudness. Those are the i9 session's job (Route B).

## Next session, in order

1. Rafael decides whether the package goes to Drive `claude_files_only/v1_workflow/` now (CLAUDE.md rule 15 says
   after it is finished and verified; the PC stages are not verified yet). If yes: upload every file as an
   individual text file, never zipped, then report ids and sizes.
2. On the i9 (Claude Code local, repo checked out): fill `config/v1_config.json` paths (see README "Before the
   first real run"), copy the master template locally, run `python run_v1.py --edition <date> --llm dry --fixture
   tests/fixtures/pool_320.jsonl --approve-all` to prove the machine, then a live collect only:
   `python run_v1.py --edition <date> --to s01` and read `work/source_ledger.json` (which of the 55 sources answer).
3. First live LLM stage in isolation: `--from s02 --to s02` and read `work/llm_log.jsonl` for real token and cost
   numbers; compare with the estimate in `docs/scan_2026-09-27/FINDINGS.md`.
4. Register the card renderer (`cards.renderer_command`; aind_cards.py from the Drive zip or the Claude-lane
   make_cards script) and confirm s11 verifies 15 PNG at 1080x1920.
5. s15 on the PC with ComfyUI open: the UI to API conversion in `stages/s15_comfy.py` is untested against the
   real node set; if `/prompt` rejects it, export "Save (API format)" from the ComfyUI frontend once and compare.
6. s16: confirm ffmpeg filter chain, the .ass rendering at phone size (house rule 7: frames are exported to
   `Headlines/supportive files/frames/`), and the loudness numbers in `Headlines_<date>_QA.json`.
7. Copy `aind_v1.py`, the stitcher and the Comfy launcher from the PC into the repo (they are PC-only today).

## Package map (all under `v1_workflow/`)

- `run_v1.py` orchestrator; `RUN_V1.cmd` double-click launcher (checks Python runs, house rule 13).
- `config/` v1_config.json (paths, gates, models, batch sizes, `max_dedupe_pairs` 240), categories.json,
  sources_v1.json, headlines_comfy_prompt.txt ({symbol} and {script} placeholders).
- `lib/` common.py (RunContext, dates, `require_approval`, `update_checkpoint`, exit codes 0/2/3/4),
  llm_client.py (live/dry/manual, cache, log), llm_dry.py (reply contracts), syllables.py.
- `llm/prompts/` eleven instruction files, one per model call.
- `stages/` s01 to s17; PC-only: s11 render, s15 comfy, s16 stitch. Approval pauses: s10, s12, s15, s16.
- `vendor/validate_delivery.py` verbatim Drive QA tool; s13 writes its `extra.aind_headlines` schema.
- `tests/` test_units.py, make_fixture.py, make_template.py, e2e_dry.py, fixtures/.
- `README.md` run instructions, stage table, config keys.

## Known limits (documented, not hidden)

- Caption timing in s16 is proportional by syllables per clip, not word-level (no Whisper on a zero-dependency
  machine). The blueprint's transcription check remains a separate step.
- s15's UI to API conversion relies on `widgets_values_named` (present in the real template) with a positional
  fallback; untested against the live ComfyUI node set.
- Dry-mode text is obviously synthetic ("DRY ...") and must never reach a real edition; `--approve-all` prints a
  warning for the same reason.
- The synthetic fixture is self-similar, so the dedupe stage records thousands of "kept separate" pairs; real
  pools will show far fewer.

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
3. Token blow-up caught by the dry run: the first dedupe pass sent every ambiguous pair to the model (333 calls
   per edition). Prevention: measure calls per prompt in every dry run before any live run (the e2e prints them).
   Fix applied: entity guard, similarity-ranked cap of 240 pairs, batch 60 (now 4 calls).
