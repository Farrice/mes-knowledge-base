---
name: "AI Carousel Content Engine — Style Board"
source_prompt: born-v2
skill: ai-carousel-content-engine
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are building a carousel style board — the reference-before-generation stage the AI Carousel Content Engine treats as a taste shortcut, not decoration. Genius Pattern 3: "Reference before generation — style direction, mood boards, and brand tokens prevent generic output." Hidden Knowledge is more specific: "A single strong reference image or style board communicates more design intent than a vague style paragraph. Build references once and reuse them." Workflow 05 (Carousel Style Match) frames this as a pre-production step, run before recurring carousel generation begins, not per-carousel.

## Input Required

- `[BRAND_OR_CLIENT]` — whose visual system this is for.
- `[REFERENCE_INPUT]` — mood board output, a `/design-md-synthesize` brand/design system, existing brand assets, or a raw style brief in prose. If none of these exist yet, say so explicitly rather than inventing a brand system from nothing.
- `[PLATFORM_TARGETS]` — Instagram, LinkedIn, or both — affects aspect ratio and density tolerance.
- `[RECURRING]` — is this a one-off carousel or the style system for a recurring content pipeline? Recurring use raises the bar: this board must be durable and reused, not re-derived each time.

## Execution Protocol

**Step 1 — Source the reference before writing the board.** Per workflow 05's sequencing: if a mood board or brand/design system doesn't already exist, run `/mood-board` or `/design-md-synthesize` first (or note that this step is outstanding) rather than fabricating palette and typography choices with no grounding. A style board built from nothing is exactly the "vague style paragraph" the source material warns against.

**Step 2 — Capture the four fields the system actually uses**, matching the shape the engine's own default style system carries: name, visual style (a full descriptive sentence — genre, brand tier, contrast level, whitespace treatment, clutter tolerance), palette (a short hex list — ground color, light/paper color, one or two accents, one neutral line color), typography (headline treatment, body treatment, label treatment as three distinct decisions, not one blanket font note), composition (the compositional rules that will apply to every slide: ideas-per-slide, visual-anchor count, copy density, numbering/consistency treatment).

**Step 3 — Resolve palette and typography to specifics, not adjectives.** "Bold" or "modern" alone is not a style board — name the actual hex values, the actual typeface category and weight behavior (e.g., "bold geometric sans headlines, readable modern sans body, small uppercase labels"), and the actual compositional constraint (e.g., "one core idea per slide, one visual anchor, short supporting copy, consistent slide number").

**Step 4 — If a custom reference direction exists, preserve it as its own field rather than folding it silently into the generic style description**, so future carousels can trace back to what the client or brand actually supplied versus what this stage inferred. Note explicitly where the board is inferring versus where it is quoting the reference.

**Step 5 — Build for reuse.** This board should compound across every future carousel for this brand/client — write it as a standing reference, not a one-time creative brief. If `[RECURRING]` is true, flag any field that feels situational (tuned to one specific carousel topic) rather than durable, and generalize it.

## Output Contract

A style board with exactly these fields: Name, Visual Style (one substantive descriptive passage), Palette (hex list, 4-6 colors with a stated role for each), Typography (headline / body / label treatments named separately), Composition (the compositional rule set applied to every slide), and — when a custom reference was supplied — a Custom Reference Direction field preserving it verbatim or near-verbatim.

## Output Skeleton

```
# Style Board — [BRAND_OR_CLIENT]

## Name
[style system name]

## Visual Style
[full descriptive sentence: genre, brand tier, contrast, whitespace, clutter tolerance]

## Palette
- [hex] — [role, e.g. ground]
- [hex] — [role, e.g. light/paper]
- [hex] — [role, e.g. primary accent]
- [hex] — [role, e.g. secondary accent]
- [hex] — [role, e.g. neutral line]

## Typography
Headline: [treatment]
Body: [treatment]
Labels: [treatment]

## Composition
[rule set: ideas-per-slide, visual-anchor count, copy density, numbering/consistency]

## Custom Reference Direction (if supplied)
[verbatim or near-verbatim reference input, with inferred vs. quoted noted]
```

## Quality Gate

- Is every palette entry a real hex value with a stated role, not an adjective ("modern," "clean")?
- Are headline, body, and label typography treatments specified as three distinct decisions rather than one blanket font note?
- Does the composition section state a concrete ideas-per-slide and copy-density rule, not just "keep it simple"?
- If `[REFERENCE_INPUT]` was absent, does the output say so plainly rather than presenting an invented brand system as grounded?
- Is this board written for reuse across future carousels (durable), not tuned only to one carousel's topic?

## Creative Latitude

Resolving a rough reference or brand feel into concrete palette and typography decisions is a genuine taste call — this is where design judgment lives, not template-filling. When the brand or platform calls for something outside the engine's default premium-operator preset (a warmer palette, a serif headline, a denser composition for a data-heavy niche), make that call and justify it against the audience and platform rather than defaulting to the preset for safety. The goal is a board specific enough that two different operators using it would land on visually consistent output — genericism here is the failure mode, not overreach.

## Deploy When

- Before recurring carousel generation begins for a brand or client, or whenever a one-off carousel needs a resolved visual system before the design prompt stage runs.
