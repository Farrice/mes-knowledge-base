# Held-Out Reference TEC-01

## Expected Behavior

- **Decision:** `NO STORY`.
- **Why:** this is an internal engineering decision and identity-safety requirement; narrative adds latency and risks emotionalizing the incident.
- **Owner:** direct engineering decision-memo owner.
- **Must preserve:** exact collision, current workaround, unbuilt status, proposed identity check, acceptance criteria.
- **Must reject:** dramatic chronology, blame, implementation claims, or a generalized distributed-systems essay.

## Reference Asset

# Decision: make handoff source identity explicit

## Problem

`handoff_store.py save --from-temp` currently discovers the newest `handoff-*.md` in a shared OS temp directory. Recency is not session identity.

On 2026-07-25, Jen Listings wrote a handoff at 10:48. One minute later, the `bc-arsenal-install` closeout consumed that file and saved Jen's body under valid BC frontmatter. The command exited successfully. A later `/resume bc-arsenal-install` could therefore have loaded authoritative-looking context for the wrong task.

## Decision

Add an explicit source-path mode and make it the preferred closeout route:

`handoff_store.py save --from <exact-path> --thread <thread-slug> ...`

If `--from-temp` remains for convenience, it must apply an identity check before recency:

1. Prefer candidates whose basename contains the normalized thread slug.
2. Refuse the save when no candidate matches the thread identity, unless an operator explicitly overrides the mismatch.
3. Print the selected source path prominently.
4. Verify the saved body identity after persistence, not only the destination frontmatter and exit status.

## Current safeguard

Until the guard is implemented:

- read the `from-temp:` line after every save;
- confirm the source basename belongs to the active thread;
- inspect the saved H1/body before treating the handoff as valid;
- if mismatched, make the correct temp handoff unambiguously newest and re-save to the same thread.

This workaround has been used successfully. It does not remove the race.

## Acceptance criteria

- Two temp handoffs from different threads can coexist without cross-selection.
- A thread-mismatched source fails closed or requires an explicit override.
- The confirmation names the exact source file.
- The persisted body identity is verified.
- Re-saving one thread does not alter the sibling thread's stored handoff.
- Existing explicit-path and ordinary single-session behavior remain intact.

## Status

The workaround is documented. The identity guard and explicit `--from` implementation are still unbuilt.

## Reference Receipt

- **Narrative decision:** `NO STORY`.
- **Primary job:** decision support and direct instruction.
- **Selected mechanic:** hierarchy and plain-language compression only.
- **Production owner:** direct engineering memo owner.
- **Truth boundary:** proposal and current behavior remain separate; no implementation or test pass is claimed.
- **Remaining risk:** the shared-temp race remains until code and regression tests are added.
