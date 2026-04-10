---
description: Generate 10+ reversed-causation insight vectors from a single market's dominant beliefs
---

# Reverse Causation Engine

Luke Iha's highest-leverage vector type, deployed as a dedicated workflow. Takes the audience's strongest "X causes Y" beliefs and systematically investigates whether the causal arrow can be flipped. Produces a ranked set of reverse-causation vectors with naming and proof pathways.

---

## Inputs Required

1. **Market/Niche** — What domain are we flipping arrows in?
2. **Product/Offer** — What are we selling? (Determines which reversals are commercially useful)
3. **Audience Causal Beliefs** — List 5-10 "X causes Y" beliefs the audience holds (from Mental Model Map or direct input)
4. **Research Access** — Can we verify reversals, or are we working from logic and observation?

---

> **🔒 Pre-Flight Gate**: This workflow focuses on ONE vector type. For full systems-grammar mining, use `/insight-vectors` instead.

## Phase 1: Belief Inventory

List every "X causes Y" belief held by this market:

| # | Audience Believes | Strength (1-10) | Source of Belief | How Widely Held |
|---|-------------------|-----------------|------------------|-----------------|
| 1 | "X causes Y" | | [doctors / media / culture / lived experience] | [universal / common / niche] |
| 2 | ... | | | |

**Minimum**: 8 causal beliefs. Dig deep — include beliefs they hold unconsciously.

---

## Phase 2: Arrow Flip Analysis

For each belief, investigate the reversal:

| # | Original: X → Y | Reversed: Y → X | Plausible? | Mechanism |
|---|-----------------|------------------|------------|-----------|
| 1 | "[cause] leads to [effect]" | "[effect] actually produces [cause]" | [yes/no/partially] | [what biological/structural/systemic mechanism could explain the reversal?] |

### For each plausible reversal, develop:

1. **The Reversal Statement**: "You're not [suffering] because of [believed cause]. Your [believed cause] is [happening] because of [actual root]."
2. **The Mechanism Bridge**: What specific process connects Y back to X?
3. **The Audience Experience Match**: Can the audience verify this matches their lived experience?
4. **The Research Support**: Is there any supporting evidence (studies, data, expert opinion)?

---

## Phase 3: SIN Filter

| # | Reverse Vector | Simple (1-10) | Intuitive (1-10) | New (1-10) | Total | Pass? |
|---|---------------|---------------|-------------------|------------|-------|-------|
| 1 | | | | | /30 | ≥21? |

**Intuitive scoring note for reverse causation**: A high-intuitive reversal makes the audience think "I ALWAYS felt like that was off." A low-intuitive reversal makes them think "Wait, that doesn't sound right." Aim for the former.

---

## Phase 4: Vicious Cycle Extension

The most powerful reverse-causation vectors reveal a VICIOUS CYCLE:
- X → Y → (makes X worse) → (Y intensifies) → trapped

For each SIN-passing reversal, investigate:
- Does the reversal create a self-reinforcing loop?
- If yes, map the loop and name it (this becomes a named mechanism)
- If no, the reversal is still valuable but solo (not looped)

**Loop Mapping Template**:
```
[Starting condition] → [causes Y] → [Y produces X] → [X worsens starting condition] → repeat
Name: "[The _____ Loop/Trap/Spiral]"
```

---

## Phase 5: Characterization + Deployment

For each finalist (3-5 vectors):

| Vector | Characterization Name | Discovery Story (30 sec) | Best Deployment |
|--------|---------------------|-------------------------|-----------------|
| [reversal statement] | [2-3 word name] | [conversational narrative seed] | [hook? mechanism? content angle? all?] |

---

## Output Format

```markdown
# Reverse Causation Report: [Market]

## Belief Inventory
[8-10 causal beliefs with strength scores]

## Plausible Reversals ([N] of [total])
[Each with reversal statement, mechanism bridge, experience match, and research support]

## SIN-Filtered Finalists

### [Vector Name 1]
- **Original belief**: "[audience thinks] X → Y"
- **Reversal**: "[reality] Y → X"
- **Mechanism**: [how the reversal works]
- **Vicious Cycle?**: [Yes → loop map / No]
- **SIN Score**: [X/30]
- **Proof pathway**: [what research/evidence could verify this]

### [Vector Name 2]
[same format]

## Stack Recommendation
[How to sequence these reversals for maximum cumulative impact]

## Deployment Map
| Vector | As Mechanism | As Hook | As Content | As Ad Angle |
|--------|-------------|---------|------------|-------------|
| [name] | [how] | [how] | [how] | [how] |
```

---

## Quality Gate

- ☐ At least 8 causal beliefs inventoried
- ☐ At least 3 plausible reversals with mechanism bridges
- ☐ SIN-filtered finalists have characterization names
- ☐ Vicious cycle extension explored for all finalists
- ☐ No fabricated reversals — only plausible ones supported by mechanism or evidence
- ☐ Deployment map shows multiple use cases per vector

> **🛡️ Anti-Pattern Check**: Reverse causation must be PLAUSIBLE, not clever. "You're not tired because you don't sleep — you don't sleep because you're tired" is CIRCULAR, not reversed. The reversal must introduce a new mechanism.
