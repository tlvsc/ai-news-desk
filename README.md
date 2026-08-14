# AI News Desk

Production repo for the AI News Desk reels — the TLV news-anchor format.

## What lives where

| Thing | Where | Why |
|---|---|---|
| Scripts, prompts, subtitle files, brand config | **this repo** | text, diffs cleanly, git is good at it |
| Raw clips, rendered masters, logo PNGs | **Google Drive** (`AI_News_Desk/`) | binaries bloat a repo permanently, and nothing here is ever deleted |

The split is deliberate: the Drive folder can move or be replaced without touching this repo.

## Making an episode

1. Generate the two vertical clips in MiniMax (opener + closer).
2. Put both in `Downloads` on the production PC.
3. Double-click `scripts/MAKE_REEL.cmd`.
   - installs ffmpeg, Python and Whisper on first run
   - stitches with a 0.5s crossfade → 1080x1920, 30fps, H.264 CRF 18, AAC 192k
   - transcribes with Whisper `small`, English
   - **stops and shows the subtitle text for approval** before burning anything
4. Fix any wrong words in `subs.srt`, type `yes`.
5. Output: `Reel_master_subbed.mp4`, plus three verification frames.

To move the subtitles without re-transcribing, run `scripts/RESTYLE_REEL.cmd` — it
reuses `_stitched.mp4` and `subs.srt`, renders preview frames at several heights,
and re-burns at the one you pick.

## Known traps

- **Subtitle size/position.** An `.srt` carries no resolution, so libass assumes a
  384x288 canvas: `FontSize` and `MarginV` come out ~6x too large and the text
  lands mid-frame. Both scripts convert to `.ass` and pin `PlayResX/Y` to
  1080x1920 so those numbers mean real pixels. Do not "simplify" this away.
- **Branding.** MiniMax cannot reproduce a specific logo — it invents lookalikes
  that differ every render. The generated set already says "TLV-NR" with mangled
  kerning, which was never a real design. Generate the set generic; add the logo
  in post as an overlay.
- **The anchor occludes the back screen.** His head sits in front of the on-set
  text, so replacing that screen needs masking, not a simple overlay. The desk
  band and the frame corners are the unoccluded places to put branding.
- **Windows PATH.** After a `winget` install, a fresh `cmd` window can still miss
  the new tool. The scripts re-read PATH from the registry and then hunt for the
  `.exe` directly.
- **The Microsoft Store python stub.** `python.exe` exists on a clean Windows box
  but only opens the Store. Checking "does python exist" is wrong; the scripts
  check "does python actually run".
