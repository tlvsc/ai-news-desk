"""Step 5 (first). Make the cover card: the approved cover with only the date changed (Cards rules, section 6).

    python make_cover.py --workdir W [--pkg <scratchpad>/cards_pkg]

Calls the repo's scripts/card_cover_adjusting_script.py with the approved base
(<pkg>/drive_refs/cards_13-9-26_I01_VL1_presenter_preview.png) and the card fonts (<pkg>/AIND_Cards_2026-09-10/
assets/fonts), and writes W/products/cards_D-M-YY/cards_D-M-YY_I01_VL1.png. --pkg defaults to W/../cards_pkg.
"""
import argparse, subprocess, sys
from pathlib import Path
from common_b import COVER_SCRIPT, edition_dates

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--workdir', required=True); ap.add_argument('--pkg')
a = ap.parse_args()
W = Path(a.workdir).resolve(); pkg = Path(a.pkg) if a.pkg else W.parent / 'cards_pkg'
ed, short, _ = edition_dates(W)
out = W / 'products' / f'cards_{short}'; out.mkdir(parents=True, exist_ok=True)
base = pkg / 'drive_refs' / 'cards_13-9-26_I01_VL1_presenter_preview.png'
fonts = pkg / 'AIND_Cards_2026-09-10' / 'assets' / 'fonts'
for p in (base, fonts):
    if not p.exists():
        raise SystemExit(f'missing {p}: fetch it in step 0')
sys.exit(subprocess.call([sys.executable, str(COVER_SCRIPT), ed, '--base', str(base), '--fonts', str(fonts),
                          '--out', str(out / f'cards_{short}_I01_VL1.png')]))
