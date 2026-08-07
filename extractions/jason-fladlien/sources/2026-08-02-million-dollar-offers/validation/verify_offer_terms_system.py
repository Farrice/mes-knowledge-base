#!/usr/bin/env python3
"""Structural and integrity verifier for JF-TERMS-2026-08-02.

This verifier does not certify semantic decision quality or market proof.
"""

from __future__ import annotations

import json
import hashlib
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
VALIDATION = Path(__file__).resolve().parent
SOURCE = VALIDATION.parent

failures: list[str] = []
checks = 0


def check(condition: bool, label: str) -> None:
    global checks
    checks += 1
    if not condition:
        failures.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def sha256(relative: str) -> str:
    return hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()


required = [
    "extractions/jason-fladlien/amplification-2026-08-02-offer-terms.md",
    "extractions/jason-fladlien/offer-terms-skill-system-contract.md",
    "extractions/jason-fladlien/sources/2026-08-02-million-dollar-offers/source-receipt.json",
    "extractions/jason-fladlien/sources/2026-08-02-million-dollar-offers/segment-index.jsonl",
    "extractions/jason-fladlien/sources/2026-08-02-million-dollar-offers/visual-context-ledger.md",
    "extractions/jason-fladlien/sources/2026-08-02-million-dollar-offers/uncertainty-report.md",
    "skills/jason-fladlien-marketing/references/offer-terms.md",
    "skills/jason-fladlien-marketing/workflows/offer-terms-diagnostic-and-rebuild.md",
    "skills/jason-fladlien-marketing/workflows/offer-adoption-and-proof-loop.md",
    "skills/jason-fladlien-marketing/references/prompts-v2/offer-terms-diagnostic-and-rebuild.md",
    "skills/jason-fladlien-marketing/references/prompts-v2/offer-adoption-and-proof-loop.md",
    ".agent/workflows/fladlien-terms.md",
    ".claude/commands/fladlien-terms.md",
    "extractions/jason-fladlien/sources/2026-08-02-million-dollar-offers/validation/decision-delta-ledger.md",
    "extractions/jason-fladlien/sources/2026-08-02-million-dollar-offers/validation/blind-review/personal-judge.md",
    "extractions/jason-fladlien/sources/2026-08-02-million-dollar-offers/validation/blind-review/client-judge.md",
    "extractions/jason-fladlien/sources/2026-08-02-million-dollar-offers/validation/blind-review/official-judge.md",
    "extractions/jason-fladlien/sources/2026-08-02-million-dollar-offers/validation/blind-review/mapping-and-suite-verdict.md",
    "extractions/jason-fladlien/sources/2026-08-02-million-dollar-offers/validation/calibration/03-official-patch-label-replay.md",
    "extractions/jason-fladlien/sources/2026-08-02-million-dollar-offers/validation/routing-receipt.md",
    "extractions/jason-fladlien/sources/2026-08-02-million-dollar-offers/validation/regression-receipt.md",
    "extractions/jason-fladlien/sources/2026-08-02-million-dollar-offers/validation/cold-start/03-official-offer-os-pilot-receipt.md",
    "extractions/jason-fladlien/sources/2026-08-02-million-dollar-offers/validation/negative-path/04-no-adoption-trigger-fixture.md",
    "extractions/jason-fladlien/sources/2026-08-02-million-dollar-offers/validation/negative-path/04-no-adoption-trigger-result.md",
    "extractions/jason-fladlien/sources/2026-08-02-million-dollar-offers/validation/run-manifest.json",
]
for relative in required:
    check((ROOT / relative).is_file(), f"missing required file: {relative}")

for group in ("fixtures", "baselines", "enhanced"):
    files = sorted((VALIDATION / group).glob("*.md"))
    check(len(files) == 3, f"{group} must contain exactly 3 markdown cases; found {len(files)}")

receipt = json.loads((SOURCE / "source-receipt.json").read_text(encoding="utf-8"))
check(receipt.get("source_id") == "JF-TERMS-2026-08-02", "source_id mismatch")
check(receipt.get("video_id") == "cEEO2TPpL0U", "video_id mismatch")
check(receipt.get("duration_seconds") == 3187, "duration mismatch")
check(receipt.get("evidence_counts") == {
    "native_caption_segments": 1386,
    "scene_candidates": 501,
    "frames_read": 100,
}, "evidence counts mismatch")
check(receipt.get("working_evidence_hashes") == {
    "video.en-orig.vtt": "94403007e0e03fcca63e8020873703f9fa4b2e1415a58ee81cbcae66d268c85f",
    "video.info.json": "a2adc729cd28538bbc00554f0dd79a56358d4c97bfc46e3c873445da9d5a28e9",
    "video.mp4": "49d520aaed0127074fd9526eaf480256d657f62b0804b4b5a781403715d29541",
}, "working evidence hashes mismatch")

rows = [
    json.loads(line)
    for line in (SOURCE / "segment-index.jsonl").read_text(encoding="utf-8").splitlines()
    if line.strip()
]
check(len(rows) == 19, f"segment index must have framework + 18 levers; found {len(rows)}")
expected = {
    "RAW-R", "RAW-A", "RAW-W",
    "FAT-F", "FAT-A", "FAT-T",
    "HOP-H", "HOP-O", "HOP-P",
    "FAVOR-F", "FAVOR-A", "FAVOR-V", "FAVOR-O", "FAVOR-R",
    "RISE-R", "RISE-I", "RISE-S", "RISE-E",
}
observed = {row["id"] for row in rows if row.get("term") != "Framework"}
check(observed == expected, f"18-lever ID set mismatch: {sorted(observed ^ expected)}")
check(sum(row.get("formula") == "RAW" for row in rows) == 3, "RAW count must be 3")
check(sum(row.get("formula") == "FAT" for row in rows) == 3, "FAT count must be 3")
check(sum(row.get("formula") == "HOP" for row in rows) == 3, "HOP count must be 3")
check(sum(row.get("formula") == "FAVOR" for row in rows) == 5, "FAVOR count must be 5")
check(sum(row.get("formula") == "RISE" for row in rows) == 4, "RISE count must be 4")

forbidden_source_files = []
for path in SOURCE.rglob("*"):
    if not path.is_file():
        continue
    lower = path.name.lower()
    if path.suffix.lower() in {".mp4", ".mov", ".mkv", ".vtt", ".srt", ".png", ".jpg", ".jpeg"}:
        forbidden_source_files.append(path)
    if lower in {"video.info.json", "transcript.txt", "full-transcript.txt"}:
        forbidden_source_files.append(path)
check(not forbidden_source_files, "raw/wholesale source files present: " + ", ".join(map(str, forbidden_source_files)))

reference = read("skills/jason-fladlien-marketing/references/offer-terms.md")
for lever in ("Recover", "Available", "Win", "Feel", "Act", "Thinking", "Habit", "Order", "Process", "Free", "Anchor", "Value", "Outcome", "Resistance", "Relative", "Internal", "Social", "External"):
    check(f"### {lever}" in reference, f"canonical reference missing lever section: {lever}")
for state in ("SUPPORTED", "FRICTION", "BLOCKER", "UNKNOWN"):
    check(state in reference, f"canonical reference missing evidence state: {state}")
for market_state in ("sent", "held", "sold", "collected"):
    check(f"`{market_state}`" in reference, f"canonical reference missing market state: {market_state}")
for phrase in ("Source status", "Offer state", "adaptation_owner", "Antigravity runtime controls", "Change-Class Calibration"):
    check(phrase.lower() in reference.lower(), f"canonical reference missing provenance axis/control: {phrase}")

public_workflow = read("skills/jason-fladlien-marketing/workflows/offer-terms-diagnostic-and-rebuild.md")
for phrase in ("Audit All 18 Levers", "one primary burden", "no more than three", "Cross-Term Non-Regression", "smallest honest change class", "Component validity", "Cold-start portability", "Market proof"):
    check(phrase.lower() in public_workflow.lower(), f"public workflow missing contract phrase: {phrase}")

internal_workflow = read("skills/jason-fladlien-marketing/workflows/offer-adoption-and-proof-loop.md")
for phrase in ("menu_exempt:", "Module Activation Matrix", "NOT APPLICABLE", "remaining change budget", "voluntary sharing", "external reuse"):
    check(phrase.lower() in internal_workflow.lower(), f"internal workflow missing boundary: {phrase}")

front_door = read(".agent/workflows/fladlien-terms.md")
check(".agent/workflows/revenue-offer-agent.md" in front_door, "public wrapper does not load function owner")
check("Revenue Offer Agent separately accepts" in front_door, "public wrapper lacks separate owner acceptance")
check("Framework coverage is not uplift" in front_door, "public wrapper lacks convergence calibration")

revenue = read(".agent/workflows/revenue-offer-agent.md")
game_pos = revenue.find("/fladlien-game-selection")
terms_pos = revenue.find("/fladlien-terms")
package_pos = revenue.find("Package the accepted offer")
check(-1 not in (game_pos, terms_pos, package_pos) and game_pos < terms_pos < package_pos,
      "Revenue Offer Agent order must be game -> TERMS -> package")
check("Prefer `PATCH`" in revenue, "Revenue Offer Agent lacks minimum-change calibration")

anatomy = read("skills/jason-fladlien-marketing/workflows/offer-anatomy-tie-down-architecture.md")
check("energy (fear) > time > money" not in anatomy, "unsupported hard cost ranking remains")
check("No unsupported guarantee or scarcity" in anatomy, "anatomy proof boundary missing")

incomparable = read("skills/jason-fladlien-marketing/workflows/incomparable-offer-architect.md")
check(incomparable.startswith("---\n"), "incomparable offer frontmatter lacks opening delimiter")
check('accepts_context: "Offer TERMS Rebuild Packet"' in incomparable, "incomparable offer TERMS handoff metadata missing")
check("Self-Funding Bonus Present" not in incomparable, "self-funding bonus remains mandatory")
check("China Concierge Move" not in incomparable, "China Concierge remains mandatory")
check("TERMS Non-Regression" in incomparable, "incomparable offer lacks TERMS non-regression")

skill = read("skills/jason-fladlien-marketing/SKILL.md")
check("38 files: 37 public + 1 internal" in skill, "skill workflow count text is stale")
check("33 deterministic practitioner prompts" in skill, "skill v2 prompt count is stale")

prompt_index = json.loads(read(".agent/prompt-index.json"))
prompt_paths = {entry.get("path") for entry in prompt_index.get("entries", [])}
for path in (
    "skills/jason-fladlien-marketing/references/prompts-v2/offer-terms-diagnostic-and-rebuild.md",
    "skills/jason-fladlien-marketing/references/prompts-v2/offer-adoption-and-proof-loop.md",
):
    check(path in prompt_paths, f"prompt index missing: {path}")

for enhanced in sorted((VALIDATION / "enhanced").glob("*.md")):
    text = enhanced.read_text(encoding="utf-8")
    for lever_id in expected:
        check(lever_id in text, f"{enhanced.name} missing source trace {lever_id}")
    check("Market state" in text, f"{enhanced.name} missing market-state verdict")

delta = (VALIDATION / "decision-delta-ledger.md").read_text(encoding="utf-8")
check("Cross-Fixture Verdict" in delta and "Blind-Judge Decision Deltas" in delta,
      "decision-delta ledger missing comparative fields")
check("Blinded material improvement without material regression" in delta,
      "decision-delta acceptance criterion missing")
check("PARTIAL PASS: 2/3" in delta, "decision-delta ledger overstates comparative suite result")

personal_judge = (VALIDATION / "blind-review/personal-judge.md").read_text(encoding="utf-8")
client_judge = (VALIDATION / "blind-review/client-judge.md").read_text(encoding="utf-8")
official_judge = (VALIDATION / "blind-review/official-judge.md").read_text(encoding="utf-8")
check("Cobalt" in personal_judge and "PASS" in personal_judge, "personal blind verdict missing")
check("Orchid" in client_judge and "PASS" in client_judge, "client blind verdict missing")
check("Winner:** Tie" in official_judge and "**FAIL**" in official_judge,
      "official tie/failure boundary missing")

calibration = (VALIDATION / "calibration/03-official-patch-label-replay.md").read_text(encoding="utf-8")
check("**Decision:** `PATCH`" in calibration, "post-judge calibration replay did not emit PATCH")
check("earlier official blind comparison remains a tie" in calibration,
      "calibration replay improperly rewrites comparative verdict")

negative = (VALIDATION / "negative-path/04-no-adoption-trigger-result.md").read_text(encoding="utf-8")
check("NOT TRIGGERED" in negative, "negative path did not stop")
check("Proposed change count:** `0`" in negative, "negative path proposed a change")

manifest_path = VALIDATION / "run-manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.is_file() else {}
for item in manifest.get("artifacts", []):
    relative = item.get("path", "")
    expected_hash = item.get("sha256", "")
    check(bool(relative and expected_hash), "run manifest item missing path or sha256")
    if relative and expected_hash:
        check((ROOT / relative).is_file(), f"run manifest path missing: {relative}")
        if (ROOT / relative).is_file():
            check(sha256(relative) == expected_hash, f"run manifest hash mismatch: {relative}")

check(manifest.get("semantic_behavior_claim") == "independent-human-or-blinded-review-required",
      "run manifest must not let structural checks certify semantic behavior")

if failures:
    print(f"FAIL — {len(failures)} of {checks} checks failed")
    for failure in failures:
        print(f"- {failure}")
    sys.exit(1)

print(f"PASS — {checks} structural/integrity checks passed; semantic behavior requires independent review")
