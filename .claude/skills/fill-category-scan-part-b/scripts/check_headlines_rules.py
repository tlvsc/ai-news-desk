"""Step 3b. Headlines rules recheck (Rafi, 4 Oct 2026): every spoken line against the Drive Headlines rules.

    python check_headlines_rules.py --workdir W [--scripts W/headlines_work/scripts_final.json]

The script check of step 3 only tests the phrasing law (15 words, banned words, 12 s). This one tests the rules of
Headlines_Master_Rules_Structure.txt (W/rules) that a script can test, then the rules agent (step 3c) tests the rest.
  A3   story clips in deck order                      A5   teaser only from the teaser card, never a story card
  A2   ending is the approved text; opening slot      B1   aim 8 s, never over 12 s (CLAUDE.md 16: stories 8 to 9 s,
       active only when Rafi asked (CLAUDE.md 16)          Fun and teaser about 8, Bigger Picture about 10)
  B2a  every story and the fun clip open with a short spoken introduction; teaser "Also in the full report",
       Bigger Picture "And for the bigger picture"
  G2   introductions rotate: never the wording of the previous day     B3  numbers as words, no digits
  G1.4 the outlet is never spoken                       15 Sep 1 and 2: pronunciation cues, Google DeepMind
  CLAUDE.md 16: one company at most 2 Headlines stories
  G1.2 a company worth under 100 billion dollars gets a two to three word tag: listed for the rules agent.
Prints PASS, WARN or FAIL per check and writes W/headlines_work/rules_check.json. Nothing passes step 7 with a FAIL.
"""
import argparse, glob, importlib.util, json, re
from pathlib import Path
from common_b import entry, prev_scripts

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--workdir', required=True); ap.add_argument('--scripts')
a = ap.parse_args()
W = Path(a.workdir)
S = json.loads(Path(a.scripts or W / 'headlines_work' / 'scripts_final.json').read_text())
sel = json.loads((W / 'cards_work' / 'selection.json').read_text())
spec = importlib.util.spec_from_file_location('fill', Path(__file__).with_name('fill_headlines.py'))
fill = importlib.util.module_from_spec(spec); spec.loader.exec_module(fill)
ENDING = "Those were today's headlines in ninety seconds. For more detailed coverage, read our daily news cards. Thank you for tuning in, and we'll see you tomorrow."
BIG = ['OpenAI', 'Anthropic', 'Google', 'Alphabet', 'Meta', 'Microsoft', 'Apple', 'Amazon', 'Nvidia', 'Tesla', 'xAI', 'Samsung',
       'Oracle', 'Broadcom', 'Intel', 'AMD', 'TSMC', 'T S M C', 'Alibaba', 'Tencent', 'Palantir', 'SK hynix', 'IBM', 'Netflix', 'SpaceX']
OUTLETS = ['Reuters', 'Bloomberg', 'Axios', 'CNBC', 'Wall Street Journal', 'New York Times', 'Financial Times', 'TechCrunch',
           'The Verge', 'Guardian', 'Nikkei', 'Associated Press', 'Business Insider', 'WIRED', 'The Information']
res, bad = [], 0


def out(rule, ok, msg, level='FAIL'):
    global bad
    st = 'PASS' if ok else level
    bad += st == 'FAIL'; res.append({'rule': rule, 'status': st, 'detail': msg}); print(f'{st:4} {rule:6} {msg}')


def intro(s):
    m = re.match(r'\s*([^.:!?]+)[.:]', s); return (m.group(1).strip() if m else '').lower()


clips = [(x['item'], x['script'], 'story') for x in S['stories']] + [('fun', S['fun']['script'], 'fun'),
         ('teaser', S['teaser']['script'], 'teaser'), ('bp', S['bp']['script'], 'bp')]
deck = [c['item'] for c in sel['cards_in_deck_order']]
order = [deck.index(i) if i in deck else -1 for i in sel['headlines_story_clips_in_order']]
out('A3', -1 not in order and order == sorted(order), f'story clips in deck order: {order}')
tz = {t['item'] for t in sel['teaser_items']}; story_items = {c['item'] for c in sel['cards_in_deck_order']}
ti = set(S['teaser'].get('items', []))
out('A5', ti <= tz and not (ti & story_items), f'teaser items {sorted(ti)} from the teaser card {sorted(tz)}')
pk = sorted(glob.glob(str(W / 'headlines_work' / '*_pack.json')))
pk = [p for p in pk if '_old' not in p]
if pk:
    slots = {s.get('slot'): s for s in json.loads(Path(pk[-1]).read_text()).get('slots', [])}
    end = (slots.get(13) or {}).get('script', '')
    out('A2', not end or end.strip() == ENDING, 'ending is the approved text' if end.strip() == ENDING else f'ending differs: {end[:80]}')
    op = slots.get(1) or {}
    out('A2', op.get('mode') == 'bypass', 'opening slot 1 is active: a new opening is generated; the stored intro is the rule '
        'unless Rafi asked for opening options (CLAUDE.md 16)', 'WARN')
    if re.search(r'\d', op.get('script', '')): out('B3', False, 'digits in the opening line: ' + op.get('script', '')[:60], 'WARN')
for k, s, kind in clips:
    syl = fill.syllables(s, {'N-vidia': 'Nvidia', 'an-thropic': 'Anthropic'}); box, _ = fill.box_seconds(syl, 4.4, 0, 0)
    aim = {'story': 9.0, 'fun': 8.5, 'teaser': 8.5, 'bp': 10.5}[kind]
    out('B1', box <= 12, f'{k} {box} s is over the 12 s maximum') if box > 12 else out('B1', box <= aim, f'{k} {box} s (aim {aim} s or less)', 'WARN')
    if kind in ('story', 'fun'):
        it = intro(s); out('B2a', 0 < len(it.split()) <= 5, f'{k} opens with a spoken introduction: "{it}"')
    if kind == 'teaser': out('B2a', s.startswith('Also in the full report'), 'teaser opens with "Also in the full report"')
    if kind == 'bp': out('B2a', s.startswith('And for the bigger picture'), 'Bigger Picture opens with "And for the bigger picture"')
    out('B3', not re.search(r'\d', s), f'{k} has no digits')
    if re.search(r'\bAnthropic\b', s): out('15Sep1', False, f'{k}: write Anthropic as "an-thropic" in speech')
    if re.search(r'\bNvidia\b|\bNVIDIA\b', s): out('15Sep1', False, f'{k}: write Nvidia as "N-vidia" in speech')
    if re.search(r'(?<!Google )DeepMind', s): out('15Sep2', False, f'{k}: say "Google DeepMind"')
    src = entry(W, k).get('source', '') if kind == 'story' else ''
    spoken_outlets = [o for o in OUTLETS + ([src] if src and src != 'AI News Desk' else []) if o and o.lower() in s.lower()]
    if spoken_outlets: out('G1.4', False, f'{k} speaks an outlet: {spoken_outlets}')
prev = prev_scripts(W)
if prev:
    p = json.loads(Path(prev).read_text())
    old = {intro(x['script']) for x in p.get('stories', [])} | {intro(p.get('fun', {}).get('script', ''))}
    rep = [(k, intro(s)) for k, s, kind in clips if kind in ('story', 'fun') and intro(s) in old]
    out('G2', not rep, f'introductions used the previous day ({Path(prev).parent.parent.name}): {rep}' if rep else
        f'no introduction repeats the previous day ({Path(prev).parent.parent.name})')
else:
    out('G2', False, 'no previous day scripts found to check rotation against', 'WARN')
cnt = {}
for k, s, kind in clips[:7]:
    for c in BIG:
        if re.search(r'\b' + re.escape(c) + r'\b', s.replace('an-thropic', 'Anthropic')): cnt[c] = cnt.get(c, 0) + 1
over = {c: n for c, n in cnt.items() if n > 2}
out('C16', not over, f'one company at most 2 story clips: {cnt}')
names = sorted({m for k, s, kind in clips for m in re.findall(r"\b[A-Z][a-zA-Z]+(?: [A-Z][a-zA-Z]+)*", s)
                if m not in BIG and m.split()[0] not in ('In', 'And', 'Also', 'The', 'A', 'I', 'U', 'S', 'T', 'V', 'Watch', 'He', 'She',
                                                        'It', 'They', 'Share', 'Rising', 'Regulators', 'OpenAI')})
out('G1.2', True, f'names for the rules agent to tag if under 100 billion dollars: {names}', 'INFO')
(W / 'headlines_work' / 'rules_check.json').write_text(json.dumps({'fails': bad, 'checks': res, 'names_to_tag': names}, indent=1))
print('RESULT', 'all rules pass' if not bad else f'{bad} rule fails: fix before step 7')
