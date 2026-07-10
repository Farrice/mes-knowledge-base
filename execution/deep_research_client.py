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
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests

# Shared success gate — validates engine content BEFORE any cost accounting.
try:
    from research_contract import validate_engine_text
except ImportError:  # when imported as execution.deep_research_client
    from execution.research_contract import validate_engine_text


# ---------------------------------------------------------------------------
# Environment
# ---------------------------------------------------------------------------

BASE_PATH = Path(__file__).parent.parent
ENV_PATH = BASE_PATH / ".env"
USAGE_FILE = BASE_PATH / ".agent" / "gemini-api-usage.json"

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
        "estimated_cost", "duration_seconds", "status",
    )

    def __init__(self, **kwargs):
        for k in self.__slots__:
            setattr(self, k, kwargs.get(k, None))
        if self.citations is None:
            self.citations = []

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
        max_wait_seconds: int = 900,  # 15 min cap — Deep Research Max can run long
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

        # ---- Start the interaction ----
        start = time.monotonic()

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
            if status in (402, 403, 429):
                raise BudgetExhaustedError(
                    f"Deep Research start failed (HTTP {status}) — likely billing/quota. "
                    f"Response: {body}. Check directives/google-api-usage-policy.md; "
                    f"Ultra may not have covered the call AND prepaid is exhausted."
                ) from e
            raise RuntimeError(
                f"Deep Research start failed (HTTP {status}). Response: {body}"
            ) from e

        interaction_id = start_data.get("id")
        if not interaction_id:
            raise RuntimeError(f"No interaction ID in start response: {start_data}")

        # ---- Poll for completion ----
        elapsed = 0
        final_data: Dict[str, Any] = {}
        while elapsed < max_wait_seconds:
            time.sleep(poll_interval_seconds)
            elapsed += poll_interval_seconds

            poll_resp = requests.get(
                f"{self.BASE_URL}/interactions/{interaction_id}",
                headers={"x-goog-api-key": self.api_key},
                timeout=30,
            )
            poll_resp.raise_for_status()
            final_data = poll_resp.json()

            status = final_data.get("status", "").lower()
            if status == "completed":
                break
            if status == "failed":
                raise RuntimeError(
                    f"Deep Research interaction failed: "
                    f"{final_data.get('error', 'unknown error')}"
                )
        else:
            raise TimeoutError(
                f"Deep Research interaction {interaction_id} did not complete "
                f"within {max_wait_seconds}s."
            )

        duration = time.monotonic() - start

        # ---- Extract text + citations ----
        # The live Deep Research Interactions API returns `steps` (model_output
        # steps whose `content[]` parts carry `.text`, plus `.data` base64 image
        # charts we skip, plus `thought` steps). Older/preview schema used
        # `outputs[]`. Parse `steps` first, fall back to `outputs`. (Fixed
        # 2026-05-31 — the old `outputs`-only parser silently returned empty text
        # for every Gemini Deep Research consumer in the system.)
        text, citations = self._parse_final(final_data)

        # --- Success gate: validate content BEFORE any cost accounting ---
        # The honest-accounting fix. A 'completed' interaction that yielded no
        # usable text must NOT increment cost, must NOT log as a real query, and
        # must return status="failed" so the dispatcher degrades to the floor.
        # (Previously this only blanked the text but still logged $0.50 spend and
        # returned status="completed" — the exact false-usage / false-PASS bug.)
        ok, reason = validate_engine_text(text, citations)
        if not ok:
            self._log_failure(
                query=query,
                agent=AGENT_IDS[mode],
                reason=reason,
                duration_seconds=round(duration, 2),
                task_context=task_context,
                query_type=query_type,
                interaction_id=interaction_id,
            )
            return DeepResearchResult(
                text="",
                citations=citations,
                agent=AGENT_IDS[mode],
                query=query,
                interaction_id=interaction_id,
                estimated_cost=0.0,
                duration_seconds=round(duration, 2),
                status="failed",
            )

        self.call_count += 1
        self.total_cost += est_cost

        # ---- Log usage (only validated content reaches here) ----
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
        )

    # ----- non-blocking (parallel background) API -----

    def _parse_final(self, final_data: Dict[str, Any]):
        """Extract (text, citations) from a completed interaction. Handles the
        live `steps` schema and the legacy `outputs` schema."""
        text = ""
        citations: List[str] = []
        steps = final_data.get("steps") or final_data.get("outputs") or []
        for step in steps:
            stype = step.get("type")
            if stype in ("model_output", "text", "output"):
                for part in (step.get("content") or []):
                    if isinstance(part, dict) and isinstance(part.get("text"), str):
                        text += part["text"]
                if isinstance(step.get("text"), str):  # legacy flat shape
                    text += step["text"] + "\n\n"
            if "citations" in step:
                citations.extend(step["citations"])
        if not citations and "citations" in final_data:
            citations = final_data["citations"]
        if not citations and text:
            # 2026-07-08: the Interactions API now embeds sources as inline
            # markdown links instead of populating a citations array — a max
            # run returned 56k chars with 65 URLs in-text and citations=[],
            # so every claim was quarantined downstream. Harvest inline URLs
            # (deduped, order-preserving) so provenance survives.
            citations = list(dict.fromkeys(
                u.rstrip(".,;") for u in
                re.findall(r"https?://[^\s)\]>\"'`]+", text)))
        return text, self._resolve_grounding_redirects(citations)

    @staticmethod
    def _resolve_grounding_redirects(citations: List[str], cap: int = 40) -> List[str]:
        """Vertex grounding redirect URLs all share one opaque Google domain,
        which destroys domain-diversity provenance downstream. Follow them to
        the real source (capped, fail-safe: unresolvable keeps the wrapper)."""
        resolved: List[str] = []
        for u in citations[:cap]:
            if "vertexaisearch.cloud.google.com/grounding-api-redirect" in u:
                try:
                    r = requests.head(u, allow_redirects=True, timeout=8)
                    resolved.append(r.url or u)
                except Exception:
                    resolved.append(u)
            else:
                resolved.append(u)
        resolved.extend(citations[cap:])
        return list(dict.fromkeys(resolved))

    def start_async(self, query: str, *, mode: str = "standard",
                    enable_google_search: bool = True,
                    enable_url_context: bool = True) -> str:
        """Fire a Deep Research interaction and return its id IMMEDIATELY (no poll).
        Lets the swarm run Gemini in parallel in the background. $0 to start.
        Raises BudgetExhaustedError if balance too low, RuntimeError on API error."""
        if mode not in AGENT_IDS:
            raise ValueError(f"Unknown mode: {mode}")
        if self.budget_remaining() < MIN_BALANCE_USD:
            raise BudgetExhaustedError(
                f"Deep Research budget too low (${self.budget_remaining():.2f}).")
        headers = {"Content-Type": "application/json", "x-goog-api-key": self.api_key}
        tools = []
        if enable_google_search:
            tools.append({"type": "google_search"})
        if enable_url_context:
            tools.append({"type": "url_context"})
        payload: Dict[str, Any] = {
            "agent": AGENT_IDS[mode], "input": query, "background": True,
            "agent_config": {"type": "deep-research", "thinking_summaries": "auto"},
        }
        if tools:
            payload["tools"] = tools
        try:
            resp = requests.post(f"{self.BASE_URL}/interactions", json=payload,
                                 headers=headers, timeout=60)
            resp.raise_for_status()
            iid = resp.json().get("id")
        except requests.HTTPError as e:
            status = e.response.status_code if e.response else "?"
            if status in (402, 403, 429):
                raise BudgetExhaustedError(f"Deep Research start failed (HTTP {status}).") from e
            raise RuntimeError(f"Deep Research start failed (HTTP {status}).") from e
        if not iid:
            raise RuntimeError("No interaction id in start response.")
        return iid

    def collect(self, interaction_id: str, *, query: str = "", mode: str = "standard",
                task_context: str = "swarm-parallel-gemini") -> DeepResearchResult:
        """Check a backgrounded interaction. If completed, parse + validate + log
        honestly (real spend only on validated content) and return the result.
        If still running, returns status='in_progress' (text=''). Never blocks."""
        headers = {"x-goog-api-key": self.api_key}
        try:
            resp = requests.get(f"{self.BASE_URL}/interactions/{interaction_id}",
                                headers=headers, timeout=30)
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            return DeepResearchResult(text="", citations=[], agent=AGENT_IDS.get(mode, ""),
                                      query=query, interaction_id=interaction_id,
                                      estimated_cost=0.0, duration_seconds=0.0,
                                      status="error")
        status = (data.get("status") or "").lower()
        if status in ("pending", "in_progress", "running", ""):
            return DeepResearchResult(text="", citations=[], agent=AGENT_IDS.get(mode, ""),
                                      query=query, interaction_id=interaction_id,
                                      estimated_cost=0.0, duration_seconds=0.0,
                                      status="in_progress")
        if status == "failed":
            self._log_failure(query=query, agent=AGENT_IDS.get(mode, ""), reason="interaction_failed",
                              duration_seconds=0.0, task_context=task_context,
                              query_type="research", interaction_id=interaction_id)
            return DeepResearchResult(text="", citations=[], agent=AGENT_IDS.get(mode, ""),
                                      query=query, interaction_id=interaction_id,
                                      estimated_cost=0.0, duration_seconds=0.0, status="failed")
        # completed
        text, citations = self._parse_final(data)
        ok, reason = validate_engine_text(text, citations)
        if not ok:
            self._log_failure(query=query, agent=AGENT_IDS.get(mode, ""), reason=reason,
                              duration_seconds=0.0, task_context=task_context,
                              query_type="research", interaction_id=interaction_id)
            return DeepResearchResult(text="", citations=citations, agent=AGENT_IDS.get(mode, ""),
                                      query=query, interaction_id=interaction_id,
                                      estimated_cost=0.0, duration_seconds=0.0, status="failed")
        est_cost = EST_COST_PER_QUERY.get(mode, 0.5)
        self.call_count += 1
        self.total_cost += est_cost
        self._log_usage(query=query, agent=AGENT_IDS[mode], estimated_cost=est_cost,
                        duration_seconds=0.0, task_context=task_context,
                        query_type="research", interaction_id=interaction_id)
        return DeepResearchResult(text=text.strip(), citations=citations, agent=AGENT_IDS[mode],
                                  query=query, interaction_id=interaction_id,
                                  estimated_cost=est_cost, duration_seconds=0.0, status="completed")

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
        reason: str,
        duration_seconds: float,
        task_context: str,
        query_type: str,
        interaction_id: str,
    ):
        """Record a failed/empty Deep Research call WITHOUT burning budget.

        This is the honest-accounting half of the success gate. A completed
        interaction that produced no usable text is a FAILURE — it must stay
        visible (so 'did Gemini actually deliver?' is answerable) but must never
        touch estimated_cost_usd, the queries array, or loop_detection counts.
        """
        usage = self._read_usage()
        failures = usage.setdefault("failures", [])
        failures.append({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "type": query_type,
            "agent": agent,
            "description": query[:200],
            "task_context": task_context,
            "reason": reason,
            "duration_seconds": duration_seconds,
            "interaction_id": interaction_id,
            "estimated_cost": 0.0,  # explicit: failures never cost
        })
        USAGE_FILE.parent.mkdir(parents=True, exist_ok=True)
        USAGE_FILE.write_text(json.dumps(usage, indent=4))


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
        "--no-google-search", action="store_true",
        help="Disable Google Search grounding",
    )
    args = parser.parse_args()

    load_env()
    client = DeepResearchClient()

    print(f"\n🧠 Starting Deep Research ({args.mode})")
    print(f"   Budget remaining: ${client.budget_remaining():.2f}")
    print(f"   Query: {args.query}\n")

    try:
        result = client.research(
            args.query,
            mode=args.mode,
            task_context=args.task_context,
            enable_google_search=not args.no_google_search,
        )
    except BudgetExhaustedError as e:
        print(f"❌ {e}")
        return 1

    print(f"✅ Completed in {result.duration_seconds:.1f}s\n")
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
