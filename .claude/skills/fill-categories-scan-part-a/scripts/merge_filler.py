"""Step 3b. Put a filler curator's items into the category file, after the main picks and before the backups.

    python merge_filler.py --workdir W --cat 13

Reads W/pool/cat_NN_extra.json, keeps the old category file as W/pool_cat_NN_before_filler_old.json (no deletions),
writes W/pool/cat_NN.json with ranks renumbered (main picks, then the filler items as main picks, then the backups)
and renames the extra file to W/pool_cat_NN_extra_old.json. Then run build_pool.py again.
"""
import argparse, json, shutil
from pathlib import Path

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--workdir', required=True); ap.add_argument('--cat', type=int, required=True)
a = ap.parse_args()
W = Path(a.workdir); nn = f'{a.cat:02d}'
cat, extra = W / 'pool' / f'cat_{nn}.json', W / 'pool' / f'cat_{nn}_extra.json'
items = sorted(json.loads(cat.read_text(encoding='utf-8')), key=lambda x: x.get('rank', 99))
add = json.loads(extra.read_text(encoding='utf-8'))
titles = {i['title'].strip().lower() for i in items}
add = [x for x in add if x['title'].strip().lower() not in titles]
shutil.copy2(cat, W / f'pool_cat_{nn}_before_filler_old.json')
mains = [i for i in items if not i.get('backup')]; backups = [i for i in items if i.get('backup')]
for x in add:
    x.update(category_id=a.cat, backup=False, filler=True)
merged = mains + add + backups
for n, x in enumerate(merged, 1):
    x['rank'] = n
cat.write_text(json.dumps(merged, indent=1, ensure_ascii=False), encoding='utf-8')
extra.rename(W / f'pool_cat_{nn}_extra_old.json')
print(f'cat {nn}: {len(mains)} main + {len(add)} filler + {len(backups)} backup = {len(merged)}; now run build_pool.py again')
