"""Step 5d. Name the rendered cards by the filename rule and make the contact sheet.

    python assemble_cards.py --workdir W --run W/products/cards_runN

The cover (I01) comes from card_cover_adjusting_script.py and must already be in W/products/cards_D-M-YY/.
Card NN of the run becomes cards_D-M-YY_INN_VL1.png (rule of 13 Sep 2026). Stops when the number of cards differs
from cards_copy.json: a card the renderer refused (CROP) is otherwise silently missing (3 Oct 2026). Contact sheet:
five per row, cards_D-M-YY_contact_sheet.jpg.
"""
import argparse, json, shutil
from pathlib import Path
from PIL import Image
from common_b import edition_dates

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--workdir', required=True); ap.add_argument('--run', required=True)
a = ap.parse_args()
W, run = Path(a.workdir), Path(a.run)
short = edition_dates(W)[1]
out = W / 'products' / f'cards_{short}'; out.mkdir(parents=True, exist_ok=True)
cover = out / f'cards_{short}_I01_VL1.png'
expected = len(json.loads((W / 'cards_copy.json').read_text())['cards'])
rendered = sorted(run.glob('card_[0-9][0-9].png'))
man = json.loads((run / 'render_manifest.json').read_text())
refused = {k: v['errors'] for k, v in man['cards'].items() if v.get('errors') and k != 'cover'}
if refused or not cover.exists() or len(rendered) + 1 != expected:
    raise SystemExit(f'STOP: cover present={cover.exists()}, rendered {len(rendered)} + cover vs {expected} cards; refused: {refused}')
files = [cover]
for p in rendered:
    dst = out / f'cards_{short}_I{int(p.stem.split("_")[1]):02d}_VL1.png'
    shutil.copy2(p, dst); files.append(dst)
thumbs = [Image.open(f).convert('RGB').resize((270, 480)) for f in files]
cols = 5; rows = -(-len(thumbs) // cols)
sheet = Image.new('RGB', (cols * 276, rows * 486), (9, 19, 42))
for i, t in enumerate(thumbs):
    sheet.paste(t, ((i % cols) * 276 + 3, (i // cols) * 486 + 3))
sheet.save(out / f'cards_{short}_contact_sheet.jpg', quality=88)
print(len(files), 'cards in', out, '| sizes', {Image.open(f).size for f in files}, '| contact sheet', sheet.size)
