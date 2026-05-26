---
version: alpha
name: Resonance — Variant B — Latin-American Daylight
description: A daytime, sober dance room in Chicago, rendered in the architectural color and tile-discipline of Latin-American daylight modernism. Terracotta, ochre, deep moss-green, and cream — the palette of Casa Wabi at 3pm, Casa Bosques in November, the courtyard wall behind a cafetería in San José. A sturdier serif (Tiempos / Canela) carries the headlines; a humanist sans (Söhne / Inter) carries the body. Geometry is architectural, not decorative — no woven texture as wallpaper, no Aztec motif as ornament. The room reads as Andrea's heritage rendered as discipline. Photography is the protagonist; type is the caption. If a photo could have been taken at 11pm, it does not belong here.

colors:
  # Atomic shades — sourced from Casa Wabi adobe walls, Costa Rican coffee at her grandmother's, mid-century Latin-American modernism, and the deep-green tile in a Mexico City courtyard at 2pm
  terracotta-700: "#8A3220"
  terracotta-600: "#A8412A"
  ochre-600:     "#B8843C"
  ochre-500:     "#C99C58"
  moss-900:      "#1F2E1E"
  moss-700:      "#36513A"
  moss-500:      "#5D7A5C"
  cream-50:      "#FAF4E6"
  cream-100:     "#F2E9D4"
  cream-200:     "#E7DABF"
  ink-900:       "#1C1611"
  ink-700:       "#3B3127"
  slate-500:     "#7A6E5C"

  # Semantic roles
  primary:    "{colors.terracotta-600}"
  secondary:  "{colors.moss-900}"
  tertiary:   "{colors.ochre-600}"
  neutral:    "{colors.cream-100}"
  surface:    "{colors.cream-50}"
  ink:        "{colors.ink-900}"
  body:       "{colors.ink-700}"
  muted:      "{colors.slate-500}"
  on-primary: "#FAF4E6"
  on-secondary: "#FAF4E6"

  # State + system
  border-hairline: "#D7C7A4"

typography:
  hero-display:
    fontFamily: "Tiempos Headline, Canela, GT Sectra, IBM Plex Serif, Georgia, serif"
    fontSize: 68px
    fontWeight: 500
    lineHeight: 1.05
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: "Tiempos Headline, Canela, GT Sectra, IBM Plex Serif, Georgia, serif"
    fontSize: 44px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.006em
  headline-md:
    fontFamily: "Tiempos Headline, Canela, GT Sectra, IBM Plex Serif, Georgia, serif"
    fontSize: 30px
    fontWeight: 500
    lineHeight: 1.18
  headline-sm:
    fontFamily: "Tiempos Headline, Canela, GT Sectra, IBM Plex Serif, Georgia, serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.22
  lead:
    fontFamily: "Söhne, Inter, Plus Jakarta Sans, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.55
  body-lg:
    fontFamily: "Söhne, Inter, Plus Jakarta Sans, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
  body-md:
    fontFamily: "Söhne, Inter, Plus Jakarta Sans, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
  body-sm:
    fontFamily: "Söhne, Inter, Plus Jakarta Sans, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
  label-caps:
    fontFamily: "Söhne, Inter, Plus Jakarta Sans, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0.16em
  caption:
    fontFamily: "Söhne, Inter, Plus Jakarta Sans, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
  hand-script:
    fontFamily: "Homemade Apple, Caveat, cursive"
    fontSize: 28px
    fontWeight: 400
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
  margin: 40px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: 16px
  button-primary-hover:
    backgroundColor: "{colors.terracotta-700}"
    textColor: "{colors.on-primary}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.secondary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: 16px
    border: "1px solid {colors.secondary}"
  button-secondary-hover:
    backgroundColor: "{colors.moss-900}"
    textColor: "{colors.on-secondary}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: 12px
  card-photo:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.none}"
    padding: 0px
  card-text:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.body}"
    rounded: "{rounded.none}"
    padding: 32px
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 14px
    border: "1px solid {colors.border-hairline}"
  divider:
    backgroundColor: "{colors.border-hairline}"
    height: 1px
  badge-event:
    backgroundColor: "{colors.moss-900}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
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
    rounded: "{rounded.none}"
    padding: 24px
---

# Resonance — Variant B — Latin-American Daylight

## Overview

Andrea is from Costa Rica. The brand bible §5 names her formation: coffee at her grandmother's, music school as her second home, the orchestra she expected to find in Chicago and the one she actually found. Variant A honors the room as a *Chicago* room. Variant B honors the room as **a room Andrea brought with her** — Latin-American daylight modernism, rendered architecturally, not decoratively.

Strategic position: **the heritage register, used as discipline.** The reference set is not the kitsch-Latin-tourist-market grammar (terracotta-tile-frame-with-cactus). It is Casa Wabi by Tadao Ando at 3pm, Casa Bosques in Mexico City, the editorial discipline of *Apartamento Magazine* when it covers a courtyard in San Pedro Sur, the deep-green tile behind the bar at Contramar with sun coming through the slats. The palette is terracotta + ochre + moss-green on cream — sourced from the actual architectural color of Latin-American mid-century daylight. The grammar is geometric and architectural — squared corners, hairline rules, no rounded radii on buttons or cards. The discipline is the heritage made visible, not the heritage made decorative.

Who in the audience this variant reaches that the others might not: Latin-American Chicagoans (a significant slice of the ICP geography), readers of *Cereal* / *Apartamento* / *Kinfolk* who recognize the register, the design-conscious Profile #1 arts-worker who would not flinch at the deep moss-green and the squared edges, the venue with terracotta brick and a south-facing window that already speaks this language. Variant B is the variant that signals *this is Andrea's room, not a brand designed at her*.

What separates B from A and C: B is **culturally specific in its color sourcing** (where A is universal-editorial), and **architecturally rigid in its geometry** (where C is softer, sage-and-gold and curve-permitting). B is the only variant that uses moss-green as the secondary anchor instead of midnight-blue. The substitution is the load-bearing move — moss-green is the color of Latin-American interior shadow at 2pm; midnight is the color of a Chicago February sky. Both are honest. They are not interchangeable.

**The discipline trap:** Variant B is the variant most at risk of drifting into kitsch. Every design decision should be checked against the *architectural-not-decorative* rule. Woven-texture wallpaper, Aztec-motif borders, "fiesta" color combinations, hand-illustrated cacti, marigold orange — all banned. The Latin-American reference here is to Luis Barragán, not to a corner restaurant menu. Police this hard.

## Colors

The palette is sourced from real Latin-American architectural daylight. Each token is named after a referenceable real-world surface.

- **Primary — Terracotta 600 (`#A8412A`).** Slightly deeper, slightly more saturated than the v1 terracotta. Sourced from Casa Wabi's adobe wall at 3pm — the wall has been baking in Oaxacan sun for decades and the color is what's left. Used for primary CTAs, the wordmark on darker surfaces, single-most-important hover. Never as body text. 5.1:1 against cream-100 (WCAG AA Large).
- **Terracotta 700 (`#8A3220`).** Hover-state. Darker still. The shadow side of the same wall.
- **Secondary — Moss 900 (`#1F2E1E`).** Deep moss-green. The color of Mexico City interior shadow at 2pm, the deep tile behind the bar at Contramar, the cypress in a Chicago courtyard in November. Replaces midnight-blue as the brand's grounding anchor. Used for body copy on cream, headline anchors, event badges. 13.1:1 against cream-100 (WCAG AAA).
- **Moss 700 (`#36513A`).** A softer moss for sub-headlines, hover-fill on photo cards. 7.9:1 against cream-100 (WCAG AAA).
- **Moss 500 (`#5D7A5C`).** The lightest moss, used for the underline accent on couples'-name pull-quotes — a green where Variant A used gold. 4.6:1 against cream-100 (WCAG AA Large).
- **Tertiary — Ochre 600 (`#B8843C`).** A warm gold-ochre. The color of late-afternoon adobe shadow, of the wood paneling at a San José cafetería, of pan-dulce on a Sunday. Used as the rare accent — a single underline on a pull-quote, a couples-list bullet, the back-of-ticket terracotta-or-ochre mark. 4.8:1 on cream-100 (WCAG AA).
- **Ochre 500 (`#C99C58`).** Sub-accent for editorial flourishes — section openers in long-form, a hairline rule under a category mark when the moss-green would be too heavy. 3.6:1 on cream-100 (AA Large only — never used for body).
- **Neutral — Cream 100 (`#F2E9D4`).** Warmer than v1's cream-100; carries a yellow-undertone that places it firmly in the Latin-American-daylight register. The breathable background.
- **Surface — Cream 50 (`#FAF4E6`).** Half-step lighter. Cards sit on cream-100 with cream-50 fills.
- **Cream 200 (`#E7DABF`).** Deepest tonal layering — the panel behind a pull-quote or the bottom-band of long-form spreads.
- **Ink 900 (`#1C1611`).** Body and headline text. Slightly warmer than v1 ink to harmonize with the warmer cream. AAA on cream-100.
- **Slate 500 (`#7A6E5C`).** Captions, metadata, photo credits. 4.7:1 on cream-100 (WCAG AA normal text).

**Banned, with reason:** hot pink (hookup), club neon (nightclub), pure white (corporate wellness), black-and-chrome (nightclub), stylized golden-hour Instagram filter (faked light), **marigold-orange** (drifts toward kitsch-Latin-restaurant), **fuchsia** (drifts toward stereotyped-festival-Mexican), **avocado-green or pastel-pistachio** (drifts toward Goop-wellness-with-Latin-veneer). Each exclusion has a mechanic-level or kitsch-prevention reason.

## Typography

Two typefaces. A third for rare human-moment punctuation.

- **Tiempos Headline / Canela** (display + headline). A contemporary serif with stronger horizontal stress and slightly more architectural geometry than GT Sectra. The reference is *Apartamento Magazine* headlines, *Cereal* mastheads, the editorial discipline of Latin-American art-book publishing (Editorial RM, Mack Books). Used for `hero-display` (68px), `headline-lg` (44px), `headline-md` (30px), `headline-sm` (22px). Weight is held at 500. The system earns gravity through size and color, not bolding. Acceptable substitutes when Tiempos/Canela are unlicensed, in order: **GT Sectra**, **IBM Plex Serif**, **Georgia**.

  Why this serif instead of GT Sectra: Tiempos and Canela both come out of contemporary type-design conversations (Klim, Commercial Type) that consciously reference both Anglo-editorial and Latin-American editorial publishing traditions. Canela in particular has a slight Iberian-letterform quality that places the brand in the right cultural lineage without being decorative about it.

- **Söhne / Inter** (body + label). Söhne is the contemporary humanist grotesk that has become the default of design-conscious editorial brands; Inter is the open-source-licensed substitute that gets shipped when the budget doesn't include Klim. Used for `lead` (20px), `body-lg` (18px), `body-md` (16px), `body-sm` (14px), `label-caps` (12px tracked +0.16em — wider than Variants A and C), `caption` (13px). Weight 400 for body, 600 for `label-caps` only.

  Sub-rule specific to Variant B: **label-caps gets +0.16em tracking** — the widest of the three variants. The architectural register depends on the wide-tracked label reading as a *category mark on a building plaque*, not as a UI element. Search "Casa Wabi signage" — the labeling discipline is exactly this.

- **Homemade Apple** (`hand-script`). Used only for human moments: Andrea's signature, a couple's quote, a single line on a thank-you card. Homemade Apple replaces Caveat in this variant — it carries a slightly more grounded, less performatively-cursive feel that pairs with the architectural register.

The discipline lives in **size + geometry**, not in weight stacking.

## Layout

The grid is **architectural — squared, gridded, planar**. Content maxes at 1180px on desktop. Photography sits in disciplined rectangles, never bleeding without a hard edge.

Spacing scale: `xs: 4`, `sm: 8`, `md: 12`, `base: 16`, `lg: 24`, `xl: 32`, `2xl: 48`, `3xl: 64`. Section margins between major content blocks default to `2xl` (48px) desktop, `xl` (32px) mobile.

**Architectural alignment rule** (Variant B signature): every layout uses a strict 12-column grid with hard column-snapping. Photography aligns to columns. Type aligns to columns. Hairline rules align to columns. The discipline is the heritage made visible — Luis Barragán's house works because every wall, every doorway, every shadow follows the geometry. The website / poster / ticket works the same way.

**Whitespace philosophy:** generous but planar. Negative space is *room*, in the architectural sense — a cleared interior, not a decorative emptiness. Crowded layouts are not just visually wrong, they are architecturally wrong — they violate the discipline the variant is built on.

**Photo composition:** photographs in Variant B emphasize **room as second protagonist**. A wide environmental shot (warm wood floor, terracotta brick, south-facing window with curtain) where bodies live inside the room rather than dominating it. This is the photographic difference from Variant A (which favors body-mid-gesture) and Variant C (which crops tighter still).

## Elevation & Depth

**Flat. Architectural.** No shadows. Depth is conveyed through the cream-50 / cream-100 / cream-200 step, and through the geometry of the layout itself — a panel on cream-100 with a 1px moss-700 hairline border has more depth, in this system, than a card with a drop shadow.

The only permitted shadow is the photographic shadow living inside the photograph — actual sunlight casting onto an actual floor. We never simulate light. We photograph it.

Floating panels, glass-morphism, neon glow, animated gradient backgrounds — forbidden.

## Shapes

**Squared. No rounding.** Variant B uses `rounded.none` (0px) on every component — buttons, cards, inputs, photo frames. The architectural discipline depends on it. `rounded.full` is permitted only for round photo crops (Andrea's portrait) — never for buttons or any other shape.

Mixing radii within a single composition is forbidden. The squared register is the entire point.

This is the sharpest geometric differentiator of the three variants. Variant A uses 2px (editorial-broadsheet softness). Variant C uses 4px (quiet-luxury softness). Variant B uses 0px (architectural discipline).

## Components

- **`button-primary`** — Terracotta 600 background, cream on-primary text, **0px radius**, `label-caps` typography (16px tracked +0.16em), 16px padding. Hover transitions to terracotta-700 (darker, not lighter). The squared corners are the variant's signature — pill-shaped buttons would break the architectural register entirely.

- **`button-secondary`** — Transparent background, moss-900 text, 1px solid moss-900 border, 0px radius, 16px padding. Hover fills with moss-900 and inverts text to cream. Used for the second action per screen.

- **`button-ghost`** — Transparent, ink-900 text, no border, 0px radius. Inline third-tier interaction.

- **`card-photo`** — Cream-50 surface, **0px radius**, zero internal padding. Captions sit beneath, not inside. Hard-edged frames.

- **`card-text`** — Cream-50 surface, 0px radius, 32px internal padding, body text in ink-700. A panel, not a card. Used for manifesto pull-quotes, story excerpts, FAQ blocks.

- **`input`** — Cream-50 background, ink-900 text, 1px solid border-hairline, 0px radius, 14px padding. Focus state: terracotta-600 border at 2px. Label sits above the input in `label-caps` and stays still.

- **`badge-event`** — Moss-900 fill, cream text, 0px radius, `label-caps` at 6px padding. Used to mark date and city on photo cards: `JULY 2026 · CHICAGO`.

- **`divider`** — 1px solid `border-hairline`. The hairline is more visible in Variant B than in A or C because the warmer cream makes the border-hairline (`#D7C7A4`) read as a deliberate architectural line rather than a paper-fold.

- **`pull-quote`** — Cream-100 background with cream-200 panel-fill, ochre-600 text, 0px radius, 32px padding. The ochre against the deep cream is the variant's most decisive color move. Used once per long-form piece.

## Do's and Don'ts

**Do:**

- Use a real photograph as the lead element of every primary surface.
- Use moss-900 as the grounding anchor instead of midnight-blue. The substitution is what makes this variant *this variant*.
- Source color references from real Latin-American architectural daylight (Casa Wabi, Casa Bosques, Casa Pedregal, Luis Barragán archive). Never from "Mexican color palette" Pinterest boards.
- Hold to 0px radius on every component. The architectural discipline depends on it.
- Set type at Tiempos/Canela 68px hero and Söhne/Inter 16px body — let scale do the work, not weight.
- Use `label-caps` at +0.16em tracking — wider than the other variants. Read as a building plaque, not a UI element.
- Photograph the **room** as the second protagonist — bodies live inside the room rather than dominate it.
- Use the 12-column architectural grid strictly. Photography aligns to columns. Type aligns to columns.
- Reserve hand-script for human moments only. Homemade Apple, not Caveat — slightly more grounded register.
- Honor the daytime mechanic absolutely. The 11pm test is the floor.

**Don't:**

- Use any photograph that could have been taken at 11pm. If unsure, kill it.
- Generate front-of-house photography with AI. AI faces are forbidden across the entire system.
- Use the kitsch-Latin grammar: woven-texture wallpaper, Aztec motif as ornament, hand-illustrated cacti, marigold-orange, fuchsia, "fiesta" color combinations, papel-picado borders. The reference here is Barragán, not a restaurant menu.
- Use rounded buttons or rounded cards. The 0px radius is the load-bearing geometric move.
- Use midnight-blue as a secondary anchor. Moss-900 replaces it. The two are not interchangeable in this variant.
- Use pastel-pistachio, avocado-green, marigold-orange, or fuchsia. Each smuggles either Goop-wellness or stereotyped-Latin-festival grammar.
- Use stylized "golden-hour Latin" filters. The light is real Mexico City / San José / Chicago daylight or it doesn't appear.
- Drop in stock dancers, dance-floor silhouettes, lens-flare overlays. These smuggle the bar-at-11pm grammar.
- Use hand-script as a default tone. More than once per composition is decorative slop.
- Combine rounded with squared shapes in a single view. Pick one register and hold.
- Mix grid alignment. Every photo, every type block, every divider snaps to the 12-column grid.

---

## Appendix — Photography Direction (Variant B specifics)

The full photography spec at `01-visual/photography-rules.md` is binding. Variant B specifics:

- **Composition is architectural — room-as-second-protagonist.** A wide environmental frame where the room (wood floor, terracotta brick, south-facing window, the deep-green of an interior plant or a tile wall) carries half the photograph. Bodies live inside the room.
- **Tonal grading is warm-but-deeper.** The cream-100 in this variant is warmer than v1's. Photography is white-balanced to honor that warmer cream — preserve the yellow undertone of Latin-American afternoon daylight, never grade away from it. Never invent the tone in post; select frames where the light was already that color.
- **Framing emphasis: room + body + the architectural detail that places it.** A terracotta brick wall behind a body. A deep-green plant in the corner. A wood-paneled wall with a single sun-pattern from a window grate. These details place the photograph in the variant's cultural register.
- **The 11pm test still applies.** No flash. No club lighting. No neon. No tungsten-only interiors. Window light or it didn't happen.
- **No kitsch detail.** Frames featuring papel picado, marigolds, dia-de-muertos iconography, Frida-Kahlo-print-shirts, or any other costume-Latin signifier are killed at the card. Heritage shows up in the *light*, the *color*, the *architectural detail* — never in the iconography.

## Appendix — Motion Principles (Variant B specifics)

Resonance moves slowly. Variant B is the most still of the three variants — the architectural register requires it.

- Default transition: 200ms, ease-out. Never bounce, never spring.
- Hover states: a single color shift (terracotta-600 → terracotta-700 darker; moss-900 fills empty button); no movement, no scale, no shadow change.
- Page transitions: a single cross-fade at 300ms.
- Scroll-triggered animation: gentle parallax on photographic blocks (≤ 10% movement at scroll speed — less than A or C). The architectural discipline rejects motion as ornament.
- Forbidden: bounce, spring, parallax >12%, animated gradient, flicker, kinetic typography, scroll-jacking, scaling on hover.

---

## Sample Applications

### Instagram Feed Post (1080 × 1350)
A full-bleed photograph of a body mid-dance against a terracotta brick wall, deep-green plant in the lower-right of the frame, south-facing window light cutting across the wood floor at 2pm. Lower-left overlay: Tiempos Headline 30px in cream-50 — *"Daytime. Sober. Curated."* Lower-right wordmark in label-caps cream-50 at 60% opacity, +0.16em tracking. The squared geometry of every overlay element matches the architectural discipline of the room itself.

### Instagram Story Frame (1080 × 1920)
Cream-100 solid background. Top-third: a small 600px-wide photograph of an empty room in Chicago daylight — terracotta brick, wood floor, the moss-green of a single plant in the corner. Below: Tiempos `headline-md` 30px in moss-900 — *"You've been in rooms that took something from you. / This room is built to give something back."* Lower-right wordmark in label-caps slate-500, 64px from edges. A 1px hairline rule sits 24px above the wordmark.

### Flyer / Poster — July Event (2550 × 3300 @ 300dpi)
**Architectural layout** in three horizontal bands:
- **Top band (40% of page):** a single horizontal photograph — bodies in mid-dance against a terracotta brick wall, deep-green plant detail, 2pm light. Edge-to-edge bleed.
- **Middle band (35% of page):** cream-100 background.
  - Wordmark *RESONANCE* in Tiempos Headline 68px moss-900, left-aligned 48px from edge.
  - 1px hairline rule beneath, 70% page width, in moss-700.
  - Event details in label-caps moss-900 +0.16em: `JULY 26, 2026 · CHICAGO · DOORS 2PM`.
  - 24px gap.
  - Single line in ink-700 body-lg: *"A daytime, sober dance party for people who want to meet a partner."*
- **Bottom band (25% of page):** cream-200 panel-fill, providing the deepest tonal layering.
  - 48px from the band's top edge: button-primary CTA *RESERVE YOUR SEAT →* in terracotta-600 with cream text, 0px radius.
  - Below the CTA: a single line in body-sm slate-500 — *"Curated admission. Apply via resonanceroom.com."*

### Event Ticket (4 × 6" postcard)
**Front:** a single photograph from the photographer brief, full-bleed. Lower-left overlay: Tiempos Headline wordmark in cream-50 at 30px. Lower-right: Andrea's hand-script signature in Homemade Apple 28px in cream-50.
**Back:** cream-100 paper-stock background (warmer warm-white than Variants A or C). Top: Tiempos `headline-sm` (22px) in moss-900 — `RESONANCE 002`. Body: event date, venue, doors, in label-caps stacked left, +0.16em tracking. Center-right: a single sentence in body-md ink-700 — *"You were in the room on [date]."* Lower-right: a 0.75" hairline-thin ochre-600 underline (the variant's only place the ochre appears at this scale). QR code for entry: lower-left, 0.75" square, moss-900.

### Andrea Portrait (founder shot for press / About page)
Andrea at the decks, mid-set, head down, hand on the fader. The room is the second protagonist — a wide environmental frame: terracotta brick wall behind her, a deep-green plant in the corner of the frame, south-facing window light cutting across the wood floor, the half-blur of a body dancing in the lower-left. Andrea is in the right third; the rest of the frame is *the room she built*. Tonal grading is warm-Latin-daylight — yellow-undertone preserved, never graded toward magenta or "moody."

### Venue Pitch — One-Pager Top Section (Letter portrait)
**Page header (top 1/4):**
- Tiempos Headline wordmark *RESONANCE* in moss-900 at hero-display 68px, left-aligned, 1" margin.
- 1px hairline rule beneath, full page-width, moss-700.
- Below rule: single line in label-caps slate-500 +0.16em — `A DAYTIME, SOBER DANCE PARTY · CHICAGO · JULY 2026`.
**Hero block (middle 1/2):**
- Single horizontal photograph, full-width within the 1" margin. The photograph is the architectural one — room as second protagonist.
- Caption in caption-13px ink-700: *"Photographed at Resonance 001, Chicago, June 2026."*
**Body block (lower 1/4):** three columns — *What it is* / *The mechanic* / *Press contact* — each in body-md, separated by 1px moss-700 hairline dividers. Bottom-band cream-200 panel-fill behind the body block, providing tonal weight to the page footer.

The page must read as the *built form* of the brand. A journalist should look at it and feel the architectural discipline of the room itself.

---

## Cross-references

- `00-foundation/05-non-negotiables.md` — the 12 lines this variant honors
- `00-foundation/01-brand-bible.md` §5 — Andrea's founding story (Costa Rica, Chicago, the orchestra she expected vs. the one she found)
- `00-foundation/01-brand-bible.md` §8 — strategic visual intent
- `00-foundation/03-voice-document.md` — voice the visual must read as; bilingual touches and sense-detail anchoring are the linguistic equivalent of this variant's color sourcing
- `01-visual/DESIGN.md` — the v1 anchor; this variant inherits the 11pm test and substitutes the secondary anchor color
- `01-visual/photography-rules.md` — binding photographer brief
- `01-visual/aesthetic-references.md` — mood board (Group 3 entries 13 + 16 are the load-bearing references for this variant — Mexico City interior design + Aimé Leon Dore documentary-lookbook discipline)
