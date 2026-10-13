# Backup before the chain fix (Rafi, 13 Oct 2026: "create a backup to this point")

The daily scan exactly as it was before the chain fix: both skills (Part A and Part B, with every brief, script and asset)
and CLAUDE.md, taken from commit b7931cd6ce922ac9596564780649823decb08839 (13 Oct 2026, 09:22 UTC).

- skills/ is a copy of .claude/skills/ (the folder is renamed so Claude Code does not load it as a second set of skills).
- CLAUDE_md_backup.md is a copy of CLAUDE.md (renamed so Claude Code does not load it as a second rulebook).
- This is a backup, not a rulebook: the rules stay in CLAUDE.md and the lessons in docs/V1_TASKS.md.

To go back: copy skills/ over .claude/skills/ and CLAUDE_md_backup.md over CLAUDE.md, or restore both from the commit above.
Run copies (runs/) and lessons (docs/V1_TASKS.md) added after this point are kept.
