---
name: "Luke Iha — Epiphany Threshold Belief Sets"
source_prompt: born-v2
skill: luke-iha-avatar-machine
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are working **Luke Iha's** Epiphany Threshold method — generating the minimum-viable insight that captures attention without tripping the bullshit detector. This operationalizes the Hegelian dialectic as a copy tool: **Thesis** (the obvious belief) → **Antithesis** (the outlandish opposite) → **Synthesis** (the Goldilocks hook). A belief sits on a spectrum from Obvious (0) to Outlandish (10): the **Boredom Zone (0–7)** is too obvious to earn attention; the **Epiphany Threshold (≈7)** is the minimum insight needed; the **Goldilocks Zone (7–9)** is surprising yet still believable; the **BS Limit (9+)** triggers instant rejection. Rule: **it's better to push toward outlandish than toward obvious** — the shallow end is where attention dies. Note the mimetic trap: every synthesis becomes the next market's thesis as it spreads (Reels/TikTok comments accelerate this), so calibrate against what's *currently* circulating, not last year's Goldilocks.

## Input Required

- `[MARKET]` — the target market (required)
- `[GROUNDING SOURCE]` — the market's real obvious/accepted beliefs and currently-circulating hooks (dossier or live FB Ad Library scan) if available, or "none — flag `[MODELED]`"
- `[GOAL]` — optional: cold ad hook / email subject / educational content / skeptical-sophisticated market — shifts which of the 4 categories to lean into

## Execution Protocol

1. **10 below-threshold beliefs** — obvious, common, Boredom-Zone statements about this market's problem/solution. These define the baseline you must escape; they are not deliverable hooks, they're the floor.

2. **10 over-BS-limit beliefs** — outlandish, unbelievable claims. These define the ceiling — the point past which the market's bullshit detector fires.

3. **10 Goldilocks-Zone beliefs (7–9)**, each with **explicit reasoning** for why it's surprising yet still believable. Draw from the 4 categories, and tag which category each belief uses:
   - **Inversion & Extremism** — flip the belief entirely, or push it to an extreme (e.g., "Over-moisturizing ages skin").
   - **Specific Exceptions & Hidden Factors** — the general truth holds, but a hidden factor/exception flips the outcome (e.g., "Boring her on the first date makes her chase you").
   - **Reframing the Goal** — question the goal itself, not the method (e.g., "Copywriters should aim to confuse, not clarify").
   - **False Dichotomy & Oversimplification** — a stark, deliberately oversimplified black/white contrast (e.g., "Women are attracted to jerks, not nice guys").

4. **Believability check** — run each Goldilocks belief against the 4 guardrails: **Plausibility** (challenges conventional wisdom without contradicting hard science) · **Implications** (doesn't imply real harm) · **Specificity** (a focused claim, not a broad generalization) · **Familiarity-vs-Novelty** (surprising but still grounded in something the market recognizes).

5. *(Optional)* **"Add sauce" pass** — turn the 3–5 strongest Goldilocks beliefs into actual hook headlines, ready to hand to the Maze Hooks or Vicious Hooks stage.

## Output Contract

- Three labeled sets of exactly 10 each: Below-Threshold, Over-BS-Limit, Goldilocks.
- Every Goldilocks item carries a category tag (one of the 4) and a reasoning line explaining why it clears the Threshold without crossing the BS Limit.
- Every Goldilocks item passes (or is revised until it passes) the 4-guardrail believability check — state pass/fail per item or per set if uniform.

## Output Skeleton

```
## Epiphany Threshold — [Market]

### Below-Threshold (Boredom Zone, 10)
1. [...]
...
10. [...]

### Over-BS-Limit (Outlandish, 10)
1. [...]
...
10. [...]

### Goldilocks Zone (7–9, 10, w/ reasoning)
1. [belief] — Category: [Inversion/Exception/Reframe/Dichotomy] — Why it lands: [reasoning]
...
10. [belief] — Category: [...] — Why it lands: [...]

Believability check: [pass/fail notes against Plausibility/Implications/Specificity/Familiarity-Novelty]

### Add Sauce (optional, 3–5 hook headlines)
[...]
```

## Quality Gate

- [ ] Exactly 10 items in each of the three sets, none blended together?
- [ ] Every Goldilocks item carries both a category tag and a reasoning line — not asserted without justification?
- [ ] Goldilocks items are genuinely surprising-yet-specific, not flat over-BS claims dressed up as insight?
- [ ] None of the Goldilocks items are actually under-threshold (obvious) beliefs mislabeled as insight?
- [ ] The set pushes toward outlandish rather than staying safe/obvious across the 10 Goldilocks items?

## Creative Latitude

This is the section of the Manifold with the most room to surprise. Push each Goldilocks belief as far toward the BS Limit as the guardrails allow — a "safe" Goldilocks set that reads more like the below-threshold set has failed the method even if it's technically labeled correctly. Mix categories across the 10 rather than leaning on one (a set that's all "Specific Exceptions" reads monotone). Where you have real market signal, calibrate the ceiling against what's *actually* circulating right now, not a generic sense of "outlandish."

## Deploy When

- Building the LEAD of a VSL, ad, or email — this is where hooks come from.
- Feeding `/market-pickup-lines` (Goldilocks filter) or `luke-iha-vicious-hooks` (viciousness pass).
- Diagnosing why a hook is falling flat: check whether it's actually under-threshold, or has crossed the BS Limit.
