import hashlib
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
REF = Path(r'C:\Users\erans\AppData\Local\Temp\aind_drive\instagram_pixels_boundary_stirps_subtitles_FROM_DRIVE.png')
assert hashlib.sha256(REF.read_bytes()).hexdigest() == '8fd8477daba8a42ca8e7b8072eba83881a5d57b33ee888ce3abc7af50a99b410'
POLY = [(0, 284), (864, 284), (825, 393), (0, 393)]
ref = Image.open(REF).convert('RGB').resize((1080, 1920), Image.LANCZOS)
navy = min(ref.crop((100, 300, 700, 380)).getdata(), key=lambda p: sum(p)); white = ref.getpixel((40, 320))
rows = {y: ref.getpixel((300, y)) for y in range(380, 400)}; cyan = max(rows.values(), key=lambda p: p[2] - p[0])
layer = Image.new('RGBA', (1080, 1920), (0, 0, 0, 0)); d = ImageDraw.Draw(layer); d.polygon(POLY, fill=white + (255,))
for y in range(388, 393):
    xr = 864 - (864 - 825) * (y - 284) / (393 - 284); d.line([(0, y), (int(xr) - 1, y)], fill=cyan + (255,))
font = ImageFont.truetype(r'C:\Windows\Fonts\arialbi.ttf', 72); TEXT = 'SUN 11 OCT 2026'
bb = d.textbbox((0, 0), TEXT, font=font); h = bb[3] - bb[1]; y = 284 + (388 - 284 - h) // 2 - bb[1]
d.text((115, y), TEXT, font=font, fill=navy + (255,))
layer.save(r'C:\Users\erans\AppData\Local\Temp\aind_stitch11\date_overlay_11-10-26.png'); print('date ok', d.textbbox((115, y), TEXT, font=font))
