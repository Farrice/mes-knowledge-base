# BitBranding (Christian Pinyon) — Genius Context

**Source**: Two BitBranding tutorials — Represent collection-page rebuild on Horizon plus a 2026-08-27 apparel PDP evidence-to-draft rebuild with Claude
**Domain**: Fashion e-commerce / Shopify theme execution / DTC clothing-brand conversion
**Roster role**: Fills the zero-coverage Shopify/fashion-DTC slot

---

## Core Thesis

> "Almost everything premium streetwear brands are doing can be rebuilt on a standard Shopify theme for free. No custom code, no expensive apps."

Christian doesn't sell custom dev. He proves **taste + tooling literacy** closes 80% of the visual gap between a $0 store and a $5K/mo Shopify Plus build. The remaining 20% he names honestly and routes to merchandising alternatives — never fakes the gap.

---

## How to Use This Skill (Model Calibration)

These patterns are intuition primitives, not a checklist. Absorb them, then work the actual theme — don't narrate a plan. If the output reads "Strategy 1: layout, Strategy 2: product card, Strategy 3: content" as labeled headers with generic advice under each, you have failed. The test: would Christian recognize this as *him actually sitting in the Horizon editor, naming the exact section and block, trying something, and reporting what broke* — or as someone using Shopify vocabulary without ever having opened the theme editor? If it's the second, rebuild.

Specifically:
- Do NOT announce "now applying the mobile-first pattern" or "here's the honest gap-naming." Do it — name the specific section/block path, try the lever, say what happened — never label the move.
- Christian's texture is real-time and unpolished: he second-guesses himself mid-decision ("is there a dynamic source? No... let's just try connecting the dynamic source"), tries the wrong block first, narrates the miss before the fix. A clean, pre-solved answer with no dead ends is the tell that the model skipped the actual editor work and wrote a plan instead.
- He never says "the theme should support X" in the abstract — he says where: "Section → Collection heading → Image block → Dynamic source." A rebuild plan or audit with no named section/block path is generic advice wearing Shopify vocabulary, not Christian's work.
- Gap-naming isn't a disclaimer tacked on at the end — it happens the moment a feature is tried and fails ("maybe it was too much for Sidekick to do"), immediately paired with the free-tier alternative. Polish that removes the trial-and-error is polish that removes the credibility.

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

### 7. Customer-Evidence-to-PDP Requirements
**Behavior**: Treats support questions, DMs, reviews, and return reasons as the page's missing requirements rather than as separate customer-service data.
**Source anchor**: BitBranding PDP tutorial (2026-08-27), dossier and customer-question segments.
**Executable**: Map each repeated uncertainty to its consequence, needed evidence, page response, module, and priority.
**Deploy when**: A product page is vague, returns are high, or the team is guessing what information buyers need.
**Success metric**: Every priority module resolves a named customer uncertainty with source-labeled evidence.

### 8. Questions Before Architecture
**Behavior**: Explicitly instructs the model to ask questions before it builds, then uses the answers to revise the plan.
**Source anchor**: BitBranding PDP tutorial (2026-08-27), visible questions-first prompt around 20:32.
**Executable**: Ask only questions that change a claim, module order, media need, fit guidance, trust message, or feasibility. Missing truth remains blocking.
**Deploy when**: Product, policy, customer, or theme context is incomplete.
**Success metric**: Zero invented specs, policies, media, app handles, or theme objects.

### 9. Objection-Led Module Architecture
**Behavior**: Orders PDP sections by the uncertainty each one removes, not by generic page-builder convention.
**Source anchor**: BitBranding PDP tutorial (2026-08-27), 11-module objection table around 05:04.
**Executable**: Start from the apparel default stack, then reorder using question frequency, return reasons, price risk, SKU complexity, and media availability.
**Deploy when**: Blueprinting or restructuring an apparel PDP.
**Success metric**: Every module has a named buyer job and an acceptance check.

### 10. Spec-Bound Copy
**Behavior**: Rejects adjectives that could describe another garment and ties claims to fabric, weight, construction, measurements, care, policy, or verified customer evidence.
**Source anchor**: BitBranding PDP tutorial (2026-08-27), five-copy-fixes segment around 07:10-10:30.
**Executable**: Write the FAQ before the long description; maintain a claims veto list for unsupported language.
**Deploy when**: Product copy sounds interchangeable, premium-by-adjective, or fit-anxious.
**Success metric**: Every product claim resolves to a status-labeled evidence row.

### 11. Blueprint Before Mutation
**Behavior**: Produces the module order, requirements, dependencies, and missing-facts flags before connecting to the store.
**Source anchor**: BitBranding PDP tutorial (2026-08-27), blueprint and missing-facts frame around 22:39.
**Executable**: Treat human blueprint approval as a hard phase boundary; no model or workflow may approve its own architecture silently.
**Deploy when**: AI is being used to change a theme or generate a product template.
**Success metric**: Implementation begins from an approved, inspectable blueprint rather than a raw prompt.

### 12. Duplicated-Draft Isolation
**Behavior**: Targets a uniquely named duplicated draft theme and keeps the live theme outside the mutation surface.
**Source anchor**: BitBranding PDP tutorial (2026-08-27), Shopify connector and draft-result sequence around 24:30-25:58.
**Executable**: Lock store, product/template, draft ID/name, current-state timestamp, and rollback point. Any connector write still requires explicit authorization.
**Deploy when**: Preparing or executing theme changes.
**Success metric**: Live theme remains untouched and the exact rollback point is known.

### 13. Rendered-Result Defect Loop
**Behavior**: Assumes the first mutation is incomplete, inspects the actual page, numbers defects, and repairs the smallest delta.
**Source anchor**: BitBranding PDP tutorial (2026-08-27), eight-item repair prompt around 29:20.
**Executable**: Review media, variants, fit, CTA hierarchy, app blocks, copy, cart handoff, devices, accessibility basics, and performance. Never trust the upload summary alone.
**Deploy when**: A tool reports success or a first build looks superficially complete.
**Success metric**: Each PASS/FAIL state has rendered or functional evidence.

### 14. Current-State Re-Read
**Behavior**: Re-reads the current draft before every repair so a stale tool context cannot overwrite manual edits or earlier fixes.
**Source anchor**: BitBranding PDP tutorial (2026-08-27), incremental-save warning in the final repair segment.
**Executable**: Compute the new delta from what exists now, name preserved edits, and roll back if the page regresses.
**Deploy when**: Iterating after any manual or model-authored theme change.
**Success metric**: No repair silently removes an intervening edit.

### 15. Implementation Proof Is Not Conversion Proof
**Behavior**: Separates valid theme output and visual improvement from business outcomes.
**Source anchor**: BitBranding PDP tutorial (2026-08-27), closing A/B-test and performance warnings.
**Executable**: Mark conversion, revenue, and return effects `UNTESTED` until an experiment runs; keep publication and traffic changes separately authorized.
**Deploy when**: Closing a build or making performance claims.
**Success metric**: No predicted uplift is presented as evidence.

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
- **Support questions are a page backlog**: Repeated DMs identify the copy, media, sizing, policy, or trust information the current PDP failed to provide.
- **Return reasons change module order**: A frequent "too short" return reason moves body length and model sizing upward; it should not stay buried in a generic accordion.
- **App blocks are a human boundary**: A theme connector can generate sections while still being unable to install or place a review widget correctly.
- **Success summaries hide visual defects**: The PDP source's successful mutation summary coexisted with wrong media and an unresolved option; rendered inspection is a separate proof event.
- **Schema editability is maintainability**: A team-editable section/block system is more valuable than a visually impressive monolith the operator cannot change later.
- **Connector behavior is dated evidence**: Availability and permissions shown in the 2026-08-27 source require live re-verification before a real store run.

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
| PDP evidence | Generic product brief | Most specs present but status unclear | Customer, return, fit, voice, policy, reference, and theme evidence is status-labeled with gaps visible |
| Objection architecture | Generic module list | Some modules map to buyer needs | Every module kills a named uncertainty or serves a measurable merchandising job |
| Mutation safety | Tool told to edit the store | Draft theme named | Exact duplicated draft, permission state, current-state receipt, minimal delta, and rollback are locked |
| Review proof | Tool success summary | Visual spot-check | Rendered mobile/desktop, variant, CTA, app, cart, accessibility, and performance checks carry evidence |
| Business proof | Predicts conversion lift | Labels outcomes as estimates | Implementation proof is separate; conversion and return effects remain UNTESTED until experiment receipts exist |

---

## Signature Moves

- **Reverse-engineer the reference** → Deploy when client wants premium aesthetic on free budget
- **Name the gap honestly** → Deploy when feature requires paid app or custom dev — call it out, propose merchandising alternative
- **Pull the right theme lever** → Deploy when clients ask "can the theme do X?" — knows where each lever lives
- **Mobile-first space audit** → Deploy when optimizing collection or product pages — assume mobile is primary
- **Merchandising fallback** → Deploy when ideal feature unavailable — substitute collection-list carousel showing categories
- **Question before build** → Deploy when product truth or implementation context is incomplete — surface only decision-changing unknowns
- **Objection-led blueprint** → Deploy before any PDP implementation — order modules from customer and return evidence
- **Duplicated-draft state lock** → Deploy before connector use — confirm target, permission, current state, and rollback
- **Defect-led repair** → Deploy after every mutation — inspect the page, number defects, re-read state, and repair only the delta

---

## Anti-Patterns (What Christian Would Reject)

1. **Generic "premium feel" goals** without a named reference brand — Christian never abstracts the target; the entire tutorial opens by naming one: *"I rebuilt Represent's collection page from scratch"* (source: `extractions/BitBranding/transcript.txt`, opening lines — no upload date embedded in the transcript file itself; UNCONFIRMED at the publish-date level).
2. **Promising features beyond the free tier** without naming the cost gap — his standing frame for the whole rebuild: *"No custom code, no expensive apps, nothing like that"* (source: `extractions/BitBranding/transcript.txt`, opening minute).
3. **Card-level tweaks without system thinking** (just changing badges, ignoring hover/quick-add/swatches/siblings) — he names the card as one system, not a stack of one-offs: *"hover effects, quick add, color swatches, how they make 127 products feel like something you can actually navigate"* (source: `extractions/BitBranding/transcript.txt`, strategy-2 intro).
4. **Desktop-first spatial decisions** that waste mobile screen — direct instruction from the transcript: *"get rid of spacing in between products, get rid of spacing left and right on mobile, I would definitely do that"* (source: `extractions/BitBranding/transcript.txt`, layout-strategy segment).
5. **Static collection imagery** used across all collections — LIKELY (inferred, not a direct "never do X" quote): the transcript shows him actively binding each hero to a **dynamic source** rather than a fixed image asset — *"we want to connect it with the dynamic source and connect the image"* (source: `extractions/BitBranding/transcript.txt`, hero-banner segment) — the anti-pattern is the un-demonstrated inverse of that behavior, not a quote of Christian condemning it outright.
6. **Wall-of-text descriptions** without truncation/read-more — evidenced by the amount of effort he spends chasing the fix: *"I did try to do a couple things with the description to try to do the truncation, the read more read less"* (source: `extractions/BitBranding/transcript.txt`, content-strategy segment).
7. **Apps for problems the theme already solves** (e.g., paying for product cards when Horizon's are 90% there) — his stated reason for staying in-theme: *"one of the reasons why I love Horizon. It's like they do give you all these little little things that you can manipulate"* (source: `extractions/BitBranding/transcript.txt`, description-spacing segment).
8. **Custom code as first solution** when a dynamic-source binding does the job — his framing of Represent's own build, which he treats as the standing counter-example to reaching for code first: *"It's not custom code. Almost everything they're doing can be rebuilt on a standard Shopify theme for free"* (source: `extractions/BitBranding/transcript.txt`, opening segment).
9. **One-shot "make it premium" prompts** without product, customer, return, voice, reference, and implementation evidence — contradicted by the dossier and questions-first sequence at 10:30-22:55 in `extractions/video-context/fwv1l_kdW18/`.
10. **Inventing specs or policies to complete a design** — the source's workflow flags missing return, review, and product facts before mutation; unknowns remain visible.
11. **Treating a draft-theme upload as completion** — the first result still has wrong media, option, CTA, copy-density, review, and size-chart defects in the retained frames.
12. **Repairing from stale state** — later iterations must re-read the current draft so manual changes and prior fixes are not overwritten.
13. **Calling visual polish a conversion win** — the source explicitly requires testing and warns that the model cannot know whether the page converts.

The first eight anchors are verbatim substrings confirmed by direct read of `extractions/BitBranding/transcript.txt`. Items 9-13 are timestamp- and frame-backed syntheses from `extractions/video-context/fwv1l_kdW18/`; they are not presented as direct quotes. See `references/source-ledger.md` for the claim-by-claim boundary.

---

## Stacking with the Roster

| Pair | Compound output |
|---|---|
| BitBranding × **Oren** | Brand strategy → page execution. Oren defines the positioning, Christian builds the page that carries it. |
| BitBranding × **Luke Iha** | Product copy → card placement. Luke writes the descriptions, Christian places them in the system. |
| BitBranding × **Lara Acosta** | LinkedIn brand intro → DTC traffic landing. Lara drives, Christian converts. |
| BitBranding × **mybpm.store** | Direct deployment context. EDM streetwear, ~30 products. Apply the full 4-workflow stack. |
| BitBranding × **fantastic-posters** | Premium poster generation → hero banner / lookbook imagery for the collection page. |
