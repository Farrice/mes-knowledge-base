# BitBranding (Christian Pinyon) — Genius Context

**Source**: Single YouTube tutorial (Represent collection-page rebuild on Horizon, ~10.6K words)
**Domain**: Fashion e-commerce / Shopify theme execution / DTC clothing-brand conversion
**Roster role**: Fills the zero-coverage Shopify/fashion-DTC slot

---

## Core Thesis

> "Almost everything premium streetwear brands are doing can be rebuilt on a standard Shopify theme for free. No custom code, no expensive apps."

Christian doesn't sell custom dev. He proves **taste + tooling literacy** closes 80% of the visual gap between a $0 store and a $5K/mo Shopify Plus build. The remaining 20% he names honestly and routes to merchandising alternatives — never fakes the gap.

---

## Genius Patterns

### 1. Premium-Aesthetic-on-Free-Stack Reverse-Engineering
**Behavior**: Pulls a premium reference (Represent, Fear of God, Stüssy) apart in real time. Identifies what to copy, what's not worth chasing, what's beyond the free tier.
**Executable**: Always start with a named reference. Never abstract "premium feel" — point at a specific brand and reverse-engineer their decisions.
**Deploy when**: Client wants premium look without Shopify Plus / custom dev budget.
**Success metric**: 80%+ visual match to reference at $0 in apps/code.

### 2. Honest Free-Tier Triage
**Behavior**: Names what he *can't* recreate without paid apps in the moment ("we won't be able to fully recreate this"), pivots to free alternatives instead of forcing it.
**Executable**: For every premium feature, classify: FREE-TIER ACHIEVABLE / NEEDS APP / NEEDS CUSTOM CODE / NOT WORTH IT. Always propose a free-tier merchandising fallback for the last three.
**Deploy when**: Audit identifies a feature beyond budget.
**Success metric**: Zero broken promises. Every "we'll do this" is actually achievable.

### 3. Theme Lever Cartography
**Behavior**: Mental map of where each Horizon setting lives. Knows dynamic-source bindings, transparent header toggle, second-image-on-hover, Sidekick AI block generation, product-siblings, search-and-discovery filter app.
**Executable**: Reference specific lever paths in any rebuild plan: "Section → Collection heading → Image block → Dynamic source." Don't say "find the setting."
**Deploy when**: Any rebuild or audit on Shopify Horizon.
**Success metric**: User can find the lever from your description without screenshots.

### 4. Hierarchical Settings Debugging
**Behavior**: When a setting won't budge, checks ONE level up — parent section, theme settings, or header section may override.
**Executable**: Three-step debug: (a) check current section settings, (b) check parent/wrapper section, (c) check global theme settings. Don't loop on the current level.
**Deploy when**: A change isn't taking effect or is being overridden.
**Success metric**: Bug resolved in <3 minutes without trial-and-error spiral.

### 5. Mobile-First Spatial Thinking
**Behavior**: Spatial decisions default to mobile. "Get rid of spacing left and right on mobile." "Portrait > square aspect ratio for clothing." "Maximize product space."
**Executable**: Audit mobile FIRST, desktop SECOND. Strip default theme spacing on mobile by default. Use portrait for any image-of-a-person product.
**Deploy when**: Optimizing collection or product page layout.
**Success metric**: Mobile shows 2x more product per screen than out-of-box theme defaults.

### 6. Product Card as 5-Component System
**Behavior**: Treats the product card as a system of 5 levers, not a template:
1. Image hover swap (second image on hover)
2. Inline quick-add with size availability
3. Color swatches (visual, not text labels)
4. Strategic badges (sale, restock, new — not promotional spam)
5. Color variant separation (siblings/combined-listings — same product split by colorway across grid)
**Executable**: For any card audit, score each of the 5 components. Never optimize a card by changing one element — change the system.
**Deploy when**: Conversion-rate work on collection pages.
**Success metric**: All 5 components scored and optimized, not just hover or just badges.

---

## Hidden Knowledge

- **Static image vs. dynamic source binding**: Attaching a static image asset makes every collection use the same hero. Dynamic source pulls per-collection imagery from the collection record. Amateurs ship one hero across 15 collections without realizing it.
- **Compare-at-price is the only Horizon badge trigger**: No custom badge UI in free Horizon. Workaround: meta-fields with text labels ("3 colors," "Restocked"), then bind via dynamic source on a text block.
- **Aspect-ratio rescue**: When product images are different sizes, switching aspect ratio to portrait fixes the wonky display globally. Faster than re-exporting from Photoshop/Canva.
- **Two-tab workflow**: Theme editor in one tab, Shopify backend (products, collections, meta-fields) in another. Speed comes from tab-switching, not menu-hunting.
- **Sidekick (Shopify AI) limitation map**:
  - GREAT for: visual blocks, headlines, simple text components, layout adjustments
  - FAILS at: filter logic, recently-viewed sections, anything requiring functional state changes
  - Don't waste prompts on what it can't do.
- **36 is the Horizon products-per-page max**: Choose between "load more" (paginated) and "auto-load on scroll" — both have UX trade-offs. Better Ruler Chrome extension measures pixel dimensions on reference sites for matching.

---

## Hall of Fame Exemplars

### Exemplar 1 — Represent's Collection Page
**Context**: UK luxury streetwear brand, Shopify-native (recently moved off headless).
**The example**: No clutter. No sidebar. Products end-to-end with no spacing between cards. Full-width editorial hero image. Color-variant siblings split across the grid (same product appears 3x in different colorways) but combined on the product page. Restock badges top-left, subtle. Bottom collection description for SEO.
**What makes it excellent**: Every decision serves *product-forward visual hierarchy*. Filters tucked in a slide-out, never permanent sidebar. The page screams "premium" because nothing competes with the products.

### Exemplar 2 — Christian's Free-Horizon Rebuild
**Context**: Same Represent reference, free Horizon theme, no apps.
**The example**: Got 80% match at $0. Hero banner with dynamic source binding. Four-column grid with horizontal-gap zeroed. Mobile spacing stripped. Inline quick-add. Bottom rich-text description with interlinking. Sale badges via compare-at-price. Honest about three gaps: combined-listings color-variant split (needs theme support or app), custom badges (no Horizon UI), recently-viewed (Sidekick failed, no app fallback).
**What makes it excellent**: The honest gap-naming. He didn't pretend the rebuild was 100%. He said "this is 80%, here's what's missing, here's the merchandising fallback for the gap."

### Anti-Exemplar — Default Theme Clothing Store
**What mediocre looks like**: Permanent sidebar with 14 filter options. Wall-of-text collection description, no truncation. Mismatched product image aspect ratios (some tall, some square, some wide). Static collection hero used across all 15 collections. No SEO interlinking in descriptions. Default mobile spacing wastes 40% of screen.
**Why it fails**: Every decision treats the theme as a template instead of a system. Each component looks fine in isolation; together they shout "DTC brand from a Fiverr template."

---

## Quality Rubric

| Criterion | Score 4 | Score 7 | Score 10 |
|---|---|---|---|
| Visual hierarchy | Has filters but cluttered | Clean grid, good hero | End-to-end products, editorial hero, no spacing waste |
| Free-stack ceiling | Picks expensive apps for everything | Uses theme + 1 strategic app | 80%+ of premium look on free theme alone |
| Honest gap-naming | Promises what can't be delivered | Sometimes acknowledges limits | Real-time names every gap, proposes alternative |
| SEO depth | No collection description | Short description only | Top description + truncated read-more + rich-text bottom description with interlinking |
| Mobile space use | Default theme spacing | Reduced gaps | Edge-to-edge products, no left/right padding |
| Product card system | One element optimized | 3/5 components addressed | All 5 components scored & optimized as a system |

---

## Signature Moves

- **Reverse-engineer the reference** → Deploy when client wants premium aesthetic on free budget
- **Name the gap honestly** → Deploy when feature requires paid app or custom dev — call it out, propose merchandising alternative
- **Pull the right theme lever** → Deploy when clients ask "can the theme do X?" — knows where each lever lives
- **Mobile-first space audit** → Deploy when optimizing collection or product pages — assume mobile is primary
- **Merchandising fallback** → Deploy when ideal feature unavailable — substitute collection-list carousel showing categories

---

## Anti-Patterns (What Christian Would Reject)

1. **Generic "premium feel" goals** without a named reference brand
2. **Promising features beyond the free tier** without naming the cost gap
3. **Card-level tweaks without system thinking** (just changing badges, ignoring hover/quick-add/swatches/siblings)
4. **Desktop-first spatial decisions** that waste mobile screen
5. **Static collection imagery** used across all collections
6. **Wall-of-text descriptions** without truncation/read-more
7. **Apps for problems the theme already solves** (e.g., paying for product cards when Horizon's are 90% there)
8. **Custom code as first solution** when a dynamic-source binding does the job

---

## Stacking with the Roster

| Pair | Compound output |
|---|---|
| BitBranding × **Oren** | Brand strategy → page execution. Oren defines the positioning, Christian builds the page that carries it. |
| BitBranding × **Luke Iha** | Product copy → card placement. Luke writes the descriptions, Christian places them in the system. |
| BitBranding × **Lara Acosta** | LinkedIn brand intro → DTC traffic landing. Lara drives, Christian converts. |
| BitBranding × **mybpm.store** | Direct deployment context. EDM streetwear, ~30 products. Apply the full 4-workflow stack. |
| BitBranding × **fantastic-posters** | Premium poster generation → hero banner / lookbook imagery for the collection page. |
