# Farrice Cain — Design Moves (Premium Minimal)

Brand-specific moves that implement the ten universal principles in `references/design-principles.md`. Imported 2026-09-02 from the Premium Minimal design contract (components, rules, grid and spatial law). The `ssc-designer` audit passes when at least two moves from this catalog appear on every content slide. Universal baselines (type floors, 30–65% whitespace, two z-index levels) still apply underneath.

## 1. Functional masthead

<!--meta
name: functional-masthead
image_bearing: false
keywords: [masthead, label, chrome, identity]
-->

**What it is:** a small uppercase identity label at the top-left edge, Helvetica Neue 700, 22px, +0.16em tracking, graphite. Master-brand mode reads `FARRICE CAIN`; offer mode reads `THE ANGLE MAP` with `FARRICE CAIN` as author.

**Why:** it is the brand's signature and its only logo. It signals a series without decorating. Implements principle 6 (repetition) and principle 7 (alignment).

**Where the value lives:** `tokens.json → chrome.masthead.labels`.

**When it breaks:** never turn it into a lockup, wordmark art, or a badge. It is a label, not a logo.

## 2. Field index

<!--meta
name: field-index
image_bearing: false
keywords: [index, numeral, page, pagination]
-->

**What it is:** a two-digit index (`FIELD / 01`, `NOTE / 02`, or plain `02`) in place of carousel dots. Large scale in stone, label scale in graphite.

**Why:** orients the reader inside a sequence the way a field guide does. Implements principle 6 (repetition) and principle 8 (proximity): one predictable corner, every page.

**Visual recipe:** label scale = caption token (22px, uppercase, +0.16em); large scale = display token in `stone` (#8C8C82) at up to 30% of canvas height, never competing with the headline.

**When NOT to use:** single-image posts with no sequence; the index reads as a mistake on a one-off.

## 3. Decision line

<!--meta
name: decision-line
image_bearing: false
keywords: [rule, hairline, structure, hierarchy]
-->

**What it is:** a thin horizontal rule that establishes structure. Hairline (1px) or structural (2px) in `line` (#D8D8D3); it becomes heavier (6px, ink) only when it underlines the recommendation.

**Why:** structure through rules and whitespace before containers. Implements principle 7 (alignment) and principle 9 (one bold move): the heavy weight is reserved for the decision.

**When it breaks:** more than one heavy rule per surface, or heavy rules where nothing is being decided.

## 4. Three-route grammar

<!--meta
name: three-route-grammar
image_bearing: false
keywords: [routes, comparison, angles, recommendation]
-->

**What it is:** three parallel strokes differentiated by number, position, and weight. The recommended route runs 6px in ink; quiet routes run 1–2px in line. Never colored.

**Why:** it is the visual form of the Angle Map: three campaign arguments, one recommendation. Implements principle 2 (hierarchy) and principle 9 (one bold move).

**When NOT to use:** any surface that is not genuinely comparing choices. Route lines as decoration are prohibited.

## 5. Proof boundary

<!--meta
name: proof-boundary
image_bearing: false
keywords: [proof, evidence, claim, boundary, ledger]
-->

**What it is:** two or three aligned fields separated by hairline rules: supported · qualified review · outside supplied proof. Labels in caption tokens; no warning colors, shields, checks, or badges.

**Why:** shows where a claim comes from and what it can carry, without compliance theater. Implements principle 1 (clarity) and principle 5 (contrast through structure, not color).

**When it breaks:** if it starts to look like a compliance department, an academic paper, or a dashboard. Proof detail belongs one click deeper than the decision.

## 6. Dark recommendation

<!--meta
name: dark-recommendation
image_bearing: false
keywords: [recommendation, dark, inversion, decision, bold]
-->

**What it is:** an ink (#101010) field with paper (#FAFAF8) text, reserved for the consequential decision. Maximum one per sequence.

**Why:** this is the system's only bold move, in place of an accent color. Implements principle 9 (one bold move per slide) and principle 5 (contrast).

**Visual recipe:** full-bleed or bounded ink field; headline in display token, sentence case; supporting line in body token at paper; no other element competes.

**When NOT to use:** general drama, hooks, or covers that are not the decision. `rules.maximum_dark_interruptions_per_sequence` = 1.

## 7. Open third

<!--meta
name: open-third
image_bearing: false
keywords: [whitespace, grid, restraint, thumbnail]
-->

**What it is:** at least one-third of every composition stays open on a twelve-column grid, maximum three hierarchy levels, one dominant idea per surface. Must survive the 320px thumbnail test.

**Why:** the restraint is the brand. Expensive because the thinking has been edited. Implements principle 3 (whitespace) and principle 2 (hierarchy).

**When it breaks:** containers, cards, or a second idea added to fill space. Use alignment, rules, and whitespace before containers, always.

## 8. Evidence crop (Performance Evidence Journal mode)

<!--meta
name: evidence-crop
image_bearing: true
required_zone_types: [photo-zone, annotation-overlay]
keywords: [evidence, screenshot, source, annotation, ledger, journal]
-->

**What it is:** a restrained crop of a real source (a label panel, a product page, a review, a study excerpt, a live AI answer) set inside a bounded ledger grid with a caption-token source label and an annotated margin note. Only owned brand artifacts and verified source excerpts qualify.

**Why:** the Health Performance buyer buys inspectable proof. Implements principle 4 (layering) and principle 1 (clarity): the crop is the evidence, the label says what it can carry.

**Visual recipe:** crop sits on `paper` inside hairline rules; source label in caption token, graphite; margin note in body token at 26–28px; no drop shadow, no frame chrome, no faux-lab styling. AI-generated imagery is not evidence and never fills this zone.

**When NOT to use:** the top-of-profile scan or a cover. Proof detail belongs one click deeper.

## 9. Original portrait

<!--meta
name: original-portrait
image_bearing: true
required_zone_types: [photo-zone]
keywords: [portrait, headshot, authority, human]
-->

**What it is:** Farrice's original, unaltered portrait (natural black wardrobe, warm real environment, direct unforced eye contact) placed as an occasional authority or story device.

**Why:** a real operator with taste is accountable for the decision. Implements principle 4 (layering) and principle 10 (human signal). Portrait energy must never outrun the offer: the decision still wins the first scan.

**Visual recipe:** crop and uniform scale only; sits inside the grid on canvas or paper; no beauty edits, synthetic generation, creator-lifestyle props, or AI upscaling.

**When NOT to use:** every asset. It is occasional by policy.

## Universal hardcoded constants (apply regardless of brand)

- Type sizes never go below the floor in `references/output-formats.md` (display ≥90px, h1 ≥68px, body ≥28px for LinkedIn carousel).
- Whitespace stays between 33% and 65% of the canvas (this brand's floor is the higher one).
- Every slide has at least two z-index levels; masthead plus field index count as the second layer on pure-typographic slides.

## 10. Script signature (editorial style, added 2026-09-03)

<!--meta
name: script-signature
image_bearing: false
keywords: [signature, script, cover, close, author]
-->

**What it is:** the author signature "Farrice Cain" in a script face (placeholder: Mrs Saint Delafield until his real handwriting lands in `visual-identity/logos/signature.svg`), overlaid across the giant lowercase display word on the cover and the close frame only. Colour: `colors.signature_accent` (#FF2D2D), the single unlocked accent.

**Why:** the one human, hand-made mark on an otherwise edited system; it says a person is accountable for the teardown. Implements principle 10 (human signal) and principle 9 (one bold move) without a second dark frame.

**When it breaks:** anywhere but cover/close; any size that competes with the display word; any other element in red.
