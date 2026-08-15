#!/usr/bin/env python3
"""Verify the canonical Google Antigravity buyer-psychology SHADOW overlay."""

from __future__ import annotations

import html
import json
import importlib.util
import re
import unicodedata
from pathlib import Path

from build_jason_canonical_admission_map import build as build_admission_map
from jason_buyer_psychology_runtime_surface import overlay_pointer_paths, promotion_violations
from verify_video_context_source_package import verify_package


ROOT = Path(__file__).resolve().parents[1]
SOURCE_IDS = (
    "jbPNjNtQqk0",
    "8U0BDpRnPFU",
    "nGZbkwKboVU",
    "ooGeFK70d5U",
    "H_TvNSNbRiU",
    "B90eANIJ2XI",
)
EXPECTED_SOURCE_METADATA = {
    "jbPNjNtQqk0": {
        "title": "8 “Buyer Secrets” that Print F*ck You Money",
        "duration": 1665,
    },
    "8U0BDpRnPFU": {
        "title": "This Secret Made Me Millions (The 4 Modes of Communication)",
        "duration": 927,
    },
    "nGZbkwKboVU": {
        "title": "The Power of Schema (18 schemas and why you’re stuck!)",
        "duration": 865,
    },
    "ooGeFK70d5U": {
        "title": "The Power Of Loaded Language",
        "duration": 760,
    },
    "H_TvNSNbRiU": {
        "title": "Step by Step on How to Close 30% of Your Audience with Webinars.",
        "duration": 1811,
    },
    "B90eANIJ2XI": {
        "title": "Watch me close 30% of a room on a $3k offer",
        "duration": 3774,
    },
}
SHADOW_DECISIONS = (
    "Belief",
    "Focus",
    "Recognition",
    "Priority",
    "Fit",
    "Choice",
    "Congruence",
    "Affect",
)
CANDIDATE_DECISIONS = ("Evidence", "Agency", "Value", "Action", "Experience")

PRIMITIVE = ROOT / "semantic_libraries/antigravity/primitives/buyer-psychology-decision-intelligence-overlay.md"
REFERENCE = ROOT / "skills/jason-fladlien-marketing/references/buyer-psychology-decision-layer.md"
SKILL = ROOT / "skills/jason-fladlien-marketing/SKILL.md"
CORPUS = ROOT / "extractions/jason-fladlien/buyer-psychology-intelligence-layer/source-corpus-index.md"
REGISTRY = ROOT / "extractions/jason-fladlien/buyer-psychology-intelligence-layer/mechanism-registry.json"
ADMISSION = ROOT / "extractions/jason-fladlien/buyer-psychology-intelligence-layer/canonical-admission-map.json"
DEPLOYMENT = ROOT / "extractions/jason-fladlien/buyer-psychology-intelligence-layer/canonical-deployment-receipt.md"
COMPILER = ROOT / "execution/jason_buyer_psychology_situation_compiler.py"
CONTEXT_INDEX = ROOT / "execution/skill_chunks.json"

ALLOWED_OVERLAY_POINTERS = {
    ".agent/workflows/campaign-architect.md",
    ".agent/workflows/copy-engine.md",
    ".agent/workflows/farrice-content-os.md",
    ".agent/workflows/high-taste-writing-os.md",
    ".agent/workflows/revenue-offer-agent.md",
    "skills/jason-fladlien-marketing/SKILL.md",
}

EXPECTED_RUNTIME_OWNER_DECISIONS = {
    "/copy-engine": {"Belief", "Focus", "Recognition", "Congruence", "Affect"},
    "/farrice-content-os": {"Belief", "Focus", "Recognition", "Priority", "Affect"},
    "/revenue-offer-agent": {"Fit", "Choice", "Congruence"},
    "/campaign-architect": {"Fit", "Choice", "Congruence"},
    "Selected Campaign Owner": {"Fit", "Choice", "Congruence"},
    "Selected Writing Owner": {"Belief", "Focus", "Recognition", "Priority", "Congruence"},
}

OWNER_FILES = {
    ROOT / ".agent/workflows/campaign-architect.md": (
        "BUYER-DECISION ARCHITECTURE SNIFF",
        "eligible **Fit, Choice, or Congruence**",
        "buyer-psychology-decision-intelligence-overlay.md",
        "`/campaign-architect` remains the campaign owner",
        "five development-only `CANDIDATE` cards",
    ),
    ROOT / ".agent/workflows/copy-engine.md": (
        "Buyer-decision intelligence sniff",
        "eligible **Belief, Focus, Recognition, Congruence, or Affect**",
        "buyer-psychology-decision-intelligence-overlay.md",
        "/copy-engine` remains the owner",
        "five `CANDIDATE` cards are development-only",
    ),
    ROOT / ".agent/workflows/farrice-content-os.md": (
        "Buyer-Decision Architecture Sniff",
        "eligible **Belief, Focus, Recognition, Priority, or Affect**",
        "buyer-psychology-decision-intelligence-overlay.md",
        "one-composer rule",
        "five `CANDIDATE` cards remain development-only",
    ),
    ROOT / ".agent/workflows/revenue-offer-agent.md": (
        "After TERMS",
        "Fit, Choice, or Congruence",
        "buyer-psychology-decision-intelligence-overlay.md",
        "TERMS remains primary",
        "existing three change slots",
    ),
    ROOT / ".agent/workflows/high-taste-writing-os.md": (
        "Reader understands but does not reconsider, decide, or act",
        "eligible Belief, Focus, Recognition, Priority, or Congruence",
        "Buyer Psychology Decision Intelligence Overlay",
        "cold SHADOW",
        "The main composer integrates",
    ),
}

FORBIDDEN_RUNTIME_PATHS = (
    ROOT / ".agent/workflows/buyer-psychology-decision-intelligence-overlay.md",
    ROOT / ".claude/commands/buyer-psychology-decision-intelligence-overlay.md",
    ROOT / ".agents/skills/source-command-buyer-psychology-decision-intelligence-overlay",
    ROOT / "agents/buyer-psychology-decision-intelligence-overlay",
    ROOT / "skills/buyer-psychology-decision-intelligence-overlay",
)
FORBIDDEN_PROMOTION_SURFACES = (
    ROOT / "CODEX.md",
    ROOT / "AGENTS.md",
    ROOT / "DOMAIN_REGISTRY.md",
    ROOT / "execution/expert_router.py",
)
ACTIVE_CORE = (PRIMITIVE, REFERENCE, SKILL, COMPILER, *OWNER_FILES)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="strict")


def require_file(path: Path, failures: list[str]) -> str:
    if not path.is_file():
        failures.append(f"missing file: {path.relative_to(ROOT)}")
        return ""
    if path.stat().st_size == 0:
        failures.append(f"empty file: {path.relative_to(ROOT)}")
        return ""
    return read(path)


def require_terms(label: str, content: str, terms: tuple[str, ...], failures: list[str]) -> None:
    lowered = content.lower()
    for term in terms:
        if term.lower() not in lowered:
            failures.append(f"{label} missing term: {term}")


def parse_timestamp(value: str) -> float | None:
    match = re.fullmatch(r"(\d{2}):(\d{2}):(\d{2})\.(\d{3})", value)
    if not match:
        return None
    hours, minutes, seconds, millis = (int(part) for part in match.groups())
    if minutes >= 60 or seconds >= 60:
        return None
    return hours * 3600 + minutes * 60 + seconds + millis / 1000


def canonical_transcript_text(value: str) -> str:
    """Normalize representation-only spacing without changing spoken words."""
    normalized = unicodedata.normalize("NFKC", html.unescape(value))
    normalized = re.sub(r"<[^>]+>", "", normalized)
    normalized = re.sub(r"\s+([,.;:!?])", r"\1", normalized)
    return re.sub(r"\s+", " ", normalized).strip()


def visible_vtt_cues(value: str) -> dict[tuple[str, str], str]:
    """Map each VTT timestamp pair to its canonical visible cue body."""
    timestamp_pattern = re.compile(
        r"^(\d{2}:\d{2}:\d{2}\.\d{3})\s+-->\s+(\d{2}:\d{2}:\d{2}\.\d{3})"
    )
    lines = value.splitlines()
    cues: dict[tuple[str, str], str] = {}
    index = 0
    while index < len(lines):
        match = timestamp_pattern.match(lines[index])
        if not match:
            index += 1
            continue
        key = match.groups()
        index += 1
        body: list[str] = []
        while index < len(lines) and not timestamp_pattern.match(lines[index]):
            if lines[index].strip():
                body.append(lines[index])
            index += 1
        cues[key] = canonical_transcript_text(" ".join(body))
    return cues


def validate_source_packages(corpus: str, failures: list[str]) -> list[str]:
    notes: list[str] = []
    for source_id in SOURCE_IDS:
        package = ROOT / "extractions/video-context" / source_id
        ok, package_failures, package_notes = verify_package(package)
        if not ok:
            failures.extend(f"{source_id}: {item}" for item in package_failures)
        if source_id not in corpus:
            failures.append(f"corpus index missing source: {source_id}")
        metadata = json.loads(require_file(package / "metadata.json", failures) or "{}")
        expected = {
            "id": source_id,
            "uploader": "Jason Fladlien",
            **EXPECTED_SOURCE_METADATA[source_id],
        }
        for key, value in expected.items():
            if metadata.get(key) != value:
                failures.append(
                    f"{source_id} metadata {key}: expected {value!r}, got {metadata.get(key)!r}"
                )

        segments = json.loads(require_file(package / "transcript_segments.json", failures) or "[]")
        transcript_text = require_file(package / "transcript.txt", failures)
        transcript_vtt = require_file(package / "transcript.vtt", failures)
        vtt_cues = visible_vtt_cues(transcript_vtt)
        malformed: list[int] = []
        timestamp_mismatches: list[int] = []
        missing_vtt_cues: list[int] = []
        source_text_mismatches: list[int] = []
        prior_start = -1.0
        if not isinstance(segments, list) or not segments:
            failures.append(f"{source_id}: transcript segments must be a non-empty list")
        else:
            for index, segment in enumerate(segments):
                if not isinstance(segment, dict):
                    malformed.append(index)
                    continue
                start = segment.get("start_seconds")
                end = segment.get("end_seconds")
                start_text = segment.get("start")
                end_text = segment.get("end")
                parsed_start = parse_timestamp(start_text) if isinstance(start_text, str) else None
                parsed_end = parse_timestamp(end_text) if isinstance(end_text, str) else None
                if (
                    not start_text
                    or not end_text
                    or not isinstance(start, (int, float))
                    or not isinstance(end, (int, float))
                    or start < prior_start
                    or end < start
                    or not str(segment.get("text", "")).strip()
                    or not str(segment.get("source_text", "")).strip()
                ):
                    malformed.append(index)
                if (
                    parsed_start is None
                    or parsed_end is None
                    or not isinstance(start, (int, float))
                    or not isinstance(end, (int, float))
                    or abs(parsed_start - start) > 0.002
                    or abs(parsed_end - end) > 0.002
                ):
                    timestamp_mismatches.append(index)
                if isinstance(start_text, str) and isinstance(end_text, str) and (
                    start_text,
                    end_text,
                ) not in vtt_cues:
                    missing_vtt_cues.append(index)
                elif canonical_transcript_text(str(segment.get("source_text", ""))) != vtt_cues[
                    (start_text, end_text)
                ]:
                    source_text_mismatches.append(index)
                prior_start = start if isinstance(start, (int, float)) else prior_start
            if malformed:
                failures.append(
                    f"{source_id}: malformed full transcript segments at indexes {malformed[:10]}"
                )
            if timestamp_mismatches:
                failures.append(
                    f"{source_id}: timestamp text/seconds mismatch at indexes {timestamp_mismatches[:10]}"
                )
            if missing_vtt_cues:
                failures.append(
                    f"{source_id}: segment timestamps missing from transcript.vtt at indexes {missing_vtt_cues[:10]}"
                )
            if source_text_mismatches:
                failures.append(
                    f"{source_id}: segment source_text differs from transcript.vtt cue body at indexes {source_text_mismatches[:10]}"
                )
            joined_segments = canonical_transcript_text(
                " ".join(str(segment.get("text", "")) for segment in segments)
            )
            if joined_segments != canonical_transcript_text(transcript_text):
                failures.append(
                    f"{source_id}: transcript_segments text does not reconstruct transcript.txt"
                )
            last_end = segments[-1].get("end_seconds")
            duration = metadata.get("duration")
            if (
                not isinstance(last_end, (int, float))
                or not isinstance(duration, (int, float))
                or last_end > duration + 5.0
            ):
                failures.append(
                    f"{source_id}: final caption end {last_end!r} exceeds duration {duration!r} + 5s tolerance"
                )
        notes.append(f"{source_id}: {', '.join(package_notes)}")
    return notes


def validate_skill_inventory(skill: str, failures: list[str]) -> None:
    workflow_root = ROOT / "skills/jason-fladlien-marketing/workflows"
    prompt_root = ROOT / "skills/jason-fladlien-marketing/references/prompts"
    prompt_v2_root = ROOT / "skills/jason-fladlien-marketing/references/prompts-v2"
    legacy_root = ROOT / "skills/jason-fladlien-marketing/references/_legacy-prompts"
    workflows = sorted(workflow_root.glob("*.md"))
    prompts = sorted(prompt_root.glob("*.md"))
    prompts_v2 = sorted(prompt_v2_root.glob("*.md"))
    legacy = sorted(legacy_root.glob("*.md"))
    if len(workflows) != 38:
        failures.append(f"canonical Jason workflows: expected 38, got {len(workflows)}")
    if len(prompts_v2) != 33:
        failures.append(f"canonical Jason prompts-v2: expected 33, got {len(prompts_v2)}")
    if len(prompts) != 26 or len(legacy) != 26:
        failures.append(f"canonical compatibility/legacy prompts: expected 26/26, got {len(prompts)}/{len(legacy)}")
    for prompt in prompts:
        counterpart = legacy_root / prompt.name
        if not counterpart.is_file() or counterpart.read_bytes() != prompt.read_bytes():
            failures.append(f"legacy duplicate drift: {prompt.name}")
    require_terms(
        "Jason skill",
        skill,
        (
            "Workflows (38 files: 37 public + 1 internal)",
            "Cold Buyer-Psychology Decision Companion",
            "buyer-psychology-decision-intelligence-overlay.md",
            "buyer-psychology-decision-layer.md",
            "canonical-admission-map.md",
            "33 deterministic practitioner prompts",
        ),
        failures,
    )


def validate_admission(failures: list[str]) -> None:
    recorded = json.loads(require_file(ADMISSION, failures) or "{}")
    try:
        generated = build_admission_map()
    except Exception as exc:  # deterministic builder should fail closed
        failures.append(f"canonical admission builder failed: {exc}")
        return
    if recorded != generated:
        failures.append("canonical admission map differs from current canonical inventory and hashes")
    summary = recorded.get("summary", {})
    if summary.get("entries") != 97:
        failures.append(f"canonical admission entries: {summary.get('entries')}")
    if summary.get("by_surface") != {
        "compatibility-prompt": 26,
        "prompt-v2-born": 7,
        "prompt-v2-refactor": 26,
        "workflow": 38,
    }:
        failures.append(f"canonical admission surface counts: {summary.get('by_surface')}")
    if summary.get("by_status") != {
        "ADMIT": 28,
        "DEFENSIVE-LITERACY-ONLY": 39,
        "EXCLUDE-FROM-MASTER": 30,
    }:
        failures.append(f"canonical admission status counts: {summary.get('by_status')}")
    if summary.get("legacy_duplicate_evidence_weight") != 0:
        failures.append("legacy duplicate evidence weight must remain zero")


def main() -> int:
    failures: list[str] = []
    corpus = require_file(CORPUS, failures)
    notes = validate_source_packages(corpus, failures)

    primitive = require_file(PRIMITIVE, failures)
    require_terms(
        "primitive",
        primitive,
        (
            "Status: SHADOW",
            "Activation",
            "Skip Conditions",
            "Evidence Language",
            "Truth and Ethics Guard",
            "Native Function Ownership",
            "Cold Context Policy",
            "Promotion Gate",
            "early SHADOW-continuation check",
            "30/30",
            "21/30",
            "18/18",
            "fifteen complete real-task receipts",
            "12/12",
            "limited opt-in candidate route",
            "Kill or Keep Cold",
            *SHADOW_DECISIONS,
        ),
        failures,
    )
    require_terms(
        "primitive owner map",
        primitive,
        (
            "`/copy-engine` | Belief, Focus, Recognition, Congruence, Affect",
            "`/farrice-content-os` | Belief, Focus, Recognition, Priority, Affect",
            "`/campaign-architect` | Fit, Choice, Congruence",
            "`/revenue-offer-agent` | Fit, Choice, Congruence",
            "`/high-taste-writing-os` | Belief, Focus, Recognition, Priority, Congruence",
        ),
        failures,
    )
    for forbidden in ("ENFORCED", "HARD BLOCK", "mandatory score", "always apply", "all knowledge work"):
        if forbidden.lower() in primitive.lower():
            failures.append(f"primitive contains forbidden promotion language: {forbidden}")

    reference = require_file(REFERENCE, failures)
    require_terms(
        "Jason cold reference",
        reference,
        (
            "Source and Authority Boundary",
            "Fast Selector",
            "Four response modes",
            "Loaded-language dual use",
            "Schema source: empathy, not targeting",
            "Primary Research Calibration",
            *SHADOW_DECISIONS,
        ),
        failures,
    )

    skill = require_file(SKILL, failures)
    validate_skill_inventory(skill, failures)

    context_index = json.loads(require_file(CONTEXT_INDEX, failures) or "{}")
    jason_chunks = [
        chunk
        for chunk in context_index.get("chunks", [])
        if chunk.get("skill") == "jason-fladlien-marketing"
    ]
    jason_index_text = "\n".join(str(chunk.get("content", "")) for chunk in jason_chunks)
    require_terms(
        "Jason context-retrieval index",
        jason_index_text,
        ("Cold Buyer-Psychology Decision Companion", "38 workflow", "Belief", "Choice"),
        failures,
    )

    retriever_path = ROOT / "execution/context_retriever.py"
    retriever_spec = importlib.util.spec_from_file_location(
        "buyer_psych_context_retriever",
        retriever_path,
    )
    if retriever_spec is None or retriever_spec.loader is None:
        failures.append("context retriever could not be loaded")
    else:
        retriever = importlib.util.module_from_spec(retriever_spec)
        retriever_spec.loader.exec_module(retriever)
        results = retriever.retrieve_context(
            "buyer psychology decision layer belief focus recognition choice",
            top_k=8,
        )
        if (
            not results
            or results[0][1].get("skill") != "jason-fladlien-marketing"
            or results[0][1].get("section") != "Cold Buyer-Psychology Decision Companion"
        ):
            failures.append(
                "Jason Cold Buyer-Psychology Decision Companion is not rank 1 for the exact discovery query"
            )

    registry = json.loads(require_file(REGISTRY, failures) or "{}")
    cards = registry.get("cards", [])
    statuses = {item.get("decision"): item.get("status") for item in cards}
    if len(cards) != 13 or any(statuses.get(item) != "SHADOW" for item in SHADOW_DECISIONS):
        failures.append(f"registry SHADOW inventory invalid: {statuses}")
    if any(statuses.get(item) != "CANDIDATE" for item in CANDIDATE_DECISIONS):
        failures.append(f"registry CANDIDATE inventory invalid: {statuses}")

    for path, terms in OWNER_FILES.items():
        content = require_file(path, failures)
        require_terms(str(path.relative_to(ROOT)), content, terms, failures)

    compiler_spec = importlib.util.spec_from_file_location(
        "buyer_psych_situation_compiler",
        COMPILER,
    )
    if compiler_spec is None or compiler_spec.loader is None:
        failures.append("situation compiler could not be loaded")
    else:
        compiler = importlib.util.module_from_spec(compiler_spec)
        compiler_spec.loader.exec_module(compiler)
        allowed = compiler.ALLOWED_NATIVE_OWNERS
        for owner, expected in EXPECTED_RUNTIME_OWNER_DECISIONS.items():
            actual = {
                decision
                for decision, owners in allowed.items()
                if decision in SHADOW_DECISIONS and owner in owners
            }
            if actual != expected:
                failures.append(
                    f"compiler owner decisions for {owner}: expected {sorted(expected)}, got {sorted(actual)}"
                )

    validate_admission(failures)
    deployment = require_file(DEPLOYMENT, failures)
    require_terms(
        "canonical deployment receipt",
        deployment,
        (
            "Google Antigravity",
            "38 workflows",
            "33",
            "8 SHADOW",
            "5 CANDIDATE",
            "5 canonical decision seams",
            "five canonical owner seams",
            "78 adversarial checks",
            "NO EVENT",
            "LOCKED",
            "PARKED",
            "NEXT ACTION",
        ),
        failures,
    )

    for path in FORBIDDEN_RUNTIME_PATHS:
        if path.exists():
            failures.append(f"forbidden promoted runtime surface exists: {path.relative_to(ROOT)}")
    for path in FORBIDDEN_PROMOTION_SURFACES:
        content = require_file(path, failures)
        if "buyer-psychology-decision-intelligence-overlay" in content:
            failures.append(f"overlay promoted into authority/router surface: {path.relative_to(ROOT)}")
    for path in ACTIVE_CORE:
        content = require_file(path, failures)
        if "/Users/farricecain/Codex Antigravity" in content:
            failures.append(f"archived comparison path leaked into active core: {path.relative_to(ROOT)}")

    pointer_paths = overlay_pointer_paths(ROOT)
    if pointer_paths != ALLOWED_OVERLAY_POINTERS:
        failures.append(
            f"overlay pointer surface mismatch: expected {sorted(ALLOWED_OVERLAY_POINTERS)}, got {sorted(pointer_paths)}"
        )
    promotion_hits = promotion_violations(ROOT)
    if promotion_hits:
        failures.append(f"overlay promoted on an active owner surface: {promotion_hits[:5]}")

    provenance_paths = list((DEPLOYMENT.parent).rglob("*"))
    for source_id in SOURCE_IDS:
        provenance_paths.extend((ROOT / "extractions/video-context" / source_id).rglob("*"))
    for path in sorted({path for path in provenance_paths if path.is_file()}):
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if "/Users/farricecain/Codex Antigravity" in content:
            failures.append(f"archived comparison path leaked into provenance: {path.relative_to(ROOT)}")

    if re.search(r"\b27[- ]workflow|## Workflows \(27\)", "\n".join(read(path) for path in ACTIVE_CORE), re.I):
        failures.append("comparison-workspace 27-workflow assumption leaked into active core")

    if failures:
        print("JASON BUYER PSYCHOLOGY OVERLAY VERIFICATION: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("JASON BUYER PSYCHOLOGY OVERLAY VERIFICATION: PASS")
    print(f"- source packages: {len(SOURCE_IDS)}")
    print(f"- canonical owner seams: {len(OWNER_FILES)}")
    print("- decisions: 8 SHADOW + 5 CANDIDATE/DEVELOPMENT_ONLY")
    print("- Jason inventory: 38 workflows + 33 prompts-v2 + 26 compatibility prompts")
    print("- admission surfaces: 97; legacy duplicate evidence weight: 0")
    print("- discovery: Jason Cold Buyer-Psychology Decision Companion ranks first for the exact query")
    print("- mode: SHADOW; no command, agent, router, authority pointer, or mandatory gate")
    for note in notes:
        print(f"- {note}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
