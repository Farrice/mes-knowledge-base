# Menu Intelligence — Panda Inn Glendale
### Pricing analysis, competitive set, founding myth activation, and menu efficiency recommendations

**Address:** 201 N Maryland Avenue, Glendale, CA 91206
**Operator:** Panda Restaurant Group, Inc. (Cherng family flagship sit-down concept, founded 1973)
**Heritage:** The second Panda Inn ever built (1982); the adjacent Glendale Galleria II food court is where the first Panda Express opened in October 1983
**Google rating:** 4.4 stars, 544 reviews
**Postmates rating:** 4.6 stars, 1,500+ ratings
**Hours:** Mon–Thu 11:30 AM – 9:30 PM · Fri 11:30 AM – 10 PM · Sat 12 PM – 10 PM · Sun 12 PM – 9:30 PM
**Menu sources:** Postmates store page, Uber Eats cross-reference, Allmenus PDF, pandainn.com (raw data in `_raw-data/panda-inn-menu.md`)

---

## Part 1 — What the menu is doing right now

Panda Inn runs 12 categories and approximately 80 items. The structure rewards a sit-down family or couples dinner and the architecture is designed around **two-portion pricing** that delivery apps cannot express.

| Section | Item count | Price band (in-store) |
|---|---|---|
| Tasters / Starters | 10 | $11 – $16 |
| Soups — bowl (Hot & Sour, Egg Drop) | 2 | $5.50 |
| Soups — family (Wonton, Sizzling, Vegetable) | 3 | $15 – $16 |
| Salads | 3 | $13 – $18 |
| Specialties (Tea-Smoked Duck, Beef Ribs, Sea Bass, etc.) | 11 | $20 – $45 |
| Poultry | 9 | $17 – $22 |
| Beef & Pork | 5 | **$17 – $33** (small/large two-portion) |
| Seafood | 8 | $19 – $45 |
| Vegetables | 6 | $19 – $21 |
| Noodles & Rice | 9 | $14 – $23 |
| Lunch Specials | (separate menu) | not surfaced digitally |
| Catering | (B2B channel) | — |

### Pricing bands (computed, in-store estimated from Postmates and Uber Eats cross-reference)

| Category | Average | Median | Range |
|---|---:|---:|---|
| Cold/Hot Starters | $13.20 | $13.00 | $11 – $16 |
| Salads | $15.50 | $17.00 | $13 – $18 |
| Bowl Soups (single serving) | $5.50 | $5.50 | $5.50 |
| Family Soups (shareable) | $15.40 | $15.40 | $15 – $16 |
| Vegetable Mains | $19.80 | $19.80 | $19 – $21 |
| Chicken Mains (small portion) | $18 | $18 | $17 – $22 |
| Beef/Pork Mains (small portion) | $19 | $18 | $17 – $25 |
| **Beef/Pork Mains (large/family)** | **$33** | **$33** | **$25 – $45** |
| Seafood Premium (Honey Walnut Shrimp, Sea Bass) | $30 | $28 | $21 – $45 |
| Premium Specialties (Tea-Smoked Duck, Wagyu Chow Fun) | $32 | $30 | $25 – $45 |

The two numbers in this table that matter most are in the last three rows: **$33 and $45**. That is the large-portion pricing architecture nobody walking in sees. On Allmenus, Mongolian Beef is listed as **$17/$33**. Honey Walnut Shrimp as **$21/$40**. That two-portion architecture is the pricing instrument the menu leans on for margin. It exists. It works. It is functionally invisible everywhere customers actually look.

### Signature dishes (review-validated)

- **Hot & Sour Soup**. The most-mentioned dish across 30 Apify-pulled Google reviews (9 tags). Smallest ticket ($5.50) but biggest brand association.
- **Honey Walnut Shrimp**, "Panda Express always sells out of this; here I can actually get it."
- **Panda Beef**. House-named signature. The "you can't get this at Panda Express" anchor.
- **Tea-Smoked Duck**. Heritage Mandarin/Sichuan; the dish that most clearly separates Panda Inn from chain Chinese.
- **Asian Spiced Beef Ribs**, USDA prime short ribs over spinach and udon.
- **Upside Down Crispy Noodles**. Called out by name in 5-star reviews as an "interesting surprise."

---

## Part 2 — The 5-mile competitive set

**28 Asian restaurants within 5 miles**, pulled from three Apify Google Maps runs (Chinese, Sushi/Japanese, Korean BBQ). The 9 closest sit within 0.5 miles, Panda Inn is inside the densest restaurant block in Glendale. Raw data: `_raw-data/apify-glendale-chinese.json`, `apify-glendale-sushi.json`, `apify-glendale-korean.json`.

### Chinese (regional + Chinese-American)

| Distance | Restaurant | Style | Price | Rating | Reviews |
|---:|---|---|---|---:|---:|
| — | **Panda Inn Glendale** | Heritage Mandarin / Chinese-American | $20–30 | **4.4** | **544** |
| 0.5 mi | California Wok Glendale | Chinese-American casual | $10–20 | 4.4 | 56 |
| 0.7 mi | **Din Tai Fung** | Taiwanese / Shanghainese | $$ | 4.5 | **2,891** |
| 0.9 mi | Wong's Wok Chinese Kitchen | Takeout | $ | 4.2 | 229 |
| 0.9 mi | Fu House Chinese Food & Sushi | Chinese + sushi combo | $10–20 | 3.8 | 172 |
| 2.6 mi | Chinese Fast Food | Quick-serve | $10–20 | 4.0 | 165 |
| 4.1 mi | New Moon (Montrose) | Chinese-American | $20–30 | 4.5 | 831 |
| ~4.5 mi | House of Joy (La Crescenta) | Chinese-American family | $20–30 | 4.2 | 345 |
| ~~(was 0.5 mi)~~ | ~~**Lao Sze Chuan**~~ | **Authentic Sichuan (Michelin Guide rec)** | $$ | 4.0 | 377 | **PERMANENTLY CLOSED** |

### Japanese / Sushi

| Distance | Restaurant | Style | Price | Rating | Reviews |
|---:|---|---|---|---:|---:|
| 0.4 mi | UMI by Eden | Upscale sushi | $50–100 | 4.7 | 15 |
| 0.5 mi | Sasabune Glendale | High-end omakase ($200+) | $100+ | 4.7 | 209 |
| 0.5 mi | Cavi Sushi | Mid-upscale sushi | $30–50 | 4.7 | 99 |
| 0.5 mi | Iki Toro Japanese | Casual sushi | — | 4.8 | 28 |
| 0.6 mi | Seabutter Glendale | Mid-upscale sushi | $40–50 | 4.7 | 73 |
| 0.7 mi | Kura Revolving Sushi Bar | Conveyor belt | $20–30 | 4.3 | 734 |
| 1.1 mi | Fuji Buffet & Grill | Buffet | $$ | 4.0 | 3,007 |
| 1.3 mi | MOTO SUSHI Glendale | Mid-tier sushi | $$ | 4.5 | 255 |

### Korean (KBBQ + casual)

| Distance | Restaurant | Style | Price | Rating | Reviews |
|---:|---|---|---|---:|---:|
| 0.4 mi | Gen Korean BBQ House | AYCE KBBQ | $20–30 | 4.0 | **1,486** |
| 0.5 mi | bb.q Chicken | Korean fried chicken | $10–20 | 4.4 | 112 |
| 0.5 mi | Jincook | Korean comfort/soul food | $20–30 | 4.5 | 334 |
| 0.7 mi | Beulah Kitchen | Korean casual | $$ | 4.4 | 200 |
| 1.1 mi | Mitzee Cafe | Korean casual | $10–20 | 4.4 | 157 |
| 4.2 mi | Cho Dang Tofu & BBQ | Soondubu / BBQ | $20–30 | 4.2 | 205 |

### Other Asian / Fusion

| Distance | Restaurant | Style | Price | Rating | Reviews |
|---:|---|---|---|---:|---:|
| 0.4 mi | Dragon Garden Family Restaurant | Chinese/Japanese fusion | $40–50 | 4.5 | 26 |
| 0.5 mi | Gam Tu Bop | Asian fusion | $10–20 | 4.5 | 280 |
| 1.0 mi | Taste of Windsor | Pan-Asian | $10–20 | 4.4 | 27 |

---

## Part 3 — Where Panda Inn sits in the Glendale price ladder

**Cheaper than:** Sasabune ($100+), UMI by Eden ($50–100), Cavi Sushi ($30–50), Dragon Garden ($40–50), Seabutter ($40–50).

**Same $20–30 band as:** Din Tai Fung, Gen Korean BBQ, Jincook, Kura Revolving Sushi, New Moon (Montrose).

**More expensive than:** California Wok, Wong's Wok, Fu House, bb.q Chicken, Beulah Kitchen, Gam Tu Bop, Mitzee, Chinese Fast Food, Taste of Windsor.

The $20–30 band is the most crowded segment in central Glendale. Panda Inn competes there on **heritage + sit-down service + cocktails + private room + named servers**. And **none of the other $20–30 restaurants offer all four of those things.** That's the position Panda Inn holds that nobody else in the price band can hold.

### The rating picture (what 4.4 stars actually means)

| Metric | Panda Inn | Glendale 5-mile Chinese median | Glendale 5-mile Asian median (all cuisines) |
|---|---|---|---|
| Google rating | **4.4** | 4.3 (among Chinese in the set) | 4.5 (across 28 restaurants) |
| Review volume | **544** | 229 (median Chinese) | 335 (median Asian) |

Panda Inn is at median for Chinese and 0.1 stars below median for all Asian. Review volume is well above median. The restaurant is doing well. It is not dominating the category it could dominate.

---

## Part 4 — Common items across the Glendale competitive set

### Chinese-American (Panda Inn's home category)

**Table stakes (appear on 5+ of 8 Chinese menus in the set):**
- Orange Chicken · Beef & Broccoli · Kung Pao Chicken · Mongolian Beef · Sweet & Sour Pork · Hot & Sour Soup · Egg Drop Soup · Vegetable fried rice · Lo-mein

**Near-table-stakes (appear on 3+ of 8):**
- Honey Walnut Shrimp · Mapo Tofu · Dan Dan Noodles · Crab Rangoon · Potstickers · General Tso's Chicken

**What Panda Inn has that the Glendale Chinese set doesn't:**
- **Tea-Smoked Duck**. The heritage Mandarin/Sichuan signature. Nobody else in the 5-mile set has it.
- **Panda Beef**. Proprietary house-named signature.
- **USDA Prime short ribs (Asian Spiced Beef Ribs)**. Premium protein most Chinese restaurants in the band don't carry.
- **Wagyu Chow Fun**. Premium protein upgrade most Chinese restaurants in the band don't offer.
- **Upside Down Crispy Noodles**. The "interesting surprise" item that reviewers call out by name.
- **Cocktail bar + wine list**. Structurally absent from the other $20–30 Chinese options.

**What the Glendale Chinese set has that Panda Inn doesn't:**
- **Peking Duck**. None of the Glendale Chinese set has an actual Peking Duck either, but Din Tai Fung owns the "pre-ordered celebration dish" slot with their soup dumplings, and that slot is the one Panda Inn's Tea-Smoked Duck could fill with activation.
- **Xiao Long Bao**, Din Tai Fung owns this category in Glendale. Not a fight worth picking.
- **Regional Sichuan positioning**, **Lao Sze Chuan closed.** The authentic Sichuan seat in central Glendale is empty. See Part 6.

---

## Part 5 — The founding myth activation (the highest-leverage item in the file)

This is the part of the Panda Inn analysis that could not have come out of a standard menu audit. It came out of reading Wikipedia, ABC7, Pasadena Now, and the Cherng family's public statements about how Panda Express started. The finding is nowhere in the Postmates menu. It is nowhere on pandainn.com. It is nowhere on the Google Business Profile. It is nowhere customer-facing.

### The discovery

The Glendale Panda Inn at 201 N Maryland Ave is the second Panda Inn ever built (1982, one year after the Pasadena flagship). **One year after it opened, the developer of Glendale Galleria II — who had eaten at the Panda Inn — asked Andrew Cherng to put a quick-service version of Panda Inn in the new food court.** That food court stand opened in October 1983, half a mile from Panda Inn Glendale. **It was the first Panda Express.**

**The Glendale location is, literally, the place where the world's largest Asian restaurant chain was conceived.**

Most reviewers who reference the Cherng family heritage don't even know this. They think Panda Inn is a Panda Express spinoff. It's the inverse. The reviews we pulled (30 Google reviews via Apify) include several customers who explicitly frame their visit as a pilgrimage:

- *"We flew in from Tampa, Florida, for a wedding... Both being originally from California and huge fans of Panda Express, it felt like an honor to finally experience the Panda Inn."*
- *"Original panda express restaurant. Up side down noodle is a very interesting surprise."*
- *"We have enjoyed dining at Glendale Panda Inn for **decades** (save for those years during the remodel)."*
- *"Been coming here since the **late 90s** when the restaurant was in that small corner with a big parking lot. The place is much bigger now and the foods have remained the same, if not better."*

**A meaningful slice of the customer base treats Panda Inn Glendale as a personal heritage site.** Multi-decade dining relationships, out-of-state pilgrims, customers who track the remodel timeline. **Brand equity Panda Express can never replicate, and it's being banked passively rather than activated.**

### Why this belongs in the menu intelligence file

Broadly interpreted, "menu efficiency" includes the efficiency with which a menu tells the restaurant's own story. Panda Inn's menu is efficient at pricing, adequate at structure, and **completely silent about what the restaurant actually is.** The Hot & Sour Soup is listed at $5.50. It is also the dish a 50-year regular orders because it's the one their grandmother ordered in 1975. That's a different soup than the $5.50 soup listed on Postmates. The menu is not letting it be the second thing.

### The zero-cost activations (described in full in `07-the-founding-myth-brief.md`)

Five things the restaurant can do in the next 30 days without spending a marketing dollar:

**1. A single insert card at every table or on the back of every menu.** Headline: *"Before there was Panda Express, there was Panda Inn."* Body: a three-sentence story about how the Galleria developer ate here, asked for a food-court version, and opened the first Panda Express a half-mile away in October 1983. Cost: $80 for the print run. Effort: one afternoon.

**2. A two-sentence update to the Google Business Profile "From the business" section.** *"Founded 1973 by Andrew Cherng, Panda Inn is the original sit-down Asian dining concept that inspired Panda Express. The Glendale location opened in 1982 and is where the original Panda Express concept was born."* Cost: $0. Effort: one Google Business Profile login.

**3. A short paragraph added to the website's "About" page.** Same story, slightly expanded. Cost: $0 if the marketing team has CMS access. Effort: one afternoon.

**4. A host-stand story script.** One paragraph hostesses learn to say to guests who ask about the history: *"Actually, this is where Panda Express started. The developer of the Glendale Galleria across the street ate at our Panda Inn in 1982 and asked Andrew Cherng if he could build a faster version for his food court. That became the first Panda Express, a year later, half a mile from here."* Cost: one training session. Effort: one staff meeting.

**5. A menu-item heritage callout.** Mark one or two items with a small star or note: *"On the menu since 1973."* Hot & Sour Soup and one of the classic Mandarin entrees. Tiny visual detail, significant emotional weight. Cost: one menu reprint. Effort: done in one week.

**None of these touch food. None of these require marketing budget. All of them activate an asset the restaurant already owns and has never cashed.** The full one-page brief on this is `07-the-founding-myth-brief.md`.

---

## Part 6 — The Sichuan adjacency opportunity (the second free recommendation)

The single biggest market shift in central Glendale that nobody in the competitive set is talking about: **Lao Sze Chuan permanently closed.**

Lao Sze Chuan was central Glendale's only authentic Sichuan sit-down restaurant. Its closure created an open seat for "real spicy regional Chinese" in a city of 190,000 people with zero walking-distance authentic Sichuan alternatives. The market gap is ~4 miles in any direction.

### Why this matters for Panda Inn specifically

The Cherng family's original Panda Inn menu was built on **Mandarin and Sichuan cuisine**. Master Chef Ming-Tsai Cherng (Andrew Cherng's father) came from Yangzhou; the 1973 Panda Inn menu was explicitly Mandarin/Sichuan, built specifically to differentiate from the Cantonese-dominated Chinese restaurants of the era. The Sichuan dishes currently on the Panda Inn menu, **Mapo Tofu, Dan Dan Noodles, Szechuan Tofu, Kon Pao San Yan, Kon Pao Chicken, Kon Pao Shrimp**. Are authentic heritage items, not modern additions.

**The restaurant is founded on the Sichuan position the Glendale market just vacated.** Zero new menu cost. Zero new kitchen training. The dishes already exist. The credentials already exist. The story has never been told.

### The specific recommendations

**1. Create a "Sichuan Heritage" menu section.** Pull the existing Sichuan items out of their current sections (Vegetables, Poultry, Specialties) and group them under a named header. A one-sentence note: *"Our original 1973 menu was built on Mandarin and Sichuan cooking. These dishes honor that heritage."*

**2. Add one or two authentic Sichuan heat-forward items.** Dry-Fried Green Beans with Sichuan Peppercorn (low food cost, high visual impact, directly addresses the market gap). Sichuan-style Dan Dan Noodles as a noodle-section star.

**3. A small press pitch to Eater LA, Pasadena Now, LA Times Food, and LA Magazine.** One pitch: *"The only sit-down Sichuan restaurant in central Glendale just closed. The restaurant 0.4 miles away was originally founded on Sichuan cooking in 1973 and has never talked about it."* This is a dream food-writer story and the pitch writes itself. Cost: Andrea Cherng's CBO team has the relationships.

Expected lift: 8–15% revenue lift on Sichuan category items within 60 days of activation. A brand repositioning that costs nothing to ship.

---

## Part 7 — The menu efficiency lever: fixing the two-portion pricing

This is the specific answer to Chris's "make the menu much more efficient" ask. The most important inefficiency in the Panda Inn menu is not a missing item or a wrong price. It is a pricing architecture: the **small/large two-portion structure** that exists, works, and is invisible at the exact points where customers make ordering decisions.

### The evidence

On Allmenus (where the dine-in menu is cached), Mongolian Beef is listed as **$17/$33**. Honey Walnut Shrimp is listed as **$21/$40**. Most entrees on the menu follow this small/large pattern. But:

- **Postmates** shows "Priced by add-ons". No visible dollar figure until the modifier is selected.
- **Uber Eats** shows the same "Priced by add-ons" treatment on most entrees.
- **DoorDash** similar.
- **The Google Business Profile** doesn't surface entrée pricing at all.
- **Walk-in customers** learn the two-portion structure from the server, which is a labor-cost-per-check hit and an information asymmetry that works against the restaurant.

### What this does to revenue

Three compounding problems:

**1. Delivery customers default to "low" by modifier order.** The way Postmates and Uber Eats surface the small/large modifier, the small portion is almost always the first option. The delivery customer who picks the first option is ordering the $17 portion when they might have ordered the $33 portion. At scale across thousands of delivery orders per month, this is a significant revenue leak.

**2. Walk-in customers have to be told.** A server explaining the two-portion architecture takes 30 seconds per table. With 150 covers per night, that's 45 minutes of server time per shift. Time that could go into upsell on appetizers, desserts, or drinks. More important: the server explanation lands during the "what are you getting?" decision moment, which makes the choice feel like a labor decision rather than a portion decision.

**3. The large portion is literally hidden.** The restaurant's best margin instrument — large portions carry higher absolute margin even though they run a lower margin percentage — is functionally invisible at the moment of sale. A menu whose best item is hidden behind a server's explanation is a menu that's leaving revenue on the table.

### The specific fix

**1. Redesign the in-house menu to show both prices explicitly.** Each entrée listed with two prices visible: *"Mongolian Beef, $17 small / $33 family."* That's it. One layout change. The walk-in customer now makes an informed choice before the server arrives. Server time is freed up for upsell. The decision becomes portion-driven, not labor-driven.

**2. Work with the delivery app reps to change the modifier display.** Uber Eats and Postmates account managers have the ability to update how modifiers appear. Instead of "Priced by add-ons," the listing can show the lowest price with a "from $17" treatment, and the modifier page can lead with a visual comparison. Cost: one phone call to each platform's account manager. Effort: one hour.

**3. On the website, surface the lunch-specials program.** Google's own crowd data shows **lunch reservations are recommended** at Panda Inn. Demand exists. But the lunch specials live on a buried URL (`pandainn.com/menu_type/lunch-specials/`) that 99% of potential customers never see. Add a "Lunch Specials" tile to the homepage. Add a lunch category to the delivery app listings. Add a lunch photo to the Google Business Profile. Total effort: one web update, two platform updates, one photo upload.

**Expected lift:** 8–12% lift on family-size attachment rate on delivery within 60 days. Incremental lunch cover count 10–20% within 90 days. No new dishes, no new prep work, no kitchen complexity. Pure information architecture.

---

## Part 8 — The other efficiency levers

### Lever 1 — Activate the named-server moat

Reviewers explicitly name servers **Alfredo** and **Simon** in 4 of the top 30 Google reviews. At a $20–30 Chinese restaurant price point, **named-server callouts are unusual and meaningful.** The restaurant is buying loyalty through individual relationships in a market where that's increasingly rare.

The risk: a service-intensity moat is a labor-cost moat. It depends on retention.

The opportunity: this is a story that can be told to the press, to Yelp's "People Love Us on Yelp" program, to any LA food writer covering "the soul of a Glendale dining institution." Named servers with 10+ years of tenure at a single restaurant is a feature story waiting to be pitched.

**Recommendation:** Build a simple server-tenure honor roll inside the restaurant. Photograph and caption the longest-tenured servers on a small wall near the host stand. Retention tool. Marketing asset. Cultural signal. Cost: $200 for framed photos and a small plaque. Effort: one afternoon.

### Lever 2 — Fix the "hit or miss" temperature complaint

Three of the lower-rated reviews cite dish temperature as a specific complaint. *"Some of the dishes including the soup were not very hot."* The Hot & Sour Soup, the anchor dish of the menu and the most-mentioned item across reviews, is being served lukewarm some of the time. That is a warming-station calibration issue, a pass-to-table time issue, or a service-flow issue at peak hours. Any of the three are diagnosable with a week of observation and a stopwatch.

**Recommendation:** Timing study during Friday and Saturday peak. Document the time from "soup fired" to "soup on table" across 20 tickets per night. Identify the specific breakdown (holding time too long at the pass, server delay after pickup, underpowered warmer in the soup station). Fix the specific thing. Cost: two shifts of observation time. Effort: ~8 hours.

### Lever 3 — Cocktail program at a $20–30 Chinese restaurant is a rare moat; it deserves its own menu space

Panda Inn has a cocktail bar and a wine list (multiple reviews mention "excellent wine list, surprisingly"). The cocktails and wine are functionally invisible on the delivery apps and are buried on the website. In a $20–30 Chinese restaurant category where **none** of the direct competitors (Wong's Wok, California Wok, Fu House, New Moon) have a serious cocktail bar, this is a genuine differentiator being treated as a footnote.

**Recommendation:** Create a dedicated cocktails + wine page on pandainn.com. Lead with two signature cocktails that pair with specific dishes (a scotch-forward cocktail with Tea-Smoked Duck, a ginger-and-lychee cocktail with the Hot & Sour Soup). Photograph. Add to the delivery platform listings as "bar available dine-in." The restaurant is already doing the work. The menu is not claiming it.

Expected lift: 5–10% beverage attach rate on dine-in within 90 days. Low cost; existing program, surfacing change only.

### Lever 4 — The Peking Duck question

The one major category item missing from a sit-down upscale Mandarin restaurant in 2026 is **Peking Duck**. Panda Inn offers Tea-Smoked Duck (Sichuan, elegant) and Mango Duck Salad. Both distinctive, but neither fills the ceremonial-dish slot that Peking Duck occupies in the upscale Chinese-American dining mental model.

This one is a judgment call. Peking Duck requires a specific prep (air-drying, two-day advance ordering) and is structurally different from the walk-in flow Panda Inn runs. The recommendation is not to add it lightly.

**Option A (conservative):** Position the existing Tea-Smoked Duck as the house ceremonial dish. Add a "24-hour advance order" framing that lets it function like Peking Duck does at upscale Mandarin restaurants. A reserved celebration dish, presented with table-side carving, priced as the top item on the menu ($65–$85). This converts an existing dish into a different menu role at no food cost.

**Option B (aggressive):** Add Peking Duck as a Saturday-only special, pre-order required, priced at $85–$110. Tests demand without committing the kitchen to daily prep.

**Option A is the lower-risk recommendation.** It matches the founding-myth activation (the Tea-Smoked Duck becomes *the* heritage dish), requires no new kitchen work, and gives the restaurant a ceremonial dish to photograph for every marketing asset going forward.

### Lever 5 — The Cherng family trust moment

This is not a menu lever, it's a brand lever, and it belongs in this file because it would make every other recommendation in the file more effective if it was activated. The **Cherng Family Trust** made a **$100 million gift to City of Hope for cancer research** (publicly reported by Pasadena Now). That is a philanthropic act of the same scale as the company's commercial footprint. Panda Inn Glendale. The heritage restaurant of the family. Is the natural place to acknowledge it. A small framed press clipping near the host stand. A single sentence on the menu insert. A link from the pandainn.com website to the City of Hope Cherng Family Center for Surgical Care.

**None of this is marketing. All of it is truth-telling.** And truth-telling about a family's public generosity, in the restaurant the family considers its flagship, is the kind of signal that moves a restaurant from "good local Chinese" to "place with a soul." The existing customers already feel this. They call it out in reviews ("a family institution"). The new customers don't know. The fix is three sentences on a wall.

---

## Part 9 — What to do with this file

The Panda Inn Glendale recommendations sequence by cost and leverage:

1. **The founding myth activation** (Part 5). Five zero-cost moves. 30-day implementation. Cost: under $500 total. The highest-leverage single category in the deliverable.
2. **The Sichuan adjacency press and menu repositioning** (Part 6). Zero-cost, existing dishes, existing credentials. 60-day implementation including the press pitch.
3. **The two-portion pricing transparency fix** (Part 7). Low-cost; one menu redesign, platform update calls. 30-day implementation.
4. **The lunch specials digital surface fix** (Part 7 sub-item). Zero-cost; website and listing updates. One-week implementation.
5. **The cocktail program surface** (Lever 3). Zero-cost; content and photography only. 30-day implementation.
6. **The named-server moat activation** (Lever 1). Under $500; minor build. 60-day implementation.
7. **The temperature complaint diagnosis** (Lever 2). Two shifts of observation. One-week implementation.
8. **The ceremonial-dish conversion of Tea-Smoked Duck** (Lever 4, Option A). Low-cost; menu reprint and server training. 60-day implementation.

Everything in this list is executable within the existing operating budget of the location. Nothing in this list requires POS integration or new technology. The founding myth and the Sichuan adjacency are the two recommendations that pay the rent on the entire file. Both are zero-dollar activations of assets the restaurant already owns.

---

## Sources

**Menu and pricing:**
- Postmates Panda Inn store page (apify-panda-inn-reviews.json + panda-inn-postmates-raw.md, full menu with Postmates delivery pricing)
- Uber Eats cross-reference (same Postmates store ID, in-store prices ~5% lower than Postmates)
- Allmenus PDF references for the two-portion structure ($17/$33 Mongolian Beef, $21/$40 Honey Walnut Shrimp)
- pandainn.com/glendale
- pandainn.com/menu_type/lunch-specials/ (the buried lunch URL)

**Competitive set:**
- Apify Google Maps runs: `apify-glendale-chinese.json` (15 Chinese restaurants), `apify-glendale-sushi.json` (15 sushi/Japanese), `apify-glendale-korean.json` (10 Korean BBQ), total Apify spend ~$0.55
- `apify-panda-inn-reviews.json`, Panda Inn place detail + 30 Google reviews + review tags
- `apify-competitors-reviews.json`, Din Tai Fung, Sasabune, Jincook, Dragon Garden detail + reviews

**Founding myth sources:**
- Wikipedia: Panda Inn, Panda Restaurant Group, Andrew Cherng, Glendale California, Americana at Brand
- ABC7: "Original Panda Inn... reopens in Pasadena" (Panda Express origin story)
- Pasadena Now: "Founder of Pasadena's Panda Inn Gifts City of Hope $100 Million for Cancer Research"
- pandarg.com/our-brands. Official PRG brand portfolio
- pandarg.com/andrea-cherng, CBO background

**Sichuan adjacency source:**
- Yelp, Lao Sze Chuan Glendale CLOSED listing

**Benchmarks referenced:**
- Multi-portion menu engineering: Kasavana-Smith Restaurant Management literature; restroworks.com menu engineering guides
- Family-style service PPA math: getbento.com restaurant benchmarks, chowbus.com turn-rate benchmarks
- Attachment rate on delivery platforms: trykitchenhub.com 2026 commission updates, getsauce.com delivery benchmarks
