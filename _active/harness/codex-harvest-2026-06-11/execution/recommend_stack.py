#!/usr/bin/env python3
"""Surface one evidence-backed recommended stack for a goal.

This is a presenter/composer layer over the existing arsenal evidence. It does
not replace routing, and it deliberately returns "No recommended stack" unless
a trigger-matched compound or equivalent registry-backed signal is present.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any
import re


ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "semantic_libraries" / "antigravity" / "stacking" / "agent-stacking-registry.json"
NO_STACK = "No recommended stack"
GENERIC_STACK_TERMS = {
    "audit",
    "system",
    "workflow",
    "workflows",
    "skill",
    "skills",
    "route",
    "routing",
    "content",
    "copy",
    "write",
    "writing",
    "agent",
    "agents",
    "brief",
    "review",
}


def load_registry(path: Path = REGISTRY) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def normalize(text: str) -> str:
    return " ".join(text.lower().replace("/", " ").replace("-", " ").split())


def stem(token: str) -> str:
    token = token.lower().strip(".,:;!?()[]{}\"'")
    for suffix in ("ing", "ed", "es", "s"):
        if len(token) > len(suffix) + 3 and token.endswith(suffix):
            return token[: -len(suffix)]
    return token


def trigger_match(query: str, triggers: list[str]) -> str:
    normalized_query = normalize(query)
    query_stems = [stem(token) for token in normalized_query.split() if len(token) > 2]

    for trigger in triggers:
        if normalize(trigger) in normalized_query:
            return trigger

    best_trigger = ""
    best_score = 0.0
    for trigger in triggers:
        words = [word for word in normalize(trigger).split() if len(word) > 2]
        if not words:
            continue
        matched = 0
        for word in words:
            word_stem = stem(word)
            if any(word_stem in query_stem or query_stem in word_stem for query_stem in query_stems):
                matched += 1
        score = matched / len(words)
        if score >= 0.6 and score > best_score:
            best_trigger = trigger
            best_score = score
    return best_trigger


def registry_confirms(registry: dict[str, Any], pair: list[str]) -> bool:
    expected = set(pair)
    for item in registry.get("expert_router_compounds", []):
        if set(item.get("pair", [])) == expected:
            return True
    return False


def token_set(text: str) -> set[str]:
    return {stem(token) for token in normalize(text).split() if len(token) > 2}


def overlap_score(query: str, value: str) -> float:
    query_tokens = token_set(query)
    value_tokens = token_set(value)
    if not query_tokens or not value_tokens:
        return 0.0
    overlap = query_tokens & value_tokens
    return len(overlap) / min(len(query_tokens), max(1, len(value_tokens)))


def meaningful_overlap(query: str, value: str) -> set[str]:
    return (token_set(query) & token_set(value)) - GENERIC_STACK_TERMS


def partner_candidates(item: dict[str, Any]) -> list[str]:
    partners = [str(value) for value in item.get("declared_partners", []) if value]
    excerpt = str(item.get("evidence_excerpt", ""))
    partners.extend(re.findall(r"\*\*([^*]{3,80})\*\*", excerpt))
    partners.extend(re.findall(r"`([^`]{3,80})`", excerpt))
    cleaned = []
    seen: set[str] = set()
    for partner in partners:
        value = partner.strip().strip("/").strip()
        if not value or value.lower() in {"stack with", "pairs with", "result"}:
            continue
        key = normalize(value)
        if key and key not in seen:
            cleaned.append(value)
            seen.add(key)
    return cleaned


def registry_stacking_match(query: str, registry: dict[str, Any]) -> dict[str, Any] | None:
    best: tuple[float, dict[str, Any], str] | None = None
    for item in registry.get("skill_stacking_guides", []):
        skill = str(item.get("skill", ""))
        excerpt = str(item.get("evidence_excerpt", ""))
        partners = partner_candidates(item)
        skill_score = max(overlap_score(query, skill), overlap_score(query, excerpt))
        for partner in partners:
            if not (meaningful_overlap(query, skill) or meaningful_overlap(query, partner)):
                continue
            score = max(skill_score, overlap_score(query, partner), overlap_score(query, f"{skill} {partner} {excerpt}"))
            if score >= 0.28 and (best is None or score > best[0]):
                best = (score, item, partner)
    if best is None:
        return None
    score, item, partner = best
    skill = str(item.get("skill", ""))
    return {
        "skill": skill,
        "partner": normalize(partner).replace(" ", "-"),
        "partner_label": partner,
        "path": item.get("path", ""),
        "excerpt": str(item.get("evidence_excerpt", ""))[:240],
        "score": score,
    }


def recommend_stack(query: str) -> dict[str, Any]:
    registry = load_registry()

    sys.path.insert(0, str(ROOT / "execution"))
    import routing_governor  # type: ignore

    if routing_governor.is_operating_alignment_intent(query) or routing_governor.is_system_failure_intent(query):
        return {
            "query": query,
            "recommended_stack": NO_STACK,
            "recommendation": NO_STACK,
            "stack": [],
            "compound_effect": "",
            "effect": "",
            "evidence_source": "execution/routing_governor.py operating-alignment/system-failure guard",
            "trigger_match": "operating-alignment-or-system-failure",
            "confidence": "high",
            "skip_reason": (
                "Operating-alignment and system-repair work is owned by the control "
                "plane. The full arsenal remains available on demand, but domain "
                "expert stacks must enter through bounded support slots instead of "
                "becoming the owner."
            ),
            "policy": "One owner first; expert lenses belong in the Composition Ledger.",
        }

    import expert_router  # type: ignore

    compounds = expert_router.find_compounds(query)
    if compounds:
        compound = compounds[0]
        pair = list(compound.get("pair", []))
        triggers = list(compound.get("trigger", []))
        confirmed = registry_confirms(registry, pair)
        evidence = "execution/expert_router.py COMPOUNDS"
        if confirmed:
            evidence += " + agent-stacking-registry.json"

        return {
            "query": query,
            "recommended_stack": " + ".join(pair),
            "recommendation": " + ".join(pair),
            "stack": pair,
            "compound_effect": compound.get("effect", ""),
            "effect": compound.get("effect", ""),
            "evidence_source": evidence,
            "trigger_match": trigger_match(query, triggers) or (triggers[0] if triggers else ""),
            "confidence": "high" if confirmed else "medium",
            "skip_reason": "",
            "policy": "Stack is surfaced as support evidence only; primary routing still decides the workflow.",
        }

    registry_match = registry_stacking_match(query, registry)
    if registry_match:
        stack = [registry_match["skill"], registry_match["partner"]]
        return {
            "query": query,
            "recommended_stack": " + ".join(stack),
            "recommendation": " + ".join(stack),
            "stack": stack,
            "compound_effect": f"Registry stacking guide: {registry_match['skill']} with {registry_match['partner_label']}",
            "effect": f"Registry stacking guide: {registry_match['skill']} with {registry_match['partner_label']}",
            "evidence_source": f"agent-stacking-registry.json skill_stacking_guides -> {registry_match['path']}",
            "trigger_match": registry_match["excerpt"],
            "confidence": "medium",
            "skip_reason": "",
            "policy": "Stack is surfaced as support evidence only; primary routing still decides the workflow.",
        }

    return {
        "query": query,
        "recommended_stack": NO_STACK,
        "recommendation": NO_STACK,
        "stack": [],
        "compound_effect": "",
        "effect": "",
        "evidence_source": "",
        "trigger_match": "",
        "confidence": "none",
        "skip_reason": "No trigger-matched compound, skill stacking guide, cascade evidence, positive ensemble feedback, or registry-backed pairing matched this goal; keep the primary workflow.",
        "policy": "Do not force stacking when one workflow or expert is enough.",
    }


def format_text(result: dict[str, Any]) -> str:
    if result["recommended_stack"] == NO_STACK:
        return "\n".join(
            [
                f"Recommended Stack: {NO_STACK}",
                f"Skip reason: {result['skip_reason']}",
                f"Policy: {result['policy']}",
            ]
        )

    return "\n".join(
        [
            f"Recommended Stack: {result['recommended_stack']}",
            f"Compound effect: {result['compound_effect']}",
            f"Evidence source: {result['evidence_source']}",
            f"Trigger match: {result['trigger_match']}",
            f"Policy: {result['policy']}",
        ]
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Recommend one evidence-backed expert/skill stack for a goal.")
    parser.add_argument("query", nargs="+", help="Goal, query, or raw context to evaluate.")
    parser.add_argument("--json", action="store_true", help="Return machine-readable JSON.")
    args = parser.parse_args()

    result = recommend_stack(" ".join(args.query))
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(format_text(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
