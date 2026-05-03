---
description: BitBranding — Build SEO + brand storytelling layer for a clothing collection page (hero direction, top description, rich-text bottom description with interlinking, below-grid merchandising)
---

# /bb-collection-content — Collection Content & SEO Stack (BitBranding)

Read and execute `skills/bitbranding-fashion-shopify/workflows/04-collection-content-seo-stack.md`.

## Usage

```
/bb-collection-content [collection name] for [brand]
```

## Pre-Flight

Load `skills/bitbranding-fashion-shopify/genius.md` for content-layer patterns and SEO depth criteria.

**Roster stack note**: This workflow pairs with **Luke Iha** (product copy) and **Oren** (brand positioning). If brand voice/positioning isn't locked, flag — content needs voice + positioning input.

## Inputs Required

1. Collection focus (name + 1-2 line concept)
2. Brand positioning (1 paragraph — voice, customer, category)
3. Product list in this collection (titles + price points)
4. Other collections in the store (minimum 3, ideally 5+ for interlinking)
5. Hero image style preference (editorial / lifestyle / product-on-color / abstract / lookbook)
6. Theme (Horizon-specific levers default)

## Output

Hero image direction (specific enough to brief a photographer or feed into `/posters`). Top short description (≤160 chars, hooks at first 80, truncates cleanly). Bottom rich-text description (150-300 words, 3 paragraphs, 3+ inline collection interlinks). Below-grid merchandising (carousel + email CTA combo). SEO keyword audit with naturalness check. All implementation steps with exact Horizon lever paths + meta-field setup.

## Pairs With

- `Luke Iha` skill — write the bottom description in voice if Christian's defaults don't fit
- `Oren` agent — lock brand positioning before running this workflow
- `fantastic-posters` skill — generate the hero image from the direction spec
- `/bb-audit` + `/bb-rebuild` — content layer is Step 5-9 of the rebuild
