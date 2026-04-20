# Emergent Behaviors Catalog — Patterns Meta-Agents Discover

A living pattern library. When designing a harness, pre-load these as explicit affordances instead of waiting for the meta-agent to rediscover them. Each entry = a specification-debt signal paid down in advance.

Sources: Kevin Goo auto-agent observations (Third Layer, April 2026), Sky Pilot Kubernetes experiment, community Reddit reports.

---

## Pattern 1 — Spot-Checking (Selective Evaluation)

**What the meta-agent invents**: Instead of running the full benchmark suite after every small edit, runs individual tasks to validate whether the edit is worth full evaluation.

**Compute savings**: 70-95% on small-edit cycles.

**Pre-load as**:
- Harness configuration flag: `benchmark_mode: 'spot' | 'full'`
- Heuristic: if variant diff < X tokens, run spot-check first
- Escalation rule: 2 passed spot-checks → run full benchmark

**Trigger condition**: small variant diff, high confidence, early iteration

**Risk**: missing regressions in tasks not spot-checked. Mitigate with rotating spot-check selection.

---

## Pattern 2 — Forced Verification Loops

**What the meta-agent invents**: Task-agent is steered to re-read its own output against the spec before declaring done. Catches format errors, missed requirements, hallucinated facts.

**Impact**: 15-30% reduction in benchmark failures attributable to task-agent sloppiness.

**Pre-load as**:
- Mandatory "verify against spec" step in task-agent prompt
- Output schema validator that blocks submission if spec fields missing
- Self-critique prompt template: "Re-read the spec. Does your output meet every explicit requirement? If no, which ones are missing?"

**Trigger condition**: task-agent about to submit final output

**Risk**: adds latency. Worth it.

---

## Pattern 3 — Formatting Validators

**What the meta-agent invents**: Structural validation (JSON parseability, required keys, format matching) separate from semantic evaluation. Catches superficial failures before expensive semantic scoring runs.

**Impact**: reduces false-negative score signal (task failed due to format, not quality).

**Pre-load as**:
- Pre-scoring format check (cheap)
- If format fails → auto-retry with format-correction prompt
- Only score-grade outputs that pass format

**Trigger condition**: any structured-output task

**Risk**: none — pure cleanup.

---

## Pattern 4 — Progressive Disclosure (Context Overflow Handling)

**What the meta-agent invents**: When results/outputs exceed context window, dumps full content to files and references files by path instead of inlining. Prevents context rot mid-loop.

**Impact**: enables long-running experiments where naive context would overflow.

**Pre-load as**:
- Automatic "dump to file, reference by path" affordance for any tool output >N tokens
- Index file that tracks what's been dumped and where
- Retrieval protocol: "if you need content from path X, read that file"

**Trigger condition**: tool output about to exceed 20% of remaining context

**Risk**: file sprawl if no cleanup. Mitigate with experiment-scoped temp directories.

---

## Pattern 5 — Task-Specific Sub-Agent Spawning

**What the meta-agent invents**: When domain requires specialization, meta-agent spawns a dedicated sub-agent with narrow focus (e.g., "format-checker", "fact-verifier", "reasoning-critic") instead of asking the main task-agent to wear many hats.

**Impact**: cleaner separation, better performance on each specialized check.

**Pre-load as**:
- Sub-agent registry with invocation syntax
- Minimum 3 pre-built sub-agents: format-checker, fact-verifier, adversarial-critic
- Handoff protocol (Pattern 6)

**Trigger condition**: task requires both generation and adversarial checking

**Risk**: coordination overhead if spawned needlessly. Set threshold: only spawn for tasks with >2 distinct check types.

---

## Pattern 6 — Handoff Logic Between Sub-Agents

**What the meta-agent invents**: Explicit handoff protocols between specialized sub-agents (e.g., generator → critic → reviser → scorer). Prevents context loss at transitions.

**Impact**: enables orchestration depth without losing fidelity.

**Pre-load as**:
- Structured handoff schema: `{from_agent, to_agent, payload, context_summary, next_action}`
- Mandatory context-summary step at each handoff
- Audit log of handoff chain

**Trigger condition**: any multi-agent pipeline

**Risk**: bureaucracy. Keep payload schema minimal.

---

## Pattern 7 — Unit Test Authoring Steering

**What the meta-agent invents**: Task-agent writes its own unit tests before generating output. Tests become the scoring gate. Self-graded.

**Impact**: higher first-pass quality, especially on code/structured outputs.

**Pre-load as**:
- Optional "write tests first" mode for code tasks
- Test execution in sandbox before submission
- Scoring partial credit for tests written vs tests passed

**Trigger condition**: task output is code, schema, or verifiable structure

**Risk**: agent writes tests that validate its own mistakes. Mitigate with independent test review.

---

## Pattern 8 — Metric Gaming Detection (Defensive Pattern — Human-Invented, NOT Emergent)

**What we add to counter meta-agent gaming**: Held-out benchmark task the variant has never seen. If variant score on seen-benchmark is significantly higher than held-out, flag as gaming.

**Why not emergent**: meta-agents don't voluntarily design constraints on themselves. This must be engineered.

**Pre-load as**:
- 10-20% of benchmark tasks held out, rotated between cycles
- Score delta threshold (e.g., seen-score > held-out + 1.5 = gaming flag)
- Gaming-flagged variants auto-DISCARDED even if they pass threshold on seen tasks

**Trigger condition**: every KEPT candidate

**Risk**: over-conservative rejection. Tune delta threshold empirically.

---

## Pattern 9 — Overfitting-to-Rubric Detection (Defensive)

**What we add**: Randomize rubric wording across benchmark runs. If variant performs well only on specific rubric phrasing, it's overfitting to words not meaning.

**Why not emergent**: same reason as Pattern 8 — meta-agents don't self-handicap.

**Pre-load as**:
- 3-5 rubric phrasings per scoring dimension
- Random selection per run
- Score variance across phrasings flagged if > threshold

**Trigger condition**: rubric-based scoring systems

**Risk**: may introduce noise. Use ≥3 runs per variant.

---

## Catalog Maintenance

**When to update this file**:
- New emergent behavior observed in a production meta-agent (ours or others)
- New defensive pattern added to counter a discovered failure mode
- Community report of a new pattern worth pre-loading

**Format for new entry**: match the 7 existing templates (What it invents / Impact / Pre-load as / Trigger / Risk).

**Current total**: 7 emergent + 2 defensive = 9 patterns.
