# AGENTS.md — Codex Antigravity Harness

This is the Codex comparison workspace for the Antigravity system. It is a separate copy from `/Users/farricecain/Google Antigravity`; do not modify the original workspace when working here.

## Canonical System Rules

Read `CODEX.md` as the primary Codex-native harness specification. It defines the active authority order, routing surface, skill-system contract, hot/cold skill policy, subagent boundary, and verification standard.

`GEMINI.md`, `CLAUDE.md`, and `.claude/commands/` are retained as legacy/source compatibility references. They are not active routing authority in Codex unless the user explicitly asks to inspect or back-port model-specific behavior.

## Codex Command Bridge

Claude slash commands are represented three ways:

- Source command text: `.claude/commands/<command>.md`
- Executable workflow: `.agent/workflows/<command>.md`
- Codex-discoverable skill: `.agents/skills/source-command-<command>/SKILL.md`

For Codex, the active routing surface is `.agent/workflows/` plus the hot
control-plane wrappers in `.agents/skills/source-command-*`. Cold migrated
wrappers live in `.agents/cold-skills/source-command-wrappers/` as recoverable
quarantine, not deletion. Keep `.claude/commands/` as source/compatibility
metadata for migrated commands; do not treat matching Claude and Codex command
names as duplicate active workflows or routing bloat.

When the user invokes `/command`, `@command`, "run command", or the bare command name, load the matching Codex skill if available, then read and execute the referenced workflow from `.agent/workflows/`. If a cold skill wrapper is missing from `.agents/skills` but the workflow exists, use the workflow directly and treat that as intentional live-surface hygiene, not a migration gap.

## Codex Subagent Bridge

Claude subagents live in `.claude/agents/*.md`. In Codex, treat them as role/process specifications, not native tools. Read the relevant subagent file when a workflow calls for that worker. Only spawn Codex subagents when the user explicitly asks for parallel agents or delegated agent work; otherwise execute the subagent protocol locally.

## Execution Preference

Prefer deterministic scripts in `execution/` before inventing manual process. Run commands from this project root. Use `.codex/config.toml` for Codex MCP/server configuration, while preserving the harness rule that Notion writes go through `execution/notion_api.py` unless the user explicitly asks for the Codex Notion connector.

For end-to-end skill-system work, follow `semantic_libraries/antigravity/primitives/skill-system-contract.md`: small components, explicit step order, input/output handoffs, human checkpoints, validation, result surface, and context policy.

For failed revisions, wrong routes, or "cannot repeat the magic" work, follow `semantic_libraries/antigravity/primitives/repeatability-spine-contract.md`: good example, failed example, failure class, preservation lock, repair route, validation, regression guard, and replay prompt.

## Written Deliverable Surface Contract

For substantial written knowledge work, make the user-facing surface a Rendered Conversation Document: the readable document shown directly in chat with clean headings, sections, spacing, and tables when useful.

Use exact surface terms:

- Rendered Conversation Document: full readable content shown in conversation.
- Local Markdown Source: saved `.md` persistence copy. It is not the primary review surface.
- External Export: `.docx`, HTML, Canva, Google Docs, Notion, PDF, or similar formats. Create only when explicitly requested.

When saving written deliverables locally, use sidecar metadata with `userFacingSurface: "rendered-conversation-document"`, `sourceRole: "persistence-copy"`, and `externalExportRequested: false` unless an export was explicitly requested. Run `python3 execution/artifact_surface_guard.py [artifact path]` and `python3 execution/export_format_guard.py [artifact path]` before finalizing substantial written artifacts.

Readable Markdown rule: human-facing `.md` files must open as documents, not
metadata records. The first meaningful line should normally be `# Title`.
Do not put visible YAML frontmatter, JSON metadata, `IsArtifact`,
`artifact_type`, `title:`, `status:`, `tags:`, or similar metadata headers at
the top of written deliverables. Use sidecar metadata instead. YAML
frontmatter remains allowed only for system surfaces that require it, such as
workflow files, command bridges, skills, agents, parseable design specs, and
explicitly machine-readable templates.

## Global Artifact Organization

Use `execution/artifact_router.py` and `/artifact-router` for files, documents, artifacts, deliverables, and project folders across `/Users/farricecain/Codex Antigravity` and `/Users/farricecain/Documents/Codex`.

Project homes live under `_active/<project-slug>/` with `INDEX.md`, `00-start-here/`, `01-source/`, `02-research/`, `03-working-drafts/`, `04-deliverables/`, `05-assets/`, `06-system/`, `90-exports/`, and `99-archive/`.

Before closeout for substantial artifact-producing work, run:

```bash
python3 execution/artifact_router.py enforce [artifact path]
python3 execution/artifact_frontmatter_guard.py [artifact path]
```

For cleanup, use staged plans and apply only safe moves. Do not modify `/Users/farricecain/Google Antigravity`.

## Migration Boundary

All Codex-specific fixes, adapters, audits, and experiments belong in this workspace. Do not edit `/Users/farricecain/Google Antigravity` unless the user explicitly asks to back-port a change.
