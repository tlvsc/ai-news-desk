# headlines_copy (mid tier)

Task: write the spoken narration for the Headlines reel clips in PAYLOAD.items, plus a text-free screen symbol for each. Follow PAYLOAD.rules.

Every item has kind: story, fun, teaser or bigger_picture, a target syllable count and an allowed range.

Narration rules
- story and fun: start with a short natural spoken introduction suited to the subject ("In robotics.", "Now the money.", "And a lighter one."). Rotate wording; never reuse an introduction listed in PAYLOAD.previous_intros. Then one or two sentences with the deed first, the key fact, and the actor named. About 35 syllables including the introduction; stay inside the range.
- teaser: starts with "Also in the full report:" or "More in today's full report." then names two or three of the teaser_items as short clauses. Never a story that already has a clip.
- bigger_picture: starts with the exact words "And for the bigger picture," then one or two sentences of desk analysis from the given head, summary and key_facts. Between 44 and 53 syllables.
- Numbers as spoken words ("twelve billion dollars", "twenty twenty-seven"), never digits. Say percent, not the sign.
- Plain language, no jargon, unfamiliar companies get a short title, no hype.
- Only facts in the item. Never add a fact.
- When an item carries "fix", rewrite the current_script to solve the stated problem and keep everything else.

Symbol rules (the hologram pane shows it instead of the logo)
- A simple glowing icon that fits the story, ending with "simple text-free symbol". No people, no faces, no letters, no numbers, no flags, no logos, no dates.

Output JSON exactly:
{"items": [{"id": "C02", "script": "...", "symbol": "..."}]}
