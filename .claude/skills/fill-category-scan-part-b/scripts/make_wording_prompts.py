"""Step 2a. Write the four agent prompts of part B from the briefs (wording and stranger check, cards and Headlines).

    python make_wording_prompts.py --workdir W [--prev-cards OLD_W/cards_copy.json] [--prev-pack OLD_PACK.json]

Writes W/cards_work/{wording_common.txt, prompt_cards.txt, prompt_stranger_cards.txt} and
W/headlines_work/{wording_common.txt, prompt_headlines.txt, prompt_stranger_headlines.txt, prompt_rules_headlines.txt}. Launch each agent with
"Read <that prompt file> and follow it exactly." The wording agents run on the Fable model (Agent tool, model "fable").
"""
import argparse, glob, re
from pathlib import Path
from common_b import B, edition_dates, prev_scripts
import json

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--workdir', required=True); ap.add_argument('--prev-cards'); ap.add_argument('--prev-pack')
a = ap.parse_args()
W = Path(a.workdir).resolve()
prev_runs = [p for p in sorted(glob.glob(str(W.parent / 'run_*'))) if Path(p) != W]
prev_cards = a.prev_cards or next((str(Path(p) / 'cards_copy.json') for p in reversed(prev_runs) if (Path(p) / 'cards_copy.json').exists()), 'none')
prev_pack = a.prev_pack or next((q for p in reversed(prev_runs) for q in sorted(glob.glob(str(Path(p) / 'headlines_work' / '*_pack.json')))),
                                str(B / 'assets' / 'pack_base.json'))
ps = prev_scripts(W)
def _intro(s):
    m = re.match(r'\s*([^.:!?]+)[.:]', s or ''); return m.group(1).strip() if m else ''
if ps:
    _p = json.loads(Path(ps).read_text())
    leadins = sorted({_intro(x['script']) for x in _p.get('stories', [])} | {_intro(_p.get('fun', {}).get('script', ''))})
else:
    leadins = []
v = {'WORKDIR': W, 'EDITION': edition_dates(W)[0], 'PREV_CARDS': prev_cards, 'PREV_PACK': prev_pack,
     'PREV_SCRIPTS': ps or 'none found', 'PREV_LEADINS': ', '.join(f'"{x}"' for x in leadins) or 'none found'}
fill = lambda name: re.sub(r'\{([A-Z_]+)\}', lambda m: str(v.get(m.group(1), m.group(0))), (B / 'briefs' / name).read_text(encoding='utf-8'))
for sub, files in (('cards_work', (('wording_common.txt', 'wording_common.md'), ('prompt_cards.txt', 'wording_cards.md'),
                                   ('prompt_stranger_cards.txt', 'stranger_cards.md'))),
                   ('headlines_work', (('wording_common.txt', 'wording_common.md'), ('prompt_headlines.txt', 'wording_headlines.md'),
                                       ('prompt_stranger_headlines.txt', 'stranger_headlines.md'),
                                       ('prompt_rules_headlines.txt', 'rules_check_headlines.md'),
                                       ('prompt_rewrite_headlines.txt', 'rewrite_headlines.md')))):
    (W / sub).mkdir(exist_ok=True)
    for out, brief in files:
        (W / sub / out).write_text(fill(brief), encoding='utf-8')
left = sorted({m for f in list((W / 'cards_work').glob('*.txt')) + list((W / 'headlines_work').glob('*.txt'))
               for m in re.findall(r'\{[A-Z_]+\}', f.read_text())})
print('prompts written to', W / 'cards_work', 'and', W / 'headlines_work', '| previous cards', prev_cards, '| previous pack', prev_pack,
      '| unfilled placeholders:', left or 'none')
