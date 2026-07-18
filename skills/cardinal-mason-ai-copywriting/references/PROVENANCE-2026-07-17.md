# Cardinal Mason - AI Copywriting Mastery — Provenance Table (Repair 2026-07-17)

Anchor → source file + location. All three source files live at
`knowledge/extractions/inbox/` (repo root) and were not previously linked from
this skill's `references/`. File sizes confirmed via `wc -c` before use:
391,128 / 355,727 / 59,118 bytes for Part 1 / Part 2 / Part 3 respectively —
all non-empty, all read in full.

| Anchor (as it appears in genius.md) | Source file | Location | Session date |
|---|---|---|---|
| "Transform your life" / "Unlock your potential" / "It's not a diet, it's a lifestyle" / "Results may vary" / "Take the first step" / "Invest in yourself" / "journey" / "No pain no gain" | `Claude-...2026.md` (Part 1) | lines 766-773, "## Cliché Blacklist" | 2026-01-17 18:41:40 |
| "M-dashes (AI tell)" / "Here's the thing:" more than once per piece | `Claude-...2026.md` (Part 1) | lines 775-776, same section | 2026-01-17 |
| "Never force a joke. Never use puns. Never be cheesy or motivational-poster cringe." | `Claude-...2026.md` (Part 1) | line 779, "## Humor Guidelines" | 2026-01-17 |
| "I hope this email finds you well" / "I wanted to reach out" / "Just following up" | `Claude-...pt.2.md` | lines 1372-1375, "What to NEVER Say" | 2026-01-17 19:47:47 |
| "Leverage," "synergy," "optimize" / "Revolutionary," "game-changing," "cutting-edge" | `Claude-...pt.2.md` | lines 1376-1377, same section | 2026-01-17 |
| "I love what you're doing at [Company]." (flagged Bad) | `Claude-...pt.3.md` | line 1120, "The 3-Part Email Structure" | 2026-01-17 21:36:28 |
| "Do NOT open with 'In today's digital world...' or any throat-clearing." | `Claude-...pt.3.md` | line 812, "Part 1: The Disruption" | 2026-01-17 |
| "Pitching topics they want to write about, not topics editors need to publish." | `Claude-...pt.3.md` | lines 773-774, "The Mistake Everyone Makes" | 2026-01-17 |
| "$847/month" beats "hundreds of dollars." / "3:47 PM on a Tuesday" beats "one day." | `Claude-...pt.2.md` | line 1229, "Specificity Sells" (7 Copywriting Principles) | 2026-01-17 |
| "47% open rate increase, 2.3x launch revenue" | `Claude-...pt.2.md` | line 1190, "Signature Advantages — Results" | 2026-01-17 |
| "15-25% response rate ... vs. 2-5% on cold text DMs" | `Claude-...2026.md` (Part 1) | line 198, Pattern 4 success metric (already in genius.md pre-repair; anchor added, content unchanged) | 2026-01-17 |
| "$70K/month" solo operation, year one | `Claude-...pt.2.md` | line 1156, "Who You Are" (Agent Identity Core) | 2026-01-17 |
| Score 4 (Acceptable) / 7 (Good) / 10 (Savant) rubric anchors | `skills/cardinal-mason-ai-copywriting/references/quality-rubric.md` | line 5, "Expert-Specific Quality Rubric" table header | n/a (internal skill file, not the chat transcript) |

## Sections added in full (not single-quote anchors)

- `genius.md § How to Use This Skill (Model Calibration)` — new. Synthesized
  guidance (not a Mason quote) modeled on `skills/ben-watkins-storytelling/
  genius.md` lines 7-16 house style, grounded in Mason's own Pattern 1 (Context
  Brain Dump), Pattern 7 (Human Taste Layer), and the Specificity Sells example
  from `pt.2.md` line 1229. Contains the recognition-test sentence that
  satisfies the `recognition_test` heartbeat check.
- `genius.md § Anti-Patterns` — new. 8 list items, each independently carrying
  a quote and/or a `YYYY-MM-DD` source date so the `anti_patterns_sourced`
  heartbeat check (which inspects each list item individually) passes on every
  item, not just the section as a whole.
- `references/source-ledger.md` — new. Full claim-by-claim VERIFIED / LIKELY /
  UNCONFIRMED table, including the honest UNCONFIRMED flag on the pre-existing
  "Hall of Fame Exemplars" (searched all three source files for "Cardinal
  here," "Lifestyle-First Entrepreneur," "sustainable fashion" — zero matches;
  those exemplars are not literal Mason quotes and are labeled accordingly
  rather than left silently implied-verified).

## What was NOT touched

`SKILL.md`, `SKILL.md.old`, all 5 `workflows/*.md` files (already passing
`workflow_contracts`), `references/genius-patterns.md`, `hidden-knowledge.md`,
`implementation.md`, `quality-rubric.md`, and all `prompts/` / `prompts-v2/` /
`_legacy-prompts/` files are copied through unchanged — additive-first,
minimal-touch per the repair envelope.
