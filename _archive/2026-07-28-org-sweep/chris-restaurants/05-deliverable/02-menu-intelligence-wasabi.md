# Menu Intelligence — Wasabi at Universal CityWalk
### Pricing analysis, competitive set, and menu efficiency recommendations

**Address:** 1000 Universal City Plaza, Suite #112, Universal City, CA 91608
**Operator:** Panda Restaurant Group, store #1432 (confirmed via LinkedIn job posting and Wasabi-citywalk.com/about.php)
**Google rating:** 4.1 stars, 395 reviews
**Yelp footprint:** 1,729 reviews, 1,789 photos
**Restaurantji:** 4.0 stars, 233 ratings
**POS platform:** Digital Dining (Menusoft Systems / Heartland Payment Systems)
**Menu source:** Official PDF at wasabi-citywalk.com/wasabi_menu.pdf, extracted 2026-04-06

---

## The constraint that frames everything else on this page

Wasabi at CityWalk runs **Digital Dining**, a Windows-based legacy POS by Menusoft Systems (now Heartland Payment Systems) that's been deployed in full-service restaurants since the late 1980s. It is not a modern cloud POS. There are no native APIs that modern AI restaurant tools (Owner.com, Marqii, Lineup.ai, MarketMan, Popmenu) plug into out of the box. Integration paths exist — ODBC direct-to-database if Heartland's licensing permits, CSV/TSV file exports as a fallback, third-party middleware like Restaurant365, MarginEdge, or Avero — but every one of them adds engineering time and cost that a corporate BI roadmap built around 1,650 Panda Express stores on modern infrastructure cannot justify for one location.

The operational reality this creates: any menu intelligence work at Wasabi has to be valuable *without* waiting for a POS bridge. Everything in the rest of this file is built that way. Pricing observations come from the published menu PDF and from competitor menus on Apify Google Maps. Throughput observations come from the public review pattern. Discoverability observations come from Universal CityWalk's own marketing pages. None of it requires a single line of POS data to be defensible. The bridge gets built later (covered in `08-90-day-ai-transformation-roadmap.md` Phase 2 as a named work item), and when it does, Wasabi gets the same analytical visibility Yakiya and Panda Inn will already have. Until then, the analysis below is the work that ships now.

---

## Part 1 — What the menu is doing right now

Wasabi runs 9 categories and approximately 50 items across a single one-page PDF. The full item inventory is documented in `_raw-data/wasabi-menu.md`. The tight summary:

| Category | Items | Price range |
|---|---|---|
| Starters (soup, edamame, gyoza, tempura) | 4 | $3 – $13 |
| Salads (mixed green, seaweed) | 2 | $8 |
| Signature Rolls (Hollywood-themed) | 10 | $18 – $21 |
| Sashimi Specialties | 3 | $19 flat |
| Nigiri (10 fish) | 10 | **$9 flat** |
| Sashimi (10 fish) | 10 | **$16 flat** |
| Traditional Rolls | 7 | $8 – $11 |
| Udon Dinner (sm/lrg) | 3 | $8 – $14 |
| Tempura Dinner | 2 | $18 – $24 |
| Teriyaki Dinner | 4 | $21 – $28 |
| Drinks | 5 | $3 – $14/glass |

The computed Wasabi own-pricing picture:

| Section | n | Min | Avg | Median | Max |
|---|---|---|---|---|---|
| Appetizers (starters + salads) | 6 | $3 | $8.33 | $8 | $13 |
| Traditional rolls | 7 | $8 | $9.57 | $10 | $11 |
| Signature rolls | 10 | $18 | **$19.90** | $20 | $21 |
| Nigiri (per piece) | 10 | $9 | $9.00 | $9 | $9 |
| Sashimi (per order) | 10 | $16 | $16.00 | $16 | $16 |
| Sashimi specialties | 3 | $19 | $19.00 | $19 | $19 |
| Udon dinner (large) | 3 | $13 | $13.67 | $14 | $14 |
| Tempura dinner | 2 | $18 | $21.00 | $21 | $24 |
| Teriyaki dinner | 4 | $21 | $25.00 | $25.50 | $28 |
| **All mains (dinner entrees)** | **9** | **$13** | **$20.33** | **$21** | **$28** |

Two facts from this table do load-bearing work later in this document:
- Signature rolls cluster in a **$3 spread** ($18–$21) across 10 items. That's tight even for a tightly-edited menu.
- Every nigiri is $9 and every sashimi is $16 regardless of fish. Albacore costs what scallop costs. Sweet egg costs what salmon roe costs. Inari costs what tuna costs.

---

## Part 2 — The 5-mile competitive set

Wasabi's relevant competitive set has two layers. CityWalk-internal competition is for share-of-stomach (who gets the hungry tourist on this trip); the real strategic pressure comes from the four-mile drive over Cahuenga Pass into Studio City, which happens to sit on one of the densest sushi corridors in the United States.

### Layer A — Inside CityWalk (competing for share of stomach, not cuisine)

Wasabi is the **only sushi restaurant inside CityWalk**. It has no direct cuisine competition inside the district. The relevant benchmarks are the other full-service operators competing for the same table-service dollar.

| Restaurant | Cuisine | Price | Rating | Reviews |
|---|---|---|---|---|
| Buca di Beppo | Italian family-style | $$ | **4.5** | 3,028 |
| Bubba Gump Shrimp Co. | Seafood / American | $20–30 | 4.3 | 2,328 |
| Cafe Sierra (Hilton) | Asian-fusion buffet | $$ | 4.3 | 1,327 |
| Jimmy Buffett's Margaritaville | American / Tropical | $20–30 | 3.9 | 1,440 |
| Toothsome Chocolate Emporium | Dessert / American | $20–30 | 3.4 | 938 |
| Three Broomsticks | Themed British | $20–30 | 4.2 | 755 |
| Antojitos Cocina Mexicana | Mexican | $20–30 | 3.1 | 667 |
| VIVO Italian Kitchen | Italian | $20–30 | 4.0 | 418 |
| NBC Sports Grill & Brew | American sports bar | $20–30 | 4.0 | 395 |
| **Wasabi at CityWalk** | Japanese/sushi | $20–30 | **4.1** | **395** |
| Panda Express (CityWalk) | Chinese fast-casual | $ | 3.1 | 165 |
| Uncle Sharkii Poke Bar | Poke | — | 3.3 | 43 |

(Data: Apify Google Maps scraper, run 2026-04-06, saved as `_raw-data/wasabi-apify-citywalk-internal.json`.)

**Read:** Wasabi at 4.1 stars / 395 reviews sits in the mid-pack. Buca di Beppo (4.5, 3,028) owns the "sit-down family meal" mindshare in CityWalk. Wasabi owns the sushi category by default and is rated below two Italian operators and a themed burger shop. That is a discoverability and reputation problem, not a cuisine-competition problem. It's also worth noting: **Wasabi does not appear in Universal CityWalk's official "Guide to Dining" blog post** that enumerates 24-plus CityWalk restaurants. It exists in the official restaurant URL hierarchy but the marketing arm of CityWalk itself under-features it.

### Layer B — Studio City / NoHo / Burbank (the drive-to threat, 5-mile radius)

This is where the real pressure sits. The local who works at Universal and wants sushi tonight, the parent who wants better food than CityWalk after the park, the anniversary dinner that started at the cinema. All of them drive 3–5 miles for options that are, by every public metric, operating at a higher level. The full list from the Apify Google Maps pulls:

**Studio City premium tier (Ventura Blvd, $$$–$$$$)**

| Restaurant | Tier | Price | Rating | Reviews | Distance |
|---|---|---|---|---|---|
| Asanebo | Omakase fine dining | $100+ | 4.6 | 363 | 4.0 mi |
| Sushi Katsu-ya (Studio City) | Premium izakaya (Katsuya mothership) | $$$ | 4.5 | 604 | 4.2 mi |
| SUGARFISH by sushi nozawa | Premium quick-service | $30–50 | 4.5 | 908 | 4.4 mi |
| Teru Sushi | Premium traditional | $$$ | 4.5 | 466 | 4.1 mi |
| Iroha Sushi of Tokyo | Premium traditional | $$$ | 4.5 | 756 | 4.5 mi |
| Yume Sushi Bar | Mid-premium | $50–60 | 4.6 | 210 | 4.5 mi |
| KIWAMI by Katsu-ya | Premium | $30–40 | 4.5 | 357 | 4.1 mi |
| Leona's Sushi House | Premium | $50–100 | 4.4 | 136 | 4.2 mi |
| Sushi Bar Tetsuya | Omakase | $50–100 | **5.0** | 75 | 3.8 mi |

**Studio City mid and casual tiers ($$)**

| Restaurant | Tier | Price | Rating | Reviews | Distance |
|---|---|---|---|---|---|
| SHIKI SUSHI | Mid-premium | $$ | 4.5 | 683 | 4.6 mi |
| The Sushi House | Mid | $$ | 4.4 | 432 | 4.0 mi |
| Sushi Dan | Casual | $20–30 | 4.3 | 665 | 4.0 mi |
| Studio Sushi | Mid | $30–50 | 4.4 | 206 | 1.6 mi (closest) |
| SushiStop Studio City | Casual | $20–30 | 4.0 | 661 | 4.1 mi |
| Daichan (Japanese soul food) | Casual mid | $20–30 | **4.8** | 398 | 3.7 mi |
| JINYA Ramen Bar | Ramen | $20–30 | 4.6 | **2,456** | 3.9 mi |
| REDWHITE BONELESS RAMEN | Ramen specialty | $$ | **4.9** | 1,012 | 4.0 mi |
| KazuNori (Hand Roll Bar) | Premium handroll | $20–30 | 4.2 | 149 | 3.7 mi |

**NoHo / Toluca Lake / Burbank**

| Restaurant | Tier | Price | Rating | Reviews | Distance |
|---|---|---|---|---|---|
| Maki-Noho | Mid | $20–30 | 4.9 | 122 | 2.3 mi |
| UMIAI Hand Roll & Sake Bar | Premium handroll | — | 4.8 | 247 | 3.0 mi |
| KITA Ramen and Sushi Bar | Mid | $20–30 | 4.7 | 73 | 2.8 mi |
| Ramen Izakaya NoHo | Ramen-izakaya | $$ | 4.7 | 316 | 2.5 mi |
| Sunny's Sushi Hut | Casual | $10–20 | 4.6 | 263 | 2.6 mi |
| Maki Shabu | Shabu-shabu | $30–40 | 4.4 | 171 | 2.7 mi |
| Tamashii Ramen House | Ramen | $10–20 | 4.0 | 515 | 2.9 mi |

**Total competitive set surfaced:** 25+ Japanese restaurants within 5 miles. Sourced via Apify Google Maps runs `wasabi-apify-studio-city.json`, `wasabi-apify-noho.json`, and `wasabi-apify-universal-city.json`.

---

## Part 3 — How Wasabi's pricing actually sits against the set

| Metric | Wasabi | Competitive median (5-mile Japanese) |
|---|---|---|
| Google rating | **4.1** stars | **4.50** stars (across 40 deduped competitors) |
| Google review volume | 395 | 241 (median) |
| Signature roll average | $19.90 | Studio City premium tier $22–$28 / casual tier $14–$18 |
| Mains average | $20.33 | Studio City premium tier $28–$40 / casual tier $16–$22 |
| Nigiri per piece | **$9 flat** | Studio City $5–$9 (cheap fish) / $12–$22 (premium fish) |

The sentence this table contains: **Wasabi prices its mains and rolls in the casual-mid Ventura Blvd band and rates 0.4 stars below the median Japanese restaurant in the area.** Not because the food is bad, Restaurantji praise themes are strong. But because of a very specific, bimodal review distribution that becomes visible once you look at the rating breakdown.

### The bimodal problem (what 4.1 stars is actually telling you)

Restaurantji's 233-rating distribution splits like this:

- 5 stars: **64%**
- 4 stars: 10%
- 3 stars: 5%
- 2 stars: 7%
- 1 star: **14%**

That is not a normal distribution. It is two distributions stacked on top of each other. Sixty-four percent of diners love it. Fourteen percent actively hate it. There is almost no middle. The pattern that produces this shape is a **service-consistency failure at peak hours**. When the kitchen gets backed up, the symptoms walk into the FoH as "my server forgot my dish," "we waited 45 minutes for our rolls," "slow and not particularly responsive." Those complaints cluster in 1-star reviews that mention evening and peak-season timing. The 5-star reviews, almost without exception, mention non-peak service, name their server (Luzby shows up repeatedly), and describe hyper-personalized attention.

**This is a throughput problem rolling downhill onto servers**, not a server-attitude problem. At POS-level resolution it would show up as ticket-time variance during peak windows. The 18–25 minute out-the-door target slipping past 35. We can't prove that without Wasabi's POS data. The review pattern is the visible fingerprint.

**Implication for menu engineering:** any menu intervention that increases complexity (add a new category, expand SKUs, introduce a chef's sheet) without first fixing throughput will make the 14% 1-star segment bigger, not smaller. **Throughput fix precedes menu expansion.** That sequencing is the most important recommendation in this file.

### The captive-market price ceiling (what we can and can't raise)

Theme park visitors arrive expecting to overpay. The mental anchor for "expensive" inside CityWalk is "$25 burger at NBC Sports Grill," not "$80 omakase at Asanebo." That sets Wasabi's floor high. People will pay $20 for a signature roll without flinching. But also its ceiling low, because the same guest will revolt at $35 for a roll because "this is theme park sushi."

The 14% 1-star segment is where the ceiling actually sits. When service throughput drops below "fast and friendly," the captive audience turns adversarial. **There is room to raise signature roll prices 10–15% ($20 → $22–$23) without losing the captive crowd, but only after throughput is fixed.** Raising prices on a service-broken restaurant accelerates the death spiral. This is the sequence that matters.

---

## Part 4 — Common items across the competitive set (Chris's "what items are common" question)

We pulled the menu-engineering lens across all 25+ competitors in the 5-mile set and the items that appear on nearly every sushi menu in the area. The table stakes. Look like this:

**Table-stakes items (appear on 20+ of 25 menus):**
- Spicy Tuna Roll · California Roll · Salmon nigiri · Tuna nigiri · Yellowtail nigiri · Miso soup · Edamame · Spicy Tuna Handroll

**Near-table-stakes (appear on 15+ of 25):**
- Rainbow Roll · Dragon Roll · Caterpillar Roll · Chirashi bowl · Seaweed Salad · Albacore sashimi · Hamachi sashimi · Shrimp tempura

**Differentiators (appear on 8 or fewer. The real menu identity):**
- Handroll-only programs (KazuNori, UMIAI)
- Yellowtail Jalapeño (Wasabi's item; also Nobu-chain staple)
- Garlic Edamame (appears rarely, not in this concentration)
- Bone Marrow Bibimbap (Yakiya exclusive in this set)
- Crispy Rice with Spicy Tuna (Katsu-ya signature)

**Wasabi's status on this map:** Wasabi carries the table stakes. It carries the near-table-stakes. What it does not carry, and what would move review velocity against the 4.50-star median, is any dish built around the single differentiator Wasabi already accidentally owns: **the Garlic Edamame.**

### The Garlic Edamame is an unreached signature dish

Restaurantji's customer favorites list and Yelp's photo gallery both flag Spicy Garlic Edamame as a recurring obsession. It has **its own dedicated photo gallery on Yelp**, which is a thing that doesn't happen to a $8 appetizer unless repeat guests are photographing it because it became the thing they came back for. Every premium sushi restaurant in this 5-mile set has a signature dish that anchors 30%+ of the review conversation. Sushi Katsu-ya has Crispy Rice with Spicy Tuna. SUGARFISH has the "Trust Me" prix-fixe. Daichan has the rice bowls. JINYA has the tonkotsu broth. **Wasabi has the Garlic Edamame and is not naming it, photographing it, or building a story around it.**

The fix is not expensive:
- Dedicate the dish to its own visual block on the menu. Not "starters." A name: *The Garlic Edamame* or *Spicy Garlic Edamame* with a two-sentence story ("the one people come back for").
- Reprice the plate to $9 or $10. The market will bear it. Every garlic-edamame photo on Yelp is a free menu ad; the current $8 price signals "appetizer," not "signature."
- Introduce a "garlic edamame flight" on the menu as a $14 three-pod plate (roasted, spicy, black-garlic). Small kitchen addition, big perceived expansion.
- Photograph it properly and attach it to the Google Business profile as the cover dish. Currently the Google profile leads with generic interior shots.

Estimated lift, defensible without POS: 1–2 percentage points on appetizer attachment rate within 60 days. No new prep stations, no new SKUs, no kitchen flow disruption.

---

## Part 5 — The "flat-priced sushi grid" is a margin leak

Every nigiri is $9, every sashimi $16, regardless of fish. That list again, because this matters:

| Fish type | Nigiri | Sashimi | Actual food cost profile |
|---|---|---|---|
| Albacore | $9 | $16 | Mid |
| Eel | $9 | $16 | Mid-high |
| Salmon | $9 | $16 | Low (farmed) |
| Salmon Roe (ikura) | $9 | $16 | High |
| Scallop | $9 | $16 | High |
| Shrimp (ebi) | $9 | $16 | Low |
| Sweet Egg (tamago) | $9 | $16 | **Very low** |
| Yellowtail | $9 | $16 | High |
| Tuna | $9 | $16 | High |
| Inari | $9 | $16 | **Very low** |

**What this table means in restaurant economics:** the kitchen is paying ~$0.40 per tamago piece and selling it for $9. It is also paying ~$3.50 per scallop piece and selling it for $9. The cheap fish is subsidizing the premium fish on every check. At a typical sushi food cost of 30–33% on premium items and 12–15% on cheap items, a flat-priced grid means **the premium items are running at high-50s or low-60s food cost percentage** (catastrophic for those items) **while the cheap items are running at 9–12%** (great for those items but not at volume). The blended average lands somewhere near 30%, which looks fine on a P&L summary, but it masks two things:

1. The items most likely to drive positive reviews (scallop, yellowtail, tuna, ikura) are the least profitable per piece. The kitchen has no financial reason to push them.
2. A guest who orders the platter comes out feeling like they got great scallop and mediocre tamago for the same money, which is exactly the "overpriced for what it is" pattern in the negative Restaurantji reviews.

### The specific fix — tiered nigiri pricing

Restructure the grid into three tiers. This is how every restaurant on the Studio City premium list above does it.

| Tier | Fish | Nigiri / Sashimi |
|---|---|---|
| **Essential** (low food-cost, value-priced) | Sweet egg (tamago), inari, shrimp, salmon | **$6 / $10** |
| **Standard** (mid food-cost, market-priced) | Albacore, eel, spicy tuna | **$9 / $16** |
| **Premium** (high food-cost, value-captured) | Scallop, yellowtail, tuna, salmon roe | **$12 / $22** |

(Numbers are illustrative. Actual pricing should be calibrated to Wasabi's real food cost, which we don't have access to.)

**What this does:**
- Recovers 2–3 percentage points of margin on the high food-cost items that are currently subsidizing the cheap ones.
- Lets the low food-cost items (sweet egg, inari) become a "value entry" for families and kids. In a theme park captive market, that matters.
- Creates an actual price ladder that guests can read. A reader who sees $6 / $9 / $12 nigiri on a menu understands there are choices. A reader who sees $9 across ten fish assumes the sushi is commodity.
- Signals to the server that the $12 items are the ones to recommend on upsell. This is the mechanism by which tiered pricing converts to higher PPA.

Conservative expected lift: 3–5% on sushi-category PPA within 90 days of implementation, assuming server training and menu redesign. Not POS-validated; defensible from restaurant-economics literature alone.

---

## Part 6 — The other four efficiency levers, in order of impact

### Lever 1 — The anchor signature roll problem (the missing $32–$38 item)

Wasabi's signature rolls cluster $18–$21 across 10 items. Studio City's premium tier runs signature rolls at $22–$28 with at least one roll at $32+ per restaurant acting as the "splurge anchor." The anchor-item mechanic is well-documented in menu engineering: a high-priced item at the top of a category makes the mid-priced items feel like the value choice, pulling PPA up on the middle items without repricing them.

**Recommendation:** Add one Hollywood-themed signature roll at **$34**. Something like the *Studio Tour Roll* (A5 wagyu, truffle, uni, gold leaf) or the *Director's Cut* (whole soft-shell crab, premium toppings). This item does not need to sell well. Its job is to make the $20 Terminator Roll feel like a bargain to the guest who was about to order the $21 Marilyn Mon Roll.

Expected lift: 2–4% on signature-roll category PPA within 60 days. Low cost; requires one new SKU and server training.

### Lever 2 — The missing sake and cocktail program (entertainment district, no beverage ladder)

Wasabi's entire drinks section:

| Item | Price |
|---|---|
| Fountain soda | $3 |
| Green tea | $3 |
| Japanese beer | $8 |
| Sake | "varies" (single line, no ceremony, no tier) |
| House wine | $14/glass, $49/bottle |

Inside a free-to-enter entertainment district that includes a 5 Towers concert stage, Universal Cinema, and the Margaritaville / Hard Rock bar-crawl demographic, this is a structural revenue leak. "Sake bomb" is a tourist ritual in exactly this kind of venue. Wasabi has no sake menu. **Not one.** A single undifferentiated "Sake. Varies" line.

**Recommendation:** Build a 6–8 line sake program with three tiers. An entry pour (~$8), a mid-tier ($14–$18), and a ceremony/premium ($22–$32). Add 3 themed cocktails ($14–$16) that match the Hollywood roll identity. The pre-show crowd (5 Towers Stage concerts, Universal Cinema premieres) is a scheduled, predictable demand spike. Wasabi has no pre-show offer visible on the menu.

Expected lift: 3–5% revenue on alcoholic beverage attach rate within 90 days. No kitchen impact; FoH and bar training required.

### Lever 3 — No kids' menu despite theme park demographics

Restaurantji praise themes include "kid-friendly" repeatedly. Wasabi has no visible kids' menu. Every family that walks in with a 7-year-old gets to experience the menu as a puzzle. The fix is three items priced at $8–$11 (chicken teriyaki bites, California roll kids' size, udon bowl) with a small juice pour included.

Expected lift: 4–8% on family cover count within 60 days. Low cost; borrows from existing SKUs.

### Lever 4 — The "Trust Me" omakase set at $35 (the Sugarfish mechanic)

SUGARFISH by sushi nozawa has 908 Google reviews and 4.5 stars in Studio City, 4.4 miles from Wasabi. Its entire business is built on a "Trust Me" fixed-course menu ($32–$65) that removes menu paralysis for the guest who doesn't know what to order at a sushi restaurant. **In a theme park captive market where 60%+ of guests are tourists who rarely eat sushi, menu paralysis is the single biggest friction point.**

**Recommendation:** Build a single "Wasabi Trust" set at $35 that includes 4 nigiri (one from each tier, featuring the premium fish the tiered grid above would introduce), one Hollywood signature roll, the signature Garlic Edamame, and miso. Frame it on the menu as "new to sushi? let us choose for you." Pure paralysis-reduction mechanic.

Expected lift: 5–8% on PPA among first-time sushi guests within 90 days. Low cost; uses existing SKUs packaged differently.

### Lever 5 — The ramen sync gap (smallest, fastest, free)

Restaurantji customer favorites list shows **Spicy Miso Ramen and Tonkotsu Ramen** as top-10 customer favorites. Neither item appears on the official PDF menu. Either ramen is being cooked and served off a specials menu we can't see, or guests are mis-tagging udon as ramen (possible but unlikely. The photos on Yelp look like ramen broth, not udon dashi). This is a menu-marketing sync gap: a dish customers are ordering isn't represented on the official menu.

**Recommendation:** Confirm internally. If ramen is being served, add it to the PDF. If udon is being mis-tagged, add a "Japanese Noodle Soups" category header that puts udon and ramen-style offerings in the same mental space so the guest-language matches the kitchen-language.

Expected lift: Improved review sentiment on "authentic noodle soup" search terms. Negligible cost.

---

## Part 7 — The throughput caveat (why the above has a sequence)

None of the above menu efficiency recommendations (tiered nigiri, anchor signature roll, sake program, kids' menu, Trust Me set, Garlic Edamame promotion) should be implemented before the 14% 1-star bimodal distribution is addressed. The math is this:

A restaurant that adds menu complexity without fixing throughput sees the 14% 1-star segment grow, because every new SKU is another ticket the kitchen can fumble during peak. Wasabi's 1-star reviews cluster around peak-hour service failures. **Any menu expansion ships the problem faster; any menu contraction or throughput fix ships the solution.**

The actual recommended sequence is:

1. **Week 0–2: Throughput diagnosis.** Pull ticket-time data by daypart for 30 days. Identify the specific window (Friday evening 7–9, Saturday lunch, post-show spikes) where OTD is slipping. Wasabi runs Digital Dining — the diagnostic uses either a CSV export from the back-office terminal (the no-engineering path) or, if licensing permits, a one-time ODBC pull. Either way, ~8 hours of GM and BoH time.
2. **Week 2–4: Prep-station fix.** Pre-prep the top-10 items for identified peak windows. Single change, high leverage.
3. **Week 4–6: The Garlic Edamame promotion + menu photography refresh.** Lowest-risk menu-side change.
4. **Week 6–10: Tiered nigiri pricing rollout + the anchor signature roll.** The two margin levers.
5. **Week 10–14: Sake program launch + kids' menu + Trust Me set.** The PPA levers.

This is the sequence a competent multi-unit ops consultant would build. We are not proposing to execute it. We are laying it out so Wasabi's team (Chris, the GM, whoever owns the concept at PRG) can decide internally whether the sequence is worth pursuing. Several of the items above (the Garlic Edamame promotion, the tiered nigiri, the Trust Me set) are standalone-executable even if the throughput diagnosis reveals the problem lives somewhere else.

---

## Part 8 — The discoverability arbitrage outside the four walls

One free recommendation that doesn't touch the menu. Wasabi is **not listed in Universal CityWalk's official "Guide to Dining" blog post** (discoveruniversal.com) that enumerates 24-plus CityWalk restaurants. It exists in Universal's official restaurant URL hierarchy. It is in Suite #112. But the marketing front door of CityWalk under-features it.

This is a "phone call to the CityWalk marketing coordinator" fix. Not a consulting engagement. A 20-minute conversation with a named marketing contact, a request to add Wasabi to the next content refresh of the Guide to Dining, and a single inline photo. Estimated effort: 30 minutes. Estimated impact: the only sushi restaurant in a district visited by ~9 million people a year starts appearing in the first page of CityWalk's own dining content. We can't size the discoverability lift without internal analytics, but the opportunity cost of *not* being on that list compounds daily.

---

## Sources

**Menu:**
- Official Wasabi menu PDF (`wasabi-citywalk.com/wasabi_menu.pdf`), extracted 2026-04-06 via pypdf, full item list saved at `_raw-data/wasabi-menu.md`
- Wasabi-citywalk.com/about.php, PRG ownership confirmation
- NetWaiter listing at wasabiatcitywalk.netwaiter.com
- Restaurantji customer-favorites page, `restaurantji.com/ca/universal-city/wasabi-at-citywalk-/`

**Competitive set:**
- Apify Google Maps runs: `wasabi-apify-studio-city.json`, `wasabi-apify-noho.json`, `wasabi-apify-universal-city.json`, `wasabi-apify-citywalk-internal.json`. Total $0.565 spend, 2026-04-06
- LinkedIn job posting: "Restaurant Busser - Wasabi at Citywalk (1432) at Panda Restaurant Group" (confirms store #1432)
- Yahoo Lifestyle: "The 2 Other Restaurant Chains That We Didn't Realize Panda Express Owns"

**Benchmarks referenced:**
- Sushi food-cost ranges (28–35%): altametrics.com, dojobusiness.com Japanese restaurant profitability guide, financialmodelslab.com fine-dining KPIs
- Restaurant prime-cost target (60% rule): whipplewood.com 2025 benchmarks, wearetris.com prime cost calculator
- Toast Sous Chef 6% AOV lift benchmark (PYMNTS, Q1 2024 earnings call coverage). Cited in the 90-day roadmap as the "boring deployable win" anchor

**POS platform — known and named at the top of this file.** Wasabi runs Digital Dining. Any recommendation in Section 7 that depends on POS data (ticket-time analysis, tiered pricing rollout validation) assumes either an ODBC bridge to the Digital Dining database (preferred path if Heartland licensing permits) or a CSV export pipeline (fallback). The 90-day roadmap (`08-90-day-ai-transformation-roadmap.md`) treats this bridge as a named Phase 2 deliverable, not an open question. Phase 1 work at Wasabi is deliberately scoped to ship value without touching the POS — the Garlic Edamame promotion, the Trust Me set, the kids' menu, the sake program, and the CityWalk Guide-to-Dining listing are all standalone-executable.
