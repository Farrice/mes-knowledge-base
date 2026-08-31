# Same Door — complete creative brief & asset handoff

Everything needed to enrich these designs in Claude Design without breaking what is
verified, compliant, or deliberate. Current as of 2026-08-31.

---

## 1. The two live surfaces

| Surface | URL | What it is |
|---|---|---|
| **Design canvas** (editable) | <https://claude.ai/code/artifact/1785940e-b1f7-49e5-a897-56dac8eab4e1> | 21 artboards. Click to select, properties panel, inline text edit, PNG/PDF export. **Save** republishes for everyone. |
| **Kit page** (what Gigi receives) | <https://claude.ai/code/artifact/595f01a0-e79c-47ee-9148-19442b475c14> | The finished package: carousels, reel scripts, captions, story sequence, covers, don't-say list. |

Canvas mechanics: each artboard is independent (no shared state). Photos are **named
files** — swapping one means replacing the file of the same name and re-saving. `Main` is
carousel slide 1.

---

## 2. The design system

**Type** — Figtree 400/500/600/700 structural, lowercase headline register · Playfair
Display italic 500 as the accent word, **one per slide, headline scale only, never on a
numeral** · Manrope for Russian (Figtree ships no Cyrillic).

**Palette** (soft navy, derived from HouseSellers `#0C4071` / Equity Union `#174579`):

| Token | Value | Role |
|---|---|---|
| ink | `#2C4A68` | headings + body on white |
| band | `#243D56` | dark ground, photo tint base |
| muted | `#75879C` | secondary copy |
| hairline | `#E3E9F0` | rules, dividers, left-borders |
| ghost | `#EDF1F6` | oversized background numeral |
| accent | `#5E86AC` | italic accent, light grounds |
| accent-lt | `#C3D4E5` | italic accent, dark grounds |
| paper | `#FDFDFC` | warm white |
| bone | `#F2F5F8` | tint panel on white slides |

**Grammar** — 1080×1350 · 64/72px padding · ruled header (name + series) and footer
(context + pagination) · oversized Playfair ghost numeral, 760px, bled off the right ·
two photo treatments only (`bleed` = colour held under a scrim, `duo` = navy duotone) ·
a left-to-right **panel** gradient under the text column so photo texture never sits
under type · dense data belongs on white, never on a photograph · framing is per-slide
inline, never global.

**Rhythm** — roughly 4 photographic story slides to 3 white structure slides per
carousel. The white slides are the luxury, not a gap.

---

## 3. Her own brand signals (from her live carousel)

Worth knowing before "improving" anything — this is what her audience already sees:

- Bold condensed **uppercase** headlines, dark charcoal-navy
- A **warm orange/tan italic script** accent ("*in December 2023*") — her accent is warm,
  ours is cool blue. A deliberate fork, not an oversight: hers reads friendly-agent, ours
  reads brokerage-editorial. **Worth testing a warm accent variant** in the canvas.
- White card layout, photo-dominant, small grey body copy
- Numbered badges bottom-left (1–8)
- Sign-off slide: check bullets, large price, script signature logo + Equity Union lockup

---

## 4. Assets on disk

`_active/clients/gigi-mironova/production/same-door/`

| Asset | Path | Notes |
|---|---|---|
| Board source | `*.dc.html` (21) | canvas format; `Main` = slide 1 |
| Layout | `canvas.json` | positions, 3 rows |
| Canvas images | `canvas-assets/` (9) | downsampled; referenced **by filename** |
| Full-res imagery | `../american-transaction/imagery/prepared/` | CC0/PDM only |
| Provenance | `../american-transaction/imagery/provenance.jsonl` | id, licence, provider, source URL per file |
| Her headshot | `../../brand/gigi-headshot.jpg` | 512×512, from her Equity Union profile |
| HouseSellers logo | `../../brand/housesellers-logo.png` | pixel-sampled `#0C4071` |
| Highlight covers | `covers/` (9) | 1080×1080, upload-ready |
| Rendered boards | `png/` (21) | 2160×2700 |
| Contact sheet | `review/sheet.png` | the review surface — always check here first |

**Regenerate:** `python3 build.py && python3 build_drops.py && python3 render.py &&
python3 review_sheet.py && python3 share_page.py`

---

## 5. Her real listing photography — the gap and the map

**I could not pull these.** Instagram blocks post images without login; her profile is
readable, the media is not. The screenshot is the only version I have, at roughly
170×200px per tile — far too small for a 1080×1350 board.

**She already has all eight.** Ask for the originals; here is exactly where each one
goes, using her own slide numbers:

| Her slide | Photo | Best slot in this system |
|---|---|---|
| 1 | Living room, remodeled | **C1** hook — replaces the Valley-at-dusk |
| 2 | Kitchen, stainless appliances | **C2** or the reel-1 cover |
| 3 | In-unit stacked washer/dryer | **R2** cover — a genuine differentiator shot |
| 4 | Dining / move-in ready | **C4** (the equity slide) |
| 5 | Bedroom with balcony access | **C6** close |
| 6 | Bathroom | spare |
| 7 | **Balcony** | **C3 / C5** — the SB 326 slide (see §6) |
| 8 | Her sign-off card | reference only — do not reuse |

Treatment when they land: `bleed` for warm interiors, `duo` for architecture. Never
apply a global scale.

---

## 6. Verified facts — the guarded set

Nothing in this column may change without new evidence.

**From her listing carousel (VERIFIED — her own published marketing):**
fully remodeled December 2023 · appliances purchased Dec 2023, all included · in-unit
washer & dryer, purchased Dec 2023 · 2-car parking · building insurance in place ·
**balcony inspection & repairs completed** · private balcony, bedroom with balcony
access · $319,999 · Gigi@myhousesellers.com · 818.826.9998

**From MLS / brokerage (VERIFIED):** unit 124, 1 bed / 1 bath, 619 sqft, MLS SR26183330 ·
also listed for lease at $2,500/mo · unit 208 at $2,400/mo · her DRE 02025393 · 16 years
litigation support (her Equity Union bio, her words) · building comps $309,000–$399,999

**Computed 2026-08-31, labelled "estimate, not a quote" wherever shown:**
$1,645 P&I (20% down, 6.66%) + $333 tax (est. 1.25%) + $477 dues + $60 insurance =
**$2,515/mo**, and **$224** of month one is principal. Rate: Freddie Mac PMMS 8/27/26.

**LIKELY, labelled on-slide:** building 12-month average sale $393,000 · 82 average days
on market · SFV median $1,034,250 · SFV April concessions 52.9%, median $25,000 ·
sale-to-list 99.6% · DOM median 22 / average 40.7.

**VERIFIED, currently unused — the biggest opening in the deck:**
California **SB 326** required condo HOAs (3+ units) to complete exterior-elevated-element
inspections by **January 1, 2025**. That deadline is over a year past. Where work was
deferred, special assessments of **$40,000–$60,000 per unit** are common, and in 2026
lenders are rejecting mortgages on condos whose HOA has no valid Balcony Safety
Certificate on file.

→ **Her listing states the balcony inspection and repairs are done.** That is the single
strongest de-risking fact in the whole listing and it is sitting sixth on her last slide.
Recommended as its own carousel: the ambush isn't the monthly dues, it's the assessment —
and this building already handled it.

**UNCONFIRMED — never assert:** unit 124's exact dues (the $477 is the building's
recorded figure for a 2-bed; say "recorded for this building") · whether the HOA holds a
current Balcony Safety Certificate (her listing says work is complete; that is her claim
about her listing, not a certificate confirmation) · year built (1990 vs 1991 across
sources) · unit count (83 vs 132) · which Instagram handle is primary
(`@gigimironova_realestate` is live and matches her bio; a second `@gigi__mironova`
also surfaced).

---

## 7. Compliance rails — non-negotiable

- Never describe a neighborhood or building by who lives there. Speaking Russian is a
  **service**, never a description of an area, in either language.
- "Estimate, not a quote" stays wherever $2,515 appears.
- Never say owning is cheaper than renting. Say "about the same, before equity."
- The $477 is "recorded for this building," never "unit 124's dues."
- No "guaranteed," no "always appreciates."
- Russian copy is a native-speaker draft for Gigi to correct — do not treat as final.
- Client-facing surfaces carry **zero operator language**: nothing that diagnoses her
  feed or her results. That lives only in `../../OPERATOR-NOTES.md`.

---

## 8. Paste-ready prompt for Claude Design

> Refine these artboards without changing the system. Type: Figtree structural, lowercase
> headline register, with exactly one Playfair Display italic accent word per slide at
> headline scale — never on a numeral. Palette: ink #2C4A68, dark ground #243D56, muted
> #75879C, hairline #E3E9F0, accent #5E86AC (light) / #C3D4E5 (dark), paper #FDFDFC.
> Format 1080×1350, 64/72px padding, ruled header and footer, an oversized Playfair ghost
> numeral bleeding off the right edge. Photography is real only — no generated images —
> treated as navy duotone or scrimmed colour bleed, always with the left-to-right panel
> gradient so type never sits on busy texture. Dense data goes on white grounds, never on
> a photograph.
>
> These numbers are verified and must not change: $2,500 rent, $319,999 list, $477
> recorded dues, $2,515/mo estimate at 6.66%, $224 month-one principal, $393,000 building
> average, 82 days, $1,034,250 SFV median, 17/17/21 contingency days, 52.9% concessions,
> $25,000 median concession. Keep "estimate, not a quote" wherever $2,515 appears. Keep
> every fair-housing rail: no neighborhood demographics, dues always "recorded for this
> building." Russian text is a native-speaker draft — do not rewrite it.
>
> Voice: calm, precise, conversational, no exclamation marks. Each slide must hand off to
> the next — the carousel is one argument, not six statements.

**If enriching with her real photos:** replace the file of the same name in
`canvas-assets/`, keep the treatment class, set `object-position` per slide, and never
add a global transform.

---

## 9. What I would enrich first, in order

1. **Her eight listing photos** — replaces every CC0 stand-in and makes the whole set
   hers. One ask, five boards upgraded.
2. **The SB 326 carousel** — the strongest unused angle in the material, and it is
   already true of her listing.
3. **A warm accent variant** — her own carousel uses a warm orange/tan accent. Worth one
   artboard testing warm against the current cool blue before committing.
4. **Unit 124's actual dues** — turns the estimate into her number.
5. **A current portrait she likes** — the 512px brokerage headshot is holding R4.
