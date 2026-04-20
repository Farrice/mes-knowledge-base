---
description: Auto-Improvement Readiness Audit — 5-layer prerequisite scorecard (context, trace, eval, sandbox, governance) with gap remediation plan
---

# /nate-auto-audit — Auto-Improvement Readiness Audit

Assess whether a team/system is ready for auto-improvement. "Auto improvement is like a graduate level capability when most orgs are struggling with agents 101."

## Workflow

### Step 1: Load Expert Context
Read `skills/nate-b-jones-auto-improvement-loops/SKILL.md` and `skills/nate-b-jones-auto-improvement-loops/genius.md`.

Read `skills/nate-b-jones-auto-improvement-loops/workflows/02-auto-improvement-readiness-audit.md` for the specific workflow.

### Step 2: Gather Input
1. Approved Triplet from WF 01 (required)
2. Team/system context: infrastructure, team size, tooling
3. Access to systems for inspection (or interview access)

### Step 3: Execute the 7-Phase Workflow
For each of 5 layers, score 0-10 with evidence:
1. **Context Layer** — structured external memory, persistent state
2. **Trace Infrastructure** — reasoning chains, not outcomes
3. **Eval Harness** — business-value correlated scoring
4. **Sandboxed Execution** — isolated experimentation
5. **Governance** — ownership, review, promotion clarity

Then: composite assessment + gap remediation plan (if any layer <7).

### Step 4: Produce Deliverable
- 5-layer scorecard with justifications
- Composite decision: PROCEED / BUILD FIRST / STOP
- Gap remediation plan with sequenced tasks (if any layer <7)
- Document at `deliverables/readiness-audit-[system-name].md`

### Step 5: Quality Gate
Score against: Prerequisite Completeness, Trace Infrastructure Depth, Revert Capability. Minimum 7 on each.

### Step 6: Hand-off
- PROCEED → invoke `/nate-auto-architecture` (WF 03)
- BUILD FIRST → remediation owners + re-audit schedule
- STOP → scope foundational project
