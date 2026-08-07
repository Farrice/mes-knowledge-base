# PROVENANCE — dr-kriukow-humanization repair (Wave 3, Lane 4, Batch 5)

Anchor → source file + location, for every new claim added in this repair.

| Anchor (where it landed) | Source file | Location | Verbatim confirmed by |
|---|---|---|---|
| genius.md § Anti-Patterns, item 1 (word-swap-only) | `extractions/dr-kriukow/dr-kriukow-humanization-extraction-report.md` | line 126, "Market Signals" | `grep -n` before writing |
| genius.md § Anti-Patterns, item 2 (sentence-by-sentence patching) | same | line 73, "Hidden Knowledge #1" | `grep -n` before writing |
| genius.md § Anti-Patterns, item 3 (one technique as mandatory) | same | line 85, "Hidden Knowledge #5" | `grep -n` before writing |
| genius.md § Anti-Patterns, item 4 (AI list order left intact) | same | line 54, "Genius Pattern 5" | `grep -n` before writing |
| genius.md § Anti-Patterns, item 5 ("too clean" prose) | same | line 76, "Hidden Knowledge #2" | `grep -n` before writing |
| genius.md § Anti-Patterns, item 6 (more word swaps post-flag) | same | line 112, "Methodology Phase 4" | `grep -n` before writing |
| genius.md § How to Use This Skill, "95%+ of AI content deployers..." quote | same | line 126, "Market Signals" | `grep -n` before writing |
| genius.md § How to Use This Skill, recognition-test closing line | Original synthesis, not a quote — grounded in the SUP/structure-first framing that is VERIFIED across Genius Patterns 1-2 (lines 26-36) | — | N/A (not a quote; a calibration instruction built from verified patterns) |
| genius.md, provenance note above "Anti-Exemplar: Superficial Word Swaps" | This repair's own finding: the exemplar text is NOT present in the extraction report | Negative-search confirmed via `grep -n "sustainable practices\|Anti-Exemplar\|Superficial Word Swaps\|Fails Statistical Unpredictability" extractions/dr-kriukow/dr-kriukow-humanization-extraction-report.md` → zero matches | Grep run, zero hits recorded |
| references/source-ledger.md, "Absence Check" table | `_active/harness/codex-harvest-2026-06-11/`, `_archive/claude-export-2026-07-01.tar.gz`, `evolution_store/v2_variants/genius_compressed/` | file sizes recorded via `wc -c`, tarball checked via `tar -tzf \| grep -i kriukow` (zero matches), compressed variant checked via `diff` | Commands run and output recorded in this session; no absence claimed without a command |

## Files NOT modified (out of scope, already passing)
- `skills/dr-kriukow-humanization/SKILL.md` — `recognition_test` fix landed in
  genius.md instead (the check accepts either file); SKILL.md untouched.
- `skills/dr-kriukow-humanization/workflows/*.md` — `workflow_contracts` already PASS
  (both files carry Output Schema + Quality Gate).
- The two pre-existing "Hall of Fame Exemplars" before/after text blocks — flagged for
  provenance (see above) but not deleted or rewritten, per additive-first rule.
