# Source Ledger — expert-assembly-os repair (Wave 3 Lane 4 Batch 5)

Every source consulted while writing `genius.md`, `workflows/assemble.md`, and
`workflows/panel-sync.md`. This skill has no `extractions/` folder — it documents
Farrice's own system, not a third-party expert extraction (confirmed via
`ls extractions/ | grep -i assembl`, zero matches, 2026-07-17).

| Source | Type | Label | Notes |
|---|---|---|---|
| `skills/expert-assembly-os/SKILL.md` (5,154 bytes) | primary, direct read | VERIFIED | All quotes checked verbatim against this file. |
| `skills/expert-assembly-os/references/lineage.md` (8,153 bytes) | primary, direct read | VERIFIED | Design-requirement dates/quotes checked verbatim. |
| `skills/expert-assembly-os/references/persona-synthesis-prompt.md` (7,365 bytes) | primary, direct read | VERIFIED | GROUNDED FORGE Step G4 quote checked verbatim; dated 2026-07-15 in-file. |
| `skills/expert-assembly-os/references/roadmap-schema.md` (5,527 bytes) | primary, direct read | VERIFIED | Labeling Rule quote checked verbatim. |
| `docs/solutions/2026-07-15-expert-assembly-os-hybrid-casting.md` (7,500 bytes) | primary, direct read | VERIFIED | Solution card; Key Decisions Locked list quoted/paraphrased with attribution. |
| `.agent/workflows/assemble.md` (8,162 bytes) | primary, direct read | VERIFIED | Base content preserved verbatim in the mirrored workflow file; Output Contract + Quality Gate are new additions, not sourced from this file. |
| `.agent/workflows/panel-sync.md` (2,565 bytes) | primary, direct read | VERIFIED | Base content preserved verbatim; Output Requirements + Quality Gate are new additions. |
| `git log`/`git show 26adc893f`, `9c8c4d098` | primary, direct read | VERIFIED | Commit dates (2026-07-15, both) and commit-message text quoted directly from `git show`. |
| `/Users/farricecain/.claude/projects/.../memory/project_expert-assembly-os.md` (3,267 bytes) | secondary, direct read | LIKELY | User memory note. Carries the harness's own caveat: "Memories are point-in-time observations, not live state." Quotes reproduced verbatim from the file as read, but the file self-flags as potentially 2 days stale — treated as LIKELY, not VERIFIED, per that caveat. |
| `skills/ben-watkins-storytelling/genius.md` (31,629 bytes), lines 7–16 | structural model, direct read | VERIFIED | Used ONLY as a structural/tonal model for "How to Use This Skill" per the batch's shared instruction — no content borrowed, no claims sourced from it. |
| `skills/adam-enfroy-affiliate-marketing/workflows/platform-niche-matchmaker.md` (6,697 bytes) | structural model, direct read | VERIFIED | Used ONLY as a house-style model for "Output Contract" / "Quality Gate" heading conventions (numbered items, "The X Test" phrasing) — no content borrowed. |
| `execution/skill_auditor.py` | tooling, direct read | VERIFIED | Read to confirm exact regex requirements for each failing check before repairing. |

## UNCONFIRMED / not used

- No claim in the repaired files rests on a source that could not be read directly.
  Nothing in this repair required an UNCONFIRMED label — every anti-pattern and
  quote traces to a file this worker opened and verified verbatim.
