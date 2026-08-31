# Behavior Proof — Design Gauntlet Cold Start

## Behavior Proof

- **Input tested:** a generic responsive product landing-page fixture with purple gradient, default sans typography, three interchangeable rounded cards, weak hierarchy, and no named evidence bar.
- **Weakness diagnosed:** the old loop could inspect five categories and self-report a score without forcing a recoverable baseline, comparator, viewport evidence, or regression restoration.
- **Source mechanics used:** library cold-start; Theme-Respect Elevate boundary; responsive screenshots; evidence-first checks; Blind Bar verdict; single-gap repair; prior-best comparison; two-round cap; surviving-risk report.
- **Output produced:** `proof/before.html`, `proof/after.html`, viewport screenshots, and `proof/design-gauntlet-result.md`.
- **Behavior delta:** the route now refuses taste PASS without a primary bar and rendered evidence, limits each repair, re-verifies affected checks, and preserves the best artifact.
- **Validation run:** recorded in `proof/design-gauntlet-result.md` after local browser capture and repository verifiers.
- **Remaining risk:** the fixture proves mechanics and visible delta, not Farrice's final taste on a live production deliverable. That remains `UNTESTED`.
