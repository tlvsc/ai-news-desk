"""Keep a text copy of the day's working files in the repo, so a wiped cloud machine loses nothing (Rafi, 3 Oct 2026).

    python save_state.py --workdir W                 # copy W's text files into <repo>/runs/<edition>/ and commit + push
    python save_state.py --workdir W --restore       # the other way: rebuild W from <repo>/runs/<edition>/ in a new session

Copied: every text file at the top of W (run.json, held.json, qa logs, viral.json, bigger_picture*.json, rules_check.md, keep lists,
id lists ...; under 2 MB each; chain fix, 13 Oct 2026, lesson 257: the old fixed list missed qa2_log_C, qa_bp_log, editor_checked_ids,
round2_ids and more), the run handoff in the scratchpad (HANDOFF_<edition>_run.md), out/, report_entries/, facts/, products/,
cards_work/, headlines_work/, rules/ and pool/ text files. Before the push it pulls (a merge, never a rebase), because other chats push
to the same branch during a run (lesson 246); a conflict stops it and nothing is pushed. Never copied: PDF, PNG, JPG, MP3, fulltext/
(media stays out of git, CLAUDE.md rule 9; the PDFs and cards are rebuilt from the JSON in minutes). Part A runs it after
the final build and after delivery; Part B after the wording is final and at the approval stop.
"""
import argparse, json, os, shutil, subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
TEXT = ('*.json', '*.csv', '*.md', '*.txt')
PARTS = ['run.json', 'held.json', 'qa1_problems.json', 'qa2_log_A.json', 'qa2_log_B.json', 'drops.json', 'dedupe_overrides.json',
         'url_fixes.json', 'bigger_picture.json', 'bigger_picture_bulletin.json', 'cards_copy.json', 'prompt_extra.json',
         'report_ids.json', 'yesterday_pool.csv', 'rules_check.md', 'bigger_picture_card.json']
DIRS = ['out', 'report_entries', 'facts', 'products', 'cards_work', 'headlines_work', 'rules', 'pool']


def copy_tree(src, dst):
    n = 0
    for pat in TEXT:
        for p in src.glob(pat):
            dst.mkdir(parents=True, exist_ok=True); shutil.copy2(p, dst / p.name); n += 1
    return n


ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--workdir', required=True); ap.add_argument('--restore', action='store_true')
a = ap.parse_args()
W = Path(a.workdir).resolve()
if a.restore:
    ed = W.name.replace('run_', ''); R = REPO / 'runs' / ed
    if not R.exists():
        raise SystemExit(f'no saved state at {R}')
    n = 0
    for p in R.rglob('*'):
        if p.is_file():
            q = W / p.relative_to(R); q.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(p, q); n += 1
    print(f'restored {n} files from {R} into {W}; PDFs, cards and the Headlines JSON are rebuilt by the skills')
    raise SystemExit
ed = json.loads((W / 'run.json').read_text())['edition']; R = REPO / 'runs' / ed
n = 0
tops = {f for f in PARTS if (W / f).exists()} | {p.name for pat in TEXT for p in W.glob(pat) if p.stat().st_size < 2_000_000}
for f in sorted(tops):
    R.mkdir(parents=True, exist_ok=True); shutil.copy2(W / f, R / f); n += 1
hand = W.parent / f'HANDOFF_{ed}_run.md'
if hand.exists():
    R.mkdir(parents=True, exist_ok=True); shutil.copy2(hand, R / hand.name); n += 1
for d in DIRS:
    if (W / d).is_dir():
        n += copy_tree(W / d, R / d)
size = sum(p.stat().st_size for p in R.rglob('*') if p.is_file())
print(f'{n} text files, {size / 1e6:.1f} MB in {R}')
SID = os.environ.get('CLAUDE_CODE_REMOTE_SESSION_ID', '').replace('cse_', 'session_', 1)  # this session's link, never a hard-coded old one (lessons 228, 257)
subprocess.run(['git', 'add', str(R)], cwd=REPO, check=True)
if subprocess.run(['git', 'diff', '--cached', '--quiet'], cwd=REPO).returncode == 0:
    print('nothing new to commit'); raise SystemExit
subprocess.run(['git', 'commit', '-q', '-m', f'Run state {ed}: text copy of the working files (restart point)\n\n'
                'Co-Authored-By: Claude <noreply@anthropic.com>'
                + (f'\nClaude-Session: https://claude.ai/code/{SID}' if SID else '')], cwd=REPO, check=True)
BR = 'claude/eager-archimedes-ajnex3'
pl = subprocess.run(['git', 'pull', '-q', '--no-rebase', '--no-edit', 'origin', BR], cwd=REPO, capture_output=True, text=True)
if pl.returncode != 0:
    subprocess.run(['git', 'merge', '--abort'], cwd=REPO, capture_output=True)
    raise SystemExit('committed here, NOT pushed: pulling origin failed (' + (pl.stderr.strip().splitlines() or ['?'])[-1]
                     + '). Run .claude/hooks/sync_repo.sh and tell Rafi; never force-push.')
r = subprocess.run(['git', 'push', '-q', '-u', 'origin', BR], cwd=REPO)
print('committed and', 'pushed' if r.returncode == 0 else 'PUSH FAILED: retry git push')
