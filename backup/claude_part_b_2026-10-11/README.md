# Backup: Claude's local Part B scripts, 11 Oct 2026

Backup of Claude's local Part B scripts that produced the approved Headlines_11-10-26_Claude-V1.mp4. Paths are Refael's Windows PC. Not a rulebook: the lessons live only in docs/V1_TASKS.md.

Files:
- final_encode_11oct_v2.py: the full stitch (cyan word, rolling source, full-screen date behind the presenter, crab footage plus credit on C09, date strip, audio master)
- make_holo_wall.py: the full-screen hologram date plus preview
- rvm_opening.py: the presenter matte for the opening (Robust Video Matting)
- crab_c09_preview.py: matte plus footage on C09's screen, with preview
- run_clips_11oct.py: cuts the ComfyUI prompt into 10 clip jobs and runs them one by one
- splice10.py: word swap or mute on the audio only (picture copied)
- make_date11.py: the date strip from the layout image
- stutter_c09c.py, stutter_c09d.py, stutter_c09e.py: the stutter finders (disfluency Whisper windows, 10 ms loudness and pitch, sampled transcripts)

Note sent with stutter_c09c.py: its second prompt contains "g- given" and biases the result. Lesson: never put the suspected words in the prompt (docs/V1_TASKS.md lesson 240).
