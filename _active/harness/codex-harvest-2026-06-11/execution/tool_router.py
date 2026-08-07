#!/usr/bin/env python3
"""
Tool Router — Dynamic tool selection for context-efficient agent operation.

Instead of loading all MCP tool definitions (~20,000 tokens), this router
selects only task-relevant tool clusters. Core tools always loaded; specialized
tools loaded on demand via keyword matching (MVP) or semantic similarity (future).

Architecture: Option C (Hybrid) — always-on core + keyword-selected specialists.

Usage:
    python3 execution/tool_router.py route "build a Notion database"
    python3 execution/tool_router.py route "deploy to firebase"
    python3 execution/tool_router.py clusters
    python3 execution/tool_router.py inventory
    python3 execution/tool_router.py stats
"""

import sys
import argparse
import json
from collections import defaultdict

# ─────────────────────────────────────────────────────────
# TOOL INVENTORY — All available tools by source
# ─────────────────────────────────────────────────────────

TOOLS = {
    # Core file operations
    "write_to_file":              {"cluster": "file_ops",  "source": "core",     "always_on": True,  "desc": "Create new files"},
    "view_file":                  {"cluster": "file_ops",  "source": "core",     "always_on": True,  "desc": "View file contents"},
    "replace_file_content":       {"cluster": "file_ops",  "source": "core",     "always_on": True,  "desc": "Edit single contiguous block"},
    "multi_replace_file_content": {"cluster": "file_ops",  "source": "core",     "always_on": True,  "desc": "Edit multiple non-contiguous blocks"},
    "list_dir":                   {"cluster": "file_ops",  "source": "core",     "always_on": True,  "desc": "List directory contents"},
    "grep_search":                {"cluster": "file_ops",  "source": "core",     "always_on": True,  "desc": "Search files with ripgrep"},

    # Terminal
    "run_command":                {"cluster": "terminal",  "source": "core",     "always_on": True,  "desc": "Execute terminal commands"},
    "command_status":             {"cluster": "terminal",  "source": "core",     "always_on": True,  "desc": "Check command status"},
    "send_command_input":         {"cluster": "terminal",  "source": "core",     "always_on": True,  "desc": "Send input to running command"},

    # Search & web
    "search_web":                 {"cluster": "search",    "source": "core",     "always_on": True,  "desc": "Web search with citations"},
    "read_url_content":           {"cluster": "search",    "source": "core",     "always_on": False, "desc": "Fetch URL content as markdown"},

    # Browser
    "browser_subagent":           {"cluster": "browser",   "source": "core",     "always_on": False, "desc": "Browser automation subagent"},

    # Image generation
    "generate_image":             {"cluster": "image",     "source": "core",     "always_on": False, "desc": "Generate images from text prompts"},

    # Research
    "perplexity_ask":             {"cluster": "research",  "source": "perplexity-ask", "always_on": False, "desc": "Perplexity AI conversation"},

    # Notion — read operations
    "notion_search":              {"cluster": "notion",    "source": "notion",   "always_on": False, "desc": "Search Notion by title"},
    "notion_retrieve_page":       {"cluster": "notion",    "source": "notion",   "always_on": False, "desc": "Retrieve a Notion page"},
    "notion_get_block_children":  {"cluster": "notion",    "source": "notion",   "always_on": False, "desc": "Get block children"},
    "notion_retrieve_database":   {"cluster": "notion",    "source": "notion",   "always_on": False, "desc": "Retrieve database schema"},
    "notion_query_data_source":   {"cluster": "notion",    "source": "notion",   "always_on": False, "desc": "Query a Notion database"},
    "notion_retrieve_block":      {"cluster": "notion",    "source": "notion",   "always_on": False, "desc": "Retrieve a single block"},
    "notion_retrieve_comment":    {"cluster": "notion",    "source": "notion",   "always_on": False, "desc": "Retrieve comments"},
    "notion_retrieve_property":   {"cluster": "notion",    "source": "notion",   "always_on": False, "desc": "Retrieve page property"},

    # Notion — write operations
    "notion_create_page":         {"cluster": "notion",    "source": "notion",   "always_on": False, "desc": "Create a Notion page"},
    "notion_patch_page":          {"cluster": "notion",    "source": "notion",   "always_on": False, "desc": "Update page properties"},
    "notion_patch_block_children":{"cluster": "notion",    "source": "notion",   "always_on": False, "desc": "Append block children"},
    "notion_create_comment":      {"cluster": "notion",    "source": "notion",   "always_on": False, "desc": "Create a comment"},
    "notion_create_data_source":  {"cluster": "notion",    "source": "notion",   "always_on": False, "desc": "Create a database"},
    "notion_update_block":        {"cluster": "notion",    "source": "notion",   "always_on": False, "desc": "Update a block"},
    "notion_delete_block":        {"cluster": "notion",    "source": "notion",   "always_on": False, "desc": "Delete a block"},
    "notion_move_page":           {"cluster": "notion",    "source": "notion",   "always_on": False, "desc": "Move a page"},
    "notion_update_data_source":  {"cluster": "notion",    "source": "notion",   "always_on": False, "desc": "Update a database"},
    "notion_get_users":           {"cluster": "notion",    "source": "notion",   "always_on": False, "desc": "List all users"},
    "notion_get_self":            {"cluster": "notion",    "source": "notion",   "always_on": False, "desc": "Get bot user info"},

    # Firebase
    "firebase_deploy":            {"cluster": "cloud",     "source": "firebase", "always_on": False, "desc": "Deploy to Firebase"},
    "firebase_hosting":           {"cluster": "cloud",     "source": "firebase", "always_on": False, "desc": "Firebase hosting operations"},
    "firebase_auth":              {"cluster": "cloud",     "source": "firebase", "always_on": False, "desc": "Firebase authentication"},
    "firebase_firestore":         {"cluster": "cloud",     "source": "firebase", "always_on": False, "desc": "Firestore database operations"},

    # Cloud Run
    "cloudrun_deploy":            {"cluster": "cloud",     "source": "cloudrun", "always_on": False, "desc": "Deploy to Cloud Run"},
    "cloudrun_services":          {"cluster": "cloud",     "source": "cloudrun", "always_on": False, "desc": "Manage Cloud Run services"},

    # Design (Pencil)
    "pencil_batch_get":           {"cluster": "design",    "source": "pencil",   "always_on": False, "desc": "Read .pen design files"},
    "pencil_edit":                {"cluster": "design",    "source": "pencil",   "always_on": False, "desc": "Edit .pen design files"},

    # MCP utilities
    "list_resources":             {"cluster": "mcp_util",  "source": "core",     "always_on": False, "desc": "List MCP server resources"},
    "read_resource":              {"cluster": "mcp_util",  "source": "core",     "always_on": False, "desc": "Read MCP server resource"},
}

# ─────────────────────────────────────────────────────────
# TOOL CLUSTERS — Functional groupings with descriptions
# ─────────────────────────────────────────────────────────

CLUSTERS = {
    "file_ops":  {"desc": "File reading, writing, editing, searching", "token_est": 1500},
    "terminal":  {"desc": "Command execution and monitoring",         "token_est": 600},
    "search":    {"desc": "Web search and URL content fetching",      "token_est": 400},
    "browser":   {"desc": "Browser automation and interaction",       "token_est": 300},
    "image":     {"desc": "Image generation from text prompts",       "token_est": 200},
    "research":  {"desc": "Deep research via Perplexity",             "token_est": 200},
    "notion":    {"desc": "Notion workspace operations (CRUD)",       "token_est": 4000},
    "cloud":     {"desc": "Firebase and Cloud Run deployment",        "token_est": 800},
    "design":    {"desc": "Pencil design file operations",            "token_est": 300},
    "mcp_util":  {"desc": "MCP server resource management",          "token_est": 200},
}

# ─────────────────────────────────────────────────────────
# INTENT → CLUSTER MAPPING — Keyword-based selection (MVP)
# ─────────────────────────────────────────────────────────

INTENT_KEYWORDS = {
    "notion": {
        "keywords": [
            "notion", "database", "notion page", "notion db", "notion api",
            "notion block", "notion comment", "notion property", "notion query",
            "kanban", "page property", "data source",
        ],
        "clusters": ["notion", "file_ops"],
    },
    "harness_diagnostics": {
        "keywords": [
            "harness", "control plane", "control-plane", "autopilot",
            "system broken", "system is broken", "things are not working",
            "fix everything", "whatever is not fixed", "get fixed now",
            "repair everything", "repair the system", "repair the harness",
            "bigger repair", "up to the standard", "standard and quality",
            "not working as envisioned", "routing failure", "routing broken",
            "orchestration failure", "runtime preflight", "live trace",
            "verifier", "verification guard", "agent arsenal",
        ],
        "clusters": ["file_ops", "terminal"],
    },
    "cloud_deploy": {
        "keywords": [
            "deploy", "firebase", "cloud run", "cloudrun", "hosting",
            "production", "ship", "launch site", "go live", "publish app",
            "firestore", "authentication", "auth",
        ],
        "clusters": ["cloud", "terminal", "file_ops"],
    },
    "web_build": {
        "keywords": [
            "website", "web app", "frontend", "html", "css", "javascript",
            "react", "next.js", "vite", "landing page", "ui", "ux",
            "component", "responsive", "layout", "styling",
        ],
        "clusters": ["file_ops", "terminal", "browser", "image"],
    },
    "research": {
        "keywords": [
            "research", "investigate", "find out", "what is", "how does",
            "compare", "analyze", "trend", "market", "competitor",
            "perplexity", "deep dive", "intelligence",
        ],
        "clusters": ["research", "search", "file_ops"],
    },
    "design": {
        "keywords": [
            "design", "pencil", ".pen", "wireframe", "mockup", "prototype",
            "visual", "graphic", "brand", "logo", "carousel", "thumbnail",
        ],
        "clusters": ["design", "image", "file_ops"],
    },
    "content": {
        "keywords": [
            "write", "draft", "content", "blog", "article", "newsletter",
            "email", "copy", "script", "post", "linkedin", "twitter",
            "ghostwrite", "edit prose",
        ],
        "clusters": ["file_ops", "search"],
    },
    "code": {
        "keywords": [
            "code", "script", "python", "function", "api", "build",
            "implement", "refactor", "debug", "fix bug", "test",
            "automation", "pipeline", "cli",
        ],
        "clusters": ["file_ops", "terminal", "search"],
    },
    "browser_task": {
        "keywords": [
            "browser", "screenshot", "click", "navigate", "login",
            "fill form", "scrape", "interact", "recording",
        ],
        "clusters": ["browser", "search"],
    },
    "image_gen": {
        "keywords": [
            "generate image", "create image", "illustration", "photo",
            "picture", "asset", "icon", "banner",
        ],
        "clusters": ["image", "file_ops"],
    },
}


def _stem(word):
    """Minimal suffix-strip stemmer matching expert_router.py pattern."""
    for suffix in ("ing", "tion", "ness", "ally", "ment", "ive", "ity", "ly", "ed", "er", "es", "s"):
        if len(word) > len(suffix) + 3 and word.endswith(suffix):
            return word[: -len(suffix)]
    return word


def select_tools(task_intent, verbose=False):
    """
    Classify task intent → return relevant tool cluster names.

    Returns the always-on clusters plus any intent-matched specialist clusters.
    """
    query_lower = task_intent.lower()
    query_words = query_lower.split()
    query_stems = [_stem(w) for w in query_words]
    query_bigrams = [f"{query_words[i]} {query_words[i+1]}" for i in range(len(query_words) - 1)]

    # Always-on clusters
    always_on = {"file_ops", "terminal"}

    # Score each intent category
    intent_scores = {}
    for intent_name, intent_data in INTENT_KEYWORDS.items():
        score = 0
        matched_keywords = []

        for kw in intent_data["keywords"]:
            # Exact substring match (strongest)
            if kw in query_lower:
                score += len(kw.split()) * 3
                matched_keywords.append(kw)
                continue

            # Stem-level matching
            kw_stems = [_stem(w) for w in kw.split()]
            overlap = sum(
                1 for ks in kw_stems
                if any(ks in qs or qs in ks for qs in query_stems if len(qs) > 2)
            )
            if overlap >= max(1, len(kw_stems) * 0.6):
                score += overlap
                matched_keywords.append(f"{kw}~")

        if score > 0:
            intent_scores[intent_name] = {
                "score": score,
                "clusters": intent_data["clusters"],
                "matched": matched_keywords,
            }

    # Collect clusters from all matching intents (threshold: score >= 2)
    selected_clusters = set(always_on)
    matched_intents = []

    for intent_name, data in sorted(intent_scores.items(), key=lambda x: -x[1]["score"]):
        if data["score"] >= 2:
            selected_clusters.update(data["clusters"])
            matched_intents.append((intent_name, data["score"], data["matched"]))

    # If nothing matched beyond always-on, add search as fallback. A matched
    # local diagnostic intent can intentionally stay file/terminal-only.
    if selected_clusters == always_on and not matched_intents:
        selected_clusters.add("search")

    return sorted(selected_clusters), matched_intents


def get_tools_for_clusters(cluster_names):
    """Return all tool names belonging to the given clusters."""
    tools = []
    for tool_name, info in TOOLS.items():
        if info["cluster"] in cluster_names or info["always_on"]:
            tools.append(tool_name)
    return sorted(set(tools))


def estimate_tokens(cluster_names):
    """Estimate token count for the given clusters."""
    total = 0
    counted = set()
    for name in cluster_names:
        if name in CLUSTERS and name not in counted:
            total += CLUSTERS[name]["token_est"]
            counted.add(name)
    return total


def format_route_output(task_intent, clusters, matched_intents):
    """Format routing results for display."""
    all_tokens = sum(c["token_est"] for c in CLUSTERS.values())
    selected_tokens = estimate_tokens(clusters)
    tools = get_tools_for_clusters(clusters)

    print(f"Task: \"{task_intent}\"\n")
    print(f"Selected clusters ({len(clusters)}/{len(CLUSTERS)}):")
    for c in clusters:
        info = CLUSTERS.get(c, {"desc": "unknown", "token_est": 0})
        marker = "★" if c in {"file_ops", "terminal"} else "→"
        print(f"  {marker} {c:12s}  {info['desc']}")
    print()

    if matched_intents:
        print("Intent matches:")
        for name, score, keywords in matched_intents:
            print(f"  {name:20s} (score: {score:.0f})  [{', '.join(keywords[:3])}]")
        print()

    print(f"Tools loaded: {len(tools)}/{len(TOOLS)}")
    print(f"Est. tokens:  {selected_tokens:,} / {all_tokens:,} ({100 - (selected_tokens/all_tokens*100):.0f}% reduction)")
    print(f"\nTool list: {', '.join(tools)}")


def show_clusters():
    """Display all tool clusters."""
    print(f"{'Cluster':15s} {'Tools':6s} {'~Tokens':8s} Description")
    print("-" * 70)
    for name, info in sorted(CLUSTERS.items()):
        tool_count = sum(1 for t in TOOLS.values() if t["cluster"] == name)
        print(f"{name:15s} {tool_count:4d}   {info['token_est']:6,d}   {info['desc']}")

    always_on = [n for n, t in TOOLS.items() if t["always_on"]]
    print(f"\nAlways-on tools ({len(always_on)}): {', '.join(always_on)}")


def show_inventory():
    """Display full tool inventory."""
    by_cluster = defaultdict(list)
    for name, info in TOOLS.items():
        by_cluster[info["cluster"]].append((name, info))

    for cluster in sorted(by_cluster):
        cluster_info = CLUSTERS.get(cluster, {"desc": cluster})
        print(f"\n[{cluster}] — {cluster_info['desc']}")
        for name, info in sorted(by_cluster[cluster]):
            ao = " ★" if info["always_on"] else ""
            print(f"  {name:35s} ({info['source']:15s}){ao}  {info['desc']}")


def show_stats():
    """Show routing statistics."""
    total_tools = len(TOOLS)
    always_on = sum(1 for t in TOOLS.values() if t["always_on"])
    on_demand = total_tools - always_on
    all_tokens = sum(c["token_est"] for c in CLUSTERS.values())
    core_tokens = sum(
        CLUSTERS[c]["token_est"] for c in {"file_ops", "terminal"}
        if c in CLUSTERS
    )

    print(f"Total tools:       {total_tools}")
    print(f"Always-on:         {always_on} (core capabilities)")
    print(f"On-demand:         {on_demand} (loaded per task)")
    print(f"Total clusters:    {len(CLUSTERS)}")
    print(f"Intent categories: {len(INTENT_KEYWORDS)}")
    print(f"\nToken estimates:")
    print(f"  All tools loaded:   ~{all_tokens:,} tokens")
    print(f"  Always-on only:     ~{core_tokens:,} tokens")
    print(f"  Typical task:       ~{core_tokens + 400:,}-{core_tokens + 1200:,} tokens")
    print(f"  Max reduction:      ~{100 - (core_tokens/all_tokens*100):.0f}%")

    by_source = defaultdict(int)
    for t in TOOLS.values():
        by_source[t["source"]] += 1
    print(f"\nTools by source:")
    for source, count in sorted(by_source.items(), key=lambda x: -x[1]):
        print(f"  {source:20s} {count:3d} tools")


def main():
    parser = argparse.ArgumentParser(description="Tool Router — Dynamic tool selection")
    sub = parser.add_subparsers(dest="command")

    route_p = sub.add_parser("route", help="Select tools for a task intent")
    route_p.add_argument("query", help="Task description")

    sub.add_parser("clusters", help="List all tool clusters")
    sub.add_parser("inventory", help="Full tool inventory")
    sub.add_parser("stats", help="Routing statistics")

    args = parser.parse_args()

    if args.command == "route":
        clusters, matched = select_tools(args.query)
        format_route_output(args.query, clusters, matched)

    elif args.command == "clusters":
        show_clusters()

    elif args.command == "inventory":
        show_inventory()

    elif args.command == "stats":
        show_stats()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
