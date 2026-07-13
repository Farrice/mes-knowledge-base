---
name: "Luke Iha — Suffering-Archetype Typing"
source_prompt: born-v2
skill: luke-iha-avatar-machine
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are working **Luke Iha's** Suffering-Archetype method — a fast read on tone, approach, and how much accountability a market can hold, derived from where it sits on the Pain Matrix dimensions (stigma, control, urgency, measurability, emotional intensity, causal clarity). The archetype is a lens, not a cage — markets can straddle two; you name the dominant and note the secondary rather than forcing a single label.

## Input Required

- `[MARKET]` — the target market (required)
- `[PAIN MATRIX]` — the market's scored dimensions (required for a justified read; if absent, run a Pain Matrix pass first — this is derivation over real scores, not vibes)

## Execution Protocol

1. **Read the dominant archetype** from the market's pain profile, against the 9:
   - **The Shadow** — hidden, high-stigma pain (private medical, financial shame). Inner turmoil + shame.
   - **The Warrior** — believes they can control/overcome; some causal understanding (saving a marriage via communication; optimizing a funnel).
   - **The Guardian** — urgency to protect others; powerless alone; wants measurable results (a parent with a child's allergy; disaster repair).
   - **The Phoenix** — emotionally intense + stigma; seeking to rise and measure progress (battling depression/addiction).
   - **The Explorer** — complex, poorly-understood, low-visibility problems; moderate urgency (autoimmune; mastering complex software).
   - **The Sisyphus** — recurring problem, moderate intensity, believes they have control but can't sustain progress (workout consistency, procrastination).
   - **The Olympian** — measurable goal, strong personal control, moderate-high urgency (lose weight for an event, raise GPA).
   - **The Alchemist** — emotionally charged + stigma; believes in self-mastery transformation (overcoming limiting beliefs, inner peace).
   - **The Seeker** — unclear causes, moderate-high urgency, some control but no direction (conflicting diet info, career path).

2. **Justify** the read with 2–3 specific dimension scores (e.g., "Stigma 8 + Emotional Intensity 9 + a rising trajectory → Phoenix"). A read with no dimension citation is a vibe, not a typing.

3. **Note the secondary** archetype if the market genuinely straddles two.

4. **Translate to directives** — tone, empathy level, proof strategy, locus-of-control handling, and what to explicitly avoid for this archetype.

## Output Contract

- Dominant archetype + 2–3 dimension-score justification.
- Secondary archetype noted if applicable (or explicitly "no meaningful straddle").
- A 4–5 line directive block: tone, empathy level, proof strategy, locus-of-control handling, what to avoid.

## Output Skeleton

```
## Suffering Archetype — [Market]

Dominant: [one of the 9]
Justification: [2–3 dimension scores + reasoning]

Secondary: [archetype, or "none — clean single-archetype read"]

### Directives
Tone: [...]
Empathy level: [...]
Proof strategy: [...]
Locus-of-control handling: [...]
Avoid: [...]
```

## Quality Gate

- [ ] Dominant archetype is justified by specific dimension scores, not asserted from impression alone?
- [ ] A secondary archetype is considered and either named or explicitly ruled out (not silently skipped)?
- [ ] All 5 directive lines (tone/empathy/proof/locus-of-control/avoid) are populated and archetype-specific, not generic?
- [ ] The typing draws from an actual Pain Matrix, not from market stereotypes?

## Deploy When

- Fast tone/approach calibration before drafting, when the full Manifold isn't needed.
- Feeding `luke-iha-unaware-ads` or any downstream tone decision.
- Sanity-checking that a draft's tone actually matches the market's archetype (e.g., catching Warrior-tone copy applied to a Shadow market).
