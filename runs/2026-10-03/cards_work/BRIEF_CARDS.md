# Task: wording for the cards deck (Cards, reader level 6 of 10)
First read WORKDIR/cards_work/BRIEF_COMMON.md and WORKDIR/cards_work/selection.json (cards_in_deck_order, teaser_items). Style examples from the 2 Oct deck are in WORKDIR/../run_2026-10-02/cards_copy.json (some of those bodies were too dense: aim for simpler and shorter than them).
Write WORKDIR/cards_work/cards_copy_fable.json with this structure:
{"stories":[{"card":"s1","item":"C13-03","head":"...","body":"..."}, ... one per card in cards_in_deck_order incl. "fun"],
 "teaser":[{"id":"t1","item":"...","head":"..."}, ... 4 lines],
 "bp":{"head":"...","body":"..."}}
Limits (the renderer refuses text that does not fit):
- Story card head: one sentence, at most 85 characters (three lines at the fixed size). Prefer 70 to 85.
- Story card body: exactly TWO sentences, at most 230 characters in total: sentence one says what actually happened in real-world terms; sentence two says why it matters or gives the honest doubt (who says it, what is unconfirmed). Each sentence at most 15 words.
- Teaser line: one short sentence, at most 90 characters, plain words, the deed first.
- BP card ("And for the bigger picture..." card, pill DESK VIEW): head one sentence at most 85 characters that SUMS UP the big thing happening that moves the market today (plain words, no jargon); body at most 160 characters in two short sentences: what happened, then what to watch. Source for the BP: WORKDIR/bigger_picture_bulletin.json (the short desk analysis; you may only use facts from it and from the entries it rests on).
- The Fun card: light tone, still precise, same limits as a story card.
Do not put the outlet name in the head. In the body you may mention who said it only when needed for a hedge ("a start-up says", "a union group says").
Validate with python json.load. Final message: one line only ("cards wording written").
