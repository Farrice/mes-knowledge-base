---
description: "Stand up the Karpathy-style self-improving knowledge base — raw/wiki/outputs + CLAUDE.md schema + compounding loop + health check. The full Video-2 five-step build."
---

# Library Second Brain

A self-improving file-based knowledge base in ~45 minutes: 3 folders, 1 schema file, 2 loops. No Obsidian, no vectors, no plugins.

## Pre-Flight Gate
- Load `genius.md` §Two Substrates + §Lifecycle.
- This is the FILE substrate. For Notion, use `/library-notion-port`.
- One KB = one subject. Multiple subjects = parent folder with its own CLAUDE.md holding multiple KBs.

## Skill Acquisition
Read `genius.md` + `references/kb-schema.md` §File substrate mapping.

## Execution
1. **Setup**: create `<parent>/<kb-name>/` with `raw/`, `wiki/`, `outputs/`, `CLAUDE.md`, `changelog.md`. Parent gets its own CLAUDE.md (how new KBs are created here).
2. **Write the KB CLAUDE.md**: focus themes (ethos sentence + 3-5 themes) · folder roles (raw = junk drawer, never organized; wiki = AI-written only, never hand-edited; outputs = every answer lands here AND is presented as an openable page) · entry schema · ingestion process incl. guided mode · the compounding rule (good answers re-ingested) · health-check spec (7 stages, monthly) · writing-rules pointer (anti-AI style guide — if absent, create one from Wikipedia's "AI writing style" inverted into never-do rules) · changelog-as-memory behavior.
3. **Dump**: user piles everything into raw/ — articles, notes, screenshots, transcripts, exports. Zero tidying. Md files preferred; PDFs flagged as degraded-read risk. Maintain an ingestion registry note.
4. **Build the wiki**: "Read everything in raw and compile a wiki in wiki/ following CLAUDE.md. Create index.md FIRST, then one md per major topic, link related topics." Writing-rules loaded before any wiki writing.
5. **Install the compounding loop**: verify the outputs rule is in CLAUDE.md; run one real question → confirm the answer lands in outputs/ as a presentable page; demonstrate the save-back ("save this answer into the wiki").
6. **Gap probe**: "Based on everything in the wiki, what are the 3 biggest gaps in my understanding of this topic?" → output feeds the first improvement cycle.
7. **Schedule the health check**: monthly, via `/library-health-check` — as a manually-triggered skill by default (economic routing), scheduled task only if the user accepts the cost.

## Content Type Adaptations
| Context | Adaptation |
|---|---|
| Claude Cowork/Desktop | Point at the folder; connectors (e.g. Notion) can feed the dump; scheduled tasks available |
| Claude Code / this repo | KB folders + CLAUDE.md inheritance; health check as a workflow command |
| Team/company | Parent = shared drive; add contribution rules to parent CLAUDE.md |
| Existing notes system (Obsidian/Notion exports) | Export → dump into raw/ wholesale; let the wiki build sort it |

## Output Requirements
Working KB: schema file complete, raw seeded, wiki built with index, one Q&A round-tripped through outputs, gap report generated, health check installed. Deliver paths + the day-1/day-100 expectation set honestly.

## Quality Gate
`genius.md` §Anti-Patterns: human edited the wiki (fail) · answers not landing in outputs (fail) · no health check installed (fail — errors will compound). Rubric: Compounding ≥8 = the loop is a CLAUDE.md rule, not a habit.
