---
version: alpha
name: {{BRAND_NAME}}
description: A daytime, sober dance party in {{CITY}} for people who want to meet a partner — rendered as an editorial broadsheet that has been left in actual sunlight. Warm terracotta and midnight blue, set on cream that breathes, with a 1978-record-jacket serif carrying the headlines and a clean humanist sans carrying the body. Photography is the protagonist; type is the caption. If a photo could have been taken at 11pm, it does not belong here.

colors:
  # Atomic shades — sourced from real {{CITY}} daylight, not stylized warm filters
  terracotta-700: "#9A3A22"
  terracotta-600: "#B8492E"
  midnight-900: "#0F1A2E"
  cream-50: "#FBF7F0"
  cream-100: "#F5EFE3"
  ink-900: "#1A1814"
  ink-700: "#3A332B"
  slate-500: "#7A6F62"
  gold-600: "#8C6526"

  # Semantic roles
  primary: "{colors.terracotta-600}"
  secondary: "{colors.midnight-900}"
  tertiary: "{colors.gold-600}"
  neutral: "{colors.cream-100}"
  surface: "{colors.cream-50}"
  ink: "{colors.ink-900}"
  body: "{colors.ink-700}"
  muted: "{colors.slate-500}"
  on-primary: "#FBF7F0"
  on-secondary: "#FBF7F0"

  # State + system
  border-hairline: "#E1D6C2"

typography:
  hero-display:
    fontFamily: "GT Sectra, Mortise, IBM Plex Serif, Georgia, serif"
    fontSize: 64px
    fontWeight: 500
    lineHeight: 1.05
    letterSpacing: -0.015em
  headline-lg:
    fontFamily: "GT Sectra, Mortise, IBM Plex Serif, Georgia, serif"
    fontSize: 44px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.01em
  headline-md:
    fontFamily: "GT Sectra, Mortise, IBM Plex Serif, Georgia, serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.005em
  headline-sm:
    fontFamily: "GT Sectra, Mortise, IBM Plex Serif, Georgia, serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.2
  lead:
    fontFamily: "Inter, Plus Jakarta Sans, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.55
  body-lg:
    fontFamily: "Inter, Plus Jakarta Sans, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
  body-md:
    fontFamily: "Inter, Plus Jakarta Sans, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
  body-sm:
    fontFamily: "Inter, Plus Jakarta Sans, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
  label-caps:
    fontFamily: "Inter, Plus Jakarta Sans, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0.12em
  caption:
    fontFamily: "Inter, Plus Jakarta Sans, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
  hand-script:
    fontFamily: "Caveat, Homemade Apple, cursive"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.2

rounded:
  none: 0px
  sm: 2px
  md: 4px
  lg: 8px
  full: 9999px

spacing:
  xs: 4px
  sm: 8px
  md: 12px
  base: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  xxxl: 64px
  gutter: 24px
  margin: 32px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.sm}"
    padding: 16px
  button-primary-hover:
    backgroundColor: "{colors.terracotta-700}"
    textColor: "{colors.on-primary}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.secondary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.sm}"
    padding: 16px
  button-secondary-hover:
    backgroundColor: "{colors.midnight-900}"
    textColor: "{colors.on-secondary}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: 12px
  card-photo:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.md}"
    padding: 0px
  card-text:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.body}"
    rounded: "{rounded.md}"
    padding: 32px
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 14px
  input-focus:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
  divider:
    backgroundColor: "{colors.border-hairline}"
    height: 1px
  badge-event:
    backgroundColor: "{colors.midnight-900}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.sm}"
    padding: 6px
  pull-quote:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.tertiary}"
    typography: "{typography.headline-md}"
    rounded: "{rounded.none}"
    padding: 32px
  caption-meta:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 0px
  body-block:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 24px
---

# {{BRAND_NAME}}

## Overview

{{BRAND_NAME}} is a daytime, sober dance party in {{CITY}} for people who want to meet a partner. The visual system is built to honor that mechanic — every choice has to survive the test: *if a photo could have been taken at 11pm, it fails.* Daytime is not a metaphor here. It is the literal physics of every image, every layout, every interaction.

The aesthetic register is **editorial broadsheet left in actual sunlight.** It borrows the structural confidence of a 1978 vinyl record jacket — heavy serif headlines, generous gutters, photo as protagonist — and renders it in the warm color science of {{CITY}} at 2pm. The intended emotional response is *recognition without performance*: the reader feels found by a room that has already seen them, not pitched by a brand that wants them.

The system is photography-led. Type captions photographs; type does not replace them. The single most important rule, taken verbatim from the Brand Bible §8: *every piece of {{BRAND_NAME}} content should feel like a photograph of a real moment, not a graphic design.* When in doubt: real photo over designed graphic. Real crowd over stock dancers. Real {{FOUNDER_NAME}} over AI portrait. The full photography spec lives in `01-visual/photography-rules.md` and is mandatory reading before any image lands.

## Colors

The palette is sourced from real-world daylight references, not from a digital color wheel. Each token has an intent, a pairing, and a contrast story.

- **Primary — Terracotta 600 (`{colors.primary}` → #B8492E):** The color of late-afternoon light hitting a real wood floor through a real window. It is not a brand color; it is an atmosphere. Used for primary CTAs, the brand wordmark accent, and the single most-important hover state per screen. Never as body text — its 4.6:1 ratio against cream-100 clears WCAG AA for large text only.
- **Secondary — Midnight 900 (`{colors.secondary}` → #0F1A2E):** Deep navy. Grounds the warmth. The sky behind the room, not the room itself. Used for body copy on cream, for headline anchors, for the badge on event passes. 14.2:1 against cream-100 — the workhorse for legibility.
- **Tertiary — Gold 600 (`{colors.tertiary}` → #8C6526):** The accent that earns its place by appearing rarely. Reserved for couples' names in story-capture, for moments worth marking, for the small underline on a manifesto pull-quote. Tuned for WCAG AA on cream-100 (4.7:1). Never used to "spice up" a layout that should hold itself with terracotta and midnight alone.
- **Neutral — Cream 100 (`{colors.neutral}` → #F5EFE3):** The breathable background. Warm, never cold. Reads as honest paper, not as software white. Default canvas for cards, sections, and text-led blocks.
- **Surface — Cream 50 (`{colors.surface}` → #FBF7F0):** A half-step lighter than neutral. Used to layer surfaces — a card on cream-100 sits on cream-50 beneath. Creates depth through tonal stepping, not shadows.
- **Ink — Ink 900 (`{colors.ink}` → #1A1814):** Body and headline text. Not pure black. Carries a barely-perceptible warmth that lets it sit on cream without the optical vibration of #000 against #FFF.
- **Slate 500 (`{colors.muted}` → #7A6F62):** Captions, metadata, dates, photo credits. The connective tissue. 4.7:1 on cream-100 — clears AA for normal text by a comfortable margin.

The palette **excludes** hot pink, club neon, pure white, black-and-chrome, and stylized golden-hour Instagram filter tones. Each exclusion has a brand reason: pink/neon read as hookup culture; pure white reads as corporate wellness; black-and-chrome read as nightclub; stylized golden-hour reads as faked light. Daylight is not a filter we apply; it is the physics we shoot in.

## Typography

Two typefaces, sparingly extended by a third for human-moment punctuation only.

- **GT Sectra (display + headline) —** the serif that carries the heat. Weighted, slightly literary, the kind of letterform that belongs on a vinyl jacket from 1978 or a Sandro photograph caption. Used for `hero-display`, `headline-lg`, `headline-md`, `headline-sm`. Weight is held at 500 — never 700 or 900 — because the system earns gravity through size and color, not through bolding. Acceptable substitutes when GT Sectra is unlicensed: Mortise, IBM Plex Serif, or Georgia in that order.

- **Inter (body + label) —** the humanist sans that carries the words. Readable at 14px on a phone screen at 2pm in actual sunlight. Used for `lead`, `body-lg`, `body-md`, `body-sm`, `label-caps`, `caption`. Weight is 400 for body, 600 for `label-caps` only. Plus Jakarta Sans is the documented substitute.

- **Caveat (`hand-script`) —** the rare punctuation. Used **only** for human moments: {{FOUNDER_NAME}}'s signature, a couple's quote pulled from a story-capture interview, a single line on a thank-you card. Never for navigation, never for body, never for headlines. Hand-script that appears more than once per composition stops feeling human and starts feeling decorative — that is the failure mode to police against.

The typographic discipline lives in the size scale, not in weight stacking. `hero-display` at 64px and `body-md` at 16px do the heavy lifting. There is no `headline-xl-bold` because a headline that needs to be made larger than `hero-display` should instead be carried by a photograph. Type is not the protagonist here.

## Layout

The grid is **body-centered, not screen-centered.** Content maxes at 1180px on desktop — wide enough for editorial photography to sit at full bleed where it earns it, narrow enough that long-form text holds at a 65–75-character measure for genuine readability.

The spacing scale is built on a 4px base, with the working scale at `xs: 4`, `sm: 8`, `md: 12`, `base: 16`, `lg: 24`, `xl: 32`, `2xl: 48`, `3xl: 64`. Section margins between major content blocks default to `2xl` (48px) on desktop, `xl` (32px) on mobile. Cards and stacked content use `lg` (24px) gutters. Vertical rhythm is honored by the line-heights of the typography scale, not by inserting bespoke `<br>` spacers.

Generous whitespace is the foundation, not an afterthought. Crowded layouts read as event-promoter design. {{BRAND_NAME}} is a curated room; the design respects the same principle — fewer things, more space.

Photography is given the **most bleed-width the layout can spare** — a hero photograph spans the full container width on desktop, full screen-width on mobile, and the headline either sits below it (default) or overlays only the lower-left corner against the most negatively-spaced quadrant of the frame. Headlines never compete with the focal subject of the photo.

## Elevation & Depth

{{BRAND_NAME}} is **flat by default with tonal layering.** Depth is conveyed through the cream-50 / cream-100 / cream-200 step, not through drop shadows. A card on the page sits on cream-100 background and has a cream-50 fill — the contrast is gentle but legible.

Shadows are reserved for two cases only: (1) hover state on interactive cards (`0 4px 12px rgba(15, 26, 46, 0.08)` — a midnight-tinted whisper), and (2) the photographic shadow that lives inside the photograph itself, which is the actual sunlight casting onto the floor. We never simulate light. We photograph it.

Floating panels, glass-morphism, neon glow, and animated gradient backgrounds are all forbidden. They smuggle in the visual grammar of a different kind of party.

## Shapes

**Editorial sharpness.** Most surfaces use `rounded.sm` (2px) or `rounded.md` (4px). The 2px radius carries the editorial broadsheet register — visible enough to feel finished, sharp enough to feel disciplined. `rounded.lg` (8px) is reserved for photo cards that need a softer corner against a busy background. `rounded.full` is used only for round photo crops ({{FOUNDER_NAME}}'s portrait, contributor avatars) and never for buttons — pill-shaped buttons read as consumer SaaS, which {{BRAND_NAME}} is not.

Mixing radii within a single composition is forbidden. Pick one register per view. The system holds discipline through geometric consistency.

## Components

- **`button-primary`** — Terracotta 600 background, cream on-primary text, 2px radius, `label-caps` typography. Hover transitions to terracotta-500 (one step lighter) — never to gold or midnight, never to a glow. The button is used for the single most-important action per screen: *Reserve a seat*, *Apply for the next event*, *Read the manifesto*.

- **`button-secondary`** — transparent background, midnight-900 text, 1px hairline border in `border-hairline`, 2px radius. Hover fills the button with midnight-900 and inverts the text to cream. Used for the second action per screen — *Read more*, *See past events*, *Subscribe*.

- **`button-ghost`** — transparent background, ink-900 text, no border, no radius. Used inline as a third-tier interaction — *Skip intro*, *Continue*, *No thanks*.

- **`card-photo`** — cream-50 surface, 4px radius, zero internal padding (the photograph fills the frame edge-to-edge). Captions sit beneath the card, not inside it. The photograph is not "contained" — the card is a frame the photograph leans against.

- **`card-text`** — cream-50 surface, 4px radius, 32px internal padding, body text in ink-700. Used for manifesto pull-quotes, story excerpts, FAQ blocks.

- **`input`** — cream-50 background, ink-900 text, 2px radius, 14px padding. Focus state: terracotta-600 border at 2px (the only place terracotta appears as a thin stroke). No animated label floats. The label sits above the input in `label-caps` and stays still.

- **`badge-event`** — midnight-900 fill, cream text, 2px radius, `label-caps` at 6px padding. Used to mark event date and city on photo cards: `JUNE 2026 · CHICAGO`. Never used to advertise discounts or hype.

- **`divider`** — 1px solid `border-hairline`. The hairline rule from a broadsheet. Used to separate stacked sections in long-form layouts. Never thicker than 1px.

## Do's and Don'ts

**Do:**
- Use a real photograph as the lead element of every primary surface.
- Lead headline copy with the **heart-vs-head** frame; let body-first explain the *how*.
- Hold terracotta back for the single most-important action per screen.
- Set type at 16px body / 64px hero — let scale do the work, not weight.
- Honor the daytime mechanic: every photographic frame must read as obviously daylight, in a real room, with real bodies.
- Reserve hand-script for human moments only — {{FOUNDER_NAME}}'s signature, a couple's quote, a single line on a thank-you card.
- Use cream-50 and cream-100 as tonal layers; let depth come from steps in the cream scale, not from shadows.

**Don't:**
- Use any photograph that could have been taken at 11pm. If you can't tell, kill it.
- Generate photography with AI for any front-of-house use. AI faces are forbidden across the entire system.
- Stack two serifs together. GT Sectra carries the heat alone — pairing it with another display serif breaks the editorial discipline.
- Use hot pink, club neon, pure white, black-and-chrome, or stylized golden-hour filter tones. Each exclusion has a brand reason in `## Colors`.
- Drop in stock dancers, dance-floor silhouettes, lens-flare overlays, or "atmospheric" low-light dance frames — these all smuggle the bar-at-11pm grammar.
- Use hand-script as a default tone. More than one hand-script element per composition stops being human and starts being decorative.
- Use pill-shaped (`rounded.full`) buttons. Pills read as consumer SaaS.
- Animate anything quickly. Motion in this system is slow, room-warm, and considered. No spring physics, no bounce, no kinetic gradients.
- Use the wordmark or any visual element on a layout that has no photograph. The system does not stand on type alone.

---

## Appendix — Photography Direction (binding summary)

Full spec at `01-visual/photography-rules.md`. The compressed rules:

1. **The 11pm test.** *If a photo could have been taken at 11pm in a club, it fails.*
2. **Natural daylight only.** Window light, sun on a wood floor, an overcast {{CITY}} afternoon. No flash. No club lighting. No neon.
3. **Real bodies, real ages, real range.** Ages 28–40, mixed race, mixed body types, mixed gender presentation. No stock dancers. No AI faces.
4. **Slight blur is acceptable.** A genuine moment of motion blur reads as real movement; the over-stabilized stock-dancer frame reads as fake.
5. **No fake golden-hour filters.** Color grading is minimal; daylight color temperature is preserved.
6. **No look-at-camera-and-smile group shots.** Candid moments only. People listening to each other. People mid-laugh. People standing the way they actually stood when the song shifted.
7. **AI image generation, when used at all, is daytime-locked.** Prompts must include daytime, natural light, real-room context. Never night-coded prompts.

## Appendix — Motion Principles (binding summary)

{{BRAND_NAME}} moves slowly. The pace of the brand on screen mirrors the pace of the room — body-warm, considered, never frenetic.

- Default transition: 200–300ms, ease-out. Never bounce, never spring.
- Hover states: a single tonal shift, no movement.
- Page transitions: a single cross-fade, never a slide-and-wipe.
- Scroll-triggered animation: gentle parallax on photographic blocks (≤ 15% movement at scroll speed), nothing else.
- Forbidden: bounce, spring physics, parallax >20%, any animated gradient, any flicker, any kinetic typography.

---

## Cross-references (BOS spine)

- {{FOUNDER_NAME}}'s anchor §3.1 (Line 1: Daytime), §3.2 (Line 2: Sober) — the mechanic this visual system honors
- Manifesto v2 paragraphs 1–2 — the source of *"the way they moved, the way they listened, the way they were standing when the song shifted"*
- A1-reconciliation.md §3 conflict #4 — the daytime-as-mechanic ruling that supersedes the legacy "{{CITY}} at golden hour" metaphor
- A1-reconciliation.md §6 cascade #1 — *"Every visual brief, venue pitch, and asset reflects daytime. No 'feels like late afternoon' imagery — actual daylight."*
- Brand Bible §8 — strategic intent for visual; this DESIGN.md is the executable spec
- `01-visual/photography-rules.md` — full photographer brief
- `01-visual/aesthetic-references.md` — mood board with 18 references
- `01-visual/component-tokens.md` — production component spec
- `01-visual/brand-library-entry.md` — entry for `knowledge/design-libraries/brands/{{BRAND_NAME_LOWER}}/`
