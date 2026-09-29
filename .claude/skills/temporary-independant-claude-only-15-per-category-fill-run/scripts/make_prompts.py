"""Write every agent prompt for the run from the briefs, filled with today's date, window and paths.

    python make_prompts.py --workdir W --stage curate|write|edit [--per-cat 15] [--fun 10]

Writes W/prompts/<stage>_NN.txt (edit: edit_A.txt, edit_B.txt). Launch each agent with the
one-line prompt: "Read <that file> and follow it exactly." so the long text never enters
the main conversation. Optional W/prompt_extra.json {"write": {"12": "extra instruction"}}
adds a line for one category (for example a story that must be traced to its original outlet).
"""
import argparse, json, re
from pathlib import Path

from common import FUN, SKILL, categories, load_run, parse_utc, short_names

OTHER_CATS = ("models=1, products/apps/agents=2, dev tools/open source=3, research/science=4, quotes=5, "
              "companies/funding=6, markets/stocks=7, chips=8, data centers/energy=9, health=10, robots=11, "
              "security/safety=12, policy/law=13, society=14, quantum=15, humor=16")


def fill(template, values):
    return re.sub(r'\{([A-Z_]+)\}', lambda m: str(values.get(m.group(1), m.group(0))), template)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--workdir', required=True)
    ap.add_argument('--stage', required=True, choices=['curate', 'write', 'edit'])
    ap.add_argument('--per-cat', type=int, default=15)
    ap.add_argument('--fun', type=int, default=10)
    a = ap.parse_args()
    W = Path(a.workdir).resolve(); run = load_run(W); (W / 'prompts').mkdir(exist_ok=True)
    start = parse_utc(run['start'])
    base = {'WORKDIR': W, 'EDITION': run['edition'], 'START': run['start'], 'END': run['end'],
            'SCRIPTS': SKILL / 'scripts', 'STALE_BEFORE': f"{start.day} {start:%b %Y}"}
    extra = json.loads((W / 'prompt_extra.json').read_text()) if (W / 'prompt_extra.json').exists() else {}
    cats, names = categories(), short_names()
    written = []
    if a.stage == 'edit':
        t = (SKILL / 'briefs' / 'editor.md').read_text(encoding='utf-8')
        for part in ('A', 'B'):
            p = W / 'prompts' / f'edit_{part}.txt'
            p.write_text(fill(t, dict(base, PART=part)), encoding='utf-8'); written.append(p.name)
    else:
        t = (SKILL / 'briefs' / ('curator.md' if a.stage == 'curate' else 'writer.md')).read_text(encoding='utf-8')
        for cid, (desc, crit) in cats.items():
            n_main = a.fun if cid == FUN else a.per_cat
            v = dict(base, CAT_ID=cid, NN=f'{cid:02d}', CAT_DESC=desc, CAT_NAME=names[cid],
                     N_MAIN=n_main, N_BACKUP_FROM=n_main + 1, N_TOTAL=n_main + 3,
                     EXTRA=extra.get(a.stage, {}).get(str(cid), ''))
            if cid == FUN:
                v.update(CRITERION_B='be genuinely funny or entertaining and about AI',
                         REJECT_EXTRA=', and cruel or offensive items',
                         QUERY_HINT=(' (try queries such as AI fail, chatbot funny, AI blunder, AI hallucination viral, '
                                     'robot fail, AI prank, AI song viral; reddit.com may also be checked with curl for '
                                     'viral AI moments, but every pick must have a news article or a stable link)'),
                         RANK_BY='Rank by how funny and notable.')
            else:
                v.update(CRITERION_B='have this category as its MAIN subject' + (f' ({crit})' if crit else ''),
                         REJECT_EXTRA=f', and items that are mainly another category ({OTHER_CATS})',
                         QUERY_HINT='', RANK_BY='Rank by importance.')
            p = W / 'prompts' / f'{a.stage}_{cid:02d}.txt'
            p.write_text(fill(t, v), encoding='utf-8'); written.append(p.name)
    left = sorted({m for f in written for m in re.findall(r'\{[A-Z_]+\}', (W / 'prompts' / f).read_text())})
    print(len(written), 'prompts in', W / 'prompts', '| unfilled placeholders:', left or 'none')


if __name__ == '__main__':
    main()
