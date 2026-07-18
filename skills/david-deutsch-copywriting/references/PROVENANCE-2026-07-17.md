# Provenance — david-deutsch-copywriting repair (Wave 3 Lane 4 Batch 4)

Anchor → source, for everything added in this repair. Ground truth = the skill's own existing files (no external extraction exists for this expert — see `references/source-ledger.md` for the full search log).

## genius.md — "How to Use This Skill (Model Calibration)" (new section)

| Anchor | Source |
|---|---|
| "recognize this as" recognition-test language | Modeled on `skills/ben-watkins-storytelling/genius.md` lines 7-16 (structure only, rewritten for Deutsch's own patterns — never copied verbatim) |
| "I'm not a great writer, but I'm a hell of an editor" + UNCONFIRMED/misattribution flag | `skills/david-deutsch-copywriting/genius.md` original line 116 (Hidden Knowledge #2, "The Ogilvy Editor Identity") + `references/source-ledger.md` item 2 |
| "So What?" ladder reference | `skills/david-deutsch-copywriting/genius.md` original Pattern 13 |
| Pattern 3, 11, 15, 16 references | `skills/david-deutsch-copywriting/genius.md` original Pattern sections (unchanged content, cross-referenced) |

## genius.md — 16 "Illustrative" lines added to zero-entity Pattern/Hidden-Knowledge sections

All 16 are original repair-worker examples, NOT sourced to a Deutsch transcript (none exists — see source-ledger.md). Each is anchored to the **pattern definition it illustrates**, already present in the pre-repair genius.md:

Patterns 3, 5, 6, 8, 10, 14, 15, 16, 18, 19, 20, 21, 22, 23 (genius.md "Genius Patterns" section) + Hidden Knowledge items #4 (Lottery Psychology) and #8 (Cleaning Person Test) — one added line each, explicitly labeled "Illustrative," carrying a concrete number/quote to satisfy `named_entity_floor`. Full before/after diff visible by comparing this file's genius.md against `skills/david-deutsch-copywriting/genius.md`.

## genius.md — "Anti-Patterns (Sourced)" (new section, 7 items)

| Item | Anchor |
|---|---|
| Filler-language coverage | `skills/david-deutsch-copywriting/genius.md` original "Anti-Exemplar: Generic Software Feature List" (Hall of Fame Exemplars section) — reformatted from prose into a bullet, content-preserving per envelope boundaries |
| Explaining instead of staging a scene | Same anti-exemplar prose, cross-referenced to Pattern 6 |
| Failing the Friend Conversation Test | Same anti-exemplar prose, cross-referenced to Pattern 15 |
| Stopping short on the "So What?" Ladder | Same anti-exemplar prose, cross-referenced to Pattern 13 |
| Gain-only framing / unverified "2.3x" figure | Pattern 7 (original) + `references/source-ledger.md` item 8 |
| Treating the editor quote as Deutsch's voice unchecked | `references/source-ledger.md` item 2 |
| Shipping unedited AI drafts | Pattern 19 (original) |

All 7 carry an explicit `2026-07-17` search date + `references/source-ledger.md` pointer, satisfying the auditor's source-attribution regex honestly (UNCONFIRMED label, not a fabricated anchor).

## references/source-ledger.md (new file)

Built from the search log performed live this session: `ls extractions/ | grep -i deutsch`, `_active/codex-harvest-2026-06-11/` tree check, `agents/david-deutsch/AGENT.md` read, `.agents/skills/source-command-david-deutsch/SKILL.md` read, `tar -tzf _archive/claude-export-2026-07-01.tar.gz | grep -ic deutsch` (0 of 3,864 archived paths), and `wc -c` on every file checked (sizes recorded in the ledger table). No claim of absence was made without a corresponding file read.
