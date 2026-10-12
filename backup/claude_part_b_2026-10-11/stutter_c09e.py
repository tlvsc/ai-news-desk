"""Read-only: sample several transcriptions of C09 and count which repeated or broken words keep coming back."""
import sys, subprocess, collections
R = r'C:\Users\erans\Documents\Codex\2026-09-11\check-if-complete-finishes-it-generation'
sys.path[:0] = [R + r'\video_runtime', R + r'\asr_runtime']
import numpy as np
from faster_whisper import WhisperModel
CLIP = r'E:\ComfyUI\output\video\headlines_11-10-26_C09_VL1_1088_00001_.mp4'
FF = r'C:\Projects\hebrew-lipsync-test\MuseTalk\ffmpeg-bin\ffmpeg.exe'
m = WhisperModel('base.en', device='cpu', compute_type='int8', cpu_threads=4, download_root=R + r'\speech_model', local_files_only=True)
pcm = subprocess.run([FF, '-v', 'error', '-i', CLIP, '-vn', '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'], capture_output=True).stdout
x = np.frombuffer(pcm, np.float32).copy()
EXPECT = "and finally something lighter a chinese company has given away the plans for its jumping crab robot so anyone can build one and use ai to teach it new tricks".split()
prompts = ["Umm, let me think like, hmm... Okay, here's what I'm, like, thinking.", "Uh, I- I- I think, um, we- we should, uh, go."]
extra = collections.Counter()
for p in prompts:
    for temp in (0.0, 0.3, 0.6, 0.9):
        for rep in range(2 if temp else 1):
            segs, _ = m.transcribe(x, language='en', beam_size=1 if temp else 5, best_of=1, temperature=temp, word_timestamps=True,
                                   condition_on_previous_text=False, initial_prompt=p, vad_filter=False)
            ws = [(w.start, w.end, ''.join(c for c in w.word.lower() if c.isalnum())) for s in segs for w in s.words]
            ws = [w for w in ws if w[2]]
            # words that are not the next expected word = inserted (repeats, fragments)
            j, odd = 0, []
            for a, b, t in ws:
                if j < len(EXPECT) and t == EXPECT[j]:
                    j += 1
                elif j < len(EXPECT) - 1 and t == EXPECT[j + 1]:
                    j += 2
                else:
                    odd.append(f'{a:.2f}-{b:.2f}:{t}')
                    extra[(round(a, 1), t)] += 1
            print(f'T={temp} prompt{prompts.index(p)}:', ' '.join(odd) or '(clean)')
print('recurring:', extra.most_common(12))
