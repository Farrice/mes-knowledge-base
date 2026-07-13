---
name: "Mark Kashef Silver Platter — Builder Handoff Prompt"
source_prompt: born-v2
skill: mark-kashef-silver-platter-agentic-os
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are writing the **handoff prompt** the operator copy-pastes into a fresh Claude Code session to address `@claude-code-guide` and get their `.claude/` folder scaffolded to match the data map you built together. This document is the bridge between mapping and building — it is a punch list, not a wall of text, and it locks the voice and constraints so whatever `@claude-code-guide` produces matches the method's standards rather than generic scaffolding.

## Input Required

```
[BUSINESS_NAME]
[BUSINESS_ARCHETYPE]
[STACK_SUMMARY] - one-line tool stack description
[MODE] - greenfield | audit-existing (changes the framing: "scaffold from scratch" vs "augment my existing setup")
[PANTRY_ITEMS] - tool, format, cadence, volume, status, feeds, cli_skill per source
[PREP_ITEMS] - name, domain, sources, schedule, status per silver platter
[PLATE_ITEMS] - name, agent, consumers, approval_gate per human-facing output
[FOLDER_STRUCTURE] - the target data/ and silver_platters/ layout derived from the data map
[SKILLS_TO_WRITE] - list of {name, purpose}
[SUBAGENTS_TO_WRITE] - list of {name, role}
[RULES_TO_WRITE] - list of {name, paths}
[WORKING_DIRECTORY_PATH] - cwd the operator will run this from
```

## Execution Protocol

**Step 1 — Frame the opening line by mode.** Greenfield: *"I want you to scaffold the `.claude/` folder so the architecture matches."* Audit-existing: reframe explicitly as augmenting, not rebuilding — name what already exists and that this handoff is additive.

**Step 2 — Render the Business section.** Name, archetype, one-line stack summary — exactly as they appear in the data map, no re-summarization.

**Step 3 — Render the Data Map section in three blocks**, each item on its own line with sub-bullets, never collapsed into prose:
- **Pantry** (what data sources exist): tool, format, cadence, volume; status; what it feeds; CLI skill if one exists.
- **Prep table** (silver platters needed): name, domain, sources, schedule, status.
- **Plate** (outputs that go to humans): name, drafting agent, consumers, approval gate.

**Step 4 — Render "What I want you to build" as a numbered punch list**, not narrative:
1. The folder structure, one line per path.
2. A root `CLAUDE.md` under 200 lines that states the one-liner, names the agent hierarchy (one bullet per role), lists the hard rules, and references the path-scoped rules folder.
3. Every skill in `[SKILLS_TO_WRITE]`, name + purpose.
4. Every subagent in `[SUBAGENTS_TO_WRITE]`, name + role.
5. Every rule in `[RULES_TO_WRITE]`, name + paths.
6. The three-hook `.claude/settings.json` config: `SessionStart` (convert_dropzone.sh), `PostToolUse Edit|Write` (audit_action.sh, appends to `outputs/audit_log.md`), `Stop` (check_acknowledgment.sh, warn-on-unsigned-draft, exits 0).

**Step 5 — Render "Hard constraints I need you to honor"** verbatim in spirit (adapt only the business-specific parts): plain-English voice, operators are not engineers, translate every jargon term inline; never use em dashes anywhere in the `.claude/` files — comma, period, or rewrite; every human-facing output requires an approval gate; silver platters get committed to git, raw data exports do not; hooks are non-blocking by default (Stop hook exits 0); the orchestrator is a hierarchy, not a flat row — specialists report to the orchestrator, the operator only talks to the orchestrator.

**Step 6 — Render "What you should NOT do"**: no external dependencies beyond pandoc, poppler, jq, xlsx2csv, python3-stdlib; no tests yet, get the scaffolding right first; no git push or main-branch modification; no auto-run — the operator reviews every file created.

**Step 7 — Close with the working directory and the three closing asks**: what files were created (a list), what to open first to verify, and any open questions `@claude-code-guide` couldn't answer from this brief.

## Output Contract

A single addressed prompt (`@claude-code-guide ...`), sections in the fixed order above: opening line -> Business -> Data map (Pantry/Prep table/Plate) -> What I want you to build (6-item punch list) -> Hard constraints -> What you should NOT do -> Working directory -> closing asks. No em dashes anywhere in the document (the constraint applies to itself, not just the files it commissions). Written to `silver_platter_output/builder_handoff.txt` (or `claude_code_guide_handoff.txt` if Claude-compatibility framing was explicitly requested).

## Output Skeleton

```
@claude-code-guide

[opening line, mode-appropriate]

# Business

- Name: [BUSINESS_NAME]
- Archetype: [BUSINESS_ARCHETYPE]
- One-line: [STACK_SUMMARY]

# Data map

## Pantry (what data sources I have)

[one entry per pantry item: tool, format/cadence/volume, status, feeds, CLI skill if any]

## Prep table (silver platters I need)

[one entry per prep item: name (domain), sources, schedule, status]

## Plate (outputs that go to humans)

[one entry per plate item: name (drafted by agent), consumers, approval gate]

# What I want you to build

1. Create the folder structure:
   [one path per line]

2. Write a lean root CLAUDE.md (target < 200 lines) that:
   [4 sub-requirements]

3. Write [N] skills under .claude/skills/:
   [name — purpose, one per line]

4. Write [N] subagents under .claude/agents/:
   [name — role, one per line]

5. Write [N] rules under .claude/rules/:
   [name — paths, one per line]

6. Configure .claude/settings.json with three hooks:
   [SessionStart / PostToolUse / Stop, as specified]

# Hard constraints I need you to honor

[6 fixed constraints]

# What you should NOT do

[4 fixed prohibitions]

# Working directory

[WORKING_DIRECTORY_PATH]

When you're done, tell me:
1. What files you created (list)
2. What I should open first to verify
3. Any open questions you couldn't answer from this brief
```

## Quality Gate

- Are Pantry, Prep, and Plate rendered as three distinct labeled blocks, never merged into one list?
- Is "What I want you to build" a numbered punch list, not narrative prose?
- Are all six hard constraints present and unmodified in substance (plain English, no em dashes, approval gates, git policy, non-blocking hooks, orchestrator hierarchy)?
- Are all four "should NOT do" prohibitions present (no extra deps, no tests yet, no git push/branch modification, no auto-run)?
- Does the document itself contain zero em dashes?
- Does the opening line correctly reflect `[MODE]` (scaffold-from-scratch vs augment-existing)?

## Creative Latitude

This document is intentionally low-latitude — it is a commissioning brief, not a creative artifact, and its power comes from being a punch list `@claude-code-guide` cannot mistake for a suggestion. The only real judgment call is what belongs in "Any open questions" territory versus what you should just decide and state as a constraint; when the data map already answers a question, answer it in the brief rather than punting it downstream.

## Deploy When

A data map (and ideally a build plan) already exists and the operator is ready to move from mapping to scaffolding — the final artifact in the Silver Platter sequence, handed to `@claude-code-guide` or a technical builder.
