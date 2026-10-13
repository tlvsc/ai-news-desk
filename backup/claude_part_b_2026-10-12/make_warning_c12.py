"""12 Oct C12: a clean "THIS IS NOT FINANCIAL ADVICE" warning on the whole holographic screen, behind the presenter,
replacing the garbled generated sign (about 0.7-6.4 s). Robust Video Matting cuts the presenter out of every C12 frame.
Writes warning_c12_overlay.png, matte_c12/pha_####.png and a C12 preview clip with its audio."""
import sys, os, math, subprocess
R = r'C:\Users\erans\Documents\Codex\2026-09-11\check-if-complete-finishes-it-generation'
sys.path[:0] = [R + r'\video_runtime', R + r'\asr_runtime']
import numpy as np, av, onnxruntime as ort
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W12 = r'C:\Users\erans\AppData\Local\Temp\aind_stitch12'
TMP = r'E:\Downloads\Claude_temporary_stitching_script_until_merged_to_ChatGPT'
SRC = r'E:\ComfyUI\output\video\headlines_12-10-26_C12_VL1_1088_00001_.mp4'
MODEL = TMP + r'\model\rvm_mobilenetv3_fp32.onnx'
DATE_STRIP = W12 + r'\date_overlay_12-10-26.png'
MATTE = W12 + r'\matte_c12'
FF = r'C:\Projects\hebrew-lipsync-test\MuseTalk\ffmpeg-bin\ffmpeg.exe'
F_BLACK, F_SEMI = r'C:\Windows\Fonts\seguibl.ttf', r'C:\Windows\Fonts\seguisb.ttf'
QUAD = [(361, 628), (1080, 600), (1080, 1029), (361, 1006)]   # whole screen inside the 16 px bezel
W, H, S = 719, 403, 4
T_IN, T_OUT, FADE = 0.7, 6.4, 0.3
os.makedirs(MATTE, exist_ok=True)


def glow(c, m, col, r, k):
    g = m.filter(ImageFilter.GaussianBlur(r * S)).point(lambda v: min(255, int(v * k)))
    l = Image.new('RGBA', c.size, col + (0,)); l.putalpha(g); c.alpha_composite(l)


def fill(c, m, rgb):
    l = Image.new('RGBA', c.size, rgb + (255,)); l.putalpha(m); c.alpha_composite(l)


def card():
    """Clean, precise layout: rounded amber warning icon and a left-aligned text block, centred together on the part of the
    screen the presenter never covers; flat navy glass, soft shadows only, no glow blur on the letters."""
    w, h = W * S, H * S
    img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    shape = Image.new('L', (w, h), 0); ImageDraw.Draw(shape).rounded_rectangle([0, 0, w + 40 * S, h - 1], radius=12 * S, fill=255)
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    t = np.clip(np.sqrt(((xx - .64 * w) / w) ** 2 + ((yy - .5 * h) / h) ** 2) / .9, 0, 1)[..., None]
    bg = (np.array([12, 40, 108], np.float32) * (1 - t) + np.array([4, 14, 44], np.float32) * t).astype(np.uint8)
    b = Image.fromarray(bg).convert('RGBA'); b.putalpha(shape); img.alpha_composite(b)
    # same studio language as the opening date card: faint dotted globe, glass highlight, thin cyan inner frame
    gx0, gy0, rad = .80 * w, .52 * h, .62 * h
    dots = Image.new('RGBA', (w, h), (0, 0, 0, 0)); dd = ImageDraw.Draw(dots)
    ti, sp = math.radians(22), math.radians(35)
    for lat in range(-78, 79, 6):
        step = max(6, int(round(6 / max(.3, math.cos(math.radians(lat))))))
        for lon in range(0, 360, step):
            la, lo = math.radians(lat), math.radians(lon) + sp
            x, y, z = math.cos(la) * math.sin(lo), math.sin(la), math.cos(la) * math.cos(lo)
            y, z = y * math.cos(ti) - z * math.sin(ti), y * math.sin(ti) + z * math.cos(ti)
            if z > 0:
                px, py, r = gx0 + x * rad, gy0 - y * rad, (.7 + 1.2 * z) * S
                dd.ellipse([px - r, py - r, px + r, py + r], fill=(90, 160, 255, int(255 * (.05 + .16 * z))))
    dots.putalpha(Image.fromarray(np.minimum(np.asarray(dots.getchannel('A')), np.asarray(shape)))); img.alpha_composite(dots)
    hl = np.clip(1 - np.abs(yy / h - .08) / .10, 0, 1) * 26
    hi = Image.new('RGBA', (w, h), (180, 220, 255, 0)); hi.putalpha(Image.fromarray(np.minimum(hl, np.asarray(shape)).astype(np.uint8))); img.alpha_composite(hi)
    fr = Image.new('L', (w, h), 0); ImageDraw.Draw(fr).rounded_rectangle([10 * S, 10 * S, w + 40 * S, h - 10 * S], radius=9 * S, outline=255, width=int(1.2 * S))
    fill(img, fr.point(lambda v: int(v * .55)), (90, 200, 255))
    d0 =  ImageDraw.Draw(Image.new('L', (8, 8)))
    f_top = ImageFont.truetype(F_SEMI, int(.074 * h)); f_big = ImageFont.truetype(F_BLACK, int(.128 * h))
    lines = [('THIS IS NOT', f_top, (255, 190, 40), 5 * S), ('FINANCIAL', f_big, (255, 255, 255), 2 * S), ('ADVICE', f_big, (255, 255, 255), 2 * S)]
    def width(txt, f, sp): return sum(d0.textlength(ch, font=f) for ch in txt) + sp * (len(txt) - 1)
    tw = max(width(t_, f, sp) for t_, f, _, sp in lines)
    asc = [f.getbbox('H')[3] - f.getbbox('H')[1] for _, f, _, _ in lines]
    gaps = [.07 * h, .05 * h]
    th = sum(asc) + sum(gaps)
    icon = .40 * h; gap = .07 * w
    group = icon + gap + tw
    gx = min(.62 * w - group / 2, .92 * w - group)                       # group centre on the visible part of the screen
    cy = .5 * h
    # icon: rounded amber triangle with a drawn (not typed) exclamation mark
    tri = Image.new('L', (w, h), 0); td = ImageDraw.Draw(tri)
    top, bl, br = (gx + icon / 2, cy - icon * .46), (gx, cy + icon * .40), (gx + icon, cy + icon * .40)
    td.polygon([top, br, bl], fill=255); td.line([top, br, bl, top], fill=255, width=int(.05 * icon), joint='curve')
    tri = tri.filter(ImageFilter.GaussianBlur(1.2 * S)).point(lambda v: 255 if v > 128 else 0)
    sh = Image.new('RGBA', (w, h), (0, 6, 20, 0)); sh.putalpha(tri.filter(ImageFilter.GaussianBlur(6 * S)).point(lambda v: int(v * .7))); img.alpha_composite(sh)
    fill(img, tri, (255, 190, 40))
    ex = Image.new('L', (w, h), 0); ed = ImageDraw.Draw(ex)
    bw = .085 * icon; mx = gx + icon / 2
    ed.rounded_rectangle([mx - bw / 2, cy - icon * .20, mx + bw / 2, cy + icon * .14], radius=bw / 2, fill=255)
    ed.ellipse([mx - bw * .62, cy + icon * .21, mx + bw * .62, cy + icon * .21 + bw * 1.24], fill=255)
    fill(img, ex, (14, 22, 44))
    # text block, left-aligned, vertically centred on the icon
    x0 = gx + icon + gap; y = cy - th / 2
    for (txt, f, col, sp), a in zip(lines, asc):
        y += a
        mt = Image.new('L', (w, h), 0); md = ImageDraw.Draw(mt); x = x0
        for ch in txt:
            md.text((x, y), ch, font=f, fill=255, anchor='ls'); x += md.textlength(ch, font=f) + sp
        shd = Image.new('RGBA', (w, h), (0, 6, 20, 0)); shd.putalpha(mt.filter(ImageFilter.GaussianBlur(4 * S)).point(lambda v: int(v * .6))); img.alpha_composite(shd)
        fill(img, mt, col)
        y += gaps.pop(0) if gaps else 0
    # one precise amber hairline under the block
    mr = Image.new('L', (w, h), 0); ImageDraw.Draw(mr).rectangle([x0, y + .06 * h, x0 + tw, y + .06 * h + 1.6 * S], fill=255); fill(img, mr, (255, 190, 40))
    return img

def coeffs(dst, src):
    a = []
    for (x, y), (u, v) in zip(dst, src):
        a.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); a.append([0, 0, 0, x, y, 1, -v * x, -v * y])
    return np.linalg.solve(np.array(a, float), np.array(src, float).reshape(8))


def to_frame(c):
    src = [(0, 0), (c.width, 0), (c.width, c.height), (0, c.height)]
    out = c.convert('RGBa').transform((2160, 3840), Image.PERSPECTIVE, tuple(coeffs([(x * 2, y * 2) for x, y in QUAD], src)), Image.BICUBIC)
    return out.resize((1080, 1920), Image.LANCZOS).convert('RGBA')


def smooth(x):
    x = min(1, max(0, x)); return x * x * (3 - 2 * x)


if __name__ == '__main__':
    ov = to_frame(card()); ov.save(W12 + r'\warning_c12_overlay.png')
    o = np.asarray(ov).astype(np.float32); oa = o[:, :, 3:4] / 255; orgb = o[:, :, :3]
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
                a = a * (1 - oa * k) + orgb * oa * k
                a = a * (1 - p) + a8.astype(np.float32) * p
            a = a * (1 - da) + ds[:, :, :3] * da
            frames.append(np.clip(a, 0, 255).round().astype(np.uint8))
            if abs(t - 3.5) < .021:
                Image.fromarray(frames[-1]).save(W12 + r'\warning_c12_still.png')
    clip = W12 + r'\warning_c12_preview.mp4'
    pr = subprocess.Popen([FF, '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', '1080x1920', '-framerate', str(fps), '-i', 'pipe:0',
                           '-i', SRC, '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-crf', '18', '-preset', 'fast', '-pix_fmt', 'yuv420p',
                           '-c:a', 'aac', '-b:a', '160k', '-shortest', '-movflags', '+faststart', clip], stdin=subprocess.PIPE)
    for fr in frames: pr.stdin.write(fr.tobytes())
    pr.stdin.close(); print('preview', clip, pr.wait(), len(frames))
