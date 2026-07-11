---
name: "Visual Direction Generator"
source_prompt: "skills/andy-lo-premium-websites/references/prompts/01-visual-direction-generator.md"
skill: andy-lo-premium-websites
standard: structure-pure-v2
refactored: 2026-07-11
---

# Visual Direction Generator

## Purpose
Establish the complete visual language of a website before touching any layout or code tool. This prompt produces two "bookend frames" — a starting frame and an ending frame — that define the aesthetic arc of the entire site.

## System Prompt

You are Andy Lo, a premium AI website creator who builds $10K-$20K quality websites using Google's free AI tools. Your core principle: **visual direction comes before everything**. You don't build until you know exactly what the site should *feel* like.

## User Prompt

```
I need to establish the visual direction for a website project.

**Project Details:**
- Brand/Client: {{BRAND_NAME}}
- Industry: {{INDUSTRY}}
- Mood/Feel: {{MOOD}} (e.g., cinematic, minimal, bold, organic, tech-forward)
- Reference URL or brand (if any): {{REFERENCE}}
- Primary product/service: {{PRODUCT}}
- Hero section focus: {{HERO_FOCUS}}

**Generate the following:**

### 1. Starting Frame Prompt (for Nano Banana / Whisk)
Write a precise image generation prompt for the OPENING frame of the website. This frame defines:
- Color palette (specific hex codes)
- Lighting direction and quality
- Composition and depth
- Texture and material feel
- Overall mood

The prompt should be specific enough that the AI produces a consistent result, but creative enough to produce something unique — NOT generic stock-photo style.

### 2. Ending Frame Prompt (for Nano Banana / Whisk)
Write a precise image generation prompt for the CLOSING frame — the visual arc's destination. This should:
- Share the same color palette as the starting frame
- Shift the composition or perspective to create visual movement
- Feel like the "resolution" of the opening frame's "tension"
- Maintain brand coherence while introducing visual progression

### 3. Motion Prompt (for Google Flow)
Write the animation prompt that describes how the starting frame should TRANSITION to the ending frame. Include:
- Speed and pacing (slow dissolve? dynamic pan? gentle float?)
- What elements move and how
- The emotional arc of the animation

### 4. Supporting Asset Prompts
Generate 2-3 additional image prompts for secondary sections (features, about, testimonials) that maintain the established visual language.

### 5. Visual Direction Summary
A 2-3 sentence "art director's brief" that anyone on the team could read to understand the site's visual intent.

**Rules:**
- No generic stock imagery language ("professional businessman" etc.)
- Every prompt must specify lighting, color, and composition
- The starting and ending frames should look like they belong to the SAME brand
- Prefer cinematic, editorial, or architectural photography styles over corporate
```

## Output Contract
- A starting frame image-generation prompt (Nano Banana/Whisk), specifying palette, lighting, composition, texture, mood
- An ending frame image-generation prompt sharing the starting frame's palette, with a shifted composition/perspective
- A motion prompt (Google Flow) describing the transition from starting to ending frame — pacing, moving elements, emotional arc
- 2-3 supporting asset prompts for secondary sections, consistent with the established visual language
- A 2-3 sentence visual direction summary ("art director's brief")

## Output Skeleton
```
STARTING FRAME PROMPT
[image generation prompt — palette (hex codes), lighting direction/quality, composition/depth, texture, mood; no generic stock-photo language]

ENDING FRAME PROMPT
[image generation prompt — same palette as starting frame, shifted composition/perspective, reads as "resolution" of the starting frame]

MOTION PROMPT (Google Flow)
[pacing descriptor] · [elements that move and how] · [emotional arc from start to end]

SUPPORTING ASSET PROMPTS
1. [section name] — [prompt: palette, lighting, composition, consistent with bookend frames]
2. [section name] — [prompt]
3. [section name — optional] — [prompt]

VISUAL DIRECTION SUMMARY
[2-3 sentence art director's brief anyone on the team could read to understand the site's visual intent]
```

## Quality Gate
- [ ] Every prompt (starting, ending, supporting) specifies lighting, color, and composition explicitly — none left implicit
- [ ] Starting and ending frames share the same color palette and read as the same brand
- [ ] No generic stock-photo language anywhere ("professional businessman," "happy team," etc.)
- [ ] The motion prompt describes pacing, moving elements, and an emotional arc — not just "animate frame 1 to frame 2"
- [ ] The visual direction summary is short enough (2-3 sentences) that a teammate who never saw the frames could still brief off it

## Deploy When
- Starting any new website project
- Creating a premium landing page
- Building a personal brand site
- Refreshing an existing site's visual identity

## Genius Patterns Applied
- Visual Direction First (#1)
- Bookend Frame Architecture (#2)
- Reference Image Anchoring (#5)
