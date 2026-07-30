#!/usr/bin/env python3
"""
handoff_store.py — Durable handoff store + multi-thread resume backstop.

The Matt Pocock `/handoff` skill writes to the OS temp dir (ephemeral). This
script copies handoffs into a version-controlled store, organizes them by
WORK-THREAD (not per-session file), and powers a deterministic resume picker so
`/session-kickoff` / `/resume` can reload ANY thread — not just the last one.

Design (2026-06-21 design panel + adversarial verification):
  * Unit = THREAD, not file. Many handoffs for one thread collapse to one menu
    row (the latest). Resuming a thread and ending writes back to the SAME
    thread (same day = overwrite the day's entry), so the menu stays one clean
    row per thread.
  * Each handoff carries frontmatter (thread/status/resume_hint/unfinished/
    branch/pin). Files without it fall back gracefully.
  * Selection is deterministic: pick by thread slug, keyword, or a cosmetic
    number that ALWAYS echoes the resolved thread. Numbers resolve against the
    SAME pool the default menu shows (live threads), so they can't drift onto a
    hidden done/archived thread.

Store layout (<repo-root>/.agent/handoffs/):
  YYYY-MM-DD-slug.md   one file per handoff (frontmatter + body)
  archive/             retired threads (still git-tracked, out of the menu)
  index.md             chronological index (auto-rebuilt)
  LATEST.md            self-contained copy of the most recent handoff

Usage:
  save <src.md>|--from-temp [--thread T --status S --hint H --unfinished U
        --branch B --pin --slug X --date YYYY-MM-DD --overwrite]
  list [--rich] [--all] [--limit N]      resume menu (threads; --all incl. done/archived)
  show <thread|keyword|number> [--all]   print a handoff (resolves + echoes thread)
  resume <thread|keyword|number> [--all] show + "Since this handoff" git/branch drift
  pin <thread> | unpin <thread>          float / unfloat a thread in the menu
  archive <thread> | unarchive <thread>  retire / restore a thread
  annotate <thread|kw|num> [fields]      set frontmatter on an existing handoff
  latest [--content] | reindex | path | threads
"""
import sys
import re
import shutil
import tempfile
import argparse
import difflib
import subprocess
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STORE = ROOT / ".agent" / "handoffs"
ARCHIVE = STORE / "archive"
INDEX = STORE / "index.md"
LATEST = STORE / "LATEST.md"
RESERVED = {"index.md", "LATEST.md"}
NAME_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
STATUSES = {"active", "blocked", "ready", "mid-build", "done"}
STALE_DAYS = 21
SUMMARY_CAP = 400
FM_KEYS = ("thread", "status", "resume_hint", "unfinished", "branch", "pin")


# ── parsing ─────────────────────────────────────────────────────────
def slugify(s: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")
    return s or "handoff"


def derive_from_filename(name: str):
    stem = Path(name).stem
    m = re.search(r"(20\d{2}-\d{2}-\d{2})", stem)
    date = m.group(1) if m else None
    slug = re.sub(r"^handoff[-_]?", "", stem)
    if date:
        slug = slug.replace(date, "")
    return date, slugify(slug)


def parse_frontmatter(text: str):
    """Return (fields_dict, body). Tolerant key: value subset; CRLF-safe."""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    block = text[3:end].strip("\n")
    body = text[end + 4:].lstrip("\n")
    fields = {}
    for line in block.splitlines():
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line.strip())
        if m:
            fields[m.group(1).lower()] = m.group(2).strip().strip('"').strip("'")
    return fields, body


def _clean(t: str) -> str:
    return re.sub(r"[*`]+", "", re.sub(r"^[-\d.)\s]+", "", t)).strip()


NEXT_RE = re.compile(
    r"(next session focus|remaining priorit|next steps?|next focus|where.*(restart|realign)|open (options|loops))",
    re.IGNORECASE,
)


def _grep_next_focus(body: str) -> str:
    out, capturing = [], False
    for line in body.splitlines():
        t = line.strip()
        m = re.match(
            r"^\*\*\s*(next session focus|remaining priorit\w*|next steps?|next focus)\s*\*\*[:：]?\s*(.+)",
            t, re.IGNORECASE,
        )
        if m and m.group(2).strip():
            return _clean(m.group(2))[:200]
        if not capturing:
            if (t.startswith("#") or t.startswith("**")) and NEXT_RE.search(t):
                capturing = True
            continue
        if t.startswith("#"):
            break
        if t:
            c = _clean(t)
            if c:
                out.append(c)
            if len(out) >= 2:
                break
    return " / ".join(out)[:200]


def _title_summary(body: str, fallback: str):
    title, summary = fallback, ""
    for line in body.splitlines():
        t = line.strip()
        if t.startswith("# ") and title == fallback:
            title = t[2:].strip()
        elif (t and not summary and not t.startswith("#") and not t.startswith(">")
              and not t.startswith("---") and not t.startswith("|")
              and not re.match(r"^\*\*[^*]+:\*\*", t)):
            summary = _clean(t)[:SUMMARY_CAP]
        if title != fallback and summary:
            break
    return title, summary


def read_meta(path: Path) -> dict:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        text = ""
    fm, body = parse_frontmatter(text)
    title, summary = _title_summary(body, path.stem)
    thread = slugify(fm["thread"]) if fm.get("thread") else derive_from_filename(path.name)[1]
    status = (fm.get("status") or "active").lower()
    hint = fm.get("resume_hint") or _grep_next_focus(body) or summary
    try:
        mtime = path.stat().st_mtime
    except OSError:
        mtime = 0
    return {
        "path": path, "name": path.name, "date": path.name[:10], "mtime": mtime,
        "thread": thread, "status": status,
        "resume_hint": hint, "unfinished": fm.get("unfinished", ""),
        "branch": fm.get("branch", ""),
        "pin": str(fm.get("pin", "")).lower() in ("true", "1", "yes"),
        "title": title,
    }


# ── collections ─────────────────────────────────────────────────────
def _files(folder: Path):
    if not folder.exists():
        return []
    return [p for p in folder.glob("*.md") if p.name not in RESERVED and NAME_RE.match(p.name)]


def all_metas(include_archived=False):
    metas = [read_meta(p) for p in _files(STORE)]
    if include_archived:
        metas += [read_meta(p) for p in _files(ARCHIVE)]
    # Sort by handoff DATE (true recency); mtime only a same-day tiebreak.
    return sorted(metas, key=lambda m: (m["date"], m["mtime"]), reverse=True)


def threads(include_done=False, include_archived=False):
    """Latest handoff per thread, pinned first then newest. Menu unit."""
    latest = {}
    for m in all_metas(include_archived=include_archived):  # newest-first
        latest.setdefault(m["thread"], m)
    metas = list(latest.values())
    if not include_done:  # independent of include_archived
        metas = [m for m in metas if m["status"] != "done"]
    return sorted(metas, key=lambda m: (m["pin"], m["date"], m["mtime"]), reverse=True)


def _age(date_str: str) -> str:
    try:
        days = (datetime.now().date() - datetime.strptime(date_str, "%Y-%m-%d").date()).days
        return "today" if days <= 0 else ("1d ago" if days == 1 else f"{days}d ago")
    except Exception:
        return "?"


def _stale(date_str: str) -> bool:
    try:
        return (datetime.now().date() - datetime.strptime(date_str, "%Y-%m-%d").date()).days > STALE_DAYS
    except Exception:
        return False


def resolve(selector: str, pool):
    """('ok', meta) | ('none', []) | ('many', metas). Deterministic."""
    sel = (selector or "").strip()
    if sel.isdigit():
        i = int(sel) - 1
        return ("ok", pool[i]) if 0 <= i < len(pool) else ("none", [])
    low = sel.lower()
    exact = [m for m in pool if m["thread"] == slugify(low)]
    if exact:
        return ("ok", exact[0])
    hits = [m for m in pool if low in m["thread"].lower() or low in m["title"].lower()]
    if not hits:
        return ("none", [])
    if len(hits) == 1:
        return ("ok", hits[0])
    return ("many", hits)


# ── rebuild index + LATEST ──────────────────────────────────────────
def rebuild():
    STORE.mkdir(parents=True, exist_ok=True)
    metas = all_metas()
    idx = ["# Handoff Index", "",
           "Newest first. Resume a thread with `/resume` (menu) or `/resume <thread>`.", ""]
    for m in metas:
        line = f"- **{m['date']}** [{m['thread']}/{m['status']}] [{m['title']}]({m['name']})"
        if m["resume_hint"]:
            line += f" — {m['resume_hint']}"
        idx.append(line)
    INDEX.write_text("\n".join(idx) + "\n", encoding="utf-8")

    if metas:
        m = metas[0]
        body = m["path"].read_text(encoding="utf-8")
        LATEST.write_text(
            "# Latest Handoff\n\n"
            f"**Thread:** {m['thread']}  \n**Full path:** .agent/handoffs/{m['name']}  \n"
            f"**Date:** {m['date']} ({_age(m['date'])})  \n**Status:** {m['status']}  \n"
            f"**Title:** {m['title']}\n\n"
            "> Not auto-loaded. Run `/resume` to choose any thread, or `/resume "
            f"{m['thread']}` for this one.\n\n---\n\n" + body + "\n",
            encoding="utf-8",
        )
    else:
        LATEST.write_text("# Latest Handoff\n\n(none yet)\n", encoding="utf-8")


# ── frontmatter writing ─────────────────────────────────────────────
def _render_fm(fields: dict) -> str:
    lines = ["---"]
    for k in FM_KEYS:
        if k in fields and fields[k] not in (None, ""):
            v = str(fields[k]).replace("\n", " ").replace("\r", " ").strip()
            if k == "pin":
                v = "true" if v.lower() in ("true", "1", "yes") else "false"
            lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def _write_with_fm(dest: Path, fields: dict, body: str):
    dest.write_text(_render_fm(fields) + body.lstrip("\n"), encoding="utf-8")


def _git(*a) -> str:
    try:
        r = subprocess.run(["git", "-C", str(ROOT), *a], capture_output=True, text=True, timeout=5)
        return r.stdout.strip()
    except Exception:
        return ""


# ── commands ────────────────────────────────────────────────────────
def _newest_temp():
    cands = sorted(Path(tempfile.gettempdir()).glob("handoff-*.md"),
                   key=lambda p: p.stat().st_mtime, reverse=True)
    return cands[0] if cands else None


def cmd_save(args) -> int:
    if args.from_temp:
        src = _newest_temp()
        if src is None:
            print(f"ERROR: no handoff-*.md in temp ({tempfile.gettempdir()})", file=sys.stderr)
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
    raw = src.read_text(encoding="utf-8")
    existing_fm, body = parse_frontmatter(raw)
    d_date, d_slug = derive_from_filename(src.name)
    date = args.date or existing_fm.get("date") or d_date or datetime.now().strftime("%Y-%m-%d")
    if not DATE_RE.match(date):
        print(f"ERROR: date must be YYYY-MM-DD, got: {date!r}", file=sys.stderr)
        return 1

    if args.thread:
        thread = slugify(args.thread)
    elif existing_fm.get("thread"):
        thread = slugify(existing_fm["thread"])
    else:
        thread = d_slug
        if thread == "handoff":
            print("ERROR: could not derive a thread slug — pass --thread explicitly "
                  "(e.g. --thread jen-listings)", file=sys.stderr)
            return 1

    existing_threads = {m["thread"] for m in all_metas(include_archived=True)}
    if thread not in existing_threads:
        close = difflib.get_close_matches(thread, list(existing_threads), n=1, cutoff=0.8)
        if close and not getattr(args, "new_thread", False):
            # AUTO-ADOPT (Farrice 2026-07-28): the old behavior warned about the
            # near-duplicate and then created it anyway — so duplicates stacked
            # and /resume showed two threads for one work-stream (it happened
            # the very day this shipped: 'opus5-adaptation' landed beside
            # 'opus5-adaptation-layer'). A warning nobody acts on is a log
            # line; the fix is to adopt the existing thread and say so.
            # Deliberate new thread with a similar name: pass --new-thread.
            print(f"AUTO-ADOPTED existing thread '{close[0]}' (asked-for '{thread}' is a "
                  f"near-duplicate). Deliberate separate thread? Re-run with --new-thread.",
                  file=sys.stderr)
            thread = close[0]
        elif close:
            print(f"WARNING: new thread '{thread}' is close to existing '{close[0]}' "
                  f"(--new-thread was passed, keeping them separate)", file=sys.stderr)
    if args.thread and existing_fm.get("thread") and slugify(existing_fm["thread"]) != thread:
        print(f"WARNING: source frontmatter thread='{existing_fm['thread']}' but --thread='{args.thread}' "
              "— verify this is the right handoff", file=sys.stderr)

    status = (args.status or existing_fm.get("status") or "active").lower()
    if status not in STATUSES:
        print(f"ERROR: status must be one of {sorted(STATUSES)}", file=sys.stderr)
        return 1
    slug = slugify(args.slug) if args.slug else thread
    dest = STORE / f"{date}-{slug}.md"

    if src.resolve() == dest.resolve():
        print(f"already stored: {dest.relative_to(ROOT)}")
        rebuild()
        return 0
    if dest.exists() and not args.overwrite:
        # same thread, same day = UPDATE today's entry (loop). different = clash.
        if read_meta(dest)["thread"] != thread:
            print(f"ERROR: {dest.name} exists for a different thread — use --slug or --overwrite",
                  file=sys.stderr)
            return 1

    # DO-NOT-REBUILD floor (Farrice 2026-07-28): the next session's biggest risk
    # is re-solving, and a handoff that only lists what WAS built invites exactly
    # that. Every stored handoff must carry the section; if the author omitted
    # it, scaffold it here — physically in the file, pointing at the thread's
    # prior handoff so "extend, never rebuild" has a concrete target. Mechanism,
    # not reminder: a nudge to add the section is prose, and prose doesn't fire.
    if not re.search(r"(?im)^#+\s*.*(do\s*n[o']?t\s+rebuild|not\s+rebuild)", body):
        prior = [m for m in all_metas(include_archived=True)
                 if m["thread"] == thread and m["path"].name != f"{date}-{args.slug or thread}.md"]
        prior.sort(key=lambda m: m.get("date", ""), reverse=True)
        prior_line = (f"- Previous handoff on this thread: `{prior[0]['path'].relative_to(ROOT)}` — "
                      f"everything it lists as shipped is EXTEND-ONLY.\n" if prior else
                      "- (first handoff on this thread — list shipped assets here as they land)\n")
        body = body.rstrip() + (
            "\n\n## Do NOT Rebuild (auto-scaffolded — the store adds this when a "
            "handoff omits it)\n"
            + prior_line +
            "- Before building anything named above: `/arsenal <task>` and read the "
            "prior handoff first. Re-solving shipped work is the #1 next-session "
            "failure mode.\n")
        print("scaffolded: Do-NOT-Rebuild section (was missing from the handoff body)",
              file=sys.stderr)

    fields = {
        "thread": thread, "status": status,
        "resume_hint": args.hint or existing_fm.get("resume_hint") or _grep_next_focus(body),
        "unfinished": args.unfinished or existing_fm.get("unfinished", ""),
        "branch": args.branch or existing_fm.get("branch", "") or _git("rev-parse", "--abbrev-ref", "HEAD"),
        "pin": "true" if args.pin else existing_fm.get("pin", "false"),
    }
    _write_with_fm(dest, fields, body)
    rebuild()
    print(f"saved:  {dest.relative_to(ROOT)}  [thread={thread} status={status}]")
    return 0


def cmd_list(args) -> int:
    pool = threads(include_done=args.all, include_archived=args.all)
    if not pool:
        print("(no live threads — try `list --all`)", file=sys.stderr)
        return 1
    if args.limit:
        pool = pool[: args.limit]
    if not args.rich:
        for i, m in enumerate(pool, 1):
            print(f"{i}. {m['thread']}  ({m['date']})")
        return 0
    # Apex W1 (2026-07-29): deliberately-parked work (blocked/mid-build) sorts
    # to the top of the rich menu — a parked thread is a promise to resume,
    # not an archive entry; date-only sort buried it among 166 threads.
    _parked = ("blocked", "mid-build")
    pool.sort(key=lambda m: (m.get("status") not in _parked,
                             not m.get("pin"), m.get("date", "")), reverse=False)
    pool.sort(key=lambda m: m.get("status") in _parked, reverse=True)
    print(f"Resume a thread (parked first, then newest, {len(pool)}{' incl. archived/done' if args.all else ' live'}):\n")
    for i, m in enumerate(pool, 1):
        pin = " 📌" if m["pin"] else ""
        stale = " · STALE" if _stale(m["date"]) else ""
        print(f"[{i}] {m['thread']} · {_age(m['date'])} · {m['status'].upper()}{pin}{stale}")
        if m["resume_hint"]:
            print(f"     ↪ {m['resume_hint']}")
        if m["unfinished"]:
            print(f"     ⧗ unfinished: {m['unfinished']}")
    print("\n/resume <thread|number>  ·  /realign <thread> (adjacent)  ·  list --all (archived/done)")
    return 0


def _pick(selector, include_all=False):
    """include_all=False → resolve against LIVE threads (matches the default menu)."""
    pool = threads(include_done=include_all, include_archived=include_all)
    kind, val = resolve(selector, pool)
    if kind == "ok":
        return val
    if kind == "none":
        hint = "" if include_all else " (add --all to include archived/done)"
        print(f"no thread matches: {selector!r} (try `list --rich`){hint}", file=sys.stderr)
    else:
        print(f"ambiguous: {selector!r} matches {[m['thread'] for m in val]} — be specific", file=sys.stderr)
    return None


def cmd_show(args) -> int:
    m = _pick(args.selector, include_all=args.all)
    if m is None:
        return 1
    print(f"# Thread: {m['thread']}  ({m['date']}, {_age(m['date'])}, {m['status']})\n")
    print(m["path"].read_text(encoding="utf-8"))
    return 0


def cmd_resume(args) -> int:
    m = _pick(args.selector, include_all=args.all)
    if m is None:
        return 1
    print(f"# ▶ Resolved → thread: {m['thread']}  ({m['date']}, {_age(m['date'])}, status={m['status']})")
    print(f"  (if that's not the thread you meant, run:  resume {m['thread']})")
    drift = []
    br = m["branch"]
    if br:
        cur = _git("rev-parse", "--abbrev-ref", "HEAD")
        exists = _git("rev-parse", "--verify", "--quiet", br) or _git("branch", "--list", br)
        if not exists:
            drift.append(f"branch '{br}' is MISSING (merged or deleted?) — verify before continuing")
        elif cur and cur != br:
            drift.append(f"you're on '{cur}', handoff was on '{br}' — consider: git checkout {br}")
            n = _git("rev-list", "--count", f"{br}..HEAD")
            if n.isdigit() and n != "0":
                drift.append(f"{n} commit(s) on HEAD not on '{br}'")
        else:
            drift.append(f"branch '{br}': current ✓")
            n = _git("rev-list", "--count", f"--since={m['date']}", "HEAD")
            if n.isdigit() and n != "0":
                drift.append(f"{n} commit(s) since {m['date']}")
    if _stale(m["date"]):
        drift.append(f"handoff is {_age(m['date'])} — treat its plan as LIKELY; reconcile with current reality")
    if drift:
        print("\n## Since this handoff")
        for d in drift:
            print(f"- {d}")
    print("\n---\n")
    print(m["path"].read_text(encoding="utf-8"))
    return 0


def _annotate(m: dict, updates: dict) -> None:
    raw = m["path"].read_text(encoding="utf-8")
    fm, body = parse_frontmatter(raw)
    base = {k: m[k] for k in FM_KEYS if m.get(k) not in (None, "")}
    base.update({k: v for k, v in fm.items() if k in FM_KEYS})
    base.update(updates)
    _write_with_fm(m["path"], base, body)
    rebuild()


def cmd_annotate(args) -> int:
    m = _pick(args.selector, include_all=True)
    if m is None:
        return 1
    updates = {}
    for k in ("thread", "status", "hint", "unfinished", "branch"):
        v = getattr(args, k, None)
        if v is not None:
            updates["resume_hint" if k == "hint" else k] = v
    if args.pin:
        updates["pin"] = "true"
    if "thread" in updates:
        updates["thread"] = slugify(updates["thread"])
    if "status" in updates and updates["status"].lower() not in STATUSES:
        print(f"ERROR: status must be one of {sorted(STATUSES)}", file=sys.stderr)
        return 1
    if not updates:
        print("nothing to annotate (pass --thread/--status/--hint/--unfinished/--branch/--pin)", file=sys.stderr)
        return 1

    # Thread rename: rewrite the thread field in ALL files of the old thread,
    # not just the latest — otherwise the menu silently splits into two rows.
    if "thread" in updates and updates["thread"] != m["thread"]:
        old, new, n = m["thread"], updates["thread"], 0
        for p in _files(STORE) + _files(ARCHIVE):
            pm = read_meta(p)
            if pm["thread"] != old:
                continue
            fm, body = parse_frontmatter(p.read_text(encoding="utf-8"))
            base = {k: pm[k] for k in FM_KEYS if pm.get(k) not in (None, "")}
            base.update({k: v for k, v in fm.items() if k in FM_KEYS})
            base["thread"] = new
            if p == m["path"]:
                base.update(updates)
            _write_with_fm(p, base, body)
            n += 1
        rebuild()
        print(f"renamed thread '{old}' → '{new}' in {n} file(s)")
        return 0

    _annotate(m, updates)
    print(f"annotated {m['thread']}: {', '.join(updates)}")
    return 0


def cmd_pin(args) -> int:
    m = _pick(args.thread, include_all=True)
    if m is None:
        return 1
    _annotate(m, {"pin": "true" if args.cmd == "pin" else "false"})
    print(f"{'pinned' if args.cmd == 'pin' else 'unpinned'}: {m['thread']}")
    return 0


def _move_thread(target: str, src_dir: Path, dst_dir: Path, verb: str) -> int:
    dst_dir.mkdir(parents=True, exist_ok=True)
    target = slugify(target)
    moved = 0
    for p in _files(src_dir):
        if read_meta(p)["thread"] != target:
            continue
        dest = dst_dir / p.name
        if dest.exists():
            dest = dst_dir / f"{p.stem}-dup-{int(p.stat().st_mtime)}.md"
        shutil.move(str(p), str(dest))
        moved += 1
    if not moved:
        print(f"no {'archived ' if verb == 'unarchive' else ''}handoffs for thread: {target!r}", file=sys.stderr)
        return 1
    rebuild()
    print(f"{verb}d {moved} file(s) for thread '{target}'")
    return 0


def cmd_archive(args) -> int:
    return _move_thread(args.thread, STORE, ARCHIVE, "archive")


def cmd_unarchive(args) -> int:
    return _move_thread(args.thread, ARCHIVE, STORE, "unarchive")


def cmd_latest(args) -> int:
    metas = all_metas()
    if not metas:
        print("(no handoffs yet)", file=sys.stderr)
        return 1
    print(metas[0]["path"].read_text(encoding="utf-8") if args.content
          else metas[0]["path"].relative_to(ROOT))
    return 0


def cmd_threads(args) -> int:
    for m in threads():
        print(f"{m['thread']:32} {m['status']:9} {m['date']} ({_age(m['date'])})")
    return 0


def cmd_path(args) -> int:
    print(STORE.relative_to(ROOT))
    return 0


def cmd_reindex(args) -> int:
    rebuild()
    print(f"reindexed: {len(all_metas())} handoff(s), {len(threads(include_done=True))} thread(s)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Durable handoff store + multi-thread resume")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("save")
    sp.add_argument("source", nargs="?")
    sp.add_argument("--from-temp", action="store_true")
    sp.add_argument("--thread"); sp.add_argument("--status"); sp.add_argument("--hint")
    sp.add_argument("--unfinished"); sp.add_argument("--branch")
    sp.add_argument("--slug"); sp.add_argument("--date")
    sp.add_argument("--pin", action="store_true"); sp.add_argument("--overwrite", action="store_true")
    sp.add_argument("--new-thread", action="store_true", dest="new_thread",
                    help="Force a genuinely new thread even when its name is a near-"
                         "duplicate of an existing one (default: auto-adopt the existing)")
    sp.set_defaults(fn=cmd_save)

    lp = sub.add_parser("list")
    lp.add_argument("--rich", action="store_true"); lp.add_argument("--all", action="store_true")
    lp.add_argument("--limit", type=int)
    lp.set_defaults(fn=cmd_list)

    shp = sub.add_parser("show")
    shp.add_argument("selector"); shp.add_argument("--all", action="store_true")
    shp.set_defaults(fn=cmd_show)

    rp = sub.add_parser("resume")
    rp.add_argument("selector"); rp.add_argument("--all", action="store_true")
    rp.set_defaults(fn=cmd_resume)

    anp = sub.add_parser("annotate")
    anp.add_argument("selector")
    anp.add_argument("--thread"); anp.add_argument("--status"); anp.add_argument("--hint")
    anp.add_argument("--unfinished"); anp.add_argument("--branch"); anp.add_argument("--pin", action="store_true")
    anp.set_defaults(fn=cmd_annotate)

    for name in ("pin", "unpin"):
        pp = sub.add_parser(name)
        pp.add_argument("thread")
        pp.set_defaults(fn=cmd_pin)

    arp = sub.add_parser("archive")
    arp.add_argument("thread")
    arp.set_defaults(fn=cmd_archive)

    uap = sub.add_parser("unarchive")
    uap.add_argument("thread")
    uap.set_defaults(fn=cmd_unarchive)

    ltp = sub.add_parser("latest")
    ltp.add_argument("--content", action="store_true")
    ltp.set_defaults(fn=cmd_latest)

    sub.add_parser("threads").set_defaults(fn=cmd_threads)
    sub.add_parser("path").set_defaults(fn=cmd_path)
    sub.add_parser("reindex").set_defaults(fn=cmd_reindex)

    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    raise SystemExit(main())
