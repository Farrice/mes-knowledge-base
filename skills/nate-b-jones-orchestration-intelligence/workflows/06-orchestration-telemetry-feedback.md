---
description: Build self-optimizing orchestration by embedding telemetry feedback loops that detect coordination inefficiencies and adjust strategy across runs
---

# Orchestration Telemetry Feedback

> Load `genius.md` first. This workflow adds a self-optimizing layer to any DPVI orchestration system — the system instruments its own coordination decisions and improves them across runs.

## When to Use
- Multi-agent system runs repeatedly (content pipelines, research sprints, evolution cycles)
- Orchestration overhead suspected of exceeding coordination value
- Need to detect whether decomposition, parallelization, or verification is creating waste
- Building a system that should get faster and more accurate over time without manual tuning

## Core Insight

DPVI tells you HOW to orchestrate. Telemetry Feedback tells you WHETHER your orchestration choices were good. The Judge currently evaluates task output — but nobody evaluates the Judge's decomposition strategy, the Planner's parallelization decisions, or whether the verification gates are calibrated correctly. This layer closes that gap.

The principle: **Every coordination decision is a hypothesis. Instrument it, measure it, feed it back.**

## Input Required
- **Existing DPVI architecture** (or architecture to be designed — can pair with Workflow 01)
- **Run history** (even 1 prior run provides signal; 5+ enables pattern detection)
- **Optimization target**: Latency? Quality? Token cost? Human review time?

## Execution

### Phase 1 — Instrument Coordination Decisions

For each DPVI stage, define what to measure:

**Decomposition Telemetry:**
| Signal | What It Reveals | Collection Method |
|--------|----------------|-------------------|
| Subtask completion time variance | Whether decomposition granularity is uneven | Timestamp each worker start/finish |
| Worker context utilization | Whether subtasks are too small (wasted overhead) or too large (context exhaustion) | Track token count per worker context |
| Re-decomposition frequency | Whether initial decomposition was too coarse | Count how often Judge triggers re-plan |
| Subtask dependency violations | Whether "independent" tasks actually had hidden dependencies | Log cases where a worker blocks on another worker's output |

**Parallelization Telemetry:**
| Signal | What It Reveals | Collection Method |
|--------|----------------|-------------------|
| Worker idle time | Whether task distribution is imbalanced | Track time between worker assignment and first output |
| Serialization bottlenecks | Whether false dependencies are forcing sequential execution | Flag tasks that wait for predecessors that could run in parallel |
| Redundant computation | Whether isolated workers are duplicating effort | Hash worker outputs, detect >70% overlap |
| Parallelization overhead ratio | Whether coordination cost exceeds parallel speedup | Compare: (sum of worker times) vs. (total wall clock + coordination time) |

**Verification Telemetry:**
| Signal | What It Reveals | Collection Method |
|--------|----------------|-------------------|
| Judge override rate | Whether verification criteria are miscalibrated | Track accept/reject ratio per subtask type |
| False positive rate | Whether Judge accepts substandard work | Sample accepted outputs for post-hoc human review |
| Iteration depth before acceptance | Whether quality bar is too high (diminishing returns) or too low (first-pass acceptance of bad work) | Count iterations per subtask |
| Verification cost as % of total | Whether the verification layer costs more than the value it provides | Track Judge token usage vs. total pipeline usage |

### Phase 2 — Define Efficiency Thresholds

For each signal, set a threshold that triggers adjustment:

**Red flags (auto-trigger investigation):**
- Any worker using >80% of context window = subtask too large
- Any worker completing in <5% of average time = subtask too small or trivially decomposed
- Judge rejecting >60% of first-pass outputs = either workers are poorly specified or verification bar is miscalibrated
- Verification cost >25% of total pipeline cost = Judge layer may exceed value of coordination
- Re-decomposition on >40% of subtasks = initial decomposition strategy is broken

**Yellow flags (log for pattern detection across runs):**
- Completion time variance >3x across parallel workers = load imbalance
- >2 iterations on >30% of subtasks = systematic quality gap
- Worker idle time >20% of total pipeline time = parallelization inefficiency

### Phase 3 — Build the Feedback Loop

The feedback loop operates BETWEEN runs, not during them. This is critical — mid-run adjustments add complexity that violates Principle 7 (Complexity Reduction > Complexity Addition).

**After each run, generate a Coordination Retrospective:**

```
## Coordination Retrospective — Run [N]

### Decomposition Assessment
- Subtasks: [count] | Avg completion time: [X] | Variance: [X]
- Context utilization: [min%-max%] | Re-decompositions: [count]
- Verdict: [WELL-CALIBRATED | TOO-COARSE | TOO-FINE | UNEVEN]

### Parallelization Assessment  
- Workers: [count] | Wall clock: [X] | Sum of worker times: [X]
- Overhead ratio: [X] | Idle time: [X%] | Redundant computation: [Y/N]
- Verdict: [EFFICIENT | BOTTLENECKED | OVER-PARALLELIZED | REDUNDANT]

### Verification Assessment
- Judge cycles: [count] | Override rate: [X%] | Avg iterations: [X]
- Verification cost: [X%] of total
- Verdict: [CALIBRATED | TOO-STRICT | TOO-LOOSE | EXPENSIVE]

### Adjustment Recommendations
1. [Specific change to decomposition/parallelization/verification]
2. [Specific change...]

### Cumulative Trend (Runs 1-N)
- [Pattern detected across multiple runs]
```

**Feed the retrospective into the next run's Planner prompt:**
The Root Planner receives the last 3 Coordination Retrospectives as context. It uses them to adjust decomposition granularity, parallelization strategy, and verification intensity. This is the self-optimization mechanism — not a new agent, but additional context that makes existing agents smarter.

### Phase 4 — Prevent Orchestration Overhead Spiral

The most dangerous failure mode of self-optimizing orchestration: the optimization layer itself becomes the primary cost center. Guard against this with hard constraints:

1. **Telemetry collection must be passive** — timestamps and counters, never additional LLM calls to "analyze" mid-run
2. **Retrospective generation is ONE pass** — a single structured summary, not a multi-round analysis
3. **Adjustment recommendations max 3 per run** — prevents oscillation between strategies
4. **Retrospective context is capped at last 3 runs** — prevents unbounded context growth
5. **If telemetry overhead exceeds 5% of total pipeline cost, strip it back to timestamps only**

The meta-rule: The optimization layer must be cheaper than the cheapest worker in the pipeline. If it isn't, it has become the problem it was designed to solve.

## Output

1. **Telemetry Schema** — what to measure at each DPVI stage, with collection methods
2. **Threshold Configuration** — red/yellow flag definitions calibrated to the specific pipeline
3. **Retrospective Template** — structured format for post-run coordination analysis
4. **Planner Integration Spec** — how retrospectives feed into the next run's planning context
5. **Overhead Budget** — hard limits on telemetry cost as a percentage of total pipeline cost

## Quality Gate

Before finalizing, verify:
- [ ] Every telemetry signal maps to a specific adjustment action (no measurement without purpose)
- [ ] No mid-run adjustment complexity was introduced (feedback is between-run only)
- [ ] The overhead budget is defined and the telemetry layer is demonstrably cheaper than any worker
- [ ] Adjustment recommendations are concrete enough that a Planner could act on them without interpretation
- [ ] The system degrades gracefully — if telemetry fails, the pipeline still runs normally

> **Anti-Pattern Check**: The telemetry layer must NEVER become a second Judge. It evaluates coordination quality, not task output quality. If you find yourself checking whether worker outputs are "good," you've crossed into the Judge's role — strip it back.
