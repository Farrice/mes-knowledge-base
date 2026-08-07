#!/usr/bin/env python3
"""front_door.py — the one generated entry point per initiative.

WHY THIS EXISTS (Farrice, 2026-08-07). `_active/linkedin/` held 440
files behind FOUR competing front doors — CAMPAIGN.md, CANON.md, INDEX.md and
04-deliverables/00-CONTROL-TOWER.md, the last of which announced itself as
"The ONE index. Open this first" while pointing at a $500 offer killed five
weeks earlier. Opening that folder cost real energy and produced no answer.

THE CANONICAL-STAMP TRAP (his diagnosis, and it was correct). A doc stamped
`status: canonical` becomes an over-powerful attractor: every later session
cites the frozen snapshot instead of the accumulated whole, so an old file
outranks newer cumulative work. Proof, live in the repo the day this was
written: CANON.md marked 03-launch/2026-07-28-PROFILE-GO-LIVE-TONIGHT.md
canonical while the actual current profile work was the 2026-08-06 rebuild.

THE RULE THAT REPLACES THE STAMP:

    A filename that LEADS with YYYY-MM-DD- is a RECORD.
    It is never truth and is never built on.

    A filename with no leading date is LIVING.
    It sits at the bucket root and is updated in place.

The marker is positional and machine-checkable, so nothing has to be
maintained and nothing can lie. "Current" comes from git, never from a stamp.

This module only READS (tree + git + frontmatter) and writes START-HERE.md /
START-HERE.html. Because every value is derived at build time, the front door
cannot go stale — the failure mode it replaces is structurally impossible here.

Usage:
    python3 execution/front_door.py build _active/linkedin/profile
    python3 execution/front_door.py build --all
    python3 execution/front_door.py check _active/linkedin/profile   # never blocks
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import render_brief  # noqa: E402
from canon_audit import frontmatter  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
ACTIVE = ROOT / "_active"

# A record announces itself in its first ten characters. Nothing else counts:
# a date elsewhere in the name (icp-2026.md) is a topic, not a timestamp.
RECORD_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})[-_]")

SKIP_DIRS = {".git", "node_modules", ".venv", "__pycache__", ".DS_Store",
             "90-exports"}
ARCHIVE_DIRS = {"99-archive", "_archive", "archive"}

# Pinned by name — contracts with other tools, never counted as living docs.
PINNED = {"INDEX.md", "README.md", "CLAUDE.md", "RISKS.md", "CANON.md",
          "CAMPAIGN.md", "MOVED.md", "AGENTS.md", "CODEX.md", "GEMINI.md",
          "START-HERE.md", "START-HERE.html"}

DOC_SUFFIXES = {".md", ".txt"}
MEDIA_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".mp4",
                  ".mov", ".mp3", ".wav", ".pdf", ".html"}

# Names that claim to be an index. More than one of these in a tree is the
# four-front-doors failure recurring — report it, never touch it.
FRONT_DOOR_CLAIM_RE = re.compile(
    r"(START.?HERE|CONTROL.?TOWER|MASTER.?INDEX|READ.?THIS.?FIRST|^INDEX)", re.I)

# Version noise stripped before grouping, so profile-copy-v8-POP.md and
# profile-copy.md land in the same slot and surface as competitors.
_VERSION_RE = re.compile(
    r"(-v\d+(\.\d+)?|-final|-draft|-copy|-new|-old|-latest|-master|"
    r"-pop|-clean|-polished|-\d{1,2})$", re.I)

# A commit touching this many files inside ONE initiative is housekeeping
# (a sweep, an org pass), not evidence that anyone worked on those files.
BULK_COMMIT_FILES = 40


# ── discovery ────────────────────────────────────────────────────────────────

def _iter_files(base: Path):
    for p in base.rglob("*"):
        if not p.is_file():
            continue
        parts = set(p.relative_to(base).parts)
        if parts & SKIP_DIRS or p.name == ".DS_Store":
            continue
        yield p


def is_arena(path: Path) -> bool:
    """An arena holds initiatives and nothing of its own but pinned files."""
    if not path.is_dir():
        return False
    kids = [c for c in path.iterdir() if c.name not in SKIP_DIRS]
    dirs = [c for c in kids if c.is_dir()]
    own = [c for c in kids if c.is_file() and c.name not in PINNED]
    return bool(dirs) and not own


def discover_initiatives() -> list[Path]:
    out: list[Path] = []
    if not ACTIVE.is_dir():
        return out
    for child in sorted(ACTIVE.iterdir()):
        if not child.is_dir() or child.name.startswith(".") or child.name in SKIP_DIRS:
            continue
        if is_arena(child):
            out += [g for g in sorted(child.iterdir())
                    if g.is_dir() and g.name not in SKIP_DIRS]
        else:
            out.append(child)
    return out


# ── git dating ───────────────────────────────────────────────────────────────

_DATE_CACHE: dict[str, dict[str, int]] = {}


def git_dates(base: Path) -> dict[str, int]:
    """repo-relative path -> newest non-bulk commit timestamp. One subprocess.

    Bulk commits are kept only as a fallback: a file whose ONLY history is a
    sweep still deserves a real date, but a sweep must not make every file in
    the tree read as touched today.

    SCOPE IS `_active/`, NOT THE INITIATIVE — and that is load-bearing.
    Scoping the log to the initiative path meant that the moment a project was
    renamed or restructured, `git log -- <new path>` had no history at all:
    every file fell back to filesystem mtime, every date read as "today", and
    because the dates were uniform nothing could appear newer than anything
    else. Reorganising a folder silently destroyed the one signal Farrice
    asked for ("dated so I know what's current"). Measured: the pilot's 16
    unabsorbed records dropped to 0 the instant the directory was renamed.

    So: scan `_active/` once with --name-status -M, follow renames backwards,
    and key every historical path to the path it occupies TODAY. Cached per
    process — one subprocess no matter how many initiatives are built.
    """
    try:
        base.relative_to(ROOT)
    except ValueError:
        return {}
    full = _git_dates_all()
    prefix = str(base.relative_to(ROOT)) + "/"
    return {k: v for k, v in full.items() if k.startswith(prefix)}


def _git_dates_all() -> dict[str, int]:
    if "all" in _DATE_CACHE:
        return _DATE_CACHE["all"]
    rel = "_active"
    try:
        # %at (AUTHOR time), not %ct. A rebased or merged commit carries a
        # later committer date, which made the board disagree with what plain
        # `git log --date=short` shows for the same file.
        #
        # core.quotepath=false is load-bearing: by default git octal-escapes
        # any non-ASCII byte in --name-only output ("…2025\342\200\2262026.md"),
        # so those paths never matched a key here and silently fell through to
        # filesystem mtime — which in a fresh worktree is checkout time, i.e.
        # today. One real file was reading five weeks newer than the truth.
        # --diff-merges=first-parent is load-bearing too: by default
        # --name-only prints NO filenames for a merge commit. Worktree lanes
        # are the standard workflow in this repo, so anything that landed via
        # a lane merge was absent from this map entirely and fell through to
        # mtime — i.e. read as "touched today", forever. Caught by
        # cross-checking every file against `git log --date=short`.
        proc = subprocess.run(
            # -M5% -l0: a move that ALSO rewrites the file's contents (exactly
            # what a relocation does — it repoints every inbound link) can drop
            # below git's default 50% similarity threshold and get recorded as
            # delete+add instead of a rename. The alias chain then breaks and
            # the file loses its history. Low threshold, no rename limit.
            ["git", "-c", "core.quotepath=false", "log",
             "--pretty=format:C%at", "--name-status", "-M5%", "-l0",
             "--diff-merges=first-parent", "--", rel],
            cwd=ROOT, capture_output=True, text=True, timeout=180,
        )
    except (OSError, subprocess.SubprocessError):
        return {}
    if proc.returncode != 0:
        return {}

    # Three tiers, best first. A date is only as good as the evidence that
    # someone actually WORKED on the file that day.
    #   focused  — authored/modified in a small, focused commit
    #   bulk     — authored/modified inside a housekeeping commit
    #   renamed  — the file only ever MOVED that day. Not work at all; used
    #              only so nothing ends up dateless.
    #
    # SCAR 2026-08-07: renames used to count as touches. A file whose entire
    # history is reorganisations (moved 2026-07-01 by a hub reshuffle, moved
    # again today) then read as "touched today" — so this very reorganisation
    # would have made every dead file in the tree look freshly worked on,
    # which is precisely backwards.
    focused: dict[str, int] = {}
    bulk: dict[str, int] = {}
    renamed: dict[str, int] = {}
    # historical path -> the path that content occupies TODAY. Built walking
    # newest -> oldest, so by the time an old commit names an old path we
    # already know where it ended up.
    alias: dict[str, str] = {}
    stamp: int | None = None
    batch: list[str] = []
    moves: list[str] = []

    def present(path: str) -> str:
        seen = set()
        while path in alias and path not in seen:
            seen.add(path)
            path = alias[path]
        return path

    def flush() -> None:
        if stamp is None:
            return
        if batch:
            target = bulk if len(batch) >= BULK_COMMIT_FILES else focused
            for f in batch:
                target.setdefault(f, stamp)
        for f in moves:
            renamed.setdefault(f, stamp)

    for line in proc.stdout.splitlines():
        if line.startswith("C") and line[1:].isdigit():
            flush()
            stamp = int(line[1:])
            batch, moves = [], []
            continue
        if not line.strip():
            continue
        parts = line.split("\t")
        code = parts[0]
        if code.startswith("R") and len(parts) >= 3:
            old, new = parts[1], parts[2]
            cur = present(new)
            alias[old] = cur
            moves.append(cur)          # a move is not work
        elif len(parts) >= 2:
            batch.append(present(parts[1]))
    flush()

    for tier in (bulk, renamed):
        for k, v in tier.items():
            focused.setdefault(k, v)
    _DATE_CACHE["all"] = focused
    return focused


def _fmt(ts: int | None) -> str:
    """LOCAL time, deliberately. `git log --date=short` and Farrice both read
    dates in local time; formatting in UTC pushed every evening commit to the
    next day and made the board disagree with git about what happened when."""
    if not ts:
        return "—"
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%d")


# ── the scan ─────────────────────────────────────────────────────────────────

def _slot(stem: str) -> str:
    s = stem.lower()
    while True:
        nxt = _VERSION_RE.sub("", s)
        if nxt == s:
            return nxt
        s = nxt


def scan(base: Path) -> dict:
    dates = git_dates(base)
    living: list[dict] = []
    records: list[dict] = []
    media: dict[str, int] = {}
    archived = 0
    drift: list[str] = []
    claims: list[str] = []

    for p in _iter_files(base):
        rel_repo = str(p.relative_to(ROOT))
        rel_proj = str(p.relative_to(base))
        parts = p.relative_to(base).parts
        bucket = parts[0] if len(parts) > 1 else "(root)"

        if set(parts) & ARCHIVE_DIRS:
            archived += 1
            continue

        ts = dates.get(rel_repo)
        if ts is None:
            try:
                ts = int(p.stat().st_mtime)
            except OSError:
                ts = None

        if p.suffix.lower() in MEDIA_SUFFIXES and p.name not in PINNED:
            media[bucket] = media.get(bucket, 0) + 1
            continue
        if p.suffix.lower() not in DOC_SUFFIXES:
            continue

        entry = {"path": rel_repo, "rel": rel_proj, "bucket": bucket,
                 "name": p.name, "ts": ts, "date": _fmt(ts)}

        m = RECORD_RE.match(p.name)
        if m:
            records.append(entry)
            continue
        if p.name in PINNED:
            if FRONT_DOOR_CLAIM_RE.search(p.stem) and p.name != "INDEX.md":
                claims.append(rel_proj)
            continue
        if FRONT_DOOR_CLAIM_RE.search(p.stem):
            claims.append(rel_proj)

        try:
            fm = frontmatter(p.read_text(errors="replace"))
        except OSError:
            fm = {}
        if (fm.get("status") or "").lower() == "canonical":
            drift.append(f"`{rel_proj}` still carries `status: canonical` — "
                         "delete the stamp; position and date are the truth now")
        entry["slot"] = f"{bucket}/{_slot(p.stem)}"
        living.append(entry)

    living.sort(key=lambda e: e["ts"] or 0, reverse=True)
    records.sort(key=lambda e: e["ts"] or 0, reverse=True)

    # Competing versions: >1 living doc collapsing to the same slot.
    groups: dict[str, list[dict]] = {}
    for e in living:
        groups.setdefault(e["slot"], []).append(e)
    competing = {k: v for k, v in groups.items() if len(v) > 1}

    # Unabsorbed: a record newer than everything living in its own bucket.
    #
    # A bucket with NO living doc is a different (and worse) condition: every
    # record there would read as unabsorbed, which is one message repeated N
    # times. Report that bucket once, by name, and keep the unabsorbed list
    # meaning what it says — work that outran a living doc that exists.
    newest_living: dict[str, int] = {}
    for e in living:
        b = e["bucket"]
        if e["ts"] and e["ts"] > newest_living.get(b, 0):
            newest_living[b] = e["ts"]
    record_buckets = {r["bucket"] for r in records}
    homeless = sorted(b for b in record_buckets if b not in newest_living)
    unabsorbed = [r for r in records
                  if r["bucket"] in newest_living and r["ts"]
                  and r["ts"] > newest_living[r["bucket"]]]
    homeless_detail = [
        {"bucket": b, "count": sum(1 for r in records if r["bucket"] == b),
         "newest": max((r["date"] for r in records if r["bucket"] == b), default="—")}
        for b in homeless
    ]

    if len(claims) > 1:
        drift.append("**" + str(len(claims)) + " files claim to be the front door** — "
                     + ", ".join(f"`{c}`" for c in sorted(claims)[:6])
                     + ". START-HERE.md is the front door; the rest are history.")

    return {"base": base, "living": living, "records": records,
            "unabsorbed": unabsorbed, "homeless": homeless_detail,
            "competing": competing,
            "media": media, "archived": archived, "drift": drift,
            "claims": claims}


def broken_link_count(base: Path) -> int | None:
    try:
        import project_filer
        return len(project_filer.scan_broken_refs(base))
    except Exception:
        return None


# ── render: markdown ─────────────────────────────────────────────────────────

def _title(base: Path) -> str:
    return base.name.replace("-", " ").replace("_", " ").title()


def render_md(s: dict, broken: int | None) -> str:
    base: Path = s["base"]
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    L: list[str] = []
    L.append(f"# {_title(base)} — start here")
    L.append("")
    L.append(f"*Generated {now} by `execution/front_door.py`. Do not edit — "
             f"every line is derived from the tree and from git, so it cannot go stale. "
             f"Dates are when the file was last actually WORKED ON: a commit that "
             f"touches {BULK_COMMIT_FILES}+ files here is housekeeping and does not "
             f"count, so a date may read older than `git log`.*")
    L.append("")
    L.append("> **Undated filename = LIVING** (current, update it in place). "
             "**Filename leading with a date = RECORD** (a session receipt — "
             "never truth, never build on it).")
    L.append("")

    L.append("## Live now")
    L.append("")
    if not s["living"]:
        L.append("*Nothing living here yet.*")
    else:
        by_bucket: dict[str, list[dict]] = {}
        for e in s["living"]:
            by_bucket.setdefault(e["bucket"], []).append(e)
        for bucket in sorted(by_bucket):
            L.append(f"**{bucket}**")
            L.append("")
            for e in by_bucket[bucket]:
                L.append(f"- `{e['rel']}` — touched {e['date']}")
            L.append("")

    if s["homeless"]:
        L.append("## ⚠ Folders with no living doc")
        L.append("")
        L.append("Every file here is a dated record. There is nothing current "
                 "to read or update — so the next session picks whichever "
                 "snapshot it finds first. Promote one file to a living doc "
                 "(drop the date from its name) or fold them into one.")
        L.append("")
        for h in s["homeless"]:
            L.append(f"- `{h['bucket']}` — {h['count']} records, "
                     f"nothing living. Newest: {h['newest']}")
        L.append("")

    if s["unabsorbed"]:
        L.append("## ⚠ Unabsorbed records")
        L.append("")
        L.append("Session work newer than the living doc in the same folder. "
                 "Fold it in, or the next session builds on the older truth.")
        L.append("")
        for e in s["unabsorbed"][:12]:
            L.append(f"- `{e['rel']}` ({e['date']}) — newer than everything "
                     f"living in `{e['bucket']}`")
        L.append("")

    if s["competing"]:
        L.append("## Competing versions")
        L.append("")
        L.append("Several undated files claim the same slot. One is the living "
                 "doc; the rest belong in `99-archive/` or need a date prefix.")
        L.append("")
        for slot, items in sorted(s["competing"].items()):
            L.append(f"- **{slot}** — {len(items)} files: "
                     + ", ".join(f"`{i['rel']}` ({i['date']})" for i in items[:8]))
        L.append("")

    if s["records"]:
        L.append("## Recent records")
        L.append("")
        for e in s["records"][:10]:
            L.append(f"- {e['date']} — `{e['rel']}`")
        L.append("")

    if s["drift"]:
        L.append("## Drift")
        L.append("")
        for d in s["drift"]:
            L.append(f"- {d}")
        L.append("")

    if s["media"]:
        L.append("## Media")
        L.append("")
        for b, n in sorted(s["media"].items(), key=lambda kv: -kv[1]):
            L.append(f"- `{b}` — {n} file(s)")
        L.append("")

    L.append("## Health")
    L.append("")
    L.append(f"- living docs: {len(s['living'])}")
    L.append(f"- records: {len(s['records'])}")
    L.append(f"- archived (not counted above): {s['archived']}")
    if broken is not None:
        L.append(f"- broken links in this tree: {broken}")
    L.append("")

    sibs = [d for d in sorted(base.parent.iterdir())
            if d.is_dir() and d != base and d.name not in SKIP_DIRS]
    if sibs and base.parent != ACTIVE:
        L.append("## Elsewhere in this arena")
        L.append("")
        for d in sibs:
            L.append(f"- `{d.name}/`")
        L.append("")

    return "\n".join(L) + "\n"


# ── render: HTML board (inherits the Premium Minimal dialect) ────────────────

def build_brief(s: dict, broken: int | None) -> dict:
    base: Path = s["base"]
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    arena = base.parent.name if base.parent != ACTIVE else "_active"
    sections: list[dict] = []

    dec_items = [{"action": f"{h['bucket']}/ has no living doc",
                  "why": f"{h['count']} dated records, nothing current "
                         f"(newest {h['newest']}). Promote one, or fold them into one."}
                 for h in s["homeless"]]
    dec_items += [{"action": e["rel"],
                   "why": f"{e['date']} — newer than everything living in {e['bucket']}"}
                  for e in s["unabsorbed"][:8]]
    if dec_items:
        sections.append({
            "kind": "decision",
            "heading": "What has outrun its living doc",
            "kicker": "FOLD THIS IN",
            "dek": ("Until these are folded in, the next session builds on the "
                    "older truth — the exact failure the canonical stamp used to cause."),
            "items": dec_items[:10],
        })

    if s["living"]:
        sections.append({
            "kind": "assets",
            "heading": "Live now",
            "tag": "THE LIVING SET",
            "items": [{"title": e["name"], "role": e["bucket"],
                       "note": f"touched {e['date']}", "path": e["path"]}
                      for e in s["living"][:40]],
        })

    stats = [{"value": len(s["living"]), "label": "living docs"},
             {"value": len(s["records"]), "label": "records"},
             {"value": s["archived"], "label": "archived"}]
    if broken is not None:
        stats.append({"value": broken, "label": "broken links",
                      "note": "0 is the target"})
    if s["media"]:
        stats.append({"value": sum(s["media"].values()), "label": "media files"})
    sections.append({"kind": "stats", "heading": "Health", "tag": "DERIVED",
                     "items": stats})

    if s["records"]:
        sections.append({
            "kind": "timeline",
            "heading": "Recent records",
            "tag": "HISTORY, NOT TRUTH",
            "items": [{"date": e["date"], "title": e["name"],
                       "body": e["bucket"], "done": True}
                      for e in s["records"][:10]],
        })

    body: list[str] = []
    for slot, items in sorted(s["competing"].items()):
        body.append(f"**{slot}** — {len(items)} undated files claim this slot: "
                    + ", ".join(f"{i['rel']} ({i['date']})" for i in items[:6]))
    body += s["drift"]
    if body:
        sections.append({"kind": "caveats", "heading": "Drift",
                         "kicker": "WORTH TEN MINUTES",
                         "body": "\n\n".join(body)})

    sibs = [d for d in sorted(base.parent.iterdir())
            if d.is_dir() and d != base and d.name not in SKIP_DIRS]
    if sibs and base.parent != ACTIVE:
        sections.append({
            "kind": "related", "heading": "Elsewhere in this arena",
            "links": [{"k": "INITIATIVE", "title": d.name,
                       "path": str((d / "START-HERE.html").relative_to(ROOT))}
                      for d in sibs],
        })

    return {
        "slug": base.name,
        "chip": f"START HERE · {arena.upper()}",
        "title": _title(base),
        "dek": ("Undated filename = living and current. A filename leading with "
                "a date is a record — a receipt of one session, never the truth "
                "to build on."),
        "window": f"{len(s['living'])} living",
        "lens": arena,
        "sources": f"{len(s['living']) + len(s['records'])} docs",
        "compiled": now,
        "footer_left": "ANTIGRAVITY · FRONT DOOR",
        "footer_right": "generated — do not edit",
        "sections": sections,
    }


# ── build / check ────────────────────────────────────────────────────────────

def build(base: Path, quiet: bool = False) -> dict:
    s = scan(base)
    broken = broken_link_count(base)
    (base / "START-HERE.md").write_text(render_md(s, broken), encoding="utf-8")
    brief = build_brief(s, broken)
    try:
        html = render_brief.render(brief, share=False)
        (base / "START-HERE.html").write_text(html, encoding="utf-8")
        html_ok = True
    except Exception as exc:  # never let a render bug block the md front door
        html_ok = False
        if not quiet:
            print(f"  (html skipped: {exc})", file=sys.stderr)

    state = {"generated": datetime.now(timezone.utc).isoformat(),
             "living": len(s["living"]), "records": len(s["records"]),
             "unabsorbed": len(s["unabsorbed"]),
             "competing": len(s["competing"]),
             "broken_links": broken, "html": html_ok}
    sysdir = base / "06-system"
    sysdir.mkdir(exist_ok=True)
    (sysdir / "front-door.state.json").write_text(
        json.dumps(state, indent=2) + "\n", encoding="utf-8")
    if not quiet:
        rel = base.relative_to(ROOT)
        print(f"{rel}: {len(s['living'])} living · {len(s['records'])} records "
              f"· {len(s['unabsorbed'])} unabsorbed · {len(s['competing'])} competing"
              + (f" · {broken} broken links" if broken is not None else ""))
    return state


def check(base: Path) -> int:
    """Report only. Exit 0 always — nothing here may block work."""
    s = scan(base)
    rel = base.relative_to(ROOT)
    if s["unabsorbed"]:
        print(f"{rel}: {len(s['unabsorbed'])} unabsorbed record(s) — "
              f"newest is {s['unabsorbed'][0]['rel']}")
    if s["competing"]:
        print(f"{rel}: {len(s['competing'])} slot(s) with competing versions")
    if len(s["claims"]) > 1:
        print(f"{rel}: {len(s['claims'])} files claim to be the front door")
    return 0


def _resolve(arg: str) -> Path:
    p = Path(arg)
    if not p.is_absolute():
        p = ROOT / arg
    return p.resolve()


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate the one front door per initiative.")
    sub = ap.add_subparsers(dest="command", required=True)
    b = sub.add_parser("build", help="Write START-HERE.md + START-HERE.html.")
    b.add_argument("path", nargs="?")
    b.add_argument("--all", action="store_true")
    b.add_argument("--quiet", action="store_true")
    c = sub.add_parser("check", help="Report drift. Never blocks.")
    c.add_argument("path", nargs="?")
    c.add_argument("--all", action="store_true")
    args = ap.parse_args()

    if args.command == "build":
        targets = discover_initiatives() if args.all else [_resolve(args.path)]
        for t in targets:
            if t.is_dir():
                build(t, quiet=args.quiet)
        return 0

    targets = discover_initiatives() if args.all else [_resolve(args.path)]
    for t in targets:
        if t.is_dir():
            check(t)
    return 0


if __name__ == "__main__":
    sys.exit(main())
