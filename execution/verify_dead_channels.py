#!/usr/bin/env python3
"""verify_dead_channels.py — the dead-channel detectors in self_heal.py
(dead_hooks, dead_launchd, stale_feeds, core_surface_bypass, wiring_orphans).

Fake-tree tests with patched module constants; pinned thresholds hardcoded
here (never read back from the module — 2026-07-27 card); structural
guarantees via AST. Exit 0 all pass, 1 any fail.
"""

import ast
import json
import os
import plistlib
import sys
import tempfile
import time
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "execution"))
import self_heal as sh  # noqa: E402

# ── PINNED thresholds (the module must match these exactly) ──────────────
PIN_CORE_MIN = 3
PIN_CORE_WINDOW = 7
PIN_DETECTORS = {"dead_hooks", "dead_launchd", "stale_feeds",
                 "core_surface_bypass", "wiring_orphans"}

PASS = 0
FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"  ok  {name}")
    else:
        FAIL += 1
        print(f"FAIL  {name}" + (f" — {detail}" if detail else ""))


def age_file(p: Path, days: float):
    t = time.time() - days * 86400
    os.utime(p, (t, t))


def main():
    check("pin_core_min_sessions", sh.CORE_BYPASS_MIN_SESSIONS == PIN_CORE_MIN)
    check("pin_core_window_days", sh.CORE_BYPASS_WINDOW_DAYS == PIN_CORE_WINDOW)

    saved = {"ROOT": sh.ROOT, "LAUNCHD_DIR": sh.LAUNCHD_DIR,
             "HOOK_EVIDENCE": sh.HOOK_EVIDENCE,
             "HOOK_UNOBSERVABLE": sh.HOOK_UNOBSERVABLE,
             "FEED_FRESHNESS": sh.FEED_FRESHNESS,
             "_launchd_loaded_labels": sh._launchd_loaded_labels}
    try:
        with tempfile.TemporaryDirectory() as tds:
            td = Path(tds)
            run_tree_checks(td)
    finally:
        for k, v in saved.items():
            setattr(sh, k, v)

    run_ast_checks()
    print(f"\n{PASS} pass / {FAIL} fail")
    sys.exit(1 if FAIL else 0)


def run_tree_checks(td: Path):
    (td / ".claude").mkdir()
    (td / ".agent" / "sessions").mkdir(parents=True)
    (td / ".agent" / "health").mkdir(parents=True)
    sh.ROOT = td

    # ── dead_hooks ───────────────────────────────────────────────────────
    (td / ".claude" / "settings.json").write_text(json.dumps({"hooks": {
        "UserPromptSubmit": [{"hooks": [
            {"command": 'python3 "$D/execution/hooks/fresh_hook.py"'},
            {"command": 'python3 "$D/execution/hooks/stale_hook.py"'},
            {"command": 'python3 "$D/execution/hooks/exempt_hook.py"'},
            {"command": 'python3 "$D/execution/hooks/mystery_hook.py"'}]}]}}))
    fresh = td / ".agent" / "fresh.json"
    fresh.write_text("{}")
    stale = td / ".agent" / "stale.json"
    stale.write_text("{}")
    age_file(stale, 12)
    sh.HOOK_EVIDENCE = {"fresh_hook.py": (".agent/fresh.json", 7),
                        "stale_hook.py": (".agent/stale.json", 7),
                        "missing_hook.py": (".agent/never.json", 7)}
    sh.HOOK_UNOBSERVABLE = {"exempt_hook.py": "print-only"}

    f = sh.detect_dead_hooks()
    check("dead_hooks_fires", f is not None and f["cls"] == "JUDGMENT")
    d = (f or {}).get("detail", {})
    check("dead_hooks_stale_named",
          any("stale_hook.py" in p for p in d.get("problems", [])), str(d))
    check("dead_hooks_fresh_clean",
          not any("fresh_hook.py" in p for p in d.get("problems", [])))
    check("dead_hooks_unmapped_named", "mystery_hook.py" in d.get("unmapped", []))
    check("dead_hooks_exempt_skipped",
          "exempt_hook.py" not in d.get("unmapped", [])
          and not any("exempt_hook.py" in p for p in d.get("problems", [])))

    # all mapped + fresh -> clean
    sh.HOOK_EVIDENCE = {"fresh_hook.py": (".agent/fresh.json", 7)}
    sh.HOOK_UNOBSERVABLE = {"stale_hook.py": "x", "exempt_hook.py": "x",
                            "mystery_hook.py": "x"}
    check("dead_hooks_clean_when_fresh", sh.detect_dead_hooks() is None)

    # ── dead_launchd ─────────────────────────────────────────────────────
    ld = td / "launchd"
    ld.mkdir()
    sh.LAUNCHD_DIR = ld

    def plist(label, log=None, weekly=False, age_days=None):
        d = {"Label": label, "ProgramArguments": ["x"]}
        if log:
            d["StandardOutPath"] = str(log)
        if weekly:
            d["StartCalendarInterval"] = {"Weekday": 0, "Hour": 6}
        else:
            d["StartCalendarInterval"] = {"Hour": 6}
        p = ld / f"{label}.plist"
        p.write_bytes(plistlib.dumps(d))
        if age_days is not None:
            age_file(p, age_days)
        return p

    log_ok = td / "ok.log"
    log_ok.write_text("x")
    log_old = td / "old.log"
    log_old.write_text("x")
    age_file(log_old, 8)
    plist("com.antigravity.good", log=log_ok, age_days=30)
    plist("com.antigravity.stale-log", log=log_old, age_days=30)
    plist("com.antigravity.unloaded", log=log_ok, age_days=30)
    plist("com.antigravity.brand-new", log=td / "never.log", age_days=0.1)
    sh._launchd_loaded_labels = lambda: {"com.antigravity.good",
                                         "com.antigravity.stale-log",
                                         "com.antigravity.brand-new"}
    f = sh.detect_dead_launchd()
    d = (f or {}).get("detail", {})
    check("launchd_fires", f is not None)
    check("launchd_unloaded_named", "com.antigravity.unloaded" in d.get("not_loaded", []))
    check("launchd_stale_log_named",
          any("stale-log" in s for s in d.get("stale", [])), str(d))
    check("launchd_good_clean",
          not any("com.antigravity.good" in s for s in d.get("stale", [])))
    check("launchd_grace_period_for_new_plist",
          not any("brand-new" in s for s in d.get("stale", [])), str(d))

    # ── stale_feeds ──────────────────────────────────────────────────────
    ok_feed = td / "feed-ok.json"
    ok_feed.write_text("{}")
    old_feed = td / "feed-old.json"
    old_feed.write_text("{}")
    age_file(old_feed, 10)
    exists_only = td / "registry.md"
    exists_only.write_text("#")
    age_file(exists_only, 400)
    sh.FEED_FRESHNESS = {"feed-ok.json": ("p1", 5), "feed-old.json": ("p2", 5),
                         "feed-missing.json": ("p3", 5),
                         "registry.md": ("p4", None)}
    f = sh.detect_stale_feeds()
    d = (f or {}).get("detail", {})
    check("feeds_fires", f is not None)
    check("feeds_stale_and_missing_named",
          any("feed-old.json" in s for s in d.get("stale", []))
          and any("feed-missing.json" in s for s in d.get("stale", [])), str(d))
    check("feeds_exists_only_never_stale",
          not any("registry.md" in s for s in d.get("stale", [])))

    # ── core_surface_bypass ──────────────────────────────────────────────
    def ledger(n, content_paths, loads, age=1, manifest=True):
        d = {"session_id": f"sess-{n}", "produced_paths": content_paths}
        if manifest:
            d["manifest"] = {"skills_full": ["x"] * loads, "skill_tool_calls": []}
        p = td / ".agent" / "sessions" / f"ledger-{n}.json"
        p.write_text(json.dumps(d))
        age_file(p, age)

    for i in range(3):
        ledger(f"bypass{i}", ["deliverables/post.md"], 0)
    ledger("loaded", ["deliverables/x.md"], 2)
    ledger("system", ["execution/tool.py"], 0)
    ledger("legacy", ["deliverables/y.md"], 0, manifest=False)
    ledger("old", ["deliverables/z.md"], 0, age=20)
    f = sh.detect_core_surface_bypass()
    check("core_bypass_fires_at_3", f is not None and "3 session(s)" in f["what"],
          str(f))

    # below the pinned threshold -> silent
    (td / ".agent" / "sessions" / "ledger-bypass2.json").unlink()
    check("core_bypass_silent_at_2", sh.detect_core_surface_bypass() is None)

    # ── wiring_orphans ───────────────────────────────────────────────────
    widx = td / ".agent" / "health" / "wiring-index.json"
    widx.write_text(json.dumps({"assets": {
        "execution:orphan_a.py": {"status": "ORPHAN", "via": "x"},
        "workflow:fine": {"status": "PROVEN", "via": "y"}}}))
    f = sh.detect_wiring_orphans()
    check("wiring_orphans_fires", f is not None and "1 asset(s)" in f["what"], str(f))
    widx.write_text(json.dumps({"assets": {
        "workflow:fine": {"status": "PROVEN", "via": "y"}}}))
    check("wiring_orphans_clean", sh.detect_wiring_orphans() is None)
    widx.unlink()
    check("wiring_orphans_silent_before_first_drain",
          sh.detect_wiring_orphans() is None)


def run_ast_checks():
    src = (REPO_ROOT / "execution" / "self_heal.py").read_text()
    tree = ast.parse(src)

    # CLASSIFIERS must contain all five; HEALERS must contain none of them —
    # the classify-only guarantee, asserted structurally.
    classifiers, healers = set(), set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and node.targets \
                and isinstance(node.targets[0], ast.Name):
            tgt = node.targets[0].id
            if tgt in ("CLASSIFIERS", "HEALERS") and isinstance(node.value, ast.Dict):
                keys = {k.value for k in node.value.keys
                        if isinstance(k, ast.Constant)}
                if tgt == "CLASSIFIERS":
                    classifiers = keys
                else:
                    healers = keys
    check("ast_all_detectors_registered", PIN_DETECTORS <= classifiers,
          f"missing: {PIN_DETECTORS - classifiers}")
    check("ast_detectors_never_healers", not (PIN_DETECTORS & healers),
          f"classify-only violated: {PIN_DETECTORS & healers}")


if __name__ == "__main__":
    main()
