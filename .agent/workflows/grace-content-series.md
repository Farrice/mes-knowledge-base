---
description: "Episodic content series from topic — Research → Series Arc → Episode Plans → Hook Engineering → Production Calendar"
---

# /grace-content-series — Episodic Content Series Builder

Transform any topic into a full episodic content series with narrative arc, cross-platform distribution, and production calendar. Combines Grace's series architecture with hook engineering from platform specialists.

## Usage

```
/grace-content-series [topic] --platform [platform] --episodes [number]
/grace-content-series "Building an AI content team from scratch" --platform YouTube --episodes 8
/grace-content-series "The psychology of pricing" --platform Newsletter --episodes 6
```

## Steps

### 1. Load Skills
Read these files:
1. `skills/grace-andrews-media-company/SKILL.md`
2. `skills/grace-andrews-media-company/genius.md`
3. `skills/grace-andrews-media-company/workflows/06-content-series-architect.md`
4. `skills/grace-andrews-media-company/workflows/08-attention-capture-map.md` (for hook engineering)

### 2. Quick Research Scan
Use 2-3 `search_web` queries to find:
- Existing content series on this topic (what's already been done?)
- Audience interest signals (search volume, Reddit threads, YouTube engagement)
- Format precedents (how have others serialized similar topics?)

### 3. Execute Content Series Architect
Run the full Workflow 06 — produces series concept, narrative arc, episode blueprints, and series bible.

### 4. Hook Engineering Sprint
For each episode, generate hooks optimized for the target platform using the Attention Capture Map (Workflow 08):
- **YouTube**: Titles + thumbnails + cold opens using curiosity gap + proof
- **LinkedIn**: First-line hooks using trapdoor + pattern interrupt
- **Newsletter**: Subject lines using fascination + specificity
- **Podcast**: Cold open clips + episode titles

### 5. Cross-Platform Distribution Map
For each episode, plan the derivative content across all active platforms.

### 6. Production Calendar
Generate a production calendar with:
- Recording/writing dates
- Editing/review dates
- Publication dates
- Distribution dates for derivatives

### 7. Save Output
Save to `.tmp/grace-andrews/content-series-[topic-slug].md`

## Output Structure

```
# Content Series: [Series Name]

## Series Concept & Arc
## Episode Blueprints (with hooks per platform)
## Series Bible
## Cross-Platform Distribution Matrix
## Production Calendar (30-60 days)
## Pilot Episode Deep Design
```
