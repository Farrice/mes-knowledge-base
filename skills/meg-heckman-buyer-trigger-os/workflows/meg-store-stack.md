---
description: "/meg-store-stack — trigger-led store architecture: collections as identity claims, homepage as identity sort, PDP trust stacked at the cart gate — compiled into a build-requirements spec for BitBranding. Meg defines what the store says; BitBranding builds it. 'Does this store feel trustworthy?'"
---

# Store Stack

A buyer the design already won can still be lost by the store. She has watched it from both ends: print-catalog stores — T-Shirts, Hoodies, New Arrivals — that make a person who just felt seen go re-find themselves in a warehouse aisle, and "objectively terrible websites" that "convert like crazy" because every shelf kept saying *you*. The store is the design's sentence continued at room scale. This workflow architects what the store SAYS — which person each collection claims, which door the homepage opens first, what the cart page must prove before legitimacy collapses — then hands BitBranding a requirements spec, not a wireframe. Meg decides what every element says; BitBranding decides which theme lever says it.

## Pre-Flight
Read these files before executing:
1. `skills/meg-heckman-buyer-trigger-os/genius.md` (§ Diagnostic Mechanics, § Hidden Knowledge 4 / 7 / 8 / 11, § Market Mechanics)
2. `skills/meg-heckman-buyer-trigger-os/references/genius-patterns.md` (Patterns 12, 15–16)
3. `skills/bitbranding-fashion-shopify/SKILL.md` (the execution partner — know what it covers so this spec references it instead of duplicating it)

> **🔒 Pre-Flight Gate**: A store cannot sort people it hasn't named. If the brand's sub-identities are not already mapped as behavioral moments, stop and run `/meg-sub-identity-map` first. Architecting collections for "everyone who likes the niche" produces a print catalog with better fonts.

## Input Required
- Product catalog: every live/planned design with its target sub-identity (gaps allowed — orphans surface in Step 1)
- The sub-identity map (from `/meg-sub-identity-map`) or best available identity definitions
- Platform + mode: Shopify new launch · Shopify restructure (store URL) · Bonfire campaign page · client audit
- Funnel numbers if they exist (Add-to-Cart, Initiate Checkout, Conversion) — they prioritize the trust stack
- The incumbent brand this customer already shops (Gap/Nike/REI-class) — the Step 4 benchmark

---

## Workflow

### Step 1: Collections as Identity Claims
The unit of store architecture is the PERSON, not the product type. "Genre Defined" beats "T-Shirts"; the casual-hiker shelf beats the all-hiking shelf — a shelf for everyone in the niche is a poster at room scale. Re-sort the catalog:

| Collection name | Sub-identity (behavioral moment) | Billboard statement ("shopping this shelf says: I ___") | Products |
|---|---|---|---|

Every collection names a person; every billboard statement is first-person and would survive `/meg-trigger-audit`. Products that fit no person are **orphans** — audit or kill; never invent a "Misc" shelf. Product-type groupings may survive as FILTERS (utility), never as front doors (architecture).

### Step 2: Homepage as Identity Sort
The first question the store asks is "which person are you?" — never "what product do you want?" Map the sort:
- **Hero** = the strongest mirror in the catalog: the lead collection's billboard statement, not a discount banner.
- **Navigation = identity doors.** Each top-level nav item is a Step 1 collection — a door the right person walks through because it is labeled with THEM.
- **Identity tiles** below the hero: one per sub-identity, billboard statement as the tile line.

The test: a cold visitor self-sorts within one screen — they know their door before they see a product grid.

### Step 3: PDP Trust Stack (the cart-gate items)
The trust gate is the CART, not the checkout (HK-4) — legitimacy collapses at initiate-checkout: shipping shock, no reviews, no return policy. Itemize what every PDP must answer BEFORE the buyer taps add-to-cart:

| Trust item | Requirement |
|---|---|
| Shipping cost clarity | Visible BEFORE the cart — no surprise at the gate |
| Delivery window | Concrete range near the CTA, not buried in FAQ |
| Reviews placement | Within one scroll of the buy box; if none exist yet, name the substitute proof |
| Return policy | Reachable from the PDP, not footer-only |
| Sizing confidence | Size chart + fit note ("runs large" beats silence) |
| **Mobile CTA position** | Audit "where my add to cart button actually lands on a mobile device" (HK-11) — position is a revenue metric, not a preference |

If funnel numbers exist: weak Add-to-Cart (7–8% healthy) → images, pricing, mobile CTA; weak Initiate Checkout (5–6%) → cart-page trust. Fix the named stage only; route deeper diagnosis to `/meg-funnel-doctor`. Thresholds are POD/Meta 2026 defaults, not laws.

### Step 4: Benchmark Law — then Identity Before Polish
Customer expectations are set by Gap, Nike, and REI, not by other POD stores (HK-8). Spec what incumbents have trained buyers to expect: a seasonal-collection slot, a drops cadence, one coherent mockup world — the store must FEEL like a brand, not a print catalog. THEN apply the override (HK-7): identity resonance beats UX polish — "objectively terrible websites... convert like crazy" when identity fit is strong. The sequence is non-negotiable: **identity architecture ships first; polish is a backlog, never a launch blocker.** A polished catalog is still a catalog.

### Step 5: Listing Copy Slots
This workflow places copy; `/meg-listing-copy` writes it. Mark the slots in the spec:
- **PDP lead** — recognition line first, identity statement, social-moment line; logic (fabric, fit) last.
- **Collection intro** — the Step 1 billboard statement expanded to 1–2 in-world sentences.

Tag each slot with its sub-identity and lead trigger so the copy arrives pre-aimed.

### Step 6: The BitBranding Handoff Spec
Compile Steps 1–5 into a build-requirements document: WHAT each element says and the trigger it serves — never HOW Shopify renders it. Theme levers, Horizon settings, product-card mechanics, and collection-page SEO structure are BitBranding's lane: route execution to `/bb-rebuild` (architecture), `/bb-product-card` (PDP components), `/bb-collection-content` (collection copy/SEO binding). The spec contains: collection structure (names, membership, order) · nav map (identity doors) · PDP trust components + positions · homepage section order · mobile checks (CTA landing, one-screen self-sort) · copy slots awaiting `/meg-listing-copy`. This is a requirements spec, not a wireframe — BitBranding owns layout and build decisions inside it.

## Content Type Adaptations
| Mode | Adaptation |
|--------|-----------|
| New store launch | Full six steps; architecture locked before any product upload — ideally the brand name already carries the twist (HK-12) |
| Existing restructure (mybpm.store-class, ~30 products) | Step 1 becomes a re-sort: map every live product to a person; orphans flagged for `/meg-trigger-audit`; nav rebuilt before any new design ships |
| Bonfire single-campaign page | No collections/nav — Steps 1–2 collapse into one identity claim above the fold; trust stack compresses to shipping, delivery, and sizing adjacent to the CTA |
| Client audit deliverable | 2-page max: page 1 = current vs. identity-sorted architecture; page 2 = top 5 cart-trust fixes + handoff list. Density over completeness |

## Output Format
```
STORE STACK — [brand] — [date] — [launch/restructure/bonfire/audit]

IDENTITY ARCHITECTURE
| Collection | Person (behavioral moment) | Billboard statement | Products |
Orphans: ___ → /meg-trigger-audit

HOMEPAGE SORT: hero = ___ · identity doors: ___ · tiles: ___
PDP TRUST STACK (cart gate): shipping ___ · delivery ___ · reviews ___ · returns ___ · sizing ___
MOBILE CTA: [where add-to-cart lands on a phone — PASS/FIX]
BENCHMARK READ: feels like [brand / print catalog] · seasonal-drop slot: ___ · polish backlog (post-launch): ___
COPY SLOTS: [n] PDP leads + [n] collection intros → /meg-listing-copy
HANDOFF → BitBranding: requirements doc at [path] · execute via /bb-rebuild → /bb-product-card → /bb-collection-content
NEXT: [/meg-listing-copy | /meg-funnel-doctor after first traffic | /meg-aov-architect for collection cohesion]
```

## Quality Gate
> **🛡️ Anti-Pattern Check**: review against `genius.md § Anti-Patterns` before delivering.
- Every collection names a person as a behavioral moment — zero product-type front doors (HK-2).
- Trust stack is itemized at the CART stage, not checkout (HK-4); shipping clarity sits before the gate.
- Mobile CTA position explicitly checked and reported (HK-11) — never assumed from desktop.
- No Shopify execution detail duplicated from BitBranding — levers and theme settings referenced to `/bb-*` workflows, not rewritten here.
- Identity-before-polish sequencing stated in the deliverable (HK-7 governs HK-8) — polish has a backlog, not a veto.
- Her thresholds carried as POD/Meta 2026 defaults; revenue claims, if cited, labeled UNCONFIRMED.

## Common Pitfalls
- **Product-type taxonomy relapse.** "T-Shirts / Hoodies / New" is the catalog instinct — it asks the buyer to do the identity work the store was supposed to do. Recovery: rename until every front door names a person; demote types to filters.
- **Trust theater at checkout while the cart leaks.** Badges and payment seals can't save the buyer who already bounced at shipping shock. Recovery: HK-4 — itemize cart-gate trust first; touch checkout only after initiate-checkout is healthy.
- **Polishing UX before identity resonance exists.** A beautiful store of posters converts like a museum. Recovery: if collections don't yet name people, stop speccing animations and return to Step 1.
- **Treating the handoff as a wireframe.** Drawing pixel layouts duplicates BitBranding's job badly and buries the requirements. Recovery: spec WHAT each element says and WHY (the trigger); BitBranding owns HOW.
