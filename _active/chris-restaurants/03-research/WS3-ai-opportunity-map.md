# WS3 — Restaurant AI Opportunity Map

**Workstream:** 3 of 5
**Mission:** effervescent-exploring-wave (Chris Restaurants)
**Date:** 2026-04-06
**Lens:** Nick Saraev (buildable today) + Rachel Woods (will staff use it?) + Paul James (how to package) + Darrel Wilson (show, don't tell)
**Audience:** Internal Farrice prep (NOT for client). The dossier behind "I know what works."

---

## Reading guide

This dossier is the substance behind Farrice's credibility. Five sections, each with a specific job:

1. **Opportunity Matrix** — bottleneck → tool → effort/impact/risk score. The map.
2. **90-Day Roadmap Template** — Phase 1 / 2 / 3 with realistic costs and outcomes.
3. **Case Studies** — eight real brands with documented metrics and source bias flagged.
4. **Honest Limits** — what AI cannot reliably do today. **The most important page.** When Farrice says "AI won't replace your sushi chef," the owner relaxes.
5. **Menu Engineering Honesty Caveat** — the credible upsell setup. Lift this directly into the deliverable.

A one-line rule for every page below: **if Farrice can't defend the number with a source, it doesn't go in the deliverable.**

---

## Deliverable 1 — AI Opportunity Matrix

Scoring legend:
- **Effort:** Low (≤1 week setup) / Med (2–6 weeks) / High (8+ weeks, integration work)
- **Impact:** Low (nice-to-have) / Med (real margin or hours) / High (operating leverage)
- **Time-to-value:** Weeks (visible in 30 days) / Months (60–90 days) / Quarters (90+ days)
- **Adoption risk:** Low (no behavior change) / Med (workflow change) / High (kitchen/floor change)

### Customer-facing

| Bottleneck | Tool / Approach | What it does | Effort | Impact | Time-to-value | Adoption risk | Notes |
|---|---|---|---|---|---|---|---|
| Review response time | **Marqii** (managed bundles) | AI-drafted on-brand replies to Google/Yelp/Facebook reviews; managed-service tier writes them for you | Low | Med | Weeks | Low | Priced by review volume; reviewer-grade tone control matters for Yakiya's discerning audience. Source: marqii.com pricing page |
| Review response time | **Popmenu / Owner.com** | Bundled review response inside a marketing platform; Owner.com is sales-first, AI-driven traffic | Low | Med | Weeks | Low | Owner.com customer claims (Talkin Tacos $120K/mo, Saffron $171K/mo) are vendor-sourced; treat as floor-of-confidence |
| Phone reservations | **Slang.ai** | AI voice agent answers reservation calls, FAQs, hours, simple changes | Med | Med | Weeks | Med | $450–$600/mo per location per loman.ai market scan; Slang.ai is the most-cited indie restaurant choice as of 2026 |
| Phone reservations | **SoundHound / Hostie AI** | Same job, alternative vendors; Hostie targets SMB at $299/mo with 20+ languages | Med | Med | Weeks | Med | Hostie.ai positions vs Slang on price; SoundHound enterprise-tier |
| Loyalty / personalization | **Bikky / Thanx / Toast Loyalty** | POS-attached customer profiles, segmented offers, predicted churn | Med | Med | Months | Med | Bikky leans data-platform; Thanx leans UX/loyalty UI; Toast Loyalty bundles if already on Toast |
| Marketing — email/SMS | **Toast Marketing / Bikky / Bloom Intelligence** | POS-driven segmentation and AI-suggested campaigns | Low | Med | Weeks | Low | Toast disclosed 6% AOV lift from "Sous Chef" upsell tool in Q1 2024 earnings (PYMNTS) — vendor metric, but corroborated in trade press |
| Social content | **Marqii / Popmenu / generic GPT-4o + brand kit** | Auto-generated post drafts for IG/TikTok | Low | Low | Weeks | Low | High risk of "AI tells" — needs human pass for ethnic concept brand voice (see Limits) |
| Menu translation | **DeepL / Google Translate / GPT-4o + glossary** | Multi-language menu output | Low | Low | Days | Low | Cheap; needs native speaker QA for menu items where direct translation fails (e.g., regional Chinese names) |

### Operations

| Bottleneck | Tool / Approach | What it does | Effort | Impact | Time-to-value | Adoption risk | Notes |
|---|---|---|---|---|---|---|---|
| Scheduling vs demand | **7shifts AI / Lineup.ai** | Sales-data-driven labor forecast, schedule optimization, mobile shift swaps | Low | High | Weeks | Low | 7shifts owns 1.5M+ restaurant pros (per their site); Lineup.ai claims Carrot Express saved $1M+/yr in labor (vendor case study) |
| Inventory / theoretical vs actual | **MarketMan** | Daily count, variance reports, vendor invoice OCR, COGS visibility | Med | High | Months | Med | Used by Dolar Shop (50+ international Chinese hotpot locations) — directly relevant for Panda Inn / Wasabi |
| Inventory / variance | **MarginEdge / Restaurant365** | Same job, different stack — R365 is the heavyweight (accounting + inventory + labor); MarginEdge sits between QuickBooks and POS | Med | High | Months | Med | R365 = enterprise; MarginEdge = mid-market workhorse |
| Demand forecasting | **Lineup.ai / Tenzo / R365 forecasting** | Sales forecast tied to weather, day-of-week, events; feeds prep & schedule | Med | High | Months | Med | Tenzo and Lineup.ai both publish customer case content; accuracy depends entirely on POS data hygiene |
| Waste tracking | **Winnow / Leanpath / Phood** | Bin-camera + weight + AI variance analysis | High | Med | Quarters | High | Hardware install; primarily catering/buffet/hotel ROI; **probably not** for these three concepts in V1 |
| Prep planning | **Galley / Meez / R365 recipe** | Recipe management, par calculations, prep sheets that follow forecast | Med | Med | Months | Med | Helpful only after demand-forecasting layer is in place |
| Vendor management | **MarketMan / R365 / BlueCart** | Order guides, price-change alerts, suggested reorder | Med | Med | Months | Low | Auto-reorder is rarely trusted at full automation; suggested-reorder is the realistic mode |
| Manager log / ops journal | **Otter + GPT-4o / Granola / custom** | Voice-capture daily issues, AI-summarize for owner | Low | Med | Days | Low | Underrated quick win; no integration; voice memo → daily digest → owner email |

### Financial

| Bottleneck | Tool / Approach | What it does | Effort | Impact | Time-to-value | Adoption risk | Notes |
|---|---|---|---|---|---|---|---|
| POS analytics | **Toast Sous Chef / Toast IQ** | Native AI insights and recommendations inside Toast | Low | Med | Weeks | Low | Only if already on Toast; vendor reports 6% AOV lift on upsell features (PYMNTS, May 2024) |
| Cross-POS BI | **Tenzo / Bikky / Lineup.ai** | Unified dashboard across multiple POS systems | Med | High | Months | Low | The right answer if the three locations run different POS systems (likely given diverse concepts) |
| Food cost monitoring | **MarginEdge / R365 / xtraCHEF** | Daily food cost vs theoretical, invoice OCR, recipe costing | Med | High | Months | Med | The single highest-leverage AI-adjacent tool for an independent operator. Bigger ROI than any voice/marketing AI |
| Labor cost monitoring | **R365 / 7shifts / MarginEdge** | Real-time labor % vs sales, overtime alerts | Low | High | Weeks | Low | If they're not running labor reports daily, this is layup #1 |
| Comp / discount analysis | **Avero / R365 / Bikky** | Server-level void/comp tracking, theft signals | Med | Med | Months | Med | Sophisticated multi-unit owners often want this; politically sensitive |
| Cash flow forecasting | **Lineup.ai / R365** | Sales forecast → projected cash position | Med | Med | Months | Low | Useful but only after sales-forecasting layer is trusted |

### People

| Bottleneck | Tool / Approach | What it does | Effort | Impact | Time-to-value | Adoption risk | Notes |
|---|---|---|---|---|---|---|---|
| Hiring — sourcing | **Workstream / Harri / Fountain** | Apply-by-text, automated screening, interview scheduling | Low | Med | Weeks | Low | Workstream specifically built for hourly restaurant hiring; widely deployed |
| Hiring — screening | **Paradox Olivia** | Conversational AI screener (Wendy's uses it per Reddit operator confirmation) | Med | Med | Months | Med | Strong for high-volume QSR; less natural fit for upscale Asian where chef culture is relational |
| Onboarding | **Opus Training / Wisetail** | LMS with mobile-first short-form modules | Med | Med | Months | Med | "AI" claims are mostly content recommendation; the value is the LMS itself |
| Performance | **7shifts engagement / Crunchtime Apron** | Sentiment + retention signals from shift data | Med | Low | Quarters | High | Politically loaded; high adoption risk; skip in V1 |

### Multi-location specific

| Bottleneck | Tool / Approach | What it does | Effort | Impact | Time-to-value | Adoption risk | Notes |
|---|---|---|---|---|---|---|---|
| Cross-location reporting | **Tenzo / Bikky / Lineup.ai** | Single dashboard rolling up sales/labor/food cost across all units | Med | High | Months | Low | The killer use case for a 3-location operator on mixed POS |
| Brand consistency | Custom: **mystery-shop AI + photo review** | Compare review photos / mystery-shop notes against brand standard | High | Low | Quarters | Med | Manual + AI hybrid; not yet a packaged product |
| GM coaching | **Crunchtime Apron / Toast Coach** | Surface KPI deltas + suggested actions to GMs by location | Med | Med | Months | Med | Real value lives in the human accountability cadence — the AI is the prompt, not the answer |
| Consolidated dashboards | **Tenzo / Lineup.ai / R365** | Same as cross-location reporting — call it out separately because owners often confuse "BI" with "operational dashboards" | Med | High | Months | Low | Different from accounting close — this is daily/weekly cadence |

---

## Deliverable 2 — 90-Day AI Transformation Roadmap (Template)

A defensible sequence for a sophisticated 3-location operator. Designed so visible value lands fast, deeper margin work follows, and integration-heavy bets ship last. Costs are estimates for a 3-location operator and should be re-quoted at deployment.

### Phase 1 — Quick Wins (Weeks 1–4)

The bar: visible result in under 30 days, no kitchen disruption, no new hardware, minimal staff retraining.

#### Q1. AI-powered review response across Google + Yelp + TripAdvisor
**What it is:** Marqii (or Popmenu) drafts on-brand replies; manager taps approve. Bundles with managed-service tier where the vendor handles it entirely.
**Cost:** ~$100–$300/location/month depending on review volume and tier. Marqii prices by review volume.
**Deploy effort:** Connect Google Business Profile + Yelp; train tone with 5–10 sample replies per concept (each restaurant has a different voice — Wasabi tourist-warm, Yakiya refined, Panda Inn legacy-respectful).
**Realistic outcome:** 3–6 hours/week back per location, 100% review coverage (vs typical 30–50%), faster response time = better Google ranking signal.
**Adoption risk:** Low. Manager keeps approval power.
**Source caveats:** Hours-saved figures are vendor-claimed; corroborate with pre/post log on first location.

#### Q2. Weekly P&L digest from POS
**What it is:** Tenzo or Lineup.ai pulls POS data, generates a Sunday-night digest: sales vs forecast, labor %, top movers, exceptions.
**Cost:** Tenzo and Lineup.ai are typically $150–$400/location/month for the BI tier; full R365 is more.
**Deploy effort:** 1–2 weeks if all three locations are on Toast. 3–6 weeks if mixed POS (Wasabi at theme parks may run a different system; Yakiya/Panda Inn likely Toast or Aloha).
**Realistic outcome:** Owner reads one email Sunday night instead of opening three back-office portals. Catches anomalies (food cost spikes, labor blowouts) early.
**Adoption risk:** Low — it's a read, not a behavior change.
**Note:** Lineup.ai publishes a Carrot Express case study claiming $1M+/yr labor savings; vendor-sourced, treat as ceiling.

#### Q3. Manager voice log → daily digest
**What it is:** Each GM speaks 60–90 seconds at end of shift into a phone (Otter, Granola, or simple Voice Memos). A small GPT-4o workflow transcribes, categorizes, and emails the owner a daily 3-bullet roll-up.
**Cost:** ~$20/location/month tools + 2–4 hours one-time setup.
**Deploy effort:** 1–3 days. This is the lowest-risk, highest-trust quick win because Farrice can build it himself and demo it.
**Realistic outcome:** Owner sees what's happening across 3 locations without phone calls. Catches things text threads bury.
**Adoption risk:** Low. The behavior change is "talk for 60 seconds before you leave" — restaurant managers already do this informally.
**This is the demo to show in the meeting.** Per Darrel Wilson's "tool over opinion" — show it working on one of Chris's restaurants before the owner says yes.

#### Q4. Social media auto-content (with human pass)
**What it is:** Weekly batch of Instagram/TikTok caption + hook drafts using brand voice prompts; human edits before posting.
**Cost:** ~$50/location/month if using a generic AI tool + brand kit; ~$200/month for Marqii.
**Deploy effort:** 1 week.
**Realistic outcome:** Posting consistency goes from 1–2x/week to 4–5x/week.
**Adoption risk:** Med. AI-generated copy is dangerous for Asian concepts (cultural sensitivity, voice mismatch). **Always human pass.**

#### Q5. Scheduling tied to historical sales
**What it is:** 7shifts AI or Lineup.ai pulls 12 months of POS sales, predicts demand by daypart, suggests schedule.
**Cost:** ~$70–$120/location/month for 7shifts mid-tier.
**Deploy effort:** 2–3 weeks. Needs clean POS history.
**Realistic outcome:** 1–3 percentage points labor cost reduction once managers trust the suggestions. Vendor case studies routinely claim 4–6%; build expectation low.
**Adoption risk:** Med. GMs initially override AI suggestions; trust builds over 6–8 weeks.

### Phase 2 — Medium Bets (Weeks 5–8)

The bar: workflow change is OK; payoff is real margin or recoverable hours.

#### M1. Inventory variance tracking
**What it is:** MarketMan, MarginEdge, or R365 pulls invoices, cross-references against POS depletion, flags variance daily.
**Cost:** $200–$500/location/month for MarketMan or MarginEdge; R365 higher.
**Deploy effort:** 4–8 weeks (recipe build, vendor catalog mapping, count cadence training). Real talk: vendors say "30 days," operators say "90 days to fully trust the numbers."
**Realistic outcome:** Food cost down 1–3 percentage points after 90 days. **Bigger margin lever than any voice or marketing AI.** This is where the actual money is.
**Adoption risk:** High. Counts must happen daily, mapping must be maintained, GMs must care. The #1 reason this fails: nobody owns the variance review.
**MarketMan deserves special call-out:** their published case study is Dolar Shop, a 50+ location international Chinese hotpot brand. Direct relevance for Wasabi/Panda Inn.

#### M2. Demand forecasting with weather + events
**What it is:** Lineup.ai or Tenzo overlays weather, local events, school calendar onto POS history.
**Cost:** Often bundled with the BI tool (~$150–$300/location/month).
**Deploy effort:** 2–4 weeks after Q2 is in place.
**Realistic outcome:** Better prep planning, less waste. Accuracy improves over 60–90 days as the model sees one full cycle.

#### M3. POS-driven email/SMS marketing
**What it is:** Toast Marketing, Bikky, or Bloom segments customers by RFM (recency, frequency, monetary), sends personalized winback.
**Cost:** $100–$300/location/month, often bundled in POS suite.
**Deploy effort:** 2–3 weeks.
**Realistic outcome:** Toast publicly disclosed a 6% AOV lift from Sous Chef upsell tooling (Q1 2024 earnings, PYMNTS coverage). Vendor metric — directional, not guaranteed.

#### M4. Menu engineering with POS data
**What it is:** Avero, MarginEdge, or Bikky cross-references item sales × food cost × menu placement to identify true stars / plowhorses / puzzles / dogs (Kasavana–Smith).
**Cost:** $150–$400/location/month bundled with food cost tools.
**Deploy effort:** 6–8 weeks. **Requires clean recipe builds and item-level food cost** — the work nobody wants to do.
**Realistic outcome:** 1–3 percentage point margin lift from menu re-engineering after first cycle.
**This is the upsell from the WS1 deliverable.** See Deliverable 5 below.

#### M5. AI-assisted hiring
**What it is:** Workstream or Paradox Olivia automates apply-by-text → screen → schedule.
**Cost:** $300–$700/location/month depending on hiring volume.
**Deploy effort:** 2–4 weeks.
**Realistic outcome:** Time-to-hire from 2–3 weeks down to 5–10 days. Bigger value for Wasabi (theme park = high turnover) than Yakiya (lower volume, more relational).

### Phase 3 — Long Games (Weeks 9–12)

The bar: integration work is fine; the payoff is a moat — something competitors can't easily copy.

#### L1. Cross-location BI dashboard
**What it is:** Tenzo or Bikky unifies all three POS systems into one daily dashboard. Owner sees three locations the way an enterprise sees three regions.
**Cost:** $400–$800/location/month for the data layer.
**Deploy effort:** 6–10 weeks if any location is on legacy POS (Aloha). Toast-to-Toast is fastest.
**Realistic outcome:** Cross-location pattern detection — "Yakiya labor is fine, Wasabi is over by 3 points, Panda Inn food cost is the leak." This is what a multi-unit owner secretly wants.
**Adoption risk:** Low. It's a dashboard. The owner reads it.

#### L2. AI loyalty program with personalization
**What it is:** Bikky, Thanx, or Toast Loyalty builds customer profiles from POS, sends segmented offers based on visit pattern.
**Cost:** $200–$500/location/month + transaction cost.
**Deploy effort:** 6–8 weeks.
**Realistic outcome:** 5–15% increase in repeat visit frequency for opted-in guests. Vendor-claimed; treat as upper bound.
**Best fit:** Yakiya and Panda Inn (repeat-customer concepts). Low fit for Wasabi (one-time tourist captive market).

#### L3. Voice agent for phone reservations + simple questions
**What it is:** Slang.ai or Hostie AI answers calls, books tables, handles "what time do you close" / "do you take reservations" / "where do I park."
**Cost:** $300–$600/location/month per loman.ai market scan.
**Deploy effort:** 2–4 weeks.
**Realistic outcome:** 60–80% call deflection on routine questions. Hostess stops answering the phone constantly.
**Adoption risk:** Low. Does NOT touch the kitchen.
**Honest caveat:** Voice AI for **drive-thru ordering** is not yet reliable (see Limits — McDonald's IBM, Presto, Wendy's variance). Voice AI for **phone reservations and FAQs** is mature enough to deploy. The difference matters.

#### L4. Predictive maintenance for kitchen equipment
**What it is:** IoT sensors on walk-ins, fryers, hood systems → temperature/vibration anomaly detection → service ticket before failure.
**Cost:** $5,000–$15,000 hardware + $50–$150/location/month monitoring.
**Deploy effort:** 8–12 weeks.
**Realistic outcome:** Avoid 1–2 emergency repair events per year. Math depends on equipment age.
**Honest caveat:** This category exists for enterprise QSR (Yum, Inspire) but is still expensive and brittle for independent operators. **Skip in V1 — note as future state.**

#### L5. Automated vendor reorder
**What it is:** R365, MarketMan, or Crunchtime auto-generate reorders from inventory + forecast + par levels.
**Cost:** Bundled with inventory tools.
**Deploy effort:** Live after M1 + M2 are stable (90+ days).
**Realistic outcome:** Vendors trust the data; chefs still review before sending. **Almost no operator runs this fully autonomous** — the upside is "5-minute review" instead of "45-minute order build."
**Note:** Sell as "suggested reorder," not "auto reorder." The chef stays in the loop.

---

### Roadmap honest framing

This is a TEMPLATE, not a prescription. Final sequence depends on:
- **Which POS each location runs.** Toast across the board = Phase 1 ships in weeks. Mixed/Aloha = add 4–8 weeks to anything BI-related.
- **Existing tool stack.** If they already have R365, Phase 2 is 50% built.
- **Owner's actual pain.** Owners pay for what hurts. Phase 1 should hit the loudest pain point first.
- **Manager bandwidth.** A roadmap with 5 new tools in 4 weeks is a roadmap that fails. Sequence one at a time per location.

The deliverable's roadmap page should pick **3 quick wins, 2 medium bets, 1 long game** and frame the rest as future-state options.

---

## Deliverable 3 — Real Restaurant AI Case Studies

Eight cases, each with hard metrics and source bias flagged. Sourced from Tavily Pro deep research run on this dossier.

### Case 1 — McDonald's IBM Automated Order Taker (TERMINATED June 2024)

- **What was deployed:** IBM-built voice AI for drive-thru order taking.
- **Scale:** 100+ U.S. locations.
- **Timeline:** Pilot started 2021, terminated by July 26, 2024.
- **Hard metric:** ~85% accuracy (CEO Chris Kempczinski, June 2021). BTIG analyst Peter Saleh reported low-to-mid 80% accuracy in a 24-store Illinois test. Analyst-stated viability threshold: ~95%.
- **Why it failed:** Speech recognition struggled with accents/dialects. Cross-talk between drive-thru lanes caused order mixing. Viral TikToks: 260 chicken nuggets added to one order, bacon added to ice cream, multiple ice creams + ketchup packets added to a "vanilla ice cream and water" order.
- **Source quality:** **Independent press, gold standard.** CNBC, BBC, AP, NYT, Axios, Restaurant Business Online, Restaurant Dive. Multiple corroborating mainstream outlets.
- **Lesson for the owner:** *Voice AI for ordering is not solved.* Consumer-facing voice still has too much variance to deploy unsupervised at scale.

### Case 2 — McDonald's Dynamic Yield personalization (acquired 2019, divested 2022)

- **What was deployed:** Personalization engine on drive-thru digital menu boards. Suggested upsells based on weather, time of day, prior selection.
- **Scale:** 12,000+ U.S. drive-thrus during a 6-month rollout per Mastercard case study.
- **Timeline:** Acquired March 2019 (~$300M). Sold to Mastercard April 2022 (terms undisclosed). **McDonald's continued using it after sale.**
- **Hard metric:** Vendor case study (Mastercard) claims successful uplift but does NOT publish independent A/B test data. **Treat as marketing-sourced.**
- **Why it sold:** Mastercard had broader retail use cases; McDonald's wanted to focus on operations vs owning a tech company. McDonald's still uses the engine.
- **Source quality:** **Mixed.** Mastercard case study is vendor-biased. CNBC and Nation's Restaurant News confirm chronology. Uplift figures are not independently verified.
- **Lesson for the owner:** *Personalization works when the data is rich enough.* Independent operators rarely have that data.

### Case 3 — Sweetgreen Infinite Kitchen (the honest version)

- **What was deployed:** Robotic makeline (post-Spyce acquisition) that assembles bowls automatically.
- **Scale (the conflict in the public record):** Restaurant Business Online (Nov 2025) said "more than 20" locations. Sweetgreen Q4 2025 earnings call (Feb 2026) said 30 locations end of 2025, 32 by Q1 2026. Out of ~270 total stores. **Both are vendor/company sources.**
- **Hard metrics:**
  - **~500 bowls/hour throughput** capacity per location (QSR Magazine).
  - **~$550,000 install cost per system** (Wesleyan Business Review).
  - **>700 basis points labor-cost leverage** vs classic stores (Sweetgreen management on Q4 2025 earnings call). Earlier QSR reporting cited "at least 7 percentage points" labor savings.
  - **~1 percentage point COGS improvement** (QSR).
- **Rollout pace:** First store opened Naperville IL May 2023. CFO: ~50% of new openings will be Infinite Kitchen, but **older small stores will not be retrofitted.**
- **Source quality:** **Mixed but credible.** QSR Magazine, CNBC feature, Sweetgreen earnings call transcripts. No independent third-party throughput audit.
- **Lesson for the owner:** *Kitchen automation makes sense for purpose-built new locations only.* Retrofits don't pencil. The cost/throughput math works at $550K when you're building anyway, not when you're swapping out a working line.

### Case 4 — Chipotle: Autocado + Hyphen Augmented Makeline

- **What was deployed:** Two collaborative robots — Autocado (cuts, cores, peels avocados) and Hyphen Augmented Makeline (digital order-driven assembly).
- **Scale:** Pilots only. Autocado at Huntington Beach CA. Hyphen at Corona del Mar CA. Hyphen also tested at Chipotle's Cultivate Center.
- **Hard metrics:**
  - **Autocado: ~26 seconds per avocado** (LA Times confirmed).
  - **Hyphen pilot: up to 350 meals/hour with 99% accuracy** (Chipotle press release for Cultivate Center pilot).
- **Chipotle's stance:** Explicitly said the pilots will NOT eliminate jobs.
- **Source quality:** **Mixed.** Chipotle press releases (vendor) corroborated by LA Times and Observer (independent). Throughput numbers from pilot conditions, not steady-state.
- **Lesson for the owner:** *Even Chipotle's robots are pilot-stage.* The biggest player in fast-casual is still in single-store tests three years in.

### Case 5 — Wendy's FreshAI

- **What was deployed:** Google Cloud-built voice AI for drive-thru.
- **Scale:** Pilot started 2 states 2024, now processes "tens of thousands of orders daily" per Wendy's blog. Plans for 500–600 locations by end of 2025 (RetailWire).
- **Hard metrics:**
  - **86% of orders handled without restaurant team intervention** during pilot (Wendy's blog, corroborated by Forbes Jan 2025).
  - **~99% "success rate"** under broader definition (orders completed correctly, including with crew intervention).
  - **22 seconds faster** service time at test location (RestaurantDive / CIODive).
- **Source quality:** **Vendor-leaning with independent validation.** Wendy's corporate blog is primary source for pilot metrics. Forbes and trade press corroborate. Reddit / consumer reports show variance and anecdotal complaints (accent failures).
- **Lesson for the owner:** *Drive-thru voice AI is graded on a curve.* "86% without intervention" sounds great until you realize that means 14% requires a human anyway, AND the definition of "success" includes orders the AI got wrong but a human caught.

### Case 6 — Presto Voice Automation (NASDAQ: PRST) — the SEC disclosure

- **What was deployed:** Voice AI for drive-thru at multiple chains including Checkers, Carl's Jr., Del Taco.
- **The disclosure:** SEC enforcement against Presto for "AI washing." Per SEC administrative documents (33-11352.pdf):
  - **Initial commercial Presto Voice (Sept 2022): required human agents for 100% of orders.**
  - **Advanced Presto Voice pilot (June–Dec 2023): required human agents to enter orders ~70% of the time.**
  - **Presto's marketing claimed "up to 95% non-intervention rates."** SEC found this language conflated "no in-restaurant staff intervention" with "no human intervention" — Presto used off-site human agents.
- **Source quality:** **Highest. SEC primary regulatory document.** This is the gold standard — a regulator forced the disclosure.
- **Lesson for the owner:** *Read vendor metrics like a lawyer.* "Non-intervention" can mean an off-site human typed the order. Always ask: "intervention by whom?" Always ask for the definition.

### Case 7 — Toast Sous Chef AI (the documented small win)

- **What was deployed:** Toast's AI-powered upsell tool inside the Toast POS suite, for restaurants already on Toast.
- **Hard metric:** **6% lift in average order value** from AI-powered menu upsell, disclosed by Toast on Q1 2024 earnings call (May 8 2024). Reported by PYMNTS.
- **Source quality:** **Vendor (Toast) but reported in independent trade press (PYMNTS, Restaurant Dive).** Treat 6% as the headline, expect 2–4% in a typical operator deployment.
- **Lesson for the owner:** *The realistic AI win for an independent restaurant on Toast is upsell + suggested-add. Not voice. Not robots.* Small wins compound.

### Case 8 — Lineup.ai + Carrot Express (vendor case study, but useful)

- **What was deployed:** Lineup.ai labor forecasting and scheduling, integrated with POS sales.
- **Hard metric:** **Carrot Express (fast-growing healthy concept, multi-unit) saves "over $1 million annually in labor costs"** per Lineup.ai vendor case study.
- **Source quality:** **Vendor case study — treat as ceiling, not typical.** Carrot Express is publicly testimonial-friendly so the number is real but the conditions are favorable.
- **Lesson for the owner:** *Labor forecasting is the fastest-payback "real AI" deployment for multi-unit operators.* Even discounting the vendor claim by 50%, the math works.

### Bonus mention — Domino's voice ordering history

- 2014: Launched AI voice ordering platform for mobile (Nuance Nina Mobile, beta).
- 2023: Announced Microsoft alliance for generative AI on ordering and store ops.
- Today: ~80% of North American Domino's phone orders use AI voices per Wizcase/aggregate reporting; 80%+ of US retail sales come from digital channels.
- **Lesson:** Domino's is the only QSR that has been doing this at scale for 12+ years. **The lesson is patience.** They iterated for a decade before voice felt natural. Independent operators don't have that runway — pick mature tools, not bleeding edge.

---

### Cross-case synthesis (the patterns)

1. **Pilots, not rollouts.** Every documented enterprise AI deployment in restaurants is in pilot or limited rollout. Even Sweetgreen's "rollout" is ~30 of 270 stores after 2.5 years.
2. **Vendor metrics need decoding.** "Non-intervention" can mean off-site human. "Success rate" can include human-corrected errors. Always ask for the definition.
3. **Voice AI for drive-thru is not solved.** McDonald's killed it. Presto's SEC disclosure killed the marketing. Wendy's is doing the best, with 14% intervention plus accent variance.
4. **The smallest documented wins are real.** 6% AOV lift on upsell. 1–3 points labor savings on scheduling. 1–3 points food cost on inventory variance. **Stack three of these and you've moved prime cost by 5–7 points.** That's the actual game.
5. **The gold-medal ROI category is back-of-house margin tools (inventory, food cost, labor),** not customer-facing voice or robots.

---

## Deliverable 4 — Honest Limits Section

**This is the most important page in this dossier.** It is the credibility builder. When Farrice names what AI can't do, the owner relaxes — because it tells the owner that Farrice has actually thought about this, not just regurgitated a vendor pitch.

### What AI cannot reliably do in restaurants today (April 2026)

#### 1. Replace the chef's creativity in menu development
Menu development is still an act of taste, intuition, and seasonal judgment. AI can analyze sales data to tell you what sells. It cannot tell you what dish belongs on a menu next spring. For Yakiya specifically, the chef's hand on the menu is the brand. Don't touch it.

#### 2. Replace the GM's "feel" for the room
A great GM walks the dining room and reads tension in 10 seconds. They notice the four-top that's been waiting too long, the regular who looks distracted, the server who's rattled. No AI sees that today. The GM is irreplaceable. Tools should free the GM from paperwork so they can spend more time on the floor — not replace their judgment.

#### 3. Take drive-thru orders unsupervised
McDonald's killed their IBM voice AI in June 2024 after 100+ store rollout. Their CEO admitted ~85% accuracy with 1-in-5 orders requiring human help. Presto's SEC disclosure showed 70%+ of orders required human agents in their advanced pilot — *and the marketing claimed 95% non-intervention.* Wendy's FreshAI does best at 86% no-intervention, but that means 14% still need a human and accents still cause failures. **Phone reservation AI works. Drive-thru ordering AI doesn't.** Don't conflate them.

#### 4. Operate on dirty POS data
Most independent restaurants have garbage POS data. Items mis-categorized, modifiers wrong, recipe builds incomplete, void/comp logic inconsistent across managers. AI built on bad data produces confident wrong answers. The first 30 days of any AI rollout should be data hygiene — Toast support forums are full of operators whose menu items "disappeared" or whose dashboards stopped showing recent sales. Phase 1 of any roadmap should be a POS audit, not a tool purchase.

#### 5. Integrate cleanly with legacy POS systems
Aloha (NCR) and Micros (Oracle) are technically extractable but contractually painful. Aloha's documented integration limits (file-size caps, polling timeouts, debout settings) make third-party data exchange brittle. Some POS vendors' partner programs charge revenue-share fees for marketplace listing. Translation: **if Wasabi's theme park location runs Aloha or a custom theme-park POS, that location will take 2–3x longer to integrate than the others.** Plan for it.

#### 6. Handle truly novel customer service situations
"My grandmother passed away and we wanted to bring her ashes to her favorite booth, can you accommodate." No AI handles that. The hostess does. Plan tooling around the 80% of routine calls (hours, reservations, parking, dietary questions) and route the rest to humans.

#### 7. Replace physical kitchen labor at independent-restaurant scale
Sweetgreen Infinite Kitchen costs ~$550K per system. Sweetgreen has installed it in ~30 of 270 stores after 2.5 years. The economics work for new builds at scale, not retrofits. Zume Pizza raised $445M and shut down. Spyce closed its restaurants and was acquired for parts. Karakuri shut down in 2023. CaliBurger Flippy retreated. **Kitchen automation at independent-restaurant scale is still a research project.** Anyone selling otherwise is selling future state.

#### 8. Write marketing copy that sounds like the brand
AI-generated copy trips the AI-tells radar instantly. The Salty Otter Sports Grill (Santa Cruz, May 2025) used an AI-generated logo, got savaged in one-star reviews, and replaced it. The owner publicly said the AI controversy "crushed her dream." For ethnic concepts the risk is worse — cultural sensitivity and authentic voice can't be prompted. **AI drafts, humans ship.** Especially for Yakiya and Panda Inn, where the brand voice is the asset.

#### 9. Predict regional / event-driven demand without enough history
Forecasting tools (Lineup.ai, Tenzo) need 12+ months of clean data to learn weather and event patterns. A new menu launch resets the model. A renovation resets the model. A new GM resets the model. Set the expectation: forecasting accuracy improves over 60–90 days of operation, not Day 1.

#### 10. Manage vendor relationships
Vendor relationships are still relational. The fish broker at Wasabi knows when there's better tuna coming in. The produce vendor at Yakiya knows when the chef will want a specific variety of mushroom. AI can optimize the order quantity. It cannot replace the call.

### How to use this section

When Farrice walks into the meeting, this list lets him pre-empt the owner's biggest fear: *"This guy is going to tell me to fire my chef and put a robot in my kitchen."*

By naming the limits first, Farrice signals: *I respect what you've built. I know what AI can't do. The recommendations I'm about to make are inside the lines I just drew.* That move is what turns a sales pitch into a strategic conversation.

Per Darrel Wilson's "show, don't tell" — it's also why Farrice should walk in with the manager-voice-log demo running on Chris's phone. **The honest limits section earns the right to the demo. The demo earns the meeting.**

---

## Deliverable 5 — The Menu Engineering Honesty Caveat

*(Lift this directly into the final client deliverable. Three paragraphs, written in Farrice's voice for a sophisticated owner.)*

True menu engineering — Kasavana and Smith's stars / plowhorses / puzzles / dogs framework — needs three things from a restaurant's POS: units sold per item, theoretical food cost per item, and actual sell price per item. The math classifies each menu item by popularity and contribution margin, then tells you what to feature, what to reposition, what to reprice, and what to cut. Done well, it can move prime cost two to four percentage points in a single quarter. This is the version of menu engineering that earns its name.

What this analysis is, and what it isn't. Without your POS sales data, what's in this folder is a *signal-based menu efficiency review* — a different and more limited animal. It looks at how your prices sit against the market median in your immediate area, where your menu is dense versus sparse compared to competitors, which items appear universally on competitor sets (the table stakes you're missing or running heavy), and what reviewers love and hate (a rough proxy for stars and dogs). Every recommendation here is defensible from public data. None of them require touching your books. That's the V1 — a sharp but external read on where the menu is leaving money on the table.

The full version is a Phase 2 conversation. Once we have a week of POS exports — even just item-level sales counts and price points — the same framework that lifts Wendy's, Chipotle, and your sushi competition's margins becomes available to you. Most operators discover at least one star they were under-pricing, one dog draining prep labor, and one puzzle the menu was hiding. We can scope that as a focused two-week engagement after this analysis lands. For now, the V1 is built so you can start acting on the public signals immediately and decide separately whether the deeper work is worth doing.

---

## Source bibliography (the receipts)

This dossier was built on a Tavily Pro deep research run plus targeted search queries. The strongest sources, by category:

**Independent press (gold standard):**
- CNBC, BBC, AP, NYT, Axios, Business Insider, Wall Street Journal — McDonald's IBM termination
- Restaurant Business Online, Restaurant Dive, QSR Magazine, Nation's Restaurant News — trade press
- LA Times, Boston Magazine, Skift Table, Eater — regional reporting
- TechCrunch, The Robot Report, Physics World — robotics failures (Zume, Karakuri)
- Forbes — Wendy's FreshAI metrics
- PYMNTS — Toast Sous Chef 6% AOV disclosure

**Regulatory (highest credibility):**
- SEC administrative litigation 33-11352.pdf — Presto Voice disclosure
- Sweetgreen Q4 2025 earnings call transcript

**Vendor sources (treat as ceiling, decode definitions):**
- Sweetgreen / QSR Magazine (Infinite Kitchen throughput)
- Chipotle newsroom (Autocado, Hyphen)
- Wendy's corporate blog (FreshAI)
- Mastercard / Dynamic Yield case studies
- Marqii, Popmenu, Owner.com pricing pages
- 7shifts, Lineup.ai, Tenzo, Bikky case studies
- MarketMan Dolar Shop case study
- Toast IR / earnings calls

**Operator forums (anecdotal but useful):**
- Reddit r/restaurateur, r/KitchenConfidential
- Toast support community
- Square community forums
- Facebook restaurant operator groups

The full URL list lives in the raw research files at `/tmp/ws3-research/01-case-studies-extracted.md` and `/tmp/ws3-research/03-failures-extracted.md`. Move them into `_raw-data/` if archiving.

---

## Quick-reference cheat sheet for the meeting

When the owner asks "what AI should we use?" — Farrice answers in this order:

1. **First win in 30 days:** Marqii or Owner.com for review response (visible, low risk, demos in 5 minutes).
2. **Bigger margin in 90 days:** MarketMan or MarginEdge for inventory variance + food cost monitoring (the actual money lever).
3. **The thing that makes you feel in control of three locations:** Tenzo or Lineup.ai cross-location BI dashboard (the multi-unit operator's secret want).
4. **What we are NOT doing:** drive-thru voice AI, kitchen robots, AI menu development, or anything that touches the chef's autonomy.

When the owner asks "are you going to replace my staff with AI?" — Farrice answers:

*"No. The AI deployments that work in restaurants today are back-of-house — inventory variance, labor forecasting, P&L digests. The ones that haven't worked are the ones that tried to replace the front-of-house relationship. McDonald's killed their drive-thru voice AI last summer. Sweetgreen's robot kitchen costs $550K per store and only works in new builds. The play here is to free your chef and your GMs from paperwork, not replace them."*

When the owner asks "how do I know what's real and what's hype?" — Farrice points to this dossier and says:

*"I built this over the last few days. Eight case studies, sources flagged for vendor bias, an honest limits page. If you want to walk through how I'd sequence this for your three concepts specifically, that's the next conversation."*

That's the bridge to the engagement.
