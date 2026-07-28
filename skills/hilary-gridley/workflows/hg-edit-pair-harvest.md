---
description: Assemble the Column A/B corpus for judgment encoding — locate real before/after pairs (sent-vs-revised, draft-vs-published, generated-vs-corrected, verdict logs) and structure them for pattern mining
---

# hg-edit-pair-harvest — Build the Evidence Base

The pipeline's raw material: real pairs of (what was submitted) × (what the expert made of it). This workflow finds, filters, and structures that corpus. No corpus → no encoding; invented standards are the anti-pattern this whole skill exists to kill.

## Pre-Flight Gate

- Load `skills/hilary-gridley/genius.md` §Crown Jewel step 1.
- Target: ONE artifact class, ONE expert whose judgment is being encoded. Both named before harvesting.

## Skill Acquisition

- `genius.md` §Edit-Pair Rubric Mining
- `references/source-quotes.md` §The pipeline

## Execution

1. **Map the sources.** Where do this expert's edits live?
   - Email: sent folder (their version) vs the draft they received/wrote first
   - Docs: version history / suggested-edits threads (v1 vs approved)
   - Content: draft vs published; revision requests with the eventual accepted version
   - Chat/AI: model generations vs the human-corrected version actually used
   - Verdict logs: felt verdicts, review comments, "this one yes / this one no" decisions (pair = rejected vs accepted sibling)
2. **Pull candidates.** Target 8-12 raw pairs; keep going until ≥5 survive filtering.
3. **Filter.** Keep pairs where the edit expresses TASTE (structure, emphasis, tone, cut/keep, framing). Discard: factual-only corrections, formatting-only, edits by someone other than the target expert, pairs where A and B differ because the *task* changed.
4. **Structure the corpus.** Table with: pair ID · Column A (verbatim) · Column B (verbatim) · edit context (audience, stakes, date). Long artifacts: excerpt the edited spans plus enough surround to read them, note what's elided.
5. **Grade the corpus**: `provenance: strong` (≥5 clean pairs, one expert, one artifact class) / `thin` (3-4, flag it) / `insufficient` (<3 — output becomes a collection brief instead: exactly what to save from the next N pieces of work, where, in what format).
6. **Hand off** to `hg-judgment-encode` with the corpus + grade.

## Content Type Adaptations

| Situation | Harvest move |
|---|---|
| Farrice's own harness | `.agent/sessions/` verdict logs, voice-ratchet history, taste-calibration entries → see `hg-verdict-to-evaluator` for the full bridge |
| Client engagement | Onboarding ask: "forward 10 emails/posts you rewrote before sending" — the request itself teaches the method |
| No history exists | Prospective harvest: collection brief + a 2-week capture habit; OR expert live-edits 5 representative samples in one sitting (fastest corpus builder) |
| Team (multi-expert) | One expert per corpus — never blend editors; blended edits encode nobody's taste |

## Output Requirements

- Deliverable: structured corpus table + provenance grade + (if insufficient) the collection brief.
- Verbatim columns — never paraphrase the edits; paraphrase destroys the signal being mined.
- Execution prompt: `references/prompts-v2/edit-pair-harvest.md`

## Quality Gate

genius.md rubric: standard provenance. Anti-patterns: blended editors, paraphrased pairs, padding with invented examples, proceeding to encoding on `insufficient`.
