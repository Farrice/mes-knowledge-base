# Provenance — darrel-wilson-ai-affiliate repair

Anchor → source file + location. Full claim-by-claim table lives in
`references/source-ledger.md`; this file indexes the specific text added during
this repair pass.

| Anchor (added text) | Location added | Source file + anchor |
|---|---|---|
| "People like to buy, but they just hate being sold to, right?" | genius.md § Operating Philosophy | `extractions/darrel-wilson-affiliate-marketing/transcript.txt` — verbatim |
| "282,000 views... about 3 years ago" (Elegant Themes tutorial) | genius.md § Operating Philosophy | same file — verbatim |
| "$1,000 to Thailand... about 31,000 Thai bots" | genius.md § Pattern 1 | `extractions/darrel-wilson-ai-money/transcript.txt` — verbatim (transcript's own "bots" artifact, flagged `[sic]`) |
| "€30,000, which is about 35,000K"; "December 18th, 2025"; "the 21st of next year" | genius.md § Pattern 4 | same file — verbatim |
| "all you got to do is give them one affiliate link. The AI will actually place the affiliate link on all the buttons" | genius.md § Pattern 8 | same file — verbatim |
| "coin signal" AI crypto-analysis site | genius.md § Pattern 8 | same file — verbatim ("so here's my website coin signal") |
| 7 Anti-Patterns (1-7) | genius.md § Anti-Patterns (new section) | each item cites its own quote + source file inline; see genius.md |
| "Model Calibration" section quotes: "some sucker, I mean a buyer"; "Top 10 Best [Product] Reviews"; "Blogging is dead. Don't do it." | genius.md § How to Use This Skill | `extractions/darrel-wilson-affiliate-marketing/transcript.txt` — first two are original-flavor paraphrase of a real running gag / genre label used throughout this skill (SKILL.md's Key Principles), third is a verbatim quote |
| Recognition-test phrase: "would Darrel Wilson recognize this as a system he'd actually run" | genius.md § How to Use This Skill | Original calibration language modeled on `skills/ben-watkins-storytelling/genius.md` lines 7-16 per envelope instruction — not a Wilson quote, a skill-authoring convention |
| Output Schema fields (all 11 workflow files) | workflows/*.md § Output Schema | Synthesized from each workflow's own pre-existing Execution section content (renamed/restructured, not new facts) — not a provenance claim, see source-ledger.md row 26 |

## Absence Checks (per envelope Rule 2 — sources checked before claiming absence)

- `extractions/` — `ls extractions/ | grep -i darrel` → exactly `darrel-wilson-affiliate-marketing/` (14,540-byte extraction-report.md + 21,929-byte transcript.txt) and `darrel-wilson-ai-money/` (14,562-byte transcript.txt). Both read in full.
- `_active/codex-harvest-2026-06-11/extractions/` — checked, zero Wilson-named entries.
- `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes) — listed via `tar -tzf`, grepped for "darrel", zero matching entries.
- `agents/darrel-wilson/AGENT.md` (cited in SKILL.md Quick Reference) — file not found on disk; recorded as UNCONFIRMED in source-ledger.md row 25, not corrected (SKILL.md was not a failing-check target this pass).
