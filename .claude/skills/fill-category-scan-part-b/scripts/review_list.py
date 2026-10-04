"""Step 7. Write the approval list for Rafi: every Headlines clip, the spoken words in bold and the blue holographic
screen beside them, plus the card wording.

    python review_list.py --workdir W

Reads W/headlines_work/headlines_D-M-YY_pack.json and W/cards_copy.json; writes W/headlines_work/review_list.md
and prints it, so it can be pasted into the chat next to the contact sheet. Opening and ending screens are the
timelines inside their prompts.
"""
import argparse, json, re
from pathlib import Path
from common_b import edition_dates

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--workdir', required=True)
W = Path(ap.parse_args().workdir)
short = edition_dates(W)[1]
pack = json.loads((W / 'headlines_work' / f'headlines_{short}_pack.json').read_text(encoding='utf-8'))
L = ['**Headlines: spoken words and the blue holographic screen.** In every story clip the logo changes slowly to one '
     'simple picture inside the blue border, no text and no people, then returns to the logo.', '']
n = 0
for s in pack['slots']:
    if s.get('state') == 'bypass':
        continue
    n += 1
    if s.get('prompt'):
        m = re.search(r'Hologram screen timeline.*?(?=The screen content)', s['prompt'], re.S)
        screen = m.group(0).strip() if m else s.get('symbol', '')
    else:
        screen = s['symbol'].replace(', simple text-free symbol', '')
    L.append(f"{n}. {s['category']}: **{s['script']}** Screen: {screen}")
cards = json.loads((W / 'cards_copy.json').read_text(encoding='utf-8'))['cards']
L += ['', '**Cards wording** (headline, then the text under it)', '']
k = 0
for c in cards:
    for x in ([c] if 'head' in c else c.get('entries', [])):
        if 'head' not in x or c['kind'] in ('closing',):
            continue
        k += 1
        L.append(f"{k}. {x.get('cat', c.get('cat', ''))}: **{x['head']}** {x.get('body', '')}".rstrip())
text = '\n'.join(L)
(W / 'headlines_work' / 'review_list.md').write_text(text + '\n', encoding='utf-8')
print(text)
