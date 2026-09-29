"""Step 7. First check (structure and data) of the written entries, and the held-back list.

    python qa_check.py --workdir W

Checks every W/report_entries/<id>.json against the pool: missing fields, wrong V1 category,
label not matching the score, Google or cut-off links, headlines copied from the publisher,
long summaries, notes left in the source name, process notes leaking into the text
("could not read", "blocked", ...), and old news re-dated into the window.
Writes W/qa1_problems.json and W/held.json. held.json keeps anything already in it:
the editor adds same-story duplicates by hand as {"duplicate": {"C13-01": "same story as C05-01"}}
and may add more re-dated items to "stale_redated".
Prints how many stories each score cutoff would give, for the report and the bulletin.
"""
import argparse, collections, difflib, glob, json, re
from datetime import timedelta
from pathlib import Path

from common import FUN, band, load_run, parse_utc, pool_path

MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
LEAK = re.compile(r"\bwe (could not|couldn.t|did not|were unable)|headline only|headline-only|only the headline|"
                  r"blocked|proxy|paywall|\bwe read\b|unreadable|not readable|\bchunk", re.I)   # advisory: an editor decides
FIELDS = ['v1_category', 'headline', 'score', 'importance_label', 'importance_line', 'source', 'status',
          'summary', 'url', 'freshness', 'verified_text']
V1 = {'POL', 'MKT', 'SEC', 'ENE', 'ROB', 'MOD', 'RES', 'LAW', 'HEA', 'SOC', 'FUN'}


def event_date(freshness, default_year):
    m = re.search(r'FOLLOW-UP of (.+)', str(freshness or ''))
    if not m:
        return None
    t = m.group(1)
    d = re.search(r'(\d{4})-(\d{2})-(\d{2})', t)
    if d:
        return tuple(map(int, d.groups()))
    d = re.search(r'(\d{1,2})\s*(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s*(\d{4})?', t)
    if d:
        return (int(d.group(3) or default_year), MON.index(d.group(2)[:3]) + 1, int(d.group(1)))
    return 'unparsed'


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--workdir', required=True)
    a = ap.parse_args()
    W = Path(a.workdir); run = load_run(W)
    pool = {p['item_id']: p for p in json.loads(pool_path(W, run).read_text(encoding='utf-8'))}
    fixes = json.loads((W / 'url_fixes.json').read_text()) if (W / 'url_fixes.json').exists() else {}
    # older than the day before the window starts = old news re-dated into the window
    cut = parse_utc(run['start']).date() - timedelta(days=1)
    cutoff = (cut.year, cut.month, cut.day)

    E = {}
    for f in sorted(glob.glob(str(W / 'report_entries' / '*.json'))):
        e = json.load(open(f, encoding='utf-8')); E[e['item_id']] = e
    print('entries', len(E), 'of', len(pool), '| missing', sorted(set(pool) - set(E)))
    P = collections.defaultdict(list)
    for k, e in E.items():
        p = pool[k]
        for fld in FIELDS:
            if fld not in e or e[fld] in (None, ''):
                P['missing_field'].append((k, fld))
        if e.get('v1_category') not in V1:
            P['bad_v1'].append((k, e.get('v1_category')))
        if p['category_id'] == FUN and e.get('v1_category') != 'FUN':
            P['fun_not_FUN'].append(k)
        try:
            if e.get('importance_label') != band(e.get('score', 0)):
                P['label_mismatch'].append((k, e.get('score'), e.get('importance_label')))
        except (TypeError, ValueError):
            P['bad_score'].append((k, e.get('score')))
        u = e.get('url', '')
        if 'news.google.com' in u:
            P['google_link'].append(k)
        if u in fixes:
            P['link_has_fix'].append(k)
        elif '?' in u and not re.search(r'\?[^=]+=', u):
            P['link_maybe_cut'].append((k, u))
        r = difflib.SequenceMatcher(None, e.get('headline', '').lower(), p['title'].lower()).ratio()
        if r > 0.85:
            P['headline_copies_source_title'].append((k, round(r, 2)))
        if len(re.findall(r'[.!?](\s|$)', e.get('summary', ''))) > 3:
            P['summary_long'].append(k)
        if re.search(r'\(|;|via |blocked', e.get('source', '')):
            P['source_has_notes'].append((k, e.get('source')))
        for fld in ('headline', 'summary', 'importance_line'):   # the fields the PDF prints
            if LEAK.search(str(e.get(fld, ''))):
                P['process_note_in_text'].append((k, fld))
        d = event_date(e.get('freshness'), parse_utc(run['end']).year)
        if d == 'unparsed':
            P['freshness_unparsed'].append((k, e.get('freshness')))
        elif d and d < cutoff and not p.get('follow_up'):
            P['stale_redated'].append((k, e.get('freshness'), p['importance']))
    for k, v in P.items():
        print(f'{k}: {len(v)}', v[:12])
    (W / 'qa1_problems.json').write_text(json.dumps(P, indent=1, ensure_ascii=False), encoding='utf-8')

    hp = W / 'held.json'
    held = json.loads(hp.read_text()) if hp.exists() else {'stale_redated': [], 'duplicate': {}}
    held['stale_redated'] = sorted(set(held.get('stale_redated', [])) | {x[0] for x in P['stale_redated']})
    held.setdefault('duplicate', {})
    hp.write_text(json.dumps(held, indent=1))
    H = set(held['stale_redated']) | set(held['duplicate'])
    print('held back', len(H), f"({len(held['stale_redated'])} re-dated, {len(held['duplicate'])} duplicate)")

    ok = {k: e for k, e in E.items() if k not in H}
    score = lambda k: int(float(pool[k]['importance']))
    for t in range(8, 3, -1):
        rep = [k for k in ok if score(k) >= t or pool[k]['category_id'] == FUN]
        print(f'report at {t}+ (plus Fun): {len(rep)} | headline only {sum(1 for k in rep if not ok[k].get("verified_text"))}')
    for t in (8, 7, 6, 5):
        bul = [k for k in ok if score(k) >= t and pool[k]['category_id'] != FUN]
        print(f'bulletin at {t}+: {len(bul)} | headline only {sum(1 for k in bul if not ok[k].get("verified_text"))}')


if __name__ == '__main__':
    main()
