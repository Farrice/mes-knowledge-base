#!/usr/bin/env python3
"""projects_index.py — generate PROJECTS.md, the repo's retrieval front door.

Answers "where does project X live and is it still alive" without a hunt.

CONTRACT (mirrors canon_audit.py): frontmatter is the source of truth, the
generated file is the map. Judgment lives in each project's own INDEX.md:

    ---
    status: active        # active | parked | done
    entry: 03-launch/CAMPAIGN.md    # optional; overrides entry-file detection
    ---

A stamp always wins. When absent, status is DERIVED from the last human commit
touching the project, so PROJECTS.md is correct-shaped with zero stamping and
stamping is an opt-in override for the cases git gets wrong. `done` is never
derived — finishing is a judgment call, and guessing it would hide live work.

Last-touched comes from git, never filesystem mtime: `node_modules` mtimes
reflect `npm install`, so a six-month-dead project reads "touched today".

Usage:
  python3 execution/projects_index.py sync     # write PROJECTS.md + health JSON
  python3 execution/projects_index.py check    # dry-run; print drift, exit 0
  python3 execution/projects_index.py json     # machine-readable to stdout

Never blocks, never exits nonzero on drift (compass, never cage).
"""
from __future__ import annotations

import json
import subprocess
import sys
from datetime import date, datetime, timezone
from pathlib import Path

# Explicit self-directory import: survives any CWD and any future orphan sweep
# that relocates a sibling. (A bare `from canon_audit import ...` is what broke
# artifact_router.py when execution/paths.py was archived on 2026-07-28.)
sys.path.insert(0, str(Path(__file__).resolve().parent))
from canon_audit import frontmatter  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PROJECT_ROOTS = ("_active", "projects")
OUTPUT_MD = ROOT / "PROJECTS.md"
OUTPUT_JSON = ROOT / ".agent" / "health" / "projects-index.json"

VALID_STATUS = ("active", "parked", "done")
ACTIVE_WINDOW_DAYS = 30      # derived active vs parked
STALE_DECLARED_DAYS = 45     # declared active but cold this long = contradiction
DONE_BUT_LIVE_DAYS = 14      # declared done but touched this recently = contradiction

PRUNE_DIRS = {".git", "node_modules", "__pycache__", ".venv", ".tmp",
              "dist", "build", ".next", ".cache"}

# The canonical lifecycle folder prefixes from directives/artifact-placement.md.
# Two dirs sharing one of THESE is a taxonomy collision; two dirs sharing any
# other number is just project-internal topic structure, which is permitted.
LIFECYCLE_PREFIXES = {"00", "01", "02", "03", "04", "05", "06", "90", "99"}

# A commit touching this many distinct projects is a sweep, not work.
BULK_COMMIT_PROJECTS = 10

# Generated maps — never counted as evidence of human work.
GENERATED_MAP_NAMES = {"INDEX.md", "CANON.md"}


# ---------------------------------------------------------------- last touched

def last_touched_git() -> tuple[dict[str, int], dict[str, int]]:
    """One git call for the whole repo, bucketed to `<root>/<project>`.

    Returns (focused, any_commit). A commit touching >= BULK_COMMIT_PROJECTS
    distinct projects is housekeeping (`end-session commit gate`, a harness
    wave, a control-plane install) — it is NOT evidence that anyone worked on
    any one of those projects, and counting it makes 14 cold projects render
    "active". The measured distribution on this repo has a clean gap: 197
    commits touch 1 project, 4 touch 10+.

    `focused` is the honest signal; `any_commit` is the fallback for projects
    whose only history is bulk commits — a real date beats no date.

    Measured 0.22s over 24 months. Per-project git calls would be ~70
    subprocesses; this is one.
    """
    try:
        proc = subprocess.run(
            ["git", "log", "--since=24 months ago", "--pretty=format:C%ct",
             "--name-only", "--", *PROJECT_ROOTS],
            cwd=ROOT, capture_output=True, text=True, timeout=60,
        )
    except (OSError, subprocess.SubprocessError):
        return {}, {}

    focused: dict[str, int] = {}
    any_commit: dict[str, int] = {}
    stamp: int | None = None
    touched: set[str] = set()

    def flush() -> None:
        if stamp is None or not touched:
            return
        for key in touched:
            if stamp > any_commit.get(key, 0):
                any_commit[key] = stamp
        if len(touched) < BULK_COMMIT_PROJECTS:
            for key in touched:
                if stamp > focused.get(key, 0):
                    focused[key] = stamp

    for line in proc.stdout.splitlines():
        if line.startswith("C") and line[1:].isdigit():
            flush()
            stamp = int(line[1:])
            touched = set()
            continue
        if not line or stamp is None:
            continue
        parts = line.split("/")
        if len(parts) < 2:
            continue
        touched.add(f"{parts[0]}/{parts[1]}")
    flush()
    return focused, any_commit


def last_touched_fs(project_dir: Path) -> int | None:
    """Fallback for git-invisible projects (today: only _active/claude-export,
    which is gitignored). Prunes machine-noise dirs so the answer means
    'a human touched this', not 'npm ran'.
    """
    newest = 0
    for current, dirs, files in project_dir.walk() if hasattr(project_dir, "walk") else _walk(project_dir):
        dirs[:] = [d for d in dirs if d not in PRUNE_DIRS and not d.startswith(".")]
        for name in files:
            # A generated map is not evidence that anyone worked here. The
            # router writes INDEX.md scaffolding on its own schedule; counting
            # it makes an empty project shell look freshly touched.
            if name in GENERATED_MAP_NAMES or name.startswith("."):
                continue
            try:
                mtime = (current / name).stat().st_mtime
            except OSError:
                continue
            if mtime > newest:
                newest = int(mtime)
    return newest or None


def _walk(root: Path):
    import os
    for cur, dirs, files in os.walk(root):
        yield Path(cur), dirs, files


# ------------------------------------------------------------------- per-project

def is_relocation_stub(project_dir: Path) -> bool:
    """A directory left behind by `project_relocate --stub`: a MOVED.md pointer
    and nothing else. It exists so a grep for the old path still finds where the
    work went — it is not a project, and listing it would put phantom rows in
    PROJECTS.md and a false `missing_index` in the drift report.

    Tolerant of generated maps: artifact_router.ensure_project_shapes() writes a
    boilerplate INDEX.md into any _active/<dir> lacking one, which silently turned
    five pointers back into "live projects". A dir holding MOVED.md and nothing
    but generated maps is still a pointer.
    """
    try:
        entries = [p for p in project_dir.iterdir() if not p.name.startswith(".")]
    except OSError:
        return False
    names = {p.name for p in entries}
    if "MOVED.md" not in names:
        return False
    return not (names - {"MOVED.md"} - GENERATED_MAP_NAMES)


def read_stamp(index_path: Path) -> dict:
    if not index_path.is_file():
        return {}
    try:
        return frontmatter(index_path.read_text(errors="replace"))
    except OSError:
        return {}


def entry_file(project_dir: Path, stamp: dict) -> str | None:
    """Where a human should start reading. Declared entry wins."""
    declared = stamp.get("entry")
    if declared and (project_dir / declared).exists():
        return declared
    if (project_dir / "CAMPAIGN.md").is_file():
        return "CAMPAIGN.md"
    start_here = project_dir / "00-start-here"
    if start_here.is_dir():
        docs = sorted(p.name for p in start_here.glob("*.md"))
        if docs:
            return f"00-start-here/{docs[0]}"
    if (project_dir / "INDEX.md").is_file():
        return "INDEX.md"
    if (project_dir / "README.md").is_file():
        return "README.md"
    return None


def derive_status(days: int | None) -> str:
    """`done` is deliberately underivable — only Farrice declares a thing finished."""
    if days is None:
        return "parked"
    return "active" if days < ACTIVE_WINDOW_DAYS else "parked"


def numeric_prefix_groups(project_dir: Path) -> dict[str, list[str]]:
    """Sibling dirs colliding on a CANONICAL lifecycle prefix (03-content +
    03-launch) mean two taxonomies were applied to one project and never
    reconciled.

    Only the canonical prefixes count. `directives/artifact-placement.md`
    explicitly permits arbitrary numbered topic folders as project-internal
    structure (coach-cooz's `16-war-on-fitness-industry/`), so flagging every
    shared number would fire on legitimate placements — and a check that cries
    wolf gets muted, which is the decay it exists to prevent.
    """
    groups: dict[str, list[str]] = {}
    try:
        entries = [d.name for d in project_dir.iterdir() if d.is_dir()]
    except OSError:
        return {}
    for name in entries:
        head, sep, _ = name.partition("-")
        if sep and head in LIFECYCLE_PREFIXES:
            groups.setdefault(head, []).append(name)
    return {k: sorted(v) for k, v in groups.items() if len(v) > 1}


def collect() -> list[dict]:
    focused_times, any_times = last_touched_git()
    today = datetime.now(timezone.utc)
    rows: list[dict] = []

    for root_name in PROJECT_ROOTS:
        root_dir = ROOT / root_name
        if not root_dir.is_dir():
            continue
        for project_dir in sorted(root_dir.iterdir()):
            if not project_dir.is_dir() or project_dir.name.startswith("."):
                continue
            if is_relocation_stub(project_dir):
                continue   # a pointer left by project_relocate, not a project
            key = f"{root_name}/{project_dir.name}"
            ts = focused_times.get(key)
            stamp_source = "git"
            if ts is None:
                # Only ever touched by a sweep. The sweep's date is not when
                # anyone worked on this — prefer the real content mtime, and
                # fall back to the sweep date only if there's nothing else.
                ts = last_touched_fs(project_dir)
                stamp_source = "mtime"
                if ts is None:
                    ts = any_times.get(key)
                    stamp_source = "git-bulk-only"
            days = None
            if ts:
                days = (today - datetime.fromtimestamp(ts, timezone.utc)).days

            index_path = project_dir / "INDEX.md"
            stamp = read_stamp(index_path)
            declared = (stamp.get("status") or "").strip().lower()

            if declared in VALID_STATUS:
                status, status_source = declared, "declared"
            else:
                status, status_source = derive_status(days), "derived"

            # When was the stamp itself written? A stamp newer than the last
            # activity is the most recent word on the project's state.
            stamped_after = False
            if declared in VALID_STATUS and ts:
                try:
                    stamped_after = index_path.stat().st_mtime >= ts
                except OSError:
                    stamped_after = False

            rows.append({
                "stamped_after_touch": stamped_after,
                "name": project_dir.name,
                "root": root_name,
                "path": key,
                "status": status,
                "status_source": status_source,
                "declared_raw": declared or None,
                "entry": entry_file(project_dir, stamp),
                "index_exists": index_path.is_file(),
                "last_touched": (date.fromtimestamp(ts).isoformat() if ts else None),
                "last_touched_source": stamp_source if ts else None,
                "days": days,
                "prefix_collisions": numeric_prefix_groups(project_dir),
            })
    return rows


# ------------------------------------------------------------------------ drift

def drift(rows: list[dict]) -> list[dict]:
    """Contradictions and blockers ONLY — never the full unstamped list.

    A 70-row "you haven't stamped this" wall is a report nobody reads, and an
    unread report is how the last three organization attempts died.
    """
    out: list[dict] = []
    for r in rows:
        if r["declared_raw"] and r["declared_raw"] not in VALID_STATUS:
            out.append({"kind": "bad_status_value", "project": r["path"],
                        "detail": f"status: {r['declared_raw']} (expected {'/'.join(VALID_STATUS)})"})
        if (r["status_source"] == "declared" and r["status"] == "active"
                and r["days"] is not None and r["days"] > STALE_DECLARED_DAYS):
            out.append({"kind": "status_declared_stale", "project": r["path"],
                        "detail": f"stamped active, untouched {r['days']}d"})
        # "Stamped done but still live" only means something if the activity came
        # AFTER the stamp. A stamp written today on a project touched today is
        # Farrice saying "this is finished" about work that just concluded — the
        # newer information wins. Without this, any housekeeping pass (filing,
        # a folder merge) makes every freshly-stamped project look contradictory,
        # and a report that cries wolf on day one is a report nobody reads.
        if (r["status_source"] == "declared" and r["status"] == "done"
                and r["days"] is not None and r["days"] < DONE_BUT_LIVE_DAYS
                and not r.get("stamped_after_touch")):
            out.append({"kind": "status_done_but_live", "project": r["path"],
                        "detail": f"stamped done, then touched {r['days']}d ago"})
        if not r["index_exists"]:
            out.append({"kind": "missing_index", "project": r["path"],
                        "detail": "no INDEX.md — project has no entry point"})
        for prefix, dirs in r["prefix_collisions"].items():
            out.append({"kind": "dual_taxonomy", "project": r["path"],
                        "detail": f"{prefix}-* collision: {' + '.join(dirs)}"})
    return out


# --------------------------------------------------------------------- render

def _row_line(r: dict) -> str:
    star = "*" if r["status_source"] == "derived" else ""
    entry = f"`{r['path']}/{r['entry']}`" if r["entry"] else "**— none —**"
    touched = r["last_touched"] or "—"
    return f"| `{r['name']}` | {r['root']}/ | {entry} | {touched} | {r['status']}{star} |"


def render_markdown(rows: list[dict], issues: list[dict]) -> str:
    lines = [
        "# PROJECTS — generated map",
        "",
        f"Generated {date.today().isoformat()} by `execution/projects_index.py`. "
        "**Do not edit manually.**",
        "",
        "Status lives in each project's own `INDEX.md` frontmatter "
        "(`status: active | parked | done`); everything else is derived from git "
        "history. A `*` means the status was derived, not declared — stamp the "
        "project's `INDEX.md` to override it. `done` is never derived.",
        "",
    ]
    by_status = {s: [r for r in rows if r["status"] == s] for s in VALID_STATUS}
    headings = {"active": "## Active", "parked": "## Parked", "done": "## Done"}
    for status in VALID_STATUS:
        group = sorted(by_status[status], key=lambda r: (r["last_touched"] or ""), reverse=True)
        lines += [headings[status], ""]
        if not group:
            lines += ["_none_", ""]
            continue
        lines += ["| Project | Tree | Entry point | Last touched | Status |",
                  "|---|---|---|---|---|"]
        lines += [_row_line(r) for r in group]
        lines.append("")

    lines += [f"**{len(rows)} projects** — "
              f"{len(by_status['active'])} active, {len(by_status['parked'])} parked, "
              f"{len(by_status['done'])} done.", ""]

    if issues:
        lines += ["## Needs judgment", "",
                  "Contradictions only — not a list of unstamped projects.", ""]
        for i in issues:
            lines.append(f"- **{i['kind']}** — `{i['project']}`: {i['detail']}")
        lines.append("")
    return "\n".join(lines)


# ----------------------------------------------------------------------- write

def write(rows: list[dict], issues: list[dict]) -> None:
    OUTPUT_MD.write_text(render_markdown(rows, issues) + "\n", encoding="utf-8")
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps({
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "rows": rows,
        "drift": issues,
    }, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    command = sys.argv[1] if len(sys.argv) > 1 else "sync"
    rows = collect()
    issues = drift(rows)

    if command == "json":
        print(json.dumps({"rows": rows, "drift": issues}, indent=2))
        return 0

    if command == "check":
        print(f"{len(rows)} projects scanned. Drift items: {len(issues)}")
        for i in issues:
            print(f"  {i['kind']:<24} {i['project']:<48} {i['detail']}")
        if not issues:
            print("  none — every project has an entry point and a coherent status.")
        return 0

    write(rows, issues)
    print(f"Wrote {OUTPUT_MD.relative_to(ROOT)} ({len(rows)} projects, {len(issues)} drift items)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
