"""Step 0c. Compare today's governing rule files with the last run's copies and print what changed.

    python rules_diff.py --new W/rules --old <last run>/rules

The Drive rule files change between runs without notice (3 Oct 2026: four files changed overnight). Read every
changed line before the stage it governs; a change that clashes with CLAUDE.md goes to Rafi (rule 0).
"""
import argparse, difflib
from pathlib import Path

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('--new', required=True); ap.add_argument('--old', required=True)
a = ap.parse_args()
for p in sorted(Path(a.new).glob('*.txt')):
    q = Path(a.old) / p.name
    if not q.exists():
        print(f'NEW FILE  {p.name} ({p.stat().st_size} bytes)'); continue
    x, y = q.read_text(encoding='utf-8').splitlines(), p.read_text(encoding='utf-8').splitlines()
    d = [l for l in difflib.unified_diff(x, y, lineterm='', n=0) if l[:1] in '+-' and not l.startswith(('+++', '---'))]
    if not d:
        print(f'same      {p.name}'); continue
    print(f'CHANGED   {p.name}: {sum(l[0] == "-" for l in d)} lines out, {sum(l[0] == "+" for l in d)} lines in')
    for l in d[:40]:
        print('   ', l[:220])
