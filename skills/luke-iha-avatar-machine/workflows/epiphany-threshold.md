---
description: Generate below-threshold, over-BS, and Goldilocks-Zone beliefs for a market; calibrate hooks to the 7-9 sweet spot
tier: 2
stacks_with: luke-iha-vicious-hooks, luke-iha-insight-vectors, luke-iha-unaware-ads
---

# Epiphany Threshold Engine

Generates the minimum-viable insight that captures attention without tripping the bullshit detector. Operationalizes the Hegelian dialectic: thesis (obvious) → antithesis (outlandish) → synthesis (Goldilocks).

## Pre-Flight Gate
- Market named.
- Remember: **better to push toward outlandish than obvious.** The shallow end is where attention dies.
- A Goldilocks belief must be *surprising yet self-limiting* (specific exception/factor), not a flat over-BS claim.

## PHASE 0 — GROUND (auto-fires; skip with `--no-ground`)
Per `references/research-spine.md`. Goldilocks calibration needs the market's REAL belief baseline + the REAL "over-BS ceiling" (what's actually circulating), not a guess at what sounds surprising.
- If the dossier exists, read `deep-research.md` for the obvious/accepted beliefs and `voc-pack.md` for live hooks.
- Standalone & not `--no-ground` — route through the ONE grounding chokepoint (reuses a fresh per-market dossier at **$0**; cold-starts paid only on a cache miss):
```bash
// turbo
python3 execution/avatar_manifold_runner.py ground --slug <slug> --market "<market>" --tier deep 2>/dev/null \
  || echo "DEGRADE → mcp__recall__search; calibrate with [MODELED] flags"
```
- Model-side: `mcp__playwright__browser_navigate` to `facebook.com/ads/library` + `browser_snapshot` for live winning hooks; harvest the real belief-spectrum endpoints before calibrating the 7–9 zone.

## Skill Acquisition
Load `references/framework-library.md` § E (the spectrum + 4 categories + believability guardrails). Optionally `source-prompts/epiphany-threshold-prompt.md` to run raw. Load genius.md Pattern 4.

## Execution
1. **10 below-threshold** beliefs (obvious, common — the Boredom Zone). These define the baseline you must escape.
2. **10 over-BS-limit** beliefs (outlandish, unbelievable). These define the ceiling.
3. **10 Goldilocks-Zone** beliefs (7–9) **with reasoning** for each — why it's surprising yet still believable. Use the 4 categories:
   - Inversion & Extremism · Specific Exceptions & Hidden Factors · Reframing the Goal · False Dichotomy & Oversimplification.
4. **Believability check** each Goldilocks belief against the 4 guardrails (Plausibility, Implications, Specificity, Familiarity-vs-Novelty).
5. *(Optional)* "Add sauce" — turn 3–5 winners into actual hook headlines (hand to `/market-pickup-lines` or `luke-iha-vicious-hooks`).

## Content Type Adaptations
| Goal | Push |
|---|---|
| Cold ad hook | Further toward outlandish (still under BS limit) |
| Email subject | Specific Exception/Hidden Factor reads best |
| Educational content | Reframing the Goal sustains a whole piece |
| Skeptical/sophisticated market | Tighten specificity; lean on Scientific/Historical framing |

## Output Requirements
- Three labeled sets of 10. Goldilocks set must include per-item reasoning + category tag.

## FINALIZE
After producing the deliverable, log it through the quality gate (skip only for pure brainstorming):
```bash
// turbo
python3 execution/chain_runner.py finalize "[what you produced] for <market>" \
  --expert luke-iha --skill luke-iha-avatar-machine --workflow epiphany-threshold \
  --type Analysis --intent N --expert-score N --adversarial N --factual N \
  --notes "Factual Grounding: N | Verification: PASS|N/A | Cache: WARM|COLD"
```
If the output contains stats / prices / dates / named entities, FIRST build a proof-claims ledger and run the deterministic G5 gate (see `/copy-engine` Phase 5):
```bash
// turbo
python3 execution/verify_proof_ledger.py --draft <draft-file> --ledger .tmp/copy-engine/<slug>/proof-claims.md || echo "label/cut claims before delivery"
```
Grep finalize output for `QUALITY GATE BLOCKED` and do NOT deliver on a match (finalize exits 0 even when it blocks).

## Quality Gate
Rubric criterion 4 (Goldilocks calibration) ≥8: the 7–9 beliefs are surprising AND self-limiting, with reasoning. Auto-fail: Goldilocks items that are actually obvious (under-threshold) or flat over-BS claims dressed up; no reasoning.
