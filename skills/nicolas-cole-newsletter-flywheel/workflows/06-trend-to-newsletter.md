---
description: Trending topic scan → audience pain cross-match → underserved opportunity → newsletter angle
---

# Trend to Newsletter — Cross-Pattern Research Engine

Scans trending topics, cross-patterns with audience pain points, and produces a newsletter angle for the next edition.

## Prerequisites
- Load `nicolas-cole-newsletter-flywheel` skill
- Newsletter tangible asset already defined
- Audience profile available (or will be built inline)

## Process

### Step 1: Trend Scan
Research current trends in the newsletter's domain using available tools:
1. **Perplexity/Web Search**: "What's trending in [domain] this week?"
2. **Platform-specific**: Check SubStack trending, Twitter/X discussions, LinkedIn trending posts, Reddit threads
3. **Tool/technology shifts**: Any new tools, platforms, or approaches that just launched?

Capture 5-7 trending signals with source links.

### Step 2: Audience Pain Mapping
For the newsletter's target audience, identify:
1. **Active pains**: Problems they're actively trying to solve right now
2. **Latent pains**: Problems they don't know they have yet (revealed by trends)
3. **Aspirational gaps**: Where they are vs. where they want to be

### Step 3: Cross-Pattern Matrix
Build a 2×2 matrix:

| | High Trend Relevance | Low Trend Relevance |
|---|---|---|
| **High Pain** | 🎯 PRIORITY — immediate edition | 📋 BACKLOG — evergreen edition |
| **Low Pain** | 🔮 EDUCATE — "here's why this matters to you" | ❌ SKIP |

Select the top 3 opportunities from the PRIORITY quadrant.

### Step 4: Tangible Asset Application
For each priority opportunity, design how the newsletter's tangible asset applies:
- "Given this trend and this pain, what specific [prompt/template/guide/etc.] would the reader want?"
- Ensure the asset passes the Save Test and Noun Test
- Write a 1-sentence edition pitch: "This week: [tangible asset] for [trend × pain intersection]"

### Step 5: Output
Deliver:
- **Trend briefing**: 5-7 signals with sources
- **Cross-pattern matrix**: Filled in with specific opportunities
- **Top 3 edition concepts**: Each with subject line, tangible asset description, and 1-sentence pitch
- **Recommended lead**: Which of the 3 to write first and why
- **Hand off to**: `/newsletter-flywheel` to produce the full post

## Output Schema

```markdown
# Trend to Newsletter — [Domain]

## Trend Briefing (5-7 signals)
1-7. [signal + source link]

## Audience Pain Map
- Active pains: [...]
- Latent pains: [...]
- Aspirational gaps: [...]

## Cross-Pattern Matrix
[2x2 filled with specific opportunities, priority quadrant highlighted]

## Top 3 Edition Concepts
1-3. [subject line + tangible asset + 1-sentence pitch]

## Recommended Lead
[which of the 3, and why]

## Hand off
/newsletter-flywheel with [chosen concept]
```

## Quality Gate

- [ ] All 5-7 trend signals carry a source link, not asserted from memory?
- [ ] Every PRIORITY-quadrant opportunity names BOTH the trend and the specific pain it intersects — not one or the other?
- [ ] Each of the top 3 concepts names a tangible asset (noun), not just a topic angle?
- [ ] The recommended lead has an explicit reasoning line, not just a pick?
