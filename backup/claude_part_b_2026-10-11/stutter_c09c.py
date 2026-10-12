"""Read-only: disfluency-aware transcription of short overlapping windows of C09, to catch small stutters."""
import sys, subprocess
R = r'C:\Users\erans\Documents\Codex\2026-09-11\check-if-complete-finishes-it-generation'
sys.path[:0] = [R + r'\video_runtime', R + r'\asr_runtime']
import numpy as np
from faster_whisper import WhisperModel
CLIP = r'E:\ComfyUI\output\video\headlines_11-10-26_C09_VL1_1088_00001_.mp4'
FF = r'C:\Projects\hebrew-lipsync-test\MuseTalk\ffmpeg-bin\ffmpeg.exe'
m = WhisperModel('base.en', device='cpu', compute_type='int8', cpu_threads=4, download_root=R + r'\speech_model', local_files_only=True)
pcm = subprocess.run([FF, '-v', 'error', '-i', CLIP, '-vn', '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'], capture_output=True).stdout
x = np.frombuffer(pcm, np.float32).copy()
prompts = ["Umm, let me think like, hmm... Okay, here's what I'm, like, thinking. I- I mean, th- the, uh, so-so.",
           "So, uh, the- the c- company, um, has, uh, g- given, like, a- away..."]
for a, b in ((0.0, 2.2), (1.9, 4.4), (4.0, 6.3), (6.2, 8.4), (8.0, 10.1), (0.0, 6.3), (2.0, 10.1)):
    seg = x[int(a * 16000):int(b * 16000)]
    for p in prompts:
        segs, _ = m.transcribe(seg, language='en', beam_size=5, word_timestamps=True, condition_on_previous_text=False,
                               initial_prompt=p, vad_filter=False)
        ws = [f'{a + w.start:.2f}:{w.word.strip()}({w.probability:.2f})' for s in segs for w in s.words]
        print(f'[{a:.1f}-{b:.1f}]', ' '.join(ws))
