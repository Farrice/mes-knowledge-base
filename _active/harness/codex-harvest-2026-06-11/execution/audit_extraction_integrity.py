#!/usr/bin/env python3
"""Audit May-June extraction integrity across source, proof, routing, and live surfaces."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

from verify_video_context_source_package import verify_package


ROOT = Path(__file__).resolve().parent.parent
EXTRACTIONS = ROOT / "extractions"
ROUTE_PROBE_TIMEOUT_SECONDS = 30
CONTROL_PLANE_TIMEOUT_SECONDS = 120


TIER_A: dict[str, dict[str, Any]] = {
    "extractions/video-context/PzVV4X37ihg": {
        "capability": "agentic-engineering-loop-contract",
        "query": "agentic engineering context engineering dependency safety small PR",
        "expected": "source-to-skill-system",
        "owner": "/source-to-skill-system",
    },
    "extractions/video-context/uf4fR3qcDkU": {
        "capability": "sam-parr-copywriting-mechanics",
        "query": "Sam Parr proof first copywriting mechanics",
        "expected": "sam-parr-copywriting-mechanics",
        "owner": "/source-to-skill-system",
    },
    "extractions/video-context/SzugliCQ3XY": {
        "capability": "low-cognitive-load-message-gate",
        "query": "copy feels smart but reader has to decode the offer",
        "expected": "low-cognitive-load-message-gate",
        "owner": "/source-to-skill-system",
    },
    "extractions/video-context/Zc4E_K48v48": {
        "capability": "attention-hijack-hooks",
        "query": "attention hijack hooks brandjacking newsjacking first 50 words",
        "expected": "attention-hijack-hooks",
        "owner": "/source-to-skill-system",
    },
    "extractions/video-context/TUdTU1pwoZ4": {
        "capability": "multi-company-operator",
        "query": "messy multi-offer founder portfolio stage gate delegation retail launch",
        "expected": "multi-company-operator",
        "owner": "/source-to-skill-system",
    },
    "extractions/kallaway-content-system": {
        "capability": "kallaway-trend-hook-engine",
        "query": "Sandcastles alternative social outlier hook trend radar",
        "expected": "kallaway-trend-hook-engine",
        "owner": "/source-to-skill-system",
    },
    "extractions/video-context/0eIN-Zdt39Q": {
        "capability": "kishotenketsu-contrast-storytelling",
        "query": "kishotenketsu contrast storytelling variable over villain",
        "expected": "kishotenketsu-contrast-storytelling",
        "owner": "/source-to-skill-system",
    },
    "extractions/video-context/DWDFRi5ONMI": {
        "capability": "oren-solo-ai-marketing-machine",
        "query": "one person marketing machine",
        "expected": "oren-solo-ai-marketing-machine",
        "owner": "/source-to-skill-system",
    },
    "extractions/oren-one-person-ai-marketing-machine": {
        "capability": "oren-solo-ai-marketing-machine",
        "query": "one person marketing machine",
        "expected": "oren-solo-ai-marketing-machine",
        "owner": "/source-to-skill-system",
    },
    "extractions/video-context/7MNa2YTPGs4": {
        "capability": "buyer-trigger-os",
        "query": "buyer trigger apparel purchase intent Meg Heckman",
        "expected": "buyer-trigger-os",
        "owner": "/source-to-skill-system",
    },
}


KEYWORDS = {
    "build_shape": (
        "build shape decision",
        "candidate shape",
        "summary only",
        "cold skill",
        "workflow bridge",
        "new command",
    ),
    "duplicate_route": (
        "duplicate",
        "existing owner",
        "existing skill",
        "rejected",
        "route fit",
        "not create a new",
        "hot command rejected",
        "companion",
    ),
    "practitioner": (
        "inputs",
        "outputs",
        "workflow",
        "step order",
        "operating method",
        "quality gate",
        "failure mode",
        "first",
        "use when",
    ),
    "behavior_proof": (
        "behavior proof",
        "before/after",
        "before-after",
        "proof lab",
        "behavior delta",
        "cold-start",
        "cold start",
        "applied scenario",
        "transformed artifact",
    ),
    "validation": (
        "validation",
        "verifier",
        "validate_skill.py",
        "codex_harness_check.py",
        "verify_",
        "pass",
    ),
    "uncertainty": (
        "uncertainty",
        "ocr unavailable",
        "visual",
        "source claim",
        "claim boundary",
        "transcript-only",
        "source boundary",
    ),
}


@dataclass
class ProbeResult:
    menu_first: str | None
    router_first: str | None
    governor_route: str | None
    ok: bool
    notes: list[str]


def parse_date(value: str) -> datetime:
    return datetime.strptime(value, "%Y-%m-%d")


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def read_text(path: Path, limit: int = 60000) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")[:limit]
    except OSError:
        return ""


def timeout_output_to_text(stdout: str | bytes | None, stderr: str | bytes | None) -> str:
    chunks: list[str] = []
    for value in (stdout, stderr):
        if not value:
            continue
        if isinstance(value, bytes):
            chunks.append(value.decode(errors="ignore"))
        else:
            chunks.append(value)
    return "".join(chunks)


def collect_roots(since: datetime, until_exclusive: datetime) -> list[Path]:
    roots: set[Path] = set()
    for file_path in EXTRACTIONS.rglob("*"):
        if not file_path.is_file():
            continue
        mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
        if not (since <= mtime < until_exclusive):
            continue
        parts = file_path.relative_to(ROOT).parts
        if len(parts) >= 3 and parts[0] == "extractions" and parts[1] == "video-context":
            roots.add(ROOT.joinpath(*parts[:3]))
        elif len(parts) >= 2 and parts[0] == "extractions":
            roots.add(ROOT.joinpath(*parts[:2]))
    return sorted(roots, key=lambda path: rel(path).lower())


def files_for(root: Path) -> list[Path]:
    return sorted([path for path in root.rglob("*") if path.is_file()])


def combined_text(root: Path) -> str:
    chunks: list[str] = []
    for path in files_for(root):
        if path.suffix.lower() not in {".md", ".txt", ".json"}:
            continue
        chunks.append(read_text(path, limit=16000))
    return "\n\n".join(chunks).lower()


def contains_any(text: str, terms: tuple[str, ...]) -> bool:
    return any(term in text for term in terms)


def is_video_package(root: Path) -> bool:
    return root.parent.name == "video-context"


def source_hygiene(root: Path) -> tuple[str, list[str]]:
    if is_video_package(root):
        ok, failures, notes = verify_package(root)
        return ("pass" if ok else "fail", failures + notes)

    names = {path.name.lower() for path in files_for(root)}
    has_source = any(
        name in names
        for name in (
            "transcript.txt",
            "source-map.md",
            "source-metadata.md",
            "extraction-brief.md",
            "extraction-report.md",
        )
    )
    if has_source:
        return "pass", ["Non-video extraction includes source or extraction surface."]
    return "unknown", ["No standard source package shape detected."]


def route_probe(info: dict[str, Any]) -> ProbeResult:
    query = info.get("query")
    expected = info.get("expected")
    if not query or not expected:
        return ProbeResult(None, None, None, False, ["No Tier A route probe configured."])

    cmd = [
        "python3",
        "-c",
        (
            "import sys; sys.path.insert(0, 'execution');"
            "import command_menu, workflow_router, routing_governor;"
            "q=%r;"
            "idx=command_menu.build_index();"
            "menu=[w.name for _,w in command_menu.search(idx,q,8)];"
            "router=[w['name'] for _,w in workflow_router.search_workflows(q,8)];"
            "d=routing_governor.evaluate(q,menu,router);"
            "import json; print(json.dumps({'menu':menu,'router':router,'governor':d.chosen_route}))"
        )
        % query,
    ]
    try:
        proc = subprocess.run(
            cmd,
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
            timeout=ROUTE_PROBE_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        return ProbeResult(
            None,
            None,
            None,
            False,
            [f"Route probe timed out after {ROUTE_PROBE_TIMEOUT_SECONDS}s."],
        )
    if proc.returncode != 0:
        return ProbeResult(None, None, None, False, [proc.stderr.strip() or proc.stdout.strip()])
    payload = json.loads(proc.stdout)
    menu_routes = payload.get("menu") or []
    router_routes = payload.get("router") or []
    menu_first = menu_routes[0] if menu_routes else None
    router_first = router_routes[0] if router_routes else None
    governor_route = payload.get("governor")
    ok = expected in {menu_first, router_first, governor_route}
    return ProbeResult(
        menu_first,
        router_first,
        governor_route,
        ok,
        [f"query={query}", f"expected=/{expected}"],
    )


def tier_info(root: Path) -> dict[str, Any]:
    root_rel = rel(root)
    if root_rel in TIER_A:
        return TIER_A[root_rel]
    for key, value in TIER_A.items():
        if root_rel.startswith(key + "/") or key.startswith(root_rel + "/"):
            return value
    return {}


def verdict_for(record: dict[str, Any]) -> tuple[str, str]:
    source = record["source_hygiene"]["status"]
    proof = record["behavior_proof"]["status"]
    exec_status = record["practitioner_executability"]["status"]
    firing = record["cold_start_firing"]["status"]
    tier = record["tier"]

    if source == "fail" and proof == "missing":
        return "redo from source", "Rebuild from source package after transcript/segment repair and proof lab."
    if tier == "A" and source == "fail":
        return "quarantine from arsenal", "Patch source package before trusting this capability as arsenal input."
    if proof == "missing" and tier == "A":
        return "patch proof/source", "Add behavior proof or cold-start fixture before calling deployed."
    if firing == "fail" and tier == "A":
        return "patch proof/source", "Fix natural-language route firing and rerun route probe."
    if exec_status == "weak" and tier == "A":
        return "patch proof/source", "Tighten practitioner workflow inputs, outputs, gates, and first-run path."
    if source in {"pass", "unknown"} and proof == "present" and exec_status == "pass" and firing in {"pass", "not_configured"}:
        return "keep", "No repair required beyond normal future validation."
    return "patch proof/source", "Review missing or weak audit dimensions and patch the smallest surface."


def audit_record(root: Path) -> dict[str, Any]:
    info = tier_info(root)
    text = combined_text(root)
    source_status, source_notes = source_hygiene(root)
    probe = route_probe(info) if info else ProbeResult(None, None, None, False, ["No Tier A route probe configured."])

    record: dict[str, Any] = {
        "extraction_id": rel(root),
        "source_path": rel(root),
        "linked_capability": info.get("capability", "unlinked"),
        "tier": "A" if info else "source-only",
        "build_shape": {
            "status": "present" if contains_any(text, KEYWORDS["build_shape"]) else "missing",
        },
        "source_hygiene": {
            "status": source_status,
            "notes": source_notes,
        },
        "uncertainty_boundary": {
            "status": "present" if contains_any(text, KEYWORDS["uncertainty"]) else "missing",
        },
        "duplicate_route_check": {
            "status": "present" if contains_any(text, KEYWORDS["duplicate_route"]) else "missing",
        },
        "practitioner_executability": {
            "status": "pass" if contains_any(text, KEYWORDS["practitioner"]) else "weak",
        },
        "behavior_proof": {
            "status": "present" if contains_any(text, KEYWORDS["behavior_proof"]) else "missing",
        },
        "cold_start_firing": {
            "status": "pass" if probe.ok else ("not_configured" if not info else "fail"),
            "menu_first": probe.menu_first,
            "workflow_first": probe.router_first,
            "governor_route": probe.governor_route,
            "notes": probe.notes,
        },
        "validation_coverage": {
            "status": "present" if contains_any(text, KEYWORDS["validation"]) else "missing",
        },
        "active_surface_risk": "review" if info else "low",
        "owner_route": info.get("owner", "/extraction-governor-agent"),
    }
    verdict, action = verdict_for(record)
    record["verdict"] = verdict
    record["repair_action"] = action
    return record


def control_plane_record() -> dict[str, Any]:
    try:
        proc = subprocess.run(
            ["python3", "execution/verify_system_control_plane.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
            timeout=CONTROL_PLANE_TIMEOUT_SECONDS,
        )
        output_lines = [line for line in (proc.stdout + proc.stderr).splitlines() if line.strip()]
    except subprocess.TimeoutExpired as exc:
        output = timeout_output_to_text(exc.stdout, exc.stderr)
        output_lines = [line for line in output.splitlines() if line.strip()]
        output_lines.append(f"Timed out after {CONTROL_PLANE_TIMEOUT_SECONDS}s.")
        proc = subprocess.CompletedProcess(
            ["python3", "execution/verify_system_control_plane.py"],
            returncode=124,
            stdout=output,
            stderr=f"Timed out after {CONTROL_PLANE_TIMEOUT_SECONDS}s.",
        )
    ok = proc.returncode == 0
    timed_out = proc.returncode == 124
    return {
        "extraction_id": "control-plane-routing:full-control-plane-audit",
        "source_path": "execution/control_plane_golden_queries.json",
        "linked_capability": "system-audit-routing",
        "tier": "A",
        "build_shape": {"status": "not_applicable"},
        "source_hygiene": {"status": "not_applicable", "notes": []},
        "uncertainty_boundary": {"status": "not_applicable"},
        "duplicate_route_check": {"status": "not_applicable"},
        "practitioner_executability": {"status": "not_applicable"},
        "behavior_proof": {"status": "not_applicable"},
        "cold_start_firing": {
            "status": "pass" if ok else "fail",
            "notes": output_lines[-8:] or [proc.stderr],
        },
        "validation_coverage": {"status": "present"},
        "active_surface_risk": "control-plane",
        "verdict": "keep" if ok else "patch proof/source",
        "owner_route": "/system-audit",
        "repair_action": (
            "Keep verifier passing."
            if ok
            else "Segment or speed up control-plane verifier duration; embedded audit timed out."
            if timed_out
            else "Fix golden query ordering so direct system-audit intent ranks /system-audit first."
        ),
    }


def summarize(records: list[dict[str, Any]]) -> dict[str, Any]:
    summary: dict[str, Any] = {
        "total_records": len(records),
        "by_verdict": {},
        "by_tier": {},
        "source_failures": [],
        "route_failures": [],
    }
    for record in records:
        summary["by_verdict"][record["verdict"]] = summary["by_verdict"].get(record["verdict"], 0) + 1
        summary["by_tier"][record["tier"]] = summary["by_tier"].get(record["tier"], 0) + 1
        if record["source_hygiene"]["status"] == "fail":
            summary["source_failures"].append(record["extraction_id"])
        if record["cold_start_firing"]["status"] == "fail":
            summary["route_failures"].append(record["extraction_id"])
    return summary


def write_markdown(out_path: Path, payload: dict[str, Any]) -> Path:
    md_path = out_path.with_suffix(".md")
    records = payload["records"]
    summary = payload["summary"]
    lines = [
        "# May-June Extraction Integrity Ledger",
        "",
        "## Summary",
        "",
        f"- Audit window: {payload['window']['since']} to {payload['window']['until']}",
        f"- Records reviewed: {summary['total_records']}",
        f"- Verdicts: {', '.join(f'{key}={value}' for key, value in sorted(summary['by_verdict'].items()))}",
        f"- Source failures: {', '.join(summary['source_failures']) or 'none'}",
        f"- Route/firing failures: {', '.join(summary['route_failures']) or 'none'}",
        "",
        "## Ledger",
        "",
        "| Extraction | Capability | Tier | Source | Proof | Firing | Verdict | Repair |",
        "|---|---|---:|---|---|---|---|---|",
    ]
    for record in records:
        lines.append(
            "| {extraction} | {capability} | {tier} | {source} | {proof} | {firing} | {verdict} | {repair} |".format(
                extraction=record["extraction_id"],
                capability=record["linked_capability"],
                tier=record["tier"],
                source=record["source_hygiene"]["status"],
                proof=record["behavior_proof"]["status"],
                firing=record["cold_start_firing"]["status"],
                verdict=record["verdict"],
                repair=record["repair_action"].replace("|", "/"),
            )
        )
    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- `quarantine from arsenal` means do not recommend or rely on the capability until the repair action passes; it does not mean delete files.",
            "- Tier A is the manually configured practitioner or harness-changing set. Source-only records get automated hygiene and proof checks only.",
            "- The JSON ledger beside this file contains full verifier notes and route probe details.",
        ]
    )
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    metadata = {
        "userFacingSurface": "rendered-conversation-document",
        "sourceRole": "persistence-copy",
        "externalExportRequested": False,
        "generatedBy": "execution/audit_extraction_integrity.py",
    }
    md_path.with_suffix(md_path.suffix + ".metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n",
        encoding="utf-8",
    )
    return md_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--since", required=True, help="Inclusive start date, YYYY-MM-DD")
    parser.add_argument("--until", required=True, help="Inclusive end date, YYYY-MM-DD")
    parser.add_argument("--out", required=True, help="JSON output path")
    args = parser.parse_args()

    since = parse_date(args.since)
    until = parse_date(args.until)
    until_exclusive = until + timedelta(days=1)
    out_path = (ROOT / args.out).resolve() if not Path(args.out).is_absolute() else Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    records = [audit_record(root) for root in collect_roots(since, until_exclusive)]
    records.append(control_plane_record())
    records = sorted(records, key=lambda item: item["extraction_id"])
    payload = {
        "generated_at": datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
        "window": {"since": args.since, "until": args.until},
        "summary": summarize(records),
        "records": records,
    }
    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    md_path = write_markdown(out_path, payload)
    print(f"Wrote JSON ledger: {rel(out_path)}")
    print(f"Wrote Markdown ledger: {rel(md_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
