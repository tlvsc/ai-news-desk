"""Step 6a. Build the day's Headlines pack from the checked scripts.

    python build_pack.py --workdir W

Reads W/headlines_work/scripts_final.json (7 stories, fun, teaser, Bigger Picture) and assets/pack_base.json
(Rafi's opening and ending of 2 Oct 2026, unchanged). Writes W/headlines_work/headlines_D-M-YY_pack.json:
C01 opening, C02-C08 stories, C09 fun, C10 teaser, C11 The Bigger Picture, C12 unused, C13 ending.
"""
import argparse, copy, json
from pathlib import Path
from common_b import B, edition_dates, entry, rules_gate

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--workdir', required=True)
W = Path(ap.parse_args().workdir)
rules_gate(W)   # GATE (Rafi, 4 Oct 2026): no Headlines pack from lines without a clean rules recheck
ed, short, title = edition_dates(W)
base = json.loads((B / 'assets' / 'pack_base.json').read_text(encoding='utf-8'))
fin = json.loads((W / 'headlines_work' / 'scripts_final.json').read_text(encoding='utf-8'))
fixed = {s['slot']: s for s in base.pop('slots_fixed')}
base.pop('note', None)
pack = copy.deepcopy(base)
pack.update(edition=ed, date_title=title,
            format=('13-slot template: C01 opening (Rafi\'s words and screen timeline, 2 Oct 2026); C02-C08 seven stories; C09 fun; '
                    'C10 teaser; C11 The Bigger Picture; C12 unused; C13 ending (Rafi\'s wording, 2 Oct 2026). Each clip aims at '
                    '8 seconds and may not pass 10 (Drive Headlines Master Section B item 1, 5 Oct 2026). Box times round up to the next half second.'),
            review_status=('Spoken lines follow the Drive phrasing file Headlines section (who, what and why in one flowing sentence, syllables the '
                           'measure), checked by check_wording.py, check_headlines_rules.py, a stranger check and a rules agent; approved by Rafael.'),
            source_check=f'Story lines were written from the Full Report entries of {ed}. Outlets are shown on screen, never spoken.',
            bigger_picture={'state': 'generated_in_C11', 'category': 'The Bigger Picture', 'source': 'AI News Desk',
                            'position': 'slot 11, after teaser, before the ending'})
slots = [fixed[1]]
for k, st in enumerate(fin['stories']):
    slots.append({'slot': 2 + k, 'kind': 'story', 'category': st['category_word'].title(), 'item': st['item'],
                  'symbol': st['screen'], 'script': st['script'], 'source': entry(W, st['item'])['source']})
f = fin['fun']
slots.append({'slot': 9, 'kind': 'fun', 'category': 'Fun', 'item': f['item'], 'symbol': f['screen'], 'script': f['script'],
              'source': entry(W, f['item'])['source']})
t = fin['teaser']
slots.append({'slot': 10, 'kind': 'teaser', 'category': 'Teaser', 'item': '; '.join(t['items']), 'symbol': t['screen'],
              'script': t['script'], 'source': 'DAILY GLOBAL AI INTELLIGENCE REPORT'})
b = fin['bp']
slots.append({'slot': 11, 'kind': 'story', 'category': 'The Bigger Picture', 'item': 'desk analysis', 'symbol': b['screen'],
              'script': b['script'], 'source': 'AI News Desk'})
slots.append({'slot': 12, 'kind': 'unused', 'state': 'bypass', 'title': f'unused (seven stories from {ed})'})
slots.append(fixed[13])
assert len(fin['stories']) == 7, f"7 story clips expected, got {len(fin['stories'])}"
pack['slots'] = slots
out = W / 'headlines_work' / f'headlines_{short}_pack.json'
out.write_text(json.dumps(pack, indent=1, ensure_ascii=False), encoding='utf-8')
print('pack written:', out, len(slots), 'slots')
