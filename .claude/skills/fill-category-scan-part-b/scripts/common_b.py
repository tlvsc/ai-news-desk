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
