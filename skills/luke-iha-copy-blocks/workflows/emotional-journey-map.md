---
description: Map the reader's emotional arc across the WHOLE piece — the sequence of feelings and the trigger that fires each one — then assign every emotional beat to the block that produces it. A funnel-level companion to the single-block Pain Chain.
---

# Emotional Journey Map — Funnel-Level Feeling Architecture

The Pain Chain gets one block emotionally deep. This gets the *whole piece* emotionally sequenced. Before writing, you map the **emotional arc** the reader travels — the ordered list of feelings from first line to CTA — and the **specific trigger** that fires each shift. Then you assign every beat to the block that produces it. Copy that lands isn't a stack of blocks; it's a felt journey where each emotion sets up the next. This is the missing bridge between "I have all 6 blocks" and "the reader *feels* pulled through."

> **🔒 Pre-Flight Gate**: You must know the market's `dominant_emotion` and `core_wound` (Decision Framework in `genius.md`). Emotion is re-triggered through story/imagination for psychological markets — you can't map a journey you can't make them *feel* in the moment.

## PHASE 0: LOAD MARKET CACHE (warm_core — $0, no re-research)
```bash
// turbo
cat .tmp/copy-engine/<slug>/warm-core.json 2>/dev/null || echo "NO CACHE — run /copy-engine for this market first, or supply dominant_emotion + core_wound + top_voc_soundbites manually."
```
Load `dominant_emotion`, `core_wound`, `pain_to_promise_gap`, `top_voc_soundbites` (the raw feeling-words the market actually uses). Build the arc from *their* emotional vocabulary, not generic sentiment.

## PHASE 1: SKILL ACQUISITION
1. `skills/luke-iha-copy-blocks/genius.md` (blocks + the Canyon metaphor — the emotional journey IS the crossing)
2. `skills/luke-iha-copy-blocks/references/the-six-blocks-deep.md` § Pain, § Promise (the emotional poles)
3. `skills/luke-iha-copy-blocks/references/craves-and-velocity.md` (E = Expressive, the charge that moves emotion)

## PHASE 2: INPUT
- Market/avatar · asset type + length · the Core Wound (low point) and Core Transformation (high point) · the mechanism (Curiosity) that pivots the arc from fear→hope · any voice-of-customer feeling-language.

## PHASE 3: MAP THE ARC (ordered feelings + triggers)
Lay out the emotional sequence the reader travels. Standard high-conversion shape:
1. **Recognition** ("this is written for me") — trigger: a callout / mirrored pain specific. *Block: Pain (general/specific).*
2. **Descent** (the ache sharpens) — trigger: cinematic dimensionalizing + the softened core-wound tap. *Block: Pain (cinematic→emotional→wound).*
3. **Curiosity/Hope-crack** (the pivot — "wait, there's a way?") — trigger: the wedge / paradoxical question / evocative-named mechanism. *Block: Curiosity (+ Constraint dissolution).*
4. **Relief/Belief** ("I could actually trust this") — trigger: proof-as-promise, the feeling of truth. *Block: Proof.*
5. **Desire/Identity-fit** ("this is who I'd become") — trigger: the Promise Ladder pitched to the identity edge. *Block: Promise.*
6. **Resolve/Urgency** ("act now — it'd be dumb not to") — trigger: curiosity-baked conditions. *Block: Conditions.*
Adapt the shape to the market; not every piece runs all six. Name the **trigger** for each beat explicitly — a feeling with no trigger is a wish.

## PHASE 4: ASSIGN + CHECK CONTINUITY
- Assign each emotional beat to its producing block (above) and confirm no beat is orphaned (a felt shift with no block to cause it) and no block is emotionally silent (present but producing no feeling — dead weight).
- **Continuity rule**: each emotion must *earn* the next. You can't jump from Descent to Desire without the Curiosity/Proof bridge — the reader won't feel the turn. Check every adjacent pair: does beat N make beat N+1 believable?
- Mark the **pivot point** (fear→hope) — the single most important transition; it usually carries the mechanism reveal.

## PHASE 5: WRITE ALONG THE ARC
Draft so each block is written to *produce its assigned feeling*, not just convey information:
- Descent uses Expressive + Visual CRAVES (the Latina-effect charge); Relief drops the intensity so Proof reads calm/credible, not desperate.
- Opening velocity high (3-4 blocks) but the *emotional* through-line stays single and clean.
- Pre-CTA: slow the rhythm so Resolve lands with weight, not a rushed pitch.

## OUTPUT FORMAT
```
### Emotional Arc (internal map)
Beat → Feeling → Trigger → Producing block   (one row per beat, in order)
Pivot point: [where fear turns to hope]

### Continuity Check
[each adjacent pair: does N earn N+1? any orphaned feeling / silent block?]

### Copy (written to the arc — NO visible labels)
[the finished asset]

### Build Notes (internal)
[the dominant_emotion carried through; where the core wound is tapped and softened]
```

## Content Type Adaptations
| Type | Notes |
|---|---|
| VSL | Full 6-beat arc; long descent, clear pivot, staged proof |
| Ad | 3 beats — Recognition → Hope-crack → Resolve; one trigger each, fast |
| Email | Single dominant feeling per email; the arc spans the *sequence*, not one send |
| Landing page | Arc maps to sections; the pivot sits at the mechanism block above the fold-2 |
| Physiological market | Compress the descent (don't over-remind present pain); weight the Hope-crack + Relief |

---
## FINALIZE
After producing the deliverable, log it through the quality gate (skip only for pure brainstorming):
```bash
// turbo
python3 execution/chain_runner.py finalize "[what you produced] for <market>" \
  --expert luke-iha --skill luke-iha-copy-blocks --workflow emotional-journey-map \
  --type Content --intent N --expert-score N --adversarial N --factual N \
  --notes "Factual Grounding: N | Verification: PASS|N/A | Cache: WARM|COLD | Pivot placed: Y/N"
```
If the output contains stats / prices / dates / named entities, FIRST build a proof-claims ledger and run the deterministic G5 gate (see `/copy-engine` Phase 5):
```bash
// turbo
python3 execution/verify_proof_ledger.py --draft <draft-file> --ledger .tmp/copy-engine/<slug>/proof-claims.md || echo "label/cut claims before delivery"
```
Grep finalize output for `QUALITY GATE BLOCKED` and do NOT deliver on a match (finalize exits 0 even when it blocks).

## Quality Gate
> **🛡️**: Does every emotional beat have a named trigger (not a wish)? Does each feeling earn the next (continuity check passed)? Is the fear→hope pivot clearly placed and carried by a real mechanism? Any orphaned feeling or emotionally-silent block? Core wound tapped indirectly with softening? If the copy conveys information but produces no felt arc, it's a block stack, not a journey — remap.
