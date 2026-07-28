# Solution Card — Front door's example row masks a skill's first workflow from the wrapper minter

**Date**: 2026-07-28 · **Domain**: system / arsenal loop · **Session**: hilary-gridley forge

## Problem

After a fresh forge, `mint_menu_wrappers.py --scope skill <name> --apply` minted wrappers for 12 of 13 workflows and reported nothing pending — the FLAGSHIP workflow (`hg-judgment-encode`) silently got no `/command`.

## Root cause

Order of operations. `sync_registries.py` generates the expert front door (`.claude/commands/<expert>.md`) BEFORE minting runs, and the front door's table cites the skill's first workflow path as its example row. `arsenal_index._command_for_path()` scans `.claude/commands/*.md` for workflow-path references, so that example row marks the first workflow `menu_status: reachable` (command = the front door). The minter only processes `unreachable` entries → the first workflow in every freshly-forged skill is skipped, invisibly (report shows `writes: [], skipped: []`).

## Fix applied

Targeted mint using the generator's own functions (still generator-authored, carries GEN_MARKER — never hand-written):

```bash
python3 -c "
import sys; sys.path.insert(0,'execution'); from pathlib import Path
import mint_menu_wrappers as m
skill, stem = '<skill>', '<workflow-stem>'; cmd = stem
path = f'skills/{skill}/workflows/{stem}.md'; desc = '<frontmatter description>'
(m.WF_DIR/f'{cmd}.md').write_text(m.wrapper_body(cmd, skill, path, Path(path), desc))
(m.CMD_DIR/f'{cmd}.md').write_text(m.shim_body(cmd, f'.agent/workflows/{cmd}.md', desc))"
python3 execution/generate_slash_commands.py
```

## Detection

After any forge/mint: `ls .agent/workflows/<prefix>-*.md | wc -l` must equal the skill's workflow count. Mismatch + clean minter report = this bug.

## Permanent fix (proposed, unbuilt)

Either (a) `_command_for_path()` should ignore front-door files (`.claude/commands/<skill-front-door>.md`) when computing reachability — a front door listing a path is a menu, not a command for that path; or (b) mint before generating the front door in the registration sequence. Option (a) is the real fix; flag for a system session.
