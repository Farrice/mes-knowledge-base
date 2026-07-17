# Workflow: Cadence Audit & Quarterly Offer Refresh

**Produces**: a cadence health report against the contract (short daily / long monthly / offer quarterly) + the next quarter's offer refresh + next month's explainer queue. Run monthly (lightweight) and at each quarter turn (full).

## Load Context

1. Read `../genius.md` (mandatory) — especially patterns 3, 5 and Hidden Knowledge 3, 5.
2. Read the SLL System Map + actual publishing record for the period (platform analytics, content log, or `_active/` content folder).

## Steps

1. **Cadence vs contract**: count actual short posts (target: daily), long-form pieces (target: 1/month), offer age (target: <90 days). Report as shipped/target per layer — no vibes.
2. **Recognition math check**: at current cadence, does a new viewer hit 11 touches inside 90 days? Below-daily = mathematically invisible; say so plainly.
3. **Lane distribution**: tally Pain/Prize/Problem/News usage. Flag lane monoculture (one lane >50%) and missing News multipliers.
4. **Bridge & orphan scan**: any short post without a bridge, any long-form without a form CTA, any form without a LAPS owner = orphan; list them.
5. **Offer refresh** (quarter turn): retire or renew the current offer; select next quarter's from the shelf (rotate type where sensible: Special Offer → P4P → Promotion). New promotion = new end date.
6. **Explainer queue**: pick next month's proof story + gap from the register; queue workflow 03.
7. **Feed the loop**: note which lanes/posts drove form fills (not likes) — weight next batches toward what fills forms.

Output step — Execution prompt: `references/prompts-v2/sll-cadence-audit.md` — honor its Output Contract.

## Output Schema

```
# SLL Cadence Audit — [Business] — [period]
| Layer | Contract | Shipped | Verdict |
Recognition math: [on/off track + arithmetic]
Lane distribution: [P/P/P/N counts + flags]
Orphans: [list or "none"]
## Offer Refresh   (retiring · incoming · end date)
## Next Explainer  (proof story · gap · due date)
## Signal Notes    (what filled forms; lane weighting for next batch)
```

## Quality Gate

- [ ] Counts are from the actual publishing record, not memory
- [ ] Verdicts are per-layer and honest (a missed cadence is named, not softened)
- [ ] Offer age checked; >90 days = refresh mandated this run
- [ ] Orphan list actioned (each gets a fix or a kill)
- [ ] Form fills, not engagement, drive the recommendations
