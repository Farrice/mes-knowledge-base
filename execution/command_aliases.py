#!/usr/bin/env python3
"""Narrow, explicit slash-command alias resolution.

Aliases apply only when the command is the leading operator instruction (bare
or after run/use/execute/invoke). Incidental mentions remain ordinary routing
text, so aliases cannot hijack broader semantic discovery.
"""

from __future__ import annotations

import re
from collections.abc import Collection


EXPLICIT_ROUTE_ALIASES: dict[str, str] = {
    "ai-topic-mining": "ai-topic-mining-engine",
}

_LEADING_COMMAND = re.compile(
    r"^\s*(?:(?:run|use|execute|invoke)\s+)?/([a-z][a-z0-9-]{2,})(?=$|[\s:])",
    re.IGNORECASE,
)


def resolve_explicit_command_alias(
    text: str,
    available_routes: Collection[str] | None = None,
) -> tuple[str, str] | None:
    """Return ``(alias, canonical_route)`` for a leading registered alias."""

    match = _LEADING_COMMAND.match(text)
    if not match:
        return None
    alias = match.group(1).lower()
    target = EXPLICIT_ROUTE_ALIASES.get(alias)
    if target is None:
        return None
    if available_routes is not None and target not in available_routes:
        return None
    return alias, target
