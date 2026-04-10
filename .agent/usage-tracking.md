# Claude Code Usage Tracking

Track sessions to understand burn rate patterns and identify if this is bugs vs. intentional throttling.

## Format
```
Date: YYYY-MM-DD
Time Started: HH:MM PT (note if in peak hours 5am-11am PT)
Session Duration: X minutes until limit hit
Prompts Sent: X
Tasks Completed: [brief list]
Experts Loaded: [list]
Hit Limit?: Yes/No
Notes: [any errors, cache warnings, unusual behavior]
```

## Sessions

### 2026-04-03
- Time Started: [FILL IN]
- Session Duration: [FILL IN]
- Prompts Sent: [FILL IN]
- Tasks Completed: [FILL IN]
- Experts Loaded: [FILL IN]
- Hit Limit?: [FILL IN]
- Notes: [FILL IN]

---

## Analysis After 1 Week

**Patterns to look for:**
1. Does burn rate correlate with peak hours (5am-11am PT)?
2. Does it correlate with specific experts/workflows?
3. Average prompts per session before hitting limit?
4. Is it getting worse over time or stable?

**Decision criteria:**
- If <10 prompts consistently = severe bug impact, need workarounds
- If 10-20 prompts = moderate, wait for fixes + safe optimizations
- If >20 prompts = working as intended given new limits
