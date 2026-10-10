"""VIRAL RULE (Rafi, 10 Oct 2026; CLAUDE.md VIRAL RULE): a story carried by 20 or more distinct outlets in the window scores at least 7.

    python3 viral_sweep.py sweep --workdir W    # step 1c, before the curators: writes W/viral.json and prints the list
    python3 viral_sweep.py check --workdir W    # after build_pool, after the writers, before the build: every floor is met

One floor only (Rafi's words): 20 or more distinct outlets -> score at least 7 (so the story goes into the Bulletin). The category stays
the one the curators give. No other tier, no cap, no extra limit. The candidate lists are already filtered to AI stories; if a cluster
is plainly not about AI (a false match), the main session lists it in W/viral_exclude.json {"clusters": [N], "why": "..."} and says so to Rafi.

The sweep also prints the LOW SCORE, HIGH REACH list (pool score 4 or lower, 8 or more outlets) for Rafi to read with the delivery.
Reads W/candidates/cand_*.json and W/candidates_55.json (title, source, link, published) and W/out/AIND_Pool_<edition>.json when it exists.
Matching is by title words (a first version; V1 needs a real story identity).
"""
import argparse, glob, json, re
from pathlib import Path

THRESHOLD = 20
FLOOR = 7
STOP = set('the a an of to in on for and with by at from as is are be its it that this how what why new says say said after over into about up out '
           'will can has have more not or than their his her they you your ai'.split())


def toks(t):
    t = re.sub(r' - [^-]{2,40}$', '', t.lower())
    return frozenset(w for w in re.findall(r"[a-z0-9']{3,}", t) if w not in STOP)


def load_rows(W):
    rows = []
    for f in sorted(glob.glob(str(W / 'candidates' / 'cand_*.json'))) + [str(W / 'candidates_55.json')]:
        if not Path(f).exists():
            continue
        d = json.load(open(f, encoding='utf-8'))
        d = d if isinstance(d, list) else d.get('items') or d.get('stories') or []
        rows += [x for x in d if isinstance(x, dict) and x.get('title')]
    return rows


def clusters(rows):
    T = [toks(r['title']) for r in rows]
    n = len(rows)
    par = list(range(n))

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    inv = {}
    for i, t in enumerate(T):
        for w in t:
            inv.setdefault(w, []).append(i)
    for w, ids in inv.items():
        if len(ids) > 200:
            continue
        for a in range(len(ids)):
            for b in range(a + 1, len(ids)):
                i, j = ids[a], ids[b]
                if find(i) == find(j):
                    continue
                inter = len(T[i] & T[j])
                if inter >= 3 and inter / min(len(T[i]), len(T[j])) >= 0.6:
                    par[find(i)] = find(j)
    cl = {}
    for i in range(n):
        cl.setdefault(find(i), []).append(i)
    return cl, T


def pool_match(tk, pool, ptoks):
    best = None
    for p, pt in zip(pool, ptoks):
        inter = len(tk & pt)
        if inter >= 3 and inter / min(len(tk), len(pt)) >= 0.5:
            if best is None or p.get('importance', 0) > best.get('importance', 0):
                best = p
    return best


def pool_of(W):
    pool_path = next(iter(sorted(glob.glob(str(W / 'out' / 'AIND_Pool_*.json')))), None)
    return json.load(open(pool_path, encoding='utf-8')) if pool_path else []


def sweep(W):
    rows = load_rows(W)
    cl, T = clusters(rows)
    pool = pool_of(W)
    ptoks = [toks(p['title']) for p in pool]
    out = []
    for ids in cl.values():
        outlets = sorted({(rows[i].get('source') or '?') for i in ids})
        if len(outlets) < 8:
            continue
        pm = None
        for i in ids:
            m = pool_match(T[i], pool, ptoks) if pool else None
            if m and (pm is None or m.get('importance', 0) > pm.get('importance', 0)):
                pm = m
        out.append({'title': rows[ids[0]]['title'], 'outlets': len(outlets), 'floor': FLOOR if len(outlets) >= THRESHOLD else 0,
                    'in_pool': pm['item_id'] if pm else None, 'pool_score': pm.get('importance') if pm else None,
                    'example_links': [rows[i].get('link') for i in ids[:3]], 'outlet_names': outlets[:40]})
    out.sort(key=lambda x: -x['outlets'])
    for k, c in enumerate(out, 1):
        c['cluster'] = k
    json.dump({'clusters': out}, open(W / 'viral.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print(f"{len(rows)} candidate rows; stories carried by {THRESHOLD} or more distinct outlets get a score of at least {FLOOR}:")
    for c in out:
        if c['floor']:
            need = 'NEEDS ENTRY' if not c['in_pool'] else ('RAISE' if (c['pool_score'] or 0) < FLOOR else 'ok')
            print(f"  #{c['cluster']:>2} {c['outlets']:>3} outlets  {need:11} pool: {c['in_pool'] or 'NOT IN POOL'}"
                  f"{' at ' + str(c['pool_score']) if c['pool_score'] is not None else ''} | {c['title'][:85]}")
    near = [c for c in out if not c['floor']]
    print(f"{len(near)} more stories carried by 8 to {THRESHOLD - 1} outlets (no floor)")
    low = [c for c in out if c['in_pool'] and c['pool_score'] is not None and c['pool_score'] <= 4]
    print('LOW SCORE, HIGH REACH (pool score 4 or lower, 8 or more outlets):', len(low))
    for c in low:
        print(f"  {c['in_pool']} score {c['pool_score']} {c['outlets']} outlets | {c['title'][:90]}")


def check(W):
    v = json.load(open(W / 'viral.json', encoding='utf-8'))['clusters']
    ex_path = W / 'viral_exclude.json'
    excluded = set(json.load(open(ex_path, encoding='utf-8')).get('clusters', [])) if ex_path.exists() else set()
    pool = pool_of(W)
    bad = 0
    for c in v:
        if not c['floor'] or c['cluster'] in excluded:
            continue
        pm = next((p for p in pool if p['item_id'] == c['in_pool']), None) if c.get('in_pool') else None
        if pm is None:
            ptoks = [toks(p['title']) for p in pool]
            pm = pool_match(toks(c['title']), pool, ptoks)
        pool_ok = pm is not None and pm.get('importance', 0) >= FLOOR
        entry_score = None
        if pm:
            ep = W / 'report_entries' / f"{pm['item_id']}.json"
            if ep.exists():
                entry_score = json.load(open(ep, encoding='utf-8')).get('score')
        entry_ok = entry_score is None or entry_score >= FLOOR
        status = 'OK  ' if pool_ok and entry_ok else 'FAIL'
        bad += status == 'FAIL'
        print(f"{status} #{c['cluster']} {c['outlets']} outlets | pool {pm['item_id'] if pm else 'MISSING'} at {pm.get('importance') if pm else '-'}"
              f" | entry score {entry_score} | {c['title'][:80]}")
    print('viral check:', 'all floors met' if not bad else f'{bad} FAIL')


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('mode', choices=['sweep', 'check'])
    ap.add_argument('--workdir', required=True)
    a = ap.parse_args()
    (sweep if a.mode == 'sweep' else check)(Path(a.workdir))
