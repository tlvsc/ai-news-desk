"""Step 5. Write one work file per category for the read-and-write agents.

    python make_chunks.py --workdir W

Writes W/chunks/cat_NN.json (publisher link, pool score, follow-up flags, default V1
category) and creates W/facts and W/report_entries for the agents' output.
"""
import argparse, json
from pathlib import Path

from common import DEFAULT_V1, load_run, pool_path


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--workdir', required=True)
    a = ap.parse_args()
    W = Path(a.workdir); run = load_run(W)
    pool = json.loads(pool_path(W, run).read_text(encoding='utf-8'))
    # publisher links: by the story's Google link (decoded_by_link.json, safe after a pool rebuild);
    # runs from before 30 Sep 2026 only have decoded.json by item number
    if (W / 'decoded_by_link.json').exists():
        by_link = json.loads((W / 'decoded_by_link.json').read_text())
        link = lambda p: by_link.get(p['url'])
    else:
        by_item = json.loads((W / 'decoded.json').read_text()) if (W / 'decoded.json').exists() else {}
        link = lambda p: by_item.get(p['item_id'])
    fixes = json.loads((W / 'url_fixes.json').read_text()) if (W / 'url_fixes.json').exists() else {}
    for d in ('chunks', 'facts', 'report_entries'):
        (W / d).mkdir(exist_ok=True)
    total = 0
    for cid in range(1, 17):
        items = []
        for p in pool:
            if p['category_id'] != cid:
                continue
            url = link(p) or p['url']
            items.append({'item_id': p['item_id'], 'title': p['title'], 'source': p['source'],
                          'url': fixes.get(url, url),
                          'google_url': p['url'] if 'news.google.com' in p['url'] else None,
                          'published': p['published'], 'pool_importance': p['importance'],
                          'follow_up': p.get('follow_up'), 'follow_up_of': p.get('follow_up_of'),
                          'curator_note': p.get('subcategory'), 'default_v1': DEFAULT_V1[cid]})
        (W / 'chunks' / f'cat_{cid:02d}.json').write_text(json.dumps(items, indent=1, ensure_ascii=False), encoding='utf-8')
        total += len(items)
    print('chunks written', total, '| still a Google link', [p['item_id'] for p in pool if not link(p)])


if __name__ == '__main__':
    main()
