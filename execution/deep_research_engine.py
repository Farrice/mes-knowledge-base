#!/usr/bin/env python3
"""
Deep Research Engine — Universal grounded research for all Antigravity workflows.

Four depth levels:
  - Quick:    3-5 web searches, summarize. Free. ~15-30s.
  - Standard: 10-15 web searches + read top pages + Perplexity synthesis. ~$0.04. ~1-3min.
  - Deep:     sonar-deep-research + wide search + full page reads. ~$0.50-0.75. ~3-8min.
  - Max:      Gemini Deep Research Max (autonomous multi-step agent). Ultra-covered. ~3-10min.
              See directives/google-api-usage-policy.md for billing safety architecture.

Every finding MUST have a source URL. No source = not grounded = gets flagged.

Usage (CLI):
    python execution/deep_research_engine.py --depth quick "AI consulting market size 2025"
    python execution/deep_research_engine.py --depth standard "ghostwriting retainer pricing"
    python execution/deep_research_engine.py --depth deep "premium coaching offer positioning"

Usage (Python):
    from deep_research_engine import ResearchEngine, load_env
    load_env()
    engine = ResearchEngine()
    result = engine.research("AI consulting market size 2025", depth="standard")
    print(result.to_markdown())

Swarm Mode (for workflow orchestration):
    # Decompose → parallel search → read best pages → synthesize
    plan = engine.decompose("How should I price my AI consulting offer?")
    # Returns 5-10 sub-questions, each with suggested search queries
    # Workflows fire these in parallel via sub-agents
"""

import argparse
import json
import os
import re
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlparse

import requests

# ---------------------------------------------------------------------------
# Environment
# ---------------------------------------------------------------------------

BASE_PATH = Path(__file__).parent.parent
ENV_PATH = BASE_PATH / ".env"
TMP_DIR = BASE_PATH / ".tmp" / "research"


def load_env(env_path: Optional[Path] = None):
    """Load .env file into os.environ."""
    path = env_path or ENV_PATH
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip())


# ---------------------------------------------------------------------------
# Data Structures
# ---------------------------------------------------------------------------

@dataclass
class ResearchFinding:
    """A single grounded research finding with provenance."""
    claim: str
    source_url: str
    source_title: str = ""
    source_domain: str = ""
    excerpt: str = ""  # Verbatim text from source
    recency: str = ""  # Date of source if available
    confidence: str = "medium"  # high, medium, low
    finding_type: str = "data"  # data, quote, statistic, opinion, case_study

    def __post_init__(self):
        if self.source_url:
            parsed = urlparse(self.source_url)
            self.source_domain = parsed.netloc


@dataclass
class ResearchSubQuestion:
    """A decomposed sub-question for parallel research."""
    question: str
    search_queries: List[str] = field(default_factory=list)
    angle: str = ""  # e.g., "market_data", "psychology", "competitive", "contrarian"
    priority: int = 1  # 1 = highest


@dataclass
class ResearchResult:
    """Complete result from a research run."""
    query: str
    depth: str
    findings: List[ResearchFinding] = field(default_factory=list)
    sub_questions: List[ResearchSubQuestion] = field(default_factory=list)
    contradictions: List[Dict[str, str]] = field(default_factory=list)
    synthesis: str = ""
    source_count: int = 0
    unique_domains: int = 0
    duration_seconds: float = 0
    estimated_cost: float = 0
    quality_score: Dict[str, Any] = field(default_factory=dict)
    raw_search_results: List[Dict] = field(default_factory=list)
    timestamp: str = ""

    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now(timezone.utc).isoformat()

    def to_markdown(self) -> str:
        """Render the research result as structured markdown."""
        lines = []
        lines.append(f"# Research Report: {self.query}")
        lines.append(f"")
        lines.append(f"**Depth**: {self.depth} | **Sources**: {self.source_count} | "
                     f"**Unique domains**: {self.unique_domains} | "
                     f"**Duration**: {self.duration_seconds:.1f}s | "
                     f"**Est. cost**: ${self.estimated_cost:.2f}")
        lines.append(f"**Timestamp**: {self.timestamp}")
        lines.append("")

        # Quality score
        if self.quality_score:
            lines.append("## Research Quality")
            for key, val in self.quality_score.items():
                lines.append(f"- **{key}**: {val}")
            lines.append("")

        # Synthesis
        if self.synthesis:
            lines.append("## Synthesis")
            lines.append(self.synthesis)
            lines.append("")

        # Findings by type
        if self.findings:
            lines.append("## Key Findings")
            lines.append("")

            # Group by type
            by_type: Dict[str, List[ResearchFinding]] = {}
            for f in self.findings:
                by_type.setdefault(f.finding_type, []).append(f)

            for ftype, group in by_type.items():
                lines.append(f"### {ftype.replace('_', ' ').title()}")
                for f in group:
                    confidence_icon = {"high": "🟢", "medium": "🟡", "low": "🔴"}.get(
                        f.confidence, "⚪"
                    )
                    lines.append(f"- {confidence_icon} **{f.claim}**")
                    lines.append(f"  - Source: [{f.source_domain}]({f.source_url})")
                    if f.excerpt:
                        lines.append(f'  - Excerpt: "{f.excerpt[:200]}..."')
                    if f.recency:
                        lines.append(f"  - Date: {f.recency}")
                lines.append("")

        # Contradictions
        if self.contradictions:
            lines.append("## Contradictions & Conflicts")
            for c in self.contradictions:
                lines.append(f"- **{c.get('topic', 'Unknown')}**: "
                            f"{c.get('claim_a', '?')} vs {c.get('claim_b', '?')}")
                if c.get("resolution"):
                    lines.append(f"  - Resolution: {c['resolution']}")
            lines.append("")

        # Source appendix
        if self.findings:
            lines.append("## Source Appendix")
            seen_urls = set()
            for f in self.findings:
                if f.source_url and f.source_url not in seen_urls:
                    seen_urls.add(f.source_url)
                    lines.append(f"- [{f.source_domain}]({f.source_url}) "
                                f"— {f.source_title or 'Untitled'}")
            lines.append("")

        return "\n".join(lines)

    def save(self, path: Optional[Path] = None) -> Path:
        """Save the research result to a markdown file."""
        if path is None:
            TMP_DIR.mkdir(parents=True, exist_ok=True)
            slug = re.sub(r"[^a-z0-9]+", "-", self.query.lower())[:50]
            path = TMP_DIR / f"{self.depth}-{slug}.md"
        path.write_text(self.to_markdown())
        return path


# ---------------------------------------------------------------------------
# Query Decomposition (for Swarm Mode)
# ---------------------------------------------------------------------------

# Default decomposition templates by research intent
DECOMPOSITION_TEMPLATES = {
    "market": [
        ResearchSubQuestion(
            question="What is the current market size, growth rate, and key trends?",
            search_queries=[
                "{topic} market size 2025 2026",
                "{topic} industry growth rate forecast",
                "{topic} market trends report",
            ],
            angle="market_data",
            priority=1,
        ),
        ResearchSubQuestion(
            question="Who are the key players and what are their strategies?",
            search_queries=[
                "{topic} top companies competitors",
                "{topic} market leaders strategy",
                "{topic} competitive landscape analysis",
            ],
            angle="competitive",
            priority=1,
        ),
        ResearchSubQuestion(
            question="What are the real customer pain points and buying triggers?",
            search_queries=[
                "{topic} customer complaints reddit",
                "{topic} buyer frustrations reviews",
                "{topic} why people buy testimonials",
            ],
            angle="psychology",
            priority=1,
        ),
        ResearchSubQuestion(
            question="What are the biggest risks, failures, and contrarian views?",
            search_queries=[
                "{topic} failures mistakes lessons",
                "{topic} criticism problems risks",
                "{topic} why it doesn't work",
            ],
            angle="contrarian",
            priority=2,
        ),
        ResearchSubQuestion(
            question="What pricing models and revenue strategies are working?",
            search_queries=[
                "{topic} pricing models how much charge",
                "{topic} revenue model business model",
                "{topic} pricing strategy examples",
            ],
            angle="market_data",
            priority=2,
        ),
    ],
    "audience": [
        ResearchSubQuestion(
            question="Who is this audience and what do they care about?",
            search_queries=[
                "{topic} psychographics interests values",
                "{topic} demographics profile",
                "{topic} what they want need",
            ],
            angle="psychology",
            priority=1,
        ),
        ResearchSubQuestion(
            question="What language do they use to describe their problems?",
            search_queries=[
                "{topic} reddit complaints frustrations",
                "{topic} forum discussions real talk",
                "{topic} reviews what people say",
            ],
            angle="psychology",
            priority=1,
        ),
        ResearchSubQuestion(
            question="Where do they spend time and money online?",
            search_queries=[
                "{topic} communities forums groups",
                "{topic} where to find audience",
                "{topic} spending habits platforms",
            ],
            angle="market_data",
            priority=1,
        ),
        ResearchSubQuestion(
            question="What existing solutions are they using and what gaps exist?",
            search_queries=[
                "{topic} alternatives solutions tools",
                "{topic} what's missing gaps underserved",
                "{topic} product comparisons best options",
            ],
            angle="competitive",
            priority=2,
        ),
    ],
    "general": [
        ResearchSubQuestion(
            question="What are the core facts and current state of this topic?",
            search_queries=[
                "{topic} overview 2025",
                "{topic} current state analysis",
                "{topic} key facts data",
            ],
            angle="market_data",
            priority=1,
        ),
        ResearchSubQuestion(
            question="What do experts and practitioners say about this?",
            search_queries=[
                "{topic} expert opinions analysis",
                "{topic} practitioner insights experience",
                "{topic} best practices recommendations",
            ],
            angle="psychology",
            priority=1,
        ),
        ResearchSubQuestion(
            question="What are the risks, downsides, or contrarian perspectives?",
            search_queries=[
                "{topic} risks downsides problems",
                "{topic} criticism contrarian view",
                "{topic} what could go wrong",
            ],
            angle="contrarian",
            priority=2,
        ),
        ResearchSubQuestion(
            question="What are specific examples, case studies, or data points?",
            search_queries=[
                "{topic} case study example results",
                "{topic} statistics data numbers",
                "{topic} success stories real examples",
            ],
            angle="market_data",
            priority=2,
        ),
    ],
}


def detect_research_intent(query: str) -> str:
    """Classify the research intent to pick the right decomposition template."""
    query_lower = query.lower()

    market_signals = ["market", "industry", "compete", "pricing", "monetize",
                      "revenue", "business model", "launch", "enter", "opportunity",
                      "niche", "sell", "offer", "product"]
    audience_signals = ["audience", "avatar", "customer", "buyer", "who",
                        "psychograph", "pain point", "frustration", "language",
                        "icp", "persona", "target"]

    market_score = sum(1 for s in market_signals if s in query_lower)
    audience_score = sum(1 for s in audience_signals if s in query_lower)

    if audience_score > market_score:
        return "audience"
    elif market_score > 0:
        return "market"
    return "general"


def decompose_query(query: str, intent: Optional[str] = None) -> List[ResearchSubQuestion]:
    """Decompose a research question into parallel sub-questions with search queries."""
    if intent is None:
        intent = detect_research_intent(query)

    template = DECOMPOSITION_TEMPLATES.get(intent, DECOMPOSITION_TEMPLATES["general"])

    # Fill in the topic
    result = []
    for sq in template:
        filled = ResearchSubQuestion(
            question=sq.question,
            search_queries=[q.format(topic=query) for q in sq.search_queries],
            angle=sq.angle,
            priority=sq.priority,
        )
        result.append(filled)

    return result


# ---------------------------------------------------------------------------
# Research Engine
# ---------------------------------------------------------------------------

class ResearchEngine:
    """
    Universal research engine with depth-controlled grounding.

    Uses search_web + read_url_content for free research,
    perplexity_client for premium research when budget allows,
    deep_research_client (Gemini) for max-tier research when Ultra-linked.
    """

    def __init__(self):
        self.perplexity_client = None
        self.deep_research_client = None
        # Provenance integrity: claims that arrive with no real source URL are
        # quarantined here and DROPPED from findings — never persisted with an
        # empty source_url. The dispatcher surfaces the count as a warning.
        self._quarantine: List[dict] = []
        self._init_perplexity()
        self._init_deep_research()

    def _init_perplexity(self):
        """Try to initialize the Perplexity client. Fails gracefully."""
        try:
            from perplexity_client import PerplexityClient
            self.perplexity_client = PerplexityClient()
        except Exception:
            self.perplexity_client = None

    def _init_deep_research(self):
        """Try to initialize the Gemini Deep Research client. Fails gracefully.

        Requires GOOGLE_AI_STUDIO_KEY (Ultra-linked AI Studio key).
        See directives/google-api-usage-policy.md.
        """
        try:
            from deep_research_client import DeepResearchClient
            self.deep_research_client = DeepResearchClient()
        except Exception:
            self.deep_research_client = None

    # ----- Public API -----

    def research(self, query: str, depth: str = "standard",
                 save_output: bool = True) -> ResearchResult:
        """
        Run a grounded research query at the specified depth.

        Args:
            query: The research question.
            depth: "quick", "standard", or "deep".
            save_output: Whether to save the result to .tmp/research/.

        Returns:
            ResearchResult with all findings, sources, and synthesis.
        """
        start = time.monotonic()

        if depth == "quick":
            result = self._research_quick(query)
        elif depth == "standard":
            result = self._research_standard(query)
        elif depth == "deep":
            result = self._research_deep(query)
        elif depth == "max":
            result = self._research_max(query)
        else:
            raise ValueError(f"Unknown depth: {depth}. Use 'quick', 'standard', 'deep', or 'max'.")

        result.duration_seconds = round(time.monotonic() - start, 2)
        result.quality_score = self._score_quality(result)

        if save_output:
            path = result.save()
            print(f"  📄 Research saved to: {path}")

        return result

    def decompose(self, query: str, intent: Optional[str] = None) -> List[ResearchSubQuestion]:
        """
        Decompose a query for swarm-mode parallel research.

        Returns sub-questions with pre-built search queries that agents
        can fire in parallel. This is the free-tier orchestration layer
        that gives Manus/Kimi-style wide research without API costs.
        """
        return decompose_query(query, intent)

    def decompose_to_markdown(self, query: str, intent: Optional[str] = None) -> str:
        """Decompose and return as markdown for agent handoff."""
        sqs = self.decompose(query, intent)
        lines = [
            f"# Research Decomposition: {query}",
            f"",
            f"**Intent**: {intent or detect_research_intent(query)}",
            f"**Sub-questions**: {len(sqs)}",
            f"",
            "Each agent should execute the search queries for their assigned sub-question,",
            "read the top 2-3 results in full, and produce findings with source URLs.",
            "",
        ]
        for i, sq in enumerate(sqs, 1):
            lines.append(f"## Sub-Question {i} (Priority: {sq.priority}, Angle: {sq.angle})")
            lines.append(f"**Question**: {sq.question}")
            lines.append(f"**Search queries**:")
            for q in sq.search_queries:
                lines.append(f"- `{q}`")
            lines.append("")
        return "\n".join(lines)

    # ----- Depth Implementations -----

    def _research_quick(self, query: str) -> ResearchResult:
        """Quick research: 3-5 web searches, extract key findings. Free."""
        print(f"  🔍 Quick research: {query}")

        result = ResearchResult(query=query, depth="quick")

        # Generate search queries
        search_queries = self._generate_search_queries(query, count=4)

        # Execute searches via Perplexity MCP (sonar = cheap) or web search
        all_findings = []
        for sq in search_queries:
            findings = self._search_and_extract(sq)
            all_findings.extend(findings)

        result.findings = self._deduplicate_findings(all_findings)
        result.source_count = len(result.findings)
        result.unique_domains = len(set(f.source_domain for f in result.findings))
        result.synthesis = self._quick_synthesize(query, result.findings)
        result.estimated_cost = 0.0  # Free tier

        return result

    def _research_standard(self, query: str) -> ResearchResult:
        """Standard research: wide search + read top pages + synthesis. ~$0.04."""
        print(f"  🔬 Standard research: {query}")

        result = ResearchResult(query=query, depth="standard")

        # Decompose into sub-questions for wider coverage
        sub_questions = self.decompose(query)
        result.sub_questions = sub_questions

        # Phase 1: Wide search across all sub-questions
        all_findings = []
        all_urls = []
        for sq in sub_questions:
            for search_query in sq.search_queries:
                findings = self._search_and_extract(search_query, angle=sq.angle)
                for f in findings:
                    f.finding_type = self._classify_finding_type(f, sq.angle)
                all_findings.extend(findings)
                all_urls.extend(f.source_url for f in findings if f.source_url)

        # Phase 2: Read top pages for depth (pick best 3-5 URLs)
        top_urls = self._rank_urls(all_urls, max_count=4)
        for url in top_urls:
            deep_findings = self._read_page_and_extract(url, query)
            all_findings.extend(deep_findings)

        # Phase 3: Perplexity synthesis (if available, otherwise local)
        result.findings = self._deduplicate_findings(all_findings)
        result.contradictions = self._detect_contradictions(result.findings)
        result.source_count = len(result.findings)
        result.unique_domains = len(set(f.source_domain for f in result.findings))

        if self.perplexity_client:
            result.synthesis = self._perplexity_synthesize(query, result.findings)
            result.estimated_cost = 0.04
        else:
            result.synthesis = self._quick_synthesize(query, result.findings)
            result.estimated_cost = 0.0

        return result

    def _research_deep(self, query: str) -> ResearchResult:
        """Deep research: sonar-deep-research + wide search + full reads. ~$0.50-0.75."""
        print(f"  🧠 Deep research: {query}")

        result = ResearchResult(query=query, depth="deep")

        # Phase 1: Perplexity Deep Research (the premium foundation)
        deep_findings = []
        deep_cost = 0.0

        if self.perplexity_client:
            try:
                remaining = self.perplexity_client.budget_remaining()
                if remaining >= 1.00:
                    # Core deep research query
                    core_result = self.perplexity_client.search(
                        f"Comprehensive analysis of {query}: market data, key players, "
                        f"trends, real examples with specific numbers. Include recent data "
                        f"from 2025-2026 where available.",
                        model="sonar-deep-research",
                        task_context="deep-research-engine",
                        query_type="research",
                    )
                    deep_findings.extend(
                        self._parse_perplexity_response(core_result.text, core_result.citations)
                    )
                    deep_cost += core_result.estimated_cost

                    # Psychology deep research query
                    if remaining >= 1.50:
                        psych_result = self.perplexity_client.search(
                            f"What are the real psychological drivers, frustrations, "
                            f"and aspirations related to {query}? What do real people "
                            f"say on Reddit, forums, and reviews? Include verbatim quotes.",
                            model="sonar-deep-research",
                            task_context="deep-research-engine",
                            query_type="social_listening",
                        )
                        psych_findings = self._parse_perplexity_response(
                            psych_result.text, psych_result.citations
                        )
                        for f in psych_findings:
                            f.finding_type = "quote" if '"' in f.claim else "opinion"
                        deep_findings.extend(psych_findings)
                        deep_cost += psych_result.estimated_cost
                else:
                    print("  ⚠️  Perplexity budget low — running deep with free tools only")
            except Exception as e:
                print(f"  ⚠️  Perplexity error: {e} — falling back to free tools")

        # Phase 2: Wide search (same as standard but more volume)
        sub_questions = self.decompose(query)
        result.sub_questions = sub_questions

        all_findings = list(deep_findings)
        all_urls = []

        for sq in sub_questions:
            for search_query in sq.search_queries:
                findings = self._search_and_extract(search_query, angle=sq.angle)
                for f in findings:
                    f.finding_type = self._classify_finding_type(f, sq.angle)
                all_findings.extend(findings)
                all_urls.extend(f.source_url for f in findings if f.source_url)

        # Phase 3: Read top pages (more than standard)
        top_urls = self._rank_urls(all_urls, max_count=6)
        for url in top_urls:
            page_findings = self._read_page_and_extract(url, query)
            all_findings.extend(page_findings)

        # Phase 4: Synthesize everything
        result.findings = self._deduplicate_findings(all_findings)
        result.contradictions = self._detect_contradictions(result.findings)
        result.source_count = len(result.findings)
        result.unique_domains = len(set(f.source_domain for f in result.findings))
        result.estimated_cost = deep_cost

        if self.perplexity_client and deep_cost > 0:
            result.synthesis = self._perplexity_synthesize(query, result.findings)
            result.estimated_cost += 0.02
        else:
            result.synthesis = self._quick_synthesize(query, result.findings)

        return result

    def _research_max(self, query: str) -> ResearchResult:
        """Max research: Gemini Deep Research Max + fallback to _research_deep if unavailable.

        Uses the Interactions API — autonomous multi-step research with Google Search
        grounding, URL Context, and synthesis. Highest accuracy tier (93.3% DeepSearchQA).

        Billing: Ultra subscription should cover most calls at $0. Prepaid $10 ceiling
        prevents any overspend. See directives/google-api-usage-policy.md.
        """
        print(f"  🚀 Max research (Gemini Deep Research Max): {query}")

        result = ResearchResult(query=query, depth="max")

        # Guardrail: if Deep Research client didn't initialize, fall back to deep
        if self.deep_research_client is None:
            print("  ⚠️  Deep Research client unavailable. Falling back to _research_deep (Perplexity).")
            fallback = self._research_deep(query)
            fallback.depth = "max (fallback → deep)"
            return fallback

        # Attempt Deep Research Max
        try:
            dr_result = self.deep_research_client.research(
                query,
                mode="max",
                task_context="research-engine-max",
                query_type="research",
            )
        except Exception as e:
            # Any error from Deep Research → graceful fallback, tagged
            print(f"  ⚠️  Deep Research Max failed: {e}. Falling back to _research_deep.")
            fallback = self._research_deep(query)
            fallback.depth = "max (fallback → deep)"
            return fallback

        # Parse Deep Research output into ResearchFindings
        findings = self._parse_deep_research_response(
            dr_result.text, dr_result.citations
        )

        # Optional: supplement with the existing wide-search layer for extra coverage
        sub_questions = self.decompose(query)
        result.sub_questions = sub_questions

        result.findings = self._deduplicate_findings(findings)
        result.contradictions = self._detect_contradictions(result.findings)
        result.source_count = len(result.findings)
        result.unique_domains = len(set(f.source_domain for f in result.findings))
        result.synthesis = dr_result.text
        result.estimated_cost = dr_result.estimated_cost

        return result

    def _parse_deep_research_response(
        self, text: str, citations: List[str]
    ) -> List[ResearchFinding]:
        """Parse a Deep Research Interactions API response into ResearchFindings.

        Deep Research returns a long synthesized report with embedded citations.
        We split by paragraph and attach citations using the same pattern as
        _parse_perplexity_response.
        """
        findings = []
        paragraphs = [p.strip() for p in text.split("\n") if p.strip() and len(p.strip()) > 30]

        for i, para in enumerate(paragraphs):
            # Match numeric citations like [1], [2]
            citation_idx = None
            citation_match = re.search(r"\[(\d+)\]", para)
            if citation_match:
                idx = int(citation_match.group(1)) - 1
                if 0 <= idx < len(citations):
                    citation_idx = idx

            if citation_idx is not None:
                source_url = citations[citation_idx]
            elif citations:
                source_url = citations[min(i, len(citations) - 1)]
            else:
                source_url = ""

            cleaned_claim = re.sub(r"\[\d+\]", "", para).strip()

            # Provenance integrity: a finding with no real source is NOT a finding.
            # Quarantine it (visible) and drop it — never persist source_url="".
            if not source_url:
                self._quarantine.append({"claim": cleaned_claim, "reason": "no_source_url"})
                continue

            confidence = "high" if citation_idx is not None else "medium"
            finding_type = "data"
            if '"' in para:
                finding_type = "quote"
            elif any(c in para for c in ["$", "%", "billion", "million"]):
                finding_type = "statistic"

            findings.append(ResearchFinding(
                claim=cleaned_claim,
                source_url=source_url,
                excerpt=para[:300],
                confidence=confidence,
                finding_type=finding_type,
            ))

        return findings

    # ----- Internal: Search & Extract -----

    def _generate_search_queries(self, query: str, count: int = 4) -> List[str]:
        """Generate varied search queries from a single question."""
        queries = [query]

        # Add date-specific variant
        year = datetime.now().year
        if str(year) not in query:
            queries.append(f"{query} {year}")

        # Add data-seeking variant
        queries.append(f"{query} statistics data report")

        # Add real-people variant
        queries.append(f"{query} reddit forum discussion")

        return queries[:count]

    def _search_and_extract(self, search_query: str, angle: str = "") -> List[ResearchFinding]:
        """
        Execute a web search and extract findings.

        NOTE: This method is designed to be called by the workflow orchestrator
        which has access to search_web and read_url_content tools. When run
        standalone via CLI, it uses the Perplexity API as the search backend.
        """
        findings = []

        if self.perplexity_client:
            # Use angle-specific task context to avoid hitting per-task cap
            task_ctx = f"research-engine-{angle}" if angle else "research-engine"
            try:
                result = self.perplexity_client.search(
                    search_query,
                    model="sonar",
                    task_context=task_ctx,
                    query_type="research",
                    max_tokens=2048,
                )
                findings = self._parse_perplexity_response(result.text, result.citations)
            except Exception as e:
                error_msg = str(e)
                if "401" in error_msg or "unauthorized" in error_msg.lower():
                    # Dead/expired key: latch off for the whole run instead of
                    # 401-spamming every sub-query (2026-07-08: 12 x 401 per
                    # topic before this latch existed).
                    print("  ⚠️  Perplexity auth failed (401) — disabling for this run, "
                          "falling back to Tavily floor")
                    self.perplexity_client = None
                elif "cap reached" in error_msg.lower() or "budget" in error_msg.lower():
                    print(f"  ℹ️  Perplexity cap/budget hit for angle '{angle}'. Skipping: {search_query[:50]}...")
                else:
                    print(f"  ⚠️  Search failed for '{search_query[:50]}...': {e}")

        # $0 Tavily floor — fires when Perplexity is absent, latched off, or
        # returned nothing. Same leg world_brief.py trusts (native_floor).
        if not findings:
            findings = self._tavily_search_findings(search_query)
        if not findings and not self.perplexity_client:
            print(f"  ℹ️  No search backend produced results for: {search_query[:60]}...")

        return findings

    def _tavily_search_findings(self, search_query: str) -> List[ResearchFinding]:
        """Tavily-backed search leg (free tier). Returns [] on any failure —
        mirrors native_floor.tavily_search's never-raise contract."""
        try:
            from native_floor import tavily_search
        except ImportError:
            return []
        findings = []
        for r in tavily_search(search_query, max_results=5):
            url = (r.get("url") or "").strip()
            content = re.sub(r"\s+", " ", (r.get("content") or "")).strip()
            title = re.sub(r"\s+", " ", (r.get("title") or "")).strip()
            if not url or not content:
                continue  # unsourced result never becomes a finding
            # Title as the claim: raw Tavily page content often opens with
            # nav junk ("Skip to content...") that would otherwise become
            # the item headline downstream.
            findings.append(ResearchFinding(
                claim=title if title else content[:200],
                source_url=url,
                source_title=title,
                excerpt=content[:300],
                confidence="medium",
                finding_type="data",
            ))
        return findings

    def _read_page_and_extract(self, url: str, query: str) -> List[ResearchFinding]:
        """
        Read a full page and extract relevant findings.

        NOTE: In workflow mode, the orchestrator calls read_url_content.
        In CLI mode, we use requests + basic extraction.
        """
        findings = []
        try:
            response = requests.get(url, timeout=15, headers={
                "User-Agent": "Mozilla/5.0 (Research Bot)"
            })
            if response.status_code == 200:
                # Basic extraction — in workflow mode, read_url_content does HTML→markdown
                text = response.text[:5000]
                # Extract title
                title_match = re.search(r"<title>(.*?)</title>", text, re.IGNORECASE)
                title = title_match.group(1) if title_match else ""

                findings.append(ResearchFinding(
                    claim=f"Page content from {urlparse(url).netloc}",
                    source_url=url,
                    source_title=title,
                    excerpt=text[:300],
                    confidence="medium",
                    finding_type="data",
                ))
        except Exception as e:
            print(f"  ⚠️  Failed to read {url}: {e}")

        return findings

    def _parse_perplexity_response(self, text: str, citations: List[str]) -> List[ResearchFinding]:
        """Parse a Perplexity API response into structured findings."""
        findings = []

        # Split text into paragraphs/sentences for individual findings
        paragraphs = [p.strip() for p in text.split("\n") if p.strip() and len(p.strip()) > 20]

        for i, para in enumerate(paragraphs):
            # Match citation to paragraph (Perplexity uses [1], [2] etc.)
            citation_idx = None
            citation_match = re.search(r"\[(\d+)\]", para)
            if citation_match:
                idx = int(citation_match.group(1)) - 1
                if 0 <= idx < len(citations):
                    citation_idx = idx

            if citation_idx is not None:
                source_url = citations[citation_idx]
            elif citations:
                source_url = citations[min(i, len(citations) - 1)]
            else:
                source_url = ""

            cleaned_claim = re.sub(r"\[\d+\]", "", para).strip()

            # Provenance integrity: drop URL-less claims into quarantine instead
            # of persisting a finding with an empty source_url.
            if not source_url:
                self._quarantine.append({"claim": cleaned_claim, "reason": "no_source_url"})
                continue

            # Determine confidence
            confidence = "high" if citation_idx is not None else "medium"
            if any(word in para.lower() for word in ["estimated", "approximately", "roughly"]):
                confidence = "medium"
            if any(word in para.lower() for word in ["unclear", "debated", "uncertain"]):
                confidence = "low"

            # Detect finding type
            finding_type = "data"
            if '"' in para:
                finding_type = "quote"
            elif any(c in para for c in ["$", "%", "billion", "million"]):
                finding_type = "statistic"

            findings.append(ResearchFinding(
                claim=cleaned_claim,
                source_url=source_url,
                excerpt=para[:200],
                confidence=confidence,
                finding_type=finding_type,
            ))

        return findings

    # ----- Internal: Quality & Synthesis -----

    def _deduplicate_findings(self, findings: List[ResearchFinding]) -> List[ResearchFinding]:
        """Remove near-duplicate findings, keeping the one with better provenance."""
        seen_claims = {}
        unique = []

        for f in findings:
            # Simple dedup key: first 50 chars of claim
            key = f.claim[:50].lower().strip()
            if key in seen_claims:
                # Keep the one with higher confidence
                existing = seen_claims[key]
                if f.confidence == "high" and existing.confidence != "high":
                    unique[unique.index(existing)] = f
                    seen_claims[key] = f
            else:
                seen_claims[key] = f
                unique.append(f)

        return unique

    def _detect_contradictions(self, findings: List[ResearchFinding]) -> List[Dict[str, str]]:
        """Detect findings that may contradict each other."""
        contradictions = []

        # Look for numeric contradictions (e.g., different market size numbers)
        numeric_findings = [
            f for f in findings
            if any(c in f.claim for c in ["$", "%", "billion", "million"])
        ]

        for i, f1 in enumerate(numeric_findings):
            for f2 in numeric_findings[i + 1:]:
                # Very basic: if they talk about similar things but have different numbers
                words1 = set(f1.claim.lower().split())
                words2 = set(f2.claim.lower().split())
                overlap = words1 & words2
                if len(overlap) > 3 and f1.source_domain != f2.source_domain:
                    contradictions.append({
                        "topic": " ".join(list(overlap)[:5]),
                        "claim_a": f"{f1.claim[:80]}... ({f1.source_domain})",
                        "claim_b": f"{f2.claim[:80]}... ({f2.source_domain})",
                        "resolution": "Needs triangulation — check sources directly",
                    })

        return contradictions[:5]  # Cap at 5 most notable

    def _classify_finding_type(self, finding: ResearchFinding, angle: str) -> str:
        """Classify a finding based on content and research angle."""
        claim_lower = finding.claim.lower()

        if '"' in finding.claim or "said" in claim_lower:
            return "quote"
        if any(c in finding.claim for c in ["$", "%", "billion", "million"]):
            return "statistic"
        if "case study" in claim_lower or "example" in claim_lower:
            return "case_study"
        if angle == "psychology":
            return "opinion"
        return "data"

    def _quick_synthesize(self, query: str, findings: List[ResearchFinding]) -> str:
        """Generate a quick synthesis without API calls."""
        if not findings:
            return "No findings gathered. Research may need to be run with a higher depth level."

        high_conf = [f for f in findings if f.confidence == "high"]
        stats = [f for f in findings if f.finding_type == "statistic"]
        sources = len(set(f.source_domain for f in findings))

        lines = [
            f"Based on {len(findings)} findings across {sources} sources:",
            "",
        ]

        if high_conf:
            lines.append("**High-confidence findings:**")
            for f in high_conf[:5]:
                lines.append(f"- {f.claim[:150]}")
            lines.append("")

        if stats:
            lines.append("**Key statistics:**")
            for f in stats[:5]:
                lines.append(f"- {f.claim[:150]} (Source: {f.source_domain})")
            lines.append("")

        return "\n".join(lines)

    def _perplexity_synthesize(self, query: str, findings: List[ResearchFinding]) -> str:
        """Use Perplexity sonar for synthesis of findings."""
        if not self.perplexity_client or not findings:
            return self._quick_synthesize(query, findings)

        # Build a synthesis prompt from findings
        findings_text = "\n".join(
            f"- {f.claim[:200]} (Source: {f.source_domain}, Confidence: {f.confidence})"
            for f in findings[:20]
        )

        try:
            result = self.perplexity_client.search(
                f"Based on these research findings, provide a clear synthesis answering: "
                f"{query}\n\nFindings:\n{findings_text}",
                model="sonar",
                task_context="research-engine-synthesis",
                query_type="research",
                max_tokens=1500,
            )
            return result.text
        except Exception:
            return self._quick_synthesize(query, findings)

    def _rank_urls(self, urls: List[str], max_count: int = 5) -> List[str]:
        """Rank URLs by relevance signals and return top N unique."""
        # Deduplicate
        seen = set()
        unique = []
        for url in urls:
            if url and url not in seen:
                seen.add(url)
                unique.append(url)

        # Score by domain authority signals
        scored = []
        for url in unique:
            domain = urlparse(url).netloc.lower()
            score = 0

            # Prefer primary sources
            high_quality = [
                "reddit.com", "quora.com",  # Real people
                "statista.com", "ibisworld.com",  # Market data
                "hbr.org", "mckinsey.com", "bcg.com",  # Business insight
                "arxiv.org", "scholar.google.com",  # Academic
            ]
            medium_quality = [
                "forbes.com", "bloomberg.com", "techcrunch.com",
                "medium.com", "substack.com",
            ]

            if any(d in domain for d in high_quality):
                score += 3
            elif any(d in domain for d in medium_quality):
                score += 2
            else:
                score += 1

            # Penalize aggregators
            low_quality = ["pinterest.com", "facebook.com", "twitter.com", "instagram.com"]
            if any(d in domain for d in low_quality):
                score -= 2

            scored.append((url, score))

        scored.sort(key=lambda x: x[1], reverse=True)
        return [url for url, _ in scored[:max_count]]

    def _score_quality(self, result: ResearchResult) -> Dict[str, Any]:
        """Score the quality of a research result."""
        score = {}

        # Source count
        if result.depth == "quick":
            min_sources = 3
        elif result.depth == "standard":
            min_sources = 8
        else:
            min_sources = 15

        score["source_count"] = f"{result.source_count}/{min_sources} minimum"
        score["source_count_pass"] = result.source_count >= min_sources

        # Domain diversity
        score["unique_domains"] = result.unique_domains
        score["domain_diversity_pass"] = result.unique_domains >= 3

        # Provenance (% of findings with URLs)
        with_urls = sum(1 for f in result.findings if f.source_url)
        total = len(result.findings) or 1
        pct = round(with_urls / total * 100)
        score["provenance"] = f"{pct}% of findings have source URLs"
        score["provenance_pass"] = pct >= 80

        # High confidence ratio
        high_conf = sum(1 for f in result.findings if f.confidence == "high")
        ratio = round(high_conf / total * 100) if total else 0
        score["high_confidence_ratio"] = f"{ratio}%"

        # Contradiction detection
        score["contradictions_found"] = len(result.contradictions)

        # Overall pass/fail
        passes = sum(1 for k, v in score.items() if k.endswith("_pass") and v)
        total_checks = sum(1 for k in score if k.endswith("_pass"))
        score["overall"] = f"{passes}/{total_checks} checks passed"

        return score


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Deep Research Engine — grounded research for Antigravity workflows"
    )
    parser.add_argument("query", help="The research question")
    parser.add_argument(
        "--depth", choices=["quick", "standard", "deep", "max"], default="standard",
        help="Research depth level (default: standard). 'max' uses Gemini Deep Research Max."
    )
    parser.add_argument(
        "--decompose-only", action="store_true",
        help="Only decompose the query into sub-questions (for swarm mode)"
    )
    parser.add_argument(
        "--intent", choices=["market", "audience", "general"],
        help="Override auto-detected research intent"
    )

    args = parser.parse_args()
    load_env()

    engine = ResearchEngine()

    if args.decompose_only:
        print(engine.decompose_to_markdown(args.query, args.intent))
    else:
        result = engine.research(args.query, depth=args.depth)
        print(result.to_markdown())


if __name__ == "__main__":
    main()
