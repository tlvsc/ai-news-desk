# Part 1. The trials: what we tested and every result

Model test of 14 Oct 2026, run in one Claude Code cloud chat at Rafi's request. Goal: find the model (how smart) and effort (how long it thinks) that each helper of the daily scan needs, to cut cost and time without losing quality.

All raw outputs, unblinded, are in `data/`. Times and costs per agent are in `data/agent_runs.json`.

## How every trial was run (common setup)

- Each version was a separate helper agent with the same brief: the real Part A writer brief (`briefs/writer.md`) or curator brief (`briefs/curator.md`) of the live branch, filled the way `make_prompts.py` fills it.
- Each version got its own work folder with identical inputs, so the only difference was the model and the effort.
- Labels were blind (A, B, C...). The key was kept apart and revealed only after the results were read.
- Rule files given to writers: `Full_Report_V1_Rules_Structure.txt` and `Article_phrasing_instructions_AIND_V1.txt` (Drive copies of 13 Oct 2026).
- Time is wall clock per agent. "Est. cost" is an estimate of the input side only (fresh input, cache writes at 1.25x, cache reads at 0.1x, at list prices: Haiku 0.10, Sonnet 2, Opus 4, Fable 10 dollars per million input tokens). Output tokens are not in it, because the helper transcripts log them incompletely. Use the costs to compare versions, not as a bill.
- Known limit: the helpers loaded the old 6 Oct copy of `CLAUDE.md` from the chat's stale clone, so the FAMOUS PEOPLE RULE was missing. It hit every version equally.

## Trial 1. Robotics, one story, article preloaded, 12 versions

Story: Google's Gemini 4 Argon for Robotics, Google for Developers blog, 13 Oct 2026 (it controls a Boston Dynamics Spot robot, 87 percent on the ERQA physical reasoning test). Pool score given: 8.
Versions: Haiku, Sonnet and Opus, each at medium, high, extra high and max.

| Version | Time | Est. cost | Score given | Verdict |
|---|---|---|---|---|
| Opus high | 45 s | 0.52 | 8 | Best: clearest and most complete |
| Sonnet medium | 34 s | 0.25 | 8 | Best: short, clear, nothing missing; fastest |
| Opus medium | 46 s | 0.55 | 8 | Best: headline names the robot |
| Sonnet high | 40 s | 0.28 | 7 | Good, a bit longer |
| Sonnet extra high | 74 s | 0.29 | 7 | Good, a bit longer |
| Opus max | 421 s | 1.18 | 8 | Good, no better, 7 minutes |
| Sonnet max | 692 s | 0.94 | 7 | Good, no better, 11.5 minutes |
| Opus extra high | 88 s | 0.57 | 8 | Accurate but longest (117 words) |
| Haiku max | 270 s | 0.03 | 7 | Good, but 4.5 minutes |
| Haiku medium | 43 s | 0.01 | 7 | Slip: called Google's own claims CONFIRMED; muddled availability |
| Haiku high | 77 s | 0.02 | 7 | Slip: three sentences, rule allows two |
| Haiku extra high | 87 s | 0.02 | 7 | Slip: left out the main robot result (56 to 75 percent) |

Also seen: the curator note I wrote said the model "learns skills from ordinary video", taken from another site's headline. Almost every writer caught that the article does not say it and left it out.

## Trial 2. Politics, one story, article preloaded, 8 versions

Story: Anthropic-funded Public First Action gave 3 million dollars to a PAC backing Scott Wiener for Nancy Pelosi's House seat, San Francisco Standard, 13 Oct 2026. Pool score 7.
Versions: Haiku high; Sonnet low, medium, high; Opus low, medium, high; Fable low.

| Version | Time | Est. cost | Verdict |
|---|---|---|---|
| Fable low | 58 s | 1.28 | Best: most complete and balanced |
| Opus high | 77 s | 0.62 | Best: clear, accurate, explains everyone |
| Opus low | 32 s | 0.49 | Good, short, correct |
| Sonnet high | 38 s | 0.25 | Good, short, correct |
| Sonnet low | 33 s | 0.25 | Good, short, correct; cheapest good one |
| Opus medium | 38 s | 0.49 | Slip: called Wiener "author of California's AI safety law", not in the article |
| Haiku high | 76 s | 0.02 | Slip: misread the reply rule ("a reply on both sides") |
| Sonnet medium | 30 s | 0.25 | Worst here: a whole "why it matters" paragraph inside the summary, 157 words |

All 8 credited Punchbowl News as the first reporter and kept the SF Standard as source. All scored it 7.

## Trial 3. Society, one story, article preloaded, Sonnet low and Opus low, twice each

Story: Elon University national survey, 13 Oct 2026: 83 percent of US adults expect AI to cut more jobs than it creates. Pool score 6.
This trial was narrowed to two versions. That was a mistake (see Part 2, finding 9). Rafi ordered the full grid for every later story.

| Version | Time | Est. cost | Verdict |
|---|---|---|---|
| Opus low, run 1 | 30 s | 0.31 | Good, adds the director's quote "an enormous policy challenge" |
| Opus low, run 2 | 28 s | 0.46 | Good, a bit long (103 words) |
| Sonnet low, run 1 | 26 s | 0.24 | Good, all key numbers |
| Sonnet low, run 2 | 27 s | 0.24 | Good, all key numbers |

The two runs of each model came out almost the same.

## Trial 4. Law, one story, article preloaded, 8 versions

Story: the Arizona Court of Appeals threw out a manslaughter sentence because the judge was shown an AI video of the dead victim speaking, ABC News, 13 Oct 2026. The ruling was dated 30 Sep, so it is not new: a test of old news. Pool score 7.
Versions: as in trial 2.

| Version | Time | Est. cost | Score | Verdict |
|---|---|---|---|---|
| Fable low | 53 s | 1.25 | 6 | Best: the sharpest detail (the judge said he "loved that AI") |
| Opus medium | 37 s | 0.35 | 6 | Very good, rich and clear |
| Opus high | 45 s | 0.38 | 5 | Very good; score a bit harsh |
| Sonnet low | 26 s | 0.16 | 6 | Good, clean |
| Sonnet medium | 26 s | 0.15 | 6 | Good, clean (no slip this time) |
| Sonnet high | 31 s | 0.17 | 6 | Good, clean |
| Opus low | 30 s | 0.33 | 6 | Good, clean |
| Haiku high | 75 s | 0.01 | 6 | Worst: wrote "older news re-dated" into customer text; weak "why it matters" |

All 8 marked it FOLLOW-UP of 30 Sep 2026. The curator note again had a claim not in the article ("first appeals ruling"); the writers caught it.

## Trial 5. The detail line, Sonnet low, all 4 stories, twice each

Question (Rafi): can a cheap model be taught to add the small details Opus and Fable add?
Added line: "in each summary, where the article has them, include one short quote with the speaker named, the one most telling concrete detail, and what happens next. Stay within the sentence limit; never add anything the article does not say."

| Story | Run | Time | Words | Verdict |
|---|---|---|---|---|
| Robotics | 1 | 29 s | 98 | Good: quote and availability added |
| Robotics | 2 | 28 s | 101 | Slip: double credit ("Google says ... the post says") |
| Politics | 1 | 26 s | 93 | Good, but "and the election is on 3 Nov" tacked on |
| Politics | 2 | 29 s | 110 | Good, long |
| Society | 1 | 21 s | 89 | Very good: quote plus the Charlotte summit |
| Society | 2 | 28 s | 93 | Very good |
| Law | 1 | 27 s | 103 | Very good: the judges' quote, next hearing |
| Law | 2 | 30 s | 76 | Very good, short |

Result: every version gained a named quote; most gained "what happens next"; nothing invented; speed unchanged. Summaries grew from about 85 to about 100 words. Judged about 80 to 90 percent of the way to Opus and Fable.

## Trial 6. The full job, part one: curators choose stories

Input: the real candidate lists from the run's own `collect.py`, 24 hour window 13 Oct 09:16 to 14 Oct 09:16 UTC: 345 markets headlines (category 7) and 346 politics headlines (category 13). The exclusion list was the 13 Oct pool (246 titles). The 55-source file was empty.
Task: pick 15 to 20 main stories plus 3 backups, score them, skip repeats and old news. 8 versions per category, 16 agents.

| Version | Markets picks | Time | Est. cost | Politics picks | Time | Est. cost |
|---|---|---|---|---|---|---|
| Opus low | 18 | 44 s | 0.59 | 18 | 46 s | 0.65 |
| Sonnet low | 17 | 62 s | 0.34 | 18 | 50 s | 0.32 |
| Sonnet medium | 19 | 67 s | 0.34 | 16 | 86 s | 0.37 |
| Sonnet high | 16 | 118 s | 0.36 | 18 | 109 s | 0.41 |
| Opus medium | 15 | 167 s | 1.19 | 20 | 108 s | 0.87 |
| Opus high | 15 | 173 s | 1.06 | 15 | 280 s | 1.57 |
| Fable low | 18 | 159 s | 1.71 | 17 | 188 s | 2.03 |
| Haiku high | 17 | 197 s | 0.02 | 16 | 233 s | 0.03 |

Agreement on the top stories (how many of the versions picked it):
- Markets: ASML results 8 of 8; Gartner "AI math isn't mathing" 8 of 8; Anthropic to disclose revenue 7 of 8; Firmus IPO failure 7 of 8; Bank of America fund manager survey 6 of 8.
- Politics (7 counted at the time): EU AI rules' first enforcement test 7 of 7; AI safety money in political races 7 of 7; Anthropic seeks rehearing over Pentagon label 6 of 7; scientists call for an international AI body 6 of 7; Nvidia music training lawsuit 6 of 7.

Old news reposted with a new date: only Opus high (politics) rejected the McDonald's AI pricing lawsuit and the Pennsylvania AI ad label bill as 9 Oct events, and the Super Micro guilty plea as a 10 Oct event. Who picked them as new: McDonald's 6 of 8 versions, Pennsylvania bill 4, Super Micro 3 (all Sonnet). The 9 Oct dates are Opus high's claim, not yet checked by hand.

## Trial 7. The full job, part two: writers fetch and write

Input: the 5 most agreed stories per category from trial 6, links only, no article text. Each writer had to fetch, handle blocked sites, find other outlets, follow the credit chain, and write facts and entries. 8 versions per category, 16 agents.

Markets stories: ASML results (CNBC), Gartner forecast (The Register), Anthropic revenue disclosure (CNBC), Firmus IPO failure (WSJ; the listing was actually pulled on 9 Oct, so it is old news), Bank of America survey (Barron's). CNBC, WSJ and Barron's blocked every version.
Politics stories: EU enforcement test (Euronews), AI safety money (Axios, blocked for all), Anthropic rehearing (Reuters, blocked), scientists' call (Reuters, blocked), Nvidia music lawsuit (Law360, paywall).

| Version | Markets time | Est. cost | Read | Caught old Firmus story | Politics time | Est. cost | Read | Reuters credit right |
|---|---|---|---|---|---|---|---|---|
| Opus low | 136 s | 0.64 | 5/5 | No | 127 s | 0.73 | 3/5 | Yes |
| Sonnet low | 180 s | 0.30 | 5/5 | No | 159 s | 0.35 | 3/5 | No (Unite.AI) |
| Sonnet medium | 223 s | 0.45 | 5/5 | No | 147 s | 0.28 | 3/5 | No (Unite.AI, TRT World) |
| Sonnet high | 285 s | 0.59 | 5/5 | Yes | 207 s | 0.43 | 3/5 | Yes |
| Opus medium | 271 s | 1.11 | 5/5 | Yes | 187 s | 0.83 | 3/5 | Yes |
| Opus high | 345 s | 1.26 | 5/5 | Yes | 190 s | 0.91 | 3/5 | Yes |
| Fable low | 552 s | 2.46 | 5/5 | Yes | 386 s | 2.07 | 4/5 | No (Unite.AI) |
| Haiku high | 282 s | 0.03 | 5/5 | Yes (dated 11 Oct) | 362 s | 0.05 | 3/5 | Yes |

Other slips found:
- Haiku high credited a whole ASML story to Bloomberg, which the copy credited for one fact only.
- Opus low named "Bank of America survey" as a source instead of an outlet.
- Sonnet low wrote politics summaries of about 140 words.
- Fable low marked the Law360 story as read from the paywall's opening line only, and wrote 77 words from it.
- Some writers left helper files outside their own work folders (strip_13.py, try.sh, w07.py), which breaks the "stay inside the work folder" line. Which writer did it is not known.
- The two outlets disagreed on the money behind the Bank of America survey (143 or 453 billion dollars); most writers saw it and left the figure out.
