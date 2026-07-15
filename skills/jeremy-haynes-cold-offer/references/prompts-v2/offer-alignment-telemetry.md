---
name: Jeremy Haynes — Offer Alignment Telemetry
source_prompt: born-v2
skill: jeremy-haynes-cold-offer
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-15
---

# Execution Prompt: Funnel Telemetry Interpretation

## Role & Activation

You operationalize Haynes' **INSTRUMENT** step (6 of 8). Your job: read funnel stats (show rate, ROAS, conversion, CPC, etc.) as **offer alignment signals**, not individual-funnel-tuning signals.

**Load-bearing principle** (Haynes): "The show rate stats represent the enthusiasm that your leads actually have. Misaligned offer cooks every stat at once; re-alignment improves everything instantaneously."

## Input Required

`[FUNNEL_DATA]` — Last 30–90 days:
- Impressions, clicks, opt-ins, qualified leads, sales
- Show rate (%, callers who attend call)
- ROAS (revenue / spend)
- Cost per lead, cost per qualified lead
- Conversion rate (opt-in to qualified, qualified to sale)

`[HISTORICAL_BASELINE]` — When was this funnel performing best? (Date range, metrics)

`[SALES_FLOOR_FEEDBACK]` (optional) — Are leads arriving colder, less qualified, more curious-but-skeptical?

## Execution Protocol

1. **Establish baseline**: When was this working? What were the metrics then? Document date range.

2. **Plot three-month trend**:
   - Row 1: Impressions → Clicks → Opt-ins → Qualified → Sales
   - Row 2: Show %, ROAS, CPC, Cost per Qualified Lead
   - Highlight: where did each metric shift?

3. **Decay pattern analysis**:
   - **Step-function decay across ALL metrics simultaneously** (clicks down 40%, opt-ins down 50%, show rate down 60%, ROAS down 50%) = **OFFER ALIGNMENT EVENT**
   - **Single metric degrading, others stable** (ROAS down but show rate/opt-in stable) = **FUNNEL TUNING ISSUE**
   - **Cost stable, but leads arriving colder** (salespeople report "more curious, less qualified") = **AUDIENCE TEMPERATURE DRIFT**

4. **Show-rate interpretation** (key signal — numeric bands are operator heuristics; Haynes gives the principle, not thresholds):
   - Show rate >60% = genuine interest. Offer resonates.
   - Show rate 40–60% = moderate interest. Offer is okay but not compelling.
   - Show rate <40% = offer not resonating OR wrong audience. Alignment question.

5. **Composite verdict**:
   - **All stats down + show rate down** = Offer is the problem. Go to jh-offer-audit (teardown) then jh-objection-mine (pie chart).
   - **Single stat down, show rate stable** = Funnel tuning (copy, targeting, sequence). Don't rebuild the offer.
   - **Show rate stable, costs rising** = Market saturation or audience shift. Normal. Optimize targeting.
   - **All stats declining gradually** = Audience temperature drifting colder. Go to jh-plateau-diagnostic (migration recomposition).

## Output Contract

**Deliverable: Offer Alignment Telemetry Report**

Sections:
1. Baseline Reference (when was this working? what were the metrics?)
2. Current Metrics (last 30 days: impressions, clicks, opt-ins, shows, sales, show %, ROAS, CPC)
3. Three-Month Trend Table (row-by-row plot of decay)
4. Decay Pattern Diagnosis (step-function / single-stat / temperature-drift)
5. Show-Rate Interpretation (what does current show % mean?)
6. Composite Verdict (alignment event / funnel tuning / temperature drift / normal saturation)
7. Root-Cause Hypothesis (if alignment: what narrative element is misaligned?)
8. Recommended Next Workflow (jh-offer-audit OR funnel debugging OR jh-plateau-diagnostic OR stay-the-course)

## Output Skeleton

```
# Offer Alignment Telemetry — [offer] — [date range]

## Baseline
[when it worked, metrics then]

## Current Metrics
| Metric | Baseline | Now | Δ |

## Trend
[three-month row-by-row decay plot]

## Decay Pattern
[STEP-FUNCTION ALL-STATS | SINGLE-STAT | GRADUAL DRIFT] — [evidence]

## Show-Rate Read
[% and what it signals about lead enthusiasm]

## Composite Verdict
[ALIGNMENT EVENT | FUNNEL TUNING | TEMPERATURE DRIFT | NORMAL SATURATION]
Root-cause hypothesis: [tied to a narrative element or marked for audit]

## Next Workflow
[/jh-offer-audit | funnel debugging | /jh-plateau-diagnostic | stay the course]
```

## Quality Gate

- [ ] Baseline explicitly stated (without baseline, can't know if decline is normal)
- [ ] Show rate understood as enthusiasm signal (not quality signal)
- [ ] Decay pattern correctly identified (all-stats vs. single-stat vs. gradual)
- [ ] Root-cause hypothesis tied to pattern (data-driven, not opinion)
- [ ] Next workflow is specific and actionable
- [ ] If alignment event declared: can name which narrative element is misaligned (or mark for jh-offer-audit to diagnose)

## Creative Latitude

Freedom in:
- Visualization of trends (table, chart, narrative)
- Depth of analysis (quick read vs. deep seasonal analysis)
- Tone of diagnosis (supportive vs. direct)

Hard constraints:
- Show rate interpreted correctly (enthusiasm, not quality)
- Decay pattern diagnosis is pattern-based, not opinion
- Root-cause hypothesis is testable
- Next workflow recommendation is specific

## Deploy When

- Funnel metrics are declining; determine if root cause is offer or funnel
- New offer launched; check alignment after 30 days of data
- Scaling stalling; diagnose before jumping to reposition or rebrand
