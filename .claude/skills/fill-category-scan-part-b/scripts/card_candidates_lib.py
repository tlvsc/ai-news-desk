"""Shared pieces of card_candidates.py and pick_gate.py: the CARD_FILTER line, the Drive category order, names."""
import re
from pathlib import Path
from common_b import B

REPO = B.parent.parent.parent
CODE = {'Politics': 'POL', 'Market': 'MKT', 'Security': 'SEC', 'Energy': 'ENE', 'Robotics': 'ROB', 'Models': 'MOD', 'Research': 'RES',
        'Ethics': 'LAW', 'Health': 'HEA', 'Society': 'SOC', 'Fun': 'FUN'}
NAME = {'POL': 'Politics and government', 'MKT': 'Market, industry and finance', 'SEC': 'Security and cyber',
        'ENE': 'Energy and infrastructure', 'ROB': 'Robotics', 'MOD': 'Models and tools', 'RES': 'Research and science',
        'LAW': 'Ethics and law', 'HEA': 'Health', 'SOC': 'Society and education', 'FUN': 'The Fun Side'}
COMPANIES = ['OpenAI', 'Anthropic', 'Google', 'Alphabet', 'Meta', 'Microsoft', 'Apple', 'Amazon', 'Nvidia', 'Tesla', 'xAI',
             'Samsung', 'Oracle', 'Broadcom', 'Intel', 'AMD', 'TSMC', 'Alibaba', 'DeepSeek', 'Palantir', 'Moonshot', 'Qualcomm', 'Arm', 'TikTok']
STOP = set('the a an and of to in on for is are was with that this it its as by at from be has have will may says say new more '
           'over after about their they than but not or into up out just also'.split())


def keys(t):
    return {w for w in re.findall(r"[a-z][a-z0-9']{3,}", t.lower()) if w not in STOP}


def read_filter():
    m = re.search(r'CARD_FILTER:\s*(.+)', (REPO / 'CLAUDE.md').read_text(encoding='utf-8'))
    if not m:
        raise SystemExit('STOP: the line "CARD_FILTER: ..." is missing in CLAUDE.md rule 16')
    f = {k: int(v) for k, v in re.findall(r'(\w+)=(\d+)', m.group(1))}
    need = {'base_min', 'extra_min', 'target', 'max_per_category', 'market_max', 'company_cards', 'company_clips'}
    if need - set(f):
        raise SystemExit(f'STOP: CARD_FILTER misses {sorted(need - set(f))}')
    return f


def read_order(W):
    p = W / 'rules' / 'Cards_Master_Rules_Structure.txt'
    if not p.exists():
        raise SystemExit(f'STOP: {p} missing (fetch it in step 0)')
    t = p.read_text(encoding='utf-8')
    a = t.find('CATEGORY ORDER'); b = t.find('Inside a category', a)
    seg = t[a:b] if a >= 0 and b > a else ''
    names = re.findall(r'(?<!\d)\d{1,2} ([A-Z][A-Za-z ,]*?) \(\d', seg)
    order = [CODE[next(k for k in CODE if n.startswith(k))] for n in names if any(n.startswith(k) for k in CODE)]
    if order != ['POL', 'MKT', 'SEC', 'ENE', 'ROB', 'MOD', 'RES', 'LAW', 'HEA', 'SOC', 'FUN'][:len(order)] and len(order) != 11:
        print('NOTICE: category order read from the Drive file:', order)
    if len(order) != 11 or order[-1] != 'FUN':
        raise SystemExit(f'STOP: could not read the 11 categories from the Drive Cards Master Section 2 item 4 (got {order})')
    return order


