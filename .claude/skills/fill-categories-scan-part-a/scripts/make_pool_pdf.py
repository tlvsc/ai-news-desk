"""The pool as a PDF (Rafi, 9 Oct 2026): every pool story, category by category, numbered, highest score first.

    python make_pool_pdf.py --workdir W

Line shape (Rafi's words): "Robotics: 1) score 7: headline / source". The headline is the publisher's headline from the
pool; the source is the credited outlet of the written entry when there is one, else the pool's source.
Writes W/products/AIND_Pool_<D-M-YY>.pdf. Fonts: W/fonts (Instrument Sans) when present.
"""
import argparse, html, json
from pathlib import Path
import pymupdf
from common import load_run, pool_path, categories, short_date, long_date, window_text, edition

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--workdir', required=True)
a = ap.parse_args()
W = Path(a.workdir)
run = load_run(W)
pool = json.loads(pool_path(W, run).read_text(encoding='utf-8'))
cats = categories()
ed = edition(run)


def cat_name(cid):
    v = cats.get(str(cid)) or cats.get(cid)
    t = v[0] if isinstance(v, list) else str(v)
    return t.split(' (')[0].rstrip('.')


def source_of(x):
    f = W / 'report_entries' / f"{x['item_id']}.json"
    if f.exists():
        try:
            return json.loads(f.read_text(encoding='utf-8')).get('source') or x.get('source', '')
        except ValueError:
            pass
    return x.get('source', '')


by = {}
for x in pool:
    by.setdefault(int(x['category_id']), []).append(x)
e = html.escape
parts = [f"<h1>AI News Desk: the daily pool</h1><p class='sub'>{e(long_date(ed))} &middot; {e(window_text(run))} &middot; "
         f"{len(pool)} stories in {len(by)} categories, highest score first</p>"]
for cid in sorted(by):
    items = sorted(by[cid], key=lambda x: (-int(x.get('importance') or 0), int(x.get('pool_rank') or 99)))
    parts.append(f"<h2>{e(cat_name(cid))} ({len(items)})</h2><ol>")
    for x in items:
        parts.append(f"<li><b>score {int(x.get('importance') or 0)}:</b> {e(x['title'].strip())} / <i>{e(source_of(x))}</i></li>")
    parts.append("</ol>")
fonts = W / 'fonts'
ff = ''
if (fonts / 'InstrumentSans-Regular.ttf').exists():
    ff = ("@font-face {font-family: IS; src: url(InstrumentSans-Regular.ttf);} "
          "@font-face {font-family: IS; src: url(InstrumentSans-Bold.ttf); font-weight: bold;} "
          "@font-face {font-family: IS; src: url(InstrumentSans-Regular.ttf); font-style: italic;} ")
css = ff + ("* {font-family: IS, sans-serif;} body {font-size: 9.5pt;} h1 {font-size: 18pt; margin-bottom: 2pt;} "
            ".sub {font-size: 9pt; color: #555;} h2 {font-size: 12pt; margin-top: 10pt; color: #1a4f8b;} li {margin-bottom: 2pt;}")
story = pymupdf.Story(html=f"<body>{''.join(parts)}</body>", user_css=css, archive=pymupdf.Archive(str(fonts)) if ff else None)
out = W / 'products' / f"AIND_Pool_{short_date(ed)}.pdf"
writer = pymupdf.DocumentWriter(str(out))
mediabox = pymupdf.paper_rect('a4')
where = mediabox + (40, 40, -40, -50)
more = 1
while more:
    dev = writer.begin_page(mediabox)
    more, _ = story.place(where)
    story.draw(dev)
    writer.end_page()
writer.close()
doc = pymupdf.open(str(out))
for i, p in enumerate(doc, 1):
    p.insert_text((40, mediabox.height - 25), f"AI News Desk pool  {short_date(ed)}   Page {i} of {len(doc)}", fontsize=7.5, color=(0.4, 0.4, 0.4))
doc.saveIncr() if False else doc.save(str(out) + '.tmp', garbage=3, deflate=True)
doc.close()
Path(str(out) + '.tmp').replace(out)
print(f'[ok] {out} pages={len(pymupdf.open(str(out)))} stories={len(pool)} categories={len(by)}')
