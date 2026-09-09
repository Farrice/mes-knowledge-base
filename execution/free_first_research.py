#!/usr/bin/env python3
"""Compile and validate Codex-native, zero-paid-spend research missions.

This module is the local half of the Free-First Research Mission. It does not
pretend Python can call Codex's host-provided web tool. Instead it:

1. compiles an inspectable mission and native-web runbook;
2. optionally performs bounded Tavily Search/Extract or on-demand RSS pulls;
3. validates findings returned by the active Codex thread; and
4. emits an evidence pack and value receipt that fail closed on stale/local
   substitution, missing URLs, or unmet depth.

It never imports or calls Apify, Gemini, Perplexity, NotebookLM, Tavily
Research, an agent swarm, a scheduler, or a background worker.

Examples:
    python3 execution/free_first_research.py plan \
      --objective "What has changed in this market?" \
      --decision "Whether to enter the market" \
      --downstream "Offer strategy" \
      --artifact "Current market decision brief" \
      --depth standard

    python3 execution/free_first_research.py ingest \
      --mission .tmp/research-missions/<mission-id>

    python3 execution/free_first_research.py verify \
      --mission .tmp/research-missions/<mission-id>
"""

from __future__ import annotations

import argparse
import html
import ipaddress
import json
import re
import ssl
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
EXEC = ROOT / "execution"
DEFAULT_MISSION_ROOT = ROOT / ".tmp" / "research-missions"
SCHEMA_VERSION = "free-first-research-mission/v1"

CLAIM_LABELS = {
    "VERIFIED",
    "TRIANGULATED",
    "DIRECTIONAL",
    "INFERENCE",
    "UNVERIFIED",
    "CONTRADICTED",
}
SOURCE_CLASSES = {
    "official",
    "primary",
    "secondary",
    "community",
    "feed",
    "user_supplied",
    "local_context",
}
RETRIEVAL_METHODS = {
    "codex_native_web",
    "tavily_search",
    "tavily_extract",
    "rss",
    "user_supplied",
    "local_context",
}
EVIDENCE_TYPES = {
    "page_read",
    "document",
    "direct_quote",
    "feed_item",
    "search_snippet",
    "local_note",
}
CLAIM_SCOPES = {"current_world", "historical", "timeless", "local_system"}
STANCES = {"support", "contradict", "context"}

BLOCKED_PROVIDERS = (
    "apify",
    "gemini_deep_research",
    "perplexity",
    "notebooklm",
    "tavily_research",
)
BLOCKED_EXECUTION = (
    "paid_accelerators",
    "real_subagents",
    "research_swarms",
    "background_workers",
    "schedules",
    "authenticated_private_scraping",
)
FULL_EVIDENCE_TYPES = {"page_read", "document", "direct_quote", "feed_item"}
NON_AUTHORITATIVE_METHODS = {"local_context"}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def slugify(value: str, limit: int = 64) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return (slug[:limit].rstrip("-") or "research-mission")


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: Iterable[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows),
        encoding="utf-8",
    )


def read_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def depth_floor(depth: str) -> Dict[str, Any]:
    sys.path.insert(0, str(EXEC))
    try:
        from research_depth import contract  # type: ignore

        return contract(depth)
    finally:
        if sys.path and sys.path[0] == str(EXEC):
            sys.path.pop(0)


def default_queries(objective: str) -> List[Dict[str, str]]:
    current_year = datetime.now(timezone.utc).year
    return [
        {
            "id": "q-official-current",
            "role": "official_current",
            "query": f"{objective} current {current_year} official documentation primary sources",
        },
        {
            "id": "q-limitations",
            "role": "counterevidence",
            "query": f"{objective} limitations failures criticism risks counterevidence {current_year}",
        },
        {
            "id": "q-comparison",
            "role": "comparison",
            "query": f"{objective} alternatives comparison pricing availability {current_year}",
        },
        {
            "id": "q-human-voice",
            "role": "human_voice",
            "query": f"{objective} real user experience discussion forum review",
        },
        {
            "id": "q-rss-changelog",
            "role": "rss_changelog",
            "query": f"{objective} RSS Atom feed changelog releases updates",
        },
    ]


def build_manifest(args: argparse.Namespace) -> Dict[str, Any]:
    now = datetime.now(timezone.utc)
    if not 1 <= args.freshness_hours <= 720:
        raise ValueError("freshness-hours must be between 1 and 720")
    mission_id = f"{slugify(args.objective)}-{now.strftime('%Y%m%dT%H%M%SZ')}"
    floor = depth_floor(args.depth)
    queries = default_queries(args.objective)
    for index, query in enumerate(args.query or [], 1):
        queries.append({"id": f"q-custom-{index}", "role": "custom", "query": query})

    skills = ["source-command-deep-research-os"]
    for skill in args.skill or []:
        if skill not in skills:
            skills.append(skill)

    return {
        "schema_version": SCHEMA_VERSION,
        "mission_id": mission_id,
        "created_at": now.isoformat(),
        "status": "PLANNED",
        "owner": "/deep-research-os",
        "execution_mode": "codex_native_free_first",
        "objective": args.objective,
        "decision": args.decision,
        "depth": args.depth,
        "value_contract": {
            "downstream_use": args.downstream,
            "use_now_artifact": args.artifact,
            "accepted_by_operator": "UNTESTED",
            "used_in_work": "NO EVENT",
            "commercial_event": "NO EVENT",
        },
        "authority_policy": {
            "current_world_authority": "live_external_sources_retrieved_this_run",
            "local_context_role": "question_shaping_constraints_skill_selection_interpretation_only",
            "conflict_rule": "live_external_evidence_wins_for_current_world_claims",
            "user_owned_rule": "user_definitions_preferences_and_project_decisions_control_intent",
        },
        "freshness_policy": {
            "max_age_hours": args.freshness_hours,
            "retrieved_during_mission_required": True,
            "future_clock_skew_minutes": 5,
        },
        "source_ladder": [
            {
                "rank": 1,
                "method": "codex_native_web",
                "required_first": True,
                "purpose": "search, open, and inspect current public sources",
            },
            {
                "rank": 2,
                "method": "tavily_search_extract",
                "required_first": False,
                "purpose": "bounded gap fill and full-page recovery; no Tavily Research",
            },
            {
                "rank": 3,
                "method": "public_rss",
                "required_first": False,
                "purpose": "on-demand dated releases, changelogs, and public signals",
            },
            {
                "rank": 4,
                "method": "local_context_and_skills",
                "required_first": False,
                "purpose": "shape questions and interpretation; never prove current world state",
            },
        ],
        "query_plan": queries,
        "context_plan": {
            "local_paths": list(dict.fromkeys(args.context or [])),
            "relevant_skills": skills,
            "hot": [
                "free-first authority policy",
                "research objective and decision",
                "source ledger and claim labels",
            ],
            "on_demand": ["domain context", "relevant skill files", "prior project decisions"],
            "skipped": ["unrelated skill corpus", "historic generated dossiers as current proof"],
        },
        "completion_gate": {
            "min_sources": int(floor["sources"]),
            "min_domains": int(floor["domains"]),
            "min_full_page_reads": max(1, int(floor.get("extracts", 0))),
            "snippets_count_half": True,
            "native_web_full_read_required": True,
            "counterevidence_query_required": True,
            "min_authoritative_claims": max(1, int(floor["domains"]) // 2),
            "invalid_findings_allowed": 0,
            "paid_cost_usd_max": 0.0,
            "value_receipt_required": True,
        },
        "blocked": {
            "providers": list(BLOCKED_PROVIDERS),
            "execution": list(BLOCKED_EXECUTION),
            "schedules_allowed": False,
            "subagents_allowed": False,
            "paid_cost_usd_max": 0.0,
            "tavily_zero_dollar_confirmation_required": True,
        },
        "execution_order": [
            "compile_mission",
            "codex_native_web",
            "tavily_search_extract_gap_fill",
            "public_rss_on_demand",
            "validate_external_evidence",
            "load_local_context_and_skills",
            "synthesize_with_citations",
            "quality_and_value_receipts",
        ],
    }


def finding_template() -> Dict[str, Any]:
    return {
        "claim_id": "c-001",
        "claim": "One atomic sourced claim.",
        "source_url": "https://example.com/source",
        "source_title": "Source title",
        "source_class": "official",
        "retrieval_method": "codex_native_web",
        "evidence_type": "page_read",
        "retrieved_at": utc_now(),
        "published_at": "",
        "query_id": "q-official-current",
        "claim_label": "VERIFIED",
        "claim_scope": "current_world",
        "stance": "support",
        "excerpt": "Short exact excerpt or faithful evidence snippet.",
    }


def render_runbook(manifest: Dict[str, Any], mission_dir: Path) -> str:
    lines = [
        f"# Native-Web Runbook: {manifest['objective']}",
        "",
        "## Decision",
        "",
        manifest["decision"],
        "",
        "## Non-Negotiable Authority Rule",
        "",
        "Current-world claims must come from live external sources retrieved in this run. "
        "Local context and skills may shape questions and interpretation, but they cannot substitute for live proof.",
        f"Evidence must be retrieved during this mission and be no older than "
        f"{manifest['freshness_policy']['max_age_hours']} hours when validated.",
        "",
        "## Execution Boundary",
        "",
        "The active Codex thread performs native web search and page opening. This Python packet cannot invoke the host-only web tool. Work sequentially in this thread: no subagents, research swarm, background worker, schedule, or paid provider.",
        "",
        "## Native Web Queries",
        "",
    ]
    for query in manifest["query_plan"]:
        lines.append(f"- **{query['id']} ({query['role']}):** {query['query']}")

    template = json.dumps(finding_template(), indent=2, ensure_ascii=False)
    native_path = mission_dir / "native-web-findings.jsonl"
    lines += [
        "",
        "## Evidence Capture",
        "",
        "1. Search each angle with Codex's native web search.",
        "2. Open the strongest pages; prefer official and primary sources.",
        "3. Use search snippets only for discovery. A `VERIFIED` claim must come from an opened page, document, direct quote, or dated official feed item.",
        "4. Record one atomic finding per JSONL line in:",
        "",
        f"`{native_path}`",
        "",
        "Finding schema example:",
        "",
        "```json",
        template,
        "```",
        "",
        "Use the same `claim_id` across independent sources when labeling a claim `TRIANGULATED`. The validator requires two distinct domains.",
        "",
        "## Optional Free Gap Fill",
        "",
        "After native web evidence exists, bounded Tavily Search/Extract may fill gaps:",
        "First verify that the Tavily account cannot create a dollar charge. The command fails closed without that confirmation.",
        "",
        "```bash",
        f"python3 execution/free_first_research.py tavily --mission {mission_dir} --confirm-zero-dollar-tavily",
        "```",
        "",
        "Pull a discovered public RSS/Atom feed on demand:",
        "",
        "```bash",
        f"python3 execution/free_first_research.py rss --mission {mission_dir} --url https://example.com/feed.xml",
        "```",
        "",
        "Neither command creates a schedule. Tavily Research is not used.",
        "",
        "## Ingest And Verify",
        "",
        "```bash",
        f"python3 execution/free_first_research.py ingest --mission {mission_dir}",
        f"python3 execution/free_first_research.py verify --mission {mission_dir}",
        "```",
        "",
        "Only after the evidence gate passes should `/deep-research-os` load relevant local context and skills, synthesize the decision brief, and run `research_quality_gate.py`.",
        "",
    ]
    return "\n".join(lines)


def resolve_output_path(value: Optional[str], manifest: Dict[str, Any]) -> Path:
    if value:
        path = Path(value).expanduser()
        if not path.is_absolute():
            path = ROOT / path
        return path.resolve()
    return (DEFAULT_MISSION_ROOT / manifest["mission_id"]).resolve()


def resolve_mission(value: str) -> Tuple[Path, Path, Dict[str, Any]]:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = ROOT / path
    path = path.resolve()
    manifest_path = path if path.name == "mission.json" else path / "mission.json"
    if not manifest_path.exists():
        raise FileNotFoundError(f"mission manifest not found: {manifest_path}")
    return manifest_path.parent, manifest_path, read_json(manifest_path)


def cmd_plan(args: argparse.Namespace) -> int:
    manifest = build_manifest(args)
    mission_dir = resolve_output_path(args.output, manifest)
    if mission_dir.exists() and any(mission_dir.iterdir()):
        print(f"Refusing to overwrite non-empty mission directory: {mission_dir}", file=sys.stderr)
        return 2
    mission_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = mission_dir / "mission.json"
    runbook_path = mission_dir / "native-web-runbook.md"
    write_json(manifest_path, manifest)
    runbook_path.write_text(render_runbook(manifest, mission_dir), encoding="utf-8")
    payload = {
        "status": "PLANNED",
        "mission_id": manifest["mission_id"],
        "mission_dir": str(mission_dir),
        "manifest": str(manifest_path),
        "runbook": str(runbook_path),
        "next_action": "execute native web queries in the active Codex thread",
        "cost_usd": 0.0,
    }
    print(json.dumps(payload, indent=2))
    return 0


def parse_iso(value: str) -> Optional[datetime]:
    if not value:
        return None
    try:
        normalized = value.replace("Z", "+00:00")
        parsed = datetime.fromisoformat(normalized)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed
    except ValueError:
        return None


def public_url_error(value: str) -> str:
    try:
        parsed = urlparse(value)
    except Exception:
        return "source_url is not parseable"
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        return "source_url must be public HTTP(S)"
    host = parsed.hostname.lower().strip("[]")
    if host == "localhost" or host.endswith(".local"):
        return "source_url cannot target localhost or .local"
    try:
        address = ipaddress.ip_address(host)
        if not address.is_global:
            return "source_url cannot target a non-public IP address"
    except ValueError:
        pass
    return ""


def normalize_finding(obj: Dict[str, Any]) -> Dict[str, Any]:
    fields = (
        "claim_id",
        "claim",
        "source_url",
        "source_title",
        "source_class",
        "retrieval_method",
        "evidence_type",
        "retrieved_at",
        "published_at",
        "query_id",
        "claim_label",
        "claim_scope",
        "stance",
        "excerpt",
    )
    finding = {field: str(obj.get(field, "")).strip() for field in fields}
    finding["claim_label"] = finding["claim_label"].upper()
    finding["source_class"] = finding["source_class"].lower()
    finding["retrieval_method"] = finding["retrieval_method"].lower()
    finding["evidence_type"] = finding["evidence_type"].lower()
    finding["claim_scope"] = finding["claim_scope"].lower()
    finding["stance"] = finding["stance"].lower()
    finding["domain"] = (urlparse(finding["source_url"]).hostname or "").lower()
    return finding


def validate_finding(finding: Dict[str, Any], manifest: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    required = (
        "claim_id",
        "claim",
        "source_url",
        "source_class",
        "retrieval_method",
        "evidence_type",
        "retrieved_at",
        "query_id",
        "claim_label",
        "claim_scope",
        "stance",
    )
    for field in required:
        if not finding.get(field):
            errors.append(f"missing {field}")

    if finding.get("claim_label") not in CLAIM_LABELS:
        errors.append(f"invalid claim_label={finding.get('claim_label')!r}")
    if finding.get("source_class") not in SOURCE_CLASSES:
        errors.append(f"invalid source_class={finding.get('source_class')!r}")
    if finding.get("retrieval_method") not in RETRIEVAL_METHODS:
        errors.append(f"invalid retrieval_method={finding.get('retrieval_method')!r}")
    if finding.get("evidence_type") not in EVIDENCE_TYPES:
        errors.append(f"invalid evidence_type={finding.get('evidence_type')!r}")
    if finding.get("claim_scope") not in CLAIM_SCOPES:
        errors.append(f"invalid claim_scope={finding.get('claim_scope')!r}")
    if finding.get("stance") not in STANCES:
        errors.append(f"invalid stance={finding.get('stance')!r}")

    url_error = public_url_error(finding.get("source_url", ""))
    if url_error:
        errors.append(url_error)
    retrieved_at = parse_iso(finding.get("retrieved_at", ""))
    if not retrieved_at:
        errors.append("retrieved_at must be an ISO-8601 timestamp")
    if finding.get("published_at") and not parse_iso(finding["published_at"]):
        errors.append("published_at must be ISO-8601 when present")

    query_ids = {query["id"] for query in manifest.get("query_plan", [])}
    if finding.get("query_id") not in query_ids:
        errors.append(f"query_id is not in mission query plan: {finding.get('query_id')!r}")

    if finding.get("claim_scope") == "current_world":
        freshness = manifest.get("freshness_policy") or {}
        mission_created_at = parse_iso(str(manifest.get("created_at") or ""))
        max_age_hours = int(freshness.get("max_age_hours", 72))
        clock_skew = timedelta(minutes=int(freshness.get("future_clock_skew_minutes", 5)))
        now = datetime.now(timezone.utc)
        if retrieved_at and retrieved_at > now + clock_skew:
            errors.append("current_world evidence retrieved_at is in the future")
        if retrieved_at and now - retrieved_at > timedelta(hours=max_age_hours):
            errors.append(
                f"current_world evidence exceeds the {max_age_hours}-hour freshness window"
            )
        if (
            retrieved_at
            and mission_created_at
            and freshness.get("retrieved_during_mission_required", True)
            and retrieved_at < mission_created_at - clock_skew
        ):
            errors.append("current_world evidence predates this mission run")
        if finding.get("source_class") == "local_context":
            errors.append("local_context cannot prove a current_world claim")
        if finding.get("retrieval_method") in NON_AUTHORITATIVE_METHODS:
            errors.append("local retrieval cannot prove a current_world claim")
        if (
            finding.get("source_class") in {"community", "feed"}
            or finding.get("evidence_type") == "feed_item"
        ) and not finding.get("published_at"):
            errors.append("current community/feed evidence requires published_at")

    if finding.get("claim_label") == "VERIFIED":
        if finding.get("evidence_type") == "search_snippet":
            errors.append("search snippets cannot be VERIFIED")
        if finding.get("retrieval_method") == "tavily_search":
            errors.append("Tavily Search results cannot be VERIFIED without a page read")
        if finding.get("source_class") in {"local_context", "user_supplied"}:
            errors.append("local or undated user-supplied context cannot be VERIFIED current evidence")

    if finding.get("claim_label") == "CONTRADICTED" and finding.get("stance") != "contradict":
        errors.append("CONTRADICTED findings must use stance=contradict")
    if finding.get("evidence_type") == "direct_quote" and not finding.get("excerpt"):
        errors.append("direct_quote evidence requires a non-empty excerpt")
    return errors


def findings_paths(mission_dir: Path, explicit: Sequence[str]) -> List[Path]:
    if explicit:
        paths = []
        for value in explicit:
            path = Path(value).expanduser()
            if not path.is_absolute():
                path = ROOT / path
            paths.append(path.resolve())
        return paths
    return sorted(mission_dir.glob("*-findings.jsonl"))


def load_and_validate_findings(
    paths: Sequence[Path], manifest: Dict[str, Any]
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    accepted: List[Dict[str, Any]] = []
    quarantined: List[Dict[str, Any]] = []
    seen = set()
    for path in paths:
        if not path.exists():
            quarantined.append({"file": str(path), "line": 0, "errors": ["file not found"]})
            continue
        for line_number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not raw.strip():
                continue
            try:
                obj = json.loads(raw)
                if not isinstance(obj, dict):
                    raise ValueError("line is not a JSON object")
            except Exception as exc:
                quarantined.append(
                    {"file": str(path), "line": line_number, "errors": [f"invalid JSON: {exc}"]}
                )
                continue
            finding = normalize_finding(obj)
            errors = validate_finding(finding, manifest)
            key = (finding.get("claim_id"), finding.get("source_url"), finding.get("claim"))
            if key in seen:
                continue
            seen.add(key)
            if errors:
                quarantined.append(
                    {
                        "file": str(path),
                        "line": line_number,
                        "claim_id": finding.get("claim_id"),
                        "errors": errors,
                        "finding": finding,
                    }
                )
            else:
                finding["input_file"] = str(path)
                accepted.append(finding)

    domains_by_claim: Dict[str, set[str]] = {}
    for finding in accepted:
        domains_by_claim.setdefault(finding["claim_id"], set()).add(finding["domain"])
    for finding in accepted:
        if finding["claim_label"] != "TRIANGULATED":
            continue
        domains = {domain for domain in domains_by_claim.get(finding["claim_id"], set()) if domain}
        if len(domains) < 2:
            quarantined.append(
                {
                    "file": finding["input_file"],
                    "line": 0,
                    "claim_id": finding["claim_id"],
                    "errors": ["TRIANGULATED requires at least two independent source domains"],
                    "finding": finding,
                }
            )
    bad_triangulated = {
        item.get("claim_id")
        for item in quarantined
        if any("TRIANGULATED" in error for error in item.get("errors", []))
    }
    accepted = [finding for finding in accepted if finding["claim_id"] not in bad_triangulated]
    return accepted, quarantined


def coverage_metrics(findings: Sequence[Dict[str, Any]], manifest: Dict[str, Any]) -> Dict[str, Any]:
    usable = [
        finding
        for finding in findings
        if finding["claim_label"] != "UNVERIFIED"
        and finding["retrieval_method"] not in NON_AUTHORITATIVE_METHODS
    ]
    urls = {finding["source_url"] for finding in usable}
    domains = {finding["domain"] for finding in usable if finding["domain"]}
    full_urls = {
        finding["source_url"]
        for finding in usable
        if finding["evidence_type"] in FULL_EVIDENCE_TYPES
        and finding["retrieval_method"] != "tavily_search"
    }
    snippet_urls = urls - full_urls
    native_full = [
        finding
        for finding in usable
        if finding["retrieval_method"] == "codex_native_web"
        and finding["evidence_type"] in FULL_EVIDENCE_TYPES
    ]
    counter_ids = {
        query["id"]
        for query in manifest.get("query_plan", [])
        if query.get("role") == "counterevidence"
    }
    counter_hits = [finding for finding in usable if finding["query_id"] in counter_ids]
    authoritative_claims = {
        finding["claim_id"]
        for finding in usable
        if finding["claim_label"] in {"VERIFIED", "TRIANGULATED"}
        and finding["evidence_type"] in FULL_EVIDENCE_TYPES
    }
    methods = sorted({finding["retrieval_method"] for finding in usable})
    return {
        "accepted_findings": len(findings),
        "usable_findings": len(usable),
        "source_urls": len(urls),
        "domains": len(domains),
        "full_page_sources": len(full_urls),
        "snippet_only_sources": len(snippet_urls),
        "effective_sources": len(full_urls) + (0.5 * len(snippet_urls)),
        "native_web_full_reads": len(native_full),
        "counterevidence_findings": len(counter_hits),
        "authoritative_claims": len(authoritative_claims),
        "retrieval_methods": methods,
    }


def research_status(
    findings: Sequence[Dict[str, Any]], quarantined: Sequence[Dict[str, Any]], manifest: Dict[str, Any]
) -> Tuple[str, List[str], Dict[str, Any]]:
    metrics = coverage_metrics(findings, manifest)
    gate = manifest["completion_gate"]
    failures: List[str] = []
    if quarantined:
        failures.append(f"{len(quarantined)} invalid finding(s) quarantined")
    if metrics["native_web_full_reads"] < 1:
        failures.append("no full page opened through Codex native web")
    if metrics["effective_sources"] < gate["min_sources"]:
        failures.append(
            f"effective source floor unmet: {metrics['effective_sources']:.1f}/{gate['min_sources']}"
        )
    if metrics["domains"] < gate["min_domains"]:
        failures.append(f"domain floor unmet: {metrics['domains']}/{gate['min_domains']}")
    if metrics["full_page_sources"] < gate["min_full_page_reads"]:
        failures.append(
            f"full-page floor unmet: {metrics['full_page_sources']}/{gate['min_full_page_reads']}"
        )
    if metrics["counterevidence_findings"] < 1:
        failures.append("counterevidence query has no recorded finding")
    if metrics["authoritative_claims"] < gate.get("min_authoritative_claims", 1):
        failures.append(
            "authoritative claim floor unmet: "
            f"{metrics['authoritative_claims']}/{gate.get('min_authoritative_claims', 1)}"
        )

    if quarantined or not findings:
        status = "FAILED"
    elif failures:
        status = "DEGRADED"
    else:
        status = "REAL"
    return status, failures, metrics


def md_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def render_evidence_pack(
    findings: Sequence[Dict[str, Any]], manifest: Dict[str, Any], receipt: Dict[str, Any]
) -> str:
    metrics = receipt["metrics"]
    lines = [
        f"# Free-First Research Evidence Pack: {manifest['objective']}",
        "",
        f"**Depth:** {manifest['depth']}  ",
        f"**Status:** {receipt['status']}  ",
        f"**Paid cost:** $0.00  ",
        f"**Retrieved:** {receipt['completed_at']}",
        "",
        "## Decision It Supports",
        "",
        manifest["decision"],
        "",
        "## Research Receipt",
        "",
        f"- Source URLs: {metrics['source_urls']}",
        f"- Independent domains: {metrics['domains']}",
        f"- Full-page sources: {metrics['full_page_sources']}",
        f"- Snippet-only sources: {metrics['snippet_only_sources']}",
        f"- Effective sources: {metrics['effective_sources']:.1f}",
        f"- Native-web full reads: {metrics['native_web_full_reads']}",
        f"- Authoritative claims: {metrics['authoritative_claims']}",
        f"- Current-world freshness window: {manifest['freshness_policy']['max_age_hours']} hours",
        f"- Retrieval methods: {', '.join(metrics['retrieval_methods']) or 'none'}",
        f"- Invalid findings quarantined: {receipt['quarantined_count']}",
        f"- Blocked paths executed: {', '.join(receipt['blocked_paths_executed']) or 'none'}",
        f"- Estimated Tavily API credits: {receipt['quota_usage']['estimated_tavily_api_credits']}",
        f"- Tavily billing-plan verification: "
        f"{'verified' if receipt['quota_usage']['billing_plan_verified'] else 'not available to runtime'}",
        "",
        "## Authority Boundary",
        "",
        "Current-world claims below come from live public sources retrieved in this run. Local context and skills are listed separately and do not count as current-world proof.",
        "",
        "## Evidence Ledger",
        "",
        "| Claim ID | Label | Claim | Source | Method | Retrieved |",
        "|---|---|---|---|---|---|",
    ]
    for finding in findings:
        label = finding["source_title"] or finding["domain"] or finding["source_url"]
        source = f"[{md_escape(label)}]({finding['source_url']})"
        lines.append(
            f"| {md_escape(finding['claim_id'])} | {finding['claim_label']} | "
            f"{md_escape(finding['claim'])} | {source} | {finding['retrieval_method']} | "
            f"{finding['retrieved_at']} |"
        )

    contradictions = [
        finding
        for finding in findings
        if finding["stance"] == "contradict" or finding["claim_label"] == "CONTRADICTED"
    ]
    lines += [
        "",
        "## Contradictions And Gaps",
        "",
        "Counterpoint, risk, and limitation evidence is separated here so agreement across official sources is not mistaken for a completed adversarial check.",
        "",
    ]
    if contradictions:
        for finding in contradictions:
            lines.append(f"- **{finding['claim_id']}:** {finding['claim']} — {finding['source_url']}")
    else:
        lines.append("- No contradiction was recorded; treat this as a gap unless the counterevidence query and receipt explain the absence.")
    for failure in receipt["gate_failures"]:
        lines.append(f"- Gate gap: {failure}")

    context_plan = manifest["context_plan"]
    lines += [
        "",
        "## Local Context And Relevant Skills",
        "",
        f"- Skills: {', '.join(context_plan['relevant_skills'])}",
        f"- Local paths: {', '.join(context_plan['local_paths']) or 'none'}",
        "- Role: question shaping, constraints, skill selection, and interpretation only.",
        "",
        "## Use-Now And Value Receipt",
        "",
        f"- Use-now artifact: {manifest['value_contract']['use_now_artifact']}",
        f"- Downstream use: {manifest['value_contract']['downstream_use']}",
        f"- Data returned: {receipt['value_receipt']['data_returned']}",
        f"- Evidence gate: {receipt['value_receipt']['evidence_gate']}",
        f"- Decision supported: {receipt['value_receipt']['decision_supported']}",
        f"- Artifact produced: {receipt['value_receipt']['artifact_produced']}",
        f"- Accepted by operator: {receipt['value_receipt']['accepted_by_operator']}",
        f"- Used in work: {receipt['value_receipt']['used_in_work']}",
        f"- Commercial event: {receipt['value_receipt']['commercial_event']}",
        "",
        "## Sources",
        "",
    ]
    seen = set()
    for finding in findings:
        if finding["source_url"] in seen:
            continue
        seen.add(finding["source_url"])
        title = finding["source_title"] or finding["domain"] or finding["source_url"]
        lines.append(f"- [{title}]({finding['source_url']})")
    return "\n".join(lines) + "\n"


def cmd_ingest(args: argparse.Namespace) -> int:
    mission_dir, _, manifest = resolve_mission(args.mission)
    paths = findings_paths(mission_dir, args.findings or [])
    findings, quarantined = load_and_validate_findings(paths, manifest)
    status, failures, metrics = research_status(findings, quarantined, manifest)
    completed_at = utc_now()
    receipt = {
        "schema_version": SCHEMA_VERSION,
        "mission_id": manifest["mission_id"],
        "completed_at": completed_at,
        "status": status,
        "acceptable": status == "REAL",
        "depth": manifest["depth"],
        "cost_usd": 0.0,
        "blocked_paths_executed": [],
        "quota_usage": quota_usage(mission_dir),
        "input_files": [str(path) for path in paths],
        "metrics": metrics,
        "quarantined_count": len(quarantined),
        "gate_failures": failures,
        "value_receipt": {
            "data_returned": len(findings),
            "evidence_gate": "PASS" if status == "REAL" else ("PARTIAL" if findings else "FAIL"),
            "decision_supported": manifest["decision"] if status == "REAL" else "NOT YET",
            "artifact_produced": str(mission_dir / "evidence-pack.md"),
            "downstream_use": manifest["value_contract"]["downstream_use"],
            "accepted_by_operator": "UNTESTED",
            "used_in_work": "NO EVENT",
            "commercial_event": "NO EVENT",
        },
    }
    write_json(mission_dir / "research-receipt.json", receipt)
    write_json(mission_dir / "validated-findings.json", findings)
    write_json(mission_dir / "quarantine.json", quarantined)
    (mission_dir / "evidence-pack.md").write_text(
        render_evidence_pack(findings, manifest, receipt), encoding="utf-8"
    )
    print(json.dumps(receipt, indent=2))
    return 0 if status == "REAL" else 2


def append_runtime_event(mission_dir: Path, event: Dict[str, Any]) -> None:
    event = {"at": utc_now(), **event}
    path = mission_dir / "runtime-events.jsonl"
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=False) + "\n")


def native_attempt_exists(mission_dir: Path) -> bool:
    path = mission_dir / "native-web-findings.jsonl"
    return path.exists() and bool(path.read_text(encoding="utf-8").strip())


def quota_usage(mission_dir: Path) -> Dict[str, Any]:
    """Summarize disclosed quota use without pretending to inspect billing."""
    credits = 0
    events = 0
    confirmed_events = 0
    path = mission_dir / "runtime-events.jsonl"
    if path.exists():
        for raw in path.read_text(encoding="utf-8").splitlines():
            try:
                event = json.loads(raw)
            except json.JSONDecodeError:
                continue
            if event.get("event") == "tavily_search_extract":
                events += 1
                credits += int(event.get("estimated_api_credits", 0))
                if event.get("zero_dollar_tavily_confirmed") is True:
                    confirmed_events += 1
    return {
        "tavily_search_extract_events": events,
        "estimated_tavily_api_credits": credits,
        "billing_plan_verified": bool(events) and confirmed_events == events,
        "note": (
            "Credit estimate is disclosed. Tavily calls fail closed unless the operator "
            "confirms the account cannot create a dollar charge; the runtime cannot inspect the plan itself."
        ),
    }


def cmd_tavily(args: argparse.Namespace) -> int:
    mission_dir, _, manifest = resolve_mission(args.mission)
    if not native_attempt_exists(mission_dir) and not args.native_unavailable_reason:
        print(
            "Native web must run first. Add native-web-findings.jsonl or provide "
            "--native-unavailable-reason to record the failed first attempt.",
            file=sys.stderr,
        )
        return 2
    if args.native_unavailable_reason:
        append_runtime_event(
            mission_dir,
            {"event": "native_web_unavailable", "reason": args.native_unavailable_reason},
        )
    if not args.confirm_zero_dollar_tavily:
        print(
            "Refusing Tavily: verify the account plan and overage setting, then rerun "
            "with --confirm-zero-dollar-tavily. Native web and RSS remain available.",
            file=sys.stderr,
        )
        return 2

    sys.path.insert(0, str(EXEC))
    try:
        from native_floor import load_env_vars, tavily_extract, tavily_search  # type: ignore

        env = load_env_vars()
        raw_results: List[Tuple[Dict[str, str], Dict[str, Any]]] = []
        for query in manifest["query_plan"][: args.max_queries]:
            results = tavily_search(
                query["query"],
                max_results=args.max_results_per_query,
                env=env,
                search_depth="basic",
            )
            raw_results.extend((query, result) for result in results)

        urls: List[str] = []
        for _, result in raw_results:
            url = str(result.get("url") or "").strip()
            if url and not public_url_error(url) and url not in urls:
                urls.append(url)
        pages = tavily_extract(urls[: args.max_extracts])
    finally:
        if sys.path and sys.path[0] == str(EXEC):
            sys.path.pop(0)

    page_map = {
        str(page.get("url")): str(page.get("raw_content") or "").strip()
        for page in pages
        if page.get("url")
    }
    retrieved_at = utc_now()
    rows: List[Dict[str, Any]] = []
    seen = set()
    for index, (query, result) in enumerate(raw_results, 1):
        url = str(result.get("url") or "").strip()
        if not url or public_url_error(url) or url in seen:
            continue
        seen.add(url)
        extracted = page_map.get(url, "")
        snippet = str(result.get("content") or result.get("title") or "").strip()
        content = clean_research_text(extracted or snippet)
        if len(content) < 40:
            continue
        rows.append(
            {
                "claim_id": f"tavily-{index:03d}",
                "claim": content[:600],
                "source_url": url,
                "source_title": str(result.get("title") or "").strip(),
                "source_class": "secondary",
                "retrieval_method": "tavily_extract" if extracted else "tavily_search",
                "evidence_type": "page_read" if extracted else "search_snippet",
                "retrieved_at": retrieved_at,
                "published_at": "",
                "query_id": query["id"],
                "claim_label": "DIRECTIONAL",
                "claim_scope": "current_world",
                "stance": "support",
                "excerpt": content[:400],
            }
        )
    output = mission_dir / (args.output or "tavily-findings.jsonl")
    write_jsonl(output, rows)
    append_runtime_event(
        mission_dir,
        {
            "event": "tavily_search_extract",
            "queries": min(args.max_queries, len(manifest["query_plan"])),
            "findings": len(rows),
            "extracts": sum(1 for row in rows if row["retrieval_method"] == "tavily_extract"),
            "search_depth": "basic",
            "extract_depth": "basic",
            "estimated_api_credits": min(args.max_queries, len(manifest["query_plan"]))
            + ((len(pages) + 4) // 5),
            "zero_dollar_tavily_confirmed": True,
            "cost_usd": 0.0,
        },
    )
    print(
        json.dumps(
            {
                "status": "COMPLETE" if rows else "EMPTY",
                "findings": len(rows),
                "output": str(output),
                "cost_usd": 0.0,
                "estimated_api_credits": min(args.max_queries, len(manifest["query_plan"]))
                + ((len(pages) + 4) // 5),
                "zero_dollar_tavily_confirmed": True,
                "tavily_research_used": False,
            },
            indent=2,
        )
    )
    return 0 if rows else 2


def strip_markup(value: str) -> str:
    value = html.unescape(value or "")
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def clean_research_text(value: str) -> str:
    """Remove embedded links from extracted prose before it enters a claim.

    The source URL belongs in `source_url`. Leaving avatar, navigation, or
    inline-markdown URLs inside claim text causes generic URL counters to treat
    page chrome as independent research sources.
    """
    value = re.sub(r"!\[[^\]]*\]\([^\)]+\)", " ", value or "")
    value = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", value)
    value = re.sub(r"https?://[^\s\)\]>]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower()


def child_text(element: ET.Element, names: Sequence[str]) -> str:
    wanted = {name.lower() for name in names}
    for child in element:
        if local_name(child.tag) in wanted and child.text:
            return child.text.strip()
    return ""


def entry_link(element: ET.Element) -> str:
    for child in element:
        if local_name(child.tag) != "link":
            continue
        href = (child.attrib.get("href") or child.text or "").strip()
        rel = (child.attrib.get("rel") or "alternate").lower()
        if href and rel in {"alternate", ""}:
            return href
    return child_text(element, ("guid",))


def normalize_feed_date(value: str) -> str:
    if not value:
        return ""
    parsed = parse_iso(value)
    if parsed:
        return parsed.astimezone(timezone.utc).isoformat()
    try:
        parsed_mail = parsedate_to_datetime(value)
        if parsed_mail.tzinfo is None:
            parsed_mail = parsed_mail.replace(tzinfo=timezone.utc)
        return parsed_mail.astimezone(timezone.utc).isoformat()
    except Exception:
        return ""


def parse_feed(data: bytes, feed_url: str, query_id: str, max_items: int) -> List[Dict[str, Any]]:
    root = ET.fromstring(data)
    entries = [node for node in root.iter() if local_name(node.tag) in {"item", "entry"}]
    retrieved_at = utc_now()
    rows: List[Dict[str, Any]] = []
    for index, entry in enumerate(entries[:max_items], 1):
        title = strip_markup(child_text(entry, ("title",)))
        summary = strip_markup(child_text(entry, ("description", "summary", "content")))
        link = entry_link(entry)
        published = normalize_feed_date(
            child_text(entry, ("pubdate", "published", "updated", "date"))
        )
        if not title or not link or public_url_error(link) or not published:
            continue
        rows.append(
            {
                "claim_id": f"rss-{slugify(urlparse(feed_url).hostname or 'feed', 20)}-{index:03d}",
                "claim": title if not summary else f"{title}: {summary[:500]}",
                "source_url": link,
                "source_title": title,
                "source_class": "feed",
                "retrieval_method": "rss",
                "evidence_type": "feed_item",
                "retrieved_at": retrieved_at,
                "published_at": published,
                "query_id": query_id,
                "claim_label": "DIRECTIONAL",
                "claim_scope": "current_world",
                "stance": "support",
                "excerpt": summary[:400],
            }
        )
    return rows


def fetch_feed(url: str, timeout: float = 30.0) -> bytes:
    error = public_url_error(url)
    if error:
        raise ValueError(error)
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Antigravity-Free-First-Research/1.0"},
    )
    try:
        import certifi

        tls_context = ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        tls_context = ssl.create_default_context()
    with urllib.request.urlopen(  # nosec B310: public URL validated; TLS verification remains enabled
        request,
        timeout=timeout,
        context=tls_context,
    ) as response:
        return response.read(2_000_000)


def cmd_rss(args: argparse.Namespace) -> int:
    mission_dir, _, manifest = resolve_mission(args.mission)
    query_ids = {query["id"] for query in manifest["query_plan"]}
    query_id = args.query_id or "q-rss-changelog"
    if query_id not in query_ids:
        print(f"Unknown query id: {query_id}", file=sys.stderr)
        return 2
    rows: List[Dict[str, Any]] = []
    errors: List[str] = []
    for url in args.url:
        try:
            rows.extend(parse_feed(fetch_feed(url), url, query_id, args.max_items))
        except Exception as exc:
            errors.append(f"{url}: {type(exc).__name__}: {exc}")
    output = mission_dir / (args.output or "rss-findings.jsonl")
    write_jsonl(output, rows)
    append_runtime_event(
        mission_dir,
        {"event": "rss_pull", "feeds": len(args.url), "findings": len(rows), "errors": errors},
    )
    print(
        json.dumps(
            {"status": "COMPLETE" if rows else "EMPTY", "findings": len(rows), "output": str(output), "errors": errors},
            indent=2,
        )
    )
    return 0 if rows else 2


def verify_manifest(manifest: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    if manifest.get("schema_version") != SCHEMA_VERSION:
        errors.append("wrong or missing schema_version")
    if manifest.get("owner") != "/deep-research-os":
        errors.append("/deep-research-os must remain the function owner")
    if manifest.get("execution_mode") != "codex_native_free_first":
        errors.append("execution_mode must be codex_native_free_first")
    ladder = manifest.get("source_ladder") or []
    if not ladder or ladder[0].get("method") != "codex_native_web":
        errors.append("Codex native web must be first in the source ladder")
    blocked = manifest.get("blocked") or {}
    if not set(BLOCKED_PROVIDERS).issubset(set(blocked.get("providers") or [])):
        errors.append("blocked provider list is incomplete")
    if blocked.get("schedules_allowed") is not False:
        errors.append("schedules must be disabled")
    if blocked.get("subagents_allowed") is not False:
        errors.append("subagents must be disabled")
    if float(blocked.get("paid_cost_usd_max", -1)) != 0.0:
        errors.append("paid cost cap must be zero")
    if blocked.get("tavily_zero_dollar_confirmation_required") is not True:
        errors.append("Tavily must require explicit zero-dollar account confirmation")
    policy = manifest.get("authority_policy") or {}
    if policy.get("current_world_authority") != "live_external_sources_retrieved_this_run":
        errors.append("live external sources must hold current-world authority")
    if not manifest.get("decision"):
        errors.append("mission must name the decision it supports")
    freshness = manifest.get("freshness_policy") or {}
    if not 1 <= int(freshness.get("max_age_hours", 0)) <= 720:
        errors.append("freshness policy must define max_age_hours between 1 and 720")
    if freshness.get("retrieved_during_mission_required") is not True:
        errors.append("current-world evidence must be retrieved during this mission")
    value = manifest.get("value_contract") or {}
    if not value.get("downstream_use") or not value.get("use_now_artifact"):
        errors.append("mission must name downstream use and use-now artifact")
    roles = {query.get("role") for query in manifest.get("query_plan") or []}
    if "official_current" not in roles or "counterevidence" not in roles:
        errors.append("query plan needs official_current and counterevidence angles")
    return errors


def cmd_verify(args: argparse.Namespace) -> int:
    mission_dir, _, manifest = resolve_mission(args.mission)
    errors = verify_manifest(manifest)
    receipt_path = mission_dir / "research-receipt.json"
    receipt: Dict[str, Any] = {}
    if args.require_receipt and not receipt_path.exists():
        errors.append("research-receipt.json is required but missing")
    elif receipt_path.exists():
        receipt = read_json(receipt_path)
        if float(receipt.get("cost_usd", -1)) != 0.0:
            errors.append("receipt paid cost must be zero")
        if receipt.get("blocked_paths_executed"):
            errors.append("receipt reports an executed blocked path")
        if receipt.get("status") == "REAL" and not receipt.get("acceptable"):
            errors.append("REAL receipt must be acceptable")
    payload = {
        "status": "PASS" if not errors else "FAIL",
        "mission_id": manifest.get("mission_id"),
        "errors": errors,
        "receipt_status": receipt.get("status", "NOT RUN"),
        "cost_usd": receipt.get("cost_usd", 0.0),
    }
    print(json.dumps(payload, indent=2))
    return 0 if not errors else 2


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="free_first_research.py",
        description="Compile and validate Codex-native, zero-paid-spend research missions.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    plan = sub.add_parser("plan", help="Compile a mission manifest and native-web runbook")
    plan.add_argument("--objective", required=True)
    plan.add_argument("--decision", required=True)
    plan.add_argument("--downstream", required=True)
    plan.add_argument("--artifact", required=True)
    plan.add_argument("--depth", default="standard", choices=("quick", "standard", "deep", "max"))
    plan.add_argument(
        "--freshness-hours",
        type=int,
        default=72,
        help="Maximum age for current-world evidence (default: 72; allowed: 1-720)",
    )
    plan.add_argument("--context", action="append", default=[])
    plan.add_argument("--skill", action="append", default=[])
    plan.add_argument("--query", action="append", default=[])
    plan.add_argument("--output", default=None)
    plan.set_defaults(func=cmd_plan)

    ingest = sub.add_parser("ingest", help="Validate JSONL findings and write evidence/value receipts")
    ingest.add_argument("--mission", required=True)
    ingest.add_argument("--findings", action="append", default=[])
    ingest.set_defaults(func=cmd_ingest)

    tavily = sub.add_parser("tavily", help="Run bounded Tavily Search/Extract after native web")
    tavily.add_argument("--mission", required=True)
    tavily.add_argument("--max-queries", type=int, default=2, choices=range(1, 6))
    tavily.add_argument("--max-results-per-query", type=int, default=3, choices=range(1, 9))
    tavily.add_argument("--max-extracts", type=int, default=4, choices=range(1, 21))
    tavily.add_argument("--native-unavailable-reason", default="")
    tavily.add_argument(
        "--confirm-zero-dollar-tavily",
        action="store_true",
        help="Assert that Tavily plan and overage settings cannot create a dollar charge",
    )
    tavily.add_argument("--output", default=None)
    tavily.set_defaults(func=cmd_tavily)

    rss = sub.add_parser("rss", help="Pull public RSS/Atom feeds once; creates no schedule")
    rss.add_argument("--mission", required=True)
    rss.add_argument("--url", action="append", required=True)
    rss.add_argument("--query-id", default="q-rss-changelog")
    rss.add_argument("--max-items", type=int, default=10, choices=range(1, 51))
    rss.add_argument("--output", default=None)
    rss.set_defaults(func=cmd_rss)

    verify = sub.add_parser("verify", help="Verify mission policy and optional completed receipt")
    verify.add_argument("--mission", required=True)
    verify.add_argument("--require-receipt", action="store_true")
    verify.set_defaults(func=cmd_verify)
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return int(args.func(args))
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
