---
description: End-to-end brand architect service — raw concept to structured archetype strategy with all foundational documents
---

# /oren-brand-architect-pipeline — Brand Architect Pipeline

The master orchestration workflow for the Archetype Arbitrage Service. Takes someone with a raw concept, idea, product, or offer and produces a complete, structured brand strategy with all foundational documents — archetype selection, content architecture, revenue bridge, and pitch deck.

This is the full service chain. The client walks away with a real business plan for their content, not a vague "post more" recommendation.

## Usage

```
/oren-brand-architect-pipeline [brand/client name] [raw concept or context]
```

## Prerequisites
- Load `genius.md` before executing
- Client intake information (who they are, what they sell, what resources they have)
- Any existing social presence to audit (optional — works for zero-to-one builds too)

## Steps

### Phase 1: Intake & Discovery (The Interview)

Run a structured intake interview. Capture:

1. **Identity**: Who is this brand/person? What do they sell/offer?
2. **Current State**: Do they have existing content? If yes, audit for archetype incoherence.
3. **Ambition**: What do they want content to DO for them? (awareness, leads, authority, sales?)
4. **Resources**: Pre-populate the resource audit dimensions:
   - Camera talent availability
   - Design/production capability
   - Showcasable assets (product, process, space, knowledge)
   - Budget reality (monthly content production budget)
   - Time reality (hours per week dedicated to content)
5. **Audience**: Who are they trying to reach? (Feed into Dai Media consumer posture if available)
6. **Competitors**: Who else is playing in this space? What are they doing on social?

**Output**: Intake Brief (1-2 page summary of raw inputs)

### Phase 2: Resource-Reality Audit

Run `/oren-resource-audit` methodology against the intake data.

Produce:
1. **Resource Inventory**: What they have, don't have, and can acquire
2. **Archetype Eligibility Matrix**: Which archetypes are POSSIBLE (not aspirational)
3. **Resource Gaps**: What they'd need to acquire for each eligible archetype
4. **Production Reality**: What content formats they can actually sustain weekly

**Decision Gate**: If ZERO archetypes are viable with current resources, the engagement shifts to "what resources do you need to acquire first?" Don't force an archetype onto an under-resourced brand.

### Phase 3: Consumer Posture Analysis

If client data supports it, run consumer posture analysis:

1. **Who is the radical individual?** (Not demographics — the specific person)
2. **What is their occupation, activity, thought process?** (Dai Media 3D framework)
3. **What do they share and why?** (Sharing mechanic maps to archetype fit)
4. **Where do they already gather?** (Platform selection)

> [!TIP]
> Stack with `/consumer-posture-profile` for premium engagements. For lighter engagements, use the abbreviated 5-question version embedded here.

**Output**: Consumer Posture Card (one-page profile of the target individual)

### Phase 4: Archetype Diagnostic & Selection

Run the full archetype diagnostic with fit-scoring:

For each ELIGIBLE archetype (from Phase 2), score on 5 dimensions:

| Dimension | Weight | Score 1-10 |
|-----------|--------|------------|
| Resource Fit | 30% | How well do current resources match requirements? |
| Consumer Fit | 25% | How well does the archetype serve the target consumer's sharing behavior? |
| Competitive Differentiation | 20% | Does this archetype differentiate from competitor strategies? |
| Brand DNA Alignment | 15% | Does this archetype feel authentic to who the brand IS? |
| Revenue Pathway Clarity | 10% | How clearly does this archetype connect to making money? |

**Weighted Score** = sum of (dimension score × weight)

Select the archetype with the highest weighted score. If two archetypes score within 5 points of each other, present both with a clear recommendation and rationale.

**Decision Gate**: Client confirms archetype selection before proceeding.

**Output**: Archetype Selection Report (scored matrix + recommendation + rationale)

### Phase 5: Archetype-Specific Content Architecture

Based on selected archetype, route to the appropriate architect workflow:

| Archetype | Route To | Core Output |
|-----------|----------|-------------|
| Oracle | `/oren-oracle-architect` methodology | 3-layer funnel + expert authority plan |
| Performer | `/oren-performer-architect` methodology | Show concept + omnipresence strategy + episode bible |
| World Builder | `/oren-world-builder-architect` methodology | Creative brief + immersive content series + risk assessment |
| Catalyst | `/oren-catalyst-architect` methodology | Aspiration ladder + community strategy + curation system |
| Helper | `/oren-helper-architect` methodology | Utility content matrix + organic-to-paid bridge + format library |

Produce for ALL archetypes:
1. **Content Type Matrix**: 5-8 specific content types with format specs
2. **Content Calendar Template**: Weekly rhythm with content types mapped to days
3. **20+ Content Ideas**: Specific, executable ideas (not "post about your product")
4. **Production Specs**: Exactly what gear, people, and time each content type requires
5. **Quality Rubric**: How to evaluate if a piece of content meets the archetype standard

**Output**: Content Architecture Document (3-5 pages)

### Phase 6: Revenue Bridge

Connect the archetype to revenue using `/oren-archetype-revenue-bridge` methodology:

1. **Funnel Mechanic**: How does this archetype's content convert? (Each archetype has a distinct conversion pathway)
2. **Offer Architecture**: What should they sell? At what price point? (Stack with `/offer-stack` for depth)
3. **Conversion Touchpoints**: Where in the content does the audience move from viewer → lead → buyer?
4. **Metrics That Matter**: Which 3-5 metrics actually indicate revenue progress for this archetype?
5. **Revenue Timeline**: Realistic expectations — when does content start generating revenue?

**Output**: Revenue Bridge Document (1-2 pages)

### Phase 7: Pitch Deck & Handoff

Compile all outputs into a professional deliverable using `/oren-archetype-pitch-deck` methodology:

1. **Executive Summary**: One-page overview of the brand strategy
2. **Archetype Selection**: Why this archetype, with scoring rationale
3. **Content Architecture**: The content system at a glance
4. **Revenue Bridge**: How this makes money
5. **Content Roadmap**: First 30 days of specific content, with production specs
6. **Exemplar Proof**: 3-5 real brands executing this archetype successfully
7. **Resource Requirements**: What the client needs to execute (people, tools, budget)
8. **Next Steps**: Specific actions for the first week

**Output**: Brand Architect Brief (comprehensive strategy document, 8-12 pages)

### Phase 8: Finalization & Quality Gate

Before delivering, audit the complete deliverable:

- [ ] Archetype is constrained by ACTUAL resources (not aspiration)
- [ ] Content ideas are specific enough to produce within 48 hours
- [ ] Revenue pathway is realistic for the client's current stage
- [ ] Exemplars are industry-relevant (not just "Nike does it")
- [ ] The client could hand this document to a team member and they'd know what to do
- [ ] No archetype mixing — every recommendation flows from ONE archetype
- [ ] Production specs have a CEILING (what they will NOT do)

---

## Deliverable Summary

The Brand Architect Pipeline produces:

| Document | Pages | Purpose |
|----------|-------|---------|
| Intake Brief | 1-2 | Raw client data organized |
| Resource Inventory | 1 | What they have, don't have, can get |
| Consumer Posture Card | 1 | Who they're reaching |
| Archetype Selection Report | 1-2 | Scored matrix + recommendation |
| Content Architecture | 3-5 | The content system |
| Revenue Bridge | 1-2 | How this makes money |
| Brand Architect Brief | 8-12 | Complete compiled strategy |

**Total**: A comprehensive brand strategy package that transforms a raw concept into an executable plan.

## Pricing Guide (Arbitrage Service)

| Tier | Scope | Price Range | Delivery |
|------|-------|-------------|----------|
| Sprint | Archetype selection + 20 content ideas + resource audit | $500-$1,000 | 24 hours |
| Standard | Full pipeline (all 7 documents) | $2,500-$3,500 | 48-72 hours |
| Premium | Full pipeline + consumer posture + competitive archetype map + 30-day content calendar | $5,000-$7,500 | 5-7 days |

## Stacking Chains

- **Upstream**: `/consumer-posture-profile` → `/storybrand` → THIS
- **Downstream**: THIS → `/oren-content-flywheel` → platform-specific deployment
- **Premium stack**: `/icp-deep-dive` → THIS → `/offer-stack` → `/high-ticket-launch`
- **Creator stack**: `/junyuh-identity` → THIS → `/sinem-publication-setup`
