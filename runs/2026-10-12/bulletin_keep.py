"""Run-folder post-filter (12 Oct 2026; adapted from runs/2026-10-10/bulletin_keep.py). Not a repo script.
CLAUDE.md rule 14 (BULLETIN SECTIONS NEVER EMPTY, Rafi 9 Oct 2026): a section with no story of 7 or more gets exactly 2 stories of the
Full Report at 6 or more (5 only if no 6); ROBOTICS (8 Oct): 3 to 5 robotics stories. build_products.py is run with floors that bring the
candidates in; this filter keeps exactly the named stories in those sections of products/bulletin_pdf.json and the Bulletin markdown, fixes
the subtitle (no internal codes) and the counts. Run it again after EVERY build_products.py run.

    python bulletin_keep.py WORKDIR
"""
import glob, json, re, sys

W = sys.argv[1]
KEEP = json.load(open(f'{W}/bulletin_keep.json'))   # {"Politics": [ids], "Energy": [ids], "Robotics": [ids]}
ent = lambda k: json.load(open(f'{W}/report_entries/{k}.json'))
head = lambda k: ent(k)['headline']
p = f'{W}/products/bulletin_pdf.json'
d = json.load(open(p, encoding='utf-8'))
dropped = []
for c in d['categories']:
    for name, ids in KEEP.items():
        if c['name'].lower().startswith(name.lower()):
            want = [head(k) for k in ids]
            have = [it['headline'] for it in c['items']]
            missing = [k for k, h in zip(ids, want) if h not in have]
            assert not missing, (name, missing)
            keep = [it for it in c['items'] if it['headline'] in want]
            dropped += [it['headline'] for it in c['items'] if it not in keep]
            for i, it in enumerate(keep, 1):
                it['rank'], it['rank_of'] = i, len(keep)
            c['items'] = keep
n = sum(len(c['items']) for c in d['categories'])
d['coverage'] = re.sub(r'\d+ stories', f'{n} stories', d['coverage'])
PURPOSE = ("A concise selection of the day's most important AI developments, taken from the Full Report: every story scored 7 or more, "
           "plus the best stories of the sections that have none that high, and the top 3 from The Fun Side.")
d['purpose'] = PURPOSE
json.dump(d, open(p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)

by_head = {}
for f in glob.glob(f'{W}/report_entries/C*.json'):
    e = json.load(open(f)); by_head[e['headline']] = e
kept = [by_head[it['headline']] for c in d['categories'] for it in c['items'] if it['headline'] in by_head]
import csv
pool = {r['item_id']: int(float(r['importance'])) for r in csv.DictReader(open(glob.glob(f'{W}/out/AIND_Pool_*.csv')[0]))}
low = sum(1 for e in kept if int(e['score']) < pool[e['item_id']])

md = glob.glob(f'{W}/products/* — Daily Bulletin (Claude*).md')[0]
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
t = re.sub(r'Rule: every story scored 7 to 10, plus the top 3 Fun Side stories \([^)]*\) \(cutoff set to the day\'s pool, CLAUDE.md rule 14\)\.',
           'Rule: every story scored 7 to 10, plus the best stories of the sections that have none that high, and the top 3 Fun Side stories.', t)
hl = len(re.findall(r'\*\(headline only\)\*', t))
t = re.sub(r'- Headline-only stories included: \d+\.', f'- Headline-only stories included: {hl}.', t)
t = re.sub(r'- Fact check suggested a lower score for \d+ of these stories', f'- Fact check suggested a lower score for {low} of these stories', t)
open(md, 'w', encoding='utf-8').write(t)
print('bulletin stories', n, '| dropped', len(dropped), '| headline only', hl, '| lower fc', low)
for h in dropped: print('  -', h[:90])
