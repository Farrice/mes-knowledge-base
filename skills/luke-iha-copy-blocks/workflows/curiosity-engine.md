---
description: Generate curiosity blocks / mechanisms — pick the Curiosity Quadrant cell for the Idea, grade Insight, then strengthen with Epiphany Threshold, Evocative Naming, Intuition Pumps, and Idea Caricature.
---

# Curiosity Engine — Idea Generation + Mechanism Naming

Curiosity is the most important and most-botched block. This workflow generates the **Idea** (Curiosity Quadrant), grades its **Insight**, and strengthens it with the **4 Thinking Tools** — producing mechanism names, hooks, and fascinations that create real tension. Stacks with `luke-iha-insight-vectors` (epiphany grammar) and `luke-iha-million-dollar-mechanisms` (full mechanism engineering).

> **🔒 Pre-Flight Gate**: Know the gap you're bridging — the specific Pain and the specific Promise. Curiosity lives in *that* gap. Know the market's existing beliefs about the problem and the solutions (for the Quadrant's external column).

## PHASE 0: LOAD MARKET CACHE (warm_core — $0, no re-research)
If this market is already grounded, read its cached intelligence — `market_beliefs` maps **1:1** onto the Curiosity Quadrant, so the cache pre-fills Phase 3:
```bash
// turbo
cat .tmp/copy-engine/<slug>/warm-core.json 2>/dev/null || echo "NO CACHE — run /copy-engine for this market first (grounds it once, then this is free), or supply the Pain→Promise gap + the 4 market_beliefs manually."
```
Load `pain_to_promise_gap` (the gap curiosity bridges) + `market_beliefs.{external_problem, internal_problem, external_solution, internal_solution}` (the 4 Quadrant cells) + `top_voc_soundbites`. Real research, not guessed. No cache + not supplied → ground first.

## PHASE 1: SKILL ACQUISITION
1. `skills/luke-iha-copy-blocks/references/curiosity-engine.md`
2. `skills/luke-iha-copy-blocks/genius.md` § Curiosity

## PHASE 2: INPUT
- Product/offer · the Pain→Promise gap · what the market currently believes about the problem and about competing solutions · output wanted (mechanism name / hooks / fascinations / sales-letter open).

## PHASE 3: GENERATE THE IDEA (Curiosity Quadrant)
Fill all four cells (split general/specific where useful):
- **External Problem** — what the market *thinks* the problem is.
- **Internal Problem (UMP)** — the *real* problem / your reframe.
- **External Solution** — what the market *thinks* the fixes are.
- **Internal Solution (UMS)** — your unique mechanism.
Then draft angles from the four moves: *(1) your problem-belief is wrong · (2) here's the real problem · (3) everyone else's solutions are BS · (4) here's the one solution that matters.*

## PHASE 4: GRADE INSIGHT
Score each candidate idea on the 4 qualities — **Simple, Easy, Explanatory⭐, Novel⭐**. Keep ideas that are *explanatory* (reframe reality / explain past failure) AND *novel*. Kill the obvious ("eat less to lose weight") and the in-line-with-what-they've-heard.

## PHASE 5: STRENGTHEN WITH THE 4 TOOLS
1. **Epiphany Threshold (0–10)** — push novelty into the 6–9 goldilocks band; pull back anything 9–10 (unbelievable).
2. **Evocative Naming** — name the mechanism specifically and tie it to the problem ("hidden cartilage destroyer," "off-market dating system"). Run the **portability test** (could it drop unchanged into an unrelated market? → too generic) and the **magnet test** (enough to guess, not enough to know).
3. **Intuition Pumps** — borrow comprehension via natural/mechanical metaphor, forces, or strong associations.
4. **Idea Caricature** — find and exaggerate the surprising/taboo facet (kidney bean → "white carb before bed").

## PHASE 6: ANTI-CONSTRAINT CHECK (bake in relief)
Where possible, choose a name/angle that *also* dissolves the dominant constraint (whisper = value-safe, lazy = effort-safe, while-you-sleep = time-safe). Curiosity + constraints fused = ideal.

## OUTPUT FORMAT
```
### Quadrant
Ext-Problem | UMP | Ext-Solution | UMS  (1–2 lines each)

### Top Ideas (Insight-graded)
1. [idea] — Explanatory:_/Novel:_ — why it reframes
...

### Mechanism Name(s)
"[name]" — associations it triggers: … — passes portability ✓ / magnet ✓
[2 alternates]

### Deployable Hooks / Fascinations
- [5–10 lines, each Quadrant-sourced + tool-strengthened, no visible labels]
```

## Content Type Adaptations
| Type | Tool emphasis |
|---|---|
| Sales-letter mechanism | Evocative Naming + Intuition Pump (general/holistic) |
| Ad hook | Idea Caricature + Epiphany Threshold (specific, punchy) |
| Bullets/fascinations | Quadrant breadth — one per cell, varied frames |
| Organic content | Specific-cell angles ("why THIS thing is bad for X") |

---
## FINALIZE
After producing the deliverable, log it through the quality gate (skip only for pure brainstorming):
```bash
// turbo
python3 execution/chain_runner.py finalize "[what you produced] for <market>" \
  --expert luke-iha --skill luke-iha-copy-blocks --workflow curiosity-engine \
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
> **🛡️**: Mechanism name fails the portability test? Rewrite. Idea sits at 9–10 (unbelievable)? Pull down. Name surfaced to the reader as "mechanism"? Hide it. Curiosity should create the magnet tension, not give the answer away.
