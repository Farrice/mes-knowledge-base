#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Mechanical migration utility: add data-slot="NAME" to existing template.html zones.

A zone is any element whose content is a single Mustache placeholder (text zone,
e.g. <div class="kicker">{{KICKER}}</div> or <span>{{TITLE_ACCENT}}</span>), or a
<div> wrapping a media element with a placeholder attribute (image zone, e.g.
<div class="photo-zone"><img src="{{PHOTO_MAIN_PATH}}"></div>). The handle is
inferred from that placeholder - the same recognition logic render_template.py
uses in substitute(). Image slot keys have trailing _PATH / _HTML / _SRC suffixes
stripped to produce the handle (e.g. PHOTO_MAIN_PATH -> PHOTO_MAIN).

Running the script twice on the same file is safe: zones that already carry
data-slot are left untouched (idempotent).

Usage:
    # Single file
    uv run migrate_data_slots.py --template path/to/template.html

    # All template.html files under a pool directory
    uv run migrate_data_slots.py --pool-dir path/to/templates/pool-name/

    # Preview without writing
    uv run migrate_data_slots.py --template path/to/template.html --dry-run
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Mustache placeholder recognition - mirrors render_template.py substitute()
# Triple-brace {{{NAME}}} handled by the outer pattern; double-brace {{NAME}}
# by the inner pattern.  Both use the same [A-Z][A-Z0-9_]* capture group.
# ---------------------------------------------------------------------------
_MUSTACHE_RE = re.compile(
    r"\{\{\{?\s*([A-Z][A-Z0-9_]*)\s*\}?\}\}"
)

# Suffixes to strip from image/path slot keys to produce the handle.
_STRIP_SUFFIXES: tuple[str, ...] = ("_PATH", "_HTML", "_SRC")

# An attribute run inside an opening tag: quoted strings may contain '>', so
# consume balanced quotes or any non-quote/non-'>' char (lazy).
_ATTRS = r'(?:"[^"]*"|\'[^\']*\'|[^>"\'])*?'

# Text zone: ANY element whose entire content is a single Mustache placeholder,
# e.g. <div class="kicker">{{KICKER}}</div> or
# <span class="title-accent">{{TITLE_ACCENT}}</span>. This generalises beyond
# the legacy class="zone" convention so real template families (semantic class
# names, spans, headings) are covered — the innermost wrapping element is the
# editable/positioned zone and receives the handle.
_TEXT_ZONE_RE = re.compile(
    r'<(?P<tag>[a-zA-Z][\w-]*)(?P<attrs>' + _ATTRS + r')>'
    r'(?P<inner>\s*\{\{\{?\s*[A-Z][A-Z0-9_]*\s*\}?\}\}\s*)'
    r'</(?P=tag)>',
    re.DOTALL,
)

# Image/media zone: a <div> directly wrapping a single media element whose
# attribute (src/srcset/data-src) carries a placeholder, e.g.
# <div class="bg photo-zone"><img src="{{PHOTO_MAIN_PATH}}"></div>. The
# positioned wrapper div receives the (suffix-stripped) handle.
_IMAGE_ZONE_RE = re.compile(
    r'<div(?P<attrs>' + _ATTRS + r')>'
    r'(?P<inner>\s*<(?:img|video|picture|source)\b[^>]*?'
    r'(?:src|srcset|data-src)\s*=\s*"[^"]*\{\{\{?\s*[A-Z][A-Z0-9_]*\s*\}?\}\}[^"]*"'
    r'[^>]*?>\s*)'
    r'</div>',
    re.DOTALL,
)

# More strict check: does this opening tag already carry data-slot?
_HAS_DATA_SLOT_RE = re.compile(r'\bdata-slot\s*=')

# Every data-slot handle already present anywhere in the document — one handle is
# ONE zone, so a handle that is already claimed (typically by an ANCESTOR container,
# e.g. <div class="bottom-pill" data-slot="CALLOUT_TEXT"> wrapping the placeholder's
# own element) must never be stamped a second time (r5f F1a sibling a). A duplicated
# handle makes the editor and the bake target two elements for one zone: text edits
# wipe the container's styled children and box tweaks apply twice.
_DATA_SLOT_VALUE_RE = re.compile(r'\bdata-slot\s*=\s*"([^"]+)"')


def infer_handle(zone_inner_html: str) -> str | None:
    """Return the stable slot handle for a zone, or None if no placeholder found.

    Finds the FIRST Mustache placeholder in *zone_inner_html* and strips
    trailing _PATH / _HTML / _SRC suffixes from the captured key.

    >>> infer_handle('{{{HERO}}}')
    'HERO'
    >>> infer_handle('<img src="{{PHOTO_MAIN_PATH}}">')
    'PHOTO_MAIN'
    >>> infer_handle('<span>no placeholder here</span>')
    """
    match = _MUSTACHE_RE.search(zone_inner_html)
    if not match:
        return None
    name = match.group(1)
    for suffix in _STRIP_SUFFIXES:
        if name.endswith(suffix):
            name = name[: -len(suffix)]
            break
    return name


def migrate(html_text: str) -> tuple[str, int]:
    """Inject data-slot="HANDLE" into every editable zone that lacks it.

    Tags two shapes (generalised beyond the legacy class="zone" convention):
      * text zones  - any element whose entire content is a single Mustache
        placeholder, e.g. <div class="kicker">{{KICKER}}</div> or
        <span class="title-accent">{{TITLE_ACCENT}}</span>;
      * image zones - a <div> wrapping a media element whose attribute carries
        a placeholder, e.g. <div class="photo-zone"><img src="{{PHOTO_MAIN_PATH}}"></div>.

    Returns (new_html, count_added).  Elements that already carry data-slot are
    left untouched, so migrate() is idempotent.  A handle that is ALREADY claimed
    anywhere in the document (e.g. by an ancestor container authored with
    data-slot="X" wrapping the placeholder's own element) is never stamped again —
    duplicated handles are the container-slot defect (r5f F1a sibling a).
    """
    count = 0
    # Handles already claimed — seeded from the document, grown as we stamp so a
    # handle stamped earlier in this same run also blocks later duplicates.
    claimed: set[str] = set(_DATA_SLOT_VALUE_RE.findall(html_text))

    def _inject_div(m: "re.Match[str]") -> str:
        nonlocal count
        attrs = m.group("attrs")
        if _HAS_DATA_SLOT_RE.search(attrs):
            return m.group(0)
        handle = infer_handle(m.group("inner"))
        if handle is None or handle in claimed:
            return m.group(0)
        count += 1
        claimed.add(handle)
        return f'<div data-slot="{handle}"{attrs}>{m.group("inner")}</div>'

    def _inject_text(m: "re.Match[str]") -> str:
        nonlocal count
        attrs = m.group("attrs")
        if _HAS_DATA_SLOT_RE.search(attrs):
            return m.group(0)
        handle = infer_handle(m.group("inner"))
        if handle is None or handle in claimed:
            return m.group(0)
        count += 1
        claimed.add(handle)
        tag = m.group("tag")
        return f'<{tag} data-slot="{handle}"{attrs}>{m.group("inner")}</{tag}>'

    # Image zones first, so the wrapper div is tagged before the text pass runs.
    html_text = _IMAGE_ZONE_RE.sub(_inject_div, html_text)
    html_text = _TEXT_ZONE_RE.sub(_inject_text, html_text)
    return html_text, count


def _migrate_file(path: Path, dry_run: bool) -> int:
    """Migrate a single file.  Returns the count of slots added."""
    original = path.read_text(encoding="utf-8")
    new_html, count = migrate(original)

    if count == 0:
        print(f"  migrated 0 zones in {path}  (already up to date)")
        return 0

    if dry_run:
        print(f"  [dry-run] would add {count} data-slot attribute(s) in {path}")
    else:
        path.write_text(new_html, encoding="utf-8")
        print(f"  migrated {count} zone(s) in {path}")

    return count


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Add data-slot attributes to zone divs in template.html files.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument(
        "--template",
        metavar="FILE",
        type=Path,
        help="Path to a single template.html to migrate.",
    )
    source.add_argument(
        "--pool-dir",
        metavar="DIR",
        type=Path,
        help="Root directory to search recursively for template.html files.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would change without writing any file.",
    )
    args = parser.parse_args()

    files: list[Path]
    if args.template:
        if not args.template.is_file():
            parser.error(f"File not found: {args.template}")
        files = [args.template]
    else:
        if not args.pool_dir.is_dir():
            parser.error(f"Directory not found: {args.pool_dir}")
        files = sorted(args.pool_dir.rglob("template.html"))
        if not files:
            print(f"No template.html files found under {args.pool_dir}")
            return

    total_added = 0
    for f in files:
        total_added += _migrate_file(f, dry_run=args.dry_run)

    if args.dry_run:
        print(f"\n[dry-run] total: {total_added} data-slot attribute(s) would be added across {len(files)} file(s).")
    else:
        print(f"\nDone. Added {total_added} data-slot attribute(s) across {len(files)} file(s).")


if __name__ == "__main__":
    main()
