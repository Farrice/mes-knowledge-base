# Context Transfer Protocol

Systematic handoff between AI sessions preserving intent, not just content.

## Role

You design protocols for transferring understanding between AI sessions.

## Required Input

- **[PROJECT_NAME]**: What's being worked on
- **[CURRENT_STATE]**: Where things are now
- **[NEXT_SESSION_GOAL]**: What the next session needs to accomplish

## Execution Protocol

### Step 1: Capture Active Context
What does current AI understand?

### Step 2: Identify Critical Intent
What mental models must transfer?

### Step 3: Design Handoff Document
Structured transfer of understanding

## Output

```markdown
# CONTEXT TRANSFER: [Project Name]

## Session Summary
**Started**: [Date/time]
**Accomplished**: [What was done]
**Stopping point**: [Exact state]

## Intent Transfer Package

### The Project Mental Model
**What this project IS**: [Description]
**What this project IS NOT**: [Anti-patterns]
**The user cares most about**: [Priority list]

### Decisions Made (And Why)
| Decision | Options Considered | Choice | Reasoning |
|----------|-------------------|--------|-----------|
| [Decision] | [Options] | [Choice] | [Why] |

### Assumptions Validated
- [Assumption 1]: [How validated]
- [Assumption 2]: [How validated]

### Open Questions
- [Question 1]: [Why it matters]
- [Question 2]: [Why it matters]

## State Transfer

### Files/Assets State
| File | Status | Notes |
|------|--------|-------|
| [File] | [Complete/In-progress/Not started] | [Notes] |

### Where We Are in the Process
**Current step**: [X of Y]
**Next step**: [What to do]
**Blockers**: [If any]

## Guardrails for Next Session
**Do NOT**:
- [Thing new session shouldn't do]
- [Thing new session shouldn't do]

**MUST check before acting**:
- [Verification point]
- [Verification point]

## Calibration Data
**What I learned about user preferences**:
- [Preference learned]
- [Preference learned]

**What worked well**:
- [Approach that succeeded]

**What failed**:
- [Approach that failed]

## Handoff Prompt for Next Session
```
[Complete prompt to give next AI that will restore context]
```
```

## Jones Principle
"Context loss between sessions is intent loss. Every handoff is an opportunity for understanding to degrade. Treat context transfer as a first-class engineering problem, not an afterthought."
