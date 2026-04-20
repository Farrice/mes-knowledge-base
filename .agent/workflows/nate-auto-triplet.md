---
description: Karpathy Triplet Design — define editable surface, metric, and time budget for an auto-improvement project
---

# /nate-auto-triplet — Karpathy Triplet Design

The gate for any auto-improvement project. Define the three constraints that make the loop tractable: one editable file, one metric, one time budget.

## Workflow

### Step 1: Load Expert Context
Read `skills/nate-b-jones-auto-improvement-loops/SKILL.md` and `skills/nate-b-jones-auto-improvement-loops/genius.md` to load the auto-improvement methodology.

Read `skills/nate-b-jones-auto-improvement-loops/workflows/01-karpathy-triplet-design.md` for the specific workflow.

Cross-reference `skills/nate-b-jones-auto-improvement-loops/references/karpathy-loop-quotes.md` for source-accurate voice.

### Step 2: Gather Input
Ask the user:
1. What system are you considering for auto-improvement?
2. How is it optimized today (human ops, periodic review)?
3. What does "better" mean to the business?
4. Any known constraints on what can be changed?

### Step 3: Execute the 5-Phase Workflow
1. **Editable Surface Identification** — single-file test, out-of-scope list
2. **Metric Definition** — objectively testable, business-value correlated
3. **Time Budget Setting** — target >10 experiments/hour
4. **Fuzziness Audit** — score 0-10 on each dimension
5. **Triplet Specification Document** — single-page output with gate decision

### Step 4: Produce Deliverable
One-page Triplet Specification Document with:
- Editable surface (path + justification + out-of-scope)
- Metric (name, formula, evaluation method, baseline)
- Time budget (per experiment, overnight throughput, cost)
- Fuzziness scores per dimension
- Gate decision: PROCEED to WF 02 / FIX FIRST with specific gap

### Step 5: Quality Gate
Score against: Triplet Clarity, Judgment Leverage, Revert Capability. Minimum 7 on each. Composite ≥7.0 with no dimension <6.

### Step 6: Hand-off
- PROCEED → invoke `/nate-auto-audit` (WF 02) for readiness assessment
- FIX FIRST → complete foundation task, then re-attempt
