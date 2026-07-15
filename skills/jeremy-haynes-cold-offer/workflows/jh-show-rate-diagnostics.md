---
description: Read funnel stats as offer telemetry — show rate, ROAS, conversion — to diagnose alignment vs. tuning problems
routing: core
tier: foundation
aliases:
  - jh-offer-telemetry
  - jh-alignment-event
requires_prior:
  - jh-offer-stack
prerequisite_for:
  - jh-objection-mine
  - jh-plateau-diagnostic
---

# /jh-show-rate-diagnostics — Offer Telemetry & Alignment Events

Step 6 of the 8-step spine: **INSTRUMENT**. Read funnel stats (show rate, ROAS, cost per call, conversion) as a signal of offer alignment, not individual funnel performance. "The show rate stats represent the enthusiasm that your leads actually have."

## Pre-Flight Gate

- **Do you have funnel data?** (last 30 days minimum: impressions, clicks, opt-ins, show rates, ROAS, cost-per-conversion). If no → this is diagnostic-only; mark as PROSPECTIVE.
- **Single stat down or everything?** If only one stat shifted (show rate steady, ROAS declining) → funnel tuning issue. If step-function decay across ALL stats + colder leads = offer alignment event.
- **Offer problem or funnel problem?** Pre-requisite question: Has this funnel been working, then degraded? Or is it new with the offer?

## Skill Acquisition

- `genius.md` — Hidden Knowledge ("offer upstream of funnel"), Step 6 (INSTRUMENT), Section on show rate as enthusiasm proxy
- `references/source-receipts.md` — Load-bearing quote about show rate stats

## Execution

1. **Establish baseline**: What were your best-performing periods? (ROAS, show %, CPC). Document date range and audience temperature (in-market, needs-convinced, or mixed).

2. **Plot the three-month trend**:
   - Impressions → Clicks → Opt-ins → Qualified Leads → Sales
   - Mark ROAS, show rate (%), cost per lead, cost per qualified lead
   - Haynes framework: "The show rate stats represent the enthusiasm that your leads actually have." Low show rate = low interest, not low quality.

3. **Diagnose alignment vs. tuning**:
   - **Step-function decay across all metrics simultaneously** (impressions same, clicks down 40%, opt-ins down 50%, show rate down 60%, ROAS down 50%) = **OFFER ALIGNMENT EVENT**. The offer is not resonating.
   - **Single metric degrading, others stable** (ROAS down but show rate stable) = **FUNNEL TUNING ISSUE**. Copy, targeting, or sequence problem, not offer.
   - **Cost per lead stable, but colder leads arriving** (salespeople report "more curious, less qualified") = **AUDIENCE TEMPERATURE DRIFT**. → `/jh-plateau-diagnostic` migration re-composition.

4. **The show-rate signal**:
   - High show rate (>60%, context-dependent) = buyers are genuinely interested in the offer. Low show rate (<40%) = either wrong audience OR misaligned offer stack.
   - When show rate is low + ROAS is low, the offer is the blocker. Haynes: "Misaligned offer cooks every stat at once; re-alignment improves everything instantaneously."

5. **Verdict**:
   - **Alignment event** → go to `/jh-offer-audit` (what's misaligned?) then `/jh-objection-mine` (what objections are breaking the show rate?).
   - **Tuning issue** → debug copy, targeting, email sequence, landing page headline. Don't rebuild the offer.
   - **Temperature drift** → go to `/jh-plateau-diagnostic` (is in-market pool exhausted? recompose for needs-convinced?).

Execution prompt: references/prompts-v2/offer-alignment-telemetry.md — honor its Output Contract.

## Content-Type Adaptations

| Scenario | Diagnostic Shift |
|----------|------------------|
| **New offer, new audience** | Baseline is "first 30 days." Show rate <40% = stack not resonating to cold traffic. |
| **Existing offer, declining metrics** | Compare pre-decline to post-decline period. Step-function = alignment event. Gradual decline = audience saturation (migration trigger). |
| **A/B tested creatives, same offer** | If creative A shows 50% show rate, creative B shows 30%, the offer is constant. Debug the copy, not the stack. |
| **High-touch sales + cold funnel** | Show rate proxy = "Leads who booked a call." Cost per booked call. Same diagnostic applies. |

## Output Requirements

**Offer Telemetry Diagnostic Report**:
- Baseline metrics (date range, audience state)
- 3-month trend table (impressions, clicks, opt-ins, show %, ROAS, CPC)
- Alignment verdict (step-function decay vs. single metric vs. temperature drift)
- Root cause hypothesis
- Recommended next workflow (`/jh-offer-audit` OR `/jh-objection-mine` OR `/jh-plateau-diagnostic`)

## Quality Gate

- [ ] Baseline explicitly stated (context for how-good-is-good)
- [ ] Show rate understood as enthusiasm signal, not quality signal
- [ ] Decay pattern correctly identified (all stats vs. single stat vs. gradual)
- [ ] Root cause hypothesis aligns with pattern (not opinion, data-driven)
- [ ] Next workflow selected based on verdict, not guesswork

