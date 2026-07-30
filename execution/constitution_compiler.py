#!/usr/bin/env python3
"""
constitution_compiler.py — one source, two constitutions (apex W3, 2026-07-29).

CLAUDE.md and AGENTS.md drifted into contradicting each other on the system's
basic posture (amnesty audit: three different blocker counts, two question
doctrines, three steering skip-lists, drifted ban subsets). Hand-sync always
drifts; this module makes the shared sections GENERATED, using the repo's
proven marker-injection pattern (slop-ban block, COUNTS, menu-parity shims).

Source of truth: directives/constitution/shared-blocks.md
Targets: CLAUDE.md, AGENTS.md — each carries
    <!-- BEGIN:shared-<name> --> ... <!-- END:shared-<name> -->
markers; sync replaces the interior verbatim. Content OUTSIDE markers stays
per-harness (that asymmetry is deliberate — Codex needs self-contained text).

Usage:
  python3 execution/constitution_compiler.py sync     # render source into both targets
  python3 execution/constitution_compiler.py check    # exit 1 + diff summary on drift
Wired into verify_codex_claude_parity.py (check mode) — drift fails the fleet.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "directives" / "constitution" / "shared-blocks.md"
TARGETS = [ROOT / "CLAUDE.md", ROOT / "AGENTS.md"]

MARK = re.compile(
    r"<!-- BEGIN:(shared-[a-z0-9-]+) -->\n(.*?)\n<!-- END:\1 -->", re.DOTALL)


def load_blocks() -> dict:
    text = SOURCE.read_text()
    return {name: body for name, body in MARK.findall(text)}


def render(target: Path, blocks: dict, write: bool):
    """Returns list of (block, status) for this target."""
    text = target.read_text()
    results = []

    def _sub(m):
        name = m.group(1)
        if name not in blocks:
            results.append((name, "UNKNOWN-BLOCK (not in source)"))
            return m.group(0)
        if m.group(2) == blocks[name]:
            results.append((name, "in-sync"))
            return m.group(0)
        results.append((name, "DRIFTED" if not write else "synced"))
        return f"<!-- BEGIN:{name} -->\n{blocks[name]}\n<!-- END:{name} -->"

    new = MARK.sub(_sub, text)
    present = {r[0] for r in results}
    for name in blocks:
        if name not in present:
            results.append((name, f"MISSING markers in {target.name}"))
    if write and new != text:
        target.write_text(new)
    return results


def main() -> int:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    write = cmd == "sync"
    blocks = load_blocks()
    if not blocks:
        print(f"ERROR: no shared blocks found in {SOURCE}")
        return 1
    drift = 0
    for t in TARGETS:
        for name, status in render(t, blocks, write):
            if status not in ("in-sync", "synced"):
                drift += 1
            if status != "in-sync" or cmd == "status":
                print(f"  {t.name}: {name} — {status}")
    if cmd == "check" and drift:
        print(f"CONSTITUTION DRIFT: {drift} block(s) out of sync — "
              "run `python3 execution/constitution_compiler.py sync` "
              "(edit shared-blocks.md, never the rendered copies)")
        return 1
    if cmd == "sync":
        print(f"sync complete — {len(blocks)} block(s) across {len(TARGETS)} targets")
    elif not drift:
        print("constitution in sync")
    return 0


if __name__ == "__main__":
    sys.exit(main())
