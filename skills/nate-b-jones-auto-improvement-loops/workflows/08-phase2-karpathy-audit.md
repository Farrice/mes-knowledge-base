---
description: META workflow — applies this skill to Antigravity's Phase 2 evolution system. Diagnostic-only prescription (no code execution) of upgrades against all 18 Karpathy patterns.
---

# Phase 2 Karpathy Audit (META)

> Load `genius.md` first. This workflow is the skill applied to THIS system. It audits Antigravity's Phase 2 (Skill Evolution) against all 18 Karpathy patterns and prescribes concrete upgrades — without executing them.

## Pre-Flight Gate

- **Read-only operation**. Does NOT modify live Phase 2 files.
- Produces a prescription document. User decides implementation scope.
- Requires read access to: `directives/evolution-direction.md`, `execution/skill_benchmark.py`, `execution/evolution_tracer.py`, `.agent/workflows/skill-evolution.md`, `.agent/workflows/harness-evolve.md`, recent Performance Log entries.

## When to Use

- Periodically (quarterly) to level up Phase 2 with new insights
- After reading a new frontier post on auto-research/auto-agent
- When Phase 2 hits a plateau (repeated DISCARDs, stalling evolution)
- When adding new failure modes (e.g., metric gaming suspected)

## Skill Acquisition

Load: `genius.md` (all 18 patterns), `references/antigravity-phase2-map.md` (pre-built pattern-to-infra map), `references/emergent-behaviors-catalog.md`, `references/karpathy-loop-quotes.md`

## Input Required

- Current state of Antigravity Phase 2 files (will be read during execution)
- Recent Performance Log entries (sampling for pattern analysis)
- `.claude/plans/` or `directives/` references for prior Phase 2 design intent

## Execution

### Phase 1 — System State Read

Read and summarize current state of:

1. `directives/evolution-direction.md`
   - Current priorities
   - Karpathy Triplet header status (present? explicit?)
   - Constraints list
   - Evolution history table (recent entries)

2. `execution/skill_benchmark.py`
   - Benchmark task structure
   - Scoring dimensions
   - Time budget
   - Held-out / rubric randomization present?

3. `execution/evolution_tracer.py` (if exists)
   - Trace schema depth
   - Score-only or reasoning-trajectory logging?
   - Storage + retrieval

4. `.agent/workflows/skill-evolution.md`
   - Loop mechanism
   - Meta/task split explicit?
   - Human gates defined?
   - Emergent affordances pre-loaded?

5. `.agent/workflows/harness-evolve.md`
   - Harness-specific vs general skill loop
   - How differs from skill-evolution

6. Recent Performance Log entries (last 30)
   - KEEP rate, DISCARD rate
   - Score improvement distribution
   - Any regression signals
   - Any emergent patterns observable

### Phase 2 — 18-Pattern Audit

For each pattern, score 0-10 and write a specific finding:

| # | Pattern | Score | Finding | Gap |
|---|---------|-------|---------|-----|
| GP-1 | Karpathy Triplet | [0-10] | [what exists, what's missing] | [specific] |
| GP-2 | Iteration rate | [0-10] | [current throughput observation] | [target delta] |
| GP-3 | Auto-research vs Auto-agent | [0-10] | [coverage assessment] | [scope clarity] |
| GP-4 | Meta/Task split | [0-10] | [explicit or implicit?] | [document gap] |
| GP-5 | Model empathy | [0-10] | [same-model pairing?] | [constraint lock-in] |
| GP-6 | Traces over scores | [0-10] | [trace schema depth] | **[likely primary gap]** |
| GP-7 | Emergent behaviors | [0-10] | [pre-loaded affordances?] | [catalog gap] |
| GP-8 | Program.md | [0-10] | [evolution-direction.md as analog] | [structure gap if any] |
| GP-9 | Local hard takeoff | [0-10] | [trajectory observation] | [N/A descriptive] |
| GP-10 | Prerequisites | [0-10] | [5-layer check] | [layer gap if any] |
| GP-11 | Small team | [0-10] | [single operator] | [N/A already optimal] |
| GP-12 | Safety modes | [0-10] | [which of 4 monitored?] | **[held-out, regression, isolation, canary]** |
| GP-13 | Outcome vs activity | [0-10] | [composite score correlation] | [revenue-tracker link status] |
| GP-14 | Concentrated judgment | [0-10] | [human gates] | [preservation check] |
| GP-15 | Labs vs open source | N/A | descriptive only | — |
| GP-16 | Earn-the-right | [0-10] | [customer-facing avoided?] | [scope discipline] |
| GP-17 | Auditability | [0-10] | [git commits + logs] | [trace archive depth] |
| GP-18 | Reddit proof point | N/A | descriptive only | — |

### Phase 3 — Gap Severity Classification

For each gap identified:

| Severity | Criteria |
|----------|----------|
| CRITICAL | Pattern score <4; system failing without this |
| HIGH | Pattern score 4-6; material upgrade would improve results meaningfully |
| MEDIUM | Pattern score 6-8; refinement opportunity |
| LOW | Pattern score >8; minor polish |

Focus prescriptive effort on CRITICAL + HIGH.

### Phase 4 — Prescriptive Upgrades

For each HIGH or CRITICAL gap, produce:

```markdown
### Upgrade: [Pattern Name]

**Current state**: [what Phase 2 does today]
**Gap**: [what's missing against Nate's pattern]
**Prescribed change**: [specific modification]
**Where it goes**: [file path(s)]
**Effort estimate**: [hours/days]
**Dependencies**: [what must exist first]
**Risk**: [what could go wrong]
**Validation**: [how to know it worked]
**Advisory note**: This is advisory — the user decides whether to implement.
```

Sequence upgrades by:
1. CRITICAL gaps first
2. Within severity, dependency order (foundations before refinements)
3. Low-risk upgrades before high-risk

### Phase 5 — Emergent Behavior Inventory

Sample 20-30 recent Phase 2 cycles. Ask:

- What patterns does the system exhibit that weren't in the original workflow spec?
- Are any of these the 7 emergent behaviors from the catalog (spot-checking, forced verification, etc.)?
- Are any of these NEW emergent patterns not in the catalog?

Document findings. Update `references/emergent-behaviors-catalog.md` if new patterns emerge.

### Phase 6 — Karpathy Triplet Proposal (Light Path C)

Specific proposal for `directives/evolution-direction.md`:

```markdown
## The Karpathy Triplet (for this system)

**Editable Surface**: Single workflow file per cycle (one `.md` file in `skills/<skill>/workflows/`)

**Metric**: Composite quality score — sum of (Intent Alignment + Expert Standard + Adversarial Resilience + Factual Grounding), each 1-10
- Acceptance threshold: composite ≥7.0 average, no single dimension <6
- Evaluation method: benchmark task run via `skill_benchmark.py`

**Time Budget**: 10 minutes per benchmark run; maximum 3 consecutive cycles per skill before human review

**Minimalism Rationale**: Constraining evolution to one file per cycle (per Karpathy's original auto-research architecture) is deliberate. The agent can read the entire workflow in one pass, understand full context, and evaluate changes in minutes. Multi-file changes would fragment the search space and reduce interpretability.
```

Advisory: this is a proposed addition to evolution-direction.md header. User decides whether to add.

### Phase 7 — Produce Prescription Document

Final deliverable:

```markdown
# Antigravity Phase 2 Karpathy Audit — [Date]

## Executive Summary
[1 paragraph: overall state, top 3 gaps, recommended priority actions]

## System State Snapshot
[Summaries of all 6 inputs from Phase 1]

## 18-Pattern Audit Scorecard
[Full table with scores, findings, gaps]

## Gap Severity Classification
[Critical, High, Medium, Low lists]

## Prescribed Upgrades (in implementation order)
[One block per upgrade, Phase 4 template]

## Emergent Behavior Inventory
[Patterns observed, catalog updates]

## Karpathy Triplet Proposal
[Light Path C: header addition for evolution-direction.md]

## Implementation Decision Matrix

| Upgrade | Severity | Effort | Expected Impact | User Decision |
|---------|----------|--------|-----------------|---------------|
| [...] | CRITICAL | 4 hrs | +1.0 avg composite | [YES/NO/LATER] |

## Next Steps
[What the user should do, in order]

## Re-Audit Schedule
[Recommend next audit cadence]
```

Location: `deliverables/phase2-karpathy-audit-[YYYY-MM-DD].md`

## Output Requirements

- Full prescription document (Phase 7 structure)
- Scorecard (all 18 patterns)
- Prescribed upgrades block (CRITICAL + HIGH only)
- Karpathy Triplet proposal (if not present)
- Decision matrix for user review
- NO code changes. NO file modifications to live system.

## Quality Gate

- **Prerequisite Completeness** (0-10): all 18 patterns audited with specific findings?
- **Judgment Leverage** (0-10): prescriptions specific enough for user to decide implementation?
- **Safety Monitoring** (0-10): 4-mode safety gaps specifically named?

Minimum: 7 on each.

## Anti-Patterns

- ❌ Making code changes to live system (this workflow is advisory only)
- ❌ Generic recommendations ("improve traces") — must be specific
- ❌ Prescribing upgrades without effort estimates
- ❌ Skipping emergent behavior inventory ("nothing to catalog")
- ❌ Only auditing patterns where Phase 2 is weak (audit all 18 for completeness)

## Hand-off

- Prescription produced → user reviews, decides which upgrades to implement
- Upgrades selected → user schedules implementation (this workflow does NOT execute them)
- Post-implementation → re-run this workflow in 3 months for delta audit

---

## Integration Note

This workflow is the only one in the skill that READS live Antigravity files. All other workflows are generic (work on any system). This one is specifically scoped to Phase 2 self-application — the "skill applied to its own system" move.

If used for non-Antigravity systems, replace file paths in Phase 1 with the equivalent files in the target system's auto-improvement infrastructure.
