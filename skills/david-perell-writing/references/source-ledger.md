# Source Ledger — David Perell Writing (POP)

Claim-by-claim provenance for `skills/david-perell-writing/`. Labels: **VERIFIED** (primary source file in repo, quote confirmed verbatim) / **LIKELY** (well-documented public fact/quote, not re-verified against a live source in this repair pass) / **UNCONFIRMED** (no primary-source file exists in the repo to check against).

## Absence check performed (repair pass, 2026-07-17)

Before labeling anything "no source exists," the following were actually searched and read:

| Location searched | Method | Result |
|---|---|---|
| `extractions/` (193 entries) | `ls extractions/` | No `perell` entry |
| `_active/codex-harvest-2026-06-11/extractions/` (27 entries) | `ls` + `grep -rli perell` on whole harvest tree | No `perell` entry; zero hits anywhere in tree |
| `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes, ~332MB) | `tar -tzf ... \| grep -i perell` over the **full** archive listing | Zero path matches |
| `agents/david-perell/AGENT.md`, `agents/david-perell/memory/context.md` | Read in full | Derived persona files, not raw source; `context.md` is an unpopulated stub ("To be populated") — no extraction content |
| `.claude/worktrees/w3-lane3-repair-execution/skills/david-perell-writing/` | `find` | Sibling worktree copy of the same skill (no additional source material — same genius.md content) |

**Conclusion as of 2026-07-17: no raw transcript, interview, podcast, or chat-export file for David Perell existed anywhere in this repo.** `SKILL.md` frontmatter claimed `source: claude.ai export 2026-07-01`, but that export session was never preserved as a file — only its distilled output survived. This was a genuine, verified absence at that date, not an unread gap.

## Addendum — new evidence lane captured 2026-08-04

A later forge captured `extractions/david-perell-nathan-barry-2026/transcript-speaker-timestamped.txt` from `QsHm_0MEhX8`, SHA-256 `474df0c2c343e6e456223b78555f35598f6ced26e69d6848fc4f6aca910813b6`. It contains 20,537 speaker-labeled words from David Perell's 2026 interview with Nathan Barry.

This does not make the earlier absence finding false; it records a new source acquired later. The new interview supports the Idea-to-Culture mechanics in `claims-ledger-QsHm_0MEhX8.md`. It does **not** verify POP, the Sizzle Spectrum, the highlight test, or the Buffett compression ladder, so the older labels below remain unchanged.

## Claims and labels

| Claim / quote | Where used | Label | Basis |
|---|---|---|---|
| POP = Personal, Observational, Playful framework attributed to Perell | SKILL.md, genius.md throughout | UNCONFIRMED (framework attribution) | No primary transcript to confirm Perell's exact wording/session; internally consistent across all skill files, treated as the skill's own settled ground truth per envelope instructions (verbatim quotes already inside skill files are usable ground truth) |
| DFW loneliness passage ("I'm pretty lonely most of the time," "my name's Dave and I live in a one by one box of bone") | Pattern: POP Writing, Pattern: The Playful Pillar | LIKELY | Consistent with David Foster Wallace's well-documented public voice/interviews; not independently re-verified via live source in this pass |
| Buffett 2001 Berkshire shareholder letter opener ("My grandfather Ernest never went to business school...") | Pattern: The Personal Pillar | LIKELY | Buffett's shareholder letters are public record and this framing is widely cited; not independently re-verified via live source in this pass |
| Buffett "swimming naked" line | Pattern: Clear, Then Memorable | LIKELY | Famous, widely-cited public Buffett line; not independently re-verified via live source in this pass |
| Howard Marks skill-vs-luck quote (33 words) | Pattern: Clear, Then Memorable | LIKELY | Consistent with Marks's publicly documented investment-writing style; not independently re-verified via live source in this pass |
| "countenanced" / SAT-word example | Pattern: The Playful Pillar, Anti-Patterns | UNCONFIRMED (exact session) | Verbatim within genius.md itself (file+section anchor confirmed); no primary transcript to confirm this was Perell's literal wording vs. paraphrase in the original claude.ai session |
| "I shy away from writing about myself... I've learned that about myself" (Perell's self-diagnosed weak pillar) | Pattern: The Highlight Test, Insight: Your Weak Pillar Is Usually Personal | UNCONFIRMED (exact session) | Verbatim within genius.md; no primary transcript to confirm exact original phrasing |
| "Information is not enough. You also need to connect." | Insight: Connection Is the X-Factor | UNCONFIRMED (exact session) | Verbatim within genius.md; no primary transcript to confirm exact original phrasing |
| Google Doc Mode description ("dry academic research paper mode") | Insight: Google Doc Mode Is the Silent Killer | UNCONFIRMED (exact session) | Verbatim within genius.md; no primary transcript to confirm exact original phrasing |
| "you don't need all three [pillars] in order" | Insight: The Pillars Don't Need Order or Equal Weight | UNCONFIRMED (exact session) | Verbatim within genius.md; no primary transcript to confirm exact original phrasing |
| Perell's public profile facts (430k Twitter followers, founder of Write of Passage, host of How I Write, interviewed Andreessen/Housel/Marks) | SKILL.md, AGENT.md | LIKELY | Public-record biographical facts, not independently re-verified via live source in this pass |
| Workflow files (`01-diagnose-and-rebalance.md`, `02-compress-to-memorable.md`, `03-draft-pop-first.md`) | Not modified this pass | N/A | Already passing `workflow_contracts`; untouched, no new claims introduced |

## What this repair pass did NOT do

- Did not run a live web search to independently re-verify the Buffett/Marks/Wallace public quotes — flagged LIKELY rather than VERIFIED, honestly, rather than claiming verification that didn't happen.
- Did not fabricate a transcript file, episode name, or timestamp that doesn't exist in the repo.
- Did not delete or alter any of the original genius.md pattern content — additive only (Model Calibration section + Anti-Patterns section).
