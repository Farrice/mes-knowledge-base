#!/usr/bin/env python3
"""Verify a portable Briefing Room directory or ZIP with stdlib only."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import tempfile
import urllib.parse
import zipfile
from html.parser import HTMLParser
from pathlib import Path


SCHEMA_VERSION = "portable-briefing-room/v1"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def inside(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


class Links(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.values: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        for key in ("href", "src"):
            if data.get(key):
                self.values.append(str(data[key]))


def safe_extract(archive: Path, target: Path) -> None:
    with zipfile.ZipFile(archive) as handle:
        for member in handle.infolist():
            candidate = (target / member.filename).resolve()
            if not inside(candidate, target.resolve()):
                raise ValueError(f"unsafe ZIP member: {member.filename}")
        handle.extractall(target)


def find_bundle(path: Path) -> tuple[Path, tempfile.TemporaryDirectory | None]:
    path = path.expanduser().resolve()
    if path.is_dir() and (path / "manifest.json").is_file():
        return path, None
    if path.is_file() and path.suffix.lower() == ".zip":
        tmp = tempfile.TemporaryDirectory(prefix="brief-export-verify-")
        root = Path(tmp.name)
        safe_extract(path, root)
        manifests = list(root.rglob("manifest.json"))
        if len(manifests) != 1:
            tmp.cleanup()
            raise ValueError(f"ZIP must contain exactly one manifest.json; found {len(manifests)}")
        return manifests[0].parent, tmp
    if path.is_dir():
        manifests = list(path.glob("*/manifest.json"))
        if len(manifests) == 1:
            return manifests[0].parent, None
    raise ValueError(f"not a portable Briefing Room bundle or ZIP: {path}")


def local_target(root: Path, page: Path, value: str) -> Path | None:
    value = value.strip()
    if not value or value.startswith(("#", "http://", "https://", "mailto:", "source-repo://", "data:")):
        return None
    if value.startswith("file://"):
        return Path("/__INVALID_FILE_URI__")
    clean = urllib.parse.unquote(value.split("#", 1)[0].split("?", 1)[0])
    target = (page.parent / clean).resolve()
    if not inside(target, root.resolve()):
        return Path("/__OUTSIDE_BUNDLE__")
    return target


def verify(root: Path) -> tuple[list[str], dict]:
    errors: list[str] = []
    manifest_path = root / "manifest.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return [f"manifest unreadable: {exc}"], {}
    if manifest.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"unsupported schema: {manifest.get('schema_version')!r}")

    recorded = set()
    for row in manifest.get("files", []):
        rel = str(row.get("path") or "")
        target = (root / rel).resolve()
        if not rel or not inside(target, root.resolve()):
            errors.append(f"unsafe manifest path: {rel!r}")
            continue
        recorded.add(rel)
        if not target.is_file():
            errors.append(f"missing file: {rel}")
            continue
        if target.stat().st_size != row.get("bytes"):
            errors.append(f"size mismatch: {rel}")
        if sha256_file(target) != row.get("sha256"):
            errors.append(f"hash mismatch: {rel}")

    actual = {
        path.relative_to(root).as_posix() for path in root.rglob("*")
        if path.is_file() and path.name != "manifest.json"
    }
    for rel in sorted(actual - recorded):
        errors.append(f"unrecorded file: {rel}")
    for rel in sorted(recorded - actual):
        errors.append(f"manifest-only file: {rel}")

    portable_surfaces = [root / "index.html"] + list((root / "briefs").glob("*/*.html"))
    portable_surfaces += list((root / "briefs").glob("*/*-context.json"))
    # Actual file:// hrefs are rejected by local_target below. Do not flag the
    # string when it appears only in explanatory prose or inert JavaScript
    # comments; portability is about behavior and leaked machine paths.
    absolute_pattern = re.compile(r"(?:^|[\"'=\s])/Users/[^/\s]+/|[A-Za-z]:\\\\")
    for path in portable_surfaces:
        if not path.is_file():
            errors.append(f"missing portable surface: {path.relative_to(root)}")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if absolute_pattern.search(text):
            errors.append(f"absolute local path leaked: {path.relative_to(root)}")
        if path.suffix == ".html":
            parser = Links()
            parser.feed(text)
            for value in parser.values:
                target = local_target(root, path, value)
                if target is not None and not target.exists():
                    errors.append(f"broken local link: {path.relative_to(root)} -> {value}")

    if manifest.get("audience") == "private":
        for context_path in (root / "briefs").glob("*/*-context.json"):
            try:
                pack = json.loads(context_path.read_text(encoding="utf-8"))
            except ValueError as exc:
                errors.append(f"context unreadable: {context_path.relative_to(root)}: {exc}")
                continue
            for item in pack.get("paths", []):
                if item.get("abs"):
                    errors.append(f"absolute field retained: {context_path.relative_to(root)}")
                rel = str(item.get("path") or "")
                target = (root / rel).resolve()
                if not inside(target, root.resolve()) or not target.is_file():
                    errors.append(f"broken context path: {context_path.relative_to(root)} -> {rel}")

    return errors, manifest


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify a portable Briefing Room folder or ZIP.")
    parser.add_argument("bundle", nargs="?", default=".")
    args = parser.parse_args()
    tmp = None
    try:
        root, tmp = find_bundle(Path(args.bundle))
        errors, manifest = verify(root)
        if errors:
            print("BRIEF EXPORT VERIFICATION FAIL")
            for error in errors:
                print(f"- {error}")
            return 1
        print("BRIEF EXPORT VERIFICATION PASS")
        print(f"- bundle: {manifest.get('title')} ({manifest.get('audience')})")
        print(f"- briefs: {len(manifest.get('briefs', []))}")
        print(f"- hashed files: {len(manifest.get('files', []))}")
        print(f"- omissions disclosed: {len(manifest.get('omissions', []))}")
        print("- all local links and portable context paths resolve")
        return 0
    except (OSError, ValueError, zipfile.BadZipFile) as exc:
        print(f"BRIEF EXPORT VERIFICATION FAIL\n- {exc}")
        return 1
    finally:
        if tmp is not None:
            tmp.cleanup()


if __name__ == "__main__":
    raise SystemExit(main())
