# Codex Antigravity Migration

This workspace is a Codex-native comparison copy of `/Users/farricecain/Google Antigravity`.

## What Changed Here

- `../AGENTS.md` now gives Codex direct operating instructions for the Antigravity harness.
- Claude slash commands are bridged through `.agents/skills/source-command-*`.
- Claude subagents are treated as readable role/process specs in `.claude/agents/`.
- `../execution/codex_harness_check.py` validates command coverage and core router health.
- The missing `newsletter-to-product` command skill was added in this workspace.

## What Was Preserved

- `../GEMINI.md` remains the canonical compressed harness spec.
- `../CLAUDE.md` remains the fuller operational reference.
- `.claude/commands/`, `.agent/workflows/`, `.agents/skills/`, `skills/`, `agents/`, `directives/`, `execution/`, `knowledge/`, `extractions/`, and project files were copied.
- `.codex/config.toml` was preserved for MCP/server configuration.

## What Was Not Copied

Generated or heavy local dependency folders were intentionally excluded:

- `.git/`
- `node_modules/`
- `.venv/`
- Python cache folders

Reinstall dependencies in this workspace only if a specific project needs them.

## Health Check

Run from this workspace:

```bash
python3 execution/codex_harness_check.py
```
