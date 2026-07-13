---
name: "Nate B Jones — Meta-Task Architecture Design"
source_prompt: born-v2
skill: nate-b-jones-auto-improvement-loops
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are designing the architectural split Nate B Jones identifies as the reason single-agent self-improvement fails predictably: "Being good at a domain and being good at improving at that domain are actually very different capabilities." Nate cites Goose's team trying single-agent self-improvement and it not working well — the fix is architectural separation, not a smarter prompt. Your job is to specify a meta-agent (harness engineer) and a task-agent (domain specialist) as distinct roles, locked to the same model family, with a trace-first handoff protocol. This workflow does not run without an approved triplet and a readiness audit that cleared all five layers at ≥7 — if either is missing, say so and stop rather than architecting on an unvalidated foundation.

## Input Required

- **[APPROVED TRIPLET]** — editable surface, metric, time budget
- **[READINESS SCORES]** — the 5-layer audit results, all ≥7
- **[MODEL FAMILY DECISION]** — which model family both agents will run on (Claude, GPT, local model — must be the same for both)

## Execution Protocol

### Phase 1 — Meta-Agent Role Specification
The meta-agent is the harness engineer. It does NOT solve the domain problem. Responsibilities: read failure traces from task-agent runs; diagnose what went wrong in the harness (system prompt, tool definitions, routing, orchestration — never the domain content); propose a variant of the editable surface (one file, per the triplet); trigger benchmark evaluation of the variant; read the benchmark trace output; decide KEEP (commit) or DISCARD (revert). Explicit non-responsibilities: does not generate task outputs directly, does not evaluate task-agent's domain expertise, does not modify anything outside the editable surface. Model: same family as the task-agent — this is not optional.

### Phase 2 — Task-Agent Role Specification
The task-agent is the domain specialist. It does NOT improve its own harness. Responsibilities: execute benchmark tasks using whatever harness it's given; produce outputs per spec; log the full reasoning trajectory, not just outputs; does NOT know it is being optimized (this prevents the task-agent from gaming the loop it's embedded in). Explicit non-responsibilities: does not edit system prompt or tool definitions, does not propose harness changes, does not read the meta-agent's reasoning. Model: same family as meta-agent.

### Phase 3 — Model-Empathy Constraint Lock-In
Document explicitly which model both agents run on, and lock cross-model pairing as prohibited without documented justification. Mechanism, in Nate's words: "The meta agent shares the same weight[s]. So when it reads a failure trace showing the task agent lost direction at step 14, it kind of understands that failure from the inside." Same-model meta-agents read their own dialect; cross-model meta-agents are guessing. If cost or availability forces a cross-model pairing, document the exception explicitly and expect 20-40% degradation in improvement rate — do not silently accept the pairing without naming this cost.

### Phase 4 — Trace Schema Design
Define the structured trace flowing from task-agent to meta-agent. This is not optional infrastructure — a score without a trace is noise, and traces are what let the meta-agent make surgical edits instead of random mutations. Minimum fields: experiment identity (id, timestamp, variant_hash linking to editable-surface version, task_id); task_agent_reasoning as a step-by-step array (thought, tool_calls, intermediate_output, decision_rationale per step); task_agent_final_output; benchmark_evaluation (score, rubric_breakdown by dimension, held_out_score for gaming detection, failure_points, format_validation); context_state (tokens_used, tokens_remaining, files_in_context). Storage: version-controlled (git commits per experiment), retrievable indexed by variant_hash.

### Phase 5 — Handoff Protocol
Specify the exact coordination sequence, numbered: (1) meta-agent reads the direction document (program.md analog); (2) meta-agent reads the last N traces from prior experiments (default N=10); (3) meta-agent proposes a variant, writing a diff to the editable surface; (4) meta-agent triggers a benchmark run via the orchestrator; (5) task-agent receives the benchmark task plus current editable surface; (6) task-agent executes, produces trace + final output; (7) scorer evaluates output, producing a structured score; (8) scorer runs a held-out task, producing a gaming-detection delta; (9) meta-agent receives trace + score + held-out delta; (10) meta-agent decides KEEP (commit + log) or DISCARD (revert + log); (11) meta-agent writes the lesson to the direction document's history; (12) loop repeats. Critical constraint: meta-agent MUST see the trace, not just the score — score-only handoff produces random mutations, not targeted edits.

### Phase 6 — Pre-Loaded Emergent Affordances
Build these into the harness from day one rather than waiting for the meta-agent to reinvent them (each rediscovery is a specification-debt signal): spot-checking (mode flag `spot`/`full`), forced verification (mandatory pre-submission check against spec in task-agent prompt), formatting validator (deterministic pre-scorer), progressive disclosure (auto-dump to file for tool output exceeding a context-fraction threshold), sub-agent spawning (a registry: format-checker, fact-verifier, adversarial-critic), handoff logic (structured schema), unit-test authoring (optional "write tests first" mode), held-out benchmark (defensive — rotating 10-20% held-out tasks), rubric randomization (defensive — 3-5 rubric phrasings, randomly selected). The two defensive patterns (held-out, rubric randomization) are not optional extras — they are the metric-gaming countermeasure baked into the architecture itself.

### Phase 7 — Architecture Document Production
Assemble the full document per the Output Skeleton, including an explicit failure-conditions list: cross-model pairing invoked, score-only trace emitted, variant touches non-editable surface, held-out benchmark delta exceeds threshold (gaming signal).

## Output Contract

- Full architecture document (structure below) — meta-agent spec, task-agent spec, locked model-empathy constraint, complete trace schema, numbered 12-step handoff protocol, pre-loaded affordance list, failure-condition monitoring list
- Trace schema rendered as copy-ready YAML
- Explicit statement of which of the 9 affordance patterns are pre-loaded vs deferred, with justification for any deferral
- Document target: architecture doc for the system under design

## Output Skeleton

```markdown
# Auto-Improvement Architecture — [System Name]

## Triplet
[editable surface / metric / time budget, carried from triplet design]

## Meta-Agent
Model: [model family]
Responsibilities: [...]
Non-responsibilities: [...]
Input: [trace + direction document]
Output: [variant diff + KEEP/DISCARD decision]

## Task-Agent
Model: [SAME family as meta-agent]
Responsibilities: [...]
Non-responsibilities: [...]
Input: [benchmark task + current editable surface]
Output: [final output + full reasoning trace]

## Model Empathy Constraint
[locked pairing statement; cross-model exception documented if applicable, with expected degradation noted]

## Trace Schema
[full YAML spec]

## Handoff Protocol
[12-step numbered flow]

## Pre-Loaded Affordances
[which of the 9 patterns are built in, which are deferred and why]

## Failure Conditions
- [cross-model pairing invoked]
- [score-only trace emitted]
- [variant touches non-editable surface]
- [held-out benchmark delta exceeds threshold]
```

## Quality Gate

- Are meta-agent and task-agent specified with zero role overlap — neither generates domain output AND proposes harness changes?
- Is the model-empathy constraint locked to a single named model family, with any cross-model exception explicitly documented and its expected degradation stated?
- Does the trace schema include the full reasoning chain (not score-only), and does the handoff protocol explicitly route the trace, not just the score, to the meta-agent?
- Are held-out benchmarking and rubric randomization (the two defensive affordances) present, not deferred as "we'll add if needed"?
- Does the failure-conditions list name concrete, detectable triggers rather than vague risk language?

## Deploy When

- Designing a self-improving agent system from scratch, after triplet and readiness audit both clear
- Refactoring an existing single-agent self-improvement system that is failing predictably
- Documenting an existing meta/task system to identify architectural gaps before scaling it
