"""Step 4. Turn every Google News link in the pool into the publisher's own link.

    python decode_links.py --workdir W

One link at a time with pauses, because Google rate-limits. Resumable: re-run it and it
continues where it stopped. Writes W/decoded.json {item_id: publisher url or null}.
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
    outp = W / 'decoded.json'
    done = json.loads(outp.read_text()) if outp.exists() else {}
    for it in pool:
        if done.get(it['item_id']):
            continue
        u = it['url'] if 'news.google.com' not in it['url'] else None
        for _ in range(3):
            if u:
                break
            u = decode(it['url'])
            time.sleep(2 if u else 5)
        done[it['item_id']] = u
        outp.write_text(json.dumps(done, indent=1))
    failed = [k for k, v in done.items() if not v]
    print('decoded', len(done) - len(failed), 'of', len(pool), '| failed', failed)


if __name__ == '__main__':
    main()
