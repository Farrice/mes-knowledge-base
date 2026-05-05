---
description: Generate the professional leave-behind strategy document from archetype selection
---

# /oren-archetype-pitch-deck

Compiles all archetype pipeline outputs into a professional, boardroom-ready strategy document. This is the leave-behind that makes the service feel premium — the client can hand this to their team, their leadership, or their investors and everyone knows exactly what to do.

## Usage
```
/oren-archetype-pitch-deck [brand name]
```

## Prerequisites
- Archetype must be selected
- Content architecture must be designed
- Revenue bridge must be mapped
- Run this LAST in the `/oren-brand-architect-pipeline`

## Steps

### 1. Compile All Prior Outputs

Gather from previous pipeline phases:
- Intake Brief
- Resource Inventory
- Consumer Posture Card (if produced)
- Archetype Selection Report (with scoring)
- Content Architecture Document
- Revenue Bridge Document

### 2. Structure the Brand Architect Brief

#### Section 1: Executive Summary (1 page)
- Who the brand is (one sentence)
- The selected archetype (one sentence)
- The strategic thesis (two sentences: why this archetype, what it produces)
- The revenue pathway (one sentence)
- Timeline to results (one sentence)

#### Section 2: The Brand Today (1 page)
- Current state assessment (what exists now)
- Current content audit findings (if applicable — archetype incoherence diagnosis)
- Resource reality (what they have to work with)
- The gap: where they are vs. where they need to be

#### Section 3: Archetype Selection (1-2 pages)
- The 5 archetypes explained (brief, accessible language for non-experts)
- Why THIS archetype was selected (fit-scoring rationale)
- What this archetype produces (the funnel mechanic in plain language)
- What this archetype does NOT do (managing expectations)

#### Section 4: Content Architecture (2-3 pages)
- Content types with format specifications
- Weekly content rhythm (the calendar)
- Production requirements (people, gear, time, budget)
- Production ceiling (what they will NOT over-invest in)
- Sample content concepts (5-10 of the best from the brainstorm)

#### Section 5: Exemplar Proof (1-2 pages)
- 3-5 real brands executing this archetype successfully
- For each: what they do, why it works, relevant metrics if available
- At least 1 exemplar from a similar industry/vertical

#### Section 6: Revenue Bridge (1 page)
- How content connects to revenue (the funnel in plain language)
- Offer architecture recommendation
- Key metrics to track
- Revenue timeline (realistic month-by-month)

#### Section 7: 30-Day Launch Plan (1 page)
- **Week 1**: Setup (profiles, production assets, team alignment)
- **Week 2**: First content batch (3-5 pieces using top-scored ideas)
- **Week 3**: Optimize and iterate (review performance, adjust)
- **Week 4**: Full rhythm (execute the weekly calendar at full velocity)

#### Section 8: Investment & Next Steps (1 page)
- What the client needs to invest (time, money, people)
- Recommended tools/platforms
- Immediate next actions (what to do TOMORROW)
- Ongoing support options (if offering retainer services)

### 3. Quality Gate

Before finalizing:

- [ ] Executive summary is clear to someone who skipped the rest
- [ ] Archetype selection rationale would convince a skeptical CMO
- [ ] Content ideas are specific enough to produce within 48 hours
- [ ] Exemplars are industry-relevant, not just "Nike does it"
- [ ] Revenue pathway is honest about timeline
- [ ] 30-day plan has specific enough actions that a team could execute without you
- [ ] No jargon that requires explanation
- [ ] Total document is 8-12 pages (not 30)

### 4. Format Options

Produce in the format most useful for the client:

| Format | When | Notes |
|--------|------|-------|
| Markdown artifact | Default — always produce this | Clean, scannable, professional |
| Notion page | If client uses Notion | Use Notion API to create directly |
| Presentation deck | If client needs to present to leadership | Key findings per slide, visual-first |
| PDF-ready | If client needs a formal document | Add headers, page breaks, cover page |

## Stacking
- **Upstream**: Full `/oren-brand-architect-pipeline` → THIS
- **Presentation stack**: THIS → `/design-first-build` (if visual deck needed)
- **Sales stack**: THIS becomes the deliverable sample for `/free-custom-sample`
