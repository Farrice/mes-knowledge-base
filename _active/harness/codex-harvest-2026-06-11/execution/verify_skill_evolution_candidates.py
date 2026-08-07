#!/usr/bin/env python3
"""Verify local-first Skill Evolution candidate helper behavior."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

import skill_evolution_candidates as candidates  # noqa: E402


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")


def make_skill(root: Path, name: str, workflows: list[str]) -> None:
    skill_dir = root / "skills" / name
    workflow_dir = skill_dir / "workflows"
    workflow_dir.mkdir(parents=True, exist_ok=True)
    (skill_dir / "SKILL.md").write_text(f"# {name}\n", encoding="utf-8")
    (skill_dir / "genius.md").write_text(f"# {name} Genius\n", encoding="utf-8")
    for workflow in workflows:
        (workflow_dir / f"{workflow}.md").write_text(f"# {workflow}\n", encoding="utf-8")


def fixture_root() -> Path:
    root = Path(tempfile.mkdtemp(prefix="skill-evolution-candidates-"))
    make_skill(root, "weak-skill", ["diagnostic"])
    make_skill(root, "sparse-skill", ["diagnostic"])
    make_skill(root, "empty-workflow-skill", [])

    write_jsonl(
        root / ".agent" / "performance-log.jsonl",
        [
            {
                "Local ID": "weak-1",
                "Output": "Weak output one",
                "Date": "2026-05-12",
                "Timestamp": "2026-05-12T01:00:00",
                "Skill": "weak-skill",
                "Workflow": "diagnostic",
                "Quality Score": 5.5,
                "Intent Alignment": 6,
                "Expert Standard": 5,
                "Adversarial Resilience": 6,
                "Status": "Keep",
                "Source Artifact": "execution/verify_fixture.py",
            },
            {
                "Local ID": "weak-2",
                "Output": "Weak output two",
                "Date": "2026-05-11",
                "Timestamp": "2026-05-11T01:00:00",
                "Skill": "weak-skill",
                "Workflow": "diagnostic",
                "Quality Score": 6.0,
                "Intent Alignment": 6,
                "Expert Standard": 6,
                "Adversarial Resilience": 5,
                "Status": "Keep",
                "Source Artifact": "execution/verify_fixture.py",
            },
            {
                "Local ID": "weak-3",
                "Output": "Weak output three",
                "Date": "2026-05-10",
                "Timestamp": "2026-05-10T01:00:00",
                "Skill": "weak-skill",
                "Workflow": "diagnostic",
                "Quality Score": 6.5,
                "Intent Alignment": 7,
                "Expert Standard": 6,
                "Adversarial Resilience": 6,
                "Status": "Keep",
                "Source Artifact": "execution/verify_fixture.py",
            },
            {
                "Local ID": "sparse-1",
                "Output": "Sparse output one",
                "Date": "2026-05-12",
                "Timestamp": "2026-05-12T02:00:00",
                "Skill": "sparse-skill",
                "Workflow": "diagnostic",
                "Quality Score": 8,
                "Intent Alignment": 8,
                "Expert Standard": 8,
                "Adversarial Resilience": 8,
                "Status": "Keep",
            },
            {
                "Local ID": "sparse-2",
                "Output": "Sparse output two",
                "Date": "2026-05-11",
                "Timestamp": "2026-05-11T02:00:00",
                "Skill": "sparse-skill",
                "Workflow": "diagnostic",
                "Quality Score": 8,
                "Intent Alignment": 8,
                "Expert Standard": 8,
                "Adversarial Resilience": 8,
                "Status": "Keep",
            },
            {
                "Local ID": "wrapper-1",
                "Output": "Command wrapper output",
                "Date": "2026-05-12",
                "Timestamp": "2026-05-12T03:00:00",
                "Skill": "source-command-wrapper-only",
                "Workflow": "wrapper-only",
                "Quality Score": 4,
                "Intent Alignment": 4,
                "Expert Standard": 4,
                "Adversarial Resilience": 4,
                "Status": "Keep",
            },
        ],
    )
    write_jsonl(
        root / ".agent" / "performance-log-inbox.jsonl",
        [
            {
                "draft_id": "draft_closeout",
                "title": "Session Closeout Intelligence",
                "workflow": "autopilot",
                "notes": "recurring closeout wrapper",
                "registration_source": "end-session",
            }
        ],
    )
    manifest = {"samples": [{"skill": "weak-skill"}]}
    manifest_path = root / "evolution_store" / "ground_truth" / "manifest.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    return root


def by_skill(rows: list[dict], skill: str) -> dict:
    match = [row for row in rows if row.get("skill") == skill]
    if not match:
        raise AssertionError(f"missing candidate for {skill}")
    return match[0]


def check_fixture_classification() -> str:
    root = fixture_root()
    snapshot = candidates.build_snapshot(root)

    weak = by_skill(snapshot["ready_candidates"], "weak-skill")
    if weak["state"] != "ready":
        raise AssertionError(f"weak-skill not ready: {weak}")
    if not weak["grounded"]:
        raise AssertionError("weak-skill should be marked grounded from manifest")

    sparse = by_skill(snapshot["watchlist"], "sparse-skill")
    if "needs 1 more" not in sparse["reason"]:
        raise AssertionError(f"sparse-skill reason wrong: {sparse}")

    wrapper = by_skill(snapshot["blocked"], "source-command-wrapper-only")
    if "missing root skill" not in wrapper["reason"] and "command-wrapper-only" not in wrapper["reason"]:
        raise AssertionError(f"wrapper-only reason wrong: {wrapper}")

    closeout = [row for row in snapshot["blocked"] if row.get("draft_id") == "draft_closeout"]
    if not closeout:
        raise AssertionError("closeout inbox draft was not blocked")
    if any(row.get("draft_id") == "draft_closeout" for row in snapshot["ready_candidates"] + snapshot["watchlist"]):
        raise AssertionError("closeout inbox draft became a candidate")
    return "fixture states ready/watchlist/blocked"


def check_duplicate_safe_write() -> str:
    root = fixture_root()
    snapshot = candidates.build_snapshot(root)
    candidates.write_outputs(snapshot, root)
    candidates.write_outputs(snapshot, root)
    saved = json.loads((root / "evolution_store" / "queue" / "skill_evolution_candidates.json").read_text(encoding="utf-8"))
    ids = [row["candidate_id"] for row in saved["ready_candidates"]]
    if len(ids) != len(set(ids)):
        raise AssertionError("duplicate candidate ids after repeated write")
    if saved["summary"]["ready"] != 1:
        raise AssertionError(f"unexpected ready count after repeated write: {saved['summary']}")
    return "snapshot writes are stable and duplicate-safe"


def check_live_cli_schema() -> str:
    result = subprocess.run(
        [sys.executable, "execution/skill_evolution_candidates.py", "scan", "--json"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(f"live scan failed:\n{result.stdout}\n{result.stderr}")
    snapshot = json.loads(result.stdout)
    required = {"generated_at", "summary", "ready_candidates", "watchlist", "blocked", "top_recommendation", "source_counts"}
    missing = sorted(required - set(snapshot))
    if missing:
        raise AssertionError(f"live scan missing schema keys: {missing}")
    return "live CLI emits required snapshot schema"


def main() -> int:
    checks = [check_fixture_classification, check_duplicate_safe_write, check_live_cli_schema]
    passed = [check() for check in checks]
    print("SKILL EVOLUTION CANDIDATE VERIFICATION PASS")
    for item in passed:
        print(f"- ok: {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
