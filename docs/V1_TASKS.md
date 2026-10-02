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
