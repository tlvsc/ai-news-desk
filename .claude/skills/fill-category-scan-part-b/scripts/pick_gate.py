"""Story choice for the cards and the Headlines (Rafi, 7 Oct 2026): the pack for the picker and the gate for its answer.

    python pick_gate.py pack --workdir W      # writes W/cards_work/pick_pack.json (+ .md): the Bulletin candidates, the reserve list, the last 7 days of decks
    python pick_gate.py gate --workdir W      # checks W/cards_work/selection_fable.json; writes gate_result.json and, only on PASS, selection.json

The picker is a Fable agent (CLAUDE.md MODEL POLICY, STORY CHOICE). The script holds no taste: it only checks what can be checked.
Numbers come from the CARD_FILTER line of CLAUDE.md; the category order from the Drive Cards Master copy in W/rules.
"""
import argparse, glob, hashlib, json, re, sys
from pathlib import Path
from card_candidates_lib import read_filter, read_order, NAME, COMPANIES, keys
from common_b import B, entry, edition_dates

REPO = B.parent.parent.parent
GENERIC = set('The A An AI OpenAI Google Anthropic Chinese US South This That It In On Our We Now After But And Its Meta Microsoft Nvidia Amazon Apple Tesla Reuters Bloomberg'.split())


def pn(s):
    return {w.lower() for w in re.findall(r"\b[A-Z][a-zA-Z0-9]+\b|\b\d[\d,.]*\b", s) if w not in GENERIC and len(w) > 2}


def heads_of(o):
    if isinstance(o, dict):
        for k in ('head', 'body', 'script'):
            if isinstance(o.get(k), str): yield o[k]
        for v in o.values(): yield from heads_of(v)
    elif isinstance(o, list):
        for v in o: yield from heads_of(v)


def old_decks(W, ed):
    """date -> list of text lines of the cards and Headlines of the 7 days before the edition."""
    from datetime import date, timedelta
    d0 = date.fromisoformat(ed); days = [(d0 - timedelta(days=i)).isoformat() for i in range(1, 8)]
    out = {d: [] for d in days}
    pats = ['cards_work/cards_copy_fable.json', 'cards_copy.json', 'headlines_work/scripts_final.json']
    for d in days:
        for base in (Path(W).parent / f'run_{d}', REPO / 'runs' / d):
            for p in pats:
                f = base / p
                if f.exists():
                    try: out[d] += list(heads_of(json.loads(f.read_text(encoding='utf-8'))))
                    except Exception: pass
        f = Path(W) / 'old_decks' / f'{d}_cards_copy.json'
        if f.exists():
            out[d] += list(heads_of(json.loads(f.read_text(encoding='utf-8'))))
        out[d] = sorted(set(out[d]))
    return out


def load(W):
    W = Path(W).resolve()
    held = json.loads((W / 'held.json').read_text())
    hid = set(held['stale_redated']) | set(held['duplicate'])
    bul = json.loads((W / 'products' / 'bulletin_pdf.json').read_text())
    rep = json.loads((W / 'products' / 'report_pdf.json').read_text())
    ents = {}
    for f in (W / 'report_entries').glob('C*.json'):
        e = json.loads(f.read_text(encoding='utf-8')); ents[e['item_id']] = e
    byhead = {e['headline']: e for e in ents.values()}
    bset = {byhead[it['headline']]['item_id'] for c in bul['categories'] for it in c['items'] if it['headline'] in byhead}
    rset = {byhead[it['headline']]['item_id'] for c in rep['categories'] for it in c['items'] if it['headline'] in byhead}
    return W, ents, hid, bset, rset


def brief(e):
    comp = [x for x in COMPANIES if re.search(rf'\b{x}\b', e['headline'])]
    return dict(id=e['item_id'], category=e['v1_category'], score=e['score'], freshness=e['freshness'], read_in_full=bool(e['verified_text']),
                status=e['status'], machine_action=e.get('machine_action'), companies=comp, headline=e['headline'], summary=e['summary'][:420])


def pack(W):
    W, ents, hid, bset, rset = load(W)
    ed = edition_dates(W)[0]
    cand = [brief(ents[i]) for i in sorted(bset) if i not in hid]
    reserve = [dict(id=i, category=ents[i]['v1_category'], score=ents[i]['score'], read_in_full=bool(ents[i]['verified_text']), freshness=ents[i]['freshness'][:24], headline=ents[i]['headline'])
               for i in sorted(rset - bset) if i not in hid]
    decks = old_decks(W, ed)
    out = dict(edition=ed, filter=read_filter(), category_order=read_order(W), bulletin_candidates=cand, reserve_from_report=reserve, last_7_days={d: v for d, v in decks.items()})
    p = W / 'cards_work' / 'pick_pack.json'; p.parent.mkdir(exist_ok=True)
    p.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding='utf-8')
    md = [f'# Pick pack {ed}', '', f'Filter: {out["filter"]}', f'Category order: {out["category_order"]}', '', '## Bulletin candidates (cards come from here)']
    for c in cand:
        md.append(f'- {c["id"]} [{c["category"]}] score {c["score"]} | {c["freshness"][:26]} | {"read" if c["read_in_full"] else "HEADLINE ONLY"} | {c["headline"]}\n    {c["summary"]}')
    md += ['', '## Reserve from the report (not in the Bulletin; only for a category with no eligible Bulletin story)']
    md += [f'- {r["id"]} [{r["category"]}] score {r["score"]} | {r["freshness"]} | {"read" if r["read_in_full"] else "HEADLINE ONLY"} | {r["headline"]}' for r in reserve]
    md += ['', '## Cards and Headlines of the last 7 days (a story that appears here must not come back)']
    for d in sorted(decks):
        md.append(f'### {d}' + ('' if decks[d] else '  (NO DECK TEXT AVAILABLE FOR THIS DAY)'))
        md += [f'- {t}' for t in decks[d]]
    (W / 'cards_work' / 'pick_pack.md').write_text('\n'.join(md), encoding='utf-8')
    gaps = [d for d, v in decks.items() if not v]
    print(f'pack: {len(cand)} Bulletin candidates, {len(reserve)} reserve, decks of {7 - len(gaps)} of 7 days; no deck text for: {gaps or "none"}')


def gate(W):
    W, ents, hid, bset, rset = load(W)
    F = read_filter(); ORDER = read_order(W); ed = edition_dates(W)[0]
    sel = json.loads((W / 'cards_work' / 'selection_fable.json').read_text(encoding='utf-8'))
    ua = W / 'cards_work' / 'update_allowed.json'; UA = set(json.loads(ua.read_text())) if ua.exists() else set()
    decks = old_decks(W, ed)
    res = []
    def chk(name, ok, why=''):
        res.append((name, bool(ok), why)); print(('PASS ' if ok else 'FAIL ') + name + ('' if ok else ' :: ' + why))
    cards = sel['cards']; ids = [c['item'] for c in cards]
    fun = sel['fun']['item']; tz = [t['item'] for t in sel['teaser']]; hl = sel['headlines']; hfun = sel.get('headlines_fun', fun); bpr = sel['bp_refs']
    allids = ids + [fun] + tz + hl + [hfun] + bpr
    chk('G1 every id exists and is not held', all(i in ents and i not in hid for i in allids), str([i for i in allids if i not in ents or i in hid]))
    chk('G2 count: 14 story cards, 4 teaser items, 7 Headlines clips', len(cards) == F['target'] and len(tz) == 4 and len(hl) == 7, f'{len(cards)} cards, {len(tz)} teaser, {len(hl)} clips')
    chk('G3 no duplicate ids among cards', len(set(ids)) == len(ids), str([i for i in ids if ids.count(i) > 1]))
    bad = [c['item'] for c in cards if c['item'] not in bset and not c.get('exception')]
    chk('G4 cards come from the Bulletin (an exception must be declared with a reason)', not bad, str(bad))
    for c in cards:
        if c.get('exception'):
            cat = ents[c['item']]['v1_category']
            elig = [i for i in bset if i not in hid and ents[i]['v1_category'] == cat and (ents[i]['freshness'] == 'NEW' or i in UA) and ents[i]['verified_text']]
            chk(f'G4b exception {c["item"]} allowed only when the Bulletin has no eligible story in its category', not elig and c.get('reason'), f'eligible Bulletin stories: {elig}')
    chk('G5 every card, clip and the fun story was read in full', all(ents[i]['verified_text'] for i in ids + hl + [fun, hfun] if i in ents), str([i for i in ids + hl + [fun, hfun] if i in ents and not ents[i]['verified_text']]))
    upd = [i for i in ids + hl + tz if i in ents and ents[i]['freshness'] != 'NEW' and i not in UA]
    chk('G6 no update of an earlier story unless Rafi named it (cards_work/update_allowed.json)', not upd, str(upd))
    cats = [ents[i]['v1_category'] for i in ids]
    chk('G7 deck is in the Drive category order', [ORDER.index(c) for c in cats] == sorted(ORDER.index(c) for c in cats), str(cats))
    over = [k for k in set(cats) if cats.count(k) > (F['market_max'] if k == 'MKT' else F['max_per_category'])]
    chk('G8 category limits (2, markets 3: a money heavy deck is a failure)', not over, str(over))
    comp = {}
    for i in ids:
        for x in brief(ents[i])['companies']: comp[x] = comp.get(x, 0) + 1
    chk('G9 company limit on cards', all(v <= F['company_cards'] for v in comp.values()), str(comp))
    comp2 = {}
    for i in hl:
        for x in brief(ents[i])['companies']: comp2[x] = comp2.get(x, 0) + 1
    chk('G10 company limit on Headlines clips', all(v <= F['company_clips'] for v in comp2.values()), str(comp2))
    chk('G11 Headlines clips are cards, in deck order', all(h in ids for h in hl) and [ids.index(h) for h in hl] == sorted(ids.index(h) for h in hl), str(hl))
    chk('G12 teaser stories are not cards and not clips', not (set(tz) & (set(ids) | set(hl))), str(set(tz) & set(ids)))
    chk('G13 robotics card shows a machine doing something', all(ents[i].get('machine_action') is not False for i in ids if ents[i]['v1_category'] == 'ROB'), '')
    chk('G14 labels are at most 15 characters', all(len(c.get('label', '')) <= 15 and c.get('label') for c in cards), str([c['item'] for c in cards if len(c.get('label', '')) > 15]))
    chk('G15 every pick has a reason and a not-a-repeat reason', all(c.get('reason') and c.get('not_repeat_because') for c in cards), str([c['item'] for c in cards if not (c.get('reason') and c.get('not_repeat_because'))]))
    chk('G15b every card has a novice test (who a novice would not know, the plain introduction)', all(c.get('novice_test') for c in cards), str([c['item'] for c in cards if not c.get('novice_test')]))
    chk('G16 Bigger Picture sources are in the report and not held', all(i in rset and i not in hid for i in bpr), str([i for i in bpr if i not in rset]))
    # G17 7 day repeat: shared names or topic words with a card, clip, teaser or Bigger Picture line of the last 7 days
    disputes = sel.get('disputed_repeats', {})
    hits = []
    for i in ids + [fun] + tz:
        e = ents[i]; a = pn(e['headline'] + ' ' + e['summary'][:300]); ka = keys(e['headline'])
        for d, lines in decks.items():
            for ln in lines:
                sh = a & pn(ln); kb = keys(ln); ov = len(ka & kb) / max(1, len(ka))
                cs = {x for x in COMPANIES if re.search(rf'\b{x}\b', e['headline']) and re.search(rf'\b{x}\b', ln)}
                if len(sh) >= 3 or (len(sh) >= 2 and ov >= 0.25) or (cs and ov >= 0.34):
                    hits.append((i, d, ln[:110], sorted(sh)[:5]))
    unresolved = [h for h in hits if h[0] not in disputes]
    chk('G17 no story of the last 7 days comes back (cards, Fun, teaser)', not unresolved, '; '.join(f'{h[0]} ~ {h[1]}: "{h[2]}" {h[3]}' for h in unresolved[:8]))
    gaps = [d for d, v in decks.items() if not v]
    print('NOTE decks available for the 7 day check:', 7 - len(gaps), 'of 7; no deck text for', gaps or 'none')
    if hits and disputes:
        print('DISPUTED REPEATS (the picker says these are not repeats; Rafi decides):', {k: v for k, v in disputes.items()})
    ok = all(r[1] for r in res)
    h = hashlib.md5((W / 'cards_work' / 'selection_fable.json').read_bytes()).hexdigest()
    (W / 'cards_work' / 'gate_result.json').write_text(json.dumps(dict(ok=ok, md5=h, results=res, decks_missing=gaps), indent=1))
    if ok:
        deck = [dict(card=f's{n + 1}', item=c['item'], category=NAME[ents[c['item']]['v1_category']], label=c['label'], type='NEW', fresh=ents[c['item']]['freshness'], score=ents[c['item']]['score']) for n, c in enumerate(cards)]
        deck.append(dict(card='fun', item=fun, category='The Fun Side', label=sel['fun'].get('label', 'Fun'), type='NEW', fresh=ents[fun]['freshness'], score=ents[fun]['score']))
        out = dict(edition=ed, note='chosen by the Fable picker and passed the gate (pick_gate.py); selection_fable.json holds the reasons', cards_in_deck_order=deck,
                   teaser_items=[dict(id=f't{n + 1}', item=i, category=NAME[ents[i]['v1_category']]) for n, i in enumerate(tz)], headlines_story_clips_in_order=hl, headlines_fun=hfun, bp_refs=bpr)
        (W / 'cards_work' / 'selection.json').write_text(json.dumps(out, indent=1, ensure_ascii=False))
        print('GATE PASS: selection.json written')
    else:
        print('GATE FAIL: fix the FAIL lines above and run the gate again; selection.json not written')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('cmd', choices=['pack', 'gate']); ap.add_argument('--workdir', required=True)
    a = ap.parse_args()
    (pack if a.cmd == 'pack' else gate)(a.workdir)
