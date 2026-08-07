#!/usr/bin/env python3
"""
Worktree Lane OS — lifecycle helper for parallel sessions (2026-08-06).

One writer per tree; lanes are automatic. The first session keeps the main
tree; every additional session (Claude Code or Codex) works in its own git
worktree "lane" with FULL harness power (hooks, .env, MCP, memory, spend
trackers — main-identical, proven by `parity`), then auto-merges back to main
when clean. Conflicts PARK the branch and surface one line — never silent loss.

STDLIB-ONLY by design: Codex lanes and the pre-bootstrap window have no venv,
so this must run under bare python3.

Commands:
  bootstrap [--if-needed] [--quiet]     provision a lane (symlinks + state + parity)
  parity                                prove full-power (also: doctor --parity)
  list [--json]                         active + parked lanes
  merge [--lane BRANCH] [--no-teardown] [--dry-run]
                                        seal -> gate -> merge -> Law-3 audit ->
                                        regen -> push -> teardown | PARK
  teardown [--lane BRANCH] [--force]    remove a merged/parked lane
  doctor [--fix] [--parity]             health table; --fix re-links/prunes

Doctrine: directives/merge-discipline.md (Law 3 mechanized in merge step 5).
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

FILE_ROOT = Path(__file__).resolve().parent.parent
LOCK_TTL_MIN = 45          # mirrors session_lock.py heartbeat TTL
FRESH_TRANSCRIPT_MIN = 10  # mirrors concurrent_session_alarm.py window

# Provisioned into every lane as symlinks -> main (single source of truth).
SHARED_LINKS = [
    ".venv", ".env", ".mcp.json",
    ".claude/settings.local.json",
    ".memory",
]
# Spend/budget state: shared so a lane can never zero-reset or double-spend.
# Only symlinked once untracked on main (Phase 3 migration); tracked -> SKIP.
SPEND_LINKS = [
    ".agent/gemini-api-usage.json", ".agent/perplexity-usage.json",
    ".agent/apify-usage.json", ".agent/notebooklm-usage.json",
    ".agent/revenue-outcomes.json", ".agent/fal-usage.json",
    ".agent/higgsfield-usage.json", ".agent/monid-usage.json",
    ".agent/cost-gate-state.json", ".agent/cost-gate-log.jsonl",
    ".agent/cost-gate-approvals.jsonl", ".agent/mcp-spend.jsonl",
]
# Committed generated artifacts: on merge conflict, keep ours + regenerate.
GENERATED_FILES = {"SLASH_COMMANDS.md", "SKILL_INDEX.md", "AGENT_INDEX.md"}
GENERATED_PREFIXES = (".claude/commands/",)
GENERATORS = ["generate_slash_commands.py", "sync_registries.py"]


# ── git plumbing ────────────────────────────────────────────────────
def _git(cwd, *args, timeout=60):
    try:
        r = subprocess.run(["git", "-C", str(cwd), *args],
                           capture_output=True, text=True, timeout=timeout)
        return r.returncode, r.stdout.strip(), r.stderr.strip()
    except Exception as e:  # pragma: no cover
        return 1, "", str(e)


def tree_root(cwd=None) -> Path:
    rc, out, _ = _git(cwd or Path.cwd(), "rev-parse", "--show-toplevel")
    return Path(out) if rc == 0 and out else FILE_ROOT


def main_root(cwd=None) -> Path:
    rc, out, _ = _git(cwd or Path.cwd(), "rev-parse",
                      "--path-format=absolute", "--git-common-dir")
    return Path(out).parent if rc == 0 and out else FILE_ROOT


def is_lane(cwd=None) -> bool:
    cwd = cwd or Path.cwd()
    rc1, gd, _ = _git(cwd, "rev-parse", "--path-format=absolute", "--git-dir")
    rc2, gcd, _ = _git(cwd, "rev-parse", "--path-format=absolute", "--git-common-dir")
    return rc1 == 0 and rc2 == 0 and gd != gcd


def current_branch(cwd) -> str:
    rc, out, _ = _git(cwd, "rev-parse", "--abbrev-ref", "HEAD")
    return out if rc == 0 else "?"


def active_lanes(main: Path) -> dict:
    """Ground truth: {branch: path} for every linked worktree (never the main
    checkout). Derived from `git worktree list --porcelain`, not the registry —
    a checked-out branch is definitionally an active lane even if the registry
    is stale or the lane was created by hand."""
    rc, out, _ = _git(main, "worktree", "list", "--porcelain")
    lanes, path, branch = {}, None, None
    if rc != 0:
        return lanes
    for line in out.splitlines() + [""]:
        if line.startswith("worktree "):
            path = Path(line[len("worktree "):])
        elif line.startswith("branch refs/heads/"):
            branch = line[len("branch refs/heads/"):]
        elif not line.strip():
            if path and branch and path.resolve() != main.resolve():
                lanes[branch] = path
            path, branch = None, None
    return lanes


# ── registry (metadata only; ground truth is git worktree list) ─────
def _registry_path(main: Path) -> Path:
    return main / ".agent" / "lanes.json"


def load_registry(main: Path) -> dict:
    try:
        return json.loads(_registry_path(main).read_text())
    except Exception:
        return {}


def save_registry(main: Path, reg: dict):
    p = _registry_path(main)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(reg, indent=2, sort_keys=True) + "\n")


# ── main-writer detection ───────────────────────────────────────────
def _flatten(p: Path) -> str:
    # Claude Code project-dir flattening: EVERY non-alphanumeric char -> "-"
    return re.sub(r"[^A-Za-z0-9]", "-", str(p))


def _lane_session_ids(main: Path) -> set:
    """Sessions registered to lanes are lane writers, not main writers — even
    though a session that auto-laned mid-session keeps its transcript in the
    MAIN tree's projects dir (transcript location is fixed at session start)."""
    ids = set()
    for meta in load_registry(main).values():
        sid = meta.get("session_id")
        if sid:
            ids.add(sid)
    env_sid = os.environ.get("CLAUDE_SESSION_ID")
    if env_sid:
        ids.add(env_sid)
    return ids


def fresh_main_writer(main: Path, exclude_ids=None) -> "str | None":
    exclude_ids = exclude_ids if exclude_ids is not None else _lane_session_ids(main)
    # (a) session lock heartbeat
    lock = main / ".agent" / "session.lock"
    if lock.exists():
        try:
            data = json.loads(lock.read_text())
            hb = float(data.get("heartbeat", 0))
            age_min = (time.time() - hb) / 60
            if age_min < LOCK_TTL_MIN:
                return f"session lock '{data.get('mission', '?')}' (heartbeat {age_min:.0f}m ago)"
        except Exception:
            pass
    # (b) fresh transcript in main's projects dir
    proj = Path.home() / ".claude" / "projects" / _flatten(main)
    if proj.is_dir():
        now = time.time()
        for t in proj.glob("*.jsonl"):
            if t.stem in exclude_ids:
                continue
            age_min = (now - t.stat().st_mtime) / 60
            if age_min < FRESH_TRANSCRIPT_MIN:
                return f"fresh session transcript {t.stem[:8]}… ({age_min:.0f}m ago)"
    return None


# ── hook-mode stdin (SessionStart / PostToolUse payload) ────────────
def _hook_payload() -> dict:
    if sys.stdin.isatty():
        return {}
    try:
        raw = sys.stdin.read()
        return json.loads(raw) if raw.strip() else {}
    except Exception:
        return {}


# ── bootstrap ───────────────────────────────────────────────────────
def _is_tracked(tree: Path, rel: str) -> bool:
    rc, _, _ = _git(tree, "ls-files", "--error-unmatch", rel, timeout=10)
    return rc == 0


def _link(main: Path, lane: Path, rel: str):
    """Returns 'linked' | 'present' | 'skip-tracked' | 'skip-no-source'."""
    src, dst = main / rel, lane / rel
    if not os.path.lexists(src):
        return "skip-no-source"
    if dst.is_symlink():
        if not dst.exists() or dst.resolve() != src.resolve():
            dst.unlink()
            dst.symlink_to(src)
        return "present"
    if os.path.lexists(dst):
        # Real file/dir in the lane. Tracked -> pre-migration, leave for git.
        # Untracked real -> leave too (never clobber); parity will flag it.
        return "skip-tracked" if _is_tracked(lane, rel) else "present"
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.symlink_to(src)
    return "linked"


def cmd_bootstrap(args) -> int:
    payload = _hook_payload()
    cwd = Path(payload.get("cwd") or os.environ.get("CLAUDE_PROJECT_DIR") or Path.cwd())
    if not cwd.is_dir():
        cwd = Path.cwd()
    if not is_lane(cwd):
        if args.if_needed:
            return 0
        print("main tree — nothing to bootstrap (lanes only)")
        return 0
    lane, main = tree_root(cwd), main_root(cwd)
    branch = current_branch(lane)

    counts = {"linked": 0, "present": 0, "skip-tracked": 0, "skip-no-source": 0}
    skipped = []
    for rel in SHARED_LINKS + SPEND_LINKS:
        res = _link(main, lane, rel)
        counts[res] += 1
        if res.startswith("skip"):
            skipped.append(f"{rel} ({res})")

    # Fresh per-lane state (isolation is correct here)
    agent = lane / ".agent"
    agent.mkdir(exist_ok=True)
    (agent / "sessions").mkdir(exist_ok=True)
    (agent / "handoffs").mkdir(exist_ok=True)
    ss = agent / "session-state.md"
    if not ss.exists():
        ss.write_text(f"# Session State — lane {branch}\n\n"
                      f"(fresh lane, bootstrapped {datetime.now():%Y-%m-%d %H:%M})\n")

    # Register (metadata; ground truth stays `git worktree list`)
    reg = load_registry(main)
    entry = reg.get(branch, {})
    entry.update({
        "path": str(lane),
        "harness": "codex" if branch.startswith("codex/") else "claude",
        "created": entry.get("created") or datetime.now().isoformat(timespec="seconds"),
        "status": "active",
        "last_seen": datetime.now().isoformat(timespec="seconds"),
    })
    sid = payload.get("session_id") or os.environ.get("CLAUDE_SESSION_ID")
    if sid:
        entry["session_id"] = sid
    reg[branch] = entry
    save_registry(main, reg)

    ok, deficiencies = run_parity(lane, main, record=True)
    if ok:
        print(f"LANE READY: {branch} at {lane} — FULL POWER "
              f"({counts['linked'] + counts['present']} links, "
              f"{counts['skip-tracked']} awaiting Phase-3 migration)"
              + ("" if not args.quiet else ""))
    else:
        print(f"LANE READY (degraded): {branch} at {lane}")
        for d in deficiencies:
            print(f"  ⚠ {d}")
        print(f"  fix: python3 execution/worktree_lane.py doctor --fix")
    if skipped and not args.quiet:
        for s_ in skipped:
            if "no-source" in s_:
                print(f"  note: {s_}")
    return 0


# ── parity (the full-power guarantee) ───────────────────────────────
def run_parity(lane: Path, main: Path, record=False):
    """Prove the lane has main-identical functionality. Returns (ok, [deficiencies]).
    Nudge, never block: informational even when degraded."""
    d = []

    # 1. every hook command resolves + its script parses under the lane python
    settings = lane / ".claude" / "settings.json"
    hooks_total = hooks_ok = 0
    lane_py = lane / ".venv" / "bin" / "python3"
    if not lane_py.exists():
        lane_py = Path(sys.executable)
    try:
        conf = json.loads(settings.read_text())
        scripts = set()
        def walk(node):
            if isinstance(node, dict):
                cmd = node.get("command")
                if isinstance(cmd, str):
                    for m in re.findall(r'\$CLAUDE_PROJECT_DIR/([^"\s]+\.(?:py|sh))', cmd):
                        scripts.add(m)
                for v in node.values():
                    walk(v)
            elif isinstance(node, list):
                for v in node:
                    walk(v)
        walk(conf.get("hooks", {}))
        hooks_total = len(scripts)
        missing, broken = [], []
        for rel in sorted(scripts):
            p = lane / rel
            if not p.exists():
                missing.append(rel)
                continue
            if rel.endswith(".py"):
                r = subprocess.run([str(lane_py), "-c",
                                    f"import ast; ast.parse(open({str(p)!r}).read())"],
                                   capture_output=True, timeout=20)
                if r.returncode != 0:
                    broken.append(rel)
                    continue
            hooks_ok += 1
        if missing:
            d.append(f"hook scripts missing in lane: {', '.join(missing[:3])}")
        if broken:
            d.append(f"hook scripts fail to parse: {', '.join(broken[:3])}")
    except Exception as e:
        d.append(f"settings.json unreadable: {e}")

    # deps reachable under lane python (the venv symlink test that matters)
    r = subprocess.run([str(lane_py), "-c", "import dotenv, requests"],
                       capture_output=True, timeout=20)
    if r.returncode != 0:
        d.append(".venv deps unreachable under lane python (dotenv/requests import failed)")

    # 2. .env parity
    env_l, env_m = lane / ".env", main / ".env"
    if not env_l.exists():
        d.append(".env absent — API clients silently unauthenticated")
    elif env_m.exists():
        def keys(p):
            try:
                return {l.split("=")[0].strip() for l in p.read_text().splitlines()
                        if "=" in l and not l.lstrip().startswith("#")}
            except Exception:
                return set()
        miss = keys(env_m) - keys(env_l)
        if miss:
            d.append(f".env missing {len(miss)} key(s) vs main: {', '.join(sorted(miss)[:3])}")

    # 3. mcp + local settings resolve
    for rel in (".mcp.json", ".claude/settings.local.json"):
        p = lane / rel
        if (main / rel).exists() and (not p.exists()):
            d.append(f"{rel} absent (symlink broken or never linked)")

    # 4. memory reachable (read-only canary against sovereign.db)
    db = lane / ".memory" / "sovereign.db"
    if (main / ".memory" / "sovereign.db").exists():
        if not db.exists():
            d.append(".memory/sovereign.db unreachable — memory_facade returns empty")
        else:
            try:
                import sqlite3
                con = sqlite3.connect(f"file:{db}?mode=ro", uri=True, timeout=5)
                n = con.execute("SELECT count(*) FROM sqlite_master").fetchone()[0]
                con.close()
                if n == 0:
                    d.append("sovereign.db opens but is empty")
            except Exception as e:
                d.append(f"sovereign.db read failed: {e}")

    # 5. in-repo surface counts (catches a stale branch base)
    for rel, label in ((".claude/commands", "slash commands"),
                       (".agent/workflows", "workflows"), ("skills", "skills")):
        lp, mp = lane / rel, main / rel
        if lp.is_dir() and mp.is_dir():
            ln, mn = len(list(lp.iterdir())), len(list(mp.iterdir()))
            if mn and abs(ln - mn) / mn > 0.02:
                d.append(f"{label} count drift vs main ({ln} vs {mn}) — stale base? "
                         f"consider rebasing the lane")

    # 6. spend symlinks point at main
    for rel in SPEND_LINKS:
        lp, mp = lane / rel, main / rel
        if mp.exists() and not _is_tracked(main, rel):
            if not (lp.is_symlink() and lp.resolve() == mp.resolve()):
                d.append(f"{rel} not shared with main — spend could fork")
                break  # one line is enough

    # 7. fresh hook-failure beacons for this tree
    beacon = main / ".agent" / "hook-failures.log"
    if beacon.exists():
        try:
            cutoff = time.time() - 24 * 3600
            fresh = [l for l in beacon.read_text().splitlines()[-200:]
                     if str(lane) in l]
            if fresh and beacon.stat().st_mtime > cutoff:
                d.append(f"hook-failures.log has entries for this tree "
                         f"(latest: {fresh[-1][:90]})")
        except Exception:
            pass

    ok = not d
    if record:
        reg = load_registry(main)
        b = current_branch(lane)
        if b in reg:
            reg[b]["health"] = "full-power" if ok else deficiency_summary(d)
            reg[b]["parity_at"] = datetime.now().isoformat(timespec="seconds")
            save_registry(main, reg)
    return ok, d


def deficiency_summary(d):
    return f"degraded ({len(d)}): " + "; ".join(x[:60] for x in d[:3])


def cmd_parity(args) -> int:
    cwd = Path.cwd()
    if not is_lane(cwd):
        print("main tree — parity is trivially full (this IS the reference)")
        return 0
    lane, main = tree_root(cwd), main_root(cwd)
    ok, d = run_parity(lane, main, record=True)
    if ok:
        print(f"FULL POWER: lane {current_branch(lane)} is main-identical "
              f"(hooks ✓ env ✓ mcp ✓ memory ✓ indexes ✓ spend ✓)")
    else:
        print(f"DEGRADED: lane {current_branch(lane)} — {len(d)} deficiency(ies):")
        for x in d:
            print(f"  ⚠ {x}")
        print("  fix: python3 execution/worktree_lane.py doctor --fix")
    return 0


# ── list ────────────────────────────────────────────────────────────
def cmd_list(args) -> int:
    main = main_root()
    lanes = active_lanes(main)
    reg = load_registry(main)
    rows = []
    for branch, path in sorted(lanes.items()):
        meta = reg.get(branch, {})
        rows.append({"branch": branch, "path": str(path),
                     "harness": meta.get("harness", "?"),
                     "status": meta.get("status", "unregistered"),
                     "health": meta.get("health", "?")})
    for branch, meta in sorted(reg.items()):
        if branch not in lanes and meta.get("status") == "parked":
            rows.append({"branch": branch, "path": meta.get("path", "?"),
                         "harness": meta.get("harness", "?"),
                         "status": f"parked — {meta.get('reason', '?')}",
                         "health": "-"})
    if args.json:
        print(json.dumps(rows, indent=2))
        return 0
    if not rows:
        print("no lanes — main tree is the only checkout")
        return 0
    for r in rows:
        print(f"{r['branch']:44s} {r['status']:28s} {r['health']:20s} {r['path']}")
    return 0


# ── merge ───────────────────────────────────────────────────────────
def _is_generated(path: str) -> bool:
    return path in GENERATED_FILES or path.startswith(GENERATED_PREFIXES)


def _park(main, lane, branch, reason) -> int:
    _git(lane, "push", "-u", "origin", branch, timeout=90)  # best effort
    reg = load_registry(main)
    entry = reg.get(branch, {})
    entry.update({"path": str(lane), "status": "parked", "reason": reason,
                  "parked_at": datetime.now().isoformat(timespec="seconds")})
    reg[branch] = entry
    save_registry(main, reg)
    print(f"LANE PARKED: {branch} — {reason}. Resolve later: "
          f"python3 execution/worktree_lane.py merge --lane {branch}")
    return 0  # a park is a surfaced outcome, not an error


def cmd_merge(args) -> int:
    cwd = Path.cwd()
    main = main_root(cwd)
    if args.lane:
        lanes = active_lanes(main)
        if args.lane not in lanes:
            print(f"ERROR: no active worktree for branch {args.lane!r} "
                  f"(active: {', '.join(lanes) or 'none'})", file=sys.stderr)
            return 1
        lane = lanes[args.lane]
    elif is_lane(cwd):
        lane = tree_root(cwd)
    else:
        print("ERROR: run from inside a lane or pass --lane <branch>", file=sys.stderr)
        return 1
    branch = current_branch(lane)

    if args.dry_run:
        print(f"[dry-run] would merge lane {branch} ({lane}) -> main ({main})")
        return 0

    # 1 SEAL — commit everything in the lane (single writer by construction)
    rc, out, _ = _git(lane, "status", "--porcelain")
    if out.strip():
        _git(lane, "add", "-A")
        _git(lane, "commit", "-m", f"chore(lane): seal {branch}")
    # 1b DROP files tracked on the branch but gitignored on main (Phase-3
    # migration class). Removing them from the branch tip pre-merge prevents
    # both modify/delete conflicts AND git refusing to overwrite main's live
    # untracked state files.
    rc, files, _ = _git(lane, "ls-files")
    to_drop = []
    if files:
        proc = subprocess.run(["git", "-C", str(main), "check-ignore", "--stdin"],
                              input=files, capture_output=True, text=True, timeout=30)
        candidates = [f for f in proc.stdout.splitlines() if f.strip()]
        if candidates:
            # NEVER drop a file main still tracks — the merge would read the
            # drop as a deletion and silently remove it from main (a gitignore
            # pattern can shadow a tracked file; ignore rules don't untrack).
            rc, main_tracked, _ = _git(main, "ls-files", "--", *candidates)
            main_set = set(main_tracked.splitlines())
            to_drop = [f for f in candidates if f not in main_set]
    if to_drop:
        _git(lane, "rm", "--cached", "-q", "--", *to_drop)
        _git(lane, "commit", "-m",
             "chore(lane): drop per-tree state files from index (gitignored on main)")

    # anything to merge at all?
    rc, count, _ = _git(main, "rev-list", "--count", f"main..{branch}")
    if rc == 0 and count == "0":
        print(f"LANE MERGED: {branch} -> main (0 commits — nothing to merge)")
        if not args.no_teardown:
            _teardown_lane(main, lane, branch)
        return 0

    # 2 GATE
    rc, out, _ = _git(main, "status", "--porcelain")
    if out.strip():
        return _park(main, lane, branch, "main tree dirty — first driver owns it")
    writer = fresh_main_writer(main)
    if writer:
        return _park(main, lane, branch, f"main has a fresh writer: {writer}")
    lockfile = (main / ".agent" / "lane-merge.lock")
    lockfile.parent.mkdir(exist_ok=True)
    lock_fd = os.open(lockfile, os.O_CREAT | os.O_RDWR)
    try:
        import fcntl
        fcntl.flock(lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        os.close(lock_fd)
        return _park(main, lane, branch, "another lane is merging right now")

    try:
        # 3 AUDITSET (Law-3 evidence, computed BEFORE the merge)
        rc, base, _ = _git(main, "merge-base", "main", branch)
        rc, added_raw, _ = _git(main, "diff", "--diff-filter=A", "--name-only", base, branch)
        added = [f for f in added_raw.splitlines() if f and f not in to_drop]
        rc, changed_raw, _ = _git(main, "diff", "--name-only", base, branch)
        gen_touched = [f for f in changed_raw.splitlines() if _is_generated(f)]

        # 4 MERGE
        rc, out, err = _git(main, "merge", "--no-ff", "--no-edit", branch, timeout=300)
        if rc != 0:
            rc2, merging, _ = _git(main, "rev-parse", "-q", "--verify", "MERGE_HEAD")
            if rc2 != 0:  # merge never started (e.g. untracked-overwrite refusal)
                return _park(main, lane, branch, f"merge refused: {(err or out)[:120]}")
            rc2, u_raw, _ = _git(main, "diff", "--name-only", "--diff-filter=U")
            unresolved = []
            for u in u_raw.splitlines():
                if not u:
                    continue
                if _is_generated(u):
                    _git(main, "checkout", "--ours", "--", u)
                    _git(main, "add", "--", u)
                    if u not in gen_touched:
                        gen_touched.append(u)
                elif u.endswith(".jsonl"):
                    rcA, ours, _ = _git(main, "show", f":2:{u}")
                    rcB, theirs, _ = _git(main, "show", f":3:{u}")
                    if rcA == 0 and rcB == 0:
                        seen = set(ours.splitlines())
                        merged = ours.splitlines() + \
                            [l for l in theirs.splitlines() if l not in seen]
                        (main / u).write_text("\n".join(merged) + "\n")
                        _git(main, "add", "--", u)
                    else:
                        unresolved.append(u)
                else:
                    unresolved.append(u)
            if unresolved:
                _git(main, "merge", "--abort")
                return _park(main, lane, branch,
                             f"conflict in {', '.join(unresolved[:3])}"
                             + (f" +{len(unresolved)-3} more" if len(unresolved) > 3 else ""))
            _git(main, "commit", "--no-edit")

        # 5 LAW-3 AUDIT — every branch-added file must exist on merged main
        dropped = [f for f in added
                   if _git(main, "cat-file", "-e", f"HEAD:{f}")[0] != 0]
        if dropped:
            _git(main, "reset", "--merge", "ORIG_HEAD")
            return _park(main, lane, branch,
                         f"Law-3 audit failed: merge dropped {dropped[0]}"
                         + (f" +{len(dropped)-1} more" if len(dropped) > 1 else ""))

        # 6 REGEN — generated artifacts are rebuilt, never hand-merged
        if gen_touched:
            py = main / ".venv" / "bin" / "python3"
            py = str(py) if py.exists() else sys.executable
            for g in GENERATORS:
                subprocess.run([py, str(main / "execution" / g)],
                               capture_output=True, timeout=600, cwd=str(main))
            rc, out, _ = _git(main, "status", "--porcelain")
            if out.strip():
                _git(main, "add", "--", *GENERATED_FILES, ".claude/commands")
                _git(main, "commit", "-m",
                     "chore(lane): regenerate indexes post-merge")

        # 7 PUSH (post-commit hook also pushes; explicit push is idempotent)
        rc, _, err = _git(main, "push", "origin", "main", timeout=120)
        push_note = "" if rc == 0 else " (push pending — will drain via post-commit hook)"

        # 8 TEARDOWN
        rc, n_commits, _ = _git(main, "rev-list", "--count", f"{base}..{branch}")
        n_files = len(changed_raw.splitlines())
        if not args.no_teardown:
            _teardown_lane(main, lane, branch)

        # 9
        print(f"LANE MERGED: {branch} -> main ({n_commits} commits, {n_files} files){push_note}")
        return 0
    finally:
        try:
            import fcntl
            fcntl.flock(lock_fd, fcntl.LOCK_UN)
        except Exception:
            pass
        os.close(lock_fd)


def _teardown_lane(main: Path, lane: Path, branch: str):
    """Post-merge teardown. Sealed lane -> only gitignored leftovers remain
    (symlinks into main, per-lane session state, .tmp scratch) — all safe to
    drop, so --force is safe here and ONLY here."""
    for rel in SHARED_LINKS + SPEND_LINKS:
        p = lane / rel
        if p.is_symlink():
            p.unlink(missing_ok=True)
    _git(main, "worktree", "remove", "--force", str(lane))
    _git(main, "branch", "-d", branch)  # just merged -> -d succeeds; never -D
    reg = load_registry(main)
    reg.pop(branch, None)
    save_registry(main, reg)


def cmd_teardown(args) -> int:
    main = main_root()
    lanes = active_lanes(main)
    branch = args.lane or (current_branch(tree_root()) if is_lane() else None)
    if not branch:
        print("ERROR: pass --lane <branch> (or run from inside a lane)", file=sys.stderr)
        return 1
    lane = lanes.get(branch)
    reg = load_registry(main)
    merged = _git(main, "merge-base", "--is-ancestor", branch, "main")[0] == 0
    pushed = _git(main, "rev-parse", "-q", "--verify", f"origin/{branch}")[0] == 0
    if not (merged or (reg.get(branch, {}).get("status") == "parked" and pushed) or args.force):
        print(f"REFUSED: {branch} is neither merged into main nor parked-and-pushed. "
              f"Merge it (worktree_lane.py merge --lane {branch}) or pass --force "
              f"to discard.", file=sys.stderr)
        return 1
    if lane and lane.exists():
        for rel in SHARED_LINKS + SPEND_LINKS:
            p = lane / rel
            if p.is_symlink():
                p.unlink(missing_ok=True)
        _git(main, "worktree", "remove", "--force", str(lane))
    if merged:
        _git(main, "branch", "-d", branch)
    elif args.force:
        # branch -D is guard-blocked by policy; plumbing is the sanctioned path
        _git(main, "update-ref", "-d", f"refs/heads/{branch}")
    reg.pop(branch, None)
    save_registry(main, reg)
    print(f"LANE TORN DOWN: {branch}")
    return 0


# ── doctor ──────────────────────────────────────────────────────────
def cmd_doctor(args) -> int:
    main = main_root()
    lanes = active_lanes(main)
    reg = load_registry(main)
    now = time.time()
    print(f"main: {main}")
    print(f"{'BRANCH':44s} {'STATE':12s} {'AGE':6s} NOTES")
    issues = 0
    for branch, path in sorted(lanes.items()):
        meta = reg.get(branch, {})
        notes = []
        state = "active" if branch in reg else "LEGACY"
        if state == "LEGACY":
            notes.append("unregistered — merge or park by hand once, "
                         "or `bootstrap` inside it to adopt")
        broken = []
        for rel in SHARED_LINKS + SPEND_LINKS:
            p = path / rel
            src = main / rel
            if not os.path.lexists(src) or _is_tracked(path, rel):
                continue  # nothing to provide, or pre-migration tracked copy
            if p.is_symlink() and not p.exists():
                broken.append(rel)          # dangling
            elif not os.path.lexists(p):
                broken.append(rel)          # deleted entirely
        if broken:
            issues += 1
            notes.append(f"broken/missing links: {', '.join(broken[:3])}")
            if args.fix:
                for rel in broken:
                    p = path / rel
                    if p.is_symlink():
                        p.unlink()
                    _link(main, path, rel)
                notes.append("(re-linked)")
        try:
            age_d = (now - path.stat().st_mtime) / 86400
        except OSError:
            age_d = -1
            issues += 1
            notes.append("path missing — `git worktree prune`")
            if args.fix:
                _git(main, "worktree", "prune")
                reg.pop(branch, None)
                notes.append("(pruned)")
        if age_d > 7:
            notes.append(f"stale ({age_d:.0f}d quiet) — merge or teardown")
        if args.parity and path.exists():
            ok, d = run_parity(path, main, record=True)
            notes.append("full-power ✓" if ok else deficiency_summary(d))
        print(f"{branch:44s} {state:12s} {age_d:5.1f}d {'; '.join(notes) or 'ok'}")
    for branch, meta in sorted(reg.items()):
        if branch in lanes:
            continue
        if meta.get("status") == "parked":
            print(f"{branch:44s} {'parked':12s} {'':6s} {meta.get('reason', '?')} — "
                  f"merge --lane {branch}")
        else:
            issues += 1
            if args.fix:
                reg.pop(branch, None)
                print(f"{branch:44s} {'pruned':12s} {'':6s} registry entry had no worktree")
            else:
                print(f"{branch:44s} {'GHOST':12s} {'':6s} registry entry, no worktree "
                      f"(--fix prunes)")
    if args.fix:
        save_registry(main, reg)
    if not lanes and not reg:
        print("(no lanes)")
    return 0


# ── entry ───────────────────────────────────────────────────────────
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    sub = ap.add_subparsers(dest="cmd", required=True)

    b = sub.add_parser("bootstrap", help="provision this lane (symlinks + state + parity)")
    b.add_argument("--if-needed", action="store_true", dest="if_needed",
                   help="exit 0 silently when not in a lane / already provisioned")
    b.add_argument("--quiet", action="store_true")
    b.set_defaults(fn=cmd_bootstrap)

    p = sub.add_parser("parity", help="prove this lane has full harness power")
    p.set_defaults(fn=cmd_parity)

    l = sub.add_parser("list")
    l.add_argument("--json", action="store_true")
    l.set_defaults(fn=cmd_list)

    m = sub.add_parser("merge", help="seal + merge this lane back to main (auto-merge-when-clean)")
    m.add_argument("--lane", help="branch name (default: the lane you're in)")
    m.add_argument("--no-teardown", action="store_true", dest="no_teardown")
    m.add_argument("--dry-run", action="store_true", dest="dry_run")
    m.set_defaults(fn=cmd_merge)

    t = sub.add_parser("teardown")
    t.add_argument("--lane")
    t.add_argument("--force", action="store_true",
                   help="discard an unmerged lane (uses update-ref plumbing)")
    t.set_defaults(fn=cmd_teardown)

    d = sub.add_parser("doctor")
    d.add_argument("--fix", action="store_true")
    d.add_argument("--parity", action="store_true")
    d.set_defaults(fn=cmd_doctor)

    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
