The Bigger Picture: written by one agent (model and effort: ONLY the BIGGER PICTURE MODEL line of CLAUDE.md; the main session never writes it), after the editors finish and after the
build that applies their holds (the item numbers must be final). One story at three lengths (CLAUDE.md rule 17):
the Full Report carries the full analysis, the Bulletin a deeper look than the card, the card and the Headlines
clip (Part B) the short hook. All three tell the same story: a summation of the big things happening, focused on
what moves the market, then things to watch, each with the reason to watch it.

NEW SHAPE FROM 18 OCT 2026 (Rafi, 17 Oct 2026, CLAUDE.md rules 38 and 40; where items 1 and 2 below differ, THIS BLOCK WINS; the old text is kept in bigger_picture_old_17oct.md):
A. Full Report version: ONE PAGE AT MOST, about 450 to 600 words. A short summary of what is happening in the market, then the conclusions, then exactly 5 key points on where the market is heading (weeks, months, years). Each key point: its time frame, the chances in percent with the reason, what would confirm it, what would weaken it. Same JSON shape as item 1 (sections with paragraphs), with the key points as the paragraphs of one section "Key points", plus a top level "key_points": [{"n", "use", "text"}]: point 1 use "headline" (the clearest point, understood in 8 spoken seconds), point 2 "card" (a short hook), points 3 and 4 "bulletin", point 5 "full". Citations {Cnn-nn} only in the section paragraphs.
B. Bulletin version: 300 to 450 words, one page: a 3 sentence summary plus the two points marked "bulletin", no citations.
C. Content: market and money points only (what moves the market, where it is heading). No policy or safety points unless they move the market. Trends and chances, no company names for stocks to buy, no buy or sell calls; the not financial advice line stays at the end of every version. A point may repeat from earlier days: say it is coming up again.
D. Lessons of 17 Oct (the Fable review of the Opus and Fable versions): every chance needs a reason from the stories, never a round number with no reason; no forecast that can hardly lose (for example "nothing happens by 2027"); a company's reporting date is a signal, never say a company states a plan at it unless a story says so; do not stretch one company's case to a whole group; do not use "a quarter" for a fall, give the percent; plain words only (no yield, restructuring, write off, comptroller: say what it means); every named person gets a title; one point must not contradict its own source story; if the same question was answered in an earlier edition, say why the chance changed.
E. Model: from 18 Oct 2026, Fable at high effort for about a week, then Rafi looks at the outcomes (CLAUDE.md rule 38). Do the second reader step on your own files.

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
- The one-quarter markets cap (Full Report rule 5.5) does NOT apply to the Bigger Picture corner (CLAUDE.md rule 17, newest ruling, 2 Oct 2026, "for this corner only"); no tickers; no buy or sell advice.
  (Rafi, 15 Oct 2026: the markets share is NOT printed in any product. NEVER print a rule number, a file name, "CLAUDE.md", "pool", "cut-off" or any other process wording in the Bigger Picture: it is a customer product. A person named gets a title in the same sentence.)

2. Bulletin: write WORKDIR/bigger_picture_bulletin.json {"title": "The Bigger Picture — Daily AI Analysis",
   "paragraphs": [...]}, 300 to 500 words, only what is necessary (Rafi, 13 Oct 2026: "300-500 words is fine for now"), plain words, NO {Cnn-nn} citations (the Bulletin prints no item numbers):
   (1) "A deeper look at today's Bigger Picture card: what is moving the market, and what to watch. The Full Report
   carries the full analysis." (2-3) "What moves the market today. Fact: ..." with attribution and hedges;
   (4) "Our view: ..."; (5) "What to watch and follow. 1. ... 2. ..." each with why it matters; (6) "Unknowns. ...".
   The markets cap of rule 5.5 does not apply to this corner (CLAUDE.md rule 17).

3. Run build_products.py again; it says "Bigger Picture: included" and prints raw {C..} marks if any are left.
4. A second reader checks every Fact against its report entry before the final build (step 12). Its input is one file: `make_prompts.py --workdir WORKDIR --stage bp_pack` writes WORKDIR/prompts/bp_reader_pack.md (both Bigger Picture files and the entry and facts of every cited item), read once instead of file by file (chain fix, 13 Oct 2026).

5. WHAT COMES NEXT (Rafi, 7 Oct 2026; written by a Fable agent): do real work on the part that looks ahead. Find the scheduled events of the coming days and weeks that bear on the day's story
   (company earnings, votes, court dates, launches, regulator or data releases), using web search sparingly, and give each one its date and its source. Say plainly when a date is not
   confirmed. Explain why each one matters and what result would change the picture. Never invent a date. Every version ends with: "This is analysis of the news, not financial advice or an
   investment recommendation."
Work only inside WORKDIR: never run git and never write files in the repo folder (chain fix, 13 Oct 2026).
