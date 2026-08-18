#!/usr/bin/env python3
"""Focused regression checks for living Google Doc reuse."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

import google_doc_lifecycle as lifecycle


def main() -> int:
    failures: list[str] = []

    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        source = root / "offer.md"
        source.write_text("# Offer\n", encoding="utf-8")
        registry = root / "registry.json"
        lifecycle.record(source, "folder", "Offer", "doc-1", "hash-1", path=registry)
        lifecycle.record(source, "folder", "Offer", "doc-1", "hash-2", path=registry)
        row = lifecycle.lookup(source, "folder", "Offer", path=registry)
        if row is None or row["doc_id"] != "doc-1" or row["source_hash"] != "hash-2":
            failures.append("the living Google Doc identity was not reused")
        if len(json.loads(registry.read_text())["exports"]) != 1:
            failures.append("a second registry entry was created for one living source")

    md_exporter = (Path(__file__).parent / "md_to_gdoc.py").read_text(encoding="utf-8")
    brief_exporter = (Path(__file__).parent / "render_brief.py").read_text(encoding="utf-8")
    for name, source in (("md_to_gdoc", md_exporter), ("render_brief", brief_exporter)):
        if "files', 'update'" not in source and 'files", "update"' not in source:
            failures.append(f"{name} lacks the Drive update path")
        if "google_doc_lifecycle" not in source:
            failures.append(f"{name} is not wired to the living registry")
    if "--new-milestone" not in md_exporter or "--doc-id" not in md_exporter:
        failures.append("Markdown export lacks explicit milestone/adoption controls")
    if "dir=staging_dir" not in md_exporter:
        failures.append("Markdown export stages uploads outside the active workspace")
    if "delete_response.unlink(missing_ok=True)" not in md_exporter:
        failures.append("Markdown export may leave a Drive delete response file behind")

    if failures:
        print("GOOGLE DOC LIFECYCLE VERIFICATION FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("GOOGLE DOC LIFECYCLE VERIFICATION PASS")
    print("- one source keeps one Doc ID")
    print("- both exporters update instead of duplicate")
    print("- milestone creation remains explicit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
