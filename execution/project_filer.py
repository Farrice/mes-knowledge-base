#!/usr/bin/env python3
"""project_filer.py — deterministic filing engine for the only-populated
project-subfolder policy (docs/solutions/2026-07-07-project-artifacts-loose-plus-empty-scaffold.md).

Fills the gaps left by artifact_router.py: nothing files loose project-root
artifacts into canonical numbered subfolders, and inbound references are never
rewritten on move. This tool plans, applies (with reference rewrites), verifies
0 broken links, and sweeps recent loose files on the session-close spine.

Reuses artifact_router logic by import (classify_path, STANDARD_PROJECT_DIRS,
append_move_ledger, aliases + write_json). The org move-ledger stays the single
history; a per-run REVERT-<date>.sh makes any pass reversible without git.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

sys.path.insert(0, str(Path(__file__).resolve().parent))

import artifact_router as ar  # noqa: E402
from artifact_router import (  # noqa: E402
    ALIASES_PATH,
    STANDARD_PROJECT_DIRS,
    append_move_ledger,
    classify_path,
    infer_lifecycle,
    load_aliases,
    write_json,
)

ROOT = ar.ROOT
MEMORY_DIR = Path(
    "/Users/farricecain/.claude/projects/-Users-farricecain-Google-Antigravity/memory"
)
ORG_HOME = ROOT / ".agent" / "organization"
RECEIPTS_DIR = ORG_HOME / "receipts"

# Files pinned by name at a project root — never filed into a subfolder.
#
# SCAR 2026-07-28: CANON.md, CAMPAIGN.md and MOVED.md were missing here. The
# sweep had been silently timing out, so the gap never bit; the moment it ran
# fast enough to finish it filed 27 of them into 04-deliverables/ — including
# _active/linkedin-launch/CAMPAIGN.md, which the SessionStart campaign beacon
# reads by exact path, and 11 MOVED.md relocation pointers, whose entire job is
# to sit at the old location. Each of these is a contract with another tool:
#   INDEX.md    project entry point + lifecycle stamp (projects_index.py)
#   CANON.md    canon map, written AT the project root (canon_audit.py)
#   CAMPAIGN.md mission queue, read by hooks/campaign_beacon.py
#   MOVED.md    relocation pointer (project_relocate.py --stub)
EXEMPT_NAMES = {"INDEX.md", "README.md", "CLAUDE.md", "RISKS.md", ".gitignore",
                "CANON.md", "CAMPAIGN.md", "MOVED.md", "AGENTS.md", "CODEX.md",
                "GEMINI.md"}

# A referrer under any of these repo roots pins the file (control plane is
# never rewritten by this tool).
CONTROL_NAMES = {"CLAUDE.md", "GEMINI.md", "AGENTS.md", "CODEX.md"}
CONTROL_TOP_DIRS = {".claude", "directives", "execution", "skills"}
CONTROL_PREFIXES = (".agent/workflows/",)

# Auto-generated bookkeeping — real authorship never lives here, so these are
# ignored entirely as referrers (rewriting router snapshots is noise).
BOOKKEEPING_PREFIXES = ("_system/organization/", ".agent/organization/", ".git/")

LIFECYCLE_TO_FOLDER = {
    "archive": "99-archive",
    "asset": "05-assets",
    "deliverable": "04-deliverables",
    "draft": "03-working-drafts",
    "export": "90-exports",
    "research": "02-research",
    "source": "01-source",
    "system": "06-system",
}

BINARY_SUFFIXES = ar.ASSET_SUFFIXES | {".pdf", ".docx", ".zip", ".gz", ".db"}

# Only targets whose final segment carries a known FILE suffix are treated as
# path refs. This excludes slash-commands (/copy-engine), bare domains
# (foo.com), reddit handles (u/x), money strings ($X/month), and fractions
# (24/7) that otherwise read as paths. Dir-only refs (intel/) are not checked.
KNOWN_FILE_SUFFIXES = {
    ".md", ".txt", ".py", ".sh", ".json", ".jsonl", ".yaml", ".yml", ".toml",
    ".csv", ".tsv", ".html", ".htm", ".pdf", ".docx", ".xlsx", ".pptx",
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".mp4", ".mov", ".mp3",
    ".db", ".zip",
}
_MD_LINK_RE = re.compile(r"\]\(([^)\s]+)(\s+\"[^\"]*\")?\)")
_INLINE_CODE_RE = re.compile(r"`([^`\n]+)`")


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _rel_to_root(path: Path) -> str | None:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return None


def is_exempt(path: Path) -> bool:
    return path.name in EXEMPT_NAMES or path.name.startswith(".")


def loose_files(project_root: Path) -> list[Path]:
    if not project_root.is_dir():
        return []
    return sorted(
        p for p in project_root.iterdir() if p.is_file() and not is_exempt(p)
    )


def propose(project_root: Path, path: Path) -> tuple[str, float, str, list[str]]:
    """Return (folder, confidence, lifecycle, reasons). Reuses classify_path
    when the file is in-tree with a resolvable destination; degrades to the
    pure suffix/keyword lifecycle heuristic for out-of-tree fixtures."""
    c = classify_path(path)
    if c.destination:
        folder = Path(c.destination).parent.name
        return folder, c.confidence, c.lifecycle, list(c.reasons)
    lifecycle, _at, reasons = infer_lifecycle(path)
    folder = LIFECYCLE_TO_FOLDER.get(lifecycle)
    if folder is None:
        folder = "04-deliverables" if path.suffix.lower() == ".md" else "01-source"
    conf = 0.8 if lifecycle in LIFECYCLE_TO_FOLDER else 0.5
    return folder, conf, lifecycle, reasons + ["degraded suffix/keyword heuristic (out-of-tree)"]


WEB_HOST_SUFFIXES = {".html", ".htm"}
WEB_ASSET_SUFFIXES = {".css", ".js", ".mjs", ".png", ".jpg", ".jpeg", ".svg",
                      ".gif", ".webp", ".ico", ".woff", ".woff2", ".map"}


def sibling_web_host(project_root: Path, path: Path) -> str | None:
    """A page in the same directory that loads this file by relative path.

    SCAR 2026-07-28: the sweep classified a site's entry script as a "draft" and
    filed it into 03-working-drafts/, but the page loaded it by relative path
    from the project root — the site broke silently. A web asset is not an
    artifact to file; it is part of a page's contract with the filesystem.

    (No literal asset filename appears here — it would make this module a
    grep-visible referrer and pin real files for the wrong reason.)
    """
    if path.suffix.lower() not in WEB_ASSET_SUFFIXES:
        return None
    for host in path.parent.iterdir():
        if host.suffix.lower() not in WEB_HOST_SUFFIXES or not host.is_file():
            continue
        try:
            text = host.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        # Match the relative form a page would actually use.
        if f'"{path.name}"' in text or f"'{path.name}'" in text or f"/{path.name}" in text:
            return _display(host)
    return None


# ─────────────────────────────────────────────────────────────
# inbound reference scan
# ─────────────────────────────────────────────────────────────

# Excluded from the grep itself, not filtered afterwards. These hold a 25MB
# manifest and multi-hundred-thousand-line move-plan snapshots; scanning them
# for every needle is what made the session-close sweep blow its 60s budget.
# They are already discarded as referrers by BOOKKEEPING_PREFIXES.
# NOTE the ':(exclude)' long form. The ':!' shorthand silently matches NOTHING
# here (verified: 41 hits unfiltered, 0 with ':!', 10 with ':(exclude)') — a
# silent zero would turn every control-plane pin into an unpinned move.
_GREP_EXCLUDES = [":(exclude)_system/organization", ":(exclude).agent/organization"]


def _git_grep(needle: str) -> list[Path]:
    try:
        r = subprocess.run(
            ["git", "grep", "-I", "-l", "-F", "--untracked", needle,
             "--", *_GREP_EXCLUDES],
            capture_output=True, text=True, cwd=str(ROOT), timeout=30,
        )
    except Exception:
        return []
    if r.returncode not in (0, 1):
        return []
    out = []
    for line in r.stdout.splitlines():
        line = line.strip()
        if line:
            out.append((ROOT / line).resolve())
    return out


def _plain_grep(needle: str, root: Path) -> list[Path]:
    if not root.exists():
        return []
    try:
        r = subprocess.run(
            ["grep", "-rIlF", needle, str(root)],
            capture_output=True, text=True, timeout=30,
        )
    except Exception:
        return []
    if r.returncode not in (0, 1):
        return []
    return [Path(line).resolve() for line in r.stdout.splitlines() if line.strip()]


def _is_bookkeeping(path: Path) -> bool:
    rel = _rel_to_root(path)
    if rel is None:
        return False
    return any(rel.startswith(pfx) for pfx in BOOKKEEPING_PREFIXES)


def is_control_referrer(path: Path) -> bool:
    rel = _rel_to_root(path)
    if rel is None:
        return False
    if path.name in CONTROL_NAMES:
        return True
    top = rel.split("/", 1)[0]
    if top in CONTROL_TOP_DIRS:
        return True
    return any(rel.startswith(pfx) for pfx in CONTROL_PREFIXES)


def scan_referrers(path: Path, project_root: Path) -> tuple[list[Path], list[Path]]:
    """Find files referencing `path` by repo-relative path OR bare filename.
    Returns (all_referrers, control_referrers). Excludes self, bookkeeping
    snapshots, and — for out-of-tree fixtures — searches the project's parent
    tree so external referrers are still caught."""
    needles = {path.name}
    rel = _rel_to_root(path)
    if rel is not None:
        needles.add(rel)

    found: set[Path] = set()
    for needle in needles:
        for hit in _git_grep(needle):
            found.add(hit)
        for hit in _plain_grep(needle, MEMORY_DIR):
            found.add(hit)
        if _rel_to_root(project_root) is None:
            # out-of-tree project (fixture): scan its parent for external refs
            for hit in _plain_grep(needle, project_root.parent):
                found.add(hit)

    referrers, control = [], []
    for f in sorted(found):
        if f == path or _is_bookkeeping(f):
            continue
        referrers.append(f)
        if is_control_referrer(f):
            control.append(f)
    return referrers, control


# ─────────────────────────────────────────────────────────────
# plan
# ─────────────────────────────────────────────────────────────

def build_plan(project_root: Path, since_minutes: int | None = None,
               with_baseline: bool = True) -> dict[str, Any]:
    project_root = project_root.resolve()
    slug = project_root.name
    cutoff = None
    if since_minutes is not None:
        cutoff = datetime.now(timezone.utc).timestamp() - since_minutes * 60

    items: list[dict[str, Any]] = []
    candidates = loose_files(project_root)
    if cutoff is not None:
        candidates = [p for p in candidates if p.stat().st_mtime >= cutoff]
    # Nothing in window: skip the whole scan. sweep() walks ~60 projects and
    # most have no eligible file — the per-project work below is what made the
    # session-close step blow its 60s budget.
    if not candidates and not with_baseline:
        return {"version": 1, "producer": "project_filer.py", "schema": 1,
                "generated_at": utc_now(), "project": str(project_root),
                "project_slug": slug, "items": [], "baseline_broken": []}
    for path in candidates:
        folder, conf, lifecycle, reasons = propose(project_root, path)
        destination = project_root / folder / path.name
        referrers, control = scan_referrers(path, project_root)
        web_host = sibling_web_host(project_root, path)
        if control:
            action = "pin"
            pin_reason = f"referenced from control-plane file: {_display(control[0])}"
        elif web_host:
            action = "pin"
            pin_reason = (f"loaded by {web_host} as a relative asset — moving it "
                          f"breaks the page")
        else:
            action = "move"
            pin_reason = ""
        items.append({
            "path": str(path),
            "destination": str(destination),
            "action": action,
            "pin_reason": pin_reason,
            "lifecycle": lifecycle,
            "confidence": round(conf, 2),
            "referrers": [str(r) for r in referrers],
            "control_referrers": [str(r) for r in control],
            "reasons": reasons,
        })

    # Pre-move broken-ref baseline: verify --against-plan fails only on
    # NET-NEW breaks relative to this set. Skipped by sweep(), which never
    # consumes it — computing it for every project was pure cost.
    baseline: list[Any] = []
    if with_baseline:
        try:
            baseline = scan_broken_refs(project_root)
        except Exception:
            baseline = []

    return {
        "version": 1,
        # Provenance stamp. apply_plan refuses anything lacking it — the 2026-07-08
        # crash came from an agent-authored plan written against an imagined schema.
        "producer": "project_filer.py",
        "schema": 1,
        "generated_at": utc_now(),
        "project": str(project_root),
        "project_slug": slug,
        "items": items,
        "baseline_broken": baseline,
    }


def _display(path: Path) -> str:
    rel = _rel_to_root(path)
    return rel if rel is not None else str(path)


def print_plan(plan: dict[str, Any]) -> None:
    moves = [i for i in plan["items"] if i["action"] == "move"]
    pins = [i for i in plan["items"] if i["action"] == "pin"]
    print(f"Project: {plan['project']}")
    print(f"  loose files: {len(plan['items'])}  moves: {len(moves)}  pins: {len(pins)}")
    for i in plan["items"]:
        src = _display(Path(i["path"]))
        if i["action"] == "move":
            dest = _display(Path(i["destination"]))
            refs = f"  [{len(i['referrers'])} referrer(s)]" if i["referrers"] else ""
            print(f"  MOVE  {src}  ->  {dest}  (conf {i['confidence']}, {i['lifecycle']}){refs}")
        else:
            print(f"  PIN   {src}  — {i['pin_reason']}")


# ─────────────────────────────────────────────────────────────
# reference rewriting
# ─────────────────────────────────────────────────────────────

def _is_pathlike(target: str) -> bool:
    if not target or " " in target:
        return False
    if "://" in target:
        return False
    if "<" in target or ">" in target:  # template placeholders like agents/<slug>/AGENT.md
        return False
    if target.startswith(("#", "mailto:", "/", "u/", "$", "~")):
        return False
    stem = target.split("#", 1)[0]
    last = stem.rsplit("/", 1)[-1]
    dot = last.rfind(".")
    if dot <= 0:
        return False
    return last[dot:].lower() in KNOWN_FILE_SUFFIXES


def _resolve_target(target: str, base_dir: Path) -> Path | None:
    t = target.split("#", 1)[0]
    if not t:
        return None
    try:
        if t.startswith("/"):
            cand = Path(t)
        else:
            cand = (base_dir / t)
        return cand.resolve()
    except Exception:
        return None


def rewrite_file(
    current: Path,
    old_dir: Path,
    move_map: dict[str, str],
    rel_pairs: list[tuple[str, str]],
) -> int:
    """Rewrite one text file: (a) plain repo-relative path-string swaps for
    in-tree moves, (b) markdown-link / inline-code targets that resolve (from
    the file's OLD directory) to a moved source, recomputed relative to the
    file's NEW directory. Returns the number of substitutions made."""
    if current.suffix.lower() in BINARY_SUFFIXES:
        return 0
    try:
        text = current.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return 0

    count = 0
    # (a) plain repo-relative path strings
    for old_rel, new_rel in rel_pairs:
        if old_rel and old_rel in text:
            n = text.count(old_rel)
            text = text.replace(old_rel, new_rel)
            count += n

    new_dir = current.parent
    file_moved = new_dir.resolve() != old_dir.resolve()

    def _recompute(target: str) -> str | None:
        if not _is_pathlike(target):
            return None
        abs_old = _resolve_target(target, old_dir)
        if abs_old is None:
            return None
        key = str(abs_old)
        if key in move_map:
            new_abs = move_map[key]
        elif file_moved and abs_old.exists():
            # This file moved but the ref target stayed put (e.g. intel/…):
            # recompute the relative path from the file's NEW location.
            new_abs = key
        else:
            # Ref did not resolve pre-move: pre-existing breakage, leave
            # byte-identical (never "fix" garbage into different garbage).
            return None
        new_target = os.path.relpath(new_abs, new_dir)
        return new_target if new_target != target else None

    def _sub_md(m: "re.Match[str]") -> str:
        nonlocal count
        target, title = m.group(1), m.group(2) or ""
        rep = _recompute(target)
        if rep is None:
            return m.group(0)
        count += 1
        return f"]({rep}{title})"

    text = _MD_LINK_RE.sub(_sub_md, text)

    def _sub_code(m: "re.Match[str]") -> str:
        nonlocal count
        target = m.group(1)
        rep = _recompute(target)
        if rep is None:
            return m.group(0)
        count += 1
        return f"`{rep}`"

    text = _INLINE_CODE_RE.sub(_sub_code, text)

    if count:
        current.write_text(text, encoding="utf-8")
    return count


# ─────────────────────────────────────────────────────────────
# apply
# ─────────────────────────────────────────────────────────────

def _revert_script_path() -> Path:
    return ORG_HOME / f"REVERT-{datetime.now().date().isoformat()}.sh"


def _prepend_revert(lines: list[str]) -> None:
    if not lines:
        return
    ORG_HOME.mkdir(parents=True, exist_ok=True)
    path = _revert_script_path()
    if path.exists():
        existing = path.read_text(encoding="utf-8").splitlines()
        body = [ln for ln in existing if ln and not ln.startswith("#!")]
    else:
        body = []
    header = ["#!/bin/sh", "# Auto-generated inverse moves (newest first). Re-run to revert.", ""]
    out = header + lines + body
    path.write_text("\n".join(out) + "\n", encoding="utf-8")
    path.chmod(0o755)


def apply_plan(plan: dict[str, Any], receipt_path: Path | None, dry_run: bool = False) -> dict[str, Any]:
    # Fail-fast schema check BEFORE any move — a malformed (e.g. agent-authored)
    # plan must die here, not mid-mutation with files moved and rewrites unrun.
    if plan.get("producer") != "project_filer.py":
        raise SystemExit(
            "plan is missing the project_filer.py provenance stamp — refusing to apply.\n"
            "Plans are generated by `project_filer.py plan`, never hand-authored.\n"
            "Regenerate: python3 execution/project_filer.py plan --project \"<dir>\" --out <plan.json>"
        )
    missing = [k for k in ("project", "project_slug", "items") if k not in plan]
    if missing:
        raise SystemExit(f"plan missing required keys {missing} — refusing to apply")
    for idx, it in enumerate(plan["items"]):
        bad = [k for k in ("path", "action") if k not in it]
        if it.get("action") == "move":
            bad += [k for k in ("destination", "referrers") if k not in it]
        if bad:
            raise SystemExit(f"plan item {idx} missing keys {bad} — refusing to apply")

    project_root = Path(plan["project"]).resolve()
    move_items = [i for i in plan["items"] if i["action"] == "move"]
    pins = [i for i in plan["items"] if i["action"] == "pin"]

    if dry_run:
        # Touch nothing. Print the exact move table an apply would perform.
        print(f"DRY RUN — {project_root}")
        print(f"  would move: {len(move_items)}   pinned: {len(pins)}")
        for item in move_items:
            src, dst = Path(item["path"]), Path(item["destination"])
            state = "" if src.exists() else "  [SOURCE MISSING]"
            if dst.exists():
                state = "  [DEST EXISTS — would skip]"
            print(f"  MOVE  {_display(src)}  ->  {_display(dst)}{state}")
        for p in pins:
            print(f"  PIN   {_display(Path(p['path']))}  — {p.get('pin_reason', '')}")
        return {"dry_run": True, "would_move": len(move_items), "pins": len(pins)}

    aliases = load_aliases()
    moved: list[dict[str, str]] = []
    skipped: list[dict[str, str]] = []
    move_map: dict[str, str] = {}
    rel_pairs: list[tuple[str, str]] = []
    revert_lines: list[str] = []

    # 1. move files (create destination dir only now = only-populated)
    for item in move_items:
        source = Path(item["path"])
        destination = Path(item["destination"])
        if not source.exists():
            # A benign retry against an already-applied plan reads as "source
            # missing", which on 2026-07-08 looked exactly like data loss.
            # The alias ledger knows better — say where the file actually went.
            prior = aliases.get("aliases", {}).get(str(source))
            if prior and prior.get("current"):
                reason = f"already moved by a prior run -> {prior['current']}"
            else:
                reason = "source missing"
            skipped.append({"path": str(source), "reason": reason})
            continue
        if destination.exists():
            skipped.append({"path": str(source), "reason": "destination exists"})
            continue
        try:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(source), str(destination))
        except Exception as exc:
            skipped.append({"path": str(source), "reason": f"move failed: {exc}"})
            continue
        moved.append({"from": str(source), "to": str(destination)})
        move_map[str(source.resolve())] = str(destination.resolve())
        old_rel, new_rel = _rel_to_root(source), _rel_to_root(destination)
        if old_rel and new_rel:
            rel_pairs.append((old_rel, new_rel))
        # Flush the inverse IMMEDIATELY, not at end-of-run. On 2026-07-08 a crash
        # in the reference-rewrite phase left 19 files moved with no revert script
        # and no receipt. Each prepend is newest-first, so revert order is preserved.
        _prepend_revert([f'mkdir -p "{source.parent}" && mv -n "{destination}" "{source}"'])
        append_move_ledger({
            "action": "project-file",
            "moved_at": utc_now(),
            "from": str(source),
            "to": str(destination),
            "tool": "project_filer.py",
        })
        aliases["aliases"][str(source)] = {
            "current": str(destination),
            "moved_at": utc_now(),
            "project": plan["project_slug"],
            "lifecycle": item.get("lifecycle"),
        }
    aliases["updated_at"] = utc_now()
    write_json(ALIASES_PATH, aliases)

    # 2. rewrite references (moved files + non-source referrers)
    sources = set(move_map.keys())
    rewrite_targets: dict[Path, Path] = {}  # current-on-disk -> old dir
    for item in move_items:
        dest = Path(item["destination"])
        if str(Path(item["path"]).resolve()) in move_map:
            rewrite_targets[dest] = Path(item["path"]).parent
        for ref in item["referrers"]:
            rp = Path(ref)
            if str(rp.resolve()) in sources:
                continue
            rewrite_targets.setdefault(rp, rp.parent)

    rewrites: dict[str, int] = {}
    for current, old_dir in rewrite_targets.items():
        if not current.exists():
            continue
        n = rewrite_file(current, old_dir, move_map, rel_pairs)
        if n:
            rewrites[str(current)] = n

    # 3. prune now-empty scaffold dirs (only-populated cleanup)
    pruned: list[str] = []
    for name in STANDARD_PROJECT_DIRS:
        d = project_root / name
        if d.is_dir() and not any(d.iterdir()):
            try:
                d.rmdir()
                pruned.append(str(d))
                revert_lines.append(f'mkdir -p "{d}"')
            except OSError:
                pass

    _prepend_revert(revert_lines)

    receipt = {
        "version": 1,
        "applied_at": utc_now(),
        "project": str(project_root),
        "project_slug": plan["project_slug"],
        "moves": moved,
        "old_paths": [m["from"] for m in moved],
        "skipped": skipped,
        "pins": [{"path": p["path"], "reason": p["pin_reason"]} for p in pins],
        "rewrites": rewrites,
        "pruned_dirs": pruned,
        "revert_script": str(_revert_script_path()),
    }
    if receipt_path is None:
        RECEIPTS_DIR.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
        receipt_path = RECEIPTS_DIR / f"{datetime.now().date().isoformat()}-{plan['project_slug']}-{stamp}.json"
    write_json(receipt_path, receipt)
    receipt["receipt_path"] = str(receipt_path)
    return receipt


# ─────────────────────────────────────────────────────────────
# verify
# ─────────────────────────────────────────────────────────────

def _iter_project_md(project_root: Path) -> Iterable[Path]:
    for p in project_root.rglob("*.md"):
        if ".git" in p.parts:
            continue
        yield p


def scan_broken_refs(project_root: Path) -> list[dict[str, str]]:
    broken: list[dict[str, str]] = []
    for md in _iter_project_md(project_root):
        try:
            text = md.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        targets = [m.group(1) for m in _MD_LINK_RE.finditer(text)]
        targets += [m.group(1) for m in _INLINE_CODE_RE.finditer(text)]
        for target in targets:
            if not _is_pathlike(target):
                continue
            t = target.split("#", 1)[0]
            if not t:
                continue
            resolved = _resolve_target(t, md.parent)
            repo_resolved = (ROOT / t).resolve() if not t.startswith("/") else None
            if (resolved and resolved.exists()) or (repo_resolved and repo_resolved.exists()):
                continue
            broken.append({"file": _display(md), "target": target})
    return broken


def _baseline_pairs(entries: Iterable[dict[str, str]]) -> set[tuple[str, str]]:
    # Files move between baseline and verify, so identity = (basename, target).
    return {(Path(e["file"]).name, e["target"]) for e in entries}


def _git_head_baseline(project_root: Path) -> list[dict[str, str]] | None:
    """Recompute the pre-move broken-ref set from git HEAD (for plans that
    predate the baseline_broken field). Existence = present in HEAD's file
    list or on disk (for refs outside the repo snapshot)."""
    rel = _rel_to_root(project_root)
    if rel is None:
        return None
    try:
        all_head = subprocess.run(
            ["git", "ls-tree", "-r", "--name-only", "HEAD"],
            capture_output=True, text=True, cwd=str(ROOT), timeout=30,
        )
        if all_head.returncode != 0:
            return None
        head_set = set(all_head.stdout.splitlines())
    except Exception:
        return None

    broken: list[dict[str, str]] = []
    for name in sorted(head_set):
        if not name.startswith(rel + "/") or not name.endswith(".md"):
            continue
        try:
            show = subprocess.run(
                ["git", "show", f"HEAD:{name}"],
                capture_output=True, text=True, cwd=str(ROOT), timeout=30,
            )
        except Exception:
            continue
        if show.returncode != 0:
            continue
        text = show.stdout
        base_dir = str(Path(name).parent)
        targets = [m.group(1) for m in _MD_LINK_RE.finditer(text)]
        targets += [m.group(1) for m in _INLINE_CODE_RE.finditer(text)]
        for target in targets:
            if not _is_pathlike(target):
                continue
            t = target.split("#", 1)[0]
            if not t:
                continue
            rel_resolved = os.path.normpath(os.path.join(base_dir, t))
            root_resolved = os.path.normpath(t)
            if rel_resolved in head_set or root_resolved in head_set:
                continue
            if (ROOT / rel_resolved).exists() or (ROOT / root_resolved).exists():
                continue
            broken.append({"file": name, "target": target})
    return broken


def verify_project(
    project_root: Path,
    against_plan: Path | None = None,
    baseline_count: int | None = None,
) -> dict[str, Any]:
    project_root = project_root.resolve()
    broken = scan_broken_refs(project_root)

    # net-new basis: subtract the pre-move baseline when one is supplied
    baseline_source = "none"
    net_new = broken
    if against_plan is not None:
        baseline_entries: list[dict[str, str]] | None = None
        try:
            plan = json.loads(against_plan.read_text(encoding="utf-8"))
            if isinstance(plan.get("baseline_broken"), list):
                baseline_entries = plan["baseline_broken"]
                baseline_source = "plan"
        except Exception:
            pass
        if baseline_entries is None:
            baseline_entries = _git_head_baseline(project_root)
            baseline_source = "git-HEAD" if baseline_entries is not None else "unavailable"
        if baseline_entries is not None:
            pairs = _baseline_pairs(baseline_entries)
            net_new = [b for b in broken
                       if (Path(b["file"]).name, b["target"]) not in pairs]
    elif baseline_count is not None:
        baseline_source = f"count={baseline_count}"
        net_new = broken[baseline_count:] if len(broken) > baseline_count else []

    # old-path residue from today's receipts for this project
    today = datetime.now().date().isoformat()
    old_paths: set[str] = set()
    if RECEIPTS_DIR.exists():
        for r in RECEIPTS_DIR.glob(f"{today}-{project_root.name}-*.json"):
            try:
                data = json.loads(r.read_text(encoding="utf-8"))
            except Exception:
                continue
            old_paths.update(data.get("old_paths", []))
    residue: list[dict[str, str]] = []
    for old in old_paths:
        rel = _rel_to_root(Path(old))
        needle = rel if rel is not None else old
        hits = [h for h in (_git_grep(needle) + _plain_grep(needle, MEMORY_DIR))
                if not _is_bookkeeping(h)]
        for h in hits:
            residue.append({"old_path": needle, "still_referenced_in": _display(h)})

    empty_dirs: list[str] = []
    for d in project_root.rglob("*"):
        if d.is_dir() and ".git" not in d.parts and not any(d.iterdir()):
            empty_dirs.append(_display(d))

    ok = not net_new and not residue and not empty_dirs
    return {
        "project": str(project_root),
        "ok": ok,
        "baseline_source": baseline_source,
        "broken_links": broken,
        "net_new_broken": net_new,
        "old_path_residue": residue,
        "empty_dirs": empty_dirs,
    }


def print_verify(result: dict[str, Any]) -> None:
    print(f"Verify: {result['project']}")
    print(f"  broken links: {len(result['broken_links'])} "
          f"(net-new vs baseline[{result['baseline_source']}]: {len(result['net_new_broken'])})")
    for b in result["net_new_broken"]:
        print(f"    NET-NEW {b['file']} -> {b['target']}")
    print(f"  old-path residue hits: {len(result['old_path_residue'])}")
    for r in result["old_path_residue"]:
        print(f"    {r['old_path']} still in {r['still_referenced_in']}")
    print(f"  empty dirs: {len(result['empty_dirs'])}")
    for d in result["empty_dirs"]:
        print(f"    {d}")
    print("  RESULT:", "PASS" if result["ok"] else "FAIL")


# ─────────────────────────────────────────────────────────────
# prune-empty
# ─────────────────────────────────────────────────────────────

def prune_empty(root: Path, dry_run: bool) -> list[Path]:
    """Bottom-up rmdir of empty dirs under root so nested empties collapse.
    In dry-run, dirs whose only contents are would-be-removed dirs also count."""
    root = root.resolve()
    removed: list[Path] = []
    removed_set: set[Path] = set()
    dirs = sorted(
        (d for d in root.rglob("*") if d.is_dir() and ".git" not in d.parts),
        key=lambda p: len(p.parts), reverse=True,
    )
    for d in dirs:
        try:
            entries = [c for c in d.iterdir() if c not in removed_set]
        except OSError:
            continue
        if entries:
            continue
        if not dry_run:
            try:
                d.rmdir()
            except OSError:
                continue
        removed.append(d)
        removed_set.add(d)
    return removed


# ─────────────────────────────────────────────────────────────
# sweep (session-close spine; never throws)
# ─────────────────────────────────────────────────────────────

def _sweep_project_roots() -> list[Path]:
    roots: list[Path] = []
    for parent_name in ("_active", "projects"):
        parent = ROOT / parent_name
        if not parent.is_dir():
            continue
        for d in parent.iterdir():
            if d.is_dir() and not d.name.startswith("."):
                roots.append(d)
    return roots


SWEEP_STATE = ORG_HOME / "sweep-state.json"


def effective_since_minutes(requested: int | None) -> int | None:
    """Resolve the sweep window from a watermark. None == full scan.

    THIS IS THE FIX FOR WHAT KILLED THE LAST ORGANIZATION LAYER. The window was a
    fixed 720 minutes, so any file created more than 12h before a session close
    was invisible to the sweep FOREVER — and after the last sweep on 2026-07-19,
    nine days of files were unreachable by any mechanism. A gap between sweeps
    must WIDEN the window, never drop files on the floor.
    """
    if requested is not None:
        return requested                      # explicit --since-minutes always wins
    try:
        last = json.loads(SWEEP_STATE.read_text()).get("last_swept_at")
    except (OSError, ValueError):
        last = None
    if not last:
        return None                           # never swept -> full scan
    elapsed = (datetime.now(timezone.utc).timestamp() - float(last)) / 60
    if elapsed > 30 * 1440:
        return None                           # >30d gap -> full scan, catch everything
    return max(720, int(elapsed) + 60)        # +60min overlap for clock skew


def _record_sweep() -> None:
    ORG_HOME.mkdir(parents=True, exist_ok=True)
    SWEEP_STATE.write_text(json.dumps(
        {"last_swept_at": datetime.now(timezone.utc).timestamp(),
         "last_swept_iso": utc_now()}, indent=2) + "\n", encoding="utf-8")


def sweep(since_minutes: int | None) -> dict[str, Any]:
    since_minutes = effective_since_minutes(since_minutes)
    auto_moved = 0
    needs_judgment: list[dict[str, Any]] = []
    projects_touched: list[str] = []

    for project_root in _sweep_project_roots():
        try:
            plan = build_plan(project_root, since_minutes=since_minutes,
                              with_baseline=False)
        except Exception:
            continue
        if not plan["items"]:
            continue
        auto_items, defer = [], []
        for item in plan["items"]:
            if (item["action"] == "move"
                    and item["confidence"] >= 0.8
                    and not item["control_referrers"]):
                auto_items.append(item)
            else:
                defer.append(item)
        if auto_items:
            sub = {**plan, "items": auto_items}
            try:
                receipt = apply_plan(sub, None)
                auto_moved += len(receipt["moves"])
                projects_touched.append(project_root.name)
            except Exception:
                for it in auto_items:
                    needs_judgment.append({"project": project_root.name, "path": it["path"],
                                           "reason": "auto-apply failed"})
        for it in defer:
            reason = ("pinned/control referrer" if it["control_referrers"]
                      else f"low confidence {it['confidence']}" if it["action"] == "move"
                      else "pinned by name/reference")
            needs_judgment.append({"project": project_root.name, "path": it["path"], "reason": reason})

    if auto_moved or needs_judgment:
        try:
            RECEIPTS_DIR.mkdir(parents=True, exist_ok=True)
            stamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
            write_json(RECEIPTS_DIR / f"sweep-{stamp}.json", {
                "swept_at": utc_now(),
                "since_minutes": since_minutes,
                "auto_moved": auto_moved,
                "projects_touched": sorted(set(projects_touched)),
                "needs_judgment": needs_judgment,
            })
        except Exception:
            pass

    _record_sweep()
    return {"auto_moved": auto_moved, "needs_judgment": len(needs_judgment),
            "projects": sorted(set(projects_touched))}


# ─────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────

def main() -> int:
    ap = argparse.ArgumentParser(description="Deterministic project filing engine (only-populated subfolders).")
    sub = ap.add_subparsers(dest="command", required=True)

    p_plan = sub.add_parser("plan", help="Plan moves for loose files at a project root.")
    p_plan.add_argument("--project", required=True)
    p_plan.add_argument("--out", help="Write plan JSON to this path.")
    p_plan.add_argument("--json", action="store_true")

    p_apply = sub.add_parser("apply", help="Apply a plan JSON: move + rewrite references + prune scaffold.")
    p_apply.add_argument("--plan", required=True)
    p_apply.add_argument("--receipt")
    p_apply.add_argument("--dry-run", action="store_true", help="Print the move table; touch nothing.")
    p_apply.add_argument("--json", action="store_true")

    p_verify = sub.add_parser("verify", help="Verify 0 broken links / 0 residue / 0 empty dirs.")
    p_verify.add_argument("--project", required=True)
    p_verify.add_argument("--against-plan", help="Fail only on NET-NEW breaks vs the plan's baseline_broken (git-HEAD fallback for older plans).")
    p_verify.add_argument("--baseline-count", type=int, help="Accept up to N pre-existing broken refs.")
    p_verify.add_argument("--json", action="store_true")

    p_prune = sub.add_parser("prune-empty", help="Recursively rmdir empty dirs under a root (bottom-up).")
    p_prune.add_argument("--root", required=True)
    p_prune.add_argument("--dry-run", action="store_true")
    p_prune.add_argument("--json", action="store_true")

    p_sweep = sub.add_parser("sweep", help="Auto-file unambiguous recent loose files (never throws).")
    # Default None -> watermark-driven (see effective_since_minutes). A fixed
    # lookback made files older than the window permanently invisible.
    p_sweep.add_argument("--since-minutes", type=int, default=None)
    p_sweep.add_argument("--json", action="store_true")

    args = ap.parse_args()

    if args.command == "plan":
        plan = build_plan(Path(args.project))
        if args.out:
            write_json(Path(args.out), plan)
        if args.json:
            print(json.dumps(plan, indent=2))
        else:
            print_plan(plan)
            if args.out:
                print(f"Plan written: {args.out}")
        return 0

    if args.command == "apply":
        plan = json.loads(Path(args.plan).read_text(encoding="utf-8"))
        receipt = apply_plan(plan, Path(args.receipt) if args.receipt else None,
                             dry_run=args.dry_run)
        if receipt.get("dry_run"):
            if args.json:
                print(json.dumps(receipt, indent=2))
            return 0
        if args.json:
            print(json.dumps(receipt, indent=2))
        else:
            print(f"Moved: {len(receipt['moves'])}  Skipped: {len(receipt['skipped'])}  "
                  f"Pruned: {len(receipt['pruned_dirs'])}  Files rewritten: {len(receipt['rewrites'])}")
            for m in receipt["moves"]:
                print(f"  {_display(Path(m['from']))} -> {_display(Path(m['to']))}")
            print(f"Receipt: {receipt['receipt_path']}")
            print(f"Revert:  {receipt['revert_script']}")
        return 0

    if args.command == "verify":
        result = verify_project(
            Path(args.project),
            against_plan=Path(args.against_plan) if args.against_plan else None,
            baseline_count=args.baseline_count,
        )
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_verify(result)
        return 0 if result["ok"] else 1

    if args.command == "prune-empty":
        removed = prune_empty(Path(args.root), args.dry_run)
        tag = "[dry-run] " if args.dry_run else ""
        if args.json:
            print(json.dumps({"dry_run": args.dry_run, "removed": [str(d) for d in removed]}, indent=2))
        else:
            print(f"{tag}pruned {len(removed)} empty dir(s)")
            for d in removed:
                print(f"  {_display(d)}")
        return 0

    if args.command == "sweep":
        try:
            result = sweep(args.since_minutes)
        except Exception as exc:
            print(f"SWEEP: degraded — {type(exc).__name__}: {exc}")
            return 0
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"SWEEP: auto-filed {result['auto_moved']} file(s) across "
                  f"{len(result['projects'])} project(s); {result['needs_judgment']} need judgment")
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
