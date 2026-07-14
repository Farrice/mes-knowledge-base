---
description: "/jcin-shot-plan — credit-costed shot plan BEFORE generation: beats table with per-shot mode, refs, surface, and credit estimate; take budgets by shot type; asset-gap list; total + approval line. Advisory layer — the cost-gate hooks still gate actual spend."
---

# Shot Plan (Joey Cinema OS)

Cost Before Generate is a signature move, not bookkeeping: every video prompt carries a declared duration, and every plan carries a credit estimate before anything runs. Joey's real numbers — ~117 credits per 13-second 1080p Seedance generation, 200–300 credits for a simple studio piece, 5,000–6,000 per music video — exist because iteration is filming takes, and takes are the budget. The skills' whole economic claim is that prep cuts trial-and-error from 8–10 takes to 2–3. This workflow puts that math on the table before the first credit moves.

## Pre-Flight Gate

> **🔒 Gate — assets and runtime before beats.** Two checks, both hard:
> 1. **Asset inventory.** Every named subject in the planned shots — character, product, vehicle, environment — either has a locked canonical reference or goes on the asset-gap list (Step 3). A plan that generates against unlocked assets is a plan to re-roll everything.
> 2. **Runtime is asked, never assumed** (worldbuilder's locked rule). Every beat gets a declared duration; no duration, no cost line, no plan.
> Compliance note: this plan is ADVISORY. The deterministic hooks (`cost_gate_hook.py`, `higgsfield_budget_guard.py`, `fal_budget_guard.py`) gate actual spend at execution and their verdicts win. A denied gate = surface to Farrice, never retry around it.

## Skill Acquisition

1. `skills/joey-cinema-os/genius.md` — patterns 21–22 (credit economy, confirmation gates), § Hidden Knowledge (economics block), § System Fit (surfaces + gates)
2. `skills/cinema-worldbuilder-pro/SKILL.md` § **MODE-SELECT TABLE** (M1–M5), § **RUNTIME & PER-SHOT TIMING** (shot complexity guidance), § **CUTS & TIMING PRECISION SCALE**
3. `skills/banana-pro-director/SKILL.md` § THE WORKFLOW — STRICT ORDER (which still modes feed which assets)
4. `skills/joey-cinema-os/SKILL.md` § Surfaces & Gates (Higgsfield @tags vs Fal prose; the Fal hard block)

## Input Required

- The mission: what's being made (15s story, ad set, music video, launch set), for whom, by when
- The beat list or story spine — even rough; the plan sharpens it
- Current asset library state: which characters/products/plates are already locked
- Target resolution and duration expectations (native resolution is a generation-time decision — 4K native ≠ 720p upscaled)
- Any wallet/budget ceiling Farrice has named for this mission

## Execution

### Step 1 — Beats table
One row per shot. This table IS the deliverable's spine.

| # | Shot (one line, observable action) | Duration | Cinema mode | Refs needed (@tags) | Surface | Credits est. | Takes budgeted | Est. total |
|---|---|---|---|---|---|---|---|---|
| 1 | | Xs | M1–M5 | | Higgsfield / Fal | | | |

Rules per row:
- **Duration** follows the worldbuilder complexity guidance: 4–8s one action, 8–12s action + reveal, 12–15s only for 2–3 timestamped beats with hard cuts; anything denser splits into two rows
- **Mode** from the § MODE-SELECT TABLE; one mode dominant per shot
- **Refs needed** lists every canonical + plate the shot consumes — canonical-over-plate, one tag per named subject
- **Surface**: Seedance video and @tag grammar → Higgsfield. **Fal seedance-1080p is HARD-BLOCKED by `fal_budget_guard.py` — never plan a 1080p Seedance shot onto Fal.** Fal rows are stills-lane only (fantastic-posters class) and carry prose-descriptor prompts, no tags.
- **Credits est.**: anchor on **~117 credits / 13s at 1080p Seedance (Higgsfield)** and scale linearly by duration (~9 cr/s); mark estimates for other models/resolutions as ESTIMATE and check `models_explore`/current pricing rather than inventing a number. Stills (Banana Pro / Soul Cinema) are cheap relative to video but count takes anyway; GPT-2 rows get flagged credit-heavy.

### Step 2 — Take budgets by shot type
Per-take cost × takes is the real number; a plan that assumes one-shot magic is fiction.

| Shot type | Takes to budget |
|---|---|
| Standard shot, all assets locked | 2–3 |
| New scene plate / first use of a locked pairing | 3–5 |
| Hardest new asset (complex garment, novel product, first face lock of a build) | up to ~50 generations, named knowingly — this budget belongs to the asset lock, not the shot |
| Any shot still failing at take 3 | stop — `/jcin-prompt-doctor` before take 4 |

Sanity anchors from production: simple studio character piece ≈ 200–300 credits all-in; full music video ≈ 5,000–6,000. If the plan's total lands wildly off these anchors for a comparable scope, re-check the math before presenting it.

### Step 3 — Asset-gap list
Everything the beats table needs that doesn't exist yet, with the workflow that builds it and its own take budget:

```
ASSET GAPS (lock these BEFORE any beat generates):
- [subject] — missing [face lock / outfit base / turnaround / plate / palette sheet]
  → build via [/jcin-character-lock | /jcin-outfit-engine | /jcin-product-lock | /jcin-scene-shot | /jcin-world-canon]
  → takes budgeted: [n]  → est. credits: [n]
```

Asset-lock credits are spent once and amortize across every future shot — say that in the plan, because it's why the upfront number looks big and is still the cheap path.

### Step 4 — Total + approval line
```
SHOT PLAN TOTAL
  Asset locks:      [n] credits ([n] generations)
  Shots (all takes): [n] credits ([n] generations)
  Contingency (+15% on video rows): [n]
  ─────────────────────────────
  TOTAL ESTIMATE:   [n] credits   vs wallet/ceiling: [state it]

  APPROVAL: generate nothing until Farrice approves this total.
  The cost-gate hooks fire per-execution regardless of this approval.
```

Present the plan, wait for the yes. Minor re-plans after approval (a duration tweak, one added take) update the total inline without re-ceremony — re-confirming on tiny deltas creates friction. New shots, new assets, or a >20% total move re-run the approval line.

## Content Type Adaptations

| Mission | Adaptation |
|---|---|
| 15s / 3-shot micro-story | Usually ONE Seedance prompt with timestamped beats — one video row, 2–3 takes, plus whatever asset gaps exist; grab → payoff → unresolved questions shapes the beats |
| Ad set (static + video, Dara/Omar stacks) | Two lanes in one table: stills rows (variants are cheap, plan more takes) + video rows; product lock amortizes across every row — front-load it |
| Music video | Plan per scene-cluster, not per video; 5–6k credit anchor; wardrobe changes each add an outfit-lock row; present as phased approvals (assets → scene cluster 1 → …) |
| Product launch set (MyBPM / TrendScale) | Hero + turnaround locks first, context plates second, video last; most of the budget is the ~50-gen hard-asset line — name it in the first breath, not the fine print |
| Client listing video (Jen) | Plates dominate, few or no character locks; short M1/M5 shots; budget stays in the low hundreds — if it doesn't, the plan is over-shooting the format |

## Output Requirements

- The beats table, complete — every row carries duration, mode, refs, surface, credit estimate, and take budget; no TBD durations
- Asset-gap list with build-workflow routing and its own subtotal
- Total block with contingency, ceiling comparison, and the explicit approval line
- Fal hard-block respected in the surface column; no Fal 1080p Seedance row exists anywhere
- Non-anchored price claims labeled ESTIMATE — the only verbatim-source number is the ~117cr/13s 1080p Seedance anchor and the 200–300 / 5–6k production anchors

Execution prompt: references/prompts-v2/shot-plan.md — honor its Output Contract.

## Quality Gate

> **🛡️ Anchor before shipping** — `genius.md § Quality Rubric` (Credit economy row) + § Anti-Patterns ("generating before the shot plan is costed").
- Every shot has a declared duration and the per-shot timing sums match any multi-beat runtime claims
- Take budgets are honest: 2–3 standard, hard assets at ~50 named knowingly — no silent one-take assumptions
- Every named subject in every row maps to a locked asset or a gap-list entry; zero orphan subjects
- The plan spends nothing itself and says so; the approval line is present and unambiguous
- A shot the format doesn't need (a 15s ask planned like a music video) got challenged, not costed
- Totals sanity-checked against the production anchors; a 10× deviation is explained or fixed

## Common Pitfalls
- **Costing shots against unlocked assets.** The beats table looks complete, the totals look sane, and every number is fiction because half the subjects will re-roll identity on every take. Recovery: the asset-gap list comes first; gap-list credits belong in the total.
- **Assuming runtime.** "About 10 seconds" becomes 13 becomes a different credit line and a different prompt structure. Recovery: the worldbuilder's rule is the plan's rule — ask, never default.
- **Planning Fal for Seedance 1080p.** The row costs out fine on paper and hard-blocks at execution. Recovery: surface column audited against the gate reality before presenting; 1080p Seedance lives on Higgsfield, period.
- **One-take line items.** A plan with takes=1 everywhere is a wish. Recovery: 2–3 standard, more for first pairings, ~50 for the hardest new asset — the honest win is fewer takes than unprepped, never zero.
- **Treating the plan as the gate.** Approval on the plan does not pre-authorize spend; a denied cost-gate at execution is surfaced, not retried. Recovery: the compliance note rides in the deliverable, and the hooks' verdicts win.
- **Letting scope creep re-total silently.** Three added shots later the approved number is 40% stale. Recovery: >20% total movement or any new asset re-runs the approval line.
