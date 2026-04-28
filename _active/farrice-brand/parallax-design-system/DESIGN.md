---
version: alpha
name: Parallax
description: Japanese minimalism meets hip-hop typography. Muji meets Madlib. Tadao Ando concrete walls with Griselda Records swagger. The Virgil Abloh 3% Rule applied to a polymath's newsletter — take the most familiar premium-newsletter format (clean typography on solid background) and change exactly 3% of it. The 3% is the offset. One letter in violet. Quiet defiance, never aggressive. Recognition before sophistication. The confidence of an empty room.

colors:
  ink: "#1C1C1E"
  violet: "#7B61FF"
  warm-white: "#F5F0EB"

  primary: "{colors.ink}"
  accent: "{colors.violet}"
  surface: "{colors.ink}"
  on-surface: "{colors.warm-white}"
  on-accent: "{colors.warm-white}"

typography:
  display:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: 64px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.02em
  wordmark:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: 140px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.02em
  headline-lg:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0
  headline-md:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
  edition-number:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.12em
  body-lg:
    fontFamily: "Source Serif 4, Source Serif Pro, Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.6
  body-md:
    fontFamily: "Source Serif 4, Source Serif Pro, Georgia, serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.65
  body-italic:
    fontFamily: "Source Serif 4, Source Serif Pro, Georgia, serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.5
  tagline:
    fontFamily: "Source Serif 4, Source Serif Pro, Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.4
  label-mono:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.05em
  button-text:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.08em
  caption:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4

rounded:
  none: 0px
  sm: 2px
  md: 4px
  full: 9999px

spacing:
  xxs: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  xxl: 128px

components:
  wordmark:
    backgroundColor: "transparent"
    textColor: "{colors.warm-white}"
    typography: "{typography.wordmark}"
    padding: 40px
  wordmark-light:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.wordmark}"
    padding: 40px
  cover-frame:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.warm-white}"
    rounded: "{rounded.none}"
    padding: 80px
  edition-cover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.warm-white}"
    typography: "{typography.headline-lg}"
    rounded: "{rounded.none}"
    padding: 80px
  email-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.warm-white}"
    rounded: "{rounded.none}"
    height: 300px
    padding: 48px
  social-card:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.warm-white}"
    rounded: "{rounded.none}"
    padding: 80px
  pull-quote:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.warm-white}"
    typography: "{typography.headline-md}"
    rounded: "{rounded.none}"
    padding: 64px
  button-subscribe:
    backgroundColor: "{colors.violet}"
    textColor: "{colors.warm-white}"
    typography: "{typography.button-text}"
    rounded: "{rounded.sm}"
    padding: 16px
  button-subscribe-hover:
    backgroundColor: "{colors.warm-white}"
    textColor: "{colors.ink}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.warm-white}"
    typography: "{typography.button-text}"
    rounded: "{rounded.sm}"
    padding: 16px
  divider-rule:
    backgroundColor: "{colors.violet}"
    height: 1px
    width: 200px
  avatar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.violet}"
    typography: "{typography.wordmark}"
    rounded: "{rounded.full}"
    size: 256px
---

<!-- Parallax DESIGN.md — derived from parallax-creative-rebrief.md (Greg Hoffman + Oren, 2026-04-15). Canonical machine-readable spec. -->

## Overview

Parallax is a polymath's newsletter — for people who see everything from more than one angle. The brand is built on a single design philosophy: **the Virgil Abloh 3% Rule applied to publishing.** Take the most proven, premium newsletter format — clean typography on a solid background, the visual register of Seth Godin's blog, The Marginalian, Stratechery — and change exactly 3% of it. The 3% is *the offset*. A precise, deliberate misalignment that says "I see this differently than you expected." Not random. Not chaotic. The kind of thing a designer notices immediately and a non-designer feels without knowing why.

The cultural anchors are specific and intentional: **Muji meets Madlib.** **Tadao Ando concrete walls with Griselda Records swagger.** Japanese minimalist restraint paired with hip-hop album-cover typographic confidence. This is the cultural intersection of the founder, Farrice "Fresh" Cain — biracial polymath, stay-at-home dad, technologist, AI-systems builder, modern philosopher. It is not cyberpunk, not tech startup, not wellness. It is editorial gravitas with a quiet kind of swagger.

The intended emotional response, in order: **Recognition** ("this is for people like me") → **Relief** ("I don't have to explain myself here") → **Intrigue** ("what's the slight shift I'm noticing?"). Never: "this looks cool," never: "this is sophisticated," never: "this is a tech newsletter." The visual identity flatters the reader's intelligence through restraint. The writing is the product. The visuals get out of the way.

## Colors

The palette is two colors. That's not a constraint — it's the point. Every iconic publication identity uses 1-2 colors, maximum. Five colors is a committee decision that never punched. When everything is monochrome except one color, that one color becomes *yours*.

- **Ink (`#1C1C1E`)** — Near-black, not indigo, not navy. The absence of pretension. Apple's system dark background — proven, invisible, premium. Same darkness whether you read at midnight or noon. This is the foundation: the dark canvas on which Parallax lives.
- **Violet (`#7B61FF`)** — The Parallax accent. The 3%. The single point of attention. Used only where intent should land — the second L in the wordmark, primary CTA buttons, the divider rule on the cover, edition numbers, and nowhere else. Restraint is what makes this color powerful.
- **Warm White (`#F5F0EB`)** — Body text on dark, softer than pure white. Reads warmer at long-form length. Carries craft.

`#FFFFFF` pure white never appears. `#000000` pure black never appears. Both feel cheap by comparison. The palette commits to its specific darks and warms with conviction.

## Typography

Three typefaces, three jobs, no overlap.

- **Space Grotesk Bold (700)** — All headlines, the wordmark, edition titles. Geometric sans with a confident swagger. The hip-hop side of the cultural anchor. Set tight (letter-spacing +20 on the wordmark, normal elsewhere). Uppercase for the wordmark, sentence case for everything else.
- **Source Serif 4 Regular (400)** — All body text, taglines, italic accents. The editorial gravitas. The Muji side. Long-form reads on this typeface for hours; that is its job. Italic variants are reserved for taglines, pull-quotes, and emotional emphasis — used sparingly.
- **JetBrains Mono Regular (400)** — Edition numbers, technical labels, the polymath stack on the profile banner, prompt-pack code blocks, captions. The terminal-output register. It signals "this person actually builds things" without saying it.

The wordmark is set in Space Grotesk Bold at +20 letter-spacing — tight and confident, not loose and airy. Body type is set at 17-20px with line-height 1.6-1.65 for relaxed long-form reading. Edition numbers and technical labels use JetBrains Mono with +12% letter-spacing in uppercase to evoke a code listing. Never use more than these three typefaces. Never use Space Grotesk for body. Never use Source Serif for the wordmark. The discipline is the brand.

## Layout

Generosity is the layout philosophy. Margins are deliberate, not residual. Negative space is not empty — it is *active*. The confidence of an empty room.

The spacing scale is built on an 8px base unit (`xs: 8px, sm: 16px, md: 24px, lg: 40px, xl: 64px, xxl: 128px`). Section breaks use `xl` or `xxl`. Inside cards, padding is `lg` minimum. Inside the wordmark, padding is at least 40px on all sides. Edition covers use 80px padding on all sides. The asset is given room to breathe.

Grid model: single-column for body, max content width 720px for long-form readability. For asset compositions (covers, banners), the layout is anchored — wordmark center-vertical at ~40% from top for square covers, left-aligned with vertical-center for banners. The polymath stack on the profile banner sits left, the wordmark sits right, creating two visual planes at different opacities and alignments. That asymmetric tension *is* the parallax.

## Elevation & Depth

**Parallax is flat.** No drop shadows. No gradients. No neumorphism. No bevels. Depth is conveyed through tonal layering and typographic hierarchy, not light simulation.

When two surfaces need separation, they separate by color — `ink` for primary surfaces, `paper` (warm white) for inverse surfaces. There is no in-between. The single allowed elevation device is the **violet rule** — a 1px horizontal violet line under the wordmark on covers, ~60% the width of the wordmark above it. That is the one piece of "ornament" the system permits, and it functions as a divider, not decoration.

If a surface needs visual weight, it gets weight from generous padding and large type, not from shadows. The brand's discipline is that depth is earned through restraint, not added through effect.

## Shapes

Sharp corners. Architectural sharpness. The shape register is **functional purity** — no rounded buttons, no rounded cards, no rounded badges except where the surface is genuinely circular (the avatar, the favicon).

- `rounded.none` (`0px`) — covers, banners, cards, social previews
- `rounded.sm` (`2px`) — subscribe button, only when a touch of softness is needed without breaking the geometric language
- `rounded.md` (`4px`) — reserved; rarely used
- `rounded.full` — only avatar, only favicon

Mixing rounded and sharp corners in the same view is forbidden. The system holds discipline through geometric consistency. If a surface feels too austere, the fix is generous padding, not rounded corners.

## Components

The component system is small and specific. Variants are explicit; no implicit states.

- **`wordmark`** — PARALLAX in Space Grotesk Bold, 140px, +20 letter-spacing, all caps. Letters 1-3 (P-A-R) in warm white, letter 4 (the second L of "PARA**L**LAX") in violet, letters 5-8 (A-L-L-A-X) in warm white. (Counting: P-A-R-A-L-L-A-X. The 6th letter — the second L — is the one. *Buried in the middle, the letter you don't expect to notice.* The first letter would be obvious. The last would be try-hard.)
- **`avatar`** — Circular, 256×256 native (Substack scales). Solid `ink` background, single letter "P" in Space Grotesk Bold at 144px, centered, in violet. The minimum signature of the brand at the smallest scale.
- **`favicon`** — 32×32 and 64×64 PNG. Letter "P" in Space Grotesk Bold, violet on ink. Same as avatar but square.
- **`cover-frame`** — Square, 1200×1200 default. Solid ink background. Wordmark centered horizontally at 40% from top. Tagline below in Source Serif 4 Italic at 24px, warm white at 50% opacity. 1px violet rule below tagline at 60% wordmark width, centered. Bottom 30% intentionally empty.
- **`email-banner`** — 1100×300, solid ink. Wordmark left-aligned, vertically centered, scaled to ~32px cap height, 48px from left edge. Right side empty. The header should be invisible to the eye and confident in stance.
- **`social-card`** — 1200×630 OG image. Wordmark centered horizontally at 40% from top, ~72px cap height. Tagline 20px below, italic, 60% opacity. Single 200px violet rule below tagline. Bottom empty. Reads cleanly at thumbnail size — that is the test.
- **`profile-banner`** — 1200×400, solid ink. Two-plane composition: vertical word stack on the left in JetBrains Mono 14px, violet at 40% opacity (the polymath list — psychology / AI systems / fatherhood / anime / spirituality / strategy / and any others), and the wordmark right-aligned, vertically centered, ~28px cap height. The two planes at different opacities, fonts, and alignments create depth through contrast. This is the only place a visual element beyond the wordmark is permitted.
- **`edition-cover`** — 1200×1200 template. Solid ink background. Edition number top-left in JetBrains Mono 14px violet uppercase ("EDITION 002" pattern). Edition title 80px from top-left in Space Grotesk Bold 48-64px warm white, left-aligned, max width 80% of canvas. Single 1px violet rule below title, 200px wide. Optional small atmospheric AI image element bottom-right at 20-30% opacity for special editions only. Default: no image. Negative space is the design.
- **`pull-quote`** — Restack/share graphic. 1200×1200 or 1080×1080. Solid ink. Quote in Space Grotesk Bold 32-40px warm white, left-aligned, max 6 lines, max 80% canvas width. Below the quote, a 1px violet rule at 100px wide. Below the rule, attribution in JetBrains Mono 14px violet: "PARALLAX · EDITION 0XX" or "@PARALLAXLETTER". Bottom 20% empty.
- **`button-subscribe`** — Violet background, warm-white text, JetBrains Mono uppercase 14px with +5% letter-spacing. 16px vertical padding, 32px horizontal. 2px corner radius — barely there. Hover inverts to warm-white background with ink text.
- **`button-secondary`** — Transparent background, warm-white text, 1px warm-white border, JetBrains Mono uppercase. Same dimensions as subscribe button. For "Read in app" or "Share" actions.
- **`divider-rule`** — 1px solid violet, ~200px wide, used below wordmarks on covers, below pull-quotes, between sections in long-form posts when section breaks need violet emphasis. Used sparingly.

## Do's and Don'ts

The brand discipline lives here. Every "do" prevents a known failure mode the rebrief identified in the prior 4-5/10 attempts.

**Do:**

- **Do** use the violet only where attention should land. One violet element per composition is the maximum. Two is sprawl. Zero is acceptable for body-text editions where no CTA is present.
- **Do** keep the wordmark identical across every surface. Same font, same letter-spacing, same color logic, same proportions. Recognition compounds when the asset never changes.
- **Do** use Space Grotesk Bold for all headlines and the wordmark. Always. Even when "another font might fit" — it doesn't.
- **Do** use Source Serif 4 for all body, taglines, and pull-quotes. Italic Source Serif for emotional emphasis only.
- **Do** use JetBrains Mono only for edition numbers, technical labels, and the polymath stack. It signals "this person builds things."
- **Do** ship typographic-only covers as the default for editions. The wordmark + edition number + title is the canonical pattern. Reach for AI-generated atmospheric images only when the edition's content demands a specific visual metaphor (a prism for an optics essay, a mountain for a father-wound piece) — and even then, the image is at 20-30% opacity, bottom-right, subordinate to the typography.
- **Do** use generous padding. 80px on edition covers, 48px+ on email banners, 40px+ on the wordmark. The brand's confidence comes from negative space.
- **Do** maintain WCAG AA on every text/background pair. Warm white (`#F5F0EB`) on ink (`#1C1C1E`) clears 14:1 — well over AA. Violet (`#7B61FF`) on ink clears 6.7:1 — passes AA for normal text. Violet on warm white at 4.4:1 only passes AA for large/bold text (use accordingly).
- **Do** lock edition numbering convention: "EDITION 001", "EDITION 002", etc. Three-digit zero-padded. JetBrains Mono uppercase. Never "Ed. 1", never "#1", never "Volume 1".

**Don't:**

- **Don't** generate a logo mark. Parallax does not have a logo. The wordmark IS the logo. One artifact, not two. The "Shifting P" / "Prism Mark" / "Layered Lens" instinct is wrong — the word IS the brand.
- **Don't** introduce a third color. Bronze, teal, blue, green, amber — all wrong. Two colors. One dark, one accent. Adding a third dilutes the violet's power.
- **Don't** use AI image generation for the wordmark, banners, or core identity assets. AI generates illustrations; identities require precision and intentionality at every pixel. AI images are seasoning, never the main course.
- **Don't** mix rounded and sharp corners in the same view. Pick one geometric register and hold it.
- **Don't** use drop shadows, gradients, glows, or any depth effect. Parallax is flat. Depth comes from tonal contrast and negative space, not light simulation.
- **Don't** use the violet for body copy on warm white. The contrast ratio (4.4:1) only passes AA for large/bold text. Reserve violet for the wordmark, primary CTAs, edition numbers, and divider rules.
- **Don't** use the subscribe button text below 14px Bold. The button's violet background + warm-white text combo is 3.71:1 — passes WCAG AA only when text qualifies as large (≥14pt regular / ≥18pt by weight metric) or bold (≥14pt bold). The `button-text` typography token is locked at 14px weight 700 specifically to clear this threshold. Lint will warn on this pair; the warning is the documented exception, not a bug.
- **Don't** use the avatar's violet "P" at any size below ~48px. The 4.05:1 violet-on-ink ratio passes AA for large text (3:1 threshold) but fails for small text. The default 144px letter clears this comfortably; smaller usage requires increasing contrast (use warm-white instead of violet at sub-48px sizes).
- **Don't** use more than two type weights on a single composition. The system uses 700 (Space Grotesk Bold) and 400 (Source Serif Regular, JetBrains Mono Regular). That's it. Adding 500 or 600 is sprawl.
- **Don't** describe parallax visually. The word already carries the concept. The visual identity doesn't need to re-explain it via layered planes, refraction, or prism imagery. The 3% offset (one violet letter) is the visual concept; everything else is restraint.
- **Don't** add visual elements to make a piece "feel finished" if the typography already feels finished. Negative space is the finish. The confidence of an empty room.
- **Don't** use AI-generated faces or human imagery anywhere. The author's photograph (when added) must be a real headshot. See `photography-direction.md`.
- **Don't** ship without the wordmark. Every public-facing asset carries the wordmark — even small. The brand recognition compounds through repetition of one specific artifact.
