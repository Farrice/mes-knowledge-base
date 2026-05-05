# Resonance — Component Tokens

*The locked production spec for repeating assets. A designer opens Figma or Canva, references this file, and ships on-brand without further direction.*

*All tokens reference `01-visual/DESIGN.md`. If a value is not specified here, default to the DESIGN.md token.*
*Source spine: A1-reconciliation §3 conflict #4 + §6 cascade #1; Brand Bible §8.*
*Last updated: 2026-05-04.*

---

## Global Defaults (apply everywhere unless overridden)

| Property | Default | Source token |
|---|---|---|
| Background | Cream 100 | `colors.neutral` (#F5EFE3) |
| Body text | Ink 900 | `colors.ink` (#1A1814) |
| Headline font | GT Sectra, weight 500 | `typography.headline-*` |
| Body font | Inter, weight 400 | `typography.body-*` |
| Accent (sparing) | Terracotta 600 | `colors.primary` (#B8492E) |
| Anchor / midnight | Midnight 900 | `colors.secondary` (#0F1A2E) |
| Hand-script | Caveat (rare punctuation only) | `typography.hand-script` |
| Border radius | 2px / 4px | `rounded.sm` / `rounded.md` |
| Hairline rule | 1px Border-hairline | `colors.border-hairline` |

The wordmark is set in GT Sectra at the headline size for the surface, in midnight 900 by default, in terracotta 600 only when the surface is photo-led and the wordmark needs to read against a darker frame.

---

## 1. Instagram Feed Post — `1080 × 1350` (4:5)

The single most-used surface. The discipline of this template carries the brand on the daily.

### Layout
- **Photo block:** Full-bleed, edge-to-edge, occupying ≥ 80% of the canvas height.
- **Headline overlay (when present):** Lower-left quadrant, 1–2 lines max, GT Sectra `headline-md` (32px equivalent) in cream-50.
- **Brand mark:** Wordmark in lower-right, `label-caps` (12px equivalent) in cream-50 with 60% opacity. Never larger than the headline.
- **Padding from canvas edge:** 64px on all sides for any text element.

### Token usage
- Photo: real photograph honoring `photography-rules.md`
- Overlay headline: `typography.headline-md` in `colors.cream-50` with subtle ink-900 drop-shadow (`0 2px 6px rgba(26,24,20,0.4)`) — only when the photo's lower-left has insufficient contrast.
- Brand mark: GT Sectra wordmark, `label-caps`, cream-50 at 60% opacity.

### Copy length
- **Floor:** 0 words on the image. A photograph alone is a complete IG post.
- **Ceiling:** 12 words on the image. *"Heart encounters, not head encounters."* + *"Chicago. June 2026."* is the maximum stack.

### Do
- Lead with the photograph; type is caption.
- Use one alignment (left). Never center two elements differently.
- Hold terracotta back — it appears in IG feed only on event-announcement posts.

### Don't
- Use more than 1 typeface in the image.
- Stack a headline and a tagline and a CTA in the same image — that's flyer grammar.
- Add color-blocked overlays, gradients, or vignettes.
- Apply Instagram filters. Native color science only.

### Reference: Event #1 announcement post structure
- Photograph: real bodies in daylight, mid-gesture
- Lower-left overlay: GT Sectra headline 32px — *"Chicago. The first event is June 2026."*
- Lower-right wordmark: cream-50 at 60% opacity
- Caption (in the IG body, not the image): full manifesto-trailer text

---

## 2. Instagram Reel Cover — `1080 × 1920` (9:16)

The cover is the entry door for a reel. Photo-led, headline reserved for the reel hook.

### Layout
- **Photo block:** Full-bleed, edge-to-edge.
- **Headline:** Vertically centered in the upper third, 1–2 lines, GT Sectra `headline-lg` (44px equivalent), cream-50 with subtle drop-shadow.
- **Brand mark:** Lower-center, `label-caps` in cream-50 at 60% opacity, 64px from bottom edge.

### Token usage
- Headline: `typography.headline-lg` in `colors.cream-50`
- Photo: real photograph; vertical-orientation crop preferred (a body in motion reads taller than wider on this canvas)

### Copy length
- **Floor:** 3 words (a question or a hook).
- **Ceiling:** 8 words.

### Do
- Use the reel cover hook as a question or a recognized phrase. *"Why is it so hard to meet a good person?"* or *"You've tried the apps."*
- Crop vertical: prioritize bodies in vertical motion.

### Don't
- Cram the entire manifesto into the cover.
- Use stock vertical "dance" footage. Real reels only.

---

## 3. Instagram Story — `1080 × 1920` (9:16)

Ephemeral. Lower text-density. Designed for swipe-throughs, polls, questions, link redirects.

### Layout
- **Photo block (or solid cream-50 fill):** Full-bleed.
- **Text:** Centered horizontally, vertically positioned at the safe-zone for IG UI (≥ 250px from top, ≥ 250px from bottom).
- **Sticker placement:** Polls and question stickers center-canvas, never overlapping the brand mark.
- **Brand mark:** Lower-right, label-caps in midnight 900 (when on cream) or cream-50 at 60% (when on photo).

### Token usage
- Text: `typography.body-lg` (18px → scales for story display) in `colors.ink` on cream OR `colors.cream-50` on photo
- Background: `colors.cream-100` solid OR a real photograph

### Copy length
- **Floor:** Single phrase or single question.
- **Ceiling:** 25 words across one story frame. Use sequential frames if more is needed.

### Do
- Use stories for daily texture: *one photo, one question*. Andrea-led voice memos, behind-the-scenes peeks at music curation, ICP recognition prompts.
- Use polls and questions to surface ICP voice (Pattern 4 — out-loud-asking).

### Don't
- Use Story templates from Canva that come pre-loaded with hookup-event grammar.
- Overlay hand-script on photographs. Hand-script is reserved for human-moment punctuation in printed/permanent assets — see §6.
- Use animated stickers, GIF backgrounds, or kinetic text. Stillness is the brand register.

---

## 4. Flyer — Digital — `8.5 × 11"` portrait (2550 × 3300px @ 300dpi)

The digital event flyer for IG carousels, email attachments, partner shares.

### Layout
- **Top half:** Single primary photograph, edge-to-edge.
- **Lower half (cream-100 background):**
  - Wordmark in midnight 900, GT Sectra at 64px
  - Hairline divider (1px border-hairline)
  - Event details in label-caps (12px): `JUNE 14, 2026 · CHICAGO · DOORS 2PM`
  - 16px padding-base spacing
  - Single line of body copy in ink-700, body-md (16px): *"A daytime, sober dance party for people who want to meet a partner."*
  - 24px padding-lg spacing
  - Application CTA in button-secondary style: `APPLY FOR THE NEXT EVENT →` in midnight 900 with hairline border

### Token usage
- Photo: real photograph from Event #1 or Event #1 visualization
- Wordmark: `typography.hero-display` 64px equivalent
- Details: `typography.label-caps`
- Body: `typography.body-md`
- CTA: button-secondary component pattern

### Copy length
- Wordmark: always *"RESONANCE"*
- Single-line body: max 12 words
- Details: 4 fields (date, city, doors, application CTA)

### Do
- Single photograph. Photo as protagonist.
- 50/50 split: photo top, type bottom. Discipline the proportion.
- Use the manifesto sub-line *"A daytime, sober dance party for people who want to meet a partner."*

### Don't
- Use multiple photographs in collage. Single hero only.
- Add price, sponsor logos, or a long bullet list of "what to expect."
- Use bottom cream space for hand-script or decorative elements.

---

## 5. Flyer — Physical Print — `8.5 × 11"` portrait

Same as Digital Flyer, with print specifications.

### Print specifications
- **Color profile:** CMYK (sRGB version stored separately for reference)
- **Paper stock:** Uncoated 100lb cover, warm-white tone (matches cream-50 on screen as closely as paper allows). Suggested stock: French Paper Construction Whitewash, Mohawk Loop Antique Vellum, or Strathmore Premium Opaque. Confirm sample swatch against cream-50 (#FBF7F0) before run.
- **Ink:** Standard CMYK. No Pantone spot for the run-of-the-mill flyer; reserved for the higher-stakes deliverables (event tickets, press one-sheeter).
- **Bleed:** 0.125" all sides. Crop marks included.
- **Finish:** No coating, no UV, no varnish. The brand is matte, paper-honest.

### Distribution rules
- Flyers go up only at venues whose own aesthetic doesn't cannibalize Resonance — independent record stores, daytime cafés, dance studios, bookshops.
- Flyers do **not** go up at bars, nightclubs, hookup-coded singles event venues.

---

## 6. Event Ticket / Keepsake — `4 × 6"` postcard

Ticket as memento. Designed to feel like the room, not like Eventbrite.

### Layout
- **Front:**
  - Single photograph from Event #1 (after Event #1 — for Event #1 itself, an evocative pre-event reference photograph), full-bleed
  - Lower-left overlay: GT Sectra wordmark in cream-50, 32px
  - Lower-right: hand-script signature of Andrea (the only place the hand-script appears on a public-facing asset for Event #1; later events may include a couple's name in hand-script per Andrea's curation)
- **Back:**
  - Cream-100 background
  - Top: GT Sectra `headline-sm` (24px) — `RESONANCE 001` (or `002`, `003`...)
  - Body: event date, venue, doors, in `label-caps` stacked on left
  - Center-right: a single sentence in `body-md`, ink-700: *"You were in the room when [date]."* — handwritten or typeset depending on whether it's a pre-event ticket (typeset) or a post-event keepsake (hand-written by Andrea or curator)
  - Lower-right: hairline-thin terracotta-600 underline

### Token usage
- Front photo: real photograph, daylight-locked
- Front wordmark: `typography.headline-md`
- Front signature: `typography.hand-script`
- Back: `typography.headline-sm` + `typography.label-caps` + `typography.body-md`
- Terracotta accent: `colors.primary` (single appearance)

### Print specifications
- 4×6" card, 16pt cover stock, uncoated, warm-white
- One side full CMYK photograph, other side single-color (midnight 900) printing on cream stock — this *is* the cream-100 paper, not a printed cream
- Optional: emboss the wordmark blind on the back of premium tickets (S2+ events, post-validation)

### Do
- Treat the ticket as a keepsake. People will save these.
- Sign by hand when the ticket count allows it (≤ 50 attendees per event).

### Don't
- Print event details on the front. Front is photo + wordmark.
- Add QR codes on the front. QR for entry goes on the back, lower-right corner, 0.75" square, in midnight 900.
- Mass-produce. The ticket carries Andrea's care; the print run reflects that.

---

## 7. Email Header — `600 × 300px` banner

For newsletter sends, RSVP confirmations, post-event recaps.

### Layout
- **Background:** Cream-100 fill (or, for hero-driven sends, a single horizontal photograph cropped to 600×300)
- **Content:**
  - GT Sectra wordmark in midnight 900 at `typography.headline-md` (32px), centered horizontally, vertically centered
  - Below: 1px hairline divider in border-hairline, 60px wide, centered
  - Below: single-line subline in `label-caps`, slate-500, e.g., `CHICAGO · JUNE 2026`

### Token usage
- Background: `colors.cream-100` OR photograph
- Wordmark: `typography.headline-md` in `colors.secondary`
- Divider: 1px in `colors.border-hairline`
- Subline: `typography.label-caps` in `colors.muted`

### Variants
- **Manifesto-send header:** Wordmark only, no subline. The body of the email carries the rest.
- **Event-announcement header:** Photograph background with wordmark in cream-50.
- **Post-event recap header:** Single photograph from the event, wordmark cream-50 over the lower-third.

### Do
- Keep the header light. The email body does the work.
- Use the subline for date + city; let the manifesto language live in the email body.

### Don't
- Stack a hero image, headline, and CTA all in the header. The header announces. The body delivers.

---

## 8. Press One-Sheeter PDF — `Letter / A4` portrait

For journalists, media, sponsor inquiries, venue pitches. One page. Designed.

### Layout
- **Page header (top 1/4):**
  - GT Sectra wordmark in midnight 900, `typography.hero-display` (64px), left-aligned
  - Hairline rule (1px border-hairline) below, full page-width
  - Below rule: single line in `label-caps`, slate-500: `RESONANCE · CHICAGO · 2026`
- **Hero block (middle 1/2):**
  - Single horizontal photograph, full-width within the 1" margin
  - Caption beneath in `caption` (13px) ink-700: *"Photographed at Event #1, Chicago, June 2026."*
- **Body block (lower 1/4):**
  - 3 columns
    - **What it is:** *"A daytime, sober dance party in Chicago for people who want to meet a partner. Heart encounters, not head encounters."* (body-md)
    - **The mechanic:** *"Daytime. Sober. Curated music. Curated crowd."* (body-md)
    - **Press contact:** Andrea + Farrice contact details, in body-sm
  - Below: single hairline divider
  - Bottom-left footer: `RESONANCEROOM.COM` in label-caps (placeholder until live URL confirms)
  - Bottom-right footer: page mark `01 / 01`

### Token usage
- Wordmark: `typography.hero-display`
- Hero photograph: real photograph
- Caption: `typography.caption` in `colors.body`
- Body columns: `typography.body-md`
- Press contact: `typography.body-sm`
- Hairline: 1px in `colors.border-hairline`

### Do
- Treat this as the brand's editorial statement on a single page. A journalist should be able to write the lede from the press one-sheeter alone.
- Use a single photograph that earns the entire middle of the page.

### Don't
- Add a logo, mission statement, founder bio, FAQ, and pricing all on one page. The press one-sheeter is **not** a full deck — it's a teaser.
- Use Word's default margins and stylings. This is designed in InDesign, Figma, or Pages with the Resonance grid honored.

---

## 9. Web Hero — Resonance Site (when it exists, post-Event #1)

The brand's first web surface. Built around a single full-bleed photograph + manifesto pull-line.

### Layout
- **Full-bleed photograph:** 100vh on desktop, 100vh on mobile. The opening hero is a single photograph from Event #1 (or, pre-event, the highest-quality reference frame from the photography brief).
- **Manifesto-line overlay:** Lower-third, GT Sectra `hero-display` (64px on desktop, 40px on mobile), cream-50 with subtle ink drop-shadow when needed for legibility.
- **Wordmark:** Top-left, `headline-md` cream-50.
- **Single CTA:** Bottom-right, button-primary style — `APPLY FOR THE NEXT EVENT →` in cream-50 on terracotta-600, with hover to terracotta-500.
- **Scroll indicator:** Center-bottom, label-caps in cream-50 at 50% opacity — `SCROLL`.

### Token usage
- Photo: real, daylight-locked
- Manifesto-line: `typography.hero-display` in `colors.cream-50`
- Wordmark: `typography.headline-md`
- CTA: `components.button-primary` (overlaid on photograph)
- Scroll: `typography.label-caps` at 50% opacity

### Hell-yes filter (the discipline)
The web hero uses **one** of the manifesto's hell-yes lines, rotated by event:
- *"Heart encounters, not head encounters."*
- *"A daytime, sober dance party in Chicago."*
- *"You've left a thousand rooms with a phone full of contacts and no one to call."*
- *"Movement before words. Stories over metrics."*

The line stays still long enough for a reader to read it. No kinetic typography. No cycle-through-multiple-lines animation.

### Do
- Hold the hero photograph until the user scrolls. The hero is the room — let it land.
- Use one CTA. Application is the only action above the fold.

### Don't
- Add a navigation bar that competes with the hero. The wordmark is the navigation; everything else lives below the fold.
- Run a video background. The system is photographic, not cinematic. Stillness is the register.

---

## Component-Specific Cross-Reference Index

| Component | Primary surface | Secondary surface |
|---|---|---|
| `card-photo` | IG feed (§1), web hero (§9) | Press one-sheeter (§8) |
| `card-text` | Email body, manifesto reprises | Web body sections |
| `button-primary` | Web CTA (§9), email primary action | Flyer CTA (§4) — only as button-secondary on flyers |
| `button-secondary` | Flyer CTA (§4), email secondary | Web subnav, footer |
| `button-ghost` | Inline actions, "skip intro" | "No thanks" / dismissal flows |
| `input` | RSVP forms, application form | Newsletter signup (when web exists) |
| `badge-event` | IG carousel announcements, flyer corner mark | Email header subline (§7) |
| `divider` | Press one-sheeter (§8), email body separators | Long-form web sections |

---

## Cross-references

- `DESIGN.md` — token source-of-truth; if any value here disagrees with DESIGN.md, DESIGN.md wins
- `photography-rules.md` — every photo on every component honors this brief
- `aesthetic-references.md` — when a designer needs to ground a decision, reference the mood board
- `brand-library-entry.md` — the entry that feeds external `knowledge/design-libraries/brands/resonance/`
- A1-reconciliation.md §3 conflict #4 — daytime-as-mechanic ruling
- Brand Bible §8 — strategic intent for visual
