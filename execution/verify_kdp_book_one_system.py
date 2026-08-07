#!/usr/bin/env python3
"""Deterministic cold-start and policy regression checks for Book One."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "execution" / "kdp_book_one.py"
RECEIPT = ROOT / "extractions" / "sean-dollwet-kdp-book-one-system" / "cold-start-receipt.json"
DETACHED_RECEIPT = ROOT / "extractions" / "sean-dollwet-kdp-book-one-system" / "detached-runtime-receipt.json"


def run(args: list[str], expect: int = 0) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        [sys.executable, str(CLI), *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if result.returncode != expect:
        raise AssertionError(f"expected {expect}, got {result.returncode}: {' '.join(args)}\n{result.stdout}")
    return result


def load(project: Path) -> dict:
    return json.loads((project / "06-system" / "book-one-state.json").read_text(encoding="utf-8"))


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def configure_ready_fixture(project: Path) -> Path:
    evidence = project / "02-research" / "decision-receipt.md"
    write(evidence, "# Decision Receipt\n\nFixture approval evidence.\n")
    write(project / "02-research" / "market-dossier.md", "# Market Dossier\n\nDated fixture evidence.\n")
    write(project / "02-research" / "claim-ledger.md", "# Claim Ledger\n\nAll claims verified or removed.\n")
    write(project / "02-research" / "rights-ledger.md", "# Rights Ledger\n\nAll asset rights pass.\n")
    write(
        project / "02-research" / "ai-asset-ledger.jsonl",
        json.dumps({
            "asset_id": "manuscript-v1",
            "creation_mode": "ai_generated",
            "kdp_disclosure_required": True,
            "disclosure_answer": "yes",
            "rights_basis": "operator-owned human edits and tool commercial terms receipt",
            "status": "PASS",
        }) + "\n" + json.dumps({
            "asset_id": "cover-v1",
            "creation_mode": "human",
            "kdp_disclosure_required": False,
            "disclosure_answer": "no",
            "rights_basis": "operator-owned fixture",
            "status": "PASS",
        }) + "\n",
    )
    write(project / "04-deliverables" / "manuscript.epub", "fixture epub")
    write(project / "05-assets" / "cover.jpg", "fixture cover")
    write(project / "04-deliverables" / "metadata.md", "# Metadata\n\nFixture title and subtitle.\n")
    write(project / "04-deliverables" / "review-plan.md", "# Review Plan\n\nNeutral optional reader invitation. No review is required or influenced.\n")
    write(project / "06-system" / "preview-receipt.json", '{"status":"PASS"}\n')

    run(["configure", "--project", str(project), "--title", "Fixture Book", "--subtitle", "A Useful Guide", "--risk-class", "low_risk"])
    for name, rel in {
        "market_dossier": "02-research/market-dossier.md",
        "claim_ledger": "02-research/claim-ledger.md",
        "ai_asset_ledger": "02-research/ai-asset-ledger.jsonl",
        "rights_ledger": "02-research/rights-ledger.md",
        "manuscript": "04-deliverables/manuscript.epub",
        "cover": "05-assets/cover.jpg",
        "metadata": "04-deliverables/metadata.md",
        "review_plan": "04-deliverables/review-plan.md",
        "preview_receipt": "06-system/preview-receipt.json",
    }.items():
        run(["artifact", "--project", str(project), "--name", name, "--path", rel, "--status", "READY"])
    for gate in (
        "demand", "sources", "manuscript", "cover", "metadata", "rights",
        "ai_disclosure", "originality", "claim_support", "review_integrity", "preview",
    ):
        run(["gate", "--project", str(project), "--name", gate, "--state", "PASS", "--evidence", str(evidence)])
    for checkpoint in ("niche", "outline", "gold_chapter", "cover"):
        run(["approve", "--project", str(project), "--checkpoint", checkpoint, "--evidence", str(evidence)])
    return evidence


def verify_state_machine(results: list[str]) -> None:
    with tempfile.TemporaryDirectory(prefix="kdp-book-one-") as temp:
        project = Path(temp) / "pilot"
        run(["init", "--project", str(project), "--pace", "rapid_7"])
        state = load(project)
        assert state["acquisition"] == "organic_only"
        assert state["kdp_select"] is False
        assert state["pace_profile"] == "rapid_7"
        first = run(["preflight", "--project", str(project), "--json", "--dry-run"], expect=1)
        assert json.loads(first.stdout)["verdict"] == "HOLD"
        assert not (project / "06-system" / "compliance-receipt.json").exists()
        run(["escalate", "--project", str(project)])
        assert load(project)["pace_profile"] == "launch_14"
        run(["escalate", "--project", str(project)])
        assert load(project)["pace_profile"] == "editorial_30"

        evidence = configure_ready_fixture(project)
        ready = run(["preflight", "--project", str(project), "--json"])
        assert json.loads(ready.stdout)["verdict"] == "READY_FOR_APPROVAL"
        run([
            "approve", "--project", str(project), "--checkpoint", "upload",
            "--evidence", str(evidence), "--explicit-upload-permission",
        ])
        submit = run(["preflight", "--project", str(project), "--json"])
        assert json.loads(submit.stdout)["verdict"] == "READY_TO_SUBMIT"

        run(["record", "--project", str(project), "--axis", "production", "--state", "DRAFTED", "--evidence", str(evidence)])
        skipped = run(["record", "--project", str(project), "--axis", "production", "--state", "LIVE", "--evidence", str(evidence)], expect=2)
        assert "invalid transition" in skipped.stdout
        results.append("state, pace, permission, and append-only transition fixture passed")


def verify_adversarial_policy(results: list[str]) -> None:
    with tempfile.TemporaryDirectory(prefix="kdp-book-one-policy-") as temp:
        project = Path(temp) / "pilot"
        run(["init", "--project", str(project)])
        configure_ready_fixture(project)

        write(
            project / "02-research" / "ai-asset-ledger.jsonl",
            json.dumps({
                "asset_id": "ai-cover",
                "creation_mode": "ai_generated",
                "kdp_disclosure_required": False,
                "disclosure_answer": "no",
                "rights_basis": "",
                "status": "HOLD",
            }) + "\n",
        )
        blocked = run(["preflight", "--project", str(project), "--json"], expect=1)
        receipt = json.loads(blocked.stdout)
        assert receipt["verdict"] == "BLOCKED"
        assert any("AI-generated asset" in item for item in receipt["blocking"])

        configure_ready_fixture(project)
        write(project / "04-deliverables" / "review-plan.md", "Free PDF in exchange for a review.\n")
        blocked = run(["preflight", "--project", str(project), "--json"], expect=1)
        assert json.loads(blocked.stdout)["verdict"] == "BLOCKED"

        write(project / "04-deliverables" / "review-plan.md", "Neutral optional invitation.\n")
        write(project / "04-deliverables" / "manuscript.pdf", "pdf only")
        run(["artifact", "--project", str(project), "--name", "manuscript", "--path", "04-deliverables/manuscript.pdf", "--status", "READY"])
        held = run(["preflight", "--project", str(project), "--json"], expect=1)
        assert json.loads(held.stdout)["verdict"] == "HOLD"
        results.append("undisclosed AI, missing rights, review exchange, and PDF-only fixtures held or blocked")


def verify_contract_surface(results: list[str]) -> None:
    required = {
        ROOT / "extractions/sean-dollwet-kdp-book-one-system/skill-system-contract.md": (
            "Source evidence", "Objective", "Components", "Step order", "Inputs", "Outputs",
            "Handoff summary", "Composition rule", "Human checkpoint", "Validation",
            "Behavior-changing proof", "Result surface", "Context policy", "Reuse hook",
        ),
        ROOT / "skills/sean-dollwet-kdp-publishing/workflows/00-book-one-pilot.md": (
            "Execution prompt:", "rapid_7", "launch_14", "editorial_30", "READY_FOR_APPROVAL",
        ),
        ROOT / "skills/sean-dollwet-kdp-publishing/references/kdp-policy-and-evidence-boundary.md": (
            "AI-generated", "review", "KDP Select", "NET_COLLECTED",
        ),
        ROOT / "extractions/sean-dollwet-kdp-book-one-system/behavior-proof.md": (
            "Input tested", "Weakness diagnosed", "Source mechanics used", "Output produced",
            "Behavior delta", "Validation run", "Remaining risk", "NO_EVENT", "UNTESTED",
        ),
        DETACHED_RECEIPT: (
            '"status": "RUNTIME_OBSERVED"', '"scope": "local_behavior_only"',
            '"market_proof": "NO_EVENT"', '"permission": "NO_PERMISSION"',
            '"publishing_action": "NOT_PERFORMED"',
        ),
    }
    for path, terms in required.items():
        if not path.exists():
            raise AssertionError(f"missing file: {path.relative_to(ROOT)}")
        text = path.read_text(encoding="utf-8", errors="ignore")
        for term in terms:
            if term not in text:
                raise AssertionError(f"missing {term!r} in {path.relative_to(ROOT)}")

    active_files = [
        ROOT / ".agent/workflows/kdp-engine.md",
        ROOT / "skills/sean-dollwet-kdp-publishing/SKILL.md",
        *sorted((ROOT / "skills/sean-dollwet-kdp-publishing/workflows").glob("*.md")),
        *sorted((ROOT / "skills/sean-dollwet-kdp-publishing/references/prompts-v2").glob("*.md")),
    ]
    forbidden = (
        "inside KDP rules",
        "copyright-humanize rule",
        "copyright unlock",
        "copyright-eligible manuscript",
        "in exchange for your honest feedback",
        "15-review gate",
        "title is irreversible",
    )
    for path in active_files:
        lowered = path.read_text(encoding="utf-8", errors="ignore").lower()
        for phrase in forbidden:
            if phrase in lowered:
                raise AssertionError(f"unsafe active instruction {phrase!r}: {path.relative_to(ROOT)}")
    results.append("contract fields and unsafe-instruction regression scan passed")


def verify_detached_runtime(results: list[str]) -> bool:
    payload = json.loads(DETACHED_RECEIPT.read_text(encoding="utf-8"))
    assert payload["independent_context"] is True
    assert payload["runtime_observed"] is True
    assert payload["status"] == "RUNTIME_OBSERVED"
    assert payload["scope"] == "local_behavior_only"
    assert payload["market_proof"] == "NO_EVENT"
    assert payload["permission"] == "NO_PERMISSION"
    assert payload["publishing_action"] == "NOT_PERFORMED"
    assert payload["route"]["owner"] == "kdp-engine"
    assert payload["route"]["command_menu_first"] == "kdp-engine"
    assert len(payload["tests"]) >= 6
    results.append("detached fresh-context probe observed local routing, dry-run HOLD, and permission behavior")
    return True


def verify_routing(results: list[str]) -> None:
    queries = (
        "start a KDP book from scratch without ads",
        "make an AI ebook that is not slop and prepare it for Amazon",
        "launch my first useful nonfiction book under a pen name",
    )
    for query in queries:
        outputs = []
        for command in (
            [sys.executable, "execution/command_menu.py", "search", query],
            [sys.executable, "execution/workflow_router.py", "search", query],
        ):
            completed = subprocess.run(command, cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
            if completed.returncode != 0:
                raise AssertionError(completed.stdout)
            outputs.append(completed.stdout)
        first_lines = "\n".join("\n".join(output.splitlines()[:6]) for output in outputs)
        if not any(route in first_lines for route in ("/kdp-engine", "/sean-dollwet-book-one-pilot")):
            raise AssertionError(f"cold query did not surface Book One route near the top: {query}\n{first_lines}")
    results.append("three cold KDP queries surfaced the Book One owner")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    results: list[str] = []
    verify_state_machine(results)
    verify_adversarial_policy(results)
    verify_contract_surface(results)
    verify_routing(results)
    runtime_observed = verify_detached_runtime(results)
    payload = {
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "status": "RUNTIME_OBSERVED" if runtime_observed else "ORCHESTRATOR_ATTESTED",
        "runtime_observed": runtime_observed,
        "runtime_scope": "local_behavior_only" if runtime_observed else None,
        "market_proof": "NO_EVENT",
        "checks": results,
    }
    if args.write_receipt:
        RECEIPT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("KDP BOOK ONE SYSTEM VERIFICATION PASS")
    for result in results:
        print(f"- {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
