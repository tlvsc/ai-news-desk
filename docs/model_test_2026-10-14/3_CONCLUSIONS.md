# Part 3. Conclusions and options

Status on 15 Oct 2026: **nothing has been changed yet.** These are the options for Rafi to decide. When a decision is made, write it into `CLAUDE.md` (MODEL POLICY) and add the date here.

## The short answer

1. **Never use max effort**, for any helper. It costs 5 to 20 times the time and wrote no better.
2. **Do not use Haiku** for news work. It slipped in every story.
3. **Do not judge a setting on an easy test.** With the article handed over, everything looks fine. The real job, with blocked sites, credit chains and old news, is where the settings differ.
4. **Low effort is fine for picking, not for the writer's full job.** Low effort missed old news and got credits wrong.
5. **Opus was the most reliable on judgment** (credit right at every level, the only one to catch reposted old news when picking). It costs about twice Sonnet.
6. **Fable writes the best but costs about 5 times Sonnet** and was the slowest. Keep it for the few items where the best wording matters.

## What the helpers use today (live CLAUDE.md, 14 Oct 2026)

- Curators, fillers, Part A writers, setup, Drive delivery: Sonnet (no effort set, so Sonnet's default, high).
- Editors, stranger check, rules agent, rewrite agent: Opus at extra high.
- Bigger Picture: Fable at max.
- Part B card and Headlines writers: Opus at normal effort, since 12 Oct.

## Options per helper

### Curators (choosing stories)

| Option | Quality seen | Time | Cost | Risk |
|---|---|---|---|---|
| A. Sonnet high (today) | Agreed with all on top stories; took old news as new | about 110 s | 0.36 to 0.41 | Old news slips through |
| B. Sonnet medium | Same picks, faster | 67 to 86 s | 0.34 to 0.37 | Same old news risk |
| C. Sonnet low | Same picks, fastest Sonnet | 50 to 62 s | 0.32 to 0.34 | Same old news risk |
| D. Opus high | The only one to reject reposted old news | 173 to 280 s | 1.06 to 1.57 | Slow, 3 to 4 times the cost |
| E. Sonnet medium plus a separate old news check | Picks as B; the check catches reposts | B plus the check | B plus the check | Needs building |

Recommendation: **E**. Picking is easy (finding 10), old news is the only weakness (finding 8). The old news check can be a script that looks up each story's first report date, or one Opus high agent over the whole pool. The run already has check_dup14.py for stories we ran before; this would catch stories that are simply old.

### Part A writers (fetch, read, write)

| Option | Quality seen on the full job | Time per 5 stories | Est. cost per 5 | Risk |
|---|---|---|---|---|
| A. Sonnet high (today) | Caught old news, credit right, clean | 207 to 285 s | 0.43 to 0.59 | Slowest Sonnet |
| B. Sonnet low or medium | Missed old news, credited a copy site, long summaries | 147 to 223 s | 0.28 to 0.45 | Judgment errors reach the report |
| C. Opus low | Fastest of all, credit right, but missed old news | 127 to 136 s | 0.64 to 0.73 | Old news slips |
| D. Opus medium | Caught old news, credit right | 187 to 271 s | 0.83 to 1.11 | About twice Sonnet |
| E. Opus high | Best judgment overall | 190 to 345 s | 0.91 to 1.26 | Slower, over twice Sonnet |
| F. Fable low | Best wording; one credit slip | 386 to 552 s | 2.07 to 2.46 | 5 times Sonnet, slowest |

Recommendation: **A, keep Sonnet high.** It held up on the real job at about half the price of Opus. Move to **D, Opus medium**, only if credit or old news slips keep reaching the report. The old news check of the curator option E would also cover the writers' miss.

Optional add-on: the detail line of trial 5 (named quote, telling detail, what happens next). It worked on Sonnet, but its home is the Drive phrasing file (CLAUDE.md READER LEVEL says the writing shape lives only there), so Rafi or ChatGPT would add it there.

### Other helpers, not tested here

Editors, the stranger check, the rules agent, the Bigger Picture and the Part B writers were not tested. Their settings stay as they are until a test of their own real job is run. Do not move them on the strength of this test.

## Money and time, a rough daily picture

A day has about 150 to 250 written items in 16 categories. Using the full job estimates per 5 stories (input side only):

| Writers on | Est. input cost per day | Writer time per category (5 stories basis, scaled to about 15) |
|---|---|---|
| Sonnet high | about 15 to 30 dollars | about 10 to 14 minutes |
| Opus medium | about 30 to 55 dollars | about 9 to 14 minutes |
| Fable low | about 60 to 120 dollars | about 20 to 28 minutes |

These are estimates from 10 stories; output tokens are missing. Measure the real day after any change.

## What this test did not prove

1. Only 4 easy stories and 10 full job stories. The gaps between Sonnet and Opus are small and could change with more stories.
2. The full job used 5 stories per writer; the real job is 15 to 20. Long jobs may tire low effort more.
3. Facts files were not graded, only the report entries.
4. Helpers loaded an old CLAUDE.md (no FAMOUS PEOPLE RULE).
5. The 9 Oct dates for the McDonald's and Pennsylvania stories are Opus high's claim, not checked by hand.

## How to run this test again

1. Pick stories (or a whole category) and give every version identical inputs in its own folder.
2. Use the real brief from the live branch, filled like make_prompts.py does.
3. Test the real job (links only, the writer fetches), not only a preloaded article.
4. Run the full grid every time: Haiku high, Sonnet low, medium and high, Opus low, medium and high, Fable low. No max.
5. Keep labels blind until the results are read.
6. Record time and tokens from the helper transcripts (data/agent_runs.json shows the fields).
7. Grade on the checks that matter: read or headline only, credit to the first reporter, old news caught, rule slips, length, invented facts.
8. Save the results here (a new dated folder) before deciding.

## Decisions log

| Date | Decision | By |
|---|---|---|
| 14 Oct 2026 | Full grid on every test story; no narrowing | Rafi |
| (open) | Curators: option ... | |
| (open) | Part A writers: option ... | |
| (open) | Detail line in the Drive phrasing file: yes / no | |
| (open) | Build the old news check: script / Opus agent / no | |
