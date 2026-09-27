# AI News Desk V1 workflow: scan findings, 2026-09-27 (Claude Code cloud session)

Scope scanned: this repo (8 files), Drive AI_News_Desk (about 175 folders, 795 files, 22 Python scripts), the Claude folders on Drive, 22 Claude lane handoffs from 26 Aug to 11 Sep, the 26 Sep handoff, Decision Log, Master Memory, Task List, registries, all current rulebooks, the 23 to 26 Sep run outputs. Mirrors and indexes are in docs/scan_2026-09-27/ next to this file.

## 1. Structural blockers (must be said first)
1. This cloud session cannot reach the PC. The scripts that run V1 daily exist only on the PC: aind_v1.py with its json and tests (the 09:00 Windows task), the Comfy launcher, the stitcher named in the rulebook (aind_v1_headline_script.py), and the Workflow Monitor working copy. None of these is on Drive. The scan covered every Drive copy.
2. This container cannot fetch publisher sites, cannot reach the OpenAI API, and has no ffmpeg. Source fetching, ComfyUI generation and the final stitch can only be tested on the PC. The container can: write and unit test code, run web search, read and write Drive, call the Anthropic API.
3. The cards renderer that the Decision Log registers (aind_cards.py) is only inside a 4.4 MB zip on Drive. The Claude lane has its own smaller renderer on Drive (make_cards_Wed9-9-26.py plus render_25sep.py and prepare_cover_25sep.py).
4. PC paths seen in the 26 Sep manifest: working root C:\Users\erans\OneDrive\Documents\ChatGPT\Codex\daily_data_generated\YYYY-MM-DD; ComfyUI at E:\ComfyUI with outputs in E:\ComfyUI\output\video.

## 2. What V1 is today, as built
Chain: 55 registered sources (five per category) -> daily-pool.md -> Full Report (target 100 to 200 stories; 18 Sep hard gates: pool at least 300 candidates, report 50 to 150) -> Bulletin 25 to 30 -> The Bigger Picture -> Cards, exactly 15 PNG 1080x1920 plus one combined image -> Headlines, 12 slot ComfyUI JSON, H3 Ref2V 544x960 upscaled to 1088x1920, stitched to 1080x1920 mp4 with srt -> Drive daily_data_generated/YYYY-MM-DD -> Rafi publishes by hand.
One rulebook per thing: report master prompt; Headlines_Master_Rules_Structure.txt; Cards_Master_Rules_Structure.txt with AIND_Cards_Rules.md and AIND_Publishing_QA.md; articles_phrasing_instructions (plain language law and the 26 Sep meaning check); AIND_daily_storage_rules.txt; AIND morning run prompt V1 with the 18 Sep gates; Decision Log 23 Sep category order; approved Headlines and cards endings.
Claude lane runs so far: 14 Sep (LV1.1 test, ten research agents), 23 Sep, 25 Sep (23 search agents, 187 candidates, 153 stories, the token burner), 26 Sep (Headlines delivered).
Every run was manual in a chat. Nothing on the Claude side is scheduled. The ChatGPT side owns the 09:00 report task.

## 3. Where an LLM is truly needed
Code only, zero tokens: fetch the 55 sources; reporting window check; exact duplicate check; pool and checkpoint files; the gates; category order; syllable count and box seconds; Comfy JSON fill; validator; Comfy queue and poll; clip inventory; stitch, date overlay, subtitles, loudness; storage manifest; Drive upload; the approval pauses.
LLM required: (a) per candidate digest with relevance, category and importance, cheap model, one batch on short records; (b) near duplicate judgement only for pairs the code flags, cheap; (c) Full Report story text, mid model; (d) forward analysis and The Bigger Picture, strong model, small input; (e) Bulletin, cards and Headlines copy under the plain language law plus the meaning check, mid; (f) final editorial QA, strong.
Token principle from the 26 Sep handoff: read raw once, distill to tiny records, never re-read raw. Rough daily budget with that shape: about 150 to 250 thousand tokens, against the millions the 25 Sep agent swarm used. This is an estimate to measure, not a promise.

## 4. Yesterday's material about agents per task
1. Handoff 26 Sep A: staged pipeline, cheap model for extraction, strong model only on the distilled brief, JSON on the PC at zero tokens. Not implemented.
2. Model Setup Comparison, 25 Sep: per stage table of code versus Luna, Sol, Astra. Marked as an untested hypothesis. Rafi's recorded lesson: work with Astra.
3. LV1.1 agent brief, 14 Sep: one research agent per search group with a fixed record format. It worked, and twenty plus agents each reading the raw web is exactly the cost problem.
4. Handoffs 26 Aug to 11 Sep contain no sub agent or model routing plan at all. The only agents were the two lanes.

## 5. Rule clashes to raise before building
1. Rafi 27 Sep: V1 only. Claude only news channel decision D4 (7 Sep) chose the V2 chain as backbone. Newest wins: V1.
2. Decision D6 (7 Sep): build and daily run in Codex on the local machine. Today: a Claude Code script. Newest wins: Claude Code. Recorded as a change.
3. Master Memory: live V1 is frozen; nothing changes without exact approval. Building in a separate Claude folder respects this. Promotion to live is a separate approval.
4. The model doc names OpenAI tiers; a Claude Code script would use Claude tiers unless an OpenAI key is chosen. Decision needed.
5. "Your folder" is ambiguous: this repo, the Drive folder Claude only news channel, or claude_files_only.
6. Trust note from the 2 and 7 Sep handoffs: open every session with the shortest plan and no work before "go". This report follows that.

## 6. Proposed V1 structure, staged, one script per process, file contracts between stages
run_v1.py orchestrator: edition date, resumable state file, gate checks, approval pauses, machine readable checkpoint, Workflow Monitor compatible run description.
s01_collect (PC, code) -> s02_digest (LLM cheap, one batch) -> s03_dedupe (code, cheap LLM for flagged pairs) -> s04_classify_rank (cheap) -> s05_gates (code, plus web search major news miss list) -> s06_report (mid; analysis strong) -> s07_bulletin (code select, mid copy) -> s08_bigger_picture (strong) -> s09_cards_select (code) -> s10_cards_copy (mid, meaning check) -> s11_cards_render (existing renderer, code) -> s12_headlines_select (code, syllables over 4.4) -> s13_headlines_fill (code, generalised from the 26 Sep fill script) -> s14_validate (existing validator) -> s15_comfy (PC, code) -> s16_stitch (PC, ffmpeg per Section D2) -> s17_store (Drive plus manifest).
Pauses for Rafi: after copy (cards and Headlines wording), before the Comfy queue, before publish. One tap each.

## 7. Routes, Rafi's effort first
A. Build here into the repo now: orchestrator, every pure code stage, prompt files, synthetic tests. Rafi pulls the repo on the i9 and runs. Fetch, ffmpeg and Comfy stay untested until the PC.
B. Same as A, plus a Claude Code local session on the i9 inside the repo for the three PC only stages. Rafi starts the session and relays.
C. Rafi widens this environment's network so the collector can be tested here. Sites may still block.
Recommend A now, then B for the PC only stages.

## 8. Decisions needed
1. Your folder: repo (recommended) / Claude only news channel on Drive / claude_files_only.
2. LLM engine for the required stages: Claude Code subagents on Rafi's subscription (recommended; Haiku cheap, Sonnet mid, Opus strong) / Anthropic API key / OpenAI Luna, Sol, Astra key.
3. Test output destination: a separate Claude test folder on Drive (recommended) / daily_data_generated.
4. PC scripts: copy aind_v1.py, the stitcher and the Comfy launcher into the repo (recommended) / into Drive.
5. First build scope: full chain skeleton with all stages (recommended) / report chain first.

## 9. Mistake record (this session)
What: four mirrored text files were emptied when a helper re-ran a decode after I had already decoded and removed the base64 originals. Prevention: never touch files a helper is still writing; decode only what exists and never overwrite non empty files. Fix: helper re-downloading the four files; contents were already captured in the notes. Where recorded: this file and the session handoff.
