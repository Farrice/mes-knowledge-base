#!/usr/bin/env python3
"""Verify the research-backed /buyer-trigger-os contract."""

from __future__ import annotations

import json
import importlib.util
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def fail(message: str) -> int:
    print(f"FAIL: {message}")
    return 1


def require_text(path: Path, needles: list[str]) -> list[str]:
    if not path.exists():
        return [f"missing file: {path}"]
    text = path.read_text()
    missing = [needle for needle in needles if needle not in text]
    return [f"{path}: missing {needle!r}" for needle in missing]


def run_json(cmd: list[str]) -> tuple[int, dict]:
    proc = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True, timeout=180)
    if proc.returncode not in (0, 2):
        return proc.returncode, {"error": proc.stderr or proc.stdout}
    try:
        return proc.returncode, json.loads(proc.stdout)
    except json.JSONDecodeError:
        return 1, {"error": f"non-json output: {proc.stdout[:400]}"}


class FakeApify:
    ACTORS = {"reddit": {"cost_per_result": 0.001}}

    def __init__(self, state: str, spent: float = 1.0, plan: float = 29.0):
        self.state = state
        self.usage = {"spent_dollars": spent, "plan_dollars": plan}
        self.ran = False

    def load_env(self) -> None:
        return None

    def load_usage(self) -> dict:
        return self.usage

    def budget_state(self, _usage: dict) -> str:
        return self.state

    def run_actor(self, _lane: str, _payload: dict, _limit: int) -> dict:
        self.ran = True
        return {
            "status": "ok",
            "fallback": False,
            "items": [{
                "url": "https://www.reddit.com/r/example/comments/apify_fixture",
                "title": "Apify fixture",
                "text": "Fixture Apify social listening item with source URL.",
            }],
        }


def load_runner_module():
    spec = importlib.util.spec_from_file_location(
        "buyer_trigger_research_contract_module",
        ROOT / "execution" / "buyer_trigger_research.py",
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load buyer_trigger_research.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    issues: list[str] = []
    issues.extend(require_text(
        ROOT / ".agent" / "workflows" / "buyer-trigger-os.md",
        [
            "Research-Trace Default",
            "execution/buyer_trigger_research.py",
            "--source-only",
            "--seed-url",
            "--seed-finding-json",
            "--apify execute",
            "Do not call `execution/research_router.py --provider auto`",
        ],
    ))
    issues.extend(require_text(
        ROOT / "skills" / "meg-heckman-buyer-trigger-os" / "SKILL.md",
        [
            "Research-Trace Default",
            "workflows/research-backed-trigger-run.md",
            "Refuse to fabricate current trends",
            "Apify",
        ],
    ))
    issues.extend(require_text(
        ROOT / "skills" / "meg-heckman-buyer-trigger-os" / "workflows" / "research-backed-trigger-run.md",
        [
            "Trigger Research Trace",
            "Research Receipt",
            "Source Ledger",
            "Insight Ledger",
            "--seed-url",
            "--seed-finding-json",
            "Do not use `execution/research_router.py --provider auto`",
        ],
    ))
    issues.extend(require_text(
        ROOT / "semantic_libraries" / "antigravity" / "primitives" / "buyer-trigger-design-psychology.md",
        ["Research-Backed Extension", "buyer_trigger_research.py", "Apify is optional"],
    ))

    py = sys.executable
    ok_code, ok_payload = run_json([
        py,
        "execution/buyer_trigger_research.py",
        "fixture apparel buyers",
        "--mode",
        "research",
        "--fixture",
        "ok",
        "--output-root",
        ".tmp/buyer-trigger-contract",
        "--json",
    ])
    if ok_code != 0 or ok_payload.get("status") != "REAL":
        issues.append(f"ok fixture should be REAL with enough source-backed evidence: {ok_payload}")
    else:
        report = ROOT / ok_payload["report"]
        if not report.exists():
            issues.append(f"ok fixture report missing: {report}")
        else:
            scan = subprocess.run(
                [py, "execution/grounding_guard.py", str(report), "--task-type", "Research", "--strict"],
                cwd=str(ROOT), capture_output=True, text=True, timeout=60,
            )
            if scan.returncode != 0:
                issues.append(f"grounding guard failed fixture report: {scan.stdout or scan.stderr}")

    empty_code, empty_payload = run_json([
        py,
        "execution/buyer_trigger_research.py",
        "fixture no-source buyers",
        "--mode",
        "research",
        "--fixture",
        "empty",
        "--output-root",
        ".tmp/buyer-trigger-contract",
        "--json",
    ])
    if empty_code != 2 or empty_payload.get("status") != "FAILED":
        issues.append(f"empty fixture should fail without fabricated evidence: code={empty_code}, payload={empty_payload}")
    else:
        report = ROOT / empty_payload["report"]
        if report.exists():
            text = report.read_text()
            if "No source-backed insight captured" not in text:
                issues.append("empty fixture report did not preserve no-source gap language")
            if "Research-backed research direction from E" in text:
                issues.append("empty fixture fabricated candidate rows")

    try:
        runner = load_runner_module()

        green = FakeApify("green")
        runner.load_apify_client = lambda: green
        preview_plan, preview_evidence = runner.maybe_run_apify(
            "fixture social listening",
            "preview",
            ["reddit"],
            10,
            0.25,
            1,
        )
        if preview_plan.executed or green.ran or preview_evidence:
            issues.append("Apify preview executed actor or returned evidence")
        if preview_plan.fallback:
            issues.append("Apify green preview should not fallback")

        red = FakeApify("red", spent=27.0)
        runner.load_apify_client = lambda: red
        red_plan, red_evidence = runner.maybe_run_apify(
            "fixture social listening",
            "execute",
            ["reddit"],
            10,
            0.25,
            1,
        )
        if not red_plan.fallback or red_plan.executed or red.ran or red_evidence:
            issues.append("Apify red budget did not hard-stop before actor execution")

        over_cap = FakeApify("green")
        runner.load_apify_client = lambda: over_cap
        cap_plan, cap_evidence = runner.maybe_run_apify(
            "fixture social listening",
            "execute",
            ["reddit"],
            1000,
            0.25,
            1,
        )
        if not cap_plan.fallback or cap_plan.executed or over_cap.ran or cap_evidence:
            issues.append("Apify over-cap estimate did not stop before actor execution")
    except Exception as exc:
        issues.append(f"Apify safety fixture failed: {type(exc).__name__}: {exc}")

    if issues:
        print("# Buyer Trigger Research Contract: FAIL")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("# Buyer Trigger Research Contract: PASS")
    print("- Runner exists and fixture behavior is source-gated.")
    print("- Workflow, skill, primitive, and hot launcher expose research-trace requirements.")
    print("- Failed research produces gap language instead of fabricated recommendations.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
