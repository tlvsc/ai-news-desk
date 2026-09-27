# cards_copy (mid tier)

Task: write the card copy for every story in PAYLOAD.items and the teaser lines in PAYLOAD.teaser, under PAYLOAD.law and PAYLOAD.rules (Cards Master Section 3).

For each story card
- head: one complete sentence, at most 110 characters, ending with a period. Names the actor and the deed. Non-market cards never open with money; funding, revenue and valuation stay out of the head and the first body sentence.
- body: exactly two sentences, at most 260 characters together: what happened with the key number or name, then why it matters or the honest doubt.
- cat: the category line "Category / two-word topic", for example "Robotics / Warehouse robots".
- src: the source name in capitals, as given in the item, for example "REUTERS".
- pill: copy the item's verification status exactly (CONFIRMED, REPORTED, PRELIMINARY or DISPUTED).

For each teaser line
- head: one line, at most 90 characters, a complete sentence ending with a period.
- cat: the category name.

Only facts from headline, summary and key_facts. Unfamiliar companies get a short title. Plain words, no jargon.

Output JSON exactly:
{"cards": [{"id": "...", "head": "...", "body": "...", "cat": "...", "src": "...", "pill": "REPORTED"}],
 "teaser": [{"id": "...", "head": "...", "cat": "..."}]}
