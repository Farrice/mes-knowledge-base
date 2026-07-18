# PROVENANCE — jim-oshaughnessy-philosopher-financier repair (2026-07-18)

Anchor → source file+location table. This skill has **no primary-source
transcript** in this repo — see `references/source-ledger.md` for full
claim-by-claim status. This table maps every new source-attribution anchor
added in this repair to the file/verification event it actually points to.

| Anchor text (in genius.md) | Points to | Verified how |
|---|---|---|
| "2026-07-18" repair-date anchors (throughout) | This repair session | Session date; used to timestamp every provenance claim |
| "332,779,255-byte `_archive/claude-export-2026-07-01.tar.gz`" | `_archive/claude-export-2026-07-01.tar.gz` | `wc -c` on the file, output = 332779255 |
| "full-text grep, 0 hits for 'oshaughnessy'" | Same archive | `tar -xzOf _archive/claude-export-2026-07-01.tar.gz \| grep -a -i -c oshaughnessy` → `0`, exit code 1 (no match), full stream read within timeout |
| "10,052-byte AI-generated... memo" (research_outputs file) | `research_outputs/ai_authority_architect_agents/jim_oshaughnessy.md` | `wc -c` = 10052; file read in full, confirmed content is a LinkedIn-ghostwriting market-strategy memo (Blue Ocean framework, Four Horsemen buyer-objection table, positioning matrix) about a third party's business, not a transcript of/interview with O'Shaughnessy |
| "`extractions/` ... 0 hits" | `extractions/` directory | `ls extractions/ \| grep -i oshaughnessy` and `grep -i osh` → no matching filenames |
| "codex-harvest... downstream copies, not an independent source" | `_active/codex-harvest-2026-06-11/agents/jim-oshaughnessy/`, `_active/codex-harvest-2026-06-11/research_outputs/ai_authority_architect_agents/jim_oshaughnessy.md` | `grep -rli oshaughnessy _active/codex-harvest-2026-06-11/`; files inspected are duplicates/mirrors of this repo's own existing agent+skill content, not an independently sourced transcript |
| "What Works on Wall Street" / OSAM / "Infinite Loops" (book, firm, podcast names) | General public knowledge (not an in-repo file) | Labeled LIKELY in `references/source-ledger.md`, not VERIFIED — no in-repo primary source confirms these; they are treated as well-established public record based on general training knowledge, explicitly flagged as unverified-in-repo |
| "a prior worker on an adjacent skill (nba-betting-edge) had already flagged the same absence" | Dispatch-prompt context from this session (nba-betting-edge repair, referenced in this worker's own instructions) | This repair independently re-verified rather than trusting that claim unread — see Sources checked table in `references/source-ledger.md` |
| Evolution Log "1 entry logged... see 2026-04-09 below" | `genius.md` `### 2026-04-09 — Decision Forcing Function` (pre-existing, unmodified) | Read directly from the file; this is the file's own pre-existing content, not a new claim |
| Quality Rubric "67,914 bytes but... malformed" | `skills/jim-oshaughnessy-philosopher-financier/references/quality-rubric.md` | `wc -c` = 67914; `python3` read confirmed the table has only 9 `\|` characters total across an 8-line file — i.e. effectively one repeated/corrupted row, not a real multi-criterion rubric. Flagged, not fixed (out of scope: not one of the six failing heartbeat checks). |

## Explicitly NOT anchored (left UNCONFIRMED)

Per the "one unforgivable failure is invented provenance" rule, the
following pre-existing claims received an UNCONFIRMED status tag rather
than a fabricated anchor, because no source could be found for them:
Barron's Gambit, the $200 Check Imagination Trigger, the Marduk Power Play
Pattern, the 45% Genetic Investment Behavior figure, the Death/Rebirth
Universal Pattern (as O'Shaughnessy-specific), the Gestabo Pass Principle,
and Patterns 2/3/5/7/8/9/10/11/12/13/14/16/17 (13 of 17 numbered patterns).
Full detail in `references/source-ledger.md`.
