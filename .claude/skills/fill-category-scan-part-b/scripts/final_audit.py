"""Final audit before ANYTHING goes to Rafi (Rafi, 14 Oct 2026: "make sure these mistakes, or any lesson we have learned, do not repeat").

    python final_audit.py --workdir W              run every check, print the lines, list lines changed since the last send
    python final_audit.py --workdir W --mark-sent  after sending: remember what Rafi now has

It runs: check_wording.py (clips and cards), check_headlines_rules.py, verify_headlines.py on the JSON. Exit code 1 when any check fails;
send nothing then. It also lists every spoken line and card head/body that CHANGED since the last send: change a line Rafi has seen only when he
asked for it (14 Oct 2026: 'worms' and other approved wording were changed without asking).
"""
import argparse, json, shutil, subprocess, sys
from pathlib import Path

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--workdir', required=True)
ap.add_argument('--mark-sent', action='store_true')
a = ap.parse_args()
W = Path(a.workdir)
S = Path(__file__).parent
SNAP = W / 'last_sent'
FILES = [W / 'headlines_work' / 'scripts_final.json', W / 'cards_work' / 'cards_copy_fable.json']

if a.mark_sent:
    SNAP.mkdir(exist_ok=True)
    for f in FILES:
        if f.exists(): shutil.copy(f, SNAP / f.name)
    print('marked as sent:', [f.name for f in FILES]); sys.exit(0)


def run(label, cmd):
    r = subprocess.run([sys.executable] + cmd, capture_output=True, text=True, cwd=W)
    out = (r.stdout + r.stderr).splitlines()
    fails = [l for l in out if l.startswith('FAIL') or 'to fix' in l and l.startswith('RESULT') or l.startswith('STOP')]
    ok = r.returncode == 0 and not fails
    print(f"{'PASS' if ok else 'FAIL'}  {label}" + ('' if ok else '   <- ' + ' | '.join(f[:140] for f in fails[:4])))
    return ok


json_files = sorted((W / 'products').glob('headlines_*_VL1.json'))
json_files = [j for j in json_files if '_old' not in j.name]
ok = True
ok &= run('wording of the Headlines clips', [str(S / 'check_wording.py'), '--workdir', str(W)])
ok &= run('wording of the cards', [str(S / 'check_wording.py'), '--workdir', str(W), '--cards', str(W / 'cards_work' / 'cards_copy_fable.json')])
ok &= run('Headlines rules (openings, order, seconds, cues)', [str(S / 'check_headlines_rules.py'), '--workdir', str(W)])
if json_files:
    ok &= run('the ComfyUI JSON', [str(S / 'verify_headlines.py'), '--json', str(json_files[-1])])
else:
    print('FAIL  no Headlines JSON in products/'); ok = False


def lines(f):
    if not f.exists(): return {}
    d = json.loads(f.read_text())
    out = {}
    if 'stories' in d and d['stories'] and 'script' in d['stories'][0]:
        for s in d['stories']: out['clip ' + s['item']] = s['script']
        out['fun'] = d['fun']['script']; out['teaser'] = d['teaser']['script']; out['bp clip'] = d['bp']['script']
    elif 'stories' in d:
        for s in d['stories']: out['card ' + s['card']] = s['head'] + ' / ' + s['body']
        for t in d.get('teaser', []): out['teaser card ' + t['id']] = t['head']
        out['bp card'] = d['bp']['head'] + ' / ' + d['bp']['body']
    return out


print('\nLINES CHANGED SINCE THE LAST SEND (change a line Rafi has seen only when he asked):')
changed = 0
for f in FILES:
    new, old = lines(f), lines(SNAP / f.name)
    if not old:
        print(f'  {f.name}: nothing sent yet'); continue
    for k, v in new.items():
        if old.get(k) != v:
            changed += 1; print(f'  {k}\n     was: {old.get(k)}\n     now: {v}')
if not changed: print('  none')
print('\nNow READ every spoken line and every card line below against Rafi\'s rules, then send. Nothing is sent on a FAIL.')
for f in FILES:
    for k, v in lines(f).items(): print(f'  {k}: {v}')
print('\nAUDIT', 'PASS' if ok else 'FAIL')
sys.exit(0 if ok else 1)
