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
