#!/usr/bin/env python3
"""Verify the global Codex-native adaptive judgment floor."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
GLOBAL_AGENTS = Path("/Users/farricecain/.codex/AGENTS.md")
GLOBAL_RAW_INTENT = Path("/Users/farricecain/.codex/skills/raw-intent-bridge/SKILL.md")
GLOBAL_AUTOPILOT = Path("/Users/farricecain/.codex/skills/autopilot/SKILL.md")
OPERATING_CONTRACT = ROOT / "semantic_libraries/antigravity/primitives/operating-alignment-contract.md"
MAGIC_SET = ROOT / "semantic_libraries/antigravity/primitives/magic-preservation-regression-set.md"
HOOK = ROOT / "execution/hooks/steering_loop_hook.py"

RAW_STRATEGIC_PROMPT = (
    "I have been thinking about a messy product idea and I want help finding the real opportunity. "
    "I do not know whether the market exists, and I also need to know how to sell it. "
    "On top of that, how would we build it, what should we avoid, and what evidence would change the decision?"
)


def fail(message: str) -> None:
    raise AssertionError(message)


def read(path: Path) -> str:
    if not path.exists():
        fail(f"Missing required surface: {path}")
    return path.read_text(encoding="utf-8")


def require(label: str, path: Path, needles: list[str]) -> None:
    text = " ".join(read(path).lower().split())
    missing = [needle for needle in needles if " ".join(needle.lower().split()) not in text]
    if missing:
        fail(f"{label} missing: {', '.join(missing)}")


def check_global_agents() -> None:
    require(
        "global AGENTS",
        GLOBAL_AGENTS,
        [
            "Global Adaptive Judgment Floor",
            "Default the reasoning principles; adapt the workflow depth",
            "without magic words",
            "senior-partner pushback",
            "Evidence must change",
            "UNTESTED",
            "LOCKED",
            "PARKED",
            "NEXT ACTION",
            "raw-intent-bridge is optional",
            "private token-by-token chain-of-thought",
        ],
    )


def check_global_front_doors() -> None:
    require(
        "global raw-intent bridge",
        GLOBAL_RAW_INTENT,
        [
            "Automatic Trigger",
            "without a prefix",
            "optional explicit invocation",
            "inspect the compiled packet",
        ],
    )
    require(
        "global autopilot",
        GLOBAL_AUTOPILOT,
        [
            "Adaptive Judgment Floor",
            "operating-alignment-contract.md",
            "raw-intent-bridge is optional",
            "evidence changes the recommendation",
        ],
    )


def check_canonical_contract() -> None:
    require(
        "operating-alignment contract",
        OPERATING_CONTRACT,
        [
            "Adaptive Judgment Floor",
            "Default the reasoning principles; adapt the workflow depth",
            "Research earns inclusion only when it changes a decision",
            "VERIFIED",
            "UNTESTED",
            "LOCKED",
            "PARKED",
            "NEXT ACTION",
        ],
    )
    require(
        "magic preservation set",
        MAGIC_SET,
        [
            "Casual Gacha Copilot Market Verdict",
            "decision compression",
            "category activity from exact-offer demand",
            "without requiring a magic phrase",
        ],
    )


def check_prompt_hook() -> None:
    proc = subprocess.run(
        [sys.executable, str(HOOK), "test-mirror"],
        cwd=ROOT,
        text=True,
        input=RAW_STRATEGIC_PROMPT,
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        fail(f"intent-mirror hook failed: {proc.stdout or proc.stderr}")
    if "fires: YES" not in proc.stdout or "INTENT MIRROR" not in proc.stdout:
        fail(f"raw strategic prompt did not trigger the intent mirror:\n{proc.stdout}")


def main() -> int:
    checks = [
        check_global_agents,
        check_global_front_doors,
        check_canonical_contract,
        check_prompt_hook,
    ]
    failures: list[str] = []
    for check in checks:
        try:
            check()
        except Exception as exc:  # noqa: BLE001 - verifier should report every failed surface.
            failures.append(f"{check.__name__}: {exc}")
    if failures:
        print("GLOBAL ADAPTIVE JUDGMENT FLOOR VERIFICATION FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("GLOBAL ADAPTIVE JUDGMENT FLOOR VERIFICATION PASS")
    print("- raw strategic language triggers the intent mirror without a command prefix")
    print("- global Codex instructions carry the adaptive judgment floor")
    print("- Google Antigravity retains the canonical contract and preservation exemplar")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
