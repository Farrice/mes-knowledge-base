---
description: Deep Canvassing Research Sprint — 5-phase research pipeline producing a complete Belief Architecture Document grounded in real audience data via Perplexity deep research
---

# Deep Canvassing Research Sprint

**Produces**: A complete **Belief Architecture Document** — the definitive audience intelligence report for any market, grounded in real voice-of-customer data.

> **Load before executing**: `skills/david-mcraney-belief-change/genius.md`

> [!IMPORTANT]
> This workflow fires Perplexity research at multiple stages. Do NOT substitute training data for real research. Every belief claim must trace to a real source (forum post, Reddit thread, review, interview, social comment).

## When to Deploy

- Entering a new market where you don't understand why prospects resist
- Building foundational audience intelligence for any campaign or product launch
- Feeding into `/belief-creative-brief`, `/persuasion-copy`, `/threshold-campaign`, or `/belief-first-audience-intelligence`
- When existing ICP research tells you WHAT people want but not WHY they won't act

## Inputs Required

- **Audience**: Who are we researching? (niche, role, demographic, psychographic)
- **Category/Market**: What domain is this about?
- **Product/Offer** (optional): What are we trying to get them to adopt/buy/believe?

---

## Phase 1: Voice-of-Customer Research Mining 🔬

**Uses**: Perplexity deep research (mandatory)

### Execute

Fire 3 parallel Perplexity research queries:

**Query 1 — Direct Belief Mining**:
```
Search for: "[audience] beliefs about [category]" — find Reddit threads, Quora answers,
forum discussions, reviews, and social media posts where [audience] EXPLICITLY STATE
what they believe about [category]. I need their actual words, not summaries.
Look in: Reddit (r/[relevant subreddits]), Quora, industry forums, Amazon reviews,
Twitter/X threads, LinkedIn comments, YouTube comments.
Return: 15-20 direct quotes with source attribution.
```

**Query 2 — Objection & Resistance Mining**:
```
Search for: Why [audience] refuses/resists/avoids/hates [product/category/approach].
Find complaints, objections, negative reviews, "why I quit" posts, "why I won't" posts.
I need the REASONS they give in their own words.
Return: 15-20 resistance statements with source attribution.
```

**Query 3 — Identity & Tribe Mining**:
```
Search for: What does [audience] identify as? What groups, communities, movements,
philosophies do they belong to that might conflict with adopting [product/category]?
What do they take PRIDE in that might be threatened by changing?
Find: Community self-descriptions, "I'm the kind of person who..." statements,
group identity markers, tribal affiliations.
Return: 10-15 identity signals with source attribution.
```

### Output: Raw Research Corpus

```
## Phase 1: Voice-of-Customer Research Corpus

### Direct Belief Statements
| # | Quote | Source | Platform |
|---|-------|--------|----------|
| 1 | "[exact quote]" | [link/attribution] | Reddit |
| ... | ... | ... | ... |

### Resistance & Objection Statements
| # | Quote | Source | Platform |
|---|-------|--------|----------|
| ... | ... | ... | ... |

### Identity & Tribal Signals
| # | Signal | Source | Platform |
|---|--------|--------|----------|
| ... | ... | ... | ... |
```

---

## Phase 2: Belief Classification & Resistance Hierarchy

**Uses**: McRaney Pattern 1 (Resistance Hierarchy)

### Execute

Take every belief and objection from Phase 1 and classify using the 4-tier hierarchy:

1. **Fact-level beliefs** — Objectively testable. Updateable with evidence alone.
   - Signal language: "I heard that...", "The data shows...", "Studies say..."
2. **Attitude-level beliefs** — Emotional + experiential. Requires emotional/experiential shift.
   - Signal language: "I feel like...", "In my experience...", "It just seems..."
3. **Value-level beliefs** — Moral/ethical anchoring. Requires social permission + identity bridging.
   - Signal language: "It's wrong to...", "I believe in...", "That's not how things should..."
4. **Identity-level beliefs** — Fused with self-concept. Requires paradigm reconstruction + face-saving.
   - Signal language: "I'm the kind of person who...", "That's not who I am...", "People like me don't..."

### Output

```
## Phase 2: Belief Classification

### Tier Map
| Belief | Classification | Strength (1-10) | Source Quote | Changeability |
|--------|---------------|-----------------|-------------|---------------|
| [belief] | Fact / Attitude / Value / Identity | [score] | "[quote]" | High / Medium / Low / Very Low |

### Distribution
- Fact-level: [X] beliefs ([X]% of total)
- Attitude-level: [X] beliefs ([X]%)
- Value-level: [X] beliefs ([X]%)
- Identity-level: [X] beliefs ([X]%)

### Critical Insight
[1-2 paragraph analysis: What does this distribution tell us about how hard this audience
will be to move? Which tier dominates? What does that mean for strategy?]
```

---

## Phase 3: Processing Chain Reverse-Engineering

**Uses**: McRaney Pattern 4 (Processing Chain), Pattern 17 (Emotional Sediment)

### Execute

For the 3-5 most critical beliefs (highest strength + lowest changeability), trace backwards through the processing chain:

1. **Current Position** → What they believe right now (from Phase 2)
2. **Evidence Recruited** → What facts/experiences they cite to support it
3. **Social Reinforcement** → Who/what community keeps this belief alive
4. **Identity Integration** → How this belief became "who they are"
5. **Emotional Reaction** → What they FEEL about this (fear, pride, betrayal, hope)
6. **Origin Experience** → The formative event/experience that seeded this belief

### Additional Research 🔬

Fire a targeted Perplexity query for each critical belief:

```
Search for: Origin stories of why [audience] started believing [specific belief].
Find "how I got started" posts, "why I switched to" posts, personal stories about
the moment they adopted this belief or position.
Return: 5-10 origin narratives.
```

### Output

```
## Phase 3: Processing Chains

### Critical Belief 1: "[belief statement]"
**Strength**: [X]/10 | **Classification**: [tier]

| Layer | Content | Evidence |
|-------|---------|----------|
| Current Position | [what they believe] | [source] |
| Evidence Recruited | [what they cite] | [source] |
| Social Reinforcement | [who keeps it alive] | [source] |
| Identity Integration | [how it became them] | [source] |
| Emotional Reaction | [what they feel] | [source] |
| Origin Experience | [what started it] | [source] |

**Emotional Sediment Map**: [2-3 sentence narrative describing the emotional history
that created this belief — past failures, authority betrayals, social rejections]

[Repeat for each critical belief]
```

---

## Phase 4: Social Death Calculation

**Uses**: McRaney Pattern 5 (Social Death Calculation), Pattern 6 (Pluralistic Ignorance)

### Execute

For each critical belief, score the social cost of changing:

1. **Tribal Cost** (1-10): Who knows they hold this position? What group membership depends on it?
2. **Face Cost** (1-10): What face would they lose by changing? Would they look stupid, naive, or disloyal?
3. **Relationship Cost** (1-10): What relationships are at risk if they change?
4. **Status Cost** (1-10): What authority, expertise, or status depends on this belief?

Then check for **Pluralistic Ignorance** (Pattern 6):

```
Is there evidence that members of this group privately doubt this belief
but publicly maintain it because they think everyone else truly believes it?
```

### Additional Research 🔬

```
Search for: "[audience/community] secretly doubts [belief/practice]" OR
"[audience] privately thinks [alternative]" OR "[audience] afraid to say [position]"
Find: Anonymous confessions, throwaway accounts, private survey data,
"unpopular opinion" posts within the community.
Return: Any evidence of pluralistic ignorance.
```

### Output

```
## Phase 4: Social Death Calculation

### Cost Matrix
| Belief | Tribal | Face | Relationship | Status | Total Social Cost |
|--------|--------|------|-------------|--------|-------------------|
| [belief 1] | [X]/10 | [X]/10 | [X]/10 | [X]/10 | [sum]/40 |
| [belief 2] | ... | ... | ... | ... | ... |

### Pluralistic Ignorance Detection
- Evidence found: [Yes/No]
- Specific signals: [list any anonymous dissent, private doubts, "unpopular opinion" posts]
- Strategic implication: [If yes — this is a massive leverage point. Surface the private doubt.]
```

---

## Phase 5: Threshold Calculation & Strategic Summary

**Uses**: McRaney Pattern 13 (Threshold Equation), Pattern 18 (Minimum Viable Change), HK 13 (30% Calibration)

### Execute

For each critical belief, calculate:

**Change Drivers** (score each 1-10):
- Trigger (how compelling is the reason to change?)
- Trusted Source (do they trust anyone who holds the new position?)
- Social Safety (how safe is it to change in their social context?)
- Identity Bridge (is there a way to change without losing identity?)

**Change Resistors** (score each 1-10):
- Investment (how much have they invested in the current position?)
- Social Risk (what do they stand to lose socially?)
- Identity Threat (how much does changing threaten "who they are"?)
- Uncertainty (how uncertain is the outcome of changing?)

**30% Calibration**:
- Estimate available counter-evidence (0-100%)
- Social Risk + Identity Threat sum → if > 12, you're in high-cost territory
- Effective threshold = 30% × social cost multiplier
- Strategy: Add evidence OR reduce cost?

**Minimum Viable Intervention**:
- Name the single thing that, if changed, would tip the balance

### Output: Complete Belief Architecture Document

```
## Phase 5: Threshold Analysis & Strategic Summary

### Threshold Equations
| Belief | Drivers Total | Resistors Total | Gap | Binding Constraint |
|--------|--------------|----------------|-----|-------------------|
| [belief 1] | [sum] | [sum] | [+/-X] | [specific variable] |

### 30% Calibration
| Belief | Evidence Available | Social Cost Multiplier | Effective Threshold | Strategy |
|--------|-------------------|----------------------|--------------------|-----------| 
| [belief 1] | ~[X]% | [X]x | ~[X]% | [Add evidence / Reduce cost] |

### Minimum Viable Interventions
1. **[Belief 1]**: [The single sentence, experience, or proof point that tips it]
2. **[Belief 2]**: [...]

### Strategic Recommendations
[3-5 paragraph executive summary answering:
- What is the dominant resistance type?
- Where is the highest-leverage intervention point?
- Should we lead with evidence or with social permission?
- What face-saving narrative do we need to pre-build?
- What's the recommended messaging sequence?]
```

---

## Quality Gate

| Criterion | Question | Pass? |
|-----------|----------|-------|
| **Grounding** | Is every belief claim traced to a real source (quote, post, review) — not training data? | |
| **Classification Accuracy** | Are beliefs correctly classified by tier? Would the audience recognize these as their beliefs? | |
| **Processing Depth** | Do the processing chains trace to genuine origin experiences, not generic assumptions? | |
| **Social Cost Realism** | Are social death scores based on actual community dynamics found in research, not guesses? | |
| **Actionability** | Could a copywriter, strategist, or campaign designer execute directly from this document? | |
| **Threshold Specificity** | Can you name the binding constraint and minimum viable intervention for each critical belief? | |

## Integration

This document feeds directly into:
- `/belief-creative-brief` (as the research foundation)
- `/persuasion-copy` (as the audience intelligence layer)
- `/threshold-campaign` (as the equation inputs)
- `/belief-first-audience-intelligence` (as Phase 1 replacement)
- `/belief-dissolve-copy` (as the belief identification source)
