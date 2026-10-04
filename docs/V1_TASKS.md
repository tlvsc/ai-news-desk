# Learned in the temporary scan runs, and tasks for V1

THE ONE LIST (Rafi, 4 Oct 2026): everything learned while running the temporary Claude scan (27 Sep 2026 onward) is
collected in this file, so that when V1 is ready the whole list moves to V1 at once. Every run adds its lessons here
(Part B step 8). Not for this temporary session to apply on Drive; the V1 task list on Drive is AI News Desk — Project
Task List (00 PROJECT OS, a Google Sheet), which this session cannot write into (rule 0 and the connector), so Rafi or
Astra copies items there.

Part 1, below the line of 27 Sep to 1 Oct, was copied on 4 Oct 2026 from the scratchpad lesson list of 30 Sep and the
Claude lane handoffs 28B and 29A, which live only on the cloud machine and are lost when it is wiped.
Part 2 starts at item 1 (2 Oct 2026) and is numbered as before.

## Part 1: learned 27 Sep to 1 Oct 2026 (status checked against the repo on 4 Oct 2026)
P1-1. Scan window 24 hours, 30 only on request. Applied: CLAUDE.md rule 16, collect.py.
P1-2. Read the source sites directly, not only Google News. Applied 2 Oct: source_scan.py, the 55 sources.
P1-3. Fun Side 5 to 10 in the Full Report, no repeats, top 3 in the Bulletin. Applied: house rules, skill, Drive rules.
P1-4. Bulletin cutoff lands near 30 to 50 stories; Full Report 5 and up plus Fun, flexed past about 150 or very few;
      always state cutoff and count (Rafi, 28 and 29 Sep). Applied: CLAUDE.md rule 14, build_products.py.
P1-5. Everything final goes to its Drive place; what the connector cannot upload, Rafi uploads. Applied: rule 0
      standing yes of 3 Oct and delivery_manifest.py. Binaries still never pass (see item 53).
P1-6. Cards 14 to 15 story cards, about half to Headlines; one company at most 2 Headlines stories, 3 cards; money
      cards at most 3; a headline only story gets a cautious card (Rafi, 29 and 30 Sep). Applied: house rules, card_candidates.py.
P1-7. Headlines news part about 90 s (7 stories of 8 to 9 s, Fun 8, teaser 8, Bigger Picture 10), every clip rounded
      UP to the next half second. Applied: check_wording.py, fill_headlines.py.
P1-8. Hologram: the prompt sets the border and what shows inside; the opening shows the Earth, then the logo circling
      it. The 28 Sep opening was good, the 29 Sep one was not. Applied: pack_base.json carries the 2 Oct opening.
P1-9. When Rafi asks for the stories in the JSON, show only the spoken words, not the prompt. Applied: review_list.py.
P1-10. Send files one at a time, never one big zip (phone storage). Applied: both skills, step 13 and step 8.
P1-11. One source of truth per rule, one home per rule, no copies (Rafi, 30 Sep). OPEN: the proposals below.
P1-12. Remove a story by its title, not its number; a story picked in two categories stays where it is a main pick;
       real links are kept by the Google link, not the story number. Applied: build_pool.py, tested.
P1-13. Never rebuild the pool after the writers start (item numbers shift). Applied: skill step 3.
P1-14. Full network access: 128 of 235 articles readable instead of 38 (30 Sep). Applied: environment setting.
P1-15. Check recent reports properly before suggesting extra stories (a broken check suggested repeats on 30 Sep).
       Applied: the four day repeat list (item 28).
P1-16. Check the approved opening before writing a new one. Applied: house rules 16 OPENING AND ENDING OPTIONS.
P1-17. Never build before Rafi's yes (house rule 4; broken on 30 Sep). Standing.
P1-18. A pgrep watcher matched itself and wasted about 45 minutes. Applied: run_in_background in the skill.
P1-19. Stop at every automatic compaction; approval to continue once does not cover the next one (28 and 29 Sep,
       and again 4 Oct, item 49). Applied: CLAUDE.md rule 18.
P1-20. Match Rafi's numbered answers against the original list in the record before acting (a recap read "7) yes" as
       a yes to the wrong item on 28 Sep). Standing.
P1-21. Show each step and wait for yes; never drop categories or write card text before asking (29 Sep). Standing.
P1-22. Mistakes of 30 Sep: old 8 story JSON sent inside the zip; hologram wording Rafi had not approved; product rules
       copied into the house rules without asking where each rule lives.
P1-23. Proposals of 30 Sep, no decision found in the record on 4 Oct (Rafi decides):
       (a) house rule 8 to say each instruction is written once in its one home (product rules in that product's Drive
           rules file, how Rafi works in CLAUDE.md), with pointers instead of copies. CLAUDE.md rule 8 still has the old wording.
       (b) the voice walkthrough applies only when Rafi asks for one (his preferences now say so: ANSWERS IN POINTS).
       (c) rule 10 exception: the opening logo animation around the globe may be generated, as approved. Not in CLAUDE.md.
       (d) move rule 16 and the counts of rule 14 out of the house rules into the Drive rules files, leaving pointers.
P1-24. Open from 28 to 30 Sep, not checked since: Bulletin rules file section 4 "scored 7 to 10" versus the flexible
       cutoff; cover script move to Card Master Permanent Assets not approved; Astra task file still says 8 stories and
       the old slot map; project pictures in the AI_News_Desk root waiting for Rafi's sort decision.

## Part 2: learned from 2 Oct 2026 on

1. (2 Oct 2026) PLAIN ENGLISH GATE for every card, Headlines line and article. Before any render
   or JSON fill, every headline and body passes two checks: (a) a script check against
   Article_phrasing_instructions_AIND_V1 (sentences of at most 15 words, the banned words, no
   "X reports that" opening on a card, at most one number per sentence); (b) a stranger check:
   a fresh agent that has not seen the story retells each item in one sentence a 12-year-old
   would say; if it cannot, the item fails. Results go to Rafi as a table before render.
   Headline model (Rafi, 2 Oct 2026): first the deed in picture words, then the explanation
   underneath. Reference example: card 13 of 2 Oct 2026, before and after.
   Naming: call the rules file by its Drive name, Article_phrasing_instructions_AIND_V1, never
   by its inside title; the file's own first line still carries the old title (Rafi's edit).

## Rules of the last three days that live only in this repo and should go into the V1 Drive files (listed 2 Oct 2026, Rafi's ask)

1. 24 hour scan window, 30 only on request (CLAUDE.md 16). No Drive file has it.
2. The 55 sources read directly after Google News, 15 to 20 stories per category (CLAUDE.md 16, SKILL step 1b). No Drive file has it.
3. One company at most 2 Headlines stories and 3 story cards (CLAUDE.md 16). Not in Cards or Headlines rules.
4. The 13 slot template, Bigger Picture as its own clip 11, stored ending in slot 13 (SKILL, fill script). Headlines rules still say twelve slots.
5. Hologram border and text free symbol lines in the generation prompt (fill script, 30 Sep). Not in the Drive prompt file.
6. Clip seconds rounded up to the next half second (CLAUDE.md 16). Drive rule B1a says do not round; Rafi to settle.
7. Bigger Picture as market summation plus things to watch, at three lengths, with a Bulletin section (CLAUDE.md 17, build_products.py). Not in Full Report, Bulletin or Cards rules.
8. Headline model (the deed in picture words first), 15 word sentences, stranger check (task 1 above). Not in Article_phrasing_instructions_AIND_V1.
9. Repeat check against the last three days of cards and Headlines, not only yesterday's pool.
10. Rule files called by their Drive name only.
11. 8 sampler steps, the 4 second voice sample, the unhurried presenter tone (CLAUDE.md 16, 2 Oct). Headlines rules say six steps; the prompt file has the old tone. Move after the 2 Oct clips prove it.
12. Opening and ending regenerated as options on request, stored ones stay approved until Rafi picks (CLAUDE.md 16, 2 Oct).
Already in Drive, nothing to port: report and Bulletin cutoffs, Fun Side top 3 in the Bulletin, bypassed opening and ending.

## Learned on 2 Oct 2026 after the porting list above (recorded the same day, Rafi's ask)

13. SPEAKING SPEED: the clip length sets the pace, not the prompt words. At 4.4 syllables per second,
    with the final second reserved for the hands and breaths between stories, the presenter rushes.
    Test on the 3 in 1 prompt by changing only the seconds: 24.5 (now), 25.5 (plus 1 s hold),
    26.5 (4.0 per second), 27.5 (4.0 plus 1 s hold, recommended). Rafi picks; then the formula
    changes in the fill script, CLAUDE.md rule 16 and, later, Drive rule B1a.
14. LONG CLIPS: a 24.5 s clip with three stories was tried on 2 Oct; nothing over 12 s was tested
    before. Record the result (pose, lip sync, screen) before allowing long clips.
15. SCREEN INSTRUCTIONS AS TIMELINES: write the hologram screen as absolute seconds inside the clip
    (0.0 to 0.5 logo, fades, picture, logo back, hold to the end), with "no readable text" and the
    reflection line. Used for the 2 Oct opening and ending; if they render well, this style goes
    into the Drive prompt blueprint.
16. ENDING SCREEN: like, follow and share as text free symbols (thumbs up, person with plus,
    share arrow), never words; logo back before the end.
17. TEST JSON METHOD: a short subset at base 544x960 only (upscale saves off) with _test30 output
    names, same seed and settings, to check new settings before the full run.
18. VOICE SAMPLE: AIND_anchor_voice_sample_4s.mp3 (first 4 s of the 8 s sample, stream copy, 192 kb/s)
    exists only in this session and on Rafi's PC; it belongs in Headlines Master Permanent Assets
    (Rafi uploads).
19. STRANGER CHECK RESULTS: a line fails when it needs background knowledge (S I = super
    intelligence), when a watch item is named without why it matters, or when two facts sound like
    one. Fix the line, not the reader.
20. FIND FIRST, WRITE SECOND: when Rafi names a project file, locate it on Drive and say where it
    is before writing anything anywhere.
21. SHEETS GAP: this session's Drive connection cannot write into a Google Sheet; the Project
    Task List is a Sheet. Connect Google Sheets to Claude, or Rafi/ChatGPT adds the row.
22. CARD COPY MODEL: ask Fable for card and Headlines wording; the owner's headline for card 13
    (the deed first: judge rejected lawsuits over Google summing up websites instead of linking)
    is the reference; five rewrites were needed on 2 Oct because no gate existed.
23. REPEATS: cards 8 and 10 of 2 Oct (Google satellite, Microsoft Copilot) had been reported on
    earlier days; the repeat check must cover the last three days of cards and Headlines.
24. CREDIT CLASH: Full Report rule 6.1 (link the original) versus the writer brief (credit the
    outlet read when the original is blocked); 7 stories on 2 Oct credit wire copies. Rafi to settle.
25. 14 of 15 story cards on 2 Oct fail the 15 word check; left as they were by Rafi's choice.
    The gate (task 1) prevents this from the next run.

## Learned on 3 Oct 2026, the first run with 16 curators at 10 items each (recorded the same day, Rafi's ask)

26. POOL MATH: 16 curators times 10 gave 160 only after a filler agent found a tenth item for one category;
    21 cross category duplicates and 1 repeat URL were removed, and the 3 backups per category filled the gaps.
    Keep the 3 backups, and add a filler step when a category ends below its count.
27. FEWER SURVIVE THAN THE POOL: the writers lowered about 40 scores and 29 stories were held as older news or
    duplicates, so a pool of 160 gave a Full Report of 112 at score 5 and up (not 150) and a Bulletin of 28 at 7 and up
    (not 30 to 50). For about 150 the pool must be about 230, or the cutoff drops to 4.
28. FOUR DAY REPEAT LIST: curators check 968 titles from 29 Sep to 2 Oct. It cut about 90 percent of the Models candidates,
    so thin categories (Models, Quantum, Developer Tools, Robotics) need extra queries (one curator ran about 150).
    The 2 Oct pool was never on Drive (rule 0), so tomorrow's repeat check needs today's pool file from Rafi.
29. FOLLOW UPS: cards and Headlines take only stories whose freshness is NEW. Follow ups of a card story (the Anthropic
    share sale, the Broadcom loan) go to the Bigger Picture or the teaser, not to a story card.
30. DRIVE RULES CHANGE BETWEEN RUNS: on 2 Oct after the morning fetch the Full Report and Bulletin rules, the phrasing file
    (now with reader levels: Full Report 7, Bulletin 7, Cards 6, Headlines 5), the Headlines Master (each clip aims at 8 s,
    12 s at most, never speed up) and the Cards rule all changed. Fetch every governing file fresh and diff it against the
    last copy; a helper agent does this in under a minute.
31. BRIEFS ARE OUT OF DATE: the writer and editor briefs still say "level five" and name the old phrasing file; the Drive
    file says 7. Rule 0 kept level five. Rafi to pick; then fix the briefs and SKILL.md in one change.
32. WRITER BRIEF GAP: nothing says no proxies or crawler user agents; one writer probed a blocked site through a reader
    proxy (nothing was used). Add the line.
33. prefetch.py (fetches all article text once) lives only in the scratchpad, not in the skill. Add it to scripts.
34. BLOCKED SOURCES: 71 of 160 stories had no readable text on the first fetch and 28 stayed headline only (WSJ, FT,
    Bloomberg, Reuters, MLex). Many writers read a wire copy and credited it, which keeps the credit clash open.
35. STRANGER CHECK WORKS AND IS NEEDED: first drafts failed 6 of 10 Headlines lines and 6 of 20 card items. Failure types:
    "it" with no referent, "the photo" with no setup, background words (memory, chip machine), a watch item without why,
    two facts that sound like one. Fable drafting took 25 to 36 minutes; the check about 5. Start drafting early.
36. RENDER CHECK: a card whose category line is too wide (CROP) is silently left out of the run. After every render count
    the card files against the card list. Keep the category label short ("Market, industry and finance / Funding").
37. CLIP SECONDS: Fable's first lines ran 9 to 11 s each (news part 100 s plus); trimmed to 8 to 10 s (news part 94 s).
    Give writers a syllable budget (about 35 to 40 for a story, 46 for the Bigger Picture), not a word budget.
38. BIGGER PICTURE: the card and clip need a reason to watch each item (a stranger asked "why the Fed meeting?").
    The Bulletin version carries no item numbers; the Full Report version cites them.
39. BULLETIN BALANCE: at 7 and up the Bulletin had no Politics story and one Robotics story. Check category spread before
    sending; consider 6 and up, or the auto cutoff.
40. DRIVE HAS A NEW V1 FOLDER (2 Oct 20:33): scripts aind_v1_report, taxonomy (19 sections, not the 16 LV2 categories),
    headline_script, media, schedule and a test file. Not run here. Rafi to say if this session should ever run them.
41. NEVER ASK WHAT THE RECORD ANSWERS: the Headlines JSON only names the voice sample; the file sits on Rafi's PC
    (I made it on 2 Oct and sent it). Part B never handles audio.
42. THE DAILY RUN IS NOW TWO CHAINED SKILLS (Rafi, 3 Oct 2026): Fill_categories_scan_part_A and Fill_category_scan_Part_B,
    repo only. Every tool that lived in the scratchpad (article fetcher, card builders, cover wrapper, Headlines fill
    and pack, the 13 slot template, Rafi's opening and ending) is now in the skills. Tested 3 Oct on that day's data:
    Part B rebuilt the 19 cards byte for byte and the same Headlines JSON. For V1: port the order of work, not the files.
43. THE NEW SCRIPT CHECK found that the 3 Oct Bigger Picture card headline has 17 words (limit 15); it went out
    before the check existed.
44. (3 Oct 2026, mistake record) Two skill rules were put to Rafi as questions about single stories (a 17 word
    headline, the robotics pick). Prevention: a rule that the gate or a script can enforce is never a question;
    only a wording choice or a judgement between two correct options goes to Rafi. Fix: the gate fails any sentence
    over 15 words before anything reaches him; the writer marks machine_action and the selector uses it.
45. (3 Oct 2026) Rafi's decisions: the skills save the day's products to the Drive date folders (standing yes);
    a text copy of the working files lives in the repo under runs/<date> as the restart point (about 4 MB a day;
    V1 decides where this lives long term); a morning Routine only after two clean manual days. Still open: the
    credit rule (explained to Rafi, his pick pending).
46. (3 Oct 2026) CREDIT RULE settled by Rafi: credit the outlet that reported the story, never the copy site;
    a story that credits another outlet credits that outlet; headline only means another outlet or our own
    desk entry labelled AI News Desk. The Drive Full Report rule 6 says nothing about blocked originals: V1
    should add this wording there (Rafi edits Drive).
47. (3 Oct 2026) The Bigger Picture card label reads AIND, not DESK VIEW (Rafi). Drive still says DESK VIEW in
    Cards_Master_Rules_Structure 1.3 and 3.5 and Article_phrasing_instructions_AIND_V1 section 3.2: V1 wording to change.
48. (4 Oct 2026) WRITE ONLY WHAT CAN PRINT (Rafi): articles only for pool score 5 and up plus Fun; 3 Oct data: 136 of
    160 written instead of 160, about 15 percent less reading and writing. make_chunks.py --min-score, --only-missing.

49. (4 Oct 2026) CONTEXT COMPACTION happened before the 4 Oct run started. Mistake: kept working in a heavy
    chat instead of proposing a fresh one after the skill build. Fix recorded as CLAUDE.md rule 18 (fresh chat
    before a run). Handoff: docs/HANDOFF_2026-10-04.md. Rafi approved continuing the 4 Oct Part A in the same chat.
50. (4 Oct 2026) REPLY STORIES (Rafi, 4 Oct 2026): card 5 (Altman on AI and religion) did not say it answered the Anthropic story of our 3 Oct
    edition; card 6 and its clip did not link Robinson's essay to his exit we reported on 3 Oct. Rafi's rule: a reply
    names and explains the story it answers. Now in CLAUDE.md rule 16, writer, editor, wording and stranger briefs,
    qa_check.py (reply_without_earlier_story) and check_wording.py (FAIL). Cards 5 and 6 and clip 4 rewritten.
51. (4 Oct 2026) OPEN, LATER (Rafi: "fix this in the other version, but not now"). Follow-up and reply stories, the upgrade
    of item 50: (1) the checks fire on every follow-up (the curator's follow_up mark), not on reply words; (2) make_chunks.py
    gives the writer the earlier story's headline, outlet and date from the earlier pool; (3) the full rule stays only in
    CLAUDE.md rule 16, the briefs keep one-line pointers; (4) "yesterday" only when it was yesterday, else the date or
    "in our 3 Oct edition". Same task for the other versions on Drive: V1 (its task list is AI News Desk — Project Task List
    in 00 PROJECT OS, a Google Sheet) and V2 (no task list; the AIND V2 Open Questions and Decision Register). The V1 task list
    and the V2 Open Questions and Decision Register cannot be edited from this session (the connector only renames or
    moves files); Rafi or Astra adds the row from the text given in chat on 4 Oct 2026.
52. (4 Oct 2026) THE V1 TASK LIST on Drive is AI News Desk — Project Task List in 00 PROJECT OS (a Google Sheet; its
    Workflow tab is all V1). V2 has no task list, only the AIND V2 Open Questions and Decision Register. Mistake: I called
    the V1 list "shared" from its title alone. Prevention: read what a list covers before naming whose it is.
53. (4 Oct 2026) DRIVE DELIVERY LIMIT: the connector carries only typed text. Of 9 Part A files, 4 reached Drive (two .md
    reports, report_pdf.json, bulletin_pdf.json); both PDFs, the pool CSV and JSON and daily-pool.md were refused (too
    large or binary), the same as 3 Oct. It also cannot write into a Google Sheet or edit a file's content (update_file
    only renames or moves). V1 needs an upload step on Rafi's PC (or Astra) for PDFs, cards, pool files and the JSON.
54. (4 Oct 2026) WEEKEND WINDOW (Sat 08:20 to Sun 08:20 UTC): thin categories after the four day repeat list
    (Developer Tools 13 after a filler, Business 10, Chips 11, Security 11); 111 articles written, 28 held (26 re-dated, 2
    duplicates). Copy sites re-date old stories: EnergyNow and Stocktwits carried Bloomberg and Reuters stories from March,
    April and August with new dates. Writers caught them from the text; qa_check held them.
55. (4 Oct 2026) GATE TREND: first stranger check failed 4 of 10 Headlines lines and 5 of 20 card items (3 Oct: 6 and 6).
    Main failures: a name never introduced (TSMC, Gemini, Terafab, Anthropic), jargon ("models", "debt watchers"), an
    idiom ("own their risks"). Fable wording took 2.5 and 5.5 minutes, not 25 to 40.
56. (4 Oct 2026) RENDER CROP AGAIN: the label "Hong Kong IPOs" made the Market category line too wide and the renderer
    refused the card; "Hong Kong" fit. With the long Market category name, labels stay at about 10 characters.
57. (4 Oct 2026) BULLETIN SPREAD: at 6 and up the Bulletin had no Ethics and law and no Society story (5 and up gave 79,
    too many). V1 may need one guaranteed slot per category in the Bulletin.
58. (4 Oct 2026) DRIVE RULE CHANGE: Headlines Master Section D1 was rewritten on 3 Oct 20:30 UTC: the layout image
    instagram_pixels_boundary_stirps_subtitles is the only layout authority; the source strip moves to the top under the
    date strip, subtitles sit at x 180 to 890, y 1356 to 1535. It affects the video post on Rafi's PC, not the JSON.
59. (4 Oct 2026) THE ONE LIST (Rafi): all lessons of the temporary scan runs live in this file, to move to V1 when V1
    is ready. Older lessons of 27 Sep to 1 Oct were copied in as Part 1.
