#!/usr/bin/env python3
"""
session_sweep.py — deterministic session collector for the Mission Briefing Room.

Combs recent Claude Code AND Codex session records, attributes what was made to
the ONGOING THREAD it belongs to, applies a mechanical promotion bar, and writes
a fact bundle. Zero LLM calls, stdlib only, read-only on every source it touches.

WHY THIS EXISTS. The record of work was already on disk in six places — handoffs,
the finalize ledger, session ledgers, the asset manifest, missions, git — and
nowhere assembled. "What is the state of this thread" required hunting. This is
the assembler; mission_brief.py is the surface.

THE PROMOTION BAR IS THE POINT, and it turns on one distinction:

  DECLARING evidence mints a thread — a live handoff, an open mission, or a
  finalized deliverable. Someone named this work, or it shipped.

  ACTIVITY evidence only enriches one — files written, assets generated,
  commits landed. These say "work happened", never "a mission exists".

Letting activity mint cards is exactly how this becomes a slop library: the first
run promoted 254 of 467 keys, because every generated image and every write into
a shared output folder claimed to be its own mission. Read-only sessions, config
fiddling and asset dumps now mint nothing. The bar is mechanical on purpose — a
judgment call here would drift session to session.

FACTS ONLY. Every field this writes is copied from a source of record. Nothing is
inferred beyond counting and date arithmetic. The meaning layer is authored
downstream against this bundle, and cannot touch a number (mission_brief.py).

FAIL-SAFE: every source reads in its own try/except; a source that fails is
REPORTED in `degraded`, never silently skipped. Exit 0 always.

Usage:
    python3 execution/session_sweep.py run [--days N] [--since ISO] [--dry-run] [--json]
    python3 execution/session_sweep.py status

Outputs: .agent/sweep/sweep-<date>.json (durable record) + .agent/sweep/latest.json
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SWEEP_DIR = ROOT / ".agent" / "sweep"
LATEST = SWEEP_DIR / "latest.json"

HOME = Path.home()
CLAUDE_PROJECTS = HOME / ".claude" / "projects"
CODEX_INDEX = HOME / ".codex" / "session_index.jsonl"
CODEX_REGISTRY = HOME / ".codex" / "end-session" / "registry.jsonl"

PERF_LOG = ROOT / ".agent" / "performance-log.jsonl"
MISSIONS = ROOT / ".agent" / "missions.jsonl"
ASSETS = ROOT / ".agent" / "assets" / "manifest.jsonl"
LEDGERS = ROOT / ".agent" / "sessions"
OUTCOMES = ROOT / ".agent" / "revenue-outcomes.json"
GUIDES = ROOT / "guides"
SOLUTIONS = ROOT / "docs" / "solutions"

DEFAULT_DAYS = 14
MAX_DAYS = 120   # a longer window reads history, not "recent" — cap it honestly
MAX_CARDS = 12   # front-door ceiling; the overflow is named, never silently dropped

# Shared with session_ledger_hook.py: a write matching this is control plane, not
# a deliverable. Kept in sync deliberately — the promotion bar and the ledger's
# own "produced" flag must agree on what counts as real work.
INTERNAL_WRITE = re.compile(r"/\.(agent|claude|tmp|memory)/|\.json$|\.jsonl$|/memory/")

# Handoff statuses that mean the thread is still live.
LIVE_STATUS = {"active", "blocked", "ready", "mid-build"}
OPEN_MISSION = {"compiled", "running"}

# Branch decorations that are lane plumbing, not thread identity.
BRANCH_PREFIX = re.compile(r"^(codex/|worktree-|claude/|brief/)")


# ── small helpers ───────────────────────────────────────────────────
def slugify(s):
    s = re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")
    return s or ""


def iso(dt):
    return dt.replace(microsecond=0).isoformat()


def parse_ts(s):
    """Best-effort ISO/epoch → datetime. Returns None rather than guessing."""
    if s is None or s == "":
        return None
    if isinstance(s, (int, float)):
        # sessions-index.json carries fileMtime in epoch MILLIseconds.
        return datetime.fromtimestamp(s / 1000.0 if s > 1e11 else s)
    txt = str(s).strip().replace("Z", "+00:00")
    for cut in (None, 19, 10):
        try:
            d = datetime.fromisoformat(txt if cut is None else txt[:cut])
            return d.replace(tzinfo=None)
        except ValueError:
            continue
    return None


def jsonl(path, limit_bytes=None):
    """Read a JSONL file, skipping unparseable lines rather than dying on one."""
    out = []
    p = Path(path)
    if not p.exists():
        return out
    with p.open("r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except ValueError:
                continue
    return out


def repo_rel(p):
    try:
        return str(Path(p).resolve().relative_to(ROOT))
    except (ValueError, OSError):
        return str(p)


# ── thread identity ─────────────────────────────────────────────────
class Registry:
    """Canonical thread keys. Named threads (handoffs, missions) win; derived
    keys collapse into them when they clearly refer to the same work.

    Collapsing is conservative — exact match, or containment with a >=6 char
    overlap. Anything shorter produces false merges ('jen' would swallow
    'jenny-hoyos'), and a wrong merge is worse than a duplicate card because it
    silently hides one thread inside another.
    """

    def __init__(self):
        self.canon = {}   # key -> canonical key
        self.named = []   # canonical keys declared by handoffs/missions

    def declare(self, key):
        key = slugify(key)
        if not key:
            return ""
        if key not in self.named:
            self.named.append(key)
        self.canon[key] = key
        return key

    def resolve(self, key):
        key = slugify(key)
        if not key:
            return ""
        if key in self.canon:
            return self.canon[key]
        for n in self.named:
            if len(n) >= 6 and (n in key or key in n):
                self.canon[key] = n
                return n
        self.canon[key] = key
        return key

    def match_title(self, text, min_tokens=2):
        """Best declared thread for a free-text session title.

        Session titles are prose ("Edit Bay Video Studio — Build + Taste Layer"),
        so slug containment never fires against `video-studio-edit-bay`. Token
        overlap does. Requires >=2 shared tokens of >=4 chars: one shared word
        ("build", "brand") matches half the repo and would cross-file work into
        the wrong thread, which is worse than leaving it unattributed.
        """
        toks = {w for w in re.split(r"[^a-z0-9]+", (text or "").lower()) if len(w) >= 4}
        if len(toks) < min_tokens:
            return ""
        best, best_n = "", 0
        for n in self.named:
            shared = len(toks & {w for w in n.split("-") if len(w) >= 4})
            if shared > best_n:
                best, best_n = n, shared
        return best if best_n >= min_tokens else ""


# Numbered buckets inside an initiative (directives/artifact-placement.md). These
# are FILING SLOTS, never thread identity — "05-assets" as a card title was the
# first thing the bar got wrong.
BUCKET_RE = re.compile(r"^(\d{2}-|_|99-archive$|archive$)")
BUCKET_NAMES = {"00-start-here", "01-source", "02-research", "03-working-drafts",
                "04-deliverables", "05-assets", "06-system", "90-exports",
                "99-archive", "_archive", "archive", "visuals", "assets"}

# Shared output surfaces — many threads write here, so the directory name is a
# destination, not a thread. Attributing to these merged unrelated work.
NON_THREAD_DIRS = {"research-briefs", "generations", "images", "designs",
                   "carousel-images", "video-enhancement", "exports", "tmp"}


def thread_from_path(rel):
    """The INITIATIVE that owns a path — the unit front_door.py indexes.

    Shape is `_active/<arena>/<initiative>/<NN-bucket>/…`, but arena-less
    initiatives (`_active/<initiative>/<NN-bucket>/`) are equally common, so the
    initiative is found as "the component before the first numbered bucket"
    rather than by fixed depth.
    """
    parts = [p for p in Path(str(rel)).parts if p not in (".", "/")]
    if not parts:
        return ""
    if parts[0] == "_active":
        rest = parts[1:]
        for i, p in enumerate(rest):
            if p.lower() in BUCKET_NAMES or BUCKET_RE.match(p.lower()):
                return slugify(rest[i - 1]) if i >= 1 else ""
        # No bucket in the path: <arena>/<initiative>/file → initiative.
        if len(rest) >= 3:
            return slugify(rest[1])
        return slugify(rest[0]) if len(rest) >= 2 else ""
    if parts[0] in ("deliverables", "projects", "extractions", "skills") and len(parts) >= 2:
        name = parts[1].lower()
        if name in NON_THREAD_DIRS or name in BUCKET_NAMES:
            return ""
        return slugify(parts[1])
    return ""


def thread_from_branch(branch):
    b = (branch or "").strip()
    if not b or b in ("main", "master", "HEAD"):
        return ""
    return slugify(BRANCH_PREFIX.sub("", b))


def arena_from_path(rel):
    parts = Path(str(rel)).parts
    if len(parts) >= 2 and parts[0] == "_active":
        return parts[1]
    return parts[0] if parts else ""


# ── collectors (each returns data; each caller wraps in try/except) ──
def collect_claude_sessions(since):
    """~/.claude/projects/*/sessions-index.json — the cheap index Claude Code
    maintains itself. Reading the 2,600+ raw .jsonl transcripts would cost
    minutes for facts this file already carries."""
    out = []
    if not CLAUDE_PROJECTS.exists():
        return out
    for idx in CLAUDE_PROJECTS.glob("*/sessions-index.json"):
        try:
            data = json.loads(idx.read_text(encoding="utf-8", errors="replace"))
        except (OSError, ValueError):
            continue
        for e in data.get("entries", []):
            ts = parse_ts(e.get("modified")) or parse_ts(e.get("fileMtime"))
            if ts is None or ts < since:
                continue
            out.append({
                "harness": "claude",
                "id": e.get("sessionId") or "",
                "title": (e.get("customTitle") or e.get("firstPrompt") or "").strip()[:200],
                "titled": bool(e.get("customTitle")),
                "ts": iso(ts),
                "messages": e.get("messageCount") or 0,
                "branch": e.get("gitBranch") or "",
                "project": idx.parent.name,
                "sidechain": bool(e.get("isSidechain")),
            })
    return out


def collect_codex_sessions(since):
    """~/.codex/session_index.jsonl — thread_name already follows the
    `[Domain]: [Object] - [Outcome]` end-session convention, so Codex threads
    arrive pre-titled. The end-session registry adds status + handoff pointer."""
    out = []
    for rec in jsonl(CODEX_INDEX):
        ts = parse_ts(rec.get("updated_at"))
        if ts is None or ts < since:
            continue
        out.append({
            "harness": "codex",
            "id": rec.get("id") or "",
            "title": (rec.get("thread_name") or "").strip()[:200],
            "titled": bool(rec.get("thread_name")),
            "ts": iso(ts),
            "messages": 0,
            "branch": "",
            "project": "codex",
            "sidechain": False,
        })
    return out


def collect_codex_closeouts(since):
    out = []
    for rec in jsonl(CODEX_REGISTRY):
        ts = parse_ts(rec.get("ts"))
        if ts is None or ts < since:
            continue
        out.append({
            "slug": slugify(rec.get("slug")),
            "title": rec.get("title") or "",
            "status": rec.get("status") or "",
            "branch": rec.get("branch") or "",
            "handoff": rec.get("handoff_path") or "",
            "ts": iso(ts),
        })
    return out


def collect_ledgers(since):
    """.agent/sessions/ledger-*.json — produced_paths[] is the per-session list
    of real artifacts, written by the SHARED session_ledger_hook, so Codex
    sessions land here identically.

    Caveat carried forward, not hidden: the hook keeps only the last 10 paths per
    session and prunes ledgers at 7 days. That is why this sweep persists its own
    dated bundle — once swept, kept."""
    out = []
    if not LEDGERS.exists():
        return out
    for f in LEDGERS.glob("ledger-*.json"):
        try:
            st = f.stat()
            if datetime.fromtimestamp(st.st_mtime) < since:
                continue
            data = json.loads(f.read_text(encoding="utf-8", errors="replace"))
        except (OSError, ValueError):
            continue
        paths = [p for p in (data.get("produced_paths") or [])
                 if p and not INTERNAL_WRITE.search(str(p))]
        # Prefer the FILE's own mtime over the ledger's: a ledger stamp is when
        # the session last wrote anything, which stacks a week of work onto one
        # day and makes the momentum chart lie. Fall back only if the file moved.
        produced = []
        for p in paths:
            when = datetime.fromtimestamp(st.st_mtime)
            try:
                fp = Path(p)
                if not fp.is_absolute():
                    fp = ROOT / p
                when = datetime.fromtimestamp(fp.stat().st_mtime)
            except OSError:
                pass
            produced.append({"path": repo_rel(p), "ts": iso(when)})
        out.append({
            "session_id": data.get("session_id") or f.stem.replace("ledger-", ""),
            "ts": iso(datetime.fromtimestamp(st.st_mtime)),
            "produced": produced,
            "spawns": data.get("subagent_spawns") or 0,
            "finalized": bool(data.get("finalized_at")),
            "pinned": bool(data.get("session_pinned")),
        })
    return out


def collect_deliverables(since):
    """.agent/performance-log.jsonl — chain_runner finalize records. The single
    strongest signal that something actually shipped."""
    out = []
    for rec in jsonl(PERF_LOG):
        ts = parse_ts(rec.get("date"))
        if ts is None or ts < since:
            continue
        out.append({
            "date": rec.get("date") or "",
            "output": (rec.get("output") or "")[:400],
            "skill": rec.get("skill") or "",
            "workflow": rec.get("workflow") or "",
            "project": rec.get("project") or "",
            "type": rec.get("task_type") or "",
            "score": rec.get("quality_score"),
            "status": rec.get("status") or "",
            "expert": rec.get("agent") or "",
            "platform": "codex" if "platform: codex" in (rec.get("notes") or "") else "claude",
        })
    return out


def collect_assets(since):
    """Reduced asset manifest (latest line per path), filtered to the window."""
    latest = {}
    for rec in jsonl(ASSETS):
        p = rec.get("path")
        if p:
            latest[p] = rec
    out = []
    for p, rec in latest.items():
        if rec.get("status") not in (None, "", "active"):
            continue
        ts = parse_ts(rec.get("ts"))
        if ts is None or ts < since:
            continue
        out.append({
            "path": p,
            "type": rec.get("type") or "",
            "zone": rec.get("zone") or "",
            "project": rec.get("project") or "",
            "ts": iso(ts),
            "prompt": (rec.get("prompt") or "")[:300],
            "model": rec.get("model") or rec.get("src") or "",
            "cost_usd": rec.get("cost_usd") or 0,
        })
    return out


def collect_missions():
    """Latest state per mission, keyed the way pulse_dashboard keys it so the two
    surfaces can never disagree about what is open."""
    latest = {}
    for m in jsonl(MISSIONS):
        key = m.get("slug") or " ".join((m.get("mission") or "?").split())
        latest[key] = m
    out = []
    for key, m in latest.items():
        ts = parse_ts(m.get("ts"))
        out.append({
            "key": key,
            "slug": slugify(m.get("slug") or key),
            "title": (m.get("mission") or key)[:200],
            "status": m.get("status") or "",
            "serves": m.get("serves") or "",
            "tier": m.get("tier") or "",
            "ts": iso(ts) if ts else "",
            "open": m.get("status") in OPEN_MISSION,
        })
    return out


def collect_threads():
    """handoff_store.threads() — the thread IS already the unit there.

    `include_done=False`: a closed thread is history, and history belongs in the
    archive shelf, not on the front door.
    """
    sys.path.insert(0, str(ROOT / "execution"))
    import handoff_store  # noqa: E402
    out = []
    for m in handoff_store.threads(include_done=False):
        ts = parse_ts(m.get("date"))
        mt = m.get("mtime")
        touched = max(filter(None, [ts, parse_ts(mt) if mt else None]), default=None)
        out.append({
            "slug": slugify(m.get("thread")),
            "thread": m.get("thread") or "",
            "title": m.get("title") or "",
            "status": m.get("status") or "",
            "resume_hint": m.get("resume_hint") or "",
            "unfinished": m.get("unfinished") or "",
            "branch": m.get("branch") or "",
            "date": m.get("date") or "",
            "touched": iso(touched) if touched else "",
            "pin": bool(m.get("pin")),
            "path": repo_rel(m.get("path")) if m.get("path") else "",
        })
    return out


def collect_commits(since):
    cmd = ["git", "log", f"--since={since.strftime('%Y-%m-%d')}",
           "--pretty=format:%H%x1f%aI%x1f%s", "--name-only", "-z"]
    res = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True, timeout=60)
    if res.returncode != 0:
        raise RuntimeError((res.stderr or "git log failed").strip()[:200])
    out = []
    for block in res.stdout.split("\n\n"):
        if not block.strip():
            continue
        head, _, rest = block.partition("\n")
        bits = head.split("\x1f")
        if len(bits) < 3:
            continue
        files = [f for f in rest.replace("\x00", "\n").split("\n") if f.strip()]
        ts = parse_ts(bits[1])
        out.append({
            "sha": bits[0][:9],
            "ts": iso(ts) if ts else "",
            "subject": bits[2][:200],
            "files": files[:200],
        })
    return out


def collect_new_files(folder, since, suffix=".md"):
    out = []
    if not Path(folder).exists():
        return out
    for f in Path(folder).glob(f"*{suffix}"):
        try:
            st = f.stat()
        except OSError:
            continue
        if datetime.fromtimestamp(st.st_mtime) < since:
            continue
        out.append({"path": repo_rel(f), "name": f.name,
                    "ts": iso(datetime.fromtimestamp(st.st_mtime))})
    return sorted(out, key=lambda x: x["ts"], reverse=True)


def collect_outcomes():
    try:
        data = json.loads(OUTCOMES.read_text(encoding="utf-8", errors="replace"))
    except (OSError, ValueError):
        return []
    out = []
    for o in data.get("outcomes", []):
        out.append({
            "deliverable": (o.get("deliverable") or "")[:200],
            "workflow": o.get("workflow") or "",
            "skill": o.get("skill") or "",
            "revenue": o.get("revenue") or 0,
            "outcome": (o.get("outcome") or "")[:300],
        })
    return out


# ── assembly ────────────────────────────────────────────────────────
def blank_thread(key):
    return {
        "slug": key, "title": "", "arena": "", "status": "", "resume_hint": "",
        "unfinished": "", "branch": "", "handoff": "", "pin": False,
        "sessions": [], "deliverables": [], "artifacts": [], "assets": [],
        "commits": [], "missions": [], "guides": [], "solutions": [],
        "outcomes": [], "harnesses": [],
        "promoted": False, "declares": [], "activity": [],
    }


def daily_counts(items, since, days):
    """One integer per day in the window, oldest first. Feeds the spark chart."""
    base = since.date()
    buckets = [0] * days
    for it in items:
        ts = parse_ts(it.get("ts") if isinstance(it, dict) else it)
        if ts is None:
            continue
        i = (ts.date() - base).days
        if 0 <= i < days:
            buckets[i] += 1
    return buckets


def infer_stage(t):
    """Lifecycle position from evidence only. Each stage requires a record —
    nothing is inferred from vibes or elapsed time."""
    if t["outcomes"]:
        return "outcome"
    if t["deliverables"]:
        return "shipped"
    if t["artifacts"] or t["assets"] or t["commits"]:
        return "build"
    return "research"


STAGES = ["research", "build", "shipped", "outcome"]


def sweep(days=DEFAULT_DAYS, since=None):
    days = max(1, min(int(days), MAX_DAYS))
    if since is None:
        since = datetime.now() - timedelta(days=days)
    else:
        days = max(1, min((datetime.now() - since).days + 1, MAX_DAYS))
    degraded = []
    reg = Registry()
    threads = {}

    def get(key):
        key = reg.resolve(key) or "unattributed"
        if key not in threads:
            threads[key] = blank_thread(key)
        return threads[key]

    def source(name, fn, default=None):
        try:
            return fn()
        except Exception as e:  # noqa: BLE001 — a dead source must never kill the sweep
            degraded.append(f"{name}: {type(e).__name__}: {e}")
            return default if default is not None else []

    # 1. Named threads first — they define the canonical keys everything else
    #    collapses into. Order matters: derived keys resolve against `named`.
    handoffs = source("handoffs", collect_threads)
    for h in handoffs:
        key = reg.declare(h["slug"])
        if not key:
            continue
        t = threads.setdefault(key, blank_thread(key))
        t.update({
            "title": h["title"] or h["thread"], "status": h["status"],
            "resume_hint": h["resume_hint"], "unfinished": h["unfinished"],
            "branch": h["branch"], "handoff": h["path"], "pin": h["pin"],
            "touched": h["touched"],
        })
        # A handoff DECLARES a live thread only if it was touched inside the
        # window (or is explicitly pinned). 306 handoff files exist; a "ready"
        # one from two months ago is a memory, not a mission, and treating it as
        # live is what put 150+ dormant threads on the front door.
        touched = parse_ts(h["touched"])
        if h["status"] in LIVE_STATUS and (h["pin"] or (touched and touched >= since)):
            t["declares"].append(f"handoff status: {h['status']}")

    missions = source("missions", collect_missions)
    for m in missions:
        key = reg.declare(m["slug"]) if m["open"] else reg.resolve(m["slug"])
        if not key:
            continue
        t = threads.setdefault(key, blank_thread(key))
        t["missions"].append(m)
        if not t["title"]:
            t["title"] = m["title"]
        if m["open"]:
            t["declares"].append("open mission")

    # 2. Windowed evidence.
    for d in source("deliverables", lambda: collect_deliverables(since)):
        # `project` is a real thread name. `workflow`/`skill` are ROUTES — "go",
        # "resume", "deep-research" are how the work was made, not what it was
        # for. A route-only deliverable declares a thread only when that thread
        # already exists; otherwise it attaches as shipped work and surfaces in
        # the mission board's "also shipped" list, never as its own card.
        raw = d["project"] or d["workflow"] or d["skill"] or d["expert"]
        key = reg.resolve(raw)
        t = get(raw)
        t["deliverables"].append(d)
        if d["project"] or key in reg.named:
            t["declares"].append("finalized deliverable")
        else:
            t["activity"].append("shipped via route")
        if d["platform"] not in t["harnesses"]:
            t["harnesses"].append(d["platform"])

    ledgers = source("ledgers", lambda: collect_ledgers(since))
    seen_art = set()
    for lg in ledgers:
        for art in lg["produced"]:
            path = art["path"]
            t = get(thread_from_path(path))
            if (t["slug"], path) in seen_art:
                continue
            seen_art.add((t["slug"], path))
            t["artifacts"].append(art)
            t["activity"].append("artifact written")
            if not t["arena"]:
                t["arena"] = arena_from_path(path)

    for a in source("assets", lambda: collect_assets(since)):
        t = get(a["project"] or thread_from_path(a["path"]))
        t["assets"].append(a)
        t["activity"].append("asset generated")

    for c in source("commits", lambda: collect_commits(since)):
        keys = {thread_from_path(f) for f in c["files"]}
        keys.discard("")
        for key in (keys or {"unattributed"}):
            t = get(key)
            t["commits"].append({k: c[k] for k in ("sha", "ts", "subject")})

    sessions = source("claude sessions", lambda: collect_claude_sessions(since))
    sessions += source("codex sessions", lambda: collect_codex_sessions(since))
    for s in sessions:
        if s["sidechain"]:
            continue  # subagent transcripts are not sessions of their own
        key = (thread_from_branch(s["branch"])
               or reg.match_title(s["title"])
               or (slugify(s["title"])[:60] if s["titled"] else ""))
        t = get(key)
        t["sessions"].append(s)
        if s["harness"] not in t["harnesses"]:
            t["harnesses"].append(s["harness"])

    for c in source("codex closeouts", lambda: collect_codex_closeouts(since)):
        t = get(c["slug"])
        if not t["title"]:
            t["title"] = c["title"]
        if not t["status"]:
            t["status"] = c["status"]
        if "codex" not in t["harnesses"]:
            t["harnesses"].append("codex")

    for g in source("guides", lambda: collect_new_files(GUIDES, since)):
        get(slugify(re.sub(r"^\d{4}-\d{2}-\d{2}-", "", g["name"]).replace(".md", "")))["guides"].append(g)
    for s in source("solutions", lambda: collect_new_files(SOLUTIONS, since)):
        get(slugify(re.sub(r"^\d{4}-\d{2}-\d{2}-", "", s["name"]).replace(".md", "")))["solutions"].append(s)

    for o in source("outcomes", collect_outcomes):
        if not (o["workflow"] or o["skill"]):
            continue
        key = reg.resolve(o["workflow"] or o["skill"])
        if key in threads and o["outcome"]:
            threads[key]["outcomes"].append(o)

    # 3. The promotion bar. Mechanical — no judgment, no drift.
    for key, t in threads.items():
        t["declares"] = sorted(set(t["declares"]))
        t["activity"] = sorted(set(t["activity"]))
        t["promotion_reasons"] = t["declares"] + t["activity"]
        # THE BAR: a thread exists because it was DECLARED (handoff / open
        # mission) or because it SHIPPED (finalize record). Files, assets and
        # commits are evidence of activity ON a thread — they enrich a card,
        # they never mint one. Without this split, every generated image and
        # every write into a shared output folder became its own "mission"
        # (254 of 467 keys promoted on the first run).
        t["promoted"] = bool(t["declares"]) and key != "unattributed"
        t["stage"] = infer_stage(t)
        t["stage_index"] = STAGES.index(t["stage"])
        t["daily"] = {
            "sessions": daily_counts(t["sessions"], since, days),
            "artifacts": daily_counts(t["artifacts"], since, days),
            "assets": daily_counts(t["assets"], since, days),
        }
        stamps = [x.get("ts") or x.get("date") for x in
                  (t["sessions"] + t["assets"] + t["commits"] + t["deliverables"])]
        stamps = sorted(s for s in stamps if s)
        t["first_seen"] = stamps[0] if stamps else ""
        t["last_active"] = stamps[-1] if stamps else ""
        if not t["title"]:
            t["title"] = key.replace("-", " ")
        if not t["arena"] and t["artifacts"]:
            t["arena"] = arena_from_path(t["artifacts"][0]["path"])

    promoted = {k: v for k, v in threads.items() if v["promoted"]}

    # Final backstop. The bar above is principled, but upstream data can always
    # surprise it, and a front door that quietly grows to 40 cards has failed
    # whatever its reasoning was. Rank by substance, then recency, and keep the
    # top MAX_CARDS. Everything cut is NAMED in `overflow` and printed — a
    # silent cap reads as "that's everything", which is the lie that matters.
    def substance(kv):
        t = kv[1]
        return (
            len(t["deliverables"]) * 3 + len(t["missions"]) * 2 + t["pin"] * 2
            + min(len(t["artifacts"]), 5) + min(len(t["assets"]), 3),
            t["last_active"],
        )

    ranked = sorted(promoted.items(), key=substance, reverse=True)
    overflow = [k for k, _ in ranked[MAX_CARDS:]]
    promoted = dict(ranked[:MAX_CARDS])

    # Shipped work that never earned a card still has to be visible somewhere.
    also_shipped = []
    for k, t in threads.items():
        if k in promoted or not t["deliverables"]:
            continue
        for d in t["deliverables"]:
            also_shipped.append({"thread": k, "date": d["date"], "output": d["output"][:160],
                                 "workflow": d["workflow"], "type": d["type"]})
    also_shipped.sort(key=lambda x: x["date"], reverse=True)

    bundle = {
        "generated": iso(datetime.now()),
        "window": {"since": iso(since), "until": iso(datetime.now()), "days": days},
        "degraded": degraded,
        "counts": {
            "sessions": len(sessions),
            "threads_seen": len(threads),
            "threads_promoted": len(promoted),
            "deliverables": sum(len(t["deliverables"]) for t in threads.values()),
            "artifacts": sum(len(t["artifacts"]) for t in threads.values()),
            "assets": sum(len(t["assets"]) for t in threads.values()),
        },
        "threads": promoted,
        "also_shipped": also_shipped[:40],
        "overflow": overflow,
        "filtered_out": sorted(k for k, v in threads.items() if not v["promoted"]),
    }
    bundle["counts"]["threads_promoted"] = len(promoted)
    bundle["counts"]["overflow"] = len(overflow)
    return bundle


def write_bundle(bundle):
    SWEEP_DIR.mkdir(parents=True, exist_ok=True)
    day = bundle["generated"][:10]
    dated = SWEEP_DIR / f"sweep-{day}.json"
    payload = json.dumps(bundle, indent=2) + "\n"
    for target in (dated, LATEST):
        tmp = target.with_suffix(".tmp")
        tmp.write_text(payload, encoding="utf-8")
        os.replace(tmp, target)
    return dated


def cmd_run(args):
    since = parse_ts(args.since) if args.since else None
    bundle = sweep(days=args.days, since=since)
    path = None
    if not args.dry_run:
        path = write_bundle(bundle)
    if args.json:
        print(json.dumps(bundle, indent=2))
        return 0
    c = bundle["counts"]
    print(f"[session_sweep] window {bundle['window']['days']}d — "
          f"{c['sessions']} sessions, {c['threads_promoted']}/{c['threads_seen']} threads promoted, "
          f"{c['deliverables']} deliverables, {c['artifacts']} artifacts, {c['assets']} assets")
    for key, t in sorted(bundle["threads"].items(),
                         key=lambda kv: kv[1]["last_active"], reverse=True):
        print(f"  · {key:38} {t['stage']:8} {', '.join(t['promotion_reasons'])[:70]}")
    if bundle["overflow"]:
        print(f"[session_sweep] over the {MAX_CARDS}-card ceiling ({len(bundle['overflow'])}), "
              f"not carded: {', '.join(bundle['overflow'][:10])}")
    if bundle["also_shipped"]:
        print(f"[session_sweep] shipped without a live thread: {len(bundle['also_shipped'])} "
              f"(surfaces on the mission board)")
    if bundle["filtered_out"]:
        print(f"[session_sweep] below the bar ({len(bundle['filtered_out'])}): "
              f"{', '.join(bundle['filtered_out'][:8])}")
    for d in bundle["degraded"]:
        print(f"[session_sweep] DEGRADED {d}")
    if path:
        print(f"[session_sweep] wrote {repo_rel(path)}")
    return 0


def cmd_status(args):
    if not LATEST.exists():
        print("[session_sweep] no sweep yet — run: python3 execution/session_sweep.py run")
        return 0
    b = json.loads(LATEST.read_text(encoding="utf-8"))
    age = (datetime.now() - (parse_ts(b.get("generated")) or datetime.now())).total_seconds() / 3600
    print(json.dumps({"generated": b.get("generated"), "age_hours": round(age, 1),
                      "counts": b.get("counts"), "degraded": b.get("degraded")}, indent=2))
    return 0


def main():
    ap = argparse.ArgumentParser(description="Deterministic session sweep across Claude Code + Codex.")
    sub = ap.add_subparsers(dest="command", required=True)
    r = sub.add_parser("run", help="Collect the window and write the fact bundle.")
    r.add_argument("--days", type=int, default=DEFAULT_DAYS, help=f"Window in days (default {DEFAULT_DAYS}).")
    r.add_argument("--since", default=None, help="ISO timestamp; overrides --days.")
    r.add_argument("--dry-run", action="store_true", help="Collect and print, write nothing.")
    r.add_argument("--json", action="store_true", help="Emit the full bundle as JSON.")
    sub.add_parser("status", help="Age + counts of the last sweep.")
    args = ap.parse_args()
    try:
        return cmd_run(args) if args.command == "run" else cmd_status(args)
    except Exception as e:  # noqa: BLE001
        print(f"[session_sweep] FAILED (non-blocking): {type(e).__name__}: {e}", file=sys.stderr)
        return 0


if __name__ == "__main__":
    sys.exit(main())
