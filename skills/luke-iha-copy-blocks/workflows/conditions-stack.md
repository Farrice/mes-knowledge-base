---
description: Deploy the 6th block — 5 condition types (Qualifications, Conversion Triggers, Risk Reversal, Value Adds, Terms) blended with curiosity so they differentiate in a Hormozi-saturated market.
---

# Conditions Stack — The 6th Block ("Infinity Stones")

Conditions are the most powerful block — but in a market where everyone runs the same guarantees and bonuses, naked conditions sound identical. This workflow stacks all 5 condition types AND blends curiosity into them so the offer differentiates. Stacks with `luke-iha-million-dollar-mechanisms` and offer-design skills.

> **🔒 Pre-Flight Gate**: Conditions require a real offer to deliver — confirm what the offer can actually back. If you're a copywriter without offer control, flag which conditions are out of scope. The edge isn't *having* conditions; it's **baking curiosity into them**.

## PHASE 0: LOAD MARKET CACHE (warm_core — $0, no re-research)
If this market is already grounded, read its cached intelligence instead of guessing:
```bash
// turbo
cat .tmp/copy-engine/<slug>/warm-core.json 2>/dev/null || echo "NO CACHE — run /copy-engine for this market first (grounds it once, then this is free), or supply the market psychology manually."
```
Load the relevant fields (`dominant_emotion`, `core_wound`, `pain_to_promise_gap`, `market_beliefs`{4 cells}, `top_voc_soundbites`) — sourced from real research, not guessed. No cache + not supplied → ground first.

## PHASE 1: SKILL ACQUISITION
1. `skills/luke-iha-copy-blocks/references/the-six-blocks-deep.md` § Conditions
2. `skills/luke-iha-copy-blocks/genius.md` § Conditions + Copy Blocks Equation

## PHASE 2: INPUT
- Offer details (price, guarantee capacity, bonuses, deadlines, payment options) · market · the curiosity mechanism name (to blend in).

## PHASE 3: STACK THE 5 TYPES
1. **Qualifications** — call-out + criteria ("Attention former athletes who've watched their bodies weaken…").
2. **Conversion Triggers** — urgency + scarcity ("9 spots remaining," "price doubles at midnight"). Keep real.
3. **Risk Reversal** — guarantee / money-back / "you don't pay."
4. **Value Adds** — bonuses, discounts, free modules, rewards.
5. **Terms & Structures** — payment plans, financing.
List what the offer can legitimately support per type.

## PHASE 4: BLEND CURIOSITY (the differentiator)
Rewrite each naked condition with the mechanism/curiosity baked in:
> "10–20 agency clients or you don't pay" → "**Former VC partner reveals lead-cloning method** that brings you 10–20 agency clients/month on autopilot — guaranteed, or you don't pay."
The conditions attack time/money/risk; the curiosity makes the *whole offer* feel new.

## PHASE 5: EQUATION CHECK
Confirm conditions are *multiplying* an already-strong `(Promise × Proof × Curiosity) ÷ Constraints` — not propping up weak blocks. If the offer leans only on conditions, send back to strengthen curiosity/proof first.

## OUTPUT FORMAT
```
### Available Conditions (by type)
Qualifications: … | Triggers: … | Risk Reversal: … | Value Adds: … | Terms: …
[flag any out of copywriter scope]

### Curiosity-Blended Stack (deployable)
- [each condition rewritten with mechanism baked in]

### Placement
[where each sits: qualification up top, triggers near CTA, risk-reversal at the price doubt-node…]
```

## Content Type Adaptations
| Type | Notes |
|---|---|
| Landing page / offer | Full stack, all 5 types, curiosity-blended |
| Ad | Qualification call-out + one trigger |
| Email close | Trigger + risk reversal, blended |
| Webinar pitch | Value adds + terms + scarcity stack |

---
## FINALIZE
After producing the deliverable, log it through the quality gate (skip only for pure brainstorming):
```bash
// turbo
python3 execution/chain_runner.py finalize "[what you produced] for <market>" \
  --expert luke-iha --skill luke-iha-copy-blocks --workflow conditions-stack \
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
> **🛡️**: Conditions naked (sound like everyone else's)? Blend in the mechanism. Fake scarcity/urgency? Cut — it poisons trust. Relying on conditions to rescue a weak promise/proof? Fix the numerator first.
