---
description: The full media company build
---

# /grace-new-media — City Blueprint with New Media Physics

Grace Andrews' content city methodology enhanced with a16z's OODA loop speed advantage and oral/written culture physics. Every content line gets tagged for culture mode. The transit system includes OODA speed. The trust pathways enforce written-first pipeline.

## Usage

```
/grace-new-media [brand/creator name] --niche "[niche]"
/grace-new-media "Farrice Cain" --niche "AI-powered business systems"
```

## Steps

### 1. Load Context
Read these files in order:
1. `skills/grace-andrews-media-company/SKILL.md`
2. `skills/grace-andrews-media-company/genius.md`
3. `skills/andreessen-horowitz-new-media/genius.md`

### 2. Deep Research Foundation
Same as `/grace-city-blueprint` — run 2 Perplexity `sonar-deep-research` queries for market intelligence.

### 3. Execute City Map with Culture Tagging
**Load**: `skills/grace-andrews-media-company/workflows/01-city-map-architect.md`

Build the city map, but with each content line tagged:

| Content Line | Platform | Culture Mode | Written-First? | OODA Speed Target |
|-------------|----------|-------------|----------------|-------------------|
| [Line 1] | YouTube Long | Written | YES — canonical | 48h production |
| [Line 2] | X Thread | Oral | Extracted from Line 1 | <4h reaction |
| [Line 3] | LinkedIn | Hybrid | Standalone | 24h production |
| [Line 4] | Substack | Written | YES — canonical | Weekly cadence |
| [Line 5] | Shorts/Reels | Oral | Extracted | <2h from concept |

**Critical enforcement**: Identify which content lines are CANONICAL (written-first, establish positions) and which are EXTRACTION (oral-mode, derived from canonical pieces).

### 4. Execute Trust Pathway with Written-First Pipeline
**Load**: `skills/grace-andrews-media-company/workflows/02-trust-pathway-planner.md`

Map trust pathways, but enforce:
- **Attention stage** → oral-culture content (hooks, short-form, burst energy)
- **Connection stage** → hybrid content (LinkedIn stories, quote threads)
- **Trust stage** → written-culture content (deep dives, case studies, long-form)
- **Conversion stage** → written-culture + direct (email sequences, sales pages)

Never try to BUILD TRUST in oral mode. Oral captures attention. Written builds trust.

### 5. OODA Layer
**Load**: `skills/andreessen-horowitz-new-media/workflows/02-ooda-media-warfare.md`

Add the speed layer:
- For each content line, define OODA speed target (how fast from observation → published)
- Identify which lines are REACTIVE (respond to market events) vs. PROACTIVE (scheduled)
- Design rapid-response content templates pre-tagged for culture mode
- Define who decides publication speed (if team, designate rapid-response authority)

### 6. Competitive OODA Benchmarking
For each competitor in the niche:
- How fast is their content loop?
- What culture modes do they dominate? Where are gaps?
- Calculate speed dominance ratio

### 7. Revenue District
**Load**: `skills/grace-andrews-media-company/workflows/09-revenue-district-architect.md`

Build revenue architecture with culture-mode awareness:
- Written-culture products (courses, ebooks, paid newsletters) sell through written-culture content
- Oral-culture products (coaching, communities, live events) sell through oral-culture content
- Match the selling medium to the product medium

### 8. 30-Day Content Sprint
**Load**: `skills/grace-andrews-media-company/workflows/11-content-sprint-planner.md`

Build calendar with culture-mode tagging:
- Written-first production schedule (canonical pieces created first in the week)
- Oral extraction schedule (derived content later in the week)
- OODA reactive slots (blank spaces reserved for rapid-response)

### 9. Assemble Blueprint
Combine all outputs with culture-mode and OODA layers clearly visible.

### 10. Quality Gate
- Is every content line tagged for oral/written mode?
- Does the written-first pipeline flow correctly (canonical → extraction)?
- Is the OODA speed target defined per content line?
- Are trust stages matched to appropriate culture modes?
- Is the speed dominance ratio ≥ 2:1 vs. nearest competitor?

### 11. Output
Save to `deliverables/grace-new-media-blueprint-[brand-slug]-[date].md`

### 12. Finalize
```bash
python3 execution/chain_runner.py finalize "Grace New Media Blueprint for [brand]" \
    --expert "grace-andrews" \
    --skill "grace-andrews-media-company" \
    --workflow "grace-new-media" \
    --type Strategy \
    --intent [evidence-based] --expert-score [evidence-based] --adversarial [evidence-based] \
    --notes "Grace city map with a16z OODA + oral/written culture integration"
```
