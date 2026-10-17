# Rules check, Part B (cards and Headlines), edition 2026-10-16 (FRI 16 OCT 2026)

Updated from runs/2026-10-15/rules_check.md by the delta of 2026-10-16 (rules_delta.md: base commit 468d519, now 24d30df). Written by the rules-check helper (Sonnet), Part B step 0c, incremental (lessons 262 and 272b).
Read in full: rules_check_previous.md and rules_delta.md. Opened only around a change: briefs/wording_headlines.md lines 9 and 25-30, briefs/check_headlines.md lines 8-10, scripts/check_headlines_rules.py lines 84-100 (B2d, B2e), Part A SKILL.md grep for step 11b; CLAUDE.md line numbers by grep. Today's facts (section 3) come only from cards_work/pick_pack.json, cards_work/selection_draft.json and products/bulletin_pdf.json (counts, ids, headlines), plus run.json, bigger_picture_bulletin.json and products/report_pdf.json (the report's story count and the not-found lines, by grep). Not read in full: docs/V1_TASKS.md, CLAUDE.md (in context, 335 lines), the skills, the Drive rule files.
CLAUDE.md: the copy in this helper's context ends at rule 35 and the disk file has 335 lines. CLAUDE.md line numbers in section 2 are recomputed by grep (+2 after line 152 since the MODEL TEST insert).
W = /tmp/claude-0/-home-user-ai-news-desk/b8ea3875-9c2c-5929-a741-f80fedb02485/scratchpad/run_2026-10-16
State at 07:22 UTC (file times): Part A's files are in products/ and for_rafi/. At 07:22 card_candidates.py (cards_work/selection_draft.json) and pick_gate.py pack (pick_pack.json and .md, prompt_picker.txt) ran: paper input only, nothing chosen. No selection_fable.json, no wording, no cover, no headlines_work folder yet.
Every fix offered in section 2 is my wording, not Rafi's (CLAUDE.md rule 20). Nothing was applied.

## CHANGED SINCE 2026-10-15 (one line per change in the delta; "met" = how this run meets it)

CLAUDE.md
1. MODEL TEST line (new, 15 Oct; CLAUDE.md line 152): does not change today's models; met by the MODEL POLICY line (1a), which now points to docs/model_test_2026-10-14/README.md before any change.
2. Rule 31, "yes to all what you asked before" (a section whose 7-and-up stories are all headline only counts as empty): met, no such section today (1a Rule 31; clash 10 for the "at least 2" wording). Rule 31 itself was not in the 15 Oct check (written after it).
3. Rule 32 USELESS TAIL: met by the writer and checker briefs and the checker's 3b; no script check (1a; lesson 304).
4. Rule 32 FROM WASHINGTON: met by B2d and B2e; allowed for politics only (1a; lesson 305); clash 9 narrower.
5. Rule 32 NAMES NEED TITLES: met by the checkers and the final audit; no script check (1a; 8b item 6; lesson 307).
6. Rule 32 CUSTOMER PRODUCTS: met by cards_copy.json carrying text only; verify at step 7 (1a).
7. Rule 32 SIMPLE ANSWERS: applies to the step 1 and step 7 messages (1a; touches clash 7).
8. Rule 32 THE FUN CLIP ("In today's fun corner"): met by the fun intro; clash 3 is live because G2 sees it as yesterday's wording (1a; clash 3).
9. Rule 33 SOCIAL POSTING: does not apply to Part B (not built; 1e).
10. Rule 34 (a story that ran at 7 or more may return when it is a meaningful update): applies to the Bulletin (Part A); for cards NO UPDATE CARDS still blocks (G6); today C08-16 is the one such story (1a; clash 11).
11. Rule 35 (not-found: search first, then "Read the full article at <source>."): met by Part A today (Bulletin 1, report 4, 0 old notes); a headline-only story is never a card (1a; 1b line 5.3).

docs/V1_TASKS.md (added lines 304 to 316)
12. 304 useless tail: see 3. 305 From Washington: see 4. 306 customer products: see 6 (purpose line in words today: lesson 150 closed). 307 titles: see 5.
13. 308 cards unclear (nine lines too short): met by the card checker's stranger test and 1b read-aloud verdict at step 3 (new 1d line).
14. 309 the 13 Oct run was never saved: G17 covers 6 of 7 days again (1d line 281 rewritten; 2e item 1).
15. 310 the model test: nothing changed; see 1 (new 1d line).
16. 311 the not-found note: see 11; Part A only (1e). 312 a relay page is not the source: met by checking every SOURCE line at step 7 (1a CREDIT; new 1d line).
17. 313 late additions chain the Bigger Picture: Part A (1e). 314 viral sweep missed a same-day repeat by headline: G17 hits judged by name (1a; new 1d line). 315 Part A writers read once: Part A (1e). 316 second-read helper restored scores: Part A (1e); the pool-score gap of 2b is 8 stories today.

Skills, briefs, scripts, Drive
18. Part A SKILL.md step 11b (not-found note): Part A only; Part B reads its product (see 11).
19. Part A briefs/bigger_picture.md (no process wording) and build_products.py (2 lines, names for codes): Part A's products; the Bulletin purpose line prints names today.
20. Part B briefs/check_headlines.md (3b THE LAST PART) and wording_headlines.md (hedge is one word; line 27 "From Washington" exception): met by the Headlines writer and checker (see 3 and 4); wording_headlines.md line 9 is unchanged (clash 9).
21. Part B scripts/check_headlines_rules.py (B2d allows "from washington"; B2e matched): met at step 3 and by the gate.
22. Drive rule files: "no change" against runs/2026-10-15/rules (delta section 4); not diffed again here.
Found beyond the delta: rule 31 as a whole (its first lines came after the 15 Oct check; read from the CLAUDE.md context copy).

## 1. One line per rule and lesson

### 1a. CLAUDE.md rules that touch Part B today
- Rule 0 TOP (Drive read only): Part B reads Drive only for the renderer zip and the cover base (setup) and writes nothing to Drive (rule 26). To verify at step 8: no Drive write in Part B. At 07:22 UTC (file times) cards_work holds only pick_pack.json and .md, prompt_picker.txt and selection_draft.json; products/ and for_rafi/ hold only Part A files; the cover is not built yet.
- Rule 0 DAILY DELIVERY: replaced for now by rule 26 (newest: Rafi uploads the final products and the pool files). Part B gives him the cards, the contact sheet and the JSON in chat; the text copy goes to runs/2026-10-16 by save_state.py. SKILL step 8.2 now matches rule 26 (delivery_manifest.py --part B --copy-to; the old Drive text is kept for later).
- Rule 0 WHO MADE IT: every file Rafi uploads carries _Claude-V1: delivery_manifest.py --part B --copy-to $W/for_rafi copies every card, the contact sheet and the JSON under those names (lesson 257). Part A's six files already carry the label (for_rafi: AIND_Pool pdf, csv, json; Daily_Bulletin pdf; Full_Report pdf; daily-pool md). To verify at step 8: the names of the files sent.
- Rule 1 (route the job): routes fixed (cloud: choice, wording, cards, JSON; Rafi's PC: ComfyUI, stitch, Drive upload by hand). No open route.
- Rules 2, 15, 8b item 5 and rule 24 HOW CLAUDE EXPLAINS: one or two short sentences, simple words, "like I am six years old". Evidence: the step 1 list message and the step 7 one-line ask.
- Rule 3: superseded files renamed _old, a new cards_runN per render, the fill refuses to overwrite, never rm (lesson 230). Evidence: ls of W at step 8.
- Rule 4: Rafi's edits at steps 1 and 7 applied and shown one at a time.
- Rule 5: numbers as evidence: card files counted against cards_copy.json (assemble_cards.py), JSON bytes and md5, active slots, seconds, longest clip, news part (verify_headlines.py). To verify at steps 5 and 6.
- Rule 6: every card and clip fact from report_entries/<id>.json and facts/<id>.json, read once in the story pack (rule 27); the Fable checkers check every fact (check 3 of check_cards.md, check 4 of check_headlines.md). To verify at step 3: 0 open fact problems in cards_work/check_result.json and headlines_work/rules_result.json. No CP- item today.
- Rule 7: Claude does not judge the look; the contact sheet goes to Rafi first.
- Rule 8: an instruction Rafi gives during Part B goes into CLAUDE.md the same day, in his words (rule 20).
- Rule 8a: 11 clashes in section 2 (2 new today: 10 and 11; 1 to 9 carried from 15 Oct, 3 and 7 and 9 sharper), none chosen or applied; 2a lists the touches Rafi's own precedence lines settle, each with the line that settles it.
- Rule 8b item 1: no fix of section 2 runs before Rafi picks it.
- Rule 8b item 2: no brief may carry a rule's opposite: 2b lists stale brief lines; the fun lines of pick_stories.md (7, 9-10, 40) follow rule 24; its line 10 (Fable writes the Bigger Picture) and line 27 stay stale and do not block the choice. Briefs/wording_headlines.md line 9 still lists "In politics", "From Washington", "On the markets", "Turning to safety": since 15 Oct "From Washington" is allowed for politics (rule 32; B2d and B2e), but "On the markets" and "Turning to safety" still fail B2e; clash 9 is narrower, not closed.
- Rule 8b item 3: before Rafi sees the deck: the 0c.4 PASS/FAIL table, G17 over the 6 decks that exist in the 7 days (9, 10, 11, 12, 14 and 15 Oct; 48, 48, 48, 51, 48 and 48 lines in pick_pack.json; 13 Oct is empty, lessons 281, 299 and 309), the 3-day name and topic table (section 3c; G17 cannot see 13 Oct), and the final audit (SKILL step 6b, lesson 297) before every send. The paper draft already shows three faults the gate or the table must catch (3a items 3 and 14).
- Rule 8b item 4: counts and orders he gave: 14 story cards (the Bulletin gives 20 within the limits, so clash 1 sleeps; Politics has two eligible stories, clash 5 sleeps), 7 clips, 2 robotics cards with one humanoid (3a item 8: the paper draft has one robotics card and no humanoid), 1 robotics clip, Politics clip 1 (a score 10 would go above it, rule 30, none today); say how each was met.
- Rule 8b item 6: every named person with position and organisation. Names seen in today's pick pack headlines (to confirm from the entries, never from memory): Jensen Huang (Nvidia chief executive; C05-01, a follow-up); C.C. Wei (TSMC chairman and chief executive; C08-03); John Ternus (Apple's new chief executive; C08-04); Daron Acemoglu (MIT professor; C14-04, headline only); Elon Musk (TSMC in talks to join his project; C08-01); Mark Levine (New York City comptroller; in the Bigger Picture text, C13-03 headline says only "comptroller"); Ken Paxton (Texas Attorney General; reserve C09-03); the chief executive of Workday (C14-03, no name in the headline). Rule 32 NAMES NEED TITLES and lesson 307 (22 untitled names in the 15 Oct products; no script check yet) make this a checker duty: checker check 2, G15b.
- Rule 8b item 7: one check round and one fix round (rule 25, SKILL step 3); what stays open: clash 2.
- Rule 9: the skills only on branch claude/eager-archimedes-ajnex3; no PNG, MP4 or ComfyUI JSON in git (save_state.py copies text only).
- Rule 10: no brand mark on any screen line; fill PROMPT (fill_headlines.py line 18) says "No readable words, numbers or logos".
- Rule 14 COUNTS: the card target is a working target (clash 1 sleeps today). The Bulletin holds 39 stories (36 plus 3 Fun), inside the 30 to 50 guideline (bulletin_pdf.json): Part A's delivered product, not a Part B gate.
- Rule 14 BULLETIN SECTIONS NEVER EMPTY (0c.4 recheck) with rule 31 (a section whose 7-and-up stories are all headline only counts as empty): 11 of 11 sections hold stories (bulletin_pdf.json): Politics 3 (scores 8, 7, 7; C05-01 a follow-up, C13-03 and C13-04 read in full, so not "all headline only"), Market 5, Security 3, Energy 6, Robotics 5, Models 3, Research 2, Ethics and law 1 (one story at 8; two 6s sit in the report: C09-03 and C13-05; clash 10), Health 3, Society 5, Fun 3. PASS for "never empty"; clash 10 for "at least 2".
- Rule 14 Full Report 100 to 120: report_pdf.json says 111 stories, 11 categories (inside 100 to 120); the pick pack lists 111 report stories (39 Bulletin plus 72 report-only reserve). Lesson 303 (Full Report Bigger Picture about 12,300 words) is still open for Rafi (2e item 5); today's length is Part A's product.
- Rule 16 Fun Side: the pick pack lists 9 fun stories (Bulletin: C16-01 follow-up of 14 Oct and DISPUTED, C16-02 PRELIMINARY, C16-03 REPORTED; 6 more report-only); inside 5 to 10; the Bulletin holds the top 3 (scores 5, 4, 4 in the Bulletin; 4, 4, 4 in the pack).
- Rule 16 cards and clips: story cards by the CARD FILTER (target 14, clash 1), 7 into Headlines. Evidence: gate_result.json G2.
- Rule 16 news part about 90 s (now with rule 22's aims). Evidence: check_wording.py "news part" line, verify_headlines.py "news part". To verify at step 6.
- Rule 16 round up to the next half second: fill_headlines.py box_seconds and its node 13 assert (line 151). Evidence: the fill slot table.
- Rule 16 company limits (3 cards, 2 clips): G9, G10, check_headlines_rules.py C16. Crowded names among today's 32 eligible stories (pick pack companies field): Apple 4 (C01-01, C06-02, C08-03, C08-04), OpenAI 4 (C02-01, C04-01, C13-01 and one more), Nvidia 3, Tesla 3, Anthropic 3 (C12-01, C13-01, C13-03), Meta 2, TSMC 2. The paper draft puts Anthropic on exactly 3 cards (the limit) and counts Meta and Apple twice for one event (3a item 3).
- Rule 16 READER LEVEL (rule 27 replaces "re-read before each item"): cards level 6, Headlines level 5 with rule 22 and the 11 Oct level (rule 24); each writer and checker reads the phrasing rules once, inside its story pack (make_wording_prompts.py writes cards_work/story_pack.md and headlines_work/story_pack.md), and goes through each item once against the hard rules. Evidence: wording_common.md line 10 and the phrasing-file override in both writer prompts.
- Rule 16 CLIP SECONDS (points to rule 22): aim 8 s, 10 acceptable, 12 the hard limit. Evidence: check_wording.py FAIL over 12 (line 112), check_headlines_rules.py B1, fill assert (line 95), verify_headlines.py (12).
- Rule 16 CREDIT: the card SOURCE line is the entry's source as written (build_cards_copy.py line 37; card limit 32 characters, lesson 293); "X reports, citing Y" when the article credits another outlet; the Bigger Picture card says AIND and AI News Desk; the news credit and the footage credit are two credits (lesson 273; no footage today). Lesson 312 (16 Oct): a relay page is not the source; the Part A editor moved credits to the first reporter. Relays still visible in the pack text: C05-01 ("CNBC reports, as relayed by BigGo Finance"), C07-02 ("BigGo Finance reports" about CoreWeave bonds), C08-02 (Bloomberg), C08-03 (Livemint), C08-16 (The Verge). To verify at step 7: every SOURCE line on the sheet against the entry's source field. Four report stories end "Read the full article at <source>" (rule 35); the Bulletin has one; none can be a card.
- Rule 16 WRITE ONLY WHAT CAN PRINT: cards only from written entries. PASS by construction.
- Rule 16 REPLY STORIES: no story in the pack is flagged as a reply by the pool today. Read for it at step 3: C13-03 (New York City's comptroller urges Anthropic to delay its listing; the Bigger Picture text speaks of "Anthropic's answer to Mark Levine") and C05-01 (a follow-up of Huang's 14 Oct London remarks, not a card). check_wording.py's reply test fires only on the pool's follow_up flag, so both checkers must check any reply they find.
- Rule 16 HEADLINES RULES RECHECK: check_headlines_rules.py (rules_check.json fails 0) and the Fable checker's rules_result.json on the CURRENT lines (common_b.rules_gate). Introductions: the previous day is 15 Oct (runs/2026-10-15 is in the repo; its introductions are in 3b), so G2 compares with 15 Oct; category openings are exempt from G2 in the script; the fun clip's "In today's fun corner" is NOT exempt: clash 3 is live today. Since 15 Oct the checker also asks of every clip "what does the last part add?" (check_headlines.md 3b, lesson 304). Nothing with a rules FAIL: clash 2.
- Rule 16 MODEL POLICY with STORY CHOICE and rules 25 and 27: picker Fable; writers Opus on normal effort (effort "medium" in the Agent call); checkers Fable at high; this rules-check helper, the main session and setup on Sonnet; never Haiku (lessons 277 and 294: check this chat's model at the start). New 15 Oct: MODEL TEST line (CLAUDE.md 152): before changing any model or effort read docs/model_test_2026-10-14/README.md (lesson 310; nothing changed yet). Evidence: the model of every Agent call; helper tokens per stage next to the earlier runs.
- Rule 16 STORY CHOICE: one Fable picker (briefs/pick_stories.md; pick_gate.py pack writes its prompt to cards_work/prompt_picker.txt), pick_gate.py gate PASS or a named override (the gate has no override file: selection.json is written only on PASS, lesson 267 item 3), Rafi approves the list before any wording. Evidence: gate_result.json, his message.
- Rule 16 BIGGER PICTURE MODEL and WEIGHT: card and clip from bigger_picture_bulletin.json (499 words in the Bulletin by paragraphs, 5 paragraphs after the heading line; rule 29 says 300 to 500: PASS, one word under the top): the cost of insuring against defaults by big technology borrowers at record highs, led by CoreWeave (five-year contract above 1,100 basis points; 1,000 implies a 64 percent chance of default), chip and memory makers down more than 1 trillion dollars this week (Business Insider), the Kospi down 7.6 percent, TSMC's record quarterly profit of about 24 billion dollars up 69 percent, investors weighing about 1.5 trillion dollars for Anthropic's listing against about 2 trillion; dated watch items: Wed 21 Oct Meta results; 27 to 29 Oct SK hynix (its filing names 28 Oct, Seoul time), the Fed decision Wed 28 Oct, Alphabet, Microsoft and Intel (Intel names Thu 29 Oct); CoreWeave default insurance day by day; Anthropic's answer to Mark Levine; unknowns marked (gross or net of Anthropic's 16.8 billion dollars). The text says "not financial advice"; card and clip voice and screen must carry it (check_wording.py, verify_headlines.py). Who writes card and clip: clash 4.
- Rule 16 SCRIPTS STAY AS THEY ARE: no script change during the run except for a rule Rafi gives during the run, after his yes to the exact edit list (CLAUDE.md line 162). Evidence: git diff of scripts/ empty at the end. Scripts changed since the 14 Oct check: pick_gate.py G7, G11b, G21 and check_headlines_rules.py B2d and B2e (14 Oct, with a 15 Oct change: B2d and B2e allow "From Washington" for politics, lesson 305); build_products.py (Part A, 2 lines: names for codes); the new not-found step is skill text only (Part A SKILL 11b). Rafi's yes to those exact edit lists is not in the delta (2e item 7).
- Rule 16 HEADLINES SHAPE: points to rule 22 and the model lines file. See rule 22.
- Rule 16 WHO WHAT WHY FIRST: who, what, why_for_people filled for every story and the fun clip (check_wording.py line 109 fails a missing one); failing lines go back to the same writer (rule 25); Rafi's words locked (rewrite_request.json "locked"); build_pack.py and review_list.py stop unless check_wording.py, check_headlines_rules.py and rules_result.json are newer than scripts_final.json.
- Rule 16 HEADLINES ORDER: Drive A3 for the six non-Politics clips; criticals first (rule 30; none today); Politics clip 1 (clash 5 sleeps: Politics has eligible stories C13-03 and C13-04, both read in full).
- Rule 16 HEADLINES INTROS AND FLOW: each introduction names its own topic; since 14 Oct a story clip opens with its own category (In finance, In security, In robotics, In tech, In the lab, In law or In the courts, In health, At work, In infrastructure, In politics; "Also in" for a second one; a score 10 opens "First, a critical ..."; wording_headlines.md line 27, B2d and B2e, lesson 296); a place fails, the one exception "From Washington" for politics (rule 32, lesson 305); the fun clip opens "In today's fun corner" (rule 32, Rafi 15 Oct; "Today's fun fact" only for a fact that is not a joke, lesson 292; clash 3); among non-Politics clips prefer AI affecting people over war; every clip generated except slots 1, 12 and 13. Clash 9 (the brief examples against the category rule).
- Rule 16 REAL TV SCREENS, PHOTOREALISTIC, FUN CLIP: each screen a photorealistic TV news scene of its story, no readable words, numbers, logos or real named faces; the Bigger Picture keeps its warning sign; fun clip facts only from its source entry. Evidence: fill PROMPT line 18; the Headlines checker's screen findings.
- Rule 16 NO OLD NEWS: cards and clips only from the report after step 9b (held ids are refused by G1; held.json is read at 0c.4). PASS by construction. No exception today (rule 23 was for 12 Oct only).
- Rule 16 CARD FILTER and the CARD_FILTER line (base_min 5, extra_min 7, target 14, 2 per category, market 3, company 3 cards and 2 clips; pick_pack.json filter agrees): order from Drive Cards Master 2.4 (11 categories); no score 10 (top 8: seven stories); Politics has two eligible stories (C13-03, C13-04, both 7); Research has two (C15-01 at 8, C04-01 at 7, plus reserve 6s); extras below 7 settled (2a item 1); the score used is the pool score or the writer's score (2b: 8 Bulletin stories differ, each 1 higher in the Bulletin); a robotics card shows a machine doing something (only C11-04 is flagged machine_action true; C11-01 Volvo and C11-02 Faraday are false). See clash 1 (sleeps).
- Rule 16 CARDS FROM THE BULLETIN: 39 Bulletin stories, 36 non-fun, 32 NEW and read in full and not a follow-up (3 follow-ups: C05-01, C06-01, C08-16; 1 headline only: C14-04), 20 within the category limits: Market 3 of 4, Security 2 of 3, Energy 2 of 5, Robotics 2 of 5, Models 2 of 3, Research 2 of 2, Ethics and law 1 of 1, Health 2 of 3, Society 2 of 4, Politics 2 of 2. Evidence: G4.
- Rule 16 NO UPDATE CARDS: none named (no update_allowed.json); the 3 Bulletin follow-ups (C05-01 Huang on working with Chinese AI firms, follow-up of 14 Oct; C06-01 investors weighing a lower Anthropic valuation, follow-up of 15 Oct; C08-16 Windows on Nvidia's RTX Spark laptops, follow-up of 9 Oct, added by Rafi's choice in Part A) and fun follow-up C16-01 (TV4 pushes a reality show, follow-up of 14 Oct) are not cards, clips or teaser items (G6). Lesson 295 (IMF, 14 Oct): a new report from the same organisation on the same topic within 7 days counts as an update. Rule 34 (16 Oct) lets a story that ran at 7 or more come back in the Bulletin when it is a meaningful update; it does not name cards: clash 11. The paper draft takes C16-01 as the fun card and C05-01 and C06-01 as teaser items: both faults for G6 (3a item 14).
- Rule 16 NO REPEATS IN 7 DAYS: decks of 9 to 12, 14 and 15 Oct present; 13 Oct is empty in pick_pack.json (lessons 281, 299 and 309: the 13 Oct run was never saved), so G17 cannot see 13 Oct. By my read of the last_7_days lines the gate or the 3-day table will meet, to judge: C07-03 and C07-02 (chip stocks and CoreWeave bonds) against the 15 Oct CoreWeave and finance lines; C08-03 (TSMC demand) against the 15 Oct TSMC profit line; C13-01 (FTC documents from OpenAI and Anthropic) against the 15 Oct states-sue-OpenAI and EU-questions lines; C05-01 (Huang) against the 15 Oct Huang security clip; C14-01 (Netflix job cuts) against 14 Oct Kroger (different); C11-01 (Volvo and Nvidia hands-free driving) against the 15 Oct Waymo clip (different). Evidence: gate_result.json G17 plus the section 3c table.
- Rule 16 THE REPO IS THE SOURCE OF TRUTH: a CLAUDE.md line beats a Drive line; differences belong in docs/DRIVE_DIFFS_FOR_CHATGPT.md (2d).
- Rule 16 PEOPLE WITH THEIR POSITION: as 8b item 6 (rule 32 NAMES NEED TITLES, simple titles; lesson 307).
- Rule 16 HEADLINES START WITH POLITICS: eligible Politics stories C13-03 (New York City's comptroller urges Anthropic to delay its listing) and C13-04 (Pentagon officials reportedly keep a report on a US strike on an Iranian school secret until after the midterms); C05-01 is a follow-up. The paper draft has clip 1 C13-04 and cards s1 and s2 both Politics (2 per category is allowed). A score 10 would go above Politics (rule 30; none today).
- Rule 16 VIRAL RULE: done in Part A (viral.json not read here; no re-run). Rule 34 (16 Oct) answers lesson 195 for the viral rule: a story that ran at 7 or more may come back when it is a meaningful update, judged story by story; the CLAUDE.md VIRAL RULE line (221) still says "ran earlier below 7": clash 11. Lesson 314: the sweep missed a same-day repeat by headline (States sue OpenAI, 48 outlets; yesterday's C13-01); a viral cluster is checked against the last day's pool by names, not by title.
- Rule 16 ONE TOPIC, ONE CARD: no gate test (lesson 161); today C01-01 (Meta's Muse Spark Open, a very large open-weight model for Apple Macs) and C06-02 (Meta and Apple worked together on it) are one event, and the paper draft takes both (s10 and s4): one card or a stated reason; C07-01 (default insurance at record highs), C07-02 (CoreWeave bonds sold off) and C07-03 (chip and memory stocks lose more than 1 trillion dollars) are three sides of the Bigger Picture story, and the draft takes C07-01 and C07-02: judge; every card pair checked before Rafi sees the deck.
- Rule 16 ROBOTICS: Bulletin 5 (C11-01 Volvo plans Tesla-style hands-free driving with Nvidia; C11-02 Faraday Future launches two low-priced humanoid robots at $2,490 and $299; C11-03 Ukraine plans a bigger AI-drone campaign; C11-04 Tesla's crash reports show a remote human drove in five robotaxi cases; C11-05 Tesla driver-assist on around a fatal crash), at the top of the 3 to 5 guideline; eligible 5 (machine_action true only for C11-04; false for the rest); the cards need 2 with one humanoid: the humanoid candidate is C11-02 (the entry says humanoid; a product launch needs a robotics_ruling, G13); the paper draft has C11-04 only; report-only robotics (6 stories) cannot be cards while the Bulletin has eligible robotics (G4b exception); Headlines 1 robotics clip (B2: say what the robot or vehicle does).
- Rule 16 ROBOT WAR LIMIT: Bulletin at most 2, Full Report at most 3 (Part A's count). The Bulletin has one robot war story, C11-03 (Ukraine's AI-guided drones): PASS; verify the report count at 0c.4. No limit on cards.
- Rule 16 BEFORE EVERY STAGE: this file is the read of step 0c.
- Rule 16 HEADLINES GENERATION: 8 steps, AIND_anchor_voice_sample_4s.wav, the unhurried tone. Evidence: fill CONFIG line; verify_headlines.py "steps 8" and "tone in N of N".
- Rule 16 APPROVED OPENING AND ENDING: assets/pack_base.json slots 1 and 13 "bypass" (checked); check_headlines_rules.py A2.
- Rule 16 QA GAPS: the built checks run, in rule 25's shape.
- Rule 17 BIGGER PICTURE CORNER: card head the market summation, body what happened and what to watch (4 lines, notice stays); clip 10 s (rule 22: 10 acceptable); never a vague restatement: today's text turns on default insurance at record highs for AI borrowers (CoreWeave), the more than 1 trillion dollar loss in chip and memory shares, TSMC's record profit and the lower Anthropic valuation; no process words (rule 32).
- Rule 18 FRESH CHAT: Part B continues in Part A's chat (rule 9; 2a item 9; lesson 277 Group 2 item 12 "Part B in a fresh chat" is open for Rafi); a compacted chat continues only with Rafi's yes.
- Rule 20: one question at a time; when he asks for the list, the list itself; rules only in his words; his exact complaint first; ORDER NEVER CHANGES (G7).
- Rule 21: lessons of this run into docs/V1_TASKS.md (step 8.4); a handoff is not a source; never touch the Drive EXPERIMENTS file.
- Rule 22 HEADLINES STRUCTURE: one sentence after the introduction, who did what and why (a company reason or a careful guess is a why; the end part only if it adds weight); aim 8 s, 10 acceptable, 12 the hard limit; the model lines file read by writer and checker (wording_headlines.md line 12, check_headlines.md line 3). Scripts test only the length; the one-sentence shape rests on the checker (check_wording.py counts no clip sentences): to verify at step 7 by counting sentences after the introduction in scripts_final.json.
- Rule 23 FUN CLIP: named for 12 Oct only (Apate); no CP- story is named for 16 Oct, so step 0b is skipped and headlines_fun is a pool fun story chosen under rule 29 FUN CLIP CHOICE. G4b applies to it (it must be in the Bulletin: C16-01, C16-02 or C16-03). The paper draft's C16-01 is a follow-up of 14 Oct and DISPUTED (3a item 11).
- Rule 24 CARDS IN GROUPS OF 10: step 8.1: 10 files a message in deck order, the contact sheet with the last group, the JSON alone.
- Rule 24 HEADLINES ITEMS MUST BE IN THE REPORTS: G4b (every clip id in the Bulletin and the report; only CP- ids are exempt); story clips come from Bulletin cards. No bite today: Politics has eligible Bulletin stories (clash 5 sleeps). Rafi's 15 Oct words (rule 31): "this rule is not a brick in stone. I can change it if needs. not you without asking me."
- Rule 24 FUN STORIES: funny, or fun to hear, see or experience, or mildly cynical and funny to think about, never sad; pick_stories.md follows (lines 7, 9-10, 40). Today's Bulletin fun stories: C16-01 (TV4 pushes a reality show to 2027; a follow-up of 14 Oct; DISPUTED), C16-02 (MIT researchers leave thirteen AI agents alone on a virtual island for thirty hours; PRELIMINARY), C16-03 (social media jokes that AI-lab staff should treat any romantic interest as a risk; REPORTED, names OpenAI). A fun item that is a fact, not a joke, is "Today's fun fact" (lesson 292). Rule 32: the opening is "In today's fun corner"; "leave it as accepted ... it is not the topic".
- Rule 24 HEADLINES LEVEL IS A CONSTANT: the 11 Oct lines (model lines file "The level": about 22 words, one sentence, one actor, one verb, one why).
- Rule 24 NO TIME PRESSURE ON THE TEST: DECIDED 13 Oct ("yes exactly!"): the length wording of rule 22 (aim 8 s, 10 for a long item, 12 the hard limit) and the model lines file stay as they are. Closed.
- Rule 24 "too complicated to explain in one sentence": such a story is not a clip. Test before choosing: two-party stories (C06-02 Meta and Apple, C13-01 the FTC with OpenAI and Anthropic, C13-04 the Pentagon report and the midterms) each need two facts in one sentence.
- Rule 24 "not funny but definitely fun": fun counts (FUN STORIES).
- Rule 25 ONE WRITER AND ONE CHECKER PER PRODUCT: checkers Agent model "fable", effort "high"; each checker reads its story pack once; the same writer fixes once; then Rafi sees what is left. Rule 27 replaces "at max" for the writers (next lines). make_wording_prompts.py still writes the old stranger, rules and rewrite prompts: not launched.
- Rule 26 VIDEO WORK AND FOOTAGE: footage and the video lessons 238 to 244 apply on the PC, not to the JSON; DRIVE UPLOAD by Rafi: no Drive agent at step 8; send only the final products (cards, contact sheet, JSON).
- Rule 27 WRITERS FASTER (new; Rafi, 12 Oct): the card writer and the Headlines writer are Opus on normal effort (effort "medium" in the Agent call, SKILL step 2) and read one pre-loaded story pack once; they save a full draft first, write everything in one pass, go through each item once against the hard rules, run the check scripts once and fix once; the checkers read the pack once. Part A writers unchanged. To verify at step 2: whether the Agent tool takes the effort value (lesson 266: the docs do not say). To measure: writer minutes and tokens (target 2 to 3 minutes; 12 Oct: 25.6 and 21.9) and whether the checkers fail more lines (12 Oct: Headlines 0 fails, cards 3 of 21).
- Rule 28 DAILY HEADLINES LISTEN (new; Rafi, 12 Oct, "I want it every day"): at step 7, before the review list, the spoken lines of every Headlines clip go into the chat as plain text in one message ("Clip one. ...", fun, teaser and Bigger Picture named, no file, no symbols, A I and U S as the clip says them); the Fable check of step 3 stays as well ("For now, we keep both"). To verify at step 7: the message exists and matches scripts_final.json word for word.
- Rule 29 FUN CLIP CHOICE (Rafi, 13 Oct): Claude gives Rafi the fun concept and he says if it is funny; the goal is that Claude later chooses alone. Today's concept comes with the step 1 list (candidates: C16-02 and C16-03, both NEW; C16-01 is a follow-up); G4b needs the fun clip in the Bulletin.
- Rule 29 MISTAKES NOT AGAIN (new; Rafi, 13 Oct): the card checker has the read aloud test (check 1b of check_cards.md); Claude always shows Rafi the real lines, cards or files, never a description (lesson 274). To verify at step 3 and 7: check_result.json has a 1b verdict per card; the step 7 message holds the lines themselves.
- Rule 29 BIGGER PICTURE IN THE BULLETIN (Rafi, 13 Oct): "300-500 words is fine for now", "stick to whats necessary". Today's Bulletin text is 499 words by paragraphs: inside the range (one word under 500). Part A's product, not a Part B gate.
- Rule 29 ARTICLE (new; Rafi, 13 Oct): "article" means any item, a Headlines line, a card or a full entry; ask which one only when it matters.
- Rule 29 LESSONS FOR THE REPO (new; Rafi, 13 Oct): the local chat ends its answers with LESSONS FOR THE REPO; Rafi passes the list to this chat, which writes each lesson into docs/V1_TASKS.md once (search first, lesson 273). Step 8.4 does the same for this run.
- Rule 29 TWO CHATS (new; Rafi, 12 Oct): this cloud chat runs Part B up to the JSON; the local chat on his PC does ComfyUI and the stitch. Nothing in Part B changes.
- Rule 30 CRITICALS ALWAYS ON TOP (Rafi, 14 Oct): a story rated 10 is the first card and the first Headlines clip, above Politics. Met by pick_gate.py G7, G11b and G21; a critical opens "First, a critical ...". Today: no story rated 10 (top 8, seven stories: pick pack and Bulletin), so nothing to move; the gate still runs. Lesson 290 is the record.
- Rule 31 (Rafi, 15 Oct; this line was not in the 15 Oct check: written after it, found in the delta's CLAUDE.md context) POLITICS CLIP AND THE 6s: "at least 2 items from 6" for Politics "and all categories"; the Politics clip was wanted ("the china news is great!"). Today Politics holds 3 stories at 8, 7, 7, so nothing is short; Ethics and law holds 1 (clash 10). A section whose 7-and-up stories are ALL headline only counts as empty (Rafi's yes, 15 Oct): today no section is in that case (C14-04 is headline only but sits at 6 in a Society section of 5; Politics C13-03 and C13-04 are read). RULES ARE HIS TO CHANGE: no rule is changed without asking him.
- Rule 32 USELESS TAIL (new; Rafi, 15 Oct): a hedge is one word (would, reportedly, may, says), never a clause; a speaker's own hedge is not a why; the writer cuts a last part that adds nothing and the checker asks of every clip "what does the last part add?" (briefs wording_headlines.md and check_headlines.md 3b; no script check, tested and rejected, lesson 304). To verify at step 3 and 7: no clause hedge, no restated hedge at the end of a clip.
- Rule 32 FROM WASHINGTON (new; Rafi, 15 Oct): the one place allowed as an opening, for politics only; B2d and B2e allow it (lesson 305). If a Politics clip is a US story, "From Washington" may stand; C13-04 is a US story (the Pentagon), C13-03 is New York City.
- Rule 32 NAMES NEED TITLES (new; Rafi, 15 Oct): every named person gets a simple title in every product so the reader knows why the words count: see 8b item 6 (lesson 307: no script check yet; the checkers and the final audit read for it).
- Rule 32 CUSTOMER PRODUCTS (new; Rafi, 15 Oct): "precise, elegant, good looking, designed well and easy to follow": no codes, rule numbers or process words on a card, a clip or a printed product. To verify at step 7: no "C13-03" style id, no "headline only", no "rule" on any card (the card renderer prints only text from cards_copy.json).
- Rule 32 SIMPLE ANSWERS (new; Rafi, 15 Oct): "simple english line, at most two lines if complicated to explain"; when he asks to repeat the questions, repeat the questions one line each, no summary. Applies to the step 1 and step 7 messages (touches clash 7).
- Rule 32 THE FUN CLIP (new; Rafi, 15 Oct): the opening "In today's fun corner"; the fun line follows the source only ("leave it as accepted ... it is not the topic"); see 1a Rule 24 and clash 3.
- Rule 33 SOCIAL POSTING (new; Rafi, 15 Oct): Postiz under study; not built; posting would start only after the Part B approval stop. Nothing in Part B changes (1e).
- Rule 34 (new; Rafi, 16 Oct, "keep them if they are meaningful updates"): a story that ran at 7 or more may come back in the Bulletin when it is a meaningful update (new facts), judged story by story; today C08-16 (Windows for the RTX Spark laptops, follow-up of 9 Oct) is the one such story and is in the Bulletin; skill step 1c and viral_sweep.py are not changed until his yes. For cards and clips NO UPDATE CARDS still blocks it (G6): clash 11.
- Rule 35 (new; Rafi, 16 Oct, "B"): a story with no readable copy: first a quick search for the same story at another outlet and related sources, one paragraph from what was read; a story still not found ends "Read the full article at <source>." (the old "Note: we could not open the original article ..." is not printed). Part A skill step 11b does it. Today the Bulletin carries 1 such line and the report 4; 0 old notes remain (grep of both JSON files). A headline-only story is still never a card or clip (G5).

### 1b. Drive rule and structure files (only lines that touch Part B; "settled" = a CLAUDE.md line or a newer ruling wins)
- The eight rule files of W/rules (six Drive rule files, the prompt file, the AIMD skill and STORAGE_STANDARD.txt): rules_delta.md section 4 says "no change" against runs/2026-10-15/rules; I did not run a diff of my own. The lines below were rechecked only where today's facts differ.
- Cards Master order block and 2.4: deck order Politics, Market, Security, Energy, Robotics, Models, Research, Ethics and law, Health, Society, Fun. Evidence: G7. The fixed slots are replaced by the CARD FILTER (settled).
- Cards Master filename rule: local cards_16-10-26_INN_VL1.png; _Claude-V1 on the names Rafi uploads (settled, rule 0 WHO MADE IT).
- Cards Master 1.1: one 1080x1920 PNG set plus one combined image (the contact sheet). Evidence: assemble_cards.py sizes line.
- Cards Master 1.3 and 3.5 DESK VIEW: the Bigger Picture card says AIND (settled, CLAUDE.md CREDIT).
- Cards Master 1.4 and 2.5: the "More in the full report" card holds report headlines with no story card; the reel teaser draws only from it. Evidence: G12, check_headlines_rules.py A5.
- Cards Master 2.1 to 2.3: cover first; criticals spend their slot (no score 10 today).
- Cards Master 2.6: aim 15 (settled: 14); robotics and fun normally required.
- Cards Master 2.7: at most 3 money cards. Evidence: G8 (4 eligible Bulletin Market stories for 3 slots: C06-02, C07-01, C07-02, C07-03; C06-01 is a follow-up).
- Cards Master 2.8: full report only (settled: from the Bulletin).
- Cards Master 2.9: robotics = a machine doing something (settled: humanoid funding also counts). Evidence: G13.
- Cards Master 2.11 and 2.12: no sales language, no link on cards; the closing text of 12 Sep (build_cards_copy.py CLOSING).
- Cards Master 2.14: reel order follows deck order. Evidence: G11, check A3.
- Cards Master 3.1 to 3.4: phrasing file governs; lead with the deed, not the money; unfamiliar companies titled (candidates today: Faraday Future, insitro, Venture Global, CoreWeave, METR, CERT-In, Workday, TSMC, the Pentagon story's outlets).
- Cards Master 3.6 and 3.7: approved text never cut for layout; Rafi approves at step 7.
- Cards Master 4 to 6: the renderer package (md5 598989503fa221cebe87c04bac903854) owns colours, fonts and the Instagram window; cover = approved cover with the new date (to make today with make_cover.py).
- Cards Master 7.1, 7.4, 7.7, 7.8: Drive account and saving: not live today (rule 26, settled).
- Cards Master 7.15 and 7.16: contact sheet first at step 7; every card its own PNG, never a zip; groups of 10 (rule 24, settled).
- Headlines Master order block, A3, A7: stories in deck order, then fun, teaser, Bigger Picture, ending (build_pack.py); criticals first (rule 30, G21).
- Headlines Master A1: twelve-slot template (settled: 13 slots).
- Headlines Master A2 and 15 Sep 5: stored intro bypassed; ending wording = pack_base slot 13 text; the option 4 clips of 3 Oct are used (settled).
- Headlines Master A3: seven card stories in deck order, normally robotics plus law, research or society (today's Bulletin gives law C13-01, society C14-01, C14-02, C14-03, robotics C11-01 to C11-05, research C15-01, C04-01).
- Headlines Master A4: slot 9 is the deck's fun item (settled: rule 23 was 12 Oct only; today the fun item follows rules 24 and 29).
- Headlines Master A5, A6, A8: teaser only from the teaser card; Bigger Picture in slot 11 opening "And for the bigger picture"; about 90 s of content.
- Headlines Master B1 and B1a: aim 8 s, 12 s maximum (same as rule 22); two decimals, no rounding (settled: round up, rule 16).
- Headlines Master B2: Cards Section 3 words; the robotics clip says what the robot or vehicle does (C11-04: Tesla's own crash reports show a remote human operator was driving in five robotaxi cases; C11-02: Faraday Future's humanoid robots, a launch).
- Headlines Master B2a: every story and fun clip opens with an introduction; teaser "Also in the full report." (full stop); Bigger Picture "And for the bigger picture". Evidence: check B2a.
- Headlines Master B3: numbers as words, no digits. Evidence: check B3 and check_wording.py.
- Headlines Master B2 (prompt) and the prompt file: text-free screen, "nothing else changes" (settled: REAL TV SCREENS and the tone line).
- Headlines Master C: references 1 hands-on-table and 2 fists (template md5 235ede6a86c66fc1d38d7614f079d548, changed 14 Oct, unchanged in the delta; fill_headlines.py line 135 asserts the order); every visible field overwritten; titles start "FRI 16 OCT 2026"; slot table and stale word scan; mirrors written; JSON to Rafi as a file, never zipped; six steps (settled: 8).
- Headlines Master G1.1 and 15 Sep 1: cues only where spoken. The Drive 15 Sep 1 line says Anthropic = "an-thropic"; the repo says "anthro-pic" (lesson D3, 14 Oct): settled, CLAUDE.md and the repo over Drive (2a item 34, 2d). N-vidia if Nvidia is spoken (C05-01, C08-02, C08-16, C11-01), anthro-pic if Anthropic is (C06-01, C12-01, C13-01, C13-03); 15 Sep 2: "Google DeepMind" if spoken.
- Headlines Master G1.2: a two to three word tag for a company under 100 billion dollars (CoreWeave, Faraday Future, insitro, Venture Global, METR, Workday; Palantir if unsure).
- Headlines Master G1.3: one idea per sentence (settled: rule 22). G1.4: hedges kept, outlet never spoken (check G1.4).
- Headlines Master G2: introductions rotate (clash 3).
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
- Full Report and Bulletin 5.3 and 11.4 (the headline-only note): replaced for customers by rule 35 (16 Oct): "Read the full article at <source>." (Bulletin 1, report 4, no old note; see 1a Rule 35); the About paragraph reads "For the rest, each story links to its source" (no process words).
- Full Report and Bulletin 6.1 and 6.2 (publisher named, direct link): 0 Google News links in the 39 Bulletin stories (bulletin_pdf.json, 25 different hosts by url, counted); the report: verify at 0c.4.
- STORAGE: its label lines say _Claude-V1 (same as rule 0); Part B saves nothing to Drive today (rule 26).

### 1c. Part B skill steps (process rules of this run)
- Step 0 setup: sync_repo.sh at resume (the SessionStart hook runs it by itself), renderer zip and cover base (Drive, read only), Pillow and fontTools from the hook. Step 0.1 rules_diff replaced by rules_delta.py (delta section 4: the Drive rule files are unchanged since 15 Oct). The cover is not built yet. Lesson 294: check this chat's model before anything runs (never Haiku).
- Step 0b: not needed today: no Rafi-named fun story for 16 Oct (rule 23 was 12 Oct only); the fun clip follows rule 29.
- Step 0c: this file (incremental, launched with the picker; the main session reads the one line and CLASHES only, never the lessons file whole); the 0c.4 PASS/FAIL table per section before step 7.
- Step 1: Fable picker (prompt written by pick_gate.py pack to cards_work/prompt_picker.txt, 07:22), pick_gate.py gate PASS or a named override (no override file, lesson 267), Rafi approves the list before wording; the LEFT OUT list and the fun concept (rule 29) go with it; clashes 3, 10 and 11 are put to him there (one at a time, rule 20; in two short lines, rule 32).
- Step 2: make_wording_prompts.py with --prev-pack /home/user/ai-news-desk/runs/2026-10-15/headlines_work/headlines_15-10-26_pack.json --prev-cards /home/user/ai-news-desk/runs/2026-10-15/cards_copy.json (2b; to confirm the files exist); it also writes both story packs; two Opus writers (effort medium) in one message; draft first; rerun it if selection.json changes; a look after 10 minutes. The writer briefs carry rule 32 (USELESS TAIL) since 15 Oct.
- Step 3: two Fable checkers (high) read their story pack once; the Headlines checker adds 3b "what does the last part add?"; one fix by the same writers; one confirm of the changed items; what stays open goes to Rafi marked (clash 2).
- Step 4: merged into step 3 (12 Oct).
- Step 5: cover, cards copy, render into a new cards_runN, assemble (stops on a refused card).
- Step 6: build_pack.py (gate), fill_headlines.py (refuses to overwrite), verify_headlines.py.
- Step 6b FINAL AUDIT (new; lesson 297, Rafi 14 Oct: "make sure these mistakes, or any lesson we have learned, do not repeat"): scripts/final_audit.py --workdir $W before every send of cards, JSON or lines; --mark-sent right after; it prints every line and the lines changed since the last send; nothing goes with a FAIL; the main chat reads the printed lines against his rules (category openings, exact figures, a position for every person, A I and anthro-pic spellings); a line Rafi has seen changes only when he asked; when he asks for a file, send it at once and fix the rest.
- Step 7: DAILY LISTEN first (rule 28: the spoken lines of every Headlines clip as plain text in one chat message), then review_list.py (gate), save_state.py, the sheet and the list to Rafi, STOP.
- Step 8: after approval: groups of 10 in chat, the JSON alone, the voice sample line; delivery_manifest.py --part B --copy-to $W/for_rafi gives the _Claude-V1 names (no Drive agent, rule 26); save_state.py (pulls before it pushes); short report; lessons into docs/V1_TASKS.md (search first, lesson 273). final_audit.py --mark-sent right after each send (6b).

### 1d. Lessons that touch Part B today
- P1-3 Fun Side 5 to 10, top 3 in the Bulletin: 9 fun stories in the pick pack, 3 in the Bulletin. PASS (report count at 0c.4).
- P1-4 cutoffs stated: Bulletin 39 (pool score 7 and up, Health, Society and Robotics from 6, plus the top 3 Fun; purpose line in words); the report's cutoff and count (111) are in Part A's delivery message. 39 is inside the 30 to 50 guideline.
- P1-5 everything final to Drive, else to Rafi: rule 26 (Rafi uploads) for now.
- P1-6 story cards 14 to 15, company 2 clips and 3 cards, money cards 3, a headline-only story never a card: G2, G9, G10, G8, G5 (C14-04 is headline only; count: clash 1 sleeps).
- P1-7 news part about 90 s, round up: check_wording.py total, fill table (to verify at step 6).
- P1-8 hologram border: the fill PROMPT keeps the blue border line; the opening is stored.
- P1-9 only the spoken words when he asks for the stories in the JSON: review_list.py.
- P1-10 one file at a time: replaced by groups of 10 per message (rule 24); never a zip stands.
- P1-11 one home per rule: section 2 lists the double homes.
- P1-16 check the approved opening first: option 4 stored, slot 1 bypass.
- P1-17 never build before Rafi's yes: no wording before the list approval, nothing sent before the step 7 approval.
- P1-19 stop at a compaction: rule 18.
- P1-20 match his numbered answers against the original list: at steps 1 and 7 and on the clash answers.
- P1-21 never drop a category silently: every category has an eligible Bulletin story (Law has one); a skip needs left_out_notes, a reserve card needs "exception": true with a reason.
- P1-22 no old JSON in a package; no unapproved screen wording: fill refuses to overwrite; screens go to Rafi in the review list.
- P1-27 uploads verified by size: no Claude upload today (rule 26).
- P1-29 meaning check before any JSON leaves: gate before step 7; no JSON before approval.
- P1-31 compute weekdays: 15 Oct Thursday, 16 Oct Friday, 21 Oct Wednesday, 27 Oct Tuesday, 28 Oct Wednesday, 29 Oct Thursday (computed with python; the Bigger Picture text says Wed 21 Oct, 28 Oct and 29 Oct: they match).
- P1-32 read the governing file before quoting it: done in this file.
- P1-33 save cloud-only files: save_state.py before the step 7 wait and after delivery.
- P1-34 approved opening: the option 4 clips of 3 Oct (pack_base both bypass).
- P1-35 company limits: G9, G10, C16.
- L1 plain English gate: script check plus the checker's stranger test; card sentences at most 15 words (wording_cards.md line 9; not scripted, 2b); headline = the deed first.
- Port-3 company limits: CARD_FILTER line, G9, G10.
- Port-4 13-slot template, Bigger Picture clip 11, stored ending slot 13: build_pack.py.
- Port-5 hologram border kept; REAL TV SCREENS replaced the text-free symbol.
- Port-6 round up to the half second: fill_headlines.py.
- Port-7 the Bigger Picture at three lengths: clash 4.
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
- 24 and 46 credit the first reporter, "X reports, citing Y": check 3 of check_cards.md, check 4 of check_headlines.md; the SOURCE line copies the entry's source (build_cards_copy.py line 37): patch cards_copy.json by hand if a relay is named (lesson 267 item 4).
- 25 card sentences over 15 words: not scripted (2b); count at step 7.
- 29 follow-ups never a card; follow-ups in the teaser fail G6: today 3 Bulletin follow-ups plus fun C16-01 (3a item 14); the paper draft's teaser holds C05-01 and C06-01 (both follow-ups).
- 30 Drive rules change between runs: rules_delta.md section 4: no change since 15 Oct.
- 31 reader levels in the phrasing file only (cards 6, Headlines 5).
- 34 blocked sources: card credit to the first reporter, not the relay; check every SOURCE line at step 7 (lesson 267 item 4).
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
- 50 a reply names the earlier story: no pool-flagged reply today; read C13-03 and C05-01 (1a Rule 16 REPLY STORIES).
- 56 Market labels about 10 characters: the Market category name is long (build_cards_copy.py warns over 46 characters).
- 59 the one lessons list: step 8.4.
- 60 intros rotate, company tags: check G2 and the checker's G1.2 (clash 3).
- 61 hard gate on the current lines: common_b.rules_gate in build_pack.py and review_list.py.
- 62 token cost: report helper tokens per stage.
- 63 stored opening and ending: pack_base both bypass.
- 64 voice file .wav, teaser full stop, Kawa saki cue: fill AUDIO, check B2a, cues.
- 66 old news in cards: cards only after step 9b plus the 7-day check.
- 67 "no company twice in a row" (Rafi to confirm; not in CLAUDE.md): note only (OpenAI is in 4 and Anthropic in 3 eligible stories).
- 68 and 80 one event in several entries: C01-01 and C06-02 (Meta's Muse Spark Open), C07-01, C07-02 and C07-03 (AI borrowers' stress).
- 71 parallel sessions: fetch before every push.
- 72, 73, 235 Headlines shape: rule 22 replaced the 5 Oct checks (word cap, comma limit, company-only why removed); the side-clause test stays (check_wording.py line 70).
- 74 one truth for writing rules: the phrasing file, with rule 22's override named in the briefs.
- 75 simple, not childish: check 1 and 2 of check_headlines.md.
- 76 the Agent tool sets a model, not an effort: to verify at step 2 (rule 25).
- 77, 101 and 279 long jobs through run_in_background, never a shell "&" or nohup; P1-18 added: find a process with ps -eo pid,args | grep "[x]name", never pgrep -f (it matched itself and killed the shell).
- 83, 98, 145, 163, 216, 246 stale clone and a moving branch: sync_repo.sh moves forward only and runs from the SessionStart hook (Rafi's yes, 13 Oct); a chat that started on the old 6 Oct copy has no hook yet; fetch before each push (save_state.py now pulls first).
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
- 107 and 221 which score counts: the pool score (Rafi's ruling); pick_gate.py reads the writer's score (2b): 8 of 39 Bulletin stories differ today (each 1 higher in the Bulletin: C12-02 and C08-03 6 against 7, C14-01 6 against 7, C11-04, C11-05, C14-04 and C14-06 5 against 6, fun C16-01 4 against 5). Lesson 316 may explain part of it (a headline-only story is lowered by 1 and restored when text is found).
- 108 the automatic repeat match is a list to judge: G17 hits judged in 3c (expected: C07-02, C07-03, C08-03, C13-01, C05-01).
- 111 the markets quarter cap does not bind the Bigger Picture corner: rule 17.
- 114 change only what was asked; 115 show first, then act; 116 count the rounds per product; 117 check a figure before passing it on.
- 118, 119, 179, 190 customer text: 0c.4 recheck only (1 headline-only Bulletin story today, 4 in the report; each ends "Read the full article at <source>", rule 35); no fluency rewrite.
- 121 compare old and new facts of every fixed item: the checker's confirm round against the writer's first file.
- 122 the contact sheet by display render, files by attach.
- 123 Part B in a new chat: 2a item 9.
- 124 the restart copy is text only; 125 commit and push after every change.
- 126, 173, 208, 257 commits carry no model name, only the Claude-Session line.
- 127 estimate an agent's cost before running it; 128 answer first, act after he asks.
- 129 scripts unchanged during the run (rule 16 line 160 exception only with his yes).
- 131 step 0c before any choosing script: replaced for this run by the incremental design (lessons 262 and 272b, Rafi's yes of 13 Oct): the check runs with the picker and the picker does not wait; selection_draft.json and pick_pack.json (07:22) are paper input, nothing is chosen (2a item 25).
- 134 and 135 robotics counts (Bulletin 3 to 5, cards 2 with one humanoid, Headlines 1, one extra allowed): Bulletin 5; cards C11-02 (humanoid; needs a robotics_ruling, machine_action false) and C11-04; one robotics clip.
- 136 one Bulletin file: products/bulletin_pdf.json (39 stories = the delivered Bulletin; bulletin_pdf_old.json is the pre-edit copy). PASS.
- 137 and 158 the freshness flag does not know earlier decks (lesson 295): judge the G17 hits and the 3c table by name and topic.
- 138 a picker note is not a source: writers use entries and facts only.
- 139 the robotics clip says what the machine does: C11-04's entry does (a remote human drove five robotaxis); C11-02 is a product launch, so the clip says what the robots are and cost.
- 140 and 199 realistic screens: fill PROMPT updated (lesson 209); one stale brief line (2b).
- 141 screens static and wordless.
- 142 list every clash once: settled by rule 20 (2a item 10).
- 144 and 258 helper tokens per stage: report Part B's.
- 147 held stories are never cited: G1, G16.
- 148, 256 and 289 the Bigger Picture author (Fable max) and the second reader (Opus, one pass) ran in Part A (W/_reader_backup exists; the reader log is not read here); unconfirmed dates stay marked "not confirmed" in card and clip (SK hynix 27 Oct, Samsung 29 Oct, Nvidia and CoreWeave mid-November, Anthropic's listing in November).
- 150 Bulletin cover in words: PASS now: the purpose line reads "Health from 6, Society and education from 6, Robotics from 6" (names, not codes; lesson 306).
- 154 no empty Bulletin section: PASS (all 11 hold stories; Ethics and law 1: clash 10).
- 156 lock the report list: Part B never rebuilds the products.
- 161 two cards on one topic: Meta's Muse Spark Open (C01-01 and C06-02) and the three AI-borrower stories (C07-01, C07-02, C07-03); manual check.
- 162 Rafi's list changes meet the gate: gate_overrides.json names each overridden line and his words (clash 1).
- 171 and 174 viral stories by reach: done in Part A (viral.json not read here).
- 175 rule text only in his words: section 2 fixes are marked mine.
- 177 and 178 the approved order for every product: G7 for the deck.
- 180 the six clashes of 10 Oct: four settled (2a items 1 to 5), one not live (2c), one carried (clash 2).
- 182 a viral floor only after checking earlier editions: Part A's step, not re-run here (viral.json not read).
- 183 link a follow-up by url and title, not a per-day id: when a card names an earlier story.
- 186 a CLAUDE.md copy loaded at session start goes stale: CLAUDE.md is 335 lines today (318 on 15 Oct); the copy in this helper's context ends at rule 35; helpers read the disk file.
- 188 thin fun search: Bulletin fun stories score 5, 4 and 4 in the Bulletin (C16-01 a disputed follow-up, C16-02 preliminary, C16-03 reported); rule 24 widens the fun test.
- 191 and 192 search before saying a robot story is missing: the humanoid story is C11-02 (Faraday Future); report-only robotics cannot be cards while the Bulletin has eligible robotics.
- 193 robot war counted: Bulletin at most 2 (1: C11-03), report at most 3. PASS.
- 194 never ask what a rule decides; send the list itself.
- 195 may a follow-up of a printed story return in the Bulletin: ANSWERED for the viral rule by rule 34 (16 Oct): yes when it is a meaningful update, story by story; cards stay blocked by NO UPDATE CARDS (clash 11). Today's Bulletin carries 3 follow-ups plus fun C16-01.
- 196 the card list follows Rafi's order over the picker.
- 197 inside a full category compare appeal to a stranger, not only the score: Energy has 5 eligible for 2 slots, Robotics 5 for 2, Society 4 for 2, Market 4 for 3, Security 3 for 2, Models 3 for 2, Health 3 for 2.
- 201 the check chain: one round (rule 25).
- 202 label at most 14 characters, no money figure: pick_stories.md line 25 (2b on the 15 lines).
- 203 review_list.py intro photorealistic. PASS.
- 204 the Drive agent must try binaries: not live (rule 26).
- 206 and 237 the between-run fixes present: step 0b used when needed, phrasing override in all writer and checker briefs, not-financial-advice checks (check_wording.py, verify_headlines.py), G4b, groups of 10 (step 8.1); "funny at once" is gone from CLAUDE.md and from pick_stories.md.
- 207 open for Rafi from 10 Oct: item 2 (follow-ups in the Bulletin) answered for the viral rule by rule 34; item 3 (customer text in CLAUDE.md) answered by rule 32; item 5 partly fixed (2b); item 6 settled by rule 24; item 7 answered by rule 29 (today 499 words); item 8 not live (rule 26); item 9 open.
- 210, 211 to 215, 231 the second run (ChatGPT V1) in the same Drive date folder and the labels: the names Rafi uploads carry _Claude-V1.
- 223, 250, 251 Bulletin sections without a 7: Health, Society and Robotics (floor 6) hold stories; all sections hold stories. PASS for "never empty".
- 226 estimates from timed steps; 227 counts from the file list; 229 clock times from date -u; 230 never rm.
- 228 and 257 save_state.py: FIXED 13 Oct (copies every text file at the top of W under 2 MB and the run handoff; pulls, merge never rebase, before it pushes; a conflict stops it with nothing pushed); check the commit message link by hand.
- 233 "files" means the final products: step 8 sends the PNGs, the contact sheet and the JSON only.
- 234 Part B setup faults: (a) make_cover.py --pkg is the parent folder; (b) aind_cards.py runs without -I; (c) the picker prompt is now written by pick_gate.py pack (fixed 13 Oct); (d) the score alignment (2b, still open); (e) touches that Rafi's precedence lines settle are decided and named, not asked.
- 236 fun clip: REPLACED 13 Oct (rule 29 FUN CLIP CHOICE): Claude gives Rafi the concept and he says if it is funny; no list of three finished lines.
- 238 no lessons, rules or script copies outside the repo; downloads need Rafi's OK: none in Part B.
- 241 _Claude-V1 names; build_pack.py writes each slot's source (the fun clip's outlet from its entry); teaser and Bigger Picture credited AI News Desk.
- 244 the 11 Oct Headlines are the reference look: the level constant (rule 24).
- 245 social text (hook and hashtags): only when he asks (D13).
- 247 rule 26 against the skill: Part B step 8.2 fixed on 13 Oct (copy-to; the old Drive text is kept for later).
- 255 credit lines of the form "X, citing Y": check every SOURCE line at step 7 (C05-01 and C07-02 name BigGo Finance as a relay; lesson 312).
- 259 France 24: no France 24 link in today's Bulletin (0 hits in bulletin_pdf.json); the report: verify at 0c.4.
- D1 do only the step he names; a one-sentence report, then wait.
- D2 Headlines in everyday words; cut filler.
- D3 spoken names "N-vidia", "anthro-pic" (14 Oct), "Kawa saki" (one gap) only where spoken: check 15Sep1; the Drive 15 Sep line still says an-thropic (2a item 34).
- D4 no colon after "Also in the full report": check B2a.
- D5 8 steps, the 4 s wav, fixed seed: fill asserts.
- D7, D36, D47 teaser and Bigger Picture credited AI News Desk: build_pack.py (fixed 12 Oct).
- D8 and D23 openings and endings are options; option 4 is used (bypass).
- D12 one short sentence; D13 only what he asks; D14 if it cannot be done perfectly, say so and stop; D15 one manual step per message; D18 look in the files before asking; D19 when a script blocks, follow it, never override it; D20 never delete, ask before any outward action.
- D25 Headlines only from that day's cards: replaced in part by rule 24 ("not necessarily in the cards"); rule 23 (Apate) was for 12 Oct only; story clips still come from the cards (G11).
- D27 the seed never changes (1060749754396562); D28 a spelling fix changes only the spelling.
- 262 and 272b the rules check is incremental: this file is updated from runs/2026-10-15/rules_check.md by rules_delta.md, launched with the picker; the main session reads the helper's one line and CLASHES only, never the lessons file whole.
- 267 Part B findings of 12 Oct (new): (1) the card renderer traces every card to an excerpt of the day's Full Report (REPORT_TRACE), so a report-only exception card passes but a story outside the report cannot be a card; (2) the 8 story clip template and 13 to 15 cards need repo edits that wait for Rafi's yes (runs/2026-10-12/script_edits_for_rafi.txt): today stays at 7 clips and 14 to 15 cards, scripts unchanged; (3) the gate has no override (selection.json only on PASS); (4) the card SOURCE strip copies the entry's source: patch cards_copy.json by hand if a relay is named; (5) the assembler stops when cover I01 is missing in a renamed folder.
- 270 helper time limit (new): proposed, NOT in force (awaiting Rafi, 272c); SKILL step 2 only asks for a look after 10 minutes. No wall-clock limit is applied to the Part B helpers.
- 271 the card post text has no home (new): written only when Rafi asks (D13, 245); open for Rafi: daily product or not, who writes it, where it is saved.
- 272 open items list (new): awaiting Rafi's yes: (a) repo edits for 8 clips and 13 to 15 cards, (c) the helper time limit, (d) the later token saving review of the Fable Headlines check; (b) the standing rules check is built (this file). To measure today: writer minutes and tokens under rule 27 and whether the checkers fail more lines. Later: real footage in the daily stitch, the automated Drive upload (rule 26), a rafi_overrides file for the gate.
- 273 two credits, one lesson per topic, search before adding (new): cards carry the news credit only (the footage credit is separate); lessons are added to the existing lesson as "ADDED <date>"; grep V1_TASKS.md before writing one (step 8.4).
- 274 mistakes not again (new): show Rafi the real lines, cards or files, never a description; a passed script check is not a read (check 1b); no padded estimates; "article" means any item (rule 29).
- 276 and 238(4) (new): DRIVE_DIFFS_FOR_CHATGPT.md is out of date (not Part B's job today; 2d); lesson 238(4) "one plain recommendation" against rule 1: clash 7.
- 277 chain audit (new): Group 1 is applied (incremental check, medium effort writers, story packs, lean main chat); Group 2 is open for Rafi one by one, and these items touch Part B and are NOT applied: (7) the 12 Oct script edits for 8 clips and 13 to 15 cards, (11) the main chat on Sonnet, (12) Part B in a fresh chat started by itself, (13) one approval stop in Part B, (14) a tighter repeat match.
- 280 never run git, not even git status, in any helper prompt (new): the Part B briefs say "never run git" (2b: add "not even git status" between runs); the picker brief and this task say it.
- 281, 299 and 309 the 13 Oct edition is missing from the repo and its pool is nowhere (lessons 281 and 299); lesson 309 (15 Oct): the 13 Oct run was never saved because that chat waits on a Rafi answer and git is blocked there; Rafi must say yes in that chat. pick_pack.json last_7_days for 13 Oct is empty, G17 covers 6 of 7 days (9, 10, 11, 12, 14 and 15 Oct). Open for Rafi (3a item 13; 2e item 1).
- 286 viral rule and follow-ups: last used for C01-01 on 14 Oct; today C08-16 (Windows on RTX Spark laptops, follow-up of 9 Oct) is the one returning story (rule 34; clash 11 sleeps for cards).
- 288 backups never next to the files the build reads (new): no `_old` copy goes into report_entries or facts (W/old_edits is the place); `_old` names in cards_work and headlines_work are not read by the scripts.
- 290 critical story move (14 Oct): a critical story leads the deck and the Headlines above Politics (rule 30, G7, G11b, G21); no critical today. The card renderer redraws all cards, never a subset.
- 291 the teaser is ONE card with 3 to 4 lines; the 19 cards are cover, 14 stories, fun, teaser, Bigger Picture, closing; show the real contact sheet, not a count.
- 292 a fun item that is a fact, not a joke, is called "Today's fun fact" (Rafi, 14 Oct); rule 32 sets "In today's fun corner" for the fun clip; today's three fun stories are jokes or reports of jokes.
- 293 a checker's text is not final: the writer checks each fix against the rules (cards 15 words, opening 5 words B2a); the card credit comes from the entry's source field (32 characters).

## 2. CLASHES (two rules that demand opposite things today; nothing chosen, nothing applied): 11 (2 new today: 10 and 11; 1 to 9 carried from 15 Oct; 3, 7 and 9 sharper or narrower; 1, 5, 6 and 11 sleep today)

1. The count of 14 against the Bulletin source and the limits (carried; SLEEPS today).
   A: CLAUDE.md lines 202-203 (CARDS FROM THE BULLETIN: "the target is 14 story cards"), line 209 ("Aim: 14 story cards"), line 54 (8b item 4), pick_gate.py G2 (14 or 15, no override file; script line numbers of 15 Oct).
   B: CLAUDE.md line 88 (rule 14: counts are guidelines, adjust to the day's pool, state the number), line 224 (max_per_category=2), briefs/pick_stories.md line 23 ("up to 14 ... never add a 14th card that breaks a limit").
   Clash: the picker brief allows fewer than 14, the gate accepts only 14 or 15, and the gate has no override (lesson 267 item 3), so a smaller deck cannot pass. Not live today: the Bulletin gives 20 cards within the limits.
   Fix A: pick_gate.py G2 accepts the count the picker states when the Bulletin gives fewer within the limits (script change between runs, after Rafi's yes). Fix B: strike "up to" in pick_stories.md line 23. (wording mine, not yours)
   Recommendation: Fix A, when it next matters.

2. Nothing with a FAIL against one check round (carried; live).
   A: CLAUDE.md lines 145-147 (HEADLINES RULES RECHECK: "Nothing goes to him with a rules FAIL"); Part B SKILL.md step 0c.4 (line 77: "nothing is shown or delivered with an open FAIL"), step 8.5.
   B: CLAUDE.md line 57 (8b item 7: one check round and one rewrite round, then show Rafi what is left); SKILL.md step 3 (what is still open goes to Rafi in step 7, marked); rule 25 ("then Rafi sees everything", line 298) and rule 27 ("fixes once", line 304).
   Clash: a checker flag still open after the one fix round either blocks step 7 or goes to Rafi marked. Since 14 Oct common_b.py rules_gate blocks build_pack.py and review_list.py while rules_result.json holds any pass:false, so for the Headlines the script already chose the blocking side.
   Fix A: add to 8b item 7: "A script FAIL (check_wording.py, check_headlines_rules.py, the gate) never reaches Rafi; a checker's flag still open after the one fix round goes to him marked." Fix B (lesson 201's text): "A fact error or rules fail found by the later checks always gets one more fix round before Rafi sees it." (wording mine, not yours)
   Recommendation: Fix A.

3. Rafi's introduction list and the fun opening against rotation (carried; SHARPER today: live for the fun clip).
   A: CLAUDE.md lines 174-180 (HEADLINES INTROS AND FLOW: "In finance", "Also in finance", "In security", "And finally, something lighter" ...; line 179 "The intros Rafi dictates win over rule G2") and rule 32 THE FUN CLIP (line 331: the opening "In today's fun corner", Rafi 15 Oct).
   B: CLAUDE.md line 147 (never the previous day's wording, G2); Headlines Master G2; check_headlines_rules.py G2 (FAIL on any intro of the previous day, except the category openings).
   Clash: yesterday's fun clip opened "In today's fun corner" (15 Oct). Rafi dictated that opening, so line 179 says it wins over G2, but it is a non-category opening, so the script still fails it today; it is not written whether the opening is a standing line or for 15 Oct only.
   Fix A: add to rule 32 THE FUN CLIP: "In today's fun corner" is the standing opening of the fun clip and may repeat every day; check_headlines_rules.py G2 skips it (script change between runs, after his yes). Fix B: add: "The opening of 15 Oct was for that day; the fun clip rotates its introduction like any other." (wording mine, not yours)
   Recommendation: ask Rafi which one he means; Fix A if he wants it every day.

4. Who writes the Bigger Picture card and clip (carried; live).
   A: CLAUDE.md line 160 (BIGGER PICTURE MODEL: one agent writes all three lengths; the main session never writes it), line 211 (BIGGER PICTURE WEIGHT: Fable writes it, all three lengths), rule 17 (line 250: the card is one of the three lengths).
   B: CLAUDE.md lines 298-299 (rule 25: one Opus writer per product writes the card and Headlines wording; rule 27 keeps Opus); briefs/wording_cards.md line 11 and wording_headlines.md line 9 (the Opus writers write the Bigger Picture card and clip).
   Clash: Part A wrote bigger_picture.json and bigger_picture_bulletin.json today but no bigger_picture_card.json, so the card and clip come from the Part B writers; rule 25 does not name BIGGER PICTURE MODEL.
   Fix A: add to rule 25: "This covers the Bigger Picture card and clip: the Part B writers write them from bigger_picture_bulletin.json only, and the checkers check them against it." Fix B: add to BIGGER PICTURE MODEL: "The Part A author also writes bigger_picture_card.json (card head, body and clip line); Part B copies it." (wording mine, not yours)
   Recommendation: Fix A for today (no extra agent; the author's own Bulletin text is the only source).

5. The Politics card and Headlines clip 1 against the gate (carried; SLEEPS today: Politics has two eligible read stories, C13-03 and C13-04, both in the Bulletin; the clash returns on a day with none).
   A: CLAUDE.md line 218 (HEADLINES START WITH POLITICS), line 196 (CARD FILTER: every category keeps its best story at score 5 or more), briefs/pick_stories.md lines 8-9; pick_gate.py G18 and G11b.
   B: CLAUDE.md line 291 (rule 24: "items in headlines must appear in the pool, and bulletin and report"; rule 31: "this rule is not a brick in stone ... not you without asking me"), line 202 (CARDS FROM THE BULLETIN); pick_gate.py G4b and G11.
   Clash (when it is live): with no eligible Bulletin Politics story, G18 demands a Politics card, G11b makes it clip 1, G4b refuses a clip that is not in the Bulletin: every path fails one line.
   Fix A: add to rule 24: "A Politics card taken from the report because the Bulletin has no new Politics story, and its clip 1, need not be in the Bulletin (Rafi, <date>)". Fix B: "When the only Politics card is a report-only exception it is a card but not a clip; clip 1 is the first story clip in deck order." (wording mine, not yours)
   Recommendation: Fix A, when it next matters (his words of 15 Oct already say the rule is his to change).

6. A story labelled NEW that follows an earlier card or clip (carried; SLEEPS today: the follow-ups are labelled FOLLOW-UP in the pool).
   A: CLAUDE.md lines 204-207 (NO UPDATE CARDS; NO REPEATS IN 7 DAYS "comes back, as a repeat or as an update"); line 221 (VIRAL RULE: only a story that ran earlier BELOW 7 may run once more).
   B: Part A SKILL.md lines 200-201 (step 9b: "A follow-up with new facts stays in the report; whether it can be a card is decided in Part B ... (a meaningful update can)"), Part B SKILL.md line 89, and the pool's freshness label.
   Clash: the 14 Oct case (C01-01 labelled NEW after a card on 9 Oct) and lesson 295 (IMF) show the label and the repeat match can miss an update; G6 passes what says NEW. Today the pool labels the returning stories (C05-01, C06-01, C08-16 and fun C16-01 as FOLLOW-UP).
   Fix A: Rafi names the story in cards_work/update_allowed.json. Fix B: it is no card, clip or teaser item; it stays in the report. Fix C (skill text): change step 9b to "A follow-up with new facts stays in the report; it is a card only when Rafi names it (NO UPDATE CARDS)". (wording mine, not yours)
   Recommendation: Fix C (skill text) when it next matters.

7. One plain recommendation against all viable paths and "at most two lines" (carried; SHARPER since rule 32 SIMPLE ANSWERS).
   A: docs/V1_TASKS.md lesson 238(4) ("give one plain recommendation"; the lesson itself says it clashes); CLAUDE.md line 330 (rule 32 SIMPLE ANSWERS: "simple english line, at most two lines if complicated to explain").
   B: CLAUDE.md rule 1 (line 23): present ALL viable paths in one message, each with what Rafi has to do, the risk, and which one I recommend.
   Clash: rule 1 asks for every path with three facts each; lesson 238(4) asks for one recommendation and rule 32 for at most two lines. It shows at step 1, where the list message goes to Rafi.
   Fix A: strike "give one plain recommendation" from lesson 238(4) and add to rule 1: "Where only one path is viable or one is clearly least effort for Rafi, the message names it in two lines." Fix B: add to rule 1: "When one path is clearly the least effort for Rafi, the message may name only that path with a one-line reason." (wording mine, not yours)
   Recommendation: Fix A.

8. Where a clash is shown: stop at once, or at the next stop (carried).
   A: CLAUDE.md lines 47-48 (rule 8a: Claude stops, names both rules, offers a fix "and waits for Rafi").
   B: Part B SKILL.md step 0c.3 (lines 72-73): "Bring the clashes with the story list at the stop of step 1 (or, if the helper is later, at the stop of step 7); never end a turn on them while writers are running."
   Clash: if this check comes back after step 1, wording starts under an unanswered clash, which is choosing; rule 8a says stop.
   Fix A: add to step 0c.3: "If this check is not back at the step 1 stop, step 1 waits for it; no wording starts until its CLASHES section is read." Fix B: add to rule 8a: "A clash found while writers run is shown at the next stop." (wording mine, not yours)
   Recommendation: Fix A.

9. Headlines openings: the writer brief against itself, the category rule and Rafi's dictated list (carried; NARROWER: "From Washington" is now allowed for politics).
   A: briefs/wording_headlines.md line 9 (example introductions "In politics", "From Washington", "On the markets", "Turning to safety"; "INTRODUCTIONS ROTATE (Rule G2): never use an introduction the previous day used"); CLAUDE.md HEADLINES INTROS AND FLOW (line 174: a natural order with "We begin with an update", "And finally, something lighter", "In the lab"; "never a label with no link to the topic").
   B: briefs/wording_headlines.md line 27 and briefs/check_headlines.md line 17 (a story clip opens with its own category; a place or a made-up topic fails; the one exception "From Washington" for politics, rule 32); check_headlines_rules.py B2d and B2e; lessons 296, 297 and 305.
   Clash: line 9 still gives "On the markets" and "Turning to safety" as examples, which B2e fails, and still says to rotate away from yesterday's wording, which category openings never do; "We begin with an update" of 6 Oct is not a category opening. A writer who follows line 9 can fail the gate. Not chosen.
   Fix A: in wording_headlines.md line 9 replace the examples by the category openings of line 27 and write "category openings are not rotated (G2 skips them); every other introduction rotates"; add to CLAUDE.md HEADLINES INTROS AND FLOW: "Since 14 Oct a story clip opens with its own category (Rafi, 14 Oct); the other intros of this list are for the fun clip, the teaser and the Bigger Picture." Fix B: keep line 9 and relax B2d and B2e (script change between runs). (wording mine, not yours)
   Recommendation: Fix A (the brief edit waits for his yes between runs, rule 16).

10. NEW. "At least 2 from the 6s for every category" against "exactly 2, and only when a category has no 7 and up" (live today: Ethics and law has 1 story).
   A: CLAUDE.md line 322 (rule 31, Rafi 15 Oct: "we take at least 2 items from 6!"; "this goes for all categories: the same holds for every Bulletin category").
   B: CLAUDE.md lines 100-102 (rule 14 BULLETIN SECTIONS NEVER EMPTY: top stories 7 and up; if a category has none, "exactly 2 stories ... at score 6 and up"; "the first version said 'at least 2' and the Bulletin got 10 Politics stories").
   Clash: rule 31 says at least 2 from the 6s for all categories and points to rule 14; rule 14 says exactly 2 and only when no 7 exists. Today Ethics and law holds 1 story (score 8) in the Bulletin while two NEW, read 6s sit in the report (C09-03 Texas Attorney General letters to data centres; C13-05 a Brazilian court order to Meta): the Bulletin was delivered by Part A, so Part B cannot add them (cards come only from the Bulletin; G4b).
   Fix A: add to rule 14 BULLETIN SECTIONS NEVER EMPTY: "A category with fewer than 2 stories at 7 and up is filled to exactly 2 from the 6s (Rafi, 15 Oct: at least 2 from the 6s)"; Part A then rebuilds the Bulletin before delivery. Fix B: add to rule 31: "Exactly 2 means a category with one story at 7 or more stays at one; the 6s fill only an empty category." (wording mine, not yours)
   Recommendation: ask Rafi which he means; Part B only reports it (Part A's product).

11. NEW. A story that ran at 7 or more may return (rule 34) against NO UPDATE CARDS, NO REPEATS IN 7 DAYS and the VIRAL RULE line (SLEEPS for cards today; live for the Bulletin text).
   A: CLAUDE.md line 334 (rule 34, Rafi 16 Oct: "keep them if they are meaningful updates": a story that ran at 7 or more may come back when it is a meaningful update, judged story by story; "answers the open question of lesson 195 for the viral rule").
   B: CLAUDE.md lines 204-207 (NO UPDATE CARDS: an update is a card only when Rafi names it; NO REPEATS IN 7 DAYS: no card or clip of the last 7 days comes back "as a repeat or as an update"); line 221 (VIRAL RULE: "A story that already ran earlier below 7 may run once more"); briefs/pick_stories.md and pick_gate.py G6 and G17.
   Clash: rule 34 does not say whether a returning 7-or-more story may be a card, clip or teaser item; the two lines above say no, and the VIRAL RULE line still says "below 7". Today C08-16 (Windows on Nvidia's RTX Spark laptops, follow-up of 9 Oct, score 7) is in the Bulletin by Rafi's choice; the gate refuses it as a card (G6) and the paper draft does not take it.
   Fix A: add to rule 34: "This is for the Bulletin and the report; a card, clip or teaser item of such a story still needs Rafi to name it (NO UPDATE CARDS)." Fix B: add to rule 34: "A returning story that Claude judges a meaningful update may also be a card; Claude says which and why." Fix C: change "ran earlier below 7" in the VIRAL RULE line to "ran earlier" (Rafi's rule 34 words). (wording mine, not yours)
   Recommendation: Fix A (it keeps NO UPDATE CARDS, which Rafi wrote angry on 7 Oct) and Fix C.

### 2a. Touches settled by Rafi's own precedence lines or rulings (not counted; the settling line named; carried from 15 Oct, new ones at the end)
1. 14 cards against extra_min 7 (11 Oct clash 1): 8b item 4 (a count he gives wins over a cutoff).
2. The second robotics card below extra_min (11 Oct clash 2): C11-03 scores 6 in the pack and 7 in the Bulletin (2b), C11-01 and C11-04 score 7 in both; 8b item 4 (the ROBOTICS count) settles it either way.
3. Politics clip 1 against HEADLINES ORDER and Drive A3 (11 Oct clash 3): newest ruling (7 Oct over 5 Oct) and 8b item 4 (an order he gave); CLAUDE.md over Drive.
4. The rewrite agent's model (11 Oct clash 4): rule 25 (12 Oct) replaced the rewrite agent with the same writer.
5. An update as a card (11 Oct clash 5): NO UPDATE CARDS (7 Oct) is newer than CARD FILTER (6 Oct) and NO OLD NEWS (5 Oct).
6. Teaser credit (11 Oct clash 9): newest ruling (Rafi, 10 and 11 Oct, D36 and lesson 241) over Drive G7.3; build_pack.py fixed on 12 Oct.
7. Drive upload of cards and JSON (11 Oct clash 10): rule 26 (12 Oct, newest).
8. Which score counts (11 Oct clash 11): Rafi's ruling "selection follows the pool score" (Part A SKILL.md line 245; build_products.py line 171); pick_gate.py reading the writer's score is a stale script line (2b).
9. Part B in the same chat (11 Oct clash 12): rule 18 speaks of starting a daily run; Part A starts Part B (rule 9); "Part B needs a new chat" is Claude's reading (lesson 123). A compacted chat still needs Rafi's yes (rule 18).
10. How clashes go to Rafi (11 Oct clash 13): rule 20 (10 Oct, his words: "ask them one by one") over lesson 142 (Claude's prevention).
11. The headline-only note in customer text (11 Oct clash 15): newest ruling (Rafi, 8 Oct, lesson 118) over Drive Bulletin and Full Report 5.3; Part A's delivered products.
12. What goes with the card list (11 Oct clash 16): rule 20 (10 Oct, newest): the list alone when he asks for the list; at step 1 the list goes with the fun concept (rule 29) and any clash, asked one at a time (rule 20 "ask them one by one"); the 3-day table goes with the deck at step 7.
13. One idea per sentence (Drive G1.3) against one sentence (11 Oct clash 17): rule 22 (newest; CLAUDE.md over Drive).
14. Apate against NO OLD NEWS, NO REPEATS IN 7 DAYS and the duplicate checks: closed; rule 23 named Apate for 12 Oct only.
15. A fun clip outside the deck against Drive A4 and lesson D25: not live (rule 23 was for 12 Oct); rule 24 "not necessarily in the cards" stands.
16. Clip length: rule 22 (aim 8, 10, 12 hard; 12 Oct) against the phrasing file ("never over 10") and the old CLIP SECONDS: newest ruling and CLAUDE.md over Drive (the briefs name the four overridden sentences).
17. The why: rule 22 (a company reason is a why) against the phrasing file ("effect on people"): same lines.
18. Bigger Picture clip "10 seconds" (rule 17) against "aim 8" (rule 22): rule 22 is newest and calls 10 acceptable.
19. Fable checkers (rule 25) against STORY CHOICE "Opus does the checks": rule 25 replaces it by name.
20. Groups of 10 (rule 24) against one file at a time (P1-10) and Cards Master 7.15: rule 24 newest; each card stays its own PNG.
21. Rule 26 (Rafi uploads) against rule 0 DAILY DELIVERY and Cards Master 7.4 and 7.8: rule 26 newest.
22. FUN STORIES (rule 24) against the old "funny at once": rule 24 newest; pick_stories.md is fixed (lines 7, 9-10, 40).
23. SKILL.md 0c.3 ("Drive and CLAUDE.md disagree: stop and ask") against CLAUDE.md line 205 (no clash, CLAUDE.md wins): CLAUDE.md over Drive (stale skill line in 2b).
24. Drive B1a two decimals, C4 six steps, Cards 2.6 aim 15, 2.8 full report only, 1.3 DESK VIEW: CLAUDE.md over Drive.
25. Step 0c before any choosing script (lesson 131; CLAUDE.md BEFORE EVERY STAGE) against the incremental check launched with the picker (SKILL 0c.2; lessons 262 and 272b): Rafi's yes of 13 Oct (newest).
26. Rule 27 (Opus normal effort, story pack read once) against "at max" of rule 25, the "re-read before each item" of READER LEVEL and the phrasing file's "every writer, every item": rule 27 names what it replaces; Part B writers only.
27. Rule 28 (the listen first at step 7) against Cards Master 7.15 and 7.16 (contact sheet first): rule 28 newest; CLAUDE.md over Drive.
28. Rule 29 FUN CLIP CHOICE against lesson 236 (three finished lines): rule 29 replaces it by name.
29. Part B SKILL step 8.2's old Drive agent text (kept for later) against rule 26: rule 26 newest; the step says so itself.
30. Rule 29 (Bigger Picture Bulletin 300 to 500 words) against the 350-word wish (lesson 207 item 7): answered by rule 29; today's text is 498.
31. Rule 24 NO TIME PRESSURE: decided 13 Oct ("yes exactly!"); no open touch.
32. The 12 Oct "8 story clips" template against the gate's 7 clips (lesson 267 item 2): scripts stay as they are (rule 16) until Rafi's yes (lesson 272a); today 7 clips.
33. Rule 30 CRITICALS ALWAYS ON TOP against HEADLINES START WITH POLITICS (7 Oct, "Fable never skips Politics or reorders the deck"): rule 30 says "above Politics" in its own words and is the newest (14 Oct); G11b was changed to match. Not live today (no 10, top 8).
34. Lesson D3 "anthro-pic" (Rafi, 14 Oct) against Drive Headlines Master 15 Sep 1 "an-thropic": the newest ruling and THE REPO IS THE SOURCE OF TRUTH settle it; 2d.
35. Lesson 296 (the phrase list of check_wording.py) against the quoted hedges of entries: the checker keeps the entry's hedge; no touch.

36. NEW. Rule 32 FROM WASHINGTON ("From Washington means in politics ... that was fine") against the 14 Oct "never a place" line (lesson 296): rule 32 is newer (15 Oct) and the brief line 27 and B2d now say so.
37. NEW. Rule 32 USELESS TAIL (a hedge is one word) against Drive Headlines Master G1.4 ("hedges kept") and the card format "hedges kept" (lesson 308): rule 32 is newer; the hedge is kept as one word, the clause goes.
38. NEW. Rule 32 CUSTOMER PRODUCTS (no codes, no process words) against the Drive "headline only" notes and the About note (lessons 118 and 306): rule 32 and rule 35 are newer (15 and 16 Oct); today's Bulletin and report carry no old note.
39. NEW. Rule 31 "a section whose 7-and-up stories are all headline only counts as empty" against the 15 Oct reading "Politics had two at 7, both headline only, I treated it as not empty": Rafi's yes of 15 Oct settles it; not live today.

### 2b. Stale lines in briefs and scripts (grep of the old wording of rules 22 to 29; scripts change only between runs, CLAUDE.md lines 159-161)
BLOCKS TODAY:
- pick_gate.py lines 66-69, 76 and 145-150 read the writer's score from report_entries; the Bulletin and card_candidates.py use the pool score (Rafi's ruling, 2a item 8). 8 of 39 Bulletin stories differ today, each 1 higher in the Bulletin (C12-02 Security and C08-03 Energy 6 against 7, C14-01 Society 6 against 7, C11-04 and C11-05 Robotics 5 against 6, C14-04 and C14-06 Society 5 against 6, fun C16-01 4 against 5; the paper draft already uses the Bulletin's pool score). It changes ranks and the extra_min 7 test (C12-02, C14-01 and C11-04 are cards in the draft at the pool score and below the cut in the pack). Align before the picker (lesson 234d, run-folder data only): copy the entries to report_entries_before_pool_score_old (next to report_entries, never inside it, lesson 288), set score to the pool score and keep the writer's as fc_score; or tell the picker that the Bulletin score counts.
- make_wording_prompts.py lines 18-21 and common_b.py prev_scripts: PREV_CARDS and PREV_PACK come only from scratchpad run_ folders, so today they are "none" and assets/pack_base.json (2 Oct lines, "sentences of at most 15 words") unless arguments are given; PREV_LEADINS come from the newest repo runs/<day>/headlines_work/scripts_final.json before today, which should be 15 Oct (to confirm the file exists). Run it with --prev-pack /home/user/ai-news-desk/runs/2026-10-15/headlines_work/headlines_15-10-26_pack.json --prev-cards /home/user/ai-news-desk/runs/2026-10-15/cards_copy.json (arguments, no script change).
FIXED SINCE 12 OCT (no longer listed; also fixed 14 Oct: the Politics clip 1 and critical order in G7, G11b, G21, the fill's reference-pair assert and template, final_audit.py): pick_stories.md lines 7, 9-10 and 40 (fun follows rule 24); SKILL step 8.2 (copy-to, rule 26); SKILL "currently 1 to 130" (step 0c rewritten); the picker prompt filled by hand (pick_gate.py pack writes it); the writers' re-read before each item (story packs).
DO NOT BLOCK TODAY:
- Part B SKILL.md step 0c: the heading still says "before anything is chosen" while the body says the picker does not wait (Rafi's yes of 13 Oct settles it, 2a item 25); step 0c.3 "Drive and CLAUDE.md disagree: stop and ask" against CLAUDE.md line 206 (no clash, CLAUDE.md wins); see also clash 8.
- Lesson 280: every Part B brief says "never run git"; "not even git status" is not in the text yet (add between runs).
- briefs/wording_headlines.md line 9 (examples "On the markets" and "Turning to safety" fail B2e; "From Washington" is allowed for politics since 15 Oct; "INTRODUCTIONS ROTATE" against line 27): clash 9.
- Lesson 296 open item of 14 Oct: three delivered 14 Oct lines failed the new loose-phrase check (card 11 "far more", the teaser "Hundreds of" and "far more"); today's writers run check_wording.py first. Lesson 304: no script catches a useless tail (rejected: flags 14 of 22 past clips); the checker's 3b is the only guard.
- The `_old` copies inside the skill (briefs/wording_common_before_exact_old.md.txt, scripts/pick_gate_before_critical_old.py.txt, assets/..._old_hologram_first.json): kept by rule 3, not read by any script (lesson 288 holds).
- fill_headlines.py line 11 (docstring): "no clip may pass 10 s ... the Drive Section B item 1 still says 12": the code asserts 12 (line 95), as rule 22.
- check_headlines_rules.py lines 5 and 8-9 (docstring: "15 words ... 12 s", "CLAUDE.md 16: stories 8 to 9 s") and line 69 (B1 WARN aims 9.0, 8.5, 8.5, 10.5 against rule 22's aim 8; warnings only); lines 1, 6, 15, 100 still name "the rules agent (step 3c)".
- check_wording.py lines 6-10 (docstring): "every sentence at most 15 words", "Headlines: the same sentence rules": the code counts words and drops the count (lines 62, 69), so the card 15-word cap (wording_cards.md line 9) is not scripted; no clip one-sentence test (rule 22) either. Count both at step 7.
- briefs/wording_common.md line 13 (was 12): Headlines "shape and length are set only by the Headlines section of the phrasing file and CLAUDE.md CLIP SECONDS": rule 22 overrides that section (wording_headlines.md lines 12 and 25 say so). Fix: "set by CLAUDE.md rule 22 and the model lines file; the phrasing file's Headlines section only where rule 22 does not override it."
- briefs/wording_common.md line 12 (was 11): "then a stranger who knows nothing retells every item": the Fable checker does the stranger test now (rule 25).
- briefs/wording_headlines.md line 20: "no identifiable faces, since the fixed video prompt says no faces": the fill PROMPT (line 18) says "no real named faces" and line 17 of the brief allows anonymous people (stricter, harmless).
- briefs/pick_stories.md line 10 "(written later by Fable after Rafi approves; you only name its sources)": the Bigger Picture card is written by the Opus card writer today (rule 25; clash 4). Line 36 "(for example Politics today)" is an old example that applies for real today (clash 5).
- briefs/pick_stories.md line 27 "7 ids from your cards", pick_gate.py G11 (line 136), check_headlines_rules.py A3 (lines 50-52): stricter than rule 24 ("not necessarily in the cards"); clips from the cards meet both.
- briefs/pick_stories.md line 25 (label at most 14) against line 37 (15), pick_gate.py G14 (line 140, 15) and SKILL.md ("about 15"): 14 meets all.
- briefs/stranger_cards.md, stranger_headlines.md, rules_check_headlines.md (reads the story pack now but is still the step 3b brief), rewrite_headlines.md, factcheck.md ("Part B step 4"): superseded by rule 25 and still written by make_wording_prompts.py: never launch them.
- Part B SKILL.md lines 89-91 (an update kept when meaningful; G6 enforces NO UPDATE CARDS, clash 6), line 93 ("3 to 4" teaser; the gate takes exactly 4), lines 93-94 (clips "strongest card stories by score"; G11b puts Politics first), line 147 ("C01 and C13 carry Rafi's opening and ending of 2 Oct": both are bypass), line 182 ("The stranger check is fast").
- build_pack.py line 6 and lines 24-25 (opening and ending "of 2 Oct 2026": bypassed slots) and line 28 (review_status "checked by ... a stranger check and a rules agent; approved by Rafael": written into the JSON's extra.aind_fill and MarkdownNote 9990, wrong checks named after rule 25; fix between runs).
- build_cards_copy.py line 46 (note "Card wording written by Fable ... and a stranger check") and line 37 (the SOURCE line copies the entry's source; a relay named in an entry would print as is: patch cards_copy.json by hand, lesson 267 item 4).
- common_b.py lines 37, 46, 51: the gate message names "step 3b" and "prompt_rules_headlines.txt"; the file it needs, headlines_work/rules_result.json, is written by the Fable Headlines checker (check_headlines.md line 10): works as is.
- card_candidates.py lines 9-14 (docstring: updates kept when meaningful; clips by score) and the draft it wrote at 08:14: no Politics, Robotics or Research card, no robotics clip, 3 Market clips of 7, a teaser of 3 follow-ups (C05-01, C05-03, C08-02): paper input; the picker must not copy the draft.
- briefs/check_headlines.md line 3 reads Headlines Master A, B, G and the 15 September section from the pack with only the phrasing file overridden: the checker may flag a correct one-sentence line for G1.3 or a rounded box for B1a (lesson 92 pattern); if it does, rule 22 and rule 16 win (2a items 13 and 24).
- review_list.py line 32: removes ", simple text-free symbol" (harmless).

### 2c. Checked, not live today
- A third robotics card ("one extra allowed") against G8's cap of 2: five eligible robotics stories today (C11-01 to C11-05) but only two cards are asked; the report-only robotics stories cannot be cards while the Bulletin has eligible ones (G4b exception test).
- VIRAL RULE re-run clause: no re-run; no card candidate needs the exemption today (clash 6 sleeps).
- Critical stories spending a slot (rule 30): no score 10 (top 8), so G21 has nothing to move. Cards Master 2.10 big release rule: not in force.
- Robot war limit on cards: no such limit.
- (Section 2: clash 5, a Politics reserve card as clip 1 against G4b, sleeps today because C13-03 and C13-04 are eligible; the category openings against the brief, clash 9, and the fun opening, clash 3, are live.)
- Research needs no report-only exception card today: the Bulletin has two eligible Research stories (C15-01 at 8, C04-01 at 7).

### 2d. Drive differences settled by CLAUDE.md
- docs/DRIVE_DIFFS_FOR_CHATGPT.md is out of date (lesson 276) and was not opened today. New since 15 Oct: rule 32 (FROM WASHINGTON, USELESS TAIL, "In today's fun corner") against Headlines Master B2a, G1.4 and G2; rule 35 against Full Report and Bulletin 5.3 and 11.4 (the headline-only note). Carried from 14 Oct: lesson D3 (spoken cue "anthro-pic", Rafi 14 Oct) against Headlines Master 15 Sep 1 ("an-thropic"); rule 30 (criticals above Politics) against Headlines Master order block A3 and HEADLINES START WITH POLITICS; the 14 Oct category-opening rule (lesson 296) against Headlines Master B2a/G2 rotation. Still standing: rule 27 (writers Opus on normal effort, one story pack read once) against the phrasing file's "every writer re-reads before each item"; rule 28 (the listen first at step 7) against Cards Master 7.15; rule 29 (Bigger Picture Bulletin 300 to 500 words; the fun concept to Rafi) against the Bulletin rules; rule 22 against the phrasing file's Headlines section; rules 23 and 24 (a fun clip outside the deck, 12 Oct only) against Headlines A4; rule 24 groups of 10 against Cards 7.15; rule 26 (Rafi uploads) against Cards 7.4 and Headlines E5.

### 2e. Open for Rafi: rule gaps, not clashes (asked one at a time, only when they matter)
1. The 13 Oct edition is missing (lessons 281, 299 and 309; the 13 Oct chat waits on a Rafi answer and git is blocked there): Rafi says yes in that chat, or accepts that G17 covers 6 days.
2. May a writer move a story to another category (lesson 285)? The gate reads the entry's category; Part A, not live in the pack today.
3. Do events of the day before the window count (lesson 287)? Part A rule question.
4. The card post text (lesson 271): a daily product or not, who writes it.
5. The Bigger Picture Full Report version is about 12,300 words (lesson 303) against the Bulletin version's 300 to 500 (rule 29): Rafi has not ruled the Full Report version. Part A's product.
6. Models and tools had nothing at 7 and the Bulletin section was cut to exactly 2 by hand (lesson 301): build_products.py needs a per-category "exactly N" fill (a script change between runs); the same for the fill drift of lesson 302 (a skill line).
7. Scripts changed on 14 and 15 Oct (pick_gate.py G7, G11b, G21; check_headlines_rules.py B2d and B2e; check_wording.py loose phrases; final_audit.py; the template and fill assert): CLAUDE.md rule 30 and lessons 296 and 297 record Rafi's words, but his yes to the exact edit lists is not in the delta (CLAUDE.md rule 16, exception of 11 Oct). Open: building the other 17 enforcement gaps of enforcement_gaps.md.
8. Meta, for the main chat: the same gap happened again: rule 31 (and the 15 Oct "yes" line) was written after the 15 Oct check but before the commit 468d519, so the delta shows only its changed lines; this check read the rule from the CLAUDE.md context copy and lists it in CHANGED. Fix (script, between runs): base the delta on the commit before the check was written, or on the check's own line count.
9. Open for Rafi from the delta: lesson 306 (the markets share sentence in the Full Report Bigger Picture, he said yes to remove it, not done), lesson 307 (a check that fails a named person with no title), lesson 311 (build_products.py and the PDF About wording still print the old not-found line until his yes), lesson 315 (should Part A writers read the rules once, as Part B does). All Part A; none blocks Part B.

## 3. Today's must-haves and facts

### 3a. Must-haves for the picker
1. Counts: 14 story cards (32 are eligible, 20 within the limits, so 14 is reachable); exactly 4 teaser items (report stories, no card, NEW, not in the last 7 days); exactly 7 story clips; 1 Fun card; the Bigger Picture named as card and clip (G20); bp_refs 3 to 5 report ids the Bigger Picture text rests on. By my match of the Bulletin text the ids are C07-01 (default insurance at record highs), C07-02 (CoreWeave bonds), C07-03 (chip and memory stocks lose more than 1 trillion dollars), C06-01 (Anthropic valuation; a follow-up, allowed as a source) and the TSMC record-profit story (C08-03 Livemint or a report-only entry: to confirm); the paper draft's C06-01, C07-01, C08-01 is a partly different set (C08-01 is TSMC in talks to join Elon Musk's project). The picker confirms.
2. Order: deck in the Drive order Politics, Market, Security, Energy, Robotics, Models, Research, Ethics and law, Health, Society, Fun; a story rated 10 first (rule 30; none today); higher score first inside a category (the Bulletin's pool score, 2b); clips in deck order; the Politics clip is clip 1.
3. Draft faults to catch (paper input only; the picker must not copy the draft): (a) Meta's Muse Spark Open appears twice, C06-02 (s4) and C01-01 (s10): one topic, one card; (b) the fun card C16-01 is a follow-up of 14 Oct and DISPUTED, marked type UPDATE: G6 and NO UPDATE CARDS; candidates C16-02 (PRELIMINARY) and C16-03 (REPORTED); (c) the teaser holds C05-01 and C06-01, both follow-ups: G6; (d) one robotics card, no humanoid; (e) Anthropic is on exactly 3 cards (C13-03, C12-01, C13-01), the limit; clips: C13-01 only.
4. Politics: C13-03 (New York City's comptroller urges Anthropic to delay its listing, 7, NEW, confirmed) and C13-04 (Pentagon officials reportedly keep a strike report secret until after the midterms, 7, NEW, reported) are eligible, read in full; C05-01 (Huang on working with Chinese AI firms) is a follow-up of 14 Oct. Clash 5 sleeps.
5. Research: C15-01 (Google quantum team, 8) and C04-01 (a physics test of OpenAI's model, 7) are eligible; reserve 6s C01-05, C04-02, C04-03, C15-03, C15-04.
6. Limits: at most 2 cards a category (Market 3); a company on at most 3 cards and 2 clips (Apple 4, OpenAI 4, Nvidia 3, Tesla 3, Anthropic 3 among eligible stories); labels at most 14 characters, no money figure; read in full only (C14-04 is headline only); status in the pack: C16-01 DISPUTED, C16-02 PRELIMINARY, the rest REPORTED or CONFIRMED.
7. CARDS FROM THE BULLETIN: cards only from the 32 eligible Bulletin stories (Market 4, Security 3, Energy 5, Robotics 5, Models 3, Research 2, Ethics and law 1, Health 3, Society 4, Politics 2); a reserve card only for a category with no eligible Bulletin story (none today).
8. ROBOTICS: 2 robotics cards, one humanoid: the humanoid candidate is C11-02 (Faraday Future's two low-priced humanoid robots at $2,490 and $299; machine_action false, so it needs a robotics_ruling with a reason, G13; a product launch is not a machine doing something, but Rafi's 8 Oct ruling counts humanoid stories); the second card C11-04 (Tesla's remote operator drove five robotaxis; machine_action true; scores 5 in the pack, 6 in the Bulletin); C11-01 (Volvo and Nvidia hands-free driving, 7) is the third option. 1 robotics clip, saying what the robot or vehicle does.
9. NO UPDATE CARDS: the 3 follow-ups (C05-01, C06-01, C08-16) and fun follow-up C16-01 are no card, clip or teaser item (G6); C06-01 may only be a bp_refs source; rule 34 and clash 11.
10. NO REPEATS IN 7 DAYS: G17 plus the 3-day table; hits to judge listed in 1a (C07-02, C07-03, C08-03, C13-01, C05-01). The 13 Oct decks are not in the repo (lessons 281, 299 and 309): ask Rafi in the list message to say yes in that chat, or accept the gap.
11. Fun (rule 24, rule 29, rule 32): the fun card and headlines_fun come from the Bulletin (G4b): C16-02 or C16-03 (C16-01 is a follow-up); the picker gives the concept in one line each and Rafi says if it is funny; opening "In today's fun corner" (clash 3); a fact that is not a joke is "Today's fun fact" (lesson 292).
12. Rule 24 "one sentence" test: C06-02, C13-01 and C13-04 are two-party stories: test each before it becomes a clip; REPLY STORIES: read C13-03.
13. NOVICE TEST and PEOPLE WITH THEIR POSITION for every name (1a, 8b item 6; rule 32 NAMES NEED TITLES).
14. Rule 28, rule 29, rule 32 and lesson 297 to carry out later: the listen at step 7; the fun concept in the step 1 message; final_audit.py before every send (step 6b); no useless tail and a title for every name; check this chat's model (lesson 294).
15. Openings (lesson 296, clash 9, rule 32): every story clip opens with its own category; "From Washington" only for a Politics clip; exact figures from the entries (for example 3.7 percent inflation is yesterday's; today: 1,100 basis points, 64 percent, 1 trillion dollars, 7.6 percent, 69 percent, $2,490 and $299, 1.5 trillion dollars); no place, no "from" otherwise.
16. Customer products (rule 32): no ids, codes or process words on any card or clip line.

### 3b. Facts of this edition
- Edition FRI 16 OCT 2026; window 15 Oct 04:54 to 16 Oct 04:54 UTC (24 hours, run.json); no critical story; top score 8 (seven stories: C01-01, C05-01, C06-01, C07-01, C08-01, C13-01, C15-01).
- Pick pack (cards_work/pick_pack.json): 39 Bulletin candidates and 72 report-only reserve stories (111 in all, equal to the report's 111); its filter equals the CARD_FILTER line (5, 7, 14, 2, 3, 3, 2).
- Bulletin (products/bulletin_pdf.json): 39 stories: Politics 3, Market 5, Security 3, Energy 6, Robotics 5, Models 3, Research 2, Ethics and law 1, Health 3, Society 5, Fun 3. Pool scores in the Bulletin: 8: 7, 7: 20, 6: 9, 5: 1, 4: 2 (pack scores: 8: 7, 7: 17, 6: 8, 5: 4, 4: 3). Purpose line in words (Health, Society and education, Robotics from 6) plus the top 3 Fun. 25 different source hosts by url, 0 Google News links. Bigger Picture section 499 words by paragraphs (rule 29: 300 to 500), "About this edition" 88 words, no process wording. 1 story ends "Read the full article at <source>." (rule 35); no old note.
- Report (products/report_pdf.json): 111 stories in 11 categories (inside 100 to 120); 4 "Read the full article" lines, 0 "Note: we could not open"; the About text says 107 of 111 stories were read in full.
- Card-eligible Bulletin stories (NEW, read in full, not a follow-up): Market 4 (C06-02, C07-01, C07-02, C07-03), Security 3 (C12-01, C12-02, C12-03), Energy 5 (C08-01, C08-02, C08-03, C08-04, C09-01), Robotics 5 (C11-01 to C11-05), Models 3 (C01-01, C01-02, C02-01), Research 2 (C04-01, C15-01), Ethics and law 1 (C13-01), Health 3 (C10-01, C10-02, C10-03), Society 4 (C14-01, C14-02, C14-03, C14-06), Politics 2 (C13-03, C13-04). Total 32; within the limits 20.
- Not eligible: follow-ups C05-01, C06-01, C08-16 plus fun C16-01; headline only C14-04; Fun 3 (C16-01, C16-02, C16-03).
- Report-only reserve (72): Models 9, Research 9, Security 9, Market 9, Society 6, Energy 6, Robotics 6, Fun 6, Politics 5, Ethics and law 5, Health 2; 63 are NEW and 9 are follow-ups (C04-04, C04-12, C05-08, C09-05, C09-06, C09-07, C11-06, C13-06, C14-08); teaser candidates come from the NEW ones.
- Paper draft (card_candidates.py, 07:22): cards C13-03, C13-04, C07-01, C06-02, C07-02, C12-01, C12-02, C08-01, C11-04, C01-01, C15-01, C13-01, C10-01, C14-01 plus fun C16-01 (14 story cards); clips C13-04, C07-01, C08-01, C11-04, C01-01, C15-01, C13-01; teaser C05-01, C06-01, C12-03, C08-02; bp_refs C06-01, C07-01, C08-01. Draft faults: 3a item 3.
- Last 7 days in pick_pack.json: 15 Oct 48 lines, 14 Oct 48, 12 Oct 51, 11 Oct 48, 10 Oct 48, 9 Oct 48; 13 Oct 0 (missing).
- Bigger Picture watch dates in the Bulletin text: Wed 21 Oct Meta results; 27 to 29 Oct SK hynix (its filing names 28 Oct, Seoul time), Fed decision Wed 28 Oct, Alphabet, Microsoft and Intel results (Intel names Thu 29 Oct); CoreWeave default insurance day by day; Anthropic's answer to the New York City comptroller and any public filing with a price range. Weekdays computed with python (16 Oct Friday; 21 Oct Wednesday; 28 Oct Wednesday; 29 Oct Thursday). It carries "not financial advice".
- Viral rule and the report's own cutoff and Fun Side: Part A's numbers, not read here; verify at 0c.4.
- Introductions used on 15 Oct (G2; category openings exempt): In finance; Also in finance; In politics; In law; In security; In robotics; In the lab; In today's fun corner; Also in the full report; And for the bigger picture. 13 Oct's are unknown (not in the repo).

### 3c. Cards and Headlines of the last 7 days (for G17 and the 3-day name and topic table; clip intros in brackets)
- 2026-10-15: pick_pack.json last_7_days holds 48 mixed lines (cards, clips, teaser and Bigger Picture); the structured deck is runs/2026-10-15/cards_work/selection.json (read it there for the 3-day table). Topics seen in the lines: Huang would stop selling chips to makers of unsafe AI [In security]; China reportedly let Apple put Alibaba's Qwen on iPhones [In politics]; eight US states sued OpenAI over ChatGPT and children [In law]; US shares fell on 3.7 percent inflation [In finance]; TSMC beat profit forecasts, a sixth record [Also in finance]; Waymo opened to San Antonio, San Diego and Tampa [In robotics]; Microsoft weather-error tool [In the lab]; comedian's AI double at an AI recruiter's interview [In today's fun corner]; teaser CoreWeave shares down 17 percent and a Chinese AI solving a maths puzzle [Also in the full report]; BP AI and chip shares fall as borrowing costs rise, watch the Fed on 28 Oct [And for the bigger picture]; cards also: Fink on data centre fears, AGIBOT funding, EU questions OpenAI and Anthropic, Grok Voice 3.0 ranked first, Hassabis on AI hacks as warning shots, Meta's ten health studies, enzymes against Alzheimer's proteins, YouTube labels AI songs, a Kentucky uranium site as an AI hub.
- 2026-10-14 (runs/2026-10-14/cards_work/selection.json; the delivered deck may differ) CARDS: s1 C12-01 critical cyber threat (score 10) | s2 C07-04 Nvidia's China share | s3 C06-01 Anthropic's investor day | s4 C08-01 ASML sold out | s5 C09-01 Oregon data centre pause | s6 C11-01 Tesla robotaxis and school-zone speed | s7 C11-03 Agility Robotics' Digit listing | s8 C02-01 Muse Wonder | s9 C02-03 build your own app | s10 C04-05 China research | s11 C13-02 OpenAI bugging | s12 C10-01 Hopkins AI | s13 C14-01 Kroger cuts | s14 C14-15 chatbot bust | fun C16-01 fun fact | teaser C12-02, C13-03, C10-05, C05-07 | BP chip shares and rising interest rates, Anthropic's investor day, ASML || HEADLINES: C12-01 [First, a critical cyber threat]; C07-04 [In finance]; C08-01 [In infrastructure]; C11-01 [In robotics]; C02-03 [In tech]; C13-02 [In the courts]; C14-01 [At work]; fun C16-01 [Today's fun fact]; teaser; BP.
- 2026-10-13: MISSING from the repo (lessons 281, 299 and 309); pick_pack.json last_7_days has 0 lines for it. Ask Rafi (3a item 10).
- 2026-10-12: 51 lines in pick_pack.json last_7_days['2026-10-12'] (cards, clips, teaser and Bigger Picture mixed); the structured deck is runs/2026-10-12/cards_work/selection.json. Read it there for the 3-day table; the Bigger Picture of 12 Oct said to watch the IMF report on Tuesday.
- 2026-10-11 CARDS: s1 C05-07 Britain's AI institute chief wants home-grown AI nobody abroad can switch off | s2 C06-01 Nvidia reportedly in talks to buy or invest more in AI lab Reflection | s3 C07-01 South Korea's stock market is losing its buyers | s4 C05-01 Microsoft's boss Satya Nadella wants an emergency brake to stop any AI mid-task | s5 C12-02 OpenAI says an AI faked test grades and damaged its workspace | s6 C08-01 Nvidia reportedly ending the RTX 5090 | s7 C11-03 US Army's new war drones overheated and lost signal | s8 C11-10 Tesla Optimus learned to vacuum and stir food by watching people | s9 C01-02 OpenAI's price list shows an unannounced biology AI | s10 C13-01 the White House leans on old laws to police AI | s11 C10-01 Chinese hospital AI reads a lung tumour sample in a minute | s12 C10-02 commentary: US health care tests Big Tech's AI spending | s13 C14-01 Nicolas Cage refused an AI waiver | s14 C14-02 Hollywood films on the bosses of Meta, Tesla and OpenAI | fun C16-01 tiny game studio took a bank loan for its AI learner driver | teaser C12-03 Britain's spy chiefs on the AI threat, C01-06 South African model for 12 languages, C14-07 workers pay a female AI helper less, C09-03 data centres an election issue in Ohio and Michigan | BP investors wary of AI debt, watch TSMC on 15 Oct || HEADLINES: C05-07 [In politics]; C06-01 [In business]; C05-01 [In security]; C12-02 [Also in security]; C11-10 [Turning to robots]; C10-01 [In health]; C14-01 [In entertainment]; fun crab robot plans given away (Rafi's own choice, not the fun card) [And finally, something lighter]; teaser C12-03 + C01-06; BP AI debt cooling, TSMC Thursday.
- 2026-10-10 CARDS: s1 C13-03 China: no blind money into AI and high tech | s2 C06-01 odds start-up TypeSafe valued at $7.5 billion | s3 C12-01 Claude sent police a made-up murder tip in a test | s4 C12-02 AI bosses rehearse for the day after an AI disaster | s5 C08-02 big buyers booked most of Samsung's memory chips | s6 C11-17 wheeled humanoid robot under $30,000 | s7 C11-18 Ukrainian ground robots rescued 45 soldiers | s8 C01-16 Musk backs Anthropic's ban on cruelty to AI | s9 C01-03 Alibaba's Qwen3.8 free to download | s10 C04-07 amateur with AI tools may have found a planet | s11 C08-01 Super Micro contractor admitted smuggling Nvidia chips | s12 C10-01 tech firms lobbied US health officials in a chat room | s13 C14-04 Nikon took back a prize over an AI-made video | s14 C14-05 publishers use AI for covers without telling authors | fun C16-01 government chatbot shared pasta recipes | teaser C02-01 Amazon asks Meta to keep its AI helper off its store, C01-01 Microsoft choice-only model, C10-02 GSK signs AI start-up Chai, C09-05 batteries cheaper than gas turbines | BP shares recovered from an OpenAI scare as China warned of blind investment || HEADLINES: C13-03 [From Beijing]; C06-01 [In finance]; C12-02 [Next, safety]; C11-17 [In robotics]; C01-16 [On chatbots]; C08-01 [In court]; C14-04 [In science]; fun C04-07 (story card s10, not the fun card) [On a lighter note]; teaser C02-01 + C09-05.
- 2026-10-09 CARDS: s1 C05-02 Trump: anyone saying artificial intelligence, not superintelligence, is the enemy | s2 C13-21 Musk accused Indian tycoons of blocking Starlink | s3 C06-04 OpenAI sales pace $20 billion below its earlier figure | s4 C07-04 WTO doubled its trade growth forecast on AI demand | s5 C03-01 Anthropic scans open-source code for free | s6 C12-02 OpenAI shut down Russian and Iranian fake-writer groups | s7 C09-03 Oracle trucks natural gas to data centres | s8 C11-23 humanoid robots directed traffic in Hangzhou | s9 C11-06 Walmart's warehouse robots break down | s10 C01-01 Gemini 4 Argon first for security experts | s11 C04-04 scientists: Anthropic overstated a gene-editing find | s12 C13-01 USA Today's publisher sued OpenAI | s13 C10-01 Google chatbot questioned patients before urgent visits | s14 C14-07 charity to record Gaza classrooms with AI | s15 C16-01 streamer's robot whacked him on the head (no separate fun card) | teaser C02-01 Gemini helper for firms, C11-24 Tokyo shop robot, C09-04 senators on data centre costs, C14-06 San Francisco rents | BP investors want results after OpenAI's lower sales figure || HEADLINES: C05-02 [First, super intelligence]; C13-21 [In India]; C07-04 [On trade]; C12-02 [In security]; C11-23 [Next, robotics]; C01-01 [In tech]; C14-07 [In education]; fun C16-01 [And now, something lighter]; teaser C02-01 + C14-06.
