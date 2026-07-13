---
name: "YouTube Video Context Analysis — Multi-Video Comparison"
source_prompt: born-v2
skill: youtube-video-context-analysis
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are operating the YouTube Video Context Analysis discipline across multiple videos at once: comparing tutorials, ads, interviews, lectures, or competitor content by their evidence packages, not by memory or impression. The discipline that holds within a single video's ledger — never mixing evidence lanes — extends across videos here: you must not compare visuals from one video against transcript-only evidence from another as if both were equally observed.

## Input Required

- [VIDEO_CONTEXT_PACKAGE_PATHS]: two or more `extractions/video-context/<video-id>/` folders, each already built via `/video-context-ledger`
- [COMPARISON_PURPOSE]: what the comparison is for — competitor pattern-spotting, format study, claim consistency check, creative reference set
- [REVIEW_PARITY_NOTE]: for each video, whether it was run in transcript-only or full-visual mode — this determines what can be honestly compared

## Execution Protocol

1. **Check review parity before comparing anything.** If one video's package has only `observed_spoken` evidence and another has full visual/OCR evidence, flag this at the top of the comparison. A visual pattern found in Video A cannot be honestly compared to Video B's silence on visuals — that is an evidence gap, not a finding that Video B lacks the pattern (Quality Gate, Multi-Video Comparison workflow).
2. **Compare across six axes**, using only rows that exist in each package:
   - **Shared claims** — spoken claims (`observed_spoken`) that recur across videos, verbatim or in substance.
   - **Repeated frameworks** — named methods, models, or structures that appear in more than one video's spoken evidence.
   - **Visual proof patterns** — recurring composition, setting, product-state, or demo choices, drawn only from `observed_visual` rows that were actually reviewed in each package being compared.
   - **On-screen text patterns** — recurring slide structures, UI conventions, or ad-copy patterns from `observed_onscreen_text` rows.
   - **Contradictions** — where videos make claims that conflict with each other, or where one video's visual/OCR evidence would contradict another's spoken claim.
   - **Uncertainty gaps** — where the comparison itself is limited because one or more packages lack a given evidence lane.
3. **Cite the source video and row/timestamp for every comparison point.** A pattern claim with no per-video citation is not admissible.
4. **Do not average or blend contradictory claims into a single "consensus" statement.** List the disagreement and which video said what.
5. **Summarize reuse value.** State what the comparison is actually good for (e.g., "safe to use for format-pattern claims across all three videos; visual-pattern claims are only supported for videos 1 and 2, which had full visual review").

## Output Contract

- A comparison report structured by the six axes, each entry citing source video + row/timestamp.
- An explicit review-parity flag at the top when packages were built at different evidence depths.
- No blended or averaged claims across contradicting videos — disagreements are listed, not resolved by fiat.

## Output Skeleton

```
# Multi-Video Comparison — [purpose]

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

## Quality Gate

- Is review parity stated explicitly before any cross-video pattern claim is made?
- Does every comparison point across all six axes cite a specific video and row/timestamp?
- Are visual or OCR patterns compared only against other packages that actually captured visual/OCR evidence — never against a transcript-only package as if it were equivalent?
- Are contradictions listed as disagreements rather than blended into a false consensus?
- Does the reuse summary state plainly what the comparison does and does not support?

## Deploy When

- Studying a competitor set, a format across multiple creators, or a series of interviews/lectures for recurring patterns.
- Checking claim consistency across multiple videos on the same topic.
- Building a creative reference set from more than one source video.
