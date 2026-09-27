# dedupe_pairs (cheap tier)

Task: for each pair of digests decide whether both describe the SAME news event (same actor, same action, same day), not merely the same topic or company.

Same event examples: two outlets reporting one product launch; a press release and an article about it.
Different event examples: two different lawsuits against the same company; a funding round and a product launch by the same startup; a follow-up development a day later that adds a new decision.

For every pair in PAYLOAD.pairs return a and b unchanged, same_event true or false, and a reason of at most 12 words.

Output JSON exactly:
{"pairs": [{"a": "...", "b": "...", "same_event": true, "reason": "..."}]}
