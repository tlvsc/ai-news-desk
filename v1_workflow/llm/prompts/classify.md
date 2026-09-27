# classify (cheap tier)

Task: for every event in PAYLOAD.events assign a category, an importance score, a verification status and one line on why it matters. Use PAYLOAD.categories and PAYLOAD.scoring_rules.

Rules
- category: one key from PAYLOAD.categories. Robotics means a robot or autonomous machine doing something. Policy about robots is POL; money about robots is MKT.
- subcategory: two to four words.
- importance: integer 1 to 10. 10 only when the event changes what AI can do, affects many people, or is a major government or court decision. A big dollar figure alone is never a 10. 8 to 9 for major company, model or policy news. 6 to 7 for solid news of interest to one audience. 1 to 5 for minor or incremental items.
- label: CRITICAL for 10, HIGH for 8 to 9, MEDIUM for 6 to 7, WATCHLIST for 1 to 5.
- verification: CONFIRMED when a primary or official source is among the sources; REPORTED for credible attributed reporting; PRELIMINARY for early or single-source claims; DISPUTED when sources conflict.
- why_it_matters: one plain sentence, at most 25 words, no jargon.
- big_name: true when the actor is a major AI company, a national government or a global institution.

Output JSON exactly:
{"classified": [{"id": "...", "category": "MOD", "subcategory": "...", "importance": 7, "label": "MEDIUM", "verification": "REPORTED", "why_it_matters": "...", "big_name": false}]}
