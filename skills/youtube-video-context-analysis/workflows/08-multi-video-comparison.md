---
description: "Compare multiple video context ledgers across claims, visuals, OCR, uncertainty, and reusable patterns"
---

# Multi-Video Comparison

Use this when comparing tutorials, ads, interviews, lectures, competitor videos, or creative references.

## Run Order

```bash
/video-context-ledger <youtube-url-1>
/video-context-ledger <youtube-url-2>
```

Then compare the package folders under `extractions/video-context/`.

## Comparison Axes

- Shared claims.
- Repeated frameworks.
- Visual proof patterns.
- On-screen text patterns.
- Contradictions.
- Uncertainty gaps.

## Output Schema

A "Multi-Video Comparison — [purpose]" report, structured by the six comparison axes, each entry citing source video + row/timestamp:

```
## Review Parity
- [video 1 id]: [transcript-only / full visual]
- [video 2 id]: [transcript-only / full visual]
[flag any lane that cannot be honestly compared across all videos]

## Shared Claims
- [claim] — [video 1: row/timestamp] / [video 2: row/timestamp]

## Repeated Frameworks
- [framework/method name] — [video citations]

## Visual Proof Patterns
- [pattern] — [video citations, reviewed frames only]

## On-Screen Text Patterns
- [pattern] — [video citations]

## Contradictions
- [point of disagreement] — [video 1 position, citation] vs [video 2 position, citation]

## Uncertainty Gaps
- [what the comparison could not evaluate, and why]

## Reuse Summary
[what this comparison is safely usable for, and what it is not]
```

Review Parity must be stated before any cross-video pattern claim — a visual pattern found in one video is never compared against another video's transcript-only silence as if that silence were a finding.

## Quality Gate

Do not compare visuals from one video against transcript-only evidence from another as if both are equally observed. Before handoff, confirm: every comparison point across all six axes cites a specific video and row/timestamp, contradictions are listed as disagreements rather than blended into a false consensus, and the Reuse Summary states plainly what the comparison does and does not support.
