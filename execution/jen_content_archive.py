#!/usr/bin/env python3
"""Resumable, source-traced Instagram archive and Jen Story Bank builder.

Raw API pages and commenter identities stay under an ignored private root. Only
redacted, source-linked derivatives may be written to the curated client tree.
"""

from __future__ import annotations

import argparse
import csv
import fcntl
import hashlib
import json
import math
import os
import statistics
import ssl
import re
import subprocess
import sys
import tempfile
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import Counter, defaultdict
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Iterable

import monid_client

try:
    import certifi
except ImportError:  # pragma: no cover - system certificate store remains the fallback
    certifi = None


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PRIVATE_ROOT = REPO_ROOT / ".tmp" / "jen-content-intelligence"
DEFAULT_CURATED_ROOT = (
    REPO_ROOT / "_active" / "clients" / "jen-listings" / "06-system" / "content-intelligence"
)
USERNAME = "_jiing"
PROVIDER = "tikhub"
PROJECT_CEILING_USD = 10.00
TRANCHE_CEILING_USD = 3.00
POST_PAGE_SIZE = 50
CLASSIFIER_VERSION = "2.0-evidence-spans"
SSL_CONTEXT = ssl.create_default_context(cafile=certifi.where()) if certifi else ssl.create_default_context()

ENDPOINTS = {
    "profile": ("/api/v1/instagram/v1/fetch_user_info_by_username_v2", 0.0015),
    "posts": ("/api/v1/instagram/v1/fetch_user_posts_v2", 0.0015),
    "comments": ("/api/v1/instagram/v1/fetch_post_comments_v2", 0.0015),
    "comments_v2": ("/api/v1/instagram/v2/fetch_post_comments", 0.003),
    "replies": ("/api/v1/instagram/v1/fetch_comment_replies", 0.0015),
    "replies_v2": ("/api/v1/instagram/v2/fetch_comment_replies", 0.003),
    "highlights": ("/api/v1/instagram/v2/fetch_user_highlights", 0.003),
    "highlight_stories": ("/api/v1/instagram/v2/fetch_highlight_stories", 0.003),
}


class ProviderCallError(RuntimeError):
    """A provider run completed but returned no usable endpoint output."""

    def __init__(self, message: str, *, logical_key: str, actual_cost: float, http_status: int | None):
        super().__init__(message)
        self.logical_key = logical_key
        self.actual_cost = actual_cost
        self.http_status = http_status

SERVICE_RULES = {
    "NOTICED": re.compile(r"\b(?:i|we)\s+(?:noticed|caught|spotted|flagged|realized)\b.{0,120}\b(?:offer|inspection|disclosure|property|home|client|buyer|seller|risk|issue|problem)\b", re.I | re.S),
    "HANDLED": re.compile(r"\b(?:i|we)\s+(?:handled|managed|coordinated|scheduled|took care of|followed (?:up|through))\b.{0,140}\b(?:offer|inspection|disclosure|repair|escrow|closing|move|client|buyer|seller|property|home)\b", re.I | re.S),
    "TRANSLATED": re.compile(r"\b(?:i|we)\s+(?:explained|translated|walked (?:my|our|the) (?:client|buyer|seller)s? through|clarified)\b.{0,140}\b(?:process|contract|offer|inspection|disclosure|escrow|timeline|options|terms)\b", re.I | re.S),
    "PROTECTED": re.compile(r"\b(?:i|we)\s+(?:protected|reviewed|verified|checked|negotiated|secured)\b.{0,140}\b(?:client|buyer|seller|offer|inspection|disclosure|contingenc|repair|credit|terms|deposit)\w*\b", re.I | re.S),
    "PREVENTED": re.compile(r"\b(?:i|we)\s+(?:prevented|avoided|stopped|caught)\b.{0,100}\b(?:risk|issue|problem|loss|delay|cost|surprise|before)\b", re.I | re.S),
    "REMOVED": re.compile(r"\b(?:i|we)\s+(?:took care of|handled|removed)\b.{0,120}\b(?:for (?:my|our|the) (?:client|buyer|seller)s?|off (?:their|the client(?:'s)?) plate)\b", re.I | re.S),
}

AUDIENCE_RULES = {
    "buyer": re.compile(r"\b(?:buyer|buyers|buy a home|buying a home|purchase|homeownership|house hunt|wrote? (?:an? )?offer|submitted (?:an? )?offer|our search)\b", re.I),
    "seller": re.compile(r"\b(?:seller|sellers|selling (?:a|your|their) home|list(?:ed|ing) (?:a|your|their|this) (?:home|property)|on the market|open house|multiple offers|over asking)\b", re.I),
}

STAGE_RULES = {
    "DREAMING": re.compile(r"\b(?:dreaming|someday|not ready yet|future home)\b", re.I),
    "PREPARING": re.compile(r"\b(?:pre[- ]?approval|credit|save up|down payment|getting ready|listing prep)\b", re.I),
    "SEARCH_OR_MARKET": re.compile(r"\b(?:house hunt|tour(?:ed|ing)?|saw (?:a|the|tons of) home|open house|hit the market|showing)\b", re.I),
    "OFFER_OR_NEGOTIATION": re.compile(r"\b(?:wrote? (?:an? )?offer|submitted (?:an? )?offer|multiple offers|counter(?:offer)?|negotiat(?:e|ed|ion)|over asking|under asking)\b", re.I),
    "ESCROW_OR_DUE_DILIGENCE": re.compile(r"\b(?:in escrow|inspection|appraisal|disclosure|contingenc|repair request|closing process)\w*\b", re.I),
    "CLOSED_OR_AFTERCARE": re.compile(r"\b(?:closed escrow|just sold|just closed|got the keys|became (?:a|the) homeowner|welcome home)\b", re.I),
}

PRIMARY_TOPIC_RULES = {
    "client move stories": re.compile(r"\b(?:my|our|the) (?:client|buyer|seller)s?\b.{0,240}\b(?:home|move|offer|escrow|sold|closed|search)\b", re.I | re.S),
    "decision clarity": re.compile(r"\b(?:here(?:'s| is) (?:what|how)|what (?:happens|to expect)|steps?|process|timeline|options|before you|what you need to know)\b.{0,180}\b(?:buy|sell|offer|escrow|home|real estate|inspection|mortgage)\w*\b", re.I | re.S),
    "work clients never carried": re.compile(r"\b(?:i|we)\s+(?:handled|managed|coordinated|negotiated|reviewed|caught|protected|secured|took care of)\b.{0,160}\b(?:client|buyer|seller|offer|inspection|repair|escrow|home|property)\b", re.I | re.S),
    "local life and homes": re.compile(r"\b(?:san fernando valley|sfv|tarzana|reseda|woodland hills|van nuys|encino|sherman oaks|porter ranch|granada hills|north hills|northridge)\b", re.I),
    "life transitions around home": re.compile(r"\b(?:new chapter|growing family|first home|first-time|stop renting|closer to (?:their|our) family|became a homeowner|investment property|moving)\b", re.I),
    "market proof and numbers": re.compile(r"\b(?:listed|sold|under contract|in escrow|days on market|multiple offers|over asking|under asking|repairs?|credit|interest rate|mortgage|median price)\b.{0,160}(?:\$[\d,.]+|\b\d+(?:\.\d+)?%|\b\d+\s+(?:days?|offers?|people))", re.I | re.S),
    "jen human lens": re.compile(r"\b(?:i remember|i realized|i thought|i learned|i felt|i never thought|if you know me|in my life|this one hits|a new chapter)\b", re.I),
    "motherhood and family life": re.compile(r"\b(?:becoming a mom|toddler mom|raver mom|pregnan|newborn|our baby|my son|my child|parent(?:ing|hood)|family life|growing family)\w*\b", re.I),
    "music community and belonging": re.compile(r"\b(?:rave|raver|festival|edc|coachella|electric sky|dance floor|music festival|dj|favorite set)\w*\b", re.I),
    "travel and experience design": re.compile(r"\b(?:honeymoon|travel(?:ed|ing)?|trip to|vacation|weekend in|playa del carmen|mexico|italy|paris|adventure)\b", re.I),
    "grief growth and resilience": re.compile(r"\b(?:my dad|my father|grief|passed away|loss|without you|hard year|healing|resilien|grew through|silver lining)\w*\b", re.I),
    "ownership and entrepreneurship": re.compile(r"\b(?:became a homeowner|own my|investment property|real estate portfolio|business owner|started (?:a|my) business|my career|entrepreneur|sales volume)\b", re.I),
}

ADDRESS_RE = re.compile(
    r"\b\d{1,6}\s+[A-Z0-9][A-Za-z0-9.'-]*(?:\s+[A-Z0-9][A-Za-z0-9.'-]*){0,4}\s+"
    r"(?:St|Street|Ave|Avenue|Blvd|Boulevard|Rd|Road|Dr|Drive|Ct|Court|Ln|Lane|Way|Pl|Place)\b\.?,?",
    re.I,
)
HANDLE_RE = re.compile(r"(?<!\w)@[A-Za-z0-9._]+")
EMAIL_RE = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
PHONE_RE = re.compile(r"(?<!\d)(?:\+?1[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?)\d{3}[-.\s]?\d{4}(?!\d)")
URL_RE = re.compile(r"https?://\S+|\bwww\.\S+", re.I)
CLIENT_NAME_RE = re.compile(r"\b(?:clients?|buyers?|sellers?)\s+([A-Z][a-z]{1,24})(?:\s+(?:and|&)\s+([A-Z][a-z]{1,24}))?\b")
MINOR_RE = re.compile(r"\b(?:baby|newborn|toddler|son|daughter|kid|child|children|\d{1,2}[- ]year[- ]old)\b", re.I)
CLIENT_QUOTE_RE = re.compile(r"\b(?:my|our|the) client(?:s)? (?:said|told|wrote|texted)\b|[“\"]{1}[^”\"]{12,}[”\"]{1}", re.I)
NEGOTIATION_DETAIL_RE = re.compile(r"\b(?:negotiated|secured|credit|repairs?|concession)\b.{0,80}(?:\$[\d,.]+|\b\d+(?:\.\d+)?%)", re.I | re.S)
FAIR_HOUSING_RE = re.compile(r"\b(?:safe neighborhood|good schools?|family[- ]friendly|ideal for families|young professionals|perfect for (?:a )?family)\b", re.I)


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def atomic_write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as handle:
        handle.write(data)
        temp_path = Path(handle.name)
    os.replace(temp_path, path)


def atomic_write_json(path: Path, value: Any) -> None:
    atomic_write_bytes(path, (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode())


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text())


@contextmanager
def exclusive_archive_lock(root: Path):
    """Prevent two archive commands from spending or saving the same state concurrently."""
    root = root.resolve()
    root.mkdir(parents=True, exist_ok=True)
    lock_path = root / ".archive.lock"
    with lock_path.open("a+") as handle:
        try:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise RuntimeError(f"Another Jen archive command already owns {lock_path}") from error
        try:
            yield
        finally:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def deep_values(value: Any) -> Iterable[Any]:
    yield value
    if isinstance(value, dict):
        for child in value.values():
            yield from deep_values(child)
    elif isinstance(value, list):
        for child in value:
            yield from deep_values(child)


def find_dict(value: Any, predicate) -> dict | None:
    for candidate in deep_values(value):
        if isinstance(candidate, dict) and predicate(candidate):
            return candidate
    return None


def find_key(value: Any, key: str) -> Any:
    for candidate in deep_values(value):
        if isinstance(candidate, dict) and key in candidate:
            return candidate[key]
    return None


def redact(text: str | None) -> str:
    if not text:
        return ""
    text = HANDLE_RE.sub("[handle removed]", text)
    text = ADDRESS_RE.sub("[address removed]", text)
    text = EMAIL_RE.sub("[email removed]", text)
    text = PHONE_RE.sub("[phone removed]", text)
    text = URL_RE.sub("[link removed]", text)
    text = CLIENT_NAME_RE.sub(lambda match: match.group(0).replace(match.group(1), "[client name removed]").replace(match.group(2), "[client name removed]") if match.group(2) else match.group(0).replace(match.group(1), "[client name removed]"), text)
    return text.strip()


def evidence_spans(text: str, pattern: re.Pattern[str], rule_id: str) -> list[dict]:
    result = []
    for match in pattern.finditer(text):
        result.append({
            "start": match.start(),
            "end": match.end(),
            "text": redact(match.group(0).strip()),
            "rule_id": rule_id,
            "evidence_state": "SOURCE_REPORTED",
        })
    return result


def sentence_evidence(text: str, patterns: list[tuple[str, re.Pattern[str]]]) -> list[dict]:
    spans = []
    for index, match in enumerate(re.finditer(r"[^.!?\n]+(?:[.!?]+|$)", text)):
        sentence = match.group(0).strip()
        for rule_id, pattern in patterns:
            if pattern.search(sentence):
                spans.append({"start": match.start(), "end": match.end(), "text": redact(sentence), "rule_id": rule_id, "evidence_state": "SOURCE_REPORTED"})
                break
    return spans


def privacy_scan(text: str) -> dict:
    detectors = {
        "CLIENT_HANDLE": HANDLE_RE,
        "CLIENT_NAME_POSSIBLE": CLIENT_NAME_RE,
        "EXACT_ADDRESS": ADDRESS_RE,
        "EMAIL": EMAIL_RE,
        "PHONE": PHONE_RE,
        "NEGOTIATION_DETAIL": NEGOTIATION_DETAIL_RE,
        "MINOR": MINOR_RE,
        "TESTIMONIAL_OR_CLIENT_QUOTE": CLIENT_QUOTE_RE,
        "FAIR_HOUSING_REVIEW": FAIR_HOUSING_RE,
    }
    flags = [name for name, pattern in detectors.items() if pattern.search(text or "")]
    hard = {"EMAIL", "PHONE", "CLIENT_NAME_POSSIBLE", "EXACT_ADDRESS", "CLIENT_HANDLE"}
    review = hard | {"NEGOTIATION_DETAIL", "MINOR", "TESTIMONIAL_OR_CLIENT_QUOTE", "FAIR_HOUSING_REVIEW"}
    state = "NEEDS_JEN_APPROVAL" if any(flag in review for flag in flags) else "DEIDENTIFIED"
    return {"state": state, "sensitivity_flags": flags, "redactions_applied": [flag for flag in flags if flag in hard], "approval_reference": None}


def int_or_none(value: Any) -> int | None:
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def caption_text(node: dict) -> str:
    caption = node.get("caption") or node.get("captionText")
    if isinstance(caption, dict):
        return str(caption.get("text") or "")
    if isinstance(caption, str):
        return caption
    edge = node.get("edge_media_to_caption") or {}
    edges = edge.get("edges") or [] if isinstance(edge, dict) else []
    if edges and isinstance(edges[0], dict):
        return str((edges[0].get("node") or {}).get("text") or "")
    return ""


def edge_count(node: dict, *keys: str) -> int | None:
    for key in keys:
        value = node.get(key)
        if isinstance(value, dict) and "count" in value:
            return int_or_none(value.get("count"))
        parsed = int_or_none(value)
        if parsed is not None:
            return parsed
    return None


def normalize_post(node: dict, raw_path: Path, raw_checksum: str) -> dict:
    media_id = str(node.get("id") or node.get("pk") or node.get("media_id") or "")
    shortcode = node.get("shortcode") or node.get("code")
    typename = str(node.get("__typename") or node.get("media_type") or node.get("mediaType") or "unknown").lower()
    if node.get("is_video") or "video" in typename or "reel" in typename:
        media_type = "reel"
    elif "sidecar" in typename or node.get("carousel_media"):
        media_type = "carousel"
    elif media_id:
        media_type = "image"
    else:
        media_type = "unknown"
    taken_at = node.get("taken_at_timestamp") or node.get("taken_at") or node.get("timestamp")
    if isinstance(taken_at, (int, float)):
        posted_at = datetime.fromtimestamp(taken_at, tz=timezone.utc).isoformat()
    else:
        posted_at = str(taken_at or "") or None
    media_urls: list[str] = []

    def add_url(value: Any) -> None:
        if isinstance(value, str) and value.startswith(("http://", "https://")) and value not in media_urls:
            media_urls.append(value)

    primary_media = node.get("video_url") or node.get("videoUrl") or node.get("display_url") or node.get("displayUrl")
    add_url(primary_media)
    image_versions = node.get("image_versions2") or node.get("imageVersions2") or {}
    for candidate in image_versions.get("candidates") or [] if isinstance(image_versions, dict) else []:
        if isinstance(candidate, dict):
            add_url(candidate.get("url"))
    for candidate in node.get("video_versions") or node.get("videoVersions") or []:
        if isinstance(candidate, dict):
            add_url(candidate.get("url"))
    for candidate in node.get("images") or []:
        add_url(candidate if isinstance(candidate, str) else candidate.get("url") if isinstance(candidate, dict) else None)
    sidecar = node.get("edge_sidecar_to_children") or {}
    for edge_item in sidecar.get("edges") or [] if isinstance(sidecar, dict) else []:
        child = edge_item.get("node") if isinstance(edge_item, dict) else None
        if isinstance(child, dict):
            child_url = child.get("video_url") or child.get("display_url")
            add_url(child_url)
    for child in node.get("carousel_media") or node.get("carouselMedia") or []:
        if isinstance(child, dict):
            add_url(child.get("video_url") or child.get("videoUrl") or child.get("display_url") or child.get("displayUrl"))
            child_images = child.get("image_versions2") or child.get("imageVersions2") or {}
            for candidate in child_images.get("candidates") or [] if isinstance(child_images, dict) else []:
                if isinstance(candidate, dict):
                    add_url(candidate.get("url"))
            for candidate in child.get("video_versions") or child.get("videoVersions") or []:
                if isinstance(candidate, dict):
                    add_url(candidate.get("url"))
    primary_media = media_urls[0] if media_urls else None
    return {
        "schema_version": "1.0",
        "media_id": media_id,
        "shortcode": shortcode,
        "permalink": f"https://www.instagram.com/p/{shortcode}/" if shortcode else None,
        "posted_at": posted_at,
        "retrieved_at": now_iso(),
        "raw_page_path": str(raw_path),
        "raw_page_sha256": raw_checksum,
        "media_type": media_type,
        "caption": caption_text(node),
        "like_count": edge_count(node, "edge_media_preview_like", "like_count", "likesCount"),
        "comment_count": edge_count(node, "edge_media_to_comment", "edge_media_preview_comment", "comment_count", "commentsCount"),
        "view_count": edge_count(node, "video_view_count", "play_count", "view_count", "viewsCount"),
        "thumbnail_url": node.get("thumbnail_src") or node.get("thumbnailSrc") or node.get("display_url") or node.get("displayUrl") or node.get("thumbnail_url") or node.get("thumbnailUrl") or (media_urls[0] if media_urls else None),
        "full_media_url": primary_media,
        "media_urls": media_urls,
        "accessibility_caption": node.get("accessibility_caption"),
    }


def timeline_from(payload: Any) -> dict | None:
    return find_dict(
        payload,
        lambda item: isinstance(item.get("edges"), list)
        and isinstance(item.get("page_info"), dict)
        and ("count" in item or any(isinstance(e, dict) and "node" in e for e in item.get("edges", []))),
    )


def nodes_from_timeline(timeline: dict | None) -> list[dict]:
    if not timeline:
        return []
    nodes = []
    for edge in timeline.get("edges") or []:
        if isinstance(edge, dict) and isinstance(edge.get("node"), dict):
            nodes.append(edge["node"])
        elif isinstance(edge, dict):
            nodes.append(edge)
    return nodes


class MonidCLI:
    def run(self, endpoint: str, query: dict) -> dict:
        command = [
            "monid", "run", "--provider", PROVIDER, "--endpoint", endpoint,
            "--query", json.dumps(query, separators=(",", ":")), "--wait", "90", "--json",
        ]
        result = subprocess.run(command, capture_output=True, text=True, timeout=120)
        if result.returncode != 0:
            raise RuntimeError((result.stderr or result.stdout or "Monid run failed").strip())
        clean = re.sub(r"\x1b\[[0-9;]*m", "", result.stdout).strip()
        return json.loads(clean)

    def get_run(self, run_id: str) -> dict:
        result = subprocess.run(
            ["monid", "runs", "get", "--run-id", run_id, "--json"],
            capture_output=True,
            text=True,
            timeout=120,
        )
        if result.returncode != 0:
            raise RuntimeError((result.stderr or result.stdout or "Monid run retrieval failed").strip())
        clean = re.sub(r"\x1b\[[0-9;]*m", "", result.stdout).strip()
        return json.loads(clean)


class JenArchive:
    def __init__(self, private_root: Path, curated_root: Path, adapter: Any | None = None):
        self.private_root = private_root.resolve()
        self.curated_root = curated_root.resolve()
        self.adapter = adapter or MonidCLI()
        self.state_path = self.private_root / "state.json"
        self.pending_path = self.private_root / "pending-call.json"
        self.state = load_json(self.state_path, self._new_state())
        self.private_root.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def _new_state() -> dict:
        return {
            "schema_version": "1.0",
            "project": "jen-content-intelligence",
            "username": USERNAME,
            "created_at": now_iso(),
            "updated_at": now_iso(),
            "project_ceiling_usd": PROJECT_CEILING_USD,
            "project_spend_usd": 0.0,
            "calls": 0,
            "phases": {},
            "quote_receipts": [],
            "coverage_gaps": [],
            "drive": {},
        }

    def save(self) -> None:
        self.state["updated_at"] = now_iso()
        atomic_write_json(self.state_path, self.state)

    def guard_clean(self) -> None:
        if self.pending_path.exists():
            pending = load_json(self.pending_path, {})
            raise RuntimeError(
                "Ambiguous prior Monid call must be resolved before retry: "
                + json.dumps(pending, sort_keys=True)
            )

    def record_phase_quote(self, phase: str, quoted_ceiling_usd: float, approved: bool) -> dict:
        """Persist the operator-visible quote that authorizes a paid phase or tranche."""
        quote = monid_client.evaluate_quote(quoted_ceiling_usd)
        if quote["decision"] == "denied":
            raise RuntimeError(f"{phase.title()} quote denied: {quote['reason']}")
        if quote["decision"] == "approval_required" and not approved:
            raise RuntimeError(f"{phase.title()} quote requires explicit --approved acknowledgement")
        if float(self.state["project_spend_usd"]) + quoted_ceiling_usd > PROJECT_CEILING_USD + 1e-9:
            raise RuntimeError(
                f"{phase.title()} quote would exceed the ${PROJECT_CEILING_USD:.2f} project ceiling"
            )
        quote_sequence = len(self.state.setdefault("quote_receipts", [])) + 1
        receipt = {
            "quote_id": f"{phase}-{quote_sequence:04d}-{now_iso().replace(':', '').replace('-', '')}",
            "phase": phase,
            "quoted_ceiling_usd": round(float(quoted_ceiling_usd), 6),
            "project_spend_before_usd": round(float(self.state["project_spend_usd"]), 6),
            "project_ceiling_usd": PROJECT_CEILING_USD,
            "approval_required": quote["decision"] == "approval_required",
            "operator_approval_acknowledged": bool(approved),
            "decision": "approved",
            "committed_usd": 0.0,
            "recorded_at": now_iso(),
        }
        self.state["quote_receipts"].append(receipt)
        quote_path = self.private_root / "receipts" / "quotes" / f"{receipt['quote_id']}.json"
        atomic_write_json(quote_path, receipt)
        self.state.setdefault("phases", {}).setdefault(phase, {})["active_quote_id"] = receipt["quote_id"]
        self.save()
        return receipt

    def _active_quote(self, phase: str) -> dict:
        quote_id = self.state.get("phases", {}).get(phase, {}).get("active_quote_id")
        for receipt in reversed(self.state.get("quote_receipts", [])):
            if receipt.get("quote_id") == quote_id:
                return receipt
        raise RuntimeError(f"No open quote receipt exists for paid phase {phase}")

    @staticmethod
    def _provider_failure(payload: Any) -> tuple[bool, int | None, str | None]:
        if not isinstance(payload, dict) or "providerResponse" not in payload:
            return False, None, None
        provider_response = payload.get("providerResponse") or {}
        http_status = int_or_none(provider_response.get("httpStatus")) if isinstance(provider_response, dict) else None
        output_missing = payload.get("output") is None
        failed = bool((http_status is not None and http_status >= 400) or output_missing or str(payload.get("status") or "").upper() not in {"", "COMPLETED"})
        message = None
        if failed:
            detail = ((provider_response.get("error") or {}).get("detail") or {}) if isinstance(provider_response, dict) else {}
            message = str(detail.get("message") or f"provider returned HTTP {http_status} with no usable output")
        return failed, http_status, message

    def resolve_pending(self, run_id: str) -> dict:
        """Recover a completed, already-billed call from Monid's run ledger."""
        pending = load_json(self.pending_path, None)
        if not pending:
            raise RuntimeError("No pending call exists")
        record = self.adapter.get_run(run_id)
        if str(record.get("status") or "").upper() != "COMPLETED":
            raise RuntimeError(f"Run {run_id} is not completed")
        if record.get("endpoint") != pending.get("endpoint"):
            raise RuntimeError("Run endpoint does not match the pending call")
        recorded_query = ((record.get("input") or {}).get("queryParams") or {})
        if recorded_query != pending.get("query"):
            raise RuntimeError("Run query does not match the pending call")
        provider_response = record.get("providerResponse") or {}
        provider_http = int_or_none(provider_response.get("httpStatus")) if isinstance(provider_response, dict) else None
        provider_failed = provider_http is not None and provider_http >= 400
        payload = record if record.get("output") is None and provider_failed else record.get("output")
        if payload is None:
            raise RuntimeError("Completed run has no recoverable output or provider failure receipt")
        cost_node = record.get("cost") or {}
        cost = float(cost_node["value"]) if "value" in cost_node else float(pending["quoted_cost_usd"])
        encoded_payload = json.dumps(payload, ensure_ascii=False, sort_keys=True).encode()
        checksum = sha256_bytes(encoded_payload)
        raw_path = self.private_root / "raw" / pending["phase"] / f"{pending['logical_key']}.json"
        receipt = {
            **pending,
            "run_id": run_id,
            "completed_at": record.get("completedAt") or now_iso(),
            "state": "recovered_provider_error" if provider_failed else "recovered_complete",
            "actual_cost_usd": cost,
            "payload_sha256": checksum,
        }
        atomic_write_json(raw_path, {"receipt": receipt, "payload": payload})
        atomic_write_bytes(raw_path.with_suffix(raw_path.suffix + ".sha256"), (sha256_bytes(raw_path.read_bytes()) + "\n").encode())
        phase_state = self.state["phases"].setdefault(pending["phase"], {"calls": 0, "spend_usd": 0.0})
        phase_state["calls"] += 1
        phase_state["spend_usd"] = round(float(phase_state["spend_usd"]) + cost, 6)
        self.state["calls"] += 1
        self.state["project_spend_usd"] = round(float(self.state["project_spend_usd"]) + cost, 6)
        for quote in self.state.get("quote_receipts", []):
            if quote.get("quote_id") == pending.get("quote_id"):
                quote["committed_usd"] = round(float(quote.get("committed_usd", 0.0)) + cost, 6)
                break
        self.save()
        self.pending_path.unlink()
        monid_client.cmd_log(SimpleNamespace(query=f"Jen recovered {pending['phase']}: {pending['logical_key']}", cost=cost, results=1))
        if provider_failed:
            self._add_gap_once({"phase": pending["phase"], "logical_key": pending["logical_key"], "reason": "provider_error", "http_status": provider_http, "actual_cost_usd": cost, "blocking": True})
            self.save()
        return {"run_id": run_id, "raw_path": str(raw_path), "cost_usd": cost, "payload_sha256": checksum, "state": receipt["state"]}

    def paid_call(self, phase: str, logical_key: str, endpoint_key: str, query: dict) -> tuple[dict, Path, str]:
        endpoint, price = ENDPOINTS[endpoint_key]
        raw_path = self.private_root / "raw" / phase / f"{logical_key}.json"
        if raw_path.exists():
            raw = load_json(raw_path, {})
            receipt = raw.get("receipt") or {}
            payload = raw.get("payload")
            payload_sha = receipt.get("payload_sha256") or receipt.get("sha256")
            calculated_sha = sha256_bytes(json.dumps(payload, ensure_ascii=False, sort_keys=True).encode())
            if receipt.get("logical_key") != logical_key or receipt.get("endpoint") != endpoint:
                raise RuntimeError(f"Cached raw-page identity mismatch: {raw_path}")
            if receipt.get("query") != query:
                raise RuntimeError(f"Cached raw-page query mismatch: {raw_path}")
            if payload_sha != calculated_sha:
                raise RuntimeError(f"Cached raw-page payload checksum mismatch: {raw_path}")
            sidecar = raw_path.with_suffix(raw_path.suffix + ".sha256")
            if sidecar.exists() and sidecar.read_text().strip() != sha256_bytes(raw_path.read_bytes()):
                raise RuntimeError(f"Cached raw-page file checksum mismatch: {raw_path}")
            pending = load_json(self.pending_path, None)
            if pending and pending.get("logical_key") == logical_key and pending.get("endpoint") == endpoint and pending.get("query") == query:
                actual_cost = float(receipt.get("actual_cost_usd") or pending.get("quoted_cost_usd") or price)
                phase_state = self.state["phases"].setdefault(phase, {})
                phase_state["calls"] = int(phase_state.get("calls", 0)) + 1
                phase_state["spend_usd"] = round(float(phase_state.get("spend_usd", 0.0)) + actual_cost, 6)
                self.state["calls"] += 1
                self.state["project_spend_usd"] = round(float(self.state["project_spend_usd"]) + actual_cost, 6)
                for quote in self.state.get("quote_receipts", []):
                    if quote.get("quote_id") == pending.get("quote_id"):
                        quote["committed_usd"] = round(float(quote.get("committed_usd", 0.0)) + actual_cost, 6)
                        break
                self.pending_path.unlink(missing_ok=True)
                self.save()
                monid_client.cmd_log(SimpleNamespace(query=f"Jen recovered local receipt {phase}: {logical_key}", cost=actual_cost, results=1))
            failed, http_status, message = self._provider_failure(payload)
            if failed:
                raise ProviderCallError(message or "Provider call failed", logical_key=logical_key, actual_cost=float(receipt.get("actual_cost_usd") or 0.0), http_status=http_status)
            return payload, raw_path, payload_sha

        self.guard_clean()
        active_quote = self._active_quote(phase)
        if float(active_quote.get("committed_usd", 0.0)) + price > float(active_quote["quoted_ceiling_usd"]) + 1e-9:
            raise RuntimeError(f"{phase.title()} quote exhausted before {logical_key}")
        projected = float(self.state["project_spend_usd"]) + price
        if projected > PROJECT_CEILING_USD + 1e-9:
            raise RuntimeError(f"Project budget stop: ${projected:.4f} would exceed ${PROJECT_CEILING_USD:.2f}")
        quote = monid_client.evaluate_quote(price)
        if quote["decision"] == "denied":
            raise RuntimeError("Monid budget denied: " + quote["reason"])

        pending = {
            "phase": phase,
            "logical_key": logical_key,
            "endpoint": endpoint,
            "query": query,
            "quoted_cost_usd": price,
            "quote_id": active_quote["quote_id"],
            "started_at": now_iso(),
            "state": "pending_or_ambiguous",
        }
        atomic_write_json(self.pending_path, pending)
        try:
            payload = self.adapter.run(endpoint, query)
        except Exception:
            raise

        encoded_payload = json.dumps(payload, ensure_ascii=False, sort_keys=True).encode()
        checksum = sha256_bytes(encoded_payload)
        billed = payload.get("cost") if isinstance(payload, dict) else None
        actual_cost = float(billed["value"]) if isinstance(billed, dict) and "value" in billed else price
        receipt = {
            **pending,
            "run_id": payload.get("runId") if isinstance(payload, dict) else None,
            "completed_at": now_iso(),
            "state": "complete",
            "actual_cost_usd": actual_cost,
            "payload_sha256": checksum,
        }
        atomic_write_json(raw_path, {"receipt": receipt, "payload": payload})
        atomic_write_bytes(raw_path.with_suffix(raw_path.suffix + ".sha256"), (sha256_bytes(raw_path.read_bytes()) + "\n").encode())

        phase_state = self.state["phases"].setdefault(phase, {"calls": 0, "spend_usd": 0.0})
        phase_state["calls"] = int(phase_state.get("calls", 0)) + 1
        phase_state["spend_usd"] = round(float(phase_state.get("spend_usd", 0.0)) + actual_cost, 6)
        self.state["calls"] += 1
        self.state["project_spend_usd"] = round(float(self.state["project_spend_usd"]) + actual_cost, 6)
        active_quote["committed_usd"] = round(float(active_quote.get("committed_usd", 0.0)) + actual_cost, 6)
        self.save()
        self.pending_path.unlink(missing_ok=True)

        monid_client.cmd_log(SimpleNamespace(query=f"Jen {phase}: {logical_key}", cost=actual_cost, results=1))
        failed, http_status, message = self._provider_failure(payload)
        if failed:
            self._add_gap_once({"phase": phase, "logical_key": logical_key, "reason": "provider_error", "http_status": http_status, "actual_cost_usd": actual_cost, "blocking": True})
            self.save()
            raise ProviderCallError(message or "Provider call failed", logical_key=logical_key, actual_cost=actual_cost, http_status=http_status)
        return payload, raw_path, checksum

    def inventory(self, max_cost: float = 0.15) -> dict:
        self.record_phase_quote("inventory", max_cost, approved=max_cost > 0.50)
        profile, profile_path, profile_sha = self.paid_call(
            "inventory", "profile", "profile", {"username": USERNAME}
        )
        user = find_dict(
            profile,
            lambda item: str(item.get("username") or "").lower() == USERNAME.lower()
            and bool(item.get("id") or item.get("pk")),
        )
        if not user:
            raise RuntimeError("Could not locate Jen's user record in the Monid response")
        user_id = str(user.get("id") or user.get("pk"))
        profile_timeline = user.get("edge_owner_to_timeline_media") or {}
        expected = int_or_none(profile_timeline.get("count")) or 0
        self.state["profile"] = {
            "user_id": user_id,
            "profile_post_count": expected,
            "extracted_post_count": self.state.get("profile", {}).get("extracted_post_count", 0),
            "profile_raw_path": str(profile_path),
            "profile_sha256": profile_sha,
        }
        self.save()

        posts: dict[str, dict] = {}
        cursor = None
        page = 0
        seen_cursors = set()
        while True:
            logical_key = f"posts-{page:04d}"
            page_is_cached = (self.private_root / "raw" / "inventory" / f"{logical_key}.json").exists()
            phase_spend = float(self.state["phases"].get("inventory", {}).get("spend_usd", 0.0))
            if not page_is_cached and phase_spend + ENDPOINTS["posts"][1] > max_cost + 1e-9:
                self.write_posts(sorted(posts.values(), key=lambda row: row.get("posted_at") or "", reverse=True))
                gap = {
                    "phase": "inventory",
                    "reason": "phase_cost_ceiling_reached",
                    "ceiling_usd": max_cost,
                    "next_cursor": cursor,
                    "extracted": len(posts),
                    "expected": expected,
                }
                self.state["coverage_gaps"] = [x for x in self.state["coverage_gaps"] if not (x.get("phase") == "inventory" and x.get("reason") == "phase_cost_ceiling_reached")]
                self.state["coverage_gaps"].append(gap)
                self.state["profile"]["extracted_post_count"] = len(posts)
                self.save()
                return self.inventory_receipt(list(posts.values()))
            query = {"user_id": user_id, "count": POST_PAGE_SIZE}
            if cursor:
                query["end_cursor"] = cursor
            payload, raw_path, raw_sha = self.paid_call(
                "inventory", logical_key, "posts", query
            )
            timeline = find_key(payload, "edge_owner_to_timeline_media")
            if not isinstance(timeline, dict):
                timeline = timeline_from(payload)
            for node in nodes_from_timeline(timeline):
                normalized = normalize_post(node, raw_path, raw_sha)
                if normalized["media_id"]:
                    posts[normalized["media_id"]] = normalized
            page_info = (timeline or {}).get("page_info") or {}
            next_cursor = page_info.get("end_cursor") or page_info.get("next_cursor")
            has_next = bool(page_info.get("has_next_page") or next_cursor)
            page += 1
            if not has_next or not next_cursor:
                break
            if next_cursor in seen_cursors:
                self.state["coverage_gaps"].append({"phase": "inventory", "reason": "repeated_cursor", "cursor": next_cursor})
                break
            seen_cursors.add(next_cursor)
            cursor = str(next_cursor)

        ordered = sorted(posts.values(), key=lambda row: row.get("posted_at") or "", reverse=True)
        self.write_posts(ordered)
        self.state["profile"]["extracted_post_count"] = len(ordered)
        self.state["phases"].setdefault("inventory", {})["complete"] = len(ordered) == expected
        self.state["coverage_gaps"] = [
            gap for gap in self.state["coverage_gaps"]
            if not (gap.get("phase") == "inventory" and gap.get("reason") == "phase_cost_ceiling_reached")
        ]
        if expected and len(ordered) != expected:
            self.state["coverage_gaps"].append({"phase": "inventory", "reason": "count_mismatch", "expected": expected, "extracted": len(ordered)})
        self.save()
        return self.inventory_receipt(ordered)

    def write_posts(self, posts: list[dict]) -> None:
        normalized = self.private_root / "normalized"
        ndjson = "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in posts)
        atomic_write_bytes(normalized / "posts.ndjson", ndjson.encode())
        fields = list(posts[0].keys()) if posts else []
        csv_path = normalized / "posts.csv"
        csv_path.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile("w", dir=csv_path.parent, delete=False, newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            if fields:
                writer.writeheader()
                writer.writerows(posts)
            temp_path = Path(handle.name)
        os.replace(temp_path, csv_path)

    def load_posts(self) -> list[dict]:
        path = self.private_root / "normalized" / "posts.ndjson"
        if not path.exists():
            raise RuntimeError("Run inventory first")
        return [json.loads(line) for line in path.read_text().split("\n") if line.strip()]

    def inventory_receipt(self, posts: list[dict] | None = None) -> dict:
        posts = posts if posts is not None else self.load_posts()
        types = Counter(row.get("media_type") or "unknown" for row in posts)
        known_count_posts = sum(row.get("comment_count") is not None for row in posts)
        unknown_count_posts = len(posts) - known_count_posts
        with_comments = sum(1 for row in posts if row.get("comment_count") is not None and row["comment_count"] > 0)
        known_comments = sum(row["comment_count"] for row in posts if row.get("comment_count") is not None)
        min_comment_cost = round(with_comments * ENDPOINTS["comments_v2"][1], 4)
        planning_calls = sum(math.ceil(row["comment_count"] / 15) for row in posts if row.get("comment_count") is not None and row["comment_count"] > 0)
        planning_cost = round(planning_calls * ENDPOINTS["comments_v2"][1], 4)
        remaining_project_budget = round(max(0.0, PROJECT_CEILING_USD - self.state["project_spend_usd"]), 4)
        return {
            "profile_count": self.state.get("profile", {}).get("profile_post_count"),
            "extracted_count": len(posts),
            "media_types": dict(types),
            "posts_reporting_comments": with_comments,
            "reported_comment_total": known_comments,
            "minimum_comment_cost_usd": min_comment_cost,
            "planning_comment_quote_usd": planning_cost,
            "firm_remaining_project_ceiling_usd": remaining_project_budget,
            "next_comment_tranche_ceiling_usd": min(TRANCHE_CEILING_USD, remaining_project_budget),
            "posts": {"profile_reported": self.state.get("profile", {}).get("profile_post_count"), "extracted": len(posts), "reels": types.get("reel", 0), "carousels": types.get("carousel", 0), "images": types.get("image", 0), "unknown": types.get("unknown", 0)},
            "highlights": {"status": "complete" if self.state.get("phases", {}).get("highlights", {}).get("complete") else "pending", "count": self.state.get("highlights", {}).get("count"), "story_count": self.state.get("highlights", {}).get("story_count")},
            "comments": {"posts_with_known_counts": known_count_posts, "posts_with_unknown_counts": unknown_count_posts, "reported_comment_total": known_comments, "minimum_first_page_cost_usd": min_comment_cost, "estimated_top_level_cost_usd": planning_cost, "reply_cost_state": "UNKNOWN_UNTIL_PARENT_COMMENTS_INSPECTED", "estimated_total_cost_usd": None, "firm_project_ceiling_remaining_usd": remaining_project_budget, "next_tranche_ceiling_usd": min(TRANCHE_CEILING_USD, remaining_project_budget)},
            "quote_note": "Working v2 estimate assumes 15 returned comments per page and is not clipped to budget. Replies remain unknown until parent comments are inspected; only the remaining project ceiling is firm.",
        }

    def reconcile_profile_count(self) -> dict:
        """Take a fresh profile snapshot after pagination to distinguish drift from an access gap."""
        self.record_phase_quote("inventory", 0.01, approved=False)
        existing = sorted((self.private_root / "raw" / "inventory").glob("profile-reconcile-*.json"))
        logical_key = existing[-1].stem if existing and not self.state.get("profile_reconciliation") else f"profile-reconcile-{len(existing) + 1:04d}"
        payload, raw_path, raw_sha = self.paid_call(
            "inventory", logical_key, "profile", {"username": USERNAME}
        )
        user = find_dict(
            payload,
            lambda item: str(item.get("username") or "").lower() == USERNAME.lower()
            and bool(item.get("id") or item.get("pk")),
        )
        if not user:
            raise RuntimeError("Could not locate Jen's user record in the reconciliation response")
        reported = int_or_none((user.get("edge_owner_to_timeline_media") or {}).get("count"))
        extracted = len(self.load_posts())
        result = {
            "reported_post_count": reported,
            "extracted_unique_posts": extracted,
            "reconciled": reported == extracted,
            "raw_path": str(raw_path),
            "payload_sha256": raw_sha,
            "checked_at": now_iso(),
        }
        self.state["profile_reconciliation"] = result
        self.state["phases"].setdefault("inventory", {})["cursor_terminal"] = True
        self.state["phases"]["inventory"]["count_reconciled"] = result["reconciled"]
        self.state["phases"]["inventory"]["accessible_complete"] = True
        self.state["phases"]["inventory"]["complete"] = result["reconciled"]
        self.save()
        return result

    def comments(self, max_cost: float, approved: bool = False, endpoint_version: str = "v2") -> dict:
        if max_cost <= 0 or max_cost > TRANCHE_CEILING_USD:
            raise RuntimeError(f"Comment tranche must be >$0 and <=${TRANCHE_CEILING_USD:.2f}")
        self.record_phase_quote("comments", max_cost, approved=approved)
        posts = self.load_posts()
        endpoint_key = "comments_v2" if endpoint_version == "v2" else "comments"
        call_price = ENDPOINTS[endpoint_key][1]
        max_calls = int(max_cost / call_price + 1e-9)
        calls_at_start = self.state["calls"]
        rows: dict[str, dict] = {}
        existing_path = self.private_root / "normalized" / "comments.ndjson"
        if existing_path.exists():
            for line in existing_path.read_text().split("\n"):
                if line.strip():
                    row = json.loads(line)
                    rows[row["comment_id"]] = row

        progress = self.state.setdefault("comment_progress", {
            "post_index": 0,
            "post_cursors": {},
            "pending_reply_parents": [],
            "seen_post_cursors": {},
            "seen_reply_cursors": {},
            "post_coverage": {},
        })
        progress.setdefault("pending_reply_parents", [])
        progress.setdefault("seen_post_cursors", {})
        progress.setdefault("seen_reply_cursors", {})
        progress.setdefault("post_coverage", {})

        while progress["pending_reply_parents"]:
            if self.state["calls"] - calls_at_start >= max_calls:
                self.write_comments(rows.values())
                self.save()
                return self.comment_receipt(rows, tranche_complete=False)
            self._fetch_reply_page(rows, progress["pending_reply_parents"][0])

        for index in range(int(progress.get("post_index", 0)), len(posts)):
            post = posts[index]
            media_id = post["media_id"]
            coverage = progress["post_coverage"].setdefault(media_id, {
                "reported_comment_count": post.get("comment_count"),
                "returned_top_level": 0,
                "returned_replies": 0,
                "top_level_terminal": False,
                "reply_terminal": True,
                "unavailable_estimate": None,
            })
            if (post.get("comment_count") or 0) <= 0:
                coverage["top_level_terminal"] = True
                progress["post_index"] = index + 1
                self.save()
                continue
            cursor = progress["post_cursors"].get(media_id)
            page = 0
            while not coverage.get("top_level_terminal"):
                if self.state["calls"] - calls_at_start >= max_calls:
                    self.write_comments(rows.values())
                    self.save()
                    return self.comment_receipt(rows, tranche_complete=False)
                if endpoint_version == "v2":
                    query = {"code_or_url": post.get("shortcode") or post.get("permalink"), "sort_by": "recent"}
                    if cursor:
                        query["pagination_token"] = cursor
                else:
                    query = {"media_id": media_id, "sort_order": "recent"}
                    if cursor:
                        query["min_id"] = cursor
                payload, raw_path, raw_sha = self.paid_call(
                    "comments", f"{media_id}-comments-{endpoint_version}-{page:04d}-{sha256_bytes(str(cursor).encode())[:8]}", endpoint_key, query
                )
                output = payload.get("output") if isinstance(payload, dict) and "output" in payload else payload
                comments = find_key(output, "items") if endpoint_version == "v2" else find_key(output, "comments")
                if not isinstance(comments, list):
                    comments = []
                for comment in comments:
                    if not isinstance(comment, dict):
                        continue
                    self._add_comment(rows, comment, media_id, None, raw_path, raw_sha)
                    previews = comment.get("preview_child_comments") or []
                    for reply in previews:
                        if isinstance(reply, dict):
                            self._add_comment(rows, reply, media_id, str(comment.get("pk") or ""), raw_path, raw_sha)
                    child_count = int_or_none(comment.get("child_comment_count")) or 0
                    if child_count > len(previews):
                        parent_id = str(comment.get("pk") or comment.get("id") or "")
                        if parent_id and not any(job.get("parent_id") == parent_id for job in progress["pending_reply_parents"]):
                            progress["pending_reply_parents"].append({
                                "media_id": media_id,
                                "shortcode": post.get("shortcode"),
                                "parent_id": parent_id,
                                "expected_replies": child_count,
                                "cursor": None,
                                "page": 0,
                            })
                            coverage["reply_terminal"] = False
                coverage["returned_top_level"] = sum(1 for row in rows.values() if row["media_id"] == media_id and row.get("depth") == 0)
                coverage["returned_replies"] = sum(1 for row in rows.values() if row["media_id"] == media_id and row.get("depth") == 1)
                self.write_comments(rows.values())
                next_cursor = find_key(output, "pagination_token") if endpoint_version == "v2" else find_key(output, "next_min_id")
                has_more = bool(next_cursor) if endpoint_version == "v2" else bool(find_key(output, "has_more_headload_comments") or next_cursor)
                if not has_more or not next_cursor:
                    progress["post_cursors"].pop(media_id, None)
                    coverage["top_level_terminal"] = True
                    self.save()
                    break
                seen = progress["seen_post_cursors"].setdefault(media_id, [])
                if str(next_cursor) == str(cursor) or str(next_cursor) in seen:
                    self._add_gap_once({"phase": "comments", "media_id": media_id, "reason": "repeated_cursor", "blocking": True})
                    self.save()
                    self.write_comments(rows.values())
                    return self.comment_receipt(rows, tranche_complete=False)
                cursor = str(next_cursor)
                seen.append(cursor)
                progress["post_cursors"][media_id] = cursor
                self.save()
                page += 1

            while progress["pending_reply_parents"] and progress["pending_reply_parents"][0]["media_id"] == media_id:
                if self.state["calls"] - calls_at_start >= max_calls:
                    self.write_comments(rows.values())
                    self.save()
                    return self.comment_receipt(rows, tranche_complete=False)
                self._fetch_reply_page(rows, progress["pending_reply_parents"][0], endpoint_version=endpoint_version)
            if any(job.get("media_id") == media_id for job in progress["pending_reply_parents"]):
                self.write_comments(rows.values())
                self.save()
                return self.comment_receipt(rows, tranche_complete=False)
            coverage["reply_terminal"] = True
            coverage["returned_top_level"] = sum(1 for row in rows.values() if row["media_id"] == media_id and row.get("depth") == 0)
            coverage["returned_replies"] = sum(1 for row in rows.values() if row["media_id"] == media_id and row.get("depth") == 1)
            reported = coverage.get("reported_comment_count")
            accessible = coverage["returned_top_level"] + coverage["returned_replies"]
            if reported is not None and accessible < reported:
                coverage["unavailable_estimate"] = reported - accessible
                self._add_gap_once({"phase": "comments", "media_id": media_id, "reason": "reported_vs_accessible_shortfall", "reported": reported, "accessible": accessible, "unavailable_estimate": reported - accessible, "blocking": False})
            progress["post_index"] = index + 1
            self.save()
        self.write_comments(rows.values())
        blocking = [gap for gap in self.state["coverage_gaps"] if gap.get("phase") == "comments" and gap.get("blocking")]
        progress["complete"] = progress["post_index"] == len(posts) and not progress["pending_reply_parents"] and not blocking
        self.state["phases"].setdefault("comments", {})["complete"] = progress["complete"]
        self.save()
        return self.comment_receipt(rows, tranche_complete=progress["complete"])

    def comments_canary(self, endpoint_version: str = "v2") -> dict:
        """Run one source-traced comment request before launching a full tranche."""
        self.record_phase_quote("canary", 0.01, approved=False)
        post = next((item for item in self.load_posts() if (item.get("comment_count") or 0) > 0 and item.get("shortcode")), None)
        if not post:
            raise RuntimeError("No comment-bearing post with shortcode is available for a canary")
        if endpoint_version == "v2":
            endpoint_key = "comments_v2"
            query = {"code_or_url": post["shortcode"], "sort_by": "recent"}
        else:
            endpoint_key = "comments"
            query = {"media_id": post["media_id"], "sort_order": "recent"}
        payload, raw_path, payload_sha = self.paid_call("canary", f"comments-{endpoint_version}-{post['media_id']}", endpoint_key, query)
        output = payload.get("output") if isinstance(payload, dict) and "output" in payload else payload
        items = find_key(output, "items") or find_key(output, "comments") or []
        token = find_key(output, "pagination_token") or find_key(output, "next_min_id")
        return {"endpoint_version": endpoint_version, "media_id": post["media_id"], "shortcode": post["shortcode"], "returned_comments": len(items) if isinstance(items, list) else 0, "has_next_cursor": bool(token), "raw_path": str(raw_path), "payload_sha256": payload_sha}

    def _fetch_reply_page(self, rows: dict[str, dict], job: dict, endpoint_version: str = "v2") -> None:
        media_id = job["media_id"]
        parent_id = job["parent_id"]
        cursor = job.get("cursor")
        if endpoint_version == "v2":
            query = {"code_or_url": job.get("shortcode"), "comment_id": parent_id}
            if cursor:
                query["pagination_token"] = cursor
            endpoint_key = "replies_v2"
        else:
            query = {"media_id": media_id, "comment_id": parent_id}
            if cursor:
                query["min_id"] = cursor
            endpoint_key = "replies"
        payload, raw_path, raw_sha = self.paid_call(
            "comments", f"{media_id}-reply-{endpoint_version}-{parent_id}-{int(job.get('page', 0)):04d}-{sha256_bytes(str(cursor).encode())[:8]}", endpoint_key, query
        )
        output = payload.get("output") if isinstance(payload, dict) and "output" in payload else payload
        replies = find_key(output, "items") if endpoint_version == "v2" else find_key(output, "child_comments")
        for reply in replies if isinstance(replies, list) else []:
            if isinstance(reply, dict):
                self._add_comment(rows, reply, media_id, parent_id, raw_path, raw_sha)
        self.write_comments(rows.values())
        next_cursor = find_key(output, "pagination_token") if endpoint_version == "v2" else find_key(output, "next_min_child_cursor") or find_key(output, "next_min_id")
        has_more = bool(next_cursor) if endpoint_version == "v2" else bool(find_key(output, "has_more_tail_child_comments") or next_cursor)
        queue = self.state["comment_progress"]["pending_reply_parents"]
        if not has_more or not next_cursor:
            queue.pop(0)
            self.save()
            return
        seen = self.state["comment_progress"]["seen_reply_cursors"].setdefault(parent_id, [])
        if str(next_cursor) == str(cursor) or str(next_cursor) in seen:
            self._add_gap_once({"phase": "comments", "media_id": media_id, "comment_id": parent_id, "reason": "repeated_reply_cursor", "blocking": True})
            queue.pop(0)
            self.save()
            return
        seen.append(str(next_cursor))
        job["cursor"] = str(next_cursor)
        job["page"] = int(job.get("page", 0)) + 1
        self.save()

    def _add_gap_once(self, gap: dict) -> None:
        identity = (gap.get("phase"), gap.get("media_id"), gap.get("comment_id"), gap.get("reason"))
        for existing in self.state.get("coverage_gaps", []):
            if (existing.get("phase"), existing.get("media_id"), existing.get("comment_id"), existing.get("reason")) == identity:
                return
        self.state.setdefault("coverage_gaps", []).append(gap)

    @staticmethod
    def _add_comment(rows: dict[str, dict], item: dict, media_id: str, parent_id: str | None, raw_path: Path, raw_sha: str) -> None:
        comment_id = str(item.get("pk") or item.get("id") or "")
        if not comment_id:
            return
        user = item.get("user") or {}
        rows[comment_id] = {
            "schema_version": "1.0",
            "comment_id": comment_id,
            "media_id": media_id,
            "parent_comment_id": parent_id or item.get("parent_comment_id"),
            "depth": 1 if parent_id or item.get("parent_comment_id") else 0,
            "created_at": item.get("created_at_utc") or item.get("created_at"),
            "text_raw_private": str(item.get("text") or ""),
            "author_username_private": user.get("username") if isinstance(user, dict) else None,
            "like_count": int_or_none(item.get("comment_like_count")),
            "raw_page_path": str(raw_path),
            "raw_page_sha256": raw_sha,
        }

    def write_comments(self, rows: Iterable[dict]) -> None:
        ordered = sorted(rows, key=lambda row: (row["media_id"], row.get("created_at") or "", row["comment_id"]))
        content = "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in ordered)
        atomic_write_bytes(self.private_root / "normalized" / "comments.ndjson", content.encode())

    def comment_receipt(self, rows: dict[str, dict], tranche_complete: bool) -> dict:
        progress = self.state.get("comment_progress", {})
        return {
            "unique_comments_and_replies": len(rows),
            "posts_completed": progress.get("post_index", 0),
            "posts_total": len(self.load_posts()),
            "archive_complete": bool(progress.get("complete")),
            "tranche_or_archive_complete": tranche_complete,
            "project_spend_usd": self.state["project_spend_usd"],
        }

    def highlights(self) -> dict:
        self.record_phase_quote("highlights", 0.05, approved=False)
        payload, raw_path, raw_sha = self.paid_call(
            "highlights", "highlight-index", "highlights", {"username": USERNAME}
        )
        items = self._highlight_items(payload)
        normalized = []
        for index, item in enumerate(items):
            highlight_id = str(item.get("id") or item.get("pk") or item.get("highlight_id") or "")
            if not highlight_id:
                continue
            stories, story_path, story_sha = self.paid_call(
                "highlights", f"highlight-{index:03d}-{highlight_id.replace(':', '_')}",
                "highlight_stories", {"highlight_id": highlight_id}
            )
            story_items = self._story_items(stories)
            normalized.append({
                "highlight_id": highlight_id,
                "title": item.get("title") or item.get("name"),
                "cover_url": item.get("cover_media") or item.get("cover_url"),
                "story_count": len(story_items),
                "stories": story_items,
                "raw_index_path": str(raw_path),
                "raw_index_sha256": raw_sha,
                "raw_stories_path": str(story_path),
                "raw_stories_sha256": story_sha,
            })
        atomic_write_json(self.private_root / "normalized" / "highlights.json", normalized)
        self.state["phases"].setdefault("highlights", {})["complete"] = True
        self.state["highlights"] = {"count": len(normalized), "story_count": sum(x["story_count"] for x in normalized)}
        self.save()
        return self.state["highlights"]

    @staticmethod
    def _highlight_items(payload: Any) -> list[dict]:
        for value in deep_values(payload):
            if isinstance(value, list) and value and all(isinstance(x, dict) for x in value):
                if any("title" in x and ("id" in x or "pk" in x) for x in value):
                    return value
        return []

    @staticmethod
    def _story_items(payload: Any) -> list[dict]:
        for value in deep_values(payload):
            if isinstance(value, list) and value and all(isinstance(x, dict) for x in value):
                if any("taken_at" in x or "media_type" in x or "image_versions2" in x for x in value):
                    return value
        return []

    def build_bank(self, provisional: bool = False) -> dict:
        phases = self.state.get("phases", {})
        inventory_ready = bool(phases.get("inventory", {}).get("complete") or phases.get("inventory", {}).get("accessible_complete"))
        required = {
            "inventory": inventory_ready,
            "comments": bool(phases.get("comments", {}).get("complete") or phases.get("comments", {}).get("operator_waived")),
            "highlights": bool(phases.get("highlights", {}).get("complete") or phases.get("highlights", {}).get("operator_waived")),
            "media": bool(phases.get("media", {}).get("complete") or phases.get("media", {}).get("accessible_complete")),
        }
        if not provisional and not all(required.values()):
            missing = [phase for phase, complete in required.items() if not complete]
            raise RuntimeError(f"Final Story Bank requires terminal archive phases; incomplete: {', '.join(missing)}")
        posts = self.load_posts()
        comment_rows = []
        comments_path = self.private_root / "normalized" / "comments.ndjson"
        if comments_path.exists():
            comment_rows = [json.loads(line) for line in comments_path.read_text().split("\n") if line.strip()]
        scored = [self._classify_post(post) for post in posts]
        self._add_performance_signals(scored)
        scored.sort(key=lambda row: (row["scores"]["story_value"], row.get("posted_at") or ""), reverse=True)
        selected = self._stratified_select(scored, 200)
        selected.sort(key=lambda row: (row["scores"]["story_value"], row.get("posted_at") or ""), reverse=True)
        stories = [self._story_entry(row, index + 1) for index, row in enumerate(selected)]
        packet_eligible = [story for story in stories if story["ranking"]["top_50_eligible"]]
        packets = [self._story_packet(story, index + 1) for index, story in enumerate(packet_eligible[:50])]
        pillars = self._derive_pillars(scored)
        audience = self._audience_language(comment_rows)
        build_state = "PROVISIONAL_NOT_FOR_PUBLISHING" if provisional else "FINAL_CANDIDATE"
        for item in stories + packets + pillars + audience:
            item["build_state"] = build_state

        self.curated_root.mkdir(parents=True, exist_ok=True)
        classified_path = self.private_root / "normalized" / "classified-posts.ndjson"
        atomic_write_bytes(classified_path, ("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in scored)).encode())
        source_ledger = [{"source_id": f"JEN-SRC-{row['media_id']}", "media_id": row["media_id"], "permalink": row.get("permalink"), "private_archive_path": row.get("raw_page_path"), "payload_sha256": row.get("raw_page_sha256"), "caption_raw_private": row.get("caption"), "classification_review_state": row["review_state"]} for row in scored]
        atomic_write_bytes(self.private_root / "normalized" / "story-source-ledger.ndjson", ("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in source_ledger)).encode())
        atomic_write_json(self.curated_root / "story-bank.json", stories)
        atomic_write_json(self.curated_root / "top-50-story-packets.json", packets)
        atomic_write_json(self.curated_root / "content-pillars-format-map.json", pillars)
        atomic_write_json(self.curated_root / "audience-language-bank.json", audience)
        self._write_audience_csv(audience)
        review_queue = [{"source_id": f"JEN-SRC-{row['media_id']}", "media_id": row["media_id"], "permalink": row.get("permalink"), "review_state": row["review_state"], "primary_topic_candidate": row["classification"]["primary_topic"]["value"], "story_value": row["scores"]["story_value"]} for row in scored if row["review_state"] != "AUTO_ACCEPT"]
        atomic_write_json(self.curated_root / "classification-review-queue.json", {"build_state": build_state, "items": review_queue})
        continuity = {"build_state": build_state, "supported_edges": [], "retrieval_queue": [{"story_id": story["story_id"], "question": "What later dated moment, if any, continued this exact story?"} for story in stories[:50]], "rule": "Thematic similarity is not continuity."}
        atomic_write_json(self.curated_root / "continuity-map.json", continuity)
        acceptance = {
            "story_count_200": len(stories) == 200,
            "deep_packet_count_50": len(packets) == 50,
            "stable_source_ids": all(story["source"]["source_id"] == f"JEN-SRC-{story['source']['media_id']}" for story in stories),
            "no_private_paths_in_curated_stories": all("private_archive_path" not in json.dumps(story) for story in stories),
            "archive_phases_terminal": all(required.values()),
        }
        analysis_receipt = {
            "schema_version": "1.0",
            "classifier_version": CLASSIFIER_VERSION,
            "build_state": build_state,
            "input_posts": len(posts),
            "classified_auto_accept": sum(row["review_state"] == "AUTO_ACCEPT" for row in scored),
            "classified_human_review": sum(row["review_state"] == "HUMAN_REVIEW" for row in scored),
            "unclassified": sum(row["review_state"] == "UNCLASSIFIED" for row in scored),
            "eligible_selected": len(stories),
            "deep_packet_eligible": len(packet_eligible),
            "deep_packets_written": len(packets),
            "selection_by_stratum": dict(Counter(story["ranking"]["selection_stratum"] for story in stories)),
            "pillar_states": dict(Counter(pillar["archive_state"] for pillar in pillars)),
            "required_archive_phases": required,
            "acceptance": acceptance,
            "acceptance_state": "PASS" if all(acceptance.values()) else "FAIL",
            "generated_at": now_iso(),
        }
        atomic_write_json(self.curated_root / "analysis-receipt.json", analysis_receipt)
        self._write_story_csv(stories)
        self._write_service_proof_doc(stories)
        self._write_pillar_doc(pillars)
        self._write_privacy_queue(stories)
        self._write_drive_manifest()
        self._write_checkpoint_report(stories, packets, pillars, analysis_receipt)
        self.state["phases"].setdefault("build-bank", {})["complete"] = not provisional and all(acceptance.values())
        self.state["phases"]["build-bank"]["provisional"] = provisional
        self.state["story_bank"] = {"entries": len(stories), "deep_packets": len(packets), "pillars": len(pillars), "provisional": provisional, "acceptance_state": analysis_receipt["acceptance_state"]}
        self.save()
        return self.state["story_bank"]

    def preserve_media(self, top: int = 200, workers: int = 6) -> dict:
        """Download all thumbnails and full media for the top story candidates."""
        posts = self.load_posts()
        classified = [self._classify_post(post) for post in posts]
        self._add_performance_signals(classified)
        selected = self._stratified_select(classified, top)
        top_ids = {row["media_id"] for row in selected}
        tasks = []
        missing_thumbnails = []
        missing_full_media = []
        for post in posts:
            if post.get("thumbnail_url"):
                tasks.append(("thumbnail", post["media_id"], 0, post["thumbnail_url"]))
            else:
                missing_thumbnails.append(post["media_id"])
            if post["media_id"] in top_ids:
                urls = post.get("media_urls") or ([post.get("full_media_url")] if post.get("full_media_url") else [])
                if not urls:
                    missing_full_media.append(post["media_id"])
                for index, url in enumerate(urls):
                    if url:
                        tasks.append(("full", post["media_id"], index, url))
        highlights_path = self.private_root / "normalized" / "highlights.json"
        highlights_waived = bool(self.state.get("phases", {}).get("highlights", {}).get("operator_waived"))
        if highlights_path.exists() and not highlights_waived:
            for highlight in load_json(highlights_path, []):
                for story in highlight.get("stories") or []:
                    story_id = str(story.get("pk") or story.get("id") or "unknown")
                    urls = []
                    image_items = (story.get("image_versions") or {}).get("items") or []
                    image_url = next(
                        (item.get("url") for item in image_items if isinstance(item, dict) and item.get("url")),
                        story.get("thumbnail_url"),
                    )
                    video_items = story.get("video_versions") or []
                    video_url = story.get("video_url") or next(
                        (item.get("url") for item in video_items if isinstance(item, dict) and item.get("url")),
                        None,
                    )
                    for value in (image_url, video_url):
                        if isinstance(value, str) and value.startswith(("http://", "https://")) and value not in urls:
                            urls.append(value)
                    for index, url in enumerate(urls):
                        tasks.append(("highlight", f"highlight-{story_id}", index, url))
        manifest_path = self.private_root / "media" / "manifest.json"
        existing = {row["key"]: row for row in load_json(manifest_path, [])}

        def download(task: tuple[str, str, int, str]) -> dict:
            kind, media_id, index, url = task
            key = f"{kind}:{media_id}:{index}"
            prior = existing.get(key)
            if prior and prior.get("status") == "complete" and Path(prior["path"]).exists():
                return prior
            suffix = Path(urllib.parse.urlparse(url).path).suffix.lower()
            if suffix not in {".jpg", ".jpeg", ".png", ".webp", ".mp4", ".mov"}:
                suffix = ".mp4" if "video" in url.lower() else ".jpg"
            target_group = {
                "thumbnail": "thumbnails",
                "full": "top-200-full",
                "highlight": "highlight-stories",
            }.get(kind, "other")
            target = self.private_root / "media" / target_group / f"{media_id}-{index:02d}{suffix}"
            request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            try:
                with urllib.request.urlopen(request, timeout=45, context=SSL_CONTEXT) as response:
                    content_type = response.headers.get_content_type()
                    data = response.read()
                if not data or content_type in {"text/html", "application/json", "text/plain"} or data[:32].lstrip().startswith((b"<html", b"<!DOCTYPE")):
                    raise RuntimeError(f"unexpected media response: {content_type}, {len(data)} bytes")
                atomic_write_bytes(target, data)
                return {"key": key, "media_id": media_id, "kind": kind, "index": index, "source_url": url, "path": str(target), "bytes": len(data), "sha256": sha256_bytes(data), "content_type": content_type, "status": "complete", "retrieved_at": now_iso()}
            except Exception as error:
                return {"key": key, "media_id": media_id, "kind": kind, "index": index, "source_url": url, "path": str(target), "status": "failed", "error": str(error), "retrieved_at": now_iso()}

        with ThreadPoolExecutor(max_workers=max(1, min(workers, 12))) as pool:
            futures = [pool.submit(download, task) for task in tasks]
            for completed_index, future in enumerate(as_completed(futures), 1):
                row = future.result()
                existing[row["key"]] = row
                if completed_index % 50 == 0:
                    atomic_write_json(manifest_path, sorted(existing.values(), key=lambda item: item["key"]))
        requested_keys = {f"{kind}:{media_id}:{index}" for kind, media_id, index, _ in tasks}
        rows = sorted((row for key, row in existing.items() if key in requested_keys), key=lambda item: item["key"])
        atomic_write_json(manifest_path, rows)
        complete = sum(1 for row in rows if row.get("status") == "complete")
        failed = sum(1 for row in rows if row.get("status") == "failed")
        attempted = complete + failed
        terminal = attempted >= len(tasks) and len(top_ids) == min(top, len(posts))
        self.state["media"] = {"requested": len(tasks), "attempted": attempted, "preserved": complete, "unavailable": failed, "top_candidate_count": len(top_ids), "all_post_count": len(posts), "missing_thumbnail_urls": len(missing_thumbnails), "missing_top_full_media_urls": len(missing_full_media), "manifest": str(manifest_path)}
        if failed:
            self._add_gap_once({"phase": "media", "reason": "download_failures", "count": failed, "blocking": False, "coverage": "Attempted but provider URL was unavailable; itemized in media manifest."})
        if missing_thumbnails:
            self._add_gap_once({"phase": "media", "reason": "missing_thumbnail_urls", "count": len(missing_thumbnails), "blocking": False})
        if missing_full_media:
            self._add_gap_once({"phase": "media", "reason": "missing_top_full_media_urls", "count": len(missing_full_media), "blocking": False, "coverage": "No accessible source URL was returned for this selected post."})
        phase = self.state["phases"].setdefault("media", {})
        phase["complete"] = terminal and failed == 0 and not missing_full_media
        phase["accessible_complete"] = terminal
        phase["coverage_state"] = "COMPLETE" if phase["complete"] else "ACCESSIBLE_COMPLETE_WITH_GAPS" if terminal else "INCOMPLETE"
        self.save()
        return self.state["media"]

    def record_drive(self, private_folder_id: str, private_url: str, curated_folder_id: str, curated_url: str) -> dict:
        self.state["drive"] = {
            "private_archive_folder_id": private_folder_id,
            "private_archive_url": private_url,
            "curated_folder_id": curated_folder_id,
            "curated_folder_url": curated_url,
            "recorded_at": now_iso(),
        }
        self.save()
        return self.state["drive"]

    def audit_state_from_raw(self, rewind_comments: bool = False) -> dict:
        """Rebuild spend from immutable provider envelopes without rewriting raw evidence."""
        phase_totals: dict[str, dict] = defaultdict(lambda: {"calls": 0, "spend_usd": 0.0, "provider_failures": 0})
        quote_committed = Counter()
        overrides = []
        for raw_path in sorted((self.private_root / "raw").glob("*/*.json")):
            raw = load_json(raw_path, {})
            receipt = raw.get("receipt") or {}
            payload = raw.get("payload")
            phase = receipt.get("phase") or raw_path.parent.name
            billed = payload.get("cost") if isinstance(payload, dict) else None
            actual = float(billed["value"]) if isinstance(billed, dict) and "value" in billed else float(receipt.get("actual_cost_usd") or 0.0)
            phase_totals[phase]["calls"] += 1
            phase_totals[phase]["spend_usd"] += actual
            failed, http_status, _ = self._provider_failure(payload)
            if failed:
                phase_totals[phase]["provider_failures"] += 1
            if abs(actual - float(receipt.get("actual_cost_usd") or 0.0)) > 1e-9:
                overrides.append({"raw_path": str(raw_path), "receipt_cost_usd": receipt.get("actual_cost_usd"), "provider_cost_usd": actual, "http_status": http_status})
            if receipt.get("quote_id"):
                quote_committed[receipt["quote_id"]] += actual
        for phase, totals in phase_totals.items():
            phase_state = self.state.setdefault("phases", {}).setdefault(phase, {})
            phase_state["calls"] = totals["calls"]
            phase_state["spend_usd"] = round(totals["spend_usd"], 6)
            phase_state["provider_failures"] = totals["provider_failures"]
        if self.state.get("phases", {}).get("inventory", {}).get("accessible_complete"):
            self.state["coverage_gaps"] = [
                gap for gap in self.state.get("coverage_gaps", [])
                if not (gap.get("phase") == "inventory" and gap.get("reason") == "phase_cost_ceiling_reached")
            ]
        for quote in self.state.get("quote_receipts", []):
            quote["committed_usd"] = round(quote_committed[quote["quote_id"]], 6)
        self.state["calls"] = sum(item["calls"] for item in phase_totals.values())
        self.state["project_spend_usd"] = round(sum(item["spend_usd"] for item in phase_totals.values()), 6)
        if rewind_comments:
            self.state["comment_progress"] = {"post_index": 0, "post_cursors": {}, "pending_reply_parents": [], "seen_post_cursors": {}, "seen_reply_cursors": {}, "post_coverage": {}, "complete": False}
            self.state.setdefault("phases", {}).setdefault("comments", {})["complete"] = False
            self.state["coverage_gaps"] = [gap for gap in self.state.get("coverage_gaps", []) if gap.get("phase") != "comments"]
        audit = {"audited_at": now_iso(), "phase_totals": dict(phase_totals), "project_spend_usd": self.state["project_spend_usd"], "cost_overrides": overrides, "comments_rewound": rewind_comments}
        self.state.setdefault("accounting_audits", []).append({"audited_at": audit["audited_at"], "project_spend_usd": audit["project_spend_usd"], "cost_override_count": len(overrides), "comments_rewound": rewind_comments})
        atomic_write_json(self.private_root / "receipts" / f"accounting-audit-{audit['audited_at'].replace(':', '').replace('-', '')}.json", audit)
        self.save()
        return audit

    def waive_comments(self) -> dict:
        """Record the operator's decision to exclude comments from the final archive."""
        phase = self.state.setdefault("phases", {}).setdefault("comments", {})
        phase["complete"] = False
        phase["operator_waived"] = True
        phase["waived_at"] = now_iso()
        phase["waiver_reason"] = "Operator removed comment and reply extraction from project scope."
        self._add_gap_once({"phase": "comments", "reason": "operator_waived", "blocking": False, "coverage": "No comment corpus in curated intelligence bank."})
        self.save()
        return {"comments_scope": "WAIVED", "paid_comment_spend_usd": phase.get("spend_usd", 0.0), "canary_spend_usd": self.state.get("phases", {}).get("canary", {}).get("spend_usd", 0.0), "recorded_at": phase["waived_at"]}

    def waive_highlights(self) -> dict:
        """Exclude Highlights from analysis and future media preservation."""
        phase = self.state.setdefault("phases", {}).setdefault("highlights", {})
        phase["operator_waived"] = True
        phase["excluded_from_analysis"] = True
        phase["waived_at"] = now_iso()
        phase["waiver_reason"] = "Operator removed Highlights from project scope. Existing paid snapshot remains private as a receipt only."
        self._add_gap_once({"phase": "highlights", "reason": "operator_waived", "blocking": False, "coverage": "Highlights excluded from Story Bank and media preservation."})
        self.save()
        return {"highlights_scope": "WAIVED", "existing_snapshot_spend_usd": phase.get("spend_usd", 0.0), "recorded_at": phase["waived_at"]}

    def _classify_post(self, post: dict) -> dict:
        caption = post.get("caption") or ""
        service_actions = []
        for canonical, pattern in SERVICE_RULES.items():
            evidence = evidence_spans(caption, pattern, f"SERVICE_{canonical}_V2")
            if evidence:
                service_actions.append({"value": canonical, "confidence": 0.9, "evidence": evidence})
        audiences = []
        for value, pattern in AUDIENCE_RULES.items():
            evidence = evidence_spans(caption, pattern, f"AUDIENCE_{value.upper()}_V2")
            if evidence:
                audiences.append({"value": value, "confidence": 0.9, "evidence": evidence})
        stages = []
        for value, pattern in STAGE_RULES.items():
            evidence = evidence_spans(caption, pattern, f"STAGE_{value}_V2")
            if evidence:
                stages.append({"value": value, "confidence": 0.85, "evidence": evidence})
        topic_candidates = []
        for topic, pattern in PRIMARY_TOPIC_RULES.items():
            evidence = evidence_spans(caption, pattern, "TOPIC_" + re.sub(r"\W+", "_", topic.upper()))
            if evidence:
                confidence = 0.9 if topic != "jen human lens" else 0.8
                topic_candidates.append({"value": topic, "confidence": confidence, "evidence": evidence})
        topic_candidates.sort(key=lambda item: (item["confidence"], len(item["evidence"])), reverse=True)
        primary_topic = topic_candidates[0] if topic_candidates else {"value": "unclassified", "confidence": 0.0, "evidence": []}

        problem_evidence = sentence_evidence(caption, [
            ("PROBLEM_TRANSACTION", re.compile(r"\b(?:lost (?:an? |the )?offer|multiple offers|stress(?:ed|ful)?|worried|problem|issue|risk|market crash|couldn(?:'|’)t|wasn(?:'|’)t|didn(?:'|’)t|rejected|outbid)\b", re.I)),
            ("PROBLEM_LIFE_TRANSITION", re.compile(r"\b(?:so hard|grief|loss|overwhelm|uncertain|not ready|rushed|struggl|scared|fear|beat(?:ing)? myself up|freaked out|passed away|without you)\w*\b", re.I)),
        ])
        pursuit_evidence = []
        for action in service_actions:
            pursuit_evidence.extend(action["evidence"])
        if not pursuit_evidence:
            pursuit_evidence = sentence_evidence(caption, [
                ("PURSUIT_EXPLICIT_ACTION", re.compile(r"\b(?:i|we)\s+(?:asked|called|showed|toured|wrote|submitted|helped|found|created|planned|prepared|reviewed|negotiated|made|built|learned|decided)\b", re.I))
            ])
        payoff_evidence = sentence_evidence(caption, [
            ("PAYOFF_TRANSACTION", re.compile(r"\b(?:closed escrow|just sold|just closed|got the keys|became (?:a|the) homeowner|under contract|in escrow|offer (?:was )?accepted|found (?:them|us|her|him) (?:a|the) home)\b", re.I)),
            ("PAYOFF_OBSERVED", re.compile(r"\b(?:now (?:they|we|she|he|i) (?:own|live|have|can)|the result|which meant|so (?:they|we|i) could|we did it|i did it|made it through|i learned|i became|it taught me|here we are)\b", re.I)),
        ])
        sfv_pattern = PRIMARY_TOPIC_RULES["local life and homes"]
        local_evidence = evidence_spans(caption, sfv_pattern, "LOCAL_SFV_NAMED_PLACE_V2")
        local_state = "SFV_OR_CITY" if local_evidence else "NONE"
        story_type = (
            "CLIENT_JOURNEY" if primary_topic["value"] == "client move stories"
            else "SERVICE_PROOF" if service_actions
            else "EDUCATIONAL" if primary_topic["value"] == "decision clarity"
            else "PERSONAL_ORIGIN" if primary_topic["value"] in {"jen human lens", "life transitions around home", "motherhood and family life", "music community and belonging", "travel and experience design", "grief growth and resilience", "ownership and entrepreneurship"}
            else "LISTING_OR_MARKET" if primary_topic["value"] == "market proof and numbers"
            else "FRAGMENT"
        )
        privacy = privacy_scan(caption)
        source_integrity = (8 if caption else 0) + (6 if post.get("permalink") else 0) + (6 if post.get("raw_page_sha256") else 0)
        service_specificity = min(20, sum(min(2, len(item["evidence"])) * 7 for item in service_actions))
        ppp_count = sum(bool(value) for value in (problem_evidence, pursuit_evidence, payoff_evidence))
        ppp_support = ppp_count * 5
        decision_relevance = min(15, (8 if audiences else 0) + (7 if stages else 0))
        human_lens = 10 if re.search(r"\b(?:i|we|my|our|client|family)\b", caption, re.I) else 0
        locality = 10 if local_evidence else 0
        adaptability = min(10, (4 if ppp_count >= 2 else 0) + (3 if post.get("thumbnail_url") else 0) + (3 if len(caption) >= 240 and (audiences or service_actions) else 0))
        personal_theme = primary_topic["value"] in {"jen human lens", "motherhood and family life", "music community and belonging", "travel and experience design", "grief growth and resilience", "ownership and entrepreneurship"}
        unused_meaning = 10 if personal_theme and ppp_count >= 2 and len(caption) >= 180 else 5 if personal_theme else 0
        adaptability = min(10, adaptability + (3 if personal_theme and ppp_count >= 2 else 0))
        story_value = min(100, source_integrity + service_specificity + ppp_support + decision_relevance + human_lens + locality + adaptability + unused_meaning)
        confidence = max([primary_topic["confidence"]] + [item["confidence"] for item in service_actions + audiences + stages])
        review_state = "AUTO_ACCEPT" if confidence >= 0.85 and story_value >= 60 else "HUMAN_REVIEW" if confidence >= 0.60 else "UNCLASSIFIED"
        return {
            **post,
            "classifier_version": CLASSIFIER_VERSION,
            "classification": {
                "audiences": audiences,
                "journey_stages": stages,
                "story_type": {"value": story_type, "confidence": confidence},
                "service_actions": service_actions,
                "topic_candidates": topic_candidates,
                "primary_topic": primary_topic,
                "local_relevance": {"state": local_state, "evidence": local_evidence},
                "problem_evidence": problem_evidence,
                "pursuit_evidence": pursuit_evidence,
                "payoff_evidence": payoff_evidence,
                "privacy": privacy,
            },
            "scores": {
                "story_value": story_value,
                "lead_path_fit": decision_relevance + service_specificity,
                "components": {
                    "source_integrity": source_integrity,
                    "service_specificity": service_specificity,
                    "problem_pursuit_payoff": ppp_support,
                    "decision_relevance": decision_relevance,
                    "human_lens": human_lens,
                    "locality": locality,
                    "adaptability": adaptability,
                    "unused_meaning": unused_meaning,
                },
            },
            "review_state": review_state,
            "commercial_proof_state": "NO_EVENT",
        }

    @staticmethod
    def _add_performance_signals(rows: list[dict]) -> None:
        cohorts: dict[tuple[str, int], list[float]] = defaultdict(list)
        all_format: dict[str, list[float]] = defaultdict(list)
        for row in rows:
            likes = row.get("like_count")
            comments = row.get("comment_count")
            if likes is None and comments is None:
                continue
            metric = float(likes or 0) + 2.0 * float(comments or 0)
            try:
                epoch = int(datetime.fromisoformat(row.get("posted_at") or "").timestamp() // (180 * 86400))
            except (TypeError, ValueError):
                epoch = 0
            cohorts[(row["media_type"], epoch)].append(metric)
            all_format[row["media_type"]].append(metric)
        for row in rows:
            likes = row.get("like_count")
            comments = row.get("comment_count")
            if likes is None and comments is None:
                row["performance_signal"] = {"metric_tier": "none", "cohort_percentile": None, "outlier_multiple": None, "cohort_n": 0}
                continue
            metric = float(likes or 0) + 2.0 * float(comments or 0)
            try:
                epoch = int(datetime.fromisoformat(row.get("posted_at") or "").timestamp() // (180 * 86400))
            except (TypeError, ValueError):
                epoch = 0
            cohort = cohorts[(row["media_type"], epoch)]
            if len(cohort) < 20:
                cohort = all_format[row["media_type"]]
            ordered = sorted(cohort)
            percentile = round(100 * sum(value <= metric for value in ordered) / len(ordered), 1) if ordered else None
            median = statistics.median(ordered) if ordered else 0
            multiple = round(metric / median, 2) if median else None
            row["performance_signal"] = {"metric_tier": "attention", "cohort_percentile": percentile, "outlier_multiple": multiple, "cohort_n": len(ordered), "raw_attention_index": metric}

    @staticmethod
    def _stratified_select(rows: list[dict], limit: int) -> list[dict]:
        eligible = [row for row in rows if row["scores"]["story_value"] >= 50 and row["review_state"] != "UNCLASSIFIED"]
        selected: list[dict] = []
        selected_ids = set()
        topic_counts = Counter()
        format_counts = Counter()
        topic_cap = max(1, int(limit * 0.20))
        format_cap = max(1, int(limit * 0.25))

        def add(row: dict, stratum: str, reason: str, relax_format: bool = False) -> bool:
            media_id = row["media_id"]
            topic = row["classification"]["primary_topic"]["value"]
            media_type = row.get("media_type") or "unknown"
            if media_id in selected_ids or topic_counts[topic] >= topic_cap:
                return False
            if not relax_format and format_counts[media_type] >= format_cap:
                return False
            copy = dict(row)
            copy["selection_stratum"] = stratum
            copy["selection_reason"] = reason
            selected.append(copy)
            selected_ids.add(media_id)
            topic_counts[topic] += 1
            format_counts[media_type] += 1
            return True

        strata = [
            (120, sorted(eligible, key=lambda row: row["scores"]["story_value"], reverse=True), "truth_value", "highest source-backed story value"),
            (40, sorted(eligible, key=lambda row: (row.get("performance_signal") or {}).get("cohort_percentile") or -1, reverse=True), "cohort_outlier", "high attention within format and era cohort"),
            (20, sorted(eligible, key=lambda row: (len(row["classification"]["audiences"]), len(row["classification"]["journey_stages"]), row["scores"]["story_value"]), reverse=True), "journey_coverage", "buyer, seller, or journey-stage coverage"),
            (20, sorted(eligible, key=lambda row: (len(row["classification"]["service_actions"]), bool(row["classification"]["local_relevance"]["evidence"]), row["scores"]["story_value"]), reverse=True), "proof_diversity", "service, local, and format diversity"),
        ]
        for quota, pool, stratum, reason in strata:
            start = len(selected)
            for row in pool:
                if len(selected) - start >= quota or len(selected) >= limit:
                    break
                add(row, stratum, reason)
        if len(selected) < limit:
            for row in sorted(eligible, key=lambda item: item["scores"]["story_value"], reverse=True):
                if len(selected) >= limit:
                    break
                add(row, "truth_value_overflow", "filled from remaining eligible evidence", relax_format=True)
        return selected

    def _story_entry(self, row: dict, number: int) -> dict:
        classification = row["classification"]
        media_id = row["media_id"]
        source_id = f"JEN-SRC-{media_id}"
        problem_evidence = classification["problem_evidence"]
        pursuit_evidence = classification["pursuit_evidence"]
        payoff_evidence = classification["payoff_evidence"]
        moment_parts = []
        for evidence in problem_evidence[:1] + pursuit_evidence[:1] + payoff_evidence[:1]:
            if evidence["text"] and evidence["text"] not in moment_parts:
                moment_parts.append(evidence["text"])
        bounded_moment = " ".join(moment_parts)
        story_id = f"JEN-STORY-{media_id}"
        actions = classification["service_actions"]
        beats_supported = sum(bool(value) for value in (problem_evidence, pursuit_evidence, payoff_evidence))
        full_story = bool(pursuit_evidence) and beats_supported == 3
        top_50_eligible = row["scores"]["story_value"] >= 65 and beats_supported >= 2 and bool(pursuit_evidence)
        privacy = classification["privacy"]
        title_source = bounded_moment or redact((row.get("caption") or "").splitlines()[0])
        return {
            "schema_version": "1.0",
            "story_id": story_id,
            "status": "DEEP_PACKET_ELIGIBLE" if top_50_eligible else "CANDIDATE",
            "title_internal": title_source[:100] if title_source else f"Archived post {media_id}",
            "bounded_moment": bounded_moment[:900],
            "story_type": classification["story_type"]["value"],
            "source_refs": [source_id],
            "source": {"source_id": source_id, "media_id": media_id, "permalink": row.get("permalink")},
            "audience": {"sides": [item["value"].upper() for item in classification["audiences"]], "stages": [item["value"] for item in classification["journey_stages"]], "desire": "a clear, handled move", "language_source_refs": []},
            "local_relevance": {"state": classification["local_relevance"]["state"], "evidence": classification["local_relevance"]["evidence"]},
            "problem": {"text": problem_evidence[0]["text"] if problem_evidence else None, "state": "SOURCE_SUPPORTED" if problem_evidence else "NEEDS_SOURCE", "evidence": problem_evidence[:2], "source_refs": [source_id] if problem_evidence else []},
            "pursuit": {"text": pursuit_evidence[0]["text"] if pursuit_evidence else None, "actions": [item["value"] for item in actions], "state": "SOURCE_SUPPORTED" if pursuit_evidence else "NEEDS_SOURCE", "evidence": pursuit_evidence[:3], "source_refs": [source_id] if pursuit_evidence else []},
            "payoff": {"text": payoff_evidence[0]["text"] if payoff_evidence else None, "payoff_type": "OBSERVED_OUTCOME" if payoff_evidence else "UNRESOLVED", "state": "SOURCE_SUPPORTED" if payoff_evidence else "NEEDS_SOURCE", "evidence": payoff_evidence[:2], "source_refs": [source_id] if payoff_evidence else []},
            "service_actions": [{"verb": action["value"], "action_summary": action["evidence"][0]["text"], "client_burden_removed": None, "observed_result": payoff_evidence[0]["text"] if payoff_evidence else None, "causal_claim_state": "NO_CAUSAL_CLAIM", "evidence": action["evidence"], "source_refs": [source_id]} for action in actions],
            "brand_throughline": {"whole_move_felt_handled": "DIRECT" if actions else "SUPPORTING", "client_knew_what_happened_next": "UNVERIFIED", "reason": "Source-reported action only; Jen review is required before a client-experience claim."},
            "narrative_status": "FULL_STORY_CANDIDATE" if full_story else "STORY_FRAGMENT_CANDIDATE",
            "proof": {"ceiling": "EXPERIENCE", "commercial_state": "NO_EVENT", "claim_safe_summary": bounded_moment[:500], "prohibited_upgrades": ["client emotion", "causal outcome", "guaranteed result"]},
            "performance_snapshot": row.get("performance_signal"),
            "privacy": privacy,
            "ranking": {"score": row["scores"]["story_value"], "rank": number, "top_50_eligible": top_50_eligible, "components": row["scores"]["components"], "selection_stratum": row.get("selection_stratum"), "selection_reason": row.get("selection_reason"), "exclusion_reasons": []},
            "topics": [classification["primary_topic"]["value"]],
            "created_at": now_iso(),
            "updated_at": now_iso(),
        }

    @staticmethod
    def _story_packet(story: dict, number: int) -> dict:
        return {
            "schema_version": "1.0",
            "packet_id": story["story_id"].replace("JEN-STORY-", "JEN-PACKET-"),
            "story_id": story["story_id"],
            "source_map": story["source_refs"],
            "bounded_moment": story["bounded_moment"],
            "problem": story["problem"],
            "pursuit": {"what_jen_noticed": [x for x in story["service_actions"] if x["verb"] == "NOTICED"], "what_jen_handled": [x for x in story["service_actions"] if x["verb"] == "HANDLED"], "what_jen_translated": [x for x in story["service_actions"] if x["verb"] == "TRANSLATED"], "what_jen_protected": [x for x in story["service_actions"] if x["verb"] == "PROTECTED"], "what_jen_prevented": [x for x in story["service_actions"] if x["verb"] == "PREVENTED"], "what_jen_removed_from_client_plate": [x for x in story["service_actions"] if x["verb"] == "REMOVED"], "action_sequence": story["pursuit"]["actions"], "source_refs": story["pursuit"]["source_refs"]},
            "payoff": {**story["payoff"], "emotional_payoff": None, "unresolved_truth": "Jen confirmation required for any client feeling or causal outcome."},
            "truth_boundary": {"safe_to_say": [item["text"] for key in ("problem", "pursuit", "payoff") for item in story[key].get("evidence", [])[:1]], "must_qualify": [], "do_not_say": story["proof"]["prohibited_upgrades"], "missing_facts": [key for key in ("problem", "pursuit", "payoff") if story[key]["state"] != "SOURCE_SUPPORTED"]},
            "privacy": story["privacy"],
            "continuity_opportunities": [],
            "recommended_retrieval_question": "What changed that you can verify?" if story["payoff"]["state"] != "SOURCE_SUPPORTED" else "What did you actually do after you noticed this?" if story["pursuit"]["state"] != "SOURCE_SUPPORTED" else "May we use the client-specific details in this story?",
            "packet_state": "NEEDS_PRIVACY_REVIEW" if story["privacy"]["state"] == "NEEDS_JEN_APPROVAL" else "NEEDS_SOURCE" if story["narrative_status"] != "FULL_STORY_CANDIDATE" else "READY",
        }

    @staticmethod
    def _derive_pillars(rows: list[dict]) -> list[dict]:
        support = defaultdict(list)
        for row in rows:
            topic = row["classification"]["primary_topic"]
            if topic["value"] != "unclassified" and topic["confidence"] >= 0.70 and row["review_state"] in {"AUTO_ACCEPT", "HUMAN_REVIEW"}:
                support[topic["value"]].append(row)
        pillars = []
        for index, (topic, topic_rows) in enumerate(sorted(support.items(), key=lambda item: len(item[1]), reverse=True), 1):
            by_id = {row["media_id"]: row for row in topic_rows}
            count = len(by_id)
            formats = Counter(row["media_type"] for row in by_id.values())
            periods = {int(datetime.fromisoformat(row["posted_at"]).timestamp() // (90 * 86400)) for row in by_id.values() if row.get("posted_at")}
            decision_or_service = sum(bool(row["classification"]["audiences"] or row["classification"]["service_actions"]) for row in by_id.values())
            threshold_met = count >= 20 and len(formats) >= 2 and len(periods) >= 3 and decision_or_service / max(1, count) >= 0.70
            state = "REVIEW_REQUIRED" if threshold_met else "EMERGING" if count >= 10 else "UNTESTED"
            format_evidence = {}
            for media_type, format_count in formats.items():
                values = [(row.get("performance_signal") or {}).get("cohort_percentile") for row in by_id.values() if row["media_type"] == media_type]
                values = [value for value in values if value is not None]
                format_evidence[media_type] = {"count": format_count, "median_percentile": round(statistics.median(values), 1) if values else None, "state": "SUPPORTED" if format_count >= 10 else "EXPERIMENT"}
            pillars.append({"pillar_id": f"JEN-PILLAR-{index:02d}", "internal_label": topic, "archive_state": state, "commercial_state": "NO_EVENT", "support_count": count, "source_post_ids": sorted(by_id), "gate_evidence": {"media_types": dict(formats), "distinct_90_day_periods": len(periods), "decision_or_service_ratio": round(decision_or_service / max(1, count), 3), "human_review_complete": False}, "format_evidence": format_evidence, "public_franchise_name": None})
        return pillars[:6]

    @staticmethod
    def _audience_language(rows: list[dict]) -> list[dict]:
        result = []
        for row in rows:
            text = redact(row.get("text_raw_private"))
            low = text.lower()
            agent_peer = bool(re.search(r"\b(?:realtor|real estate agent|broker|my clients?|content strategy|lead gen)\b", low))
            spam = bool(re.search(r"\b(?:promote it on|send pic|dm us|crypto|forex|investment return|check my page)\b", low))
            buyer_intent = bool(re.search(r"\b(?:buy|buying|buyer|offer|mortgage|pre[- ]?approv|down payment|first home)\b", low))
            seller_intent = bool(re.search(r"\b(?:sell|selling|seller|list my|listing my|home value|what is my home worth)\b", low))
            concrete_signals = {
                "place": bool(PRIMARY_TOPIC_RULES["local life and homes"].search(text)),
                "budget": bool(re.search(r"\$|\b\d{3,}(?:k|,\d{3})?\b|budget|payment", low)),
                "property": bool(re.search(r"\b(?:condo|townhome|house|home|property|bedroom|bathroom|yard|pool)\b", low)),
                "timeline": bool(re.search(r"\b(?:this (?:month|year|summer|fall|winter)|next (?:month|year)|soon|by [a-z]+|in \d+ months?|ready now)\b", low)),
                "ownership_change": bool(re.search(r"\b(?:renting|landlord|inherit|divorc|relocat|downsizing|growing family)\b", low)),
                "decision_help": "?" in text or bool(re.search(r"\b(?:can you help|what should|how do|where should|should i|need help)\b", low)),
            }
            intent = "buying_signal" if buyer_intent else "selling_signal" if seller_intent else "consumer_question" if "?" in text else "affinity"
            qualified = (buyer_intent or seller_intent) and any(concrete_signals.values()) and not agent_peer and not spam
            if intent == "affinity" and len(text) < 20:
                continue
            result.append({"comment_id": row["comment_id"], "media_id": row["media_id"], "curated_text_redacted": text, "intent_type": intent, "qualified_hand_raise": qualified, "concrete_signals": [name for name, present in concrete_signals.items() if present], "agent_peer_excluded": agent_peer, "spam_excluded": spam, "proof_effect": "AUDIENCE_LANGUAGE_ONLY", "privacy_state": "redacted_curated"})
        return result

    def _write_story_csv(self, stories: list[dict]) -> None:
        path = self.curated_root / "Jen Story Bank.csv"
        fields = ["rank", "story_id", "title_internal", "bounded_moment", "audience", "topics", "service_actions", "score", "source_media_id", "source_permalink", "privacy_state", "proof_ceiling", "packet_state"]
        with tempfile.NamedTemporaryFile("w", dir=path.parent, delete=False, newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            for story in stories:
                writer.writerow({"rank": story["ranking"]["rank"], "story_id": story["story_id"], "title_internal": story["title_internal"], "bounded_moment": story["bounded_moment"], "audience": "; ".join(story["audience"]["sides"]), "topics": "; ".join(story["topics"]), "service_actions": "; ".join(x["verb"] for x in story["service_actions"]), "score": story["ranking"]["score"], "source_media_id": story["source"]["media_id"], "source_permalink": story["source"]["permalink"], "privacy_state": story["privacy"]["state"], "proof_ceiling": story["proof"]["ceiling"], "packet_state": "DEEP" if story["ranking"]["top_50_eligible"] else "BANK"})
            temp_path = Path(handle.name)
        os.replace(temp_path, path)

    def _write_audience_csv(self, audience: list[dict]) -> None:
        path = self.curated_root / "Audience Questions + Language Bank.csv"
        fields = ["comment_id", "media_id", "curated_text_redacted", "intent_type", "qualified_hand_raise", "privacy_state", "build_state"]
        with tempfile.NamedTemporaryFile("w", dir=path.parent, delete=False, newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            if not audience:
                writer.writerow({
                    "comment_id": "SCOPE_NOTE",
                    "media_id": "",
                    "curated_text_redacted": "Comments and replies were waived by the operator; no audience-language corpus is represented in this baseline archive.",
                    "intent_type": "scope_note",
                    "qualified_hand_raise": False,
                    "privacy_state": "no_comment_data",
                    "build_state": "FINAL_CANDIDATE",
                })
            for row in audience:
                writer.writerow({key: row.get(key) for key in fields})
            temp_path = Path(handle.name)
        os.replace(temp_path, path)

    def _write_service_proof_doc(self, stories: list[dict]) -> None:
        lines = ["# Service Proof Library", "", "> Brand promise: The whole move feels handled.", "> Content proof: You will always know what happens next.", "", "Every claim below is source-linked and capped at the recorded proof ceiling.", ""]
        for story in stories:
            if not story["service_actions"]:
                continue
            lines.extend([f"## {story['ranking']['rank']}. {story['title_internal']}", "", story["bounded_moment"], "", f"- Jen service evidence: {', '.join(x['verb'] for x in story['service_actions'])}", f"- Source: {story['source']['permalink'] or story['source']['media_id']}", f"- Proof ceiling: {story['proof']['ceiling']}", f"- Privacy: {story['privacy']['state']}", ""])
        atomic_write_bytes(self.curated_root / "Service Proof Library.md", ("\n".join(lines) + "\n").encode())

    def _write_pillar_doc(self, pillars: list[dict]) -> None:
        lines = ["# Content Pillars + Format Map", "", "Internal labels only. A pillar is archive-backed at 20 reviewed examples; this is not commercial proof.", ""]
        for pillar in pillars:
            formats = ", ".join(f"{name}: {evidence['count']} ({evidence['state']})" for name, evidence in pillar["format_evidence"].items())
            lines.extend([f"## {pillar['internal_label'].title()}", "", f"- Archive state: {pillar['archive_state']}", f"- Support: {pillar['support_count']} unique posts", f"- Commercial state: {pillar['commercial_state']}", f"- Formats: {formats or 'No supported format yet'}", ""])
        lines.extend(["## Format rules", "", "- Silent/photo Reel: human or local evidence first; real estate enters on beat two.", "- Decision-map carousel: one claim per frame; proof before CTA.", "- Photo/caption handled moment: show what Jen removed from the client's plate.", "- Stories: recognition, one useful fact, then a calm reply or DM door.", ""])
        atomic_write_bytes(self.curated_root / "Content Pillars + Format Map.md", ("\n".join(lines) + "\n").encode())

    def _write_privacy_queue(self, stories: list[dict]) -> None:
        queue = [{"story_id": x["story_id"], "title": x["title_internal"], "reason": x["privacy"]["sensitivity_flags"], "source_permalink": x["source"]["permalink"]} for x in stories if x["privacy"]["state"] == "NEEDS_JEN_APPROVAL"]
        atomic_write_json(self.curated_root / "privacy-review-queue.json", queue)

    def _write_drive_manifest(self) -> None:
        files = []
        mapping = {
            "Jen Story Bank.csv": "google_sheet",
            "Service Proof Library.md": "google_doc",
            "Audience Questions + Language Bank.csv": "google_sheet",
            "Content Pillars + Format Map.md": "google_doc",
            "top-50-story-packets.json": "private_curated_file",
            "privacy-review-queue.json": "private_curated_file",
        }
        for name, target_type in mapping.items():
            path = self.curated_root / name
            if path.exists():
                files.append({"local_path": str(path), "sha256": sha256_bytes(path.read_bytes()), "target_type": target_type, "privacy": "curated_redacted"})
        atomic_write_json(self.curated_root / "drive-export-manifest.json", {"schema_version": "1.0", "private_archive_folder_name": "Jen · Content Intelligence Archive — PRIVATE", "shared_curated_folder_name": "00 · content bank — curated", "files": files, "drive_receipts": self.state.get("drive", {})})

    def _write_checkpoint_report(self, stories: list[dict], packets: list[dict], pillars: list[dict], receipt: dict) -> None:
        posts = self.load_posts()
        media_types = Counter(post.get("media_type") or "unknown" for post in posts)
        story_types = Counter(story.get("story_type") or "unknown" for story in stories)
        narrative_states = Counter(story.get("narrative_status") or "unknown" for story in stories)
        packet_states = Counter(packet.get("packet_state") or "unknown" for packet in packets)
        topics = Counter(topic for story in stories for topic in story.get("topics", []))
        actions = Counter(action.get("verb") for story in stories for action in story.get("service_actions", []))
        privacy = Counter(story.get("privacy", {}).get("state") or "unknown" for story in stories)
        profile = self.state.get("profile_reconciliation", {})
        highlights = self.state.get("highlights", {})
        media = self.state.get("media", {})
        comments = self.state.get("phases", {}).get("comments", {})
        reported_post_count = int(profile.get("reported_post_count") or len(posts))
        lines = [
            "# Jen Content Intelligence Bank — Checkpoint Report",
            "",
            "> Decision surface: the archive is a source system, not lead proof. Nothing here is approved for publishing until Jen clears voice, privacy, fair-housing, and story truth.",
            "",
            "## Outcome",
            "",
            f"- Source archive: **{len(posts):,} accessible posts** from **{reported_post_count:,} profile-reported posts**.",
            f"- Highlights: **WAIVED**; the already-captured snapshot of {highlights.get('count', 0):,} Highlights / {highlights.get('story_count', 0):,} stories remains private as a receipt and is excluded from analysis.",
            f"- Curated intelligence: **{len(stories)} Story Bank entries** and **{len(packets)} deep Story Packets**.",
            f"- Monid spend: **${self.state.get('project_spend_usd', 0.0):.3f}** of the **${self.state.get('project_ceiling_usd', 10.0):.2f}** project ceiling.",
            f"- Comments: **WAIVED** by the operator; one $0.003 canary is retained as a receipt and no comment corpus is represented.",
            "",
            "## What the archive actually says",
            "",
            "**VERIFIED:** Jen has a large human-and-local archive plus repeated client-move evidence. The strongest candidate pillar is client move stories; the remaining themes are context lenses until reviewed against buyer/seller decisions or explicit service actions.",
            "",
            "**Working inference:** Jen's most differentiated lane is not generic real-estate education. It is making a complex move feel understood and handled—using a human observation first, then showing the specific decision, translation, protection, or follow-through that removed uncertainty.",
            "",
            "**NOT PROVEN:** Likes, comments, and archive volume do not show that content generated DMs, consultations, clients, closings, or revenue. Commercial proof remains `NO_EVENT`.",
            "",
            "## Evidence map",
            "",
            "| Layer | Result | Interpretation |",
            "|---|---:|---|",
            f"| Images | {media_types.get('image', 0):,} | Largest source format |",
            f"| Carousels | {media_types.get('carousel', 0):,} | Strongest reusable teaching/story structure |",
            f"| Reels | {media_types.get('reel', 0):,} | Smaller historical pool; treat new Reel formats as tests |",
            f"| Full Problem/Pursuit/Payoff candidates | {narrative_states.get('FULL_STORY_CANDIDATE', 0):,} | All three story beats have source evidence |",
            f"| Client-journey or service-proof selections | {story_types.get('CLIENT_JOURNEY', 0) + story_types.get('SERVICE_PROOF', 0):,} | Directest route to handled-move proof, but not automatically complete |",
            f"| Personal-origin selections | {story_types.get('PERSONAL_ORIGIN', 0):,} | Human lens and trust material, not automatic sales proof |",
            f"| Fragments | {story_types.get('FRAGMENT', 0):,} | Retrieval prompts or supporting beats, not finished stories |",
            f"| Needs Jen privacy approval | {privacy.get('NEEDS_JEN_APPROVAL', 0):,} | Must stay out of publishing until cleared |",
            f"| Preserved media files | {media.get('preserved', 0):,} | Successfully downloaded |",
            f"| Attempted but unavailable | {media.get('unavailable', 0):,} | Explicit coverage gap, not silently omitted |",
            "",
            "## Kallaway content architecture",
            "",
            "Pillars are candidate strategy lanes. `REVIEW_REQUIRED` means the numeric threshold appears met but 20 examples still need human evidence review; `EMERGING` is not a validated public pillar.",
            "",
            "| Candidate pillar | Support | State | Best current use |",
            "|---|---:|---|---|",
        ]
        for pillar in pillars:
            use = "Review 20 examples for a core client-proof lane" if pillar["internal_label"] == "client move stories" else "Use as a human/local lens only when joined to a real decision or handled moment"
            lines.append(f"| {pillar['internal_label'].title()} | {pillar['support_count']:,} | {pillar['archive_state']} | {use} |")
        lines.extend([
            "",
            "## Jun story architecture",
            "",
            "Every deep packet retains a stable source ID, exact evidence spans, a Problem/Pursuit/Payoff truth state, privacy state, and a proof ceiling. Missing beats remain missing; no client feeling or causal outcome is invented.",
            "",
            f"- Packet readiness: {packet_states.get('READY', 0)} source-complete/privacy-clear; {packet_states.get('NEEDS_PRIVACY_REVIEW', 0)} need Jen approval; {packet_states.get('NEEDS_SOURCE', 0)} need a missing fact.",
            f"- Selection topics: {', '.join(f'{name} ({count})' for name, count in topics.most_common()) or 'none'}.",
            f"- Explicit service actions in the selected bank: {', '.join(f'{name} ({count})' for name, count in actions.most_common()) or 'none'}.",
            "- Continuity is intentionally unclaimed: the map contains retrieval questions until a dated later source proves a chain.",
            "",
            "## Coverage and truth limits",
            "",
            f"- Inventory gap: **{max(0, reported_post_count - len(posts))} post** reported by Instagram but not accessible through the extracted cursor set.",
            f"- Media state: **{self.state.get('phases', {}).get('media', {}).get('coverage_state', 'PENDING')}**.",
            "- Highlights were removed from scope and do not contribute evidence to the bank.",
            "- The Audience Questions + Language Bank is coverage-labeled and intentionally empty because comments were waived.",
            "- Raw usernames, raw captions, private paths, checksums, and sensitive source material remain in the private archive only.",
            "",
            "## Lead-path standard",
            "",
            "Attention → attributable DM → consultation → signed client → closing → collected revenue.",
            "",
            "Only the later stages advance commercial proof. The archive supplies source material and testable hypotheses; it does not manufacture a lead claim.",
            "",
            "## Decision",
            "",
            "**LOCKED:** `The whole move feels handled` is the internal service standard and selection lens.",
            "",
            "**PARKED:** public franchise names, trend-jacking, copied Coffee & Contracts identity, and a 30-day publishing pack before Story Bank review.",
            "",
            "**NEXT ACTION:** review 20 client-move examples and the top privacy queue, then promote only the evidence that survives into the first 12-asset publishing pack.",
            "",
            f"Build state: `{receipt.get('build_state')}` · Acceptance: `{receipt.get('acceptance_state')}` · Generated: `{receipt.get('generated_at')}`",
            "",
        ])
        report_path = self.curated_root / "Jen Content Intelligence Bank — Checkpoint Report.md"
        atomic_write_bytes(report_path, ("\n".join(lines)).encode())
        atomic_write_json(
            report_path.with_suffix(report_path.suffix + ".metadata.json"),
            {
                "title": "Jen Content Intelligence Bank — Checkpoint Report",
                "artifact_type": "strategy",
                "audience": "operator",
                "source_of_truth": str(self.private_root / "state.json"),
                "generated_at": receipt.get("generated_at"),
            },
        )

    def status(self) -> dict:
        result = dict(self.state)
        result["pending_ambiguous_call"] = load_json(self.pending_path, None)
        result["private_root"] = str(self.private_root)
        result["curated_root"] = str(self.curated_root)
        return result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Jen Instagram content intelligence archive")
    parser.add_argument("--root", type=Path, default=DEFAULT_PRIVATE_ROOT, help="Ignored private archive root")
    parser.add_argument("--curated-root", type=Path, default=DEFAULT_CURATED_ROOT)
    sub = parser.add_subparsers(dest="command", required=True)
    inventory = sub.add_parser("inventory")
    inventory.add_argument("--max-cost", type=float, default=0.50)
    comments = sub.add_parser("comments")
    comments.add_argument("--max-cost", type=float, default=3.0)
    comments.add_argument("--approved", action="store_true", help="Acknowledge explicit operator approval for a quote above $0.50")
    comments.add_argument("--endpoint-version", choices=("v1", "v2"), default="v2")
    canary = sub.add_parser("comments-canary")
    canary.add_argument("--endpoint-version", choices=("v1", "v2"), default="v2")
    sub.add_parser("highlights")
    sub.add_parser("reconcile-profile")
    build_bank = sub.add_parser("build-bank")
    build_bank.add_argument("--provisional", action="store_true")
    sub.add_parser("drive-export")
    media = sub.add_parser("media")
    media.add_argument("--top", type=int, default=200)
    media.add_argument("--workers", type=int, default=6)
    record_drive = sub.add_parser("record-drive")
    record_drive.add_argument("--private-folder-id", required=True)
    record_drive.add_argument("--private-url", required=True)
    record_drive.add_argument("--curated-folder-id", required=True)
    record_drive.add_argument("--curated-url", required=True)
    audit_state = sub.add_parser("audit-state")
    audit_state.add_argument("--rewind-comments", action="store_true")
    sub.add_parser("waive-comments")
    sub.add_parser("waive-highlights")
    sub.add_parser("status")
    sub.add_parser("inventory-receipt")
    recover = sub.add_parser("resolve-pending")
    recover.add_argument("--run-id", required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    with exclusive_archive_lock(args.root):
        archive = JenArchive(args.root, args.curated_root)
        if args.command == "inventory":
            result = archive.inventory(args.max_cost)
        elif args.command == "comments":
            result = archive.comments(args.max_cost, approved=args.approved, endpoint_version=args.endpoint_version)
        elif args.command == "comments-canary":
            result = archive.comments_canary(args.endpoint_version)
        elif args.command == "highlights":
            result = archive.highlights()
        elif args.command == "reconcile-profile":
            result = archive.reconcile_profile_count()
        elif args.command == "build-bank":
            result = archive.build_bank(provisional=args.provisional)
        elif args.command == "drive-export":
            archive._write_drive_manifest()
            result = {"manifest": str(archive.curated_root / "drive-export-manifest.json"), "note": "Use the authenticated Drive connector to create or update files; record returned IDs in state.drive."}
        elif args.command == "media":
            result = archive.preserve_media(top=args.top, workers=args.workers)
        elif args.command == "record-drive":
            result = archive.record_drive(args.private_folder_id, args.private_url, args.curated_folder_id, args.curated_url)
        elif args.command == "audit-state":
            result = archive.audit_state_from_raw(rewind_comments=args.rewind_comments)
        elif args.command == "waive-comments":
            result = archive.waive_comments()
        elif args.command == "waive-highlights":
            result = archive.waive_highlights()
        elif args.command == "resolve-pending":
            result = archive.resolve_pending(args.run_id)
        elif args.command == "inventory-receipt":
            result = archive.inventory_receipt()
        else:
            result = archive.status()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
