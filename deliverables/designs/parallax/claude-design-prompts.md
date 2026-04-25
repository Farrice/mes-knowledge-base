# Parallax — Claude Design Prompts

Typography-only identity system. Deep Ink `#1C1C1E`, Warm White `#F5F0EB`, single accent Parallax Violet `#7B61FF` (the second L in PARALLAX — nothing else). Space Grotesk Bold for display, Source Serif 4 Italic for editorial flourishes, JetBrains Mono for watermark metadata. Negative space carries the weight. The aesthetic target is an Apple keynote slide lit by an A24 title card: quiet, absolute, still. Every pixel is intentional; nothing decorates.

---

## 1. PARALLAX Wordmark (1344x256, transparent PNG)

```
Design a horizontal wordmark lockup on a fully transparent background.

Canvas: 1344px wide x 256px tall. Transparent (alpha) — no fill.

Typography:
- Single line of text: PARALLAX (all caps, 8 letters).
- Typeface: Space Grotesk Bold.
- Type size: 140px cap height.
- Letter-spacing: +20 (tracking ~14% of em).
- Baseline: optically centered vertically on canvas (expect ~58px top padding, ~58px bottom to cap height).
- Horizontal alignment: optically centered in canvas — let the natural letter widths sit inside ~90px margins left and right.

Color:
- Letters P, A, R, A, L, A, X: Warm White #F5F0EB.
- The SECOND L only (7th character, between the second A and the final A): Parallax Violet #7B61FF. Same weight, same size, same baseline — the color is the only difference.

Composition rules:
- No background shape. No container. No frame. No rule. No underline.
- No shadow, glow, outline, bevel, gradient, or texture anywhere.
- Do not render the tagline. Do not render a subtitle. Do not render a symbol or icon.
- The wordmark sits alone in space.

Emotional direction: This is a film title card mid-fade — the exact frame where the word has arrived and nothing else has happened yet. Denis Villeneuve opening credit. Absolute stillness. The violet letter is the only moment of tension on the page; the rest is certainty.

Export: PNG, 1344x256, transparent background, RGB color space, 1x (no retina upscale).

Forbidden: gradients, textures, photographs, illustrations, AI-generated imagery, decorative elements, secondary accent colors, all-caps serif, any mention of the word "minimalist" anywhere on the asset.
```

---

## 2. Favicon (512x512, PNG)

```
Design a single-letter brand mark on a solid dark square.

Canvas: 512px x 512px. Background: solid fill #1C1C1E edge to edge. No rounding of corners — perfect square.

Typography:
- Single character: P (uppercase).
- Typeface: Space Grotesk Bold.
- Type size: 360px cap height (~70% of canvas height).
- Color: Parallax Violet #7B61FF.
- Alignment: optically centered on canvas — the P's visual center (accounting for the bowl weighting the top-right) sits on the 256/256 intersection. Expect a very slight upward nudge (~6-10px) so the optical center, not the geometric center, lands on the middle.

Composition rules:
- Nothing else on the canvas. No second letter. No full wordmark. No tagline. No rule. No frame.
- No shadow, glow, outline, bevel, gradient, texture, or halo around the P.
- The background must stay perfectly flat #1C1C1E — no vignette, no noise, no gradient.

Emotional direction: Aesop bottle cap stamped into dark glass. One confident letter. Readable at 16px browser tab size because the contrast is absolute and the form is pure.

Export: PNG, 512x512, opaque (not transparent), sRGB.

Forbidden: gradients, textures, photos, illustrations, AI imagery, decorative elements, multiple accent colors, rounded corners, serif letterforms, the word "minimalist" anywhere.
```

---

## 3. Substack Cover Photo (1200x1200, PNG)

```
Design a square Substack publication cover with the wordmark and tagline anchored in the upper 40%, the lower half left intentionally empty.

Canvas: 1200px x 1200px. Background: solid fill #1C1C1E.

Vertical layout (top to bottom):
- 0 to 360px: negative space (top margin).
- 360 to 480px: PARALLAX wordmark, horizontally centered.
- 480 to 540px: negative space (60px gutter).
- 540 to 545px: a single horizontal rule, 5px tall, 120px wide, centered. Color: Parallax Violet #7B61FF. Nothing else on this line.
- 545 to 605px: negative space (60px gutter).
- 605 to 680px: tagline, horizontally centered.
- 680 to 1200px: negative space. Completely empty. No mark. No watermark. No page number.

Typography:
- Wordmark: "PARALLAX" — Space Grotesk Bold, 96px cap height, letter-spacing +20, Warm White #F5F0EB, with the SECOND L in Parallax Violet #7B61FF. Everything else in Warm White.
- Tagline: "For people who see everything from more than one angle." — Source Serif 4 Italic, 36px, Warm White #F5F0EB, single line (if the line breaks naturally, center both lines and reduce to 32px; do not hyphenate).

Composition rules:
- Everything anchored in the upper 40% of the canvas except the rule, which sits at the optical midpoint of the cluster.
- Bottom 520px is pure empty #1C1C1E. Resist the instinct to fill it.
- No frame, no corner marks, no publication date, no author credit on the asset.

Emotional direction: The closing beat of a Kinfolk feature spread. Editorial gravity. The emptiness below is not unfinished — it is the point. The reader's eye falls through the open space the way it falls through a clear morning sky.

Export: PNG, 1200x1200, opaque, sRGB.

Forbidden: gradients, textures, photography, illustration, AI imagery, decorative elements, multiple accent colors, all-caps serif, the tagline rendered in anything other than italic, the word "minimalist" on the asset.
```

---

## 4. Email Header Banner (1100x300, PNG)

```
Design a wide email header banner with the wordmark anchored hard left and the remaining canvas held as pure negative space.

Canvas: 1100px x 300px. Background: solid fill #1C1C1E.

Layout:
- Left padding: 48px.
- Right padding: flexible (the wordmark ends wherever it ends; everything to the right of it is empty).
- Vertical: wordmark optically centered on the 150px midline.

Typography:
- Single line: "PARALLAX" — Space Grotesk Bold, 48px cap height, letter-spacing +20.
- Color: Warm White #F5F0EB for all letters except the SECOND L, which is Parallax Violet #7B61FF.
- Left edge of the P sits exactly 48px from the canvas left edge.

Composition rules:
- No tagline. No rule. No date. No issue number. No icon. No author avatar. No social handles.
- The right 70% of the canvas is empty #1C1C1E. Do not fill it with anything — not a dot, not a gradient, not a watermark.

Emotional direction: The letterhead on a note slid under a hotel door at 6am. Quiet arrival. The reader opens the email and the brand is simply there, in its corner, saying one word.

Export: PNG, 1100x300, opaque, sRGB.

Forbidden: gradients, textures, photos, illustrations, AI imagery, decorative elements, multiple accent colors, the word "minimalist" anywhere.
```

---

## 5. Social Preview / OG Image (1200x630, PNG)

```
Design a social preview card optimized for link unfurls on X, LinkedIn, and iMessage — wordmark and tagline anchored at 40% from the top, everything below left empty.

Canvas: 1200px x 630px. Background: solid fill #1C1C1E.

Vertical layout (top to bottom):
- 0 to 180px: negative space.
- 180 to 252px: PARALLAX wordmark, horizontally centered.
- 252 to 292px: negative space (40px gutter).
- 292 to 295px: single horizontal rule, 3px tall, 96px wide, centered, Parallax Violet #7B61FF.
- 295 to 335px: negative space (40px gutter).
- 335 to 385px: tagline, horizontally centered.
- 385 to 630px: negative space. Empty.

Typography:
- Wordmark: "PARALLAX" — Space Grotesk Bold, 72px cap height, letter-spacing +20, Warm White #F5F0EB with the SECOND L in Parallax Violet #7B61FF.
- Tagline: "For people who see everything from more than one angle." — Source Serif 4 Italic, 28px, Warm White #F5F0EB, single line, centered. Do not break, do not hyphenate; shrink to 26px if it does not fit single-line.

Composition rules:
- All elements live in the upper 61% of the canvas (the fold that survives aggressive platform cropping).
- Bottom 245px is empty #1C1C1E — this is intentional breathing room that reads as confidence when the card is rendered at thumbnail size on a mobile feed.
- No URL. No author name. No date. No "new edition" stamp. No logo mark.

Emotional direction: A gallery wall label at MoMA — the work is not on this card; the card only names what you are about to look at. Restrained, authoritative, slightly cold.

Export: PNG, 1200x630, opaque, sRGB.

Forbidden: gradients, textures, photos, illustrations, AI imagery, decorative elements, multiple accent colors, all-caps serif, the word "minimalist" anywhere.
```

---

## 6. LinkedIn Profile Banner (1200x400, PNG)

```
Design a LinkedIn profile banner with a faint monospaced word list watermark on the left and a crisp wordmark on the right.

Canvas: 1200px x 400px. Background: solid fill #1C1C1E.

LEFT ZONE (0 to 720px, the watermark column):
- Render a vertical list of single words, one per line, in JetBrains Mono Regular, 28px, Warm White #F5F0EB at 40% opacity (i.e., rgba(245, 240, 235, 0.40)).
- Words (in this exact order, one per line):
    psychology
    AI systems
    fatherhood
    anime
    spirituality
    strategy
- Line-height: 1.6 (so lines sit ~45px apart).
- Left padding: 64px. Top padding: calculate so the 6-line block is vertically centered on the 200px midline of the canvas (expect the block to be ~270px tall; top padding ~65px).
- Letters are lowercase as written above, with the exception of "AI" which stays capitalized. No bullets, no dashes, no numerals, no punctuation, no hover state — just the list.
- Safe zone note: LinkedIn crops ~60px from top and bottom on mobile; keep the word list within the middle 280px vertical band.

RIGHT ZONE (720 to 1200px, the wordmark column):
- "PARALLAX" — Space Grotesk Bold, 64px cap height, letter-spacing +20, Warm White #F5F0EB with the SECOND L in Parallax Violet #7B61FF at 100% opacity (full strength — this is the sharp element).
- Right-aligned: the final X sits 64px from the right edge of the canvas.
- Vertically centered on the 200px midline.

Composition rules:
- The two zones read at different weights: the watermark is whispered (40%), the wordmark is spoken (100%). The contrast in opacity is the composition.
- No rule between zones. No divider. No background panel behind either element.
- No icons, no social handles, no tagline on this asset.

Emotional direction: A library card catalog drawer — the faint list of topics the person has spent their life inside, and then the proper name of the publication stamped sharp on the right. Interior life on the left, public name on the right.

Export: PNG, 1200x400, opaque, sRGB.

Forbidden: gradients, textures, photos, illustrations, AI imagery, decorative elements, multiple accent colors, the word "minimalist" anywhere, bullets or punctuation in the word list.
```

---

## 7. New Edition Announcement Card (1080x1350, PNG)

```
Design a vertical announcement card for Substack Notes and Instagram — wordmark at top, giant violet edition numeral dominating the center, serif italic edition title below, then empty lower third.

Canvas: 1080px x 1350px (4:5 vertical). Background: solid fill #1C1C1E.

Vertical layout (top to bottom):
- 0 to 80px: negative space (top margin).
- 80 to 120px: PARALLAX wordmark, horizontally centered. Space Grotesk Bold, 40px cap height, letter-spacing +20, Warm White #F5F0EB with the SECOND L in Parallax Violet #7B61FF.
- 120 to 380px: negative space (deep gutter — 260px of empty canvas is the point).
- 380 to 780px: the edition numeral. Two digits, rendered in Space Grotesk Bold, 400px cap height, Parallax Violet #7B61FF, horizontally centered. Placeholder numerals: "01". (For production: swap to 02, 03, 04, etc.) Letter-spacing: 0 (tight). The numeral dominates the composition — it is the largest visual element on the card.
- 780 to 840px: negative space (60px gutter).
- 840 to 843px: single horizontal rule, 3px tall, 80px wide, centered, Warm White #F5F0EB at 100%.
- 843 to 900px: negative space (57px gutter).
- 900 to 960px: edition title, rendered in Source Serif 4 Italic, 42px, Warm White #F5F0EB, horizontally centered. Placeholder title: "The Articulation Gap" (swap per edition; keep under 32 characters).
- 960 to 1350px: negative space. Empty. No date. No byline. No CTA. No "read now" button.

Composition rules:
- Three distinct zones, each separated by deliberate empty space: brand mark (top), edition number (center, massive, violet), title (below center, small, serif italic).
- The 390px of empty canvas at the bottom is intentional — it lets the card breathe on a vertical feed and gives Instagram's caption area visual rest.
- No decorative numbers around the edition numeral. No "issue" label. No Roman numerals. No serial number framing. The numeral stands alone.

Emotional direction: A Criterion Collection spine label crossed with a Rick Owens lookbook divider. The numeral is the moment — everything else is the frame that lets the numeral hit.

Export: PNG, 1080x1350, opaque, sRGB.

Forbidden: gradients, textures, photos, illustrations, AI imagery, decorative elements, multiple accent colors, all-caps serif, "Issue" or "Vol." prefixes on the numeral, the word "minimalist" anywhere.
```

---

## Canva Handoff (Claude Design → Canva Magic Layer)

Claude Design outputs flat PNGs. Canva is where you iterate the micro-adjustments (cropping, placement tweaks, versioning numerals across editions, exporting platform variants).

**Workflow:**

1. **Export from Claude Design** — save each PNG at the exact dimension specified above. Keep filenames descriptive: `parallax-wordmark-1344x256.png`, `parallax-og-1200x630.png`, etc.
2. **Open Canva** — create a new design at the matching canvas size (Custom size → enter the dimensions). Do NOT start from a Canva template — you want a blank canvas so no template defaults contaminate the layout.
3. **Import** — drag the PNG onto the blank canvas, or use `Uploads → Upload files`. Size it to fill the canvas at 100%.
4. **Magic Edit / Magic Layer** — select the PNG, click `Edit image → Magic Edit`. Use it only for:
    - Nudging the violet letter if it reads off-position at final size.
    - Color-matching the violet against a monitor reference if it drifts warm or cool.
    - Swapping the edition numeral on the announcement card (prompt: "replace the numerals 01 with 02, keep all other elements identical, keep the color #7B61FF").
5. **Version out** — duplicate the Canva design per edition/platform, swap the one variable (numeral, tagline crop), export as PNG at 1x. Name files `parallax-edition-02-1080x1350.png`, etc.
6. **Do not** run Canva's built-in filters, effects, or "enhance" passes on these assets. The aesthetic is flat on purpose; any Canva polish will break it.

Canva's role here is a versioning and handoff tool, not a design tool. The design is locked in Claude Design. Canva is where it ships.

---

## Prompt Engineering Notes

A brief on why these prompts are built this way. Useful for calibrating your creative-direction muscle on the next asset system you commission.

**1. Dimensions before description.** Every prompt opens with canvas size and background fill. A design-capable model allocates its attention budget to whatever you mention first; front-loading geometry forces the model to solve the spatial problem before it gets seduced by style words. If you open with "minimal, premium, editorial," the model generates to those moods and then crams your specs in afterward. Reverse the order.

**2. Pixel ranges, not percentages.** "Upper 40%" is vague to a model; "0 to 360px: negative space. 360 to 480px: wordmark." is a contract. Ranges remove interpretation. A good prompt reads like a layout grid, not a brief.

**3. Name the negative space as a layer.** Every prompt lists empty regions as explicit vertical bands with their own coordinates. Models treat unnamed emptiness as a problem to solve (they fill it). Naming it — "605 to 1200px: completely empty, no mark, no watermark, no page number" — converts emptiness into a deliberate element the model has to preserve.

**4. The forbidden list is half the prompt.** "Do not add a gradient" is more protective than "make it flat." Design-capable models have strong priors toward decoration, ambient glow, and safe "premium" gestures (subtle shadows, faint textures, soft vignettes). The `Forbidden:` block names each specific failure mode so the model's instinct to add polish gets blocked at its exact location.

**5. Emotional direction goes last, not first.** The mood line ("Denis Villeneuve opening credit. Absolute stillness.") sits near the end of each prompt on purpose. Open with mood and the model anchors on aesthetic; open with geometry and close with mood and the model uses the mood as a tiebreaker for micro-decisions within a locked structure. Mood is the finish, not the foundation.

**6. One accent, named by position.** "Parallax Violet #7B61FF on the second L" is enforceable; "a single accent color, used sparingly" is not. Every accent instruction names the specific character, line, rule, or numeral that carries it. Models don't deviate from positional specificity the way they deviate from frequency-based rules.

**7. Typography specified as cap height, not font size.** "140px cap height" gives the model a measurable target on the canvas. "Font size 140" is ambiguous — it's the point size of the typeface metadata, which doesn't map cleanly to rendered pixels across weights. Cap height is what the human eye measures; specify what the eye measures.

**8. Optical centering vs. geometric centering.** The P in the favicon sits optically centered (~6-10px nudge upward), not geometrically centered. Calling this out in the prompt protects the asset from a mathematically centered P that reads visually low. Any time a letterform or numeral is the sole element on a canvas, specify optical centering or the asset will look subtly wrong for reasons the viewer can't articulate.

**9. The asset forbids its own category label.** "Do not render the word 'minimalist' on the asset" is not a joke — design-capable models have been trained on stock output where the aesthetic word appears as decoration inside the aesthetic. Bar the word and the asset can't collapse into a meta-joke about itself.

**10. Every prompt is self-contained.** Claude Design opens without memory. Each prompt re-specifies palette, typography, signature move (the violet L), and forbidden elements. This is not redundancy — it's insurance against drift. A prompt that references "the palette we established" will work in one session and fail in the next.

The meta-principle: a great creative-direction prompt is closer to a CAD file than a poem. The poetry is in the emotional-direction line. The rest is a contract the model cannot misread.
