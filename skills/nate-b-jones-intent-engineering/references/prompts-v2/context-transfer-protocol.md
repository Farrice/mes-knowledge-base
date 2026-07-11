---
name: "Context Transfer Protocol"
source_prompt: "skills/nate-b-jones-intent-engineering/references/prompts/context-transfer-protocol.md"
skill: nate-b-jones-intent-engineering
standard: structure-pure-v2
refactored: 2026-07-11
---

# Context Transfer Protocol

Systematic handoff between AI sessions that preserves intent, not just content.

---

## ROLE & ACTIVATION

You design protocols for transferring understanding between AI sessions. Context loss between sessions is intent loss — every handoff is an opportunity for understanding to degrade. Treat context transfer as a first-class engineering problem, not an afterthought: the next session needs the mental model, not just the file list.

---

## INPUT REQUIRED

- **[PROJECT_NAME]**: What's being worked on
- **[CURRENT_STATE]**: Where things are now
- **[NEXT_SESSION_GOAL]**: What the next session needs to accomplish

---

## EXECUTION PROTOCOL

### Step 1: Capture Active Context
What does the current session understand that isn't written down anywhere else?

### Step 2: Identify Critical Intent
Which mental models — priorities, rejected options, learned preferences — must transfer for the next session to act correctly on the first try?

### Step 3: Design Handoff Document
Structure the transfer so understanding, not just state, survives the boundary.

---

## DEPLOY WHEN

Ending a session on [PROJECT_NAME] that will be picked up later — by you, by a teammate, or by a fresh AI session with no memory of this conversation — especially when [CURRENT_STATE] includes decisions, rejected approaches, or user preferences that aren't recoverable from the files alone.

---

## Output Contract

A **CONTEXT TRANSFER** document containing exactly these components, each grounded in the actual [PROJECT_NAME], [CURRENT_STATE], and [NEXT_SESSION_GOAL] supplied — never generic status-update boilerplate:

1. **Session Summary** — start point, what was accomplished, exact stopping point
2. **Intent Transfer Package** — the project mental model (what it is / isn't, top priorities), decisions made with reasoning, validated assumptions, and open questions
3. **State Transfer** — file/asset status and current position in the process
4. **Guardrails for Next Session** — explicit do-nots and required pre-action checks
5. **Calibration Data** — what was learned about user preferences, what worked, what failed
6. **Handoff Prompt** — a single ready-to-paste prompt that restores context for the next session

**Format**: Markdown document with labeled section headers, matching the skeleton below.

---

## Output Skeleton

```
# CONTEXT TRANSFER: [Project Name]

## Session Summary
**Started**: [date/time]
**Accomplished**: [what was done]
**Stopping point**: [exact state]

## Intent Transfer Package

### The Project Mental Model
**What this project IS**: [description]
**What this project IS NOT**: [anti-patterns]
**The user cares most about**: [priority list]

### Decisions Made (And Why)
| Decision | Options Considered | Choice | Reasoning |
|----------|-------------------|--------|-----------|
| [decision] | [options] | [choice] | [why] |
[repeat for each material decision]

### Assumptions Validated
- [assumption]: [how validated]
[repeat for each validated assumption]

### Open Questions
- [question]: [why it matters]
[repeat for each open question]

## State Transfer

### Files/Assets State
| File | Status | Notes |
|------|--------|-------|
| [file] | [Complete/In-progress/Not started] | [notes] |
[repeat for each file/asset]

### Where We Are in the Process
**Current step**: [X of Y]
**Next step**: [what to do]
**Blockers**: [if any]

## Guardrails for Next Session
**Do NOT**:
- [thing next session shouldn't do]
[repeat as needed]

**MUST check before acting**:
- [verification point]
[repeat as needed]

## Calibration Data
**What I learned about user preferences**:
- [preference learned]

**What worked well**:
- [approach that succeeded]

**What failed**:
- [approach that failed]

## Handoff Prompt for Next Session
[complete prompt to give the next AI session that will restore context]
```

---

## Quality Gate

- [ ] "Stopping point" states an exact, checkable state — not a vague "mostly done"
- [ ] Every row in Decisions Made includes the rejected options, not just the choice — the reasoning is meaningless without knowing what else was considered
- [ ] Guardrails for Next Session name specific actions to avoid, not generic caution ("be careful")
- [ ] The Handoff Prompt is self-contained — a session with zero other context could act correctly from it alone
- [ ] Calibration Data distinguishes what worked from what failed; it is not a single undifferentiated list
- [ ] Nothing in the output is invented to fill a section — any component with no real content is marked [none captured this session] rather than fabricated
