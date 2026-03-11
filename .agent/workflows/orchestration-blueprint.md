---
description: Design a multi-agent orchestration architecture from scratch using the DPVI pattern (Decompose-Parallelize-Verify-Iterate)
---

# /orchestration-blueprint — Multi-Agent Architecture Design

Design a complete multi-agent orchestration system using Nate B. Jones's DPVI methodology.

## Workflow

### Step 1: Load Expert Context
Read `skills/nate-b-jones-orchestration-intelligence/SKILL.md` and `skills/nate-b-jones-orchestration-intelligence/genius.md` to load the orchestration intelligence methodology.

Read `skills/nate-b-jones-orchestration-intelligence/workflows/orchestration-architecture-blueprint.md` for the specific workflow.

### Step 2: Gather Objective
Ask the user:
1. What is the complex objective that requires multi-agent coordination?
2. What tools/APIs/actions are available to the agents?
3. What's the consequence profile? (reversible vs. irreversible actions)
4. Any existing agent infrastructure to build on?

### Step 3: Execute the Orchestration Architecture Blueprint Workflow
Follow the 5-phase process from the loaded workflow:
1. **Objective Decomposition** — Break the objective into parallelizable work units
2. **Agent Role Assignment** — Design planner, worker, and judge roles
3. **Coordination Protocol** — Define handoff, communication, and verification patterns
4. **Verification Architecture** — Map domains to verifiability tiers, build sniff-checks
5. **Iteration Design** — Define convergence criteria and feedback loops

### Step 4: Produce Deliverable
Output a complete orchestration architecture document:
- Agent hierarchy diagram
- Role specifications for each agent type
- Coordination protocol
- Verification criteria per domain
- Failure modes and recovery patterns
- Progressive autonomy roadmap

### Step 5: Quality Gate
Score against: Intent Alignment, Expert Standard, Adversarial Resilience.
Composite < 7 → retry weakest section.
