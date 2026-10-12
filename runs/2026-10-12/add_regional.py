"""Run-folder helper (12 Oct 2026, not part of the repo scripts): add stories found by a regional search to the final pool
WITHOUT rebuilding it, so the item numbers of the written entries do not shift (SKILL step 3, adding a story by hand).

    python add_regional.py WORKDIR CAT IDX [IDX ...]      (IDX = position in pool/cat_CC_regional.json, from 0)

Backs up out/ once as out_before_regional_old/, gives the new rows the next free ids of the category (C10-16 ...),
re-sorts the pool exactly as build_pool.py does and writes the JSON and the CSV the same way.
"""
import csv, json, shutil, sys
from pathlib import Path

W = Path(sys.argv[1]); cat = int(sys.argv[2]); idxs = [int(x) for x in sys.argv[3:]]
sys.path.insert(0, '/home/user/ai-news-desk/.claude/skills/fill-categories-scan-part-a/scripts')
from common import POOL_ORDER  # noqa: E402

edition = json.loads((W / 'run.json').read_text())['edition']
pj = W / 'out' / f'AIND_Pool_{edition}.json'
if not (W / 'out_before_regional_old').exists():
    shutil.copytree(W / 'out', W / 'out_before_regional_old')
pool = json.loads(pj.read_text(encoding='utf-8'))
src = json.loads((W / 'pool' / f'cat_{cat:02d}_regional.json').read_text(encoding='utf-8'))
catname = next(p['category'] for p in pool if int(p['category_id']) == cat)
nums = [int(p['item_id'].split('-')[1]) for p in pool if int(p['category_id']) == cat]
nxt = max(nums) + 1
titles = {p['title'].strip().lower() for p in pool}
for i in idxs:
    it = dict(src[i])
    if it['title'].strip().lower() in titles:
        sys.exit(f'already in the pool: {it["title"]}')
    it.update(item_id=f'C{cat:02d}-{nxt:02d}', pool_rank=nxt, category=catname, from_backup=False, backup=False,
              date_check=it.get('date_check', 'datetime'), regional_search=True)
    pool.append(it)
    print('added', it['item_id'], it['importance'], it['source'], '|', it['title'][:90])
    nxt += 1
pool.sort(key=lambda it: (POOL_ORDER.index(int(it['category_id'])), -int(float(it.get('importance') or 0)), int(it.get('pool_rank') or 99)))
pj.write_text(json.dumps(pool, indent=2, ensure_ascii=False), encoding='utf-8')
cols = ["item_id", "category_id", "category", "pool_rank", "title", "summary", "source", "url",
        "published", "time_verified", "subcategory", "importance", "also_fits", "label", "from_backup"]
with open(pj.with_suffix('.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction='ignore', lineterminator='\n')
    w.writeheader()
    for it in pool:
        w.writerow(dict(it, also_fits=",".join(str(x) for x in it.get("also_fits") or [])))
print('pool now', len(pool))
