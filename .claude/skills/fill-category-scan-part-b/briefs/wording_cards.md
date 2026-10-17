# Task: wording for the cards deck (Cards, the reader level and the writing shape in its product section of WORKDIR/rules/Article_phrasing_instructions_AIND_V1.txt (the only place they are set))
First read WORKDIR/cards_work/wording_common.txt and WORKDIR/cards_work/selection.json (cards_in_deck_order, teaser_items, bp_refs). WORKDIR = {WORKDIR}. Style example from an earlier deck: {PREV_CARDS} (aim simpler and shorter than any dense body there).
Write WORKDIR/cards_work/cards_copy_fable.json:
{"stories":[{"card":"s1","item":"...","head":"...","body":"..."}, ... one per card in cards_in_deck_order including "fun"],
 "teaser":[{"id":"t1","item":"...","head":"..."}, ... one per teaser item],
 "bp":{"head":"...","body":"..."}}
Limits (the renderer refuses text that does not fit):
- Story card head: one sentence, at most 85 characters (three lines). Prefer 70 to 85.
- Story card body: exactly TWO sentences, at most 230 characters: what actually happened in real-world terms, then why it matters or the honest doubt (who says it, what is unconfirmed). Each sentence at most 15 words.
- Teaser line: one short sentence, at most 90 characters, the deed first.
- Bigger Picture card ("And for the bigger picture" card, label AIND): head one sentence of at most 85 characters that sums up the big thing happening that moves the market today; body at most 160 characters in two short sentences: what happened, then what to watch AND why. Source: WORKDIR/bigger_picture_bulletin.json and the entries named in bp_refs only (CLAUDE.md rule 17).
- The Fun card: light tone, still precise, same limits as a story card.
Validate with python json.load. BEFORE YOU HAND BACK (Rafi, 12 Oct 2026): run python3 /home/user/ai-news-desk/.claude/skills/fill-category-scan-part-b/scripts/check_wording.py --workdir WORKDIR --cards WORKDIR/cards_work/cards_copy_fable.json and fix every FAIL yourself, at most two rounds; never hand back a FAIL without saying so. Later you may get a message listing only the cards the checker flagged: fix only those, run the script again and rewrite the file. Final message: one line only ("cards wording written").

POST TEXT FOR THE CARDS (Rafi, 17 Oct 2026, his words: "one hook for card one for headline and one click copy"; "Do it the same as the other days. Icon with a hook."). After the cards pass, also write WORKDIR/cards_work/post_text.txt, plain text, exactly this shape (the 17 Oct text is the model):
line 1: one icon, then a hook of one or two short sentences built on the day's strongest or most surprising card.
blank line, then the 7 biggest story cards, one plain sentence each, in deck order, facts only from the cards.
blank line, then "The Bigger Picture: " and the Bigger Picture card in one sentence, then "This is not financial advice."
blank line, "AI News Desk", blank line, then 5 hashtags naming the biggest companies in the day's cards (for example #Tesla #Anthropic #OpenAI).
Same plain words as the cards; no dashes, no rule words, no closing question. (Mine, not yours: the wording of this block.)
