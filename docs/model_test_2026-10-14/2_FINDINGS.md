# Part 2. The findings

Each finding says what we saw, the evidence (trial numbers from Part 1) and how sure we are.

## The two dials

Every helper is set by two dials. **The model is how smart: Haiku, Sonnet, Opus, Fable, from smallest to strongest. The effort is how long it thinks: low, medium, high, extra high, max.** More effort means more time and more tokens. It does not always mean a better result.

## Finding 1. Max effort is never worth it
- Evidence: trial 1. Sonnet max took 692 seconds, Opus max 421 and Haiku max 270, against 34 to 46 seconds for the best versions. None wrote better.
- Certainty: high. 5 to 20 times the time for no gain.

## Finding 2. Extra high adds time but no quality for writing
- Evidence: trial 1. Opus extra high (88 s) wrote the longest entry; Sonnet extra high (74 s) was no better than Sonnet high (40 s).
- Certainty: medium (one story).

## Finding 3. Haiku is the weakest every time
- Evidence: trials 1, 2, 4. Rule slips in every story: wrong status, three sentences, a missing key fact, a misread reply rule, a process note in customer text. In trial 7 it misattributed a story to Bloomberg. It was also slow, because it worked longer to compensate.
- Certainty: high. Its only strength is price (about 20 times cheaper than Sonnet).

## Finding 4. On an easy job, Sonnet and Opus at low to high are close
- Evidence: trials 1 to 4. With the article handed over, Sonnet low, medium and high and Opus low, medium and high all wrote correct, hedged entries. Opus was a little richer in wording.
- Certainty: high for the easy job only. See finding 7.

## Finding 5. Fable writes the best, but costs about 5 times Sonnet and is the slowest
- Evidence: trials 2 and 4 (best both times: the sharpest detail and the best balance); trial 7 (552 and 386 seconds, the slowest; est. cost 2.46 and 2.07 against 0.30 to 0.59 for Sonnet).
- Certainty: high on quality and cost. Fable also made a credit slip in trial 7 (Unite.AI), so it is not perfect.

## Finding 6. Slips are partly luck; one slip does not condemn a level
- Evidence: Sonnet medium was among the best in trial 1 and the worst in trial 2, then clean in trial 4. Opus medium invented a small fact in trial 2 and was very good in trial 4.
- Certainty: high. Judge on the total across many stories, never on one.

## Finding 7. The easy test was misleading: the real job needs judgment
- Evidence: trials 1 to 5 (article handed over) against trial 7 (links only). On the easy job Sonnet low looked as good as Opus. On the real job it missed old news, credited a copy site and wrote 140 word summaries.
- Why: writing is easy for all of them. Judgment is the hard part: finding the story elsewhere when a site blocks us, following the credit to the first reporter, and noticing that a "new" story is old. Judgment is what thinking time buys.
- Certainty: high. This is the most important finding.

## Finding 8. Low effort misses old news
- Evidence: trial 7, the Firmus listing pulled on 9 Oct. Missed by Opus low, Sonnet low and Sonnet medium. Caught by Sonnet high, Opus medium, Opus high, Fable low and Haiku high. Trial 6: only Opus high rejected the reposted McDonald's, Pennsylvania and Super Micro stories.
- Certainty: medium to high (two trials, same pattern).

## Finding 9. Credit judgment differs by model: every Opus level got it right
- Evidence: trial 7, politics. With Reuters blocked, Opus low, medium and high credited Reuters (correct under the CREDIT rule). Sonnet low, Sonnet medium and Fable low credited Unite.AI, an AI-written copy site, or TRT World. Sonnet high and Haiku credited Reuters.
- Certainty: medium (one story pair).

## Finding 10. Choosing stories is easy; all versions agree on the big ones
- Evidence: trial 6. The top 5 stories in each category were picked by 6 to 8 of the 8 versions. No version missed a major story.
- Certainty: high. A cheaper model is enough for picking; catching old news needs a stronger check (finding 8).

## Finding 11. A cheap model can be taught the small details
- Evidence: trial 5. One added line gave Sonnet low named quotes and next steps in 7 of 8 runs, at the same speed. About 80 to 90 percent of Opus and Fable. Side effects: longer summaries (about 100 words), some details tacked on awkwardly.
- Certainty: medium. Tested on the easy job only.

## Finding 12. Blocked sites hit everyone equally
- Evidence: trial 7. CNBC, WSJ, Barron's, Reuters, Axios and Law360 blocked all 8 versions. In markets all 8 still read 5 of 5 through other outlets; in politics all got 3 of 5 (Fable 4, using a paywall's opening line).
- Certainty: high. The model does not change what we can fetch; it changes what the writer does about it.

## Finding 13. Time and cost per story (estimates)
| Version | Easy job, per story | Full job, per 5 stories | Est. input cost, full job |
|---|---|---|---|
| Sonnet low | about 26 to 33 s | 159 to 180 s | 0.30 to 0.35 |
| Sonnet medium | about 26 to 34 s | 147 to 223 s | 0.28 to 0.45 |
| Sonnet high | about 31 to 40 s | 207 to 285 s | 0.43 to 0.59 |
| Opus low | about 28 to 32 s | 127 to 136 s | 0.64 to 0.73 |
| Opus medium | about 37 to 46 s | 187 to 271 s | 0.83 to 1.11 |
| Opus high | about 45 to 77 s | 190 to 345 s | 0.91 to 1.26 |
| Fable low | about 53 to 58 s | 386 to 552 s | 2.07 to 2.46 |
| Haiku high | about 75 to 77 s | 282 to 362 s | 0.03 to 0.05 |
- Opus low was the fastest on the full job. Fable was always the slowest.
- Costs leave out output tokens (see Part 1, common setup). Compare them, do not bill them.

## Finding 14. Mistakes made during the test, and their fix
1. I narrowed the society test to two versions. Fix (Rafi): every test story runs the full agreed grid.
2. My curator notes twice carried a claim from another headline, not from the article. Fix: notes come from the article only.
3. I recommended Sonnet low from the easy tests before the full job test. Fix: test the real job before any recommendation.
