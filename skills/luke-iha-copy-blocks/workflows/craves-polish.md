---
description: Elevate any flat line, headline, or copy block through CRAVES — Clear, Relevant, Accurate, Visual, Expressive, Specific. The universal strengthener.
---

# CRAVES Polish — The Universal Block Strengthener

Take any line that's structurally fine but emotionally flat and elevate it across the six CRAVES dimensions. Two pieces of copy can contain the *exact same blocks* and score 6/10 vs 10/10 — this workflow closes that gap. Atom: used standalone or as the final pass inside every other copy-blocks workflow.

> **🔒 Pre-Flight Gate**: Confirm the line already has its blocks (if blocks are *missing*, run `copy-block-audit` first — CRAVES strengthens; it doesn't add blocks). Know the market's dominant emotion / Core Wound to pick the right power-word bank.

## PHASE 0: LOAD MARKET CACHE (warm_core — $0, no re-research)
If this market is already grounded, read its cached intelligence instead of guessing the emotion:
```bash
// turbo
cat .tmp/copy-engine/<slug>/warm-core.json 2>/dev/null || echo "NO CACHE — run /copy-engine for this market first (grounds it once, then this is free), or supply the Core Wound / dominant emotion manually."
```
Use `dominant_emotion` + `core_wound` to pick the right power-word bank, and `top_voc_soundbites` for real phrasing. These come from real research, not a guess. No cache + not supplied → ground first (this is a refinement tool; it needs grounding to refine).

## PHASE 1: SKILL ACQUISITION
1. `skills/luke-iha-copy-blocks/references/craves-and-velocity.md`
2. `skills/luke-iha-copy-blocks/genius.md` § CRAVES

## PHASE 2: INPUT
- The line(s) to polish · the market + product · (optional) the Core Wound / dominant emotion.

## PHASE 3: SIX-DIMENSION PASS
Run the line through each dimension; note which are *already* strong and which are the lift:
- **Clear** — any ambiguity, jargon-creep, or tangle? (Clarity is King — wins all ties.)
- **Relevant** — is this the real, segment-specific desire?
- **Accurate** — precise to their reality / nuance?
- **Visual** — can they *picture* it? Dimensionalize ("rewires your mind, body & emotions" > "clears hidden roots").
- **Expressive** — emotional charge? Apply the right power-word bank (Greed/Lazy/Lust/Safety/Terror). The "Latina effect": same facts, apex-of-importance delivery.
- **Specific** — named mechanism? Concrete problem-tokens ("can't sit with legs crossed" > "weight loss")? "Clinical studies prove" > "doctors say"?

## PHASE 4: PRODUCE 3 ESCALATING VERSIONS
- **V1 — Clarity-trued** (C·R·A fixed, minimal).
- **V2 — Charged** (+ Visual·Expressive·Specific).
- **V3 — Maxed** (full saturation — then sanity-check it didn't break Clarity or believability).
Recommend one. Show the single highest-leverage dimension that moved the needle.

## OUTPUT FORMAT
```
Original: "…"
CRAVES read: C[✓/✗] R[ ] A[ ] V[ ] E[ ] S[ ]  → weakest: [dimension]
V1 (clear): "…"
V2 (charged): "…"
V3 (maxed): "…"
→ Recommend: V_ — because [dimension] was the gap.
```

## Content Type Adaptations
| Type | Emphasis |
|---|---|
| Headline | Specific + Visual carry most weight; keep Clear |
| Bullet/fascination | Specific + Expressive (Evocative mechanism name) |
| Pain line | Visual (cinematic) + Expressive (terror/loss bank) |
| Promise line | Visual (8K life-picture) + Expressive |
| CTA-adjacent | Clarity dominates; dial expressive *down* for trust |

---
## FINALIZE
After producing the deliverable, log it through the quality gate (skip only for pure brainstorming):
```bash
// turbo
python3 execution/chain_runner.py finalize "[what you produced] for <market>" \
  --expert luke-iha --skill luke-iha-copy-blocks --workflow craves-polish \
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
> **🛡️**: Did saturation break Clarity or trip the believability/epiphany threshold? If V3 reads as "trying too hard," ship V2. Power words matched to the Core Wound, not sprinkled at random.
