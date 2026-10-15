# Model test, 14 Oct 2026: which model and effort each helper needs

Read this before changing any model or effort in the daily scan (CLAUDE.md points here).

## In one paragraph

We ran 72 helper agents on real stories of 13 and 14 Oct 2026, blind, with identical inputs: Haiku, Sonnet, Opus and Fable at different efforts. On an easy job (article handed over) the cheap settings wrote almost as well as the expensive ones. On the real job (find the article, blocked sites, credit chain, old news) low effort made judgment mistakes: it missed old news and credited copy sites instead of Reuters. Max effort never helped. Haiku slipped every time. Opus got credit right at every level. Fable wrote best but costs about 5 times Sonnet. Nothing has been changed yet; the options are in Part 3.

## The files

| File | What it holds |
|---|---|
| `1_TRIALS.md` | Every trial: setup, stories, every version's time, cost and verdict |
| `2_FINDINGS.md` | 14 findings with evidence and certainty |
| `3_CONCLUSIONS.md` | Recommendations, options per helper with cost and risk, what is unproven, how to run the test again, the decisions log |
| `report.html` | The same results as charts and tables (open in a browser) |
| `data/` | Raw outputs, unblinded: every entry each version wrote, curator picks, time and tokens per agent |

## The seven things to remember

1. Model is how smart; effort is how long it thinks.
2. Never max effort.
3. Never Haiku for news work.
4. Test the real job, not an easy version of it.
5. Low effort is fine for picking stories, not for the writer's full job.
6. Opus has the best judgment (credit, old news); Sonnet high held up at half its price.
7. Fable: best wording, 5 times the price; only for the few items that need it.

## Keywords (for searching later)

model test, effort test, Haiku Sonnet Opus Fable, max effort, writer model, curator model, MODEL POLICY, credit chain, old news, Unite.AI, Firmus, 14 Oct 2026.
