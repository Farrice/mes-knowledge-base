#!/usr/bin/env python3
"""Cold-start verifier for the heyDominik Instagram Growth OS."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import tempfile


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "heydominik-instagram-growth-os"
SOURCE = ROOT / "extractions" / "video-context" / "kY-t009NMWU"


def load_core():
    path = ROOT / "execution" / "instagram_growth_os.py"
    spec = importlib.util.spec_from_file_location("instagram_growth_os", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


def main() -> int:
    checks: list[tuple[str, bool, str]] = []
    core = load_core()
    spec_path = SKILL / "references" / "instagram-growth-os.skills.json"
    spec_result = core.validate_spec(spec_path)
    checks.append(("json_spec", spec_result["status"] == "PASS", json.dumps(spec_result)))

    invalid_payload = json.loads(spec_path.read_text(encoding="utf-8"))
    del invalid_payload["skills"][0]["success_metric"]
    with tempfile.TemporaryDirectory(prefix="instagram-growth-os-") as tmpdir:
        invalid_path = Path(tmpdir) / "invalid-spec.json"
        invalid_path.write_text(json.dumps(invalid_payload), encoding="utf-8")
        invalid_result = core.validate_spec(invalid_path)
    checks.append(("invalid_spec_rejected", invalid_result["status"] == "FAIL", json.dumps(invalid_result)))

    payload = json.loads(spec_path.read_text(encoding="utf-8"))
    for item in payload["skills"]:
        checks.append((f"prompt_{item['id']:02d}", (SKILL / item["system_prompt_path"]).is_file(), item["system_prompt_path"]))
        workflow = SKILL / "workflows" / f"{item['id']:02d}-{item['slug']}.md"
        checks.append((f"workflow_{item['id']:02d}", workflow.is_file(), str(workflow.relative_to(ROOT))))

    expected_files = [
        SKILL / "workflows" / "00-instagram-growth-os.md",
        ROOT / ".agent" / "workflows" / "instagram-growth-os.md",
        ROOT / ".claude" / "commands" / "instagram-growth-os.md",
        ROOT / ".agents" / "skills" / "source-command-instagram-growth-os" / "SKILL.md",
        SOURCE / "skill-system-contract.md",
        SOURCE / "behavior-proof.md",
    ]
    for path in expected_files:
        checks.append((f"file_{path.name}", path.is_file(), str(path.relative_to(ROOT))))

    corpus = "\n".join(path.read_text(encoding="utf-8") for path in [SKILL / "SKILL.md", SKILL / "workflows" / "00-instagram-growth-os.md", *sorted((SKILL / "references" / "prompts-v2").glob("*.md"))])
    for token in ["NO_EVENT", "UNVERIFIED", "shadowban", "explicit consent", "external write", "$20k+"]:
        checks.append((f"boundary_{token}", token.lower() in corpus.lower(), token))

    fixtures = json.loads((SOURCE / "fixtures" / "audit-cases.json").read_text(encoding="utf-8"))
    for record in fixtures:
        diagnosis = core.diagnose(record)
        actual = diagnosis["breaking_point"]
        checks.append((f"case_{record['case']}", actual == record["expected"], f"expected={record['expected']} actual={actual}"))
        if record["case"] == "Byron":
            checks.append(("byron_no_shadowban_claim", "shadowban" not in json.dumps(diagnosis).lower(), json.dumps(diagnosis)))

    zero_denominator = core.diagnose({
        "offer_clarity": "clear",
        "compliance_risk": False,
        "profile_state": "clear",
        "trust_state": "present",
        "monetization_state": "clear",
        "metrics": {"views": 0, "profile_visits": 5},
    })
    checks.append(("zero_denominator_is_null", zero_denominator["ratios"]["profile_visit_rate"] is None, json.dumps(zero_denominator)))

    failures = [{"check": name, "detail": detail} for name, passed, detail in checks if not passed]
    result = {"status": "PASS" if not failures else "FAIL", "checks": len(checks), "failures": failures}
    print(json.dumps(result, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
