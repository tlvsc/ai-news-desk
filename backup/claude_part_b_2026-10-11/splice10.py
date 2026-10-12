"""Word swap on the audio only, same math as aind_v1_headline_script.apply_word_repair (stereo 48 kHz float, donor time-fitted with
atempo to the slot, gain clamped 0.7-1.3 to the replaced span, 5 ms edges). Picture stream is copied untouched, no frames removed."""
import subprocess, wave, sys, json
import numpy as np
from pathlib import Path
FF = r'C:\Projects\hebrew-lipsync-test\MuseTalk\ffmpeg-bin\ffmpeg.exe'
SR = 48000
def pcm(p):
    d = subprocess.run([FF, '-v', 'error', '-i', str(p), '-vn', '-ac', '2', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    return np.frombuffer(d, np.float32).reshape(-1, 2).copy()
def fit(donor, count):
    tempo = len(donor) / count
    r = subprocess.run([FF, '-v', 'error', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', 'pipe:0', '-af', f'atempo={tempo:.12f}', '-f', 'f32le', 'pipe:1'], input=donor.tobytes(), capture_output=True)
    w = np.frombuffer(r.stdout, np.float32).reshape(-1, 2).copy()
    return np.pad(w, ((0, max(0, count - len(w))), (0, 0)))[:count], tempo
def apply(clip, out, edits, wav):
    x = pcm(clip); report = []
    for e in edits:
        kind, s, t = e[0], e[1], e[2]
        a, b = round(s * SR), round(t * SR); count = b - a
        fade = np.ones(count, np.float32); edge = round(.005 * SR)
        fade[:edge] = np.linspace(0, 1, edge); fade[-edge:] = np.linspace(1, 0, edge)
        if kind == 'word':
            donor = pcm(e[3])[round(e[4] * SR):round(e[5] * SR)]
            word, tempo = fit(donor, count)
            ref = x[a:b] if len(e) < 7 else x[round(e[6][0] * SR):round(e[6][1] * SR)]   # optional reference span for loudness
            gain = min(1.3, max(.7, float(np.sqrt(np.mean(ref ** 2)) / max(1e-8, np.sqrt(np.mean(word ** 2))))))
            word *= gain
            report.append((kind, s, t, round(tempo, 3), round(gain, 2)))
        else:  # mute: fade the old voice to silence over the span
            word = np.zeros((count, 2), np.float32); report.append((kind, s, t))
        x[a:b] = x[a:b] * (1 - fade[:, None]) + word * fade[:, None]
    with wave.open(str(wav), 'wb') as o:
        o.setnchannels(2); o.setsampwidth(2); o.setframerate(SR)
        o.writeframes((np.clip(x, -1, 1) * 32767).astype('<i2').tobytes())
    r2 = subprocess.run([FF, '-v', 'error', '-y', '-i', str(clip), '-i', str(wav), '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
                         '-ar', str(SR), '-movflags', '+faststart', str(out)], capture_output=True, text=True)
    return report, r2.returncode, r2.stderr[-200:]
if __name__ == '__main__':
    job = json.load(open(sys.argv[1], encoding='utf-8'))
    Path(job['out']).parent.mkdir(parents=True, exist_ok=True)
    print(apply(job['clip'], job['out'], job['edits'], job['wav']))
