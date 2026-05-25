#!/usr/bin/env python3
"""
Multi-model deliberation — Gemini voice for the /deliberate skill.

The /deliberate workflow runs the same prompt through Claude (the running
orchestrator, inline in the conversation) AND Gemini (this script). Claude
then synthesizes both — surfacing contradictions explicitly instead of
blending them away.

This script provides only the Gemini half of the deliberation. Claude
produces its take directly in the chat; we don't need an Anthropic SDK
call here.

Output format (--json):
  {
    "model": "gemini-2.5-pro",
    "response": "<Gemini's full answer>",
    "input_tokens": int,
    "output_tokens": int,
    "estimated_cost_usd": float,
    "duration_seconds": float,
    "grounding_used": bool
  }

Usage:
  python3 deliberate.py --prompt "Should we price at $5K or $7.5K?" --json
  python3 deliberate.py --prompt "..." --system "You are a pricing strategist." --model pro --grounding
  python3 deliberate.py --prompt "..." --model flash    # cheaper, faster
"""
from __future__ import annotations

import argparse
import contextlib
import io
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gemini_client import GeminiClient, load_env

load_env()


@contextlib.contextmanager
def _silence_stdout():
    """Suppress stdout chatter from sibling modules during the Gemini call.

    gemini_client.py prints retry warnings to stdout. When deliberate.py runs
    in --json mode (consumed by the /deliberate workflow), those warnings
    corrupt the JSON parse. This context manager swallows them.
    Errors raised by the Gemini API still propagate as exceptions — we only
    suppress benign print() chatter.
    """
    sink = io.StringIO()
    original = sys.stdout
    sys.stdout = sink
    try:
        yield sink
    finally:
        sys.stdout = original


def cmd_ask(args) -> int:
    """Run a single Gemini call and return its response."""
    try:
        client = GeminiClient()
    except ValueError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        print("HINT: set GEMINI_API_KEY in .env or environment", file=sys.stderr)
        return 1

    # Pass model as a kwarg to generate_sync — this triggers resolve_model
    # (tier name "flash" / "pro" / "lite" → full Gemini model ID).
    generate_kwargs = {
        "prompt": args.prompt,
        "model": args.model,
        "temperature": args.temperature,
        "max_output_tokens": args.max_tokens,
    }
    if args.system:
        generate_kwargs["system_instruction"] = args.system
    if args.grounding:
        generate_kwargs["grounding"] = True

    try:
        # Suppress gemini_client stdout chatter so --json output is parseable
        with _silence_stdout():
            text, meta = client.generate_sync(**generate_kwargs)
    except Exception as e:
        # Surface clearly — Claude needs to know the deliberation failed so it
        # can either fall back to single-model or surface the gap to the user.
        err = {"error": str(e), "stage": "gemini_call_failed"}
        if args.json:
            print(json.dumps(err))
        else:
            print(f"❌ Gemini call failed: {e}", file=sys.stderr)
        return 1

    result = {
        "model": meta.model,
        "response": text,
        "input_tokens": meta.input_tokens,
        "output_tokens": meta.output_tokens,
        "total_tokens": meta.total_tokens,
        "estimated_cost_usd": round(meta.estimated_cost_usd, 6),
        "duration_seconds": round(meta.duration_seconds, 2),
        "grounding_used": bool(args.grounding),
    }

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("=" * 64)
        print(f"GEMINI VOICE  ({meta.model})")
        print("=" * 64)
        print(text)
        print()
        print("-" * 64)
        print(
            f"Tokens: in={meta.input_tokens} out={meta.output_tokens}  "
            f"Cost: ${meta.estimated_cost_usd:.4f}  Duration: {meta.duration_seconds:.1f}s"
        )

    return 0


def _tier_to_model(tier: str) -> str:
    """Map convenience tier names to actual Gemini model IDs.

    'pro' / 'flash' / 'lite' map via gemini_client's MODEL_TIERS at call time.
    Anything else passes through (full model ID strings work too).
    """
    return tier  # gemini_client.resolve_model handles the lookup


def main() -> int:
    p = argparse.ArgumentParser(
        description="Gemini voice for /deliberate — multi-model deliberation",
    )
    p.add_argument(
        "--prompt",
        required=True,
        help="The question or deliberation seed Gemini should respond to",
    )
    p.add_argument(
        "--system",
        default="",
        help="(Optional) system instruction / expert framing for Gemini",
    )
    p.add_argument(
        "--model",
        default="flash",
        help="Model tier (pro|flash|lite) or full Gemini model ID. Default: flash. "
             "(pro is paid-tier on most GEMINI_API_KEY accounts; use flash unless you've confirmed pro quota.)",
    )
    p.add_argument(
        "--temperature",
        type=float,
        default=0.7,
        help="Sampling temperature (0.0-2.0). Default: 0.7.",
    )
    p.add_argument(
        "--max-tokens",
        type=int,
        default=4096,
        help="Max response length in tokens. Default: 4096.",
    )
    p.add_argument(
        "--grounding",
        action="store_true",
        help="Enable Google Search grounding for factual queries",
    )
    p.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON (for /deliberate workflow consumption) instead of human-readable",
    )

    args = p.parse_args()
    return cmd_ask(args)


if __name__ == "__main__":
    sys.exit(main())
