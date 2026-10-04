# Tasks for V1 (not for this temporary session)

Recorded here so they are not lost; the project's task list lives on Drive
(AI News Desk — Project Task List) and Rafi copies them there (rule 0).

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
