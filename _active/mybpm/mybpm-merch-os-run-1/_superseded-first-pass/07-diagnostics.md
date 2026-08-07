# Phase 5 — DIAGNOSE: Instrumentation + Pre-Committed Rules

> Thresholds = Heckman calibration defaults (POD/Meta 2026) — recalibrate after MyBPM's own first 2 weeks of data. Her figures: self-reported, UNCONFIRMED.

## Instrumentation Gaps (close before paid test)

| Gap | Action | Where |
|---|---|---|
| No Google Search Console (as of 2026-04) | Verify domain, submit sitemap | search.google.com/search-console |
| No Merchant Center | Connect Shopify → Google channel app | Shopify admin → Sales channels |
| Meta pixel/CAPI health | Confirm purchase events fire test-purchase | Meta Events Manager |
| Mobile CTA position | Physical phone check: where add-to-cart lands on PDP | Before any traffic |

## The 6 Numbers (weekly ritual — read in THIS order, fix the FIRST failing stage)

| # | Metric | Default healthy | The question | Where to read | If weak, fix THIS first |
|---|---|---|---|---|---|
| 1 | CPC | $0.55–0.75 | Does the creative stop people? | Meta Ads Manager | MOCKUP SWAP (same design, new presentation) — never rebuild targeting first |
| 2 | Add-to-Cart % | 7–8% | Do they want it? | Shopify analytics | PDP images, lead line, price display, mobile CTA |
| 3 | Initiate Checkout % | 5–6% | Does the store feel trustworthy? | Shopify | CART page: shipping cost clarity, delivery window, returns line, reviews block |
| 4 | Conversion % | 3–4% | How easy is buying? | Shopify | Checkout friction, load speed, payment options (Shop Pay on), mobile |
| 5 | AOV | $45+ | Profit per order? | Shopify | "Any 2 for $70" pair nudge; capsule cohesion (concepts already pair: #1+#2, #5+#1) — no upsell apps yet |
| 6 | ROAS | 2.0 = break-even floor · 2.5–3.5 = scale | Dollars back per dollar? | Meta | Almost always a stage-1–5 problem in disguise — trace upstream before touching the ad account |

## Pre-Committed Kill/Scale Rules (test slate — taste cannot veto data)

- **48h read 1** (per ad set): CPC >$1.20 with sane mockup → swap mockup, rerun 48h. CPC in range + ATC <4% → PDP problem, fix page not ad.
- **Day 4 verdict** (two reads): ROAS <1.0 → pause that concept's ads (concept stays live in store/email). ROAS 1.0–2.0 → hold budget, fix the first failing stage, one more 48h. ROAS ≥2.5 → scale +50% budget, queue wave-2 concept from the same world.
- **Day 10 capsule read**: any concept with organic/email sales but failed ads = presentation problem (new mockup/photography), not concept death. Zero sales anywhere on all 3 = sub-identity re-read (back to 01-ground.md candidate #2 or #3) — per the rule: a funnel cannot save a poster, and a poster verdict needs the person re-checked first.
- **The love clause**: if Farrice loves a concept the data kills — it gets ONE mockup swap, then it dies in ads. "The market does not care what you love. The market cares about what it loves."

## Factory Loop (install after first signal)

After day-10 read: set `/meg-factory-loop` cadence — generate (wave-2 concepts from the winning world, 4–6/month), test (one new ad set per 2 weeks, $15/day floor), scale-or-cut (rules above), email (2/week minimum: drop, story, pair-nudge rotation), repeat. Review ritual: Mondays, 15 minutes, the 6 numbers in order, one fix max per week.

## Run Ledger

- Phases complete: 0 GROUND ✓ · 1 CONCEPT ✓ · 2 SCORE ✓ · 3 LISTING ✓ · 4 LAUNCH PLAN ✓ · 5 DIAGNOSE ✓
- Awaiting Farrice: founder approval gate (phrases, price) · cost-gate approval for mockup generation
- Live store facts pulled 2026-06-10 via products.json (29 products, names/prices verified — VERIFIED) · Heckman method claims labeled per source-quotes ledger
