#!/usr/bin/env python3
"""Verify the Google Antigravity operator-core back-port."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = Path.home() / ".codex" / "config.toml"
HOOKS_PATH = ROOT / ".codex" / "hooks.json"

HOT_ROUTES = [
    "mission",
    "source-to-skill-system",
    "orchestrate",
    "repeatability-spine",
    "knowledge-librarian",
    "expert-composition-governor",
    "extraction-governor-agent",
    "steering-compass",
    "system-audit",
]

PROBES = [
    ("I need mission control for this repair", "mission"),
    ("source to skill system reusable operating layer", "source-to-skill-system"),
    ("Codex hooks are not firing", "system-audit"),
    ("Codex is failing across split workspaces with global/workspace drift and not-firing hooks", "system-audit"),
    ("Codex explains and plans instead of executing safe local next actions", "system-audit"),
    ("execution bias repair with parallel agents", "system-audit"),
    ("Why do I have to be so deterministic with you in Codex compared to Claude Code?", "system-audit"),
    ("The pre-flight things did not kick in and I had to iterate 5 to 6 times.", "system-audit"),
    ("Codex is blocking hooks and routing wrong defaults; match Claude Code without breaking my workspace", "system-audit"),
    ("Can you do a full audit or check and repair on things that are not wired or should not be wired together and are the default settings? source-command-steering-compass source-command-convene", "system-audit"),
    ("See, this whole selective language being linked to stuff is nonsense. I feel like it's what's causing issues. What's going on here?!", "system-audit"),
    ("Please implement this Codex routing/wiring parity repair plan with no-log route probes, hook verification, and a previous session caliber regression case.", "system-audit"),
    ("so what was done here? from the looks nothing was fixed that I wanted", "system-audit"),
    ("I copied over everything from my Claude Code workspace and nothing works at the same caliber; import from my previous session shows the massive difference.", "repeatability-spine"),
    ("This final output is the standard and floor. Preserve this.", "repeatability-spine"),
    ("Create production-ready paid ad scripts for a recruiter and founder with no AI slop.", "high-taste-writing-os"),
    ("Run the high-taste plus copy-engine route, load the PDP and prior brief, then write only production-ready scripts that pass the copy gate.", "high-taste-writing-os"),
    ("The wording is not routing even when it is obvious.", "system-audit"),
    ("The hooks still sound generic and scientific, stating facts rather than appealing to human psychology and copywriting. Use the research word banks and customer avatar language.", "high-taste-writing-os"),
    ("I think this final version got worse again with the script.", "repeatability-spine"),
    ("The script is just an explanation, like notes and not actually copywriting.", "repeatability-spine"),
    ("We apply one fix and then something else breaks.", "repeatability-spine"),
    ("I give up. Codex is not working in my workspace, the brief gets worse and worse, and this is now a context issue and not usable.", "system-audit"),
    ("Write paid-ad voiceover that is recordable as-is and not strategy notes.", "high-taste-writing-os"),
    ("give me better 3 next prompts and an operator lesson", "steering-compass"),
    ("full arsenal too many experts not interwoven", "expert-composition-governor"),
]

HOOK_STATE_SUFFIXES = [
    "pre_tool_use:0:0",
    "pre_tool_use:0:1",
    "post_tool_use:0:0",
    "user_prompt_submit:0:0",
    "user_prompt_submit:0:1",
    "stop:0:0",
]


def run(args: list[str], input_text: str | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True, input=input_text)


def fail(message: str) -> None:
    raise AssertionError(message)


def check_file(path: Path, label: str) -> None:
    if not path.exists():
        fail(f"Missing {label}: {path.relative_to(ROOT)}")
    if path.stat().st_size == 0:
        fail(f"Empty {label}: {path.relative_to(ROOT)}")


def first_route(router_stdout: str) -> str:
    for line in router_stdout.splitlines():
        match = re.match(r"\s*/([A-Za-z0-9._-]+)\s+.", line)
        if match:
            return match.group(1)
    return ""


def check_hot_surfaces() -> list[str]:
    checked: list[str] = []
    slash = (ROOT / "SLASH_COMMANDS.md").read_text(encoding="utf-8")
    for route in HOT_ROUTES:
        check_file(ROOT / ".agent" / "workflows" / f"{route}.md", f"/{route} workflow")
        check_file(ROOT / ".claude" / "commands" / f"{route}.md", f"/{route} Claude command")
        check_file(
            ROOT / ".agents" / "skills" / f"source-command-{route}" / "SKILL.md",
            f"/{route} source-command skill",
        )
        if f"`/{route}`" not in slash:
            fail(f"Missing /{route} row in SLASH_COMMANDS.md")
        checked.append(route)
    return checked


def check_router_probes() -> list[str]:
    receipts: list[str] = []
    for query, expected in PROBES:
        proc = run([sys.executable, "execution/workflow_router.py", "search", query])
        if proc.returncode != 0:
            fail(f"workflow_router failed for {query!r}: {proc.stderr.strip()}")
        got = first_route(proc.stdout)
        if got != expected:
            fail(f"Router probe {query!r} expected /{expected}, got /{got or 'none'}")
        receipts.append(f"{query} -> /{got}")
    return receipts


def check_routing_enforcer() -> list[str]:
    receipts: list[str] = []
    for query, expected in PROBES:
        proc = run(
            [
                sys.executable,
                "execution/routing_enforcer.py",
                "check",
                "--request",
                query,
                "--workflow",
                expected,
                "--no-log",
            ]
        )
        if proc.returncode != 0:
            fail(f"routing_enforcer rejected /{expected} for {query!r}: {proc.stdout or proc.stderr}")
        data = json.loads(proc.stdout)
        if not data.get("valid"):
            fail(f"routing_enforcer marked /{expected} invalid for {query!r}: {data}")
        receipts.append(f"{query} valid as /{expected}")
    return receipts


def check_hook_parity() -> list[str]:
    receipts: list[str] = []
    check_file(ROOT / ".codex" / "tools" / "codex_hook_runner.py", "Codex hook runner")
    check_file(HOOKS_PATH, "Codex hooks config")

    data = json.loads(HOOKS_PATH.read_text(encoding="utf-8"))
    commands: list[str] = []
    for groups in data.get("hooks", {}).values():
        for group in groups:
            for hook in group.get("hooks", []):
                command = str(hook.get("command") or "")
                if command:
                    commands.append(command)

    if len(commands) != 6:
        fail(f"Expected 6 hook commands, found {len(commands)}")
    if not all("codex_hook_runner.py" in command for command in commands):
        fail("Every Codex hook command must call codex_hook_runner.py")
    if not any("dangerous-git" in command for command in commands):
        fail("Codex hook bridge is missing dangerous-git protection")
    if any("CLAUDE_PROJECT_DIR" in command for command in commands):
        fail(".codex/hooks.json still directly depends on CLAUDE_PROJECT_DIR")
    receipts.append("hooks.json uses codex_hook_runner.py for all 6 hooks, including dangerous-git")

    config = CONFIG_PATH.read_text(encoding="utf-8") if CONFIG_PATH.exists() else ""
    missing_optional: list[str] = []
    for suffix in HOOK_STATE_SUFFIXES:
        key = f'{HOOKS_PATH}:{suffix}'
        header = f'[hooks.state."{key}"]'
        marker = config.find(header)
        if marker == -1:
            if suffix == "pre_tool_use:0:1":
                missing_optional.append(key)
                continue
            fail(f"Missing current-root hook state: {key}")
        next_header = config.find("\n[", marker + 1)
        block = config[marker:] if next_header == -1 else config[marker:next_header]
        if "enabled = true" not in block.lower():
            if suffix == "pre_tool_use:0:1":
                missing_optional.append(key)
                continue
            fail(f"Current-root hook state is not enabled: {key}")
    if missing_optional:
        receipts.append("dangerous-git hook trust is pending desktop consent in ~/.codex/config.toml")
    else:
        receipts.append("current-root hook states enabled in ~/.codex/config.toml")

    skill_payload = json.dumps(
        {
            "session_id": "verify-hook-parity",
            "prompt": "Write converting copy from scratch for a supplement brand using Luke Iha copy blocks.",
        }
    )
    proc = run(
        [sys.executable, ".codex/tools/codex_hook_runner.py", "skill-router"],
        input_text=skill_payload,
    )
    if proc.returncode != 0:
        fail(f"skill-router hook dry-run failed: {proc.stderr.strip()}")
    if "ROUTING SUGGESTION" not in proc.stdout:
        fail("skill-router hook dry-run did not emit routing context")
    receipts.append("skill-router hook dry-run emitted routing context")

    safe_bash_payload = json.dumps(
        {
            "tool_name": "Bash",
            "tool_input": {"command": "python3 -c 'print(1)'"},
        }
    )
    proc = run(
        [sys.executable, ".codex/tools/codex_hook_runner.py", "cost-gate"],
        input_text=safe_bash_payload,
    )
    if proc.returncode != 0:
        fail(f"cost-gate hook blocked safe Bash command: {proc.stderr.strip()}")
    receipts.append("cost-gate hook dry-run allowed safe Bash")

    dangerous_git_payload = json.dumps(
        {
            "tool_name": "Bash",
            "tool_input": {"command": "git reset --hard"},
        }
    )
    proc = run(
        [sys.executable, ".codex/tools/codex_hook_runner.py", "dangerous-git"],
        input_text=dangerous_git_payload,
    )
    if proc.returncode != 2:
        fail("dangerous-git hook did not block git reset --hard dry-run payload")
    receipts.append("dangerous-git hook dry-run blocked git reset --hard")

    safe_git_payload = json.dumps(
        {
            "tool_name": "Bash",
            "tool_input": {"command": "git status --short"},
        }
    )
    proc = run(
        [sys.executable, ".codex/tools/codex_hook_runner.py", "dangerous-git"],
        input_text=safe_git_payload,
    )
    if proc.returncode != 0:
        fail(f"dangerous-git hook blocked safe git status payload: {proc.stderr.strip()}")
    receipts.append("dangerous-git hook dry-run allowed safe git status")
    return receipts


def check_preflight_schema() -> dict[str, Any]:
    proc = run(
        [
            sys.executable,
            "execution/codex_operator_preflight.py",
            "Codex hooks are not firing",
            "--json",
        ]
    )
    if proc.returncode != 0:
        fail(f"codex_operator_preflight failed: {proc.stderr.strip()}")
    data = json.loads(proc.stdout)
    required = [
        "intent_lock",
        "co_creative_launchpad",
        "route_candidates",
        "chosen_path",
        "execution_decision",
        "manual_gate_checklist",
        "verification_plan",
        "local_next_action",
        "closeout_prompt",
    ]
    missing = [key for key in required if key not in data]
    if missing:
        fail("Preflight missing schema keys: " + ", ".join(missing))
    if data["chosen_path"].get("owner") != "system-audit":
        fail(f"Preflight expected /system-audit, got /{data['chosen_path'].get('owner')}")
    if not data["execution_decision"].get("can_execute_now"):
        fail("Preflight should execute safe /system-audit hook repair locally")
    if data["local_next_action"].get("mode") != "patch_and_verify":
        fail("Preflight local_next_action should default to patch_and_verify")
    gate_text = json.dumps(data["manual_gate_checklist"]).lower()
    receipt_text = json.dumps(data).lower()
    if "codex_hook_runner.py" not in gate_text or "enabled" not in gate_text or "codex hook bridge configured" not in receipt_text:
        fail("Preflight manual gates do not make Codex hook bridge requirements explicit")
    return data


def check_quality_preflight() -> dict[str, Any]:
    proc = run(
        [
            sys.executable,
            "execution/codex_operator_preflight.py",
            "Create production-ready paid ad scripts for a recruiter and founder with no AI slop",
            "--json",
        ]
    )
    if proc.returncode != 0:
        fail(f"quality preflight failed: {proc.stderr.strip()}")
    data = json.loads(proc.stdout)
    owner = data["chosen_path"].get("owner")
    if owner != "high-taste-writing-os":
        fail(f"Quality preflight expected /high-taste-writing-os, got /{owner}")
    risks = data["intent_lock"].get("risk_reasons") or []
    if risks:
        fail(f"Quality preflight incorrectly risk-blocked paid ad copy language: {risks}")
    support = data["chosen_path"].get("support_gates") or []
    if "copy-engine" not in support or "publishable-copy-gate" not in support:
        fail(f"Quality preflight missing copy support gates: {support}")
    if not data["execution_decision"].get("can_execute_now"):
        fail("Quality preflight should run locally with assumptions after false paid-risk fix")
    return data


def check_regression_preflight() -> dict[str, Any]:
    query = (
        "I think this final version got worse again with the script. "
        "The script is just an explanation, like notes and not actually copywriting. "
        "We apply one fix and then something else breaks."
    )
    proc = run(
        [
            sys.executable,
            "execution/codex_operator_preflight.py",
            query,
            "--json",
        ]
    )
    if proc.returncode != 0:
        fail(f"regression preflight failed: {proc.stderr.strip()}")
    data = json.loads(proc.stdout)
    owner = data["chosen_path"].get("owner")
    if owner != "repeatability-spine":
        fail(f"Regression preflight expected /repeatability-spine, got /{owner}")
    lane = data["intent_lock"].get("lane")
    if lane != "output-regression":
        fail(f"Regression preflight expected output-regression lane, got {lane}")
    if not data["execution_decision"].get("can_execute_now"):
        fail("Regression preflight should run locally with verifier-backed repair.")
    return data


def check_context_failure_preflight() -> dict[str, Any]:
    query = (
        "I give up. Codex is not working in my workspace, the brief gets worse and worse, "
        "and this is now a context issue and not usable."
    )
    proc = run(
        [
            sys.executable,
            "execution/codex_operator_preflight.py",
            query,
            "--json",
        ]
    )
    if proc.returncode != 0:
        fail(f"context-failure preflight failed: {proc.stderr.strip()}")
    data = json.loads(proc.stdout)
    owner = data["chosen_path"].get("owner")
    if owner != "system-audit":
        fail(f"Context-failure preflight expected /system-audit, got /{owner}")
    lane = data["intent_lock"].get("lane")
    if lane != "system-failure":
        fail(f"Context-failure preflight expected system-failure lane, got {lane}")
    if not data["execution_decision"].get("can_execute_now"):
        fail("Context-failure preflight should start safe local system repair.")
    return data


def check_contextual_prompts() -> None:
    proc = run(
        [
            sys.executable,
            "execution/contextual_next_prompts.py",
            "--objective",
            "fix operator lesson and 3 next prompts",
        ]
    )
    if proc.returncode != 0:
        fail(f"contextual_next_prompts failed: {proc.stderr.strip()}")
    text = proc.stdout
    for needle in (
        "## 3 Next Prompts",
        "Use Now",
        "Harden",
        "Expand",
        "/steering-compass",
        "Operator Insight",
        "Hidden Gap/Opportunity",
        "Capability Revealed",
    ):
        if needle not in text:
            fail(f"contextual_next_prompts missing {needle!r}")
    proc = run(
        [
            sys.executable,
            "execution/contextual_next_prompts.py",
            "--stage",
            "execute-next",
            "--objective",
            "Codex explains instead of executing safe local next actions",
        ]
    )
    if proc.returncode != 0:
        fail(f"contextual_next_prompts execute-next failed: {proc.stderr.strip()}")
    text = proc.stdout
    for needle in ("## Local Next Action", "patch_and_verify", "First command", "Verifier"):
        if needle not in text:
            fail(f"contextual_next_prompts execute-next missing {needle!r}")


def check_run_receipt() -> None:
    proc = run([sys.executable, "execution/run_receipt.py", "--verify"])
    if proc.returncode != 0:
        fail(f"run_receipt verification failed: {proc.stdout or proc.stderr}")
    if "PASS" not in proc.stdout:
        fail("run_receipt verifier did not print PASS")


def check_subagent_approval_language() -> None:
    proc = run([sys.executable, "execution/verify_subagent_approval_language.py"])
    if proc.returncode != 0:
        fail(f"subagent approval verifier failed: {proc.stdout or proc.stderr}")


def check_global_execution_bias_bridge() -> None:
    proc = run([sys.executable, "execution/verify_global_execution_bias_bridge.py"])
    if proc.returncode != 0:
        fail(f"global execution-bias bridge verifier failed: {proc.stdout or proc.stderr}")


def check_steering_compass_quality() -> None:
    proc = run([sys.executable, "execution/verify_steering_compass_quality.py"])
    if proc.returncode != 0:
        fail(f"steering compass quality verifier failed: {proc.stdout or proc.stderr}")


def check_global_steering_persistence() -> None:
    proc = run([sys.executable, "execution/verify_global_steering_persistence.py"])
    if proc.returncode != 0:
        fail(f"global steering persistence verifier failed: {proc.stdout or proc.stderr}")


def main() -> int:
    failures: list[str] = []
    sections: list[tuple[str, Any]] = []
    checks = [
        ("hot_surfaces", check_hot_surfaces),
        ("router_probes", check_router_probes),
        ("routing_enforcer", check_routing_enforcer),
        ("hook_parity", check_hook_parity),
        ("preflight_schema", check_preflight_schema),
        ("quality_preflight", check_quality_preflight),
        ("regression_preflight", check_regression_preflight),
        ("context_failure_preflight", check_context_failure_preflight),
        ("contextual_prompts", check_contextual_prompts),
        ("run_receipt", check_run_receipt),
        ("subagent_approval_language", check_subagent_approval_language),
        ("global_execution_bias_bridge", check_global_execution_bias_bridge),
        ("steering_compass_quality", check_steering_compass_quality),
        ("global_steering_persistence", check_global_steering_persistence),
    ]
    for name, func in checks:
        try:
            sections.append((name, func()))
        except Exception as exc:  # noqa: BLE001 - verifier should report all sections cleanly.
            failures.append(f"{name}: {exc}")

    if failures:
        print("GOOGLE OPERATOR CORE VERIFICATION FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("GOOGLE OPERATOR CORE VERIFICATION PASS")
    for name, details in sections:
        if details:
            print(f"- {name}: {details}")
        else:
            print(f"- {name}: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
