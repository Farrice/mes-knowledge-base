---
description: Build the pain sequence — general → specific → cinematic → emotional → core wound — calibrated by the Pain Matrix, with indirect/softened core-wound weaving.
---

# Pain Chain Builder

Construct a market's full pain escalation the way Luke does in winning VSLs: an overarching description, three specifics, a cinematic life-picture, the emotion, and a brief, *indirect* touch on the core wound. Calibrated by the Pain Matrix so you re-trigger psychological pain (via story) without over-reminding physiological pain.

> **🔒 Pre-Flight Gate**: Identify the **dominant Pain-Matrix dimension** first — especially psychological vs. physiological. It changes the whole approach: physiological pain is felt *now* (acknowledge, don't dwell); psychological pain is intermittent (must be re-triggered through story/imagination while they read).

## PHASE 0: LOAD MARKET CACHE (warm_core — $0, no re-research)
If this market is already grounded, read its cached intelligence instead of inventing the pain:
```bash
// turbo
cat .tmp/copy-engine/<slug>/warm-core.json 2>/dev/null || echo "NO CACHE — run /copy-engine for this market first (grounds it once, then this is free), or supply the Core Wound + pain dimension manually."
```
Load `core_wound` (the existential bottom), `dominant_emotion`, and `top_voc_soundbites` (the rawest verbatim fear/shame language — build the Pain Chain from *their* words). Real research, not guessed. No cache + not supplied → ground first.

## PHASE 1: SKILL ACQUISITION
1. `skills/luke-iha-copy-blocks/references/the-six-blocks-deep.md` § Pain
2. `skills/luke-iha-copy-blocks/references/craves-and-velocity.md` (Visual + Expressive)

## PHASE 2: INPUT
- Market/avatar · the problem · (optional) voice-of-customer language, the Core Transformation (for the promise mirror).

## PHASE 3: PAIN MATRIX CALIBRATION
Classify the pain:
- **Psychological or physiological?** (master split — sets re-trigger strategy)
- **Measurable or not?** (if not, connect any stat to a concrete *feeling*)
- **Social stigma?** (how directly can you approach it)
State the approach implication in one line before building.

## PHASE 4: BUILD THE CHAIN (5 levels)
1. **General** — the overarching description of what's bothering them.
2. **Specific** — 3 concrete aspects.
3. **Cinematic** — dimensionalize: a movie of it in their actual day (Visual).
4. **Emotional** — what they *feel* (Expressive — match the power-word bank).
5. **Core Wound** — brief, *indirect*, softened touch on the existential bottom (death/annihilation/abandonment/total loss).

## PHASE 5: CORE WOUND — IDENTIFY + WEAVE
- Name the market's one dominant Core Wound (skincare → invisibility; joint pain → loss of freedom).
- Weave it **indirectly** (never "Do you feel invisible?"), with **softening/hedging** language ("I don't know if you've felt this, but…"), often via victimization framing ("how it *robs* you, *forces* you, makes you feel old before your time").
- Make it a recurring subtle theme (marketing DNA), not a callout.

## OUTPUT FORMAT
```
### Pain Matrix Read
Type: [psych/physio] · measurable:_ · stigma:_ → approach: …

### Core Wound
"[the wound]" — weave strategy: [indirect via …]

### The Pain Chain (deployable copy — no visible labels)
General: "…"
Specific: "…", "…", "…"
Cinematic: "…"
Emotional: "…"
Core-wound touch (softened): "…"

### Promise Mirror (optional handoff)
[the inverse line that pops the wound positively → feeds promise-engineering]
```

## Content Type Adaptations
| Type | Notes |
|---|---|
| VSL | Full 5-level chain up front |
| Email | General + one specific + emotion; single core-wound whisper |
| Ad | Cinematic or emotional level only — fast |
| Physiological market | Compress levels 1–4; lead toward the new-solution belief |

---
## FINALIZE
After producing the deliverable, log it through the quality gate (skip only for pure brainstorming):
```bash
// turbo
python3 execution/chain_runner.py finalize "[what you produced] for <market>" \
  --expert luke-iha --skill luke-iha-copy-blocks --workflow pain-chain-builder \
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
> **🛡️**: Core wound direct or un-softened? Rewrite. Psychological pain not re-triggered via story? Add the cinematic level. Stats cited without a connected feeling? Fix. No assumption of "I know exactly how you feel."
