# analysis (strong tier)

Task: write the FORWARD-LOOKING ANALYSIS section of the Daily Global AI Intelligence Report from the numbered items in PAYLOAD.items (headline, label, category only). PAYLOAD.previous_analyses holds excerpts of recent editions so you do not repeat yesterday's framing.

Rules
- Desk judgement, clearly separated from reported facts. Cite item numbers in brackets like [12] after each claim that rests on an item.
- Structure in markdown: three to five short themed sections with a bold heading each, then a section "Probabilities" with three to six one-line scenarios, each with a rough probability in words (likely, possible, unlikely) and the items that support it, then a section "What to watch" with three to five bullets.
- No investment recommendation, no price target, no buy or sell language. Not financial advice.
- Plain language, short sentences, at most 450 words in total.
- Do not introduce facts that are not in the items.

Output JSON exactly:
{"analysis_markdown": "..."}
