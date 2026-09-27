# bulletin_copy (mid tier)

Task: rewrite every item in PAYLOAD.items as a Daily Bulletin entry under PAYLOAD.law (the AIND plain language law).

For each item
- headline: one complete spoken sentence a newsreader could say, ending with a period. Name the actor. Unfamiliar companies get a short title ("robot brain startup Skild"). Non-market stories lead with the deed, not the money.
- body: exactly two sentences. Sentence one: what happened, with the key number or name. Sentence two: why it matters, or the honest doubt.
- Only facts in headline, summary and key_facts. Never add a fact. Keep verification wording ("reportedly", "says") when the item is REPORTED or PRELIMINARY.
- No jargon, no hype words, no acronyms without the plain meaning.

Output JSON exactly:
{"items": [{"id": "...", "headline": "...", "body": "..."}]}
