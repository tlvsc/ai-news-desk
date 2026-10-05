"""Shared helpers for Fill_category_scan_Part_B: paths, edition dates, report entries."""
import json
from datetime import date
from pathlib import Path

B = Path(__file__).resolve().parent.parent
A = B.parent / 'fill-categories-scan-part-a'
COVER_SCRIPT = B.parent.parent.parent / 'scripts' / 'card_cover_adjusting_script.py'
MON = ('JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC')
WD = ('MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN')


def run(W):
    return json.loads((Path(W) / 'run.json').read_text())


def edition_dates(W):
    """('2026-10-03', '3-10-26', 'SAT 3 OCT 2026')"""
    ed = run(W)['edition']; d = date.fromisoformat(ed)
    return ed, f'{d.day}-{d.month}-{d.year % 100}', f'{WD[d.weekday()]} {d.day} {MON[d.month - 1]} {d.year}'


def entry(W, item):
    return json.loads((Path(W) / 'report_entries' / f'{item}.json').read_text(encoding='utf-8'))


def prev_scripts(W):
    """The previous edition's final Headlines scripts (scratchpad run folders first, then the repo restart copies)."""
    W = Path(W).resolve(); ed = run(W)['edition']
    cands = [Path(p) for p in sorted(W.parent.glob('run_*/headlines_work/scripts_final.json'))]
    cands += [Path(p) for p in sorted((B.parent.parent.parent / 'runs').glob('*/headlines_work/scripts_final.json'))]
    older = [(c.parent.parent.name.replace('run_', ''), c) for c in cands if c.parent.parent.name.replace('run_', '') < ed]
    return str(max(older)[1]) if older else None


def rules_gate(W):
    """GATE (Rafi, 4 Oct 2026): stop unless the Headlines rules recheck (Part B step 3b) is clean for the current lines."""
    H = Path(W) / 'headlines_work'
    sf, rc, rr = H / 'scripts_final.json', H / 'rules_check.json', H / 'rules_result.json'
    why = []
    if not rc.exists() or rc.stat().st_mtime < sf.stat().st_mtime:
        why.append('check_headlines_rules.py has not run on the current scripts_final.json')
    elif json.loads(rc.read_text()).get('fails'):
        why.append(f"check_headlines_rules.py reports {json.loads(rc.read_text())['fails']} rule fails")
    if not rr.exists() or rr.stat().st_mtime < sf.stat().st_mtime:
        why.append('the rules agent (prompt_rules_headlines.txt) has not checked the CURRENT lines (any edit after it needs a new check)')
    wc = H / 'wording_check.json'
    if not wc.exists() or wc.stat().st_mtime < sf.stat().st_mtime or json.loads(wc.read_text()).get('fails'):
        why.append('check_wording.py has not passed on the current lines (level 5, who, what, why)')
    if why:
        raise SystemExit('STOP, step 3b is not done: ' + '; '.join(why))
