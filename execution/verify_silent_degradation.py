#!/usr/bin/env python3
"""verify_silent_degradation — find failures wearing the costume of success.

WHAT IT HUNTS (the 2026-08-08 audit class): an `except` handler that quietly
returns a PLAUSIBLE value — "", 0, True, None, {}, [] — or is `pass`-only, so
a failure renders as health. The confirmed specimens this class produced:

    lane_state()        except -> ("", 0)    GREEN "0 commits stranded"
    corpus audit        except -> True       GREEN "v2 corpus pass"
    mission_board       fall-through         "everything live is moving"
    brief_library nav   except -> ""         page renders "OK", nav missing
                                             (reproduced DURING the fix session)

AST, NOT GREP — a docstring or comment mentioning `except Exception: return ""`
must never flag. Only real handler nodes are inspected.

QUIET-ON-PURPOSE stays quiet (Compass Doctrine — non-blocking intent is
correct; dropping the signal is the bug):
  1. `# DELIBERATE-QUIET: <reason>` on the except line or the line above.
     An EMPTY reason still flags — intent must be stated, not gestured at.
  2. execution/quiet_handlers.allow — `path:function  # reason` for
     entrypoint-level intent no single handler owns.
  3. A handler that calls degraded()/degraded_html(), raises, logs, or prints
     is already downgrading-not-dropping — not flagged.

SEVERITY: HIGH only for modules that RENDER (boards, receipts, report
writers) — a quiet hole there reaches Farrice's eyes as false health.
Everything else is INFO, reported as a count so the HIGH list stays readable
instead of becoming wallpaper.

Exit 0 always (audit-only). Named verify_* so the fleet glob runs it weekly.
--self-test proves it can fail in both directions.
"""
from __future__ import annotations

import ast
import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXEC = ROOT / "execution"
OUT = ROOT / ".agent" / "health" / "silent-degradation.json"
ALLOW = EXEC / "quiet_handlers.allow"
MARKER = "DELIBERATE-QUIET:"

# Modules whose output reaches Farrice's eyes — a quiet hole here is false health.
HIGH_RISK = {
    "pulse_dashboard.py", "mission_board.py", "oracle_dashboard.py",
    "asset_gallery.py", "brief_library.py", "render_brief.py", "mdview.py",
    "execution_receipt.py", "front_door.py", "mission_brief.py",
    "signal_scout.py", "session_closeout_intelligence.py", "cos_prep.py",
    "end_session_closeout.py", "homework_binder.py", "lane_reconciler.py",
}

# A handler that CALLS one of these is downgrading, not dropping.
SIGNAL_CALLS = {"degraded", "degraded_html", "print", "warning", "error",
                "exception", "info", "debug", "log", "_record", "append"}

_PLAUSIBLE = {"", 0, 0.0, True, None}


def _is_plausible_const(node) -> bool:
    if isinstance(node, ast.Constant):
        return node.value in _PLAUSIBLE
    if isinstance(node, (ast.Dict, ast.List, ast.Set)):
        return not getattr(node, "keys", getattr(node, "elts", [])) or not node.elts \
            if hasattr(node, "elts") else not node.keys
    if isinstance(node, ast.Tuple):
        return all(_is_plausible_const(e) for e in node.elts)
    return False


def _handler_signals(h: ast.ExceptHandler) -> bool:
    for n in ast.walk(h):
        if isinstance(n, (ast.Raise,)):
            return True
        if isinstance(n, ast.Call):
            name = ""
            if isinstance(n.func, ast.Name):
                name = n.func.id
            elif isinstance(n.func, ast.Attribute):
                name = n.func.attr
            if name in SIGNAL_CALLS:
                return True
    return False


def _marked(lines: list[str], lineno: int) -> tuple[bool, bool]:
    """-> (has_marker, marker_has_reason). Checks the except line and the line above."""
    for ln in (lineno - 1, lineno - 2):
        if 0 <= ln < len(lines) and MARKER in lines[ln]:
            reason = lines[ln].split(MARKER, 1)[1].strip()
            return True, bool(reason)
    return False, False


def _load_allow() -> set[str]:
    entries = set()
    if ALLOW.exists():
        for line in ALLOW.read_text().splitlines():
            line = line.split("#", 1)[0].strip()
            if line:
                entries.add(line)
    return entries


def _enclosing_function(tree: ast.AST, lineno: int) -> str:
    best = ""
    for n in ast.walk(tree):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if n.lineno <= lineno <= (n.end_lineno or n.lineno):
                best = n.name  # innermost wins on repeated matches
    return best or "<module>"


def scan_file(path: Path, allow: set[str]) -> list[dict]:
    import warnings
    try:
        src = path.read_text(encoding="utf-8", errors="replace")
        with warnings.catch_warnings():
            # scanned files' own SyntaxWarnings (bad escapes etc.) are their
            # problem, not this report's noise
            warnings.simplefilter("ignore", SyntaxWarning)
            tree = ast.parse(src)
    except (OSError, SyntaxError):
        return []  # DELIBERATE-QUIET: unparseable file is not a quiet HANDLER finding; other verifiers own syntax health
    lines = src.splitlines()
    findings = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.ExceptHandler):
            continue
        body = node.body
        pass_only = all(isinstance(s, ast.Pass) for s in body)
        quiet_return = (len(body) == 1 and isinstance(body[0], ast.Return)
                        and body[0].value is not None
                        and _is_plausible_const(body[0].value))
        if not (pass_only or quiet_return):
            continue
        if _handler_signals(node):
            continue
        has_marker, has_reason = _marked(lines, node.lineno)
        if has_marker and has_reason:
            continue
        func = _enclosing_function(tree, node.lineno)
        if f"{path.name}:{func}" in allow:
            continue
        findings.append({
            "file": path.name, "function": func, "line": node.lineno,
            "shape": "pass-only" if pass_only else "quiet-return",
            "severity": "HIGH" if path.name in HIGH_RISK else "INFO",
            "marker_empty": has_marker and not has_reason,
        })
    return findings


def run() -> dict:
    allow = _load_allow()
    findings = []
    for p in sorted(EXEC.glob("*.py")):
        findings.extend(scan_file(p, allow))
    high = [f for f in findings if f["severity"] == "HIGH"]
    report = {
        "ts": datetime.now().isoformat(timespec="seconds"),
        "high": high,
        "info_count": len(findings) - len(high),
        "total": len(findings),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2))
    return report


def self_test() -> int:
    import tempfile
    ok, bad = 0, []

    def check(name, cond):
        nonlocal ok
        ok += 1 if cond else 0
        if not cond:
            bad.append(name)

    with tempfile.TemporaryDirectory() as td:
        f = Path(td) / "fixture.py"
        # 1 must-flag: quiet plausible return
        f.write_text("def a():\n    try:\n        x()\n    except OSError:\n        return ''\n")
        check("quiet return '' flags", len(scan_file(f, set())) == 1)
        # 2 must-flag: pass-only
        f.write_text("def a():\n    try:\n        x()\n    except Exception:\n        pass\n")
        check("pass-only flags", len(scan_file(f, set())) == 1)
        # 3 must-NOT-flag: same text inside a docstring (AST != grep)
        f.write_text('def a():\n    """except Exception: return \'\' — docs only."""\n    return 1\n')
        check("docstring text does NOT flag", len(scan_file(f, set())) == 0)
        # 4 must-NOT-flag: handler that signals
        f.write_text("def a():\n    try:\n        x()\n    except OSError as e:\n        return degraded('', 'why', e)\n")
        check("degraded() call silences", len(scan_file(f, set())) == 0)
        # 5 marker with reason silences
        f.write_text("def a():\n    try:\n        x()\n    # DELIBERATE-QUIET: probe cache, absence is normal\n    except OSError:\n        return ''\n")
        check("marker with reason silences", len(scan_file(f, set())) == 0)
        # 6 marker with EMPTY reason still flags
        f.write_text("def a():\n    try:\n        x()\n    # DELIBERATE-QUIET:\n    except OSError:\n        return ''\n")
        r = scan_file(f, set())
        check("empty-reason marker still flags", len(r) == 1 and r[0]["marker_empty"])
        # 7 allowlist silences by file:function
        f.write_text("def myfn():\n    try:\n        x()\n    except OSError:\n        return ''\n")
        check("allowlist silences", len(scan_file(f, {"fixture.py:myfn"})) == 0)
        # 8 false-red control: a loud handler must not flag
        f.write_text("def a():\n    try:\n        x()\n    except OSError:\n        raise\n")
        check("raise does not flag", len(scan_file(f, set())) == 0)

    print(f"verify_silent_degradation self-test: {'OK' if not bad else 'FAILED'} "
          f"({ok} passed, {len(bad)} failed)")
    for b in bad:
        print(f"  FAIL: {b}")
    return 0 if not bad else 1


def main() -> int:
    if "--self-test" in sys.argv:
        return self_test()
    r = run()
    print(f"SILENT DEGRADATION: {len(r['high'])} HIGH · {r['info_count']} info "
          f"(full list: {OUT})")
    for f in r["high"][:15]:
        tag = " [marker has no reason]" if f.get("marker_empty") else ""
        print(f"  HIGH {f['file']}:{f['line']} {f['function']}() — {f['shape']}{tag}")
    if len(r["high"]) > 15:
        print(f"  … +{len(r['high']) - 15} more")
    # self-test result decides the exit code so the fleet sees a real failure
    # when the detector itself breaks; findings alone never block (audit-only).
    return self_test() if "--strict" in sys.argv else 0


if __name__ == "__main__":
    sys.exit(main())
