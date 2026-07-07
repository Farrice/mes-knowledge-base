---
name: SessionEnd Hook Re-Entry Guard
problem_signature: SessionEnd hook side-effects (closeout spine) double-fire on clear+exit because PostToolUse marker-detection can't see hook-internal subprocess calls
domain: system
tags: [hooks, session-management, closeout, idempotency, ledger]
date: 2026-07-07
status: active
session: harness-apex-2026-07-07
---

## Problem

`session_end_hook.py` runs `end_session_closeout.py --degraded` as a backstop when a
session produced artifacts but `/end-session` never ran. SessionEnd can fire twice
(clear, then exit) — without a guard, the second fire re-runs the spine, duplicating
the COS journal line, sovereign-memory milestone, and session-state archive.

## Root Cause

`session_ledger_hook.py`'s `handle_posttool` detects finished work by scanning Bash
output for markers (e.g. `CLOSEOUT SPINE COMPLETE`). That only works when the spine
runs *inside* the session via a Bash tool call. `session_end_hook.py` invokes the spine
itself via `subprocess.run` from *outside* any observed tool call — the marker-detection
path and the auto-run path are structurally invisible to each other.

## Approach That Worked

1. Added `closeout_ran: False` to the ledger's default shape (`_load`, ~line 88).
2. `handle_posttool` sets it True on marker/invocation match (in-session path).
3. `session_end_hook.py` checks `closeout_ran` first and exits silently if True.
4. After running its own degraded closeout, it writes `closeout_ran = True` back to
   its own ledger file directly — not via PostToolUse. This is the fix: the hook
   authors its own idempotency marker instead of trusting one set elsewhere.

## Dead Ends

- Relying on PostToolUse marker detection alone — it can't see hook-internal calls.
- Assuming a ledger field gets set correctly everywhere just because it's declared.

## Verification

Traced every code path that can set `closeout_ran`: in-session marker detection and
the hook's own write-back. Confirmed a second SessionEnd fire hits the top-of-`main()`
guard before any subprocess call.

## Weaker-Model Trap

Sees the flag in the schema and assumes it's set on every path that matters, without
tracing WHO writes `True` on each entry point. A fix that only patches the schema
ships a flag that's dead on exactly the path (hook-internal subprocess) it existed for.

## Pointers

- `execution/hooks/session_ledger_hook.py` (`_load` ~88; closeout-detection ~335)
- `execution/hooks/session_end_hook.py` (re-entry guard + write-back, lines 85-93)
- `.agent/workflows/end-session.md` §"Deterministic backstop"
