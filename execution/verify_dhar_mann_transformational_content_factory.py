#!/usr/bin/env python3
"""Verify the Dhar Mann Transformational Community Storytelling skill system."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "dhar-mann-transformational-storytelling"
WORKFLOW_NAME = "dhar-transformational-content-factory"
SKILL = ROOT / "skills" / SLUG
EXTRACTION = ROOT / "extractions" / SLUG
SOURCE_PACKAGES = {
    "Ht241IIaDCA": ROOT / "extractions" / "video-context" / "Ht241IIaDCA",
    "8GfgSz7LfLw": ROOT / "extractions" / "video-context" / "8GfgSz7LfLw",
}
CONDUCTOR = ROOT / ".agent" / "workflows" / f"{WORKFLOW_NAME}.md"
EXPERT_WORKFLOW = ROOT / ".agent" / "workflows" / "dhar-mann.md"
AGENT = ROOT / "agents" / "dhar-mann" / "AGENT.md"
CODEX_CONDUCTOR = (
    ROOT / ".agents" / "skills" / f"source-command-{WORKFLOW_NAME}" / "SKILL.md"
)
CODEX_EXPERT = ROOT / ".agents" / "skills" / "source-command-dhar-mann" / "SKILL.md"
CLAUDE_CONDUCTOR = ROOT / ".claude" / "commands" / f"{WORKFLOW_NAME}.md"
BEHAVIOR_PROOF = EXTRACTION / "behavior-proof.md"
SMOKE_FIXTURE = EXTRACTION / "fixtures" / "composite-smoke-test.json"
RECEIPT_ROOT = EXTRACTION / "production-receipts"
PLUGIN_READINESS = EXTRACTION / "plugin-readiness.md"
PLUGIN_SCORECARD = EXTRACTION / "plugin-readiness-scorecard-2026-07-30.md"
BAYER_MIRROR = ROOT / ".agent" / "workflows" / "bayer-mirror.md"
BAYER_AUTHORITY = (
    ROOT
    / "skills"
    / "david-bayer-elite-communication"
    / "workflows"
    / "magnetic-authority-content-system.md"
)
STANTON_CHANGE = (
    ROOT
    / "skills"
    / "andrew-stanton-audience-engineering"
    / "workflows"
    / "stanton-change-engine.md"
)
KOBI_AHA = (
    ROOT
    / "skills"
    / "kobi-brown-educational-virality"
    / "workflows"
    / "10-universal-aha-engine.md"
)

EXPECTED_WORKFLOWS = {
    "01-heart-transformation-north-star.md",
    "02-seen-heard-emotional-story-brief.md",
    "03-packaging-promise-covenant.md",
    "04-accelerated-youtube-beat-map.md",
    "05-audience-cogreenlight-loop.md",
    "06-recognized-before-transformed.md",
    "07-transform-without-preaching.md",
    "08-story-to-production-continuity.md",
    "09-production-capacity-learning-loop.md",
}

EXPECTED_PROMPTS = {
    "heart-transformation-north-star.md",
    "seen-heard-emotional-story-brief.md",
    "packaging-promise-covenant.md",
    "accelerated-youtube-beat-map.md",
    "audience-cogreenlight-loop.md",
    "recognized-before-transformed.md",
    "transform-without-preaching.md",
    "story-to-production-continuity.md",
    "production-capacity-learning-loop.md",
    "transformational-content-factory-run.md",
}

EXPECTED_RECEIPTS = {
    "PR-001-development-intake",
    "PR-002-published-story-continuity",
    "PR-003-capacity-learning",
}

REQUIRED_PROMPT_SECTIONS = {
    "## Role & Activation",
    "## Input Required",
    "## Execution Protocol",
    "## Output Contract",
    "## Output Skeleton",
    "## Quality Gate",
    "## Creative Latitude",
    "## Deploy When",
}

REQUIRED_CONTRACT_FIELDS = {
    "Source evidence",
    "Objective",
    "Components",
    "Step order",
    "Inputs",
    "Outputs",
    "Handoff summary",
    "Composition rule",
    "Human checkpoint",
    "Validation",
    "Behavior-changing proof",
    "Result surface",
    "Context policy",
    "Reuse hook",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def read_json(path: Path) -> object:
    return json.loads(read(path))


def run(args: list[str]) -> tuple[int, str]:
    completed = subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return completed.returncode, completed.stdout


def require_file(path: Path, failures: list[str]) -> None:
    if not path.is_file():
        failures.append(f"missing file: {path.relative_to(ROOT)}")
    elif path.stat().st_size == 0:
        failures.append(f"empty file: {path.relative_to(ROOT)}")


def verify_relative_links(path: Path, failures: list[str]) -> None:
    if not path.exists():
        return
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", read(path)):
        target = target.strip().split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "#")):
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            failures.append(
                f"broken relative link in {path.relative_to(ROOT)}: {target}"
            )


def verify_sources(failures: list[str], notes: list[str]) -> None:
    required = (
        "metadata.json",
        "transcript.vtt",
        "transcript.txt",
        "transcript_segments.json",
        "video-context-ledger.md",
        "video-context-ledger.json",
        "uncertainty-report.md",
        "frame-notes.md",
    )
    expected_words = {
        "Ht241IIaDCA": (7530, "MID"),
        "8GfgSz7LfLw": (4951, "THIN"),
    }

    for source_id, package in SOURCE_PACKAGES.items():
        for filename in required:
            require_file(package / filename, failures)

        transcript = package / "transcript.txt"
        if transcript.exists():
            words = len(read(transcript).split())
            expected, band = expected_words[source_id]
            if words != expected:
                failures.append(
                    f"{source_id} normalized transcript: expected {expected} words, got {words}"
                )
            notes.append(f"{source_id}: {words} normalized words / {band}")

        segments_path = package / "transcript_segments.json"
        if segments_path.exists():
            try:
                segments = read_json(segments_path)
            except json.JSONDecodeError as exc:
                failures.append(f"{source_id} invalid transcript segments: {exc}")
            else:
                if not isinstance(segments, list) or len(segments) < 100:
                    failures.append(f"{source_id} timestamped segments are implausibly short")
                else:
                    notes.append(f"{source_id}: {len(segments)} timestamped segments")

        ledger_path = package / "video-context-ledger.json"
        if ledger_path.exists():
            try:
                ledger = read_json(ledger_path)
            except json.JSONDecodeError as exc:
                failures.append(f"{source_id} invalid video context ledger: {exc}")
            else:
                spoken = [
                    row
                    for row in ledger
                    if isinstance(row, dict) and row.get("type") == "observed_spoken"
                ]
                if len(spoken) < 8:
                    failures.append(f"{source_id} needs at least eight observed_spoken anchors")
                if source_id == "8GfgSz7LfLw":
                    if not all(row.get("claim_status") == "SELF_REPORTED" for row in spoken):
                        failures.append(
                            "second-source operational rows must remain SELF_REPORTED"
                        )


def verify_manifests(failures: list[str], notes: list[str]) -> None:
    base_path = EXTRACTION / "manifest.json"
    delta_path = EXTRACTION / "manifest-delta-02.json"
    rollup_path = EXTRACTION / "manifest-rollup.json"
    for path in (base_path, delta_path, rollup_path):
        require_file(path, failures)
    if not all(path.exists() for path in (base_path, delta_path, rollup_path)):
        return

    try:
        base = read_json(base_path)
        delta = read_json(delta_path)
        rollup = read_json(rollup_path)
    except json.JSONDecodeError as exc:
        failures.append(f"invalid manifest JSON: {exc}")
        return

    expected_base = {
        "band": "MID",
        "corpus_words": 7530,
        "extension": False,
        "workflows": 7,
        "prompts_floor": 8,
        "orchestrator_eligible": False,
        "fidelity": "full",
    }
    for key, value in expected_base.items():
        if not isinstance(base, dict) or base.get(key) != value:
            failures.append(f"base manifest {key}: expected {value!r}")

    expected_delta = {
        "band": "THIN",
        "corpus_words": 4951,
        "extension": True,
        "workflows": 2,
        "prompts_floor": 2,
        "orchestrator_eligible": False,
        "fidelity": "low",
    }
    for key, value in expected_delta.items():
        if not isinstance(delta, dict) or delta.get(key) != value:
            failures.append(f"delta manifest {key}: expected {value!r}")

    if isinstance(delta, dict) and delta.get("yields") != {
        "patterns": 4,
        "hidden": 2,
        "exemplars": 3,
        "deliverables": 2,
        "stacking_hits": 1,
    }:
        failures.append("delta manifest yields changed from the source-earned extraction")

    shipped = rollup.get("shipped") if isinstance(rollup, dict) else {}
    corpus = rollup.get("corpus_words") if isinstance(rollup, dict) else {}
    if shipped != {
        "base_workflows": 7,
        "delta_workflows": 2,
        "total_workflows": 9,
        "base_prompts": 8,
        "delta_prompts": 2,
        "total_prompts": 10,
    }:
        failures.append("manifest rollup shipped counts are wrong")
    if corpus != {"base": 7530, "delta_02": 4951, "total": 12481}:
        failures.append("manifest rollup corpus counts are wrong")
    notes.append("manifests: base 7+8 / delta 2+2 / rollup 9+10")


def verify_skill_shape(failures: list[str], notes: list[str]) -> None:
    for path in (SKILL / "SKILL.md", SKILL / "genius.md", AGENT):
        require_file(path, failures)
    verify_relative_links(SKILL / "SKILL.md", failures)
    verify_relative_links(SKILL / "genius.md", failures)

    skill_text = read(SKILL / "SKILL.md") if (SKILL / "SKILL.md").exists() else ""
    for term in ('version: "1.1"', "workflows: 9", "8GfgSz7LfLw"):
        if term not in skill_text:
            failures.append(f"SKILL.md missing expansion marker: {term}")

    workflow_dir = SKILL / "workflows"
    workflow_files = {path.name for path in workflow_dir.glob("*.md")}
    if workflow_files != EXPECTED_WORKFLOWS:
        failures.append(
            "workflow set mismatch: "
            f"missing={sorted(EXPECTED_WORKFLOWS - workflow_files)}, "
            f"extra={sorted(workflow_files - EXPECTED_WORKFLOWS)}"
        )

    for path in sorted(workflow_dir.glob("*.md")):
        text = read(path)
        for term in (
            "## Inputs",
            "## Diagnose before treatment",
            "## Steps",
            "## Output contract",
            "## Output schema",
            "Execution prompt:",
            "## Adaptations",
            "## Quality gate",
        ):
            if term not in text:
                failures.append(f"{path.relative_to(ROOT)} missing {term}")

    prompt_dir = SKILL / "references" / "prompts-v2"
    prompt_files = {path.name for path in prompt_dir.glob("*.md")}
    if prompt_files != EXPECTED_PROMPTS:
        failures.append(
            "prompt set mismatch: "
            f"missing={sorted(EXPECTED_PROMPTS - prompt_files)}, "
            f"extra={sorted(prompt_files - EXPECTED_PROMPTS)}"
        )

    for path in sorted(prompt_dir.glob("*.md")):
        text = read(path)
        for term in (
            "source_prompt: born-v2",
            f"skill: {SLUG}",
            "standard: structure-pure-v2",
            "forged: born-v2",
        ):
            if term not in text:
                failures.append(f"{path.relative_to(ROOT)} missing frontmatter term: {term}")
        for section in REQUIRED_PROMPT_SECTIONS:
            if section not in text:
                failures.append(f"{path.relative_to(ROOT)} missing {section}")

    notes.append(f"skill shape: {len(workflow_files)} workflows / {len(prompt_files)} prompts")


def verify_contract_and_boundaries(failures: list[str]) -> None:
    contract = EXTRACTION / "SKILL-SYSTEM-CONTRACT.md"
    require_file(contract, failures)
    if contract.exists():
        text = read(contract)
        for field in REQUIRED_CONTRACT_FIELDS:
            if field not in text:
                failures.append(f"skill-system contract missing field: {field}")

    for path in (
        CONDUCTOR,
        EXPERT_WORKFLOW,
        CODEX_CONDUCTOR,
        CODEX_EXPERT,
        CLAUDE_CONDUCTOR,
        BAYER_MIRROR,
        BAYER_AUTHORITY,
        STANTON_CHANGE,
        KOBI_AHA,
    ):
        require_file(path, failures)

    if CONDUCTOR.exists():
        conductor = read(CONDUCTOR)
        for term in (
            "one Bayer mode",
            "one transformation route",
            "one body author",
            "Phase 4.5: Optional production continuity",
            "08-story-to-production-continuity.md",
            "09-production-capacity-learning-loop.md",
            "another studio's crew count",
            "directing, editing, screenplay",
            "Discovery",
            "Retention",
            "Connection",
            "Transformation",
            "therapy equivalence",
            "Plugin boundary",
            ".agent/workflows/bayer-mirror.md",
            "skills/david-bayer-elite-communication/workflows/magnetic-authority-content-system.md",
            "skills/andrew-stanton-audience-engineering/workflows/stanton-change-engine.md",
            "skills/kobi-brown-educational-virality/workflows/10-universal-aha-engine.md",
        ):
            if term not in conductor:
                failures.append(f"conductor missing boundary term: {term}")

    unexpected_plugin_dirs = (
        [path for path in (ROOT / "plugins").glob("*dhar*") if path.exists()]
        if (ROOT / "plugins").exists()
        else []
    )
    if unexpected_plugin_dirs:
        failures.append("premature Dhar plugin package exists")


def verify_reference_corpus(failures: list[str], notes: list[str]) -> None:
    corpus = EXTRACTION / "reference-corpus"
    pieces = [
        path
        for path in corpus.glob("*.txt")
        if path.is_file() and path.stat().st_size > 0
    ]
    if len(pieces) < 2:
        failures.append("blind-pass reference corpus needs at least two published pieces")
        return
    for piece in pieces:
        text = read(piece)
        if "Source: https://www.youtube.com/watch?v=" not in text:
            failures.append(f"reference piece lacks provenance URL: {piece.relative_to(ROOT)}")
        if len(text.split()) < 500:
            failures.append(f"reference piece is implausibly short: {piece.relative_to(ROOT)}")
    notes.append(f"published reference pieces: {len(pieces)}")


def verify_behavior_proof(failures: list[str], notes: list[str]) -> None:
    require_file(SMOKE_FIXTURE, failures)
    require_file(BEHAVIOR_PROOF, failures)

    if SMOKE_FIXTURE.exists():
        try:
            fixture = read_json(SMOKE_FIXTURE)
        except json.JSONDecodeError as exc:
            failures.append(f"invalid composite smoke fixture: {exc}")
        else:
            if not isinstance(fixture, dict):
                failures.append("composite smoke fixture must be a JSON object")
            else:
                if fixture.get("provenance_status") != "PROVENANCE MISSING":
                    failures.append("smoke fixture must expose missing provenance")
                if fixture.get("real_lived_scene") is not None:
                    failures.append("smoke fixture must not invent a lived scene")

    if BEHAVIOR_PROOF.exists():
        proof = read(BEHAVIOR_PROOF)
        for term in (
            "## Baseline behavior",
            "## Source mechanics activated",
            "### HEART Transformation Card",
            "### Viewer Transformation Contract",
            "### Packaging Integrity Packet",
            "### Accelerated Beat Map",
            "### Audience Co-Greenlight Loop",
            "### Four-Scoreboard Measurement Plan",
            "### Composition Ledger",
            "## Behavior delta",
            "[Provenance missing: full body blocked]",
            "Therapy equivalence or guaranteed outcome: **ABSENT**",
            "Invented Farrice experience: **ABSENT**",
        ):
            if term not in proof:
                failures.append(f"behavior proof missing invariant: {term}")
        notes.append("original behavior fixture preserved")


def verify_receipts(failures: list[str], notes: list[str]) -> None:
    require_file(RECEIPT_ROOT / "README.md", failures)
    receipt_dirs = {path.name for path in RECEIPT_ROOT.iterdir() if path.is_dir()} if RECEIPT_ROOT.exists() else set()
    if receipt_dirs != EXPECTED_RECEIPTS:
        failures.append(
            f"receipt set mismatch: expected {sorted(EXPECTED_RECEIPTS)}, got {sorted(receipt_dirs)}"
        )
        return

    routing_path = ROOT / ".agent" / "routing-intelligence.json"
    require_file(routing_path, failures)
    routing_ids: set[str] = set()
    if routing_path.exists():
        try:
            routing = read_json(routing_path)
        except json.JSONDecodeError as exc:
            failures.append(f"routing-intelligence.json is invalid: {exc}")
        else:
            if isinstance(routing, dict):
                routing_ids = {
                    row.get("routing_id")
                    for row in routing.get("routing_decisions", [])
                    if isinstance(row, dict)
                    and row.get("workflow_used") == WORKFLOW_NAME
                    and row.get("routing_id")
                }

    seen_ids: set[str] = set()
    seen_routing: set[str] = set()
    expected_finalization = {
        "PR-001-development-intake": (7.0, "MARGINAL"),
        "PR-002-published-story-continuity": (7.6, "PASS"),
        "PR-003-capacity-learning": (7.6, "PASS"),
    }
    for directory_name in sorted(EXPECTED_RECEIPTS):
        directory = RECEIPT_ROOT / directory_name
        json_path = directory / "receipt.json"
        md_path = directory / "receipt.md"
        output_path = directory / "output.md"
        for path in (json_path, md_path, output_path):
            require_file(path, failures)
        if not json_path.exists():
            continue

        try:
            receipt = read_json(json_path)
        except json.JSONDecodeError as exc:
            failures.append(f"{directory_name} invalid receipt JSON: {exc}")
            continue
        if not isinstance(receipt, dict):
            failures.append(f"{directory_name} receipt must be a JSON object")
            continue

        receipt_id = receipt.get("receipt_id")
        if receipt_id != directory_name or receipt_id in seen_ids:
            failures.append(f"{directory_name} receipt_id is missing, mismatched, or duplicated")
        seen_ids.add(str(receipt_id))

        evidence_class = str(receipt.get("evidence_class") or "")
        if "COMPONENT_VALIDATION" not in evidence_class:
            failures.append(f"{directory_name} overstates its evidence class")
        if (receipt.get("input") or {}).get("synthetic") is not False:
            failures.append(f"{directory_name} input must be real source material")
        if receipt.get("promotion_credit") != "COMPONENT_VALIDATION_ONLY":
            failures.append(f"{directory_name} must not claim plugin-promotion proof")
        if receipt.get("human_felt_verdict") != "PENDING":
            failures.append(f"{directory_name} must keep human felt verdict pending")
        if "NOT_PUBLISHED" not in str(receipt.get("publication")):
            failures.append(f"{directory_name} derived output must remain not published")

        route = receipt.get("route") or {}
        if route.get("owner") != SLUG:
            failures.append(f"{directory_name} has the wrong function owner")
        if route.get("workflow") not in {
            "08-story-to-production-continuity",
            "09-production-capacity-learning-loop",
        }:
            failures.append(f"{directory_name} has an unsupported component route")

        checks = receipt.get("checks") or {}
        for key in ("provenance", "claim_labels", "output_contract", "unsupported_gaps_exposed"):
            if checks.get(key) != "PASS":
                failures.append(f"{directory_name} check {key} did not pass")

        finalization = receipt.get("finalization") or {}
        expected_composite, expected_gate = expected_finalization[directory_name]
        if finalization.get("composite") != expected_composite:
            failures.append(f"{directory_name} finalization composite is inaccurate")
        if finalization.get("quality_gate") != expected_gate:
            failures.append(f"{directory_name} finalization gate is inaccurate")

        routing_id = receipt.get("routing_id")
        if not isinstance(routing_id, str) or not routing_id.startswith("rt_"):
            failures.append(f"{directory_name} lacks a routing receipt")
        elif routing_id not in routing_ids:
            failures.append(f"{directory_name} routing receipt is not in routing intelligence")
        elif routing_id in seen_routing:
            failures.append(f"{directory_name} reuses another receipt's routing id")
        else:
            seen_routing.add(routing_id)

        outputs = receipt.get("outputs") or []
        if len(outputs) != 1:
            failures.append(f"{directory_name} must name exactly one primary output")
        for output in outputs:
            resolved = ROOT / output
            if not resolved.exists():
                failures.append(f"{directory_name} output does not exist: {output}")

        output_text = read(output_path) if output_path.exists() else ""
        if "SELF-REPORTED" not in output_text and directory_name != "PR-002-published-story-continuity":
            failures.append(f"{directory_name} lost its self-reported claim boundary")

    if len(seen_routing) != 3:
        failures.append("three distinct finalized routing receipts are required")
    notes.append("production receipts: 3 component-validation runs / 3 routing records")


def parse_plugin_row(report: str) -> tuple[int, str] | None:
    pattern = re.compile(
        rf"\| `{re.escape(WORKFLOW_NAME)}` \|(?:[^|]*\|){{6}}\s*(\d+)\s*\|\s*([^|]+?)\s*\|"
    )
    match = pattern.search(report)
    if not match:
        return None
    return int(match.group(1)), match.group(2).strip()


def verify_plugin_readiness(failures: list[str], notes: list[str]) -> None:
    require_file(PLUGIN_READINESS, failures)
    require_file(PLUGIN_SCORECARD, failures)

    code, live_report = run(
        [sys.executable, "execution/plugin_readiness_audit.py", WORKFLOW_NAME, "--stdout"]
    )
    if code != 0:
        failures.append(f"plugin readiness audit failed:\n{live_report}")
        return
    live = parse_plugin_row(live_report)
    if live is None:
        failures.append("could not parse live plugin readiness row")
        return
    score, decision = live
    if score != 54 or decision != "KEEP AS WORKFLOW":
        failures.append(
            f"plugin readiness changed: expected 54 / KEEP AS WORKFLOW, got {score} / {decision}"
        )

    for path in (PLUGIN_READINESS, PLUGIN_SCORECARD):
        if path.exists():
            text = read(path)
            if "54" not in text or "KEEP AS WORKFLOW" not in text:
                failures.append(f"{path.relative_to(ROOT)} does not match live readiness")

    if PLUGIN_READINESS.exists():
        text = read(PLUGIN_READINESS)
        for term in (
            "component validation",
            "not three independent creator runs",
            "cold-start",
            "felt verdict",
            "No plugin package",
        ):
            if term not in text:
                failures.append(f"plugin readiness missing evidence boundary: {term}")
    notes.append("plugin readiness: 54/100 / KEEP AS WORKFLOW")


def verify_router(failures: list[str], notes: list[str]) -> None:
    query = (
        "turn an approved transformation story into production units and "
        "department handoffs without losing the viewer shift"
    )
    code, output = run([sys.executable, "execution/workflow_router.py", "search", query])
    if code != 0:
        failures.append(f"workflow_router failed:\n{output}")
    elif "/dhar-transformational-content-factory" not in output:
        failures.append("natural-language routing did not surface the Dhar factory")
    else:
        notes.append("natural-language production-continuity route surfaces Dhar factory")

    direct_query = "dhar transformational content factory"
    code, output = run([sys.executable, "execution/command_menu.py", "search", direct_query])
    if code != 0:
        failures.append(f"command_menu failed:\n{output}")
    elif "/dhar-transformational-content-factory" not in output:
        failures.append("direct command search did not surface the Dhar factory")
    else:
        notes.append("direct command search surfaces Dhar factory")


def main() -> int:
    failures: list[str] = []
    notes: list[str] = []

    verify_sources(failures, notes)
    verify_manifests(failures, notes)
    verify_skill_shape(failures, notes)
    verify_contract_and_boundaries(failures)
    verify_reference_corpus(failures, notes)
    verify_behavior_proof(failures, notes)
    verify_receipts(failures, notes)
    verify_plugin_readiness(failures, notes)
    verify_router(failures, notes)

    if failures:
        print("Dhar Mann Transformational Content Factory verification: FAIL")
        for failure in failures:
            print(f"- {failure}")
        for note in notes:
            print(f"- NOTE: {note}")
        return 1

    print("Dhar Mann Transformational Content Factory verification: PASS")
    for note in notes:
        print(f"- {note}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
