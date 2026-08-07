---
description: Create a focused transfer-ready handoff for another Codex session, branch, tool, or agent without closing the whole session
---

# /handoff - Focused Session Transfer

Use this when a branch of the current work should move to another session,
agent, prototype lane, research lane, or tool without ending the parent session.
Use `/end-session` when the whole session is being closed.

This workflow adapts Matt Pocock's MIT-licensed `/handoff` pattern from
`mattpocock/skills` into Codex Antigravity's receipt/status model. Source
evidence for the video is stored at
`extractions/video-context/dtAJ2dOd3ko/`.

## Usage

```bash
/handoff [what the next session will be used for]
```

## Pre-Flight

Read only the context needed for the destination purpose:

1. `.agent/intent-memory/current.json`
2. `.agent/system-cohesion-state.json`
3. `.agent/run-receipts/latest.md`
4. `.agent/session-state.md` if present
5. User-named artifacts, source packages, workflows, or files

## Handoff Rules

- Save disposable transfer handoffs to the OS temp directory, not the project
  workspace, unless the user explicitly asks for a durable local artifact.
- Reference existing artifacts by path or URL instead of copying large content.
- Redact secrets, API keys, credentials, private contact details, and sensitive
  personal information.
- Tailor the handoff to the destination purpose; do not summarize everything.
- Include suggested Antigravity skills/workflows so the next session does not
  require command memory.
- Keep the main Codex thread as integration owner unless real subagents were
  explicitly authorized.

## Output Shape

```markdown
# Handoff: [Destination Purpose]

## Purpose
- **Next session should do:**
- **Not in scope:**

## Load First
- [path or URL] - [why it matters]

## Current State
- **Objective:**
- **What is already done:**
- **What is uncertain or stale:**
- **Latest proof/receipt:**

## Suggested Skills / Workflows
- `/route` - [why this is the right next route]

## Exact Next Prompt
```text
[copy-paste prompt for the next session]
```

## Acceptance Criteria
- [observable completion bar]

## Risk Notes
- [privacy, routing, stale state, or verification risks]
```

## Verification

After changing this workflow, run:

```bash
python3 execution/verify_contextual_next_prompts.py
python3 execution/command_menu.py search "prepare a handoff document for a fresh agent"
python3 execution/workflow_router.py search "prepare a handoff document for a fresh agent"
```
