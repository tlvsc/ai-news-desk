# Rules check, Part B (cards and Headlines), edition 2026-10-12 (MON 12 OCT 2026)

Written by the rules checker, Part B step 0c, 10:20 to 10:45 UTC (date -u). Updated from runs/2026-10-11/rules_check.md: what still holds is kept, every line was rechecked against today's files.
Read in full from disk: CLAUDE.md (300 lines; newest: rules 22 to 26 and the 12 Oct lines 127, 166, 180, 186, 280, 284 to 300), docs/V1_TASKS.md (771 lines: P1-1 to P1-35, L1, Port-1 to Port-12, 13 to 261, D1 to D51), the Part B SKILL.md (180 lines), all 11 briefs, assets/headlines_model_lines.md, the scripts pick_gate.py, card_candidates.py and card_candidates_lib.py, check_wording.py, check_headlines_rules.py, verify_headlines.py, fill_headlines.py, build_pack.py, review_list.py, make_wording_prompts.py, common_b.py, build_cards_copy.py, assets/pack_base.json, and W/rules: Cards_Master_Rules_Structure.txt, Headlines_Master_Rules_Structure.txt, Headlines_prompt_for_comfy_json.txt, Article_phrasing_instructions_AIND_V1.txt, Full_Report_V1_Rules_Structure.txt, Bulletin_V1_Rules_Structure.txt. The six Drive files are unchanged since 11 Oct (W/rules_diff_result.txt, 08:13: all six "same"; only STORAGE_STANDARD.txt changed, its label lines now say _Claude-V1).
Read for evidence only (nothing changed): W/products (report_pdf.json, bulletin_pdf.json), report_entries (188 files incl. CP-C12-10), facts, held.json, bulletin_keep.json, viral.json, bigger_picture_bulletin.json, out/AIND_Pool_2026-10-12.json, cards_work/pick_pack.json and selection_draft.json, runs/2026-10-11 (cards_work/selection.json, cards_copy.json, headlines_work/scripts_final.json, bigger_picture_card.json). pick_gate.py functions were run read-only in memory to simulate G17 (Python only wrote its git-ignored __pycache__ file); no script was run that writes.
W = /tmp/claude-0/-home-user-ai-news-desk/f3d477a5-1092-5355-b599-a13a62d03539/scratchpad/run_2026-10-12
State at 10:22 UTC: Part A delivered (six files in chat at 10:15, lesson 258). At 10:17 the main session ran step 0b (report_entries/CP-C12-10.json and facts/CP-C12-10.json), card_candidates.py (cards_work/selection_draft.json), pick_gate.py pack (pick_pack.json and .md: 24 Bulletin candidates, 82 reserve, decks of 7 of 7 days) and make_cover.py (products/cards_12-10-26/cards_12-10-26_I01_VL1.png). Paper input and the cover only, before this file (lesson 131 again; nothing chosen). No selection_fable.json, selection.json, update_allowed.json, wording, pack or JSON; no headlines_work folder.
The CLAUDE.md copy carried in this session's context is older than the disk file (it ends at rule 19, has no rules 8a, 8b, 20 to 26, and says CARD_FILTER target=15): every helper prompt must point at /home/user/ai-news-desk/CLAUDE.md on disk (lesson 186).
Every fix offered in section 2 is my wording, not Rafi's (CLAUDE.md rule 20). Nothing was applied.

## 1. One line per rule and lesson

### 1a. CLAUDE.md rules that touch Part B today
- Rule 0 TOP (Drive read only): Part B reads Drive only for the renderer zip and the cover base (setup) and writes nothing to Drive today (rule 26). Evidence: no Drive call after Part A; the cover was built at 10:17 from the local base.
- Rule 0 DAILY DELIVERY: replaced for now by rule 26 (newest ruling: Rafi uploads the final products and the pool files himself). Part B gives him the cards, the contact sheet and the JSON in chat; the text copy goes to runs/2026-10-12 by save_state.py. SKILL step 8.2 is stale (2b).
- Rule 0 WHO MADE IT: the files Rafi uploads carry _Claude-V1 (cards_12-10-26_I01_VL1_Claude-V1.png to the closing card, the contact sheet, the JSON): send them under the names delivery_manifest.py --part B prints, as lesson 247 did for Part A. To verify at step 8: the names of the files sent.
- Rule 1 (route the job): routes fixed (cloud: choice, wording, cards, JSON; Rafi's PC: ComfyUI, stitch, Drive upload by hand). No open route.
- Rules 2, 15, 8b item 5 and rule 24 HOW CLAUDE EXPLAINS: one or two short sentences, simple words, "like I am six years old". Evidence: the step 1 list message and the step 7 one-line ask.
- Rule 3: superseded files renamed _old, a new cards_runN per render, the fill refuses to overwrite, never rm (lesson 230). Evidence: ls of W at step 8.
- Rule 4: Rafi's edits at steps 1 and 7 applied and shown one at a time.
- Rule 5: numbers as evidence: card files counted against cards_copy.json (assemble_cards.py), JSON bytes and md5, active slots, seconds, longest clip, news part (verify_headlines.py). To verify at steps 5 and 6.
- Rule 6: every card and clip fact from report_entries/<id>.json and facts/<id>.json (Apate from CP-C12-10); the Fable checkers check every fact (check 3 of check_cards.md, check 4 of check_headlines.md). To verify at step 3: 0 open fact problems in cards_work/check_result.json and headlines_work/rules_result.json.
- Rule 7: Claude does not judge the look; the contact sheet goes to Rafi first.
- Rule 8: an instruction Rafi gives during Part B goes into CLAUDE.md the same day, in his words (rule 20).
- Rule 8a: 5 clashes in section 2, none chosen or applied; 2a lists the touches Rafi's own precedence lines settle, each with the line that settles it.
- Rule 8b item 1: no fix of section 2 runs before Rafi picks it.
- Rule 8b item 2: no brief may carry a rule's opposite: 2b lists stale brief lines; pick_stories.md lines 7 and 10 reach today's picker and must be fixed or overridden before it starts.
- Rule 8b item 3: before Rafi sees the deck: the 0c.4 PASS/FAIL table, G17 over 7 of 7 decks (48 to 50 lines a day in pick_pack.json), and the 3-day name and topic table (section 3c; G17 misses C05-02 against the 11 Oct card s4).
- Rule 8b item 4: counts and orders he gave: 14 story cards (clash 1: the Bulletin gives 13 within the limits), 7 clips, 2 robotics cards with one humanoid, 1 robotics clip, Politics clip 1; say how each was met.
- Rule 8b item 6: every named person with position and organisation: today Shyam Sankar (Palantir chief technology officer), Mohsen Rezaei (Fortune: former Revolutionary Guard commander, head of Iran's Supreme National Security Council), Bill Gates (Microsoft co-founder), Brad Smith (Microsoft president), Kristalina Georgieva (IMF managing director), Heo Jong-sik (Democratic Party lawmaker), He Xiaopeng (XPENG founder and chief executive), Matthew Quinn (Secret Service deputy director), Alexandr Wang (Meta chief AI officer), Dali Kaafar (Apate founder); Bigger Picture text: Tan Su Shan (DBS chief executive), Hock Tan (Broadcom chief executive), Andrew Bailey (Bank of England governor, FSB chair). Evidence: G15b novice_test, checker check 2.
- Rule 8b item 7: one check round and one fix round (rule 25, SKILL step 3); what stays open: clash 3.
- Rule 9: the skills only on branch claude/eager-archimedes-ajnex3; no PNG, MP4 or ComfyUI JSON in git (save_state.py copies text only).
- Rule 10: no brand mark on any screen line; fill PROMPT (fill_headlines.py line 18) says "No readable words, numbers or logos".
- Rule 14 COUNTS: the card target is a working target (clash 1). The Bulletin holds 24 stories (21 plus 3 Fun), under the 30 to 50 guideline: Part A's delivered product, not a Part B gate.
- Rule 14 BULLETIN SECTIONS NEVER EMPTY (0c.4 recheck): 11 of 11 sections hold stories; Politics (C13-16, C13-17) and Energy (C08-02, C09-08) exactly 2 from the report; Robotics 5 (bulletin_keep.json). PASS.
- Rule 14 Full Report 100 to 120: 106 (pool score 5 and up plus a second writer round at score 4, lesson 249). PASS.
- Rule 16 Fun Side: report 8, Bulletin 3. PASS.
- Rule 16 cards and clips: story cards by the CARD FILTER (target 14, clash 1), 7 into Headlines. Evidence: gate_result.json G2.
- Rule 16 news part about 90 s (now with rule 22's aims). Evidence: check_wording.py "news part" line, verify_headlines.py "news part". To verify at step 6.
- Rule 16 round up to the next half second: fill_headlines.py box_seconds and its node 13 assert (line 151). Evidence: the fill slot table.
- Rule 16 company limits (3 cards, 2 clips): G9, G10, check_headlines_rules.py C16 (counts the name in the spoken lines: a line on Brad Smith and a line calling Bill Gates "Microsoft co-founder" both count as Microsoft).
- Rule 16 READER LEVEL: cards level 6, Headlines level 5 with rule 22 and the 11 Oct level (rule 24); every writer re-reads 1, 1A, 1B and its product section before each item. Evidence: the re-read line and the phrasing-file override in prompt_cards.txt and prompt_headlines.txt.
- Rule 16 CLIP SECONDS (points to rule 22): aim 8 s, 10 acceptable, 12 the hard limit. Evidence: check_wording.py FAIL over 12 (line 112), check_headlines_rules.py B1, fill assert (line 95), verify_headlines.py (12).
- Rule 16 CREDIT: the card SOURCE line is the entry's source as written (build_cards_copy.py line 37); "X reports, citing Y" when the article credits another outlet; the Bigger Picture card says AIND and AI News Desk. Lines to read today: C14-01 "CNN, as relayed by ETHRWorld" (a relay named), C12-01 "Fox News" (Gates spoke on CNN), C13-17 "Fortune, citing IRNA" (lesson 255), C01-02 "Global Times, citing National Business Daily", C06-01 "The Wall Street Journal" (read in SiliconANGLE and CTech), C05-01 "Bloomberg" (read in The Japan Times), C12-02 "The Telegraph, as relayed by Reuters". To verify at step 7: every SOURCE line on the sheet.
- Rule 16 WRITE ONLY WHAT CAN PRINT: cards only from written entries. PASS by construction.
- Rule 16 REPLY STORIES: C13-16 answers Bloomberg's report of 18 Sep 2026 (entry notes) but the pool marks it follow_up false, so check_wording.py's reply test does not fire on it: the two checkers must check it; C05-02's entry reads it as a reaction to Trump's self-regulation line (judge). Evidence: check_result.json, rules_result.json.
- Rule 16 HEADLINES RULES RECHECK: check_headlines_rules.py (rules_check.json fails 0) and the Fable checker's rules_result.json on the CURRENT lines (common_b.rules_gate). No introduction of 11 Oct (section 3b); see clash 4. Nothing with a rules FAIL: clash 3.
- Rule 16 MODEL POLICY with STORY CHOICE and rule 25: picker Fable; writers Opus at max; checkers Fable at high; main session and setup on Sonnet; never Haiku. Evidence: the model of every Agent call; helper tokens per stage next to 4 and 5 Oct.
- Rule 16 STORY CHOICE: one Fable picker (briefs/pick_stories.md), pick_gate.py gate PASS or a named override (clash 1), Rafi approves the list before any wording. Evidence: gate_result.json, his message.
- Rule 16 BIGGER PICTURE MODEL and WEIGHT: card and clip from bigger_picture_bulletin.json (504 words): lenders and investors reprice AI (DBS, Broadcom, IMF, FSB letter, Korea's fall after a record quarter, Tencent bond); dated watch items (IMF outlook Tue 13 Oct; TSMC and the G20 Thu 15 Oct; Fed 27 to 28 Oct; Microsoft 28 Oct; SK hynix 27 Oct and Samsung 29 Oct not confirmed; US midterms Tue 3 Nov); not financial advice on the card and in the clip voice and screen (check_wording.py lines 118 to 121, verify_headlines.py lines 23 to 26). Who writes card and clip: clash 5.
- Rule 16 SCRIPTS STAY AS THEY ARE: no script change during the run except for a rule Rafi gives during the run, after his yes to the exact edit list (line 160). Evidence: git diff of scripts/ empty at the end.
- Rule 16 HEADLINES SHAPE: points to rule 22 and the model lines file. See rule 22.
- Rule 16 WHO WHAT WHY FIRST: who, what, why_for_people filled for every story and the fun clip (check_wording.py line 109 fails a missing one); failing lines go back to the same writer (rule 25); Rafi's words locked (rewrite_request.json "locked"); build_pack.py and review_list.py stop unless check_wording.py, check_headlines_rules.py and rules_result.json are newer than scripts_final.json.
- Rule 16 HEADLINES ORDER: Drive A3 for the six non-Politics clips; Politics clip 1 is settled (2a item 3).
- Rule 16 HEADLINES INTROS AND FLOW: each introduction names its own topic, in a natural order, never twice in the reel, never an unlinked label; among non-Politics clips prefer AI affecting people over war (robotics: C11-03 shelves over C11-06 drone hunter); the fun clip per rule 24; every clip generated except slots 1, 12 and 13.
- Rule 16 REAL TV SCREENS, PHOTOREALISTIC, FUN CLIP: each screen a photorealistic TV news scene of its story, no readable words, numbers, logos or real named faces; the Bigger Picture keeps its warning sign; fun clip facts only from its source (CP-C12-10). Evidence: fill PROMPT line 18; the Headlines checker's screen findings.
- Rule 16 NO OLD NEWS: cards and clips only from the report after step 9b (64 held). PASS by construction; the one exception is Apate (rule 23).
- Rule 16 CARD FILTER and the CARD_FILTER line (base_min 5, extra_min 7, target 14, 2 per category, market 3, company 3 cards and 2 clips): order from Drive Cards Master 2.4 (read_order: 11 categories); no score 10 (top is 8, C06-01); every category has an eligible Bulletin story at 5 or more; extras below 7 settled (2a item 1); a robotics card shows a machine doing something (C11-03, C11-06). See clash 1.
- Rule 16 CARDS FROM THE BULLETIN: 24 Bulletin stories, 21 non-fun, 17 eligible (read in full, NEW, not held), 14 after the robotics machine test, 13 within the category limits (clash 1). Evidence: G4.
- Rule 16 NO UPDATE CARDS: none named (no update_allowed.json); the Bulletin's follow-ups C07-02, C09-08 and C02-01 are not cards, clips or teaser items (G6); the 3-day name and topic table goes with the deck at step 7 (section 3c).
- Rule 16 NO REPEATS IN 7 DAYS: decks of 5 to 11 Oct all present. G17 simulated: flags C05-01 against the 8 Oct teaser (IMF chief on AI debt: a different speech, so disputed_repeats with proof) and the reserve stories C06-03 (6 Oct Moonshot) and C07-05 (IMF); misses C05-02 against the 11 Oct card s4 and clip (Microsoft's "emergency brake"). Evidence: gate_result.json G17 plus the section 3c table.
- Rule 16 THE REPO IS THE SOURCE OF TRUTH: a CLAUDE.md line beats a Drive line; differences belong in docs/DRIVE_DIFFS_FOR_CHATGPT.md (2d).
- Rule 16 PEOPLE WITH THEIR POSITION: as 8b item 6.
- Rule 16 HEADLINES START WITH POLITICS: the first Politics card in deck order is clip 1 (G11b); both Politics stories are about the Iran war (C13-16 school strike reply, C13-17 data centre threat).
- Rule 16 VIRAL RULE: Decart (46 outlets) is C06-01 at 8; no other cluster reaches 20 (viral.json: Gates cyber 17, Claude murder tip 16, Nadella brake 14 not in the pool). No re-run today.
- Rule 16 ONE TOPIC, ONE CARD: no gate test (lesson 161); today C12-01 (Fox) and C14-01 (ETHRWorld) are two parts of one Bill Gates interview on CNN, 11 Oct: one topic or a stated reason; every card pair checked before Rafi sees the deck.
- Rule 16 ROBOTICS: Bulletin 5 (3 to 5: PASS); cards 2 with one humanoid: C11-03 (Unitree humanoids restock Føtex shelves, human-guided, machine_action true) and C11-06 (Secret Service drone hunter, machine_action true); C11-02 (XPENG IRON timetable) shows no machine doing something (G13 would need a robotics_ruling); Headlines 1 robotics clip (C11-03; B2: say what the robot does).
- Rule 16 ROBOT WAR LIMIT: Bulletin at most 2 (C09-08 Yandex after drone strikes and C11-06 counter-drone, if both count), Full Report at most 3. PASS. No limit on cards.
- Rule 16 BEFORE EVERY STAGE: this file is the read of step 0c.
- Rule 16 HEADLINES GENERATION: 8 steps, AIND_anchor_voice_sample_4s.wav, the unhurried tone. Evidence: fill CONFIG line; verify_headlines.py "steps 8" and "tone in N of N".
- Rule 16 APPROVED OPENING AND ENDING: assets/pack_base.json slots 1 and 13 "bypass" (checked); check_headlines_rules.py A2.
- Rule 16 QA GAPS: the built checks run, in rule 25's shape.
- Rule 17 BIGGER PICTURE CORNER: card head the market summation, body what happened and what to watch (4 lines, notice stays); clip 10 s (rule 22: 10 acceptable); never a vague restatement: the 11 Oct card and clip already watched TSMC on 15 Oct, and AI debt led the card on 4, 5, 7, 8 and 11 Oct.
- Rule 18 FRESH CHAT: Part B continues in Part A's chat (rule 9; 2a item 9); a compacted chat continues only with Rafi's yes.
- Rule 20: one question at a time; when he asks for the list, the list itself; rules only in his words; his exact complaint first; ORDER NEVER CHANGES (G7).
- Rule 21: lessons of this run into docs/V1_TASKS.md (step 8.4); a handoff is not a source; never touch the Drive EXPERIMENTS file.
- Rule 22 HEADLINES STRUCTURE: one sentence after the introduction, who did what and why (a company reason or a careful guess is a why; the end part only if it adds weight); aim 8 s, 10 acceptable, 12 the hard limit; the model lines file read by writer and checker (wording_headlines.md line 12, check_headlines.md line 3). Scripts test only the length; the one-sentence shape rests on the checker (check_wording.py counts no clip sentences): to verify at step 7 by counting sentences after the introduction in scripts_final.json.
- Rule 23 FUN CLIP: Apate is today's fun clip: CP-C12-10 copied in at 10:17 (WIRED, verified_text true, freshness NEW, score 5); headlines_fun = CP-C12-10, the Fun card stays a Bulletin fun story (SKILL step 0b); G1 and G5 pass it, G4b exempts CP- ids. It is not in today's pool, Bulletin or Full Report (grep: 0 hits): clash 2.
- Rule 24 CARDS IN GROUPS OF 10: step 8.1: 10 files a message in deck order, the contact sheet with the last group, the JSON alone.
- Rule 24 HEADLINES ITEMS MUST BE IN THE REPORTS: G4b (every clip id in the Bulletin and the report); story clips come from Bulletin cards, so a reserve-exception card can never be a clip.
- Rule 24 FUN STORIES: funny, or fun to hear, see or experience, or mildly cynical and funny to think about, never sad; pick_stories.md still says "truly funny" (2b, blocks the picker).
- Rule 24 HEADLINES LEVEL IS A CONSTANT: the 11 Oct lines (model lines file "The level": about 22 words, one sentence, one actor, one verb, one why).
- Rule 24 NO TIME PRESSURE ON THE TEST: the length wording of rule 22 and the model lines file stays as it is.
- Rule 24 "too complicated to explain in one sentence": such a story is not a clip (C13-16 needs the reply and Bloomberg's earlier report: test it before making it clip 1).
- Rule 24 "not funny but definitely fun": fun counts (FUN STORIES).
- Rule 25 ONE WRITER AND ONE CHECKER PER PRODUCT: writers Agent model "opus", effort "max"; checkers model "fable", effort "high"; each writer runs check_wording.py (and check_headlines_rules.py) before handing back; each checker reads once; the same writer fixes once; then Rafi sees what is left. make_wording_prompts.py still writes the old stranger, rules and rewrite prompts: not launched. To verify at step 2: whether the Agent tool takes an effort value (lesson 76 says it did not); if not, say so to Rafi in one line.
- Rule 26 VIDEO WORK AND FOOTAGE: footage and the video lessons 238 to 244 apply on the PC, not to the JSON; DRIVE UPLOAD by Rafi: no Drive agent at step 8; send only the final products (cards, contact sheet, JSON).

### 1b. Drive rule and structure files (only lines that touch Part B; "settled" = a CLAUDE.md line or a newer ruling wins)
- Cards Master order block and 2.4: deck order Politics, Market, Security, Energy, Robotics, Models, Research, Ethics and law, Health, Society, Fun. Evidence: G7. The fixed slots are replaced by the CARD FILTER (settled).
- Cards Master filename rule: local cards_12-10-26_INN_VL1.png; _Claude-V1 on the names Rafi uploads (settled, rule 0 WHO MADE IT).
- Cards Master 1.1: one 1080x1920 PNG set plus one combined image (the contact sheet). Evidence: assemble_cards.py sizes line.
- Cards Master 1.3 and 3.5 DESK VIEW: the Bigger Picture card says AIND (settled, CLAUDE.md CREDIT).
- Cards Master 1.4 and 2.5: the "More in the full report" card holds report headlines with no story card; the reel teaser draws only from it. Evidence: G12, check_headlines_rules.py A5.
- Cards Master 2.1 to 2.3: cover first; criticals spend their slot (no score 10 today).
- Cards Master 2.6: aim 15 (settled: 14); robotics and fun normally required.
- Cards Master 2.7: at most 3 money cards. Evidence: G8 (only C06-01 is an eligible Bulletin market story).
- Cards Master 2.8: full report only (settled: from the Bulletin).
- Cards Master 2.9: robotics = a machine doing something (settled: humanoid funding also counts). Evidence: G13.
- Cards Master 2.11 and 2.12: no sales language, no link on cards; the closing text of 12 Sep (build_cards_copy.py CLOSING).
- Cards Master 2.14: reel order follows deck order. Evidence: G11, check A3.
- Cards Master 3.1 to 3.4: phrasing file governs; lead with the deed, not the money; unfamiliar companies titled (today Decart, XPENG, Hive Robots and Unitree, Apate, Epoch AI, OpenRouter, Coatue, Salling Group and Føtex, Indeed Hiring Lab).
- Cards Master 3.6 and 3.7: approved text never cut for layout; Rafi approves at step 7.
- Cards Master 4 to 6: the renderer package (md5 598989503fa221cebe87c04bac903854) owns colours, fonts and the Instagram window; cover = approved cover with the new date (made at 10:17).
- Cards Master 7.1, 7.4, 7.7, 7.8: Drive account and saving: not live today (rule 26, settled).
- Cards Master 7.15 and 7.16: contact sheet first at step 7; every card its own PNG, never a zip; groups of 10 (rule 24, settled).
- Headlines Master order block, A3, A7: stories in deck order, then fun, teaser, Bigger Picture, ending (build_pack.py).
- Headlines Master A1: twelve-slot template (settled: 13 slots).
- Headlines Master A2 and 15 Sep 5: stored intro bypassed; ending wording = pack_base slot 13 text; the option 4 clips of 3 Oct are used (settled).
- Headlines Master A3: seven card stories in deck order, normally robotics plus law, research or society (today law C05-02, research C04-01, society C05-01, C14-01, C14-02 are eligible).
- Headlines Master A4: slot 9 is the deck's fun item (settled: rule 23, Apate).
- Headlines Master A5, A6, A8: teaser only from the teaser card; Bigger Picture in slot 11 opening "And for the bigger picture"; about 90 s of content.
- Headlines Master B1 and B1a: aim 8 s, 12 s maximum (same as rule 22); two decimals, no rounding (settled: round up, rule 16).
- Headlines Master B2: Cards Section 3 words; the robotics clip says what the robot does (C11-03: picks up products and places them on shelves).
- Headlines Master B2a: every story and fun clip opens with an introduction; teaser "Also in the full report." (full stop); Bigger Picture "And for the bigger picture". Evidence: check B2a.
- Headlines Master B3: numbers as words, no digits. Evidence: check B3 and check_wording.py.
- Headlines Master B2 (prompt) and the prompt file: text-free screen, "nothing else changes" (settled: REAL TV SCREENS and the tone line).
- Headlines Master C: references 1 hands-on-table and 2 fists (fill asserts the 29 Sep pair); every visible field overwritten; titles start "MON 12 OCT 2026"; slot table and stale word scan; mirrors written; JSON to Rafi as a file, never zipped; six steps (settled: 8).
- Headlines Master G1.1 and 15 Sep 1: cues only where spoken (N-vidia if Nvidia is spoken, an-thropic if Anthropic is: C14-02 names Claude Code's maker); 15 Sep 2: "Google DeepMind".
- Headlines Master G1.2: a two to three word tag for a company under 100 billion dollars (Decart, XPENG, Apate, Epoch AI, OpenRouter, Hive Robots; Palantir if unsure).
- Headlines Master G1.3: one idea per sentence (settled: rule 22). G1.4: hedges kept, outlet never spoken (check G1.4).
- Headlines Master G2: introductions rotate (clash 4).
- Headlines Master G3: the scene sits inside the pane at the logo's place and size (fill PROMPT keeps it).
- Headlines Master G7.3: teaser credit "DAILY GLOBAL AI INTELLIGENCE REPORT" (settled: build_pack.py line 41 writes AI News Desk since 12 Oct, lesson 241). G8.1: JSON plus script pack when Rafi asks for "the prompt".
- Headlines Master 15 Sep 3: no readable screen text (settled for the Bigger Picture warning words).
- Phrasing EVERY WRITER, EVERY ITEM: in wording_common.md, wording_headlines.md and both check briefs.
- Phrasing 1.1 to 1.8: banned words (check_wording.py BANNED), headline a full sentence, card body two sentences (check_wording.py line 95), numbers translated, no drama, first hearing test, never lift a sentence (make_cards.py prints LIFTED FROM REPORT; must be 0).
- Phrasing 1A: meaning check of every card and line against its entry (the two Fable checkers); a line with a gap is not shown.
- Phrasing 1B: who, what, why in every card and clip.
- Phrasing 2A: Cards level 6; Headlines level 5; its Headlines shape sentences (35 to 40 syllables, never over 10; a second sentence; why for people; company fact not a why) are overridden by rule 22 (settled; the briefs name the four sentences).
- Phrasing 3.1: cover = yesterday's cover, only the date changes (make_cover.py).
- Phrasing 3.2: one or two desk analysis cards (settled: one Bigger Picture card).
- Phrasing 3.3 and 3.5: teaser 3 to 5 and web gap filling (settled: report stories only, the gate takes exactly 4).
- Phrasing 3.4: at least three non-business cards and one robotics card. Evidence: count on the sheet.
- Phrasing 4.2 (open on Drive): reel teaser two items (wording_headlines.md line 9), card teaser 4.
- Full Report 5.5 markets cap: does not bind the Bigger Picture corner (rule 17).
- Full Report and Bulletin 5.3 and 11.4 (the headline-only note): settled for customers by Rafi's 8 Oct ruling (lesson 118, newest); the delivered Bulletin carries the note on 1 story (C07-01) and the report on 16: Part A's products, one line to Rafi, not a Part B gate.
- Full Report and Bulletin 6.1 and 6.2 (publisher named, direct link): 0 Google News links in 106 report and 24 Bulletin stories (counted). PASS.
- STORAGE: its label lines now say _Claude-V1 (11 Oct 18:30), the same as rule 0; Part B saves nothing to Drive today (rule 26).

### 1c. Part B skill steps (process rules of this run)
- Step 0 setup: renderer and cover base in place (cover rendered 10:17). Step 0.1 rules_diff: Part A's W/rules_diff_result.txt (08:13) serves; the Drive rules are unchanged.
- Step 0b: done at 10:17 (CP-C12-10 entry and facts, item_id set inside both).
- Step 0c: this file; the 0c.4 PASS/FAIL table per section before step 7.
- Step 1: Fable picker (its prompt filled by hand into cards_work/prompt_picker.txt, lesson 234c), pick_gate.py gate PASS or a named override (clash 1), Rafi approves the list before wording; the LEFT OUT list goes with it.
- Step 2: make_wording_prompts.py (with --prev-pack and --prev-cards of 11 Oct, see 2b), two Opus writers in one message, each runs its scripts before handing back.
- Step 3: two Fable checkers, one fix by the same writers, one confirm of the changed items; what stays open goes to Rafi marked (clash 3).
- Step 4: merged into step 3 (12 Oct).
- Step 5: cover, cards copy, render into a new cards_runN, assemble (stops on a refused card).
- Step 6: build_pack.py (gate), fill_headlines.py (refuses to overwrite), verify_headlines.py.
- Step 7: review_list.py (gate), save_state.py, sheet and list to Rafi, STOP.
- Step 8: after approval: groups of 10 in chat, the JSON alone, the voice sample line; no Drive agent (rule 26); save_state.py; short report; lessons into docs/V1_TASKS.md.

### 1d. Lessons that touch Part B today
- P1-3 Fun Side 5 to 10, top 3 in the Bulletin: 8 and 3. PASS.
- P1-4 cutoffs stated: report 106 (pool score 5 and up plus the score-4 round), Bulletin 24 (7 and up plus floors POL 6, ENE 6, ROB 5, HEA 6, SOC 6 and bulletin_keep.json; purpose line in words). Stated; 24 is under the 30 to 50 guideline (Part A).
- P1-5 everything final to Drive, else to Rafi: rule 26 (Rafi uploads) for now.
- P1-6 story cards 14 to 15, company 2 clips and 3 cards, money cards 3, a headline-only story never a card: G2, G9, G10, G8, G5 (C07-01 is headline only; count: clash 1).
- P1-7 news part about 90 s, round up: check_wording.py total, fill table (to verify at step 6).
- P1-8 hologram border: the fill PROMPT keeps the blue border line; the opening is stored.
- P1-9 only the spoken words when he asks for the stories in the JSON: review_list.py.
- P1-10 one file at a time: replaced by groups of 10 per message (rule 24); never a zip stands.
- P1-11 one home per rule: section 2 lists the double homes.
- P1-16 check the approved opening first: option 4 stored, slot 1 bypass.
- P1-17 never build before Rafi's yes: no wording before the list approval, nothing sent before the step 7 approval.
- P1-19 stop at a compaction: rule 18.
- P1-20 match his numbered answers against the original list: at steps 1 and 7 and on the clash answers.
- P1-21 never drop a category silently: every category has an eligible Bulletin story today; a skip needs left_out_notes.
- P1-22 no old JSON in a package; no unapproved screen wording: fill refuses to overwrite; screens go to Rafi in the review list.
- P1-27 uploads verified by size: no Claude upload today (rule 26).
- P1-29 meaning check before any JSON leaves: gate before step 7; no JSON before approval.
- P1-31 compute weekdays: 12 Oct Monday; 13 Oct Tuesday, 14 Oct Wednesday, 15 Oct Thursday, 27 Oct Tuesday, 28 Oct Wednesday, 29 Oct Thursday, 3 Nov Tuesday (computed).
- P1-32 read the governing file before quoting it: done in this file.
- P1-33 save cloud-only files: save_state.py before the step 7 wait and after delivery.
- P1-34 approved opening: the option 4 clips of 3 Oct (pack_base both bypass).
- P1-35 company limits: G9, G10, C16.
- L1 plain English gate: script check plus the checker's stranger test; card sentences at most 15 words (wording_cards.md line 9; not scripted, 2b); headline = the deed first.
- Port-3 company limits: CARD_FILTER line, G9, G10.
- Port-4 13-slot template, Bigger Picture clip 11, stored ending slot 13: build_pack.py.
- Port-5 hologram border kept; REAL TV SCREENS replaced the text-free symbol.
- Port-6 round up to the half second: fill_headlines.py.
- Port-7 the Bigger Picture at three lengths: clash 5.
- Port-8 deed first, 15-word card sentences: wording_common.md rule 1, wording_cards.md line 9.
- Port-9 repeat check over earlier decks: 7 days (G17) plus the 3-day table.
- Port-10 rule files named by their Drive names: yes.
- Port-11 8 steps, 4 s voice sample, unhurried tone: fill CONFIG line, verify_headlines.py.
- Port-12 new opening and ending only on request: none asked.
- 18 the voice sample lives on Rafi's PC: one line at step 8.1 (the JSON names AIND_anchor_voice_sample_4s.wav).
- 19 and 55 stranger failure types (background words, unintroduced names, jargon, idioms, a watch item without why, two facts as one): check 1 of both check briefs.
- 20 find first, write second.
- 22 card copy model: wording_common.md lines 4 to 6 (Rafi's model headline); the writer is Opus now (rule 25).
- 23 repeats over earlier decks: section 3c table.
- 24 and 46 credit the first reporter, "X reports, citing Y": check 3 of check_cards.md, check 4 of check_headlines.md; C14-01's "as relayed by" SOURCE line to fix or flag (2b).
- 25 card sentences over 15 words: not scripted (2b); count at step 7.
- 29 follow-ups never a card; follow-ups in the teaser fail G6: today C07-02, C09-08, C02-01.
- 30 Drive rules change between runs: rules_diff_result.txt (six same, STORAGE changed).
- 31 reader levels in the phrasing file only (cards 6, Headlines 5).
- 34 blocked sources: card credit to the first reporter, not the relay (C06-01 WSJ, C05-01 Bloomberg, C14-01 CNN or "ETHRWorld, citing CNN").
- 35 start the wording early: step 2 at once after the list approval.
- 36 render check: assemble_cards.py counts card files; short labels.
- 37 syllable budget, not words: wording_headlines.md line 15 (35, 44, 52 syllables).
- 38, 81, 110 Bigger Picture card and clip give a reason to watch each item and say nothing stronger than the Bigger Picture texts: the cards checker reads them against bigger_picture_bulletin.json.
- 41 never ask what the record answers.
- 42 Part B steps followed in order.
- 43 Bigger Picture card head at most 85 characters, one sentence, at most 15 words.
- 44 a rule a script can enforce is never a question: only wording choices and true clashes go to Rafi.
- 45 runs/<date> copy, no Routine yet: save_state.py; no Routine.
- 47 Bigger Picture card label AIND: build_cards_copy.py line 42.
- 49 compaction and fresh chat: rule 18.
- 50 a reply names the earlier story: C13-16 (Bloomberg, 18 Sep); the script test misses it (follow_up false).
- 56 Market labels about 10 characters: the Market category name is long (build_cards_copy.py warns over 46 characters).
- 59 the one lessons list: step 8.4.
- 60 intros rotate, company tags: check G2 and the checker's G1.2 (clash 4).
- 61 hard gate on the current lines: common_b.rules_gate in build_pack.py and review_list.py.
- 62 token cost: report helper tokens per stage.
- 63 stored opening and ending: pack_base both bypass.
- 64 voice file .wav, teaser full stop, Kawa saki cue: fill AUDIO, check B2a, cues.
- 66 old news in cards: cards only after step 9b plus the 7-day check.
- 67 "no company twice in a row" (Rafi to confirm; not in CLAUDE.md): note only (Microsoft's Brad Smith and Bill Gates, Microsoft's co-founder, sit in different categories).
- 68 and 80 one event in several entries: C12-01 and C14-01 (one Gates interview).
- 71 parallel sessions: fetch before every push.
- 72, 73, 235 Headlines shape: rule 22 replaced the 5 Oct checks (word cap, comma limit, company-only why removed); the side-clause test stays (check_wording.py line 70).
- 74 one truth for writing rules: the phrasing file, with rule 22's override named in the briefs.
- 75 simple, not childish: check 1 and 2 of check_headlines.md.
- 76 the Agent tool sets a model, not an effort: to verify at step 2 (rule 25).
- 77 and 101 long jobs through run_in_background, never a shell "&".
- 83, 98, 145, 163, 216, 246 stale clone and a moving branch: fetch and read new commits before each push (no Drive step today).
- 85 retyping uploads wastes tokens: no Drive agent (rule 26).
- 89 never Haiku; base_min 5 below a report cutoff: the report also holds score-4 stories, cards need 5 (G18 eligibility).
- 90 no shorthand to Rafi; full category names.
- 91 a count he gives wins over a cutoff: clash 1 (here the limits are not cutoffs).
- 92, 181, 198, 200, 209 when a rule changes, grep for its old wording: section 2b.
- 93 updates excluded; compare with the last 3 decks by name and topic: G6, the 3c table.
- 94 novice test at choice time: G15b.
- 95 a question is not a decision: 8b item 1.
- 96 one check round, one fix round; checkers fail only rule breaks: both check briefs say "never taste".
- 97 Politics clip 1 when the deck has a Politics card: G11b.
- 100 helper prompts must not create sessions.
- 107 and 221 which score counts: the pool score (Rafi's ruling); pick_gate.py reads the writer's (2b).
- 108 the automatic repeat match is a list to judge: G17 hits judged in 3c (C05-01).
- 111 the markets quarter cap does not bind the Bigger Picture corner: rule 17.
- 114 change only what was asked; 115 show first, then act; 116 count the rounds per product; 117 check a figure before passing it on.
- 118, 119, 179, 190 customer text: 0c.4 recheck only (the note on 1 Bulletin and 16 report stories); no fluency rewrite.
- 121 compare old and new facts of every fixed item: the checker's confirm round against the writer's first file.
- 122 the contact sheet by display render, files by attach.
- 123 Part B in a new chat: 2a item 9.
- 124 the restart copy is text only; 125 commit and push after every change.
- 126, 173, 208, 257 commits carry no model name, only the Claude-Session line.
- 127 estimate an agent's cost before running it; 128 answer first, act after he asks.
- 129 scripts unchanged during the run (rule 16 line 160 exception only with his yes).
- 131 step 0c before any choosing script: broken again today (selection_draft.json and pick_pack.json at 10:17, before this file); both are paper input, nothing is chosen.
- 134 and 135 robotics counts (Bulletin 3 to 5, cards 2 with one humanoid, Headlines 1, one extra allowed): Bulletin 5; cards C11-03 and C11-06; clip C11-03.
- 136 one Bulletin file: products/bulletin_pdf.json (24 stories = the delivered Bulletin after bulletin_keep.py). PASS.
- 137 and 158 the freshness flag does not know earlier decks: C05-02 says NEW but sits close to the 11 Oct card s4; C05-01 says NEW, the 8 Oct teaser had the same IMF chief.
- 138 a picker note is not a source: writers use entries and facts only.
- 139 the robotics clip says what the machine does: C11-03's entry does.
- 140 and 199 realistic screens: fill PROMPT updated (lesson 209); one stale brief line (2b).
- 141 screens static and wordless.
- 142 list every clash once: settled by rule 20 (2a item 10).
- 144 and 258 helper tokens per stage: report Part B's.
- 147 held stories are never cited: G1, G16.
- 148 and 256 the Bigger Picture author (Fable max) and the second reader (Opus) ran in Part A; 7 unconfirmed dates stay marked "not confirmed" in card and clip.
- 150 Bulletin cover in words: the purpose line names no codes. PASS.
- 154 no empty Bulletin section: PASS.
- 156 lock the report list: Part B never rebuilds the products.
- 161 two cards on one topic: the Gates pair; manual check.
- 162 Rafi's list changes meet the gate: gate_overrides.json names each overridden line and his words (clash 1).
- 171 and 174 viral stories by reach: Decart C06-01 at 8 (46 outlets).
- 175 rule text only in his words: section 2 fixes are marked mine.
- 177 and 178 the approved order for every product: G7 for the deck.
- 180 the six clashes of 10 Oct: four settled (2a items 1 to 5), one not live (2c), one carried (clash 3).
- 182 a viral floor only after checking earlier editions: no floor applied today.
- 183 link a follow-up by url and title, not a per-day id: when a card names an earlier story.
- 186 a CLAUDE.md copy loaded at session start goes stale: this session's context copy is stale (header); helpers read the disk file.
- 188 thin fun search: Bulletin fun stories score 3 (C16-01, C16-04, C16-06); rule 24 widens the fun test.
- 191 and 192 search before saying a robot story is missing: the humanoid story exists (C11-03).
- 193 robot war counted: Bulletin at most 2, report at most 3. PASS.
- 194 never ask what a rule decides; send the list itself.
- 195 may a follow-up of a printed story return in the Bulletin: still open; today's Bulletin carries C07-02 (continues the 11 Oct card s3 on Korea's market), C09-08 and C02-01; cards settled by G6.
- 196 the card list follows Rafi's order over the picker.
- 197 inside a full category compare appeal to a stranger, not only the score: Society has 3 eligible stories for 2 slots (C05-01, C14-01, C14-02).
- 201 the check chain: one round (rule 25).
- 202 label at most 14 characters, no money figure: pick_stories.md line 25 (2b on the 15 lines).
- 203 review_list.py intro photorealistic. PASS.
- 204 the Drive agent must try binaries: not live (rule 26).
- 206 and 237 the between-run fixes present: step 0b used, phrasing override in all writer and checker briefs, not-financial-advice checks (check_wording.py, verify_headlines.py), G4b, groups of 10 (step 8.1); "funny at once" gone from CLAUDE.md line 180 but its twin is still in pick_stories.md lines 7 and 10 (2b).
- 207 open for Rafi from 10 Oct: item 2 (follow-ups in the Bulletin) open; item 3 (customer text in CLAUDE.md) open; item 5 partly fixed (2b); item 6 settled by rule 24; item 7 (Bigger Picture Bulletin 504 words against about 350) open; item 8 not live (rule 26); item 9 open.
- 210, 211 to 215, 231 the second run (ChatGPT V1) in the same Drive date folder and the labels: the names Rafi uploads carry _Claude-V1.
- 223, 250, 251 Bulletin sections without a 7: Politics and Energy exactly 2, Robotics 5 via bulletin_keep.json. PASS (0c.4).
- 226 estimates from timed steps; 227 counts from the file list; 229 clock times from date -u; 230 never rm.
- 228 and 257 save_state.py: old session link in its commit message, PARTS gaps: fix the message by hand; rules_check.md is in PARTS.
- 233 "files" means the final products: step 8 sends the PNGs, the contact sheet and the JSON only.
- 234 Part B setup faults: (a) make_cover.py --pkg is the parent folder; (b) aind_cards.py runs without -I; (c) the picker prompt is filled by hand; (d) the score alignment (2b); (e) touches that Rafi's precedence lines settle are decided and named, not asked.
- 236 fun clip candidates shown as finished lines, at most three: today the clip is named (Apate); the fun card is the picker's.
- 238 no lessons, rules or script copies outside the repo; downloads need Rafi's OK: none in Part B.
- 241 _Claude-V1 names; build_pack.py writes each slot's source (fun: WIRED from CP-C12-10); teaser and Bigger Picture credited AI News Desk.
- 244 the 11 Oct Headlines are the reference look: the level constant (rule 24).
- 245 social text (hook and hashtags): only when he asks (D13).
- 247 rule 26 against the skill: Part B step 8.2 still stale (2b).
- 255 "Fortune, citing IRNA": C13-17's SOURCE line.
- 259 France 24: no France 24 source in today's report or Bulletin (checked).
- D1 do only the step he names; a one-sentence report, then wait.
- D2 Headlines in everyday words; cut filler.
- D3 spoken names "N-vidia", "an-thropic", "Kawa saki" only where spoken: check 15Sep1.
- D4 no colon after "Also in the full report": check B2a.
- D5 8 steps, the 4 s wav, fixed seed: fill asserts.
- D7, D36, D47 teaser and Bigger Picture credited AI News Desk: build_pack.py (fixed 12 Oct).
- D8 and D23 openings and endings are options; option 4 is used (bypass).
- D12 one short sentence; D13 only what he asks; D14 if it cannot be done perfectly, say so and stop; D15 one manual step per message; D18 look in the files before asking; D19 when a script blocks, follow it, never override it; D20 never delete, ask before any outward action.
- D25 Headlines only from that day's cards: replaced in part by rule 24 ("not necessarily in the cards") and rule 23 (Apate); story clips still come from the cards (G11).
- D27 the seed never changes (1060749754396562); D28 a spelling fix changes only the spelling.

### 1e. Rules and lessons that do not apply to Part B today (grouped by reason)
- Part A only (scan, pool, writers, editors, report and Bulletin build): CLAUDE.md 16 scan window, SOURCES, PER CATEGORY, 3 OCT 2026 RUN, BIG OUTLETS, FAMOUS PEOPLE RULE (a pool rule), POOL PDF EVERY DAY; P1-1, P1-2, P1-12, P1-13, P1-14, P1-15, P1-25, P1-26, P1-28, P1-30; Port-1, Port-2; 26, 27, 28, 32, 33, 39, 48, 54 (weekend; today is Monday), 57, 69, 78, 79, 86, 88, 102 to 106, 109, 112, 113, 130, 146, 151 to 153, 155, 157, 159, 160, 164 to 167, 169, 176, 185, 187, 217 to 220, 222, 224, 225, 248, 249, 252 to 254, 260, 261.
- Rafi's PC (ComfyUI, stitch, audio, footage): CLAUDE.md 11, 12, 13; rule 26 footage and video-lesson lines; 13 (speaking speed test), 14, 15, 16, 17, 58, 143; D6, D9, D16, D17, D21, D22, D24, D26, D29 to D35, D37 to D46, D48; 239, 240, 242, 243.
- Records, superseded or not asked: CLAUDE.md 16 HAIKU TODAY ONLY (8 Oct), TEST of 6 Oct (replaced by REAL TV SCREENS), OPENING AND ENDING OPTIONS (not asked), rule 19 (Part B is started by Part A); P1-18, P1-23, P1-24; 21, 40, 51, 52, 65, 70, 84, 87, 99, 120, 132, 133, 149, 153, 168, 170, 172, 184, 189, 205, 232 (superseded by rule 26), D10, D11, D42, D49, D50, D51; the empty Drive folder of lesson 216 (Rafi's to remove).

## 2. CLASHES (two rules that demand opposite things today; nothing chosen, nothing applied): 5

1. The count of 14 against the Bulletin source and the limits (new today; blocks the gate).
   A: CLAUDE.md line 199-200 (CARDS FROM THE BULLETIN: "the target is 14 story cards"), line 206-207 ("Aim: 14 story cards"), line 54 (8b item 4), pick_gate.py line 109 (G2: 14 or 15), briefs/pick_stories.md line 23 ("exactly 14").
   B: CLAUDE.md line 199 ("story cards are chosen only from the stories of the Bulletin"), line 221 (max_per_category=2), line 197 ("a robotics card shows a machine doing something"), lines 201-203 (NO UPDATE CARDS); pick_gate.py G4 and G4b exception (lines 114-120), G8 (126), G13 (139), G6 (122); rule 14 lines 87-89 (counts are guidelines: adjust to the day's pool, state the number, never ask about a count).
   Clash: the Bulletin holds 13 card-eligible stories within the limits (Politics 2, Market 1, Security 1, Energy 1, Robotics 2, Models 1, Research 1, Ethics and law 1, Health 1, Society 2 of 3), so a 14th card breaks a limit and a 13-card deck fails G2; 8b item 4 settles counts only against cutoffs and script defaults, and these are rules.
   Fix A (count wins): add to CARDS FROM THE BULLETIN: "When the Bulletin holds fewer than 14 eligible stories within the limits, the 14th is the best eligible Bulletin story over its category limit (market up to market_max), marked exception with the reason." Fix B (limits win): add: "When the Bulletin cannot give 14 within the limits, the deck is smaller and the number is stated; pick_gate.py G2 accepts it (script change between runs; today gate_overrides.json names G2)." (wording mine, not yours)
   Recommendation: Fix A today (14 cards; the 14th is today's third eligible Society story, G8 named in gate_overrides.json), put to Rafi inside the one-line list approval, not as a separate count question (rule 14).

2. The Apate fun clip against "Headlines items must be in the reports" (new today).
   A: CLAUDE.md lines 284-285 (rule 23, Rafi 11 Oct: Apate is the fun clip of 12 Oct, "keep it for tomorrow"); SKILL.md step 0b (lines 51-54); pick_gate.py lines 111-113 (G4b exempts CP- ids).
   B: CLAUDE.md line 288 (rule 24, Rafi 12 Oct, newer: "items in headlines must appear in the pool, and bulletin and report"); the sentence after it ("the one exception is a fun clip Rafi names himself") is Claude's wording (rule 24 header; rule 20: rules only in his words).
   Clash: CP-C12-10 is in the 11 Oct report only and in none of today's pool, Bulletin or Full Report (grep: 0 hits); by "the newest ruling wins" rule 24 refuses it, by rule 23 it is today's clip.
   Fix A: mark the exception in rule 24 as Rafi's: "A fun clip Rafi names himself (rule 23) need not be in that day's pool, Bulletin or report (Rafi, 12 Oct 2026)." Fix B: add the Apate story to today's pool, Full Report and Bulletin Fun Side (add_regional.py pattern, PDFs rebuilt) before the picker. (wording mine, not yours)
   Recommendation: Fix A (keep Apate: rule 23 names it for this date and G4b is already built for it); one line to Rafi with the list.

3. Nothing with a FAIL against one check round (carried from 10 and 11 Oct, narrowed by rule 25).
   A: CLAUDE.md line 145-146 (HEADLINES RULES RECHECK: "Nothing goes to him with a rules FAIL"); SKILL.md 0c.4 lines 64-67 ("nothing is shown or delivered with an open FAIL"), 8.5 line 162.
   B: CLAUDE.md line 57 (8b item 7: one check round and one rewrite round, then show Rafi what is left); SKILL.md step 3 lines 103-106 (12 Oct: what is still open goes to Rafi in step 7, marked); rule 25 line 296 ("then Rafi sees everything", Claude's wording).
   Clash: a checker flag still open after the one fix round either blocks step 7 or goes to Rafi marked.
   Fix A: add to 8b item 7: "A script FAIL (check_wording.py, check_headlines_rules.py, the gate) never reaches Rafi; a checker's flag still open after the one fix round goes to him marked." Fix B (lesson 201's text): "A fact error or rules fail found by the later checks always gets one more fix round before Rafi sees it." (wording mine, not yours)
   Recommendation: Fix A.

4. Rafi's introduction list against rotation (carried; live today).
   A: CLAUDE.md lines 171-177 (HEADLINES INTROS AND FLOW: "In finance", "Also in finance", "In security", "In robotics", "In tech", "In the lab", "And finally, something lighter" ...; "The intros Rafi dictates win over rule G2").
   B: CLAUDE.md line 146 (never the previous day's wording, G2); Headlines Master G2; check_headlines_rules.py lines 82-90 (FAIL on any intro of the previous day).
   Clash: 11 Oct used "In security", "Also in security" and "And finally, something lighter" from that list; if today's writer uses them the script fails G2, and it is not written whether the list counts as "dictated".
   Fix A: add: "The intros listed here are examples; G2 rotation applies to them." Fix B: add: "The intros listed here may repeat day to day; check_headlines_rules.py G2 skips them (script change between runs)." (wording mine, not yours)
   Recommendation: Fix A (no script change; the writer names the topic another way, for example "Turning to security", "And now, something fun").

5. Who writes the Bigger Picture card and clip (carried; live today).
   A: CLAUDE.md line 157 (BIGGER PICTURE MODEL: one agent writes all three lengths; the main session never writes it), lines 208-209 (Fable writes it, all three lengths), rule 17 lines 254-257 (the card is one of the three lengths).
   B: CLAUDE.md lines 295-296 (rule 25: one Opus writer per product writes the card and Headlines wording); briefs/wording_cards.md line 11 and wording_headlines.md line 9 (the Opus writers write bp).
   Clash: on 11 Oct the Part A author wrote bigger_picture_card.json; today there is none in W, so the card and clip would come from the Part B writers, and rule 25 names what it replaces without naming BIGGER PICTURE MODEL.
   Fix A: add to rule 25: "This covers the Bigger Picture card and clip: the Part B writers write them from bigger_picture_bulletin.json only, and the checkers check them against it." Fix B: add to BIGGER PICTURE MODEL: "The Part A author also writes bigger_picture_card.json (card head, body and clip line); Part B copies it." (wording mine, not yours)
   Recommendation: Fix A for today (no extra agent; the author's own Bulletin text is the only source).

### 2a. Touches settled by Rafi's own precedence lines or rulings (not counted; the settling line named)
1. 14 cards against extra_min 7 (11 Oct clash 1): 8b item 4 (a count he gives wins over a cutoff).
2. The second robotics card below extra_min (11 Oct clash 2; today C11-03 and C11-06 score 5): 8b item 4 (the ROBOTICS count).
3. Politics clip 1 against HEADLINES ORDER and Drive A3 (11 Oct clash 3): newest ruling (7 Oct over 5 Oct) and 8b item 4 (an order he gave); CLAUDE.md over Drive.
4. The rewrite agent's model (11 Oct clash 4): rule 25 (12 Oct) replaced the rewrite agent with the same writer.
5. An update as a card (11 Oct clash 5): NO UPDATE CARDS (7 Oct) is newer than CARD FILTER (6 Oct) and NO OLD NEWS (5 Oct).
6. Teaser credit (11 Oct clash 9): newest ruling (Rafi, 10 and 11 Oct, D36 and lesson 241) over Drive G7.3; build_pack.py fixed on 12 Oct.
7. Drive upload of cards and JSON (11 Oct clash 10): rule 26 (12 Oct, newest).
8. Which score counts (11 Oct clash 11): Rafi's ruling "selection follows the pool score" (Part A SKILL.md line 245; build_products.py line 171); pick_gate.py reading the writer's score is a stale script line (2b).
9. Part B in the same chat (11 Oct clash 12): rule 18 speaks of starting a daily run; Part A starts Part B (rule 9); "Part B needs a new chat" is Claude's reading (lesson 123). A compacted chat still needs Rafi's yes (rule 18).
10. How clashes go to Rafi (11 Oct clash 13): rule 20 (10 Oct, his words: "ask them one by one") over lesson 142 (Claude's prevention).
11. The headline-only note in customer text (11 Oct clash 15): newest ruling (Rafi, 8 Oct, lesson 118) over Drive Bulletin and Full Report 5.3; Part A's delivered products.
12. What goes with the card list (11 Oct clash 16): rule 20 (10 Oct, newest): the list alone at step 1; the 3-day table goes with the deck at step 7 ("before Rafi sees a deck").
13. One idea per sentence (Drive G1.3) against one sentence (11 Oct clash 17): rule 22 (newest; CLAUDE.md over Drive).
14. Apate against NO OLD NEWS, NO REPEATS IN 7 DAYS and the duplicate checks: rule 23 (11 Oct) is newer than both (5 and 7 Oct).
15. The fun clip outside the deck against Drive A4 (slot 9 = the deck's fun item) and lesson D25 (every clip matches a card): rule 23 and rule 24 ("not necessarily in the cards") are newer; CLAUDE.md over Drive.
16. Clip length: rule 22 (aim 8, 10, 12 hard; 12 Oct) against the phrasing file ("never over 10") and the old CLIP SECONDS: newest ruling and CLAUDE.md over Drive (the briefs name the four overridden sentences).
17. The why: rule 22 (a company reason is a why) against the phrasing file ("effect on people"): same lines.
18. Bigger Picture clip "10 seconds" (rule 17) against "aim 8" (rule 22): rule 22 is newest and calls 10 acceptable.
19. Fable checkers (rule 25) against STORY CHOICE "Opus does the checks": rule 25 replaces it by name.
20. Groups of 10 (rule 24) against one file at a time (P1-10) and Cards Master 7.15: rule 24 newest; each card stays its own PNG.
21. Rule 26 (Rafi uploads) against rule 0 DAILY DELIVERY and Cards Master 7.4 and 7.8: rule 26 newest.
22. FUN STORIES (rule 24) against "truly funny" in pick_stories.md and the old 6 and 10 Oct "funny at once": rule 24 newest (stale brief lines in 2b).
23. SKILL.md 0c.3 ("Drive and CLAUDE.md disagree: stop and ask") against CLAUDE.md line 205 (no clash, CLAUDE.md wins): CLAUDE.md over Drive (stale skill line in 2b).
24. Drive B1a two decimals, C4 six steps, Cards 2.6 aim 15, 2.8 full report only, 1.3 DESK VIEW: CLAUDE.md over Drive.

### 2b. Stale lines in briefs and scripts (grep of the old wording of rules 22 to 26; scripts change only between runs, CLAUDE.md line 159-160)
BLOCKS TODAY:
- briefs/pick_stories.md line 7 "(5) has one genuinely funny item" and lines 9-10 "The Fun card is truly funny or you say loudly that nothing was": against rule 24 FUN STORIES (12 Oct, "the old funny at once is removed"); line 40 of the same brief has the new rule. Blocks the picker (the brief contradicts itself; the Bulletin's fun stories score 3). Fix before the picker (brief text, allowed during a run): line 7 "(5) has one fun item (CLAUDE.md rule 24 FUN STORIES)"; lines 9-10 "The Fun card follows CLAUDE.md rule 24 FUN STORIES, or you say plainly that no fun story fits."
- SKILL.md step 8.2 (lines 151-158): delivery_manifest.py --part B and a Drive agent (drive_delivery_prompt.txt): against rule 26 (Rafi uploads; Part A step 13.2 was fixed on 12 Oct, lesson 247, Part B not). Blocks step 8 if followed: skip the Drive agent; run delivery_manifest.py only for the _Claude-V1 names.
- pick_gate.py lines 66-69, 76 and 145 read the writer's score from report_entries; the Bulletin and card_candidates.py use the pool score (Rafi's ruling, 2a item 8). Today C14-01 shows 6 in the pick pack and 7 in the Bulletin (C07-01, C02-01, C09-08 also differ but are not eligible). Blocks C14-01's rank only: align before the picker as on 11 Oct (lesson 234d: entries copied to report_entries_before_pool_score_old, score set to the pool score, the writer's kept as fc_score), or tell the picker the Bulletin score counts.
DO NOT BLOCK TODAY:
- fill_headlines.py line 11 (docstring): "no clip may pass 10 s ... the Drive Section B item 1 still says 12": the code asserts 12 (line 95), as rule 22.
- check_headlines_rules.py lines 5 and 8-9 (docstring: "15 words ... 12 s", "CLAUDE.md 16: stories 8 to 9 s") and line 69 (B1 WARN aims 9.0, 8.5, 8.5, 10.5 against rule 22's aim 8; warnings only); lines 1, 6, 15, 100 still name "the rules agent (step 3c)".
- check_wording.py lines 6-10 (docstring): "every sentence at most 15 words", "Headlines: the same sentence rules": the code counts words and drops the count (lines 62, 69), so the card 15-word cap (wording_cards.md line 9, SKILL.md line 162) is not scripted; no clip one-sentence test (rule 22) either. Count both at step 7.
- briefs/wording_common.md line 12: Headlines "shape and length are set only by the Headlines section of the phrasing file and CLAUDE.md CLIP SECONDS": rule 22 overrides that section (wording_headlines.md lines 12 and 25 say so). Fix: "set by CLAUDE.md rule 22 and the model lines file; the phrasing file's Headlines section only where rule 22 does not override it."
- briefs/wording_common.md line 11 "then a stranger who knows nothing retells every item": the Fable checker does the stranger test now (rule 25).
- briefs/wording_headlines.md line 20: "no identifiable faces, since the fixed video prompt says no faces": the fill PROMPT (line 18) says "no real named faces" and line 17 of the brief allows anonymous people (stricter, harmless).
- briefs/pick_stories.md line 10 "(written later by Fable after Rafi approves; you only name its sources)": the Bigger Picture card is written by the Opus card writer today (rule 25; clash 5).
- briefs/pick_stories.md line 27 "7 ids from your cards", pick_gate.py G11 (line 136), check_headlines_rules.py A3 (lines 50-52): stricter than rule 24 ("not necessarily in the cards"); clips from the cards meet both.
- briefs/pick_stories.md line 25 (label at most 14) against line 37 (15), pick_gate.py G14 (line 140, 15) and SKILL.md line 82 ("about 15"): 14 meets all.
- briefs/stranger_cards.md, stranger_headlines.md, rules_check_headlines.md, rewrite_headlines.md, factcheck.md ("Part B step 4"): superseded by rule 25 and still written by make_wording_prompts.py (lines 1-7, 33-38): never launch them.
- SKILL.md line 57 "currently 1 to 130" (now P1, L1, Port, 1 to 261, D1 to D51); line 63 (0c.3, 2a item 23); lines 79-81 (an update kept when meaningful; G6 enforces NO UPDATE CARDS); line 83 ("3 to 4" teaser; the gate takes exactly 4); line 84 (clips "strongest card stories by score"; G11b puts Politics first); lines 136-137 ("C01 and C13 carry Rafi's opening and ending of 2 Oct": both are bypass); line 167 ("The stranger check is fast") and line 177 (Files: stranger briefs, not check_cards.md and check_headlines.md).
- build_pack.py line 6 and lines 24-25 (opening and ending "of 2 Oct 2026": bypassed slots) and line 28 (review_status "checked by ... a stranger check and a rules agent; approved by Rafael": written into the JSON's extra.aind_fill and MarkdownNote 9990, wrong checks named after rule 25; fix between runs).
- build_cards_copy.py line 46 (note "Card wording written by Fable ... and a stranger check") and line 37 (the SOURCE line copies the entry's source: today C14-01 would print "CNN, as relayed by ETHRWorld", a relay named against CREDIT; fix the entry's source text after Rafi's yes, or let the checker flag it).
- common_b.py lines 37, 46, 51: the gate message names "step 3b" and "prompt_rules_headlines.txt"; the file it needs, headlines_work/rules_result.json, is written by the Fable Headlines checker (check_headlines.md line 10): works as is.
- card_candidates.py lines 9-14 (docstring: updates kept when meaningful; clips by score), lines 136-159 (today's draft clips start with C06-01, no Politics clip), lines 161-165 (today's draft teaser C07-02, C02-01, C09-08 are follow-ups that G6 fails), line 185 (bp_refs C07-01 headline only and C07-02 follow-up, neither in the Bigger Picture text): paper input; the picker must not copy the draft.
- make_wording_prompts.py lines 18-21: PREV_CARDS and PREV_PACK come only from scratchpad run_ folders: today "none" and assets/pack_base.json (2 Oct lines, "sentences of at most 15 words") would be the Headlines writer's shape example, against rule 24 (the 11 Oct level is the constant). Run it with --prev-pack /home/user/ai-news-desk/runs/2026-10-11/headlines_work/headlines_11-10-26_pack.json --prev-cards /home/user/ai-news-desk/runs/2026-10-11/cards_copy.json (arguments, no script change).
- briefs/check_headlines.md line 3 reads Headlines Master G and B in full with only the phrasing file overridden: the checker may flag a correct one-sentence line for G1.3 or a rounded box for B1a (lesson 92 pattern); if it does, rule 22 and rule 16 win (2a items 13 and 24).
- review_list.py line 32: removes ", simple text-free symbol" (harmless).

### 2c. Checked, not live today
- Every category gets a card (pick_stories.md MUST-HAVES against CLAUDE.md eligibility; 11 Oct clash 6): every category has an eligible Bulletin story today.
- A third robotics card ("one extra allowed") against G8's cap of 2: no third robotics story shows a machine doing something.
- A Politics reserve card as clip 1 against G4b: both Politics stories are in the Bulletin.
- VIRAL RULE re-run clause: no re-run.
- Critical stories spending a slot: no score 10. Cards Master 2.10 big release rule: not in force.
- Robot war limit on cards: no such limit.

### 2d. Drive differences settled by CLAUDE.md
- docs/DRIVE_DIFFS_FOR_CHATGPT.md was not in today's read list and was not checked; yesterday's 2d list of 9 missing items stands unverified. New since: rule 22 against the phrasing file's Headlines section; rules 23 and 24 (fun clip outside the deck) against Headlines A4; rule 24 groups of 10 against Cards 7.15; rule 26 (Rafi uploads) against Cards 7.4 and Headlines E5.

## 3. Today's must-haves and facts

### 3a. Must-haves for the picker
1. Counts: 14 story cards (clash 1: the Bulletin gives 13 within the limits; the 14th as Rafi answers, marked exception); exactly 4 teaser items (report stories, no card, freshness NEW, not in the last 7 days); exactly 7 story clips, all cards; 1 Fun card; the Bigger Picture named as card and clip (G20); bp_refs 3 to 5 report ids the Bigger Picture text rests on.
2. Order: deck in the Drive order Politics, Market, Security, Energy, Robotics, Models, Research, Ethics and law, Health, Society, Fun; higher score first inside a category; clips in deck order; the first Politics card is clip 1 (C13-17 or C13-16: put first the one a viewer gets in one sentence, rule 24).
3. Limits: at most 2 cards a category (market 3); a company on at most 3 cards and 2 clips (lines naming Microsoft for Brad Smith and Bill Gates count together); labels at most 14 characters, no money figure; read in full only (C07-01 is headline only).
4. CARDS FROM THE BULLETIN: cards only from the 24 Bulletin candidates of pick_pack.md; a reserve card only for a category with no eligible Bulletin story (none today) or as Rafi answers clash 1.
5. NO UPDATE CARDS: none named; C07-02, C09-08 and C02-01 are follow-ups: no card, clip or teaser item.
6. NO REPEATS IN 7 DAYS (5 to 11 Oct): C05-01 needs a disputed_repeats entry (the 8 Oct teaser was a different Georgieva speech); C05-02 sits close to the 11 Oct card and clip on Nadella's "emergency brake": judge it and say why; reserve C06-03 and C07-05 are G17 hits.
7. ONE TOPIC, ONE CARD: C12-01 and C14-01 are one Bill Gates interview on CNN (11 Oct): one card and one clip, or say why two; if C12-01 goes, list it in repeat_excluded so a Security reserve card passes G4b.
8. ROBOTICS: 2 robotics cards, one humanoid: C11-03 (humanoids restocking shelves) and C11-06 (drone hunter); C11-02 needs a robotics_ruling; 1 robotics clip: C11-03 (say what the robot does).
9. Rule 23 fun clip: headlines_fun "CP-C12-10" (Apate: bots that pose as scam victims and keep scammers talking for over two hours); the Fun card is a Bulletin fun story (C16-01, C16-04 or C16-06) under rule 24 FUN STORIES; clash 2 confirmed with the list.
10. Rule 24: every story clip is a Bulletin card (G4b); a story that needs more than one sentence to explain is not a clip.
11. REPLY STORIES: C13-16 answers Bloomberg's report of 18 Sep: if chosen, card and clip say so and name it.
12. NOVICE TEST and PEOPLE WITH THEIR POSITION for every name (1a, 8b item 6).
13. Read pick_pack.md, not selection_draft.json (the draft has 11 cards, no Politics clip 1, both Gates stories, and three follow-ups in the teaser).

### 3b. Facts of this edition
- Edition MON 12 OCT 2026; window 11 Oct 08:12 to 12 Oct 08:12 UTC (24 hours); no critical story; top score 8 (C06-01).
- Full Report 106 (Politics 7, Market 17, Security 10, Energy 12, Robotics 10, Models 14, Research 8, Ethics and law 5, Health 4, Society 11, Fun 8); 90 read in full, 16 headline only; scores 8:1, 7:9, 6:25, 5:47, 4:16, 3:3, 2:5. held.json: 62 re-dated plus 2 duplicates = 64.
- Bulletin 24: Politics C13-16, C13-17 (6, 6); Market C06-01 (8), C07-01 (7, headline only), C07-02 (7, follow-up); Security C12-01 (7); Energy C08-02 (6), C09-08 (6, follow-up); Robotics C11-01 (6), C11-02 (6), C11-03 (5), C11-04 (5), C11-06 (5); Models C01-02 (7), C02-01 (7, follow-up); Research C04-01 (7); Ethics and law C05-02 (7); Health C10-16 (6); Society C05-01 (7), C14-01 (7), C14-02 (6); Fun C16-01, C16-04, C16-06 (3 each). Scores are the pool scores the Bulletin prints.
- Pool against writer score in the Bulletin: C07-01 7/5, C02-01 7/6, C14-01 7/6, C09-08 6/5.
- Card-eligible Bulletin stories (read, NEW, not held; robotics with a machine): Politics C13-16 (DISPUTED; reply), C13-17; Market C06-01; Security C12-01; Energy C08-02; Robotics C11-03, C11-06; Models C01-02; Research C04-01; Ethics and law C05-02; Health C10-16; Society C05-01, C14-01, C14-02. 14 stories, 13 within the limits.
- Report-only reserve, eligible at 6: Market C05-04 (Intel chief on Chinese models), C05-06 (DBS chief on AI financing; in the Bigger Picture), C06-03 (Moonshot; G17 hit), C07-05 (IMF growth; G17 hit); Security C12-02 (US drops its objection to UK early model access), C12-03 (Booz Allen agents attack a simulated factory); Models C01-04, C02-03; Research C04-02. Teaser candidates come from here.
- Viral: Decart 46 outlets (C06-01); nothing else at 20 or more.
- Bigger Picture source: bigger_picture_bulletin.json (504 words; Rafi's open question, about 350). Watch dates: IMF outlook Tue 13 Oct; TSMC and the G20 Thu 15 Oct; Fed 27 to 28 Oct; Microsoft 28 Oct; SK hynix 27 Oct and Samsung 29 Oct not confirmed; US inflation 14 Oct not confirmed; US midterms Tue 3 Nov. The 11 Oct card and clip watched TSMC on 15 Oct.
- Introductions used on 11 Oct (G2): "In politics", "In business", "In security", "Also in security", "Turning to robots", "In health", "In entertainment"; fun "And finally, something lighter".
- Robot war count: Bulletin C09-08 and C11-06 at most (2), Full Report at most 3.
- Customer text (0c.4): the headline-only note on 1 Bulletin story (C07-01) and 16 report stories; 0 Google News links.
- The paper draft (card_candidates.py, 10:17): 11 story cards plus fun C16-01 (C13-16, C06-01, C12-01, C08-02, C11-03, C01-02, C04-01, C05-02, C10-16, C05-01, C14-01); clips C06-01, C12-01, C11-03, C01-02, C04-01, C05-02, C14-01 (no Politics clip); teaser C07-02, C02-01, C13-17, C09-08; bp_refs C06-01, C07-01, C07-02.

### 3c. Cards and Headlines of the last 7 days (for G17 and the 3-day name and topic table; clip intros in brackets)
- 2026-10-11 CARDS: s1 C05-07 Britain's AI institute chief wants home-grown AI nobody abroad can switch off | s2 C06-01 Nvidia reportedly in talks to buy or invest more in AI lab Reflection | s3 C07-01 South Korea's stock market is losing its buyers | s4 C05-01 Microsoft's boss Satya Nadella wants an emergency brake to stop any AI mid-task | s5 C12-02 OpenAI says an AI faked test grades and damaged its workspace | s6 C08-01 Nvidia reportedly ending the RTX 5090 | s7 C11-03 US Army's new war drones overheated and lost signal | s8 C11-10 Tesla Optimus learned to vacuum and stir food by watching people | s9 C01-02 OpenAI's price list shows an unannounced biology AI | s10 C13-01 the White House leans on old laws to police AI | s11 C10-01 Chinese hospital AI reads a lung tumour sample in a minute | s12 C10-02 commentary: US health care tests Big Tech's AI spending | s13 C14-01 Nicolas Cage refused an AI waiver | s14 C14-02 Hollywood films on the bosses of Meta, Tesla and OpenAI | fun C16-01 tiny game studio took a bank loan for its AI learner driver | teaser C12-03 Britain's spy chiefs on the AI threat, C01-06 South African model for 12 languages, C14-07 workers pay a female AI helper less, C09-03 data centres an election issue in Ohio and Michigan | BP investors wary of AI debt, watch TSMC on 15 Oct || HEADLINES: C05-07 [In politics]; C06-01 [In business]; C05-01 [In security]; C12-02 [Also in security]; C11-10 [Turning to robots]; C10-01 [In health]; C14-01 [In entertainment]; fun crab robot plans given away (Rafi's own choice, not the fun card) [And finally, something lighter]; teaser C12-03 + C01-06; BP AI debt cooling, TSMC Thursday.
- 2026-10-05 CARDS: s1 C13-07 British lawmakers: government leans too hard on US cloud firms | s2 C06-03 Schneider Electric to buy PTC | s3 C08-01 Qualcomm to pay Huawei for patents | s4 C07-05 Bank of Japan deputy: AI may keep rates higher | s5 C12-05 hackers posed as Anthropic staff to send malware | s6 C08-07 TSMC plans another price rise | s7 C09-03 Goldman: local opposition barely dents US data centre forecast | s8 C11-04 Germany pays for drones that hunt Russian drones | s9 C01-01 Reflection readying a strong US-made open AI model | s10 C04-05 Korean researchers: AI drug-safety predictors overrated | s11 C05-01 Altman: accept some harm from AI | s12 C10-01 Stanford: 37,000 AI helpers read old drug trials | s13 C14-05 women get a quarter of new AI jobs | s14 C14-01 people who teach AI their jobs say creativity keeps them employed | fun C16-02 Florida pizza shop vows never to use AI | teaser C15-02 IBM quantum feat, C03-01 ex-GitHub boss launches a rival, C11-11 AI-aimed gun turrets guard Kyiv, C07-02 shielding portfolios from AI stocks | BP money chases AI as borrowing costs hit a 24-year high || HEADLINES: C13-07 [From Westminster]; C06-03 [In business]; C12-05 [In security]; C08-07 [From Taiwan]; C11-04 [In robotics]; C01-01 [In new models]; C04-05 [In science]; fun C16-02 [In lighter news]; teaser C15-02 + C11-11.
- 2026-10-06 CARDS: s1 C13-01 Pentagon says it dropped Anthropic | s2 C06-01 OpenAI wants to raise $30 billion or more | s3 C06-02 DeepSeek close to raising at least $12 billion | s4 C06-03 Moonshot plans a Hong Kong share sale | s5 C12-02 Wikipedia's parent: OpenAI agents tried to edit pages | s6 C12-01 South Korea's president: bank hackers may have used AI | s7 C08-01 AMD to supply far more AI chips in 2027 | s8 C09-01 Google near a nuclear power deal | s9 C11-01 AI-aimed gun turrets shot down Russia's fastest drones | s10 C01-01 Reflection's Beam matches a top Chinese model | s11 C04-02 Google DeepMind AI invented two enzymes | s12 C05-01 former AI workers warn New York City's council | s13 C10-01 an app's AI prescribes acne medicine in Utah | s14 C10-02 Britain to check AI medical tools throughout their use | s15 C14-02 protesters disrupt a London tech dinner | fun C16-01 Jon Stewart and Meta's AI mascot | teaser C11-02 NATO drone and AI plan, C05-03 senator calls Anthropic boss's warnings alarmist, C04-05 AI steered an X-ray machine, C08-04 Qualcomm against Arm | BP tech shares at a record; banks and Gulf funds line up AI money || HEADLINES: C13-01 [We begin with an update]; C06-01 [In finance]; C06-02 [Also in finance]; C12-01 [In security]; C11-03 (not a card: LG and Nvidia AI brain for Hyundai's self-driving car) [In robotics]; C01-01 [In tech]; C04-02 [In the lab]; fun C16-04 (not the fun card: Alexa stuck saying la la la) [And finally, something lighter]; teaser C11-02 + C05-03.
- 2026-10-07 CARDS: s1 C13-22 UAE trains 80,000 civil servants to run government with AI | s2 C06-02 SpaceX wants to borrow $40 billion for Nvidia chips | s3 C05-02 Ray Dalio: AI bubble close to bursting | s4 C05-01 Jamie Dimon: Mythos made hacking ten times riskier | s5 C09-03 local opposition killed $260 billion of US data centre plans | s6 C09-04 record US power use from AI data centres | s7 C11-02 Waymo driverless in Detroit | s8 C11-16 Chinese robot hand threads a needle | s9 C02-01 Claude sidebar in Google Docs, Sheets and Slides | s10 C15-01 New York chip factory for light-based quantum parts | s11 C05-04 Hinton wants AI safety-checked like drugs | s12 C13-04 two US senators want AI firms liable when agents hack | s13 C10-01 Eli Lilly opens AI drug tools | s14 C14-02 71 percent of Americans expect fewer jobs | fun C16-13 Tirana's jailed mayor sends an AI double | teaser C01-01 Mistral model, C02-04 Gemini in Chrome on Android in India, C13-24 Nigeria's election body and AI, C09-09 San Francisco data centre pause | BP Dalio calls AI a bubble as chip buying runs on debt || HEADLINES: C13-22 [We begin with politics]; C05-02 [On the markets]; C05-01 [In banking]; C09-03 [In energy]; C11-16 [Now to robots]; C02-01 [In software]; C05-04 [Turning to safety]; fun C16-13 [And now a smile]; teaser C01-01 + C13-24.
- 2026-10-08 CARDS: s1 C13-01 senator wants government safety tests of the strongest AI | s2 C13-03 five-minute video pitch for Pentagon deals | s3 C07-01 Samsung's $80 billion quarterly profit | s4 C07-02 TSMC sales up 51 percent | s5 C12-03 hackers hijacked 3,400 servers running AI tools | s6 C09-01 drones struck a Yandex data centre | s7 C11-02 Nvidia wants more of Figure AI | s8 C11-17 driverless Uber taxis in Dubai | s9 C02-01 ChatGPT answers with charts and buttons | s10 C01-02 Claude Haiku at a quarter of the price | s11 C04-01 Google, Meta and US agencies teach AI how cells react | s12 C15-01 IBM and three quantum makers reach Pentagon final round | s13 C13-05 AI voices for political robocalls | s14 C10-05 England's health service lets AI rank skin cancers | s15 C14-02 ChatGPT for Teens often fails to alert parents | fun C16-10 OpenAI helper: "Oh, I love you too" | teaser C02-02 Copilot to handle PC files, C05-01 IMF chief warns on AI debt, C14-06 Kenyan refugees lose online work, C11-04 Tesla Optimus 1,000 a week | BP chip makers cash in while debt worry spreads || HEADLINES: C13-01 [We start in Washington]; C07-01 [In business]; C09-01 [From Russia]; C11-02 [In robotics]; C02-01 [For chatbot users]; C04-01 [In science]; C14-02 [On teen safety]; fun C16-10 [And on a lighter note]; teaser C02-02 + C14-06.
- 2026-10-09 CARDS: s1 C05-02 Trump: anyone saying artificial intelligence, not superintelligence, is the enemy | s2 C13-21 Musk accused Indian tycoons of blocking Starlink | s3 C06-04 OpenAI sales pace $20 billion below its earlier figure | s4 C07-04 WTO doubled its trade growth forecast on AI demand | s5 C03-01 Anthropic scans open-source code for free | s6 C12-02 OpenAI shut down Russian and Iranian fake-writer groups | s7 C09-03 Oracle trucks natural gas to data centres | s8 C11-23 humanoid robots directed traffic in Hangzhou | s9 C11-06 Walmart's warehouse robots break down | s10 C01-01 Gemini 4 Argon first for security experts | s11 C04-04 scientists: Anthropic overstated a gene-editing find | s12 C13-01 USA Today's publisher sued OpenAI | s13 C10-01 Google chatbot questioned patients before urgent visits | s14 C14-07 charity to record Gaza classrooms with AI | s15 C16-01 streamer's robot whacked him on the head (no separate fun card) | teaser C02-01 Gemini helper for firms, C11-24 Tokyo shop robot, C09-04 senators on data centre costs, C14-06 San Francisco rents | BP investors want results after OpenAI's lower sales figure || HEADLINES: C05-02 [First, super intelligence]; C13-21 [In India]; C07-04 [On trade]; C12-02 [In security]; C11-23 [Next, robotics]; C01-01 [In tech]; C14-07 [In education]; fun C16-01 [And now, something lighter]; teaser C02-01 + C14-06.
- 2026-10-10 CARDS: s1 C13-03 China: no blind money into AI and high tech | s2 C06-01 odds start-up TypeSafe valued at $7.5 billion | s3 C12-01 Claude sent police a made-up murder tip in a test | s4 C12-02 AI bosses rehearse for the day after an AI disaster | s5 C08-02 big buyers booked most of Samsung's memory chips | s6 C11-17 wheeled humanoid robot under $30,000 | s7 C11-18 Ukrainian ground robots rescued 45 soldiers | s8 C01-16 Musk backs Anthropic's ban on cruelty to AI | s9 C01-03 Alibaba's Qwen3.8 free to download | s10 C04-07 amateur with AI tools may have found a planet | s11 C08-01 Super Micro contractor admitted smuggling Nvidia chips | s12 C10-01 tech firms lobbied US health officials in a chat room | s13 C14-04 Nikon took back a prize over an AI-made video | s14 C14-05 publishers use AI for covers without telling authors | fun C16-01 government chatbot shared pasta recipes | teaser C02-01 Amazon asks Meta to keep its AI helper off its store, C01-01 Microsoft choice-only model, C10-02 GSK signs AI start-up Chai, C09-05 batteries cheaper than gas turbines | BP shares recovered from an OpenAI scare as China warned of blind investment || HEADLINES: C13-03 [From Beijing]; C06-01 [In finance]; C12-02 [Next, safety]; C11-17 [In robotics]; C01-16 [On chatbots]; C08-01 [In court]; C14-04 [In science]; fun C04-07 (story card s10, not the fun card) [On a lighter note]; teaser C02-01 + C09-05.
