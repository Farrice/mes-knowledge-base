# Provenance — alan-aragon-nutrition repair (Wave 3 Batch 2)

Ground-truth source located: no `extractions/` directory matches "aragon" (checked
`ls extractions/ | grep -i aragon` — zero results). The skill's own frontmatter
(`source: "claude.ai export 2026-07-01"`) points at the claude.ai conversation export
instead. Confirmed real, non-empty source material (this satisfies rule #2 of the
envelope — verified via actual file reads and recorded sizes, not asserted absent):

- `_active/claude-export/index.json` lists 5 conversations with "Alan Aragon" in the
  title (ids: `31c83d77-6e5b-4966-9b84-e70a814e446c`, `a68ee5f7-6258-48c7-9469-151c38367620`,
  `1db2cbc6-69fa-4016-a4c6-ed5f052fee69`, `7e474b9e-16d2-4808-b683-13b3aaf1934f`,
  `375a40ce-46f0-43c4-8336-158eed3b6a1b`).
- These are packed inside `_archive/claude-export-2026-07-01.tar.gz` (332,779,255
  bytes) at path `claude-export/normalized/conversations/<id>.md`. Extracted only the
  5 matching files (not the full 333 MB archive) via `tar -xzf ... <specific paths>`
  to `/private/tmp/claude-501/.../scratchpad/aragon-src/`. File sizes confirmed
  non-empty: `a68ee5f7-...md` = 146,833 bytes (3,314 lines), `31c83d77-...md` =
  180,399 bytes, `375a40ce-...md` = 158,489 bytes, `7e474b9e-...md` = 24,898 bytes,
  `1db2cbc6-...md` = 14,160 bytes.
- Every anchor added to `genius.md` in this repair comes from ONE of these files:
  `a68ee5f7-6258-48c7-9469-151c38367620.md` — a Merlin-AI-transcribed YouTube
  interview, title "Fat Burning Expert: The Real Reason You Can't Lose Weight!
  PCOS, Menopause & Stubborn Belly Fat" (youtube.com/watch?v=3C185Gkgg0U),
  conversation `created: 2025-08-25T08:27:38Z`. Speaker attribution to Alan is
  inferable from Q&A structure (interviewer asks a numbered/topic question,
  Alan's answer follows the next `>>` turn marker) — verified by reading the
  question immediately preceding each quoted answer, not assumed.

## Anchor → Source Table (Anti-Patterns Alan Would Reject, genius.md)

| # | Anti-pattern | Source file | Line range (raw transcript) | Timestamp |
|---|---|---|---|---|
| 1 | Ranking meal-timing/distribution above the daily protein total | `a68ee5f7-...md` | 199–227 | ~5:45–6:25 |
| 2 | Defaulting clients to crash diets / aggressive deficits | `a68ee5f7-...md` | 605–615 | ~22:19–22:24 |
| 3 | Prescribing seasonal fasts/detoxes to undo a binge period | `a68ee5f7-...md` | 1990–2010 | ~80:10–80:40 |
| 4 | Treating all artificial sweeteners as equally dangerous | `a68ee5f7-...md` | 2695–2705 | ~110:20–110:39 |
| 5 | Lumping fruit sugar in with added/refined sugar | `a68ee5f7-...md` | 2750–2763, 2825–2831 | ~112:24–112:55, ~115:40 |
| 6 | Citing raw glycemic index without checking glycemic load | `a68ee5f7-...md` | 2799–2812 | ~114:34–115:22 |
| 7 | Assuming zero-carb/strict keto blocks muscle-gain outcomes | `a68ee5f7-...md` | 2155–2166 | ~87:25–87:37 |

All 7 quotes were extracted programmatically (line-range slice + timestamp-prefix
strip, no manual retyping) directly from the file above, then spot-checked against
the raw (unstripped) transcript lines via `grep -n` on the exact phrase before
quoting. No quote in this repair is retyped from memory or training data.

## Existing content NOT touched (already passing, left as-is)

- `references/prompts-v2/*.md` already carry VERIFIED/LIKELY/UNCONFIRMED labels —
  this is what makes `source_ledger` pass; no new ledger file was needed for the
  audit to pass, so none was added (additive-first, minimal-touch — did not want to
  create a second, potentially-drifting source-of-truth file).
- The pre-existing "Never…" clauses scattered across `## Genius Patterns` and
  `## Hidden Knowledge` (7 of them, matched by the auditor's fallback anti-item
  regex before this repair) were left untouched. Once a heading-matched
  `## Anti-Patterns...` section exists, the auditor only counts items inside that
  section — the scattered `Never` clauses no longer factor into the check, but
  they were not deleted (content-preserving).
