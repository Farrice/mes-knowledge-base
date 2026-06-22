#!/usr/bin/env python3
"""
Workflow Router — Intelligent workflow lookup to reduce context overhead.

Instead of loading all 524 workflow descriptions into every prompt,
this script provides fast keyword/domain-based routing.

Usage:
    python3 execution/workflow_router.py search "linkedin content strategy"
    python3 execution/workflow_router.py domain "proof"
    python3 execution/workflow_router.py stats
    python3 execution/workflow_router.py domains
"""

import os
import re
import sys
import argparse
from pathlib import Path
from collections import defaultdict

WF_DIR = Path(".agent/workflows")
INDEX_CACHE = None

# Domain mapping for intelligent routing
DOMAIN_MAP = {
    "linkedin": ["diandra", "lara", "high-dwell", "profile-conversion", "algorithmic-reach"],
    "copy": ["proof", "vicious", "hook", "mechanism", "copy", "fascination", "persuasion"],
    "brand": ["junyuh", "caleb", "oren", "taste", "grace", "zero-to-brand", "manifesto"],
    "ghostwriting": ["ghost", "voice", "cole", "roth"],
    "content": ["content", "atomize", "format", "serial", "parallel-content", "quantity-sprint"],
    "newsletter": ["newsletter", "substack", "parallax", "book-never-ends"],
    "psychology": ["drk", "kallaway", "belief", "identity", "consciousness", "resistance"],
    "seo": ["gotch", "parasite-seo", "analyze-intent"],
    "ads": ["ad-script", "full-stack-ad", "cash-method", "creative-diversity", "ai-ad-production"],
    "offers": ["design-offer", "offer-stack", "offer-cycle", "high-ticket", "nuclear-vsl"],
    "real-estate": ["enrico", "listing", "data-driven-ops"],
    "agentic": ["saraev", "swarm", "council", "parallel", "orchestration", "auto-experiment"],
    "system": ["system", "health-check", "calibrate", "harness", "evolution", "session"],
    "writing": ["connelly", "wright", "roth", "word", "haunt", "erosion", "estrangement", "memoir"],
    "research": ["research", "deep-research", "competitor", "icp", "generate-brief"],
    "extraction": ["extract", "convert", "compile-knowledge", "knowledge"],
    "client": ["client", "outreach", "proposal", "npq", "cold-outreach", "upwork"],
    "fladlien": ["fladlien"],
    "revenue": ["revenue", "monetize", "recurring", "affiliate", "lifestyle-business"],
}

CONTROL_PLANE_PRIORITY = [
    (
        ("autopilot", "triage menu", "skill selection", "what workflow", "what should i use", "too many tools", "front door"),
        "autopilot",
    ),
    (
        ("autopilot", "triage menu", "skill selection", "self improving", "self-improving"),
        "source-to-skill-system",
    ),
    (
        ("autopilot", "triage menu", "show me the menu", "orchestration", "skill selection"),
        "orchestrate",
    ),
    (
        ("autopilot", "routing", "monitoring", "triage menu"),
        "routing-intelligence",
    ),
    (
        ("autopilot", "self improving", "self-improving", "improve workflow"),
        "self-evolve",
    ),
    (
        ("autopilot", "skill selection", "quality plateau", "skill prompt"),
        "skill-anneal",
    ),
    (
        ("not firing", "isn't firing", "codex feels", "harness", "routing layer", "orchestration layer", "hook parity", "context load", "skill loading"),
        "system-audit",
    ),
    (
        ("lost the magic", "cannot repeat", "can't repeat", "revision got worse", "repeatability", "regression", "preservation lock"),
        "repeatability-spine",
    ),
    (
        ("source-to-skill-system", "source to skill system", "source-to-system", "source to system", "turn this source", "connected skill system", "workflow bridge"),
        "source-to-skill-system",
    ),
    (
        ("knowledge pulse", "library pulse", "prior decisions", "reusable solution", "sleeping giants", "underused workflow"),
        "knowledge-librarian",
    ),
]


def build_index():
    """Build the workflow index from .agent/workflows/."""
    global INDEX_CACHE
    if INDEX_CACHE is not None:
        return INDEX_CACHE

    index = []
    for f in sorted(WF_DIR.glob("*.md")):
        name = f.stem
        try:
            content = f.read_text(errors="ignore")
        except (FileNotFoundError, OSError):
            continue  # Skip missing/inaccessible workflow files gracefully

        # Extract description from YAML frontmatter
        desc_match = re.search(r"^description:\s*(.+)$", content, re.MULTILINE)
        if desc_match:
            desc = desc_match.group(1).strip().strip("\"'")
        else:
            # Fallback: first heading after frontmatter
            heading = re.search(r"^#+\s+(.+)$", content, re.MULTILINE)
            desc = heading.group(1) if heading else name

        # Extract first-level heading for full name
        h1 = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        full_name = h1.group(1) if h1 else name

        index.append({
            "name": name,
            "full_name": full_name,
            "description": desc,
            "size": len(content),
            "path": str(f),
        })

    INDEX_CACHE = index
    return index


def search_workflows(query, top_n=10):
    """Search workflows by keyword matching against name + description."""
    index = build_index()
    query_lower = query.lower()
    query_terms = query_lower.split()
    scored = []

    for wf in index:
        searchable = f"{wf['name']} {wf['description']} {wf['full_name']}".lower()
        score = 0
        for term in query_terms:
            if term in searchable:
                # Exact name match scores highest
                if term in wf["name"]:
                    score += 3
                # Description match
                if term in wf["description"].lower():
                    score += 2
                # Full name match
                if term in wf["full_name"].lower():
                    score += 1
        for signals, workflow in CONTROL_PLANE_PRIORITY:
            if wf["name"] == workflow and any(signal in query_lower for signal in signals):
                score += 50
        if wf["name"] == "autopilot" and "autopilot" in query_lower:
            score += 150
        if score > 0:
            scored.append((score, wf))

    scored.sort(key=lambda x: (-x[0], x[1]["name"]))
    return scored[:top_n]


def domain_lookup(domain):
    """Get all workflows in a domain."""
    index = build_index()
    domain = domain.lower()

    if domain in DOMAIN_MAP:
        prefixes = DOMAIN_MAP[domain]
    else:
        prefixes = [domain]

    results = []
    for wf in index:
        for prefix in prefixes:
            if prefix in wf["name"]:
                results.append(wf)
                break

    return results


def list_domains():
    """List all available domains with workflow counts."""
    index = build_index()
    for domain, prefixes in sorted(DOMAIN_MAP.items()):
        count = len(domain_lookup(domain))
        print(f"  {domain:20s} ({count:3d} workflows) → prefixes: {', '.join(prefixes)}")


def show_stats():
    """Show index statistics."""
    index = build_index()
    total_chars = sum(wf["size"] for wf in index)
    avg_size = total_chars / len(index) if index else 0

    print(f"Total workflows:        {len(index)}")
    print(f"Total content:          {total_chars:,} chars ({total_chars // 4:,} est. tokens)")
    print(f"Avg workflow size:      {avg_size:,.0f} chars ({avg_size // 4:,.0f} est. tokens)")
    print(f"Domains mapped:         {len(DOMAIN_MAP)}")
    print()

    # Show domain distribution
    print("Domain distribution:")
    list_domains()


def main():
    parser = argparse.ArgumentParser(description="Workflow Router")
    sub = parser.add_subparsers(dest="command")

    search_p = sub.add_parser("search", help="Search workflows by keyword")
    search_p.add_argument("query", help="Search query")
    search_p.add_argument("-n", "--top", type=int, default=10, help="Number of results")

    domain_p = sub.add_parser("domain", help="List workflows in a domain")
    domain_p.add_argument("name", help="Domain name")

    sub.add_parser("domains", help="List all domains")
    sub.add_parser("stats", help="Show index statistics")

    args = parser.parse_args()

    if args.command == "search":
        results = search_workflows(args.query, args.top)
        if not results:
            print(f"No workflows match '{args.query}'")
            return
        print(f"Top {len(results)} matches for '{args.query}':\n")
        for score, wf in results:
            print(f"  /{wf['name']:40s} — {wf['description']}")

    elif args.command == "domain":
        results = domain_lookup(args.name)
        if not results:
            print(f"No workflows in domain '{args.name}'")
            return
        print(f"{len(results)} workflows in '{args.name}':\n")
        for wf in results:
            print(f"  /{wf['name']:40s} — {wf['description']}")

    elif args.command == "domains":
        list_domains()

    elif args.command == "stats":
        show_stats()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
