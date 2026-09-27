# meaning_check (mid tier)

Task: the 26 September source-to-script meaning check. For every item in PAYLOAD.items compare the written copy (PAYLOAD.items[].written, any fields) against the source facts (PAYLOAD.items[].source_facts).

Decide
- PASS: every claim in the written copy is supported by the source facts and nothing important was dropped or reversed.
- FAIL: the copy states something the facts do not support, reverses a meaning, drops the central fact, or turns a report into a certainty.
- UNVERIFIED: the facts are too thin to judge.

Report
- missing: important source facts the copy dropped (short strings, may be empty).
- unsupported: claims in the copy that the facts do not support (short strings, may be empty).
- note: at most 20 words.

Be strict about numbers, actors, dates and causality. Wording differences are fine.

Output JSON exactly:
{"results": [{"id": "...", "result": "PASS", "missing": [], "unsupported": [], "note": "..."}]}
