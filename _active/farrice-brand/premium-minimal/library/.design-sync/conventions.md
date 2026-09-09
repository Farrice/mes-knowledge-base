# Farrice Cain Premium Minimal — how to build with this system

Restrained. Contemporary. Decisive. Every choice must serve at least one of those three words. A choice that serves none gets removed. The work should feel expensive because the thinking was edited, not because the surface was decorated.

## Wrap everything in `Surface`

`Surface` is the root wrapper and it is not optional. It carries the type family, the canvas colour, the contract's safe margins, and the container context the type scale reads. **A component rendered outside a `Surface` comes out unstyled and at the wrong size.**

```jsx
<Surface size="feed">
  <Masthead mode="master-brand" />
  <div style={{ flex: 1 }} />
  <FieldIndex label="FIELD" index="01" />
  <Display level={1}>A new hook is not a new campaign angle.</Display>
  <DecisionLine weight="structural" />
  <Secondary>
    More creative can become a socially safer substitute for choosing one
    message direction.
  </Secondary>
</Surface>
```

`size`: `banner` (1584×396) · `cover` (1920×1080) · `feed` and `carousel` (1080×1350) · `field-guide` (16:9) · `free` (unsized, for web layout). `tone`: `canvas` (default) · `paper` (lifted page) · `ink` (dark).

## There is no utility-class vocabulary

This system styles through components and props — not class names. Do not invent `bg-*`, `text-*`, or `p-*` classes; nothing will resolve them.

For your own layout glue, use the CSS custom properties the stylesheet defines:

- Colour: `--fc-canvas` `--fc-paper` `--fc-ink` `--fc-graphite` `--fc-line` `--fc-stone` `--fc-white`
- Type: `--fc-font-sans` `--fc-tracking-display` (−0.025em) `--fc-tracking-label` (+0.16em)
- Space: `--fc-space-1` … `--fc-space-9` (12, 18, 24, 36, 48, 72, 84, 96, 120px)
- Rules: `--fc-rule-hairline` (1px) `--fc-rule-structural` (2px) `--fc-route-lead` (6px)

Every spacing value comes off that scale. Nothing is 20px.

## The spatial law — this is the part that makes it the brand

- **Twelve columns** on every surface. Use `Grid` and `Column`.
- **Keep at least one third of the composition open.** The empty space is the system, not room left over. If it looks full, it is wrong.
- **Maximum three hierarchy levels. One dominant idea per surface.** One level-1 `Display`, never two.
- **Use alignment, rules, and whitespace before containers.** Reach for `DecisionLine` before you reach for a box.
- **One dark interruption per sequence, maximum.** `tone="ink"` or `DarkRecommendation` — once. A deck where three panels go dark has taught the reader that dark means nothing.
- At **320px wide**, the dominant thought must still be understandable.

## Never produce these

Serif type. Italics. Gradients. Shadows. Rounded pills. Badges. Seals. Ornamental icons. Card-heavy layouts. Black-and-gold luxury theatre. Title-case or all-caps headlines — headlines are **sentence case**, always. Decorative route colours. Route lines when nothing is actually being compared. Warning colours, shields, or check marks on `ProofBoundary` — the honest boundary is the point, not compliance theatre.

Uppercase appears in exactly one place: `FunctionalLabel` and the masthead, at +0.16em tracking.

## Two modes

`Masthead mode="master-brand"` → `FARRICE CAIN` + the category descriptor. For point of view, lived observation, teardowns, frameworks.

`Masthead mode="offer"` → `THE ANGLE MAP`, authored by `FARRICE CAIN`. For three campaign arguments and one recommendation.

## Read the real files before styling

- `_ds/<folder>/styles.css` and its imports — the actual tokens and component CSS.
- `guidelines/design-contract.md` — the full approved contract, including the standard surface dimensions and safe margins.
- `guidelines/brand-foundation.md` — audience, authority posture, and voice invariants. Read it before writing any copy inside a design.
- Each component's `.prompt.md` — per-component usage and worked examples.

## Known deviation

Production assets ship in Helvetica Neue only. In the browser that is a Mac-only system font, so this bundle ships the contract's own fallback chain — Helvetica Neue, Helvetica, Arial, sans-serif. On non-Mac viewers type renders in Arial. This substitution is approved for screen work; it does not authorize any other font.
