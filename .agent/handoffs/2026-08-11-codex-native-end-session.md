---
thread: codex-native-end-session
status: done
resume_hint: Begin the first substantive Codex-primary production task. Let real task receipts reveal whether any further harness change is warranted.
branch: codex/antigravity-operator-core
pin: false
---

# System: Codex-Native End Session - Hardened and Verified

## Purpose

- **Next session should do:** Use `/end-session` normally after the next substantive Codex task; the operator lane will be preserved and only task-owned paths will be committed locally.
- **Not in scope:** Push, merge into dirty `main`, global receipt writes, broad lane cleanup, or changes to Claude Code and Cowork behavior.

## Completed

- Kept the existing `/end-session` command, canonical workflow, and thin global bridge instead of creating a duplicate cleanup system.
- Added explicit lane disposition, Git synchronization, and global receipt policies to the Codex-native coordinator.
- Made `codex/antigravity-operator-core` a mechanically recognized persistent lane that survives task closeout.
- Made local commit the default and global receipt writes opt-in; no push or global mutation occurred in this run.
- Made temporary lanes return an exact approval-required merge-or-park action and keep incomplete closeouts pinned.
- Prevented the shared closeout spine from removing its worktree before Codex verification and manifest-scoped Git finish.
- Bounded the Codex spine so it does not rebuild unrelated mission material, and made absent lane-local autopilot state a quiet optional input.
- Added behavior tests, operating documentation, and a reusable solution card.

## Remaining Priority

- Begin the first substantive Codex-primary production task. Let real task receipts reveal whether any further harness change is warranted.

## Core Paths

- `.agent/workflows/end-session.md` - canonical closeout behavior and operator rules
- `execution/codex_end_session.py` - Codex-native coordinator and safety policies
- `execution/verify_codex_end_session.py` - behavioral acceptance proof
- `docs/OPERATING-CODEX-AND-CLAUDE.md` - multi-surface operating contract
- `docs/solutions/2026-08-11-codex-end-session-lane-disposition.md` - root cause and reusable repair pattern

## Verification

- Codex End-session behavior verifier: PASS.
- End-session Operator Core verifier and sync check: PASS.
- End-session control-plane verifier: PASS.
- Google Operator Core, Codex authority, live-surface, harness, subagent language, and Claude/Codex parity checks: PASS.
- Platform lint: PASS in canonical main; the isolated lane still lacks ignored `.agent/cos/goals.json`, so the lane-only lint warning remains a known adapter boundary rather than permission to copy runtime state.

## Lane And Git State

- Branch: `codex/antigravity-operator-core`.
- Intended disposition: preserve the reusable operator lane.
- Intended Git policy: commit task-owned paths locally only.
- Push, merge, teardown, global receipt write, and unrelated cleanup: not authorized and not performed.

## Exact Next Prompt

```text
Use the dedicated Codex operator lane for this task. Execute through the canonical Google Antigravity owner, verify the outcome, and finish with the native /end-session closeout. Preserve the operator lane, commit only task-owned paths locally, and surface any temporary-lane merge or park action instead of leaving it hidden: [task].
```

## Do Not Rebuild

- Do not create another end-session command, cleanup harness, Git router, global skill mirror, or parallel handoff registry.
- Do not make task completion synonymous with deleting the persistent operator lane.
- Do not hide push, `main` mutation, global receipt writes, or temporary-lane debt inside a generic cleanup step.
