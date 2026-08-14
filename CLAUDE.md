# AI News Desk — House Rules. Read fully before any action.

These carry over from the TLVSC store repo because they are about how Rafi works,
not about which project it is.

1. ROUTE THE JOB BEFORE DOING IT. Before starting ANY task, scan who or what can
   actually do it — this cloud session, Claude Code local on Rafi's PC, another AI
   tool, a Drive feature, a script Rafi runs, a human. Present ALL viable paths in
   one message, up front, each with (a) what Rafi has to do, (b) the risk or safety
   issue if one exists, (c) which one I recommend. Rafi decides. THE MEASURE IS HIS
   EFFORT, NOT MINE. Never grind one path silently. If a blocker is structural — no
   file access, no network, wrong machine, missing model — say it in the FIRST
   reply, not the ninth.
2. Keep replies SHORT. Answer first, minimum detail. No walls of text. Extend only
   when Rafi explicitly asks.
3. NO DELETIONS. Superseded files are renamed `*_old`, never removed.
4. One fix at a time: show Rafi, get approval, then the next one.
5. EVIDENCE BEFORE DONE. Verify the artefact and report the actual numbers. A
   summary is not evidence. For video that means duration, streams, and frames —
   not "it worked".
6. Do NOT invent content. Anchor scripts, episode copy and names come from Rafi or
   from source material, never from me.
7. Claude cannot see rendered output. Ask for frames or screenshots before any
   visual judgement.
8. Every workflow instruction Rafi gives in ANY Claude chat gets written into this
   file so the next session already knows it.

## Project-specific

9. MEDIA STAYS OUT OF GIT. Clips, masters and logo masters live in Google Drive
   (`AI_News_Desk/`). This repo holds scripts, prompts, subtitle text and brand
   config only. The Drive folder must stay replaceable without touching the repo.
10. BRANDING IS ADDED IN POST, NEVER GENERATED. MiniMax cannot reproduce a specific
    logo — it produces a different lookalike every render. Generate the set generic
    and overlay the real asset with ffmpeg. Set dressing and backgrounds are fine to
    generate; anything carrying the brand is not.
11. SUBTITLE CANVAS IS LOAD-BEARING. An `.srt` has no resolution, so libass assumes
    384x288 and renders text ~6x oversized in mid-frame. Always convert to `.ass`
    and pin `PlayResX: 1080` / `PlayResY: 1920`. Never burn straight from `.srt`.
12. THE SUBTITLE APPROVAL PAUSE IS NOT OPTIONAL. Whisper mangles proper nouns
    ("ChatGPT Atlas" came out "chat GPT Astras"). Always show Rafi the transcript
    and wait for his word before burning.
13. Scripts must be double-clickable and self-installing. Rafi's production machine
    is Windows 10 22H2. Assume nothing is installed; assume PATH is stale after any
    install; assume `python.exe` may be the Microsoft Store stub that only opens the
    Store. Check that a tool RUNS, not that it exists.
