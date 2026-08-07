#!/usr/bin/env python3
"""Kallaway Trend Hook Radar.

Local Sandcastles-gap workflow for compliant signal intake, outlier scoring,
hook pattern clustering, creative-reaction prompts, and book/content opportunity
mapping. The script is intentionally useful with manual or owned data first; it
only calls budget-guarded public-data tooling when explicitly requested.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import os
import re
import statistics
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_PACKAGE = ROOT / "extractions" / "video-context" / "a7VjpIqq8Xk"
DEFAULT_OUTPUT_ROOT = (
    ROOT
    / "_active"
    / "farrice-content-os"
    / "04-deliverables"
    / "kallaway-trend-hook-engine"
)

APPROVED_LINKEDIN_STATUSES = {
    "approved",
    "approved_csv",
    "owned",
    "owned_metrics",
    "export",
    "exported",
    "screenshot",
    "manual",
    "manual_reference",
}

FIELD_ALIASES = {
    "platform": ["platform", "channel_platform", "network"],
    "source_ref": ["source_ref", "source", "source_name", "dataset", "watchlist"],
    "creator": ["creator", "channel", "author", "handle", "account"],
    "url": ["url", "link", "permalink", "post_url", "video_url"],
    "published_at": ["published_at", "date", "posted_at", "created_at", "published"],
    "title": ["title", "headline", "post_title"],
    "hook_text": ["hook_text", "hook", "opening", "first_line", "lead", "title"],
    "caption": ["caption", "body", "text", "transcript_excerpt", "description"],
    "topic": ["topic", "category", "content_topic", "idea"],
    "format_hint": ["format_hint", "format", "content_format", "post_type"],
    "views": ["views", "view_count", "plays", "impressions"],
    "likes": ["likes", "like_count", "reactions"],
    "comments": ["comments", "comment_count", "replies"],
    "shares": ["shares", "share_count", "reposts"],
    "saves": ["saves", "save_count", "bookmarks"],
    "leads": ["leads", "conversions", "email_signups", "sales_calls", "qualified_leads"],
    "avg_views": ["avg_views", "average_views", "baseline_views", "creator_avg_views"],
    "follower_count": ["follower_count", "followers", "subscriber_count", "subscribers"],
    "paid_brand_deal": ["paid_brand_deal", "sponsored", "ad", "brand_deal"],
    "permission_status": ["permission_status", "approval", "evidence_permission"],
    "evidence_lane": ["evidence_lane", "lane", "input_lane"],
}


@dataclass
class SignalItem:
    signal_id: str
    platform: str
    source_ref: str
    creator: str
    url: str
    published_at: str
    title: str
    hook_text: str
    caption: str
    topic: str
    format_hint: str
    views: float | None
    likes: float | None
    comments: float | None
    shares: float | None
    saves: float | None
    leads: float | None
    avg_views: float | None
    follower_count: float | None
    paid_brand_deal: bool
    permission_status: str
    evidence_lane: str
    input_path: str
    compliance_status: str
    included: bool
    exclusion_reason: str = ""
    raw: dict[str, Any] = field(default_factory=dict)


@dataclass
class OutlierScore:
    signal_id: str
    platform: str
    creator: str
    hook_text: str
    topic: str
    url: str
    views: float | None
    baseline_views: float | None
    outlier_multiplier: float | None
    engagement_rate: float | None
    lead_rate: float | None
    outlier_score: float
    confidence: str
    winner_line_status: str
    reason_codes: list[str]


@dataclass
class HookPattern:
    pattern_id: str
    desire_template: str
    hook_format: str
    signal_count: int
    avg_outlier_score: float
    max_views: float
    confidence: str
    sample_hooks: list[str]
    source_signal_ids: list[str]
    book_opportunity: str


@dataclass
class CreativeReactionPrompt:
    prompt_id: str
    source_pattern_id: str
    human_question: str
    evidence_prompt: str
    candidate_hook_moves: list[str]
    next_component: str


@dataclass
class RunReceipt:
    run_id: str
    generated_at: str
    source_package: str
    source_counts: dict[str, int]
    input_files: list[str]
    signal_count: int
    included_signal_count: int
    excluded_signal_count: int
    apify_status: list[dict[str, Any]]
    compliance_boundary: list[str]
    output_files: dict[str, str]
    next_workflow_chain: list[str]


def clean_text(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def normalize_key(key: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", key.lower()).strip("_")


def coerce_number(value: Any) -> float | None:
    text = clean_text(value)
    if not text:
        return None
    text = text.replace(",", "").replace("$", "").replace("%", "")
    multiplier = 1.0
    if text.lower().endswith("k"):
        multiplier = 1_000.0
        text = text[:-1]
    elif text.lower().endswith("m"):
        multiplier = 1_000_000.0
        text = text[:-1]
    try:
        return float(text) * multiplier
    except ValueError:
        return None


def coerce_bool(value: Any) -> bool:
    return clean_text(value).lower() in {"1", "true", "yes", "y", "paid", "sponsored", "ad"}


def first_present(row: dict[str, Any], canonical: str) -> str:
    aliases = FIELD_ALIASES.get(canonical, [canonical])
    for alias in aliases:
        normalized_alias = normalize_key(alias)
        if normalized_alias in row and clean_text(row[normalized_alias]):
            return clean_text(row[normalized_alias])
    return ""


def stable_id(row: dict[str, Any], input_path: str, index: int) -> str:
    base = "|".join(
        [
            first_present(row, "platform"),
            first_present(row, "creator"),
            first_present(row, "url"),
            first_present(row, "hook_text"),
            input_path,
            str(index),
        ]
    )
    return hashlib.sha1(base.encode("utf-8")).hexdigest()[:12]


def compliance_for(row: dict[str, Any], input_lane: str, platform: str) -> tuple[str, bool, str]:
    platform = platform.lower()
    permission = first_present(row, "permission_status").lower() or input_lane.lower()
    lane = first_present(row, "evidence_lane").lower() or input_lane.lower()

    if platform == "linkedin":
        approved = permission in APPROVED_LINKEDIN_STATUSES or lane in APPROVED_LINKEDIN_STATUSES
        if not approved:
            return (
                "rejected",
                False,
                "LinkedIn rows require approved CSV/export/screenshot/owned/manual evidence status.",
            )
        return ("approved_linkedin_evidence", True, "")

    if input_lane in {"manual_csv", "owned_metrics", "public_web", "apify_public"}:
        return ("approved_read_only", True, "")

    return ("approved_read_only", True, "")


def signal_from_row(row: dict[str, Any], input_path: str, index: int, input_lane: str) -> SignalItem:
    normalized_row = {normalize_key(k): v for k, v in row.items()}
    platform = first_present(normalized_row, "platform").lower() or "unknown"
    compliance_status, included, exclusion = compliance_for(normalized_row, input_lane, platform)
    paid_brand_deal = coerce_bool(first_present(normalized_row, "paid_brand_deal"))
    if paid_brand_deal:
        included = False
        exclusion = "Paid or sponsored item excluded from outlier winner set."

    hook_text = first_present(normalized_row, "hook_text")
    title = first_present(normalized_row, "title")
    caption = first_present(normalized_row, "caption")
    if not hook_text:
        hook_text = title or caption[:180]

    return SignalItem(
        signal_id=stable_id(normalized_row, input_path, index),
        platform=platform,
        source_ref=first_present(normalized_row, "source_ref") or input_lane,
        creator=first_present(normalized_row, "creator") or "unknown",
        url=first_present(normalized_row, "url"),
        published_at=first_present(normalized_row, "published_at"),
        title=title,
        hook_text=hook_text,
        caption=caption,
        topic=first_present(normalized_row, "topic") or infer_topic(hook_text or caption),
        format_hint=first_present(normalized_row, "format_hint"),
        views=coerce_number(first_present(normalized_row, "views")),
        likes=coerce_number(first_present(normalized_row, "likes")),
        comments=coerce_number(first_present(normalized_row, "comments")),
        shares=coerce_number(first_present(normalized_row, "shares")),
        saves=coerce_number(first_present(normalized_row, "saves")),
        leads=coerce_number(first_present(normalized_row, "leads")),
        avg_views=coerce_number(first_present(normalized_row, "avg_views")),
        follower_count=coerce_number(first_present(normalized_row, "follower_count")),
        paid_brand_deal=paid_brand_deal,
        permission_status=first_present(normalized_row, "permission_status"),
        evidence_lane=first_present(normalized_row, "evidence_lane") or input_lane,
        input_path=input_path,
        compliance_status=compliance_status,
        included=included,
        exclusion_reason=exclusion,
        raw=dict(normalized_row),
    )


def load_csv(path: Path, input_lane: str) -> list[SignalItem]:
    if not path.exists():
        raise FileNotFoundError(f"Input CSV not found: {path}")
    signals: list[SignalItem] = []
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        for index, row in enumerate(reader, start=1):
            signals.append(signal_from_row(row, str(path), index, input_lane))
    return signals


def load_json(path: Path, input_lane: str) -> list[SignalItem]:
    if not path.exists():
        raise FileNotFoundError(f"Input JSON not found: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    rows = data if isinstance(data, list) else data.get("items", [])
    signals: list[SignalItem] = []
    for index, row in enumerate(rows, start=1):
        if isinstance(row, dict):
            signals.append(signal_from_row(row, str(path), index, input_lane))
    return signals


def infer_topic(text: str) -> str:
    words = [
        word.lower()
        for word in re.findall(r"[a-zA-Z][a-zA-Z0-9'-]{3,}", text)
        if word.lower()
        not in {
            "this",
            "that",
            "with",
            "from",
            "your",
            "have",
            "about",
            "what",
            "when",
            "into",
            "will",
            "hook",
            "hooks",
            "video",
            "content",
        }
    ]
    return " ".join(words[:3]) if words else "uncategorized"


def median(values: Iterable[float]) -> float | None:
    clean = [value for value in values if value and value > 0]
    if not clean:
        return None
    return statistics.median(clean)


def group_key(signal: SignalItem) -> str:
    return f"{signal.platform}:{signal.creator}".lower()


def compute_group_baselines(signals: list[SignalItem]) -> dict[str, float]:
    by_group: dict[str, list[float]] = {}
    global_views: list[float] = []
    for signal in signals:
        if not signal.included or signal.views is None or signal.views <= 0:
            continue
        global_views.append(signal.views)
        by_group.setdefault(group_key(signal), []).append(signal.views)

    global_median = median(global_views)
    baselines: dict[str, float] = {}
    for key, views in by_group.items():
        if len(views) >= 3:
            group_median = median(views)
            if group_median:
                baselines[key] = group_median
        elif global_median:
            baselines[key] = global_median
    return baselines


def engagement_rate(signal: SignalItem) -> float | None:
    if not signal.views or signal.views <= 0:
        return None
    actions = sum(
        value or 0
        for value in [signal.likes, signal.comments, signal.shares, signal.saves]
    )
    if actions <= 0:
        return None
    return actions / signal.views


def lead_rate(signal: SignalItem) -> float | None:
    if not signal.views or signal.views <= 0 or not signal.leads:
        return None
    return signal.leads / signal.views


def percentile_rank(value: float, population: list[float]) -> float:
    if not population:
        return 0.0
    below_or_equal = sum(1 for item in population if item <= value)
    return below_or_equal / len(population)


def preliminary_score(signal: SignalItem, baseline: float | None, population: list[float]) -> tuple[float, float | None]:
    multiplier = None
    if signal.views and baseline and baseline > 0:
        multiplier = signal.views / baseline
        score = multiplier
    elif signal.views:
        score = 0.5 + percentile_rank(signal.views, population) * 1.5
    else:
        score = 0.0

    er = engagement_rate(signal) or 0.0
    lr = lead_rate(signal) or 0.0
    score *= 1 + min(0.35, er * 2.0)
    score *= 1 + min(0.25, lr * 5.0)
    return round(score, 4), multiplier


def winner_thresholds(scores: list[tuple[SignalItem, float]]) -> dict[str, float]:
    by_group: dict[str, list[float]] = {}
    for signal, score in scores:
        by_group.setdefault(group_key(signal), []).append(score)

    thresholds: dict[str, float] = {}
    for key, values in by_group.items():
        values = sorted([value for value in values if value > 0], reverse=True)
        threshold = 1.5
        if len(values) >= 4:
            drops = []
            for idx in range(len(values) - 1):
                next_value = max(values[idx + 1], 0.001)
                drops.append((values[idx] / next_value, idx))
            largest_drop, index = max(drops, key=lambda item: item[0])
            if largest_drop >= 1.4:
                threshold = max(1.2, values[index + 1] + 0.001)
        thresholds[key] = threshold
    return thresholds


def confidence_for(signal: SignalItem, multiplier: float | None) -> str:
    has_source = bool(signal.url or signal.source_ref)
    has_hook = bool(signal.hook_text)
    if multiplier is not None and has_hook and has_source:
        return "high"
    if signal.views is not None and has_hook:
        return "medium"
    return "low"


def score_signals(signals: list[SignalItem]) -> list[OutlierScore]:
    included = [signal for signal in signals if signal.included]
    baselines = compute_group_baselines(included)
    population = [signal.views for signal in included if signal.views and signal.views > 0]

    prelim: list[tuple[SignalItem, float, float | None, float | None]] = []
    for signal in included:
        baseline = signal.avg_views or baselines.get(group_key(signal))
        score, multiplier = preliminary_score(signal, baseline, population)
        prelim.append((signal, score, multiplier, baseline))

    thresholds = winner_thresholds([(signal, score) for signal, score, _mult, _base in prelim])
    scored: list[OutlierScore] = []
    for signal, score, multiplier, baseline in prelim:
        threshold = thresholds.get(group_key(signal), 1.5)
        if score >= threshold:
            status = "above_winner_line"
        elif score >= 1.0:
            status = "study_but_not_winner"
        else:
            status = "below_winner_line"

        reason_codes = []
        if multiplier is not None:
            reason_codes.append(f"baseline_multiplier={multiplier:.2f}")
        elif signal.views:
            reason_codes.append("views_present_no_creator_baseline")
        else:
            reason_codes.append("missing_views")
        if engagement_rate(signal) is not None:
            reason_codes.append("engagement_signal")
        if lead_rate(signal) is not None:
            reason_codes.append("conversion_signal")
        if signal.platform == "linkedin":
            reason_codes.append("approved_linkedin_read_only")

        scored.append(
            OutlierScore(
                signal_id=signal.signal_id,
                platform=signal.platform,
                creator=signal.creator,
                hook_text=signal.hook_text,
                topic=signal.topic,
                url=signal.url,
                views=signal.views,
                baseline_views=baseline,
                outlier_multiplier=round(multiplier, 4) if multiplier is not None else None,
                engagement_rate=round(engagement_rate(signal), 6) if engagement_rate(signal) is not None else None,
                lead_rate=round(lead_rate(signal), 6) if lead_rate(signal) is not None else None,
                outlier_score=score,
                confidence=confidence_for(signal, multiplier),
                winner_line_status=status,
                reason_codes=reason_codes,
            )
        )
    return sorted(scored, key=lambda item: item.outlier_score, reverse=True)


def hook_format(text: str) -> str:
    lowered = text.lower().strip()
    if not lowered:
        return "missing-hook"
    if re.match(r"^(how to|how i|the system|the framework|copy this)\b", lowered):
        return "tutorial-system"
    if "?" in lowered or re.match(r"^(why|what|how|when|where|who)\b", lowered):
        return "question"
    if re.search(r"(^|\s)(\d+|\$[0-9]|[0-9]+%)", lowered):
        return "specific-number"
    if re.search(r"\b(i was wrong|i stopped|mistake|confession|i used to)\b", lowered):
        return "confession"
    if re.search(r"\b(vs\.?|versus|instead of|before|after|difference between|not .+ but)\b", lowered):
        return "contrast"
    if re.search(r"\b(stop|don't|avoid|warning|never)\b", lowered):
        return "warning"
    if re.match(r"^(\d+|five|three|seven|ten)\b", lowered):
        return "list"
    if re.match(r"^(if you|for creators|for founders|for anyone)\b", lowered):
        return "identity"
    if re.search(r"\b(without|even if|using only|in [0-9]+ days?|no .+ required)\b", lowered):
        return "condition-free"
    return "concrete-declarative"


def desire_template(text: str) -> str:
    lowered = text.lower()
    if re.search(r"\b(without|even if|no .+ required|using only|in [0-9]+ days?)\b", lowered):
        return "Condition-Free Method"
    if re.search(r"\b(secret|unfair|edge|cheat|template|system|machine|framework)\b", lowered):
        return "Unfair-Advantage Filter"
    if re.search(r"\b(i|we|regular people|beginner|founder|creator)\b", lowered):
        return "Relatable Character"
    if re.search(r"\b(get|grow|build|make|earn|create|win|blow up|perform better)\b", lowered):
        return "Dream Outcome"
    return "Specificity-First Declarative"


def pattern_confidence(count: int, avg_score: float) -> str:
    if count >= 3 and avg_score >= 1.5:
        return "high"
    if count >= 2 and avg_score >= 1.0:
        return "medium"
    return "low"


def book_opportunity_for(template: str, fmt: str) -> str:
    if template == "Condition-Free Method":
        return "Turn the constraint into a chapter promise: outcome without the old prerequisite."
    if template == "Unfair-Advantage Filter":
        return "Build a chapter around the mechanism, then show ethical use cases and proof."
    if template == "Relatable Character":
        return "Use this as a case-study spine: person, constraint, decision, result, lesson."
    if template == "Dream Outcome":
        return "Open a section with the desired future, then backfill the method and proof."
    if fmt == "specific-number":
        return "Use as a scoreboard or benchmark chapter with measurable before/after proof."
    return "Use as a repeatable content series prompt; collect stronger source examples before book packaging."


def cluster_patterns(scored: list[OutlierScore]) -> list[HookPattern]:
    winners = [item for item in scored if item.winner_line_status == "above_winner_line"]
    if not winners:
        winners = scored[: min(5, len(scored))]

    groups: dict[tuple[str, str], list[OutlierScore]] = {}
    for item in winners:
        fmt = hook_format(item.hook_text)
        template = desire_template(item.hook_text)
        groups.setdefault((template, fmt), []).append(item)

    patterns: list[HookPattern] = []
    for (template, fmt), items in groups.items():
        avg_score = round(sum(item.outlier_score for item in items) / len(items), 4)
        max_views = max([item.views or 0 for item in items], default=0)
        digest = hashlib.sha1(f"{template}|{fmt}".encode("utf-8")).hexdigest()[:8]
        samples = [item.hook_text for item in sorted(items, key=lambda x: x.outlier_score, reverse=True)[:3]]
        patterns.append(
            HookPattern(
                pattern_id=f"pattern-{digest}",
                desire_template=template,
                hook_format=fmt,
                signal_count=len(items),
                avg_outlier_score=avg_score,
                max_views=max_views,
                confidence=pattern_confidence(len(items), avg_score),
                sample_hooks=samples,
                source_signal_ids=[item.signal_id for item in items],
                book_opportunity=book_opportunity_for(template, fmt),
            )
        )
    return sorted(patterns, key=lambda item: (item.avg_outlier_score, item.signal_count), reverse=True)


def candidate_moves(pattern: HookPattern, topics: list[str], business_objective: str) -> list[str]:
    topic = topics[0] if topics else "[topic]"
    objective = business_objective or "create a measurable business result"
    if pattern.desire_template == "Condition-Free Method":
        return [
            f"How to use {topic} to {objective} without the usual prerequisite",
            f"The {topic} method for creators trying to {objective}, even if they are starting cold",
            f"Stop waiting for permission before using {topic} to {objective}",
        ]
    if pattern.desire_template == "Unfair-Advantage Filter":
        return [
            f"The unfair {topic} advantage most people miss",
            f"Copy this {topic} system before the market catches up",
            f"The hidden mechanism that helps you {objective}",
        ]
    if pattern.desire_template == "Relatable Character":
        return [
            f"I was wrong about {topic} until this changed the result",
            f"How a normal creator can use {topic} to {objective}",
            f"The mistake I kept making with {topic}",
        ]
    return [
        f"How to use {topic} to {objective}",
        f"The difference between average {topic} and a real engine that helps you {objective}",
        f"Most {topic} advice delays the payoff. This frontloads it.",
    ]


def creative_prompts(
    patterns: list[HookPattern],
    topics: list[str],
    business_objective: str,
) -> list[CreativeReactionPrompt]:
    prompts: list[CreativeReactionPrompt] = []
    for index, pattern in enumerate(patterns[:8], start=1):
        prompts.append(
            CreativeReactionPrompt(
                prompt_id=f"reaction-{index:02d}",
                source_pattern_id=pattern.pattern_id,
                human_question=(
                    "What is your non-obvious take on this pattern that a generic AI would not say?"
                ),
                evidence_prompt=(
                    f"Pattern uses {pattern.desire_template} plus {pattern.hook_format}; "
                    f"avg score {pattern.avg_outlier_score} from {pattern.signal_count} signal(s)."
                ),
                candidate_hook_moves=candidate_moves(pattern, topics, business_objective),
                next_component="/kcs-topic-format -> /kcs-hook-triad -> /ai-creative-sprint",
            )
        )
    return prompts


def source_counts(source_package: Path) -> dict[str, int]:
    ledger = source_package / "video-context-ledger.json"
    counts: dict[str, int] = {}
    if not ledger.exists():
        return counts
    try:
        rows = json.loads(ledger.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return counts
    if not isinstance(rows, list):
        return counts
    for row in rows:
        if not isinstance(row, dict):
            continue
        kind = clean_text(row.get("type")) or "unknown"
        counts[kind] = counts.get(kind, 0) + 1
    return counts


def apify_payload_for(lane: str, query: str, limit: int) -> dict[str, Any]:
    if lane == "reddit":
        return {
            "startUrls": [{"url": f"https://www.reddit.com/search/?q={query.replace(' ', '+')}&type=link&sort=relevance"}],
            "maxItems": limit,
            "scrollTimeout": 40,
            "skipComments": True,
            "skipUserPosts": False,
            "skipCommunity": False,
        }
    if lane == "youtube":
        return {"keywords": [query], "maxItems": limit, "downloadSubtitles": True, "subtitlesLanguage": "en"}
    if lane == "tiktok":
        return {"hashtags": [query.lstrip("#")], "resultsPerPage": limit}
    if lane == "instagram":
        return {"directUrls": [f"https://www.instagram.com/{query.lstrip('@')}/"], "resultsType": "posts", "resultsLimit": limit}
    if lane == "web":
        return {"query": query, "maxResults": limit}
    return {"query": query, "maxItems": limit}


def signal_from_apify_item(item: dict[str, Any], lane: str, query: str, index: int) -> SignalItem:
    row = {
        "platform": lane,
        "source_ref": f"apify:{lane}:{query}",
        "creator": item.get("author")
        or item.get("channelName")
        or item.get("ownerUsername")
        or item.get("username")
        or item.get("user")
        or query,
        "url": item.get("url") or item.get("link") or item.get("shortLink") or "",
        "published_at": item.get("date") or item.get("publishedAt") or item.get("timestamp") or "",
        "title": item.get("title") or item.get("text") or item.get("caption") or "",
        "hook_text": item.get("title") or item.get("text") or item.get("caption") or "",
        "caption": item.get("text") or item.get("description") or item.get("caption") or "",
        "topic": query,
        "views": item.get("viewCount") or item.get("views") or item.get("playCount") or item.get("numViews"),
        "likes": item.get("likeCount") or item.get("likes"),
        "comments": item.get("commentCount") or item.get("comments"),
        "shares": item.get("shareCount") or item.get("shares"),
        "saves": item.get("saveCount") or item.get("bookmarks"),
        "evidence_lane": "apify_public",
        "permission_status": "public_read_only",
    }
    signal = signal_from_row(row, f"apify:{lane}:{query}", index, "apify_public")
    signal.raw = item
    return signal


def collect_apify_signals(
    lanes: list[str],
    queries: list[str],
    limit: int,
    execute: bool,
) -> tuple[list[SignalItem], list[dict[str, Any]]]:
    statuses: list[dict[str, Any]] = []
    if not execute:
        return [], [
            {
                "status": "skipped",
                "fallback": True,
                "message": "Public data actors were not executed. Use --execute-apify after confirming budget and permissions.",
            }
        ]

    sys.path.insert(0, str(ROOT / "execution"))
    try:
        import apify_client  # type: ignore
    except Exception as exc:  # pragma: no cover - defensive local fallback
        return [], [
            {
                "status": "error",
                "fallback": True,
                "message": f"Could not load execution/apify_client.py: {exc}",
            }
        ]

    apify_client.load_env()
    signals: list[SignalItem] = []
    for lane in lanes:
        for query in queries:
            payload = apify_payload_for(lane, query, limit)
            result = apify_client.run_actor(lane, payload, limit)
            statuses.append(
                {
                    "lane": lane,
                    "query": query,
                    "status": result.get("status"),
                    "fallback": result.get("fallback", False),
                    "message": result.get("message", ""),
                    "result_count": result.get("result_count", len(result.get("items", []))),
                    "cost_dollars": result.get("cost_dollars", 0),
                }
            )
            for index, item in enumerate(result.get("items", []), start=1):
                if isinstance(item, dict):
                    signals.append(signal_from_apify_item(item, lane, query, index))
    return signals, statuses


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_markdown_with_metadata(path: Path, content: str, run_id: str, title: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    metadata = {
        "userFacingSurface": "rendered-conversation-document",
        "sourceRole": "persistence-copy",
        "externalExportRequested": False,
        "title": title,
        "runId": run_id,
        "generatedBy": "execution/kallaway_trend_hook_radar.py",
        "updatedAt": datetime.now().isoformat(timespec="seconds"),
    }
    write_json(path.with_name(path.name + ".metadata.json"), metadata)


def write_outlier_csv(path: Path, scores: list[OutlierScore], excluded: list[SignalItem]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    headers = [
        "signal_id",
        "platform",
        "creator",
        "topic",
        "hook_text",
        "url",
        "views",
        "baseline_views",
        "outlier_multiplier",
        "engagement_rate",
        "lead_rate",
        "outlier_score",
        "confidence",
        "winner_line_status",
        "reason_codes",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers)
        writer.writeheader()
        for score in scores:
            row = asdict(score)
            row["reason_codes"] = ";".join(score.reason_codes)
            writer.writerow(row)
        for signal in excluded:
            writer.writerow(
                {
                    "signal_id": signal.signal_id,
                    "platform": signal.platform,
                    "creator": signal.creator,
                    "topic": signal.topic,
                    "hook_text": signal.hook_text,
                    "url": signal.url,
                    "views": signal.views,
                    "confidence": "excluded",
                    "winner_line_status": "excluded",
                    "reason_codes": signal.exclusion_reason or signal.compliance_status,
                }
            )


def fmt_number(value: float | int | None) -> str:
    if value is None:
        return ""
    if isinstance(value, float) and math.isnan(value):
        return ""
    if abs(float(value)) >= 1_000_000:
        return f"{float(value) / 1_000_000:.1f}M"
    if abs(float(value)) >= 1_000:
        return f"{float(value) / 1_000:.1f}K"
    return f"{float(value):.0f}"


def markdown_table(rows: list[list[str]], headers: list[str]) -> list[str]:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        safe = [cell.replace("|", "/").replace("\n", " ") for cell in row]
        lines.append("| " + " | ".join(safe) + " |")
    return lines


def render_pattern_report(
    run_id: str,
    source_package: Path,
    signals: list[SignalItem],
    scores: list[OutlierScore],
    patterns: list[HookPattern],
) -> str:
    lines = [
        "# Kallaway Trend Hook Radar - Hook Pattern Report",
        "",
        f"Run ID: `{run_id}`",
        f"Source package: `{source_package.relative_to(ROOT) if source_package.is_relative_to(ROOT) else source_package}`",
        "",
        "## Evidence Boundary",
        "",
        "- Source-grounded Kallaway method: local video-context ledger for `a7VjpIqq8Xk`.",
        "- Trend claims in this report come only from supplied rows or explicit public-data runs.",
        "- LinkedIn rows are accepted only from approved CSV/export/screenshot/owned/manual evidence.",
        "- OCR for the source video is unavailable; visual claims require human review or a vision adapter.",
        "",
        "## Signal Summary",
        "",
        f"- Total normalized signals: {len(signals)}",
        f"- Included in scoring: {sum(1 for signal in signals if signal.included)}",
        f"- Excluded by compliance/sponsor filters: {sum(1 for signal in signals if not signal.included)}",
        f"- Above winner line: {sum(1 for score in scores if score.winner_line_status == 'above_winner_line')}",
        "",
    ]

    if not scores:
        lines.extend(
            [
                "## No Trend Claims Yet",
                "",
                "No compliant performance rows were supplied, so this run does not claim anything is trending.",
                "",
                "Next data step: provide a manual CSV, owned analytics export, or approved public-data run with at least `platform`, `creator`, `hook_text`, `views`, and ideally `avg_views`.",
                "",
            ]
        )
        return "\n".join(lines) + "\n"

    top_rows = []
    for score in scores[:10]:
        top_rows.append(
            [
                score.platform,
                score.creator,
                score.topic,
                fmt_number(score.views),
                f"{score.outlier_score:.2f}",
                score.confidence,
                score.winner_line_status,
                score.hook_text[:90],
            ]
        )
    lines.extend(["## Outlier Ledger Preview", ""])
    lines.extend(
        markdown_table(
            top_rows,
            ["Platform", "Creator", "Topic", "Views", "Score", "Confidence", "Line", "Hook"],
        )
    )
    lines.append("")

    if not patterns:
        lines.extend(
            [
                "## Hook Pattern Clusters",
                "",
                "No stable hook clusters were found yet. Add more rows per creator or topic to move from one-off examples to repeatable patterns.",
                "",
            ]
        )
        return "\n".join(lines) + "\n"

    pattern_rows = []
    for pattern in patterns:
        pattern_rows.append(
            [
                pattern.pattern_id,
                pattern.desire_template,
                pattern.hook_format,
                str(pattern.signal_count),
                f"{pattern.avg_outlier_score:.2f}",
                fmt_number(pattern.max_views),
                pattern.confidence,
            ]
        )
    lines.extend(["## Hook Pattern Clusters", ""])
    lines.extend(
        markdown_table(
            pattern_rows,
            ["Pattern", "Desire Template", "Hook Format", "Signals", "Avg Score", "Max Views", "Confidence"],
        )
    )
    lines.append("")

    lines.extend(["## Pattern Notes", ""])
    for pattern in patterns[:8]:
        lines.extend(
            [
                f"### {pattern.pattern_id}: {pattern.desire_template} / {pattern.hook_format}",
                "",
                f"- Average outlier score: {pattern.avg_outlier_score:.2f}",
                f"- Confidence: {pattern.confidence}",
                f"- Book/content opportunity: {pattern.book_opportunity}",
                "- Sample hooks:",
            ]
        )
        for hook in pattern.sample_hooks:
            lines.append(f"  - {hook[:180]}")
        lines.append("")

    return "\n".join(lines) + "\n"


def render_creative_brief(
    run_id: str,
    prompts: list[CreativeReactionPrompt],
    topics: list[str],
    business_objective: str,
) -> str:
    lines = [
        "# Kallaway Trend Hook Radar - Creative Reaction Brief",
        "",
        f"Run ID: `{run_id}`",
        "",
        "## Creative Boundary",
        "",
        "This brief gives the human creator a pattern-backed starting point. It does not decide the take, stance, story, or voice.",
        "",
        f"- Target topics: {', '.join(topics) if topics else 'not supplied'}",
        f"- Business objective: {business_objective or 'not supplied'}",
        "",
    ]

    if not prompts:
        lines.extend(
            [
                "## Missing Input",
                "",
                "No compliant outlier pattern exists yet. Add manual/owned/public signal rows before asking for generated hooks.",
                "",
                "Minimum CSV columns: `platform`, `creator`, `hook_text`, `views`, `avg_views`, `topic`, `url`.",
                "",
            ]
        )
        return "\n".join(lines) + "\n"

    for prompt in prompts:
        lines.extend(
            [
                f"## {prompt.prompt_id}",
                "",
                f"- Source pattern: `{prompt.source_pattern_id}`",
                f"- Evidence prompt: {prompt.evidence_prompt}",
                f"- Human reaction question: {prompt.human_question}",
                f"- Next component: `{prompt.next_component}`",
                "",
                "Candidate moves to react to, rewrite, or reject:",
            ]
        )
        for move in prompt.candidate_hook_moves:
            lines.append(f"- {move}")
        lines.append("")
        lines.extend(
            [
                "Human creative reaction slot:",
                "",
                "- My actual opinion:",
                "- The story only I can tell:",
                "- What I refuse to say because it feels generic:",
                "- The angle that earns buyer-quality attention:",
                "",
            ]
        )

    return "\n".join(lines) + "\n"


def render_book_map(run_id: str, patterns: list[HookPattern], scores: list[OutlierScore]) -> str:
    lines = [
        "# Kallaway Trend Hook Radar - Book And Content Opportunity Map",
        "",
        f"Run ID: `{run_id}`",
        "",
        "## Purpose",
        "",
        "Map validated hook/outlier patterns into book chapters, content series, lead magnets, and reusable creative prompts.",
        "",
    ]

    if not patterns:
        lines.extend(
            [
                "## No Opportunity Claim Yet",
                "",
                "This run does not contain enough compliant trend evidence to recommend book or content opportunities.",
                "",
                "Next data step: supply 20-50 rows from owned analytics, manual research CSVs, or approved public-data lanes, then rerun the radar.",
                "",
            ]
        )
        return "\n".join(lines) + "\n"

    rows = []
    for pattern in patterns[:12]:
        rows.append(
            [
                pattern.pattern_id,
                pattern.desire_template,
                pattern.hook_format,
                pattern.book_opportunity,
                "Use only after human POV is added" if pattern.confidence != "high" else "Ready for one-rep test",
            ]
        )
    lines.extend(markdown_table(rows, ["Pattern", "Desire", "Format", "Book/Content Use", "Action"]))
    lines.append("")

    lines.extend(
        [
            "## Production Handoff",
            "",
            "1. Send top opportunities into `/kcs-topic-format` for topic and format fit.",
            "2. Use `/kcs-hook-triad` to build short hook, visual hook, and payoff hook.",
            "3. Use `/ai-creative-sprint` to force the human take before script drafting.",
            "4. Use `/word-grip` or `/word-opener` only after the idea has a real opinion.",
            "",
        ]
    )

    top_winners = [score for score in scores if score.winner_line_status == "above_winner_line"][:5]
    if top_winners:
        lines.extend(["## Best Source Rows To Watch Or Review", ""])
        for score in top_winners:
            lines.append(
                f"- `{score.signal_id}` - {score.creator} / {score.topic} / score {score.outlier_score:.2f}: {score.url or 'no URL supplied'}"
            )
        lines.append("")

    return "\n".join(lines) + "\n"


def render_receipt_markdown(receipt: RunReceipt) -> str:
    lines = [
        "# Kallaway Trend Hook Radar - Run Receipt",
        "",
        f"Run ID: `{receipt.run_id}`",
        f"Generated: {receipt.generated_at}",
        "",
        "## Counts",
        "",
        f"- Normalized signals: {receipt.signal_count}",
        f"- Included signals: {receipt.included_signal_count}",
        f"- Excluded signals: {receipt.excluded_signal_count}",
        f"- Source counts: {receipt.source_counts}",
        "",
        "## Outputs",
        "",
    ]
    for label, path in receipt.output_files.items():
        lines.append(f"- {label}: `{path}`")
    lines.extend(
        [
            "",
            "## Compliance Boundary",
            "",
        ]
    )
    for item in receipt.compliance_boundary:
        lines.append(f"- {item}")
    lines.extend(["", "## Next Workflow Chain", ""])
    for item in receipt.next_workflow_chain:
        lines.append(f"- `{item}`")
    lines.append("")
    return "\n".join(lines) + "\n"


def output_paths(run_dir: Path) -> dict[str, Path]:
    return {
        "normalized_signals": run_dir / "normalized-signals.json",
        "outlier_ledger": run_dir / "outlier-ledger.csv",
        "hook_pattern_report": run_dir / "hook-pattern-report.md",
        "creative_reaction_brief": run_dir / "creative-reaction-brief.md",
        "book_and_content_opportunity_map": run_dir / "book-and-content-opportunity-map.md",
        "run_receipt_json": run_dir / "run-receipt.json",
        "run_receipt_md": run_dir / "run-receipt.md",
    }


def relative(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the Kallaway Trend Hook Radar.")
    parser.add_argument("--signals-csv", action="append", default=[], help="Manual compliant CSV input.")
    parser.add_argument("--signals-json", action="append", default=[], help="Manual compliant JSON input.")
    parser.add_argument("--owned-metrics-csv", action="append", default=[], help="Owned analytics export CSV.")
    parser.add_argument("--approved-linkedin-csv", action="append", default=[], help="Approved LinkedIn evidence CSV/export.")
    parser.add_argument("--source-package", default=str(DEFAULT_SOURCE_PACKAGE), help="Video context package used as method evidence.")
    parser.add_argument("--output-root", default=str(DEFAULT_OUTPUT_ROOT), help="Root directory for dated run folders.")
    parser.add_argument("--run-id", default="", help="Stable run id. Defaults to local timestamp.")
    parser.add_argument("--topic", action="append", default=[], help="Topic to generate creative reaction prompts for.")
    parser.add_argument("--business-objective", default="", help="Business outcome the content should support.")
    parser.add_argument("--execute-apify", action="store_true", help="Run budget-guarded public-data lanes.")
    parser.add_argument("--apify-lane", action="append", choices=["youtube", "reddit", "tiktok", "instagram", "web"], default=[])
    parser.add_argument("--apify-query", action="append", default=[], help="Public-data query or handle.")
    parser.add_argument("--limit", type=int, default=10, help="Per-lane public-data result limit.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    run_id = args.run_id or datetime.now().strftime("%Y-%m-%d-%H%M%S")
    output_root = Path(args.output_root)
    if not output_root.is_absolute():
        output_root = ROOT / output_root
    run_dir = output_root / run_id
    paths = output_paths(run_dir)

    source_package = Path(args.source_package)
    if not source_package.is_absolute():
        source_package = ROOT / source_package

    input_files: list[str] = []
    signals: list[SignalItem] = []
    for path_text in args.signals_csv:
        path = Path(path_text)
        if not path.is_absolute():
            path = ROOT / path
        signals.extend(load_csv(path, "manual_csv"))
        input_files.append(relative(path))
    for path_text in args.signals_json:
        path = Path(path_text)
        if not path.is_absolute():
            path = ROOT / path
        signals.extend(load_json(path, "manual_json"))
        input_files.append(relative(path))
    for path_text in args.owned_metrics_csv:
        path = Path(path_text)
        if not path.is_absolute():
            path = ROOT / path
        signals.extend(load_csv(path, "owned_metrics"))
        input_files.append(relative(path))
    for path_text in args.approved_linkedin_csv:
        path = Path(path_text)
        if not path.is_absolute():
            path = ROOT / path
        signals.extend(load_csv(path, "approved_linkedin"))
        input_files.append(relative(path))

    lanes = args.apify_lane or ["youtube", "reddit"]
    queries = args.apify_query or args.topic or ["social media hook patterns"]
    apify_signals, apify_status = collect_apify_signals(lanes, queries, args.limit, args.execute_apify)
    signals.extend(apify_signals)

    scores = score_signals(signals)
    patterns = cluster_patterns(scores)
    prompts = creative_prompts(patterns, args.topic, args.business_objective)

    excluded = [signal for signal in signals if not signal.included]
    run_dir.mkdir(parents=True, exist_ok=True)
    write_json(paths["normalized_signals"], [asdict(signal) for signal in signals])
    write_outlier_csv(paths["outlier_ledger"], scores, excluded)
    write_markdown_with_metadata(
        paths["hook_pattern_report"],
        render_pattern_report(run_id, source_package, signals, scores, patterns),
        run_id,
        "Kallaway Trend Hook Radar - Hook Pattern Report",
    )
    write_markdown_with_metadata(
        paths["creative_reaction_brief"],
        render_creative_brief(run_id, prompts, args.topic, args.business_objective),
        run_id,
        "Kallaway Trend Hook Radar - Creative Reaction Brief",
    )
    write_markdown_with_metadata(
        paths["book_and_content_opportunity_map"],
        render_book_map(run_id, patterns, scores),
        run_id,
        "Kallaway Trend Hook Radar - Book And Content Opportunity Map",
    )

    receipt = RunReceipt(
        run_id=run_id,
        generated_at=datetime.now().isoformat(timespec="seconds"),
        source_package=relative(source_package),
        source_counts=source_counts(source_package),
        input_files=input_files,
        signal_count=len(signals),
        included_signal_count=sum(1 for signal in signals if signal.included),
        excluded_signal_count=sum(1 for signal in signals if not signal.included),
        apify_status=apify_status,
        compliance_boundary=[
            "Manual CSV, owned metrics, approved LinkedIn evidence, and explicit public-data runs only.",
            "No login automation, scraping of private LinkedIn pages, publishing, DMs, likes, comments, or outreach.",
            "Budget-guarded public lanes must return structured fallbacks when unavailable.",
        ],
        output_files={key: relative(path) for key, path in paths.items()},
        next_workflow_chain=[
            "/kallaway-trend-hook-engine",
            "/ai-topic-mining",
            "/ai-hook-extractor",
            "/kcs-topic-format",
            "/kcs-hook-triad",
            "/ai-creative-sprint",
        ],
    )
    write_json(paths["run_receipt_json"], asdict(receipt))
    write_markdown_with_metadata(
        paths["run_receipt_md"],
        render_receipt_markdown(receipt),
        run_id,
        "Kallaway Trend Hook Radar - Run Receipt",
    )

    print(
        json.dumps(
            {
                "status": "ok",
                "run_id": run_id,
                "run_dir": relative(run_dir),
                "signals": len(signals),
                "included": receipt.included_signal_count,
                "excluded": receipt.excluded_signal_count,
                "patterns": len(patterns),
                "outputs": receipt.output_files,
                "apify_status": apify_status,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
