# Dara Format Outcome Ledger

## Purpose

The ledger stores what happened after a format recommendation. It keeps source priors, live observations, and human promotion decisions separate so the format system can learn without turning one noisy result into doctrine.

Default path: `.agent/dara-format-outcomes.jsonl`  
Writer and reader: `execution/dara_format_outcome_ledger.py`  
Schema: `dara-format-outcome/v1`

## Two Event Types

### Observation

One dated performance read for a specific format × message × persona × category × channel combination.

Required decision fields include:

- format ID and label;
- category and persona;
- spend and currency;
- hook-rate numerator, denominator, and definition when hook rate is known;
- conversion event, count, value, attribution window, and evidence state;
- evidence receipt for any conversion evidence above `none`;
- fatigue state, observation window, and frequency when available.

### Decision

One explicit human decision: `observe`, `hold`, `promote`, `demote`, or `retire`.

A decision event requires a reason, an evidence path or URL, and the accountable decision owner. The script never infers promotion from hook rate.

## Conversion Evidence Ladder

| State | Meaning |
|---|---|
| `none` | No conversion evidence observed |
| `directional` | Qualified reply, save, or other non-attributed signal |
| `platform-attributed` | Platform reports the named conversion under a stated window |
| `first-party-confirmed` | CRM, checkout, or another first-party system confirms it |
| `revenue-confirmed` | Collected revenue is tied to the conversion receipt |

Do not compare conversion counts without preserving the event definition and attribution window.

## Fatigue States

- `unknown`: insufficient dated evidence
- `fresh`: no material decay signal
- `watch`: early decay or frequency concern
- `fatigued`: precommitted fatigue criterion cleared
- `recovered`: performance recovered after a change or rest period

Fatigue is context-specific. A format may fatigue for one persona or category while remaining viable elsewhere.

## Commands

Record one observation:

```bash
python3 execution/dara_format_outcome_ledger.py record \
  --format-id founder-ad --format-label "Founder's Ad" \
  --source-prior-tier S --campaign-id hp-angle-map --asset-id F01 \
  --message-id unmade-belief --category supplement \
  --persona "translation-burdened founder" --channel linkedin \
  --funnel-stage recognition --spend 100 --currency USD \
  --hook-events 300 --hook-opportunities 1000 \
  --hook-rate-definition "three-second views / impressions" \
  --conversion-event qualified-dm --conversion-count 2 \
  --conversion-evidence-state directional \
  --evidence deliverables/receipts/f01.json \
  --fatigue-state fresh --fatigue-window days-1-3 --frequency 1.2
```

Record a decision:

```bash
python3 execution/dara_format_outcome_ledger.py decide \
  --format-id founder-ad --format-label "Founder's Ad" \
  --source-prior-tier S --campaign-id hp-angle-map --asset-id F01 \
  --message-id unmade-belief --category supplement \
  --persona "translation-burdened founder" --channel linkedin \
  --funnel-stage recognition --decision promote \
  --decision-reason "Cleared the precommitted qualified-response and fatigue gates" \
  --decision-evidence deliverables/receipts/f01-decision.md \
  --decided-by Farrice
```

Read the scoreboard:

```bash
python3 execution/dara_format_outcome_ledger.py scoreboard --group-by format-category-persona
python3 execution/dara_format_outcome_ledger.py verify
```

## Promotion Discipline

- Source tier is a prior, never live evidence.
- High hook rate with weak conversion evidence means the opening works; it does not prove the offer or format converts.
- Compare like with like: same hook definition, channel, category, persona, funnel stage, and attribution window.
- A different message or persona creates a different test cell even when the format label is unchanged.
- Promotion and demotion thresholds come from the test plan. The ledger records them; it does not invent universal thresholds.
- Retain retired and demoted events. Append a new decision rather than editing history.
