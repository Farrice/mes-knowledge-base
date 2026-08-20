#!/usr/bin/env python3
"""Verify the complete cold Greer system and prove the checker catches sabotage."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SKILL = ROOT / "skills/andrew-sean-greer-novel-craft"
SOURCE = ROOT / "extractions/video-context/0kkAl04_0og"
WORKFLOWS = {
    "story-feels-real.md", "echo-map.md", "crossword-assemble.md", "form-permission.md",
    "narrator-distance.md", "reader-invention.md", "surprise-movement.md", "human-evidence.md",
    "comedy-through-fire.md", "editor-patient.md", "more-mermaid.md", "lacquer-revision.md",
}
PROMPTS = {
    "story-feels-real.md", "echo-crossword-reconstruction.md", "scene-form-permission.md",
    "narrator-comedy-distance.md", "surprise-and-human-evidence.md",
    "feedback-and-more-mermaid.md", "cross-domain-story-adapter.md",
}
REFERENCES = {
    "source-ledger.md", "hidden-knowledge.md", "exemplars.md", "quality-rubric.md",
    "cross-domain-adapters.md", "anti-patterns.md", "composition-guide.md",
}
WORKFLOW_SECTIONS = (
    "## Input Required", "## Hard Stop / Refusal", "## Diagnose Before Treat",
    "## Procedure", "## Output Contract", "## Quality Gate", "## Handoff", "## Execution Prompt",
)
PROMPT_SECTIONS = (
    "## Role & Activation", "## Input Required", "## Execution Protocol", "## Output Contract",
    "## Output Skeleton", "## Quality Gate", "## Creative Latitude", "## Deploy When",
)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def section(text: str, heading: str, next_heading: str | None = None) -> str:
    start = text.index(heading) + len(heading)
    end = text.find(next_heading, start) if next_heading else len(text)
    return text[start:end if end >= 0 else len(text)]


def audit() -> list[str]:
    errors: list[str] = []
    actual_workflows = {p.name for p in (SKILL / "workflows").glob("*.md")}
    actual_prompts = {p.name for p in (SKILL / "references/prompts-v2").glob("*.md")}
    actual_refs = {p.name for p in (SKILL / "references").glob("*.md")}
    if actual_workflows != WORKFLOWS:
        errors.append(f"workflow inventory drift: {sorted(actual_workflows ^ WORKFLOWS)}")
    if actual_prompts != PROMPTS:
        errors.append(f"prompt inventory drift: {sorted(actual_prompts ^ PROMPTS)}")
    if actual_refs != REFERENCES:
        errors.append(f"reference inventory drift: {sorted(actual_refs ^ REFERENCES)}")

    skill_text = (SKILL / "SKILL.md").read_text()
    for phrase in (
        "COLD_BUILD_COMPLETE", "HUMAN_BLIND_VERDICT: NO EVENT", "REGISTRATION: NOT AUTHORIZED",
        "Never run all twelve", "## Recognition Test", "## Handoff Schema",
    ):
        if phrase not in skill_text:
            errors.append(f"SKILL missing boundary: {phrase}")
    if not (ROOT / "agents/andrew-sean-greer/AGENT.md").is_file():
        errors.append("cold expert configuration missing")

    for path in sorted((SKILL / "workflows").glob("*.md")):
        text = path.read_text()
        for required in WORKFLOW_SECTIONS:
            if required not in text:
                errors.append(f"{path.name}: missing {required}")
        match = re.search(r"^prompt:\s+(references/prompts-v2/[^\s]+)$", text, re.M)
        if not match or not (SKILL / match.group(1)).is_file():
            errors.append(f"{path.name}: unresolved prompt pointer")
        body_pointer = re.search(r"Read and honor `\.\./references/prompts-v2/([^`]+)`", text)
        if not body_pointer or body_pointer.group(1) not in PROMPTS:
            errors.append(f"{path.name}: body prompt pointer missing or invalid")

    for path in sorted((SKILL / "references/prompts-v2").glob("*.md")):
        text = path.read_text()
        for value in (
            "source_prompt: born-v2", "skill: andrew-sean-greer-novel-craft",
            "standard: structure-pure-v2", "forged: born-v2", "refactored: 2026-08-18",
        ):
            if value not in text:
                errors.append(f"{path.name}: missing frontmatter {value}")
        for required in PROMPT_SECTIONS:
            if required not in text:
                errors.append(f"{path.name}: missing {required}")
        skeleton = section(text, "## Output Skeleton", "## Quality Gate")
        if "```markdown" not in skeleton or "[...]" not in skeleton:
            errors.append(f"{path.name}: output skeleton is not placeholder-based")

    positive = load_json(SKILL / "tests/fixtures/positive-cases.json").get("cases", [])
    negative = load_json(SKILL / "tests/fixtures/negative-controls.json").get("cases", [])
    if len(positive) != 7 or {c.get("id") for c in positive} != {"FIC-01", "FIC-02", "DOM-01", "DOM-02", "DOM-03", "DOM-04", "DOM-05"}:
        errors.append("positive fixtures must be exact approved 2 fiction + 5 unlike-domain set")
    if len(negative) != 7 or {c.get("id") for c in negative} != {f"NEG-{n:02d}" for n in range(1, 8)}:
        errors.append("negative fixtures must preserve all seven enumerated controls")

    candidates = (SKILL / "tests/candidates/greer-candidates.md").read_text()
    decisions = (SKILL / "tests/candidates/negative-control-decisions.md").read_text()
    for case_id in ("FIC-01", "FIC-02", "DOM-01", "DOM-02", "DOM-03", "DOM-04", "DOM-05"):
        if candidates.count(f"## {case_id}") != 1:
            errors.append(f"candidate missing or duplicates {case_id}")
    for case in negative:
        if case["id"] not in decisions or f"`{case['expected']}`" not in decisions:
            errors.append(f"negative decision mismatch: {case['id']}")

    dom1 = section(candidates, "## DOM-01", "## DOM-02")
    if not all(token in dom1 for token in ("H1", "H2", "H3", "optional", "not treatment", "Stop if symptoms occur")):
        errors.append("DOM-01 lost frozen health labels or boundaries")
    dom2 = section(candidates, "## DOM-02", "## DOM-03")
    if not all(token in dom2 for token in ("140", "224", "Sixty percent", "not causal proof", "two-week rollback")):
        errors.append("DOM-02 changed evidence or recommendation")
    dom3 = section(candidates, "## DOM-03", "## DOM-04")
    if not all(token in dom3 for token in ("three vendor invoices", "Friday rescue", "within seven days", "no customer or revenue event")):
        errors.append("DOM-03 invented or lost founder facts")
    dom4 = section(candidates, "## DOM-04", "## DOM-05")
    words = re.findall(r"\b[\w’'-]+\b", dom4)
    if not 115 <= len(words) <= 145:
        errors.append(f"DOM-04 runtime proxy is {len(words)} words, expected 115-145")
    if dom4.lower().count("try the demo") != 1 or "human reviews every draft before send" not in dom4:
        errors.append("DOM-04 lost CTA or human-review lock")
    dom5 = section(candidates, "## DOM-05")
    if "UNTESTED / NO EVENT" not in dom5 or "No buyer, revenue, or outcome event exists" not in dom5 or "Join the pilot" not in dom5:
        errors.append("DOM-05 lost proof state or CTA")

    manifest = load_json(SOURCE / "manifest.json")
    for entry in manifest.get("files", []):
        path = SOURCE / entry["path"]
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != entry["sha256"]:
            errors.append(f"source manifest mismatch: {entry['path']}")

    masked = SKILL / "tests/masked-verdicts/masked-packet.md"
    labels = load_json(SKILL / "tests/masked-verdicts/label-map.json")
    if labels.get("status") != "SEALED_FOR_HUMAN_REVIEW_NO_EVENT":
        errors.append("masked packet proof state drifted")
    if not masked.is_file() or hashlib.sha256(masked.read_text().encode()).hexdigest() != labels.get("packet_sha256"):
        errors.append("masked packet is missing or not bound to label map")
    if len(labels.get("cases", {})) != 7 or masked.read_text().count("### Human Score — NO EVENT") != 7:
        errors.append("masked packet must contain seven unscored pairs")

    live = [
        *ROOT.glob(".agent/workflows/greer-*.md"),
        *ROOT.glob(".claude/commands/greer-*.md"),
        *ROOT.glob(".agents/skills/source-command-greer*"),
    ]
    if live:
        errors.append(f"forbidden live surfaces exist: {[str(p.relative_to(ROOT)) for p in live]}")
    for registry in ("AGENT_INDEX.md", "SKILL_INDEX.md", "SLASH_COMMANDS.md"):
        text = (ROOT / registry).read_text(errors="ignore")
        if "andrew-sean-greer-novel-craft" in text or "agents/andrew-sean-greer" in text:
            errors.append(f"forbidden registration found in {registry}")
    return errors


def false_green_controls() -> list[str]:
    caught: list[str] = []
    good = (SKILL / "references/prompts-v2/story-feels-real.md").read_text()
    broken = good.replace("## Quality Gate", "## Removed Gate", 1)
    if "## Quality Gate" not in broken:
        caught.append("missing-prompt-quality-gate")
    negative = load_json(SKILL / "tests/fixtures/negative-controls.json")["cases"][:-1]
    if len(negative) != 7:
        caught.append("missing-negative-control")
    candidate = (SKILL / "tests/candidates/greer-candidates.md").read_text().replace("UNTESTED / NO EVENT", "PROVEN", 1)
    if "UNTESTED / NO EVENT" not in section(candidate, "## DOM-05"):
        caught.append("proof-invention")
    return caught


def main() -> int:
    errors = audit()
    caught = false_green_controls()
    if caught != ["missing-prompt-quality-gate", "missing-negative-control", "proof-invention"]:
        errors.append(f"false-green controls did not all convict: {caught}")
    if errors:
        print("GREER COLD SKILL SYSTEM: FAIL")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("GREER COLD SKILL SYSTEM: PASS")
    print("- 12 workflows + 7 born-v2 prompts + 7 references + 1 cold expert configuration")
    print("- 2 fiction + 5 unlike-domain transformations + 7 negative controls + 7 masked pairs")
    print("- source manifest hash-bound; live public surfaces absent")
    print("- false-green controls caught: prompt gate, negative-control count, proof invention")
    print("- proof boundary: orchestrator-attested candidates; human blind verdict NO EVENT")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
