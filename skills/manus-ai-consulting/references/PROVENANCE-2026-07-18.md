# Provenance — manus-ai-consulting repair (2026-07-18)

Anchor → source file + location, for every new claim added to `genius.md`.

| Anchor (genius.md location) | Source file | Location in source | Verbatim? |
|---|---|---|---|
| Anti-Patterns #1 (specialized sub-agent selling) | `_active/harness/swarm-apex-2026-07-07/research/manus.md` | Line 9, "Agent Loop Mechanics" § | Yes — quote copy-checked against file |
| Anti-Patterns #2 (stripping context/tools mid-task) | `_active/harness/swarm-apex-2026-07-07/research/manus.md` | Lines 13-14, "Context Engineering Specifics" § | Yes |
| Anti-Patterns #3 (scrubbing failed attempts) | `_active/harness/swarm-apex-2026-07-07/research/manus.md` | Line 17, "Context Engineering Specifics" § | Yes |
| Anti-Patterns #4 (scope written once, never re-surfaced) | `_active/harness/swarm-apex-2026-07-07/research/manus.md` | Line 15, "Context Engineering Specifics" § | Yes |
| Anti-Patterns #5 (no spend ceiling on fan-out) | `_active/harness/swarm-apex-2026-07-07/research/manus.md` | Line 28, "Best At / Weaknesses" § | Yes |
| Model Calibration recognition-test line (Peak Ji / general-executor architecture) | `_active/harness/swarm-apex-2026-07-07/research/manus.md` | Line 9 (same Peak Ji quote as Anti-Patterns #1) | Yes |
| Model Calibration section structure/tone | `skills/ben-watkins-storytelling/genius.md` | Lines 7-16 ("How to Use This Skill (Opus Calibration)") | Structural model only, not a quote — new prose written for Manus's actual patterns, not copied |

All five Anti-Patterns quotes were checked by direct `Read` of
`_active/harness/swarm-apex-2026-07-07/research/manus.md` in this session (not
reconstructed from memory or from the audit file). File confirmed
non-empty: `wc -c` = 5,141 bytes.

No claim in this repair cites an `extractions/` file — none exists for
Manus.ai in this repo (`ls extractions/ | grep -i manus` returned no
results, checked this session).

Pre-existing genius.md content (Self-Executing Deliverable Architecture,
Hall of Fame Exemplars, Signature Moves, Quality Rubric) was left
untouched (additive-first boundary) and is labeled UNCONFIRMED in
`references/source-ledger.md` — no source file located for any of it.
