# Rules check, Part B (cards and Headlines), edition 2026-10-10 (SAT 10 OCT 2026)

Written by the rules checker (Opus) at about 11:20 UTC, Part B step 0c. Read in full: CLAUDE.md (260 lines, the file on disk; its VIRAL RULE is the 10:55 UTC text of commit accc952), docs/V1_TASKS.md (516 lines, lessons P1-1 to P1-35, 1, the porting list 1 to 12, 13 to 176, D1 to D9), docs/DRIVE_DIFFS_FOR_CHATGPT.md (20 entries), the Part B SKILL.md (196 lines), and W/rules: Cards_Master_Rules_Structure.txt, Headlines_Master_Rules_Structure.txt, Headlines_prompt_for_comfy_json.txt, Article_phrasing_instructions_AIND_V1.txt, Full_Report_V1_Rules_Structure.txt, Bulletin_V1_Rules_Structure.txt (rules/_diff_B.txt: all six the same as 9 Oct).
W = /tmp/claude-0/-home-user-ai-news-desk/df59d67d-a5b7-5aa2-97f7-5f66358ede71/scratchpad/run_2026-10-10

State when written: step 1 not done. cards_work holds pick_pack.json/.md (39 Bulletin candidates, 75 reserve, decks of 7 of 7 days, 3 to 9 Oct), selection_draft.json (card_candidates.py paper input: 12 story cards plus fun, no Politics or Research card, 1 robotics card), prompt_picker.txt, update_allowed.json = ["C01-16"]. No selection_fable.json, selection.json, wording, pack or JSON yet. So most lines below name the check to run at step 7.

## Facts of this edition used below (all from W unless named)
- Bulletin (products/bulletin_pdf.json): 39 stories. Politics 2 (C05-01, C05-02, both score 6, both FOLLOW-UP of 9 Oct cards), Market 4, Security 4, Energy 3, Robotics 5 (C11-01 7, C11-16 7, C11-05 5 not read in full, C11-10 5, C11-13 5), Models 6, Research 1 (C04-01, not read in full), Ethics and law 3, Health 3, Society 5, Fun 3. Purpose line has no internal codes.
- Full Report (products/report_pdf.json): 114 stories, 11 sections, Fun 7. held.json: 32 re-dated plus 8 duplicates or repeats.
- Highest score today 9 (C01-16, C12-14): no critical (10) story.
- Viral (viral.json, 20 or more outlets): C12-14 OpenAI firing (9; ran 8 Oct as C12-01 at 7 and 9 Oct as C05-01 at 7, so the VIRAL re-run clause does not cover it), C12-01 Anthropic false police tip (8, NEW), C01-16 cruelty ban (9; ran 9 Oct at 5 and 3: re-run allowed, and Rafi named it), C07-07 Firmus (7; ran 9 Oct as C06-01 at 8 and sat in the 9 Oct Bigger Picture card and clip: re-run clause does not cover it), C11-16 Tesla rename (7; ran 9 Oct as C11-12 at 5: one re-run allowed; its entry says NEW).
- Robotics read in full with machine_action true: C11-10 Zipline drones (Bulletin, 5), C11-12 L3Harris Wolf Pack (report only, 5). Robotics at 7 (C11-01 Stellantis and Wayve, C11-16 Tesla rename) have machine_action false. Humanoid robot stories: C11-03, C11-04, C11-09 held; C16-03 (humanoid Garba dance) is Fun at 2. Eligible humanoid robotics card today: 0.
- Politics: no eligible Bulletin story (both are updates). Reserve, new and read: C13-03 (6, Reuters), C13-05, C13-07, C13-09 (5).
- Research: Bulletin C04-01 not read in full. Reserve, new and read: C04-03 (6, Anthropic), C15-01 (6), others at 5.
- Non-update, read-in-full Bulletin stories at 7 or more available as extra cards: Security C12-02, C12-03; Models C01-01, C02-02; Ethics and law C08-01; Robotics C11-01, C11-16 (no machine). Market, Energy, Health, Society have no second story at 7 that is not an update.
- Previous day's introductions (runs/2026-10-09/headlines_work/scripts_final.json): "First", "In India", "On trade", "In security", "Next", "In tech", "In education", "And now, something lighter".
- Scores: card_candidates.py shows pool scores (selection_draft.json: C01-01 8, C09-02 7, C14-01 7); report_entries hold 7, 6, 6. pick_gate.py and the products use the entry score.
- Branch claude/eager-archimedes-ajnex3; no uncommitted change under the Part B scripts.

## 1. One line per rule and lesson

### 1a. CLAUDE.md rules
CLAUDE.md 0 (Drive read only): no Drive create, upload, rename, move or edit except the daily delivery -> Part B touched Drive only to read rules (rules/_fetched_B.json, AIMD file, modified 2 Oct); check at step 8 that only delivery writes happened.
CLAUDE.md 0 DAILY DELIVERY: products into daily_data_generated/2026-10-10, sizes verified, never overwrite; text copy in runs/2026-10-10 -> step 8: delivery_manifest.py --part B then --check; save_state.py before the step 7 wait and after delivery. The morning Routine: not applicable (needs two clean manual days).
CLAUDE.md 1 (route the job): not applicable to the checks: the route is set (cloud session for Part B, ComfyUI on Rafi's PC for video, lesson 123).
CLAUDE.md 2, 15 and 8b item 5 (short replies, one sentence, simple English): the step 7 message is the sheet, the review list and a one-line ask; no shorthand (lesson 90) -> read the message before sending.
CLAUDE.md 3 (no deletions): replaced outputs renamed _old; fill_headlines.py refuses to overwrite; each render goes to a new cards_runN -> check ls for _old names, no rm used.
CLAUDE.md 4 (one fix at a time): Rafi's edits after step 7 applied and shown one change at a time -> step 7 edits loop.
CLAUDE.md 5 (evidence): report card files counted against the list (assemble_cards.py), JSON size and md5, active slots and seconds (verify_headlines.py) -> step 7 and 8 numbers.
CLAUDE.md 6 (no invented content): every card and clip fact from report_entries/<id>.json and facts/<id>.json (briefs/wording_common.md) -> step 4 claim-by-claim read.
CLAUDE.md 7 (Claude cannot judge rendered output): the contact sheet is checked for counts and cut-offs; visual judgement is Rafi's -> send the sheet first.
CLAUDE.md 8 (every instruction into CLAUDE.md): any instruction Rafi gives in Part B is written into CLAUDE.md the same day. Gap found: the 7 Oct MUST-HAVES (every category a card, reserve exception) live only in briefs/pick_stories.md (clash 1).
CLAUDE.md 8a (two rules touch: stop and ask): section 2 lists 6 clashes and section 2b 14 brief or script conflicts -> the main session asks Rafi once, all together (lesson 142), and waits.
CLAUDE.md 8b item 1 (a question is not a decision): no recommended fix in section 2 is applied before Rafi picks it.
CLAUDE.md 8b item 2 (never put one rule's opposite into a model brief): section 2b lists the brief lines that do (15 word cap on Headlines, 48 and 53 syllables, 12 s, "text-free symbol", "No people, no faces").
CLAUDE.md 8b item 3 (check against every rule and the last 7 days before showing): this file plus the step 7 checklist; pick_gate.py G17 over 7 of 7 decks; the 3-day table.
CLAUDE.md 8b item 4 (a count Rafi gives wins over a cutoff): 14 story cards, 7 clips, 2 robotics cards, 1 robotics clip, C01-16 as card and clip -> state how each was met; see clash 2 for extra_min.
CLAUDE.md 8b item 6 (every named person with position and organisation; every name introduced): G15b novice_test at choice, then read every card and clip.
CLAUDE.md 8b item 7 (one check round, one rewrite round, then show what is left; cheapest path): one stranger round and one rules round per product, one rewrite round -> see clash 6.
CLAUDE.md 9 (skills only in the repo branch, media out of git): branch claude/eager-archimedes-ajnex3 confirmed; save_state copies text only -> check git status shows no PNG or MP4 staged.
CLAUDE.md 10 (branding in post): screens carry no logos or brand marks; the card wordmark is drawn by the renderer -> rules agent reads every screen line.
CLAUDE.md 11 (subtitle canvas): not applicable: subtitles are made on Rafi's PC after generation.
CLAUDE.md 12 (subtitle approval pause): not applicable: after generation, on Rafi's PC.
CLAUDE.md 13 (Windows double-click scripts): not applicable: Part B scripts run only in this cloud session.
CLAUDE.md 14 COUNTS ARE GUIDELINES: card target 14 is a working target, state the number, never stop to ask about a count -> state the final count; see clash 2 (8b item 4 versus this line).
CLAUDE.md 14 BULLETIN SECTIONS NEVER EMPTY (step 7 recheck of Part A products, skill 0c item 4): 11 of 11 Bulletin sections hold stories; Politics holds exactly 2 at 6 (none at 7) -> PASS.
CLAUDE.md 16 scan window, SOURCES, PER CATEGORY, 3 OCT RUN, BIG OUTLETS, WRITE ONLY WHAT CAN PRINT, POOL PDF: not applicable: Part A (done; pool 240, AIND_Pool_10-10-26.pdf delivered).
CLAUDE.md 16 Fun Side: 5 to 10 in the report, top 3 in the Bulletin -> report Fun 7, Bulletin Fun 3: PASS.
CLAUDE.md 16 Cards and Headlines counts: story cards from the CARD FILTER, 7 to Headlines -> pick_gate.py G2 (14 or 15 cards, 4 teaser items, 7 clips).
CLAUDE.md 16 news part about 90 s (7 stories 8 to 9 s, fun 8, teaser 8, Bigger Picture 10; opening and ending on top) -> check_wording.py prints the news part total; verify_headlines.py "news part".
CLAUDE.md 16 rounding: every clip rounded UP to the next half second -> fill_headlines.py box_seconds (ceil) and its own assert on node 13.
CLAUDE.md 16 company limits (in CARD FILTER) -> pick_gate.py G9 (3 cards), G10 (2 clips); check_headlines_rules.py C16 (2 story clips).
CLAUDE.md 16 delivery of everything final; what the connection cannot take goes to Rafi in chat -> step 8 manifest; PNGs and JSON in chat.
CLAUDE.md 16 READER LEVEL (only in the phrasing file; re-read 1, 1A, 1B and the product section before each item; who, what, why) -> cards level 6, Headlines level 5 (rules/Article_phrasing_instructions_AIND_V1.txt); the line is in wording_common, wording_headlines and rewrite briefs; stranger 1b checks who, what, why.
CLAUDE.md 16 CLIP SECONDS (4.4 syllables a second, round up, aim 8, never over 10 = 44 syllables) -> check_wording.py FAIL over 10 s; check_headlines_rules.py B1. Brief conflict: wording_headlines.md allows 48 and 53 syllables (section 2b).
CLAUDE.md 16 CREDIT (the outlet that reported, never a copy site; "X reports, citing Y" when unclear; Bigger Picture card label AIND, source strip AI News Desk) -> build_cards_copy.py writes 'The Bigger Picture / AIND', pill AIND, src 'AI News Desk'; card SOURCE lines copy the entry source raw: C11-10, C11-12, C11-13 carry "relayed by" (section 2b) -> read every SOURCE line at step 7.
CLAUDE.md 16 REPLY STORIES (who answers whom, name and explain the earlier story) -> check_wording.py reply check; the Musk reply to the cruelty ban (C05-09), if used, sits on the C01-16 card and clip and says who answers whom.
CLAUDE.md 16 HEADLINES RULES RECHECK (script plus rules agent before Rafi sees the lines; intros never the previous day's) -> check_headlines_rules.py (rules_check.json fails 0) and the Opus rules agent (rules_result.json) on the current lines; G2 list above.
CLAUDE.md 16 MODEL POLICY (Sonnet bulk; Opus for editors, stranger, rules agent, rewrite agent; never Haiku) -> stranger and rules agents on model "opus"; no Haiku anywhere; rewrite agent model: clash 4.
CLAUDE.md 16 STORY CHOICE (Fable picks and writes; script gate; Rafi approves the list before wording; Opus final audit per product with PASS or FAIL and evidence; token use per stage) -> picker on model "fable"; pick_gate.py gate PASS; approval time earlier than cards_copy_fable.json and scripts_fable.json; Opus audit at step 7; tokens per stage in the final report.
CLAUDE.md 16 BIGGER PICTURE MODEL (one agent writes all three lengths, Fable at max; the main session never writes it) -> bigger_picture.json and bigger_picture_bulletin.json hold only the report and Bulletin lengths; check who writes the Bigger Picture card and clip and say it (best: the Part A Bigger Picture author, Fable).
CLAUDE.md 16 HAIKU TODAY ONLY: not applicable (8 Oct 2026 only).
CLAUDE.md 16 SCRIPTS STAY AS THEY ARE DURING A RUN -> no script edited (git diff of scripts empty at 11:16 UTC); fixes go into list files (update_allowed.json, gate_overrides.json, rules_overrides.json) and skill text.
CLAUDE.md 16 HEADLINES SHAPE (the phrasing file shape; check_wording.py fails a line that breaks it; a fix is shorter) -> check_wording.py all pass on scripts_final.json; rewrite lines no longer than the old ones (count syllables old against new).
CLAUDE.md 16 WHO WHAT WHY FIRST (who, what, why_for_people filled before each line; why spoken; main session never rewrites a line; gate refuses JSON and review list unless checks passed on current lines) -> check_wording.py "missing" and "why is not spoken" checks; common_b.rules_gate in build_pack.py and review_list.py.
CLAUDE.md 16 HEADLINES ORDER (order and choice only from the Drive Headlines Master) -> clips in deck order: G11 and A3; choice: clash 3.
CLAUDE.md 16 HEADLINES INTROS AND FLOW (intro names its topic, natural order, never twice, never a label unrelated to the topic; prefer AI affecting people among non-politics stories; fun funny at once; every JSON clip generated except opening, ending and spare slot) -> check_headlines_rules.py B2a and G2; rules agent reads each intro against its topic; pack slots 1, 12, 13 bypass, 2 to 11 active.
CLAUDE.md 16 REAL TV SCREENS (realistic TV-news scene of the story's subject; no readable words, numbers, logos or real named faces; Bigger Picture keeps its warning sign) and FUN CLIP (set-up then punchline, facts only from the source) -> read every "screen" line and the fun line; the fill prompt still says "No people, no faces" (lesson 140): write screens without people.
CLAUDE.md 16 NO OLD NEWS (cards and Headlines only from what survived the 14-day check) -> every id in report_pdf.json and not in held.json (G1).
CLAUDE.md 16 CARD FILTER (category order from the Drive Cards Master; criticals first; best story per category at base_min 5; extras at extra_min 7; max 2 per category, market 3; read in full; robotics card shows a machine doing something) -> G7, G8, G5, G13; extra_min is not tested by the gate: read the scores; clashes 1, 2, 5.
CLAUDE.md 16 CARDS FROM THE BULLETIN (cards only from Bulletin stories; target 14) -> G4 and G4b exceptions; clash 1 for Politics and Research.
CLAUDE.md 16 NO UPDATE CARDS (an update is a card only if Rafi named it; compare every card with the last 3 days of cards and Headlines by name and topic and show the table) -> update_allowed.json = ["C01-16"]; G6 covers cards, clips and teaser; the 3-day table (7, 8, 9 Oct) goes to Rafi with the deck.
CLAUDE.md 16 NO REPEATS IN 7 DAYS -> G17 over decks of 3 to 9 Oct (7 of 7); disputed repeats shown to Rafi.
CLAUDE.md 16 THE REPO IS THE SOURCE OF TRUTH (Drive differences are not clashes; keep DRIVE_DIFFS and V1_TASKS) -> no new Drive difference found today beyond the 20 listed; lessons of Part B go into V1_TASKS.md at step 8.
CLAUDE.md 16 Aim 14 story cards and 7 story clips -> G2; today the CARD FILTER as written gives at most 13 (11 without the Politics and Research exceptions of clash 1) until Rafi answers clash 2.
CLAUDE.md 16 BIGGER PICTURE WEIGHT (meaningful analysis and thing to watch; not financial advice in card and clip; clip screen flashes "This is not financial advice"; caption carries it) -> make_cards.py adds the notice on the card; screen line read; the post caption is made on Rafi's PC: say so at delivery.
CLAUDE.md 16 PEOPLE WITH THEIR POSITION -> read every card and clip: each named person has position and organisation in the same sentence (for example Antonio Filosa in C11-01, Elon Musk in C16-01 or C05-09).
CLAUDE.md 16 HEADLINES START WITH POLITICS (a Politics card is clip 1; never skipped) -> G11b; clash 3.
CLAUDE.md 16 FAMOUS PEOPLE RULE: not applicable to card choice (pool scope); C05-02 (Musk and Ambani) is an update of the 9 Oct card C13-21, so not a card.
CLAUDE.md 16 VIRAL RULE (20 or more outlets, score at least 7; one re-run of a story that ran below 7 despite NO OLD NEWS, NO UPDATE CARDS, NO REPEATS IN 7 DAYS) -> C01-16 card and clip (Rafi's order, named); C11-16 may run once; C12-14 and C07-07 ran at 7 or more before, so they stay blocked as cards, clips and teaser unless Rafi names them.
CLAUDE.md 16 ONE TOPIC, ONE CARD -> every card pair and clip pair checked for a shared topic before Rafi sees the deck (manual table; the gate has no such check).
CLAUDE.md 16 CARD_FILTER numbers base_min=5 extra_min=7 target=14 max_per_category=2 market_max=3 company_cards=3 company_clips=2 -> pick_pack.md "Filter" line matches; pick_gate.py reads them.
CLAUDE.md 16 ROBOTICS (Bulletin 3 to 5; Headlines 1 robotics clip; cards 2, one humanoid; guidelines; funding for a humanoid company counts) -> Bulletin 5: PASS; cards and clip: clash 2; humanoid: 0 eligible, state it.
CLAUDE.md 16 BEFORE EVERY STAGE -> this file is the read; scripts run as the truth (pick_gate.py, check_wording.py, check_headlines_rules.py, fill_headlines.py, verify_headlines.py).
CLAUDE.md 16 HEADLINES GENERATION (8 steps, AIND_anchor_voice_sample_4s.wav, unhurried presenter tone, written into the JSON) -> fill_headlines.py asserts steps 8 and the .wav; verify_headlines.py checks the tone sentence in every active prompt.
CLAUDE.md 16 OPENING AND ENDING OPTIONS: not applicable (Rafi has not asked for new options today).
CLAUDE.md 16 APPROVED OPENING AND ENDING (slots 1 and 13 bypassed; option 4 clips of 3 Oct used in the stitch) -> assets/pack_base.json slots 1 and 13 "bypass"; check_headlines_rules.py A2.
CLAUDE.md 16 QA GAPS -> the card choice gate (pick_gate.py), card wording check (check_wording.py), Headlines rules check exist; report and Bulletin rules: step 7 recheck item 47 below.
CLAUDE.md 17 THE BIGGER PICTURE CORNER (card head is the market summation; body what happened and what to watch, 4 lines, notice stays; clip same content, 10 s; one story at three lengths) -> card head at most 85 characters, body at most 160 characters in 2 sentences (check_wording.py); clip at most 10 s; content only from bigger_picture_bulletin.json and bp_refs (G16).
CLAUDE.md 18 FRESH CHAT BEFORE A RUN -> this chat delivered Part A at 07:40 UTC and then the viral work; Part B continues the same run (rule 9 chain). If this chat was compacted, Rafi's explicit yes is needed; lesson 123 says Part B needs a new chat. Check and say which applies.
CLAUDE.md 19 THE START LINE: not applicable to Part B (Part A started with "run skill part A for 10/10/26", nothing added).

### 1b. Lessons of docs/V1_TASKS.md
P1-1: not applicable: scan window (Part A).
P1-2: not applicable: direct source reading (Part A).
P1-3: Fun Side 5 to 10 in report, top 3 in Bulletin -> report 7, Bulletin 3: PASS.
P1-4: not applicable: report and Bulletin cutoffs (Part A stated them: report 114, Bulletin 39).
P1-5: everything final to Drive, what the connection cannot take to Rafi -> step 8 manifest; PNGs and JSON in chat.
P1-6: 14 to 15 story cards, half to Headlines, company 2 clips and 3 cards, money cards at most 3, headline-only story only as a cautious card -> G2, G10, G9, G8; G5 allows no headline-only card today.
P1-7: news part about 90 s, clips rounded up to the half second -> check_wording.py total; fill_headlines.py.
P1-8: hologram border and screen set by the prompt -> the fill prompt carries the border line; opening bypassed (stored option 4).
P1-9: show only spoken words when Rafi asks for the stories -> review_list.py prints script and screen, not the prompt.
P1-10: files one at a time, never a zip -> step 8 item 1.
P1-11: not applicable: proposal not decided.
P1-12: not applicable: pool editing (Part A).
P1-13: not applicable: pool fixed (240).
P1-14: not applicable: network setting.
P1-15: check recent reports before suggesting extra stories -> any reserve card is checked by G17 against 7 days of decks and was in the report.
P1-16: check the approved opening before a new one -> slots 1 and 13 bypass.
P1-17: never build before Rafi's yes -> list approval before wording; no cards or JSON sent before the step 7 approval.
P1-18: no pgrep watchers -> long jobs only with run_in_background.
P1-19: stop at every compaction -> if Part B compacts, stop for Rafi's yes (CLAUDE.md 18).
P1-20: match numbered answers to the original list -> when Rafi answers section 2 or the review list by number, map each number to the message he answered.
P1-21: show each step and wait; never drop a category or write card text before asking -> list approval before wording; every skipped category named in left_out_notes.
P1-22: no old JSON in a zip, no unapproved hologram wording, no rule copied without asking -> no zip; screens from REAL TV SCREENS only; no CLAUDE.md change without Rafi's word.
P1-23: not applicable: undecided proposals.
P1-24: not applicable: old open items, not in this run.
P1-25: broken Google News links -> report and Bulletin JSON hold 0 news.google and 0 utm links: PASS.
P1-26: re-dated stories held -> no card, clip or teaser id in held.json (32 re-dated): G1.
P1-27: Drive text uploads lose characters -> step 8 verifies by size (and md5 where possible).
P1-28: not applicable: curator choice.
P1-29: meaning check before any JSON leaves -> steps 3, 3b, 4 before step 6; nothing sent before approval.
P1-30: not applicable: fan-out test.
P1-31: compute weekdays -> 2026-10-10 is a Saturday (computed): date strings "SAT 10 OCT 2026" and "10-10-26".
P1-32: read the governing V1 file before quoting -> all six rules files read today (same as 9 Oct).
P1-33: save working files before a new chat -> save_state.py before the step 7 wait and after delivery.
P1-34: reuse the approved opening -> superseded by APPROVED OPENING AND ENDING (option 4 of 3 Oct): slots bypassed.
P1-35: no wrong drops, no 4.5 minute audio, no three OpenAI clips, no five OpenAI cards -> news part about 90 s; G9, G10, C16.
1: plain English gate (script check and stranger check, table to Rafi before render; deed first; file named by its Drive name) -> check_wording.py plus Opus stranger agents; results table in the step 7 message. Note: check_wording.py no longer counts words (variable w unused), so the 15 word card rule is counted by hand at step 7.
Port-1: not applicable: porting list item (24 h window, Part A).
Port-2: not applicable: porting list item (sources, Part A).
Port-3: company limits on cards and clips -> G9, G10.
Port-4: 13 slot template, Bigger Picture clip 11, stored ending slot 13 -> build_pack.py slots C01 to C13, C12 unused.
Port-5: hologram border and screen lines in the prompt -> fill_headlines.py PROMPT (screens now REAL TV SCREENS).
Port-6: clip seconds rounded up (CLAUDE.md wins over Drive B1a) -> fill_headlines.py.
Port-7: Bigger Picture at three lengths -> card and clip from bigger_picture_bulletin.json.
Port-8: deed first, sentence limits, stranger check -> check_wording.py and stranger agents.
Port-9: repeat check against decks -> now 7 days (G17) plus the 3-day table.
Port-10: rules files by Drive name -> this file names them so.
Port-11: 8 steps, 4 s voice sample, unhurried tone -> fill_headlines.py and verify_headlines.py.
Port-12: opening and ending only as options on request -> not asked today; bypassed.
13: not applicable: speaking speed test not decided; formula stays 4.4 syllables a second.
14: long clips untested -> no clip over 10 s.
15: not applicable: timeline screens were for the opening and ending, both bypassed.
16: not applicable: ending screen (stored ending used).
17: not applicable: test JSON only on Rafi's request.
18: voice sample lives on Rafi's PC -> the JSON names AIND_anchor_voice_sample_4s.wav; one line at delivery that it must be in ComfyUI/input.
19: stranger fails background words, watch items without why, two facts as one -> stranger briefs; the line is fixed, not the reader.
20: not applicable: no file named by Rafi to find.
21: not applicable: Google Sheets.
22: Fable for card and Headlines wording -> wording agents on model "fable".
23: repeat check over earlier decks -> G17 7 days plus the 3-day table.
24: credit clash -> settled by lesson 46 (CREDIT rule).
25: 15 word cards -> counted by hand at step 7 (script does not count).
26: not applicable: pool math.
27: not applicable: survival rate (Part A).
28: not applicable: four-day pool repeat list (Part A).
29: cards and Headlines take only NEW stories; follow-ups go to the Bigger Picture or teaser -> tightened by NO UPDATE CARDS: G6 also blocks updates in the teaser (the draft teaser C12-14, C09-01, C05-01, C07-01 are all updates).
30: fetch and diff rules each run -> rules/_diff_B.txt: six files the same as 9 Oct.
31: reader level only from the phrasing file -> the briefs name no level number: PASS.
32: not applicable: writer proxy line (Part A).
33: not applicable: prefetch (Part A).
34: blocked sources -> cards only from read-in-full entries (G5); C11-05 and C04-01 excluded.
35: stranger check needed -> one Opus stranger round per product.
36: render check: a too-wide CATEGORY line drops a card -> assemble_cards.py stops on a missing card; build_cards_copy.py warns over 46 characters.
37: syllable budget 35 to 40 per story -> wording_headlines.md says so for stories; its 48 for the Bigger Picture breaks CLAUDE.md (section 2b).
38: the Bigger Picture card and clip give a reason for each thing to watch -> read; Bulletin version has no item numbers (Part A).
39: not applicable: Bulletin balance (Part A; 11 of 11 sections today).
40: not applicable: Drive V1 scripts not run.
41: never ask what the record answers -> the voice sample is on Rafi's PC; do not ask.
42: two chained skills -> Part B started from Part A's folder W.
43: Bigger Picture card head checked by script -> check_wording.py on the bp head and body.
44: a rule a script can enforce is never a question to Rafi -> only the clashes of section 2 and wording choices go to him.
45: Drive date folders and runs/<date> copy -> step 8 and save_state.py.
46: CREDIT rule -> card SOURCE line is the first reporter (see section 2b item 8).
47: Bigger Picture label AIND -> build_cards_copy.py: PASS.
48: not applicable: write only what can print (Part A).
49: compaction before a run -> CLAUDE.md 18 line above.
50: reply stories name the earlier story -> check_wording.py reply check.
51: not applicable: open upgrade, "not now".
52: not applicable: V1 task list.
53: Drive takes only typed text -> PNGs and JSON to Rafi in chat.
54: not applicable: weekend window (Part A).
55: names never introduced, jargon, idioms -> novice_test (G15b) and stranger check.
56: Market labels about 10 characters -> G14 (15) and the 46 character warning.
57: not applicable: Bulletin spread (Part A).
58: not applicable: layout image affects the video post on Rafi's PC.
59: the one list -> Part B lessons into V1_TASKS.md at step 8.
60: Headlines written to the rules (G2 intros, G1.2 tags, fun and teaser about 8 s) -> make_wording_prompts.py passes the 9 Oct intros; rules agent checks tags; B1 aim 8.5 s for fun and teaser.
61: hard gate on current lines -> common_b.rules_gate in build_pack.py and review_list.py.
62: token cost -> report helper tokens per stage at the end.
63: stored opening and ending -> slots 1 and 13 bypass: PASS.
64: .wav voice, "Also in the full report." with a full stop, "Kawa saki" -> fill_headlines.py AUDIO .wav; check_headlines_rules.py B2a; cue list.
65: not applicable: start line (Part A).
66: old news in cards -> report after check_dup14 plus G17 over 7 of 7 decks.
67: company caps -> G9 (3 cards), G10 (2 clips); "no company twice in a row" was never confirmed by Rafi and is not in the skill: not a check.
68: same deal twice -> ONE TOPIC check on card pairs.
69: not applicable: pool CSV path (Part A).
70: not applicable: model trial.
71: parallel sessions -> git fetch and compare before pushing; never rebase onto a force-updated origin (lesson 163).
72: Headlines level 5 shape -> check_wording.py shape checks; a fix is shorter.
73: who, what, why as data; main session never rewrites a line -> check_wording.py; rewrites by an agent only (model: clash 4).
74: one truth for writing rules -> phrasing file only; but wording_common.md still caps every sentence at 15 words for the Headlines writer (section 2b).
75: simple is not childish -> stranger and rules agents fail fragments.
76: model policy; the Agent tool sets no effort -> say so when reporting Fable "max".
77: no shell "&" -> run_in_background only.
78: not applicable: manifest path (Part A).
79: not applicable: check_dup14 looseness (Part A).
80: one event in several entries -> ONE TOPIC check on cards.
81: Bigger Picture overstatements -> the card and clip are checked claim by claim against the Bigger Picture texts at step 4.
82: thin days, counts are guidelines -> state the card count if under 14.
83: stale clone -> git fetch and compare before any Part B agent; use the CLAUDE.md on disk (the copy loaded into this session at start had the older tiered VIRAL text).
84: not applicable: pool table.
85: Drive upload by retyping wastes tokens -> no Drive agent for files over about 30 KB.
86: not applicable: Part A cheap wins.
87: not applicable: Part A token record.
88: the Bigger Picture is written by an agent, not the main session -> also for its card and clip.
89: (a) never Haiku, (d) Drive agent only for text up to about 30 KB, (e) one Bigger Picture agent; open clash "base_min 5 below report cutoff 6" -> today the report holds score-5 fill stories (114), and cards come from the Bulletin, so it does not bite.
90: no shorthand to Rafi -> full category names, terms explained once.
91: a count rule wins over a cutoff -> 8b item 4; clash 2.
92: grep for an old rule's wording when it changes -> found: 15 word cap in wording_common.md for Headlines; "about 20 words" in rules_check_headlines.md and rewrite_headlines.md (section 2b).
93: repeat cards -> update_allowed.json; 3-day name and topic table shown before the deck.
94: novice test at choice time -> G15b.
95: never run my own recommendation -> section 2 fixes wait for Rafi's pick.
96: no check loops; agents fail only on rule breaks -> one round each; clash 6.
97: Politics card left out of the clips -> G11b; clash 3.
98: git pull first -> done at Part A step -1 (reset to origin); fetch again before Part B agents.
99: not applicable: no Haiku today.
100: helper agents must not create sessions -> check no helper created a remote session; Rafi decides the tool list.
101: no shell "&" -> run_in_background.
102: not applicable: SHORT warning (Part A).
103: measure before claiming a shortage -> robotics and humanoid counts in the facts section above.
104: not applicable: feeds.
105: not applicable: language filter.
106: not applicable: report fill (Part A).
107: which score counts -> pick_gate.py and the deck use the entry score; selection_draft.json shows pool scores: say which score Rafi sees.
108: an automatic repeat match is a list to judge -> read every G17 hit against its earlier line.
109: not applicable: editors (Part A).
110: second reader for the Bigger Picture -> Part A done; card and clip checked at step 4.
111: when a newer rule overrides, change the brief and grep -> section 2b lists stale brief lines.
112: not applicable: re-dated rule (Part A held.json).
113: meaning check before the PDF -> step 7 rechecks the report and Bulletin text (item 47).
114: change only what is asked -> Rafi's edits change only the named items (also HEADLINES INTROS AND FLOW).
115: show first, then act -> no hold, swap or fix before Rafi sees the list.
116: count rounds per product -> one check, one rewrite per product.
117: check a figure before passing it on -> every number in the step 7 message read from a file.
118: customer text: headline once, no process notes, a source link on every story -> step 7 item 47: 0 missing links: PASS; "What changed:" labels: FAIL (7 report, 2 Bulletin items); copy sites printed in source lines ("relayed by", "relaying"): FAIL (4 report, 2 Bulletin).
119: the headline-only note stays until the Drive rule changes -> 15 "Note: we could not open..." lines remain: as required.
120: test a check on real cases -> G17 and check_wording false alarms judged against entries.
121: compare old and new facts of every rewritten item by script -> after the one rewrite round, diff names and numbers per item.
122: send with "attach", one file at a time -> step 8.
123: the cloud chat cannot reach the PC; Part B in a new chat -> CLAUDE.md 18 line above.
124: restart copy is text only -> save_state.py.
125: commit and push after every change -> runs/2026-10-10 copy and lessons committed.
126: model names in commits: Rafi to decide -> lesson 173 says trailers carry only the session link; note the session's attribution reminder asks for a model line: follow Rafi's repo rule (lesson 173).
127: estimate cost before a filler or scout -> say the cost before any extra agent.
128: answer first, one question at a time, plain words, no unasked changes -> the step 7 and clash messages.
129: scripts unchanged; new scripts flagged -> bulletin_keep.py is a run-folder copy (flagged in Part A).
130: "What changed:" and "What is new:" out of customer text -> FAIL: 7 report items and 2 Bulletin items start "Why it matters: What changed:".
131: step 0c before any script that chooses -> card_candidates.py and pick_gate.py pack ran at 11:02 (paper input only); the picker must not run before this file is read.
132: robotics clash settled into ROBOTICS -> but the CARD FILTER robotics line still differs (clash 2).
133: not applicable: no comparison test today.
134: robotics counts: Bulletin 3 to 5, cards 2 (one humanoid), Headlines 1 -> Bulletin 5: PASS; cards and clip: clash 2; humanoid 0 eligible.
135: robotics counts are guidelines; one extra allowed -> state counts.
136: one Bulletin data file -> products/bulletin_pdf.json is the delivered Bulletin's data (bulletin_keep.py writes it; PDF rebuilt 11:00): PASS.
137: gate gaps (count 14 or 15, freshness flag blind to decks, humanoid ruling) -> G2, G17, G13 robotics_ruling.
138: a picker note is not a source -> wording only from entries and facts files.
139: the robotics clip must say what the machine does -> C11-10 and C11-12 say it; C11-01 and C11-16 do not.
140: REAL TV SCREENS versus the fill prompt "No people, no faces" -> screens without people (script unchanged).
141: screens static and wordless -> rules agent checks for camera moves and implied text.
142: list every clash once at 0c -> section 2 and 2b, one message.
143: not applicable: ComfyUI crash on Rafi's PC.
144: Part B tokens (8 Oct about 2.9 M) -> report today's per stage.
145: stale clone -> see 83 and 163.
146: not applicable: pool against last four pools (Part A).
147: held ids never cited -> G1 and G16 cover cards, clips, teaser and bp_refs.
148: Fable max Bigger Picture with an independent second reader -> Part A done; Part B card and clip checked by Opus stranger and rules agents and step 4.
149: not applicable: report Bigger Picture length (Part A).
150: no internal codes on the Bulletin cover -> purpose line reads "(Health and Society from 6; Robotics, the 5 best of those from 5)": PASS.
151: not applicable: report fill editing (Part A; editors V, W, X ran).
152: not applicable: Bulletin spread (Part A).
153: not applicable: Part A tokens.
154: Bulletin never without Politics -> 2 Politics stories: PASS.
155: not applicable: world politics pass (Part A).
156: not applicable: PDF rebuilds (Part A).
157: big famous-people stories -> C05-02 (Musk and Ambani) is in the Bulletin; as an update of the 9 Oct card C13-21 it is not a card.
158: freshness records the newest development -> C11-16 says NEW but re-runs 9 Oct C11-12 (VIRAL clause allows one run); C01-16 says FOLLOW-UP of 8 Oct (named).
159: not applicable: report fill steering.
160: not applicable: category flags (Part A).
161: one topic, one card -> card pair check; the Musk reply (C05-09) goes on the C01-16 card only.
162: Rafi's list changes meet the gate -> gate_overrides.json with his words and each overridden line (9 Oct pattern).
163: force-updated branch -> fetch and compare; back up and reset, never rebase.
164: not applicable: report fill (Part A).
165: not applicable: check_dup14 (Part A).
166: editors' holds -> no card, clip, teaser or bp_refs id among the 8 duplicates (C03-03, C04-05, C07-02, C04-10, C16-09, C11-04, C13-08, C09-09).
167: robotics keep list -> Bulletin robotics 5: PASS.
168: not applicable: Bigger Picture length (Part A; Rafi to say).
169: not applicable: pymupdf (Part A).
170: manifest prints FAIL for files skipped by the 30 KB rule -> read those as "in chat" at step 8.
171: a viral story scored low -> C01-16 at 9 as card and clip (Rafi's order).
172: not applicable: pool scoring.
173: no model name in commit trailers -> commits of this run carry only the session link.
174: one viral floor, no cap, no tiers -> viral_picks.json note "cap of 3 under discussion" is stale; the disk rule has no cap.
175: no rule text with my own limits -> every fix in section 2 is the checker's proposal, marked so; Rafi decides.
176: viral applied today -> C01-16 card and clip; C12-14 and C07-07 not cards, clips or teaser (updates, re-run clause does not cover them) unless Rafi names them; C11-16 allowed once.
D1: do only the step Rafi names; one sentence after a step; read every spoken line before any render -> step 7 message and edits.
D2: level 5, who did what and why -> phrasing Headlines section; stranger 1b.
D3: hard names as spoken -> cues an-thropic, N-vidia, Kawa saki only where spoken (check_headlines_rules.py 15Sep1).
D4: no colon after "Also in the full report" -> B2a check.
D5: 8 steps, .wav voice, seconds formula -> fill_headlines.py asserts; the libx264 crash is on the PC (not applicable here).
D6: not applicable: speech QA on the PC.
D7: finishing layout on the PC -> not applicable to the JSON; note: D7 says the teaser credit is AI NEWS DESK while build_pack.py writes DAILY GLOBAL AI INTELLIGENCE REPORT (Drive G7.3): flag at delivery (section 2b item 13).
D8: openings and endings are options; current option 4 -> bypass: PASS.
D9: not applicable: layout picture upload.

## 2. CLASHES AMONG CLAUDE.md RULES
Only places where two CLAUDE.md rules demand opposite things for this run. Each fix is the checker's proposal (mine, not Rafi's); the main session runs none of them until Rafi picks (8a, 8b item 1).

Clash 1. CARD FILTER ("Every category keeps its best story if it scores base_min or more") versus CARDS FROM THE BULLETIN ("story cards are chosen only from the stories of the Bulletin").
How: Politics (Bulletin: 2 updates) and Research (Bulletin: C04-01 not read in full) have no eligible Bulletin story but have eligible Full Report stories (C13-03 at 6; C04-03 and C15-01 at 6): the first rule keeps a card for them, the second forbids it. The scripts take opposite sides (card_candidates.py gives no Politics or Research card; pick_gate.py G18 fails without them), and the picker prompt orders a reserve Politics card from the 7 Oct MUST-HAVES that live only in briefs/pick_stories.md.
Paste-ready fix (add to CARDS FROM THE BULLETIN): "Exception (Rafi, 7 Oct 2026): a category with no eligible Bulletin story (new or named by Rafi, read in full) takes its best Full Report story at base_min or more as its one card, marked exception with the reason."

Clash 2. CARD FILTER ("a robotics card shows a machine doing something"; extra slots only at extra_min 7) with rule 14 ("Counts are guidelines ... adjust them to the day's pool") versus ROBOTICS ("the cards carry 2 robotics cards ... Robotics means anything about humanoid robots and any other robotics") with 8b item 4 ("A count or an order Rafi gives wins over any cutoff or script default").
How: today no robotics story meets both: the robotics stories at 7 (C11-01 Stellantis and Wayve, C11-16 Tesla rename) show no machine doing something, and the machine stories (C11-10 Zipline, C11-12 L3Harris) score 5, below extra_min for a second robotics card; so ROBOTICS and 8b item 4 ask for 2 robotics cards and 14 story cards, while CARD FILTER with rule 14 gives 1 robotics card and 13 story cards.
Paste-ready fix (add to ROBOTICS): "The two robotics cards and the one robotics clip are exempt from extra_min (base_min is enough) and may come from the Full Report below the Bulletin cut-off; each shows a machine doing something, except a humanoid robot story, which counts as it is (funding included). The CARD FILTER target of 14 wins over extra_min: when the stories at extra_min run out, the next best eligible stories at base_min fill to 14."

Clash 3. HEADLINES START WITH POLITICS ("when the deck has a Politics card its clip is clip 1 ... it never skips Politics") versus HEADLINES ORDER ("the order and choice of the seven clips are set ONLY by the Drive file ... This repo never restates or reinterprets it") and the CARD FILTER line "Headlines are chosen by the Drive Headlines Master (HEADLINES ORDER above), which says the strongest card stories by score".
How: today's Politics card can only be a reserve story at 6 (C13-03) or 5, while the eligible deck has up to 9 other cards at 7 or more (C01-16 9, C12-01 8, C13-01 8, C06-01, C08-02, C10-01 and the extras at 7): the strongest-by-score choice leaves Politics out of the 7 clips, the Politics rule makes it clip 1.
Paste-ready fix (replace the HEADLINES ORDER sentence): "HEADLINES ORDER (Rafi, 5 Oct 2026): the clips follow the deck order of the Drive file Headlines_Master_Rules_Structure.txt (General order of categories, criticals lead, Section A item 3); the choice is the strongest card stories by score, after the clips this file requires: the Politics card as clip 1 (HEADLINES START WITH POLITICS), one robotics clip (ROBOTICS) and any story Rafi names." In CARD FILTER replace the Headlines sentence with: "Headlines are chosen by HEADLINES ORDER above."

Clash 4. MODEL POLICY ("Hard tasks run on Opus 5.5 ...: the editors, the stranger check, the rules agent and the rewrite agent") versus WHO WHAT WHY FIRST ("failing lines go to a Fable rewrite agent (Part B step 3a)"), supported by STORY CHOICE ("Fable ... writes their wording ... a different model must check the author").
How: if any card or Headlines line fails the one check round, the first sends it to an Opus rewrite agent, the second to a Fable one.
Paste-ready fix (MODEL POLICY): replace "the editors, the stranger check, the rules agent and the rewrite agent" with "the editors, the stranger check and the rules agent; the card and Headlines rewrite agent is Fable, their author (WHO WHAT WHY FIRST, STORY CHOICE)".

Clash 5. CARD FILTER ("A meaningful update of an earlier story can be a card ... and the card names the earlier story") and NO OLD NEWS ("A meaningful update of an earlier story can be a card (CARD FILTER below)") versus NO UPDATE CARDS ("an update of an earlier story is a card ONLY when a major story changed meaningfully AND Rafi has named it; the default is none").
How: today's Bulletin updates C12-14 (9), C09-01 (8), C07-01 and C07-07 (7), C05-01, C05-02, C08-03 (6) may be cards under the first two lines and may not under the third (only C01-16 is named; pick_gate.py G6 applies the third).
Paste-ready fix: in CARD FILTER replace the update sentence with "An update of an earlier story is a card only under NO UPDATE CARDS (Rafi named it) or the VIRAL RULE re-run, and the card names the earlier story."; in NO OLD NEWS replace its last sentence with "An update can be a card only under NO UPDATE CARDS."

Clash 6. HEADLINES RULES RECHECK ("Nothing goes to him with a rules FAIL") with WHO WHAT WHY FIRST ("The gate refuses the JSON and the review list unless the checks passed on the current lines") versus 8b item 7 ("No check loops: one check round and one rewrite round, then show Rafi what is left").
How: bites only if a line still fails after the one rewrite round (5, 6 and 7 Oct needed several rounds; 9 Oct ended with a rules override waiting for Rafi's yes): one rule says keep it from Rafi until it passes, the other says stop and show him what is left.
Paste-ready fix (HEADLINES RULES RECHECK): replace "Nothing goes to him with a rules FAIL." with "After one check round and one rewrite round (8b item 7), any line still failing goes to Rafi as a short list (line, rule, reason) for his call; no pack, JSON or review list is built from a failing line."

Tested and not counted as clashes (each pair can be met together today):
- VIRAL RULE versus NO OLD NEWS, NO UPDATE CARDS, NO REPEATS IN 7 DAYS: the VIRAL RULE names them as not blocking its one re-run; today it covers only C01-16 and C11-16.
- HEADLINES INTROS AND FLOW (its intro list; dictated intros win over G2) versus HEADLINES RULES RECHECK (intros rotate): the list was Rafi's dictation of 6 Oct (runs/2026-10-06 rules_overrides.json); nothing dictated today, so rotation applies; "In security" and "In tech" (9 Oct) need other topic-naming intros.
- HEADLINES INTROS AND FLOW (prefer AI affecting people over politics) versus HEADLINES START WITH POLITICS: settled in the 7 Oct text.
- REAL TV SCREENS versus BIGGER PICTURE WEIGHT warning words: REAL TV SCREENS keeps the Bigger Picture sign.
- NEVER Haiku versus HAIKU TODAY ONLY: 8 Oct only.
- CLIP SECONDS (max 10) versus rule 16 timings and rule 17 (Bigger Picture 10 s): consistent.
- NO REPEATS IN 7 DAYS versus "last three decks" (CARD FILTER, NO UPDATE CARDS table): 7 days is stricter; both met.
- PEOPLE WITH THEIR POSITION versus HEADLINES SHAPE (no stacked descriptions, one comma): one compact title ("Stellantis chief Antonio Filosa") meets both.
- BIGGER PICTURE MODEL (one agent, three lengths) versus STORY CHOICE (Fable writes card and Headlines wording): both met if the Part A Bigger Picture author writes the card and clip.
- CARDS FROM THE BULLETIN versus ROBOTICS: ROBOTICS says the Bulletin cut-off does not stop the two robotics stories.
- Rule 18 versus rule 9 (Part A starts Part B): rule 18 governs the start of a run; a compaction would still need Rafi's yes.
- CARD FILTER base_min versus the Fun card (C16-01 at 3): "fun is always last" and "not counting Fun" treat Fun as its own slot (9 Oct fun was also 3).

## 2b. Conflicts between CLAUDE.md and a brief, a script or a run file (not CLAUDE.md-internal; 8a and 8b item 2 cover them)
1. briefs/wording_common.md hard rule 1 "Every sentence at most 15 words" goes to the Headlines writer too (headlines_work/wording_common.txt) against HEADLINES SHAPE and the phrasing file ("syllables are the only measure ... never a word count"); same pattern as lesson 92.
2. briefs/wording_headlines.md "the Bigger Picture at most 48 (11 s). Never more than 53 (12 s)" and briefs/rules_check_headlines.md "never over 12 s" against CLIP SECONDS ("never passes 10 (44 syllables)") and rule 17 ("10 seconds"); check_wording.py would fail the line anyway.
3. briefs/wording_headlines.md "Script shape ... <the deed in one plain sentence>. <one plain sentence ...>" and rules_check_headlines.md and rewrite_headlines.md "two full natural sentences ... about 20 words at most" against the phrasing shape (ONE flowing sentence; a second only when the why cannot ride inside); the same brief later gives the right shape.
4. briefs/wording_headlines.md bullet "every other clip keeps its text-free symbol" (7 Oct) against REAL TV SCREENS (8 Oct) and the same brief's own screen line.
5. fill_headlines.py PROMPT "one simple bold picture ... No people, no faces. No readable text ..." on every active slot, including C11 whose screen must flash "This is not financial advice" (BIGGER PICTURE WEIGHT) and against REAL TV SCREENS (only real named faces are barred). The script stays during the run: write screens without people; the C11 prompt contradicts itself (the 9 Oct pack did too); the Drive 15 Sep item 3 puts required words in post.
6. review_list.py header tells Rafi "one simple picture inside the blue border, no text and no people": stale against REAL TV SCREENS.
7. check_wording.py docstring promises "every sentence at most 15 words" for cards, but the code never tests it (variable w unused): the card 15 word rule (wording_cards.md, SKILL step 8 item 5, lesson 1) is not enforced by script.
8. build_cards_copy.py copies the entry source raw to the card SOURCE line: C11-10 "Zipline, relayed by Unite.AI", C11-12 "L3Harris, relayed by Defence Industry Europe", C11-13 "UK Government, relayed by The AI Insider", and "citing" forms, against CREDIT (the outlet that reported, never a copy site).
9. cards_work/prompt_picker.txt order 2 says for the viral stories "every other rule still applies (no repeats, no update cards unless Rafi named it)", leaving out the VIRAL re-run clause; in practice it touches only C11-16, whose entry says NEW.
10. viral_picks.json note "cap of 3 under discussion with Rafi", and the CLAUDE.md copy loaded into this session at start (tiers 7, 8, 9; at most 3 a day; AI only), are stale against the disk VIRAL RULE (one floor of 7 at 20 outlets; lessons 174, 175).
11. pick_gate.py G4b judges a reserve exception without machine_action or score: a reserve robotics card (C11-12) fails G4b because the Bulletin holds new read robotics stories without a machine (C11-01, C11-16, C11-13), although ROBOTICS lets the two robotics stories pass the Bulletin cut-off; needs gate_overrides.json with Rafi's words if chosen.
12. selection_draft.json (card_candidates.py) teaser C12-14, C09-01, C05-01, C07-01 are all updates: pick_gate.py G6 fails them in the teaser.
13. Lesson D7 (teaser and Bigger Picture credit AI NEWS DESK) against build_pack.py and Drive G7.3 (teaser credit DAILY GLOBAL AI INTELLIGENCE REPORT): decided on Rafi's PC at finishing; flag.
14. Part A products (step 7 recheck, skill 0c item 4): "Why it matters: What changed:" in 7 Full Report and 2 Bulletin items (lesson 130); copy sites printed in the source line ("relayed by", "relaying") of 4 Full Report and 2 Bulletin items (build_pdf.py prints the source as is; CREDIT "never a copy site"); "citing" source lines (8 Full Report, 1 Bulletin) are allowed by CREDIT only when the chain is unclear, and "Stocktwits, citing the Financial Times" puts a copy site before the known first reporter. Also C07-07 Firmus is in the Bulletin at the viral floor although it ran at 8 on 9 Oct (C06-01); the sweep's exclusion fix (commit ab35623, 11:01 UTC) came after it was raised.

## 3. STEP 7 CHECKLIST
Every rule the final cards and Headlines must pass, with the test. Write PASS or FAIL per item with the evidence; nothing is shown with an open FAIL except as clash 6 allows once Rafi answers it.
1. Choice gate: `python3 $S/pick_gate.py gate --workdir W` prints GATE PASS; gate_result.json ok true and its md5 equals the current selection_fable.json; any overridden line sits in gate_overrides.json with Rafi's words.
2. Rafi approved the story list before any wording: his message time is earlier than cards_copy_fable.json and scripts_fable.json.
3. Counts: 14 story cards (15 allowed) plus fun, teaser (4 items), Bigger Picture, cover, closing; 7 story clips plus fun, teaser, Bigger Picture; any shortfall stated with its reason (G2; count selection.json).
4. Source of cards: Bulletin candidates only, exceptions marked with a reason (G4, G4b); expected today: Politics and Research, as Rafi rules on clash 1.
5. Every id exists and is not held (G1; held.json 40 ids); bp_refs in the report, not held (G16).
6. Read in full: every card, clip and fun story has verified_text (G5).
7. Updates: only C01-16 (update_allowed.json) and the VIRAL re-run C11-16; C12-14, C07-07, C09-01, C07-01, C05-01, C05-02, C08-03 are not cards, clips or teaser items (G6, read).
8. Repeats: G17 PASS over the decks of 3 to 9 Oct (7 of 7); every disputed repeat shown to Rafi; the 3-day table (each card against the cards and Headlines of 7, 8, 9 Oct by name and topic) goes with the deck.
9. One topic, one card: every card pair and clip pair checked for a shared topic, reply or follow-up (manual table).
10. Deck order is the Drive category order, Fun last, high score first inside a category (G7).
11. Category limits: at most 2 per category, Market at most 3, no money-heavy deck (G8).
12. Company limits: at most 3 cards and 2 clips per company (G9, G10, check_headlines_rules.py C16); watch Anthropic (C01-16, C12-01, C12-03, C02-02, C04-03).
13. CARD FILTER scores: each category's card at 5 or more; extra cards at 7 or more, as Rafi rules on clash 2 (not tested by the gate: read the entry scores).
14. Coverage: every category with an eligible story has a card (G18); robotics two when two qualify (G19); humanoid count stated (0 eligible today).
15. Robotics card shows a machine doing something or carries robotics_ruling (G13), as Rafi rules on clash 2; the robotics clip says what the machine does (rules agent, B2).
16. Labels at most 15 characters (G14); CATEGORY line at most 46 characters (build_cards_copy.py warning).
17. Every card has reason, not_repeat_because and novice_test (G15, G15b).
18. Headlines choice: clips are cards in deck order (G11, check_headlines_rules.py A3); the Politics card is clip 1 if the deck has one (G11b), as Rafi rules on clash 3; 1 robotics clip; C01-16 is a clip (Rafi's order); teaser items are neither cards nor clips (G12, A5).
19. The Bigger Picture is one card and one clip (G20).
20. Wording script check: check_wording.py "RESULT all pass" on cards_copy_fable.json and scripts_final.json; wording_check.json newer than scripts_final.json.
21. Card limits: head one sentence at most 85 characters; body exactly 2 sentences at most 230 characters (Bigger Picture at most 160); teaser line at most 90; at most one number per sentence; no banned word; no "X reports that" opening (check_wording.py).
22. Card sentences at most 15 words: count with a one-line script (check_wording.py does not count).
23. Headlines shape: one flowing sentence after the introduction (a second only for the why), 35 to 40 syllables, no side-clause opening, at most one comma, no digits, who, what and why_for_people filled and the why spoken; no word cap (check_wording.py, rules agent).
24. Clip seconds: syllables / 4.4 rounded up to the half second; every clip at most 10 s; stories about 8 to 9, fun and teaser about 8, Bigger Picture about 10; news part about 90 s (check_wording.py, check_headlines_rules.py B1, verify_headlines.py).
25. Stranger check: one Opus round on cards and on Headlines (stranger_result.json in both folders); fixes in one rewrite round, as Rafi rules on clash 4 (model) and clash 6 (what is left).
26. Rules recheck: check_headlines_rules.py "all rules pass" (rules_check.json fails 0) and the Opus rules agent's rules_result.json on the current lines; build_pack.py runs (common_b.rules_gate passes).
27. Introductions: every story and fun clip opens with a short intro naming its topic; none twice in the reel; none of 9 Oct's ("First", "In India", "On trade", "In security", "Next", "In tech", "In education", "And now, something lighter"); teaser opens "Also in the full report." with a full stop; Bigger Picture opens "And for the bigger picture" (B2a, G2).
28. Pronunciation and names: an-thropic, N-vidia, Kawa saki only where spoken; "Google DeepMind" (check_headlines_rules.py 15Sep1, 15Sep2; fill_headlines.py CUES line).
29. No outlet spoken (G1.4); numbers as words (B3); every company under 100 billion dollars tagged (G1.2, rules agent).
30. Who, what, why in every card and clip; the why is the effect on people (phrasing 1B and Headlines section; stranger 1b).
31. People with their position and organisation in the same sentence; every name introduced (read every card and clip).
32. Unfamiliar companies get a short title; non-market cards lead with the deed, not the money (Cards Master 3.3, 3.4; read).
33. Facts: every claim matches its entry (attribution, hedge, number), nothing from picker notes, nothing stronger than the entry (step 4 read; phrasing 1A); make_cards.py prints no "LIFTED FROM REPORT".
34. Reply stories say who answers whom and name the earlier story (check_wording.py reply check; read).
35. Fun card and clip: funny at once, set-up then punchline, facts only from the source (read).
36. Screens: each story, fun and teaser screen is a realistic TV-news scene of that story's subject; no readable words, numbers, logos or real named faces; static; written without people (the fill prompt bars them); Bigger Picture screen is the warning sign with "This is not financial advice" (rules agent; read the pack slots).
37. Bigger Picture card and clip: market summation, what happened, what to watch and why, only from bigger_picture_bulletin.json and bp_refs; card notice present (make_cards.py); clip at most 10 s; say who wrote them (BIGGER PICTURE MODEL); label AIND and source AI News Desk (build_cards_copy.py).
38. Card SOURCE lines: the first reporter, never a copy site, no "relayed by" (C11-10, C11-12, C11-13 entries carry it); "X reports, citing Y" only when unclear; pill equals the entry status (read cards_copy.json src and pill).
39. Cover: the approved cover with only the date changed to SAT 10 OCT 2026 (make_cover.py); closing card text is the approved 12 Sep wording (build_cards_copy.py CLOSING).
40. Render: a new products/cards_runN; assemble_cards.py finds every card; card files counted against the list; contact sheet made; file names cards_10-10-26_I01_VL1.png onward.
41. JSON: fill_headlines.py prints CONFIG steps=8 and audio AIND_anchor_voice_sample_4s.wav, SPECTRUM CONNECTED, MIRROR ALL AGREE, STALE none; verify_headlines.py RESULT PASS; slots 1, 12, 13 bypass and 2 to 11 active.
42. Nothing sent before Rafi's approval; after it, files one at a time with "attach", never a zip; one line that the voice sample must be in ComfyUI/input.
43. Model use: picker and wording on Fable; stranger and rules agents on Opus; rewrite agent as Rafi rules on clash 4; no Haiku; the main session wrote no line.
44. Rounds: one check round and one rewrite round per product; old files kept as _old; old and new facts of every rewritten item compared by script.
45. Clashes: section 2 sent to Rafi once, all six together, and his answers recorded in CLAUDE.md the same day (rule 8); no fix run before his pick.
46. Delivery and records: delivery_manifest.py --part B then --check (text up to about 30 KB by agent, verified by size; the rest in chat); save_state.py before the wait and after delivery; commit and push; Part B lessons into V1_TASKS.md; helper tokens per stage reported next to 4, 5 and 8 Oct.
47. Full Report and Bulletin text recheck (skill 0c item 4): no "What changed:" or "What is new:" label (FAIL now: 7 report, 2 Bulletin items); source lines name the first reporter, never a copy site (FAIL now: 4 report and 2 Bulletin items print "relayed by" or "relaying"; "Stocktwits, citing the Financial Times" in the report; 8 report and 1 Bulletin "citing" lines to judge under CREDIT); every story has a direct http link (0 missing: PASS); no Google News or utm link (0: PASS); no internal C-codes (0: PASS); all 11 Bulletin sections hold stories (PASS); headline-only note stays as the Drive rule requires (15 lines). Part A is already delivered: put the two FAILs to Rafi in one line.
