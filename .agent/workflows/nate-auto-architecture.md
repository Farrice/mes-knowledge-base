---
description: Meta-Task Architecture Design — meta-agent/task-agent split, same-model pairing, trace schema, handoff protocol
---

# /nate-auto-architecture — Meta-Task Architecture Design

Design the meta/task split that makes self-improvement work. "Being good at a domain and being good at improving at that domain are actually very different capabilities."

## Workflow

### Step 1: Load Expert Context
Read `skills/nate-b-jones-auto-improvement-loops/SKILL.md` and `skills/nate-b-jones-auto-improvement-loops/genius.md`.

Read `skills/nate-b-jones-auto-improvement-loops/workflows/03-meta-task-architecture.md` for the specific workflow.

Cross-reference `skills/nate-b-jones-auto-improvement-loops/references/emergent-behaviors-catalog.md` for affordance catalog.

### Step 2: Gather Input
1. Approved Triplet (from WF 01)
2. Readiness scores (from WF 02) — all layers ≥7 required
3. Model family decision (Claude? GPT? local?)

### Step 3: Execute the 7-Phase Workflow
1. **Meta-Agent Role Specification** — harness engineer, not domain solver
2. **Task-Agent Role Specification** — domain specialist, not self-improver
3. **Model-Empathy Constraint Lock-In** — same-model pairing required
4. **Trace Schema Design** — full reasoning trajectory, not scores
5. **Handoff Protocol** — 12-step flow between meta and task
6. **Pre-Loaded Emergent Affordances** — 9 patterns from catalog
7. **Architecture Document Production** — full spec with failure conditions

### Step 4: Produce Deliverable
- Full architecture document
- Trace schema (YAML)
- Handoff protocol (numbered flow)
- Pre-loaded affordance list
- Failure condition monitoring list

### Step 5: Quality Gate
Meta/Task Separation, Trace Infrastructure Depth, Safety Monitoring — min 7 each.

### Step 6: Hand-off
- Approved → `/nate-auto-traces` (WF 04)
- Rejected → return to WF 02 readiness audit

**Execution prompts**: before producing the deliverable, check `skills/nate-b-jones-auto-improvement-loops/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
