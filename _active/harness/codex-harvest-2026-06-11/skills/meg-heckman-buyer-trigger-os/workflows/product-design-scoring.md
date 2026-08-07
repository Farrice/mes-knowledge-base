---
description: Score buyer-trigger strength and decide whether a product/design should ship, revise, or die before testing.
---

# Product Design Scoring

## Source-Trace Requirement

Before scoring, load `references/source-ledger.md` and `references/genius-patterns.md`, name the source timestamp anchors used, and separate `Source Mechanics` from `Domain Extrapolation`.

If the request includes `--research`, current buyer insights, trends, social listening, purchase intent research, competitor evidence, or market claims, run `workflows/research-backed-trigger-run.md` before scoring. Current-world claims need evidence IDs or source URLs.

## Input

- Product/design candidate.
- Target buyer.
- Intended channel: ad, organic, marketplace, gift, product page, event, client pitch, launch.
- Constraints: printability, brand safety, IP safety, price/margin, production method.

## Scorecard

Score each from 1-5:

| Criterion | Score | Notes |
|---|---:|---|
| Identity Signal |  |  |
| Recognition Speed |  |  |
| Specificity |  |  |
| Social Currency |  |  |
| Familiar/Twist |  |  |
| Emotion First |  |  |
| Product/Print Fit |  |  |
| Original/IP Safety |  |  |

## Verdict Rules

- **Ship/Test:** no score under 3, and identity + recognition + IP safety are 4 or higher.
- **Revise:** one to three scores under 3, with a clear trigger fix.
- **Kill:** identity, recognition, or IP safety fails; or the concept only works after explanation.

## Output

- Trigger scores.
- Verdict.
- One highest-leverage revision.
- Test channel.
- Evidence/proof note.

## Research Guard

- Separate `Source Mechanics`, `Live Evidence Used`, and `Domain Extrapolation`.
- If research status is `DEGRADED`, label the scorecard as research-informed.
- If research status is `FAILED`, do not score against invented market claims; return evidence gaps and source needs.
- Do not claim a score is trend-backed, social-listening-backed, or buyer-language-backed without a source URL.
