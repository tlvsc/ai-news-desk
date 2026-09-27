# digest (cheap tier)

Task: turn each collected article into a tiny factual record. This is the only time the raw text is read, so capture every concrete fact now.

For every item in PAYLOAD.items return one digest with the same id.

Rules
- headline: one factual line, at most 140 characters, present tense, no clickbait, no source name.
- summary: one or two complete sentences, at most 400 characters, only facts present in the text or title.
- key_facts: two to five short strings. Each carries a concrete fact: a number, a name, a date, a place, a decision. Copy numbers exactly as written.
- entities: up to four organisation or product names that appear in the text.
- event_date: the date the event happened if the text states it, as YYYY-MM-DD, otherwise "".
- ai_relevant: false when the article is not about artificial intelligence, machine learning, robotics driven by AI, AI chips, AI policy or AI companies.
- fun: true only for light, quirky or humorous stories.
- category_guess: one key from POL, MKT, SEC, ENE, ROB, MOD, RES, LAW, HEA, SOC, FUN. Use category_hint only when the text agrees with it.
- If text is empty, digest from the title alone and keep key_facts to what the title states.
- Never add facts, never guess numbers, never merge two items.

Output JSON exactly:
{"digests": [{"id": "...", "headline": "...", "summary": "...", "key_facts": ["..."], "entities": ["..."], "event_date": "", "ai_relevant": true, "fun": false, "category_guess": "MOD"}]}
