---
name: "Customer Intelligence"
source_prompt: "skills/business-intelligence-audit/references/prompts/03-customer-intelligence.md"
skill: business-intelligence-audit
standard: structure-pure-v2
refactored: 2026-07-11
---

# Prompt 03: Customer Intelligence

> Identify who they actually serve (and who they're missing).

---

## Purpose

Understand the real customer beyond demographics—their posture, their internal logic, their actual needs. Identify underserved segments.

---

## Input Required

- **Business Scan output** (from Prompt 01)
- **Website content** (testimonials, case studies, about page)

---

## Execution Protocol

```
You are applying the Consumer Posture methodology (Dai Media) to build deep customer intelligence.

Based on extracted data for [COMPANY], identify:
1. Who they CLAIM to serve
2. Who they ACTUALLY serve (evidence-based)
3. Who they COULD serve (untapped segments)

## Instructions

1. Extract all customer-facing language (who they mention serving)
2. Analyze testimonials/case studies for ACTUAL customer profiles
3. Look for gaps between stated audience and proven audience
4. Apply the Three Dimensions Framework: Occupation in the World, Activity in the World, Thought Process in the World
```

---

## Output Contract

- **Stated vs. Proven vs. Underserved:** all three audience views present, not just the stated one
- **Three Dimensions Framework:** Occupation, Activity, and Thought Process each answered — not skipped even if evidence is thin (mark "insufficient evidence" where true)
- **Gap Analysis table:** four rows (Industry, Role/Title, Problem, Sophistication), stated vs. proven for each
- **Underserved Segments:** three named categories — adjacent, overlooked, premium
- **Recommendations:** minimum 3, each tied to a specific gap identified above

---

## Output Skeleton

```
### Stated Target Audience
- [who they say they serve, from marketing copy]
- Specificity: [specific / generic, with the phrase that shows it]

### Proven Customer Profile

**Dimension 1: Occupation in the World**
- [role, industry, context — drawn from testimonials/case studies]

**Dimension 2: Activity in the World**
- [daily rituals, where they spend time, what triggers the search for a solution]

**Dimension 3: Thought Process in the World**
- [self-belief, internal logic, what they'd never say out loud — flag "insufficient evidence" if not supportable]

### Gap Analysis

| Aspect | Stated Audience | Proven Audience | Mismatch? |
|--------|-----------------|-----------------|-----------|
| Industry | [value] | [value] | [yes/no + why] |
| Role/Title | [value] | [value] | [yes/no + why] |
| Problem | [value] | [value] | [yes/no + why] |
| Sophistication | [value] | [value] | [yes/no + why] |

### Underserved Segments

1. Adjacent Segment: [who is close but not targeted]
2. Overlooked Segment: [who has the problem but isn't spoken to]
3. Premium Segment: [who would pay more for a better version]

### Recommendations

1. [Messaging adjustment for current audience]
2. [New segment opportunity]
3. [Content/positioning move to attract ideal customer]
```

---

## Quality Gate

- [ ] All three Three-Dimensions fields answered with evidence, or explicitly flagged as unsupported
- [ ] Gap Analysis table has no blank cells
- [ ] Underserved Segments names three genuinely distinct groups, not restatements of the stated audience
- [ ] Every recommendation traces to a named gap or segment above it
- [ ] Proven Customer Profile is built from testimonials/case studies, not assumed from the stated audience

---

## Cross-Reference

Combine insights with:
- **Prompt 04 (Messaging Audit)** → align messaging to true customer
- **Prompt 09 (Recommendations)** → prioritize segment opportunities
