#!/usr/bin/env python3
"""Verify the Agentic Engineering Loop contract and workflow adoption."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRIMITIVE = ROOT / "semantic_libraries" / "antigravity" / "primitives" / "agentic-engineering-loop-contract.md"
SOURCE_PACKAGE = ROOT / "extractions" / "video-context" / "PzVV4X37ihg"
FILES = {
    "source_to_skill": ROOT / ".agent" / "workflows" / "source-to-skill-system.md",
    "expert_composition": ROOT / ".agent" / "workflows" / "expert-composition-governor.md",
    "self_evolve": ROOT / ".agent" / "workflows" / "self-evolve.md",
    "system_audit": ROOT / ".agent" / "workflows" / "system-audit.md",
    "codex": ROOT / "CODEX.md",
}

REQUIRED_PRIMITIVE_TERMS = [
    "Human-owned thinking",
    "Context sweet spot",
    "Source truth first",
    "Plan then shrink",
    "Small chunks",
    "Structure cleanup",
    "Review-until-stop",
    "Dependency safety",
    "Ship earlier, harden faster",
    "Default Agentic Engineering Packet",
    "Dependency Safety Gate",
    "Review Loop Standard",
]

REQUIRED_PACKET_FIELDS = [
    "Objective",
    "Source truth",
    "Context plan",
    "Work chunks",
    "Review loop",
    "Dependency gate",
    "Structure pass",
    "Use-now artifact",
    "Hardening proof",
]

ROUTING_QUERIES = [
    "agentic engineering context engineering small PR review loop",
    "turn this agent engineering video into source-to-system improvements",
    "package safety dependency security agent built work",
    "context engineering source truth review-until-stop loop",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def run(args: list[str]) -> str:
    result = subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(f"{' '.join(args)} failed:\n{result.stdout}")
    return result.stdout


def main() -> int:
    failures: list[str] = []

    if not PRIMITIVE.exists():
        failures.append(f"missing primitive: {PRIMITIVE.relative_to(ROOT)}")
    else:
        primitive = read(PRIMITIVE)
        for term in REQUIRED_PRIMITIVE_TERMS + REQUIRED_PACKET_FIELDS:
            if term not in primitive:
                failures.append(f"primitive missing term: {term}")
        if "PzVV4X37ihg" not in primitive:
            failures.append("primitive missing source video id")
        if "transcript-backed spoken evidence only" not in primitive:
            failures.append("primitive missing transcript-only evidence limit")

    for label, path in FILES.items():
        if not path.exists():
            failures.append(f"missing {label}: {path.relative_to(ROOT)}")
            continue
        content = read(path)
        if "agentic-engineering-loop-contract.md" not in content:
            failures.append(f"{path.relative_to(ROOT)} does not reference agentic engineering contract")

    codex = read(FILES["codex"]) if FILES["codex"].exists() else ""
    if "verify_agentic_engineering_loop_contract.py" not in codex:
        failures.append("CODEX.md verification standard missing agentic engineering verifier")

    source_files = [
        SOURCE_PACKAGE / "metadata.json",
        SOURCE_PACKAGE / "transcript.txt",
        SOURCE_PACKAGE / "video-context-ledger.md",
        SOURCE_PACKAGE / "uncertainty-report.md",
        SOURCE_PACKAGE / "analysis.md",
    ]
    for path in source_files:
        if not path.exists():
            failures.append(f"source evidence missing: {path.relative_to(ROOT)}")

    transcript = SOURCE_PACKAGE / "transcript.txt"
    if transcript.exists() and transcript.stat().st_size < 10000:
        failures.append("source transcript is too small to be a grounded package")

    metadata_path = SOURCE_PACKAGE / "metadata.json"
    if metadata_path.exists():
        try:
            metadata = json.loads(read(metadata_path))
        except json.JSONDecodeError as exc:
            failures.append(f"metadata.json invalid JSON: {exc}")
            metadata = {}
        if metadata.get("id") != "PzVV4X37ihg":
            failures.append("metadata.json has wrong YouTube id")
        if metadata.get("title") != "Stop Vibe Coding, Start Agentic Engineering – Micky":
            failures.append("metadata.json has unexpected title")

    uncertainty = SOURCE_PACKAGE / "uncertainty-report.md"
    if uncertainty.exists():
        report = read(uncertainty)
        for term in [
            "`observed_spoken`: 3280",
            "`observed_visual`: 0",
            "Frame extraction skipped because mode is transcript.",
            "OCR skipped because mode is transcript.",
        ]:
            if term not in report:
                failures.append(f"uncertainty report missing: {term}")

    allowed_routes = [
        "/source-to-skill-system",
        "/expert-composition-governor",
        "/self-evolve",
        "/system-audit",
        "/ai-employee-os",
        "/context-audit",
        "/extraction-governor-agent",
        "/domain-verifiability-map",
    ]
    for query in ROUTING_QUERIES:
        menu = run([sys.executable, "execution/command_menu.py", "search", query])
        router = run([sys.executable, "execution/workflow_router.py", "search", query])
        combined = menu + "\n" + router
        if not any(route in combined for route in allowed_routes):
            failures.append(f"routing query did not surface an agentic engineering route: {query}")

    if failures:
        print("AGENTIC ENGINEERING LOOP CONTRACT VERIFICATION FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("AGENTIC ENGINEERING LOOP CONTRACT VERIFICATION PASS")
    print(f"- ok: {PRIMITIVE.relative_to(ROOT)}")
    print(f"- ok: {SOURCE_PACKAGE.relative_to(ROOT)} transcript-backed source package")
    print("- ok: source-to-skill, expert-composition, self-evolve, system-audit, and CODEX references")
    print("- ok: routing checks surface agentic engineering routes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
