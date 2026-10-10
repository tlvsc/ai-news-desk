"""Merge the ROBOT PASS (Rafi, 10 Oct 2026) into category 11 before the pool is built.

    python3 merge_robot_pass.py --workdir W        # after the 16 curators and the robot pass agent, before build_pool.py

Reads W/robot_pass.json (briefs/robot_pass.md) and appends its stories to W/pool/cat_11.json as main picks, skipping a story whose url
or title is already there; the old file is kept as cat_11_before_robot_pass_old.json. Main picks are ranked by importance (backups
stay last). Scores are the curator's own; a score raised by Rafi's order is raised later, by hand, with his words recorded.
"""
import argparse, json, shutil
from pathlib import Path
from common import norm_url, similar

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--workdir', required=True)
W = Path(ap.parse_args().workdir)
rp = json.loads((W / 'robot_pass.json').read_text(encoding='utf-8'))
cp = W / 'pool' / 'cat_11.json'
cur = json.loads(cp.read_text(encoding='utf-8'))
shutil.copy(cp, W / 'pool' / 'cat_11_before_robot_pass_old.json')
urls = {norm_url(x['url']) for x in cur}
added = []
for s in rp:
    if norm_url(s['url']) in urls or any(similar(s['title'], x['title']) >= 0.6 for x in cur):
        continue
    cur.append({"category_id": 11, "rank": 99, "backup": False, "title": s['title'], "summary": s['title'], "source": s['source'],
                "url": s['url'], "published": s['published'], "time_verified": True,
                "subcategory": 'Humanoid robots' if s.get('humanoid') else 'Robots at work', "importance": int(s.get('importance') or 4),
                "also_fits": [], "follow_up": False, "follow_up_of": None, "robot_pass": True})
    added.append(s['title'])
mains = sorted([x for x in cur if not x.get('backup')], key=lambda x: (-int(x.get('importance') or 0), int(x.get('rank') or 99)))
backs = [x for x in cur if x.get('backup')]
for n, x in enumerate(mains + backs, 1):
    x['rank'] = n
cp.write_text(json.dumps(mains + backs, indent=1, ensure_ascii=False), encoding='utf-8')
print(f'robot pass: {len(added)} stories added to category 11 ({len(mains)} main picks, {len(backs)} backups)')
for t in added:
    print('  +', t[:100])
