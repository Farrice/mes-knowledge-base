---
status: done
---

# Operator Cockpit V2

## Purpose
Chat-first and command-backed operating cockpit for non-trivial Codex Antigravity work.

**Nothing is missing from this folder.** The cockpit shipped as *execution modules*, not
as project artifacts — this directory has only ever held this INDEX.md (verified by
`git log`, 2026-07-29). It is a pointer, deliberately kept so the name stays findable.

| What | Where |
|---|---|
| The cockpit entry point | `execution/operator_cockpit.py` |
| Friction capture | `execution/friction_ledger.py` |
| Routing governance | `execution/routing_governor.py` |
| Co-creative launchpad | `execution/co_creative_launchpad.py` |
| Runtime preflight | `execution/autopilot_runtime_preflight.py` |

Front doors: `.agent/workflows/system-audit.md` · `.agent/workflows/artifact-router.md`

## Use
- Run `python3 execution/operator_cockpit.py --intent "<raw request>" --plain` before meaningful work.
- New system artifacts for this lane live under `06-system/`.
- Cleanup and migration plans are staged under `_system/organization/`; no broad moves happen automatically.

Marked `done` (2026-07-29) so it stops reading as live work — the code it points to is live and maintained.
