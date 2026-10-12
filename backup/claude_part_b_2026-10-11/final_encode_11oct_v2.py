"""11 Oct Headlines final (Claude-V1), done the way aind_v1_headline_script.py does it (Drive copy of 11 Oct, read and followed, not run):
native 1088->1080 crop, 24->30 fps cadence, 1.2 s screen/reflection-only join blends, 9-frame fade in/out padding,
mastered audio (highpass 60 Hz, 0.3 s delay, -14 LUFS), captions + source strips from its caption layout,
cyan spoken word and rolling source strip (approved 10 Oct), date strip on every frame, SUN 11 OCT hologram card in the opening.
Opening, ending, layout image, fonts and stitcher all come from Drive and were checked this session."""
import sys, json, re, difflib, subprocess, threading
sys.dont_write_bytecode = True
from fractions import Fraction
from pathlib import Path
R = r'C:\Users\erans\Documents\Codex\2026-09-11\check-if-complete-finishes-it-generation'
DRIVE = Path(r'C:\Users\erans\AppData\Local\Temp\aind_drive')
sys.path[:0] = [R + r'\video_runtime', R + r'\asr_runtime', str(DRIVE / 'mod11')]
import numpy as np, av
from PIL import Image
import aind_v1_headline_script as st
from faster_whisper import WhisperModel

FF = r'C:\Projects\hebrew-lipsync-test\MuseTalk\ffmpeg-bin\ffmpeg.exe'
WORK = Path(r'C:\Users\erans\AppData\Local\Temp\aind_stitch11')
OUT = WORK / 'out'; OUT.mkdir(exist_ok=True)
VIDEO = Path(r'E:\ComfyUI\output\video')
DATE = WORK / 'date_overlay_11-10-26.png'
CARD = Path(r'C:\Users\erans\AppData\Local\Temp\aind_holo\holo_wall_11oct_overlay.png')   # whole holographic screen
OPEN_MATTE = Path(r'C:\Users\erans\AppData\Local\Temp\aind_holo\matte')                    # presenter alpha, opening
C09_MATTE = Path(r'C:\Users\erans\AppData\Local\Temp\aind_crab\matte_c09')                # presenter alpha, C09
CRAB_GIF = Path(r'C:\Users\erans\AppData\Local\Temp\aind_crab\download\official-jump.gif')  # KingKong Robotics, Apache-2.0
CRAB_CREDIT = 'Video: KingKong Robotics (Apache-2.0)'
SCREEN = [(361, 628), (1080, 600), (1080, 1029), (361, 1006)]                               # inside the 16 px bezel
AUDIO = OUT / 'Headlines_11-10-26_master_audio.wav'
ASS = OUT / 'Headlines_11-10-26_Claude-V1.ass'
SRT = OUT / 'Headlines_11-10-26_Claude-V1.srt'
FINAL = Path(r'E:\Downloads\Headlines_11-10-26_Claude-V1.mp4')
WORDS = OUT / 'Headlines_11-10-26_words.json'
FONTS = DRIVE / 'fonts'
PAD = st.PADDING_FRAMES                   # 9 frames at 30 fps = 0.3 s

# Spoken lines come from the approved 11 Oct workflow JSON; outlets from the 11 Oct Daily Bulletin (Claude-V1) on Drive.
WF = r'C:\Users\erans\AppData\Local\Comfy-Desktop\ComfyUI-Installs\ComfyUI-refael\ComfyUI\user\default\workflows\headlines_11-10-26_VL1.json'
_nodes = {str(n['id']): n for n in json.load(open(WF, encoding='utf-8'))['nodes']}
def spoken(k):
    return re.findall(r'"([^"]{20,})"', str(_nodes[str(100 * k + 12)]['widgets_values'][0]))[-1]
def written(t):
    for a, b in (('A I', 'AI'), ('N-vidia', 'NVIDIA'), ('T S M C', 'TSMC'), ('twelve', '12')): t = t.replace(a, b)
    return t
SOURCES = {2: 'The Guardian', 3: 'Financial Times', 4: 'TechCrunch', 5: 'The Decoder', 6: 'Startup Fortune', 7: 'China Daily',
           8: 'Variety', 9: 'Interesting Engineering', 10: 'AI News Desk', 11: 'AI News Desk'}
assert all(SOURCES.values()), 'missing source for ' + str([k for k, v in SOURCES.items() if not v])
CLIP_FILES = {9: Path(r'C:\Users\erans\AppData\Local\Temp\aind_stitch11\fixed\headlines_11-10-26_C09_VL1_1088_muted_v3.mp4')}
rows = [{'id': 'opening', 'file': DRIVE / 'AIND_opening_option4_2026-10-03_VL1_1088_FROM_DRIVE.mp4', 'sources': [],
         'text': 'Welcome to AI News Desk. I am Rafael, and every day I bring you the headlines from all fields of AI, the tech, the money, the people, and the tools shaping our world. Ninety seconds, starting now.'}]
for c in range(2, 12):
    f = CLIP_FILES.get(c, VIDEO / f'headlines_11-10-26_C{c:02d}_VL1_1088_00001_.mp4')
    assert f.exists() and f.stat().st_size > 1_000_000, f
    rows.append({'id': f'C{c:02d}', 'file': f, 'sources': [SOURCES[c]], 'text': written(spoken(c))})
rows.append({'id': 'ending', 'file': DRIVE / 'AIND_ending_option4_2026-10-03_VL1_1088_FROM_DRIVE.mp4', 'sources': [],
             'text': "Those were today's headlines in ninety seconds. For more detailed coverage, read our daily news cards. Thank you for tuning in, and we'll see you tomorrow."})

# --- picture facts per clip (all frames kept) and boundary frames for the join blends
for r in rows:
    with av.open(str(r['file'])) as c:
        v = c.streams.video[0]; r['fps'] = Fraction(v.average_rate)
        frames = [st.native_rgb(f) for f in c.decode(video=0)]
    r['frames'] = len(frames); r['duration'] = float(Fraction(len(frames)) / r['fps'])
    r['edges'] = (frames[0], frames[-1]); del frames
    print(r['id'], r['frames'], 'frames', round(r['duration'], 3), 's', flush=True)

# --- words: approved written text, timed by the speech recogniser
if WORDS.exists():
    saved = json.loads(WORDS.read_text(encoding='utf-8'))
    for r in rows: r['words'] = saved[r['id']]
else:
    model = WhisperModel('base.en', device='cpu', compute_type='int8', cpu_threads=4, download_root=R + r'\speech_model', local_files_only=True)
    norm = lambda w: re.sub(r"[^a-z0-9']", '', w.lower())
    for r in rows:
        segs, _ = model.transcribe(str(r['file']), language='en', beam_size=5, word_timestamps=True, condition_on_previous_text=False)
        asr = [w for s in segs for w in s.words]; want = r['text'].split()
        sm = difflib.SequenceMatcher(a=[norm(w) for w in want], b=[norm(w.word) for w in asr], autojunk=False)
        t = [None] * len(want)
        for b in sm.get_matching_blocks():
            for k in range(b.size): t[b.a + k] = (asr[b.b + k].start, asr[b.b + k].end)
        known = [i for i, x in enumerate(t) if x]
        for i in range(len(want)):
            if t[i] is None:
                p = max([k for k in known if k < i], default=None); n = min([k for k in known if k > i], default=None)
                a = t[p][1] if p is not None else (asr[0].start if asr else 0.0)
                e = t[n][0] if n is not None else (asr[-1].end if asr else r['duration'] - .1)
                span = list(range((p if p is not None else -1) + 1, n if n is not None else len(want))); j = span.index(i); s = (e - a) / max(1, len(span))
                t[i] = (a + j * s, a + (j + 1) * s)
        r['words'] = [{'word': w, 'start': max(0.0, x[0]), 'end': min(r['duration'] - .03, max(x[1], x[0] + .05))} for w, x in zip(want, t)]
        print('words', r['id'], len(r['words']), flush=True)
    WORDS.write_text(json.dumps({r['id']: r['words'] for r in rows}, indent=1), encoding='utf-8')

# --- captions/credits with the script's layout and 0.3 s padding offset
ass, srt, timeline = st.caption_files([{'id': r['id'], 'duration': r['duration'], 'words': r['words'], 'sources': r['sources']} for r in rows],
                                      {'body_bold': FONTS / 'InstrumentSans-Bold.ttf'}, padding_seconds=st.PADDING_SECONDS)
ASS.write_text(ass, encoding='utf-8'); SRT.write_text(srt, encoding='utf-8')
# --- karaoke: the word being spoken turns cyan, the rest stay white (same layout, same timing source)
def _sec(t):
    h, m, r = t.split(':'); return int(h) * 3600 + int(m) * 60 + float(r)
def _fmt(x):
    cs = int(round(x * 100)); h, r = divmod(cs, 360000); m, r = divmod(r, 6000); sec, c = divmod(r, 100)
    return f'{h}:{m:02d}:{sec:02d}.{c:02d}'
seq, cur = [], st.PADDING_SECONDS
for r in rows:
    for w in r['words']: seq.append(cur + w['start'])
    cur += r['duration']
src_lines, out_lines, i, widx = ass.split('\n'), [], 0, 0
is_text = lambda L: L.startswith('Dialogue: 1,') and '\\an8\\pos(' in L
while i < len(src_lines):
    L = src_lines[i]
    if not is_text(L):
        out_lines.append(L); i += 1; continue
    p0 = L.split(',', 9); grp = []
    while i < len(src_lines) and is_text(src_lines[i]) and src_lines[i].split(',', 9)[1:3] == p0[1:3]:
        grp.append(src_lines[i].split(',', 9)); i += 1
    parts = []
    for g in grp:
        cut = g[9].index('}') + 1; parts.append((g, g[9][:cut], g[9][cut:].split(' ')))
    n = sum(len(t) for _, _, t in parts); starts = seq[widx:widx + n]; widx += n
    ev_s, ev_e = _sec(p0[1]), _sec(p0[2])
    for k in range(n):
        a = ev_s if k == 0 else max(ev_s, starts[k]); b = min(ev_e, starts[k + 1]) if k + 1 < n else ev_e
        if b - a < 0.01: continue
        c = 0
        for g, tag, toks in parts:
            shown = []
            for t in toks:
                shown.append('{\\c&HF6E13E&}' + t + '{\\c&HFFFFFF&}' if c == k else t); c += 1
            out_lines.append(','.join([g[0], _fmt(a), _fmt(b)] + g[3:9]) + ',' + tag + ' '.join(shown))
assert widx == len(seq), (widx, len(seq))
ass = '\n'.join(out_lines); ASS.write_text(ass, encoding='utf-8')
print('karaoke events', sum(1 for L in out_lines if is_text(L)), flush=True)
# --- source strip rolls out to the left and rolls back in with the next source
import re as _re
ROLL, OFF = 0.35, -760
def _moved(text, dx_from, dx_to, t_ms):
    return _re.sub(r'\\pos\((-?\d+),(-?\d+)\)', lambda m: f'\\move({int(m.group(1)) + dx_from},{m.group(2)},{int(m.group(1)) + dx_to},{m.group(2)},0,{t_ms})', text)
src2, res, j = ass.split('\n'), [], 0
is_credit = lambda L: L.startswith('Dialogue:') and L.split(',', 9)[3:4] == ['Credit']
while j < len(src2):
    L = src2[j]
    if not is_credit(L):
        res.append(L); j += 1; continue
    k0 = L.split(',', 9); grp = []
    while j < len(src2) and is_credit(src2[j]) and src2[j].split(',', 9)[1:3] == k0[1:3]:
        grp.append(src2[j].split(',', 9)); j += 1
    a, b = _sec(k0[1]), _sec(k0[2]); r = min(ROLL, (b - a) / 3)
    for g in grp:
        head = lambda t0, t1: ','.join([g[0], _fmt(t0), _fmt(t1)] + g[3:9]) + ','
        res.append(head(a, a + r) + _moved(g[9], OFF, 0, int(r * 1000)))
        res.append(head(a + r, b - r) + g[9])
        res.append(head(b - r, b) + _moved(g[9], 0, OFF, int(r * 1000)))
ass = '\n'.join(res); ASS.write_text(ass, encoding='utf-8')
print('roll credits done', sum(1 for L in res if is_credit(L)), flush=True)
print('captions', len(timeline['captions']), 'credits', len(timeline['credits']), flush=True)

# --- mastered audio, as master_audio(): concat, highpass 60 Hz, 0.3 s delay, pad, then -14 LUFS / -1.5 dBTP
if not AUDIO.exists():
    args = []; flt = []
    for i, r in enumerate(rows):
        args += ['-i', str(r['file'])]
        flt.append(f'[{i}:a]aresample=48000,aformat=channel_layouts=stereo,asetpts=PTS-STARTPTS,apad,atrim=duration={r["duration"]:.9f}[a{i}]')
    flt.append(''.join(f'[a{i}]' for i in range(len(rows))) + f'concat=n={len(rows)}:v=0:a=1,highpass=f=60,adelay=delays=300:all=1,apad=pad_dur={st.PADDING_SECONDS},'
               'loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]')
    res = subprocess.run([FF, '-hide_banner', '-y', *args, '-filter_complex', ';'.join(flt), '-map', '[a]', '-c:a', 'pcm_s16le', str(AUDIO)], capture_output=True, text=True, encoding='utf-8', errors='replace')
    assert res.returncode == 0, res.stderr[-1500:]
    print('audio mastered', flush=True)

# --- picture: join blends + whole-screen layers behind the presenter (opening date, C09 crab clip) + date strip on every frame
from PIL import ImageDraw, ImageFont, ImageFilter, ImageSequence
mask = st.screen_reflection_mask()
date = np.asarray(Image.open(DATE).convert('RGBA')).astype(np.float32); date_a = date[:, :, 3:4] / 255; date_rgb = date[:, :, :3]
card = np.asarray(Image.open(CARD).convert('RGBA')).astype(np.float32); card_a = card[:, :, 3:4] / 255; card_rgb = card[:, :, :3]
def coeffs(dst, src):
    m = []
    for (x, y), (u, v) in zip(dst, src):
        m.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); m.append([0, 0, 0, x, y, 1, -v * x, -v * y])
    return np.linalg.solve(np.array(m, float), np.array(src, float).reshape(8))
def to_screen(img):
    w, h = 719 * 4, 403 * 4
    big = img.convert('RGB').resize((w, h), Image.LANCZOS).convert('RGBA')
    m = Image.new('L', (w, h), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, w + 200, h - 1], radius=48, fill=255)
    big.putalpha(m.filter(ImageFilter.GaussianBlur(4)))
    out = big.convert('RGBa').transform((2160, 3840), Image.PERSPECTIVE, tuple(coeffs([(x * 2, y * 2) for x, y in SCREEN], [(0, 0), (w, 0), (w, h), (0, h)])), Image.BICUBIC)
    out = np.asarray(out.resize((1080, 1920), Image.LANCZOS).convert('RGBA')).astype(np.float32)
    return out[:, :, :3], out[:, :, 3:4] / 255
crab = [to_screen(f.copy()) for f in ImageSequence.Iterator(Image.open(CRAB_GIF))]
cl = Image.new('RGBA', (1080, 1920), (0, 0, 0, 0)); cd = ImageDraw.Draw(cl)
cf = ImageFont.truetype(str(FONTS / 'InstrumentSans-Bold.ttf'), 22)
tw = cd.textlength(CRAB_CREDIT, font=cf); x1, y0 = 1060, 614
cd.rounded_rectangle([x1 - tw - 20, y0, x1, y0 + 32], radius=8, fill=(0, 10, 30, 150))
cd.text((x1 - 10, y0 + 16), CRAB_CREDIT, font=cf, fill=(255, 255, 255, 255), anchor='rm')
credit = np.asarray(cl).astype(np.float32); credit_a = credit[:, :, 3:4] / 255; credit_rgb = credit[:, :, :3]
def matte(folder, idx):
    return np.asarray(Image.open(folder / f'pha_{idx:04d}.png')).astype(np.float32)[..., None] / 255
def card_alpha(local):
    if local < 1.8 or local > 4.6: return 0.0
    if local < 2.5: return st.smooth_fraction((local - 1.8) / .7)
    if local > 3.8: return 1 - st.smooth_fraction((local - 3.8) / .8)
    return 1.0
def crab_alpha(local):
    return st.smooth_fraction((local - 1.4) / .4) * (1 - st.smooth_fraction((local - 6.8) / .4))
def compose(picture, i, local, src):
    orig = picture.astype(np.float32); res = orig
    if i > 0 and local < .6:
        w = (1 - st.smooth_fraction((local + .6) / 1.2)) * mask
        res = res * (1 - w) + rows[i - 1]['edges'][1] * w
    elif i < len(rows) - 1 and local > rows[i]['duration'] - .6:
        w = st.smooth_fraction((local - rows[i]['duration'] + .6) / 1.2) * mask
        res = res * (1 - w) + rows[i + 1]['edges'][0] * w
    if i == 0 and card_alpha(local) > 0:                  # opening: date on the whole screen, presenter in front
        k = card_alpha(local); pha = matte(OPEN_MATTE, src)
        res = res * (1 - card_a * k) + card_rgb * card_a * k
        res = res * (1 - pha) + orig * pha
    if rows[i]['id'] == 'C09' and crab_alpha(local) > 0:  # C09: crab clip on the whole screen, presenter in front, credit
        k = crab_alpha(local); pha = matte(C09_MATTE, src)
        rgb, al = crab[int((local - 1.4) / 0.08) % len(crab)]
        res = res * (1 - al * k) + rgb * al * k
        res = res * (1 - pha) + orig * pha
        res = res * (1 - credit_a * k) + credit_rgb * credit_a * k
    res = res * (1 - date_a) + date_rgb * date_a
    return np.clip(res, 0, 255).round().astype(np.uint8)

fp = lambda p: str(p).replace('\\', '/').replace(':', '\\:')
if FINAL.exists(): raise SystemExit('exists, not overwriting: ' + str(FINAL))
cmd = [FF, '-v', 'warning', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', '1080x1920', '-framerate', '30', '-i', 'pipe:0', '-i', str(AUDIO),
       '-map', '0:v:0', '-map', '1:a:0', '-vf', f"ass='{fp(ASS)}':fontsdir='{fp(FONTS)}',setsar=1",
       '-c:v', 'libx264', '-profile:v', 'high', '-preset', 'fast', '-crf', '17', '-pix_fmt', 'yuv420p', '-threads', '4',
       '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-shortest', '-movflags', '+faststart', str(FINAL)]
proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
errs = []; th = threading.Thread(target=lambda: errs.extend(l.decode(errors='replace') for l in iter(proc.stderr.readline, b''))); th.start()
total = round(sum(Fraction(r['frames']) / r['fps'] for r in rows) * 30)
out = 0; start = Fraction(0); last = None
first = compose(rows[0]['edges'][0], 0, 0.0, 0)
for k in range(PAD): proc.stdin.write(np.round(first * (k / (PAD - 1))).astype(np.uint8).tobytes())
for i, r in enumerate(rows):
    kept = 0
    with av.open(str(r['file'])) as c:
        for f in c.decode(video=0):
            pic = st.native_rgb(f)
            stop = st.output_frame_count(start, r['fps'], kept, total)
            while out < stop:
                local = max(0., float(Fraction(out, 30) - start))
                last = compose(pic, i, local, kept); proc.stdin.write(last.tobytes()); out += 1
            kept += 1
    start += Fraction(kept) / r['fps']
    print('encoded', r['id'], out, flush=True)
for k in range(PAD): proc.stdin.write(np.round(last * (1 - k / (PAD - 1))).astype(np.uint8).tobytes())
proc.stdin.close(); code = proc.wait(); th.join()
print('ffmpeg exit', code, ''.join(errs)[-800:])
print('final', FINAL, FINAL.stat().st_size if FINAL.exists() else 0)
import shutil
SRT_OUT = Path(r'E:\Downloads\Headlines_11-10-26_Claude-V1.srt')
if not SRT_OUT.exists(): shutil.copyfile(SRT, SRT_OUT)
print('srt', SRT_OUT, SRT_OUT.stat().st_size)
