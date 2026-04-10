---
description: Rewrite existing copy with insight vectors injected at structural weak points
---

# Insight Copy Injector

Takes existing copy that makes CLAIMS and rewrites it with INSIGHT VECTORS — transforming "Here's what our product does" into "Here's a genuine aha moment that makes you need our product." This is the copywriting-specific deployment tool.

---

## Inputs Required

1. **Existing Copy** — The full text to be injected with insight vectors
2. **Copy Type** — VSL script, ad, email, landing page, social post, or sales letter
3. **Product/Offer** — What is being sold?
4. **Available Vectors** (optional) — Pre-generated insight vectors from `/insight-vectors`. If not provided, Phase 2 generates them on-the-fly.
5. **Performance Issues** (optional) — What's wrong with the current copy? Low CTR? Low conversion? High bounce?

---

> **🔒 Pre-Flight Gate**: If available vectors are not provided, run a quick mental-model snapshot from `genius.md` § Decision Framework before Phase 2.

## Phase 1: Copy Weakness Scan

Read the copy and flag every point where the copy CLAIMS rather than creates an insight:

| Line/Section | Current Copy | Classification | Weakness |
|-------------|-------------|----------------|----------|
| [location] | "[quote]" | CLAIM / FEATURE / VAGUE / VECTOR ✓ | [What's missing — no mechanism? No proof? No aha?] |

### Weakness Types:
- **CLAIM**: "Our product does X" — no mechanism, no insight
- **FEATURE**: "Contains 12 ingredients" — features without framework
- **VAGUE**: "Transform your life" — meaningless abstraction
- **VECTOR ✓**: Already functioning as an insight vector (leave alone or enhance)

**Target**: Identify 3-7 injection points where vectors would transform the copy.

---

## Phase 2: Vector Selection

For each injection point, select or generate the optimal vector type:

| Injection Point | Copy Weakness | Best Vector Type | Specific Vector |
|----------------|---------------|-----------------|----------------|
| Opening hook | CLAIM → needs paradoxical pull | Reverse Causation or False Assumption | [specific vector sentence] |
| Problem section | VAGUE → needs systemic explanation | Vicious Cycle or Hidden Constraint | [specific vector] |
| Mechanism section | FEATURE → needs aha moment | Structural Revelation or Missing Variable | [specific vector] |
| Proof section | CLAIM → needs cognitive validation | Leading Indicator or Multiple Causation | [specific vector] |
| Close/CTA | VAGUE → needs urgency logic | Hidden Condition or Vicious Cycle | [specific vector] |

### Selection Rules:
- **Opening**: Use the most ATTENTION-grabbing vector (reverse causation, false assumption)
- **Problem**: Use vectors that name the INVISIBLE trap (vicious cycle, hidden constraint)
- **Mechanism**: Use vectors that explain the WHY (structural revelation, missing variable)
- **Proof**: Use vectors that the audience can VERIFY (leading indicator, multiple causation)
- **Close**: Use vectors that create URGENCY through logic (hidden condition, vicious cycle compounding)

---

## Phase 3: Injection Rewrites

For each injection point, write the before/after:

### Injection Point [N]: [Section Name]

**BEFORE** (Original — Claim/Feature/Vague):
> "[Original copy]"

**AFTER** (Rewrite — Insight Vector Injected):
> "[Rewritten copy with vector]"

**Vector Type Used**: [type]
**What Changed**: [1-sentence explanation of why this is stronger]

---

## Phase 4: Continuity Check

After all injections, read the full revised copy to ensure:

1. **Tonal continuity** — The vectors feel native to the copy's voice, not grafted on
2. **Logical flow** — Each vector builds on the previous one (stacking, not scattering)
3. **Density calibration** — 1 vector per 200-300 words is optimal. More = cognitive overload.
4. **Stack coherence** — All vectors point toward the same conclusion (your product)

If any injection breaks flow, revise for integration.

---

## Phase 5: Full Revised Copy

Produce the complete rewritten copy with all vectors injected, maintaining original structure where it works and only replacing weak sections.

---

## Output Format

```markdown
# Insight Copy Injection Report

## Scan Summary
- **Total injection points identified**: [N]
- **Weakness breakdown**: [X claims, Y features, Z vague, W existing vectors]
- **Vector density target**: 1 per [N] words

## Injection Map
[Table from Phase 2: injection points, vector types, specific vectors]

## Before/After Comparisons
[Phase 3 rewrites for each injection point]

## Full Revised Copy
[Complete text with all injections integrated]

## Performance Prediction
- **Expected impact on hook**: [what changes]
- **Expected impact on read-through**: [what changes]
- **Expected impact on conversion**: [what changes]
- **Biggest single improvement**: [which injection makes the most difference]
```

---

## Quality Gate

- ☐ At least 3 injection points identified and addressed
- ☐ Each injection uses a named vector TYPE (not just "better copy")
- ☐ Before/after comparisons show clear transformation from claim → vector
- ☐ Full revised copy reads as one cohesive piece (not Frankenstein)
- ☐ Vectors are grounded in product truth (no fabricated mechanisms)
- ☐ Vector density is calibrated (not oversaturated)

> **🛡️ Anti-Pattern Check**: Injected vectors must feel NATIVE to the copy. If a vector feels like it was "pasted in" — revise until seamless. Also check: no AI slop words (leverage, utilize, robust, etc.)
