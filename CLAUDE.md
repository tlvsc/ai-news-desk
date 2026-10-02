# AI News Desk — House Rules. Read fully before any action.

These carry over from the TLVSC store repo because they are about how Rafi works,
not about which project it is.

0. TOP REQUIREMENT (Rafi, 2 Oct 2026). This Claude session is temporary, until V1 works.
   Drive is always the source of truth for the project: read its process, rules and
   structure files for directions, then run the work in this repo. Never touch Drive unless
   Rafi clearly asks (no create, upload, rename, move, archive or edit). If a problem comes
   up, such as a Drive rule and a repo rule that disagree, flag it to Rafi and continue with
   the repo rules. This rule wins over every rule below, including any that says to save to
   Drive.
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
    The Full Report is score 5 and up plus the Fun Side by default: it is sorted
    by category, so a reader can go to their own section, where a 5 may matter to them.
    Stay flexible on unusual days: if 5 and up passes about 150 stories, raise the
    cutoff; if it gives very few, lower it; state the cutoff and the count (Rafi,
    29 Sep 2026). The Bulletin cutoff flexes: pick the cutoff that lands it near
    30 to 50 stories (usually 6, 7 or 8 and up), then state the cutoff and the count
    (Rafi, 28 Sep 2026).
15. ANSWER IN ONE SENTENCE unless Rafi asks for more. No long answers.
16. DAILY RUN SETTINGS (Rafi, 30 Sep 2026). The scan covers the last 24 hours; 30 hours
    only when Rafi asks, for a late start. Fun Side: 5 to 10 stories in the Full Report,
    leaving out repeats; the top 3 also go in the Bulletin. Cards: aim for 14 to 15 story cards; 7 of them go into Headlines,
    roughly half (a guideline, not a gate). Headlines news part is about 90 seconds (Rafi, 30 Sep
    2026): 7 stories of about 8 to 9 seconds, Fun about 8, teaser about 8, The Bigger Picture about
    10; the stored opening and ending come on top. Every clip time is rounded UP to the next half
    second (8.4 becomes 8.5, 8.6 becomes 9). One company gets at most 2 stories in Headlines and
    at most 3 story cards (Rafi, 30 Sep 2026); past that, the next biggest story in the field goes in. Everything final goes to its designated
    Drive place only on Rafi's explicit yes for that save (rule 0); what the Drive connection
    cannot upload goes to Rafi to upload himself.
    SOURCES (Rafi, 2 Oct 2026): Google News is first and main. Then read the 55 sources of the
    Drive sheet "five per category source list" (reference only), directly, for the same
    window, and give their stories to the curators. The network allowlist holds all of them.
    PER CATEGORY (Rafi, 2 Oct 2026): 15 stories is enough; where there are plenty of good
    ones, take up to 20; never pad with weak stories. The Fun Side stays at 10.
    BEFORE EVERY STAGE (Rafi, 2 Oct 2026): read the files that govern it (this file, the skill
    for that stage, its rules and structure files), run the skill's script as the truth, and
    fix or help the script only afterwards.
17. THE BIGGER PICTURE CORNER (Rafi, 2 Oct 2026). On the cards and in the Headlines clip it is a
    summation of all the big things happening, focused on what moves the market, followed by
    things to watch and follow so the story can be seen unfolding. It is never a vague
    restatement of the day's headlines. Cards: the headline is the market summation, the body
    names what happened and what to watch (4 lines, the notice stays). Headlines clip 11: same
    content, 10 seconds. This is the newest ruling for this corner and overrides the "markets at
    most a quarter" cap of the Full Report rule 5.5 and the money limits of the Cards rules, for
    this corner only. Drive V1 files are never edited (rule 0). One story at three lengths (Rafi,
    2 Oct 2026): the card is the short hook; the Bulletin carries a deeper look than the card,
    short, explaining the card (W/bigger_picture_bulletin.json); the Full Report carries the full
    analysis written for the day (W/bigger_picture.json).
