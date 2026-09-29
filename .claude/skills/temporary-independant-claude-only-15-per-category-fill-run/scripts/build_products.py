"""Steps 8 and 11. Assemble the V1 Full Report and Daily Bulletin from the written entries.

    python build_products.py --workdir W [--report-min auto|N] [--bulletin-min auto|N]

Selection (CLAUDE.md rule 14): stories not held back, with pool score at or above the
report cutoff, plus every Fun Side story, go in the report; report stories at or above the
bulletin cutoff, minus Fun, go in the bulletin. "auto" picks the cutoff whose count lands
closest to 50-150 for the report (tries 8 down to 1) and 30-50 for the bulletin (8 down
to 5), the higher cutoff on a tie. The shown score is the pool score; the writer's own score is kept as fc_score.
Writes to W/products: the report and bulletin markdown, report_pdf.json and bulletin_pdf.json
(the input of build_pdf.py), daily-pool.md, and W/report_ids.json (report items split in
two halves for the two editors). The Bigger Picture comes from W/bigger_picture.json when
it exists ({Cnn-nn} references become report item numbers); on the first pass it is missing.
Optional W/known_gaps.txt adds lines to the Known gaps section of daily-pool.md.
"""
import argparse, glob, json, re
from datetime import datetime, timezone
from pathlib import Path

from common import (FUN, NAMES, ORDER, WEEKDAYS, band, edition, load_run, long_date, parse_utc,
                    pool_path, window_text)


def pick(counts, lo, hi, target):
    """The cutoff whose story count lands closest to the target range (CLAUDE.md rule 14);
    on a tie, the higher cutoff."""
    a, b = target
    dist = lambda n: 0 if a <= n <= b else (a - n if n < a else n - b)
    return min(range(hi, lo - 1, -1), key=lambda t: (dist(counts(t)), -t))


def clean_source(src):
    src = re.split(r"\s\(|;|, via | — ", src or "")[0].strip()
    return src.split(",")[0].strip() if len(src) > 45 else src


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--workdir', required=True)
    ap.add_argument('--report-min', default='auto')
    ap.add_argument('--bulletin-min', default='auto')
    a = ap.parse_args()
    W = Path(a.workdir); run = load_run(W); OUT = W / 'products'; OUT.mkdir(exist_ok=True)
    ed = edition(run); DATE = long_date(ed); WINDOW = window_text(run)
    end = parse_utc(run['end'])

    pool = {x['item_id']: x for x in json.loads(pool_path(W, run).read_text(encoding='utf-8'))}
    entries = []
    for f in sorted(glob.glob(str(W / 'report_entries' / '*.json'))):
        e = json.load(open(f, encoding='utf-8'))
        e['v1_category'] = e.get('v1_category') or ('FUN' if pool[e['item_id']]['category_id'] == FUN else 'MOD')
        e['fc_score'] = int(e['score'])
        e['score'] = int(float(pool[e['item_id']]['importance']))
        e['importance_label'] = band(e['score'])
        entries.append(e)
    hp = W / 'held.json'
    HELD = json.loads(hp.read_text()) if hp.exists() else {'stale_redated': [], 'duplicate': {}}
    held_ids = set(HELD['stale_redated']) | set(HELD['duplicate'])
    held = [e for e in entries if e['item_id'] in held_ids]
    live = [e for e in entries if e['item_id'] not in held_ids]

    in_rep = lambda e, t: e['score'] >= t or e['v1_category'] == 'FUN'
    rmin = pick(lambda t: sum(in_rep(e, t) for e in live), 1, 8, (50, 150)) if a.report_min == 'auto' else int(a.report_min)
    report = [e for e in live if in_rep(e, rmin)]
    report.sort(key=lambda e: (ORDER.index(e['v1_category']), -e['score'], e['item_id']))
    in_bul = lambda e, t: e['score'] >= t and e['v1_category'] != 'FUN'
    bmin = pick(lambda t: sum(in_bul(e, t) for e in report), 5, 8, (30, 50)) if a.bulletin_min == 'auto' else int(a.bulletin_min)
    bulletin = [e for e in report if in_bul(e, bmin)]

    for n, e in enumerate(report, 1):
        e['n'] = n
    for k in ORDER:
        grp = [e for e in report if e['v1_category'] == k]
        for r, e in enumerate(grp, 1):
            e['rank'], e['rank_of'] = r, len(grp)
    num = {e['item_id']: e['n'] for e in report}
    refs = lambda text: re.sub(r"\{(C\d\d-\d\d)\}", lambda m: f"(item {num.get(m.group(1), '?')})", text)

    bpf = W / 'bigger_picture.json'
    bp = json.loads(bpf.read_text(encoding='utf-8')) if bpf.exists() else None
    if bp:
        missing = [r for s in bp['sections'] for p in s['paragraphs'] for r in re.findall(r"\{(C\d\d-\d\d)\}", p)
                   if r not in num]
        if missing:
            print('WARNING: Bigger Picture cites items not in the report:', missing)
    headline_only = sum(1 for e in report if not e.get('verified_text'))
    followups = sum(1 for e in report if str(e.get('freshness', '')).upper().startswith('FOLLOW'))
    spread = {b: sum(1 for e in report if e['importance_label'] == b) for b in ['CRITICAL', 'HIGH', 'MEDIUM', 'WATCHLIST']}
    rule_r = f"pool score {rmin} to 10 plus The Fun Side"
    rule_b = f"every story scored {bmin} to 10"

    # ---------- Full Report markdown (the card renderer reads it as report_file)
    L = ["# Daily Global AI Intelligence Report (Claude LV1.1) — TEST RUN", "",
         f"Daily report date: {WEEKDAYS[ed.weekday()]}, {DATE}  ",
         f"Coverage period: {WINDOW}  ",
         f"Final unique stories: {len(report)} (pool {len(pool)}; report rule: {rule_r}; {len(held)} pool stories held back as older news re-dated into the window or duplicates)  ",
         f"Score spread: CRITICAL {spread['CRITICAL']}, HIGH {spread['HIGH']}, MEDIUM {spread['MEDIUM']}, WATCHLIST {spread['WATCHLIST']}  ",
         f"Stories with full article text read: {len(report) - headline_only}; headline only: {headline_only}; follow-ups of earlier news: {followups}  ",
         "Source coverage certificate: SOURCE SCAN INCOMPLETE. Stories were collected through Google News; articles were read from the 101-source list where the sites allowed it. Test run approved by Rafi.  ",
         ("Coverage QA: ATTENTION REQUIRED — some publisher sites block automated reading, so some stories rest on headlines only."
          if headline_only else "Coverage QA: every story was read in full."), ""]
    for k in ORDER:
        grp = [e for e in report if e['v1_category'] == k]
        L += [f"## {NAMES[k].upper()} — {len(grp)}", ""]
        if not grp:
            L += ["No qualifying items found for this reporting window.", ""]
        for e in grp:
            L.append(f"{e['n']}. {e['headline']}")
            L.append(f"CATEGORY: {NAMES[k]} — rank {e['rank']} of {e['rank_of']} in this category")
            L.append(f"SCORE: {e['score']} — {e.get('score_reason', '')}")
            L.append(f"Importance: {e['importance_label']} — {e.get('importance_line', '')}")
            L.append(f"Source: {e.get('source', '')}. Status: {e.get('status', '')}." + ("" if e.get('verified_text') else " (Headline only: full article not readable.)"))
            L.append(f"Summary: {e.get('summary', '')}")
            L.append(f"Full article: {e.get('url', '')}")
            L += ["---", ""]
    if bp:
        L += [f"## {bp['title'].upper()}", "", f"*{bp['description']}*", ""]
        for s in bp['sections']:
            L += [f"### {s['title']}", ""] + [refs(p) + "\n" for p in s['paragraphs']]
    REPORT_MD = OUT / f"{ed.isoformat()} — Daily Global AI Intelligence Report (Claude LV1.1).md"
    REPORT_MD.write_text("\n".join(L), encoding="utf-8")

    # ---------- Bulletin markdown
    BL = ["# Daily Bulletin (Claude LV1.1) — TEST RUN", "", f"{DATE}. Coverage: {WINDOW}.  ",
          f"Source: the Full Report only. Order: category order of 23 Sep, highest score first. Rule: {rule_b} (cutoff set to the day's pool, CLAUDE.md rule 14).  ",
          f"**{len(bulletin)} stories.**", ""]
    for k in ORDER[:-1]:
        grp = [e for e in bulletin if e['v1_category'] == k]
        BL.append(f"## {NAMES[k].upper()} — {len(grp)}")
        if not grp:
            BL.append(f"No story scored {bmin} or more today; see the Full Report.")
        for e in grp:
            BL.append(f"**{e['score']} {e['importance_label']} — {e['headline']}** (report item {e['n']})  ")
            BL.append(f"{e.get('summary', '')} *{e.get('source', '')}, {e.get('status', '')}*" + ("" if e.get('verified_text') else " *(headline only)*"))
            BL.append("")
    BL += ["## CHECKS", "", f"- Stories: {len(bulletin)}; all come from the Full Report with facts, scores and sources unchanged.",
           f"- Fact check suggested a lower score for {sum(1 for e in bulletin if e['fc_score'] < e['score'])} of these stories (stale, overstated or headline only); selection follows the pool score as Rafi ruled.",
           f"- Headline-only stories included: {sum(1 for e in bulletin if not e.get('verified_text'))}."]
    (OUT / f"{ed.isoformat()} — Daily Bulletin (Claude LV1.1).md").write_text("\n".join(BL), encoding="utf-8")

    # ---------- PDF inputs (Full_Report_V1_Rules_Structure section 8)
    def pdf_item(e):
        paras = [e.get('summary', '')]
        if e.get('importance_line'):
            paras.append("Why it matters: " + e['importance_line'])
        if not e.get('verified_text'):
            paras.append("Note: we could not open the original article; this entry relies on its headline and related coverage.")
        return {"headline": e['headline'], "score": e['score'], "importance": e['importance_label'], "rank": e['rank'],
                "rank_of": e['rank_of'], "status": e.get('status', ''), "paragraphs": paras,
                "source": clean_source(e.get('source', '')), "url": e.get('url', '')}

    about = {"title": "About this edition", "paragraphs": [
        f"This is a test edition. Stories were collected through Google News for the {run['hours']} hours ending {end:%H:%M} UTC on {long_date(end.date())}, and articles were read from our 101-source list where the sites allowed it.",
        f"We read the full article for {len(report) - headline_only} of {len(report)} stories. The rest are marked as headline only because their websites could not be opened from our system.",
        "Scores run from 1 to 10: 10 is critical, 8 and 9 high, 6 and 7 medium, 5 and below watchlist. Nothing here is investment advice."]}
    cats = lambda sel: [{"name": NAMES[k], "items": [pdf_item(e) for e in sel if e['v1_category'] == k]}
                        for k in ORDER if any(e['v1_category'] == k for e in sel)]
    extra = [about]
    if bp:
        extra.insert(0, {"title": bp['title'], "paragraphs": [bp['description']] + [
            f"{s['title']}. " + " ".join(refs(p) for p in s['paragraphs']) for s in bp['sections']]})
    rep_json = {"title": "Full Report", "date": DATE,
                "purpose": "The day's comprehensive AI intelligence report: every story we kept from today's pool, grouped by subject and ranked by importance.",
                "coverage": f"{WINDOW} · {len(report)} stories · {len(cats(report))} categories",
                "categories": cats(report), "extra_sections": extra}
    bul_json = {"title": "Daily Bulletin", "date": DATE,
                "purpose": f"A concise selection of the day's most important AI developments, taken from the Full Report: every story scored {bmin} or more.",
                "coverage": f"{WINDOW} · {len(bulletin)} stories",
                "categories": cats(bulletin), "extra_sections": [about]}
    (OUT / 'report_pdf.json').write_text(json.dumps(rep_json, indent=1, ensure_ascii=False), encoding='utf-8')
    (OUT / 'bulletin_pdf.json').write_text(json.dumps(bul_json, indent=1, ensure_ascii=False), encoding='utf-8')
    ids = [e['item_id'] for e in report]
    (W / 'report_ids.json').write_text(json.dumps({'A': ids[:len(ids) // 2], 'B': ids[len(ids) // 2:]}, indent=1))

    # ---------- daily-pool.md: the pool and what happened to each story
    log = json.loads((W / 'out' / 'build_log.json').read_text(encoding='utf-8')) if (W / 'out' / 'build_log.json').exists() else {}
    E = {e['item_id']: e for e in entries}
    bh, rh = {e['item_id'] for e in bulletin}, {e['item_id'] for e in report}
    cands = sum(len(json.load(open(f, encoding='utf-8'))) for f in glob.glob(str(W / 'candidates' / 'cand_*.json')))

    def outcome(k):
        if k in HELD['duplicate']:
            return 'held: ' + HELD['duplicate'][k]
        if k in held_ids:
            return 'held: older news re-dated into the window (' + E.get(k, {}).get('freshness', '') + ')'
        if k in bh:
            return 'Full Report + Bulletin'
        if k in rh:
            return 'Full Report'
        return 'not written' if k not in E else f'pool only (pool score below {rmin})'
    per_cat = {}
    for p in pool.values():
        per_cat[p['category']] = per_cat.get(p['category'], 0) + 1
    P = [f"# daily-pool.md — {ed.isoformat()} (Claude lane, test run)", "",
         f"Edition date: {ed.isoformat()} (Asia/Jerusalem)  ", f"Reporting window: {WINDOW}  ",
         f"Run identity: Claude Code cloud session; Google News collection, 16 curator agents (LV2 16-category taxonomy), 16 read-and-write agents, V1 11-category mapping; skill Temporary_independant_claude_only_15_per_category_fill_run  ",
         f"Last updated: {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC  ",
         "Status: PARTIAL — stories collected through Google News; articles read from the 101-source list where sites allowed it", "",
         "## Counts", "", f"- Raw dated candidates collected inside the window: {cands}",
         f"- Curated pool: {len(pool)} (per category: " + ", ".join(f"{k} {v}" for k, v in per_cat.items()) + ")",
         f"- Removed at pool build: {len(log.get('manual_drops', []))} by the editor, {len(log.get('dupe_cross', []))} same stories in two categories",
         f"- Held back after reading: {len(held_ids)} ({len(HELD['stale_redated'])} older news re-dated into the window, {len(HELD['duplicate'])} duplicate)",
         f"- Articles read: {sum(1 for e in entries if e.get('verified_text'))} of {len(entries)}; headline only: {sum(1 for e in entries if not e.get('verified_text'))}",
         f"- Full Report: {len(report)} ({rule_r}); Bulletin: {len(bulletin)} (pool score {bmin} to 10)", "",
         "## Removed at pool build", ""] + [f"- cat {c}: {t} — {w}" for c, t, w in log.get('manual_drops', [])] + [
         "", "## Curated pool (item, V1 category, pool score, outlet, published, title, link, outcome)", ""]
    for k in sorted(pool, key=lambda k: (ORDER.index(E[k]['v1_category']) if k in E else 99, -int(float(pool[k]['importance'])), k)):
        p = pool[k]; e = E.get(k, {})
        P.append(f"- {k} · {e.get('v1_category', '?')} · {int(float(p['importance']))} · {e.get('source') or p['source']} · "
                 f"{p['published']} · {p['title']} · {e.get('url') or p['url']} · {outcome(k)}")
    P += ["", "## Known gaps", "", f"- {headline_only} of {len(report)} Full Report stories rest on headlines only; their sites could not be opened from this session."]
    if (W / 'known_gaps.txt').exists():
        P += [f"- {x.strip()}" for x in (W / 'known_gaps.txt').read_text(encoding='utf-8').splitlines() if x.strip()]
    (OUT / 'daily-pool.md').write_text("\n".join(P) + "\n", encoding='utf-8')

    print(f"cutoffs: report {rmin}+ plus Fun, bulletin {bmin}+ | report {len(report)} (held {len(held)}), "
          f"bulletin {len(bulletin)}, headline-only {headline_only}, follow-ups {followups}, spread {spread}")
    print("bulletin by category", {k: sum(1 for e in bulletin if e['v1_category'] == k) for k in ORDER[:-1]})
    print("Bigger Picture:", "included" if bp else "MISSING (write W/bigger_picture.json, then run again)")


if __name__ == '__main__':
    main()
