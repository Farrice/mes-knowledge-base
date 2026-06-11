---
description: "Install the compounding loop on a KB — answers feed back in, sessions log to memory with pickup prompts, gap questions drive growth."
---

# Library Compound Loop

The difference between a reference shelf and a learning system: every use makes the next use better.

## Pre-Flight Gate
- Load `genius.md` §Compounding Loop + §Lifecycle steps 4-5.
- KB must exist and be seeded. An empty KB has nothing to compound.

## Skill Acquisition
Read `genius.md` + the target KB's schema file.

## Execution
1. **Install the outputs rule** in the KB schema: every question's answer is generated into outputs/ (files) or saved as a page/entry (Notion) AND presented to the user as an openable page — never chat-only. If answers have been evaporating in chat, this is the first fix.
2. **Install the save-back rule**: answers the user likes get re-ingested — as a wiki article (files) or DB entry with Confidence=Untested (Notion). Criterion: "would I want the next answer to build on this?"
3. **Install session memory**: end-of-session ritual — log key decisions to the chat-history/session-memory store + generate a pickup prompt referencing that entry for the next window (cross-session continuity where the platform has none).
4. **Run one full loop live**: question → output saved → answer saved back → session logged → pickup prompt produced. The loop is installed only when it has executed once.
5. **Gap-question cadence**: schedule the growth question — "based on everything in the KB, what are the 3 biggest gaps in my understanding of [focus themes]?" — outputs feed ingestion targets and the next health check.
6. **Mistake guard**: note in the schema that save-backs can compound errors → the monthly `/library-health-check` is the counterweight (stage 1 contradictions + stage 3 provenance).

## Content Type Adaptations
| Context | Adaptation |
|---|---|
| Notion | Session memory = DB5 (chat-history database); save-backs = new DB1 entries, Untested |
| Claude files | outputs/ + changelog; pickup prompt pasted into next session |
| Antigravity | Outputs already land in deliverables/ — the missing half is save-back: lessons → library entries (pair with /library-extraction-bridge) |
| Team use | Save-back requires a curator role: who approves what enters the shared wiki |

## Output Requirements
Schema updated with the three rules + one demonstrated full loop (transcript) + gap report #1 + the pickup prompt. State plainly which half was missing before (usually save-back).

## Quality Gate
`genius.md` §Rubric Compounding — ≥8 = the loop is a schema RULE with one demonstrated cycle, not advice. §Anti-Patterns: bookmark graveyard, static library.
