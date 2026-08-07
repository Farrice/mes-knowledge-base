# Plugin Readiness Audit Hidden Knowledge

## Antigravity-Specific Bridge

Codex command discoverability in this workspace depends on:

- `.agent/workflows/<command>.md`
- `.claude/commands/<command>.md`
- `.agents/skills/source-command-<command>/SKILL.md`

For plugin packaging, add:

- `plugins/<plugin-name>/.codex-plugin/plugin.json`
- `plugins/<plugin-name>/skills/<skill-name>/SKILL.md`
- `.agents/plugins/marketplace.json`

## Known Local Friction

Creating folders under `.agents/skills` or `.agents/plugins` can require elevated filesystem permission in this workspace. Treat that as a bridge verification step, not as evidence the plan is wrong.

## Fresh-Thread Proof

A local plugin package is not proven until Codex can find it from the marketplace and the user can ask for the outcome without re-explaining the operating system.

