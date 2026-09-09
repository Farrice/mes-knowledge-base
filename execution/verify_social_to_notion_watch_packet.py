#!/usr/bin/env python3
"""Deterministic, offline verifier for /watch -> Social Intelligence wiring."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import math
import sys
import tempfile
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

BASE = Path(__file__).parent.parent
sys.path.insert(0, str(BASE))

from execution.notion_api import NotionAPI  # noqa: E402
from execution import social_to_notion as bridge  # noqa: E402


VIDEO_ID = "HH6QqWyXJu8"
CANONICAL_URL = f"https://www.youtube.com/watch?v={VIDEO_ID}"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def make_packet(
    root: Path,
    url: str = f"https://youtu.be/{VIDEO_ID}?t=103",
    *,
    captured: int = 2,
    duration: float = 738.0,
    published="20260102",
    canonical_url: str | None = CANONICAL_URL,
    stem: str = "base",
) -> dict:
    """Build the same content-bound integrity shape emitted by /watch."""
    artifact_dir = root / stem
    artifact_dir.mkdir(parents=True, exist_ok=True)
    frames = []
    ocr_rows = []
    alignment_rows = []
    segment_count = max(captured, 2)
    segments = [
        {
            "start": float(index * 10),
            "end": float(index * 10 + 2),
            "text": (
                "First spoken line" if index == 0 else
                "Second spoken line" if index == 1 else
                f"Spoken line {index}"
            ),
        }
        for index in range(segment_count)
    ]
    for index in range(captured):
        frame_path = artifact_dir / f"frame_{index:04d}.jpg"
        frame_path.write_bytes(f"deterministic-frame-{stem}-{index}".encode())
        timestamp = float(index * 10)
        digest = sha256_file(frame_path)
        frame = {
            "path": str(frame_path),
            "timestamp_seconds": timestamp,
            "reason": "scene",
            "width": 1024,
            "height": 576,
            "sha256": digest,
        }
        ocr = {
            "path": str(frame_path),
            "timestamp_seconds": timestamp,
            "status": "pass",
            "text": f"SCREEN {index}",
        }
        frames.append(frame)
        ocr_rows.append(ocr)
        alignment_rows.append({
            **frame,
            "ocr": ocr,
            "transcript": [segments[index]],
            "review_status": "not_inspected",
            "alignment_method": "overlap",
            "alignment_distance_seconds": 0.0,
        })

    source_identity = canonical_url if canonical_url else "sha256:" + "c" * 64
    source_content_sha256 = None if canonical_url else "c" * 64
    capture = {
        "detail": "balanced",
        "resolution": 1024,
        "frame_strategy": "scene-aware",
        "ocr_requested": True,
    }
    transcript_text = "\n".join(
        f"[{int(row['start']) // 60:02d}:{int(row['start']) % 60:02d}] {row['text']}"
        for row in segments
    )
    packet = {
        "schema_version": bridge.WATCH_PACKET_SCHEMA,
        "source": {
            "original": url,
            "kind": "url" if canonical_url else "local",
            "id": VIDEO_ID if canonical_url else None,
            "identity": source_identity,
            "content_sha256": source_content_sha256,
            "title": "Test Video",
            "uploader": "Test Creator",
            "published": published,
            "canonical_url": canonical_url,
        },
        "scope": {"duration_seconds": duration, "duration_basis": "media_metadata"},
        "capture": capture,
        "acquisition": {
            "visual_source": "storyboard",
            "direct_media": {"status": "fail", "reason": "http_403"},
        },
        "transcript": {
            "status": "pass",
            "source": "native captions",
            "segment_count": len(segments),
            "segments": segments,
            "text": transcript_text,
        },
        "visual": {
            "status": "captured_unreviewed" if captured else "unavailable",
            "evidence_label": "VISUALS_EXTRACTED_NOT_INSPECTED" if captured else "TRANSCRIPT_ONLY",
            "captured_count": captured,
            "reviewed_count": 0,
            "engine": "storyboard",
            "candidate_count": captured,
            "frames": frames,
        },
        "ocr": {
            "status": "pass" if captured else "skipped",
            "reason": None if captured else "ocr_not_requested",
            "attempted": captured,
            "succeeded": captured,
            "nonempty": captured,
            "failed": 0,
            "rows": ocr_rows,
        },
        "alignment": {"frames": alignment_rows},
        "catalog": {"topics": ["AI Agents", "Claude"]},
        "limitations": ["sparse storyboard coverage"],
    }
    basis = {
        "schema_version": "watch-capture-integrity/v1",
        "source_identity": source_identity,
        "source_content_sha256": source_content_sha256,
        "source_metadata": bridge._source_integrity_metadata(packet["source"]),
        "scope": packet["scope"],
        "capture_config": capture,
        "transcript_sha256": bridge._json_sha256(segments),
        "transcript_text_sha256": bridge._json_sha256(transcript_text),
        "transcript_meta_sha256": bridge._json_sha256(
            bridge._transcript_meta_integrity(packet["transcript"])
        ),
        "frames": bridge._frame_integrity_rows(frames),
        "ocr_sha256": bridge._json_sha256(bridge._ocr_integrity_rows(ocr_rows)),
        "ocr_meta_sha256": bridge._json_sha256(bridge._ocr_meta_integrity(packet["ocr"])),
        "alignment_sha256": bridge._json_sha256(bridge._alignment_integrity_rows(alignment_rows)),
        "visual_source": "storyboard",
        "visual_meta_sha256": bridge._json_sha256(
            bridge._visual_meta_integrity(packet["visual"])
        ),
        "direct_media_sha256": bridge._json_sha256(
            bridge._direct_media_integrity(packet["acquisition"])
        ),
        "limitations_sha256": bridge._json_sha256(packet["limitations"]),
    }
    fingerprint = bridge._json_sha256(basis)
    packet["integrity"] = {"algorithm": "sha256", "basis": basis}
    packet["fingerprint"] = fingerprint
    packet["packet_id"] = f"watch:{VIDEO_ID}:{fingerprint[:16]}"
    return packet


def make_receipt(packet: dict, *, state: str = "PARTIAL_VISUAL_VERIFIED") -> dict:
    reviewed_frames = [
        {
            "path": row["path"],
            "timestamp_seconds": row["timestamp_seconds"],
            "sha256": row["sha256"],
            "observation": f"Reviewed scene {index}",
        }
        for index, row in enumerate(packet["visual"]["frames"])
    ]
    return {
        "schema_version": bridge.WATCH_RECEIPT_SCHEMA,
        "source_id": packet["source"]["id"],
        "packet_fingerprint": packet["fingerprint"],
        "captured_count": len(packet["visual"]["frames"]),
        "reviewed_count": len(reviewed_frames),
        "review_state": state,
        "coverage_limit": "storyboard samples only",
        "reviewed_frames": reviewed_frames,
    }


class FakeNotion:
    title = staticmethod(NotionAPI.title)
    rich_text = staticmethod(NotionAPI.rich_text)
    select = staticmethod(NotionAPI.select)
    multi_select = staticmethod(NotionAPI.multi_select)
    number = staticmethod(NotionAPI.number)
    date = staticmethod(NotionAPI.date)
    checkbox = staticmethod(NotionAPI.checkbox)
    heading2 = staticmethod(NotionAPI.heading2)
    para = staticmethod(NotionAPI.para)
    bullet = staticmethod(NotionAPI.bullet)

    def __init__(
        self,
        results=None,
        query_error: Exception | None = None,
        *,
        fail_update_once: bool = False,
    ):
        self.results = list(results or [])
        self.query_error = query_error
        self.fail_update_once = fail_update_once
        self.query_calls = []
        self.schema_calls = []
        self.create_calls = []
        self.update_calls = []
        self.append_calls = []
        self.events = []
        self.blocks: dict[str, list[dict]] = {}

    def _ensure_properties(self, database_id, required):
        self.events.append("schema")
        self.schema_calls.append((database_id, required))
        return set(required)

    def query_database(self, database_id, filter=None, sorts=None, page_size=100):
        self.events.append("query")
        self.query_calls.append((database_id, filter, page_size))
        if self.query_error:
            raise self.query_error
        return {"results": self.results}

    def create_page(self, database_id, properties, children=None):
        self.events.append("create")
        self.create_calls.append((database_id, properties, children or []))
        self.blocks["new-page"] = list(children or [])
        return {"id": "new-page", "url": "https://notion.so/new-page"}

    def update_page(self, page_id, properties):
        self.events.append("update")
        self.update_calls.append((page_id, properties))
        if self.fail_update_once:
            self.fail_update_once = False
            raise RuntimeError("simulated property update failure")
        return {"id": page_id}

    def list_block_children(self, block_id, start_cursor=None, page_size=100):
        rows = self.blocks.get(block_id, [])
        start = int(start_cursor or 0)
        page = rows[start:start + page_size]
        next_index = start + len(page)
        return {
            "results": page,
            "has_more": next_index < len(rows),
            "next_cursor": str(next_index) if next_index < len(rows) else None,
        }

    def _request(self, method, path, body=None):
        self.events.append("append")
        self.append_calls.append((method, path, body or {}))
        page_id = path.split("/")[2]
        self.blocks.setdefault(page_id, []).extend((body or {}).get("children") or [])
        return {"ok": True}


def notion_page(
    watch_fingerprint: str,
    page_id: str = "existing",
    *,
    batch: str = "riley:human-owned-batch",
    extract_candidate: bool = True,
) -> dict:
    return {
        "id": page_id,
        "url": f"https://notion.so/{page_id}",
        "properties": {
            "Watch Fingerprint": NotionAPI.rich_text(watch_fingerprint),
            "Batch": NotionAPI.rich_text(batch),
            "Extract Candidate": NotionAPI.checkbox(extract_candidate),
        },
    }


def expect_error(fn, contains: str) -> None:
    try:
        fn()
    except Exception as exc:
        assert contains in str(exc), str(exc)
    else:
        raise AssertionError(f"expected error containing {contains!r}")


def run_main(argv: list[str]) -> tuple[int, str]:
    stdout = io.StringIO()
    with mock.patch.object(sys, "argv", argv), contextlib.redirect_stdout(stdout):
        try:
            bridge.main()
        except SystemExit as exc:
            return int(exc.code or 0), stdout.getvalue()
    return 0, stdout.getvalue()


def main() -> int:
    variants = [
        f"https://youtu.be/{VIDEO_ID}?t=103",
        f"https://www.youtube.com/watch?v={VIDEO_ID}&t=103",
        f"https://youtube.com/shorts/{VIDEO_ID}?feature=share",
        f"https://youtube.com/embed/{VIDEO_ID}#fragment",
    ]
    assert {bridge.canonical_post_url(url) for url in variants} == {CANONICAL_URL}
    assert bridge.normalize_published_date(20260102) == "2026-01-02"
    assert bridge.normalize_published_date("20261340") is None
    assert bridge.normalize_published_date("2026-02-30") is None
    expect_error(
        lambda: bridge.canonical_post_url("https://facebook.com/watch?v=A"),
        "YouTube video URLs only",
    )

    with tempfile.TemporaryDirectory(prefix="watch-notion-verify-") as tmp:
        root = Path(tmp)
        base_packet = make_packet(root, stem="base")
        bridge.validate_watch_packet(base_packet)
        unreviewed = bridge.watch_packet_to_record(
            base_packet, topics="Claude, Video Analysis, claude"
        )
        assert unreviewed["url"] == CANONICAL_URL
        assert unreviewed["evidence_state"] == "VISUAL_CAPTURED_UNREVIEWED"
        assert unreviewed["topics"] == ["AI Agents", "Claude", "Video Analysis"]
        assert unreviewed["hook"] == "First spoken line"
        assert unreviewed["published"] == "2026-01-02"

        receipt = make_receipt(base_packet)
        reviewed = bridge.watch_packet_to_record(base_packet, inspection_receipt=receipt)
        assert reviewed["evidence_state"] == "PARTIAL_VISUAL_VERIFIED"
        assert reviewed["timeline"][0]["review_observation"] == "Reviewed scene 0"
        assert reviewed["sync_fingerprint"] != unreviewed["sync_fingerprint"]
        topic_change = bridge.watch_packet_to_record(
            base_packet, topics="New Topic", inspection_receipt=receipt
        )
        assert topic_change["sync_fingerprint"] != reviewed["sync_fingerprint"]

        empty_receipt = {**receipt, "reviewed_frames": []}
        expect_error(
            lambda: bridge.watch_packet_to_record(base_packet, inspection_receipt=empty_receipt),
            "reviewed_count does not match",
        )
        duplicate_receipt = {**receipt, "reviewed_frames": [receipt["reviewed_frames"][0]] * 2}
        expect_error(
            lambda: bridge.watch_packet_to_record(base_packet, inspection_receipt=duplicate_receipt),
            "unmapped or duplicate",
        )
        unmapped_receipt = json.loads(json.dumps(receipt))
        unmapped_receipt["reviewed_frames"][0]["sha256"] = "f" * 64
        expect_error(
            lambda: bridge.watch_packet_to_record(base_packet, inspection_receipt=unmapped_receipt),
            "unmapped or duplicate",
        )
        blank_receipt = json.loads(json.dumps(receipt))
        blank_receipt["reviewed_frames"][0]["observation"] = " "
        expect_error(
            lambda: bridge.watch_packet_to_record(base_packet, inspection_receipt=blank_receipt),
            "nonblank observation",
        )
        full_storyboard_receipt = make_receipt(base_packet, state="VISUAL_VERIFIED")
        expect_error(
            lambda: bridge.watch_packet_to_record(
                base_packet, inspection_receipt=full_storyboard_receipt
            ),
            "storyboard evidence cannot be promoted",
        )

        receipt_path = root / "receipt.json"
        receipt_path.write_text(json.dumps(receipt), encoding="utf-8")
        assert bridge.load_inspection_receipt(receipt_path, base_packet)["review_state"] == "PARTIAL_VISUAL_VERIFIED"

        count_mismatch = json.loads(json.dumps(base_packet))
        count_mismatch["visual"]["captured_count"] += 1
        expect_error(
            lambda: bridge.validate_watch_packet(count_mismatch),
            "captured_count does not match",
        )
        mutation_packet = make_packet(root, stem="mutation")
        Path(mutation_packet["visual"]["frames"][0]["path"]).write_bytes(b"changed pixels")
        expect_error(
            lambda: bridge.validate_watch_packet(mutation_packet),
            "missing or changed",
        )
        narrative_mutation = json.loads(json.dumps(base_packet))
        narrative_mutation["transcript"]["text"] = "changed narrative"
        expect_error(
            lambda: bridge.validate_watch_packet(narrative_mutation),
            "fingerprint does not match",
        )
        alignment_mutation = json.loads(json.dumps(base_packet))
        alignment_mutation["alignment"]["frames"][0]["transcript"][0]["text"] = "wrong cue"
        expect_error(
            lambda: bridge.validate_watch_packet(alignment_mutation),
            "absent from transcript.segments",
        )
        source_url_mutation = json.loads(json.dumps(base_packet))
        source_url_mutation["source"]["canonical_url"] = "https://www.youtube.com/watch?v=AAAAAAAAAAA"
        expect_error(
            lambda: bridge.validate_watch_packet(source_url_mutation),
            "identity is not bound",
        )
        source_title_mutation = json.loads(json.dumps(base_packet))
        source_title_mutation["source"]["title"] = "Relabeled Video"
        expect_error(
            lambda: bridge.validate_watch_packet(source_title_mutation),
            "fingerprint does not match",
        )
        ocr_count_mutation = json.loads(json.dumps(base_packet))
        ocr_count_mutation["ocr"]["nonempty"] = 999
        expect_error(
            lambda: bridge.validate_watch_packet(ocr_count_mutation),
            "OCR counts do not match",
        )
        direct_media_mutation = json.loads(json.dumps(base_packet))
        direct_media_mutation["acquisition"]["direct_media"]["status"] = "pass"
        expect_error(
            lambda: bridge.validate_watch_packet(direct_media_mutation),
            "fingerprint does not match",
        )
        alignment_path_mutation = json.loads(json.dumps(base_packet))
        alignment_path_mutation["alignment"]["frames"][0]["path"] = "/tmp/not-captured.jpg"
        expect_error(
            lambda: bridge.validate_watch_packet(alignment_path_mutation),
            "alignment path does not match",
        )
        alignment_reason_mutation = json.loads(json.dumps(base_packet))
        alignment_reason_mutation["alignment"]["frames"][0]["reason"] = "invented_reason"
        expect_error(
            lambda: bridge.validate_watch_packet(alignment_reason_mutation),
            "alignment reason does not match",
        )
        alignment_ocr_mutation = json.loads(json.dumps(base_packet))
        alignment_ocr_mutation["alignment"]["frames"][0]["ocr"]["text"] = "invented OCR"
        expect_error(
            lambda: bridge.validate_watch_packet(alignment_ocr_mutation),
            "alignment OCR does not match",
        )
        alignment_review_mutation = json.loads(json.dumps(base_packet))
        alignment_review_mutation["alignment"]["frames"][0]["review_status"] = "visually_verified"
        expect_error(
            lambda: bridge.validate_watch_packet(alignment_review_mutation),
            "cannot self-claim visual review",
        )
        alignment_distance_mutation = json.loads(json.dumps(base_packet))
        alignment_distance_mutation["alignment"]["frames"][0]["alignment_distance_seconds"] = 999
        expect_error(
            lambda: bridge.validate_watch_packet(alignment_distance_mutation),
            "fingerprint does not match",
        )
        visual_state_mutation = json.loads(json.dumps(base_packet))
        visual_state_mutation["visual"]["evidence_label"] = "VISUAL_VERIFIED"
        expect_error(
            lambda: bridge.validate_watch_packet(visual_state_mutation),
            "visual proof state does not match",
        )
        transcript_source_mutation = json.loads(json.dumps(base_packet))
        transcript_source_mutation["transcript"]["source"] = "invented transcript source"
        expect_error(
            lambda: bridge.validate_watch_packet(transcript_source_mutation),
            "fingerprint does not match",
        )

        local_packet = make_packet(root, canonical_url=None, stem="local")
        expect_error(
            lambda: bridge.watch_packet_to_record(local_packet),
            "public http(s)",
        )
        nan_packet = make_packet(root, duration=math.nan, stem="nan")
        expect_error(
            lambda: bridge.watch_packet_to_record(nan_packet),
            "finite nonnegative",
        )

        payload_api = FakeNotion()
        payload = bridge.build_social_intel_payload(reviewed, payload_api, "social-db")
        props = payload["properties"]
        assert props["Post URL"] == {"url": CANONICAL_URL}
        assert props["Platform"]["select"]["name"] == "YouTube"
        assert props["Type"]["select"]["name"] == "Video"
        assert props["Evidence State"]["select"]["name"] == "PARTIAL_VISUAL_VERIFIED"
        assert props["Watch Fingerprint"] == NotionAPI.rich_text(reviewed["sync_fingerprint"])
        assert props["Topics"]["multi_select"] == [
            {"name": "AI Agents"}, {"name": "Claude"},
        ]
        assert len(payload["children"]) <= 90
        assert payload["request_bytes"]["create"] <= bridge.MAX_NOTION_REQUEST_BYTES
        assert any(
            "Capture-time limitation:" in bridge._block_plain_text(block)
            for block in payload["children"]
        )

        large_record = dict(reviewed)
        large_record["transcript"] = "T" * 500_000
        large_record["timeline"] = [
            {
                "timestamp_seconds": float(index),
                "reason": "scene",
                "path": f"/tmp/frame-{index:03d}.jpg",
                "ocr": {"text": "O" * 700},
                "transcript": [{"text": "S" * 700}],
                "review_observation": "R" * 700,
            }
            for index in range(60)
        ]
        large_payload = bridge.build_social_intel_payload(large_record, FakeNotion(), "social-db")
        assert large_payload["request_bytes"]["create"] <= bridge.MAX_NOTION_REQUEST_BYTES
        assert any(
            "Transcript truncated in Notion" in bridge._block_plain_text(block)
            for block in large_payload["children"]
        )
        unicode_record = dict(reviewed)
        unicode_record["transcript"] = "é🙂" * 70_000
        unicode_record["timeline"] = [
            {
                "timestamp_seconds": float(index),
                "reason": "scene",
                "path": f"/tmp/unicode-{index:03d}.jpg",
                "ocr": {"text": "🙂" * 700},
                "transcript": [{"text": "é" * 700}],
                "review_observation": "🙂" * 700,
            }
            for index in range(60)
        ]
        unicode_payload = bridge.build_social_intel_payload(
            unicode_record, FakeNotion(), "social-db"
        )
        assert unicode_payload["request_bytes"]["create"] <= bridge.MAX_NOTION_REQUEST_BYTES

        created_api = FakeNotion()
        created = bridge.sync_social_intel_record(created_api, "social-db", reviewed)
        assert created["action"] == "created" and len(created_api.create_calls) == 1
        assert created_api.events[:3] == ["query", "schema", "create"]

        unchanged_api = FakeNotion([notion_page(reviewed["sync_fingerprint"])])
        unchanged = bridge.sync_social_intel_record(unchanged_api, "social-db", reviewed)
        assert unchanged["action"] == "unchanged"
        assert not unchanged_api.update_calls and not unchanged_api.append_calls

        updated_api = FakeNotion([notion_page(unreviewed["sync_fingerprint"])])
        updated = bridge.sync_social_intel_record(updated_api, "social-db", reviewed)
        assert updated["action"] == "updated"
        assert len(updated_api.update_calls) == 1 and len(updated_api.append_calls) == 1
        refresh_properties = updated_api.update_calls[0][1]
        for shared_key in ("Name", "Creator", "Hook", "Analysis", "Batch", "Extract Candidate"):
            assert shared_key not in refresh_properties

        topic_api = FakeNotion([notion_page(reviewed["sync_fingerprint"])])
        topic_payload = bridge.build_social_intel_payload(topic_change, topic_api, "social-db")
        topic_result = bridge.upsert_social_intel_page(
            topic_api,
            "social-db",
            topic_payload,
            CANONICAL_URL,
            topic_change["sync_fingerprint"],
        )
        assert topic_result["action"] == "updated"

        duplicate_api = FakeNotion([
            notion_page("a" * 64, "one"),
            notion_page("b" * 64, "two"),
        ])
        expect_error(
            lambda: bridge.sync_social_intel_record(duplicate_api, "social-db", reviewed),
            "duplicate audit failed",
        )
        assert duplicate_api.events == ["query"]

        query_failure_api = FakeNotion(query_error=RuntimeError("offline"))
        expect_error(
            lambda: bridge.sync_social_intel_record(query_failure_api, "social-db", reviewed),
            "no page was written",
        )
        assert query_failure_api.events == ["query"]
        assert not query_failure_api.schema_calls and not query_failure_api.create_calls

        retry_api = FakeNotion(
            [notion_page(unreviewed["sync_fingerprint"])], fail_update_once=True
        )
        retry_payload = bridge.build_social_intel_payload(reviewed, retry_api, "social-db")
        expect_error(
            lambda: bridge.upsert_social_intel_page(
                retry_api,
                "social-db",
                retry_payload,
                CANONICAL_URL,
                reviewed["sync_fingerprint"],
            ),
            "simulated property update failure",
        )
        bridge.upsert_social_intel_page(
            retry_api,
            "social-db",
            retry_payload,
            CANONICAL_URL,
            reviewed["sync_fingerprint"],
        )
        assert len(retry_api.append_calls) == 1, "retry duplicated the Watch Refresh body"
        assert len(retry_api.update_calls) == 2

        packet_path = root / "packet.json"
        packet_path.write_text(json.dumps(base_packet), encoding="utf-8")
        with mock.patch.object(
            bridge, "_load_apify_client_module", side_effect=AssertionError("Apify must not load")
        ), mock.patch.object(
            NotionAPI, "__init__", side_effect=AssertionError("Notion client must not instantiate")
        ):
            code, stdout = run_main([
                "social_to_notion.py", "--watch-packet", str(packet_path),
                "--topics", "AI Agents", "--dry-run",
            ])
        assert code == 0
        dry_output = json.loads(stdout)
        assert dry_output["status"] == "dry_run"
        assert dry_output["database"] == "social_intel"

        transcript_path = root / "legacy.txt"
        transcript_path.write_text("Legacy transcript", encoding="utf-8")
        dummy_apify = SimpleNamespace(
            run_actor=lambda *args, **kwargs: (_ for _ in ()).throw(
                AssertionError("legacy dry-run must not call Apify")
            )
        )
        with mock.patch.object(bridge, "_load_apify_client_module", return_value=dummy_apify):
            code, stdout = run_main([
                "social_to_notion.py", CANONICAL_URL,
                "--transcript-file", str(transcript_path), "--dry-run",
            ])
        assert code == 0
        legacy_output = json.loads(stdout)
        assert legacy_output["record"]["transcript"] == "Legacy transcript"

    print(
        "PASS: packet integrity, receipt truth, canonicalization, safe Notion upsert/retry, "
        "and zero-network dry runs"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
