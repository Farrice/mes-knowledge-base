---
description: Map the Resonance Hierarchy (Experience→Belief→Value→Identity), identify the Big Three + identity constraints to work around, then dissolve where necessary via the AWE framework.
---

# Constraint Dissolution — Resonance Hierarchy + AWE

Most copywriters can't even *identify* a market's constraints, let alone dissolve them. This workflow maps how constraints formed, decides what to **work around** vs. **dissolve**, and builds AWE (Acknowledge–Wedge–Elaborate) sequences for the ones you must address — a top-1% edge. Stacks with belief-dissolution skills and `luke-iha-unaware-ads`.

> **🔒 Pre-Flight Gate**: Default posture is **work around constraints, don't trigger them** — especially identity and values. Only dissolve directly when the constraint blocks the sale and can't be sidestepped.

## PHASE 0: LOAD MARKET CACHE (warm_core — $0, no re-research)
If this market is already grounded, read its cached intelligence instead of guessing:
```bash
// turbo
cat .tmp/copy-engine/<slug>/warm-core.json 2>/dev/null || echo "NO CACHE — run /copy-engine for this market first (grounds it once, then this is free), or supply the market psychology manually."
```
Load the relevant fields (`dominant_emotion`, `core_wound`, `pain_to_promise_gap`, `market_beliefs`{4 cells}, `top_voc_soundbites`) — sourced from real research, not guessed. No cache + not supplied → ground first.

## PHASE 1: SKILL ACQUISITION
1. `skills/luke-iha-copy-blocks/references/constraint-dissolution.md`
2. `skills/luke-iha-copy-blocks/genius.md` § Constraints

## PHASE 2: INPUT
- Product/offer · target market · known objections / hesitations · (optional) avatar research.

## PHASE 3: BIG THREE AUDIT
Rate the market's **Money / Time / Effort** constraints and their ratio (money-rich+time-poor vs. reverse). Note the relief each needs — and whether it can be baked into the mechanism name.

## PHASE 4: RESONANCE HIERARCHY MAP
For the blocking belief, reconstruct the likely formation chain:
```
Experience → Belief → Value → Identity
```
Mark each constraint's **level**. Crystallization rule: identity/values = work around (never challenge in copy); beliefs = sometimes dissolvable; experience-interpretation = the soft layer where dissolution happens. Flag identity "I am…" constraints explicitly so they're respected, not attacked.

## PHASE 5: DECIDE — WORK AROUND vs. DISSOLVE
- **Work around** (default): reframe the offer to meet them at their identity level (e.g. don't sell "date supermodels" to men with "I'm not good enough" identity); bake relief into the mechanism (Anti-Constraint naming).
- **Dissolve** (only when blocking + unavoidable): proceed to AWE.

## PHASE 6: BUILD THE AWE SEQUENCE (for constraints you must dissolve)
- **A — Acknowledge**: validate the belief, lower resistance ("I used to think this too").
- **W — Wedge**: split the bundled hidden assumptions with a counter-example / paradoxical question / study / analogy. *(Paradoxical questions are nuclear — they dissolve belief AND spike curiosity.)* Name the two bundled assumptions explicitly, then concede one and detonate the other.
- **E — Elaborate**: expand the opened gap into the new belief, hand off to your mechanism.

## OUTPUT FORMAT
```
### Big Three
Money:_ Time:_ Effort:_ — ratio: … — relief baked into name? [how]

### Resonance Map (key constraint)
Experience: … → Belief: … → Value: … → Identity: "I am…"
Verdict: [work around / dissolve]

### Work-Arounds
- [reframes + Anti-Constraint mechanism names]

### AWE Sequences (only for must-dissolve constraints)
Constraint: "[belief]"
A: "…"  W: [bundled assumptions a/b] → "…"  E: "…"
```

## Content Type Adaptations
| Type | Notes |
|---|---|
| VSL | Full AWE for the one core blocking belief; work around the rest |
| Email | One constraint, fast AWE or a single paradoxical-question wedge |
| Landing page | Big-Three relief in conditions; identity constraints worked around |
| Offer design | Hormozi exercise — solve+prioritize every constraint at offer level |

---
## FINALIZE
After producing the deliverable, log it through the quality gate (skip only for pure brainstorming):
```bash
// turbo
python3 execution/chain_runner.py finalize "[what you produced] for <market>" \
  --expert luke-iha --skill luke-iha-copy-blocks --workflow constraint-dissolution \
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
> **🛡️**: Did you challenge an identity/value head-on? Rewrite to work around. Acknowledge present before every wedge (no bare attacks). Wedge uses a real counter-example, not an assertion. The dissolved belief hands off to the mechanism, not to thin air.
