---
description: Convert raw insight vectors into SIN-scored mechanism candidates with characterization names — bridge to Million Dollar Mechanisms
---

# Insight-to-Mechanism Bridge

Takes raw insight vectors from the Insight Vectors system and converts them into fully-formed mechanism candidates ready for the Million Dollar Mechanisms pipeline (SIN filter, Universal Mechanism Matrix positioning, characterization naming). This is the bridge workflow between the two Luke Iha skills.

---

## Inputs Required

1. **Insight Vectors** — 3-5 shortlisted vectors from `/insight-vectors` or `/reverse-cause`
2. **Product/Offer** — What are we selling?
3. **UMP/UMS Direction** — Problem mechanism or solution mechanism? (If not yet decided, this workflow will force the decision)
4. **Market Sophistication** — How many competing claims exist?

---

> **🔒 Pre-Flight Gate**: This assumes insight vectors have already been generated and SIN-filtered. If you're starting from scratch, run `/insight-vectors` first.

## Phase 1: Vector → Mechanism Translation

For each insight vector, translate to mechanism language:

| Insight Vector | Vector Type | Mechanism Translation | UMP or UMS? |
|---------------|-----------|---------------------|-------------|
| [raw vector statement] | [reverse causation / hidden constraint / etc.] | "[The reason it works / fails is because] [mechanism explanation]" | [problem / solution] |

### Translation rules:
- **Reverse Causation** vectors → usually become UMPs (you flip the problem's cause)
- **Hidden Constraint** vectors → usually become UMPs (you name what's ACTUALLY blocking)
- **Missing Variable** vectors → can be UMP or UMS (the variable you measure or restore)
- **Virtuous/Vicious Cycle** vectors → become UMS (your product breaks/initiates the cycle)
- **Leading Indicator** vectors → become UMS positioned as diagnostic tools
- **Archetype** vectors → become UMS split by type

---

## Phase 2: Matrix Positioning

Place each mechanism candidate in the Universal Mechanism Matrix:

|  | Structure | Function | Element |
|--|-----------|----------|---------| 
| **Too Much** | [does this mechanism describe excess structure?] | [excess function?] | [excess element?] |
| **Too Little** | [deficient structure?] | [deficient function?] | [deficient element?] |
| **Out of Balance** | [misaligned structure?] | [competing functions?] | [blocking elements?] |
| **Dysfunctional** | [damaged structure?] | [hijacked function?] | [corrupted element?] |

**For each mechanism candidate**: Identify which matrix cell it fits. Mechanisms that don't fit any cell may need reframing.

---

## Phase 3: SIN Re-Score (Mechanism-Level)

Re-score now at the MECHANISM level (not vector level — mechanisms must pass independently):

| # | Mechanism | Matrix Position | Simple (1-10) | Intuitive (1-10) | New (1-10) | Total | Pass? |
|---|----------|----------------|---------------|-------------------|------------|-------|-------|
| 1 | | [e.g., Too Much × Function] | | | | /30 | ≥21? |

---

## Phase 4: Characterization Sprint

For each SIN-passing mechanism, generate 5+ name candidates:

### Naming Formulas:
- [Vivid Adjective] + [Body/System Part]: "Toxic Calcium," "Silent Inflammation"
- [Thing] + [Action Verb]: "Cortisol Switch," "Fatigue Loop"
- "The [Hidden/Secret/Forgotten] + [Effect]": "The Hidden Hunger Signal"
- [Surprising Noun] + [Domain]: "Sugar Brain," "Plastic Gut"

| Mechanism | Name 1 | Name 2 | Name 3 | Name 4 | Name 5 | Selected |
|----------|--------|--------|--------|--------|--------|----------|
| [mechanism description] | | | | | | |

### Name Quality Checklist:
- ☐ 2-3 words maximum
- ☐ Visual — creates an image
- ☐ Emotional — triggers a feeling
- ☐ Enemy-coded (UMP) or hero-coded (UMS)
- ☐ Dinner table test — would a non-expert remember it after one hearing?

---

## Phase 5: Mechanism Dossier

For each finalist mechanism, build the complete dossier:

```markdown
### [Mechanism Name]

**Origin Vector**: [which insight vector type generated this]
**Type**: [UMP / UMS]
**Matrix Position**: [cell]
**SIN Score**: [X/30]

**One-sentence mechanism**: [plain language explanation]

**Validation Triangle**:
- **Story**: [Does this mechanism have a natural "discovery story"?]
- **Hook**: [Does naming this mechanism create a hook?]
- **Visual Metaphor**: [Can you draw or describe this mechanism visually?]

**Discovery Story Seed (60 seconds)**:
[How would you tell this mechanism's origin in conversation?]

**Audience Suspicion Tapped**:
[What do they already half-believe that this mechanism names?]

**Competitive Uniqueness**:
[Has any competitor used this mechanism or a similar one? How is this different?]
```

---

## Output Format

```markdown
# Insight → Mechanism Bridge Report

## Input Vectors ([N] vectors processed)
[Brief list of input vectors with types]

## UMP/UMS Decision
[Direction chosen with justification]

## Mechanism Candidates

### Finalist 1: [Mechanism Name]
[Full dossier from Phase 5]

### Finalist 2: [Mechanism Name]
[Full dossier]

### Finalist 3: [Mechanism Name]
[Full dossier]

## Recommended Primary Mechanism
[Which one and why — with deployment recommendation]

## Handoff Ready For:
→ `/mechanism-validate` — for full validation
→ `/mechanism-copy` — for copy generation from mechanism
→ `/little-big-idea` — for product truth × desire intersection
```

---

## Quality Gate

- ☐ Each vector successfully translated to mechanism language
- ☐ Matrix positioning identified for all mechanism candidates
- ☐ SIN re-score completed at mechanism level (may differ from vector-level score)
- ☐ All finalist mechanisms have characterization names passing the 5-point test
- ☐ Validation triangle completed (story + hook + visual metaphor)
- ☐ Clear handoff recommendation to downstream Luke Iha workflows

> **🛡️ Anti-Pattern Check**: Mechanisms must be GROUNDED — no fabricated biology or invented processes. If the insight vector reveals a real pattern but the mechanism feels speculative, flag it and recommend research before use.
