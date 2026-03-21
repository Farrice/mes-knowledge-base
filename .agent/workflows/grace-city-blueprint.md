---
description: "Full end-to-end city build — Deep Research → City Map → Trust Pathways → Revenue District → 30-day calendar"
---

# /grace-city-blueprint — Complete Media Company Build

Build a complete content city from scratch in one session. Chains City Map → Trust Pathways → Revenue District → Content Sprint with a deep research pre-flight to ground every decision in real market data.

**The standard**: This is the "one-shot media company" command — the output should be a comprehensive, actionable blueprint that a creator can immediately start executing against.

## Usage

```
/grace-city-blueprint [brand/creator name] --niche "[niche description]"
/grace-city-blueprint "Farrice Cain" --niche "AI-powered business systems for solopreneurs"
```

## Steps

### 1. Load Skills
Read these files:
1. `skills/grace-andrews-media-company/SKILL.md`
2. `skills/grace-andrews-media-company/genius.md`

### 2. Deep Research Foundation
Run a condensed deep research pre-flight (2 Perplexity `sonar-deep-research` queries):

**Query 1**: "Who are the top 5-10 creators/media companies in [niche]? What content formats dominate? What's the audience size and revenue range? Include specific data."

**Query 2**: "What does the audience in [niche] actually want from content creators? What formats get the most engagement? What are they willing to pay for? Use Reddit, YouTube comments, and forum data."

Save to `.tmp/grace-blueprint/research-*.md`. Compress key findings for injection into subsequent workflows.

### 3. Execute City Map Architect
Run `skills/grace-andrews-media-company/workflows/01-city-map-architect.md` — inject research findings as context.

### 4. Execute Trust Pathway Planner
Run `skills/grace-andrews-media-company/workflows/02-trust-pathway-planner.md` — use the city map from Step 3.

### 5. Execute Revenue District Architect
Run `skills/grace-andrews-media-company/workflows/09-revenue-district-architect.md` — reference market benchmarks from research.

### 6. Execute Content Sprint Planner
Run `skills/grace-andrews-media-company/workflows/11-content-sprint-planner.md` — produce a 30-day calendar.

### 7. Assemble Final Blueprint
Combine all workflow outputs into a single master blueprint document.

### 8. Quality Gate
Score the blueprint:
- Does every content line have a trust pathway purpose?
- Does the revenue district have 3+ streams?
- Is the 30-day calendar realistic for the creator's capacity?
- Are all recommendations grounded in research data?

### 9. Save Output
Save to `deliverables/grace-city-blueprint-[brand-slug]-[date].md`

## Output Structure

```
# [Brand] — Media Company Blueprint

## Research Foundation (key data points)
## City Map (complete transit system)
## Trust Pathways (stage-tagged content plan)
## Revenue District (product ladder + conversion paths)
## 30-Day Content Sprint (calendar)
## Risk Assessment (what could go wrong)
## Next Steps (prioritized action items)
```
