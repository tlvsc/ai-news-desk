"""SUPERSEDED 6 Oct 2026 (Rafi): replaced by card_candidates.py (the CARD FILTER). Kept only because superseded files are renamed _old, never removed. DO NOT RUN.

Step 1. List the card and Headlines candidates from the final Full Report and write a draft selection.

    python card_candidates.py --workdir W [--previous OLD_W/cards_copy.json ...]

Cards rules (Cards_Master_Rules_Structure.txt section 2, CLAUDE.md rule 16): critical stories (score 10) first, each
spending its category's slot; then Rafi's category order with its slots: Politics 1, Market 3, Security 1, Energy 1,
Robotics 1, Models 1, Research 1, Ethics and law 1, Health 1, Society 1, Fun 1 (always the last story card). For 14 to
15 story cards add one more Security and one more Energy card. Money cards (market slots plus money criticals) at most 3.
The robotics card shows a machine doing something. Only stories whose freshness is NEW (3 Oct 2026: follow ups of a
card story go to the Bigger Picture or the teaser). One company at most 3 story cards and 2 Headlines stories.
Prints the candidates per category, flags repeats of earlier decks, and writes W/cards_work/selection_draft.json.
Read it, change what the rules or judgement say, and save it as W/cards_work/selection.json.
"""
import argparse, glob, json, re
from pathlib import Path
from common_b import entry

ORDER = ['POL', 'MKT', 'SEC', 'ENE', 'ROB', 'MOD', 'RES', 'LAW', 'HEA', 'SOC', 'FUN']
SLOTS = {'POL': 1, 'MKT': 3, 'SEC': 2, 'ENE': 2, 'ROB': 1, 'MOD': 1, 'RES': 1, 'LAW': 1, 'HEA': 1, 'SOC': 1, 'FUN': 1}
NAME = {'POL': 'Politics and government', 'MKT': 'Market, industry and finance', 'SEC': 'Security and cyber',
        'ENE': 'Energy and infrastructure', 'ROB': 'Robotics', 'MOD': 'Models and tools', 'RES': 'Research and science',
        'LAW': 'Ethics and law', 'HEA': 'Health', 'SOC': 'Society and education', 'FUN': 'The Fun Side'}
COMPANIES = ['OpenAI', 'Anthropic', 'Google', 'Alphabet', 'Meta', 'Microsoft', 'Apple', 'Amazon', 'Nvidia', 'Tesla', 'xAI',
             'Samsung', 'Oracle', 'Broadcom', 'Intel', 'AMD', 'TSMC', 'Alibaba', 'DeepSeek', 'Palantir']
STOP = set('the a an and of to in on for is are was with that this it its as by at from be has have will may says say new more '
           'over after about their they than but not or into up out just also'.split())


def keys(t):
    return {w for w in re.findall(r"[a-z][a-z0-9']{3,}", t.lower()) if w not in STOP}


ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--workdir', required=True)
ap.add_argument('--previous', action='append', default=[], help='cards_copy.json of an earlier day (default: the 3 sibling run folders before this one)')
a = ap.parse_args()
W = Path(a.workdir)
prev = a.previous or sorted(glob.glob(str(W.parent / 'run_*' / 'cards_copy.json')))
prev = [p for p in prev if Path(p).parent != W][-3:]
old = []
for p in prev:
    for c in json.loads(Path(p).read_text())['cards']:
        for x in ([c] if 'head' in c else c.get('entries', [])):
            if 'head' in x:
                old.append((Path(p).parent.name, x['head'] + ' ' + x.get('body', '')))
rp = json.loads((W / 'products' / 'report_pdf.json').read_text())
heads = {}
for f in (W / 'report_entries').glob('C*.json'):
    e = json.loads(f.read_text(encoding='utf-8')); heads[e['headline']] = e
cand = {k: [] for k in ORDER}
for c in rp['categories']:
    for it in c['items']:
        e = heads[it['headline']]
        cand[e['v1_category']].append(dict(id=e['item_id'], score=it['score'], fresh=e['freshness'], vt=e['verified_text'],
                                           status=e['status'], head=it['headline'], machine=e.get('machine_action')))
crit = [x for k in ORDER for x in cand[k] if x['score'] >= 10 and x['fresh'] == 'NEW']
print('critical stories:', [x['id'] for x in crit] or 'none')
draft = {'cards_in_deck_order': [], 'teaser_items': [], 'headlines_story_clips_in_order': [], 'headlines_fun': None, 'bp_refs': []}
used, n = set(), 0
cat_of = {x['id']: k for k in ORDER for x in cand[k]}


def add(x, k):
    global n
    used.add(x['id'])
    if k == 'FUN':
        card = 'fun'
    else:
        n += 1; card = f's{n}'
    draft['cards_in_deck_order'].append({'card': card, 'item': x['id'], 'category': NAME[k], 'label': 'SHORT LABEL'})


for x in sorted(crit, key=lambda x: -x['score']):
    add(x, cat_of[x['id']])
for k in ORDER:
    new = [x for x in cand[k] if x['fresh'] == 'NEW' and x['id'] not in used]
    print(f'\n## {NAME[k]} ({len(cand[k])} in report, {len(new)} NEW, slots {SLOTS[k]})')
    for x in new[:6]:
        comp = [c for c in COMPANIES if re.search(rf'\b{c}\b', x['head'])]
        rep = max(((len(keys(x['head']) & keys(o)) / max(1, len(keys(x['head']))), d) for d, o in old), default=(0, ''))
        print(f"  {x['id']} s{x['score']} {x['status'][:4]} {'read' if x['vt'] else 'HEADLINE ONLY'}"
              f"{' machine action' if x['machine'] else (' NO machine action' if k == 'ROB' and x['machine'] is False else (' machine action unknown' if k == 'ROB' else ''))}"
              f"{' companies=' + ','.join(comp) if comp else ''}{f' MAYBE REPEAT of {rep[1]} ({rep[0]:.2f})' if rep[0] >= 0.35 else ''}"
              f" | {x['head'][:110]}")
    free = SLOTS[k] - sum(1 for x in crit if cat_of[x['id']] == k)
    ranked = [y for y in new if y['vt']] + [y for y in new if not y['vt']]
    if k == 'ROB':   # the robotics card shows a machine doing something (Cards rules section 2; writer flag machine_action)
        ranked = [y for y in ranked if y['machine']] + [y for y in ranked if y['machine'] is None] + [y for y in ranked if y['machine'] is False]
    picks = ranked[:max(0, free)]
    for x in picks:
        add(x, k)
# HEADLINES: the only rule is the Drive file Headlines_Master_Rules_Structure.txt ("General order of categories" and Section A
# item 3): criticals lead regardless of category, then the deck in the category list order (ORDER above, Politics first), one clip
# per category until seven. Nothing here reinterprets that file (Rafi, 5 Oct 2026, one source of truth).
score_of = {x['id']: x['score'] for k in cand for x in cand[k]}
crit = [c for c in draft['cards_in_deck_order'] if c['card'] != 'fun' and score_of.get(c['item'], 0) >= 10]
picks = [c['item'] for c in crit]
for k in ORDER:
    if k == 'FUN' or len(picks) >= 7: continue
    first = next((c for c in draft['cards_in_deck_order'] if c['category'] == NAME[k] and c['item'] not in picks), None)
    if first: picks.append(first['item'])
pos = {c['item']: i for i, c in enumerate(draft['cards_in_deck_order'])}
draft['headlines_story_clips_in_order'] = sorted(picks[:7], key=lambda i: pos[i])
fun = next((c for c in draft['cards_in_deck_order'] if c['card'] == 'fun'), None)
draft['headlines_fun'] = fun and fun['item']
rest = sorted((x for k in ORDER if k != 'FUN' for x in cand[k] if x['id'] not in used and x['fresh'] == 'NEW'),
              key=lambda x: -x['score'])
cats_t, i = set(), 0
for x in rest:
    k = next(k for k in ORDER if x in cand[k])
    if k not in cats_t and len(draft['teaser_items']) < 4:
        i += 1; cats_t.add(k); draft['teaser_items'].append({'id': f't{i}', 'item': x['id'], 'category': NAME[k]})
draft['bp_refs'] = [x['id'] for x in sorted((x for k in ('MKT', 'ENE') for x in cand[k]), key=lambda x: -x['score'])[:3]]
(W / 'cards_work').mkdir(exist_ok=True)
(W / 'cards_work' / 'selection_draft.json').write_text(json.dumps(draft, indent=1, ensure_ascii=False))
print(f"\ndraft: {len(draft['cards_in_deck_order'])} cards ({n} story + fun), "
      f"{len(draft['headlines_story_clips_in_order'])} Headlines stories, teaser {[t['item'] for t in draft['teaser_items']]}, "
      f"bp_refs {draft['bp_refs']} -> W/cards_work/selection_draft.json (labels still to write)")
