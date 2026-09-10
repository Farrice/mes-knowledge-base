#!/usr/bin/env python3
"""Local, deterministic runtime for the LinkedIn zero-to-scale operating system."""

from __future__ import annotations

import argparse
import csv
import json
import statistics
import sys
from datetime import date
from pathlib import Path


IDEA_FIELDS = [
    "idea_id", "topic", "north_star", "bucket", "source", "attention_potential",
    "time_to_create", "smart_score", "surprising_or_actionable", "status",
]
POST_FIELDS = [
    "post_id", "published_at", "topic", "north_star", "bucket", "format", "hook_family",
    "sequence_id", "impressions", "saves", "reposts", "comments", "profile_views",
    "followers_gained", "dms", "leads", "revenue", "notes",
]
REQUIRED_CONFIG = ["account_name", "offer", "icp", "outcome", "mechanism", "posting_capacity"]


def write_csv(path: Path, fields: list[str], rows: list[dict[str, object]] | None = None) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows or [])


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def number(value: str | int | float | None) -> float:
    try:
        return float(value or 0)
    except (TypeError, ValueError):
        return 0.0


def init_workspace(args: argparse.Namespace) -> int:
    root = Path(args.output).resolve()
    root.mkdir(parents=True, exist_ok=True)
    config = {
        "account_name": args.name,
        "offer": args.offer,
        "icp": args.icp,
        "outcome": args.outcome,
        "mechanism": args.mechanism,
        "posting_capacity": args.cadence,
        "target": "source-inspired growth ambition; not a guaranteed follower outcome",
        "created": date.today().isoformat(),
    }
    (root / "config.json").write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
    write_csv(root / "ideas.csv", IDEA_FIELDS)
    write_csv(root / "posts.csv", POST_FIELDS)
    (root / "profile.md").write_text(
        "# Profile conversion brief\n\n"
        "## Headline\n\n[What you do] + [who you help] + [specific outcome]\n\n"
        "## About\n\n### Before state\n[Observed buyer pain]\n\n### Epiphany\n[Mechanism learned]\n\n"
        "### After state\n[Proof-bounded result]\n\n### Service bridge\n[One next action]\n\n"
        "## Featured section\n\n1. [Owned resource]\n2. [Proof asset]\n3. [Offer path]\n",
        encoding="utf-8",
    )
    (root / "operating-rhythm.md").write_text(
        "# Operating rhythm\n\n"
        "## Every two weeks\n\n- Add 20 ideas.\n- Score attention potential and time to create from 1-5.\n"
        "- Reject ideas below 6 unless strategic judgment overrides the score with a note.\n\n"
        "## Every post\n\n- Draft the body before the hook.\n- Create three hook options.\n"
        "- Use one dopamine-density device only when the source or proof supports it.\n"
        "- Record the result in posts.csv after publishing.\n\n"
        "## Every 10 posts\n\n- Run review.\n- Inspect the top posts by follower efficiency and depth rate.\n"
        "- Change one variable for the next block; preserve the rest.\n\n"
        "## Every 100 posts\n\n- Keep the top 10 patterns.\n- Retire weak topic-hook-format combinations.\n"
        "- Start the next 100-post learning cycle.\n",
        encoding="utf-8",
    )
    print(f"LinkedIn growth workspace initialized: {root}")
    return 0


def rank_ideas(args: argparse.Namespace) -> int:
    source = Path(args.input)
    rows = read_csv(source)
    failures: list[str] = []
    for index, row in enumerate(rows, start=2):
        attention = number(row.get("attention_potential"))
        effort = number(row.get("time_to_create"))
        if attention not in {1, 2, 3, 4, 5} or effort not in {1, 2, 3, 4, 5}:
            failures.append(f"row {index}: attention_potential and time_to_create must be integers 1-5")
            continue
        row["smart_score"] = str(int(attention + effort))
    if failures:
        print("Idea ranking failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 2
    rows.sort(key=lambda row: (-number(row.get("smart_score")), row.get("idea_id", "")))
    output = Path(args.output or source)
    write_csv(output, IDEA_FIELDS, rows)
    print(f"Ranked {len(rows)} ideas: {output}")
    return 0


def review_posts(args: argparse.Namespace) -> int:
    rows = read_csv(Path(args.input))
    if not rows:
        print("Review failed: posts ledger has no rows", file=sys.stderr)
        return 2
    scored: list[dict[str, object]] = []
    for row in rows:
        impressions = number(row.get("impressions"))
        scored.append({
            **row,
            "follower_efficiency": number(row.get("followers_gained")) * 1000 / impressions if impressions else 0,
            "depth_rate": (number(row.get("saves")) + number(row.get("reposts")) + number(row.get("comments"))) / impressions if impressions else 0,
        })
    top_follow = sorted(scored, key=lambda row: float(row["follower_efficiency"]), reverse=True)[:10]
    top_depth = sorted(scored, key=lambda row: float(row["depth_rate"]), reverse=True)[:10]
    followers = sum(number(row.get("followers_gained")) for row in scored)
    leads = sum(number(row.get("leads")) for row in scored)
    revenue = sum(number(row.get("revenue")) for row in scored)
    lines = [
        "# LinkedIn learning review", "", f"Posts reviewed: {len(scored)}",
        f"Followers gained: {followers:g}", f"Leads: {leads:g}", f"Attributed revenue: {revenue:g}",
        f"Median impressions: {statistics.median(number(row.get('impressions')) for row in scored):g}", "",
        "## Top follower-efficiency posts", "",
        "| Post | Topic | Bucket | Followers / 1K impressions |", "|---|---|---|---:|",
    ]
    for row in top_follow:
        lines.append(f"| {row.get('post_id','')} | {row.get('topic','')} | {row.get('bucket','')} | {float(row['follower_efficiency']):.2f} |")
    lines += ["", "## Top depth-rate posts", "", "| Post | Topic | Hook | Depth rate |", "|---|---|---|---:|"]
    for row in top_depth:
        lines.append(f"| {row.get('post_id','')} | {row.get('topic','')} | {row.get('hook_family','')} | {float(row['depth_rate']):.2%} |")
    lines += [
        "", "## Decision rule", "",
        "Repeat the topic-hook-format patterns shared by the top group. Change one weak variable in the next block; do not copy the post verbatim.",
        "", "## Proof state", "",
        "This report measures recorded events only. It does not prove causality or guarantee future follower growth.",
    ]
    output = Path(args.output)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Reviewed {len(scored)} posts: {output}")
    return 0


def doctor(args: argparse.Namespace) -> int:
    root = Path(args.workspace)
    failures: list[str] = []
    for name in ("config.json", "ideas.csv", "posts.csv", "profile.md", "operating-rhythm.md"):
        if not (root / name).is_file():
            failures.append(f"missing {name}")
    if (root / "config.json").is_file():
        try:
            config = json.loads((root / "config.json").read_text(encoding="utf-8"))
            failures.extend(f"config missing {field}" for field in REQUIRED_CONFIG if not config.get(field))
        except json.JSONDecodeError as exc:
            failures.append(f"invalid config.json: {exc}")
    for filename, fields in (("ideas.csv", IDEA_FIELDS), ("posts.csv", POST_FIELDS)):
        path = root / filename
        if path.is_file():
            with path.open(encoding="utf-8", newline="") as handle:
                actual = next(csv.reader(handle), [])
            missing = [field for field in fields if field not in actual]
            if missing:
                failures.append(f"{filename} missing columns: {', '.join(missing)}")
    if failures:
        print("LinkedIn growth workspace: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("LinkedIn growth workspace: PASS")
    return 0


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    sub = root.add_subparsers(dest="command", required=True)
    init = sub.add_parser("init", help="Create a client/account operating workspace")
    init.add_argument("--name", required=True)
    init.add_argument("--offer", required=True)
    init.add_argument("--icp", required=True)
    init.add_argument("--outcome", required=True)
    init.add_argument("--mechanism", required=True)
    init.add_argument("--cadence", type=int, choices=(3, 5, 7), default=5)
    init.add_argument("--output", required=True)
    init.set_defaults(func=init_workspace)
    rank = sub.add_parser("rank-ideas", help="Apply the 1-5 + 1-5 Smart Post queue")
    rank.add_argument("--input", required=True)
    rank.add_argument("--output")
    rank.set_defaults(func=rank_ideas)
    review = sub.add_parser("review", help="Analyze a post block or Rule-of-100 ledger")
    review.add_argument("--input", required=True)
    review.add_argument("--output", required=True)
    review.set_defaults(func=review_posts)
    check = sub.add_parser("doctor", help="Validate a workspace and its schema")
    check.add_argument("--workspace", required=True)
    check.set_defaults(func=doctor)
    return root


def main() -> int:
    args = parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
