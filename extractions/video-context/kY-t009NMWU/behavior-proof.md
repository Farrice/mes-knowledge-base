# Behavior Proof — Reverse-Funnel Diagnosis

## Input tested

Four named cases supplied by the user, a missing-data negative control, and a repair-order control in `fixtures/audit-cases.json`.

## Weakness diagnosed

Generic Instagram advisors default to reach tactics, conflate views with demand, and call low distribution a shadowban without proving recommendation eligibility.

## Source mechanics used

One-job layers, offer-first gate, non-follower attraction check, cold-profile scan, embodied trust audit, offer visibility, compliance-first restricted-category handling, and one-link monetization.

## Output produced

The deterministic verifier requires distinct expected routes:

- Greta → `OFFER`
- Kiara → `OFFER` primary, with Trust retained as the next dependency
- Byron → `COMPLIANCE`
- German finance → `MONETIZATION`
- missing telemetry → `UNVERIFIED`
- clear offer/profile + voiceless trust + weak monetization → `TRUST` before Monetization

## Behavior delta

The system does not prescribe more content for high-reach/no-revenue cases, does not claim a shadowban for the health case, and does not invent a bottleneck when required telemetry is absent.

## Validation run

`python3 execution/verify_heydominik_instagram_growth_os.py`

## Remaining risk

Exact case figures remain user-supplied/source-reported unless timestamp-retained in the ledger. Live field performance is `UNTESTED / NO EVENT`.
