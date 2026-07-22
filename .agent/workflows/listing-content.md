---
description: Generate expert-powered viral video hooks for Jen's listings
---

# /listing-content

> Jen Santulan's expert-powered viral hook engine — 6 video hooks per property, two-pass architecture (expert mechanics → Jen voice polish).

## Quick Deploy

```
Load: skills/jen-santulan-listing-content/genius.md
Execute: skills/jen-santulan-listing-content/workflows/01-listing-content.md
```

## Usage

```
/listing-content [property address or Zillow/Redfin URL]
```

## When to Use

- New listing just hit the market — need 6 hook variants for Reels
- Property is FTHB-eligible (under $1M, SFV/SoCal, near amenities)
- Jen wants to test multiple angles before committing camera time

## Output

6 video hooks (80-120 words each), each engineered for one viral mechanic:
1. Scrollstop Discovery
2. First-Time Buyer Permission (mandatory — Jen's niche move)
3. Lifestyle Transformation
4. Smart Money
5. Scarcity / Urgency
6. Complete Package

Plus: Expert Analysis Pass + Performance Enhancement Notes.

## Related Workflows

- `/buyer-education-story` — FTHB-focused educational Stories (skill workflow 02)
- `/neighborhood-deep-dive` — SFV neighborhood carousels (skill workflow 03)
- **Listing posters (batch)** — `skills/fantastic-posters/templates/listing-batch.json`. Edit listings array, run `node generate.js --batch=...`. Native `luxury-real-estate` + `luxury-estate-cover` styles. Per-listing cost: $0.17 high quality. **Always pre-flight via `python3 execution/fal_budget_guard.py check --quality=high --n=<chunk_size>`** — guard enforces $1/call ceiling, so split 10+ listing batches into chunks of 5.

Full spec: `skills/jen-santulan-listing-content/workflows/01-listing-content.md`

**Execution prompts**: before producing the deliverable, check `skills/jen-santulan-listing-content/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
