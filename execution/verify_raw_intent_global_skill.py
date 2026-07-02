#!/usr/bin/env python3
"""Verify the global Raw Intent Bridge skill wrappers."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]
GLOBAL_SKILLS = Path.home() / ".codex" / "skills"
RAW_SKILL = GLOBAL_SKILLS / "raw-intent-bridge" / "SKILL.md"
ALIAS_SKILL = GLOBAL_SKILLS / "source-command-raw-intent-bridge" / "SKILL.md"
FALLBACK_SCRIPT = GLOBAL_SKILLS / "raw-intent-bridge" / "scripts" / "compile_packet.py"
VALIDATOR = Path.home() / ".codex" / "skills" / ".system" / "skill-creator" / "scripts" / "quick_validate.py"
INVOCATION_FORMS = (
    "/raw-intent-bridge [payload]",
    "raw-intent-bridge: [payload]",
    "source-command-raw-intent-bridge: [payload]",
)
PREFIX_LEAKS = ("/raw-intent-bridge", "raw-intent-bridge:", "source-command-raw-intent-bridge:")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def validator_python() -> str:
    venv_python = ROOT / ".venv" / "bin" / "python"
    return str(venv_python if venv_python.exists() else Path(sys.executable))


def verify_files() -> None:
    require(RAW_SKILL.exists(), f"missing global skill: {RAW_SKILL}")
    require(ALIAS_SKILL.exists(), f"missing global alias skill: {ALIAS_SKILL}")
    require(FALLBACK_SCRIPT.exists(), f"missing bundled fallback compiler: {FALLBACK_SCRIPT}")

    raw = read(RAW_SKILL)
    alias = read(ALIAS_SKILL)

    require("name: raw-intent-bridge" in raw, "raw global skill frontmatter name mismatch")
    require("name: source-command-raw-intent-bridge" in alias, "alias global skill frontmatter name mismatch")
    require("Use before normal routing" in raw, "raw global skill must trigger before normal routing")
    require("natural-language thinking" in raw, "raw global skill missing natural-language trigger")
    require("says he is the bottleneck" in raw, "raw global skill missing bottleneck trigger")
    require("cannot translate ideas specifically or deterministically" in raw, "raw global skill missing original intent trigger")
    require("does not know how to ask Codex" in raw, "raw global skill missing natural-language trigger")
    require("Codex-ready run packet" in raw, "raw global skill missing run-packet trigger")
    require("Core Promise" in raw, "raw global skill missing behavior promise")
    require("Invocation Contract" in raw, "raw global skill missing invocation contract")
    require("Packet + Run Default" in raw, "raw global skill missing Packet + Run default")
    require("Put this skill before any raw context" in raw, "raw global skill must promise prefix-style use")
    require("everything after the prefix" in raw, "raw global skill must define payload stripping")
    require("immediately follow the first safe local action" in raw, "raw global skill missing Packet + Run action rule")
    require("Bundled fallback" in raw, "raw global skill missing bundled fallback path")
    require("do not make him become the prompt engineer" in raw, "raw global skill missing operator-relief rule")
    require("/Users/farricecain/Google Antigravity" in raw, "raw global skill missing Google Antigravity fallback")
    require("raw_intent_run_packet.py" in raw, "raw global skill missing compiler reference")
    require("scripts/compile_packet.py" in raw, "raw global skill missing fallback compiler reference")
    require("plugin marketplace edits" in raw, "raw global skill missing plugin boundary")
    require("real Codex subagents" in raw, "raw global skill missing subagent boundary")
    require("/Users/farricecain/.codex/skills/raw-intent-bridge/SKILL.md" in alias, "alias missing global skill pointer")
    require("scripts/compile_packet.py" in alias, "alias missing fallback compiler reference")
    require("raw_intent_run_packet.py" in alias, "alias missing compiler reference")
    require("Invocation Contract" in alias, "alias missing invocation contract")
    require("Packet + Run Default" in alias, "alias missing Packet + Run default")
    require("everything after the prefix" in alias, "alias must define payload stripping")
    for form in INVOCATION_FORMS:
        require(form in raw, f"raw global skill missing invocation form: {form}")
        require(form in alias, f"alias global skill missing invocation form: {form}")


def validate_skill(path: Path) -> None:
    require(VALIDATOR.exists(), f"missing skill validator: {VALIDATOR}")
    result = subprocess.run(
        [validator_python(), str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    require(result.returncode == 0, f"skill validation failed for {path}: {result.stdout}\n{result.stderr}")


def verify_local_bridge_still_passes() -> None:
    result = subprocess.run(
        [sys.executable, "execution/verify_raw_intent_bridge_command.py"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    require(result.returncode == 0, f"local bridge verifier failed: {result.stdout}\n{result.stderr}")


def verify_fallback_compiler() -> None:
    def run_case(intent: str) -> dict:
        result = subprocess.run(
            [
                sys.executable,
                str(FALLBACK_SCRIPT),
                intent,
                "--json",
            ],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        require(result.returncode == 0, f"fallback compiler failed for {intent!r}: {result.stderr}")
        data = json.loads(result.stdout)
        for field in ("raw_intent", "first_safe_action", "operator_run_prompt"):
            value = str(data[field]).lower()
            for prefix in PREFIX_LEAKS:
                require(prefix.lower() not in value, f"fallback leaked {prefix} into {field}: {data[field]}")
        require(str(data["first_safe_action"]).startswith("/"), f"fallback first safe action not executable: {data['first_safe_action']}")
        return data

    data = run_case(
        "I was clear about my intent but this skill is not what I envisioned; rebuild it so my messy natural thoughts become Codex execution packets"
    )
    required = {
        "raw_intent",
        "predicted_need",
        "center",
        "success_standard",
        "constraints",
        "missing_inputs",
        "questions_that_change_execution",
        "chosen_route",
        "support_gates",
        "first_safe_action",
        "verification_plan",
        "operator_run_prompt",
        "plugin_packaging_verdict",
    }
    missing = sorted(required - set(data))
    require(not missing, f"fallback packet missing fields: {missing}")
    require(data["chosen_route"] == "system-audit", f"fallback should route repair language to system-audit, got {data['chosen_route']}")
    require("source-to-skill-system" in data["support_gates"], "fallback system repair missing source-to-skill support")
    require("Farrice's natural-language intent" in data["center"], "fallback must preserve natural-language bridge center")

    slash = run_case("/raw-intent-bridge I have a messy business idea and need the right execution path")
    require(slash["chosen_route"] in {"autopilot", "revenue-offer-agent"}, f"slash fallback chose unexpected route: {slash['chosen_route']}")

    colon = run_case("raw-intent-bridge: I have a rough offer idea but do not know how to ask Codex")
    require(colon["chosen_route"] == "revenue-offer-agent", f"colon fallback should route offer payload to revenue, got {colon['chosen_route']}")

    source_command = run_case("source-command-raw-intent-bridge: audit this raw task and give me the first safe action")
    require(source_command["chosen_route"] == "system-audit", f"source-command fallback should route audit payload to system-audit, got {source_command['chosen_route']}")


def main() -> int:
    verify_files()
    validate_skill(RAW_SKILL.parent)
    validate_skill(ALIAS_SKILL.parent)
    verify_fallback_compiler()
    verify_local_bridge_still_passes()
    print("Raw Intent Bridge global skill verification: PASS")
    print("- global raw-intent-bridge skill exists and points to the canonical compiler")
    print("- global source-command alias exists and delegates to raw-intent-bridge")
    print("- bundled fallback compiler renders a system-audit repair packet")
    print("- global invocation contract documents slash, colon, and source-command forms")
    print("- fallback compiler strips all bridge prefixes before route/action generation")
    print("- both global wrappers validate as Codex skills")
    print("- local /raw-intent-bridge command verifier still passes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
