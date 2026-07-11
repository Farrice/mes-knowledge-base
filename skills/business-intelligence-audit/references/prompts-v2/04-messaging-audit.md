---
name: "Messaging Audit"
source_prompt: "skills/business-intelligence-audit/references/prompts/04-messaging-audit.md"
skill: business-intelligence-audit
standard: structure-pure-v2
refactored: 2026-07-11
---

# Prompt 04: Messaging Audit

> Analyze copy, positioning, and conversion architecture.

---

## Purpose

Evaluate the quality and effectiveness of messaging across key pages. Identify copy weaknesses and positioning opportunities.

---

## Input Required

- **Key page URLs** (homepage, sales page, about page)
- **Business Scan output** (for context)

---

## Execution Protocol

```
You are auditing this business's messaging against proven copywriting principles (specificity, surprise, emotional resonance).

Conduct a comprehensive messaging audit on [COMPANY].

## Instructions

1. Extract key pages (homepage, main sales/service page, about page)
2. Analyze each element against the Three Rules Test
3. For every major claim, run the "Zoom In" Test for concreteness
4. Identify quick wins and systemic issues

## The Three Rules Test

- Specific: Does it avoid generic language? Would a competitor say the exact same thing?
- Surprising: Does it violate expectations? Is there tension or conflict?
- Emotional: Does it speak to identity, not just features?

## The "Zoom In" Test

For each major claim, assess concreteness: is it abstract ("we help businesses grow") or is it concrete (specific, sourced number/outcome/timeframe actually stated by the business)? Never invent a concrete number to illustrate the fix — pull the improvement from what the business could truthfully claim, or flag that no concrete proof exists yet.
```

---

## Output Contract

- **Executive Summary:** one paragraph verdict — working or not, and why
- **Headline Analysis table:** every key page scored on Specific/Surprising/Emotional + composite /10
- **Value Proposition Audit:** clarity, differentiation, credibility, each with a score /10
- **Proof Architecture table:** six proof types assessed (testimonials, case studies, metrics/data, logos, press/media, certifications)
- **CTA Analysis:** primary CTA, copy quality, friction, urgency
- **Funnel Gaps:** assessed across Awareness→Interest, Interest→Desire, Desire→Action
- **Zoom In Test table:** claims marked abstract or concrete with a real (not invented) improvement path
- **Top 5 Messaging Issues:** each paired with a specific fix
- **Quick Wins:** changes deployable within a week, each with expected impact stated in terms actually inferable from the audit (no invented percentages)

---

## Output Skeleton

```
### Executive Summary
[one paragraph: is this messaging working, and why]

### Headline Analysis

| Page | Headline | Specific? | Surprising? | Emotional? | Score /10 |
|------|----------|-----------|-------------|------------|-----------|
| [page] | [headline text] | [yes/no] | [yes/no] | [yes/no] | [score] |

### Value Proposition Audit
- Clarity: [can a visitor understand what they do in 5 seconds — yes/no + why]
- Differentiation: [is it clear why them vs. alternatives]
- Credibility: [is the claim believable and backed up]
- Score: [x]/10

### Proof Architecture

| Proof Type | Present? | Quality | Recommendation |
|------------|----------|---------|----------------|
| Testimonials | [y/n] | [assessment] | [fix] |
| Case Studies | [y/n] | [assessment] | [fix] |
| Metrics/Data | [y/n] | [assessment] | [fix] |
| Logos | [y/n] | [assessment] | [fix] |
| Press/Media | [y/n] | [assessment] | [fix] |
| Certifications | [y/n] | [assessment] | [fix] |

### CTA Analysis
- Primary CTA: [what it is, and whether it's clear]
- CTA Copy: [generic or specific — quote it]
- Friction: [perceived commitment level]
- Urgency: [any scarcity/urgency elements present]

### Funnel Gaps
1. Awareness → Interest: [does messaging hook attention]
2. Interest → Desire: [does it build wanting]
3. Desire → Action: [does it make action easy]

### The "Zoom In" Test

| Claim | Abstract or Concrete? | Improvement |
|-------|------------------------|-------------|
| [claim quoted from source] | [abstract/concrete] | [a truthful, sourced concretization — not an invented number] |

### Top 5 Messaging Issues

1. [Issue] → [specific fix]
2. [Issue] → [specific fix]
3. [Issue] → [specific fix]
4. [Issue] → [specific fix]
5. [Issue] → [specific fix]

### Quick Wins

1. [specific change + realistic expected impact]
2. [specific change + realistic expected impact]
3. [specific change + realistic expected impact]
```

---

## Quality Gate

- [ ] Every score (/10) is paired with a one-line rationale, never a bare number
- [ ] Zoom In Test table contains zero invented statistics — every "concrete" suggestion is either sourced from the business's actual claims or flagged as "needs real data to support"
- [ ] Top 5 Issues are ranked by impact, not listed in extraction order
- [ ] Every Quick Win is achievable within a week with no new data collection
- [ ] Proof Architecture table has all six rows filled, none skipped
