#!/usr/bin/env python3
"""No-network acceptance checks for Jen's content intelligence archive."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

import jen_content_archive as archive_module
import monid_client


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


class FakeMonid:
    def __init__(self) -> None:
        self.calls = []

    def run(self, endpoint: str, query: dict) -> dict:
        self.calls.append((endpoint, dict(query)))
        if endpoint.endswith("fetch_user_info_by_username_v2"):
            return {"data": {"user": {"id": "u1", "username": "_jiing", "edge_owner_to_timeline_media": {"count": 3}}}}
        if endpoint.endswith("fetch_user_posts_v2"):
            cursor = query.get("end_cursor")
            if not cursor:
                return {"data": {"user": {"edge_owner_to_timeline_media": {"edges": [
                    {"node": {"id": "1", "shortcode": "one", "caption": {"text": "I handled the offer timeline before my buyer had to worry, and then the offer was accepted."}, "edge_media_to_comment": {"count": 1}, "edge_media_preview_like": {"count": 10}}},
                    {"node": {"id": "2", "shortcode": "two", "caption": {"text": "A family day in the Valley."}, "edge_media_to_comment": {"count": 0}, "edge_media_preview_like": {"count": 20}}}
                ], "page_info": {"has_next_page": True, "end_cursor": "c2"}}}}}
            return {"data": {"user": {"edge_owner_to_timeline_media": {"edges": [
                {"node": {"id": "2", "shortcode": "two", "caption": {"text": "duplicate"}, "edge_media_to_comment": {"count": 0}}},
                {"node": {"id": "3", "shortcode": "three", "caption": {"text": "We reviewed 123 Main St before the seller had to decide."}, "edge_media_to_comment": {"count": 1}, "edge_media_preview_like": {"count": 30}}}
            ], "page_info": {"has_next_page": False, "end_cursor": None}}}}}
        if endpoint.endswith("fetch_post_comments_v2"):
            media_id = query["media_id"]
            preview = [{"pk": "r-1", "text": "Tarzana would be ideal", "user": {"username": "replyperson"}}] if media_id == "1" else []
            return {"comment_count": 1, "comments": [{"pk": f"c-{media_id}", "text": "Can you help us buy at 700k? @someone", "user": {"username": "privateperson"}, "child_comment_count": 2 if media_id == "1" else 0, "preview_child_comments": preview}], "next_min_id": None, "has_more_headload_comments": False}
        if endpoint.endswith("fetch_comment_replies"):
            return {"child_comments": [
                {"pk": "r-1", "text": "Tarzana would be ideal", "user": {"username": "replyperson"}, "parent_comment_id": query["comment_id"]},
                {"pk": "r-2", "text": "We hope to move this summer", "user": {"username": "replyperson2"}, "parent_comment_id": query["comment_id"]},
            ], "next_min_child_cursor": None, "has_more_tail_child_comments": False}
        if endpoint.endswith("fetch_user_highlights"):
            return {"data": {"items": [{"id": "highlight:1", "title": "Clients"}, {"id": "highlight:2", "title": "SFV"}]}}
        if endpoint.endswith("fetch_highlight_stories"):
            return {"data": {"items": [{"pk": "s1", "taken_at": 1, "media_type": 1}]}}
        raise AssertionError(f"Unexpected endpoint {endpoint}")


def main() -> int:
    checks = 0
    with tempfile.TemporaryDirectory(prefix="jen-archive-test-") as temp_dir:
        root = Path(temp_dir)
        monid_client.TRACKER_PATH = root / "monid-usage.json"
        fake = FakeMonid()
        archive = archive_module.JenArchive(root / "private", root / "curated", adapter=fake)

        receipt = archive.inventory()
        require(receipt["profile_count"] == 3, "profile count missing")
        require(receipt["extracted_count"] == 3, "cross-page media dedupe failed")
        require(archive.state["phases"]["inventory"]["complete"] is True, "inventory did not reconcile")
        require(archive.state["quote_receipts"][0]["phase"] == "inventory", "inventory phase quote missing")
        checks += 4

        before = archive.state["calls"]
        archive.inventory()
        require(archive.state["calls"] == before, "resume recharged existing inventory pages")
        checks += 1

        try:
            archive.comments(0.51, endpoint_version="v1")
        except RuntimeError as error:
            require("--approved" in str(error), "approval boundary returned wrong error")
        else:
            raise AssertionError("unapproved >$0.50 tranche executed")
        checks += 1

        comments = archive.comments(0.51, approved=True, endpoint_version="v1")
        require(comments["unique_comments_and_replies"] == 4, "comment and reply normalization failed")
        comment_calls = [call for call in fake.calls if call[0].endswith("fetch_post_comments_v2")]
        require(len(comment_calls) == 2, "zero-comment post caused a paid call")
        reply_calls = [call for call in fake.calls if call[0].endswith("fetch_comment_replies")]
        require(len(reply_calls) == 1, "missing child replies were not paginated")
        require(comments["archive_complete"] is True, "complete comment archive was not marked terminal")
        require(archive.state["quote_receipts"][-1]["operator_approval_acknowledged"] is True, "comment approval not receipted")
        checks += 5

        highlight_receipt = archive.highlights()
        require(highlight_receipt == {"count": 2, "story_count": 2}, "highlight extraction failed")
        checks += 1

        archive.state["phases"]["media"] = {"complete": True}
        archive.save()
        bank = archive.build_bank()
        require(bank["entries"] >= 1, "story bank failed to retain evidence-bearing fixture")
        story_text = (root / "curated" / "Jen Story Bank.csv").read_text()
        audience_text = (root / "curated" / "audience-language-bank.json").read_text()
        require("123 Main St" not in story_text, "exact address leaked into curated story bank")
        require("@someone" not in audience_text and "privateperson" not in audience_text, "raw commenter identity leaked")
        require("private_archive_path" not in (root / "curated" / "story-bank.json").read_text(), "private source path leaked into curated story JSON")
        checks += 4

        sabotage = archive._classify_post({
            "media_id": "sabotage",
            "caption": "Before photos are my favorite. Clear skies in the Valley. $5 coffee at home. Closed for the weekend.",
            "media_type": "image",
            "raw_page_sha256": "abc",
            "permalink": "https://www.instagram.com/p/sabotage/",
            "thumbnail_url": None,
        })
        require(not sabotage["classification"]["service_actions"], "broad words became service proof")
        require(not sabotage["classification"]["payoff_evidence"], "non-transaction close became payoff")
        require(sabotage["classification"]["primary_topic"]["value"] != "market proof and numbers", "coffee price became market proof")
        checks += 3

        buyer_listing = archive._classify_post({
            "media_id": "buyer-listing",
            "caption": "We toured this listing with my buyers and submitted an offer.",
            "media_type": "carousel",
            "raw_page_sha256": "abc",
            "permalink": "https://www.instagram.com/p/buyer-listing/",
            "thumbnail_url": "https://example.com/thumb.jpg",
        })
        sides = {item["value"] for item in buyer_listing["classification"]["audiences"]}
        require("buyer" in sides, "buyer listing fixture lost buyer audience")
        require("seller" not in sides, "listing token forced false seller audience")
        checks += 2

        archive.pending_path.write_text(json.dumps({"logical_key": "uncertain"}))
        try:
            archive.paid_call("inventory", "new-call", "profile", {"username": "_jiing"})
        except RuntimeError as error:
            require("Ambiguous prior" in str(error), "ambiguous call returned wrong error")
        else:
            raise AssertionError("ambiguous pending call was silently retried")
        checks += 1

        require(archive.state["project_spend_usd"] < 10.0, "fixture exceeded project cap")
        require((root / "curated" / "drive-export-manifest.json").exists(), "Drive export manifest missing")
        checks += 2

    with tempfile.TemporaryDirectory(prefix="jen-archive-tranche-test-") as temp_dir:
        tranche_root = Path(temp_dir)
        monid_client.TRACKER_PATH = tranche_root / "monid-usage.json"
        tranche_archive = archive_module.JenArchive(tranche_root / "private", tranche_root / "curated", adapter=FakeMonid())
        tranche_archive.inventory()
        paused = tranche_archive.comments(0.0015, endpoint_version="v1")
        require(paused["archive_complete"] is False, "tranche exhaustion falsely completed comments")
        require(tranche_archive.state["comment_progress"]["post_index"] == 0, "post advanced before child replies completed")
        require(len(tranche_archive.state["comment_progress"]["pending_reply_parents"]) == 1, "never-started reply job was not persisted")
        resumed = tranche_archive.comments(0.01, endpoint_version="v1")
        require(resumed["archive_complete"] is True, "resumed reply queue did not reach terminal state")
        checks += 4

    print(f"JEN CONTENT ARCHIVE: PASS ({checks} checks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
