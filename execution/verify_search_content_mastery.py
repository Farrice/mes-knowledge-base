#!/usr/bin/env python3
"""Acceptance verifier for the Search Content Mastery companion OS.

The verifier exercises the public command surface in temporary project packs.
It never publishes, calls a connector, uses a paid service, or mutates a skill.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
RUNTIME = ROOT / "execution" / "search_content_mastery.py"
FIXTURES = ROOT / "execution" / "fixtures" / "search-content-mastery"
SCHEMA_ROOT = ROOT / "schemas" / "search-content-mastery"
CORPUS_IDS = (
    "vVJB2FjOF2k",
    "3sHPiOIHPTY",
    "Fh_54G6p_cs",
    "AaSyn9YSNYQ",
    "4tqCKkGilXI",
    "hDBsQTK7VTc",
    "lkFA-aBN_LM",
    "qzMAGdzra88",
    "53h_-LoEGiw",
    "6o0mabKRmIo",
    "LiLD7_tjn4o",
)
PROTECTED_HASHES = {
    "_active/health-performance-ip-library/AUTOMATION_PROMPT.md": "d02422402dd4d9435510d06d44b3c65385e1cab295e1c6c1d1e30b11011abe1b",
    "_active/linkedin/04-deliverables/context-os/02-OFFER-CANON.md": "e485f8f386e085710dd5985de0dfe12612be715ed7a9298ebfd7da9975c92b05",
    "_active/health-performance-ip-library/ledger/insights.jsonl": "2400d50880c5164065ea624315dc8cb8606fb98ab216693969577db09ca43fd5",
    "_active/health-performance-ip-library/ledger/promises-not-kept.jsonl": "6dcc0663f26bf119dddac05d2ba5a2b5df1ad95dc6afb88662f865ada8df7a70",
}
ROUTING_QUERY = "build a source-grounded SEO AEO GEO content system that can audit plan create score and measure"
ROUTING_FIXTURE = FIXTURES / "routing" / "natural-language.json"
ANGLE_MAP_PROTOTYPE = ROOT / "_active" / "search-content-mastery" / "angle-map-search-answer-prototype"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_json_output(text: str) -> dict[str, Any]:
    try:
        value = json.loads(text)
    except json.JSONDecodeError as exc:
        raise AssertionError(f"command did not return JSON: {text[-1000:]}") from exc
    if not isinstance(value, dict):
        raise AssertionError("command result must be a JSON object")
    return value


def run_command(argv: list[str], expected: int = 0) -> tuple[dict[str, Any], subprocess.CompletedProcess[str]]:
    completed = subprocess.run(argv, cwd=ROOT, text=True, capture_output=True, check=False)
    if completed.returncode != expected:
        raise AssertionError(
            f"expected exit {expected}, received {completed.returncode}\n"
            f"stdout:\n{completed.stdout[-2000:]}\nstderr:\n{completed.stderr[-2000:]}"
        )
    stream = completed.stdout if expected == 0 else completed.stderr
    return parse_json_output(stream), completed


def run_runtime(*args: str, expected: int = 0) -> dict[str, Any]:
    result, _ = run_command([sys.executable, str(RUNTIME), *args], expected=expected)
    return result


class Receipt:
    def __init__(self) -> None:
        self.checks: list[dict[str, Any]] = []

    def check(self, name: str, fn: Any) -> None:
        try:
            evidence = fn()
            self.checks.append({"name": name, "status": "PASS", "evidence": evidence})
        except Exception as exc:  # noqa: BLE001 - verifier must collect every failure
            self.checks.append({"name": name, "status": "FAIL", "evidence": str(exc)})

    @property
    def passed(self) -> bool:
        return all(item["status"] == "PASS" for item in self.checks)

    def payload(self) -> dict[str, Any]:
        passed = sum(item["status"] == "PASS" for item in self.checks)
        return {
            "schema_version": "search-content-mastery-verification/v1",
            "verified_at": utc_now(),
            "status": "PASS" if self.passed else "FAIL",
            "proof_state": "RUNTIME_OBSERVED" if self.passed else "UNTESTED",
            "market_effect_state": "UNTESTED",
            "summary": {"passed": passed, "failed": len(self.checks) - passed, "total": len(self.checks)},
            "checks": self.checks,
            "boundaries": [
                "Runtime observation proves local behavior, not rankings, citations, traffic, leads, conversions, or revenue.",
                "No external publishing, outreach, connector write, payment, deployment, or paid generation occurred.",
            ],
        }


def first_existing(directory: Path, names: tuple[str, ...]) -> Path:
    for name in names:
        candidate = directory / name
        if candidate.exists():
            return candidate
    raise AssertionError(f"none of {names} exists in {directory}")


def verify_corpus() -> dict[str, Any]:
    root = ROOT / "extractions" / "video-context"
    details: dict[str, Any] = {}
    for video_id in CORPUS_IDS:
        package = root / video_id
        if not package.is_dir():
            raise AssertionError(f"missing evidence package: {video_id}")
        metadata = first_existing(package, ("metadata.json", "source-metadata.json"))
        provenance = first_existing(package, ("provenance.json", "transcript-provenance.json"))
        transcript = first_existing(package, ("transcript.txt", "transcript-reference.json"))
        analysis = first_existing(package, ("analysis.md", "evidence-analysis.md", "claims.json"))
        uncertainty = first_existing(package, ("uncertainty.md", "uncertainty-report.md"))
        visual = first_existing(package, ("visual-ledger.json", "visual-ledger.md"))
        hashes = first_existing(package, ("hashes.json", "evidence-package.json", "manifest.json"))
        for path in (metadata, provenance, transcript, analysis, uncertainty, visual, hashes):
            if path.stat().st_size == 0:
                raise AssertionError(f"empty evidence file: {path}")
        timestamped = package / "transcript_segments.json"
        if not timestamped.is_file() or timestamped.stat().st_size == 0:
            raise AssertionError(f"missing timestamped transcript derivative: {video_id}")
        analysis_text = analysis.read_text(encoding="utf-8", errors="replace")
        if not re.search(r"\b\d{1,2}:\d{2}\b", analysis_text):
            raise AssertionError(f"analysis has no timestamped claim anchors: {video_id}")
        hash_payload = json.loads((package / "hashes.json").read_text(encoding="utf-8"))
        hash_entries = hash_payload.get("files", hash_payload)
        verified_hashes = 0
        for ref, expected_hash in hash_entries.items():
            if not isinstance(expected_hash, str) or not re.fullmatch(r"[a-f0-9]{64}", expected_hash):
                continue
            candidate = (package / ref).resolve()
            if not candidate.is_file():
                # Frame/download binaries stay in the temporary capture store;
                # their hashes remain in the visual/source ledger by design.
                continue
            if sha256(candidate) != expected_hash:
                raise AssertionError(f"source hash mismatch: {video_id}/{ref}")
            verified_hashes += 1
        if verified_hashes < 4:
            raise AssertionError(f"too few on-disk source hashes verified for {video_id}: {verified_hashes}")
        details[video_id] = {
            "metadata": str(metadata.relative_to(ROOT)),
            "transcript": str(transcript.relative_to(ROOT)),
            "analysis": str(analysis.relative_to(ROOT)),
            "visual": str(visual.relative_to(ROOT)),
            "verified_hashes": verified_hashes,
        }
    if set(details) != set(CORPUS_IDS):
        raise AssertionError("corpus is not exactly the locked eleven-source set")
    return {"packages": len(details), "video_ids": list(details), "details": details}


def normalized_tokens(path: Path) -> list[str]:
    return re.findall(r"[a-z0-9]+", path.read_text(encoding="utf-8", errors="replace").lower())


def transcript_path_from_reference(package: Path) -> Path:
    direct = package / "transcript.txt"
    if direct.exists():
        return direct
    ref = json.loads((package / "transcript-reference.json").read_text(encoding="utf-8"))
    for key in ("path", "transcript_path", "canonical_path", "source_path", "reference"):
        if isinstance(ref.get(key), str):
            candidate = (package / ref[key]).resolve() if not Path(ref[key]).is_absolute() else Path(ref[key]).resolve()
            if candidate.exists():
                return candidate
    raise AssertionError(f"unresolvable transcript reference: {package / 'transcript-reference.json'}")


def verify_reused_sources() -> dict[str, Any]:
    canonical = {
        "3sHPiOIHPTY": ROOT / "extractions" / "nathan-gotch" / "transcript.txt",
        "qzMAGdzra88": ROOT / "extractions" / "nathan-gotch-ai-seo" / "reference-corpus" / "how-to-rank-everywhere-seo-content.txt",
        "6o0mabKRmIo": ROOT / "extractions" / "nathan-gotch-ai-seo" / "reference-corpus" / "ecommerce-seo-strategy-2026.txt",
    }
    result: dict[str, Any] = {}
    for video_id, source in canonical.items():
        if not source.exists():
            raise AssertionError(f"missing canonical reused source: {source}")
        package = ROOT / "extractions" / "video-context" / video_id
        reference_path = package / "transcript-reference.json"
        if not reference_path.exists():
            raise AssertionError(f"reused source was duplicated instead of referenced: {video_id}")
        reference = json.loads(reference_path.read_text(encoding="utf-8"))
        packaged = transcript_path_from_reference(package)
        if packaged.resolve() != source.resolve():
            raise AssertionError(f"transcript reference does not point to canonical source: {video_id}")
        if reference.get("canonical_sha256") != sha256(source):
            raise AssertionError(f"canonical hash receipt mismatch for {video_id}")
        exact = reference.get("normalized_token_stream_exact_match") or reference.get("preamble_stripped_normalized_exact_match")
        if exact is not True or float(reference.get("normalized_similarity_ratio", 0)) != 1.0:
            raise AssertionError(f"fresh capture did not exactly match reused source: {video_id}")
        derivative = package / "transcript_segments.json"
        if sha256(derivative) != reference.get("timed_derivative_sha256"):
            raise AssertionError(f"timestamped derivative hash mismatch for {video_id}")
        result[video_id] = {
            "canonical": str(source.relative_to(ROOT)),
            "canonical_sha256": sha256(source),
            "reference": str(reference_path.relative_to(ROOT)),
            "normalized_exact_match": True,
            "timed_derivative_sha256": reference["timed_derivative_sha256"],
        }
    return result


def verify_protected_files() -> dict[str, str]:
    observed: dict[str, str] = {}
    for ref, expected in PROTECTED_HASHES.items():
        path = ROOT / ref
        if not path.exists():
            raise AssertionError(f"protected file missing: {ref}")
        actual = sha256(path)
        if actual != expected:
            raise AssertionError(f"protected file changed: {ref}; expected {expected}, observed {actual}")
        observed[ref] = actual
    return observed


def verify_routing() -> dict[str, Any]:
    fixture = json.loads(ROUTING_FIXTURE.read_text(encoding="utf-8"))
    cases = {
        "system-language": {
            "request": ROUTING_QUERY,
            "expected_first_route": "search-content-mastery",
            "expected_binding": "operator_search_content_mastery",
        },
        "natural-language-angle-map": fixture,
    }
    observed: dict[str, Any] = {}
    for name, case in cases.items():
        query = str(case["request"])
        expected_route = str(case["expected_first_route"])
        expected_binding = str(case["expected_binding"])

        completed = subprocess.run(
            [sys.executable, str(ROOT / "execution" / "workflow_router.py"), "search", query, "--top", "3"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        if completed.returncode != 0:
            raise AssertionError(completed.stderr)
        route_lines = [line.strip() for line in completed.stdout.splitlines() if line.strip().startswith("/")]
        if not route_lines or not route_lines[0].startswith(f"/{expected_route}"):
            raise AssertionError(f"{name} unexpected first route: {route_lines[:3]}")

        menu = subprocess.run(
            [sys.executable, str(ROOT / "execution" / "command_menu.py"), "search", query, "--limit", "3"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        if menu.returncode != 0:
            raise AssertionError(menu.stderr)
        menu_lines = [line.strip() for line in menu.stdout.splitlines() if re.match(r"^\d+\. `/", line.strip())]
        if not menu_lines or not menu_lines[0].startswith(f"1. `/{expected_route}`"):
            raise AssertionError(f"{name} unexpected first command-menu route: {menu_lines[:3]}")

        binding, _ = run_command(
            [
                sys.executable,
                str(ROOT / "execution" / "routing_enforcer.py"),
                "check",
                "--request",
                query,
                "--workflow",
                expected_route,
                "--no-log",
            ]
        )
        if binding.get("binding_matched") != expected_binding:
            raise AssertionError(f"{name} wrong binding: {binding}")

        preflight, _ = run_command(
            [
                sys.executable,
                str(ROOT / "execution" / "autopilot_runtime_preflight.py"),
                query,
                "--json",
            ]
        )
        chosen = preflight.get("chosen_path", {}).get("primary_route")
        if chosen != expected_route:
            raise AssertionError(f"{name} Autopilot chose {chosen!r}, expected {expected_route!r}")
        observed[name] = {
            "workflow_router_first": route_lines[0],
            "command_menu_first": menu_lines[0],
            "autopilot_route": chosen,
            "binding_signal": binding.get("matched_signal"),
        }

    from routing_enforcer import match_bindings  # local, side-effect-free

    negatives = {
        "perform a technical SEO audit for example.com",
        "design one AEO citation experiment",
        "health check the harness",
        "write a YouTube video script from this approved brief",
    }
    false_positives = [query for query in negatives if any(hit["binding_id"] == "operator_search_content_mastery" for hit in match_bindings(query))]
    if false_positives:
        raise AssertionError(f"binding false positives: {false_positives}")
    return {
        "cases": observed,
        "negative_cases": len(negatives),
    }


def create_project(temp_root: Path, key: str, context_name: str) -> Path:
    project = temp_root / key
    result = run_runtime(
        "foundation",
        "--project",
        str(project),
        "--context",
        str(FIXTURES / "contexts" / context_name),
    )
    if result.get("status") != "CREATED":
        raise AssertionError(result)
    return project


def plan_and_score(project: Path, fixture: str, *, judgment: bool = False, override: bool = False) -> dict[str, Any]:
    brief_result = run_runtime(
        "plan",
        "--project",
        str(project),
        "--input",
        str(FIXTURES / "briefs" / f"{fixture}.json"),
    )
    brief = Path(brief_result["brief"])
    handoff = run_runtime("create", "--project", str(project), "--brief", str(brief))
    score_args = [
        "score",
        "--project",
        str(project),
        "--brief",
        str(brief),
        "--content",
        str(FIXTURES / "content" / f"{fixture}.md"),
    ]
    if judgment:
        score_args.extend(["--expert-judgment", str(FIXTURES / "expert-judgment.json")])
    if override:
        score_args.extend(["--override", str(FIXTURES / "operator-override.json")])
    score = run_runtime(*score_args)
    receipt = json.loads(Path(score["receipt"]).read_text(encoding="utf-8"))
    if len(receipt["dimensions"]) != 10:
        raise AssertionError(f"expected 10 score dimensions for {fixture}")
    if receipt["proof_state"] != "PREDICTED" or receipt["observed_outcomes"]:
        raise AssertionError("score receipt collapsed predicted readiness into observed outcomes")
    if override and (
        receipt["operator_override"]["original_score"] != receipt["original_composite"]
        or receipt["operator_override"]["override_score"] != receipt["final_composite"]
        or receipt["original_composite"] == receipt["final_composite"]
    ):
        raise AssertionError("operator override did not preserve the original score")
    return {
        "fixture": fixture,
        "brief": str(brief),
        "handoff_route": handoff["route"],
        "original_score": receipt["original_composite"],
        "final_score": receipt["final_composite"],
        "dimensions": len(receipt["dimensions"]),
    }


def verify_runtime() -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="search-content-mastery-verify-") as temp:
        temp_root = Path(temp)
        batch_project = temp_root / "batch-project"
        batch_file = temp_root / "batch.json"
        batch_file.write_text(
            json.dumps(
                {
                    "jobs": [
                        {
                            "mode": "foundation",
                            "parameters": {
                                "project": str(batch_project),
                                "context": str(FIXTURES / "contexts" / "local-service.json"),
                            },
                        },
                        {"mode": "audit", "parameters": {"project": str(batch_project)}},
                    ]
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        batch_result = run_runtime("batch", "--file", str(batch_file))
        batch_statuses = [item["result"]["status"] for item in batch_result.get("results", [])]
        if batch_result.get("status") != "BATCH_COMPLETE" or batch_statuses != ["CREATED", "READY_FOR_PLANNING"]:
            raise AssertionError(f"ordered local batch failed: {batch_result}")
        projects = {
            "health": create_project(temp_root, "health", "health-performance.json"),
            "local": create_project(temp_root, "local", "local-service.json"),
            "ecommerce": create_project(temp_root, "ecommerce", "ecommerce.json"),
        }
        resumes = {
            name: run_runtime("foundation", "--project", str(project), "--resume")
            for name, project in projects.items()
        }
        if {result.get("status") for result in resumes.values()} != {"VALID"}:
            raise AssertionError(f"portable project resume failed: {resumes}")
        audits = {name: run_runtime("audit", "--project", str(project)) for name, project in projects.items()}
        scored = [
            plan_and_score(projects["health"], "article", judgment=True, override=True),
            plan_and_score(projects["local"], "local-service-page"),
            plan_and_score(projects["ecommerce"], "ecommerce-page"),
            plan_and_score(projects["health"], "linkedin-post"),
            plan_and_score(projects["health"], "video-script"),
            plan_and_score(projects["health"], "visual-brief"),
        ]

        ecommerce = projects["ecommerce"]
        valid = run_runtime(
            "measure", "--project", str(ecommerce), "--source", "gsc",
            "--input", str(FIXTURES / "imports" / "valid-gsc.csv"),
            "--stage", "TRAFFIC", "--content-id", "ecommerce-page-fixture",
        )
        duplicate = run_runtime(
            "measure", "--project", str(ecommerce), "--source", "gsc",
            "--input", str(FIXTURES / "imports" / "valid-gsc.csv"),
            expected=2,
        )
        partial = run_runtime(
            "measure", "--project", str(ecommerce), "--source", "gsc",
            "--input", str(FIXTURES / "imports" / "partial-gsc.csv"), expected=2,
        )
        malformed = run_runtime(
            "measure", "--project", str(ecommerce), "--source", "gsc",
            "--input", str(FIXTURES / "imports" / "malformed-gsc.csv"), expected=2,
        )
        unknown = run_runtime(
            "measure", "--project", str(ecommerce), "--source", "gsc",
            "--input", str(FIXTURES / "imports" / "unknown-schema-gsc.csv"), expected=2,
        )
        conflicting = run_runtime(
            "measure", "--project", str(ecommerce), "--source", "gsc",
            "--input", str(FIXTURES / "imports" / "aliased-gsc.csv"),
            "--mapping", str(FIXTURES / "imports" / "aliased-gsc.mapping.json"),
            "--date-start", "2026-07-02", expected=2,
        )
        aliased = run_runtime(
            "measure", "--project", str(ecommerce), "--source", "gsc",
            "--input", str(FIXTURES / "imports" / "aliased-gsc.csv"),
            "--mapping", str(FIXTURES / "imports" / "aliased-gsc.mapping.json"),
        )
        citation = run_runtime(
            "measure", "--project", str(ecommerce), "--source", "ai_citation",
            "--input", str(FIXTURES / "imports" / "valid-ai-citation.json"),
            "--stage", "CITED", "--content-id", "ecommerce-page-fixture",
        )
        expected_codes = {
            "duplicate": (duplicate, "DUPLICATE_IMPORT"),
            "partial": (partial, "INCOMPLETE_SCHEMA"),
            "malformed": (malformed, "MALFORMED_IMPORT"),
            "unknown": (unknown, "UNKNOWN_SCHEMA"),
            "conflicting": (conflicting, "CONFLICTING_DATE_RANGE"),
        }
        for name, (result, code) in expected_codes.items():
            if result.get("code") != code:
                raise AssertionError(f"{name} expected {code}, received {result}")
        outcomes = [json.loads(line) for line in (ecommerce / "ledgers" / "outcomes.jsonl").read_text().splitlines() if line.strip()]
        stages = {row["stage"] for row in outcomes}
        if stages != {"TRAFFIC", "CITED"}:
            raise AssertionError(f"outcome stages were collapsed: {stages}")
        recommendations = run_runtime("measure", "--project", str(ecommerce), "--recommend")
        manifest_states = {
            name: json.loads((project / "manifest.json").read_text())["proof_state"]
            for name, project in projects.items()
        }
        if set(manifest_states.values()) != {"UNTESTED"}:
            raise AssertionError(f"cold starts self-promoted their manifests: {manifest_states}")
        return {
            "ordered_local_batch": {"jobs": batch_result["jobs"], "statuses": batch_statuses},
            "cold_starts": {name: audits[name]["status"] for name in projects},
            "portable_resumes": {name: resumes[name]["status"] for name in projects},
            "evaluator_fixtures": scored,
            "imports": {
                "valid": valid["status"],
                "aliased": aliased["status"],
                "ai_citation": citation["status"],
                "rejections": {name: value[0]["code"] for name, value in expected_codes.items()},
            },
            "independent_outcome_stages": sorted(stages),
            "learning_loop": recommendations,
            "project_proof_states": manifest_states,
        }


def verify_system_files() -> dict[str, Any]:
    required = (
        "skills/search-content-mastery-os/SKILL.md",
        "skills/search-content-mastery-os/genius.md",
        ".agent/workflows/search-content-mastery.md",
        ".claude/commands/search-content-mastery.md",
        ".agents/skills/source-command-search-content-mastery/SKILL.md",
        "schemas/search-content-mastery/search-project-manifest.schema.json",
        "schemas/search-content-mastery/search-brief.schema.json",
        "schemas/search-content-mastery/content-score-receipt.schema.json",
        "schemas/search-content-mastery/search-event.schema.json",
        "schemas/search-content-mastery/service-receipt.schema.json",
        "extractions/nathan-gotch-search-content-mastery/skill-system-contract.md",
        "extractions/nathan-gotch-search-content-mastery/agentic-engineering-packet.md",
        "extractions/nathan-gotch-search-content-mastery/goal-packet.md",
    )
    missing = [ref for ref in required if not (ROOT / ref).is_file()]
    if missing:
        raise AssertionError(f"missing system files: {missing}")
    return {"required_files": len(required), "missing": []}


def verify_claim_risk_language() -> dict[str, Any]:
    from search_content_mastery import non_negated_risk_terms

    safe = "This structure does not guarantee that a page will rank or will be cited."
    unsafe = "Our system guarantees results and will rank your page."
    safe_terms = non_negated_risk_terms(safe)
    unsafe_terms = non_negated_risk_terms(unsafe)
    if safe_terms:
        raise AssertionError(f"disclaimer produced false-positive risk terms: {safe_terms}")
    if not unsafe_terms:
        raise AssertionError("asserted guarantee was not detected")
    return {"safe_terms": safe_terms, "asserted_terms": unsafe_terms}


def verify_record_schemas() -> dict[str, Any]:
    """Validate one runtime-observed instance of every public record type."""
    try:
        from jsonschema import Draft202012Validator, FormatChecker
    except ImportError as exc:  # pragma: no cover - environment proof boundary
        raise AssertionError("jsonschema is required for the acceptance verifier") from exc

    pilot_pack = ROOT / "_active" / "search-content-mastery" / "health-performance-pilot" / "project-pack"
    service_files = sorted((pilot_pack / "receipts").glob("service-*.json"))
    brief_files = sorted((pilot_pack / "briefs").glob("brief-*.json"))
    if not service_files or not brief_files:
        raise AssertionError("pilot does not contain schema instances for service and brief records")
    service_records = [
        (path, json.loads(path.read_text(encoding="utf-8")))
        for path in service_files
    ]
    service_path, service_record = max(service_records, key=lambda item: item[1]["created_at"])
    score_path = Path(service_record["artifacts"]["evaluation_receipt"])
    instances: dict[str, Path] = {
        "search-project-manifest.schema.json": pilot_pack / "manifest.json",
        "search-brief.schema.json": brief_files[-1],
        "content-score-receipt.schema.json": score_path,
        "service-receipt.schema.json": service_path,
    }
    validated: dict[str, str] = {}
    checker = FormatChecker()
    for schema_name, record_path in instances.items():
        schema = json.loads((SCHEMA_ROOT / schema_name).read_text(encoding="utf-8"))
        record = json.loads(record_path.read_text(encoding="utf-8"))
        Draft202012Validator(schema, format_checker=checker).validate(record)
        validated[schema_name] = record_path.name

    with tempfile.TemporaryDirectory(prefix="search-content-mastery-schema-") as temp:
        project = create_project(Path(temp), "schema", "ecommerce.json")
        run_runtime(
            "measure", "--project", str(project), "--source", "gsc",
            "--input", str(FIXTURES / "imports" / "valid-gsc.csv"),
            "--stage", "TRAFFIC", "--content-id", "schema-fixture",
        )
        event = json.loads((project / "ledgers" / "outcomes.jsonl").read_text(encoding="utf-8").splitlines()[0])
        event_schema_name = "search-event.schema.json"
        event_schema = json.loads((SCHEMA_ROOT / event_schema_name).read_text(encoding="utf-8"))
        Draft202012Validator(event_schema, format_checker=checker).validate(event)
        validated[event_schema_name] = event["event_id"]
    return {"validated": validated, "draft": "2020-12"}


def verify_service_pilot() -> dict[str, Any]:
    pilot = ROOT / "_active" / "search-content-mastery" / "health-performance-pilot"
    manifest = pilot / "project-pack" / "manifest.json"
    service_map = pilot / "service-artifacts.json"
    behavior_proof = pilot / "behavior-proof.md"
    if not manifest.exists() or not service_map.exists() or not behavior_proof.exists():
        raise AssertionError("Health Performance pilot has not been assembled")
    proof_text = behavior_proof.read_text(encoding="utf-8")
    for marker in ("2.3 / 10", "9.1 / 10", "+6.8", "Remaining proof gap", "UNTESTED"):
        if marker not in proof_text:
            raise AssertionError(f"behavior proof is missing acceptance marker: {marker}")
    source_project = manifest.parent
    artifact_refs = json.loads(service_map.read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory(prefix="search-content-mastery-service-") as temp:
        temp_root = Path(temp)
        project = create_project(temp_root, "health-service", "health-performance.json")
        absolute_refs: dict[str, str] = {}
        for key, ref in artifact_refs.items():
            if key == "project_manifest":
                absolute_refs[key] = str(project / "manifest.json")
                continue
            candidate = Path(ref)
            absolute_refs[key] = str(candidate.resolve() if candidate.is_absolute() else (source_project / candidate).resolve())
        temp_map = temp_root / "service-artifacts.json"
        temp_map.write_text(json.dumps(absolute_refs, indent=2) + "\n", encoding="utf-8")
        result = run_runtime("service", "--project", str(project), "--artifacts", str(temp_map))
        if result.get("prototype_state") != "UNTESTED":
            raise AssertionError(f"pilot proof boundary regressed: {result}")
        receipt = json.loads(Path(result["receipt"]).read_text(encoding="utf-8"))
        if "The Angle Map remains the live offer canon." not in receipt["boundaries"]:
            raise AssertionError("service receipt does not preserve the live offer canon")
        return {
            "pilot": str(pilot.relative_to(ROOT)),
            "prototype_state": result["prototype_state"],
            "delivery_state": result["status"],
            "artifacts": len(receipt["artifacts"]),
            "behavior_proof": {"before": 2.3, "after": 9.1, "delta": 6.8},
        }


def verify_angle_map_application() -> dict[str, Any]:
    """Verify the real Angle Map prototype, not only synthetic fixtures."""
    try:
        from jsonschema import Draft202012Validator, FormatChecker
    except ImportError as exc:  # pragma: no cover - environment proof boundary
        raise AssertionError("jsonschema is required for the applied prototype verifier") from exc

    prototype = ANGLE_MAP_PROTOTYPE
    pack = prototype / "project-pack"
    required_artifacts = (
        "00-START-HERE.md",
        "architecture-verdict.md",
        "official-standards-crosswalk.md",
        "intake.md",
        "entity-context-pack.md",
        "baseline-audit.md",
        "opportunity-map.md",
        "owned-answer-page.md",
        "linkedin-answer-bridge.md",
        "proof-to-angle-media-brief.md",
        "experiment-plan.md",
        "behavior-proof.md",
        "service-delivery-receipt.md",
        "service-artifacts.json",
    )
    missing = [name for name in required_artifacts if not (prototype / name).is_file()]
    if missing:
        raise AssertionError(f"Angle Map prototype artifacts missing: {missing}")

    checker = FormatChecker()

    def validate(schema_name: str, path: Path) -> None:
        schema = json.loads((SCHEMA_ROOT / schema_name).read_text(encoding="utf-8"))
        record = json.loads(path.read_text(encoding="utf-8"))
        Draft202012Validator(schema, format_checker=checker).validate(record)

    manifest_path = pack / "manifest.json"
    validate("search-project-manifest.schema.json", manifest_path)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("proof_state") != "UNTESTED":
        raise AssertionError(f"Angle Map manifest self-promoted: {manifest.get('proof_state')}")

    brief_paths = sorted((pack / "briefs").glob("brief-*.json"))
    if len(brief_paths) != 3:
        raise AssertionError(f"expected three Angle Map briefs, found {len(brief_paths)}")
    target_queries = set()
    for path in brief_paths:
        validate("search-brief.schema.json", path)
        brief = json.loads(path.read_text(encoding="utf-8"))
        target_queries.add(brief["target_query"])
    expected_query = "how to create supplement marketing angles without overclaiming"
    if target_queries != {expected_query}:
        raise AssertionError(f"Angle Map briefs drifted across targets: {target_queries}")

    score_records = [
        (path, json.loads(path.read_text(encoding="utf-8")))
        for path in (pack / "scores").glob("score-*.json")
    ]

    def current_score(asset: Path) -> tuple[Path, dict[str, Any]]:
        asset_hash = sha256(asset)
        matches = [
            (path, record)
            for path, record in score_records
            if Path(str(record.get("content_ref", ""))).name == asset.name
            and record.get("content_hash") == asset_hash
        ]
        if not matches:
            raise AssertionError(f"no current score receipt matches {asset.name} and its hash")
        return max(matches, key=lambda item: item[1]["created_at"])

    assets = {
        "owned_answer_page": (prototype / "owned-answer-page.md", 9.43),
        "linkedin_answer_bridge": (prototype / "linkedin-answer-bridge.md", 8.83),
        "visual_brief": (prototype / "proof-to-angle-media-brief.md", 8.68),
    }
    current_scores: dict[str, tuple[Path, dict[str, Any]]] = {}
    for key, (asset, expected_score) in assets.items():
        path, record = current_score(asset)
        validate("content-score-receipt.schema.json", path)
        if record.get("proof_state") != "PREDICTED" or record.get("observed_outcomes"):
            raise AssertionError(f"{key} score collapsed predicted readiness into observed proof")
        if record.get("final_composite") != expected_score:
            raise AssertionError(f"{key} score drifted: {record.get('final_composite')} != {expected_score}")
        override = record.get("operator_override", {})
        if override.get("applied") or record.get("original_composite") != record.get("final_composite"):
            raise AssertionError(f"{key} contains an unapproved or lossy score override")
        current_scores[key] = (path, record)

    baseline_path, baseline = current_score(prototype / "before-answer-fixture.md")
    validate("content-score-receipt.schema.json", baseline_path)
    if baseline.get("final_composite") != 1.4:
        raise AssertionError(f"baseline score drifted: {baseline.get('final_composite')}")
    answer_score = current_scores["owned_answer_page"][1]["final_composite"]
    delta = round(answer_score - baseline["final_composite"], 2)
    if delta != 8.03:
        raise AssertionError(f"behavior-proof delta drifted: {delta}")

    service_paths = sorted((pack / "receipts").glob("service-*.json"))
    if not service_paths:
        raise AssertionError("Angle Map prototype has no service receipt")
    service_records = [(path, json.loads(path.read_text(encoding="utf-8"))) for path in service_paths]
    service_path, service = max(service_records, key=lambda item: item[1]["created_at"])
    validate("service-receipt.schema.json", service_path)
    if service.get("prototype_state") != "UNTESTED" or service.get("delivery_state") != "READY_FOR_INTERNAL_REVIEW":
        raise AssertionError(f"Angle Map service state drifted: {service}")
    answer_score_path = current_scores["owned_answer_page"][0]
    if Path(service["artifacts"]["evaluation_receipt"]).name != answer_score_path.name:
        raise AssertionError("latest service receipt points to a stale answer score")
    service_map = json.loads((prototype / "service-artifacts.json").read_text(encoding="utf-8"))
    if Path(service_map["evaluation_receipt"]).name != answer_score_path.name:
        raise AssertionError("service artifact map points to a stale answer score")

    ledger_sizes = {
        name: (pack / "ledgers" / name).stat().st_size
        for name in ("outcomes.jsonl", "recommendations.jsonl")
    }
    if any(ledger_sizes.values()):
        raise AssertionError(f"unobserved Angle Map prototype has market/learning rows: {ledger_sizes}")

    behavior_text = (prototype / "behavior-proof.md").read_text(encoding="utf-8")
    for marker in ("1.40 / 10", "9.43 / 10", "+8.03", "Remaining Proof Gap", "UNTESTED"):
        if marker not in behavior_text:
            raise AssertionError(f"Angle Map behavior proof is missing: {marker}")

    return {
        "prototype": str(prototype.relative_to(ROOT)),
        "artifacts": len(required_artifacts),
        "briefs": len(brief_paths),
        "target_query": expected_query,
        "scores": {key: value[1]["final_composite"] for key, value in current_scores.items()},
        "baseline": baseline["final_composite"],
        "score_delta": delta,
        "service_receipt": service_path.name,
        "delivery_state": service["delivery_state"],
        "prototype_state": service["prototype_state"],
        "outcome_rows": 0,
        "recommendation_rows": 0,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify Search Content Mastery runtime and contracts")
    parser.add_argument("--receipt", help="Optional JSON receipt path")
    parser.add_argument("--skip-pilot", action="store_true", help="Run core verification before the pilot exists")
    args = parser.parse_args()

    receipt = Receipt()
    receipt.check("system-files", verify_system_files)
    receipt.check("locked-eleven-source-corpus", verify_corpus)
    receipt.check("reused-source-hash-and-stream-check", verify_reused_sources)
    receipt.check("routing-first-with-negative-boundary", verify_routing)
    receipt.check("portable-runtime-imports-scoring-and-cold-starts", verify_runtime)
    receipt.check("claim-risk-negation-regression", verify_claim_risk_language)
    receipt.check("versioned-record-json-schemas", verify_record_schemas)
    receipt.check("protected-health-and-offer-files-unchanged", verify_protected_files)
    if not args.skip_pilot:
        receipt.check("health-performance-service-pilot", verify_service_pilot)
        receipt.check("angle-map-search-answer-application", verify_angle_map_application)

    payload = receipt.payload()
    if args.receipt:
        path = Path(args.receipt).expanduser().resolve()
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if receipt.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
