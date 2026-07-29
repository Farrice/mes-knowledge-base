# Competitive Pricing Dashboards
### Three restaurants, three 5-mile competitor sets, visualized

**Purpose:** A visual, tabular read of how each restaurant sits against its relevant competitive set. Built to be instantly legible and easy to convert to Gamma or Canva slides for a meeting deck.

**Reading note:** Each dashboard shows the restaurant's price position plotted against rating and review volume. In markdown these are ASCII scatter plots and side-by-side tables. The underlying data is the same as the three menu intelligence files. This dashboard is the visual distillation.

---

## Dashboard 1 — Wasabi at CityWalk vs Japanese 5-mile set

### The position scatter (price tier × rating)

```
                            RATING (Google stars)
5.0 │  ⬤ Tetsuya(5.0)                                             ▲
    │                                                          omakase
4.9 │                          ⬤ REDWHITE Ramen                    │
    │                                                              │
4.8 │                          ⬤ Daichan(soul)   ⬤ UMIAI(handroll) │
    │                          ⬤ Maki-Noho                         │
4.7 │                                             ⬤ KITA           │
    │                                             ⬤ Ramen-Izakaya  │
4.6 │       ⬤ Asanebo(omakase)  ⬤ JINYA           ⬤ Yume           │
    │                           ⬤ Sunny's                          │
4.5 │                ⬤ SUGARFISH  ⬤ Katsu-ya(Studio City)           │
    │                ⬤ Teru  ⬤ SHIKI  ⬤ Iroha  ⬤ KIWAMI            │
4.4 │                ⬤ Leona's  ⬤ The Sushi House  ⬤ Maki Shabu    │
    │                ⬤ Studio Sushi(1.6mi)                         │
4.3 │   ⬤ Sushi Dan                                                │
4.2 │   ⬤ KazuNori                                                 │
    │                                                              │
4.1 │   ⬤ WASABI at CityWalk ◀━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ SUBJECT
    │                                                              │
4.0 │   ⬤ SushiStop   ⬤ Tamashii Ramen                             │
    │                                                              ▼
    │                                                          casual
    └──────────────────────────────────────────────────────────────
        $         $$         $$$        $$$$       $100+
        (casual)  (mid)      (premium)  (fine)     (omakase)
                        PRICE TIER
```

### The numbers (sorted by rating)

| Rank | Restaurant | Tier | Rating | Reviews | Distance |
|---:|---|---|---:|---:|---:|
| 1 | **Sushi Bar Tetsuya** | omakase | 5.0 | 75 | 3.8 mi |
| 2 | Daichan (Japanese soul food) | $20–30 | 4.8 | 398 | 3.7 mi |
| 3 | REDWHITE BONELESS RAMEN | $$ | 4.9 | 1,012 | 4.0 mi |
| 4 | UMIAI Hand Roll & Sake | — | 4.8 | 247 | 3.0 mi |
| 5 | Maki-Noho | $20–30 | 4.9 | 122 | 2.3 mi |
| 6 | KITA Ramen and Sushi Bar | $20–30 | 4.7 | 73 | 2.8 mi |
| 7 | Ramen Izakaya NoHo | $$ | 4.7 | 316 | 2.5 mi |
| 8 | **Asanebo** | $100+ | 4.6 | 363 | 4.0 mi |
| 9 | JINYA Ramen Bar | $20–30 | 4.6 | **2,456** | 3.9 mi |
| 10 | Yume Sushi Bar | $50–60 | 4.6 | 210 | 4.5 mi |
| 11 | **Sushi Katsu-ya (Studio City)** | $$$ | 4.5 | 604 | 4.2 mi |
| 12 | **SUGARFISH by sushi nozawa** | $30–50 | 4.5 | 908 | 4.4 mi |
| 13 | Teru Sushi | $$$ | 4.5 | 466 | 4.1 mi |
| 14 | SHIKI SUSHI | $$ | 4.5 | 683 | 4.6 mi |
| 15 | Iroha Sushi of Tokyo | $$$ | 4.5 | 756 | 4.5 mi |
| 16 | KIWAMI by Katsu-ya | $30–40 | 4.5 | 357 | 4.1 mi |
| 17 | Studio Sushi | $30–50 | 4.4 | 206 | 1.6 mi (closest) |
| 18 | Leona's Sushi House | $50–100 | 4.4 | 136 | 4.2 mi |
| 19 | The Sushi House | $$ | 4.4 | 432 | 4.0 mi |
| 20 | Sushi Dan | $20–30 | 4.3 | 665 | 4.0 mi |
| 21 | KazuNori (Hand Roll Bar) | $20–30 | 4.2 | 149 | 3.7 mi |
| **22** | **⬤ WASABI at CityWalk** | **$20–30** | **4.1** | **395** | **(subject)** |
| 23 | SushiStop Studio City | $20–30 | 4.0 | 661 | 4.1 mi |
| 24 | Tamashii Ramen House | $10–20 | 4.0 | 515 | 2.9 mi |

### Headline stats

- **Wasabi rating: 4.1 stars.** Competitive set median: **4.50 stars**. Gap: **−0.4 stars**.
- **Wasabi review volume: 395 Google / 1,729 Yelp.** Median of set: **~241 Google** (Wasabi is above median on volume, below on rating).
- **Rating rank: 22 out of 24** in the 5-mile Japanese competitive set.
- **Price position: $20–30 ($20.33 average main, $19.90 average signature roll).** The Studio City premium tier runs $28–$40 mains and $22–$28 signature rolls. Wasabi is priced at the **casual-mid band** and rated **0.4 stars below the median**.

### The sentence this dashboard exists to deliver

Wasabi's problem is not that it's competing against 24 sushi restaurants. Its problem is that it's the **only sushi restaurant inside CityWalk**. A category monopolist inside a 9-million-annual-visitor district. But its review reputation is being set by the 14% of guests who hit the service-failure window and compare it to the Ventura Blvd alternatives four miles away. The gap closes when throughput is fixed, not when new items are added.

*Source: Apify Google Maps scraper runs 2026-04-06, files `wasabi-apify-studio-city.json`, `wasabi-apify-noho.json`, `wasabi-apify-citywalk-internal.json`, `wasabi-apify-universal-city.json`. Menu pricing from wasabi-citywalk.com/wasabi_menu.pdf.*

---

## Dashboard 2 — Yakiya vs Pasadena Japanese 5-mile set

### The position scatter (price tier × rating)

```
                            RATING (Google stars)
5.0 │                                                             ▲
    │                                                          premium
4.9 │          ⬤ Sushi Karen(14-seat, $65-96)                      │
    │          ⬤ Wagyu Master Shabu                                │
4.8 │                                                              │
    │                                                              │
4.7 │          ⬤ Osawa(922)   ⬤ Mills Alley(izakaya)               │
    │          ⬤ Kyushu       ⬤ Sushigah                           │
4.6 │          ⬤ Oseyo Shabu  ⬤ Oji Sushi   ⬤ KAVIAR(386 rev)      │
    │          ⬤ Bay Poke                                          │
4.5 │          ⬤ Go Go Sushi  ⬤ MAMA M  ⬤ Sushi Roku(674)          │
    │          ⬤ ⬤ YAKIYA(88 rev) ◀━━━━━━━━━━━━━━━━━━━━━━━━━ SUBJECT
4.4 │          ⬤ Kabuki(1234)  ⬤ Gyu-Kaku  ⬤ Kaiba                 │
    │          ⬤ ICHIMA                                            │
4.3 │          ⬤ Shogun   ⬤ SushiStop                              │
4.2 │          ⬤ Mako Bowl                                         │
    │                                                              │
4.0 │                                                              ▼
    │                                                          casual
    └──────────────────────────────────────────────────────────────
        $         $$         $$$        $$$$       $100+
        (casual)  (mid)      (premium)  (fine)     (omakase)
                        PRICE TIER
```

### The numbers (premium tier, sorted by review velocity)

| Restaurant | Tier | Rating | Reviews | PPA / top tier |
|---|---|---:|---:|---|
| **Osawa Shabu Shabu & Sushi** | $$ | 4.7 | **922** | à la carte $21–$89 |
| **Sushi Roku Pasadena** | $$$ | 4.5 | **674** | Chef's selection $85/2 |
| **Sushi Enya Pasadena** | — | 4.5 | **504** | **$200/pp omakase** |
| **KAVIAR Pasadena** | $100+ | 4.6 | **386** | **$89 Dine LA / $109 Chef's Omakase** |
| **Wagyu Master Shabu House** | — | **4.9** | 365 | AYCE A5 wagyu tiered |
| **Sushi Karen** | $50–100 | **4.9** | 121 | **$65–$96 omakase** |
| **⬤ YAKIYA Pasadena** | **$100+** | **4.5** | **88** | **$78 / $128 tasting** |

### Headline stats

- **Yakiya review count: 88 Google / 265 Yelp / 49 OpenTable** after nearly 10 years of operation.
- **Premium-set median review count: ~408 Google.** Yakiya has **~22% of the review volume** of the median premium Pasadena Japanese restaurant.
- **Yakiya rating: 4.5 stars.** Premium-set median: 4.65 stars. Gap: **−0.15 stars**.
- **Pasadena omakase/tasting median: ~$98/pp.** Yakiya at $128/pp is in the upper third. But KAVIAR at $109, Sushi Karen at $65–$96, and Mills Alley's izakaya at $38+ all offer equivalent or lower pricing with higher ratings and higher review velocity.
- **Closest premium competitor distance: 3.94 mi** (Sushi Enya). In East Pasadena / Hastings Ranch, Yakiya has a **2.5-mile local monopoly** on premium Japanese. No competitor within that radius.

### The sentence this dashboard exists to deliver

Yakiya is priced at the premium tier, reviewed at the mid tier, and categorized as a Japanese steakhouse by diners searching for omakase. The category problem is more important than the price problem. A $20 cocktail reprice and a category rebrand from "Japanese steakhouse" to "Wagyu Tasting House" would move more revenue than any dish-level menu change.

*Source: Apify Google Maps scraper runs, files `competitors-sushi-pasadena.json` (30 results), `competitors-yakiniku-pasadena.json` (10 results), `competitors-table.json`. Pricing from yakiya.res-menu.net and verified Parkzer.com receipt July 2024.*

---

## Dashboard 3 — Panda Inn Glendale vs Asian 5-mile set

### The position scatter (price tier × rating)

```
                            RATING (Google stars)
5.0 │                                                             ▲
    │                                                          premium
4.9 │                                                              │
    │                                                              │
4.8 │                               ⬤ Iki Toro                     │
4.7 │        ⬤ Jincook(334 rev)     ⬤ UMI by Eden  ⬤ Sasabune      │
    │        ⬤ Cavi Sushi   ⬤ Seabutter                            │
4.6 │        ⬤ Oseyo Shabu  ⬤ bb.q Chicken                         │
    │                                                              │
4.5 │        ⬤ Din Tai Fung(2891!)  ⬤ MOTO  ⬤ Dragon Garden  ⬤ Gam Tu Bop │
    │        ⬤ New Moon   ⬤ Oji Sushi                              │
4.4 │        ⬤ ⬤ PANDA INN Glendale(544 rev) ◀━━━━━━━━━━━━━━ SUBJECT
    │        ⬤ Mitzee   ⬤ Beulah Kitchen   ⬤ Taste of Windsor      │
    │        ⬤ California Wok                                      │
4.3 │        ⬤ Kura Revolving Sushi                                │
4.2 │        ⬤ House of Joy   ⬤ Wong's Wok                         │
    │                                                              │
4.0 │        ⬤ Gen Korean BBQ(1486!)   ⬤ Fuji Buffet(3007!)        │
    │                                                              ▼
    │                                                          casual
    └──────────────────────────────────────────────────────────────
        $         $$         $$$        $$$$       $100+
        (casual)  (mid)      (premium)  (fine)     (omakase)
                        PRICE TIER
```

### The numbers (sorted by review velocity — where the Glendale volume actually is)

| Rank | Restaurant | Cuisine | Price | Rating | Reviews | Distance |
|---:|---|---|---|---:|---:|---:|
| 1 | **Fuji Buffet & Grill** | Buffet | $$ | 4.0 | **3,007** | 1.1 mi |
| 2 | **Din Tai Fung** | Taiwanese/Shanghainese | $$ | 4.5 | **2,891** | 0.7 mi |
| 3 | **Gen Korean BBQ** | KBBQ | $20–30 | 4.0 | **1,486** | 0.4 mi |
| 4 | **Shogun** (Pasadena edge) | Japanese | $$ | 4.3 | 1,480 | (edge) |
| 5 | Kura Revolving Sushi Bar | Conveyor | $20–30 | 4.3 | 734 | 0.7 mi |
| 6 | **⬤ PANDA INN Glendale** | **Heritage Mandarin** | **$20–30** | **4.4** | **544** | **(subject)** |
| 7 | New Moon (Montrose) | Chinese-American | $20–30 | 4.5 | 831 | 4.1 mi |
| 8 | House of Joy (La Crescenta) | Chinese-American | $20–30 | 4.2 | 345 | ~4.5 mi |
| 9 | **Jincook** | Korean comfort | $20–30 | **4.5** | 334 | 0.5 mi |
| 10 | Gam Tu Bop | Asian fusion | $10–20 | 4.5 | 280 | 0.5 mi |
| 11 | MOTO SUSHI Glendale | Mid-tier sushi | $$ | 4.5 | 255 | 1.3 mi |
| 12 | Wong's Wok Chinese Kitchen | Takeout | $ | 4.2 | 229 | 0.9 mi |
| 13 | Sasabune Glendale | High-end omakase | **$100+** | **4.7** | 209 | 0.5 mi |
| 14 | Beulah Kitchen | Korean casual | $$ | 4.4 | 200 | 0.7 mi |
| 15 | Mitzee Cafe | Korean casual | $10–20 | 4.4 | 157 | 1.1 mi |
| 16 | Chinese Fast Food | Quick-serve | $10–20 | 4.0 | 165 | 2.6 mi |
| — | **~~Lao Sze Chuan~~** | **Sichuan (Michelin Guide)** | **$$** | **4.0** | **377** | **CLOSED** |

### Headline stats

- **Panda Inn rating: 4.4 stars.** Chinese-5mi median: ~4.3 stars. All-Asian-5mi median: ~4.5 stars.
- **Panda Inn review volume: 544.** Above median for the Chinese 5-mile set. Below Din Tai Fung (2,891) and Fuji Buffet (3,007) on raw volume but both of those are high-volume category leaders, not direct comparables.
- **Price position: $20–30 ($19.80 vegetable mains, $18 chicken mains, $33 large-portion beef, $30 premium specialties).** This is the most crowded price band in central Glendale and Panda Inn is the only operator in it with heritage + sit-down service + cocktails + private dining + named-server service.
- **Lao Sze Chuan (the one authentic Sichuan competitor within 4 miles) permanently closed.** The Sichuan category is empty. The Cherng family founded on Mandarin and Sichuan. Category is wide open and nobody's running at it.

### The sentence this dashboard exists to deliver

Panda Inn is positioned well and competing under itself. The 544-review / 4.4-star baseline is an underleveraged position, not a contested one. Din Tai Fung owns soup-dumpling occasions. Gen Korean BBQ owns AYCE group occasions. Sasabune owns destination omakase. **Panda Inn owns the heritage celebration-dinner occasion and is not claiming it.** The founding-myth activation and Sichuan repositioning are the two moves that convert the position into the ratings and review velocity the position deserves.

*Source: Apify Google Maps scraper runs 2026-04-06, files `apify-glendale-chinese.json`, `apify-glendale-sushi.json`, `apify-glendale-korean.json`, `apify-panda-inn-reviews.json`, `apify-competitors-reviews.json`. Menu pricing from Postmates and Uber Eats cross-references.*

---

## Cross-portfolio summary

| | **Wasabi at CityWalk** | **Yakiya Pasadena** | **Panda Inn Glendale** |
|---|---|---|---|
| **Rating** | 4.1 (−0.4 vs set median) | 4.5 (−0.15 vs premium set median) | 4.4 (at chinese median, −0.1 all-asian) |
| **Reviews** | 395 Google / 1,729 Yelp | 88 Google / 265 Yelp | 544 Google / 1,500+ Postmates |
| **Price position** | Casual-mid ($20 avg main) | Upper premium ($128/pp) | Mid ($20–30 band, $33 large) |
| **Market gap (reviews) vs category leader in 5-mi set** | 6× below Buca di Beppo | ~10× below Osawa | 5× below Din Tai Fung |
| **Category monopoly held** | Only sushi in CityWalk | Only premium Japanese in 2.5 mi | Only heritage Chinese-American sit-down in ~1 mi |
| **Category monopoly being pressed?** | No (discoverability gap on Universal's own dining guide) | No (category itself is wrong on listings) | No (founding myth silent, Sichuan vacancy open) |
| **Single highest-impact free recommendation** | Get on the CityWalk Guide to Dining list | Rebrand to "Wagyu Tasting House" on all listings | Activate the founding myth on menu and wall |
| **Single highest-dollar lever** | Tiered nigiri pricing + anchor signature roll | **Beverage program fix ($300K–$700K/yr)** | Two-portion pricing transparency |

### The pattern that shows up across all three

Each restaurant owns a position that isn't being pressed. Each is rated below where the category math would predict — not because the food is bad, but because a specific structural issue (throughput at Wasabi, category mismatch at Yakiya, underactivated heritage at Panda Inn) is capping visible reputation. None of the fixes require capital expenditure. All of them are implementable within 60–90 days. The dollar lever at Yakiya alone — the beverage program fix — sits at a scale that would justify the entire engagement by itself.

---

*For the full version of each competitive analysis, see `02-menu-intelligence-wasabi.md`, `03-menu-intelligence-yakiya.md`, `04-menu-intelligence-panda-inn.md`. Raw Apify data files are in `_raw-data/`.*
