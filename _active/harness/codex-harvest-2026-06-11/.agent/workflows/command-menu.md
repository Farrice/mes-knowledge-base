---
description: Dynamic command palette for selecting Antigravity workflows
---

# /command-menu — Dynamic Workflow Command Palette

Use this when Farrice wants to browse, search, compare, or choose which slash-command workflow to run.

This is a selector, not an executor. It should present options and wait unless Farrice explicitly says to run the selected workflow.

## Usage

```bash
/command-menu
/command-menu linkedin growth
/command-menu domain copy
/command-menu show deep-research
```

## Steps

### 1. Build the Dynamic Index

Run the command menu script from the project root:

```bash
python3 execution/command_menu.py
```

For a search query:

```bash
python3 execution/command_menu.py search "[query]"
```

For a domain:

```bash
python3 execution/command_menu.py domain "[domain]"
```

For one command:

```bash
python3 execution/command_menu.py show "[command]"
```

### 2. Present the Shortlist

Show the best matches with:

- slash command name
- plain-English description
- detected domain
- whether the Codex skill bridge exists
- whether the source command exists

### 3. Ask for Selection

End with a simple choice prompt:

```text
Reply with the number or command name to run it, or ask for narrower alternatives.
```

### 4. Execute Only After Direction

When Farrice selects a command, load its matching hot `source-command-*` skill if present, then read and execute `.agent/workflows/[command].md`.

If the Codex skill is cold-quarantined or missing but the workflow exists, use the workflow directly. Treat this as intentional live-surface hygiene unless the command is one of the hot control-plane routes.
