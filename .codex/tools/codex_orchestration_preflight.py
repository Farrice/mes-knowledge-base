#!/usr/bin/env python3
"""Codex orchestration preflight for Google Antigravity.

This is the Codex-native substitute for the Claude Code hook stack when hooks
are unavailable or disabled. It emits a Context Load Packet before substantial
work so routing, context, and verification are explicit rather than remembered.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
GLOBAL_CODEX_CONFIG = Path.home() / ".codex" / "config.toml"
HOOKS_PATH = REPO_ROOT / ".codex" / "hooks.json"
CANONICAL_GOOGLE_ROOT = Path("/Users/farricecain/Google Antigravity")
CANONICAL_CODEX_WORKFLOWS = Path("/Users/farricecain/Codex Antigravity/.agent/workflows")
GLOBAL_SKILLS_ROOT = Path.home() / ".codex" / "skills"

CONTROL_PLANE_ROUTES = {
    "system-audit": {
        "global_skill": GLOBAL_SKILLS_ROOT / "system-audit" / "SKILL.md",
        "canonical_workflow": CANONICAL_CODEX_WORKFLOWS / "system-audit.md",
        "required_refs": [
            Path("/Users/farricecain/Codex Antigravity/semantic_libraries/antigravity/primitives/operating-alignment-contract.md"),
            Path("/Users/farricecain/Codex Antigravity/semantic_libraries/antigravity/primitives/magic-preservation-regression-set.md"),
        ],
    },
    "repeatability-spine": {
        "global_skill": GLOBAL_SKILLS_ROOT / "repeatability-spine" / "SKILL.md",
        "canonical_workflow": CANONICAL_CODEX_WORKFLOWS / "repeatability-spine.md",
        "required_refs": [
            Path("/Users/farricecain/Codex Antigravity/semantic_libraries/antigravity/primitives/repeatability-spine-contract.md"),
            Path("/Users/farricecain/Codex Antigravity/semantic_libraries/antigravity/primitives/skill-system-contract.md"),
        ],
    },
    "knowledge-librarian": {
        "global_skill": GLOBAL_SKILLS_ROOT / "knowledge-librarian" / "SKILL.md",
        "canonical_workflow": CANONICAL_CODEX_WORKFLOWS / "knowledge-librarian.md",
        "required_refs": [],
    },
    "source-to-skill-system": {
        "global_skill": GLOBAL_SKILLS_ROOT / "source-to-skill-system" / "SKILL.md",
        "canonical_workflow": CANONICAL_CODEX_WORKFLOWS / "source-to-skill-system.md",
        "required_refs": [
            Path("/Users/farricecain/Codex Antigravity/semantic_libraries/antigravity/primitives/skill-system-contract.md"),
        ],
    },
    "autopilot": {
        "global_skill": GLOBAL_SKILLS_ROOT / "autopilot" / "SKILL.md",
        "canonical_workflow": CANONICAL_CODEX_WORKFLOWS / "autopilot.md",
        "required_refs": [],
    },
}

SYSTEM_FIRING_SIGNALS = (
    "not firing",
    "isn't firing",
    "not using",
    "under-loading",
    "under loading",
    "underloaded",
    "routing layer",
    "orchestration layer",
    "wrong workflow",
    "wrong workflows",
    "workflow not firing",
    "workflows not firing",
    "route picked the wrong",
    "route failed",
    "misroute",
    "harness",
    "codex feels",
    "claude code",
    "parity",
    "context load",
    "genius.md",
    "skill loading",
    "agent.md",
    "agents.md",
)

REPEATABILITY_SIGNALS = (
    "lost the magic",
    "cannot repeat",
    "can't repeat",
    "repeatability",
    "repeatable",
    "repeat this",
    "reproduce this",
    "revision got worse",
    "got worse",
    "regression",
    "regressed",
    "preserve the good",
    "preservation lock",
    "reverse engineer",
    "codify this",
    "codify it",
    "quality bar",
    "golden sample",
    "gold standard",
    "bar i want",
    "get to this point again",
    "get results like this",
)

SOURCE_SYSTEM_SIGNALS = (
    "turn this source",
    "source to skill",
    "source-to-skill",
    "source to system",
    "source-to-system",
    "source to skill system",
    "source-to-skill-system",
    "connected skill system",
    "workflow bridge",
    "reusable skill",
    "reusable skills",
    "build out all the workflows",
    "harvest all the genius",
)

KNOWLEDGE_SIGNALS = (
    "knowledge pulse",
    "library pulse",
    "knowledge-librarian",
    "session start pulse",
    "prior decisions",
    "reusable solution",
    "reusable solutions",
    "underused workflow",
    "underused workflows",
    "sleeping giants",
)

LINKEDIN_CONTENT_SIGNALS = (
    "linkedin",
    "post",
    "posts",
    "article",
    "content",
    "content packet",
    "content plan",
    "week 1",
    "client-attraction",
    "ghostwriting",
    "public-audit",
    "public audit",
)

MODE_CHOICES = ("deliverable", "system", "research")


def _python() -> str:
    override = os.environ.get("ANTIGRAVITY_PYTHON")
    if override:
        return override
    venv_python = REPO_ROOT / ".venv" / "bin" / "python"
    if venv_python.exists():
        return str(venv_python)
    return sys.executable


def _run(args: list[str], timeout: int = 25) -> dict[str, Any]:
    try:
        proc = subprocess.run(
            args,
            cwd=str(REPO_ROOT),
            text=True,
            capture_output=True,
            timeout=timeout,
        )
        return {
            "ok": proc.returncode == 0,
            "code": proc.returncode,
            "stdout": proc.stdout.strip(),
            "stderr": proc.stderr.strip(),
            "cmd": " ".join(args),
        }
    except Exception as exc:  # keep preflight fail-soft
        return {"ok": False, "code": None, "stdout": "", "stderr": str(exc), "cmd": " ".join(args)}


def _json_from_run(result: dict[str, Any]) -> Any:
    if not result.get("stdout"):
        return None
    try:
        return json.loads(result["stdout"])
    except json.JSONDecodeError:
        return None


def _intent_score(intent: str, mode: str) -> dict[str, Any]:
    low = intent.lower()
    checks = {
        "deliverable": bool(re.search(r"\b(write|draft|build|create|produce|audit|research|fix|repair|generate|turn)\b", low)),
        "audience": bool(re.search(r"\b(for|audience|client|customer|buyer|brand|founder|operator|codex|claude|linkedin)\b", low)),
        "context": len(intent.split()) >= 8,
        "end_state": bool(re.search(r"\b(ready|publish|client|proof|pass|fix|working|parity|smoke|receipt|reusable)\b", low)),
        "specific_language": bool(re.search(r"[/._-]|codex|claude|google antigravity|linkedin|seo|geo|genius|workflow", low)),
    }
    score = sum(1 for value in checks.values() if value)
    if mode in {"system", "research"} and score < 3:
        score += 1
    return {"score": min(score, 5), "checks": checks}


def _resolve_package(intent: str) -> tuple[dict[str, Any], dict[str, Any]]:
    result = _run([_python(), "execution/intent_to_package.py", "resolve", "--intent", intent, "--json"])
    package = _json_from_run(result)
    if isinstance(package, dict):
        return package, result
    return {
        "outcome_class": "unknown",
        "primary_workflow": "big-project",
        "skills_to_load": [],
        "experts": [],
        "confidence": 0.0,
        "reasoning": "intent_to_package.py did not return JSON; using safe fallback.",
        "matched_signals": [],
    }, result


def _has_any(text: str, phrases: tuple[str, ...]) -> bool:
    low = text.lower()
    return any(phrase in low for phrase in phrases)


def _is_linkedin_content(intent: str) -> bool:
    low = intent.lower()
    return "linkedin" in low and _has_any(low, LINKEDIN_CONTENT_SIGNALS)


def _apply_codex_overrides(package: dict[str, Any], intent: str, mode: str) -> tuple[dict[str, Any], list[str]]:
    reasons: list[str] = []
    adjusted = dict(package)

    if _has_any(intent, SOURCE_SYSTEM_SIGNALS):
        adjusted.update(
            {
                "outcome_class": "source_to_system",
                "primary_workflow": "source-to-skill-system",
                "skills_to_load": [],
                "experts": ["source-to-skill-system"],
                "confidence": max(float(package.get("confidence") or 0), 0.82),
                "reasoning": "Source-to-capability requests route to the connected skill-system lane.",
                "matched_signals": sorted(
                    phrase for phrase in SOURCE_SYSTEM_SIGNALS if phrase in intent.lower()
                ),
            }
        )
        reasons.append("source-to-system override")
        return adjusted, reasons

    if _has_any(intent, KNOWLEDGE_SIGNALS):
        adjusted.update(
            {
                "outcome_class": "knowledge_librarian",
                "primary_workflow": "knowledge-librarian",
                "skills_to_load": [],
                "experts": ["knowledge-librarian"],
                "confidence": max(float(package.get("confidence") or 0), 0.84),
                "reasoning": "Knowledge-library and prior-decision asks route to /knowledge-librarian.",
                "matched_signals": sorted(
                    phrase for phrase in KNOWLEDGE_SIGNALS if phrase in intent.lower()
                ),
            }
        )
        reasons.append("knowledge-librarian override")
        return adjusted, reasons

    if _has_any(intent, REPEATABILITY_SIGNALS):
        adjusted.update(
            {
                "outcome_class": "repeatability_repair",
                "primary_workflow": "repeatability-spine",
                "skills_to_load": [],
                "experts": ["repeatability-spine"],
                "confidence": max(float(package.get("confidence") or 0), 0.86),
                "reasoning": "Lost-magic, failed-revision, and regression asks route to /repeatability-spine.",
                "matched_signals": sorted(
                    phrase for phrase in REPEATABILITY_SIGNALS if phrase in intent.lower()
                ),
            }
        )
        reasons.append("repeatability-spine override")
        return adjusted, reasons

    if mode == "system" or _has_any(intent, SYSTEM_FIRING_SIGNALS):
        adjusted.update(
            {
                "outcome_class": "system",
                "primary_workflow": "system-audit",
                "skills_to_load": [],
                "experts": ["system-audit"],
                "confidence": max(float(package.get("confidence") or 0), 0.88),
                "reasoning": "Codex firing-layer/system pain routes to /system-audit before domain workflows.",
                "matched_signals": sorted(
                    phrase for phrase in SYSTEM_FIRING_SIGNALS if phrase in intent.lower()
                ),
            }
        )
        reasons.append("system-firing override")
        return adjusted, reasons

    if mode == "deliverable" and _is_linkedin_content(intent):
        adjusted.update(
            {
                "outcome_class": "linkedin_content_packet",
                "primary_workflow": "content-sprint",
                "skills_to_load": [
                    "lara-acosta-linkedin-mastery",
                    "fresh-voice-system",
                    "new-media-ghostwriting",
                    "nicolas-cole-client-acquisition",
                ],
                "experts": ["lara-acosta-linkedin-mastery"],
                "confidence": max(float(package.get("confidence") or 0), 0.86),
                "reasoning": "LinkedIn content packets route to /content-sprint with loadable Lara owner files, not /big-project.",
                "matched_signals": sorted(
                    phrase for phrase in LINKEDIN_CONTENT_SIGNALS if phrase in intent.lower()
                ),
            }
        )
        reasons.append("linkedin-content override")
        return adjusted, reasons

    if mode == "research" and adjusted.get("outcome_class") != "research":
        adjusted.update(
            {
                "outcome_class": "research",
                "primary_workflow": "deep-research",
                "skills_to_load": [],
                "experts": ["deep-research"],
                "confidence": max(float(package.get("confidence") or 0), 0.75),
                "reasoning": "Research mode forces the research lane unless a stronger research package already matched.",
            }
        )
        reasons.append("research-mode override")

    return adjusted, reasons


def _find_skills(intent: str) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    result = _run([_python(), "execution/find_skill.py", "--json", "--top", "5", intent])
    parsed = _json_from_run(result)
    return (parsed if isinstance(parsed, list) else []), result


def _memory(intent: str) -> tuple[dict[str, Any], dict[str, Any]]:
    facade = REPO_ROOT / "execution" / "memory_facade.py"
    if facade.exists():
        result = _run([_python(), "execution/memory_facade.py", intent, "--top", "5", "--json"], timeout=35)
        parsed = _json_from_run(result)
        if isinstance(parsed, dict):
            return parsed, result
        return {"results": [], "degraded": [result.get("stderr") or "memory_facade returned non-json"]}, result
    result = _run([_python(), "execution/memory_retrieve.py", intent, "--top", "5"], timeout=25)
    return {"results": [], "degraded": ["memory_facade missing; memory_retrieve text fallback used"], "text": result.get("stdout", "")}, result


def _route_proof(intent: str, workflow: str) -> dict[str, Any]:
    sys.path.insert(0, str(REPO_ROOT / "execution"))
    try:
        from routing_enforcer import check_routing  # type: ignore

        proof = check_routing(intent, workflow)
        proof["source"] = "routing_enforcer.check_routing"
        return proof
    except Exception as exc:
        return {
            "valid": None,
            "binding_matched": None,
            "chosen_workflow": workflow,
            "violation_reason": f"routing_enforcer unavailable: {exc}",
            "source": "fallback",
        }


def _hook_state() -> dict[str, Any]:
    state = {
        "workspace_hooks_file": str(HOOKS_PATH),
        "workspace_hooks_exists": HOOKS_PATH.exists(),
        "workspace_role": _workspace_role(),
        "canonical_hooks_file": str(CANONICAL_GOOGLE_ROOT / ".codex" / "hooks.json"),
        "global_config": str(GLOBAL_CODEX_CONFIG),
        "project_trusted": False,
        "canonical_project_trusted": False,
        "enabled_states": [],
        "disabled_states": [],
        "canonical_enabled_states": [],
        "notes": [],
    }
    if not GLOBAL_CODEX_CONFIG.exists():
        state["notes"].append("global Codex config not found")
        return state
    text = GLOBAL_CODEX_CONFIG.read_text(errors="ignore")
    state["project_trusted"] = f'[projects."{REPO_ROOT}"]' in text and 'trust_level = "trusted"' in text
    state["canonical_project_trusted"] = (
        f'[projects."{CANONICAL_GOOGLE_ROOT}"]' in text and 'trust_level = "trusted"' in text
    )
    current = None
    for line in text.splitlines():
        if line.startswith("[hooks.state.") and str(HOOKS_PATH) in line:
            current = line.strip()[1:-1]
        elif current and line.strip().startswith("enabled"):
            if "true" in line.lower():
                state["enabled_states"].append(current)
            else:
                state["disabled_states"].append(current)
            current = None
    current = None
    canonical_hooks = str(CANONICAL_GOOGLE_ROOT / ".codex" / "hooks.json")
    for line in text.splitlines():
        if line.startswith("[hooks.state.") and canonical_hooks in line:
            current = line.strip()[1:-1]
        elif current and line.strip().startswith("enabled"):
            if "true" in line.lower():
                state["canonical_enabled_states"].append(current)
            current = None
    if state["disabled_states"] and not state["enabled_states"]:
        state["notes"].append("Codex hook definitions exist but are disabled in global config.")
    if state["workspace_hooks_exists"] and not state["enabled_states"]:
        state["notes"].append("No enabled hook states were found for this exact hooks.json path.")
    if not state["project_trusted"]:
        state["notes"].append("This active root is not explicitly trusted in global Codex config.")
    if state["workspace_role"] == "worktree" and state["canonical_enabled_states"]:
        state["notes"].append("Canonical Google Antigravity hooks are enabled; worktree needs active-root runner or direct trust.")
    return state


def _workspace_role() -> str:
    root = REPO_ROOT.resolve()
    if root == CANONICAL_GOOGLE_ROOT:
        return "canonical"
    if ".codex/worktrees" in str(root) and root.name == "Google Antigravity":
        return "worktree"
    return "other"


def _file_status(path: str) -> dict[str, Any]:
    p = Path(path).expanduser()
    if not p.is_absolute():
        p = REPO_ROOT / path
    display = path if not p.is_absolute() or str(p).startswith(str(REPO_ROOT)) else str(p)
    return {"path": display, "exists": p.exists()}


def _skill_exists(slug: str) -> bool:
    return (REPO_ROOT / "skills" / slug / "SKILL.md").exists()


def _workflow_files(workflow: str) -> list[dict[str, Any]]:
    candidates = [
        f".agent/workflows/{workflow}.md",
        f".agents/skills/source-command-{workflow}/SKILL.md",
        f".claude/commands/{workflow}.md",
    ]
    if workflow in CONTROL_PLANE_ROUTES:
        route = CONTROL_PLANE_ROUTES[workflow]
        candidates.extend(
            [
                str(route["global_skill"]),
                str(route["canonical_workflow"]),
            ]
        )
        candidates.extend(str(path) for path in route.get("required_refs", []))
    return [_file_status(path) for path in candidates]


def _choose_skill_workflow(base: Path, slug: str, workflow_hint: str | None = None) -> Path | None:
    workflows_dir = base / "workflows"
    if not workflows_dir.exists():
        return None
    workflows = sorted(workflows_dir.glob("*.md"))
    if not workflows:
        return None

    hint = (workflow_hint or "").strip("/").lower()
    preferred_names = {
        "content-sprint": {
            "lara-acosta-linkedin-mastery": ["high-performance-content-engine.md"],
            "fresh-voice-system": ["03-bridge-post-production.md", "02-serial-content-production.md"],
            "new-media-ghostwriting": ["01-voice-to-media-empire.md"],
            "nicolas-cole-client-acquisition": ["zero-to-client-sprint.md", "no-portfolio-client-landing.md"],
        }
    }
    for name in preferred_names.get(hint, {}).get(slug, []):
        candidate = workflows_dir / name
        if candidate.exists():
            return candidate

    for candidate in workflows:
        if hint and hint in candidate.stem.lower():
            return candidate
    return workflows[0]


def _skill_files(slug: str, workflow_hint: str | None = None) -> list[dict[str, Any]]:
    base = REPO_ROOT / "skills" / slug
    files = [
        f"skills/{slug}/SKILL.md",
        f"skills/{slug}/genius.md",
    ]
    if base.exists():
        workflow_file = _choose_skill_workflow(base, slug, workflow_hint)
        if workflow_file:
            files.append(str(workflow_file.relative_to(REPO_ROOT)))
    return [_file_status(path) for path in files]


def _load_plan(package: dict[str, Any], skill_matches: list[dict[str, Any]]) -> dict[str, Any]:
    workflow = str(package.get("primary_workflow") or "big-project").strip("/")
    package_skills = [str(s).strip("/") for s in package.get("skills_to_load") or [] if str(s).strip("/")]

    lanes: list[dict[str, Any]] = []
    rejected_routes: list[dict[str, Any]] = []
    if package_skills:
        for i, slug in enumerate(package_skills[:3]):
            if _skill_exists(slug):
                lanes.append(
                    {
                        "role": "owner" if not lanes else "support",
                        "name": slug,
                        "load_tier": "Tier 2 for creative/taste/client work; Tier 1 if purely mechanical",
                        "files": _skill_files(slug, workflow),
                    }
                )
            else:
                rejected_routes.append(
                    {
                        "name": slug,
                        "reason": "mission package named a skill with no local skills/<name>/SKILL.md; use loadable finder match instead",
                    }
                )
        if not lanes:
            for match in skill_matches:
                slug = str(match.get("directory") or "")
                if slug and _skill_exists(slug):
                    lanes.append(
                        {
                            "role": "owner_fallback",
                            "name": slug,
                            "load_tier": "Tier 2 because package skills were not loadable",
                            "files": _skill_files(slug, workflow),
                        }
                    )
                    break
    elif workflow in {"system-audit", "source-to-skill-system", "repeatability-spine", "knowledge-librarian", "autopilot", "extract-forge", "deep-research", "research-swarm"}:
        lanes.append(
            {
                "role": "owner",
                "name": workflow,
                "load_tier": "Workflow + referenced contracts",
                "files": _workflow_files(workflow),
            }
        )
    elif skill_matches:
        slug = str(skill_matches[0].get("directory") or "")
        lanes.append(
            {
                "role": "owner_candidate",
                "name": slug,
                "load_tier": "Tier 2 if chosen",
                "files": _skill_files(slug, workflow),
            }
        )

    support: list[dict[str, Any]] = []
    for match in skill_matches[:5]:
        slug = str(match.get("directory") or "")
        if slug and slug not in {lane["name"] for lane in lanes}:
            support.append(
                {
                    "name": slug,
                    "score": round(float(match.get("score") or 0), 2),
                    "command": match.get("slash"),
                    "use_only_if": "bounded support lane; do not rewrite owner voice",
                }
            )

    required_context = [
        _file_status("AGENTS.md"),
        _file_status("PRODUCTION_CORE.md"),
        _file_status("directives/routing-bindings.md"),
        _file_status("directives/agent-loading-protocol.md"),
        _file_status("directives/skill-invocation-and-routing.md"),
        _file_status(".codex/hooks.json"),
    ]

    return {
        "workflow_files": _workflow_files(workflow),
        "owner_lanes": lanes,
        "support_candidates": support[:4],
        "rejected_routes": rejected_routes,
        "required_context": required_context,
        "rejected_routes_rule": "Reject any expert/workflow that cannot name its bounded job before drafting.",
    }


def _context_load_manifest(package: dict[str, Any], load_plan: dict[str, Any], route_proof: dict[str, Any]) -> dict[str, Any]:
    workflow = str(package.get("primary_workflow") or "big-project").strip("/")
    required_files: list[dict[str, Any]] = []
    optional_files: list[dict[str, Any]] = []
    warnings: list[str] = []

    def add_required(items: list[dict[str, Any]]) -> None:
        for item in items:
            if str(item.get("path", "")).startswith(".claude/commands/"):
                optional_files.append(item)
                continue
            if item not in required_files:
                required_files.append(item)

    add_required(load_plan.get("required_context", []))
    add_required(load_plan.get("workflow_files", []))

    owner_lanes = load_plan.get("owner_lanes", [])
    if not owner_lanes:
        warnings.append("No owner lane selected; route label is not executable yet.")

    for lane in owner_lanes:
        lane_files = lane.get("files", [])
        if lane.get("role") in {"owner", "owner_fallback", "owner_candidate"}:
            add_required(lane_files)
        else:
            optional_files.extend(lane_files)

    if workflow in CONTROL_PLANE_ROUTES:
        source_wrapper = f".agents/skills/source-command-{workflow}/SKILL.md"
        if not (REPO_ROOT / source_wrapper).exists():
            warnings.append(f"Missing Codex source-command bridge for /{workflow}.")

    if route_proof.get("valid") is False:
        warnings.append(f"Routing proof failed: {route_proof.get('violation_reason')}")
    elif route_proof.get("valid") is None:
        warnings.append(f"Routing proof degraded: {route_proof.get('violation_reason')}")

    required_missing = [item for item in required_files if not item.get("exists")]
    optional_missing = [item for item in optional_files if not item.get("exists")]

    bridge_only = bool(owner_lanes) and all(
        not any(str(item.get("path", "")).startswith("skills/") or "/.codex/skills/" in str(item.get("path", "")) for item in lane.get("files", []))
        for lane in owner_lanes
    )
    if bridge_only and workflow not in CONTROL_PLANE_ROUTES:
        warnings.append("Owner lane is bridge-only; load a real skill package before producing.")

    ready = not required_missing and route_proof.get("valid") is not False and not any(
        warning.startswith("No owner lane") or warning.startswith("Owner lane is bridge-only")
        for warning in warnings
    )

    return {
        "owner_workflow": workflow,
        "status": "PASS" if ready else "FAIL",
        "must_read_before_output": required_files,
        "optional_support_reads": optional_files,
        "missing_required": required_missing,
        "missing_optional": optional_missing,
        "warnings": warnings,
        "receipt_rule": "Substantial output is draft-quality until every must_read_before_output file is read and the Orchestration Receipt is filled.",
    }


def _receipt_template() -> dict[str, Any]:
    return {
        "intent_score": "fill from preflight",
        "owner_workflow": "fill from preflight",
        "route_proof": "valid / invalid / degraded",
        "memory_retrieved": "top memories or degraded reason",
        "files_loaded": ["SKILL.md", "genius.md", "workflow or contract"],
        "patterns_extracted": ["3 concrete patterns before producing"],
        "support_lanes": ["bounded jobs only"],
        "rejected_routes": ["routes intentionally not used"],
        "verifier_results": ["routing", "fact", "prose", "finalize"],
        "finalize_status": "PASS / PARTIAL / NOT RUN with reason",
    }


def build_packet(intent: str, mode: str) -> dict[str, Any]:
    raw_package, package_run = _resolve_package(intent)
    package, overrides = _apply_codex_overrides(raw_package, intent, mode)
    skill_matches, find_skill_run = _find_skills(intent)
    memory_payload, memory_run = _memory(intent)
    workflow = str(package.get("primary_workflow") or "big-project").strip("/")
    route_proof = _route_proof(intent, workflow)
    load_plan = _load_plan(package, skill_matches)
    manifest = _context_load_manifest(package, load_plan, route_proof)

    return {
        "packet_type": "Context Load Packet",
        "intent": intent,
        "mode": mode,
        "python": _python(),
        "intent_score": _intent_score(intent, mode),
        "mission_package": package,
        "raw_mission_package": raw_package,
        "codex_overrides": overrides,
        "route_proof": route_proof,
        "memory": {
            "degraded": memory_payload.get("degraded", []),
            "results": memory_payload.get("results", [])[:5],
            "summary": memory_payload.get("summary"),
        },
        "skill_matches": [
            {
                "directory": item.get("directory"),
                "slash": item.get("slash"),
                "score": round(float(item.get("score") or 0), 2),
                "description": item.get("description"),
            }
            for item in skill_matches[:5]
        ],
        "load_plan": load_plan,
        "context_load_manifest": manifest,
        "hook_state": _hook_state(),
        "orchestration_receipt_template": _receipt_template(),
        "preflight_health": {
            "intent_to_package_ok": package_run.get("ok"),
            "find_skill_ok": find_skill_run.get("ok"),
            "memory_ok": memory_run.get("ok"),
            "notes": [
                "Global hook enabling is approval-gated; current state is reported above.",
                "Use this packet before substantial Codex work when hooks are disabled or untrusted.",
            ],
        },
    }


def _short_file_list(items: list[dict[str, Any]]) -> str:
    if not items:
        return "- none"
    return "\n".join(
        f"- {'PASS' if item.get('exists') else 'MISS'} {item.get('path')}" for item in items
    )


def render_md(packet: dict[str, Any]) -> str:
    pkg = packet["mission_package"]
    route = packet["route_proof"]
    load_plan = packet["load_plan"]
    manifest = packet["context_load_manifest"]
    hook = packet["hook_state"]
    memory = packet["memory"]
    score = packet["intent_score"]

    lines = [
        "# Context Load Packet",
        "",
        f"Intent: {packet['intent']}",
        f"Mode: {packet['mode']}",
        f"Intent score: {score['score']}/5",
        "",
        "## Route",
        f"- Outcome: {pkg.get('outcome_class')}",
        f"- Owner workflow: /{pkg.get('primary_workflow')}",
        f"- Confidence: {pkg.get('confidence')}",
        f"- Matched signals: {', '.join(pkg.get('matched_signals') or []) or 'none'}",
        f"- Codex overrides: {', '.join(packet['codex_overrides']) or 'none'}",
        f"- Routing proof: {route.get('valid')} via {route.get('source')}",
        f"- Binding: {route.get('binding_matched') or 'none'}",
    ]
    if route.get("violation_reason"):
        lines.append(f"- Violation: {route.get('violation_reason')}")

    lines.extend(
        [
            "",
            "## Load Plan",
            "Workflow surfaces:",
            _short_file_list(load_plan["workflow_files"]),
            "",
            "Required context:",
            _short_file_list(load_plan["required_context"]),
            "",
            "Owner lanes:",
        ]
    )
    for lane in load_plan["owner_lanes"]:
        lines.append(f"- {lane['role']}: {lane['name']} ({lane['load_tier']})")
        for item in lane["files"]:
            lines.append(f"  - {'PASS' if item.get('exists') else 'MISS'} {item.get('path')}")
    if not load_plan["owner_lanes"]:
        lines.append("- none")

    lines.extend(["", "Support candidates:"])
    for item in load_plan["support_candidates"]:
        lines.append(f"- {item['name']} ({item['command']}, score {item['score']}): {item['use_only_if']}")
    if not load_plan["support_candidates"]:
        lines.append("- none")

    lines.extend(["", "Rejected routes:"])
    for item in load_plan["rejected_routes"]:
        lines.append(f"- {item['name']}: {item['reason']}")
    if not load_plan["rejected_routes"]:
        lines.append("- none")

    lines.extend(
        [
            "",
            "## Context Load Manifest",
            f"- Status: {manifest.get('status')}",
            f"- Owner workflow: /{manifest.get('owner_workflow')}",
            "- Must read before output:",
        ]
    )
    for item in manifest.get("must_read_before_output") or []:
        lines.append(f"  - {'PASS' if item.get('exists') else 'MISS'} {item.get('path')}")
    if not manifest.get("must_read_before_output"):
        lines.append("  - none")
    lines.append("- Optional support reads:")
    for item in manifest.get("optional_support_reads") or []:
        lines.append(f"  - {'PASS' if item.get('exists') else 'MISS'} {item.get('path')}")
    if not manifest.get("optional_support_reads"):
        lines.append("  - none")
    lines.append("- Warnings:")
    for warning in manifest.get("warnings") or []:
        lines.append(f"  - {warning}")
    if not manifest.get("warnings"):
        lines.append("  - none")

    lines.extend(
        [
            "",
            "## Memory",
            f"- Degraded: {', '.join(memory.get('degraded') or []) or 'none'}",
        ]
    )
    for item in memory.get("results") or []:
        source = item.get("source") or item.get("store") or "memory"
        text = item.get("text") or item.get("content") or item.get("snippet") or item.get("summary") or ""
        lines.append(f"- {source}: {str(text).strip()[:220]}")
    if not memory.get("results"):
        lines.append("- no structured memory rows returned")

    lines.extend(
        [
            "",
            "## Codex Hook State",
            f"- Hooks file: {'PASS' if hook.get('workspace_hooks_exists') else 'MISS'} {hook.get('workspace_hooks_file')}",
            f"- Workspace role: {hook.get('workspace_role')}",
            f"- Active root trusted: {hook.get('project_trusted')}",
            f"- Canonical root trusted: {hook.get('canonical_project_trusted')}",
            f"- Enabled hook states: {len(hook.get('enabled_states') or [])}",
            f"- Disabled hook states: {len(hook.get('disabled_states') or [])}",
            f"- Canonical enabled hook states: {len(hook.get('canonical_enabled_states') or [])}",
            f"- Notes: {', '.join(hook.get('notes') or []) or 'none'}",
            "",
            "## Orchestration Receipt Required",
            "- files_loaded: SKILL.md + genius.md + workflow/contract before expert-domain output",
            "- patterns_extracted: at least 3 concrete mechanics, not expert names",
            "- rejected_routes: name tempting routes not used",
            "- verifier_results: route, fact/prose as applicable, finalize status",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Emit a Codex Context Load Packet before substantial Antigravity work.")
    parser.add_argument("--intent", required=True, help="Raw user ask or sharpened task intent.")
    parser.add_argument("--mode", choices=MODE_CHOICES, default="deliverable")
    parser.add_argument("--format", choices=("md", "json"), default="md")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero if the context load manifest fails.")
    args = parser.parse_args()

    packet = build_packet(args.intent, args.mode)
    if args.format == "json":
        print(json.dumps(packet, indent=2))
    else:
        print(render_md(packet))
    if args.strict and packet.get("context_load_manifest", {}).get("status") != "PASS":
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
