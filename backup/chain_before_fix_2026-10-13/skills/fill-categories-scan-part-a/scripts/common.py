"""Shared helpers for the daily run: the run file, dates, categories, URL and title matching.

Every script takes --workdir. collect.py writes WORKDIR/run.json (edition date and
reporting window); every later script reads the window from there, so it is set once.
"""
import csv, json, re
from datetime import date, datetime, timezone
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December']
WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# V1 report categories (order of 23 Sep 2026) and the default V1 home of each LV2 category
ORDER = ['POL', 'MKT', 'SEC', 'ENE', 'ROB', 'MOD', 'RES', 'LAW', 'HEA', 'SOC', 'FUN']
NAMES = {'POL': 'Politics and government', 'MKT': 'Market, industry and finance', 'SEC': 'Security and cyber',
         'ENE': 'Energy and infrastructure', 'ROB': 'Robotics', 'MOD': 'Models and tools',
         'RES': 'Research and science', 'LAW': 'Ethics and law', 'HEA': 'Health',
         'SOC': 'Society and education', 'FUN': 'The Fun Side'}
DEFAULT_V1 = {1: 'MOD', 2: 'MOD', 3: 'MOD', 4: 'RES', 5: 'choose', 6: 'MKT', 7: 'MKT', 8: 'ENE', 9: 'ENE',
              10: 'HEA', 11: 'ROB', 12: 'SEC', 13: 'POL or LAW', 14: 'SOC', 15: 'RES', 16: 'FUN'}
FUN = 16
# THE ORDER NEVER CHANGES (Rafi, 10 Oct 2026, "the order never change again for any products"): the approved order of categories of
# 23 Sep 2026 is ORDER above (Politics first, Fun last). Every product that lists categories uses it. The 16 curator categories of the pool
# sit under their V1 section like this (13 Policy, Law and 5 Industry Voices under Politics; Law has no curator category of its own):
CAT_SECTION = {13: 'POL', 5: 'POL', 6: 'MKT', 7: 'MKT', 12: 'SEC', 8: 'ENE', 9: 'ENE', 11: 'ROB', 1: 'MOD', 2: 'MOD', 3: 'MOD',
               4: 'RES', 15: 'RES', 10: 'HEA', 14: 'SOC', 16: 'FUN'}
POOL_ORDER = sorted(CAT_SECTION, key=lambda c: (ORDER.index(CAT_SECTION[c]), list(CAT_SECTION).index(c)))


def categories():
    """{id: (description, extra criterion)} for the 16 LV2 curator categories."""
    raw = json.loads((SKILL / 'categories.json').read_text(encoding='utf-8'))
    return {int(k): v for k, v in raw.items()}


def short_names():
    """'Models & Core AI' style names: the description up to its first bracket or full stop."""
    return {k: re.split(r' \(|\. ', v[0])[0].strip() for k, v in categories().items()}


def load_run(workdir):
    return json.loads((Path(workdir) / 'run.json').read_text(encoding='utf-8'))


def parse_utc(s):
    dt = datetime.fromisoformat(s.replace('Z', '+00:00'))
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


def edition(run):
    return date.fromisoformat(run['edition'])


def long_date(d):          # 29 September 2026
    return f'{d.day} {MONTHS[d.month - 1]} {d.year}'


def short_date(d):         # 29-9-26, the file-name date
    return f'{d.day}-{d.month}-{d.year % 100}'


def window_text(run):      # 28 Sep 2026 00:23 UTC to 29 Sep 2026 06:23 UTC (30 hours)
    s, e = parse_utc(run['start']), parse_utc(run['end'])
    f = lambda t: f'{t.day} {MONTHS[t.month - 1][:3]} {t.year} {t:%H:%M} UTC'
    return f"{f(s)} to {f(e)} ({run['hours']} hours)"


def band(score):
    s = int(score)
    return 'CRITICAL' if s >= 10 else 'HIGH' if s >= 8 else 'MEDIUM' if s >= 6 else 'WATCHLIST'


def norm_url(u):
    u = (u or '').strip().lower()
    u = re.sub(r'^https?://(www\.)?', '', u)
    return u.split('#')[0].split('?')[0].rstrip('/')


def words(t):
    return {w for w in re.findall(r'[a-z0-9]+', (t or '').lower()) if len(w) > 3}


def similar(a, b):
    wa, wb = words(a), words(b)
    return len(wa & wb) / len(wa | wb) if wa and wb else 0.0


def load_pool_file(path):
    """Yesterday's pool from its JSON or CSV (the CSV is what Drive keeps)."""
    p = Path(path)
    if p.suffix.lower() == '.csv':
        with open(p, encoding='utf-8', newline='') as f:
            return list(csv.DictReader(f))
    return json.loads(p.read_text(encoding='utf-8'))


def pool_path(workdir, run):
    return Path(workdir) / 'out' / f"AIND_Pool_{run['edition']}.json"
