---
description: Emergent Behavior Playbook — pre-load 9 harness affordances (7 emergent + 2 defensive) instead of waiting for meta-agent rediscovery
---

# /nate-auto-emergent — Emergent Behavior Playbook

Pre-load specification debt. "None of this was specified in the directive. The meta agent discovered these strategies by analyzing its own failure traces."

## Workflow

### Step 1: Load Expert Context
Read `skills/nate-b-jones-auto-improvement-loops/SKILL.md` and `skills/nate-b-jones-auto-improvement-loops/genius.md`.

Read `skills/nate-b-jones-auto-improvement-loops/workflows/05-emergent-behavior-playbook.md` for the specific workflow.

Read full catalog: `skills/nate-b-jones-auto-improvement-loops/references/emergent-behaviors-catalog.md`.

### Step 2: Gather Input
1. Harness architecture from WF 03
2. Trace infrastructure from WF 04
3. Existing affordances (if any) to audit

### Step 3: Execute the 5-Phase Workflow
1. **Pattern Inventory** — assess all 9 patterns present/absent, 0-10 quality
2. **Pre-Load Design** — affordance spec for each missing/weak pattern
3. **Trigger Condition Mapping** — when each affordance fires
4. **Integration with Trace System** — trace field per affordance
5. **Gap Detection** — monitor for NEW emergent patterns in first 30 experiments

### Step 4: Produce Deliverable
- Pattern inventory scorecard (9 patterns)
- Per-pattern affordance spec (missing/weak)
- Trigger condition table
- Trace integration field list
- Document at `deliverables/emergent-affordances-[system].md`

### Step 5: Quality Gate
Safety Monitoring, Trace Infrastructure Depth, Prerequisite Completeness — min 7 each.

### Step 6: Hand-off
- Loaded → `/nate-auto-safety` (WF 06)

**Execution prompts**: before producing the deliverable, check `skills/nate-b-jones-auto-improvement-loops/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
