#!/usr/bin/env python3
"""Verify Codex Claude-parity routing and hook bridge behavior.

This verifier is intentionally narrow. It checks the complaint family that was
misrouted before, the repeatability/caliber-drift path, normal expert content
routing, prompt-hook suppression, and Codex-local hook parity without touching
the `.claude/` surface.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
HOOKS_PATH = ROOT / ".codex" / "hooks.json"
CLAUDE_DIR = ROOT / ".claude"

SYSTEM_PROMPT = (
    "Codex is blocking hooks and routing wrong defaults; "
    "match Claude Code without breaking my workspace"
)
REPEATABILITY_PROMPT = (
    "I copied over everything and the previous session import shows a massive caliber difference"
)
CONTENT_PROMPT = "Write production-ready paid ad scripts with no AI slop"
RAW_INTENT_SKILL_LINK_PROMPT = (
    "[$raw-intent-bridge](/Users/farricecain/.codex/skills/raw-intent-bridge/SKILL.md) "
    "Josh has copyright issues and needs brand identity clarity for Lindy Hop apparel."
)
WIRING_PROMPT = (
    "Can you do a full audit or check and repair on things that are not wired "
    "or should not be wired together and are the default settings? I feel like "
    "the biggest thing is that certain hooks or routes are being handcuffed and "
    "chained together that should not be. source-command-steering-compass "
    "source-command-convene"
)
SELECTIVE_LANGUAGE_PROMPT = (
    "See, this whole selective language being linked to stuff is nonsense. "
    "I feel like it's what's causing issues. What's going on here?!"
)
IMPLEMENT_PLAN_PROMPT = (
    "Please implement this Codex routing/wiring parity repair plan: add no-log "
    "route probes, tighten preflight, verify hooks, and keep the previous session "
    "caliber probe as a repeatability test case."
)
REPAIR_STATUS_REVIEW_PROMPT = (
    "so what was done here? from the looks nothing was fixed that I wanted"
)
STEERING_PROMPT = "give me better 3 next prompts and an operator lesson"
CONVENE_PROMPT = "Convene the council to deliberate on an offer strategy"
CONTEXT_NOTE_PROMPT = "The KU was the complete practical test that I gave."


def run(args: list[str], input_text: str | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True, input=input_text)


def fail(message: str) -> None:
    raise AssertionError(message)


def first_route(router_stdout: str) -> str:
    for line in router_stdout.splitlines():
        match = re.match(r"\s*/([A-Za-z0-9._-]+)\s+.", line)
        if match:
            return match.group(1)
    return ""


def check_router() -> list[str]:
    probes = [
        (SYSTEM_PROMPT, "system-audit"),
        (WIRING_PROMPT, "system-audit"),
        (SELECTIVE_LANGUAGE_PROMPT, "system-audit"),
        (IMPLEMENT_PLAN_PROMPT, "system-audit"),
        (REPAIR_STATUS_REVIEW_PROMPT, "system-audit"),
        (REPEATABILITY_PROMPT, "repeatability-spine"),
        (CONTENT_PROMPT, "high-taste-writing-os"),
        (STEERING_PROMPT, "steering-compass"),
        (CONVENE_PROMPT, "convene"),
    ]
    receipts: list[str] = []
    for prompt, expected in probes:
        proc = run([sys.executable, "execution/workflow_router.py", "search", prompt])
        if proc.returncode != 0:
            fail(f"workflow_router failed for {prompt!r}: {proc.stderr.strip()}")
        got = first_route(proc.stdout)
        if got != expected:
            fail(f"workflow_router expected /{expected} for {prompt!r}, got /{got or 'none'}")
        receipts.append(f"{prompt} -> /{got}")
    return receipts


def check_routing_enforcer() -> list[str]:
    probes = [
        (SYSTEM_PROMPT, "system-audit"),
        (WIRING_PROMPT, "system-audit"),
        (SELECTIVE_LANGUAGE_PROMPT, "system-audit"),
        (IMPLEMENT_PLAN_PROMPT, "system-audit"),
        (REPAIR_STATUS_REVIEW_PROMPT, "system-audit"),
        (REPEATABILITY_PROMPT, "repeatability-spine"),
        (CONTENT_PROMPT, "high-taste-writing-os"),
        (STEERING_PROMPT, "steering-compass"),
        (CONVENE_PROMPT, "convene"),
    ]
    receipts: list[str] = []
    for prompt, expected in probes:
        proc = run(
            [
                sys.executable,
                "execution/routing_enforcer.py",
                "check",
                "--request",
                prompt,
                "--workflow",
                expected,
                "--no-log",
            ]
        )
        if proc.returncode != 0:
            fail(f"routing_enforcer rejected /{expected} for {prompt!r}: {proc.stdout or proc.stderr}")
        data = json.loads(proc.stdout)
        if not data.get("valid"):
            fail(f"routing_enforcer marked /{expected} invalid for {prompt!r}: {data}")
        receipts.append(f"{prompt} valid as /{expected}")
    return receipts


def preflight(prompt: str) -> dict[str, Any]:
    proc = run([sys.executable, "execution/codex_operator_preflight.py", prompt, "--json"])
    if proc.returncode != 0:
        fail(f"codex_operator_preflight failed for {prompt!r}: {proc.stderr.strip()}")
    return json.loads(proc.stdout)


def check_preflight() -> list[str]:
    receipts: list[str] = []

    system = preflight(SYSTEM_PROMPT)
    if system["chosen_path"].get("owner") != "system-audit":
        fail(f"preflight system prompt expected /system-audit, got /{system['chosen_path'].get('owner')}")
    if system["intent_lock"].get("lane") != "system-failure":
        fail(f"preflight system prompt expected system-failure lane, got {system['intent_lock'].get('lane')}")
    if not system["execution_decision"].get("can_execute_now"):
        fail("'without breaking my workspace' should not block safe local diagnosis")
    if system["intent_lock"].get("risk_reasons"):
        fail(f"system prompt should not be risk-gated: {system['intent_lock'].get('risk_reasons')}")
    receipts.append("system complaint preflight -> /system-audit, executable local diagnosis")

    wiring = preflight(WIRING_PROMPT)
    if wiring["chosen_path"].get("owner") != "system-audit":
        fail(f"preflight wiring prompt expected /system-audit, got /{wiring['chosen_path'].get('owner')}")
    if wiring["intent_lock"].get("lane") != "system-failure":
        fail(f"preflight wiring prompt expected system-failure lane, got {wiring['intent_lock'].get('lane')}")
    support_gates = wiring["chosen_path"].get("support_gates") or []
    if "steering-compass" in support_gates or "convene" in support_gates:
        fail(f"wiring/system-audit support gates should not hard-chain steering or convene: {support_gates}")
    receipts.append("wiring/default-settings preflight -> /system-audit without steering/convene support-chain")

    selective = preflight(SELECTIVE_LANGUAGE_PROMPT)
    if selective["chosen_path"].get("owner") != "system-audit":
        fail(f"selective-language prompt expected /system-audit, got /{selective['chosen_path'].get('owner')}")
    if selective["intent_lock"].get("lane") != "system-failure":
        fail(f"selective-language prompt expected system-failure lane, got {selective['intent_lock'].get('lane')}")
    receipts.append("selective-language complaint preflight -> /system-audit")

    implementation = preflight(IMPLEMENT_PLAN_PROMPT)
    if implementation["chosen_path"].get("owner") != "system-audit":
        fail(
            "implementation plan prompt expected /system-audit even with embedded "
            f"repeatability wording, got /{implementation['chosen_path'].get('owner')}"
        )
    if implementation["intent_lock"].get("lane") != "system-failure":
        fail(
            "implementation plan prompt expected system-failure lane, "
            f"got {implementation['intent_lock'].get('lane')}"
        )
    receipts.append("implementation plan with embedded repeatability probe preflight -> /system-audit")

    repair_status = preflight(REPAIR_STATUS_REVIEW_PROMPT)
    if repair_status["chosen_path"].get("owner") != "system-audit":
        fail(
            "repair status-review prompt expected /system-audit, "
            f"got /{repair_status['chosen_path'].get('owner')}"
        )
    if repair_status["co_creative_launchpad"].get("questions_that_change_execution"):
        fail(
            "repair status-review prompt should not ask broad questions: "
            f"{repair_status['co_creative_launchpad'].get('questions_that_change_execution')}"
        )
    receipts.append("repair status-review prompt preflight -> /system-audit without broad questions")

    repeatability = preflight(REPEATABILITY_PROMPT)
    if repeatability["chosen_path"].get("owner") != "repeatability-spine":
        fail(
            "preflight repeatability prompt expected /repeatability-spine, "
            f"got /{repeatability['chosen_path'].get('owner')}"
        )
    if repeatability["intent_lock"].get("lane") != "output-regression":
        fail(
            "preflight repeatability prompt expected output-regression lane, "
            f"got {repeatability['intent_lock'].get('lane')}"
        )
    receipts.append("prior-session caliber prompt preflight -> /repeatability-spine")

    content = preflight(CONTENT_PROMPT)
    if content["chosen_path"].get("owner") != "high-taste-writing-os":
        fail(f"preflight content prompt expected /high-taste-writing-os, got /{content['chosen_path'].get('owner')}")
    if content["intent_lock"].get("risk_reasons"):
        fail(f"content prompt should not be risk-gated by 'paid ad': {content['intent_lock'].get('risk_reasons')}")
    receipts.append("expert content prompt preflight -> /high-taste-writing-os")

    steering = preflight(STEERING_PROMPT)
    if steering["chosen_path"].get("owner") != "steering-compass":
        fail(f"explicit steering prompt expected /steering-compass, got /{steering['chosen_path'].get('owner')}")
    receipts.append("explicit steering prompt still routes -> /steering-compass")

    convene = preflight(CONVENE_PROMPT)
    if convene["chosen_path"].get("owner") != "convene":
        fail(f"explicit convene prompt expected /convene, got /{convene['chosen_path'].get('owner')}")
    receipts.append("explicit convene prompt still routes -> /convene")

    return receipts


def hook_context(prompt: str) -> str:
    payload = json.dumps({"session_id": "verify-codex-claude-parity", "prompt": prompt})
    proc = run([sys.executable, ".codex/tools/codex_hook_runner.py", "skill-router"], input_text=payload)
    if proc.returncode != 0:
        fail(f"skill_router_hook failed for {prompt!r}: {proc.stderr.strip()}")
    if not proc.stdout.strip():
        return ""
    data = json.loads(proc.stdout)
    return str(data.get("hookSpecificOutput", {}).get("additionalContext") or "")


def check_prompt_hook() -> list[str]:
    receipts: list[str] = []
    noisy_routes = ("/luke", "/diandra", "/kallaway", "/design", "/supercomputer", "/paid")

    system_context = hook_context(SYSTEM_PROMPT)
    if "CONTROL ROUTING" not in system_context or "/system-audit" not in system_context:
        fail(f"system prompt hook did not emit /system-audit override: {system_context}")
    if "ROUTING SUGGESTION" in system_context:
        fail("system prompt hook emitted expert suggestions instead of suppressing them")
    if any(route in system_context.lower() for route in noisy_routes):
        fail(f"system prompt hook leaked noisy expert route suggestions: {system_context}")
    receipts.append("system complaint hook suppressed expert suggestions and emitted /system-audit")

    wiring_context = hook_context(WIRING_PROMPT)
    if "CONTROL ROUTING" not in wiring_context or "/system-audit" not in wiring_context:
        fail(f"wiring prompt hook did not emit /system-audit override: {wiring_context}")
    if "ROUTING SUGGESTION" in wiring_context:
        fail("wiring prompt hook emitted expert suggestions instead of suppressing them")
    if any(route in wiring_context.lower() for route in noisy_routes):
        fail(f"wiring prompt hook leaked noisy expert route suggestions: {wiring_context}")
    receipts.append("wiring/default-settings hook suppressed expert suggestions and emitted /system-audit")

    selective_context = hook_context(SELECTIVE_LANGUAGE_PROMPT)
    if "CONTROL ROUTING" not in selective_context or "/system-audit" not in selective_context:
        fail(f"selective-language hook did not emit /system-audit override: {selective_context}")
    if "ROUTING SUGGESTION" in selective_context:
        fail("selective-language hook emitted expert suggestions instead of suppressing them")
    receipts.append("selective-language hook suppressed expert suggestions and emitted /system-audit")

    implementation_context = hook_context(IMPLEMENT_PLAN_PROMPT)
    if "CONTROL ROUTING" not in implementation_context or "/system-audit" not in implementation_context:
        fail(f"implementation plan hook did not emit /system-audit override: {implementation_context}")
    if "ROUTING SUGGESTION" in implementation_context:
        fail("implementation plan hook emitted expert suggestions instead of suppressing them")
    receipts.append("implementation plan hook suppressed experts and emitted /system-audit")

    status_context = hook_context(REPAIR_STATUS_REVIEW_PROMPT)
    if "CONTROL ROUTING" not in status_context or "/system-audit" not in status_context:
        fail(f"repair status-review hook did not emit /system-audit override: {status_context}")
    if "ROUTING SUGGESTION" in status_context:
        fail("repair status-review hook emitted expert suggestions instead of suppressing them")
    receipts.append("repair status-review hook suppressed experts and emitted /system-audit")

    repeatability_context = hook_context(REPEATABILITY_PROMPT)
    if "CONTROL ROUTING" not in repeatability_context or "/repeatability-spine" not in repeatability_context:
        fail(f"repeatability prompt hook did not emit /repeatability-spine override: {repeatability_context}")
    if "ROUTING SUGGESTION" in repeatability_context:
        fail("repeatability prompt hook emitted expert suggestions instead of suppressing them")
    receipts.append("prior-session caliber hook suppressed experts and emitted /repeatability-spine")

    content_context = hook_context(CONTENT_PROMPT)
    if "CONTROL ROUTING" in content_context:
        fail(f"content prompt should not be control-overridden: {content_context}")
    if "ROUTING SUGGESTION" not in content_context:
        fail("content prompt should still receive expert routing suggestions")
    receipts.append("content prompt still receives expert routing suggestions")

    raw_intent_context = hook_context(RAW_INTENT_SKILL_LINK_PROMPT)
    if "CONTROL ROUTING OVERRIDE" in raw_intent_context:
        fail(f"explicit skill-link content prompt should not be control-overridden: {raw_intent_context}")
    receipts.append("explicit skill-link content prompt does not emit /system-audit override")

    context_note = hook_context(CONTEXT_NOTE_PROMPT)
    if context_note:
        fail(f"context-only follow-up should not emit routing context: {context_note}")
    receipts.append("context-only KU follow-up stays quiet")
    return receipts


def hook_commands() -> list[str]:
    data = json.loads(HOOKS_PATH.read_text(encoding="utf-8"))
    commands: list[str] = []
    for groups in data.get("hooks", {}).values():
        for group in groups:
            for hook in group.get("hooks", []):
                command = str(hook.get("command") or "")
                if command:
                    commands.append(command)
    return commands


def check_hook_bridge() -> list[str]:
    receipts: list[str] = []
    if not HOOKS_PATH.exists():
        fail("missing .codex/hooks.json")
    commands = hook_commands()
    expected_targets = (
        "cost-gate",
        "dangerous-git",
        "active-tool-lock",
        "skill-router",
        "session-ledger posttool",
        "artifact-placement",
        "session-ledger prompt",
        "guard-stranded",
        "session-ledger stop",
    )
    if len(commands) != 9:
        fail(f"expected 9 Codex hook commands, found {len(commands)}")
    if not all("codex_hook_runner.py" in command for command in commands):
        fail("every Codex hook command must call codex_hook_runner.py")
    for target in expected_targets:
        if not any(target in command for command in commands):
            fail(f"missing Codex hook target: {target}")
    if any(".claude/" in command for command in commands):
        fail("Codex hooks should not shell into .claude hook files")
    receipts.append(
        "Codex hook bridge includes cost-gate, dangerous-git, active-tool-lock, "
        "skill-router, session-ledger posttool/prompt/stop, and guard-stranded"
    )

    dangerous_payload = json.dumps({"tool_name": "Bash", "tool_input": {"command": "git reset --hard"}})
    proc = run([sys.executable, ".codex/tools/codex_hook_runner.py", "dangerous-git"], input_text=dangerous_payload)
    if proc.returncode != 2:
        fail("dangerous-git hook did not block git reset --hard dry-run payload")
    receipts.append("dangerous-git dry-run blocks git reset --hard")

    safe_git_payload = json.dumps({"tool_name": "Bash", "tool_input": {"command": "git status --short"}})
    proc = run([sys.executable, ".codex/tools/codex_hook_runner.py", "dangerous-git"], input_text=safe_git_payload)
    if proc.returncode != 0:
        fail(f"dangerous-git hook blocked safe git status payload: {proc.stderr.strip()}")
    receipts.append("dangerous-git dry-run allows git status --short")

    safe_payload = json.dumps({"tool_name": "Bash", "tool_input": {"command": "python3 --version"}})
    proc = run([sys.executable, ".codex/tools/codex_hook_runner.py", "cost-gate"], input_text=safe_payload)
    if proc.returncode != 0:
        fail(f"cost-gate blocked normal safe local command: {proc.stderr.strip()}")
    receipts.append("cost-gate dry-run allows safe local command")

    paid_payload = json.dumps(
        {
            "tool_name": "Bash",
            "tool_input": {
                "command": "python3 execution/fal_video_seedance.py --resolution 1080p --duration 5"
            },
        }
    )
    proc = run([sys.executable, ".codex/tools/codex_hook_runner.py", "cost-gate"], input_text=paid_payload)
    if proc.returncode != 2:
        fail("cost-gate should block or require approval for a paid 1080p Seedance command")
    receipts.append("cost-gate dry-run blocks/requires approval for paid 1080p Seedance command")
    return receipts


def check_no_claude_edit_from_repair() -> list[str]:
    receipts: list[str] = []
    commands = hook_commands()
    if any(str(CLAUDE_DIR) in command or ".claude/" in command for command in commands):
        fail("Codex hook bridge references .claude files")
    receipts.append("Codex parity bridge does not reference .claude hook files")
    receipts.append("no verifier writes to .claude; git dirt in .claude must be judged from pre-existing status")
    return receipts


def check_constitution_sync() -> list[str]:
    """Apex W3 (2026-07-29): the shared constitution blocks are GENERATED from
    directives/constitution/shared-blocks.md — drift between CLAUDE.md and
    AGENTS.md now fails the fleet instead of surfacing months later."""
    proc = subprocess.run(
        [sys.executable, str(ROOT / "execution" / "constitution_compiler.py"), "check"],
        capture_output=True, text=True, cwd=ROOT)
    if proc.returncode != 0:
        fail(f"constitution drift: {proc.stdout.strip()[:300]}")
    return ["shared constitution blocks in sync (compiler check exit 0)"]


def main() -> int:
    checks = [
        ("router", check_router),
        ("routing_enforcer", check_routing_enforcer),
        ("preflight", check_preflight),
        ("prompt_hook", check_prompt_hook),
        ("hook_bridge", check_hook_bridge),
        ("no_claude_bridge", check_no_claude_edit_from_repair),
        ("constitution_sync", check_constitution_sync),
    ]
    sections: list[tuple[str, Any]] = []
    failures: list[str] = []
    for name, func in checks:
        try:
            sections.append((name, func()))
        except Exception as exc:  # noqa: BLE001 - verifier should aggregate receipts.
            failures.append(f"{name}: {exc}")

    if failures:
        print("CODEX CLAUDE PARITY VERIFICATION FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("CODEX CLAUDE PARITY VERIFICATION PASS")
    for name, details in sections:
        print(f"- {name}: {details}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
