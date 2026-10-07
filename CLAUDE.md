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
   DAILY DELIVERY, the one standing yes (Rafi, 3 Oct 2026): the two daily skills save the day's
   products into AI_News_Desk / daily_data_generated / <date> (reports, cards, Headlines and their
   supportive files), creating missing subfolders, verifying every upload by size, never overwriting
   or deleting; what the connection cannot take goes to Rafi in chat. A text copy of each day's working
   files is kept in this repo under runs/<date> (no media) as the restart point when the cloud machine
   is wiped. A morning Routine that starts the chain by itself comes only after two clean manual days.
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

8a. WHEN TWO RULES CLASH, STOP AND ASK (Rafi, 7 Oct 2026, angry): whenever two rules, rulings or instructions touch or seem to clash, in a brief, a skill, a script or a Drive file, Claude does NOT choose.
   It stops, names both rules and where they are written, says in one line how they clash, offers a paste-ready fix, and waits for Rafi. A higher rule in this file wins only if Rafi has said so.

## Project-specific

9. MEDIA STAYS OUT OF GIT. Clips, masters and logo masters live in Google Drive
   (`AI_News_Desk/`). This repo holds prompts, subtitle text and brand config.
   Scripts that belong to a product live in Drive, in that product's blueprint
   Permanent Assets; this repo holds only helper scripts for Claude's cloud
   sessions (Rafi, 27 Sep 2026). The Drive folder must stay replaceable without
   touching the repo. Temporary exception (Rafi, 29 Sep 2026; renamed and split 3 Oct 2026):
   the daily run is two chained skills, Fill_categories_scan_part_A (scan, pool, Full Report,
   Bulletin; `.claude/skills/fill-categories-scan-part-a`) and Fill_category_scan_Part_B (cards
   and Headlines with Rafi's approval stop; `.claude/skills/fill-category-scan-part-b`). Part A
   starts part B by itself. Both live ONLY in this repo on branch claude/eager-archimedes-ajnex3:
   never on Drive and never merged to main, so ChatGPT and other tools never see them (a second
   source of truth), and they run only in a Claude session connected to this repo.
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
14. COUNTS ARE GUIDELINES, NOT GATES. Card count (the CARD FILTER target), bulletin size, report size and
    category slots are working targets. Adjust them to the day's pool and state the number.
    Never stop to ask Rafi about a count.
    The Full Report is score 5 and up plus the Fun Side by default: it is sorted
    by category, so a reader can go to their own section, where a 5 may matter to them.
    Stay flexible on unusual days: if 5 and up passes about 150 stories, raise the
    cutoff; if it gives very few, lower it; state the cutoff and the count (Rafi,
    29 Sep 2026). NEWER RULING (Rafi, 7 Oct 2026, replaces the 150 figure): aim the Full Report at 100 to 120 stories, because 177 is too long to read; pick
    the cutoff (5 or 6, or whatever lands closest to that range) and state the cutoff and the count. On 7 Oct 2026 cutoff 6 gave 93 and cutoff 5 gave 177. If the cutoff leaves fewer than 100, fill up to about 110 with the best stories of the next lower score (build_products.py --report-fill-to 110): Rafi said "keep it between 100 and 120" and 93 was a misreading (7 Oct 2026). The Bulletin cutoff flexes: pick the cutoff that lands it near
    30 to 50 stories (usually 6, 7 or 8 and up), then state the cutoff and the count
    (Rafi, 28 Sep 2026). Health and Society and education get a lower bulletin cutoff of 6, so those two sections are never empty (Rafi, 7 Oct 2026;
    build_products.py --bulletin-min-cat HEA=6,SOC=6).
15. ANSWER IN ONE SENTENCE unless Rafi asks for more. No long answers.
16. DAILY RUN SETTINGS (Rafi, 30 Sep 2026). The scan covers the last 24 hours; 30 hours
    only when Rafi asks, for a late start. Fun Side: 5 to 10 stories in the Full Report,
    leaving out repeats; the top 3 also go in the Bulletin. Cards: the number of story cards comes from the CARD FILTER below; 7 of them go into Headlines,
    roughly half (a guideline, not a gate). Headlines news part is about 90 seconds (Rafi, 30 Sep
    2026): 7 stories of about 8 to 9 seconds, Fun about 8, teaser about 8, The Bigger Picture about
    10; the stored opening and ending come on top. Every clip time is rounded UP to the next half
    second (8.4 becomes 8.5, 8.6 becomes 9). Company limits (Rafi, 30 Sep 2026) are
    in the CARD FILTER below; past a limit, the next biggest story in the field goes in. Everything final goes to its designated
    Drive place by the skills' delivery step (the standing yes of 3 Oct 2026 in rule 0); what the Drive
    connection cannot upload goes to Rafi in chat.
    SOURCES (Rafi, 2 Oct 2026): Google News is first and main. Then read the 55 sources of the
    Drive sheet "five per category source list" (reference only), directly, for the same
    window, and give their stories to the curators. The network allowlist holds all of them.
    PER CATEGORY (Rafi, 2 Oct 2026): 15 stories is enough; where there are plenty of good
    ones, take up to 20; never pad with weak stories. The Fun Side stays at 10.
    3 OCT 2026 RUN (Rafi, 3 Oct 2026, one run only): 16 curator agents, one per LV2 category,
    10 new unique items each, pool 160. Rafi's ruling after it (3 Oct 2026): back to 15 to 20
    per category as in the PER CATEGORY line above. Kept from the 3 Oct run: repeats are checked
    against the last 4 days of pools, and the 3 flagged backups replace items dropped as duplicates.
    READER LEVEL (Rafi, 3 and 5 Oct 2026): the reader levels and the writing shape live ONLY in the Drive file
    Article_phrasing_instructions_AIND_V1 (Prompt Library / prompts); this repo never restates them. Every writer re-reads its
    Sections 1, 1A, 1B and its product section BEFORE EACH ITEM, and every item answers who, what and why. The writer and editor briefs follow that file.
    CLIP SECONDS (Rafi, 3 and 5 Oct 2026): count syllables (4.4 a second), round UP to the next half second, over the
    Drive Headlines Master rule 1a (two decimals); every item aims at 8 seconds and never passes 10 (44 syllables): Rafi, 5 Oct
    2026, "max 10 sec item, preferably 8"; the Drive Section B item 1 says 12 and is updated to 10 the same day.
    CREDIT (Rafi, 3 Oct 2026): the source printed is always the outlet that reported the story, never
    a copy site that carries its text; if the article we read credits another outlet, the credit goes
    to that outlet. Headline only: take the story from another outlet that has it and credit it, or
    build our own entry from several outlets and label the source AI News Desk, naming them inside.
    Follow the chain to the first reporter; when unclear, write "X reports, citing Y". A desk-built
    news entry keeps a news status label. The Bigger Picture card, the one AI News Desk item of
    every day, carries the short label AIND and, on the source strip, AI News Desk (Rafi, 3 Oct 2026; the Drive Cards
    rules 1.3 and 3.5 and the phrasing file 3.2 still say DESK VIEW, a line for Rafi to change there).
    Always inside the law: our own words, short quotes only, always a credit.
    WRITE ONLY WHAT CAN PRINT (Rafi, 4 Oct 2026, to save tokens): the pool keeps every story as headline
    and link; an article is read and written only for stories at curator score 5 and up (the report
    cutoff; writers never raise a score) and for the Fun Side. The rest stays pool only in daily-pool.md.
    REPLY STORIES (Rafi, 4 Oct 2026): when a story is a reply, reaction or comment to an earlier story, every product says it
    plainly (who answers whom) and names and explains the earlier story it answers (who reported what, and
    when; "yesterday we carried a New York Times report: ..."), so a reader who missed it understands the reply.
    A reply that names no one is "widely read as a reply". The report check and the wording check enforce it.
    HEADLINES RULES RECHECK (Rafi, 4 Oct 2026): before Rafi sees the Headlines lines, they are checked against the
    Drive Headlines Master rules, by a script (check_headlines_rules.py) and a rules agent (Part B step 3b). Nothing
    goes to him with a rules FAIL. Introductions rotate: never the previous day's wording (Drive rule G2).
    MODEL POLICY (Rafi, 6 Oct 2026, replaces the MODEL TRIAL): the main session and the bulk agents (16 curators, fillers,
    16 writers, setup, Drive delivery) run on Sonnet (Agent tool model "sonnet"). Hard tasks run on Opus 5.5 at extra high
    effort (Agent tool model "opus"): the editors, the stranger check, the
    rules agent and the rewrite agent. NEVER Haiku (Rafi, 7 Oct 2026: not for setup, Drive, writers or anything else).
    STORY CHOICE FOR CARDS AND HEADLINES (Rafi, 7 Oct 2026, replaces the Fable-only-on-request line: "this is our adverts, if it
    sucks nobody follows and the business falls"): Fable chooses the stories of the cards and the Headlines and writes their wording, under the Drive
    Cards Master (Sections 2 and 3) and Headlines Master (Sections A and B), the phrasing file and this file. A script gates the choice (ids exist, read in full, no
    repeat of the last 7 days, no update unless Rafi named it, company and category limits, counts, order) and refuses to go on until it passes. Rafi approves the list before any wording is
    written. Opus does the checks (stranger, rules, final audit per product, a checklist of every rule with PASS or FAIL and evidence), because a different model must check the author.
    Fable is used elsewhere only when Rafi names the item. Report the helper token use per stage next to the 4 and 5 Oct runs.
    The temporary scan keeps running daily until V1 is ready (Rafi, 4 Oct 2026).
    HEADLINES SHAPE (Rafi, 5 Oct 2026): set in the Headlines section of the phrasing file; check_wording.py
    reads the sentence limit from that file and fails a line that breaks the shape. A fix is shorter and simpler, never longer.
    WHO WHAT WHY FIRST (Rafi, 5 Oct 2026; the stranger check answers who, what and why from the line alone, and a line fails when it cannot): the Headlines writer fills who, what and why_for_people for every clip before the line
    and writes the line from them; the script fails a clip without them or whose why is not spoken. The main session never rewrites a
    line by hand: failing lines go to a Fable rewrite agent (Part B step 3a); Rafi's own wording is locked. The gate refuses the JSON
    and the review list unless the checks passed on the current lines.
    HEADLINES ORDER (Rafi, 5 Oct 2026, one source of truth): the order and choice of the seven clips are set ONLY by the Drive file
    Headlines_Master_Rules_Structure.txt (General order of categories, criticals lead, and Section A item 3). This repo never restates or
    reinterprets it; card_candidates.py applies it and names the file. Claude broke this twice on 5 Oct 2026 by writing its own reading here.
    HEADLINES INTROS AND FLOW (Rafi, 6 Oct 2026; it belongs in the Drive Headlines Master B2a, which Rafi or ChatGPT still have to update
    there; until then this is the one place): the Headlines are read like a presenter reads the news, not like a list. Each clip opens with
    an intro that names its own topic, in a natural order ("We begin with an update", "In finance", "Also in finance", "In security",
    "In robotics", then "In tech", "In the lab", "And finally, something lighter", "Also in the full report", "And for the bigger
    picture"), never the same intro twice and never a label with no link to the topic ("On the road" for a robotics clip made Rafi
    furious). The intros Rafi dictates win over rule G2 (rotation). When Rafi asks only for the intros, or for one story to change, ONLY
    that changes: the bodies and every other clip stay word for word, and the cards stay as they are (he overrode rule A3 on 6 Oct 2026).
    Headlines stories are chosen and worded for what matters to people all over the world: prefer a story that shows AI development
    affecting people over one that is mainly war or politics (6 Oct 2026: LG and Nvidia's AI car platform replaced the Ukraine gun
    turrets). The fun clip must be funny at once for anyone (6 Oct 2026: Alexa stuck saying "la la la" replaced a comedian's sketch).
    Every clip of the JSON is generated: bypass only the stored opening, the stored ending and the spare slot, never a clip Rafi did not
    ask to leave out. TEST (6 Oct 2026): clips 1, 5 and 8 show a short realistic video on the holographic screen instead of the glowing
    symbol; the Drive Headlines Master (15 Sep, item 3, and G3) keeps text-free symbols until Rafi says the test worked.
    NO OLD NEWS (Rafi, 5 Oct 2026): the last stage of removing duplicates, before the Bigger Picture and the final Full Report, compares
    every report entry with the Full Reports of the 14 previous days in Drive (read only; Part A step 9b, check_dup14.py). Cards and
    Headlines take only what survives it. A meaningful update of an earlier story can be a card (CARD FILTER below).
    CARD FILTER (Rafi, 6 Oct 2026; the ONE place for card numbers and company limits; replaces the fixed slots of the Drive Cards Master
    Section 2 item 4, which Rafi or ChatGPT still have to update there; scripts and skills point here and hold no numbers): the category
    order stays (read from the Drive Cards Master Section 2 item 4). Critical stories (score 10) come first, each spending its category's
    slot. Every category keeps its best story if it scores base_min or more; fun is always last. The remaining slots, up to target story
    cards, go to the highest scored stories left, if they score extra_min or more, at most max_per_category per category (market
    market_max, the money cap). A meaningful update of an earlier story can be a card (a decision, a confirmation, a first result or a
    new party) and the card names the earlier story; a repeat of the last three decks without a meaningful update is a failure. Only
    stories read in full; a robotics card shows a machine doing something. Past a limit, the next biggest story in the field goes in.
    Headlines are chosen by the Drive Headlines Master (HEADLINES ORDER above), which says the strongest card stories by score.
    CARDS FROM THE BULLETIN (Rafi, 7 Oct 2026): story cards are chosen only from the stories of the Bulletin, not from the whole Full Report, and the target
    is 14 story cards (Headlines stay 7); card_candidates.py reads products/bulletin_pdf.json.
    NO UPDATE CARDS (Rafi, 7 Oct 2026, angry: Pentagon and Anthropic, DeepSeek, OpenAI and the Korean bank hack came back as cards on 3 days in a row): an update of
    an earlier story is a card ONLY when a major story changed meaningfully AND Rafi has named it; the default is none (card_candidates.py reads cards_work/update_allowed.json,
    empty by default). Before Rafi sees a deck, every card is compared with the cards and Headlines of the last 3 days by name and topic, and the table is shown.
    NO REPEATS IN 7 DAYS (Rafi, 7 Oct 2026): no story that was a card or a Headlines clip in the last 7 days comes back, as a repeat or as an update (see NO UPDATE CARDS).
    THE REPO IS THE SOURCE OF TRUTH FOR NOW; DRIVE IS CHATGPT'S (Rafi, 7 Oct 2026, replaces "clash to fix on Drive"): where this file differs from a Drive rules file there is no clash; this file wins.
    Claude keeps docs/DRIVE_DIFFS_FOR_CHATGPT.md (every difference) and docs/V1_TASKS.md (every lesson), and when the scan is fully operational both go to ChatGPT. Aim: 14 story cards and 7 Headlines
    story clips, not counting Fun, teaser, Bigger Picture, like and follow, cover and closing.
    BIGGER PICTURE WEIGHT (Rafi, 7 Oct 2026): the Bigger Picture must be a meaningful analysis with a meaningful thing to watch, in the Full Report, the Bulletin, the card and the Headlines clip, and each
    must say it is not financial advice. Fable writes it (all three lengths) and puts real effort into seeing what comes next: scheduled events in the coming days and weeks (earnings, votes, court dates,
    launches, data releases), each with its date and source, and says plainly when a date is not confirmed. In the Full Report and the Bulletin it stays at the END for now (Rafi, 7 Oct 2026). The Headlines clip
    screen flashes a warning sign with the words "This is not financial advice" (Rafi, 7 Oct 2026; newer than the text-free screen rule, which stays for every other clip), and the post caption carries
    the same line.
    PEOPLE WITH THEIR POSITION (Rafi, 7 Oct 2026): every named person is given their position and organisation in the same sentence, so their words carry weight, for example "Ray Dalio, founder of
    Bridgewater, one of the world's biggest hedge funds" or "Jamie Dimon, chief executive of JPMorgan Chase, the biggest US bank". Never a vague label like "big investor" or "billionaire investor". Applies to every product.
    HEADLINES START WITH POLITICS (Rafi, 7 Oct 2026): the Headlines reel follows the deck order, so when the deck has a Politics card its clip is clip 1; Fable may choose which other cards
    become clips, but it never skips Politics or reorders the deck. "Prefer AI affecting people over war or politics" (6 Oct) applies only when choosing among the other categories.
    CARD_FILTER: base_min=5 extra_min=7 target=14 max_per_category=2 market_max=3 company_cards=3 company_clips=2
    BEFORE EVERY STAGE (Rafi, 2 Oct 2026): read the files that govern it (this file, the skill
    for that stage, its rules and structure files), run the skill's script as the truth, and
    fix or help the script only afterwards.
    HEADLINES GENERATION (Rafi, 2 Oct 2026, to be tested on the 2 Oct clips; if it works it moves to
    the Drive prompt blueprint): 8 sampler steps, not 6 (8 fixed the stuttering voice); the voice
    reference is the 4 second sample AIND_anchor_voice_sample_4s.wav, not the 8 second one; the
    prompt never rushes the presenter: "at a natural, unhurried pace, in an authoritative and
    informative news presenter tone, clear and easy to understand, never rushed". The fill
    writes these into the JSON (visible and named values) and says so in its CONFIG line.
    OPENING AND ENDING OPTIONS (Rafi, 2 Oct 2026): when Rafi asks, slots 1 and 13 are generated
    as new options (the opening with the 28 Sep 2026 prompt wording, the ending with the approved
    15 Sep 2026 wording) and compared with the stored clips; the stored clips stay the approved
    ones until Rafi picks. Stored so far: openings 2026-09-09, 2026-09-11, 2026-09-23 (two clips);
    endings 2026-09-09 and 2026-09-15 (approved), in Headlines Master Permanent Assets.
    APPROVED OPENING AND ENDING (Rafi, 4 Oct 2026): the daily Headlines use the stored option 4 clips of 3 Oct,
    Headlines Master Permanent Assets / openings / 2026-10-03 / AIND_opening_option4_2026-10-03_VL1_1088.mp4 and
    endings / 2026-10-03 / AIND_ending_option4_2026-10-03_VL1_1088.mp4. The JSON bypasses slots 1 and 13; the stitch puts
    these two clips first and last. New openings or endings are generated only when Rafi asks.
    QA GAPS (Rafi, 4 Oct 2026): the four missing checks (card choice, card rules, report and bulletin rules, the Bigger
    Picture) are built on 5 Oct, scripts first.
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
18. FRESH CHAT BEFORE A RUN (Rafi, 4 Oct 2026). Before starting a daily run, if the chat already
    carries a delivered run or a skill build, write the handoff and ask Rafi to open a new chat
    first. A compacted chat continues only with Rafi's explicit yes (he gave it on 4 Oct 2026 for
    the 4 Oct Part A run).
19. THE START LINE (Rafi, 5 Oct 2026). A daily run starts with one fixed line, "Run Part A for <date>", in a cloud session
    on branch claude/eager-archimedes-ajnex3 (docs/START_LINE.md). Never add extra items, fixes or lessons to a start
    message; they live in this file, the skills and the repo.
