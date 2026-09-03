# Template: kicker-stack-body

source_ref: ../../../visual_refs/ref-02-premium-minimal-carousel.png
canvas: 1080x1350 (4:5 LinkedIn carousel)
strategy: html-overlay
role: body

## Rationale

see rationale.md — form: solid-css · edit_mode: none (pure CSS/HTML, no AI generation)

## Inventory

```yaml
ignore_screenshot_chrome: []

bg_treatment:
  kind: solid-color
  has_baked_overlays: false
  needs_clean_ref: false
  cleaned_bg_path: null

requires_photo_zone: false
photo_zones: []

elements:
  - name: masthead-left
    bbox: [7.8, 6, 40, 3]
    type: text
    content: "FARRICE CAIN"
    decision: slot
    notes: "brand functional masthead label, moves.md #1; graphite, tracked uppercase"

  - name: field-index
    bbox: [55, 6, 37, 3]
    type: text
    content: "02 / 04"
    decision: slot
    notes: "brand field-index chrome move, moves.md #2; per-post variation axis (slide position in sequence)"

  - name: hairline-rule-1
    bbox: [7.8, 10.5, 84.4, 0.2]
    type: rule
    content: null
    decision: skip
    reason: "structural decision-line move (moves.md #3), a 1px CSS border, not slot-editable content"

  - name: kicker-1
    bbox: [7.8, 17.5, 84.4, 3]
    type: text
    content: "SO THE TEAM ASKS FOR"
    decision: slot
    notes: "caption-scale tracked uppercase label introducing the headline stack"

  - name: headline-stack
    bbox: [7.8, 24, 84.4, 30]
    type: text
    content: "More UGC.<br>More statics.<br>Another creator."
    decision: slot
    notes: "the slide's one dominant idea; brand display face, bold, ink, sentence case, tight leading"

  - name: hairline-rule-2
    bbox: [7.8, 68.5, 84.4, 0.2]
    type: rule
    content: null
    decision: skip
    reason: "structural decision-line move (moves.md #3), a 1px CSS border, not slot-editable content"

  - name: kicker-2
    bbox: [7.8, 73, 84.4, 3]
    type: text
    content: "WHAT STAYED THE SAME"
    decision: slot
    notes: "caption-scale tracked uppercase label introducing the closing statement"

  - name: statement
    bbox: [7.8, 78, 84.4, 6]
    type: text
    content: "The familiar category claim."
    decision: slot
    notes: "regular-weight subtitle-scale line, graphite; deliberate contrast to the bold headline above"

chrome_observed:
  masthead_visible_in_ref: true
  pagination_dots_visible_in_ref: false
  page_indicator_visible_in_ref: true
```

## Visual summary

A pure-typography body slide on the brand's flat canvas fill — no photography, no texture, no AI generation.
The functional masthead (identity label left, field index right) sits above a hairline rule; below it, a
tracked kicker introduces a bold 3-line escalating headline stack (the slide's one dominant idea, in the
brand's only display face at full ink weight). A second hairline rule separates that block from a closing
kicker + a single regular-weight, graphite statement line — the deliberate typographic contrast between
"what's escalating" (bold, black, stacked) and "what stayed the same" (calm, gray, single line). Use this
template for any body slide in a carousel series that makes a before/after or escalation/constant argument
in pure type.

## AI Image

```
generation_route: none
ref_input: none
```

No `[ai-image-zone]` block — `edit_mode: none` per `rationale.md` §③. The background is
`background: var(--brand-bg-light);` CSS only.

## Slots

- **MASTHEAD_LEFT** — brand identity label (top-left masthead)
  - bbox: 7.8% 6% 40% 3%
  - style: caption token, 2.0cqw, uppercase, +0.16em tracking, weight 700, `var(--brand-secondary)`
  - sample: "FARRICE CAIN"

- **FIELD_INDEX** — field-index page position (top-right)
  - bbox: 55% 6% 37% 3%, right-aligned
  - style: caption token, 2.0cqw, uppercase, +0.16em tracking, weight 700, `var(--brand-secondary)`
  - sample: "02 / 04"
  - user_editable: true

- **KICKER_1** — small tracked label introducing the headline
  - bbox: 7.8% 17.5% 84.4% 3%
  - style: caption token, 2.0cqw, uppercase, +0.16em tracking, weight 700, `var(--brand-secondary)`
  - sample: "So the team asks for"

- **HEADLINE** — the dominant 2–4 line escalating display stack (HTML-bearing: supports `<br>`)
  - bbox: 7.8% 25% 84.4% 42%
  - style: brand display face, 11.3cqw, weight 700, line-height 1.05, letter-spacing -0.025em,
    `var(--brand-text-on-light)`, sentence case, left-align
  - sample: "More UGC.<br>More statics.<br>Another creator."

- **KICKER_2** — small tracked label introducing the closing statement
  - bbox: 7.8% 73% 84.4% 3%
  - style: caption token, 2.0cqw, uppercase, +0.16em tracking, weight 700, `var(--brand-secondary)`
  - sample: "What stayed the same"

- **STATEMENT** — the closing single-line statement (HTML-bearing: supports `<mark>`/`<em>`/`<strong>`)
  - bbox: 7.8% 78% 84.4% 6%
  - style: subtitle token, 3.3cqw, weight 400, line-height 1.3, letter-spacing -0.01em,
    `var(--brand-secondary)`, sentence case, left-align
  - sample: "The familiar category claim."

## Fixed elements (not slot-editable)

- The `#F3F3F0` canvas fill — CSS `background: var(--brand-bg-light);`, never a slot.
- The two hairline rules (moves.md decision-line move) — CSS `border-top: 1px solid var(--brand-text-on-light);
  opacity: 0.15;`, structural, not content.
- The masthead's 3-slot flex layout (left = identity, center = empty, right = field index) — the layout
  pattern is fixed; only the two slot VALUES (`MASTHEAD_LEFT`, `FIELD_INDEX`) are editable.

## Strategy notes

- All zones are html-overlay. No ai-edit needed — `edit_mode: none`.
- Chrome injected: masthead (3-slot flex, left + right populated, center empty) per
  `tokens.json → chrome.masthead.enabled: true` + this ref's evidence; field index per `tokens.json →
  chrome.field_index` + this ref's evidence. No pagination dots (`tokens.json → chrome.pagination: null`, and
  the ref shows a field index, not dots, in that role anyway).
- Bg is solid `var(--brand-bg-light)` via CSS — no `_ai_bg/bg.png` file for this template.

## Possible future variations

- Allow the headline stack to run 2 or 4 lines instead of the sampled 3 (the slot already supports `<br>`
  freely; the auto-shrink fit mechanic handles the extra/fewer lines).
- Allow `STATEMENT` to carry an `<mark>` accent word for a body variant that wants one emphasized term.
