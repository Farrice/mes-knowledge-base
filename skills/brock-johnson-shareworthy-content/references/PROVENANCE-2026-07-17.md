# Provenance — brock-johnson-shareworthy-content repair (Wave 3 Lane 4)

Anchor → source file + location. Every quote below was located by direct
`Read` of the cited file during this repair pass (2026-07-17); none are
reconstructed from memory.

## Anti-Patterns (Sourced) — genius.md new `## Anti-Patterns (Sourced)` section

| Anchor text (as written in genius.md) | Source file | Verbatim location |
|---|---|---|
| "Algorithm-dependent (fragile)" | `references/_legacy-prompts/algorithm-transcendence-playbook.md` | Line 34, EXECUTION PROTOCOL step 1 bullet list ("Posting time optimization → Algorithm-dependent (fragile)", "Hashtag strategies → Algorithm-dependent (fragile)") |
| "Algorithmic suppression of pod engagement" | `references/_legacy-prompts/algorithm-transcendence-playbook.md` | Line 76, EXAMPLE OUTPUT Algorithm Dependency Audit bullet ("Engagement pods for initial boost → Fragile. Algorithmic suppression of pod engagement.") |
| "doesn't say anything interesting about the sharer... aimed at everyone, so it feels aimed at no one" | `references/_legacy-prompts/viral-share-optimizer.md` | Line 75, EXAMPLE OUTPUT § Share Blocker Diagnosis |
| "Look At Me" Aspirational Post anti-exemplar, Aspiration Gap Engineering 0/10 | `references/quality-rubric.md` | Lines 26–32, `### Anti-Exemplar: The "Look At Me" Aspirational Post` |
| "Believe in yourself and good things will happen" / 0/10 scores | `skills/brock-johnson-shareworthy-content/genius.md` (pre-repair, unchanged) | Original lines 86–92, `### Anti-Exemplar: The Vague Motivational Graphic` — this repair only adds the citation line; the anti-exemplar text itself was already present and passing (verbatim_exemplars check) |
| "Format isn't a container for content. Format IS content." | `references/_legacy-prompts/content-format-architect.md` | Line 10, ROLE & ACTIVATION |

## Named-entity-floor anchors (4 sections repaired, zero-entity ratio 0.25 → 0.00)

| Section in genius.md | Anchor added | Source | Location |
|---|---|---|---|
| Unconscious Mastery Behaviors #7 "Algorithm Transcendence" | "Algorithms change quarterly. Human nature hasn't changed in 200,000 years." | `references/_legacy-prompts/algorithm-transcendence-playbook.md` | Line 10, ROLE & ACTIVATION |
| Hidden Knowledge #2 "Metrics That Actually Matter" | "1 share = 150-400 views (10-26x more than likes)" — labeled UNCONFIRMED as a platform stat | `skills/brock-johnson-shareworthy-content/SKILL.md` (unchanged) | Line 13 |
| Hidden Knowledge #3 "The Format-Psychology Match" | "Format isn't a container for content. Format IS content." | `references/_legacy-prompts/content-format-architect.md` | Line 10 |
| "## Quality Rubric" pointer | 83,382-byte file size | `references/quality-rubric.md` | Confirmed via `wc -c` 2026-07-17 (see terminal output logged in REPAIR-NOTES.md) |

## Model Calibration section — genius.md new `## How to Use This Skill (Model Calibration)`

| Line | Source | Location |
|---|---|---|
| "Who do they send it TO? What do they say WHEN they send it?" | `references/_legacy-prompts/viral-share-optimizer.md` | Line 40, EXECUTION PROTOCOL step 2 |
| "Day 47 of being my own boss and I just scheduled a meeting... with myself" | `references/_legacy-prompts/shareworthy-content-generator.md` | Lines 78–80, EXAMPLE OUTPUT "The Meeting That Should Have Been an Email" (quoted with `...` marking the original's own em-dash pause, not an elision of separate sentences — reproduced verbatim from the hook line) |

## What is explicitly NOT claimed as sourced

Per the envelope's hard rule 2 (a claim that sources are absent is itself a
provenance claim), the following was verified by direct file read/search,
not assumed:

- No `extractions/` file matches `brock` or `johnson` (confirmed via `ls extractions/ | grep -i`, zero results, directory itself exists and is non-empty for other experts).
- No interview transcript, podcast transcript, or dated primary source exists anywhere in the repo (confirmed via `find . -iname "*brock*johnson*"`, all results are this skill's own files, the agent persona file, or generated evolution-store artifacts).
- The biographical claims in `SKILL.md` and `agents/brock-johnson/AGENT.md` (Adam Mosseri interview, 100K+ following, 18+ months proven implementation) are therefore UNCONFIRMED — not because they're false, but because no file in this repo substantiates them. Full detail in `references/source-ledger.md`.
