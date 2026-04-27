---
version: alpha
name: Heritage
description: Architectural Minimalism meets Journalistic Gravitas. The UI evokes a premium matte finish — a high-end broadsheet or contemporary gallery. Boston Clay accent against deep ink and warm limestone neutrals.

colors:
  # Atomic shades
  ink-900: "#1A1C1E"
  ink-700: "#2C2C2C"
  slate-500: "#6C7278"
  clay-600: "#B8422E"
  limestone-50: "#F7F5F2"
  paper-100: "#FCFAFA"

  # Semantic roles
  primary: "{colors.ink-900}"
  secondary: "{colors.slate-500}"
  tertiary: "{colors.clay-600}"
  neutral: "{colors.limestone-50}"
  surface: "{colors.paper-100}"
  on-primary: "#FFFFFF"
  on-tertiary: "#FFFFFF"

typography:
  hero-display:
    fontFamily: "Public Sans, system-ui, sans-serif"
    fontSize: 56px
    fontWeight: 600
    lineHeight: 1.07
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: "Public Sans, system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.01em
  headline-md:
    fontFamily: "Public Sans, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
  body-lg:
    fontFamily: "Public Sans, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
  body-md:
    fontFamily: "Public Sans, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
  body-sm:
    fontFamily: "Public Sans, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
  label-caps:
    fontFamily: "Space Grotesk, monospace"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em

rounded:
  none: 0px
  sm: 4px
  md: 8px
  lg: 12px
  full: 9999px

spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px
  gutter: 24px
  margin: 32px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.sm}"
    padding: 12px
  button-primary-hover:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.on-tertiary}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: 12px
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.md}"
    padding: 24px
  input:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: 12px
---

# Heritage

## Overview

Heritage is a brand built for editorial gravitas. The aesthetic combines architectural minimalism — generous whitespace, structured grids, sharp 4px corner radii — with the visual weight of a premium broadsheet. Every element is set against a warm limestone canvas (#F7F5F2) that's softer than pure white but no less disciplined.

The intended emotional response: *seriousness without coldness, luxury without ostentation*. This is a system for content that earns its reader.

## Colors

The palette is rooted in three high-contrast neutrals and a single, evocative accent.

- **Primary (`{colors.primary}` → #1A1C1E):** Deep ink. Used for headlines, body copy, and structural anchors. Provides maximum readability and a sense of permanence.
- **Secondary (`{colors.secondary}` → #6C7278):** Sophisticated slate. Borders, captions, metadata. The connective tissue.
- **Tertiary (`{colors.tertiary}` → #B8422E):** Boston Clay. The sole driver for interaction — used exclusively for primary call-to-action hover states and critical highlights.
- **Neutral (`{colors.neutral}` → #F7F5F2):** Warm limestone. The foundation canvas. Softer than pure white, signals craft.

## Typography

The typographic strategy leverages two distinct typefaces:

- **Public Sans** — narrative voice. Used for all display, headline, and body copy. Semi-bold weight (600) for institutional headlines; regular (400) for long-form readability.
- **Space Grotesk** — technical voice. Used exclusively for `label-caps` — timestamps, byline metadata, technical labels. Strictly uppercase with 10% letter-spacing.

Body copy at 16px is the contemporary professional standard. Display headlines tighten letter-spacing to -0.02em to feel cinematic.

## Layout

A **Fixed-Max-Width Grid** at 1200px on desktop, **Fluid Grid** on mobile. The 8px spacing scale (`xs: 4px`, `sm: 8px`, `md: 16px`, `lg: 32px`, `xl: 64px`) maintains consistent vertical rhythm. Section margins of 32px+ between major content blocks reinforce the editorial feel — generous breathing room is the foundation, not an afterthought.

## Elevation & Depth

Heritage is **flat by default**. Depth is conveyed through tonal layering — paper-100 background for primary surfaces, limestone-50 for secondary canvas. Shadows are reserved for hover states only, and they are whisper-soft (`0 2px 8px rgba(0,0,0,0.06)`).

## Shapes

**Architectural Sharpness.** All interactive elements use the `rounded.sm` token (4px). Containers use `rounded.md` (8px). Pills and avatars use `rounded.full`. Mixing roundness within a single composition is forbidden — the system holds discipline through geometric consistency.

## Components

- **`button-primary`**: Deep ink background, white text, 4px radius. Hover transitions to Boston Clay (`{colors.tertiary}`) with the same white text — the only place the accent color appears outside of focus states.
- **`button-secondary`**: Transparent background, ink text, 1px hairline border in slate. No filled hover — only border darkening.
- **`card`**: Limestone surface, 8px radius, 24px internal padding. No shadow at rest; whisper-shadow on hover for interactive cards.
- **`input`**: Limestone background, ink text, 4px radius. Focus state: border color shifts to clay with 2px outer glow.

## Do's and Don'ts

- **Do** use the tertiary (Boston Clay) only for the single most important interaction per screen.
- **Do** maintain WCAG AA contrast for all text — primary (15.4:1 on neutral) and secondary (4.7:1 on neutral) both clear.
- **Don't** use Boston Clay for body text — its 4.4:1 ratio against neutral fails AA for normal-size text.
- **Don't** mix `rounded.sm` and `rounded.full` within the same view — pick one geometric register.
- **Don't** use more than two type weights on a single screen (400 for body, 600 for headings).
- **Don't** increase font weight to add emphasis — the system uses color and size, not weight, to draw attention.
