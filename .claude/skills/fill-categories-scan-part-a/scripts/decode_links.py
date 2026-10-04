"""Step 4. Turn every Google News link in the pool into the publisher's own link.

    python decode_links.py --workdir W

One link at a time with pauses, because Google rate-limits. Resumable: re-run it and it
continues where it stopped. The results are kept by the story's own Google link in
W/decoded_by_link.json {google link: publisher url or null}, so they stay with the right story
when the pool is rebuilt and the item numbers shift (30 Sep 2026: links saved by number landed
on the wrong stories in category 12). It also writes W/decoded.json {item_id: publisher url or
null} for the current pool; make_chunks.py reads the by-link file.
Optional W/url_fixes.json {bad url: good url} corrects links found broken later.
Run it in the background; about 230 links take 10 to 15 minutes.
"""
import argparse, json, time
from pathlib import Path

from common import load_run, pool_path
from gd import decode


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--workdir', required=True)
    a = ap.parse_args()
    W = Path(a.workdir); run = load_run(W)
    pool = json.loads(pool_path(W, run).read_text(encoding='utf-8'))
    cache_p = W / 'decoded_by_link.json'
    cache = json.loads(cache_p.read_text()) if cache_p.exists() else {}
    if not cache and (W / 'decoded.json').exists():
        print('note: decoded.json from an older version is not reused; links are decoded again by Google link')
    for it in pool:
        g = it['url']
        if cache.get(g):
            continue
        u = g if 'news.google.com' not in g else None
        for _ in range(3):
            if u:
                break
            u = decode(g)
            time.sleep(2 if u else 5)
        cache[g] = u
        cache_p.write_text(json.dumps(cache, indent=1))
    done = {it['item_id']: cache.get(it['url']) for it in pool}
    (W / 'decoded.json').write_text(json.dumps(done, indent=1))
    failed = [k for k, v in done.items() if not v]
    print('decoded', len(done) - len(failed), 'of', len(pool), '| failed', failed)


if __name__ == '__main__':
    main()
