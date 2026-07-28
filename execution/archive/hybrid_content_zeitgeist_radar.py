#!/usr/bin/env python3
"""
Hybrid Content Zeitgeist Radar.

Builds a content-side signal brief without scraping LinkedIn. LinkedIn enters
through human-approved artifacts only. Apify lanes are available behind an
explicit flag so the workflow can use paid/public sources without surprising
the operator.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any

BASE = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))

from apify_client import ACTORS, PLAN_DOLLARS, budget_state, load_env, load_usage, run_actor  # noqa: E402
from hybrid_morning_signal_radar import (  # noqa: E402
    LINKEDIN_EVIDENCE_FIELDS,
    load_linkedin_evidence,
    summarize_linkedin_evidence,
)


DEFAULT_QUERIES = [
    "AI workflow still needs human review",
    "AI content sounds generic",
    "AI automation agency client delivery",
    "prompt library not working",
    "founder using AI but still rewriting",
]

DEFAULT_TIKTOK_HASHTAGS = [
    "aitools",
    "aiautomation",
    "contentstrategy",
]

DEFAULT_INSTAGRAM_HANDLES = [
    "openai",
]

ANGLE_MAP = {
    "correction": "Oracle: polished-but-wrong output",
    "rewrite": "Catalyst: repeated correction as source material",
    "prompt": "Hot Take: prompt-library ceiling",
    "workflow": "Field Note: workflow teardown",
    "automation": "Proof: automation without legible work fails",
    "content": "Buyer Language: generic content pain",
}


def today_path(out_dir: Path) -> Path:
    return out_dir / f"hybrid-content-zeitgeist-radar-{date.today().isoformat()}.md"


def budget_summary() -> dict[str, Any]:
    usage = load_usage()
    spent = float(usage.get("spent_dollars") or 0)
    plan = float(usage.get("plan_dollars") or PLAN_DOLLARS)
    return {
        "month": usage.get("month"),
        "plan_dollars": plan,
        "spent_dollars": round(spent, 4),
        "remaining_dollars": round(plan - spent, 4),
        "state": budget_state(usage),
        "percent_used": round((spent / plan) * 100, 1) if plan else 0,
    }


def estimate_source_cost(source_plan: dict[str, int]) -> float:
    total = 0.0
    for actor, count in source_plan.items():
        total += ACTORS[actor]["cost_per_result"] * count
    return round(total, 4)


def apify_source_plan(limit: int, queries: list[str], hashtags: list[str], instagram_handles: list[str]) -> dict[str, int]:
    return {
        "reddit": len(queries) * limit,
        "youtube": len(queries) * limit,
        "tiktok": len(hashtags) * limit,
        "instagram": len(instagram_handles) * limit,
    }


def run_apify_lanes(
    *,
    queries: list[str],
    hashtags: list[str],
    instagram_handles: list[str],
    limit: int,
    enabled_lanes: set[str],
) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []

    if "reddit" in enabled_lanes:
        for query in queries:
            response = run_actor(
                "reddit",
                {
                    "startUrls": [{"url": f"https://www.reddit.com/search/?q={query.replace(' ', '+')}&type=link&sort=relevance"}],
                    "maxItems": limit,
                    "scrollTimeout": 40,
                    "skipComments": False,
                    "skipUserPosts": False,
                    "skipCommunity": False,
                },
                limit,
            )
            results.append({"lane": "reddit", "query": query, "response": response})

    if "youtube" in enabled_lanes:
        for query in queries:
            response = run_actor("youtube", {"keywords": [query], "maxItems": limit}, limit)
            results.append({"lane": "youtube", "query": query, "response": response})

    if "tiktok" in enabled_lanes:
        for hashtag in hashtags:
            response = run_actor("tiktok", {"hashtags": [hashtag], "resultsPerPage": limit}, limit)
            results.append({"lane": "tiktok", "query": hashtag, "response": response})

    if "instagram" in enabled_lanes:
        for handle in instagram_handles:
            response = run_actor(
                "instagram",
                {
                    "directUrls": [f"https://www.instagram.com/{handle.lstrip('@')}/"],
                    "resultsType": "posts",
                    "resultsLimit": limit,
                    "onlyPostsNewerThan": "365 days",
                },
                limit,
            )
            results.append({"lane": "instagram", "query": handle, "response": response})

    return results


def item_text(item: Any) -> str:
    if not isinstance(item, dict):
        return ""
    parts = []
    for key in [
        "title",
        "text",
        "body",
        "caption",
        "description",
        "shortDescription",
        "hashtags",
        "channelName",
        "author",
        "url",
    ]:
        value = item.get(key)
        if isinstance(value, list):
            parts.append(" ".join(str(part) for part in value))
        elif value:
            parts.append(str(value))
    return " ".join(parts)


def classify_angle(text: str) -> str:
    lower = text.lower()
    for keyword, angle in ANGLE_MAP.items():
        if keyword in lower:
            return angle
    return "Open Question: needs human angle selection"


def synthesize_apify_results(results: list[dict[str, Any]]) -> dict[str, Any]:
    lane_counts: Counter[str] = Counter()
    fallback_messages: list[str] = []
    angle_counts: Counter[str] = Counter()
    excerpts: list[dict[str, str]] = []

    for result in results:
        lane = result["lane"]
        response = result["response"]
        if response.get("fallback"):
            fallback_messages.append(f"{lane}: {response.get('message', 'fallback')}")
            continue
        items = response.get("items") or []
        lane_counts[lane] += len(items)
        for item in items[:5]:
            text = item_text(item)
            if not text:
                continue
            angle = classify_angle(text)
            angle_counts[angle] += 1
            excerpts.append({
                "lane": lane,
                "angle": angle,
                "excerpt": text[:240].replace("\n", " "),
            })

    return {
        "lane_counts": lane_counts.most_common(),
        "fallback_messages": fallback_messages[:8],
        "angle_counts": angle_counts.most_common(8),
        "excerpts": excerpts[:12],
    }


def read_owned_post_metrics(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=[
                "date_posted",
                "platform",
                "post_reference",
                "topic",
                "format",
                "hook",
                "impressions",
                "comments",
                "saves",
                "inbound_messages",
                "audit_requests",
                "lesson",
            ])
            writer.writeheader()
        return []

    with path.open(newline="", encoding="utf-8") as handle:
        return [dict(row) for row in csv.DictReader(handle) if any(row.values())]


def write_brief(
    path: Path,
    *,
    budget: dict[str, Any],
    dry_run: bool,
    source_plan: dict[str, int],
    estimated_cost: float,
    enabled_lanes: set[str],
    linkedin_evidence_csv: Path,
    linkedin_summary: dict[str, Any],
    owned_metrics_csv: Path,
    owned_metrics_rows: list[dict[str, str]],
    apify_summary: dict[str, Any],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Hybrid Content Zeitgeist Radar",
        "",
        f"- **Date**: {date.today().isoformat()}",
        f"- **Mode**: {'dry-run / plan only' if dry_run else 'Apify-enabled run'}",
        f"- **Budget state**: {budget['state']} (${budget['spent_dollars']} spent / ${budget['plan_dollars']} plan)",
        f"- **Estimated Apify cost if enabled**: ${estimated_cost}",
        f"- **Enabled lanes**: {', '.join(sorted(enabled_lanes)) if enabled_lanes else 'none'}",
        f"- **LinkedIn evidence rows**: {linkedin_summary['rows']}",
        f"- **Owned post metric rows**: {len(owned_metrics_rows)}",
        "",
        "## Operating Verdict",
        "",
        "Do not make LinkedIn the scraped source of truth. Make it the evidence surface Farrice controls: post URLs, screenshots, pasted comments, and owned analytics.",
        "Use Apify for adjacent social/listening lanes where the wrapper already has budget guards: Reddit, YouTube, TikTok, Instagram, Google Maps, and generic web fetches.",
        "",
        "## Source Lanes",
        "",
        f"- **Apify source plan**: {json.dumps(source_plan, sort_keys=True)}",
        "- **LinkedIn lane**: human-approved artifacts only; no login automation, profile harvesting, auto-comments, auto-likes, or DMs.",
        f"- **LinkedIn evidence CSV**: {linkedin_evidence_csv}",
        f"- **Owned metrics CSV**: {owned_metrics_csv}",
        "",
        "## Zeitgeist Signals",
        "",
    ]

    if dry_run:
        lines.extend([
            "- Dry run only: no external source calls were made.",
            "- Next active run can enable lanes with `--execute-apify --lanes reddit,youtube,tiktok` after budget review.",
            "",
        ])
    else:
        if apify_summary["lane_counts"]:
            lines.append("- **Items by lane**: " + ", ".join(
                f"{lane}: {count}" for lane, count in apify_summary["lane_counts"]
            ))
        if apify_summary["angle_counts"]:
            lines.append("- **Angle clusters**: " + ", ".join(
                f"{angle} ({count})" for angle, count in apify_summary["angle_counts"]
            ))
        if apify_summary["fallback_messages"]:
            lines.append("- **Fallbacks**: " + " | ".join(apify_summary["fallback_messages"]))
        if not any([apify_summary["lane_counts"], apify_summary["angle_counts"], apify_summary["fallback_messages"]]):
            lines.append("- No Apify items returned.")
        lines.append("")

    lines.extend([
        "## LinkedIn Evidence Synthesis",
        "",
    ])
    if linkedin_summary["status"] == "empty":
        lines.extend([
            "- No approved LinkedIn evidence rows yet.",
            "- Add 3-5 rows from manual URLs, screenshots, pasted hooks/comments, or owned analytics before expecting platform-specific confidence.",
        ])
    else:
        if linkedin_summary["top_formats"]:
            lines.append("- **Formats showing up**: " + ", ".join(
                f"{name} ({count})" for name, count in linkedin_summary["top_formats"]
            ))
        if linkedin_summary["top_archetypes"]:
            lines.append("- **Archetypes showing up**: " + ", ".join(
                f"{name} ({count})" for name, count in linkedin_summary["top_archetypes"]
            ))
        if linkedin_summary["buyer_language"]:
            lines.append("- **Buyer phrases to test**: " + " | ".join(
                f"\"{phrase}\"" for phrase in linkedin_summary["buyer_language"]
            ))
    lines.extend([
        "",
        "## Best Content Bet",
        "",
        "- **Primary angle**: The polished-but-wrong AI output is the expensive one.",
        "- **Format**: body-first LinkedIn post with a diagnostic teardown, not a broad AI opinion.",
        "- **Proof move**: show three guess-points in a sanitized/fake AI output.",
        "- **CTA**: Send one output you had to rescue and I will map where it guessed.",
        "",
        "## 30-Minute Dad-Proof Work Block",
        "",
        "1. 5 minutes: read the top signals and pick one buyer phrase.",
        "2. 10 minutes: write the body first around the pain, diagnosis, and proof move.",
        "3. 5 minutes: generate three hooks from Oracle, Catalyst, and Hot Take angles.",
        "4. 5 minutes: add one manual LinkedIn evidence row from a post/comment you saw.",
        "5. 5 minutes: choose publish, save, or rewrite; do not drift into more research.",
        "",
        "## Compliance Boundary",
        "",
        "This radar prepares research and content strategy. It does not scrape LinkedIn, log into LinkedIn, publish, DM, comment, like, or contact anyone.",
        "",
    ])
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a content-side zeitgeist radar brief.")
    parser.add_argument("--limit", type=int, default=3, help="Max results per Apify query/source.")
    parser.add_argument("--out-dir", default="deliverables", help="Output directory.")
    parser.add_argument("--execute-apify", action="store_true", help="Actually call enabled Apify source lanes.")
    parser.add_argument("--lanes", default="reddit,youtube", help="Comma-separated Apify lanes: reddit,youtube,tiktok,instagram.")
    parser.add_argument("--daily-cap", type=float, default=0.35, help="Max estimated Apify cost for this radar run.")
    parser.add_argument("--linkedin-evidence", default="deliverables/hybrid-linkedin-evidence-intake.csv")
    parser.add_argument("--owned-metrics", default="deliverables/hybrid-owned-post-metrics.csv")
    args = parser.parse_args()

    load_env()
    out_dir = BASE / args.out_dir
    linkedin_evidence_path = Path(args.linkedin_evidence)
    owned_metrics_path = Path(args.owned_metrics)
    if not linkedin_evidence_path.is_absolute():
        linkedin_evidence_path = BASE / linkedin_evidence_path
    if not owned_metrics_path.is_absolute():
        owned_metrics_path = BASE / owned_metrics_path

    requested_lanes = {lane.strip() for lane in args.lanes.split(",") if lane.strip()}
    valid_lanes = {"reddit", "youtube", "tiktok", "instagram"}
    enabled_lanes = requested_lanes & valid_lanes
    source_plan = apify_source_plan(args.limit, DEFAULT_QUERIES, DEFAULT_TIKTOK_HASHTAGS, DEFAULT_INSTAGRAM_HANDLES)
    active_plan = {lane: source_plan[lane] for lane in enabled_lanes}
    estimated_cost = estimate_source_cost(active_plan)
    budget = budget_summary()
    dry_run = not args.execute_apify

    apify_results: list[dict[str, Any]] = []
    if args.execute_apify:
        if budget["state"] == "red":
            apify_results.append({
                "lane": "budget",
                "query": "budget",
                "response": {"fallback": True, "message": "Monthly Apify budget state is red."},
            })
        elif estimated_cost > args.daily_cap:
            apify_results.append({
                "lane": "budget",
                "query": "budget",
                "response": {
                    "fallback": True,
                    "message": f"Estimated cost ${estimated_cost} exceeds daily cap ${args.daily_cap}.",
                },
            })
        else:
            apify_results = run_apify_lanes(
                queries=DEFAULT_QUERIES,
                hashtags=DEFAULT_TIKTOK_HASHTAGS,
                instagram_handles=DEFAULT_INSTAGRAM_HANDLES,
                limit=args.limit,
                enabled_lanes=enabled_lanes,
            )

    linkedin_rows = load_linkedin_evidence(linkedin_evidence_path)
    linkedin_summary = summarize_linkedin_evidence(linkedin_rows)
    owned_metrics_rows = read_owned_post_metrics(owned_metrics_path)
    apify_summary = synthesize_apify_results(apify_results)
    output_path = today_path(out_dir)

    write_brief(
        output_path,
        budget=budget,
        dry_run=dry_run,
        source_plan=active_plan,
        estimated_cost=estimated_cost,
        enabled_lanes=enabled_lanes if args.execute_apify else set(),
        linkedin_evidence_csv=linkedin_evidence_path,
        linkedin_summary=linkedin_summary,
        owned_metrics_csv=owned_metrics_path,
        owned_metrics_rows=owned_metrics_rows,
        apify_summary=apify_summary,
    )

    print(json.dumps({
        "status": "ok",
        "mode": "dry_run" if dry_run else "apify_enabled",
        "brief": str(output_path),
        "estimated_apify_cost": estimated_cost,
        "budget": budget,
        "enabled_lanes": sorted(enabled_lanes) if args.execute_apify else [],
        "linkedin_evidence_csv": str(linkedin_evidence_path),
        "linkedin_evidence_rows": linkedin_summary["rows"],
        "owned_metrics_csv": str(owned_metrics_path),
        "owned_metrics_rows": len(owned_metrics_rows),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
