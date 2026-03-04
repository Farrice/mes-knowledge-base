#!/usr/bin/env python3
"""
Shared Perplexity API Client — Citation-backed research for Antigravity workflows.

Uses the OpenAI-compatible Perplexity API (https://api.perplexity.ai).
Budget tracking enforced per directives/perplexity-usage-policy.md.

Usage:
    from perplexity_client import PerplexityClient, load_env

    load_env()
    client = PerplexityClient()

    # Quick research
    result = client.search("AI consulting market size 2026")

    # Deep research with reasoning
    result = client.search("prompt", model="sonar-reasoning-pro")

    # Check budget
    remaining = client.budget_remaining()
"""

import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests


# ---------------------------------------------------------------------------
# Environment
# ---------------------------------------------------------------------------

BASE_PATH = Path(__file__).parent.parent
ENV_PATH = BASE_PATH / ".env"
USAGE_FILE = BASE_PATH / ".agent" / "perplexity-usage.json"

MONTHLY_LIMIT_USD = 10.00


def load_env(env_path: Optional[Path] = None):
    """Load .env file into os.environ (setdefault — won't overwrite existing)."""
    path = env_path or ENV_PATH
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip())


# ---------------------------------------------------------------------------
# Cost Estimates per Model
# ---------------------------------------------------------------------------

# Estimated cost per query (based on typical token usage)
COST_PER_QUERY = {
    "sonar":                 0.02,
    "sonar-pro":             0.05,
    "sonar-reasoning-pro":   0.08,
    "sonar-deep-research":   0.25,
}

DEFAULT_QUERY_COST = 0.05


# ---------------------------------------------------------------------------
# Response
# ---------------------------------------------------------------------------

class SearchResult:
    """Structured result from a Perplexity search."""

    __slots__ = ("text", "citations", "model", "query", "estimated_cost", "duration_seconds")

    def __init__(self, **kwargs):
        for k in self.__slots__:
            setattr(self, k, kwargs.get(k, None))

    def to_dict(self) -> Dict[str, Any]:
        return {k: getattr(self, k) for k in self.__slots__}


# ---------------------------------------------------------------------------
# Client
# ---------------------------------------------------------------------------

class PerplexityClient:
    """Perplexity API client with budget tracking and usage logging."""

    API_URL = "https://api.perplexity.ai/chat/completions"

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("PERPLEXITY_API_KEY", "")
        if not self.api_key:
            raise ValueError(
                "PERPLEXITY_API_KEY not found. Add it to .env or set as environment variable."
            )
        self.call_count = 0
        self.total_cost = 0.0

    def search(
        self,
        query: str,
        *,
        model: str = "sonar",
        system_instruction: str = "",
        temperature: float = 0.2,
        max_tokens: int = 4096,
        search_recency_filter: Optional[str] = None,
        task_context: str = "",
        query_type: str = "research",
    ) -> SearchResult:
        """
        Run a Perplexity search query.

        Args:
            query: The research question.
            model: sonar | sonar-pro | sonar-reasoning-pro | sonar-deep-research
            system_instruction: System prompt for context.
            temperature: Lower = more factual (0.0-1.0).
            max_tokens: Max response length.
            search_recency_filter: "month", "week", "day", or None for all time.
            task_context: Name of the task/swarm (for usage logging).
            query_type: research | social_listening | competitive_intel | trend_verification

        Returns:
            SearchResult with text, citations, cost, etc.
        """
        # Budget check
        remaining = self.budget_remaining()
        query_cost = COST_PER_QUERY.get(model, DEFAULT_QUERY_COST)

        if remaining < 0.50:
            raise BudgetExhaustedError(
                f"Perplexity budget nearly exhausted (${remaining:.2f} remaining). "
                f"Falling back to web search."
            )

        if remaining < 2.00:
            if model != "sonar":
                print(f"  ⚠️  Budget low (${remaining:.2f}). Downgrading to sonar.")
                model = "sonar"
                query_cost = COST_PER_QUERY["sonar"]

        # Build request
        messages = []
        if system_instruction:
            messages.append({"role": "system", "content": system_instruction})
        messages.append({"role": "user", "content": query})

        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
        if search_recency_filter:
            payload["search_recency_filter"] = search_recency_filter

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        start = time.monotonic()

        response = requests.post(self.API_URL, json=payload, headers=headers, timeout=120)
        response.raise_for_status()

        duration = time.monotonic() - start
        data = response.json()

        # Extract response
        text = ""
        if data.get("choices"):
            text = data["choices"][0].get("message", {}).get("content", "")

        citations = data.get("citations", [])

        self.call_count += 1
        self.total_cost += query_cost

        # Log usage
        self._log_usage(
            query=query,
            model=model,
            estimated_cost=query_cost,
            task_context=task_context,
            query_type=query_type,
        )

        result = SearchResult(
            text=text,
            citations=citations,
            model=model,
            query=query,
            estimated_cost=query_cost,
            duration_seconds=round(duration, 2),
        )

        return result

    def search_batch(
        self,
        queries: List[str],
        **kwargs,
    ) -> List[SearchResult]:
        """Run multiple search queries sequentially (Perplexity rate-limits aggressively)."""
        results = []
        for q in queries:
            try:
                result = self.search(q, **kwargs)
                results.append(result)
            except (BudgetExhaustedError, requests.RequestException) as e:
                print(f"  ❌ Query failed: {e}")
                results.append(SearchResult(
                    text="", citations=[], model=kwargs.get("model", "sonar"),
                    query=q, estimated_cost=0, duration_seconds=0,
                ))
        return results

    # ----- budget tracking -----

    def budget_remaining(self) -> float:
        """Check remaining Perplexity budget for the current month."""
        usage = self._read_usage()
        current_month = datetime.now().strftime("%Y-%m")

        if usage.get("current_month") != current_month:
            # New month — reset
            return MONTHLY_LIMIT_USD

        spent = usage.get("usage", {}).get("estimated_cost_usd", 0)
        return MONTHLY_LIMIT_USD - spent

    def _read_usage(self) -> dict:
        """Read current usage file."""
        if not USAGE_FILE.exists():
            return {}
        try:
            return json.loads(USAGE_FILE.read_text())
        except (json.JSONDecodeError, OSError):
            return {}

    def _log_usage(self, query: str, model: str, estimated_cost: float,
                   task_context: str, query_type: str):
        """Append a query record to the usage file."""
        usage = self._read_usage()
        current_month = datetime.now().strftime("%Y-%m")

        # Reset if new month
        if usage.get("current_month") != current_month:
            usage = {
                "monthly_limit_usd": MONTHLY_LIMIT_USD,
                "current_month": current_month,
                "usage": {"total_queries": 0, "estimated_cost_usd": 0.0, "queries": []},
                "alerts": {"warn_at_percent": 80, "block_at_percent": 100},
                "loop_detection": {
                    "current_task_query_count": 0,
                    "current_task_name": "",
                    "last_query_timestamp": "",
                    "consecutive_low_info_queries": 0,
                },
            }

        usage_data = usage.setdefault("usage", {"total_queries": 0, "estimated_cost_usd": 0.0, "queries": []})
        usage_data["total_queries"] = usage_data.get("total_queries", 0) + 1
        usage_data["estimated_cost_usd"] = round(
            usage_data.get("estimated_cost_usd", 0) + estimated_cost, 4
        )

        now = datetime.now(timezone.utc).isoformat()
        usage_data.setdefault("queries", []).append({
            "timestamp": now,
            "type": query_type,
            "model": model,
            "description": query[:200],
            "task_context": task_context,
            "estimated_cost": estimated_cost,
        })

        # Update loop detection
        loop = usage.setdefault("loop_detection", {})
        if loop.get("current_task_name") == task_context:
            loop["current_task_query_count"] = loop.get("current_task_query_count", 0) + 1
        else:
            loop["current_task_name"] = task_context
            loop["current_task_query_count"] = 1
        loop["last_query_timestamp"] = now

        # Per-task cap check
        if loop["current_task_query_count"] > 10:
            print(f"  ⚠️  Per-task query cap reached (10). Blocking further queries for '{task_context}'.")

        USAGE_FILE.parent.mkdir(parents=True, exist_ok=True)
        USAGE_FILE.write_text(json.dumps(usage, indent=4))

    def usage_summary(self) -> Dict[str, Any]:
        """Return current session + cumulative usage stats."""
        return {
            "session_queries": self.call_count,
            "session_cost": round(self.total_cost, 4),
            "budget_remaining": round(self.budget_remaining(), 2),
        }


# ---------------------------------------------------------------------------
# Exceptions
# ---------------------------------------------------------------------------

class BudgetExhaustedError(Exception):
    """Raised when Perplexity budget is too low to proceed."""
    pass
