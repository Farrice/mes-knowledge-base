#!/usr/bin/env python3
"""
Semantic Memory Selector — LLM-powered context retrieval for Antigravity.

Replaces manual "check KI summaries" and keyword-based routing with
semantic query-aware selection. Uses Gemini Flash Lite (~$0.00015/call)
for cost-efficient relevance scoring.

Usage:
    # CLI — quick selection for a query
    python execution/memory_selector.py "How do I write vicious hooks for a SaaS product?"

    # CLI — with category filter
    python execution/memory_selector.py "Build a LinkedIn content strategy" --category skills

    # CLI — rebuild the manifest cache
    python execution/memory_selector.py --rebuild

    # Python API
    from memory_selector import MemorySelector, load_env
    load_env()
    selector = MemorySelector()
    results = selector.select_sync("How do I write vicious hooks?", top_k=5)
    for item in results:
        print(f"{item['name']} ({item['category']}) — {item['relevance']}")
"""

import argparse
import asyncio
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Allow imports from execution/
sys.path.insert(0, str(Path(__file__).parent))
from gemini_client import GeminiClient, load_env

BASE_PATH = Path(__file__).parent.parent
SKILLS_DIR = BASE_PATH / "skills"
KI_DIR = Path.home() / ".gemini" / "antigravity" / "knowledge"
DIRECTIVES_DIR = BASE_PATH / "directives"
MANIFEST_CACHE = BASE_PATH / ".agent" / "memory-manifest.json"

# Categories of memory items
CATEGORIES = ["skills", "knowledge_items", "directives"]


# ---------------------------------------------------------------------------
# Manifest Builder — scans the file system and extracts descriptions
# ---------------------------------------------------------------------------

def extract_skill_description(skill_dir: Path) -> Optional[Dict[str, str]]:
    """Extract name + description from a skill's SKILL.md file."""
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return None

    content = skill_md.read_text(errors="ignore")[:2000]  # First 2KB is enough

    # Extract name from frontmatter or first heading
    name = skill_dir.name
    name_match = re.search(r'^name:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
    if name_match:
        name = name_match.group(1).strip()

    # Extract description from frontmatter or first paragraph
    desc = ""
    desc_match = re.search(r'^description:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
    if desc_match:
        desc = desc_match.group(1).strip()
    else:
        # Fall back to first non-heading paragraph
        lines = content.split("\n")
        for line in lines:
            line = line.strip()
            if line and not line.startswith("#") and not line.startswith("---") and not line.startswith("name:"):
                desc = line[:200]
                break

    if not desc:
        desc = f"Expert skill: {name}"

    # Check for genius.md availability (indicates deep mode)
    has_genius = (skill_dir / "genius.md").exists()

    # Count workflows
    workflows_dir = skill_dir / "workflows"
    workflow_count = len(list(workflows_dir.glob("*.md"))) if workflows_dir.exists() else 0

    return {
        "name": name,
        "path": str(skill_dir.relative_to(BASE_PATH)),
        "category": "skills",
        "description": desc,
        "has_genius": has_genius,
        "workflow_count": workflow_count,
    }


def extract_ki_description(ki_dir: Path) -> Optional[Dict[str, str]]:
    """Extract name + description from a KI's metadata.json."""
    meta_file = ki_dir / "metadata.json"
    if not meta_file.exists():
        return None

    try:
        meta = json.loads(meta_file.read_text())
    except (json.JSONDecodeError, UnicodeDecodeError):
        return None

    name = meta.get("title", ki_dir.name)
    summary = meta.get("summary", "")
    if not summary:
        summary = f"Knowledge item: {name}"

    return {
        "name": name,
        "path": str(ki_dir),
        "category": "knowledge_items",
        "description": summary[:300],
    }


def extract_directive_description(directive_file: Path) -> Optional[Dict[str, str]]:
    """Extract name + first-line description from a directive .md file."""
    if not directive_file.suffix == ".md":
        return None

    content = directive_file.read_text(errors="ignore")[:500]
    name = directive_file.stem

    # Get first non-empty, non-heading line as description
    desc = ""
    for line in content.split("\n"):
        line = line.strip()
        if line and not line.startswith("#") and not line.startswith("---") and not line.startswith(">"):
            desc = line[:200]
            break

    if not desc:
        desc = f"Directive: {name}"

    return {
        "name": name,
        "path": str(directive_file.relative_to(BASE_PATH)),
        "category": "directives",
        "description": desc,
    }


def build_manifest(
    categories: Optional[List[str]] = None,
    force_rebuild: bool = False,
) -> List[Dict[str, Any]]:
    """Build or load cached manifest of all memory items."""

    # Use cache if fresh (< 1 hour old)
    if not force_rebuild and MANIFEST_CACHE.exists():
        age_seconds = time.time() - MANIFEST_CACHE.stat().st_mtime
        if age_seconds < 3600:
            try:
                cached = json.loads(MANIFEST_CACHE.read_text())
                if categories:
                    return [m for m in cached if m["category"] in categories]
                return cached
            except (json.JSONDecodeError, KeyError):
                pass  # Rebuild if cache is corrupted

    cats = categories or CATEGORIES
    manifest = []

    # 1. Skills
    if "skills" in cats and SKILLS_DIR.exists():
        for skill_dir in sorted(SKILLS_DIR.iterdir()):
            if skill_dir.is_dir() and not skill_dir.name.startswith("."):
                item = extract_skill_description(skill_dir)
                if item:
                    manifest.append(item)

    # 2. Knowledge Items
    if "knowledge_items" in cats and KI_DIR.exists():
        for ki_dir in sorted(KI_DIR.iterdir()):
            if ki_dir.is_dir():
                item = extract_ki_description(ki_dir)
                if item:
                    manifest.append(item)

    # 3. Directives
    if "directives" in cats and DIRECTIVES_DIR.exists():
        for directive_file in sorted(DIRECTIVES_DIR.glob("*.md")):
            item = extract_directive_description(directive_file)
            if item:
                manifest.append(item)

    # Cache the full manifest
    MANIFEST_CACHE.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_CACHE.write_text(json.dumps(manifest, indent=2))

    if categories:
        return [m for m in manifest if m["category"] in categories]
    return manifest


# ---------------------------------------------------------------------------
# Semantic Selector — uses Gemini to pick the most relevant items
# ---------------------------------------------------------------------------

SELECTION_SYSTEM_PROMPT = """You are a memory selector for an AI orchestration system called Antigravity.

Given a user query and a manifest of available memory items (skills, knowledge items, directives), select the 3-5 most relevant items that should be loaded into context to best handle this query.

Rules:
1. Select items whose descriptions SEMANTICALLY match the query intent — not just keyword overlap
2. Prefer skills with workflows and genius.md (deeper expertise) for complex tasks
3. Include relevant directives only if they directly affect how to handle this query
4. For content tasks, include at least 2 skills (per content creation gate)
5. If the query mentions a specific expert by name, their skill MUST be included
6. Deprioritize items that are tangentially related — precision over recall

Return ONLY a JSON array of objects, each with:
- "name": The item name exactly as shown in the manifest
- "category": "skills" | "knowledge_items" | "directives"
- "relevance": A 1-sentence explanation of why this item is relevant
- "priority": 1-5 (1 = most relevant)

Example:
[
  {"name": "luke-iha-vicious-hooks", "category": "skills", "relevance": "Directly teaches the hook writing methodology requested", "priority": 1},
  {"name": "lara-acosta-linkedin-mastery", "category": "skills", "relevance": "LinkedIn platform expertise for targeting context", "priority": 2}
]"""


class MemorySelector:
    """LLM-powered semantic memory selector."""

    def __init__(self, client: Optional[GeminiClient] = None):
        self.client = client or GeminiClient()

    async def select(
        self,
        query: str,
        *,
        top_k: int = 5,
        categories: Optional[List[str]] = None,
        force_rebuild: bool = False,
    ) -> List[Dict[str, Any]]:
        """
        Semantically select the most relevant memory items for a query.

        Args:
            query: The user's request or intent.
            top_k: Maximum items to return (default: 5).
            categories: Filter to specific categories.
            force_rebuild: Force manifest rebuild.

        Returns:
            List of selected memory items with relevance explanations.
        """
        manifest = build_manifest(categories=categories, force_rebuild=force_rebuild)

        if not manifest:
            return []

        # Build compact manifest for the LLM
        compact_lines = []
        for i, item in enumerate(manifest):
            extras = ""
            if item.get("has_genius"):
                extras += " [has genius.md]"
            if item.get("workflow_count", 0) > 0:
                extras += f" [{item['workflow_count']} workflows]"
            compact_lines.append(
                f"{i+1}. [{item['category']}] {item['name']}: {item['description']}{extras}"
            )

        manifest_text = "\n".join(compact_lines)

        prompt = f"""USER QUERY: {query}

AVAILABLE MEMORY ITEMS ({len(manifest)} total):
{manifest_text}

Select the {top_k} most relevant items. Return ONLY a JSON array."""

        text, meta = await self.client.generate(
            prompt,
            system_instruction=SELECTION_SYSTEM_PROMPT,
            model="lite",  # Cheapest tier — ~$0.00015/call
            temperature=0.1,  # Low temperature for consistent selection
            max_output_tokens=1024,
            response_mime_type="application/json",
        )

        # Parse response
        try:
            # Clean potential markdown fencing
            clean = text.strip()
            if clean.startswith("```"):
                clean = re.sub(r'^```\w*\n?', '', clean)
                clean = re.sub(r'\n?```$', '', clean)
            selections = json.loads(clean)
        except json.JSONDecodeError:
            print(f"  ⚠️  Memory selector returned invalid JSON, falling back to empty")
            return []

        # Enrich with full manifest data
        name_to_item = {item["name"]: item for item in manifest}
        enriched = []
        for sel in selections[:top_k]:
            name = sel.get("name", "")
            base = name_to_item.get(name, {})
            enriched.append({
                **base,
                "relevance": sel.get("relevance", ""),
                "priority": sel.get("priority", 99),
            })

        # Sort by priority
        enriched.sort(key=lambda x: x.get("priority", 99))

        print(f"\n  🧠 Memory Selector: {len(enriched)} items selected "
              f"(cost: ${meta.estimated_cost_usd:.4f})")
        for item in enriched:
            print(f"     [{item.get('priority', '?')}] {item.get('name', '?')} "
                  f"({item.get('category', '?')}) — {item.get('relevance', '')}")

        return enriched

    def select_sync(
        self,
        query: str,
        **kwargs,
    ) -> List[Dict[str, Any]]:
        """Synchronous wrapper for select()."""
        loop = asyncio.new_event_loop()
        try:
            return loop.run_until_complete(self.select(query, **kwargs))
        finally:
            loop.close()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Semantic Memory Selector — find the most relevant skills, KIs, and directives for any query"
    )
    parser.add_argument(
        "query",
        nargs="?",
        help="The query to find relevant memory items for"
    )
    parser.add_argument(
        "--category",
        choices=["skills", "knowledge_items", "directives"],
        help="Filter to a specific category"
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=5,
        help="Number of items to return (default: 5)"
    )
    parser.add_argument(
        "--rebuild",
        action="store_true",
        help="Force rebuild of the manifest cache"
    )
    parser.add_argument(
        "--manifest-only",
        action="store_true",
        help="Just build/show the manifest without LLM selection"
    )

    args = parser.parse_args()
    load_env()

    categories = [args.category] if args.category else None

    if args.rebuild or args.manifest_only:
        manifest = build_manifest(categories=categories, force_rebuild=True)
        print(f"\n📋 Manifest: {len(manifest)} items")
        for cat in CATEGORIES:
            count = sum(1 for m in manifest if m["category"] == cat)
            if count:
                print(f"   {cat}: {count}")
        if args.manifest_only:
            return

    if not args.query:
        if not args.rebuild:
            parser.print_help()
        return

    selector = MemorySelector()
    results = selector.select_sync(
        args.query,
        top_k=args.top_k,
        categories=categories,
        force_rebuild=args.rebuild,
    )

    if not results:
        print("\n❌ No relevant items found.")
        return

    # Output as JSON for scripting
    print(f"\n📑 Results ({len(results)} selected):")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
