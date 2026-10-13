#!/bin/bash
# Repo sync and tools for the AI News Desk cloud chats (chain fix, Rafi's yes of 13 Oct 2026; docs/V1_TASKS.md lesson 246).
# Every cloud chat since about 6 Oct started on an old, shallow copy of the branch (6 Oct, commit c72b14e). It looked like
# "50 local commits against 56 on origin" and cost the 13 Oct run 30 minutes, old rules for the first writers and a nag after
# every turn. This script brings the copy up to date and installs the PDF and image tools.
# It only moves FORWARD (fast-forward). It never resets, rebases, deletes or pushes. It always exits 0.
#   bash .claude/hooks/sync_repo.sh        (also run by the SessionStart hook in .claude/settings.json, at a new chat's start only:
#                                          never on a resume or after a compaction, so scripts never change in the middle of a run)
[ "${CLAUDE_CODE_REMOTE:-}" = "true" ] || [ "${1:-}" = "--force" ] || { echo "sync_repo: not a cloud chat, nothing done"; exit 0; }
BRANCH=claude/eager-archimedes-ajnex3
REPO="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "$0")/../.." && pwd)}"
cd "$REPO" 2>/dev/null || { echo "sync_repo: no repo at $REPO"; exit 0; }
say() { echo "sync_repo: $*"; }
cur=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)
if [ "$cur" != "$BRANCH" ]; then
  say "on branch '$cur', not $BRANCH: nothing done"
else
  if [ "$(git rev-parse --is-shallow-repository 2>/dev/null)" = "true" ]; then
    git fetch -q --unshallow origin "$BRANCH" 2>/dev/null || git fetch -q --depth=100000 origin "$BRANCH" 2>/dev/null
  else
    git fetch -q origin "$BRANCH" 2>/dev/null
  fi
  git update-ref "refs/remotes/origin/$BRANCH" FETCH_HEAD 2>/dev/null
  behind=$(git rev-list --count "HEAD..origin/$BRANCH" 2>/dev/null || echo "?")
  ahead=$(git rev-list --count "origin/$BRANCH..HEAD" 2>/dev/null || echo "?")
  if [ "$behind" = "0" ] && [ "$ahead" = "0" ]; then
    say "up to date with origin ($(git log -1 --format='%h %cd' --date=format:'%d %b %H:%M'))"
  elif [ "$ahead" = "0" ]; then
    if git merge -q --ff-only "origin/$BRANCH" 2>/dev/null; then
      say "moved forward $behind commits to $(git log -1 --format='%h %cd' --date=format:'%d %b %H:%M'); read CLAUDE.md and the skills again"
    else
      say "STOP: $behind new commits on origin but the fast-forward failed (local file changes?). Tell Rafi; change nothing."
    fi
  else
    say "STOP: this copy has $ahead commits that origin does not have and origin has $behind new ones. Tell Rafi; never reset or force-push."
  fi
fi
# Tools: the pool PDF needs PyMuPDF (lesson 169); the card renderer needs Pillow 12.3.0 and fontTools 4.61.1 (Part B step 0).
need=()
python3 -c "import pymupdf" 2>/dev/null || need+=(pymupdf)
python3 -c "import PIL, sys; sys.exit(PIL.__version__ != '12.3.0')" 2>/dev/null || need+=("Pillow==12.3.0")
python3 -c "import fontTools, sys; sys.exit(fontTools.version != '4.61.1')" 2>/dev/null || need+=("fonttools==4.61.1")
if [ ${#need[@]} -gt 0 ]; then   # in the background: about a minute, and nothing needs these tools before the pool PDF
  nohup bash -c "pip install -q --break-system-packages ${need[*]} || pip install -q ${need[*]}" >/tmp/sync_repo_pip.log 2>&1 &
  say "installing in the background: ${need[*]} (log /tmp/sync_repo_pip.log)"
fi
exit 0
