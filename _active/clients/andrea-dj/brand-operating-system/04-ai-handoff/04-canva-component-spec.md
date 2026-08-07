# 04 — Canva Component Spec

*Locked Canva templates and brand-system setup so Andrea's daily design workflow stays on-brand without rebuilding the system every time. One-time setup: ~45 minutes. After that: open template, swap photo, swap copy, ship.*

*Last updated: 2026-05-04. Status: canonical.*

---

## The Spine Reminder

> *Resonance is heart encounters, not head encounters — a daytime, sober dance party in Chicago for people who want to meet a partner. The mechanic is body-first: the music does the emotional labor so the people don't have to. The metric is couples, not followers.*

---

## Why Canva (and What Canva Is For)

Canva is the daily workhorse for Andrea's design-execution layer. Specifically: IG feed posts, IG stories, flyers, ticket layouts, email header banners, sponsor decks, and quick social graphics. Canva is **not** the right tool for: the press one-sheeter (use a designer + InDesign), the printed event ticket on real cardstock (use a print partner), or the website (use a real web stack, not Canva Sites).

The job of this spec: pre-load every brand variable into Canva *once* — fonts, colors, photo treatment presets, type sizes, layout grids — so that any new design Andrea makes inherits the system without her having to remember every token. Pre-load the system; design from the system; never improvise the system mid-asset.

This file works against `01-visual/DESIGN.md` and `01-visual/component-tokens.md`. When those amend, this file updates with them.

---

## Step 1 — Install The Brand Fonts In Canva (10 min)

Canva supports custom font upload on Pro+ tiers. Install these three fonts before doing anything else.

### Fonts to upload

1. **GT Sectra** (license required — purchase at grilli.type)
   - Weight to upload: GT Sectra Book (400) and GT Sectra Medium (500)
   - This is the heat serif. Do NOT upload heavier weights — Resonance never uses 700+ on Sectra.

2. **Inter** (free — Google Fonts)
   - Weights to upload: Inter Regular (400), Inter SemiBold (600)
   - This is the body sans. SemiBold is reserved for `label-caps` only.

3. **Caveat** (free — Google Fonts)
   - Weights to upload: Caveat Regular
   - This is the rare hand-script. Used **only** for Andrea's signature on a thank-you note. NOT for body, NOT for headlines, NOT for navigation, NOT for event tickets.

### Acceptable substitutes (when GT Sectra is unlicensed)

If the GT Sectra license is unavailable, in priority order:

1. **Mortise** (Canva Pro library) — closest commercial substitute
2. **IBM Plex Serif** (free — Google Fonts)
3. **Georgia** (system default — last resort, but acceptable)

**Plus Jakarta Sans** is the documented substitute for Inter. Available in Canva's free font library.

### Where to upload

- Canva → Brand Hub → Brand Kit → Fonts → Upload Font
- Tag each font with its role: "GT Sectra — Display", "Inter — Body", "Caveat — Signature only"
- Pin them to the top of the font list so they appear first when designing

---

## Step 2 — Add The Brand Color Palette (5 min)

Canva → Brand Hub → Brand Kit → Colors → Add Color. Add each hex code below with the name as listed.

### Primary palette (load in this order — order = display order in Canva picker)

| Name in Canva | Hex | Role |
|---|---|---|
| Resonance Cream 100 | `#F5EFE3` | Background canvas |
| Resonance Cream 50 | `#FBF7F0` | Surface layer (one tonal step lighter) |
| Resonance Midnight 900 | `#0F1A2E` | Body type / headline / event badge fill |
| Resonance Ink 900 | `#1A1814` | Body type alt / fine detail (slightly warm black) |
| Resonance Ink 700 | `#3A332B` | Long-body text |
| Resonance Terracotta 600 | `#B8492E` | Primary CTA / single accent per layout |
| Resonance Terracotta 700 | `#9A3A22` | Hover / pressed state for CTAs |
| Resonance Slate 500 | `#7A6F62` | Captions, metadata, dates |
| Resonance Gold 600 | `#8C6526` | Tertiary accent (rare — couples' names in story-capture only) |
| Resonance Border Hairline | `#E1D6C2` | 1px dividers, input borders |

### Critical — what NOT to add

Do NOT add:

- Any default Canva-suggested palette (pinks, purples, "trending" gradients)
- Pure white (`#FFFFFF`) — Resonance uses Cream-50, not white
- Pure black (`#000000`) — Resonance uses Ink-900, not pure black
- Bright neons of any kind
- "Sober community" pastels (lavender, mint, blush)

If a previous version of the Brand Kit has any of these, delete them. Canva's color picker auto-suggests recently-used colors — pollution at this layer breaks discipline downstream.

---

## Step 3 — Set Up The Photo Treatment Presets (5 min)

Canva applies filters/effects/adjustments per-image. The Resonance discipline is: **no filters, no effects, daylight color preserved**. The "preset" for Resonance photography is *no preset.*

### The Resonance Photo Treatment

When inserting any photograph into a Canva template:

1. **Filter**: None. Click "None" in the filter panel. Never use Auto-Enhance.
2. **Adjust**: All sliders at 0 (Brightness, Contrast, Saturation, Tint, Blur, X-Process). The photograph was already color-corrected at the import stage; Canva should not re-touch it.
3. **Effects**: None. No drop shadow, no glow, no auto-focus, no duotone, no halftone, no neon-edge, no grayscale.
4. **Crop**: only as needed for the layout. Preserve native aspect ratio when possible.

### Acceptable adjustments (rare cases)

- **Brightness +5 to +10** if the import is too dark on Canva's display
- **Color temperature +5 (warmer)** ONLY if the import lost warmth in the JPEG conversion — never to "make it feel sunny"

That's it. Three sliders, low-magnitude, used rarely.

### Forbidden (kill on sight)

- Any Canva auto-filter (Vintage, Black & White, Cinematic, Drama, etc.)
- "Color Pop" effect (highlights one color, desaturates the rest)
- Duotone overlays (terracotta-and-midnight tinting of the image — kills the daylight)
- Gradient mask overlays
- "Photo to Cartoon" / any AI-stylization filter
- Frames (drop-shadow rectangles, polaroid borders, scribble outlines)
- Any "trending" filter Canva pushes weekly

### Save the preset

Canva doesn't currently support saving "no-effects" as a named preset. Alternative: create a **Brand Template** (Step 5) with the photo treatment baked in. Andrea pulls from the template instead of starting blank.

---

## Step 4 — Configure Brand Voice In Canva's AI Tools (3 min)

Canva's "Magic Write" and AI design suggestions are off-brand by default. Configure them.

### Brand voice settings

Canva → Brand Hub → Brand Voice → Configure

- **Tone**: paste the Resonance one-paragraph voice description (from `00-foundation/03-voice-document.md` §1)
- **Banned words**: paste the top 5 banned phrases from `04-ai-handoff/00-ai-brain-master.md` ("Here's what/why/how", "It's not X. It's Y.", "vibes/intentional/conscious/sacred", "high-value/alpha/king", "sober-curious community")
- **Required reading**: paste the spine reminder

This won't make Magic Write produce great output, but it will produce less catastrophically off-brand output.

### What to use Canva's AI for

- Resizing a finished design across formats (acceptable — preserves the design system)
- Background remover for placing a photo on cream-100 (acceptable)

### What NOT to use Canva's AI for

- Magic Write for captions, headlines, body copy — use Claude with the AI Brain Master instead
- Magic Edit for photographs — never AI-edit a real photograph; the photographer's work is the canonical source
- Text Effects (gradient text, shadow text, neon text) — banned by the design system

---

## Step 5 — Build The Five Locked Templates (20 min)

Build these once, save as Brand Templates, never recreate from scratch. Each template inherits the fonts, colors, and photo discipline from Steps 1-3.

### Template 1 — IG Feed Post

**Canvas**: 1080×1350 px (4:5 portrait)
**Layout**:
- Wordmark "Resonance" top-left, GT Sectra 24pt, Cream-100 (against photo) or Midnight-900 (against cream).
- Photo region: 1080×880 (top 65% of canvas), full bleed.
- Date/location stamp below photo: Inter SemiBold 12pt, all-caps, Slate-500, letter-spacing 0.12em. Format: `JUNE 14, 2026 · CHICAGO`.
- Headline below stamp: GT Sectra 64pt, Midnight-900, max 2 lines, ≤8 words.
- Body line below headline: Inter Regular 18pt, Ink-700, max 1 line, ≤30 words.
- CTA at bottom: Inter Regular 14pt, Terracotta-600, format: `Application opens June 1 · resonance.[domain]/apply`.

**Photo placeholder**: a real daytime room photo (post-Event-#1) or the Andrea-at-decks daytime portrait (pre-Event-#1).

**Save as**: Brand Template → name "IG Feed — Event Announcement"

### Template 2 — IG Story

**Canvas**: 1080×1920 px (9:16 portrait)
**Layout**:
- Photo region: full bleed across the entire canvas.
- Text overlay (when used): centered or lower-third placement, max 12 words.
- If text-on-photo: GT Sectra 48pt for headline, Inter Regular 18pt for body, all on Cream-100 or Midnight-900 depending on photo.
- Sticker placement (poll, question, link): single sticker per story frame, lower-third, off-center.
- Wordmark: optional, top-left, GT Sectra 18pt.

**Photo placeholder**: same as Template 1.

**Save as**: Brand Template → name "IG Story — Single Frame"

### Template 3 — Flyer (Digital + Physical)

**Canvas**: two versions:
- Digital: 1080×1350 px (matches IG Feed for cross-posting)
- Physical: 8.5×11 inches at 300dpi, CMYK profile

**Layout**: see `02-briefs/flyer-poster.md` Section 7.5 textual mockup.

Both versions inherit the same component arrangement; only the canvas and resolution differ.

**Photo placeholder**: a daytime room photograph, full bleed across upper 65-75% of the canvas.

**Save as**: Brand Template → name "Flyer — Event Announcement (Digital)" + "Flyer — Event Announcement (Print)"

### Template 4 — Ticket (Digital)

**Canvas**: 1200×1800 px (4:6 landscape — matches a 4×6 inch postcard at 300dpi)

**Layout**: see `02-briefs/event-ticket.md` Section 7 textual mockup. Front and back as two pages of the same Canva project.

**Critical**: NO photograph on the ticket. The ticket is type-led. The manifest line is the focal element.

**Save as**: Brand Template → name "Event Ticket — Digital"

### Template 5 — Email Header Banner

**Canvas**: 600×200 px (standard email header banner sizing — survives most email clients)

**Layout**:
- Cream-50 background.
- Wordmark "Resonance" left-aligned, GT Sectra 32pt, Midnight-900.
- Optional 1px hairline divider in Border-Hairline below the wordmark.
- That's it. The header banner is restrained — it's a letterhead, not a marketing graphic.

**Save as**: Brand Template → name "Email Header — Newsletter"

---

## Step 6 — The 45-Minute Setup Walk-Through

If Andrea is doing this from scratch in a single session:

| Time | Step | What gets done |
|---|---|---|
| 0:00 - 0:10 | Step 1 | Install GT Sectra, Inter, Caveat in Canva |
| 0:10 - 0:15 | Step 2 | Add 10 brand colors to Brand Kit |
| 0:15 - 0:18 | Step 3 | Confirm "no-filter" photo discipline; delete any existing brand-violating presets |
| 0:18 - 0:21 | Step 4 | Configure Magic Write voice settings |
| 0:21 - 0:25 | Step 5a | Build Template 1 (IG Feed Post) |
| 0:25 - 0:29 | Step 5b | Build Template 2 (IG Story) |
| 0:29 - 0:35 | Step 5c | Build Template 3 (Flyer — both versions) |
| 0:35 - 0:40 | Step 5d | Build Template 4 (Event Ticket) |
| 0:40 - 0:43 | Step 5e | Build Template 5 (Email Header) |
| 0:43 - 0:45 | Verify | Open each template, confirm fonts/colors load, save versions |

Done. From here forward: every IG post, story, flyer, or ticket starts from a locked template — not from a blank canvas.

---

## Step 7 — Daily Workflow (After Setup)

The end-state Andrea operates in:

1. **New IG post needed** → Open "IG Feed — Event Announcement" template → swap photo (drag in real daytime image, set filter to None, all sliders 0) → swap headline → swap date/location stamp → swap CTA → done in 6 minutes.
2. **New flyer needed** → Open "Flyer — Event Announcement" → same process → done in 8 minutes (digital) or 12 minutes (print).
3. **New ticket needed** → Open "Event Ticket — Digital" → swap recipient name → swap manifest line (rotate per Section 6 of `02-briefs/event-ticket.md`) → swap event date → done in 4 minutes per ticket.
4. **Email needed** → Use the Email Header template; the body is plain text in the email client, not in Canva.

**Andrea never starts from a blank Canva canvas for any of these surfaces.** That's the whole point of the setup.

---

## Step 8 — When To Update This Spec

Update this file when:

- A foundational doc amends (DESIGN.md adds a new color, component-tokens adds a new component).
- A new asset type enters daily workflow (e.g., a podcast cover, a sponsor deck cover).
- Canva ships a new feature relevant to the workflow (e.g., a saved photo-treatment preset feature).

Do NOT update for: occasional one-off designs, experimental templates, seasonal variations. Stability is the value.

---

## Common Failure Modes (and Fixes)

**Failure: Canva auto-suggests a default purple/pink/blue palette when designing.**
*Fix*: this happens when the Brand Kit isn't fully loaded. Re-do Step 2; pin the brand palette to top.

**Failure: GT Sectra renders incorrectly on a phone preview.**
*Fix*: Canva's mobile font rendering can lag on custom fonts. Confirm the font weight is exactly 400 or 500 (not 600/700). If still failing, fall back to Mortise (Canva native).

**Failure: A photo looks "flat" after import — Andrea wants to brighten it.**
*Fix*: confirm with the photographer first whether the import preserved color. If yes, brightness +5 is acceptable; never +20+. If the image needs heavy correction, re-export from the photographer's RAW with proper white balance.

**Failure: Andrea's collaborator opens a template and sees default Canva fonts (not GT Sectra).**
*Fix*: Brand Kit access requires Pro+ tier. Confirm the collaborator is added to the Resonance Brand Kit (not just shared on a template).

**Failure: A Magic Write caption draft uses banned phrases despite the Brand Voice setup.**
*Fix*: Magic Write's Brand Voice is loose; do not rely on it. Use Claude with the AI Brain Master instead, paste the result into Canva. This is the workflow.

---

## What's Out Of Scope For This File

- The press one-sheeter — designed in InDesign by a designer; not Canva work.
- The printed cardstock event ticket (Phase 2+) — produced by a print partner using the digital ticket as the source file; Canva → print-partner export, not Canva direct print.
- The website — coded with the design system per `01-visual/DESIGN.md`, not assembled in Canva Sites.
- The DJ booking pack PDF — designed in InDesign or Figma for the typography discipline.

Canva's job is the **daily-iteration social and email surfaces.** Anchor surfaces use real design tools.

---

## Source Citations

- `01-visual/DESIGN.md` — the canonical visual system this Canva setup mirrors
- `01-visual/component-tokens.md` — the components this file's templates execute
- `01-visual/photography-rules.md` §3 (banned editing) + §6 (no AI portraits) — the photo treatment discipline
- `00-foundation/03-voice-document.md` §1 + §5 — voice config for Canva's AI tools
- `02-briefs/ig-feed-post.md` Section 7 — the IG Feed template spec
- `02-briefs/ig-story.md` — the IG Story template spec
- `02-briefs/flyer-poster.md` Section 7 + 7.5 — the flyer template spec
- `02-briefs/event-ticket.md` Section 7 — the ticket template spec
- `02-briefs/email-newsletter.md` Section 7 — the email header spec
- `04-ai-handoff/00-ai-brain-master.md` — the cold-start that pairs with Canva for the copy side of the workflow
