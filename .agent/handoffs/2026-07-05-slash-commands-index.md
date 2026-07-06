---
thread: slash-commands-index
status: done
resume_hint: Work complete — command index fully wired into sync flow; all commits pushed to branch feat/session-auto-naming-pin
unfinished: 
branch: feat/session-auto-naming-pin
pin: true
---

# SLASH_COMMANDS Index — Complete Regeneration (1866 commands, re-runnable generator)

**Status:** ready · **Date:** 2026-07-05

## What this session did
Farrice noticed `SLASH_COMMANDS.md` was missing commands. Confirmed: the file
claimed 697 but listed 787, while **1,865 commands exist on disk** (union of
`.agent/workflows/` + `.claude/commands/`). **1,079 were missing.**

Built a **re-runnable, non-destructive generator** instead of hand-editing:
- `execution/generate_slash_commands.py` (NEW, untracked)
- Regenerated `SLASH_COMMANDS.md` (MODIFIED): 697 → **1866 commands**, 2788 lines.

### How the generator works (design decisions)
- **Preserves the hand-curated file byte-for-byte** — verified `diff` of lines
  2–1528 vs backup is identical. All curated descriptions, Natural-Language-
  Triggers table, How-I-Write OS, Fork Harvest sections untouched.
- Appends ONE fenced region (`<!-- AUTO-INDEX:BEGIN/END -->`): "📚 Complete
  Command Index — Everything Else (1079)", same `| Command | What It Does |`
  table format, grouped by expert-family + an A–Z long-tail table.
- **Idempotent** (sentinel-fenced; re-runs rebuild, never duplicate). Auto-
  maintains the line-1 count and floats the "Quick tip" footer to the end.
- Description extraction handles: fenced/unfenced YAML, `>-`/`|` block scalars,
  skill-command shims (→ target SKILL.md), workflow pointers, self-named
  headings, generic section labels, list/metadata-line skipping, pipe-escaping.
- Coverage: only 1 of 1079 (`/references`, a near-empty file) uses a placeholder.

Run: `python3 execution/generate_slash_commands.py` (or `--check` for report-only).

## Work completed (2026-07-05 continuation)
1. ✅ **Committed all files** (commits a40aa711 + 031157bb):
   - `execution/generate_slash_commands.py` (generator)
   - `SLASH_COMMANDS.md` (1,866 commands, fully indexed)
2. ✅ **Wired generator into `sync_registries.py`**:
   - Now auto-regenerates `SLASH_COMMANDS.md` every time `sync_registries.py` runs
   - Idempotent and non-destructive; command index stays current as workflows change
   - Tested: ran sync_registries successfully with no unwanted diffs

## Known open question (raised, not yet decided)
The curated sections above still show their ORIGINAL per-expert counts (e.g.
"Luke Iha (35)") — I kept the change additive. A future bigger pass could fully
re-categorize everything into one structure, but that rewrites hand-curation.
Farrice has NOT asked for that; default is to leave additive.

## Result
Complete command index is now **self-maintaining**. Every invocation of 
`sync_registries.py` (which runs during routine system maintenance) automatically 
regenerates `SLASH_COMMANDS.md` to reflect new workflows/commands. The 1,865-command 
corpus is fully indexed and current; index corruption (like the original 42% gap) 
cannot recur.

## Key files
- `execution/generate_slash_commands.py` — the generator (read its module docstring).
- `SLASH_COMMANDS.md` — the regenerated index.
- Backup of pre-change version: `/tmp/SLASH_COMMANDS.bak.md` (ephemeral).
