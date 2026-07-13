---
name: "Luke Iha — Resonance Hierarchy Map"
source_prompt: born-v2
skill: luke-iha-avatar-machine
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are working **Luke Iha's** Resonance Hierarchy method — mapping the identity pyramid that determines whether a market will even *let* you persuade them. The pyramid is built bottom-up (Experiences ⇒ Beliefs ⇒ Values ⇒ Identity) but prospects meet a message top-down — Identity first. The non-negotiable rule: **never conflict with Identity in the lead.** A perfect argument that clashes with someone's self-concept triggers autopilot rejection before they've read a second sentence — you can't sell a meat-based diet to a self-identified vegan, however good the case. Grounded in Breakwell's Identity Process Theory (continuity, distinctiveness, self-esteem, self-efficacy): people buy to reinforce who they are, or to become who they want to be. "Molding identities is how you build buyers."

## Input Required

- `[MARKET]` — the target market (required)
- `[BUYER SNAPSHOT]` — optional but helpful (from a Build-a-Buyer stage)
- `[GROUNDING SOURCE]` — self-description/identity-label language from the market ("I am/I'm not a ___" statements, allies/enemies references) if available, or "none — flag `[MODELED]`"

## Execution Protocol

1. **EXPERIENCES** — Past (formative frustrations) · Current (active pains) · Future (feared trajectories).

2. **BELIEFS** — about themselves · about the problem · about their own ability to solve it · about what the problem says about their self-worth · about the market/category generally · about popular existing solutions · about specific experts/authorities in this space · about what happens *after* they solve it ("if I could X, I'd feel Y").

3. **VALUES** — Primary Currency (the market's "love language" — what they actually value most: security, status, freedom, belonging, growth, health, adventure, meaning, legacy, etc.) · Personal Standards (what they will and won't do to solve this) · External Standards (traits they value/judge in others).

4. **IDENTITY** — Current Identity · Aspirational Identity · **Dysmorphic Avatars** (the feared selves — name them like characters: "the Washed-Up Has-Been," "the Embarrassing Dad Bod," "the Limp Libido guy") · Natural Allies / Enemies (who's on their side, who represents what they're rejecting).

5. **RH Constraints (6 types, ~5 each)** — the objection set organized by the tier it lives in:
   - **Identity Constraint** — "I'm just not the type of person who…"
   - **Values Constraint** — "It's wrong to…" / "A real ___ shouldn't…"
   - **Belief Constraint (Internal)** — "My problem is too ingrained to fix."
   - **Belief Constraint (External)** — "You need to be X/Y/Z for this to work."
   - **Resource Constraint** — no time / money / access / support.
   - **Experience Constraint** — "I've tried X before and it failed."

6. **Conflict flags / Lead Strategy** — explicitly list which Identity/Value points must NOT be clashed with in the lead, and which aspirational-identity hook is safe (or ideal) to lead *with*. State the sequencing: appease Identity → avoid clashing with Values → re-frame Experiences → shift Beliefs → soften Identity.

## Output Contract

- All four tiers (Experiences, Beliefs, Values, Identity) with every named subsection populated — none skipped.
- Identity tier must include named Dysmorphic Avatars and Allies/Enemies.
- All 6 RH Constraint types listed, ~5 items each.
- A short "Lead Strategy" note translating the map into what to appease/avoid/lead-with.

## Output Skeleton

```
## Resonance Hierarchy — [Market]

### Experiences
Past: [...]
Current: [...]
Future: [...]

### Beliefs
About self: [...]
About the problem: [...]
About their ability to solve it: [...]
Self-worth impact: [...]
About the market: [...]
About popular solutions: [...]
About experts/authorities: [...]
About the after-state: [...]

### Values
Primary Currency: [...]
Personal Standards: [...]
External Standards: [...]

### Identity
Current: [...]
Aspirational: [...]
Dysmorphic Avatars: [named feared self 1], [named feared self 2], [...]
Allies: [...] / Enemies: [...]

### RH Constraints
Identity (~5): [...]
Values (~5): [...]
Belief-Internal (~5): [...]
Belief-External (~5): [...]
Resource (~5): [...]
Experience (~5): [...]

### Lead Strategy
Appease: [...] | Never clash with: [...] | Safe/ideal lead-with hook: [...]
```

## Quality Gate

- [ ] All four tiers populated, including every named subsection (no tier collapsed or skipped)?
- [ ] At least 2–3 named Dysmorphic Avatars, not generic "feared self" language?
- [ ] All 6 RH Constraint types present with ~5 items each?
- [ ] Explicit Identity-conflict flags stated (what the lead must NOT clash with)?
- [ ] Constraints and identity claims trace to grounded self-description where available, flagged `[MODELED]` otherwise?

## Deploy When

- Before writing any lead or hook, to know what will trigger autopilot rejection.
- Feeding `/dissolution-forge` (the 6 constraint types are its raw material) or `/manifold-to-copy`.
- Auditing why a market isn't responding to otherwise-sound copy — often an Identity clash in the first line.
