---
category: Structure
---

# Surface

The root wrapper. Every Premium Minimal composition sits inside one.

Surface carries the type family, the canvas colour, the contract's safe margins, and the container context the type scale reads. Place a component outside a Surface and it renders unstyled at the wrong size.

## Sizes

| `size` | Canvas | Safe margin |
|---|---|---|
| `banner` | 1584 × 396 | 48px |
| `cover` | 1920 × 1080 | 120px |
| `feed` | 1080 × 1350 | 84px sides, 96 top, 108 bottom |
| `carousel` | 1080 × 1350 | same as feed; every page identical |
| `field-guide` | 16:9 | 5.4% |
| `free` | unsized | 48px |

Use `free` for web layout. Use a named size when producing an actual asset — the padding is a percentage of width, so the declared margins hold at any render scale.

## Tone

`canvas` is the default field. `paper` is a lifted or alternate page. `ink` is the dark interruption — **one per sequence, maximum**.

```jsx
<Surface size="feed">
  <Masthead mode="master-brand" />
  <Display level={1}>Most supplement brands buy attention they already had.</Display>
  <DecisionLine weight="structural" />
</Surface>
```
