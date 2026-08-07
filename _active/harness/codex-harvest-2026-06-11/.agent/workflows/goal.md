---
description: "Use Codex native /goal for long-running, measurable Antigravity work"
---

# /goal - Codex Native Goal Mode Bridge

## Purpose

This workflow documents how to use OpenAI Codex's native `/goal` command inside the Antigravity harness.

It does not implement the native slash command. Native `/goal` is owned by the Codex runtime. This bridge exists so the Antigravity command menu, workflow router, and Codex skill bridge can discover the command and apply local operating standards.

## Native Command Surface

Use these directly in a Codex interactive session:

| Command | Use |
|---|---|
| `/goal` | Show the current goal state |
| `/goal <objective>` | Create or replace the active goal |
| `/goal pause` | Pause the active goal |
| `/goal unpause` | Resume a paused goal |
| `/goal clear` | Clear the goal |

## When To Use

Use `/goal` when the work is multi-turn, measurable, and benefits from Codex continuing until a concrete condition is met.

Good Antigravity fits:

- System evolution: complete one audit cycle, identify command bridge gaps, make verified fixes.
- Command migration: migrate missing Claude commands into Codex skills until command-menu search and workflow-router agree.
- AI Brain: build the next context layer, compile source notes, validate retrieval, and summarize changes.
- Revenue/content: turn one proof asset into LinkedIn, Substack, outreach, and offer angles with quality checks.
- Client deliverables: produce an artifact-first strategic deliverable, run the Chain, verify claims, and finalize.
- Design/build: generate or refine DESIGN.md, validate it, then build the UI surface from that design source.
- Betting/data ops: run the paper-trading review loop, update tracking, and report system health without placing real bets.

Avoid `/goal` for quick single-turn prompts, simple file reads, one-off answers, or commands that already have a tighter dedicated workflow.

## Antigravity Protocol

1. State the goal as a concrete outcome, not a vague aspiration.
   - Good: `/goal Migrate the missing goal command bridge, enable the goals feature, and verify command discovery.`
   - Weak: `/goal Work on the system.`
2. If the goal will produce any deliverable, the Chain still applies to each deliverable.
3. For source-backed claims, run factual verification before final delivery.
4. For file changes, keep edits inside `/Users/farricecain/Codex Antigravity` unless the user explicitly asks to back-port.
5. Do not use `/goal` to bypass approvals, budget guards, or required workflow routing.

## Personal Goal Templates

```text
/goal Complete one Antigravity system evolution pass: audit command discovery, fix the highest-impact bridge gap, run verification, and summarize the result.
```

```text
/goal Build the next AI Brain context layer: gather source notes, compile a concise knowledge artifact, validate retrieval, and document changed files.
```

```text
/goal Turn one proof asset into a revenue content package: LinkedIn post, Substack angle, outreach angle, offer angle, and final quality check.
```

```text
/goal Produce an artifact-first client deliverable: route experts, load context, draft, verify claims, finalize, and report acceptance criteria.
```

```text
/goal Refine a DESIGN.md and build from it: synthesize tokens, validate accessibility, implement the surface, and test responsive rendering.
```

## Output Contract For This Bridge

When this workflow is invoked through natural language rather than the native slash command, return:

- The exact `/goal ...` command the user should run.
- Why it is a good fit for goal mode.
- Any dedicated Antigravity workflow that should run inside the goal.
- The verification checks that mark the goal complete.

## Verification

After setup or changes, verify:

```bash
codex features list
python3 execution/command_menu.py search goal
python3 execution/workflow_router.py search goal
```

Expected:

- `goals` is enabled in the Codex feature list.
- `/goal` appears in command-menu search.
- `/goal` appears in workflow-router search.
