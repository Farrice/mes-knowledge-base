---
description: Design a complete digital offer with funnel architecture, pricing model, sales page outline, and email sequence — from idea to revenue blueprint
---

# /design-offer — Offer + Funnel Architecture

Take a product/service idea and produce a complete offer design: market validation, pricing architecture, sales page outline, email sequence, and revenue projections. Uses Agent Teams for coordinated strategy + copywriting.

## Usage

```
/design-offer [offer idea]
/design-offer "AI-powered content system for solopreneurs"
/design-offer --type course "Expert extraction methodology"
/design-offer --type template "Weekly solopreneur planning system"
```

## When to Use

- You have an expertise area and want to monetize it
- You need to design a complete offer from scratch (not just a sales page)
- You want revenue projections and pricing architecture before building
- You're evaluating multiple product ideas and need to pick the best one

---

## Steps

### 1. Capture the Offer Seed

From the user's input, determine:
- **Offer idea**: What's the core value being sold?
- **Type** (if not specified): Course / Template / Guide / Toolkit / Coaching / Community / Bundle
- **Target audience**: Who is this for? (default from FARRICE.md)
- **Revenue target**: What monthly income should this support? (default: $10-20K/month)

Present for confirmation:

```markdown
## Offer Design Brief

**Idea**: [offer idea]
**Type**: [product type]
**Target audience**: [audience]
**Revenue target**: $[X]/month

### Design Phases
1. Market Validation (parallel research — 3 agents)
2. Offer Architecture (strategist + copywriter coordination)
3. Sales Assets (parallel generation — 3 agents)

Proceed? Or adjust the brief?
```

Wait for approval.

### 2. Market Validation (Parallel — 3 Agents)

Spawn 3 research agents **in a single message**:

**Agent 1: Demand Validation**
```
You are a market researcher validating demand for a digital offer.

**Offer**: [idea]
**Type**: [product type]
**Audience**: [target audience]

Use WebSearch to investigate:
1. How big is the market for this type of offer? (Total addressable, serviceable)
2. What are people actively searching for? (keyword signals, Reddit questions, forum posts)
3. What's the pain level? (Is this a vitamin or a painkiller?)
4. What's the urgency? (Is the audience actively seeking solutions NOW?)

Produce a demand validation score (1-10) with evidence.

Write to: .tmp/design-offer/research-demand.md
```

**Agent 2: Competitive Landscape**
```
You are a competitive analyst researching existing offers in this space.

**Offer**: [idea]
**Type**: [product type]
**Audience**: [target audience]

Use WebSearch to find:
1. Top 5 competing offers (name, price, format, positioning)
2. Price range across the market ($low - $high)
3. Gaps in existing offers (what are customers complaining about?)
4. Differentiation opportunities (what can Farrice do that others can't?)

Produce a competitive matrix with pricing data.

Write to: .tmp/design-offer/research-competitive.md
```

**Agent 3: Buyer Psychology**
```
You are a buyer psychology researcher.

**Offer**: [idea]
**Type**: [product type]
**Audience**: [target audience]

Use WebSearch to find:
1. Top objections buyers have for this type of offer (price, trust, time, overwhelm)
2. Buying triggers (what pushes someone from "interested" to "purchased"?)
3. Language patterns (exact words buyers use to describe this problem)
4. Social proof signals (what type of proof matters most — results, testimonials, case studies?)

Write to: .tmp/design-offer/research-buyer.md
```

### 3. Offer Architecture (Agent Teams)

Create a team with `TeamCreate` named `"offer-design"`. Spawn 2 teammates:

**Strategist (Daniel Priestley methodology)**
```
You are the Offer Strategist on team "offer-design". Your name is "strategist".

## SKILL ACQUISITION
Read:
1. /Users/farricecain/Google Antigravity/skills/daniel-priestley-oversubscribed/SKILL.md
2. /Users/farricecain/Google Antigravity/skills/daniel-priestley-oversubscribed/genius.md
3. /Users/farricecain/Google Antigravity/skills/daniel-priestley-oversubscribed/workflows/high-stakes-offer-architecture.md

## MARKET RESEARCH
Read the 3 research files in .tmp/design-offer/ for market validation data.

## YOUR TASK
Design the complete offer architecture:

### Offer Structure
- **Core offer**: [what the buyer gets]
- **Pricing tier(s)**: [1-tier, 2-tier, or 3-tier with prices]
- **Pricing model**: [one-time, subscription, cohort, pay-what-you-want]
- **Positioning angle**: [how this is different from competitors]

### Revenue Math
- Price point: $[X]
- Units needed per month for $[target]: [N]
- Conversion rate assumption: [%]
- Traffic/leads needed: [N]
- Feasibility score: [1-10]

### Funnel Architecture
1. **Awareness**: [how do people discover this?]
2. **Interest**: [what hooks them?]
3. **Decision**: [what pushes them to buy?]
4. **Purchase**: [what's the buying experience?]
5. **Retention**: [how do you keep them / get referrals?]

### Oversubscribed Strategy
Apply the "oversubscribed" methodology:
- Capacity: [limited spots? limited time?]
- Signaling demand: [waitlist? social proof? scarcity?]
- 7/11/4 rule: [7 hours of content, 11 touchpoints, 4 different locations]

Write your architecture to: .tmp/design-offer/offer-architecture.md
Then send a message to "copywriter" with the positioning angle and pricing so they can start on sales assets.
```

**Copywriter (Cardinal Mason + April Dunford)**
```
You are the Copywriter on team "offer-design". Your name is "copywriter".

## SKILL ACQUISITION
Read:
1. /Users/farricecain/Google Antigravity/skills/cardinal-mason-ai-copywriting/SKILL.md
2. /Users/farricecain/Google Antigravity/skills/cardinal-mason-ai-copywriting/genius.md
3. /Users/farricecain/Google Antigravity/skills/april-dunford-positioning/SKILL.md
4. /Users/farricecain/Google Antigravity/skills/april-dunford-positioning/workflows/product-positioning-blueprint.md

## VOICE CONTEXT
Read /Users/farricecain/Google Antigravity/FARRICE.md for voice markers.

## YOUR TASK
Wait for the strategist to send you the positioning angle and pricing. Then produce:

### Sales Page Outline
1. **Headline**: [Power headline using the positioning angle]
2. **Subheadline**: [Clarify the transformation]
3. **Problem section**: [3-5 pain points in buyer's language]
4. **Solution reveal**: [What this offer does differently]
5. **What's included**: [Feature → benefit mapping]
6. **Social proof section**: [What type of proof to use]
7. **Pricing section**: [Anchoring strategy + CTA]
8. **FAQ section**: [Top 5 objections, pre-handled]
9. **Final CTA**: [Urgency/scarcity close]

### Email Sequence (5 emails)
1. **Welcome/story** (Day 0): Hook with personal story, introduce the problem
2. **Problem amplification** (Day 2): Deepen the pain, show cost of inaction
3. **Solution preview** (Day 4): Show the framework, one free win
4. **Social proof** (Day 6): Results, testimonials, case studies
5. **Close** (Day 7): CTA with urgency, handle final objection

For each email: subject line + preview text + full body draft.

Write to: .tmp/design-offer/sales-assets.md
Then send a message to the team lead summarizing the sales angle and key copy hooks.
```

### 4. Compile and Present

After both teammates return, read all outputs and compile:

```markdown
# Offer Design: [Offer Name]

**Date**: [date]
**Type**: [product type]
**Target**: [audience]

---

## Market Validation Summary

### Demand Score: [X/10]
[Key evidence from demand research]

### Competitive Position
[How this offer is differentiated — top 3 competitors and gaps]

### Buyer Psychology
[Top objections + buying triggers in buyer's language]

---

## Offer Architecture

[From strategist — structure, pricing, funnel, oversubscribed strategy]

### Revenue Projections
| Scenario | Price | Units/Month | Monthly Revenue |
|----------|-------|-------------|----------------|
| Conservative | $[X] | [N] | $[total] |
| Target | $[X] | [N] | $[total] |
| Optimistic | $[X] | [N] | $[total] |

---

## Sales Page Outline
[From copywriter — full outline with copy hooks]

---

## Email Sequence
[From copywriter — 5 emails with subject lines and drafts]

---

## Next Steps
1. Validate with 5-10 potential buyers (show the offer, get reactions)
2. Build landing page → `/design-first-build` with this sales outline
3. Write full email sequence → `/launch-day` with email focus
4. Set up funnel → Manual or `/product-build` (when available)
```

Save to `.tmp/design-offer/offer-design-[slug].md`.

### 5. Shutdown Team and Offer Execution

Shutdown teammates. Offer:
- Build the landing page now (`/design-first-build`)
- Write the full email sequence (`/launch-day --formats "email"`)
- Validate with audience first (suggested interview questions)
- Run `/atomize` on the sales page to create promotional content

---

## Parallelism Details

| Stage | Tier | Agents | Why |
|-------|------|--------|-----|
| Market validation | Tier 1 (Parallel Task Calls) | 3 | Independent research angles |
| Offer architecture | Tier 2 (Agent Teams) | 2 | Strategist feeds copywriter |
| Compilation | Sequential | Main orchestrator | Must combine everything |

## Error Handling

- If market research shows demand score < 4: flag it prominently. "Market signals are weak. Consider pivoting the offer angle before building."
- If strategist and copywriter disagree on positioning: present both angles, let user choose
- If competitive research finds a saturated market: highlight differentiation opportunities, not despair

## Output Files

```
.tmp/design-offer/
  research-demand.md
  research-competitive.md
  research-buyer.md
  offer-architecture.md
  sales-assets.md
  offer-design-[slug].md   (combined final output)
```
