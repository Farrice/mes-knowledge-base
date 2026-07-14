---
description: "Phase 2 engine — strip raw community text to signal while keeping every word intact (verbatim, no paraphrase), source-tag every line, and enforce the Verbatim-Integrity Gate that discards any line not found as a substring of its source chunk. Outputs one running list of real, signal-rich, source-tagged sentences"
---

# /ctm-clean

Clean the noise into signal. Raw community text is mostly noise — strip it to signal while keeping the original wording untouched, tag every surviving line, and run the Verbatim-Integrity Gate so nothing paraphrased, summarized, or grammar-fixed survives. The raw, ungrammatical phrasing IS the asset.

## Trigger
`/ctm-clean`

## Workflow
`skills/customer-truth-map/workflows/ctm-clean.md`

## Quick Use
Provide the raw corpus from `/ctm-gather`, chunked to ~a few thousand words. Runs prompt P3 (verbatim extraction) one chunk at a time. Cleaning removes noise, never polishes language.

## Pipeline
1 Run P3 on a chunk (3 rules: word-for-word, drop noise, bracket for sense) → 2 Source-tag every line → 3 Verbatim-Integrity Gate (substring check; discard + re-issue rule on drift) → 4 Append to one running list, advance chunk

## Output
One running list of cleaned, verbatim, source-tagged sentences + a gate log (kept vs discarded with reasons, re-issue count) + DO-workaround pre-flags + a one-line honesty confirmation. Hands to `/ctm-map`.

## Stacks With
→ upstream `/ctm-gather`, downstream `/ctm-map`
→ owns rubric criterion 1 (Verbatim Integrity — the veto)
