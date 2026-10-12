import sys
sys.path.insert(0, '/home/user/ai-news-desk/.claude/skills/fill-category-scan-part-b/scripts')
"""Step 6c. Independent check of the filled Headlines JSON (a different angle from the fill script's own asserts).

    python verify_headlines.py --json W/products/headlines_D-M-YY_VL1.json

Prints size and md5, the steps and voice sample settings, the active slots and their seconds, the news part total,
the unhurried tone in every active prompt, and digits in any spoken line except Rafi's opening ("90 seconds").
"""
import argparse, hashlib, json, re
from pathlib import Path

TONE = 'at a natural, unhurried pace, in an authoritative and informative news presenter tone, clear and easy to understand, never rushed'
ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--json', required=True)
p = Path(ap.parse_args().json); b = p.read_bytes(); wf = json.loads(b); nodes = {n['id']: n for n in wf['nodes']}
print(p.name, len(b), 'bytes, md5', hashlib.md5(b).hexdigest())
print('steps', nodes[11]['widgets_values'][1], '| voice sample', nodes[8]['widgets_values'][0])
act, tone, dig = [], 0, []
for s in range(1, 14):
    n12, n13 = nodes[s * 100 + 12], nodes[s * 100 + 13]
    if n12['mode'] == 0:
        act.append((s, n13['widgets_values'][0])); t = n12['widgets_values'][0]; tone += TONE in t
        spoken = re.search(r'says exactly.*?"(.*?)" at', t, re.S).group(1)
        if s == 12:   # NOT FINANCIAL ADVICE (Rafi, 7 Oct 2026): spoken AND on the screen, checked in the finished JSON
            nfa = ('not financial advice' in spoken.lower(), 'not financial advice' in t.split('says exactly')[0].lower())
            print('Bigger Picture clip: "not financial advice" spoken', nfa[0], '| on the screen', nfa[1])
            if not all(nfa): dig.append('C12 not financial advice missing')
        if s != 1 and re.search(r'\d', spoken): dig.append(s)
ok = all(x[1] <= 12 for x in act) and tone == len(act) and not dig and nodes[11]['widgets_values'][1] == 8
print('active', [x[0] for x in act], '| seconds', [x[1] for x in act], '| longest', max(x[1] for x in act),
      '| total', sum(x[1] for x in act), '| news part', sum(x[1] for x in act if 2 <= x[0] <= 11))
print('tone in', tone, 'of', len(act), '| digits in spoken lines', dig or 'none')
print('RESULT', 'PASS' if ok else 'FAIL')
