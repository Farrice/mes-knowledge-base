---
name: session-state-reminder
enabled: true
event: stop
action: warn
conditions:
  - field: transcript
    operator: not_contains
    pattern: session-state.md
---

**Session State Reminder**: No session state checkpoint detected in this session. Consider writing `.agent/session-state.md` with: Active Task, Decisions Made, Experts Deployed, Next Steps. This preserves context across compaction and new sessions. Protocol: `directives/session-state-protocol.md`.
