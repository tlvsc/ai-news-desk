"""Read-only: 10 ms loudness and pitch around the two C09 candidates (after "lighter", and "to to teach")."""
import subprocess
import numpy as np
CLIP = r'E:\ComfyUI\output\video\headlines_11-10-26_C09_VL1_1088_00001_.mp4'
FF = r'C:\Projects\hebrew-lipsync-test\MuseTalk\ffmpeg-bin\ffmpeg.exe'
pcm = subprocess.run([FF, '-v', 'error', '-i', CLIP, '-vn', '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'], capture_output=True).stdout
x = np.frombuffer(pcm, np.float32)
def pitch(fr):
    fr = fr - fr.mean()
    if np.sqrt(np.mean(fr ** 2)) < 1e-3: return 0
    c = np.correlate(fr, fr, 'full')[len(fr) - 1:]
    lo, hi = 16000 // 400, 16000 // 70
    k = lo + int(np.argmax(c[lo:hi]))
    return 16000 / k if c[k] > 0.3 * c[0] else 0
for a, b in ((1.20, 1.80), (8.76, 9.22)):
    print(f'--- {a}-{b} s: time dB pitchHz')
    for t in np.arange(a, b, 0.01):
        i = int(t * 16000)
        fr = x[i:i + 160]; big = x[i - 240:i + 400] if i >= 240 else x[i:i + 640]
        print(f'{t:5.2f} {20 * np.log10(max(1e-6, float(np.sqrt(np.mean(fr ** 2))))):6.1f} {pitch(big):5.0f}')
