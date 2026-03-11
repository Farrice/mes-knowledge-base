---
description: Design a complete multi-agent coordination architecture using the DPVI pattern and planner-worker-judge hierarchy
---

# Orchestration Architecture Blueprint

> Load `genius.md` first. This workflow produces a complete multi-agent architecture design.

## When to Use
- Designing a new multi-agent system from scratch
- Auditing an existing multi-agent system for structural gaps
- Scaling a single-agent workflow to multi-agent coordination
- Planning long-horizon autonomous work (>1 day agent runtime)

## Input Required
- **Objective**: What the multi-agent system needs to accomplish
- **Scale**: Expected task duration, complexity, and number of parallel streams
- **Domain**: The work domain (for verifiability classification)
- **Existing infrastructure**: Current agent setup, tools, and constraints

## Execution

### Phase 1 — Domain Assessment
1. **Classify the domain** by verifiability tier:
   - Tier 1 (machine-checkable): Automated tests, compilation, mathematical validation
   - Tier 2 (expert-checkable): Experienced practitioners reach consensus on correctness
   - Tier 3 (unverifiable): Genuinely novel or subjective (<10% of work)
2. **Map existing organizational patterns** — what human team structure would solve this problem? Sprint cycles? Peer review? Draft-revise-publish?
3. **Identify the context window boundary** — at what point does the work exceed single-context capacity?

### Phase 2 — DPVI Architecture Design
For each major objective, design the four phases:

**Decompose:**
- Break the objective into subtasks that fit within a single context window
- Define clear acceptance criteria for each subtask
- Identify dependencies (sequential) vs. independent tasks (parallelizable)
- Create a recursive decomposition tree if subtasks are themselves complex

**Parallelize:**
- Assign isolated workers to independent subtask streams
- Define isolation boundaries (no cross-worker communication)
- Specify the artifact format each worker produces (not conversation state — structured output)
- Set up parallel execution environments (git worktrees, sandboxes, isolated contexts)

**Verify:**
- For Tier 1 tasks: Define automated verification (tests, compilation, constraint checking)
- For Tier 2 tasks: Build sniff-check protocol (see Sniff-Check Protocol Builder)
- Design the judge role: What does "accept" vs. "iterate" look like?
- Enable clean restart: Judge can spawn fresh context with accumulated artifacts

**Iterate:**
- Define iteration cycles (judge evaluates → planners redecompose → workers re-execute)
- Specify progress accumulation format (what carries between iterations)
- Set termination criteria (when to stop iterating)
- Build the "fresh context + artifacts" handoff protocol

### Phase 3 — Role Architecture
Define each role:

| Role | Responsibilities | Isolation Level | Coordination Protocol |
|------|-----------------|-----------------|----------------------|
| **Root Planner** | Decompose objective, spawn sub-planners | None — orchestrates everything | Writes task files, reads worker artifacts |
| **Sub-Planner(s)** | Decompose assigned sub-objective | Limited to assigned scope | Reports to root planner via artifact |
| **Worker(s)** | Execute single task to completion | Full isolation — no awareness of other workers | Reads assigned task file, writes completion artifact |
| **Judge** | Evaluate cycle output, decide iterate/accept | Reads all artifacts, no execution | Triggers fresh iteration or accepts completion |

### Phase 4 — Harness Specification
For each role, define the harness:
- [ ] **Memory**: What persists between context resets?
- [ ] **Task specification**: What document defines the work?
- [ ] **Progress tracking**: How does the agent know what's done?
- [ ] **Restart procedure**: How does a fresh context begin?
- [ ] **Isolation mechanism**: How is cross-contamination prevented?

## Output
A complete architecture document containing:
1. **Domain verifiability classification** for all subtask types
2. **DPVI flow diagram** (decomposition tree → parallel execution map → verification gates → iteration cycles)
3. **Role definitions** with responsibilities, isolation levels, and coordination protocols
4. **Harness specifications** for each role
5. **Simplification review** — what coordination can be removed without losing capability?
6. **Human overlay** — where does human sniff-checking insert into the loop?

## Quality Gate
Before finalizing, ask: "Could I remove one role or coordination layer and still get the same result?" If yes, remove it. Complexity reduction > complexity addition.
