#!/usr/bin/env python3
"""
Shared NotebookLM Client — RAG knowledge retrieval for Antigravity workflows.

Wraps the notebooklm-mcp CLI for programmatic notebook queries.
Budget tracking enforced per directives/notebooklm-usage-policy.md.

Usage:
    from notebooklm_client import NotebookLMClient, load_env

    load_env()
    client = NotebookLMClient()

    # Query specific notebook
    result = client.query("notebook-id", "What are the key patterns?")

    # Search all notebooks
    results = client.search_all_notebooks("LinkedIn hooks")

    # Check budget
    used, remaining = client.check_budget()
"""

import hashlib
import json
import os
import shutil
import subprocess
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


# ---------------------------------------------------------------------------
# Environment
# ---------------------------------------------------------------------------

BASE_PATH = Path(__file__).parent.parent
ENV_PATH = BASE_PATH / ".env"
USAGE_FILE = BASE_PATH / ".agent" / "notebooklm-usage.json"
CACHE_FILE = BASE_PATH / ".agent" / "knowledge-cache.json"
NOTEBOOKS_REGISTRY = BASE_PATH / "mcp-servers" / "notebooklm" / "notebooks.md"
CHROME_PROFILE = BASE_PATH / "mcp-servers" / "notebooklm" / "chrome_profile_notebooklm"
CONFIG_FILE = BASE_PATH / "mcp-servers" / "notebooklm" / "notebooklm-config.json"

MONTHLY_QUERY_LIMIT = 100
CACHE_TTL_DAYS = 7
MAX_RESPONSE_TOKENS = 500


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
# Response
# ---------------------------------------------------------------------------

class NotebookResult:
    """Structured result from a NotebookLM query."""

    __slots__ = ("text", "notebook_id", "notebook_name", "query", "cached", "duration_seconds")

    def __init__(self, **kwargs):
        for k in self.__slots__:
            setattr(self, k, kwargs.get(k, None))

    def to_dict(self) -> Dict[str, Any]:
        return {k: getattr(self, k) for k in self.__slots__}

    def compress(self, max_tokens: int = MAX_RESPONSE_TOKENS) -> str:
        """Compress response to token limit (rough estimate: 1 token ≈ 4 chars)."""
        if not self.text:
            return ""
        max_chars = max_tokens * 4
        if len(self.text) <= max_chars:
            return self.text
        return self.text[:max_chars] + "..."


# ---------------------------------------------------------------------------
# Client
# ---------------------------------------------------------------------------

class NotebookLMClient:
    """NotebookLM client with budget tracking, caching, and usage logging."""

    def __init__(self):
        self.call_count = 0
        self.cache_hits = 0

    def query(
        self,
        notebook_id: str,
        query: str,
        *,
        context: str = "",
        task_context: str = "",
        use_cache: bool = True,
    ) -> NotebookResult:
        """
        Query a specific NotebookLM notebook.

        Args:
            notebook_id: Notebook ID from notebooks.md registry
            query: The question to ask
            context: Optional context for the query
            task_context: Name of the task (for usage logging)
            use_cache: Whether to use cached responses (default True)

        Returns:
            NotebookResult with text, notebook info, etc.
        """
        # Budget check
        queries_used, queries_remaining = self.check_budget()

        if queries_remaining <= 0:
            raise BudgetExhaustedError(
                f"NotebookLM budget exhausted ({queries_used}/{MONTHLY_QUERY_LIMIT} queries used). "
                f"Resets on 1st of next month."
            )

        if queries_remaining <= 20:
            print(f"  ⚠️  Budget low ({queries_remaining} queries remaining).")

        # Check cache
        if use_cache:
            cached_result = self._check_cache(notebook_id, query)
            if cached_result:
                self.cache_hits += 1
                print(f"  ✓ Cache hit for notebook query")
                return cached_result

        # Get notebook name from registry
        notebook_name = self._get_notebook_name(notebook_id)

        # Execute query via notebooklm-mcp CLI
        start = time.monotonic()

        try:
            result_text = self._execute_cli_query(notebook_id, query, context)
        except subprocess.CalledProcessError as e:
            raise NotebookLMError(f"Query failed: {e.stderr}") from e

        duration = time.monotonic() - start

        self.call_count += 1

        # Log usage
        self._log_query(
            notebook_id=notebook_id,
            query=query,
            task_context=task_context,
        )

        result = NotebookResult(
            text=result_text,
            notebook_id=notebook_id,
            notebook_name=notebook_name,
            query=query,
            cached=False,
            duration_seconds=round(duration, 2),
        )

        # Cache result
        self._cache_result(notebook_id, query, result)

        return result

    def search_all_notebooks(
        self,
        query: str,
        *,
        limit: int = 3,
        task_context: str = "",
    ) -> Dict[str, NotebookResult]:
        """
        Search across all registered notebooks.

        Args:
            query: The search query
            limit: Max number of notebooks to query (default 3)
            task_context: Name of the task (for usage logging)

        Returns:
            Dict mapping notebook_id -> NotebookResult
        """
        notebooks = self.list_notebooks()

        if not notebooks:
            return {}

        # Limit to top N notebooks
        notebooks = notebooks[:limit]

        results = {}
        for nb in notebooks:
            try:
                result = self.query(
                    notebook_id=nb["id"],
                    query=query,
                    task_context=task_context or "search_all",
                )
                results[nb["id"]] = result
            except (BudgetExhaustedError, NotebookLMError) as e:
                print(f"  ❌ Query failed for {nb['name']}: {e}")
                continue

        return results

    def list_notebooks(self) -> List[Dict[str, str]]:
        """
        List all registered NotebookLM notebooks from registry.

        Returns:
            List of dicts with keys: id, name, purpose
        """
        if not NOTEBOOKS_REGISTRY.exists():
            return []

        notebooks = []
        content = NOTEBOOKS_REGISTRY.read_text()

        # Parse markdown table
        for line in content.splitlines():
            line = line.strip()
            if line.startswith("|") and "`" in line and line.count("|") >= 3:
                # Table row: | **Name** | `id` | Purpose |
                parts = [p.strip() for p in line.split("|")[1:-1]]  # Skip first/last empty
                if len(parts) >= 3 and parts[1].startswith("`"):
                    name = parts[0].replace("**", "").strip()
                    notebook_id = parts[1].strip("`").strip()
                    purpose = parts[2].strip()

                    if notebook_id and len(notebook_id) > 10:  # Valid UUID-like
                        notebooks.append({
                            "id": notebook_id,
                            "name": name,
                            "purpose": purpose,
                        })

        return notebooks

    def check_budget(self) -> Tuple[int, int]:
        """
        Check remaining NotebookLM budget for the current month.

        Returns:
            (queries_used, queries_remaining)
        """
        usage = self._read_usage()
        current_month = datetime.now().strftime("%Y-%m")

        if usage.get("current_month") != current_month:
            # New month — reset
            return (0, MONTHLY_QUERY_LIMIT)

        queries_used = usage.get("usage", {}).get("total_queries", 0)
        queries_remaining = MONTHLY_QUERY_LIMIT - queries_used

        return (queries_used, queries_remaining)

    # ----- Private methods -----

    def _build_cli_env(self) -> dict:
        """Build subprocess env with SSL cert fix applied."""
        env = os.environ.copy()
        try:
            import certifi
            cert_path = certifi.where()
            env.setdefault("SSL_CERT_FILE", cert_path)
            env.setdefault("REQUESTS_CA_BUNDLE", cert_path)
        except ImportError:
            pass  # certifi not installed; SSL will use system defaults
        return env

    def _reset_chrome_session(self) -> None:
        """
        Clear Chrome session state that causes 'Could not find chat input element'.
        Deletes session/cache directories while preserving auth cookies and login data.
        """
        session_dirs = [
            "Default/Session Storage",
            "Default/Cache",
            "Default/Code Cache",
            "Default/Service Worker",
            "Default/BrowsingTopicsState",
        ]
        for rel_dir in session_dirs:
            target = CHROME_PROFILE / rel_dir
            if target.exists():
                shutil.rmtree(target, ignore_errors=True)
        print("  ↻  Chrome session state cleared — retrying query...")

    def _execute_cli_query(self, notebook_id: str, query: str, context: str) -> str:
        """Execute notebooklm-mcp CLI query with SSL fix and auto-reset on broken session."""
        cmd = [
            "uv", "run", "notebooklm-mcp",
            "--config", str(CONFIG_FILE),
            "chat",
            "--message", query,
            "--notebook", notebook_id,
        ]
        if context:
            cmd.extend(["--context", context])

        env = self._build_cli_env()
        run_kwargs = dict(
            cwd=BASE_PATH / "mcp-servers" / "notebooklm",
            capture_output=True,
            text=True,
            timeout=180,
            env=env,
        )

        result = subprocess.run(cmd, **run_kwargs)

        # Detect broken Chrome session and retry once with reset
        broken_session_signals = [
            "Could not find chat input element",
            "TimeoutError",
            "ElementHandle",
        ]
        combined_output = (result.stdout or "") + (result.stderr or "")
        if result.returncode != 0 or any(s in combined_output for s in broken_session_signals):
            self._reset_chrome_session()
            result = subprocess.run(cmd, check=True, **run_kwargs)

        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, cmd, result.stdout, result.stderr)

        return result.stdout.strip()

    def _get_notebook_name(self, notebook_id: str) -> str:
        """Get notebook name from registry."""
        notebooks = self.list_notebooks()
        for nb in notebooks:
            if nb["id"] == notebook_id:
                return nb["name"]
        return "Unknown Notebook"

    def _check_cache(self, notebook_id: str, query: str) -> Optional[NotebookResult]:
        """Check if cached response exists and is still valid."""
        if not CACHE_FILE.exists():
            return None

        try:
            cache = json.loads(CACHE_FILE.read_text())
        except (json.JSONDecodeError, OSError):
            return None

        cache_key = self._cache_key(notebook_id, query)
        entry = cache.get(cache_key)

        if not entry:
            return None

        # Check TTL
        cached_at = datetime.fromisoformat(entry["cached_at"])
        age = datetime.now(timezone.utc) - cached_at

        if age > timedelta(days=CACHE_TTL_DAYS):
            return None

        # Return cached result
        return NotebookResult(
            text=entry["text"],
            notebook_id=notebook_id,
            notebook_name=entry["notebook_name"],
            query=query,
            cached=True,
            duration_seconds=0,
        )

    def _cache_result(self, notebook_id: str, query: str, result: NotebookResult):
        """Cache a query result."""
        cache = {}
        if CACHE_FILE.exists():
            try:
                cache = json.loads(CACHE_FILE.read_text())
            except (json.JSONDecodeError, OSError):
                cache = {}

        cache_key = self._cache_key(notebook_id, query)
        cache[cache_key] = {
            "text": result.text,
            "notebook_name": result.notebook_name,
            "cached_at": datetime.now(timezone.utc).isoformat(),
        }

        # Write cache
        CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
        CACHE_FILE.write_text(json.dumps(cache, indent=4))

    def _cache_key(self, notebook_id: str, query: str) -> str:
        """Generate cache key for notebook + query."""
        combined = f"{notebook_id}:{query.lower().strip()}"
        return hashlib.sha256(combined.encode()).hexdigest()[:16]

    def _read_usage(self) -> dict:
        """Read current usage file."""
        if not USAGE_FILE.exists():
            return {}
        try:
            return json.loads(USAGE_FILE.read_text())
        except (json.JSONDecodeError, OSError):
            return {}

    def _log_query(self, notebook_id: str, query: str, task_context: str):
        """Append a query record to the usage file."""
        usage = self._read_usage()
        current_month = datetime.now().strftime("%Y-%m")

        # Reset if new month
        if usage.get("current_month") != current_month:
            usage = {
                "monthly_limit": MONTHLY_QUERY_LIMIT,
                "current_month": current_month,
                "usage": {"total_queries": 0, "queries": []},
                "alerts": {"warn_at_queries": 80, "block_at_queries": 100},
                "loop_detection": {
                    "current_task_query_count": 0,
                    "current_task_name": "",
                    "last_query_timestamp": "",
                },
            }

        usage_data = usage.setdefault("usage", {"total_queries": 0, "queries": []})
        usage_data["total_queries"] = usage_data.get("total_queries", 0) + 1

        now = datetime.now(timezone.utc).isoformat()
        notebook_name = self._get_notebook_name(notebook_id)

        usage_data.setdefault("queries", []).append({
            "timestamp": now,
            "notebook_id": notebook_id,
            "notebook_name": notebook_name,
            "query": query[:200],  # Truncate long queries
            "task_context": task_context,
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
        if loop["current_task_query_count"] > 5:
            print(f"  ⚠️  Per-task query cap reached (5). Consider consolidating queries for '{task_context}'.")

        USAGE_FILE.parent.mkdir(parents=True, exist_ok=True)
        USAGE_FILE.write_text(json.dumps(usage, indent=4))

    def usage_summary(self) -> Dict[str, Any]:
        """Return current session + cumulative usage stats."""
        queries_used, queries_remaining = self.check_budget()

        return {
            "session_queries": self.call_count,
            "session_cache_hits": self.cache_hits,
            "monthly_queries_used": queries_used,
            "monthly_queries_remaining": queries_remaining,
        }


# ---------------------------------------------------------------------------
# Exceptions
# ---------------------------------------------------------------------------

class BudgetExhaustedError(Exception):
    """Raised when NotebookLM query budget is exhausted."""
    pass


class NotebookLMError(Exception):
    """Raised when NotebookLM query fails."""
    pass


# ---------------------------------------------------------------------------
# CLI (for testing)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import sys

    load_env()

    if len(sys.argv) < 4:
        print("Usage: python notebooklm_client.py query <notebook-id> <query>")
        print("       python notebooklm_client.py search <query>")
        print("       python notebooklm_client.py list")
        print("       python notebooklm_client.py budget")
        sys.exit(1)

    client = NotebookLMClient()
    command = sys.argv[1]

    if command == "query":
        notebook_id = sys.argv[2]
        query_text = " ".join(sys.argv[3:])

        result = client.query(notebook_id, query_text, task_context="cli_test")
        print(f"\n{result.compress()}\n")
        print(f"[{result.notebook_name} | {result.duration_seconds}s | cached: {result.cached}]")

    elif command == "search":
        query_text = " ".join(sys.argv[2:])

        results = client.search_all_notebooks(query_text, task_context="cli_search")
        for nb_id, result in results.items():
            print(f"\n### {result.notebook_name}")
            print(result.compress())
            print()

    elif command == "list":
        notebooks = client.list_notebooks()
        print(f"\nRegistered Notebooks ({len(notebooks)}):\n")
        for nb in notebooks:
            print(f"• {nb['name']}")
            print(f"  ID: {nb['id']}")
            print(f"  Purpose: {nb['purpose']}\n")

    elif command == "budget":
        used, remaining = client.check_budget()
        print(f"\nNotebookLM Budget:")
        print(f"  Used: {used}/{MONTHLY_QUERY_LIMIT} queries")
        print(f"  Remaining: {remaining} queries")

        if remaining <= 20:
            print(f"  ⚠️  Warning: Low budget!")
