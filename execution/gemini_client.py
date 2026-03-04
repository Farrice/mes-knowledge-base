#!/usr/bin/env python3
"""
Shared Gemini API Client — Single point of upgrade for all Antigravity scripts.

Features:
- Async-first with sync fallback
- Google Search grounding (opt-in)
- Thinking/reasoning mode (opt-in)
- Model tiering (lite/flash/pro per-call override)
- Structured output via response_schema (opt-in)
- Centralized token tracking and cost estimation
- Exponential backoff retry

Usage:
    from gemini_client import GeminiClient, load_env

    load_env()
    client = GeminiClient()

    # Async
    text, meta = await client.generate("prompt", system_instruction="context")

    # With grounding
    text, meta = await client.generate("prompt", grounding=True)

    # With thinking
    text, meta = await client.generate("prompt", thinking_budget=2048)

    # With model override
    text, meta = await client.generate("prompt", model="pro")

    # With structured output
    text, meta = await client.generate("prompt", response_schema=my_schema,
                                        response_mime_type="application/json")

    # Sync wrapper
    text, meta = client.generate_sync("prompt")


    # Image generation (Nano Banana 2)
    images, meta = await client.generate_image("A futuristic logo for Antigravity")

    # Image with specific size/aspect
    images, meta = await client.generate_image("prompt", image_size="4K", aspect_ratio="16:9")
"""

import asyncio
import base64
import os
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from google import genai
from google.genai import types


# ---------------------------------------------------------------------------
# Environment
# ---------------------------------------------------------------------------

BASE_PATH = Path(__file__).parent.parent
ENV_PATH = BASE_PATH / ".env"


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
# Model Tiers & Cost
# ---------------------------------------------------------------------------

MODEL_TIERS = {
    "lite":  os.environ.get("GEMINI_MODEL_LITE",  "gemini-3.1-flash-lite-preview"),
    "flash": os.environ.get("GEMINI_MODEL_FLASH", "gemini-2.5-flash"),
    "pro":   os.environ.get("GEMINI_MODEL_PRO",   "gemini-2.5-pro"),
    "image": os.environ.get("GEMINI_MODEL_IMAGE", "gemini-3.1-flash-image-preview"),
}

# Cost per 1M tokens (input / output) — verified March 2026
# Source: https://ai.google.dev/gemini-api/docs/pricing
COST_PER_MILLION = {
    # Gemini 2.5 series (stable, production)
    "gemini-2.5-flash-lite":      {"input": 0.10, "output": 0.40},
    "gemini-2.5-flash":           {"input": 0.30, "output": 2.50},
    "gemini-2.5-pro":             {"input": 1.25, "output": 10.00},
    # Gemini 3.x series (preview)
    "gemini-3-flash-preview":     {"input": 0.50, "output": 3.00},
    "gemini-3.1-flash-lite-preview": {"input": 0.25, "output": 1.50},
    "gemini-3.1-pro-preview":     {"input": 2.00, "output": 12.00},
    # Image models (token cost is secondary — image gen is the main cost)
    "gemini-3.1-flash-image-preview": {"input": 0.30, "output": 2.50},
}

DEFAULT_COST = {"input": 0.50, "output": 3.00}  # fallback for unknown models


def estimate_cost(model: str, input_tokens: int, output_tokens: int) -> float:
    """Estimate USD cost for a single API call."""
    rates = COST_PER_MILLION.get(model, DEFAULT_COST)
    return (input_tokens / 1_000_000 * rates["input"] +
            output_tokens / 1_000_000 * rates["output"])


# ---------------------------------------------------------------------------
# Response Metadata
# ---------------------------------------------------------------------------

class ResponseMeta:
    """Metadata returned alongside generated text."""

    __slots__ = (
        "model", "input_tokens", "output_tokens", "total_tokens",
        "thinking_tokens", "grounding_queries", "estimated_cost_usd",
        "duration_seconds",
    )

    def __init__(self, **kwargs):
        for k in self.__slots__:
            setattr(self, k, kwargs.get(k, 0))
        if isinstance(kwargs.get("model"), str):
            self.model = kwargs["model"]

    def to_dict(self) -> Dict[str, Any]:
        return {k: getattr(self, k) for k in self.__slots__}


# ---------------------------------------------------------------------------
# Client
# ---------------------------------------------------------------------------

class GeminiClient:
    """Unified async Gemini client for all Antigravity scripts."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        default_model: Optional[str] = None,
    ):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY", "")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment or argument")

        self.default_model = (
            default_model
            or os.environ.get("GEMINI_MODEL", "gemini-2.0-flash")
        )
        self._client = genai.Client(api_key=self.api_key)

        # Cumulative tracking for budget enforcement
        self.total_tokens_used = 0
        self.total_cost_usd = 0.0
        self.call_count = 0

    # ----- model resolution -----

    def resolve_model(self, model: Optional[str] = None) -> str:
        """Resolve a model tier name or full model ID."""
        if model is None:
            return self.default_model
        return MODEL_TIERS.get(model, model)  # tier name → full ID, or pass-through

    # ----- core async generate -----

    async def generate(
        self,
        prompt: str,
        *,
        system_instruction: str = "",
        model: Optional[str] = None,
        temperature: float = 0.7,
        max_output_tokens: int = 4096,
        thinking_budget: Optional[int] = None,
        grounding: bool = False,
        response_schema: Any = None,
        response_mime_type: Optional[str] = None,
        retries: int = 1,
    ) -> Tuple[str, ResponseMeta]:
        """
        Generate content from Gemini.

        Args:
            prompt: The user prompt text.
            system_instruction: Expert context / system instruction.
            model: Model tier ("lite"/"flash"/"pro") or full model ID. None = default.
            temperature: Sampling temperature (0.0-2.0).
            max_output_tokens: Max response length.
            thinking_budget: Token budget for chain-of-thought reasoning. None = disabled.
            grounding: Enable Google Search grounding.
            response_schema: JSON schema dict for structured output.
            response_mime_type: MIME type for structured output (e.g. "application/json").
            retries: Max retry attempts on failure.

        Returns:
            (response_text, ResponseMeta)
        """
        resolved_model = self.resolve_model(model)

        # Build config
        config = types.GenerateContentConfig(
            temperature=temperature,
            max_output_tokens=max_output_tokens,
        )

        if system_instruction:
            config.system_instruction = system_instruction

        # Thinking mode
        if thinking_budget is not None and thinking_budget > 0:
            config.thinking_config = types.ThinkingConfig(
                thinking_budget=thinking_budget
            )

        # Google Search grounding
        if grounding:
            config.tools = [types.Tool(google_search=types.GoogleSearch())]

        # Structured output
        if response_schema is not None:
            config.response_schema = response_schema
            config.response_mime_type = response_mime_type or "application/json"

        # Execute with retry
        start = time.monotonic()
        last_error = None

        for attempt in range(retries + 1):
            try:
                response = await self._client.aio.models.generate_content(
                    model=resolved_model,
                    contents=prompt,
                    config=config,
                )

                duration = time.monotonic() - start

                # Extract token counts
                input_tokens = 0
                output_tokens = 0
                total_tokens = 0
                thinking_tokens = 0

                if response.usage_metadata:
                    um = response.usage_metadata
                    input_tokens = getattr(um, "prompt_token_count", 0) or 0
                    output_tokens = getattr(um, "candidates_token_count", 0) or 0
                    total_tokens = getattr(um, "total_token_count", 0) or 0
                    thinking_tokens = getattr(um, "thoughts_token_count", 0) or 0
                    # Fallback: if only total is set
                    if total_tokens and not (input_tokens or output_tokens):
                        input_tokens = total_tokens  # conservative estimate

                # Count grounding queries from response metadata
                grounding_queries = 0
                if grounding and hasattr(response, "candidates"):
                    for candidate in (response.candidates or []):
                        gm = getattr(candidate, "grounding_metadata", None)
                        if gm:
                            queries = getattr(gm, "search_entry_point", None)
                            if queries:
                                grounding_queries += 1

                cost = estimate_cost(resolved_model, input_tokens, output_tokens)

                # Update cumulative tracking
                self.total_tokens_used += total_tokens
                self.total_cost_usd += cost
                self.call_count += 1

                meta = ResponseMeta(
                    model=resolved_model,
                    input_tokens=input_tokens,
                    output_tokens=output_tokens,
                    total_tokens=total_tokens,
                    thinking_tokens=thinking_tokens,
                    grounding_queries=grounding_queries,
                    estimated_cost_usd=cost,
                    duration_seconds=round(duration, 2),
                )

                return response.text or "", meta

            except Exception as e:
                last_error = e
                if attempt < retries:
                    wait = 2 ** attempt
                    print(f"  ⚠️  Retry {attempt + 1}/{retries} ({wait}s): {e}")
                    await asyncio.sleep(wait)

        raise last_error  # type: ignore[misc]

    # ----- sync wrapper -----

    def generate_sync(
        self,
        prompt: str,
        **kwargs,
    ) -> Tuple[str, ResponseMeta]:
        """Synchronous wrapper around generate(). Use for scripts that don't run async."""
        loop = asyncio.new_event_loop()
        try:
            return loop.run_until_complete(self.generate(prompt, **kwargs))
        finally:
            loop.close()

    # ----- batch execution -----

    async def generate_batch(
        self,
        items: list,
        *,
        max_parallel: int = 10,
        prompt_fn=None,
        token_budget: Optional[int] = None,
    ) -> list:
        """
        Run multiple generate calls in parallel with concurrency control.

        Args:
            items: List of work items (any type).
            max_parallel: Max concurrent API calls.
            prompt_fn: Callable(item) -> dict of kwargs for generate().
                       Must return at minimum {"prompt": "..."}.
            token_budget: Stop spawning if cumulative tokens exceed this.

        Returns:
            List of (item, text, ResponseMeta) tuples in original order.
        """
        semaphore = asyncio.Semaphore(max_parallel)
        results = [None] * len(items)

        async def _run(idx, item):
            if token_budget and self.total_tokens_used >= token_budget:
                results[idx] = (item, "", ResponseMeta(
                    model=self.default_model,
                    estimated_cost_usd=0,
                    duration_seconds=0,
                ))
                return

            kwargs = prompt_fn(item) if prompt_fn else {"prompt": str(item)}
            async with semaphore:
                try:
                    text, meta = await self.generate(**kwargs)
                    results[idx] = (item, text, meta)
                except Exception as e:
                    results[idx] = (item, "", ResponseMeta(
                        model=self.resolve_model(kwargs.get("model")),
                        estimated_cost_usd=0,
                        duration_seconds=0,
                    ))
                    print(f"  ❌ Batch item {idx} failed: {e}")

        tasks = [_run(i, item) for i, item in enumerate(items)]
        await asyncio.gather(*tasks)
        return results

    # ----- image generation (Nano Banana 2) -----

    IMAGE_MODEL = "gemini-3.1-flash-image-preview"

    async def generate_image(
        self,
        prompt: str,
        *,
        model: Optional[str] = None,
        image_size: str = "1K",
        aspect_ratio: str = "1:1",
        input_image_path: Optional[str] = None,
        retries: int = 1,
    ) -> Tuple[List[bytes], ResponseMeta]:
        """
        Generate images using Nano Banana 2 (gemini-3.1-flash-image-preview).

        Args:
            prompt: Description of the image to generate.
            model: Override model (default: gemini-2.0-flash-preview-image-generation).
            image_size: Resolution — "512px", "1K", "2K", or "4K".
            aspect_ratio: Aspect ratio — e.g. "1:1", "16:9", "9:16", "4:3", "3:4".
            input_image_path: Path to an image for editing (text+image input).
            retries: Max retry attempts.

        Returns:
            (list_of_image_bytes, ResponseMeta)
            Each item in list is raw PNG bytes. Save with: Path("out.png").write_bytes(img)
        """
        resolved_model = model or self.IMAGE_MODEL

        config = types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
            image_config=types.ImageConfig(
                aspect_ratio=aspect_ratio,
            ),
        )

        # Build contents — text only, or text + image for editing
        contents = [prompt]
        if input_image_path:
            from PIL import Image as PILImage
            img = PILImage.open(input_image_path)
            contents.append(img)

        start = time.monotonic()
        last_error = None

        for attempt in range(retries + 1):
            try:
                response = await self._client.aio.models.generate_content(
                    model=resolved_model,
                    contents=contents,
                    config=config,
                )

                duration = time.monotonic() - start

                # Extract images and text from response parts
                images = []
                text_parts = []
                for part in (response.parts or []):
                    if part.text is not None:
                        text_parts.append(part.text)
                    elif part.inline_data is not None:
                        # Decode base64 image data
                        raw = part.inline_data.data
                        if isinstance(raw, str):
                            images.append(base64.b64decode(raw))
                        elif isinstance(raw, bytes):
                            images.append(raw)

                # Token tracking
                input_tokens = 0
                output_tokens = 0
                total_tokens = 0
                if response.usage_metadata:
                    um = response.usage_metadata
                    input_tokens = getattr(um, "prompt_token_count", 0) or 0
                    output_tokens = getattr(um, "candidates_token_count", 0) or 0
                    total_tokens = getattr(um, "total_token_count", 0) or 0

                cost = estimate_cost(resolved_model, input_tokens, output_tokens)
                self.total_tokens_used += total_tokens
                self.total_cost_usd += cost
                self.call_count += 1

                meta = ResponseMeta(
                    model=resolved_model,
                    input_tokens=input_tokens,
                    output_tokens=output_tokens,
                    total_tokens=total_tokens,
                    estimated_cost_usd=cost,
                    duration_seconds=round(duration, 2),
                )

                return images, meta

            except Exception as e:
                last_error = e
                if attempt < retries:
                    wait = 2 ** attempt
                    print(f"  ⚠️  Image retry {attempt + 1}/{retries} ({wait}s): {e}")
                    await asyncio.sleep(wait)

        raise last_error  # type: ignore[misc]

    def generate_image_sync(
        self,
        prompt: str,
        **kwargs,
    ) -> Tuple[List[bytes], ResponseMeta]:
        """Synchronous wrapper for generate_image()."""
        loop = asyncio.new_event_loop()
        try:
            return loop.run_until_complete(self.generate_image(prompt, **kwargs))
        finally:
            loop.close()

    # ----- diagnostics -----

    def usage_summary(self) -> Dict[str, Any]:
        """Return cumulative usage stats."""
        return {
            "total_tokens": self.total_tokens_used,
            "total_cost_usd": round(self.total_cost_usd, 4),
            "api_calls": self.call_count,
        }
