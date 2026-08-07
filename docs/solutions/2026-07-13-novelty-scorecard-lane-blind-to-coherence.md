---
name: novelty-scorecard-lane-blind-to-coherence
problem_signature: "Kallaway Gut-Check scorecard rated two versions of the same post 10/10 while the human ranked them apart — the deciding axis lives outside all five scored components"
domain: content
tags: [kallaway, novelty, scorecard, benchmark, quality-gates, writers-room]
date: 2026-07-13
status: active
session: "085d3918-6379-4389-8d36-a939854e85e6"
---

## Problem

The Kallaway Gut-Check scorecard scored an original post and its rewrite both 10/10, while Farrice ranked them clearly apart. A benchmark of 13 workflows against 2 specimens confirmed the pattern: the skill scores its five components honestly, but the axis that decided the human verdict — body coherence and narrative-loop closure — is not one of the five components. The scorecard is honest inside its lane and blind outside it.

## Root Cause

Component scorecards measure the presence and strength of discrete ingredients (hook, novelty, contrast, proof, payoff). Two pieces can carry identical ingredients while one drops the narrative loop the hook opened, leaving the body flat. Loop integrity is a whole-piece property, so no per-component score can register its absence. A perfect component score therefore says "ingredients present," never "piece works."

## Approach That Worked

1. Ran the 13-workflow × 2-specimen benchmark to isolate where the human/scorecard divergence lives (report: `_active/linkedin/99-archive/kallaway-novelty-benchmark/00-REPORT.md`). Verdict: skill honest, lane-blind.
2. Routed original-vs-rewrite quality calls to the loop-integrity lens instead — `/novelty-to-addictive` caught the rewrite's dropped narrative loop, the exact flatness Farrice felt.
3. Set the routing rule: ceiling-level pieces are never ranked on the novelty scorecard alone; add a loop-integrity or prose/writers-room read before declaring a winner.

## Dead Ends

- Re-scoring with stricter component thresholds — both versions still tied, because the failure is between components, not inside any of them.
- Treating the tie as a scorecard bug to patch — the benchmark showed the five components were scored correctly; adding a sixth ad hoc component would just move the blind spot.

## Verification

Benchmark artifacts on disk: 13 workflows run against both specimens, human ranking as ground truth. `/novelty-to-addictive` independently flagged the rewrite's broken loop, matching the human verdict the scorecard missed. Report at `_active/linkedin/99-archive/kallaway-novelty-benchmark/00-REPORT.md`.

## Weaker-Model Trap

Trusting a clean 10/10 as "better" and shipping the flat rewrite. A perfect component score on two rivals means the scorecard cannot decide between them — escalate to a whole-piece lens, never break the tie by rerunning the same card.

## Pointers

- `skills/kallaway-illusion-of-novelty/references/gut-check-scorecard.md` — the component scorecard (honest, lane-scoped)
- `_active/linkedin/99-archive/kallaway-novelty-benchmark/00-REPORT.md` — benchmark report proving the lane-blindness
- `/novelty-to-addictive` — the loop-integrity lens that caught the dropped loop
