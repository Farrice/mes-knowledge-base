---
description: "Phase 3 engine — sort the cleaned, source-tagged list into SAY / THINK / FEEL / DO + PAINS / GAINS (a quote may sit in several), keep original wording, name 2–3 strongest patterns per category, flag vivid/repeated quotes as copy gold, and tag every DO-category workaround ⚠ WORKAROUND. Outputs the saved Customer Truth Map"
---

# /ctm-map

Build the Customer Truth Map — the heart of the system. Sort every cleaned quote into the six categories (Say/Think/Feel/Do + Pains/Gains), keep the original wording, name the strongest patterns, and circle the gold. The structure is the Empathy Map filled only with real, sourced quotes.

## Trigger
`/ctm-map`

## Workflow
`skills/customer-truth-map/workflows/ctm-map.md`

## Quick Use
Provide the gate-passed running list from `/ctm-clean`. Runs prompt P4. Sorting is a move, not an edit — wording stays exactly as cleaned.

## Pipeline
1 Sort into the six categories (P4; dual-coding allowed) → 2 Keep wording + source tags → 3 Name 2–3 patterns per category → 4 Flag ★ COPY GOLD (vivid/repeated) → 5 Tag ⚠ WORKAROUND on every DO DIY fix → 6 Save the dated living document

## Output
The saved Customer Truth Map (all six categories, source-tagged verbatim quotes) + 2–3 named patterns each + ★ COPY GOLD flags + ⚠ WORKAROUND tags + honesty confirmation. Feeds `/ctm-jobs`, `/ctm-gaps`, and the Phase-5 apply layer.

## Stacks With
→ upstream `/ctm-clean`, downstream `/ctm-jobs` `/ctm-gaps` `/ctm-to-*`
→ owns rubric criteria 4 (Map Completeness) + 5 (Do-Category Mining)
