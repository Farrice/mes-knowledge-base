#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "fal-client>=0.5.0",
#     "requests>=2.31.0",
# ]
# ///
"""decompose.py — fal.ai / Qwen image-layer decomposition wrapper.

Decomposes a flat image into RGBA layers using ``fal-ai/qwen-image-layered``.
Each returned layer is written to ``{output_dir}/layers/NN.png`` and a
``manifest.json`` is written alongside (status: ok / skipped / error).

Exit codes
----------
EXIT_OK      = 0   decomposition succeeded; layers/ + manifest.json written
EXIT_ERROR   = 1   API / network / safety error; manifest.json written,
                   NO partial layers/ dir (atomic)
EXIT_SKIPPED = 3   FAL_KEY not set; skipped-stub manifest written, no layers/

Fail-safe contract
------------------
Consumers MUST handle EXIT_SKIPPED (3) gracefully — FAL_KEY is OPTIONAL.
When absent the wrapper writes::

    {"status": "skipped", "reason": "no_fal_key", "layers": []}

and exits with EXIT_SKIPPED. No exception is raised, no traceback emitted.

CLI
---
Usage::

    decompose.py (--image PATH | --image-url URL) [--output-dir DIR]
                 [--num-layers N] [--steps N] [--guidance F]
                 [--format {PNG,JPEG,WEBP}] [--seed N]
                 [--prompt TEXT] [--negative-prompt TEXT]

Options:
    --image PATH            Local image file to upload and decompose.
    --image-url URL         Pre-hosted image URL (skips upload).
    --output-dir DIR        Directory for manifest.json + layers/ (default: cwd).
    --num-layers N          Number of layers to decompose into (default: 4).
    --steps N               Inference steps (default: 28).
    --guidance F            Guidance scale (default: 5.0).
    --format FMT            Output format: PNG | JPEG | WEBP (default: PNG).
    --seed N                Random seed for reproducibility.
    --prompt TEXT           Optional positive prompt to guide decomposition.
    --negative-prompt TEXT  Optional negative prompt.

Manifest schema (status: ok)
-----------------------------
::

    {
      "tool": "decompose.py",
      "model": "fal-ai/qwen-image-layered",
      "source_image": "<path or url>",
      "status": "ok",
      "layer_count": 4,
      "seed": 42,
      "has_nsfw_concepts": [false, false, false, false],
      "params": {
        "num_layers": 4,
        "num_inference_steps": 28,
        "guidance_scale": 5.0,
        "output_format": "PNG"
      },
      "cost_usd_estimate": 0.05,
      "layers": [
        {"index": 0, "file": "layers/00.png", "width": 1080, "height": 1350,
         "source_url": "https://cdn.fal.ai/..."}
      ]
    }

~$0.05 per image (fal.ai pay-as-you-go pricing, 2026-06-04 estimate).
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
import tempfile
from pathlib import Path

# ── Exit code constants ────────────────────────────────────────────────────
EXIT_OK = 0       # decomposition succeeded
EXIT_ERROR = 1    # API / network / safety error (manifest written, no layers/)
EXIT_SKIPPED = 3  # FAL_KEY not set (skipped-stub manifest written, no layers/)

_MODEL = "fal-ai/qwen-image-layered"
_COST_USD_ESTIMATE = 0.05

# requests is declared in PEP-723 deps above; imported at module level so tests
# can patch "decompose.requests" cleanly. The no-key path does NOT call requests.
try:
    import requests
except ImportError:  # pragma: no cover — CI has no fal-client stack
    requests = None  # type: ignore[assignment]


# ── Env loading (re-read .env at point of use) ────────────────────────────

def _load_env_file() -> None:
    """Populate ``os.environ`` from the nearest project ``.env`` (walk up from
    cwd) so ``FAL_KEY`` resolves at the point of use — even when this script is
    invoked directly and the caller's shell never exported it.

    Called fresh at ``main()`` entry (not at import), so a key pasted into
    ``.env`` after the pipeline started is honored on the next decompose run.
    This mirrors ``clean_ref.py`` and generalizes the per-request key read
    (AIOS-139 Addendum 7 key-at-click / Addendum 9 project-root .env) to the
    decompose credential point. Existing ``os.environ`` values win, so a key
    injected by a parent process (e.g. Content Studio) is never overwritten.
    """
    here = Path.cwd()
    for candidate in [here, *here.parents]:
        env = candidate / ".env"
        if env.is_file():
            try:
                lines = env.read_text(encoding="utf-8", errors="replace").splitlines()
            except OSError:
                return
            for raw in lines:
                line = raw.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                k = k.strip()
                v = v.strip().strip('"').strip("'")
                if k and k not in os.environ:
                    os.environ[k] = v
            return


# ── Lazy fal_client loader (testable + no-import-on-no-key) ───────────────

def _get_fal_client():
    """Import and return the fal_client module.

    Separated into its own function so tests can patch it without needing
    fal-client installed in CI. The no-key fail-safe path never calls this.
    """
    try:
        import fal_client  # type: ignore[import]
        return fal_client
    except ImportError as exc:
        raise ImportError(
            "fal-client not installed. Run `uv add fal-client` or "
            "run via `uv run decompose.py ...`."
        ) from exc


# ── Helpers ───────────────────────────────────────────────────────────────

def _write_manifest(output_dir: Path, data: dict) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "manifest.json").write_text(
        json.dumps(data, indent=2), encoding="utf-8"
    )


def _get(obj, key, default=None):
    """Read ``key`` from a fal result that may be a dict (real API) or an
    attribute object/MagicMock (older client versions / tests). The real
    ``fal_client.subscribe`` returns a plain dict, so dict access must win.
    """
    if isinstance(obj, dict):
        return obj.get(key, default)
    return getattr(obj, key, default)


def _build_arguments(args: argparse.Namespace, image_url: str) -> dict:
    """Map parsed CLI args to the fal-ai/qwen-image-layered arguments dict."""
    arguments: dict = {
        "image_url": image_url,
        "num_layers": args.num_layers,
        "num_inference_steps": args.steps,
        "guidance_scale": args.guidance,
        # fal-ai/qwen-image-layered requires a lowercase enum ('png'|'webp');
        # the CLI accepts upper/mixed case for convenience.
        "output_format": args.format.lower(),
    }
    if args.seed is not None:
        arguments["seed"] = args.seed
    if args.prompt:
        arguments["prompt"] = args.prompt
    if args.negative_prompt:
        arguments["negative_prompt"] = args.negative_prompt
    return arguments


# ── Main ──────────────────────────────────────────────────────────────────

def main(argv: list[str] | None = None) -> None:
    """Entry point. Parses *argv* (or sys.argv[1:]) and runs decomposition.

    Always calls sys.exit() with EXIT_OK / EXIT_SKIPPED / EXIT_ERROR.
    Never raises an unhandled exception to the caller.
    """
    ap = argparse.ArgumentParser(
        description="Decompose a flat image into RGBA layers via fal.ai/Qwen."
    )
    src_group = ap.add_mutually_exclusive_group()
    src_group.add_argument("--image", metavar="PATH",
                           help="Local image file to upload and decompose.")
    src_group.add_argument("--image-url", metavar="URL",
                           help="Pre-hosted image URL (skips upload).")
    ap.add_argument("--output-dir", metavar="DIR", default=".",
                    help="Directory for manifest.json + layers/ (default: cwd).")
    ap.add_argument("--num-layers", type=int, default=4,
                    help="Number of layers (default: 4).")
    ap.add_argument("--steps", type=int, default=28,
                    help="Inference steps (default: 28).")
    ap.add_argument("--guidance", type=float, default=5.0,
                    help="Guidance scale (default: 5.0).")
    ap.add_argument("--format", default="PNG", choices=["PNG", "WEBP"],
                    help="Output image format: PNG | WEBP (default: PNG). "
                         "RGBA layers need alpha, so JPEG is not offered. Sent to "
                         "the model lowercased.")
    ap.add_argument("--seed", type=int, default=None,
                    help="Random seed for reproducibility.")
    ap.add_argument("--prompt", default=None,
                    help="Optional positive prompt.")
    ap.add_argument("--negative-prompt", default=None, dest="negative_prompt",
                    help="Optional negative prompt.")

    args = ap.parse_args(argv)
    output_dir = Path(args.output_dir).resolve()

    # Re-read .env fresh at the point of use so a FAL_KEY added after the
    # pipeline started is honored (point-of-use revalidation, not a cached
    # start-of-run verdict). os.environ wins, so an injected key is preserved.
    _load_env_file()

    # ── Fail-safe: no FAL_KEY ──────────────────────────────────────────────
    if not os.environ.get("FAL_KEY"):
        print(
            "decompose: FAL_KEY not set — decomposition skipped",
            file=sys.stderr,
        )
        _write_manifest(output_dir, {
            "tool": "decompose.py",
            "model": _MODEL,
            "source_image": args.image or args.image_url or "",
            "status": "skipped",
            "reason": "no_fal_key",
            "layers": [],
        })
        sys.exit(EXIT_SKIPPED)

    # ── OK path ────────────────────────────────────────────────────────────
    source_label = args.image or args.image_url or ""
    try:
        fal_client = _get_fal_client()

        # Upload local file if given; otherwise use the provided URL directly.
        if args.image:
            image_url = fal_client.upload_file(args.image)
        else:
            image_url = args.image_url

        arguments = _build_arguments(args, image_url)

        result = fal_client.subscribe(_MODEL, arguments=arguments)

        # Download each returned layer image to a temp dir atomically.
        # Only on FULL success do we move the temp dir to the final location.
        with tempfile.TemporaryDirectory() as _tmp:
            tmp_layers = Path(_tmp) / "layers"
            tmp_layers.mkdir()

            layer_entries = []
            for idx, img in enumerate(_get(result, "images", []) or []):
                fname = f"{idx:02d}.png"
                dest = tmp_layers / fname
                img_url = _get(img, "url")
                resp = requests.get(img_url, timeout=30)
                resp.raise_for_status()
                dest.write_bytes(resp.content)
                # Width/height not always in the response — default to 0.
                # Cast explicitly: a mock/absent value (CI) must not crash.
                try:
                    _w = _get(img, "width")
                    w = int(_w) if _w is not None else 0
                except (TypeError, ValueError):
                    w = 0
                try:
                    _h = _get(img, "height")
                    h = int(_h) if _h is not None else 0
                except (TypeError, ValueError):
                    h = 0
                layer_entries.append({
                    "index": idx,
                    "file": f"layers/{fname}",
                    "width": w,
                    "height": h,
                    "source_url": img_url or "",
                })

            # Atomic move: only fires when all downloads succeeded.
            final_layers = output_dir / "layers"
            if final_layers.exists():
                shutil.rmtree(final_layers)
            output_dir.mkdir(parents=True, exist_ok=True)
            shutil.copytree(str(tmp_layers), str(final_layers))

        manifest = {
            "tool": "decompose.py",
            "model": _MODEL,
            "source_image": source_label,
            "status": "ok",
            "layer_count": len(layer_entries),
            "seed": _get(result, "seed"),
            "has_nsfw_concepts": [bool(v) for v in (_get(result, "has_nsfw_concepts", []) or [])],
            "params": {
                "num_layers": args.num_layers,
                "num_inference_steps": args.steps,
                "guidance_scale": args.guidance,
                "output_format": args.format,
            },
            "cost_usd_estimate": _COST_USD_ESTIMATE,
            "layers": layer_entries,
        }
        _write_manifest(output_dir, manifest)
        print(
            f"decompose: ok — {len(layer_entries)} layer(s) written to "
            f"{output_dir}/layers/ (~${_COST_USD_ESTIMATE:.2f})",
            file=sys.stderr,
        )
        sys.exit(EXIT_OK)

    except Exception as exc:  # noqa: BLE001
        # Error path: write error manifest, ensure NO partial layers/ dir.
        layers_partial = output_dir / "layers"
        if layers_partial.exists():
            shutil.rmtree(layers_partial, ignore_errors=True)
        _write_manifest(output_dir, {
            "tool": "decompose.py",
            "model": _MODEL,
            "source_image": source_label,
            "status": "error",
            "reason": str(exc),
            "layers": [],
        })
        print(f"decompose: error — {exc}", file=sys.stderr)
        sys.exit(EXIT_ERROR)


if __name__ == "__main__":
    main()
