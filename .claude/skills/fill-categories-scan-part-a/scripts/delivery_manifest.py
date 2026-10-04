"""Step 13a. List the day's deliverables with their Drive destination and byte size, for the Drive delivery agent and the check.

    python delivery_manifest.py --workdir W [--part A|B|all]         # prints the list and writes W/products/delivery_manifest.json
    python delivery_manifest.py --workdir W --check W/products/drive_delivery.json   # compares the agent's result with the list

Destinations (AI News Desk — STORAGE & FILE ROUTING STANDARD): daily_data_generated/<edition>/reports (the two PDFs and the two
markdown files), reports/supportive files (pool CSV and JSON, daily-pool.md, the two PDF input JSON files), cards (the PNGs and
the contact sheet), cards/supportive files (cards_copy, edition and lock JSON), Headlines/supportive files (the ComfyUI JSON,
the pack, the scripts).
"""
import argparse, glob, json
from pathlib import Path

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--workdir', required=True); ap.add_argument('--part', default='all', choices=['A', 'B', 'all'])
ap.add_argument('--check')
a = ap.parse_args()
W = Path(a.workdir).resolve(); ed = json.loads((W / 'run.json').read_text())['edition']
y, m, d = ed.split('-'); short = f'{int(d)}-{int(m)}-{y[2:]}'
P = W / 'products'
rows = []


def add(folder, path):
    p = Path(path)
    if p.exists():
        rows.append({'folder': folder, 'title': p.name, 'path': str(p), 'bytes': p.stat().st_size})
    else:
        rows.append({'folder': folder, 'title': p.name, 'path': str(p), 'bytes': None, 'status': 'MISSING LOCALLY'})


if a.part in ('A', 'all'):
    add('reports', P / f'Full_Report_{short}.pdf'); add('reports', P / f'Daily_Bulletin_{short}.pdf')
    for f in sorted(P.glob(f'{ed} — *.md')):
        add('reports', f)
    for f in (P / f'AIND_Pool_{ed}.csv', W / 'out' / f'AIND_Pool_{ed}.json', P / 'daily-pool.md', P / 'report_pdf.json', P / 'bulletin_pdf.json'):
        add('reports/supportive files', f)
if a.part in ('B', 'all'):
    for f in sorted(glob.glob(str(P / f'cards_{short}' / f'cards_{short}_I*_VL1.png'))) + [P / f'cards_{short}' / f'cards_{short}_contact_sheet.jpg']:
        add('cards', f)
    for f in (W / 'cards_copy.json', P / 'cards_edition.json', P / 'cards_content_lock.json'):
        add('cards/supportive files', f)
    for f in (P / f'headlines_{short}_VL1.json', W / 'headlines_work' / f'headlines_{short}_pack.json', W / 'headlines_work' / 'scripts_final.json'):
        add('Headlines/supportive files', f)
out = P / 'delivery_manifest.json'
out.write_text(json.dumps({'edition': ed, 'files': rows}, indent=1, ensure_ascii=False))
brief = (Path(__file__).resolve().parent.parent / 'briefs' / 'drive_delivery.md').read_text(encoding='utf-8')
(P / 'drive_delivery_prompt.txt').write_text(brief.replace('{EDITION}', ed).replace('{MANIFEST}', str(out)).replace('{WORKDIR}', str(W))
                                            .replace('{{', '{').replace('}}', '}'), encoding='utf-8')
for r in rows:
    print(f"{r['folder']:26} {r['title']:60} {r['bytes'] if r['bytes'] is not None else r['status']}")
print(len(rows), 'files ->', out, '| agent prompt:', P / 'drive_delivery_prompt.txt')
if a.check:
    done = {(x['folder'], x['title']): x for x in json.loads(Path(a.check).read_text())}
    bad = 0
    for r in rows:
        x = done.get((r['folder'], r['title']))
        ok = x and x.get('drive_bytes') == r['bytes'] and x.get('status') in ('OK', 'already there')
        bad += not ok
        print('OK  ' if ok else 'FAIL', r['folder'], r['title'], '' if ok else (x or {}).get('status', 'not uploaded'))
    print('delivery check:', 'all files on Drive with the right size' if not bad else f'{bad} files to fix')
