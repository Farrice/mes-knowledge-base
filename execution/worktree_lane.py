#!/usr/bin/env python3
"""
Worktree Lane OS — lifecycle helper for parallel sessions (2026-08-06).

Main is integration-only; every write-capable Claude Code or Codex session
works in its own git worktree "lane" with FULL harness power (hooks, .env, MCP,
memory, spend trackers — main-identical, proven by `parity`), then auto-merges
back to clean main. Read-only inspection may stay on main. Conflicts PARK the
branch and surface one line — never silent loss.

STDLIB-ONLY by design: Codex lanes and the pre-bootstrap window have no venv,
so this must run under bare python3.

Commands:
  bootstrap [--if-needed] [--quiet]     provision a lane (symlinks + state + parity)
  parity                                prove full-power (also: doctor --parity)
  list [--json]                         active + parked lanes
  merge [--lane BRANCH] [--no-teardown] [--push] [--no-push] [--dry-run]
                                        seal -> gate -> merge -> Law-3 audit ->
                                        regen -> local by default; explicit push
                                        -> teardown | PARK
  preserve [--slug S] [--dry-run] [--push]
                                        move human work stranded on main into
                                        its own lane; main becomes clean
  teardown [--lane BRANCH] [--force]    remove a merged/parked lane
  doctor [--fix] [--parity]             health table; --fix re-links/prunes

Doctrine: directives/merge-discipline.md (Law 3 mechanized in merge step 5).
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

FILE_ROOT = Path(__file__).resolve().parent.parent
LOCK_TTL_MIN = 45          # mirrors session_lock.py heartbeat TTL

# Provisioned into every lane as symlinks -> main (single source of truth).
SHARED_LINKS = [
    ".venv", ".env", ".mcp.json",
    ".claude/settings.local.json",
    ".memory",
    ".agent/cos",
]
# Workspace-local context starts main-identical but must remain isolated after
# bootstrap. Copy it once instead of symlinking it back to the main workspace.
SNAPSHOT_DIRS = [
    ".agent/intent-memory",
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
GENERATED_FILES = {"SLASH_COMMANDS.md", "SKILL_INDEX.md", "AGENT_INDEX.md",
                   ".agent/handoffs/index.md", ".agent/handoffs/LATEST.md"}
GENERATED_PREFIXES = (".claude/commands/", "knowledge/compiled/")
# Append-style ledger docs: both sides add entries; line-union preserves every
# entry from both (same semantics as the .jsonl rule; dedupe per Law 2).
UNION_DOCS = {"knowledge/log.md", "PROJECTS.md", "docs/solutions/index.md",
              "guides/INDEX.md", "evolution_store/failure-registry.md",
              "knowledge/index.md"}
# (script, args) pairs, run against main after a merge that touched GENERATED
GENERATORS = [("generate_slash_commands.py", []),
              ("sync_registries.py", []),
              ("handoff_store.py", ["reindex"])]


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


def fresh_main_writer(main: Path, exclude_ids=None, own_lock_token=None) -> "str | None":
    """Return actual evidence of a live main writer.

    Fresh transcripts are deliberately not write evidence. Since main became
    integration-only, read-only sessions correctly remain there, and background
    artifact-monitor events keep their transcripts fresh. A main writer must
    hold the session lock; tracked changes and the merge mutex are checked
    separately by ``cmd_merge``.
    """
    own_lock_token = own_lock_token or os.environ.get("SESSION_LOCK_TOKEN")
    # Session lock heartbeat (our own lock doesn't make us a foreign writer).
    lock = main / ".agent" / "session.lock"
    if lock.exists():
        try:
            data = json.loads(lock.read_text())
            hb = float(data.get("heartbeat", 0))
            age_min = (time.time() - hb) / 60
            if age_min < LOCK_TTL_MIN and data.get("token") != own_lock_token:
                return f"session lock '{data.get('mission', '?')}' (heartbeat {age_min:.0f}m ago)"
        except Exception:
            pass
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

    snapshots = 0
    for rel in SNAPSHOT_DIRS:
        src, dst = main / rel, lane / rel
        if src.is_dir() and not os.path.lexists(dst):
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(src, dst)
            snapshots += 1

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
              f"{snapshots} context snapshots, "
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

    # Codex has a separate hook surface. A lane is not full-power merely
    # because Claude hooks parse; prove the Codex config, runner, and desktop
    # trust state resolve through the canonical main hook file.
    codex_hooks = lane / ".codex" / "hooks.json"
    try:
        codex_conf = json.loads(codex_hooks.read_text())
        codex_commands = [
            str(hook.get("command") or "")
            for groups in codex_conf.get("hooks", {}).values()
            for group in groups
            for hook in group.get("hooks", [])
            if hook.get("command")
        ]
        if len(codex_commands) != 9:
            d.append(f"Codex hooks.json expected 9 commands, found {len(codex_commands)}")
        if not codex_commands or not all("codex_hook_runner.py" in command for command in codex_commands):
            d.append("Codex hook commands do not all use codex_hook_runner.py")
        for command in codex_commands:
            match = re.search(r'"([^"]*codex_hook_runner\.py)"', command)
            if match and not Path(match.group(1)).exists():
                d.append(f"Codex hook runner missing: {match.group(1)}")
                break
        desktop_config = Path.home() / ".codex" / "config.toml"
        config_text = desktop_config.read_text() if desktop_config.exists() else ""
        trusted_hooks = main / ".codex" / "hooks.json"
        required_states = (
            "pre_tool_use:0:0",
            "pre_tool_use:0:2",
            "post_tool_use:0:0",
            "user_prompt_submit:0:0",
            "user_prompt_submit:0:1",
            "user_prompt_submit:0:2",
            "stop:0:0",
        )
        missing_states = []
        for suffix in required_states:
            header = f'[hooks.state."{trusted_hooks}:{suffix}"]'
            marker = config_text.find(header)
            if marker == -1:
                missing_states.append(suffix)
                continue
            next_header = config_text.find("\n[", marker + 1)
            block = config_text[marker:] if next_header == -1 else config_text[marker:next_header]
            block_lower = block.lower()
            if "trusted_hash" not in block_lower or "enabled = false" in block_lower:
                missing_states.append(suffix)
        if missing_states:
            d.append(f"Codex desktop hook trust missing/explicitly-disabled states: {', '.join(missing_states[:3])}")
    except Exception as e:
        d.append(f"Codex hooks.json unreadable: {e}")

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

    if (main / ".agent" / "cos" / "goals.json").exists() and not (
        lane / ".agent" / "cos" / "goals.json"
    ).exists():
        d.append(".agent/cos/goals.json absent — current goals and mission context are unavailable")

    if (main / ".agent" / "intent-memory" / "current.json").exists() and not (
        lane / ".agent" / "intent-memory" / "current.json"
    ).exists():
        d.append(".agent/intent-memory/current.json absent — active intent context is unavailable")

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


STAMP_LINE = re.compile(
    r"^\s*(\|\s*\*\*(Last Activated|Activation Count|30-Day Review|Last Updated|"
    r"Last Run|Last Synced)|\*Last activated)")


def _theirs_only_stamps(main: Path, path: str) -> bool:
    """During a conflict: True when the branch side's ONLY changes vs the merge
    base are activation-stamp rows (chain_runner bumps counters inside tracked
    directive files, per tree — divergent-but-worthless). Taking ours keeps
    main's newer stamps and loses nothing."""
    rc1, base, _ = _git(main, "show", f":1:{path}")
    rc3, theirs, _ = _git(main, "show", f":3:{path}")
    if rc1 != 0 or rc3 != 0:
        return False
    import difflib
    changed = [l[1:] for l in difflib.unified_diff(base.splitlines(), theirs.splitlines(), n=0)
               if (l.startswith("+") or l.startswith("-"))
               and not l.startswith(("+++", "---"))]
    return bool(changed) and all(not l.strip() or STAMP_LINE.match(l) for l in changed)


def _theirs_is_stale(main: Path, path: str, depth: int = 60) -> bool:
    """During a conflict: True when THEIR version of `path` (stage 3) matches
    some historical version of the file on main — the branch side is a stale
    snapshot and taking ours provably loses nothing."""
    rc, unmerged, _ = _git(main, "ls-files", "-u", "--", path)
    th = None
    for line in unmerged.splitlines():
        parts = line.split()          # mode sha stage\tpath
        if len(parts) >= 3 and parts[2] == "3":
            th = parts[1]
    if not th:
        return False
    rc, revs, _ = _git(main, "rev-list", f"-{depth}", "HEAD", "--", path)
    for rev in revs.split():
        rc2, h, _ = _git(main, "rev-parse", f"{rev}:{path}")
        if rc2 == 0 and h == th:
            return True
    return False


def _park(main, lane, branch, reason, push=True) -> int:
    if push:
        _git(lane, "push", "-u", "origin", branch, timeout=90)  # best effort
    reg = load_registry(main)
    entry = reg.get(branch, {})
    entry.update({"path": str(lane), "status": "parked", "reason": reason,
                  "parked_at": datetime.now().isoformat(timespec="seconds")})
    entry.pop("merge_in_flight", None)
    reg[branch] = entry
    save_registry(main, reg)
    print(f"LANE PARKED: {branch} — {reason}. Resolve later: "
          f"python3 execution/worktree_lane.py merge --lane {branch}")
    return 0  # a park is a surfaced outcome, not an error


def _main_mid_merge(main: Path) -> bool:
    """True when the integration tree has an unconcluded merge (MERGE_HEAD)."""
    return _git(main, "rev-parse", "-q", "--verify", "MERGE_HEAD")[0] == 0


def _abort_merge(main: Path) -> "str | None":
    """Conclude a failed merge on main so it is NEVER left mid-merge.

    Scar (2026-09-02): main sat with MERGE_HEAD + 40 UU files for hours; every
    other lane parked on it. The old code ran `merge --abort` and discarded
    the return code. Now: abort -> fallback `reset --merge` -> verify. Returns
    None on success, else the error text (caller surfaces it LOUDLY).
    """
    rc, _, err = _git(main, "merge", "--abort")
    if rc != 0 or _main_mid_merge(main):
        rc2, _, err2 = _git(main, "reset", "--merge")
        if rc2 != 0 or _main_mid_merge(main):
            return (err or err2 or "MERGE_HEAD still present")[:200]
    return None


def _set_in_flight(main: Path, branch: str, lane: Path, on: bool):
    reg = load_registry(main)
    entry = reg.get(branch, {})
    if on:
        entry.update({"path": str(lane), "merge_in_flight":
                      datetime.now().isoformat(timespec="seconds")})
    else:
        entry.pop("merge_in_flight", None)
    reg[branch] = entry
    save_registry(main, reg)


def cmd_merge(args) -> int:
    if args.no_push:
        # This repo's post-commit and post-merge hooks auto-push. Suppress them
        # inside this one-shot helper process so local-only means local-only.
        os.environ["GIT_CONFIG_COUNT"] = "1"
        os.environ["GIT_CONFIG_KEY_0"] = "core.hooksPath"
        os.environ["GIT_CONFIG_VALUE_0"] = "/dev/null"
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

    # 2 GATE — tracked modifications only: untracked files (telemetry, scratch)
    # can't be swept into a merge commit; a path collision with a branch file
    # surfaces as "merge refused" below and parks anyway.
    rc, out, _ = _git(main, "status", "--porcelain")
    tracked_dirty = [l for l in out.splitlines() if l.strip() and not l.startswith("??")]
    if tracked_dirty:
        return _park(main, lane, branch,
                     f"main integration tree dirty ({len(tracked_dirty)} tracked change(s)) — "
                     f"reconcile main before merging lanes", push=not args.no_push)
    exclude = _lane_session_ids(main) | set(getattr(args, "exclude_session", None) or [])
    writer = fresh_main_writer(main, exclude_ids=exclude,
                               own_lock_token=getattr(args, "lock_token", None))
    if writer:
        return _park(main, lane, branch, f"main has a fresh writer: {writer}",
                     push=not args.no_push)
    lockfile = (main / ".agent" / "lane-merge.lock")
    lockfile.parent.mkdir(exist_ok=True)
    lock_fd = os.open(lockfile, os.O_CREAT | os.O_RDWR)
    try:
        import fcntl
        fcntl.flock(lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        os.close(lock_fd)
        return _park(main, lane, branch, "another lane is merging right now",
                     push=not args.no_push)

    try:
        # 3 AUDITSET (Law-3 evidence, computed BEFORE the merge)
        rc, base, _ = _git(main, "merge-base", "main", branch)
        rc, added_raw, _ = _git(main, "diff", "--diff-filter=A", "--name-only", base, branch)
        added = [f for f in added_raw.splitlines() if f and f not in to_drop]
        rc, changed_raw, _ = _git(main, "diff", "--name-only", base, branch)
        gen_touched = [f for f in changed_raw.splitlines() if _is_generated(f)]

        # 3b PRE-FLIGHT — never stack a merge on a merge. A foreign actor's
        # unconcluded merge (MERGE_HEAD present) is theirs to abort; our own
        # stale one (registry marker merge_in_flight) we conclude ourselves.
        if _main_mid_merge(main):
            reg_entry = load_registry(main).get(branch, {})
            if reg_entry.get("merge_in_flight"):
                _abort_merge(main)
            if _main_mid_merge(main):
                return _park(main, lane, branch,
                             "main already mid-merge (foreign actor) — run "
                             "`git merge --abort` on main, then retry",
                             push=not args.no_push)
        _set_in_flight(main, branch, lane, True)
        try:
            # 4 MERGE
            rc, out, err = _git(main, "merge", "--no-ff", "--no-edit", branch, timeout=300)
            if rc != 0:
                rc2, merging, _ = _git(main, "rev-parse", "-q", "--verify", "MERGE_HEAD")
                if rc2 != 0:  # merge never started (e.g. untracked-overwrite refusal)
                    return _park(main, lane, branch, f"merge refused: {(err or out)[:120]}",
                                 push=not args.no_push)
                rc2, u_raw, _ = _git(main, "diff", "--name-only", "--diff-filter=U")
                unresolved = []
                for u in u_raw.splitlines():
                    if not u:
                        continue
                    rc_ign, _, _ = _git(main, "check-ignore", "-q", "--", u)
                    rc_del, del_out, _ = _git(main, "ls-files", "-u", "--", u)
                    stages = {p.split()[2] for p in del_out.splitlines() if len(p.split()) >= 3}
                    if rc_ign == 0:
                        # Tracked leftover that main's .gitignore now covers: drop
                        # from index, file survives on disk (rule 4c, conflict form).
                        _git(main, "rm", "-q", "--cached", "--", u)
                    elif "3" not in stages and "2" in stages:
                        # modify/delete, theirs deleted ours modified: keep ours —
                        # never let a lane's deletion erase main's evolved copy.
                        _git(main, "add", "--", u)
                    elif _is_generated(u):
                        _git(main, "checkout", "--ours", "--", u)
                        _git(main, "add", "--", u)
                        if u not in gen_touched:
                            gen_touched.append(u)
                    elif u.endswith(".jsonl") or u in UNION_DOCS:
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
                    elif _theirs_is_stale(main, u) or _theirs_only_stamps(main, u):
                        # Branch side provably holds no information main lacks
                        # (stale snapshot of main history, or stamp-only churn).
                        _git(main, "checkout", "--ours", "--", u)
                        _git(main, "add", "--", u)
                    else:
                        unresolved.append(u)
                if unresolved:
                    abort_err = _abort_merge(main)
                    suffix = (f" — WARNING: main left mid-merge, abort failed: {abort_err}"
                              if abort_err else "")
                    if abort_err:
                        print(f"MAIN MID-MERGE — ABORT FAILED: {abort_err}", file=sys.stderr)
                    return _park(main, lane, branch,
                                 f"conflict in {', '.join(unresolved[:3])}"
                                 + (f" +{len(unresolved)-3} more" if len(unresolved) > 3 else "")
                                 + suffix,
                                 push=not args.no_push)
                _git(main, "commit", "--no-edit")

            # 5 LAW-3 AUDIT — every branch-added file must exist on merged main
            dropped = [f for f in added
                       if _git(main, "cat-file", "-e", f"HEAD:{f}")[0] != 0]
            if dropped:
                _git(main, "reset", "--merge", "ORIG_HEAD")
                return _park(main, lane, branch,
                             f"Law-3 audit failed: merge dropped {dropped[0]}"
                             + (f" +{len(dropped)-1} more" if len(dropped) > 1 else ""),
                             push=not args.no_push)

            # 6 REGEN — generated artifacts are rebuilt, never hand-merged
            if gen_touched:
                py = main / ".venv" / "bin" / "python3"
                py = str(py) if py.exists() else sys.executable
                for g, gargs in GENERATORS:
                    subprocess.run([py, str(main / "execution" / g), *gargs],
                                   capture_output=True, timeout=600, cwd=str(main))
                rc, out, _ = _git(main, "status", "--porcelain")
                if out.strip():
                    _git(main, "add", "--", *sorted(GENERATED_FILES), ".claude/commands")
                    _git(main, "commit", "-m",
                         "chore(lane): regenerate indexes post-merge")

        except Exception as e:  # any crash inside the merge body
            abort_err = _abort_merge(main)
            note = f" — WARNING: main left mid-merge, abort failed: {abort_err}" if abort_err else ""
            return _park(main, lane, branch,
                         f"merge crashed: {type(e).__name__}: {str(e)[:120]}{note}",
                         push=not args.no_push)
        _set_in_flight(main, branch, lane, False)

        # 7 PUSH (optional: local reconciliation does not imply remote export)
        if args.no_push:
            push_note = " (local only — push skipped)"
        else:
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


def _status_paths(porcelain: str) -> "tuple[list[str], list[str]]":
    """(tracked dirty paths, untracked paths) from `status --porcelain`.
    Renames ("R  old -> new") contribute both sides."""
    tracked, untracked = [], []
    for line in porcelain.splitlines():
        if not line.strip():
            continue
        if line.startswith("??"):
            untracked.append(line[3:])
            continue
        # `_git` strips stdout, so the FIRST line may have lost its leading
        # status space (" M path" -> "M path"). Split on the first run of
        # whitespace after the status token instead of slicing at column 3
        # (evidenced 2026-09-02: ".agent/x" became "agent/x").
        parts = line.split(None, 1)
        rest = parts[1] if len(parts) == 2 else line[3:]
        if " -> " in rest:
            a, b = rest.split(" -> ", 1)
            tracked.extend([a, b])
        else:
            tracked.append(rest)
    return sorted(set(tracked)), sorted(set(untracked))


def cmd_preserve(args) -> int:
    """Move human work stranded on main into its own lane, leaving main clean.

    The missing counterpart to main_drift_absorb (which sweeps MACHINE drift
    and correctly ABORTS on human-authored paths). Scar (2026-09-02): 134
    staged deliverable files sat on main; every lane parked on "main dirty";
    no audited command could move them, so nothing merged for hours.

    Loss-proof by construction (Law 3): the preserve lane's commit is written
    and verified to contain every dirty tracked path BEFORE main is touched.
    Untracked files are never moved — listed only. The new lane is registered
    like any other, so the normal `merge` brings the work back as a real commit.
    """
    main = main_root(Path.cwd())
    if _main_mid_merge(main):
        print("ERROR: main is mid-merge (MERGE_HEAD). Conclude or abort that merge first.",
              file=sys.stderr)
        return 1
    rc, out, _ = _git(main, "status", "--porcelain")
    tracked, untracked = _status_paths(out)
    if not tracked:
        print("MAIN CLEAN: no tracked changes to preserve"
              + (f" ({len(untracked)} untracked left alone)" if untracked else ""))
        return 0
    writer = fresh_main_writer(main, own_lock_token=getattr(args, "lock_token", None))
    if writer:
        print(f"REFUSED: main has a fresh writer: {writer}", file=sys.stderr)
        return 1
    slug = re.sub(r"[^a-z0-9-]+", "-", (args.slug or "main-dirty").lower()).strip("-")
    stamp = datetime.now().strftime("%Y%m%d")
    branch = f"worktree-main-dirty-preserve-{stamp}-{slug}"
    lane = main / ".claude" / "worktrees" / f"main-dirty-preserve-{stamp}-{slug}"
    if branch in active_lanes(main) or lane.exists():
        print(f"ERROR: {branch} already exists — pass a different --slug", file=sys.stderr)
        return 1
    print(f"PRESERVE: {len(tracked)} tracked path(s) on main -> lane {branch}")
    if untracked:
        print(f"  ({len(untracked)} untracked path(s) stay where they are)")
    if args.dry_run:
        for p_ in tracked[:20]:
            print("   ", p_)
        if len(tracked) > 20:
            print(f"    … +{len(tracked)-20} more")
        return 0

    # 1 LANE at main's HEAD, then copy the working-tree state of every dirty path
    rc, _, err = _git(main, "worktree", "add", str(lane), "-b", branch, "HEAD", timeout=120)
    if rc != 0:
        print(f"ERROR: worktree add failed: {err[:200]}", file=sys.stderr)
        return 1
    for rel in tracked:
        src, dst = main / rel, lane / rel
        if src.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
        elif dst.exists():
            dst.unlink()
    # Whole-tree add: the fresh lane differs from HEAD in exactly the copied
    # paths, and a pathspec form would abort the ENTIRE add when one path no
    # longer exists on either side (renames/deletes) — evidenced 2026-09-02.
    rc, out, err = _git(lane, "add", "-A")
    if rc != 0:
        print(f"ERROR: preserve add failed: {(err or out)[:300]} — main untouched; "
              f"removing the half-built lane", file=sys.stderr)
        _git(main, "worktree", "remove", "--force", str(lane))
        _git(main, "update-ref", "-d", f"refs/heads/{branch}")
        return 1
    # Mechanical commit: repo hooks (auto-push, closeout) stay out of it — our
    # own --push handles the remote, and a hook failing in a fresh worktree
    # must never look like "nothing to preserve".
    rc, out, err = _git(lane, "-c", "core.hooksPath=/dev/null", "commit", "-q", "-m",
                        f"chore(preserve): human work stranded on main ({len(tracked)} paths)")
    if rc != 0:
        print(f"ERROR: preserve commit failed: {(err or out)[:300]} — main untouched; "
              f"removing the half-built lane", file=sys.stderr)
        _git(main, "worktree", "remove", "--force", str(lane))
        _git(main, "update-ref", "-d", f"refs/heads/{branch}")
        return 1

    # 2 LAW-3 — every surviving path must be in the preserve commit before main moves
    missing = [rel for rel in tracked
               if (main / rel).exists()
               and _git(lane, "cat-file", "-e", f"HEAD:{rel}")[0] != 0]
    if missing:
        print(f"ERROR: preserve commit lacks {missing[0]} (+{len(missing)-1} more) — "
              f"main untouched; lane {branch} kept for inspection", file=sys.stderr)
        return 1

    # 3 RESTORE main to HEAD for exactly those paths (index + tree)
    _git(main, "reset", "-q", "--", *tracked)
    in_head = set(_git(main, "ls-tree", "-r", "--name-only", "HEAD", "--", *tracked)[1].splitlines())
    for rel in tracked:
        if rel in in_head:
            _git(main, "checkout", "-q", "HEAD", "--", rel)
        else:
            p_ = main / rel
            if p_.exists():
                p_.unlink()
    rc, out, _ = _git(main, "status", "--porcelain")
    still, _ = _status_paths(out)
    if still:
        print(f"WARNING: main still shows {len(still)} tracked change(s) after restore: "
              f"{', '.join(still[:3])}", file=sys.stderr)

    # 4 REGISTER + optional push
    reg = load_registry(main)
    reg[branch] = {"path": str(lane), "status": "active", "harness": "preserve",
                   "created": datetime.now().isoformat(timespec="seconds"),
                   "reason": f"preserved {len(tracked)} human-authored path(s) from main"}
    save_registry(main, reg)
    push_note = ""
    if getattr(args, "push", False):
        rc, _, err = _git(lane, "push", "-u", "origin", branch, timeout=120)
        push_note = " (pushed)" if rc == 0 else f" (push failed: {err[:80]})"
    print(f"PRESERVED: {len(tracked)} path(s) -> {branch}{push_note}. Land them with: "
          f"python3 execution/worktree_lane.py merge --lane {branch}")
    return 0


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
        for rel in SNAPSHOT_DIRS:
            src, dst = main / rel, path / rel
            if src.is_dir() and not os.path.lexists(dst):
                issues += 1
                notes.append(f"missing context snapshot: {rel}")
                if args.fix:
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copytree(src, dst)
                    notes.append("(snapshotted)")
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
    push_mode = m.add_mutually_exclusive_group()
    push_mode.add_argument("--push", action="store_false", dest="no_push",
                           help="explicitly push the merged main branch to origin")
    push_mode.add_argument("--no-push", action="store_true", dest="no_push",
                           help="compatibility alias; local-only is already the default")
    m.add_argument("--dry-run", action="store_true", dest="dry_run")
    m.add_argument("--lock-token", dest="lock_token",
                   help="session_lock token owned by the caller (own lock ≠ foreign writer)")
    m.add_argument("--exclude-session", dest="exclude_session", action="append",
                   help="session id to exclude from fresh-writer detection (repeatable)")
    m.set_defaults(fn=cmd_merge, no_push=True)

    pv = sub.add_parser("preserve",
                        help="move human work stranded on main into its own lane (main becomes clean)")
    pv.add_argument("--slug", help="lane suffix (default: main-dirty)")
    pv.add_argument("--dry-run", action="store_true", dest="dry_run")
    pv.add_argument("--push", action="store_true", help="push the preserve branch to origin")
    pv.add_argument("--lock-token", dest="lock_token")
    pv.set_defaults(fn=cmd_preserve)

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
