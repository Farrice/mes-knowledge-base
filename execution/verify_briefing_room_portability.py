#!/usr/bin/env python3
"""Regression proof for Briefing Room cards and context packs across worktrees."""

from __future__ import annotations

import tempfile
from pathlib import Path

import brief_library as library
import render_brief as renderer


def check_context_pack_contract() -> None:
    pack = renderer.build_context_pack(
        {
            "slug": "portable-fixture",
            "title": "portable fixture",
            "context": [{"path": "execution/brief_library.py", "role": "fixture"}],
            "sections": [],
        }
    )
    item = pack["paths"][0]
    assert item["path"] == "execution/brief_library.py", item
    assert item["scope"] == "repo", item
    assert pack["path_policy"]["canonical_field"] == "path", pack["path_policy"]
    assert "render-time hint" in pack["path_policy"]["absolute_semantics"]


def check_resolution_order() -> None:
    original_root = library.ROOT
    original_canonical = library.CANONICAL_ROOT
    try:
        with tempfile.TemporaryDirectory(prefix="brief-portability-") as tmp:
            base = Path(tmp)
            active = base / "lane"
            canonical = base / "main"
            active.mkdir()
            canonical.mkdir()

            active_file = active / "tracked" / "brief.md"
            active_file.parent.mkdir()
            active_file.write_text("lane", encoding="utf-8")

            main_media = canonical / "media" / "clip.mp4"
            main_media.parent.mkdir()
            main_media.write_bytes(b"fixture")

            library.ROOT = active
            library.CANONICAL_ROOT = canonical

            stale_abs = str(base / "deleted-worktree" / "tracked" / "brief.md")
            assert library.resolve_context_path(
                {"path": "tracked/brief.md", "scope": "repo", "abs": stale_abs}
            ) == active_file.resolve()
            assert library.resolve_context_path(
                {"path": "media/clip.mp4", "scope": "repo", "abs": stale_abs}
            ) == main_media.resolve()
            assert library.resolve_context_path(
                {
                    "path": "missing/in-active-and-main.md",
                    "scope": "repo",
                    "abs": str(active_file.resolve()),
                }
            ) is None
    finally:
        library.ROOT = original_root
        library.CANONICAL_ROOT = original_canonical


def main() -> int:
    check_context_pack_contract()
    check_resolution_order()
    errors = library.verify_room()
    assert not errors, "\n".join(errors)
    print("BRIEFING ROOM PORTABILITY VERIFICATION PASS")
    print("- generated context packs use repo-relative canonical paths")
    print("- active checkout outranks stale absolute hints")
    print("- canonical main recovers main-only media")
    print("- missing repo targets are not masked by an unrelated absolute file")
    print("- current card routes resolve")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
