#!/usr/bin/env python3
"""Verify the human-readable Markdown metadata guard."""

from __future__ import annotations

import json
import shutil
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

import artifact_frontmatter_guard as guard  # noqa: E402


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def main() -> int:
    failures: list[str] = []
    temp_dir = Path(tempfile.mkdtemp(prefix="markdown-readability-"))
    try:
        active = temp_dir / "_active" / "demo" / "04-deliverables"
        active.mkdir(parents=True)

        readable = active / "readable.md"
        readable.write_text("# Readable\n\nThis starts like a document.\n", encoding="utf-8")
        readable.with_name("readable.md.metadata.json").write_text(
            json.dumps(
                {
                    "userFacingSurface": "rendered-conversation-document",
                    "sourceRole": "persistence-copy",
                    "externalExportRequested": False,
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        require(not guard.scan_paths([readable]), "readable Markdown with sidecar should pass", failures)

        yaml_doc = active / "yaml-doc.md"
        yaml_doc.write_text("---\ntitle: Demo Brief\nstatus: draft\n---\n\nBody starts here.\n", encoding="utf-8")
        yaml_issues = guard.scan_paths([yaml_doc])
        require(yaml_issues and yaml_issues[0]["kind"] == "leading-frontmatter", "visible YAML frontmatter should fail", failures)
        require(guard.fix_file(yaml_doc), "--fix should modify visible YAML frontmatter", failures)
        fixed_yaml = yaml_doc.read_text(encoding="utf-8")
        require(fixed_yaml.startswith("# Demo Brief\n"), "--fix should make migrated title the H1", failures)
        yaml_sidecar = json.loads(yaml_doc.with_name("yaml-doc.md.metadata.json").read_text(encoding="utf-8"))
        require(yaml_sidecar.get("migratedVisibleMetadata", {}).get("status") == "draft", "--fix should migrate YAML fields", failures)

        kv_doc = active / "key-value-doc.md"
        kv_doc.write_text("Title: Key Value Brief\nStatus: review\n\n# Real Heading\n\nBody.\n", encoding="utf-8")
        kv_issues = guard.scan_paths([kv_doc])
        require(kv_issues and kv_issues[0]["kind"] == "leading-key-value-metadata", "visible key-value metadata should fail", failures)
        require(guard.fix_file(kv_doc), "--fix should modify visible key-value metadata", failures)
        fixed_kv = kv_doc.read_text(encoding="utf-8")
        require(fixed_kv.startswith("# Real Heading\n"), "--fix should preserve existing H1 after stripping key-values", failures)

        json_doc = active / "json-doc.md"
        json_doc.write_text('{"title": "JSON Brief", "status": "draft"}\n\nBody.\n', encoding="utf-8")
        json_issues = guard.scan_paths([json_doc])
        require(json_issues and json_issues[0]["kind"] == "leading-json-metadata", "visible JSON metadata should fail", failures)

        workflow = temp_dir / ".agent" / "workflows" / "demo.md"
        workflow.parent.mkdir(parents=True)
        workflow.write_text("---\ndescription: Demo\n---\n\n# /demo\n", encoding="utf-8")
        require(not guard.scan_paths([workflow]), "workflow frontmatter should be allowed", failures)

        skill = temp_dir / ".agents" / "skills" / "demo" / "SKILL.md"
        skill.parent.mkdir(parents=True)
        skill.write_text("---\nname: demo\ndescription: Demo\n---\n\n# Demo\n", encoding="utf-8")
        require(not guard.scan_paths([skill]), "skill frontmatter should be allowed", failures)

        design = active / "DESIGN.md"
        design.write_text("---\nversion: 1\nname: Demo\n---\n\n# Design\n", encoding="utf-8")
        require(not guard.scan_paths([design]), "DESIGN.md frontmatter should be allowed", failures)
    finally:
        shutil.rmtree(temp_dir)

    if failures:
        print("Markdown readability guard verification FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Markdown readability guard verification PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
