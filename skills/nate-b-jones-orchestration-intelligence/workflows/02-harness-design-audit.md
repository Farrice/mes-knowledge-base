---
description: Audit agent scaffolding for memory, task files, progress tracking, restart procedures, and isolation — diagnose harness gaps before blaming model capability
---

# Harness Design Audit

> Load `genius.md` first. This workflow diagnoses harness gaps in any agent system.

## When to Use
- Agents are capable but inconsistent in output quality
- You suspect harness problems rather than intelligence problems
- Before upgrading to a more expensive model
- After deploying a new agent that's underperforming expectations
- Periodic maintenance audit on existing agent infrastructure

## Input Required
- **Agent(s) to audit**: Specific agent names, files, or system identifiers
- **Failure symptoms**: What inconsistency or unreliability looks like
- **Current harness elements**: What scaffolding currently exists (if known)

## Execution

### Phase 1 — 5-Point Harness Inspection
For each agent, evaluate against the Harness Checklist:

**1. Persistent Memory**
- [ ] Does the agent have a memory mechanism that survives context resets?
- [ ] Format: Task files, progress logs, structured artifacts, conversation summaries?
- [ ] Scope: What does the agent remember? What does it forget?
- **Gap indicator**: Agent repeats work, loses context between sessions, or contradicts previous outputs.

**2. Clear Task Specification**
- [ ] Does the agent have a written specification defining its objective?
- [ ] Does the specification include: objective, constraints, communication channels, failure modes?
- [ ] Can a "literal-minded but creative employee" follow this specification without misinterpretation?
- **Gap indicator**: Agent produces correct-but-wrong-direction output, misinterprets scope, or solves the wrong problem.

**3. Progress Tracking**
- [ ] Can the agent determine what's done, what's remaining, and what failed?
- [ ] Format: Task checklist, completion percentages, phase markers?
- [ ] Is progress visible to judges/planners (not just the worker)?
- **Gap indicator**: Agent restarts completed work, skips steps, or can't report its own status.

**4. Restart Procedures**
- [ ] Can the agent begin a fresh context without losing accumulated progress?
- [ ] Is there a handoff artifact (not full conversation history) that carries essential state?
- [ ] Can a judge trigger a clean restart that improves on the last iteration?
- **Gap indicator**: Agent degrades over long sessions, accumulates errors, or can't recover from bad paths.

**5. Isolation Mechanisms**
- [ ] Does the agent execute without contamination from other agents' contexts?
- [ ] Are execution environments separated (sandboxes, worktrees, isolated contexts)?
- [ ] Can multiple workers run in parallel without coordination overhead?
- **Gap indicator**: Agent outputs vary when run alongside other agents, or agents block each other.

### Phase 2 — Diagnose the Gap Pattern
Score: ___/5 harness elements present.

| Score | Diagnosis | Action |
|-------|-----------|--------|
| 5/5 | Harness is solid — issue is likely model capability or specification quality | Investigate prompt design or model fit |
| 3-4/5 | Partial harness — fix missing elements before other interventions | Implement missing elements (see Phase 3) |
| 1-2/5 | Harness failure — agent is operating without organizational structure | Full harness build required |
| 0/5 | No harness — agent is working "in 30 seconds with no notes" | Stop. Build harness before any further deployment |

### Phase 3 — Fix Protocol
For each missing harness element, produce:
1. **Implementation specification**: Exact mechanism to add (file format, storage location, update triggers)
2. **Integration steps**: How to wire it into the existing agent workflow
3. **Verification test**: How to confirm the fix is working
4. **Expected impact**: What improvement to expect from this specific fix

### Phase 4 — Simplification Pass
After fixing gaps, check for unnecessary complexity:
- Are there coordination layers that can be removed?
- Are there verification steps that are redundant?
- Can inter-agent communication be eliminated in favor of artifact-based handoffs?

**Decision rule**: If the system performs just as well without a component, remove the component.

## Output
A harness audit report containing:
1. **Per-agent scorecard** (5-point inspection with gap indicators)
2. **Diagnosis** (harness failure vs. model limitation vs. specification issue)
3. **Fix plan** with implementation specs, integration steps, and verification tests
4. **Simplification recommendations** (components to remove)
5. **Before/after prediction** (expected improvement from harness fixes alone)
