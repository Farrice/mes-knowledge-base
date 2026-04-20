---
description: Trace Infrastructure Blueprint — reasoning-trajectory logging schema, storage, retrieval, analysis for any agent system
---

# /nate-auto-traces — Trace Infrastructure Blueprint

Build traces BEFORE optimization. "The quality of your trace infrastructure determines the quality of your auto improvement."

## Workflow

### Step 1: Load Expert Context
Read `skills/nate-b-jones-auto-improvement-loops/SKILL.md` and `skills/nate-b-jones-auto-improvement-loops/genius.md`.

Read `skills/nate-b-jones-auto-improvement-loops/workflows/04-trace-infrastructure-blueprint.md` for the specific workflow.

### Step 2: Gather Input
1. Agent system architecture (what agents exist, what they do)
2. Current logging state (what's captured today)
3. Storage constraints (budget, retention policy)

### Step 3: Execute the 6-Phase Workflow
1. **Reasoning Chain Schema** — full trace YAML spec
2. **Decision Point Instrumentation** — 8 minimum instrumentation points
3. **Failure Capture** — 6 failure types with capture mechanisms
4. **Storage + Retrieval** — format, partitioning, retention, indexing
5. **Analysis Layer** — direct access, summarizer, or query DSL
6. **Implementation Checklist** — validation of build completeness

### Step 4: Produce Deliverable
- Trace schema (copyable YAML)
- 8 instrumentation points documented
- Storage architecture decision
- Retrieval query patterns
- Implementation checklist
- Document at `deliverables/trace-infrastructure-[system].md`

### Step 5: Quality Gate
Trace Infrastructure Depth, Prerequisite Completeness, Judgment Leverage — min 7 each.

### Step 6: Hand-off
- Built → `/nate-auto-emergent` (WF 05) for affordance pre-load
- Incomplete → remediate gaps
