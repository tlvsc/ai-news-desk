"""Fetch every decoded article once and save its body text, so the writers can read local files.

    python prefetch.py --workdir W        (step 5b, after make_chunks.py; about 2 minutes)

Reads WORKDIR/chunks/cat_NN.json, writes WORKDIR/fulltext/<item_id>.txt (article paragraphs)
and WORKDIR/fulltext/_status.json {item_id: {"chars": n, "http": code, "url": ...}}.
Skips items already fetched, so it can be re-run.
"""
import concurrent.futures as cf, html, json, re, subprocess, sys
from pathlib import Path

import argparse
ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--workdir', required=True)
W = Path(ap.parse_args().workdir)
OUT = W / 'fulltext'
OUT.mkdir(exist_ok=True)
STATUS = OUT / '_status.json'
status = json.loads(STATUS.read_text()) if STATUS.exists() else {}


def fetch(url):
    r = subprocess.run(['curl', '-s', '-L', '--max-time', '25', '-A', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                        '-w', '\n%{http_code}', url], capture_output=True)
    body = r.stdout.decode('utf-8', 'replace')
    body, _, code = body.rpartition('\n')
    return body, code.strip()


def paragraphs(page):
    page = re.sub(r'(?is)<(script|style|noscript|svg|nav|footer|header|aside|form)\b.*?</\1>', ' ', page)
    paras = []
    for m in re.finditer(r'(?is)<p\b[^>]*>(.*?)</p>', page):
        t = html.unescape(re.sub(r'(?s)<[^>]+>', '', m.group(1)))
        t = re.sub(r'\s+', ' ', t).strip()
        if len(t) >= 60:
            paras.append(t)
    return paras


def one(item):
    iid, url = item['item_id'], item['url']
    if 'news.google.com' in url:
        return iid, {'chars': 0, 'http': 'google-link', 'url': url}
    try:
        page, code = fetch(url)
    except Exception as e:  # network error: record and move on
        return iid, {'chars': 0, 'http': f'error {e.__class__.__name__}', 'url': url}
    paras = paragraphs(page)
    text = '\n\n'.join(paras)
    if text:
        (OUT / f'{iid}.txt').write_text(f'URL: {url}\nTITLE: {item["title"]}\n\n{text}\n', encoding='utf-8')
    return iid, {'chars': len(text), 'http': code, 'url': url}


items = []
for f in sorted((W / 'chunks').glob('cat_*.json')):
    items += json.loads(f.read_text())
todo = [i for i in items if i['item_id'] not in status]
with cf.ThreadPoolExecutor(8) as ex:
    for iid, st in ex.map(one, todo):
        status[iid] = st
STATUS.write_text(json.dumps(status, indent=1))
good = sum(1 for s in status.values() if s['chars'] >= 800)
print(f'items {len(items)} | text of 800+ chars: {good} | short or blocked: {len(items) - good}')
