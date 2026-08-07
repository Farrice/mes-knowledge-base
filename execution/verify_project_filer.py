#!/usr/bin/env python3
"""verify_project_filer.py — the sweep must never eat a file another tool owns.

Two failures on 2026-07-28, both silent until they weren't:

1. EXEMPT_NAMES lacked CANON.md / CAMPAIGN.md / MOVED.md. The sweep had been
   quietly TIMING OUT, so the gap never bit. The moment it ran fast enough to
   finish, it filed 27 of them into 04-deliverables/ — including
   _active/linkedin/CAMPAIGN.md, which hooks/campaign_beacon.py reads by
   exact path, and 11 MOVED.md relocation pointers whose whole job is to sit at
   the old location.

2. A `git grep` pathspec exclusion added for speed used the ':!' shorthand,
   which silently matches NOTHING on this git. Every control-plane pin
   evaporated and pinned files became eligible moves. A silent zero is the
   worst possible failure for a pin check.

Exit 0 = PASS, 1 = FAIL.
"""
from __future__ import annotations

import ast
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import project_filer as pf  # noqa: E402

# Each is a contract with another tool; filing it away breaks that tool.
MUST_BE_EXEMPT = {
    "INDEX.md": "projects_index.py — project entry point + lifecycle stamp",
    "CANON.md": "canon_audit.py — written AT the project root",
    "CAMPAIGN.md": "hooks/campaign_beacon.py — read by exact path",
    "MOVED.md": "project_relocate.py — relocation pointer, must stay put",
    "CLAUDE.md": "per-client context inheritance",
    "README.md": "project readme",
    "RISKS.md": "per-project risk register",
}


def main() -> int:
    failures: list[str] = []

    # 1. Names another tool owns are never filed.
    for name, why in MUST_BE_EXEMPT.items():
        if name not in pf.EXEMPT_NAMES:
            failures.append(f"{name} missing from EXEMPT_NAMES — {why}")
        if not pf.is_exempt(Path("/tmp/proj") / name):
            failures.append(f"is_exempt() says {name} is filable — {why}")

    # 2. The grep exclusion must EXCLUDE, not annihilate. A pathspec form that
    #    matches nothing turns every pin into a move, silently.
    needle = "CLAUDE.md"
    try:
        plain = subprocess.run(
            ["git", "grep", "-I", "-l", "-F", "--untracked", needle],
            cwd=pf.ROOT, capture_output=True, text=True, timeout=60)
        scoped = subprocess.run(
            ["git", "grep", "-I", "-l", "-F", "--untracked", needle,
             "--", *pf._GREP_EXCLUDES],
            cwd=pf.ROOT, capture_output=True, text=True, timeout=60)
        n_plain = len([l for l in plain.stdout.splitlines() if l.strip()])
        n_scoped = len([l for l in scoped.stdout.splitlines() if l.strip()])
        if n_plain and not n_scoped:
            failures.append(
                f"_GREP_EXCLUDES annihilates the search ({n_plain} hits -> 0). "
                f"The ':!' shorthand does this silently; use ':(exclude)path'. "
                f"Every control-plane pin would become an unpinned move."
            )
        if n_scoped > n_plain:
            failures.append(f"scoped grep returned MORE than unscoped ({n_scoped} > {n_plain})")
    except (OSError, subprocess.SubprocessError) as exc:
        failures.append(f"grep exclusion check could not run: {exc}")

    # 3. A real control-plane referrer still pins.
    if not pf.is_control_referrer(pf.ROOT / "CLAUDE.md"):
        failures.append("CLAUDE.md is not recognised as a control referrer")
    if not pf.is_control_referrer(pf.ROOT / ".agent" / "workflows" / "go.md"):
        failures.append(".agent/workflows/* is not recognised as a control referrer")

    # 4. A web asset a sibling page loads is pinned, not filed.
    with tempfile.TemporaryDirectory() as tmp:
        proj = Path(tmp) / "site"
        proj.mkdir()
        (proj / "index.html").write_text('<script src="app.js"></script>', encoding="utf-8")
        (proj / "app.js").write_text("console.log(1)", encoding="utf-8")
        (proj / "notes.md").write_text("# notes", encoding="utf-8")
        if not pf.sibling_web_host(proj, proj / "app.js"):
            failures.append("a script loaded by a sibling index.html was NOT pinned — "
                            "filing it silently breaks the page")
        if pf.sibling_web_host(proj, proj / "notes.md"):
            failures.append("a plain .md was treated as a web asset")

    # 5. The write-time hook and the filer must agree on what never moves.
    #    They drifted on 2026-07-28: the filer exempted CAMPAIGN.md while the hook
    #    still advised filing it, so the enforcement layer was actively
    #    recommending the move that had just been reversed.
    #    Read by walking the AST — a verifier must never execute the thing it checks.
    hook = Path(__file__).resolve().parent / "hooks" / "artifact_placement_hook.py"
    if hook.is_file():
        pinned: set[str] = set()
        try:
            tree = ast.parse(hook.read_text(encoding="utf-8"))
            for node in ast.walk(tree):
                if not isinstance(node, ast.Assign):
                    continue
                if not any(getattr(t, "id", None) == "PINNED_NAMES" for t in node.targets):
                    continue
                if isinstance(node.value, (ast.Set, ast.List, ast.Tuple)):
                    pinned = {e.value for e in node.value.elts
                              if isinstance(e, ast.Constant) and isinstance(e.value, str)}
        except (OSError, SyntaxError) as exc:
            failures.append(f"could not parse PINNED_NAMES from the placement hook: {exc}")
        missing = {n for n in MUST_BE_EXEMPT if n not in pinned}
        if pinned and missing:
            failures.append(
                f"placement hook PINNED_NAMES is missing {sorted(missing)} — the "
                f"write-time advisory would tell an agent to file a file the "
                f"filer itself refuses to move"
            )

    # 6. The sweep window must widen after a gap, never drop files.
    if pf.effective_since_minutes(None) is not None and not pf.SWEEP_STATE.exists():
        failures.append("no sweep state should mean a full scan (None)")
    if pf.effective_since_minutes(30) != 30:
        failures.append("an explicit --since-minutes must win")

    if failures:
        print("Project filer verification FAILED")
        for f in failures:
            print(f"- {f}")
        return 1
    print("Project filer verification PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
