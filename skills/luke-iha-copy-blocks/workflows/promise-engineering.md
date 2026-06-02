---
description: Build the Promise Ladder to the Core Transformation, make promises "have balls" (specificity + emotion + conviction), calibrate to the Identity Runway, and gradualize upward.
---

# Promise Engineering

Most copywriters under-promise and hedge. This workflow builds a promise that lands — laddered to the Core Transformation, painted with conviction, and calibrated to the prospect's **identity** ceiling (not their belief ceiling), with a gradualization path for the ambitious segment. Stacks with `luke-iha-proof-ladder` (proof balances the promise) and `luke-iha-unaware-ads` (awareness sets the ceiling).

> **🔒 Pre-Flight Gate**: The master calibration — **the Identity Runway is shorter than the Belief Runway.** Pitch the core promise to the edge of what they believe is possible *for them* (identity), not the edge of what's provable (belief). Know the market's identity ceiling before writing.

## PHASE 0: LOAD MARKET CACHE (warm_core — $0, no re-research)
If this market is already grounded, read its cached intelligence instead of guessing:
```bash
// turbo
cat .tmp/copy-engine/<slug>/warm-core.json 2>/dev/null || echo "NO CACHE — run /copy-engine for this market first (grounds it once, then this is free), or supply the market psychology manually."
```
Load the relevant fields (`dominant_emotion`, `core_wound`, `pain_to_promise_gap`, `market_beliefs`{4 cells}, `top_voc_soundbites`) — sourced from real research, not guessed. No cache + not supplied → ground first.

## PHASE 1: SKILL ACQUISITION
1. `skills/luke-iha-copy-blocks/references/the-six-blocks-deep.md` § Promise
2. `skills/luke-iha-copy-blocks/references/craves-and-velocity.md` (Visual + Expressive)

## PHASE 2: INPUT
- Offer + what it can realistically deliver (full range) · market · identity ceiling estimate · proof strength available · the Core Wound (for the transformation mirror).

## PHASE 3: FIND THE CORE TRANSFORMATION
Name the one transformation the market most wants — often an *identity* shift ("the person they become"). This is the dominant theme. Mirror the Core Wound positively (loss of freedom → "every possibility opens back up").

## PHASE 4: BUILD THE PROMISE LADDER (5 levels)
*General → Specific → Cinematic → Emotional → Core Transformation.* Feature the promise **early and prominently**.

## PHASE 5: IDENTITY-RUNWAY CALIBRATION
- Set the **core promise** at the identity ceiling (copywriter market ≈ $10–20k/mo even if $50k is deliverable).
- Use proof strength as the second lever: stronger proof → push the promise further.

## PHASE 6: MAKE IT "HAVE BALLS" (specificity + emotion + conviction)
Rewrite the core promise from sketch → 8K hidden-camera video of their actual life. Paint with zero doubt. (Same "$10k/mo" rendered poolside, typing voice-notes into a bot, clients raving — vs. a flat number.)

## PHASE 7: GRADUALIZE UPWARD
For the segment without the identity constraint, build the ladder past the core promise: "…some people double down and scale to $30–50k." (Only with real proof of the higher tier.) Never open with the BS-triggering number.

## OUTPUT FORMAT
```
### Core Transformation
"[the identity/outcome shift]" (mirrors Core Wound: …)

### Promise Ladder (deployable — no labels)
General → Specific → Cinematic → Emotional → Core Transformation (1 line each)

### Calibration
Identity ceiling: [X] · core promise set at: [X] · proof lever: [how far it pushes]

### "Balls" Version (the featured promise)
"[specific + emotional + conviction-painted]"

### Gradualization Path
Core → "[bigger, for the ambitious segment]" (proof required: …)
```

## Content Type Adaptations
| Type | Notes |
|---|---|
| VSL | Full ladder + gradualization + future-pacing variants |
| Ad | Core "balls" promise only, one cinematic beat |
| Email | One ladder rung, vivid; proof-as-promise |
| Landing | Core promise above the fold, laddered down the page |

---
## FINALIZE
After producing the deliverable, log it through the quality gate (skip only for pure brainstorming):
```bash
// turbo
python3 execution/chain_runner.py finalize "[what you produced] for <market>" \
  --expert luke-iha --skill luke-iha-copy-blocks --workflow promise-engineering \
  --type Content --intent N --expert-score N --adversarial N --factual N \
  --notes "Factual Grounding: N | Verification: PASS|N/A | Cache: WARM|COLD"
```
If the output contains stats / prices / dates / named entities, FIRST build a proof-claims ledger and run the deterministic G5 gate (see `/copy-engine` Phase 5):
```bash
// turbo
python3 execution/verify_proof_ledger.py --draft <draft-file> --ledger .tmp/copy-engine/<slug>/proof-claims.md || echo "label/cut claims before delivery"
```
Grep finalize output for `QUALITY GATE BLOCKED` and do NOT deliver on a match (finalize exits 0 even when it blocks).

## Quality Gate
> **🛡️**: Promise pitched to belief edge instead of identity edge? Trips the BS detector — pull to identity. Promise hedged/flat? Add specificity + conviction. Gradualized tier without proof? Cut it. Promise buried late? Move it up.
