#!/usr/bin/env python3
"""platform_compiler.py — keep per-platform constitutions honest and in sync.

The system runs on multiple agent platforms, each reading its own constitution:
    Claude Code      -> CLAUDE.md                      (canon, hand-authored)
    Gemini surfaces  -> GEMINI.md                      (derived sibling)
    Codex            -> AGENTS.md                      (derived sibling, self-contained)
    Antigravity IDE  -> .agent/rules/constitution.md   (derived sibling, distilled)

v1 is deliberately read-only on constitutions: it detects drift and lints
invariants; it never rewrites a working file. (v2 may generate siblings from
canon + overlays.)

Commands:
    check   exit 1 if any tracked file changed since the last bless (sync)
    lint    exit 1 if any portability invariant is violated
    sync    bless current state (writes .agent/platform_hashes.json)
    forks   report known fork locations and their staleness (informational)
    report  human summary of check + lint + forks (exit 1 if check/lint fail)

Wired into evolution_orchestrator.run_daily() as an observe-only report section.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HASH_STORE = ROOT / ".agent" / "platform_hashes.json"
CONSTITUTION_CORE_DIR = ROOT / "directives" / "constitution-core"
CONSTITUTION_FILES = ["CLAUDE.md", "GEMINI.md", "AGENTS.md"]

TRACKED = [
    "CLAUDE.md",
    "GEMINI.md",
    "AGENTS.md",
    ".agent/rules/constitution.md",
    ".gemini/settings.json",
    ".codex/config.toml",
]

CANON = "CLAUDE.md"

CANARIES = {
    "GEMINI.md": "ANTIGRAVITY-GEMINI-7X4K",
    "AGENTS.md": "ANTIGRAVITY-CODEX-3J8R",
    ".agent/rules/constitution.md": "ANTIGRAVITY-IDE-9Q2M",
}

# Gemini drops early-placed constraints; CRITICAL block must sit in the
# final third of every derived constitution.
CONSTRAINTS_LAST = ["GEMINI.md", "AGENTS.md", ".agent/rules/constitution.md"]
CONSTRAINTS_MARKER = "## CRITICAL"
CONSTRAINTS_MIN_OFFSET = 0.60

GEMINI_MAX_CHARS = 15_000

# Internal paths referenced by constitutions must exist (broken pointers were
# a root cause of the failed ports).
REF_PATTERN = re.compile(
    r"`((?:directives|execution|skills|\.agent|\.gemini)/[A-Za-z0-9_\-./]+\.(?:md|py|json))`"
)

# Single-source constitution compilation (Wave 2, 2026-07-06). Shared blocks
# live once in directives/constitution-core/<block>.md; constitutions carry
# <!-- BEGIN:<block> --> ... <!-- END:<block> --> marker pairs around the
# passage they share. `compile` substitutes canonical text between markers.
# A missing marker pair in a given file is NOT an error — some platforms
# (AGENTS.md's terse style, GEMINI.md's tuned variants) legitimately keep
# their own wording for a passage and simply carry no markers for it.
BLOCK_MARKER_RE = re.compile(r"<!-- BEGIN:([A-Za-z0-9_-]+) -->(.*?)<!-- END:\1 -->", re.DOTALL)
BLOCK_HEADER_RE = re.compile(r"^<!--\s*constitution-core block:.*?-->\s*\n?", re.MULTILINE)


def _load_constitution_core_blocks() -> dict:
    blocks = {}
    if not CONSTITUTION_CORE_DIR.exists():
        return blocks
    for p in sorted(CONSTITUTION_CORE_DIR.glob("*.md")):
        text = BLOCK_HEADER_RE.sub("", p.read_text(), count=1)
        blocks[p.stem] = text.strip("\n")
    return blocks

# Active Opus pins caused "model not available" stalls. Archived agents are exempt.
OPUS_SCAN_GLOBS = [".claude/agents/**/*.md", "agents/**/AGENT.md"]
OPUS_PIN = re.compile(r"^\s*model:\s*.*opus", re.IGNORECASE)

KNOWN_FORKS = [
    Path.home() / "Codex Antigravity",
    Path.home() / ".codex" / "skills",
    Path.home() / ".gemini" / "antigravity" / "knowledge",
]


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _current_hashes() -> dict:
    out = {}
    for rel in TRACKED:
        p = ROOT / rel
        out[rel] = _sha(p) if p.exists() else "MISSING"
    return out


def cmd_sync() -> int:
    HASH_STORE.parent.mkdir(parents=True, exist_ok=True)
    HASH_STORE.write_text(json.dumps({
        "blessed_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "hashes": _current_hashes(),
    }, indent=2) + "\n")
    print(f"Blessed {len(TRACKED)} files -> {HASH_STORE.relative_to(ROOT)}")
    return 0


def cmd_check(as_json: bool = False) -> int:
    if not HASH_STORE.exists():
        result = {"drifted": [], "error": "no baseline — run: python3 execution/platform_compiler.py sync"}
        print(json.dumps(result) if as_json else result["error"])
        return 1
    blessed = json.loads(HASH_STORE.read_text())["hashes"]
    current = _current_hashes()
    drifted = [rel for rel in TRACKED if blessed.get(rel) != current.get(rel)]
    result = {"drifted": drifted, "blessed_at": json.loads(HASH_STORE.read_text()).get("blessed_at")}
    if as_json:
        print(json.dumps(result))
        return 1 if drifted else 0
    if not drifted:
        print("In sync — all platform constitutions match the blessed baseline.")
        return 0
    print("PLATFORM DRIFT — files changed since last bless:")
    for rel in drifted:
        print(f"  - {rel}")
    if CANON in drifted:
        siblings = [f for f in CONSTRAINTS_LAST if f not in drifted]
        if siblings:
            print(f"  CLAUDE.md (canon) changed but these siblings did not: {', '.join(siblings)}")
            print("  Review whether the change must propagate before blessing.")
    print("After reviewing siblings: python3 execution/platform_compiler.py sync")
    return 1


def _lint_failures() -> list:
    fails = []

    for rel in TRACKED:
        if not (ROOT / rel).exists():
            fails.append(f"missing tracked file: {rel}")

    gemini = ROOT / "GEMINI.md"
    if gemini.exists() and len(gemini.read_text()) > GEMINI_MAX_CHARS:
        fails.append(f"GEMINI.md exceeds {GEMINI_MAX_CHARS} chars (Gemini context budget)")

    for rel, token in CANARIES.items():
        p = ROOT / rel
        if p.exists() and token not in p.read_text():
            fails.append(f"canary {token} missing from {rel}")

    for rel in CONSTRAINTS_LAST:
        p = ROOT / rel
        if not p.exists():
            continue
        text = p.read_text()
        idx = text.find(CONSTRAINTS_MARKER)
        if idx == -1:
            fails.append(f"{rel}: no '{CONSTRAINTS_MARKER}' block")
        elif idx < len(text) * CONSTRAINTS_MIN_OFFSET:
            fails.append(f"{rel}: CRITICAL block sits too early ({idx}/{len(text)} chars) — constraints go LAST")

    for rel in CONSTRAINTS_LAST:
        p = ROOT / rel
        if not p.exists():
            continue
        for ref in REF_PATTERN.findall(p.read_text()):
            if not (ROOT / ref).exists():
                fails.append(f"{rel}: references missing file {ref}")

    for pattern in OPUS_SCAN_GLOBS:
        for p in ROOT.glob(pattern):
            if "_archived" in p.parts:
                continue
            try:
                head = "".join(p.read_text().splitlines(keepends=True)[:20])
            except (UnicodeDecodeError, OSError):
                continue
            for i, line in enumerate(head.splitlines(), 1):
                if OPUS_PIN.match(line):
                    fails.append(f"active Opus pin: {p.relative_to(ROOT)}:{i} — never pin opus (capacity-flaky)")

    settings = ROOT / ".claude" / "settings.json"
    if settings.exists() and "opus" in settings.read_text().lower():
        fails.append('active Opus reference in .claude/settings.json')

    # Surface budget + core-roster integrity (2026-06-12).
    # The production-core roster is capped the way the paid APIs are capped:
    # a hard ceiling that forces replacement over addition. Promotion to CORE
    # requires demoting something. Every roster id must also exist on disk —
    # a core entry pointing at nothing silently degrades routing.
    core_path = ROOT / ".agent" / "production-core.json"
    if not core_path.exists():
        fails.append("missing .agent/production-core.json (core roster)")
    else:
        try:
            core = json.loads(core_path.read_text())
            skills = core.get("skills", [])
            workflows = core.get("workflows", [])
            infra = core.get("infrastructure", [])
            budget = int(core.get("surface_budget", 45))
            roster = len(skills) + len(workflows) + len(infra)
            if roster > budget:
                fails.append(
                    f"core roster {roster} exceeds surface_budget {budget} — "
                    "promotion requires demotion (.agent/production-core.json)"
                )
            for s in skills:
                sid = s.get("id", "")
                if sid and not (ROOT / "skills" / sid).is_dir():
                    fails.append(f"production-core skill '{sid}' has no skills/{sid}/ directory")
            for w in workflows:
                wid = w.get("id", "")
                if wid and not (ROOT / ".agent" / "workflows" / f"{wid}.md").exists() \
                        and not (ROOT / "skills" / wid).is_dir():
                    fails.append(f"production-core workflow '{wid}' not found in .agent/workflows/ or skills/")
            for inf in infra:
                iid = inf.get("id", "")
                if iid and not ((ROOT / iid).exists()
                                or (ROOT / "skills" / iid).is_dir()
                                or (ROOT / ".agent" / "workflows" / f"{iid}.md").exists()):
                    fails.append(f"production-core infrastructure '{iid}' missing on disk")
        except Exception as exc:
            fails.append(f"production-core.json unreadable: {exc}")

    return fails


def cmd_lint(as_json: bool = False) -> int:
    fails = _lint_failures()
    if as_json:
        print(json.dumps({"failures": fails}))
        return 1 if fails else 0
    if not fails:
        print("Lint clean — all portability invariants hold.")
        return 0
    print(f"LINT FAILURES ({len(fails)}):")
    for f in fails:
        print(f"  - {f}")
    return 1


def cmd_compile(check: bool = False, write: bool = False) -> int:
    """Compile directives/constitution-core/ blocks into marked passages.

    --check (default if neither flag given): report-only, exit 1 on divergence.
    --write: substitute canonical text between existing marker pairs, then
    re-run the existing lint invariants (CANARIES, CONSTRAINTS_LAST, char caps)
    to confirm the write didn't break anything.
    """
    blocks = _load_constitution_core_blocks()
    if not blocks:
        print(f"No blocks in {CONSTITUTION_CORE_DIR.relative_to(ROOT)} — nothing to compile.")
        return 0

    divergent: list = []
    touched: set = set()

    for rel in CONSTITUTION_FILES:
        p = ROOT / rel
        if not p.exists():
            continue
        text = p.read_text()

        def _sub(match: "re.Match[str]", rel: str = rel) -> str:
            name = match.group(1)
            canonical = blocks.get(name)
            if canonical is None:
                return match.group(0)
            touched.add(name)
            current_inner = match.group(2)
            multiline = current_inner.startswith("\n")
            replacement_inner = f"\n{canonical}\n" if multiline else canonical
            if current_inner == replacement_inner:
                return match.group(0)
            divergent.append(f"{rel}:{name}")
            return f"<!-- BEGIN:{name} -->{replacement_inner}<!-- END:{name} -->"

        new_text = BLOCK_MARKER_RE.sub(_sub, text)
        if write and new_text != text:
            p.write_text(new_text)

    if write:
        if divergent:
            print(f"Compiled {len(divergent)} block instance(s) to canonical text:")
            for d in divergent:
                print(f"  - {d}")
        else:
            print("No divergence — marked passages already matched canonical blocks.")
        lint_fails = _lint_failures()
        if lint_fails:
            print(f"POST-COMPILE LINT FAILURES ({len(lint_fails)}):")
            for f in lint_fails:
                print(f"  - {f}")
            return 1
        print("Post-compile lint clean — CANARIES/CONSTRAINTS/char-cap invariants hold.")
        return 0

    # --check or default: report-only, never write.
    if divergent:
        print("CONSTITUTION COMPILE DIVERGENCE — marked passages differ from canonical block text:")
        for d in divergent:
            print(f"  - {d}")
        print("Review, then: python3 execution/platform_compiler.py compile --write")
        return 1
    print("compile --check clean — all marked blocks match directives/constitution-core/.")
    return 0


def cmd_forks() -> int:
    print("Known fork locations (informational — canonical system is THIS repo):")
    now = time.time()
    for fork in KNOWN_FORKS:
        if not fork.exists():
            print(f"  - {fork}: absent")
            continue
        newest = max((f.stat().st_mtime for f in fork.rglob("*") if f.is_file()), default=fork.stat().st_mtime)
        days = (now - newest) / 86_400
        flag = "  <-- ACTIVE, harvest/retire" if days < 7 else ""
        print(f"  - {fork}: newest file {days:.1f}d old{flag}")
    return 0


def cmd_report() -> int:
    print("=== platform_compiler report ===")
    rc_check = cmd_check()
    print()
    rc_lint = cmd_lint()
    print()
    cmd_forks()
    return 1 if (rc_check or rc_lint) else 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Platform constitution drift + lint")
    sub = parser.add_subparsers(dest="cmd", required=True)
    chk = sub.add_parser("check")
    chk.add_argument("--json", action="store_true")
    lnt = sub.add_parser("lint")
    lnt.add_argument("--json", action="store_true")
    sub.add_parser("sync")
    sub.add_parser("forks")
    sub.add_parser("report")
    cmp_ = sub.add_parser("compile")
    cmp_.add_argument("--check", action="store_true", help="report-only; exit 1 on divergence (default)")
    cmp_.add_argument("--write", action="store_true", help="substitute canonical block text, then re-lint")
    args = parser.parse_args()
    if args.cmd == "check":
        return cmd_check(as_json=args.json)
    if args.cmd == "lint":
        return cmd_lint(as_json=args.json)
    if args.cmd == "compile":
        return cmd_compile(check=args.check, write=args.write)
    return {"sync": cmd_sync, "forks": cmd_forks, "report": cmd_report}[args.cmd]()


if __name__ == "__main__":
    sys.exit(main())
