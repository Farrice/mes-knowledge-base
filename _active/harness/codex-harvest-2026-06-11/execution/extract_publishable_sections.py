#!/usr/bin/env python3
"""Extract marked publishable copy sections from Markdown source files."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


SECTION_RE = re.compile(
    r"<!--\s*publishable:(?P<name>[a-z0-9_-]+):start\s*-->\s*(?P<body>.*?)\s*<!--\s*publishable:(?P=name):end\s*-->",
    re.IGNORECASE | re.DOTALL,
)


def extract(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    return {match.group("name"): match.group("body").strip() for match in SECTION_RE.finditer(text)}


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract publishable sections from Markdown files.")
    parser.add_argument("files", nargs="+", help="Markdown files to scan.")
    parser.add_argument("--section", help="Only output one section name.")
    parser.add_argument("--output-dir", help="Write extracted sections as .txt files.")
    parser.add_argument("--json", action="store_true", help="Emit JSON map instead of plain text.")
    args = parser.parse_args()

    sections: dict[str, str] = {}
    for file_name in args.files:
        path = Path(file_name)
        for name, body in extract(path).items():
            key = name
            if key in sections:
                key = f"{path.stem}-{name}"
            sections[key] = body

    if args.section:
        sections = {args.section: sections[args.section]} if args.section in sections else {}

    if args.output_dir:
        output_dir = Path(args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        for name, body in sections.items():
            (output_dir / f"{name}.txt").write_text(body + "\n", encoding="utf-8")

    if args.json:
        print(json.dumps(sections, indent=2))
    elif not args.output_dir:
        for name, body in sections.items():
            print(f"## {name}\n")
            print(body)
            print()
    else:
        print(json.dumps({"written": sorted(sections)}, indent=2))

    return 0 if sections else 1


if __name__ == "__main__":
    raise SystemExit(main())
