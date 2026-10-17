# Rules delta for edition 2026-10-17: everything that changed since the rules check of 2026-10-16
Base: commit 03bfffc (the save of runs/2026-10-16/rules_check.md); now: 6a581ff.
Read with W/rules_check_previous.md. Lines starting with + are new, - are gone.

## 1. CLAUDE.md

diff --git a/CLAUDE.md b/CLAUDE.md
index ec15f6b..f8cce5e 100644
--- a/CLAUDE.md
+++ b/CLAUDE.md
@@ -335 +335,13 @@ not about which project it is.
 35. RAFI'S WORDS OF 16 OCT 2026, ON STORIES WE COULD NOT READ (rule 8; the wording around his quotes is Claude's): when a story has no readable copy, "note than should be 'access full article on the source website / source name / link'"; "for bulletin you need one paragraph ... searching for same article and write just one paragraph about the topic"; "you can have a quick search, and also get information from sources related to the item". So: first a quick search for the same story at another outlet and related sources, then one paragraph from what was read; only a story still not found ends with "Read the full article at <source name>." (the source name and link are printed under the story). Rafi saw both versions on the real Bulletin page and picked this one ("B"). The old line "Note: we could not open the original article ..." is not printed any more (rule 32). (Mine, not yours: this reading, and the skill text and the post-build step that apply it; build_products.py is not changed until Rafi says yes to the exact edit.)
+36. RAFI'S WORDS OF 16 OCT 2026, ON PLAIN WORDS (rule 8; the wording around his quotes is Claude's): about the Bigger Picture clip that said borrowing is getting "dearer": "Stop using the word dearer!!!! ... Headlines are 5 out of 10!!! Simple fucking english. Why are you always repeating the same mistake over and over again." Every spoken line and every card line uses words an ordinary person says in daily talk, no rare or British words (not dearer, debut, watchdog; say costs more, start, regulator or the agency's name). The two wording writers read each line once for this before handing back, and the checkers check it. (Mine, not yours: the wording around his quotes and the example words.) Rafi's follow-up (16 Oct 2026, his words): "we don't want to really keep it person turn to a friend. We still want to make it news-like, but it has to be news that are very, very simple for people to understand. So the word dearer is shit. Just say, more expensive, cost more, whatever option ... and then you don't use the stupid down 5th and instead drop down 30% or whatever. All kind of examples like that." So the register is news-like and very simple, not chatty; a plain number or percent, not a fraction such as a fifth. (His message stopped at "So make sure you"; the rest is not yet known.) (Mine, not yours: this reading.)
+37. RAFI'S WORDS OF 16 OCT 2026, THE STYLE HE WANTS (rule 8; the wording around his quotes is Claude's): about the rewritten insurance clip, "In finance. The cost of insuring A I debt hit a record, which means investors fear it may not be repaid, and data centre firms like CoreWeave are hurt most.": "This is an amazing item, and that's how things should be explained. Simple English so people understand what is fucking going on. This is super. If all the news will be like that, my business will succeed." Before it, about the first version ("Insurance against tech firms failing to repay reached record prices ..."): "completely not understandable ... Explain to a person what happening". So a clip says what happened and what it means, in very simple English, one sentence, and a named person gets a real title ("Mark Levine, New York City's chief financial officer"). Whether this applies to every clip is Rafi's to say. (Mine, not yours: the wording around his quotes.)
+38. RAFI'S WORDS OF 17 OCT 2026, ON THE BIGGER PICTURE (rule 8; the wording around his quotes is Claude's): "For today, use Opus high because we're low on credit. Maybe later we're going to go back to Fable. I want to see the outcomes. So now we're going to try for maybe for the next week Fable at high, one page at maximum ... not like yesterday it was 12,000 words, about six pages of useless. It was good information, but not necessarily correct as a bigger picture. The bigger picture should summarize what is happening in the field ... We need to give an investor a clear investor tips and where the market is heading. So what is happening in the market and the conclusions."
+    So: the Full Report Bigger Picture is one page at most. Model and effort: 17 Oct 2026 Opus at high; from the next run, for about a week, Fable at high; then Rafi looks at the outcomes. This replaces "Fable at effort max" of BIGGER PICTURE MODEL (9 Oct) and the long form of the Full Report version. Content: what is happening in the market, the conclusions, where the market is heading, clear investor takeaways. The "not financial advice" line of BIGGER PICTURE WEIGHT (7 Oct) stays. (Mine, not yours: reading "investor tips" as plain takeaways and things to watch, no buy or sell calls, until he says otherwise; the Bulletin version stays at 300 to 500 words, which is under one page.)
+    RAFI'S WORDS, SAME DAY (17 Oct 2026), THE SHAPE AND THE TEST: "one page that gets all the important ... and where the market is heading, and then a list of key points of where the market is heading ... let's say 5 key points ... what's happening in the upcoming weeks or upcoming months or upcoming years, those points should be as points, even with estimations of how things can happen and what are the chances ... one point for the headline, 1 point for the card, 2 points of the summarization for the bulletin, and then the rest will appear in the full report ... for today, try to separate and build Opus at extra high and Fable at extra high, or even at max. Fable at max and then Opus at max, and compare the results, and then we decide what to use in the future."
+    So: the Full Report Bigger Picture is one page with a short summary and about 5 key points, each with horizon (weeks, months or years), the chances and the reason. Use of the points: 1 for the Headlines clip, 1 for the card, 2 for the Bulletin, all in the Full Report. Today two versions are written, Opus at max and Fable at max, and compared; Rafi decides the model after. This replaces the model line of the paragraph above for 17 Oct. (Mine, not yours: reading "max" for both; the Part B scripts that read the Bigger Picture for the card and the clip are not changed until Rafi says yes to the exact edit.)
+39. RAFI'S WORDS OF 17 OCT 2026, ON THIN BULLETIN SECTIONS (rule 8; the wording around his quotes is Claude's): the Bulletin had 1 story in each of Models, Research and Society; Claude asked whether to add the best 6s, and Rafi said "Yes!! Isnt thats our rules?" and then "Make this a rule".
+    So: every Bulletin section has at least 2 stories. A section with fewer than 2 at the day's cutoff takes its next best stories from the Full Report, a 6 first and a 5 only when there is no 6, until it has 2. This extends BULLETIN SECTIONS NEVER EMPTY (rule 14, 9 Oct 2026), which gave 2 stories only to a section with none. (Mine, not yours: reading "at least 2" as filling up to 2 and no more, so a section is not flooded as Politics was on 9 Oct; the Fun Side keeps its top 3; build_products.py is not changed until Rafi says yes to the exact edit, so until then Part A step 8 does it with the run-folder filter, as on 17 Oct.)
+    RAFI'S ANSWER, SAME DAY (his words): "Ok for 4 ..dont overload the bulletin so 2 or 3 is enough if that category is weak". So the fill-up of rule 39 stops at 2 or 3 stories for a weak section, never more; the "up to 2" reading above is replaced by "2 or 3". (Mine, not yours: reading "Ok for 4" as agreeing with point 4 of my message, the fill-up reading; Claude picks 2 or 3 by how many good stories the section has.)
+40. RAFI'S WORDS OF 17 OCT 2026, ON REDESIGNING THE BIGGER PICTURE AS AN INVESTOR PRODUCT (rule 8; the wording around his quotes is Claude's; said on a bicycle, by voice): "To be honest, I think they're both not doing the right job. If I want to give a product for investors to save them money in doing the work themselves ... one page that's called Investor Watch or the bigger picture, and that should have a real meaningful effect of what is happening in the market in the next week, in the next month, in the next year, or in the next 3 years ... I want my customers to be able to find the next Nvidia, to be able to find the next Micron, or the next upcoming either trends or demands ... about a month ago ... magnets started going up because robotics need magnets ... if we count all our pool articles, or we look at the past of our items ... connecting all the threads, what is happening throughout all the items ... and then predict the future, give it chances."
+    His rulings after: "we do not give prediction, but trend is not a prediction. If we give an item saying it would be important and there's big chances that memory will rise because demands from this and this and this happening, then we don't give names of companies, we just give what's happening, and that's good enough. We can put charts if needed ... one like every week on Friday, give a big final report, like a weekly report ... it's okay to repeat points during the week ... we can point it out that this point is coming up again."
+    So: the new product gives trends and chances, no company names, charts allowed, a big weekly report every Friday, and points may come back during the week marked as coming up again. Not built; the one page of rule 38 stays as it is until he decides. Claude offered three options (a trend counter on the pool history, a research helper that follows a rising theme outside the news, the Friday report), recommended the first two as one test edition, and waits for his yes. (Mine, not yours: the wording around his quotes and the three options; on 17 Oct the pool history held 17 days and the magnets story showed 3 times, so the pool alone cannot find a theme like that; a lawyer check on naming companies is advised, and he has ruled no names.)

## 2. docs/V1_TASKS.md: added or changed lines (new lessons and ADDED notes)

+317. (16 Oct, Part B, Rafi angry) THE BIGGER PICTURE CLIP SAID BORROWING IS GETTING "DEARER". Headlines and cards are level 5 out of 10, plain daily English; the writer, the script check, the Fable checker and I all let a British word through, and I read the lines before sending without testing for it. Prevention: the wording brief now has a PLAIN WORDS line and each writer reads every line once for it (CLAUDE.md rule 36); the checkers check it; I read every line for rare words before sending, as a separate pass. Fix applied: both writers replace the word and review all lines, then the same checkers confirm.
+318. (16 Oct, Part B, Rafi's decision, not a rule) BREAKING TESLA FLYING ROADSTER, ADDED AFTER THE SCAN WINDOW. The story broke 7 to 12 UTC, after the 04:54 UTC window, so no product had it. Rafi's choice: one extra Headlines clip played first and one extra card without a number, nothing else regenerated. Built as separate files: a one-clip JSON (and a two-part JSON of 8.5 s each), and one card rendered inside a copy of the full edition with a local copy of the renderer that takes a label field (BREAKING NEWS instead of STORY nn / 14). The gate's rule that every clip story is also in the Bulletin was skipped for this story at his word. Footage: no reuse licence was found (Tesla's pages block the cloud session with 403; the shorts show no Creative Commons mark; credit alone is not permission); 8 outlets checked, most host Tesla's footage in their own player, Euronews credits it "Copyright @Tesla". Rafi chose to put a Tesla clip on the screen with the credit "Copyright @Tesla" (same as Euronews), at his own risk; the download and the stitch happen on his PC in the local chat. Sources of the official clips: Tesla's YouTube shorts "The Ramp" and "The Kickflip" and the "Roadster Event" video.
+319. (17 Oct, Part A, my mistake, caught before any product) A VIRAL STORY THAT RAN YESTERDAY AT 8 WAS SENT TO THE CURATORS AS "MUST INCLUDE". viral_sweep.py printed "RAN BEFORE" only for one cluster; I checked the other clusters against the earlier pools by title words only ("muse spark"), and yesterday's titles said "open-weight AI model that runs on Macs" and "Muse AI models", so Meta's Muse Spark Open (16 Oct C01-01 at 8, C06-02 at 7, and in the 16 Oct Bigger Picture) went to the Models curator with a floor of 7. I also first judged the RTX Spark on-sale story a meaningful update without reading the 16 Oct report, which had already printed the sale date and the early test limits. The Models curator's own note caught the first; then I grepped the 14 day reports. Fix applied: clusters 4 and 6 went into viral_exclude.json, the Muse pick was dropped (drops.json), the Chips curator was told before it finished. Prevention: before any floor goes into prompt_extra.json, grep each viral cluster's key names and numbers (for example "816", "Muse", "on sale") in archive14 for the last 3 days, not only pool titles; for a story that ran at 7 or more, the "meaningful update" call of CLAUDE.md rule 34 is made only after reading the earlier report lines.
+## Part 10: open items from all chats of 10 to 16 Oct 2026 (collected 17 Oct 2026, Rafi's ask: "collect all the open topics ... into one chat so I'm not gonna have to jump between windows")
+Read by helpers from the cloud chats of 10, 11, 12, 13, 14, 15 and 16 Oct (Part A), the 11 Oct Part B chat (the PC chat, 8 to 16 Oct), Comfy work review (12 to 15 Oct), Scan efficiency (13 to 15 Oct), Postiz (15 Oct) and Setup check (13 Oct, nothing open). Some early hours of the 10, 12, 13 and 14 Oct chats were read only through their summaries. Repeats across chats are merged; items about one past day's product (a line, a card, a screen of that day) are dropped as stale. Status is as of 17 Oct; nothing here is decided.
+### A. Rules and clashes, for Rafi to decide
+A1. Rule 14: every Bulletin section at least 2 to 3 stories, going down to 6, or 5 if no 6; replaces "exactly 2" (Rafi 16 Oct: "yes for the next runs"; exact wording waits for his yes).
+A2. The rule clashes found by the rules check and the audit (18, from 13 and 14 Oct), the six CLAUDE.md clashes of 10 Oct, and rule 8b item 7 (one check round) against "nothing goes to Rafi with a rules FAIL". Rafi: clashes last.
+A3. Preferences clash: VOICE WALKTHROUGH (one item, then stop) against ANSWERS IN POINTS (all in one reply).
+A4. Rafi's "fix everything" against CLAUDE.md rule 4 (one fix at a time) and the scripts-only-between-runs line of rule 16.
+A5. CLAUDE.md rule 21 (lessons only in the repo) against the Drive "Claude to ChatGPT Sync Checkpoint Protocol" (a CLAUDE_HANDOFF file for ChatGPT).
+A6. Viral rule against the repeat rules (Gemini 4 and Musk, lesson 286): rule 34 answers part; skill step 1c and viral_sweep.py wait for his yes.
+A7. What goes into the repo per day: text only, text and PDFs, or everything with cards; clashes with rule 0 "no media" and rule 9.
+A8. Reference image 2: Drive says "fists", the script uses smile_v4; "smile is fine" was never written down.
+A9. Comfy rulebook clashes: 6 against 8 steps, "don't round up" against round up to half a second, the old boundary mock v9.
+A10. Two Codex V1 pipeline copies (OneDrive, 11 Oct, against E: drive, 27 Sep): which one is the real one.
+A11. May writers move a story to another category, or does the curator's category stay?
+A12. Stories whose event happened before the scan window: count only events inside the window?
+A13. Standing permission for gate script edits the day Rafi gives a new rule.
+A14. Full review of the process against Rafi's own words: which rules are Claude's additions, what can be cut without losing quality (Rafi: later).
+A15. Does rule 37 (say what happened and what it means) apply to every clip?
+A16. Write Rafi's 8 Oct customer text rules into CLAUDE.md?
+A17. Lesson 318 and its handoff note: keep or remove (Rafi 16 Oct: "lets see if it will disturb us").
+A18. "Name the item for what it truly is" for politics labels: how to apply it.
+A19. Two scans fill the same Drive day folder: which run is the day's product.
+A20. A plan so the chain runs without Rafi's decisions, only critical ones.
+### B. Script and skill fixes waiting for Rafi's yes (scripts change only between runs)
+B1. The 12 Oct edit list for 8 Headlines clips and 13 to 15 cards.
+B2. A standing rules check that tests only what changed (Rafi: "very important", later).
+B3. A time limit in every helper brief, and never wait idle for a helper (lessons 262, 263).
+B4. Five fixes for side effects of the Group 1 efficiency changes (viral check, "never open scripts", rule file reading, CLAUDE.md reread, PDF tool check).
+B5. Last week's Bigger Picture texts in the fact checker pack.
+B6. New checks: unexplained spoken short forms (I M F); a named person with no title (lesson 307); a stranger plain English check; brief examples that break a script check; the 18 rules with no script check, one at a time.
+B7. A model check at the start of a run that stops on Haiku (13 and 14 Oct ran on Haiku).
+B8. Repeat checks: read past reports from the repo first, not Drive; a stricter match (26 of 43 flags false on 14 Oct); run collect after the four day repeat list (bug, wrong order 14 and 15 Oct, lesson 278).
+B9. Bulletin build: an exact number per section (lessons 301, 14 Oct cap).
+B10. Fill drift: build the fill after the holds, editor C for new fill ids (lesson 302).
+B11. Viral check false FAILs: title mismatch, shared Google link (Harmonic and Labelbox).
+B12. The script does not check scores set by a helper's own count.
+B13. save_state.py: old session link hard coded.
+B14. The pool markdown file name has no date (clashes with earlier days).
+B15. Rule 35 into build_products.py (the skill post-build step does it for now).
+B16. Stale lines: fill_headlines.py screen prompt "no people, no faces"; review list intro "no text and no people".
+B17. Customer PDFs: remove "test edition" and the source count lines, add "Page N" in the contents.
+B18. Check that the PDF tools installed before Part A step 11.
+B19. The "markets share of this analysis" sentence in the Full Report Bigger Picture (Rafi said remove, 15 Oct; not done in the builder).
+B20. About 20 small fixes from the lessons, and the 24 lessons written but not built (12 Oct audit).
+B21. Lean main chat did not work: count questions, helpers still run git status.
+B22. Part A writers read the rules once in two categories (lesson 315).
+B23. Two day-folder Bulletin scripts of 13 Oct not moved into the repo.
+### C. Speed, cost and models
+C1. The Group 2 efficiency list (15 items): effort for curators, fillers and Part A writers; Part B writers medium or high; rules read once in Part A; Bigger Picture on Opus high or started during the editors; drop the regional search; thin days write score 4; slimmer CLAUDE.md; Part B in a fresh chat; one approval stop in Part B; and the items in B.
+C2. Model test decisions: writers on Sonnet high or Opus medium; curators on Sonnet medium plus an old news check; Fable low for top stories only; a detail line for Sonnet low writers.
+C3. Tests never judged: the faster Part B writers; Part B writers medium against high on the same stories; the 15 Oct Sonnet medium run against the 13 Oct backup; the chain fix rollback (options 1, 2, 3).
+C4. Rafi's target of a 20 minute scan with a report: 14 Oct took 106 minutes; no target agreed.
+C5. A word limit for the Full Report Bigger Picture (about 12,300 words on 15 Oct; lesson 303).
+C6. The Fable check cheaper, later.
+C7. Rafi's question never answered: "why would Sonnet just figure things out the best way?"
+C8. The model test walkthrough stopped after lesson 3 of 8.
+### D. Repo and saving
+D1. The 13 Oct run is not in the repo (runs/ has no 2026-10-13): Rafi's yes in the 13 Oct chat, or the 13 Oct pool from his PC.
+D2. The 13 Oct chat holds 50 old local commits on a stale copy; push options never picked.
+D3. Backup tag backup-claude-partb-2026-10-11 never pushed.
+D4. PC scripts of 13 to 16 Oct (tvwall.py, realglow2.py, fix_wall_v8 and v10, breaking and footage scripts), the TV spec and its reference PNG are not backed up in the repo.
+D5. Lessons not yet in this file: the PC chat's of 12 to 16 Oct, the 14 Oct chat's (fun line passed 3 checks, chain fix, Haiku start, PC app archive), the 12 Oct Comfy line (take only Comfy technical knowledge from other projects).
+D6. docs/DRIVE_DIFFS_FOR_CHATGPT.md: ten differences missing, three old lines.
+D7. Reports of 1, 2 and 13 Oct missing for the 14 day old news check.
+### E. Drive (only on Rafi's order, rule 0)
+E1. Claude's Drive duplicates (aind_caption_effects.py, AIND_lessons_11-10-26.md, four tools in the 10 Oct supportive files, five files in all): rename _superseded and archive (Rafi 13 Oct: "rename and move to archive!"); not shown done.
+E2. Missing products on Drive: the 21 files of 10 Oct, the 13 Oct PDFs, the products audit.
+E3. "dearer" still in the Drive phrasing sheet (two examples); rules G7 item 3 still credits the teaser to the old report name; the Drive Project Task List out of date since 2 Oct; four tools of 10 Oct never compared with the repo.
+E4. The automatic Drive upload (waits for the Google Cloud key from ChatGPT's account).
+E5. Send the repo lessons to Astra on Drive (Rafi: later).
+### F. Video, PC and ComfyUI
+F1. Tesla permission email to press@tesla.com (Rafi sends it).
+F2. Verdicts waiting: 16 Oct main video (three spots: C02 at 5.7 s, C07 at 6.4 s "its its", end of C04); 16 Oct breaking video v2.
+F3. The official V1 stitcher: the handoff to ChatGPT not sent; old opening and ending, fixed _ChatGPT-V1 label; Claude's stitch effects (cyan word, rolling strip, full screen date, footage, stutter mute, TV method, BREAKING strip) not merged.
+F4. Real footage in the daily stitch: not built; licences.
+F5. Small look questions: the 13 Oct ending "looks like a kid made it" (card or ending clip); the opening date in the DIN broadcast font; a more realistic warning sign; new skills, apps or connectors for Claude's editing.
+F6. Source facts of posted videos never verified (13 Oct C10 Bloomberg, 12 Oct C05, 14 Oct latte).
+F7. The V1 Headlines writer lets hard wording through ("fell a fifth", semicolons, on-screen text prompts).
+F8. PC stability: 0x4E blue screen after the BIOS update; XMP off and a RAM test advised; crash cause not confirmed; no test render since.
+F9. ComfyUI tests and fixes: Sparse Attention node, ComfyUI 0.40.0, the 8 step H3 speed LoRA, the Spectrum node, tests A to E, opener audio fix and the 4 s voice reference, VRAM thrash, the Qwen editor black output, "Takaichi" pronunciation, the desk reflection.
+F10. ComfyUI ideas waiting for a go: audio-first lip sync, Xenia face and studio LoRAs, a HeyGen-style avatar, H3 clip chaining, Alpha-Gen matte, a backup lip sync tool.
+F11. PC housekeeping: 14 stalled .part downloads (needs yes); the broken 13 Sep chat (save the summary or check Windows Previous Versions); stray Temp scripts; Comfy knowledge from other chats only partly collected.
+F12. How the local chat keeps all repo rules in mind.
+### G. Social posting and small questions
+G1. Postiz: where it runs (Google Cloud, a cheap server, hosted, the PC); which platforms first; access to Google Cloud; Drive media access; cloud chat posts cards and PC chat posts video; compare Mixpost, n8n, direct APIs; platform approvals take days; rule 33's "3) doesn't matter" unclear.
+G2. Post text: where it lives, who writes it, closing question, hashtags, emojis, a short X version.
+G3. Renting a 5090 for ComfyUI (RunPod, Vast.ai).
+G4. A list of every fun story Rafi says yes or no to, so the picker learns what is funny.
+G5. A real xlsx of the pool, or is the CSV enough?
+G6. Five small questions: France 24 credit, MarkTechPost feed, keep the regional search, the XPeng card note, the crab clip credit (Digitec or KingKong Robotics).
+G7. The token counter jumped back to 15 million on 15 Oct: a compaction?

## 3. Skills and briefs (scripts listed by name only)

.../skills/fill-categories-scan-part-a/SKILL.md    |  2 +-
 .../briefs/bigger_picture.md                       |  7 ++++
 .../briefs/bigger_picture_old_17oct.md             | 45 ++++++++++++++++++++++
 .../assets/headlines_model_lines.md                |  5 +++
 .../briefs/wording_common.md                       |  2 +
 5 files changed, 60 insertions(+), 1 deletion(-)

diff --git a/.claude/skills/fill-categories-scan-part-a/SKILL.md b/.claude/skills/fill-categories-scan-part-a/SKILL.md
index 1eaa88b..f3de2ee 100644
--- a/.claude/skills/fill-categories-scan-part-a/SKILL.md
+++ b/.claude/skills/fill-categories-scan-part-a/SKILL.md
@@ -179,3 +179,3 @@ FILL DRIFT (10 Oct 2026, lessons 164, 185): every added or held story changes wh
 lands near 30 to 50 (usually 6, 7 or 8 and up), plus the top 3 Fun (CLAUDE.md rule 14; 3 Oct 2026 Rafi chose 7
-and up). Read the "CHECK bulletin spread" line: a category with no story is stated to Rafi with the count.
+and up). Read the "CHECK bulletin spread" line: a category with no story is stated to Rafi with the count. EVERY BULLETIN SECTION HAS AT LEAST 2 STORIES (Rafi, 17 Oct 2026, CLAUDE.md rule 39): a section with fewer than 2 takes its next best from the Full Report (a 6, a 5 only if no 6), to 2 or 3 and no more (Rafi, 17 Oct 2026: "dont overload the bulletin so 2 or 3 is enough if that category is weak"), before the PDFs are built; on 17 Oct this was done with a run-folder filter (bulletin_keep.py, bulletin_keep.json, build floors MOD=6,RES=6,SOC=5) until the build script is changed.
 
diff --git a/.claude/skills/fill-category-scan-part-b/assets/headlines_model_lines.md b/.claude/skills/fill-category-scan-part-b/assets/headlines_model_lines.md
index e36113a..a02e55f 100644
--- a/.claude/skills/fill-category-scan-part-b/assets/headlines_model_lines.md
+++ b/.claude/skills/fill-category-scan-part-b/assets/headlines_model_lines.md
@@ -53,2 +53,7 @@ The difference every time: one actor, one verb, one why. Examples, second detail
 
+## Examples from 16 Oct 2026 (Rafi's own words or lines he approved; examples only, they change no rule above)
+1. In finance. The cost of insuring A I debt hit a record, which means investors fear it may not be repaid, and data centre firms like CoreWeave are hurt most. (Rafi: "an amazing item, and that's how things should be explained. Simple English so people understand what is going on.")
+2. In robotics. Swedish car maker Volvo plans hands-free driving using N-vidia's A I by twenty thirty. (Rafi's own wording for that one item: "That's it. Not more, not less.")
+3. In politics. Mark Levine, New York City's chief financial officer, asked anthro-pic to delay its stock market debut and deal with A I safety first. (Rafi: name the man with his real position.)
+
 ## Never like this (lines Rafi rejected, and why)

## 4. Drive rule files (W/rules against runs/2026-10-16/rules)

no change
