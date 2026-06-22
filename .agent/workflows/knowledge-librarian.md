---
description: Compact session-start knowledge pulse that finds relevant solution docs, underused workflows, expert stacks, stale or overlap risks, and one exact start command without dumping the library
---

# /knowledge-librarian - Antigravity Knowledge Librarian

Surface the right knowledge, skills, experts, and underused workflows at the start of serious work so the arsenal compounds instead of becoming shelfware.

Use this as a compact routing aid, not a library browser. The goal is to reduce reconstruction burden and name the next usable command.

## Operator Core Alignment

This workflow is the canonical source of truth for Knowledge-librarian behavior.
Global and local Knowledge-librarian wrappers must stay thin compatibility
wrappers that point back here, not competing behavior contracts.

Preserve these invariants:

- `/knowledge-librarian` is a compact session-start knowledge pulse by default.
- Default scans are read-only: use `python3 execution/knowledge_compiler.py stats` and `python3 execution/knowledge_compiler.py solutions "[focus]" --top 8 --stdout`.
- Read `knowledge/compiled/briefing.md` if it exists; do not generate or refresh the briefing by default.
- Use router and expert commands only to ground recommendations in local evidence.
- Do not write `.agent/knowledge-librarian-state.md`, refresh compiled knowledge, create solution docs, mutate Mission, perform cleanup, or mirror global files unless explicitly requested.
- Route repair, drift-audit, and broken-system language to `/system-audit` or `/autopilot`; use `/knowledge-librarian` for library pulse, reusable-context, prior-decision, solution-doc, and underused-workflow questions.
- Real Codex subagents require explicit authorization.

## Usage

```bash
/knowledge-librarian
/knowledge-librarian [focus area]
/knowledge-librarian --deep [focus area]
```

## Default Output

Produce a compact **Library Pulse**:

- current knowledge base status
- reusable `docs/solutions/` entries relevant to the focus
- most relevant skills for the current focus
- sleeping giants Farrice is underusing
- stale, overlap, or gap warnings
- recommended expert stacks
- extraction opportunities worth turning into workflows or agents

Keep the pulse tight:

- up to 5 capabilities
- up to 3 reusable solution docs
- up to 3 sleeping giants
- up to 2 expert stacks
- exactly 1 start command or start sequence

If the library has no relevant solution docs for the focus, say `No matching solution doc found` instead of inventing one.

## Pre-Flight

Read:

1. `agents/knowledge-librarian/AGENT.md`
2. `.agent/knowledge-librarian-state.md` if present
3. `.agent/session-state.md` if present
4. `knowledge/compiled/briefing.md` if present

## Focus Fallback

If the user gives a focus area, use it. If not, infer the focus from `.agent/session-state.md`, then from `knowledge/compiled/briefing.md`. If neither provides a usable focus, use `current Antigravity operating session` and produce a general pulse.

Ask a clarifying question only when the focus changes which commands would be safe to recommend. Otherwise state the inferred focus and continue.

## Library Scan

Run from the project root:

```bash
python3 execution/knowledge_compiler.py stats
python3 execution/knowledge_compiler.py solutions "[session focus or current objective]" --top 8 --stdout
```

Read `knowledge/compiled/briefing.md` if it already exists. Do not run
`python3 execution/knowledge_compiler.py briefing` by default because it writes
compiled output.

If the user provides a focus area, also run:

```bash
python3 execution/knowledge_compiler.py solutions "[focus]" --top 8 --stdout
python3 execution/command_menu.py search "[focus]"
python3 execution/workflow_router.py search "[focus]"
python3 execution/expert_router.py route "[focus]"
python3 execution/expert_router.py compounds "[focus]"
python3 execution/context_retriever.py search "[focus]" --top 10
```

Evidence rule: every named capability must come from at least one local source:
command menu result, workflow router result, expert router result, context
retriever result, existing compiled briefing, or solution search. Do not name
assets from memory alone when a local check can verify them.

Use `--deep` only when the user wants library maintenance, consolidation, or a larger audit. In deep mode, add:

```bash
python3 execution/knowledge_compiler.py stale
python3 execution/knowledge_compiler.py overlap
```

## Library Pulse Schema

```markdown
# Library Pulse: [Date or Focus]

## Current Arsenal Status
- **Knowledge base**: [file/word count from stats]
- **Recent signals**: [from compiled briefing/session state]
- **Operating risk**: [underuse, stale knowledge, overlap, missing proof, etc.]

## Most Relevant Capabilities
| Capability | Command/Skill | Why it matters now |
|------------|---------------|--------------------|

## Reusable Solutions
| Solution Doc | Why it matters now | Mission use |
|--------------|--------------------|-------------|

## Sleeping Giants
| Underused asset | What it unlocks | When to deploy |
|-----------------|-----------------|----------------|

## Recommended Expert Stacks
1. [Expert/skill] + [Expert/skill] -> [compound output]
2. ...

## Gaps and Cleanup
- **Stale/overlap risk**: [if any]
- **Extraction opportunity**: [if any]
- **Bridge/index issue**: [if any]
- **Solution promotion**: [new reusable learning to add to docs/solutions, if any]

## Start Here
[one concrete command or sequence for today's work]
```

## Missing-Info Behavior

- Missing focus, but session state exists: infer and continue.
- Missing focus and no useful state: use `current Antigravity operating session`.
- No solution docs matched: state that plainly and continue with commands.
- Routers disagree: show the top disagreement only if it changes the start command.
- The result would become a giant menu: cut to the top 3 capabilities and one start command.

## State Snapshot

Only when the user explicitly asks to persist the pulse or run a maintenance
refresh, update `.agent/knowledge-librarian-state.md` with:

- date
- focus
- reusable solution docs surfaced
- top surfaced skills/workflows
- sleeping giants
- stale/overlap/gap warnings
- recommended next command

Keep this lightweight. Do not duplicate compiler reports.

## Quality Gate

Before delivering, check:

- The pulse surfaces at least 3 relevant capabilities when the library has matches.
- The pulse checks `docs/solutions/` and names applicable reusable solution docs before recommending new work.
- If no solution docs match, it explicitly says `No matching solution doc found`.
- It avoids dumping a giant inventory.
- It names exact commands or skills, not vague categories.
- It distinguishes underused assets from already-active workflows.
- It ends with one clear start command.
- It does not create a new root skill or duplicate the bridged `source-command-knowledge-librarian` surface.

## Verification

After changing this workflow, run:

```bash
python3 execution/sync_operator_core_knowledge_librarian.py --check
python3 execution/verify_operator_core_knowledge_librarian.py
python3 execution/validate_skill.py source-command-knowledge-librarian
python3 execution/knowledge_compiler.py solutions "operator core" --top 1 --stdout
python3 execution/operator_core_status.py --plain
python3 execution/verify_operator_core_status.py
python3 execution/verify_system_control_plane.py
python3 execution/codex_live_surface_audit.py --strict
python3 execution/codex_harness_check.py
```
