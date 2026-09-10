#!/usr/bin/env python3
"""Outcome recipes for the Antigravity intent-to-outcome layer."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from typing import Iterable


@dataclass(frozen=True)
class OutcomeRecipe:
    name: str
    signals: tuple[str, ...]
    primary_route: str
    support_gates: tuple[str, ...]
    artifact: str
    verifiers: tuple[str, ...]
    plugin_ladder: str


RECIPES: dict[str, OutcomeRecipe] = {
    "kishotenketsu-contrast-storytelling": OutcomeRecipe(
        name="kishotenketsu-contrast-storytelling",
        signals=(
            "kishotenketsu",
            "contrast storytelling",
            "contrast driven storytelling",
            "variable over villain",
            "process as plot",
            "world invitation",
            "changed-world messaging",
            "perspective shift",
            "integration over victory",
        ),
        primary_route="kishotenketsu-contrast-storytelling",
        support_gates=(
            "high-taste-writing-os",
            "publishable-copy-gate",
            "positioning-message-bridge",
            "new-media-ghostwriting",
        ),
        artifact="contrast-driven narrative rewrite or strategy package with behavior proof",
        verifiers=(
            "python3 execution/validate_skill.py lucas-alpay-storytelling",
            "python3 execution/verify_skill_system_contract.py",
        ),
        plugin_ladder="workflow and Lucas companion layer first; client-service packaging only after repeated proof labs",
    ),
    "system-repair": OutcomeRecipe(
        name="system-repair",
        signals=("broken", "not firing", "system", "harness", "autopilot", "routing", "control plane"),
        primary_route="system-audit",
        support_gates=("routing-intelligence", "health-check", "self-evolve", "friction-ledger"),
        artifact="control-plane issue ledger plus run receipt",
        verifiers=(
            "python3 execution/verify_system_control_plane.py",
            "python3 execution/verify_autopilot_runtime_preflight.py",
            "python3 execution/codex_harness_check.py",
        ),
        plugin_ladder="workflow/helper first; plugin only after repeated fresh-thread proof",
    ),
    "source-to-skill": OutcomeRecipe(
        name="source-to-skill",
        signals=("source", "transcript", "book", "video", "skill system", "source-to-skill", "extract"),
        primary_route="source-to-skill-system",
        support_gates=("knowledge-librarian", "extraction-governor-agent", "expert-composition-governor"),
        artifact="grounded evidence package plus command-grade workflow/skill surface",
        verifiers=(
            "python3 execution/verify_skill_system_contract.py",
        ),
        plugin_ladder="skill wrapper before plugin candidate",
    ),
    "plugin-packaging": OutcomeRecipe(
        name="plugin-packaging",
        signals=("plugin", "package", "packaging", "marketplace", "bundle"),
        primary_route="plugin-readiness-audit",
        support_gates=("capability-graph", "run-receipt", "plugin-forge"),
        artifact="plugin readiness scorecard and packaging verdict",
        verifiers=(
            "python3 execution/plugin_readiness_audit.py --stdout autopilot mission orchestrate",
            "python3 execution/capability_graph.py --json",
        ),
        plugin_ladder="helper/script -> workflow -> skill wrapper -> plugin candidate -> plugin",
    ),
    "revenue-sprint": OutcomeRecipe(
        name="revenue-sprint",
        signals=("revenue", "cash", "client", "income", "paid", "offer", "monetize"),
        primary_route="first-10k",
        support_gates=("revenue-offer-agent", "client-acquire", "publishable-copy-gate", "adversarial-review"),
        artifact="buyer-facing offer/action package",
        verifiers=(
            "python3 execution/verify_autopilot_routing.py",
            "python3 execution/routing_intelligence.py scoreboard",
        ),
        plugin_ladder="keep as workflow family until paid-use repetition is proven",
    ),
    "content-package": OutcomeRecipe(
        name="content-package",
        signals=("content", "post", "linkedin", "newsletter", "script", "copy", "draft"),
        primary_route="create",
        support_gates=("high-taste-writing-os", "publishable-copy-gate", "excellence-latch"),
        artifact="publishable draft package plus copy gate result",
        verifiers=("python3 execution/verify_autopilot_routing.py",),
        plugin_ladder="workflow family before plugin; preserve draft-only boundaries",
    ),
    "research-synthesis": OutcomeRecipe(
        name="research-synthesis",
        signals=("research", "current", "latest", "market", "competitor", "facts", "verify"),
        primary_route="deep-research-os",
        support_gates=("research-intelligence-agent", "ground-truth", "adversarial-review"),
        artifact="claim-labeled research synthesis with source ledger",
        verifiers=("python3 execution/verify_free_first_research_mission.py",),
        plugin_ladder="do not package until external-source permissions are stable",
    ),
    "deep-research-os": OutcomeRecipe(
        name="deep-research-os",
        signals=(
            "deep research os",
            "ultimate research",
            "social listening",
            "wide research",
            "market intelligence",
            "product-market fit",
            "offer-market fit",
            "anti hallucination",
        ),
        primary_route="deep-research-os",
        support_gates=("research-intelligence-agent", "ground-truth", "adversarial-review", "research-quality-gate"),
        artifact="source-backed research package with plan, evidence ledger, claim table, social listening, and synthesis",
        verifiers=(
            "python3 execution/verify_deep_research_os.py",
            "python3 execution/verify_deep_research_ledger.py",
            "python3 execution/verify_free_first_research_mission.py",
        ),
        plugin_ladder="workflow and cold command wrapper first; promote only after repeated receipts",
    ),
    "client-audit": OutcomeRecipe(
        name="client-audit",
        signals=("client audit", "client-facing", "proposal", "deliverable", "sop", "playbook"),
        primary_route="24-assets-client-audit",
        support_gates=("research-intelligence-agent", "adversarial-review", "ground-truth"),
        artifact="client-facing audit or delivery artifact",
        verifiers=("python3 execution/verify_autopilot_routing.py",),
        plugin_ladder="package only after repeatable client delivery proof",
    ),
    "design-build": OutcomeRecipe(
        name="design-build",
        signals=("design", "build", "ui", "website", "app", "interface"),
        primary_route="product-design-page-build",
        support_gates=("creative-quality-audit-system", "ground-truth", "design-to-code-execution"),
        artifact="implemented interface plus visual verification",
        verifiers=("python3 execution/verify_autopilot_routing.py",),
        plugin_ladder="keep local unless the design/build loop repeats across projects",
    ),
    "mission-continuation": OutcomeRecipe(
        name="mission-continuation",
        signals=("mission", "resume", "continue", "handoff", "approved package"),
        primary_route="mission",
        support_gates=("knowledge-librarian", "run-receipt", "end-session"),
        artifact="mission handoff receipt plus next executable command",
        verifiers=("python3 execution/mission_control.py validate",),
        plugin_ladder="mission stays governance layer, not plugin",
    ),
    "repeatability-repair": OutcomeRecipe(
        name="repeatability-repair",
        signals=("revision got worse", "lost the good part", "repeat", "regression", "wrong route"),
        primary_route="repeatability-spine",
        support_gates=("self-evolve", "skill-anneal", "publishable-copy-gate"),
        artifact="preservation lock, repair route, regression guard",
        verifiers=("python3 execution/verify_repeatability_spine.py",),
        plugin_ladder="repair the route before packaging anything",
    ),
}


def _contains_any(text: str, signals: Iterable[str]) -> bool:
    lowered = text.lower()
    return any(signal in lowered for signal in signals)


def classify_outcome(query: str, lane: str = "", route: str = "") -> OutcomeRecipe:
    lowered = query.lower()
    if lane == "kishotenketsu-contrast-storytelling" or route == "kishotenketsu-contrast-storytelling":
        return RECIPES["kishotenketsu-contrast-storytelling"]
    if lane == "deep-research-os" or route == "deep-research-os":
        return RECIPES["deep-research-os"]
    if "package" in lowered and any(
        signal in lowered
        for signal in ("research", "social listening", "market intelligence", "deep research", "wide research")
    ):
        return RECIPES["deep-research-os"]
    if "plugin" in lowered or "package" in lowered or "marketplace" in lowered:
        return RECIPES["plugin-packaging"]
    if lane == "system-failure":
        return RECIPES["system-repair"]
    if lane == "skill-system" or route == "source-to-skill-system":
        return RECIPES["source-to-skill"]
    if lane == "revenue":
        return RECIPES["revenue-sprint"]
    if lane == "repeatability":
        return RECIPES["repeatability-repair"]
    for recipe in RECIPES.values():
        if _contains_any(query, recipe.signals):
            return recipe
    return OutcomeRecipe(
        name="general-operator",
        signals=(),
        primary_route=route or "autopilot",
        support_gates=("routing-governor", "run-receipt"),
        artifact="intent-to-outcome run receipt",
        verifiers=("python3 execution/verify_autopilot_runtime_preflight.py",),
        plugin_ladder="keep as workflow until repeated use proves packaging",
    )


def as_jsonable(recipe: OutcomeRecipe) -> dict[str, object]:
    return asdict(recipe)


def main() -> int:
    parser = argparse.ArgumentParser(description="Classify a request into an Antigravity outcome recipe.")
    parser.add_argument("query", nargs="*", help="Raw request to classify.")
    parser.add_argument("--lane", default="", help="Optional governor lane.")
    parser.add_argument("--route", default="", help="Optional chosen route.")
    parser.add_argument("--list", action="store_true", help="List available recipes.")
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    args = parser.parse_args()

    if args.list:
        payload = [as_jsonable(recipe) for recipe in RECIPES.values()]
    else:
        payload = as_jsonable(classify_outcome(" ".join(args.query), args.lane, args.route))

    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        if isinstance(payload, list):
            for item in payload:
                print(f"{item['name']}: /{item['primary_route']}")
        else:
            print(f"Outcome Recipe: {payload['name']}")
            print(f"Primary route: /{payload['primary_route']}")
            print("Support gates: " + ", ".join(f"/{gate}" for gate in payload["support_gates"]))
            print(f"Artifact: {payload['artifact']}")
            print(f"Plugin ladder: {payload['plugin_ladder']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
