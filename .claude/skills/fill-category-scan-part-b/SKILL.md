---
name: fill-category-scan-part-b
description: Fill_category_scan_Part_B. The AI News Desk daily run, part B, in a Claude Code cloud session on this repo - from the finished Full Report it chooses the cards (14 to 15 story cards plus Fun, teaser, Bigger Picture, cover and closing) and the 7 Headlines stories, gets the wording from Fable, runs the plain English gate (script check and stranger check), shows Rafi the cards contact sheet and every Headlines line with its holographic screen, STOPS for his approval, then delivers every card and the Headlines ComfyUI JSON. Started by Fill_categories_scan_part_A when its products are delivered, or by Rafi to redo cards and Headlines.
---

# Fill_category_scan_Part_B

Rafi's name and spelling (3 Oct 2026). Lives ONLY in this repo, on branch claude/eager-archimedes-ajnex3, next to
part A: never on Drive, never merged to main, out of ChatGPT's reach; runs only in a Claude session connected to
this repo (CLAUDE.md rules 0 and 9). Video generation is not part of it: Rafi runs the JSON in ComfyUI on his PC.

Input: part A's working folder W of the same edition (final report_entries, facts, products/report_pdf.json, the
report markdown, bigger_picture_bulletin.json, rules/). Run alone (cards only, another day): point W at that day.

The RULES live in Drive and are fetched fresh (step 0); flag any clash with CLAUDE.md to Rafi in one line and follow
CLAUDE.md (rule 0):
- Cards_Master_Rules_Structure.txt (Card Master Permanent Assets, Drive 1mA6HnSS3McV7rVxSEyW5tjVUGzsqGQyT)
- Headlines_Master_Rules_Structure.txt (Blueprint_Library / Headlines blueprint; take the file of that name)
- Headlines_prompt_for_comfy_json.txt (Headlines Master Permanent Assets)
- AIMD_LV1_Adverts_Automation_Skill_V1.md (Prompt Library / prompts, Drive 124MVq-0ZTmlouD693MBb1j5diBTAn9pp)
- Article_phrasing_instructions_AIND_V1 (already in W/rules from part A): Cards level 6, Headlines level 5.
- CLAUDE.md rules 16 and 17 (counts, seconds rounded up, 12 s maximum, company caps, the Bigger Picture corner).

## Paths
```
B=/home/user/ai-news-desk/.claude/skills/fill-category-scan-part-b
S=$B/scripts
W=<scratchpad>/run_<YYYY-MM-DD>                      # part A's folder of this edition
PKG=<scratchpad>/cards_pkg/AIND_Cards_2026-09-10       # the card renderer, fetched in step 0
```

## Steps

### 0. Setup (Drive read only; skip what is already in place)
0. RESUME (a new session after the cloud machine was wiped): `git pull`, then
   `python3 <part A>/scripts/save_state.py --workdir <scratchpad>/run_<edition> --restore` rebuilds W from the repo copy
   `runs/<edition>` (report entries, facts, wording, pack, selection). Then continue at the first step whose output
   is missing: the cover and cards (step 5) and the JSON (step 6) are rebuilt in minutes; step 7 shows Rafi the
   sheet and the list again.
1. Fetch the four rule files above into `$W/rules/` with drive_save.py (part A, "Saving a Drive file to disk") and
   run `python3 <part A>/scripts/rules_diff.py --new $W/rules --old <last run>/rules`. Read every changed line.
2. If `$PKG/aind_cards.py` is missing: download AIND_Cards_Implementation_2026-09-10.zip (Drive
   13Ic8tAb_IgWFUTWgrzmC0eLp4OxCzk3V, 4,398,696 bytes, md5 598989503fa221cebe87c04bac903854) and unzip it into
   `<scratchpad>/cards_pkg/`. `pip install Pillow==12.3.0 fonttools==4.61.1` if missing.
3. If missing: the approved cover base cards_13-9-26_I01_VL1_presenter_preview.png (Drive
   1sizbDjBLJB_7K-3uRzZ4S_xI2zpCjdIs, 1,219,821 bytes) into `<scratchpad>/cards_pkg/drive_refs/`.
4. The Headlines template is in the skill: `$B/assets/Aind_headlines_comfy_template_13slots.json` (13 slots, the
   29 Sep reference pair, Spectrum on; md5 bbbed6ed8496ee80f04288468f597aa5). The voice sample is NOT needed here:
   the JSON only names AIND_anchor_voice_sample_4s.wav, which Rafi keeps in ComfyUI/input on his PC.

### 1. Choose on paper (main session)
```
python3 $S/card_candidates.py --workdir $W
```
It prints the NEW candidates per category (score, status, read or headline only, big company names, possible
repeats of the last decks) and writes `$W/cards_work/selection_draft.json`. Check it against the Cards rules
(criticals first and spending their slot; Rafi's order and slots; money cards at most 3; a robot doing something;
lead with the deed; one company at most 3 cards and 2 Headlines stories; NEW stories only; no repeat of the last
three days of cards and Headlines), write a short "label" for each card (the second level of its CATEGORY line,
at most about 15 characters), and save it as `$W/cards_work/selection.json` with: cards_in_deck_order,
teaser_items (3 to 4, categories not already on cards), headlines_story_clips_in_order (7, roughly half of the
story cards, deck order), headlines_fun, bp_refs (the entries the Bigger Picture card rests on).

### 2. Wording (2 Fable agents in parallel, 25 to 40 minutes: start at once)
```
python3 $S/make_wording_prompts.py --workdir $W
```
Launch both in ONE message with the Agent tool, model "fable", run in background:
`Read $W/cards_work/prompt_cards.txt and follow it exactly.` and `Read $W/headlines_work/prompt_headlines.txt and
follow it exactly.` They write `$W/cards_work/cards_copy_fable.json` and `$W/headlines_work/scripts_fable.json`.
While they work, do step 5's cover (it needs no wording).

### 3. The plain English gate (script check, then stranger check)
```
cp $W/headlines_work/scripts_fable.json $W/headlines_work/scripts_final.json
python3 $S/check_wording.py --workdir $W --cards $W/cards_work/cards_copy_fable.json --headlines $W/headlines_work/scripts_final.json
```
Fix every FAIL and shorten every clip marked long (story about 8 to 9 s, the news part about 90 s), keeping the old
file as `_old`. Then two fresh Fable agents (model "fable", in parallel, a few minutes each), which see only the
words: `Read $W/cards_work/prompt_stranger_cards.txt and follow it exactly.` and the same for
`$W/headlines_work/prompt_stranger_headlines.txt`. Read `stranger_result.json` in both folders; apply or improve
every fix (check facts and hedges against the entry; never add a fact), run check_wording.py again until it says
"all pass". 3 Oct 2026: 6 of 10 lines and 6 of 20 cards failed the first stranger check.
REPLY STORIES (Rafi, 4 Oct 2026): the script fails a card or clip of a reply story (pool follow_up plus reply words in its entry) unless it says it
is a reply AND names the earlier story ("Yesterday we carried a New York Times report: ...").

### 3b. Headlines rules recheck (Rafi, 4 Oct 2026; nothing goes to step 7 with a rules FAIL)
```
python3 $S/check_headlines_rules.py --workdir $W
```
It tests the Drive Headlines Master rules a script can test: deck order (A3), teaser only from the teaser card (A5),
approved ending and the opening slot (A2), timing aim and 12 s maximum (B1), spoken introductions (B2a), INTRODUCTIONS
ROTATE, never the previous day's wording (G2), numbers as words (B3), no outlet spoken (G1.4), pronunciation cues and
Google DeepMind (15 Sep), one company at most 2 story clips. Then one Fable agent (model "fable"):
`Read $W/headlines_work/prompt_rules_headlines.txt and follow it exactly.` It checks every clip against every rule of the
Headlines Master A, B, G and 15 Sep sections, the phrasing law 1, 1A, 1B and Cards Master Section 3 (company tags under
100 billion dollars, WHO, WHAT, WHY, deed first, the robotics clip shows what the machine does) and writes
`$W/headlines_work/rules_result.json`. Apply or improve every fix, then run step 3 and 3b again until both pass.
4 Oct 2026: the brief itself fixed "In <category>" and "And a lighter story" as lead-ins, so six of eight repeated the
previous day (rule G2), and Kawasaki had no tag (G1.2). The brief now points to the rules file and lists the previous
day's introductions.

### 4. Every factual claim against its entry
Read each final card and line next to its report entry: same attribution, same hedge, same number. A stronger
claim than the entry ("starts trading Monday" for "plans to, subject to approval") is rewritten.

### 5. Cards build
```
python3 $S/make_cover.py --workdir $W [--pkg <scratchpad>/cards_pkg]   # the approved cover, only the date changes
python3 $S/build_cards_copy.py --workdir $W
python3 $S/make_cards.py --workdir $W
python3 $PKG/aind_cards.py render --edition $W/products/cards_edition.json --lock $W/products/cards_content_lock.json --out $W/products/cards_runN
python3 $S/assemble_cards.py --workdir $W --run $W/products/cards_runN
```
The render folder must be new (cards_run1, cards_run2, ...). "UNVERIFIED: no review" lines are the normal draft
status. assemble_cards.py stops when a card is missing (a CATEGORY line that is too wide makes the renderer refuse
the card): shorten the label and render again. Look at the contact sheet yourself before showing it.

### 6. Headlines build
```
python3 $S/build_pack.py --workdir $W
python3 $S/fill_headlines.py --pack $W/headlines_work/headlines_D-M-YY_pack.json \
  --template $B/assets/Aind_headlines_comfy_template_13slots.json --out $W/products/headlines_D-M-YY_VL1.json
python3 $S/verify_headlines.py --json $W/products/headlines_D-M-YY_VL1.json
```
The fill refuses to overwrite: rename an earlier JSON `_old` first. C01 and C13 carry Rafi's opening and ending of
2 Oct 2026 (switch them to "bypass" in `$B/assets/pack_base.json` to use the stored clips).

### 7. STOP: Rafi's approval
```
python3 $S/review_list.py --workdir $W
python3 <part A>/scripts/save_state.py --workdir $W        # restart point before the wait
```
Send Rafi the contact sheet (SendUserFile, display render) and, in the chat, the review list: every Headlines clip
with the spoken words in bold and the holographic screen beside it, then the card wording. Ask for his approval or
edits in one line. Do not send the cards or the JSON before his approval. Edits: change the wording files, then
steps 3 (script check), 5 and 6 again (rename replaced outputs `_old`), and show the changed items only.

### 8. Deliver (after approval)
1. Send, one file at a time, never a zip: the contact sheet, then every card in order (I01 cover to the closing),
   then the Headlines JSON. One line: the 4 second voice sample must be in ComfyUI/input.
2. Drive (Rafi's standing yes of 3 Oct 2026 for the day's products):
```
python3 <part A>/scripts/delivery_manifest.py --workdir $W --part B
```
   Launch one background agent: `Read $W/products/drive_delivery_prompt.txt and follow it exactly.` (cards and the
   contact sheet into cards, the copy files into cards/supportive files, the JSON, pack and scripts into
   Headlines/supportive files). Then run the same command with `--check $W/products/drive_delivery.json` and tell
   Rafi what is on Drive and what the connection refused.
3. `python3 <part A>/scripts/save_state.py --workdir $W` once more (final wording and pack in the repo copy).
4. Report in short numbered points: cards (story cards plus extras), Headlines clips and seconds (news part, longest
   clip), the gate results, what is on Drive, anything open. Write what was learned into docs/V1_TASKS.md and the handoff.
5. Nothing passes the gate with a FAIL: a headline over 15 words, a body of three sentences or a clip over 12 s is
   fixed before step 7, never sent for Rafi to judge (the rule is in the law; only wording choices are his).

## Gotchas (2 and 3 Oct 2026)
- Fable writes well but slowly (25 to 40 minutes); a stalled agent gets one nudge with SendMessage, then a second
  agent. The stranger check is fast (about 5 minutes).
- Clip length sets the speaking pace, not the prompt words: cut words, never ask for faster speech.
- Never ask Rafi for what the record answers (the voice sample is on his PC; the JSON only names it).
- A card that repeats an earlier deck's story is a failure: card_candidates.py flags possible repeats; check them.
- The Bigger Picture card and clip name what to watch and why; the Bulletin version is the longer cousin.

## Files
- scripts/card_candidates.py (step 1), make_wording_prompts.py (2), check_wording.py (3), make_cover.py,
  build_cards_copy.py, make_cards.py, assemble_cards.py (5), build_pack.py, fill_headlines.py, verify_headlines.py (6), review_list.py (7),
  common_b.py (paths and dates).
- briefs/wording_common.md, wording_cards.md, wording_headlines.md, stranger_cards.md, stranger_headlines.md.
- assets/Aind_headlines_comfy_template_13slots.json (the ComfyUI template), assets/pack_base.json (pack fields and
  Rafi's opening and ending).
- make_cover.py calls the shared repo script scripts/card_cover_adjusting_script.py.
