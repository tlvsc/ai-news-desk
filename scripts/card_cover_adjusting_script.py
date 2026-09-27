"""card_cover_adjusting_script.py - puts a new date on the approved card cover.

Rule (Plain Language Law, section 3, rule 1): the cover is the approved cover
exactly as it is; only the date changes. This script erases the old date in
both places (header "SUN 13 SEP 2026" and the big blue "13 SEP 2026") and
writes the new one in the same fonts, size, position and colour.

Usage:
    python card_cover_adjusting_script.py 2026-09-28
    python card_cover_adjusting_script.py 2026-09-28 --base <cover.png> --fonts <folder> --out <file.png>

Inputs (media stays out of git, CLAUDE.md rule 9):
    --base   the approved cover, default cards_13-9-26_I01_VL1_presenter_preview.png
             (Drive 1sizbDjBLJB_7K-3uRzZ4S_xI2zpCjdIs). Its own date is --base-date.
    --fonts  folder holding BigShoulders-variable.ttf and RedHatMono-Bold.ttf
             (the cards package, AIND_Cards_2026-09-10/assets/fonts).
Output: cards_D-M-YY_I01_VL1.png, 1080x1920.
"""
import argparse, datetime as dt, importlib, subprocess, sys

for mod, pkg in (("numpy", "numpy"), ("cv2", "opencv-python-headless"), ("PIL", "Pillow")):
    try:
        importlib.import_module(mod)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", pkg])
import numpy as np, cv2
from PIL import Image, ImageFont, ImageDraw

MONTHS = ('JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC')
WEEKDAYS = ('MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN')
BIG_BOX = (1262, 1372, 70, 720)   # y0, y1, x0, x1 around the big blue date
HDR_BOX = (462, 505, 690, 1010)   # around the header date


def texts(d):
    big = f'{d.day} {MONTHS[d.month - 1]} {d.year}'   # same format as the card renderer
    return big, f'{WEEKDAYS[d.weekday()]} {big}'


def text_mask(font, text, shape, xy):
    img = Image.new('L', (shape[1], shape[0]))
    ImageDraw.Draw(img).text(xy, text, font=font, fill=255)
    return np.array(img)


def align(font, text, real, box):
    """Draw origin where the rendered old text best matches the real text pixels."""
    y0, y1, x0, x1 = box
    probe = text_mask(font, text, (400, 1200), (100, 100))
    ys, xs = np.where(probe > 128)
    oy, ox = ys.min() - 100, xs.min() - 100
    ry, rx = np.where(real[y0:y1, x0:x1])
    ty, tx = ry.min() + y0, rx.min() + x0
    best = (-1.0, None)
    for dy in range(-3, 4):
        for dx in range(-3, 4):
            xy = (int(tx - ox + dx), int(ty - oy + dy))
            m = text_mask(font, text, real.shape, xy)[y0:y1, x0:x1] > 128
            r = real[y0:y1, x0:x1]
            iou = (m & r).sum() / (m | r).sum()
            if iou > best[0]:
                best = (iou, xy)
    return best


def fill_rows(img, mask):
    """Fill masked pixels row by row from the nearest clean pixels on each side.
    The set behind the dates is built from horizontal bands, so this leaves no smudge."""
    out = img.astype(float)
    for y in np.where(mask.any(1))[0]:
        row = mask[y]
        clean = np.where(~row)[0]
        for c in range(3):
            out[y, row, c] = np.interp(np.where(row)[0], clean, out[y, clean, c])
    blur = cv2.GaussianBlur(out, (5, 5), 0)
    out[mask] = blur[mask]
    return out.clip(0, 255).astype(np.uint8)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('date', help='new edition date, YYYY-MM-DD')
    ap.add_argument('--base', default='cards_13-9-26_I01_VL1_presenter_preview.png')
    ap.add_argument('--base-date', default='2026-09-13')
    ap.add_argument('--fonts', default='.')
    ap.add_argument('--out', default=None)
    a = ap.parse_args()
    new, old = dt.date.fromisoformat(a.date), dt.date.fromisoformat(a.base_date)
    new_big, new_hdr = texts(new)
    old_big, old_hdr = texts(old)
    out_path = a.out or f'cards_{new.day}-{new.month}-{new.year % 100}_I01_VL1.png'

    base = np.array(Image.open(a.base).convert('RGB'))
    I = base.astype(int)
    R, G, B = I[..., 0], I[..., 1], I[..., 2]
    big = ImageFont.truetype(f'{a.fonts}/BigShoulders-variable.ttf', 109)
    big.set_variation_by_axes([900, 14])          # weight 900, optical size 14: matched to the approved cover
    hdr = ImageFont.truetype(f'{a.fonts}/RedHatMono-Bold.ttf', 32)
    real_big = (B > 200) & (G > 120) & (R < 90)   # the blue date pixels
    real_hdr = (R > 170) & (G > 170) & (B > 170)  # the white header pixels
    iou_big, xy_big = align(big, old_big, real_big, BIG_BOX)
    iou_hdr, xy_hdr = align(hdr, old_hdr, real_hdr, HDR_BOX)
    if iou_big < 0.8 or iou_hdr < 0.7:
        sys.exit(f'Old date not found where expected (match {iou_big:.2f}, {iou_hdr:.2f}). Check --base and --base-date.')

    # blue colour per row, so the new date keeps the original's vertical gradient
    y0, y1, x0, x1 = BIG_BOX
    rows = {}
    for y in range(y0, y1):
        sel = real_big[y, x0:x1]
        if sel.any():
            rows[y] = np.median(I[y, x0:x1][sel], 0)

    # erase both old dates, filling each row from the background either side
    out = base.copy()
    for font, text, xy, real, (by0, by1, bx0, bx1) in ((big, old_big, xy_big, real_big, BIG_BOX),
                                                       (hdr, old_hdr, xy_hdr, real_hdr, HDR_BOX)):
        m = np.zeros(base.shape[:2], np.uint8)
        m[by0:by1, bx0:bx1] = ((text_mask(font, text, base.shape, xy)[by0:by1, bx0:bx1] > 20)
                               | real[by0:by1, bx0:bx1]).astype(np.uint8) * 255
        out = fill_rows(out, cv2.dilate(m, np.ones((7, 7), np.uint8)) > 0)

    # write the new dates
    alpha = text_mask(big, new_big, base.shape, xy_big).astype(float)[..., None] / 255
    keys = sorted(rows)
    colour = np.array([rows[min(keys, key=lambda k: abs(k - y))] for y in range(base.shape[0])])[:, None, :]
    out = (out.astype(float) * (1 - alpha) + colour * alpha).clip(0, 255).astype(np.uint8)
    img = Image.fromarray(out)
    right = xy_hdr[0] + hdr.getlength(old_hdr)   # the header date is right-aligned
    ImageDraw.Draw(img).text((round(right - hdr.getlength(new_hdr)), xy_hdr[1]), new_hdr, font=hdr, fill=(255, 255, 255))
    img.save(out_path)
    print(f'{out_path}: {new_hdr} (old date matched {iou_big:.2f} and {iou_hdr:.2f})')


if __name__ == '__main__':
    main()
