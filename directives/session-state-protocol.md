# Session State Anchor Protocol

> **Purpose**: Prevent context drift after compaction by writing checkpoint files at key moments. When compaction occurs, re-read the anchor to recover precise context instead of relying on lossy summaries.
> **State File**: `.agent/session-state.md`
> **Created**: 2026-02-27

---

## Why This Exists

When Claude Code compacts conversations (summarizing older turns to free context), fine details get lost:
- Decisions and their rationale flatten into vague summaries
- Expert context and patterns applied get dropped
- The "thread" of multi-step work loses precision
- Follow-up work drifts from the original validated intent

**Session state anchors** are checkpoint files that survive compaction. Re-reading them restores precise context.

---

## Anchor Format

Write to `.agent/session-state.md`:

```markdown
# Session State Anchor
> Last updated: [ISO timestamp]

## Active Task
[1-2 sentence description of what we're working on]

## Intent (Validated)
- **Deliverable**: [what]
- **Audience**: [who]
- **Success criteria**: [what "done" looks like]

## Decisions Made
- [Decision 1]: [choice made] — [rationale in <10 words]
- [Decision 2]: [choice made] — [rationale]

## Experts Deployed
- [Expert Name]: [what they contributed, 1 line]
- Patterns applied: [list by name]

## Key Findings (Compressed)
- [Finding 1]: [1-line]
- [Finding 2]: [1-line]

## Files Created/Modified This Session
- [path]: [what it is]

## Current Phase
[Where we are in the workflow]

## Next Steps
1. [Next action]
2. [Next action]
```

---

## When to Write

| Trigger | What to Anchor |
|---------|---------------|
| After intent validation (DICE protocol completes) | The validated intent so it survives compaction |
| After major analysis (research, extraction, brief) | Key findings and methodology |
| After expert deployment (skill loaded and applied) | Which experts, which patterns, what they produced |
| After any user decision (chose direction, confirmed approach) | The decision and rationale |
| Before spawning sub-agents | Current state so main thread resumes cleanly |
| When 10+ file reads have occurred in the session | Preemptive anchor before context fills |

---

## When to Read

| Trigger | Why |
|---------|-----|
| After compaction occurs (context feels thin, prior details seem vague) | Recover precise context |
| After returning from sub-agent work | Pick up the main thread |
| At start of a continued/resumed session | Restore prior session state |
| When uncertain about a prior decision | Verify against the anchor |

---

## Staleness Warning

The anchor includes a timestamp. If the current conversation has diverged significantly from the anchored state (e.g., user changed direction mid-session), treat the anchor as **directional guidance**, not gospel. Update the anchor to reflect the new direction.

---

## Execution Integration

Session state functions are available in `execution/checkpoint_manager.py`:
- `save_session_state(state)` — Writes the anchor file
- `load_session_state()` — Reads and returns anchor contents

These keep state management deterministic (Layer 3) while the agent (Layer 2) decides when to trigger them.

---

## Graceful Failure

If the state file doesn't exist or can't be read, fall back to the compacted summary. No hard dependency. The anchor is an enhancement, not a requirement.

---

*Created: 2026-02-27 | Context Engine v1.0*
