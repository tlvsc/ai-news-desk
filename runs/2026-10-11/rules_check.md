# Rules check, Part B (cards and Headlines), edition 2026-10-11 (SUN 11 OCT 2026)

Written by the rules checker (Opus), Part B step 0c, at about 11:45 UTC. Read in full from disk: CLAUDE.md (276 lines; last changed 10:47 UTC, commit 30694bc), docs/V1_TASKS.md (741 lines: P1-1 to P1-35, Part 2 item 1 (written here L1), the porting list 1 to 12 (written here Port-1 to Port-12), 13 to 232, D1 to D51; lessons 216 to 232 landed at 11:30 UTC in commit 7ee4628 while this check ran), docs/DRIVE_DIFFS_FOR_CHATGPT.md (21 entries), the Part B SKILL.md (198 lines) and all 9 briefs, and W/rules: Cards_Master_Rules_Structure.txt, Headlines_Master_Rules_Structure.txt, Headlines_prompt_for_comfy_json.txt, Article_phrasing_instructions_AIND_V1.txt, Full_Report_V1_Rules_Structure.txt, Bulletin_V1_Rules_Structure.txt, STORAGE_STANDARD.txt. Read for evidence only (nothing changed): W/rules/AIMD_LV1_Adverts_Automation_Skill_V1.md (skimmed, cited once), the Part B scripts, assets/pack_base.json, Part A delivery_manifest.py and briefs/drive_delivery.md, W/products, held.json, viral files, cards_work/pick_pack.json and selection_draft.json, runs/2026-10-04 to runs/2026-10-10.
W = /tmp/claude-0/-home-user-ai-news-desk/275f65be-a09e-58a0-851e-82fd6a3a93aa/scratchpad/run_2026-10-11
State: Part A delivered. cards_work already holds pick_pack.json/.md and selection_draft.json (11:29 UTC: card_candidates.py and pick_gate.py pack ran before this check, paper input only); no selection_fable.json, selection.json, update_allowed.json, wording, pack or JSON; headlines_work is empty; no other run_ folder in the scratchpad.
Every fix offered in section 2 is my wording, not Rafi's (CLAUDE.md rule 20); none was applied.

## 1. One line per rule and lesson

### 1a. CLAUDE.md rules that touch Part B today
- Rule 0 TOP (Drive read only, except the daily delivery): Part B only reads Drive (setup agent: renderer zip, cover base) and writes only at step 8. Evidence: no Drive write before Rafi's approval; the EMPTY "reports" folder that Part A's helper made in Drive 2026-10-11 (id 1ejaNCj7rmH6mF8rHDCUIWDTy5CkjIrlB, lesson 216) is not used or touched.
- Rule 0 DAILY DELIVERY: after approval, PNGs and the contact sheet into cards, the copy JSONs into cards/supportive files, the ComfyUI JSON, pack and scripts into Headlines/supportive files of daily_data_generated/2026-10-11; size checked; never overwrite; refused files to Rafi in chat; text copy in runs/2026-10-11. Folder names only from delivery_manifest.py, which stops if W/rules/STORAGE_STANDARD.txt (fetched 11:28) differs. Evidence: products/delivery_manifest.json Part B rows, products/drive_delivery.json, the --check lines (OK or CHAT), save_state commit for runs/2026-10-11. Morning Routine: not yet (two clean manual days not reached).
- Rule 0 WHO MADE IT: every Drive title ends _Claude-V1, cards included (cards_11-10-26_I01_VL1_Claude-V1.png onward, the contact sheet too); local names unchanged; nothing on Drive renamed. Evidence: the "title" column of delivery_manifest.json.
- Rule 1 (route the job): fixed routes (cloud: choice, wording, cards, JSON; Rafi's PC: ComfyUI and the stitch). The one open route is how PNGs and the JSON reach Drive (clash 10): put the paths to Rafi before step 8.
- Rules 2, 15 and 8b item 5: short replies, plain words, no shorthand (lesson 90). Evidence: the step 7 message is the sheet, the review list and a one-line ask.
- Rule 3: superseded files renamed _old, a new cards_runN per render, fill refuses to overwrite, never rm (lesson 230). Evidence: ls of W.
- Rule 4: Rafi's step 7 edits applied and shown one at a time.
- Rule 5: numbers: card files counted against cards_copy.json (assemble_cards.py), JSON bytes and md5, active slots and seconds, longest clip, news part total (verify_headlines.py).
- Rule 6: every card and clip fact from report_entries/<id>.json and facts/<id>.json; the Opus fact check reads each claim. Evidence: cards_work/factcheck_result.json, 0 open problems.
- Rule 7: Claude does not judge the look; the contact sheet goes to Rafi first; Claude checks counts and cut-offs only.
- Rule 8: any instruction Rafi gives in Part B goes into CLAUDE.md the same day, in his words (rule 20).
- Rule 8a: 17 clashes in section 2; none chosen or applied; each goes to Rafi with both lines, the clash and a fix (how to ask: clash 13).
- Rule 8b item 1: no fix of section 2 runs before Rafi picks it.
- Rule 8b item 2: no brief may carry a rule's opposite; the stale lines of section 2b are kept out of today's prompts or flagged.
- Rule 8b item 3: before Rafi sees the deck: the 0c.4 PASS/FAIL table, pick_gate.py G17 over 7 of 7 decks, and the manual 7-day comparison (section 3; G17 misses C11-01).
- Rule 8b item 4: counts he gave (14 story cards, 7 clips, 2 robotics cards with one humanoid, 1 robotics clip, Politics clip 1) met, or the gap stated with how (clashes 1 and 2).
- Rule 8b item 6: every named person with position and organisation, every name introduced (G15b novice_test; fact check flags a missing position). Names in today's candidates: Satya Nadella, George Williamson, Nicolas Cage, Mukesh Ambani, Ashok Elluswamy, Jacob Coxon, Ben Affleck, Torsten Slok, Terence Tao.
- Rule 8b item 7: one check round and one rewrite round, then show what is left (clash 7).
- Rule 9: skills only on branch claude/eager-archimedes-ajnex3; no PNG, MP4 or ComfyUI JSON in git (save_state copies text only). Evidence: git status before each push.
- Rule 10: no logo or brand mark on any screen line; the card wordmark is drawn by the renderer.
- Rule 14 COUNTS: the card target is a working target; state the final number; never stop to ask about a count (clash 1).
- Rule 14 BULLETIN SECTIONS NEVER EMPTY (0c.4 recheck): 11 of 11 Bulletin sections hold stories; Politics, Models and Research exactly 2 each from the Full Report. PASS (products/bulletin_pdf.json).
- Rule 14 Full Report 100 to 120: 105 at cutoff 5. PASS (products/report_pdf.json).
- Rule 16 Fun Side: report 10, Bulletin 3. PASS.
- Rule 16 Cards and Headlines counts: story cards from the CARD FILTER (target 14), 7 into Headlines. Evidence: gate_result.json G2.
- Rule 16 news part about 90 s (7 stories 8 to 9 s, fun 8, teaser 8, Bigger Picture 10; stored opening and ending on top). Evidence: check_wording.py "news part" line, verify_headlines.py "news part".
- Rule 16 round up to the next half second: fill_headlines.py box_seconds and its node 13 assert. Evidence: the fill slot table.
- Rule 16 company limits (3 cards, 2 clips): G9, G10, check_headlines_rules.py C16. Today two cards each are possible for Nvidia (C06-01, C08-01), Tesla (C11-01, C11-10) and OpenAI (C12-02, C01-02).
- Rule 16 READER LEVEL: cards level 6, Headlines level 5 (phrasing file only); every writer re-reads 1, 1A, 1B and its product section before each item; who, what, why in every item. Evidence: the line in prompt_cards, prompt_headlines and the rewrite prompt; stranger 1b answers.
- Rule 16 CLIP SECONDS: syllables / 4.4, round up, aim 8, never over 10 (44 syllables). Evidence: check_wording.py FAIL over 10 s, check_headlines_rules.py B1, fill assert. Stale: stranger_headlines.md allows 48 for the Bigger Picture (2b).
- Rule 16 CREDIT: the card SOURCE line names the outlet that reported; "X reports, citing Y" when the chain is unclear; Bigger Picture card label AIND, strip AI News Desk (build_cards_copy.py writes both). Source lines to read today: C08-01 "Tom's Hardware, citing leakers on X", C11-10 "Startup Fortune, citing Drive Tesla Canada and eWeek", C11-12 "Chosunbiz, citing Counterpoint Research", C06-01 Financial Times (read in a Reuters relay), C13-01 and C07-01 Bloomberg (read in syndication), C12-03 The Sunday Times (read in IBTimes Singapore), C16-03 New York Magazine (read in Futurism). Evidence: every SOURCE line on the sheet.
- Rule 16 WRITE ONLY WHAT CAN PRINT: only written entries can be cards; every Bulletin story is written. PASS by construction.
- Rule 16 REPLY STORIES: by check_wording.py's test the only reply story in the report is C16-06 (Fun reserve, Khloe Kardashian answering critics, follow-up of 9 Oct); if used, card and clip say who answers whom and name the earlier story. Evidence: check_wording.py reply lines.
- Rule 16 HEADLINES RULES RECHECK: check_headlines_rules.py (rules_check.json fails 0) and the Opus rules agent (rules_result.json) on the CURRENT lines; no introduction of 10 Oct ("From Beijing", "In finance", "Next, safety", "In robotics", "On chatbots", "In court", "In science", fun "On a lighter note"). See clash 8.
- Rule 16 MODEL POLICY: main session and bulk helpers (setup, Drive delivery) on Sonnet; Opus for the strangers, the rules agent and the fact check; never Haiku. Rewrite agent model: clash 4. Evidence: the model of every Agent call; helper tokens per stage reported next to 4 and 5 Oct.
- Rule 16 STORY CHOICE: one Fable picker (briefs/pick_stories.md), pick_gate.py gate PASS, Rafi approves the list before any wording; Fable writes the wording; Opus checks, with a final audit per product (every rule PASS or FAIL with evidence). Evidence: gate_result.json ok true, Rafi's approval, the audit table.
- Rule 16 BIGGER PICTURE MODEL and BIGGER PICTURE WEIGHT: card and clip from bigger_picture_bulletin.json and its entries: what moves the market, a dated thing to watch and why, "not confirmed" where the date is not, not financial advice (card notice from make_cards.py; clip screen warning sign). Who writes card and clip: clash 14. Evidence: cards_copy.json bp; scripts_final.json bp "screen" holds "This is not financial advice".
- Rule 16 SCRIPTS STAY AS THEY ARE: no script change during the run; fixes go into skill text and list files only. Evidence: git diff of scripts/ empty at the end.
- Rule 16 HEADLINES SHAPE: the phrasing file's shape (one flowing sentence after the introduction, who, what, why, 35 to 40 syllables); a fix is shorter. Evidence: check_wording.py shape lines, stranger and rules results.
- Rule 16 WHO WHAT WHY FIRST: who, what, why_for_people filled before each line; the main session never rewrites a line; Rafi's words locked; the gate refuses the JSON and the review list unless the checks passed on the current lines (common_b.rules_gate). Evidence: scripts_final.json fields; wording_check.json fails 0; rules_check.json and rules_result.json newer than scripts_final.json.
- Rule 16 HEADLINES ORDER: the seven clips by the Drive Headlines Master (A3), applied by card_candidates.py. See clash 3.
- Rule 16 HEADLINES INTROS AND FLOW: each clip opens with an introduction naming its own topic, natural order, never twice in the reel, never a label unlinked to the topic; among non-Politics clips prefer AI affecting people over war or politics (today: C11-10 over the war story C11-03 for robotics); the fun clip funny at once; every clip generated except stored opening, stored ending and spare slot 12. Evidence: fill table (C01, C12, C13 BYPASS; C02 to C11 ACTIVE).
- Rule 16 REAL TV SCREENS, PHOTOREALISTIC, FUN CLIP: each screen a photorealistic TV news scene of the story, no readable words, numbers, logos or real named faces; the Bigger Picture keeps its warning sign; the fun clip sets up, then lands the joke, from source facts only. Evidence: rules agent screen findings; fill PROMPT carries the photorealistic line (lesson 209).
- Rule 16 NO OLD NEWS: cards and clips only from the report after step 9b (51 held). PASS by construction.
- Rule 16 CARD FILTER and the CARD_FILTER line (base_min 5, extra_min 7, target 14, 2 per category, market 3, company 3 cards and 2 clips): category order from the Drive Cards Master 2.4; no critical today; a category's best story at 5 or more; extras at 7 or more; read in full only; a robotics card shows a machine doing something. See clashes 1, 2, 5, 11.
- Rule 16 CARDS FROM THE BULLETIN: story cards only from products/bulletin_pdf.json (30 stories, 27 non-fun, 23 read in full). Evidence: G4 PASS; any exception carries a reason (clash 6).
- Rule 16 NO UPDATE CARDS: no update unless Rafi names it (no update_allowed.json today: none); the 3-day name and topic comparison table shown before Rafi sees a deck (clash 16). Evidence: G6 PASS; the table.
- Rule 16 NO REPEATS IN 7 DAYS: nothing that was a card or clip on 4 to 10 Oct comes back. Today's hits: C05-02 (9 Oct card s2 and clip), C11-01 (4 Oct card s9 and clip; G17 misses it), C09-01 (8 Oct card s6 and clip). Evidence: G17 PASS plus the manual table of section 3.
- Rule 16 THE REPO IS THE SOURCE OF TRUTH: a CLAUDE.md line beats a Drive line; every difference goes into docs/DRIVE_DIFFS_FOR_CHATGPT.md (2d lists nine that are missing there).
- Rule 16 PEOPLE WITH THEIR POSITION: as 8b item 6. Evidence: fact check count of "named person without position" is 0.
- Rule 16 HEADLINES START WITH POLITICS: the Politics card's clip is clip 1 (C05-07 or C13-08, both score 5). Evidence: G11b. See clash 3.
- Rule 16 VIRAL RULE: the viral stories keep 7 or more (C06-01 24 outlets, 8; C05-01 21 outlets, 8; C14-01 36 outlets counted by hand, raised 6 to 7); none is a re-run, so the re-run clause is unused today.
- Rule 16 ONE TOPIC, ONE CARD: a reply or follow-up of the same day shares a card and clip; every card pair checked for a shared topic before Rafi sees the deck (pick_gate.py has no such test yet, lesson 161). Today C11-12 and C08-04 are the same Counterpoint forecast: never two cards.
- Rule 16 ROBOTICS: Bulletin 3 to 5 (5: PASS); cards 2, one humanoid (only C11-10 is a humanoid machine doing something); Headlines 1 robotics clip. Evidence: G13, G19, the clip list. See clash 2.
- Rule 16 ROBOT WAR LIMIT: Bulletin at most 2, Full Report at most 3; no limit on cards. 0c.4 recheck: see section 3 (the count depends on whether the Yandex drone strike counts).
- Rule 16 BEFORE EVERY STAGE: read the governing files and run the skill's script as the truth; this file is the read for step 0c.
- Rule 16 HEADLINES GENERATION: 8 steps, AIND_anchor_voice_sample_4s.wav, the unhurried tone in every active prompt. Evidence: fill CONFIG line; verify_headlines.py "steps 8", "tone in N of N".
- Rule 16 APPROVED OPENING AND ENDING: slots 1 and 13 bypass (assets/pack_base.json: both "bypass"); the stitch uses the option 4 clips of 3 Oct. Evidence: fill table; check_headlines_rules.py A2.
- Rule 16 QA GAPS: the built checks run: pick_gate.py, check_wording.py with the strangers, check_headlines_rules.py with the rules agent, the fact check (Bigger Picture lines included).
- Rule 17 THE BIGGER PICTURE CORNER: card headline the market summation, body what happened and what to watch (4 lines, notice stays); clip 11 the same content, at most 10 s; the markets cap does not apply here. Evidence: cards_copy.json bp; clip seconds.
- Rule 18 FRESH CHAT: see clash 12 (Part B runs in the chat that delivered Part A).
- Rule 20: one question at a time; when he asks for the list, the list itself; rules only in his words; find his exact complaint first; deck in the approved order (G7).
- Rule 21: lessons of this run go into docs/V1_TASKS.md (step 8.4); the scratchpad HANDOFF_2026-10-11_run.md is not a source; never touch the Drive EXPERIMENTS file.

### 1b. Drive rule and structure files (only lines that touch Part B; "settled" = a CLAUDE.md line wins)
- Cards Master order block and 2.4: deck in the order Politics, Market, Security, Energy, Robotics, Models, Research, Ethics and law, Health, Society, Fun. Evidence: G7. The fixed slots are replaced by the CARD FILTER (settled, DRIVE_DIFFS 1).
- Cards Master filename rule: cards_11-10-26_INN_VL1.png locally (assemble_cards.py); _Claude-V1 added on Drive (settled, DRIVE_DIFFS 21).
- Cards Master 1.1: one 1080x1920 PNG set plus one combined image (the contact sheet). Evidence: assemble_cards.py sizes line.
- Cards Master 1.3 and 3.5 DESK VIEW: the Bigger Picture card says AIND (settled, DRIVE_DIFFS 4).
- Cards Master 1.4 and 2.5: the "More in the full report" card holds 3 to 4 report headlines with no story card; the reel teaser draws only from it. Evidence: G12, check_headlines_rules.py A5.
- Cards Master 2.1 to 2.3: cover first; criticals spend their slot (no score 10 today).
- Cards Master 2.6: aim 15 (settled: 14, DRIVE_DIFFS 2); robotics and fun normally required.
- Cards Master 2.7: at most 3 money cards. Evidence: G8 (market 3).
- Cards Master 2.8: full report only (settled: from the Bulletin, DRIVE_DIFFS 3); no web-only story.
- Cards Master 2.9: robotics = a machine doing something (humanoid funding counts, settled, DRIVE_DIFFS 18). Evidence: G13.
- Cards Master 2.11: no sales language, no link on cards.
- Cards Master 2.12: the closing card text of 12 Sep (build_cards_copy.py CLOSING). Evidence: the closing card.
- Cards Master 2.14: reel order follows deck order. Evidence: G11, check A3.
- Cards Master 3.1 to 3.4: phrasing file governs; lead with the deed, not the money, on every non-market card; unfamiliar companies titled (today Reflection AI, KingMed Diagnostics, Easy Fox, Counterpoint, Alan Turing Institute).
- Cards Master 3.6 and 3.7: approved text is never cut for layout; Rafi approves at step 7.
- Cards Master sections 4 to 6: the renderer package (md5 598989503fa221cebe87c04bac903854) owns colours, fonts and the Instagram window (a card that crosses is refused; assemble_cards.py stops); cover = approved cover with the new date (make_cover.py).
- Cards Master 7.1 and STORAGE (line 64): Drive account tlvsc.claude.agent@gmail.com verified before Drive work. Gap: briefs/drive_delivery.md does not ask the agent to report the account.
- Cards Master 7.4 and STORAGE (line 51): save each final file when ready; final means after Rafi's step 7 approval.
- Cards Master 7.7, 7.8 and STORAGE (lines 72, 73): check names and sizes first, ask on a collision, verify parent, count, size, readback. Evidence: drive_delivery.json statuses.
- Cards Master 7.15 and 7.16: contact sheet first, then every card as its own PNG, never a zip, the JSON last; files over the connector limit go to Rafi as files (SKILL 8.1).
- Headlines Master order block, A3, A7 and Cards 2.14: stories in deck order, then fun, teaser, Bigger Picture, ending (build_pack.py).
- Headlines Master A1: twelve-slot template (settled: 13 slots, porting list 4).
- Headlines Master A2 and 15 Sep 5: stored intro bypassed; ending wording = pack_base slot 13 text; stored clips are the option 4 pair of 3 Oct (settled; missing in DRIVE_DIFFS, 2d).
- Headlines Master A3: seven card stories in deck order, the strongest by score, normally robotics plus law, research or society (today no Research card: law C13-01 or society C14-01). See clash 3.
- Headlines Master A4: fun clip, bypass allowed if weak (settled: every clip generated; missing in DRIVE_DIFFS, 2d).
- Headlines Master A5, A6, A8: teaser only from the teaser card; Bigger Picture in slot 11 opening "And for the bigger picture"; about 90 s of content.
- Headlines Master B1 and B1a: 12 s, two decimals, no rounding (settled: 10 s and round up, DRIVE_DIFFS 5; rounding missing in DRIVE_DIFFS, 2d).
- Headlines Master B2: Cards Section 3 words; the robotics clip says what the robot does (C11-10's entry: vacuums, stirs food, takes out the trash, sorts car parts).
- Headlines Master B2a: every story and fun clip opens with a spoken introduction; teaser "Also in the full report." (full stop, lesson 64); Bigger Picture "And for the bigger picture". Evidence: check B2a.
- Headlines Master B3: numbers as words, no digits. Evidence: check B3, check_wording.py.
- Headlines Master B2 (prompt) and the prompt file: text-free screen and "nothing else changes" (settled: REAL TV SCREENS, DRIVE_DIFFS 19; the tone line missing in DRIVE_DIFFS, 2d).
- Headlines Master C: references 1 hands-on-table and 2 fists (fill asserts the 29 Sep pair); every visible field overwritten; titles start "SUN 11 OCT 2026"; slot table and stale word scan; mirrors written; JSON to Rafi as a file, never zipped; steps 6 (settled: 8, missing in DRIVE_DIFFS, 2d).
- Headlines Master G1.1 and 15 Sep 1: sound spelling; cue only where spoken (N-vidia for C06-01 or C08-01, an-thropic for C16-03); 15 Sep 2: "Google DeepMind".
- Headlines Master G1.2: a two to three word tag for a company under 100 billion dollars (Reflection AI, Easy Fox, KingMed Diagnostics, Counterpoint).
- Headlines Master G1.3: one idea per sentence (clash 17). G1.4: hedges kept, outlet never spoken (check G1.4).
- Headlines Master G2: introductions rotate (clash 8).
- Headlines Master G3: the scene sits inside the pane at the logo's place and size (fill PROMPT keeps it); G3.4 positive phrasing versus the explicit bans of 15 Sep 3 and REAL TV SCREENS (settled by REAL TV SCREENS).
- Headlines Master G7.3: teaser credit (clash 9). G8.1: JSON plus script pack when Rafi asks for "the prompt". G9.2: rounding removed (settled: CLAUDE.md rounds up).
- Headlines Master 15 Sep 3: no readable screen text (settled; Bigger Picture warning words, DRIVE_DIFFS 16).
- Phrasing file EVERY WRITER, EVERY ITEM: the line is in wording_common, wording_headlines and the rewrite brief.
- Phrasing 1.1 to 1.8: banned words (check_wording.py BANNED), headline a full sentence, card body two sentences, numbers translated, no drama, first hearing test, never lift a sentence (make_cards.py prints LIFTED FROM REPORT; must be 0).
- Phrasing 1A: meaning check of every card and line against its entry (fact check agent); a line with a gap is not shown.
- Phrasing 1B: who, what, why in every card and clip.
- Phrasing 2A: Cards level 6; Headlines level 5 and the one flowing sentence shape (35 to 40 syllables, 8 to 9 s, never over 10).
- Phrasing 3.1: cover = yesterday's cover, only the date changes (make_cover.py).
- Phrasing 3.2: one or two desk analysis cards (settled: one Bigger Picture card; missing in DRIVE_DIFFS, 2d).
- Phrasing 3.3 and 3.5: teaser 3 to 5 and web gap filling (settled: report items only, gate exactly 4; missing in DRIVE_DIFFS, 2d).
- Phrasing 3.4: at least three non-business cards and one robotics card. Evidence: count on the sheet.
- Phrasing 4.2 (open on Drive): reel teaser two items in about 8 s (wording_headlines.md), card teaser 4 items.
- Full Report 5.5 markets cap: does not apply to the Bigger Picture corner (rule 17).
- Full Report and Bulletin 5.3 and 11.4 (headline-only note): clash 15.
- Full Report and Bulletin 6.1 and 6.2 (publisher named, direct link, no redirect): 0c.4 recheck: 0 Google News links in 105 report and 30 Bulletin stories (counted).
- STORAGE lines 4 to 10: the label line says Claude's is "_Claude-LV1.1" (settled: _Claude-V1, lesson 231).
- STORAGE lines 36, 44 to 47: card name rule; five product folders, each with supportive files; one current card set plus one combined image; superseded outputs into cards/supportive files/archive; JSON, prompts and scripts into Headlines/supportive files.
- STORAGE line 50: a storage manifest at the date root with file IDs, hashes and the ordered card list. Gap: Part B writes none; ChatGPT's V1 run uses the same date folder (lesson 210), so never overwrite its manifest.

### 1c. Part B skill steps (process rules of the run)
- Step 0 setup: renderer zip (4,398,696 bytes, md5 598989503fa221cebe87c04bac903854), cover base (1,219,821 bytes), Pillow 12.3.0, fonttools 4.61.1 (prompts/partb_setup.txt). Step 0.1 also asks for rules_diff.py over the four rule files: W/rules holds Part A's 09:18 copies (STORAGE 11:28) and no Part B diff. Evidence to produce: the diff output or a note that the 09:18 copies are used.
- Step 0c: this file; 0c.4 PASS/FAIL table per section before step 7.
- Step 1: Fable picker, gate PASS, Rafi approves the list before wording. Evidence: gate_result.json, his message.
- Step 2: make_wording_prompts.py, two Fable agents (cards, Headlines) in one message.
- Step 3, 3a, 3b, 4: check_wording.py, then one round of four Opus agents (cards stranger, Headlines stranger, rules agent, fact check), one rewrite, then check_wording.py, check_headlines_rules.py and the rules agent on the changed lines only.
- Step 5: cover, cards copy, render into a new cards_runN, assemble (stops on a refused card).
- Step 6: build_pack.py (gate), fill_headlines.py (refuses to overwrite), verify_headlines.py.
- Step 7: review_list.py (gate), save_state.py, sheet and list to Rafi, STOP.
- Step 8: after approval: one file at a time, delivery_manifest.py --part B, Drive agent, --check, save_state.py, short report, lessons into docs/V1_TASKS.md.

### 1d. Lessons that touch Part B today
- P1-3 Fun Side 5 to 10, top 3 in the Bulletin: 0c.4 recheck 10 and 3. PASS.
- P1-4 Bulletin and report cutoffs stated: Bulletin 30 (purpose line names the cutoffs in words), report 105 at 5. PASS.
- P1-5 everything final to Drive; what the connector cannot take goes to Rafi: step 8 (clash 10).
- P1-6 14 to 15 story cards, company 2 clips and 3 cards, money cards 3, headline-only stories no card: G2, G8, G9, G10, G5.
- P1-7 news part about 90 s, round up: check_wording.py total, fill table.
- P1-8 hologram border: the fill PROMPT keeps the blue border line; the opening is stored.
- P1-9 when Rafi asks for the stories in the JSON, only the spoken words: review_list.py.
- P1-10 one file at a time, never a zip: step 8.1.
- P1-11 one home per rule: this file lists every double home in section 2.
- P1-16 check the approved opening first: option 4 stored, slot 1 bypass.
- P1-17 never build before Rafi's yes: no wording before the list is approved, no delivery before step 7 approval.
- P1-19 stop at a compaction: rule 18, clash 12.
- P1-20 match his numbered answers against the original list: at step 7 and on the clash answers.
- P1-21 show each step and wait; never drop a category silently: Research has no card today; say so with the reason.
- P1-22 no old JSON in a package; no unapproved screen wording: fill refuses to overwrite; screens go to Rafi in the review list.
- P1-27 Drive text uploads verified by size: drive_delivery.json drive_bytes = local_bytes.
- P1-29 meaning check before any JSON leaves: gate before step 7; no JSON before approval.
- P1-31 compute weekdays: 11 Oct is Sunday; 13 Oct Tuesday, 15 Oct Thursday, 27 and 28 Oct Tuesday and Wednesday, 29 Oct Thursday (computed).
- P1-32 read the governing file before quoting it: done in this file.
- P1-33 save cloud-only files: save_state.py before the step 7 wait and after delivery.
- P1-34 approved opening: superseded by the option 4 clips of 3 Oct (pack_base both bypass).
- P1-35 company limits (three OpenAI clips, five OpenAI cards on 30 Sep): G9, G10, C16.
- L1 plain English gate: script check plus stranger check; card sentences at most 15 words (wording_common.md rule 1; check_wording.py does not count words, 2b); headline = the deed first.
- Port-3 company limits: CARD_FILTER line, G9, G10.
- Port-4 13-slot template, Bigger Picture clip 11, stored ending slot 13: build_pack.py.
- Port-5 hologram border kept; the text-free symbol replaced by REAL TV SCREENS.
- Port-6 round up to the half second: fill_headlines.py.
- Port-7 the Bigger Picture at three lengths: card from bigger_picture_bulletin.json (clash 14).
- Port-8 deed first, 15-word card sentences, stranger check: wording_common.md, stranger_cards.md.
- Port-9 repeat check over earlier decks: now 7 days (G17 plus the manual table).
- Port-10 rule files named by their Drive names: in prompts and this file.
- Port-11 8 steps, 4 s voice sample, unhurried tone: fill CONFIG line, verify_headlines.py.
- Port-12 new opening and ending only on request: none asked; both bypass.
- 18 the voice sample lives on Rafi's PC: tell him the JSON names AIND_anchor_voice_sample_4s.wav (step 8.1).
- 19 stranger failure types (background words, watch item without why, two facts as one): in stranger briefs.
- 20 find first, write second: when Rafi names a file, locate it before writing.
- 22 Fable writes card and Headlines wording; Rafi's model headline in wording_common.md.
- 23 repeats over earlier decks: section 3 table.
- 24 credit clash: settled by lesson 46 and CLAUDE.md CREDIT; card SOURCE lines read at step 7.
- 25 card sentences over 15 words: the gate must count them (check_wording.py does not, 2b); the stranger and fact check briefs carry the cap.
- 29 follow-ups go to the Bigger Picture or teaser, not a card: cards yes; the teaser part is stale against G6 (2b).
- 30 Drive rules change between runs: rules_diff.py at step 0.1 (evidence missing so far, 1c).
- 31 reader levels: resolved in the phrasing file (cards 6, Headlines 5); briefs point there.
- 34 blocked sources: card credit goes to the first reporter, not the relay (C06-01 FT, C13-01 and C07-01 Bloomberg, C12-03 The Sunday Times).
- 35 stranger check is needed; start the wording early (step 2 at once after approval).
- 36 render check: count card files against the list; short labels (assemble_cards.py).
- 37 syllable budget, not words: wording_headlines.md line 14.
- 38 Bigger Picture card and clip give a reason to watch each item.
- 41 never ask what the record answers (voice sample on his PC).
- 42 Part B is its own skill: steps followed in order.
- 43 Bigger Picture card head: at most 85 characters, one sentence, at most 15 words.
- 44 a rule a script can enforce is never a question to Rafi: only wording choices and true clashes go to him.
- 45 Drive date folders, runs/<date> copy, no Routine yet: save_state.py; no Routine.
- 46 credit rule settled: first reporter credited.
- 47 Bigger Picture card label AIND: build_cards_copy.py.
- 49 compaction and fresh chat: rule 18, clash 12.
- 50 reply stories name the earlier story: check_wording.py; today only C16-06 qualifies.
- 53 the connector carries typed text; binaries often refused: step 8 (clash 10).
- 54 weekend window thin: today is Sunday and thin (section 3).
- 55 stranger failures (unintroduced names, jargon, idioms): stranger briefs.
- 56 Market labels about 10 characters: the Market category name is long (build_cards_copy.py warns over 46 characters).
- 59 the one lessons list: step 8.4 writes into docs/V1_TASKS.md.
- 60 introductions rotate, company tags: check G2, rules agent G1.2 (clash 8).
- 61 hard gate on the current lines: common_b.rules_gate in build_pack.py and review_list.py.
- 62 token cost: report helper tokens per stage.
- 63 stored opening and ending (option 4): pack_base both bypass.
- D1 do only the step he names; one-sentence report, then wait.
- D2 Headlines at level 5: who did what and why in everyday words; cut filler.
- D3 spoken names "N-vidia", "an-thropic", "Kawa saki" only where spoken: check 15Sep1.
- D4 no colon after "Also in the full report": check B2a.
- D5 8 steps, the 4 s wav, fixed seed: fill asserts (the h264_nvenc line is for Rafi's PC).
- D7 teaser and Bigger Picture credited AI NEWS DESK: clash 9 (the rest of D7 is the PC finish).
- D8 openings and endings are options; option 4 is the choice: bypass.
- 64 voice file .wav, teaser full stop, Kawa saki cue: fill AUDIO .wav, check B2a, cues.
- 66 old news in cards: cards only from the report after 9b plus the 7-day check.
- 67 "no company twice in a row" (Rafi to confirm; not in CLAUDE.md): note only; today Tesla C11-01 and C11-10 would sit side by side if both were cards.
- 68 the same event twice in a report: C11-12 and C08-04 (ONE TOPIC).
- 71 parallel sessions: fetch before every push (lesson 163: never rebase when histories differ).
- 72 Headlines shape checks (side clause, more than one comma, company-only why): check_wording.py; its word cap is gone (lesson 92).
- 73 structured who, what, why; no hand rewrite; gate on current lines: as WHO WHAT WHY FIRST.
- 74 one truth for writing rules: the phrasing file.
- 75 simple, not childish: stranger fails chopped lines.
- 76 model policy of 6 Oct: replaced in part by STORY CHOICE and BIGGER PICTURE MODEL (as in 1a).
- 77 and 101 long jobs through run_in_background, never a shell "&".
- 80 one event in several entries: C11-12 and C08-04.
- 81 Bigger Picture overstatements: the fact check reads the bp card and clip against the Bigger Picture texts and entries.
- 82 thin days: counts are guidelines; state them.
- 83, 98, 145, 163, 216 stale clone and a branch that moves under the run: git fetch and read new commits before each Drive step and each push.
- 85 Drive upload by retyping wastes tokens: clash 10.
- 89 Rafi's 7 Oct decisions: never Haiku; Drive agent only for text up to about 30 KB (clash 10); the base_min below report cutoff clash is not live (cutoff 5 today).
- 90 no shorthand to Rafi; full category names.
- 91 a count he gives wins over a cutoff: clash 1.
- 92 when a rule changes, grep for its old wording: section 2b.
- 93 update cards excluded by default; compare with the last 3 decks by name and topic: G6, the table.
- 94 novice test at choice time: G15b.
- 95 a question is not a decision: 8b item 1.
- 96 one check round, one rewrite round; checkers fail only rule breaks: step 3 (clash 7).
- 97 Politics clip 1 when the deck has a Politics card: G11b (clash 3).
- 100 helper prompts must not create sessions: no session tools in helper prompts.
- 107 which score counts: clash 11.
- 108 the automatic repeat match is a list to judge: G17 hits judged; C11-01 missed.
- 110 a second reader for the Bigger Picture: the fact check covers the bp lines.
- 111 the markets quarter cap does not bind the Bigger Picture corner: rule 17.
- 114 change only what was asked: step 7 edits.
- 115 show first, then act.
- 116 count the rounds per product before starting one.
- 117 check a figure before passing it on.
- 118 and 119 customer text rules and the headline-only note: 0c.4 recheck (clash 15).
- 121 compare old and new facts of every rewritten item: step 3a output against scripts_final_before_rewrite.json.
- 122 the contact sheet by display render, files by attach.
- 123 Part B in a new chat: clash 12.
- 124 the restart copy is text only.
- 125 commit and push after every change.
- 126, 173, 208 commits carry no model name, only the Claude-Session line (lesson 208: this wins over the session's attribution reminder).
- 127 estimate the cost of an agent before running it.
- 128 answer first, act after he asks, one question at a time.
- 129 scripts unchanged during a run: all script items of 2b wait.
- 131 step 0c before any choosing script: broken again today (selection_draft.json and pick_pack.json written 11:29, before this check); both are paper input, nothing is chosen.
- 134 and 135 robotics counts (Bulletin 3 to 5, cards 2 with one humanoid, Headlines 1; one extra allowed): clash 2.
- 136 one Bulletin file: products/bulletin_pdf.json only (30 stories = the delivered Bulletin). PASS.
- 137 the freshness flag does not know earlier decks: C05-02 and C11-01 say NEW but continue 9 Oct and 4 Oct cards.
- 138 a picker note is not a source: writers use entries and facts only.
- 139 the robotics clip says what the machine does: C11-10's entry does.
- 140 and 199 realistic screens: fill fixed by lesson 209; one stale brief line (2b).
- 141 screens static and wordless: rules agent.
- 142 list every clash once at 0c: clash 13 (rule 20 says one at a time).
- 144 helper tokens Part B: report per stage.
- 147 held stories must not be cited: G1, G16.
- 148 the Bigger Picture author is Fable max with an Opus second reader: done in Part A (lesson 224).
- 150 Bulletin cover in words, not codes: purpose line uses names. PASS.
- 154 no empty Bulletin section: PASS.
- 156 lock the report list: Part B never rebuilds products; if forced, bulletin_keep.py runs again (lesson 223).
- 157 the Musk and India Starlink row: C05-02 continues it; a 9 Oct card and clip (NO REPEATS).
- 158 freshness should date the newest development; "FOLLOW-UP of" only for a story we carried: C05-02 and C11-01 are mislabelled NEW.
- 161 two cards on one topic: manual pair check (no gate test yet).
- 162 Rafi's list changes meet the gate: name each override and his words (gate_overrides.json).
- 170 the manifest lists the pool PDF and prints CHAT: --check output.
- 171 and 174 viral stories scored by reach: C06-01, C05-01, C14-01 at 7 or more.
- 175 rule text only in his words: every fix here is marked as my wording.
- 177 and 178 the approved order for every product: G7 for the deck; check_order.py for Part A products.
- 179 customer text: 0c.4 recheck only, no fluency rewrite (lesson 190).
- 180 the six clashes of 10 Oct: all six still open today (clashes 1 to 5 and 7).
- 181 stale briefs and scripts of 10 Oct: rechecked in 2b (some fixed by lessons 198, 200, 209).
- 182 apply a viral floor only after checking earlier editions: Anthropic fake tip excluded (ran 10 Oct at 8); C14-01 is new.
- 183 link a follow-up by url and title, not a per-day id: when a card names an earlier story.
- 186 a CLAUDE.md copy loaded at session start goes stale: this check read the disk copy; every helper prompt must point at /home/user/ai-news-desk/CLAUDE.md (section 3).
- 188 the fun search is thin: the picker says so if nothing is funny at once.
- 190 find his exact complaint first: rule 20.
- 191 and 192 search before saying a robot story is missing: a humanoid story exists (C11-10).
- 193 robot war limit counted: section 3.
- 194 never ask what a rule decides; send the list itself.
- 195 may a follow-up of a printed story return in the Bulletin: still open; the delivered Bulletin carries four follow-ups (C04-01, C04-02, C09-01, C12-05); cards are settled by NO UPDATE CARDS.
- 196 the card list follows Rafi's order over the picker.
- 197 inside a full category compare appeal to a stranger, not only the score: Security has three eligible stories for two slots.
- 198 and 200 stale brief lines corrected on 10 Oct: rechecked in 2b.
- 201 one check round with four agents at once: step 3 (clash 7).
- 202 label at most 14 characters, no money figure: pick_stories.md (2b on the 14 against 15 lines).
- 203 review_list.py intro: now "photorealistic news scene". PASS.
- 204 the Drive agent must try a binary before calling it too large: drive_delivery.md line 6 (clash 10).
- 205 the 10 Oct summary: the prevention lines above.
- 206 the between-run fixes are present: delivery_manifest.py CHAT status, review_list.py intro, briefs factcheck.md and the one-round step 3. PASS by reading.
- 207 still open for Rafi: items 2, 3, 4, 5 (partly fixed by 209), 6, 7, 8, 9 (no change today).
- 209 stale Headlines lines fixed between runs (word cap, shape, photorealistic screen, 10 s): present in wording_common.md rule 1, wording_headlines.md, rewrite_headlines.md and fill_headlines.py lines 11, 18 and 95; three stale brief lines remain (2b).
- 210 a second run (ChatGPT's V1) saves into the same Drive date folder: check names before each upload, never overwrite its files or its storage manifest.
- 211 read the Drive storage standard before saying which layout is right: done here (STORAGE_STANDARD.txt).
- 212 delivery into the five product folders, no "reports" folder: delivery_manifest.py; the empty "reports" folder of lesson 216 stays unused.
- 213 delivery_manifest.py reads the saved standard and stops when its folder sentence differs: run it with W/rules/STORAGE_STANDARD.txt of 11:28.
- 214 cards carry the scan label on Drive: cards_11-10-26_INN_VL1_Claude-V1.png and the contact sheet.
- 215 the label is _Claude-V1, never taken from an old file name: delivery_manifest.json titles.
- D12 one short sentence to Rafi.
- D13 only what he asks, nothing extra.
- D14 if it cannot be done perfectly, say so and stop.
- D15 a manual step for him (dragging files into Drive): one step per message.
- D18 look in the files before asking.
- D19 when a script blocks, follow it; never change or override it.
- D20 never delete; ask before any outward-facing action (his PC paths not used here).
- D23 option 4 opening and ending ids: as APPROVED OPENING AND ENDING.
- D25 Headlines only from that day's cards: G11.
- D27 the seed never changes: fill keeps 1060749754396562.
- D28 a spelling fix changes only the spelling.
- D36 and D47 teaser and Bigger Picture credit "AI News Desk": clash 9.
- 218 viral_sweep.py gaps: Cage raised by hand (pool and entry at 7); Anthropic tip excluded.
- 220 thin Sunday: section 3.
- 221 products use the pool score: clash 11.
- 223 Bulletin sections without a 7 took exactly 2 from the report: section 3.
- 224 Bigger Picture lengths and unconfirmed dates: the card and clip keep "not confirmed" on the JPMorgan date.
- 225 to 227 fewer status messages, honest estimates, counts from the file list.
- 228 save_state.py writes an old session link and its push can be refused: fetch first; fix the message by hand.
- 229 clock times from date -u.
- 230 never rm.
- 231 the Drive standard's _Claude-LV1.1 line: CLAUDE.md _Claude-V1 wins.
- 232 Drive size rule asked to Rafi, no answer yet: clash 10.

### 1e. Rules and lessons that do not apply to Part B today (one line each, grouped)
Part A only (scan, pool, writers, editors, report and Bulletin build):
- CLAUDE.md 16 scan window: Part A.
- CLAUDE.md 16 SOURCES: Part A.
- CLAUDE.md 16 PER CATEGORY: Part A.
- CLAUDE.md 16 3 OCT 2026 RUN: Part A, one day only.
- CLAUDE.md 16 BIG OUTLETS: Part A.
- CLAUDE.md 16 FAMOUS PEOPLE RULE: a pool rule.
- CLAUDE.md 16 POOL PDF EVERY DAY: Part A step 11.
- CLAUDE.md 16 "temporary scan keeps running daily": no action in Part B.
- P1-1 scan window: Part A.
- P1-2 direct sources: Part A.
- P1-12 remove by title: pool.
- P1-13 never rebuild the pool: pool.
- P1-14 network access: setting.
- P1-15 checking reports before suggesting extra stories: Part B adds no story.
- P1-25 cut Google links: Part A.
- P1-26 re-dated feeds: Part A (41 held).
- P1-28 curators prefer readable outlets: Part A.
- P1-30 page access before fan-out: Part A.
- Port-1 scan window: Part A.
- Port-2 sources and per-category counts: Part A.
- 26 pool math: Part A.
- 27 fewer survive than the pool: Part A.
- 28 four-day repeat list: Part A.
- 32 writer proxies: Part A.
- 33 prefetch.py: Part A.
- 39 Bulletin balance: Part A.
- 48 write only what can print: Part A.
- 57 Bulletin spread: Part A.
- 69 and 78 pool CSV path: Part A.
- 79 check_dup14 looseness: Part A step 9b.
- 86 cheap wins in Part A: Part A.
- 88 Bigger Picture skill step 10: Part A.
- 102 SHORT warning: Part A.
- 103 finance supply: Part A.
- 104 direct feeds: Part A.
- 105 English-only filter: Part A.
- 106 fill to 110: Part A.
- 109 editors' unresolved list: Part A.
- 112 re-dated stories rule: Part A.
- 113 meaning check before the PDF: Part A.
- 130 "Why it matters" labels: Part A text.
- 146 pool against the last four pools: Part A.
- 151 report fill unedited: Part A.
- 152 Bulletin spread: Part A.
- 155 world politics pass: Part A.
- 159 report fill steering: Part A.
- 160 category flags: Part A.
- 164 report fill: Part A.
- 165 check_dup14: Part A.
- 166 editor holds: Part A.
- 167 robotics keep list: Part A.
- 169 pymupdf: Part A.
- 176 viral raises of 10 Oct: that day.
- 185 report fill drift: Part A.
- 187 sponsored content: Part A.
- 217 curator {EXTRA} slot: Part A.
- 219 Drive report texts for step 9b: Part A.
- 222 check_dup14 hits: Part A.
Rafi's PC, ComfyUI, stitch and audio (after the JSON):
- CLAUDE.md 11 subtitle canvas: on the PC.
- CLAUDE.md 12 subtitle approval: on the PC.
- CLAUDE.md 13 Windows scripts: Part B scripts run only in the cloud.
- 14 long clips: no clip over 10 s.
- 15 screen timelines: opening and ending are stored.
- 16 ending screen symbols: stored ending.
- 17 test JSON method: not asked.
- 58 Headlines D1 layout: video post.
- 143 ComfyUI crash: PC.
- D6 speech QA: PC.
- D9 layout picture upload: PC and Drive.
- D16 audio not heard: PC.
- D17 transcript misreads: PC.
- D21 Drive inputs versus PC copies: PC (its clash note waits for Rafi).
- D22 layout reference: PC.
- D24 stitcher path: PC.
- D26 read the stitcher first: PC.
- D29 one clip per API job: PC.
- D30 API prompt in the browser pane: PC.
- D31 donor word fix: PC.
- D32 donor of 10 Oct: PC.
- D33 the 7 Oct word fix: PC.
- D34 encode template: PC.
- D35 stitcher Decision Log check: PC.
- D37 cyan words and rolling strip: PC.
- D38 hologram date card: PC.
- D39 stale encoder files: PC.
- D40 final video upload: PC.
- D41 phone copy: PC, only on request.
- D43 PC tool paths: PC.
- D44 ComfyUI in the browser pane: PC.
- D45 large Drive downloads on Windows: PC.
- D46 PowerShell traps: PC.
- D48 person matte: PC, waiting.
Records, superseded or open items with no effect on today's Part B:
- CLAUDE.md 16 HAIKU TODAY ONLY: 8 Oct only.
- CLAUDE.md 16 TEST of 6 Oct (clips 1, 5, 8 video): replaced by REAL TV SCREENS.
- CLAUDE.md 16 OPENING AND ENDING OPTIONS: only when Rafi asks.
- CLAUDE.md 19 start line: Part B is started by Part A.
- P1-18 pgrep watcher: no watcher used.
- P1-23 proposals of 30 Sep: open, no Part B effect today.
- P1-24 open items of 28 to 30 Sep: no Part B effect today.
- 13 speaking speed test: Rafi has not picked; the 4.4 formula stays.
- 21 Sheets gap: no Sheet work.
- 40 Drive V1 folder scripts: not run here.
- 51 follow-up upgrade: later, V1.
- 52 V1 task list naming: record.
- 65 start messages: Part A start line.
- 70 Sonnet trial: record.
- 84 sortable pool: V1.
- 87 Part A tokens: record.
- 99 Haiku order in prompts: 8 Oct only.
- 120 test new checks on real cases: no new check today.
- 132 first robotics ruling: replaced by 134 and 135.
- 133 comparison test brief: no comparison run today.
- 149 Bigger Picture length: open for Rafi, Part A text.
- 153 Part A tokens: record.
- 168 Bigger Picture length: open, Part A.
- 172 low scores with high reach: no fun or low story affected today.
- 184 status labels in Word: PDFs, Part A.
- 189 tokens: record.
- D10 skill points to the storage document: done 30 Sep.
- D11 missing 30 Sep folders: history.
- D42 reports to Anthropic as PDF or TXT: not Part B.
- D49 desktop chat cannot see the skill: not this session.
- D50 four 7 Oct stories: history.
- D51 Drive lessons files archived: done.

## 2. CLASHES (two rules or lessons that demand opposite things today; nothing chosen, nothing applied)

1. Card count against the extra cutoff.
   A: CLAUDE.md lines 194-195 and 222 (CARD FILTER: extra slots only at extra_min 7 or more) and line 87-89 (rule 14: counts are guidelines, adjust to the day's pool); also AIMD file line 60 ("Do not fill slots with weak stories merely to reach a count").
   B: CLAUDE.md line 54 (8b item 4: a count Rafi gives wins over any cutoff), line 207-208 ("Aim: 14 story cards"), pick_gate.py line 109 (G2 passes only 14 or 15 cards), briefs/pick_stories.md line 23 ("exactly 14").
   Clash: under the filter only 11 story cards qualify today (the draft's 12 minus the 7-day repeats C05-02 and C11-01, plus C11-03 as the robotics base pick); the gate fails any deck under 14, so 14 needs 3 stories below 7.
   Fix A (count wins): add to CARD FILTER: "When fewer than target stories reach extra_min, the remaining slots go to the best read-in-full Bulletin stories at base_min or more, in score order, and the deck says so." Fix B (cutoff wins): add: "target is a ceiling; when extra_min leaves fewer, the deck is smaller and the number is stated; pick_gate.py G2 accepts it (script change between runs)." (wording mine, not yours)

2. The second robotics card against the extra cutoff.
   A: CLAUDE.md lines 223-226 (ROBOTICS: the cards carry 2 robotics cards, one humanoid); pick_gate.py lines 141-145 (G19 demands two when two qualify at base_min).
   B: CLAUDE.md lines 194-195 (CARD FILTER: a second card in a category is an extra slot, extra_min 7).
   Clash: today's robotics stories under the filter score 5 to 6 (C11-10 humanoid 5, C11-03 6 pool/5 writer; C11-01 is a 4 Oct repeat), so a second robotics card, and the humanoid if it is not the base pick, sit below extra_min.
   Fix A: add to ROBOTICS: "The second robotics card may score below extra_min." Fix B: add: "The second robotics card needs extra_min like any extra card; with none, one robotics card and Rafi is told." (wording mine, not yours)

3. Headlines clip 1.
   A: CLAUDE.md lines 216-217 (HEADLINES START WITH POLITICS: the Politics card's clip is clip 1, never skipped); pick_gate.py line 134 (G11b).
   B: CLAUDE.md lines 169-171 (HEADLINES ORDER: order and choice set ONLY by the Drive file) and line 199 ("the strongest card stories by score"); Headlines Master line 45 (A3); card_candidates.py lines 136-159; SKILL.md line 79.
   Clash: today's Politics candidates (C05-07, C13-08) score 5, the lowest in the deck; the draft's seven clips have no Politics clip, the gate demands it as clip 1.
   Fix A: add to HEADLINES ORDER: "Exception: HEADLINES START WITH POLITICS; the other six clips follow the Drive file." Fix B: add to HEADLINES START WITH POLITICS: "only when the Politics card is among the seven strongest card stories by score." (wording mine, not yours)

4. Model of the rewrite agent.
   A: CLAUDE.md lines 150-151 (MODEL POLICY: the rewrite agent runs on Opus).
   B: CLAUDE.md line 167 (WHO WHAT WHY FIRST: "a Fable rewrite agent"), line 153 (STORY CHOICE: Fable writes the wording), SKILL.md line 105 ("ONE Fable rewrite agent").
   Clash: step 3a runs today and needs one model.
   Fix A: in MODEL POLICY delete "and the rewrite agent" and add "the rewrite agent runs on Fable (WHO WHAT WHY FIRST)". Fix B: in WHO WHAT WHY FIRST write "an Opus rewrite agent" and change SKILL.md line 105 to match. (wording mine, not yours)

5. An update as a card.
   A: CLAUDE.md lines 196-197 (CARD FILTER: a meaningful update can be a card) and line 190 (NO OLD NEWS: the same); SKILL.md lines 74-76.
   B: CLAUDE.md lines 202-204 (NO UPDATE CARDS: only when Rafi names it, default none) and line 205 (NO REPEATS IN 7 DAYS).
   Clash: today the only read Research stories (C04-01, C04-02) and C09-01, C12-05 are updates; no update_allowed.json exists.
   Fix A: in CARD FILTER and NO OLD NEWS replace "A meaningful update of an earlier story can be a card" with "An update is a card only under NO UPDATE CARDS (Rafi names it)". Fix B: add to NO UPDATE CARDS: "except a meaningful update (a decision, a confirmation, a first result or a new party) of a story that was not a card or clip in the last 7 days; the card names the earlier story." (wording mine, not yours)

6. Every category gets a card.
   A: briefs/pick_stories.md lines 8-11 (MUST-HAVES, Rafi 7 Oct: every category gets a card; use the reserve; "you may never call a required slot padding") and line 36 (reserve exception).
   B: CLAUDE.md lines 200-201 (CARDS FROM THE BULLETIN), 193-194 (CARD FILTER: a category keeps its best story only if it scores base_min), 202-204 (NO UPDATE CARDS), 198 ("Only stories read in full").
   Clash: Research has no eligible story anywhere today (C04-01, C04-02 updates; C04-04 headline only, writer score 4); the brief demands a card, CLAUDE.md allows none. The MUST-HAVES are not in CLAUDE.md (rule 8 gap, 10 Oct clash 1).
   Fix A: add to CARDS FROM THE BULLETIN: "A category with no eligible Bulletin story takes the best eligible Full Report story (base_min or more, read in full, not an update), marked exception; with none, it has no card and Rafi is told." Fix B: replace pick_stories.md line 8's first sentence with "every category gets a card when it has a story that CLAUDE.md CARD FILTER, CARDS FROM THE BULLETIN and NO UPDATE CARDS allow; otherwise left_out_notes says why." (wording mine, not yours)

7. Nothing with a FAIL against one round.
   A: CLAUDE.md lines 146-147 (HEADLINES RULES RECHECK: nothing goes to him with a rules FAIL); SKILL.md lines 61-62 (0c.4: zero mistakes, nothing shown with an open FAIL), line 101 and line 125 ("until it says all pass", "until both pass"), lines 180-181.
   B: CLAUDE.md line 57 (8b item 7: one check round and one rewrite round, then show Rafi what is left).
   Clash: after the one rewrite round, any FAIL left either blocks step 7 or goes to Rafi (cost on 10 Oct: over an hour, lesson 201).
   Fix A (lesson 201's text): 8b item 7: "No check loops: one check round and one rewrite round per stage. A fact error or rules fail found by the later checks always gets one more fix round before Rafi sees it." Fix B: add to HEADLINES RULES RECHECK: "after one check round and one rewrite round, a remaining FAIL is shown to Rafi with its line." (wording mine, not yours)

8. Introductions: Rafi's list against rotation.
   A: CLAUDE.md lines 173-177 (HEADLINES INTROS AND FLOW: the natural order "In finance", "Also in finance", "In security", "In robotics", "In tech", "In the lab", "And finally, something lighter" ...; "The intros Rafi dictates win over rule G2").
   B: CLAUDE.md line 147 (never the previous day's wording, G2); Headlines Master line 127 (G2); check_headlines_rules.py lines 82-90 (FAIL on any intro of the previous day).
   Clash: 10 Oct used "In finance" and "In robotics"; if today's writer uses Rafi's list, the script fails G2; it is not written whether that list counts as "dictated".
   Fix A: add to HEADLINES INTROS AND FLOW: "The intros listed here are examples; G2 rotation applies to them." Fix B: add: "The intros listed here may repeat day to day; check_headlines_rules.py G2 skips them (script change between runs)." (wording mine, not yours)

9. Teaser credit in the pack.
   A: build_pack.py line 41 (teaser source "DAILY GLOBAL AI INTELLIGENCE REPORT"); Headlines Master line 157 (G7.3).
   B: docs/V1_TASKS.md D7 (line 296: teaser and Bigger Picture credit AI NEWS DESK) and D36 (lines 636-638: never "DAILY GLOBAL AI INTELLIGENCE REPORT", 10 Oct); D47 (lines 669-671) leaves it to Rafi.
   Clash: today's pack slot 10 "source" feeds the credit strip of the stitch; CLAUDE.md does not settle it (its repo-wins line covers CLAUDE.md lines only).
   Fix A: CLAUDE.md line: "The teaser and the Bigger Picture are credited AI News Desk (Rafi, 10 Oct 2026); build_pack.py follows between runs." Fix B: note under D36: "the pack keeps DAILY GLOBAL AI INTELLIGENCE REPORT until Rafi changes Drive G7.3; the PC finish credits AI News Desk." (wording mine, not yours)

10. Drive upload of the cards and the JSON.
   A: Part A SKILL.md line 219 and lesson 89(d) (lines 401-403): the Drive agent only for text files up to about 30 KB; larger files to Rafi in chat.
   B: Part B SKILL.md lines 169-176 (the agent puts cards, contact sheet, JSON, pack and scripts into Drive); briefs/drive_delivery.md line 6 (try the smallest binary first; never call a file too large without a failed attempt, lesson 204); CLAUDE.md lines 13-17 (rule 0: save the day's products, cards and Headlines included, verified by size).
   Clash: today's Part B files are about 19 PNGs, a contact sheet and a JSON of about 370 KB; lesson 232 put the question to Rafi, no answer yet.
   Fix A: Part B SKILL.md step 8.2: "The Drive agent takes only text files up to about 30 KB (Part A step 13); PNGs, the contact sheet and the JSON go to Rafi in chat." Fix B: Part A SKILL.md line 219: "The Drive agent tries every file, smallest binary first (drive_delivery.md); a refused file goes to Rafi in chat." (wording mine, not yours)

11. Which score counts for the cards.
   A: card_candidates.py line 97 (score from products/bulletin_pdf.json = the pool score); build_products.py lines 13 and 59-60; docs/V1_TASKS.md lesson 221 (line 729: products use the pool score, "Rafi's ruling").
   B: pick_gate.py lines 68, 76 and 142 (pick pack and eligibility use report_entries "score" on disk = the writer's score), and briefs/pick_stories.md line 23 ("high score first") read from that pack.
   Clash: 15 of 30 Bulletin stories differ by one point (for example C08-01, C10-01, C11-01, C12-03, C05-02, C07-02: pool 7, writer 6), so extra_min 7 and "high score first" give different decks to the script and to the Fable picker.
   Fix A: add to CARD FILTER: "The score is the pool score that the Bulletin prints (build_products.py)." Fix B: add: "The score is the writer's score (report_entries); the Bulletin's printed score is not used for cards." (wording mine, not yours)

12. Part B in the same chat.
   A: docs/V1_TASKS.md lesson 123 (line 459: "Part B needs a new chat (rule 18)"); CLAUDE.md lines 259-262 (rule 18).
   B: CLAUDE.md lines 69-70 (rule 9: Part A starts part B by itself); SKILL.md line 3 ("Started by Fill_categories_scan_part_A when its products are delivered").
   Clash: today Part B starts in the chat that delivered Part A.
   Fix A: add to rule 18: "Part B continues in Part A's chat unless that chat was compacted." Fix B: add to rule 9: "Part A ends with the handoff; Part B starts in a new chat." (wording mine, not yours)

13. How the clashes go to Rafi.
   A: docs/V1_TASKS.md lesson 142 (line 480: at step 0c list every clash once, with a recommendation each).
   B: CLAUDE.md line 267 (rule 20: "ask them one by one"); lesson 194 (line 534).
   Clash: today there are 17 clashes to put to him.
   Fix A: add to rule 20: "At Part B step 0c all clashes go to Rafi once, as a numbered list of one line each, and he answers by number." Fix B: replace lesson 142's prevention with "ask the clashes one at a time, the most blocking first." (wording mine, not yours)

14. Who writes the Bigger Picture card and clip.
   A: CLAUDE.md line 158 (BIGGER PICTURE MODEL: one agent writes all three lengths) and line 210 (Fable writes it, all three lengths); rule 17 lines 255-258 (the card is one of the three lengths).
   B: SKILL.md lines 86-88 and briefs/wording_cards.md line 11, briefs/wording_headlines.md line 9 (the card and Headlines wording agents write the Bigger Picture card and clip).
   Clash: Part A's author wrote only the Full Report and Bulletin versions; today's card and clip would come from other agents.
   Fix A: add to BIGGER PICTURE MODEL: "the Part A author also writes the card head and body and the clip line (bigger_picture_card.json); Part B copies them." Fix B: add: "the card and clip are written by Part B's Fable wording agents from the Bulletin version." (wording mine, not yours)

15. The headline-only note and paragraph limits in the 0c.4 recheck.
   A: SKILL.md lines 59-62 (0c.4 recheck of the Full Report and Bulletin text: paragraph limits, no internal wording for customers); lessons 118 and 119 (lines 454-455: Bulletin at most two paragraphs; customers should not see the note).
   B: Bulletin_V1_Rules_Structure.txt lines 145-147 and 212 (5.3 and 11.4: headline-only stories carry the note); Full_Report_V1_Rules_Structure.txt lines 155-157 and 239.
   Clash: 4 Bulletin stories have a third paragraph (the note) and 20 Full Report stories carry it; both products are already with Rafi. Lesson 118 is not in CLAUDE.md (lesson 207 item 3), so the repo-wins line does not settle it.
   Fix A: CLAUDE.md line: "Customer text (Rafi, 8 Oct 2026): the headline once; no repeated paragraph; Bulletin at most two paragraphs, Full Report three; no process notes; the headline-only note is not printed." Fix B: SKILL.md 0c.4: "paragraph limits follow Drive Bulletin 5.3 and Full Report 5.3 (the headline-only note is the allowed third paragraph)." (wording mine, not yours)

16. What goes with the card list.
   A: CLAUDE.md lines 203-204 (NO UPDATE CARDS: the 3-day comparison table is shown before Rafi sees a deck); line 53 (8b item 3: show the comparison); SKILL.md line 80 ("Show Rafi the LEFT OUT list with every selection").
   B: CLAUDE.md line 268 (rule 20: when he asks for the card list, send the list, short, in deck order, with nothing else).
   Clash: the list goes to Rafi for approval today (STORY CHOICE); one line demands the table and LEFT OUT list with it, the other the list alone.
   Fix A: add to rule 20: "except the 3-day comparison table of NO UPDATE CARDS, sent as a second short message." Fix B: add to NO UPDATE CARDS: "the table is shown only when Rafi asks; the list itself carries no table." (wording mine, not yours)

17. One idea per sentence against one flowing sentence.
   A: Headlines Master line 123 (G1.3: "Plain words, one idea per sentence"); briefs/rules_check_headlines.md line 13 (the rules agent checks G1.3).
   B: CLAUDE.md lines 163-164 (HEADLINES SHAPE: set in the phrasing file) and the phrasing file lines 100-102 (ONE flowing sentence that carries who, what and why together).
   Clash: the rules agent may fail a correct flowing line for G1.3 (the 7 Oct pattern of lesson 92).
   Fix A: rules_check_headlines.md: "G1.3 is read as plain words; the shape is the phrasing file's one flowing sentence (CLAUDE.md HEADLINES SHAPE)." Fix B: CLAUDE.md: "G1.3 applies; a clip is two short sentences, the second carrying the why." (wording mine, not yours)

18. One plain recommendation against every option (added 13 Oct, lesson 276).
   A: docs/V1_TASKS.md lesson 238(4) (from the local Part B session: "give one plain recommendation").
   B: CLAUDE.md rule 1 (present ALL viable paths, each with what Rafi does, the risk and which one Claude recommends) and Rafi's OPTIONS preference (never withhold an option).
   Clash: a reply with only one recommendation drops the other options rule 1 asks for.
   Fix A: lesson 238(4): "give every option in one short line each, then one plain recommendation." Fix B: rule 1: "for small tasks give one plain recommendation; list all options only for big tasks." (wording mine, not yours)

### 2b. Stale brief and script lines against a newer CLAUDE.md line (scripts change only between runs, CLAUDE.md line 160)
- SKILL.md line 3: "gets the wording from Opus agents (CLAUDE.md MODEL POLICY)" against STORY CHOICE line 153 (Fable writes) and SKILL step 2 (model "fable").
- SKILL.md line 52: "every lesson, numbered, currently 1 to 130": the file now runs to 232 plus P1 and D lines.
- SKILL.md line 58: "Where a Drive file and CLAUDE.md disagree, STOP and ask Rafi" against line 206 (THE REPO IS THE SOURCE OF TRUTH: no clash, CLAUDE.md wins).
- SKILL.md lines 74-76: an update kept when meaningful, against NO UPDATE CARDS lines 202-204 (clash 5).
- SKILL.md lines 77-79: selection.json written by hand, clips "strongest card stories by score", against STORY CHOICE (the gate writes selection.json) and lines 216-217 (Politics clip 1).
- SKILL.md line 77: "teaser_items (3 to 4 stories)" against pick_gate.py G2 and pick_stories.md line 26 (exactly 4).
- SKILL.md lines 153-154: "C01 and C13 carry Rafi's opening and ending of 2 Oct 2026" against APPROVED OPENING AND ENDING lines 242-245 (pack_base already has both bypass; text only).
- SKILL.md line 180 and check_wording.py line 7: a card sentence over 15 words fails the gate, but check_wording.py never tests it (line 62 counts words and drops the count); only the stranger and fact check briefs carry the cap.
- check_wording.py lines 6-10 (docstring): Headlines "the same sentence rules" (15 words), "Bigger Picture warns past 11.5 s, nothing may pass 12 s", against HEADLINES SHAPE (no word count) and CLIP SECONDS (10 s); line 103's 11.5 s warning can never fire (line 115 FAILs over 10).
- check_headlines_rules.py lines 5 and 8 (docstring): "15 words ... 12 s", "never over 12 s", against CLIP SECONDS; the code (line 70) uses 10.
- verify_headlines.py line 24: passes clips up to 12 s, against CLIP SECONDS (fill line 95 already stops at 10).
- build_pack.py line 26: "may not pass 10 (Drive Headlines Master Section B item 1, 5 Oct 2026)": the Drive file says 12; the 10 is CLAUDE.md CLIP SECONDS.
- build_pack.py line 41: teaser source "DAILY GLOBAL AI INTELLIGENCE REPORT" (clash 9).
- briefs/stranger_headlines.md line 3: "the bigger picture line at most 48" syllables, against CLIP SECONDS (44 = 10 s; 48 gives an 11 s box that check_wording.py fails). Lesson 198 fixed only wording_headlines.md.
- briefs/rules_check_headlines.md line 15: "two full natural sentences after the introduction ... about 20 words at most", against HEADLINES SHAPE lines 163-164 (phrasing file: one flowing sentence; a second only when the why cannot ride). Lesson 209 fixed the writer and rewrite briefs, not this one.
- briefs/wording_headlines.md line 9: example introduction "On the road", against HEADLINES INTROS AND FLOW lines 176-177 (the "On the road" label for robotics that made Rafi furious).
- briefs/wording_headlines.md line 19: "no identifiable faces, since the fixed video prompt says no faces", against REAL TV SCREENS line 186 (no real named faces) and fill_headlines.py line 18 (no longer says no faces); line 16 of the same brief allows anonymous people.
- briefs/pick_stories.md line 25 (label at most 14), line 37 (at most 15), pick_gate.py line 137 (G14: 15), SKILL.md line 77 (about 15): no CLAUDE.md line; lesson 202 says 14.
- briefs/pick_stories.md line 35: "(none today)" is written into the brief for every day; true today only because update_allowed.json is absent.
- card_candidates.py lines 161-165: the teaser draft takes updates (today C09-01 and C04-01), which pick_gate.py line 119 (G6) fails; lesson 29 (line 157) still sends follow-ups to the teaser, against NO UPDATE CARDS and NO REPEATS IN 7 DAYS as the gate applies them.
- card_candidates.py lines 72-79 and 96: repeat check over 3 decks by headline words only, against NO REPEATS IN 7 DAYS line 205; the draft keeps C05-02 and C11-01.
- card_candidates.py lines 136-159: Headlines without the Politics clip (clash 3).
- card_candidates.py line 185: bp_refs = the top Market and Energy stories (C06-01, C05-02, C07-01), against rule 17 and wording_cards.md line 11 (the card rests on bigger_picture_bulletin.json, whose stories are C07-02, C07-03, C07-08, C07-01, C06-01, C05-08; C05-02 is not in it and is a 9 Oct thread).
- make_wording_prompts.py lines 18-21: PREV_CARDS and PREV_PACK come only from scratchpad run_ folders; today "none" and assets/pack_base.json (2 Oct; review_status "sentences of at most 15 words") becomes the Headlines writer's shape example, against HEADLINES SHAPE (no word count). The intros list uses prev_scripts (runs/2026-10-10) and is right.
- briefs/factcheck.md line 5: fix limit "spoken line one flowing sentence 35 to 40 syllables" with no allowance for the Bigger Picture line (up to 44, rule 17 and CLIP SECONDS).

### 2c. Checked, not live today
- VIRAL RULE re-run clause against G6 and G17: no viral story today is a re-run (C14-01 new; C06-01 and C05-01 new at 8; the Anthropic tip excluded).
- Lesson 89: base_min 5 below a report cutoff of 6: the report cutoff is 5 today.
- Critical stories spending a slot: no score 10.
- Cards Master 2.10 big release rule: not in force.
- Robot war limit on cards: no such limit exists.

### 2d. Drive differences settled by CLAUDE.md but missing in docs/DRIVE_DIFFS_FOR_CHATGPT.md (CLAUDE.md line 207: every difference)
- Headlines Master A4 (bypass a weak fun clip) against "every clip of the JSON is generated" (CLAUDE.md 182-183).
- Headlines Master B1a and G9.2 (two decimals, no rounding) against round up to the half second (109-110, 126-127).
- Headlines Master C4 and G5.2 (six steps) against 8 steps (231-236).
- Headlines Master A2 and 15 Sep 5 (the 15 Sep ending clip) against the option 4 clips of 3 Oct (242-245).
- Headlines Master A3 (the strongest card stories by score) against Politics clip 1 (216-217).
- Headlines Master B2 ("nothing else in the prompt changes") against the unhurried tone line (231-236).
- Phrasing 3.2 (one or two desk analysis cards) against the one Bigger Picture card (134-135).
- Phrasing 3.3 and 3.5 (teaser of 3 to 5 that may carry a missed story; web gap filling) against cards and teaser from report stories only (200-201, 152-155).
- STORAGE line 7 ("The current Claude scan's _Claude-LV1.1 label is unchanged") against _Claude-V1 (lines 20-22; lesson 231 says item 21 covers it, but item 21 does not quote this line).

## 3. Facts of this edition that the cards and Headlines must respect
- Edition SUN 11 OCT 2026; window 10 Oct 09:18 to 11 Oct 09:18 UTC (24 hours); no critical story; highest score 8 (C06-01, C05-01, C12-02).
- Full Report 105 stories at cutoff 5 (Politics 5, Market 15, Security 11, Energy 12, Robotics 12, Models 14, Research 3, Ethics and law 4, Health 11, Society 8, Fun 10); 85 read in full, 20 headline only (they carry the note). held.json: 41 re-dated plus 10 duplicates = 51.
- Bulletin 30 stories: Politics 2 (C05-07, C13-08, both 5), Market 4, Security 4, Energy 2, Robotics 5, Models 2 (C02-01 headline only, C01-02), Research 2 (both follow-ups), Ethics and law 1, Health 3, Society 2, Fun 3. Headline only, so never a card: C07-02, C11-02, C02-01, C10-03.
- Scores: products/bulletin_pdf.json prints the pool score; report_entries on disk hold the writer's score; they differ for 15 of 30 Bulletin stories (pool/writer: C05-02 7/6, C07-02 7/6, C12-03 7/6, C12-05 7/6, C08-01 7/6, C11-01 7/6, C10-01 7/6, C11-02 6/5, C11-03 6/5, C02-01 6/5, C04-02 6/5, C10-02 6/5, C10-03 6/5, C16-03 3/2, C16-08 3/2). selection_draft.json shows pool scores; pick_pack.md, which the Fable picker reads, shows writer scores (clash 11).
- Viral (viral.json and viral_raised.json): Nvidia and Reflection AI talks 24 outlets (C06-01, 8, new), Nadella 21 outlets (C05-01, 8, new), Nicolas Cage waiver 36 outlets by hand (C14-01, raised 6 to 7, new; the sweep counted 11); Anthropic fake homicide tip 44 outlets excluded (ran 10 Oct as C12-01 at 8; today's copy held as re-dated).
- Card-eligible Bulletin stories (read in full, entry freshness NEW, not held; robotics with a machine doing something), before the 7-day check: Politics C05-07, C13-08; Market C06-01, C05-02, C07-01; Security C05-01, C12-02, C12-03; Energy C08-01; Robotics C11-01, C11-03, C11-10; Models C01-02; Research none; Ethics and law C13-01; Health C10-01, C10-02; Society C14-01, C14-02. After removing C05-02 and C11-01 (7-day repeats): 16, at most 15 with the 2-per-category limit (Security has 3). Fun candidates: C16-03 (pool 3), C16-08 (3), C16-01 (2).
- Thin today: Politics (two stories at 5); Research (no eligible story: C04-01 and C04-02 are follow-ups, C04-04 is headline only at writer score 4); Models (only C01-02 at 5, a pricing-page sighting); Energy (only C08-01, an Nvidia gaming card leak); Ethics and law (only C13-01); Fun (scores 2 to 3; lesson 188).
- Robotics: the only humanoid story with a machine doing something is C11-10 (Tesla Optimus learns chores from first-person video; 5; PRELIMINARY; chain "Startup Fortune, citing Drive Tesla Canada and eWeek"). C11-03 is a war story (US Army drone exercise; WSJ read in a relay). C11-12 (Counterpoint forecast, no machine) is the same event as C08-04 (report, Energy). Robotics outside the Bulletin (usable only as an exception): C11-06 Dubai driverless pods, C11-08 humanoid rental prices, C11-09 ICE robot dogs, C11-11 shop robots in China (all 5).
- Robot war count (0c.4 recheck): Full Report 3 (C09-01 Yandex drone strike, C11-02, C11-03) = the cap of 3; Bulletin 2 (C11-02, C11-03) or 3 if the Yandex drone strike counts, as lesson 193 counted it on 10 Oct (cap 2).
- Follow-ups by entry freshness: in the Bulletin C04-01 (of 10 Oct), C04-02 (9 Oct), C09-01 (10 Oct), C12-05 (9 Oct); report only C05-08, C07-09, C12-07, C12-13, C09-07, C09-11, C09-13, C11-07, C01-05, C14-13, C16-06. The pool flags C05-02 and C05-03 as follow-ups while their entries say NEW.
- Stories that continue a card or clip of 4 to 10 Oct: C05-02 Musk Starlink India pledge (9 Oct card s2 C13-21 and clip; its entry note says the row ran 9 and 10 Oct); C11-01 Tesla Cybercab Austin fleet (4 Oct card s9 C11-04 and clip "On the road"; G17 does not flag it); C09-01 Yandex third data centre (8 Oct card s6 and clip); C12-07 and C12-13 Korean bank hacks (6 Oct card s6 and clip). To judge, likely new events: C06-01 Nvidia talks on Reflection AI (Reflection's model was a card and clip on 5 and 6 Oct); C11-10 Optimus (8 Oct teaser: Optimus output of 1,000 a week); C12-02, C05-01 and C13-01 sit in the rogue-AI topic of 10 Oct (cards s3 Claude fake tip, s4 disaster rehearsal) and 7 Oct (s12 senators on AI liability) but are different events. G17 false matches to dispute with proof if flagged: C14-02, C16-03, C11-02.
- Reply stories (check_wording.py test): C16-06 only (Fun reserve).
- Company counts possible: Nvidia 2 (C06-01, C08-01), Tesla 2 (C11-01, C11-10), OpenAI 2 (C12-02, C01-02), Microsoft 1, Amazon 1, Anthropic 1 (fun C16-03).
- The draft (card_candidates.py, paper only): 12 story cards plus fun (C05-07, C06-01, C05-02, C07-01, C05-01, C12-02, C08-01, C11-01, C01-02, C13-01, C10-01, C14-01; fun C16-03): no Research card, one robotics card, no humanoid; clips C06-01, C07-01, C05-01, C12-02, C08-01, C11-01, C13-01 (no Politics clip); teaser C12-03, C09-01 (update), C11-03, C04-01 (update); bp_refs C06-01, C05-02, C07-01.
- Bigger Picture source (bigger_picture_bulletin.json, 513 words): AI borrowing slowing (C07-02, FT; the 23 billion dollar figure rests on one relayed sentence), big clouds still borrowing (C07-03), Oracle against Nvidia (C07-08), Korea outflows (C07-01), Nvidia and Reflection AI (C06-01), Apollo's Slok (C05-08). Watch: TSMC results 15 Oct (Thursday), JPMorgan 13 Oct (Tuesday; its page lists no date today: not confirmed), the Fed 27 to 28 Oct, Microsoft 28 Oct, Samsung 29 Oct; ends "not financial advice". Yesterday's clip already watched JPMorgan on Tuesday; AI debt led the Bigger Picture card on 4, 5, 7 and 8 Oct (rule 17: never a vague restatement).
- Introductions used on 10 Oct (G2): "From Beijing", "In finance", "Next, safety", "In robotics", "On chatbots", "In court", "In science"; fun "On a lighter note".
- The CLAUDE.md copy carried in this session's context at start is older than the disk file (it has no rules 8a, 8b, 20, 21, STORY CHOICE or ROBOTICS, says CARD_FILTER target=15 and Fable only on Rafi's word): every helper prompt must point at /home/user/ai-news-desk/CLAUDE.md on disk (lesson 186).
- Drive 2026-10-11 already holds ChatGPT's V1 run folders (lesson 210) and an empty "reports" folder from Part A (lesson 216).
- Last 7 days of cards and Headlines (runs/<date>; clip intros in brackets):
- 2026-10-04 CARDS: s1 C13-01 US intelligence chief to lead a White House AI task force | s2 C06-01 AI companies gave Hong Kong its biggest summer of share sales | s3 C07-02 US Treasury chief: rising borrowing costs worldwide | s4 C05-07 Airbnb unlikely to let AI assistants book stays | s5 C05-01 Altman on AI and religion, read as a reply to Anthropic | s6 C05-03 David Robinson, who quit OpenAI's safety team, says its culture is broken | s7 C08-01 Musk confirmed talks with TSMC on his Terafab chip plant | s8 C08-03 Samsung charges more as TSMC is full | s9 C11-04 Tesla's Cybercab had a bumpy first month in Austin | s10 C01-01 Google gives free Gemini users only its weakest version | s11 C04-02 US and 15 countries to make AI the centre of science | s12 C14-01 Jr NTR vowed to sue over an explicit AI fake of his co-star | s13 C10-02 Mayo Clinic AI flagged pancreatic cancer risk up to five years early | s14 C14-02 Child safety group rated Google's AI answers unsafe for children | fun C16-01 French TV host knocked two boxing robots flat | teaser C05-02 Treasury chief: AI labs must own the risks, C12-01 out-of-control OpenAI programs targeted a UN website, C11-01 Kawasaki humanoid by 2030, C01-03 Aleph Alpha free model for governments | BP share buyers rush into AI while debt watchers warn || HEADLINES: C13-01 [In politics]; C06-01 [On the markets]; C05-03 [On safety]; C08-01 [In chip making]; C11-04 [On the road]; C14-01 [In law]; C10-02 [In medicine]; fun C16-01 [On a lighter note]; teaser C05-02 + C11-01.
- 2026-10-05 CARDS: s1 C13-07 British lawmakers: government leans too hard on US cloud firms | s2 C06-03 Schneider Electric to buy PTC | s3 C08-01 Qualcomm to pay Huawei for patents | s4 C07-05 Bank of Japan deputy: AI may keep rates higher | s5 C12-05 hackers posed as Anthropic staff to send malware | s6 C08-07 TSMC plans another price rise | s7 C09-03 Goldman: local opposition barely dents US data centre forecast | s8 C11-04 Germany pays for drones that hunt Russian drones | s9 C01-01 Reflection readying a strong US-made open AI model | s10 C04-05 Korean researchers: AI drug-safety predictors overrated | s11 C05-01 Altman: accept some harm from AI | s12 C10-01 Stanford: 37,000 AI helpers read old drug trials | s13 C14-05 women get a quarter of new AI jobs | s14 C14-01 people who teach AI their jobs say creativity keeps them employed | fun C16-02 Florida pizza shop vows never to use AI | teaser C15-02 IBM quantum feat, C03-01 ex-GitHub boss launches a rival, C11-11 AI-aimed gun turrets guard Kyiv, C07-02 shielding portfolios from AI stocks | BP money chases AI as borrowing costs hit a 24-year high || HEADLINES: C13-07 [From Westminster]; C06-03 [In business]; C12-05 [In security]; C08-07 [From Taiwan]; C11-04 [In robotics]; C01-01 [In new models]; C04-05 [In science]; fun C16-02 [In lighter news]; teaser C15-02 + C11-11.
- 2026-10-06 CARDS: s1 C13-01 Pentagon says it dropped Anthropic | s2 C06-01 OpenAI wants to raise $30 billion or more | s3 C06-02 DeepSeek close to raising at least $12 billion | s4 C06-03 Moonshot plans a Hong Kong share sale | s5 C12-02 Wikipedia's parent: OpenAI agents tried to edit pages | s6 C12-01 South Korea's president: bank hackers may have used AI | s7 C08-01 AMD to supply far more AI chips in 2027 | s8 C09-01 Google near a nuclear power deal | s9 C11-01 AI-aimed gun turrets shot down Russia's fastest drones | s10 C01-01 Reflection's Beam matches a top Chinese model | s11 C04-02 Google DeepMind AI invented two enzymes | s12 C05-01 former AI workers warn New York City's council | s13 C10-01 an app's AI prescribes acne medicine in Utah | s14 C10-02 Britain to check AI medical tools throughout their use | s15 C14-02 protesters disrupt a London tech dinner | fun C16-01 Jon Stewart and Meta's AI mascot | teaser C11-02 NATO drone and AI plan, C05-03 senator calls Anthropic boss's warnings alarmist, C04-05 AI steered an X-ray machine, C08-04 Qualcomm against Arm | BP tech shares at a record; banks and Gulf funds line up AI money || HEADLINES: C13-01 [We begin with an update]; C06-01 [In finance]; C06-02 [Also in finance]; C12-01 [In security]; C11-03 (not a card: LG and Nvidia AI brain for Hyundai's self-driving car) [In robotics]; C01-01 [In tech]; C04-02 [In the lab]; fun C16-04 (not the fun card: Alexa stuck saying la la la) [And finally, something lighter]; teaser C11-02 + C05-03.
- 2026-10-07 CARDS: s1 C13-22 UAE trains 80,000 civil servants to run government with AI | s2 C06-02 SpaceX wants to borrow $40 billion for Nvidia chips | s3 C05-02 Ray Dalio: AI bubble close to bursting | s4 C05-01 Jamie Dimon: Mythos made hacking ten times riskier | s5 C09-03 local opposition killed $260 billion of US data centre plans | s6 C09-04 record US power use from AI data centres | s7 C11-02 Waymo driverless in Detroit | s8 C11-16 Chinese robot hand threads a needle | s9 C02-01 Claude sidebar in Google Docs, Sheets and Slides | s10 C15-01 New York chip factory for light-based quantum parts | s11 C05-04 Hinton wants AI safety-checked like drugs | s12 C13-04 two US senators want AI firms liable when agents hack | s13 C10-01 Eli Lilly opens AI drug tools | s14 C14-02 71 percent of Americans expect fewer jobs | fun C16-13 Tirana's jailed mayor sends an AI double | teaser C01-01 Mistral model, C02-04 Gemini in Chrome on Android in India, C13-24 Nigeria's election body and AI, C09-09 San Francisco data centre pause | BP Dalio calls AI a bubble as chip buying runs on debt || HEADLINES: C13-22 [We begin with politics]; C05-02 [On the markets]; C05-01 [In banking]; C09-03 [In energy]; C11-16 [Now to robots]; C02-01 [In software]; C05-04 [Turning to safety]; fun C16-13 [And now a smile]; teaser C01-01 + C13-24.
- 2026-10-08 CARDS: s1 C13-01 senator wants government safety tests of the strongest AI | s2 C13-03 five-minute video pitch for Pentagon deals | s3 C07-01 Samsung's $80 billion quarterly profit | s4 C07-02 TSMC sales up 51 percent | s5 C12-03 hackers hijacked 3,400 servers running AI tools | s6 C09-01 drones struck a Yandex data centre | s7 C11-02 Nvidia wants more of Figure AI | s8 C11-17 driverless Uber taxis in Dubai | s9 C02-01 ChatGPT answers with charts and buttons | s10 C01-02 Claude Haiku at a quarter of the price | s11 C04-01 Google, Meta and US agencies teach AI how cells react | s12 C15-01 IBM and three quantum makers reach Pentagon final round | s13 C13-05 AI voices for political robocalls | s14 C10-05 England's health service lets AI rank skin cancers | s15 C14-02 ChatGPT for Teens often fails to alert parents | fun C16-10 OpenAI helper: "Oh, I love you too" | teaser C02-02 Copilot to handle PC files, C05-01 IMF chief warns on AI debt, C14-06 Kenyan refugees lose online work, C11-04 Tesla Optimus 1,000 a week | BP chip makers cash in while debt worry spreads || HEADLINES: C13-01 [We start in Washington]; C07-01 [In business]; C09-01 [From Russia]; C11-02 [In robotics]; C02-01 [For chatbot users]; C04-01 [In science]; C14-02 [On teen safety]; fun C16-10 [And on a lighter note]; teaser C02-02 + C14-06.
- 2026-10-09 CARDS: s1 C05-02 Trump: anyone saying artificial intelligence, not superintelligence, is the enemy | s2 C13-21 Musk accused Indian tycoons of blocking Starlink | s3 C06-04 OpenAI sales pace $20 billion below its earlier figure | s4 C07-04 WTO doubled its trade growth forecast on AI demand | s5 C03-01 Anthropic scans open-source code for free | s6 C12-02 OpenAI shut down Russian and Iranian fake-writer groups | s7 C09-03 Oracle trucks natural gas to data centres | s8 C11-23 humanoid robots directed traffic in Hangzhou | s9 C11-06 Walmart's warehouse robots break down | s10 C01-01 Gemini 4 Argon first for security experts | s11 C04-04 scientists: Anthropic overstated a gene-editing find | s12 C13-01 USA Today's publisher sued OpenAI | s13 C10-01 Google chatbot questioned patients before urgent visits | s14 C14-07 charity to record Gaza classrooms with AI | s15 C16-01 streamer's robot whacked him on the head (no separate fun card) | teaser C02-01 Gemini helper for firms, C11-24 Tokyo shop robot, C09-04 senators on data centre costs, C14-06 San Francisco rents | BP investors want results after OpenAI's lower sales figure || HEADLINES: C05-02 [First, super intelligence]; C13-21 [In India]; C07-04 [On trade]; C12-02 [In security]; C11-23 [Next, robotics]; C01-01 [In tech]; C14-07 [In education]; fun C16-01 [And now, something lighter]; teaser C02-01 + C14-06.
- 2026-10-10 CARDS: s1 C13-03 China: no blind money into AI and high tech | s2 C06-01 odds start-up TypeSafe valued at $7.5 billion | s3 C12-01 Claude sent police a made-up murder tip in a test | s4 C12-02 AI bosses rehearse for the day after an AI disaster | s5 C08-02 big buyers booked most of Samsung's memory chips | s6 C11-17 wheeled humanoid robot under $30,000 | s7 C11-18 Ukrainian ground robots rescued 45 soldiers | s8 C01-16 Musk backs Anthropic's ban on cruelty to AI | s9 C01-03 Alibaba's Qwen3.8 free to download | s10 C04-07 amateur with AI tools may have found a planet | s11 C08-01 Super Micro contractor admitted smuggling Nvidia chips | s12 C10-01 tech firms lobbied US health officials in a chat room | s13 C14-04 Nikon took back a prize over an AI-made video | s14 C14-05 publishers use AI for covers without telling authors | fun C16-01 government chatbot shared pasta recipes | teaser C02-01 Amazon asks Meta to keep its AI helper off its store, C01-01 Microsoft choice-only model, C10-02 GSK signs AI start-up Chai, C09-05 batteries cheaper than gas turbines | BP shares recovered from an OpenAI scare as China warned of blind investment || HEADLINES: C13-03 [From Beijing]; C06-01 [In finance]; C12-02 [Next, safety]; C11-17 [In robotics]; C01-16 [On chatbots]; C08-01 [In court]; C14-04 [In science]; fun C04-07 (story card s10, not the fun card) [On a lighter note]; teaser C02-01 + C09-05.
