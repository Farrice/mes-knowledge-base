---
description: Turn a winning competitor ad into on-brand creative variants — Riley Brown template-steal pattern via our own creative stack (no Paper.design)
---

# /creative-from-winners — Winning Ad → On-Brand Creative

Riley Brown's pattern: never design ads from a blank canvas. Take an ad that has already proven itself (longest-running = paid-for-a-reason), keep its *structure*, and swap in your brand — then diverge from there. His stack used Paper.design; ours routes through the creative infrastructure we already own.

**Lineage**: `skills/riley-brown-marketing-automation/` (template-steal pattern) · feeds from `/ad-spy` · produces for Farrice or clients (supplement/performance brands = $2,500 sprint lane).

## Usage

```
/creative-from-winners [ad reference — Social Intelligence page, image path, or ad description] --brand [brand/client]
```

## Steps

### 1. Ground the winner

Pull the source ad from the **Social Intelligence** Notion DB (`NOTION_DB_SOCIAL_INTEL`, populated by `/ad-spy`) or from a provided image/URL. Extract its skeleton before touching design:

- Offer framing · Hook mechanism · Visual hierarchy (what you read 1st/2nd/3rd) · CTA type · Proof element · Why it survived (the Analysis field)

### 2. Ground the brand

Load brand truth before generation — never hand a bare prompt to a generator (Fantastic Studio rule):

- Client brand: their DESIGN.md (or run `/brand-asset-scrape` first if none exists)
- Farrice's own: `_active/farrice-brand/` + VOICE-CARD as copy layer

### 3. Concept + composition (structure transfer, not clone)

Route by need — these are options, never pipeline steps:

| Need | Route |
|------|-------|
| Static ad concepts + test plan | `/dara-static-engine` (17 workflows — format selection, hooks, objection engine) |
| Full art direction + prompt compile | `skills/fantastic-posters/` → Fantastic Studio flow |
| Copy skeleton on the winner's structure | `/copy-engine` or Luke Iha hooks layer |

Riley's floor and ours: "Would we ever do this word for word? We'd change it more than this." The winner supplies the **skeleton**; the brand supplies the flesh. One structure → 3+ divergent executions.

### 4. Production

- **Canva MCP** (`generate-design`, brand templates) — layout-true statics
- **Higgsfield MCP** (`generate_image`, Soul for people) — pre-flight `creative_router.py` per visual-tool-routing memory
- Both are cost/credit-gated where applicable — surface cost to Farrice before batch generation, never auto-spend.

### 5. Close the loop

Write finished variants back to the Social Intelligence page (Media property) so ad → analysis → variant lives in one record. Offer `/jam` on taste-bearing picks.

## Quality Gate

- Structure borrowed, brand native — a cold viewer must not clock the source ad
- No real people/names/bylines carried over from the source creative (Riley's own demo accidentally kept "Dr. Fahim Hussain" from the competitor ad — this is the named failure mode)
- Copy passes `prose_classifier.py check` + reader-contract dials
