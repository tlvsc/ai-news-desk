"""VIRAL RULE (Rafi, 10 Oct 2026; CLAUDE.md VIRAL RULE): count how many distinct outlets carry the same story, set a score floor.

    python3 viral_sweep.py sweep --workdir W            # step 1c, before the curators: writes W/viral.json and prints the list
    python3 viral_sweep.py check --workdir W            # after build_pool, after the writers, before the build: every floor is met

Floors (CLAUDE.md): 10 or more distinct outlets -> score at least 7; 20 or more -> 8; 30 or more, or 20 or more with at least 3 top outlets -> 9 (my reading of "top outlet leading").
At most 3 floors a day, only for stories about AI: the script lists up to MAX_LIST clusters (outlets, floor, whether the
story is already in the pool and at what score); the MAIN SESSION picks at most 3 that are about AI and writes them into
W/viral_picks.json {"picks": [{"cluster": 1, "note": "why"}]}. The curators get the picks as must-includes and the pool
and the writers must keep each pick at its floor (the writers cannot lower it; they still check facts and dates).

Also prints the LOW SCORE, HIGH REACH list: stories in the pool at score 4 or lower that 8 or more outlets carry, for
Rafi to read with the delivery (CLAUDE.md VIRAL RULE: a 3 or 4 is not final for a story with wide reach).

Reads W/candidates/cand_*.json and W/candidates_55.json (title, source, link, published) and, when it exists,
W/out/AIND_Pool_<edition>.json. Matching is by title words (a first version; V1 needs a real story identity).
"""
import argparse, glob, json, re
from pathlib import Path

TOP = {'bbc', 'bbc news', 'reuters', 'cbs news', 'ap', 'ap news', 'associated press', 'the new york times', 'new york times',
       'bloomberg', 'bloomberg.com', 'the wall street journal', 'wsj', 'cnn', 'the guardian', 'financial times', 'the washington post',
       'washington post', 'nbc news', 'abc news', 'npr', 'axios', 'the verge', 'techcrunch', 'cnbc'}
STOP = set('the a an of to in on for and with by at from as is are be its it that this how what why new says say said after over into about up out '
           'will can has have more not or than their his her they you your ai'.split())
MAX_LIST = 8
TOP_MIN_COUNT = 3
TOP_MIN_OUTLETS = 20


def toks(t):
    t = re.sub(r' - [^-]{2,40}$', '', t.lower())
    return frozenset(w for w in re.findall(r"[a-z0-9']{3,}", t) if w not in STOP)


def floor_for(n, top_count):
    # "top outlet leading" (CLAUDE.md) is read here as: 20 or more outlets and at least 3 of the top outlets carry it
    # (my reading of 10 Oct 2026; Rafi to confirm or change TOP_MIN_COUNT and TOP_MIN_OUTLETS)
    if n >= 30 or (top_count >= TOP_MIN_COUNT and n >= TOP_MIN_OUTLETS):
        return 9
    if n >= 20:
        return 8
    if n >= 10:
        return 7
    return 0


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


def sweep(W):
    rows = load_rows(W)
    cl, T = clusters(rows)
    pool_path = next(iter(sorted(glob.glob(str(W / 'out' / 'AIND_Pool_*.json')))), None)
    pool = json.load(open(pool_path, encoding='utf-8')) if pool_path else []
    ptoks = [toks(p['title']) for p in pool]
    out = []
    for ids in cl.values():
        outlets = sorted({(rows[i].get('source') or '?') for i in ids})
        if len(outlets) < 8:
            continue
        top_count = sum(1 for o in outlets if o.lower() in TOP)
        title = rows[ids[0]]['title']
        pm = None
        for i in ids:
            m = pool_match(T[i], pool, ptoks) if pool else None
            if m and (pm is None or m.get('importance', 0) > pm.get('importance', 0)):
                pm = m
        out.append({'title': title, 'outlets': len(outlets), 'top_outlets': [o for o in outlets if o.lower() in TOP][:6],
                    'floor': floor_for(len(outlets), top_count),
                    'in_pool': pm['item_id'] if pm else None, 'pool_score': pm.get('importance') if pm else None,
                    'example_links': [rows[i].get('link') for i in ids[:3]]})
    out.sort(key=lambda x: -x['outlets'])
    for k, c in enumerate(out, 1):
        c['cluster'] = k
    json.dump({'clusters': out}, open(W / 'viral.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print(f"{len(rows)} candidate rows, {len(out)} stories carried by 8 or more distinct outlets (floors: 10 -> 7, 20 -> 8, 30 or top outlet leading -> 9)")
    for c in out[:MAX_LIST]:
        print(f"  #{c['cluster']:>2} {c['outlets']:>3} outlets floor {c['floor'] or '-'}  pool: {c['in_pool'] or 'NOT IN POOL'}"
              f"{' at ' + str(c['pool_score']) if c['pool_score'] is not None else ''} | {c['title'][:90]}")
    low = [c for c in out if c['in_pool'] and c['pool_score'] is not None and c['pool_score'] <= 4]
    print('LOW SCORE, HIGH REACH (pool score 4 or lower, 8 or more outlets):', len(low))
    for c in low:
        print(f"  {c['in_pool']} score {c['pool_score']} {c['outlets']} outlets | {c['title'][:90]}")
    print('Next: the main session picks at most 3 stories about AI and writes W/viral_picks.json {"picks": [{"cluster": N, "note": "..."}]}')


def check(W):
    v = json.load(open(W / 'viral.json', encoding='utf-8'))['clusters']
    picks_path = W / 'viral_picks.json'
    picks = json.load(open(picks_path, encoding='utf-8'))['picks'] if picks_path.exists() else []
    if len(picks) > 3:
        print('FAIL: more than 3 viral picks')
    pool_path = next(iter(sorted(glob.glob(str(W / 'out' / 'AIND_Pool_*.json')))), None)
    pool = json.load(open(pool_path, encoding='utf-8')) if pool_path else []
    ptoks = [toks(p['title']) for p in pool]
    bad = 0
    for pk in picks:
        c = next((x for x in v if x['cluster'] == pk['cluster']), None)
        if not c:
            print('FAIL: unknown cluster', pk)
            bad += 1
            continue
        pm = None
        for ttl in [c['title']]:
            pm = pool_match(toks(ttl), pool, ptoks)
        if c.get('in_pool'):
            pm = next((p for p in pool if p['item_id'] == c['in_pool']), pm)
        pool_ok = pm is not None and pm.get('importance', 0) >= c['floor']
        entry_score = None
        if pm:
            ep = W / 'report_entries' / f"{pm['item_id']}.json"
            if ep.exists():
                entry_score = json.load(open(ep, encoding='utf-8')).get('score')
        entry_ok = entry_score is None or entry_score >= c['floor']
        status = 'OK  ' if pool_ok and entry_ok else 'FAIL'
        bad += status == 'FAIL'
        print(f"{status} #{c['cluster']} floor {c['floor']} | pool {pm['item_id'] if pm else 'MISSING'} at {pm.get('importance') if pm else '-'}"
              f" | entry score {entry_score} | {c['title'][:80]}")
    print('viral check:', 'all floors met' if not bad else f'{bad} FAIL')


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('mode', choices=['sweep', 'check'])
    ap.add_argument('--workdir', required=True)
    a = ap.parse_args()
    (sweep if a.mode == 'sweep' else check)(Path(a.workdir))
