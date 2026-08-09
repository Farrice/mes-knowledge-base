#!/usr/bin/env python3
"""
signal_scout.py — Niche-resonance listening on LinkedIn (LISTENING-ONLY).

Cody Schneider doctrine (extraction 2026-08-06): engagement is a hand-raise —
who engages with what in your niche is the highest-signal targeting AND content
intelligence available. This tool does the LISTENING half only. It never
contacts anyone; it produces intelligence files for the Angle Brief and the
human operator. (Farrice decision 2026-08-06: outbound/DM drafting is parked;
reputation and distribution stay human.)

Pipeline (deterministic, no LLM):
  creators file → recent posts per creator (apimaestro/linkedin-profile-posts)
  → reactions + comments per post (apimaestro post-reactions / post-comments)
  → (1) RESONANCE REPORT: which topics/hooks pulled hand-raises, reaction mix,
        top comment language (ICP verbatim)
  → (2) ENGAGER ROSTER: deduped, scored (comment=3, reaction=1, +2 ICP-title match)

Outputs:
  _active/linkedin/05-lead-gen/engager-rosters/ROSTER-YYYY-MM-DD.md (+.json)
  .agent/health/signal-scout-YYYY-MM-DD.json (receipt)

Usage:
  python3 execution/signal_scout.py --creators-file _active/linkedin/05-lead-gen/listening-creators.md
  python3 execution/signal_scout.py --posts "<post_url1>,<post_url2>"
  python3 execution/signal_scout.py --creators justinwelsh,gisenberg --posts-per-creator 2

Budgets: every actor call goes through apify_client.run_actor (monthly $29 guard,
$5/run cap, never raises). Default scope (≤10 creators × 3 posts) ≈ well under $2/run.
"""

import argparse
import json
import os
import re
import sys
from datetime import date, datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "execution"))

from degrade import degraded  # noqa: E402

# Load .env so headless (launchd) runs have APIFY_TOKEN without shell profile help.
try:
    from dotenv import load_dotenv
    load_dotenv(REPO / ".env")
except ImportError as e:
    degraded(None, "python-dotenv not importable — .env skipped; headless runs may lack APIFY_TOKEN", e)

import apify_client as ac  # noqa: E402  (needs sys.path + dotenv first)

DEFAULT_CREATORS_FILE = REPO / "_active/linkedin/05-lead-gen/listening-creators.md"
DEFAULT_OUT_DIR = REPO / "_active/linkedin/05-lead-gen/engager-rosters"
HEALTH_DIR = REPO / ".agent/health"

# Campaign ICP (Proof-to-Market: funded supplement/performance brand deciders)
# + adjacent buyers. Override with --icp-titles.
DEFAULT_ICP_TITLES = (
    r"founder|co-?founder|ceo|cmo|owner|head of brand|head of marketing"
    r"|vp[ ,.]*(of )?(brand|marketing|growth)|director[ ,.]*(of )?(brand|marketing|growth)"
)

MAX_ACTOR_CALLS = 80  # hard sanity rail per run, independent of $ budgets

# Actor calls that did not come back "ok" this run. A roster written over these
# would state "0 engagers" as a business fact (mirror: social_intel.py refuses
# Notion writes on a failed scrape). main() refuses the roster write when set.
SCRAPE_FAILURES: list[str] = []


def _scrape_failed(what: str, r: dict) -> None:
    msg = f"{what} — status: {r.get('status')}. {r.get('message', '')}".strip()
    print(msg)
    SCRAPE_FAILURES.append(msg)


def read_creators(path: Path) -> list[str]:
    """Creators file: one handle/URL per line; '#' comments and blanks ignored."""
    creators = []
    for line in path.read_text().splitlines():
        line = line.split("#", 1)[0].strip().lstrip("-").strip()
        if not line or line.startswith("---") or line.lower().startswith(("status:", "purpose:")):
            continue
        if "linkedin.com" in line:
            m = re.search(r"/in/([^/\s)\]]+)", line)
            line = m.group(1) if m else line
        creators.append(line)
    return creators


def first_line(text: str, width: int = 110) -> str:
    line = (text or "").strip().splitlines()[0] if (text or "").strip() else "(no text)"
    return (line[: width - 1] + "…") if len(line) > width else line


class CallCounter:
    def __init__(self, limit: int):
        self.n = 0
        self.limit = limit

    def spend(self) -> bool:
        self.n += 1
        return self.n <= self.limit


def fetch_posts(creator: str, n_posts: int, counter: CallCounter) -> list[dict]:
    if not counter.spend():
        return []
    r = ac.run_actor("linkedin-posts", {"username": creator, "limit": n_posts}, n_posts)
    if r.get("status") != "ok":
        _scrape_failed(f"posts scrape failed for {creator}", r)
        return []
    return r.get("items", [])


def fetch_engagement(post_url: str, limit: int, counter: CallCounter) -> tuple[list, list]:
    reactions, comments = [], []
    if counter.spend():
        r = ac.run_actor(
            "linkedin-post-reactions",
            {"post_urls": [post_url], "page_number": 1, "reaction_type": "ALL",
             "limit": max(1, min(limit, 100))},
            limit,
        )
        if r.get("status") == "ok":
            reactions = r.get("items", [])
        else:
            _scrape_failed(f"reactions scrape failed for {post_url}", r)
    if counter.spend():
        r = ac.run_actor(
            "linkedin-post-comments",
            {"postIds": [post_url], "page_number": 1, "sortOrder": "most recent",
             "limit": max(1, min(limit, 100))},
            limit,
        )
        if r.get("status") == "ok":
            comments = r.get("items", [])
        else:
            _scrape_failed(f"comments scrape failed for {post_url}", r)
    return reactions, comments


def main():
    p = argparse.ArgumentParser(description="LinkedIn niche-resonance listening (never contacts anyone)")
    p.add_argument("--creators-file", type=Path, default=DEFAULT_CREATORS_FILE)
    p.add_argument("--creators", help="Comma-separated handles/URLs (overrides file)")
    p.add_argument("--posts", help="Comma-separated post URLs (skip creator discovery)")
    p.add_argument("--posts-per-creator", type=int, default=3)
    p.add_argument("--engagers-per-post", type=int, default=100, help="Reactions+comments page size (≤100)")
    p.add_argument("--icp-titles", default=DEFAULT_ICP_TITLES, help="Regex scored +2 on headline match")
    p.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    p.add_argument("--tag", default="", help="Optional label suffix for output files")
    args = p.parse_args()

    icp_re = re.compile(args.icp_titles, re.IGNORECASE)
    counter = CallCounter(MAX_ACTOR_CALLS)
    started = datetime.now().isoformat(timespec="seconds")
    budget_before = ac.load_usage().get("spent_dollars")

    # -- Gather posts ------------------------------------------------------
    posts: list[dict] = []  # {creator, url, text, stats}
    if args.posts:
        posts = [{"creator": "(direct)", "url": u.strip(), "text": "", "stats": {}}
                 for u in args.posts.split(",") if u.strip()]
    else:
        if args.creators:
            creators = [c.strip() for c in args.creators.split(",") if c.strip()]
        else:
            if not args.creators_file.exists():
                sys.exit(f"Creators file not found: {args.creators_file}")
            creators = read_creators(args.creators_file)
        for creator in creators:
            for it in fetch_posts(creator, args.posts_per_creator, counter):
                url = it.get("url") or it.get("post_url") or ""
                if url:
                    posts.append({"creator": creator, "url": url,
                                  "text": it.get("text", ""), "stats": it.get("stats", {})})

    # -- Engagement per post ----------------------------------------------
    roster: dict[str, dict] = {}  # profile_url -> lead
    resonance: list[dict] = []
    for post in posts:
        reactions, comments = fetch_engagement(post["url"], args.engagers_per_post, counter)

        top_comments = sorted(
            comments,
            key=lambda c: (c.get("stats", {}) or {}).get("total_reactions", 0),
            reverse=True,
        )[:5]
        resonance.append({
            "creator": post["creator"],
            "url": post["url"],
            "hook": first_line(post["text"]),
            "stats": post["stats"],
            "sampled_reactions": len(reactions),
            "sampled_comments": len(comments),
            "top_comment_language": [
                {"text": (c.get("text") or "")[:300],
                 "author_headline": (c.get("author", {}) or {}).get("headline", "")}
                for c in top_comments
            ],
        })

        for rx in reactions:
            actor = rx.get("reactor", {}) or {}
            key = actor.get("profile_url") or actor.get("urn") or ""
            if not key:
                continue
            lead = roster.setdefault(key, {
                "name": actor.get("name", ""), "headline": actor.get("headline", ""),
                "profile_url": key, "score": 0, "evidence": []})
            lead["score"] += 1
            lead["evidence"].append(f"reacted:{post['url'][-40:]}")
        for c in comments:
            author = c.get("author", {}) or {}
            key = author.get("profile_url") or author.get("urn") or author.get("name", "")
            if not key:
                continue
            lead = roster.setdefault(key, {
                "name": author.get("name", ""), "headline": author.get("headline", ""),
                "profile_url": key if key.startswith("http") else "", "score": 0, "evidence": []})
            lead["score"] += 3
            lead["evidence"].append(f"commented:{(c.get('text') or '')[:60]}")

    for lead in roster.values():
        if icp_re.search(lead.get("headline") or ""):
            lead["score"] += 2
            lead["icp_match"] = True

    ranked = sorted(roster.values(), key=lambda x: x["score"], reverse=True)
    resonance.sort(
        key=lambda r: (r["stats"] or {}).get("total_reactions", r["sampled_reactions"]),
        reverse=True,
    )

    stamp = date.today().isoformat() + (f"-{args.tag}" if args.tag else "")

    # -- Refuse the roster write on a failed scrape ------------------------
    # (Mirrors social_intel.py: no partial writes on a failed/budget-exhausted
    # scrape.) A ROSTER-*.md written over failed calls would state "0 engagers"
    # as a business conclusion when the truth is "the scrape didn't run".
    if SCRAPE_FAILURES:
        print(f"{len(SCRAPE_FAILURES)} scrape call(s) failed — roster NOT written "
              "(no false '0 engagers' conclusion). Fix the scrape and re-run.")
        budget_after = ac.load_usage().get("spent_dollars")
        HEALTH_DIR.mkdir(parents=True, exist_ok=True)
        receipt = {
            "run": started, "status": "scrape-failed",
            "failures": SCRAPE_FAILURES,
            "posts": len(posts), "engagers": 0,
            "actor_calls": counter.n, "call_cap": MAX_ACTOR_CALLS,
            "budget_spent_before": budget_before,
            "budget_spent_after": budget_after,
            "outputs": [],
            "contacted_anyone": False,
        }
        (HEALTH_DIR / f"signal-scout-{stamp}.json").write_text(json.dumps(receipt, indent=2))
        print(json.dumps(receipt, indent=2))
        return  # exit 0 — a failed scrape is surfaced, never a crashed run

    # -- Write outputs -----------------------------------------------------
    args.out_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.out_dir / f"ROSTER-{stamp}.json"
    md_path = args.out_dir / f"ROSTER-{stamp}.md"

    json_path.write_text(json.dumps(
        {"generated": started, "posts_analyzed": len(posts),
         "resonance": resonance, "roster": ranked}, indent=2))

    lines = [
        f"# Signal Scout — {stamp}",
        "",
        "> LISTENING-ONLY intelligence. No one on this list has been contacted by any system.",
        f"> {len(posts)} posts · {len(ranked)} unique engagers · scoring: comment=3, reaction=1, ICP-title +2.",
        "",
        "## Resonance — what pulled hand-raises",
        "",
        "| # | Creator | Hook (first line) | Reactions | Comments | Sampled |",
        "|---|---------|-------------------|-----------|----------|---------|",
    ]
    for i, r in enumerate(resonance, 1):
        s = r["stats"] or {}
        lines.append(
            f"| {i} | {r['creator']} | {r['hook']} | {s.get('total_reactions', '—')} "
            f"| {s.get('comments', '—')} | {r['sampled_reactions']}r/{r['sampled_comments']}c |")
    lines += ["", "### ICP verbatim (top comment language per post)", ""]
    for r in resonance:
        if not r["top_comment_language"]:
            continue
        lines.append(f"**{r['hook']}**")
        for c in r["top_comment_language"][:3]:
            head = f" — *{c['author_headline'][:60]}*" if c["author_headline"] else ""
            lines.append(f"- \"{c['text'][:200]}\"{head}")
        lines.append("")
    lines += [
        "## Engager roster (top 50)",
        "",
        "| Score | Name | Headline | ICP | Profile |",
        "|-------|------|----------|-----|---------|",
    ]
    for lead in ranked[:50]:
        icp = "✓" if lead.get("icp_match") else ""
        lines.append(
            f"| {lead['score']} | {lead['name']} | {(lead['headline'] or '')[:80]} "
            f"| {icp} | {lead['profile_url']} |")
    md_path.write_text("\n".join(lines) + "\n")

    # -- Receipt -----------------------------------------------------------
    budget_after = ac.load_usage().get("spent_dollars")
    HEALTH_DIR.mkdir(parents=True, exist_ok=True)
    receipt = {
        "run": started, "posts": len(posts), "engagers": len(ranked),
        "actor_calls": counter.n, "call_cap": MAX_ACTOR_CALLS,
        "budget_spent_before": budget_before,
        "budget_spent_after": budget_after,
        "outputs": [str(md_path), str(json_path)],
        "contacted_anyone": False,
    }
    (HEALTH_DIR / f"signal-scout-{stamp}.json").write_text(json.dumps(receipt, indent=2))

    print(json.dumps({"status": "ok", **receipt}, indent=2))


if __name__ == "__main__":
    main()
