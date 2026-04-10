---
description: Diagnose existing copy or campaigns — which insight vector types are used, which are missing, and where the audience coverage gaps are
---

# Insight Vector Audit

Reverse-engineer any existing copy, campaign, or content piece to identify which insight vector types are present, which are missing, and where structural gaps leave the audience unconvinced. Produces a diagnostic report with specific prescriptions.

---

## Inputs Required

1. **Copy/Content to Audit** — Paste the full text or provide the asset
2. **Product/Offer Context** — What is being sold? (For relevance assessment)
3. **Target Audience** — Who is this aimed at?
4. **Performance Data** (optional) — CTR, conversion rate, engagement metrics, or qualitative feedback

---

> **🔒 Pre-Flight Gate**: Load `genius.md` § Decision Framework for vector type reference. Load `references/insight-vector-framework.md` if needed.

## Phase 1: Vector Identification

Read the copy line by line. For each segment, identify:

| Copy Segment | Vector Type Present? | Vector Quality (1-10) | Notes |
|-------------|---------------------|----------------------|-------|
| [Quote segment 1] | [Reverse Causation / Multiple Causation / etc. / NONE] | [quality of execution] | [what works or doesn't] |
| [Quote segment 2] | ... | ... | ... |

### Classification rules:
- A **claim** is NOT a vector. "Our product boosts metabolism" = claim. "Your fat is what slows your metabolism" = vector.
- A **feature** is NOT a vector. "Contains 12 clinically-tested ingredients" = feature. No map disruption.
- A **story** might contain a vector. Look for the moment where the narrative reveals something the reader didn't know.
- A **statistic** might support a vector but isn't one alone. "80% of diets fail" = stat. "80% of diets fail because they trigger the muscle-loss spiral" = stat + vector.

---

## Phase 2: Coverage Analysis

### Vector Type Coverage Map

| Vector Type | Present? | Quality (1-10) | Example |
|-------------|---------|----------------|---------|
| **Reverse Causation** | ☐ Yes / ☐ No | | |
| **Multiple Causation** | ☐ Yes / ☐ No | | |
| **Hidden Condition** | ☐ Yes / ☐ No | | |
| **System Archetypes** | ☐ Yes / ☐ No | | |
| **Virtuous Cycle** | ☐ Yes / ☐ No | | |
| **Vicious Cycle** | ☐ Yes / ☐ No | | |
| **Leading Indicator** | ☐ Yes / ☐ No | | |
| **Hidden Constraint** | ☐ Yes / ☐ No | | |
| **False Assumption** | ☐ Yes / ☐ No | | |
| **Missing Variable** | ☐ Yes / ☐ No | | |
| **Model Limitation Reframe** | ☐ Yes / ☐ No | | |
| **Structural Revelation** | ☐ Yes / ☐ No | | |

### Coverage Score: [X]/12 vector types present

---

## Phase 3: Elaboration Analysis

For each vector that IS present, assess the 8-Fold Elaboration beats:

| Beat | Present? | Quality | Notes |
|------|---------|---------|-------|
| Paradoxical Question | ☐ Yes / ☐ No | | |
| UMP/UMS | ☐ Yes / ☐ No | | |
| Trigger | ☐ Yes / ☐ No | | |
| Testable Proof | ☐ Yes / ☐ No | | |
| Intensifiers | ☐ Yes / ☐ No | | |
| Myths & Mistakes | ☐ Yes / ☐ No | | |
| Cause | ☐ Yes / ☐ No | | |
| Resolution | ☐ Yes / ☐ No | | |

### Elaboration Score: [X]/8 beats present

---

## Phase 4: Diagnosis

### Overall Assessment
- **Vector Density**: [How many insight vectors per 500 words?]
- **Vector Diversity**: [How many different types?]
- **Elaboration Depth**: [How fully developed are existing vectors?]
- **Stack Coherence**: [Do the vectors point to the same conclusion?]

### Specific Diagnosis

**Why this copy [succeeds/struggles]:**
- [Specific reason 1, tied to vector presence or absence]
- [Specific reason 2]
- [Specific reason 3]

---

## Phase 5: Prescriptions

### Critical Additions (Must-Have)
For each missing vector type that would significantly strengthen the copy:

| Priority | Missing Vector Type | Specific Vector to Add | Where to Insert |
|----------|-------------------|----------------------|-----------------|
| 1 | [type] | [concrete vector sentence] | [specific location in the copy] |
| 2 | [type] | [vector] | [location] |

### Enhancement Upgrades (Nice-to-Have)
For existing vectors that could be strengthened:

| Vector Location | Current Quality | Enhancement | Expected Impact |
|----------------|----------------|-------------|-----------------|
| [quote/location] | [X/10] | [specific improvement] | [what it fixes] |

### Structural Recommendations
- [If beats are missing from elaboration — which to add]
- [If stacking is weak — which vectors to add for convergent certainty]
- [If opening hook is claim-based rather than vector-based — how to fix]

---

## Output Format

```markdown
# Insight Vector Audit: [Copy/Campaign Name]

## Summary
- **Vector Density**: [X] vectors per 500 words
- **Coverage Score**: [X]/12 vector types
- **Elaboration Score**: [X]/8 beats on strongest vector
- **Overall Grade**: [A-F with one-sentence justification]

## Vector Type Coverage Map [table]

## Diagnosis
[3-5 specific findings]

## Critical Prescriptions [table with priority]

## Enhancement Upgrades [table]

## Before/After Preview
[Take the weakest section of the copy and rewrite it with the highest-priority prescription applied — showing the concrete difference]
```

---

## Quality Gate

- ☐ Every segment of the copy has been classified (vector / claim / feature / story)
- ☐ Coverage map is complete (all 12 types assessed)
- ☐ At least 2 specific prescriptions with concrete vector sentences
- ☐ Before/after preview demonstrates a real improvement
- ☐ Diagnosis connects to performance issues (if data available)

> **🛡️ Anti-Pattern Check**: Don't recommend adding vectors that would make the copy feel forced. Vectors must be EARNED from the product's actual truth.
