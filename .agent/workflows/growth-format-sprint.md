---
description: Batch growth format production
---

# `/growth-format-sprint` — Batch Growth Format Production

Scans trending brands, people, and news in your niche simultaneously → ranks entities by growth potential → produces 3-5 publish-ready growth posts in one sprint. Fill your entire growth bucket for the week in a single session.

## When to Use
- Content day: you need a week's worth of growth posts fast
- You want to batch-produce across ALL jack types (brandjack + newsjack + namejack + hot take)
- You want the research done for you — trending entity discovery + ranking
- You want Diandra's 35% growth bucket ratio handled in one session

## Usage

```
/growth-format-sprint [niche or domain]
/growth-format-sprint "B2B SaaS marketing"
/growth-format-sprint --entities "Apple, Sam Altman, AI regulation" --count 3
/growth-format-sprint --count 5   (produce 5 posts)
```

---

## Phase 1: Trend Scan (Parallel Research)

**Actor**: Orchestrator + 3 parallel research sweeps

### Scan 1: Trending Brands
```
search_web: "[niche] brand news announcement campaign 2026"
search_web: "[niche] company decision strategy pivot 2026"
```
→ Extract 5-7 brand candidates with what happened

### Scan 2: Notable People
```
search_web: "[niche] thought leader viral LinkedIn post 2026"
search_web: "[niche] CEO founder controversial statement 2026"
```
→ Extract 5-7 person candidates with their recent notable actions

### Scan 3: Breaking News
```
search_web: "[niche] breaking news industry update march 2026"
search_web: "[niche] regulation policy change announcement 2026"
```
→ Extract 5-7 news candidates with timing

Use `read_url_content` on top 3 results per scan for specifics.

---

## Phase 2: Opportunity Ranking

**Actor**: Orchestrator

Score ALL discovered entities on Diandra's criteria:

```markdown
## Entity Ranking: [Niche]

| # | Entity | Jack Type | Recognition (1-10) | Recency (1-10) | ICP Overlap (1-10) | Boomerang (1-10) | Angle Richness (1-10) | TOTAL |
|---|--------|-----------|-------------------|----------------|--------------------|-----------------|-----------------------|-------|
| 1 | [brand] | Brandjack | | | | | | |
| 2 | [person] | Namejack | | | | | | |
| 3 | [news] | Newsjack | | | | | | |
| 4 | [belief] | Hot Take | | | | | | |
| ... |

**Top recommendations**:
1. [Entity] — [1-line why]: [total score]
2. [Entity] — [1-line why]: [total score]
3. [Entity] — [1-line why]: [total score]

**Pick 3-5 entities to produce. Include at least 2 different jack types for variety.**
```

**WAIT FOR USER SELECTION.**

---

## Phase 3: Parallel Post Production

**Actor**: 1 sub-agent per entity, launched in parallel (max 5)
**Prerequisite**: User selected 3-5 entities

For each selected entity, spawn a dedicated sub-agent **in a single message**:

### Sub-Agent Template (repeated per entity)
```
You are Diandra Escobar's Writing Engine producing a GROWTH post.

## SKILL ACQUISITION
Read these files IN ORDER:
1. /Users/farricecain/Google Antigravity/skills/diandra-escobar-linkedin-growth/genius.md
2. /Users/farricecain/Google Antigravity/skills/diandra-escobar-linkedin-growth/workflows/[type-specific-workflow].md
3. /Users/farricecain/Google Antigravity/skills/diandra-escobar-linkedin-growth/workflows/09-linkedin-writing-engine.md

## ENTITY
- **Name**: [entity]
- **Jack Type**: [type]
- **What Happened**: [from Phase 1 research]
- **Key Details**: [specific numbers, dates, decisions from research]

## CONTEXT
Read /Users/farricecain/Google Antigravity/FARRICE.md for voice and positioning.

## YOUR TASK
Produce a complete LinkedIn growth post:

1. **Entity Assessment**: Recognition, recency, ICP overlap, boomerang potential (quickscore)
2. **Angle Selection**: Pick the single best angle for THIS entity (What They Did Right / What They Missed / What This Means For You)
3. **Body-First Writing**:
   - Write 150-300 words of genuine analysis
   - Include specific details (numbers, names, decisions)
   - Add YOUR expert POV — not a news summary
4. **Hook Mining**:
   - Generate 3 hook candidates from the body
   - Select the strongest
   - Entity name MUST appear in first 2 lines
5. **CTA**: Growth bucket — invite discussion
6. **Visual Brief**: 1-sentence image recommendation
7. **Boomerang Notes**: If entity is active on LinkedIn, recommend tag strategy

## QUALITY GATES
- "So What?" test: position, not summary
- Entity-in-hook check
- Specificity: ≥2 specific details
- Anti-Exemplar check against genius.md

## OUTPUT FORMAT
```markdown
### Post [N]: [Entity] ([Jack Type])

**Angle**: [selected]
**Boomerang Viability**: [score/10]

**THE POST**:
[Complete publish-ready post]

**Hook Alternatives**:
1. [alt hook 1]
2. [alt hook 2]

**Visual Brief**: [1-sentence]
**Tag Strategy**: [recommendation]
**Best Posting Window**: [recommendation]
```

Write to: .tmp/growth-format-sprint/post-[N]-[slug].md
```

### Workflow Routing Per Jack Type:

| Jack Type | Workflow to Load |
|-----------|-----------------|
| Brandjack | `workflows/01-brandjack-post-generator.md` |
| Newsjack | `workflows/02-newsjack-post-generator.md` |
| Namejack | `workflows/03-namejack-post-generator.md` |
| Hot Take | `workflows/04-hot-take-post-generator.md` |

---

## Phase 4: Calendar Integration

**Actor**: Orchestrator
**Prerequisite**: All sub-agent outputs received

### Posting Schedule

Arrange posts in optimal order:

```markdown
## Suggested Posting Calendar

| Day | Post | Entity | Jack Type | Why This Order |
|-----|------|--------|-----------|----------------|
| Mon | Post 1 | [entity] | Brandjack | Freshest news — LinkedIn lag advantage |
| Tue | Post 2 | [entity] | Hot Take | Contrarian mid-week works best |
| Wed | — | | | Rest day / engagement focus |
| Thu | Post 3 | [entity] | Namejack | Person-tagged posts perform well Th-Fr |
| Fri | Post 4 | [entity] | Newsjack | End-of-week news roundup feel |

**Posting times**: 7-9 AM EST for max LinkedIn distribution
```

### Bucket Balance Check

Ensure the sprint fills the growth bucket without over-indexing:

```markdown
**Growth bucket status**: [X] posts this month / target [Y] (35% of monthly content)
**Remaining to target**: [Z] more growth posts needed this month
```

---

## Phase 5: Quality Gate + Deliver

### Quality Checks (across all posts):

| Check | All Posts Must Pass |
|-------|-------------------|
| Jack Type Variety | At least 2 different jack types represented |
| "So What?" Gate | Every post has a position, not a summary |
| Entity-in-Hook | Brand/person name in first 2 lines of every post |
| Body-First | All hooks mined from body content |
| Specificity | ≥2 specific details per post |
| Voice Consistency | All posts sound like the same creator |
| No Repetition | Posts don't repeat the same structural pattern |

### Deliver

```markdown
# 📦 GROWTH FORMAT SPRINT: [Niche]

**Posts produced**: [N]
**Jack types covered**: [list]
**Date**: [date]

---

## POST 1: [Entity] (Brandjack)
[Full post + hook alternatives + visual brief + boomerang strategy]

---

## POST 2: [Entity] (Namejack)
[Full post + hook alternatives + visual brief + boomerang strategy]

---

## POST 3: [Entity] (Hot Take)
[Full post + hook alternatives + visual brief + boomerang strategy]

---

[... repeat for each post]

---

## POSTING CALENDAR
[Calendar from Phase 4]

## BUCKET STATUS
[Balance check from Phase 4]

## PROVENANCE
- Research: [total query count] queries | 🟢 GROUNDED
- Entities scanned: [count] | Selected: [count]
- Skills: Diandra Escobar genius.md + workflows 01-04, 09
- Quality: All [N] posts passed 7-point gate
```

Save to `.tmp/growth-format-sprint/sprint-[date].md`.

### Next Steps

```
> **Week sorted.**
>
> - Post them in the calendar order above
> - Run `/diandra-content-engine` to fill your authority and conversion buckets
> - Run `/diandra-steal-and-remix` to build your mechanic library for next sprint
> - Run `/growth-format-sprint` again next week with fresh entities
```

---

## Output Files

```
.tmp/growth-format-sprint/
  post-1-[slug].md
  post-2-[slug].md
  post-3-[slug].md
  [post-4-[slug].md]
  [post-5-[slug].md]
  sprint-[date].md   (assembled final package)
```

## Limits

- **Max 5 posts per sprint** (quality degrades beyond this)
- **At least 2 different jack types** (variety > repetition)
- Each sub-agent loads skill files fresh (clean context)
- Posts are produced independently — no cross-referencing between them
