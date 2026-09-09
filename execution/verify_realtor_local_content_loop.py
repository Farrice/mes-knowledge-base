#!/usr/bin/env python3
"""Connected proof and sabotage suite for the Realtor Local-Signal system."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

from realtor_local_signal_engine import (  # noqa: E402
    evaluate_signal,
    rank_signals,
    validate_content_card,
)


RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    RESULTS.append((name, bool(condition), detail))


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def agent(name: str, market: str, target: str, comfort: str, capacity: int) -> dict[str, object]:
    return {
        "name": name,
        "market": market,
        "niche": "residential real estate",
        "target_person": target,
        "voice_markers": ["specific", "plainspoken"],
        "genuine_interests": ["local life", "practical decisions"],
        "production_comfort": comfort,
        "max_posts_per_week": capacity,
        "offer": "a useful planning conversation",
        "compliance_boundaries": ["fair housing", "source current local claims"],
    }


def signal(
    signal_id: str,
    market: str,
    *,
    source_type: str = "local_source",
    target: str = "one plausible local person",
    source: str = "fixture://verified-local-source",
    evidence: str = "SYNTHETIC",
    transfer: str = "topic_and_format",
    pov: str = "This is the agent's supported local interpretation.",
    fit: bool = True,
    voice: bool = True,
    scores: tuple[int, int, int, int, int] = (2, 2, 2, 2, 2),
    **extra: object,
) -> dict[str, object]:
    row: dict[str, object] = {
        "id": signal_id,
        "title": signal_id.replace("-", " "),
        "source_type": source_type,
        "source": source,
        "evidence_status": evidence,
        "market": market,
        "target_person": target,
        "transfer_scope": transfer,
        "original_pov": pov,
        "supported_by_agent_fit": fit,
        "voice_match": voice,
        "score_inputs": dict(
            zip(
                (
                    "local_specificity",
                    "audience_relevance",
                    "creator_conviction",
                    "conversation_potential",
                    "production_fit",
                ),
                scores,
            )
        ),
    }
    row.update(extra)
    return row


def valid_card(name: str, cadence: str = "2/week") -> dict[str, object]:
    return {
        "title": name,
        "target_person": "a specific local buyer",
        "recognizable_tension": "The person has a concrete local decision to make.",
        "source": "fixture://verified-local-source",
        "evidence_status": "SYNTHETIC",
        "original_pov": "A supported agent observation.",
        "hook": "A specific local thesis.",
        "beat_map": ["signal", "meaning", "next check"],
        "visual_plan": "Voiceover over local footage.",
        "cta": "Ask for the source checklist.",
        "human_response_path": "Agent sends it and asks one relevant question.",
        "real_estate_memory": "Shows how to evaluate location fit.",
        "attention_metrics": ["local_reach", "saves", "shares"],
        "pipeline_metrics": ["qualified_conversations", "appointments", "collected_revenue"],
        "voice_approved": True,
        "cadence": cadence,
    }


# Connected file surface.
source_files = (
    "extractions/video-context/eDGyKfiXsyQ/metadata.json",
    "extractions/video-context/eDGyKfiXsyQ/transcript.vtt",
    "extractions/video-context/eDGyKfiXsyQ/transcript.txt",
    "extractions/video-context/eDGyKfiXsyQ/transcript_segments.json",
    "extractions/video-context/eDGyKfiXsyQ/video-context-ledger.md",
    "extractions/video-context/eDGyKfiXsyQ/video-context-ledger.json",
    "extractions/video-context/eDGyKfiXsyQ/frame-notes.md",
    "extractions/video-context/eDGyKfiXsyQ/uncertainty-report.md",
    "extractions/video-context/eDGyKfiXsyQ/analysis.md",
    "extractions/video-context/eDGyKfiXsyQ/source-to-skill-brief.md",
    "extractions/video-context/eDGyKfiXsyQ/skill-system-contract.md",
)
missing = [path for path in source_files if not (ROOT / path).is_file()]
check("source package files", not missing, ", ".join(missing))
check(
    "visual evidence preserved",
    len(list((ROOT / "extractions/video-context/eDGyKfiXsyQ/frames").glob("*.jpg"))) == 25,
    "expected 25 locally inspected frames",
)

workflow_path = "skills/enrico-incarnati-instagram-realestate/workflows/11-local-signal-content-loop.md"
prompt_path = "skills/enrico-incarnati-instagram-realestate/references/prompts-v2/local-signal-content-loop.md"
workflow = read(workflow_path)
prompt = read(prompt_path)
skill = read("skills/enrico-incarnati-instagram-realestate/SKILL.md")
check(
    "workflow contract is complete",
    all(
        token in workflow
        for token in (
            "Agent Fit Card",
            "Signal Pack",
            "Hard rejection",
            "Qualified-local-attention score",
            "Local Content Cards",
            "Voice and compliance checkpoint",
            "Conversation bridge",
            "Learning receipt",
        )
    ),
)
check(
    "prompt-v2 execution layer",
    all(
        token in prompt
        for token in (
            "## Role & Activation",
            "## Input Required",
            "## Execution Protocol",
            "## Output Contract",
            "## Output Skeleton",
            "## Quality Gate",
            "## Deploy When",
        )
    ),
)
check("Enrico owner registers connected workflow", "/enrico-local-signal-loop" in skill)

bridges = (
    ".agent/workflows/enrico-local-signal-loop.md",
    ".claude/commands/enrico-local-signal-loop.md",
    ".agents/skills/source-command-enrico-local-signal-loop/SKILL.md",
)
check("all three command bridges", all((ROOT / path).is_file() for path in bridges))

product_files = (
    "_active/products/realtor-content-pack/04-deliverables/month-01-pack/07-LOCAL-SIGNAL-PLAYBOOK.md",
    "_active/products/realtor-content-pack/04-deliverables/month-01-pack/07-LOCAL-SIGNAL-PLAYBOOK.metadata.json",
    "_active/products/realtor-content-pack/06-research/2026-09-01-local-signal-behavior-proof.md",
    "_active/products/realtor-content-pack/06-research/2026-09-01-local-signal-behavior-proof.metadata.json",
)
check("product playbook and proof files", all((ROOT / path).is_file() for path in product_files))

proof = read(product_files[2])
cards = re.findall(r"^## Card \d+:", proof, re.MULTILINE)
check("nine-card behavior proof", len(cards) == 9, f"found={len(cards)}")
negative_tokens = (
    "verbatim_imitation",
    "unsourced_factual_claim",
    "fair_housing_steering",
    "wrong_market_or_audience",
    "artificial_opinion",
    "cta_without_human_response_path",
    "lifestyle_without_real_estate_memory",
    "forced_daily_cadence",
)
check("eight explicit negative-control receipts", all(token in proof for token in negative_tokens))
check(
    "product proof preserves evidence boundary",
    all(token in proof for token in ("NO EVENT", "UNCONFIRMED", "Attention metrics", "Pipeline metrics")),
)
check(
    "Listing Launch remains flagship",
    "Listing Launch System remains the flagship"
    in read("_active/products/realtor-content-pack/04-deliverables/month-01-pack/00-PACK-GUIDE.md"),
)

# Positive selection behavior across three profiles.
jen = agent("Jen", "San Fernando Valley and Los Angeles", "a local luxury buyer or seller", "mixed", 3)
avery = agent("Avery", "Northfield Junction", "a first-time buyer comparing practical tradeoffs", "faceless", 2)
marco = agent("Marco", "Harbor City", "an urban relocation prospect", "talking-head and green-screen", 4)

positive_profiles = {
    "Jen": (
        jen,
        signal("jen-private-arrival", "San Fernando Valley and Los Angeles", source_type="lived_observation"),
    ),
    "Avery": (avery, signal("avery-route-8", "Northfield Junction")),
    "Marco": (marco, signal("marco-night-market", "Harbor City")),
}
for profile, (fit_card, candidate) in positive_profiles.items():
    result = evaluate_signal(fit_card, candidate)
    check(f"{profile} qualified signal accepted", result["accepted"] and result["score"] == 10, str(result))

# Rank order and tie-break behavior.
ranking = rank_signals(
    avery,
    [
        signal("easy-but-flat", "Northfield Junction", scores=(2, 2, 1, 2, 2)),
        signal("conviction-wins", "Northfield Junction", scores=(2, 2, 2, 1, 2)),
        signal("lower-total", "Northfield Junction", scores=(2, 1, 2, 1, 2)),
    ],
)
check(
    "ranking uses total then conviction",
    [row["id"] for row in ranking["accepted"]] == ["conviction-wins", "easy-but-flat", "lower-total"],
    repr([row["id"] for row in ranking["accepted"]]),
)

# Signal-level sabotage controls.
sabotage = {
    "verbatim_imitation": signal(
        "copied-competitor",
        "Northfield Junction",
        transfer="verbatim",
        copied_language=True,
    ),
    "unsourced_factual_claim": signal(
        "unsourced-value-claim",
        "Northfield Junction",
        source="",
        evidence="UNCONFIRMED",
        claim="This project will raise nearby values 12%.",
    ),
    "fair_housing_steering": signal(
        "steering-copy",
        "Northfield Junction",
        draft_language="The perfect safe neighborhood for young families.",
    ),
    "wrong_market_or_audience": signal(
        "foreign-mansion",
        "Foreign Viral Market",
        reach_evidence="10M views",
    ),
    "artificial_opinion": signal(
        "invented-rage",
        "Northfield Junction",
        fit=False,
        scores=(2, 2, 0, 2, 2),
    ),
    "generic_or_unapproved_voice": signal(
        "generic-ai",
        "Northfield Junction",
        pov="",
        voice=False,
    ),
    "missing_target_person": signal(
        "nobody-specific",
        "Northfield Junction",
        target="",
    ),
}
for reason, candidate in sabotage.items():
    receipt = evaluate_signal(avery, candidate)
    check(
        f"rejects {reason}",
        not receipt["accepted"] and reason in receipt["rejection_reasons"],
        str(receipt["rejection_reasons"]),
    )

format_only = signal(
    "foreign-format-localized",
    "Foreign Viral Market",
    source_type="format_reference",
    transfer="format_only",
    localized_market="Northfield Junction",
    source="https://example.invalid/format-reference",
    evidence="UNCONFIRMED",
    reach_evidence="public proxy only",
)
format_receipt = evaluate_signal(avery, format_only)
check("format-only transfer can survive after localization", format_receipt["accepted"], str(format_receipt))

# Card-level sabotage controls and a valid control.
good_card = valid_card("A sourced local route explainer")
check("complete Local Content Card passes", not validate_content_card(avery, good_card))

missing_response = valid_card("CTA without owner")
missing_response["human_response_path"] = ""
check(
    "rejects CTA without human response path",
    "cta_without_human_response_path" in validate_content_card(avery, missing_response),
)

no_real_estate_memory = valid_card("Lifestyle with no Realtor relevance")
no_real_estate_memory["real_estate_memory"] = ""
check(
    "rejects lifestyle without real-estate memory",
    "lifestyle_without_real_estate_memory" in validate_content_card(avery, no_real_estate_memory),
)

forced_daily = valid_card("Forced daily calendar", cadence="daily")
check(
    "rejects forced daily cadence",
    "forced_daily_cadence" in validate_content_card(avery, forced_daily),
)

overlap_card = valid_card("Views are not leads")
overlap_card["pipeline_metrics"] = ["local_reach", "appointments"]
check(
    "rejects attention and pipeline overlap",
    "attention_pipeline_metric_overlap" in validate_content_card(avery, overlap_card),
)

# False-green controls: malformed input and a broken source package must fail.
bad_signal = signal("bad-score", "Northfield Junction")
bad_signal["score_inputs"]["production_fit"] = 3  # type: ignore[index]
bad_receipt = evaluate_signal(avery, bad_signal)
check("rejects out-of-range score", "invalid_score:production_fit" in bad_receipt["rejection_reasons"])

with tempfile.TemporaryDirectory(prefix="realtor-local-signal-proof-") as raw:
    payload = Path(raw) / "payload.json"
    payload.write_text(json.dumps({"agent": avery, "signals": [positive_profiles["Avery"][1]]}), encoding="utf-8")
    completed = subprocess.run(
        [sys.executable, "execution/realtor_local_signal_engine.py", str(payload)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    check(
        "cold-start CLI emits ranked JSON",
        completed.returncode == 0 and '"accepted"' in completed.stdout and '"rejected"' in completed.stdout,
        completed.stderr.strip(),
    )

source_check = subprocess.run(
    [sys.executable, "execution/verify_video_context_source_package.py", "extractions/video-context/eDGyKfiXsyQ"],
    cwd=ROOT,
    text=True,
    capture_output=True,
    check=False,
)
check(
    "video source package verifier",
    source_check.returncode == 0 and "Video context source package: PASS" in source_check.stdout,
    source_check.stdout.strip().splitlines()[0] if source_check.stdout else source_check.stderr.strip(),
)

failed = [row for row in RESULTS if not row[1]]
for name, ok, detail in RESULTS:
    suffix = f"  [{detail}]" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'}  {name}{suffix}")

print(f"\nRealtor Local-Signal Content System: {'PASS' if not failed else 'FAIL'} " f"({len(RESULTS) - len(failed)}/{len(RESULTS)} checks)")
raise SystemExit(1 if failed else 0)
