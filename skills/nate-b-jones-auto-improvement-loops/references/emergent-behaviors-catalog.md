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

## Pattern 10 — Additive-Non-Blocking Audit Layering (Defensive — Human-Invented)

**What we add**: New audit layers (regression suite, cascade detector) surface signals but never auto-revert KEPT cycles. The ratchet stays forward; audits gate the *next* cycle, not the current one.

**Why this matters**: Auto-reverting on audit failure is attractive in theory but dangerous in practice. Audits on first implementation are under-calibrated — false positives would undo legitimate progress. The additive-non-blocking stance buys calibration time without sacrificing safety.

**Impact**: deployment risk drops to near-zero; audits can ship before their thresholds are battle-tested.

**Pre-load as**:
- All new audit layers default to `non_blocking=True` on first ship
- Flag surfaces via `flag: bool` in result JSON; workflow surfaces to user in final report
- Escalation to blocking only after N cycles of calibration + user approval
- Mirror audit result into v3 trace store regardless of blocking status, so signals feed the Karpathy search set even when non-blocking

**Trigger condition**: any new audit layer added to an already-live loop

**Risk**: tolerates detected regressions for 1+ cycle before human intervention. Mitigate with mandatory final-report surfacing.

**Observed in**: Antigravity Phase 2 cascade audit (Upgrade 5, 2026-04-20) and regression audit (Upgrade 3, 2026-04-20).

---

## Pattern 11 — Proxy-from-Log Fallback (Defensive — Human-Invented)

**What we add**: Audits that notionally require live task execution (golden-set regression) instead fall back to rolling averages of the same domain's recent Performance Log entries. Scoring is tagged `scoring_method: "proxy_from_log"` vs `"manual"` so the downstream reader knows fidelity.

**Why this matters**: Live execution is slow + expensive + often unavailable. But proxy signal from recent work is usually sufficient for the regression question "has this domain's quality drifted?" — and the proxy is free.

**Impact**: enables continuous silent-degradation monitoring without per-cycle execution cost. Proxy can be upgraded to manual scoring selectively when a regression signal fires.

**Pre-load as**:
- Every metric layer accepts a `current_score: float | None` slot that can be filled by proxy OR manual
- Metadata tag (`scoring_method`) is mandatory on every scored entry
- Manual-score merge is a first-class CLI command (`log-result --score X`), not an afterthought
- Proxy defaults are silent; only manual scores are trusted for baseline updates

**Trigger condition**: any audit that notionally requires expensive execution

**Risk**: proxy is domain-aggregate, not task-specific — may miss task-level regression that averages out. Mitigate by flagging any PASS with `scoring_method: "proxy_from_log"` as provisional until validated.

**Observed in**: Antigravity Phase 2 regression suite (Upgrade 3, 2026-04-20).

---

## Pattern 12 — Relationship-Weighted Downstream Sampling (Defensive — Human-Invented)

**What we add**: Cross-skill cascade audits don't sample uniformly. They rank candidate downstream skills by weighted confidence across 4 relationship types (same-expert, shared-refs, stacking-declared, pattern-transfer) and sample the top N. High-confidence candidates get checked first because they have the highest prior probability of being affected.

**Why this matters**: Uniform sampling across 200+ skills is computationally expensive and signal-poor. Weighted sampling focuses the audit on the skills most likely to have moved.

**Impact**: enables cascade detection at low cost; 3-skill sample captures 80%+ of realistic cascade risk.

**Pre-load as**:
- Relationship taxonomy with explicit weights (same-expert 3.0, shared-refs 2.0/overlap, stacking 2.5, pattern-transfer 1.5)
- Each flagged regression carries its `reasons` (which relationships drove it onto the sample list), so the user can diagnose *why* it was checked
- Graph is cached (`cascade_graph.json`) and regenerated on demand
- Weights are tunable via code constants, not hardcoded logic

**Trigger condition**: any KEEP operation in a multi-skill loop

**Risk**: a genuine cascade into a low-confidence downstream skill will be missed. Mitigate with occasional full-sweep audits (sample_size = all-downstream) at longer cadence.

**Observed in**: Antigravity Phase 2 cascade detector (Upgrade 5, 2026-04-20).

---

## Catalog Maintenance

**When to update this file**:
- New emergent behavior observed in a production meta-agent (ours or others)
- New defensive pattern added to counter a discovered failure mode
- Community report of a new pattern worth pre-loading

**Format for new entry**: match the 9 existing templates (What it invents / Impact / Pre-load as / Trigger / Risk).

**Current total**: 7 emergent + 2 defensive = 9 patterns.
