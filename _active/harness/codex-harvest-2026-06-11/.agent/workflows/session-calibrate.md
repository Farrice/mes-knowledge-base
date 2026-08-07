---
description: Scan the current or recent session for reusable learnings and propose safe skill, workflow, setting, or memory improvements
---

# /session-calibrate - Daily Session Learning Loop

Use this daily operator command when a session exposed corrections, preferences, repeated friction, wrong routing, tool errors, or reusable improvements.

## Usage

```text
/session-calibrate
/session-calibrate --light
/session-calibrate --apply
```

## Pre-Flight

Read only what is needed:

1. `semantic_libraries/antigravity/primitives/daily-operator-command-kit.md`
2. `extractions/video-context/xC6N_TNR8wA/timestamp-map.md` only if source trace is needed
3. `.agent/session-state.md` if present
4. `.agent/performance-log-inbox.jsonl` and `.agent/routing-feedback-inbox.jsonl` if present and relevant

Do not edit global Codex memory unless the user explicitly asks to remember or update memory.

## Behavior

### Default

Scan the current conversation plus any loaded local state and return a numbered improvement plan:

- observed correction or friction
- likely reusable lesson
- target surface: skill, workflow, setting, routing note, memory suggestion, or no change
- exact proposed edit or next command
- confidence and risk

No files are changed in default mode.

### `--light`

Return at most three high-signal improvements. Use this when token budget is low or the session had only minor friction.

### `--apply`

Apply only local, reversible changes inside `/Users/farricecain/Codex Antigravity` after the proposed edits are clear. For global writes, paid tools, destructive actions, publishing, outreach, or changes outside this workspace, ask for explicit approval.

When applying:

1. Make the smallest useful edit.
2. Preserve user changes.
3. Run the smallest relevant validator.
4. Report files changed and remaining risks.

## Output

```markdown
# Session Calibration

## Signals Found
1. ...

## Proposed Improvements
1. **[Target]**
   - Evidence:
   - Proposed change:
   - Confidence:
   - Apply now?: yes/no

## Recommended Move
...
```

