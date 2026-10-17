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
   products into AI_News_Desk / daily_data_generated / <date>, into the product folders set ONLY by the Drive file
   "AI News Desk — STORAGE & FILE ROUTING STANDARD" (00 — PROJECT OS); the folder names live only in delivery_manifest.py, which reads that
   Drive file every run and stops when the two differ (Rafi, 11 Oct 2026, option c; the wording is Claude's), creating missing subfolders, verifying every upload by size, never overwriting
   or deleting; what the connection cannot take goes to Rafi in chat. A text copy of each day's working
   files is kept in this repo under runs/<date> (no media) as the restart point when the cloud machine
   is wiped. A morning Routine that starts the chain by itself comes only after two clean manual days.
   WHO MADE IT (Rafi, 11 Oct 2026, his words: two or three scans save into the same folders, so "each file name says exactly who or which scan it is";
   "all products should, no need to do historical items, start from today on"): every file this scan saves to Drive ends with _Claude-V1, cards included
   (the label lives in delivery_manifest.py; the wording of this line is Claude's). Files already on Drive are not renamed.
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

8b. NEVER AGAIN (Rafi, 7 Oct 2026, the worst day of the project; details in docs/V1_TASKS.md lessons 85 to 97). Before every reply and every build, Claude checks these seven:
   1. A question is not a decision: answer the question first; a recommended option is never run until Rafi picks it.
   2. Two rules that touch: stop and ask (8a), never choose, never put one rule's opposite into a model brief.
   3. Check the work against every rule and against the last 7 days BEFORE showing it; show the comparison, not a promise.
   4. A count or an order Rafi gives wins over any cutoff or script default; say how it was met.
   5. Replies: one or two short sentences, simple English, no shorthand or jargon, unless he asks for more.
   6. Every named person has position and organisation; every name is introduced, never avoided.
   7. No check loops: one check round and one rewrite round, then show Rafi what is left. Use the cheapest path that meets the rules.

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
   Exception (Rafi, 12 Oct 2026, his words: "backup stays in repo for now"; "not in drive . repo and download folder"; "drive causes confusions"): backups of Claude's local video scripts are kept in this repo under backup/<name>_<date>/ (first: backup/claude_part_b_2026-10-11, the scripts of the approved 11 Oct video) and in Rafi's PC Downloads folder for the local chat, never on Drive; a backup is not a rulebook, the lessons stay in docs/V1_TASKS.md. (Mine, not yours: the wording around his quotes.)
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
    BULLETIN SECTIONS NEVER EMPTY (Rafi, 9 Oct 2026, after a Bulletin with no Politics story, "7 billion people, 350 countries and no political AI story"): every category of the Bulletin takes its top stories, 7 and up.
    If a category has none, the search is expanded first, to Asia, Europe and the Middle East (the big outlets and regional searches), and the new stories go through the same reading, writing and checks.
    If still none fit, the category gets exactly 2 stories from the Full Report, at score 6 and up (5 only if there is no 6): Rafi, 9 Oct 2026, "I asked only 2 items in case we do not have 7 and up" (the first version said "at least 2" and the Bulletin got 10 Politics stories). This holds for every category; the HEA and SOC line above stays as it is until Rafi says otherwise.
    An empty category is fixed BEFORE the PDFs are built, never reported after delivery.
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
    Drive Headlines Master rule 1a (two decimals). The length is rule 22: aim 8 seconds for every item, 10 acceptable when an item is long and cannot fit, 12 the hard limit (Rafi, 12 Oct 2026; the 5 Oct "max 10 sec" is replaced).
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
    MODEL TEST (Rafi, 15 Oct 2026): before changing any model or effort, read docs/model_test_2026-10-14/README.md (72 blind
    runs of 14 Oct 2026; nothing changed yet; the options and the decisions log are in its 3_CONCLUSIONS.md).
    STORY CHOICE FOR CARDS AND HEADLINES (Rafi, 7 Oct 2026, replaces the Fable-only-on-request line: "this is our adverts, if it
    sucks nobody follows and the business falls"): Fable chooses the stories of the cards and the Headlines and writes their wording, under the Drive
    Cards Master (Sections 2 and 3) and Headlines Master (Sections A and B), the phrasing file and this file. A script gates the choice (ids exist, read in full, no
    repeat of the last 7 days, no update unless Rafi named it, company and category limits, counts, order) and refuses to go on until it passes. Rafi approves the list before any wording is
    written. Opus does the checks (stranger, rules, final audit per product, a checklist of every rule with PASS or FAIL and evidence), because a different model must check the author.
    Fable is used elsewhere only when Rafi names the item. Report the helper token use per stage next to the 4 and 5 Oct runs.
    BIGGER PICTURE MODEL (Rafi, 9 Oct 2026, replaces the 8 Oct line "Fable at effort high"): one agent writes all three lengths, on Fable at effort max or Opus at max, whichever is smarter; Fable max is the choice. The main session never writes it.
    HAIKU TODAY ONLY (Rafi, 8 Oct 2026): on 8 Oct 2026 every helper job that says Sonnet runs on Haiku; Opus and Fable jobs do not change. The NEVER Haiku line above stands for every other day.
    SCRIPTS STAY AS THEY ARE DURING A RUN (Rafi, 8 Oct 2026): fixes go into the skill text and its list files; a script changes only between runs, when Rafi says so.
    Exception (Rafi's yes, 11 Oct 2026; mine, not yours: the wording): when Rafi gives a new rule during a run, the scripts that enforce the old rule are updated the same day, after he says yes to the exact edit list.
    BIG OUTLETS (Rafi, 8 Oct 2026; extends the 55 sources line of 2 Oct): the scan also reads investing.com, MarketWatch, Yahoo Finance, CNA, BBC, Euronews, DW, taz and Sixth Tone. France 24 is not used.
    The temporary scan keeps running daily until V1 is ready (Rafi, 4 Oct 2026).
    HEADLINES SHAPE: rule 22 (one sentence: who did what and why) and the model lines file; where the phrasing file allows a second sentence, rule 22 wins (Rafi, 11 Oct 2026). A fix is shorter and simpler, never longer (Rafi, 5 Oct 2026).
    WHO WHAT WHY FIRST (Rafi, 5 Oct 2026): the Headlines writer fills who, what and why for every clip before the line and writes the line from them
    (the why as rule 22 says; the old "why is not spoken" test is removed, Rafi 11 Oct 2026). The main session never rewrites a
    line by hand: failing lines go back to the same writer (Part B step 3; rule 25 replaces the Fable rewrite agent, Rafi 12 Oct 2026); Rafi's own wording is locked. The gate refuses the JSON
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
    turrets). The fun clip follows rule 24 (FUN STORIES; Rafi, 12 Oct 2026, removed "funny at once").
    Every clip of the JSON is generated: bypass only the stored opening, the stored ending and the spare slot, never a clip Rafi did not
    ask to leave out. TEST (6 Oct 2026): clips 1, 5 and 8 show a short realistic video on the holographic screen instead of the glowing
    symbol; the Drive Headlines Master (15 Sep, item 3, and G3) keeps text-free symbols until Rafi says the test worked.
    REAL TV SCREENS (Rafi, 8 Oct 2026; replaces the TEST line above and the text-free symbol for every story, fun and teaser clip): each holographic screen shows a short
    realistic TV-news style scene of that story's subject, like a real TV (for example a humanoid robot factory for a robotics story); no readable words, numbers, logos or
    real named faces; the Bigger Picture clip keeps its warning sign. PHOTOREALISTIC (Rafi, 10 Oct 2026, his words): "the holographic screen should be real photo realistic; give thought to how to portray the article well: what would a big news channel put as image or video for this item". FUN CLIP (Rafi, 8 Oct 2026): facts only from the source (the "explains the joke so it lands at once, set-up then punchline" part is removed for now, Rafi 12 Oct 2026; see rule 24 FUN STORIES).
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
    FAMOUS PEOPLE RULE (Rafi, 9 Oct 2026, after the Musk and India Starlink row, carried by about 100 outlets, was missed): a story whose main actor is a top AI or tech leader or a head of government (for example Musk, Altman, Zuckerberg, Nadella, Pichai, Huang, Amodei, Trump, Modi, Xi) and that is big, meaning many outlets carry it, goes into the pool as AI adjacent even when AI is not its main subject, scored by global consequence; the curators of Politics and Industry Voices look for it every run. The big story sweep is decided by the VIRAL RULE below (Rafi, 10 Oct 2026); the watch list file and the AI adjacent scope question are NOT decided yet.
    VIRAL RULE (Rafi, 10 Oct 2026): if a story is carried by 20 or more distinct outlets in the window, its score is at least 7, so it goes into the Bulletin. It keeps the category the curators gave it. A script counts the outlets. The writers cannot lower it below 7; they still check facts and dates. A story that already ran earlier below 7 may run once more at 7 or more; NO OLD NEWS, NO UPDATE CARDS and NO REPEATS IN 7 DAYS do not block that one run.
    POOL PDF EVERY DAY (Rafi, 9 Oct 2026): the pool is also delivered as a PDF, AIND_Pool_<D-M-YY>.pdf: every pool story, category by category, numbered, highest score first, one line each: "score 7: headline / source" (Part A step 11, make_pool_pdf.py). It goes to Rafi with the Full Report and the Bulletin.
    ONE TOPIC, ONE CARD (Rafi, 9 Oct 2026, after Trump's "super intelligence" post and Japan's prime minister's answer to it got two cards): a reply, reaction or follow-up to a story of the same day goes on the SAME card and in the same Headlines clip, never as a second card or clip; the picker treats stories with the same topic as one, and before Rafi sees a deck every card pair is checked for a shared topic.
    CARD_FILTER: base_min=5 extra_min=7 target=14 max_per_category=2 market_max=3 company_cards=3 company_clips=2
    ROBOTICS (Rafi, 8 Oct 2026; overrides Cards Master 2.6 and 2.9 for robotics, and the Bulletin cut-off does not stop these two stories): the Bulletin must hold at least 3 and up to 5 robotics stories;
    Headlines must carry 1 robotics clip; the cards carry 2 robotics cards, one of them a humanoid robot story. These counts are guidelines, not iron rules: one extra robotics story is allowed where needed. Robotics means anything about humanoid robots
    and any other robotics: robot inventions, developments and anything super important, which goes into the cards and the Headlines. A funding round for a humanoid robot company counts
    (the Nvidia and Figure story is the model).
    ROBOT WAR LIMIT (Rafi, 10 Oct 2026, his words: "limit robot war stories to 2 max in the Bulletin, 3 in the Full Report; the pool is free, if it is unique stories"): robot war stories are at most 2 in the Bulletin and 3 in the Full Report; the pool has no limit as long as the stories are unique.
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
20. HOW TO ASK AND SHOW, AND WHAT A RULE IS (Rafi, 10 Oct 2026, his words, recorded because rule 8 asks for every instruction; docs/V1_TASKS.md lessons 175, 190, 194):
    ASK ONE AT A TIME: "ask them one by one", "ask it simply, one sentence, simple and easy to understand". Never ask what a rule of this file already decides: decide it and say which rule.
    SEND THE THING ITSELF: when he asks for the card list, send the list, short, in deck order, with nothing else; when he asks for a file, send that file on its own.
    RULES ONLY IN HIS WORDS: "who approved you to add rules without my consent?" Claude writes into this file only what he said, in his words; any line that is Claude's own idea is marked "mine, not yours" and waits for his yes.
    HIS COMPLAINT FIRST: when he complains about a product, Claude finds the exact fault in what he sent and says it back in one line before proposing any work ("the stories are fine, it was just the order that was bad").
    ORDER NEVER CHANGES: the approved category order is read from common.py (POOL_ORDER, ORDER) by every product, and check_order.py (Part A step 12) fails a product that breaks it.
    (The words around his quotes in rule 20 are Claude's wording; Rafi can strike any line.)
21. ONE LESSONS FILE; A HANDOFF IS NOT A SOURCE OF TRUTH (Rafi, 11 Oct 2026, his words: "all these files should be submerged to the things we learned into the repo"; "do not create another source of truth"; "handoff should be saved but not served as source of truth, just a file for continue our work; we need to make sure this is enforced").
    The things we learned file is docs/V1_TASKS.md in this repo. Lessons found anywhere else (a Drive lessons file, a handoff, another chat) are merged into it, and the other file is then superseded to the archive (rule 3). (Mine, not yours: the wording of this line.)
    A handoff is saved only to continue the work. A new session takes its rules from this file and its lessons from docs/V1_TASKS.md, never from a handoff; a lesson written in a handoff is first written into docs/V1_TASKS.md. (Mine, not yours: the wording of this line.)
    "AI News Desk — EXPERIMENTS & TECHNICAL LEARNINGS" (Drive, 00 — PROJECT OS) is a different file, about ComfyUI work and experiments: Claude never touches it (Rafi, 11 Oct 2026).
22. HEADLINES STRUCTURE, KEEP IT (Rafi, 11 Oct 2026, his words, after seeing the rewritten 11 Oct Headlines: "Finally everything is perfect! You must retain the structure from now on!").
    The structure, his words: "who made what? And why it matters, all in one sentence." His model line: "NVIDIA is reportedly in talks of buying AI firm Reflection, which could strengthen its position in open weights models. That's it."
    "Either no need for the end part or if so it must be impactful." "If the item makes an assumption it can say that: presumably..., might help..., can promote... and 1000 more options to say the why." "Why is company why isnt allowed?" "It's open weight model, not open AI model."
    Clip length, his words: "stay under 12 seconds maximum, but we aim for 10 ... we stick to 8 to 10 seconds. We can go up to 12 seconds max."
    Clip length, his newer words (12 Oct 2026, these win): "shouldnt and cant are not the same limits! we aim for 8 seconed, 10 acceptable in case item is long and cant be fit in, 12 is hard limit ... so we are flexible with limits. but always aim for 8 second item."
    (Mine, not yours: the wording around his quotes, and this reading: rule 22 replaces the 10 second maximum of CLIP SECONDS in rule 16.)
    Every Headlines writer and checker reads .claude/skills/fill-category-scan-part-b/assets/headlines_model_lines.md (12 model lines from 26 Sep to 1 Oct and 11 Oct, and the rejected ones): Rafi's yes, 11 Oct 2026.
    The stranger check follows rule 22: a company reason or a careful guess is a why, and a line with no why passes when it is clear without one; the 5 Oct "why it matters to me or people like me" test is replaced (Rafi's yes to fixing the checker, 11 Oct 2026). (Mine, not yours: the wording of these two lines.)
23. FUN CLIP FOR 12 OCT 2026 (Rafi, 11 Oct 2026, his words: "keep it for tomorrow"): the Apate story (AI bots that play the perfect victim and keep phone scammers talking for over two hours; WIRED, in the 11 Oct Full Report as C12-10) is the fun clip of 12 Oct.
    (Mine, not yours: the wording of this line, and this reading: NO OLD NEWS and the duplicate checks do not block this one story on 12 Oct, because he named it.)
24. RAFI'S INSTRUCTIONS OF 11 AND 12 OCT 2026, HIS WORDS (rule 8; the wording around his quotes is Claude's):
    CARDS IN GROUPS OF 10: "groups of 10 is easier for me to download" (12 Oct 2026). Cards are sent in groups of 10 files per message, in deck order (Part B step 8).
    HEADLINES ITEMS MUST BE IN THE REPORTS: "items in headlines must appear in the pool, and bulletin and report (not necessarily in the cards)" (12 Oct 2026). pick_gate.py G4b checks it; the one exception is a fun clip Rafi names himself (rule 23).
    FUN STORIES: "they can be either funny stories, or just fun to hear/see/experience for humans, or be mild sarcastic/cynical that are funny to think about (not sad sarcastic/cynical)" (12 Oct 2026). The old "funny at once" is removed. The crab robot story (11 Oct, not in the pool) was Rafi's own choice before this rule.
    HOW CLAUDE EXPLAINS TO HIM: "explain to me like I am six years old", "simple English so I understand" (12 Oct 2026). Applies to every explanation given to Rafi.
    HEADLINES LEVEL IS A CONSTANT: "yesterday headlines level were perfect ... so we will keep those settings as our constant" (12 Oct 2026). The level is the 11 Oct lines; its description is in assets/headlines_model_lines.md under "The level" (mine, not yours: the description).
    NO TIME PRESSURE ON THE TEST: "we try it like this and decide today" (12 Oct 2026). DECIDED (Rafi, 13 Oct 2026, "yes exactly!"): the Headlines length wording of rule 22 (aim 8 seconds, 10 for a long item, 12 the hard limit) and the model lines file stay as they are.
    "too complicated to explain in one sentence" (Rafi, 11 Oct 2026, about a fun story): a story that needs more than one sentence to explain does not become a clip.
    "not funny but definitely fun" (Rafi, 11 Oct 2026, the crab robot): fun counts, see FUN STORIES.
25. CARDS AND HEADLINES WORDING: ONE WRITER AND ONE CHECKER PER PRODUCT (Rafi, 12 Oct 2026, his words: "split it! Opus at max writes, fable at high checks"; "for now use opus at max to write"; "we will try this option than change if we didnt like it"; his reason: "cards are level 6 out of 10 ... and headlines are level 5 out of 10, so maybe each product get a different writer and checker").
    For the wording of the cards and the Headlines this replaces "Fable ... writes their wording" (STORY CHOICE) and, for that wording, "Opus does the checks" and the rewrite agent of MODEL POLICY; the choice of the stories stays as it is. Each writer runs its own checking scripts before handing back; each checker reads once (stranger, rules, facts; for Headlines also the read-aloud test and the match with the card); the same writer fixes once; then Rafi sees everything (Part B steps 2 and 3). (Mine, not yours: the wording around his quotes.)
26. VIDEO WORK AND FOOTAGE (Rafi, 12 Oct 2026, his words; the wording around his quotes is Claude's):
    "only footage that can be reused" (the licence must allow reuse; the credit goes on the video; docs/V1_TASKS.md lesson 243).
    THE VIDEO LESSONS ARE ALWAYS FOLLOWED: "make sure the lessons are being transferred in full and will always be followed to all future work" ("cap cut... holographic screen position... layers... etc."). Every session that renders, fixes, stitches or finishes the Headlines video reads docs/V1_TASKS.md lessons 238 to 244 first and follows them; "lesson can go to repo but we will have to push those to astra as well which is on drive... later though"; "make sure lessons don't repeat... just elaborated coherently without loosing edges!"
    DRIVE UPLOAD: "for now I do it, later we find an automated way" (12 Oct 2026); what he uploads: "give me only the final products and the pool files" (Full Report and Bulletin PDFs, cards and contact sheet, the Headlines JSON, and the pool PDF, CSV, markdown and JSON); the automated upload is a script that runs when the final products exist and puts each file in its Drive place (to build; Rafi's yes, 12 Oct 2026).
27. WRITERS FASTER (Rafi, 12 Oct 2026, his words, after the card writer took 23 minutes and the Headlines writer 22 for a few thousand characters of text): "change it to opus on normal than!!!! Not at max"; "make it read so we dont go back and make mistakes" (read the rules once if the model can hold them, not before each item); "it makes sure it follows each card and dont forget"; "2 minutes is better than 22"; "yes fix it for tomorrow".
    For the Part B card writer and Headlines writer this replaces "at max" of rule 25 (Opus on normal effort) and the "re-read before each item" of the READER LEVEL line: the writer reads one pre-loaded story pack once (make_wording_prompts.py writes it: the phrasing rules and the entry and facts of every item), writes everything in one pass, goes through each item once against the hard rules, runs the checking scripts once and fixes once; the checkers stay as in rule 25. Part A writers are unchanged until Rafi says. (Mine, not yours: the wording around his quotes and the scope to Part B.)
28. DAILY HEADLINES LISTEN, EVERY DAY, NO EXCEPTION (Rafi, 12 Oct 2026, his words, while driving; he repeated: "Make it clear, I want it every day"): "Maybe I should do the read and listen every day. 90-second listen is best for me. So the headlines, so always we do that. The headlines will be, you'll just put it in text and read it to me. And just like this. And that will be the check."; "You don't need to create a text file, you just write it in text here in the chat and I'll just press play."
    His decision on the Fable check: "For now, we keep both. Later, when the whole system works well, we see how we can save tokens." So the Fable checker of rule 25 stays, and the listen is added after it (Part B step 7).
    (Mine, not yours: the wording around his quotes. The shape of the listen follows what he heard on 12 Oct: one chat message, the spoken lines only, in clip order, said "Clip one" and so on, A I and U S spelled as the clip says them, no dashes or symbols, then a two line note. If he wants it changed he says so.)
29. RAFI'S DECISIONS OF 12 AND 13 OCT 2026, HIS WORDS (rule 8; the wording around his quotes is Claude's):
    TWO CHATS: "ok we stay 2 chat for now" (12 Oct 2026): this cloud chat and the local Part B chat on his PC.
    HIS PC: "we just need to make sure my pc stays secure" (12 Oct 2026). A second computer for the work: "we keep that option for future" (12 Oct 2026).
    DRIVE UPLOAD KEY: "we will do that later with chat gpt...who already opened an account with google cloud" (12 Oct 2026): the key for the automated upload of rule 26 comes later, from that account.
    ARTICLE: "article mean item, can be a headline or a full item" (13 Oct 2026). When he says article, it can mean a Headlines line, a card or a full report entry; ask which one only when it matters.
    BIGGER PICTURE IN THE BULLETIN: "300-500 words is fine for now" (13 Oct 2026); "stick to whats necessary".
    DRIVE DUPLICATES CLAUDE MADE: "rename and move to archive!" (13 Oct 2026), as rule 3 says, never delete.
    LESSONS FOR THE REPO: "yes must!!! lesson are important to not repeat mistakes" (13 Oct 2026). The local chat ends its answers with a list headed LESSONS FOR THE REPO; Rafi passes it to the cloud chat, which writes each lesson into docs/V1_TASKS.md once.
    DOWNLOADS: asked "should the local chat ask you before it downloads any file?", Rafi said "yes" (13 Oct 2026). The local chat asks him first and names the file, where it comes from and its size.
    MISTAKES NOT AGAIN: asked "should the card checker read each card as if out loud and check that it flows like real speech, and should I always show you the real thing, never a description?", Rafi said "yes" (13 Oct 2026). The card checker has the read aloud test (briefs/check_cards.md 1b); Claude always shows Rafi the real lines, cards or files, never a description of them (lesson 274).
    FUN CLIP CHOICE: "not necessary. you give me the concept and ill tell you if its funny. but I want to get to a point you understand whats funny and you choose yourself. full autonomous chain!" (13 Oct 2026). For now Claude gives him the fun concept and he says if it is funny; the goal is that Claude chooses the fun clip alone, with no stop. This replaces the "at most three finished lines" idea of lesson 236.
30. CRITICALS ALWAYS ON TOP (Rafi, 14 Oct 2026, his words: "You have strict rules that criticals always go on top. Everything that's rated 10 is always broadcast. It pushes everything down."; "You add it to the fucking script so this doesn't happen again. If there's critical, they go above and push everything down."). A story rated 10 is the first card and the first Headlines clip, above Politics, and pushes the rest down. pick_gate.py G11b was changed the same day so a Politics clip may sit behind critical clips. (Mine, not yours: the wording around his quotes.)
31. RAFI'S WORDS OF 15 OCT 2026, ON EMPTY BULLETIN SECTIONS AND RULES (rule 8; the wording around his quotes is Claude's):
    POLITICS CLIP AND THE 6s: "we said no politics we take at least 2 items from 6!"; the China story (Alibaba's Qwen on iPhones, score 6) was wanted as the Politics card and clip: "the china news is great!". It entered the Bulletin with a second Politics story from the 6s and is clip 1. "this goes for all categories": the same holds for every Bulletin category, see BULLETIN SECTIONS NEVER EMPTY in rule 14.
    RULES ARE HIS TO CHANGE: about the Headlines-in-Bulletin rule of rule 24: "this rule is not a brick in stone. I can change it if needs. not you without asking me."
    Rafi's yes (15 Oct 2026, "yes to all what you asked before"): a section whose stories at 7 and up are ALL headline only counts as empty for rule 14, because a card or clip needs a story read in full (mine, not yours: the wording). Today Politics had two at 7, both headline only, and I treated it as not empty: my miss.
32. RAFI'S WORDS OF 15 OCT 2026, ON HEADLINES, CARDS AND CUSTOMER PRODUCTS, HIS WORDS (rule 8; the wording around his quotes is Claude's):
    USELESS TAIL: "why would you add... useless text to an item and make the generation a few minutes longer... this repeats all the time". A hedge is one word (would, reportedly, may, says), never a clause; a speaker's own hedge is not a why; the writer and the checker cut a last part that adds nothing (briefs wording_headlines.md and check_headlines.md carry it).
    FROM WASHINGTON: "From Washington means in politics... that was fine to say": the one place allowed as an opening, for politics only (check_headlines_rules.py B2d and B2e allow it; the brief line 27 says so).
    NAMES NEED TITLES: "a name should get a title so we know why his words are important/creditable", simple, for every named person in every product.
    CUSTOMER PRODUCTS: "this is a final product for customers. must be precise! elegant, good looking, designed well and easy to follow": no codes, rule numbers or process words in a product (the Bulletin purpose line prints section names, not codes; the Bigger Picture brief forbids process wording).
    SIMPLE ANSWERS: "simple english line, at most two lines if complicated to explain"; "I didn't ask you to summarize" when he asks to repeat the questions: repeat the questions, one line each.
    THE FUN CLIP: the opening "In today's fun corner"; "leave it as accepted... as long as he got booked another follow-up. it is not the topic." (the source says the bots booked a follow-up, not that he got the job).
33. SOCIAL POSTING (Rafi, 15 Oct 2026, his words): "I want this session to be incharge of posting to all social medias"; "I want it to be eassy ...so when claude finishes its work. it autamticly post it"; "claude should have some sort of mcp to the app". Tool under study: Postiz (open source). Not built yet; setup and platforms still to be decided by Rafi.
    (Mine, not yours: the wording around his quotes, and this reading: posting starts only after his approval stop of Part B, and the Headlines video is made on his PC.)
34. RAFI'S WORDS OF 16 OCT 2026, ON STORIES THAT ALREADY RAN AT 7 OR MORE (rule 8; the wording around his quote is Claude's): about three stories the viral sweep left out because they ran at 7 or more on earlier days (Anthropic Q3 revenue, the states suing OpenAI, Windows for the Nvidia RTX Spark laptops), Rafi said: "keep them if they are meaningful updates." So a story that ran at 7 or more may come back when it is a meaningful update (new facts, not the same news again); Claude judges that story by story and says which and why. This answers the open question of lesson 195 for the viral rule. (Mine, not yours: this reading, and that skill step 1c and viral_sweep.py are not changed until Rafi says yes to the exact edit.)
35. RAFI'S WORDS OF 16 OCT 2026, ON STORIES WE COULD NOT READ (rule 8; the wording around his quotes is Claude's): when a story has no readable copy, "note than should be 'access full article on the source website / source name / link'"; "for bulletin you need one paragraph ... searching for same article and write just one paragraph about the topic"; "you can have a quick search, and also get information from sources related to the item". So: first a quick search for the same story at another outlet and related sources, then one paragraph from what was read; only a story still not found ends with "Read the full article at <source name>." (the source name and link are printed under the story). Rafi saw both versions on the real Bulletin page and picked this one ("B"). The old line "Note: we could not open the original article ..." is not printed any more (rule 32). (Mine, not yours: this reading, and the skill text and the post-build step that apply it; build_products.py is not changed until Rafi says yes to the exact edit.)
36. RAFI'S WORDS OF 16 OCT 2026, ON PLAIN WORDS (rule 8; the wording around his quotes is Claude's): about the Bigger Picture clip that said borrowing is getting "dearer": "Stop using the word dearer!!!! ... Headlines are 5 out of 10!!! Simple fucking english. Why are you always repeating the same mistake over and over again." Every spoken line and every card line uses words an ordinary person says in daily talk, no rare or British words (not dearer, debut, watchdog; say costs more, start, regulator or the agency's name). The two wording writers read each line once for this before handing back, and the checkers check it. (Mine, not yours: the wording around his quotes and the example words.) Rafi's follow-up (16 Oct 2026, his words): "we don't want to really keep it person turn to a friend. We still want to make it news-like, but it has to be news that are very, very simple for people to understand. So the word dearer is shit. Just say, more expensive, cost more, whatever option ... and then you don't use the stupid down 5th and instead drop down 30% or whatever. All kind of examples like that." So the register is news-like and very simple, not chatty; a plain number or percent, not a fraction such as a fifth. (His message stopped at "So make sure you"; the rest is not yet known.) (Mine, not yours: this reading.)
37. RAFI'S WORDS OF 16 OCT 2026, THE STYLE HE WANTS (rule 8; the wording around his quotes is Claude's): about the rewritten insurance clip, "In finance. The cost of insuring A I debt hit a record, which means investors fear it may not be repaid, and data centre firms like CoreWeave are hurt most.": "This is an amazing item, and that's how things should be explained. Simple English so people understand what is fucking going on. This is super. If all the news will be like that, my business will succeed." Before it, about the first version ("Insurance against tech firms failing to repay reached record prices ..."): "completely not understandable ... Explain to a person what happening". So a clip says what happened and what it means, in very simple English, one sentence, and a named person gets a real title ("Mark Levine, New York City's chief financial officer"). Whether this applies to every clip is Rafi's to say. (Mine, not yours: the wording around his quotes.)
38. RAFI'S WORDS OF 17 OCT 2026, ON THE BIGGER PICTURE (rule 8; the wording around his quotes is Claude's): "For today, use Opus high because we're low on credit. Maybe later we're going to go back to Fable. I want to see the outcomes. So now we're going to try for maybe for the next week Fable at high, one page at maximum ... not like yesterday it was 12,000 words, about six pages of useless. It was good information, but not necessarily correct as a bigger picture. The bigger picture should summarize what is happening in the field ... We need to give an investor a clear investor tips and where the market is heading. So what is happening in the market and the conclusions."
    So: the Full Report Bigger Picture is one page at most. Model and effort: 17 Oct 2026 Opus at high; from the next run, for about a week, Fable at high; then Rafi looks at the outcomes. This replaces "Fable at effort max" of BIGGER PICTURE MODEL (9 Oct) and the long form of the Full Report version. Content: what is happening in the market, the conclusions, where the market is heading, clear investor takeaways. The "not financial advice" line of BIGGER PICTURE WEIGHT (7 Oct) stays. (Mine, not yours: reading "investor tips" as plain takeaways and things to watch, no buy or sell calls, until he says otherwise; the Bulletin version stays at 300 to 500 words, which is under one page.)
