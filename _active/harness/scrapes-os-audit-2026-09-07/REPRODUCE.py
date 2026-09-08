#!/usr/bin/env python3
"""Replay audit probes without changing the production system.

Run using repository .venv/bin/python3 -B with PYTHONDONTWRITEBYTECODE=1.
Temporary files and in-memory handlers only; no renderer, paid provider,
installer, real patch or external action is invoked.
"""
import copy
import importlib.util
import json
import os
from pathlib import Path
import sqlite3
import tempfile

ROOT = Path("/Users/farricecain/Google Antigravity")
LANE = ROOT / ".tmp/codex-worktrees/scrapes-os-audit-20260907"

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def memory_probe():
    modules = [
        ("canonical", load("memory_main_audit", ROOT / "execution/memory_facade.py")),
        ("lane", load("memory_lane_audit", LANE / "execution/memory_facade.py")),
    ]
    result = {"override_set": bool(os.environ.get("ANTIGRAVITY_EPISODIC_PROJECTS"))}
    for label, m in modules:
        keys = m.EPISODIC_PROJECTS
        if not keys:
            result[label] = {"skipped": "Explicit all-project override; do not broaden this probe"}
            continue
        with sqlite3.connect(f"file:{m.EPISODIC_DB}?mode=ro", uri=True) as con:
            con.execute("PRAGMA query_only=ON")
            count = con.execute(
                "SELECT COUNT(*) FROM exchanges WHERE project IN (" +
                ",".join("?" for _ in keys) + ")", keys
            ).fetchone()[0]
        matches = m._query_episodic("Scrapes", 5)
        result[label] = {
            "project_keys": keys, "rows": count,
            "matches": len(matches["results"]), "degraded": matches["degraded"],
            "ids": [x.get("id") for x in matches["results"]],
        }
    lane_m = modules[1][1]
    lane_m.EPISODIC_PROJECTS = modules[0][1].EPISODIC_PROJECTS
    control = lane_m._query_episodic("Scrapes", 5)
    result["filter_only_control"] = {
        "matches": len(control["results"]),
        "ids": [x.get("id") for x in control["results"]],
    }
    return result

def readiness_probe():
    sb = load("scrapes_brand_audit", ROOT / "execution/scrapes_brand.py")
    with tempfile.TemporaryDirectory(prefix="scrapes-os-audit-", dir="/private/tmp") as td:
        t = Path(td)
        bc = t / "client/brand_context"
        (bc / "visual-identity").mkdir(parents=True)
        (bc / "voice-profile.md").write_text("")
        (bc / "visual-identity/tokens.json").write_text("{}")
        b = {
            "brand": "client", "brand_root": str(t / "client"),
            "brand_context": str(bc),
            "output_base": str(t / "unregistered-other-client/out"),
            "template_pools": {"carousel": str(bc / "templates/carousel")},
            "renderer_fallback": str(t / "missing-renderer.py"),
        }
        broken_fallback = sb.check({"client": b}, b, "carousel")
        pool = bc / "templates/carousel"
        pool.mkdir(parents=True)
        (pool / "manifest.json").write_text(json.dumps({
            "templates": [{"id": "ghost", "status": "approved"}]
        }))
        b["renderer_fallback"] = None
        ghost_template = sb.check({"client": b}, b, "carousel")
        return {"broken_fallback": broken_fallback, "ghost_template": ghost_template}

def ledger_probe():
    os.environ["LEDGER_ENFORCE"] = "0"
    sl = load("ledger_audit", ROOT / "execution/hooks/session_ledger_hook.py")
    base = sl._load("audit-nonexistent-temp-state-no-save")
    base["pending_routing"] = {
        "routing_id": "test", "suggested_dirs": ["test-expert"]
    }
    sl._is_expert_skill = lambda name: True
    sl._detect_birth_wiring = lambda path: None
    sl._reconcile_routing_feedback = (
        lambda ledger, name: ledger.update(pending_routing=None) or True
    )
    cases = [
        ("full-shell-read", "Bash", {"command": "cat skills/test-expert/SKILL.md"},
         {"stdout": "entire skill contents", "stderr": ""}),
        ("native-read", "Read", {"file_path": str(ROOT / "skills/test-expert/SKILL.md")}, {}),
        ("native-patch", "apply_patch", {"patch": "*** Begin Patch\n*** Add File: "
         "/private/tmp/proof.md\n+x\n*** End Patch"}, {}),
        ("native-write", "Write", {"file_path": "/private/tmp/proof.md"}, {}),
        ("failed-shell", "Bash", {"command": "exit 7"}, {"output": "", "exit_code": 7}),
    ]
    results = {}
    for label, tool, tool_input, response in cases:
        ledger = copy.deepcopy(base)
        saved = []
        sl._load = lambda _: ledger
        sl._save = lambda value: saved.append(copy.deepcopy(value))
        try:
            sl.handle_posttool({
                "session_id": "audit-temp", "tool_name": tool,
                "tool_input": tool_input, "tool_response": response,
            })
        except SystemExit:
            pass
        results[label] = {
            "changed": bool(saved), "full_load": ledger["manifest"]["skills_full"],
            "debts": ledger["debts"], "produced": ledger["produced"],
            "pending_routing": ledger["pending_routing"],
            "failure_streak": ledger["bash_fail_streak"],
        }
    return results

if __name__ == "__main__":
    print(json.dumps({
        "memory": memory_probe(), "readiness": readiness_probe(),
        "ledger": ledger_probe(),
    }, indent=2, default=str))
