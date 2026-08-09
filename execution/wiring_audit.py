#!/usr/bin/env python3
"""wiring_audit.py — Tier 3 of the dead-channel layer: the full-asset wiring ratchet.

An asset is REAL only when a firing path exists: a hook, a launchd job, a spine
step, or an invocable registration something actually routes through. This
module proves (or fails to prove) that path for every asset in the inventory,
~BATCH per day, so the historical backlog drains to zero in about a month and
then the audit is maintenance-only.

WHAT "DRAIN" MEANS (Farrice, 2026-07-28): read-only audit. Nothing is ever
deleted, disabled, moved, or rewritten by this module. Outcomes per asset:
  PROVEN — a firing path exists (recorded with the path that proved it)
  ORPHAN — no firing path found (flagged; fixing/archiving is a human call,
           surfaced via self_heal.detect_wiring_orphans -> /cos + session open)

PROOF RULES (the fire path, never mere existence —
docs/solutions/2026-07-21-wired-but-never-loaded-prompts.md):
  workflow  a .claude/commands/<name>.md wrapper exists (menu-parity mints and
            maintains these), OR the name is in SLASH_COMMANDS.md, OR the file
            declares `status: superseded` (a deliberate redirect is wired).
  skill     listed in SKILL_INDEX.md (the router hook demonstrably fires every
            prompt and matches against the index), OR referenced by a wrapper
            or workflow.
  agent     listed in AGENT_INDEX.md.
  execution referenced by a hook command in .claude/settings.json, a launchd
            plist, another execution script, a workflow, or a directive.
            verify_*.py are PROVEN as a class: verify_fleet.py globs them.
            hooks/*.py must appear in .claude/settings.json specifically.

Usage:
    python3 execution/wiring_audit.py drain [--batch 150]   # audit next batch
    python3 execution/wiring_audit.py status                # coverage summary
    python3 execution/wiring_audit.py check <path>          # one asset, now
State: .agent/health/wiring-index.json (append-forward; PROVEN is re-checked
only after all assets have been seen once). Exit 0 always — compass doctrine.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / ".agent" / "health" / "wiring-index.json"
DEFAULT_BATCH = 150  # pinned; weekly-closeout passes --batch 400

WRAPPER_DIR = ROOT / ".claude" / "commands"
WORKFLOW_DIR = ROOT / ".agent" / "workflows"
SKILLS_DIR = ROOT / "skills"
AGENTS_DIR = ROOT / "agents"
EXEC_DIR = ROOT / "execution"
LAUNCHD_DIR = Path.home() / "Library" / "LaunchAgents"


# ──────────────────────────────────────────────────────────────────
# inventory
# ──────────────────────────────────────────────────────────────────
def inventory() -> list[str]:
    """Stable, sorted asset keys: '<class>:<name>'."""
    out = []
    try:
        out += [f"workflow:{p.stem}" for p in WORKFLOW_DIR.glob("*.md")]
        out += [f"skill:{p.parent.name}" for p in SKILLS_DIR.glob("*/SKILL.md")]
        out += [f"agent:{p.parent.name}" for p in AGENTS_DIR.glob("*/AGENT.md")]
        out += [f"execution:{p.relative_to(EXEC_DIR)}" for p in EXEC_DIR.rglob("*.py")
                if ".venv" not in p.parts and "__pycache__" not in p.parts
                and "archive" not in p.parts
                and not any(part.startswith("_archived") for part in p.parts)]
    except OSError:
        pass
    return sorted(set(out))


# ──────────────────────────────────────────────────────────────────
# reference corpora (built once per run, lazily)
# ──────────────────────────────────────────────────────────────────
class Corpus:
    def __init__(self):
        self._wrappers = None
        self._slash = None
        self._skill_index = None
        self._agent_index = None
        self._exec_refs = None
        self._workflow_text = None

    @property
    def wrappers(self) -> set[str]:
        if self._wrappers is None:
            try:
                self._wrappers = {p.stem for p in WRAPPER_DIR.glob("*.md")}
            except OSError:
                self._wrappers = set()
        return self._wrappers

    def _read(self, p: Path) -> str:
        try:
            return p.read_text(errors="replace")
        except OSError:
            return ""

    @property
    def slash(self) -> str:
        if self._slash is None:
            self._slash = self._read(ROOT / "SLASH_COMMANDS.md")
        return self._slash

    @property
    def skill_index(self) -> str:
        if self._skill_index is None:
            self._skill_index = self._read(ROOT / "SKILL_INDEX.md")
        return self._skill_index

    @property
    def agent_index(self) -> str:
        if self._agent_index is None:
            self._agent_index = self._read(ROOT / "AGENT_INDEX.md")
        return self._agent_index

    @property
    def workflow_text(self) -> str:
        """Concatenated workflow + wrapper sources (skill/exec references)."""
        if self._workflow_text is None:
            parts = []
            for d in (WORKFLOW_DIR, WRAPPER_DIR):
                try:
                    for p in d.glob("*.md"):
                        parts.append(self._read(p))
                except OSError:
                    pass
            self._workflow_text = "\n".join(parts)
        return self._workflow_text

    @property
    def exec_refs(self) -> str:
        """Everything that can invoke an execution script."""
        if self._exec_refs is None:
            parts = [self._read(ROOT / ".claude" / "settings.json"),
                     self._read(ROOT / "CLAUDE.md")]
            try:
                for p in LAUNCHD_DIR.glob("com.antigravity.*.plist"):
                    parts.append(self._read(p))
            except OSError:
                pass
            # skills/ + docs/solutions/ added 2026-07-28 (scar: the audit
            # orphaned weather_data.py despite 26 skill-prose invocations, and
            # nearly archived wiring_audit.py itself)
            for d in (EXEC_DIR, ROOT / "directives", ROOT / "skills",
                      ROOT / "docs" / "solutions"):
                try:
                    for p in d.rglob("*"):
                        if p.suffix in (".py", ".md") and p.is_file() \
                                and ".venv" not in p.parts:
                            parts.append(self._read(p))
                except OSError:
                    pass
            parts.append(self.workflow_text)
            self._exec_refs = "\n".join(parts)
        return self._exec_refs


# ──────────────────────────────────────────────────────────────────
# proof
# ──────────────────────────────────────────────────────────────────
def prove(key: str, c: Corpus) -> tuple[str, str]:
    """Return (status, via) for one asset key. Read-only."""
    klass, _, name = key.partition(":")

    if klass == "workflow":
        if name in c.wrappers:
            return "PROVEN", "wrapper in .claude/commands/ (menu-parity)"
        if f"/{name}" in c.slash or f"`{name}`" in c.slash:
            return "PROVEN", "listed in SLASH_COMMANDS.md"
        head = ""
        try:
            head = (WORKFLOW_DIR / f"{name}.md").read_text(errors="replace")[:400]
        except OSError:
            pass
        if "status: superseded" in head:
            return "PROVEN", "superseded — deliberate redirect"
        return "ORPHAN", "no wrapper, not in SLASH_COMMANDS.md"

    if klass == "skill":
        if name in c.skill_index:
            return "PROVEN", "listed in SKILL_INDEX.md (router-reachable)"
        if f"skills/{name}/" in c.workflow_text or f"skills/{name}\n" in c.workflow_text:
            return "PROVEN", "referenced by a workflow/wrapper"
        return "ORPHAN", "not in SKILL_INDEX.md, unreferenced by workflows"

    if klass == "agent":
        if name in c.agent_index:
            return "PROVEN", "listed in AGENT_INDEX.md"
        return "ORPHAN", "not in AGENT_INDEX.md"

    if klass == "execution":
        base = name.rsplit("/", 1)[-1]
        if base.startswith("verify_") and "/" not in name:
            # ASSERT the glob, never assume it (2026-08-08). This branch read
            # "PROVEN — run by the Sunday fleet glob" for 13 days after commit
            # 2397327cf replaced that glob with a hardcoded 2-item list naming
            # two files that do not exist. 84 verifiers were stamped PROVEN by a
            # firing path that had ceased to exist, and the auditor built to
            # catch dead assets was blind to the largest dead class in the repo.
            # An unverified claim about a firing path IS the failure mode this
            # module exists to detect — so prove it against the runner's own
            # discovery function.
            try:
                import importlib.util
                spec = importlib.util.spec_from_file_location(
                    "_vf_probe", EXEC_DIR / "verify_fleet.py")
                vf = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(vf)
                if any(p.name == base for p in vf.discover()):
                    return "PROVEN", "verify_* — confirmed in verify_fleet.discover()"
                if base == "verify_fleet.py":
                    # The runner excludes itself from its own glob by design;
                    # the probe just loaded it and executed its discovery — that
                    # IS the liveness proof for the runner itself (2026-08-08).
                    return "PROVEN", "the fleet runner itself — discovery executed by this probe"
                return "ORPHAN", "verify_* but NOT discovered by verify_fleet.discover()"
            except Exception as e:
                return "ORPHAN", f"verify_* — fleet discovery unprovable ({type(e).__name__})"
        if name.startswith("hooks/"):
            if base in c._read(ROOT / ".claude" / "settings.json"):
                return "PROVEN", "registered in .claude/settings.json"
            return "ORPHAN", "hook file not registered in .claude/settings.json"
        # count references OUTSIDE the file itself: its own name occurs once
        # per self-reference; require an occurrence in the corpus minus its
        # own source text.
        own = ""
        try:
            own = (EXEC_DIR / name).read_text(errors="replace")
        except OSError:
            pass
        refs = c.exec_refs.count(base) - own.count(base)
        if refs > 0:
            return "PROVEN", f"referenced {refs}x (hooks/launchd/scripts/workflows/directives)"
        # Python imports don't say ".py" (2026-07-28 fix — the audit was blind
        # to `import x` / `from x import` consumers)
        stem = base[:-3] if base.endswith(".py") else base
        for pat in (f"import {stem}\n", f"import {stem} ", f"from {stem} import"):
            if (c.exec_refs.count(pat) - own.count(pat)) > 0:
                return "PROVEN", f"python-imported ({pat.strip()!r})"
        return "ORPHAN", "no reference anywhere in the invocation surfaces"

    return "ORPHAN", f"unknown asset class {klass!r}"


# ──────────────────────────────────────────────────────────────────
# state
# ──────────────────────────────────────────────────────────────────
def load_index() -> dict:
    try:
        d = json.loads(INDEX.read_text())
        if isinstance(d, dict) and isinstance(d.get("assets"), dict):
            return d
    except (OSError, ValueError):
        pass
    return {"generated": None, "assets": {}}


def save_index(d: dict) -> None:
    d["generated"] = datetime.now().isoformat()
    INDEX.parent.mkdir(parents=True, exist_ok=True)
    INDEX.write_text(json.dumps(d, indent=1))


def drain(batch: int) -> dict:
    """Audit the next `batch` assets: never-checked first, then stalest."""
    inv = inventory()
    idx = load_index()
    assets = idx["assets"]
    # prune index entries whose asset left the disk (renamed/archived)
    for gone in [k for k in assets if k not in set(inv)]:
        assets.pop(gone, None)
    unchecked = [k for k in inv if k not in assets]
    stalest = sorted((k for k in inv if k in assets),
                     key=lambda k: assets[k].get("checked", ""))
    todo = (unchecked + stalest)[:max(batch, 1)]
    c = Corpus()
    now = datetime.now().isoformat()
    flips = []
    for key in todo:
        status, via = prove(key, c)
        prev = (assets.get(key) or {}).get("status")
        if prev and prev != status:
            flips.append(f"{key}: {prev} -> {status}")
        assets[key] = {"status": status, "via": via, "checked": now}
    save_index(idx)
    orphans = [k for k, v in assets.items() if v["status"] == "ORPHAN"]
    return {"audited": len(todo), "new": len([k for k in todo if k in unchecked]),
            "coverage": f"{len(assets)}/{len(inv)}",
            "orphans_total": len(orphans), "flips": flips,
            "orphans_sample": orphans[:8]}


def status() -> dict:
    inv = inventory()
    idx = load_index()
    assets = idx["assets"]
    known = [k for k in inv if k in assets]
    orphans = [k for k, v in assets.items() if v["status"] == "ORPHAN" and k in set(inv)]
    by_class: dict[str, int] = {}
    for k in orphans:
        by_class[k.split(":", 1)[0]] = by_class.get(k.split(":", 1)[0], 0) + 1
    return {"inventory": len(inv), "checked": len(known),
            "coverage_pct": round(100 * len(known) / len(inv), 1) if inv else 0.0,
            "orphans": len(orphans), "orphans_by_class": by_class,
            "generated": idx.get("generated"),
            "orphans_sample": orphans[:12]}


def check_one(path_or_key: str) -> dict:
    """Birth-wiring surface: prove a single asset right now (read-only)."""
    key = path_or_key
    if ":" not in key or "/" in key.split(":", 1)[0]:
        p = (ROOT / path_or_key) if not path_or_key.startswith("/") else Path(path_or_key)
        try:
            rel = p.resolve().relative_to(ROOT.resolve())
        except ValueError:
            return {"error": f"outside repo: {path_or_key}"}
        s = str(rel)
        if s.startswith(".agent/workflows/"):
            key = f"workflow:{p.stem}"
        elif s.startswith("skills/"):
            key = f"skill:{s.split('/')[1]}"
        elif s.startswith("agents/"):
            key = f"agent:{s.split('/')[1]}"
        elif s.startswith("execution/") and s.endswith(".py"):
            key = f"execution:{s[len('execution/'):]}"
        else:
            return {"key": s, "status": "UNTRACKED_CLASS",
                    "via": "not an audited asset class"}
    stat, via = prove(key, Corpus())
    idx = load_index()
    idx["assets"][key] = {"status": stat, "via": via,
                          "checked": datetime.now().isoformat()}
    save_index(idx)
    return {"key": key, "status": stat, "via": via}


def main() -> int:
    args = sys.argv[1:]
    mode = args[0] if args else "status"
    try:
        if mode == "drain":
            batch = DEFAULT_BATCH
            if "--batch" in args:
                batch = int(args[args.index("--batch") + 1])
            out = drain(batch)
        elif mode == "check" and len(args) > 1:
            out = check_one(args[1])
        else:
            out = status()
        print(json.dumps(out, indent=2))
    except Exception as e:  # noqa: BLE001 — audit-only; never break a caller
        print(json.dumps({"error": f"{type(e).__name__}: {e}"}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
