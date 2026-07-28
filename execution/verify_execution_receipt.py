#!/usr/bin/env python3
"""verify_execution_receipt.py — prove the execution receipt actually observes.

WHY: this verifier exists because of the failure it guards against. On
2026-07-27 a launchd health check in this same session reported "16 scripts
MISSING" — and it was wrong: the grep broke on the space in "Google
Antigravity". A check that is not itself checked manufactures false
confidence in BOTH directions, and false green is worse than no check.

So the receipt gets tested the way it will actually be used: real hook
subprocesses, real JSON payloads on stdin, real ledger files on disk, then
assert the receipt SEES what happened and FLAGS what didn't.

Joins the Sunday fleet automatically (execution/verify_*.py glob).

Usage:  python3 execution/verify_execution_receipt.py
Exit:   0 all pass · 1 any failure
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOOK = ROOT / "execution" / "hooks" / "session_ledger_hook.py"
RECEIPT = ROOT / "execution" / "execution_receipt.py"
SESSIONS = ROOT / ".agent" / "sessions"
PY = sys.executable

FAILURES: list[str] = []
PASSES = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASSES
    if ok:
        PASSES += 1
        print(f"  PASS  {label}")
    else:
        FAILURES.append(f"{label}{(' — ' + detail) if detail else ''}")
        print(f"  FAIL  {label}{(' — ' + detail) if detail else ''}")


def fire(mode: str, payload: dict) -> subprocess.CompletedProcess:
    """Run the hook exactly as Claude Code does: JSON on stdin, mode in argv."""
    return subprocess.run(
        [PY, str(HOOK), mode],
        input=json.dumps(payload), capture_output=True, text=True,
        timeout=30, cwd=str(ROOT),
    )


def ledger_path(sid: str) -> Path:
    return SESSIONS / f"ledger-{re.sub(r'[^A-Za-z0-9_-]', '_', sid)[:64]}.json"


def read_ledger(sid: str) -> dict:
    p = ledger_path(sid)
    return json.loads(p.read_text()) if p.exists() else {}


def pick_expert_skill() -> str | None:
    """A real expert skill (carries genius.md) — the hook's own definition."""
    try:
        for d in sorted((ROOT / "skills").iterdir()):
            if (d / "genius.md").exists() and (d / "SKILL.md").exists():
                return d.name
    except OSError:
        pass
    return None


def main() -> int:
    print("verify_execution_receipt.py — receipt observation contract\n")

    check("hook exists", HOOK.exists(), str(HOOK))
    check("receipt module exists", RECEIPT.exists(), str(RECEIPT))
    if FAILURES:
        return 1

    # Both files must at least compile — a syntax error here silently disables
    # the ledger for every session (the hook is fail-safe by design, so a
    # broken hook fails OPEN and quietly).
    for f in (HOOK, RECEIPT):
        r = subprocess.run([PY, "-m", "py_compile", str(f)], capture_output=True, text=True)
        check(f"{f.name} compiles", r.returncode == 0, (r.stderr or "").strip()[:160])
    if FAILURES:
        return 1

    skill = pick_expert_skill()
    check("found a real expert skill to test with", skill is not None)
    if not skill:
        return 1

    sid = "verify-receipt-selftest"
    ledger_path(sid).unlink(missing_ok=True)

    # ── 1. observation: a full SKILL.md read is recorded at Tier 1 ─────────
    fire("posttool", {"session_id": sid, "tool_name": "Read",
                      "tool_input": {"file_path": str(ROOT / "skills" / skill / "SKILL.md")}})
    led = read_ledger(sid)
    mf = led.get("manifest") or {}
    check("SKILL.md read lands in manifest.skills_full",
          skill in (mf.get("skills_full") or []), json.dumps(mf.get("skills_full"))[:120])
    check("read counter increments", int(mf.get("reads_total") or 0) == 1,
          f"got {mf.get('reads_total')}")

    # ── 2. observation: genius.md is recorded as Tier 2 DEPTH, not Tier 1 ──
    fire("posttool", {"session_id": sid, "tool_name": "Read",
                      "tool_input": {"file_path": str(ROOT / "skills" / skill / "genius.md")}})
    mf = (read_ledger(sid).get("manifest") or {})
    check("genius.md read lands in manifest.genius_read",
          skill in (mf.get("genius_read") or []))
    check("genius.md does NOT double-count as skills_full",
          (mf.get("skills_full") or []).count(skill) == 1)

    # ── 3. observation: a workflow file read is recorded ───────────────────
    wf = next(iter(sorted((ROOT / ".agent" / "workflows").glob("*.md"))), None)
    if wf:
        fire("posttool", {"session_id": sid, "tool_name": "Read",
                          "tool_input": {"file_path": str(wf)}})
        mf = (read_ledger(sid).get("manifest") or {})
        check("workflow read lands in manifest.workflows_read",
              wf.stem in (mf.get("workflows_read") or []))

    # ── 4. observation: a gate script Bash run is recorded ─────────────────
    fire("posttool", {"session_id": sid, "tool_name": "Bash",
                      "tool_input": {"command": 'python3 execution/memory_facade.py "x" --top 3'},
                      "tool_response": {"stdout": "ok", "stderr": ""}})
    mf = (read_ledger(sid).get("manifest") or {})
    check("memory_facade run lands in manifest.gates_run",
          "tier_1_5b_memory_facade" in (mf.get("gates_run") or []),
          json.dumps(mf.get("gates_run"))[:120])

    # ── 5. THE FLAG THAT MATTERS: deliverable written under the skill floor ─
    #    One skill loaded + a deliverable produced must raise UNDER FLOOR.
    sid2 = "verify-receipt-underfloor"
    ledger_path(sid2).unlink(missing_ok=True)
    fire("posttool", {"session_id": sid2, "tool_name": "Read",
                      "tool_input": {"file_path": str(ROOT / "skills" / skill / "SKILL.md")}})
    fire("posttool", {"session_id": sid2, "tool_name": "Write",
                      "tool_input": {"file_path": str(ROOT / "deliverables" / "_receipt_selftest.md")}})
    sys.path.insert(0, str(ROOT / "execution"))
    import execution_receipt  # noqa: E402

    r2 = execution_receipt.build(read_ledger(sid2))
    check("deliverable write is detected", bool(r2["deliverables"]),
          json.dumps(r2["deliverables"])[:120])
    check("UNDER FLOOR flag raised on 1 skill + deliverable",
          any("UNDER FLOOR" in f for f in r2["flags"]),
          json.dumps(r2["flags"])[:200])
    check("NO FINALIZE flag raised (finalize never ran)",
          any("NO FINALIZE" in f for f in r2["flags"]))
    check("render() produces text without raising",
          "EXECUTION RECEIPT" in execution_receipt.render(read_ledger(sid2)))

    # ── 6. NO FALSE GREEN: two skills + finalize must clear the floor flag ──
    sid3 = "verify-receipt-clean"
    ledger_path(sid3).unlink(missing_ok=True)
    others = [d.name for d in sorted((ROOT / "skills").iterdir())
              if (d / "SKILL.md").exists()][:2]
    for s in others:
        fire("posttool", {"session_id": sid3, "tool_name": "Read",
                          "tool_input": {"file_path": str(ROOT / "skills" / s / "SKILL.md")}})
    fire("posttool", {"session_id": sid3, "tool_name": "Write",
                      "tool_input": {"file_path": str(ROOT / "deliverables" / "_receipt_selftest2.md")}})
    r3 = execution_receipt.build(read_ledger(sid3))
    check("UNDER FLOOR flag NOT raised when the floor is met",
          not any("UNDER FLOOR" in f for f in r3["flags"]),
          json.dumps(r3["flags"])[:200])

    # ── 7. fail-safe: a corrupt ledger must not raise, and must not block ───
    sid4 = "verify-receipt-corrupt"
    ledger_path(sid4).write_text("{ this is not json")
    p = fire("stop", {"session_id": sid4, "stop_hook_active": False})
    check("corrupt ledger: stop hook still exits 0", p.returncode == 0,
          f"rc={p.returncode} stderr={(p.stderr or '')[:120]}")
    check("corrupt ledger: no block decision emitted",
          '"decision"' not in (p.stdout or ""), (p.stdout or "")[:160])

    # ── 8. receipt must never block, even with every flag lit ──────────────
    p = fire("stop", {"session_id": sid2, "stop_hook_active": False})
    check("flagged session: stop hook exits 0", p.returncode == 0, f"rc={p.returncode}")
    check("flagged session: receipt printed to stderr",
          "EXECUTION RECEIPT" in (p.stderr or ""), (p.stderr or "")[:200])
    check("flagged session: no block decision",
          '"decision": "block"' not in (p.stdout or ""), (p.stdout or "")[:200])

    # ── 9. de-dupe: an unchanged flag set must not reprint every turn ──────
    p2 = fire("stop", {"session_id": sid2, "stop_hook_active": False})
    check("unchanged receipt is not reprinted on the next stop",
          "EXECUTION RECEIPT" not in (p2.stderr or ""), (p2.stderr or "")[:200])

    # ── 10. CLI surface works standalone ───────────────────────────────────
    p3 = subprocess.run([PY, str(RECEIPT), sid2, "--json"],
                        capture_output=True, text=True, timeout=30, cwd=str(ROOT))
    ok_json = False
    try:
        ok_json = isinstance(json.loads(p3.stdout), dict)
    except ValueError:
        pass
    check("CLI --json emits a parseable receipt", ok_json and p3.returncode == 0,
          (p3.stderr or p3.stdout or "")[:160])

    # ── 11. legacy ledgers (written before `manifest` existed) ─────────────
    #    Must not crash — and must WITHHOLD manifest-derived flags rather than
    #    infer them from absent data (the false-RED half of the trust problem).
    sid5 = "verify-receipt-legacy"
    ledger_path(sid5).write_text(json.dumps({
        "session_id": sid5, "debts": [{"type": "skill_loaded", "name": skill, "ts": ""}],
        "produced": True,
        "produced_paths": [str(ROOT / "deliverables" / "old.md")], "subagent_spawns": 0,
    }))
    try:
        r5 = execution_receipt.build(read_ledger(sid5))
        txt5 = execution_receipt.render(read_ledger(sid5))
        check("pre-manifest ledger renders without raising", True)
        check("legacy ledger is marked not-live", r5["manifest_live"] is False)
        check("legacy ledger withholds TIER 1 ONLY (no false RED)",
              not any("TIER 1 ONLY" in f for f in r5["flags"]),
              json.dumps(r5["flags"])[:200])
        check("legacy ledger withholds NO GROUNDING (no false RED)",
              not any("NO GROUNDING" in f for f in r5["flags"]))
        check("legacy receipt says so in the text", "legacy session" in txt5)
    except Exception as e:  # noqa: BLE001
        check("pre-manifest ledger renders without raising", False, f"{type(e).__name__}: {e}")

    # ── 12. REGRESSION (bug found in the first real run) ───────────────────
    #    DELIVERABLE_ROOTS shipped without guides/ docs/ skills/ execution/,
    #    so real sessions scored zero deliverables and UNDER FLOOR never fired.
    #    Every root must be exercised, or the next omission goes unnoticed the
    #    same way. (The first commit of this test only checked guides/ and
    #    therefore could not distinguish the two candidate root causes.)
    sid6 = "verify-receipt-abspath"
    ledger_path(sid6).unlink(missing_ok=True)
    fire("posttool", {"session_id": sid6, "tool_name": "Read",
                      "tool_input": {"file_path": str(ROOT / "skills" / skill / "SKILL.md")}})
    fire("posttool", {"session_id": sid6, "tool_name": "Write",
                      "tool_input": {"file_path": str(ROOT / "guides" / "_receipt_abspath.md")}})
    r6 = execution_receipt.build(read_ledger(sid6))
    check("ABSOLUTE deliverable path is recognised (regression)",
          bool(r6["deliverables"]), json.dumps(r6["produced_paths"])[:160])
    check("UNDER FLOOR fires on an absolute-path deliverable (regression)",
          any("UNDER FLOOR" in f for f in r6["flags"]), json.dumps(r6["flags"])[:200])

    # EVERY declared root must actually resolve — this is the test that would
    # have caught the real bug. An unexercised root is an untested root.
    missed = []
    for root in execution_receipt.DELIVERABLE_ROOTS:
        probe = {"session_id": "x", "produced_paths": [str(ROOT / root / "probe.md")],
                 "debts": [], "produced": True}
        if not execution_receipt._deliverables(probe):
            missed.append(root)
    check("every DELIVERABLE_ROOT resolves to a deliverable",
          not missed, f"unresolved: {missed}")

    # Path-form robustness (separate from the root-list bug): a same-named
    # directory OUTSIDE the repo must not score as a deliverable.
    outside = {"session_id": "x", "debts": [], "produced": True,
               "produced_paths": [str(Path.home() / "Downloads" / "projects" / "notes.md")]}
    check("same-named dir outside the repo is NOT a deliverable",
          not execution_receipt._deliverables(outside),
          json.dumps(execution_receipt._deliverables(outside))[:160])

    # ── 13. scratchpad/tmp writes must NEVER count as deliverables ─────────
    sid7 = "verify-receipt-ephemeral"
    ledger_path(sid7).unlink(missing_ok=True)
    fire("posttool", {"session_id": sid7, "tool_name": "Write",
                      "tool_input": {"file_path": "/private/tmp/claude-501/x/scratchpad/note.md"}})
    r7 = execution_receipt.build(read_ledger(sid7))
    check("scratchpad write is NOT a deliverable", not r7["deliverables"],
          json.dumps(r7["deliverables"])[:160])
    check("scratchpad-only session raises no UNDER FLOOR",
          not any("UNDER FLOOR" in f for f in r7["flags"]))
    ledger_path(sid6).unlink(missing_ok=True)
    ledger_path(sid7).unlink(missing_ok=True)

    # cleanup
    for s in (sid, sid2, sid3, sid4, sid5):
        ledger_path(s).unlink(missing_ok=True)

    print(f"\n{PASSES} passed, {len(FAILURES)} failed")
    if FAILURES:
        print("\nFAILURES:")
        for f in FAILURES:
            print(f"  - {f}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
