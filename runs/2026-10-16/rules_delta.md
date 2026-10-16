# Rules delta for edition 2026-10-16: everything that changed since the rules check of 2026-10-15
Base: commit 468d519 (the save of runs/2026-10-15/rules_check.md); now: 24d30df.
Read with W/rules_check_previous.md. Lines starting with + are new, - are gone.

## 1. CLAUDE.md

diff --git a/CLAUDE.md b/CLAUDE.md
index 9d84d63..ec15f6b 100644
--- a/CLAUDE.md
+++ b/CLAUDE.md
@@ -151,2 +151,4 @@ not about which project it is.
     rules agent and the rewrite agent. NEVER Haiku (Rafi, 7 Oct 2026: not for setup, Drive, writers or anything else).
+    MODEL TEST (Rafi, 15 Oct 2026): before changing any model or effort, read docs/model_test_2026-10-14/README.md (72 blind
+    runs of 14 Oct 2026; nothing changed yet; the options and the decisions log are in its 3_CONCLUSIONS.md).
     STORY CHOICE FOR CARDS AND HEADLINES (Rafi, 7 Oct 2026, replaces the Fable-only-on-request line: "this is our adverts, if it
@@ -321,2 +323,13 @@ not about which project it is.
     RULES ARE HIS TO CHANGE: about the Headlines-in-Bulletin rule of rule 24: "this rule is not a brick in stone. I can change it if needs. not you without asking me."
-    (Mine, not yours, waits for your yes: my reading is that a section whose stories at 7 and up are ALL headline only counts as empty for rule 14, because a card or clip needs a story read in full. Today Politics had two at 7, both headline only, and I treated it as not empty: my miss.)
+    Rafi's yes (15 Oct 2026, "yes to all what you asked before"): a section whose stories at 7 and up are ALL headline only counts as empty for rule 14, because a card or clip needs a story read in full (mine, not yours: the wording). Today Politics had two at 7, both headline only, and I treated it as not empty: my miss.
+32. RAFI'S WORDS OF 15 OCT 2026, ON HEADLINES, CARDS AND CUSTOMER PRODUCTS, HIS WORDS (rule 8; the wording around his quotes is Claude's):
+    USELESS TAIL: "why would you add... useless text to an item and make the generation a few minutes longer... this repeats all the time". A hedge is one word (would, reportedly, may, says), never a clause; a speaker's own hedge is not a why; the writer and the checker cut a last part that adds nothing (briefs wording_headlines.md and check_headlines.md carry it).
+    FROM WASHINGTON: "From Washington means in politics... that was fine to say": the one place allowed as an opening, for politics only (check_headlines_rules.py B2d and B2e allow it; the brief line 27 says so).
+    NAMES NEED TITLES: "a name should get a title so we know why his words are important/creditable", simple, for every named person in every product.
+    CUSTOMER PRODUCTS: "this is a final product for customers. must be precise! elegant, good looking, designed well and easy to follow": no codes, rule numbers or process words in a product (the Bulletin purpose line prints section names, not codes; the Bigger Picture brief forbids process wording).
+    SIMPLE ANSWERS: "simple english line, at most two lines if complicated to explain"; "I didn't ask you to summarize" when he asks to repeat the questions: repeat the questions, one line each.
+    THE FUN CLIP: the opening "In today's fun corner"; "leave it as accepted... as long as he got booked another follow-up. it is not the topic." (the source says the bots booked a follow-up, not that he got the job).
+33. SOCIAL POSTING (Rafi, 15 Oct 2026, his words): "I want this session to be incharge of posting to all social medias"; "I want it to be eassy ...so when claude finishes its work. it autamticly post it"; "claude should have some sort of mcp to the app". Tool under study: Postiz (open source). Not built yet; setup and platforms still to be decided by Rafi.
+    (Mine, not yours: the wording around his quotes, and this reading: posting starts only after his approval stop of Part B, and the Headlines video is made on his PC.)
+34. RAFI'S WORDS OF 16 OCT 2026, ON STORIES THAT ALREADY RAN AT 7 OR MORE (rule 8; the wording around his quote is Claude's): about three stories the viral sweep left out because they ran at 7 or more on earlier days (Anthropic Q3 revenue, the states suing OpenAI, Windows for the Nvidia RTX Spark laptops), Rafi said: "keep them if they are meaningful updates." So a story that ran at 7 or more may come back when it is a meaningful update (new facts, not the same news again); Claude judges that story by story and says which and why. This answers the open question of lesson 195 for the viral rule. (Mine, not yours: this reading, and that skill step 1c and viral_sweep.py are not changed until Rafi says yes to the exact edit.)
+35. RAFI'S WORDS OF 16 OCT 2026, ON STORIES WE COULD NOT READ (rule 8; the wording around his quotes is Claude's): when a story has no readable copy, "note than should be 'access full article on the source website / source name / link'"; "for bulletin you need one paragraph ... searching for same article and write just one paragraph about the topic"; "you can have a quick search, and also get information from sources related to the item". So: first a quick search for the same story at another outlet and related sources, then one paragraph from what was read; only a story still not found ends with "Read the full article at <source name>." (the source name and link are printed under the story). Rafi saw both versions on the real Bulletin page and picked this one ("B"). The old line "Note: we could not open the original article ..." is not printed any more (rule 32). (Mine, not yours: this reading, and the skill text and the post-build step that apply it; build_products.py is not changed until Rafi says yes to the exact edit.)

## 2. docs/V1_TASKS.md: added or changed lines (new lessons and ADDED notes)

+304. (15 Oct, Part B, Rafi angry: "why would you add 'though he called it hypothetical'... this repeats all the time") THE USELESS TAIL. Cause found: rule 22 needs a why for every clip; for Huang there was none, so the writer filled the why slot with the speaker's own hedge ("why: it is a hypothetical, so it is a hedged threat"); the checker brief counted "their own stated reason" as a why; the rule "either no need for the end part" stood in the writer brief as words with no check. Fix (Rafi's yes 15 Oct): wording_headlines.md and check_headlines.md now say a hedge is one word, a speaker's own hedge is not a why, and the checker asks of every clip what the last part adds. A script check was tested on 22 past clips and rejected: it flags 14, including the approved 11 Oct model line, because the why is also a second part.
+305. (15 Oct, Part B) "FROM WASHINGTON" is allowed for politics (Rafi): check_headlines_rules.py B2d and B2e and brief line 27 changed. The rest of the 14 Oct rule (no places) stands.
+306. (15 Oct) CUSTOMER PRODUCTS SHOWED OUR PROCESS: the Bulletin purpose line printed codes (HEA, SOC, MOD, POL; lesson 150 had said fix it on 9 Oct and it was never built); the Bigger Picture printed "CLAUDE.md rule 17", "rule 5.5", "headline only", "unread", "window". Fixed in the products by hand and in build_products.py (names, not codes) and bigger_picture.md (no process wording). Open: the markets share sentence is still in the Full Report Bigger Picture (Rafi said yes to remove it; the helper was stopped when he interrupted); the About note still says "marked as headline only" (decision: keep).
+307. (15 Oct, Part A) TITLES: 22 named people lacked a title in the products; one Opus helper added them from the entries' facts or sources; Musk's title is "chief executive of SpaceX and Tesla" (no source yet shows his SpaceXSI title). Rule PEOPLE WITH THEIR POSITION was in the writer briefs but no check enforced it. Open: a check that fails a named person with no title.
+308. (15 Oct, Part B) CARDS UNCLEAR: nine card lines were cut so short that the links between facts were lost (the card format is 85 characters plus two sentences of 15 words, hedges kept, one writer pass). The checker tests facts and rules, not whether a stranger follows at once. Fixes applied by the writer after Rafi's yes.
+309. (15 Oct) THE 13 OCT RUN WAS NEVER SAVED: the 13 Oct chat waits on a Rafi answer and git is blocked there; Rafi must say yes in that chat. Open.
+310. (14 to 15 Oct, Rafi: "save a full description of all our trials ... so next time I, or you look at it we remember exactly what we tested") THE MODEL TEST: 72 blind helper runs (Haiku, Sonnet, Opus, Fable at different efforts) on real stories, saved in docs/model_test_2026-10-14/ (README, 1_TRIALS, 2_FINDINGS, 3_CONCLUSIONS, report.html, raw data). Lessons: max effort never helps (5 to 20 times the time); Haiku slips every time; an easy test (article handed over) hides the differences, the real job (fetch, blocked sites, credit chain, old news) shows them; low effort missed old news and credited copy sites (Unite.AI) instead of Reuters; every Opus level got the credit right; Fable writes best at about 5 times Sonnet's price; one slip in one story does not condemn a level; run the full grid on every test story (Rafi). Nothing changed yet; options and the decisions log in 3_CONCLUSIONS.md. CLAUDE.md MODEL POLICY now points there.
+311. (16 Oct, Part A run) THE NOT-READ NOTE WAS PROCESS WORDING IN A CUSTOMER PRODUCT, AND MOST OF THOSE STORIES COULD BE READ ELSEWHERE. build_products.py printed "Note: we could not open the original article; this entry relies on its headline" under 9 stories, and the About paragraph said "their websites could not be opened from our system", against CLAUDE.md rule 32 (no process words) while the skill Gotchas said "the PDF prints a note". Two rules clashed, I stopped (8a); Rafi asked why a story is not simply searched at another outlet and written as one paragraph. A search pass (3 Sonnet helpers, about 3 minutes) found 4 of the 9 at other outlets (BigGo and Investing.com for the FT and Bloomberg stories, Yahoo/Newsmax for Axios, NBC Boston), 1 in part, 4 not at all. Rafi's rule (CLAUDE.md 35): quick search plus related sources first, one paragraph from what was read; a story still not found ends "Read the full article at <source>."; he saw both versions on the real Bulletin page and picked that one. Prevention: the writers should do this search themselves before settling for a headline-only entry (a small step in the writer brief, scripts unchanged during a run); build_products.py and the About wording of the PDFs still print the old line and need Rafi's yes to change.
+312. (16 Oct) A RELAY PAGE IS NOT THE SOURCE. The searchers credited Yahoo News and Investing.com, which only rewrite Axios and Bloomberg; the Opus editor moved the credit to the first reporter and the link to the original (the readers can open it even where our proxy gets a 403). Same lesson as the CREDIT rule; a fresh search helper does not know it unless told.
+313. (16 Oct) A STORY ADDED OR REWRITTEN AFTER THE BIGGER PICTURE STARTS A CHAIN. Adding the Windows story pushed one score 5 story out of the fill that the Bigger Picture cited (C14-11); I set the fill to 111 instead of 110 so every cited story stayed. Rewriting 4 entries needed a recheck of the Bigger Picture facts that cite them (13 fixes: "scale not known" was no longer true). Do the late additions before the Bigger Picture, or recheck its citations every time.
+314. (16 Oct) VIRAL SWEEP MISSED A SAME-DAY REPEAT BY HEADLINE. "States sue AI giant OpenAI" (AP, 48 outlets) was yesterday's C13-01 at 8 under a different headline; the sweep's RAN BEFORE line did not show it, the curator flagged it. Check every viral cluster against the last day's pool by names, not only by title. Rafi's rule 34: a story that ran at 7 or more may return when it is a meaningful update; on 16 Oct none of the repeats qualified except the Windows story, which he chose to add.
+315. (16 Oct) TWO PART A WRITERS (Healthcare, Society) READ THE RULES ONCE, NOT BEFORE EACH ITEM, as rule 27 allows only for Part B. The Opus editors changed 43 entries afterwards. If Rafi wants Part A writers to read once too, he says so.
+316. (16 Oct) A SECOND-READ HELPER RESTORED SCORES WHEN THE STORY WAS FOUND (6 back to 7): the writer lowers a headline-only story by 1, so finding the text should restore the pool score; check that the new score matches the pool, not the lowered one (C16-05 was left at 2 against a pool 3).

## 3. Skills and briefs (scripts listed by name only)

.claude/skills/fill-categories-scan-part-a/SKILL.md                   | 3 +++
 .claude/skills/fill-categories-scan-part-a/briefs/bigger_picture.md   | 2 +-
 .claude/skills/fill-categories-scan-part-a/scripts/build_products.py  | 4 ++--
 .claude/skills/fill-category-scan-part-b/briefs/check_headlines.md    | 1 +
 .claude/skills/fill-category-scan-part-b/briefs/wording_headlines.md  | 3 ++-
 .../skills/fill-category-scan-part-b/scripts/check_headlines_rules.py | 3 ++-
 6 files changed, 11 insertions(+), 5 deletions(-)

diff --git a/.claude/skills/fill-categories-scan-part-a/SKILL.md b/.claude/skills/fill-categories-scan-part-a/SKILL.md
index aafc6c6..1eaa88b 100644
--- a/.claude/skills/fill-categories-scan-part-a/SKILL.md
+++ b/.claude/skills/fill-categories-scan-part-a/SKILL.md
@@ -215,2 +215,5 @@ D-M-YY is the file-name date, e.g. 3-10-26.
 
+### 11b. Not-found note (Rafi, 16 Oct 2026, CLAUDE.md rule 35; skill text only, build_products.py is unchanged until he says yes)
+After the final build_products.py and before build_pdf.py, in both `products/report_pdf.json` and `products/bulletin_pdf.json`, every paragraph that starts with "Note: we could not open" is replaced by "Read the full article at <the story's source>." (the source name and link print under the story anyway). Before that, a story with no readable copy gets one quick search for the same story at another outlet and related sources, and one paragraph from what was read (a writer, then an editor check, then the Bigger Picture facts that cite it are rechecked). Keep the before copy as `*_old.json`.
+
 ### 12. Second check (a different angle)

## 4. Drive rule files (W/rules against runs/2026-10-15/rules)

no change
