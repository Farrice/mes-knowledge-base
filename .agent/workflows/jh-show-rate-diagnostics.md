---
description: Read funnel telemetry as offer alignment signal
skill: jeremy-haynes-cold-offer
tier: foundation
---

# /jh-show-rate-diagnostics — Offer Alignment Telemetry

Read 30-90 days of funnel data (show rate, ROAS, CPC) as offer signals, not individual funnel tuning signals. Diagnoses whether the offer is misaligned (step-function decay all stats) vs. a funnel tuning issue (single metric) vs. audience temperature drift (colder leads arriving).

**Execution**: Read `skills/jeremy-haynes-cold-offer/workflows/jh-show-rate-diagnostics.md` and follow. Load execution prompt at `skills/jeremy-haynes-cold-offer/references/prompts-v2/offer-alignment-telemetry.md` before beginning.

**Next**: `/jh-offer-audit` (if alignment event detected) or `/jh-objection-mine` (if offer misalignment suspected)
