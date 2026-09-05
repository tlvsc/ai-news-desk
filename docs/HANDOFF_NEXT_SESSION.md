# AI News Desk — Session Handoff

Last updated: 2026-08-14, end of the first session.

## Where things stand

**Episode 1 is finished and on Rafi's PC.** `Reel_master_subbed.mp4` in
`C:\Users\tlvsc\Downloads` — 18.4s, 1080x1920, 30fps, H.264 + AAC, burned-in
English subtitles. Verified: duration within 0.04s of clip1+clip2-0.5s, audio
stream present, three frames checked by eye.

Subtitles were re-burned once at `MarginV = 420` so they clear the "TLV NEWS ROOM"
desk graphic. The first master is kept as `Reel_master_subbed_old.mp4`.

## Open items

1. **Logo overlay — waiting on the PNG.** Rafi has a new logo in Drive at
   `AI_News_Desk/logos/` (horizontal + circular, transparent masters). The plan
   agreed: corner bug and/or a replacement desk band, overlaid in post with
   ffmpeg. NOT regenerated in MiniMax — see CLAUDE.md rule 10.
   The back screen behind the anchor is **not** a candidate: his head occludes the
   on-set text, so that needs masking, not an overlay.
2. **Generation speed.** Rafi runs the clips locally (ComfyUI — the `_00070_`
   filename numbering), GPU power-capped to 300W, and estimates ~600s for a
   480x768 clip. He wants it faster. This needs a session that can see the GPU,
   the VRAM and the workflow JSON — a cloud container cannot. Route to Claude Code
   local. Unanswered when this session ended: which card, and how many
   frames/steps that 600s covers.
   Worth checking first: a 300W cap on a modern card typically costs ~5-10%, so it
   is probably not the bottleneck. Steps, frame count, fp8 weights and step-caching
   are the bigger levers; dropping resolution softens faces, which is the whole
   format.
3. **Drive access.** Rafi may open `drive.google.com` + `googleapis.com` on the
   environment (claude.ai/code -> environment settings -> Network access). Until
   then a cloud session can list Drive files by name but cannot read image bytes —
   he has to drag images into the chat.

## Environment gotchas (cost most of a day, do not rediscover)

The tlvsc-store cloud environment blocks everything except GitHub and the package
registries. Confirmed blocked: `drive.google.com`, `huggingface.co` and mirrors,
`openaipublic.azureedge.net` (Whisper weights), Ubuntu PPAs, `cdn.shopify.com`.
So a cloud session **cannot** transcribe — no model weights are reachable — and
cannot fetch Drive media. All video work happens on Rafi's PC.

The GitHub App also had to be granted access to this repo separately; it is
installed per-repository, not per-account.

## Rafi's machine

Windows 10 Pro 22H2. Now has: Git 2.55, ffmpeg 9.0 (winget Gyan.FFmpeg), Python
3.12, openai-whisper + torch 2.13, MSVC redistributable. Claude Code installed.
The scripts in `scripts/` assume none of this and install what is missing.
