# Agent Workflow Update

## Purpose And Operating Definition

This primitive governs edits that change how future agents, commands, or workflows behave in Codex Antigravity. The work is not "edit markdown." The work is modifying an operational surface that future agents may execute.

## When To Use

- Adding a new slash command.
- Updating an existing workflow.
- Creating a skill that should be command-discoverable.
- Changing bridge files that affect routing or command execution.

## When Not To Use

- One-off prose drafts that are not part of the operating system.
- External publishing or outreach actions.
- Changes outside `/Users/farricecain/Codex Antigravity` unless explicitly authorized.

## Inputs

| Input | Required | Source Of Truth | Notes |
|---|---|---|---|
| User objective | Yes | Current conversation | Must define desired capability |
| Existing workflow conventions | Yes | `.agent/workflows/`, `.claude/commands/`, `.agents/skills/` | Preserve bridge shape |
| Skill or agent context | Sometimes | `skills/`, `agents/`, indexes | Load only relevant files |

## Outputs

| Output | Format | Destination | Owner |
|---|---|---|---|
| Workflow | Markdown | `.agent/workflows/` | Codex Antigravity |
| Claude command shim | Markdown | `.claude/commands/` | Codex Antigravity |
| Codex source-command skill | `SKILL.md` | `.agents/skills/source-command-*` | Codex Antigravity |
| Validation evidence | Command output summary | Final response or local log | Implementing agent |

## Objects And Meaning

| Object | What It Means | Why It Matters |
|---|---|---|
| Workflow file | Executable operating protocol | Future agents follow it |
| Command shim | Command bridge from slash command to workflow | Keeps legacy command surface working |
| Source-command skill | Codex-discoverable trigger | Makes commands loadable in Codex |
| Registry index | Search and routing truth | Confirms discoverability |

## Authority And Permissions

| Action | Agent May Do | Requires Approval | Never Do |
|---|---|---|---|
| Edit local bridge files | Yes | No | Do not edit original Google Antigravity workspace |
| Run validation scripts | Yes | No | Do not claim unrun validation |
| Use network or paid tools | Only when necessary | Yes if sandbox or policy requires it | Do not bypass approval |
| Delete or reset files | No | Explicit request required | Never destructively clean unrelated changes |

## Execution Protocol

1. Interpret the user objective as an operating capability.
2. Inspect nearby workflow and skill conventions.
3. Create or update all required bridge layers.
4. Sync registries if a skill or agent was added.
5. Validate via skill validator, command menu, workflow router, and index search.
6. Report any warnings directly.

## Decision Rules

| Condition | Rule | Reason |
|---|---|---|
| Skill should be slash-command runnable | Add all three bridge layers | Partial bridge causes future routing gaps |
| New skill creates reusable expertise | Add skill files and references | Avoid one-off prompt drift |
| Workflow changes future behavior | Run validation | Future agents depend on it |

## Examples

### Good Example

Adding `/semantic-doc-generate` includes `.agent/workflows/semantic-doc-generate.md`, `.claude/commands/semantic-doc-generate.md`, `.agents/skills/source-command-semantic-doc-generate/SKILL.md`, registry sync, and router verification.

### Counterexample

Only adding a workflow file and saying the command exists.

## Quality Tests

| Test | Pass Criteria | Failure Response |
|---|---|---|
| Command menu | Command appears in search | Add or fix bridge metadata |
| Workflow router | Workflow appears for relevant query | Improve description or registration |
| Skill validation | No critical errors | Add missing required files |
| Index search | Skill and agent appear after sync | Re-run sync or fix frontmatter |

## Failure Modes

| Failure Mode | Early Signal | Prevention | Recovery |
|---|---|---|---|
| Partial bridge | Command not discoverable | Create three layers together | Add missing layer |
| Stale index | Skill exists but index misses it | Run registry sync | Re-run sync and inspect frontmatter |
| Unsafe scope | Original workspace modified | Confirm cwd and path | Stop and report |

## Maintenance Protocol

- Owner: Codex Antigravity operator.
- Review cadence: whenever new command surfaces are added.
- Update triggers: bridge convention changes, router changes, validation script changes.
- Last updated: 2026-05-06.
