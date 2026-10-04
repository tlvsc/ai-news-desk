"""Step 4b. Find tracking codes in the decoded publisher links and write W/url_fixes.json {bad: good}.

    python url_fixes.py --workdir W

Run after decode_links.py and before make_chunks.py. It removes utm_ and other tracking parameters; a link with
an A/B test code (userab=) loses its whole query. Existing entries in url_fixes.json are kept. Also lists links
that end in ?, = or & (cut off) so they can be fixed by hand.
"""
import argparse, json, re
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

TRACK = re.compile(r'^(utm_|fbclid$|gclid$|mc_|cmpid$|ocid$|taid$|smid$|ref_src$|referrer$|guccounter$|guce_)', re.I)


def clean(u):
    s = urlsplit(u)
    keys = [k for k, _ in parse_qsl(s.query, keep_blank_values=True)]
    if 'userab' in keys:
        return urlunsplit((s.scheme, s.netloc, s.path, '', ''))
    q = [(k, v) for k, v in parse_qsl(s.query, keep_blank_values=True) if not TRACK.match(k)]
    return urlunsplit((s.scheme, s.netloc, s.path, urlencode(q), ''))


ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--workdir', required=True)
W = Path(ap.parse_args().workdir)
dec = json.loads((W / 'decoded_by_link.json').read_text())
urls = {v if isinstance(v, str) else (v or {}).get('url', '') for v in dec.values()}
fx_path = W / 'url_fixes.json'
fixes = json.loads(fx_path.read_text()) if fx_path.exists() else {}
new = 0
for u in sorted(x for x in urls if x):
    c = clean(u)
    if c != u and u not in fixes:
        fixes[u] = c; new += 1; print('FIX ', u[:110], '->', c[:110])
    if re.search(r'[?=&]$', u):
        print('CUT OFF, fix by hand:', u)
fx_path.write_text(json.dumps(fixes, indent=1))
print(f'{new} new fixes, {len(fixes)} in {fx_path.name}; {sum(1 for u in urls if "news.google.com" in (u or ""))} still Google links')
