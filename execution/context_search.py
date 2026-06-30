#!/usr/bin/env python3
"""
context_search.py — Search across the conversation index for artifacts,
topics, experts, and context from past sessions.

Usage:
    python execution/context_search.py "keyword"
    python execution/context_search.py "keyword" --domain LinkedIn
    python execution/context_search.py --expert "Nicolas Cole"
    python execution/context_search.py --type implementation_plan
    python execution/context_search.py --recent 5
    python execution/context_search.py --since 2026-03-25
    python execution/context_search.py --all-domains
    python execution/context_search.py --all-experts
"""

import argparse
import json
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BRAIN_DIR = Path.home() / ".gemini" / "antigravity" / "brain"
INDEX_JSON = BRAIN_DIR / "_index" / "conversations.json"
ROOT = Path(__file__).resolve().parent.parent
ORG_MANIFEST = ROOT / "_system" / "organization" / "manifest.json"

# ---------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------

def load_index() -> list:
    """Load the conversation index."""
    if not INDEX_JSON.exists():
        print("❌ No index found. Run: python execution/conversation_index.py build")
        sys.exit(1)
    return json.loads(INDEX_JSON.read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# Search functions
# ---------------------------------------------------------------------------

def search_keyword(conversations: list, query: str) -> list:
    """Search conversations by keyword across all text fields."""
    query_lower = query.lower()
    scored = []
    
    for conv in conversations:
        score = 0
        
        # Title match (highest weight)
        if query_lower in conv.get("title", "").lower():
            score += 10
        
        # Domain match
        for domain in conv.get("domains", []):
            if query_lower in domain.lower():
                score += 5
        
        # Expert match
        for expert in conv.get("experts", []):
            if query_lower in expert.lower():
                score += 5
        
        # Topic match
        for topic in conv.get("topics", []):
            if query_lower in topic.lower():
                score += 3
        
        # Artifact name/summary match
        for artifact in conv.get("artifacts", []):
            if query_lower in artifact.get("name", "").lower():
                score += 4
            if query_lower in artifact.get("summary", "").lower():
                score += 2
        
        if score > 0:
            scored.append((score, conv))
    
    # Sort by score descending
    scored.sort(key=lambda x: -x[0])
    return [conv for _, conv in scored]


def search_organization_manifest(query: str, max_results: int = 5) -> list[dict]:
    """Search the artifact organization manifest when available."""

    if not query or not ORG_MANIFEST.exists():
        return []
    try:
        manifest = json.loads(ORG_MANIFEST.read_text(encoding="utf-8"))
    except Exception:
        return []

    terms = [term for term in query.lower().split() if len(term) > 2]
    matches = []
    for entry in manifest.get("entries", []):
        haystack = " ".join(
            str(entry.get(field, ""))
            for field in (
                "path",
                "relative_path",
                "root",
                "domain",
                "project",
                "artifact_type",
                "lifecycle",
                "status",
            )
        ).lower()
        score = sum(1 for term in terms if term in haystack)
        if score:
            matches.append((score, entry))

    matches.sort(key=lambda item: (-item[0], str(item[1].get("relative_path") or item[1].get("path") or "")))
    return [entry for _, entry in matches[:max_results]]


def filter_domain(conversations: list, domain: str) -> list:
    """Filter conversations by domain."""
    domain_lower = domain.lower()
    return [c for c in conversations if any(domain_lower in d.lower() for d in c.get("domains", []))]


def filter_expert(conversations: list, expert: str) -> list:
    """Filter conversations by expert name."""
    expert_lower = expert.lower()
    return [c for c in conversations if any(expert_lower in e.lower() for e in c.get("experts", []))]


def filter_type(conversations: list, artifact_type: str) -> list:
    """Filter conversations by artifact type."""
    type_lower = artifact_type.lower()
    return [c for c in conversations if any(type_lower in a.get("name", "").lower() for a in c.get("artifacts", []))]


def filter_since(conversations: list, since_date: str) -> list:
    """Filter conversations since a given date."""
    return [c for c in conversations if c.get("date", "") >= since_date]


def get_recent(conversations: list, n: int) -> list:
    """Get the N most recent conversations."""
    return conversations[:n]


# ---------------------------------------------------------------------------
# Display
# ---------------------------------------------------------------------------

def display_results(results: list, max_results: int = 20):
    """Display search results in a readable format."""
    if not results:
        print("🔍 No results found.")
        return
    
    shown = results[:max_results]
    print(f"\n🔍 Found {len(results)} result(s)" + (f" (showing top {max_results})" if len(results) > max_results else ""))
    print("=" * 70)
    
    for i, conv in enumerate(shown, 1):
        date_short = conv.get("date", "")[:10]
        status_icon = {"completed": "✅", "in-progress": "🔄", "unknown": "⬜"}.get(conv.get("status", ""), "⬜")
        
        print(f"\n{i}. {status_icon} {conv.get('title', 'Untitled')}")
        print(f"   📅 {date_short}  |  ID: {conv['id'][:12]}...")
        
        if conv.get("domains"):
            print(f"   🏷️  Domains: {', '.join(conv['domains'][:4])}")
        
        if conv.get("experts"):
            print(f"   👤 Experts: {', '.join(conv['experts'][:3])}")
        
        if conv.get("topics"):
            print(f"   📌 Topics: {', '.join(conv['topics'][:5])}")
        
        if conv.get("artifacts"):
            print(f"   📄 Artifacts:")
            for art in conv["artifacts"]:
                print(f"      • {art['name']}")
                if art.get("summary"):
                    summary = art["summary"][:100]
                    print(f"        {summary}...")
    
    print("\n" + "=" * 70)
    if len(results) > max_results:
        print(f"   ... and {len(results) - max_results} more results")


def display_organization_matches(matches: list[dict]):
    """Display organization manifest matches after conversation results."""

    if not matches:
        return
    print("\nOrganization matches")
    print("=" * 70)
    for i, entry in enumerate(matches, 1):
        rel = entry.get("relative_path") or entry.get("path") or "unknown"
        project = entry.get("project") or "unknown"
        domain = entry.get("domain") or "unknown"
        status = entry.get("status") or "unknown"
        print(f"{i}. {rel}")
        print(f"   project: {project}  |  domain: {domain}  |  status: {status}")


def display_all_domains(conversations: list):
    """Show all domains with counts."""
    domain_counts = {}
    for conv in conversations:
        for d in conv.get("domains", []):
            domain_counts[d] = domain_counts.get(d, 0) + 1
    
    print("\n📂 ALL DOMAINS:")
    print("=" * 40)
    for domain, count in sorted(domain_counts.items(), key=lambda x: -x[1]):
        bar = "█" * min(count, 30)
        print(f"  {domain:20s} {count:3d}  {bar}")


def display_all_experts(conversations: list):
    """Show all experts with counts."""
    expert_counts = {}
    for conv in conversations:
        for e in conv.get("experts", []):
            expert_counts[e] = expert_counts.get(e, 0) + 1
    
    print("\n👤 ALL EXPERTS:")
    print("=" * 40)
    for expert, count in sorted(expert_counts.items(), key=lambda x: -x[1]):
        bar = "█" * min(count, 30)
        print(f"  {expert:20s} {count:3d}  {bar}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Search your conversation history and artifacts",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument("query", nargs="?", default="", help="Search keyword or phrase")
    parser.add_argument("--domain", "-d", help="Filter by domain (e.g., LinkedIn, Strategy)")
    parser.add_argument("--expert", "-e", help="Filter by expert name")
    parser.add_argument("--type", "-t", help="Filter by artifact type (e.g., walkthrough, implementation_plan)")
    parser.add_argument("--since", "-s", help="Filter conversations since date (YYYY-MM-DD)")
    parser.add_argument("--recent", "-r", type=int, help="Show N most recent conversations")
    parser.add_argument("--max", "-m", type=int, default=20, help="Max results to display (default: 20)")
    parser.add_argument("--all-domains", action="store_true", help="List all domains with counts")
    parser.add_argument("--all-experts", action="store_true", help="List all experts with counts")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    
    args = parser.parse_args()
    
    conversations = load_index()
    
    # Special display modes
    if args.all_domains:
        display_all_domains(conversations)
        return
    
    if args.all_experts:
        display_all_experts(conversations)
        return
    
    # Apply filters
    results = conversations
    
    if args.query:
        results = search_keyword(results, args.query)
    
    if args.domain:
        results = filter_domain(results, args.domain)
    
    if args.expert:
        results = filter_expert(results, args.expert)
    
    if args.type:
        results = filter_type(results, args.type)
    
    if args.since:
        results = filter_since(results, args.since)
    
    if args.recent:
        results = get_recent(results, args.recent)
    
    # No filters applied and no query
    if not args.query and not args.domain and not args.expert and not args.type and not args.since and not args.recent:
        print("Usage: python execution/context_search.py \"keyword\"")
        print("       python execution/context_search.py --recent 5")
        print("       python execution/context_search.py --all-domains")
        print("Run with --help for all options.")
        return
    
    organization_matches = search_organization_manifest(args.query, max_results=args.max) if args.query else []

    # Output
    if args.json:
        print(json.dumps({"conversations": results[:args.max], "organization_matches": organization_matches}, indent=2, default=str))
    else:
        display_results(results, max_results=args.max)
        display_organization_matches(organization_matches)


if __name__ == "__main__":
    main()
