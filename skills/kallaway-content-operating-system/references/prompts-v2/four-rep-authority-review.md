---
name: Kallaway Content OS — Four-Rep Authority Review
source_prompt: born-v2
skill: kallaway-content-operating-system
standard: structure-pure-v2
forged: born-v2
refactored: 2026-08-29
---

## Role & Activation

You are reviewing a completed or partially completed authority portfolio. Four fair executions per core bucket are the minimum evidence floor, not an automatic kill timer. Protect high-value authority signals from vanity-metric decisions and protect the system from endless “needs more data” avoidance.

## Input Required

- Authority job: [ ]
- Positioning contrast: [ ]
- Precommitted bucket jobs and thresholds: [PLAN]
- Post-level results: [RESULTS]
- Qualitative buyer/viewer signals: [SIGNALS]
- Commercial actions: [CALLS / PROPOSALS / DEPOSITS / SALES]
- Confounders or execution failures: [CONFOUNDERS]
- Replacement candidates: [QUEUE]

## Execution Protocol

1. Count fair, meaningfully different executions per bucket.
2. If a core bucket has fewer than four, return `CONTINUE` unless a factual, safety, privacy, or permission veto applies.
3. Separate reach, fit, trust, and commercial action.
4. Judge each bucket by its declared job and precommitted threshold.
5. Inspect countervailing evidence: low reach with strong buyer action; high reach with poor fit; execution or distribution confounders.
6. For narrow authority content, inspect authority-transfer evidence: did qualified readers repeat, save, reference, or apply the new decision rule to another example? Treat absence as a depth diagnosis, not automatic proof of failure.
7. Return `KEEP`, `MODIFY`, `KILL`, or `INCONCLUSIVE` for each bucket after the floor.
8. Promote a chaos candidate only after four fair reps and enough evidence to enter a core role.
9. Specify the exact change to the next batch and write one decision-log row per change.

## Output Contract

- Evidence-floor audit by bucket
- Reach/fit/trust/commercial evidence table
- One decision per bucket with controlling evidence and uncertainty
- Chaos promotion or continuation decision
- Exact next-batch changes
- Decision-log rows
- Remaining instrumentation gap

## Output Skeleton

```markdown
# Four-Rep Authority Review

## Evidence Floor
| Bucket | Fair reps | Floor met? | Confounder |
|---|---:|---|---|
| [ ] | [ ] | [ ] | [ ] |

## Evidence by Job
| Bucket | Reach | Fit | Trust | Commercial action | Controlling evidence |
|---|---|---|---|---|---|
| [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

## Decisions
### [Bucket]: [KEEP / MODIFY / KILL / INCONCLUSIVE / CONTINUE]
- Reason: [ ]
- Counterevidence: [ ]
- Unknown: [ ]
- Next-batch change: [ ]

## Chaos Decision
[ ]

## Decision Log
| Date | Bucket | Decision | Evidence | Change |
|---|---|---|---|---|
| [ ] | [ ] | [ ] | [ ] | [ ] |

## Instrumentation Gap
[ ]
```

## Quality Gate

- Did every core bucket receive at least four fair reps before an ordinary performance verdict?
- Is each bucket judged by its own job rather than a universal reach metric?
- Does high reach with poor fit avoid a false win?
- Does low reach with strong trust or commercial action avoid a false loss?
- Does narrow content show evidence of a perspective shift being remembered or applied?
- Is chaos held to the same four-rep floor before promotion?
- Does the review produce exact next-batch changes rather than commentary?

## Deploy When

Use after a 3-2-1 batch has results, when the operator must decide what to keep, modify, kill, continue, or hold as inconclusive.
