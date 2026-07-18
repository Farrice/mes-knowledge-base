# Source Ledger — re-compliance-pack (RE-1 Fair Housing Auditor)

Every authority claim used in `SKILL.md`, `genius.md`, `README.md`, `workflows/01-fh-auditor.md`, `references/hud-standards/hud-word-phrase-list.md`, and `references/test-listings.md`, checked claim-by-claim. Verification pass run 2026-07-18 via live web search (Cornell LII, eCFR, nar.realtor, HUD/Fair Housing nonprofit summaries, Keller Williams official materials). No claim below was answered from training memory alone — see method note at bottom.

## VERIFIED

| Claim | Where used | Verification |
|---|---|---|
| **24 CFR §100.75** ("Discriminatory advertisements, statements and notices") is the actual Fair Housing Act regulation governing prohibited-bases advertising language. | `SKILL.md`, `genius.md`, `workflows/01-fh-auditor.md`, `references/hud-standards/hud-word-phrase-list.md` | Confirmed live at law.cornell.edu/cfr/text/24/100.75 and ecfr.gov, 2026-07-18. Text matches: prohibits indicating preference/limitation/discrimination based on race, color, religion, sex, handicap, familial status, or national origin in advertising. |
| **NAR Code of Ethics Article 12** governs truthfulness in REALTOR® advertising and requires Fair Housing Act compliance in marketing. | `SKILL.md`, `genius.md`, `README.md` | Confirmed live at nar.realtor (Article 12 text + case interpretations page), 2026-07-18. Article 12 covers "honest and truthful communications" and "true picture" in advertising; fair-housing training is a related NAR requirement. |
| **KW MREA 8x8 / 33-touch follow-up standard** exists as a documented Keller Williams lead-nurture cadence (8 touches over 8 weeks, then 33 touches/year). | `SKILL.md` (RE-2 authority row) | Confirmed via official Keller Williams instructor PDF (kw-sites.s3-us-west-2.amazonaws.com "8 X 8 + 33 TOUCH = MAGIC") and multiple independent real-estate-coaching summaries, 2026-07-18. |
| **12 CFR §1026.19(f)(1)(ii)(A)** (TRID Closing Disclosure timing — 3-business-day rule; §1026.19(e) governs Loan-Estimate timing) is a real, currently-in-force regulation. Subsection corrected from (e) to (f)(1)(ii)(A) by Opus adversarial verify, 2026-07-18. | `SKILL.md` (RE-3 authority row) | Confirmed live at law.cornell.edu/cfr/text/12/1026.19 and consumerfinance.gov, 2026-07-18. |
| **$19,787** is a real HUD-published figure. | `SKILL.md` line 28, `README.md`, `genius.md` (Voice & Education Tone) | Confirmed via fairhousingnc.org civil-penalty-adjustment summary, 2026-07-18 — **but** it is documented as the inflation-adjusted **maximum** civil penalty for a first Fair Housing Act violation under 24 CFR §180.671, not a "median" of actual settlements as the pack's copy states. The number is real; the "median" framing is a mischaracterization. Flagged as an anti-pattern in `genius.md`, not silently corrected in `SKILL.md`/`README.md` (out of scope for this repair pass — those checks were passing).

## LIKELY

| Claim | Where used | Note |
|---|---|---|
| A 2016 HUD guidance document treats "walking distance to schools" and similar school-proximity phrasing as familial-status-coded advertising language. | `genius.md`, `workflows/01-fh-auditor.md`, `references/hud-standards/hud-word-phrase-list.md` | The *general principle* is confirmed as standard fair-housing-advertising guidance (multiple secondary sources, 2026-07-18: distinguishing "walking distance to [named school]" as lower-risk/factual vs. "great schools for your kids" as exclusionary). Could not pin the citation to one specific titled 2016 HUD document this pass — treat "HUD Guidance 2016" as shorthand for a real, recurring guidance theme, not a single verified document title. |
| NAR SOP 11-1 requires five specific opinion-of-value disclosures for CMAs. | `SKILL.md` (RE-3 description) | Not checked this pass — RE-3 workflow does not exist yet (README: "coming"). Concept is consistent with known NAR CMA-disclosure practice but the specific "five mandatory disclosures" enumeration is unverified. |
| Fannie Mae B3-3.2-01 is relevant TRID/CMA authority. | `SKILL.md` (RE-3 authority row) | Not checked this pass — same reason as above (RE-3 not yet built; out of this repair's scope). |

## UNCONFIRMED

| Claim | Where used | Status |
|---|---|---|
| ***Fair Housing Council v. 1734 East 82nd Street*** (9th Cir. 2019) — holding that "safe neighborhood" is race-coded. | `genius.md` (Case Law Armory, Tier 1 dog-whistle codes), `workflows/01-fh-auditor.md` (example citations), `receipts/audit-test-listing-1.json` | Could not locate this case in public case-law search (HUD case database, DOJ housing case list, general web search) as of 2026-07-18. Do not present as settled precedent to Jen or her broker without independent legal-database confirmation. |
| ***United States v. Newberry*** (4th Cir. 1999) — holding that age-coded language ("retirees," "young professionals") violates familial status. | Same locations as above | Could not locate this case in public search, 2026-07-18. UNCONFIRMED. |
| ***Fair Housing Center v. Sears*** (8th Cir. 2009) — holding that "quiet area" implies disabled persons unwelcome. | Same locations as above | Could not locate this case in public search, 2026-07-18. (A 2009 EEOC v. Sears ADA *employment* case exists but is unrelated to housing advertising and is not the case being cited here.) UNCONFIRMED. |
| ***Fair Housing Center of West Michigan v. Karwoski*** (6th Cir. 2015) — holding that photos + language together amplify discrimination. | Same locations as above | Could not locate this case in public search, 2026-07-18. The Fair Housing Center of West Michigan is a real organization (fhcwm.org) but no matching case titled "v. Karwoski" surfaced. UNCONFIRMED. The underlying principle (visual + textual discrimination compounding) is independently consistent with general fair-housing-advertising guidance, but the specific case citation is not confirmed. |

## Method Note

Verification run via live web search (not training-memory recall) against primary sources where possible (Cornell LII, eCFR, nar.realtor, official Keller Williams materials, HUD-adjacent nonprofit summaries citing the Federal Register). Case-law citations were searched by exact name/circuit/year in multiple phrasings; absence from search results is treated as UNCONFIRMED, not as proof of non-existence — per repair-fleet protocol, a claim that a source is *absent* is itself a provenance claim, so this ledger states what was searched and found, not that the cases "don't exist." Broker/legal counsel should independently confirm the four UNCONFIRMED citations before they are used in any client-facing defensibility statement.
