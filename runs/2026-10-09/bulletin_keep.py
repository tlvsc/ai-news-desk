"""Scratchpad post-filter (9 Oct 2026, Rafi: Politics only 2 stories at 6 when none at 7; Robotics 3 to 5).
Keeps only the named items in the named Bulletin sections of products/bulletin_pdf.json and the Bulletin markdown."""
import json, re, sys, glob
W = sys.argv[1]
KEEP = {'Politics and government': ['C05-02', 'C13-21'], 'Robotics': ['C11-01', 'C11-23', 'C11-24', 'C11-06', 'C11-04']}
head = lambda k: json.load(open(f'{W}/report_entries/{k}.json'))['headline']
p = f'{W}/products/bulletin_pdf.json'; d = json.load(open(p, encoding='utf-8'))
dropped = []
for c in d['categories']:
    for name, ids in KEEP.items():
        if c['name'].lower().startswith(name.lower()):
            want = [head(k) for k in ids]
            keep = [it for it in c['items'] if it['headline'] in want]
            missing = [k for k, h in zip(ids, want) if h not in [it['headline'] for it in c['items']]]
            assert not missing, (name, missing)
            dropped += [it['headline'] for it in c['items'] if it not in keep]
            for i, it in enumerate(keep, 1):
                it['rank'], it['rank_of'] = i, len(keep)
            c['items'] = keep
n = sum(len(c['items']) for c in d['categories'])
d['coverage'] = re.sub(r'\d+ stories', f'{n} stories', d['coverage'])
d['purpose'] = re.sub(r'\(HEA from 6[^)]*\)', '(Politics: the 2 best at 6, as none reached 7; Robotics, Health and Society from 6)', d['purpose'])
json.dump(d, open(p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
md = glob.glob(f'{W}/products/* — Daily Bulletin (Claude LV1.1).md')[0]
L = open(md, encoding='utf-8').read().split('\n'); out = []; i = 0
while i < len(L):
    m = re.match(r'\*\*\d+ \w+ — (.*)\*\* \(report item', L[i])
    if m and m.group(1) in dropped:
        i += 3; continue
    out.append(L[i]); i += 1
t = '\n'.join(out)
for c in d['categories']:
    t = re.sub(r'^## ' + re.escape(c['name'].upper()) + r' — \d+', f"## {c['name'].upper()} — {len(c['items'])}", t, flags=re.M)
t = re.sub(r'\*\*\d+ stories\.\*\*', f'**{n} stories.**', t, count=1)
t = re.sub(r'- Stories: \d+;', f'- Stories: {n};', t)
open(md, 'w', encoding='utf-8').write(t)
print('bulletin stories', n, '| dropped', len(dropped)); [print('  -', h[:90]) for h in dropped]
