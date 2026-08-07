#!/usr/bin/env python3
"""Verify the frozen Kyle/Matthew attribution ledger against captured source bytes."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
VIDEO_ID = "UFNlbNa2T4w"
LEDGER_DIR = ROOT / "extractions/kyle-milligan-copywriting"
VIDEO_DIR = ROOT / f"extractions/video-context/{VIDEO_ID}"
LEDGER_PATH = LEDGER_DIR / "speaker-ledger.jsonl"
MANIFEST_PATH = LEDGER_DIR / "speaker-ledger.manifest.json"
SCHEMA_PATH = LEDGER_DIR / "speaker-ledger.schema.json"
HUMAN_PATH = LEDGER_DIR / "source-ledger.md"
SEGMENT_PATH = VIDEO_DIR / "transcript_segments.json"

EXPECTED_WORKFLOWS = {
    "531-swipe-discipline",
    "unique-promise-spine",
    "four-beat-opening-builder",
    "first-four-lines-audit",
    "thumbtack-continuity-audit",
    "proof-texture-dimensionalizer",
    "mumbo-jumbo-pruner",
    "negative-space-copy-chief",
}
MATTHEW_ONLY_HUMAN_ROWS = {
    "H-006", "H-008", "H-013", "H-020", "H-026", "H-044", "H-049", "H-053"
}
COAUTHORED_HUMAN_ROWS = {
    "H-015", "H-028", "H-035", "H-037", "H-040", "H-042", "H-045",
    "H-050", "H-052", "H-054",
}
REQUIRED_SPLITS = {
    "H-001", "H-005", "H-009", "H-015", "H-022", "H-023", "H-025",
    "H-028", "H-031", "H-036", "H-048", "H-049", "H-054", "H-055",
}


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_path(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def load_rows(errors: list[str]) -> list[dict]:
    rows: list[dict] = []
    for line_number, line in enumerate(LEDGER_PATH.read_text().splitlines(), start=1):
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            fail(f"ledger line {line_number} is not valid JSON: {exc}", errors)
    return rows


def human_row_count() -> int:
    text = HUMAN_PATH.read_text()
    table = text.split("## Speaker and Provenance Ledger", 1)[1].split(
        "## Visual Evidence Ledger", 1
    )[0]
    return sum(
        1 for line in table.splitlines()
        if re.match(r"^\| [0-9]{2}:[0-9]{2}:[0-9]{2}", line)
    )


def main() -> int:
    errors: list[str] = []
    for required_path in (LEDGER_PATH, MANIFEST_PATH, SCHEMA_PATH, HUMAN_PATH, SEGMENT_PATH):
        if not required_path.is_file():
            fail(f"missing required file: {required_path.relative_to(ROOT)}", errors)
    if errors:
        print("SOURCE LEDGER: FAIL")
        print("\n".join(f"- {error}" for error in errors))
        return 1

    manifest = json.loads(MANIFEST_PATH.read_text())
    schema = json.loads(SCHEMA_PATH.read_text())
    segments = json.loads(SEGMENT_PATH.read_text())
    rows = load_rows(errors)

    if manifest.get("status") != "FROZEN":
        fail("manifest status must be FROZEN", errors)
    if manifest.get("source_video_id") != VIDEO_ID:
        fail("manifest video ID mismatch", errors)
    if manifest.get("source_segment_count") != 2915 or len(segments) != 2915:
        fail("source segment count must remain 2,915", errors)
    if manifest.get("human_ledger_row_count") != 55 or human_row_count() != 55:
        fail("readable ledger must contain exactly 55 reviewed rows", errors)
    if manifest.get("machine_ledger_row_count") != len(rows) or len(rows) < 55:
        fail("machine row count is missing or inconsistent", errors)
    if set(manifest.get("atomic_split_human_rows", [])) != REQUIRED_SPLITS:
        fail("atomic split inventory drifted", errors)
    if manifest.get("schema_sha256") != sha256_path(SCHEMA_PATH):
        fail("schema hash does not match manifest", errors)
    if manifest.get("ledger_sha256") != sha256_path(LEDGER_PATH):
        fail("ledger hash does not match manifest", errors)
    for relative, expected in manifest.get("source_hashes", {}).items():
        path = ROOT / relative
        if not path.is_file() or sha256_path(path) != expected:
            fail(f"frozen source hash mismatch: {relative}", errors)

    required_fields = set(schema.get("required", []))
    allowed_fields = set(schema.get("properties", {}))
    row_ids: list[str] = []
    covered_human_ids: list[str] = []
    workflow_coverage: Counter[str] = Counter()
    truth_coverage: Counter[str] = Counter()
    rows_by_human: dict[str, list[dict]] = {}

    for expected_index, row in enumerate(rows, start=1):
        row_id = row.get("row_id", "<missing>")
        expected_id = f"SL-{expected_index:03d}"
        if row_id != expected_id:
            fail(f"row order mismatch: expected {expected_id}, found {row_id}", errors)
        row_ids.append(row_id)
        missing = required_fields - set(row)
        extra = set(row) - allowed_fields
        if missing:
            fail(f"{row_id}: missing fields {sorted(missing)}", errors)
        if extra:
            fail(f"{row_id}: unexpected fields {sorted(extra)}", errors)
        if row.get("source_video_id") != VIDEO_ID:
            fail(f"{row_id}: wrong source video", errors)
        if row.get("review_status") != "HUMAN_REVIEWED":
            fail(f"{row_id}: row is not human reviewed", errors)

        human_ids = row.get("human_ledger_row_ids", [])
        if len(human_ids) != 1:
            fail(f"{row_id}: v1 rows must resolve to exactly one readable-ledger row", errors)
        for human_id in human_ids:
            covered_human_ids.append(human_id)
            rows_by_human.setdefault(human_id, []).append(row)

        truth = row.get("truth_class")
        truth_coverage[truth] += 1
        if truth in {"SELF_REPORTED", "ILLUSTRATIVE", "THIRD_PARTY"}:
            forbidden = set(row.get("forbidden_uses", []))
            if "offer_proof" not in forbidden:
                fail(f"{row_id}: {truth} evidence must forbid offer_proof", errors)
        if truth == "SELF_REPORTED" and "role_credential" not in row.get("forbidden_uses", []):
            fail(f"{row_id}: self-reported evidence must forbid role_credential", errors)
        if row.get("speaker_class") == "UNRESOLVED" and "method_grounding" in row.get("permitted_uses", []):
            fail(f"{row_id}: unresolved attribution cannot ground doctrine", errors)

        for target in row.get("workflow_targets", []):
            workflow_coverage[target] += 1

        refs = row.get("source_refs", [])
        if len(refs) != 1:
            fail(f"{row_id}: expected exactly one source reference", errors)
            continue
        ref = refs[0]
        source_kind = row.get("source_kind")
        if source_kind == "SPOKEN":
            required_ref = {
                "source_path", "source_sha256", "start_segment_index", "end_segment_index",
                "start_segment_id", "end_segment_id", "requested_start_ms", "requested_end_ms",
                "segment_start_ms", "segment_end_ms", "normalized_excerpt", "excerpt_sha256",
            }
            if not required_ref.issubset(ref):
                fail(f"{row_id}: incomplete spoken-source reference", errors)
                continue
            first, last = ref["start_segment_index"], ref["end_segment_index"]
            if not (0 <= first <= last < len(segments)):
                fail(f"{row_id}: invalid segment bounds", errors)
                continue
            if ref["start_segment_id"] != f"{VIDEO_ID}:s{first:06d}":
                fail(f"{row_id}: start segment ID is not the zero-based derived ID", errors)
            if ref["end_segment_id"] != f"{VIDEO_ID}:s{last:06d}":
                fail(f"{row_id}: end segment ID is not the zero-based derived ID", errors)
            excerpt = " ".join(segments[index]["text"].strip() for index in range(first, last + 1)).strip()
            if excerpt != ref["normalized_excerpt"]:
                fail(f"{row_id}: excerpt does not reproduce from segment text", errors)
            if sha256_bytes(excerpt.encode()) != ref["excerpt_sha256"]:
                fail(f"{row_id}: excerpt hash mismatch", errors)
            if ref["source_sha256"] != sha256_path(ROOT / ref["source_path"]):
                fail(f"{row_id}: source byte hash mismatch", errors)
            if ref["segment_end_ms"] <= ref["requested_start_ms"]:
                fail(f"{row_id}: cited segments do not overlap requested start", errors)
            if ref["segment_start_ms"] >= max(ref["requested_end_ms"], ref["requested_start_ms"] + 1):
                fail(f"{row_id}: cited segments do not overlap requested end", errors)
        elif source_kind == "VISUAL":
            required_ref = {"frame_path", "frame_sha256", "timestamp_ms"}
            if set(ref) != required_ref:
                fail(f"{row_id}: visual reference must contain only frame path/hash/timestamp", errors)
                continue
            frame_path = ROOT / ref["frame_path"]
            if not frame_path.is_file() or sha256_path(frame_path) != ref["frame_sha256"]:
                fail(f"{row_id}: visual frame is missing or changed", errors)
            if row.get("speaker_class") != "VISUAL" or row.get("claim_kind") != "VISUAL":
                fail(f"{row_id}: visual row has a spoken attribution", errors)
        elif source_kind == "SYNTHESIS":
            if truth != "INFERRED" or not ref.get("anchor_row_ids"):
                fail(f"{row_id}: synthesis must be inferred and anchored", errors)
        else:
            fail(f"{row_id}: unknown source kind {source_kind}", errors)

    if len(row_ids) != len(set(row_ids)):
        fail("machine row IDs are not unique", errors)
    expected_human = {f"H-{index:03d}" for index in range(1, 56)}
    if set(covered_human_ids) != expected_human:
        fail("machine ledger does not cover exactly H-001 through H-055", errors)
    for human_id in REQUIRED_SPLITS:
        truth_classes = {row["truth_class"] for row in rows_by_human.get(human_id, [])}
        if len(truth_classes) < 2:
            fail(f"{human_id}: required atomic truth split is absent", errors)
    for human_id in MATTHEW_ONLY_HUMAN_ROWS:
        if {row["speaker_class"] for row in rows_by_human.get(human_id, [])} != {"MATTHEW"}:
            fail(f"{human_id}: Matthew-only attribution drifted", errors)
    for human_id in COAUTHORED_HUMAN_ROWS:
        if {row["speaker_class"] for row in rows_by_human.get(human_id, [])} != {"CO_AUTHORED"}:
            fail(f"{human_id}: co-authored attribution drifted", errors)
    if EXPECTED_WORKFLOWS - set(workflow_coverage):
        fail(f"workflow source coverage missing: {sorted(EXPECTED_WORKFLOWS - set(workflow_coverage))}", errors)
    if truth_coverage["OBSERVED"] < 1 or truth_coverage["SELF_REPORTED"] < 1 or truth_coverage["ILLUSTRATIVE"] < 1:
        fail("truth-class partition is incomplete", errors)

    if errors:
        print("SOURCE LEDGER: FAIL")
        print("\n".join(f"- {error}" for error in errors))
        return 1

    print("SOURCE LEDGER: PASS")
    print(f"- readable rows: 55")
    print(f"- atomic machine rows: {len(rows)}")
    print(f"- spoken/visual: {sum(r['source_kind'] == 'SPOKEN' for r in rows)}/{sum(r['source_kind'] == 'VISUAL' for r in rows)}")
    print(f"- truth classes: {dict(sorted(truth_coverage.items()))}")
    print(f"- workflow anchors: {dict(sorted((k, v) for k, v in workflow_coverage.items() if k in EXPECTED_WORKFLOWS))}")
    print("- boundary: attribution/source trace only; no behavior, embodiment, or market proof")
    return 0


if __name__ == "__main__":
    sys.exit(main())
