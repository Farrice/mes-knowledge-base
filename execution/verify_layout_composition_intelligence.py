#!/usr/bin/env python3
"""Verify the layout/composition intelligence integration with negative controls."""

from __future__ import annotations

import argparse
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "extractions/satori-graphics/expansion-2026-08-31-layout-composition-intelligence"
PRIMITIVE = ROOT / "semantic_libraries/antigravity/primitives/layout-composition-intelligence-contract.md"
WORKFLOW = ROOT / "skills/satori-graphics/workflows/27-composition-intelligence-brief.md"
PROMPT = ROOT / "skills/satori-graphics/references/prompts-v2/composition-intelligence-brief.md"
WRAPPER = ROOT / ".agent/workflows/satori-composition-brief.md"
SOURCE_COMMAND = ROOT / ".agents/skills/source-command-satori-composition-brief/SKILL.md"
CONSUMERS = (
    ROOT / ".agent/workflows/design-first-build.md",
    ROOT / ".agent/workflows/fantastic-studio.md",
    ROOT / "skills/jack-roberts-design-mastery/workflows/design-gauntlet.md",
    ROOT / "skills/kittl-graphic-design/workflows/professional-layout-execution.md",
    ROOT / "skills/kittl-graphic-design/workflows/ai-visual-asset-synthesis.md",
    ROOT / "skills/fantastic-posters/SKILL.md",
    ROOT / "skills/gpt-image-2-director/SKILL.md",
    ROOT / "skills/canvas-design/SKILL.md",
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.is_file() else ""


def checks(consumer_override: dict[Path, str] | None = None) -> list[tuple[str, bool]]:
    override = consumer_override or {}
    primitive = read(PRIMITIVE)
    workflow = read(WORKFLOW)
    prompt = read(PROMPT)
    skill = read(ROOT / "skills/satori-graphics/SKILL.md")
    movement = read(ROOT / "skills/satori-graphics/references/movement-flow-ladder.md")
    lift = read(ROOT / "skills/satori-graphics/references/lift-system-decision-criteria.md")
    required_package = (
        "metadata.json", "transcript.vtt", "transcript.txt", "video-context-ledger.md",
        "uncertainty-report.md", "analysis.md", "skill-system-contract.md", "frame-notes.md",
        "behavior-proof.md",
    )
    results = [
        ("source package", all((PACKAGE / name).is_file() for name in required_package)),
        ("visual exemplars", len(list((PACKAGE / "frames").glob("*.jpg"))) >= 12),
        ("source identity", "PKfZ1gnVJ44" in read(PACKAGE / "metadata.json")),
        ("behavior-changing proof", "Evidence Of Change" in read(PACKAGE / "behavior-proof.md") and "Negative Controls" in read(PACKAGE / "behavior-proof.md")),
        ("shadow contract", "SHADOW companion" in primitive and "Promotion Boundary" in primitive),
        ("activation and skip", "Activate When" in primitive and "Skip When" in primitive),
        ("composition packet", all(term in primitive for term in ("Leverage point", "Eye path", "Grid commitment", "Friction budget", "Transfer adaptations"))),
        ("source-faithful I", "I — Internal Rhythm" in primitive and "eye choreography is the mechanism" in primitive),
        ("four temporal beats", "Punch → Slow → Pull → Release" in workflow and "Punch → Slow → Pull → Release" in movement),
        ("workflow forged", all(term in workflow for term in ("Lock Leverage", "Choreograph Internal Rhythm", "Commit The Grid", "Budget Friction", "Design Transfer"))),
        ("prompt forged", "source_prompt: born-v2" in prompt and "Quality Gate" in prompt),
        ("command wrapper", "/satori-composition-brief" in read(WRAPPER)),
        ("source-command bridge", "source-command-satori-composition-brief" in read(SOURCE_COMMAND)),
        ("skill linked", "27-composition-intelligence-brief.md" in skill and "/satori-composition-brief" in skill),
        ("LIFT fidelity", "I — Internal Rhythm" in lift and "eye choreography" in lift.lower()),
    ]
    for path in CONSUMERS:
        content = override.get(path, read(path))
        results.append((f"consumer:{path.relative_to(ROOT)}", "/satori-composition-brief" in content))
    return results


def run_self_test() -> bool:
    baseline = checks()
    if not all(ok for _, ok in baseline):
        return False
    target = CONSUMERS[0]
    mutated = read(target).replace("/satori-composition-brief", "/missing-composition-route")
    negative = checks({target: mutated})
    failed = [name for name, ok in negative if not ok]
    return failed == [f"consumer:{target.relative_to(ROOT)}"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    results = checks()
    for name, ok in results:
        print(f"{'PASS' if ok else 'FAIL'} {name}")
    if args.self_test:
        ok = run_self_test()
        print(f"{'PASS' if ok else 'FAIL'} negative-control self-test")
        return 0 if ok else 1
    return 0 if all(ok for _, ok in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
