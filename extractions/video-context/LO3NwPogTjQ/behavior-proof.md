# Behavior Proof: Transaction-to-Proof Story System

These controls test behavior, not market performance. The complete source-grounded replay is in [`source-case-replay.md`](source-case-replay.md).

| Control | Input | Required output | Replay result |
|---|---|---|---|
| Complete resolved case | Supported timeline/result, proof, permission | `READY FOR HUMAN REVIEW`, `FULL STORY`, proof carousel, trust lane | `PASS` |
| Active private negotiation | Live deal, leverage risk, no safe-after date | `HOLD / PERMISSION`, `NO STORY`, private capture | `PASS` |
| No real case | Request for viral win, no facts or proof | `HOLD / PROOF NEEDED`, no publishable copy | `PASS` |
| Strong evidence, no movement | Verified checklist, educational job | `NO STORY`, direct explainer | `PASS` |
| High engagement, no business event | Views/likes/saves, no identified conversation | Attention populated, pipeline `NO EVENT` | `PASS` |

## Pass conditions

- The complete case binds results to proof and avoids monocausal claims.
- The active case cannot be sanitized into a victory story.
- The no-case request cannot become fabricated social proof.
- The direct explainer stays direct.
- Attention never becomes a lead without an identified two-way exchange.

## Replay prompt

```text
Run /enrico-proof-story audit on this Case Receipt. Return the publishability verdict, narrative dosage, format decision, proof gaps, prohibited details, CTA lane, and separate attention/pipeline rows. Do not write ready-to-publish content when the result or permission is unresolved.
```

## Current state

- Manual replay on 2026-09-03: `PASS 5/5`
- Full source-case replay: `PASS`
- Blind second-model replay: `UNTESTED` because real subagents were not authorized
- Jen market result: `UNTESTED / NO EVENT`
