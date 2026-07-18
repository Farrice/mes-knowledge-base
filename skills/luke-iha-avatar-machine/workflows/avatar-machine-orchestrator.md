---
description: Skill-side companion to the /avatar-machine cold-start orchestrator. The runbook lives at .agent/workflows/avatar-machine.md.
tier: system
wired: true
---

# Avatar Machine Orchestrator (companion)

The executable runbook is **`.agent/workflows/avatar-machine.md`** (the `/avatar-machine` slash command resolves there). This file is the skill-internal reference.

## What it orchestrates (Phase 0–5)
1. **PHASE 0 — PROJECT STATE** — `anchor_memory init <slug>`.
2. **PHASE 1 — GROUND** — `execution/avatar_manifold_runner.py ground` (deterministic backstop) → `.tmp/copy-engine/deep-research.md` + `voc-pack.md` + MCP enrichment (Playwright FB Ad Library, Recall) + floor check. See `references/research-spine.md`.
3. **PHASE 2 — BUILD MANIFOLD** — 14 stages in 6 dependency batches (B0–B6), Agent-tool fan-out, `anchor_memory` threads state, Gate A per stage. Prose stages stay on the Agent tool (heartbeat guard).
4. **PHASE 3 — AUDIT** — `/manifold-audit`; re-run leverage gaps.
5. **PHASE 4 — COPY** — `/manifold-to-copy --objective "…"` (real invoker, asset→skill chain, Gate B).
6. **PHASE 5 — FINALIZE** — per-artifact `chain_runner.finalize` (Gate C, never batch).

## Dependency DAG
```
B0 build-a-buyer
B1 pain-matrix · specific-language
B2 core-wound · benefit-matrix
B3 resonance-hierarchy · daisy-chain · anti-hero · suffering-archetype
B4 rh-constraints · epiphany-threshold · landmines
B5 dissolution · market-pickup-lines
B6 concatenate + 5-Part Sales Formula Map
```
Critical-path depth 6; ~11/14 stages parallelize within their batch.

## When to use this vs `/avatar-manifold`
- `/avatar-machine` — full cold-start → finished copy, orchestrated fan-out (this).
- `/avatar-manifold` — the intelligence package only, single-context sequential build (still GROUND-wired).

## Output Requirements
- The end-to-end run produces **four** artifacts, in order, never fewer: (1) the Phase 1 GROUND dossier (`.tmp/copy-engine/<slug>/deep-research.md` + `voc-pack.md`), (2) the concatenated 14-stage Avatar Manifold (Phase 2, canonical order per `genius.md`), (3) the `/manifold-audit` gap report (Phase 3), (4) the finished copy artifact(s) named in `--objective` (VSL/ad/sequence, Phase 4) each carrying a per-artifact `chain_runner.finalize` score (Phase 5).
- A run that stops at the Manifold with no Phase 4 copy is only valid when the invoking request explicitly scoped to "intelligence package only" — otherwise it's an incomplete orchestration, not a shorter one.
- Each Phase 2 batch (B0–B6) writes its stage output into the shared `anchor_memory` thread before the next batch starts. A stage that reads a dependency's output before that dependency's batch has completed (e.g., B3 running before B1/B2 land) is a dependency-DAG violation, not a stylistic shortcut.
- If Phase 1 degrades (budget-exhaustion fail-closed to recall-only), every downstream stage that consumed the degraded stream must be flagged `[MODELED]` — never silently upgraded to unflagged fact.

## Quality Gate
- **Gate A** (per Phase-2 stage): the stage's output scores against its matching `genius.md` rubric dimension — dimensionality, Core Wound depth, Identity-layer fidelity, Goldilocks calibration, reframe mechanics, specific language, landmine awareness, or deployability, whichever the stage produces.
- **Gate B** (Phase 4 copy): the invoked downstream copy skill's own quality gate (e.g., `luke-iha-vsl-leads`, `luke-iha-vicious-hooks`) — this orchestrator does not substitute its own bar for the receiving skill's.
- **Gate C** (Phase 5): `chain_runner.finalize` run per artifact, never batched across artifacts. Composite < 7 or any dimension < 6 → retry the weakest section once, then re-finalize.
- **Auto-fail:** skipping Phase 1 GROUND when research tools were available (modeled-by-default instead of modeled-by-necessity); running a Phase 2 stage out of DAG order; delivering the Manifold alone when the objective asked for finished copy; batching Gate C across multiple artifacts instead of scoring each on its own.
