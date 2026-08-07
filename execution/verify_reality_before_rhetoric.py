#!/usr/bin/env python3
"""Verify the capability-preserving Reality Before Rhetoric restoration."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
FIXTURE_ROOT = ROOT / "execution" / "fixtures" / "reality_before_rhetoric"
V1_FIXTURE = FIXTURE_ROOT / "regression-set.json"
ANTI_SHACKLE_FIXTURE = FIXTURE_ROOT / "anti-shackle-regression-set.json"
EXPECTED_V1_HASH = "20fd35a3dfb99c088d481649a71a73eecfef8afaec73cffb11e288d263ce6077"

CONSTITUTION = (
    ROOT
    / "semantic_libraries"
    / "antigravity"
    / "primitives"
    / "anti-shackle-constitution.md"
)
PROTOCOL = (
    ROOT
    / "semantic_libraries"
    / "antigravity"
    / "primitives"
    / "reality-before-rhetoric-contract.md"
)
HELPER = ROOT / "execution" / "reality_before_rhetoric.py"
LAUNCHPAD = ROOT / "execution" / "co_creative_launchpad.py"
PACKET = (
    ROOT
    / "docs"
    / "mission-artifacts"
    / "reality-before-rhetoric"
    / "restoration-agentic-engineering-packet.md"
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(read(path))


def v1_accepted_behavior_hash(payload: dict[str, Any]) -> str:
    frozen_surface = {
        "schema_version": payload.get("schema_version"),
        "fixtures": [
            {
                "id": fixture.get("id"),
                "accepted_behavior": fixture.get("accepted_behavior"),
            }
            for fixture in payload.get("fixtures", [])
        ],
        "bypass_controls": [
            {
                "id": control.get("id"),
                "expected_activation": control.get("expected_activation"),
                "reason": control.get("reason"),
            }
            for control in payload.get("bypass_controls", [])
        ],
    }
    canonical = json.dumps(
        frozen_surface,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def anti_shackle_hash(payload: dict[str, Any]) -> str:
    frozen_surface = {
        key: value
        for key, value in payload.items()
        if key != "accepted_behavior_sha256"
    }
    canonical = json.dumps(
        frozen_surface,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def run_launchpad(query: str, route: str) -> dict[str, Any]:
    completed = subprocess.run(
        [
            sys.executable,
            str(LAUNCHPAD),
            query,
            "--route",
            route,
            "--json",
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if completed.returncode != 0:
        raise AssertionError(completed.stdout)
    return json.loads(completed.stdout)


def require_terms(
    label: str, content: str, terms: list[str] | tuple[str, ...], failures: list[str]
) -> None:
    for term in terms:
        if term not in content:
            failures.append(f"{label} missing required term: {term}")


def forbid_terms(
    label: str, content: str, terms: list[str] | tuple[str, ...], failures: list[str]
) -> None:
    for term in terms:
        if term in content:
            failures.append(f"{label} retains forbidden enforcement term: {term}")


def main() -> int:
    failures: list[str] = []
    notes: list[str] = []

    for path in (
        V1_FIXTURE,
        ANTI_SHACKLE_FIXTURE,
        CONSTITUTION,
        PROTOCOL,
        HELPER,
        LAUNCHPAD,
        PACKET,
    ):
        if not path.exists():
            failures.append(f"missing required file: {path.relative_to(ROOT)}")

    if V1_FIXTURE.exists():
        try:
            v1 = load_json(V1_FIXTURE)
        except json.JSONDecodeError as exc:
            failures.append(f"invalid frozen V1 fixture JSON: {exc}")
        else:
            digest = v1_accepted_behavior_hash(v1)
            if v1.get("freeze_status") != "frozen":
                failures.append("V1 fixture corpus is no longer frozen")
            if v1.get("accepted_behavior_sha256") != EXPECTED_V1_HASH:
                failures.append("V1 stored hash changed")
            if digest != EXPECTED_V1_HASH:
                failures.append(f"V1 accepted behavior drifted: {digest}")
            notes.append(f"frozen V1 historical hash preserved: {digest}")

    anti: dict[str, Any] = {}
    if ANTI_SHACKLE_FIXTURE.exists():
        try:
            anti = load_json(ANTI_SHACKLE_FIXTURE)
        except json.JSONDecodeError as exc:
            failures.append(f"invalid anti-shackle fixture JSON: {exc}")
        else:
            if anti.get("schema_version") != "reality-before-rhetoric-anti-shackle/v1":
                failures.append("unexpected anti-shackle fixture schema")
            if anti.get("freeze_status") != "frozen":
                failures.append("anti-shackle fixture is not frozen")
            digest = anti_shackle_hash(anti)
            if anti.get("accepted_behavior_sha256") != digest:
                failures.append(
                    "anti-shackle accepted-behavior hash mismatch: "
                    f"stored={anti.get('accepted_behavior_sha256')!r}, computed={digest}"
                )

    if CONSTITUTION.exists():
        constitution = read(CONSTITUTION)
        require_terms(
            "Anti-Shackle Constitution",
            constitution,
            (
                "Freedom Is The Default",
                "Gate The Claim, Not Cognition",
                "No keyword or route name alone may trigger enforcement",
                "fabricated fact",
                "Proof promotion",
                "private material",
                "without permission",
                "three independent production receipts",
                "immediately returns to `SHADOW`",
            ),
            failures,
        )

    if PROTOCOL.exists():
        protocol = read(PROTOCOL)
        require_terms(
            "Reality Before Rhetoric optional practice",
            protocol,
            (
                "optional co-creative depth practice",
                "OPEN",
                "SHADOW",
                "ENFORCE",
                "fabricated fact",
                "proof promotion",
                "private",
                "permission",
                "supported adjacent work continues",
            ),
            failures,
        )
        forbid_terms(
            "Reality Before Rhetoric optional practice",
            protocol,
            ("Authorized artifact tier", "maximum five", "Activate when"),
            failures,
        )

    if HELPER.exists():
        helper = read(HELPER)
        if "FROZEN V1 EXPERIMENT" not in helper:
            failures.append("historical V1 helper is not visibly marked inactive")

    if LAUNCHPAD.exists():
        launchpad_source = read(LAUNCHPAD)
        if "reality_before_rhetoric" in launchpad_source:
            failures.append("Co-Creative Launchpad still imports or emits RBR")

    safe_passes = 0
    for control in anti.get("safe_controls", []):
        expected = control.get("accepted_behavior", {})
        if expected.get("launchpad_rbr_field") is not False:
            failures.append(f"{control.get('id')} must freeze no launchpad RBR field")
            continue
        try:
            packet = run_launchpad(control["query"], control["route"])
        except (AssertionError, json.JSONDecodeError, KeyError) as exc:
            failures.append(f"{control.get('id')} launchpad failure: {exc}")
            continue
        if "reality_before_rhetoric" in packet:
            failures.append(f"{control.get('id')} still receives a top-level RBR gate")
            continue
        if "reality_before_rhetoric" in packet.get("handoff", {}):
            failures.append(f"{control.get('id')} still receives an RBR handoff")
            continue
        safe_passes += 1

    vetoes = anti.get("hard_veto_controls", [])
    veto_ids = {item.get("id") for item in vetoes}
    if veto_ids != {"truth", "proof", "privacy", "permission"}:
        failures.append(f"hard-veto set drifted: {sorted(str(v) for v in veto_ids)}")
    for item in vetoes:
        if item.get("affected_unit") != "claim-or-material":
            failures.append(f"{item.get('id')} is not claim/material-local")
        if item.get("supported_adjacent_work_continues") is not True:
            failures.append(f"{item.get('id')} does not preserve adjacent work")

    surfaces = {
        "Launchpad contract": ROOT
        / "semantic_libraries"
        / "antigravity"
        / "primitives"
        / "co-creative-launchpad-contract.md",
        "High-Taste workflow": ROOT / ".agent" / "workflows" / "high-taste-writing-os.md",
        "High-Taste contract": ROOT
        / "semantic_libraries"
        / "antigravity"
        / "primitives"
        / "high-taste-writing-os-contract.md",
        "Farrice Content OS": ROOT / ".agent" / "workflows" / "farrice-content-os.md",
        "Dhar factory": ROOT
        / ".agent"
        / "workflows"
        / "dhar-transformational-content-factory.md",
        "Dhar expert bridge": ROOT / ".agent" / "workflows" / "dhar-mann.md",
        "Seen-Heard workflow": ROOT
        / "skills"
        / "dhar-mann-transformational-storytelling"
        / "workflows"
        / "02-seen-heard-emotional-story-brief.md",
        "Seen-Heard prompt": ROOT
        / "skills"
        / "dhar-mann-transformational-storytelling"
        / "references"
        / "prompts-v2"
        / "seen-heard-emotional-story-brief.md",
    }
    forbidden_by_surface = {
        "Launchpad contract": ("reality_before_rhetoric", "activation check"),
        "High-Taste workflow": ("authorized_artifact_tier", "Phase 2.5: Reality Before Rhetoric"),
        "High-Taste contract": ("Reality Before Rhetoric activation", "Source Depth Packet"),
        "Farrice Content OS": (
            "source_depth_packet:",
            "authorized_artifact_tier:",
            "Phase 2.25 Reality Before Rhetoric",
        ),
        "Dhar factory": ("authorized_artifact_tier", "Activate Reality Before Rhetoric"),
        "Dhar expert bridge": ("artifact tier is `draft`",),
        "Seen-Heard workflow": ("AUTHORIZED ARTIFACT TIER", "SOURCE DEPTH:"),
        "Seen-Heard prompt": ("AUTHORIZED ARTIFACT TIER", "SOURCE DEPTH:"),
    }
    for label, path in surfaces.items():
        if not path.exists():
            failures.append(f"missing active surface: {path.relative_to(ROOT)}")
            continue
        forbid_terms(label, read(path), forbidden_by_surface[label], failures)

    optional_surfaces = {
        "Dhar skill": ROOT / "skills" / "dhar-mann-transformational-storytelling" / "SKILL.md",
        "Dhar factory": surfaces["Dhar factory"],
    }
    for label, path in optional_surfaces.items():
        if path.exists():
            require_terms(label, read(path), ("Reality Before Rhetoric", "optional"), failures)

    capability_passes = 0
    for item in anti.get("capability_preservation", []):
        path = ROOT / item.get("path", "")
        if not path.exists():
            failures.append(f"missing capability surface: {item.get('path')}")
            continue
        before = len(failures)
        require_terms(
            item.get("path", "capability surface"),
            read(path),
            tuple(item.get("required_terms", [])),
            failures,
        )
        if len(failures) == before:
            capability_passes += 1

    if failures:
        print("RBR ANTI-SHACKLE RESTORATION: FAIL")
        for failure in failures:
            print(f"- {failure}")
        print(
            f"- notes: safe controls {safe_passes}/{len(anti.get('safe_controls', []))}; "
            f"capability surfaces {capability_passes}/{len(anti.get('capability_preservation', []))}"
        )
        for note in notes:
            print(f"- note: {note}")
        return 1

    print("RBR ANTI-SHACKLE RESTORATION: PASS")
    print(f"- safe controls: {safe_passes}/{len(anti.get('safe_controls', []))}")
    print("- hard vetoes: truth, proof, privacy, permission")
    print(
        "- capability preservation: "
        f"{capability_passes}/{len(anti.get('capability_preservation', []))}"
    )
    for note in notes:
        print(f"- {note}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
