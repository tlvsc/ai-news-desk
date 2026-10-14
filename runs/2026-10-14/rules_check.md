# Rules check, Part B (cards and Headlines), edition 2026-10-14 (WED 14 OCT 2026)

Updated from runs/2026-10-12/rules_check.md by the delta of 2026-10-14 (rules_delta.md: base commit 7a128c5, now 13c68a0). Written by the rules-check helper (Sonnet), Part B step 0c, incremental (lessons 262 and 272b), 08:25 to 08:33 UTC (date -u).
Read in full: rules_check_previous.md and rules_delta.md. Opened only around a change: briefs/check_cards.md, check_headlines.md, rules_check_headlines.md, rules_check_update.md, wording_common.md, wording_headlines.md, wording_cards.md, pick_stories.md; Part B SKILL.md (steps 0c, 7 and the stale-line grep) and Part A SKILL.md step 9b; pick_gate.py (G2 to G20 lines); make_wording_prompts.py and common_b.py (previous-run lookup); lessons 238 and 276 of docs/V1_TASKS.md; CLAUDE.md lines named in section 2. Today's facts (section 3) come only from cards_work/pick_pack.json, cards_work/selection_draft.json and products/bulletin_pdf.json (counts and ids; a few summaries for repeat and credit checks). Not read in full: docs/V1_TASKS.md, the skills, the Drive rule files (delta section 4: no change).
CLAUDE.md: the copy in this helper's context and the disk file agree (317 lines, both end at rule 29 FUN CLIP CHOICE).
W = /tmp/claude-0/-home-user-ai-news-desk/752c7fb8-5733-578c-a28a-6c00f253a6a8/scratchpad/run_2026-10-14
State at 08:25 UTC: Part A's six _Claude-V1 files are in for_rafi (whether Rafi has them in chat: not checked here). At 08:14 card_candidates.py (cards_work/selection_draft.json) and pick_gate.py pack (pick_pack.json and .md, prompt_picker.txt) ran: paper input only, nothing chosen. No selection_fable.json, no wording, no cover, no headlines_work folder yet.
Every fix offered in section 2 is my wording, not Rafi's (CLAUDE.md rule 20). Nothing was applied.

## CHANGED SINCE 2026-10-12 (one line per change in the delta; "met" = how this run meets it)

CLAUDE.md
1. Rule 24 NO TIME PRESSURE: DECIDED 13 Oct ("yes exactly!"): rule 22 length wording and the model lines file stay. Met: nothing to change; 1a line closed.
2. Rule 27 WRITERS FASTER: Opus normal effort, one story pack read once. Met at step 2 (effort "medium"); 1a lines rewritten, new rule 27 line.
3. Rule 28 DAILY HEADLINES LISTEN: met at step 7 (spoken lines in the chat before the review list); new 1a line; Fable check stays.
4. Rule 29 TWO CHATS: cloud chat for Part B, local chat for the PC; no Part B change (new line).
5. Rule 29 HIS PC, DRIVE UPLOAD KEY, DOWNLOADS, DRIVE DUPLICATES: do not apply to Part B (1e).
6. Rule 29 ARTICLE: "article" means any item; ask which only when it matters (new line).
7. Rule 29 BIGGER PICTURE IN THE BULLETIN (300 to 500 words): today's text is 531 words, Part A's product: one line to Rafi (new line).
8. Rule 29 LESSONS FOR THE REPO: lessons of this run into docs/V1_TASKS.md once, search first (new line).
9. Rule 29 MISTAKES NOT AGAIN: read aloud test is check 1b of check_cards.md; show the real lines (new line).
10. Rule 29 FUN CLIP CHOICE: Claude gives Rafi the fun concept; replaces lesson 236's three lines (new line; rule 23 Apate was 12 Oct only).

docs/V1_TASKS.md (added or changed lines)
11. P1-18 ADDED (pgrep -f killed the shell): Part B uses run_in_background and ps with a bracket pattern (1d line 77/101 rewritten).
12. 217 DONE (NOTES slot in curator and filler briefs): Part A only (1e).
13. 236 REPLACED by rule 29: see 10 (1d line rewritten).
14. 240 ADDED (stutter fixing): Rafi's PC (1e).
15. 246 ADDED (sync_repo.sh hook): Part B step 0 runs it; 1d line rewritten; fetch before each push.
16. 248 ADDED (viral check matches by link): Part A (1e).
17. 254 ADDED (check_dup14 prints the full line): Part A (1e).
18. 257 ADDED, FIXED (save_state.py, delivery_manifest.py --copy-to): used at steps 7 and 8 (1d line rewritten).
19. 262 ADDED (incremental rules check in force): this file is that check; 131 and 262 meet in 2a item 25 (new 1d line).
20. 266 ADDED (medium effort, draft first, no code reading, checkers read the pack, cards checker sees the Bigger Picture text): met by SKILL step 2 and the briefs; to measure (rule 27 line).
21. 267 (Part B findings: report trace, 8 clip template, gate has no override, source strip patch, assembler needs I01): new 1d line; edits wait for Rafi's yes.
22. 268 (the daily listen): rule 28 (new line).
23. 269 (footage search): PC and later (1e); screens stay generated.
24. 270 (helper time limit): proposed, NOT in force; not applied (new 1d line).
25. 271 (card post text has no home): only when Rafi asks; open for Rafi (new 1d line).
26. 272 (one open items list, with "later today 13 Oct" items): Part B items awaiting Rafi, none applied (new 1d line).
27. 273 (two credits, one lesson per topic, search before adding): news credit only on cards; step 8.4 searches first (new 1d line).
28. 274 (mistake record): show the real thing, a passed check is not a read (new 1d line).
29. 275 (V1 stitcher, clip runner, final encode): Rafi's PC (1e).
30. 276 (DRIVE_DIFFS out of date; lesson 238(4) against rule 1 joins the clash list): clash 7; 2d updated.
31. 277 (chain audit): Group 1 applied; Group 2 open, items 7, 11, 12, 13, 14 touch Part B, none applied (new 1d line).
32. 278 (step 0 order, yesterday_pool.csv): Part A (1e).
33. 279 (long jobs run_in_background): 1d line 77/101 rewritten.
34. 280 (helpers ran git status): Part B briefs say "never run git", not "not even git status" (2b; new 1d line).
35. 281 (the 13 Oct edition is missing): G17 sees 6 of 7 days, G2 compares with 12 Oct (3a item 9; new 1d line; open for Rafi).
36. 282 (build_pool wording): Part A (1e).
37. 283 (robotics in the Bulletin): Bulletin has 2 robotics stories today, a guideline of 3 to 5 (1d line 134/135 rewritten).
38. 284 (qa_check LEAK false positive): Part A (1e).
39. 285 (writers moved categories): Part A rule gap; the gate reads the entry's category (1e; 2e).
40. 286 (viral rule and follow-ups, C01-01): clash 6 (new 1d line).
41. 287 (window gap events): Part A rule question (1e; 2e); the 12 Oct events are follow-ups here (G6), so not cards.
42. 288 (backups next to the build's files): no `_old` copy in report_entries or facts (new 1d line).
43. 289 (Bigger Picture second reader found 30 small errors, all fixed): done in Part A (1d line 148/256 rewritten).

Skills, briefs, scripts, Drive
44. Part A SKILL.md (CHAIN FIX lines, sync_repo, editor pack and xhigh, Bigger Picture pack, 13.2 copy-to, 13.4 start Part B in the same turn): Part A (1e); Part B takes the "Working with Rafi" lines (45).
45. Part B SKILL.md "Working with Rafi": no questions the rules answer, never look stopped, lean main chat, helpers inside W. Met: this helper writes only in W; the main chat reads one line and CLASHES.
46. Part B SKILL.md description and Article_phrasing line: writers Opus normal effort; phrasing read once in the pack (rule 27). 1a lines rewritten.
47. Part B SKILL.md step 0: sync_repo.sh at resume; Pillow and fontTools from the hook (1c).
48. Part B SKILL.md step 0c incremental, helper launched with the picker: met; its 0c.3 defers clash stops to step 1 or 7: clash 8.
49. Part B SKILL.md step 1: pick_gate.py pack writes cards_work/prompt_picker.txt: met (file exists).
50. Part B SKILL.md step 2: effort "medium", story packs, rerun make_wording_prompts.py if selection.json changes, look after 10 minutes (1c).
51. Part B SKILL.md step 7: DAILY LISTEN first (1c; 2a item 27).
52. Part B SKILL.md step 8.2: delivery_manifest.py --part B --copy-to $W/for_rafi (1c); the stale 8.2 line of 2b is gone.
53. briefs/check_cards.md: story pack once, check 1b read aloud, Bigger Picture Bulletin text, never run git (1a).
54. briefs/check_headlines.md: story pack once (phrasing file, model lines, Master A, B, G and 15 Sep, entries and facts) (1a).
55. briefs/pick_stories.md: line 50 "never run git, never write in the repo folder"; its fun lines (7, 9-10, 40) and line 23 already follow rules 24 and 14 (2b).
56. briefs/rules_check_headlines.md: reads the story pack; still the superseded step 3b brief (2b).
57. briefs/rules_check_update.md (new): this task.
58. briefs/wording_common.md: story pack read once, DRAFT FIRST, never open code or run git (rule 27 line; line numbers in 2b moved by one).
59. briefs/wording_headlines.md: Master sections come from the pack, read once (rule 27 line).
60. scripts/make_wording_prompts.py: writes both story packs; the previous-run lookup is still scratchpad-only (2b).
61. scripts/pick_gate.py: pack fills prompt_picker.txt; G2, G4b, G11b and G18 are unchanged (clash 1 and clash 5).
62. scripts/rules_delta.py (new): wrote rules_delta.md and this prompt (1c).
63. Drive rule files (Cards, Headlines, prompt, phrasing, Full Report, Bulletin): no change since 12 Oct (delta section 4); STORAGE_STANDARD.txt in W/rules not in the delta.

## 1. One line per rule and lesson

### 1a. CLAUDE.md rules that touch Part B today
- Rule 0 TOP (Drive read only): Part B reads Drive only for the renderer zip and the cover base (setup) and writes nothing to Drive (rule 26). To verify at step 8: no Drive write in Part B. At 08:25 UTC products/ holds only Part A files; the cover is not built yet.
- Rule 0 DAILY DELIVERY: replaced for now by rule 26 (newest: Rafi uploads the final products and the pool files). Part B gives him the cards, the contact sheet and the JSON in chat; the text copy goes to runs/2026-10-14 by save_state.py. SKILL step 8.2 now matches rule 26 (delivery_manifest.py --part B --copy-to; the old Drive text is kept for later).
- Rule 0 WHO MADE IT: every file Rafi uploads carries _Claude-V1: delivery_manifest.py --part B --copy-to $W/for_rafi copies every card, the contact sheet and the JSON under those names (lesson 257, fixed 13 Oct). Part A's six files already carry the label (for_rafi, 6 files). To verify at step 8: the names of the files sent.
- Rule 1 (route the job): routes fixed (cloud: choice, wording, cards, JSON; Rafi's PC: ComfyUI, stitch, Drive upload by hand). No open route.
- Rules 2, 15, 8b item 5 and rule 24 HOW CLAUDE EXPLAINS: one or two short sentences, simple words, "like I am six years old". Evidence: the step 1 list message and the step 7 one-line ask.
- Rule 3: superseded files renamed _old, a new cards_runN per render, the fill refuses to overwrite, never rm (lesson 230). Evidence: ls of W at step 8.
- Rule 4: Rafi's edits at steps 1 and 7 applied and shown one at a time.
- Rule 5: numbers as evidence: card files counted against cards_copy.json (assemble_cards.py), JSON bytes and md5, active slots, seconds, longest clip, news part (verify_headlines.py). To verify at steps 5 and 6.
- Rule 6: every card and clip fact from report_entries/<id>.json and facts/<id>.json, read once in the story pack (rule 27); the Fable checkers check every fact (check 3 of check_cards.md, check 4 of check_headlines.md). To verify at step 3: 0 open fact problems in cards_work/check_result.json and headlines_work/rules_result.json. No CP- item today.
- Rule 7: Claude does not judge the look; the contact sheet goes to Rafi first.
- Rule 8: an instruction Rafi gives during Part B goes into CLAUDE.md the same day, in his words (rule 20).
- Rule 8a: 8 clashes in section 2 (4 new today), none chosen or applied; 2a lists the touches Rafi's own precedence lines settle, each with the line that settles it.
- Rule 8b item 1: no fix of section 2 runs before Rafi picks it.
- Rule 8b item 2: no brief may carry a rule's opposite: 2b lists stale brief lines; the fun lines of pick_stories.md (7, 9-10, 40) now follow rule 24; its line 10 (Fable writes the Bigger Picture) and line 27 stay stale and do not block the choice.
- Rule 8b item 3: before Rafi sees the deck: the 0c.4 PASS/FAIL table, G17 over the 6 decks that exist (7 to 12 Oct, 48 to 51 lines a day in pick_pack.json; 13 Oct is empty, lesson 281), and the 3-day name and topic table (section 3c; G17 cannot see 13 Oct).
- Rule 8b item 4: counts and orders he gave: 14 story cards (the Bulletin gives 17 within the limits, so clash 1 sleeps; Politics and Research have no new Bulletin story: clash 5 and 3a), 7 clips, 2 robotics cards with one humanoid (3a item 8), 1 robotics clip, Politics clip 1 (clash 5); say how each was met.
- Rule 8b item 6: every named person with position and organisation. Names in today's pick pack: Geoffrey Hinton (Nobel prize-winning computer scientist, often called a godfather of AI) and Jensen Huang (Nvidia chief executive) in C05-02; Sir Ken McCallum (director general of MI5, Britain's domestic security service) in C12-03; Liam Booth-Smith (Anthropic's head of Europe) and Tom Duff Gordon (an OpenAI vice president) in C13-03; Kamala Harris (former US Vice President, reserve C05-07); Mark Zuckerberg (Meta chief executive, fun C16-02); Austan Goolsbee (president of the Federal Reserve Bank of Chicago, follow-up C05-05, not a card). Evidence: G15b novice_test, checker check 2.
- Rule 8b item 7: one check round and one fix round (rule 25, SKILL step 3); what stays open: clash 2.
- Rule 9: the skills only on branch claude/eager-archimedes-ajnex3; no PNG, MP4 or ComfyUI JSON in git (save_state.py copies text only).
- Rule 10: no brand mark on any screen line; fill PROMPT (fill_headlines.py line 18) says "No readable words, numbers or logos".
- Rule 14 COUNTS: the card target is a working target (clash 1 sleeps today). The Bulletin holds 48 stories (45 plus 3 Fun), inside the 30 to 50 guideline (bulletin_pdf.json): Part A's delivered product, not a Part B gate.
- Rule 14 BULLETIN SECTIONS NEVER EMPTY (0c.4 recheck): 11 of 11 sections hold stories (bulletin_pdf.json): Politics 1 (C05-01, score 9; the rule asks for exactly 2 only when a category has none at 7 and up), Research 2, Robotics 2, Fun 3. PASS.
- Rule 14 Full Report 100 to 120: the pick pack lists 104 report stories (48 Bulletin plus 56 report-only); the report's own count and cutoff are Part A's delivery numbers, checked at 0c.4 from products/report_pdf.json (not read here).
- Rule 16 Fun Side: the pick pack lists 6 fun stories (Bulletin: C16-01, C16-02, C16-05; report-only: C16-06, C16-07, C16-09); the Bulletin holds the top 3. The report's own Fun Side count (5 to 10): verify at 0c.4.
- Rule 16 cards and clips: story cards by the CARD FILTER (target 14, clash 1), 7 into Headlines. Evidence: gate_result.json G2.
- Rule 16 news part about 90 s (now with rule 22's aims). Evidence: check_wording.py "news part" line, verify_headlines.py "news part". To verify at step 6.
- Rule 16 round up to the next half second: fill_headlines.py box_seconds and its node 13 assert (line 151). Evidence: the fill slot table.
- Rule 16 company limits (3 cards, 2 clips): G9, G10, check_headlines_rules.py C16. Crowded names among today's 32 eligible stories (pick pack companies field): Anthropic 7 (C02-01, C03-01, C06-01, C09-05, C12-01, C13-01, C13-03), Nvidia 4 (C03-02, C05-02, C06-04, C07-04), Google 3 (C01-01, C02-03, C13-03). The paper draft already puts Anthropic on 3 cards (C06-01, C12-01, C13-01, the limit) and 2 clips (C06-01, C12-01).
- Rule 16 READER LEVEL (rule 27 replaces "re-read before each item"): cards level 6, Headlines level 5 with rule 22 and the 11 Oct level (rule 24); each writer and checker reads the phrasing rules once, inside its story pack (make_wording_prompts.py writes cards_work/story_pack.md and headlines_work/story_pack.md), and goes through each item once against the hard rules. Evidence: wording_common.md line 10 and the phrasing-file override in both writer prompts.
- Rule 16 CLIP SECONDS (points to rule 22): aim 8 s, 10 acceptable, 12 the hard limit. Evidence: check_wording.py FAIL over 12 (line 112), check_headlines_rules.py B1, fill assert (line 95), verify_headlines.py (12).
- Rule 16 CREDIT: the card SOURCE line is the entry's source as written (build_cards_copy.py line 37); "X reports, citing Y" when the article credits another outlet; the Bigger Picture card says AIND and AI News Desk; the news credit and the footage credit are two credits (lesson 273; no footage today). Sources named in the pack summaries: C06-01 "CNBC, citing two people familiar", C06-02 "The Standard of Hong Kong, citing mainland Chinese media it does not name", C07-02 "CGTN", C01-01 "The Verge", C02-01 "Mashable", C05-02 and C12-01 "The Guardian", C13-01 "Reuters", C13-03 "WIRED", C11-03 "Agility Robotics, in a Business Wire release" (the company's own release). To verify at step 7: every SOURCE line on the sheet.
- Rule 16 WRITE ONLY WHAT CAN PRINT: cards only from written entries. PASS by construction.
- Rule 16 REPLY STORIES: C05-02 (Hinton answers Nvidia chief Jensen Huang, who said Hinton's predictions had all been wrong) is a reply: card and clip must name Huang's earlier claim and who made it; check_wording.py's reply test fires only on the pool's follow_up flag (the pack shows C05-02 as NEW), so both checkers must check it. The reply follow-ups C05-04 (Musk answers Broadcom's chief), C05-03 and C05-01 are not cards (G6). Evidence: check_result.json, rules_result.json.
- Rule 16 HEADLINES RULES RECHECK: check_headlines_rules.py (rules_check.json fails 0) and the Fable checker's rules_result.json on the CURRENT lines (common_b.rules_gate). Introductions: the previous day is 13 Oct, whose lines are not in the repo (lesson 281), so PREV_LEADINS and G2 compare with 12 Oct only; see clash 3. Nothing with a rules FAIL: clash 2.
- Rule 16 MODEL POLICY with STORY CHOICE and rules 25 and 27: picker Fable; writers Opus on normal effort (effort "medium" in the Agent call); checkers Fable at high; this rules-check helper, the main session and setup on Sonnet; never Haiku (lesson 277: the 13 Oct main chat ran on Haiku after a switch in the app: verify this chat's model). Evidence: the model of every Agent call; helper tokens per stage next to 4 and 5 Oct and 12 and 13 Oct.
- Rule 16 STORY CHOICE: one Fable picker (briefs/pick_stories.md; pick_gate.py pack writes its prompt to cards_work/prompt_picker.txt), pick_gate.py gate PASS or a named override (the gate has no override file: selection.json is written only on PASS, lesson 267 item 3), Rafi approves the list before any wording. Evidence: gate_result.json, his message.
- Rule 16 BIGGER PICTURE MODEL and WEIGHT: card and clip from bigger_picture_bulletin.json (531 words in the Bulletin; rule 29 says 300 to 500: Part A's product, one line to Rafi): Korea's chip sell-off (main index down more than 6 percent), ASML unable to meet 2027 and 2028 demand, Anthropic's investor meeting on 14 Oct, Microsoft's reported cost cuts (disputed); dated watch items (Thu 15 Oct TSMC; Wed 21 Oct Meta; 27 to 28 Oct the Fed; 28 Oct Alphabet and Microsoft; 2 Nov the Agility Robotics merger vote; SK hynix 27 Oct and Samsung 29 Oct reported, not confirmed; the September US inflation figure on 14 Oct not confirmed); the Bulletin text carries "not financial advice"; card and clip voice and screen must carry it (check_wording.py, verify_headlines.py). Who writes card and clip: clash 4.
- Rule 16 SCRIPTS STAY AS THEY ARE: no script change during the run except for a rule Rafi gives during the run, after his yes to the exact edit list (line 160). Evidence: git diff of scripts/ empty at the end.
- Rule 16 HEADLINES SHAPE: points to rule 22 and the model lines file. See rule 22.
- Rule 16 WHO WHAT WHY FIRST: who, what, why_for_people filled for every story and the fun clip (check_wording.py line 109 fails a missing one); failing lines go back to the same writer (rule 25); Rafi's words locked (rewrite_request.json "locked"); build_pack.py and review_list.py stop unless check_wording.py, check_headlines_rules.py and rules_result.json are newer than scripts_final.json.
- Rule 16 HEADLINES ORDER: Drive A3 for the six non-Politics clips; Politics clip 1 is NOT settled today (clash 5).
- Rule 16 HEADLINES INTROS AND FLOW: each introduction names its own topic, in a natural order, never twice in the reel, never an unlinked label; among non-Politics clips prefer AI affecting people over war; the fun clip per rules 24 and 29; every clip generated except slots 1, 12 and 13.
- Rule 16 REAL TV SCREENS, PHOTOREALISTIC, FUN CLIP: each screen a photorealistic TV news scene of its story, no readable words, numbers, logos or real named faces; the Bigger Picture keeps its warning sign; fun clip facts only from its source entry. Evidence: fill PROMPT line 18; the Headlines checker's screen findings.
- Rule 16 NO OLD NEWS: cards and clips only from the report after step 9b (held ids are refused by G1; held.json is read at 0c.4). PASS by construction. No exception today (rule 23 was for 12 Oct only).
- Rule 16 CARD FILTER and the CARD_FILTER line (base_min 5, extra_min 7, target 14, 2 per category, market 3, company 3 cards and 2 clips; pick_pack.json filter agrees): order from Drive Cards Master 2.4 (11 categories); no score 10 (top is 9: C01-01 Models, C05-01 Politics); Politics and Research have no new eligible Bulletin story (3a items 3 and 4); extras below 7 settled (2a item 1); a robotics card shows a machine doing something (both Bulletin robotics stories are flagged machine_action false: 3a item 8). See clash 1 (sleeps) and clash 5.
- Rule 16 CARDS FROM THE BULLETIN: 48 Bulletin stories, 45 non-fun, 32 NEW and read in full (11 follow-ups, 2 headline only), 17 within the category limits: Market 3 of 7, Security 2 of 4, Energy 2 of 4, Robotics 2 of 2, Models 2 of 5, Ethics and law 2 of 3, Health 2 of 4, Society 2 of 3; Politics 0 and Research 0. Evidence: G4.
- Rule 16 NO UPDATE CARDS: none named (no update_allowed.json); the 11 Bulletin follow-ups are not cards, clips or teaser items (G6): C02-02, C04-02, C05-01, C05-03, C05-04, C05-05, C07-01, C08-02, C08-03, C09-03, C14-03. C01-01 is labelled NEW but follows the 9 Oct card (clash 6). The 3-day name and topic table goes with the deck at step 7 (section 3c).
- Rule 16 NO REPEATS IN 7 DAYS: decks of 7 to 12 Oct present; 13 Oct is empty in pick_pack.json (lesson 281), so G17 cannot see what ran on 13 Oct. By my read of the last_7_days lines the gate or the 3-day table will meet: C01-01 (Gemini 4 Argon, card and clip 9 Oct), C05-02 (Hinton, card and clip 7 Oct; a different story today), C06-02 (DeepSeek, 12 Oct lines), C07-02 (the IMF report watched on 12 Oct), C13-01 (Pentagon and Anthropic, 6 Oct card). Evidence: gate_result.json G17 plus the section 3c table.
- Rule 16 THE REPO IS THE SOURCE OF TRUTH: a CLAUDE.md line beats a Drive line; differences belong in docs/DRIVE_DIFFS_FOR_CHATGPT.md (2d).
- Rule 16 PEOPLE WITH THEIR POSITION: as 8b item 6.
- Rule 16 HEADLINES START WITH POLITICS: the Bulletin's only Politics story, C05-01 (Trump on the AI warnings, score 9), is a follow-up of 12 Oct (no card, G6); the only new Politics story is C05-07 (Harris in Seoul, report only). A Politics card makes a story outside the Bulletin clip 1 (G11b against G4b): clash 5.
- Rule 16 VIRAL RULE: done in Part A (viral.json not read here; no re-run). The clause for earlier runs below 7 does not free C01-01, which ran at 10 (1 Oct) and 9 (9 Oct): clash 6.
- Rule 16 ONE TOPIC, ONE CARD: no gate test (lesson 161); today C06-03 (Market) and C14-15 (Society) are the same Character.AI bankruptcy and Disney licence in two entries: one card or a stated reason; C05-03 and C05-04 are replies in one argument about AI spending (follow-ups, no cards); every card pair checked before Rafi sees the deck.
- Rule 16 ROBOTICS: Bulletin 2 (C11-01 Tesla robotaxis and the school-zone speed petition; C11-03 Agility Robotics, maker of the Digit humanoid, merger with a blank-check firm), below the 3 to 5 guideline (lesson 283; counts are guidelines, rule 14); cards 2 with one humanoid = both, each needing a robotics_ruling because the pack flags machine_action false for both (G13); report-only robotics C11-05, C11-10 (20 humanoids cleared in South Korea) and C11-14 (Astribot funding) cannot be cards while the Bulletin has eligible robotics stories (G4b exception); Headlines 1 robotics clip (B2: say what the robot or vehicle does).
- Rule 16 ROBOT WAR LIMIT: Bulletin at most 2, Full Report at most 3 (Part A's count). The 2 Bulletin robotics stories are Tesla robotaxis and Agility's Digit: no robot war story; C12-03 (MI5 on AI-aided drone attacks) is Security. No limit on cards. Verify the report count at 0c.4.
- Rule 16 BEFORE EVERY STAGE: this file is the read of step 0c.
- Rule 16 HEADLINES GENERATION: 8 steps, AIND_anchor_voice_sample_4s.wav, the unhurried tone. Evidence: fill CONFIG line; verify_headlines.py "steps 8" and "tone in N of N".
- Rule 16 APPROVED OPENING AND ENDING: assets/pack_base.json slots 1 and 13 "bypass" (checked); check_headlines_rules.py A2.
- Rule 16 QA GAPS: the built checks run, in rule 25's shape.
- Rule 17 BIGGER PICTURE CORNER: card head the market summation, body what happened and what to watch (4 lines, notice stays); clip 10 s (rule 22: 10 acceptable); never a vague restatement: the 12 Oct text told readers to watch the IMF report on Tuesday and AI debt led the card on 4, 5, 7, 8, 11 and 12 Oct; today's turns on Korea's sell-off, ASML's supply limit, Anthropic's investor day and the disputed Microsoft cost cuts.
- Rule 18 FRESH CHAT: Part B continues in Part A's chat (rule 9; 2a item 9; lesson 277 Group 2 item 12 "Part B in a fresh chat" is open for Rafi); a compacted chat continues only with Rafi's yes.
- Rule 20: one question at a time; when he asks for the list, the list itself; rules only in his words; his exact complaint first; ORDER NEVER CHANGES (G7).
- Rule 21: lessons of this run into docs/V1_TASKS.md (step 8.4); a handoff is not a source; never touch the Drive EXPERIMENTS file.
- Rule 22 HEADLINES STRUCTURE: one sentence after the introduction, who did what and why (a company reason or a careful guess is a why; the end part only if it adds weight); aim 8 s, 10 acceptable, 12 the hard limit; the model lines file read by writer and checker (wording_headlines.md line 12, check_headlines.md line 3). Scripts test only the length; the one-sentence shape rests on the checker (check_wording.py counts no clip sentences): to verify at step 7 by counting sentences after the introduction in scripts_final.json.
- Rule 23 FUN CLIP: named for 12 Oct only (Apate); no CP- story is named for 14 Oct, so step 0b is skipped and headlines_fun is a pool fun story chosen under rule 29 FUN CLIP CHOICE. G4b applies to it (it must be in the Bulletin: C16-01, C16-02 or C16-05).
- Rule 24 CARDS IN GROUPS OF 10: step 8.1: 10 files a message in deck order, the contact sheet with the last group, the JSON alone.
- Rule 24 HEADLINES ITEMS MUST BE IN THE REPORTS: G4b (every clip id in the Bulletin and the report; only CP- ids are exempt); story clips come from Bulletin cards, so a reserve-exception card can never be a clip. This bites Politics today (clash 5).
- Rule 24 FUN STORIES: funny, or fun to hear, see or experience, or mildly cynical and funny to think about, never sad; pick_stories.md now says so (lines 7, 9-10, 40). Today's Bulletin fun stories score 3, 3 and 2: C16-01 (OpenAI's always-on dot assistant used over 300,000 tokens a day with no prompts; "token" is a banned word, so the line needs another way to say it), C16-02 (Zuckerberg winces at a pint of Guinness on a podcast), C16-05 (an AI-made film of a theft at the Ballon d'Or gala).
- Rule 24 HEADLINES LEVEL IS A CONSTANT: the 11 Oct lines (model lines file "The level": about 22 words, one sentence, one actor, one verb, one why).
- Rule 24 NO TIME PRESSURE ON THE TEST: DECIDED 13 Oct ("yes exactly!"): the length wording of rule 22 (aim 8 s, 10 for a long item, 12 the hard limit) and the model lines file stay as they are. Closed.
- Rule 24 "too complicated to explain in one sentence": such a story is not a clip. Test before choosing: C05-02 (Huang's claim and Hinton's answer) and C13-01 (the court ruling and the Pentagon's supply chain label) each need two facts in one sentence.
- Rule 24 "not funny but definitely fun": fun counts (FUN STORIES).
- Rule 25 ONE WRITER AND ONE CHECKER PER PRODUCT: checkers Agent model "fable", effort "high"; each checker reads its story pack once; the same writer fixes once; then Rafi sees what is left. Rule 27 replaces "at max" for the writers (next lines). make_wording_prompts.py still writes the old stranger, rules and rewrite prompts: not launched.
- Rule 26 VIDEO WORK AND FOOTAGE: footage and the video lessons 238 to 244 apply on the PC, not to the JSON; DRIVE UPLOAD by Rafi: no Drive agent at step 8; send only the final products (cards, contact sheet, JSON).
- Rule 27 WRITERS FASTER (new; Rafi, 12 Oct): the card writer and the Headlines writer are Opus on normal effort (effort "medium" in the Agent call, SKILL step 2) and read one pre-loaded story pack once; they save a full draft first, write everything in one pass, go through each item once against the hard rules, run the check scripts once and fix once; the checkers read the pack once. Part A writers unchanged. To verify at step 2: whether the Agent tool takes the effort value (lesson 266: the docs do not say). To measure: writer minutes and tokens (target 2 to 3 minutes; 12 Oct: 25.6 and 21.9) and whether the checkers fail more lines (12 Oct: Headlines 0 fails, cards 3 of 21).
- Rule 28 DAILY HEADLINES LISTEN (new; Rafi, 12 Oct, "I want it every day"): at step 7, before the review list, the spoken lines of every Headlines clip go into the chat as plain text in one message ("Clip one. ...", fun, teaser and Bigger Picture named, no file, no symbols, A I and U S as the clip says them); the Fable check of step 3 stays as well ("For now, we keep both"). To verify at step 7: the message exists and matches scripts_final.json word for word.
- Rule 29 FUN CLIP CHOICE (new; Rafi, 13 Oct): Claude gives Rafi the fun concept and he says if it is funny; the goal is that Claude later chooses alone. Today's concept comes with the step 1 list (candidates: C16-01, C16-02, C16-05, all Bulletin stories, 1a Rule 24 FUN STORIES); G4b needs the fun clip in the Bulletin.
- Rule 29 MISTAKES NOT AGAIN (new; Rafi, 13 Oct): the card checker has the read aloud test (check 1b of check_cards.md); Claude always shows Rafi the real lines, cards or files, never a description (lesson 274). To verify at step 3 and 7: check_result.json has a 1b verdict per card; the step 7 message holds the lines themselves.
- Rule 29 BIGGER PICTURE IN THE BULLETIN (new; Rafi, 13 Oct): "300-500 words is fine for now", "stick to whats necessary". Today's Bulletin text is 531 words (bulletin_pdf.json, 31 over): Part A's product, one line to Rafi, not a Part B gate.
- Rule 29 ARTICLE (new; Rafi, 13 Oct): "article" means any item, a Headlines line, a card or a full entry; ask which one only when it matters.
- Rule 29 LESSONS FOR THE REPO (new; Rafi, 13 Oct): the local chat ends its answers with LESSONS FOR THE REPO; Rafi passes the list to this chat, which writes each lesson into docs/V1_TASKS.md once (search first, lesson 273). Step 8.4 does the same for this run.
- Rule 29 TWO CHATS (new; Rafi, 12 Oct): this cloud chat runs Part B up to the JSON; the local chat on his PC does ComfyUI and the stitch. Nothing in Part B changes.

### 1b. Drive rule and structure files (only lines that touch Part B; "settled" = a CLAUDE.md line or a newer ruling wins)
- The six Drive rule files and STORAGE_STANDARD.txt are unchanged since 12 Oct (rules_delta.md section 4: "no change"); the lines below were rechecked only where today's facts differ.
- Cards Master order block and 2.4: deck order Politics, Market, Security, Energy, Robotics, Models, Research, Ethics and law, Health, Society, Fun. Evidence: G7. The fixed slots are replaced by the CARD FILTER (settled).
- Cards Master filename rule: local cards_14-10-26_INN_VL1.png; _Claude-V1 on the names Rafi uploads (settled, rule 0 WHO MADE IT).
- Cards Master 1.1: one 1080x1920 PNG set plus one combined image (the contact sheet). Evidence: assemble_cards.py sizes line.
- Cards Master 1.3 and 3.5 DESK VIEW: the Bigger Picture card says AIND (settled, CLAUDE.md CREDIT).
- Cards Master 1.4 and 2.5: the "More in the full report" card holds report headlines with no story card; the reel teaser draws only from it. Evidence: G12, check_headlines_rules.py A5.
- Cards Master 2.1 to 2.3: cover first; criticals spend their slot (no score 10 today).
- Cards Master 2.6: aim 15 (settled: 14); robotics and fun normally required.
- Cards Master 2.7: at most 3 money cards. Evidence: G8 (7 eligible Bulletin Market stories for 3 slots: C06-01, C06-02, C06-03, C06-04, C06-05, C07-02, C07-04).
- Cards Master 2.8: full report only (settled: from the Bulletin).
- Cards Master 2.9: robotics = a machine doing something (settled: humanoid funding also counts). Evidence: G13.
- Cards Master 2.11 and 2.12: no sales language, no link on cards; the closing text of 12 Sep (build_cards_copy.py CLOSING).
- Cards Master 2.14: reel order follows deck order. Evidence: G11, check A3.
- Cards Master 3.1 to 3.4: phrasing file governs; lead with the deed, not the money; unfamiliar companies titled (candidates today: DeepSeek, Agility Robotics, ASML, Character.AI, OpenEvidence, Kroger, Applied Materials, NTT Data).
- Cards Master 3.6 and 3.7: approved text never cut for layout; Rafi approves at step 7.
- Cards Master 4 to 6: the renderer package (md5 598989503fa221cebe87c04bac903854) owns colours, fonts and the Instagram window; cover = approved cover with the new date (to make today with make_cover.py).
- Cards Master 7.1, 7.4, 7.7, 7.8: Drive account and saving: not live today (rule 26, settled).
- Cards Master 7.15 and 7.16: contact sheet first at step 7; every card its own PNG, never a zip; groups of 10 (rule 24, settled).
- Headlines Master order block, A3, A7: stories in deck order, then fun, teaser, Bigger Picture, ending (build_pack.py).
- Headlines Master A1: twelve-slot template (settled: 13 slots).
- Headlines Master A2 and 15 Sep 5: stored intro bypassed; ending wording = pack_base slot 13 text; the option 4 clips of 3 Oct are used (settled).
- Headlines Master A3: seven card stories in deck order, normally robotics plus law, research or society (today's Bulletin gives law C13-01, C13-02, C13-03, society C14-01, C14-15, robotics C11-01, C11-03; research has no eligible Bulletin story).
- Headlines Master A4: slot 9 is the deck's fun item (settled: rule 23 was 12 Oct only; today the fun item follows rules 24 and 29).
- Headlines Master A5, A6, A8: teaser only from the teaser card; Bigger Picture in slot 11 opening "And for the bigger picture"; about 90 s of content.
- Headlines Master B1 and B1a: aim 8 s, 12 s maximum (same as rule 22); two decimals, no rounding (settled: round up, rule 16).
- Headlines Master B2: Cards Section 3 words; the robotics clip says what the robot or vehicle does (C11-01: Tesla's driverless taxis exceed the speed limit in school zones; C11-03 is a listing step, so say only what Agility does).
- Headlines Master B2a: every story and fun clip opens with an introduction; teaser "Also in the full report." (full stop); Bigger Picture "And for the bigger picture". Evidence: check B2a.
- Headlines Master B3: numbers as words, no digits. Evidence: check B3 and check_wording.py.
- Headlines Master B2 (prompt) and the prompt file: text-free screen, "nothing else changes" (settled: REAL TV SCREENS and the tone line).
- Headlines Master C: references 1 hands-on-table and 2 fists (fill asserts the 29 Sep pair); every visible field overwritten; titles start "WED 14 OCT 2026"; slot table and stale word scan; mirrors written; JSON to Rafi as a file, never zipped; six steps (settled: 8).
- Headlines Master G1.1 and 15 Sep 1: cues only where spoken (N-vidia if Nvidia is spoken, an-thropic if Anthropic is: 7 eligible stories name Anthropic); 15 Sep 2: "Google DeepMind".
- Headlines Master G1.2: a two to three word tag for a company under 100 billion dollars (DeepSeek, Agility Robotics, Character.AI, OpenEvidence, Kroger; Palantir if unsure).
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
- Full Report and Bulletin 5.3 and 11.4 (the headline-only note): settled for customers by Rafi's 8 Oct ruling (lesson 118, newest); the Bulletin holds 2 headline-only stories (C01-02, C04-01); whether each carries the note, and the report's count: verify at 0c.4 (Part A's products, one line to Rafi, not a Part B gate).
- Full Report and Bulletin 6.1 and 6.2 (publisher named, direct link): 0 Google News links in the 48 Bulletin stories (bulletin_pdf.json, 37 different hosts, counted); the report: verify at 0c.4.
- STORAGE: its label lines now say _Claude-V1 (11 Oct 18:30), the same as rule 0; Part B saves nothing to Drive today (rule 26).

### 1c. Part B skill steps (process rules of this run)
- Step 0 setup: sync_repo.sh at resume (Part A step -1; the SessionStart hook runs it by itself), renderer zip and cover base (Drive, read only), Pillow and fontTools from the hook. Step 0.1 rules_diff: replaced by rules_delta.py (delta section 4: the Drive rule files are unchanged since 12 Oct). The cover is not built yet.
- Step 0b: not needed today: no Rafi-named fun story for 14 Oct (rule 23 was 12 Oct only); the fun clip follows rule 29.
- Step 0c: this file (incremental, launched with the picker; the main session reads the one line and CLASHES only, never the lessons file whole); the 0c.4 PASS/FAIL table per section before step 7.
- Step 1: Fable picker (prompt written by pick_gate.py pack to cards_work/prompt_picker.txt), pick_gate.py gate PASS or a named override (no override file, lesson 267), Rafi approves the list before wording; the LEFT OUT list and the fun concept (rule 29) go with it; clashes 5 and 6 are put to him there.
- Step 2: make_wording_prompts.py with --prev-pack /home/user/ai-news-desk/runs/2026-10-12/headlines_work/headlines_12-10-26_pack.json --prev-cards /home/user/ai-news-desk/runs/2026-10-12/cards_copy.json (2b); it also writes both story packs; two Opus writers (effort medium) in one message; draft first; rerun it if selection.json changes; a look after 10 minutes.
- Step 3: two Fable checkers (high) read their story pack once; one fix by the same writers; one confirm of the changed items; what stays open goes to Rafi marked (clash 2).
- Step 4: merged into step 3 (12 Oct).
- Step 5: cover, cards copy, render into a new cards_runN, assemble (stops on a refused card).
- Step 6: build_pack.py (gate), fill_headlines.py (refuses to overwrite), verify_headlines.py.
- Step 7: DAILY LISTEN first (rule 28: the spoken lines of every Headlines clip as plain text in one chat message), then review_list.py (gate), save_state.py, the sheet and the list to Rafi, STOP.
- Step 8: after approval: groups of 10 in chat, the JSON alone, the voice sample line; delivery_manifest.py --part B --copy-to $W/for_rafi gives the _Claude-V1 names (no Drive agent, rule 26); save_state.py (pulls before it pushes); short report; lessons into docs/V1_TASKS.md (search first, lesson 273).

### 1d. Lessons that touch Part B today
- P1-3 Fun Side 5 to 10, top 3 in the Bulletin: 6 fun stories in the pick pack, 3 in the Bulletin. PASS (report count at 0c.4).
- P1-4 cutoffs stated: Bulletin 48 (pool score 7 and up, Health and Society from 6, plus the top 3 Fun; purpose line in words); the report's cutoff and count are in Part A's delivery message (verify at 0c.4). 48 is inside the 30 to 50 guideline.
- P1-5 everything final to Drive, else to Rafi: rule 26 (Rafi uploads) for now.
- P1-6 story cards 14 to 15, company 2 clips and 3 cards, money cards 3, a headline-only story never a card: G2, G9, G10, G8, G5 (C01-02 and C04-01 are headline only; count: clash 1 sleeps).
- P1-7 news part about 90 s, round up: check_wording.py total, fill table (to verify at step 6).
- P1-8 hologram border: the fill PROMPT keeps the blue border line; the opening is stored.
- P1-9 only the spoken words when he asks for the stories in the JSON: review_list.py.
- P1-10 one file at a time: replaced by groups of 10 per message (rule 24); never a zip stands.
- P1-11 one home per rule: section 2 lists the double homes.
- P1-16 check the approved opening first: option 4 stored, slot 1 bypass.
- P1-17 never build before Rafi's yes: no wording before the list approval, nothing sent before the step 7 approval.
- P1-19 stop at a compaction: rule 18.
- P1-20 match his numbered answers against the original list: at steps 1 and 7 and on the clash answers.
- P1-21 never drop a category silently: Politics and Research have no new eligible Bulletin story (3a items 3 and 4); a skip needs left_out_notes, a reserve card needs "exception": true with a reason.
- P1-22 no old JSON in a package; no unapproved screen wording: fill refuses to overwrite; screens go to Rafi in the review list.
- P1-27 uploads verified by size: no Claude upload today (rule 26).
- P1-29 meaning check before any JSON leaves: gate before step 7; no JSON before approval.
- P1-31 compute weekdays: 14 Oct Wednesday; 13 Oct Tuesday, 15 Oct Thursday, 16 Oct Friday, 21 Oct Wednesday, 27 Oct Tuesday, 28 Oct Wednesday, 29 Oct Thursday, 2 Nov Monday (computed with python).
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
- 29 follow-ups never a card; follow-ups in the teaser fail G6: today 11 Bulletin follow-ups (3a item 5); the paper draft's teaser holds C05-01, C05-03 and C08-02.
- 30 Drive rules change between runs: rules_delta.md section 4: no change since 12 Oct.
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
- 50 a reply names the earlier story: C05-02 (Hinton answers Huang); the script test may miss it (the pack shows it as NEW).
- 56 Market labels about 10 characters: the Market category name is long (build_cards_copy.py warns over 46 characters).
- 59 the one lessons list: step 8.4.
- 60 intros rotate, company tags: check G2 and the checker's G1.2 (clash 3).
- 61 hard gate on the current lines: common_b.rules_gate in build_pack.py and review_list.py.
- 62 token cost: report helper tokens per stage.
- 63 stored opening and ending: pack_base both bypass.
- 64 voice file .wav, teaser full stop, Kawa saki cue: fill AUDIO, check B2a, cues.
- 66 old news in cards: cards only after step 9b plus the 7-day check.
- 67 "no company twice in a row" (Rafi to confirm; not in CLAUDE.md): note only (Anthropic is on 3 cards and 2 clips of the paper draft).
- 68 and 80 one event in several entries: C06-03 and C14-15 (the Character.AI bankruptcy).
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
- 107 and 221 which score counts: the pool score (Rafi's ruling); pick_gate.py reads the writer's score (2b): 6 of 11 categories differ today.
- 108 the automatic repeat match is a list to judge: G17 hits judged in 3c (expected: C01-01, C05-02, C06-02, C07-02, C13-01).
- 111 the markets quarter cap does not bind the Bigger Picture corner: rule 17.
- 114 change only what was asked; 115 show first, then act; 116 count the rounds per product; 117 check a figure before passing it on.
- 118, 119, 179, 190 customer text: 0c.4 recheck only (2 headline-only Bulletin stories today; the note and the report count are verified there); no fluency rewrite.
- 121 compare old and new facts of every fixed item: the checker's confirm round against the writer's first file.
- 122 the contact sheet by display render, files by attach.
- 123 Part B in a new chat: 2a item 9.
- 124 the restart copy is text only; 125 commit and push after every change.
- 126, 173, 208, 257 commits carry no model name, only the Claude-Session line.
- 127 estimate an agent's cost before running it; 128 answer first, act after he asks.
- 129 scripts unchanged during the run (rule 16 line 160 exception only with his yes).
- 131 step 0c before any choosing script: replaced for this run by the incremental design (lessons 262 and 272b, Rafi's yes of 13 Oct): the check runs with the picker and the picker does not wait; selection_draft.json and pick_pack.json (08:14) are paper input, nothing is chosen (2a item 25).
- 134 and 135 robotics counts (Bulletin 3 to 5, cards 2 with one humanoid, Headlines 1, one extra allowed): Bulletin 2 (lesson 283, a Part A script limit; a guideline); cards C11-01 and C11-03, each needing a robotics_ruling; one robotics clip.
- 136 one Bulletin file: products/bulletin_pdf.json (48 stories = the delivered Bulletin). PASS.
- 137 and 158 the freshness flag does not know earlier decks: C01-01 says NEW but ran as a card and clip on 9 Oct; C05-02 (Hinton, 7 Oct card) and C13-01 (Pentagon and Anthropic, 6 Oct card) may touch earlier cards; C07-02 follows the 12 Oct Bigger Picture watch.
- 138 a picker note is not a source: writers use entries and facts only.
- 139 the robotics clip says what the machine does: C11-01's summary does (robotaxis speed in school zones); C11-03 is a listing step (Agility's merger vote), so the clip says what the company does.
- 140 and 199 realistic screens: fill PROMPT updated (lesson 209); one stale brief line (2b).
- 141 screens static and wordless.
- 142 list every clash once: settled by rule 20 (2a item 10).
- 144 and 258 helper tokens per stage: report Part B's.
- 147 held stories are never cited: G1, G16.
- 148, 256 and 289 the Bigger Picture author (Fable max) and the second reader (Opus, one pass over bp_reader_pack.md) ran in Part A; the reader found 30 small errors, all fixed and confirmed by grep (lesson 289); unconfirmed dates stay marked "not confirmed" in card and clip (SK hynix 27 Oct, Samsung 29 Oct, US inflation 14 Oct).
- 150 Bulletin cover in words: the purpose line names no codes. PASS.
- 154 no empty Bulletin section: PASS.
- 156 lock the report list: Part B never rebuilds the products.
- 161 two cards on one topic: the Character.AI pair (C06-03, C14-15); manual check.
- 162 Rafi's list changes meet the gate: gate_overrides.json names each overridden line and his words (clash 1).
- 171 and 174 viral stories by reach: done in Part A (viral.json not read here).
- 175 rule text only in his words: section 2 fixes are marked mine.
- 177 and 178 the approved order for every product: G7 for the deck.
- 180 the six clashes of 10 Oct: four settled (2a items 1 to 5), one not live (2c), one carried (clash 2).
- 182 a viral floor only after checking earlier editions: Part A's step, not re-run here (viral.json not read).
- 183 link a follow-up by url and title, not a per-day id: when a card names an earlier story.
- 186 a CLAUDE.md copy loaded at session start goes stale: today the context copy and the disk file agree (317 lines, both end at rule 29 FUN CLIP CHOICE); helpers still read the disk file.
- 188 thin fun search: Bulletin fun stories score 3, 3 and 2 (C16-01, C16-02, C16-05); rule 24 widens the fun test.
- 191 and 192 search before saying a robot story is missing: the humanoid story exists (C11-03; Astribot funding C11-14 and South Korea's 20 humanoids C11-10 are report-only).
- 193 robot war counted: Bulletin at most 2, report at most 3. PASS.
- 194 never ask what a rule decides; send the list itself.
- 195 may a follow-up of a printed story return in the Bulletin: still open; today's Bulletin carries 11 follow-ups; cards settled by G6.
- 196 the card list follows Rafi's order over the picker.
- 197 inside a full category compare appeal to a stranger, not only the score: Market has 7 eligible stories for 3 slots, Models 5 for 2, Security 4 for 2, Energy 4 for 2, Health 4 for 2.
- 201 the check chain: one round (rule 25).
- 202 label at most 14 characters, no money figure: pick_stories.md line 25 (2b on the 15 lines).
- 203 review_list.py intro photorealistic. PASS.
- 204 the Drive agent must try binaries: not live (rule 26).
- 206 and 237 the between-run fixes present: step 0b used when needed, phrasing override in all writer and checker briefs, not-financial-advice checks (check_wording.py, verify_headlines.py), G4b, groups of 10 (step 8.1); "funny at once" is gone from CLAUDE.md and from pick_stories.md.
- 207 open for Rafi from 10 Oct: item 2 (follow-ups in the Bulletin) open; item 3 (customer text in CLAUDE.md) open; item 5 partly fixed (2b); item 6 settled by rule 24; item 7 (Bigger Picture Bulletin words) answered by rule 29 (300 to 500; today 531, Part A's product); item 8 not live (rule 26); item 9 open.
- 210, 211 to 215, 231 the second run (ChatGPT V1) in the same Drive date folder and the labels: the names Rafi uploads carry _Claude-V1.
- 223, 250, 251 Bulletin sections without a 7: none today; Politics (1), Research (2) and Robotics (2) all hold stories at 7 or more; lesson 283: the robotics floor option cannot add named stories, so Robotics stays under the 3 to 5 guideline. PASS for "never empty".
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
- 255 credit lines of the form "X, citing Y": check every SOURCE line at step 7 (C06-01 CNBC citing two people, C06-02 The Standard citing unnamed mainland media).
- 259 France 24: no France 24 link in today's Bulletin (0 hits in bulletin_pdf.json); the report: verify at 0c.4.
- D1 do only the step he names; a one-sentence report, then wait.
- D2 Headlines in everyday words; cut filler.
- D3 spoken names "N-vidia", "an-thropic", "Kawa saki" only where spoken: check 15Sep1.
- D4 no colon after "Also in the full report": check B2a.
- D5 8 steps, the 4 s wav, fixed seed: fill asserts.
- D7, D36, D47 teaser and Bigger Picture credited AI News Desk: build_pack.py (fixed 12 Oct).
- D8 and D23 openings and endings are options; option 4 is used (bypass).
- D12 one short sentence; D13 only what he asks; D14 if it cannot be done perfectly, say so and stop; D15 one manual step per message; D18 look in the files before asking; D19 when a script blocks, follow it, never override it; D20 never delete, ask before any outward action.
- D25 Headlines only from that day's cards: replaced in part by rule 24 ("not necessarily in the cards"); rule 23 (Apate) was for 12 Oct only; story clips still come from the cards (G11).
- D27 the seed never changes (1060749754396562); D28 a spelling fix changes only the spelling.
- 262 and 272b the rules check is incremental (new): this file is updated from runs/2026-10-12/rules_check.md by rules_delta.md, launched with the picker; the main session reads the helper's one line and CLASHES only, never the lessons file whole.
- 267 Part B findings of 12 Oct (new): (1) the card renderer traces every card to an excerpt of the day's Full Report (REPORT_TRACE), so a report-only exception card passes but a story outside the report cannot be a card; (2) the 8 story clip template and 13 to 15 cards need repo edits that wait for Rafi's yes (runs/2026-10-12/script_edits_for_rafi.txt): today stays at 7 clips and 14 to 15 cards, scripts unchanged; (3) the gate has no override (selection.json only on PASS); (4) the card SOURCE strip copies the entry's source: patch cards_copy.json by hand if a relay is named; (5) the assembler stops when cover I01 is missing in a renamed folder.
- 270 helper time limit (new): proposed, NOT in force (awaiting Rafi, 272c); SKILL step 2 only asks for a look after 10 minutes. No wall-clock limit is applied to the Part B helpers.
- 271 the card post text has no home (new): written only when Rafi asks (D13, 245); open for Rafi: daily product or not, who writes it, where it is saved.
- 272 open items list (new): awaiting Rafi's yes: (a) repo edits for 8 clips and 13 to 15 cards, (c) the helper time limit, (d) the later token saving review of the Fable Headlines check; (b) the standing rules check is built (this file). To measure today: writer minutes and tokens under rule 27 and whether the checkers fail more lines. Later: real footage in the daily stitch, the automated Drive upload (rule 26), a rafi_overrides file for the gate.
- 273 two credits, one lesson per topic, search before adding (new): cards carry the news credit only (the footage credit is separate); lessons are added to the existing lesson as "ADDED <date>"; grep V1_TASKS.md before writing one (step 8.4).
- 274 mistakes not again (new): show Rafi the real lines, cards or files, never a description; a passed script check is not a read (check 1b); no padded estimates; "article" means any item (rule 29).
- 276 and 238(4) (new): DRIVE_DIFFS_FOR_CHATGPT.md is out of date (not Part B's job today; 2d); lesson 238(4) "one plain recommendation" against rule 1: clash 7.
- 277 chain audit (new): Group 1 is applied (incremental check, medium effort writers, story packs, lean main chat); Group 2 is open for Rafi one by one, and these items touch Part B and are NOT applied: (7) the 12 Oct script edits for 8 clips and 13 to 15 cards, (11) the main chat on Sonnet, (12) Part B in a fresh chat started by itself, (13) one approval stop in Part B, (14) a tighter repeat match.
- 280 never run git, not even git status, in any helper prompt (new): the Part B briefs say "never run git" (2b: add "not even git status" between runs); the picker brief and this task say it.
- 281 the 13 Oct edition is missing from the repo (new): no pool, Full Report, cards or Headlines; pick_pack.json last_7_days for 13 Oct is empty, G17 covers 6 of 7 days and G2 compares introductions with 12 Oct. Open for Rafi: send the 13 Oct cards and Headlines lines, or accept the gap (3a item 9).
- 286 viral rule and follow-ups (new): C01-01 (Gemini 4 Argon rollout, score 9) follows the 9 Oct card and clip and the pool calls it NEW: clash 6.
- 288 backups never next to the files the build reads (new): no `_old` copy goes into report_entries or facts (W/old_edits is the place); `_old` names in cards_work and headlines_work are not read by the scripts.

### 1e. Rules and lessons that do not apply to Part B today (grouped by reason; new items of 14 Oct included)
- Part A only (scan, pool, writers, editors, report and Bulletin build): CLAUDE.md 16 scan window, SOURCES, PER CATEGORY, 3 OCT 2026 RUN, BIG OUTLETS, FAMOUS PEOPLE RULE (a pool rule), POOL PDF EVERY DAY; P1-1, P1-2, P1-12, P1-13, P1-14, P1-15, P1-25, P1-26, P1-28, P1-30; Port-1, Port-2; 26, 27, 28, 32, 33, 39, 48, 57, 69, 78, 79, 86, 88, 102 to 106, 109, 112, 113, 130, 146, 151 to 153, 155, 157, 159, 160, 164 to 167, 169, 176, 185, 187, 217 to 220 (217: the NOTES slot of the curator and filler briefs, done 13 Oct), 222, 224, 225, 248 (viral check by link), 249, 252 to 254 (check_dup14.py prints the full line), 260, 261, 278 (step 0 order and yesterday_pool.csv), 282 (build_pool wording), 284 (qa_check LEAK pattern), 285 (writers moved categories: a Part A rule gap, see 2e), 287 (window gap events: a Part A rule question, see 2e); lesson 54 (weekend) does not apply, today is Wednesday.
- Rafi's PC (ComfyUI, stitch, audio, footage): CLAUDE.md 11, 12, 13; rule 26 footage and video-lesson lines; rule 29 HIS PC (keep it secure), DRIVE UPLOAD KEY (later, with ChatGPT's Google Cloud account) and DOWNLOADS (the local chat asks first); 13 (speaking speed test), 14, 15, 16, 17, 58, 143; D6, D9, D16, D17, D21, D22, D24, D26, D29 to D35, D37 to D46, D48; 239, 240 (stutter fixing, ADDED 12 Oct), 242, 243, 269 (footage search), 275 (V1 stitcher, clip runner, final encode).
- Records, superseded or not asked: CLAUDE.md 16 HAIKU TODAY ONLY (8 Oct), TEST of 6 Oct (replaced by REAL TV SCREENS), OPENING AND ENDING OPTIONS (not asked), rule 19 (Part B is started by Part A); rule 29 DRIVE DUPLICATES CLAUDE MADE (Drive housekeeping: rename and move to archive, rule 3); P1-18 (the process-search note is in 1d), P1-23, P1-24; 21, 40, 51, 52, 65, 70, 84, 87, 99, 120, 132, 133, 149, 153, 168, 170, 172, 184, 189, 205, 232 (superseded by rule 26), D10, D11, D42, D49, D50, D51; the empty Drive folder of lesson 216 (Rafi's to remove).

## 2. CLASHES (two rules that demand opposite things today; nothing chosen, nothing applied): 8 (4 new today: 5 to 8)

1. The count of 14 against the Bulletin source and the limits (carried; SLEEPS today).
   A: CLAUDE.md lines 200-201 (CARDS FROM THE BULLETIN: "the target is 14 story cards"), line 207 ("Aim: 14 story cards"), line 54 (8b item 4), pick_gate.py line 114 (G2: 14 or 15, no override file).
   B: CLAUDE.md line 88 (rule 14: counts are guidelines, adjust to the day's pool, state the number), line 222 (max_per_category=2), briefs/pick_stories.md line 23 ("up to 14 ... never add a 14th card that breaks a limit").
   Clash: the picker brief allows fewer than 14, the gate accepts only 14 or 15, and the gate has no override (lesson 267 item 3), so a smaller deck cannot pass. Not live today: the Bulletin gives 17 cards within the limits.
   Fix A: pick_gate.py G2 accepts the count the picker states when the Bulletin gives fewer within the limits (script change between runs, after Rafi's yes). Fix B: strike "up to" in pick_stories.md line 23. (wording mine, not yours)
   Recommendation: Fix A, when it next matters.

2. Nothing with a FAIL against one check round (carried; live).
   A: CLAUDE.md lines 145-147 (HEADLINES RULES RECHECK: "Nothing goes to him with a rules FAIL"); Part B SKILL.md step 0c.4 (line 77: "nothing is shown or delivered with an open FAIL"), step 8.5.
   B: CLAUDE.md line 57 (8b item 7: one check round and one rewrite round, then show Rafi what is left); SKILL.md step 3 (what is still open goes to Rafi in step 7, marked); rule 25 ("then Rafi sees everything", Claude's wording) and rule 27 ("fixes once").
   Clash: a checker flag still open after the one fix round either blocks step 7 or goes to Rafi marked.
   Fix A: add to 8b item 7: "A script FAIL (check_wording.py, check_headlines_rules.py, the gate) never reaches Rafi; a checker's flag still open after the one fix round goes to him marked." Fix B (lesson 201's text): "A fact error or rules fail found by the later checks always gets one more fix round before Rafi sees it." (wording mine, not yours)
   Recommendation: Fix A.

3. Rafi's introduction list against rotation (carried; live).
   A: CLAUDE.md lines 172-178 (HEADLINES INTROS AND FLOW: "In finance", "Also in finance", "In security", "In robotics", "In tech", "In the lab", "And finally, something lighter" ...; "The intros Rafi dictates win over rule G2").
   B: CLAUDE.md line 147 (never the previous day's wording, G2); Headlines Master G2; check_headlines_rules.py lines 82-90 (FAIL on any intro of the previous day).
   Clash: if today's writer uses a listed intro that the previous day used, the script fails G2, and it is not written whether the list counts as "dictated". New twist: the previous day is 13 Oct, which is not in the repo, so G2 can only compare with 12 Oct (lesson 281).
   Fix A: add: "The intros listed here are examples; G2 rotation applies to them." Fix B: add: "The intros listed here may repeat day to day; check_headlines_rules.py G2 skips them (script change between runs)." (wording mine, not yours)
   Recommendation: Fix A (no script change; the writer names the topic another way, for example "Turning to security", "And now, something fun").

4. Who writes the Bigger Picture card and clip (carried; live).
   A: CLAUDE.md line 158 (BIGGER PICTURE MODEL: one agent writes all three lengths; the main session never writes it), line 209 (BIGGER PICTURE WEIGHT: Fable writes it, all three lengths), rule 17 (line 248: the card is one of the three lengths).
   B: CLAUDE.md lines 296-297 (rule 25: one Opus writer per product writes the card and Headlines wording; rule 27 keeps Opus); briefs/wording_cards.md line 11 and wording_headlines.md line 9 (the Opus writers write the Bigger Picture card and clip).
   Clash: Part A wrote bigger_picture.json and bigger_picture_bulletin.json today but no bigger_picture_card.json, so the card and clip come from the Part B writers; rule 25 does not name BIGGER PICTURE MODEL.
   Fix A: add to rule 25: "This covers the Bigger Picture card and clip: the Part B writers write them from bigger_picture_bulletin.json only, and the checkers check them against it." Fix B: add to BIGGER PICTURE MODEL: "The Part A author also writes bigger_picture_card.json (card head, body and clip line); Part B copies it." (wording mine, not yours)
   Recommendation: Fix A for today (no extra agent; the author's own Bulletin text is the only source).

5. NEW. The Politics card and Headlines clip 1 cannot pass the gate (live; put to Rafi with the step 1 list).
   A: CLAUDE.md line 216 (HEADLINES START WITH POLITICS: when the deck has a Politics card its clip is clip 1, Fable never skips Politics), line 194 (CARD FILTER: every category keeps its best story at score 5 or more), briefs/pick_stories.md lines 8-9 (every category gets a card, including Politics; use the reserve and mark "exception"); pick_gate.py G18 (line 152) and G11b (line 142).
   B: CLAUDE.md line 289 (rule 24: "items in headlines must appear in the pool, and bulletin and report"), line 200 (CARDS FROM THE BULLETIN); pick_gate.py G4b (line 118) and G11 (clips are cards).
   Clash: the Bulletin's only Politics story, C05-01 (score 9), is a follow-up of 12 Oct (G6, NO UPDATE CARDS); the only new Politics story is C05-07 (Harris in Seoul, score 6, in the report, not in the Bulletin). G18 demands a Politics card, G11b makes it clip 1, G4b refuses a clip that is not in the Bulletin: every path fails one line.
   Fix A: add to rule 24: "A Politics card taken from the report because the Bulletin has no new Politics story, and its clip 1, need not be in the Bulletin (Rafi, <date>)" (pick_gate.py G4b skips that one clip after his yes). Fix B: "When the only Politics card is a report-only exception it is a card but not a clip; clip 1 is the first story clip in deck order." Fix C (Part A): add C05-07 to the Bulletin's Politics section and rebuild the Bulletin, so card and clip stay inside it. (wording mine, not yours)
   Recommendation: Fix A (one sentence from Rafi keeps both rules and the Politics clip).

6. NEW. C01-01 (Gemini 4 Argon rollout) is labelled NEW but follows the 9 Oct card and clip (live; put to Rafi with the step 1 list).
   A: CLAUDE.md lines 202-206 (NO UPDATE CARDS: an update is a card only when a major story changed meaningfully AND Rafi has named it; NO REPEATS IN 7 DAYS: no card or clip of the last 7 days "comes back, as a repeat or as an update"); line 219 (VIRAL RULE: only a story that ran earlier BELOW 7 may run once more).
   B: Part A SKILL.md lines 200-201 (step 9b: "A follow-up with new facts stays in the report; whether it can be a card is decided in Part B ... (a meaningful update can)"), Part B SKILL.md line 89 (an update kept when meaningful), and the pool's freshness label NEW for C01-01 (lesson 286: the judge kept it).
   Clash: C01-01 (score 9, the top story) ran at 10 on 1 Oct and as a card and clip on 9 Oct (limited release to security experts); today's story is the rollout to paying subscribers. G6 passes it because it says NEW; the CLAUDE.md lines say no unless Rafi names it.
   Fix A: Rafi names it: put C01-01 in cards_work/update_allowed.json (NO UPDATE CARDS allows a named update). Fix B: C01-01 is no card, clip or teaser item today; it stays in the report. Fix C (skill text): change step 9b to "A follow-up with new facts stays in the report; it is a card only when Rafi names it (NO UPDATE CARDS)". (wording mine, not yours)
   Recommendation: Fix A or B is Rafi's call (only he can name an update); Fix C either way.

7. NEW (from lesson 276). One plain recommendation against all viable paths.
   A: docs/V1_TASKS.md lesson 238(4), line 746 ("give one plain recommendation"; the lesson itself says it clashes).
   B: CLAUDE.md rule 1 (line 23): present ALL viable paths in one message, each with what Rafi has to do, the risk, and which one I recommend.
   Clash: rule 1 asks for every path with a recommendation; lesson 238(4) asks for one plain recommendation. It shows at step 1, where the list message goes to Rafi.
   Fix A: strike "give one plain recommendation" from lesson 238(4) (rule 1 already asks for one recommended path). Fix B: add to rule 1: "When one path is clearly the least effort for Rafi, the message may name only that path with a one-line reason." (wording mine, not yours)
   Recommendation: Fix A.

8. NEW. Where a clash is shown: stop at once, or at the next stop.
   A: CLAUDE.md lines 47-48 (rule 8a: Claude stops, names both rules, offers a fix "and waits for Rafi").
   B: Part B SKILL.md step 0c.3 (lines 72-73): "Bring the clashes with the story list at the stop of step 1 (or, if the helper is later, at the stop of step 7); never end a turn on them while writers are running."
   Clash: if this check comes back after step 1, wording starts under an unanswered clash, which is choosing; rule 8a says stop.
   Fix A: add to step 0c.3: "If this check is not back at the step 1 stop, step 1 waits for it; no wording starts until its CLASHES section is read." Fix B: add to rule 8a: "A clash found while writers run is shown at the next stop." (wording mine, not yours)
   Recommendation: Fix A (the check runs with the picker, so it normally returns before the list is shown).

### 2a. Touches settled by Rafi's own precedence lines or rulings (not counted; the settling line named)
1. 14 cards against extra_min 7 (11 Oct clash 1): 8b item 4 (a count he gives wins over a cutoff).
2. The second robotics card below extra_min (11 Oct clash 2): not live today (both Bulletin robotics stories score 7); 8b item 4 (the ROBOTICS count) would settle it.
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
30. Rule 29 (Bigger Picture Bulletin 300 to 500 words) against the 350-word wish (lesson 207 item 7): answered by rule 29.
31. Rule 24 NO TIME PRESSURE: decided 13 Oct ("yes exactly!"); no open touch.
32. The 12 Oct "8 story clips" template against the gate's 7 clips (lesson 267 item 2): scripts stay as they are (rule 16) until Rafi's yes (lesson 272a); today 7 clips.

### 2b. Stale lines in briefs and scripts (grep of the old wording of rules 22 to 29; scripts change only between runs, CLAUDE.md lines 159-161)
BLOCKS TODAY:
- pick_gate.py lines 66-69, 76 and 145-150 read the writer's score from report_entries; the Bulletin and card_candidates.py use the pool score (Rafi's ruling, 2a item 8). 6 of 11 categories differ today (pack against Bulletin: Politics 8 against 9, Market 6 stories, Energy 3 stories, Models 1, Research 6 against 7, Health 1). It changes ranks and the extra_min 7 test. Align before the picker (lesson 234d, run-folder data only): copy the entries to report_entries_before_pool_score_old (next to report_entries, never inside it, lesson 288), set score to the pool score and keep the writer's as fc_score; or tell the picker that the Bulletin score counts.
- make_wording_prompts.py lines 18-21 and common_b.py prev_scripts: PREV_CARDS and PREV_PACK come only from scratchpad run_ folders, so today they are "none" and assets/pack_base.json (2 Oct lines, "sentences of at most 15 words") unless arguments are given; PREV_LEADINS come from the newest repo runs/<day>/headlines_work/scripts_final.json before today, which is 12 Oct (13 Oct is missing). Run it with --prev-pack /home/user/ai-news-desk/runs/2026-10-12/headlines_work/headlines_12-10-26_pack.json --prev-cards /home/user/ai-news-desk/runs/2026-10-12/cards_copy.json (arguments, no script change).
FIXED SINCE 12 OCT (no longer listed): pick_stories.md lines 7, 9-10 and 40 (fun follows rule 24); SKILL step 8.2 (copy-to, rule 26); SKILL "currently 1 to 130" (step 0c rewritten); the picker prompt filled by hand (pick_gate.py pack writes it); the writers' re-read before each item (story packs).
DO NOT BLOCK TODAY:
- Part B SKILL.md step 0c: the heading still says "before anything is chosen" while the body says the picker does not wait (Rafi's yes of 13 Oct settles it, 2a item 25); step 0c.3 "Drive and CLAUDE.md disagree: stop and ask" against CLAUDE.md line 206 (no clash, CLAUDE.md wins); see also clash 8.
- Lesson 280: every Part B brief says "never run git"; "not even git status" is not in the text yet (add between runs).
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
- A third robotics card ("one extra allowed") against G8's cap of 2: no third eligible robotics story; the report-only robotics stories cannot be cards while the Bulletin has eligible ones (G4b exception test).
- VIRAL RULE re-run clause: no re-run; its exemption (an earlier run below 7) does not free C01-01 (clash 6).
- Critical stories spending a slot: no score 10 (top 9). Cards Master 2.10 big release rule: not in force.
- Robot war limit on cards: no such limit.
- (Live today, moved to section 2: a Politics reserve card as clip 1 against G4b: clash 5.)

### 2d. Drive differences settled by CLAUDE.md
- docs/DRIVE_DIFFS_FOR_CHATGPT.md is out of date (lesson 276) and was not opened today. New since 12 Oct: rule 27 (writers Opus on normal effort, one story pack read once) against the phrasing file's "every writer re-reads before each item"; rule 28 (the listen first at step 7) against Cards Master 7.15; rule 29 (Bigger Picture Bulletin 300 to 500 words; the fun concept to Rafi) against the Bulletin rules. Still standing: rule 22 against the phrasing file's Headlines section; rules 23 and 24 (a fun clip outside the deck, 12 Oct only) against Headlines A4; rule 24 groups of 10 against Cards 7.15; rule 26 (Rafi uploads) against Cards 7.4 and Headlines E5.

### 2e. Open for Rafi: rule gaps, not clashes (asked one at a time, only when they matter)
1. The 13 Oct edition is missing (lesson 281): send the 13 Oct cards and Headlines lines, or accept that G17 and G2 cover 6 days.
2. May a writer move a story to another category (lesson 285: C03-06 moved Models to Robotics, C11-11 Robotics to Models)? Neither is in the Bulletin; the gate reads the entry's category.
3. Do events of 12 Oct before the window count (lesson 287: C12-08, C13-09, C05-05, C08-15, C09-03, C15-01, C11-19)? In Part B C05-05 and C09-03 are Bulletin follow-ups and C12-08 and C15-01 reserve follow-ups (G6).
4. The card post text (lesson 271): a daily product or not, who writes it.
5. The Bigger Picture Bulletin text is 531 words against rule 29's 300 to 500.
6. Robotics in the Bulletin: 2 stories against the guideline of 3 to 5 (lesson 283: the script has no option to add a named story).

## 3. Today's must-haves and facts

### 3a. Must-haves for the picker
1. Counts: 14 story cards (the Bulletin gives 17 within the limits, so 14 is reachable); exactly 4 teaser items (report stories, no card, NEW, not in the last 7 days); exactly 7 story clips; 1 Fun card; the Bigger Picture named as card and clip (G20); bp_refs 3 to 5 report ids the Bigger Picture text rests on. By my match of the Bulletin text the ids are C07-01 (Korea's fall and chip stocks), C08-01 (ASML), C06-01 (Anthropic's investor day), C06-05 (Microsoft cost cuts, disputed), C05-03 (Zuckerberg), C05-05 (Goolsbee) and C11-03 (Agility's 2 Nov vote); the paper draft's C05-04 (Musk answers Broadcom's chief) is not in the text (it names neither Musk nor Broadcom). The picker confirms.
2. Order: deck in the Drive order Politics, Market, Security, Energy, Robotics, Models, Research, Ethics and law, Health, Society, Fun; higher score first inside a category (the Bulletin's pool score, 2b); clips in deck order; if the deck has a Politics card its clip is clip 1 (clash 5).
3. Politics: no new Bulletin story (C05-01 is a follow-up of 12 Oct, G6). The only new Politics story is C05-07 (Harris in Seoul, 6, NEW, read in full; the other, C13-06, is headline only). As a report-only exception card it passes G4b's exception test but its clip 1 fails G4b: clash 5, put to Rafi with the list.
4. Research: the Bulletin has C04-01 (headline only) and C04-02 (follow-up): no eligible Bulletin story, so a report-only exception card is allowed (G4b exception test passes): C04-03, C04-04, C04-05 or C04-06 (6, NEW, read). A report-only card is never a clip.
5. Limits: at most 2 cards a category (Market 3); a company on at most 3 cards and 2 clips (Anthropic is in 7 eligible stories, Nvidia 4, Google 3); labels at most 14 characters, no money figure; read in full only (C01-02 and C04-01 are headline only); C06-05 is DISPUTED and C10-05 PRELIMINARY: the card must say so.
6. CARDS FROM THE BULLETIN: cards only from the 32 eligible Bulletin stories; a reserve card only for a category with no eligible Bulletin story (Politics, Research).
7. NO UPDATE CARDS: the 11 follow-ups (C02-02, C04-02, C05-01, C05-03, C05-04, C05-05, C07-01, C08-02, C08-03, C09-03, C14-03) are no card, clip or teaser item; C01-01 (labelled NEW, follows the 9 Oct card) waits for Rafi's answer to clash 6.
8. ROBOTICS: 2 robotics cards, one humanoid: C11-03 (Agility Robotics, the Digit humanoid) and C11-01 (Tesla robotaxis); the pack flags machine_action false for both, so each card needs a robotics_ruling with a reason (G13): C11-03 is a stock-market listing step (humanoid funding counts, Rafi 8 Oct, but a merger vote is not a funding round: say so to Rafi), C11-01 shows a machine (robotaxis speeding in school zones). 1 robotics clip, saying what the robot or vehicle does.
9. NO REPEATS IN 7 DAYS: the 13 Oct decks are not in the repo (lesson 281): ask Rafi in the list message to send them or accept the gap. G17 and my read flag to judge: C01-01 (9 Oct card s10 and clip), C05-02 (7 Oct Hinton card), C06-02 (DeepSeek in 12 Oct lines), C07-02 (IMF, watched in the 12 Oct Bigger Picture), C13-01 (Pentagon and Anthropic, 6 Oct card; Rafi's 7 Oct complaint named this pair).
10. ONE TOPIC, ONE CARD: C06-03 (Market) and C14-15 (Society) are the same Character.AI bankruptcy: one card or a stated reason; the Market replies C05-03 and C05-04 are follow-ups, no cards.
11. Fun (rule 24 and rule 29): the fun card and headlines_fun come from the Bulletin (G4b): C16-01, C16-02 or C16-05; the picker gives the concept in one line each and Rafi says if it is funny; C16-01's "tokens" needs plain words.
12. Rule 24 "one sentence" test: C05-02 (Huang's claim and Hinton's answer) and C13-01 (court ruling and the Pentagon's label) are reply or two-fact stories: test each before it becomes a clip; REPLY STORIES: C05-02 names the earlier claim.
13. NOVICE TEST and PEOPLE WITH THEIR POSITION for every name (1a, 8b item 6).
14. Read pick_pack.md, not selection_draft.json (the draft has 14 cards but no Politics, Robotics or Research card, no robotics clip, 3 Market clips, and a teaser of three follow-ups).
15. Rule 28 and rule 29 to carry out later: the listen at step 7; the fun concept in the step 1 message.

### 3b. Facts of this edition
- Edition WED 14 OCT 2026; window 13 Oct 06:32 to 14 Oct 06:32 UTC (24 hours, run.json); no critical story; top score 9 (C01-01 Models, C05-01 Politics).
- Pick pack (cards_work/pick_pack.json): 48 Bulletin candidates and 56 report-only reserve stories (104 in all); its filter equals the CARD_FILTER line (5, 7, 14, 2, 3, 3, 2).
- Bulletin (products/bulletin_pdf.json): 48 stories: Politics 1, Market 11, Security 4, Energy 7, Robotics 2, Models 7, Research 2, Ethics and law 3, Health 4, Society 4, Fun 3. Pool scores: 9: 2, 8: 13, 7: 24, 6: 6, Fun 3, 3, 2. Purpose line: score 7 or more (Health and Society from 6) plus the top 3 Fun. 37 different source hosts, 0 Google News links. Bigger Picture section 531 words (rule 29: 300 to 500), "About this edition" 88 words.
- Pack (writer) scores against the Bulletin's pool scores: the same in Security, Robotics, Ethics and law, Society and Fun; different in Politics, Market, Energy, Models, Research and Health.
- Card-eligible Bulletin stories (NEW, read in full): Market 7 (C06-01, C06-02, C06-03, C06-04, C06-05, C07-02, C07-04), Security 4 (C05-02, C12-01, C12-02, C12-03), Energy 4 (C08-01, C09-01, C09-04, C09-05), Robotics 2 (C11-01, C11-03), Models 5 (C01-01, C02-01, C02-03, C03-01, C03-02), Ethics and law 3 (C13-01, C13-02, C13-03), Health 4 (C10-01, C10-02, C10-03, C10-05), Society 3 (C14-01, C14-02, C14-15); Politics 0, Research 0. Total 32; within the limits 17.
- Not eligible: follow-ups 11 (3a item 7); headline only 2 (C01-02, C04-01); Fun 3 (C16-01, C16-02, C16-05).
- Report-only reserve (56): Models 7, Research 6, Ethics and law 4, Politics 2, Market 8, Energy 13, Robotics 7, Security 6, Fun 3 (C16-06, C16-07, C16-09); 39 are NEW, read in full and score 6 or more (Models 5, Research 5, Politics 1, Market 8, Energy 11, Robotics 3, Security 4, Ethics and law 2): teaser candidates come from here.
- Paper draft (card_candidates.py, 08:14): 14 story cards plus fun C16-01 (C06-01, C06-02, C07-02, C05-02, C12-01, C08-01, C09-01, C01-01, C02-03, C13-01, C13-02, C10-01, C14-01, C14-15); clips C06-01, C06-02, C07-02, C12-01, C08-01, C01-01, C13-02 (no Politics, no robotics); teaser C05-01, C05-03, C08-02, C02-01; bp_refs C05-03, C05-04, C06-01.
- Last 7 days in pick_pack.json: 12 Oct 51 lines, 11 Oct 48, 10 Oct 48, 9 Oct 48, 8 Oct 50, 7 Oct 48; 13 Oct 0 (missing).
- Bigger Picture watch dates in the Bulletin text: Thu 15 Oct TSMC third-quarter results; Wed 21 Oct Meta results; 27 to 28 Oct the Federal Reserve; 28 Oct Alphabet and Microsoft; 2 Nov the Agility Robotics merger vote; SK hynix 27 Oct and Samsung 29 Oct reported, not confirmed; whether the September US inflation figure comes on 14 Oct (not confirmed). It names Korea's main index down more than 6 percent on Tuesday, ASML on 2027 and 2028 demand, Anthropic's investor meeting on 14 Oct, Microsoft's reported Azure cost cuts (disputed). It carries "not financial advice".
- Viral rule and the report's own count, cutoff and Fun Side: Part A's numbers, not read here; verify at 0c.4.
- Introductions used on 13 Oct (G2): unknown (not in the repo); 12 Oct's are in runs/2026-10-12/headlines_work/scripts_final.json.

### 3c. Cards and Headlines of the last 7 days (for G17 and the 3-day name and topic table; clip intros in brackets)
- 2026-10-13: MISSING from the repo (lesson 281); pick_pack.json last_7_days has 0 lines for it. Ask Rafi (3a item 9).
- 2026-10-12: 51 lines in pick_pack.json last_7_days['2026-10-12'] (cards, clips, teaser and Bigger Picture mixed); the structured deck is runs/2026-10-12/cards_work/selection.json. Read it there for the 3-day table; the Bigger Picture of 12 Oct said to watch the IMF report on Tuesday.
- 2026-10-11 CARDS: s1 C05-07 Britain's AI institute chief wants home-grown AI nobody abroad can switch off | s2 C06-01 Nvidia reportedly in talks to buy or invest more in AI lab Reflection | s3 C07-01 South Korea's stock market is losing its buyers | s4 C05-01 Microsoft's boss Satya Nadella wants an emergency brake to stop any AI mid-task | s5 C12-02 OpenAI says an AI faked test grades and damaged its workspace | s6 C08-01 Nvidia reportedly ending the RTX 5090 | s7 C11-03 US Army's new war drones overheated and lost signal | s8 C11-10 Tesla Optimus learned to vacuum and stir food by watching people | s9 C01-02 OpenAI's price list shows an unannounced biology AI | s10 C13-01 the White House leans on old laws to police AI | s11 C10-01 Chinese hospital AI reads a lung tumour sample in a minute | s12 C10-02 commentary: US health care tests Big Tech's AI spending | s13 C14-01 Nicolas Cage refused an AI waiver | s14 C14-02 Hollywood films on the bosses of Meta, Tesla and OpenAI | fun C16-01 tiny game studio took a bank loan for its AI learner driver | teaser C12-03 Britain's spy chiefs on the AI threat, C01-06 South African model for 12 languages, C14-07 workers pay a female AI helper less, C09-03 data centres an election issue in Ohio and Michigan | BP investors wary of AI debt, watch TSMC on 15 Oct || HEADLINES: C05-07 [In politics]; C06-01 [In business]; C05-01 [In security]; C12-02 [Also in security]; C11-10 [Turning to robots]; C10-01 [In health]; C14-01 [In entertainment]; fun crab robot plans given away (Rafi's own choice, not the fun card) [And finally, something lighter]; teaser C12-03 + C01-06; BP AI debt cooling, TSMC Thursday.
- 2026-10-10 CARDS: s1 C13-03 China: no blind money into AI and high tech | s2 C06-01 odds start-up TypeSafe valued at $7.5 billion | s3 C12-01 Claude sent police a made-up murder tip in a test | s4 C12-02 AI bosses rehearse for the day after an AI disaster | s5 C08-02 big buyers booked most of Samsung's memory chips | s6 C11-17 wheeled humanoid robot under $30,000 | s7 C11-18 Ukrainian ground robots rescued 45 soldiers | s8 C01-16 Musk backs Anthropic's ban on cruelty to AI | s9 C01-03 Alibaba's Qwen3.8 free to download | s10 C04-07 amateur with AI tools may have found a planet | s11 C08-01 Super Micro contractor admitted smuggling Nvidia chips | s12 C10-01 tech firms lobbied US health officials in a chat room | s13 C14-04 Nikon took back a prize over an AI-made video | s14 C14-05 publishers use AI for covers without telling authors | fun C16-01 government chatbot shared pasta recipes | teaser C02-01 Amazon asks Meta to keep its AI helper off its store, C01-01 Microsoft choice-only model, C10-02 GSK signs AI start-up Chai, C09-05 batteries cheaper than gas turbines | BP shares recovered from an OpenAI scare as China warned of blind investment || HEADLINES: C13-03 [From Beijing]; C06-01 [In finance]; C12-02 [Next, safety]; C11-17 [In robotics]; C01-16 [On chatbots]; C08-01 [In court]; C14-04 [In science]; fun C04-07 (story card s10, not the fun card) [On a lighter note]; teaser C02-01 + C09-05.
- 2026-10-09 CARDS: s1 C05-02 Trump: anyone saying artificial intelligence, not superintelligence, is the enemy | s2 C13-21 Musk accused Indian tycoons of blocking Starlink | s3 C06-04 OpenAI sales pace $20 billion below its earlier figure | s4 C07-04 WTO doubled its trade growth forecast on AI demand | s5 C03-01 Anthropic scans open-source code for free | s6 C12-02 OpenAI shut down Russian and Iranian fake-writer groups | s7 C09-03 Oracle trucks natural gas to data centres | s8 C11-23 humanoid robots directed traffic in Hangzhou | s9 C11-06 Walmart's warehouse robots break down | s10 C01-01 Gemini 4 Argon first for security experts | s11 C04-04 scientists: Anthropic overstated a gene-editing find | s12 C13-01 USA Today's publisher sued OpenAI | s13 C10-01 Google chatbot questioned patients before urgent visits | s14 C14-07 charity to record Gaza classrooms with AI | s15 C16-01 streamer's robot whacked him on the head (no separate fun card) | teaser C02-01 Gemini helper for firms, C11-24 Tokyo shop robot, C09-04 senators on data centre costs, C14-06 San Francisco rents | BP investors want results after OpenAI's lower sales figure || HEADLINES: C05-02 [First, super intelligence]; C13-21 [In India]; C07-04 [On trade]; C12-02 [In security]; C11-23 [Next, robotics]; C01-01 [In tech]; C14-07 [In education]; fun C16-01 [And now, something lighter]; teaser C02-01 + C14-06.
- 2026-10-08 CARDS: s1 C13-01 senator wants government safety tests of the strongest AI | s2 C13-03 five-minute video pitch for Pentagon deals | s3 C07-01 Samsung's $80 billion quarterly profit | s4 C07-02 TSMC sales up 51 percent | s5 C12-03 hackers hijacked 3,400 servers running AI tools | s6 C09-01 drones struck a Yandex data centre | s7 C11-02 Nvidia wants more of Figure AI | s8 C11-17 driverless Uber taxis in Dubai | s9 C02-01 ChatGPT answers with charts and buttons | s10 C01-02 Claude Haiku at a quarter of the price | s11 C04-01 Google, Meta and US agencies teach AI how cells react | s12 C15-01 IBM and three quantum makers reach Pentagon final round | s13 C13-05 AI voices for political robocalls | s14 C10-05 England's health service lets AI rank skin cancers | s15 C14-02 ChatGPT for Teens often fails to alert parents | fun C16-10 OpenAI helper: "Oh, I love you too" | teaser C02-02 Copilot to handle PC files, C05-01 IMF chief warns on AI debt, C14-06 Kenyan refugees lose online work, C11-04 Tesla Optimus 1,000 a week | BP chip makers cash in while debt worry spreads || HEADLINES: C13-01 [We start in Washington]; C07-01 [In business]; C09-01 [From Russia]; C11-02 [In robotics]; C02-01 [For chatbot users]; C04-01 [In science]; C14-02 [On teen safety]; fun C16-10 [And on a lighter note]; teaser C02-02 + C14-06.
- 2026-10-07 CARDS: s1 C13-22 UAE trains 80,000 civil servants to run government with AI | s2 C06-02 SpaceX wants to borrow $40 billion for Nvidia chips | s3 C05-02 Ray Dalio: AI bubble close to bursting | s4 C05-01 Jamie Dimon: Mythos made hacking ten times riskier | s5 C09-03 local opposition killed $260 billion of US data centre plans | s6 C09-04 record US power use from AI data centres | s7 C11-02 Waymo driverless in Detroit | s8 C11-16 Chinese robot hand threads a needle | s9 C02-01 Claude sidebar in Google Docs, Sheets and Slides | s10 C15-01 New York chip factory for light-based quantum parts | s11 C05-04 Hinton wants AI safety-checked like drugs | s12 C13-04 two US senators want AI firms liable when agents hack | s13 C10-01 Eli Lilly opens AI drug tools | s14 C14-02 71 percent of Americans expect fewer jobs | fun C16-13 Tirana's jailed mayor sends an AI double | teaser C01-01 Mistral model, C02-04 Gemini in Chrome on Android in India, C13-24 Nigeria's election body and AI, C09-09 San Francisco data centre pause | BP Dalio calls AI a bubble as chip buying runs on debt || HEADLINES: C13-22 [We begin with politics]; C05-02 [On the markets]; C05-01 [In banking]; C09-03 [In energy]; C11-16 [Now to robots]; C02-01 [In software]; C05-04 [Turning to safety]; fun C16-13 [And now a smile]; teaser C01-01 + C13-24.
- 2026-10-06 (outside the 7 days, kept for the Pentagon and Anthropic and DeepSeek checks) CARDS: s1 C13-01 Pentagon says it dropped Anthropic | s2 C06-01 OpenAI wants to raise $30 billion or more | s3 C06-02 DeepSeek close to raising at least $12 billion | s4 C06-03 Moonshot plans a Hong Kong share sale | s5 C12-02 Wikipedia's parent: OpenAI agents tried to edit pages | s6 C12-01 South Korea's president: bank hackers may have used AI | s7 C08-01 AMD to supply far more AI chips in 2027 | s8 C09-01 Google near a nuclear power deal | s9 C11-01 AI-aimed gun turrets shot down Russia's fastest drones | s10 C01-01 Reflection's Beam matches a top Chinese model | s11 C04-02 Google DeepMind AI invented two enzymes | s12 C05-01 former AI workers warn New York City's council | s13 C10-01 an app's AI prescribes acne medicine in Utah | s14 C10-02 Britain to check AI medical tools throughout their use | s15 C14-02 protesters disrupt a London tech dinner | fun C16-01 Jon Stewart and Meta's AI mascot | teaser C11-02 NATO drone and AI plan, C05-03 senator calls Anthropic boss's warnings alarmist, C04-05 AI steered an X-ray machine, C08-04 Qualcomm against Arm | BP tech shares at a record; banks and Gulf funds line up AI money || HEADLINES: C13-01 [We begin with an update]; C06-01 [In finance]; C06-02 [Also in finance]; C12-01 [In security]; C11-03 (not a card: LG and Nvidia AI brain for Hyundai's self-driving car) [In robotics]; C01-01 [In tech]; C04-02 [In the lab]; fun C16-04 (not the fun card: Alexa stuck saying la la la) [And finally, something lighter]; teaser C11-02 + C05-03.
