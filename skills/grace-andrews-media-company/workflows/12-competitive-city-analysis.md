---
description: "Analyze competitors' content cities via parallel swarm and map white-space opportunities"
---

# Competitive City Analysis

> **Produces**: Competitor content city maps with white-space heat map and opportunity report  
> **Used When**: Entering a crowded niche, feeling outmatched, or seeking differentiation strategy  
> **Time**: 60-90 minutes (includes parallel research)  
> **Genius Patterns**: Media Company Default, City Architecture, Niche Precision Despite Breadth  
> **Cross-Stack**: Parallel Swarm (3-5 agents analyzing simultaneously), Deep Research, Kieran Flanagan (competitive intel)  
> **Research**: Uses parallel swarm (`--grounded`) for simultaneous competitor analysis

---

## Pre-Flight Check

- [ ] YOUR City Map exists (run Workflow 01 first — you need your own map before mapping rivals)
- [ ] 3-5 competitors identified (by name — not vague "other people in my niche")
- [ ] Loaded `genius.md` for quality ceiling calibration
- [ ] Understand what "winning" means for you (more newsletter subs? More revenue? More authority?)

---

## Step 1: Competitor Identification

Select 3-5 competitors strategically — not just "people I follow":

| Competitor | Why Them | Their Audience Size (estimate) | Their Revenue Model (known/guessed) |
|-----------|---------|------------------------------|-------------------------------------|
| [Name 1] | [Direct competitor? Aspirational model? Same audience?] | [Approx numbers] | [How they make money] |
| [Name 2] | | | |
| [Name 3] | | | |
| [Name 4] (optional) | | | |
| [Name 5] (optional) | | | |

**Selection quality gate**:
- ✅ At least 1 direct competitor (same audience, similar offer)
- ✅ At least 1 aspirational model (where you want to be in 2 years)
- ✅ At least 1 adjacent competitor (different niche, same audience or format)
- ❌ NOT all direct competitors (you'll miss strategic moves from adjacent spaces)

---

## Step 2: Parallel Swarm Deployment

Deploy competitive analysis via parallel swarm. Each agent maps one competitor's content city.

### Swarm Configuration

```bash
python execution/parallel_swarm.py --grounded --max-agents [N] \
  "Analyze [competitor name]'s content strategy as a media company using the City Map framework.
   
   Map their:
   1. Grand Central Station — What is their editorial mission? What belief drives everything?
   2. Content Lines — What formats do they publish? How often? Which platforms?
   3. Trust Pathway — How do they move people from attention to conversion? What bridge content exists?
   4. Revenue Architecture — How do they monetize? What products at what price points?
   5. Forgettable/Memorable Split — What % of their content is truly memorable vs. forgettable noise?
   6. Consistency vs Experimentation — Are they innovating or coasting on proven formats?
   
   Be SPECIFIC. Name actual content pieces, series, products. Use real data."
```

**Alternative** (if running manually): Deploy 3-5 sub-agents with `search_web` + `read_url_content`:

Each agent receives:
```
Research [Competitor Name]'s content strategy:
- List all content formats they publish (YouTube, podcast, newsletter, social, etc.)
- Note their posting frequency per format
- Identify their most successful/viral content pieces (engagement metrics if visible)
- Document their products, courses, communities, and pricing
- Note their collaboration/guest strategy
- Identify any recurring series or episodic content

Use search_web to find recent data. Read their newsletter landing page, YouTube channel, and social profiles.
Write findings to .tmp/competitive-analysis/[competitor-slug].md
```

Save each competitor's analysis to `.tmp/competitive-analysis/[competitor-slug].md`

---

## Step 3: Competitor City Map Construction

For each competitor, build a simplified City Map:

```
COMPETITOR: [Name]
AUDIENCE SIZE: [Estimate across platforms]

GRAND CENTRAL: [Their editorial mission/belief]

CONTENT LINES:
  Line 1: [Format] @ [Frequency] → [Trust stage served] | Quality: [H/M/L]
  Line 2: [Format] @ [Frequency] → [Trust stage served] | Quality: [H/M/L]  
  Line 3: [Format] @ [Frequency] → [Trust stage served] | Quality: [H/M/L]

TRUST PATHWAY:
  Attention → [How they capture it]
  Discovery → [How people find more of them]
  Connection → [How they build personal resonance]
  Trust → [How they prove expertise]
  Conversion → [How they sell]
  
  WEAKEST STAGE: [Where their pathway breaks]

REVENUE:
  Stream 1: [Product/Service] at $[Price] → [Volume estimate]
  Stream 2: [Product/Service] at $[Price] → [Volume estimate]
  
  TOTAL ESTIMATED: $[Range]

FORGETTABLE/MEMORABLE RATIO: [Estimate — what % of content is truly memorable?]
CONSISTENCY/EXPERIMENTATION: [Are they innovating or repeating?]
```

---

## Step 4: White-Space Heat Map

Cross-reference all competitor maps to identify:

### Format White Space
| Content Format | Competitor 1 | Competitor 2 | Competitor 3 | YOUR Coverage | Opportunity? |
|---------------|-------------|-------------|-------------|---------------|-------------|
| Long-form YouTube | ✅ | ✅ | ❌ | [status] | [H/M/L opportunity] |
| Podcast | ❌ | ✅ | ✅ | [status] | [H/M/L opportunity] |
| Newsletter | ✅ | ❌ | ❌ | [status] | [H/M/L opportunity] |
| Short-form video | ✅ | ✅ | ✅ | [status] | [Saturated — differentiate or skip] |
| Community/membership | ❌ | ❌ | ❌ | [status] | [🔥 HIGH — nobody's doing it] |

### Trust Stage White Space
| Trust Stage | Competitor 1 | Competitor 2 | Competitor 3 | YOUR Coverage | Opportunity? |
|------------|-------------|-------------|-------------|---------------|-------------|
| Attention | ✅ | ✅ | ✅ | [status] | [Everyone's here — need differentiation] |
| Discoverability | ✅ | ❌ | ✅ | [status] | [Opportunity level] |
| Connection | ❌ | ❌ | ✅ | [status] | [🔥 Few competitors here] |
| Trust | ✅ | ✅ | ❌ | [status] | [Opportunity level] |
| Conversion | ❌ | ❌ | ❌ | [status] | [🔥 Nobody's closing well] |

### Niche White Space
| Topic/Angle | Competitor Coverage | YOUR Opportunity |
|------------|-------------------|-----------------|
| [Topic 1] | [Heavily covered by all] | [Skip or find a unique angle] |
| [Topic 2] | [Covered by 1, ignored by others] | [Medium — differentiate approach] |
| [Topic 3] | [Nobody covers this] | [🔥 Green field — own it] |

---

## Step 5: Differentiation Strategy

Based on the white-space analysis, design your differentiation:

### Three Differentiation Moves

**Move 1: Uncovered District** — Move into a trust stage no competitor serves well
> "If nobody in your space is doing deep-trust content (case studies, long-form tutorials, genuine vulnerability), THAT is your unfair advantage."

**Move 2: Format Innovation** — Use a format nobody in your niche has adopted
> "If all your competitors are on YouTube and Instagram, and nobody has a great newsletter — own newsletter. First mover in a format = authority by default."

**Move 3: Niche Within Niche** — Go deeper where competitors go broad
> "If competitors serve 'entrepreneurs,' you serve 'bootstrapped SaaS founders.' Niche precision is Grace's deepest principle."

---

## Output Format

Deliver:
1. **Competitor City Maps** (one per competitor) — Grand Central, content lines, trust pathway, revenue, quality assessment
2. **White-Space Heat Map** — cross-competitor analysis showing format, trust stage, and niche gaps
3. **Differentiation Strategy Brief** — 3 specific moves to differentiate, ranked by opportunity size and execution difficulty
4. **Your City Map Adjustment Recommendations** — specific changes to make to your own City Map based on competitive intelligence
5. **90-Day Competitive Response Plan** — what to build/change based on the analysis
