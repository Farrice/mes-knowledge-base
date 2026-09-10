# Gigi Mironova — demand + brand foundation

Living doc. Everything v2 is built on has to trace back to a line in here. Researched
2026-08-31, free tools only, $0 spent.

---

## 1. The brand is not a guess any more

Pulled from the live sites, not inferred.

| Asset | Value | Source |
|---|---|---|
| HouseSellers logo blue | **#0C4071** (gradient range #083D6E → #23527F) | pixel-sampled from `company-logo.png` |
| Equity Union primary navy | **#174579** (758 uses) | computed styles, equityunion.com |
| Equity Union deep navy | **#0F2D4F** | computed styles |
| Equity Union steel | **#687994** | computed styles |
| Equity Union body grey | **#333333** | computed styles |
| Structural face | **Futura / futura-pt**, fallback declared as **Jost** | computed styles |
| Display serif | **Bodoni Moda** | computed styles |
| Logo face | Trajan Pro | computed styles |

**The finding that matters: Equity Union's own homepage is already built in the exact
grammar the editorial system uses.** Their hero is a geometric sans with a high-contrast
serif italic accent word ("MOVE *FORWARD*") on navy. That is structurally the same move as
Figtree + Playfair italic + navy — the thing that makes the system read editorial instead of
corporate is *already the brokerage's own top-tier brand language*.

Nobody on the team uses it below the homepage. That is the whole opening: this is not an
outside style imposed on their brand, it is their brand, executed the way their own
homepage does it.

`myhousesellers.com` is a stock IDX vendor template — Open Sans, literal Bootstrap blue
(`#0D6EFD`), no design system. The only real brand asset there is the logo. So "the
HouseSellers brand" in practice means **the HouseSellers lockup sitting inside the Equity
Union house system**, which is where the actual design language lives.

### Type decision, with its one known gap

- **Jost carries the structural role in both languages.** It is Equity Union's own declared
  Futura fallback, it is free, and it ships `cyrillic`. One face, brand-faithful, bilingual.
  Strictly better than the Figtree + Manrope split v1 needed.
- **Bodoni Moda has no Cyrillic subset at all** (latin, latin-ext, math, symbols only).
  Verified against the Google Fonts CSS API. Playfair Display italic ships Cyrillic and is
  the closest high-contrast stand-in, so it takes the accent word on Russian slides only.
  Prata has Cyrillic but no italic; Cormorant is too low-contrast to sit next to Bodoni.

---

## 2. The Russian lane is NOT empty. My v1 claim was wrong.

The v1 brief said *"almost no one is producing quality real-estate content in Russian for the
LA market."* That was an assumption and it does not survive contact with a search.

Established Russian-speaking competitors, LA / SFV:

| Who | Position | Overlap with her territory |
|---|---|---|
| **Gary Rapoport** (GBR Properties, Burbank) | 20–25 yrs, brands explicitly as "Russian Speaking Real Estate Broker", own YouTube channel, 22 Yelp reviews | Sherman Oaks, Encino, Studio City, Tarzana, Woodland Hills, North Hollywood — **direct** |
| **Jacob Arutiunian + Liubov Savoskin** | 10+ yrs, stated $120M+ volume | LA |
| **Svetlana Yukin** | 16 yrs LA, NAR + CAR member | LA |
| **Olga Ribardo** | Keller Williams, CalDRE 01955978 | Pasadena |
| **Chernov Team** | "premier real estate services group in the SFV" | Studio City, Sherman Oaks, Encino — **direct** |

Plus two standing Russian-language YouTube channels aimed at this market
(«Риелтор в Лос Анджелесе», «Риелтор в Калифорнии»), a Russian-language LA realtor
directory (bazar.club), and a listicle of LA agencies with Russian-speaking staff.

**What this changes.** The lane is real but contested, and at least one incumbent owns her
exact geography with a 20-year head start and the literal words "Russian Speaking" in his
business name. Positioning Gigi *around* Russian would drop her into a fight she did not
pick, against people who have been in it for two decades.

**What survives.** Russian stays a genuine capability and a real edge — as **one pillar**,
not the spine. A translated version of the strongest post costs almost nothing to produce
and reaches an audience most of her team cannot. That is additive. It is not an identity.

**Still unconfirmed:** nobody's *content quality or volume* was measured. Subscriber counts,
posting cadence and engagement for the two YouTube channels were not opened. Whether anyone
is doing Instagram-native short-form in Russian for this market is unknown, and it is the
one question that would tell us if there is a format gap even though there is no market gap.

---

## 3. The real demand finding: what the SFV market is actually doing

**San Fernando Valley, April 2026, 556 closed sales** *(source: Zac Wasserman / RE/MAX ONE
market update, aggregating recent closed sales — one agent's compilation of MLS data, not an
official association report; label LIKELY, re-verify against a second source before any
number ships)*

| Metric | Value |
|---|---|
| Median closed price, all types | $1,034,250 |
| Median single-family | $1,224,500 |
| Median $/sqft | $637 |
| Median days on market | 22 |
| **Average** days on market | **40.7** |
| Sale-to-list ratio | 99.6% |
| Sold **above** original list | 32.7% |
| Sold **below** original list | 56.8% |
| **Transactions with seller concessions** | **52.9%** |
| **Median concession** | **$25,000** (average $31,116) |
| Sold in 0–7 days | 19.6% |
| Sold in 60+ days | 20.0% |

**National context (VERIFIED — Redfin, three months ending 2026-05-31, carried by multiple
outlets):** concessions in **46.2%** of US home sales, up from 43.1% a year earlier — the
highest spring share since Redfin began tracking in 2019. Roughly **47% more sellers than
buyers** in the market nationally. Metro spread is wide: San Diego 62.3%, San Francisco
14.9%, San Jose 5.9%.

### The story inside the numbers

Three real ones, none of which anyone on her team is posting:

1. **The list price stopped telling the truth.** Sale-to-list is 99.6% — which reads like
   everyone is getting their number. But 52.9% of sellers wrote a concession averaging
   $25–31K. The negotiation moved off the price and into the concessions, where it does not
   show up in the comps your neighbour quotes at you.
2. **SFV concedes more than the country does.** 52.9% local against 46.2% national. A seller
   here planning to hold firm is planning against the majority of their own market.
3. **"22 days" is a fiction.** Median 22, average 40.7, and a fifth of homes sit past 60
   days while another fifth go in under a week. It is two markets wearing one statistic, and
   which one a seller is in is decided before the listing goes live.

Every one of these is a seller story, which matters: her team is literally called
**My House Sellers**.

---

## 4. Gaps and what they cost

- **Ahrefs API returns `Insufficient plan`** — no keyword volume, no search-suggestion
  mining, no SERP gap analysis. Everything above is search-result and published-data
  research, not query-volume data. Real volume would need a plan upgrade or a paid research
  pass, neither of which is approved.
- **No paid research run.** Gemini Deep Research ($10 ceiling) and Perplexity were not used;
  no budget was approved. Everything here is free-tier.
- **Her own listings are the strongest unused asset.** 6853 Willis Ave and 1654 Moonseed Ln
  are already on disk with verified material. Real photographs of her actual inventory beat
  every CC0 frame in the bank, and they are hers, which is the whole point.
- **Not measured:** her per-post engagement, her actual farm-area concentration, and whether
  the concession pattern holds in her specific price bands.
