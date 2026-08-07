#!/usr/bin/env python3
"""project_relocate.py — move a whole project directory WITH its inbound links.

`project_filer.py` files loose files *inside* a project. Nothing moved a project
*directory*, so the only way to do it was a bare `mv` — which
`directives/artifact-placement.md` forbids, because it orphans every inbound
reference. This closes that gap.

Unlike project_filer, this DOES rewrite control-plane referrers (CLAUDE.md,
.agent/workflows/, skills/, execution/). It has to: when a directory moves, a
hardcoded project path in CLAUDE.md is not a pin to respect, it is a broken
path. Every rewrite is listed before it happens and recorded in a receipt.

(Deliberately no literal project path appears in this file — it would make the
tool a referrer to its own examples and rewrite its own documentation.)

Usage:
  python3 execution/project_relocate.py plan  <src-rel> <dst-rel>
  python3 execution/project_relocate.py apply <src-rel> <dst-rel> [--stub]

  --stub   leave a pointer file at the old location (for archive moves, so a
           grep still finds where the work went). Never used for live moves.

Safety contract, same as project_filer:
  * `plan` writes nothing.
  * `apply` uses `git mv` (history preserved), rewrites every referrer,
    appends an inverse to .agent/organization/REVERT-<date>.sh, and writes a
    receipt to .agent/organization/receipts/.
  * Nothing is ever deleted.
  * Refuses if the destination exists.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ORG_HOME = ROOT / ".agent" / "organization"
RECEIPTS = ORG_HOME / "receipts"

# Never rewrite inside these: frozen historical records and machine ledgers whose
# whole purpose is to remember the OLD path.
FROZEN = (
    "_system/organization/inbox/",
    "_system/organization/backlog-maps/",
    "_system/organization/manifest.json",
    "_system/organization/move-ledger.jsonl",
    "_system/organization/aliases.json",
    ".agent/organization/receipts/",
    ".agent/organization/REVERT-",
    # A move-plan is a before/after record. Rewriting it to the after-state makes
    # it describe moves it says haven't happened yet — history, not a live pointer.
    "/move-plan.md",
    ".git/",
    # 2026-08-07: protected by NEITHER tool before today. An append-only asset
    # index keyed by live path (5,032 lines, one _active/ research path alone
    # accounts for them) — regenerate it after a move via asset_index.py,
    # never rewrite it in place.
    ".agent/assets/manifest.jsonl",
    ".agent/organization/sweep-state.json",
    "_active/_ledgers/",
)

TEXT_SUFFIXES = {".md", ".py", ".json", ".jsonl", ".js", ".ts", ".tsx", ".yml",
                 ".yaml", ".txt", ".sh", ".html", ".toml", ".cfg"}


def _git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


class GrepFailure(RuntimeError):
    """A referrer scan failed. An empty result must never be read as "no
    referrers" — that silently downgrades a move to one with zero rewrites."""


def _is_frozen(line: str) -> bool:
    return any(str(line).startswith(f) or f in str(line) for f in FROZEN)


def _keep(line: str) -> bool:
    if not line.strip():
        return False
    return not _is_frozen(line)


def find_referrers(needle: str) -> list[Path]:
    """Every tracked-or-untracked text file mentioning the old path."""
    r = _git("grep", "-I", "-l", "-F", "--untracked", needle)
    if r.returncode not in (0, 1):  # 1 == no matches, which is a real answer
        raise GrepFailure(f"git grep exited {r.returncode}: {r.stderr.strip()[:200]}")
    hits = []
    for line in r.stdout.splitlines():
        if not _keep(line):
            continue
        p = ROOT / line
        if p.is_file() and (p.suffix.lower() in TEXT_SUFFIXES or not p.suffix):
            hits.append(p)
    # `git grep --untracked` still skips GITIGNORED trees — untracked is not
    # the same as ignored. Measured 2026-08-07: five real referrers inside a
    # gitignored `_build-*` tree were never offered to the rewriter and kept
    # pointing at the old path after a 439-file move. Special-casing one
    # directory was not enough; sweep the whole repo with plain grep and union.
    r2 = subprocess.run(
        ["grep", "-rIlF", "--exclude-dir=.git", "--exclude-dir=node_modules",
         "--exclude-dir=.venv", needle, str(ROOT)],
        capture_output=True, text=True, timeout=300)
    if r2.returncode not in (0, 1):
        raise GrepFailure(f"repo-wide grep exited {r2.returncode}")
    for line in r2.stdout.splitlines():
        if not line.strip():
            continue
        rel = line[len(str(ROOT)) + 1:] if line.startswith(str(ROOT)) else line
        if not _keep(rel):
            continue
        p = Path(line)
        if p.is_file() and (p.suffix.lower() in TEXT_SUFFIXES or not p.suffix):
            hits.append(p)
    # The user-memory dir lives outside the repo; project_filer rewrites it too.
    mem = Path.home() / ".claude" / "projects" / "-Users-farricecain-Google-Antigravity" / "memory"
    if mem.is_dir():
        r3 = subprocess.run(["grep", "-rIlF", needle, str(mem)],
                            capture_output=True, text=True, timeout=180)
        if r3.returncode not in (0, 1):
            raise GrepFailure(f"grep of memory dir exited {r3.returncode}")
        hits += [Path(l) for l in r3.stdout.splitlines() if l.strip()]
    return sorted(set(hits))


SENTINEL = "\x00\x00RELOCATE\x00\x00"


def rewrite(path: Path, src_rel: str, dst_rel: str) -> int:
    """Replace src_rel with dst_rel, idempotently.

    The destination usually CONTAINS the source (`deliverables/x.md` ->
    `.../04-deliverables/x.md`). A naive str.replace would then rewrite INSIDE
    an already-correct path on a second run, producing corruption like
    `.../04-_active/.../04-deliverables/x.md`. Mask the destination first so
    already-rewritten text is never touched.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return 0

    if src_rel in dst_rel:
        # Destination CONTAINS the source (deliverables/x.md ->
        # .../04-deliverables/x.md). Mask first so a second run cannot rewrite
        # inside an already-correct path. This is the original 2026-07 scar.
        masked = text.replace(dst_rel, SENTINEL)
        if src_rel not in masked:
            return 0
        n = masked.count(src_rel)
        out = masked.replace(src_rel, dst_rel).replace(SENTINEL, dst_rel)
    else:
        # SCAR 2026-08-07: when the SOURCE contains the destination — any
        # rename that SHORTENS a path, e.g. `<x>-launch` -> `<x>` — masking
        # the destination first destroyed the source string, `src_rel not in
        # masked` was true, and the function returned 0. A 439-file move
        # reported "total_rewrites: 0" and left 308 referrers pointing at a
        # path that no longer existed. Caught only because 0 looked wrong.
        #
        # Boundary guard instead: never match the source as a prefix of a
        # longer sibling name. A trailing "." or "/" still matches.
        pat = re.compile(re.escape(src_rel) + r"(?![\w-])")
        n = len(pat.findall(text))
        if not n:
            return 0
        out = pat.sub(lambda _m: dst_rel, text)

    path.write_text(out, encoding="utf-8")
    return n


def build(src_rel: str, dst_rel: str) -> dict:
    src, dst = ROOT / src_rel, ROOT / dst_rel
    if not src.exists():
        raise SystemExit(f"source does not exist: {src_rel}")
    if dst.exists():
        raise SystemExit(f"destination already exists, refusing: {dst_rel}")
    referrers = find_referrers(src_rel)
    control = [p for p in referrers
               if any(str(p.relative_to(ROOT) if ROOT in p.parents else p).startswith(c)
                      for c in ("CLAUDE.md", "AGENTS.md", "CODEX.md", "GEMINI.md",
                                "OPERATING_MANUAL.md", "directives/", "execution/",
                                "skills/", ".agent/workflows/", ".claude/"))]
    return {
        "producer": "project_relocate.py",
        "schema": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "src": src_rel, "dst": dst_rel,
        "files_in_project": (sum(1 for _ in src.rglob("*") if _.is_file())
                             if src.is_dir() else 1),
        "referrers": [str(p) for p in referrers],
        "control_referrers": [str(p) for p in control],
    }


def apply(plan: dict, stub: bool) -> dict:
    if plan.get("producer") != "project_relocate.py":
        raise SystemExit("plan not produced by project_relocate.py — refusing")
    src_rel, dst_rel = plan["src"], plan["dst"]
    src, dst = ROOT / src_rel, ROOT / dst_rel
    if dst.exists():
        raise SystemExit(f"destination appeared, refusing: {dst_rel}")

    dst.parent.mkdir(parents=True, exist_ok=True)
    r = _git("mv", src_rel, dst_rel)
    if r.returncode != 0:  # untracked dirs aren't git-movable; fall back
        import shutil
        shutil.move(str(src), str(dst))
        moved_by = "shutil (untracked)"
    else:
        moved_by = "git mv"

    # Inverse FIRST, before the rewrite phase, so a crash mid-rewrite is still
    # undoable (the 2026-07-08 lesson).
    #
    # SCAR 2026-08-07, found by actually REHEARSING the rollback: with --stub,
    # a MOVED.md pointer is left behind, so the source directory still exists
    # when the inverse runs. `mv -n <dst> <existing-dir>` then moves the tree
    # INSIDE it — producing foo/foo/ — instead of restoring it. The revert
    # reported exit 0 while silently corrupting the tree. A stubbed move must
    # clear its own stub before the inverse.
    ORG_HOME.mkdir(parents=True, exist_ok=True)
    rev = ORG_HOME / f"REVERT-{date.today().isoformat()}.sh"
    prior = rev.read_text(encoding="utf-8").splitlines() if rev.exists() else []
    body = [l for l in prior if l and not l.startswith("#!")]
    inverse = []
    if stub:
        inverse.append(f'rm -f "{src / "MOVED.md"}"')
        inverse.append(f'rmdir "{src}" 2>/dev/null || true')
    inverse.append(f'mv -n "{dst}" "{src}"')
    rev.write_text("\n".join(
        ["#!/bin/sh", "# Auto-generated inverse moves (newest first). Re-run to revert.", ""]
        + inverse + body) + "\n", encoding="utf-8")
    rev.chmod(0o755)

    rewrites = {}
    for ref in plan["referrers"]:
        p = Path(ref)
        if not p.exists():
            # Referrers that live INSIDE the moved tree were enumerated at their
            # old paths and have just moved with it. Translate, don't skip — or a
            # doc that references its own directory keeps pointing at the old
            # location and `verify` fails.
            try:
                rel = p.relative_to(ROOT / src_rel)
            except ValueError:
                continue
            p = ROOT / dst_rel / rel
            if not p.exists():
                continue
        n = rewrite(p, src_rel, dst_rel)
        if n:
            rewrites[str(p)] = n

    # Recompute the OUTBOUND relative links inside the files that just moved.
    #
    # SCAR 2026-08-07: this tool rewrote every reference TO the moved thing but
    # never touched references FROM inside it. Moving a tree to a different
    # DEPTH therefore silently broke its own links: `../02-offer/x.md` was
    # correct at <project>/00-start-here/ and points into the archive from
    # <project>/99-archive/<date>/00-start-here-june-era/. Measured: archiving
    # two dead front doors ADDED 16 broken links. project_filer.rewrite_file
    # already solves exactly this, so borrow it rather than reimplement.
    internal = 0
    if dst.is_dir():
        try:
            import project_filer as _pf
            for moved in dst.rglob("*"):
                if not moved.is_file() or moved.suffix.lower() not in {".md", ".txt"}:
                    continue
                old_dir = src / moved.relative_to(dst).parent
                # rel_pairs=[] — the src->dst string swap already ran above;
                # this pass is only for path RECOMPUTATION.
                internal += _pf.rewrite_file(moved, old_dir, {}, [])
        except Exception as exc:
            print(f"  (internal link recompute skipped: {exc})")
    if internal:
        rewrites["<internal links in moved files>"] = internal

    # A plan that found referrers but produced no rewrites is not a clean move,
    # it is a silent failure — that is exactly how the prefix bug above shipped
    # a 439-file move with 308 orphaned referrers and printed a tidy receipt.
    # Say it loudly; the REVERT script is already written at this point.
    expected = [r for r in plan["referrers"] if not _is_frozen(r)]
    substantive = sum(v for k, v in rewrites.items() if not k.startswith("<"))
    if expected and substantive == 0:
        print(f"!! WARNING: {len(expected)} referrer(s) were found but ZERO were "
              f"rewritten. Every one of them still points at {src_rel!r}.")
        print(f"!! This move is NOT complete. Revert with: sh {rev}")

    if stub:
        src.mkdir(parents=True, exist_ok=True)
        (src / "MOVED.md").write_text(
            f"# Moved\n\nThis project now lives at `{dst_rel}`.\n\n"
            f"Relocated {date.today().isoformat()} by the global org sweep. "
            f"Nothing was deleted — the full contents moved intact.\n",
            encoding="utf-8")

    receipt = {
        "version": 1, "applied_at": datetime.now(timezone.utc).isoformat(),
        "action": "project-relocate", "moved_by": moved_by,
        "src": src_rel, "dst": dst_rel, "stub_left": stub,
        "files_moved": plan["files_in_project"],
        "rewrites": rewrites, "total_rewrites": sum(rewrites.values()),
        "revert_script": str(rev),
    }
    RECEIPTS.mkdir(parents=True, exist_ok=True)
    rp = RECEIPTS / f"{date.today().isoformat()}-relocate-{Path(dst_rel).name.replace(' ', '_')}.json"
    rp.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    receipt["receipt_path"] = str(rp)

    with (ROOT / "_system" / "organization" / "move-ledger.jsonl").open("a") as fh:
        fh.write(json.dumps({"action": "project-relocate",
                             "moved_at": receipt["applied_at"],
                             "from": src_rel, "to": dst_rel,
                             "tool": "project_relocate.py"}) + "\n")
    return receipt


def verify(src_rel: str, dst_rel: str) -> dict:
    """Zero live references to the old path (frozen ledgers excluded).

    The destination frequently CONTAINS the source as a substring — moving
    `deliverables/x.md` into `.../04-deliverables/x.md` means a correctly
    rewritten file still literally contains the old string. Blank the new path
    out first, then look for genuine leftovers; otherwise every such move
    reports a false failure and halts a good run.
    """
    stale = []
    for p in find_referrers(src_rel):
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if src_rel in text.replace(dst_rel, "\x00"):
            stale.append(str(p.relative_to(ROOT)) if ROOT in p.parents else str(p))
    # .exists(), not .is_dir() — this tool relocates single files too.
    return {"stale_referrers": stale, "ok": not stale,
            "destination_exists": (ROOT / dst_rel).exists()}


def main() -> int:
    if len(sys.argv) < 4:
        print(__doc__)
        return 1
    cmd, src_rel, dst_rel = sys.argv[1], sys.argv[2].rstrip("/"), sys.argv[3].rstrip("/")

    if cmd == "plan":
        plan = build(src_rel, dst_rel)
        print(json.dumps(plan, indent=2))
        return 0
    if cmd == "apply":
        plan = build(src_rel, dst_rel)
        receipt = apply(plan, stub="--stub" in sys.argv)
        print(json.dumps(receipt, indent=2))
        return 0
    if cmd == "verify":
        v = verify(src_rel, dst_rel)
        print(json.dumps(v, indent=2))
        return 0 if v["ok"] else 1
    print(f"unknown command: {cmd}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
