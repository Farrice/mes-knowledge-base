#!/usr/bin/env python3
"""
Research Contract — the single boundary type every research consumer receives.

This module is the trust spine of the unified research engine. Its whole job is
to make three classes of bug *structurally impossible*:

  1. "False success" — an empty/failed API response masquerading as a completed
     result. Fixed by ResearchStatus: FAILED is a first-class return value, not a
     bare empty string the caller has to remember to check.

  2. "False findings" — a finding with no real source. Fixed by the Finding
     invariant: source_url can never be "". URL-less candidates are rejected at
     construction and routed to warnings instead.

  3. "Silent grounding" — not knowing what engine actually produced a result or
     at what depth. Fixed by the ResearchReceipt: every result carries an honest
     log of what was attempted, what succeeded, what failed, and what it cost.

Dependency-free (stdlib only) so every engine — Gemini, Perplexity, the native
floor, the avatar runner — can import it without circular dependencies.

Usage:
    from research_contract import (
        ResearchResult, ResearchStatus, EngineKind, Finding, Source,
        EngineAttempt, AttemptOutcome, validate_engine_text,
    )

    ok, reason = validate_engine_text(text, citations)
    if not ok:
        ...  # log failure, $0, status=FAILED — never log cost
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlparse


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

class ResearchStatus(str, Enum):
    """The honest status of a research result. FAILED is a real return."""
    REAL = "REAL"          # validated content that met the provenance floor for its depth
    DEGRADED = "DEGRADED"  # usable content, but below floor (thin sources, fallback engine, warnings present)
    FAILED = "FAILED"      # no validated content — caller MUST NOT persist this as a finding


class EngineKind(str, Enum):
    """Which engine actually produced the result."""
    GEMINI_DEEP = "gemini_deep"      # accelerator
    PERPLEXITY = "perplexity"        # accelerator
    NATIVE = "native"                # Claude bedrock floor (WebSearch + WebFetch + Tavily) — cannot break
    NATIVE_SWARM = "native_swarm"    # multi-agent expert swarm (fan-out + gap-fill + verify), $0
    CACHE_WARM = "cache_warm"        # served from avatar_manifold warm cache at $0


class AttemptOutcome(str, Enum):
    """What happened when an engine was tried."""
    SUCCESS = "SUCCESS"            # returned validated content
    FAILED = "FAILED"             # tried, returned empty/invalid/errored
    SKIPPED = "SKIPPED"           # not tried (budget, depth policy)
    NOT_ATTEMPTED = "NOT_ATTEMPTED"  # not reached (an earlier engine succeeded)
    ACTIVE = "ACTIVE"             # the engine that carried the final result (esp. the floor)


# ---------------------------------------------------------------------------
# Value types
# ---------------------------------------------------------------------------

@dataclass
class Source:
    url: str
    title: str = ""
    domain: str = ""
    accessed_at: str = ""

    def __post_init__(self):
        if self.url and not self.domain:
            self.domain = urlparse(self.url).netloc
        if not self.accessed_at:
            self.accessed_at = datetime.now(timezone.utc).isoformat()


class InvalidFinding(ValueError):
    """Raised when a Finding is constructed without a real source_url."""
    pass


@dataclass
class Finding:
    """A single sourced claim.

    INVARIANT: source_url is never "". A finding with no source is not a finding —
    it is an unverified assertion and belongs in warnings, not here. Construction
    raises InvalidFinding if this is violated, so the bug cannot reach disk.
    """
    claim: str
    source_url: str
    excerpt: str = ""
    confidence: str = "medium"   # high | medium | low
    finding_type: str = "data"   # data | quote | statistic | opinion | case_study
    modeled: bool = False        # True ONLY for explicitly-flagged inference; never counts as REAL grounding

    def __post_init__(self):
        if not (self.source_url and str(self.source_url).strip()):
            raise InvalidFinding(
                f"Finding has no source_url (claim={self.claim[:80]!r}). "
                "URL-less candidates must go to ResearchResult.warnings, never findings."
            )


@dataclass
class EngineAttempt:
    """One row in the Research Receipt — what an engine did, honestly."""
    engine: EngineKind
    outcome: AttemptOutcome
    detail: str = ""             # "14 sources", "empty body", "budget $0.31 < $0.50", "bad API key"
    cost_logged: float = 0.0     # what was actually charged. FAILED/SKIPPED are always 0.0.
    sources_found: int = 0
    duration_seconds: float = 0.0


# ---------------------------------------------------------------------------
# The result contract
# ---------------------------------------------------------------------------

@dataclass
class ResearchResult:
    """The single boundary contract every consumer receives.

    No more silent empty strings: status is explicit, cost is only ever the
    validated spend, and the receipt records exactly what happened.
    """
    query: str
    status: ResearchStatus
    engine_used: EngineKind
    findings: List[Finding] = field(default_factory=list)
    sources: List[Source] = field(default_factory=list)
    synthesis: str = ""
    provenance_pct: float = 0.0      # % of total claims that carried a real source (0-100)
    unique_domains: int = 0
    source_count: int = 0
    cost_usd: float = 0.0            # ONLY incremented for calls that returned validated content
    duration_seconds: float = 0.0
    depth: str = "standard"          # quick | standard | deep | max  (requested)
    depth_achieved: str = ""         # what was actually achieved (may be lower if accelerator failed)
    warnings: List[str] = field(default_factory=list)
    quarantined_count: int = 0       # claims dropped for missing source_url
    attempts: List[EngineAttempt] = field(default_factory=list)  # the receipt log
    timestamp: str = ""

    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now(timezone.utc).isoformat()
        if not self.depth_achieved:
            self.depth_achieved = self.depth

    # ----- properties -----

    @property
    def is_usable(self) -> bool:
        return self.status in (ResearchStatus.REAL, ResearchStatus.DEGRADED)

    # ----- aggregates -----

    def recompute_aggregates(self) -> "ResearchResult":
        """Derive source_count, unique_domains, and provenance_pct from current
        findings/sources. provenance = sourced findings / (findings + quarantined)."""
        domains = {s.domain for s in self.sources if s.domain}
        # findings carry their own urls too — fold them in
        for f in self.findings:
            d = urlparse(f.source_url).netloc
            if d:
                domains.add(d)
        urls = {s.url for s in self.sources if s.url} | {f.source_url for f in self.findings}
        self.source_count = len(urls)
        self.unique_domains = len(domains)
        total_claims = len(self.findings) + self.quarantined_count
        self.provenance_pct = round(100.0 * len(self.findings) / total_claims, 1) if total_claims else 0.0
        return self

    # ----- serialization -----

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["status"] = self.status.value
        d["engine_used"] = self.engine_used.value
        d["attempts"] = [
            {**asdict(a), "engine": a.engine.value, "outcome": a.outcome.value}
            for a in self.attempts
        ]
        return d

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=False)

    # ----- the Research Receipt (the capstone) -----

    def render_receipt(self) -> str:
        """Render the honest provenance banner. Answers at a glance:
        'what depth did I actually get, and can I trust it?'"""
        bar = "═" * 60
        lines = [
            f"═══ RESEARCH RECEIPT {'═' * 40}",
            f"Query:         {self.query[:80]}",
            f"Depth:         requested={self.depth}  ·  achieved={self.depth_achieved}",
            f"Status:        {self.status.value}",
            f"Engine used:   {self.engine_used.value}",
            "Attempts:",
        ]
        if not self.attempts:
            lines.append("  • (none recorded)")
        for a in self.attempts:
            tail = f" ({a.detail})" if a.detail else ""
            cost = f"  ${a.cost_logged:.2f}" if a.cost_logged else "  $0.00"
            lines.append(f"  • {a.engine.value:<12} → {a.outcome.value:<13}{cost}{tail}")
        lines += [
            f"Provenance:    {self.provenance_pct:.0f}% of claims sourced · "
            f"{self.unique_domains} domains · {self.source_count} sources",
            f"Cost this run: ${self.cost_usd:.2f}",
        ]
        if self.quarantined_count:
            lines.append(f"Quarantined:   {self.quarantined_count} claim(s) dropped for missing source URL")
        if self.warnings:
            lines.append("Warnings:")
            for w in self.warnings:
                lines.append(f"  ! {w}")
        else:
            lines.append("Warnings:      none")
        lines.append(bar)
        return "\n".join(lines)

    def to_markdown(self) -> str:
        """Full report = receipt banner + synthesis + sourced findings."""
        out = ["```", self.render_receipt(), "```", ""]
        if self.synthesis:
            out += [self.synthesis, ""]
        if self.findings:
            out.append("## Findings\n")
            for i, f in enumerate(self.findings, 1):
                tag = " `[MODELED]`" if f.modeled else ""
                out.append(f"{i}. {f.claim}{tag}")
                if f.excerpt:
                    out.append(f"   > {f.excerpt[:300]}")
                out.append(f"   — {f.source_url}  ·  confidence: {f.confidence}")
                out.append("")
        if self.sources:
            out.append("## Sources\n")
            for i, s in enumerate(self.sources, 1):
                label = s.title or s.domain or s.url
                out.append(f"{i}. [{label}]({s.url})")
        return "\n".join(out)


# ---------------------------------------------------------------------------
# The shared success gate
# ---------------------------------------------------------------------------

_PLACEHOLDER_PATTERNS = (
    "no findings", "no results", "i cannot", "i'm unable", "unable to",
    "no information", "could not find",
)


def validate_engine_text(text: Optional[str], citations: Optional[List[str]] = None
                         ) -> Tuple[bool, str]:
    """The shared success gate. Called by every engine client BEFORE any cost
    accounting. Returns (ok, reason).

    An engine response is only "valid content" if it is non-empty, has real
    substance (not just a one-line refusal/placeholder), and isn't obviously a
    failure message. This is what stops the false-usage bug: cost is logged only
    when this returns ok=True.
    """
    if text is None:
        return False, "none_response"
    stripped = text.strip()
    if not stripped:
        return False, "empty_content"
    # Substance floor — a real research answer is more than a sentence fragment.
    if len(stripped) < 40:
        return False, "too_short"
    low = stripped.lower()
    # A short body that is *only* a refusal/placeholder is a failure, not content.
    if len(stripped) < 200 and any(p in low for p in _PLACEHOLDER_PATTERNS):
        return False, "placeholder_or_refusal"
    return True, "ok"


def extract_urls(text: str) -> List[str]:
    """Deterministic URL extraction — shared by the quality gate and the floor."""
    if not text:
        return []
    return list(dict.fromkeys(re.findall(r"https?://[^\s\)\"'>\]]+", text)))


# ---------------------------------------------------------------------------
# Self-test (no network, no side effects)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # Construct + serialize + receipt render — the P0 verification.
    r = ResearchResult(
        query="S&C coaching buyer psychology 2026",
        status=ResearchStatus.REAL,
        engine_used=EngineKind.GEMINI_DEEP,
        depth="deep",
    )
    r.attempts.append(EngineAttempt(EngineKind.GEMINI_DEEP, AttemptOutcome.SUCCESS,
                                    detail="14 sources", cost_logged=0.0, sources_found=14))
    r.attempts.append(EngineAttempt(EngineKind.PERPLEXITY, AttemptOutcome.NOT_ATTEMPTED,
                                    detail="gemini succeeded"))
    r.findings.append(Finding(claim="Market grew 18% YoY", source_url="https://example.com/report",
                              excerpt="...", confidence="high", finding_type="statistic"))
    r.sources.append(Source(url="https://example.com/report", title="Industry Report 2026"))
    r.recompute_aggregates()

    print(r.render_receipt())
    print()
    print("to_dict OK:", isinstance(r.to_dict(), dict))
    print("to_json bytes:", len(r.to_json()))

    # Invariant check — a URL-less finding must be rejected at construction.
    try:
        Finding(claim="unsourced claim", source_url="")
        print("INVARIANT FAILED: empty source_url accepted")
    except InvalidFinding:
        print("invariant OK: empty source_url rejected")

    # Success gate checks
    assert validate_engine_text("", [])[0] is False
    assert validate_engine_text(None, [])[0] is False
    assert validate_engine_text("x" * 500, [])[0] is True
    assert validate_engine_text("I cannot help with that.", [])[0] is False
    print("validate_engine_text OK")
