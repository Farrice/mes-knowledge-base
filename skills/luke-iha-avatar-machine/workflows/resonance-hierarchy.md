---
description: Map a market's full Resonance Hierarchy (Experiences-Beliefs-Values-Identity) plus the 6 constraint types
tier: 1
stacks_with: luke-iha-proof-ladder, luke-iha-unaware-ads, jeremy-miner
---

# Resonance Hierarchy Mapper

Maps the four-tier identity pyramid that determines whether a market will even *let* you persuade them. Built bottom-up (Experiences → Beliefs → Values → Identity), but prospects meet your message top-down — Identity first.

## Pre-Flight Gate
- Market named. Buyer Snapshot helpful but not required.
- Core rule (genius.md Pattern 3): **never conflict with Identity in the lead.** This map's job is to find what to appease and what to avoid clashing with.
- Things harden as they rise — you change Identity by re-framing the Experiences/Beliefs beneath it, never head-on.

## PHASE 0 — GROUND (auto-fires; skip with `--no-ground`)
Per `references/research-spine.md`. The Identity layer (current/aspirational/dysmorphic) must be pulled from how the market describes ITSELF, not invented.
- If the dossier exists, mine `voc-pack.md` for self-description, identity labels, allies/enemies, and "I am / I'm not a ___" language.
- Standalone & not `--no-ground` — route through the ONE grounding chokepoint (reuses a fresh per-market dossier at **$0**; cold-starts paid only on a cache miss):
```bash
// turbo
python3 execution/avatar_manifold_runner.py ground --slug <slug> --market "<market>" --tier deep 2>/dev/null \
  || echo "DEGRADE → mcp__recall__search; map with [MODELED] flags"
```
- Flag the Identity/Value points the lead must NOT clash with — those come straight from the grounded self-language.

## Skill Acquisition
Load `references/framework-library.md` § D (full hierarchy + subsections + Market Love Languages + the 6 RH Constraints). Load genius.md Pattern 3 + Signature Move 3.

## Execution
1. **EXPERIENCES** — Past (frustrations) · Current (pains) · Future (fears).
2. **BELIEFS** — about themselves · the problem · their ability to solve it · self-worth impact · the market · popular solutions · specific experts/authorities · what happens *after* they solve it.
3. **VALUES** — Primary Currency (market love language) · Personal Standards (will/won't do) · External Standards (traits valued in others).
4. **IDENTITY** — Current · Aspirational · **Dysmorphic Avatars** (the feared selves, named like "the Washed-Up Has-Been") · Natural Allies / Enemies.
5. **RH Constraints (6 types)** — list ~5 each: Identity · Values · Belief-Internal · Belief-External · Resource · Experience. (These feed `/dissolution-forge`.)
6. **Conflict flags** — explicitly list which Identity/Value points you must NOT clash with in the lead, and which aspirational-identity hooks you can lead *with*.

## Content Type Adaptations
| Market | Tier that carries the weight |
|---|---|
| Status/coaching/personal brand | Identity + Aspirational + dysmorphic avatars |
| Health/supplement | Beliefs (about ability, about market scams) + Experience constraints |
| Political/values-charged | Values + Identity (allies/enemies) — lead carefully |
| Skills/MMO | Beliefs about self + Belief-External ("you need to be X") |

## Output Requirements
- All four tiers with every subsection populated.
- 6 constraint lists.
- A short "Lead Strategy" note: what to appease, what to avoid, which aspirational hook to lead with.

## FINALIZE
After producing the deliverable, log it through the quality gate (skip only for pure brainstorming):
```bash
// turbo
python3 execution/chain_runner.py finalize "[what you produced] for <market>" \
  --expert luke-iha --skill luke-iha-avatar-machine --workflow resonance-hierarchy \
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
Rubric criterion 3 (Identity-layer fidelity) ≥8: all four tiers + dysmorphic avatars + allies/enemies + explicit lead-conflict flags. Auto-fail: skipping Identity; no dysmorphic avatars; no conflict flags.
