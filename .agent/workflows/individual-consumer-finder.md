---
description: Find the ONE real, specific individual who embodies your ideal consumer — with search methodology and candidate profiles
---

# /individual-consumer-finder — Real Human Consumer Search

Deploy Dai Media's Crown Jewel #2 — the Individual Consumer Finder. Creates a step-by-step methodology to find ONE real, specific person who embodies the ideal consumer. Not a persona — a findable human being you could have coffee with.

## Inputs Required

Ask the user for (or extract from context):

1. **[BRAND NAME]**: The brand seeking its individual consumer
2. **[BRAND CATEGORY]**: Industry/product category
3. **[BRAND ESSENCE]**: What the brand stands for (2-3 sentences)
4. **[PRICE POINT/POSITIONING]**: Where the brand sits in market
5. **[EXISTING AUDIENCE SIGNALS]**: Optional — current customers, engagement patterns

> **Best with**: A Consumer Posture Profile (from `/consumer-posture-profile` or `/icp-build`). If you have one, feed it as context — the finder will be dramatically more precise.

## Steps

### 1. Load Expert Context
// turbo
Read these files in order:
1. `/Users/farricecain/Google Antigravity/skills/dai-media-consumer-posture/genius.md`
2. `/Users/farricecain/Google Antigravity/skills/dai-media-consumer-posture/references/prompts/individual-consumer-finder.md`

You are Dai Media executing investigative consumer search. Most brand owners think in groups. Your breakthrough: find ONE real person who exists in the world.

### 2. Execute the Search Architecture

Following the prompt's execution protocol:

1. **DECODE** — Translate brand essence into human characteristics — personality traits, lifestyle patterns, psychological profile
2. **IDENTIFY** — Signal environments: platforms, communities, physical spaces where this individual appears. Think counterintuitively — where they WOULDN'T expect to be found.
3. **DEFINE** — Recognition criteria: what they post, how they speak, what they reference, what they refuse. Include positive markers (5) AND negative markers (5).
4. **GENERATE** — Search methodology: concrete, step-by-step protocol using available tools, organized into a 7-day timeline.
5. **PRODUCE** — 3 candidate profiles with enough specificity to recognize them in the wild.
6. **ESTABLISH** — Validation questions to confirm you found the right person.

### 3. Deliver Output

Produce a structured deliverable containing:
- **The Individual Decoded** — characteristics derived from brand essence
- **Signal Environments** — where to look (digital + physical, with specific platform locations)
- **Recognition Criteria** — 5 positive markers, 5 negative markers
- **Search Methodology** — step-by-step 7-day timeline
- **3 Candidate Profiles** — vivid, findable-feeling individuals
- **Validation Protocol** — questions to confirm you found the right person
- **The Coffee Test** — what a 20-minute conversation would reveal that a survey never could

## Quality Gate
- Can the brand owner **identify a specific real individual within 7 days** using this protocol?
- Are signal environments **specific** (not just "social media" — which subreddit, which type of LinkedIn post)?
- Are candidate profiles vivid enough to **recognize in the wild**?
- Does the Coffee Test reveal something **no survey could**?

## Standalone vs. Pipeline
This command runs independently. For the full ICP pipeline, use `/icp-deep-dive`. Used as Pipeline Stage 4 in `/icp-build`.
