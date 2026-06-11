---
description: "/meg-funnel-doctor — stage-isolated funnel diagnosis for e-com and POD stores. Each weak metric maps to ONE question, ONE failing stage, ONE fix. The panic move (rebuild the ad account) is almost always wrong."
---

# Funnel Doctor

A store owner watches ROAS drop to 1.4 and opens the ad account. Wrong room. The ad account is an echo chamber — it reflects a decision made three layers upstream, on a product page, a mockup, a cart that looks like a scam. This workflow refuses to touch the ad account until it has proven the problem actually lives there. "Most ROAS problems are actually Shopify problems disguised as ad problems." Six numbers. One failing stage. One fix. That is the entire diagnosis.

## Pre-Flight

Read these files before executing:
1. `skills/meg-heckman-buyer-trigger-os/genius.md` (Diagnostic Mechanics — the 6-metric table and symptom displacement)
2. `skills/meg-heckman-buyer-trigger-os/references/genius-patterns.md` (Patterns 15–16, Exemplar 4)

> **🔒 Pre-Flight Gate**: Before diagnosis begins, confirm which store context applies (POD/Shopify, Etsy/marketplace, SaaS trial, newsletter, or client audit deliverable). The 6 metrics must be mapped to their context-equivalent before any threshold is applied. Diagnosing with the wrong metric proxies produces confident wrong answers.

## Input Required

- The 6 core metrics (or best available): CPC, ROAS, Add-to-Cart %, Initiate Checkout %, Conversion Rate, AOV
- Store context: platform, product type, price point, traffic source
- Any known store characteristics (new vs. established, limited SKUs vs. catalog, mobile-dominant audience)
- Optional: recent changes (new designs, mockup swaps, pricing updates, ad creative changes)

Missing metrics get estimated or flagged — the diagnosis is only as good as the inputs. State confidence level explicitly when proxying.

---

## Workflow

### Step 1: Intake + Calibration Layer

Lay the 6 metrics against her calibration defaults. These are **POD/Meta 2026 defaults — not laws**. Recalibrate per category before applying.

| Metric | Default Healthy Range | The Single Question | Stage It Governs |
|---|---|---|---|
| CPC | $0.55–$0.75 | Does this creative make people stop? | Presentation / mockup |
| ROAS | 2.0 floor / 2.5–3.5 scale trigger | Dollars back per dollar spent? | Whole funnel — trace upstream first |
| Add-to-Cart % | 7–8% | Do they actually want it? | Product page (images, description, pricing, mobile CTA position) |
| Initiate Checkout % | 5–6% | Does this store feel trustworthy? | Cart-page trust (shipping clarity, reviews, returns, delivery window) |
| Conversion Rate | 3–4% | How easy is it to buy? | Checkout (friction, load speed, payment options, mobile) |
| AOV | $45+ | How much profit per order? | Collection cohesion + shipping structure |

"The rest of the metrics I simply ignore."

State each metric as either HEALTHY, MARGINAL (within 20% of floor), or WEAK. Flag any gaps: "IC% not tracked — proxying from platform analytics; confidence LOW."

---

### Step 2: Find the First Failing Stage

Diagnose in funnel order. Fix upstream before downstream ever gets touched. The order is not negotiable.

```
CPC → Add-to-Cart % → Initiate Checkout % → Conversion Rate → AOV → ROAS
```

The first metric that falls below its threshold is the diagnosis. Everything downstream of it is a symptom, not a cause. Mark the failing stage explicitly before proceeding:

> "First failing stage: [metric] at [value] vs. [default threshold]. Everything below this is noise until this is fixed."

If CPC is the only failing metric, the funnel is healthy from the click onward — the entire problem is presentation. If IC% fails but ATC% is healthy, the cart page is the room, not the checkout, not the ads.

---

### Step 3: Symptom-Displacement Check

Before naming a fix, run the displacement check. The sick number is frequently the echo, not the source.

ROAS is the most common echo metric. A ROAS of 1.4 reads as an ad problem. In most cases it is a conversion problem — and the conversion problem is usually a trust problem that lives on the cart page, or a presentation problem that lives on the mockup. "Most ROAS problems are actually Shopify problems disguised as ad problems."

Apply the displacement check to the first failing stage:

- CPC high → Is this a targeting problem, or a presentation problem? Default: presentation first. Same design, different mockup, retest one variable before touching audiences.
- ROAS low → Is this an ad problem, or a Shopify problem? Trace to the first funnel stage that is off-threshold — the answer is almost always there.
- ATC% low → Is this a desire problem, or a visibility problem? Check mobile CTA position before rewriting the description.
- IC% low → Is this a checkout problem, or a cart-page trust problem? The trust collapse happens before checkout opens.
- CVR low → Is this a friction problem, or a desire problem? Desire lives upstream; friction lives here.
- AOV low → Is this an upsell problem, or a catalog cohesion problem? Upsell apps require a catalog worth buying twice from.

State the displacement verdict before prescribing:

> "Displacement: this [ROAS] problem traces to [cart-page trust]. Fix the cart before the ad account."

---

### Step 4: Prescribe the ONE Stage Fix

One fix per diagnosis. Never a list of ten. The fix names the failing stage before naming the action.

**CPC HIGH — Stage: Presentation**
The mockup swap is the first move, not the last. "We ended up swapping the mockup and reran our tests. And it showed the exact same design on a different mockup and the CPCs immediately started to come down. That told us that the issue was not Meta or the ad account, it was an issue with our presentation." One variable isolated. Same design, different presentation, retest. Targeting adjustments come only after a mockup swap fails to move CPC.

**ATC% LOW — Stage: Product Page**
Check in order: primary image quality → mobile CTA position → price relative to perceived value → description clarity. She audits "where my add to cart button actually lands on a mobile device." Button below the fold on mobile is a position problem, not a conversion problem.

**IC% LOW — Stage: Cart-Page Trust**
The trust gate is the cart, not the checkout. IC% collapsing means the store failed a legitimacy test before the buyer ever opened checkout. Checklist: shipping cost visible, return policy present, reviews present, delivery window stated. Fixing any one of these can recover IC% without touching checkout or ads.

**CVR LOW — Stage: Checkout**
Friction, load speed, payment options, mobile checkout flow. The one stage where technical fixes are the actual fix — not creative, not audiences, not mockups. Reduce steps, add Shop Pay or PayPal, test load time on mobile.

**AOV LOW — Stage: Collection Cohesion**
Shipping arbitrage only works when the catalog earns a second item in the cart. "You want designs that people naturally want to buy together." Collection cohesion — designs that belong in the same identity set — comes before any upsell app installation. If the catalog is incoherent, an upsell app surfaces random products and converts nothing. Route to `/meg-aov-architect` for the full collection architecture workflow.

**ROAS LOW WITH HEALTHY UPSTREAM STAGES — Stage: Trace**
If CPC, ATC%, IC%, and CVR are all healthy but ROAS is soft: re-examine AOV and product margin. A 3% CVR at $32 AOV on a $12 product cost produces ROAS 2.1 with no room to scale. The math problem is not in the funnel.

---

### Step 5: Scale Call

ROAS 2.0 is the break-even floor, not a success signal. "If my ROAS is at two, I'm not making money. I'm just not losing it." Scaling triggers at 2.5+, with other stages healthy. At 2.5–3.5, with CPC, ATC%, IC%, and CVR all on-threshold: "I'm bumping my budgets."

State the scale verdict explicitly:

> ROAS [value] — [HOLD / SCALE / INVESTIGATE] — reason: [one sentence]

Do not call a 2.1 ROAS "working." Call it "at floor — no losses, no margin for error, not a scale signal."

---

### Step 6: All-Clear Reroute

If all six stages are healthy and the funnel is still not profitable, the problem is upstream of the funnel. A healthy funnel cannot save a product without a trigger. Route to `/meg-trigger-audit`.

> "The funnel can't save a poster. All six metrics are on-threshold — the diagnosis is not in the funnel. The design has no trigger. Run `/meg-trigger-audit` before returning to diagnostics."

---

## Context Adaptations

| Store Type | Adaptation |
|---|---|
| POD / Shopify | Full workflow as-is; all 6 defaults apply |
| Etsy / marketplace | CPC = promoted listing CPC; IC% + CVR often merge — state proxy confidence; cart-page control limited, fix narrows to image and pricing |
| SaaS trial funnel | ATC% = trial starts; IC% = upgrade page views; CVR = paid conversions; AOV = MRR. Defaults don't apply — establish category baseline first |
| Newsletter funnel | ATC% = opt-in; IC% = purchase page visit; CVR = buyer conversion. Stage logic holds; defaults don't |
| Client audit deliverable | 2-page max: metric table with RAG status → displacement verdict → one failing stage → one fix. Client gets a diagnosis, not a workshop |

---

## Output Format

```
FUNNEL DOCTOR DIAGNOSIS — [store/project] — [date]

METRIC INTAKE
| Metric | Reported | Default | Status |
|---|---|---|---|
| CPC | | $0.55–0.75 | |
| ROAS | | 2.0 floor / 2.5 scale | |
| ATC% | | 7–8% | |
| IC% | | 5–6% | |
| CVR | | 3–4% | |
| AOV | | $45+ | |

Note: Defaults = POD/Meta 2026 calibration. Recalibrated for [context] as follows: [any adjustments or N/A]

FIRST FAILING STAGE: [metric] — [value] vs [threshold]
Everything downstream is noise until this is fixed.

DISPLACEMENT CHECK: [this problem traces to / does not trace to] [cause]

STAGE FIX: [stage name before fix name]
[One concrete action. Mockup swap, cart checklist, CTA position, checkout audit, collection cohesion, or route to /meg-aov-architect.]

SCALE CALL: ROAS [value] — [HOLD / SCALE / INVESTIGATE]
[One sentence reason]

NEXT: [/meg-trigger-audit if all-clear / /meg-aov-architect if AOV stage / return with swapped mockup data]
```

---

## Quality Gate

- One fix per diagnosis — never a list of options.
- Thresholds labeled as defaults for POD/Meta 2026, not universal laws.
- Mockup-before-targeting discipline honored for every CPC diagnosis.
- Cart-before-checkout discipline honored for every IC% diagnosis.
- Fix names the failing STAGE before naming the action.
- ROAS 2.0 is called a floor, not a success, every time.
- All-stages-healthy routes to `/meg-trigger-audit`, not to more funnel work.
- Scale verdict stated explicitly — no ambiguous "looks good."

## Common Pitfalls

- **Rebuilding the ad account on a presentation problem.** Opening the ad account before swapping the mockup is the single most common expensive mistake in this system. One mockup swap with one variable isolated answers the question in 48 hours.
- **Celebrating ROAS 2.1.** "I'm not making money. I'm just not losing it." The floor is not the win condition.
- **Fixing checkout when the cart is the leak.** IC% collapses at the cart page, not the checkout screen. The buyer failed the trust test before they got to payment.
- **Treating the thresholds as laws across categories.** A $200 AOV apparel store and a $35 POD store do not share the same ROAS floor. Calibrate per category; state when you are working from defaults.
- **Installing upsell apps before collection cohesion.** An incoherent catalog converts nothing twice. The app is not the problem; the catalog is.
