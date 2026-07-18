# Andrew Lane — Source Ledger

Claim-by-claim provenance for `skills/andrew-lane-design-systems/`. Ground truth for
this skill is unusually thin: no `extractions/` directory exists for this expert, and
the raw claude.ai conversation transcripts referenced by the agent memory file were
never landed in this repo. That absence was verified with real file reads, not assumed
— see "Absence Verification" below. As a result, nearly every claim below is labeled
UNCONFIRMED at the transcript level; what IS verifiable is that the quotes exist
verbatim inside the skill's own already-shipped files, which is the level this ledger
certifies.

## Absence Verification (run 2026-07-17)

| Check | Method | Result |
|---|---|---|
| `extractions/` directory for this expert | `find extractions -iname "*lane*"` | 0 hits — no extraction directory exists |
| Archived claude.ai export | `tar -tzf _archive/claude-export-2026-07-01.tar.gz` (3,864 entries confirmed readable) then grepped for `lane\|mood.?board\|dude.?woof` | 0 matches — the tarball is real and large but contains nothing Lane-specific |
| Harvest build manifest | `_active/claude-export/harvest/lanes-build-input.json` (18,471 bytes, read in full via Python `json.load`) | No entry with `skill` or `agent` containing "lane" — the file's name ("lanes") refers to build lanes, not Andrew Lane |
| Raw normalized conversations | `.tmp/claude-export/normalized/conversations/` (the path referenced by the harvest manifest) | Directory does not exist (`ls` error: No such file or directory) — the raw transcripts were never persisted past the original ingestion |
| Skill's own file sizes (confirm not 0-byte / not truncated) | `wc -c` on every file in `skills/andrew-lane-design-systems/` | SKILL.md 3,928 B · genius.md 11,365 B · workflows/01 4,436 B · workflows/02 4,036 B · workflows/03 5,078 B · references/prompts-v2/brand-vibe-foundation.md 9,347 B · references/prompts-v2/brand-layer-library.md 7,969 B · references/prompts-v2/business-branding-decision-split.md 8,997 B — all non-empty, all real content |

Conclusion: the two source conversations named in `agents/andrew-lane/memory/context.md`
("How I Build Brands In Minutes With ChatGPT (Mood Board Method)" and "The ChatGPT
Method Makes Branding Fun & Easy") are genuinely absent from this repo. Nothing below
claims otherwise.

## Claims

| Claim | Label | Basis |
|---|---|---|
| Andrew Lane is a professional designer, 15+ years experience, built multiple 7-figure brands, taught thousands of entrepreneurs | UNCONFIRMED | Asserted in SKILL.md:12 and AGENT.md:10 with `source: claude.ai export 2026-07-01` frontmatter but the underlying transcript is absent (see Absence Verification). No independent bio source consulted for this repair — not re-verified externally. |
| "Mood Board Method" name and moodboardmethod.com | UNCONFIRMED | AGENT.md:10 names the domain; not fetched or independently checked as part of this repair (out of scope — envelope grounds this repair in `extractions/` + the skill's own verbatim material, not live web verification). |
| "Do NOT discuss fonts, colors, or logos" | VERIFIED (in-skill) | Verbatim at `workflows/01-build-vibe-foundation.md:23`. Confirmed by direct file read this session. Original-conversation provenance beyond the skill file: UNCONFIRMED. |
| "it just doesn't come out right and I want to have more control" | VERIFIED (in-skill) | Verbatim at `genius.md:51` (pre-existing, unedited by this repair). Confirmed by direct file read. Original-conversation provenance: UNCONFIRMED. |
| "Now go in a completely different direction — show me the opposite style of brand for this." | VERIFIED (in-skill) | Verbatim at `genius.md:22` and `references/prompts-v2/brand-vibe-foundation.md:53`. Confirmed by direct file read; both locations match word-for-word. Original-conversation provenance: UNCONFIRMED. |
| "Assume they cannot see this or any other visual — the description must be clear and easy to follow with no visual inspiration available." | VERIFIED (in-skill) | Verbatim at `references/prompts-v2/brand-vibe-foundation.md:60`. Confirmed by direct file read. Original-conversation provenance: UNCONFIRMED. |
| "branding cannot fix an undecided offer" | VERIFIED (in-skill) | Verbatim at `workflows/03-split-brand-decisions.md:25`. Confirmed by direct file read. Original-conversation provenance: UNCONFIRMED. |
| "No fabricated hex codes, font names, or imagery claims not grounded in [EXISTING BRAND MATERIAL] or the generated mood board" | VERIFIED (in-skill) | Verbatim at `references/prompts-v2/brand-vibe-foundation.md:79`. Confirmed by direct file read. This is itself the v2 prompt's own anti-fabrication rule — self-consistent with this ledger's standard. |
| Dude Woof convergence anecdote (genius.md:73-75, "AI Convergence as Validation") | UNCONFIRMED | Specific narrative detail (founder spent months on an unpublished rebrand that the AI's blind output matched) has no source beyond the absent transcript. "Dude Woof" is left as-is (pre-existing content, not rewritten by this repair) but should be treated as an illustrative claim, not a verified case study, until the source conversation is recovered. |
| All 3 `references/prompts-v2/*.md` execution prompts (Output Contract/Skeleton/Quality Gate) | VERIFIED (in-repo) | `source_prompt: born-v2`, `forged: born-v2`, `refactored: 2026-07-13` frontmatter in each file (confirmed via `grep -n`). These are system-forged deliverable contracts, not expert-attributed quotes — provenance is the repo's own prompt-forging pipeline, not the claude.ai export. |
| The 3 workflow files' procedural content (Phases, Output Contract, Quality Gate) | VERIFIED (in-repo) | Pre-existing content, unedited by this repair; internally consistent with genius.md pattern descriptions and the v2 prompts. Not independently re-verified against a transcript (none exists). |

## What This Repair Changed vs. Left Alone

- **Added** (this repair): `## How to Use This Skill (Model Calibration)` section and `## Anti-Patterns` section in `genius.md`. Every anti-pattern bullet quotes text that was already verbatim in the skill before this repair — no new Lane quotes were invented.
- **Untouched**: SKILL.md, all 3 workflow files, all 3 `references/prompts-v2/*.md` files, and every pre-existing genius.md pattern/insight. This repair is additive-only per the envelope's boundaries.
