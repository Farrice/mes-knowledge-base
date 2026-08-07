# Google Antigravity Operating Structure

## Purpose

Use one active Antigravity source of truth while giving Claude Code and Codex
separate write lanes.

## Active Surfaces

| Surface | Role | Write Rule |
| --- | --- | --- |
| `/Users/farricecain/Google Antigravity` | Main hub, source of truth, Claude Code primary lane | Read-first for Codex unless clean and clearly assigned |
| `/Users/farricecain/Google-Antigravity-Codex` | Codex-owned worktree for mutations | Preferred Codex edit lane |
| `/Users/farricecain/.codex` | Thin global bridge and Codex instructions | Bridge only, never a full harness copy |
| `/Users/farricecain/Codex Antigravity` | Archived historical workspace | No routing, source truth, workflow ownership, or fallback unless Farrice explicitly names it |

## Default Operating Rule

Keep the harness in one place. Separate operators by worktree, not by duplicated
workspaces.

## When To Use Each Lane

### Use Google Antigravity main

- Reading source truth
- Routing work through local workflows
- Running status, preflight, search, and verification
- Claude Code sessions
- Content/client/project work already active in the main tree

### Use the Codex worktree

- Codex file edits
- System repairs
- Workflow/router/helper changes
- New durable operating docs
- Any mutation while Claude Code may also be active
- Any mutation while the main tree is dirty

### Use global Codex bridge

- Projectless Codex threads
- Quick route/preflight/status checks
- Getting from a raw request to the right Google-local workflow
- Checking write safety before mutations

## Mutation Protocol

1. Resolve the active hub with:
   `python3 ~/.codex/tools/antigravity_global.py status`
2. Check the write lane with:
   `python3 ~/.codex/tools/antigravity_global.py write-check`
3. If the helper returns `USE_WORKTREE`, make edits in:
   `/Users/farricecain/Google-Antigravity-Codex`
4. Verify from the lane where the edit was made.
5. Use a receipt for meaningful system work.

## Handoff Protocol

Before switching between Claude Code and Codex:

1. Stop active edits in the current tool.
2. Check status in the lane that was edited.
3. Leave a short handoff with:
   - objective
   - files touched
   - verification run
   - known dirty state
   - next safe action
4. Resume in the other tool only after the lane is clear or intentionally handed off.

## Project Organization

Keep projects inside Google Antigravity instead of creating new harness copies.

Recommended pattern:

| Project Type | Location |
| --- | --- |
| Active client/project work | `_active/<project-name>/` |
| Deliverables | `_active/<project-name>/04-deliverables/` |
| Exports | `_active/<project-name>/90-exports/` |
| Session handoffs | `.agent/handoffs/` |
| System receipts | `.agent/run-receipts/` |
| Operating docs | `_system/organization/` |

## Decision Rule

If the work needs the Antigravity brain, keep it in Google Antigravity. If the
work needs Codex to change files, do it in the Codex worktree. If the work is
only a standalone experiment with no harness dependency, it can live outside the
hub.
