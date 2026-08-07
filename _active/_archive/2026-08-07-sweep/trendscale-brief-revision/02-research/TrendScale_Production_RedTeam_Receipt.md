# TrendScale Production Red-Team Receipt

Date: 2026-06-29

## Workflow Stack Used

- `/recommend`: routed the work as solution-aware, revenue-adjacent client creative.
- `/copy-engine`: owner workflow for ad-script structure and conversion logic.
- Luke Iha copy/proof stack: used for hook/body sequencing, proof adjacency, and claim-to-mechanism fit.
- `/adversarial-review`: used as the red-team frame for client-facing readiness.
- Accuracy-without-clickbait red team: used to narrow claims without flattening curiosity.
- Harry Dry precision audit: used to remove generic, internal, or hard-to-picture phrasing.

## Major Fixes

- Removed internal/revision language from the DOCX bodies, including founder/recruiter-facing notes and "source packet" language.
- Replaced `Client to insert PDP URL` with a client-facing pending-PDP field for each product.
- Removed the `AI UGC` contradiction and aligned cast type with the original assignment: HeyGen narrator plus AI b-roll, not handheld UGC.
- Restored JCKED's original dose/competitor contrast by making `4,000mg vs 500mg` the buying angle without claiming every competitor underdoses.
- Corrected Puravita's proof surface:
  - changed `600+ enzyme reactions` to NIH-backed `300+ enzyme systems`,
  - kept the `less than 1% in serum` proof,
  - used form-dependent absorption as the 12-form rationale,
  - removed Huberman/Attia named-reference copy from the production brief.
- Removed AI/prose tells flagged by local gates: em-dash risk, reveal-pattern cadence, triple-anaphora cadence, generic revision phrasing.

## Claim/Proof Ledger

| Claim | Status | Source/Proof | Brief Decision |
|---|---|---|---|
| L-carnitine plays a role in transporting long-chain fatty acids into mitochondria | Verified | Linus Pauling Institute, Oregon State: L-carnitine transport role in mitochondrial fatty acid oxidation | Kept |
| JCKED provides 4,000mg liquid L-carnitine | Product-claim pending final PDP/label | Product name/source packet says Liquid L-Carnitine 4000mg; final PDP not supplied | Kept with PDP/label confirmation guardrail |
| 500mg products are a dose contrast | Conditional/strategic | Original brief called out competitor underdosing; no universal "most brands" claim used | Kept as contrast, not universal market claim |
| Magnesium supports enzyme systems in the body | Verified | NIH Office of Dietary Supplements: more than 300 enzyme systems | Kept, corrected from 600+ |
| Less than 1% of total magnesium is in blood serum | Verified | NIH Office of Dietary Supplements | Kept |
| Magnesium forms absorb differently | Verified | NIH Office of Dietary Supplements bioavailability/form discussion | Kept |
| Huberman/Attia named recommendations | Usage-risk / not needed | External named-reference use would need clearance and exact sourcing | Removed from production brief |

## Verification Results

- DOCX structure: PASS. Both files preserve the TrendScale template shape and include one expanded script table.
- Internal-language scan: PASS. No `Founder liked`, `recruiter`, `Client to insert`, `source packet`, `AI UGC`, `Huberman`, `Attia`, or `600+` residue.
- Content finish gate: PASS. Clean for em dashes, reveal patterns, triple anaphora, and cheap close.
- Prose classifier: PASS. Clean, AI score 0/10.
- Grounding guard: PASS. No risk signals.

## Remaining Send Risk

- Final PDP URLs were not discoverable in the supplied packet or live search under the provided product names. The briefs now mark PDP as pending instead of inventing links.
- Final launch copy should still be checked against each client label/PDP before ads go live, especially serving size, exact dosage, and brand-approved claims.

## Verdict

SHIP for recruiter/founder review.

The briefs now read as client-facing production briefs, not internal revision notes.
