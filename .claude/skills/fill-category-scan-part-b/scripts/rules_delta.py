"""Step 0c. What changed since the last rules check (chain fix, Rafi's yes of 13 Oct 2026; lessons 262 and 272b).

    python3 rules_delta.py --workdir W

Part B step 0c used to read the whole lessons file (165 KB), CLAUDE.md and six Drive rule files every day and rebuild rules_check.md
from nothing (12 Oct: 23 minutes, 13 Oct: 38 minutes). The check is now incremental: this script finds the newest saved check
(runs/<day>/rules_check.md, a day before this edition), the commit that saved it, and writes
    W/rules_check_previous.md   a copy of that check
    W/rules_delta.md            everything that changed since: CLAUDE.md, docs/V1_TASKS.md (added lines), both skills and their
                                briefs, and the Drive rule files in W/rules against that day's copy in runs/<day>/rules
It also fills briefs/rules_check_update.md into W/rules_check_prompt.txt: the rules checker reads only these two files and writes W/rules_check.md.
With no earlier check, or no git history for it, it prints FULL CHECK NEEDED (the old way, once).
"""
import argparse, difflib, json, shutil, subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--workdir', required=True)
a = ap.parse_args()
W = Path(a.workdir).resolve()
ed = json.loads((W / 'run.json').read_text())['edition']


def git(*args):
    r = subprocess.run(['git', *args], cwd=REPO, capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


days = sorted(p.parent.name for p in (REPO / 'runs').glob('*/rules_check.md') if p.parent.name < ed)
if not days:
    raise SystemExit('FULL CHECK NEEDED: no earlier runs/<day>/rules_check.md in the repo')
base_day = days[-1]
base = (git('log', '-1', '--format=%H', '--', f'runs/{base_day}/rules_check.md') or '').strip()
if not base:
    raise SystemExit(f'FULL CHECK NEEDED: no git history for runs/{base_day}/rules_check.md (shallow copy? run .claude/hooks/sync_repo.sh)')
shutil.copy2(REPO / 'runs' / base_day / 'rules_check.md', W / 'rules_check_previous.md')

out = [f'# Rules delta for edition {ed}: everything that changed since the rules check of {base_day}',
       f'Base: commit {base[:7]} (the save of runs/{base_day}/rules_check.md); now: {(git("rev-parse", "--short", "HEAD") or "?").strip()}.',
       'Read with W/rules_check_previous.md. Lines starting with + are new, - are gone.', '']
counts = {}

claude = git('diff', '-U1', base, 'HEAD', '--', 'CLAUDE.md') or ''
counts['CLAUDE.md'] = sum(1 for x in claude.splitlines() if x[:1] in '+-' and x[:3] not in ('+++', '---'))
out += ['## 1. CLAUDE.md', '', claude.strip() or 'no change', '']

lessons = [x for x in (git('diff', '-U0', base, 'HEAD', '--', 'docs/V1_TASKS.md') or '').splitlines()
           if x.startswith('+') and not x.startswith('+++') and x[1:].strip()]
counts['lessons'] = len(lessons)
out += ['## 2. docs/V1_TASKS.md: added or changed lines (new lessons and ADDED notes)', ''] + (lessons or ['no change']) + ['']

skills = git('diff', '-U1', base, 'HEAD', '--', '.claude/skills/*/SKILL.md', '.claude/skills/*/briefs', '.claude/skills/*/assets/*.md') or ''
stat = git('diff', '--stat', base, 'HEAD', '--', '.claude/skills') or ''
counts['skills and briefs'] = sum(1 for x in skills.splitlines() if x[:1] in '+-' and x[:3] not in ('+++', '---'))
out += ['## 3. Skills and briefs (scripts listed by name only)', '', stat.strip() or 'no change', '', skills.strip() or '', '']

drive = []
old_rules = REPO / 'runs' / base_day / 'rules'
for f in sorted((W / 'rules').glob('*.txt')):
    o = old_rules / f.name
    if not o.exists():
        drive += [f'### {f.name}: NEW (no copy on {base_day}); read it in full', '']
        continue
    d = list(difflib.unified_diff(o.read_text(encoding='utf-8', errors='replace').splitlines(),
                                  f.read_text(encoding='utf-8', errors='replace').splitlines(), lineterm='', n=1))
    if d:
        drive += [f'### {f.name}', ''] + d[2:] + ['']
counts['Drive rule files'] = sum(1 for x in drive if x[:1] in '+-')
out += ['## 4. Drive rule files (W/rules against runs/%s/rules)' % base_day, ''] + (drive or ['no change', ''])

(W / 'rules_delta.md').write_text('\n'.join(out), encoding='utf-8')
brief = (Path(__file__).resolve().parent.parent / 'briefs' / 'rules_check_update.md').read_text(encoding='utf-8')
(W / 'rules_check_prompt.txt').write_text(brief.replace('{WORKDIR}', str(W)).replace('{EDITION}', ed).replace('{BASE_DAY}', base_day),
                                          encoding='utf-8')
print(f'rules delta since {base_day} (commit {base[:7]}):', ', '.join(f'{k} {v} lines' for k, v in counts.items()))
print('written:', W / 'rules_delta.md', W / 'rules_check_previous.md', 'and the checker prompt', W / 'rules_check_prompt.txt')
