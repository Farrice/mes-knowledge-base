---
description: Design a complete multi-agent orchestration architecture using the DPVI pattern
---

# Orchestration Architecture Blueprint

Design multi-agent systems from scratch using the DPVI pattern (Decompose → Parallelize → Verify → Iterate).

## When to Use
- Building a new multi-agent system from scratch
- Redesigning an underperforming agent team
- Scaling from single-agent to multi-agent architecture
- Planning agent coordination for a complex objective

## Workflow

### Phase 1: Objective Decomposition
Break the complex objective into discrete work units.

**Inputs needed:**
- The overarching objective
- Available tools/APIs/actions
- Consequence profile (reversible vs. irreversible)

**Process:**
1. Identify the atomic tasks that compose the objective
2. Map dependencies between tasks (which must happen before which)
3. Identify tasks that can run independently (parallelizable)
4. Flag tasks with irreversible consequences for human-in-the-loop design

**Output:** Dependency graph of work units with parallelization opportunities.

### Phase 2: Agent Role Assignment (Planner-Worker-Judge)

Design the three-tier hierarchy:

**Planner Agent:**
- Receives the overarching objective
- Decomposes into work assignments
- Routes assignments to appropriate workers
- Manages iteration based on judge feedback
- Holds the "intent document" — goals, failure conditions, tradeoffs

**Worker Agents:**
- Receive specific, scoped work assignments
- Execute using their specialized tools/skills
- Return structured outputs to judges
- Have NO knowledge of other workers' tasks (isolation)
- Specialize by domain (code, copy, research, data, etc.)

**Judge Agents:**
- Evaluate worker outputs against verification criteria
- Use domain-appropriate evaluation methods:
  - Hard-verifiable domains: Boolean checks (code compiles, math checks out)
  - Soft-verifiable domains: Sniff-check protocols (does it feel right?)
  - Unverifiable domains: Flag for human review
- Return pass/fail with specific improvement instructions

### Phase 3: Coordination Protocol Design

Define how agents communicate:

1. **Message Format**: Structured output schema for each agent type
2. **Handoff Protocol**: How work moves between planner → workers → judges → planner
3. **Error Handling**: What happens when a worker fails, a judge rejects, or a planner can't decompose
4. **State Management**: Where intermediate results are stored
5. **Timeout/Budget Controls**: Token limits, time limits, retry caps

### Phase 4: Verification Architecture

Map each work domain to its verifiability tier:

| Tier | Verification Method | Autonomy Level | Examples |
|------|-------------------|----------------|----------|
| Hard-Verifiable | Boolean logic | Full automation | Code compilation, data validation, math |
| Soft-Verifiable | Sniff-check protocol | Supervised automation | Copy quality, design review, strategy |
| Unverifiable | Human judgment | Human-in-the-loop | Novel research, ethical decisions, creative judgment |

### Phase 5: Iteration Design

Define convergence:
1. What does "done" look like? (specific criteria, not vibes)
2. Maximum iteration count (prevent infinite loops)
3. Feedback format from judges back to workers
4. Escalation triggers (when to involve the planner or human)
5. Progressive quality thresholds (each iteration should improve on specific dimensions)

## Deliverable

A complete orchestration architecture document containing:
- Agent hierarchy diagram
- Role specifications with tool access for each agent
- Coordination protocol (message formats, handoffs, error handling)
- Verification criteria per domain
- Iteration/convergence design
- Failure modes and recovery patterns
- Progressive autonomy roadmap
- Cost/latency estimates
