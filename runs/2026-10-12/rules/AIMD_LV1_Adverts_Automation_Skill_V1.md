---
name: aimd-lv1-adverts-automation-skill-v1
description: Run AI News Desk LV1 daily adverts from the dated Full Report through cards, Headlines prompts, ComfyUI JSON and authorized generation. Use for Rafael's AIND LV1 adverts automation or one-command daily run; preserve current project masters and approval boundaries.
---

# AIMD_LV1_Adverts_Automation_Skill_V1

Version 1, created 13 September 2026 at Rafael's request. This is an execution skill, not a replacement for AIND's rules, a scheduler, or permission to alter either LV1 or LV2. The requested human-readable file keeps Rafael's spelling. The installable skill identifier uses Codex-compatible hyphens.

25 Sep 2026 (Rafael: one source for every rule, no duplicates): the Headlines rules were removed from this skill and now live only in Headlines_Master_Rules_Structure.txt (formerly "daily headlines prompt blueprint V9.2.txt"); this skill points to it. Files are found by name in their folder, never by file ID, because a re-upload changes the ID. The previous text is kept as AIMD_LV1_Adverts_Automation_Skill_V1_old.md.

## Invocation and scope

Suggested command: `Use $aimd-lv1-adverts-automation-skill-v1 for today's AIND LV1 adverts. Run the agreed workflow.`

Resolve the edition in Asia/Jerusalem. Follow the caller's authorized endpoint: cards, prompt review, JSON, Comfy generation, or complete final-video delivery. A one-command invocation starts the workflow and resumes from verified artifacts. It does not silently waive an explicit copy-review checkpoint, authorize publication, install models, change shared workflows, or activate a daily schedule. If the caller explicitly authorizes automatic selection and generation for that run, proceed within that authorization. Otherwise show the concrete cards/Headlines wording before JSON and generation, as Rafael requested in this workflow. Do not ask again for an action already explicitly approved.

Treat new speech or messages as steering; pause when Rafael says to stop. Use concise numbered updates and ask only the specific unresolved question. Do not delegate unless requested. Never delete; preserve existing filenames and versions. Do not edit project rules, source reports, shared renderers, permanent references, or earlier outputs as part of a daily run.


## One-command reusable sequence for tomorrow

1. Load governing sources once: Cards_Master_Rules_Structure, AI News Desk — STORAGE & FILE ROUTING STANDARD, AIND_Publishing_QA, and the current Decision Log.
2. Read one requested edition's Full Report, Bulletin, daily-pool, and current status artifact.
3. Build cards in one pass with the count and naming sequence specified by Cards_Master_Rules_Structure.txt.
4. Create or load the approved slot-to-story order and generate Headlines JSON from Headlines_Master_Rules_Structure.txt.
5. Queue only clips that are missing or failed. Never queue the full pack twice.
6. For each queued clip, generate with the 544x960 base and the 1088x1920 upscale both on, then verify speech (rules file, September 13 section).
7. Check clip identity, full-resolution decode, transcript and lip sync before assembly. Classify speech issues under Rafael's current instruction in MASTER PROJECT MEMORY: apply approved minor repairs during editing/stitching and identify major errors for regeneration.
8. Save all outputs directly to designated folders and run `scripts/validate_delivery.py` for storage integrity.
9. Mark only local workflow status; do not mark publication-ready unless posting permission and publishing QA are explicitly approved.
## Focused authority check

Use the Google Drive skill and verify the account is `tlvsc.claude.agent@gmail.com` before Drive operations. Follow AI News Desk — MASTER PROJECT MEMORY, “ONE SOURCE OF TRUTH”. Resolve each current authority by its exact approved filename inside its designated live folder. Cached IDs and installed files are locators or execution copies, not proof of current authority. Verify name, parent folder and modification time; an ID that now names an _old or SUPERSEDED file must not supply current rules. Read the current applicable contents, retain IDs, modification times and hashes in the existing run record, and refresh after an announced or detected change before the affected production step. Avoid broad archive or unrelated V2 scans. Particular local-backup access still requires Rafael's explicit permission.

Precedence: newest applicable Rafael instruction; current Decision Log; current product master. AI News Desk — Project Task List holds current tasks and next steps. Consult historical handoffs only when Rafael explicitly asks. Memory, registries and implementation guides are locators, not overriding authorities. Check relevant current decisions and product rules; older blueprint versions are history only.

| Needed for | Current source and Drive ID |
|---|---|
| Card structure and editorial/layout rules | `Cards_Master_Rules_Structure.txt`, by name in Card Master Permanent Assets |
| Headlines rules, format and JSON | `Headlines_Master_Rules_Structure.txt`, by exact name in Blueprint_Library / Headlines blueprint; never a file whose name ends in _old or starts with SUPERSEDED. It is complete; older blueprint versions are history only. |
| Headlines generation prompt | `Headlines_prompt_for_comfy_json.txt`, in Blueprint_Library / Headlines blueprint / Headlines Master Permanent Assets / Headlines_prompt_for_comfy_json. The Prompt Vault copy `Headlines_prompt_for_comfy_json_backup.txt` is a backup, never the working copy. |
| Headlines ComfyUI template | `Aind_headlines_comfy_Master_workflow_template.json`, by name in Blueprint_Library / Headlines blueprint / Headlines Master Permanent Assets / comfy_template |
| Validator | `AIMD_LV1_Adverts_Automation_Skill_V1_validate_delivery.py`, by name in Prompt Library/prompts |
| Plain language | `Article_phrasing_instructions_AIND_V1`, by exact name in Prompt Library/prompts |
| Storage before saving to Drive | `AI News Desk — STORAGE & FILE ROUTING STANDARD`, `1ModaHnDZvjn5SxEvwRXwxlrhoXXKzDq-Mhs0NS0eVms` |
| Relevant current decisions | `1LJqFghkIc_dBaqWK2-XiAfUjEZLXxLwmSwwXc6O0S0Q` |
| Production/editorial QA | `AIND_Publishing_QA.md`, `1zm5nQPlPj6zdQYXgh8ONfBxSOMhpEtoc` |
| Daily folder root | `1nzOWXclWAExDQ6WqQ2C9DmSkM3rrqLYx` |
| Card permanent assets | `15pESFnyFwQHUbJg6MAYG3f9zlTLZJQUW` |
| Headlines permanent assets | `1ZSGR9LRdyRY1jS4egew_8RyOsBLyNkDH` |
| Shared report prompts, only if upstream research is requested | `1uzjcUMuZ7_1B_CEM3CIkWh_O0Sk45PBn` |

If an authoritative file is unavailable or genuinely conflicts with another current instruction, show the exact conflict. Complete independent preparation, but do not spend GPU on the affected item or silently decide a permanent rule. Already-resolved older text is not a new conflict.

## Daily source and selection

1. Locate only the requested edition's Full Report, Bulletin, run status and `daily-pool.md`/pool ledger. Record edition date, coverage window, source IDs and item IDs. Bulletin follows Bulletin_V1_Rules_Structure.txt; it is separate from the Full Report and Headlines, and its READY label is not proof that today's derivative passed QA.
2. Cards and Headlines draw from the Full Report. Web checks validate selected claims/dates and identify omissions. Do not insert web-only news or silently repair the upstream report. Select once, maintain a source-to-card-to-clip mapping, and revise only for a discovered problem or user feedback.
3. Prioritize public consequence, global importance, novelty, listener interest and reliable evidence. Scores guide ranking; Rafael's editorial judgment matters. Preserve all criticals. Do not fill slots with weak stories merely to reach a count. A big-name story must still have a clear event and consequence.
4. Verify original article date and underlying event date separately. An item reappearing in an aggregator today does not make it fresh. Check selected sources before expensive rendering. Preserve uncertainty and attribution. An advocacy claim is not scientific proof; a proposed medical system is not an approved working treatment. Keep biological-misuse coverage high-level and preserve the disclosed limits on intent and identities.
5. Record source limitations beside the affected item. Follow actual editorial QA; never fabricate original-source inspection, human declarations, approval, or a PASS. Continue unaffected work. Approval to render a private review does not confer publication approval.

## Cards

PROVISIONAL PRESENTER APPROVAL - RAFAEL, 13 SEPTEMBER 2026
Rafael approved the original-face preview "for now" for future card runs. This approves the presenter-face treatment; it does not replace the entire established cover layout or authorize publication.
Use the original Studio_Cover.png presenter image as the facial source, preserved in Card Master Permanent Assets: 1PpIs2czZxHdDNSTXlaMtgGR6tdI64W_Y. Source SHA256: 22127b7e7fd41699e7040bdd32bfea2fc81c2895a364bcec5e5a4d972c489361.
Approved visual example: cards_13-9-26_I01_VL1_presenter_preview.png, Drive 1sizbDjBLJB_7K-3uRzZ4S_xI2zpCjdIs, SHA256 61f13d586e2aa1cc7a62041a41213a1a0176d850595439ab1a3dd1df6769fa0d. Pixel verification record: 16QEoQnY7okJhE-Fjldc2wCw4hS0PrJrM.
Reuse the original facial pixels directly. Do not generatively edit, redraw, beautify or reshape the face. Preserve natural aspect ratio; if resizing is necessary, use the same scale for width and height. At unchanged scale compare the head pixels exactly; when proportionally resampling, compare against the same resampled source, not a newly generated likeness. Keep the face out of any generated date/text/layout edit.
The approved preview copied the source head rectangle (476,770)-(603,934) to (476,700)-(603,864) at 1:1 scale; all pixels in that head rectangle match exactly. Only a small surrounding patch edge was blended. These coordinates document this example, not a forced placement for other layouts.
The AI-edited face preview exec-8fab3a66-51d8-46d4-b0bb-0c0aacdf7a9d.png is not the approved source. Earlier notes calling the presenter treatment unapproved are superseded by this provisional approval. Today's active 15 cards and combined image have not been replaced under this future-run instruction.


Use the current Cards Master and approved renderer/assets. `AIND_card_execution_master.md` and package guides are not the governing structure. Do not patch a shared renderer during a daily run.

Default order: cover; all score-ten criticals first; remaining category cards; one More in the full report; The Bigger Picture; approved closing. Criticals spend their category slots.

Category order, slots and card count follow Cards_Master_Rules_Structure.txt; record the selection within the current set.

Choose the strongest eligible story within each category. A robotics item describes a robot/autonomous machine doing something. Sensors, funding, policy or a school robotics theme do not automatically satisfy that category. Do not equate an AI company's proposal with government action. Explain omissions and exceptions to Rafael; do not relabel weak items to make a coverage table pass. Big-release-first priority was not permanently approved as of this skill's creation.

Write a complete, spoken-sentence headline. Two body sentences: the event, then why it matters or an honest doubt. Explain unfamiliar companies briefly. Lead non-market news with the deed, not the money. Prefer concrete words that a first-time listener understands. Preserve meaningful detail and factual certainty. Avoid hype, analyst jargon, dramatic labels and vague rhetorical questions. Read the copy aloud mentally before layout. Lock approved wording; do not rewrite it just to fit a box.

Teaser: three or four report items that have no story card. The Bigger Picture is clearly identified desk analysis; separate it from reported facts. Preserve the exact current approved closing and live sales/link restrictions.

Render the current cards with count governed by Cards_Master_Rules_Structure.txt, preserving 1080x1920 PNG, the existing Instagram-safe content area and one combined image. Do not export square crops, alternate ratios or a second deliverable version unless Rafael explicitly requests them. Create combined-image thumbnails in memory; they are not separate card files. Preserve earlier material in cards/supportive files/archive. Verify decoded dimensions, text bounds and appearance across all current cards. Inspect the contact sheet and any crowded card. Technical render success is separate from editorial acceptance. Do not reuse September 13's temporary square-cover-in-portrait treatment as a permanent rule; approved-cover integration was still unresolved.

## Headlines (every rule lives in the rules file)

Every Headlines rule lives only in `Headlines_Master_Rules_Structure.txt`, found by name in Blueprint_Library / Headlines blueprint. This skill gives the procedure and points to the rules file; it does not repeat the rules. If this skill and the rules file ever differ, follow the rules file and report the difference to Rafael.

1. Slots and selection: rules file Section A.
2. Words, spoken introductions and box timing: rules file Section B, items 1, 1a, 2, 2a and 3. Count syllables word by word; never guess or copy boxes from an earlier edition.
2a. Required editorial check: before presenting a Headlines item as ready, apply the SOURCE-TO-SCRIPT MEANING CHECK in `Article_phrasing_instructions_AIND_V1`, Section 1A, found by exact name in Prompt Library/prompts. Keep the source comparison and result in the item's existing story pack or editorial QA record. A failed or unchecked item remains a draft and must not enter the approved narration or generation. Passing JSON validation does not satisfy this check.
3. Review before the JSON: show Rafael the complete sequence, including the opening, every story with its introduction, the fun item, the teaser, The Bigger Picture and the ending, unless he authorized automatic selection for this run. Once approved, the narration is locked in the prompt, the JSON and the subtitle source.
4. Prompt: `Headlines_prompt_for_comfy_json.txt` only (rules file Section B2), with its two <article content> placeholders filled, plus a pronunciation cue only as the rules file's 15 September section item 1 says.
5. JSON: copy `Aind_headlines_comfy_Master_workflow_template.json` from the comfy_template folder into a new dated file and fill it by rules file Section C. Never change the template during a daily run.
6. Validation pack: the fill also writes `extra.aind_headlines`: edition; slots, each with slot, kind, title, story_id or story_ids, narration, intro, syllable_audit (word and syllables), estimated_syllables, seconds and generation_prompt; the two reviewed references with node_id, filename, role (boundary_hands_on_table, secondary_gesture) and visually_verified; card_story_ids; card_teaser_story_ids; syllables_per_second 4.4; timing_formula "syllables / 4.4"; timing_decision_confirmed true; boundary_hold_duration_is_flexible true; unresolved_issues empty. Then run `scripts/validate_delivery.py --headlines <workflow.json> --prompt "<local copy of Headlines_prompt_for_comfy_json.txt>" --comfy-url http://127.0.0.1:<verified-port>`. A failure blocks readiness and queueing. The validator checks structure; it does not prove facts, approval, correct speech or picture.
7. Generation, upscale and speech check: the rules file's September 13 section (upscale always on), 15 September section, 17 September continuity amendment and 19 September lessons.
8. Before assembly, compare the actual saved clips with today's unchanged workflow using `python -B scripts/validate_delivery.py --headlines <workflow.json> --clips-dir <explicitly approved Comfy output folder>`. Supply existing `--ffprobe` and `--ffmpeg` executable paths if needed. The checker reads files only and prints expected clip IDs and resolutions, missing outputs, invalid files and ambiguous duplicate attempts; it writes no file and queues nothing. Check provenance against the existing source manifest and generation record. A matching total count or successful decode does not prove the correct speech, story or generation attempt.
9. Assembly: rules file Sections D, D1, D2 and G7. Command: `python -B scripts/aind_v1_headline_script.py run --edition YYYY-MM-DD` with the dated `Headlines_D-M-YY_source_manifest.json`.

Inspect the actual image pixels and verify their filenames against the live backend. Picture 1 defines the hands-resting-together-on-the-table boundary pose; Picture 2 is the reviewed secondary gesture/fists pose. Never invent dated input filenames. Both images must belong to the same approved studio; an existing filename alone is not visual approval. H3 reference inputs are not first/last-frame constraints. Explicitly prompt the same settled hands on the table, face straight toward the camera, eyes directly into the lens, closed mouth, framing and logo state at both ends of every generated clip, then check the actual base clip.

Record teaser source IDs and compare them against the supplied More in the full report card and story-card IDs; never duplicate a story card in the teaser. Preserve reported/preliminary attribution, distinguish annual run rate from realized revenue, lead science with the result, and compare repeated facts between stories and the Bigger Picture.

### Comfy backend and queue discipline

6. Check the existing local backend, `/system_stats`, `/object_info`, `/queue`, and targeted history. App open is not proof the backend runs. If the requested generation needs startup, locate the existing launcher/settings and reuse them without installation, update or persistent configuration changes. Launch background helpers hidden. Verify the actual runtime attention setting from startup output; a JSON cannot prove Sage is enabled. Respect other users of the shared GPU; never interrupt or clear unrelated jobs.
7. Check reference files, output-name collisions, model availability and schema compatibility before queueing. Validate the graph and fixed settings. Record the exact UI/API SHA-256, edition, clip IDs, client/request identity and an attempt record BEFORE POST. Preserve prompt IDs and responses. On an uncertain result, inspect queue/history before retrying. Never enqueue the whole pack twice. Retry only the failed/missing authorized clip, and preserve the failed attempt's evidence.
8. Reuse verified approved assets instead of regenerating them. Opening reuse needs matching identity/wording and a separately dated overlay. Ending reuse needs matching current approved words; an old clip saying “brief” is not an acceptable substitute. Generate an authorized new ending only if no verified matching asset exists. Unresolved wording conflicts must be surfaced before the affected generation.
9. Monitor only the submitted prompt IDs. Poll with reasonable backoff, not rapid full-history scans. Distinguish queued, running, failed, generated, decoded, speech-verified and assembled. A prompt acceptance or empty queue is not a completed video. Preserve clip paths and hashes; intermediate clips stay local. Do not claim completion until direct evidence supports it.

## Storage and finish

CURRENT FILENAME RULE - RAFAEL, 13 SEPTEMBER 2026
For numbered production media, use this order: product_short-date_media-number_workflow-lane.ext.
For every current and future individual card: cards_D-M-YY_I01_VL1.png through the edition's final image number; use VL2 instead of VL1 only when Lane 2 actually created it. Exact September 13 Lane 1 example: cards_13-9-26_I01_VL1.png.
Use uppercase I for images and C for numbered video clips, with two-digit sequence numbers. Keep the approved product name first, the short date second, media number third, and VL1 or VL2 fourth. Lane means the producing workflow, not the revision of the copy. Record producing_lane in the product manifest and verify it from run provenance.
Do not prefix daily media filenames with AIND. Do not append version_2, another revision suffix, or repeat the word version. Revision history remains in the manifest and archive; it is not another deliverable filename suffix.
Apply this rule to current card filenames and future numbered-media saves. Preserve the images, printed numbers, sequence, existing Drive IDs, folders and original provenance. Do not enlarge printed numbers or create a ZIP for this request. Drive Name ascending displays individual cards in sequence; do not claim control of phone download completion or Instagram ordering.
The current 15 September 13 cards were produced in Lane 1, including the copy revision formerly called version 2, so all carry VL1. An existing current card name may be changed to this exact authorized format despite older generic filename-preservation clauses. Preserve unrelated original/archive/permanent-asset names; do not invent image or clip numbers for unnumbered support files or the combined image.


CURRENT APPROVED STORAGE AND CARD DELIVERY
Follow AI News Desk — STORAGE & FILE ROUTING STANDARD for daily destinations, supportive files, manifests, saving and delivery verification; follow Cards_Master_Rules_Structure.txt for card count, format and combined-image requirements.

The helper is preserved in Drive as AIMD_LV1_Adverts_Automation_Skill_V1_validate_delivery.py, found by name in Prompt Library/prompts; install it as scripts/validate_delivery.py beside this skill.

Use `scripts/validate_delivery.py --manifest <existing dated manifest> --inventory <fresh recursive Drive listing JSON> --cards-dir <current local cards folder>` before declaring delivery complete. The inventory is keyed by folder ID and contains actual list_folder entries. Validate the complete ordered current card-ID list against the approved selection, one combined image, master-format PNG dimensions and hashes, no extra current images, product folders at the date root, and every recorded file’s parent. Missing or extra files fail validation. This is a storage check, not publishing clearance.

Do not execute the archived September 13 dual-format render helpers for a new edition. Configure the selected renderer for only the approved single output format before generation. After a correction, replace the manifest’s explicit current selection and archive superseded outputs; never tell a posting agent to choose the newest-looking file.

Drive is the source of truth for the AIND project (Rafael, 25 Sep 2026): resolve the exact current skill and helper filenames in Prompt Library/prompts, then refresh the existing installed SKILL.md and scripts/validate_delivery.py from those Drive copies at the start of each run. Never edit an installed copy alone. Record source identities and revisions in the existing approved run record; decisions belong in the existing Decision Log and unfinished tasks in the existing Project Task List. Do not create a handoff or another tracking file unless requested. The archive scheduler remains paused. Live automation bindings are verified separately; a saved rule is not proof of an unattended run.

## September 13 learning, not permanent editorial rules

- The approved proposal used report items 1, 2, 3, 29, 31, 36 and 45, followed by teaser 17/33/27 and desk analysis. It omitted weak fun and the older sensor item. Seven main stories were a daily decision, not a new mandatory structure. The selection did not establish full literal robotics/law/research category coverage.
- Ten-second story boxes plus ten-second teaser and twelve-second analysis total 92 seconds, not a measured 88–90. Speech needs rendered verification.
- Source dates can invalidate an approved-looking item. The final Bloomberg miners check found a September 9 original outside the edition's window; explicit background-context permission was requested before spending GPU on that clip. Do not carry this exception into later editions.
- The current run's approval selected the exact ending proposed to Rafael: “Those were today’s headlines in ninety seconds. For more detailed coverage, read our daily news cards. Thank you for tuning in, and we’ll see you tomorrow.” This does not rewrite the shared Decision Log or resolve all future ending versions.
- The JSON build preserved fixed settings and found/synchronized stale named metadata. Comfy startup directly verified Sage attention on the RTX 3090. These are observations from this run; recheck cheap live state tomorrow.
- The September 13 per-run Python helpers contain fixed dates and copy. They are evidence, not generic tomorrow-run scripts. Do not execute them for a new edition or clone yesterday's narrative blindly.



The 15 September pronunciation, company names, screen text and reusable ending rules and the 17 September continuity rules live in the rules file (see Headlines above). They are no longer repeated here.

## 19 September 2026 - Headlines mistakes, fixes and prevention

Documented at Rafael's request. Detailed evidence and per-clip status live in `daily_data_generated/2026-09-19/Headlines/supportive files/headlines_19-9-26_VL1_1.json`, under `extra.aind_run.mistakes_and_fixes`. The following are dated findings, not claims that every clip was fixed.

1. **Unused pronunciation cues contaminated generation.** Every prompt included Anthropic and NVIDIA guidance even when neither brand was spoken. C07 showed an NVIDIA logo instead of protein imagery; C08 added NVIDIA-related speech. Removing unused cues corrected those symptoms with the same script, seed, timing, voice and references. Keep only cues for brands actually in that clip's narration; the validator rejects unused cues. This did not solve every speech defect.
2. **Copied values could disagree.** The supplied workflow had six visible base steps and eight in hidden metadata. A saved API snapshot can also retain an old prompt after the UI changes. Synchronize the structured pack, visible values, named values and current API graph. The validator now checks included API prompts, durations, output names, references, voice, seeds and base scheduler/sampler values against the UI. Keep old graphs explicitly historical; never submit `original_api_graph` as current.
3. **Timing must come from the established formula.** Rules file Section B item 1a records earlier words-per-second and copied-box mistakes. Count the whole spoken line, including the introduction, and use rules file Section B item 1a (syllables / 4.4, no rounding up, no added time). The formula used on September 19 was later replaced by Rafael. Hands-on-table and face-to-camera holds are flexible; do not add hold time. The registered frame grid can make decoded duration slightly longer than the box.
4. **Correct written dialogue did not ensure correct audio.** The corrective pass still left C04 with extra ending speech, C06 with repeated words, and C09 with extra ending speech. Check the complete unprompted transcription, including middles and tails; recheck suspect intervals. Business-name and currency transcription variants needed verification, not blind rejection or blind acceptance. Report failed clips to Rafael (rules file, September 13 section; the upscale is always on since 25 Sep 2026). The proposed stricter speech instruction remained untested and unapplied at this documentation update.
5. **Backend shutdown lost cached generation data.** The exit cause was not established; do not label it an out-of-memory failure. Discover the actual process/port and reuse the existing launch settings. A saved MP4 does not contain the base latent needed by the registered upscale. Preserve passing full-resolution outputs; recover only authorized missing outputs. Where possible, complete a passing base's upscale while that latent remains cached.
6. **A matching filename was not proof of a finished output.** C03 had an incomplete 48-byte upscale; an older C05 full-resolution file belonged to another workflow. Use the exact submitted prompt's history, file path, full decode and hash. Preserve originals and failed attempts; never choose a file solely because its name or timestamp looks right.
7. **Reference prompts are not exact endpoint conditioning.** Picture 1 is the table-hands boundary reference; Picture 2 is the secondary fists/gesture reference. Check actual first/last frames at both base and upscale. Some upscaled opening mouths appeared slightly parted despite good sampled hand/face poses. Report those limits; sampled poses do not certify closed-mouth holds, lip-sync or fluent stitching.
8. **Keep status and permission precise.** This pass produced six accepted full-resolution clips and held three for speech; it was not a finished stitched delivery. Current status must come from the run record, not this dated count. Separate applied fixes, verified effects, open defects and proposed tests. Reuse existing approvals within scope; a documentation request is not evidence that an untested fix succeeded. Do not repeat identical failed generations or silently change locked settings.
