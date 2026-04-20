---
description: Phase 2 Karpathy Audit — apply this skill to Antigravity's own Phase 2 evolution system; prescribes concrete upgrades (advisory only, no execution)
---

# /nate-auto-phase2 — Phase 2 Karpathy Audit (META)

The skill applied to Antigravity itself. Read-only audit of Phase 2 infrastructure against all 18 Karpathy patterns. Produces a prescription document. Does NOT modify live files.

## Workflow

### Step 1: Load Expert Context
Read `skills/nate-b-jones-auto-improvement-loops/SKILL.md` and `skills/nate-b-jones-auto-improvement-loops/genius.md`.

Read `skills/nate-b-jones-auto-improvement-loops/workflows/08-phase2-karpathy-audit.md` for the specific workflow.

Read pre-built map: `skills/nate-b-jones-auto-improvement-loops/references/antigravity-phase2-map.md`.

### Step 2: Read System State (All Read-Only)
Inspect:
1. `directives/evolution-direction.md` — priorities, triplet header, constraints, history
2. `execution/skill_benchmark.py` — benchmark tasks, scoring, time budget, held-out
3. `execution/evolution_tracer.py` — trace schema depth
4. `.agent/workflows/skill-evolution.md` — loop mechanism, meta/task split
5. `.agent/workflows/harness-evolve.md` — harness-specific variant
6. Recent Performance Log entries (last 30) — KEEP rate, patterns, emergent behaviors

### Step 3: Execute the 7-Phase Audit
1. **System State Read** — summaries of all 6 inputs
2. **18-Pattern Audit** — score each pattern 0-10 with finding + gap
3. **Gap Severity Classification** — CRITICAL / HIGH / MEDIUM / LOW
4. **Prescriptive Upgrades** — for CRITICAL + HIGH, specific change + effort estimate
5. **Emergent Behavior Inventory** — sample 20-30 cycles, catalog new patterns
6. **Karpathy Triplet Proposal** — Light Path C header for evolution-direction.md
7. **Prescription Document Production** — full audit doc for user review

### Step 4: Produce Deliverable
- Full prescription document at `deliverables/phase2-karpathy-audit-[YYYY-MM-DD].md`
- 18-pattern scorecard
- Prescribed upgrades (CRITICAL + HIGH)
- Karpathy Triplet proposal
- Decision matrix for user review
- **NO code changes. NO file modifications.**

### Step 5: Quality Gate
Prerequisite Completeness, Judgment Leverage, Safety Monitoring — min 7 each. Specifically: all 18 patterns audited, prescriptions specific enough for implementation decisions.

### Step 6: Hand-off
- Prescription produced → user reviews, decides which upgrades to implement
- Upgrades selected → user schedules implementation separately
- Post-implementation → re-run this workflow in 3 months for delta audit

## Integration Note

This workflow reads LIVE Antigravity files. All other WFs in this skill are generic. This one is specifically scoped to Phase 2 self-application. Advisory only.
