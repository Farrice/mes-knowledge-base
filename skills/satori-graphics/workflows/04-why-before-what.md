---
description: Concept-decision audit on every element — keeps, evicts, justifies. The rent test.
---

# /satori-why-before-what — Why-Before-What Decision Gate

Audit every element on a layout against the rent test: each element must serve concept, hierarchy, or psychology. Otherwise, it gets evicted. This is Satori's most foundational discipline — design as decision-making before expression.

## Pre-Flight Gate

**Use this when**:
- A layout feels cluttered but you can't articulate why
- A draft is ready and you want a pre-delivery decision audit
- You inherited / are reworking someone else's design
- A brief is unclear and you need to derive the design intent from the elements

**Do NOT use this when**:
- The layout is at sketch / concept stage with no committed elements yet (use `/satori-logo-concept` for logo briefs or do the one-sentence reduction directly)
- The design is purely typographic (use Kittl)
- You're in ideation mode — this is an audit/refinement workflow, not generative

## Skill Acquisition

Load:
- `genius.md` — GP-01 (Why-Before-What), GP-08 (One-Sentence Brief), GP-09 (Concept-Direction-First)
- `references/source-quotes.md` — Satori's verbatim phrasing on the rent test

## Execution

### Step 1: Lock the One-Sentence Brief

Before auditing elements, the brief must exist in one declarative sentence.

**Format**: *"A [thing] that [verb] [audience] [outcome/feeling]."*

If a one-sentence brief exists, document it. If not:
- Examine the layout
- Infer what it's *trying* to say
- Write the one-sentence brief
- Confirm with stakeholder if possible

If you cannot write a defensible one-sentence brief, **halt the audit**. The design has no foundation; route back to brief refinement.

### Step 2: Lock the Visual Primitive

Identify the visual primitive in use:
- Vertical lines / horizontal lines / curves / sharp angles / asymmetry / symmetry / hand-drawn / geometric

Document: which primitive is in use? Is it consistent with the one-sentence brief?

If the primitive contradicts the brief, that's a foundation issue — flag and propose primitive alignment.

### Step 3: Element Inventory

List every element on the layout. Group by category:
- **Typography elements**: headline, subheads, body, captions, labels, CTA
- **Image elements**: photos, illustrations, icons, patterns
- **Structural elements**: rules / lines, frames, dividers, badges
- **Decorative elements**: backgrounds, gradients, textures, ornaments
- **Brand elements**: logo, brand mark, taglines

Number each element (E1, E2, …) for the audit table.

### Step 4: Run the Rent Test

For each element, document one of three reasons:

| Reason | Test |
|---|---|
| **Concept** | Does this serve the central idea / metaphor / one-sentence brief? |
| **Hierarchy** | Does this guide the eye to the leverage point or support the journey? |
| **Psychology** | Does this engineer a specific emotional / cognitive response? |

If you cannot write a non-aesthetic reason in one sentence, the element fails the rent test.

**Output table**:

| # | Element | Reason category | Reason (one sentence) | Verdict |
|---|---|---|---|---|
| E1 | Headline "..." | Hierarchy | Largest element; pulls eye first | KEEP |
| E2 | Top-right ornament | — | — | **EVICT** |
| E3 | Vertical rule between columns | Hierarchy | Separates sections, reinforces vertical primitive | KEEP |
| ... | ... | ... | ... | ... |

### Step 5: Justify the Keeps

For every KEEP, the reason must be **non-aesthetic**. "Looks cool" / "balances the composition" / "fills the corner" all fail. Rewrite weak reasons:

| Weak reason | Strong reason |
|---|---|
| "Balances the composition" | "Anchors the eye journey at the closing point before CTA" |
| "Looks more designy" | "Reinforces the angular visual primitive established by the headline" |
| "Adds visual interest" | "Creates re-engagement at the scroll-fall-off zone" |
| "Fills the corner" | "Counters edge tension created by the bleed image" |

If you cannot strengthen a weak reason, demote KEEP → EVICT.

### Step 6: Process the Evictions

For each EVICT element:
- **Remove** from the layout
- **OR** redesign with a defensible reason
- **OR** flag for stakeholder discussion if it represents a brief / brand / legal constraint

Do not keep an element on the layout because "the client wants it" without documenting WHY the client wants it. If the client's reason holds, it's a KEEP with reason "client constraint: [reason]." If the client's reason doesn't hold, surface that as a brief-conversation item.

### Step 7: Multi-Job Audit

Some elements do two jobs (concept + hierarchy, or psychology + hierarchy). Verify both jobs are intentional.

If an element does three jobs, audit for overload — overloaded elements weaken on every job. Consider splitting into two elements with single jobs each.

### Step 8: Output the Audit

```markdown
# Why-Before-What Audit — [layout name]

## Foundation
- **One-sentence brief**: "..."
- **Visual primitive**: [...]
- **Primitive aligned to brief?**: yes/no

## Element Inventory
[Numbered list — E1 through En]

## Rent Test Results

| # | Element | Reason category | Reason (one sentence) | Verdict |
|---|---|---|---|---|
[full table]

## Eviction List
- E_: [reason for eviction]
- E_: [reason for eviction]

## Strengthening List
- E_: weak reason "[old]" → strong reason "[new]"

## Multi-Job Audit
- E_: does jobs [X + Y] — both intentional? [yes/no]
- E_: doing 3 jobs — propose split? [yes/no]

## Action List
[Specific changes a designer can implement]

## Foundation Fix Required?
[If brief or primitive unclear, route to: brief reduction / primitive lock-in]
```

## Content Type Adaptations

| Content type | Common eviction targets | Common strengthening targets |
|---|---|---|
| **Web hero** | Decorative background gradients without concept tie | Hero copy with weak hierarchy reason ("balances headline") |
| **Listing reel** | Generic "luxury" badges / icons | Price tag with weak reason ("for info") → strengthen to "leverage point for buyer scan" |
| **Streetwear poster** | Faux-vintage textures without concept | Disruption elements with weak reason ("looks cool") → strengthen to "memory encoding via resolve-something" |
| **Pitch deck** | Stock corporate icons | Section dividers with weak reason ("separator") → strengthen to "rhythm beat for temporal flow" |
| **Newsletter visual** | Decorative pull quotes | Imagery with weak reason ("matches topic") → strengthen to "predictive empathy cue" |
| **Logo presentation** | Background patterns on context mockups | Concept-iteration grids with weak reason ("show variations") → strengthen to "comparison framing for client" |

## Output Requirements

Audit must include:
1. Foundation check (one-sentence brief + visual primitive aligned)
2. Complete element inventory (no element skipped)
3. Rent test verdict per element with reason category + one-sentence reason
4. Eviction list with specific elements and reasons
5. Strengthening list (weak reasons rewritten as strong)
6. Multi-job audit
7. Action list — executable changes
8. Foundation fix flag if brief / primitive unclear

## Quality Gate (Genius Rubric)

- [ ] **One-sentence brief documented** (no audit without foundation)
- [ ] **Every element evaluated** (no skipped elements)
- [ ] **No aesthetic reasons accepted** ("looks good" / "balances" → strengthened or evicted)
- [ ] **Eviction list executed** (or flagged for stakeholder review with reason)
- [ ] **Action list executable** (specific element + change, not vague directives)

## Source Grounding

> *"A competent designer treats every element like it has to pay rent. If it doesn't serve a purpose, then nine times out of 10, it's going to get evicted."* — Satori

> *"This is the essence of the why before the what mindset. It's the decision that comes before the decoration or the design aspects."* — Satori
