# PROVENANCE — nathan-gotch-ai-seo repair (Wave 3 Lane 4 Batch 12)

Anchor → source file+location table for every new claim/anchor introduced by this repair.

| Anchor (as written in genius.md) | Points to | Verified how |
|---|---|---|
| Every "Anti-Patterns" bullet's `(UNCONFIRMED, no primary Gotch source — see references/source-ledger.md, 2026-07-18)` | `references/source-ledger.md` Absence Verification table | Ledger built from real greps/reads this session: `grep -ril "gotch" extractions/` (0 genuine hits), `find . -iname "*gotch*"` (scaffolding only), `grep -ril "gotchseo" .` (0 hits), full read of `research_outputs/ai_authority_architect_agents/nathan_gotch.md` (unrelated audit, not a Gotch source), `wc -c` on `SKILL.md.old` (2,532 B) and all live skill files |
| Pattern 2 `**Baseline Window**` — "24 hours" | `references/implementation.md:7` "Hour 0-4: Measurement Foundation" | Direct read; Hour 0-4 falls within the first 24 hours of the 24-Hour Quickstart section |
| Pattern 5 `**Build Window**` — "Hour 8-16", "Hour 16-24", "Day 30" | `references/implementation.md:17,22,47` | Direct read of the same file's own section headers |
| Pattern 9 `**Cross-Reference**` — "10+ optimized platforms" | `references/implementation.md:50` Day 30 Benchmark | Direct read |
| Pattern 10 `**Worked Example**` — "Hour 8-16", "20+ AI-assisted content pieces" | `references/implementation.md:17,52` | Direct read |
| Pattern 11 `**Cadence**` — "~90 days", "30-Day Transformation" | `references/implementation.md:40` section header "30-Day Transformation" | Direct read; 3×30=90 is arithmetic, not a new fact |
| Pattern 13 `**Cross-Reference**` — "top 50+ sources" | `genius.md` (pre-existing) Signature Moves § "The AI's Brain Scan" | Same file, pre-existing text, confirmed by read before editing |
| Hidden Knowledge 1 `**Cross-Reference**` — "70%+" | `genius.md` (pre-existing) Pattern 1 Success Metric | Same file, pre-existing text |
| Hidden Knowledge 2 `**Cross-Reference**` — "80%+" | `genius.md` (pre-existing) Pattern 8 Success Metric | Same file, pre-existing text |
| Hidden Knowledge 3 `**Cross-Reference**` — "Hour 8-16", "Hour 16-24" | `references/implementation.md:17,22` | Direct read |
| Hidden Knowledge 6 `**Cross-Reference**` — "~90-day" | Pattern 11 (same file, pre-existing) + arithmetic | Same file |
| Hall of Fame Exemplar 1 & 2 `**Note**` flags | This repair's own addition | No external source — flags the pre-existing exemplars as illustrative composites, which they already were (fictional company names "MedInsight AI," "EcoBuild Pro") |
| "How to Use This Skill (Model Calibration)" section structure | `skills/ben-watkins-storytelling/genius.md` lines 7-16 | Read in full before drafting; content authored fresh for Gotch's retrieval-layer/measurement-first craft, not copied |

No anchor in this table claims a verified Nathan Gotch primary source (transcript, video,
article, interview). Every number used to satisfy `named_entity_floor` was already
present somewhere in the pre-existing skill files before this repair — this repair only
cross-references and labels, it does not introduce new factual claims about Gotch.
