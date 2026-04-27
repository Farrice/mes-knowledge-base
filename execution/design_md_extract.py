#!/usr/bin/env python3
"""
Extract a DESIGN.md scaffold from a codebase or remote URL.

Two modes:
    codebase  — read tailwind.config / theme files / globals.css
    url       — fetch a page and harvest computed styles (requires Playwright MCP, called from Claude)

This script handles the codebase mode end-to-end. The URL mode is exposed as a
shell helper that prepares the harvest payload — actual browser navigation
runs through Playwright MCP from the Claude conversation.

Usage:
    python3 execution/design_md_extract.py codebase /path/to/project [--out DESIGN.md]
    python3 execution/design_md_extract.py codebase /path/to/project --to-stdout
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


def find_styling_target(project_root: Path) -> tuple[str, Path | None]:
    """Return (system_name, primary_config_path)."""
    candidates = [
        ("tailwind", "tailwind.config.ts"),
        ("tailwind", "tailwind.config.js"),
        ("tailwind", "tailwind.config.mjs"),
        ("tailwind", "tailwind.config.cjs"),
        ("panda", "panda.config.ts"),
        ("panda", "panda.config.js"),
        ("unocss", "unocss.config.ts"),
        ("unocss", "unocss.config.js"),
        ("css-vars", "src/styles/globals.css"),
        ("css-vars", "src/app.css"),
        ("css-vars", "styles/globals.css"),
        ("css-vars", "app/globals.css"),
    ]
    for system, rel in candidates:
        path = project_root / rel
        if path.exists():
            return system, path
    return "unknown", None


def extract_from_tailwind(config_path: Path) -> dict[str, Any]:
    """Naive extraction of theme.extend.colors / fontSize / borderRadius / spacing.

    Doesn't actually evaluate JS/TS; uses regex to pull obvious patterns.
    For complex configs, the user should hand-edit afterward.
    """
    text = config_path.read_text()
    extracted: dict[str, Any] = {"colors": {}, "typography": {}, "rounded": {}, "spacing": {}}

    # Find the theme.extend or theme block
    m = re.search(r"theme\s*:\s*\{(.+?)\n\s*\}\s*[,)]", text, re.S)
    block = m.group(1) if m else text

    # Extract colors object
    cm = re.search(r"colors\s*:\s*\{([^}]+(?:\{[^}]*\}[^}]*)*)\}", block, re.S)
    if cm:
        for k, v in re.findall(r"['\"]?([a-zA-Z0-9\-_]+)['\"]?\s*:\s*['\"](#[0-9a-fA-F]{3,8})['\"]", cm.group(1)):
            extracted["colors"][k] = v

    # Extract fontSize
    fm = re.search(r"fontSize\s*:\s*\{([^}]+(?:\{[^}]*\}[^}]*)*)\}", block, re.S)
    if fm:
        for line in fm.group(1).split("\n"):
            n = re.search(r"['\"]?([a-zA-Z0-9\-_]+)['\"]?\s*:\s*\[?\s*['\"]([0-9.]+(?:px|rem|em))['\"]", line)
            if n:
                extracted["typography"][n.group(1)] = {
                    "fontFamily": "system-ui, sans-serif",
                    "fontSize": n.group(2),
                }

    # borderRadius → rounded
    bm = re.search(r"borderRadius\s*:\s*\{([^}]+)\}", block, re.S)
    if bm:
        for k, v in re.findall(r"['\"]?([a-zA-Z0-9\-_]+)['\"]?\s*:\s*['\"]([^'\"]+)['\"]", bm.group(1)):
            extracted["rounded"][k] = v

    # spacing
    sm = re.search(r"spacing\s*:\s*\{([^}]+)\}", block, re.S)
    if sm:
        for k, v in re.findall(r"['\"]?([a-zA-Z0-9\-_]+)['\"]?\s*:\s*['\"]([^'\"]+)['\"]", sm.group(1)):
            extracted["spacing"][k] = v

    return extracted


def extract_from_css_vars(css_path: Path) -> dict[str, Any]:
    """Read CSS custom properties from :root."""
    text = css_path.read_text()
    extracted: dict[str, Any] = {"colors": {}, "typography": {}, "rounded": {}, "spacing": {}}

    rm = re.search(r":root\s*\{([^}]+)\}", text, re.S)
    if not rm:
        return extracted

    for line in rm.group(1).split("\n"):
        m = re.match(r"\s*--([a-z0-9\-]+)\s*:\s*([^;]+);?", line)
        if not m:
            continue
        var_name = m.group(1).strip()
        value = m.group(2).strip()
        if var_name.startswith("color-") or var_name.startswith("c-"):
            key = var_name.replace("color-", "").replace("c-", "")
            if value.startswith("#"):
                extracted["colors"][key] = value
        elif var_name.startswith("space-") or var_name.startswith("spacing-"):
            key = re.sub(r"^(space|spacing)-", "", var_name)
            extracted["spacing"][key] = value
        elif var_name.startswith("radius-") or var_name.startswith("rounded-"):
            key = re.sub(r"^(radius|rounded)-", "", var_name)
            extracted["rounded"][key] = value
        elif var_name.startswith("text-") or var_name.startswith("font-size-"):
            key = re.sub(r"^(text|font-size)-", "", var_name)
            extracted["typography"][key] = {
                "fontFamily": "system-ui, sans-serif",
                "fontSize": value,
            }

    return extracted


def compose_design_md(name: str, extracted: dict[str, Any], source_note: str) -> str:
    """Compose a DESIGN.md draft from extracted tokens."""
    lines = ["---", f"name: {name}", "description: Auto-extracted from existing project; refine description after review."]

    if extracted.get("colors"):
        lines.append("\ncolors:")
        for k, v in extracted["colors"].items():
            lines.append(f"  {k}: \"{v}\"")
    if extracted.get("typography"):
        lines.append("\ntypography:")
        for k, v in extracted["typography"].items():
            lines.append(f"  {k}:")
            for tk, tv in v.items():
                lines.append(f"    {tk}: \"{tv}\"")
    if extracted.get("rounded"):
        lines.append("\nrounded:")
        for k, v in extracted["rounded"].items():
            lines.append(f"  {k}: {v}")
    if extracted.get("spacing"):
        lines.append("\nspacing:")
        for k, v in extracted["spacing"].items():
            lines.append(f"  {k}: {v}")

    lines.append("---\n")
    lines.append(f"<!-- {source_note} -->\n")
    lines.append("## Overview\n\n*TODO: write the brand description. Don't say 'modern, clean'. Name the cultural anchor and the tension.*\n")
    lines.append("## Colors\n\n*TODO: explain the role of each color palette. Use descriptive names.*\n")
    lines.append("## Typography\n\n*TODO: explain the role of each typography level and the font choices.*\n")
    lines.append("## Layout\n\n*TODO: describe the grid, spacing rhythm, density philosophy.*\n")
    lines.append("## Elevation & Depth\n\n*TODO: shadow strategy or flat-design alternative.*\n")
    lines.append("## Shapes\n\n*TODO: corner-radius philosophy, geometric register.*\n")
    lines.append("## Components\n\n*TODO: per-component style rules. Build out via component-build workflow.*\n")
    lines.append("## Do's and Don'ts\n\n- Do *(specific rule)*\n- Don't *(specific anti-pattern)*\n")

    return "\n".join(lines)


def cmd_codebase(args) -> int:
    project_root = Path(args.project_root).resolve()
    if not project_root.is_dir():
        sys.stderr.write(f"ERROR: not a directory: {project_root}\n")
        return 2

    system, config_path = find_styling_target(project_root)
    if not config_path:
        sys.stderr.write(f"ERROR: no recognized styling system found in {project_root}.\n")
        sys.stderr.write("  Looked for: tailwind.config.{ts,js}, panda.config.ts, src/styles/globals.css\n")
        return 1

    print(f"Detected: {system} → {config_path.relative_to(project_root)}", file=sys.stderr)

    if system == "tailwind":
        extracted = extract_from_tailwind(config_path)
    elif system == "css-vars":
        extracted = extract_from_css_vars(config_path)
    else:
        sys.stderr.write(f"ERROR: extraction for '{system}' not yet implemented.\n")
        return 1

    name = project_root.name.replace("-", " ").replace("_", " ").title()
    source_note = f"Extracted from {config_path.relative_to(project_root)} on $(date)"
    md = compose_design_md(name, extracted, source_note)

    if args.to_stdout:
        print(md)
        return 0

    out = Path(args.out).resolve()
    if out.exists() and not args.force:
        sys.stderr.write(f"ERROR: {out} already exists. Pass --force to overwrite.\n")
        return 1
    out.write_text(md)
    print(f"\n✓ Wrote {out}", file=sys.stderr)
    print("\nNext steps:", file=sys.stderr)
    print(f"  1. Edit the markdown body — fill in the TODOs", file=sys.stderr)
    print(f"  2. Validate: python3 execution/design_md_validate.py {out}", file=sys.stderr)
    print(f"  3. Build components: see skills/product-design-build/", file=sys.stderr)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract DESIGN.md from a codebase.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_cb = sub.add_parser("codebase", help="Extract from project source files")
    p_cb.add_argument("project_root")
    p_cb.add_argument("--out", default="./DESIGN.md")
    p_cb.add_argument("--to-stdout", action="store_true")
    p_cb.add_argument("--force", action="store_true")

    args = parser.parse_args()

    if args.cmd == "codebase":
        return cmd_codebase(args)
    return 2


if __name__ == "__main__":
    sys.exit(main())
