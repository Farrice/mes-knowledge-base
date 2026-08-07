# Regression Fixture HLT-01: Evidence-Sensitive Fragments Cannot Invent Narrator Attitude

## Replay Evidence

Replay: `replays/HLT-01-pass-1.md`

The post added:

> That question never sounded silly to me.

The brief supplied that women asked the question during Farrice's five years behind the counter. It did not supply how he judged or felt about the question. The sentence invents a first-person attitude inside an evidence-sensitive asset.

## Failure Class

- **Hard gate:** unsupported motive or emotional state.
- **Rubric:** source fidelity.

## Expected Behavior

Use only the supplied counter fact. Do not add the narrator's reaction, judgment, feeling, memory texture, or internal monologue unless it appears in the fact packet. A story fragment may create recognition through selection and sequence, not invented interiority.

## Smallest Existing Owner

`viral-social-content-engine` workflow and exact v2 prompt.

## Preservation Lock

- Keep the dated metrics, trial design, form/dose distinction, and uncertainty labels primary.
- Keep exactly one fragment.
- Add no health route or evidence source.
- Tighten only the first-person fact-trace rule in evidence-sensitive work.

## Status

- Initial replay: `REPAIR`.
- Repair: the social owner now requires first-person reactions, judgments, feelings, memories, and intentions to trace to the source packet in evidence-sensitive work.
- Bounded replay: `replays/HLT-01-repair-1.md` used only the supplied counter fact and added no narrator interiority.
- Final status: `REPAIRED`.
