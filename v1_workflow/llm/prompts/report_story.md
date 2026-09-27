# report_story (mid tier)

Task: write the Full Report story block for every event in PAYLOAD.events, in the Daily Global AI Intelligence Report format.

For each event
- headline: one line, factual, specific, present tense, at most 120 characters. Name the actor. No source name, no question marks.
- importance_reason: at most 25 words: who is affected and why this matters now. Fits after "Importance: LABEL —".
- summary: one or two complete sentences that give the new facts with their numbers, names and context. Do not repeat the headline. Do not speculate. Only facts in key_facts and summary.

Plain language: short words, no jargon, no hype. Numbers as written in the facts.

Output JSON exactly:
{"stories": [{"id": "...", "headline": "...", "importance_reason": "...", "summary": "..."}]}
