---
description: "Phase 6 merge — consolidate 2+ maps built from different sources about the same customer into ONE confidence-labeled map that splits Consistent Truths (high-confidence, build core messaging here) from Source-Specific (lower-confidence, hold loosely, name the source)"
---

# /ctm-triangulate

Merge the maps without flattening them — the map's confidence layer. Take 2+ Customer Truth Maps built from different sources about the same customer (e.g. a Reddit map, a review-site map, a sales-call map) and merge them, but split what's consistent across sources (high-confidence) from what showed up in only one (lower-confidence). Every forum has its own culture, loud voices, and blind spots; naive merge over-weights one room's obsessions.

## Trigger
`/ctm-triangulate`

## Workflow
`skills/customer-truth-map/workflows/ctm-triangulate.md`

## Quick Use
Provide 2+ verbatim-clean maps of the same narrow customer, each with distinct named provenance. Set the "most/all" threshold for what counts as Consistent. Runs prompt P10. Never invent a "consensus" quote to bridge sources.

## Pipeline
1 Normalize and stack the sources (P10) → 2 Split CONSISTENT TRUTHS vs SOURCE-SPECIFIC, count sources per pattern → 3 Write the consolidated map + confidence preamble (sources, threshold, per-source bias read)

## Output
The confidence preamble + the consolidated six-category map (each split into Consistent / Source-Specific, every quote tagged) + the build-here shortlist (2–3 highest-confidence patterns for core messaging; Source-Specific patterns flagged as sub-group candidates).

## Stacks With
→ upstream: per-source `/customer-truth-map` BUILD runs · `/ctm-refresh` a thin/stale source first
→ downstream: `/ctm-deepen`, `/ctm-to-copy`, `/ctm-to-content`, `/ctm-to-offer` · fact-verifier for riding claims
