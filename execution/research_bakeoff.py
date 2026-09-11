#!/usr/bin/env python3
"""Research OS parity contracts, capped provider ledger, imports, and blind grading.

This module is a deterministic companion behind ``/deep-research-os``.  It does
not search the web itself: Codex host web tools and provider agents gather the
evidence, while this module freezes the mission, normalizes candidate reports,
enforces provider-spend boundaries, anonymizes candidates, and computes the
requested bakeoff score.

No provider call is made from this module unless all of these are true:

* the mission explicitly allows that provider and mode;
* one-call and total-spend ledgers have room;
* the provider billing path has a machine-verifiable hard ceiling;
* the shared cost gate has a live approval token when required.

That last condition is deliberately stricter than an estimated-cost warning.
Google documents typical Deep Research Agent costs, not a per-request maximum;
therefore a local ``$10`` preference alone is not a provable provider hard cap.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parent.parent
EXEC = ROOT / "execution"
SCHEMA_VERSION = "research-parity/v1"
CANDIDATE_SCHEMA_VERSION = "research-parity-candidate/v1"
LEDGER_SCHEMA_VERSION = "research-provider-spend/v1"

ABSOLUTE_CAP_USD = 10.0
AUTHORIZATION_CAP_USD = 8.0
GEMINI_STANDARD_TYPICAL_LOW_USD = 1.0
GEMINI_STANDARD_TYPICAL_HIGH_USD = 3.0
GEMINI_MAX_TYPICAL_HIGH_USD = 7.0

SCORE_WEIGHTS = {
    "citation_accuracy": 20.0,
    "authority_resolution": 20.0,
    "decision_usefulness": 20.0,
    "counterevidence": 15.0,
    "source_breadth": 10.0,
    "cost": 10.0,
    "time": 5.0,
}

URL_RE = re.compile(r"https?://[^\s\)\]\>\"']+")


class ContractError(ValueError):
    """A mission, candidate, or receipt failed its deterministic contract."""


class SpendBlocked(RuntimeError):
    """A provider action cannot prove it will remain inside the hard boundary."""


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def read_json(path: Path) -> Dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ContractError(f"file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ContractError(f"invalid JSON in {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise ContractError(f"expected JSON object in {path}")
    return payload


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temporary.replace(path)


def slugify(value: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return value[:80] or "research-parity"


def unique_urls(text: str) -> List[str]:
    cleaned: List[str] = []
    seen = set()
    for match in URL_RE.findall(text or ""):
        url = match.rstrip(".,;:")
        if url not in seen:
            seen.add(url)
            cleaned.append(url)
    return cleaned


def unique_domains(urls: Iterable[str]) -> List[str]:
    domains = []
    seen = set()
    for url in urls:
        domain = urlparse(url).netloc.lower().removeprefix("www.")
        if domain and domain not in seen:
            seen.add(domain)
            domains.append(domain)
    return domains


@dataclass
class ResearchMission:
    mission_id: str
    exact_question: str
    as_of_date: str
    depth: str
    candidates: List[Dict[str, Any]]
    parked_concepts: List[str]
    authority_sources: List[str]
    decision_criteria: List[str]
    proof_state: str
    spending_policy: Dict[str, Any]
    source_path: str = ""

    @classmethod
    def from_path(cls, path: Path) -> "ResearchMission":
        payload = read_json(path)
        required = (
            "mission_id", "exact_question", "as_of_date", "depth", "candidates",
            "parked_concepts", "authority_sources", "decision_criteria",
            "proof_state", "spending_policy",
        )
        missing = [key for key in required if key not in payload]
        if missing:
            raise ContractError(f"mission missing required fields: {missing}")
        if payload.get("schema_version") != SCHEMA_VERSION:
            raise ContractError(
                f"mission schema must be {SCHEMA_VERSION}, got {payload.get('schema_version')!r}"
            )
        if payload["depth"] not in {"quick", "standard", "deep", "max"}:
            raise ContractError(f"invalid depth: {payload['depth']}")
        if not payload["candidates"]:
            raise ContractError("mission requires at least one eligible offer candidate")
        policy = dict(payload["spending_policy"])
        absolute = float(policy.get("absolute_cap_usd", -1))
        authorization = float(policy.get("authorization_cap_usd", -1))
        if absolute != ABSOLUTE_CAP_USD or authorization != AUTHORIZATION_CAP_USD:
            raise ContractError(
                "mission must preserve the approved $10 absolute / $8 authorization caps"
            )
        return cls(
            mission_id=str(payload["mission_id"]),
            exact_question=str(payload["exact_question"]),
            as_of_date=str(payload["as_of_date"]),
            depth=str(payload["depth"]),
            candidates=list(payload["candidates"]),
            parked_concepts=[str(x) for x in payload["parked_concepts"]],
            authority_sources=[str(x) for x in payload["authority_sources"]],
            decision_criteria=[str(x) for x in payload["decision_criteria"]],
            proof_state=str(payload["proof_state"]),
            spending_policy=policy,
            source_path=str(path.resolve()),
        )

    def to_dict(self) -> Dict[str, Any]:
        return {"schema_version": SCHEMA_VERSION, **asdict(self)}

    def frozen_prompt(self) -> str:
        offers = "\n".join(
            f"- {item.get('name')}: {item.get('definition', '')}" for item in self.candidates
        )
        parked = ", ".join(self.parked_concepts) or "none"
        criteria = "\n".join(f"- {item}" for item in self.decision_criteria)
        authority = "\n".join(f"- {item}" for item in self.authority_sources)
        return (
            f"# Frozen Deep Research Mission — {self.mission_id}\n\n"
            f"As-of date: {self.as_of_date}\n"
            f"Requested depth: {self.depth}\n"
            f"Required proof state: {self.proof_state}\n\n"
            f"## Exact question\n{self.exact_question}\n\n"
            f"## Eligible offer hypotheses\n{offers}\n\n"
            f"## Authority lock\nThe following concepts are parked and ineligible as the primary recommendation: {parked}.\n"
            "Do not treat prior polish, local validation, or category demand as exact-offer validation.\n\n"
            f"## Local authority sources\n{authority}\n\n"
            f"## Required decision criteria\n{criteria}\n\n"
            "## Evidence requirements\n"
            "Use current external evidence for current-world claims. Open and inspect sources, search for counterevidence, "
            "resolve contradictions, and cite every load-bearing claim. Keep all exact offers UNTESTED / NO EVENT until "
            "a real payment clears. Return ICP, avatar, paid pains, resisted/non-purchased framings, positioning, offer, "
            "LinkedIn proof strategy, kill gate, contradictions, limitations, and a source ledger.\n"
        )


@dataclass
class ResearchClaim:
    claim_id: str
    claim: str
    source_url: str
    support_passage: str = ""
    authority_class: str = "unknown"
    stance: str = "support"
    verification_status: str = "UNVERIFIED"
    load_bearing: bool = True
    high_risk: bool = False


@dataclass
class ResearchReceipt:
    provider: str
    engine: str
    run_id: str
    started_at: str
    completed_at: str
    elapsed_seconds: float
    source_count: int
    domain_count: int
    resolved_citations: int
    estimated_cost_usd: float
    actual_cost_usd: Optional[float]
    billing_verification: str
    stop_reason: str
    warnings: List[str] = field(default_factory=list)


class SpendLedger:
    """Mission-local provider ledger with reservation and idempotency checks."""

    def __init__(self, path: Path, mission: ResearchMission):
        self.path = path
        self.mission = mission
        if path.exists():
            self.data = read_json(path)
        else:
            self.data = {
                "schema_version": LEDGER_SCHEMA_VERSION,
                "mission_id": mission.mission_id,
                "created_at": now_iso(),
                "absolute_cap_usd": ABSOLUTE_CAP_USD,
                "authorization_cap_usd": AUTHORIZATION_CAP_USD,
                "recorded_spend_usd": 0.0,
                "pending_upper_bound_usd": 0.0,
                "provider_calls": [],
                "events": [],
            }
            self.save()
        self._validate()

    def _validate(self) -> None:
        if self.data.get("schema_version") != LEDGER_SCHEMA_VERSION:
            raise ContractError("spend ledger schema mismatch")
        if self.data.get("mission_id") != self.mission.mission_id:
            raise ContractError("spend ledger belongs to another mission")
        if float(self.data.get("absolute_cap_usd", -1)) != ABSOLUTE_CAP_USD:
            raise ContractError("spend ledger changed the $10 absolute cap")
        if float(self.data.get("authorization_cap_usd", -1)) != AUTHORIZATION_CAP_USD:
            raise ContractError("spend ledger changed the $8 authorization cap")

    def save(self) -> None:
        write_json(self.path, self.data)

    @property
    def exposure(self) -> float:
        return round(
            float(self.data.get("recorded_spend_usd", 0.0))
            + float(self.data.get("pending_upper_bound_usd", 0.0)),
            4,
        )

    def _prior_provider_calls(self, provider: str) -> List[Dict[str, Any]]:
        return [row for row in self.data.get("provider_calls", []) if row.get("provider") == provider]

    def reserve_gemini_standard(self, billing: Dict[str, Any]) -> str:
        if self._prior_provider_calls("gemini"):
            raise SpendBlocked("Gemini provider call already reserved or executed; paid retries are forbidden")
        if not bool(billing.get("machine_verified_hard_ceiling")):
            raise SpendBlocked(
                "Gemini billing has no machine-verified hard provider ceiling. Typical $1-$3 pricing is not a maximum; "
                "the approved fail-closed policy forbids the live call until a provider/project ceiling is verified."
            )
        verified_ceiling = float(billing.get("verified_remaining_ceiling_usd", -1))
        if verified_ceiling < 0 or verified_ceiling > ABSOLUTE_CAP_USD:
            raise SpendBlocked("verified provider ceiling is missing or exceeds the $10 absolute cap")
        upper = GEMINI_STANDARD_TYPICAL_HIGH_USD
        if self.exposure + upper > AUTHORIZATION_CAP_USD:
            raise SpendBlocked(
                f"projected exposure ${self.exposure + upper:.2f} exceeds ${AUTHORIZATION_CAP_USD:.2f} authorization cap"
            )
        reservation_id = hashlib.sha256(
            f"{self.mission.mission_id}:gemini:standard".encode("utf-8")
        ).hexdigest()[:16]
        row = {
            "reservation_id": reservation_id,
            "provider": "gemini",
            "mode": "standard",
            "status": "reserved",
            "reserved_at": now_iso(),
            "typical_low_usd": GEMINI_STANDARD_TYPICAL_LOW_USD,
            "reserved_upper_bound_usd": upper,
            "billing_verification": dict(billing),
            "interaction_id": "",
        }
        self.data.setdefault("provider_calls", []).append(row)
        self.data["pending_upper_bound_usd"] = round(
            float(self.data.get("pending_upper_bound_usd", 0.0)) + upper, 4
        )
        self.data.setdefault("events", []).append(
            {"at": now_iso(), "event": "reserve", "provider": "gemini", "amount_usd": upper}
        )
        self.save()
        return reservation_id

    def complete(self, reservation_id: str, interaction_id: str, estimated_cost: float) -> None:
        rows = [row for row in self.data.get("provider_calls", []) if row.get("reservation_id") == reservation_id]
        if len(rows) != 1:
            raise ContractError("reservation not found or duplicated")
        row = rows[0]
        if row.get("status") != "reserved":
            raise ContractError("reservation already finalized")
        duplicate = [
            item for item in self.data.get("provider_calls", [])
            if item is not row and interaction_id and item.get("interaction_id") == interaction_id
        ]
        if duplicate:
            raise ContractError("duplicate Gemini interaction id")
        reserved = float(row.get("reserved_upper_bound_usd", 0.0))
        estimated_cost = max(0.0, float(estimated_cost))
        self.data["pending_upper_bound_usd"] = round(
            max(0.0, float(self.data.get("pending_upper_bound_usd", 0.0)) - reserved), 4
        )
        self.data["recorded_spend_usd"] = round(
            float(self.data.get("recorded_spend_usd", 0.0)) + estimated_cost, 4
        )
        if float(self.data["recorded_spend_usd"]) > ABSOLUTE_CAP_USD:
            raise ContractError("recorded provider spend exceeded the $10 absolute cap")
        row.update({
            "status": "completed",
            "completed_at": now_iso(),
            "interaction_id": interaction_id,
            "estimated_cost_usd": estimated_cost,
        })
        self.data.setdefault("events", []).append(
            {"at": now_iso(), "event": "complete", "provider": "gemini", "amount_usd": estimated_cost}
        )
        self.save()

    def release(self, reservation_id: str, reason: str, interaction_started: bool = False) -> None:
        rows = [row for row in self.data.get("provider_calls", []) if row.get("reservation_id") == reservation_id]
        if len(rows) != 1:
            raise ContractError("reservation not found or duplicated")
        row = rows[0]
        if row.get("status") != "reserved":
            return
        reserved = float(row.get("reserved_upper_bound_usd", 0.0))
        self.data["pending_upper_bound_usd"] = round(
            max(0.0, float(self.data.get("pending_upper_bound_usd", 0.0)) - reserved), 4
        )
        row.update({
            "status": "failed_after_start" if interaction_started else "blocked_before_start",
            "completed_at": now_iso(),
            "reason": reason[:300],
        })
        if interaction_started:
            # Provider usage may be billable even when the report is invalid.
            self.data["recorded_spend_usd"] = round(
                float(self.data.get("recorded_spend_usd", 0.0)) + reserved, 4
            )
        self.data.setdefault("events", []).append({
            "at": now_iso(), "event": row["status"], "provider": "gemini",
            "amount_usd": reserved if interaction_started else 0.0,
        })
        self.save()


def _report_authority_errors(text: str, parked: Iterable[str]) -> List[str]:
    errors = []
    lowered = text.lower()
    for concept in parked:
        token = concept.lower()
        bad_patterns = (
            # Stay within one sentence so "recommend X. Angle Map remains
            # parked" does not become a false authority-drift failure.
            rf"recommend(?:ed|ation)?[^.\n]{{0,80}}{re.escape(token)}",
            rf"test now[^.\n]{{0,80}}{re.escape(token)}",
            rf"{re.escape(token)}[^.\n]{{0,80}}(?:primary|winner|best offer)",
        )
        if any(re.search(pattern, lowered) for pattern in bad_patterns):
            errors.append(f"parked concept promoted: {concept}")
    if "untested / no event" not in lowered:
        errors.append("required UNTESTED / NO EVENT proof state missing")
    return errors


def _section_hits(text: str) -> Dict[str, bool]:
    lowered = text.lower()
    return {
        "icp_avatar": "icp" in lowered and "avatar" in lowered,
        "paid_pains": "paid pain" in lowered or "paying for" in lowered,
        "resisted_framings": any(x in lowered for x in ("resisted", "not willing to pay", "non-purchased", "reject")),
        "positioning_offer": "positioning" in lowered and "offer" in lowered,
        "linkedin_proof": "linkedin" in lowered and any(x in lowered for x in ("proof", "demonstration", "content")),
        "kill_gate": "kill gate" in lowered or "park if" in lowered,
    }


def _counterevidence_count(text: str) -> int:
    lowered = text.lower()
    markers = (
        "counterevidence", "contradiction", "limitation", "downside", "risk", "resisted",
        "not willing to pay", "category demand", "no market proof",
    )
    return sum(lowered.count(marker) for marker in markers)


def parse_claim_ledger(text: str) -> Tuple[List[ResearchClaim], List[str]]:
    """Parse the report's claim table into normalized claim objects.

    This avoids a hand-maintained research JSONL side channel. The human-facing
    report is the claim source of truth; the machine ledger is generated from it.
    """
    start = "<!-- CLAIM_LEDGER_START -->"
    end = "<!-- CLAIM_LEDGER_END -->"
    if start not in text or end not in text:
        return [], ["claim ledger markers missing"]
    block = text.split(start, 1)[1].split(end, 1)[0]
    claims: List[ResearchClaim] = []
    errors: List[str] = []
    for raw in block.splitlines():
        line = raw.strip()
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if not cells or cells[0].lower() in {"id", "---"} or set(cells[0]) <= {"-", ":"}:
            continue
        if len(cells) != 9:
            errors.append(f"{cells[0] if cells else 'unknown'}: expected 9 claim columns, got {len(cells)}")
            continue
        claim_id, claim, source_url, passage, authority, stance, load_bearing, high_risk, verdict = cells
        if not re.match(r"https?://", source_url):
            errors.append(f"{claim_id}: invalid source URL")
        if len(passage) < 20:
            errors.append(f"{claim_id}: support passage is too short")
        if stance not in {"support", "counter", "limitation"}:
            errors.append(f"{claim_id}: invalid stance {stance!r}")
        if verdict not in {"VERIFIED", "TRIANGULATED", "DIRECTIONAL", "CONTRADICTED", "UNVERIFIED"}:
            errors.append(f"{claim_id}: invalid verification verdict {verdict!r}")
        claims.append(ResearchClaim(
            claim_id=claim_id,
            claim=claim,
            source_url=source_url,
            support_passage=passage,
            authority_class=authority,
            stance=stance,
            verification_status=verdict,
            load_bearing=load_bearing.lower() == "yes",
            high_risk=high_risk.lower() == "yes",
        ))
    if not claims:
        errors.append("no claims parsed")
    ids = [claim.claim_id for claim in claims]
    if len(ids) != len(set(ids)):
        errors.append("duplicate claim IDs")
    return claims, errors


def build_claim_audit(report_path: Path, out_dir: Path) -> Dict[str, Any]:
    text = report_path.read_text(encoding="utf-8")
    claims, errors = parse_claim_ledger(text)
    supported = {"VERIFIED", "TRIANGULATED"}
    load_bearing = [claim for claim in claims if claim.load_bearing]
    high_risk = [claim for claim in claims if claim.high_risk]
    audit = {
        "schema_version": "research-claim-audit/v1",
        "report_path": str(report_path.resolve()),
        "citation_claims_total": len(load_bearing),
        "citation_claims_supported": sum(claim.verification_status in supported for claim in load_bearing),
        "high_risk_claims_total": len(high_risk),
        "high_risk_claims_supported": sum(claim.verification_status in supported for claim in high_risk),
        "counterevidence_count": sum(claim.stance in {"counter", "limitation"} for claim in claims),
        "authority_classes": sorted({claim.authority_class for claim in claims}),
        "verification_method": "claim table generated after host-native page open/reopen; support passage retained",
        "errors": errors,
        "passed": bool(claims) and not errors,
        "audited_at": now_iso(),
    }
    out_dir.mkdir(parents=True, exist_ok=True)
    write_json(out_dir / "normalized-claims.json", {
        "schema_version": "research-claims/v1",
        "claims": [asdict(claim) for claim in claims],
    })
    write_json(out_dir / "claim-audit.json", audit)
    return audit


def load_audit(path: Optional[Path]) -> Dict[str, Any]:
    if path is None:
        return {}
    return read_json(path)


def validate_import_report(mission: ResearchMission, report_path: Path) -> Dict[str, Any]:
    if not report_path.exists():
        raise ContractError(f"report not found: {report_path}")
    text = report_path.read_text(encoding="utf-8")
    urls = unique_urls(text)
    domains = unique_domains(urls)
    source_floor = 15 if mission.depth == "deep" else 8
    domain_floor = 6 if mission.depth == "deep" else 4
    errors: List[str] = []
    if len(urls) < source_floor:
        errors.append(f"import has {len(urls)} resolved URLs; {source_floor} required")
    if len(domains) < domain_floor:
        errors.append(f"import has {len(domains)} source domains; {domain_floor} required")
    if re.search(r"\[cite:\s*[\d,\s]+\]", text, flags=re.IGNORECASE):
        errors.append("unresolved provider citation markers remain")
    if re.search(r"turn\d+(?:search|view|fetch)\d+", text, flags=re.IGNORECASE):
        errors.append("internal browser reference IDs remain instead of source URLs")
    if "source" not in text.lower() and "reference" not in text.lower():
        errors.append("report lacks a visible source or reference section")
    return {
        "passed": not errors,
        "errors": errors,
        "resolved_url_count": len(urls),
        "domain_count": len(domains),
        "source_floor": source_floor,
        "domain_floor": domain_floor,
    }


def score_candidate(
    mission: ResearchMission,
    provider: str,
    report_path: Path,
    receipt: Dict[str, Any],
    audit: Dict[str, Any],
) -> Dict[str, Any]:
    text = report_path.read_text(encoding="utf-8")
    urls = unique_urls(text)
    domains = unique_domains(urls)
    authority_errors = _report_authority_errors(text, mission.parked_concepts)
    sections = _section_hits(text)
    counter_count = max(int(audit.get("counterevidence_count", 0)), _counterevidence_count(text))

    claims_total = int(audit.get("citation_claims_total", 0))
    claims_supported = int(audit.get("citation_claims_supported", 0))
    high_total = int(audit.get("high_risk_claims_total", 0))
    high_supported = int(audit.get("high_risk_claims_supported", 0))
    citation_ratio = claims_supported / claims_total if claims_total else 0.0
    citation_score = SCORE_WEIGHTS["citation_accuracy"] * citation_ratio

    authority_score = SCORE_WEIGHTS["authority_resolution"]
    authority_score -= min(authority_score, 10.0 * len(authority_errors))

    decision_ratio = sum(1 for value in sections.values() if value) / len(sections)
    decision_score = SCORE_WEIGHTS["decision_usefulness"] * decision_ratio

    counter_score = min(SCORE_WEIGHTS["counterevidence"], counter_count * 5.0)

    source_floor = 15 if mission.depth == "deep" else 8
    domain_floor = 6 if mission.depth == "deep" else 4
    source_ratio = min(1.0, len(urls) / max(1, source_floor))
    domain_ratio = min(1.0, len(domains) / max(1, domain_floor))
    source_score = SCORE_WEIGHTS["source_breadth"] * ((source_ratio + domain_ratio) / 2.0)

    cost = float(receipt.get("estimated_cost_usd", receipt.get("cost_usd", 0.0)) or 0.0)
    if cost <= 0:
        cost_score = 10.0
    elif cost <= 3:
        cost_score = 8.0
    elif cost <= AUTHORIZATION_CAP_USD:
        cost_score = 5.0
    else:
        cost_score = 0.0

    elapsed = float(receipt.get("elapsed_seconds", receipt.get("duration_seconds", 0.0)) or 0.0)
    if elapsed <= 900:
        time_score = 5.0
    elif elapsed <= 1800:
        time_score = 3.0
    else:
        time_score = 1.0

    scores = {
        "citation_accuracy": round(citation_score, 2),
        "authority_resolution": round(max(0.0, authority_score), 2),
        "decision_usefulness": round(decision_score, 2),
        "counterevidence": round(counter_score, 2),
        "source_breadth": round(source_score, 2),
        "cost": round(cost_score, 2),
        "time": round(time_score, 2),
    }
    total = round(sum(scores.values()), 2)
    floors = {
        "overall_85": total >= 85.0,
        "citation_80pct": citation_score >= 16.0,
        "authority_80pct": authority_score >= 16.0,
        "load_bearing_90pct": citation_ratio >= 0.90,
        "high_risk_100pct": high_total > 0 and high_supported == high_total,
        "deep_source_floor": len(urls) >= source_floor and len(domains) >= domain_floor,
        "counterevidence_present": counter_count >= 3,
        "parked_authority_preserved": not authority_errors,
    }
    grade_complete = claims_total > 0 and high_total > 0
    return {
        "schema_version": CANDIDATE_SCHEMA_VERSION,
        "mission_id": mission.mission_id,
        "provider": provider,
        "report_path": str(report_path.resolve()),
        "receipt": receipt,
        "audit": audit,
        "metrics": {
            "source_count": len(urls),
            "domain_count": len(domains),
            "citation_ratio": round(citation_ratio, 4),
            "high_risk_claims_total": high_total,
            "high_risk_claims_supported": high_supported,
            "counterevidence_count": counter_count,
            "authority_errors": authority_errors,
            "decision_sections": sections,
        },
        "scores": scores,
        "total_score": total,
        "floors": floors,
        "grade_complete": grade_complete,
        "grade_status": "COMPLETE" if grade_complete else "PENDING_CITATION_AUDIT",
        "created_at": now_iso(),
    }


def anonymize_candidates(mission: ResearchMission, candidates: List[Dict[str, Any]], out_dir: Path) -> Dict[str, str]:
    out_dir.mkdir(parents=True, exist_ok=True)
    ordered = sorted(
        candidates,
        key=lambda item: hashlib.sha256(
            f"{mission.mission_id}:{item['provider']}".encode("utf-8")
        ).hexdigest(),
    )
    mapping: Dict[str, str] = {}
    for index, candidate in enumerate(ordered):
        blind_id = f"Candidate {chr(ord('A') + index)}"
        mapping[blind_id] = candidate["provider"]
        report_text = Path(candidate["report_path"]).read_text(encoding="utf-8")
        for provider_name in ("codex", "gemini", "chatgpt", "openai", "google"):
            report_text = re.sub(provider_name, "research system", report_text, flags=re.IGNORECASE)
        (out_dir / f"candidate-{chr(ord('a') + index)}.md").write_text(
            f"# {blind_id}\n\n{report_text}", encoding="utf-8"
        )
        sanitized = dict(candidate)
        sanitized["provider"] = blind_id
        sanitized["report_path"] = f"candidate-{chr(ord('a') + index)}.md"
        write_json(out_dir / f"candidate-{chr(ord('a') + index)}.json", sanitized)
    write_json(out_dir / "identity-map.private.json", mapping)
    return mapping


def parity_verdict(candidates: List[Dict[str, Any]]) -> Tuple[str, str]:
    by_provider = {item["provider"]: item for item in candidates}
    codex = by_provider.get("codex-native")
    required = {"codex-native", "gemini-native", "chatgpt-native"}
    if not required.issubset(by_provider):
        missing = sorted(required - set(by_provider))
        if codex and codex.get("grade_complete"):
            if missing == ["chatgpt-native"]:
                return "PARTIAL — CHATGPT REFERENCE PENDING", "native ChatGPT subscription export has not been imported"
            if missing == ["gemini-native"]:
                return "PARTIAL — GEMINI REFERENCE PENDING", "Gemini challenger has not produced an eligible sealed candidate"
            return "PARTIAL — PROVIDER REFERENCES PENDING", f"missing sealed candidate(s): {', '.join(missing)}"
        return "PARTIAL — CANDIDATE OR CITATION AUDIT PENDING", f"missing or incomplete candidate(s): {', '.join(missing)}"
    if not all(item.get("grade_complete") for item in candidates):
        return "PARTIAL — CITATION AUDIT PENDING", "one or more candidates lack claim-level citation audit"
    top = max(float(item.get("total_score", 0.0)) for item in candidates)
    codex_score = float(codex.get("total_score", 0.0)) if codex else 0.0
    floors = codex.get("floors", {}) if codex else {}
    all_floors = all(bool(value) for value in floors.values())
    if codex and all_floors and codex_score >= 85.0 and top - codex_score <= 5.0:
        return "EQUIVALENT", "Codex-native met every floor and finished within five points of the top provider"
    if codex and codex_score >= 75.0 and top - codex_score <= 10.0 and floors.get("citation_80pct") and floors.get("authority_80pct"):
        return "CONDITIONALLY EQUIVALENT", "Codex-native was close but missed at least one full parity floor"
    return "NOT EQUIVALENT", "Codex-native missed the sealed parity standard; use provider research plus Research OS import"


def build_bakeoff(mission_path: Path, candidates_dir: Path, out_dir: Path) -> Dict[str, Any]:
    mission = ResearchMission.from_path(mission_path)
    candidate_files = sorted(candidates_dir.glob("*.candidate.json"))
    candidates = [read_json(path) for path in candidate_files]
    if not candidates:
        raise ContractError(f"no *.candidate.json files found in {candidates_dir}")
    mapping = anonymize_candidates(mission, candidates, out_dir / "blind")
    verdict, reason = parity_verdict(candidates)
    reference_status = []
    status_files = sorted(candidates_dir.glob("*-blocked-receipt.json")) + sorted(
        candidates_dir.glob("*-import-status.json")
    )
    for path in status_files:
        status = read_json(path)
        reference_status.append({
            "provider": status.get("provider", path.stem),
            "candidate_status": status.get("candidate_status", "UNKNOWN"),
            "interaction_started": bool(status.get("interaction_started", False)),
            "estimated_cost_usd": float(status.get("estimated_cost_usd", 0.0) or 0.0),
            "actual_cost_usd": float(status.get("actual_cost_usd", 0.0) or 0.0),
            "stop_reason": status.get("stop_reason", "status receipt supplied"),
            "source_receipt": str(path.resolve()),
        })
    payload = {
        "schema_version": "research-parity-bakeoff/v1",
        "mission_id": mission.mission_id,
        "verdict": verdict,
        "reason": reason,
        "candidate_count": len(candidates),
        "candidates": candidates,
        "reference_status": reference_status,
        "blind_identity_map_path": str((out_dir / "blind" / "identity-map.private.json").resolve()),
        "generated_at": now_iso(),
        "spending": {
            "absolute_cap_usd": ABSOLUTE_CAP_USD,
            "authorization_cap_usd": AUTHORIZATION_CAP_USD,
            "recorded_candidate_cost_usd": round(sum(float(c.get("receipt", {}).get("estimated_cost_usd", 0.0) or 0.0) for c in candidates), 4),
        },
    }
    write_json(out_dir / "bakeoff-results.json", payload)
    rows = []
    reverse = {provider: blind for blind, provider in mapping.items()}
    for candidate in candidates:
        rows.append(
            f"| {reverse.get(candidate['provider'], 'Unknown')} | {candidate.get('total_score', 0):.2f} | "
            f"{candidate.get('grade_status')} | {candidate.get('metrics', {}).get('source_count', 0)} | "
            f"{candidate.get('metrics', {}).get('domain_count', 0)} | "
            f"${float(candidate.get('receipt', {}).get('estimated_cost_usd', 0.0) or 0.0):.2f} |"
        )
    status_rows = [
        f"| {status['provider']} | {status['candidate_status']} | "
        f"{'yes' if status['interaction_started'] else 'no'} | "
        f"${status['estimated_cost_usd']:.2f} | {status['stop_reason']} |"
        for status in reference_status
    ]
    report = (
        f"# Deep Research Parity Bakeoff\n\n"
        f"## Verdict\n\n**{verdict}** — {reason}\n\n"
        "## Blind scorecard\n\n"
        "| Candidate | Score | Grade status | Sources | Domains | Estimated API cost |\n"
        "|---|---:|---|---:|---:|---:|\n"
        + "\n".join(rows)
        + ("\n\n## Reference status\n\n"
           "| Reference | Status | Interaction started | Estimated API cost | Reason |\n"
           "|---|---|---|---:|---|\n" + "\n".join(status_rows) if status_rows else "")
        + "\n\n## Guardrails\n\n"
        f"- Absolute provider ceiling: ${ABSOLUTE_CAP_USD:.2f}\n"
        f"- Application authorization ceiling: ${AUTHORIZATION_CAP_USD:.2f}\n"
        "- No paid retry and no Gemini Max\n"
        "- Exact offer proof state remains UNTESTED / NO EVENT\n"
    )
    (out_dir / "bakeoff-report.md").write_text(report, encoding="utf-8")
    return payload


def cmd_freeze(args: argparse.Namespace) -> int:
    mission = ResearchMission.from_path(Path(args.mission))
    out_dir = Path(args.out_dir) if args.out_dir else Path(args.mission).resolve().parent
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "frozen-research-prompt.md").write_text(mission.frozen_prompt(), encoding="utf-8")
    write_json(out_dir / "normalized-mission.json", mission.to_dict())
    SpendLedger(out_dir / "spend-ledger.json", mission)
    print(json.dumps({
        "ok": True,
        "mission_id": mission.mission_id,
        "prompt": str((out_dir / "frozen-research-prompt.md").resolve()),
        "spend_ledger": str((out_dir / "spend-ledger.json").resolve()),
    }, indent=2))
    return 0


def cmd_budget_status(args: argparse.Namespace) -> int:
    mission = ResearchMission.from_path(Path(args.mission))
    out_dir = Path(args.out_dir) if args.out_dir else Path(args.mission).resolve().parent
    ledger = SpendLedger(out_dir / "spend-ledger.json", mission)
    billing = mission.spending_policy.get("gemini_billing_verification", {})
    allowed = True
    reason = "eligible"
    try:
        if ledger._prior_provider_calls("gemini"):
            raise SpendBlocked("Gemini provider call already reserved or executed")
        if not bool(billing.get("machine_verified_hard_ceiling")):
            raise SpendBlocked("provider hard ceiling is not machine verified")
        if ledger.exposure + GEMINI_STANDARD_TYPICAL_HIGH_USD > AUTHORIZATION_CAP_USD:
            raise SpendBlocked("application authorization ceiling would be exceeded")
    except SpendBlocked as exc:
        allowed = False
        reason = str(exc)
    print(json.dumps({
        "allowed": allowed,
        "reason": reason,
        "recorded_spend_usd": ledger.data.get("recorded_spend_usd", 0.0),
        "pending_upper_bound_usd": ledger.data.get("pending_upper_bound_usd", 0.0),
        "authorization_cap_usd": AUTHORIZATION_CAP_USD,
        "absolute_cap_usd": ABSOLUTE_CAP_USD,
        "billing_verification": billing,
    }, indent=2))
    return 0 if allowed else 2


def cmd_import(args: argparse.Namespace) -> int:
    mission = ResearchMission.from_path(Path(args.mission))
    report_path = Path(args.report)
    import_validation = validate_import_report(mission, report_path)
    if not import_validation["passed"]:
        raise ContractError("import validation failed: " + "; ".join(import_validation["errors"]))
    receipt = read_json(Path(args.receipt)) if args.receipt else {
        "provider": args.provider,
        "engine": args.provider,
        "run_id": "imported-" + hashlib.sha256(report_path.read_bytes()).hexdigest()[:12],
        "elapsed_seconds": 0.0,
        "estimated_cost_usd": 0.0,
        "billing_verification": "subscription_import_no_incremental_api_cost",
        "stop_reason": "completed",
    }
    audit = load_audit(Path(args.audit) if args.audit else None)
    candidate = score_candidate(mission, args.provider, report_path, receipt, audit)
    candidate["import_validation"] = import_validation
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{slugify(args.provider)}.candidate.json"
    write_json(out_path, candidate)
    print(json.dumps({"ok": True, "candidate": str(out_path.resolve()), "grade_status": candidate["grade_status"]}, indent=2))
    return 0


def cmd_audit(args: argparse.Namespace) -> int:
    out_dir = Path(args.out_dir)
    audit = build_claim_audit(Path(args.report), out_dir)
    print(json.dumps({
        "ok": audit["passed"],
        "claim_count": audit["citation_claims_total"],
        "high_risk_claim_count": audit["high_risk_claims_total"],
        "counterevidence_count": audit["counterevidence_count"],
        "audit": str((out_dir / "claim-audit.json").resolve()),
    }, indent=2))
    return 0 if audit["passed"] else 2


def cmd_bakeoff(args: argparse.Namespace) -> int:
    payload = build_bakeoff(Path(args.mission), Path(args.candidates_dir), Path(args.out_dir))
    print(json.dumps({
        "ok": True,
        "verdict": payload["verdict"],
        "candidate_count": payload["candidate_count"],
        "results": str((Path(args.out_dir) / "bakeoff-results.json").resolve()),
    }, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Research OS parity and capped bakeoff runtime")
    sub = parser.add_subparsers(dest="command", required=True)

    freeze = sub.add_parser("freeze", help="Validate a parity mission and emit one immutable prompt")
    freeze.add_argument("--mission", required=True)
    freeze.add_argument("--out-dir", default="")
    freeze.set_defaults(func=cmd_freeze)

    budget = sub.add_parser("budget-status", help="Fail-closed provider eligibility status")
    budget.add_argument("--mission", required=True)
    budget.add_argument("--out-dir", default="")
    budget.set_defaults(func=cmd_budget_status)

    audit = sub.add_parser("audit", help="Generate normalized claims and a citation audit from a report claim table")
    audit.add_argument("--report", required=True)
    audit.add_argument("--out-dir", required=True)
    audit.set_defaults(func=cmd_audit)

    imported = sub.add_parser("import", help="Normalize and score a completed research report")
    imported.add_argument("--mission", required=True)
    imported.add_argument("--provider", required=True, choices=["codex-native", "gemini-native", "chatgpt-native"])
    imported.add_argument("--report", required=True)
    imported.add_argument("--receipt", default="")
    imported.add_argument("--audit", default="")
    imported.add_argument("--out-dir", required=True)
    imported.set_defaults(func=cmd_import)

    bakeoff = sub.add_parser("bakeoff", help="Anonymize candidates and compute the sealed parity verdict")
    bakeoff.add_argument("--mission", required=True)
    bakeoff.add_argument("--candidates-dir", required=True)
    bakeoff.add_argument("--out-dir", required=True)
    bakeoff.set_defaults(func=cmd_bakeoff)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return int(args.func(args))
    except SpendBlocked as exc:
        print(json.dumps({"ok": False, "status": "BLOCKED", "reason": str(exc)}, indent=2))
        return 2
    except ContractError as exc:
        print(json.dumps({"ok": False, "status": "INVALID", "reason": str(exc)}, indent=2))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
