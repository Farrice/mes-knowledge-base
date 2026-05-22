---
name: autopilot-ledger-reminder
enabled: true
event: stop
action: warn
conditions:
  - field: transcript
    operator: contains_any
    pattern: "/autopilot|autopilot engaged|autopilot session|ap-20\\d{6}|autopilot_session_id"
  - field: transcript
    operator: not_contains
    pattern: "orchestration_ledger|ORCHESTRATION LEDGER|_active/_ledgers/autopilot-"
---

**Autopilot Ledger Missing**: This session invoked `/autopilot` but no orchestration ledger was emitted. Phase 5 of the autopilot workflow is NON-OPTIONAL — the ledger is how the user gets copy-pasteable refinement prompts, suggested next moves, and the trace of what ran.

Before ending this turn, emit the ledger:

```bash
python3 execution/orchestration_ledger.py \
    --session-id "<autopilot_session_id>" \
    --since "<session_started_at ISO timestamp>"
```

This auto-archives to `_active/_ledgers/autopilot-<session_id>.md`. If you skipped Phase 5 because the run was aborted or pivoted to a different workflow, say so explicitly to the user — silent ledger-skip is the AI-Memory-Dependent-Observability anti-pattern that put this hook here.

Full Phase 5 spec: `.agent/workflows/autopilot.md` Phase 5.
