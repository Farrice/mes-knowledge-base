#!/usr/bin/env python3
"""Protect the integration-only main checkout from ordinary authoring.

This hook is deliberately narrower than a shell sandbox. It blocks the write
shapes that repeatedly dirty main while allowing read-only inspection and the
two audited integration owners (`worktree_lane.py merge` and
`lane_reconciler.py`). Worktree lanes are always allowed.

Exit 2 = block; exit 0 = allow.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path


WRITE_TOOLS = {"Write", "Edit", "NotebookEdit", "apply_patch"}
TARGET_KEYS = ("file_path", "notebook_path", "path")

# These commands are the only ordinary shell shapes that may intentionally
# mutate main. Their own code supplies the merge mutex, dirty-tree gate,
# Law-3 audit, and local-only default.
INTEGRATION_COMMANDS = (
    re.compile(r"\bworktree_lane\.py\s+merge\b"),
    re.compile(r"\blane_reconciler\.py\b"),
    re.compile(r"\bgit\s+worktree\s+(?:add|list|prune|remove)\b"),
)

# High-confidence direct Git mutations. Read-only Git commands remain usable.
GIT_MUTATIONS = re.compile(
    r"\bgit(?:\s+-C\s+(?:\"[^\"]+\"|'[^']+'|\S+))?\s+"
    r"(?:add|am|apply|checkout|cherry-pick|commit|merge|mv|rebase|restore|rm)\b"
)

# These are evidenced tracked-tree writers from closeout and generated-index
# paths. More may be added only with a failing fixture; this is not a generic
# list of every Python script in the repository.
KNOWN_WRITERS = (
    re.compile(r"\bend_session_closeout\.py\s+run\b"),
    re.compile(r"\bcodex_end_session\.py\s+run\b"),
    re.compile(r"\bchain_runner\.py\s+finalize\b"),
    re.compile(r"\bprojects_index\.py\s+sync\b"),
    re.compile(r"\bsession_closeout_intelligence\.py\s+run\b"),
    re.compile(r"\bmint_menu_wrappers\.py\b[^\n]*\s--apply\b"),
    re.compile(r"\bgenerate_slash_commands\.py\b(?![^\n]*\s--check\b)"),
    re.compile(r"\bsync_registries\.py\b(?![^\n]*\s--check\b)"),
    re.compile(r"\bself_heal\.py\s+heal\b"),
)


def _git(cwd: Path, *args: str) -> tuple[int, str]:
    try:
        proc = subprocess.run(
            ["git", "-C", str(cwd), *args],
            capture_output=True,
            text=True,
            timeout=10,
        )
        return proc.returncode, proc.stdout.strip()
    except Exception:
        return 1, ""


def _repo_context(cwd: Path) -> tuple[Path | None, bool]:
    """Return (worktree root, is_main_checkout). Fail open outside Git."""
    rc, root = _git(cwd, "rev-parse", "--show-toplevel")
    if rc != 0 or not root:
        return None, False
    tree = Path(root).resolve()
    rc1, git_dir = _git(tree, "rev-parse", "--path-format=absolute", "--git-dir")
    rc2, common = _git(tree, "rev-parse", "--path-format=absolute", "--git-common-dir")
    return tree, bool(rc1 == 0 and rc2 == 0 and git_dir == common)


def _target(payload: dict, cwd: Path) -> Path | None:
    tool_input = payload.get("tool_input") or {}
    raw = next((tool_input.get(key) for key in TARGET_KEYS if tool_input.get(key)), None)
    if not raw:
        return None
    path = Path(str(raw)).expanduser()
    return (path if path.is_absolute() else cwd / path).resolve(strict=False)


def _inside(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def _ignored(root: Path, path: Path) -> bool:
    try:
        rel = str(path.relative_to(root))
    except ValueError:
        return False
    rc, _ = _git(root, "check-ignore", "-q", "--", rel)
    return rc == 0


def bash_mutation(command: str) -> str | None:
    if any(pattern.search(command) for pattern in INTEGRATION_COMMANDS):
        return None
    if GIT_MUTATIONS.search(command):
        return "direct Git mutation"
    for pattern in KNOWN_WRITERS:
        if pattern.search(command):
            return "tracked-tree writer"
    return None


def verdict(payload: dict) -> tuple[bool, str]:
    cwd = Path(payload.get("cwd") or os.environ.get("CODEX_PROJECT_DIR")
               or os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()).resolve()
    root, is_main = _repo_context(cwd)
    if root is None or not is_main:
        return True, "outside main or already in a lane"

    tool_name = str(payload.get("tool_name") or "")
    if tool_name in WRITE_TOOLS:
        target = _target(payload, cwd)
        if target is not None and (not _inside(target, root) or _ignored(root, target)):
            return True, "write is outside the tracked main surface"
        detail = str(target.relative_to(root)) if target and _inside(target, root) else "unknown target"
        return False, f"native write to {detail}"

    if tool_name == "Bash":
        command = str((payload.get("tool_input") or {}).get("command") or "")
        reason = bash_mutation(command)
        if reason:
            return False, reason
    return True, "read-only or unclassified command"


def main() -> int:
    try:
        raw = sys.stdin.read()
        payload = json.loads(raw) if raw.strip() else {}
    except Exception:
        return 0
    allowed, reason = verdict(payload if isinstance(payload, dict) else {})
    if allowed:
        return 0
    print(
        "MAIN WRITE GUARD — BLOCKED: main is integration-only "
        f"({reason}). Create or enter a worktree lane, make the change there, "
        "then let worktree_lane.py merge it through the audited integration path. "
        "Read-only inspection may continue on main.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
