# bigger_picture (strong tier)

Task: write The Bigger Picture, the daily analysis corner, from PAYLOAD.items (the Daily Bulletin) only. Names, description and opening words are in PAYLOAD. Follow PAYLOAD.rules.

Produce
- head: the analysis headline for the card, one sentence, at most 90 characters.
- card_body: two sentences for the card: the pattern you see today, then what it could mean for technology, business or everyday life.
- items: two to four one-line desk observations, each ending with the report item numbers it rests on in brackets, like "(report items 3, 12)".
- spoken: the reel narration for the Bigger Picture clip. It MUST start with the exact opening words in PAYLOAD.opening (without the ellipsis, followed by a comma), be one or two sentences, and run between PAYLOAD.spoken_syllables[0] and PAYLOAD.spoken_syllables[1] syllables. Numbers as words. Plain language.
- full_markdown: the full analysis document body in markdown: three to five short paragraphs with bold lead-ins, then a "Why it matters" list, citing report item numbers in brackets. At most 400 words.
- report_refs: the list of report item numbers used.

Desk judgement, clearly separated from reported facts. No investment advice, no price targets.

Output JSON exactly:
{"head": "...", "card_body": "...", "items": ["..."], "spoken": "...", "full_markdown": "...", "report_refs": [1, 2]}
