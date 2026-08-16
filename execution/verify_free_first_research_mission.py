#!/usr/bin/env python3
"""Deterministic and negative-control checks for Free-First Research Mission."""

from __future__ import annotations

import ast
import json
import subprocess
import sys
import tempfile
from types import SimpleNamespace
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXEC = ROOT / "execution"
SCRIPT = EXEC / "free_first_research.py"
WORKFLOW = ROOT / ".agent" / "workflows" / "deep-research-os.md"
WRAPPER = ROOT / ".agents" / "skills" / "source-command-deep-research-os" / "SKILL.md"
CONTRACT = (
    ROOT
    / "semantic_libraries"
    / "antigravity"
    / "primitives"
    / "free-first-research-mission-contract.md"
)

sys.path.insert(0, str(EXEC))
import free_first_research as mission  # type: ignore  # noqa: E402
import autopilot_runtime_preflight as autopilot  # type: ignore  # noqa: E402
import outcome_recipes  # type: ignore  # noqa: E402
import routing_enforcer  # type: ignore  # noqa: E402


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def run(args: list[str], expected: int = 0) -> subprocess.CompletedProcess[str]:
    completed = subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    require(
        completed.returncode == expected,
        f"command exit {completed.returncode}, expected {expected}: {' '.join(args)}\n{completed.stdout}",
    )
    return completed


def plan(mission_dir: Path, depth: str = "standard") -> dict:
    completed = run(
        [
            sys.executable,
            str(SCRIPT),
            "plan",
            "--objective",
            "Determine whether current free research infrastructure can support decision-grade Codex research",
            "--decision",
            "Whether to make free-first the default Codex research path",
            "--downstream",
            "Deep Research OS",
            "--artifact",
            "Current research capability evidence brief",
            "--depth",
            depth,
            "--context",
            ".agent/workflows/deep-research-os.md",
            "--skill",
            "source-command-deep-research-os",
            "--output",
            str(mission_dir),
        ]
    )
    payload = json.loads(completed.stdout)
    require(payload["status"] == "PLANNED", "plan did not return PLANNED")
    require((mission_dir / "mission.json").exists(), "mission.json missing")
    require((mission_dir / "native-web-runbook.md").exists(), "native-web-runbook.md missing")
    return json.loads((mission_dir / "mission.json").read_text(encoding="utf-8"))


def valid_findings(manifest: dict) -> list[dict]:
    domains = (
        "docs.example.com",
        "research.example.org",
        "standards.example.net",
        "updates.example.edu",
    )
    retrieved = datetime.now(timezone.utc).isoformat()
    rows = []
    for index in range(8):
        query_id = "q-limitations" if index == 1 else "q-official-current"
        stance = "contradict" if index == 1 else "support"
        label = "CONTRADICTED" if index == 1 else "VERIFIED"
        rows.append(
            {
                "claim_id": f"c-{index + 1:03d}",
                "claim": f"Fixture claim {index + 1} is supported by an opened page.",
                "source_url": f"https://{domains[index % len(domains)]}/source-{index + 1}",
                "source_title": f"Fixture source {index + 1}",
                "source_class": "official" if index < 4 else "primary",
                "retrieval_method": "codex_native_web",
                "evidence_type": "page_read",
                "retrieved_at": retrieved,
                "published_at": "",
                "query_id": query_id,
                "claim_label": label,
                "claim_scope": "current_world",
                "stance": stance,
                "excerpt": f"Evidence excerpt {index + 1}.",
            }
        )
    return rows


def verify_happy_path(tmp: Path) -> list[str]:
    mission_dir = tmp / "happy"
    manifest = plan(mission_dir)
    require(not mission.verify_manifest(manifest), "valid manifest failed policy verification")
    rows = valid_findings(manifest)
    mission.write_jsonl(mission_dir / "native-web-findings.jsonl", rows)
    completed = run(
        [sys.executable, str(SCRIPT), "ingest", "--mission", str(mission_dir)]
    )
    receipt = json.loads(completed.stdout)
    require(receipt["status"] == "REAL", f"happy path not REAL: {receipt}")
    require(receipt["acceptable"] is True, "REAL receipt not acceptable")
    require(receipt["cost_usd"] == 0.0, "happy path logged non-zero cost")
    require(receipt["blocked_paths_executed"] == [], "blocked path reported as executed")
    require(
        receipt["quota_usage"]["estimated_tavily_api_credits"] == 0,
        "native-only fixture reported Tavily credit use",
    )
    require(receipt["metrics"]["native_web_full_reads"] == 8, "native web reads not counted")
    require(receipt["metrics"]["domains"] == 4, "domain diversity not counted")
    require(receipt["metrics"]["authoritative_claims"] == 7, "authoritative claims not counted")
    run(
        [
            sys.executable,
            str(SCRIPT),
            "verify",
            "--mission",
            str(mission_dir),
            "--require-receipt",
        ]
    )
    evidence = (mission_dir / "evidence-pack.md").read_text(encoding="utf-8")
    require("Current-world claims" in evidence, "evidence pack lost authority boundary")
    require("Accepted by operator: UNTESTED" in evidence, "value receipt overclaims acceptance")
    require("Used in work: NO EVENT" in evidence, "value receipt overclaims downstream use")
    run(
        [
            sys.executable,
            str(EXEC / "research_quality_gate.py"),
            "validate",
            str(mission_dir / "evidence-pack.md"),
            "--strict",
            "--depth",
            "standard",
            "--receipt",
        ]
    )
    depth_receipt = json.loads(
        (mission_dir / "evidence-pack.md.depth-receipt.json").read_text(encoding="utf-8")
    )
    require(depth_receipt["overall_pass"] is True, "shared research quality gate did not pass")
    require(depth_receipt["overall_score"] >= 90, "shared quality score retained a stale penalty")
    return [
        "cold local fixture compiles a mission packet and reaches REAL at the standard depth floor",
        "receipt preserves $0 cost, native-web provenance, and UNTESTED / NO EVENT value states",
        "shared quality receipt recomputes after explicit-depth override instead of retaining a stale penalty",
    ]


def verify_negative_controls(tmp: Path) -> list[str]:
    mission_dir = tmp / "negative"
    manifest = plan(mission_dir, depth="quick")
    base = valid_findings(manifest)[0]

    local_current = dict(base)
    local_current.update(
        {
            "source_class": "local_context",
            "retrieval_method": "local_context",
            "evidence_type": "local_note",
        }
    )
    errors = mission.validate_finding(mission.normalize_finding(local_current), manifest)
    require(
        any("cannot prove a current_world claim" in error for error in errors),
        f"local current-world substitution did not fail: {errors}",
    )

    stale_current = dict(base)
    stale_current["retrieved_at"] = "2020-01-01T00:00:00Z"
    errors = mission.validate_finding(mission.normalize_finding(stale_current), manifest)
    require(
        any("freshness window" in error for error in errors)
        and any("predates this mission" in error for error in errors),
        f"stale current-world evidence did not fail: {errors}",
    )

    snippet_verified = dict(base)
    snippet_verified.update(
        {"retrieval_method": "tavily_search", "evidence_type": "search_snippet"}
    )
    errors = mission.validate_finding(mission.normalize_finding(snippet_verified), manifest)
    require(any("cannot be VERIFIED" in error for error in errors), "VERIFIED snippet did not fail")

    one_domain = dict(base)
    one_domain["claim_label"] = "TRIANGULATED"
    mission.write_jsonl(mission_dir / "native-web-findings.jsonl", [one_domain])
    completed = run(
        [sys.executable, str(SCRIPT), "ingest", "--mission", str(mission_dir)],
        expected=2,
    )
    receipt = json.loads(completed.stdout)
    require(receipt["status"] == "FAILED", "invalid triangulation did not fail closed")
    quarantine = json.loads((mission_dir / "quarantine.json").read_text(encoding="utf-8"))
    require(
        any("TRIANGULATED" in " ".join(item["errors"]) for item in quarantine),
        "triangulation failure not quarantined",
    )

    tavily_dir = tmp / "tavily-order"
    plan(tavily_dir, depth="quick")
    completed = run(
        [sys.executable, str(SCRIPT), "tavily", "--mission", str(tavily_dir)],
        expected=2,
    )
    require("Native web must run first" in completed.stdout, "Tavily ran before native web")
    mission.write_jsonl(tavily_dir / "native-web-findings.jsonl", [{"attempt": "recorded"}])
    completed = run(
        [sys.executable, str(SCRIPT), "tavily", "--mission", str(tavily_dir)],
        expected=2,
    )
    require(
        "Refusing Tavily" in completed.stdout and "--confirm-zero-dollar-tavily" in completed.stdout,
        "Tavily did not fail closed on an unverified account billing boundary",
    )

    directional_dir = tmp / "directional-only"
    directional_manifest = plan(directional_dir, depth="quick")
    directional_rows = valid_findings(directional_manifest)
    for row in directional_rows:
        row["claim_label"] = "DIRECTIONAL"
    mission.write_jsonl(directional_dir / "native-web-findings.jsonl", directional_rows)
    completed = run(
        [sys.executable, str(SCRIPT), "ingest", "--mission", str(directional_dir)],
        expected=2,
    )
    receipt = json.loads(completed.stdout)
    require(receipt["status"] == "DEGRADED", "directional-only research reached REAL")
    require(
        any("authoritative claim floor" in failure for failure in receipt["gate_failures"]),
        "directional-only receipt did not name the authoritative-claim gap",
    )
    return [
        "local context is rejected as current-world proof",
        "stale evidence cannot be relabeled as a current mission retrieval",
        "search snippets cannot be promoted to VERIFIED",
        "single-domain TRIANGULATED claims fail closed",
        "directional-only sources cannot earn a REAL decision-grade receipt",
        "Tavily Search/Extract refuses to run before the native-web attempt",
        "Tavily Search/Extract refuses to run until the zero-dollar account boundary is confirmed",
    ]


def verify_rss_parser() -> list[str]:
    feed = b"""<?xml version='1.0' encoding='UTF-8'?>
    <feed xmlns='http://www.w3.org/2005/Atom'>
      <title>Official updates</title>
      <entry>
        <title>Release one</title>
        <link href='https://updates.example.org/releases/one'/>
        <updated>2026-08-16T12:00:00Z</updated>
        <summary>Release notes with current details.</summary>
      </entry>
    </feed>"""
    rows = mission.parse_feed(
        feed,
        "https://updates.example.org/feed.xml",
        "q-rss-changelog",
        10,
    )
    require(len(rows) == 1, f"RSS parser returned {len(rows)} rows")
    require(rows[0]["retrieval_method"] == "rss", "RSS method not preserved")
    require(rows[0]["published_at"], "RSS publication date not preserved")
    cleaned = mission.clean_research_text(
        "![avatar](https://images.example/avatar.png) [Official docs](https://docs.example/page) useful text"
    )
    require("http" not in cleaned and "useful text" in cleaned, "embedded links were not stripped")
    return [
        "public RSS/Atom parsing works on demand without creating a schedule",
        "embedded page-chrome URLs cannot inflate source-count receipts",
    ]


def verify_tavily_extract_env_bridge() -> list[str]:
    import native_floor  # type: ignore

    captured: dict = {}
    original_run = native_floor._subprocess.run
    original_load_env = native_floor.load_env_vars

    def fake_run(*args, **kwargs):
        captured.update(kwargs)
        return SimpleNamespace(
            returncode=0,
            stdout=json.dumps(
                {
                    "results": [
                        {
                            "url": "https://docs.example.com/source",
                            "title": "Fixture",
                            "raw_content": "Full extracted page content for deterministic verification.",
                        }
                    ]
                }
            ),
        )

    try:
        native_floor._subprocess.run = fake_run
        native_floor.load_env_vars = lambda: {"TAVILY_API_KEY": "fixture-key"}
        rows = native_floor.tavily_extract(["https://docs.example.com/source"])
    finally:
        native_floor._subprocess.run = original_run
        native_floor.load_env_vars = original_load_env

    require(len(rows) == 1, "Tavily Extract fixture did not parse")
    require(
        captured.get("env", {}).get("TAVILY_API_KEY") == "fixture-key",
        "Tavily Extract did not pass the workspace key to its child process",
    )
    return ["Tavily Extract receives the workspace key in a child-only environment without a global export"]


def verify_static_boundaries() -> list[str]:
    source = SCRIPT.read_text(encoding="utf-8")
    tree = ast.parse(source)
    imported: set[str] = set()
    called: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported.add(node.module or "")
            imported.update(alias.name for alias in node.names)
        elif isinstance(node, ast.Call):
            fn = node.func
            if isinstance(fn, ast.Name):
                called.add(fn.id)
            elif isinstance(fn, ast.Attribute):
                called.add(fn.attr)

    blocked_import_fragments = (
        "apify",
        "deep_research_client",
        "perplexity",
        "notebooklm",
        "subprocess",
        "threading",
        "concurrent",
    )
    for fragment in blocked_import_fragments:
        require(
            not any(fragment in name.lower() for name in imported),
            f"blocked import present: {fragment} in {sorted(imported)}",
        )
    require("tavily_research" not in called, "Tavily Research call present")
    require("_create_unverified_context" not in source, "RSS transport disables TLS verification")
    require("tavily_search" in imported and "tavily_extract" in imported, "Search/Extract legs missing")
    require('search_depth="basic"' in source, "free-first Tavily search is not pinned to basic depth")
    require("--confirm-zero-dollar-tavily" in source, "Tavily zero-dollar confirmation gate missing")

    floor_source = (EXEC / "native_floor.py").read_text(encoding="utf-8")
    require(
        '"--extract-depth", "basic"' in floor_source,
        "Tavily extract is not pinned to basic depth",
    )

    workflow = WORKFLOW.read_text(encoding="utf-8")
    wrapper = WRAPPER.read_text(encoding="utf-8")
    contract = CONTRACT.read_text(encoding="utf-8")
    for term in (
        "Codex Free-First Default",
        "python3 execution/free_first_research.py plan",
        "live external evidence retrieved in this run",
        "Tavily **Search and Extract**",
        "Local-only work",
        "cost_usd: 0.0",
    ):
        require(term in workflow, f"workflow missing free-first term: {term}")
    require("execution/research_router.py" not in workflow, "workflow still points to nonexistent research_router.py")
    require(
        workflow.index("Codex Free-First Default") < workflow.index("Provider-backed entrypoint"),
        "paid provider path appears before the Codex free-first default",
    )
    require("free-first-research-mission-contract.md" in wrapper, "hot wrapper does not load free-first contract")
    require("Authority Order" in contract and "Value Receipt" in contract, "semantic contract is incomplete")

    create_workflow = (ROOT / ".agent" / "workflows" / "create.md").read_text(encoding="utf-8")
    for stale_command in (
        "execution/apify_client.py",
        "mcp__perplexity-ask__perplexity_search",
        "python3 execution/research.py",
    ):
        require(stale_command not in create_workflow, f"/create still carries stale paid research command: {stale_command}")
    return [
        "runtime imports only basic-depth Tavily Search/Extract from the existing floor and discloses estimated credits; no paid, delegated, or background client is callable",
        "Deep Research OS, its hot wrapper, and /create route current research into the free-first companion contract",
    ]


def verify_autopilot_free_first_handoff() -> list[str]:
    prompts = (
        "Research the current market for AI lead generation tools.",
        "Do deep research on the current creator economy and cite live sources.",
        "What is happening in my niche right now? Include social listening.",
    )
    forbidden_gates = {"research-swarm", "parallel-research", "deep-research-gemini"}
    for query in prompts:
        payload = autopilot.build_preflight(query)
        require(
            payload["chosen_path"]["primary_route"] == "deep-research-os",
            f"Autopilot did not choose Free-First Deep Research for {query!r}: {payload['chosen_path']}",
        )
        require(payload["runtime_resolution"]["ready"], f"Autopilot route did not resolve: {payload['runtime_resolution']}")
        gates = set(payload["chosen_path"]["support_gates"])
        require(not gates & forbidden_gates, f"blocked research fan-out leaked into support gates: {sorted(gates & forbidden_gates)}")
        planned = payload["trace"]["verification_planned"]
        require(
            not any("research_router.py" in command for command in planned),
            f"dead research_router command survived: {planned}",
        )

    binding_ids = {
        match["binding_id"]
        for match in routing_enforcer.match_bindings(prompts[0])
    }
    require("unified_research" in binding_ids, f"generic current research did not match unified binding: {binding_ids}")

    unresolved: list[str] = []
    for recipe in outcome_recipes.RECIPES.values():
        for route in (recipe.primary_route, *recipe.support_gates):
            if not any(path.exists() for path in autopilot.route_target_candidates(route)):
                unresolved.append(f"{recipe.name}:{route}")
    require(not unresolved, f"Autopilot outcome recipes still point to nonexistent targets: {unresolved}")
    return [
        "natural-language current research, explicit deep research, and social listening all hand off to /deep-research-os",
        "Autopilot research support excludes swarms, parallel agents, and Gemini Deep Research",
        "every Autopilot outcome-recipe owner and support gate resolves to a callable local target",
    ]


def main() -> int:
    results: list[str] = []
    with tempfile.TemporaryDirectory(prefix="free-first-research-") as tmp_value:
        tmp = Path(tmp_value)
        results.extend(verify_happy_path(tmp))
        results.extend(verify_negative_controls(tmp))
    results.extend(verify_rss_parser())
    results.extend(verify_tavily_extract_env_bridge())
    results.extend(verify_static_boundaries())
    results.extend(verify_autopilot_free_first_handoff())
    print("FREE-FIRST RESEARCH MISSION VERIFICATION: PASS")
    for result in results:
        print(f"- {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
