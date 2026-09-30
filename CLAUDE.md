# AI News Desk — House Rules. Read fully before any action.

These carry over from the TLVSC store repo because they are about how Rafi works,
not about which project it is.

1. ROUTE THE JOB BEFORE DOING IT. Before starting ANY task, scan who or what can
   actually do it — this cloud session, Claude Code local on Rafi's PC, another AI
   tool, a Drive feature, a script Rafi runs, a human. Present ALL viable paths in
   one message, up front, each with (a) what Rafi has to do, (b) the risk or safety
   issue if one exists, (c) which one I recommend. Rafi decides. THE MEASURE IS HIS
   EFFORT, NOT MINE. Never grind one path silently. If a blocker is structural — no
   file access, no network, wrong machine, missing model — say it in the FIRST
   reply, not the ninth.
2. Keep replies SHORT. Answer first, minimum detail. No walls of text. Extend only
   when Rafi explicitly asks.
3. NO DELETIONS. Superseded files are renamed `*_old`, never removed. In Drive, a
   superseded file gets `_superseded` added to its name and moves to that product's
   `supportive files/archive` folder (Rafi, 27 Sep 2026).
4. One fix at a time: show Rafi, get approval, then the next one.
5. EVIDENCE BEFORE DONE. Verify the artefact and report the actual numbers. A
   summary is not evidence. For video that means duration, streams, and frames —
   not "it worked".
6. Do NOT invent content. Anchor scripts, episode copy and names come from Rafi or
   from source material, never from me.
7. Claude cannot see rendered output. Ask for frames or screenshots before any
   visual judgement.
8. Every workflow instruction Rafi gives in ANY Claude chat gets written into this
   file so the next session already knows it.

## Project-specific

9. MEDIA STAYS OUT OF GIT. Clips, masters and logo masters live in Google Drive
   (`AI_News_Desk/`). This repo holds prompts, subtitle text and brand config.
   Scripts that belong to a product live in Drive, in that product's blueprint
   Permanent Assets; this repo holds only helper scripts for Claude's cloud
   sessions (Rafi, 27 Sep 2026). The Drive folder must stay replaceable without
   touching the repo. Temporary exception (Rafi, 29 Sep 2026): the daily report skill
   Temporary_independant_claude_only_15_per_category_fill_run and its scripts live in
   this repo, in `.claude/skills/`, for now. It stays on branch
   claude/eager-archimedes-ajnex3 and is used only in this Claude session; do not merge it
   to main, so ChatGPT and other tools never see a second source of truth.
10. BRANDING IS ADDED IN POST, NEVER GENERATED. MiniMax cannot reproduce a specific
    logo — it produces a different lookalike every render. Generate the set generic
    and overlay the real asset with ffmpeg. Set dressing and backgrounds are fine to
    generate; anything carrying the brand is not.
11. SUBTITLE CANVAS IS LOAD-BEARING. An `.srt` has no resolution, so libass assumes
    384x288 and renders text ~6x oversized in mid-frame. Always convert to `.ass`
    and pin `PlayResX: 1080` / `PlayResY: 1920`. Never burn straight from `.srt`.
12. THE SUBTITLE APPROVAL PAUSE IS NOT OPTIONAL. Whisper mangles proper nouns
    ("ChatGPT Atlas" came out "chat GPT Astras"). Always show Rafi the transcript
    and wait for his word before burning.
13. Scripts must be double-clickable and self-installing. Rafi's production machine
    is Windows 10 22H2. Assume nothing is installed; assume PATH is stale after any
    install; assume `python.exe` may be the Microsoft Store stub that only opens the
    Store. Check that a tool RUNS, not that it exists.
14. COUNTS ARE GUIDELINES, NOT GATES. Card count (~15), bulletin size, report size and
    category slots are working targets. Adjust them to the day's pool, e.g. 15 plus or
    minus 2 cards, and state the number. Never stop to ask Rafi about a count.
    The Full Report is score 5 and up plus every Fun Side story by default: it is sorted
    by category, so a reader can go to their own section, where a 5 may matter to them.
    Stay flexible on unusual days: if 5 and up passes about 150 stories, raise the
    cutoff; if it gives very few, lower it; state the cutoff and the count (Rafi,
    29 Sep 2026). The Bulletin cutoff flexes: pick the cutoff that lands it near
    30 to 50 stories (usually 6, 7 or 8 and up), then state the cutoff and the count
    (Rafi, 28 Sep 2026).
15. ANSWER IN ONE SENTENCE unless Rafi asks for more. No long answers.
16. DAILY RUN SETTINGS (Rafi, 30 Sep 2026). The scan covers the last 24 hours; 30 hours
    only when Rafi asks, for a late start. The Bulletin also carries the top 2 or 3 Fun
    Side stories. Cards: aim for 14 to 15 story cards; 7 to 8 of them go into Headlines,
    roughly half (a guideline, not a gate). Everything final is saved to its designated
    Drive place; what the Drive connection cannot upload goes to Rafi to upload himself.
    The environment allows about 100 source sites (the network allowlist); Google News is
    only the first of them, so read and scan those sources directly.
