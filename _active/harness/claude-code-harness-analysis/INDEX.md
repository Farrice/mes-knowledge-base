---
status: parked
entry: README.md
---

# Claude Code Harness Analysis

## Purpose
Reference material: decompiled harness source (v2.1.88) + system prompts. Cited by `execution/hooks/session_ledger_hook.py` for Bash tool_response semantics — reference only, never edit to 'fix' anything.

## Map
- `kuberwastaken-analysis/`
- `source-code-v2.1.88/`
- `system-prompts/`

## Filing
New artifacts go in the canonical subfolder at creation time (`directives/artifact-placement.md`), never loose at the project root. Moving anything: `python3 execution/project_filer.py plan --project "<abs dir>"` — never bare `mv`.
