#!/usr/bin/env python3
"""Cold, deterministic verification for the Research OS parity companion."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

import deep_research_client as gemini_client
from research import research as programmatic_research

from research_bakeoff import (
    ABSOLUTE_CAP_USD,
    AUTHORIZATION_CAP_USD,
    ContractError,
    ResearchMission,
    SpendBlocked,
    SpendLedger,
    build_claim_audit,
    build_bakeoff,
    score_candidate,
    validate_import_report,
    write_json,
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def mission_payload() -> dict:
    return {
        "schema_version": "research-parity/v1",
        "mission_id": "cold-parity-fixture",
        "exact_question": "Which eligible offer deserves the next LinkedIn paid validation test?",
        "as_of_date": "2026-08-17",
        "depth": "deep",
        "candidates": [
            {"name": "15-Ad Creative Test Pack", "definition": "Five concepts and 15 statics."},
            {"name": "Lead-to-Proposal Proof Sprint", "definition": "One bounded workflow."},
        ],
        "parked_concepts": ["The Angle Map"],
        "authority_sources": ["local-authority.md"],
        "decision_criteria": ["ICP", "avatar", "paid pains", "positioning", "LinkedIn proof", "kill gate"],
        "proof_state": "UNTESTED / NO EVENT",
        "spending_policy": {
            "absolute_cap_usd": 10.0,
            "authorization_cap_usd": 8.0,
            "gemini_standard_calls_max": 1,
            "gemini_max_allowed": False,
            "paid_retries_allowed": False,
            "gemini_billing_verification": {
                "machine_verified_hard_ceiling": False,
                "verified_remaining_ceiling_usd": None,
            },
        },
    }


def report_text(promote_angle_map: bool = False) -> str:
    urls = [f"https://source{i}.example/report" for i in range(1, 16)]
    source_lines = "\n".join(f"- {url}" for url in urls)
    verdict = "Recommend The Angle Map as the primary winner." if promote_angle_map else (
        "Recommend the 15-Ad Creative Test Pack. The Angle Map remains parked supporting IP."
    )
    return f"""# Corrected PMF Deep Research

## Verdict
{verdict} Every exact offer remains UNTESTED / NO EVENT.

## ICP and avatar
Already-advertising health brand with approved claims.

## Paid pains and what buyers are paying for
Creative testing and bounded workflow implementation.

## Resisted framings and non-purchased promises
Buyers reject generic AI consulting and unsupported performance promises.

## Positioning and offer
Sell a bounded learning object.

## LinkedIn content, demonstration, and proof
Show the test map and claim boundary.

## Counterevidence, limitations, risk, and contradictions
Counterevidence one. Limitation two. Risk three. No market proof exists.

## Kill gate
Park after twenty qualified conversations with no deposit.

## Sources
{source_lines}
"""


def audit_payload() -> dict:
    return {
        "citation_claims_total": 10,
        "citation_claims_supported": 10,
        "high_risk_claims_total": 3,
        "high_risk_claims_supported": 3,
        "counterevidence_count": 3,
    }


def main() -> int:
    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        mission_path = root / "mission.json"
        write_json(mission_path, mission_payload())
        mission = ResearchMission.from_path(mission_path)
        require(mission.spending_policy["absolute_cap_usd"] == ABSOLUTE_CAP_USD, "absolute cap drift")
        require(mission.spending_policy["authorization_cap_usd"] == AUTHORIZATION_CAP_USD, "authorization cap drift")

        ledger = SpendLedger(root / "spend-ledger.json", mission)
        try:
            ledger.reserve_gemini_standard(mission.spending_policy["gemini_billing_verification"])
            raise AssertionError("unverified provider ceiling did not fail closed")
        except SpendBlocked:
            pass

        ledger.data["recorded_spend_usd"] = 7.99
        ledger.save()
        billing = {"machine_verified_hard_ceiling": True, "verified_remaining_ceiling_usd": 10.0}
        try:
            ledger.reserve_gemini_standard(billing)
            raise AssertionError("$7.99 exposure allowed another $3 reservation")
        except SpendBlocked:
            pass

        ledger.data["recorded_spend_usd"] = 0.0
        ledger.save()
        reservation = ledger.reserve_gemini_standard(billing)
        ledger.complete(reservation, "interaction-1", 3.0)
        try:
            ledger.complete(reservation, "interaction-1", 3.0)
            raise AssertionError("duplicate interaction was billed twice")
        except ContractError:
            pass
        require(ledger.data["recorded_spend_usd"] == 3.0, "idempotent completion changed spend")

        # The legacy Gemini usage file is a second accounting surface. Replay
        # of an already-collected interaction must be idempotent there too.
        original_usage_file = gemini_client.USAGE_FILE
        gemini_client.USAGE_FILE = root / "gemini-usage.json"
        try:
            client = gemini_client.DeepResearchClient(api_key="fixture-key")
            first = client._log_usage(
                query="fixture", agent="deep-research-pro-preview-12-2025",
                estimated_cost=3.0, duration_seconds=1.0,
                task_context="cold-parity-fixture", query_type="research",
                interaction_id="provider-interaction-1",
            )
            replay = client._log_usage(
                query="fixture", agent="deep-research-pro-preview-12-2025",
                estimated_cost=3.0, duration_seconds=1.0,
                task_context="cold-parity-fixture", query_type="research",
                interaction_id="provider-interaction-1",
            )
            usage = json.loads(gemini_client.USAGE_FILE.read_text(encoding="utf-8"))
            require(first is True and replay is False, "Gemini replay was not rejected as a duplicate")
            require(usage["usage"]["total_queries"] == 1, "Gemini replay incremented query count")
            require(usage["usage"]["estimated_cost_usd"] == 3.0, "Gemini replay doubled estimated spend")
        finally:
            gemini_client.USAGE_FILE = original_usage_file

        programmatic = programmatic_research("fixture", depth="deep", mode="gemini")
        require(str(programmatic.status).lower().endswith("failed"),
                "programmatic Gemini bypass did not fail closed")
        require("mission spend ledger" in " ".join(programmatic.warnings),
                "programmatic Gemini bypass did not name the required reservation")
        legacy_programmatic = programmatic_research("fixture", depth="deep", mode="legacy-accelerators")
        require(str(legacy_programmatic.status).lower().endswith("failed"),
                "legacy paid fan-out remained callable at the public research boundary")
        require("parked" in " ".join(legacy_programmatic.warnings),
                "legacy provider block did not explain the parked route")
        direct_client = gemini_client.DeepResearchClient(api_key="fixture-key")
        try:
            direct_client.research("fixture", mode="standard")
            raise AssertionError("direct Gemini client started without a mission reservation")
        except gemini_client.BudgetExhaustedError:
            pass
        try:
            direct_client.start_async("fixture", mode="standard")
            raise AssertionError("uncapped Gemini background start remained callable")
        except gemini_client.BudgetExhaustedError:
            pass

        good_report = root / "good.md"
        bad_report = root / "bad.md"
        good_report.write_text(report_text(False), encoding="utf-8")
        bad_report.write_text(report_text(True), encoding="utf-8")
        receipt = {"elapsed_seconds": 600, "estimated_cost_usd": 0.0}
        good = score_candidate(mission, "codex-native", good_report, receipt, audit_payload())
        bad = score_candidate(mission, "codex-native", bad_report, receipt, audit_payload())
        require(good["grade_complete"], "complete claim audit was not recognized")
        require(good["floors"]["parked_authority_preserved"], "valid parked concept failed")
        require(not bad["floors"]["parked_authority_preserved"], "Angle Map authority negative control passed")
        imported = validate_import_report(mission, good_report)
        require(imported["passed"] and imported["resolved_url_count"] == 15, "deep import lost citation URLs")
        unresolved = root / "unresolved.md"
        unresolved.write_text(report_text(False) + "\n[cite: 1]\n", encoding="utf-8")
        require(not validate_import_report(mission, unresolved)["passed"], "unresolved provider citations passed import")

        ledger_report = root / "ledger-report.md"
        ledger_report.write_text(
            """# Ledger fixture
<!-- CLAIM_LEDGER_START -->
| ID | Claim | Source URL | Support passage | Authority | Stance | Load bearing | High risk | Verdict |
|---|---|---|---|---|---|---|---|---|
| C01 | A checked pricing claim. | https://official.example/pricing | The opened pricing page names the exact package and amount. | seller_primary | support | yes | yes | VERIFIED |
| C02 | A buyer resistance signal. | https://forum.example/thread | The buyer describes a failed implementation and the missing controls. | public_buyer_voice | counter | yes | no | VERIFIED |
<!-- CLAIM_LEDGER_END -->
""",
            encoding="utf-8",
        )
        generated = build_claim_audit(ledger_report, root / "generated-audit")
        require(generated["passed"], f"report claim ledger did not normalize: {generated}")
        require(generated["citation_claims_total"] == 2, "claim normalization lost load-bearing rows")
        require(generated["counterevidence_count"] == 1, "counterevidence stance was not preserved")

        imported_out = root / "chatgpt-import"
        imported_cli = subprocess.run(
            [sys.executable, str(Path(__file__).resolve().parent / "research.py"), "run",
             "--mission", str(mission_path), "--mode", "benchmark-import",
             "--report", str(good_report), "--audit", str(root / "generated-audit" / "claim-audit.json"),
             "--out-dir", str(imported_out), "--depth", "deep",
             "--max-total-provider-spend", "10", "--json"],
            text=True, capture_output=True, check=False,
        )
        require(imported_cli.returncode == 0, f"ChatGPT benchmark import failed: {imported_cli.stdout} {imported_cli.stderr}")
        imported_candidate = json.loads((imported_out / "chatgpt-native.candidate.json").read_text(encoding="utf-8"))
        require(imported_candidate["provider"] == "chatgpt-native", "benchmark import lost provider identity")
        require(imported_candidate["import_validation"]["resolved_url_count"] == 15,
                "benchmark import lost source provenance")
        require(imported_candidate["receipt"]["estimated_cost_usd"] == 0.0,
                "subscription import was recorded as API spend")

        candidates = root / "candidates"
        candidates.mkdir()
        write_json(candidates / "codex-native.candidate.json", good)
        write_json(candidates / "gemini-blocked-receipt.json", {
            "provider": "gemini-native", "candidate_status": "NOT RUN",
            "interaction_started": False, "estimated_cost_usd": 0.0,
            "actual_cost_usd": 0.0, "stop_reason": "unbounded provider cost",
        })
        write_json(candidates / "chatgpt-import-status.json", {
            "provider": "chatgpt-native", "candidate_status": "EXPORT PENDING",
            "interaction_started": False, "estimated_cost_usd": 0.0,
            "actual_cost_usd": 0.0, "stop_reason": "subscription export pending",
        })
        results = build_bakeoff(mission_path, candidates, root / "bakeoff")
        require(results["verdict"].startswith("PARTIAL"), "missing provider candidates did not remain partial")
        require(results["spending"]["recorded_candidate_cost_usd"] == 0.0, "subscription/native candidate logged API spend")
        require(len(results["reference_status"]) == 2, "missing reference receipts were omitted from bakeoff")
        require(not any(row["interaction_started"] for row in results["reference_status"]),
                "unstarted provider references were reported as executed")

        native_out = root / "native-auto"
        auto = subprocess.run(
            [sys.executable, str(Path(__file__).resolve().parent / "research.py"), "run",
             "--mission", str(mission_path), "--mode", "auto", "--depth", "deep",
             "--max-total-provider-spend", "10", "--out-dir", str(native_out), "--json"],
            text=True, capture_output=True, check=False,
        )
        require(auto.returncode == 0, f"auto mode failed: {auto.stdout} {auto.stderr}")
        native_ledger = json.loads((native_out / "spend-ledger.json").read_text(encoding="utf-8"))
        require(native_ledger["provider_calls"] == [], "auto mode activated a provider call")

        no_depth = subprocess.run(
            [sys.executable, str(Path(__file__).resolve().parent / "research_quality_gate.py"),
             "validate", str(good_report), "--strict"],
            text=True, capture_output=True, check=False,
        )
        require(no_depth.returncode != 0 and "STRICT RESEARCH DEPTH UNSPECIFIED" in no_depth.stdout,
                "strict gate degraded to an undeclared depth floor")

    research_py = (Path(__file__).resolve().parent / "research.py").read_text(encoding="utf-8")
    require("--mode" in research_py and "codex-native" in research_py, "unified research entrypoint lacks explicit modes")
    require("legacy-accelerators" in research_py, "legacy provider path is not explicitly named")
    workflow = (Path(__file__).resolve().parents[1] / ".agent/workflows/deep-research-os.md").read_text(encoding="utf-8")
    require("benchmark-import" in workflow and "ensemble" in workflow, "Deep Research OS workflow lacks parity modes")

    print("RESEARCH PARITY VERIFICATION: PASS")
    print("- $10 absolute and $8 authorization caps are contract-locked")
    print("- unverified provider hard ceilings fail closed")
    print("- $7.99 exposure blocks another standard reservation")
    print("- duplicate Gemini interactions cannot double-count spend")
    print("- Gemini usage replays are idempotent across the legacy accounting surface")
    print("- direct/programmatic Gemini starts cannot bypass the mission spend ledger")
    print("- the public research boundary cannot activate the legacy paid-provider fan-out")
    print("- parked Angle Map promotion fails authority resolution")
    print("- report claim tables normalize into machine-readable audit files without hand-authored JSONL")
    print("- deep imports preserve resolved URLs and reject unresolved provider citation markers")
    print("- ChatGPT subscription exports normalize through the unified import route at $0 API spend")
    print("- auto mode creates no provider calls and strict validation requires an explicit depth")
    print("- incomplete three-way bakeoffs remain PARTIAL")
    print("- missing provider references retain blocked/pending status and zero-cost receipts")
    print("- unified entrypoint and Deep Research OS expose explicit modes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
