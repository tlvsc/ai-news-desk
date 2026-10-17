"""Step 2a. Write the four agent prompts of part B from the briefs (wording and stranger check, cards and Headlines).

    python make_wording_prompts.py --workdir W [--prev-cards OLD_W/cards_copy.json] [--prev-pack OLD_PACK.json]

Writes W/cards_work/{wording_common.txt, prompt_cards.txt, prompt_stranger_cards.txt} and
W/headlines_work/{wording_common.txt, prompt_headlines.txt, prompt_stranger_headlines.txt, prompt_rules_headlines.txt}. Launch each agent with
"Read <that prompt file> and follow it exactly." The writers run on Opus at normal effort (CLAUDE.md rule 27, Rafi 12 Oct 2026, replaces \"at max\" of rule 25), the checkers on Fable at high (rule 25). Also writes W/cards_work/story_pack.md and W/headlines_work/story_pack.md.
"""
import argparse, glob, re
from pathlib import Path
from common_b import B, edition_dates, prev_scripts
import json

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--workdir', required=True); ap.add_argument('--prev-cards'); ap.add_argument('--prev-pack')
a = ap.parse_args()
W = Path(a.workdir).resolve()
prev_runs = [p for p in sorted(glob.glob(str(W.parent / 'run_*'))) if Path(p) != W]
prev_cards = a.prev_cards or next((str(Path(p) / 'cards_copy.json') for p in reversed(prev_runs) if (Path(p) / 'cards_copy.json').exists()), 'none')
prev_pack = a.prev_pack or next((q for p in reversed(prev_runs) for q in sorted(glob.glob(str(Path(p) / 'headlines_work' / '*_pack.json')))),
                                str(B / 'assets' / 'pack_base.json'))
ps = prev_scripts(W)
def _intro(s):
    m = re.match(r'\s*([^.:!?]+)[.:]', s or ''); return m.group(1).strip() if m else ''
if ps:
    _p = json.loads(Path(ps).read_text())
    leadins = sorted({_intro(x['script']) for x in _p.get('stories', [])} | {_intro(_p.get('fun', {}).get('script', ''))})
else:
    leadins = []
v = {'WORKDIR': W, 'EDITION': edition_dates(W)[0], 'PREV_CARDS': prev_cards, 'PREV_PACK': prev_pack,
     'PREV_SCRIPTS': ps or 'none found', 'PREV_LEADINS': ', '.join(f'"{x}"' for x in leadins) or 'none found'}
fill = lambda name: re.sub(r'\{([A-Z_]+)\}', lambda m: str(v.get(m.group(1), m.group(0))), (B / 'briefs' / name).read_text(encoding='utf-8'))
for sub, files in (('cards_work', (('wording_common.txt', 'wording_common.md'), ('prompt_cards.txt', 'wording_cards.md'),
                                   ('prompt_stranger_cards.txt', 'stranger_cards.md'), ('prompt_check_cards.txt', 'check_cards.md'))),
                   ('headlines_work', (('wording_common.txt', 'wording_common.md'), ('prompt_headlines.txt', 'wording_headlines.md'),
                                       ('prompt_stranger_headlines.txt', 'stranger_headlines.md'),
                                       ('prompt_rules_headlines.txt', 'rules_check_headlines.md'),
                                       ('prompt_rewrite_headlines.txt', 'rewrite_headlines.md'), ('prompt_check_headlines.txt', 'check_headlines.md')))):
    (W / sub).mkdir(exist_ok=True)
    for out, brief in files:
        (W / sub / out).write_text(fill(brief), encoding='utf-8')
# STORY PACK (Rafi, 12 Oct 2026: "make it read [the rules once] so we dont go back and make mistakes"; "2 minutes is better than 22"): one file per
# product that holds the whole phrasing file and the entry and facts of every item, so the writer reads once and writes in one pass.
def _story_pack(sub, ids, extras):
    out = ['# STORY PACK: read this file ONCE, at the start. It holds the phrasing rules and every story you write (entry and facts).',
           '# Do not open the entries or facts files and do not re-read the rules before each item (Rafi, 12 Oct 2026, CLAUDE.md rule 27).', '',
           '## 1. THE PHRASING RULES (Article_phrasing_instructions_AIND_V1, the whole file)', '',
           (W / 'rules' / 'Article_phrasing_instructions_AIND_V1.txt').read_text(encoding='utf-8')]
    for title, path in extras:
        if Path(path).exists():
            out += ['', f'## {title}', '', Path(path).read_text(encoding='utf-8')]
    out += ['', '## STORIES: entry (what we publish) and facts (what the article says) of every item', '']
    for i in ids:
        e, f = W / 'report_entries' / f'{i}.json', W / 'facts' / f'{i}.json'
        if not e.exists():
            out += [f'### {i}: MISSING entry', '']; continue
        ent = json.loads(e.read_text(encoding='utf-8'))
        keep = {k: ent.get(k) for k in ('item_id', 'headline', 'summary', 'importance_line', 'status', 'source', 'freshness', 'verified_text', 'score', 'machine_action', 'notes')}
        out += [f'### {i}', 'ENTRY: ' + json.dumps(keep, ensure_ascii=False)]
        if f.exists():
            fa = json.loads(f.read_text(encoding='utf-8'))
            out.append('FACTS: ' + json.dumps({k: fa.get(k) for k in ('key_facts', 'quote_evidence', 'notes', 'status')}, ensure_ascii=False))
        out.append('')
    bpf = W / 'bigger_picture.json'   # 17 Oct 2026, Rafi's yes: the card and clip points live in the one page Full Report file (CLAUDE.md rule 38)
    if bpf.exists():
        pick = [k for k in (json.loads(bpf.read_text(encoding='utf-8')).get('key_points') or []) if k.get('use') in ('headline', 'card')]
        if pick:
            out += ['## THE BIGGER PICTURE KEY POINTS FOR THE CLIP AND THE CARD (point marked headline = the Headlines clip, point marked card = the card; plain words only, say a percent not a fraction, no "restructuring", and it is not financial advice)', '',
                    json.dumps(pick, ensure_ascii=False, indent=1)]
    bpb = W / 'bigger_picture_bulletin.json'
    if bpb.exists():
        out += ['## THE BIGGER PICTURE BULLETIN TEXT (the longer cousin; the clip and card take their point from the key points above when there are key points, otherwise this text is the only source)', '', bpb.read_text(encoding='utf-8')]
    (W / sub / 'story_pack.md').write_text('\n'.join(out), encoding='utf-8')
    return len('\n'.join(out))
selp = W / 'cards_work' / 'selection.json'
if selp.exists():
    sel = json.loads(selp.read_text(encoding='utf-8'))
    tz = [t['item'] for t in sel.get('teaser_items', [])]
    c_ids = [c['item'] for c in sel['cards_in_deck_order']] + tz + sel.get('bp_refs', [])
    h_ids = sel.get('headlines_story_clips_in_order', []) + [sel.get('headlines_fun')] + tz + sel.get('bp_refs', [])
    n1 = _story_pack('cards_work', list(dict.fromkeys(c_ids)), [])
    n2 = _story_pack('headlines_work', list(dict.fromkeys(i for i in h_ids if i)),
                     [('2. THE HEADLINES MODEL LINES', B / 'assets' / 'headlines_model_lines.md'), ('3. THE HEADLINES MASTER RULES', W / 'rules' / 'Headlines_Master_Rules_Structure.txt')])
    print('story packs written:', n1, 'and', n2, 'characters')
else:
    print('NO story pack: cards_work/selection.json is missing (run the pick gate first)')
left = sorted({m for f in list((W / 'cards_work').glob('*.txt')) + list((W / 'headlines_work').glob('*.txt'))
               for m in re.findall(r'\{[A-Z_]+\}', f.read_text())})
print('prompts written to', W / 'cards_work', 'and', W / 'headlines_work', '| previous cards', prev_cards, '| previous pack', prev_pack,
      '| unfilled placeholders:', left or 'none')
