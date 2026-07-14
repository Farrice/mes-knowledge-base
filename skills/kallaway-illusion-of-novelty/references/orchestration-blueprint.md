---
description: The routing diagram + decision gates for /novelty-engine — which of the 13 /novelty-* workflows and cross-skill stacks fire in which phase, the mode logic (SINGLE/CAMPAIGN/BATCH), the closed-loop QA gate rule, and the write-vs-read fan-out posture. The engine's wiring map.
---

# Novelty Engine — Orchestration Blueprint

> How `/novelty-engine` composes the skill. The engine is a CONDUCTOR: it routes by mode and gates on the scorecard; it never blindly runs all 14. This file is its wiring.

## The pipeline (phase → workflow → gate)

```
PHASE 0   Intake & Ground        — capture need/asset/avatar/goal/mode; Path A/B; honesty inventory
            └ stack: kallaway-audience-obsession / mcraney-deep-canvass (avatar)  [GATE: avatar known?]
PHASE 0.5 Research & Ground       — LIVE signal: trend scan → fact/proof harvest → what's-working scan
            └ tools: /hunt-trends · perplexity · research.py · tavily · Apify · recall  (see research-grounding-stack.md)
PHASE 1   Angle                   — /novelty-angles → score → pick (or honor forced angle)
PHASE 2   Build the illusion      — /novelty-reveal → /novelty-contrast → /novelty-urgency → /novelty-proof
            → /novelty-hook → /novelty-forge assembly (canonical ordering + 8-step)   [SINGLE COHERENT AUTHOR]
PHASE 3   Make it stick           — /novelty-to-addictive (close loops, kill dead air)        [DO NOT SKIP]
PHASE 4   Voice & delivery        — kallaway-word-mastery: /tone-calibration-engine · /rhythm-rewrite · /believability-audit
PHASE 5   Protect                 — /novelty-protect (mascot scrub + town-crier scrub)
PHASE 6   QA GATE (closed-loop)   — /novelty-audit (Gut-Check scorecard) + honesty/verification gate   [GATE]
PHASE 7   Scale (CAMPAIGN only)   — /novelty-campaign (atomize across platforms; each leads diff component)
PHASE 8   Calibrate               — /novelty-pattern on REAL data (own winners + Phase 0.5 competitor signal)
```

## Mode logic

| Mode | Phases that fire | Notes |
|---|---|---|
| **SINGLE** | 0 → 0.5 → 1 → 2 → 3 → 4 → 5 → 6 → (8 if data) | One finished asset. Phase 7 skipped. |
| **CAMPAIGN** | 0 → 0.5 → 1 → 2 → 3 → 4 → 5 → 6 → **7** → 8 | Phase 6 validates the spine asset, then Phase 7 atomizes; each atomized asset re-runs ≥ Phases 5–6. |
| **BATCH** | 0 → 0.5 → 1 (top N angles) → [2–6 per variant] → 8 | N variants, ONE dimension varied across them for clean testing. |

## The QA gate decision rule (Phase 6)

```
score = /novelty-audit Gut-Check (0–2 per component, /10)
integrity = Illusion Integrity (PASS/FAIL)

IF score >= 9 AND integrity == PASS AND honesty-gate clean:
    → SHIP
ELSE:
    → route the SINGLE weakest component back to its repair workflow
      (reveal / contrast / urgency / proof / protect), apply ONE fix, re-audit
    → cap at 2 repair cycles; if still failing, surface the blocker to the user
      (never force a fabricated component to hit the number)
```
Reminder: an honest urgency skip scores 1/2 → a piece with no real window honestly caps at **9/10**, and that ships. Only *fake* urgency scores 0.

## Fan-out posture (write vs read) — the no-sandwich rule

| Phase | Posture | Why |
|---|---|---|
| 0.5 Research | **PARALLEL (read-heavy)** | Trend / fact / competitor scans are independent reads. |
| 1 Angle | PARALLEL ok (divergent ideation) | Angle mining is read/ideation. |
| 2 Build body | **SEQUENTIAL — ONE author** | Write-heavy. Stitched multi-author bodies test flat (the no-sandwich law). One coherent voice writes the body; the granular workflows supply ingredients, not fragments. |
| 3–5 Refine | SEQUENTIAL — same author | Retention/delivery/protect are rewrites of one voice; keep one hand. |
| 6 QA gate | **PARALLEL (read-only diagnosis)** | Scorecard / coherence / fact-voice each DIAGNOSE; they return findings, not rewrites. |
| 7 Scale | SEQUENTIAL by default | Each atomized asset is a write; parallel writes diverge in voice. |

## Cross-skill stack map (what the engine reaches for, when)

| Phase | Stack | For |
|---|---|---|
| 0 | kallaway-audience-obsession · mcraney-deep-canvass · ICP | held belief + wanted outcome (Contrast + Proof inputs) |
| 0.5 / 8 | research-grounding-stack.md tools | live trend + verified facts + winner signal |
| 3 | kallaway-addictive-storytelling (`/addiction-loop-architect`) | retention / loop closure |
| 4 | kallaway-word-mastery | whisper register, rhythm, AI-tell scrub |
| 7 | /platform-adapt · /atomize · /content-series | multi-platform scale |

## Honesty spine (always on, every phase)
The illusion is of NOVELTY only. Facts, urgency windows, and proof are REAL and sourced (labeled VERIFIED/LIKELY/UNCONFIRMED at harvest in Phase 0.5). No fabricated fact, no bolted-on urgency, no invented proof — automatic fail regardless of the novelty score. Unpermissioned real-person anecdotes are flagged for Chain Step 5.5, never auto-"improved" into a sharper mimic.
