# Detached Fixture 3: No Story

**Fixture type:** Synthetic internal API-migration decision memo

**Truth risk:** Ordinary operational facts; all values are invented for the test and labeled synthetic

**Expected decision:** `NO STORY`

## Supplied decision packet

- Decision required: choose migration Option A or Option B by 2026-09-15.
- Three incidents in the current quarter were traced to the legacy authentication gateway.
- The service has consumed 62% of its error budget.
- Owner: Platform Team.
- Option A: phased migration over eight weeks with dual running; lower cutover risk; two additional weeks supporting the legacy gateway.
- Option B: one cutover in four weeks; shorter legacy overlap; higher rollback exposure.
- No cost estimate, customer-impact comparison, or staffing analysis is supplied.

## Router diagnosis

- **Primary job:** Enable an internal decision.
- **Narrative decision:** `NO STORY`
- **Why:** The task is a risk and tradeoff decision. A protagonist, scene, or emotional arc would slow comprehension and imply facts not supplied.
- **Selected Shaan contribution:** Hierarchy and plain-language compression only.
- **Production owner:** Direct decision-memo owner.
- **Rejected routes:** Full story would create narrative theater; a fragment adds no explanatory value beyond the incident count and tradeoffs.

## Final asset

### Decision required: authentication-gateway migration

- **Decision owner:** Platform Team
- **Decision deadline:** 2026-09-15
- **Decision:** Choose Option A or Option B.

#### Current state

- Three incidents in the current quarter were traced to the legacy authentication gateway.
- The service has consumed 62% of its error budget.

#### Options

| Option | Schedule | Advantage | Tradeoff |
|---|---|---|---|
| A: phased migration | Eight weeks with dual running | Lower cutover risk | Two additional weeks supporting the legacy gateway |
| B: single cutover | Four weeks | Shorter legacy overlap | Higher rollback exposure |

#### Decision rule

- Choose A if minimizing cutover risk is the controlling priority.
- Choose B if shortening legacy overlap is the controlling priority and the higher rollback exposure is acceptable.

#### Missing inputs

The supplied packet does not include cost, customer impact, or staffing analysis. It does not support an unconditional recommendation until the decision owner either supplies those comparisons or explicitly chooses the controlling priority.

## Story Deployment Receipt

| Field | Result |
|---|---|
| Narrative decision | `NO STORY` |
| Production owner | Direct decision-memo owner |
| Shaan contribution | Hierarchy and plain-language compression |
| Facts retained | Three incidents; 62% error budget; Platform Team; 2026-09-15; both schedules and tradeoffs |
| Prohibited move | No outage scene, protagonist, dialogue, emotionalized risk, or invented recommendation |
| Truth check | PASS: every operational detail matches the supplied packet |
| Remaining risk | A final recommendation needs the missing comparisons or an explicit priority |

## Observable behavior delta

The transformed output moves the decision, owner, deadline, options, and missing inputs to the surface. It improves attention without using a story.
