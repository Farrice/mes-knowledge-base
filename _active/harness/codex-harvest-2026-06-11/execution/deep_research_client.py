#!/usr/bin/env python3
"""
Deep Research Client — Gemini Interactions API wrapper for Antigravity workflows.

Calls Google's Deep Research API (released Dec 2025, Max variant April 2026).
Uses the Ultra-linked AI Studio key (GOOGLE_AI_STUDIO_KEY) — billed against
Ultra subscription coverage with $10 prepaid balance as defense-in-depth.

Billing pathway: see directives/google-api-usage-policy.md
Three layers of defense guarantee surprise bills are physically impossible.

Usage:
    from deep_research_client import DeepResearchClient, load_env

    load_env()
    client = DeepResearchClient()

    # Standard Deep Research (faster, ~$0.25-0.50)
    result = client.research("AI consulting market 2026", mode="standard")

    # Deep Research Max (comprehensive, ~$0.50-1.50)
    result = client.research("Premium coaching offer positioning", mode="max")

    print(result.text)
    print(result.citations)
"""

import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

try:
    import requests
except ImportError:
    import urllib.error
    import urllib.request

    class _CompatHTTPError(Exception):
        def __init__(self, response):
            self.response = response
            super().__init__(getattr(response, "text", "HTTP error"))

    class _CompatResponse:
        def __init__(self, status_code: int, text: str):
            self.status_code = status_code
            self.text = text

        def json(self):
            return json.loads(self.text)

        def raise_for_status(self):
            if self.status_code >= 400:
                raise _CompatHTTPError(self)

    class _CompatRequests:
        HTTPError = _CompatHTTPError
        RequestException = Exception

        @staticmethod
        def request(method: str, url: str, *, json: Optional[dict] = None,
                    headers: Optional[dict] = None, timeout: int = 30):
            data = None
            if json is not None:
                data = __import__("json").dumps(json).encode("utf-8")
            req = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
            try:
                with urllib.request.urlopen(req, timeout=timeout) as resp:
                    return _CompatResponse(resp.status, resp.read().decode("utf-8"))
            except urllib.error.HTTPError as e:
                return _CompatResponse(e.code, e.read().decode("utf-8", errors="replace"))

        @classmethod
        def post(cls, url: str, **kwargs):
            return cls.request("POST", url, **kwargs)

        @classmethod
        def get(cls, url: str, **kwargs):
            return cls.request("GET", url, **kwargs)

    requests = _CompatRequests()


# ---------------------------------------------------------------------------
# Environment
# ---------------------------------------------------------------------------

BASE_PATH = Path(__file__).parent.parent
ENV_PATH = BASE_PATH / ".env"
USAGE_FILE = BASE_PATH / ".agent" / "gemini-api-usage.json"
STATUS_DIR = BASE_PATH / ".tmp" / "deep-research-status"

# Defense Layer 3: prepaid ceiling. Anything more is a code bug.
PREPAID_CEILING_USD = 10.00

# Hard block threshold — BudgetExhaustedError fires below this.
MIN_BALANCE_USD = 0.50


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


def validate_engine_text(text: str, citations: List[str]) -> Tuple[bool, str]:
    """Use the research contract validator when available, with a local fallback."""
    try:
        from research_contract import validate_engine_text as _validate
    except Exception:
        try:
            from execution.research_contract import validate_engine_text as _validate
        except Exception:
            _validate = None
    if _validate:
        return _validate(text, citations)
    if not (text or "").strip():
        return False, "empty text"
    if not citations:
        return False, "no citations"
    return True, "ok"


# ---------------------------------------------------------------------------
# Model Configuration
# ---------------------------------------------------------------------------

AGENT_IDS = {
    "standard": "deep-research-preview-04-2026",
    "max": "deep-research-max-preview-04-2026",
}

# Conservative estimates. Real billing tracked via prepaid balance,
# these are for budget arithmetic before the call completes.
EST_COST_PER_QUERY = {
    "standard": 0.50,
    "max": 1.50,
}


# ---------------------------------------------------------------------------
# Response
# ---------------------------------------------------------------------------

class DeepResearchResult:
    """Structured result from a Deep Research interaction."""

    __slots__ = (
        "text", "citations", "agent", "query", "interaction_id",
        "estimated_cost", "duration_seconds", "status", "raw",
    )

    def __init__(self, **kwargs):
        for k in self.__slots__:
            setattr(self, k, kwargs.get(k, None))
        if self.citations is None:
            self.citations = []
        if self.raw is None:
            self.raw = {}

    def to_dict(self) -> Dict[str, Any]:
        return {k: getattr(self, k) for k in self.__slots__}


# ---------------------------------------------------------------------------
# Client
# ---------------------------------------------------------------------------

class DeepResearchClient:
    """Gemini Deep Research client with three-layer spend defense."""

    BASE_URL = "https://generativelanguage.googleapis.com/v1beta"

    def __init__(self, api_key: Optional[str] = None):
        # Deliberately uses a DIFFERENT env var than GEMINI_API_KEY (used by
        # legacy gemini_client.py). This prevents accidentally routing Deep
        # Research through the legacy pay-as-you-go key.
        self.api_key = api_key or os.environ.get("GOOGLE_AI_STUDIO_KEY", "")
        if not self.api_key:
            raise ValueError(
                "GOOGLE_AI_STUDIO_KEY not found. This is the Ultra-linked AI Studio key. "
                "Generate it at https://aistudio.google.com/ from an account linked to Google AI Ultra. "
                "Add it to .env. See directives/google-api-usage-policy.md."
            )
        self.call_count = 0
        self.total_cost = 0.0

    # ----- public API -----

    def research(
        self,
        query: str,
        *,
        mode: str = "standard",
        task_context: str = "",
        query_type: str = "research",
        poll_interval_seconds: int = 10,
        max_wait_seconds: int = 3600,
        enable_google_search: bool = True,
        enable_url_context: bool = True,
    ) -> DeepResearchResult:
        """
        Run a Deep Research query.

        Args:
            query: Research question.
            mode: "standard" or "max" — see AGENT_IDS.
            task_context: Logical task name (for loop detection).
            query_type: research | verification | synthesis | social_listening
            poll_interval_seconds: Seconds between polling the Interactions API.
            max_wait_seconds: Abort if no completion by this time.
            enable_google_search: Give Deep Research access to Google Search.
            enable_url_context: Give Deep Research access to URL Context tool.

        Returns:
            DeepResearchResult with synthesized text and citations.

        Raises:
            BudgetExhaustedError: If prepaid balance below threshold or per-task cap hit.
            requests.RequestException: Network/API errors.
        """
        if mode not in AGENT_IDS:
            raise ValueError(f"Unknown mode: {mode}. Use 'standard' or 'max'.")

        # ---- Pre-flight defense Layer 3: prepaid balance check ----
        remaining = self.budget_remaining()
        est_cost = EST_COST_PER_QUERY[mode]

        if remaining < MIN_BALANCE_USD:
            raise BudgetExhaustedError(
                f"Deep Research budget too low (${remaining:.2f} remaining, "
                f"need at least ${MIN_BALANCE_USD:.2f}). "
                f"Fall back to Perplexity via perplexity_client.py."
            )

        # Per-task cap — Deep Research calls are heavy, 5 per task is generous
        usage = self._read_usage()
        loop = usage.get("loop_detection", {})
        task_cap = 5
        if (loop.get("current_task_name") == task_context
                and loop.get("current_task_query_count", 0) >= task_cap):
            raise BudgetExhaustedError(
                f"Per-task Deep Research cap reached ({task_cap}) for '{task_context}'. "
                f"Collapse queries or switch tasks."
            )

        # If the estimated cost would drop us below MIN_BALANCE, downgrade mode
        if mode == "max" and (remaining - est_cost) < MIN_BALANCE_USD:
            print(f"  ⚠️  Max mode would exhaust budget. Downgrading to standard.")
            mode = "standard"
            est_cost = EST_COST_PER_QUERY[mode]

        start = time.monotonic()
        interaction_id, start_data = self.start_interaction(
            query,
            mode=mode,
            enable_google_search=enable_google_search,
            enable_url_context=enable_url_context,
        )
        self._write_status(
            interaction_id,
            {
                "status": "running",
                "query": query,
                "mode": mode,
                "agent": AGENT_IDS[mode],
                "task_context": task_context,
                "query_type": query_type,
                "started_at": datetime.now(timezone.utc).isoformat(),
                "estimated_cost": est_cost,
                "start_response": start_data,
            },
        )

        try:
            final_data = self.poll_interaction(
                interaction_id,
                query=query,
                mode=mode,
                task_context=task_context,
                query_type=query_type,
                poll_interval_seconds=poll_interval_seconds,
                max_wait_seconds=max_wait_seconds,
                started_monotonic=start,
                estimated_cost=est_cost,
            )
        except TimeoutError as e:
            self._write_status(
                interaction_id,
                {
                    "status": "timeout",
                    "query": query,
                    "mode": mode,
                    "agent": AGENT_IDS[mode],
                    "task_context": task_context,
                    "query_type": query_type,
                    "interaction_id": interaction_id,
                    "timed_out_at": datetime.now(timezone.utc).isoformat(),
                    "max_wait_seconds": max_wait_seconds,
                    "message": str(e),
                },
            )
            raise

        duration = time.monotonic() - start

        text, citations = self._extract_text_and_citations(final_data)

        self.call_count += 1
        self.total_cost += est_cost

        # ---- Log usage ----
        self._log_usage(
            query=query,
            agent=AGENT_IDS[mode],
            estimated_cost=est_cost,
            duration_seconds=round(duration, 2),
            task_context=task_context,
            query_type=query_type,
            interaction_id=interaction_id,
        )

        return DeepResearchResult(
            text=text.strip(),
            citations=citations,
            agent=AGENT_IDS[mode],
            query=query,
            interaction_id=interaction_id,
            estimated_cost=est_cost,
            duration_seconds=round(duration, 2),
            status="completed",
            raw=final_data,
        )

    def start_interaction(
        self,
        query: str,
        *,
        mode: str = "standard",
        enable_google_search: bool = True,
        enable_url_context: bool = True,
    ) -> Tuple[str, Dict[str, Any]]:
        """Start a background Gemini Deep Research interaction and return its id."""
        if mode not in AGENT_IDS:
            raise ValueError(f"Unknown mode: {mode}. Use 'standard' or 'max'.")

        headers = {
            "Content-Type": "application/json",
            "x-goog-api-key": self.api_key,
        }

        tools = []
        if enable_google_search:
            tools.append({"type": "google_search"})
        if enable_url_context:
            tools.append({"type": "url_context"})

        start_payload: Dict[str, Any] = {
            "agent": AGENT_IDS[mode],
            "input": query,
            "background": True,
            "agent_config": {
                "type": "deep-research",
                "thinking_summaries": "auto",
                "visualization": "auto",
                "collaborative_planning": False,
            },
        }
        if tools:
            start_payload["tools"] = tools

        try:
            start_resp = requests.post(
                f"{self.BASE_URL}/interactions",
                json=start_payload,
                headers=headers,
                timeout=60,
            )
            start_resp.raise_for_status()
            start_data = start_resp.json()
        except requests.HTTPError as e:
            status = e.response.status_code if e.response else "?"
            body = e.response.text[:500] if e.response is not None else ""
            self._log_failure(query=query, agent=AGENT_IDS[mode], status=str(status), message=body)
            if status in (402, 403, 429):
                raise BudgetExhaustedError(
                    f"Deep Research start failed (HTTP {status}) — likely billing/quota. "
                    f"Response: {body}. Check directives/google-api-usage-policy.md."
                ) from e
            raise RuntimeError(
                f"Deep Research start failed (HTTP {status}). Response: {body}"
            ) from e

        interaction_id = start_data.get("id")
        if not interaction_id:
            raise RuntimeError(f"No interaction ID in start response: {start_data}")
        return interaction_id, start_data

    def start_async(
        self,
        query: str,
        *,
        mode: str = "standard",
        enable_google_search: bool = True,
        enable_url_context: bool = True,
    ) -> str:
        """Start a background Deep Research interaction and return immediately."""
        if mode not in AGENT_IDS:
            raise ValueError(f"Unknown mode: {mode}. Use 'standard' or 'max'.")
        if self.budget_remaining() < MIN_BALANCE_USD:
            raise BudgetExhaustedError(
                f"Deep Research budget too low (${self.budget_remaining():.2f})."
            )
        interaction_id, start_data = self.start_interaction(
            query,
            mode=mode,
            enable_google_search=enable_google_search,
            enable_url_context=enable_url_context,
        )
        self._write_status(
            interaction_id,
            {
                "status": "running",
                "query": query,
                "mode": mode,
                "agent": AGENT_IDS[mode],
                "interaction_id": interaction_id,
                "started_at": datetime.now(timezone.utc).isoformat(),
                "estimated_cost": EST_COST_PER_QUERY.get(mode, 0.5),
                "start_response": start_data,
            },
        )
        return interaction_id

    def get_interaction(self, interaction_id: str) -> Dict[str, Any]:
        """Fetch the current Gemini Interactions API state for an interaction."""
        poll_resp = requests.get(
            f"{self.BASE_URL}/interactions/{interaction_id}",
            headers={"x-goog-api-key": self.api_key},
            timeout=30,
        )
        poll_resp.raise_for_status()
        return poll_resp.json()

    def poll_interaction(
        self,
        interaction_id: str,
        *,
        query: str = "",
        mode: str = "standard",
        task_context: str = "",
        query_type: str = "research",
        poll_interval_seconds: int = 10,
        max_wait_seconds: int = 3600,
        started_monotonic: Optional[float] = None,
        estimated_cost: Optional[float] = None,
    ) -> Dict[str, Any]:
        """Poll a background interaction until completion or timeout."""
        started_monotonic = started_monotonic or time.monotonic()
        estimated_cost = estimated_cost if estimated_cost is not None else EST_COST_PER_QUERY.get(mode, 0.5)
        elapsed = 0
        final_data: Dict[str, Any] = {}
        while elapsed < max_wait_seconds:
            time.sleep(poll_interval_seconds)
            elapsed += poll_interval_seconds
            final_data = self.get_interaction(interaction_id)
            status = final_data.get("status", "").lower()
            self._write_status(
                interaction_id,
                {
                    "status": status or "unknown",
                    "query": query,
                    "mode": mode,
                    "task_context": task_context,
                    "query_type": query_type,
                    "interaction_id": interaction_id,
                    "last_polled_at": datetime.now(timezone.utc).isoformat(),
                    "elapsed_seconds": elapsed,
                    "estimated_cost": estimated_cost,
                },
            )
            if status == "completed":
                return final_data
            if status == "failed":
                self._log_failure(
                    query=query,
                    agent=AGENT_IDS.get(mode, mode),
                    status="failed",
                    message=json.dumps(final_data.get("error", final_data))[:1000],
                    interaction_id=interaction_id,
                )
                raise RuntimeError(
                    f"Deep Research interaction failed: "
                    f"{final_data.get('error', 'unknown error')}"
                )

        raise TimeoutError(
            f"Deep Research interaction {interaction_id} did not complete "
            f"within {max_wait_seconds}s. Resume with --resume {interaction_id}."
        )

    def resume(
        self,
        interaction_id: str,
        *,
        query: str = "",
        mode: str = "standard",
        task_context: str = "resume",
        query_type: str = "research",
        poll_interval_seconds: int = 10,
        max_wait_seconds: int = 3600,
    ) -> DeepResearchResult:
        """Resume polling an existing background interaction."""
        start = time.monotonic()
        final_data = self.poll_interaction(
            interaction_id,
            query=query,
            mode=mode,
            task_context=task_context,
            query_type=query_type,
            poll_interval_seconds=poll_interval_seconds,
            max_wait_seconds=max_wait_seconds,
            started_monotonic=start,
        )
        text, citations = self._extract_text_and_citations(final_data)
        duration = time.monotonic() - start
        return DeepResearchResult(
            text=text.strip(),
            citations=citations,
            agent=AGENT_IDS.get(mode, mode),
            query=query,
            interaction_id=interaction_id,
            estimated_cost=0.0,
            duration_seconds=round(duration, 2),
            status="completed",
            raw=final_data,
        )

    def collect(
        self,
        interaction_id: str,
        *,
        query: str = "",
        mode: str = "standard",
        task_context: str = "swarm-parallel-gemini",
    ) -> DeepResearchResult:
        """Check a background interaction once; never blocks.

        Completed, validated content logs estimated usage. Pending interactions
        return status='in_progress' with empty text.
        """
        try:
            data = self.get_interaction(interaction_id)
        except Exception as e:
            self._write_status(
                interaction_id,
                {
                    "status": "error",
                    "query": query,
                    "mode": mode,
                    "interaction_id": interaction_id,
                    "message": f"{type(e).__name__}: {str(e)[:300]}",
                    "last_polled_at": datetime.now(timezone.utc).isoformat(),
                },
            )
            return DeepResearchResult(
                text="",
                citations=[],
                agent=AGENT_IDS.get(mode, mode),
                query=query,
                interaction_id=interaction_id,
                estimated_cost=0.0,
                duration_seconds=0.0,
                status="error",
                raw={},
            )

        status = (data.get("status") or "").lower()
        pending = {"", "pending", "in_progress", "running", "queued"}
        completed = {"completed", "complete", "done", "succeeded", "success"}
        if status in pending:
            self._write_status(
                interaction_id,
                {
                    "status": status or "running",
                    "query": query,
                    "mode": mode,
                    "interaction_id": interaction_id,
                    "last_polled_at": datetime.now(timezone.utc).isoformat(),
                },
            )
            return DeepResearchResult(
                text="",
                citations=[],
                agent=AGENT_IDS.get(mode, mode),
                query=query,
                interaction_id=interaction_id,
                estimated_cost=0.0,
                duration_seconds=0.0,
                status="in_progress",
                raw=data,
            )
        if status == "failed":
            self._log_failure(
                query=query,
                agent=AGENT_IDS.get(mode, mode),
                status="failed",
                message=json.dumps(data.get("error", data))[:1000],
                interaction_id=interaction_id,
            )
            self._write_status(
                interaction_id,
                {
                    "status": "failed",
                    "query": query,
                    "mode": mode,
                    "interaction_id": interaction_id,
                    "last_polled_at": datetime.now(timezone.utc).isoformat(),
                },
            )
            return DeepResearchResult(
                text="",
                citations=[],
                agent=AGENT_IDS.get(mode, mode),
                query=query,
                interaction_id=interaction_id,
                estimated_cost=0.0,
                duration_seconds=0.0,
                status="failed",
                raw=data,
            )

        if status not in completed:
            self._write_status(
                interaction_id,
                {
                    "status": status or "unknown",
                    "query": query,
                    "mode": mode,
                    "interaction_id": interaction_id,
                    "last_polled_at": datetime.now(timezone.utc).isoformat(),
                },
            )
            return DeepResearchResult(
                text="",
                citations=[],
                agent=AGENT_IDS.get(mode, mode),
                query=query,
                interaction_id=interaction_id,
                estimated_cost=0.0,
                duration_seconds=0.0,
                status=status or "unknown",
                raw=data,
            )

        text, citations = self._extract_text_and_citations(data)
        ok, reason = validate_engine_text(text, citations)
        if not ok:
            self._log_failure(
                query=query,
                agent=AGENT_IDS.get(mode, mode),
                status="failed",
                message=reason,
                interaction_id=interaction_id,
            )
            self._write_status(
                interaction_id,
                {
                    "status": "failed",
                    "query": query,
                    "mode": mode,
                    "interaction_id": interaction_id,
                    "message": reason,
                    "last_polled_at": datetime.now(timezone.utc).isoformat(),
                },
            )
            return DeepResearchResult(
                text="",
                citations=citations,
                agent=AGENT_IDS.get(mode, mode),
                query=query,
                interaction_id=interaction_id,
                estimated_cost=0.0,
                duration_seconds=0.0,
                status="failed",
                raw=data,
            )

        est_cost = EST_COST_PER_QUERY.get(mode, 0.5)
        status_path = STATUS_DIR / f"{interaction_id}.json"
        existing: Dict[str, Any] = {}
        if status_path.exists():
            try:
                existing = json.loads(status_path.read_text())
            except json.JSONDecodeError:
                existing = {}
        if not existing.get("usage_logged"):
            self.call_count += 1
            self.total_cost += est_cost
            self._log_usage(
                query=query,
                agent=AGENT_IDS.get(mode, mode),
                estimated_cost=est_cost,
                duration_seconds=0.0,
                task_context=task_context,
                query_type="research",
                interaction_id=interaction_id,
            )
        self._write_status(
            interaction_id,
            {
                "status": "completed",
                "query": query,
                "mode": mode,
                "interaction_id": interaction_id,
                "usage_logged": True,
                "completed_at": datetime.now(timezone.utc).isoformat(),
                "estimated_cost": est_cost,
            },
        )
        return DeepResearchResult(
            text=text.strip(),
            citations=citations,
            agent=AGENT_IDS.get(mode, mode),
            query=query,
            interaction_id=interaction_id,
            estimated_cost=est_cost,
            duration_seconds=0.0,
            status="completed",
            raw=data,
        )

    # ----- budget tracking -----

    def budget_remaining(self) -> float:
        """Estimated remaining prepaid balance (defense Layer 3 only)."""
        usage = self._read_usage()
        current_month = datetime.now().strftime("%Y-%m")

        if usage.get("current_month") != current_month:
            return PREPAID_CEILING_USD

        spent = usage.get("usage", {}).get("estimated_cost_usd", 0)
        return PREPAID_CEILING_USD - spent

    def usage_summary(self) -> Dict[str, Any]:
        """Session + month-to-date stats."""
        return {
            "session_queries": self.call_count,
            "session_estimated_cost": round(self.total_cost, 4),
            "budget_remaining_estimate": round(self.budget_remaining(), 2),
        }

    # ----- internal -----

    def _read_usage(self) -> dict:
        if not USAGE_FILE.exists():
            return {}
        try:
            return json.loads(USAGE_FILE.read_text())
        except (json.JSONDecodeError, OSError):
            return {}

    def _log_usage(
        self,
        *,
        query: str,
        agent: str,
        estimated_cost: float,
        duration_seconds: float,
        task_context: str,
        query_type: str,
        interaction_id: str,
    ):
        """Append a query record to the usage file."""
        usage = self._read_usage()
        current_month = datetime.now().strftime("%Y-%m")

        if usage.get("current_month") != current_month:
            usage = {
                "prepaid_ceiling_usd": PREPAID_CEILING_USD,
                "current_month": current_month,
                "usage": {
                    "total_queries": 0,
                    "estimated_cost_usd": 0.0,
                    "queries": [],
                },
                "alerts": {"warn_at_percent": 80, "block_at_percent": 95},
                "loop_detection": {
                    "current_task_query_count": 0,
                    "current_task_name": "",
                    "last_query_timestamp": "",
                },
                "notes": (
                    "Defense-in-depth tracker. Ultra subscription should cover most "
                    "calls at $0. This tracks estimated spend against the $10 prepaid "
                    "ceiling as a last-resort check. See directives/google-api-usage-policy.md."
                ),
            }

        usage_data = usage.setdefault(
            "usage",
            {"total_queries": 0, "estimated_cost_usd": 0.0, "queries": []},
        )
        usage_data["total_queries"] = usage_data.get("total_queries", 0) + 1
        usage_data["estimated_cost_usd"] = round(
            usage_data.get("estimated_cost_usd", 0) + estimated_cost, 4
        )

        now = datetime.now(timezone.utc).isoformat()
        usage_data.setdefault("queries", []).append({
            "timestamp": now,
            "type": query_type,
            "agent": agent,
            "description": query[:200],
            "task_context": task_context,
            "estimated_cost": estimated_cost,
            "duration_seconds": duration_seconds,
            "interaction_id": interaction_id,
        })

        loop = usage.setdefault("loop_detection", {})
        if loop.get("current_task_name") == task_context:
            loop["current_task_query_count"] = loop.get("current_task_query_count", 0) + 1
        else:
            loop["current_task_name"] = task_context
            loop["current_task_query_count"] = 1
        loop["last_query_timestamp"] = now

        USAGE_FILE.parent.mkdir(parents=True, exist_ok=True)
        USAGE_FILE.write_text(json.dumps(usage, indent=4))

    def _log_failure(
        self,
        *,
        query: str,
        agent: str,
        status: str,
        message: str,
        interaction_id: str = "",
    ):
        usage = self._read_usage()
        usage.setdefault("failures", []).append({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "agent": agent,
            "status": status,
            "description": query[:200],
            "message": message[:1000],
            "interaction_id": interaction_id,
        })
        USAGE_FILE.parent.mkdir(parents=True, exist_ok=True)
        USAGE_FILE.write_text(json.dumps(usage, indent=4))

    def _write_status(self, interaction_id: str, payload: Dict[str, Any]):
        STATUS_DIR.mkdir(parents=True, exist_ok=True)
        path = STATUS_DIR / f"{interaction_id}.json"
        existing: Dict[str, Any] = {}
        if path.exists():
            try:
                existing = json.loads(path.read_text())
            except json.JSONDecodeError:
                existing = {}
        existing.update(payload)
        path.write_text(json.dumps(existing, indent=2))

    def _extract_text_and_citations(self, data: Dict[str, Any]) -> Tuple[str, List[str]]:
        text_parts: List[str] = []
        citations: List[str] = []

        def add_citation(value: Any):
            if isinstance(value, str) and value.startswith(("http://", "https://")):
                citations.append(value)
            elif isinstance(value, dict):
                for key in ("uri", "url", "source_url", "web_url"):
                    if isinstance(value.get(key), str):
                        add_citation(value[key])

        for output in data.get("outputs", []):
            if isinstance(output, dict):
                if output.get("type") == "text" and output.get("text"):
                    text_parts.append(output.get("text", ""))
                elif output.get("content"):
                    content = output["content"]
                    if isinstance(content, str):
                        text_parts.append(content)
                    elif isinstance(content, list):
                        for item in content:
                            if isinstance(item, dict) and item.get("text"):
                                text_parts.append(item["text"])
                for key in ("citations", "sources", "grounding_metadata"):
                    value = output.get(key)
                    if isinstance(value, list):
                        for item in value:
                            add_citation(item)
                    elif isinstance(value, dict):
                        add_citation(value)

        for key in ("citations", "sources"):
            value = data.get(key)
            if isinstance(value, list):
                for item in value:
                    add_citation(item)

        if not text_parts and isinstance(data.get("output"), str):
            text_parts.append(data["output"])

        deduped = []
        seen = set()
        for citation in citations:
            if citation not in seen:
                seen.add(citation)
                deduped.append(citation)
        return "\n\n".join(text_parts), deduped


# ---------------------------------------------------------------------------
# Exceptions
# ---------------------------------------------------------------------------

class BudgetExhaustedError(Exception):
    """Raised when Deep Research budget is too low to proceed safely."""
    pass


# ---------------------------------------------------------------------------
# CLI (for quick manual testing)
# ---------------------------------------------------------------------------

def _cli():
    import argparse

    parser = argparse.ArgumentParser(description="Deep Research CLI")
    parser.add_argument("query", help="Research question")
    parser.add_argument(
        "--mode", choices=["standard", "max"], default="standard",
        help="Deep Research (fast) or Deep Research Max (comprehensive)",
    )
    parser.add_argument(
        "--task-context", default="cli-test",
        help="Task name for loop detection and logging",
    )
    parser.add_argument(
        "--resume",
        help="Resume polling an existing Gemini interaction id instead of starting a new one",
    )
    parser.add_argument(
        "--max-wait-seconds", type=int, default=3600,
        help="Maximum polling time before writing resumable timeout status",
    )
    parser.add_argument(
        "--poll-interval-seconds", type=int, default=10,
        help="Seconds between background interaction polls",
    )
    parser.add_argument(
        "--no-google-search", action="store_true",
        help="Disable Google Search grounding",
    )
    args = parser.parse_args()

    load_env()
    client = DeepResearchClient()

    print(f"\nStarting Deep Research ({args.mode})")
    print(f"   Budget remaining: ${client.budget_remaining():.2f}")
    print(f"   Query: {args.query}\n")

    try:
        if args.resume:
            result = client.resume(
                args.resume,
                query=args.query,
                mode=args.mode,
                task_context=args.task_context,
                max_wait_seconds=args.max_wait_seconds,
                poll_interval_seconds=args.poll_interval_seconds,
            )
        else:
            result = client.research(
                args.query,
                mode=args.mode,
                task_context=args.task_context,
                enable_google_search=not args.no_google_search,
                max_wait_seconds=args.max_wait_seconds,
                poll_interval_seconds=args.poll_interval_seconds,
            )
    except BudgetExhaustedError as e:
        print(f"ERROR: {e}")
        return 1

    print(f"Completed in {result.duration_seconds:.1f}s\n")
    print(result.text)
    if result.citations:
        print("\n## Citations\n")
        for i, c in enumerate(result.citations, 1):
            print(f"{i}. {c}")

    print(f"\n--- Usage ---")
    print(json.dumps(client.usage_summary(), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(_cli())
