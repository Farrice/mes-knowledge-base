#!/usr/bin/env python3
"""Deterministically verify the cold Expert Practice OS skill-system build.

This is a structural gate, not runtime proof. It verifies the approved files,
source binding, prompt contracts, closed routes, fixtures, and absence of public
registration surfaces. Passing this file may be recorded only as
ORCHESTRATOR_ATTESTED until a detached runtime receipt exists.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
SKILL = ROOT / "skills" / "expert-practice-os"
SUNNY = ROOT / "skills" / "sunny-lenarduzzi-youtube"
SOURCE = ROOT / "extractions" / "video-context" / "4HqO0h13MX4"
SOURCE_HASH = "f9579ec33b60b5094ce0eb00b4619158eadbbdc3e1dd8ab5bd5c4af66daf8a29"

EXPECTED_SKILL_FILES = {
    "SKILL.md",
    "genius.md",
    "workflows/01-diagnose-and-route-practice.md",
    "references/practitioner-protocol-packet.md",
    "references/route-ownership-map.md",
    "references/proof-state-schema.md",
    "references/economics-activation-contract.md",
    "references/adapters/ai-consulting.md",
    "references/adapters/life-coaching.md",
    "references/adapters/solopreneurship.md",
    "references/adapters/claims-safety.md",
    "references/prompts-v2/expert-practice-routing-receipt.md",
    "tests/verify_skill_system.py",
    "tests/verify_behavior_run.py",
    "tests/test_verify_behavior_run.py",
    "tests/fixtures/acceptance-cases.jsonl",
    "tests/fixtures/final-10-ai-consulting/practitioner-protocol-packet.json",
    "tests/fixtures/final-10-ai-consulting/expected-route.json",
    "tests/fixtures/final-10-ai-consulting/acceptance-contract.json",
    "tests/fixtures/final-10-ai-consulting/proof-boundary.md",
    "tests/fixtures/life-design-coach-pop/practitioner-protocol-packet.json",
    "tests/fixtures/life-design-coach-pop/expected-route.json",
    "tests/fixtures/life-design-coach-pop/acceptance-contract.json",
    "tests/fixtures/life-design-coach-pop/proof-boundary.md",
}

SUNNY_ADDITIONS = {
    "workflows/04-profitable-offer-prototype.md",
    "references/source-delta-4HqO0h13MX4.md",
    "references/prompts-v2/profitable-offer-prototype.md",
}

AUTHORITY_SURFACES = (
    ROOT / "agents" / "expert-practice-os",
    ROOT / ".agent" / "workflows" / "expert-practice-os.md",
    ROOT / ".claude" / "commands" / "expert-practice-os.md",
    ROOT / ".agents" / "skills" / "source-command-expert-practice-os",
    ROOT / ".agents" / "cold-skills" / "expert-practice-os",
)

ROUTING_REGISTRIES = (
    ROOT / "SKILL_INDEX.md",
    ROOT / "AGENT_INDEX.md",
    ROOT / "DOMAIN_REGISTRY.md",
    ROOT / "SLASH_COMMANDS.md",
    ROOT / ".agent" / "arsenal-index.json",
)

PROMPT_PATHS = {
    "skills/expert-practice-os/references/prompts-v2/expert-practice-routing-receipt.md",
    "skills/sunny-lenarduzzi-youtube/references/prompts-v2/profitable-offer-prototype.md",
}


class Gate:
    def __init__(self) -> None:
        self.passed = 0
        self.failures: list[str] = []

    def check(self, condition: bool, label: str, detail: str = "") -> None:
        if condition:
            self.passed += 1
            print(f"PASS  {label}")
        else:
            message = f"{label}: {detail}" if detail else label
            self.failures.append(message)
            print(f"FAIL  {message}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load(path: Path) -> Any:
    return json.loads(read(path))


def visible_files(path: Path) -> set[str]:
    return {
        str(item.relative_to(path))
        for item in path.rglob("*")
        if item.is_file() and "__pycache__" not in item.parts and item.suffix != ".pyc"
    }


def require_tokens(gate: Gate, path: Path, tokens: tuple[str, ...], label: str) -> None:
    text = read(path)
    missing = [token for token in tokens if token not in text]
    gate.check(not missing, label, f"missing {missing}")


def main() -> int:
    gate = Gate()

    actual_files = visible_files(SKILL)
    gate.check(
        actual_files == EXPECTED_SKILL_FILES,
        "exact cold Expert Practice OS inventory",
        f"missing={sorted(EXPECTED_SKILL_FILES - actual_files)} extra={sorted(actual_files - EXPECTED_SKILL_FILES)}",
    )
    gate.check(
        all((SUNNY / path).is_file() for path in SUNNY_ADDITIONS),
        "three additive Sunny POP files exist",
    )

    source_hash = hashlib.sha256((SOURCE / "transcript_segments.json").read_bytes()).hexdigest()
    gate.check(source_hash == SOURCE_HASH, "frozen transcript hash", source_hash)
    source_delta = read(SUNNY / "references/source-delta-4HqO0h13MX4.md")
    source_anchors = (
        "seg-38 to seg-71",
        "seg-89 to seg-94",
        "seg-99 to seg-117",
        "seg-122 to seg-159",
        "seg-809 to seg-821",
        "seg-822 to seg-838",
        "seg-846 to seg-859",
        "seg-895 to seg-937",
        "seg-906 to seg-909",
        "seg-969 to seg-978",
        "seg-995 to seg-1008",
        "seg-1010 to seg-1034",
        "SOURCE_REPORTED",
        SOURCE_HASH,
    )
    gate.check(all(token in source_delta for token in source_anchors), "source delta is hash- and segment-bound")

    source_verifier = subprocess.run(
        [sys.executable, "execution/verify_video_context_source_package.py", str(SOURCE)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    gate.check(source_verifier.returncode == 0, "canonical video source verifier", source_verifier.stdout + source_verifier.stderr)

    skill_text = read(SKILL / "SKILL.md")
    gate.check("status: cold-unregistered" in skill_text and "routing: menu-exempt" in skill_text, "cold skill frontmatter")
    gate.check("workflows: 1" in skill_text, "thin one-workflow conductor")
    gate.check(
        all(token in skill_text for token in ("AI_CONSULTING", "LIFE_COACHING_OR_LIFE_DESIGN", "SOLOPRENEURSHIP", "HOLD_UNREGISTERED_ADAPTER")),
        "closed practice enum and unregistered-adapter hold",
    )
    gate.check("first candidate public configuration" in skill_text and "Final 10% Diagnostic" in skill_text, "Farrice-first lane without universal payload transfer")

    sunny_skill = read(SUNNY / "SKILL.md")
    gate.check("workflows: 4" in sunny_skill and "04-profitable-offer-prototype" in sunny_skill, "Sunny workflow count and pointer")
    gate.check("catalog presence does not authorize" in sunny_skill, "prompt catalog is non-authoritative")

    conductor_workflow = SKILL / "workflows/01-diagnose-and-route-practice.md"
    sunny_workflow = SUNNY / "workflows/04-profitable-offer-prototype.md"
    gate.check(len(read(conductor_workflow).splitlines()) <= 250, "conductor stays thin")
    require_tokens(gate, conductor_workflow, ("menu_exempt:", "### Hold branch", "loaded_context_paths:", "truth_counters:", "economics_model: null", "proof_reuse_requested: false"), "conductor workflow contract")
    require_tokens(gate, sunny_workflow, ("menu_exempt:", "Authority.io / Sunny-led", "### Hold branch", "sent / held / sold / collected", "LOCKED_PRE_RUNTIME"), "Sunny POP workflow contract")

    prompt_sections = (
        "## Role & Activation",
        "## Input Required",
        "## Execution Protocol",
        "## Output Contract",
        "## Output Skeleton",
        "## Quality Gate",
    )
    for path in sorted(PROMPT_PATHS):
        prompt = ROOT / path
        require_tokens(gate, prompt, prompt_sections, f"born-v2 prompt structure: {path}")
    require_tokens(
        gate,
        SKILL / "references/prompts-v2/expert-practice-routing-receipt.md",
        ("loaded_context_paths:", "truth_counters:", "economics_model: null", "proof_reuse_requested: false", "### Hold branch"),
        "routing prompt/verifier field parity",
    )

    proof_schema = read(SKILL / "references/proof-state-schema.md")
    gate.check(
        all(token in proof_schema for token in ("RUNTIME_OBSERVED", "ORCHESTRATOR_ATTESTED", "OPERATOR_ATTESTED", "registration_eligible=true", "detached")),
        "proof provenance and registration gates",
    )
    economics = read(SKILL / "references/economics-activation-contract.md")
    gate.check(
        all(token in economics for token in ("No annual or monthly economics workflow exists", "Detached `RUNTIME_OBSERVED`", "Stage-appropriate operating inputs", "Explicit human approval", "LOCKED_PRE_RUNTIME")),
        "economics remains activation-gated",
    )
    gate.check(not list((SKILL / "workflows").glob("*economics*")) and not list((SKILL / "references/prompts-v2").glob("*economics*")), "no premature economics workflow or prompt")

    gate.check(not any(path.exists() for path in AUTHORITY_SURFACES), "no command, agent, mirror, or public workflow surface")
    registry_hits = [str(path.relative_to(ROOT)) for path in ROUTING_REGISTRIES if path.exists() and "expert-practice-os" in read(path)]
    sunny_registry_hits = [str(path.relative_to(ROOT)) for path in ROUTING_REGISTRIES if path.exists() and "04-profitable-offer-prototype" in read(path)]
    gate.check(not registry_hits and not sunny_registry_hits, "no routing or arsenal registration", f"expert={registry_hits} sunny={sunny_registry_hits}")

    prompt_index = load(ROOT / ".agent/prompt-index.json")
    indexed = {entry.get("path") for entry in prompt_index.get("entries", []) if entry.get("kind") == "prompt-v2"}
    gate.check(PROMPT_PATHS.issubset(indexed), "cold prompts are discoverable in non-authoritative prompt catalog", f"missing={sorted(PROMPT_PATHS - indexed)}")
    gate.check(
        all("BEGIN:execution-prompts" in read(path) for path in (SKILL / "SKILL.md", SUNNY / "SKILL.md")),
        "generated prompt pointers are wired",
    )

    architecture_meta = load(SOURCE / "architecture-checkpoint.metadata.json")
    contract_meta = load(SOURCE / "skill-system-contract.metadata.json")
    gate.check(
        architecture_meta.get("status") == "cold_build_complete_runtime_pending"
        and contract_meta.get("status") == "cold_build_complete_runtime_pending",
        "checkpoint metadata records cold completion only",
    )
    gate.check(
        architecture_meta.get("publicly_active") is False
        and contract_meta.get("publicly_active") is False
        and contract_meta.get("prompt_asset_catalog_allowed") is True,
        "metadata preserves cold/public boundary",
    )

    cases = [json.loads(line) for line in read(SKILL / "tests/fixtures/acceptance-cases.jsonl").splitlines() if line.strip()]
    gate.check(len(cases) == 21 and len({case["id"] for case in cases}) == 21, "21 unique adversarial cases")

    fixture_routes: list[dict[str, Any]] = []
    json_failures: list[str] = []
    for fixture_dir in sorted((SKILL / "tests/fixtures").iterdir()):
        if not fixture_dir.is_dir():
            continue
        for name in ("practitioner-protocol-packet.json", "expected-route.json", "acceptance-contract.json"):
            try:
                load(fixture_dir / name)
            except (OSError, json.JSONDecodeError) as exc:
                json_failures.append(f"{fixture_dir.name}/{name}: {exc}")
        fixture_routes.append(load(fixture_dir / "expected-route.json"))
    gate.check(not json_failures and len(fixture_routes) == 2, "two complete JSON fixture families", "; ".join(json_failures))
    if len(fixture_routes) == 2:
        gate.check(
            fixture_routes[0]["practice_type"] != fixture_routes[1]["practice_type"]
            and fixture_routes[0]["selected_lane_owner"] != fixture_routes[1]["selected_lane_owner"]
            and fixture_routes[0]["terminal_decision"] != fixture_routes[1]["terminal_decision"],
            "fixtures diverge by practice, owner, and terminal decision",
        )
        selected_paths = {path for route in fixture_routes for path in route["selected_workflow_paths"]}
        missing_selected = [path for path in selected_paths if not (ROOT / path).exists()]
        gate.check(not missing_selected, "all fixture-selected workflow paths exist", str(missing_selected))

    symlinks = [str(path.relative_to(ROOT)) for base in (SKILL, *(SUNNY / path for path in SUNNY_ADDITIONS)) for path in ([base] if base.is_symlink() else [])]
    gate.check(not symlinks, "cold additions contain no symlinks", str(symlinks))

    print()
    if gate.failures:
        print(f"COLD SKILL SYSTEM: FAIL ({gate.passed} checks passed, {len(gate.failures)} failed)")
        for failure in gate.failures:
            print(f"- {failure}")
        return 1

    print(f"COLD SKILL SYSTEM: PASS ({gate.passed} checks)")
    print("Proof class: ORCHESTRATOR_ATTESTED (structural/fixture evidence only)")
    print("Registration: false | Economics: locked | External actions: none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
