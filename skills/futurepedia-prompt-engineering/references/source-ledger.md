# Source Ledger — futurepedia-prompt-engineering

Claim-by-claim provenance for the repair pass (Wave 3 Lane 4 Batch 6, 2026-07-17). Existing
`prompts/`, `prompts-v2/`, `_legacy-prompts/` files were already source-tagged and are not
re-audited here — this ledger covers only the material touched by this repair.

## Primary source located

`knowledge/extractions/inbox/Claude-🧑🏽_💻💡💎 Futurepedia ! Advance Prompt Engineering ! The Simple 3-Step System to Do Anything with .md`
(399,965 bytes, 9,691 lines — confirmed by direct read, 2026-07-17). This is a Claude-generated
MES 3.0 extraction report dated 2026-01-18, built from a ~12-minute Futurepedia YouTube tutorial
transcript on the "Expert Anchor System." **Important distinction**: this file is the extraction
artifact, not the raw YouTube transcript itself — the original video/transcript is not archived
anywhere in this repo (confirmed: no `extractions/*futurepedia*` directory, no transcript file
found by content grep of `_archive/claude-export-2026-07-01.tar.gz` filenames or `codex-harvest`
tree).

## Labels

- **VERIFIED** — text confirmed verbatim, at the cited line, by direct `Read` of the extraction
  file during this repair (2026-07-17).
- **LIKELY** — the extraction file asserts this reflects the original Futurepedia video content,
  but the primary video/transcript was not independently checked against it.
- **UNCONFIRMED** — no locatable source; flagged, never anchored.

| Claim / quote used in genius.md | Location cited | Label |
|---|---|---|
| "Analyze and identify the core framework... Do not summarize, reconstruct the system." | source file line 165 | VERIFIED (verbatim in extraction file) / LIKELY (as Futurepedia's actual video content) |
| "prevents 'momentum' problems where AI sticks to established directions" | source file line 196 | VERIFIED / LIKELY |
| "its attention splits and it defaults back to generic advice" | source file line 220 | VERIFIED / LIKELY |
| "Know that `<context>` beats wall-of-text every time." | source file line 3759 | VERIFIED / LIKELY |
| "Never mix expert extraction, context gathering, and execution in the same chat. Each gets its own clean session." | source file line 198 | VERIFIED / LIKELY |
| "average of the internet" tendency | source file line 154 | VERIFIED / LIKELY |
| "Summaries lose operational detail. Reconstructions preserve the executable system." | source file line 234 | VERIFIED / LIKELY |
| "Once an AI is mid-response, it's much harder to restructure. It has momentum." | source file line 241 | VERIFIED / LIKELY |
| "looks right and sounds professional" / "execution test" | source file lines 141, 143 | VERIFIED / LIKELY |
| "Ask me a series of questions one by one... Do not move on until I've answered each one." | source file line 187 | VERIFIED / LIKELY |
| Creator of "30+ courses with 1,000+ lessons" (AGENT.md identity claim) | `_active/codex-harvest-2026-06-11/agents/futurepedia/AGENT.md` line 9 | UNCONFIRMED — this figure is asserted by the extraction/agent files but not independently checked against a Futurepedia bio, course catalog, or company page; not used as a new anchor in this repair, flagged for any future pass |

## Not found / explicitly checked absent

- `extractions/` — no `futurepedia*` file exists (checked via `ls extractions/ | grep -i futurepedia`, 2026-07-17).
- `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes, 3,864 archived paths) — no filename
  matches `*futurepedia*` in the tar listing (checked via `tar -tzf`, 2026-07-17). Content-level grep
  across the full uncompressed tarball was not run (cost/time); absence is confirmed at the filename
  level only, not exhaustively at the content level.
- `_active/codex-harvest-2026-06-11/` — contains `agents/futurepedia/AGENT.md` (persona file, no new
  raw source) and `.agents/skills/source-command-futurepedia-prompt/SKILL.md` /
  `.claude/commands/futurepedia*.md` (thin pointer/command files, 8-16 lines each, no additional
  source material beyond what's already reflected in the skill).
