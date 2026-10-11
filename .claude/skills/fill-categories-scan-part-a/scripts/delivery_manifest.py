"""Step 13a. List the day's deliverables with their Drive destination and byte size, for the Drive delivery agent and the check.

    python delivery_manifest.py --workdir W [--part A|B|all]         # prints the list and writes W/products/delivery_manifest.json
    python delivery_manifest.py --workdir W --check W/products/drive_delivery.json   # compares the agent's result with the list

Destinations (Drive "AI News Desk — STORAGE & FILE ROUTING STANDARD", DAILY STORAGE, changed 9 Oct 2026; Rafi 11 Oct 2026: the Drive
layout is the right one): daily_data_generated/<edition>/ with five product folders, each with its own supportive files:
pool of items (pool PDF, pool CSV, daily-pool.md; pool JSON in supportive files), Full Report (PDF and markdown; report_pdf.json in
supportive files), Bulletin (PDF and markdown; bulletin_pdf.json in supportive files), cards (the PNGs and the contact sheet;
cards_copy, edition and lock JSON in supportive files), Headlines (the ComfyUI JSON, the pack and the scripts in supportive files).

STANDARD CHECK (Rafi, 11 Oct 2026, option c: CLAUDE.md rule 0 points to the Drive file, the folder names live only here, and every run
checks them): W/rules/STORAGE_STANDARD.txt is the Drive Google Doc "AI News Desk — STORAGE & FILE ROUTING STANDARD"
(1ModaHnDZvjn5SxEvwRXwxlrhoXXKzDq-Mhs0NS0eVms), saved in Part A step 0. The script stops when the file is missing or when its
"product folders" sentence names other folders than FOLDERS below.
    python delivery_manifest.py --workdir W --standard-only        # step 0: the check alone
"""
import argparse, glob, json, re, sys
from pathlib import Path

FOLDERS = ['pool of items', 'Full Report', 'Bulletin', 'cards', 'Headlines']
# WHO MADE IT (Rafi, 11 Oct 2026: two or three scans save into the same folders, "each file name says exactly who or which scan it is"):
# every Drive title carries the creator and version of this scan. Cards keep their Drive name rule until Rafi answers (CARDS_LABEL).
RUN_LABEL = 'Claude-LV1.1'
CARDS_LABEL = False


def titled(folder, name):
    if 'Claude' in name or (folder.startswith('cards') and folder == 'cards' and not CARDS_LABEL):
        return name
    stem, dot, ext = name.rpartition('.')
    return f'{stem}_{RUN_LABEL}.{ext}' if dot else f'{name}_{RUN_LABEL}'
STANDARD_ID = '1ModaHnDZvjn5SxEvwRXwxlrhoXXKzDq-Mhs0NS0eVms'


def check_standard(W):
    f = W / 'rules' / 'STORAGE_STANDARD.txt'
    if not f.exists():
        sys.exit(f'STOP: {f} is missing. Save the Drive storage standard ({STANDARD_ID}) there first (Part A step 0).')
    text = re.sub(r'[\\*#_]', '', f.read_text(encoding='utf-8', errors='replace'))
    m = re.search(r'with product folders\s+(.+?)\.\s+Each product', text, re.S)
    if not m:
        sys.exit('STOP: the storage standard no longer has its "with product folders ... Each product" sentence; read it and tell Rafi.')
    named = [x.strip() for x in re.split(r',\s*|\s+and\s+', ' '.join(m.group(1).split())) if x.strip()]
    if named != FOLDERS:
        sys.exit(f'STOP: the Drive storage standard names {named}, this script uses {FOLDERS}. Tell Rafi (CLAUDE.md rule 8a); change nothing on Drive.')
    print('storage standard check: the Drive file and this script name the same five product folders:', ', '.join(FOLDERS))

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--workdir', required=True); ap.add_argument('--part', default='all', choices=['A', 'B', 'all'])
ap.add_argument('--check'); ap.add_argument('--standard-only', action='store_true')
a = ap.parse_args()
W = Path(a.workdir).resolve()
check_standard(W)
if a.standard_only:
    sys.exit(0)
ed = json.loads((W / 'run.json').read_text())['edition']
y, m, d = ed.split('-'); short = f'{int(d)}-{int(m)}-{y[2:]}'
P = W / 'products'
rows = []


def add(folder, path):
    p = Path(path)
    if p.exists():
        rows.append({'folder': folder, 'title': titled(folder, p.name), 'path': str(p), 'bytes': p.stat().st_size})
    else:
        rows.append({'folder': folder, 'title': titled(folder, p.name), 'path': str(p), 'bytes': None, 'status': 'MISSING LOCALLY'})


if a.part in ('A', 'all'):
    add('Full Report', P / f'Full_Report_{short}.pdf'); add('Bulletin', P / f'Daily_Bulletin_{short}.pdf')
    for f in sorted(P.glob(f'{ed} — *.md')):
        if f.name.endswith('_old.md') or '_old' in f.stem:
            continue
        add('Bulletin' if 'Bulletin' in f.name else 'Full Report', f)
    add('Full Report/supportive files', P / 'report_pdf.json'); add('Bulletin/supportive files', P / 'bulletin_pdf.json')
    for f in (P / f'AIND_Pool_{short}.pdf', P / f'AIND_Pool_{ed}.csv', P / 'daily-pool.md'):
        add('pool of items', f)
    add('pool of items/supportive files', W / 'out' / f'AIND_Pool_{ed}.json')
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
    bad = 0; inchat = []
    for r in rows:
        x = done.get((r['folder'], r['title']))
        ok = x and x.get('drive_bytes') == r['bytes'] and x.get('status') in ('OK', 'already there')
        chat = not ok and x and x.get('status') == 'too large'
        bad += not ok and not chat
        inchat.append(r['title']) if chat else None
        print('OK  ' if ok else ('CHAT' if chat else 'FAIL'), r['folder'], r['title'], '' if ok else (x or {}).get('status', 'not uploaded'))
    print('delivery check:', 'all files on Drive with the right size' if not bad else f'{bad} files to fix')
    if inchat:
        print(f'{len(inchat)} files the connection refused after a real attempt (status "too large"): they go to Rafi in chat')
