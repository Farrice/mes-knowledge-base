#!/usr/bin/env python3
"""Deterministic completion proof for the reconciled Kallaway skill system.

This verifier checks the connected build rather than one directory in isolation:
source evidence, owning skills, workflow and prompt manifests, command bridges,
the literal topic-mining alias, signal-pack v2, behavior proof, and offline
sabotage suites.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    RESULTS.append((name, bool(condition), detail))


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def run(name: str, command: list[str], expected: str) -> None:
    completed = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    output = "\n".join(part for part in (completed.stdout, completed.stderr) if part).strip()
    tail = output.splitlines()[-1] if output else f"exit={completed.returncode}"
    check(name, completed.returncode == 0 and expected in output, tail)


source_files = (
    "extractions/video-context/GmIn1W9V8Rs/metadata.json",
    "extractions/video-context/GmIn1W9V8Rs/transcript.txt",
    "extractions/video-context/GmIn1W9V8Rs/transcript_segments.json",
    "extractions/video-context/GmIn1W9V8Rs/video-context-ledger.md",
    "extractions/video-context/GmIn1W9V8Rs/frame-notes.md",
    "extractions/video-context/GmIn1W9V8Rs/uncertainty-report.md",
    "extractions/video-context/GmIn1W9V8Rs/analysis.md",
    "extractions/video-context/GmIn1W9V8Rs/skill-system-contract.md",
    "extractions/video-context/GmIn1W9V8Rs/proof/cold-start-fixture.md",
    "extractions/video-context/GmIn1W9V8Rs/proof/cold-start-output.md",
)
missing_source = [path for path in source_files if not (ROOT / path).is_file()]
check("source package is decision-complete", not missing_source, ", ".join(missing_source))

analysis = read("extractions/video-context/GmIn1W9V8Rs/analysis.md")
check(
    "mastery extraction carries tacit mechanics and implementation",
    all(token in analysis for token in ("## Hidden Knowledge Revealed", "## Implementation Pathway", "## Transcendence Opportunities")),
)

contract = read("extractions/video-context/GmIn1W9V8Rs/skill-system-contract.md")
contract_fields = (
    "| Source evidence |",
    "| Objective |",
    "| Components |",
    "| Step order |",
    "| Handoff summary |",
    "| Human checkpoint |",
    "| Validation |",
    "| Behavior-changing proof |",
    "| Result surface |",
    "| Context policy |",
    "| Reuse hook |",
)
check("skill-system contract is complete", all(field in contract for field in contract_fields))

skills = {
    "kallaway-ai-content-engine": (5, 5),
    "kallaway-content-operating-system": (2, 10),
    "growth-blueprint-os": (10, 6),
}
all_workflows: list[str] = []
for skill, (workflow_count, prompt_count) in skills.items():
    skill_root = ROOT / "skills" / skill
    skill_text = read(f"skills/{skill}/SKILL.md")
    frontmatter = re.search(r"^workflows:\s*(\d+)\s*$", skill_text, re.MULTILINE)
    workflows = sorted(path.stem for path in (skill_root / "workflows").glob("*.md"))
    prompts = sorted(path.stem for path in (skill_root / "references" / "prompts-v2").glob("*.md"))
    all_workflows.extend(workflows)
    check(f"{skill} canonical files", (skill_root / "SKILL.md").is_file() and (skill_root / "genius.md").is_file())
    check(
        f"{skill} workflow manifest",
        len(workflows) == workflow_count and frontmatter is not None and int(frontmatter.group(1)) == workflow_count,
        f"files={len(workflows)} frontmatter={frontmatter.group(1) if frontmatter else 'missing'} expected={workflow_count}",
    )
    check(f"{skill} prompt-v2 coverage", len(prompts) == prompt_count, f"found={len(prompts)} expected={prompt_count}")

public_bridges = {
    "ai-topic-mining-engine": "ai-topic-mining-engine",
    "ai-hook-pattern-extractor": "ai-hook-pattern-extractor",
    "ai-creative-reaction-sprint": "ai-creative-reaction-sprint",
    "ai-content-operations": "ai-content-ops",
    "trend-hook-radar": "kallaway-trend-hook-engine",
    "content-os-orchestrator": "kallaway-content-os",
    "micro-fame-authority-density": "kallaway-content-os",
    **{name: name for name in all_workflows if name.startswith("gb-")},
}
missing_bridges = [
    f"{component}->{command}"
    for component, command in public_bridges.items()
    if not (ROOT / ".agent" / "workflows" / f"{command}.md").is_file()
]
check("all public Kallaway commands have canonical bridges", not missing_bridges, ", ".join(missing_bridges))
check(
    "literal topic-mining command has a live source-command wrapper",
    (ROOT / ".agents" / "skills" / "source-command-ai-topic-mining-engine" / "SKILL.md").is_file(),
)

sys.path.insert(0, str(ROOT / "execution"))
from command_aliases import resolve_explicit_command_alias  # noqa: E402

alias = resolve_explicit_command_alias("/ai-topic-mining", {"ai-topic-mining-engine"})
check("literal /ai-topic-mining resolves exactly", alias == ("ai-topic-mining", "ai-topic-mining-engine"), repr(alias))
check(
    "broader routing is not hijacked by incidental text",
    resolve_explicit_command_alias("compare ai topic mining options") is None,
)

producer = read("execution/outlier_radar.py")
schema = read("execution/specs/outlier-radar-pack.schema.md")
signal_fields = (
    "evidence_class",
    "owned_corpus_size",
    "data_maturity_state",
    "cohort_role",
    "engagement_rate",
    "signal_hygiene",
    "rejection_reasons",
)
check("signal-pack v2 producer carries required fields", all(field in producer for field in signal_fields))
check(
    "signal-pack v2 schema carries required fields",
    re.search(r"pack_version(?:\W+)2", schema) is not None and all(field in schema for field in signal_fields),
)

proof = read("extractions/video-context/GmIn1W9V8Rs/proof/cold-start-output.md")
proof_tokens = (
    "Behavior-changing proof: PASS (6/6)",
    "Celebrity-scale topic confounder",
    "FORMAT ONLY",
    "PRIVATE_OUTCOME",
    "No creator opinion was generated",
)
check("cold-start proof covers positive and negative controls", all(token in proof for token in proof_tokens))

python = ROOT / ".venv" / "bin" / "python3"
if not python.exists():
    python = Path(sys.executable)
run(
    "signal-pack contract and sabotage suite",
    [str(python), "extractions/kallaway/validation/verify_outlier_radar.py"],
    "14/14 passed",
)
run(
    "lead-magnet full/degraded/enriched suite",
    [str(python), "extractions/kallaway/validation/verify_lead_magnet_bakes.py"],
    "43/43 checks passed",
)
run(
    "authority-density behavior and sabotage suite",
    [str(python), "execution/verify_kallaway_authority_density_companion.py"],
    "Kallaway Authority Density companion: PASS",
)

failed = [row for row in RESULTS if not row[1]]
for name, ok, detail in RESULTS:
    suffix = f"  [{detail}]" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'}  {name}{suffix}")
print(f"\n{len(RESULTS) - len(failed)}/{len(RESULTS)} completion checks passed")
raise SystemExit(1 if failed else 0)
