"""Step 5b. Turn W/cards_copy.json into the card renderer's edition and content lock (same format since 27 Sep 2026).

    python make_cards.py --workdir W        (after part A's final build_products.py)

Writes W/products/cards_edition.json and W/products/cards_content_lock.json, and prints the head and body length of
every card and any sentence lifted word for word from the report.
"""
import argparse, copy, glob, hashlib, json, re
from pathlib import Path

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--workdir', required=True)
W = Path(ap.parse_args().workdir)
run = json.loads((W / 'run.json').read_text())
ed = run['edition']
REPORT_MD = Path(glob.glob(str(W / 'products' / f'{ed} — Daily Global AI Intelligence Report*.md'))[0])
rep_text = REPORT_MD.read_text(encoding='utf-8')
flat = [it['headline'] for c in json.loads((W / 'products' / 'report_pdf.json').read_text())['categories'] for it in c['items']]
num = {h: i for i, h in enumerate(flat, 1)}
head = {f.stem: json.loads(f.read_text())['headline'] for f in (W / 'report_entries').glob('C*.json')}


def ref(item):
    h = head[item]
    if h not in num:
        raise SystemExit(f'{item} is not in the final report: {h[:80]}')
    assert h in rep_text
    return {'item': num[h], 'excerpt': h}


cc = json.loads((W / 'cards_copy.json').read_text())
cards = []
for c in cc['cards']:
    c = copy.deepcopy(c)
    if c['kind'] in ('story', 'fun'):
        c['report_refs'] = [ref(c.pop('item'))]
    elif c['kind'] == 'teaser':
        for t in c['entries']:
            t['kind'] = 'teaser_item'
            t['report_refs'] = [ref(t.pop('item'))]
    elif c['kind'] == 'analysis':
        c['report_refs'] = [ref(i) for i in c.pop('refs')]
        c['coverage'] = {'robotics': False, 'outside_business': True}
        c['notice'] = 'General news and commentary. Not financial advice or an investment recommendation.'
    cards.append(c)

n_story = sum(1 for c in cards if c['kind'] == 'story')
edition = {'edition': ed, 'report_file': str(REPORT_MD), 'report_sha256': hashlib.sha256(REPORT_MD.read_bytes()).hexdigest(),
           'destinations': ["Instagram @Ai_news_desk (pending Rafael's publication approval)"],
           'template': {'headline_size': 68, 'body_size': 40}, 'cards': cards, 'derivatives': [],
           'editorial_exceptions': {
               'card_count': {'reason': f'{len(cards)} cards with {n_story} story cards; Rafi, 30 Sep 2026: aim for 14 to 15 story cards, at most 20 cards.', 'notification_reference': 'Rafael chat 30 Sep 2026'}
               }}
lock = dict(copy.deepcopy(edition), selection_reference=f'Claude deck selection {ed}, cards_copy.json', copy_reference=f'cards_copy.json, {ed}')
(W / 'products' / 'cards_edition.json').write_text(json.dumps(edition, indent=1, ensure_ascii=False), encoding='utf-8')
(W / 'products' / 'cards_content_lock.json').write_text(json.dumps(lock, indent=1, ensure_ascii=False), encoding='utf-8')

SENT = re.compile(r'[.!?](\s|$)')
for c in cards:
    for x in ([c] if c['kind'] != 'teaser' else c['entries']):
        if 'head' not in x:
            continue
        lift = [s for s in re.split(r'(?<=[.!?])\s', x['head'] + ' ' + x.get('body', '')) if len(s) > 40 and s.strip() in rep_text]
        print(x['id'], 'head', len(x['head']), 'body', len(x.get('body', '')), 'LIFTED FROM REPORT' if lift else '')
print(len(cards), 'cards,', n_story, 'story cards')
