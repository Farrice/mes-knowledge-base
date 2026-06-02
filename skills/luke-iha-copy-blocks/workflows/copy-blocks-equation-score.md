---
description: Score any offer, headline, or piece of copy on the Copy Blocks Equation — (Promise × Proof × Curiosity) ÷ Constraints × Conditions — and name the single limiting factor to fix.
---

# Copy Blocks Equation Score

A diagnostic scorer built on Luke's parallel to Hormozi's value equation. Instead of vague "this could be stronger," it locates the **one limiting factor** dragging the copy/offer down — because a multiplicative equation collapses on its weakest term. Stacks with `excellence-predictor` (pre-flight grade) and the `copy-block-audit` (line-level fixes).

$$\text{Value} = \frac{\text{Promise} \times \text{Proof} \times \text{Curiosity}}{\text{Constraints}} \times \text{Conditions}$$

> **🔒 Pre-Flight Gate**: This scores *composition strength*, not a CVS density number. The output is a limiting-factor diagnosis + the highest-leverage fix — not a vanity score to report to clients.

## PHASE 0: LOAD MARKET CACHE (warm_core — $0, no re-research)
If this market is already grounded, read its cached intelligence instead of guessing:
```bash
// turbo
cat .tmp/copy-engine/<slug>/warm-core.json 2>/dev/null || echo "NO CACHE — run /copy-engine for this market first (grounds it once, then this is free), or supply the market psychology manually."
```
Load the relevant fields (`dominant_emotion`, `core_wound`, `pain_to_promise_gap`, `market_beliefs`{4 cells}, `top_voc_soundbites`) — sourced from real research, not guessed. No cache + not supplied → ground first.

## PHASE 1: SKILL ACQUISITION
1. `skills/luke-iha-copy-blocks/genius.md` § Copy Blocks Equation + § The 6 Blocks
2. `skills/luke-iha-copy-blocks/references/the-six-blocks-deep.md` (for any weak term's deep fix)

## PHASE 2: INPUT
- The offer / headline / copy · market · awareness level · (optional) what's underperforming.

## PHASE 3: SCORE EACH TERM (1–10)
- **Promise** (dream outcome) — laddered? at identity edge? "has balls"?
- **Proof** (perceived likelihood) — balances the promise? braided, not clustered?
- **Curiosity** (vehicle/mechanism) — Evocative, insightful, in the epiphany band?
- **Constraints** (denominator — *higher = worse*) — Big Three + identity/value blocks unaddressed?
- **Conditions** (multiplier) — present, curiosity-blended, believable?

## PHASE 4: FIND THE LIMITING FACTOR
Because the equation is multiplicative (and Constraints divides), the **lowest numerator term OR the highest constraint** dominates. A perfect promise/proof/curiosity still fails if a **value constraint** ("scam grandmothers") blows up the denominator. Name the single binding constraint.

## PHASE 5: PRESCRIBE THE FIX
Point to the exact workflow for the limiting term:
- Promise → `promise-engineering` · Proof → `luke-iha-proof-mechanisms` · Curiosity → `curiosity-engine` · Constraints → `constraint-dissolution` · Conditions → `conditions-stack`.
Give the one fix that moves the equation most.

## OUTPUT FORMAT
```
### Equation Read
Promise:_/10 · Proof:_/10 · Curiosity:_/10 · Constraints:_/10 (↑=worse) · Conditions:_/10

### Limiting Factor
[term] — why it's binding (1–2 sentences)

### Highest-Leverage Fix
[the single change] → run /[workflow]

### Watch
[the trap if you fix the wrong term — e.g. adding proof when the real blocker is a value constraint]
```

## Content Type Adaptations
| Type | Notes |
|---|---|
| Offer (pre-copy) | Score at offer level — Hormozi parallel; fix structure before writing |
| Headline | Compressed scoring; usually curiosity or specificity binds |
| Full asset | Score, then hand the binding term to its workflow + `copy-block-audit` |

---
## FINALIZE
After producing the deliverable, log it through the quality gate (skip only for pure brainstorming):
```bash
// turbo
python3 execution/chain_runner.py finalize "[what you produced] for <market>" \
  --expert luke-iha --skill luke-iha-copy-blocks --workflow copy-blocks-equation-score \
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
> **🛡️**: Did you prescribe strengthening a term that isn't the limiting factor? Re-check — multiplicative equations don't reward boosting a 9 to a 10 while a 3 sits in the denominator. Constraint scored as numerator? It divides — recount.
