# PROVENANCE — luke-iha-vsl-leads heartbeat repair

Frontier Wave 3 PoC. Every addition made to `genius.md` and `workflows/lead-reverse-engineer.md` traced to file + section/line. No claim below was invented; where no source could be located, the pre-existing content was flagged (not deleted, not silently kept unlabeled) — see `REPAIR-NOTES.md` and `references/source-ledger.md` for the full breakdown.

## genius.md additions

| Addition | Anchor text used | Source file | Source location |
|---|---|---|---|
| "How to Use This Skill (Model Calibration)" section | New section, modeled on `skills/ben-watkins-storytelling/genius.md` lines 7-16 (structure/format only — content is original to VSL-lead craft) | `skills/ben-watkins-storytelling/genius.md` | lines 7-16 (format template) |
| "$100 million" VSL stat in Core Philosophy | "just one VSSL I did did $100 million" | `extractions/luke-iha/video-1-proof-mechanisms/transcript.txt` | single-block transcript (no internal line breaks in source file) |
| Cross-confirmation of $100M figure | "$100mm" / "Over $100M generated with VSLs" | `extractions/luke-iha/extraction-report.md` | lines 4-5 |
| "3+ unresolved curiosity loops" metric | "Success Metric: Lead ends with 3+ unresolved curiosity loops. Zero mechanism reveals in the lead." | `skills/luke-iha-vsl-leads/references/genius-patterns.md` | line 12 (GP2) |
| Eugene Schwartz 5 awareness stages | "This is from Eugene Schwarz. You have unaware, problem aware, solution aware, product aware, and then most aware." | `extractions/luke-iha/video-3-levels-of-awareness/transcript.txt` | single-block transcript |
| Lead length 2,000-5,000 / 200-500 words | HK3 text verbatim | `skills/luke-iha-vsl-leads/references/hidden-knowledge.md` | lines 7-8 |
| "10+/15" checklist target in Lead Body Phases | "Success Metric: Score 10+/15 on lead checklist." | `skills/luke-iha-vsl-leads/references/genius-patterns.md` | line 24 (GP4) |
| "8-12 fascination bullets" sizing anchor | "Fascination Bullets: 8-12 'you'll also discover...' bullets" | `skills/luke-iha-vsl-leads/workflows/vsl-lead-writer.md` | Phase 6 (pre-existing workflow content, this skill's own file) |
| Traffic Temperature Matrix footnote (hedging quote) | "If you hedge even a little bit, your ad is dead on arrival." | `extractions/luke-iha-hooks/transcript.txt` | single-block transcript |
| Anti-Patterns section — 7 items | See `references/source-ledger.md` VERIFIED-QUOTE/ADJACENT-SOURCE table for full quote-by-quote mapping | `extractions/luke-iha-hooks/transcript.txt`, `extractions/luke-iha/video-1-proof-mechanisms/transcript.txt`, `extractions/luke-iha/video-3-levels-of-awareness/transcript.txt` | see ledger |
| Provenance flags on Viewer State Calibration and Hall of Fame Exemplars | N/A — these are honesty labels on PRE-EXISTING content, not new claims | `references/source-ledger.md` UNCONFIRMED table | — |

## workflows/lead-reverse-engineer.md change

| Change | Detail |
|---|---|
| Heading `## PHASE 8: REWRITE BLUEPRINT` → `## PHASE 8: REWRITE BLUEPRINT (OUTPUT FORMAT)` | Minimal-touch addition of the literal string "OUTPUT FORMAT" to match house style. Confirmed by grepping the other 3 workflow files in this skill dir (`vsl-lead-writer.md` line 91, `fascination-bullet-factory.md` line 64, `micro-lead-generator.md` line 64) — all three use `## OUTPUT FORMAT` as a standalone heading. No other content changed; the Phase 8 body (Rewrite Blueprint code block) is untouched. |

## Files copied unmodified (for audit completeness / output mirroring)

- `workflows/vsl-lead-writer.md`, `workflows/micro-lead-generator.md`, `workflows/fascination-bullet-factory.md` — copied verbatim from `skills/luke-iha-vsl-leads/workflows/` so the audit script sees the full 4-workflow set. No content changes.
- `SKILL.md` was NOT copied into this output directory (not a changed file) — recognition-test language was added to `genius.md` instead, so SKILL.md needs no edit. It was temporarily copied in only during local audit verification and removed afterward.

## Anti-pattern sourcing method

Grepped every available Luke Iha transcript (`extractions/luke-iha*/transcript.txt` across 6 directories, plus 8 video subdirectories under `extractions/luke-iha/`) for `mistake|don't|avoid|never|wrong|polite|dead|flat|random` and cross-context. The VSL-leads source video itself (`extractions/luke-iha/video-5-vsl-leads/`) has no surviving `transcript.txt` — only `extraction-report.md`, which contains zero explicit "don't do this" statements (it's a distilled framework document, not verbatim). All 7 anti-patterns therefore trace to adjacent Luke Iha source videos (hooks, proof mechanisms, unaware ads) that this skill's own SKILL.md explicitly cross-references in its "Skill Stacking" section. This is disclosed, not hidden — see the Anti-Patterns section intro in `genius.md` and the ADJACENT-SOURCE labels in `references/source-ledger.md`.
