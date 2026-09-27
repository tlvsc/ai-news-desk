# editorial_qa (strong tier)

Task: the final editorial check of a product (cards copy or Headlines scripts) in PAYLOAD.product against its source items in PAYLOAD.sources and the rules in PAYLOAD.rules.

Check, one result per check
- facts: every claim is supported by the sources; numbers, actors and dates match.
- certainty: reported or preliminary items are not stated as certain.
- language: plain language law: no jargon, short sentences, numbers as words in spoken scripts.
- structure: the order and count follow the rules given.
- money: non-market items lead with the deed, not the money.

status: APPROVED when every check passes; CHANGES when any check fails. corrections: one entry per failing item with id, field, problem and a proposed corrected text (only from the sources).

Output JSON exactly:
{"status": "APPROVED", "checks": [{"name": "facts", "result": "PASS", "note": "..."}], "corrections": [{"id": "...", "field": "...", "problem": "...", "proposed": "..."}]}
