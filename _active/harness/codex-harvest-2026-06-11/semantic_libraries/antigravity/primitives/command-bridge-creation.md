# Command Bridge Creation

## Purpose And Operating Definition

This primitive governs adding or updating a slash-command surface in Codex Antigravity. The work is not "create a markdown file." The work is making a command reliably invokable across the live workflow, legacy Claude command, and Codex skill discovery surfaces so future agents do not misfire.

## When To Use

- Creating a new `/command`.
- Migrating a Claude slash command into Codex.
- Adding a workflow that should be discoverable from natural language.
- Updating command metadata, descriptions, or routing language.
- Fixing a command that exists in one surface but not another.

## When Not To Use

- A private reference file that is not meant to be invoked.
- A skill workflow that should remain internal and not slash-command accessible.
- A one-off deliverable or client document with no command surface.

## Inputs

| Input | Required | Source Of Truth | Notes |
|---|---|---|---|
| Command slug | Yes | User request or workflow name | Use kebab-case without leading slash in filenames |
| Command purpose | Yes | User objective and workflow frontmatter | Must be specific enough for routing |
| Workflow body | Yes | `.agent/workflows/[slug].md` | Executable protocol |
| Source command shim | Yes | `.claude/commands/[slug].md` | Legacy command bridge |
| Codex command skill | Yes | `.agents/skills/source-command-[slug]/SKILL.md` | Codex discoverability |
| Validation query | Yes | User language and likely natural-language trigger | Test both exact command and vague intent |

## Outputs

| Output | Format | Destination | Owner |
|---|---|---|---|
| Workflow file | Markdown | `.agent/workflows/[slug].md` | Codex Antigravity |
| Claude command shim | Markdown | `.claude/commands/[slug].md` | Codex Antigravity |
| Codex source-command skill | `SKILL.md` | `.agents/skills/source-command-[slug]/` | Codex Antigravity |
| Validation evidence | Command output summary | Final response or validation log | Implementing agent |

## Objects And Meaning

| Object | What It Means | Why It Matters |
|---|---|---|
| `.agent/workflows/[slug].md` | The actual executable command protocol | Future agents follow this file |
| `.claude/commands/[slug].md` | Legacy slash-command shim | Preserves original command behavior |
| `.agents/skills/source-command-[slug]/SKILL.md` | Codex-discoverable command trigger | Lets Codex load the command as a skill |
| Frontmatter description | Routing signal | Determines whether natural-language search finds the command |
| Command menu result | Live command surface truth | Confirms the command is user-visible |
| Workflow router result | Semantic route truth | Confirms vague intent finds the command |

## Authority And Permissions

| Action | Agent May Do | Requires Approval | Never Do |
|---|---|---|---|
| Create bridge files in Codex Antigravity | Yes | No | Do not modify Google Antigravity |
| Create `.agents/skills` directories | Yes | Escalation if sandbox blocks it | Do not bypass approval |
| Run registry sync and validation | Yes | No | Do not claim checks were run if they were not |
| Delete or rename existing commands | No | Explicit request | Never break unrelated command surfaces |

## Execution Protocol

1. Define the command slug and the user-facing trigger language.
2. Create or update `.agent/workflows/[slug].md` with executable steps.
3. Create or update `.claude/commands/[slug].md` pointing to the workflow.
4. Create or update `.agents/skills/source-command-[slug]/SKILL.md` with matching purpose and command template.
5. Use descriptions that include both exact command language and likely natural-language intent.
6. Run `python3 execution/sync_registries.py` if a skill or index-relevant file changed.
7. Verify `python3 execution/command_menu.py show [slug]`.
8. Verify `python3 execution/command_menu.py search "[natural-language trigger]"`.
9. Verify `python3 execution/workflow_router.py search "[natural-language trigger]"`.
10. Record any router weakness and tighten descriptions if needed.

## Decision Rules

| Condition | Rule | Reason |
|---|---|---|
| Command should be user-invokable | Create all three bridge layers | Partial command surfaces create misfires |
| Router misses vague intent | Add trigger language to frontmatter and skill description | Search depends heavily on descriptions |
| Command only supports exact slug | Improve natural-language metadata | Users often ask in plain English |
| `.agents/skills` creation is blocked | Request sandbox escalation | This is a required command layer |
| Existing command is being changed | Preserve unrelated behavior | Avoid accidental regressions |

## Examples

### Good Example

`/steering-compass` includes `.agent/workflows/steering-compass.md`, `.claude/commands/steering-compass.md`, `.agents/skills/source-command-steering-compass/SKILL.md`, command menu show validation, command menu search validation, workflow router validation, and tightened natural-language metadata for "I have an idea and do not know what command to run."

### Counterexample

Creating `.agent/workflows/new-command.md` and telling the user the slash command is ready without adding the source-command skill or testing the command menu.

## Quality Tests

| Test | Pass Criteria | Failure Response |
|---|---|---|
| Three-layer presence | All three files/directories exist | Add missing bridge layer |
| Exact command show | `command_menu.py show [slug]` resolves | Fix filename or metadata |
| Natural-language search | `command_menu.py search` finds command in top results | Strengthen descriptions |
| Workflow router search | Router finds command for likely user wording | Add trigger terms |
| Skill index integrity | Registry sync does not break skill validation | Re-run sync and inspect |
| Boundary safety | No original workspace edits | Stop and report if violated |

## Failure Modes

| Failure Mode | Early Signal | Prevention | Recovery |
|---|---|---|---|
| Workflow-only command | Command not visible in Codex skill bridge | Require three-layer checklist | Add missing source-command skill |
| Vague routing miss | Exact slug works, plain English misses | Include user-language triggers | Patch descriptions and re-test |
| Stale registry | Index lacks new skill/workflow count | Run sync | Inspect frontmatter |
| Overbroad description | Wrong command ranks first | Use specific trigger language | Narrow metadata |
| Sandbox bridge block | Cannot create `.agents/skills` dir | Request escalation | Retry approved mkdir |

## Maintenance Protocol

- Owner: Codex Antigravity operator.
- Review cadence: every time a command is added, migrated, or made user-facing.
- Update triggers: command menu miss, workflow router miss, new bridge convention, repeated "command not found" behavior.
- Last updated: 2026-05-06.
