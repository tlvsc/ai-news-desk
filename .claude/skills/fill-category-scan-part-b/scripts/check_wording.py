"""Step 3a. Script check of the card wording and the Headlines scripts (the first half of the plain English gate).

    python check_wording.py --workdir W --cards W/cards_work/cards_copy_fable.json
    python check_wording.py --workdir W --headlines W/headlines_work/scripts_final.json

Cards: head at most 85 characters, body exactly two sentences and at most 230 characters (Bigger Picture body at
most 160, teaser line at most 90); every sentence at most 15 words and at most one number; no banned word; never
starts with an outlet's "X reports that". Headlines: the same sentence rules, no digits (numbers are spoken words),
the speaking time from syllables / 4.4 rounded up to the half second; a story aims at 8 s and warns past 9.5 s, the
Bigger Picture warns past 11.5 s, nothing may pass 12 s. Writes the stranger check input next to the file
(stranger_input.json: the words only, no ids or facts) and prints PASS or FAIL per item.
REPLY STORIES (Rafi, 4 Oct 2026): a story that is a reply, reaction or comment to an earlier story (pool follow_up
plus reply words in its report entry) fails unless its card or clip says it is a reply AND names the earlier story
(yesterday, earlier, reported, report, story ...).
"""
import argparse, importlib.util, json, re
from pathlib import Path

BANNED = re.compile(r'\b(materially|signals|exposure|ecosystem|headwinds|execution-dependent|capacity buildout|monetisation|'
                    r'monetization|at scale|tranche|yields?|futures|valuation|lockup|benchmark|inference|tokens?|GPUs?|HBM\d?|'
                    r'leverage)\b', re.I)
spec = importlib.util.spec_from_file_location('fill', Path(__file__).with_name('fill_headlines.py'))
fill = importlib.util.module_from_spec(spec); spec.loader.exec_module(fill)
CUES = {'N-vidia': 'Nvidia', 'an-thropic': 'Anthropic', 'Kawa saki': 'Kawasaki'}
REPLY = re.compile(r"\b(repl(y|ies|ied)|in response to|responded to|reaction to|reacted to|jab|hits? back|hit back|rebut\w*|"
                   r"answer(s|ed)? (to|a|an|the)|criticis\w+|criticiz\w+|swipe|dig at)\b", re.I)
SAYS_REPLY = re.compile(r"\b(repl(y|ies|ied)|answer\w*|response|responded|reaction|react\w*|hit back|hits back|rebut\w*)\b", re.I)
NAMES_EARLIER = re.compile(r"\b(yesterday|earlier|last week|this week|days ago|reported|report|story|article|essay|interview)\b", re.I)


def reply_items(W):
    """Item ids whose report entry is a reply to an earlier story."""
    pools = [f for f in sorted((W / 'out').glob('AIND_Pool_*.json')) if '_old' not in f.name]
    pool = {x['item_id']: x for x in json.loads(pools[-1].read_text())} if pools else {}
    out = set()
    for i, x in pool.items():
        f = W / 'report_entries' / f'{i}.json'
        if not f.exists() or not (x.get('follow_up') or x.get('follow_up_of')):
            continue
        e = json.loads(f.read_text())
        if REPLY.search(' '.join(str(e.get(k, '')) for k in ('headline', 'summary', 'importance_line'))):
            out.add(i)
    return out


def reply_problem(item, text, replies):
    if item not in replies:
        return []
    if SAYS_REPLY.search(text) and NAMES_EARLIER.search(text):
        return []
    return ['reply story: say it is a reply and name the earlier story it answers (who reported what, when)']


def sentences(t):
    t = re.sub(r'^(In [a-z ]+\.|And a lighter story\.|Also in the full report\.|And for the bigger picture:)\s*', '', t.strip())
    return [s for s in re.split(r'(?<=[.!?])\s+', t) if s.strip()]


def problems(text, kind):
    out = []
    for s in sentences(text):
        w = len(re.sub(r'\b(?:[A-Z] )+[A-Z]\b', 'X', s).split())   # a spoken acronym is one word
        if w > 15: out.append(f'{w} words: "{s[:60]}"')
        if len(re.findall(r'\d[\d,.]*', s)) > 1: out.append(f'two numbers: "{s[:60]}"')
    for m in BANNED.findall(text): out.append(f'banned word "{m}"')
    if re.match(r"^[A-Z][\w.' ]+ (reports|says) that", text): out.append('opens with an outlet')
    if kind == 'clip' and re.search(r'\d', text): out.append('digits in a spoken line')
    if kind == 'clip':   # HEADLINES SHAPE from the phrasing file (Rafi, 5 Oct 2026): short, plain, who did what, then why it matters to people
        for s in sentences(text):
            w = len(re.sub(r'\b(?:[A-Z] )+[A-Z]\b', 'X', s).split())   # a spoken acronym (A I, T S M C) is one word
            if w > MAXW: out.append(f'headlines shape: {w} words, keep a spoken sentence to {MAXW}: "{s[:50]}"')
            if re.match(r"^(\w+ing\b[^,]*,|(With|After|Despite|While|Although|Amid)\b)", s): out.append(f'headlines shape: starts with a side clause, start with who did what: "{s[:40]}"')
            if s.count(',') > 1: out.append(f'headlines shape: more than one comma, split or cut: "{s[:40]}"')
        if re.search(r"\b(its|their|the company's|\w+'s) (biggest|largest) (deal|acquisition|purchase)", text, re.I):
            out.append('headlines shape: "biggest deal" matters to the company, say why it matters to people')
    return out


ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--workdir', required=True); ap.add_argument('--cards'); ap.add_argument('--headlines')
a = ap.parse_args()
bad = 0
REPLIES = reply_items(Path(a.workdir))
# ONE TRUTH (Rafi, 5 Oct 2026): the sentence limit comes from the Headlines section of the phrasing file, never from this script
_ph = (Path(a.workdir) / 'rules' / 'Article_phrasing_instructions_AIND_V1.txt').read_text(encoding='utf-8')
_m = re.search(r'PRODUCT:headlines -->(.*?)<!--', _ph, re.S)
_n = re.search(r'at most (\d+) words', _m.group(1)) if _m else None
if not _n: raise SystemExit('STOP: the Headlines section of the phrasing file gives no sentence limit; fetch the current file (Part A step 0)')
MAXW = int(_n.group(1))
if a.cards:
    d = json.loads(Path(a.cards).read_text()); rows, si = [], []
    items = [(s['card'], s['head'], s['body'], 230) for s in d['stories']] + [(t['id'], t['head'], '', 0) for t in d['teaser']]
    items.append(('bp', d['bp']['head'], d['bp']['body'], 160))
    ITEM = {s['card']: s['item'] for s in d['stories']} | {x['id']: x['item'] for x in d['teaser']}
    for cid, h, b, lim in items:
        p = problems(h, 'card') + (problems(b, 'card') if b else [])
        hl = 90 if not b else 85
        if len(h) > hl: p.append(f'head {len(h)} > {hl} characters')
        if b and len(b) > lim: p.append(f'body {len(b)} > {lim} characters')
        if b and len(sentences(b)) != 2: p.append(f'body has {len(sentences(b))} sentences, not 2')
        p += reply_problem(ITEM.get(cid), h + ' ' + b, REPLIES)
        bad += bool(p); print(f"{'FAIL' if p else 'PASS'} {cid:7} {'; '.join(p)}")
        si.append({'n': len(si) + 1, 'card': cid, 'headline': h, 'body': b})
    (Path(a.cards).parent / 'stranger_input.json').write_text(json.dumps(si, indent=1, ensure_ascii=False))
if a.headlines:
    d = json.loads(Path(a.headlines).read_text()); si = []; total = 0
    items = [(s['item'], s['script'], 9.5) for s in d['stories']] + [('fun', d['fun']['script'], 9.5),
             ('teaser', d['teaser']['script'], 9.5), ('bp', d['bp']['script'], 11.5)]
    for k, s, warn in items:
        syl = fill.syllables(s, CUES); box, sp = fill.box_seconds(syl, 4.4, 0, 0); total += box
        p = problems(s, 'clip') + reply_problem(k, s, REPLIES)
        rec = next((x for x in d['stories'] if x['item'] == k), d.get(k) if k in ('fun',) else None)
        if rec is not None:   # WHO, WHAT, WHY FIRST (Rafi, 5 Oct 2026)
            miss = [f for f in ('who', 'what', 'why_for_people') if not str(rec.get(f, '')).strip()]
            if miss: p.append('missing ' + ', '.join(miss) + ' (fill who, what, why first, then write the line)')
            else:
                ww = {x for x in re.findall(r"[a-z]{4,}", rec['why_for_people'].lower())} - {'that','this','with','they','their','will','would','could','more','from','have','about'}
                if ww and len(ww & set(re.findall(r"[a-z]{4,}", s.lower()))) < max(1, len(ww) // 3):
                    p.append('the why is not spoken in the line: ' + rec['why_for_people'][:60])
        if box > 12: p.append(f'{box} s is over the 12 s maximum')
        w = f' (long: aim 8 s)' if box > warn else ''
        bad += bool(p); print(f"{'FAIL' if p else 'PASS'} {k:7} {syl:3} syl {box:4} s{w} {'; '.join(p)}")
        si.append({'n': len(si) + 1, 'line': s})
    print(f'news part (7 stories, fun, teaser, Bigger Picture): {total} s; about 90 s is the target')
    (Path(a.headlines).parent / 'stranger_input.json').write_text(json.dumps(si, indent=1, ensure_ascii=False))
if a.headlines:   # stamp for the gate in common_b.rules_gate
    (Path(a.headlines).parent / 'wording_check.json').write_text(json.dumps({'fails': bad, 'file': str(a.headlines)}))
print('RESULT', 'all pass' if not bad else f'{bad} to fix')
