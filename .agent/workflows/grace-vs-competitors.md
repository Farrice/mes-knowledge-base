---
description: "Competitive city analysis via parallel swarm — map 3-5 competitor content cities simultaneously and find white space"
---

# /grace-vs-competitors — Competitive City Analysis

Map competitors' content strategies as "rival cities" using parallel agents, then identify white-space opportunities for differentiation. Each agent analyzes one competitor simultaneously, producing city maps that are cross-referenced for gaps.

## Usage

```
/grace-vs-competitors [your niche] --competitors "Competitor A, Competitor B, Competitor C"
/grace-vs-competitors "AI business coaching" --competitors "Dan Koe, Nicolas Cole, Ali Abdaal, Justin Welsh"
```

## Steps

### 1. Load Skills
Read these files:
1. `skills/grace-andrews-media-company/SKILL.md`
2. `skills/grace-andrews-media-company/genius.md`
3. `skills/grace-andrews-media-company/workflows/12-competitive-city-analysis.md`

### 2. Deploy Parallel Swarm (Grounded)

// turbo
```bash
python /Users/farricecain/Google\ Antigravity/execution/parallel_swarm.py --grounded --max-agents [N] \
  "Analyze [competitor name]'s content strategy as a media company. Map their:
   1. Grand Central Station — editorial mission and core belief
   2. Content Lines — formats, platforms, frequencies
   3. Trust Pathway — how they move people from attention to conversion
   4. Revenue Architecture — products, pricing, revenue streams
   5. Forgettable/Memorable Split — what % is truly memorable
   6. Strengths and Weaknesses — where are they dominant and where are they exposed
   
   Research their actual content using Google Search. Name specific content pieces, series, and products."
```

If parallel swarm is unavailable, deploy individual `search_web` + `read_url_content` research agents for each competitor.

### 3. Build Competitor City Maps
Following Workflow 12, construct a simplified city map for each competitor from the swarm output.

### 4. Cross-Reference for White Space
Build the White-Space Heat Map (format gaps, trust stage gaps, niche gaps) by overlaying all competitor maps.

### 5. Design Differentiation Strategy
Identify 3 specific differentiation moves ranked by opportunity size.

### 6. Save Output
Save to `research_outputs/[date]-competitive-city-analysis-[niche-slug].md`

## Output Structure

```
# Competitive City Analysis: [Niche]

## Competitor City Maps (one per competitor)
## White-Space Heat Map (format × trust stage × niche)
## Differentiation Strategy (3 ranked moves)
## Your City Map Adjustment Recommendations
## 90-Day Competitive Response Plan
```
