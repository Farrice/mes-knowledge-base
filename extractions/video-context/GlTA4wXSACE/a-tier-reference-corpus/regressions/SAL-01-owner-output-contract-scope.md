# Regression Fixture SAL-01: Narrow Request Must Not Silently Break the Selected Owner Contract

## Replay Evidence

Replay: `replays/SAL-01-pass-1.md`

The receipt selected `story-driven-sales-conversion-funnel`, then said:

> Scope override: The selected owner can produce a broader funnel, but this execution was limited to the requested 650–900 word landing-page core. No email sequence was produced.

At replay time, that owner's shipped Output Contract required a sales page, a 5–7 email sequence, and pattern architecture. The asset was useful, but the claimed owner execution did not satisfy its own contract.

## Failure Class

- **Rubric:** domain fitness and practitioner usefulness.
- **Router gate:** the final asset must satisfy the selected owner's own Quality Gate.
- **Failure:** exact requested scope and existing owner contract had no explicit subset rule, so the worker silently overrode the owner.

## Expected Behavior

When `/shaan-story-deploy` passes an exact bounded deliverable such as one landing-page core, the existing sales owner may return that requested subset only when its workflow and prompt explicitly authorize bounded subset execution. The receipt must say which subset ran and must not claim the omitted funnel components were executed.

## Smallest Existing Owner

`story-driven-sales-conversion-funnel` workflow and exact v2 prompt.

## Preservation Lock

- Keep `FULL STORY | STORY FRAGMENT | NO STORY` unchanged.
- Keep one body owner.
- Add no route, expert, domain adapter, or second writer.
- Preserve the full-funnel contract when a full funnel is requested.
- Change only the existing owner's handling of a router-supplied narrow exit condition.

## Status

- Initial replay: `REPAIR`.
- Repair: existing sales owner now explicitly supports an exact router-supplied subset while preserving its full-funnel default.
- Bounded replay: `replays/SAL-01-repair-1.md` declared the landing-page subset and all omitted default components.
- Final status: `REPAIRED`.
