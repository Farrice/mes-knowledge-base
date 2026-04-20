---
description: Design the meta-agent / task-agent split with same-model pairing, handoff protocol, and trace schema. The architectural foundation for every auto-improvement system.
---

# Meta-Task Architecture Design

> Load `genius.md` first. "Being good at a domain and being good at improving at that domain are actually very different capabilities." — Nate B Jones

## Pre-Flight Gate

- Triplet approved (WF 01)
- Readiness audit passed (WF 02, all layers ≥7)
- If either is missing, STOP — do not design architecture yet

## When to Use

- Designing a self-improving agent system from scratch
- Refactoring a single-agent self-improvement system (predictable failure — see GP-4)
- Documenting an existing meta/task system to identify gaps

## Skill Acquisition

Load: `genius.md` (GP-4, GP-5, GP-6, GP-7, GP-8, SM-2, SM-3, SM-6)

## Input Required

- Approved Triplet (from WF 01)
- Readiness scores (from WF 02)
- Model family decision (Claude? GPT? local model?)

## Execution

### Phase 1 — Meta-Agent Role Specification

The meta-agent is the **harness engineer**. It does NOT solve the domain problem.

**Responsibilities**:
1. Read failure traces from task-agent runs
2. Diagnose what went wrong in the harness (system prompt, tool definitions, routing, orchestration)
3. Propose a variant of the editable surface (one file, per GP-1)
4. Trigger benchmark evaluation of the variant
5. Read benchmark trace output
6. Decide: KEEP (commit change) or DISCARD (revert)

**Explicit NON-responsibilities**:
- Does NOT generate task outputs directly
- Does NOT evaluate task-agent's domain expertise
- Does NOT modify anything outside the editable surface

**Model**: same family as task-agent (GP-5 model empathy).

### Phase 2 — Task-Agent Role Specification

The task-agent is the **domain specialist**. It does NOT improve its own harness.

**Responsibilities**:
1. Execute benchmark tasks using whatever harness it has
2. Produce outputs per spec
3. Log full reasoning trajectory (not just outputs)
4. Does NOT know it is being optimized (prevents gaming)

**Explicit NON-responsibilities**:
- Does NOT edit system prompt or tool definitions
- Does NOT propose harness changes
- Does NOT read meta-agent's reasoning

**Model**: same family as meta-agent (GP-5).

### Phase 3 — Model-Empathy Constraint Lock-In

Document the constraint explicitly:

```markdown
## Model Empathy Constraint

- Meta-Agent Model: [Claude Opus 4.7 / GPT-5 / etc.]
- Task-Agent Model: [SAME as Meta-Agent]
- Cross-model pairings PROHIBITED without documented justification

Rationale (from genius.md GP-5): "The meta agent shares the same weight. So when it reads a failure trace showing the task agent lost direction at step 14, it kind of understands that failure from the inside."
```

Edge case: if Meta and Task MUST use different models (e.g., cost constraints), the cross-model penalty must be documented and monitored. Expect 20-40% degradation in improvement rate.

### Phase 4 — Trace Schema Design

Define the structured trace that flows from task-agent → meta-agent.

Minimum fields (GP-6, SM-3):

```yaml
trace:
  experiment_id: uuid
  timestamp: iso8601
  variant_hash: sha256  # links to editable-surface version
  task_id: string
  
  task_agent_reasoning:
    - step: integer
      thought: string
      tool_calls: []
      intermediate_output: string
      decision_rationale: string
  
  task_agent_final_output: string
  
  benchmark_evaluation:
    score: float
    rubric_breakdown: {dimension: score}
    held_out_score: float  # Pattern 8 from emergent-behaviors-catalog
    failure_points: []  # where task-agent lost direction
    format_validation: pass/fail
  
  context_state:
    tokens_used: int
    tokens_remaining: int
    files_in_context: []
```

Storage: version-controlled (git commits per experiment). Retrieval: indexed by variant_hash for meta-agent query.

### Phase 5 — Handoff Protocol

The exact coordination between meta-agent and task-agent.

```
1. Meta-agent reads evolution-direction.md (program.md analog)
2. Meta-agent reads last N traces from prior experiments (default N=10)
3. Meta-agent proposes variant (writes diff to editable surface)
4. Meta-agent triggers benchmark run via orchestrator
5. Task-agent receives benchmark task + current editable surface
6. Task-agent executes, produces trace + final output
7. Scorer evaluates output → produces structured score
8. Scorer runs held-out task → produces gaming-detection delta
9. Meta-agent receives trace + score + held-out delta
10. Meta-agent decides KEEP (commit + log) or DISCARD (revert + log)
11. Meta-agent writes lesson to direction.md history
12. Loop repeats for next experiment
```

Critical: meta-agent MUST see trace, not just score. Score-only handoff → GP-6 violation → random mutations.

### Phase 6 — Pre-Loaded Emergent Affordances (Pattern Library from `references/emergent-behaviors-catalog.md`)

Build these into the harness from Day 1:

| Pattern | Affordance |
|---------|-----------|
| Spot-checking | Harness flag `benchmark_mode: 'spot' \| 'full'` |
| Forced verification | "Verify against spec" step in task-agent prompt |
| Formatting validator | Pre-scoring format check |
| Progressive disclosure | Auto-dump to file for tool output >N tokens |
| Sub-agent spawning | Sub-agent registry (format-checker, fact-verifier, adversarial-critic) |
| Handoff logic | Structured handoff schema |
| Unit-test authoring | Optional "write tests first" mode |
| **Held-out benchmark** (defensive) | Rotating 10-20% held-out tasks |
| **Rubric randomization** (defensive) | 3-5 rubric phrasings, random selection |

### Phase 7 — Architecture Document Production

Produce the full architecture doc:

```markdown
# Auto-Improvement Architecture — [System Name]

## Triplet (from WF 01)
[editable surface, metric, time budget]

## Meta-Agent
- Model: [model]
- Responsibilities: [...]
- Input: [trace + direction.md]
- Output: [variant diff + KEEP/DISCARD decision]

## Task-Agent
- Model: [SAME as meta-agent]
- Responsibilities: [...]
- Input: [benchmark task + current editable surface]
- Output: [final output + full reasoning trace]

## Model Empathy Constraint
[locked: Meta = Task model family]

## Trace Schema
[full YAML spec]

## Handoff Protocol
[12-step flow]

## Pre-Loaded Affordances
[9 patterns from catalog]

## Failure Conditions
- Cross-model pairing invoked
- Score-only trace emitted
- Variant touches non-editable surface
- Held-out benchmark delta > threshold (gaming)
```

## Content Type Adaptations

| System | Meta-Agent Focus | Task-Agent Focus | Trace Critical Fields |
|--------|-----------------|-----------------|----------------------|
| Harness optimization | Prompt structure, tool definitions | Execute benchmark tasks | Reasoning chain + tool-call sequence |
| Content workflow | Workflow step ordering | Generate content per spec | Draft iterations + rationale |
| Pricing engine | Pricing rule logic | Score pricing outcomes | Market inputs + rule application |
| Fraud model | Detection threshold tuning | Classify transactions | Feature values + decision path |

## Output Requirements

- Full architecture document
- Trace schema (copyable YAML)
- Handoff protocol (12-step flow, numbered)
- Pre-loaded affordance list (reference: `emergent-behaviors-catalog.md`)
- Failure condition monitoring list

## Quality Gate (from genius.md rubric)

- **Meta/Task Separation** (0-10): distinct roles, no overlap, same-model pairing?
- **Trace Infrastructure Depth** (0-10): full trajectory, not just scores?
- **Safety Monitoring** (0-10): held-out + rubric randomization pre-loaded?

Minimum: 7 on each.

## Anti-Patterns

- ❌ Single-agent self-improvement (GP-4 violation — predictable failure)
- ❌ Cross-model pairing without documented justification (GP-5)
- ❌ Score-only handoff (GP-6)
- ❌ Omitting pre-loaded affordances (waits for rediscovery)
- ❌ No held-out benchmark (metric-gaming blind spot)

## Hand-off

- Architecture approved → `/nate-auto-traces` (WF 04) for trace infrastructure build
- Architecture rejected → return to WF 02 readiness audit
