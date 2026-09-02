# SHADOW Routing False-Alarm Audit

## Verdict

The false alarm was real and narrow. A standalone `SHADOW` token was enough for
the fuzzy workflow router to surface `/shadow-market-validation-report` even
when the request concerned a cold system experiment rather than a market.

The workspace-local repair passes and does not touch Signal Fidelity. Leave the
branch unmerged until reviewed with the Signal Fidelity evidence separately.

## What Changed

`/shadow-market-validation-report` now needs actual market-validation context
before fuzzy matching can surface it: market, validation, demand, launch, niche,
aftermath, or MVP language. Explicit bindings and governed ownership remain
authoritative.

## Regression Proof

| Control | Result |
|---|---:|
| Signal Fidelity SHADOW repair | Suppressed from market route |
| Generic SHADOW observation cycle | Suppressed from market route |
| Cold buyer-psychology SHADOW | Suppressed from market route |
| SHADOW marketing experiment | Suppressed from market route |
| Visual light-and-shadow request | Suppressed from market route |
| Real shadow-market requests | 3/3 still rank the market workflow first |

The broader Autopilot routing suite passes. The runtime preflight, skill-system
contract, authority check, subagent boundary, platform lint, and 14-surface
Operator Core snapshot also pass. The control-plane golden routing matrix passed
85 queries before the full verifier reached unrelated global-wrapper failures.

## Honest Remaining Boundaries

Two pre-existing global alignment failures remain outside this workspace-only
repair: stale end-session closeout wording and missing explicit-subagent wording
in global AGENTS. Fixing either requires separate global approval.

An older slash-alias gap also remains: writing the literal
`/shadow-market-validation-report` is not resolved by the generic alias helper.
That defect did not cause this incident, and widening this patch to command
aliasing would violate the smallest-repair boundary.

## Decision

- **Repaired:** ambiguous SHADOW-to-market fuzzy coupling.
- **Preserved:** real shadow-market discovery and all Signal Fidelity state.
- **Not changed:** global wrappers, slash aliases, Signal Fidelity promotion,
  routing ownership outside this one ambiguous workflow, or enforcement.
