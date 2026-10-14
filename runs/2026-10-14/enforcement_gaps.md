# Enforcement gaps: Headlines JSON and cards (audit, 14 Oct 2026)

Read only. Sources: Drive copies in run_2026-10-14/rules (HM = Headlines_Master_Rules_Structure.txt, CM = Cards_Master_Rules_Structure.txt, PH = Article_phrasing_instructions_AIND_V1.txt), CLAUDE.md (CL), and the Part B scripts in .claude/skills/fill-category-scan-part-b/scripts. "l." = line number.

Labels:
- **SCRIPT**: a script fails it or builds it so it cannot be wrong. "(partial)", "(warn)" or "(not gated)" means the check is weak, explained in the note.
- **CHECKER ONLY**: only a model checker (Fable, briefs/check_cards.md or check_headlines.md) reads it.
- **NOTHING**: no script and no checker. At most the writer's own brief mentions it, and the writer is the author, not a checker.
- **JUDGEMENT**: taste, which a script cannot decide.

## Counts

| Group | SCRIPT | of which partial/warn | CHECKER ONLY | NOTHING | JUDGEMENT | Total |
|---|---|---|---|---|---|---|
| Headlines | 31 | 10 | 9 | 7 | 4 | 51 |
| Cards | 17 | 4 | 8 | 5 | 2 | 32 |
| Order and choice | 20 | 4 | 0 | 6 | 2 | 28 |
| **All** | **68** | **18** | **17** | **18** | **8** | **111** |

## The gate holes behind the gaps (read these first)

1. **The card 15-words-per-sentence check is dead code.** check_wording.py l.63 computes `w` (the word count) and never tests it. The docstring (l.7), wording_common.md l.13 and SKILL step 8.5 ("a headline over 15 words ... is fixed before step 7") all say it is enforced. It is not.
2. **The card wording has no gate.** No script reads cards_work/check_result.json (the card checker's result). check_wording.py --cards writes no stamp file (l.124: the stamp is for Headlines only). build_cards_copy.py, make_cards.py and the renderer build whatever is in cards_copy_fable.json, whether or not the check ran or passed.
3. **A Headlines checker FAIL never blocks.** common_b.rules_gate l.45-46 checks only that rules_result.json is newer than scripts_final.json, not that every entry passed. Script FAILs (rules_check.json, wording_check.json) do block.
4. **The A2 opening and ending check usually runs on nothing.** check_headlines_rules.py runs in step 3, but the pack is built in step 6 (build_pack.py). On the first check of the day there is no pack, so A2 is silently skipped (l.73-75).
5. **The 7-day repeat check (G17) passes days it cannot see.** A day with no deck text only prints a NOTE (pick_gate l.174), and the picker can wave a hit away with "disputed_repeats".
6. **Two of Rafi's 14 Oct rules are not in CLAUDE.md** (rule 8 says every instruction goes there): category openings (only in wording_headlines.md l.27, check_headlines.md l.17 and the B2d/B2e checks) and exact figures (only in wording_common.md l.25 and the LOOSE regex).

## Headlines

| # | Rule | Where | Enforcement | Note / how a script could check |
|---|---|---|---|---|
| H1 | 13 slots: C01 opening, C02-08 seven stories, C09 fun, C10 teaser, C11 BP, C12 unused, C13 ending | HM A1-A7 l.43-49; CL l.242-246 | SCRIPT build_pack.py l.32-47 (assert 7 stories); pick_gate G2 | DRIVE DIFF: HM A1/A2 say 12 slots with the ending in slot 12 |
| H2 | Opening and ending are the stored option 4 clips of 3 Oct; slots 1 and 13 bypassed | CL l.242-246 | SCRIPT (warn) assets/pack_base.json (both "bypass"); check_headlines_rules A2 WARNs if slot 1 is active | Hole 4. SKILL step 6 text is stale ("C01 and C13 carry Rafi's opening and ending of 2 Oct") |
| H3 | Ending says the approved words | HM A2 l.44 | SCRIPT (partial) check_headlines_rules A2 l.77-78 (pack text) | Nothing checks that the stored 3 Oct clip actually says these words (HM A2: "reuse only after verifying") |
| H4 | Every clip is generated; bypass only opening, ending and the spare slot | CL l.182 | SCRIPT build_pack.py (builds every slot active); fill_headlines asserts modes l.145 | verify_headlines lists active slots but does not fail on a missing one |
| H5 | No clip over 12 s | CL 22 l.277-284, l.128; HM B1 l.53 | SCRIPT check_wording l.114; check_headlines_rules B1 l.87; fill_headlines assert l.95; verify_headlines l.28 | Stale docstring: fill_headlines l.11 still says "no clip may pass 10 s" |
| H6 | Aim 8 s, 10 acceptable for a long item | CL 22, l.128 | SCRIPT (warn) check_headlines_rules B1 (warns past 9.0/8.5/10.5); check_wording (warns past 9.5/11.5) | The warn levels are the 30 Sep figures (CL l.108-110), not rule 22's 8 and 10. Inside CLAUDE.md, l.108-110 ("8 to 9 s") and l.128 ("aim 8") disagree |
| H7 | Box = syllables / 4.4, rounded UP to the next half second | CL l.110, l.127 | SCRIPT fill_headlines box_seconds l.45-50, assert l.151 | DRIVE DIFF: HM B1a l.54 says two decimals, never round up (CL says it overrides) |
| H8 | News part about 90 s | HM A8 l.50; CL l.108 | NOTHING (printed only: check_wording l.118, verify_headlines l.29) | WARN outside about 80 to 100 s |
| H9 | Every story and fun clip opens with a short spoken intro | HM B2a l.56 | SCRIPT check_headlines_rules B2a l.89 (1 to 5 words) | |
| H10 | A story clip opens with its category ("In finance"); "First, a critical" for a 10; never a place | Rafi 14 Oct: wording_headlines.md l.27; CL INTROS l.172-180 | SCRIPT check_headlines_rules B2d, B2e l.90-92 | Not in CLAUDE.md (hole 6). CLASH inside the brief: see K4 |
| H11 | Teaser opens "Also in the full report." | HM B2a l.56 | SCRIPT check_headlines_rules l.93 | |
| H12 | BP opens "And for the bigger picture" | HM A6 l.48 | SCRIPT check_headlines_rules l.94 | |
| H13 | Intros rotate, never the previous day's wording | HM G2 l.126-127 | SCRIPT (partial) check_headlines_rules G2 l.102-110 | Category openings are exempt (l.106), so only the fun intro is really tested. DRIVE DIFF with the 14 Oct category rule; CL l.177 says Rafi's intros win over G2 |
| H14 | Numbers spoken as words, no digits | HM B3 l.57 | SCRIPT check_wording l.68; check_headlines_rules B3; verify_headlines l.27 | |
| H15 | Exact figure, never a loose phrase ("about a third") | wording_common.md l.25 (Rafi 14 Oct) | SCRIPT (partial) check_wording LOOSE l.19 | Not in CLAUDE.md. CLASH K5 (same brief, l.13, says the opposite) |
| H16 | No outlet spoken | HM G1.4 l.124 | SCRIPT (partial) check_headlines_rules G1.4 l.99-101 (15 outlets plus the entry's source) | |
| H17 | Hedges kept; nothing stronger than the entry | HM G1.4; PH 1A | CHECKER ONLY (check_headlines.md item 4) | Script: each hedge word in the entry (reportedly, plans, may, could, says, allegedly) must appear in the line |
| H18 | Pronunciation cues only where spoken; "Google DeepMind" | HM 15 Sep 1-2 l.239-240 | SCRIPT check_headlines_rules 15Sep1/2 l.96-98 | DRIVE DIFF: Drive cue is "an-thropic", repo uses "anthro-pic" |
| H19 | Acronyms spaced for speech (A I, C E O) | HM G1.1 l.121 | CHECKER ONLY | Script: FAIL any unspaced capital run of 2 to 5 letters ("AI", "CEO") in a spoken line |
| H20 | ONE sentence: who did what and why | CL 22 l.277-284, l.164 | CHECKER ONLY (the who/what/why fields are checked as non-empty, check_wording l.110-112; a side clause at the start fails, l.72) | Script: count sentence ends after the intro; FAIL if more than 1. DRIVE DIFF: PH l.100-103 allows a second sentence (briefs carry an override) |
| H21 | Every named person has position and organisation | CL l.214-215 | CHECKER ONLY | Script: each person name (entry's people, or a capitalised First Last) must be followed in the same sentence by a role word (chief, founder, minister, head, president, professor) or "of <Org>" |
| H22 | Company under 100 billion dollars gets a 2 to 3 word tag | HM G1.2 l.122 | CHECKER ONLY (check_headlines_rules only lists the names, INFO l.117-120) | Script: any company not on the BIG list must have descriptive words right before it |
| H23 | Plain words; deed first, never the money, for non-market stories | HM B2 l.55; CM 3.3 l.76 | CHECKER ONLY | Script: for non-MKT clips, FAIL money words ($, billion, million, funding, raised, valuation, revenue) before the main verb |
| H24 | Robotics clip says what the robot does | HM B2 l.55 | CHECKER ONLY | Partly JUDGEMENT; the entry's machine_action could be required to be echoed |
| H25 | Banned jargon words | wording_common.md l.14 | SCRIPT check_wording BANNED l.20-22 | |
| H26 | Reply story says it is a reply and names the earlier story | CL l.141-144 | SCRIPT check_wording reply_problem l.32-52 | |
| H27 | BP clip says "This is not financial advice" and the screen shows it | CL l.209-213 | SCRIPT check_wording l.120-123; verify_headlines l.23-26 | |
| H28 | BP = market summation plus what to watch and why, dated | CL 17 l.248-258, l.209-213 | CHECKER ONLY | Partly JUDGEMENT |
| H29 | Screen: photoreal TV news scene; no readable words, numbers, logos or named faces | CL l.185-187; HM 15 Sep 3 l.241 | NOTHING for the writer's `screen` line (the fixed prompt sentence in fill_headlines l.18 is SCRIPT) | Script: FAIL digits, quotes, company or outlet names, "logo", "text" or person names in `screen` (BP warning sign excepted) |
| H30 | Level is the 11 Oct model lines (constant) | CL 24 l.292 | JUDGEMENT (checker reads the model lines) | |
| H31 | Clip line does not contradict its card | CL 25 l.297 | CHECKER ONLY | |
| H32 | Fun clip is fun (rule 24); explainable in one sentence | CL l.290, l.294 | JUDGEMENT | Rafi judges the concept for now (CL 29 l.317) |
| H33 | Teaser only from the teaser card, never a story card | HM A5 l.47 | SCRIPT check_headlines_rules A5 l.72; pick_gate G12 | |
| H34 | Teaser and BP credited "AI News Desk" | build_pack l.41, l.44 (lesson 241) | SCRIPT (built in) | DRIVE DIFF: HM G7.3 l.157 says the teaser credit is DAILY GLOBAL AI INTELLIGENCE REPORT |
| H35 | Headlines items are in the pool, Bulletin and report | CL 24 l.289 | SCRIPT pick_gate G4b l.118 | |
| H36 | One company in at most 2 clips | CL CARD_FILTER l.222 | SCRIPT (partial) pick_gate G10 (24 names, entry headline only); check_headlines_rules C16 (25 names, spoken text, the 2 is hard-coded, not read from CARD_FILTER) | |
| H37 | 8 sampler steps | CL l.231-236 | SCRIPT fill_headlines l.61, l.133; verify_headlines l.28 | DRIVE DIFF: HM C4 l.70 and G5.2 l.143 say 6 steps. CL l.231 said "if it works it moves to Drive"; it never did |
| H38 | 4 s voice sample | CL l.233 | SCRIPT fill_headlines l.62, l.134 | DRIVE DIFF: HM C4 says the fill never changes the voice |
| H39 | "Unhurried ... never rushed" in every active prompt | CL l.234-236 | SCRIPT verify_headlines l.21, l.28 | |
| H40 | The prompt is the Drive prompt file; nothing else changes | HM B2 l.62-63 | NOTHING | fill_headlines l.18 hard-codes its own prompt and never reads Headlines_prompt_for_comfy_json.txt. The two differ (tone words, "no on-screen text" vs "outside the hologram panel", news scene). Script: diff against the Drive file and the list of approved repo changes; STOP on anything else. DRIVE DIFF |
| H41 | Seed, LoRA, references, Spectrum, links and node count unchanged; upscale saves on | HM C4 l.70; 25 Sep l.217 | SCRIPT fill_headlines asserts l.130-150 | |
| H42 | Reference 1 is the hands-on-table image, reference 2 the fists image | HM C l.66 | SCRIPT (partial) fill_headlines l.135 asserts the 29 Sep file names | The assert names "...smile_v4.png" as reference 2, not a "fists" image. Possible difference: ask Rafi |
| H43 | Visible and named widgets agree; stale word scan | HM C6-7 l.72-73 | SCRIPT (partial) fill_headlines assert l.155-157 | The stale scan only prints (l.176-178), it never fails |
| H44 | Titles start with the edition date; new workflow id | HM C2, C4 | SCRIPT (built in) fill_headlines l.105-112 | |
| H45 | No pack, JSON or review list until the script checks and the checker have run on the current lines | CL l.145-147, l.164-168 | SCRIPT (partial) common_b.rules_gate (build_pack l.16, review_list l.67) | Hole 3: the checker's result is checked for age, not for FAILs |
| H46 | Nothing goes to Rafi with a rules FAIL | CL l.145-147 | NOTHING for checker FAILs (script FAILs block, see H45) | CLASH K2 |
| H47 | Daily listen: all spoken lines in the chat before the review | CL 28 l.304-306 | NOTHING (a step for the main session) | review_list.py could print the listen block first |
| H48 | Two critical stories on the same theme may share one clip | HM A3 l.45 | NOTHING | CLASH K6: pick_gate G21 needs every critical as its own clip id |
| H49 | Headlines carry 1 robotics clip (keep robotics, law, research or society) | CL ROBOTICS l.223-226; HM A3 l.45 | NOTHING | Script: pick_gate FAIL if the deck has a ROB card but no ROB id is in `headlines` (unless waived) |
| H50 | Prefer AI affecting people over war or politics | CL l.180 | JUDGEMENT | |
| H51 | Clips are the strongest card stories | HM A3; CL l.199, l.216-217 | JUDGEMENT (Fable may choose) | |

## Cards

| # | Rule | Where | Enforcement | Note / how a script could check |
|---|---|---|---|---|
| C1 | Head: one sentence, at most 85 characters | wording_cards.md l.8; check_cards.md l.7 | SCRIPT (partial) check_wording l.94-95 | Length only; "one sentence" is not counted |
| C2 | Body: exactly 2 sentences, at most 230 characters | same | SCRIPT check_wording l.96-97 | Hole 2: not gated |
| C3 | Every sentence at most 15 words | wording_common.md l.13; check_wording doc l.7; SKILL 8.5 | NOTHING | Hole 1: `w` computed at l.63, never tested. Fix: `if kind == 'card' and w > 15: out.append(...)` |
| C4 | At most one number per sentence | wording_common.md l.13 | SCRIPT check_wording l.64 | |
| C5 | Teaser line at most 90 characters, deed first | wording_cards.md l.10 | SCRIPT (length) l.94; deed first is checker only | |
| C6 | BP card: head at most 85, body at most 160, two sentences | wording_cards.md l.11 | SCRIPT check_wording l.90, l.96-97 | |
| C7 | Banned jargon words | wording_common.md l.14 | SCRIPT check_wording l.20-22 | |
| C8 | No outlet in a headline; never "X reports that" | wording_common.md l.15, l.20 | SCRIPT (partial) check_wording l.67 (opening pattern only) | Script: test heads against the outlet list and the entry source, as G1.4 does for clips |
| C9 | Lead with the deed, never the money (non-market cards) | CM 3.3 l.76 | CHECKER ONLY (check_cards reads CM Section 3) | Script: for non-MKT cards, FAIL money words in the head or the first body sentence |
| C10 | Unfamiliar companies get a short title | CM 3.4 l.77 | CHECKER ONLY | Same script idea as H22 |
| C11 | Every named person has position and organisation | CL l.214-215 | CHECKER ONLY | Same script idea as H21 |
| C12 | Credit the true first reporter ("X reports, citing Y"), never a copy site | CM 3.5 l.78; CL CREDIT l.129-140 | CHECKER ONLY (the source line itself is built in: build_cards_copy l.37) | |
| C13 | Status pill mirrors the QA status | CM 3.5 l.78 | SCRIPT (built in) build_cards_copy l.37 | |
| C14 | BP card label AIND, source "AI News Desk" | CL l.135-139 | SCRIPT (built in) build_cards_copy l.42-43 | DRIVE DIFF: CM 1.3 l.41 says pill DESK VIEW |
| C15 | BP card carries the not financial advice notice | CL l.209-213 | SCRIPT (built in) make_cards l.44 | The post caption line (CL l.212-213): nothing |
| C16 | BP card = market summation plus what to watch and why | CL 17 l.248-258 | CHECKER ONLY (check_cards.md l.7) | |
| C17 | BP written by one Fable-max agent, all three lengths | CL BP MODEL l.158; BP WEIGHT l.209-211 | NOTHING | CLASH K3: the Opus card writer writes the BP card (wording_cards.md l.11) |
| C18 | Reply story says it is a reply and names the earlier story | CL l.141-144 | SCRIPT check_wording l.98 | |
| C19 | Exact figures, never loose phrases | wording_common.md l.25 | SCRIPT (partial) check_wording LOOSE l.19 | CLASH K5 |
| C20 | Read aloud: the two body sentences connect like speech | CL 29 l.316 | CHECKER ONLY (check_cards.md 1b) | |
| C21 | Stranger test: who did what and why from the card alone | check_cards.md l.5 | CHECKER ONLY | |
| C22 | Facts and hedges match the entry | check_cards.md l.8 | CHECKER ONLY | Same script idea as H17 |
| C23 | Approved text is never changed to fix layout; the layout bends | CM 3.6 l.79 | NOTHING | |
| C24 | CATEGORY line short (label at most 15) or the renderer drops the card | build_cards_copy l.8-9, l.34; pick_gate G14 | SCRIPT G14; build_cards_copy WARN; assemble_cards STOP l.120-121 | pick_stories.md says 14 at l.25 and 15 at l.37 |
| C25 | Instagram window y 465-1457 (renderer asserts 420-1500) | CM Section 5 l.94 | SCRIPT (partial) the external renderer aind_cards.py | Not in the repo; not verified here |
| C26 | Closing card wording as approved on 12 Sep | CM 2.12 l.61-66 | SCRIPT (built in) build_cards_copy l.15-17 (matches Drive) | |
| C27 | Cover: the approved cover, only the date changes | CM Section 6 l.100; presenter l.7-12 | SCRIPT (built in) make_cover.py | |
| C28 | File names cards_D-M-YY_INN_VL1 (+ _Claude-V1 on delivery) | CM l.16-19; CL l.20 | SCRIPT assemble_cards l.124; delivery_manifest.py | |
| C29 | Card wording checked (script plus checker) before render | CL 25 l.297; SKILL step 3 | NOTHING | Hole 2. Script: a cards_gate in build_cards_copy.py like common_b.rules_gate: check_wording stamp with 0 fails, check_result.json newer than cards_copy_fable.json with all pass (or listed as shown to Rafi) |
| C30 | Send in groups of 10, never a zip | CL 24 l.288 | NOTHING (process) | |
| C31 | Card reader level 6/10 | PH l.91 | JUDGEMENT | |
| C32 | Fun card light tone, still precise | wording_cards.md l.12 | JUDGEMENT | |

## Order and choice

| # | Rule | Where | Enforcement | Note / how a script could check |
|---|---|---|---|---|
| O1 | Deck in the approved category order | CM l.1-5, 2.4 l.51-53; CL 20 l.271 | SCRIPT pick_gate G7 l.131 (order read from the Drive CM copy) | |
| O2 | A story rated 10 is the first card and the first clip | CL 30 l.318; CM 2.2 l.49; HM l.7 | SCRIPT pick_gate G21 l.145, G11b l.143 | G21 counts every entry rated 10, even held ones (would be impossible to pass) |
| O3 | A critical spends its category's slot | CM 2.3 l.50 | SCRIPT pick_gate G8 (criticals are counted in their category) | |
| O4 | Inside a category the highest score goes first | CM 2.4 l.53; pick_stories.md l.23 | NOTHING | Script: in G7, also require scores to fall within each category run |
| O5 | Clips are cards, in deck order | HM A3 l.45; CM 2.14 l.69 | SCRIPT pick_gate G11 l.142; check_headlines_rules A3 l.69 | |
| O6 | A Politics card is clip 1 (behind criticals) | CL l.216-217 | SCRIPT pick_gate G11b l.143 | |
| O7 | Fun is the last story card; the reel goes stories, fun, teaser, BP, ending | CM 2.4 item 11; HM A7 l.49 | SCRIPT (built in) pick_gate l.182; build_pack | |
| O8 | 14 story cards (15 allowed), 4 teaser items, 7 clips | CL CARD_FILTER l.222, l.200-201 | SCRIPT pick_gate G2 l.114 | CLASH K1 |
| O9 | Cards only from the Bulletin (an exception needs a reason) | CL l.200-201 | SCRIPT pick_gate G4, G4b l.119-125 | |
| O10 | At most 2 per category, markets 3 | CL CARD_FILTER | SCRIPT pick_gate G8 l.133 | DRIVE DIFF: CM 2.4 fixed slots, CM 2.6 "aim for 15" |
| O11 | Money cap: market slots plus any money critical at most 3 | CM 2.7 l.56 | SCRIPT (partial) G8 counts MKT only | A money story filed under another category is not counted |
| O12 | One company on at most 3 cards | CL CARD_FILTER | SCRIPT (partial) pick_gate G9 (24 names, entry headline only) | |
| O13 | Every category gets a card when an eligible story exists | CL CARD FILTER l.191-198 | SCRIPT pick_gate G18 l.156 | |
| O14 | 2 robotics cards; a robotics card shows a machine doing something (humanoid funding counts) | CL ROBOTICS l.223-226; CM 2.9 l.58 | SCRIPT pick_gate G13, G19 | DRIVE DIFF: CM 2.9 says "not a funding round" |
| O15 | One of the robotics cards is a humanoid story | CL l.224 | NOTHING | Script: if an eligible ROB entry mentions "humanoid", one ROB card must too |
| O16 | No update of an earlier story unless Rafi named it | CL l.202-204 | SCRIPT pick_gate G6 l.128 | |
| O17 | No story of the last 7 days' cards or clips comes back | CL l.205 | SCRIPT (partial) pick_gate G17 l.160-172 | Hole 5 |
| O18 | Compare each card with the last 3 days and SHOW Rafi the table | CL l.203-204 | NOTHING | The gate prints hits only; no table |
| O19 | ONE TOPIC, ONE CARD: a reply goes on the same card and clip; every pair of cards is checked for a shared topic | CL l.221 | NOTHING | Script: pairwise pn()/keys() overlap between chosen cards (as G17 does against old decks); FAIL unless declared |
| O20 | Every card and clip story was read in full | CL CARD FILTER | SCRIPT pick_gate G5 l.126 | |
| O21 | Ids exist and are not held (14-day NO OLD NEWS) | CL l.188-190 | SCRIPT pick_gate G1 l.113 | |
| O22 | Teaser stories get no card and no clip | HM A5; CM 1.4 l.42 | SCRIPT pick_gate G12 l.146 | |
| O23 | BP sources are in the report and not held | CL 17 | SCRIPT pick_gate G16 l.159 | |
| O24 | Every pick has a reason, a not-a-repeat reason and a novice test | pick_stories.md l.23 | SCRIPT (partial) G15, G15b (checks they are present, not what they say) | |
| O25 | Rafi's own article: last story card before fun | CM 2.13 l.68 | NOTHING | Rare |
| O26 | Rafi approves the story list before any wording is written | CL l.155-156; SKILL step 1 | NOTHING | Script: make_wording_prompts.py refuses without an approval stamp file |
| O27 | Fun story choice (rule 24) | CL l.290 | JUDGEMENT | |
| O28 | Stories that matter worldwide and interest a wide crowd | CL l.152-155, l.180 | JUDGEMENT | |
| (not counted) | Big release takes the first slot after criticals | CM 2.10 l.59 | not in force (CM 9.3: waits for Rafi's "go") | |

## Clashes

### Inside the repo (CLAUDE.md, the briefs and the scripts disagree): Rafi must decide (CL 8a)

- **K1 Counts.** CL 14 l.88-91 says "counts are guidelines, not gates", and pick_stories.md l.23 says "give the number the Bulletin supports". But pick_gate G2 FAILs anything other than 14 or 15 cards, exactly 4 teaser items and 7 clips. SKILL step 1 and CM 2.5 say 3 to 4 teaser items.
- **K2 FAILs shown to Rafi.** CL HEADLINES RULES RECHECK l.145-147 says "nothing goes to him with a rules FAIL". CL 25 l.297 and SKILL step 3 say "whatever is still open goes to Rafi in step 7, marked". The gate only checks that the checker ran.
- **K3 Who writes the Bigger Picture card and clip.** CL BIGGER PICTURE MODEL l.158 and WEIGHT l.209-211 say one Fable-max agent writes all three lengths. CL 25/27 replace only the STORY CHOICE writer line, yet wording_cards.md l.11 and wording_headlines.md l.9 have the Opus writers write the BP card and clip. pick_stories.md l.10 still says "written later by Fable".
- **K4 Opening examples.** wording_headlines.md l.9 gives "From Washington", "On the markets" and "Turning to safety" as example intros. l.27 of the same brief and check_headlines_rules B2d/B2e fail exactly those.
- **K5 Loose numbers.** wording_common.md l.13 says "about a third, not 31.4 percent". l.25 of the same brief (Rafi, 14 Oct) and check_wording LOOSE fail "about a third".
- **K6 Shared critical clip.** HM A3 l.45 says two critical stories on the same theme may share one clip. pick_gate G21 needs every story rated 10 as its own clip id, so a shared clip fails.
- **K7 Clip timing in CLAUDE.md itself.** l.108-110 says stories 8 to 9 s and BP about 10; l.128 and rule 22 say aim 8, 10 acceptable. check_headlines_rules uses the old figures for its warnings.
- **K8 (possible) Reference image 2.** HM C l.66 says the fists image. fill_headlines l.135 asserts "AIND_Comfy_reference_3_2160x3840_smile_v4.png". Confirm with Rafi.

### Drive vs repo (the repo wins by CL l.206-208; these belong in docs/DRIVE_DIFFS_FOR_CHATGPT.md)

D1 HM B1a two decimals vs round up to the half second (H7). D2 HM C4/G5.2 six steps vs 8 steps (H37). D3 HM C4 voice unchanged vs 4 s sample (H38). D4 HM B2 Drive prompt only vs fill's hard-coded prompt (H40). D5 HM A1/A2 12 slots vs 13 (H1). D6 cue "an-thropic" vs "anthro-pic" (H18). D7 HM G7.3 teaser credit vs "AI News Desk" (H34). D8 HM G2 rotation vs daily category openings (H13). D9 HM G3/15 Sep 3 text-free symbols vs REAL TV SCREENS (H29). D10 PH Headlines l.100-103 (second sentence, at most 10 s, a company reason is not a why) vs rule 22 (H20). D11 CM 1.3 DESK VIEW vs AIND (C14). D12 CM 2.4/2.6 fixed slots and aim 15 vs CARD_FILTER (O10). D13 CM 2.9 no funding round vs humanoid funding counts (O14).
