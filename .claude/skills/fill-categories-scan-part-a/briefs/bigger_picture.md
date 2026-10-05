The Bigger Picture: written by the main session (not an agent), after the editors finish and after the
build that applies their holds (the item numbers must be final). One story at three lengths (CLAUDE.md rule 17):
the Full Report carries the full analysis, the Bulletin a deeper look than the card, the card and the Headlines
clip (Part B) the short hook. All three tell the same story: a summation of the big things happening, focused on
what moves the market, then things to watch, each with the reason to watch it.

Rules: BEFORE EACH ITEM you write or fix, re-read Sections 1, 1A and 1B and your product section of WORKDIR/rules/Article_phrasing_instructions_AIND_V1.txt (its rule EVERY WRITER, EVERY ITEM). WORKDIR/rules/Full_Report_V1_Rules_Structure.txt section 5.5 (fixed order, labels, forecasts,
endings A to D). Use today's report entries (WORKDIR/report_entries) plus earlier reports when available.

1. Full Report: write WORKDIR/bigger_picture.json:
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
- In the Full Report, markets stay at most a quarter of the analysis (rule 5.5); no tickers; no buy or sell advice.
  Print the share: 3 Oct 2026 was 15 percent.

2. Bulletin: write WORKDIR/bigger_picture_bulletin.json {"title": "The Bigger Picture — Daily AI Analysis",
   "paragraphs": [...]}, about 350 words, plain words, NO {Cnn-nn} citations (the Bulletin prints no item numbers):
   (1) "A deeper look at today's Bigger Picture card: what is moving the market, and what to watch. The Full Report
   carries the full analysis." (2-3) "What moves the market today. Fact: ..." with attribution and hedges;
   (4) "Our view: ..."; (5) "What to watch and follow. 1. ... 2. ..." each with why it matters; (6) "Unknowns. ...".
   The markets cap of rule 5.5 does not apply to this corner (CLAUDE.md rule 17).

3. Run build_products.py again; it says "Bigger Picture: included" and prints raw {C..} marks if any are left.
4. A second reader checks every Fact against its report entry before the final build (step 12).
