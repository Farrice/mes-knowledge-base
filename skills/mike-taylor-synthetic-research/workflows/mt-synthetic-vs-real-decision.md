---
description: "/mt-synthetic-vs-real-decision — the research-budget triage: given the '99 questions you can't afford to ask' logic and the $8-12K/weeks-long focus-group cost frame, decide which questions synthetic research answers and which ones deserve real budget. Also routes the research-stack (Gemini/Claude/Deep Research) tool-to-strength sequencing."
---

# Synthetic vs. Real Research Decision

The boundary condition for this entire skill: synthetic panels answer the 99 questions you couldn't otherwise afford to ask, so real research budget goes to the few questions that survive triage — never a replacement for real research on the ones that matter enough to spend on. This workflow makes that triage explicit and sequences which AI tool does which part of the research stack.

## Pre-Flight
Read `skills/mike-taylor-synthetic-research/genius.md` (Pattern 16, Pattern 17, Real-Research Boundary).

> **Pre-Flight Gate**: This workflow decides ROUTING (synthetic vs. real, which tool) — it doesn't generate a panel or a research report itself. It hands off to the other workflows in this skill, or to real research, or to `/buyer-council` for the operational front-door version of this same boundary.

## Input Required
- The list of open questions the operator actually has (as many as exist — the "99 questions" framing assumes there are more than budget allows)
- What real research budget/time actually exists (dollars, weeks, access to real customers)
- Whether this decision involves money, launch timing, or strategic commitment (the stakes test)

## Workflow

### Step 1: Inventory the Questions
List every open question, not just the one that feels most urgent. The "99 questions you can't afford to ask" framing only works if the full inventory exists — triaging one question in isolation loses the budget-allocation logic entirely.

### Step 2: Triage Each Question
For each question, classify:
- **SYNTHETIC-SUFFICIENT**: directional/exploratory, low individual stakes, answerable by a panel workflow in this skill (route to the matching workflow — panel triage, grounding, latent-demand, headline triage)
- **SYNTHETIC-FIRST**: needs a synthetic pass to narrow options or find the angle before real research confirms it (most questions land here)
- **REAL-REQUIRED**: money, launch, or strategic commitment riding on the answer — synthetic output can inform but never substitute (route to real customer interviews, real AB tests, real focus groups)

### Step 3: Apply the Cost Frame
State the real-research alternative cost explicitly for any REAL-REQUIRED question: "$8-12,000, weeks if hurrying, a month or two at normal pace" is Taylor's stated 2025 benchmark (VERIFIED, his framing) — recalibrate for the operator's actual market/vendor rates rather than treating this as a fixed price. The point of naming it is to make the tradeoff (spend real budget vs. spend synthetic-panel time) visible, not to anchor on his exact number.

### Step 4: Sequence the Research Stack
For questions proceeding synthetically, route tools to their demonstrated strength (Pattern 16):
- **Data-grounded one-pager on the audience**: an AI connected to existing internal documentation (Drive/G-Suite-connected tools) — pulls from what the operator already has
- **Content/copy creation from that one-pager**: hand it to a model tuned for content craft
- **Cited, external market-level research**: a deep-research tool that traverses many external sources and shows its methodology (cost breakdowns, market sizing, competitive data)
- **Persona panel work itself**: this skill's workflows (`mt-persona-panel-triage.md`, `mt-persona-grounding.md`, etc.)

### Step 5: Route to Buyer-Council for Fast Operational Runs
If the question at hand is a single artifact needing a fast directional gut-check (not a multi-question research-budget triage), the operational front door is `/buyer-council` TRIAGE mode — it runs this skill's core mechanic (Patterns 1-5) in ~5 minutes with the council/verdict machinery already built. Escalate to `/buyer-council` COUNCIL mode, or to this skill's deeper workflows, based on stakes — never duplicate the council machinery here.

## Content Type Adaptations
| Format | Adaptation |
|---|---|
| Multi-question research-budget planning session | Full workflow, all 5 steps |
| Single artifact, fast gut-check needed | Skip to Step 5 — route directly to `/buyer-council` TRIAGE |
| Ongoing research program (recurring decisions) | Steps 1-2 become a standing triage log, revisited each cycle rather than rebuilt from scratch |
| High-stakes launch decision | Full workflow, with Step 3's real-cost frame made explicit to whoever holds the budget |

## Output Format
```
SYNTHETIC vs REAL RESEARCH DECISION — [context] — [date]

QUESTION INVENTORY: [n] questions listed

TRIAGE
| Question | Classification | Routing |
|---|---|---|
| [q1] | SYNTHETIC-SUFFICIENT | mt-persona-panel-triage.md |
| [q2] | REAL-REQUIRED | real customer interviews, est. [cost/time] |
...

REAL-RESEARCH BUDGET ALLOCATION: [n] questions escalated, estimated cost/time per Step 3

RESEARCH STACK SEQUENCE (for synthetic-track questions)
Audience one-pager: [tool]
Content/copy pass: [tool]
External market research: [tool]
Panel work: [this skill's workflow(s)]

NEXT STEP: [proceed synthetic-track now | schedule real-research track | for a single fast artifact check, route to /buyer-council TRIAGE instead of this full workflow]
```

## Quality Gate
> Review against `genius.md § Quality Rubric` before delivering.
- [ ] Full question inventory exists before triage, not a single question in isolation
- [ ] Every question carries an explicit classification and routing, not just the highest-priority one
- [ ] REAL-REQUIRED questions carry a real-cost frame, recalibrated to the operator's actual market rather than anchored on Taylor's stated number
- [ ] Research-stack tool sequencing matches demonstrated strengths (Pattern 16), not habitual single-tool use
- [ ] Fast single-artifact checks were routed to `/buyer-council` rather than run through this full workflow

## Common Pitfalls
- **Triaging one question instead of the full inventory.** The budget-allocation logic only works with the full list in view.
- **Treating synthetic-sufficient as "never needs real validation."** Most questions are SYNTHETIC-FIRST, not SYNTHETIC-SUFFICIENT — narrow with a panel, confirm before serious spend.
- **Duplicating `/buyer-council`'s machinery here.** This workflow decides ROUTING; the council/verdict/dissent-preservation engine lives in buyer-council, not here.
- **Anchoring on Taylor's exact $8-12K figure as universal.** It's a stated 2025 benchmark from one guest on one show — recalibrate to the real vendor quotes available.

## Pairs With
- `skills/geoff-woods-ai-thought-partner/workflows/17-buyer-council.md` — the fast operational front door for a single artifact; this workflow is for multi-question research-budget planning and tool-stack sequencing, the layer above it.
- `mt-persona-panel-triage.md`, `mt-persona-grounding.md`, `mt-latent-demand-mining.md`, `mt-concept-headline-triage.md` — the synthetic-track workflows this one routes into.
- `mt-distribution-calibration-check.md` — run before any synthetic-track output actually informs the decision.

Execution prompt: `references/prompts-v2/synthetic-vs-real-decision.md`
