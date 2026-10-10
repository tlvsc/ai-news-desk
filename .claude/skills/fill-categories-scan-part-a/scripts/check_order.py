"""ORDER CHECK (Rafi, 10 Oct 2026: "the order never change again for any products").

    python3 check_order.py --workdir W        # step 12, before anything is sent; exits 1 on any FAIL

The approved order of categories (Drive Decision Log of 23 Sep 2026; common.ORDER: Politics and government first, The Fun Side last)
must hold in every product that lists categories: the Full Report, the Bulletin, the pool PDF, the pool CSV and JSON, daily-pool.md.
Cards and Headlines are checked by their own gate (pick_gate G7, check_headlines_rules A3).
"""
import argparse, csv, json, re
from pathlib import Path
import pymupdf
from common import CAT_SECTION, NAMES, ORDER, POOL_ORDER, load_run, pool_path, short_date, edition, categories

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--workdir', required=True)
W = Path(ap.parse_args().workdir)
run = load_run(W)
res = []


def chk(name, ok, why=''):
    res.append(bool(ok))
    print(('PASS ' if ok else 'FAIL ') + name + ('' if ok else ' :: ' + why))


def monotonic(seq):
    return all(a <= b for a, b in zip(seq, seq[1:]))


# 1 and 2: Full Report and Bulletin sections
for fn, label in (('report_pdf.json', 'Full Report'), ('bulletin_pdf.json', 'Bulletin')):
    p = W / 'products' / fn
    if p.exists():
        names = [c['name'] for c in json.loads(p.read_text(encoding='utf-8'))['categories']]
        idx = [list(NAMES.values()).index(n) if n in NAMES.values() else 99 for n in names]
        chk(f'{label} sections follow the approved order', monotonic(idx) and 99 not in idx, str(names))
# 3: pool JSON and CSV
pp = pool_path(W, run)
if pp.exists():
    pool = json.loads(pp.read_text(encoding='utf-8'))
    pos = [POOL_ORDER.index(int(x['category_id'])) for x in pool]
    chk('pool JSON follows the approved order', monotonic(pos), 'first rows: ' + str([x['category'] for x in pool[:3]]))
    cp = pp.with_suffix('.csv')
    for q in (cp, W / 'products' / cp.name):
        if q.exists():
            rows = list(csv.DictReader(open(q, encoding='utf-8')))
            pos = [POOL_ORDER.index(int(r['category_id'])) for r in rows]
            chk(f'pool CSV {q.parent.name}/{q.name} follows the approved order', monotonic(pos), 'first row: ' + rows[0]['category'])
# 4: pool PDF headings
ed = edition(run)
pdf = W / 'products' / f"AIND_Pool_{short_date(ed)}.pdf"
if pdf.exists():
    text = ''.join(p.get_text() for p in pymupdf.open(str(pdf)))
    cats = categories()
    where = []
    for cid in POOL_ORDER:
        v = cats.get(str(cid)) or cats.get(cid)
        nm = (v[0] if isinstance(v, list) else str(v)).split(' (')[0].split('. ')[0].rstrip('.')
        m = re.search(r'(?m)^' + re.escape(nm) + r' \(\d+\)', text)
        where.append(m.start() if m else -1)
    chk('pool PDF headings follow the approved order', all(w >= 0 for w in where) and monotonic(where), str(where))
# 5: daily-pool.md
md = W / 'products' / 'daily-pool.md'
if md.exists():
    seq = []
    for line in md.read_text(encoding='utf-8').splitlines():
        m = re.match(r'- C\d\d-\d\d · ([A-Z]{3}) · ', line)
        if m and m.group(1) in ORDER:
            seq.append(ORDER.index(m.group(1)))
    chk('daily-pool.md follows the approved order', bool(seq) and monotonic(seq), 'sequence breaks')
print('order check:', 'all pass' if all(res) else f'{res.count(False)} FAIL')
raise SystemExit(0 if all(res) else 1)
