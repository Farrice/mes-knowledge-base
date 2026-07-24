---
description: Scrape a brand's site into a structured asset sheet (colors, type, logos, voice) — Riley Brown Firecrawl pattern via Tavily + Playwright at $0
---

# /brand-asset-scrape — Site → Brand Asset Sheet

Riley Brown's Firecrawl move — "scrape a website in full, get all the assets" — replicated on infrastructure we already own: Tavily (crawl/extract) + Playwright (screenshots) instead of a Firecrawl subscription. Output feeds DESIGN.md work and `/creative-from-winners`.

**Lineage**: `skills/riley-brown-marketing-automation/` · pairs with `/design-md-extract` (which formalizes findings into a Google-Labs-v2 DESIGN.md).

## Usage

```
/brand-asset-scrape [domain] [--client name] [--depth pages|site]
```

## Steps

### 1. Crawl (Tavily, $0 floor)

- Single page: `tavily-extract` skill on the landing page
- Full site: `tavily-map` → pick brand-bearing pages (home, about, product, pricing) → `tavily-extract` each
- JS-heavy/blocked pages → Playwright fallback (`browser_navigate` + `browser_evaluate`), Tier 1 read-only per `directives/browser-automation-safety.md`

### 2. Visual capture (Playwright)

`browser_take_screenshot` on each brand-bearing page (full-page). Read screenshots to extract what HTML can't say: actual rendered type hierarchy, spacing feel, imagery style, photography vs illustration.

### 3. Asset harvest

From page source + screenshots, collect into `deliverables/[client]/brand-assets/` (or `.tmp/` for exploratory runs):

- **Logos**: logo/wordmark/favicon URLs (og:image, link rel=icon, header img)
- **Colors**: hex values from CSS custom properties + computed styles (`browser_evaluate`: getComputedStyle on header/buttons/body) — label primary/secondary/accent/background
- **Type**: font-family stacks per role (display/body/mono), weights in use
- **Voice**: 5-10 verbatim copy samples (hero, CTAs, product descriptions) — the verbal identity
- **Layout patterns**: grid, section rhythm, CTA placement

### 4. Ship the sheet

One markdown asset sheet (`BRAND-ASSETS.md`): every asset with its source URL, colors as swatches table, voice samples quoted. ≤2 pages (density > completeness).

### 5. Optional formalization

- `/design-md-extract` → full DESIGN.md spec from the sheet
- `brand-system-builder` agent → complete brand system if this is a client engagement

## Cost

$0 — Tavily floor + local Playwright. No Firecrawl. If a site hard-blocks automation, note it and fall back to manual screenshot + `Read`.

## Quality Gate

- Every color/font claim traceable to a URL or screenshot (no "probably uses")
- Voice samples verbatim, never paraphrased
- No login-gated scraping without the browser-safety confirmation flow
