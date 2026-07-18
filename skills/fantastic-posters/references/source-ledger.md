# Source Ledger — fantastic-posters repair (Wave 3 Lane 4 Batch 5, 2026-07-17)

Sources consulted this repair session, each claim-by-claim, per `directives/verification-agent-protocol.md` labeling. `source_ledger` was already PASSING before this repair (`references/prompts-v2/critique-refine-ledger.md` exists and matches the auditor's filename check) — this file is additive documentation of the repair's own grounding, not a replacement.

| Claim used in repair | Source consulted | Label |
|---|---|---|
| v1→v2 "thin brain" diagnosis quote (Anti-Pattern #1) | `skills/fantastic-posters/genius.md` (pre-repair version, read in full) | VERIFIED |
| "shortest prompt... verbose specs make the model drift" (Anti-Pattern #7) | `skills/fantastic-posters/.claude/skills/fantastic-posters/SKILL.md`, "Trust the Reference" section | VERIFIED |
| "2026-05→07 fal-usage.json staleness" root-cause comment (Anti-Pattern #8) | `skills/fantastic-posters/generate.js`, lines 39-60 | VERIFIED |
| "If a title runs more than ~6 words, expect typos" (Anti-Pattern #9) | `skills/fantastic-posters/README.md`, "Settings" section | VERIFIED |
| No `extractions/` source exists for this skill (it's a tool skill, not a person-extraction) | `ls extractions/ \| grep -iE "poster\|fal\|fantastic"` — zero matches | VERIFIED (absence confirmed via actual file-system read, not assumed) |
| Workflow Quality Gate / Output Schema checklist content | Each target workflow file's own pre-existing "Output Requirements," "Execution," "Standard Run," and "Anti-Patterns" sections (self-referential — no external claim introduced) | VERIFIED |
| House style for `## Quality Gate` placement/format | `skills/fantastic-posters/workflows/00-studio.md` (the pre-repair passing sibling workflow) | VERIFIED |
| House style for "How to Use This Skill" section structure | `skills/ben-watkins-storytelling/genius.md`, lines 7-16 (per ENVELOPE instruction) | VERIFIED |

No claim in this repair required an UNCONFIRMED or LIKELY label — every anchor traces to a file this session actually opened and quoted verbatim, confirmed against file size/content before citing (`wc -c` spot-checks below).

## File-size spot-check (anti-fabrication discipline per ENVELOPE rule 2 — `wc -c`, verified 2026-07-17)

```
skills/fantastic-posters/generate.js                                  — 24,626 bytes — read in full through the spend-logging block (lines 39-60)
skills/fantastic-posters/README.md                                    — 8,637 bytes — 170 lines, read in full
skills/fantastic-posters/.claude/skills/fantastic-posters/SKILL.md    — 18,484 bytes — 242 lines, read in full
skills/fantastic-posters/genius.md (pre-repair)                       — 14,883 bytes — 199 lines, read in full
skills/ben-watkins-storytelling/genius.md (house-style reference)     — 31,629 bytes — lines 7-16 read for the "How to Use This Skill" model
```

No source cited above was empty or unreadable — all sizes confirm real, substantive files, not the "unrecoverable/0-byte" false-absence failure mode the ENVELOPE flags.
