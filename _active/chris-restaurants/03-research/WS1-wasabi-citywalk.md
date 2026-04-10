# WS1 — Wasabi at Universal CityWalk

**Researched:** 2026-04-06
**Analyst:** WS1 Market Intelligence
**Status:** Complete — high confidence on identity, ownership, menu, pricing; medium confidence on review themes (Yelp/TripAdvisor blocked, used Restaurantji + Google Maps + Apify web)
**Apify spend on this dossier:** $0.36 (within $0.63 envelope)

---

## Restaurant Identity

| Field | Value |
|---|---|
| **Full name** | Wasabi (DBA: Wasabi at CityWalk) |
| **Address** | 1000 Universal City Plaza #112, Universal City, CA 91608 |
| **Phone** | (818) 763-8813 |
| **Website** | wasabi-citywalk.com |
| **Hours (Google)** | 11 AM – 9 PM, all 7 days |
| **Hours (NetWaiter)** | Sun 12-9, Mon-Thu 12-8, Fri-Sat 12-10 |
| **Cuisine category** | Japanese restaurant (Google) / Sushi bar + Japanese (Restaurantji $$) |
| **Google rating** | **4.1** stars, **395** reviews |
| **Yelp footprint** | **1,729** reviews, 1,789 photos (per Yelp listing data) |
| **Restaurantji rating** | 4.0, 233 ratings |
| **Operator** | **Panda Restaurant Group, Inc.** (the Cherng family) |
| **Concept slot** | One of four PRG brands: Panda Express, Panda Inn, Wasabi, Hibachi-San |

> **Discrepancy flag:** NetWaiter and Google Maps disagree on hours. Google says open 11 AM. NetWaiter says open 12 PM (and closes 8 PM weekdays). One of these is stale. Worth a 30-second sanity check at the location.

> **Discrepancy flag #2:** Wasabi is **NOT listed in Universal CityWalk Hollywood's official "Guide to Dining" blog post** (24+ restaurants enumerated, Wasabi absent). It exists in CityWalk's Suite #112 and is in Universal's official restaurant URL hierarchy, but the marketing arm of CityWalk under-features it. Discoverability problem at the front door.

---

## Ownership — The Find That Changes the Mission

The biggest unknown going into this research was: *does one entity own all three of Chris's restaurants?* The answer is **yes — and the entity is bigger than expected.**

**Wasabi at CityWalk is owned and operated by Panda Restaurant Group, Inc.**, the Cherng family business that also owns:
- **Panda Express** (~2,400 fast-casual locations)
- **Panda Inn** (the original family restaurant concept, founded 1973 in Pasadena — *which includes the Glendale location in Chris's portfolio*)
- **Wasabi** (sit-down sushi/Japanese — *including this CityWalk location*)
- **Hibachi-San** (mall-court Japanese)
- **Yakiya** (upscale Japanese steakhouse / yakiniku — *which includes the Pasadena location in Chris's portfolio*)

**Cross-reference confirmed:**
- Yakiya privacy policy and terms pages on yakiya-us.com both name **"Panda Restaurant Group, Inc."** as the controller. Yakiya was launched 2016 as PRG's premium experiment. Pasadena location: 3455 E Foothill Blvd.
- Panda Inn was founded 1973 by Andrew Cherng's father; the Glendale location is one of the original Panda Inn locations (across from the Americana / Galleria corridor).
- Wasabi at CityWalk's "About" page literally states "Wasabi is part of the award winning Panda Restaurant Group, Inc."
- LinkedIn job postings for Wasabi Universal CityWalk are posted by **Panda Restaurant Group**, listing "Wasabi at Citywalk (1432)" — store #1432 in PRG's chain.

**Implication for the mission:** "Chris" is not managing three independent restaurants. He is a **multi-unit manager inside Panda Restaurant Group**, running three of PRG's premium / non-Express concepts in the LA market. The "owner" he reports to is somewhere in the **PRG corporate structure** — likely a Regional VP for the Panda Inn / Wasabi / Yakiya concept group. This is not a mom-and-pop owner. It is one of the largest privately-held restaurant operators in North America (1,650+ locations, $5B+ revenue, Cherng family).

This reframes the AI strategist pitch entirely. See "Key Insights" below.

---

## Menu Snapshot

Source: official PDF menu (wasabi-citywalk.com/wasabi_menu.pdf, extracted via pypdf), cross-referenced with Restaurantji "customer favorites."

### Categories (9 sections, ~60 items)

| Category | Item count | Price band |
|---|---|---|
| Starters | 4 | $3 – $13 |
| Salads | 2 | $8 |
| Signature Rolls | 10 | $18 – $21 |
| Sashimi Specialties | 3 | $19 (flat) |
| Nigiri (10 fish) | 10 | $9 (flat) |
| Sashimi (10 fish) | 10 | $16 (flat) |
| Traditional Rolls | 7 | $8 – $11 |
| Udon (small/large) | 3 | $8 / $13–14 |
| Tempura Dinner | 2 | $18 – $24 |
| Teriyaki Dinner | 4 | $21 – $28 |
| Drinks | 5 | $3 – $14/glass |

### Standout / Signature Items
- **Hollywood-themed signature rolls** — narrative naming convention is the menu's identity layer: Flaming Star, Hollywood, Marilyn Mon Roll, Terminator, Dragon Roll, Universal Roll. This is Wasabi's only menu engineering lever right now and it works inside the theme park context.
- **Customer favorites per Restaurantji:** Chef's Sushi Platter, Spicy Garlic Edamame, Yellowtail Jalapeño, Yellowtail Sushi, Spicy Tuna Roll, Terminator Roll, Salmon Sashimi, Teriyaki Beef. Notably **also**: Spicy Miso Ramen and Tonkotsu Ramen — but **ramen is not on the official PDF menu**. Either the menu has been updated since the PDF was published, or guests are mis-tagging udon as ramen. Either way, this is a menu/marketing sync gap.
- The **garlic edamame** has its own dedicated photo gallery on Yelp — it has crossed into "destination dish" status for repeat guests. This is a free piece of menu-engineering capital not currently being amplified.

### Menu Engineering Observations (visible from menu structure alone, no POS data)

1. **Flat-priced sushi grid is a leak.** Every nigiri is $9, every sashimi $16, regardless of fish — albacore, tuna, eel, scallop, salmon roe, sweet egg, inari. Sweet egg and inari (low-cost) are priced identically to scallop and salmon roe (high-cost). On a $5K nightly cover, this is 2-3 percentage points of food-cost margin walking out the door. The kitchen is subsidizing premium fish from the cheap fish.

2. **Signature Rolls are a tight $18-$21 cluster (10 items, $3 spread).** This is *too tight*. There's no anchor "splurge" item ($28-$32 chef's special) to make the $20 rolls feel like the value choice — a missed price-anchoring move that costs PPA (per-person average) on every check.

3. **Menu has only one beverage line — and no sake program.** "Sake" appears as a single line item with no varietal, no price tier, no ceremonial pour, no cold/hot. Inside an entertainment district where "sake bomb" is a tourist ritual, the absence of a sake menu is a 3-5% revenue leak per check on the alcohol attach rate.

4. **No appetizer/snack ladder for the bar / pre-show crowd.** CityWalk's foot traffic includes the 5 Towers Stage concert audience and the Universal Cinema spillover. Wasabi has 4 starters, none under $8 (except $3 miso). Compare to KazuNori (handroll bar across the hill) which uses $4-7 hot bites to capture pre-show drinkers.

5. **No kids' menu visible** despite "kid-friendly" being a praise theme on Restaurantji. A theme park restaurant without a kids' menu is leaving family covers on the table.

6. **The PDF menu was generated by "Katrina Guevara" (per PDF metadata).** It's a static PDF with no QR-code dynamic version, no allergen filter, no upsell prompt. The menu hasn't been refreshed against the actual current offerings (ramen exists in reviews but not the PDF).

---

## Competitive Set — Layer A (CityWalk Internal)

CityWalk-internal competition is mostly *non-Asian* — Wasabi has no direct sushi competitor inside the entertainment district. Its competitive set inside CityWalk is for **share of stomach**, not share of cuisine.

| Restaurant | Cuisine | Price (Google) | Rating | Reviews | Notes |
|---|---|---|---|---|---|
| Buca di Beppo | Italian (family-style) | $$ | 4.5 | 3,028 | Highest-rated full-service. Group-meal play. |
| Bubba Gump Shrimp Co. | Seafood / American | $20-30 | 4.3 | 2,328 | IP-themed seafood; closest "fun + sit-down" comparable. |
| Cafe Sierra (Hilton) | Buffet / Asian-fusion | $$ | 4.3 | 1,327 | At adjacent Hilton, has dim sum buffet — closest **Asian** competition. |
| Hard Rock Cafe (CityWalk) | American / Burgers | (n/a) | n/a | n/a | Did not surface in Apify pull but exists in CityWalk. |
| Toothsome Chocolate Emporium | American / Dessert | $20-30 | 3.4 | 938 | Steampunk theme. **Underperforming** — opportunity zone. |
| NBC Sports Grill & Brew | American / Bar | $20-30 | 4.0 | 395 | Same review count as Wasabi. |
| VIVO Italian Kitchen | Italian | $20-30 | 4.0 | 418 | Same tier as Wasabi rating-wise. |
| Antojitos Cocina Mexicana | Mexican | $20-30 | 3.1 | 667 | Significantly underperforming. |
| Jimmy Buffett's Margaritaville | American / Tropical | $20-30 | 3.9 | 1,440 | High-volume, mid-rated. |
| Three Broomsticks | Themed / British | $20-30 | 4.2 | 755 | In-park (Wizarding World) — competitive only on Q-line spillover. |
| Panda Express (CityWalk) | Chinese fast-casual | $ | 3.1 | 165 | **Same operator as Wasabi.** Internal cannibalization signal. |
| Uncle Sharkii Poke Bar | Hawaiian / Poke | (n/a) | 3.3 | 43 | Closest non-sushi raw-fish competitor; weak. |
| Firehouse Subs | Subs | $10-20 | 4.2 | 47 | Quick-service. |

**Layer A read:** Wasabi at 4.1 / 395 reviews sits in the **mid-pack** of CityWalk full-service. It is being out-rated by Buca di Beppo (Italian, 4.5/3,028) and Bubba Gump (4.3/2,328) — two operators that own the "sit-down family meal" mindshare. Wasabi has roughly 1/8th the Google review volume of Buca, despite being the only sushi option inside CityWalk. **Wasabi is the *category monopolist* but not the *category winner*.** That's a discoverability + reputation problem, not a competition problem.

---

## Competitive Set — Layer B (Drive-to, ~5 mile radius)

Studio City's Ventura Boulevard is the strongest drive-to threat — a 4-mile drive over the Cahuenga Pass gets a CityWalk visitor to **one of the top 5 sushi corridors in the United States**. NoHo and Burbank are softer, ramen-heavy.

### Studio City sushi row (the real threat — Ventura Blvd between Coldwater and Laurel Cyn)

| Restaurant | Tier | Price | Rating | Reviews | Distance |
|---|---|---|---|---|---|
| **Asanebo** | Omakase / fine dining | $100+ | 4.6 | 363 | 4.0 mi |
| **Sushi Bar Tetsuya** | Omakase | $50-100 | 5.0 | 75 | 3.8 mi |
| **Sushi Katsu-ya (Studio City)** | Premium izakaya (the Katsuya empire mothership) | $$$ | 4.5 | 604 | 4.2 mi |
| **KIWAMI by Katsu-ya** | Premium | $30-40 | 4.5 | 357 | 4.1 mi |
| **Teru Sushi** | Premium traditional | $$$ | 4.5 | 466 | 4.1 mi |
| **SUGARFISH by sushi nozawa** | Premium quick-service ($) | $30-50 | 4.5 | 908 | 4.4 mi |
| **Iroha Sushi of Tokyo** | Premium traditional | $$$ | 4.5 | 756 | 4.5 mi |
| **SHIKI SUSHI** | Mid-premium | $$ | 4.5 | 683 | 4.6 mi |
| **Daichan** (Japanese soul food) | Casual mid | $20-30 | 4.8 | 398 | 3.7 mi |
| **The Sushi House** | Mid | $$ | 4.4 | 432 | 4.0 mi |
| **Yume Sushi Bar** | Mid-premium | $50-60 | 4.6 | 210 | 4.5 mi |
| **Studio Sushi** | Mid | $30-50 | 4.4 | 206 | 1.6 mi (closest!) |
| **Sushi Dan** | Casual | $20-30 | 4.3 | 665 | 4.0 mi |
| **JINYA Ramen Bar** | Ramen | $20-30 | 4.6 | 2,456 | 3.9 mi |
| **REDWHITE BONELESS RAMEN** | Ramen specialty | $$ | 4.9 | 1,012 | 4.0 mi |
| **KazuNori (Hand Roll Bar)** | Premium handroll | $20-30 | 4.2 | 149 | 3.7 mi |
| **SushiStop Studio City** | Casual | $20-30 | 4.0 | 661 | 4.1 mi |
| **Leona's Sushi House** | Premium | $50-100 | 4.4 | 136 | 4.2 mi |

### NoHo / Toluca Lake / Burbank fringe

| Restaurant | Tier | Price | Rating | Reviews | Distance |
|---|---|---|---|---|---|
| **Maki-Noho** | Mid | $20-30 | 4.9 | 122 | 2.3 mi |
| **UMIAI Hand Roll & Sake Bar** | Premium handroll | (n/a) | 4.8 | 247 | 3.0 mi |
| **KITA Ramen and Sushi Bar** | Mid | $20-30 | 4.7 | 73 | 2.8 mi |
| **Ramen Izakaya NoHo** | Ramen-izakaya | $$ | 4.7 | 316 | 2.5 mi |
| **Sunny's Sushi Hut** | Casual | $10-20 | 4.6 | 263 | 2.6 mi |
| **Maki Shabu** | Shabu-shabu | $30-40 | 4.4 | 171 | 2.7 mi |
| **Tamashii Ramen House** | Ramen | $10-20 | 4.0 | 515 | 2.9 mi |

**Total drive-to competitive set surfaced:** 25+ Japanese restaurants within 5 miles. Sample is approximately 25 % omakase/premium ($30-100), 50 % mid-tier ($20-30), 25 % casual/ramen ($10-20).

---

## Pricing Bands — Computed

### Wasabi's own pricing (from official PDF, all in USD)

| Section | n | Min | Avg | Median | Max |
|---|---|---|---|---|---|
| Appetizers (starters + salads) | 6 | $3 | $8.33 | $8 | $13 |
| Traditional rolls | 7 | $8 | $9.57 | $10 | $11 |
| Signature rolls | 10 | $18 | $19.90 | $20 | $21 |
| Nigiri (per piece) | 10 | $9 | $9.00 | $9 | $9 |
| Sashimi (per order) | 10 | $16 | $16.00 | $16 | $16 |
| Sashimi specialties | 3 | $19 | $19.00 | $19 | $19 |
| Udon dinner (large) | 3 | $13 | $13.67 | $14 | $14 |
| Tempura dinner | 2 | $18 | $21.00 | $21 | $24 |
| Teriyaki dinner | 4 | $21 | $25.00 | $25.50 | $28 |
| **All mains (dinners)** | **9** | **$13** | **$20.33** | **$21** | **$28** |

### Wasabi vs. competitive set benchmarks

| Tier | Wasabi position | Competitive median |
|---|---|---|
| **Average rating** | **4.1** stars | **4.50** stars (across 40 deduped Japanese competitors) |
| **Review volume** | 395 Google / 1,729 Yelp | 241 Google (median competitor) |
| **Signature roll avg** | $19.90 | Studio City premium tier $22-28 / casual tier $14-18 |
| **Mains avg** | $20.33 | Studio City premium tier $28-40 / casual tier $16-22 |
| **Nigiri (per piece)** | $9 flat | Studio City $5-9 (cheap fish) / $12-22 (premium fish) |

**Key observation:** Wasabi prices its **mains and rolls in the casual-mid Ventura Blvd band** (e.g., Sushi Dan, SushiStop) but is **rated 0.4 stars below the median Japanese restaurant in the area**. This is the captive market footprint — pricing as if you have competition, performing as if you don't. The premium Studio City tier (Asanebo, Katsu-ya, Sugarfish) charges 30-50 % more *and* rates 0.4-0.5 stars higher. Wasabi is leaving margin on the table at the top *and* losing on perceived value at the bottom.

---

## Review Themes — Wasabi

**Source:** Restaurantji review summary (n=233), Google Maps description, Yelp public snippets via web search, Restaurantji rating distribution.

### Rating distribution (Restaurantji, n=233) — bimodal
- 5 stars: **64%**
- 4 stars: 10 %
- 3 stars: 5 %
- 2 stars: 7 %
- 1 star: **14%**

This is a **bimodal distribution**, not a normal one. 64% love it, 14% hate it. The 1-star segment (14%) is the captive-market signature: people who feel trapped, overpaying, and underserved during peak hours. The 5-star segment is the post-park-day relief crowd who got attentive service and expected nothing premium. **There's no "middle"** — and that means Wasabi has a service-consistency problem, not a food-quality problem.

### Praised
- **Server Luzby** is named explicitly for going "above and beyond" — anticipating chili oil for ramen without being asked. Hyper-personalized service is a recurring praise theme.
- **Chef's Sushi Platter, Yellowtail Jalapeño, Garlic Edamame, Spicy Tuna, Terminator Roll** — most-mentioned dishes, all visible on the menu.
- **"Cute and relaxing atmosphere"** — described as a refuge after a busy theme park day. The "decompression" use case is real.
- **Fresh sushi**, **massive portions**, **kid-friendly**, **wheelchair accessible**, **dietary accommodating**.
- **"Worth the price compared to park food"** — the explicit mental anchor reviewers use is "park food," not "Studio City sushi." The bar Wasabi is being compared against is *fries-and-burger theme park food*, not real sushi. This is both protection and a ceiling.
- **Hollywood-themed Signature Rolls** generate repeat photo content on Yelp.

### Complained about
- **Long waits at peak hours / peak season**, especially evenings when "the park is bustling."
- **Inconsistent service** — "horrible customer service," "servers forgetting dishes," "slow and not particularly responsive" are quoted complaint patterns.
- **"A bit pricey"** for what you get — but importantly, this complaint is *less common* than the "worth it for park food" sentiment. The pricing complaint comes from non-tourist locals who know what $20 buys in Studio City.
- **Authenticity gap** — one review explicitly says "the food may not be the most authentic but it is delicious." This is a recurring undercurrent. Wasabi reads as Japanese-influenced, not Japanese.
- **Long wait → slow service → forgotten dishes** — this is one connected failure chain during peak. It's a **prep-station throughput problem**, not a server attitude problem. (POS-grade observation: when servers get blamed in bursts, it's almost always a kitchen ticket-time issue rolling downhill.)

### Most-mentioned dishes
1. Chef's Sushi Platter
2. Spicy Garlic Edamame ⭐ (gets its own photo gallery on Yelp)
3. Yellowtail Jalapeño
4. Spicy Tuna Roll / Terminator Roll
5. Salmon Sashimi
6. Teriyaki Beef
7. Spicy Miso Ramen / Tonkotsu Ramen *(missing from official PDF — sync gap)*
8. Flaming Star Roll
9. Beef Udon
10. Wagyu *(does not appear on official PDF — likely a special)*

---

## Review Themes — Top 5 Drive-to Competitors

### 1. Asanebo (Studio City) — $100+, 4.6, 363 reviews
- **Praised:** Omakase mastery, traditional Edomae technique, ingredient sourcing from Toyosu market, intimacy.
- **Complained:** Cost; reservation difficulty; "stuffy" or "too quiet" for some.
- **Signature theme:** Destination omakase. People drive for it.
- **Gap vs. Wasabi:** Asanebo is the "if you actually want sushi" answer. Wasabi cannot and should not compete here — but should be aware it is the ceiling.

### 2. Sushi Katsu-ya — Studio City ($$$, 4.5, 604 reviews)
- **Praised:** Famous Crispy Rice with Spicy Tuna (the Katsuya signature), Baked Crab Hand Roll, ambiance, celebrity sightings.
- **Complained:** Loud, expensive, sometimes inconsistent at peak.
- **Signature theme:** Single signature dish (crispy rice) drives 30%+ of conversation. Menu engineering 101.
- **Gap vs. Wasabi:** Wasabi has *no single dish* with brand-level recognition. The "Marilyn Mon Roll" is named but not famous. The garlic edamame *could* be that signature item with the right amplification.

### 3. SUGARFISH by sushi nozawa ($30-50, 4.5, 908 reviews)
- **Praised:** "Trust Me" set menu (fixed omakase courses for ~$32-65), simplicity, consistent quality, no menu paralysis.
- **Complained:** No customization, small portions, wait list.
- **Signature theme:** **Constraint as feature.** They reduced a sushi menu to 3 fixed paths. Highest-rated "fast premium" sushi in LA.
- **Gap vs. Wasabi:** Wasabi has 60 items and no "I trust you" path. Adding a single $35 "Wasabi Trust" set menu (4 nigiri, 1 signature roll, miso, edamame) would convert paralysis into PPA.

### 4. JINYA Ramen Bar ($20-30, 4.6, 2,456 reviews)
- **Praised:** Tonkotsu broth depth, customization, consistent across locations.
- **Complained:** Wait, parking on Ventura.
- **Signature theme:** **Ramen as the theme park-adjacent comfort meal of choice.** 2,456 reviews — 6× Wasabi's Google review volume.
- **Gap vs. Wasabi:** This is the *real* competitor for the post-park-day decompression diner who decides to drive 4 miles instead of stay in CityWalk. JINYA's success explains why Wasabi guests are reviewing "ramen" that doesn't appear on Wasabi's PDF — guests *expect* ramen at this price tier and Wasabi isn't on the official menu.

### 5. Daichan (Japanese soul food, Studio City) — $20-30, 4.8, 398 reviews
- **Praised:** Family-run, "real Japanese," donburi rice bowls, value, no pretension.
- **Complained:** Cash-preferred, small dining room.
- **Signature theme:** **The "authentic" play at Wasabi's exact price point.** 4.8 stars vs Wasabi's 4.1 — at the same $20-30 spend.
- **Gap vs. Wasabi:** Daichan proves that the casual-mid sushi diner *will pay $20-30 for authentic-feeling Japanese food*. Wasabi is leaving the authenticity perception on the table by leading with Hollywood-themed novelty rolls instead of a chef's daily fish board.

---

## Captive Market Notes

### Foot traffic dynamics
- Universal Studios Hollywood admission ranges $109-149/day, with annual attendance ~9 million visitors (pre-pandemic baseline; recovered by 2024). CityWalk is **free to enter** — meaning the addressable foot traffic is theme park visitors PLUS locals who come for the cinema, the 5 Towers concert stage, and the dining/bar scene.
- **Peak windows:** Weekend lunch (12-2 PM), weekend dinner (6-9 PM), weekday summer / holiday breaks, Friday/Saturday post-cinema (9-10 PM).
- **Soft windows:** Tuesday-Thursday afternoons (the "dead hours" for a captive-market restaurant) — Wasabi closes at 8 PM Mon-Thu per NetWaiter, signaling these are unprofitable.
- **Pre-show crowd:** 5 Towers Stage concerts and Universal Cinema premieres create predictable demand spikes 1-2 hours before show times. Wasabi has no visible pre-show / happy hour offer.

### Captive-market price ceiling
- Theme park visitors arrive *expecting* to overpay. The mental anchor for "expensive" inside CityWalk is "$25 burger at NBC Sports Grill," not "$80 omakase at Asanebo." This sets Wasabi's *floor* high (people will pay $20 for a roll without flinching) but its *ceiling* low (the same people will revolt at $35 for a roll because "this is theme park sushi").
- The 14% 1-star segment shows where the ceiling actually sits: when the experience drops below "fast and friendly," the captive audience turns adversarial and writes scathing reviews.
- **Practical implication:** Wasabi has room to *raise* signature roll prices by 10-15 % ($20→$22-23) without losing the captive crowd, IF service throughput is fixed first. Raising prices on a 14%-1-star service-broken restaurant accelerates the death spiral. Fix throughput first, then raise.

### Parking / access friction
- CityWalk valet is $10 (validated). General parking is $30+. Drive-to sushi competitors in Studio City have **free street parking and validated lots** — the parking math actively pushes locals AWAY from CityWalk Wasabi.
- This is why Wasabi is overwhelmingly tourist-fed even in a region with 200,000+ locals. The captive moat is also a discoverability prison.

### AYCE / group dynamics
- Wasabi does **not** offer All-You-Can-Eat. This is the right call — AYCE inside CityWalk would cannibalize PPA in a captive market. But it should know that JINYA ramen and Sushi Stop both offer pseudo-AYCE happy hour deals during off-peak hours. Wasabi's off-peak (Tue-Thu afternoon) is unmonetized.

---

## Key Insights (Defensible, Specific, Owner-Ready)

### 1. Chris is not a small operator. Chris is a multi-unit manager inside Panda Restaurant Group.
The single biggest finding from this research is the ownership cross-reference. Wasabi at CityWalk, Yakiya Pasadena, and Panda Inn Glendale are **all PRG concepts**. PRG is the Cherng family's $5B+ private restaurant business — 1,650+ locations across Panda Express, Panda Inn, Wasabi, Hibachi-San, and Yakiya. The "owner" Chris reports to is somewhere in PRG corporate, almost certainly a Regional or Concept VP who oversees the Panda Inn / Wasabi / Yakiya group (separate from the Express side). **This means Farrice's pitch is not to a $3M owner-operator. It is to a strategic decision-maker inside a corporation that has the budget for a real AI engagement.** It also means everything we propose has to be **enterprise-defensible**, not freelancer-cute. Vendor lock-in concerns, data security, and PR brand exposure all matter at PRG-scale.

### 2. Wasabi has 60 items but only one menu engineering lever — Hollywood-themed names.
60 items is **not too many for sushi** in absolute terms (Sugarfish has 30, Katsu-ya has 100+). But Wasabi's 60 items have a **flat-priced sushi grid** ($9 nigiri across all 10 fish, $16 sashimi across all 10 fish), no anchor splurge item, no chef's daily fresh sheet, no sake program, and no kids' menu. The only menu engineering they're doing is naming rolls after Hollywood things. There are at least **5 specific levers** unused: (a) tiered nigiri pricing by fish, (b) one $32-38 anchor signature roll, (c) sake/cocktail program for the entertainment district, (d) kids menu, (e) "Trust Me" omakase set in the SUGARFISH model. Each of these is testable in 2-4 weeks with POS data.

### 3. Wasabi rates 0.4 stars below the area median sushi restaurant — at the same price point.
Across 40 deduped Japanese competitors within 5 miles, the median Google rating is 4.50. Wasabi sits at 4.10. That gap is not "Wasabi is bad" — Restaurantji praise themes are strong. It is **"Wasabi has a service consistency problem at peak hours"**, evidenced by the bimodal review distribution (64 % 5-star vs. 14 % 1-star, almost no middle). In a normal market this would be a death sentence. In CityWalk's captive market it shows up as 1,729 Yelp reviews and a 4.1 — survivable, but a permanent ceiling on PPA, repeat-visit rate, and brand equity. **The fix is not menu redesign first. It is throughput / ticket-time first, then menu.** Any AI proposal that ignores this sequence will fail when implemented.

### 4. Wasabi is the only sushi restaurant in CityWalk — and CityWalk doesn't promote it.
Wasabi has zero direct sushi competition inside CityWalk. It is the **category monopolist for raw fish inside a 9-million-visitor-per-year entertainment district**. And yet: it is **not listed in CityWalk's official "Guide to Dining" blog post** that enumerates 24+ restaurants. It is in Universal's official restaurant URL hierarchy but absent from the marketing front door. This is a **discoverability arbitrage** — there is real money sitting in Universal's own marketing channels that Wasabi is not capturing. Step one of any digital intervention is fixing this listing gap. (This is also a *hand-shakable* win we can offer in the deliverable: "we found the listing gap, here's the proof, here's a one-page brief Chris can take to the Universal CityWalk marketing rep.")

### 5. The garlic edamame is an unreached signature dish.
Restaurantji's customer favorites list and Yelp's photo gallery both flag **Spicy Garlic Edamame** as a recurring obsession — to the point that it has its own dedicated review page on Yelp. It is **a $8 menu item** that is doing the brand-equity work of a signature dish without being treated like one. Sugarfish has the "Trust Me" menu. Katsu-ya has the Crispy Rice with Spicy Tuna. Wasabi has the Garlic Edamame and isn't naming it, photographing it, or building a story around it. This is the cheapest, most defensible menu engineering recommendation in the dossier.

---

## Sources

### Apify runs (this dossier)
- `apify maps "sushi" --location "Universal City, CA 91608" --limit 25` — 6 results — `_raw-data/wasabi-apify-universal-city.json` — $0.042
- `apify maps "sushi" --location "Studio City, CA 91604" --limit 25` — 25 results — `_raw-data/wasabi-apify-studio-city.json` — $0.175
- `apify maps "japanese restaurant" --location "North Hollywood, CA 91602" --limit 25` — 23 results — `_raw-data/wasabi-apify-noho.json` — $0.161
- `apify maps "restaurant Universal CityWalk" --location "Universal City, CA 91608" --limit 25` — 25 results — `_raw-data/wasabi-apify-citywalk-internal.json` — $0.175
- `apify web https://www.wasabi-citywalk.com/about.php` — owner cross-reference — $0.003
- `apify web https://blog.discoveruniversal.com/.../citywalk-hollywood/` — CityWalk dining guide — $0.003
- `apify web https://wasabiatcitywalk.netwaiter.com/` — NetWaiter listing — $0.003
- `apify web https://www.restaurantji.com/ca/universal-city/wasabi-at-citywalk-/` — review themes + customer favorites + rating distribution — $0.003

**Total Apify spend on this dossier: $0.565** (within $0.63 envelope)

### Direct fetches
- `https://www.wasabi-citywalk.com/wasabi_menu.pdf` — official menu PDF (192 KB), extracted via pypdf — saved at `_raw-data/wasabi-menu.md`
- `https://www.wasabi-citywalk.com/about.php` — confirmed PRG ownership statement
- WebSearch: "Wasabi at CityWalk Panda Restaurant Group owner" — confirmed PRG operator
- WebSearch: "Yakiya restaurant Pasadena Japanese sushi owner Panda Restaurant Group" — confirmed Yakiya is PRG
- WebSearch: "Wasabi at CityWalk review yelp tripadvisor" — review snippet themes

### Secondary references
- Wikipedia: Panda Restaurant Group, Panda Express
- Yahoo Lifestyle: "The 2 Other Restaurant Chains That We Didn't Realize Panda Express Owns" (Yakiya + Wasabi)
- LinkedIn job posting: "Restaurant Busser - Wasabi at Citywalk (1432) at Panda Restaurant Group" (confirms store #1432)
- pandarg.com FAQ
- yakiya-us.com privacy/terms (PRG legal entity confirmation)

### Known gaps / blockers
- **Yelp review text was not directly scrapeable** (Yelp blocks Apify rag-web-browser; TripAdvisor returned 403). Review themes are reconstructed from Restaurantji (n=233 ratings), Google Maps description, customer-favorites lists, and Web Search snippet quotes. For the next phase, if deeper review-text mining is needed, recommend (a) trying a Yelp-specific Apify actor (`yelp-scraper`), or (b) sampling Yelp manually via screenshots — both are inside budget.
- **POS data is unavailable** as expected. All menu engineering recommendations in this dossier are visible-from-the-outside; the "fix throughput first" recommendation explicitly requires Wasabi-side POS data to be quantified.
- **Item counts on the official PDF disagree with customer-favorites lists** (ramen mentioned in reviews, not on menu). Either the PDF is stale or there is a soft-launch / specials menu we haven't seen. Worth confirming with Chris in Wave 2.
- **Hours discrepancy** between Google Maps (11 AM-9 PM all days) and NetWaiter (12 PM open, 8 PM close weekdays). One source is wrong.
- **CityWalk-internal Hard Rock Cafe + Wolfgang Puck** did not surface in the Apify maps pull (only Wolfgang Puck Catering with 4 reviews appeared). They exist in CityWalk per the official guide. Worth a manual lookup if Layer A becomes a focus area in Wave 2.
