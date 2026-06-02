---
description: Score an existing ICP, avatar, or creative brief against the Avatar Manifold standard and surface what's missing
tier: 3
stacks_with: avatar-manifold, adversarial-review, copy-doctor
---

# Avatar Manifold Audit

The diagnostic. Scores any existing ICP / persona / avatar / creative brief against the full Manifold standard and produces a prioritized gap list. Use it to QA client work, upgrade a thin persona, or stress-test your own Manifold before delivery.

## Pre-Flight Gate
- An existing artifact to audit (the user's, a competitor's, or a draft Manifold).
- This is a scoring/diagnostic pass — don't rebuild here; output is a gap report + fixes. (Rebuild = `/avatar-manifold`.)

## PHASE 0 — GROUND (auto-fires; skip with `--no-ground`)
Per `references/research-spine.md`. The audit's most valuable check is whether the artifact's "specific language" is REAL — so the audit itself fires a provenance check.
- Run the floor-check + quality gate on the audited artifact's VOC/language section:
```bash
// turbo
python3 execution/research_quality_gate.py validate "<path-to-artifact>" --strict 2>/dev/null \
  || echo "Artifact fails strict provenance — flag its 'specific language' as likely MODELED"
```
- Optional one-shot fact-check of the artifact's market claims — use a CHEAP single Perplexity call (~$0.01–0.02), NOT full Deep Research (this is verification of a few claims, not a re-ground):
  - Model-side: `mcp__perplexity-ask__perplexity_ask` — "Fact-check these market claims about <market>: <key claims>". If a cached `.tmp/copy-engine/<slug>/ground-dossier.md` exists, check it FIRST (its citations may already cover the claims, $0).
- Score rubric criterion 6 (specific-language) against whether the artifact's soundbites trace to real sources or read as invented.

## Skill Acquisition
Load genius.md (rubric + anti-patterns) + `references/framework-library.md` (to check coverage). Load `references/worked-manifold-exemplar.md` as the standard.

## Execution
1. **Coverage scan** — check the artifact for each Manifold component: Buyer Snapshot · Pain Matrix (10 dims) · Core Wound + Ontological Resources · Benefit Matrix · Desire Daisy-Chain · Resonance Hierarchy (4 tiers + dysmorphic avatars) · RH Constraints (6) · Dissolution Frameworks · Epiphany Threshold · Pick-Up Lines · Anti-Hero's Journey · Specific Language (VOC) · Ejection Triggers · Market Addictions · Consciousness level. Mark each Present / Partial / Missing.
2. **Score the 8 rubric criteria** (genius.md) 1–10 with the matching anchor named for any score ≥8.
3. **Anti-pattern flags** — single-adjective descriptions · scores without consequences · invented "specific language" · Identity-clashing leads · fragments-not-Manifold · generic-ICP-treatment.
4. **Prioritized gap list** — rank the missing/weak components by leverage (Core Wound, Identity layer, Specific Language, and Dimensionality first).
5. **Fix recommendations** — for each top gap, name the workflow that closes it (`/core-wound`, `/resonance-hierarchy`, `/buyer-sourcer`, etc.).

## Content Type Adaptations
| Auditing | Focus |
|---|---|
| Generic marketing persona | Almost always missing Core Wound + dimensionality + VOC |
| Competitor's avatar | Reverse-engineer their consciousness level + ejection triggers |
| Own draft Manifold | Pre-delivery QA against all 8 rubric criteria |
| A creative brief | Check it actually plots, not just describes |

## Output Requirements
- Coverage table (Present/Partial/Missing per component).
- 8 rubric scores with anchors for ≥8.
- Anti-pattern flags + prioritized gap list + per-gap fix workflow.

## FINALIZE
After producing the deliverable, log it through the quality gate (skip only for pure brainstorming):
```bash
// turbo
python3 execution/chain_runner.py finalize "[what you produced] for <market>" \
  --expert luke-iha --skill luke-iha-avatar-machine --workflow manifold-audit \
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
Every component checked; scores anchored; gaps ranked by leverage with a named fix. Auto-fail: vague "could be deeper" feedback; no prioritization; not naming the fix workflow.
