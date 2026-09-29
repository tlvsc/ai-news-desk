The Bigger Picture: written by the main session (not an agent), after the editors finish.

Rules: WORKDIR/rules/Full_Report_V1_Rules_Structure.txt section 5.5 (fixed order, labels, forecasts,
endings A to D). Use today's report plus earlier reports when they are available in Drive.

Write WORKDIR/bigger_picture.json:
{"title": "The Bigger Picture — Daily AI Analysis",
 "description": "What today's developments could mean for technology, business and everyday life",
 "sections": [
   {"title": "1. What AI can do now", "paragraphs": ["Fact: ... {C04-01}.", "Inference: ..."]},
   {"title": "2. People and society", "paragraphs": [...]},
   {"title": "3. Safety, security and law", "paragraphs": [...]},
   {"title": "4. Infrastructure", "paragraphs": [...]},
   {"title": "5. Markets", "paragraphs": [...]},
   {"title": "Forecasts", "paragraphs": ["1. ... Probability 60 percent. Horizon: 1 to 3 months. Confidence: medium. Signal: ... {C08-01}. Confirms: ... Weakens: ... Affects: ..."]},
   {"title": "A. Highest conviction developments to watch", "paragraphs": [...]},
   {"title": "B. Low probability, high impact scenarios", "paragraphs": [...]},
   {"title": "C. Signals that would change this view", "paragraphs": [...]},
   {"title": "D. Key unknowns and data gaps", "paragraphs": [...]}]}

- Cite stories as {Cnn-nn} (pool item ids); build_products.py turns them into "(item N)".
  Cite only stories that are in today's report; the script warns about any that are not.
- Every Fact is attributed as in its story ("a researcher says", "Reuters reports").
  Keep every hedge; a report of a plan is not the plan happening.
- Markets at most a quarter of the analysis; no tickers; no buy or sell advice.
- A second reader checks it against the report entries before the final build (step 12).
