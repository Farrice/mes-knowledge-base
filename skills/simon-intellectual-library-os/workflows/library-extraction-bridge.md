---
description: "Convert an Antigravity extraction (genius patterns, hidden knowledge, exemplars) into atomized library entries — one pattern, one entry, glanceable and filterable."
---

# Library Extraction Bridge

The connector between EXTRACT (MES 3.0) and ORGANIZE (the library). An extraction report is deep but not glanceable; this atomizes it into entries humans scan and agents filter.

## Pre-Flight Gate
- Load `genius.md` §6-Property Entry Schema.
- Target library must exist (Notion DB1 or file KB). Else run `/library-notion-port` or `/library-kb-design` first.
- Read the SOURCE extraction in full: `extractions/<expert>/extraction-report.md` + `skills/<skill>/genius.md` + references. Bridge from the richest artifact, not from memory.

## Skill Acquisition
Read `genius.md` + `references/kb-schema.md` + the source extraction set.

## Execution
1. **Inventory the atoms**: each genius pattern, each hidden-knowledge insight, each Hall-of-Fame exemplar, each signature move = ONE entry candidate. (A 16-pattern extraction yields ~25-35 entries with hidden knowledge + exemplars.)
2. **Normalize each** to the schema:
   - Title = the pattern/insight name · Type = Pattern/Principle/Case Study/Example
   - Category = the library's lanes (map the expert's domain to existing lanes; propose a new lane only if ≥5 entries need it)
   - Key Insight = the executable behavior in 1-2 sentences (NOT the description — the deployable move)
   - When to Apply = the extraction's "Deploy when" trigger
   - Confidence = Tested (demonstrated in source) / Untested (asserted) / Proven (validated in OUR deployments — check finalize logs)
   - Expert + Source relations · entry body per template (What/Why/How/Examples/Connections)
3. **Cross-link**: connect new entries to existing entries from OTHER experts ("Daniel Priestley says something similar" — the cross-source linking pattern). Minimum: every new entry gets ≥1 link attempt; report undrawable ones.
4. **Register**: expert → Experts DB (rollup picks up entry count); source material → Sources DB.
5. **Honesty pass**: self-reported expert claims (revenue, results) carry their UNCONFIRMED labels INTO the entries — provenance survives the bridge.
6. **Glance check**: filter the library by the new lane/expert — does the expert's thinking read at a glance? Spot-fix the 3 weakest Key Insights.

## Content Type Adaptations
| Source | Adaptation |
|---|---|
| Full forge extraction | All four atom classes; expect 25-35 entries |
| Light /extract | Patterns + crown-jewel prompt premises; 8-15 entries |
| Finalize-log lessons | Type=Pattern, Category=Systems & AI, Confidence=Proven (they happened) |
| Recall cards | Same atom — dedupe against existing entries before creating |

## Output Requirements
Entries created (count by type), cross-links drawn (count + notable cross-expert connections), registries updated, UNCONFIRMED labels preserved, glance-check verdict. List anything from the extraction deliberately NOT bridged and why.

## Quality Gate
`genius.md` §Rubric Atomization + Provenance ≥8: one idea per entry, When-to-Apply on all, confidence honest. §Anti-Patterns: wholesale copying (the mess, ported) and orphan entries (no links attempted).
