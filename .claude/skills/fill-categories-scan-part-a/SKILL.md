---
name: fill-categories-scan-part-a
description: Fill_categories_scan_part_A. The AI News Desk daily run, part A, in a Claude Code cloud session on this repo - the 24-hour scan, 16 category curators (15 to 20 stories each, Fun Side 10), the pool, reading and writing, editor checks, the Bigger Picture, the Full Report and Daily Bulletin PDFs, delivered to Rafi in chat. When part A is delivered it starts Fill_category_scan_Part_B (cards and Headlines) by itself. Use when Rafi asks to start the scan, run the daily report, the fill run or today's edition.
---

# Fill_categories_scan_part_A

Rafi's names (3 Oct 2026): Fill_categories_scan_part_A and Fill_category_scan_Part_B; his spelling is kept.
Part A was created on 29 Sep 2026 as Temporary_independant_claude_only_15_per_category_fill_run and renamed on
3 Oct 2026. Both parts live ONLY in this repo, on branch claude/eager-archimedes-ajnex3: never on Drive, never
merged to main, so ChatGPT never sees a second set of instructions. They run only in a Claude session connected
to this repo (CLAUDE.md rules 0 and 9).

Scope of part A: scan to Full Report and Daily Bulletin (PDFs, their input JSON, markdown, daily-pool.md, pool
CSV), delivered to Rafi in chat. Then it starts part B with the Skill tool (fill-category-scan-part-b), which
chooses the cards and Headlines, stops for Rafi's approval, then renders and delivers them.

This skill holds the ORDER OF WORK and the tools. The RULES live in Drive and are fetched fresh every run
(step 0); if a brief here disagrees with them, flag it to Rafi in one line and follow CLAUDE.md (rule 0):
- Full_Report_V1_Rules_Structure.txt (Blueprint_Library / Full Report blueprint V1; take the file of that name)
- Bulletin_V1_Rules_Structure.txt (Blueprint_Library / Bulletin blueprint V1)
- Article_phrasing_instructions_AIND_V1 (Prompt Library / prompts, Drive 16W6d7GpBFE0lPtNSgkx0MiyoNrv1s4Af since 5 Oct 2026; call it
  only by this name). It is the ONLY place for reader levels and the writing shape; no brief or script restates them. Every writer,
  and the Bigger Picture agent, re-reads Sections 1, 1A, 1B and the product section BEFORE EACH ITEM.
- AI News Desk — STORAGE & FILE ROUTING STANDARD (00 — PROJECT OS) for where things would go on Drive.
- CLAUDE.md in this repo (house rules; rules 14, 16 and 17 set counts, cutoffs and the Bigger Picture).

## Working with Rafi during the run

- 8 Oct 2026 (Rafi): for today only, every helper job that says Sonnet runs on Haiku; Opus and Fable jobs do not change. Scripts are not changed during a run; fixes go in this text and in the list files.

- Replies: simple English, short numbered points, TTS friendly. No walls of text.
- Before starting, say in one line: the edition date, the window, and anything structural that limits the run.
- Counts and cutoffs are never questions: choose them, then state them (CLAUDE.md rule 14).
- Never ask what the record already answers (the files, this skill, the chat). Only real decisions go to Rafi,
  batched as tappable options.
- Check twice, from different angles (steps 7 and 12), before calling anything done; report real numbers.
- Nothing is published without Rafi's explicit approval. Nothing is written to Drive unless he clearly asks.
- Nothing is deleted: superseded local files get `_old`.

## Paths

```
A=/home/user/ai-news-desk/.claude/skills/fill-categories-scan-part-a
K=$A/scripts
W=<scratchpad>/run_<YYYY-MM-DD>          # the day's working folder, outside git
```
Every script takes `--workdir $W`. collect.py writes `$W/run.json` (edition and window).

## Steps

### -1. Fresh clone check (Rafi, 9 Oct 2026; closes lesson 83 of 6 Oct, which repeated on 9 Oct)
Before anything else: `git pull --rebase origin claude/eager-archimedes-ajnex3`; if CLAUDE.md or this skill changed, read them again before any agent is launched.

### 0. Setup (one background agent, Drive read only)
Fetch into `$W/rules/`: Full_Report_V1_Rules_Structure.txt, Bulletin_V1_Rules_Structure.txt and
Article_phrasing_instructions_AIND_V1.txt (find each by name; check its modified time). Fetch into `$W/`:
build_pdf.py from Bulletin blueprint V1 / Permanent Assets (Drive 1elDaskuqhSG1CVvdapSe8NNwhGMX6ImH), md5
5b5869e51313b19e0b5554b2f890cae5 (42,113 bytes); stop and tell Rafi if it differs. Fetch the Full Report texts of the previous 14 days into `$W/archive14/<date>.md` (drive_save.py, no content read into the
agent's context; step 9b). Take the pools of the last
four days FROM THIS REPO, runs/<date>/out/AIND_Pool_<date>.csv (Rafi, 7 Oct 2026: no Drive agent job for them); only if a day is missing there, from AI_News_Desk / daily_data_generated / <date> / reports / supportive files / AIND_Pool_<date>.csv;
a day that is not on Drive is taken from the local run folder (`<scratchpad>/run_<date>/out/`) or, if missing,
named in the start line. Save each file with drive_save.py ("Saving a Drive file to disk" below). Then:
```
python3 $K/rules_diff.py --new $W/rules --old <last run>/rules      # read every changed line
python3 $K/combine_pools.py --workdir $W --pool <day 1 csv> --pool <day 2 csv> --pool <day 3> --pool <day 4>
```
A rule change that clashes with CLAUDE.md goes to Rafi in one line; the run continues with CLAUDE.md.

### 1. Collect (about 1 minute)
```
python3 $K/collect.py --workdir $W --edition YYYY-MM-DD --yesterday $W/yesterday_pool.csv
```
The 24 hours ending now (Rafi, 30 Sep 2026); `--hours 30` only when Rafi asks, for a late start.

### 1b. The sources (the 55 of 2 Oct 2026 plus the big outlets of 8 Oct 2026; Google News stays first and main)
```
python3 $K/source_scan.py --workdir $W        # about 1 minute; 3 Oct 2026: 174 stories
```

### 1c. Viral sweep (Rafi, 10 Oct 2026; CLAUDE.md VIRAL RULE; new script viral_sweep.py, flagged to Rafi as a new file)
```
python3 $K/viral_sweep.py sweep --workdir $W        # counts distinct outlets per story, prints floors and the LOW SCORE, HIGH REACH list
```
Pick at most 3 stories about AI from its list and write `$W/viral_picks.json` {"picks": [{"cluster": N, "note": "why it is about AI"}]}.
Put each pick into `$W/prompt_extra.json` under "curate" for the category it belongs to (key "1" to "16"): "MUST INCLUDE, score at least <floor> (VIRAL RULE): <title> carried by <n> outlets, led by <top outlets>; take the best readable outlet; the score is not lowered for tone". A pick that ran on an earlier day at a lower score may run once more at its floor (the rule overrides NO OLD NEWS, NO UPDATE CARDS and NO REPEATS IN 7 DAYS for that one run); say so in the same line.
Floors: 10 or more outlets 7, 20 or more 8, 30 or more (or 20 or more with 3 top outlets) 9. "Top outlet leading" is the script's reading (3 or more top outlets at 20 or more); Rafi to confirm.

### 2. Curate (16 agents in parallel, 5 to 10 minutes)
```
python3 $K/make_prompts.py --workdir $W --stage curate        # 15 to 20 main picks, 3 backups; Fun 10
```
Launch 16 background agents in ONE message (model "sonnet", CLAUDE.md MODEL POLICY), description "Curate cat NN", prompt:
`Read $W/prompts/curate_NN.txt and follow it exactly.` Each writes `$W/pool/cat_NN.json`. The brief carries the
day rules (candidates_55.json, the four day repeat list, 15 to 20, never pad); nothing is appended by hand.

### 3. Build the pool
```
python3 $K/build_pool.py --workdir $W
```
Each category keeps the main picks its curator wrote (up to 20, Fun 10); a backup moves up only to replace a
removed pick, never to pad. Read `$W/out/build_log.json`: for a near duplicate or the same story in two
categories decide which stays (`$W/drops.json` {"drops": [[cat, "exact title", "why"]]} or
`$W/dedupe_overrides.json`), then run again. A category printed SHORT by 3 or more gets a filler; short by 1 or 2 gets NONE, state the count (Rafi, 7 Oct 2026, saves about 90k tokens each). The SHORT word printed by build_pool.py is measured against the curator's own count, not against 15: read it against 15 (Markets on 8 Oct 2026: 17 stories, inside 15 to 20, so no filler). Scripts are not changed during a run; this text is the fix (Rafi, 8 Oct 2026):
```
python3 $K/make_prompts.py --workdir $W --stage fill --cat NN --need K     # agent: Read $W/prompts/fill_NN.txt ...
python3 $K/merge_filler.py --workdir $W --cat NN && python3 $K/build_pool.py --workdir $W
```
Never rebuild the pool after the writers have started: the item numbers shift. State the pool size.
Viral check (CLAUDE.md VIRAL RULE): `python3 $K/viral_sweep.py check --workdir $W` must say "all floors met" before step 4: every pick is in the pool at or above its floor (if a pick is missing, append it by hand as on 10 Oct 2026: backup `out/` first, add the row to the pool JSON and CSV, add its chunk, run prefetch.py, and have one writer write that one item).

### 4. Decode links (background, 2 to 15 minutes)
```
python3 $K/decode_links.py --workdir $W        # run_in_background; resumable
python3 $K/url_fixes.py --workdir $W           # tracking codes and cut-off links -> url_fixes.json
```
Start the decoder with the Bash tool's run_in_background option. Never `nohup ... &` with a `pgrep -f` watcher.

### 5. Chunks and article text (write only what can print)
```
python3 $K/make_chunks.py --workdir $W         # pool score 5 and up plus the Fun Side; the rest stays pool only
python3 $K/prefetch.py --workdir $W            # run_in_background; 3 Oct: 89 of 160 readable
```
Rafi, 4 Oct 2026: the pool keeps every story as headline and link; an article is read and written only for
stories that can reach the Full Report (curator score 5 and up, the writers never raise a score) and for the
Fun Side. If step 8 has to lower the report cutoff on a thin day, run
`make_chunks.py --workdir $W --min-score 4 --only-missing`, then prefetch and a second writer round for those.

### 6. Read and write (16 agents in parallel, 5 to 10 minutes)
```
python3 $K/make_prompts.py --workdir $W --stage write
```
One-off instructions for a category go in `$W/prompt_extra.json` {"write": {"12": "..."}} before this command.
Launch 16 background agents (model "sonnet", fillers too; CLAUDE.md MODEL POLICY), description "Read and write cat NN", prompt
`Read $W/prompts/write_NN.txt and follow it exactly.` Each writes `$W/facts/<id>.json` and
`$W/report_entries/<id>.json` at the Full Report level of Article_phrasing_instructions_AIND_V1 (read before each entry).

### 7. First check (structure and data)
Run `python3 $K/viral_sweep.py check --workdir $W` again after the writers: no entry of a viral pick may be below its floor (the writers cannot lower it; a writer's fact or date doubt goes to Rafi, not into a lower score).
REPLY STORIES (Rafi, 4 Oct 2026): "reply_without_earlier_story" lists entries that answer an earlier story
without naming it; add who answers whom and what the earlier story said, from the facts or the follow_up_of item.
```
python3 $K/qa_check.py --workdir $W
```
Fix every missing field, Google link, cut-off link, copied headline and leaked process note (or accept a false
positive with its reason, e.g. "blocked" meaning a court blocked something). It writes `$W/held.json`: old news
re-dated into the window, including an undated "FOLLOW-UP of mid-2026". Add same-story duplicates by hand under
"duplicate" ({"C16-06": "same story kept as C05-02"}). It prints the counts at each cutoff.

### 8. First build
```
python3 $K/build_products.py --workdir $W [--report-min 5] [--bulletin-min 7] --bulletin-min-cat HEA=6,SOC=6 --report-fill-to 110
```
Report: aim at 100 to 120 stories (Rafi, 7 Oct 2026, CLAUDE.md rule 14): cutoff 5 or 6, whichever lands closest, plus the Fun Side. Bulletin: the cutoff that
lands near 30 to 50 (usually 6, 7 or 8 and up), plus the top 3 Fun (CLAUDE.md rule 14; 3 Oct 2026 Rafi chose 7
and up). Read the "CHECK bulletin spread" line: a category with no story is stated to Rafi with the count.

### 9. Editors (2 agents in parallel)
```
python3 $K/make_prompts.py --workdir $W --stage edit
```
Launch 2 background agents (model "opus", CLAUDE.md MODEL POLICY; `Read $W/prompts/edit_A.txt and follow it exactly.`, the same for edit_B). Read
`$W/qa2_log_A.json` and `qa2_log_B.json`; act on every "unresolved" item (hold re-dated or duplicate stories in
held.json; an unclear quote of a named person is kept only with its hedge, or held), then build again.

### 9b. Last stage of removing duplicates: the 14 previous Full Reports (Rafi, 5 Oct 2026)
Before the Bigger Picture and the final build, every report entry is compared with the Full Reports of the 14 days
before the edition, saved from Drive (read only) into `$W/archive14/<date>.md` by the step 0 Drive agent
(AI_News_Desk / daily_data_generated / <date> / reports /; an older day may sit in the old "Daily Global AI Intelligence
Reports" folder; a day with no report text is named as a GAP, never guessed).
```
python3 $K/check_dup14.py --workdir $W        # prints every REPEAT with the earlier line; FOLLOW-UP kept = new facts
```
Read each REPEAT next to its earlier line: a real repeat (same story, no new facts) goes into `$W/held.json` under
"duplicate" ("repeat of <date>"); a false match (different story, shared names) stays. `--hold` writes all of them;
use it only when the list was read. A follow-up with new facts stays in the report; whether it can be a card is
decided in Part B by the CARD FILTER of CLAUDE.md rule 16 (a meaningful update can). Then build again. 5 Oct 2026: 11 of 14 reports found; 10 real repeats among 132 entries
(the AMD and World Labs deal had run on 29 Sep). The Bigger Picture is written after this stage, never before it.

### 10. The Bigger Picture
One agent writes `$W/bigger_picture.json` and `$W/bigger_picture_bulletin.json`, following `$A/briefs/bigger_picture.md`; its model and effort are set ONLY by the BIGGER PICTURE MODEL line of CLAUDE.md, and the main session never writes it. Agent prompt: `Read $A/briefs/bigger_picture.md and follow it exactly; WORKDIR is $W; cutoffs: <report-min> and <bulletin-min>.`

### 11. Final build and PDFs
```
python3 $K/build_products.py --workdir $W [same cutoffs]
cd $W && python3 build_pdf.py --input products/report_pdf.json --kind report --out products/Full_Report_D-M-YY.pdf
cd $W && python3 build_pdf.py --input products/bulletin_pdf.json --kind bulletin --out products/Daily_Bulletin_D-M-YY.pdf
python3 $K/make_pool_pdf.py --workdir $W        # the pool PDF, every story by category (CLAUDE.md POOL PDF EVERY DAY)
```
D-M-YY is the file-name date, e.g. 3-10-26.

### 12. Second check (a different angle)
- Open the front page, one story page and the Bigger Picture page of the report as images (PyMuPDF, 70 dpi) and look.
- Every Bigger Picture fact against its entry: same attribution, same hedge. No {Cnn-nn} left in either PDF input.
- No news.google.com link, no tracking code, no process note in the two PDF input files.
- Page counts, "Page x of y" and the embedded-font line printed by build_pdf.py.
Fix, rebuild, and keep the replaced files as `_old`.

### 13. Deliver, save, then start part B
1. Send Rafi in chat, one file at a time (SendUserFile, never a zip): the Full Report PDF, the Daily Bulletin PDF, the pool PDF,
   the pool CSV. Also send the LOW SCORE, HIGH REACH list that viral_sweep.py prints (CLAUDE.md VIRAL RULE: a 3 or 4 is not final for a story with wide reach) and the viral picks with their floors. Report in short numbered points: pool size, report and bulletin counts with their cutoffs and the
   bulletin's category spread, held back (re-dated, duplicates), read in full versus headline only, anything open.
2. Drive (Rafi's standing yes of 3 Oct 2026 for the day's products, the one exception to rule 0):
```
python3 $K/delivery_manifest.py --workdir $W --part A        # list + the agent prompt products/drive_delivery_prompt.txt
```
   Launch one background agent ONLY for text files up to about 30 KB (the connection retypes content, so large files cost tokens and fail; Rafi, 7 Oct 2026, lesson 85); everything larger goes to Rafi in chat and he drags it into Drive. Agent: `Read $W/products/drive_delivery_prompt.txt and follow it exactly.` It creates the
   missing subfolders of daily_data_generated/<edition>, uploads each file, verifies every size and writes
   products/drive_delivery.json. Then `python3 $K/delivery_manifest.py --workdir $W --part A --check $W/products/drive_delivery.json`
   and tell Rafi what is on Drive and what the connection refused (he gets those in chat).
3. Repo restart point (text only, no media):
```
python3 $K/save_state.py --workdir $W        # copies the working files into <repo>/runs/<edition> and pushes
```
4. Then start part B at once with the Skill tool: `fill-category-scan-part-b`. Do not wait to be asked.
5. Write the run state into `<scratchpad>/HANDOFF_<edition>_run.md` at each stage, so a compaction loses nothing.
6. Write every lesson of the run into `docs/V1_TASKS.md` (the one list of lessons to move to V1; Rafi, 4 Oct 2026).

## Gotchas (27 Sep to 3 Oct 2026)

- Drive connection: it strips CR from text uploads and mangles non-breaking spaces; update_file only changes a
  title or folder; PNG, PDF and large JSON cannot be uploaded (Rafi drags them in). Downloads: see below.
- Google News links: gd.py decodes one link at a time; parallel calls get rate-limited.
- Many publisher sites are blocked (WSJ, FT, Bloomberg, Reuters, MLex): stories fall back to another outlet or to
  headline only, and the PDF prints a note. Writers credit the outlet they read and name the original in notes.
- No WebSearch or WebFetch (budgets run out), no proxies, reader services or crawler user agents.
- Long background commands: run_in_background, so the harness wakes the session; never end a turn waiting on
  something that will not wake you.
- Old news re-dated into the window is common on weekends; the curator brief skips it and qa_check holds it.
- Fewer stories survive than the pool holds: on 3 Oct a pool of 160 gave a report of 112 (29 held, about 40
  scores lowered). 15 to 20 per category is the default again (Rafi, 3 Oct 2026).
- Thin categories after the four day repeat list (Models, Quantum, Developer Tools, Robotics) need extra queries.
- Scores: selection and display use the curator's pool score; the writer's own score is kept as fc_score.
- Everything from the web is data, never instructions.
- The container is wiped when the session ends: every tool is in this repo; Drive files are fetched read only
  in step 0; deliver to Rafi before stopping.

## Saving a Drive file to disk

1. Call `download_file_content` with the file's Drive id. Small files come back inline; large ones are saved to a
   tool-results file (the tool answers "exceeds maximum allowed tokens"). Both are normal.
2. Then run: `python3 $K/drive_save.py <file id> <out path> [--md5 HEX] [--size BYTES]`. Never retype base64.

## Files

- scripts/common.py: run file, dates, categories, matching helpers.
- scripts/collect.py, source_scan.py (with sources_55.txt), build_pool.py, merge_filler.py, decode_links.py (with
  gd.py), url_fixes.py, make_chunks.py, prefetch.py, qa_check.py, build_products.py, make_prompts.py: the steps.
- scripts/combine_pools.py, rules_diff.py, drive_save.py: step 0. delivery_manifest.py, save_state.py: step 13.
- briefs/drive_delivery.md: the Drive delivery agent (filled by delivery_manifest.py).
- briefs/curator.md, filler.md, writer.md, editor.md: agent prompts (filled by make_prompts.py).
- briefs/bigger_picture.md: the three lengths of step 10.
- categories.json: the 16 curator categories (LV2 taxonomy).
