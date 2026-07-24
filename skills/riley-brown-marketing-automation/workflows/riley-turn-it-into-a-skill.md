---
description: "Riley Brown's core meta-move — freeze any successful run as a named, inspectable skill/workflow (New workflow / AGENTS.md / record-and-replay), read what the agent wrote, and write corrections into the file so they compound."
---

# /riley-turn-it-into-a-skill — Freeze a Run into a Named Asset

The load-bearing pattern under everything Riley does (Patterns 2, 3, 14): "I'll tell the agent to do a thing, then... make the thing better and then I'll just tell it to turn it into a skill." The durable asset is a *named, callable file* born from a successful run — never a prompt written cold. On his screen this is a first-class command: Codex's palette ships **"New workflow — Save this task as a new workflow"** and **"Memory — Create an AGENTS.md file for Codex."** And "just turn it into a skill" hides real generated code — the Foreplay skill was a 4-file Python pipeline. **Treat a skill as software: open it and read what it wrote.**

## Pre-Flight Gate

Load `genius.md` first. Fire this when:
- A run just succeeded and the task **will recur** (Riley's trigger: "would this be useful on a recurring basis?").
- OR a correction was just made that should **stick** rather than evaporate in chat.
- The three creation paths available: **compile-from-scrape** (a scraped corpus), **refine-a-task** (a good run you improved), **record-a-screen** (a GUI workflow with no clean API).

## Skill Acquisition

- `genius.md` — Patterns 2 (skill-creation-by-doing), 3 (self-update), 14 (record-and-replay); Hidden Knowledge #1, #2
- `references/source-quotes.md` — quotes 7, 17, 19, 20, 24
- Antigravity analogs: `/extract` (compile), `.agent/workflows/*.md` authoring conventions, `directives/steering-loop.md` Forge Radar

## Execution

1. **Confirm the run was good.** Riley freezes *successful* runs, never aspirational ones. If the output didn't survive being read aloud, refine first.
2. **Pick the creation path:**
   - *Compile-from-scrape* → the corpus is banked; graduate to `/extract`.
   - *Refine-a-task* → capture the improved procedure as a `.agent/workflows/<name>.md` (frontmatter + steps), matching house conventions.
   - *Record-a-screen* (no API) → Riley's record-and-replay: drive the GUI once via Playwright (Tier 1 read-only where possible), then codify the observed steps into a computer-use workflow. His analog: "Show me the Typefully draft process... it's creating this skill called manual tweet draft."
3. **Name it.** The memorable name is the API into the capability ("Call it Callaway top performing"). Pick a slash-name that reads at a glance.
4. **Read what it wrote.** Open the generated file/pipeline — a skill may be real code (Hidden Knowledge #1). Confirm it does what you think; note any AGENTS.md-style memory it persisted.
5. **Bake in the two non-negotiables:** *return a link/artifact path* on every producing skill, and (for outbound) a *draft/link terminus behind approval* — never auto-execute.
6. **Correct into the file.** When it later drifts, write the fix *into the skill* ("please update the … skill so that you never say X") — Pattern 3, corrections compound. Log a Solution Card via `/extract-approach` if the crack was non-trivial (CLAUDE.md Step 6.5).

## Content Type Adaptations

| Path | When | Antigravity route |
|---|---|---|
| Compile-from-scrape | you have a corpus | `/extract` (ungated) |
| Refine-a-task | a good run to freeze | `.agent/workflows/<name>.md` |
| Record-a-screen | GUI, no API | Playwright drive → computer-use workflow |
| Correction | drift after use | edit the skill file in-session |

## Output Requirements

- A **named**, inspectable file (workflow/skill/extraction) — not a re-explained prompt.
- Evidence you *read* what the agent wrote (what the file/pipeline actually contains).
- "Return a link" + approval terminus present on any producing/outbound skill.
- Corrections written into the file, with a one-line note of what changed.

Execution prompt: references/prompts-v2/durable-asset-forge.md — honor its Output Contract.

## Quality Gate

Born from a *successful* run, not aspiration? · Named memorably (the name is the API)? · You opened and read the generated file (not a black box)? · Link-return + human-gate terminus baked in? · Would this survive Farrice invoking it cold next month?
