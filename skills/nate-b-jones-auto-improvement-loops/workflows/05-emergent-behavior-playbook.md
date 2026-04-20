---
description: Explicit harness affordances for 7 documented emergent patterns plus 2 defensive patterns. Pre-load specification debt instead of waiting for rediscovery.
---

# Emergent Behavior Playbook

> Load `genius.md` first. "None of this was specified in the directive. The meta agent discovered these strategies by analyzing its own failure traces and reasoning about what would help." — Nate B Jones

## Pre-Flight Gate

Emergent behaviors are specification debt signals (HK-4). Pre-loading = paying debt before starting the loop.

## When to Use

- Designing a new harness (build affordances from Day 1)
- Auditing existing harness (which affordances are missing?)
- After 3+ evolution cycles (check if meta-agent invented something to catalog)

## Skill Acquisition

Load: `genius.md` (GP-7, HK-4, SM-6), `references/emergent-behaviors-catalog.md` (full catalog, 9 patterns)

## Input Required

- Harness architecture from WF 03
- Trace infrastructure from WF 04
- Existing affordances (if any) to audit

## Execution

### Phase 1 — Pattern Inventory

Walk through all 9 patterns from `emergent-behaviors-catalog.md`. For each, assess:

| Pattern | Present? | Quality 0-10 | Notes |
|---------|---------|--------------|-------|
| 1. Spot-checking | Y/N | [score] | [observations] |
| 2. Forced verification | Y/N | [score] | |
| 3. Formatting validators | Y/N | [score] | |
| 4. Progressive disclosure | Y/N | [score] | |
| 5. Sub-agent spawning | Y/N | [score] | |
| 6. Handoff logic | Y/N | [score] | |
| 7. Unit-test steering | Y/N | [score] | |
| 8. Held-out benchmark (defensive) | Y/N | [score] | |
| 9. Rubric randomization (defensive) | Y/N | [score] | |

Target: each pattern ≥7 quality OR explicitly flagged as "not needed for this harness type" with justification.

### Phase 2 — Pre-Load Design

For each missing or weak pattern, design the explicit affordance.

#### Pattern 1 — Spot-Checking

**Affordance**:
```yaml
benchmark_config:
  mode_selection:
    default: 'spot'
    escalation_rule: '2 consecutive spot passes → full benchmark'
    spot_task_count: 3
    full_task_count: 20
  
  spot_selection:
    method: 'rotating'  # rotating | random | stratified
    coverage_floor: 0.2  # ensure 20% of tasks sampled over last N cycles
```

Integration: meta-agent respects `mode_selection.default` on small diffs, escalates per rule.

#### Pattern 2 — Forced Verification

**Affordance**: modify task-agent system prompt with mandatory section:

```
## Pre-Submission Verification

Before declaring your output complete, perform this verification:

1. Re-read the spec for this task
2. For each explicit requirement, check your output meets it. List any gaps.
3. If gaps exist, either fix them OR explicitly state "incomplete: [gap]" in output
4. Only submit after this step

Verification is mandatory. Skipping it is a task failure.
```

#### Pattern 3 — Formatting Validators

**Affordance**: deterministic pre-scorer:

```python
def validate_format(output, spec):
    checks = []
    if spec.expects_json:
        checks.append(json.loads succeed)
    if spec.required_keys:
        checks.append(all required_keys present)
    if spec.length_bounds:
        checks.append(within bounds)
    return all(checks), [failed check reasons]
```

Integration: run before semantic scorer. If fails, retry with format-correction prompt. Only grade outputs that pass.

#### Pattern 4 — Progressive Disclosure

**Affordance**:
```python
def handle_tool_output(output, context_remaining):
    if len(output) > 0.2 * context_remaining:
        path = dump_to_file(output, experiment_scoped=True)
        return f"[Large output dumped to {path}. Read file to access full content. Summary: {summary}]"
    return output
```

Integration: middleware between tool call and agent context.

#### Pattern 5 — Sub-Agent Spawning

**Affordance**: pre-built sub-agent registry:

```yaml
sub_agents:
  format_checker:
    role: "Validate output structure against spec"
    model: same_as_parent
    invocation: "@spawn format_checker with output=<output>"
  
  fact_verifier:
    role: "Verify factual claims against provided sources"
    model: same_as_parent
    invocation: "@spawn fact_verifier with claims=<list>"
  
  adversarial_critic:
    role: "Find weaknesses a skeptical reader would identify"
    model: same_as_parent
    invocation: "@spawn adversarial_critic with content=<content>"
```

Spawn threshold: tasks requiring >2 distinct check types.

#### Pattern 6 — Handoff Logic

**Affordance**: structured handoff schema (copy from `references/emergent-behaviors-catalog.md` Pattern 6).

Mandatory fields: `{from_agent, to_agent, payload, context_summary, next_action}`.

#### Pattern 7 — Unit Test Authoring

**Affordance** (optional, for code/structured tasks):

Task-agent prompt includes:
```
For code generation tasks, follow this order:
1. Read the spec
2. Write 3-5 unit tests that encode the spec requirements
3. Implement the solution
4. Run tests, fix until passing
5. Submit code + tests

Submit tests-written even if implementation incomplete.
```

Partial credit scoring: tests_written × 0.3 + tests_passed × 0.7.

#### Pattern 8 — Held-Out Benchmark (Defensive)

**Affordance**:
```yaml
benchmark_config:
  held_out:
    percentage: 0.15  # 15% of tasks held out
    rotation: 'per_cycle'  # rotate which tasks are held out each cycle
    gaming_detection:
      seen_score_minus_held_out_threshold: 1.5
      action_on_flag: 'auto_discard'
```

Critical: held-out tasks must NEVER appear in variant generation context. Data isolation is mandatory (GP-12, contamination prevention).

#### Pattern 9 — Rubric Randomization (Defensive)

**Affordance**:
```yaml
rubric_config:
  phrasings_per_dimension: 5  # minimum
  selection: 'random_per_run'
  variance_check:
    min_runs: 3
    max_variance_threshold: 2.0  # points on 0-10 scale
    action_on_flag: 'rerun_with_new_phrasings'
```

### Phase 3 — Trigger Condition Mapping

For each affordance, document WHEN it fires:

| Affordance | Trigger | Cooldown |
|-----------|---------|----------|
| Spot-check | Default; escalates on 2 passes | — |
| Forced verification | Pre-submission of any task | — |
| Format validator | Pre-scorer, all tasks | — |
| Progressive disclosure | Tool output >20% context | — |
| Sub-agent spawn | Task has >2 check types | — |
| Handoff schema | Any multi-agent flow | — |
| Unit-test authoring | Code/structured output tasks | — |
| Held-out benchmark | Every KEPT candidate | — |
| Rubric randomization | Every scoring run | — |

### Phase 4 — Integration with Trace System

Each affordance must emit trace data for meta-agent consumption:

| Affordance | Trace Field Added |
|-----------|-------------------|
| Spot-check | `benchmark.mode: 'spot' \| 'full'` + tasks evaluated |
| Forced verification | `verification_step` in reasoning_chain |
| Format validator | `format_validation_result` in evaluation |
| Progressive disclosure | `context_dumps: [{path, size}]` |
| Sub-agent spawn | `spawned_sub_agents: [{name, parent_trace_id}]` |
| Handoff | `handoff_chain: [{from, to, timestamp}]` |
| Unit-test | `tests: {written: int, passed: int}` |
| Held-out | `held_out_score` + delta |
| Rubric randomization | `rubric_phrasing_id` per run |

### Phase 5 — Gap Detection

After all 9 patterns pre-loaded, ask: what's still missing?

Observe meta-agent behavior over first 30 experiments:
- What patterns does it invent beyond the 9?
- What failures does it encounter that don't match existing patterns?
- What affordances does it wish existed?

Add to catalog. Update this playbook.

## Content Type Adaptations

| Harness Type | Most Critical Patterns | Can Skip |
|-------------|------------------------|----------|
| Code-gen | 3 (format), 4 (progressive disclosure), 7 (unit-test) | 5 if simple |
| Content workflow | 2 (verification), 3 (format), 9 (rubric randomization) | 7 |
| Research agent | 2 (verification), 5 (fact-verifier sub-agent), 6 (handoff) | 7 |
| Pricing engine | 3 (format), 8 (held-out), 9 (rubric) | 7 |
| Customer service | 2 (verification), 5 (adversarial-critic), 8 (held-out) | 7 |

## Output Requirements

- Pattern inventory scorecard
- Per-pattern affordance spec (for each missing/weak pattern)
- Trigger condition table
- Trace integration field list
- Gap detection monitoring plan
- Document: `deliverables/emergent-affordances-[system].md`

## Quality Gate

- **Safety Monitoring** (0-10): patterns 8 and 9 (defensive) present?
- **Trace Infrastructure Depth** (0-10): affordances emit trace data?
- **Prerequisite Completeness** (0-10): all 9 patterns assessed, not just a subset?

Minimum: 7 on each.

## Anti-Patterns

- ❌ Implementing patterns 1-7 but skipping 8-9 ("defensive is paranoid")
- ❌ Pre-loading without trace integration (invisible affordances)
- ❌ "We'll add these if needed" (they're needed — that's the point)
- ❌ Assuming emergent patterns = good (Pattern 8 counters emergent gaming)

## Hand-off

- Affordances loaded → proceed to `/nate-auto-safety` (WF 06)
