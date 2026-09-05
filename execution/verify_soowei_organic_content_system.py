#!/usr/bin/env python3
"""Verify the SooWei organic-content expansion and its failure boundaries."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "soowei-consulting-leverage"
PACKAGE = ROOT / "extractions" / "soowei-goh-organic-content-acquisition-2026"
BLIND_ROOT = ROOT / "extractions" / "soowei-consulting-leverage"

BLIND_CORPUS = {
    "2026-08-12-lie-detector.md": "e96823ef8b45d7d5d396f11b7ec4ed2b4474c869374758ce2ca1253ba650e881",
    "2026-08-31-in-house-content-team.md": "5907ad4ace027319f282db5b0dcff96867065b9a392a3d289471bcf90bbe4da8",
}

WORKFLOWS = (
    "buyer-mirror-content-intelligence",
    "trust-sequence-content-architecture",
    "two-pipeline-content-operations",
    "broad-to-buyer-script-funnel",
    "owned-proof-content-builder",
    "triple-hook-format-packaging",
    "soowei-organic-content-system",
    "retention-repurposing-learning-loop",
)

PRESERVED_WORKFLOWS = {
    "founder-leverage-exit-roadmap.md": "928e148591e7ef9d51a9cbd72c95499da556f2bf4dede94103af2fb57d373f82",
    "high-leverage-offer-architecture.md": "25e81a1374467109a81ae2ffea44cba54496e98706f73cc9bd39acfbc26da1ce",
    "high-ticket-conversion-engine.md": "66e27b827aecf6812eba2bf5f211f4644b243616c1436e6929bf2576b9900ff2",
    "scalable-delivery-ip-system.md": "e41d26f47d0041d777dba2f4e8e12faa7154f14b227b6acb522aa2f5b8f6491f",
}

WORKFLOW_SECTIONS = (
    "## Pre-Flight Gate",
    "## Input Required",
    "## Execution Protocol",
    "## Content Type Adaptations",
    "## Output Contract",
    "## Quality Gate",
)

PROMPT_SECTIONS = (
    "## Role & Activation",
    "## Input Required",
    "## Execution Protocol",
    "## Output Contract",
    "## Output Skeleton",
    "## Quality Gate",
    "## Deploy When",
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(*args: str) -> tuple[int, str]:
    result = subprocess.run(
        list(args),
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return result.returncode, result.stdout


def main() -> int:
    failures: list[str] = []
    notes: list[str] = []

    manifest = read(SKILL / "SKILL.md")
    if 'version: "3.0"' not in manifest or "workflows: 12" not in manifest:
        failures.append("SKILL.md must declare version 3.0 and 12 workflows")

    for slug in WORKFLOWS:
        workflow = SKILL / "workflows" / f"{slug}.md"
        prompt = SKILL / "references" / "prompts-v2" / f"{slug}.md"
        wrapper = ROOT / ".agent" / "workflows" / f"{slug}.md"
        shim = ROOT / ".claude" / "commands" / f"{slug}.md"

        for path in (workflow, prompt, wrapper, shim):
            if not path.exists():
                failures.append(f"missing {path.relative_to(ROOT)}")

        if workflow.exists():
            body = read(workflow)
            for section in WORKFLOW_SECTIONS:
                if section not in body:
                    failures.append(f"{slug} workflow missing {section}")
            pointer = f"references/prompts-v2/{slug}.md"
            if pointer not in body:
                failures.append(f"{slug} workflow missing exact prompt pointer")

        if prompt.exists():
            body = read(prompt)
            if "standard: structure-pure-v2" not in body or "forged: born-v2" not in body:
                failures.append(f"{slug} prompt has invalid born-v2 frontmatter")
            for section in PROMPT_SECTIONS:
                if section not in body:
                    failures.append(f"{slug} prompt missing {section}")

        if wrapper.exists():
            body = read(wrapper)
            if f"skills/soowei-consulting-leverage/workflows/{slug}.md" not in body:
                failures.append(f"{slug} wrapper points to the wrong workflow")
            if f"skills/soowei-consulting-leverage/references/prompts-v2/{slug}.md" not in body:
                failures.append(f"{slug} wrapper points to the wrong prompt")

        if shim.exists() and f".agent/workflows/{slug}.md" not in read(shim):
            failures.append(f"{slug} command shim points to the wrong wrapper")

    for filename, expected in PRESERVED_WORKFLOWS.items():
        path = SKILL / "workflows" / filename
        if not path.exists() or sha256(path) != expected:
            failures.append(f"preservation lock failed for {filename}")

    for required in (
        SKILL / "references" / "organic-content-acquisition-source-map.md",
        SKILL / "references" / "hidden-knowledge.md",
        PACKAGE / "skill-system-contract.md",
        PACKAGE / "behavior-proof" / "fixture.md",
        PACKAGE / "behavior-proof" / "baseline-current-skill.md",
        PACKAGE / "behavior-proof" / "expanded-system-output.md",
        PACKAGE / "behavior-proof" / "comparison.md",
        PACKAGE / "behavior-proof" / "cold-start.md",
        PACKAGE / "behavior-proof" / "negative-controls.json",
        BLIND_ROOT / "reference-corpus" / "README.md",
        BLIND_ROOT / "blind-pass" / "README.md",
        BLIND_ROOT / "blind-pass" / "generator-packet.md",
        BLIND_ROOT / "blind-pass" / "matched-form-addendum.md",
        BLIND_ROOT / "blind-pass" / "source-integrity-audit.md",
        BLIND_ROOT / "blind-pass" / "judgment-sheet.md",
        BLIND_ROOT / "blind-pass" / "generated" / "candidate-1-content-operation.md",
        BLIND_ROOT / "blind-pass" / "generated" / "candidate-2-trust-proof.md",
        BLIND_ROOT / "blind-pass" / "generated" / "specimen-1-content-team-transcript.md",
        BLIND_ROOT / "blind-pass" / "generated" / "specimen-2-trust-interview-transcript.md",
        BLIND_ROOT / "blind-pass" / "review" / "judgment-sheet.md",
        BLIND_ROOT / "blind-pass" / "review" / "assembly-receipt.md",
        BLIND_ROOT / "blind-pass" / "review" / "pair-1-sample-a.md",
        BLIND_ROOT / "blind-pass" / "review" / "pair-1-sample-b.md",
        BLIND_ROOT / "blind-pass" / "review" / "pair-2-sample-a.md",
        BLIND_ROOT / "blind-pass" / "review" / "pair-2-sample-b.md",
        BLIND_ROOT / "blind-pass" / ".sealed-mapping.json",
    ):
        if not required.exists() or required.stat().st_size == 0:
            failures.append(f"missing or empty {required.relative_to(ROOT)}")

    corpus_dir = BLIND_ROOT / "reference-corpus"
    counted_corpus = sorted(
        path for path in corpus_dir.glob("*.md")
        if path.name != "README.md" and path.stat().st_size > 0
    )
    if [path.name for path in counted_corpus] != sorted(BLIND_CORPUS):
        failures.append("blind corpus must contain exactly the two approved unseen pieces")
    for filename, expected in BLIND_CORPUS.items():
        path = corpus_dir / filename
        if not path.exists() or sha256(path) != expected:
            failures.append(f"blind-corpus integrity failed for {filename}")

    generator_packet = BLIND_ROOT / "blind-pass" / "generator-packet.md"
    if generator_packet.exists():
        packet = read(generator_packet)
        for boundary in ("## Forbidden Reads", "reference-corpus/", "self-assessment: omitted", "external actions: NONE"):
            if boundary not in packet:
                failures.append(f"generator packet missing clean-room boundary: {boundary}")

    generated_dir = BLIND_ROOT / "blind-pass" / "generated"
    for filename in (
        "candidate-1-content-operation.md",
        "candidate-2-trust-proof.md",
        "specimen-1-content-team-transcript.md",
        "specimen-2-trust-interview-transcript.md",
    ):
        path = generated_dir / filename
        if path.exists():
            body = read(path)
            for boundary in ("Forbidden reads: NONE", "External actions: NONE"):
                if boundary not in body:
                    failures.append(f"{filename} missing clean-room receipt: {boundary}")

    review_dir = BLIND_ROOT / "blind-pass" / "review"
    public_leak_markers = (
        "Source URL:", "Published:", "Creator:", "Acquisition:", "Blind status:",
        "Generation Receipt", "Authorized reads:", "Forbidden reads:",
        "INTERVIEWER:", "CONSULTANT:",
    )
    for filename in (
        "pair-1-sample-a.md", "pair-1-sample-b.md",
        "pair-2-sample-a.md", "pair-2-sample-b.md",
    ):
        path = review_dir / filename
        if path.exists():
            body = read(path)
            if any(marker in body for marker in public_leak_markers):
                failures.append(f"blind review identity or generation marker leaked in {filename}")
            if len(body.split()) < 2000:
                failures.append(f"blind review sample too short for A-tier comparison: {filename}")

    sealed_mapping = BLIND_ROOT / "blind-pass" / ".sealed-mapping.json"
    if sealed_mapping.exists():
        try:
            mapping = json.loads(read(sealed_mapping))
            pairs = mapping.get("pairs", [])
            if len(pairs) != 2:
                failures.append("sealed mapping must contain exactly two pairs")
            for pair in pairs:
                samples = pair.get("samples", {})
                if set(samples) != {"A", "B"}:
                    failures.append("each sealed pair must contain neutral labels A and B")
                    continue
                if {samples["A"].get("kind"), samples["B"].get("kind")} != {"real", "generated"}:
                    failures.append("each sealed pair must contain one real and one generated specimen")
        except json.JSONDecodeError as exc:
            failures.append(f"sealed mapping JSON invalid: {exc}")

    controls_path = PACKAGE / "behavior-proof" / "negative-controls.json"
    if controls_path.exists():
        try:
            controls = json.loads(read(controls_path))
            expected_ids = {
                "missing_buyer_evidence",
                "unsupported_proof",
                "no_publish_permission",
                "reach_only",
                "ratio_as_law",
            }
            actual_ids = {row.get("id") for row in controls if isinstance(row, dict)}
            if actual_ids != expected_ids:
                failures.append("negative controls are incomplete or unexpected")
            if any(not row.get("expected") or not row.get("forbidden") for row in controls):
                failures.append("every negative control needs expected and forbidden behavior")
        except json.JSONDecodeError as exc:
            failures.append(f"negative controls JSON invalid: {exc}")

    behavior = read(PACKAGE / "behavior-proof" / "comparison.md") if (PACKAGE / "behavior-proof" / "comparison.md").exists() else ""
    expanded = read(PACKAGE / "behavior-proof" / "expanded-system-output.md") if (PACKAGE / "behavior-proof" / "expanded-system-output.md").exists() else ""
    cold_start = read(PACKAGE / "behavior-proof" / "cold-start.md") if (PACKAGE / "behavior-proof" / "cold-start.md").exists() else ""
    if "## Verdict: PASS" not in behavior or "synthetic" not in behavior.lower():
        failures.append("behavior comparison lacks a bounded PASS verdict")
    for boundary in ("NO EVENT", "NO PERMISSION", "earliest missing layer", "Stop before publishing"):
        if boundary.lower() not in expanded.lower():
            failures.append(f"expanded behavior proof missing boundary: {boundary}")
    for receipt in ("ranked `/soowei-organic-content-system` first", "Behavior comparison: PASS", "Outcome state: UNTESTED"):
        if receipt.lower() not in cold_start.lower():
            failures.append(f"cold-start receipt missing: {receipt}")

    safeguards = {
        "missing buyer evidence": (SKILL / "workflows" / "buyer-mirror-content-intelligence.md", "Evidence Acquisition Mode"),
        "unsupported proof": (SKILL / "workflows" / "owned-proof-content-builder.md", "proof-capture plan"),
        "no publishing permission": (SKILL / "workflows" / "soowei-organic-content-system.md", "Stop before publishing"),
        "reach-only result": (SKILL / "workflows" / "retention-repurposing-learning-loop.md", "NO EVENT"),
        "fixed ratio": (SKILL / "workflows" / "broad-to-buyer-script-funnel.md", "planning metaphor"),
    }
    for label, (path, phrase) in safeguards.items():
        if not path.exists() or phrase.lower() not in read(path).lower():
            failures.append(f"negative-control safeguard missing: {label}")

    verifier = ROOT / "execution" / "verify_video_context_source_package.py"
    for video_id in ("Y388trCakrs", "PRqSCE8uZns"):
        source = PACKAGE / "sources" / video_id
        code, output = run(sys.executable, str(verifier), str(source))
        if code != 0:
            failures.append(f"source package {video_id} failed:\n{output}")

    route_query = "turn buyer interviews proof and content performance into an organic content to call system"
    combined = ""
    for script in ("command_menu.py", "workflow_router.py"):
        code, output = run(sys.executable, str(ROOT / "execution" / script), "search", route_query)
        if code != 0:
            failures.append(f"{script} failed during route check")
        combined += output
    if "/soowei-organic-content-system" not in combined:
        failures.append("natural-language routing does not surface /soowei-organic-content-system")

    if failures:
        print("SooWei organic content system: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    notes.append(f"{len(WORKFLOWS)} workflows + {len(WORKFLOWS)} born-v2 prompts")
    notes.append("8 generated wrappers + 8 native command shims")
    notes.append("4 existing workflows byte-preserved")
    notes.append("5 negative-control boundaries present")
    notes.append("2 source packages pass")
    notes.append("behavior comparison and natural-language route pass")
    notes.append("cold-start execution receipt present")
    notes.append("A-tier blind review ready 2/2; clean-room access and sealed randomization pass; human verdict pending")
    print("SooWei organic content system: PASS")
    for note in notes:
        print(f"- {note}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
