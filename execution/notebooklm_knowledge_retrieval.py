#!/usr/bin/env python3
"""
Hybrid Knowledge Retrieval — Smart routing across all Antigravity knowledge sources.

Routes queries to the appropriate knowledge source(s) based on query type:
- Expert methodology → NotebookLM + Skills
- Project context → Notion + NotebookLM
- Current trends → Perplexity
- Code/system → Files (directives, skills, agents)
- Historical → Files (git, session state) + Notion

Returns ranked, merged results compressed to max 1,500 tokens.

Usage:
    from notebooklm_knowledge_retrieval import HybridKnowledgeRetrieval

    retriever = HybridKnowledgeRetrieval()
    result = retriever.search("What are Lara's hook patterns?", scope="auto")

    print(result.summary())
"""

import hashlib
import json
import re
import subprocess
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import List, Optional

from execution.notebooklm_client import NotebookLMClient, load_env


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BASE_PATH = Path(__file__).parent.parent
CACHE_FILE = BASE_PATH / ".agent" / "hybrid-search-cache.json"
CACHE_TTL_HOURS = 24
MAX_TOTAL_TOKENS = 1500


# ---------------------------------------------------------------------------
# Data Structures
# ---------------------------------------------------------------------------

@dataclass
class KnowledgeSnippet:
    """A single knowledge result from a source."""
    source: str  # "notebooklm:LinkedIn Research", "skills:lara-acosta", "files:CLAUDE.md", etc.
    content: str
    relevance_score: float = 0.0
    timestamp: Optional[datetime] = None
    tokens: int = 0  # Rough estimate: len(content) / 4

    def __post_init__(self):
        if self.tokens == 0:
            self.tokens = len(self.content) // 4


@dataclass
class KnowledgeResult:
    """Aggregated result from hybrid knowledge search."""
    query: str
    sources_searched: List[str] = field(default_factory=list)
    results: List[KnowledgeSnippet] = field(default_factory=list)
    total_tokens: int = 0
    cache_hit: bool = False

    def summary(self) -> str:
        """Generate a summary of all results."""
        if not self.results:
            return f"No results found for: {self.query}"

        output = []
        output.append(f"## Knowledge Search Results\n")
        output.append(f"**Query**: {self.query}")
        output.append(f"**Sources searched**: {', '.join(self.sources_searched)}")
        output.append(f"**Cache hit**: {'Yes' if self.cache_hit else 'No'}\n")

        for i, snippet in enumerate(self.results, 1):
            output.append(f"### {i}. {snippet.source} (relevance: {snippet.relevance_score:.0%})")
            output.append(f"{snippet.content}\n")

        output.append(f"**Total tokens**: ~{self.total_tokens}")

        return "\n".join(output)

    def compress(self, max_tokens: int = MAX_TOTAL_TOKENS) -> 'KnowledgeResult':
        """Compress results to fit token budget."""
        if self.total_tokens <= max_tokens:
            return self

        # Sort by relevance, truncate to fit budget
        sorted_results = sorted(self.results, key=lambda x: x.relevance_score, reverse=True)

        compressed = []
        token_budget = 0

        for snippet in sorted_results:
            if token_budget + snippet.tokens > max_tokens:
                # Truncate this snippet to fit
                remaining_tokens = max_tokens - token_budget
                remaining_chars = remaining_tokens * 4
                if remaining_chars > 100:  # Only include if meaningful content remains
                    truncated_content = snippet.content[:remaining_chars] + "..."
                    compressed.append(KnowledgeSnippet(
                        source=snippet.source,
                        content=truncated_content,
                        relevance_score=snippet.relevance_score,
                        timestamp=snippet.timestamp,
                        tokens=remaining_tokens,
                    ))
                break

            compressed.append(snippet)
            token_budget += snippet.tokens

        return KnowledgeResult(
            query=self.query,
            sources_searched=self.sources_searched,
            results=compressed,
            total_tokens=token_budget,
            cache_hit=self.cache_hit,
        )


# ---------------------------------------------------------------------------
# Query Classification
# ---------------------------------------------------------------------------

class QueryClassifier:
    """Classifies queries to determine which knowledge sources to use."""

    PATTERNS = {
        "expert_methodology": [
            r"what (did|does|is) (\w+) (say|teach|recommend)",
            r"(\w+)'s (methodology|approach|framework|strategy)",
            r"how (did|does) (\w+) (handle|approach|solve)",
            r"(hook|cta|proof|story|framework) patterns?",
        ],
        "project_context": [
            r"my (icp|avatar|audience|target)",
            r"my (product|offer|service)",
            r"our (positioning|brand|messaging)",
            r"current (project|campaign|initiative)",
        ],
        "current_trends": [
            r"latest (\w+)",
            r"current (state|trends?|market)",
            r"(\d{4}) (data|research|analysis)",
            r"recent (changes?|developments?)",
        ],
        "code_system": [
            r"how (do|to) (add|create|modify|build) (a|an|the)",
            r"(agent|skill|directive|workflow|command)",
            r"file (structure|organization)",
            r"implementation",
        ],
        "historical": [
            r"why (did|do) (we|i) (choose|decide|use)",
            r"(previous|past|earlier) (decision|choice)",
            r"what happened",
            r"when (did|was)",
        ],
    }

    def classify(self, query: str) -> str:
        """Classify query into type."""
        query_lower = query.lower()

        for query_type, patterns in self.PATTERNS.items():
            for pattern in patterns:
                if re.search(pattern, query_lower):
                    return query_type

        # Default: expert_methodology (most common)
        return "expert_methodology"


# ---------------------------------------------------------------------------
# Hybrid Knowledge Retrieval
# ---------------------------------------------------------------------------

class HybridKnowledgeRetrieval:
    """Orchestrates searches across all knowledge sources."""

    def __init__(self):
        load_env()
        self.notebooklm = NotebookLMClient()
        self.classifier = QueryClassifier()

    def search(
        self,
        query: str,
        *,
        scope: str = "auto",
        use_cache: bool = True,
    ) -> KnowledgeResult:
        """
        Search across knowledge sources.

        Args:
            query: The search query
            scope: "auto" (smart routing), "local" (files only), "notion", "notebooks", "web", "all"
            use_cache: Whether to use cached results (default True)

        Returns:
            KnowledgeResult with aggregated, ranked results
        """
        # Check cache
        if use_cache:
            cached = self._check_cache(query, scope)
            if cached:
                print(f"  ✓ Cache hit for hybrid search")
                return cached

        # Determine sources to search
        if scope == "auto":
            query_type = self.classifier.classify(query)
            sources = self._get_sources_for_type(query_type)
        else:
            sources = self._get_sources_for_scope(scope)

        # Search each source
        results = []
        sources_searched = []

        for source in sources:
            try:
                snippets = self._search_source(source, query)
                results.extend(snippets)
                sources_searched.append(source)
            except Exception as e:
                print(f"  ⚠️  Search failed for {source}: {e}")
                continue

        # Rank by relevance
        results = self._rank_results(results, query)

        # Build result
        total_tokens = sum(r.tokens for r in results)

        result = KnowledgeResult(
            query=query,
            sources_searched=sources_searched,
            results=results,
            total_tokens=total_tokens,
            cache_hit=False,
        )

        # Compress if needed
        if total_tokens > MAX_TOTAL_TOKENS:
            result = result.compress()

        # Cache result
        self._cache_result(query, scope, result)

        return result

    def _get_sources_for_type(self, query_type: str) -> List[str]:
        """Get knowledge sources for a query type."""
        routing = {
            "expert_methodology": ["notebooklm", "skills"],
            "project_context": ["notion", "notebooklm"],
            "current_trends": ["perplexity"],
            "code_system": ["files"],
            "historical": ["files", "notion"],
        }
        return routing.get(query_type, ["notebooklm", "skills"])

    def _get_sources_for_scope(self, scope: str) -> List[str]:
        """Get knowledge sources for explicit scope."""
        scopes = {
            "local": ["files", "skills"],
            "notion": ["notion"],
            "notebooks": ["notebooklm"],
            "web": ["perplexity"],
            "all": ["notebooklm", "notion", "files", "skills", "perplexity"],
        }
        return scopes.get(scope, ["notebooklm", "skills"])

    def _search_source(self, source: str, query: str) -> List[KnowledgeSnippet]:
        """Search a specific knowledge source."""
        if source == "notebooklm":
            return self._search_notebooklm(query)
        elif source == "skills":
            return self._search_skills(query)
        elif source == "files":
            return self._search_files(query)
        elif source == "notion":
            return self._search_notion(query)
        elif source == "perplexity":
            return self._search_perplexity(query)
        else:
            return []

    def _search_notebooklm(self, query: str) -> List[KnowledgeSnippet]:
        """Search NotebookLM notebooks."""
        try:
            results = self.notebooklm.search_all_notebooks(query, limit=3, task_context="hybrid_search")
            snippets = []

            for nb_id, result in results.items():
                snippets.append(KnowledgeSnippet(
                    source=f"notebooklm:{result.notebook_name}",
                    content=result.compress(),
                    relevance_score=0.9,  # High relevance for direct matches
                    timestamp=datetime.now(timezone.utc),
                ))

            return snippets

        except Exception as e:
            print(f"  ⚠️  NotebookLM search failed: {e}")
            return []

    def _search_skills(self, query: str) -> List[KnowledgeSnippet]:
        """Search skills directory."""
        try:
            # Use grep to search SKILL.md and genius.md files
            cmd = [
                "grep", "-r", "-i", "-n",
                "--include=SKILL.md",
                "--include=genius.md",
                query,
                str(BASE_PATH / "skills"),
            ]

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)

            if result.returncode != 0:
                return []

            # Parse grep output
            snippets = []
            for line in result.stdout.splitlines()[:5]:  # Top 5 matches
                if ":" in line:
                    path, content = line.split(":", 2)[0], line.split(":", 2)[-1]
                    skill_name = Path(path).parent.name

                    snippets.append(KnowledgeSnippet(
                        source=f"skills:{skill_name}",
                        content=content.strip()[:500],  # Truncate
                        relevance_score=0.8,
                    ))

            return snippets

        except Exception as e:
            print(f"  ⚠️  Skills search failed: {e}")
            return []

    def _search_files(self, query: str) -> List[KnowledgeSnippet]:
        """Search files (directives, CLAUDE.md, etc.)."""
        try:
            # Search directives and root docs
            search_paths = [
                BASE_PATH / "directives",
                BASE_PATH / "CLAUDE.md",
                BASE_PATH / "DOMAIN_REGISTRY.md",
                BASE_PATH / ".agent",
            ]

            snippets = []

            for path in search_paths:
                if not path.exists():
                    continue

                if path.is_file():
                    # Search single file
                    content = path.read_text()
                    if query.lower() in content.lower():
                        # Extract context around match
                        idx = content.lower().index(query.lower())
                        start = max(0, idx - 200)
                        end = min(len(content), idx + 300)
                        snippet_text = content[start:end]

                        snippets.append(KnowledgeSnippet(
                            source=f"files:{path.name}",
                            content=snippet_text.strip(),
                            relevance_score=0.7,
                        ))

            return snippets[:3]  # Top 3 matches

        except Exception as e:
            print(f"  ⚠️  Files search failed: {e}")
            return []

    def _search_notion(self, query: str) -> List[KnowledgeSnippet]:
        """Search Notion databases (stub — requires notion_api.py integration)."""
        # TODO: Integrate with notion_api.py when available
        return []

    def _search_perplexity(self, query: str) -> List[KnowledgeSnippet]:
        """Search Perplexity (stub — requires perplexity_client.py integration)."""
        # TODO: Integrate with perplexity_client.py when available
        return []

    def _rank_results(self, results: List[KnowledgeSnippet], query: str) -> List[KnowledgeSnippet]:
        """Rank results by relevance."""
        # Simple ranking: already have relevance scores set per source
        # In future: could do semantic similarity, keyword matching, etc.
        return sorted(results, key=lambda x: x.relevance_score, reverse=True)

    def _check_cache(self, query: str, scope: str) -> Optional[KnowledgeResult]:
        """Check if cached result exists and is valid."""
        if not CACHE_FILE.exists():
            return None

        try:
            cache = json.loads(CACHE_FILE.read_text())
        except (json.JSONDecodeError, OSError):
            return None

        cache_key = self._cache_key(query, scope)
        entry = cache.get(cache_key)

        if not entry:
            return None

        # Check TTL
        cached_at = datetime.fromisoformat(entry["cached_at"])
        age = datetime.now(timezone.utc) - cached_at

        if age > timedelta(hours=CACHE_TTL_HOURS):
            return None

        # Reconstruct result
        results = [
            KnowledgeSnippet(
                source=r["source"],
                content=r["content"],
                relevance_score=r["relevance_score"],
                timestamp=datetime.fromisoformat(r["timestamp"]) if r.get("timestamp") else None,
                tokens=r["tokens"],
            )
            for r in entry["results"]
        ]

        return KnowledgeResult(
            query=entry["query"],
            sources_searched=entry["sources_searched"],
            results=results,
            total_tokens=entry["total_tokens"],
            cache_hit=True,
        )

    def _cache_result(self, query: str, scope: str, result: KnowledgeResult):
        """Cache a search result."""
        cache = {}
        if CACHE_FILE.exists():
            try:
                cache = json.loads(CACHE_FILE.read_text())
            except (json.JSONDecodeError, OSError):
                cache = {}

        cache_key = self._cache_key(query, scope)
        cache[cache_key] = {
            "query": result.query,
            "sources_searched": result.sources_searched,
            "results": [
                {
                    "source": r.source,
                    "content": r.content,
                    "relevance_score": r.relevance_score,
                    "timestamp": r.timestamp.isoformat() if r.timestamp else None,
                    "tokens": r.tokens,
                }
                for r in result.results
            ],
            "total_tokens": result.total_tokens,
            "cached_at": datetime.now(timezone.utc).isoformat(),
        }

        CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
        CACHE_FILE.write_text(json.dumps(cache, indent=4))

    def _cache_key(self, query: str, scope: str) -> str:
        """Generate cache key for query + scope."""
        combined = f"{scope}:{query.lower().strip()}"
        return hashlib.sha256(combined.encode()).hexdigest()[:16]


# ---------------------------------------------------------------------------
# CLI (for testing)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python notebooklm_knowledge_retrieval.py <query> [scope]")
        print("Scopes: auto (default), local, notion, notebooks, web, all")
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    scope = "auto"

    # Check if last arg is a scope
    if query.split()[-1] in ["auto", "local", "notion", "notebooks", "web", "all"]:
        scope = query.split()[-1]
        query = " ".join(query.split()[:-1])

    retriever = HybridKnowledgeRetrieval()
    result = retriever.search(query, scope=scope)

    print(result.summary())
