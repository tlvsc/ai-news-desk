"""Step 5a. Merge the checked card wording with the report entries into W/cards_copy.json.

    python build_cards_copy.py --workdir W

Reads W/cards_work/selection.json (the paper selection; each card has "card", "item", "category" and a short
"label", the second level of its CATEGORY line) and W/cards_work/cards_copy_fable.json (the checked wording).
Same structure as the cards_copy.json files since 27 Sep 2026, which make_cards.py reads.
Keep the CATEGORY line short: "Market, industry and finance / Robot start-ups" was too wide and the renderer
silently left that card out (3 Oct 2026); about 40 characters is safe.
"""
import argparse, json
from pathlib import Path
from common_b import entry, edition_dates

CLOSING = ('That was today’s headlines in cards. Soon, subscribers and followers will get access to our full daily report and '
           'industry analysis helping investors understand the bigger picture behind AI developments.\n\nIf this adds value to '
           'your day, share it with someone who should know. Thank you, and see you tomorrow.')   # approved 12 Sep 2026

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--workdir', required=True)
W = Path(ap.parse_args().workdir)
ed = edition_dates(W)[0]
sel = json.loads((W / 'cards_work' / 'selection.json').read_text())
fab = json.loads((W / 'cards_work' / 'cards_copy_fable.json').read_text())
by_card = {s['card']: s for s in fab['stories']}
cards = [{'id': 'cover', 'kind': 'cover'}]
for c in sel['cards_in_deck_order']:
    if c.get('label', 'SHORT LABEL') == 'SHORT LABEL':
        raise SystemExit(f"{c['card']}: write a short label in selection.json (step 1) before building")
    e, f = entry(W, c['item']), by_card[c['card']]
    assert f['item'] == c['item'], (c, f['item'])
    fun = c['card'] == 'fun'
    cat = ('Fun and humour' if fun else c['category']) + ' / ' + c['label']
    if len(cat) > 46:
        print(f'WARNING {c["card"]}: CATEGORY line "{cat}" is {len(cat)} characters; shorten the label')
    cards.append({'id': c['card'], 'kind': 'fun' if fun else 'story', 'item': c['item'], 'cat': cat,
                  'head': f['head'], 'body': f['body'], 'src': e['source'], 'pill': e['status'].upper(),
                  'coverage': {'robotics': c['category'] == 'Robotics', 'outside_business': not c['category'].startswith('Market')}})
t = {x['id']: x for x in fab['teaser']}
cards.append({'id': 'teaser', 'kind': 'teaser', 'entries': [
    {'id': x['id'], 'item': x['item'], 'cat': x['category'], 'head': t[x['id']]['head']} for x in sel['teaser_items']]})
cards.append({'id': 'bp', 'kind': 'analysis', 'opening': 'And for the bigger picture…', 'cat': 'The Bigger Picture / Desk view',
              'head': fab['bp']['head'], 'body': fab['bp']['body'], 'src': 'AI NEWS DESK', 'pill': 'DESK VIEW',
              'refs': sel['bp_refs']})
cards.append({'id': 'closing', 'kind': 'closing', 'head': 'Like, follow and share.', 'body': CLOSING})
out = {'edition': ed, 'note': 'Card wording written by Fable from the Full Report entries, checked by check_wording.py and a stranger check.',
       'cards': cards}
(W / 'cards_copy.json').write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding='utf-8')
print(len(cards), 'cards written to', W / 'cards_copy.json')
