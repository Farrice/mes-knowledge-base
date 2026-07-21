---
description: The advanced contrast tier as a standalone play — name a learned association the audience holds (type-psychology, symbol-emotion, genre-concept) and deliberately invert it for memorability that serves the message
---

# 25 — Expectation Flip

> **/satori-expectation-flip** — Psychology, emotion, and concept contrast: subvert one learned association on purpose. The violated expectation is the pause that forms the memory (GP-03 by other means).

> *"To achieve this, you first need to understand psychology of graphic design so you can then twist and manipulate it in your work."* — Satori

The teal skull: a death symbol in bright, playful, uplifting color — it reads joyful and lodges precisely because it violates the symbol. The NHS campaign: humor carrying a deadly-serious message — memorable AND relatable. The narrow serif in an urban hip-hop narrative. One flip, deliberately chosen, serving the message.

## Pre-Flight Gate

**Use this when**:
- Memorability is the brief's explicit job (awareness campaigns, brand moments, scroll-stoppers, launch assets)
- A design is competent but forgettable — basic + intermediate contrast present, nothing lodges
- Category conventions are so uniform that obeying them guarantees invisibility
- Emotional briefs where information alone won't move anyone (pairs with GP-16 technique 7)

**Do NOT use this when**:
- The audience doesn't hold the norm you want to flip — no expectation, no violation, no effect
- Trust-first surfaces where subversion reads as unreliability (legal, medical UI, checkout flows)
- The flip would contradict the message (a confusing flip fails GP-17 — if it needs explaining, it failed)
- You haven't verified the association's cultural read across the actual audience (Cultural Connotation Check — validate symbols with lived experience before shipping)
- More than one flip is tempting — two flips = noise; this is a one-move play

## Skill Acquisition

```
Load: skills/satori-graphics/genius.md
  ├─ GP-20 (Contrast Stack — advanced tier rules)
  ├─ GP-03 (Memory Encoding — why the violated expectation lodges)
  ├─ GP-14 (Feeling-Before-Information — the audience gate)
  └─ GP-17 (Perception Gap — the failure mode of a confusing flip)
Load: skills/satori-graphics/references/contrast-stack.md   # Tier 3 section
```

## Execution

### Step 1 — Name the Norm (in writing, with evidence)

What learned association does THIS audience hold? Sources: category conventions (what every competitor does), symbol psychology (skull = death, serif = luxury/tradition), genre expectations (hip-hop = bold sans), emotional register (charity = solemn). One line: `NORM: [audience] expects [element] to mean/feel [association]`. If you can't evidence the norm from the audience's world, halt — you'd be flipping an expectation nobody holds.

### Step 2 — Choose the Flip Axis (one of three)

| Axis | Move | Watched exemplar |
|---|---|---|
| **Psychology** | Element used AGAINST its learned connotation | Serif in urban hip-hop; skull in teal/pink/playful yellow |
| **Emotion** | Two opposing feelings on one design | NHS: humor × smoking-around-children; movie poster: love × sadness (+ the crack in the ice) |
| **Concept** | The whole treatment contradicts the expected treatment | Flat lackluster tech poster rebuilt 3D-modern; premium-minimal vs. rustic-hectic menu |

Pick ONE. Write the inversion: `FLIP: instead, [element/treatment] will [inverted association]`.

### Step 3 — The Service Gate (cleverness check)

Three questions, all must pass:
1. **Does the flip serve the communication problem?** (NHS humor makes a serious message spreadable; it doesn't mock it)
2. **Does the flipped read still transmit the message without narration?** (GP-17 — run a mental sequence-recall)
3. **Does the audience gate hold?** (GP-14 — the flip's net feeling matches who's receiving it; validate cultural connotations with someone holding the lived context if the symbol is culture-loaded)

Fail any → return to Step 2 or log "no flip — norm-compliant by decision" and exit. That exit is a PASS, not a failure.

### Step 4 — Engineer the Straight Field

A flip only reads against a straight field: everything else in the design must OBEY expectations so the one violation is unmissable. The skull design works because the composition around it is conventional poster grammar. Inventory the other elements; keep them norm-compliant (this is the zonal rule — the flip is the one loud zone).

### Step 5 — Output

Execution prompt: `references/prompts-v2/expectation-flip-spec.md`

## Content-Type Adaptations

| Surface | Typical flip | Caution |
|---|---|---|
| **Awareness/campaign** | Emotion (humor × gravity, hope × loss) | Never mock the cause; the flip carries the message further, not sideways |
| **Brand identity** | Psychology (type/symbol against category) | The flip becomes the brand's permanent signature — commit like the red-lens system (HOF-07) |
| **Social hooks** | Concept (treatment nobody expects in the feed) | Frame 1 only; the body content plays straight |
| **Poster/merch (MyBPM)** | Psychology (streetwear thrives on symbol inversion) | Cultural connotation check is mandatory |
| **Editorial** | Emotion (bittersweet pairings) | The crack-in-the-ice move: plant one small tell of the second emotion |
| **Product/UI** | Rare — micro-flips only (playful copy in a formal flow) | Trust surfaces mostly forbid flips |

## Output Requirements

An **Expectation-Flip Spec**: (1) the norm with audience evidence, (2) the chosen axis + inversion line, (3) service-gate verdicts (all three questions answered), (4) the straight-field inventory (what stays conventional so the flip reads), (5) execution directives (specific element treatments), (6) the no-flip exit if taken, with reason. One flip maximum.

## Quality Gate

Guards anti-patterns **#14 information over emotion**, **#15 explanation-required**, **#16 feeling-audience mismatch**.

- [ ] Norm evidenced from the audience's world, not assumed
- [ ] Exactly one flip (or a logged no-flip decision)
- [ ] Service gate passed — the flip carries the message, doesn't replace it
- [ ] Cultural connotation validated for culture-loaded symbols
- [ ] Straight field engineered — everything else obeys expectations
- [ ] Message transmits without narration (mental sequence-recall run)

## Related Workflows

- **`/satori-contrast-stack`** (22) — the parent system; this is its Tier-3 deep-dive
- **`/satori-memory-encoding`** (08) — sibling memory mechanism (metaphor/absence/swap); choose flip OR encode, rarely both
- **`/satori-concept`** (16) — upstream when the flip should BE the concept (what-if, hidden truth)
- **`/satori-perception-gap`** (18) — post-draft: prove the flip reads without explanation
- **`/novelty-forge`** (Kallaway) — cross-expert stack: illusion-of-novelty framing for the flip's rollout copy
