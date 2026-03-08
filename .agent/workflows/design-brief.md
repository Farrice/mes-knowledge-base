---
description: Generate a complete creative direction brief (typography, color, copy, layout) for any visual asset. Optimized for handoff to Pencil or external design tools.
---

# /design-brief — Creative Direction Generator

Takes a raw concept and produces a complete, copy-pasteable design brief — typography system, color palette, per-section copy, layout composition, and AI imagery prompts. Designed for handoff to Pencil's native AI agents or any visual design tool.

## Usage

```
/design-brief [raw concept]
/design-brief --carousel "inspirational post about morning routines"
/design-brief --poster "event flyer for a jazz night"
/design-brief --landing "SaaS product launch page"
/design-brief --deck "investor pitch for AI startup"
```

## Expert Stack

| Expert | Genius File | Role |
|--------|------------|------|
| **Kittl** | `skills/kittl-graphic-design/genius.md` | Typography, font psychology, composition, AI image prompts |
| **Kallaway** | `skills/kallaway-content-psychology/genius.md` | Hook engineering, viral packaging, content psychology |
| **Oren** | `skills/oren-taste-development/genius.md` | CEV pre-check (Composition, Effectivity, Vibes) |

## Steps

### 1. Capture Concept

Parse the raw idea and identify:
- **Asset type**: Carousel, poster, landing page, slide deck, social graphic, etc.
- **Platform**: Instagram, LinkedIn, web, print, presentation
- **Audience**: Who sees this? What do they care about?
- **Mood/vibe**: Modern, luxury, editorial, playful, bold, minimal, etc.
- **Constraints**: Brand colors, existing fonts, specific copy, dimensions

If an `--option` flag is provided, use it to set the asset type and platform defaults:
- `--carousel` → Instagram, 1080x1350 (4:5), 5-10 slides, swipe-optimized
- `--poster` → Single frame, print or social, typography-dominant
- `--landing` → Web, 1440px wide, scroll sections, hero + features + CTA
- `--deck` → 16:9, 1920x1080, slide sequence

### 2. Sharpen (if needed)

Score the concept on DICE (Deliverable, Intended audience, Context, End state):
- Score 4-5: Proceed directly.
- Score 1-3: Ask 1-2 focused clarifying questions. One round max. Fill in what you can infer.

### 3. Load Kittl Genius — Typography & Composition Intelligence

Read `skills/kittl-graphic-design/genius.md`. Apply these patterns:

- **Pattern 1** (Mood-First Font Selection): Write 3 mood words from the concept → select fonts that match
- **Pattern 2** (Serif/Sans Mood Mapping): Ethereal/Elegant/Nostalgic = Serif first. Techy/Modern/Sporty = Sans first.
- **Pattern 3** (Height-Width Contrast Pairing): Headline font's dominant trait (tall/condensed OR wide/extended) → pair with opposite
- **Pattern 4** (Letter Spacing as Mood): Modern/Editorial = tighten. Luxurious/Minimal = loosen.
- **Pattern 5** (Line Spacing Compression): Display type = reduce line height until lines nearly touch but remain legible
- **Pattern 11** (Gray Hierarchy): Primary = full color, secondary = 40-60% opacity/gray
- **Tacit 1** (90s Serif Secret): When brief calls for "timeless but not stuffy," reach for 90s serif revivals
- **Tacit 5** (Texture Blending): Note where texture/grain overlays would elevate the design

### 4. Generate Typography System

Produce a complete type system:

```
PRIMARY FONT: [Name] — [Weight range] — Used for: [headlines, display, etc.]
SECONDARY FONT: [Name] — [Weight range] — Used for: [body, labels, etc.]

TYPE SCALE:
- Display/Hero: [Xpx], [weight], tracking [Xpx], line-height [X]
- Title: [Xpx], [weight], tracking [Xpx], line-height [X]
- Subtitle: [Xpx], [weight], tracking [Xpx], line-height [X]
- Body: [Xpx], [weight], tracking [Xpx], line-height [X]
- Label/Caption: [Xpx], [weight], tracking [Xpx], line-height [X]

RATIONALE: [Why this pairing works — cite Kittl patterns]
```

### 5. Generate Color Palette

Produce 5-7 colors with usage rules:

```
PALETTE:
- Background: [hex] — [usage note]
- Primary Text: [hex] — [usage note]
- Secondary Text: [hex] — [usage note]
- Accent: [hex] — [usage note]
- Muted/Tertiary: [hex] — [usage note]
- Highlight (optional): [hex] — [usage note]
- Dark Surface (optional): [hex] — [usage note]

MOOD RATIONALE: [Why these colors — warm/cool, contrast ratio, emotional resonance]
GRADIENT (if applicable): [Start] → [End], [angle], [type: linear/mesh/radial]
TEXTURE NOTE: [Where grain, noise, or blending modes would add depth]
```

### 6. Load Kallaway Genius — Content Psychology

Read `skills/kallaway-content-psychology/genius.md`. Apply relevant patterns for copy:

- Hook engineering (curiosity gaps, pattern interrupts, dopamine architecture)
- Scroll-stop mechanics (what makes someone pause)
- Retention architecture (what keeps them reading/swiping)
- CTA psychology (what drives action)
- Shareability triggers (what makes someone send this to a friend)

### 7. Generate Copy/Content

Per-slide or per-section, produce:

```
SLIDE/SECTION 1 — [Purpose: Cover/Hook/Content/CTA]
  Title: [text]
  Subtitle: [text, if applicable]
  Body: [text, if applicable]
  Label: [text, if applicable]
  Psychology note: [Why this works — cite Kallaway pattern]

SLIDE/SECTION 2 — [Purpose]
  ...
```

For carousels: Cover hook → 3-5 content slides → CTA close.
For landing pages: Hero → social proof → features → testimonials → CTA.
For decks: Cover → problem → solution → evidence → ask.

### 8. Compose Layout & Composition Spec

Per-slide or per-section:

```
SLIDE/SECTION 1:
  Layout: [vertical/horizontal/grid]
  Alignment: [left/center/asymmetric]
  Primary element: [what dominates — text, image, number]
  Secondary elements: [supporting items]
  Spacing rhythm: [gaps between elements]
  Decorative elements: [abstract shapes, lines, orbs, texture]
  Background: [solid/gradient/image]
  Image direction (if applicable): [AI prompt for background or hero image]
```

### 9. CEV Pre-Check

Load Oren's CEV matrix (Pattern 6 from `skills/oren-taste-development/genius.md`):

- **Composition**: Is the brief's layout spec well-structured? Would it produce a balanced design?
- **Effectivity**: Will this design achieve its purpose? (Stop scroll, communicate message, drive action)
- **Vibes**: Does the palette + type + composition create the intended emotional resonance?

If any dimension scores below 7/10, revise the relevant section before outputting.

### 10. Report

Present the complete design brief in a single, formatted block. Use clear headers. The brief should be directly copy-pasteable into Pencil, Figma, Canva, or any design tool's AI assistant.

```
# Design Brief: [Title]

## Asset Type & Platform
[Type, dimensions, platform, slide count if carousel]

## Mood & Direction
[3-5 mood words, aesthetic reference, emotional target]

## Typography System
[Full type system from Step 4]

## Color Palette
[Full palette from Step 5]

## Content
[Per-slide/section copy from Step 7]

## Layout & Composition
[Per-slide/section layout spec from Step 8]

## AI Imagery Prompts
[Ready-to-use prompts for AI image generation, if applicable]

## CEV Pre-Check
C: [X]/10 | E: [X]/10 | V: [X]/10
[Any notes]
```

## Options

- **`--carousel`**: Optimize for Instagram carousel (1080x1350, 4:5, swipe format, 5-10 slides)
- **`--poster`**: Optimize for single-frame graphic (typography-dominant)
- **`--landing`**: Optimize for landing page (1440px, scroll sections)
- **`--deck`**: Optimize for presentation slides (16:9, 1920x1080)
- **`--no-copy`**: Skip Kallaway copy generation — typography and visual direction only
- **`--brand [name]`**: Load brand guidelines from `brand-guidelines/` if available
