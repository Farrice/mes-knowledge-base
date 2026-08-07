#!/usr/bin/env python3
"""Local runtime for the Search Content Mastery companion OS.

The runtime is intentionally import-first and standard-library only. It creates
portable project packs, produces transparent records and handoffs, normalizes
local exports, and appends observed events. It does not browse, publish, call a
connector, schedule work, or mutate skills from performance data.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import sys
from collections import defaultdict
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parent.parent
SCHEMA_ROOT = ROOT / "schemas" / "search-content-mastery"
IMPORT_PROFILES_PATH = SCHEMA_ROOT / "import-profiles.json"

OUTCOME_STAGES = (
    "PREDICTED",
    "PUBLISHED",
    "INDEXED",
    "RANKED",
    "CITED",
    "TRAFFIC",
    "CONVERTED",
    "COLLECTED",
)

DIMENSIONS = (
    "intent_fit",
    "information_gain",
    "source_quality",
    "technical_on_page_readiness",
    "aeo_geo_readiness",
    "human_usefulness",
    "format_fit",
    "conversion_alignment",
    "claim_risk",
    "measurement_readiness",
)

CONTEXT_FILES = {
    "entity_truth": "context/entity-truth.json",
    "brand_context": "context/brand-offer-audience-voice.json",
    "source_policy": "context/source-policy.json",
    "claim_policy": "context/claim-policy.json",
    "competitor_patterns": "context/competitor-patterns.json",
    "search_inputs": "context/search-inputs.json",
    "operator_taste": "context/operator-taste.json",
}

LEDGER_FILES = {
    "execution": "ledgers/execution.jsonl",
    "outcomes": "ledgers/outcomes.jsonl",
    "recommendations": "ledgers/recommendations.jsonl",
}

SERVICE_ARTIFACTS = (
    "project_manifest",
    "intake",
    "entity_context_pack",
    "baseline_audit",
    "opportunity_map",
    "improved_answer_asset",
    "media_brief",
    "evaluation_receipt",
    "experiment_plan",
)

CHANNEL_ROUTES = {
    "article": ["/search-content-mastery", "/create", "nathan-gotch-ai-seo", "ethan-smith-aeo"],
    "local_service_page": ["/search-content-mastery", "/create", "nathan-gotch-ai-seo", "ethan-smith-aeo"],
    "ecommerce_page": ["/search-content-mastery", "/create", "nathan-gotch-ai-seo", "ethan-smith-aeo"],
    "linkedin_post": ["/search-content-mastery", "/create", "farrice-voice-card"],
    "video_script": ["/search-content-mastery", "/create", "video craft master", "skills/generate"],
    "visual_brief": ["/search-content-mastery", "/create", "/fantastic-studio", "skills/generate"],
    "audio_script": ["/search-content-mastery", "/create", "audio craft master", "skills/generate"],
}


class ContractError(RuntimeError):
    """Raised when an input violates an explicit system contract."""

    def __init__(self, code: str, message: str, details: Any | None = None) -> None:
        super().__init__(message)
        self.code = code
        self.details = details


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "search-project"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def record_id(prefix: str, *parts: Any) -> str:
    payload = json.dumps([*parts, utc_now()], sort_keys=True, default=str).encode("utf-8")
    return f"{prefix}-{sha256_bytes(payload)[:12]}"


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ContractError("MISSING_FILE", f"Required file does not exist: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ContractError("MALFORMED_JSON", f"Malformed JSON in {path}: {exc}") from exc


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temporary.replace(path)


def append_jsonl(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, sort_keys=True) + "\n")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ContractError("MALFORMED_JSONL", f"Malformed JSONL at {path}:{number}: {exc}") from exc
        if not isinstance(value, dict):
            raise ContractError("MALFORMED_JSONL", f"JSONL row must be an object at {path}:{number}")
        rows.append(value)
    return rows


def require_keys(payload: dict[str, Any], required: Iterable[str], label: str) -> None:
    missing = [key for key in required if key not in payload]
    if missing:
        raise ContractError("INCOMPLETE_SCHEMA", f"{label} is missing required fields: {', '.join(missing)}", missing)


def reject_unknown_keys(payload: dict[str, Any], allowed: Iterable[str], label: str) -> None:
    unknown = sorted(set(payload) - set(allowed))
    if unknown:
        raise ContractError("UNKNOWN_SCHEMA", f"{label} has unknown fields: {', '.join(unknown)}", unknown)


def parse_date_value(value: Any, label: str) -> date:
    text = str(value).strip()
    if not text:
        raise ContractError("MALFORMED_DATE", f"{label} is blank")
    try:
        if "T" in text:
            return datetime.fromisoformat(text.replace("Z", "+00:00")).date()
        return date.fromisoformat(text[:10])
    except ValueError as exc:
        raise ContractError("MALFORMED_DATE", f"{label} must be ISO-8601, received {text!r}") from exc


def project_path(project: str | Path) -> Path:
    return Path(project).expanduser().resolve()


def safe_project_ref(project: Path, ref: str) -> Path:
    candidate = (project / ref).resolve() if not Path(ref).is_absolute() else Path(ref).resolve()
    if not candidate.is_relative_to(project):
        raise ContractError("UNSAFE_REFERENCE", f"Project reference escapes the pack: {ref}")
    return candidate


def load_manifest(project: Path) -> dict[str, Any]:
    manifest = read_json(project / "manifest.json")
    validate_manifest(manifest)
    return manifest


def validate_manifest(manifest: dict[str, Any]) -> None:
    required = (
        "schema_version", "record_type", "project_id", "project_name", "vertical",
        "created_at", "proof_state", "references", "ledgers", "boundaries",
    )
    allowed = (*required, "extensions")
    require_keys(manifest, required, "SearchProjectManifest")
    reject_unknown_keys(manifest, allowed, "SearchProjectManifest")
    if manifest["schema_version"] != "search-project-manifest/v1" or manifest["record_type"] != "SearchProjectManifest":
        raise ContractError("SCHEMA_VERSION", "SearchProjectManifest must use search-project-manifest/v1")
    if manifest["proof_state"] not in {"UNTESTED", "RUNTIME_OBSERVED"}:
        raise ContractError("PROOF_STATE", "Manifest proof_state must be UNTESTED or RUNTIME_OBSERVED")
    if not isinstance(manifest["references"], dict) or set(manifest["references"]) != set(CONTEXT_FILES):
        raise ContractError("INCOMPLETE_SCHEMA", "Manifest references must name every portable context file")
    if not isinstance(manifest["ledgers"], dict) or set(manifest["ledgers"]) != set(LEDGER_FILES):
        raise ContractError("INCOMPLETE_SCHEMA", "Manifest ledgers must name execution, outcomes, and recommendations")


def validate_brief(brief: dict[str, Any]) -> None:
    required = (
        "schema_version", "record_type", "brief_id", "project_id", "created_at", "status",
        "target_query", "intent", "audience", "information_gain_requirement", "source_receipts",
        "structural_pattern", "channel", "cta", "risk_boundary", "measurement_hypothesis",
    )
    allowed = (*required, "operator_taste_refs", "notes")
    require_keys(brief, required, "SearchBrief")
    reject_unknown_keys(brief, allowed, "SearchBrief")
    if brief["schema_version"] != "search-brief/v1" or brief["record_type"] != "SearchBrief":
        raise ContractError("SCHEMA_VERSION", "SearchBrief must use search-brief/v1")
    if brief["status"] not in {"DRAFT", "APPROVED", "REJECTED"}:
        raise ContractError("INVALID_STATUS", "SearchBrief status must be DRAFT, APPROVED, or REJECTED")
    if brief["intent"] not in {"informational", "commercial", "transactional", "navigational", "local", "mixed"}:
        raise ContractError("INVALID_INTENT", f"Unknown search intent: {brief['intent']}")
    if brief["channel"] not in CHANNEL_ROUTES:
        raise ContractError("INVALID_CHANNEL", f"Unknown channel: {brief['channel']}")
    if not brief["source_receipts"] or not all(str(item).strip() for item in brief["source_receipts"]):
        raise ContractError("MISSING_SOURCE_RECEIPT", "SearchBrief requires at least one non-empty source receipt")
    hypothesis = brief["measurement_hypothesis"]
    require_keys(hypothesis, ("prediction", "primary_stage", "observation_window_days", "falsifier"), "measurement_hypothesis")
    reject_unknown_keys(hypothesis, ("prediction", "primary_stage", "observation_window_days", "falsifier"), "measurement_hypothesis")
    if hypothesis["primary_stage"] not in OUTCOME_STAGES:
        raise ContractError("INVALID_STAGE", f"Unknown measurement stage: {hypothesis['primary_stage']}")
    if not isinstance(hypothesis["observation_window_days"], int) or hypothesis["observation_window_days"] < 1:
        raise ContractError("INVALID_WINDOW", "observation_window_days must be a positive integer")


def validate_project(project: Path) -> dict[str, Any]:
    manifest = load_manifest(project)
    missing: list[str] = []
    malformed: list[str] = []
    for ref in manifest["references"].values():
        path = safe_project_ref(project, ref)
        if not path.exists():
            missing.append(ref)
            continue
        try:
            value = read_json(path)
        except ContractError:
            malformed.append(ref)
            continue
        if not isinstance(value, dict):
            malformed.append(ref)
    for ref in manifest["ledgers"].values():
        path = safe_project_ref(project, ref)
        if not path.exists():
            missing.append(ref)
        else:
            read_jsonl(path)
    if missing or malformed:
        raise ContractError("INVALID_PROJECT_PACK", "Portable project pack failed validation", {"missing": missing, "malformed": malformed})
    return manifest


def execution_event(project: Path, manifest: dict[str, Any], action: str, artifact: str, status: str = "PASS") -> None:
    append_jsonl(
        safe_project_ref(project, manifest["ledgers"]["execution"]),
        {
            "schema_version": "search-execution-event/v1",
            "event_id": record_id("exec", manifest["project_id"], action, artifact),
            "project_id": manifest["project_id"],
            "action": action,
            "artifact": artifact,
            "status": status,
            "recorded_at": utc_now(),
        },
    )


def foundation(args: argparse.Namespace) -> dict[str, Any]:
    project = project_path(args.project)
    context: dict[str, Any] = {}
    if args.context:
        context = read_json(Path(args.context).expanduser().resolve())
        if not isinstance(context, dict):
            raise ContractError("UNKNOWN_SCHEMA", "Foundation context must be a JSON object")
        reject_unknown_keys(context, ("project_name", "vertical", *CONTEXT_FILES), "foundation context")

    if args.resume:
        manifest = validate_project(project)
        return {"status": "VALID", "project": str(project), "manifest": str(project / "manifest.json"), "project_id": manifest["project_id"]}

    name = args.name or context.get("project_name")
    vertical = args.vertical or context.get("vertical")
    if not name or not vertical:
        raise ContractError("INCOMPLETE_SCHEMA", "foundation requires explicit --name and --vertical or equivalent context fields")
    if (project / "manifest.json").exists():
        raise ContractError("PROJECT_EXISTS", f"Project pack already exists: {project}; pass --resume to validate it")

    project.mkdir(parents=True, exist_ok=True)
    for directory in ("context", "ledgers", "imports/raw", "imports/normalized", "briefs", "handoffs", "scores", "assets", "receipts"):
        (project / directory).mkdir(parents=True, exist_ok=True)

    defaults = {
        "entity_truth": {"schema_version": "search-context/v1", "entities": [], "verified_facts": [], "unresolved": []},
        "brand_context": {"schema_version": "search-context/v1", "brand": {}, "offer": {}, "audience": {}, "voice": {}},
        "source_policy": {"schema_version": "search-context/v1", "allowed_sources": [], "prohibited_sources": [], "claim_labels": ["OBSERVED", "INFERRED", "CORROBORATED", "UNCONFIRMED"]},
        "claim_policy": {"schema_version": "search-context/v1", "allowed": [], "requires_review": [], "prohibited": []},
        "competitor_patterns": {"schema_version": "search-context/v1", "patterns": [], "evidence_refs": []},
        "search_inputs": {"schema_version": "search-context/v1", "queries": [], "surfaces": [], "imports": []},
        "operator_taste": {"schema_version": "search-context/v1", "decisions": [], "overrides": []},
    }
    for key, ref in CONTEXT_FILES.items():
        value = context.get(key, defaults[key])
        if not isinstance(value, dict):
            raise ContractError("UNKNOWN_SCHEMA", f"Foundation field {key} must be an object")
        write_json(project / ref, value)
    for ref in LEDGER_FILES.values():
        (project / ref).touch(exist_ok=True)

    project_id = slugify(name)
    manifest = {
        "schema_version": "search-project-manifest/v1",
        "record_type": "SearchProjectManifest",
        "project_id": project_id,
        "project_name": name,
        "vertical": vertical,
        "created_at": utc_now(),
        "proof_state": "UNTESTED",
        "references": CONTEXT_FILES,
        "ledgers": LEDGER_FILES,
        "boundaries": [
            "No publishing, outreach, connector writes, scheduling, deployment, payment creation, or paid generation.",
            "Scores are predictions; outcome stages require separate dated evidence.",
            "Workflow recommendations are queue-only and require human promotion.",
        ],
        "extensions": {},
    }
    validate_manifest(manifest)
    write_json(project / "manifest.json", manifest)
    execution_event(project, manifest, "foundation", "manifest.json")
    return {"status": "CREATED", "project": str(project), "manifest": str(project / "manifest.json"), "project_id": project_id}


def audit(args: argparse.Namespace) -> dict[str, Any]:
    project = project_path(args.project)
    manifest = validate_project(project)
    context_summary: dict[str, Any] = {}
    warnings: list[str] = []
    for key, ref in manifest["references"].items():
        value = read_json(safe_project_ref(project, ref))
        nonempty = any(bool(item) for field, item in value.items() if field != "schema_version")
        context_summary[key] = {"ref": ref, "populated": nonempty}
        if not nonempty:
            warnings.append(f"{key} is structurally valid but contains no project evidence")
    receipt = {
        "schema_version": "search-baseline-audit/v1",
        "record_type": "SearchBaselineAudit",
        "audit_id": record_id("audit", manifest["project_id"]),
        "project_id": manifest["project_id"],
        "created_at": utc_now(),
        "proof_state": manifest["proof_state"],
        "context": context_summary,
        "warnings": warnings,
        "verdict": "READY_FOR_PLANNING" if not warnings else "CONTEXT_GAPS_VISIBLE",
    }
    output = project / "receipts" / f"{receipt['audit_id']}.json"
    write_json(output, receipt)
    execution_event(project, manifest, "audit", str(output.relative_to(project)))
    return {"status": receipt["verdict"], "receipt": str(output), "warnings": warnings}


def plan(args: argparse.Namespace) -> dict[str, Any]:
    project = project_path(args.project)
    manifest = validate_project(project)
    supplied = read_json(Path(args.input).expanduser().resolve())
    if not isinstance(supplied, dict):
        raise ContractError("UNKNOWN_SCHEMA", "SearchBrief input must be a JSON object")
    allowed = (
        "status", "target_query", "intent", "audience", "information_gain_requirement",
        "source_receipts", "structural_pattern", "channel", "cta", "risk_boundary",
        "measurement_hypothesis", "operator_taste_refs", "notes",
    )
    required = allowed[:11]
    reject_unknown_keys(supplied, allowed, "SearchBrief input")
    require_keys(supplied, required, "SearchBrief input")
    brief = {
        "schema_version": "search-brief/v1",
        "record_type": "SearchBrief",
        "brief_id": record_id("brief", manifest["project_id"], supplied["target_query"], supplied["channel"]),
        "project_id": manifest["project_id"],
        "created_at": utc_now(),
        **supplied,
    }
    validate_brief(brief)
    output = project / "briefs" / f"{brief['brief_id']}.json"
    write_json(output, brief)
    execution_event(project, manifest, "plan", str(output.relative_to(project)))
    return {"status": brief["status"], "brief": str(output), "brief_id": brief["brief_id"]}


def create_handoff(args: argparse.Namespace) -> dict[str, Any]:
    project = project_path(args.project)
    manifest = validate_project(project)
    brief_path = Path(args.brief).expanduser().resolve()
    brief = read_json(brief_path)
    validate_brief(brief)
    if brief["project_id"] != manifest["project_id"]:
        raise ContractError("PROJECT_MISMATCH", "SearchBrief belongs to a different project")
    if brief["status"] != "APPROVED":
        raise ContractError("APPROVAL_REQUIRED", "Only an APPROVED SearchBrief may enter production routing")
    channel = brief["channel"]
    handoff = {
        "schema_version": "search-production-handoff/v1",
        "record_type": "SearchProductionHandoff",
        "handoff_id": record_id("handoff", brief["brief_id"]),
        "project_id": manifest["project_id"],
        "brief_id": brief["brief_id"],
        "created_at": utc_now(),
        "channel": channel,
        "route": CHANNEL_ROUTES[channel],
        "inputs": {
            "brief_ref": str(brief_path),
            "project_manifest": str(project / "manifest.json"),
            "source_receipts": brief["source_receipts"],
            "operator_taste_refs": brief.get("operator_taste_refs", []),
        },
        "output_contract": "Produce the channel-native asset, then return it to /search-content-mastery score before any external action.",
        "risk_boundary": brief["risk_boundary"],
        "paid_generation": "APPROVAL_REQUIRED" if channel in {"video_script", "visual_brief", "audio_script"} else "NOT_REQUESTED",
        "external_action": "NO_PERMISSION",
    }
    output = project / "handoffs" / f"{handoff['handoff_id']}.json"
    write_json(output, handoff)
    execution_event(project, manifest, "create", str(output.relative_to(project)))
    return {"status": "HANDOFF_READY", "handoff": str(output), "route": handoff["route"]}


def check(check_id: str, passed: bool, points: float, evidence: str) -> dict[str, Any]:
    return {"id": check_id, "passed": bool(passed), "points": points if passed else 0, "available_points": points, "evidence": evidence}


def dimension(checks: list[dict[str, Any]]) -> dict[str, Any]:
    available = sum(item["available_points"] for item in checks)
    earned = sum(item["points"] for item in checks)
    score = round((earned / available) * 10, 2) if available else 0.0
    return {"deterministic_score": score, "checks": checks}


def title_text(text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return text.splitlines()[0].strip() if text.splitlines() else ""


def non_negated_risk_terms(text: str) -> list[str]:
    """Return asserted outcome-guarantee terms while ignoring disclaimers.

    Claim-safe assets must be able to state "does not guarantee" or "will not
    rank" without the boundary itself reducing the claim-risk score. Expert
    judgment still handles more distant or rhetorically ambiguous negation.
    """
    lowered = text.lower()
    pattern = re.compile(
        r"\b(?:guarantee(?:d)?|always ranks?|rankings? on command|zero risk|will rank|will be cited)\b"
    )
    negation = re.compile(r"\b(?:does not|do not|did not|cannot|can't|will not|won't|never|without|no)\b")
    asserted: list[str] = []
    for match in pattern.finditer(lowered):
        sentence_start = max(lowered.rfind(mark, 0, match.start()) for mark in (".", "!", "?", "\n")) + 1
        prefix = lowered[max(sentence_start, match.start() - 120):match.start()]
        if negation.search(prefix):
            continue
        asserted.append(match.group(0))
    return asserted


def deterministic_dimensions(text: str, brief: dict[str, Any]) -> dict[str, dict[str, Any]]:
    lower = text.lower()
    title = title_text(text).lower()
    query = brief["target_query"].lower()
    query_tokens = {token for token in re.findall(r"[a-z0-9]+", query) if len(token) > 2}
    audience_tokens = {token for token in re.findall(r"[a-z0-9]+", brief["audience"].lower()) if len(token) > 3}
    token_hits = sum(1 for token in query_tokens if token in lower)
    audience_hits = sum(1 for token in audience_tokens if token in lower)
    urls = re.findall(r"https?://[^\s)>]+", text)
    citation_markers = re.findall(r"\[[0-9]+\]|\([^)]*(?:source|study|report|receipt)[^)]*\)", lower)
    headings = [line for line in text.splitlines() if line.lstrip().startswith("#")]
    bullets = [line for line in text.splitlines() if re.match(r"\s*(?:[-*]|\d+\.)\s+", line)]
    words = re.findall(r"\b\w+\b", text)
    sentences = [item for item in re.split(r"[.!?]+", text) if item.strip()]
    average_sentence = len(words) / max(1, len(sentences))
    source_refs_visible = sum(1 for ref in brief["source_receipts"] if str(ref).lower() in lower)
    numbers = re.findall(r"(?<!\w)\d+(?:\.\d+)?%?", text)
    guarantee_terms = non_negated_risk_terms(text)
    absolute_terms = re.findall(r"\b(?:everyone|nobody|never fails|all searches|the only way)\b", lower)
    direct_answer = any(marker in " ".join(words[:80]).lower() for marker in (" is ", " means ", " the answer ", "because "))
    question_heading = any("?" in heading for heading in headings)
    cta_present = brief["cta"].lower() in lower
    info_markers = any(marker in lower for marker in ("original data", "we observed", "our analysis", "case study", "first-hand", "firsthand", "interviewed", "dataset"))
    worked_example = any(marker in lower for marker in ("for example", "example:", "case study", "here is", "step 1", "scenario"))
    intent_markers = {
        "informational": ("how", "why", "what", "guide", "steps"),
        "commercial": ("best", "compare", "versus", "choice", "recommend"),
        "transactional": ("buy", "book", "start", "price", "order"),
        "navigational": ("contact", "login", "location", "official"),
        "local": ("near", "local", "area", "city", "service"),
        "mixed": ("how", "best", "start", "compare"),
    }
    intent_present = any(marker in lower for marker in intent_markers[brief["intent"]])

    dimensions: dict[str, dict[str, Any]] = {}
    dimensions["intent_fit"] = dimension([
        check("query_in_title", query in title, 4, f"title={title_text(text)!r}"),
        check("query_token_coverage", not query_tokens or token_hits / max(1, len(query_tokens)) >= 0.6, 2, f"{token_hits}/{len(query_tokens)} query tokens present"),
        check("audience_language", bool(audience_tokens) and audience_hits > 0, 2, f"{audience_hits}/{len(audience_tokens)} audience tokens present"),
        check("intent_marker", intent_present, 2, f"intent={brief['intent']}"),
    ])
    dimensions["information_gain"] = dimension([
        check("explicit_gain", brief["information_gain_requirement"].lower() in lower, 3, "brief information-gain requirement appears verbatim"),
        check("originality_marker", info_markers, 3, "original-data, observation, case, or first-hand marker"),
        check("worked_example", worked_example, 2, "worked example or scenario marker"),
        check("specificity", len(set(numbers)) >= 2, 2, f"{len(set(numbers))} distinct numeric anchors"),
    ])
    dimensions["source_quality"] = dimension([
        check("brief_receipts_visible", source_refs_visible > 0, 4, f"{source_refs_visible}/{len(brief['source_receipts'])} source refs visible"),
        check("linked_sources", len(urls) >= 1, 3, f"{len(urls)} URLs"),
        check("citation_markers", len(citation_markers) >= 1, 3, f"{len(citation_markers)} citation markers"),
    ])
    technical_checks = [
        check("title", bool(title), 2, "title or first-line label exists"),
        check("structured_headings", len(headings) >= 2, 2, f"{len(headings)} headings"),
        check("scannable_units", len(bullets) >= 3, 2, f"{len(bullets)} bullets or numbered steps"),
    ]
    if brief["channel"] in {"article", "local_service_page", "ecommerce_page"}:
        technical_checks.extend([
            check("meta_description", "meta description" in lower, 1, "explicit meta description field"),
            check("internal_link", "internal link" in lower or len(urls) >= 2, 1, "internal-link marker or multiple links"),
            check("schema_or_faq", "schema" in lower or "faq" in lower, 1, "schema or FAQ marker"),
            check("url_or_canonical", "canonical" in lower or "suggested url" in lower or "slug" in lower, 1, "URL/canonical marker"),
        ])
    else:
        technical_checks.extend([
            check("channel_label", brief["channel"].replace("_", " ") in lower, 2, f"channel={brief['channel']}"),
            check("production_cues", any(marker in lower for marker in ("hook", "scene", "shot", "visual", "voiceover", "slide")), 2, "channel-native production cue"),
        ])
    dimensions["technical_on_page_readiness"] = dimension(technical_checks)
    dimensions["aeo_geo_readiness"] = dimension([
        check("direct_answer", direct_answer, 3, "answer-like language appears in opening"),
        check("question_heading", question_heading, 2, "question heading present"),
        check("structured_answer", len(bullets) >= 3 or "|" in text, 2, "list or table present"),
        check("entity_definition", bool(re.search(r"\b[A-Z][A-Za-z0-9 -]{2,}\s+(?:is|means|refers to)\b", text)), 1, "named entity definition"),
        check("source_support", len(urls) + len(citation_markers) >= 2, 2, "multiple source-support markers"),
    ])
    dimensions["human_usefulness"] = dimension([
        check("substantive", len(words) >= 120, 2, f"{len(words)} words"),
        check("readable_sentences", average_sentence <= 24, 2, f"average sentence length {average_sentence:.1f}"),
        check("actionable", len(bullets) >= 3 or "step 1" in lower, 2, "steps or scannable actions"),
        check("example", worked_example, 2, "example or scenario present"),
        check("limits", any(marker in lower for marker in ("limit", "caveat", "does not", "not a guarantee", "uncertain")), 2, "limitation or caveat visible"),
    ])
    channel_markers = {
        "article": ("meta description", "introduction", "conclusion"),
        "local_service_page": ("service area", "location", "contact"),
        "ecommerce_page": ("product", "price", "specification", "shipping"),
        "linkedin_post": ("hook", "comment", "dm", "linkedin"),
        "video_script": ("hook", "scene", "voiceover", "shot"),
        "visual_brief": ("visual", "composition", "palette", "frame"),
        "audio_script": ("voice", "sound", "music", "pause"),
    }
    marker_hits = sum(1 for marker in channel_markers[brief["channel"]] if marker in lower)
    dimensions["format_fit"] = dimension([
        check("channel_markers", marker_hits >= 2, 5, f"{marker_hits}/{len(channel_markers[brief['channel']])} channel markers"),
        check("structural_pattern", brief["structural_pattern"].lower() in lower, 3, "brief structural pattern appears"),
        check("length_present", len(words) >= 40, 2, f"{len(words)} words"),
    ])
    dimensions["conversion_alignment"] = dimension([
        check("cta_present", cta_present, 5, f"CTA={brief['cta']!r}"),
        check("single_next_action", lower.count(brief["cta"].lower()) <= 3 and cta_present, 2, "CTA is present without obvious repetition"),
        check("audience_bridge", audience_hits > 0, 2, "audience language supports CTA"),
        check("no_outcome_guarantee", not guarantee_terms, 1, f"{len(guarantee_terms)} guarantee-risk terms"),
    ])
    dimensions["claim_risk"] = dimension([
        check("no_guarantees", not guarantee_terms, 4, f"{len(guarantee_terms)} guarantee-risk terms"),
        check("few_absolutes", len(absolute_terms) <= 1, 2, f"{len(absolute_terms)} absolute terms"),
        check("numbers_supported", not numbers or bool(urls or citation_markers), 2, f"{len(numbers)} numbers; {len(urls) + len(citation_markers)} support markers"),
        check("risk_boundary_visible", brief["risk_boundary"].lower() in lower or any(marker in lower for marker in ("not a guarantee", "requires review", "unconfirmed", "untested")), 2, "brief boundary or equivalent visible"),
    ])
    hypothesis = brief["measurement_hypothesis"]
    dimensions["measurement_readiness"] = dimension([
        check("prediction_visible", hypothesis["prediction"].lower() in lower, 3, "prediction appears in content or attached plan"),
        check("stage_visible", hypothesis["primary_stage"].lower() in lower, 2, f"primary stage={hypothesis['primary_stage']}"),
        check("window_visible", str(hypothesis["observation_window_days"]) in lower, 2, f"window={hypothesis['observation_window_days']} days"),
        check("falsifier_visible", hypothesis["falsifier"].lower() in lower, 3, "falsifier appears in content or attached plan"),
    ])
    return dimensions


def score_content(args: argparse.Namespace) -> dict[str, Any]:
    project = project_path(args.project)
    manifest = validate_project(project)
    brief = read_json(Path(args.brief).expanduser().resolve())
    validate_brief(brief)
    if brief["project_id"] != manifest["project_id"]:
        raise ContractError("PROJECT_MISMATCH", "SearchBrief belongs to a different project")
    content_path = Path(args.content).expanduser().resolve()
    if not content_path.exists() or not content_path.is_file():
        raise ContractError("MISSING_FILE", f"Content does not exist: {content_path}")
    text = content_path.read_text(encoding="utf-8")
    dimensions = deterministic_dimensions(text, brief)

    expert: dict[str, Any] | None = None
    if args.expert_judgment:
        expert = read_json(Path(args.expert_judgment).expanduser().resolve())
        require_keys(expert, ("reviewer", "dimensions", "notes"), "expert judgment")
        reject_unknown_keys(expert, ("reviewer", "dimensions", "notes"), "expert judgment")
        if not isinstance(expert["dimensions"], dict):
            raise ContractError("UNKNOWN_SCHEMA", "expert judgment dimensions must be an object")
        reject_unknown_keys(expert["dimensions"], DIMENSIONS, "expert judgment dimensions")
        for name, value in expert["dimensions"].items():
            if not isinstance(value, (int, float)) or not 0 <= float(value) <= 10:
                raise ContractError("INVALID_SCORE", f"Expert score for {name} must be between 0 and 10")

    combined_scores: list[float] = []
    for name in DIMENSIONS:
        expert_score = float(expert["dimensions"][name]) if expert and name in expert["dimensions"] else None
        deterministic_score = dimensions[name]["deterministic_score"]
        combined = round(deterministic_score * 0.7 + expert_score * 0.3, 2) if expert_score is not None else deterministic_score
        dimensions[name]["expert_judgment"] = {
            "status": "PROVIDED" if expert_score is not None else "NOT_PROVIDED",
            "score": expert_score,
            "reviewer": expert.get("reviewer") if expert_score is not None else None,
            "notes": expert.get("notes") if expert_score is not None else None,
        }
        dimensions[name]["combined_score"] = combined
        combined_scores.append(combined)
    original = round(sum(combined_scores) / len(combined_scores), 2)

    override_record = {
        "applied": False,
        "original_score": original,
        "override_score": None,
        "operator": None,
        "reason": None,
        "recorded_at": None,
    }
    final_score = original
    if args.override:
        override = read_json(Path(args.override).expanduser().resolve())
        require_keys(override, ("score", "operator", "reason"), "operator override")
        reject_unknown_keys(override, ("score", "operator", "reason"), "operator override")
        if not isinstance(override["score"], (int, float)) or not 0 <= float(override["score"]) <= 10:
            raise ContractError("INVALID_SCORE", "Override score must be between 0 and 10")
        if not str(override["operator"]).strip() or not str(override["reason"]).strip():
            raise ContractError("INCOMPLETE_SCHEMA", "Override requires a named operator and non-empty reason")
        final_score = round(float(override["score"]), 2)
        override_record = {
            "applied": True,
            "original_score": original,
            "override_score": final_score,
            "operator": str(override["operator"]),
            "reason": str(override["reason"]),
            "recorded_at": utc_now(),
        }

    content_hash = sha256_file(content_path)
    receipt = {
        "schema_version": "content-score-receipt/v1",
        "record_type": "ContentScoreReceipt",
        "receipt_id": record_id("score", brief["brief_id"], content_hash),
        "project_id": manifest["project_id"],
        "brief_id": brief["brief_id"],
        "content_ref": str(content_path),
        "content_hash": content_hash,
        "created_at": utc_now(),
        "method": "transparent-heuristics-plus-bounded-judgment",
        "dimensions": dimensions,
        "original_composite": original,
        "operator_override": override_record,
        "final_composite": final_score,
        "observed_outcomes": [],
        "proof_state": "PREDICTED",
    }
    output = project / "scores" / f"{receipt['receipt_id']}.json"
    write_json(output, receipt)
    execution_event(project, manifest, "score", str(output.relative_to(project)))
    return {"status": "SCORED", "receipt": str(output), "original_score": original, "final_score": final_score, "proof_state": "PREDICTED"}


def load_import_rows(path: Path) -> tuple[list[dict[str, Any]], list[str]]:
    if path.suffix.lower() == ".csv":
        try:
            with path.open("r", encoding="utf-8-sig", newline="") as handle:
                reader = csv.DictReader(handle)
                if not reader.fieldnames:
                    raise ContractError("MALFORMED_IMPORT", f"CSV has no header: {path}")
                return [dict(row) for row in reader], list(reader.fieldnames)
        except UnicodeDecodeError as exc:
            raise ContractError("MALFORMED_IMPORT", f"CSV is not valid UTF-8: {path}") from exc
    if path.suffix.lower() == ".json":
        payload = read_json(path)
        rows = payload.get("rows") if isinstance(payload, dict) else payload
        if not isinstance(rows, list) or not all(isinstance(row, dict) for row in rows):
            raise ContractError("MALFORMED_IMPORT", "JSON import must be an array of objects or an object with a rows array")
        headers = list(rows[0]) if rows else []
        if any(set(row) != set(headers) for row in rows):
            raise ContractError("MALFORMED_IMPORT", "All JSON import rows must use the same fields")
        return rows, headers
    raise ContractError("UNKNOWN_SCHEMA", f"Only CSV and JSON imports are supported: {path.suffix}")


def parse_bool(value: Any, label: str) -> bool:
    if isinstance(value, bool):
        return value
    lowered = str(value).strip().lower()
    if lowered in {"true", "1", "yes"}:
        return True
    if lowered in {"false", "0", "no"}:
        return False
    raise ContractError("MALFORMED_IMPORT", f"{label} must be true or false")


def parse_number(value: Any, label: str) -> float | int:
    text = str(value).strip().replace(",", "")
    if not text:
        raise ContractError("MALFORMED_IMPORT", f"{label} is blank")
    try:
        number = float(text.rstrip("%"))
    except ValueError as exc:
        raise ContractError("MALFORMED_IMPORT", f"{label} must be numeric, received {value!r}") from exc
    if text.endswith("%"):
        number /= 100
    return int(number) if number.is_integer() else number


def import_profiles() -> dict[str, Any]:
    payload = read_json(IMPORT_PROFILES_PATH)
    require_keys(payload, ("schema_version", "profiles"), "import profiles")
    return payload["profiles"]


def normalize_import(
    source: str,
    rows: list[dict[str, Any]],
    headers: list[str],
    mapping_path: Path | None,
    date_start: str | None,
    date_end: str | None,
) -> tuple[list[dict[str, Any]], dict[str, str], str, str]:
    profiles = import_profiles()
    if source not in profiles:
        raise ContractError("UNKNOWN_SOURCE", f"Unknown import source: {source}")
    profile = profiles[source]
    mapping = {header: header for header in headers}
    if mapping_path:
        supplied = read_json(mapping_path)
        require_keys(supplied, ("source", "field_map"), "field mapping")
        reject_unknown_keys(supplied, ("source", "field_map"), "field mapping")
        if supplied["source"] != source or not isinstance(supplied["field_map"], dict):
            raise ContractError("MAPPING_MISMATCH", "Field mapping source must match the selected import source")
        mapping = {str(key): str(value) for key, value in supplied["field_map"].items()}
        if set(mapping) != set(headers):
            raise ContractError("INCOMPLETE_MAPPING", "Field mapping must explicitly map every source column")
    canonical = list(mapping.values())
    if len(canonical) != len(set(canonical)):
        raise ContractError("CONFLICTING_MAPPING", "Two source fields cannot map to the same canonical field")
    allowed = set(profile["required"]) | set(profile.get("optional", []))
    unknown = sorted(set(canonical) - allowed)
    missing = sorted(set(profile["required"]) - set(canonical))
    if unknown:
        raise ContractError("UNKNOWN_SCHEMA", f"Unknown canonical fields for {source}: {', '.join(unknown)}", unknown)
    if missing:
        raise ContractError("INCOMPLETE_SCHEMA", f"Missing required {source} fields: {', '.join(missing)}", missing)
    start = parse_date_value(date_start, "date_start") if date_start else None
    end = parse_date_value(date_end, "date_end") if date_end else None
    if start and end and start > end:
        raise ContractError("CONFLICTING_DATE_RANGE", f"date_start {start} is after date_end {end}")

    normalized: list[dict[str, Any]] = []
    observed_dates: list[date] = []
    for index, row in enumerate(rows, start=1):
        converted = {mapping[key]: value for key, value in row.items()}
        for field in profile["required"]:
            value = converted.get(field)
            if value is None or (str(value).strip() == "" and not (source == "ai_citation" and field == "cited_url")):
                raise ContractError("INCOMPLETE_SCHEMA", f"Row {index} has blank required field: {field}")
        for field in profile.get("numeric", []):
            if field in converted and str(converted[field]).strip() != "":
                converted[field] = parse_number(converted[field], f"row {index}.{field}")
        for field in profile.get("boolean", []):
            if field in converted:
                converted[field] = parse_bool(converted[field], f"row {index}.{field}")
        if source == "ai_citation" and converted.get("cited") and not str(converted.get("cited_url", "")).strip():
            raise ContractError("INCOMPLETE_SCHEMA", f"Row {index} says cited=true but cited_url is blank")
        observed = parse_date_value(converted[profile["date_field"]], f"row {index}.{profile['date_field']}")
        if start and observed < start:
            raise ContractError("CONFLICTING_DATE_RANGE", f"Row {index} date {observed} precedes declared start {start}")
        if end and observed > end:
            raise ContractError("CONFLICTING_DATE_RANGE", f"Row {index} date {observed} exceeds declared end {end}")
        observed_dates.append(observed)
        normalized.append(converted)
    if not normalized:
        raise ContractError("EMPTY_IMPORT", "Import contains no rows")
    derived_start = str(min(observed_dates))
    derived_end = str(max(observed_dates))
    return normalized, mapping, str(start or derived_start), str(end or derived_end)


def append_search_event(
    project: Path,
    manifest: dict[str, Any],
    content_id: str,
    stage: str,
    evidence_refs: list[str],
    hashes: list[str],
    provenance: str,
    value: Any = None,
    notes: str = "",
) -> dict[str, Any]:
    if stage not in OUTCOME_STAGES:
        raise ContractError("INVALID_STAGE", f"Unknown search event stage: {stage}")
    if not content_id or not evidence_refs or not hashes:
        raise ContractError("INCOMPLETE_SCHEMA", "SearchEvent requires content_id, evidence_refs, and source_hashes")
    event = {
        "schema_version": "search-event/v1",
        "record_type": "SearchEvent",
        "event_id": record_id("event", manifest["project_id"], content_id, stage, hashes),
        "project_id": manifest["project_id"],
        "content_id": content_id,
        "stage": stage,
        "observed_at": utc_now(),
        "evidence_refs": evidence_refs,
        "source_hashes": hashes,
        "provenance": provenance,
        "value": value,
        "notes": notes,
    }
    append_jsonl(safe_project_ref(project, manifest["ledgers"]["outcomes"]), event)
    return event


def existing_import_hashes(project: Path) -> set[str]:
    index = project / "imports" / "index.jsonl"
    return {row.get("raw_hash", "") for row in read_jsonl(index)}


def measure_import(args: argparse.Namespace) -> dict[str, Any]:
    project = project_path(args.project)
    manifest = validate_project(project)
    # Validate the event contract before copying or indexing an import. A
    # rejected invocation must be side-effect free; otherwise a corrected retry
    # would be misclassified as a duplicate even though no valid event exists.
    if args.stage and not args.content_id:
        raise ContractError("INCOMPLETE_SCHEMA", "--content-id is required when --stage is supplied")
    input_path = Path(args.input).expanduser().resolve()
    if not input_path.exists() or not input_path.is_file():
        raise ContractError("MISSING_FILE", f"Import file does not exist: {input_path}")
    raw_hash = sha256_file(input_path)
    if raw_hash in existing_import_hashes(project):
        raise ContractError("DUPLICATE_IMPORT", f"Import hash already exists in this project: {raw_hash}")
    rows, headers = load_import_rows(input_path)
    mapping_path = Path(args.mapping).expanduser().resolve() if args.mapping else None
    normalized, mapping, date_start, date_end = normalize_import(args.source, rows, headers, mapping_path, args.date_start, args.date_end)

    raw_target = project / "imports" / "raw" / args.source / f"{raw_hash}{input_path.suffix.lower()}"
    raw_target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(input_path, raw_target)
    normalized_target = project / "imports" / "normalized" / args.source / f"{raw_hash}.json"
    write_json(
        normalized_target,
        {
            "schema_version": "normalized-search-import/v1",
            "source": args.source,
            "raw_hash": raw_hash,
            "date_range": {"start": date_start, "end": date_end},
            "field_mapping": mapping,
            "rows": normalized,
        },
    )
    receipt = {
        "schema_version": "search-import-receipt/v1",
        "record_type": "SearchImportReceipt",
        "receipt_id": record_id("import", manifest["project_id"], raw_hash),
        "project_id": manifest["project_id"],
        "source": args.source,
        "created_at": utc_now(),
        "raw_ref": str(raw_target.relative_to(project)),
        "raw_hash": raw_hash,
        "normalized_ref": str(normalized_target.relative_to(project)),
        "row_count": len(normalized),
        "date_range": {"start": date_start, "end": date_end},
        "field_mapping": mapping,
        "status": "ACCEPTED",
    }
    receipt_path = project / "receipts" / f"{receipt['receipt_id']}.json"
    write_json(receipt_path, receipt)
    append_jsonl(project / "imports" / "index.jsonl", receipt)
    event = None
    if args.stage:
        event = append_search_event(
            project,
            manifest,
            args.content_id,
            args.stage,
            [str(receipt_path), str(raw_target)],
            [raw_hash],
            f"local {args.source} import",
            notes=args.notes or "",
        )
    execution_event(project, manifest, "measure-import", str(receipt_path.relative_to(project)))
    return {"status": "ACCEPTED", "receipt": str(receipt_path), "normalized": str(normalized_target), "event_id": event["event_id"] if event else None}


def recommend_from_events(project: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    events = read_jsonl(safe_project_ref(project, manifest["ledgers"]["outcomes"]))
    by_content: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for event in events:
        by_content[str(event.get("content_id", ""))].append(event)
    existing = read_jsonl(safe_project_ref(project, manifest["ledgers"]["recommendations"]))
    existing_signatures = {row.get("signature") for row in existing}
    candidates = [
        ("PUBLISHED", "INDEXED", "Verify crawl, canonical, sitemap, and index eligibility before changing content strategy."),
        ("INDEXED", "RANKED", "Revisit query-intent fit, information gain, internal support, and authority evidence."),
        ("RANKED", "TRAFFIC", "Inspect position, snippet/title appeal, SERP features, and query demand before rewriting the page."),
        ("TRAFFIC", "CONVERTED", "Inspect CTA-message continuity, offer fit, page friction, and measurement instrumentation."),
        ("CONVERTED", "COLLECTED", "Inspect offer qualification and payment handoff; do not treat conversions as collected revenue."),
        ("CITED", "TRAFFIC", "Test hidden attribution through branded-search movement and post-conversion source questions; citation clicks alone undercount influence."),
    ]
    appended: list[dict[str, Any]] = []
    ledger = safe_project_ref(project, manifest["ledgers"]["recommendations"])
    for content_id, content_events in by_content.items():
        stages = {event.get("stage") for event in content_events}
        for present, absent, recommendation in candidates:
            if present not in stages or absent in stages:
                continue
            evidence_ids = sorted(event["event_id"] for event in content_events if event.get("stage") == present)
            signature = sha256_bytes(json.dumps([content_id, present, absent, evidence_ids], sort_keys=True).encode("utf-8"))
            if signature in existing_signatures:
                continue
            row = {
                "schema_version": "search-workflow-recommendation/v1",
                "recommendation_id": record_id("recommendation", signature),
                "signature": signature,
                "project_id": manifest["project_id"],
                "content_id": content_id,
                "state": "PROPOSED",
                "observed_stage": present,
                "missing_stage": absent,
                "recommendation": recommendation,
                "evidence_event_ids": evidence_ids,
                "causal_status": "UNCONFIRMED",
                "promotion": "HUMAN_REQUIRED",
                "created_at": utc_now(),
            }
            append_jsonl(ledger, row)
            appended.append(row)
            existing_signatures.add(signature)
    execution_event(project, manifest, "measure-recommend", manifest["ledgers"]["recommendations"])
    return {"status": "PROPOSALS_READY", "recommendations_appended": len(appended), "recommendations": appended}


def measure(args: argparse.Namespace) -> dict[str, Any]:
    project = project_path(args.project)
    manifest = validate_project(project)
    if args.review_recommendations:
        rows = read_jsonl(safe_project_ref(project, manifest["ledgers"]["recommendations"]))
        return {"status": "REVIEW_ONLY", "count": len(rows), "states": dict(sorted({state: sum(1 for row in rows if row.get('state') == state) for state in {row.get('state') for row in rows}}.items()))}
    if args.recommend:
        return recommend_from_events(project, manifest)
    if not args.source or not args.input:
        raise ContractError("INCOMPLETE_SCHEMA", "measure import requires --source and --input")
    return measure_import(args)


def service(args: argparse.Namespace) -> dict[str, Any]:
    project = project_path(args.project)
    manifest = validate_project(project)
    artifacts = read_json(Path(args.artifacts).expanduser().resolve())
    if not isinstance(artifacts, dict):
        raise ContractError("UNKNOWN_SCHEMA", "Service artifact map must be a JSON object")
    reject_unknown_keys(artifacts, SERVICE_ARTIFACTS, "Service artifact map")
    require_keys(artifacts, SERVICE_ARTIFACTS, "Service artifact map")
    normalized: dict[str, str] = {}
    missing: list[str] = []
    for name, ref in artifacts.items():
        path = Path(ref).expanduser()
        if not path.is_absolute():
            path = (project / path).resolve()
        else:
            path = path.resolve()
        normalized[name] = str(path)
        if not path.exists() or not path.is_file():
            missing.append(f"{name}: {path}")
    if missing:
        raise ContractError("INCOMPLETE_SERVICE_PACK", "Service artifacts are missing", missing)
    receipt = {
        "schema_version": "service-receipt/v1",
        "record_type": "ServiceReceipt",
        "service_id": record_id("service", manifest["project_id"], normalized),
        "project_id": manifest["project_id"],
        "created_at": utc_now(),
        "prototype_state": "UNTESTED",
        "delivery_state": "READY_FOR_INTERNAL_REVIEW",
        "artifacts": normalized,
        "boundaries": [
            "The service guarantees the scoped analysis and artifacts, not rankings, citations, traffic, leads, conversions, or revenue.",
            "No publication, outreach, connector write, payment setup, or offer replacement occurred.",
            "The Angle Map remains the live offer canon.",
        ],
        "proof_gaps": [
            "No external market event has tested willingness to pay for this prototype.",
            "No dated ranking, citation, traffic, conversion, or collected-revenue outcome is attributed to this delivery.",
        ],
    }
    output = project / "receipts" / f"{receipt['service_id']}.json"
    write_json(output, receipt)
    execution_event(project, manifest, "service", str(output.relative_to(project)))
    return {"status": receipt["delivery_state"], "receipt": str(output), "prototype_state": "UNTESTED"}


def namespace_to_argv(mode: str, parameters: dict[str, Any]) -> list[str]:
    if mode == "batch":
        raise ContractError("BATCH_RECURSION", "Batch jobs cannot invoke batch")
    argv = [mode]
    for key, value in parameters.items():
        flag = "--" + key.replace("_", "-")
        if isinstance(value, bool):
            if value:
                argv.append(flag)
        elif value is not None:
            argv.extend([flag, str(value)])
    return argv


def batch(args: argparse.Namespace) -> dict[str, Any]:
    payload = read_json(Path(args.file).expanduser().resolve())
    jobs = payload.get("jobs") if isinstance(payload, dict) else None
    if not isinstance(jobs, list):
        raise ContractError("UNKNOWN_SCHEMA", "Batch file must be an object with a jobs array")
    results: list[dict[str, Any]] = []
    parser = build_parser()
    for index, job in enumerate(jobs, start=1):
        if not isinstance(job, dict):
            raise ContractError("UNKNOWN_SCHEMA", f"Batch job {index} must be an object")
        require_keys(job, ("mode", "parameters"), f"batch job {index}")
        reject_unknown_keys(job, ("mode", "parameters"), f"batch job {index}")
        if not isinstance(job["parameters"], dict):
            raise ContractError("UNKNOWN_SCHEMA", f"Batch job {index}.parameters must be an object")
        parsed = parser.parse_args(namespace_to_argv(str(job["mode"]), job["parameters"]))
        results.append({"job": index, "mode": job["mode"], "result": dispatch(parsed)})
    return {"status": "BATCH_COMPLETE", "jobs": len(results), "results": results}


def add_project_argument(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--project", required=True, help="Portable project pack directory")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Search Content Mastery local command runtime")
    subparsers = parser.add_subparsers(dest="mode", required=True)

    foundation_parser = subparsers.add_parser("foundation", help="Create or validate a portable project pack")
    add_project_argument(foundation_parser)
    foundation_parser.add_argument("--name")
    foundation_parser.add_argument("--vertical")
    foundation_parser.add_argument("--context", help="Strict JSON context object")
    foundation_parser.add_argument("--resume", action="store_true")

    audit_parser = subparsers.add_parser("audit", help="Validate project truth and produce a baseline receipt")
    add_project_argument(audit_parser)

    plan_parser = subparsers.add_parser("plan", help="Create a versioned SearchBrief")
    add_project_argument(plan_parser)
    plan_parser.add_argument("--input", required=True, help="Strict SearchBrief input JSON")

    create_parser = subparsers.add_parser("create", help="Route an approved brief to existing production workflows")
    add_project_argument(create_parser)
    create_parser.add_argument("--brief", required=True)

    score_parser = subparsers.add_parser("score", help="Produce a transparent ContentScoreReceipt")
    add_project_argument(score_parser)
    score_parser.add_argument("--brief", required=True)
    score_parser.add_argument("--content", required=True)
    score_parser.add_argument("--expert-judgment")
    score_parser.add_argument("--override")

    measure_parser = subparsers.add_parser("measure", help="Normalize imports, append events, or propose human-reviewed changes")
    add_project_argument(measure_parser)
    measure_parser.add_argument("--source", choices=sorted(import_profiles()))
    measure_parser.add_argument("--input")
    measure_parser.add_argument("--mapping")
    measure_parser.add_argument("--date-start")
    measure_parser.add_argument("--date-end")
    measure_parser.add_argument("--content-id")
    measure_parser.add_argument("--stage", choices=OUTCOME_STAGES)
    measure_parser.add_argument("--notes")
    measure_parser.add_argument("--recommend", action="store_true")
    measure_parser.add_argument("--review-recommendations", action="store_true")

    service_parser = subparsers.add_parser("service", help="Validate a service pack and create a bounded ServiceReceipt")
    add_project_argument(service_parser)
    service_parser.add_argument("--artifacts", required=True, help="JSON map of the nine required artifact paths")

    batch_parser = subparsers.add_parser("batch", help="Run a local ordered batch of the seven public modes")
    batch_parser.add_argument("--file", required=True)
    return parser


def dispatch(args: argparse.Namespace) -> dict[str, Any]:
    handlers = {
        "foundation": foundation,
        "audit": audit,
        "plan": plan,
        "create": create_handoff,
        "score": score_content,
        "measure": measure,
        "service": service,
        "batch": batch,
    }
    return handlers[args.mode](args)


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        result = dispatch(args)
    except ContractError as exc:
        print(json.dumps({"status": "REJECTED", "code": exc.code, "message": str(exc), "details": exc.details}, indent=2), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
