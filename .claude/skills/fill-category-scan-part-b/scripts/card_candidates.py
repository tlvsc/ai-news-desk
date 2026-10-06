"""Step 1. Choose the cards and the Headlines stories from the final Full Report with the CARD FILTER, and write a draft selection.

    python card_candidates.py --workdir W [--previous OLD_cards_copy.json ...]

ONE SOURCE OF TRUTH (Rafi, 6 Oct 2026): this script holds no card numbers and no category order.
- The numbers (base_min, extra_min, target, max_per_category, market_max, company limits) are read from the line
  "CARD_FILTER: ..." of CLAUDE.md rule 16, where the CARD FILTER is written in words.
- The category order is read from the Drive Cards Master copy W/rules/Cards_Master_Rules_Structure.txt (Section 2 item 4).
- The Headlines stories follow the Drive Headlines Master (Section A items 3 and 8): the strongest card stories by score, shown in deck order,
  normally with a robotics story and one law, research or society story; company clip limit from the CARD FILTER line.
The filter: critical stories (10) first; every category keeps its best story if it scores base_min or more; fun last; the remaining slots up to
target go to the highest scored stories left that score extra_min or more (max_per_category, market_max); stories read in full only; a robotics
card shows a machine doing something; an UPDATE (freshness FOLLOW-UP) is a candidate, and the main session keeps it only when the update is
meaningful (it then names the earlier story). The script prints every pick, the LEFT OUT list (score 6 and up) with the reason, big company names
and possible repeats of the last three decks, and writes W/cards_work/selection_draft.json (labels still to write).
"""
import argparse, glob, json, re
from pathlib import Path
from common_b import B, entry, edition_dates

REPO = B.parent.parent.parent
CODE = {'Politics': 'POL', 'Market': 'MKT', 'Security': 'SEC', 'Energy': 'ENE', 'Robotics': 'ROB', 'Models': 'MOD', 'Research': 'RES',
        'Ethics': 'LAW', 'Health': 'HEA', 'Society': 'SOC', 'Fun': 'FUN'}
NAME = {'POL': 'Politics and government', 'MKT': 'Market, industry and finance', 'SEC': 'Security and cyber',
        'ENE': 'Energy and infrastructure', 'ROB': 'Robotics', 'MOD': 'Models and tools', 'RES': 'Research and science',
        'LAW': 'Ethics and law', 'HEA': 'Health', 'SOC': 'Society and education', 'FUN': 'The Fun Side'}
COMPANIES = ['OpenAI', 'Anthropic', 'Google', 'Alphabet', 'Meta', 'Microsoft', 'Apple', 'Amazon', 'Nvidia', 'Tesla', 'xAI',
             'Samsung', 'Oracle', 'Broadcom', 'Intel', 'AMD', 'TSMC', 'Alibaba', 'DeepSeek', 'Palantir', 'Moonshot', 'Qualcomm', 'Arm', 'TikTok']
STOP = set('the a an and of to in on for is are was with that this it its as by at from be has have will may says say new more '
           'over after about their they than but not or into up out just also'.split())


def keys(t):
    return {w for w in re.findall(r"[a-z][a-z0-9']{3,}", t.lower()) if w not in STOP}


def read_filter():
    m = re.search(r'CARD_FILTER:\s*(.+)', (REPO / 'CLAUDE.md').read_text(encoding='utf-8'))
    if not m:
        raise SystemExit('STOP: the line "CARD_FILTER: ..." is missing in CLAUDE.md rule 16')
    f = {k: int(v) for k, v in re.findall(r'(\w+)=(\d+)', m.group(1))}
    need = {'base_min', 'extra_min', 'target', 'max_per_category', 'market_max', 'company_cards', 'company_clips'}
    if need - set(f):
        raise SystemExit(f'STOP: CARD_FILTER misses {sorted(need - set(f))}')
    return f


def read_order(W):
    p = W / 'rules' / 'Cards_Master_Rules_Structure.txt'
    if not p.exists():
        raise SystemExit(f'STOP: {p} missing (fetch it in step 0)')
    t = p.read_text(encoding='utf-8')
    a = t.find('CATEGORY ORDER'); b = t.find('Inside a category', a)
    seg = t[a:b] if a >= 0 and b > a else ''
    names = re.findall(r'(?<!\d)\d{1,2} ([A-Z][A-Za-z ,]*?) \(\d', seg)
    order = [CODE[next(k for k in CODE if n.startswith(k))] for n in names if any(n.startswith(k) for k in CODE)]
    if order != ['POL', 'MKT', 'SEC', 'ENE', 'ROB', 'MOD', 'RES', 'LAW', 'HEA', 'SOC', 'FUN'][:len(order)] and len(order) != 11:
        print('NOTICE: category order read from the Drive file:', order)
    if len(order) != 11 or order[-1] != 'FUN':
        raise SystemExit(f'STOP: could not read the 11 categories from the Drive Cards Master Section 2 item 4 (got {order})')
    return order


ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--workdir', required=True)
ap.add_argument('--previous', action='append', default=[], help='cards_copy.json of earlier days (default: the 3 latest earlier runs, scratchpad siblings then runs/ of the repo)')
a = ap.parse_args()
W = Path(a.workdir).resolve()
F = read_filter(); ORDER = read_order(W)
print('CARD FILTER read from CLAUDE.md:', F, '\ncategory order read from the Drive Cards Master:', ORDER)
ed = edition_dates(W)[0]
prev = a.previous
if not prev:
    cands = sorted(glob.glob(str(W.parent / 'run_*' / 'cards_copy.json'))) + sorted(glob.glob(str(REPO / 'runs' / '*' / 'cards_copy.json')))
    byday = {}
    for p in cands:
        d = Path(p).parent.name.replace('run_', '')
        if d < ed: byday[d] = p
    prev = [byday[d] for d in sorted(byday)[-3:]]
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
cand = []
for c in rp['categories']:
    for it in c['items']:
        e = heads[it['headline']]
        k = e['v1_category']
        rep = max(((len(keys(it['headline']) & keys(o)) / max(1, len(keys(it['headline']))), d) for d, o in old), default=(0, ''))
        cand.append(dict(id=e['item_id'], k=k, s=int(it['score']), upd=e['freshness'] != 'NEW', fresh=e['freshness'], read=bool(e['verified_text']),
                         mach=e.get('machine_action'), status=e['status'], head=it['headline'],
                         comp=[x for x in COMPANIES if re.search(rf'\b{x}\b', it['headline'])], rep=rep))
cand_nf = [x for x in cand if x['k'] != 'FUN']
why = {}
ok = lambda x: x['read'] and (x['k'] != 'ROB' or x['mach'] is not False)
chosen, cnt = [], {}
def capk(k): return F['market_max'] if k == 'MKT' else F['max_per_category']
def can(x):
    if sum(1 for y in chosen if y['k'] == x['k']) >= capk(x['k']): why[x['id']] = 'category full'; return False
    if any(cnt.get(c, 0) >= F['company_cards'] for c in x['comp']): why[x['id']] = 'company limit ' + '/'.join(x['comp']); return False
    return True
def take(x):
    chosen.append(x)
    for c in x['comp']: cnt[c] = cnt.get(c, 0) + 1
crit = [x for x in cand_nf if x['s'] >= 10 and ok(x)]
print('critical stories:', [x['id'] for x in crit] or 'none')
for x in sorted(crit, key=lambda x: -x['s']):
    if can(x): take(x)
for k in ORDER[:-1]:
    if any(y['k'] == k for y in chosen): continue          # a critical already spent this category's slot
    best = sorted([x for x in cand_nf if x['k'] == k and ok(x) and x['s'] >= F['base_min'] and x not in chosen], key=lambda x: (-x['s'], x['upd']))
    if best and can(best[0]): take(best[0])
extras = sorted([x for x in cand_nf if x not in chosen and ok(x) and x['s'] >= F['extra_min']], key=lambda x: (-x['s'], ORDER.index(x['k']), x['upd']))
for x in extras:
    if len(chosen) >= F['target']:
        why.setdefault(x['id'], 'target reached'); continue
    if can(x): take(x)
deck = sorted(chosen, key=lambda x: (ORDER.index(x['k']), -x['s']))
fun = sorted([x for x in cand if x['k'] == 'FUN' and x['read']], key=lambda x: -x['s'])
print(f"\nCARD FILTER DECK: {len(deck)} story cards (target {F['target']}) + fun")
for i, x in enumerate(deck, 1):
    print(f"{i:2} {x['k']} s{x['s']} {x['id']} {'UPDATE ' + x['fresh'] if x['upd'] else 'NEW'} {x['status'][:4]}"
          f"{' companies=' + ','.join(x['comp']) if x['comp'] else ''}{f' MAYBE REPEAT of {x[chr(114)+chr(101)+chr(112)][1]} ({x[chr(114)+chr(101)+chr(112)][0]:.2f})' if x['rep'][0] >= 0.35 else ''} | {x['head'][:90]}")
print('per category:', {k: sum(1 for y in deck if y['k'] == k) for k in ORDER[:-1]}, '| company cards:', cnt)
if fun: print(f"fun: {fun[0]['id']} s{fun[0]['s']} | {fun[0]['head'][:90]}")
# Headlines (Drive Headlines Master Section A items 3 and 8): the strongest card stories by score, shown in deck order;
# normally keep robotics and one law, research or society story; company clip limit from the CARD FILTER line.
pool = sorted(deck, key=lambda x: (-x['s'], ORDER.index(x['k']), x['upd']))
hl, hc = [], {}
hok = lambda x: all(hc.get(c, 0) < F['company_clips'] for c in x['comp'])
def hadd(x):
    hl.append(x)
    for c in x['comp']: hc[c] = hc.get(c, 0) + 1
for x in pool:
    if len(hl) < 7 and hok(x): hadd(x)
def ensure(cats):
    if any(x['k'] in cats for x in hl): return
    for x in pool:
        if x['k'] in cats and x not in hl:
            if any(c in hc and hc[c] >= F['company_clips'] for c in x['comp']): continue
            weak = sorted(hl, key=lambda y: (y['s'], -ORDER.index(y['k'])))
            drop = next((y for y in weak if sum(1 for z in hl if z['k'] == y['k']) > 1), next((y for y in weak if y['k'] not in ('ROB',)), None))
            if drop:
                hl.remove(drop)
                for c in drop['comp']: hc[c] -= 1
                hadd(x); return
ensure({'ROB'}); ensure({'LAW', 'RES', 'SOC'})
hl = sorted(hl, key=lambda x: (ORDER.index(x['k']), -x['s']))
print('HEADLINES (strongest card stories, deck order):', [(x['id'], x['k'], x['s']) for x in hl], '| company clips', hc)
# teaser: strongest stories without a card, distinct categories, read in full
left = sorted([x for x in cand_nf if x not in chosen], key=lambda x: (-x['s'], ORDER.index(x['k'])))
teaser, tc = [], set()
for x in left:
    if x['read'] and x['k'] not in tc and len(teaser) < 4 and x['s'] >= 6:
        tc.add(x['k']); teaser.append(x)
for x in left:
    if x['s'] < 5 or x['id'] in why: continue
    if x['read'] is False: why[x['id']] = 'not read in full'
    elif x['k'] == 'ROB' and x['mach'] is False: why[x['id']] = 'robotics card needs a machine doing something'
    elif x['s'] < F['extra_min'] and any(y['k'] == x['k'] for y in chosen): why[x['id']] = f"below extra_min ({F['extra_min']}) and the category has its card"
    else: why[x['id']] = why.get(x['id'], 'lost to higher scores')
print('\nLEFT OUT with score 6 and up (why):')
for x in [x for x in left if x['s'] >= 6]:
    print(f"   s{x['s']} {x['id']} {x['k']} {'UPDATE' if x['upd'] else 'NEW'} | {why.get(x['id'], '?')} | {x['head'][:80]}")
draft = {'cards_in_deck_order': [], 'teaser_items': [], 'headlines_story_clips_in_order': [x['id'] for x in hl],
         'headlines_fun': fun[0]['id'] if fun else None, 'bp_refs': []}
for i, x in enumerate(deck, 1):
    draft['cards_in_deck_order'].append({'card': f's{i}', 'item': x['id'], 'category': NAME[x['k']], 'label': 'SHORT LABEL',
                                         'type': 'UPDATE' if x['upd'] else 'NEW', 'fresh': x['fresh'], 'score': x['s']})
if fun:
    draft['cards_in_deck_order'].append({'card': 'fun', 'item': fun[0]['id'], 'category': NAME['FUN'], 'label': 'SHORT LABEL',
                                         'type': 'UPDATE' if fun[0]['upd'] else 'NEW', 'fresh': fun[0]['fresh'], 'score': fun[0]['s']})
for i, x in enumerate(teaser, 1):
    draft['teaser_items'].append({'id': f't{i}', 'item': x['id'], 'category': NAME[x['k']]})
draft['bp_refs'] = [x['id'] for x in sorted((x for x in cand_nf if x['k'] in ('MKT', 'ENE')), key=lambda x: -x['s'])[:3]]
(W / 'cards_work').mkdir(exist_ok=True)
(W / 'cards_work' / 'selection_draft.json').write_text(json.dumps(draft, indent=1, ensure_ascii=False))
print(f"\ndraft: {len(deck)} story cards + fun, {len(hl)} Headlines stories, teaser {[t['item'] for t in draft['teaser_items']]}, "
      f"bp_refs {draft['bp_refs']} -> W/cards_work/selection_draft.json (labels, update notes and bp_refs still to write)")
