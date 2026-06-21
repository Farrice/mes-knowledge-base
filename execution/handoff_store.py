#!/usr/bin/env python3
"""
handoff_store.py — Durable handoff persistence + resume backstop.

The Matt Pocock `/handoff` skill writes to the OS temp dir (ephemeral — macOS
clears it on reboot). This script copies handoffs into a version-controlled
store so they survive reboots, land in git, and let `/session-kickoff`
deterministically resume the most recent one. It is the deterministic backstop
the handoff/resume loop runs on — no reliance on the model remembering a path.

Store layout (<repo-root>/.agent/handoffs/):
  YYYY-MM-DD-slug.md   one file per handoff (copied verbatim from the source)
  index.md             chronological index, newest first (auto-rebuilt)
  LATEST.md            self-contained copy of the most recent handoff (resume here)

Usage:
  python execution/handoff_store.py save <source.md> [--slug S] [--date YYYY-MM-DD] [--overwrite]
  python execution/handoff_store.py save --from-temp   # auto-find newest handoff-*.md in OS temp dir
  python execution/handoff_store.py latest [--content]  # path (or full text) of newest; exit 1 if none
  python execution/handoff_store.py list                # print the index
  python execution/handoff_store.py reindex             # rebuild index.md + LATEST.md from disk
  python execution/handoff_store.py path                # print the store dir
"""
import sys
import re
import shutil
import tempfile
import argparse
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STORE = ROOT / ".agent" / "handoffs"
INDEX = STORE / "index.md"
LATEST = STORE / "LATEST.md"
RESERVED = {"index.md", "LATEST.md"}
NAME_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SUMMARY_CAP = 400


def slugify(s: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")
    return s or "handoff"


def derive_from_filename(name: str):
    """Pull a date and slug out of an arbitrary handoff filename."""
    stem = Path(name).stem
    m = re.search(r"(20\d{2}-\d{2}-\d{2})", stem)
    date = m.group(1) if m else None
    slug = re.sub(r"^handoff[-_]?", "", stem)
    if date:
        slug = slug.replace(date, "")
    return date, slugify(slug)


def store_files():
    """Handoff files, newest first by modification time (robust to same-day saves)."""
    if not STORE.exists():
        return []
    files = [p for p in STORE.glob("*.md") if p.name not in RESERVED and NAME_RE.match(p.name)]
    return sorted(files, key=lambda p: p.stat().st_mtime, reverse=True)


def _is_meta(t: str) -> bool:
    return (
        not t
        or t.startswith("#")
        or t.startswith(">")
        or t.startswith("---")
        or t.startswith("|")
        or bool(re.match(r"^\*\*[^*]+:\*\*", t))  # **Key:** value metadata
    )


def title_and_summary(path: Path):
    """First H1 as title; first real paragraph (not metadata) as the summary."""
    title = path.stem
    summary_lines = []
    started = False
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            t = line.strip()
            if t.startswith("# ") and title == path.stem and not started:
                title = t[2:].strip()
                continue
            if not started:
                if _is_meta(t):
                    continue
                started = True
                summary_lines.append(t)
            else:
                if not t or t.startswith("#"):
                    break
                summary_lines.append(t)
    except OSError:
        pass
    return title, " ".join(summary_lines)[:SUMMARY_CAP]


def rebuild():
    """Regenerate index.md and LATEST.md from disk (filesystem is the source of truth)."""
    STORE.mkdir(parents=True, exist_ok=True)
    files = store_files()

    idx = [
        "# Handoff Index",
        "",
        "Newest first. Resume the latest with `/session-kickoff` (auto) or read `LATEST.md`.",
        "",
    ]
    for p in files:
        title, summary = title_and_summary(p)
        line = f"- **{p.name[:10]}** — [{title}]({p.name})"
        if summary:
            line += f" — {summary}"
        idx.append(line)
    INDEX.write_text("\n".join(idx) + "\n", encoding="utf-8")

    if files:
        latest = files[0]
        title, _ = title_and_summary(latest)
        body = latest.read_text(encoding="utf-8")
        LATEST.write_text(
            "# Latest Handoff — resume here\n\n"
            f"**File:** {latest.name}  \n"
            f"**Full path:** .agent/handoffs/{latest.name}  \n"
            f"**Date:** {latest.name[:10]}  \n"
            f"**Title:** {title}\n\n"
            "---\n\n"
            "_Self-contained copy of the latest handoff (no need to open another file):_\n\n"
            + body
            + "\n",
            encoding="utf-8",
        )
    else:
        LATEST.write_text("# Latest Handoff\n\n(none yet)\n", encoding="utf-8")


def _newest_temp_handoff():
    tmp = Path(tempfile.gettempdir())
    cands = sorted(tmp.glob("handoff-*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
    return cands[0] if cands else None


def cmd_save(args) -> int:
    if args.from_temp:
        src = _newest_temp_handoff()
        if src is None:
            print(f"ERROR: no handoff-*.md found in temp dir ({tempfile.gettempdir()})", file=sys.stderr)
            return 1
        print(f"from-temp: {src}")
    elif args.source:
        src = Path(args.source).expanduser()
    else:
        print("ERROR: provide a source path or --from-temp", file=sys.stderr)
        return 1

    if not src.exists():
        print(f"ERROR: source not found: {src}", file=sys.stderr)
        return 1

    STORE.mkdir(parents=True, exist_ok=True)
    d_date, d_slug = derive_from_filename(src.name)
    date = args.date or d_date or datetime.now().strftime("%Y-%m-%d")
    if not DATE_RE.match(date):
        print(f"ERROR: date must be YYYY-MM-DD, got: {date!r}", file=sys.stderr)
        return 1
    slug = slugify(args.slug) if args.slug else d_slug
    dest = STORE / f"{date}-{slug}.md"

    if src.resolve() == dest.resolve():
        print(f"already stored: {dest.relative_to(ROOT)}")
        rebuild()
        return 0
    if dest.exists() and not args.overwrite:
        print(f"ERROR: {dest.name} already exists — use --slug to differentiate or --overwrite", file=sys.stderr)
        return 1

    shutil.copyfile(src, dest)
    rebuild()
    print(f"saved:  {dest.relative_to(ROOT)}")
    print(f"latest: {LATEST.relative_to(ROOT)}")
    return 0


def cmd_latest(args) -> int:
    files = store_files()
    if not files:
        print("(no handoffs yet)", file=sys.stderr)
        return 1
    if args.content:
        print(files[0].read_text(encoding="utf-8"))
    else:
        print(files[0].relative_to(ROOT))
    return 0


def cmd_list(args) -> int:
    if INDEX.exists():
        print(INDEX.read_text(encoding="utf-8"))
        return 0
    print("(no handoffs yet — index not built)", file=sys.stderr)
    return 1


def cmd_path(args) -> int:
    print(STORE.relative_to(ROOT))
    return 0


def cmd_reindex(args) -> int:
    rebuild()
    print(f"reindexed: {len(store_files())} handoff(s)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Durable handoff store + resume backstop")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("save", help="persist a handoff file into the store")
    sp.add_argument("source", nargs="?", help="path to the handoff .md (omit when using --from-temp)")
    sp.add_argument("--from-temp", action="store_true", help="auto-find the newest handoff-*.md in the OS temp dir")
    sp.add_argument("--slug", help="override the slug")
    sp.add_argument("--date", help="override the date (YYYY-MM-DD)")
    sp.add_argument("--overwrite", action="store_true", help="allow overwriting an existing same-day/slug handoff")
    sp.set_defaults(fn=cmd_save)

    lp = sub.add_parser("latest", help="print the latest handoff path (or content); exit 1 if none")
    lp.add_argument("--content", action="store_true", help="print full content instead of path")
    lp.set_defaults(fn=cmd_latest)

    sub.add_parser("list", help="print the chronological index").set_defaults(fn=cmd_list)
    sub.add_parser("path", help="print the store directory").set_defaults(fn=cmd_path)
    sub.add_parser("reindex", help="rebuild index.md + LATEST.md from disk").set_defaults(fn=cmd_reindex)

    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    raise SystemExit(main())
