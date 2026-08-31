---
description: "Record and read spend, hook rate, conversion evidence, fatigue, category, persona, and explicit promotion or demotion decisions for Dara creative formats"
---

# `/dara-format-outcome-ledger` — Append-Only Format Learning

Use this after a format test produces a dated observation or an accountable promotion/demotion decision. The deterministic owner is `execution/dara_format_outcome_ledger.py`; this workflow explains the evidence boundary and correct command.

## Pre-Flight Gate

Read:

1. `../references/format-outcome-ledger.md`
2. the relevant test plan or production brief containing cell IDs, metric definitions, thresholds, and control
3. the evidence receipt before recording conversion evidence above `none`

## Input Required

- Event type: performance observation or human decision
- Format ID/label, message ID, campaign/asset IDs
- Category, persona, channel, and funnel stage
- Spend and currency
- Hook numerator, denominator, and exact definition when available
- Conversion event/count/value, attribution window, evidence state, and receipt
- Fatigue state/window/frequency
- Decision, rationale, evidence, and accountable owner when recording a decision

## Execution

1. **Preserve the test cell.** Format, message, persona, category, channel, and funnel stage remain separate fields.
2. **Record the observation.** Use `record`; never estimate a missing metric. Hook rate needs a denominator and definition. Any conversion evidence above `none` needs a path or URL receipt.
3. **Read the scoreboard.** Group by format-category-persona before comparing cross-context performance.
4. **Make decisions explicitly.** Use `decide` for `observe`, `hold`, `promote`, `demote`, or `retire`. The ledger never promotes from hook rate automatically.
5. **Feed learning back.** `/dara-denney-creative-format-intelligence` and `/dara-test-plan` read the scoreboard before the next portfolio or matrix.

Execution prompt: `references/prompts-v2/29-format-outcome-ledger.md` — honor its Output Contract.

## Commands

```bash
python3 execution/dara_format_outcome_ledger.py record [observation fields]
python3 execution/dara_format_outcome_ledger.py decide [decision fields]
python3 execution/dara_format_outcome_ledger.py scoreboard --group-by format-category-persona
python3 execution/dara_format_outcome_ledger.py verify
```

## Decision Rules

- `SOURCE PRIOR` can seed a test but cannot promote a format.
- High hook rate plus weak conversion evidence means the opening may work; it is not a commercial win.
- Conversion counts are comparable only when event definition and attribution window match.
- Fatigue is read inside category × persona × channel context.
- Different messages or personas are different cells even when the format matches.
- Test-plan thresholds govern promotion/demotion. The ledger does not invent universal benchmarks.
- Append a new decision. Never edit or delete an earlier event to make the history look cleaner.

## Output Schema

```markdown
## Dara Format Outcome Readout
- Ledger verification:
- Filters and grouping:
- Spend and weighted hook rate:
- Conversion evidence and receipt strength:
- Fatigue state:
- Latest explicit decision:
- Decision gap or next observation:
```

## Quality Gate

- Spend is non-negative and currency is explicit.
- Hook definition, numerator, and denominator match.
- Conversion evidence has the right receipt strength.
- Category and persona are never omitted from an observation.
- A decision is human-owned and evidence-linked.
- No “winner” language appears without an explicit promotion decision.

## Stop Conditions

- Metric definitions differ -> split the cells or normalize upstream; do not aggregate.
- Conversion receipt is missing -> record `none` or `directional`, not attributed evidence.
- User asks to erase a poor result -> preserve the ledger and append a correction event in a future schema revision.
