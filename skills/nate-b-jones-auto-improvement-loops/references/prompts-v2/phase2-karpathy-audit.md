---
name: "Nate B Jones — Phase 2 Karpathy Audit (META)"
source_prompt: born-v2
skill: nate-b-jones-auto-improvement-loops
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are applying the full Karpathy-pattern lens Nate B Jones developed to Antigravity's own Phase 2 (Skill Evolution) system — the "skill applied to its own system" move. This is a **read-only, advisory** workflow: it produces a prescription document and makes no code changes to the live system. The user decides implementation scope. This is the only workflow in the skill that reads live Antigravity files directly; if adapted for a non-Antigravity system, replace the file paths in Phase 1 with that system's equivalents.

## Input Required

- **[LIVE SYSTEM STATE]** — read access to `directives/evolution-direction.md`, `execution/skill_benchmark.py`, `execution/evolution_tracer.py` (if it exists), `.agent/workflows/skill-evolution.md`, `.agent/workflows/harness-evolve.md`
- **[PERFORMANCE LOG SAMPLE]** — the last 30 Performance Log entries
- **[PRIOR DESIGN INTENT]** — any `.claude/plans/` or `directives/` references documenting the original Phase 2 design intent

## Execution Protocol

### Phase 1 — System State Read
Read and summarize: (1) `directives/evolution-direction.md` — current priorities, whether a Karpathy Triplet header is present and explicit, the constraints list, the evolution history table's recent entries; (2) `execution/skill_benchmark.py` — benchmark task structure, scoring dimensions, time budget, whether held-out/rubric randomization exist; (3) `execution/evolution_tracer.py` if present — trace schema depth, score-only vs reasoning-trajectory logging, storage + retrieval; (4) `.agent/workflows/skill-evolution.md` — loop mechanism, whether the meta/task split is explicit, whether human gates are defined, whether emergent affordances are pre-loaded; (5) `.agent/workflows/harness-evolve.md` — how this harness-specific loop differs from the general skill-evolution loop; (6) the last 30 Performance Log entries — KEEP rate, DISCARD rate, score improvement distribution, any regression signals, any observable emergent patterns.

### Phase 2 — 18-Pattern Audit
Score every one of the 18 genius patterns 0-10 (GP-15 and GP-18 are descriptive/N/A — Labs-vs-open-source scale claim and the Reddit proof point respectively — score the other 16) with a specific finding and gap for each: GP-1 Karpathy Triplet (what exists/missing); GP-2 iteration rate (current throughput observation, target delta); GP-3 auto-research vs auto-agent (coverage assessment, scope clarity); GP-4 meta/task split (explicit or implicit? document gap); GP-5 model empathy (same-model pairing confirmed? constraint lock-in); GP-6 traces over scores (trace schema depth — flag as likely primary gap unless proven otherwise); GP-7 emergent behaviors (pre-loaded affordances present? catalog gap); GP-8 program.md (evolution-direction.md as the analog — structure gap if any); GP-9 local hard takeoff (trajectory observation, descriptive); GP-10 prerequisites (5-layer check, layer gap if any); GP-11 small team (single-operator context — likely already optimal, note explicitly); GP-12 safety modes (which of the 4 are actually monitored — flag held-out, regression, isolation, canary as the likely gap set); GP-13 outcome vs activity (composite score correlation, revenue-tracker link status); GP-14 concentrated judgment (human gates preservation check); GP-16 earn-the-right (is customer-facing avoided, scope discipline); GP-17 auditability (git commits + logs, trace archive depth).

### Phase 3 — Gap Severity Classification
Classify every gap: CRITICAL (score <4; system failing without this); HIGH (score 4-6; material upgrade would meaningfully improve results); MEDIUM (score 6-8; refinement opportunity); LOW (score >8; minor polish). Focus prescriptive effort on CRITICAL + HIGH only — do not spend prescription depth on LOW items.

### Phase 4 — Prescriptive Upgrades
For every CRITICAL or HIGH gap, produce a block: current state (what Phase 2 does today), gap (what's missing against the pattern), prescribed change (specific modification, not a vague direction), where it goes (exact file path(s)), effort estimate (hours/days), dependencies (what must exist first), risk (what could go wrong), validation (how to know it worked), and an explicit advisory note that this is advisory only — the user decides whether to implement. Sequence upgrades: CRITICAL first; within a severity tier, dependency order (foundations before refinements); low-risk upgrades before high-risk ones.

### Phase 5 — Emergent Behavior Inventory
Sample 20-30 recent Phase 2 cycles and ask: what patterns does the system exhibit that weren't in the original workflow spec? Do any match the 7 catalogued emergent behaviors (spot-checking, forced verification, etc.)? Are any genuinely new, uncatalogued patterns? Document findings and flag whether `references/emergent-behaviors-catalog.md` needs an update.

### Phase 6 — Karpathy Triplet Proposal (Light Path C)
Draft a specific proposal for `directives/evolution-direction.md`'s header, using this as the reference shape: editable surface = a single workflow file per cycle (one `.md` file in `skills/<skill>/workflows/`); metric = composite quality score, sum of (Intent Alignment + Expert Standard + Adversarial Resilience + Factual Grounding) each 1-10, acceptance threshold composite ≥7.0 average with no single dimension below 6, evaluated via `skill_benchmark.py`; time budget = 10 minutes per benchmark run, maximum 3 consecutive cycles per skill before human review; minimalism rationale = constraining evolution to one file per cycle mirrors Karpathy's original architecture deliberately — the agent can read the entire workflow in one pass, evaluate changes in minutes, and multi-file changes would fragment the search space and reduce interpretability. State explicitly this is a proposed addition — the user decides whether to add it.

### Phase 7 — Produce Prescription Document
Assemble per the Output Skeleton. No code changes, no file modifications to the live system — this workflow only ever produces the prescription.

## Output Contract

- Full prescription document per the structure below, saved as read-only advisory output
- Complete 18-pattern scorecard (16 scored + 2 descriptive/N/A)
- Prescribed upgrades block for CRITICAL + HIGH gaps only, each with effort estimate and advisory note
- Karpathy Triplet proposal for evolution-direction.md, if not already present
- Implementation decision matrix for user review
- Document target: `deliverables/phase2-karpathy-audit-[YYYY-MM-DD].md`
- Hard constraint: zero code changes, zero live-file modifications — this workflow is diagnostic only

## Output Skeleton

```markdown
# Antigravity Phase 2 Karpathy Audit — [Date]

## Executive Summary
[1 paragraph: overall state, top 3 gaps, recommended priority actions]

## System State Snapshot
[summaries of all 6 Phase 1 inputs]

## 18-Pattern Audit Scorecard
| # | Pattern | Score | Finding | Gap |
|---|---------|-------|---------|-----|
[all 18, GP-15/GP-18 marked N/A descriptive]

## Gap Severity Classification
CRITICAL: [...]
HIGH: [...]
MEDIUM: [...]
LOW: [...]

## Prescribed Upgrades (implementation order)
### Upgrade: [Pattern Name]
Current state: [...]
Gap: [...]
Prescribed change: [...]
Where it goes: [file path(s)]
Effort estimate: [...]
Dependencies: [...]
Risk: [...]
Validation: [...]
Advisory note: This is advisory — the user decides whether to implement.
[repeat per CRITICAL/HIGH gap]

## Emergent Behavior Inventory
[patterns observed, catalog update flag]

## Karpathy Triplet Proposal
[Light Path C header addition, or "already present" if it exists]

## Implementation Decision Matrix
| Upgrade | Severity | Effort | Expected Impact | User Decision |
|---------|----------|--------|-----------------|----------------|
[one row per prescribed upgrade]

## Next Steps
[ordered list for the user]

## Re-Audit Schedule
[recommended cadence]
```

## Quality Gate

- Are all 16 scoreable patterns (18 minus GP-15/GP-18) actually scored with a specific finding — not just the patterns where Phase 2 is weak?
- Does every CRITICAL/HIGH upgrade block include an effort estimate and an explicit advisory-only note?
- Is the document confirmed read-only — no code changes, no live-file edits described as already-executed?
- Is the Karpathy Triplet proposal concrete (named file path, named metric formula, named time budget) rather than a generic recommendation to "define a triplet"?
- Does the emergent behavior inventory report an actual sample size (20-30 cycles) rather than asserting findings without a stated sample?

## Deploy When

- Periodic (quarterly) review to level up Phase 2 with new frontier insights
- After encountering a new frontier post on auto-research/auto-agent patterns worth checking against
- Phase 2 has hit a plateau — repeated DISCARDs, stalling evolution
- Suspected new failure mode (e.g., metric gaming) needs a structured diagnostic pass
