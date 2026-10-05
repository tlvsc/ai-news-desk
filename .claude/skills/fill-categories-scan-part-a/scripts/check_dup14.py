"""Last stage before the final build: compare the day's report entries with the Full Reports of the
previous 14 days (Rafi, 5 Oct 2026: "the last stage of remove duplicate is compare to 14 days previous
full reports in drive").

    python3 check_dup14.py --workdir W [--archive W/archive14] [--days 14] [--hold]

W/archive14/<YYYY-MM-DD>.md are the previous days' Full Report texts, saved from Drive (read only) by the
Drive setup agent with drive_save.py. A day with no report text is listed as a GAP; its pool CSV from the
repo (runs/<date>/out) is not compared here (build_pool already checks 4 days of pools).

An entry is a REPEAT when its distinctive words (names, numbers, long words) overlap an earlier report line
by at least 0.5 and at least 3 words, and the pool does not mark it as a follow-up with new facts.
--hold writes the REPEATS into W/held.json under "duplicate" ("repeat of <date>"); every line is printed
first so a human or the main session can undo a false match by removing it from held.json.
"""
import argparse, glob, json, re, sys
from datetime import date, timedelta
from pathlib import Path

from common import load_run, pool_path

STOP = set("with from that this have will been their about after over into more than says said also first which would could "
           "they them were what when your some most only other while where there these those after before report reports "
           "reported according source status summary reuters confirmed daily date category score rank "
           "monday tuesday wednesday thursday friday saturday sunday january february march april june july august september "
           "october november december 2026 street journal wall times financial post news bloomberg group company companies "
           "reports said statement announced announces announcement investors market markets chief executive officer "
           "president government people research researchers according system systems artificial intelligence".split())


def distinct(s):
    out = set()
    for w in re.findall(r"[A-Za-z0-9][A-Za-z0-9\-\.\$%]*", s):
        lw = w.lower().strip('.-')
        if lw in STOP or len(lw) < 4 and not any(c.isdigit() for c in lw):
            continue
        if w[0].isupper() or any(c.isdigit() for c in w) or len(lw) >= 7:
            out.add(lw)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--workdir', required=True)
    ap.add_argument('--archive')
    ap.add_argument('--days', type=int, default=14)
    ap.add_argument('--hold', action='store_true')
    a = ap.parse_args()
    W = Path(a.workdir); run = load_run(W)
    arch = Path(a.archive) if a.archive else W / 'archive14'
    ed = date.fromisoformat(run['edition'])
    want = [(ed - timedelta(days=i)).isoformat() for i in range(1, a.days + 1)]
    lines, have = [], []
    for d in want:
        f = arch / f'{d}.md'
        if not f.exists():
            continue
        have.append(d)
        for ln in f.read_text(encoding='utf-8', errors='ignore').split('\n'):
            t = distinct(ln)
            if len(t) >= 4:
                lines.append((d, ln.strip(), t))
    gaps = [d for d in want if d not in have]
    print(f'compared with {len(have)} of {a.days} previous Full Reports ({len(lines)} lines) | GAP days: {gaps or "none"}')
    pool = {p['item_id']: p for p in json.loads(pool_path(W, run).read_text(encoding='utf-8'))}
    held = json.loads((W / 'held.json').read_text()) if (W / 'held.json').exists() else {'stale_redated': [], 'duplicate': {}}
    gone = set(held.get('stale_redated', [])) | set(held.get('duplicate', {}))
    repeats = []
    for f in sorted(glob.glob(str(W / 'report_entries' / '*.json'))):
        k = Path(f).stem
        if k in gone:
            continue
        e = json.loads(Path(f).read_text(encoding='utf-8'))
        q = distinct(e.get('headline', '') + ' ' + e.get('summary', '')[:260])
        if len(q) < 4:
            continue
        best = (0, '', '')
        for d, ln, t in lines:
            sh = q & t
            sc = len(sh) / min(len(q), len(t))
            if (len(sh) >= 4 or (len(sh) >= 3 and sc >= 0.67)) and sc > best[0]:
                best = (sc, d, ln)
        p = pool.get(k, {})
        if best[0] >= 0.5:
            repeats.append((k, round(best[0], 2), best[1], bool(p.get('follow_up')), e.get('headline', '')[:80], best[2][:110]))
    for k, sc, d, fu, h, ln in sorted(repeats):
        print(f"{'FOLLOW-UP kept' if fu else 'REPEAT'}  {k}  {sc}  {d}  | {h}\n      earlier: {ln}")
    rep = [r for r in repeats if not r[3]]
    print(f'{len(rep)} repeats, {len(repeats) - len(rep)} follow-ups kept')
    if a.hold:
        for k, sc, d, fu, h, ln in rep:
            held['duplicate'][k] = f'repeat of the {d} Full Report (14 day check)'
        (W / 'held.json').write_text(json.dumps(held, indent=1))
        print('written to held.json; run build_products.py again')


if __name__ == '__main__':
    main()
