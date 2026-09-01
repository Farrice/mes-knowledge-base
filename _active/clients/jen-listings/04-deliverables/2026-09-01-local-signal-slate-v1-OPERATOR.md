# LOCAL-SIGNAL RUN: Jen Santulan — San Fernando Valley (operator receipts, 2026-09-01)

Paired file for `2026-09-01-local-signal-slate-v1.md` (the Jen-facing slate). This file never goes to Jen.

Pipeline: `/enrico-local-signal-loop` (workflow 11) → `realtor_local_signal_engine.py` scoring guard → Jen skill register (calm-warm @_jiing lane) → Sherrard carousel grammar → fair-housing lint → prose classifier. Payload and engine output: `.tmp/jen-sfv-local-signals-2026-09-01.json` / `.result.json`.

## AGENT FIT CARD

| Field | Value | Evidence |
|---|---|---|
| Market | San Fernando Valley | canon |
| Niche | first-time buyers; luxury listings on a separate Quiet Flex register | `_active/clients/jen-listings/CLAUDE.md` |
| Target person (this run) | renting couple, mid-30s to early 40s, ~$2,900 for a 2-bed in Van Nuys/Reseda, touring $450–550K condos and $700–900K houses | rent: apartmenthomeliving 2026-08-28 (LIKELY) |
| Voice markers | calm-warm lowercase, gentle misconception-correct, ellipses, one emoji, invitation closers | `references/jen-real-voice-profile.md` |
| Convictions on file | "hardest part is figuring out what's actually true" (her caption, 2026-07-25); authority-POV hook pick (5200 Armida, 2026-08-05) | VERIFIED |
| Production comfort | talking head + lav, walk-and-talk, b-roll takeover, serif single-word captions | voice profile |
| Weekly capacity | **3 posts/week — ASSUMPTION, not confirmed by Jen** | ask her in her words: "how many could you actually film in a sitting?" |
| Offer | no-pressure game-plan chat | voice profile CTAs |
| Response owner | Jen | — |
| Compliance | fair-housing floor, schools off camera, no urgency, **no keyword CTAs** (Jen: cheesy, 2026-09-01), no unverified price/program claims | memory + client CLAUDE.md |

## SIGNAL PACK

| ID | Type | Source / date | Evidence | Transfer |
|---|---|---|---|---|
| S1 condo full review | local_source | Fannie LL-2026-03 / Freddie 2026-C, eff. 2026-08-03; TheStreet, Zeitro, Goeglein (Aug 2026) | VERIFIED | topic_only |
| S2 FAIR Plan +29.1% | local_source | CDI approval, eff. 2026-10-15; Yahoo Finance, zacsellsca, caroline-park (Aug 2026) | VERIFIED | topic_only |
| S3 East SFV light rail | local_source | Metro $2.43B contract; Commercial Observer 08-14, Daily News 08-24, LA Times 08-20, LADOT 08-06 | VERIFIED | topic_only |
| S4 Prop 37 | local_source | CA Budget & Policy Center 2026-08-12 | VERIFIED | topic_only |
| S5 rates 6.66% | local_source | Freddie PMMS 2026-08-27 | VERIFIED | topic_only |
| S6 cutout-over-place format | format_reference | Sherrard/Thornburg frame T-0010 (San Diego) | VERIFIED format; reach UNCONFIRMED | format_only → SFV |
| S7 her misconceptions reel | own_channel_signal | @_jiing DYkn2gBPWJq, scrape 2026-07-25 | VERIFIED | lived_experience |
| S8 "family-friendly Reseda" | lived_observation | negative control | UNCONFIRMED | — |
| S9 Reseda vs Van Nuys gap | local_source | zacsellsca July MLS summary 2026-08-05 (single source) | LIKELY | topic_only |

## ACCEPTED RANKING (engine output)

| Rank | Signal | Local | Audience | Conviction | Conversation | Production | Total |
|---|---|---|---|---|---|---|---|
| 1 | S7 own-channel pattern | 1 | 2 | 2 | 2 | 2 | 9 (pattern input, not a topic) |
| 2 | S1 condo full review | 1 | 2 | 2 | 2 | 2 | 9 |
| 3 | S3 light rail | 2 | 2 | 1 | 2 | 2 | 9 |
| 4 | S4 Prop 37 | 0 | 2 | 1 | 2 | 2 | 7 |
| 5 | S2 FAIR Plan | 2 | 1 | 1 | 1 | 2 | 7 |
| 6 | S6 format ref | 1 | 1 | 1 | 1 | 1 | 5 |

**Judgment override on the 4th/5th tie:** engine broke the S4/S2 tie on id. I shipped S2 (FAIR Plan) over S4 (Prop 37) because Prop 37 is statewide, new-construction-only, and a November political story on her grid. That is her call, not ours. S4 is parked as the fourth concept with a candidate hook: "the ballot measure everyone will DM me about."

## REJECTION RECEIPTS

| Signal | Rejected because | Safe continuation |
|---|---|---|
| S5 rates update | artificial_opinion, generic voice | fold the 6.66% figure into a caption line only when a concept needs it; never a standalone post (Sherrard: "stat without translation = billboard") |
| S8 Reseda family pocket | fair_housing_steering (engine + `fair_housing_lint.py`) | rebuild as housing-stock/price/commute facts about Reseda with no audience descriptor |
| S9 Reseda vs Van Nuys gap | unsourced_factual_claim (LIKELY, single source) | pull Redfin "median sale, last 3 months" for both the day of posting → re-run engine → eligible |

## VERIFY-BEFORE-POST LEDGER

| Claim in slate | Status | Action before Jen posts |
|---|---|---|
| Full Review on conventional condo loans from 2026-08-03; reserve floor 10%→15% from 2027-01-04; $50K per-unit deductible cap; 15% delinquency threshold | VERIFIED (3 independent lender/legal writeups citing LL-2026-03) | none; optional: pull the lender letter PDF for the file |
| FAIR Plan +29.1% avg, effective policies dated on/after 2026-10-15, weighted to wildfire | VERIFIED (CDI approval reported by 4+ outlets) | none |
| "policy effective before Oct 15 generally written at current rate for term" | LIKELY (broker/agent explainers) | Jen confirms with her insurance broker before saying on camera; carousel slide 5 says "generally" |
| Valley-floor admitted carriers ~$1,800–$3,500/yr | LIKELY (community thread + broker post) | kept OFF the reel; carousel slide 4 gives no number; caption says "regular carrier" only |
| FAIR + DIC "well above a standard policy" | LIKELY (40–65% figure from lametrohomefinder) | slate uses no percentage |
| Light rail: $2.43B contract, 6.7 mi, 11 stations, Van Nuys→San Fernando Rd, opening Dec 2031, 7–10 min peak headways | VERIFIED (Metro via Commercial Observer, Daily News, LA Times, LADOT) | none |
| Van Nuys G Line station closed for rebuild until ~Dec 2027 | VERIFIED as of 2026-07-02 (`6853-willis proof-claims-ledger.md`) | re-check Metro page the week of posting |
| SFV condo median $489,500 / 34 DOM (July) | LIKELY (single agent MLS summary) | **not used in slate**; if Jen wants a number on the condo reel, pull Redfin same-day |
| "condo in van nuys under 500" (reel 1 scene) | scene framing, not a stat | fine as spoken; do not add a median |
| Dream For All 2026 window closed Mar 16 | VERIFIED | "watch for next round" only |

## THE CTA FORK (decided, reversible)

Sherrard's carousel grammar ends on a keyword CTA card ("DM me 'AUSTIN'"). Jen finds keyword CTAs cheesy (2026-09-01). Shipped alternative: an **address-first process ask** ("send me the address before you write... i'll read the package with you"). It reads experienced and trustworthy, gives her a real reply to make, and sets up the routing question below. If she wants automation later, ManyChat can trigger on any DM containing a street number, no keyword needed.

## CONVERSATION BRIDGE

```
reel/carousel → "send me the address / tell me how long you're staying"
→ Jen replies within the evening (human)
→ routing question: "are you here for the valley updates, or actually looking this fall?"
→ need-discovery: timeline, condo vs house, pre-approval status
→ CRM: tag source concept (condo / rail / insurance) + next step (HOA read, quote pull, game-plan chat)
```

Follower who only wanted the update gets the update. No sequence.

## ATTENTION LEDGER (per post)
reach · 3-second hold · completion · saves · shares · profile visits · comment count. Status: **NO EVENT**.

## PIPELINE LEDGER (per concept)
address DMs · qualified conversations · game-plan chats booked · signed buyers · closed revenue. Status: **NO EVENT**.

## CADENCE + FORMULA SYNTHESIS (what the slate is built on)

| Mechanic | Evidence | Label |
|---|---|---|
| 2 Reels + 1 carousel per week as the floor | Emily Terrell 2026-08-10; Reallyo 3-3-3 rule 2026-09-01; Shhots "3/week for 90 days" 2026-08-24 | LIKELY (practitioner consensus, no controlled data) |
| Reels 15–45s; completion is the ranking signal | Shhots citing Instagram 2026-08-24; videoguru 2026-08-21 | LIKELY |
| Hook in first 2–5s with on-screen text; agent on camera 1.6–1.8x vs faceless | BIGVU 10-account analysis 2026-08-13 | LIKELY (n=10, one vendor) |
| Carousel = 6–8 slide save-and-send asset; hook → numbered slides → one CTA | Sherrard workflow 04; Terrell 2026-08-10 | VERIFIED as method, NO EVENT as outcome |
| Local signal → own take → conversation, attention ≠ pipeline | Sherrard/Thornburg 2026-06-24 extraction | VERIFIED as method; reach anecdotes UNCONFIRMED |
| Her own pattern: misconception-correct talking head + closing question | @_jiing scrape 2026-07-25 | VERIFIED own-channel |

## EVIDENCE LIMITS + NEXT PROOF GATE

- Cadence of 3/week is an assumption about Jen's capacity; the loop's rule is capacity sets cadence, so confirm before she commits.
- Concept 2's opinion is a candidate POV. `voice_approved: false` until she says it's hers.
- Nothing here has published. All performance is NO EVENT. First proof gate: one concept posted (reel + carousel), 7 days of attention data, and any address DMs logged separately.
- Cost of this run: 8 Perplexity search calls (est. under $0.10, UNCONFIRMED against the tracker); no paid generation.
