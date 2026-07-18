# Agentic Commerce Integration

> **Expert**: Oren — Content-Team Architecture
> **Produces**: Commerce Layer Architecture + Content-to-Conversion Protocol + Implementation Plan
> **Use When**: Integrating AI-powered commerce (shoppable content, automated checkout, content-driven conversion) into the content flywheel
> **Load First**: [genius.md](../genius.md) — Patterns 11 (Content-Product Integration), 2 (Flywheel), 9 (Paid Creative Ops)

---

## Step 1: Commerce Readiness Assessment

Collect:
1. **E-commerce platform** — Shopify, WooCommerce, custom? API capabilities?
2. **Current conversion path** — how does someone go from content to purchase today?
3. **Friction points** — where do you lose people between content and checkout?
4. **Product catalog size** — 1 product? 10? 100+? SKU complexity?
5. **Content volume** — how much content per week features products?
6. **Tech stack** — what tools currently connect content to commerce?

---

## Step 2: Agentic Commerce Architecture

### What Agentic Commerce Means
The shift from "click link in bio → browse website → find product → checkout" to "see content → purchase within the content experience." The AI agent eliminates friction between inspiration and transaction.

### The Three Layers

```
LAYER 1: Content-to-Commerce Tagging
Every piece of content that features a product gets:
├── Product ID linked
├── Price point embedded
├── Variant info (size, color) available
├── Checkout capability within the platform (where possible)
└── Attribution tracking to source content

LAYER 2: AI-Powered Discovery
An agentic layer that:
├── Recommends products based on content viewing behavior
├── Cross-references content watched with purchase history
├── Surfaces related content when a product is viewed
├── Auto-generates product context from content library
└── Personalizes the shopping experience per user

LAYER 3: Autonomous Checkout
The minimal-friction commerce layer:
├── One-tap purchase from content
├── AI chatbot that answers product questions using content library
├── Dynamic pricing/offers based on engagement depth
├── Cart persistence across content touchpoints
└── Post-purchase content loop (buy → receive → create content → share)
```

---

## Step 3: Platform-Specific Implementation

### Instagram/TikTok Shop Integration
```
CONTENT REQUIREMENTS:
├── Every product post tagged with shop product
├── Stories with product stickers (not just link stickers)
├── Live shopping events (founder or creator hosts)
├── Shop tab curated as "editorial picks" not just product grid
└── Creator content must include product tags (add to brief template)

WORKFLOW INTEGRATION:
├── Brief template adds: "Product to feature: [SKU]"
├── Strategist ensures 30%+ of weekly content has commerce tags
├── Analytics track: views → shop clicks → purchases per content piece
└── Monthly commerce performance review added to creative audit
```

### Website/PDP Integration
```
CONTENT ON PRODUCT PAGES:
├── Creator video embedded on every PDP
├── "As seen in" linking content to product
├── UGC gallery pulling from tagged social posts
├── Founder video explaining design decisions (from /oren-founder-content)
└── Dynamic content rotation based on engagement data

PRODUCT IN CONTENT HUB:
├── Brand blog/editorial → every article links to featured products
├── Video library on-site → shoppable video player
├── Lookbook pages → every look is instantly purchasable
└── Newsletter archive → past issues with live product links
```

### AI Chat Commerce
```
THE AI SHOPPING AGENT:
├── Trained on: product catalog + brand content library + FAQs
├── Can: answer product questions using content context
│   Example: "You asked about the running jacket. Here's our founder
│   explaining why we chose this fabric [link to content]."
├── Can: recommend products based on what content the user watched
├── Can: complete checkout within chat flow
├── Can: schedule follow-up content (post-purchase education)
└── Cannot: make promises not in the product spec, offer unauthorized discounts

IMPLEMENTATION:
├── Tool options: Swap (Oren-referenced), custom GPT, Shopify Sidekick
├── Training data: product descriptions, creator content transcripts,
│   FAQ database, return policy, sizing guides
├── Placement: website widget, Instagram DM auto-responder,
│   email response system
└── Measurement: conversations → checkout rate, avg order value,
    repeat purchase rate
```

---

## Step 4: Content-to-Commerce Metrics

Track these metrics to measure the agentic commerce layer:

```
CONTENT COMMERCE METRICS:
├── Content-attributed revenue: $ from content-first touchpoints
├── Content-to-checkout conversion rate: % who see content → purchase
├── Avg touchpoints to purchase: how many content pieces before buying
├── Top-converting content: which specific pieces drive most revenue
├── Creator attribution: which creator's content drives most revenue
├── Platform attribution: which platform → most commerce
├── AI agent conversion: chat → checkout rate
├── Post-purchase content creation: % of buyers who create content
└── Content CAC: cost to create content that drives each customer acquisition
```

---

## Step 5: Post-Purchase Content Loop

The flywheel doesn't end at purchase. Design the post-purchase content engine:

```
POST-PURCHASE SEQUENCE:
├── Day 0: Order confirmation with content ("Here's how to use your [product]")
├── Day 3: Delivery + unboxing prompt ("Share your unboxing → tag us")
├── Day 7: Usage content (founder video: "Here's how I use mine")
├── Day 14: Review request + incentive
├── Day 30: Community feature opportunity
└── Day 60: Repeat purchase content ("Pair it with…")

USER-GENERATED CONTENT CAPTURE:
├── Branded hashtag for customers
├── Weekly DM outreach to customers who post organically
├── Permission workflow: spot → contact → approve → feature → attribute
├── Best customer content enters the ad creative pipeline
└── Top customers invited to external creator network
```

---

## Step 6: Output Schema — Commerce Integration Blueprint

```
BRAND: [Name]
E-COM PLATFORM: [Platform]
MONTHLY CONTENT VOLUME: [N pieces]
CURRENT CONTENT-ATTRIBUTED REVENUE: $[N] (or "unknown")

LAYER 1 — TAGGING:
├── % of content currently tagged: [X%]
├── Target: [Y%]
├── Gap: [What needs to change]
└── Timeline: [Weeks to implement]

LAYER 2 — AI DISCOVERY:
├── Current state: [None / Basic / Advanced]
├── Tool selection: [Which AI commerce tool]
├── Training data sources: [Listed]
└── Timeline: [Weeks to implement]

LAYER 3 — AUTONOMOUS CHECKOUT:
├── Current friction points: [Listed]
├── Solutions: [Listed]
├── Tech requirements: [Listed]
└── Timeline: [Weeks to implement]

POST-PURCHASE LOOP:
├── Current state: [None / Basic sequence / Full loop]
├── Gaps: [Listed]
└── Implementation plan: [Listed]

MEASUREMENT:
├── Key metrics: [From Step 4]
├── Reporting cadence: [Weekly/monthly]
└── Owner: [Who tracks this]

BUDGET:
├── Tools: $[N]/month
├── Implementation: $[N] one-time
└── Ongoing operations: $[N]/month
```

---

## Quality Gate

- [ ] All 3 layers (Tagging, AI Discovery, Autonomous Checkout) state BOTH current state and target — never target-only
- [ ] Content-attributed revenue is a real number or explicitly flagged "unknown" — never left blank
- [ ] The AI shopping agent's "Cannot" boundaries are named (no unauthorized discounts, no off-catalog promises)
- [ ] Post-purchase sequence covers Day 0 through Day 60, not just the unboxing moment
- [ ] Every layer carries a timeline in weeks, not "TBD"

---

## Stacking

| After This Workflow | Stack With | For |
|:-------------------|:-----------|:----|
| Need better product content | `/oren-signature-series` | Product-focused series |
| Need conversion copy | `/storybrand-copy` | Messaging on PDPs |
| AI agent needs training | `/knowledge-alchemy` | Knowledge base build |
| Post-purchase content loop | `/oren-creator-network` | Turn customers into creators |
| Full flywheel check | `/oren-content-flywheel` | Verify all connections |
