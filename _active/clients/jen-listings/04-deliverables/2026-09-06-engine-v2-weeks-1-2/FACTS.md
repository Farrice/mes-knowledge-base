# facts ledger · weeks 1 and 2 (operator only, never in the Drive folder)

Every number in the six posts, where it came from, and what to re-check on send day. Labels: VERIFIED (read from the source today) · LIKELY · UNCONFIRMED.

## pulled 2026-09-02

| used in | claim | label | source | re-check |
|---|---|---|---|---|
| 01 attract | 6324 Tampa, Tarzana 91335 · $869,000 · 3 bd / 1.5 ba · 1,136 sq ft · 7,296 sq ft lot · "ideal for future ADU expansion" | VERIFIED | Redfin Tarzana search, house, $800K–$950K | still active Sept 8? price unchanged? |
| 01 attract | 6531 Hayvenhurst Ave, Van Nuys 91406 (Lake Balboa) · $850,000 · 3 bd / 1 ba · 1,126 sq ft · "steps from Lake Balboa Park" | VERIFIED | Redfin Sherman Oaks search spillover ("nearby homes") | still active Sept 8? |
| 01 attract | 15035 Gilmore St, Van Nuys 91411 · $815,000 · 4 bd / 1.5 ba · 1,390 sq ft · pool | VERIFIED | same | still active Sept 8? |
| 02 position | 30-yr fixed averaged 6.66% week of Aug 27, 2026 (6.65% prior week; 6.56% a year ago) | VERIFIED | Freddie Mac PMMS release Aug 27, 2026 | Sept 3 release lands the day after build; swap the number on the card and caption if it moved (`build_weeks.py`, two strings) |
| 02 position | half a point on $850,000 with 20% down ≈ $220/mo | VERIFIED (arithmetic) | $680,000 loan, 30-yr: 6.66% → $4,369/mo P&I; 6.16% → $4,147/mo; diff $222 | illustrative; principal + interest only, stated as "about" |
| 03 convert | 5421 Bothwell Rd, Tarzana · Active · $5,695,000 · listing agents Marty Azoulay + Jennifer Santulan · updated Sept 2, 2026 2:22 PM | VERIFIED | coldwellbanker.com listing page (MLS SR26099697) | Jen confirms price and status from her MLS before Sat Sept 12 |
| 03 convert | 5,468 sq ft main · 882 sq ft ADU with kitchen · 238 sq ft rec room · 6,588 total · white oak floors/cabinets · Taj Mahal quartzite · Thermador + Sub-Zero · Venetian plaster (office, powder, theater, primary bath, fireplace) · pocket doors living → backyard · pool · half basketball court · 11 ft ceilings down | VERIFIED (her spec sheet) | `5421-bothwell-tarzana/listing-package.md` (spec sheet, 2026-05-07) | none; hers |
| 04 attract | 3928 Madelia Ave, Sherman Oaks 91403 · $899,900 · 1 bd / 1 ba · "generous lot… expand or build" | VERIFIED | Redfin Sherman Oaks search, house, $800K–$1M | still active Sept 15? |
| 04 attract | 6467 Woodley, Van Nuys 91406 · $888,000 · 4 bd / 2 ba · 1,576 sq ft | VERIFIED | same page (compact row; no description shown) | still active Sept 15? confirm bd/ba from MLS |
| 05 position | CA FAIR Plan +29.1% average, effective Oct 15, 2026; weighted to wildfire risk; policy start date sets the rate | VERIFIED (prior session, CDI) | `COPY-FINAL-v2-condo-and-reels.md` reel 3, sourced California Dept of Insurance | none |
| 06 position | Tarzana median sale price $949,676, Jul 2026, −14.5% YoY, all home types | VERIFIED | Redfin Tarzana page, "real estate trends" | Redfin's Aug 2026 figure lands mid-Sept; refresh the card if it prints before Sat Sept 19 |
| 06 position | Tarzana inventory ranges $650,000 to $19,999,000 (149 houses) | VERIFIED | Homes.com Tarzana summary via search | fine as a range |
| 06 position | Sherman Oaks median $1,524,480 Jul 2026, −1.6% YoY | VERIFIED (not used on a frame) | Redfin Sherman Oaks page | banked |

## not used, and why

- 5200 Armida (her Aug 5 listing at $3,199,000): status UNCONFIRMED today; one search hit shows a different Armida address at $1,599,000. Ask Jen. If still active it becomes week 3's convert reel; the shoot sheet has the lines.
- 6319 Aura Ave, Tarzana 91335 · $925,000 · Equity Union listing (her brokerage, not hers). Can't be posted as hers; could be the week 3 "what $X buys" anchor if the listing agent is fine with it.
- The Van Nuys city URL on Redfin redirects to Great Barrington MA (bad city id); Van Nuys comps came from the Sherman Oaks page's "nearby homes." Enough for two posts; pull a clean Van Nuys page for week 3.

## the rules these posts obey

- Other agents' listings are described by neighborhood, price, and specs, never by address on the frame or in the caption. The addresses go out only in her DM, one to one. (CRMLS advertising rules on another broker's listing; also the mechanism: the address is the reason to write.)
- No "first home," no "first-time buyer," no buyer-type hashtag. "Buying or selling" appears in every ask (ENGINE-V2 §1 guardrail).
- Fair-housing floor: `python3 execution/fair_housing_lint.py COPY-weeks-1-2.md` before every Drive drop.
- Photos are placeholders until folder 01 has her shoots; `PHOTO-SWAP.md` is the map. Nothing goes to Drive folder 04 on placeholders.
