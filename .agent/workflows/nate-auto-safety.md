---
description: 4-Mode Safety Audit — detection and response for metric gaming, silent degradation, contamination, compounding errors
---

# /nate-auto-safety — 4-Mode Safety Audit

Not optional. "The relevant safety concerns when we're talking about autoimproving agents in the business context are not really intelligence explosions. They're about failure modes that are quiet and specific and very easy to miss."

## Workflow

### Step 1: Load Expert Context
Read `skills/nate-b-jones-auto-improvement-loops/SKILL.md` and `skills/nate-b-jones-auto-improvement-loops/genius.md`.

Read `skills/nate-b-jones-auto-improvement-loops/workflows/06-safety-audit-four-modes.md` for the specific workflow.

### Step 2: Gather Input
1. Architecture from WF 03
2. Trace infrastructure from WF 04
3. Affordances from WF 05 (patterns 8 + 9 especially)
4. Production system scope (what this will eventually touch)

### Step 3: Execute the 7-Phase Workflow
1. **Metric Gaming Detection** — held-out + OOD + business-value correlation
2. **Silent Degradation Detection** — regression + quality baseline + consistency
3. **Contamination Detection** — data isolation + eval independence + cross-contamination
4. **Compounding Errors Detection** — cross-system + canary + dependency regression
5. **Human Inspection Gates** — promotion, graduation, incident, monthly, quarterly
6. **Revert Protocol Verification** — full-cycle revert test
7. **Safety Audit Document** — composite safety score + deployment recommendation

### Step 4: Produce Deliverable
- 4-mode audit document with detection + response per mode
- Human inspection gate schedule
- Revert protocol test results
- Composite safety score
- Deployment recommendation: APPROVED / CONDITIONAL / BLOCKED

### Step 5: Quality Gate
Safety Monitoring, Revert Capability, Judgment Leverage — min 8 for customer-facing; 7 for internal.

### Step 6: Hand-off
- PASSED → `/nate-auto-takeoff` (WF 07)
- FAILED → remediate, re-audit
