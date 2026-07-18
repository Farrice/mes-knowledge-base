# PROVENANCE — chief-of-staff-os repair

Anchor → source file + location. All sizes are real `wc -c` reads at repair time
(2026-07-17), not estimates.

| Anchor (in genius.md) | Source file | Location / size |
|---|---|---|
| "Compass, never cage" binding, 2026-07-05 | `.agent/handoffs/2026-07-05-cos-launch.md` | "Compass-Never-Cage rule now binding..." (2,826 bytes) |
| Mentor seat added 2026-07-08, "I thought I would be getting more mentorship..." | `.agent/handoffs/2026-07-08-cos-os.md` | quote verbatim (5,123 bytes); cross-referenced against pre-existing genius.md Seat Depth → Mentor |
| "Headless" brief lines corrected 2026-07-08 | `.agent/handoffs/2026-07-08-cos-os.md` | "'headless' brief lines = failure..." (5,123 bytes) |
| "Parked" 3rd correction, 2026-07-11 | `guides/2026-07-13-chief-of-staff-os.md` | "'Parked' means a retrievable shelf, never a gate (binding, 3rd correction 2026-07-11)" (7,685 bytes) |
| Incumbency Rule, 7-0 council vote, 2026-07-01 | `FARRICE-MASTER-CONTEXT.md` | line 101 (18,497 bytes) |
| Board seat staffing table | `.agent/cos/board.md` | seat table (4,707 bytes, gitignored, read directly — structural charter, not personal content) |
| Build-session composite scores + fatigue-mitigation notes | `evolution_store/v2_traces/trace_20260702_202457_chief-of-staff-os.json` | notes field (1,915 bytes) |
| Recognition-test quote reused ("real support or next steps that expand my capabilities") | `.agent/handoffs/2026-07-08-cos-os.md` | same file as Mentor-seat anchor |
| "Their thinking, not your terminology" rule | `skills/chief-of-staff-os/genius.md` (pre-existing, unchanged line) | Voice Rules bullet, line 15 of original file |

## Absence checks (verified, not assumed)

- No `/extractions` source exists for this expert-shaped skill: `ls extractions/ | grep -iE "chief|cos|staff"` returned only `lara-acosta` and `lara-acosta-content-system` — both unrelated. This skill is system infrastructure, not a person extraction; ground truth is the skill's own build history (handoffs, guides, traces), per the ENVELOPE's system-skill guidance.
- `.agent/cos/life-context.md`, `journal/*.md`, `decisions.md` were confirmed present on disk (sizes recorded in `references/source-ledger.md`) but their bodies were deliberately NOT read or quoted — they are gitignored private founder data (family/health), and genius.md's own Hard Rule 5 privacy boundary applies to this repair worker too. No claim in this repair depends on their contents.

## Files changed (full list)

- `genius.md` — added `## How to Use This Skill (Model Calibration)`, `## Recognition Test`, `## Anti-Patterns (Corrected, Dated)`. All prior content preserved verbatim, unedited, unreordered (only insertions).
- `references/source-ledger.md` — new file.
- `workflows/cos-daily.md` — added `## Output Schema` before `## Quality Gate`. All prior content unchanged.
- `workflows/cos-dump.md` — added `## Output Schema` before `## Quality Gate`. All prior content unchanged.
- `workflows/cos-status.md` — added `## Output Schema` before `## Quality Gate`. All prior content unchanged.
- `workflows/cos-weekly.md` — added `## Output Schema` before `## Quality Gate`. All prior content unchanged.
- `SKILL.md` — NOT changed (recognition-test language landed in genius.md instead; SKILL.md's router-facing content was already correct and is left untouched per additive-first/minimal-touch).
- `references/prompts-v2/*.md` (6 files) — NOT changed, out of scope for the failing checks.
