# Solution Capture: AI Misfire Copy Gate Recovery

Created: 2026-05-10
Mission: ai-misfire-copy-gate-recovery

Use this while context is fresh. If the learning is generalizable, copy or convert it into `docs/solutions/`.

## Track
- Type: workflow / guardrail

## Symptoms Or Context
- Active AI Misfire artifacts carried Copy Gate Result sections that rated hook, voice, and tension as 9+ even though the user read the copy as generic 3-4/10. The scoring looked authoritative but did not reflect public-performance reality.

## What Did Not Work
- Naming expert routes inside a Copy Gate did not prove the experts' standards were actually applied.
- Passing `prose_classifier.py` did not mean the copy had punch, tension, voice, or buyer-language specificity.
- A strategically correct thesis still produced generic public copy when it opened with ambiguous internal language instead of a scroll-stopping audience hook.

## Working Solution Or Durable Guidance
- Start the next gate from the user's calibration, not the system's confidence.
- Cap scores below 9 unless there is live market/user proof.
- Require a concrete "failure addressed" field that names what changed from the rejected draft.
- Use manual anti-slop review alongside static classifiers.
- Rebuild public copy around the buyer's private moment and one observable proof mechanism.

## Why This Works
- It converts qualitative rejection into a reusable calibration constraint. The system cannot pass by formatting a scorecard; it must show how the new draft changed the failure mode and avoid claiming excellence without external signal.

## Prevention Or Reuse
- `execution/publishable_copy_guard.py` now checks current-intent Copy Gates for user-calibrated baseline, failure addressed, score discipline, classifier-only review, average score inflation, and 9+ scores without proof.

## Generalization Decision
- Keep mission-local: no.
- Promote to `docs/solutions/`: yes, `docs/solutions/copy-gate-score-calibration.md`.
