---
name: codex-end-session-lane-disposition
problem_signature: "Codex-native end-session treated the persistent operator lane like an ephemeral task lane and coupled safe closeout to implicit push or global writes"
domain: system
tags: [codex, end-session, worktree, git-safety, handoff]
date: 2026-08-11
status: active
session: "019ff141-3893-78d1-bfc3-ba5c1eb298ba"
---

## Problem

The Codex coordinator called the shared closeout spine before its own verifiers
and Git gate. The spine's last step could merge and remove the current worktree,
while the coordinator still needed that worktree. The coordinator also pushed a
Codex branch and wrote global receipts by default. That made a normal local
closeout capable of crossing three separate boundaries: lane teardown, remote
Git mutation, and global state mutation.

## Root Cause

The system had one lane lifecycle for two different objects. Temporary task
lanes are meant to merge or park; `codex/antigravity-operator-core` is a
persistent operational workbench. Task completion, lane disposition, Git sync,
and receipt location were implicit side effects instead of independent policies.

## Approach That Worked

1. Add explicit `lane_disposition`, `git_sync`, and `global_receipts` policies
   with safe Codex defaults: auto-classify the operator branch as persistent,
   commit locally, and keep global writes off.
2. Force the shared spine to leave the lane in place until Codex verification
   and manifest-scoped Git finish, and run its bounded mode so it does not
   rebuild unrelated mission artifacts. Treat absent per-session autopilot state
   as optional. Return temporary-lane merge as an exact, approval-required
   action; keep incomplete `done` tasks pinned.

## Dead Ends

- Blindly running the shared spine from the persistent operator lane would have
  attempted the legacy auto-merge path and could have removed the active lane.
- Treating a branch push as part of "commit" hid an external side effect inside
  ordinary hygiene.
- A separate Codex cleanup command would have duplicated the canonical
  `/end-session` contract instead of fixing its lifecycle boundary.

## Verification

- `python3 execution/verify_codex_end_session.py`
- `python3 execution/verify_operator_core_end_session.py`
- `python3 execution/verify_system_control_plane.py --section end-session`
- `python3 execution/sync_operator_core_end_session.py --check`
- `python3 execution/verify_google_operator_core.py`
- Canonical-main `python3 execution/platform_compiler.py lint --json`

The behavior verifier proves local commit by default, global receipt skip,
persistent-lane preservation, temporary-lane approval surfacing, and the
pre-teardown spine guard without performing a push.

## Weaker-Model Trap

A weaker implementation equates "session done" with "delete the worktree" or
equates "save the work" with "push it." Those are different decisions. Close
the task first, then resolve the lane, remote, and global boundaries separately.

## Pointers

- `execution/codex_end_session.py`
- `execution/session_closeout_intelligence.py`
- `execution/verify_codex_end_session.py`
- `execution/verify_end_session_intelligence.py`
- `.agent/workflows/end-session.md`
- `docs/OPERATING-CODEX-AND-CLAUDE.md`
- `docs/solutions/2026-08-06-parallel-session-lanes.md`
