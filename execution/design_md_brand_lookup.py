#!/usr/bin/env python3
"""
Search and import brand DESIGN.md files from the local library at
knowledge/design-libraries/brands/.

Falls back to upstream `npx getdesign@latest add <slug>` if a brand isn't
local.

Usage:
    python3 execution/design_md_brand_lookup.py list
    python3 execution/design_md_brand_lookup.py search "minimal dev tools"
    python3 execution/design_md_brand_lookup.py info <slug>
    python3 execution/design_md_brand_lookup.py use <slug> [--to ./DESIGN.md]
    python3 execution/design_md_brand_lookup.py fetch <slug>   # from upstream
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIB_DIR = ROOT / "knowledge" / "design-libraries"
BRANDS_DIR = LIB_DIR / "brands"
MANIFEST = LIB_DIR / "manifest.json"


def load_manifest() -> list[dict]:
    if not MANIFEST.exists():
        sys.stderr.write(f"ERROR: manifest not found at {MANIFEST}.\n")
        sys.stderr.write("Regenerate with: python3 -c \"from execution.design_md_brand_lookup import _rebuild_manifest; _rebuild_manifest()\"\n")
        sys.exit(2)
    return json.loads(MANIFEST.read_text())


def cmd_list(args) -> int:
    entries = load_manifest()
    print(f"\n{len(entries)} brand DESIGN.md files in library:\n")
    print(f"{'SLUG':<20} {'NAME':<28} DESCRIPTION")
    print("-" * 100)
    for e in entries:
        desc = e["description"][:60]
        if len(e["description"]) > 60:
            desc += "…"
        print(f"{e['slug']:<20} {e['name'][:28]:<28} {desc}")
    print()
    return 0


def cmd_search(args) -> int:
    query = args.query.lower()
    terms = [t for t in re.split(r"\s+", query) if t]
    entries = load_manifest()
    scored = []
    for e in entries:
        haystack = (e["name"] + " " + e["description"] + " " + e["slug"]).lower()
        score = sum(1 for t in terms if t in haystack)
        if score:
            scored.append((score, e))
    scored.sort(key=lambda x: (-x[0], x[1]["slug"]))
    if not scored:
        print(f"\nNo matches for '{args.query}'.\n")
        print("Try `list` to see all brands, or `fetch <slug>` to pull from upstream.\n")
        return 1
    print(f"\n{len(scored)} matches for '{args.query}':\n")
    for score, e in scored[:10]:
        desc = e["description"][:80]
        if len(e["description"]) > 80:
            desc += "…"
        print(f"  [{score}] {e['slug']:<20} — {e['name']}")
        print(f"      {desc}")
        print()
    return 0


def cmd_info(args) -> int:
    entries = load_manifest()
    match = next((e for e in entries if e["slug"] == args.slug), None)
    if not match:
        sys.stderr.write(f"ERROR: brand '{args.slug}' not in local library.\n")
        sys.stderr.write(f"Try: python3 {sys.argv[0]} fetch {args.slug}\n")
        return 1
    print(f"\n{match['name']}")
    print(f"  Slug:        {match['slug']}")
    print(f"  Path:        {match['path']}")
    print(f"  Format:      {match.get('format', 'unknown')}")
    print(f"  Description: {match['description']}")

    path = ROOT / match["path"]
    if path.exists():
        line_count = sum(1 for _ in open(path))
        size_kb = path.stat().st_size / 1024
        print(f"  Size:        {line_count} lines ({size_kb:.1f} KB)")
    if match.get("format") == "legacy-prose":
        print(f"\n  Note: This is the legacy descriptive-prose format. Usable as agent reference,")
        print(f"        but does not have YAML tokens and won't validate with `npx @google/design.md lint`.")
        print(f"        For lint-clean import, run `fetch {match['slug']} --force` to refresh, or")
        print(f"        manually convert to YAML+markdown per the spec at github.com/google-labs-code/design.md")
    print()
    return 0


def cmd_use(args) -> int:
    entries = load_manifest()
    match = next((e for e in entries if e["slug"] == args.slug), None)
    if not match:
        sys.stderr.write(f"ERROR: brand '{args.slug}' not in local library.\n")
        sys.stderr.write(f"Try: python3 {sys.argv[0]} fetch {args.slug}\n")
        return 1
    src = ROOT / match["path"]
    dst = Path(args.to).resolve()
    if dst.exists() and not args.force:
        sys.stderr.write(f"ERROR: {dst} already exists. Pass --force to overwrite.\n")
        return 1
    dst.parent.mkdir(parents=True, exist_ok=True)
    content = src.read_text()
    # Add attribution comment at top of markdown body (after YAML front matter)
    if content.startswith("---"):
        end = content.find("\n---", 3)
        if end != -1:
            insert_at = content.find("\n", end + 4) + 1
            attribution = f"\n<!-- Customized from knowledge/design-libraries/brands/{match['slug']}/DESIGN.md (getdesign.md, MIT license) -->\n"
            content = content[:insert_at] + attribution + content[insert_at:]
    dst.write_text(content)
    print(f"\n✓ Imported {match['name']} → {dst}")
    print(f"\nNext steps:")
    print(f"  1. Customize at minimum: name, description, one signature element")
    print(f"  2. Validate: python3 execution/design_md_validate.py {dst}")
    print(f"  3. Build components: see skills/product-design-build/")
    print()
    return 0


def cmd_fetch(args) -> int:
    if not shutil.which("npx"):
        sys.stderr.write("ERROR: `npx` not found. Install Node.js to fetch from upstream.\n")
        return 2
    slug = args.slug
    folder_slug = slug.replace(".", "-")
    target_dir = BRANDS_DIR / folder_slug
    if target_dir.exists() and not args.force:
        sys.stderr.write(f"ERROR: {target_dir} already exists. Pass --force to refresh.\n")
        return 1

    # getdesign CLI fails on paths with spaces. Use a /tmp staging dir.
    with tempfile.TemporaryDirectory(dir="/tmp") as tmpdir:
        try:
            subprocess.run(
                ["npx", "-y", "getdesign@latest", "add", slug],
                cwd=tmpdir,
                check=True,
                capture_output=True,
                timeout=60,
            )
        except subprocess.CalledProcessError as e:
            sys.stderr.write(f"ERROR: getdesign failed for slug '{slug}'.\n")
            sys.stderr.write(f"  stderr: {e.stderr.decode()[:500]}\n")
            return 1
        except subprocess.TimeoutExpired:
            sys.stderr.write("ERROR: getdesign timed out.\n")
            return 2

        src = Path(tmpdir) / "DESIGN.md"
        if not src.exists():
            sys.stderr.write(f"ERROR: getdesign claimed success but no DESIGN.md was produced.\n")
            return 1
        target_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy(src, target_dir / "DESIGN.md")

    print(f"\n✓ Fetched {slug} → {target_dir / 'DESIGN.md'}")
    print(f"\nRun `python3 {sys.argv[0]} use {folder_slug}` to import into a project.")
    print(f"Re-run manifest rebuild: python3 -c 'from execution.design_md_brand_lookup import _rebuild_manifest; _rebuild_manifest()'")
    print()
    return 0


def _rebuild_manifest() -> None:
    """Rebuild manifest.json + INDEX.md from the brands/ directory. Idempotent.

    Detects format: 'spec-v1' (YAML front matter, official spec) vs 'legacy-prose'
    (descriptive-prose-only, pre-Apr-2026). Both are usable by agents but spec-v1
    files validate cleanly with `npx @google/design.md lint`.
    """
    entries = []
    for slug_dir in sorted(BRANDS_DIR.iterdir()):
        if not slug_dir.is_dir():
            continue
        path = slug_dir / "DESIGN.md"
        if not path.exists():
            continue
        text = path.read_text()
        head = text[:3000]

        # Format detection: YAML front matter present?
        if text.startswith("---\n") or text.startswith("---\r\n"):
            fmt = "spec-v1"
            name_m = re.search(r"^name:\s*(.+)$", head, re.M)
            desc_m = re.search(r"^description:\s*(.+?)(?=\n[a-z\-]+:|\n---)", head, re.M | re.S)
            name = name_m.group(1).strip() if name_m else slug_dir.name
            desc = desc_m.group(1).strip().replace("\n", " ") if desc_m else "(no description)"
        else:
            fmt = "legacy-prose"
            # First H1 is the name
            name_m = re.search(r"^#\s+(.+?)$", head, re.M)
            name = name_m.group(1).strip() if name_m else slug_dir.name
            # Strip "Design System Inspired by " prefix if present
            name = re.sub(r"^Design System Inspired by\s+", "", name)
            # Description: first prose paragraph after the first H2
            desc_m = re.search(r"^##\s+[^\n]+\n+([^\n#].+?)(?=\n\n|\n##)", head, re.M | re.S)
            desc = desc_m.group(1).strip().replace("\n", " ") if desc_m else "(legacy prose format)"

        desc = re.sub(r"\s+", " ", desc)[:300]
        entries.append({
            "slug": slug_dir.name,
            "name": name,
            "description": desc,
            "format": fmt,
            "path": str(path.relative_to(ROOT)),
        })
    MANIFEST.write_text(json.dumps(entries, indent=2))
    spec_v1 = sum(1 for e in entries if e.get("format") == "spec-v1")
    legacy = sum(1 for e in entries if e.get("format") == "legacy-prose")
    print(f"Wrote manifest.json with {len(entries)} entries ({spec_v1} spec-v1, {legacy} legacy-prose).")


def main() -> int:
    parser = argparse.ArgumentParser(description="Search and import brand DESIGN.md files.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("list", help="List all brands in the local library")

    p_search = sub.add_parser("search", help="Search brands by keyword")
    p_search.add_argument("query")

    p_info = sub.add_parser("info", help="Show details for one brand")
    p_info.add_argument("slug")

    p_use = sub.add_parser("use", help="Import a brand as project starter")
    p_use.add_argument("slug")
    p_use.add_argument("--to", default="./DESIGN.md", help="Output path (default: ./DESIGN.md)")
    p_use.add_argument("--force", action="store_true", help="Overwrite existing file")

    p_fetch = sub.add_parser("fetch", help="Fetch a brand from upstream getdesign.md")
    p_fetch.add_argument("slug")
    p_fetch.add_argument("--force", action="store_true", help="Refresh even if local exists")

    sub.add_parser("rebuild-manifest", help="Regenerate manifest.json from brand files")

    args = parser.parse_args()

    handlers = {
        "list": cmd_list,
        "search": cmd_search,
        "info": cmd_info,
        "use": cmd_use,
        "fetch": cmd_fetch,
        "rebuild-manifest": lambda _a: (_rebuild_manifest(), 0)[1],
    }
    return handlers[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
