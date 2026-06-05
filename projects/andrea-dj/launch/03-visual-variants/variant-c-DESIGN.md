---
version: alpha
name: Resonance — Variant C — Quiet Luxury Daylight
description: A daytime, sober dance room in Chicago, rendered with the restraint of a New Yorker subscriber's interior life. Cream, sage, warm-gold, and ink — the palette of a Gentlewoman spread, a Cereal Magazine architectural feature, an Aimé Leon Dore lookbook page that has been sitting on a marble table in a south-facing apartment for an hour. A refined modern serif (Söhne Breit / Domaine Display) carries the headlines at restrained scale; a humanist grotesk (Söhne / Inter) carries the body at the rhythm of an essay. The system disappears so the photograph and the language can do the work. Photography is the protagonist; type is the caption. If a photo could have been taken at 11pm, it does not belong here.

colors:
  # Atomic shades — sourced from a marble table at 3pm, sage tea cooling, the gold of unvarnished brass in soft daylight
  ink-900:      "#16140F"
  ink-800:      "#252118"
  ink-700:      "#3A332B"
  sage-700:     "#4B5849"
  sage-500:     "#7B8A78"
  sage-300:     "#B5C0AF"
  gold-700:     "#7A5A1F"
  gold-600:     "#9C7833"
  gold-500:     "#B8965A"
  cream-50:     "#FDFAF3"
  cream-100:    "#F7F2E6"
  cream-200:    "#EFE7D2"
  slate-500:    "#7A7468"
  terracotta-600: "#A14A30"

  # Semantic roles
  primary:    "{colors.ink-900}"
  secondary:  "{colors.sage-700}"
  tertiary:   "{colors.gold-600}"
  accent:     "{colors.terracotta-600}"
  neutral:    "{colors.cream-100}"
  surface:    "{colors.cream-50}"
  ink:        "{colors.ink-900}"
  body:       "{colors.ink-800}"
  muted:      "{colors.slate-500}"
  on-primary: "#FDFAF3"
  on-secondary: "#FDFAF3"

  # State + system
  border-hairline: "#E5DCC6"

typography:
  hero-display:
    fontFamily: "Domaine Display, Söhne Breit, Tiempos Headline, GT Sectra, Georgia, serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: -0.012em
  headline-lg:
    fontFamily: "Domaine Display, Söhne Breit, Tiempos Headline, GT Sectra, Georgia, serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.12
    letterSpacing: -0.008em
  headline-md:
    fontFamily: "Domaine Display, Söhne Breit, Tiempos Headline, GT Sectra, Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
  headline-sm:
    fontFamily: "Domaine Display, Söhne Breit, Tiempos Headline, GT Sectra, Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.25
  lead:
    fontFamily: "Söhne, Inter, Plus Jakarta Sans, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.55
  body-lg:
    fontFamily: "Söhne, Inter, Plus Jakarta Sans, system-ui, sans-serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.65
  body-md:
    fontFamily: "Söhne, Inter, Plus Jakarta Sans, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
  body-sm:
    fontFamily: "Söhne, Inter, Plus Jakarta Sans, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.6
  label-caps:
    fontFamily: "Söhne, Inter, Plus Jakarta Sans, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0.18em
  caption:
    fontFamily: "Söhne, Inter, Plus Jakarta Sans, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
  hand-script:
    fontFamily: "Homemade Apple, Caveat, cursive"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.25

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
  xxl: 56px
  xxxl: 80px
  gutter: 32px
  margin: 56px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.md}"
    padding: 16px
  button-primary-hover:
    backgroundColor: "{colors.ink-800}"
    textColor: "{colors.on-primary}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.md}"
    padding: 16px
    border: "1px solid {colors.border-hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.cream-200}"
    textColor: "{colors.ink}"
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
    padding: 40px
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 14px
    border: "1px solid {colors.border-hairline}"
  divider:
    backgroundColor: "{colors.border-hairline}"
    height: 1px
  badge-event:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: 0px
    border-top: "1px solid {colors.border-hairline}"
    border-bottom: "1px solid {colors.border-hairline}"
  pull-quote:
    backgroundColor: "transparent"
    textColor: "{colors.gold-700}"
    typography: "{typography.headline-md}"
    rounded: "{rounded.none}"
    padding: 0px
    border-left: "2px solid {colors.gold-600}"
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
    padding: 32px
---

# Resonance — Variant C — Quiet Luxury Daylight

## Overview

Variant C is the variant for the room where the magazine is on the marble table and the magazine is *The Gentlewoman*. Quiet luxury, used as discipline rather than aesthetic — no monogrammed silk, no Champagne-and-cashmere, no quiet-luxury cliché. Just the editorial restraint that an *Apartamento* spread, a *Cereal* feature, or an Aimé Leon Dore lookbook earns when it trusts that the photograph and the language are enough.

Strategic position: **the restrained register of an audience that doesn't need to be shouted at.** Type is held back to smaller sizes (56px hero, not 72px). Color is held back to a tighter range (cream + sage + warm-gold + ink, with terracotta surviving as an *accent* used once or twice per layout). Every component is more spacious — `card-text` carries 40px of internal padding, not 32px. The system disappears so the photograph and the language can do the work. The reader feels treated like an adult.

Who in the audience this variant reaches that the others might not: the *New Yorker*–reading Profile #1 arts-worker who is tired of brands trying so hard, the Profile #2 (when written) who came up reading *The Gentlewoman* and reads design literacy as a credibility signal, the venue owner who would respect a press one-sheeter that *doesn't shout*. Variant C is the variant most likely to be quoted in editorial press without alteration — because nothing about it needs alteration; the discipline is already there.

What separates C from A and B: C is **typographically lighter** (hero at 56px not 72px, weight 400 not 500), **chromatically restrained** (the brand-primary is *ink-900*, not terracotta — terracotta survives as an *accent* used sparingly), and **more spacious** in its component padding. Where A and B both anchor the brand on warm color, C anchors the brand on **ink against cream**, with color used as quiet punctuation. This is the variant Andrea picks if she wants the brand to read as *I trust the room to speak for itself.*

**The risk:** Variant C requires the most discipline to execute. A loud photo will overwhelm the restrained type, and the type will then feel weak rather than restrained. A lazy designer can make Variant C look like generic minimal-Squarespace. The discipline is in the photographic selection — the photo must carry the warmth that the type doesn't. Police this in selection, not in post.

## Colors

The palette is the most restrained of the three variants. Ink and sage do the heavy lifting. Gold and terracotta survive as accents. Cream is the room.

- **Primary — Ink 900 (`#16140F`).** The brand's grounding color. This is the variant's most decisive move: the brand-primary is *ink against cream*, not terracotta. Terracotta survives, but as an accent, not as the dominant color. The discipline: a brand that doesn't need a "brand color" to be recognized has earned the right to be recognized by its restraint. 16.2:1 against cream-100 (WCAG AAA).
- **Ink 800 (`#252118`).** Body text on cream surfaces. Slightly softer than ink-900 to reduce contrast vibration in long-form reading. 13.4:1 against cream-100 (WCAG AAA).
- **Ink 700 (`#3A332B`).** Sub-body text — captions on body-photo composites, secondary metadata. 9.6:1 (WCAG AAA).
- **Secondary — Sage 700 (`#4B5849`).** The variant's "color." A deep sage-green pulled from real cooling tea, real cypress shadow at 3pm, real moss on the lake stone at 4pm in late October. Used for sub-headlines, button-secondary hover, the underline accent on couples'-name pull-quotes. 7.4:1 against cream-100 (WCAG AAA).
- **Sage 500 (`#7B8A78`).** A softer sage for tertiary type, secondary-card backgrounds when a chromatic tone reads better than another cream-step. 4.5:1 against cream-100 (WCAG AA Large; never used for body).
- **Sage 300 (`#B5C0AF`).** The lightest sage, for hairline accents on photo-cards and the underline beneath section opener marks. Decorative-only — never carries text.
- **Tertiary — Gold 600 (`#9C7833`).** The warm-gold accent. The color of unvarnished brass in soft daylight, of pan-dulce at 3pm, of a sage tea in a brass cup. Used as the rare accent: couples'-names in a pull-quote, the back-of-ticket underline, one word italicized for emphasis in the manifesto. 4.6:1 against cream-100 (WCAG AA Large).
- **Gold 700 (`#7A5A1F`).** The deeper gold, used inside `pull-quote` text. 6.4:1 against cream-100 (WCAG AA).
- **Gold 500 (`#B8965A`).** The lightest gold, for hairline accents and decorative rules only. 3.4:1 (AA Large only — never for body text).
- **Accent — Terracotta 600 (`#A14A30`).** Terracotta is *demoted* from primary to accent in Variant C. Used once per layout maximum, for moments of recognition: a single italicized word, a back-of-ticket underline, the lower-right mark on a press one-sheeter. 5.6:1 against cream-100 (WCAG AA).
- **Neutral — Cream 100 (`#F7F2E6`).** The breathable background. Cooler than Variants A or B by a half-step — the cream of cold-pressed paper rather than baked adobe.
- **Surface — Cream 50 (`#FDFAF3`).** Half-step lighter.
- **Cream 200 (`#EFE7D2`).** Deepest tonal layering.
- **Slate 500 (`#7A7468`).** Captions, metadata, photo credits. 4.7:1 on cream-100 (WCAG AA normal text).

**Banned, with reason:** hot pink (hookup), club neon (nightclub), pure white (corporate wellness — the cream is the explicit anti-white), black-and-chrome (nightclub), stylized golden-hour Instagram filter (faked light), pure black (#000) — the brand's ink is always #16140F, never #000, because pure black against cream creates an optical vibration the restrained register cannot afford.

## Typography

Two typefaces. A third for rare human-moment punctuation.

- **Domaine Display / Söhne Breit** (display + headline). A refined modern serif — closer to *The Gentlewoman*'s headline type than to Reid Miles' Blue Note grammar. The letterforms are more architectural, the proportions more classical, the contrast between thicks and thins higher. Used for `hero-display` (56px), `headline-lg` (40px), `headline-md` (28px), `headline-sm` (20px). **Weight is held at 400** — the lightest weight of the three variants — because the restrained register depends on type that doesn't shout. Acceptable substitutes, in order: **Söhne Breit**, **Tiempos Headline**, **GT Sectra**, **Georgia**.

  Why this serif: Domaine is what *Apartamento*, *Cereal*, and design-conscious editorial publishing reach for when they want headline type that reads as *cultivated* rather than *bold*. The 400-weight choice is the variant's most decisive type move — weight 500 would push the variant back toward Variants A and B; weight 400 keeps it in the restrained register.

- **Söhne / Inter** (body + label). Same humanist grotesk as Variant B's body face, but used at slightly smaller default sizes (`body-md` at 15px, not 16px; `label-caps` at 11px, not 12px). The size reduction is *deliberate restraint* — the variant trusts the reader to lean in. Used for `lead` (20px), `body-lg` (17px), `body-md` (15px), `body-sm` (13px), `label-caps` (11px tracked +0.18em — widest of the three variants), `caption` (12px). Weight 400 for body, 500 for `label-caps` only (not 600 — the restrained register depends on the lighter label-caps weight).

  Sub-rule specific to Variant C: **label-caps gets +0.18em tracking, the widest of the three variants.** This is the only place the variant pushes letterspacing. The wider tracking lets the small (11px) label-caps read at a confident size despite being numerically smaller than A or B. The register: a *category mark in a magazine spread*, not a UI label.

- **Homemade Apple** (`hand-script`). Used only for human moments. Slightly smaller (26px in this variant, not 28px) to match the overall restrained scale.

The discipline lives in the **scale reduction + letterspacing widening**. A 56px hero at 400-weight on cream feels more confident than a 72px hero at 500-weight, because the 56px hero is saying *I don't need to be bigger to be heard*.

## Layout

The grid is **body-centered with generous gutters.** Content maxes at 1180px on desktop. The variant's signature is **spacious internal padding** — `card-text` at 40px (Variants A and B use 32px), `xxl` at 56px (vs. 48px), `xxxl` at 80px (vs. 64–72px).

Spacing scale: `xs: 4`, `sm: 8`, `md: 12`, `base: 16`, `lg: 24`, `xl: 32`, `2xl: 56`, `3xl: 80`.

Section margins between major content blocks default to `2xl` (56px) desktop, `xl` (32px) mobile. Cards and stacked content use `xl` (32px) gutters — wider than A or B.

**Whitespace philosophy:** the variant's most decisive move. Where A favors editorial-broadsheet density and B favors architectural alignment, C favors **room around every element**. A pull-quote in this system has 80px of whitespace above and below it. A section header is preceded by 80px. A photograph is followed by 56px of caption-and-breathing-room before the body resumes. The system trusts the reader's pace.

**Photo composition:** photographs in Variant C are tighter-cropped than A or B. Where A shows body + room context and B shows room + body inside it, C crops to **gesture, detail, and the suggestive fragment**. A hand on a fader. The side of a face listening. Two bodies' shoulders almost touching, framed from the waist up. The variant's photographic register is intimate-essayistic, not environmental.

## Elevation & Depth

**Flat. The most flat of the three variants.** No shadows except the photographic shadow living inside the photograph itself. Depth comes from the cream-50 / cream-100 / cream-200 step and from the *generous internal padding* of every component.

A `card-text` block in Variant C has so much internal padding (40px) that it reads as a *cleared space*, not as a card with a fill. The padding is the depth.

Hover state on interactive elements: a single tonal background shift (e.g., `button-secondary` hover changes from transparent to cream-200). No shadow change, no scale change, no movement.

Floating panels, glass-morphism, neon glow, animated gradient backgrounds — forbidden. They smuggle the visual grammar of a different kind of party.

## Shapes

**Quietly rounded.** Variant C uses `rounded.md` (4px) on every component — buttons, cards, inputs, photo frames. The 4px is the variant's compromise: not the editorial sharpness of A (2px), not the architectural rigidity of B (0px), but a quiet softness that says *this is a refined room, not a museum*.

`rounded.full` only for round photo crops (Andrea's portrait). Never for buttons.

Mixing radii within a single composition is forbidden. The 4px register holds.

## Components

- **`button-primary`** — **Ink-900 background**, cream on-primary text, **4px radius**, `label-caps` typography (11px, weight 500, +0.18em tracking), 16px padding. Hover transitions to ink-800 (the softest hover of the three variants). The most decisive component move in Variant C: the primary button is **ink, not terracotta**. Terracotta has been demoted to an accent used elsewhere. Used for the single most-important action per screen.

- **`button-secondary`** — Transparent background, ink-900 text, 1px solid border-hairline, 4px radius, 16px padding. Hover fills with cream-200 (not ink — the variant's secondary hover is a *tonal warming* of the background, not a chromatic inversion). Used for the second action per screen.

- **`button-ghost`** — Transparent, ink-900 text, no border, 0px radius. Inline third-tier interaction. The only `rounded.none` component in the system — ghost buttons are *type with hit-area*, not buttons.

- **`card-photo`** — Cream-50 surface, 4px radius, zero internal padding. Captions sit beneath, not inside.

- **`card-text`** — Cream-50 surface, 4px radius, **40px internal padding** (the variant's signature — more generous than A or B). Body text in ink-800. Used for manifesto pull-quotes, story excerpts, FAQ blocks.

- **`input`** — Cream-50 background, ink-900 text, 1px solid border-hairline, 4px radius, 14px padding. Focus state: ink-900 border at 2px. The variant is the only one whose input focus is *ink*, not terracotta — consistent with terracotta's demotion to accent.

- **`badge-event`** — **Transparent background**, ink-900 text, 0px radius (no card-fill), 1px hairline border top + bottom only, `label-caps`. The variant's most decisive component substitution: the badge is *not a filled pill*; it is *text framed by two horizontal hairlines*. Used to mark date and city in editorial layout: `JULY 2026 · CHICAGO`.

- **`divider`** — 1px solid `border-hairline`. The hairline is more visible in Variant C than in A because the cooler cream-100 lets the hairline read as a deliberate paper-cut rather than a paper-fold.

- **`pull-quote`** — Transparent background, gold-700 text, no card-fill, 2px solid gold-600 left-border. The most editorial pull-quote of the three variants — it is *not a panel*; it is *type with a hairline rule beside it*, the way a magazine sets a pull-quote in the margin. Used once per long-form piece.

## Do's and Don'ts

**Do:**

- Use a real photograph as the lead element of every primary surface.
- Crop tighter than Variants A and B. Gesture, detail, suggestive fragment. The intimate-essayistic register depends on it.
- Hold type at smaller sizes — 56px hero, 15px body. The restraint is the discipline.
- Use the lighter type weight (400 hero, 400 body, 500 label-caps). The variant's confidence lives in the lightness.
- Use ink-900 as the brand-primary, not terracotta. Terracotta is the rare accent, used once per layout maximum.
- Use sage-700 as the secondary anchor. Where A uses midnight, B uses moss, C uses a softer sage that reads as a cleared interior, not as architectural shadow.
- Use `label-caps` at +0.18em tracking — the widest of the three variants. Small label-caps + wide tracking is the variant's signature.
- Give every component generous internal padding — 40px for `card-text`, 56px for section margins, 80px before pull-quotes. The whitespace is the variant.
- Use the editorial `pull-quote` (transparent + left-border) instead of a filled card. The magazine grammar.
- Use the editorial `badge-event` (transparent + horizontal hairlines top/bottom). Not a pill, not a fill.
- Honor the daytime mechanic absolutely. The 11pm test is the floor.

**Don't:**

- Use any photograph that could have been taken at 11pm. If unsure, kill it.
- Generate front-of-house photography with AI. AI faces are forbidden across the entire system.
- Push hero type past 56px or body type past 17px. The variant is defined by the restraint.
- Use type weight 500 or 600 for hero or body. The 400 weight is load-bearing.
- Use terracotta as the brand-primary. Terracotta is demoted to *accent*. Treat it as you would italics — used sparingly, for moments of emphasis.
- Use pure white (#FFF) or pure black (#000) for backgrounds or text. The cream-50 and ink-900 are the explicit anti-defaults.
- Drop the internal padding to "save space." The whitespace IS the design.
- Use a filled pill or rounded-full badge. The badge is transparent + horizontal hairlines.
- Use a colored-panel pull-quote. The pull-quote is transparent + left-border. The magazine grammar matters.
- Animate quickly. Motion in this variant is the slowest of the three.
- Use hand-script as a default tone. More than once per composition is decorative slop.
- Combine the 4px radius with 0px or 8px shapes in the same view. Pick one register and hold.

---

## Appendix — Photography Direction (Variant C specifics)

The full photography spec at `01-visual/photography-rules.md` is binding. Variant C specifics:

- **Composition is intimate-essayistic.** Tight crops: a hand on a fader, the side of a face listening, two bodies' shoulders almost touching framed from the waist up, the slight bend of a wrist mid-gesture. Where Variant A shows body-and-room and Variant B shows room-with-body-inside-it, Variant C shows **the detail that contains the whole feeling**. Annie Leibovitz's quiet single-subject portraits and Nan Goldin's daytime kitchen-table frames (from `aesthetic-references.md` Group 2) are the load-bearing references.
- **Tonal grading is cool-restrained.** The cream-100 in this variant is the coolest of the three. Photography is white-balanced to honor that cooler cream — preserve the slight blue undertone of overcast Chicago afternoon daylight, never warm it artificially. The terracotta of the brand survives in the photograph only when it is *literally there in the room* (a brick wall, a wood floor in late light) — never invented in post.
- **Framing emphasis: gesture + restraint.** The eye is led to the gesture by the absence of competing information. Empty negative space carries weight. A photograph in this variant has more *visible room* in the frame than the body occupies.
- **The 11pm test still applies.** No flash. No club lighting. No neon. No tungsten-only interiors.

## Appendix — Motion Principles (Variant C specifics)

Resonance moves slowly. Variant C is the slowest of all — the restrained register requires it.

- Default transition: 280ms, ease-out. The longest of the three variants.
- Hover states: a single tonal-background warming (cream → cream-200 for button-secondary; ink-900 → ink-800 for button-primary). No movement, no shadow, no scale.
- Page transitions: a single cross-fade at 320ms.
- Scroll-triggered animation: gentle parallax on photographic blocks (≤ 8% movement — least of the three variants). The restrained register rejects motion as ornament.
- Forbidden: bounce, spring, parallax >10%, animated gradient, flicker, kinetic typography, scroll-jacking, scale-on-hover, glow-on-focus.

---

## Sample Applications

### Instagram Feed Post (1080 × 1350)
A tight-cropped photograph of two bodies' shoulders almost touching, framed from the waist up, in cream-walled south-facing window light. The composition leaves the upper two-thirds of the frame as cleared room — the white wall, the soft shadow, the suggestion of a single sage plant in the deep-left corner. Lower-third overlay: Domaine Display 28px in ink-900 — *"The body knows first."* Lower-right: wordmark in label-caps ink-900 at 60% opacity, +0.18em tracking, very small (11px equivalent at IG scale). The system disappears; the photograph and the line carry the post.

### Instagram Story Frame (1080 × 1920)
Cream-100 solid background. Vertically centered: Domaine Display `headline-md` (28px) in ink-900 — *"You have read enough articles about why you are still single. / This is a room."* A single hairline rule (1px border-hairline) sits 32px below the type, 80px wide, left-aligned beneath the first character. Lower-right wordmark in label-caps slate-500 at +0.18em tracking. The most type-driven of any sample frame across the three variants — Variant C's restraint earns the right to occasionally let type alone do the work, when the line is the photograph.

### Flyer / Poster — July Event (2550 × 3300 @ 300dpi)
**The most spacious of the three variant flyers.** Page is divided into three asymmetric bands with generous whitespace between:
- **Top band (30% of page):** cream-100. Wordmark *Resonance* in Domaine Display 56px ink-900, weight 400, left-aligned 80px from edges (Variant C's `xxxl` margin). Beneath: a single 1px hairline rule in border-hairline, 60% page width. Below rule: `JULY 2026 · CHICAGO · DOORS 2PM` in label-caps ink-900 +0.18em.
- **Middle band (45% of page):** single horizontal photograph, tight-cropped to gesture-and-detail (a hand on the fader, or two bodies' shoulders almost touching). Aligned center, with 80px of breathing room above and below.
- **Bottom band (25% of page):** cream-100. Single line in body-lg ink-800: *"A daytime, sober dance party for people who want to meet a partner."* 56px gap. Button-secondary CTA *Reserve your seat →* in ink-900 with 1px hairline border, 4px radius. Lower-right (small): a single italicized line in body-sm slate-500 — *Resonance 002 · Curated admission · resonanceroom.com*.

### Event Ticket (4 × 6" postcard)
**Front:** a single intimate-cropped photograph from the photographer brief — a hand on a fader, or the side of a face listening — full-bleed. Lower-left overlay: Domaine Display wordmark *Resonance* in cream-50 at 28px, weight 400. Lower-right: Andrea's hand-script signature in Homemade Apple 26px in cream-50.
**Back:** cream-100 paper-stock background (cool-warm-white, uncoated). Top-left: Domaine Display `headline-sm` (20px) in ink-900 — *Resonance 002*. Body: event date, venue, doors, in label-caps stacked left, +0.18em tracking, very widely spaced. Center: a single sentence in body-md ink-800, italicized — *"You were in the room on [date]."* Lower-right: a 0.75" hairline-thin terracotta-600 underline (the variant's one place terracotta appears at this scale — keeping the brand-accent legibility alive). QR code for entry: lower-left, 0.75" square, ink-900.

### Andrea Portrait (founder shot for press / About page)
Andrea at the decks, mid-set, head down, hand on the fader. The crop is tighter than Variants A or B — framed from the waist up, the room visible only as a soft cream wall and a sliver of natural daylight in the upper-right. Negative space is the second protagonist; the room appears as *suggestion*, not as architectural detail. Tonal grading is cool-restrained — the slightly blue undertone of overcast Chicago afternoon preserved. The shot reads as *the founder, mid-thought*, not as *the founder posing as the founder*. On a press one-sheeter, this photograph sits in the middle band with 12px caption-12px slate-500 beneath: *"Andrea — Resonance 001, Chicago, July 18, 2026."*

### Venue Pitch — One-Pager Top Section (Letter portrait)
**The most spacious of the three variant one-pagers.**
**Page header (top 1/5):**
- Domaine Display wordmark *Resonance* in ink-900 at hero-display 56px, weight 400, left-aligned, 1" margin from the page edge.
- 1px hairline rule beneath, full page-width.
- Below rule: single line in label-caps slate-500 +0.18em — `A DAYTIME SOBER DANCE PARTY · CHICAGO · 2026`.
**Hero block (middle 1/2):**
- Single horizontal photograph, full-width within the 1" margin. Tight-cropped to intimate-essayistic detail (hand-on-fader or shoulders-almost-touching).
- Caption in caption-12px ink-800: *"Photographed at Resonance 001, Chicago, July 18, 2026."*
**Body block (lower 1/4):** three columns — *What it is* / *The mechanic* / *Press contact* — each in body-md (15px), separated by hairline dividers. Generous 80px whitespace between the hero block and the body block.

The page reads as a magazine feature, not as a sales sheet. The discipline is the discipline of an audience that is treated as adult.

---

## Cross-references

- `00-foundation/05-non-negotiables.md` — the 12 lines this variant honors
- `00-foundation/01-brand-bible.md` §8 — strategic visual intent
- `00-foundation/03-voice-document.md` — voice the visual must read as
- `01-visual/DESIGN.md` — the v1 anchor this variant restrains
- `01-visual/photography-rules.md` — binding photographer brief (composition emphasis Variant C: Annie Leibovitz quiet portraits + Nan Goldin daytime frames from Group 2)
- `01-visual/aesthetic-references.md` — mood board (Group 4 entries 20 + 19 — Gentlewoman / Fantastic Man and NYRB layout — are the load-bearing references for this variant)
