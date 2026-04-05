---
description: JCC Pulse — mission status dashboard
---

# /jcc-pulse — JARVIS Command Center Mission Pulse

Show quick status of all active workstreams, completed work, and items needing attention.

## Execution

Display the current Mission Pulse:

```
━━━ MISSION PULSE ━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Mission Name] | [Scale]

  [✓/►/○] [Workstream] — [Expert] [Status]
  ...

  ⚡ [N] decisions need your input (if any)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

1. Check current task states (TaskList if available)
2. Review any pending checkpoints or blockers
3. If no mission is active, say so and offer `/solo`, `/strike`, `/campaign`, or `/jcc-deploy`
