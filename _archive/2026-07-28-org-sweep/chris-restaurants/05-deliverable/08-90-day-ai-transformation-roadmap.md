# The 90-Day AI Transformation Roadmap
### What can actually ship in 90 days for the four legacy concepts, with the limits named first

**Audience:** Anyone reading this folder past the menu intelligence files
**Scope:** Wasabi at CityWalk, Yakiya Pasadena, Panda Inn Glendale, with applicability to Hibachi-San and the rest of PRG's specialty/non-Express portfolio
**Premise:** This is a roadmap of work that can be executed, not a vendor catalog. Every item below has a documented case study, a defensible cost range, and a known failure mode.

---

## Before the roadmap — the 1975 fact this document has to acknowledge

Peggy Tsiang Cherng holds a PhD in electrical engineering from the University of Missouri. Her dissertation built a pattern-recognition program that digitized X-rays to diagnose congenital heart disease. In 1975. When most people selling "AI for restaurants" today were not yet born. She customized the POS analytics for Panda Inn. **Panda Restaurant Group is, by any honest assessment, the most data-mature Asian restaurant family in America.** Andrea Cherng, Chief Brand Officer, built PRG's digital business team. PRG announced a $200M automation investment for 2025. Generic "AI for restaurants" framing is wrong on the facts and offensive in the room.

**This roadmap is not a pitch to introduce AI to a company that doesn't have it.** It is a sequenced set of operational interventions on the four orphaned legacy concepts that the corporate roadmap is mathematically constrained from prioritizing. Panda Express at 1,650 stores is where the corporate analytics team's quarterly attention has to live. That's not a critique of the team, it's arithmetic. The legacy concepts (Panda Inn, Yakiya, Wasabi, Hibachi-San) are emotionally protected and operationally orphaned by the same arithmetic. **The work below is the work that exists to be done at the scale where the corporate ROI math can't justify the analyst hours, until it can.** That's the side-quest specialist position. Everything that follows is built inside that frame.

---

## Phase 1 — Quick Wins (Weeks 1–4)

The bar for Phase 1: visible result in under 30 days, no kitchen disruption, no new hardware, minimal staff retraining, defensible math.

### Q1. Manager voice log → daily digest

**What it is:** Each GM speaks 60–90 seconds at the end of shift into a phone, Otter, Granola, or just Voice Memos. A small workflow built on GPT-4o transcribes, categorizes (people, food cost, customer, equipment, inventory, vendor), and emails the owner a daily three-bullet roll-up at 6 AM. Three locations become one email instead of three phone calls.

**Why this is item #1:** A working prototype of this exists. It can be demoed live on Chris's phone in 5 minutes during the first meeting. Per Darrel Wilson's "tool over opinion" rule. Show the thing working before anyone has to imagine it. The behavior change is "talk for 60 seconds before you leave," which restaurant managers already do informally. The trust curve on this is the steepest of any item in this roadmap.

**Cost:** ~$20/location/month in tools. 2–4 hours one-time setup work. Sub-$100/month total cost across three locations.

**Deploy effort:** 1–3 days.

**Realistic outcome:** Owner sees what's happening across three locations without phone calls. Catches the things that text threads bury. Builds a searchable archive of operational issues across the legacy concepts.

**Adoption risk:** Low.

**Honest caveat:** The categorization quality depends on the prompt design. Expect the first two weeks to need a tuning round as the categories miss things or over-trigger. By week 3 it stabilizes.

**Source bias:** The category "manager log + AI summarization" has no documented vendor case study because most vendors haven't built this yet. The math is back-of-envelope, not benchmark-validated. Defensible because the input cost is so small.

### Q2. AI-powered review response across Google + Yelp + TripAdvisor

**What it is:** Marqii (or Owner.com or Popmenu. Three viable vendors in this category) drafts on-brand replies to every Google, Yelp, and TripAdvisor review across all three locations. Manager taps approve. A managed-service tier is available where the vendor handles review response entirely. Useful when Chris is in the weeds.

**Three concept voices, three setups:** Wasabi gets a tourist-warm voice ("So glad you found us inside CityWalk!"). Yakiya gets a refined voice ("We deeply appreciate your time at our chef's tasting"). Panda Inn gets a heritage-respectful voice ("We've been honored to serve guests at this address since 1982"). Each voice is trained with 5–10 sample replies before launch.

**Cost:** $100–$300/location/month depending on review volume and tier. Marqii prices by review volume; their pricing page lists tiered packages.

**Deploy effort:** 2 weeks. Connect Google Business Profile + Yelp + TripAdvisor for each location. Train tone with samples. Test for two weeks before going live to managed-service tier.

**Realistic outcome:** 3–6 hours/week back per location on review-related work. **100% review coverage** (versus typical 30–50% for restaurants without a dedicated review-response process). Faster response times correlate with better Google ranking signal. Yakiya's discoverability gap (88 reviews after 10 years) is partly solved by closing the response loop on every existing review, which signals freshness to the algorithm and prompts more reviews from future guests.

**Adoption risk:** Low. Manager keeps approval power. Manager voice/quality control is preserved.

**Honest caveat:** Hours-saved figures are vendor-claimed. Corroborate with a pre/post log on the first location before scaling. Some Yelp reviews can't be responded to publicly due to platform restrictions; the workflow accounts for this.

**Source bias:** Marqii vendor pricing page (marqii.com/pricing). Owner.com customer claims (Talkin Tacos $120K/mo, Saffron $171K/mo) are vendor-sourced. Treat as floor of confidence.

### Q3. Weekly P&L digest from POS

**What it is:** Tenzo or Lineup.ai pulls POS data and generates a Sunday-night digest: sales versus forecast, labor percentage, top movers, exceptions, an "alerts" section for anomalies. The owner reads one email Sunday night instead of opening three back-office portals.

**Cost:** Tenzo and Lineup.ai are typically $150–$400/location/month for the BI tier. Restaurant365 is more (it's a full ERP, not just BI). Budget for $450–$1,200/month across three locations.

**Deploy effort:** 1–2 weeks for Yakiya and Panda Inn (assuming both run a modern POS). Wasabi joins after the W1 Digital Dining bridge ships in Phase 2. Until then, the Q3 digest covers the two cloud-POS concepts and Wasabi's data flows in once the bridge is live.

**Realistic outcome:** Owner catches food cost spikes and labor blowouts within 48 hours instead of waiting for the monthly close. Builds a daily/weekly cadence that doesn't currently exist for the legacy concepts (Panda Express has it; the legacy concepts don't get the same treatment).

**Adoption risk:** Low. It's a read-only email. No behavior change required.

**Honest caveat:** Lineup.ai publishes a Carrot Express case study claiming $1M+/year labor savings on a multi-unit fast-growing concept. **Treat as vendor-sourced and as a ceiling, not typical.** Realistic Phase 1 expectation: surface anomalies that would otherwise be discovered at the monthly close. The labor-savings number kicks in later when scheduling automation is layered on (Phase 2).

### Phase 1 honest sequencing

The three Phase 1 items can ship in the order above or in parallel. They don't depend on each other. The recommended sequence is **Q1 first** (because it's the demo asset), **Q2 second** (because review response generates the fastest visible improvement to Google sentiment), **Q3 third** (because the BI tooling depends on POS data hygiene that the other two items help surface).

### Phase 1 — Wasabi-specific note (read this before scoping Wasabi work)

> **Wasabi runs Digital Dining. Phase 1 at Wasabi is explicitly non-POS-integrated.**
>
> Digital Dining (Menusoft Systems / Heartland Payment Systems, late-1980s lineage) has no plug-and-play connector to modern AI restaurant tools. Owner.com, Marqii, Lineup.ai, MarketMan, and Popmenu all build for Toast / Square / Clover first and Digital Dining last, if at all. Building the Wasabi POS bridge is real engineering work and it lives in Phase 2 — see W1 below. In the meantime, every Phase 1 item ships at Wasabi without touching the POS:
>
> - **Q1 (Manager voice log → daily digest)**: input is voice memo, not POS data. Ships at Wasabi day one.
> - **Q2 (Review response automation)**: input is Google / Yelp / TripAdvisor APIs, not POS. Ships at Wasabi day one.
> - **Q3 (Weekly P&L digest from POS)**: ships at Yakiya and Panda Inn first while the Wasabi POS bridge is being scoped. Wasabi joins in Phase 2.
>
> Yakiya and Panda Inn can run the full Phase 1 stack in parallel. Wasabi runs the non-POS subset and waits for the bridge. This sequencing is deliberate, not a workaround — and it's also exactly why the side-quest specialist position exists. PRG corporate IT will not prioritize a Digital Dining bridge for a single location against a roadmap built around 1,650 Panda Express stores on modern infrastructure. The arithmetic doesn't justify it. That gap is the engagement.

---

## Phase 2 — Medium Bets (Weeks 5–8)

The bar for Phase 2: workflow change is okay; the payoff is real margin or recoverable hours.

### W1. Wasabi Digital Dining → analytics bridge (the named engineering deliverable)

**What it is:** A scoped engineering project to give Wasabi the same analytical visibility Yakiya and Panda Inn already have via their cloud POS systems. Three implementation paths, evaluated in this order:

1. **ODBC direct-to-database connection (preferred).** Digital Dining stores its data in a SQL database that's queryable via ODBC if Heartland's licensing tier permits. A read-only ODBC connection lets a downstream BI tool (Tenzo, Bikky, or a custom Python pipeline) pull item-level sales, ticket times, void/comp logic, and labor data on a daily cadence. This is the cleanest path. It also requires confirming Heartland's specific licensing terms for the Wasabi installation, which is a one-week procurement conversation, not a technical project.
2. **CSV / TSV export pipeline (fallback).** If the ODBC path is blocked by licensing, Digital Dining can export end-of-day reports to a watched folder. A small ETL job (cron + Python or a managed service like Stitch / Fivetran's flat-file connector) picks up the file, normalizes the schema, and pushes it into the same downstream BI layer. Higher latency than ODBC, but still daily, still defensible, still ships.
3. **Third-party middleware (third option).** Restaurant365, MarginEdge, or Avero all advertise Digital Dining support in their integration matrices. The cost is higher ($300–$800/month per location for the middleware layer alone) and the integration depth varies by vendor. This path is the right call if PRG wants to standardize the legacy concepts on a single back-office platform, but it's the most expensive path per dollar of analytical lift.

**Why this is a Phase 2 item, not Phase 3:** The non-POS Phase 1 work at Wasabi (voice log, review response, discoverability) ships visible value in 30 days. Phase 2 is where the bridge gets built so Phase 3's cross-location BI dashboard can include Wasabi as a peer to Yakiya and Panda Inn instead of as a footnote. Without this work, Wasabi stays operationally orphaned.

**Cost:** $3,000–$8,000 one-time engineering depending on which path runs, plus the middleware monthly fee if Path 3 is chosen. The ODBC path is the cheapest by a wide margin.

**Deploy effort:** 3–6 weeks. The first week is procurement-side (confirming Heartland licensing). Weeks 2–4 are the build. Weeks 5–6 are validation against the back-office terminal's own reports.

**Realistic outcome:** Wasabi gets the same daily P&L digest, the same item-level sales analytics, the same ticket-time visibility that Yakiya and Panda Inn have on day one of the engagement. The 14% 1-star bimodal review distribution can finally be cross-referenced against ticket-time data by daypart, which is the missing piece that turns Section 7 of the Wasabi menu file from observation into a measured, repeatable diagnostic.

**Adoption risk:** Low once built. Medium during build because integration projects with legacy POS systems frequently surface licensing surprises. Mitigation: run the procurement conversation with Heartland in week 1 before any code is written, so the path is locked before engineering hours are spent.

**Honest caveat:** No published case study exists for "AI consultancy successfully bridges Digital Dining to a modern BI stack at a single multi-unit operator's request." The reason is exactly why this engagement exists: nobody's corporate roadmap has ever allocated the engineering hours to a single legacy POS location when there are 1,650 modern POS locations to optimize first. This work is the side-quest, named as a specific deliverable instead of a vague capability.

**Source bias:** Digital Dining integration depth references come from Heartland Payment Systems product documentation, Restaurant365 / MarginEdge / Avero integration matrices, and operator forum threads (e.g., r/restaurateur, RestaurantOwner.com). No vendor case study cited because no comparable case study exists publicly.

### M1. Inventory variance tracking

**What it is:** MarketMan, MarginEdge, or Restaurant365 pulls invoices, cross-references against POS depletion, and flags variance daily. The "what did we actually use vs. what theoretical recipes say we should have used" report. The most important single number in restaurant back-office that most independents never look at.

**The MarketMan / Dolar Shop case is directly relevant.** MarketMan's most-cited customer is Dolar Shop, a 50+ location international Chinese hotpot chain. Same kind of operation as Wasabi and Panda Inn at the unit level. Multi-protein, multi-vegetable, family-style service, a long list of high-variance ingredients. The case study (MarketMan's published vendor reference) documents food cost reductions in the 2–3 percentage-point range across the rollout. **Treat as ceiling; realistic deployment outcome is 1–3 percentage points after the variance review process becomes a real weekly habit.**

**Cost:** $200–$500/location/month for MarketMan or MarginEdge. Restaurant365 higher. Budget $600–$1,500/month across three locations.

**Deploy effort:** 4–8 weeks. The vendors say 30 days; operators say 90 days to fully trust the numbers. Recipe build, vendor catalog mapping, count cadence training all need to happen before the variance numbers are actionable. **This is the deployment that fails most often because nobody owns the variance review.** The single most important hire/assignment in this rollout is the person whose job is "review the variance report every Monday at 9 AM and ask the kitchen to explain the top three line items." Without that role, the tool is just dashboards nobody opens.

**Realistic outcome:** Food cost down 1–3 percentage points after 90 days. **Bigger margin lever than any voice or marketing AI in this entire roadmap.** This is where the actual money is.

**Adoption risk:** High. Counts must happen daily, mapping must be maintained, GMs must care. Mitigation: pilot at one location first (recommended: Yakiya, because the SKU count is small enough to make recipe build manageable, and the food cost is highest because of the wagyu).

**Source bias:** MarketMan vendor case study (treat as ceiling). Independent corroboration: trade press coverage of multi-unit Chinese operators using inventory variance tools (Restaurant Business Online).

### M2. POS-driven email/SMS marketing with the Toast Sous Chef pattern

**What it is:** Toast Marketing, Bikky, or Bloom Intelligence segments customers by RFM (recency, frequency, monetary) and sends personalized winback campaigns. For Panda Inn. Where the named-server moat already exists. This is the tool that converts named-server loyalty into trackable visit cadence. For Yakiya. Where the chef is invisible and the review velocity is 88 reviews after 10 years. This is the tool that closes the post-visit loop with a prompt for a Google review.

**The Toast Sous Chef case is the anchor.** Toast disclosed a **6% lift in average order value** from its AI-powered upsell tool on its Q1 2024 earnings call (May 8, 2024), reported by PYMNTS. **That is the realistic small-win benchmark for this kind of deployment**. Not a 50% lift, not a transformation, a documented 6% AOV bump on the existing customer base. Stack 6% AOV across three locations against the $128 PPA at Yakiya alone and you have meaningful annual revenue.

**Cost:** $100–$300/location/month, often bundled in the POS suite. Budget $300–$900/month across three locations.

**Deploy effort:** 2–3 weeks for Toast-native deployment. Longer for non-Toast.

**Realistic outcome:** 2–6% AOV lift on the customer base that opts in (typically 30–50% of guests). Best case for Yakiya and Panda Inn (repeat-customer concepts). Lower fit for Wasabi (mostly one-time tourist captive market).

**Adoption risk:** Low. The marketing flows automatically; the manager approves campaigns once a week.

**Source bias:** Toast Q1 2024 earnings call disclosure is independent press (PYMNTS, Restaurant Dive). 6% is the headline; expect 2–4% in a typical operator deployment.

### M3. Scheduling tied to historical sales

**What it is:** 7shifts AI or Lineup.ai pulls 12 months of POS sales, predicts demand by daypart, suggests a schedule. The labor forecast goes from "Chris's intuition" to "pattern-matching against 52 weeks of data plus weather plus event calendar."

**This is the layer Wasabi at CityWalk needs most.** Universal Studios attendance is itself a daily moving target driven by ride downtime, weather, school calendars, and marquee events. A scheduling tool that pulls Universal's published event calendar into the labor forecast and knows that the Friday before a Universal-exclusive movie premiere doubles cover counts is the difference between "we got crushed and called in two extras at 6 PM" and "we already had two extras on the schedule."

**Cost:** $70–$120/location/month for 7shifts mid-tier. Budget $200–$360/month across three locations.

**Deploy effort:** 2–3 weeks. Needs clean POS history, which the Phase 1 work helps surface.

**Realistic outcome:** 1–3 percentage points labor cost reduction after 6–8 weeks of GM trust-building. Vendor case studies routinely claim 4–6%; build expectation low.

**Adoption risk:** Medium. GMs initially override AI suggestions out of habit. Trust builds over 6–8 weeks. Mitigation: start with the GM who is most curious, not the most resistant. Use the second GM to validate, then roll to the third.

**Source bias:** 7shifts is widely deployed (1.5M+ restaurant pros per their site). Lineup.ai's published Carrot Express case study claims $1M+ annual labor savings. Vendor metric, treat as ceiling.

---

## Phase 3 — Long Game (Weeks 9–12)

The bar for Phase 3: integration work is fine; the payoff is a moat. Something competitors can't easily copy.

### L1. Cross-location BI dashboard

**What it is:** Tenzo, Bikky, or Lineup.ai unifies all three POS systems into one daily dashboard. Owner sees three locations the way an enterprise sees three regions: same KPIs side by side, comparable, drillable. *"Yakiya labor is fine, Wasabi is over by 3 points, Panda Inn food cost is the leak."*

**Why this is in Phase 3 instead of Phase 1:** Wasabi runs Digital Dining, which means the cross-location dashboard depends on the W1 bridge shipping first. Phase 3 picks up after W1 has been validated against Wasabi's back-office reports, so all three locations land in the dashboard at the same level of fidelity instead of two clean and one bolted-on.

**Cost:** $400–$800/location/month for the data layer. Budget $1,200–$2,400/month across three locations.

**Deploy effort:** 6–10 weeks. Toast-to-Toast is fastest. Mixed POS adds 4–8 weeks.

**Realistic outcome:** Cross-location pattern detection. The owner reads one dashboard at 6 AM Monday and knows where to spend the week's attention. **This is what a multi-unit owner secretly wants and rarely says out loud.**

**Adoption risk:** Low. It's a dashboard. Reading it is the entire interaction.

**Source bias:** Tenzo and Lineup.ai both publish customer case content; accuracy depends entirely on POS data hygiene. None of the published cases are direct PRG-scale enterprise comparables. Treat as a multi-unit operator tool, not an enterprise BI tool.

---

## The Honest Limits — read this section before reading anything else

Per WS3's reading rule for this dossier: *if you can't defend the number with a source, it doesn't go in the deliverable.* The most important page is the page that names what AI cannot reliably do today. This section earns the right to make the recommendations above.

### 1. Replace the chef's creativity in menu development

Menu development is still an act of taste, intuition, and seasonal judgment. AI can analyze sales data to tell you what sells. It cannot tell you what dish belongs on a menu next spring. For Yakiya specifically, the chef's hand on the menu is the brand. **Don't touch it.**

### 2. Replace the GM's "feel" for the room

A great GM walks the dining room and reads tension in 10 seconds. They notice the four-top that's been waiting too long, the regular who looks distracted, the server who's rattled. No AI sees that today. The GM is irreplaceable. The tools above should free the GM from paperwork so they can spend more time on the floor. Not replace their judgment.

### 3. Take drive-thru orders unsupervised

McDonald's killed their IBM voice AI in **June 2024** after a 100+ store rollout. CEO Chris Kempczinski admitted approximately **85% accuracy** with one in five orders requiring human help. Viral TikToks documented 260 chicken nuggets added to one order, bacon added to ice cream, and other failures. Independent press corroboration: CNBC, BBC, AP, NYT, Axios, Restaurant Business Online, Restaurant Dive. Gold-standard coverage across multiple mainstream outlets.

Presto Voice's SEC enforcement (Administrative Litigation 33-11352, 2024) showed the same pattern from a regulatory primary source: *initial commercial Presto Voice required human agents for 100% of orders; the advanced 2023 pilot still required human agents for ~70% of orders, while marketing claimed up to 95% non-intervention.* The SEC found this language conflated "no in-restaurant staff intervention" with "no human intervention", Presto used off-site human agents.

Wendy's FreshAI does best at 86% no-intervention. Meaning **14% still need a human and accents still cause failures.**

**Phone reservation AI works. Drive-thru ordering AI does not.** Don't conflate them. Anyone selling drive-thru voice AI today is selling future state. That distinction is the line Chris's owner should hear named first.

### 4. Operate on dirty POS data

Most restaurants. Independent and enterprise. Have garbage POS data. Items mis-categorized, modifiers wrong, recipe builds incomplete, void/comp logic inconsistent across managers. AI built on bad data produces confident wrong answers. **The first 30 days of any AI rollout should be data hygiene, not a tool purchase.** Phase 1 of this roadmap is built around tools that don't depend on clean POS data (manager voice log, review response) so that the data hygiene work can happen in parallel with visible Phase 1 wins. Q3 (the weekly P&L digest) ships at Yakiya and Panda Inn during Phase 1; Wasabi waits for the W1 Digital Dining bridge in Phase 2 before joining.

### 5. Integrate cleanly with legacy POS systems

Aloha (NCR Voyix), Micros (Oracle), and Digital Dining (Menusoft Systems / Heartland Payment Systems) are technically extractable but contractually painful. Documented integration limits — file-size caps, polling timeouts, ODBC licensing tiers, debout settings — make third-party data exchange brittle. Some POS vendors charge revenue-share fees for marketplace listing. Translation: Wasabi runs Digital Dining and the integration takes 2–3x longer than a Toast or Square location. **That's why W1 above is a named Phase 2 deliverable with a specific budget and a specific build path, instead of an asterisk.**

### 6. Handle truly novel customer service situations

The "my grandmother passed away and we wanted to bring her ashes to her favorite booth" call. No AI handles that. The hostess does. Plan tooling around the 80% of routine calls (hours, reservations, parking, dietary questions) and route the rest to humans.

### 7. Replace physical kitchen labor at independent-restaurant scale

Sweetgreen Infinite Kitchen costs approximately **$550,000 per system** and has been installed in approximately 30 of 270 stores after 2.5 years of rollout. Per Sweetgreen's Q4 2025 earnings call, the economics work for **new builds at scale**, not retrofits. CFO Mitch Reback was explicit on the call: older small stores will not be retrofitted. Zume Pizza raised $445M and shut down. Spyce closed its restaurants and was acquired for parts. Karakuri shut down in 2023. CaliBurger Flippy retreated.

**Kitchen automation at independent or four-unit-concept scale is still a research project, not a deployable solution.** Anyone selling otherwise is selling future state.

### 8. Write marketing copy that sounds like the brand

AI-generated copy trips the AI-tells radar instantly. The Salty Otter Sports Grill (Santa Cruz, May 2025) used an AI-generated logo, got savaged in one-star reviews, and replaced it. The owner publicly said the AI controversy "crushed her dream." For ethnic concepts the risk is worse. Cultural sensitivity and authentic voice can't be prompted. **AI drafts; humans ship.** Especially at Yakiya and Panda Inn, where the brand voice is the asset.

### 9. Predict demand without enough history

Forecasting tools (Lineup.ai, Tenzo) need 12+ months of clean data to learn weather and event patterns. A new menu launch resets the model. A renovation resets the model. A new GM resets the model. **Set the expectation: forecasting accuracy improves over 60–90 days of operation, not Day 1.**

### 10. Manage vendor relationships

Vendor relationships are still relational. The fish broker at Wasabi knows when there's better tuna coming in. The produce vendor at Yakiya knows when the chef will want a specific variety of mushroom. AI can optimize the order quantity. **It cannot replace the call.**

---

## The Menu Engineering Honesty Caveat

*(Lifted from WS3 verbatim because it's already in Farrice's voice and earns its keep here.)*

True menu engineering, Kasavana and Smith's stars / plowhorses / puzzles / dogs framework. Needs three things from a restaurant's POS: units sold per item, theoretical food cost per item, and actual sell price per item. The math classifies each menu item by popularity and contribution margin, then tells you what to feature, what to reposition, what to reprice, and what to cut. Done well, it can move prime cost two to four percentage points in a single quarter. This is the version of menu engineering that earns its name.

What this analysis is, and what it isn't. Without your POS sales data, what's in this folder is a *signal-based menu efficiency review*. A different and more limited animal. It looks at how your prices sit against the market median in your immediate area, where your menu is dense versus sparse compared to competitors, which items appear universally on competitor sets (the table stakes you're missing or running heavy), and what reviewers love and hate (a rough proxy for stars and dogs). Every recommendation here is defensible from public data. None of them require touching your books. That's the V1. A sharp but external read on where the menu is leaving money on the table.

The full version is a Phase 2 conversation. Once we have a week of POS exports. Even just item-level sales counts and price points. The same framework that lifts Wendy's, Chipotle, and your sushi competition's margins becomes available to you. Most operators discover at least one star they were under-pricing, one dog draining prep labor, and one puzzle the menu was hiding. That can be scoped as a focused two-week engagement after this analysis lands. For now, the V1 is built so you can start acting on the public signals immediately and decide separately whether the deeper work is worth doing.

---

## The estimated math at the end of 90 days

If all seven items above (Q1, Q2, Q3, W1, M1, M2, M3) ship on schedule, the realistic conservative estimate of operational lift across three locations:

| Lever | Conservative annual lift | Source |
|---|---|---|
| Inventory variance (M1) | 1–3 prime-cost percentage points | MarketMan / Dolar Shop case (treat as ceiling) |
| Toast-pattern upsell + email/SMS (M2) | 2–4% AOV lift on opted-in customers | Toast Q1 2024 earnings call (PYMNTS) |
| Scheduling labor forecast (M3) | 1–2 percentage-point labor cost reduction | 7shifts / Lineup.ai vendor cases (treat as ceiling) |
| Manager voice log (Q1) | Time recovery, not direct revenue | Estimated 3–5 hours/week saved per location |
| Review response (Q2) | Estimated 0.1–0.2 star Google rating lift | Marqii vendor case studies |
| BI dashboard (L1, Q3) | Decision-quality improvement, not directly modeled | Tenzo / Lineup.ai vendor case studies |

Across the three legacy concepts, **conservative annualized lift ranges from $80,000 to $250,000 in margin and recovered revenue**, before counting the Yakiya beverage program leverage (which is documented separately in the Yakiya menu file as a $300K–$700K/year opportunity at one location, and which is a Phase 0 fix that doesn't require any of the tools in this roadmap. It's a beverage director conversation and a menu reprint).

**The total cost of the tools in Phases 1, 2, and 3 across three locations: approximately $2,500–$5,500/month.** Annualized: $30K–$66K. The math works at the low end of every assumption.

---

## The 1975 question pre-empted

The single objection Peggy Cherng or Tom Davin or Gigi Cheung will surface within the first 90 seconds of any meeting:

*"We've been investing in restaurant tech since 1975. What is a consultant going to tell me I do not already have on my CIO's roadmap?"*

The reframe isn't "I know more than your team." It is: *"You can. Your CIO can. But they won't this quarter. Because the ROI math on four legacy concepts can't compete with the ROI math on 1,650 Panda Express stores. That's not a critique of your team. It's arithmetic. The work in this roadmap is the work that exists to be done while the arithmetic isn't ready to flip."* That sentence makes the position defensible, non-threatening, and leaves Peggy's lifework intact. Everything in this roadmap is built inside that frame.

---

## What this roadmap is, structurally

Seven items. Three phases. Twelve weeks. Each item has a documented cost, a documented case-study reference (or, in the case of W1, a transparent absence of one), an honest failure-mode caveat, and a defensible expected outcome. Nothing in here is a robot. Nothing in here promises voice AI in the drive-thru. Nothing in here assumes the kitchen wants to be replaced. Nothing in here pretends that PRG corporate doesn't know how to run analytics. **This is a roadmap for the four orphaned legacy concepts, executable inside the existing operating budget of those four locations, deployable by a small team in 90 days.**

The first phase is shippable inside Chris's existing operating envelope. The second phase needs Gigi Cheung's nod. The third phase touches IT and would need a brief conversation with whoever runs PRG's tech function on the legacy side. Not to ask permission, but to make sure the integration assumptions hold and the data is being read the same way the corporate team reads it.

---

## Sources

**Case studies anchored in the roadmap above:**
- **Toast Sous Chef AI 6% AOV lift**, Toast Q1 2024 earnings call, May 8 2024, reported by PYMNTS and Restaurant Dive
- **MarketMan / Dolar Shop**, MarketMan published vendor case study, 50+ international Chinese hotpot locations
- **McDonald's IBM drive-thru termination June 2024**, CNBC, BBC, AP, NYT, Axios, Restaurant Business Online, Restaurant Dive (independent press, gold standard)
- **Presto Voice SEC enforcement**, SEC Administrative Litigation 33-11352.pdf (regulatory primary source. Highest credibility)
- **Wendy's FreshAI**, Wendy's corporate blog corroborated by Forbes Jan 2025
- **Sweetgreen Infinite Kitchen**, Sweetgreen Q4 2025 earnings call transcript (Feb 2026), Restaurant Business Online Nov 2025, QSR Magazine throughput coverage
- **7shifts and Lineup.ai labor forecasting**, 7shifts.com, lineup.ai vendor case studies (Carrot Express claim treated as ceiling)
- **Marqii / Owner.com / Popmenu review response**. Vendor pricing pages (marqii.com/pricing), customer claim references (Owner.com Talkin Tacos / Saffron)

**Honest limits sources:**
- Salty Otter Sports Grill AI logo controversy (May 2025, Santa Cruz, owner statement reproduced in trade press)
- Zume Pizza shutdown (TechCrunch, The Robot Report)
- Spyce / Karakuri / CaliBurger Flippy (Robot Report, Physics World, trade press)
- POS integration limits (Aloha NCR documented limits, Toast support community, restaurant operator forums)

**Operator psychology and the 1975 reframe:**
- WS2 operator-psychology research file (`03-research/WS2-operator-psychology.md`)
- math.oregonstate.edu/impact/2023/07, Peggy Cherng's biographical and academic background
- Forbes coverage of Peggy Cherng
- pandarg.com/our-story
- en.wikipedia.org/wiki/Peggy_Cherng
- nrn.com Innovation Kitchen 2025 coverage
- pandarg.com/andrea-cherng, Andrea Cherng CBO profile, including digital business team build
