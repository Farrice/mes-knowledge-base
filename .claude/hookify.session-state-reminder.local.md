---
name: session-state-reminder
# amnesty 2026-07-29: disabled — no positive trigger, fired on virtually every session (pure noise).
# The session-state protocol itself is alive in CLAUDE.md (write after intent validation / 10+ reads / before compaction).
enabled: false
event: stop
action: warn
conditions:
  - field: transcript
    operator: not_contains
    pattern: session-state.md
---

**Session State Reminder**: No session state checkpoint detected in this session. Consider writing `.agent/session-state.md` with: Active Task, Decisions Made, Experts Deployed, Next Steps. This preserves context across compaction and new sessions. Protocol: `directives/session-state-protocol.md`.
