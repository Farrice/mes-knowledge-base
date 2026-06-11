"""Audit a working directory for existing Claude and Codex OS surfaces.

Read-only. Returns JSON describing what is already present so the
silver-platter interview can skip questions about infrastructure that exists.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def safe_count_lines(path: Path) -> int:
    try:
        return len(path.read_text(encoding="utf-8").splitlines())
    except Exception:
        return 0


def list_md(directory: Path) -> list[str]:
    if not directory.is_dir():
        return []
    return sorted(path.stem for path in directory.glob("*.md") if path.is_file())


def list_subdirs(directory: Path) -> list[str]:
    if not directory.is_dir():
        return []
    return sorted(path.name for path in directory.iterdir() if path.is_dir())


def list_files(directory: Path, pattern: str) -> list[str]:
    if not directory.is_dir():
        return []
    return sorted(path.name for path in directory.glob(pattern) if path.is_file())


def settings_has_hooks(path: Path) -> bool:
    if not path.is_file():
        return False
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return bool(data.get("hooks", {}))
    except Exception:
        return False


def command_names(directory: Path) -> list[str]:
    return [path.removesuffix(".md") for path in list_files(directory, "*.md")]


def audit(root: Path) -> dict:
    claude_dir = root / ".claude"
    codex_agent_dir = root / ".agent"
    codex_agents_dir = root / ".agents"
    data_dir = root / "data"
    silver_platters = root / "silver_platters"
    outputs = root / "outputs"

    root_claude = root / "CLAUDE.md"
    nested_claude = claude_dir / "CLAUDE.md"
    codex_md = root / "CODEX.md"
    agents_md = root / "AGENTS.md"

    detections = {
        "claude_md": {
            "exists": nested_claude.is_file() or root_claude.is_file(),
            "lines": safe_count_lines(nested_claude if nested_claude.is_file() else root_claude),
            "path": str(nested_claude.relative_to(root)) if nested_claude.is_file() else (str(root_claude.relative_to(root)) if root_claude.is_file() else None),
        },
        "codex_authority": {
            "codex_md": codex_md.is_file(),
            "agents_md": agents_md.is_file(),
            "active_workflow_count": len(command_names(codex_agent_dir / "workflows")),
            "command_skill_count": len(list_subdirs(codex_agents_dir / "skills")),
        },
        "settings_json": {
            "exists": (claude_dir / "settings.json").is_file(),
            "has_hooks": settings_has_hooks(claude_dir / "settings.json"),
        },
        "claude_skills": {
            "count": len(list_subdirs(claude_dir / "skills")),
            "names": list_subdirs(claude_dir / "skills"),
        },
        "codex_root_skills": {
            "count": len(list_subdirs(root / "skills")),
            "names": list_subdirs(root / "skills")[:80],
        },
        "claude_agents": {
            "count": len(list_md(claude_dir / "agents")),
            "names": list_md(claude_dir / "agents"),
        },
        "codex_agents": {
            "count": len(list_subdirs(root / "agents")),
            "names": list_subdirs(root / "agents")[:80],
        },
        "rules": {
            "count": len(list_md(claude_dir / "rules")),
            "names": list_md(claude_dir / "rules"),
        },
        "commands": {
            "claude_count": len(command_names(claude_dir / "commands")),
            "codex_workflow_count": len(command_names(codex_agent_dir / "workflows")),
        },
        "data_namespaces": list_subdirs(data_dir),
        "silver_platters": list_files(silver_platters, "*.md"),
        "audit_log": {
            "exists": (outputs / "audit_log.md").is_file(),
            "line_count": safe_count_lines(outputs / "audit_log.md"),
        },
        "raw_dropzone": {
            "exists": (data_dir / "raw_dropzone").is_dir(),
            "file_count": len(list((data_dir / "raw_dropzone").iterdir())) if (data_dir / "raw_dropzone").is_dir() else 0,
        },
        "converted": {
            "exists": (data_dir / "converted").is_dir(),
            "file_count": len(list((data_dir / "converted").iterdir())) if (data_dir / "converted").is_dir() else 0,
        },
    }

    has_anything = any(
        [
            detections["claude_md"]["exists"],
            detections["codex_authority"]["codex_md"],
            detections["settings_json"]["exists"],
            detections["claude_skills"]["count"] > 0,
            detections["claude_agents"]["count"] > 0,
            detections["rules"]["count"] > 0,
            detections["data_namespaces"],
            detections["silver_platters"],
        ]
    )

    skip_questions: list[str] = []
    if detections["claude_skills"]["count"] or detections["codex_root_skills"]["count"]:
        skip_questions.append("Are you already using an AI coding workspace?")
    if detections["claude_agents"]["count"] or detections["codex_agents"]["count"]:
        skip_questions.append("Do you already have agent roles?")
    if detections["silver_platters"]:
        skip_questions.append("Do you already have weekly silver platters?")
    if detections["raw_dropzone"]["exists"]:
        skip_questions.append("Do you have a conversion hook for non-text files?")

    return {
        "mode": "audit-existing" if has_anything else "greenfield",
        "detections": detections,
        "skip_questions": skip_questions,
    }


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
    print(json.dumps(audit(root), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

