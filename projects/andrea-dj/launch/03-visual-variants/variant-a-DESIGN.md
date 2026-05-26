---
version: alpha
name: Resonance — Variant A — Editorial Broadsheet
description: The v1 direction pushed to its fullest expression. A daytime, sober dance room in Chicago, rendered as a 1978 record-jacket left in actual sunlight. Warm terracotta and midnight blue on cream that breathes, with a heavy literary serif (GT Sectra) carrying every headline and a humanist sans carrying the body. Generous gutters, editorial discipline, a hairline rule under every category mark. The room you walk into and recognize without being told. Photography is the protagonist; type is the caption. If a photo could have been taken at 11pm, it does not belong here.

colors:
  # Atomic shades — sourced from late-afternoon Chicago daylight on real wood floors, not stylized warm filters
  terracotta-700: "#9A3A22"
  terracotta-600: "#B8492E"
  midnight-900:  "#0F1A2E"
  midnight-700:  "#1F3151"
  cream-50:      "#FBF7F0"
  cream-100:     "#F5EFE3"
  cream-200:     "#EDE3CE"
  ink-900:       "#1A1814"
  ink-700:       "#3A332B"
  slate-500:     "#7A6F62"
  gold-600:      "#8C6526"

  # Semantic roles
  primary:    "{colors.terracotta-600}"
  secondary:  "{colors.midnight-900}"
  tertiary:   "{colors.gold-600}"
  neutral:    "{colors.cream-100}"
  surface:    "{colors.cream-50}"
  ink:        "{colors.ink-900}"
  body:       "{colors.ink-700}"
  muted:      "{colors.slate-500}"
  on-primary: "#FBF7F0"
  on-secondary: "#FBF7F0"

  # State + system
  border-hairline: "#E1D6C2"

typography:
  hero-display:
    fontFamily: "GT Sectra, Mortise, IBM Plex Serif, Georgia, serif"
    fontSize: 72px
    fontWeight: 500
    lineHeight: 1.02
    letterSpacing: -0.018em
  headline-lg:
    fontFamily: "GT Sectra, Mortise, IBM Plex Serif, Georgia, serif"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.08
    letterSpacing: -0.012em
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
    fontSize: 21px
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
    letterSpacing: 0.14em
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
  xxxl: 72px
  gutter: 32px
  margin: 48px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.sm}"
    padding: 18px
  button-primary-hover:
    backgroundColor: "{colors.terracotta-700}"
    textColor: "{colors.on-primary}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.secondary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.sm}"
    padding: 18px
    border: "1px solid {colors.border-hairline}"
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
    rounded: "{rounded.sm}"
    padding: 0px
  card-text:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    padding: 32px
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 14px
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
    rounded: "{rounded.sm}"
    padding: 24px
---

# Resonance — Variant A — Editorial Broadsheet

## Overview

This is the v1 direction taken to its fullest expression — not a redesign, an arrival. Variant A is what Resonance looks like when the editorial-broadsheet instinct is allowed to finish its sentence. A 1978 record-jacket grammar (Reid Miles, Blue Note, ECM) on cream paper, in actual Chicago daylight. The serif is heavy, the gutters are wide, the hairline rule under every category mark is honest 1-pixel ink. The atmosphere is *recognition*: the reader sees the room before they read the headline, and the headline confirms what they already felt.

Strategic position: **the literary register of a curated room.** This variant says *we take the room seriously, and the design takes itself seriously the same way.* It is the variant that earns press coverage, gets reposted by *The Gentlewoman*–reading account, and lands in the hands of an arts-worker ICP who notices that the typography respects them.

Who in the audience this variant reaches that the others might not: the literary-leaning ICP, the design-conscious Profile #1 arts-worker, the journalist who would read a press one-sheeter, the venue owner who needs to see that this is a real cultural project. Variant A is the variant a *Sandro Miller subject* would recognize. It is also the lowest-risk choice — it is the canon, refined, not reinvented.

What separates it from B and C: A is **typographically heavier** than C (which is quiet-luxury restraint) and **culturally less specific** than B (which is Latin-American daylight). A is the universal-editorial variant — the one that translates anywhere a broadsheet would translate.

## Colors

The palette extends the v1 anchor with two added tonal steps for finer layering: a cream-200 for deepest paper-tone and a midnight-700 for sub-anchor reads (e.g., footer panels, secondary headlines on photo).

- **Primary — Terracotta 600 (`#B8492E`).** The color of late-afternoon light hitting a real wood floor through a real window. Used for primary CTAs, the wordmark accent on photographic surfaces, and the single most-important hover state per screen. Never as body text. Contrast against cream-100: 4.6:1 (WCAG AA Large).
- **Secondary — Midnight 900 (`#0F1A2E`).** Deep navy. Grounds the warmth. The sky behind the room, not the room itself. Used for body copy on cream, headline anchors, event badges. 14.2:1 against cream-100 (WCAG AAA).
- **Midnight 700 (`#1F3151`).** A softer midnight for sub-headlines, hover-fill on photo cards, the lower-band of editorial spreads where a softer anchor reads better than the full midnight. 9.8:1 against cream-100 (WCAG AAA).
- **Tertiary — Gold 600 (`#8C6526`).** The accent that earns its place by appearing rarely. Reserved for couples' names in story-capture, for a single underlined word in a manifesto pull-quote, for the lower-right terracotta-or-gold mark on event tickets. 4.7:1 on cream-100 (WCAG AA).
- **Neutral — Cream 100 (`#F5EFE3`).** The breathable background. Warm, never cold. Honest paper.
- **Surface — Cream 50 (`#FBF7F0`).** A half-step lighter; cards sit on cream-100 with cream-50 fills, creating depth through tonal stepping.
- **Cream 200 (`#EDE3CE`).** Used only for deepest tonal layering — the slight tonal shift at the bottom of a long-form page, the panel behind a pull-quote when contrast against cream-100 reads too flat.
- **Ink 900 (`#1A1814`).** Body and headline text. Carries a barely-perceptible warmth that lets it sit on cream without optical vibration. AAA on cream-100 (14.2:1).
- **Slate 500 (`#7A6F62`).** Captions, metadata, dates, photo credits. 4.7:1 on cream-100 (WCAG AA normal text).

**Banned, with reason:** hot pink (hookup), club neon (nightclub), pure white (corporate wellness), black-and-chrome (nightclub), stylized golden-hour Instagram filter (faked light). Each exclusion is mechanic-level.

## Typography

Two typefaces. A third for human-moment punctuation only.

- **GT Sectra** (display + headline). Heavy, literary, the kind of letterform that belongs on a vinyl jacket from 1978 or on the spine of a Wright Thompson book. Used for `hero-display` (72px), `headline-lg` (48px), `headline-md` (32px), `headline-sm` (24px). Weight is held at 500. The system earns gravity through size and color, not bolding — there is no 700 or 900 weight in this system. Acceptable substitutes when GT Sectra is unlicensed, in order: **Mortise**, **IBM Plex Serif**, **Georgia**.

- **Inter** (body + label). The humanist sans that carries the words. Readable at 14px on a phone in actual sunlight. Used for `lead` (21px), `body-lg` (18px), `body-md` (16px), `body-sm` (14px), `label-caps` (12px tracked +0.14em), `caption` (13px). Weight 400 for body, 600 for `label-caps` only. **Plus Jakarta Sans** is the documented substitute.

- **Caveat** (`hand-script`). Used **only** for human moments: Andrea's signature on a ticket back, a couple's quote pulled from a story-capture interview, one line on a thank-you card. Never for navigation, never for body, never for headlines. More than one hand-script element per composition stops being human and starts being decorative — that is the failure mode to police against.

The discipline lives in the **size scale**, not in weight stacking. `hero-display` at 72px and `body-md` at 16px do the heavy lifting. There is no `headline-xl-bold` because a headline that needs to be larger than `hero-display` should instead be carried by a photograph.

A sub-rule specific to Variant A: **label-caps gets +0.14em tracking** (vs. +0.12em in v1). The wider letterspacing pushes the system slightly toward the editorial-magazine register and away from app-UI. Small change, decisive feel.

## Layout

The grid is **body-centered, not screen-centered.** Content maxes at 1180px on desktop. Editorial photography sits at full bleed where it earns it; long-form text holds at a 65–75-character measure for genuine readability.

The spacing scale is built on a 4px base with the working set at `xs: 4`, `sm: 8`, `md: 12`, `base: 16`, `lg: 24`, `xl: 32`, `2xl: 48`, `3xl: 72`. Variant A pushes the `3xl` to 72px (vs. v1's 64px) to give editorial spreads slightly more breathing room between sections — the difference between a magazine and a website.

Section margins between major content blocks default to `2xl` (48px) desktop, `xl` (32px) mobile. Cards and stacked content use `lg` (24px) gutters. Vertical rhythm comes from typography line-heights, not from `<br>` spacers.

**Whitespace philosophy:** the layout assumes the reader has time. Crowded layouts read as event-promoter design. Resonance is a curated room; the design respects the same principle — fewer things, more space. A hero photograph spans the full container width on desktop, full screen-width on mobile, with the headline either sitting below it (default) or overlaid in the lower-left negative-space quadrant of the frame.

**The hairline rule** is a Variant A signature. Every category mark, every section break, every wordmark on a primary surface sits above or below a 1px hairline in `border-hairline`. The hairline is the broadsheet's signature gesture and Variant A leans on it heavily.

## Elevation & Depth

**Flat by default with tonal layering.** Depth is conveyed through the cream-50 / cream-100 / cream-200 step, not through drop shadows. A card on the page sits on cream-100 with a cream-50 fill — gentle but legible.

Shadows are reserved for two cases only: (1) hover state on interactive cards (`0 4px 12px rgba(15, 26, 46, 0.08)` — a midnight-tinted whisper), and (2) the photographic shadow living inside the photograph itself, which is the actual sunlight casting onto the actual floor. We never simulate light. We photograph it.

Floating panels, glass-morphism, neon glow, animated gradient backgrounds — forbidden. They smuggle the visual grammar of a different party.

## Shapes

**Editorial sharpness.** Most surfaces use `rounded.sm` (2px) — the broadsheet register. `rounded.md` (4px) for photo cards needing softer corners against a busy background. `rounded.full` only for round photo crops (Andrea's portrait, contributor avatars) — **never** for buttons. Pill-shaped buttons read as consumer SaaS, which Resonance is not.

Mixing radii within a single composition is forbidden. Pick one register per view.

## Components

- **`button-primary`** — Terracotta 600 background, cream on-primary text, 2px radius, `label-caps` typography, 18px padding (slightly heavier than v1 to match the heavier display type). Hover transitions to terracotta-700 (one step darker, not lighter — this variant's hover deepens rather than lifts). Used for the single most-important action per screen: *Reserve a seat*, *Apply for the next event*, *Read the manifesto*.

- **`button-secondary`** — Transparent background, midnight-900 text, 1px hairline border in `border-hairline`, 2px radius, 18px padding. Hover fills with midnight-900 and inverts text to cream. Used for the second action per screen — *Read more*, *See past events*, *Subscribe*.

- **`button-ghost`** — Transparent, ink-900 text, no border, no radius. Inline third-tier interaction — *Skip intro*, *Continue*, *No thanks*.

- **`card-photo`** — cream-50 surface, 2px radius (sharper than v1's 4px to match the editorial register), zero internal padding. Captions sit beneath, not inside. The photograph is not "contained" — the card is a frame the photograph leans against.

- **`card-text`** — cream-50 surface, 2px radius, 32px internal padding, body text in ink-700. Used for manifesto pull-quotes, story excerpts, FAQ blocks.

- **`input`** — cream-50 background, ink-900 text, 2px radius, 14px padding. Focus state: terracotta-600 border at 2px. No animated label floats; the label sits above the input in `label-caps` and stays still.

- **`badge-event`** — midnight-900 fill, cream text, 2px radius, `label-caps` at 6px padding. Used to mark date and city on photo cards: `JUNE 2026 · CHICAGO`. Never used to advertise discounts or hype.

- **`divider`** — 1px solid `border-hairline`. Never thicker than 1px. The hairline rule from a broadsheet.

- **`pull-quote`** — cream-100 background, gold-600 text, no border, 32px padding. Used once per long-form piece, never twice. A pull-quote that appears more than once stops being a pull and starts being a wall.

## Do's and Don'ts

**Do:**

- Use a real photograph as the lead element of every primary surface.
- Lead headline copy with the **heart-vs-head** frame; let body-first explain the *how*.
- Hold terracotta back for the single most-important action per screen.
- Set type at 16px body / 72px hero — let scale do the work, not weight.
- Use the hairline rule generously — it is Variant A's signature gesture.
- Honor the daytime mechanic: every photographic frame must read as obviously daylight, real room, real bodies.
- Reserve hand-script for human moments only — Andrea's signature, a couple's quote.
- Layer depth via cream-50 / cream-100 / cream-200, not shadows.
- Use `label-caps` at +0.14em tracking — the editorial register depends on it.
- Treat the wordmark as a category mark, not as a logo — set it in GT Sectra at the headline size for the surface, never as a graphic asset.

**Don't:**

- Use any photograph that could have been taken at 11pm. If you can't tell, kill it.
- Generate front-of-house photography with AI. AI faces are forbidden across the system.
- Stack two serifs. GT Sectra carries the heat alone — pairing it with another display serif breaks the editorial discipline.
- Use hot pink, club neon, pure white, black-and-chrome, or stylized golden-hour filter tones. Each exclusion has a brand reason in `## Colors`.
- Drop in stock dancers, dance-floor silhouettes, lens-flare overlays, or "atmospheric" low-light dance frames. These smuggle the bar-at-11pm grammar.
- Use hand-script as a default tone. More than once per composition is decorative slop.
- Use pill-shaped (`rounded.full`) buttons. Pills read as consumer SaaS.
- Animate quickly. Motion is slow, room-warm, considered. No spring, no bounce.
- Use the wordmark or any visual element on a layout that has no photograph. The system does not stand on type alone.
- Use the `pull-quote` more than once per long-form piece.
- Combine radii (2px and 8px on the same view). Pick one register and hold.

---

## Appendix — Photography Direction (Variant A specifics)

The full photography spec at `01-visual/photography-rules.md` is binding. Variant A specifics:

- **Composition is editorial-broadsheet.** Decentered framing. Subject in the right third or lower-left. Negative space holds the rest of the frame so type has somewhere to land. This is more deliberately composed than B (which favors environmental architectural frames) and less restrained than C (which crops tighter still).
- **Tonal grading is warm-neutral.** Preserve actual daylight color temperature. Variant A leans slightly into the terracotta tone the brand palette is sourced from — the wood-floor warmth — but never via filter, only by selection.
- **Framing emphasis: bodies + gesture.** The hero shot is a body mid-gesture, not a wide environmental. Wide-room shots are supporting frames for the second-tier layouts.
- **The 11pm test still applies.** No flash. No club lighting. No neon. No tungsten-only interiors. Window light or it didn't happen.

## Appendix — Motion Principles (Variant A specifics)

Resonance moves slowly. Variant A is the slowest of the three variants — the editorial register requires stillness.

- Default transition: 250ms, ease-out. Never bounce, never spring.
- Hover states: a single tonal shift, no movement. (E.g., button hover deepens terracotta-600 → terracotta-700; no lift, no shadow change.)
- Page transitions: a single cross-fade at 300ms, never a slide-and-wipe.
- Scroll-triggered animation: gentle parallax on photographic blocks (≤ 12% movement at scroll speed). Nothing else.
- The hairline rule never animates. It is paper.
- Forbidden: bounce, spring, parallax >15%, animated gradient, flicker, kinetic typography, scroll-jacking, snap-scroll between sections.

---

## Sample Applications

### Instagram Feed Post (1080 × 1350)
A full-bleed photograph of three bodies mid-laugh on a wood floor at 2pm, south-facing window light bouncing off cream walls. Lower-left overlay: GT Sectra 32px headline in cream-50 — *"Heart encounters, not head encounters."* Lower-right wordmark in label-caps cream-50 at 60% opacity. A single hairline rule sits 12px above the wordmark, the broadsheet's signature gesture migrated to social. Caption (in the IG body, not the image): manifesto trailer copy.

### Instagram Story Frame (1080 × 1920)
Cream-100 solid background. Centered vertically: a single GT Sectra `headline-md` line in midnight-900 — *"You've left a thousand rooms / with a phone full of contacts / and no one to call."* A 60px hairline rule below the type, centered. Wordmark in label-caps slate-500, lower-right, 64px from edge. No photo. The exception that proves the photo-led rule: a story frame that earns being pure-type because the manifesto-line is the photograph.

### Flyer / Poster — July Event (2550 × 3300 @ 300dpi)
**Top half:** a single horizontal photograph from the photographer brief — bodies mid-dance, real Chicago loft, 2pm light. Edge-to-edge bleed.
**Lower half on cream-100:**
  - Wordmark *RESONANCE* in GT Sectra 72px midnight-900, left-aligned 48px from the photo edge.
  - 1px hairline rule beneath the wordmark, 60% page width.
  - Event details in label-caps midnight-900: `JULY 26, 2026 · CHICAGO · DOORS 2PM`.
  - 32px gap.
  - Single line in ink-700 body-lg: *"A daytime, sober dance party for people who want to meet a partner."*
  - 48px gap.
  - Button-secondary CTA: `APPLY FOR THE NEXT EVENT →` in midnight-900 with a hairline border.

### Event Ticket (4 × 6" postcard)
**Front:** a single photograph from the photographer brief, full-bleed. Lower-left overlay: GT Sectra wordmark in cream-50 at 32px. Lower-right: Andrea's hand-script signature in Caveat 28px in cream-50.
**Back:** cream-100 paper-stock background (uncoated, warm-white). Top: GT Sectra `headline-sm` (24px) in midnight-900 — `RESONANCE 002`. Body: event date, venue, doors, in label-caps stacked left. Center-right: a single sentence in body-md ink-700 — *"You were in the room on [date]."* Lower-right: a 0.75" hairline-thin terracotta-600 underline. QR code for entry: lower-left, 0.75" square, midnight-900.

### Andrea Portrait (founder shot for press / About page)
Andrea at the decks, mid-set, head down, hand on the fader, real Chicago loft light from a south-facing window behind her. Mid-shot, decentered: Andrea in the right third, the rest of the frame is the room — wood floor, terracotta brick wall, the half-blur of a body dancing behind her. Tonal grading is warm-neutral. The shot reads as *the founder doing the work*, not *the founder posing as the founder.* On a press one-sheeter, this photograph sits in the middle band with a 13px slate-500 caption beneath: *"Andrea — Resonance 001, Chicago, June 2026."*

### Venue Pitch — One-Pager Top Section (Letter portrait)
**Page header (top 1/4):**
- GT Sectra wordmark *RESONANCE* in midnight-900 at hero-display 72px, left-aligned.
- 1px hairline rule beneath, full page-width.
- Below rule: single line in label-caps slate-500 — `A PRESS ONE-SHEETER · CHICAGO · JULY 2026`.
**Hero block (middle 1/2):**
- Single horizontal photograph, full-width within the 1" margin.
- Caption in caption-13px ink-700: *"Photographed at Resonance 001, Chicago, June 2026."*
**Body block (lower 1/4):** three columns — *What it is* / *The mechanic* / *Press contact* — each in body-md, separated by a hairline divider.

The page must read as a single editorial statement. A journalist should be able to write the lede from this one page.

---

## Cross-references

- `00-foundation/05-non-negotiables.md` — the 12 lines this variant honors
- `01-visual/DESIGN.md` — the v1 anchor this variant extends
- `01-visual/photography-rules.md` — binding photographer brief
- `01-visual/aesthetic-references.md` — mood board (Groups 1–4 anchor; Group 5 kill list)
- `01-visual/component-tokens.md` — current production component spec (variant-applicable values inherited)
- `00-foundation/01-brand-bible.md` §8 — strategic intent
- `00-foundation/03-voice-document.md` — voice the visual must read as
