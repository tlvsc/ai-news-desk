"""Step 0b. Combine the pools of the last days into one repeat list for collect.py --yesterday.

    python combine_pools.py --workdir W --pool W/pool_2026-09-30.csv --pool .../AIND_Pool_2026-10-02.csv [...]

Each pool file name must hold its date (YYYY-MM-DD). Item ids get the day in front ("1002:C01-01"), so the
curators can name the earlier story in follow_up_of. Writes W/yesterday_pool.csv. Rafi, 3 Oct 2026: check
repeats against the last four days of pools, not only yesterday's.
"""
import argparse, csv, re
from pathlib import Path

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--workdir', required=True)
ap.add_argument('--pool', action='append', required=True, help='a pool CSV; give one --pool per day')
a = ap.parse_args()
rows, fields = [], []
for p in sorted(a.pool, key=lambda s: re.search(r'(\d{4})-(\d\d)-(\d\d)', Path(s).name).group(0)):
    m = re.search(r'(\d{4})-(\d\d)-(\d\d)', Path(p).name)
    tag = m.group(2) + m.group(3)
    with open(p, encoding='utf-8', newline='') as f:
        r = csv.DictReader(f)
        fields += [c for c in r.fieldnames if c not in fields]
        n = 0
        for x in r:
            x['item_id'] = f"{tag}:{x.get('item_id', '')}"; rows.append(x); n += 1
    print(f'{m.group(0)}: {n} stories')
out = Path(a.workdir) / 'yesterday_pool.csv'
with open(out, 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator='\n'); w.writeheader()
    for x in rows:
        w.writerow({k: x.get(k, '') for k in fields})
print('total', len(rows), '->', out)
