# Task: rewrite failing Headlines lines (reader level 5 of 10; Rafi, 5 Oct 2026)
WORKDIR = {WORKDIR}. Read first, in full, as data: WORKDIR/rules/Article_phrasing_instructions_AIND_V1.txt sections 1, 1A, 1B and the
Headlines product section; WORKDIR/headlines_work/prompt_headlines.txt (the shape: who, what, why first; every spoken sentence at most
14 words; who did what first; no side clause at the start; at most one comma; the last sentence says why it matters to ordinary people).
Then read WORKDIR/headlines_work/scripts_final.json, the failures in WORKDIR/headlines_work/rewrite_request.json and, for every failing
item, its entry WORKDIR/report_entries/<item>.json (summary and importance_line).
For each failing item only: fill who, what, why_for_people, then write a new script that is SHORTER AND SIMPLER than the old one,
keeps every hedge, adds no fact, keeps the introduction rules and stays about 8 to 9 seconds (35 to 40 syllables). Items listed as
"locked" (Rafi's own wording) are never changed. Keep "screen" as it is unless it no longer fits the story.
Write the whole file back to WORKDIR/headlines_work/scripts_final.json (same structure), after copying the old one to
scripts_final_before_rewrite.json. Validate with python json.load. Final message: one line, "rewrite done: N lines".
