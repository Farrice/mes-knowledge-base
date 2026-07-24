---
description: "Riley Brown's Firecrawl move — scrape a brand's site in full into a structured asset sheet (colors, type, logos, voice samples), replicated on Tavily + Playwright at $0. Feeds creative work and DESIGN.md."
---

# /riley-brand-scrape — Site → Brand Asset Sheet

Riley's move (Pattern 12, Exemplar 2 step 3): "use the firecrawl and I want you to go to chorus.com... scrape all of that whole page... take all the individual assets from the page and put that in a different frame." He improvised it live ("I'm making this up on the spot... we can just use firecrawl to scrape and put it on there"). His stack used Firecrawl; ours uses Tavily + Playwright at **$0**. Output grounds `/riley-template-steal-ads` and DESIGN.md work.

## Pre-Flight Gate

Load `genius.md` first. Proceed if:
- You have a brand domain to scrape.
- The intent is *grounding creative in real brand truth* (before generating anything).
- Read-only browsing is acceptable (no login-gated scraping without the browser-safety confirmation flow).

## Skill Acquisition

- `genius.md` — Pattern 12 (improvised multi-tool assembly), Exemplar 2
- Live infra: `.agent/workflows/brand-asset-scrape.md` (the full Tavily + Playwright procedure)
- Downstream: `/design-md-extract`, `brand-system-builder` agent

## Execution

Run `/brand-asset-scrape`:
1. **Crawl (Tavily, $0).** Single page → `tavily-extract`; full site → `tavily-map` → pick brand-bearing pages (home/about/product/pricing) → `tavily-extract` each. JS-heavy/blocked → Playwright fallback (Tier 1 read-only).
2. **Visual capture.** `browser_take_screenshot` full-page on each brand-bearing page — read what HTML can't say (rendered type hierarchy, spacing feel, imagery style).
3. **Asset harvest** into `deliverables/[client]/brand-assets/` (or `.tmp/` for exploration): logos/wordmark/favicon URLs; colors as hex from CSS custom props + computed styles (label primary/secondary/accent/bg); font stacks per role; 5–10 **verbatim** voice samples (hero, CTAs, product copy); layout patterns.
4. **Ship the sheet.** One `BRAND-ASSETS.md`: every asset with its source URL, colors as a swatches table, voice samples quoted. ≤2 pages (density > completeness).
5. **Optional formalization.** `/design-md-extract` → full DESIGN.md; `brand-system-builder` if it's a client engagement.

Riley's own board move — putting the scraped page "right next to" the ads to reskin — maps to feeding this sheet straight into `/riley-template-steal-ads`.

## Content Type Adaptations

| Brand type | Adaptation |
|---|---|
| SaaS/product | scrape pricing + product pages for the real value-prop voice |
| DTC/e-commerce | product photography style + lifestyle imagery patterns matter most |
| Personal/creator | headshots, tone samples, signature phrases |
| Client (supplement/performance) | feeds the $2,500 sprint lane — pair with `/riley-ad-spy` on their #1 competitor |

## Output Requirements

- A `BRAND-ASSETS.md` sheet, ≤2 pages, every claim traceable to a URL or screenshot.
- Colors as hex swatches; fonts per role; 5–10 verbatim voice samples.
- No "probably uses" — traceable or omitted.

Execution prompt: references/prompts-v2/brand-asset-sheet.md — honor its Output Contract.

## Quality Gate

Every color/font claim traceable to a source (no guessing)? · Voice samples verbatim, never paraphrased? · Sheet ≤2 pages? · No login-gated scraping without confirmation? · Ready to feed `/riley-template-steal-ads` or `/design-md-extract`?
