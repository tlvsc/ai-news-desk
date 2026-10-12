"""Full-wall hologram date (hologram blueprint V2): the date fills the whole blue glass TV, inside the 16 px bezel,
as a layer BEHIND the presenter (restored on top with the Robust Video Matting alpha from rvm_opening.py).
Usage: python make_holo_wall.py SUN 11 OCT 2026 -> holo_wall_<day><mon>_overlay.png + a still and a 0-5.2 s preview clip."""
import sys, os, math, subprocess
R = r'C:\Users\erans\Documents\Codex\2026-09-11\check-if-complete-finishes-it-generation'
sys.path[:0] = [R + r'\video_runtime']
import numpy as np, av
from PIL import Image, ImageDraw, ImageFont, ImageFilter
HOLO = r'C:\Users\erans\AppData\Local\Temp\aind_holo'
WEEKDAY, DAY, MONTH, YEAR = sys.argv[1:5] if len(sys.argv) > 4 else ('SUN', '11', 'OCT', '2026')
TAG = f'{DAY}{MONTH.lower()}'
SRC = r'C:\Users\erans\AppData\Local\Temp\aind_drive\AIND_opening_option4_2026-10-03_VL1_1088_FROM_DRIVE.mp4'
DATE_STRIP = sys.argv[5] if len(sys.argv) > 5 else r'C:\Users\erans\AppData\Local\Temp\aind_stitch11\date_overlay_11-10-26.png'
FF = r'C:\Projects\hebrew-lipsync-test\MuseTalk\ffmpeg-bin\ffmpeg.exe'
F_BLACK, F_LIGHT = r'C:\Windows\Fonts\seguibl.ttf', r'C:\Windows\Fonts\segoeuil.ttf'
S = 4

# Outer glass frame measured on the opening at 3.2 s (1080x1920): seam x 345, top rail 613 -> 584, bottom rail 1027@520 -> 1045@1080.
top = lambda x: 613 + (584 - 613) * (x - 345) / (1080 - 345)
bot = lambda x: 1027 + (1045 - 1027) * (x - 520) / (1080 - 520)
BEZEL = 16
X0, X1 = 345 + BEZEL, 1080
QUAD = [(X0, top(X0) + BEZEL), (X1, top(X1) + BEZEL), (X1, bot(X1) - BEZEL), (X0, bot(X0) - BEZEL)]   # TL TR BR BL
W = int(X1 - X0); H = int(round(((QUAD[3][1] - QUAD[0][1]) + (QUAD[2][1] - QUAD[1][1])) / 2))


def font(path, size):
    return ImageFont.truetype(path, int(size * S))


def glow(canvas, mask, color, radius, strength):
    g = mask.filter(ImageFilter.GaussianBlur(radius * S)).point(lambda v: min(255, int(v * strength)))
    layer = Image.new('RGBA', canvas.size, color + (0,)); layer.putalpha(g); canvas.alpha_composite(layer)


def fill(canvas, mask, rgb_img):
    layer = rgb_img.convert('RGBA'); layer.putalpha(mask); canvas.alpha_composite(layer)


def vgrad(size, a, b, y0, y1):
    w, h = size
    t = np.clip((np.arange(h) - y0) / max(1, y1 - y0), 0, 1)[:, None, None]
    return Image.fromarray(np.broadcast_to(np.array(a, np.float32) * (1 - t) + np.array(b, np.float32) * t, (h, w, 3)).astype(np.uint8))


def text_mask(txt, f, xy, size, anchor='ls'):
    m = Image.new('L', size, 0); ImageDraw.Draw(m).text(xy, txt, font=f, fill=255, anchor=anchor); return m


def heavy(canvas, txt, f, xy, anchor, top_rgb=(255, 255, 255), bot_rgb=(176, 214, 255)):
    m = text_mask(txt, f, xy, canvas.size, anchor); bb = m.getbbox()
    sh = Image.new('RGBA', canvas.size, (0, 14, 50, 0)); sh.putalpha(m.filter(ImageFilter.GaussianBlur(3 * S)).point(lambda v: int(v * .85)))
    canvas.alpha_composite(sh); glow(canvas, m, (40, 140, 255), 9, .75); fill(canvas, m, vgrad(canvas.size, top_rgb, bot_rgb, bb[1], bb[3]))
    return bb


def wall_card():
    w, h = W * S, H * S
    card = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    shape = Image.new('L', (w, h), 0); ImageDraw.Draw(shape).rounded_rectangle([0, 0, w + 40 * S, h - 1], radius=12 * S, fill=255)
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    dist = np.sqrt(((xx - .62 * w) / w) ** 2 + ((yy - .45 * h) / h) ** 2) / .8
    t = np.clip(dist, 0, 1)[..., None]
    bg = (np.array([16, 66, 165], np.float32) * (1 - t) + np.array([3, 16, 56], np.float32) * t).astype(np.uint8)
    bgimg = Image.fromarray(bg).convert('RGBA'); bgimg.putalpha(shape.point(lambda v: int(v * .95))); card.alpha_composite(bgimg)
    # faint scan lines across the whole glass
    scan = Image.new('L', (w, h), 0); sd = ImageDraw.Draw(scan)
    for y in range(0, h, 5 * S): sd.line([(0, y), (w, y)], fill=18, width=S)
    fill(card, Image.fromarray(np.minimum(np.asarray(scan), np.asarray(shape))), Image.new('RGB', (w, h), (120, 200, 255)))
    # dotted globe on the right half, behind the date
    gx, gy, rad = .66 * w, .5 * h, .46 * h
    halo = Image.new('L', (w, h), 0); ImageDraw.Draw(halo).ellipse([gx - rad * 1.08, gy - rad * 1.08, gx + rad * 1.08, gy + rad * 1.08], fill=110)
    glow(card, halo, (40, 120, 255), 30, .6)
    dots = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(dots)
    ti, sp = math.radians(22), math.radians(35)
    for lat in range(-78, 79, 6):
        step = max(6, int(round(6 / max(.3, math.cos(math.radians(lat))))))
        for lon in range(0, 360, step):
            la, lo = math.radians(lat), math.radians(lon) + sp
            x, y, z = math.cos(la) * math.sin(lo), math.sin(la), math.cos(la) * math.cos(lo)
            y, z = y * math.cos(ti) - z * math.sin(ti), y * math.sin(ti) + z * math.cos(ti)
            if z > 0:
                px, py, r = gx + x * rad, gy - y * rad, (.8 + 1.6 * z) * S
                d.ellipse([px - r, py - r, px + r, py + r], fill=(95, 175, 255, int(255 * (.15 + .5 * z))))
    card.alpha_composite(dots)
    # date: SUN above, big day, month and year stacked to its right; centred in the part of the wall the presenter never covers
    dm = ImageDraw.Draw(Image.new('L', (8, 8)))
    f_day, f_wd, f_mo, f_yr = font(F_BLACK, .62 * H), font(F_BLACK, .19 * H), font(F_BLACK, .24 * H), font(F_LIGHT, .235 * H)
    dw = dm.textbbox((0, 0), DAY, font=f_day, anchor='ls'); mw = dm.textbbox((0, 0), MONTH, font=f_mo, anchor='ls'); yw = dm.textbbox((0, 0), YEAR, font=f_yr, anchor='ls')
    gap = .05 * H * S
    group = (dw[2] - dw[0]) + gap + max(mw[2] - mw[0], yw[2] - yw[0])
    cx = .64 * w; base = .86 * h
    bb_day = heavy(card, DAY, f_day, (cx - group / 2 - dw[0], base), 'ls')
    rx = bb_day[2] + gap
    heavy(card, MONTH, f_mo, (rx - mw[0], bb_day[1] - mw[1]), 'ls')
    ym = text_mask(YEAR, f_yr, (rx - yw[0], base), card.size, 'ls'); glow(card, ym, (40, 160, 255), 7, 1.0)
    bb = ym.getbbox(); fill(card, ym, vgrad(card.size, (150, 230, 255), (70, 170, 255), bb[1], bb[3]))
    heavy(card, WEEKDAY, f_wd, (cx, bb_day[1] - .06 * h), 'ms')
    return card


def coeffs(dst, src):
    a = []
    for (x, y), (u, v) in zip(dst, src):
        a.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); a.append([0, 0, 0, x, y, 1, -v * x, -v * y])
    return np.linalg.solve(np.array(a, float), np.array(src, float).reshape(8))


def to_frame(card):
    big = (1080 * 2, 1920 * 2)
    src = [(0, 0), (card.width, 0), (card.width, card.height), (0, card.height)]
    warped = card.convert('RGBa').transform(big, Image.PERSPECTIVE, tuple(coeffs([(x * 2, y * 2) for x, y in QUAD], src)), Image.BICUBIC)
    return warped.resize((1080, 1920), Image.LANCZOS).convert('RGBA')


def smooth(x):
    x = min(1, max(0, x)); return x * x * (3 - 2 * x)


def card_alpha(t):
    if t < 1.8 or t > 4.6: return 0.0
    if t < 2.5: return smooth((t - 1.8) / .7)
    if t > 3.8: return 1 - smooth((t - 3.8) / .8)
    return 1.0


if __name__ == '__main__':
    overlay = to_frame(wall_card())
    out_png = os.path.join(HOLO, f'holo_wall_{TAG}_overlay.png'); overlay.save(out_png)
    ov = np.asarray(overlay).astype(np.float32); ca0 = ov[:, :, 3:4] / 255; crgb = ov[:, :, :3]
    ds = np.asarray(Image.open(DATE_STRIP).convert('RGBA')).astype(np.float32); da = ds[:, :, 3:4] / 255
    frames = []
    with av.open(SRC) as c:
        fps = float(c.streams.video[0].average_rate)
        for i, f in enumerate(c.decode(video=0)):
            t = i / fps
            if t > 5.2: break
            a = f.to_ndarray(format='rgb24')[:, 4:1084].astype(np.float32)
            pha = np.asarray(Image.open(os.path.join(HOLO, 'matte', f'pha_{i:04d}.png'))).astype(np.float32)[..., None] / 255
            k = card_alpha(t)
            res = a * (1 - ca0 * k) + crgb * ca0 * k          # date layer on the TV
            res = res * (1 - pha) + a * pha                   # presenter back in front
            res = res * (1 - da) + ds[:, :, :3] * da          # date strip on top, as in the final
            frames.append(np.clip(res, 0, 255).round().astype(np.uint8))
            if abs(t - 3.2) < .021:
                Image.fromarray(frames[-1]).save(os.path.join(HOLO, f'holo_wall_{TAG}_still.png'))
                Image.fromarray(frames[-1]).crop((250, 480, 1080, 1200)).save(os.path.join(HOLO, f'holo_wall_{TAG}_zoom.png'))
    clip = os.path.join(HOLO, f'holo_wall_{TAG}_preview.mp4')
    p = subprocess.Popen([FF, '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', '1080x1920', '-framerate', str(fps), '-i', 'pipe:0',
                          '-ss', '0', '-t', f'{len(frames) / fps:.3f}', '-i', SRC, '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-crf', '18',
                          '-preset', 'fast', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '160k', '-shortest', '-movflags', '+faststart', clip], stdin=subprocess.PIPE)
    for fr in frames: p.stdin.write(fr.tobytes())
    p.stdin.close(); print('preview', clip, p.wait(), 'quad', [(round(x), round(y)) for x, y in QUAD], 'card', W, H)
