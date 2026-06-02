---
description: Write A-level copy from zero using the blocks — assemble all 6, interleave for velocity, compress, then CRAVES-polish. The production counterpart to the audit.
---

# Copy From Scratch — Block-First Production

Write any persuasive asset from a blank page using the copy-blocks grammar. The method removes blank-page paralysis: you never "think of something good," you *assemble blocks*, then tune. Mirrors how Luke wrote a winning VSL in 4 days instead of 2 weeks — every decision has a stated reason behind it.

> **🔒 Pre-Flight Gate**: Run the **Decision Framework** in `genius.md`. You must know: the Core Wound + Core Transformation, the pain dimension (psychological → re-trigger via story; physiological → acknowledge), the identity ceiling for the promise, and the top constraints to work around.

## PHASE 0: LOAD MARKET CACHE (warm_core — $0, no re-research)
If this market is already grounded, read its cached intelligence instead of guessing:
```bash
// turbo
cat .tmp/copy-engine/<slug>/warm-core.json 2>/dev/null || echo "NO CACHE — run /copy-engine for this market first (grounds it once, then this is free), or supply the market psychology manually."
```
Load the relevant fields (`dominant_emotion`, `core_wound`, `pain_to_promise_gap`, `market_beliefs`{4 cells}, `top_voc_soundbites`) — sourced from real research, not guessed. No cache + not supplied → ground first.

## PHASE 1: SKILL ACQUISITION
1. `skills/luke-iha-copy-blocks/genius.md`
2. `skills/luke-iha-copy-blocks/references/the-six-blocks-deep.md`
3. `skills/luke-iha-copy-blocks/references/craves-and-velocity.md`
4. For the curiosity mechanism: `skills/luke-iha-copy-blocks/references/curiosity-engine.md`

## PHASE 2: INPUT
- Product/offer · target market · awareness level · asset type (ad / VSL lead / email / landing / headline) · desired length · any proof assets available.

## PHASE 3: SOURCE THE BLOCKS (the raw material)
Generate raw material per block *before* writing prose:
1. **Pain** — Pain Chain (general→specific→cinematic→emotional→core wound), calibrated by the dominant Pain-Matrix dimension. *(Or run `pain-chain-builder`.)*
2. **Promise** — Promise Ladder to the Core Transformation, pitched to the identity ceiling. *(Or `promise-engineering`.)*
3. **Curiosity** — the mechanism: pick the Quadrant cell, give it an Evocative Name, strengthen with the 4 tools. *(Or `curiosity-engine`.)*
4. **Proof** — match proof to promise level; pick the doubt-nodes where proof will sit. *(Deep: `luke-iha-proof-mechanisms`.)*
5. **Constraints** — Big Three + top identity/value constraint; decide work-around vs. AWE-dissolve. *(Or `constraint-dissolution`.)*
6. **Conditions** — the 5 types available, blended with curiosity. *(Or `conditions-stack`.)*

## PHASE 3.5: BELIEF-STATE SEQUENCING (decide block order)
Block order is a persuasion decision, not a template. Diagnose the reader's **entry state** and sequence accordingly:
- **Identity-resistant / skeptical** → open Conditions/Qualification or Curiosity *first* (recognition before pain) to bypass defensive rejection.
- **Problem-aware, pain-present** → Pain-first is fine.
- **Unaware** → Curiosity/Story-first (Show), pain re-triggered mid-stream.
Map the sequence as a block string before writing.

## PHASE 4: WRITE — INTERLEAVE FOR VELOCITY
Write prose deploying the blocks in the sequenced order, applying velocity rules:
- Opening ~100 words hit 3–4 blocks.
- No block 4+ consecutive sentences; fresh angle on every reappearance.
- Proof Braid: every claim carries an intertwined proof element (Belief Bank stays balanced).
- Core wound woven indirectly with softening language.
- Pre-CTA: deliberately slow the rhythm.

## PHASE 5: COMPRESS (velocity) + CRAVES POLISH
- Cut filler — say the same thing in fewer words (density).
- Run each block through CRAVES; strengthen the weakest dimension (esp. the curiosity name → Specific/Visual). *(Or run `craves-polish` on the key lines.)*

## OUTPUT FORMAT
```
### Block Plan
Sequence: [block string] · entry state: [diagnosis]
Pain | Promise | Curiosity (mechanism: "[name]") | Proof | Constraints | Conditions — 1-line each

### Copy
[the finished asset — NO visible block labels]

### Build Notes (internal)
[Why this sequence; the limiting factor watched on the Copy Blocks Equation]
```

## Content Type Adaptations
| Type | Notes |
|---|---|
| Facebook/short ad | Hook-heavy; 1 mechanism; conditions light; high opening velocity |
| VSL lead | Full Pain Chain + Promise Ladder; mechanism reveal is the spine → pairs `luke-iha-vsl-leads` |
| Email | One idea, one frame; fast velocity; proof-as-promise common |
| Landing page | All 6 blocks; conditions stack heavy; proof at each doubt-node |
| Headline | Compress all blocks into 1–2 lines; CRAVES-max |

---
## FINALIZE
After producing the deliverable, log it through the quality gate (skip only for pure brainstorming):
```bash
// turbo
python3 execution/chain_runner.py finalize "[what you produced] for <market>" \
  --expert luke-iha --skill luke-iha-copy-blocks --workflow copy-from-scratch \
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
> **🛡️**: Run against `genius.md` § Anti-Patterns. Blocks invisible to the reader. Promise at identity edge (not belief edge). Claim never bigger than proof. Mechanism name passes the portability test. Clarity is King.
