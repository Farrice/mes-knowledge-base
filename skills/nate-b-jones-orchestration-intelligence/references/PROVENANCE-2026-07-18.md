# Provenance — nate-b-jones-orchestration-intelligence repair (Wave 3 Lane 4 Batch 12)

Anchor → source file+location table. Full claim-by-claim status lives in `references/source-ledger.md`; this is the quick-index.

| Anchor (genius.md location) | Source file | Location | Status |
|---|---|---|---|
| "How to Use This Skill (Model Calibration)" section (structure only) | `skills/ben-watkins-storytelling/genius.md` | lines 7-16 | n/a (structural model, no factual claim) |
| GP-2 entity-floor sentence ("Planners create tasks. Workers execute them. A judge evaluates results.") | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/a8e9b3ee-cd0e-4fec-8682-20b5a258762d.md` | Yaggi/Cursor two-tier hierarchy paragraph | VERIFIED |
| GP-7 entity-floor sentence ("20 agents ended up producing a 10% output...") | same file | flat-team failure paragraph | VERIFIED |
| GP-9 entity-floor sentence ("Gartner predicts 40%...") | same file | opening stakes paragraph | VERIFIED |
| HK-2 entity-floor sentence (10% output quote, reused) | same file | flat-team failure paragraph | VERIFIED |
| HK-3 entity-floor sentence ("the path is unpredictable, but the outcome is guaranteed") | same file | Yaggi non-deterministic idempotence paragraph | VERIFIED |
| Research Enrichment × 4 subsection additions (Cursor/Anthropic/OpenAI/DeepMind) | same file | multiple paragraphs (two-tier quote, 79% quote, Gas Town pole-cats, Google/MIT 45% finding) | VERIFIED |
| Exemplar 2 entity-floor sentence (cross-ref to Exemplar 1) | internal — this file | Hall of Fame Exemplars section | VERIFIED (internal cross-reference) |
| Exemplar 3 entity-floor sentence (79% quote) | `a8e9b3ee-...md` | failure-cause paragraph | VERIFIED |
| Pattern 14 entity-floor sentence (idempotence quote, reused) | `a8e9b3ee-...md` | Yaggi paragraph | VERIFIED |
| New "Anti-Patterns: Orchestration Framing Failures" section (6 items) | `a8e9b3ee-...md` | 6 distinct paragraphs across the transcript (human-team consensus; scope-creep; tool-catalog contention; drift/continuous-operation; 79% spec/coordination stat; deep-hierarchy drift) | VERIFIED, all re-confirmed independently against raw transcript text |
| Genius Patterns 1-10, Hidden Knowledge 1-7, Methodology (pre-existing, untouched except entity-floor appends) | `extractions/nate-b-jones/smoothing-jagged-frontier-extraction.md` | full file | LIKELY (extraction doc real and dated; raw video transcript not located anywhere in repo despite full-archive search) |
| Genius Patterns 11-13, HK Addendum #8 (pre-existing, untouched) | `a8e9b3ee-cd0e-4fec-8682-20b5a258762d.md` | throughout | VERIFIED — this pass located and confirmed the file that was previously cited by title/date only |
| SKILL.md `source:` field (untouched, not a failing check) | `extractions/nate-b-jones/smoothing-jagged-frontier-extraction.md` | line 6-7 | LIKELY — title attributed there; raw transcript of that specific video not found anywhere in repo |

## Absence searches performed (with evidence, per SOURCE-SEARCH DISCIPLINE)

1. `extractions/` dir listed and read: `ls extractions/ | grep -i jones` → only `nate-b-jones/` (4 files) and `nate-herk/` (unrelated expert). All 4 files in `nate-b-jones/` read in full or grepped; 3 of 4 ruled out by content (Karpathy Loop ×2, TurboQuant/context-engineering — none mention jagged/DPVI/planner-worker-judge/Cursor).
2. `knowledge/extractions/inbox/` JARVIS Protocol file (349,923 bytes) grepped for 5 terms — 2 hits, both irrelevant to this skill.
3. `_archive/claude-export-2026-07-01.tar.gz` — 7,425 conversation members scanned via Python `tarfile` (not extracted to disk) in two passes: first for Pattern 11-14 markers (found `a8e9b3ee-...md`, 51,792-byte tar member / 51,557-byte decoded text), second for the "4 AI Labs..." video's own title/terms (one false-positive hit, read and ruled out; genuine absence confirmed).

No 0-byte or "unrecoverable" claims were made anywhere in this repair — every file referenced above was opened and its size recorded.
