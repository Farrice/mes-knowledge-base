# Workflow 05: Financial Leak Audit

Use this when growth is hiding profit leaks or a company is preparing for diligence.

## Inputs

- Revenue and channel mix.
- Gross margin or CM1 target.
- Trade spend or deduction data.
- 3PL, freight, shipping, and warehouse details.
- Retail or wholesale terms.

## Leak Categories

- Gross-to-net waterfall.
- Trade spend and deductions.
- 3PL costs.
- Shipping collected versus actual shipping.
- Freight and warehouse geography.
- Late delivery or chargeback exposure.
- Margin by SKU and channel.

## Output Schema

- Leakage map: every leak category above addressed with a finding or an explicit "not assessed" flag — silence on a category is not treated as "clean."
- Biggest leak verdict: the single largest leak, named, not a list of equally-weighted issues.
- Enterprise-value impact note: a multiple-adjusted estimate, or explicitly flagged as directional/unverified if the input data cannot support a number.
- Owner and fix path: who owns the fix and the concrete next step.
- Next data request: the specific number or document needed to tighten the estimate.
- Stop condition: the data point that would change the verdict.

## Quality Gate

- Is every leak category (gross-to-net, trade spend, 3PL, shipping, freight/warehouse, chargebacks, SKU/channel margin) addressed, with categories lacking data explicitly marked "not assessed" rather than silently dropped?
- Is the biggest leak verdict a single named leak, not a tie or a list?
- Is the enterprise-value impact stated as a multiple-adjusted estimate, or explicitly flagged as directional/unverified when the input data is thin?
- Does the fix path name an owner, not just a general recommendation?
- Is the stop condition a specific data point, not "keep monitoring"?
