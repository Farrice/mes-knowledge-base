# Yakiya — Menu Capture (Pasadena Location, 91107)

**Sources:**
- Apify rag-web-browser fetch of `yakiya-us.com/menu` (returned title only — SPA blocks scraping)
- Apify rag-web-browser fetch of `yakiya.res-menu.net/menu` (community-maintained mirror with full beverage list)
- Adam Parkzer eyewitness review (parkzer.com/2024/07/17/yakiya-pasadena-california) — full 15-course chef's tasting receipt
- Yelp / OpenTable / Tripadvisor extracts via WebSearch
- Trade press: Restaurant Hospitality, Nation's Restaurant News (YakiYan / Panda Restaurant Group)

> **Note on completeness:** Yakiya's official site is a JavaScript SPA hardened against scraping (Akamai protection on OpenTable, anti-bot on yakiya-us.com). The food menu is not directly extractable via headless browser. The detailed menu below is reconstructed from a verified eyewitness 15-course tasting receipt + multiple Yelp/Tripadvisor reviews + the trade press menu description. Beverage prices are direct from the community-maintained res-menu.net mirror.

---

## Format & Structure

Yakiya is a chef's pre-fixe (tasting menu) yakiniku/shabu concept. There is no a la carte ordering of the main dining experience; the chef chooses every dish.

Pasadena allows the tabletop grill to be swapped for a shabu-shabu hot pot. Hacienda Heights is yakiniku-only.

**Three core menus** (confirmed across multiple sources):

| Menu | Format | Price/guest | Course count |
|---|---|---|---|
| **Yakiniku Tasting** (signature) | 15-course chef's pre-fixe, tableside grill | **$128** | 15 |
| **Yakiniku Tasting** (lighter) | 10-course pre-fixe | **$78** | 10 |
| **Shabu Tasting** (Pasadena exclusive) | Pre-fixe hot pot format | **$78** | ~10 |
| Kids menu (under 12) | Simplified | $28 | — |

**Promotional**: $98/pp Mon–Thu (limited-time discount on $128 menu), per Yakiya messaging cited in 2026 marketing.

**Service window**: 4:30 PM – 10:00 PM Mon–Sat; 11:30 AM – 10:00 PM Sun. Each seating is **90 minutes** (per restaurant policy).

---

## $128 Signature 15-Course Tasting — Reconstructed Lineup

This is the dish-by-dish lineup reported by Parkzer's eyewitness review (party of 4, July 2024) cross-referenced with multiple Yelp reviews. Order/exact composition rotates by season per "We change menu and price by season" (Pimlada I., Yelp).

| # | Course | Dish | Notes |
|---|---|---|---|
| 1 | Welcome | Warm hand towel + yuzu refresher | Service ritual |
| 2 | Appetizer (raw) | Raw ground A5 Miyazaki wagyu, ponzu jelly, truffle, arimo sancho pepper | Signature opener |
| 3 | Appetizer (raw) | USDA Prime ribeye tataki, ponzu, garlic, kaiware | Carpaccio-style, raw |
| 4 | Sashimi | Bluefin tuna + hamachi, Kaluga caviar, scallion oil, wasabi | Premium fish |
| 5 | Egg | Chawanmushi, Dungeness crab, ikura, shiitake | Seasonal egg custard |
| 6 | Vegetable | Local farmer's market crudité, multigrain rice cracker, house-made red miso | Raw vegetables |
| 7 | Soup | Wagyu meatballs + radish, oxtail broth | Hot, brothy |
| 8 | Grill #1 | American wagyu beef tongue, scallion kosho | First grill course |
| 9 | Grill #2 | USDA Prime ribeye + USDA Prime outside skirt + A5 Miyazaki chuck, wasabi sauce | Trio of cuts |
| 10 | Palate cleanser | Heirloom tomato, shishito pepper, truffle mushroom | Between mains |
| 11 | Grill #3 | American wagyu short rib + USDA Prime filet mignon chateaubriand, bone marrow, garlic miso, kimchi, nori | Star course — bone marrow signature |
| 12 | Grill #4 | A5 Miyazaki wagyu strip loin, poached egg, Maldon sea salt | Premium finale |
| 13 | Rice | Bone Marrow Bibimbap (hot stone bowl, two roasted marrow cuts, rice, seaweed, kimchi) | Signature dish — most-mentioned in reviews |
| 14 | Dessert #1 | Lemon sorbet, basil oil | Best-rated dish in Parkzer review |
| 15 | Dessert #2 | Matcha balls (interactive — diner cracks open) | Theatrical close |

**Other dishes mentioned across reviews** (likely on rotation or as substitutions):
- Wagyu sukiyaki (closing course in some 18-dish iterations)
- Wagyu garlic fried rice (alternate to bibimbap)
- Smoked raw beef (Yelp Tammy T.)
- Wagyu carpaccio + tartare opening pair (Tina Y.)
- Snow crab chawanmushi variation
- USDA Prime filet mignon chateaubriand (a la carte add-on suggested by reviewers)

---

## Menu Categories Summary

| Category | Items (estimate) | Price band | Notes |
|---|---|---|---|
| **Pre-fixe tasting** | 1–3 menus (Yakiniku $128, Yakiniku $78, Shabu $78) | $78–$128/pp | Core revenue driver |
| **A la carte** | Listed on site but not the focus; likely add-on cuts (bone marrow, A5 ribeye+egg) | $20–$60/item | Reviewers say "add the bone marrow and A5 ribeye to your course" |
| **Happy Hour** | Mentioned on site, no detail captured | unknown | |
| **Cocktails (signature)** | 7 named ($13–$15) | $13–$15 | Below $20+ that some reviewers complained about |
| **Hibiki Hi-Ball** | Single highball | $15 | |
| **Mocktails** | Available, can convert any cocktail | $6 | |
| **Sake (categorized: Earthy/Crisp/Subtle/Specialty)** | ~12+ bottles | $10–$960 | Daiginjo range very deep ($130–$960) |
| **Japanese Whisky** | 6 pours | $22–$250 | Hibiki $45, Yamazaki $80, Komagatake $250 |
| **Wine** | ~12 bottles (white/red/sparkling) | $12–$388 | Insignia $388, Caymus $185 |
| **Draft beer** | 4 Coedo + 1 Echigo | $8–$9 | All Japanese craft |
| **Non-alcoholic / juice** | Sodas, fresh-squeezed juices, lemonades | $3–$8 | Includes Japanese lemonade |

---

## Beverage Pricing — Verified (res-menu.net mirror, current as of 2026 fetch)

### Cocktails (all $13 unless noted)
- Red Crowned Crane / The Pagoda / Green Kimono / Bloody Ox / Fog On Mount Fuji / Bullet Train — **$13**
- Hibiki Hi-Ball — **$15**
- Mocktail conversion — **$6**

### Sake (selected)
- Akitabare Koshiki Junzukuri **$13**
- Miyasaka Yawaraka Junmai **$10**
- Sohomare Tokubetsu Kimoto **$14**
- Dewazakura Oka **$13** / Izumi Judan **$14**
- Kubota Ginjo **$14**
- Kokuryu Junmai Ginjo **$16**
- Hoyo Kura No Hana **$18**
- Masumi Nanago **$24**
- **Dassai Junmai Daiginjo $130**
- **Dewazakura Yukimanman $222**
- **Dassai Beyond Junmai Daiginjo $960** ← portrait cellar item

### Whisky
- Ichiro's Malt & Grain $22 / Chichibu Floor Malted $34 / Hibiki $45 / Hakushu $60 / Yamazaki $80 / Komagatake $250

### Wine highlights
- Hobo Zinfandel $12, Folk Machine Pinot Noir $13, Brea Cab Sauv $16, Genuine Risk Red Blend $18
- **Caymus Cabernet Sauvignon $185, Joseph Phelps Insignia $388**

### Draft beer
- Coedo Shiro Hefeweizen / Shikkoku Black Lager — **$9**
- Coedo Kyara IPL / Beniaka Sweet Potato Ale — **$8**
- Koshihikari Echigo Pilsner — **$9**

---

## Sample Receipt — Real Diner Data Point (Parkzer, July 2024)

| Item | Subtotal |
|---|---|
| Chef's Tasting Menu × 4 | $512.00 |
| Soft Pagoda mocktail | $13.00 |
| Cherry Blossom mocktail | $13.00 |
| S.Pellegrino sparkling | $8.00 |
| S.Pellegrino still | $8.00 |
| Gratuity | $90.00 |
| Sales tax | $56.79 |
| **Total for 4** | **$700.79** |

**Per-cover average (PPA): $175.20** — including tax & tip, beverage attach was minimal ($10.50/pp).

---

## Menu Engineering Observations (Visible from Structure Alone)

1. **Single-format dependency.** Almost all revenue rides on the $128 (or $78) tasting menu. There's no a la carte path for casual diners, no light dinner option, no value lunch (Hacienda Heights has Sat/Sun lunch service but Pasadena doesn't open until 4:30 PM Mon–Sat).

2. **Beverage attach rate is unclear and likely under-monetized.** Most cocktails priced at $13 — undermarket for an upscale wagyu concept. The cellar has $960 sake and $388 wine bottles, but no mid-tier $40–$80 anchor bottles to bridge the gap. This is a classic price-ladder gap.

3. **The "switch grill for shabu" feature is a Pasadena differentiator** but isn't visibly priced or marketed at premium. Both formats are $78 — leaves Yakiya competing with $20–$30 shabu houses on form factor without a clear positioning premium.

4. **The 90-minute table cap** at $128/pp = ~$85/hr/cover. With ~50 covers per night × 90 min, that's a hard ceiling on revenue. No 2nd seating premium, no chef's counter premium, no late-night premium.

5. **Kids meal at $28** suggests they take families — unusual signal for a $128/pp tasting concept. May indicate softer dayparts they're trying to fill.

---

## Cross-reference: Hacienda Heights vs Pasadena

| | Hacienda Heights (original) | Pasadena |
|---|---|---|
| Address | 17188 Colima Rd, Suite C, 91745 | 3455 E Foothill Blvd, 91107 |
| Opened | First location | Second (newer) |
| Format | Yakiniku only | Yakiniku OR Shabu (grill switches out) |
| Lunch service | Sat/Sun 11:30 AM–2:30 PM | None — dinner only Mon–Sat |
| Sunday open | 11:30 AM | 11:30 AM |
| Yelp reviews | 1,237 | 265 |
| Yelp photos | 11,351 | 2,274 |
| Tasting menu | $78 (yakiniku set) | $78 + $128 (multiple tiers) |
| Demographic | Asian-suburban (San Gabriel Valley) | Mixed local Pasadena/Hastings Ranch |

The Pasadena location has only ~21% of the Hacienda Heights review volume despite being a more affluent market — strong signal that Pasadena hasn't reached steady-state demand yet.
