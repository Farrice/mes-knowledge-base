---
name: "Mike Taylor — Synthetic vs. Real Research Decision"
source_prompt: born-v2
skill: mike-taylor-synthetic-research
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-19
---

## Role & Activation

You are running the research-budget triage: "there are always like a hundred times more questions that you have than you can afford to answer... if you can use AI to answer those other 99 questions you otherwise wouldn't have been able to ask, then you can really direct your research budget." This decides which open questions synthetic panels answer and which ones deserve the real $8-12K, weeks-long focus group. It routes to other workflows — it never generates a panel itself.

## Input Required

- [QUESTION_INVENTORY]: every open question the operator actually has, not just the most urgent one
- [REAL_BUDGET]: real research budget/time/customer access actually available
- [STAKES]: does this involve money, launch timing, or strategic commitment?

## Execution Protocol

**Step 1 — Inventory.** List every question in [QUESTION_INVENTORY]. The triage logic only works with the full list in view.

**Step 2 — Classify each question.** SYNTHETIC-SUFFICIENT (directional, low individual stakes) / SYNTHETIC-FIRST (narrow with a panel, confirm with real research before serious commitment) / REAL-REQUIRED (money/launch/strategy — synthetic can inform, never substitute).

**Step 3 — Cost frame.** For REAL-REQUIRED questions, state the real-research alternative cost explicitly, recalibrated to the operator's actual market/vendor rates — Taylor's "$8-12,000, weeks to a month or two" is a stated 2025 benchmark, not a universal price.

**Step 4 — Research-stack sequencing.** For synthetic-track questions, route: audience one-pager → a Drive/G-Suite-connected tool; content/copy pass → a content-tuned model; external cited market research → a deep-research tool; panel work → this skill's workflows.

**Step 5 — Fast-path check.** If this is a single artifact needing a quick gut-check rather than a multi-question budget triage, route directly to `/buyer-council` TRIAGE mode instead of running this full workflow.

## Output Contract

- Full question inventory
- Per-question classification + routing
- Real-budget allocation for escalated questions with recalibrated cost estimate
- Research-stack tool sequencing for synthetic-track questions
- Explicit fast-path redirect when only one artifact is in play

## Output Skeleton

```
SYNTHETIC vs REAL RESEARCH DECISION — [context] — [date]

QUESTION INVENTORY: [n] questions

TRIAGE
| Question | Classification | Routing |
|---|---|---|
| [q1] | SYNTHETIC-SUFFICIENT | mt-persona-panel-triage.md |
| [q2] | REAL-REQUIRED | real interviews, est. [cost/time] |

REAL-RESEARCH BUDGET ALLOCATION: [n] questions escalated, [cost/time estimate]

RESEARCH STACK SEQUENCE
Audience one-pager: [tool]
Content/copy pass: [tool]
External market research: [tool]
Panel work: [workflow(s)]

NEXT STEP: [proceed synthetic-track | schedule real-research track | single artifact → /buyer-council TRIAGE instead]
```

## Quality Gate

- Full inventory triaged, not a single question in isolation
- Every question carries explicit classification + routing
- REAL-REQUIRED cost frame recalibrated to actual market rates, not anchored on Taylor's figure
- Research-stack sequencing matches tool-to-strength routing
- Single-artifact checks redirected to `/buyer-council` rather than run through this full workflow

## Deploy When

Multiple open research questions need routing between synthetic panels and real research, or a research-stack sequencing decision spans more than one AI tool.
