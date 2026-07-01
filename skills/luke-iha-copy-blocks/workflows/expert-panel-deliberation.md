---
description: Assemble a tailored 3-7 expert panel, map each expert to the blocks they strengthen, and run a user-gated deliberation loop that refines the copy one lens at a time — collaborative refinement, not solo drafting.
---

# Expert Panel Deliberation — Collaborative Block Refinement

Most copy-blocks workflows are solo-author: one voice assembles all 6 blocks. This one is different. It stands up a **custom panel of 3-7 top-tier experts** — assembled for *this specific* objective — and runs the copy through a **collaborative, user-gated deliberation** where each expert improves the block they own. The panel doesn't stitch a Frankenstein draft (that fails — see genius.md); it critiques and rewrites *specific blocks* while one author keeps the spine coherent. Use it when a solo pass has plateaued, the stakes are high, or the client wants to *see* the reasoning.

> **🔒 Pre-Flight Gate**: Run the **Decision Framework** in `genius.md` first (Core Wound, Core Transformation, pain dimension, identity ceiling, top constraints). The panel refines an *existing* block plan — it is not a substitute for grounding. If nothing has been drafted, run `copy-from-scratch` first, then bring the draft here.

## PHASE 0: LOAD MARKET CACHE (warm_core — $0, no re-research)
```bash
// turbo
cat .tmp/copy-engine/<slug>/warm-core.json 2>/dev/null || echo "NO CACHE — run /copy-engine for this market first, or supply market psychology (core_wound, dominant_emotion, market_beliefs) manually."
```
Load `dominant_emotion`, `core_wound`, `market_beliefs` (4 cells), `top_voc_soundbites`. The panel argues from real intelligence, never invented market facts.

## PHASE 1: SKILL ACQUISITION
1. `skills/luke-iha-copy-blocks/genius.md` (the block grammar every expert reasons in)
2. `skills/luke-iha-copy-blocks/references/craves-and-velocity.md`
3. For contested blocks, the matching deep reference (`the-six-blocks-deep.md`, `curiosity-engine.md`, `constraint-dissolution.md`).

## PHASE 2: INPUT
- The objective (asset type + market + core transformation) · the current draft OR block plan · which block(s) feel weakest · any brand voice constraints.

## PHASE 3: ASSEMBLE THE PANEL (3-7 experts, mapped to blocks)
Generate a panel **tailored to this objective** — not a fixed roster. Each expert gets a persona AND an explicit block assignment:
```
**Name:** [expert name]
**Lens:** [what they see that others miss]
**Owns block(s):** [Pain | Promise | Proof | Constraints | Curiosity | Conditions]
**Bias to watch:** [the failure mode of over-indexing on this lens]
```
Rules:
- **Cover every weak block.** At minimum assign one expert to each block flagged in Phase 2. The Curiosity block (the marketing) always gets its own owner — it is the block most copywriters underserve.
- **Diverse, non-redundant lenses.** A psychology expert (Pain/Constraints), a mechanism/idea expert (Curiosity), a proof-craft expert (Proof), a voice/authenticity expert (kills AI tells across all blocks). Do not stack two experts with the same lens.
- **One expert is the SPINE-KEEPER** — owns coherence and velocity across the whole piece. Their job is to *reject* any block rewrite that breaks the single-author heartbeat. (This is the guard against the multi-author Frankenstein: experts propose block-level lines; the spine-keeper decides what survives.)
- Present the panel to the user for approval/adjustment before deliberating. **Wait for the user.**

## PHASE 4: DELIBERATION ROUND (one block at a time, user-gated)
For each targeted block, run the loop — and stop for user input between rounds:
1. **Owning expert diagnoses** the block against CRAVES + its native grammar (Pain→Pain Chain, Curiosity→Quadrant + 4 tools, etc.). Names the single weakest dimension.
2. **Owning expert rewrites** — feedback ONLY in the form of copy (Kat Merrit's rule; genius.md). No "add more proof" — the better line, written.
3. **One dissent** from a cross-lens expert (e.g. the voice expert flags an AI tell; the proof expert flags a claim now bigger than its proof).
4. **Spine-keeper adjudicates**: accept the rewrite, accept-with-edit, or reject for breaking velocity/coherence. States the reason.
5. Present the before/after for that block to the user. **Wait.** Then next block.

## PHASE 5: REINTEGRATE + VELOCITY PASS
The spine-keeper stitches the surviving rewrites back into ONE coherent draft (single author, not concatenated fragments), then:
- Re-interleave so no block dominates 4+ sentences; every reappearance uses a fresh angle.
- Confirm the Belief Bank stays balanced (no claim now outruns its proof after the rewrites).
- Run the whole piece through `prose_classifier.py` mentally: no twin-sentence endings, no triple anaphora, ≤1-2 em dashes.

## OUTPUT FORMAT
```
### Panel (mapped to blocks)
[Name — Lens — Owns block — Bias to watch] × 3-7

### Deliberation Ledger (internal)
Per block: weakest dimension → expert rewrite → dissent → spine-keeper verdict + reason

### Copy (final, single coherent author — NO visible block/expert labels)
[the reintegrated asset]

### What Changed & Why
[2-4 lines: which blocks moved, the limiting factor on the Copy Blocks Equation now]
```

## Content Type Adaptations
| Type | Notes |
|---|---|
| VSL / long-form | Full panel; deliberate every major block; spine-keeper essential |
| Ad / short | 3-expert panel (Curiosity, Pain, Voice); one round, fast |
| Email | Voice expert leads; light panel — one idea, one frame |
| Client-facing review | Show the full ledger — the reasoning IS the deliverable |

> **Frankenstein guard**: Never publish concatenated multi-expert paragraphs. Experts refine *blocks*; the spine-keeper writes the *body*. Multi-author bodies test worse than one coherent voice (system lesson: Sandwich = 4/10 disjointed).

---
## FINALIZE
After producing the deliverable, log it through the quality gate (skip only for pure brainstorming):
```bash
// turbo
python3 execution/chain_runner.py finalize "[what you produced] for <market>" \
  --expert luke-iha --skill luke-iha-copy-blocks --workflow expert-panel-deliberation \
  --type Content --intent N --expert-score N --adversarial N --factual N \
  --notes "Factual Grounding: N | Verification: PASS|N/A | Cache: WARM|COLD | Panel size: N"
```
If the output contains stats / prices / dates / named entities, FIRST build a proof-claims ledger and run the deterministic G5 gate (see `/copy-engine` Phase 5):
```bash
// turbo
python3 execution/verify_proof_ledger.py --draft <draft-file> --ledger .tmp/copy-engine/<slug>/proof-claims.md || echo "label/cut claims before delivery"
```
Grep finalize output for `QUALITY GATE BLOCKED` and do NOT deliver on a match (finalize exits 0 even when it blocks).

## Quality Gate
> **🛡️**: Did every weak block get a dedicated expert? Was every critique paired with a rewritten line (not an opinion)? Did the spine-keeper reject anything that broke velocity? Is the final draft ONE coherent voice, not stitched fragments? Blocks + experts invisible to the reader? If the panel just rubber-stamped the draft, it wasn't a real deliberation — re-run with sharper dissent.
