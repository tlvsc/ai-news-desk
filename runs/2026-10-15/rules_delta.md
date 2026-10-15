# Rules delta for edition 2026-10-15: everything that changed since the rules check of 2026-10-14
Base: commit 75a5d62 (the save of runs/2026-10-14/rules_check.md); now: d7d1153.
Read with W/rules_check_previous.md. Lines starting with + are new, - are gone.

## 1. CLAUDE.md

diff --git a/CLAUDE.md b/CLAUDE.md
index 321019d..0612a85 100644
--- a/CLAUDE.md
+++ b/CLAUDE.md
@@ -317 +317,2 @@ not about which project it is.
     FUN CLIP CHOICE: "not necessary. you give me the concept and ill tell you if its funny. but I want to get to a point you understand whats funny and you choose yourself. full autonomous chain!" (13 Oct 2026). For now Claude gives him the fun concept and he says if it is funny; the goal is that Claude chooses the fun clip alone, with no stop. This replaces the "at most three finished lines" idea of lesson 236.
+30. CRITICALS ALWAYS ON TOP (Rafi, 14 Oct 2026, his words: "You have strict rules that criticals always go on top. Everything that's rated 10 is always broadcast. It pushes everything down."; "You add it to the fucking script so this doesn't happen again. If there's critical, they go above and push everything down."). A story rated 10 is the first card and the first Headlines clip, above Politics, and pushes the rest down. pick_gate.py G11b was changed the same day so a Politics clip may sit behind critical clips. (Mine, not yours: the wording around his quotes.)

## 2. docs/V1_TASKS.md: added or changed lines (new lessons and ADDED notes)

+D3. Hard names as spoken: "N-vidia", "anthro-pic" (changed 14 Oct 2026, Rafi: an-thropic is pronounced wrong), "Kawa saki" (one gap; "Ka-wa-sa-ki" came out "Kavanua Saki").
+296. (14 Oct, Part B, Rafi: "what happened or changed that these mistakes started happening?") Causes found in the record: (1) place openings ("From Beijing" 10 Oct, "From Iran" 12 Oct, "From the Netherlands" 14 Oct) were never blocked: the check only counted words, the checker passed them; (2) the number rule said only "spell numbers as words", never "use the exact figure", so "about a third" for 34% passed every check; (3) since 12 Oct the writers run on Opus normal effort and read one pack once (rule 27) and since 13 Oct the checkers read one pack (chain fix), 14 Oct was the first run on both; not proven to be the cause; (4) the main chat ran on Haiku and passed checker fixes on without checking them. Guards added 14 Oct: check_headlines_rules.py B2d fails an opening with "from"; check_wording.py fails loose phrases (about a third, hundreds of, far more...); the briefs and both checker briefs say so. Open: three delivered card lines fail the new check (card 11 "far more", teaser "Hundreds of" and "far more").
+297. (14 Oct, Part B, Rafi: "make sure these mistakes, or any lesson we have learned, do not repeat") THE FINAL AUDIT: scripts/final_audit.py (Part B step 6b) runs every check, prints every line and lists lines changed since the last send. Mistakes of 14 Oct it exists for: changing approved wording without asking ("worms"); loose figures ("about a third", "next two years"); openings that are not categories ("From the Netherlands", "In driverless cars", "On your phone"); a checker's fix passed on without checking it against the rules (15 words, 5 word opening); answering a question with an action; sending a file late when Rafi asked for it. Also found: Rafi's rules were sentences nobody turned into script checks (enforcement_gaps.md in the run folder lists 18 rules checked by nothing). Open for Rafi: build the other gaps, and the 8 clashes the audit found.
+298. (15 Oct, Part A) FOUR DAY REPEAT LIST NEEDS A SECOND COLLECT: combine_pools.py writes yesterday_pool.csv but collect.py builds yesterday_pool_titles.txt, so the first collect with only yesterday gave 259 titles instead of 976. Fix for the skill: run collect.py after combine_pools, or run combine_pools first. Cost on 15 Oct: one extra collect and a changed viral cluster order (the Huang cluster fell below 20 outlets).
+299. (15 Oct, Part A) THE 13 OCT POOL IS NOWHERE: no runs/2026-10-13 in the repo and no AIND_Pool_2026-10-13 on Drive (only ChatGPT-V1 files). The repeat list on 15 Oct used 10, 11, 12 and 14 Oct. 13 Oct stories may have repeated. Open: save the 13 Oct run, or accept the gap.
+300. (15 Oct, Part A) VIRAL CHECK FALSE FAIL: viral_sweep.py check reported Harmonic Security missing (pool C06-10 at 5) while it was in the pool as C12-01 at 7; the cluster shares a Google link with the Labelbox story. Handled by listing the cluster in viral_exclude.json with the reason. Also: a drop by item id must be read from the pool just built, never from the viral check line (I dropped Labelbox by mistake once and had to rebuild).
+301. (15 Oct, Part A) EMPTY BULLETIN SECTION, EXACTLY 2: Models and tools had nothing at 7 and up. The expanded search (Asia, Europe, Middle East) found nothing. --bulletin-min-cat MOD=6 gives every 6 (5 stories, not exactly 2), so the section was trimmed by hand to 2 after the final build, in bulletin_pdf.json and the markdown (originals kept as _old). Open: build_products.py needs a per category "exactly N" fill.
+302. (15 Oct, Part A) FILL DRIFT AGAIN: after the editors, the 14 day check and holds moved the report, 9 score 5 fill stories had no editor read. Fixed with two small Opus editors (C for 8 items, D for 1) made from edit_A.txt. Open: the skill should say to build the fill after the holds and to make an editor C for new fill ids by default.
+303. (15 Oct, Part A) REPORT SIZE: the Bigger Picture Full Report version came out at about 12,300 words (3 Oct: much shorter). Rafi has only ruled the Bulletin version (300 to 500). Open for Rafi: a word limit for the Full Report version.

## 3. Skills and briefs (scripts listed by name only)

.claude/skills/fill-category-scan-part-b/SKILL.md  |     9 +-
 .../Aind_headlines_comfy_template_13slots.json     |     8 +-
 ..._comfy_template_13slots_old_hologram_first.json | 18318 +++++++++++++++++++
 .../assets/headlines_model_lines.md                |     2 +-
 .../assets/pack_base.json                          |     2 +-
 .../briefs/check_cards.md                          |     2 +
 .../briefs/check_headlines.md                      |     4 +
 .../briefs/rules_check_headlines.md                |     2 +-
 .../briefs/wording_common.md                       |     2 +
 .../briefs/wording_common_before_exact_old.md.txt  |    23 +
 .../briefs/wording_headlines.md                    |     4 +-
 .../pick_gate_before_critical_old.py.txt           |   192 +
 .../scripts/check_headlines_rules.py               |    28 +-
 .../scripts/check_wording.py                       |     5 +-
 .../fill-category-scan-part-b/scripts/common_b.py  |     7 +
 .../scripts/fill_headlines.py                      |     2 +-
 .../scripts/final_audit.py                         |    78 +
 .../fill-category-scan-part-b/scripts/pick_gate.py |    10 +-
 18 files changed, 18680 insertions(+), 18 deletions(-)

diff --git a/.claude/skills/fill-category-scan-part-b/SKILL.md b/.claude/skills/fill-category-scan-part-b/SKILL.md
index 38cfb6f..558ba61 100644
--- a/.claude/skills/fill-category-scan-part-b/SKILL.md
+++ b/.claude/skills/fill-category-scan-part-b/SKILL.md
@@ -51,3 +51,3 @@ helpers run, a lean main chat (never read the lessons file, a pack or a rules fi
 4. The Headlines template is in the skill: `$B/assets/Aind_headlines_comfy_template_13slots.json` (13 slots, the
-   29 Sep reference pair, Spectrum on; md5 bbbed6ed8496ee80f04288468f597aa5). The voice sample is NOT needed here:
+   29 Sep reference pair, Spectrum on; md5 235ede6a86c66fc1d38d7614f079d548). The voice sample is NOT needed here:
    the JSON only names AIND_anchor_voice_sample_4s.wav, which Rafi keeps in ComfyUI/input on his PC.
@@ -149,2 +149,9 @@ The fill refuses to overwrite: rename an earlier JSON `_old` first. C01 and C13
 
+### 6b. FINAL AUDIT before ANYTHING goes to Rafi (Rafi, 14 Oct 2026: "make sure these mistakes, or any lesson we have learned, do not repeat")
+```
+python3 $S/final_audit.py --workdir $W            # before every send of cards, JSON or lines
+python3 $S/final_audit.py --workdir $W --mark-sent    # right after sending
+```
+It runs every wording, rules and JSON check, prints every spoken line and card line, and lists each line that CHANGED since the last send. Send nothing while it prints a FAIL. Change a line Rafi has already seen only when he asked for it. Read the printed lines yourself against his rules (openings are the story's category, exact figures, a position for every person, A I and anthro-pic spellings) before you send. When Rafi asks for the JSON or a file, send it at once, then fix the rest.
+
 ### 7. STOP: Rafi's approval
diff --git a/.claude/skills/fill-category-scan-part-b/assets/headlines_model_lines.md b/.claude/skills/fill-category-scan-part-b/assets/headlines_model_lines.md
index f02b5fd..e36113a 100644
--- a/.claude/skills/fill-category-scan-part-b/assets/headlines_model_lines.md
+++ b/.claude/skills/fill-category-scan-part-b/assets/headlines_model_lines.md
@@ -15,3 +15,3 @@ The why is about whoever the story is about: a company story gets the company's
 If nothing adds weight, end after the action, or add the one fact that is the punch ("and ...").
-Spoken spelling stays: A I spaced, N-vidia and an-thropic cues, numbers as words.
+Spoken spelling stays: A I spaced, N-vidia and anthro-pic cues, numbers as words.

## 4. Drive rule files (W/rules against runs/2026-10-14/rules)

no change
