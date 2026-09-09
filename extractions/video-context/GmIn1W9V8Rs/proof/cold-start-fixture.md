# Cold-Start Behavior Fixture

## Business Context

- Objective: sell a source-grounded content strategy service to funded health/performance brands.
- Owned corpus: 12 published videos with usable views, relevant-follower, and qualified-lead data.
- Highest available metric: qualified leads.
- Expected state: `HYBRID`.

## Candidate Signals

| Candidate | Niche | Creator Scale | Views | Outlier | Engagement | Qualified Leads | Creator Has a Real Take? |
|---|---|---:|---:|---:|---:|---:|---|
| A: Celebrity morning routine | performance | 4.8M followers | 9.2M | 8.7x | 0.7% | unavailable | no |
| B: Small-brand claim audit | health marketing | 42K followers | 186K | 6.2x | 3.1% | unavailable | yes |
| C: Luxury unboxing cold open | luxury fashion | 310K followers | 1.1M | 7.4x | 4.0% | unavailable | no |
| D: Owned evidence-led teardown | health marketing | first party | 38K | 2.4x | 2.8% | 11 | yes |

## Expected Negative Controls

1. Candidate A must not become topic evidence: celebrity-scale confounder and engagement below 2%.
2. Candidate C may inform format only; its luxury-fashion topic must not enter the health-marketing topic ranking.
3. Competitor views must remain `PUBLIC_PROXY`; the output must not claim they prove leads, demand, or revenue.
4. No creator take supplied means no generated opinion. The field remains an unanswered reaction question.

## Expected Positive Behavior

1. Declare `HYBRID` because the owned corpus contains 12 pieces.
2. Lead ranking with Candidate D's 11 qualified leads (`PRIVATE_OUTCOME`), despite lower views.
3. Retain Candidate B as same-niche, comparable-scale topic evidence.
4. Route Candidate C's cold-open pattern to `FORMAT_ONLY`.
