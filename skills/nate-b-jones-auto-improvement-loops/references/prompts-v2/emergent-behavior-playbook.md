---
name: "Nate B Jones — Emergent Behavior Playbook"
source_prompt: born-v2
skill: nate-b-jones-auto-improvement-loops
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are pre-loading specification debt the way Nate B Jones frames the discovery from Karpathy's meta-agent: "None of this was specified in the directive. The meta agent discovered these strategies by analyzing its own failure traces and reasoning about what would help." Nate's catalogued list — spot-checking, forced verification loops, formatting validators, unit-test steering, progressive disclosure, task-specific sub-agents, handoff logic — were all invented, not specified. Your frame: every emergent behavior a meta-agent invents is a gap in the original spec. This workflow pays down that debt in advance rather than waiting for costly rediscovery, and adds two defensive patterns (held-out benchmarking, rubric randomization) that counter the metric-gaming risk emergent capability creates.

## Input Required

- **[HARNESS ARCHITECTURE]** — the meta/task architecture this playbook applies to
- **[TRACE INFRASTRUCTURE]** — the trace schema/system already in place (affordances must emit trace data into it)
- **[EXISTING AFFORDANCES]** — what's already built, if auditing rather than designing fresh

## Execution Protocol

### Phase 1 — Pattern Inventory
Walk all 9 patterns and assess each as present/absent, quality 0-10, with observation notes: (1) spot-checking, (2) forced verification, (3) formatting validators, (4) progressive disclosure, (5) sub-agent spawning, (6) handoff logic, (7) unit-test steering, (8) held-out benchmark (defensive), (9) rubric randomization (defensive). Target: each pattern ≥7 quality, OR explicitly flagged "not needed for this harness type" with a stated justification — silent omission is not acceptable for any of the 9, especially not for patterns 8 and 9.

### Phase 2 — Pre-Load Design (for each missing or weak pattern)
Design the explicit affordance per pattern:
- **Spot-checking**: config with default mode ('spot'), escalation rule (2 consecutive spot passes → full benchmark), spot_task_count (3), full_task_count (20), rotating spot selection with a coverage floor (e.g. 20% of tasks sampled over the last N cycles).
- **Forced verification**: mandatory pre-submission section in the task-agent system prompt — re-read the spec, check each explicit requirement against the output, list gaps, either fix them or explicitly state "incomplete: [gap]," only submit after this step. Skipping it is a task failure, not a shortcut.
- **Formatting validators**: a deterministic pre-scorer that checks JSON validity if expected, required-keys presence, length bounds — run before the semantic scorer; failures trigger a format-correction retry; only passing outputs get graded.
- **Progressive disclosure**: middleware between tool call and agent context — if tool output exceeds roughly 20% of remaining context, dump to an experiment-scoped file and return a summary + file path instead of the raw output.
- **Sub-agent spawning**: a pre-built registry (format_checker, fact_verifier, adversarial_critic — each with role, model=same_as_parent, invocation pattern); spawn threshold is tasks requiring more than 2 distinct check types.
- **Handoff logic**: a structured schema with mandatory fields `{from_agent, to_agent, payload, context_summary, next_action}`.
- **Unit-test authoring** (optional, for code/structured tasks): task-agent prompt sequences spec-read → write 3-5 unit tests encoding spec requirements → implement → run/fix until passing → submit code + tests, with partial-credit scoring (tests_written × 0.3 + tests_passed × 0.7) so incomplete implementations still surface useful signal.
- **Held-out benchmark** (defensive): 15% of tasks held out, rotated per cycle, gaming-detection flag when seen_score minus held_out_score exceeds 1.5, auto-discard on flag. Held-out tasks must NEVER appear in variant-generation context — data isolation here is mandatory, not best-effort.
- **Rubric randomization** (defensive): minimum 5 phrasings per dimension, randomly selected per run, variance check across a minimum of 3 runs with a max-variance threshold of 2.0 points (0-10 scale) — exceeding it triggers a rerun with new phrasings.

### Phase 3 — Trigger Condition Mapping
For every affordance, document exactly when it fires and any cooldown: spot-check (default, escalates on 2 passes), forced verification (pre-submission of any task), format validator (pre-scorer, all tasks), progressive disclosure (tool output >20% context), sub-agent spawn (task has >2 check types), handoff schema (any multi-agent flow), unit-test authoring (code/structured output tasks only), held-out benchmark (every KEPT candidate), rubric randomization (every scoring run).

### Phase 4 — Integration with Trace System
Each affordance must emit trace data the meta-agent can consume — an invisible affordance is functionally absent. Map: spot-check → `benchmark.mode` + tasks evaluated; forced verification → `verification_step` in reasoning_chain; format validator → `format_validation_result` in evaluation; progressive disclosure → `context_dumps: [{path, size}]`; sub-agent spawn → `spawned_sub_agents: [{name, parent_trace_id}]`; handoff → `handoff_chain: [{from, to, timestamp}]`; unit-test → `tests: {written, passed}`; held-out → `held_out_score` + delta; rubric randomization → `rubric_phrasing_id` per run.

### Phase 5 — Gap Detection
After all 9 are pre-loaded, observe meta-agent behavior over the first 30 experiments and ask: what patterns does it invent beyond these 9? What failures don't match existing patterns? What affordances does it seem to "wish existed"? Add new discoveries to the catalog — the playbook itself is a living document that should absorb its own emergent-behavior findings.

## Output Contract

- 9-row pattern inventory scorecard (present/absent, quality 0-10, notes)
- Per-pattern affordance spec for every pattern scoring below 7 or absent
- Trigger condition table (all 9, condition + cooldown)
- Trace integration field list (all 9, mapped to specific trace fields)
- Gap detection monitoring plan for the post-deployment observation window
- Document target: `deliverables/emergent-affordances-[system].md`

## Output Skeleton

```markdown
# Emergent Behavior Playbook — [System Name]

## Pattern Inventory
| # | Pattern | Present? | Quality 0-10 | Notes |
|---|---------|----------|--------------|-------|
| 1 | Spot-checking | [Y/N] | [score] | [...] |
[... all 9, including both defensive patterns]

## Pre-Load Specs (missing/weak patterns)
### Pattern [N] — [Name]
[affordance spec: config/prompt-text/schema as applicable]
Integration: [how it wires into the harness]

## Trigger Conditions
| Affordance | Trigger | Cooldown |
|-----------|---------|----------|
[... all 9]

## Trace Integration
| Affordance | Trace Field Added |
|-----------|-------------------|
[... all 9]

## Gap Detection Plan
[observation window, what to watch for, cadence]
```

## Quality Gate

- Are all 9 patterns assessed, including both defensive patterns (held-out, rubric randomization) — never a subset?
- For any pattern marked "not needed," is there a stated justification, not a silent skip?
- Does every pre-loaded affordance include a trace-integration field — is any affordance built without a way for the meta-agent to see it fire?
- Is the held-out benchmark specified with explicit data-isolation language (held-out tasks never visible in variant-generation context)?
- Does the gap detection plan define a concrete observation window (e.g., first 30 experiments) rather than "monitor ongoing"?

## Deploy When

- Designing a new harness — build affordances in from day one rather than waiting for rediscovery
- Auditing an existing harness to find which of the 9 affordances are missing
- After 3+ evolution cycles, to check whether the meta-agent invented something worth cataloguing
