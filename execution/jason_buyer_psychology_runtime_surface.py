#!/usr/bin/env python3
"""Shared active-runtime inventory for the buyer-psychology canaries."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path


STATIC_PATHS = (
    "CODEX.md",
    "AGENTS.md",
    "DOMAIN_REGISTRY.md",
    "AGENT_INDEX.md",
    "SKILL_INDEX.md",
    ".codex/config.toml",
    "execution/activation_governor.py",
    "execution/artifact_router.py",
    "execution/autopilot_runtime_preflight.py",
    "execution/codex_operator_preflight.py",
    "execution/command_menu.py",
    "execution/context_retriever.py",
    "execution/creative_router.py",
    "execution/expert_router.py",
    "execution/operator_cockpit.py",
    "execution/routing_enforcer.py",
    "execution/routing_governor.py",
    "execution/routing_intelligence.py",
    "execution/skill_router_hook.py",
    "execution/tool_router.py",
    "execution/workflow_router.py",
    "semantic_libraries/antigravity/primitives/buyer-psychology-decision-intelligence-overlay.md",
)

ACTIVE_GLOBS = (
    ".agent/workflows/**/*.md",
    ".agents/skills/**/SKILL.md",
    ".agents/skills/**/workflows/**/*.md",
    ".claude/commands/**/*.md",
    ".claude/agents/**/*.md",
    "agents/**/AGENT.md",
    "skills/**/SKILL.md",
    "skills/**/workflows/**/*.md",
)

OVERLAY_DEFINITION = (
    "semantic_libraries/antigravity/primitives/"
    "buyer-psychology-decision-intelligence-overlay.md"
)

OVERLAY_POINTER_PATTERN = re.compile(
    r"buyer[\s_-]+psychology[\s_-]+decision[\s_-]+intelligence[\s_-]+overlay",
    re.IGNORECASE,
)

# The canonical title is the preferred pointer, but active surfaces can promote
# the same layer indirectly. Treat the established companion name and a
# Jason-skill-qualified "decision companion" as equivalent runtime references
# so aliases cannot bypass the exact six-pointer boundary.
LAYER_REFERENCE_PATTERN = re.compile(
    r"(?:"
    r"buyer[\s_-]+psychology[\s_-]+decision[\s_-]+intelligence[\s_-]+overlay"
    r"|buyer[\s_-]+psychology[\s_-]+decision[\s_-]+companion"
    r"|decision[\s_-]+companion[^.!?\n]{0,120}jason[\s_-]+fladlien(?:['’]s)?[\s_-]+skill"
    r"|jason[\s_-]+fladlien(?:['’]s)?[\s_-]+skill[^.!?\n]{0,120}decision[\s_-]+companion"
    r")",
    re.IGNORECASE,
)

COLD_RUNTIME_MARKERS = (
    "buyer-psychology-intelligence-layer/mechanism-registry",
    "jason_buyer_psychology_situation_compiler",
    "sales psychology situation compiler",
    "belief-reconsideration-v1",
    "focus-working-set-v1",
    "recognition-supported-pattern-v1",
    "priority-consequence-v1",
    "fit-sufficient-path-v1",
    "choice-honest-default-v1",
    "congruence-signal-alignment-v1",
    "affect-evidence-pairing-v1",
    "evidence-diagnostic-proof-v1",
    "agency-voluntary-choice-v1",
    "value-truthful-reference-v1",
    "action-buyer-authored-plan-v1",
    "experience-promise-delivery-v1",
)

FORBIDDEN_PROMOTION_PATTERNS = (
    ("always-activation", re.compile(r"\balways\s+(?:activate|apply|load|use)\b", re.IGNORECASE)),
    ("must-activation", re.compile(r"\bmust\s+(?:activate|apply|load|use)\b", re.IGNORECASE)),
    ("mandatory", re.compile(r"\bmandatory\b", re.IGNORECASE)),
    ("required", re.compile(r"\brequired\b", re.IGNORECASE)),
    ("every-task", re.compile(r"\bevery\s+(?:(?:copy|content|marketing|sales)\s+)?task\b", re.IGNORECASE)),
    ("each-assignment", re.compile(r"\beach\s+(?:(?:copy|content|marketing|sales)\s+)?assignment\b", re.IGNORECASE)),
    ("whenever", re.compile(r"\bwhenever\b", re.IGNORECASE)),
    ("default-activation", re.compile(r"\bdefault\s+to\b", re.IGNORECASE)),
    ("all-work", re.compile(r"\ball\s+(?:copy|content|marketing|sales|knowledge\s+work)\b", re.IGNORECASE)),
    ("hot-or-enforced-status", re.compile(r"\bstatus\s*:\s*(?:hot|enforced)\b", re.IGNORECASE)),
    ("global-promotion", re.compile(r"\bglobal(?:ly)?\s+(?:activate|apply|load|use|enforcement|gate)\b", re.IGNORECASE)),
    ("hard-block", re.compile(r"\bhard\s+block\b", re.IGNORECASE)),
    ("enforced", re.compile(r"\benforced\b", re.IGNORECASE)),
)


def overlay_pointer_paragraphs(text: str) -> list[str]:
    """Return normalized paragraphs that invoke the layer by title or alias."""
    return [
        paragraph.strip()
        for paragraph in re.split(r"\n\s*\n", text)
        if LAYER_REFERENCE_PATTERN.search(paragraph)
    ]


def active_runtime_paths(root: Path) -> list[Path]:
    """Return configured authority, owner, skill, command, and Python control surfaces."""
    paths = {root / relative for relative in STATIC_PATHS}
    for pattern in ACTIVE_GLOBS:
        paths.update(path for path in root.glob(pattern) if path.is_file())
    return sorted(
        (path for path in paths if path.is_file()),
        key=lambda path: str(path.relative_to(root)),
    )


def runtime_payloads(
    root: Path,
    injected_surface: tuple[str, str] | None = None,
) -> list[tuple[str, bytes]]:
    """Read active surfaces, optionally appending an adversarial test payload."""
    payloads: list[tuple[str, bytes]] = []
    for path in active_runtime_paths(root):
        relative = str(path.relative_to(root))
        data = path.read_bytes()
        if injected_surface is not None and relative == injected_surface[0]:
            data += b"\n" + injected_surface[1].encode("utf-8")
        payloads.append((relative, data))
    return payloads


def runtime_surface_digest(
    root: Path,
    injected_surface: tuple[str, str] | None = None,
) -> tuple[str, int]:
    """Hash both active paths and bytes so the receipt binds the full surface."""
    digest = hashlib.sha256()
    payloads = runtime_payloads(root, injected_surface)
    for relative, data in payloads:
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(data)
        digest.update(b"\0")
    return digest.hexdigest(), len(payloads)


def runtime_policy_attestation(root: Path) -> dict[str, object]:
    """Bind both the full runtime snapshot and policy-relevant matches.

    The policy aggregate supports focused diagnosis. The full-surface digest
    prevents an unmanifested active routing file from changing while a frozen
    canonical receipt still claims the exact six-pointer boundary.
    """
    digest = hashlib.sha256()
    pointers: list[str] = []
    violations: list[str] = []
    promotions: list[str] = []
    pointer_paragraph_hashes: dict[str, str] = {}
    payloads = runtime_payloads(root)
    full_surface_sha256, full_surface_count = runtime_surface_digest(root)
    if full_surface_count != len(payloads):
        raise RuntimeError("active runtime inventory changed during attestation")
    for relative, data in payloads:
        text = data.decode("utf-8", errors="replace")
        pointer_paragraphs = overlay_pointer_paragraphs(text)
        is_pointer = relative != OVERLAY_DEFINITION and bool(pointer_paragraphs)
        marker_hits = sorted(marker for marker in COLD_RUNTIME_MARKERS if marker in text.lower())
        if is_pointer:
            pointers.append(relative)
            pointer_paragraph_hashes[relative] = hashlib.sha256(
                "\n\n".join(pointer_paragraphs).encode("utf-8")
            ).hexdigest()
        for marker in marker_hits:
            violations.append(f"{relative}:{marker}")
        promotion_hits = promotion_hits_for_text(relative, text)
        promotions.extend(promotion_hits)
        if is_pointer or marker_hits or promotion_hits:
            digest.update(relative.encode("utf-8"))
            digest.update(b"\0")
            digest.update(("pointer" if is_pointer else "clean").encode("utf-8"))
            digest.update(b"\0")
            digest.update(pointer_paragraph_hashes.get(relative, "").encode("utf-8"))
            digest.update(b"\0")
            digest.update("\n".join(marker_hits).encode("utf-8"))
            digest.update(b"\0")
            digest.update("\n".join(promotion_hits).encode("utf-8"))
            digest.update(b"\0")
    return {
        "scannedFileCount": len(payloads),
        "fullSurfaceSha256": full_surface_sha256,
        "policyAggregateSha256": digest.hexdigest(),
        "overlayPointers": sorted(pointers),
        "pointerParagraphSha256": dict(sorted(pointer_paragraph_hashes.items())),
        "coldMarkerViolations": sorted(violations),
        "promotionViolations": sorted(promotions),
    }


def promotion_hits_for_text(relative: str, text: str) -> list[str]:
    """Return promotion-policy hits in paragraphs that invoke the overlay."""
    hits: list[str] = []
    for paragraph in overlay_pointer_paragraphs(text):
        for label, pattern in FORBIDDEN_PROMOTION_PATTERNS:
            if pattern.search(paragraph):
                hits.append(f"{relative}:{label}")
    return sorted(set(hits))


def promotion_violations(
    root: Path,
    injected_surface: tuple[str, str] | None = None,
) -> list[str]:
    """Scan every overlay-bearing runtime paragraph for hot-promotion prose."""
    violations: list[str] = []
    for relative, data in runtime_payloads(root, injected_surface):
        violations.extend(
            promotion_hits_for_text(relative, data.decode("utf-8", errors="replace"))
        )
    return sorted(set(violations))


def overlay_pointer_paths(
    root: Path,
    injected_surface: tuple[str, str] | None = None,
) -> set[str]:
    """Find pointers by canonical title or established companion aliases."""
    pointers: set[str] = set()
    for relative, data in runtime_payloads(root, injected_surface):
        if relative == OVERLAY_DEFINITION:
            continue
        text = data.decode("utf-8", errors="replace")
        if LAYER_REFERENCE_PATTERN.search(text):
            pointers.add(relative)
    return pointers
