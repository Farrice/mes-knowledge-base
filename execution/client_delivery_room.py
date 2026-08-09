#!/usr/bin/env python3
"""Build the private and client editions of an Angle Map delivery room.

This script owns deterministic mechanics only: project scaffolding, readiness
checks, release-language checks, rendering, portable export, ZIP creation, and
verification. Strategic judgment and evidence interpretation remain in the
`/client-delivery-room` workflow.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
EXECUTION = ROOT / "execution"
if str(EXECUTION) not in sys.path:
    sys.path.insert(0, str(EXECUTION))

import brief_export  # noqa: E402
import render_brief  # noqa: E402
import verify_brief_export  # noqa: E402


SCHEMA_VERSION = "client-delivery-room/v1"
RELEASE_SCHEMA_VERSION = "client-delivery-room-release/v1"
PROJECT_FILE = "client-room.json"
PLACEHOLDER_RE = re.compile(r"(?:\bTODO\b|\bTBD\b|\bHOLD\b|\[[A-Z][^\]]*\]|<[^>]+>)", re.I)
LOCAL_PATH_RE = re.compile(r"(?:^|[\"'=\s])/Users/[^/\s]+/|[A-Za-z]:\\\\")

DEFAULT_FORBIDDEN_CLIENT_TERMS = [
    "source-repo://",
    "file://",
    ".agent/",
    "_active/",
    "Antigravity",
    "God Agent",
    "Claude Code",
    "Codex",
    "worktree",
    "prompt-v2",
    "PRIVATE_CONTEXT",
]

REQUIRED_REVIEWS = (
    "editorial_review",
    "evidence_review",
    "privacy_review",
    "brand_review",
    "link_review",
)

REQUIRED_INTAKE_PATHS = (
    "project.client_name",
    "project.engagement",
    "decision.live_occasion",
    "decision.message_decision",
    "decision.deadline",
    "decision.final_decision_maker",
    "offer.product_or_offer",
    "offer.buyer_situation",
    "message.current_message",
    "message.team_uncertainty",
    "evidence.claim_boundaries",
    "delivery.final_audience",
    "delivery.reader_decision",
    "handling.mode",
)

DEFAULT_INTERNAL_HEADINGS = (
    "source",
    "customer truth",
    "problem-qualified",
    "angles",
    "message-market-fit",
    "unknown",
)

DEFAULT_CLIENT_HEADINGS = (
    "decision",
    "reviewed",
    "evidence",
    "three angles",
    "recommendation",
    "message-market-fit",
    "boundary",
)


class ProjectError(ValueError):
    """Raised when a project cannot be safely loaded or built."""


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    if not slug:
        raise ProjectError("client name must contain at least one letter or number")
    return slug


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_json(path: Path, label: str) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ProjectError(f"missing {label}: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ProjectError(f"invalid {label} JSON: {path}: {exc}") from exc


def inside(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def project_path(project_root: Path, raw: str, label: str) -> Path:
    value = str(raw or "").strip()
    if not value:
        raise ProjectError(f"project manifest is missing path: {label}")
    candidate = (project_root / value).resolve()
    if Path(value).is_absolute() or not inside(candidate, project_root.resolve()):
        raise ProjectError(f"{label} must be a safe project-relative path: {value!r}")
    return candidate


def nested(data: Any, dotted: str) -> Any:
    current = data
    for key in dotted.split("."):
        if not isinstance(current, dict) or key not in current:
            return None
        current = current[key]
    return current


def blank_or_placeholder(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return not value.strip() or bool(PLACEHOLDER_RE.search(value))
    if isinstance(value, (list, dict)):
        return not value
    return False


def flatten_strings(value: Any) -> list[str]:
    output: list[str] = []
    if isinstance(value, str):
        output.append(value)
    elif isinstance(value, dict):
        for key, item in value.items():
            output.extend(flatten_strings(key))
            output.extend(flatten_strings(item))
    elif isinstance(value, list):
        for item in value:
            output.extend(flatten_strings(item))
    return output


def section_headings(brief: dict) -> str:
    return "\n".join(str(section.get("heading") or "") for section in brief.get("sections", []))


def source_location_exists(project_root: Path, location: str) -> bool:
    value = str(location or "").strip()
    if value.startswith(("https://", "http://")):
        return True
    if not value:
        return False
    candidate = Path(value)
    if candidate.is_absolute():
        return False
    local = (project_root / candidate).resolve()
    if inside(local, project_root.resolve()) and local.exists():
        return True
    repo = (ROOT / candidate).resolve()
    return inside(repo, ROOT.resolve()) and repo.exists()


def load_project(project_root: Path) -> dict:
    root = project_root.expanduser().resolve()
    manifest = load_json(root / PROJECT_FILE, "project manifest")
    if manifest.get("schema_version") != SCHEMA_VERSION:
        raise ProjectError(f"unsupported project schema: {manifest.get('schema_version')!r}")
    paths = manifest.get("paths") or {}
    resolved = {
        key: project_path(root, paths.get(key), key)
        for key in ("intake", "source_inventory", "release_gate", "internal_brief", "client_brief")
    }
    return {
        "root": root,
        "manifest": manifest,
        "paths": resolved,
        "intake": load_json(resolved["intake"], "intake"),
        "sources": load_json(resolved["source_inventory"], "source inventory"),
        "release": load_json(resolved["release_gate"], "release gate"),
        "internal_brief": load_json(resolved["internal_brief"], "internal brief"),
        "client_brief": load_json(resolved["client_brief"], "client brief"),
    }


def validate_intake(project: dict, errors: list[str]) -> None:
    intake = project["intake"]
    if intake.get("schema_version") != SCHEMA_VERSION:
        errors.append("intake schema_version must be client-delivery-room/v1")
    for dotted in REQUIRED_INTAKE_PATHS:
        if blank_or_placeholder(nested(intake, dotted)):
            errors.append(f"intake field is missing or unresolved: {dotted}")

    mode = str(nested(intake, "handling.mode") or "").upper()
    confidential = bool(nested(intake, "project.confidential_material"))
    if mode == "NON_CONFIDENTIAL_DEMO":
        if confidential:
            errors.append("NON_CONFIDENTIAL_DEMO cannot declare confidential material")
        return
    if mode not in {"HUMAN_ONLY", "AI_ASSISTED_APPROVED"}:
        errors.append("handling.mode must be NON_CONFIDENTIAL_DEMO, HUMAN_ONLY, or AI_ASSISTED_APPROVED")
        return

    for key in (
        "transfer_channel", "authorized_access", "working_copy_location",
        "nda_state", "retention_period", "deletion_request_path", "reuse_state",
    ):
        value = nested(intake, f"handling.{key}")
        if blank_or_placeholder(value):
            errors.append(f"confidential handling field is unresolved: handling.{key}")
    if mode == "AI_ASSISTED_APPROVED":
        for key in ("approved_ai_tools", "approved_information_types", "written_ai_permission"):
            if blank_or_placeholder(nested(intake, f"handling.{key}")):
                errors.append(f"AI handling field is unresolved: handling.{key}")


def validate_sources(project: dict, errors: list[str], warnings: list[str]) -> None:
    inventory = project["sources"]
    if inventory.get("schema_version") != SCHEMA_VERSION:
        errors.append("source inventory schema_version must be client-delivery-room/v1")
    rows = inventory.get("sources")
    if not isinstance(rows, list) or not rows:
        errors.append("source inventory requires at least one source")
        return
    identifiers: set[str] = set()
    client_safe = 0
    for index, row in enumerate(rows, 1):
        prefix = f"source {index}"
        if not isinstance(row, dict):
            errors.append(f"{prefix} must be an object")
            continue
        source_id = str(row.get("id") or "").strip()
        if not source_id or source_id in identifiers:
            errors.append(f"{prefix} needs a unique id")
        identifiers.add(source_id)
        if row.get("evidence_type") not in {"FACT", "QUOTE", "CLAIM", "INFERENCE", "UNKNOWN"}:
            errors.append(f"{prefix} has invalid evidence_type")
        if row.get("visibility") not in {"CLIENT_SAFE", "INTERNAL_ONLY"}:
            errors.append(f"{prefix} visibility must be CLIENT_SAFE or INTERNAL_ONLY")
        elif row.get("visibility") == "CLIENT_SAFE":
            client_safe += 1
        if blank_or_placeholder(row.get("permission")):
            errors.append(f"{prefix} permission is unresolved")
        location = str(row.get("location") or "")
        if not source_location_exists(project["root"], location):
            errors.append(f"{prefix} location is missing, outside the project/repo, or not a public URL: {location!r}")
        if row.get("evidence_type") == "UNKNOWN" and not row.get("limitation"):
            warnings.append(f"{prefix} is UNKNOWN without a limitation note")
    if client_safe == 0:
        errors.append("source inventory needs at least one CLIENT_SAFE source for the client edition")


def validate_brief_shape(project: dict, errors: list[str]) -> None:
    manifest = project["manifest"]
    for label, brief, default_headings in (
        ("internal", project["internal_brief"], DEFAULT_INTERNAL_HEADINGS),
        ("client", project["client_brief"], DEFAULT_CLIENT_HEADINGS),
    ):
        slug = str(brief.get("slug") or "")
        if not re.fullmatch(r"[a-z0-9][a-z0-9._-]*", slug):
            errors.append(f"{label} brief needs a safe lowercase slug")
        if blank_or_placeholder(brief.get("title")):
            errors.append(f"{label} brief title is missing or unresolved")
        if not isinstance(brief.get("sections"), list) or not brief["sections"]:
            errors.append(f"{label} brief needs sections")
            continue
        required = (manifest.get("required_headings") or {}).get(label) or list(default_headings)
        headings = section_headings(brief).lower()
        for keyword in required:
            if str(keyword).lower() not in headings:
                errors.append(f"{label} brief is missing required heading signal: {keyword}")


def validate_release(project: dict, errors: list[str]) -> None:
    release = project["release"]
    if release.get("schema_version") != RELEASE_SCHEMA_VERSION:
        errors.append("release gate schema_version must be client-delivery-room-release/v1")
    reviews = release.get("reviews") or {}
    for key in REQUIRED_REVIEWS:
        if reviews.get(key) != "PASS":
            errors.append(f"release gate is not PASS: reviews.{key}")
    if release.get("permission_to_share") != "YES":
        errors.append("release gate permission_to_share must be YES")
    for key in ("reviewer", "reviewed_at"):
        if blank_or_placeholder(release.get(key)):
            errors.append(f"release gate is missing {key}")


def scan_client_payload(project: dict, errors: list[str]) -> None:
    brief = project["client_brief"]
    payload = json.dumps(brief, ensure_ascii=False)
    if PLACEHOLDER_RE.search(payload):
        errors.append("client brief contains an unresolved placeholder or HOLD")
    if LOCAL_PATH_RE.search(payload):
        errors.append("client brief contains an absolute local path")

    forbidden = list(DEFAULT_FORBIDDEN_CLIENT_TERMS)
    forbidden.extend(project["manifest"].get("forbidden_client_terms") or [])
    folded = payload.casefold()
    for term in dict.fromkeys(str(term) for term in forbidden if str(term).strip()):
        if term.casefold() in folded:
            errors.append(f"client brief contains forbidden outward term: {term}")

    def inspect(value: Any, key: str = "") -> None:
        if isinstance(value, dict):
            for child_key, child in value.items():
                inspect(child, str(child_key))
        elif isinstance(value, list):
            for child in value:
                inspect(child, key)
        elif isinstance(value, str) and key in {"url", "source_url", "href"}:
            if value.startswith("#"):
                return
            if not value.startswith(("https://", "http://")):
                errors.append(f"client brief {key} must be public http(s) or an in-page anchor: {value!r}")

    inspect(brief)


def validate_project(project_root: Path) -> dict:
    project = load_project(project_root)
    working_errors: list[str] = []
    warnings: list[str] = []
    validate_intake(project, working_errors)
    validate_sources(project, working_errors, warnings)
    validate_brief_shape(project, working_errors)

    release_errors: list[str] = []
    validate_release(project, release_errors)
    scan_client_payload(project, release_errors)
    return {
        "project": project,
        "working_errors": working_errors,
        "release_errors": release_errors,
        "warnings": warnings,
        "ready_for_working_room": not working_errors,
        "ready_for_client_export": not working_errors and not release_errors,
    }


def bundle_verification(path: Path) -> list[str]:
    tmp = None
    try:
        root, tmp = verify_brief_export.find_bundle(path)
        errors, _ = verify_brief_export.verify(root)
        return errors
    finally:
        if tmp is not None:
            tmp.cleanup()


def scan_rendered_client(bundle: Path, forbidden_terms: list[str]) -> list[str]:
    errors: list[str] = []
    html_files = sorted(bundle.rglob("*.html"))
    if not html_files:
        return ["client bundle contains no HTML files"]
    required_brand = ("#F3F3F0", "#FAFAF8", "#101010", "#3D5A94", "Helvetica Neue", "FARRICE CAIN")
    joined = "\n".join(path.read_text(encoding="utf-8", errors="replace") for path in html_files)
    for token in required_brand:
        if token not in joined:
            errors.append(f"client bundle is missing Premium Minimal brand token: {token}")
    if LOCAL_PATH_RE.search(joined):
        errors.append("client bundle contains an absolute local path")
    folded = joined.casefold()
    for term in dict.fromkeys(forbidden_terms):
        if term and term.casefold() in folded:
            errors.append(f"client bundle contains forbidden outward term: {term}")
    return errors


def exporter_args(*, slug: str, source_root: Path, output: Path, title: str, audience: str) -> argparse.Namespace:
    return argparse.Namespace(
        slugs=[slug], all=False, list=False, output=str(output), title=title,
        audience=audience, brief_root=str(source_root), zip=True,
        include_hidden=False, max_file_mb=brief_export.DEFAULT_MAX_FILE_MB,
        max_total_mb=brief_export.DEFAULT_MAX_TOTAL_MB,
    )


def build_release(project_root: Path, output: Path, working_only: bool = False) -> Path:
    report = validate_project(project_root)
    if report["working_errors"]:
        raise ProjectError("working room is not ready:\n- " + "\n- ".join(report["working_errors"]))
    if not working_only and report["release_errors"]:
        raise ProjectError("client export is blocked:\n- " + "\n- ".join(report["release_errors"]))

    project = report["project"]
    manifest = project["manifest"]
    target = output.expanduser().resolve()
    if target.exists():
        raise ProjectError(f"release output already exists: {target}")
    target.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix=f".{target.name}.tmp-", dir=target.parent))
    try:
        private_render_root = stage / ".private-render-source"
        private_paths = render_brief.write_brief(
            project["internal_brief"], out_root=private_render_root,
            share=False, src_json=project["paths"]["internal_brief"],
        )
        private_slug = project["internal_brief"]["slug"]
        private_output = stage / "private-working-room"
        private_title = f"{manifest['client_name']} — Private Working Room"
        brief_export.export_bundle(exporter_args(
            slug=private_slug, source_root=private_render_root, output=private_output,
            title=private_title, audience="private",
        ))

        bundles = [
            {"kind": "private", "folder": "private-working-room", "zip": "private-working-room.zip"}
        ]
        if not working_only:
            client_json = project["paths"]["client_brief"]
            client_source_root = client_json.parent.parent
            client_slug = project["client_brief"]["slug"]
            client_output = stage / "client-room"
            client_title = manifest.get("client_room_title") or f"{manifest['client_name']} — Client Room"
            brief_export.export_bundle(exporter_args(
                slug=client_slug, source_root=client_source_root, output=client_output,
                title=client_title, audience="share",
            ))
            bundles.append({"kind": "client", "folder": "client-room", "zip": "client-room.zip"})

        verification: list[dict] = []
        for bundle in bundles:
            for key in ("folder", "zip"):
                rel = bundle[key]
                errors = bundle_verification(stage / rel)
                verification.append({"path": rel, "status": "PASS" if not errors else "FAIL", "errors": errors})
                if errors:
                    raise ProjectError(f"portable verification failed for {rel}: " + "; ".join(errors))

        forbidden = list(DEFAULT_FORBIDDEN_CLIENT_TERMS)
        forbidden.extend(manifest.get("forbidden_client_terms") or [])
        if not working_only:
            rendered_errors = scan_rendered_client(stage / "client-room", forbidden)
            if rendered_errors:
                raise ProjectError("rendered client scan failed: " + "; ".join(rendered_errors))
            verification.append({"path": "client-room", "status": "PASS", "checks": [
                "Premium Minimal identity", "forbidden outward language", "absolute paths",
            ]})

        receipt = {
            "schema_version": RELEASE_SCHEMA_VERSION,
            "project_id": manifest["project_id"],
            "client_name": manifest["client_name"],
            "engagement": manifest["engagement"],
            "release_id": manifest["release_id"],
            "built_at": utc_now(),
            "mode": "WORKING_ONLY" if working_only else "PRIVATE_AND_CLIENT",
            "source_commit": brief_export.source_commit(),
            "proof_boundary": "Packaging, hashes, links, brand, and release-language checks passed. Strategic truth and market outcomes remain governed by the authored evidence states.",
            "release_gate": project["release"] if not working_only else {"status": "NOT APPLIED TO WORKING-ONLY BUILD"},
            "bundles": [
                {
                    **bundle,
                    "zip_sha256": brief_export.sha256_file(stage / bundle["zip"]),
                }
                for bundle in bundles
            ],
            "verification": verification,
            "warnings": report["warnings"],
        }
        write_json(stage / "release-receipt.json", receipt)
        if private_render_root.exists():
            shutil.rmtree(private_render_root)
        os.replace(stage, target)
        stage = None
        return target
    finally:
        if stage is not None and stage.exists():
            shutil.rmtree(stage)


def verify_release(release_dir: Path) -> list[str]:
    root = release_dir.expanduser().resolve()
    receipt = load_json(root / "release-receipt.json", "release receipt")
    if receipt.get("schema_version") != RELEASE_SCHEMA_VERSION:
        return [f"unsupported release receipt schema: {receipt.get('schema_version')!r}"]
    errors: list[str] = []
    for bundle in receipt.get("bundles", []):
        for key in ("folder", "zip"):
            rel = str(bundle.get(key) or "")
            path = (root / rel).resolve()
            if not rel or not inside(path, root):
                errors.append(f"unsafe receipt path: {rel!r}")
                continue
            if not path.exists():
                errors.append(f"missing release artifact: {rel}")
                continue
            errors.extend(f"{rel}: {error}" for error in bundle_verification(path))
        zip_path = root / str(bundle.get("zip") or "")
        if zip_path.is_file() and brief_export.sha256_file(zip_path) != bundle.get("zip_sha256"):
            errors.append(f"ZIP hash differs from release receipt: {zip_path.name}")
    return errors


def starter_brief(slug: str, client: str, client_edition: bool) -> dict:
    if client_edition:
        headings = (
            "the decision", "what we reviewed", "what the evidence supports",
            "the three angles", "our recommendation", "the message-market-fit test",
            "evidence boundary",
        )
        sections = [
            {"kind": "summary", "heading": headings[0], "kicker": "EXECUTIVE ANSWER", "body": "[WRITE THE CLIENT DECISION]"},
            {"kind": "stats", "heading": headings[1], "items": [{"value": "[COUNT]", "label": "CLIENT-SAFE SOURCES"}]},
            {"kind": "evidence", "heading": headings[2], "rows": []},
            {"kind": "decision", "heading": headings[3], "items": []},
            {"kind": "decision", "heading": headings[4], "items": []},
            {"kind": "deploy", "heading": headings[5], "blocks": []},
            {"kind": "caveats", "heading": headings[6], "body": "[WRITE THE EVIDENCE AND CLAIM BOUNDARY]"},
        ]
        chip = f"{client.upper()} · ANGLE MAP"
        title = "the message decision *room*"
        dek = "[WRITE ONE CLIENT-RELEVANT SENTENCE]"
    else:
        headings = (
            "source coverage", "customer truth dossier", "problem-qualified segment",
            "the three angles", "message-market-fit test", "unknowns and release boundary",
        )
        sections = [
            {"kind": "stats", "heading": headings[0], "items": []},
            {"kind": "evidence", "heading": headings[1], "rows": []},
            {"kind": "decision", "heading": headings[2], "items": []},
            {"kind": "decision", "heading": headings[3], "items": []},
            {"kind": "deploy", "heading": headings[4], "blocks": []},
            {"kind": "caveats", "heading": headings[5], "body": "[PRESERVE UNKNOWN, CONFLICTS, AND RELEASE STATE]"},
        ]
        chip = f"{client.upper()} · PRIVATE WORKING ROOM"
        title = "the private *decision record*"
        dek = "[WRITE THE CANDID INTERNAL READ]"
    return {
        "slug": slug,
        "chip": chip,
        "title": title,
        "dek": dek,
        "window": "[DATE RANGE]",
        "lens": "customer truth · problem qualification · message-market fit",
        "sources": "[SOURCE COVERAGE]",
        "compiled": "[DATE]",
        "category": f"client: {client}",
        "priority": 1,
        "sections": sections,
        "ledger": [],
        "context": [],
    }


def init_project(project_dir: Path, client: str) -> Path:
    root = project_dir.expanduser().resolve()
    if root.exists():
        raise ProjectError(f"project directory already exists: {root}")
    root.mkdir(parents=True)
    slug = slugify(client)
    project_id = f"{slug}-angle-map"
    internal_slug = f"{project_id}-working"
    client_slug = f"{project_id}-client"
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "project_id": project_id,
        "client_name": client,
        "engagement": "The Angle Map + Message-Market-Fit Intelligence",
        "release_id": "v1",
        "client_room_title": f"{client} — Message Decision Room",
        "paths": {
            "intake": "intake.json",
            "source_inventory": "source-inventory.json",
            "release_gate": "release-gate.json",
            "internal_brief": f"briefs/private/{internal_slug}/{internal_slug}-brief.json",
            "client_brief": f"briefs/client/{client_slug}/{client_slug}-brief.json",
        },
        "forbidden_client_terms": [],
    }
    intake = {
        "schema_version": SCHEMA_VERSION,
        "project": {"client_name": client, "engagement": manifest["engagement"], "confidential_material": True},
        "decision": {
            "live_occasion": "[LIVE OCCASION]", "message_decision": "[ONE MESSAGE DECISION]",
            "deadline": "[DATE]", "final_decision_maker": "[NAME AND ROLE]",
        },
        "offer": {"product_or_offer": "[PRODUCT OR OFFER]", "buyer_situation": "[BUYER SITUATION]"},
        "message": {"current_message": "[CURRENT MESSAGE]", "team_uncertainty": "[UNRESOLVED CHOICE]", "prior_attempts": "UNKNOWN"},
        "evidence": {"claim_boundaries": "[APPROVED, REVIEW, AND OUT-OF-SCOPE BOUNDARIES]"},
        "delivery": {"final_audience": "[READERS]", "reader_decision": "[WHAT THEY MUST DECIDE]"},
        "handling": {
            "mode": "HOLD", "transfer_channel": "HOLD", "authorized_access": [],
            "working_copy_location": "HOLD", "nda_state": "HOLD", "retention_period": "HOLD",
            "deletion_request_path": "HOLD", "reuse_state": "Private only",
            "approved_ai_tools": [], "approved_information_types": [], "written_ai_permission": "HOLD",
        },
    }
    sources = {"schema_version": SCHEMA_VERSION, "sources": []}
    release = {
        "schema_version": RELEASE_SCHEMA_VERSION,
        "reviews": {key: "HOLD" for key in REQUIRED_REVIEWS},
        "permission_to_share": "NO",
        "reviewer": "[NAME]",
        "reviewed_at": "[ISO DATE/TIME]",
        "notes": "Client export remains blocked until every review passes.",
    }
    write_json(root / PROJECT_FILE, manifest)
    write_json(root / "intake.json", intake)
    write_json(root / "source-inventory.json", sources)
    write_json(root / "release-gate.json", release)
    write_json(root / manifest["paths"]["internal_brief"], starter_brief(internal_slug, client, False))
    write_json(root / manifest["paths"]["client_brief"], starter_brief(client_slug, client, True))
    shutil.copy2(ROOT / "templates" / "client-delivery-room" / "intake-form.md", root / "INTAKE-FORM.md")
    (root / "START-HERE.md").write_text(
        f"# {client}: Client Delivery Room\n\n"
        "1. Complete `intake.json` and place permitted files in this project.\n"
        "2. Record every source in `source-inventory.json`.\n"
        "3. Run the `/client-delivery-room` workflow to author the private and client brief JSON files.\n"
        "4. Complete `release-gate.json` only after human review.\n"
        "5. Run `python3 execution/client_delivery_room.py build <project-dir> --output <new-release-dir>`.\n",
        encoding="utf-8",
    )
    return root


def print_check(report: dict) -> None:
    print("CLIENT DELIVERY ROOM CHECK")
    print(f"- working room: {'READY' if report['ready_for_working_room'] else 'HOLD'}")
    print(f"- client export: {'READY' if report['ready_for_client_export'] else 'HOLD'}")
    for label, rows in (("working", report["working_errors"]), ("release", report["release_errors"]), ("warning", report["warnings"])):
        for row in rows:
            print(f"- {label}: {row}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build and verify a dual-edition Angle Map client room.")
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init", help="create a new guarded client-room project")
    init.add_argument("--project-dir", required=True)
    init.add_argument("--client", required=True)

    check = sub.add_parser("check", help="check intake, evidence, brief, and release readiness")
    check.add_argument("project_dir")
    check.add_argument("--release", action="store_true", help="exit nonzero unless the client export is ready")

    build = sub.add_parser("build", help="build verified private and client bundles")
    build.add_argument("project_dir")
    build.add_argument("--output", required=True, help="new release directory; existing paths are refused")
    build.add_argument("--working-only", action="store_true", help="build only the private room before release approval")

    verify = sub.add_parser("verify", help="re-verify a built release and its ZIP hashes")
    verify.add_argument("release_dir")

    args = parser.parse_args()
    try:
        if args.command == "init":
            path = init_project(Path(args.project_dir), args.client)
            print(f"[client_delivery_room] INIT → {path}")
            print(f"[client_delivery_room] NEXT → complete {path / 'intake.json'}")
            return 0
        if args.command == "check":
            report = validate_project(Path(args.project_dir))
            print_check(report)
            ready = report["ready_for_client_export"] if args.release else report["ready_for_working_room"]
            return 0 if ready else 1
        if args.command == "build":
            path = build_release(Path(args.project_dir), Path(args.output), args.working_only)
            print(f"[client_delivery_room] BUILD PASS → {path}")
            print(f"[client_delivery_room] VERIFY → python3 execution/client_delivery_room.py verify {path}")
            return 0
        if args.command == "verify":
            errors = verify_release(Path(args.release_dir))
            if errors:
                print("CLIENT DELIVERY ROOM VERIFICATION FAIL")
                for error in errors:
                    print(f"- {error}")
                return 1
            print("CLIENT DELIVERY ROOM VERIFICATION PASS")
            print(f"- release: {Path(args.release_dir).expanduser().resolve()}")
            print("- bundle hashes, local links, and portable paths resolve")
            return 0
    except ProjectError as exc:
        print(f"[client_delivery_room] ERROR — {exc}", file=sys.stderr)
        return 1
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
