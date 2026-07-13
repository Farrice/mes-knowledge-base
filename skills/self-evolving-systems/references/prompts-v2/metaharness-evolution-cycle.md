---
name: "Self-Evolving Systems — MetaHarness Evolution Cycle"
source_prompt: born-v2
skill: self-evolving-systems
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are running a **MetaHarness propose-evaluate-log-iterate loop** (Yoonho Lee / Andrej Karpathy / Rich Sutton composite frame, sourced from "MetaHarness — End-to-End Optimization of Model Harnesses," arXiv:2603.28052v1, Stanford/MIT/Crafted, plus Karpathy's 2026 "autoresearch" pattern) on a single Antigravity component — a workflow, prompt, retrieval pattern, memory-management routine, or orchestration pattern.

Founding premise: a **6x performance gap** exists between the best and worst harness for the *same* model weights on the *same* task. The harness is not decoration around the model — it is an intelligence layer in its own right. When a workflow underperforms, the reflex to blame the model and reach for a bigger one is the anti-pattern this loop exists to prevent.

This is one cycle: propose a change, evaluate it against real failure cases, log the full trace (not just a score), and decide keep/discard. It is a single-cycle loop — for governing many cycles over time with monotonic-progress enforcement, that is a separate deliverable (Trajectory Ratchet).

## Input Required

- **[EVOLUTION TARGET]** — the specific workflow/prompt/retrieval-logic/memory-routine/orchestration pattern to evolve
- **[EVALUATION METRIC]** — quality gate score, task accuracy, token cost, user satisfaction, or another explicit metric
- **[SEARCH SET]** — the actual failure cases, hard examples, or edge cases this cycle will be evaluated against (never "general examples" — see Execution Protocol Step 2)
- **[ITERATION BUDGET]** — number of iterations planned this cycle (5 for a quick sprint, 10-20 for a full run)
- **[BASELINE]** — the current version of the target and its documented performance on the evaluation metric
- **[SCOPE CONSTRAINTS]** — what the proposer is allowed to change: everything, prompts only, flow only, retrieval only, etc.
- **[FORBIDDEN]** — safety rails, non-negotiable behaviors, or brand-voice constraints the proposer may NOT touch regardless of score gains

## Execution Protocol

### Step 1 — Answer the Decision Framework before proposing anything

Before any change is proposed, answer all seven questions explicitly using the inputs above: target, evaluation metric, search set, iteration count, baseline, scope, and what's forbidden. A cycle that skips this step is optimizing without a defined objective.

### Step 2 — Diagnose harness vs. model (the 6x Lever)

When [BASELINE] performance is weak, do not default to "the model needs to be stronger." Exhaustively examine the harness first: prompt construction, retrieval logic, state management, orchestration sequencing. Only after the harness has been genuinely evolved and still underperforms is a model-tier upgrade the right lever. Upgrading the model to fix a harness-level problem is the named anti-pattern here.

### Step 3 — Debug the skill text before running the full budget (skill text dominates)

Iterating on the instructions given to the proposer has a larger effect on search quality than changing iteration count or population size. Before spending the full [ITERATION BUDGET], run 3-5 short (roughly 3-iteration) cycles specifically to refine the skill/instruction text the proposer will operate under. Do not run a 20-iteration loop against a mediocre instruction set and expect volume to compensate.

### Step 4 — Give the proposer real agency, not a summarized prompt

The proposer must be a coding agent with:
- access to prior harness code — ALL versions, not only the best-performing one
- access to full execution traces (actual prompts sent, actual responses received)
- the ability to navigate and search the artifact store (grep/cat/diff)
- freedom to make local edits OR full rewrites, not a fixed edit shape

Summarizing history into a single fixed prompt and asking "what should change?" discards the diagnostic signal the loop depends on.

### Step 5 — Let it see the failures, not just the wins

Keep ALL prior iterations in the material the proposer can inspect, including low-scoring ones — a poorly-performing prior harness can still contain one buried insight. Showing only top-performing variants biases the search toward local maxima.

### Step 6 — Build the search set from the hardest cases

The [SEARCH SET] must be constructed from examples the current baseline gets wrong, or a genuinely difficult/diverse subset. If the search set is examples the baseline already handles well, evolution has nothing real to optimize.

### Step 7 — Represent the harness as code/structured workflow, not free text

Whatever is being evolved should be represented as executable code or a structured workflow, not arbitrary free-form prompt text. Structured representation gives coding-model proposers a natural regularization bias toward coherent, generalizable solutions rather than brittle one-off heuristics.

### Step 8 — Log traces, not scores

For every iteration, log the actual prompt sent, the actual response received, state updates made, retrieval queries issued, and files accessed — in a queryable format (e.g. JSON). A final score alone ("7/10") strips the information needed to trace a downstream failure back to the harness decision that caused it.

### Step 9 — Lightweight pre-check before full evaluation

Run a cheap validation pass (import/instantiate/call on 2-3 examples) on every proposed candidate before committing it to full evaluation against [SEARCH SET]. This catches malformed or nonfunctional candidates before spending the full evaluation budget on them.

### Step 10 — Keep/discard per iteration, against the seven anti-patterns

For each iteration, explicitly check against these seven failure modes before logging a KEEP:
1. **Score Worship** — optimizing a single number instead of understanding why it moved
2. **Trace Amnesia** — logging only final scores, no execution trace
3. **Success Bias** — showing the proposer only winning variants
4. **Premature Optimization** — running evolution on something that hasn't been manually tuned at all yet
5. **Iteration Inflation** — running far more iterations than the returns justify
6. **Skill Neglect** — under-investing in the proposer's instruction quality (see Step 3)
7. **Monolithic Prompts** — packing everything into one prompt instead of adaptive, navigable access

## Output Contract

An **Evolution Cycle Report** containing: the seven Decision Framework answers, the documented baseline, a per-iteration log (proposed change, mechanism hypothesis, trace summary, evaluation result, keep/discard verdict with reason), the final recommended harness version with its score delta vs. baseline, and an explicit self-check against all seven anti-patterns. Length scales with [ITERATION BUDGET] — one log entry per iteration, no compression of the trace into a summary-only line.

## Output Skeleton

```
## MetaHarness Evolution Cycle Report — [EVOLUTION TARGET]

### Decision Framework
- Target: [...]
- Evaluation metric: [...]
- Search set: [description + why these are the hardest cases]
- Iteration budget: [N]
- Baseline: [version + documented performance]
- Scope constraints: [what the proposer may change]
- Forbidden: [safety rails / non-negotiables]

### Skill-Text Debug Pass (Step 3, if run)
- Prior instruction issues found: [...]
- Instruction revisions made: [...]

### Harness vs. Model Diagnosis (Step 2)
- Verdict: [harness-level / model-level / mixed]
- Evidence: [specific prompt/retrieval/state findings, not a guess]

### Iteration Log
[repeat per iteration]
- Iteration [N]
  - Proposed change: [...]
  - Mechanism hypothesis: [...]
  - Pre-check result: [pass/fail]
  - Trace summary: [prompt sent / response received / state changes / retrieval queries]
  - Evaluation result: [score vs. metric]
  - Anti-pattern check: [any of the 7 triggered? which?]
  - Verdict: [KEEP/DISCARD] — [reason]

### Final Result
- Recommended version: [iteration N or baseline retained]
- Score delta vs. baseline: [+/-]
- Anti-pattern self-check: [pass/fail per anti-pattern, 7 total]
```

## Quality Gate

- Are all seven Decision Framework questions answered explicitly before any proposal is made?
- Is Step 2's harness-vs-model diagnosis present, with evidence, before any model-upgrade language appears?
- Does every iteration log a full trace (prompt/response/state/retrieval), not a score-only line?
- Was the search set built from actual failure cases, and is that stated (not asserted without evidence)?
- Does the final report include an explicit self-check against all seven anti-patterns, not just the ones that happen not to apply?
- If [ITERATION BUDGET] exceeds 5, is there evidence a skill-text debug pass (Step 3) happened before the full run?

## Creative Latitude

The proposer's actual value is in what it notices, not in following this checklist mechanically:

- **Mechanism hypotheses** — the causal "why" behind each proposed change is where genuine insight lives; a hypothesis that just restates the metric name is not a hypothesis.
- **Scope of change** — local edit vs. full rewrite is a live choice per iteration, not a fixed mode; let the evidence in the trace determine which is warranted.
- **Which failures to chase first** — when the search set contains multiple failure classes, prioritizing which one to target first is a judgment call the proposer should make and justify, not something this protocol prescribes.

## Deploy When

- A workflow or skill has been manually tuned but performance has plateaued.
- Quality gate scores consistently land in the 6-7 range.
- The same class of error keeps recurring despite self-annealing fixes.
- Before upgrading to a more expensive model — evolve the harness first and confirm the ceiling is genuinely model-level, not harness-level.
- A periodic (weekly/monthly) optimization sprint is due on a high-value workflow.
