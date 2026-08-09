# Behavior Proof Fixture A — Mature Company With Conflicting Sources

> Synthetic evaluation fixture. None of the rows below are market claims.

## Input

**Company:** AcmeFlow, fictional B2B scheduling software.  
**Decision:** Which churn problem should GTM investigate before repositioning?

| ID | Source | Synthetic record |
|---|---|---|
| A1 | Product events | 31 of 42 churned accounts had fewer than two weekly active coordinators in the final 30 days. |
| A2 | Product events | 23 of those 31 never completed the multi-team schedule setup event. |
| A3 | CRM churn reason | 26 of 42 are labeled `PRICE`. |
| A4 | Cancellation call | “I couldn't get the other department managers to use it, so I was scheduling around them.” |
| A5 | Cancellation call | “The price is hard to justify when half the schedule still lives in a spreadsheet.” |
| A6 | Support tickets | 18 churned accounts asked how to invite or permission other department managers. |
| A7 | Sales claim | “Mid-market buyers churn because procurement pushes back on price.” |
| A8 | Counterexample | 7 high-adoption accounts also complained about price but renewed. |

## Naive baseline

“Price sensitivity is the main churn problem. Target companies with 100–500 employees and emphasize ROI, discounts, and easier procurement.”

## Jordan-system output

### Source coverage

| Source class | Coverage | Limit |
|---|---|---|
| Product actions | 42 churned accounts | No interviews with non-admin users |
| Voice | 2 calls, 18 support-ticket accounts | Small call sample |
| CRM/operator claims | 42 labels, one sales claim | Incentive and shorthand risk |
| Counterexamples | 7 renewals | Renewal cohort size not provided |

### Atomic evidence and reconciliation

| Row | Type | Evidence | Weight | Interpretation link |
|---|---|---|---|---|
| E01 | FACT | A1: 31/42 had fewer than two weekly active coordinators | High | Low cross-team adoption preceded churn |
| E02 | FACT | A2: 23/31 did not complete multi-team setup | High | Setup/adoption friction is plausible |
| E03 | CLAIM | A3: CRM says `PRICE` for 26/42 | Medium-low | Price was recorded, but not necessarily causal |
| E04 | QUOTE | A4, verbatim | Medium | Cross-department non-adoption created workaround burden |
| E05 | QUOTE | A5, verbatim | Medium | Price is evaluated through incomplete adoption |
| E06 | FACT | A6: 18 accounts asked about multi-manager setup | High | Repeated implementation obstacle |
| E07 | CLAIM | A7: sales attributes churn to procurement | Low | Uncorroborated operator explanation |
| E08 | FACT | A8: 7 high-adoption accounts complained about price and renewed | High | Price complaint alone does not predict churn |

### Provisional problem cluster

**Worst current interpretation:** multi-team adoption failure makes the software coexist with spreadsheets, which destroys perceived value and turns price into the stated cancellation reason.

This is an `INFERENCE`, supported by E01, E02, E04, E05, E06, and E08. It is not yet a market-wide causal claim.

### Conflict ledger

- CRM and sales say price/procurement (E03, E07).
- Actions and counterexamples suggest price is conditional on cross-team adoption (E01, E02, E06, E08).
- Preserve both; do not rewrite old churn labels.

### Unknowns

- Whether non-admin managers resisted the product, lacked permissions, or were never invited.
- Whether multi-team setup completion predicts retention after controlling for company size.
- Whether the same pattern appears in non-churned low-adoption accounts.

### Next research action

Interview five churned admin users and five retained low-adoption users about the last scheduling cycle, then compare multi-team setup and weekly-active-coordinator events. Stop if the causal sequence becomes predictable across both groups; otherwise revise the cluster.

## Behavior delta

The baseline converted a CRM label into a demographic ICP and discount message. The system preserved the conflict, elevated behavioral evidence, found a conditional adoption mechanism, protected uncertainty, and moved the next action upstream into causal research.

