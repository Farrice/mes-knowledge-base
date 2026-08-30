#!/usr/bin/env python3
"""Deterministic checks for the MyBPM Shopify staging package."""

from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
THEME = ROOT / "theme"
PREVIEW = ROOT / "preview"


class PreviewParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.local_refs: list[str] = []
        self.images = 0
        self.images_without_alt: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"] or "")
        if tag == "img":
            self.images += 1
            if not (values.get("alt") or "").strip():
                self.images_without_alt.append(values.get("src") or "unknown")
        for key in ("href", "src"):
            value = values.get(key) or ""
            if value and not value.startswith(("http://", "https://", "data:", "#", "mailto:", "tel:")):
                self.local_refs.append(value)


def strip_json_comments(text: str) -> str:
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)
    return re.sub(r"^\s*//.*$", "", text, flags=re.MULTILINE)


def parse_json_files(errors: list[str]) -> int:
    count = 0
    for path in sorted(THEME.rglob("*.json")):
        try:
            json.loads(strip_json_comments(path.read_text(encoding="utf-8")))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"JSON: {path.relative_to(ROOT)}: {exc}")
        count += 1
    return count


def parse_liquid_schemas(errors: list[str]) -> int:
    count = 0
    pattern = re.compile(r"{%\s*schema\s*%}(.*?){%\s*endschema\s*%}", re.DOTALL)
    for path in sorted(THEME.rglob("*.liquid")):
        text = path.read_text(encoding="utf-8")
        for match in pattern.finditer(text):
            try:
                json.loads(match.group(1))
            except json.JSONDecodeError as exc:
                errors.append(f"SCHEMA: {path.relative_to(ROOT)}: {exc}")
            count += 1
    return count


def check_required_files(errors: list[str]) -> None:
    required = [
        THEME / "assets/mybpm-premium.css",
        THEME / "sections/mybpm-editorial-hero.liquid",
        THEME / "sections/mybpm-manifesto.liquid",
        THEME / "sections/mybpm-editorial-split.liquid",
        THEME / "sections/mybpm-proof-strip.liquid",
        THEME / "sections/mybpm-collection-hero.liquid",
        THEME / "sections/mybpm-product-notes.liquid",
        THEME / "templates/index.json",
        THEME / "templates/collection.json",
        THEME / "templates/product.json",
        PREVIEW / "index.html",
        PREVIEW / "design-board.html",
        PREVIEW / "preview.css",
        ROOT / "DESIGN.md",
        ROOT / "data/shopify-config-manifest.json",
        ROOT / "06-qa.md",
    ]
    for path in required:
        if not path.is_file():
            errors.append(f"MISSING: {path.relative_to(ROOT)}")


def check_content(errors: list[str]) -> None:
    searchable = []
    for path in list(THEME.rglob("*")) + list(PREVIEW.rglob("*")):
        if (
            path.is_file()
            and path.suffix in {".json", ".liquid", ".css", ".html"}
            and "locales" not in path.parts
        ):
            searchable.append((path, path.read_text(encoding="utf-8", errors="replace")))
    forbidden = [
        r"\bLorem ipsum\b",
        r">\s*Product Name\s*<",
        r"\bTODO\b",
        r"black\.png\?v=2056",
        r"white\.png\?v=2056",
        r"#F1EFE8",
        r"#B7B3AA",
    ]
    for path, text in searchable:
        for term in forbidden:
            if re.search(term, text, flags=re.IGNORECASE):
                errors.append(f"PLACEHOLDER/BROKEN-ASSET: {path.relative_to(ROOT)} matched {term}")

    theme_layout = (THEME / "layout/theme.liquid").read_text(encoding="utf-8")
    if "mybpm-premium.css" not in theme_layout:
        errors.append("WIRING: custom stylesheet is not loaded by layout/theme.liquid")

    product_notes = (THEME / "sections/mybpm-product-notes.liquid").read_text(encoding="utf-8")
    for key in ("product_story", "material", "fit_note", "care", "production_note"):
        if f"custom.{key}" not in product_notes:
            errors.append(f"METAFIELD: product notes does not reference custom.{key}")

    settings = (THEME / "config/settings_data.json").read_text(encoding="utf-8")
    if settings.count('"background": "#FFFFFF"') < 2:
        errors.append("PALETTE: current and default theme backgrounds must both be Signal White")

    css = (THEME / "assets/mybpm-premium.css").read_text(encoding="utf-8")
    if ".mybpm-section--marble" not in css or "--mybpm-mineral: #f7f7f4" not in css:
        errors.append("PALETTE: restrained Mineral White treatment is missing")


def check_preview(errors: list[str]) -> int:
    image_count = 0
    for html_path in sorted(PREVIEW.glob("*.html")):
        parser = PreviewParser()
        html = html_path.read_text(encoding="utf-8")
        parser.feed(html)
        image_count += parser.images
        for ref in parser.local_refs:
            target = (PREVIEW / ref.split("?", 1)[0]).resolve()
            if not target.is_file():
                errors.append(f"PREVIEW LINK: {html_path.name} missing local asset {ref}")
        if parser.images_without_alt:
            errors.append(f"ACCESSIBILITY: {html_path.name} has {len(parser.images_without_alt)} images with empty alt text")
        for anchor in re.findall(r'href="#([^"]+)"', html):
            if anchor not in parser.ids:
                errors.append(f"PREVIEW ANCHOR: {html_path.name} #{anchor} has no target")
    return image_count


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    json_count = parse_json_files(errors)
    schema_count = parse_liquid_schemas(errors)
    check_content(errors)
    preview_images = check_preview(errors)

    print(f"JSON files parsed: {json_count}")
    print(f"Liquid schemas parsed: {schema_count}")
    print(f"Preview images checked: {preview_images}")
    if errors:
        print(f"FAIL ({len(errors)} issue(s))")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: package structure, JSON, Liquid schema JSON, wiring, placeholders, preview links, anchors, and image alt text")
    return 0


if __name__ == "__main__":
    sys.exit(main())
