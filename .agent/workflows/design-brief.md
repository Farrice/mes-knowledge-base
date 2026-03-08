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

### 10b. Pencil Execution Prompt (if handoff target is Pencil)

After generating the human-readable brief, also produce a **Pencil Execution Prompt** — a phased, frame-first instruction set structured for how Pencil's AI agents actually process commands. This is the copy-paste artifact that goes into Pencil.

**Why a separate format**: Pencil agents operate via MCP tools on named frames. They need explicit spatial anchors, action verbs, and incremental instructions — not prose descriptions. A monolithic brief will overwhelm or crash the agent.

Generate the Pencil Execution Prompt in this structure:

```
# PENCIL EXECUTION PROMPT: [Title]

## Phase 1 — Setup & Frames
Paste this first. Wait for frames to appear before proceeding.

Design a LinkedIn carousel with the following setup:
- Style: [mood description — e.g., "dark, premium, editorial"]
- Create [N] separate square frames (1080x1080px each), arranged horizontally:
  - "Slide-1-Cover"
  - "Slide-2-[Purpose]"
  - "Slide-3-[Purpose]"
  - ... (one per slide)
- Background color for all frames: [hex]
- Font setup: [Primary font] for headlines, [Secondary font] for body text

## Phase 2 — Slide Content
Paste one slide at a time, or all together if the agent handles it.

### Slide 1 — Cover
In frame "Slide-1-Cover":
- Add [element type] "[exact text]" — [font], [size]px, [weight], color [hex], [alignment]
- Add [element type] "[exact text]" — [font], [size]px, [weight], color [hex], [alignment]
- Add [decorative element] — [color hex], [dimensions], [position]

### Slide 2 — [Purpose]
In frame "Slide-2-[Purpose]":
- ...

(Repeat for all slides)

## Phase 3 — Polish
Paste after reviewing the rendered slides.

- [Specific adjustments: spacing, alignment, texture, color tweaks]
- Verify all text is legible and within frame boundaries
- Check visual consistency across all slides
```

**Format rules for Pencil prompts:**
- Use action verbs: "Add", "Create", "Set", "Apply" — not "The label should be..."
- Reference frames by exact name in every instruction
- Specify font, size, weight, color, and alignment for every text element
- Keep each phase self-contained so it can be pasted independently
- Include exact text content in quotes — never use placeholders

---

## Options

- **`--carousel`**: Optimize for Instagram carousel (1080x1350, 4:5, swipe format, 5-10 slides)
- **`--poster`**: Optimize for single-frame graphic (typography-dominant)
- **`--landing`**: Optimize for landing page (1440px, scroll sections)
- **`--deck`**: Optimize for presentation slides (16:9, 1920x1080)
- **`--no-copy`**: Skip Kallaway copy generation — typography and visual direction only
- **`--brand [name]`**: Load brand guidelines from `brand-guidelines/` if available

---

## Pencil Handoff Best Practices

When handing off to Pencil's AI agents:

1. **Select a style guide in Pencil first** (Shadcn, Halo, Lunaris, or Nitro) — this constrains the AI's visual decisions and prevents generic defaults
2. **Use Claude Code CLI for execution**, not Pencil's native chat — the CLI gives more consistent results per BetterStack's testing
3. **Paste Phase 1 first**, wait for frames to appear on canvas, then proceed to Phase 2
4. **If the agent crashes or stalls**, reduce to single-slide prompts — paste one slide's instructions at a time
5. **Name frames semantically** (Slide-1-Cover, Slide-2-Problem) — these names travel through MCP and help the agent understand structure
6. **After Pencil builds the design**, run `/design-taste-gate` to audit quality and get specific refinement directives
