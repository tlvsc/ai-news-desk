# Handoff 2026-10-17 Part A (a file to continue the work, not a source of truth; rules: CLAUDE.md, lessons: docs/V1_TASKS.md)

W=/tmp/claude-0/-home-user-ai-news-desk/6580d523-b769-5244-8c8f-b7cc2b9a5a86/scratchpad/run_2026-10-17
Window 2026-10-16T07:44Z to 2026-10-17T07:44Z. Collect 3950 rows, sources 249.

Done: step -1 (up to date 66a992f), step 0 (rules same as 16 Oct, build_pdf md5 OK, storage check OK; 13 Oct pool and report not on Drive, gap),
repeat list = pools 12, 14, 15, 16 Oct (1010), archive14 = 13 of 14 from repo runs/ (gap 13 Oct).
Viral: 6 clusters; #3 excluded (false match, mixed data center stories); floors in prompt_extra curate for
cat 13 (China export controls 50; Anthropic safety bill 29), 11 (Waymo Toronto 41), 1 (Meta Muse Spark Open 29),
8 (RTX Spark on sale and reviews 28, meaningful update of 16 Oct C08-16 at 7, rule 34).

CORRECTION: Muse Spark Open ran 16 Oct at 8 (C01-01) -> cluster 4 excluded, dropped from cat 1 (drops.json);
RTX Spark sale date and early tests were printed 16 Oct -> cluster 6 excluded, cat 8 curator told before it finished.
viral_exclude.json = clusters 3, 4, 6. Floors: China export C13-01 8, Waymo Toronto C11-01 7, Anthropic bill C13-02 8.
Done: curators, robot pass (12 merged), pool 247 (drops: Muse, AWS CFO dup in cat 7). Short by 1-2, no filler: cat 3 14, cat 7 16, cat 13 17.
Done: decode 247/247, chunks 202, prefetch 111 readable, 16 writers, qa_check (held 28 stale; C11-19 unheld as first report;
duplicates C11-05, C16-07 added by hand to held.json; DO NOT rerun qa_check, it rewrites held.json; backup held_qa1_old.json).
Build flags: --report-min 6 --bulletin-min 7 --bulletin-min-cat HEA=6,SOC=6,ROB=5 --report-fill-to 110, then ALWAYS
python3 $W/bulletin_keep.py $W (bulletin_keep.json: Robotics C11-01, C11-03, C11-04, C11-09 humanoid). Report 110, Bulletin 32.
dup14: 13 of 14 (gap 13 Oct); 11 REPEAT flags in the report read, none real; C09-04 to name 7 Oct story (Editor A told).
Editors done: B 3 re-dated held; A 11 unresolved -> held C12-05, C12-10 (before window), dup C03-04, C08-04, C07-04, C07-07, C05-14;
kept C02-02 (reworded), C12-08, C09-02. A also checked C02-08, C12-12, C12-14 (fill). LOCKED: --report-fill-to 100 -> report 100, all
editor checked (report_ids_checked.json = first 110); bulletin 30 after bulletin_keep. 11b script ready: $W/notfound_note.py (9 notes).
Running: Bigger Picture (fable max).
Next: act on qa2 logs, rebuild, set fill-to to the count, Bigger Picture (fable max), final build, 11b, PDFs, checks, deliver, save_state, Part B.
Open for Rafi (delivery report): clusters 3, 4, 6 excluded with reasons; Tesla Roadster (16 Oct breaking extra only) is in cat 5.
LESSON to write: check each viral cluster against the 14 day reports by topic words, not titles (Muse almost re-ran).
