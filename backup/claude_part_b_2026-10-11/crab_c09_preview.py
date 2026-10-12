"""C09 test: KingKong Robotics' Jumper clip (official-jump.gif, Apache-2.0) plays on the whole holographic screen behind the presenter.
1) Robust Video Matting cuts the presenter out of every C09 frame; 2) the GIF loops inside the screen (16 px bezel) from 1.4 to 7.2 s;
3) the presenter goes back on top; 4) the date strip on top. Writes a C09 preview clip with its audio."""
import sys, os, subprocess
R = r'C:\Users\erans\Documents\Codex\2026-09-11\check-if-complete-finishes-it-generation'
sys.path[:0] = [R + r'\video_runtime', R + r'\asr_runtime']
import numpy as np, av, onnxruntime as ort
from PIL import Image, ImageSequence, ImageDraw, ImageFilter
SRC = r'C:\Users\erans\AppData\Local\Temp\aind_stitch11\fixed\headlines_11-10-26_C09_VL1_1088_muted_v3.mp4'
GIF = r'C:\Users\erans\AppData\Local\Temp\aind_crab\download\official-jump.gif'
MODEL = r'C:\Users\erans\AppData\Local\Temp\aind_rvm\model\rvm_mobilenetv3_fp32.onnx'
DATE_STRIP = r'C:\Users\erans\AppData\Local\Temp\aind_stitch11\date_overlay_11-10-26.png'
MATTE = r'C:\Users\erans\AppData\Local\Temp\aind_crab\matte_c09'
OUT = r'C:\Users\erans\AppData\Local\Temp\aind_crab\c09_crab_preview.mp4'
FF = r'C:\Projects\hebrew-lipsync-test\MuseTalk\ffmpeg-bin\ffmpeg.exe'
QUAD = [(361, 628), (1080, 600), (1080, 1029), (361, 1006)]       # same screen as the opening, inside the 16 px bezel
T_IN, T_OUT, FADE = 1.4, 7.2, 0.4
os.makedirs(MATTE, exist_ok=True)


def coeffs(dst, src):
    a = []
    for (x, y), (u, v) in zip(dst, src):
        a.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); a.append([0, 0, 0, x, y, 1, -v * x, -v * y])
    return np.linalg.solve(np.array(a, float), np.array(src, float).reshape(8))


def warp(img):
    """Fit one clip frame to the screen: 4x supersampled perspective warp, rounded left corners, soft edge."""
    w, h = 719 * 4, 403 * 4
    big = img.convert('RGB').resize((w, h), Image.LANCZOS).convert('RGBA')
    m = Image.new('L', (w, h), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, w + 200, h - 1], radius=48, fill=255)
    big.putalpha(m.filter(ImageFilter.GaussianBlur(4)))
    src = [(0, 0), (w, 0), (w, h), (0, h)]
    out = big.convert('RGBa').transform((2160, 3840), Image.PERSPECTIVE, tuple(coeffs([(x * 2, y * 2) for x, y in QUAD], src)), Image.BICUBIC)
    out = np.asarray(out.resize((1080, 1920), Image.LANCZOS).convert('RGBA')).astype(np.float32)
    return out[:, :, :3], out[:, :, 3:4] / 255


def smooth(x):
    x = min(1, max(0, x)); return x * x * (3 - 2 * x)


gif = [warp(f.copy()) for f in ImageSequence.Iterator(Image.open(GIF))]
GIF_STEP = 0.08                                                   # 80 ms per GIF frame, looped
ds = np.asarray(Image.open(DATE_STRIP).convert('RGBA')).astype(np.float32); da = ds[:, :, 3:4] / 255
sess = ort.InferenceSession(MODEL, providers=['CPUExecutionProvider'])
rec = [np.zeros([1, 1, 1, 1], np.float32)] * 4; ratio = np.array([0.25], np.float32)
frames = []
with av.open(SRC) as c:
    fps = float(c.streams.video[0].average_rate)
    for i, f in enumerate(c.decode(video=0)):
        t = i / fps
        a8 = f.to_ndarray(format='rgb24')[:, 4:1084]
        _, pha, *rec = sess.run(None, {'src': (a8.astype(np.float32) / 255).transpose(2, 0, 1)[None], 'r1i': rec[0], 'r2i': rec[1],
                                       'r3i': rec[2], 'r4i': rec[3], 'downsample_ratio': ratio})
        p8 = (pha[0, 0] * 255).round().astype(np.uint8); Image.fromarray(p8).save(os.path.join(MATTE, f'pha_{i:04d}.png'))
        a = a8.astype(np.float32); p = p8.astype(np.float32)[..., None] / 255
        k = smooth((t - T_IN) / FADE) * (1 - smooth((t - (T_OUT - FADE)) / FADE))
        if k > 0:
            rgb, al = gif[int((t - T_IN) / GIF_STEP) % len(gif)]
            a = a * (1 - al * k) + rgb * al * k                   # clip on the screen
            a = a * (1 - p) + a8.astype(np.float32) * p           # presenter back in front
        a = a * (1 - da) + ds[:, :, :3] * da                      # date strip on top
        frames.append(np.clip(a, 0, 255).round().astype(np.uint8))
        if abs(t - 4.0) < 0.021:
            Image.fromarray(frames[-1]).crop((250, 480, 1080, 1200)).save(r'C:\Users\erans\AppData\Local\Temp\aind_crab\c09_crab_zoom.png')
pr = subprocess.Popen([FF, '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', '1080x1920', '-framerate', str(fps), '-i', 'pipe:0',
                       '-i', SRC, '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-crf', '18', '-preset', 'fast', '-pix_fmt', 'yuv420p',
                       '-c:a', 'aac', '-b:a', '160k', '-shortest', '-movflags', '+faststart', OUT], stdin=subprocess.PIPE)
for fr in frames: pr.stdin.write(fr.tobytes())
pr.stdin.close(); print('preview', OUT, pr.wait(), len(frames), 'frames')
