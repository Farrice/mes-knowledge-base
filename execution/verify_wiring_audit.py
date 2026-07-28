#!/usr/bin/env python3
"""verify_wiring_audit.py — Tier 3 wiring ratchet (wiring_audit.py).

Fake-tree tests: every behavioral check builds a temp repo, patches the
module's path constants, and exercises inventory → prove → drain → prune.
Pinned expectations are HARDCODED (never read from the module under test,
2026-07-27 card: a test that reads the constant it tests cannot detect that
constant changing). Read-only guarantee is enforced by AST, not by trust.

Exit: 0 all pass, 1 any fail (Sunday fleet counts nonzero exits).
"""

import ast
import json
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "execution"))
import wiring_audit as wa  # noqa: E402

PIN_DEFAULT_BATCH = 150
PIN_STATUSES = {"PROVEN", "ORPHAN"}

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


def build_tree(td: Path):
    (td / ".agent" / "workflows").mkdir(parents=True)
    (td / ".agent" / "health").mkdir(parents=True)
    (td / ".claude" / "commands").mkdir(parents=True)
    (td / "skills" / "wired-skill").mkdir(parents=True)
    (td / "skills" / "orphan-skill").mkdir(parents=True)
    (td / "agents" / "wired-agent").mkdir(parents=True)
    (td / "execution" / "hooks").mkdir(parents=True)
    (td / "execution" / "_archived_verifiers").mkdir(parents=True)
    (td / "directives").mkdir(parents=True)

    (td / ".agent" / "workflows" / "wired-wf.md").write_text("# wf")
    (td / ".claude" / "commands" / "wired-wf.md").write_text("wrapper")
    (td / ".agent" / "workflows" / "orphan-wf.md").write_text("# wf")
    (td / ".agent" / "workflows" / "old-wf.md").write_text(
        "---\nstatus: superseded\nsuperseded_by: wired-wf\n---\n")
    (td / "SLASH_COMMANDS.md").write_text("| /wired-wf | x |\n")

    (td / "skills" / "wired-skill" / "SKILL.md").write_text("# s")
    (td / "skills" / "orphan-skill" / "SKILL.md").write_text("# s")
    (td / "SKILL_INDEX.md").write_text("wired-skill\n")

    (td / "agents" / "wired-agent" / "AGENT.md").write_text("# a")
    (td / "AGENT_INDEX.md").write_text("wired-agent\n")

    (td / "execution" / "wired_script.py").write_text("# referenced\n")
    (td / "execution" / "orphan_script.py").write_text("# unreferenced\n")
    (td / "execution" / "verify_something.py").write_text("# fleet-run\n")
    (td / "execution" / "hooks" / "wired_hook.py").write_text("# hook\n")
    (td / "execution" / "hooks" / "orphan_hook.py").write_text("# hook\n")
    (td / "execution" / "_archived_verifiers" / "verify_dead.py").write_text("#\n")
    (td / ".claude" / "settings.json").write_text(json.dumps({
        "hooks": {"UserPromptSubmit": [{"hooks": [
            {"command": "python3 execution/hooks/wired_hook.py"}]}]}}))
    (td / "directives" / "ref.md").write_text("run python3 execution/wired_script.py\n")
    (td / "CLAUDE.md").write_text("# root\n")


PATCH_ATTRS = ("ROOT", "INDEX", "WRAPPER_DIR", "WORKFLOW_DIR", "SKILLS_DIR",
               "AGENTS_DIR", "EXEC_DIR", "LAUNCHD_DIR")


def patched(td: Path) -> dict:
    saved = {a: getattr(wa, a) for a in PATCH_ATTRS}
    wa.ROOT = td
    wa.INDEX = td / ".agent" / "health" / "wiring-index.json"
    wa.WRAPPER_DIR = td / ".claude" / "commands"
    wa.WORKFLOW_DIR = td / ".agent" / "workflows"
    wa.SKILLS_DIR = td / "skills"
    wa.AGENTS_DIR = td / "agents"
    wa.EXEC_DIR = td / "execution"
    wa.LAUNCHD_DIR = td / "empty-launchd"
    return saved


def unpatch(saved: dict):
    for k, v in saved.items():
        setattr(wa, k, v)


def main():
    check("pin_default_batch", wa.DEFAULT_BATCH == PIN_DEFAULT_BATCH,
          f"module says {wa.DEFAULT_BATCH}")

    with tempfile.TemporaryDirectory() as tds:
        td = Path(tds)
        build_tree(td)
        saved = patched(td)
        try:
            inv = wa.inventory()
            check("inventory_counts",
                  len([k for k in inv if k.startswith("workflow:")]) == 3
                  and len([k for k in inv if k.startswith("skill:")]) == 2
                  and len([k for k in inv if k.startswith("agent:")]) == 1,
                  str(inv))
            check("inventory_excludes_archived",
                  not any("_archived" in k for k in inv), str(inv))

            out = wa.drain(999)
            idx = json.loads(wa.INDEX.read_text())
            a = idx["assets"]
            def st(k):
                return (a.get(k) or {}).get("status")

            check("workflow_wrapper_proven", st("workflow:wired-wf") == "PROVEN")
            check("workflow_orphan_caught", st("workflow:orphan-wf") == "ORPHAN")
            check("workflow_superseded_proven", st("workflow:old-wf") == "PROVEN")
            check("skill_indexed_proven", st("skill:wired-skill") == "PROVEN")
            check("skill_orphan_caught", st("skill:orphan-skill") == "ORPHAN")
            check("agent_indexed_proven", st("agent:wired-agent") == "PROVEN")
            check("exec_referenced_proven", st("execution:wired_script.py") == "PROVEN")
            check("exec_orphan_caught", st("execution:orphan_script.py") == "ORPHAN")
            check("verify_class_proven", st("execution:verify_something.py") == "PROVEN")
            check("hook_registered_proven",
                  st("execution:hooks/wired_hook.py") == "PROVEN")
            check("hook_unregistered_orphan",
                  st("execution:hooks/orphan_hook.py") == "ORPHAN")
            check("statuses_closed_set",
                  all(v["status"] in PIN_STATUSES for v in a.values()))
            check("drain_reports_orphans", out["orphans_total"] == 4, str(out))

            # wiring the orphan flips it on re-check (ratchet moves forward)
            (td / ".claude" / "commands" / "orphan-wf.md").write_text("wrapper")
            one = wa.check_one(".agent/workflows/orphan-wf.md")
            check("check_one_flips_to_proven", one["status"] == "PROVEN", str(one))

            # deleting an asset prunes it from the index on next drain
            (td / ".agent" / "workflows" / "orphan-wf.md").unlink()
            (td / ".claude" / "commands" / "orphan-wf.md").unlink()
            wa.drain(999)
            idx2 = json.loads(wa.INDEX.read_text())
            check("index_prunes_deleted_assets",
                  "workflow:orphan-wf" not in idx2["assets"])

            s = wa.status()
            check("status_shape",
                  {"inventory", "checked", "coverage_pct", "orphans"} <= set(s))
        finally:
            unpatch(saved)

    # ── read-only guarantee: no deletion/mutation APIs in the module ─────
    tree = ast.parse((REPO_ROOT / "execution" / "wiring_audit.py").read_text())
    banned = {"unlink", "rmdir", "remove", "rmtree", "rename", "replace",
              "write_text", "write_bytes", "open"}
    offenders = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = ""
            if isinstance(node.func, ast.Attribute):
                name = node.func.attr
            elif isinstance(node.func, ast.Name):
                name = node.func.id
            if name in banned:
                offenders.append(f"{name}@L{node.lineno}")
    # The ONLY writes allowed are the index save + reads. Pin them explicitly:
    allowed = {o for o in offenders if o.startswith(("write_text", "open"))}
    check("ast_only_index_writes",
          all(o.startswith("write_text") for o in offenders) and len(offenders) <= 1,
          f"calls found: {offenders}")
    check("ast_no_subprocess",
          not any(isinstance(n, (ast.Import, ast.ImportFrom))
                  and any("subprocess" in getattr(a, "name", "") or
                          (getattr(n, "module", "") or "") == "subprocess"
                          for a in getattr(n, "names", []))
                  for n in ast.walk(tree)))

    print(f"\n{PASS} pass / {FAIL} fail")
    sys.exit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
