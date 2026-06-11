#!/usr/bin/env python3
"""Install the Codex Dynamic Workflow runtime into the global Codex home."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNTIME_SOURCE = ROOT / "execution" / "codex_dynamic_workflow.py"


SKILL_TEXT = """---
name: "codex-dynamic-workflow"
description: "Global manifest-held workflow runtime for large, resumable, multi-phase Codex work"
---

# Codex Dynamic Workflow

Use this skill when the user asks for a dynamic workflow, workflow manifest,
resumable multi-phase run, many-file migration plan, bounded audit,
cross-checked research, adversarial review, or source-to-system extraction.

## Runtime

Run the global runtime from any workspace:

```bash
python3 ~/.codex/tools/codex_dynamic_workflow.py plan "[objective]"
python3 ~/.codex/tools/codex_dynamic_workflow.py status
python3 ~/.codex/tools/codex_dynamic_workflow.py complete-phase [phase-id] --result-path [path] --summary "[summary]"
python3 ~/.codex/tools/codex_dynamic_workflow.py verify
python3 ~/.codex/tools/codex_dynamic_workflow.py receipt
```

By default, state is stored in the current workspace under
`.agent/dynamic-workflows/`. To force a specific workspace root, set
`CODEX_DYNAMIC_WORKFLOW_ROOT=/absolute/path`.

## Operating Rules

- Keep the main Codex thread as final integration owner.
- Prepare worker packets, but do not spawn real Codex subagents unless the user
  explicitly authorizes delegation through the available Codex tool surface.
- Keep external writes, publishing, outreach, connector writes, paid/API usage,
  destructive cleanup, global mirrors, and Mission/system memory mutation behind
  approval gates.
- Use `complete-phase` after writing a phase result artifact so the manifest,
  worker packets, current phase, status, and receipt surface stay consistent.
- Use `verify` before trusting a saved manifest and `receipt` before closeout.

## Antigravity Compatibility

Inside the Codex Antigravity workspace, prefer `/virtuoso --workflow` as the
front door. In other workspaces, use this global runtime directly.
"""


def codex_home() -> Path:
    return Path.home() / ".codex"


def install(*, dry_run: bool = False) -> dict[str, str | bool]:
    home = codex_home()
    tool_dir = home / "tools"
    skill_dir = home / "skills" / "codex-dynamic-workflow"
    tool_path = tool_dir / "codex_dynamic_workflow.py"
    skill_path = skill_dir / "SKILL.md"
    result = {
        "dry_run": dry_run,
        "runtime_source": str(RUNTIME_SOURCE),
        "tool_path": str(tool_path),
        "skill_path": str(skill_path),
    }
    if dry_run:
        return result
    if not RUNTIME_SOURCE.exists():
        raise FileNotFoundError(f"runtime source missing: {RUNTIME_SOURCE}")
    tool_dir.mkdir(parents=True, exist_ok=True)
    skill_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(RUNTIME_SOURCE, tool_path)
    tool_path.chmod(0o755)
    skill_path.write_text(SKILL_TEXT, encoding="utf-8")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Install Codex Dynamic Workflow globally.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    print(json.dumps(install(dry_run=args.dry_run), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
