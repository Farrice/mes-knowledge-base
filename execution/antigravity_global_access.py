#!/usr/bin/env python3
"""Classify requests for the thin Antigravity global-access layer.

This module is intentionally narrow. It protects the control-plane owner for
global-access and hot/cold reconciliation work without turning every mention of
Antigravity, plugins, or global configuration into a system route.
"""

from __future__ import annotations

import re
from typing import Any


ANTIGRAVITY_MARKERS = (
    "google antigravity",
    "antigravity workspace",
    "antigravity skill",
    "antigravity workflow",
    "antigravity operator",
)

GLOBAL_SURFACE_MARKERS = (
    "global codex",
    "global access",
    "global skill",
    "globally in codex",
    "skill manifest",
    "personal plugin",
    "workflow menu",
    "slash command menu",
    "context rot",
    "hot/cold",
    "hot cold",
)

RECONCILE_MARKERS = (
    "audit",
    "reconcile",
    "repair",
    "routing",
    "route ownership",
    "hot/cold",
    "hot cold",
    "context rot",
    "access layer",
    "not firing",
    "not working",
    "drift",
)

BUILD_MARKERS = (
    "build",
    "implement",
    "create",
    "package",
    "plugin",
    "manifest",
    "install",
)


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value.lower()).strip()


def _hits(query: str, markers: tuple[str, ...]) -> list[str]:
    return [marker for marker in markers if marker in query]


def classify_global_access_intent(prompt: str) -> dict[str, Any]:
    """Return a deterministic owner for Antigravity global-access work.

    Reconciliation and repair are owned by /system-audit. A pure, explicit
    build/package request is owned by /source-to-skill-system. A combined
    request keeps /system-audit as the function owner and records the builder
    as a bounded support gate.
    """

    query = normalize(prompt)
    antigravity_hits = _hits(query, ANTIGRAVITY_MARKERS)
    surface_hits = _hits(query, GLOBAL_SURFACE_MARKERS)
    if not antigravity_hits or not surface_hits:
        return {
            "matched": False,
            "route": "",
            "lane": "",
            "stage": "",
            "support_gates": [],
            "reason": "",
            "evidence": [],
            "confidence": 0,
        }

    reconcile_hits = _hits(query, RECONCILE_MARKERS)
    build_hits = _hits(query, BUILD_MARKERS)
    if reconcile_hits:
        route = "system-audit"
        stage = "reconcile-then-build" if build_hits else "reconcile"
        support = ["source-to-skill-system"] if build_hits else []
        reason = (
            "Antigravity global access changes require routing and hot/cold proof before packaging."
        )
        lane = "system-failure"
    else:
        route = "source-to-skill-system"
        stage = "build"
        support = ["system-audit"]
        reason = (
            "An explicit Antigravity global manifest or plugin build belongs to the connected skill-system builder."
        )
        lane = "system-build"

    evidence = antigravity_hits[:2] + surface_hits[:3] + reconcile_hits[:2] + build_hits[:2]
    return {
        "matched": True,
        "route": route,
        "lane": lane,
        "stage": stage,
        "support_gates": support,
        "reason": reason,
        "evidence": evidence,
        "confidence": 97,
    }

