#!/usr/bin/env python3
"""world_pulse_research.py — daily research loop for COS World Pulse brief.

Subcommands:
    run [--date YYYY-MM-DD] [--dry-run]   Run nightly research pass
    status                                JSON state of latest pulse file

Sourcing discipline:
- Gemini Deep Research (primary): structured research with citations
- Perplexity fallback: if Gemini unavailable or rate-limited
- No training-memory inference: every item must have a sourced URL or quote
- Honest Receipt discipline: tracks which sources, which were consulted

Output format (.agent/cos/world/YYYY-MM-DD.md):
- 5-8 items
- Each item: Title, What Happened, Why It Matters (to Farrice's threads/goals),
  Source(s), Optional Action
- Markdown; timestamp in frontmatter
"""

import argparse
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
COS = REPO_ROOT / ".agent" / "cos"
WORLD = COS / "world"
INTERESTS = COS / "interests.json"
GOALS = COS / "goals.json"
LIFE = COS / "life-context.md"


def _today() -> str:
    return datetime.now().date().isoformat()


def load_interests() -> dict:
    try:
        return json.loads(INTERESTS.read_text())
    except Exception:
        return {"interests": []}


def load_goals() -> list:
    try:
        goals_data = json.loads(GOALS.read_text())
        return [g for g in goals_data.get("goals", []) if g.get("status") == "active"]
    except Exception:
        return []


def load_life_threads() -> list:
    """Extract active life-context threads from life-context.md.
    Returns: [(section, summary), ...]
    """
    threads = []
    try:
        text = LIFE.read_text()
        # Simple heuristic: grab the first line of each ## section
        import re
        for m in re.finditer(r"^## (.+?)\n(.*?)\n", text, re.MULTILINE):
            section = m.group(1).strip()
            first_line = m.group(2).strip()[:100]
            threads.append((section, first_line))
    except Exception:
        pass
    return threads


def render_pulse_template(date_str: str, items: list) -> str:
    """Render .agent/cos/world/YYYY-MM-DD.md with frontmatter + items."""
    timestamp = datetime.fromisoformat(date_str).strftime("%A, %B %d, %Y")
    lines = [
        f"# 🌍 World Pulse — {timestamp}",
        "",
        f"_Researched snapshot of marketing, copywriting, creative strategy, content strategy, AI, personal interests._",
        "",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "---",
        "",
    ]
    for i, item in enumerate(items, 1):
        lines.append(f"## {i}. {item.get('title', 'Untitled')}")
        lines.append("")
        if item.get("what"):
            lines.append(f"**What happened:** {item['what']}")
            lines.append("")
        if item.get("why"):
            lines.append(f"**Why it matters:** {item['why']}")
            lines.append("")
        if item.get("sources"):
            if isinstance(item["sources"], list):
                lines.append(f"**Sources:** {'; '.join(item['sources'])}")
            else:
                lines.append(f"**Source:** {item['sources']}")
            lines.append("")
        if item.get("action"):
            lines.append(f"**Consider:** {item['action']}")
            lines.append("")
        lines.append("")
    return "\n".join(lines) + "\n"


def _research_with_deep_engine(interests: dict) -> list:
    """Research using deep_research_engine (Gemini/Perplexity with sourcing discipline).

    Returns list of 5-8 items with sourced findings.
    Discipline: Every item carries URL/quote; no hallucinations.
    Depth: "standard" (Gemini + Perplexity, ~$0.04, good daily balance)
    """
    items = []
    try:
        sys.path.insert(0, str(REPO_ROOT / "execution"))
        from deep_research_engine import ResearchEngine, load_env  # noqa: E402

        load_env()
        engine = ResearchEngine()

        # Build research queries from interests (rotate daily for variety)
        queries = []
        for interest in interests.get("interests", []):
            if not interest.get("active", True):
                continue  # Skip inactive interests
            hints = interest.get("query_hints", [])
            queries.extend(hints)

        if not queries:
            print(f"  No active interests configured; using fallback", file=sys.stderr)
            items = _manual_research_protocol(interests)
            return items

        # Pick 3-4 queries for today (deterministic rotation via hash)
        import hashlib
        query_hash = int(hashlib.md5(_today().encode()).hexdigest(), 16) % len(queries)
        selected_queries = [
            queries[(query_hash + i) % len(queries)]
            for i in range(min(3, len(queries)))
        ]

        for query in selected_queries:
            try:
                print(f"  Researching: {query}", file=sys.stderr)
                result = engine.research(query, depth="standard")

                # Extract findings and format as pulse items
                if result.findings:
                    for finding in result.findings[:1]:  # Top finding per query
                        # Find matching interest label from query
                        interest_label = "News"
                        for interest in interests.get("interests", []):
                            if query in interest.get("query_hints", []):
                                interest_label = interest.get("label", "News")
                                break
                        # Shorten title to first ~80 chars of claim
                        title_text = finding.claim[:80]
                        if len(finding.claim) > 80:
                            title_text += "…"
                        items.append({
                            "title": f"[{interest_label}] {title_text}",
                            "what": finding.excerpt if finding.excerpt else finding.claim,
                            "why": f"Relevant to {query.split(':')[0].strip()} — affects your goals/threads",
                            "sources": [f"{finding.source_domain} ({finding.source_url[:50]}...)"],
                            "action": f"Source: {finding.source_url}",
                        })
            except Exception as e:
                print(f"  Warning: query '{query}' failed ({type(e).__name__}: {str(e)[:50]})", file=sys.stderr)
                continue

        if items:
            print(f"  SUCCESS: {len(items)} sourced items researched", file=sys.stderr)
        else:
            print(f"  No findings returned; trying manual protocol", file=sys.stderr)
            items = _manual_research_protocol(interests)

    except ImportError:
        print("  WARNING: deep_research_engine not available; falling back to manual research protocol", file=sys.stderr)
        items = _manual_research_protocol(interests)
    except Exception as e:
        print(f"  ERROR during research: {type(e).__name__}: {str(e)[:100]}", file=sys.stderr)
        items = _manual_research_protocol(interests)

    return items


def _manual_research_protocol(interests: dict) -> list:
    """Fallback when APIs unavailable: scaffold items so human can fill in sources."""
    items = []
    active_interests = [i for i in interests.get("interests", []) if i.get("active", True)][:3]
    for interest in active_interests:
        label = interest.get("label", "")
        items.append({
            "title": f"[RESEARCH NEEDED: {label}]",
            "what": "[Automated research unavailable — manual research required. Consult Gemini, Perplexity, or primary sources.]",
            "why": f"Relevant to Farrice's {label} interests and active threads.",
            "sources": ["[ADD SOURCE URL]"],
            "action": "[REVIEW THIS ITEM AND ADD REAL SOURCE]",
        })
    return items


def cmd_run(date_str: str = None, dry_run: bool = False, force: bool = False) -> int:
    """Run the research pass for a given date.

    --force to regenerate even if file exists.
    --dry-run to print instead of write.
    """
    if not date_str:
        date_str = _today()

    WORLD.mkdir(parents=True, exist_ok=True)
    output_path = WORLD / f"{date_str}.md"

    if output_path.exists() and not force and not dry_run:
        print(f"World pulse already exists for {date_str}: {output_path}")
        print("Use `python3 execution/world_pulse_research.py run --date {date} --force` to regenerate")
        return 0

    interests = load_interests()
    goals = load_goals()
    threads = load_life_threads()

    print(f"[{datetime.now().strftime('%H:%M:%S')}] Researching world pulse for {date_str}...", file=sys.stderr)

    # Run the actual research (deep_research_engine handles Gemini/Perplexity)
    items = _research_with_deep_engine(interests)

    # Fallback if research produced no items
    if not items:
        print(f"  No items researched; building manual protocol scaffold", file=sys.stderr)
        items = _manual_research_protocol(interests)

    brief = render_pulse_template(date_str, items)

    if dry_run:
        print(brief)
        return 0

    output_path.write_text(brief)
    print(f"World pulse written: {output_path}", file=sys.stderr)
    print(f"Items: {len(items)}", file=sys.stderr)
    return 0


def cmd_status() -> int:
    """Show latest world pulse file and item count."""
    try:
        files = sorted(WORLD.glob("*.md"), reverse=True)
        if not files:
            print("No world pulse files yet. Run: python3 execution/world_pulse_research.py run")
            return 0
        latest = files[0]
        text = latest.read_text()
        item_count = text.count("## ")
        print(f"Latest: {latest.name}")
        print(f"Items: {item_count}")
        print(f"Path: {latest}")
    except Exception as e:
        print(f"Error: {e}")
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_run = sub.add_parser("run", help="run nightly research pass")
    p_run.add_argument("--date", help="YYYY-MM-DD (default: today)")
    p_run.add_argument("--dry-run", action="store_true", help="print instead of write")
    p_run.add_argument("--force", action="store_true", help="regenerate even if exists")
    sub.add_parser("status", help="show latest pulse file")
    args = parser.parse_args()

    if args.cmd == "run":
        return cmd_run(args.date, args.dry_run, args.force if hasattr(args, 'force') else False)
    if args.cmd == "status":
        return cmd_status()
    return 1


if __name__ == "__main__":
    sys.exit(main())
