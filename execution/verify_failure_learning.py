#!/usr/bin/env python3
"""verify_failure_learning.py — prove the anti-repeat loop learns, and only from evidence.

A learner that writes rules into a registry is a machine that edits the
system's own memory. Its value is entirely in what it REFUSES to record, so
the safety properties come first:

  1. No recurrence -> NO rule. A registry that fills with speculation is worse
     than one that sits empty, because you stop reading it.
  2. Thresholds are real. 2 failures is not CHRONIC; 3 is.
  3. One rule per failure signature. A repeat occurrence refreshes the existing
     rule's volatile lines and NEVER appends a duplicate or rewrites its prose.
  4. `--report` writes nothing.
  5. Never raises. A learner that breaks a heal is worse than no learner.

Joins the Sunday fleet via the execution/verify_*.py glob.

Usage: python3 execution/verify_failure_learning.py
Exit:  0 all pass · 1 any failure
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MOD = ROOT / "execution" / "failure_learning.py"
PY = sys.executable

FAILURES: list[str] = []
PASSES = 0
PORCELAIN_AT_START = ""


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASSES
    if ok:
        PASSES += 1
        print(f"  PASS  {label}")
    else:
        FAILURES.append(f"{label}{(' — ' + detail) if detail else ''}")
        print(f"  FAIL  {label}{(' — ' + detail) if detail else ''}")


def rows_for(fid: str, action: str, n: int, spread_days: int = 0) -> list[dict]:
    base = datetime.now() - timedelta(days=spread_days)
    step = timedelta(days=spread_days / max(n - 1, 1)) if spread_days else timedelta(seconds=1)
    return [{"ts": (base + step * i).isoformat(), "id": fid, "cls": "AUTO",
             "action": action, "note": f"synthetic {i}"} for i in range(n)]


def main() -> int:
    print("verify_failure_learning.py — anti-repeat learning contract\n")
    global PORCELAIN_AT_START
    PORCELAIN_AT_START = subprocess.run(
        ["git", "status", "--porcelain"], cwd=str(ROOT),
        capture_output=True, text=True, timeout=30).stdout

    check("module exists", MOD.exists(), str(MOD))
    if FAILURES:
        return 1
    r = subprocess.run([PY, "-m", "py_compile", str(MOD)], capture_output=True, text=True)
    check("failure_learning.py compiles", r.returncode == 0, (r.stderr or "")[:160])
    if FAILURES:
        return 1

    sys.path.insert(0, str(ROOT / "execution"))
    import failure_learning as fl  # noqa: E402

    # Redirect ALL state to a sandbox. The real log and registry are never
    # touched by this suite — see the git-cleanliness assertion at the end.
    tmp = Path(tempfile.mkdtemp(prefix="verify-fl-"))
    real = (fl.HEAL_LOG, fl.REGISTRY, fl.REPORT_CACHE, fl.LATEST, fl.PLUGIN_MIRROR)
    fl.HEAL_LOG = tmp / "self-heal.jsonl"
    fl.REGISTRY = tmp / "failure-registry.md"
    fl.REPORT_CACHE = tmp / "report.json"
    fl.LATEST = tmp / "latest.json"
    fl.PLUGIN_MIRROR = tmp / "mirror" / "failure-registry.md"  # parent absent -> no-op

    def write_log(rows: list[dict]) -> None:
        fl.HEAL_LOG.write_text("".join(json.dumps(r) + "\n" for r in rows))

    try:
        # ── 1. SAFETY: no recurrence -> no rule ────────────────────────────
        write_log(rows_for("thing", "healed", 1))
        check("a single heal records NOTHING", fl.analyse() == [],
              json.dumps(fl.analyse(), default=str)[:160])

        # ── 1b. THRESHOLDS ARE PINNED TO VALUES, not read from the module ──
        #    NC-A (2026-07-27) exposed this: the tests below derive their counts
        #    from fl.CHRONIC_FAILS, so lowering the constant to 1 moved the tests
        #    with it and the whole suite still passed while the learner had begun
        #    recording speculation. A test that reads the constant it is testing
        #    cannot detect that constant changing. Pin the values, and use
        #    HARDCODED counts below so the assertions stand independent of them.
        check("CHRONIC_FAILS is pinned at 3", fl.CHRONIC_FAILS == 3,
              f"got {fl.CHRONIC_FAILS} — lowering this makes the registry record noise")
        check("RECURRING_HEALS is pinned at 5", fl.RECURRING_HEALS == 5,
              f"got {fl.RECURRING_HEALS}")
        check("RECURRING_DAYS is pinned at 5", fl.RECURRING_DAYS == 5,
              f"got {fl.RECURRING_DAYS}")
        check("ROTTING_DAYS is pinned at 7", fl.ROTTING_DAYS == 7,
              f"got {fl.ROTTING_DAYS}")

        # Hardcoded-count probes: independent of the module's own constants.
        write_log(rows_for("hard", "heal_failed", 2))
        check("2 heal_failed records NOTHING (hardcoded, threshold-independent)",
              not any(f["kind"] == "CHRONIC" for f in fl.analyse()),
              json.dumps(fl.analyse(), default=str)[:200])
        write_log(rows_for("hard", "healed", 4, spread_days=30))
        check("4 heals over 30 days is NOT recurring (hardcoded)",
              not any(f["kind"] == "RECURRING" for f in fl.analyse()),
              json.dumps(fl.analyse(), default=str)[:200])

        # ── 2. thresholds are real, not decorative ─────────────────────────
        write_log(rows_for("bad", "heal_failed", fl.CHRONIC_FAILS - 1))
        check(f"{fl.CHRONIC_FAILS - 1} failures is NOT chronic (below threshold)",
              not any(f["kind"] == "CHRONIC" for f in fl.analyse()))
        write_log(rows_for("bad", "heal_failed", fl.CHRONIC_FAILS))
        found = fl.analyse()
        check(f"{fl.CHRONIC_FAILS} failures IS chronic",
              any(f["kind"] == "CHRONIC" and f["id"] == "bad" for f in found),
              json.dumps(found, default=str)[:200])

        # RECURRING needs BOTH a count and a time spread — repeated heals in one
        # afternoon are a retry loop, not an upstream cause.
        write_log(rows_for("churn", "healed", fl.RECURRING_HEALS, spread_days=0))
        check("many heals in one day is NOT 'recurring' (no time spread)",
              not any(f["kind"] == "RECURRING" for f in fl.analyse()))
        write_log(rows_for("churn", "healed", fl.RECURRING_HEALS,
                           spread_days=fl.RECURRING_DAYS + 1))
        check("many heals across many days IS 'recurring'",
              any(f["kind"] == "RECURRING" and f["id"] == "churn" for f in fl.analyse()))

        # ── 3. writing: rule matches the registry's documented schema ───────
        write_log(rows_for("bad", "heal_failed", fl.CHRONIC_FAILS))
        changed = fl.learn()
        text = fl.REGISTRY.read_text()
        check("a rule is written for a chronic failure",
              any(c["action"] == "recorded" for c in changed), json.dumps(changed, default=str)[:160])
        for field in ("**Added:**", "**What Happened:**", "**Root Cause:**",
                      "**Prevention Rule:**", "**Last Triggered:**", "**Status:**"):
            check(f"rule carries the schema field {field}", field in text)
        check("rule is placed after the sentinel", fl.SENTINEL in text
              and text.index(fl.SENTINEL) < text.index("### [CHRONIC]: bad"))

        # ── 4. ONE rule per signature — never duplicated on repeat ──────────
        before_n = text.count("### [CHRONIC]: bad")
        write_log(rows_for("bad", "heal_failed", fl.CHRONIC_FAILS + 4))
        fl.learn()
        text2 = fl.REGISTRY.read_text()
        check("a repeat occurrence does NOT append a second rule",
              text2.count("### [CHRONIC]: bad") == before_n == 1,
              f"{text2.count('### [CHRONIC]: bad')} copies")
        check("a repeat occurrence DOES refresh the occurrence count",
              f"**Occurrences:** {fl.CHRONIC_FAILS + 4}" in text2,
              "occurrence count not refreshed")

        # Hand-edited prose must survive the learner (the human's words win).
        edited = text2.replace("- **Prevention Rule:** ",
                               "- **Prevention Rule:** HUMAN-EDITED: ", 1)
        fl.REGISTRY.write_text(edited)
        fl.learn()
        check("hand-edited rule prose is preserved, never overwritten",
              "HUMAN-EDITED:" in fl.REGISTRY.read_text())

        # ── 5. --report writes nothing ─────────────────────────────────────
        fl.REGISTRY.unlink(missing_ok=True)
        write_log(rows_for("bad", "heal_failed", fl.CHRONIC_FAILS))
        fl.learn(dry_run=True)
        check("--report / dry_run writes no registry", not fl.REGISTRY.exists())

        # ── 6. fail-safe: a corrupt log must not raise ──────────────────────
        fl.HEAL_LOG.write_text("{ not json\n{\"id\":\"ok\",\"action\":\"healed\"}\n")
        try:
            fl.analyse()
            fl.learn()
            check("corrupt log lines are skipped, not fatal", True)
        except Exception as e:  # noqa: BLE001
            check("corrupt log lines are skipped, not fatal", False,
                  f"{type(e).__name__}: {e}")

        fl.HEAL_LOG.unlink(missing_ok=True)
        check("a missing log yields no findings and no raise", fl.analyse() == [])

        # ── 7. the mirror never becomes the canonical store ────────────────
        src = MOD.read_text()
        check("canonical registry lives in the repo, not the plugin cache",
              'REGISTRY = ROOT / "evolution_store"' in src,
              "registry is not repo-canonical")
        check("plugin mirror write is best-effort only",
              "def mirror_to_plugin" in src and "except OSError" in src)

    finally:
        fl.HEAL_LOG, fl.REGISTRY, fl.REPORT_CACHE, fl.LATEST, fl.PLUGIN_MIRROR = real
        import shutil
        shutil.rmtree(tmp, ignore_errors=True)

    # ── 8. the suite left the repo untouched ───────────────────────────────
    now = subprocess.run(["git", "status", "--porcelain"], cwd=str(ROOT),
                         capture_output=True, text=True, timeout=30).stdout
    check("verifier did not dirty the working tree", now == PORCELAIN_AT_START,
          "the suite mutated tracked state")

    print(f"\n{PASSES} passed, {len(FAILURES)} failed")
    if FAILURES:
        print("\nFAILURES:")
        for f in FAILURES:
            print(f"  - {f}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
