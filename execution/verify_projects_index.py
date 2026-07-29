#!/usr/bin/env python3
"""verify_projects_index.py — assert the project-status stamp survives its guards.

WHY THIS EXISTS: `status:` is in artifact_frontmatter_guard.VISIBLE_METADATA_KEYS
and `_active` is in its DEFAULT_PATHS, so a project-root INDEX.md carrying a
lifecycle stamp is only legal because of one exemption
(`is_project_root_index`). Remove that exemption in a refactor — or add a new
colliding key — and every stamp starts silently vanishing on the next
`--fix` run, while `artifact_router verify` goes red and blocks filer runs.
Nothing else would notice. This makes the fleet go red that day instead.

Round-trips a real stamp through the real scanner on a throwaway path.

Exit 0 = PASS, 1 = FAIL.
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import artifact_frontmatter_guard as guard  # noqa: E402
import projects_index  # noqa: E402

STAMP = "---\nstatus: active\nentry: 04-deliverables/x.md\n---\n\n# Fixture\n\nbody\n"


def main() -> int:
    failures: list[str] = []

    # 1. The exemption predicate covers exactly the project-root surface.
    for rel, expected in (
        ("_active/fixture-project/INDEX.md", True),
        ("projects/fixture-project/INDEX.md", True),
        ("_active/fixture-project/voice/INDEX.md", False),
        ("deliverables/fixture/INDEX.md", False),
        ("_active/fixture-project/NOTES.md", False),
    ):
        got = guard.is_project_root_index(Path(rel))
        if got != expected:
            failures.append(f"is_project_root_index({rel}) == {got}, expected {expected}")

    # 2. Round-trip: a stamped project-root INDEX.md must scan clean.
    with tempfile.TemporaryDirectory() as tmp:
        proj = Path(tmp) / "_active" / "fixture-project"
        proj.mkdir(parents=True)
        index = proj / "INDEX.md"
        index.write_text(STAMP, encoding="utf-8")
        issues = guard.scan_paths([index])
        if issues:
            failures.append(
                f"stamped project-root INDEX.md flagged by the frontmatter guard "
                f"({len(issues)} issue(s)) — the exemption is gone, stamps will be "
                f"stripped by --fix: {issues[0]}"
            )

        # 3. And the generator must actually read that stamp back.
        stamp = projects_index.read_stamp(index)
        if stamp.get("status") != "active":
            failures.append(f"read_stamp did not recover status: got {stamp!r}")
        if stamp.get("entry") != "04-deliverables/x.md":
            failures.append(f"read_stamp did not recover entry: got {stamp!r}")

    # 4. The path exemption must be narrow: a nested INDEX.md carrying NON-canon
    #    metadata is still guarded. (Canon-vocabulary frontmatter is legitimately
    #    allowed at any depth — that's is_canon_frontmatter's job, tested below —
    #    so this fixture must use real document metadata to probe the path rule.)
    polluted = "---\nauthor: Someone\ndate: 2026-01-01\ndomain: Brand\n---\n\n# Doc\n"
    with tempfile.TemporaryDirectory() as tmp:
        deep = Path(tmp) / "_active" / "fixture-project" / "sub" / "INDEX.md"
        deep.parent.mkdir(parents=True)
        deep.write_text(polluted, encoding="utf-8")
        if not guard.scan_paths([deep]):
            failures.append(
                "a nested INDEX.md with document metadata was NOT flagged — the "
                "path exemption is too broad and pollution can hide under the filename"
            )

    # 5. Canon-layer routing frontmatter survives anywhere (it is how a stale doc
    #    stops winning greps), but a block mixing canon keys with real metadata,
    #    or carrying a bogus status, must still be flagged.
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp) / "_active" / "fixture-project" / "02-research"
        base.mkdir(parents=True)
        for name, body, want_flagged in (
            ("canon.md", "---\nstatus: superseded\nsuperseded_by: x.md\n---\n\n# D\n", False),
            ("mixed.md", "---\nstatus: superseded\nauthor: Someone\n---\n\n# D\n", True),
            ("bogus.md", "---\nstatus: not-a-real-status\n---\n\n# D\n", True),
        ):
            f = base / name
            f.write_text(body, encoding="utf-8")
            flagged = bool(guard.scan_paths([f]))
            if flagged != want_flagged:
                failures.append(
                    f"canon frontmatter check wrong for {name}: flagged={flagged}, "
                    f"expected {want_flagged}"
                )

    if failures:
        print("Projects index verification FAILED")
        for f in failures:
            print(f"- {f}")
        return 1
    print("Projects index verification PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
