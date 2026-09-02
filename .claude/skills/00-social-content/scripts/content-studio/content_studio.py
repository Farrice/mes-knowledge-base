#!/usr/bin/env python3
"""Content Studio — a thin local-server wrapper around the existing carousel editor.

This is NOT a rewrite. It serves the editor that ``preview_editor.py`` already
generates (HTML/CSS/JS) **as-is** and adds a small server layer so the user can:

  * **Apply** edits live — ``/apply`` runs ``render_template.py --tweaks`` and returns
    the freshly baked PNG, killing the old export-file / paste-back loop.
  * **Save / load** edit state (``tweaks.json`` + ``comments.json``) to the run folder,
    so re-opening Content Studio restores the session.

Design constraints (Addendum 3 — "Content Studio", AIOS-139):
  * **Stdlib only** — ``http.server`` + ``webbrowser`` + ``subprocess``. ZERO new deps.
  * **Reuse the engine as-is** — ``preview_editor.build_editor_html`` for the UI and
    ``render_template.py --tweaks`` for the bake (RNDR-04 parity is inherited, not
    re-implemented: the server never touches the bake math).
  * **Auto-launch** — picks a free port and opens the browser; the user runs no command.
  * **Light** — ships inside the npm pack. The only client-side addition is a small
    injected ``studio.js`` shim that wires Save/Apply to the endpoints.
  * **SaaS-safe boundary** — all state goes through endpoints (``/apply``, ``/save``,
    ``/load``); nothing assumes a local filesystem on the client side.

Endpoints:
  GET  /            → the editor HTML (with the studio.js shim injected before </body>)
  GET  /studio.js   → the client shim (Save / Apply / Break-into-layers / Publish / status)
  GET  /healthz     → "ok" (readiness probe used by the launcher)
  GET  /load        → {tweaks, comments, hasZernioKey} read from the run folder (resume)
  GET  /slide-info  → {slides: {id: {is_full_ai}}} so the client gates the layers button
  POST /save        → {tweaks, comments} written to the run folder
  POST /apply       → {tweaks} → rebake affected slides via render_template --tweaks,
                      return [{slide, png(data-uri), ok, error}] for live swap-in
  POST /decompose   → {slide_id} → run decompose.py on a full-AI slide's PNG; return its
                      RGBA layers; fail-safe on missing FAL_KEY (status:"skipped")
  POST /ai-edit     → {slide, handle, provider, prompt, image(dataURI)} → run the
                      viz-image-gen edit script (GPT/Gemini) with the layer's current
                      image as --input-image; return {ok, png(dataURI)} for the modal
                      preview. Buttons are gated by key PRESENCE (values never leave
                      the server); Apply reuses the Replace-image imgSrc path.
  POST /post        → {platform?, accountId?, mode, scheduleFor?, pdf?, documentTitle?}
                      → thin wrapper over publish_rest.py; fail-safe on missing key

``/decompose`` (Qwen, FASE 2) decomposes a flat full-AI slide into editable RGBA layers
via ``00-social-content/scripts/gates/decompose.py``. ``/post`` (Zernio, FASE 3) is a thin
subprocess wrapper around ``tool-publisher/scripts/publish_rest.py`` — no REST rebuild.
Both fail safe (missing FAL_KEY / ZERNIO_API_KEY → HTTP 200 ok:false, never a crash).

Usage:
    python content_studio.py <run_folder> [--brand-context DIR] [--port N] [--no-open]
"""
from __future__ import annotations

import argparse
import base64
import json
import math
import os
import re
import shutil
import socket
import struct
import subprocess
import sys
import tempfile
import threading
import time
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

_SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_SCRIPT_DIR))

# Reuse the existing editor generator and run-folder introspection verbatim.
from preview_editor import (  # type: ignore[import]
    build_editor_html,
    _find_slides_info,
    _resolve_brand_context,
)

# render_template.py lives in the sibling viz-image-gen skill. _SCRIPT_DIR is
# .../skills/00-social-content/scripts/content-studio, so .parent.parent.parent
# reaches the skills root — one extra hop vs the old mkt-visual-identity/scripts home.
RENDER_TEMPLATE = (
    _SCRIPT_DIR.parent.parent.parent / "viz-image-gen" / "scripts" / "render_template.py"
)
# decompose.py lives in this skill's own scripts/gates/ dir (moved out of the
# shared mkt-visual-identity skill, which is now brand-identity-agnostic).
DECOMPOSE = (
    _SCRIPT_DIR.parent / "gates" / "decompose.py"
)
# Intentionally NOT asserted at import: a missing sibling skill must not take down
# the whole server (parity with RENDER_TEMPLATE / PUBLISH_REST, which fail-soft).
# /decompose validates DECOMPOSE at use time and returns a clean error.
# AI-edit generation scripts (studio-ai-edit) — siblings of render_template.py in
# the viz-image-gen skill, reused AS-IS (zero changes there). Same fail-soft rule:
# /ai-edit validates the script path at use time, never at import.
GEN_IMAGE_GPT = RENDER_TEMPLATE.parent / "generate_image_gpt.py"
GEN_IMAGE_GEMINI = RENDER_TEMPLATE.parent / "generate_image_gemini.py"
# publish_rest.py lives in the sibling tool-publisher skill (same hop count as
# RENDER_TEMPLATE: content-studio/ → scripts/ → 00-social-content/ → skills/ → skill root,
# then into tool-publisher/scripts/).
PUBLISH_REST = (
    _SCRIPT_DIR.parent.parent.parent / "tool-publisher" / "scripts" / "publish_rest.py"
)
# Vendored single-file Konva (UMD, no build) for the canvas overlay.
KONVA_JS = _SCRIPT_DIR / "vendor" / "konva.min.js"
# Vendored Zernio logo (tiny PNG) for the "Publish with Zernio" topbar CTA.
ZERNIO_LOGO = _SCRIPT_DIR / "vendor" / "zernio-logo.png"
# Vendored Agentic OS logo (hex-triad mark) for the command-centre topbar (FASE 5).
AGENTIC_LOGO = _SCRIPT_DIR / "vendor" / "agentic-logo.png"


_UNSET = object()


def _install_root() -> Path | None:
    """The project/install root: the parent of the ``.claude`` directory this
    script is installed under.

    In a real install the pack lives at
    ``<project>/.claude/skills/00-social-content/scripts/content-studio/``, so the
    project root (where the user's ``.env`` lives) is unambiguous from ``__file__``
    — independent of where the run folder sits and of the global ``~/.claude``.
    Returns None when running from the dev/source tree (no ``.claude`` ancestor).
    """
    for parent in _SCRIPT_DIR.parents:
        if parent.name == ".claude":
            return parent.parent
    return None


def _env_file(run: Path, install_root: object = _UNSET) -> Path | None:
    """Resolve the single ``.env`` for this run, bounded to the project root.

    Walks up from the run folder but NEVER above the install/project root, so a
    stray ``.env`` higher in the filesystem (the dev cwd, the user's home dir) is
    never picked up (AIOS-139 Addendum 9 #1). In a real install the run sits under
    the project, so run→root is walked and the project ``.env`` wins. In the
    dev/test tree there is no install root → only the run folder's own ``.env`` is
    considered, which keeps the fail-safe tests hermetic.

    ``install_root`` is injectable for tests: pass an explicit Path to simulate an
    install, or ``None`` to simulate the dev tree; the default computes it.
    """
    root = _install_root() if install_root is _UNSET else install_root
    run = run.resolve()
    chain = [run]
    if isinstance(root, Path):
        root = root.resolve()
        # Walk up only while still inside the project root (run→root inclusive).
        try:
            run.relative_to(root)
            inside = True
        except ValueError:
            inside = False
        if inside:
            for p in run.parents:
                chain.append(p)
                if p == root:
                    break
    for d in chain:
        env = d / ".env"
        if env.is_file():
            return env
    return None


def _env_key_value(run: Path, name: str) -> str | None:
    """Return the value of ``<name>=`` from the run's project-bounded ``.env``.

    Mirrors the find_env() + load_api_key() logic in publish_rest.py (the resolved
    ``.env`` is read; a file present without the key yields None) but bounds the
    walk to the install root so a credential from the dev/test cwd never leaks in.
    Never raises, so callers can present a clean fail-safe. This is the single
    per-run ``.env`` reader shared by every optional credential
    (ZERNIO_API_KEY, FAL_KEY, …).
    """
    env = _env_file(run)
    if env is None:
        return None
    prefix = name + "="
    try:
        for raw in env.read_text(encoding="utf-8", errors="replace").splitlines():
            line = raw.strip()
            if line.startswith(prefix):
                val = line.split("=", 1)[1].strip().strip('"').strip("'")
                return val or None
    except OSError:
        pass
    return None


def _zernio_key_present(run: Path) -> bool:
    """True if a ZERNIO_API_KEY is set in a .env walking up from ``run``."""
    return bool(_env_key_value(run, "ZERNIO_API_KEY"))


def _fal_key(run: Path) -> str | None:
    """Resolve FAL_KEY the same way as the Zernio key — the nearest ``.env``
    walking up from the run folder wins; fall back to an exported ``FAL_KEY`` in
    the process environment so a standalone ``decompose.py`` run still works.
    """
    return _env_key_value(run, "FAL_KEY") or os.environ.get("FAL_KEY")


# ── AI edit (studio-ai-edit) — provider registry + helpers ────────────────────
# Provider → the env key that gates it + the script that serves it + the label
# used in user-facing errors. Key NAMES are safe to surface; key VALUES never
# leave this server (not in responses, not in logs — see _scrub_key_values).
_AI_EDIT_PROVIDERS = {
    "gpt": {"key": "OPENAI_API_KEY", "label": "GPT"},
    "gemini": {"key": "GEMINI_API_KEY", "label": "Gemini"},
}

# Maximum number of input images (slot image [0] + extra references) each
# provider's edit endpoint accepts. GPT (gpt-image-1/2) takes up to 16; Gemini
# (Nano Banana Pro) up to 14. Over the cap → a clean 400 in /ai-edit, never a
# silent drop or a provider-side failure (ai-edit-multi-input MUST 4).
_AI_EDIT_IMAGE_CAP = {"gpt": 16, "gemini": 14}

# Output-geometry menus of the two scripts (generate_image_gpt.py accepts exactly
# three sizes in edit mode; generate_image_gemini.py mirrors its
# SUPPORTED_ASPECT_RATIOS). The edit keeps the layer's CURRENT aspect as close as
# possible: nearest candidate by |Δ log(aspect)| (symmetric for wide vs tall).
_AI_EDIT_GPT_SIZES = ("1024x1024", "1536x1024", "1024x1536")
_AI_EDIT_GEMINI_ASPECTS = (
    "1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9",
)


def _ai_edit_providers(run: Path) -> dict[str, bool]:
    """Presence-only availability of the AI-edit providers (studio-ai-edit).

    Same two sources the generation scripts honor, mirrored with the server's
    stdlib reader: the project-bounded ``.env`` walked up from ``run``
    (``_env_key_value`` — the hasFalKey precedent) OR an already-exported
    variable in ``os.environ`` (the scripts' python-dotenv load never overrides
    an existing env var, so an exported key wins there too). Only these booleans
    ever leave the function — key values never reach the client, a log or a
    response. Re-resolved on every editor build / request, so a key added
    mid-session is one F5 away (no restart).
    """
    return {
        prov: bool(_env_key_value(run, meta["key"]) or os.environ.get(meta["key"]))
        for prov, meta in _AI_EDIT_PROVIDERS.items()
    }


def _scrub_key_values(text: str, run: Path) -> str:
    """Belt-and-braces: strip any provider key VALUE that leaked into an error
    string (e.g. a provider echoing the credential back in a message) before it
    reaches a response. Key NAMES stay (they tell the user what to configure)."""
    out = text or ""
    for meta in _AI_EDIT_PROVIDERS.values():
        val = _env_key_value(run, meta["key"]) or os.environ.get(meta["key"])
        if val and val in out:
            out = out.replace(val, "***")
    return out


def _nearest_gpt_size(dims: tuple[int, int] | None) -> str:
    """The GPT size (of its 3 fixed WxH options) nearest the input's aspect.
    Unknown dims → square (generation still works; only the aspect choice
    degrades)."""
    if not dims:
        return "1024x1024"
    target = math.log(dims[0] / dims[1])

    def _dist(opt: str) -> float:
        w, h = opt.split("x")
        return abs(target - math.log(int(w) / int(h)))

    return min(_AI_EDIT_GPT_SIZES, key=_dist)


def _nearest_gemini_aspect(dims: tuple[int, int] | None) -> str:
    """The Gemini aspect ratio (of its supported set) nearest the input's aspect.
    Unknown dims → 1:1."""
    if not dims:
        return "1:1"
    target = math.log(dims[0] / dims[1])

    def _dist(opt: str) -> float:
        w, h = opt.split(":")
        return abs(target - math.log(int(w) / int(h)))

    return min(_AI_EDIT_GEMINI_ASPECTS, key=_dist)


# /ai-edit accepts ONLY a base64 image data URI — no path or URL resolution
# server-side, which kills the traversal/SSRF class by construction (spec MUST 4).
_IMAGE_DATA_URI_RE = re.compile(
    r"^data:image/(png|jpe?g|webp|gif);base64,([A-Za-z0-9+/=\s]+)$",
    re.IGNORECASE | re.DOTALL,
)


def _decode_image_data_uri(data_uri: str) -> tuple[bytes, str] | None:
    """Decode the /ai-edit image payload. Returns ``(bytes, ".ext")`` or None
    when the payload is not a valid base64 image data URI."""
    m = _IMAGE_DATA_URI_RE.match(data_uri or "")
    if not m:
        return None
    try:
        raw = base64.b64decode(m.group(2), validate=False)
    except (ValueError, base64.binascii.Error):  # type: ignore[attr-defined]
        return None
    if not raw:
        return None
    ext = m.group(1).lower()
    ext = "jpeg" if ext == "jpg" else ext
    return raw, "." + ext


def _jpeg_dimensions(path: Path) -> tuple[int, int] | None:
    """(width, height) from a JPEG's SOF frame header, stdlib-only.

    The client's canvas path always produces PNG, but the pass-through case (a
    layer already carrying a Replace-image data URI) can be JPEG — the aspect
    pick must still work there. Returns None on any malformed read."""
    try:
        with path.open("rb") as fh:
            if fh.read(2) != b"\xff\xd8":
                return None
            while True:
                b = fh.read(1)
                if not b:
                    return None
                if b != b"\xff":
                    continue
                marker = fh.read(1)
                while marker == b"\xff":
                    marker = fh.read(1)
                if not marker:
                    return None
                m = marker[0]
                if m == 0x01 or 0xD0 <= m <= 0xD9:
                    continue  # standalone markers carry no length segment
                seg = fh.read(2)
                if len(seg) < 2:
                    return None
                seglen = struct.unpack(">H", seg)[0]
                # SOF0..SOF15 minus DHT(C4)/JPG(C8)/DAC(CC) carry the frame dims.
                if 0xC0 <= m <= 0xCF and m not in (0xC4, 0xC8, 0xCC):
                    data = fh.read(5)
                    if len(data) < 5:
                        return None
                    h, w = struct.unpack(">HH", data[1:5])
                    return (int(w), int(h)) if w > 0 and h > 0 else None
                fh.seek(max(seglen - 2, 0), 1)
    except (OSError, struct.error):
        return None


def _image_dimensions(path: Path) -> tuple[int, int] | None:
    """Best-effort (width, height) of the AI-edit input (PNG / JPEG / GIF).

    None for anything else (e.g. WebP) — the caller then falls back to a square
    output: generation still works, only the aspect choice degrades."""
    try:
        with path.open("rb") as fh:
            head = fh.read(10)
    except OSError:
        return None
    if head.startswith(b"\x89PNG\r\n\x1a\n"):
        return _png_dimensions(path)
    if head.startswith(b"\xff\xd8"):
        return _jpeg_dimensions(path)
    if head[:6] in (b"GIF87a", b"GIF89a") and len(head) >= 10:
        w, h = struct.unpack("<HH", head[6:10])
        return (int(w), int(h)) if w > 0 and h > 0 else None
    return None


# Aspects within this relative tolerance are treated as "already matching" — the
# crop is then a no-op and the original bytes are preserved (no reencode, no
# quality loss). 0.5% absorbs integer-rounding of the provider's fixed sizes.
_AI_EDIT_ASPECT_TOL = 0.005


def _center_crop_to_aspect(png_path: Path, target_dims: tuple[int, int] | None) -> bool:
    """Center-crop the PNG at ``png_path`` (in place) to the aspect ratio of
    ``target_dims`` — cover semantics, NO stretching.

    The AI-edit providers emit one of their fixed sizes (1024², 1024×1536, …),
    which rarely matches the slot image being edited; the generated image then
    enters the canvas with the wrong footprint (the "veio maior" symptom). We
    crop the excess off the long axis, centered, so the result carries the
    slot's aspect while keeping the generated image's full (high) resolution on
    the short axis.

    No-op (returns False, bytes untouched) when:
      • ``target_dims`` is unknown (caller couldn't read input [0] dims), or
      • the aspects already match within ``_AI_EDIT_ASPECT_TOL`` — avoids a
        needless reencode / quality loss.

    Alpha is preserved: the image is processed in RGBA when it carries
    transparency (the transparent-routing path), so the crop never flattens it.
    Best-effort: any failure leaves the original file intact and returns False —
    a crop must never lose a generation that already succeeded.
    """
    if not target_dims:
        return False
    tw, th = target_dims
    if tw <= 0 or th <= 0:
        return False
    target_ar = tw / th
    try:
        from PIL import Image  # noqa: PLC0415 — optional, imported at use site
    except Exception:  # noqa: BLE001 — Pillow absent → skip the crop, keep output
        return False
    try:
        with Image.open(png_path) as im:
            w, h = im.size
            if w <= 0 or h <= 0:
                return False
            cur_ar = w / h
            # Already matching (within tolerance) → leave bytes as-is.
            if abs(cur_ar - target_ar) <= _AI_EDIT_ASPECT_TOL * target_ar:
                return False
            if cur_ar > target_ar:
                # Too wide → trim the sides, keep full height.
                new_w = max(1, round(h * target_ar))
                left = (w - new_w) // 2
                box = (left, 0, left + new_w, h)
            else:
                # Too tall → trim top/bottom, keep full width.
                new_h = max(1, round(w / target_ar))
                top = (h - new_h) // 2
                box = (0, top, w, top + new_h)
            # crop() preserves the source mode, so a transparent PNG stays RGBA
            # (alpha channel intact) and an opaque one keeps its RGB mode — no
            # flatten, no needless channel add.
            im.crop(box).save(png_path, format="PNG")
        return True
    except Exception:  # noqa: BLE001 — never lose a successful generation
        return False


def _next_ai_edit_output(run: Path, slide_id: str, handle: str, provider: str) -> Path:
    """Next free ``run/_ai_edits/<slide>-<handle>-<provider>-<NN>.png``.

    The audit trail of every generation — NEVER overwrites a previous one (NN
    increments). slide/handle come from the client, so they are reduced to a
    filename-safe token first (no separators survive → no traversal)."""
    def _safe(s: str) -> str:
        return re.sub(r"[^A-Za-z0-9_-]+", "-", str(s)).strip("-") or "x"

    adir = run / "_ai_edits"
    adir.mkdir(parents=True, exist_ok=True)
    stem = f"{_safe(slide_id)}-{_safe(handle)}-{_safe(provider)}"
    nn = 0
    while True:
        cand = adir / f"{stem}-{nn:02d}.png"
        if not cand.exists():
            return cand
        nn += 1


def _resolve_slot_image(info: dict, handle: str) -> Path | None:
    """For a templated slide, resolve the on-disk PNG of an image SLOT (e.g. the
    hero ``PHOTO_MAIN``) so the Magic Layer can decompose that specific image.
    Looks up ``data[handle]`` / ``data[handle+'_PATH']`` resolved against the slide
    dir. Returns None when the slot has no resolvable local image."""
    tdir = info.get("template_dir")
    if not tdir or not handle:
        return None
    tdir = Path(tdir)
    data = info.get("data") or {}
    handle = handle.upper()
    for key in (handle, handle + "_PATH", handle.replace("_PATH", "") + "_PATH"):
        cand = data.get(key)
        if isinstance(cand, str) and cand and not cand.startswith(("data:", "http://", "https://")):
            p = Path(cand)
            p = p if p.is_absolute() else (tdir / cand)
            if p.is_file():
                return p
    return None


def _resolve_hero_image(info: dict) -> Path | None:
    """The template's AI hero — the default Magic Layer source. Resolution order,
    robust to how a template names its hero file:
      1. the ``PHOTO_MAIN`` slot (a real post pins it), else
      2. the canonical ``_ai_bg/photo_main.png``, else
      3. the single ``_ai_bg/*.png`` when there is exactly one
         (e.g. ``numbered-body`` ships ``_ai_bg/bg.png``), else
      4. a conventional template-root ``bg.png``.
    Returns None only when the hero asset is genuinely absent (truly unwired)."""
    p = _resolve_slot_image(info, "PHOTO_MAIN")
    if p is not None:
        return p
    tdir = info.get("template_dir")
    if not tdir:
        return None
    tdir = Path(tdir)
    canonical = tdir / "_ai_bg" / "photo_main.png"
    if canonical.is_file():
        return canonical
    ai_bg = tdir / "_ai_bg"
    if ai_bg.is_dir():
        pngs = sorted(q for q in ai_bg.glob("*.png") if q.is_file())
        if len(pngs) == 1:
            return pngs[0]
    root_bg = tdir / "bg.png"
    return root_bg if root_bg.is_file() else None


def _clean_subprocess_error(text: str, *, what: str = "request") -> str:
    """Turn raw subprocess stderr into a clean, user-facing message (AIOS-139
    Addendum 9 #5 — never surface a Python traceback in the UI).

    A network read timeout escaped as ``TimeoutError: The read operation timed
    out`` (ssl ``recv_into``); map known patterns to friendly text and, for any
    other traceback, keep only the final ``ExceptionType: message`` line.
    """
    if not text:
        return f"{what} failed — please try again"
    low = text.lower()
    if "timed out" in low or "timeout" in low:
        return f"{what} timed out — check your connection and try again"
    if "ssl" in low and ("error" in low or "handshake" in low):
        return f"secure connection failed during {what} — please try again"
    if "name or service not known" in low or "getaddrinfo" in low or "connection refused" in low:
        return f"could not reach the server for {what} — check your connection"
    if "Traceback (most recent call last)" in text:
        # Collapse a stack trace to its final exception line (no file paths/frames).
        last = ""
        for line in text.strip().splitlines():
            s = line.strip()
            if s and not s.startswith(("File \"", "Traceback", "during handling")):
                last = s
        if ":" in last:
            last = last.split(":", 1)[1].strip() or last
        return f"{what} failed: {last[:160]}" if last else f"{what} failed — please try again"
    return text.strip()[-300:]


# ──────────────────────────────────────────────────────────────────────────
# Client shim — injected into the served editor. Pure vanilla JS, no deps.
# Wires the editor's existing tweaks/comments state (window.__getTweaks /
# window.__getComments, exposed by preview_editor.py) to the server endpoints.
# ──────────────────────────────────────────────────────────────────────────
STUDIO_JS = r"""
(function () {
  "use strict";
  // Only activate when served over http(s) by the studio server (not file://).
  if (location.protocol === "file:") return;

  function el(tag, attrs, kids) {
    var n = document.createElement(tag);
    attrs = attrs || {};
    Object.keys(attrs).forEach(function (k) {
      if (k === "style") n.setAttribute("style", attrs[k]);
      else if (k === "text") n.textContent = attrs[k];
      else n.setAttribute(k, attrs[k]);
    });
    (kids || []).forEach(function (c) { n.appendChild(c); });
    return n;
  }

  // ── Command-centre topbar styling (FASE 5) — injected so studio chrome is
  // self-contained. Pills mirror the command-centre nav-item: muted by default,
  // white pill + terracotta + soft shadow on hover/active. ─────────────────────
  (function injectCss() {
    var css =
      "#studio-bar{display:flex;align-items:center;gap:6px}" +
      ".cs-pill{border:none;background:transparent;color:#5E5E65;font:600 13px/1 'Hanken Grotesk',system-ui,sans-serif;" +
        "display:inline-flex;align-items:center;gap:7px;padding:8px 12px;border-radius:11px;cursor:pointer;" +
        "transition:background .15s,color .15s,box-shadow .15s}" +
      ".cs-pill:hover{color:#93452A;background:#fff;box-shadow:0 4px 12px rgba(147,69,42,.06)}" +
      ".cs-pill.on{color:#93452A;background:#fff;box-shadow:0 4px 12px rgba(147,69,42,.06)}" +
      // Comment mode armed — filled terracotta so it reads as an engaged toggle.
      // !important on background + an explicit :hover so the lower-specificity armed
      // state still wins over .cs-pill:hover (which would otherwise wash it white).
      ".cs-pill--on,.cs-pill--on:hover{color:#fff !important;" +
        "background:linear-gradient(135deg,#93452A 0%,#B25D3F 100%) !important;" +
        "box-shadow:0 6px 16px rgba(147,69,42,.22)}" +
      "body.cs-commenting .comment-stage,body.cs-commenting #comment-stage{cursor:crosshair}" +
      ".cs-pill-chev{font-size:10px;opacity:.7;margin-left:-2px}" +
      ".cs-cta{border:none;cursor:pointer;color:#fff;font:700 13px/1 'Hanken Grotesk',system-ui,sans-serif;" +
        "display:inline-flex;align-items:center;gap:8px;padding:9px 15px 9px 12px;border-radius:11px;" +
        "background:linear-gradient(135deg,#93452A 0%,#B25D3F 100%);box-shadow:0 6px 16px rgba(147,69,42,.22);" +
        "transition:filter .15s,box-shadow .15s}" +
      ".cs-cta:hover{filter:brightness(1.05);box-shadow:0 8px 22px rgba(147,69,42,.30)}" +
      ".cs-cta img{border-radius:5px;display:block}" +
      "#studio-status{position:fixed;left:50%;bottom:18px;transform:translateX(-50%);z-index:99999;" +
        "padding:9px 14px;border-radius:11px;background:rgba(27,28,27,.92);color:#FCF9F7;" +
        "font:500 13px 'Hanken Grotesk',system-ui,sans-serif;box-shadow:0 12px 32px rgba(27,28,27,.28);" +
        "max-width:520px;display:none}" +
      /* custom texture dropdown — readable on any bg */
      ".cs-pop{position:fixed;z-index:100000;width:260px;background:#fff;color:#1B1C1B;border-radius:14px;" +
        "padding:12px;box-shadow:0 18px 48px rgba(27,28,27,.22),0 0 0 1px rgba(27,28,27,.06);" +
        "font:500 13px 'Hanken Grotesk',system-ui,sans-serif;display:none}" +
      ".cs-pop h4{margin:2px 0 8px;font:700 10px/1 'Space Grotesk',sans-serif;letter-spacing:.12em;" +
        "text-transform:uppercase;color:#A29D94}" +
      ".cs-pop h4:not(:first-child){margin-top:14px}" +
      ".cs-opt{display:flex;align-items:center;gap:8px;width:100%;text-align:left;border:none;background:transparent;" +
        "padding:8px 9px;border-radius:9px;cursor:pointer;color:#1B1C1B;font:600 13px 'Hanken Grotesk',sans-serif}" +
      ".cs-opt:hover{background:#F4F2EE}" +
      ".cs-opt.sel{background:#ECEBFB;color:#4F52E0}" +
      ".cs-opt .sw{width:18px;height:18px;border-radius:5px;flex:none;background-size:cover;box-shadow:inset 0 0 0 1px rgba(0,0,0,.12)}" +
      ".cs-chips{display:flex;flex-wrap:wrap;gap:5px}" +
      ".cs-chip{border:1px solid #E7E4DF;background:#fff;color:#5E5E65;border-radius:8px;padding:5px 9px;" +
        "cursor:pointer;font:600 12px 'Hanken Grotesk',sans-serif}" +
      ".cs-chip.sel{background:#1B1C1B;color:#fff;border-color:#1B1C1B}" +
      ".cs-range{display:flex;align-items:center;gap:8px;margin-top:4px}" +
      ".cs-range input{flex:1}" +
      // ── Magic Layer loading overlay — covers the WHOLE studio (canvas + inspector
      // + topbar) so nothing is interactable while /decompose runs (~20s). A Scrapes
      // wordmark "walks" left↔right; a CSS spinner is the asset-free fallback. ──────
      "#cs-magic-overlay{position:fixed;inset:0;z-index:2147483600;display:none;" +
        "flex-direction:column;align-items:center;justify-content:center;gap:22px;" +
        "background:rgba(252,249,247,.93);backdrop-filter:blur(3px);" +
        "-webkit-backdrop-filter:blur(3px);cursor:wait}" +
      "#cs-magic-overlay.on{display:flex}" +
      ".cs-magic-logo{display:block;will-change:transform;" +
        "animation:cs-magic-walk 1.5s ease-in-out infinite alternate}" +
      "@keyframes cs-magic-walk{from{transform:translateX(-95px)}to{transform:translateX(95px)}}" +
      ".cs-magic-spin{width:54px;height:54px;border-radius:50%;border:5px solid rgba(147,69,42,.18);" +
        "border-top-color:#93452A;animation:cs-magic-spin .9s linear infinite}" +
      "@keyframes cs-magic-spin{to{transform:rotate(360deg)}}" +
      ".cs-magic-cap{font:600 15px/1.3 'Hanken Grotesk',system-ui,sans-serif;color:#5E5E65;" +
        "letter-spacing:.01em;text-align:center}";
    var s = document.createElement("style"); s.textContent = css; document.head.appendChild(s);
  })();

  // ── Action pills — left-clustered into the editor's #topbar-actions (logo left) ──
  function mkPill(label) {
    var b = document.createElement("button");
    b.type = "button"; b.className = "cs-pill"; b.textContent = label;
    return b;
  }
  // Edit/browse mode toggle WITHOUT the "free transform" jargon (label = the OTHER mode).
  var canvasBtn = mkPill("Browse");
  canvasBtn.title = "Switch between editing elements and swiping through slides";
  var addImageBtn = mkPill("Add image");
  var downloadBtn = mkPill("Download");
  var saveBtn = mkPill("Save");
  // Comment — an explicit MODE toggle (AIOS-139 Addendum 9 #4). Default OFF so the
  // caption + canvas stay directly editable; ON = clicking the stage drops a pin.
  var commentBtn = mkPill("Comment");
  commentBtn.title = "Toggle comment mode — when on, click the slide to leave a note";
  window.__commentMode = false;
  window.__firstComment = "";  // populated from /load; panel reads this on open
  commentBtn.addEventListener("click", function () {
    window.__commentMode = !window.__commentMode;
    commentBtn.classList.toggle("cs-pill--on", window.__commentMode);
    document.body.classList.toggle("cs-commenting", window.__commentMode);
    if (window.__setCommentMode) window.__setCommentMode(window.__commentMode);
    toast(window.__commentMode
      ? "Comment mode on — click the slide to leave a note"
      : "Comment mode off");
  });
  var texBtn = mkPill("Texture");
  texBtn.id = "tex-trigger";
  texBtn.innerHTML = 'Texture <span class="cs-pill-chev">&#9662;</span>';
  // Break-into-layers is the in-editor magic-pencil now — keep the element only for the
  // shared visibility/disable logic below; it is never shown in the topbar.
  var layersBtn = document.createElement("button");
  layersBtn.style.display = "none";
  // Publish with Zernio — terracotta CTA + vendored logo. ALWAYS enabled (FASE 5 §3).
  var publishBtn = document.createElement("button");
  publishBtn.type = "button"; publishBtn.className = "cs-cta";
  publishBtn.innerHTML =
    '<img src="/zernio-logo.png" alt="" width="17" height="17">Publish with Zernio';
  var status = el("span", { id: "studio-status" });

  // ── Template Studio chrome (only wired up in template mode) ─────────────
  var isTemplateMode = (window.__studioMode === "template");
  var approveBtn = null, compareBtn = null;
  // Per-template tweaks map: keyed by template_id so Approve NEVER sends
  // another template's tweaks. Populated as the conference loads each template.
  window.__tplTweaks = window.__tplTweaks || {};
  if (isTemplateMode) {
    approveBtn = document.createElement("button");
    approveBtn.type = "button"; approveBtn.className = "cs-cta";
    approveBtn.style.background = "linear-gradient(135deg,#4F52E0 0%,#6366f1 100%)";
    approveBtn.style.boxShadow = "0 6px 16px rgba(79,82,224,.22)";
    approveBtn.textContent = "Approve template";
    compareBtn = mkPill("Conference");
    compareBtn.id = "ts-compare-btn";
  }

  var closeStudioBtn = mkPill("Close Studio");
  closeStudioBtn.style.marginLeft = "auto";
  closeStudioBtn.style.color = "#aaa";
  closeStudioBtn.addEventListener("click", function() {
    fetch("/shutdown").then(function() { window.close(); }).catch(function() { window.close(); });
  });

  var host = document.getElementById("topbar-actions");
  if (!host) {  // standalone (no server topbar) fallback
    host = el("div", { id: "studio-bar", style: "position:fixed;top:12px;left:16px;z-index:99999;" });
    document.body.appendChild(host);
  }
  // Post mode: standard pill cluster + Publish CTA.
  // Template mode: same cluster minus Publish, plus Compare pill + Approve CTA.
  if (isTemplateMode) {
    [canvasBtn, addImageBtn, downloadBtn, saveBtn, commentBtn, texBtn, compareBtn, approveBtn, closeStudioBtn]
      .forEach(function (b) { host.appendChild(b); });
  } else {
    [canvasBtn, addImageBtn, downloadBtn, saveBtn, commentBtn, texBtn, publishBtn, closeStudioBtn]
      .forEach(function (b) { host.appendChild(b); });
  }
  document.body.appendChild(status);

  // ── Template Studio — hide social chrome + add "Template Studio" badge ───
  if (isTemplateMode) {
    (function hideSocialChrome() {
      [".li-head", ".li-caption", ".li-react", ".li-actions", "#comment-hint"].forEach(function (s) {
        Array.prototype.forEach.call(document.querySelectorAll(s), function (e) {
          e.style.display = "none";
        });
      });
      var brand = document.querySelector(".brand");
      if (brand && !brand.querySelector(".ts-badge")) {
        var badge = document.createElement("span");
        badge.className = "ts-badge";
        badge.textContent = "Template Studio";
        badge.style = "font:700 10px/1 'Space Grotesk',sans-serif;letter-spacing:.1em;" +
          "text-transform:uppercase;color:#4F52E0;background:#ECEBFB;border-radius:5px;" +
          "padding:3px 7px;margin-left:8px;vertical-align:middle;";
        brand.appendChild(badge);
      }
    })();

    // Fit the slide canvas entirely within the stage (no scrollbars). The base
    // editor pins .slide-frame at a fixed scale tied to the 440px social mock,
    // which overflows the template-mode stage. Here we resize the wrap to the
    // available viewport and recompute the frame scale. We resize the real layout
    // (not a transform over the top) so getBoundingClientRect/clientWidth — what
    // the pin/drag math reads — stay consistent. Template mode only.
    (function fitToViewport() {
      var raf = 0;
      function fit() {
        raf = 0;
        var stage = document.querySelector(".stage");
        var post = document.querySelector(".li-post");
        var wrap = document.querySelector(".slide-frame-wrap");
        var frame = document.querySelector(".slide-frame");
        var fullai = document.querySelector(".fullai-img");
        if (!stage) return;
        stage.style.overflow = "hidden";
        stage.style.padding = "16px";
        if (post) { post.style.width = "auto"; post.style.maxWidth = "none";
                    post.style.background = "transparent"; post.style.boxShadow = "none"; }
        var availW = stage.clientWidth - 32, availH = stage.clientHeight - 32;
        if (availW <= 0 || availH <= 0) return;
        var w = Math.min(availW, availH * 1080 / 1350), h = w * 1350 / 1080;
        if (wrap) { wrap.style.width = w + "px"; wrap.style.height = h + "px"; wrap.style.margin = "0 auto"; }
        if (frame) { frame.style.transformOrigin = "top left"; frame.style.transform = "scale(" + (w / 1080) + ")"; }
        if (fullai) { fullai.style.width = w + "px"; fullai.style.height = "auto"; }
        // Kill residual scrollbars and round corners around the canvas — the slide
        // is a hard-edged image, so the frame matches it (square, no chrome bar).
        [".li-post", ".li-viewer", ".slide-viewer", ".carousel-track", ".slide-frame-wrap"]
          .forEach(function (s) {
            var el = document.querySelector(s);
            if (el) { el.style.overflow = "hidden"; el.style.borderRadius = "0"; }
          });
        if (frame) frame.setAttribute("scrolling", "no");
      }
      function schedule() { if (!raf) raf = requestAnimationFrame(fit); }
      window.addEventListener("resize", schedule);
      var stage = document.querySelector(".stage");
      if (window.ResizeObserver && stage) { new ResizeObserver(schedule).observe(stage); }
      // The slide iframe/canvas mounts after first paint — re-fit as nodes are added
      // (childList only, so our own style writes don't re-trigger it).
      if (stage) { new MutationObserver(schedule).observe(stage, { childList: true, subtree: true }); }
      schedule(); setTimeout(fit, 80); setTimeout(fit, 350);
    })();

    // Main-screen template navigation: ‹ › arrows step through the pool and switch
    // the active editing template (no Conference needed). Kept inside the stage so
    // they don't overlap the right-hand panel. Switch = /select-template + reload.
    (function templateArrows() {
      var stage = document.querySelector(".stage");
      if (!stage) return;
      stage.style.position = "relative";
      var ids = [], curIdx = 0, ready = false;
      function go(dir) {
        if (!ready) return;
        if (window.__magicInFlight) return;  // locked while a decompose runs
        var j = curIdx + dir;
        if (j < 0 || j >= ids.length) return;
        // P0 #1: AUTOSAVE the current template's edits BEFORE switching so the
        // ‹ › swap is lossless. /select-template repoints state.run, so this /save
        // (which writes to the CURRENT state.run) MUST land first. The reload then
        // rehydrates tweaks.json into the editor (build_editor_html replays it).
        toast("Saving…");
        post("/save", { tweaks: getTweaks(), comments: getComments(),
                        caption: getCaption(), first_comment: getFirstComment() })
          .catch(function () { return null; })  // a save hiccup must not strand mid-pool
          .then(function () { return post("/select-template", { template_id: ids[j] }); })
          .then(function (s) {
            if (s && s.ok) window.location.reload();
          });
      }
      function arrow(side, label) {
        var b = document.createElement("button");
        b.id = "ts-arrow-" + side;
        b.textContent = label; b.type = "button";
        b.title = side === "left" ? "Previous template" : "Next template";
        b.style.cssText = "position:absolute;top:50%;transform:translateY(-50%);display:none;" +
          "z-index:30;width:40px;height:40px;border-radius:50%;border:none;cursor:pointer;" +
          "background:rgba(27,28,27,.82);color:#fff;font-size:22px;line-height:1;font-weight:400;" +
          "box-shadow:0 2px 10px rgba(0,0,0,.32);align-items:center;justify-content:center;";
        b.addEventListener("mouseenter", function () { b.style.background = "rgba(27,28,27,.96)"; });
        b.addEventListener("mouseleave", function () { b.style.background = "rgba(27,28,27,.82)"; });
        b.addEventListener("click", function () { go(side === "left" ? -1 : 1); });
        return b;
      }
      var L = arrow("left", "‹"), R = arrow("right", "›");
      stage.appendChild(L); stage.appendChild(R);
      // P2 #17: small "i / N" position pill so the user can tell pool size/position
      // (the bare arrows only say "there's more this way"). Populated from the same
      // /pool-templates fetch as the arrows; hidden for a single-template pool.
      var counter = document.createElement("div");
      counter.id = "ts-tpl-counter";
      counter.style.cssText = "position:absolute;top:10px;left:50%;transform:translateX(-50%);" +
        "display:none;z-index:30;padding:3px 10px;border-radius:999px;" +
        "background:rgba(27,28,27,.82);color:#fff;font-size:12px;line-height:1.4;" +
        "font-weight:600;letter-spacing:.02em;box-shadow:0 2px 10px rgba(0,0,0,.32);" +
        "pointer-events:none;font-variant-numeric:tabular-nums;";
      stage.appendChild(counter);
      function updateCounter() {
        if (ready && ids.length > 1) {
          counter.textContent = (curIdx + 1) + " / " + ids.length;
          counter.style.display = "block";
        } else {
          counter.style.display = "none";
        }
      }
      // Sit the arrows just inside the canvas edges (not the far stage edges), and
      // only show one when there's actually a template on that side.
      function reposition() {
        var wrap = stage.querySelector(".slide-frame-wrap") || stage.querySelector(".li-post");
        if (!wrap) return;
        var sr = stage.getBoundingClientRect(), wr = wrap.getBoundingClientRect();
        L.style.left = Math.max(8, (wr.left - sr.left) + 10) + "px";
        R.style.right = Math.max(8, (sr.right - wr.right) + 10) + "px";
      }
      function applyVisibility() {
        if (!ready) return;
        L.style.display = (curIdx > 0) ? "flex" : "none";
        R.style.display = (curIdx < ids.length - 1) ? "flex" : "none";
        updateCounter();
        reposition();
      }
      // §5 (work-through-the-queue): the front shows ONLY templates still needing
      // work. Filter out any whose manifest marks them approved:true so the ‹ › arrows
      // + "i / N" counter reflect the remaining count. When none remain, show an
      // "All templates approved" state instead of an empty/broken nav.
      var allApprovedEl = null;
      function showAllApproved() {
        ready = false;
        L.style.display = "none"; R.style.display = "none";
        counter.style.display = "none";
        if (!allApprovedEl) {
          allApprovedEl = document.createElement("div");
          allApprovedEl.id = "ts-all-approved";
          allApprovedEl.style.cssText = "position:absolute;inset:0;z-index:25;display:flex;" +
            "flex-direction:column;align-items:center;justify-content:center;gap:8px;" +
            "background:rgba(252,249,247,.96);color:#1B1C1B;text-align:center;padding:24px;";
          allApprovedEl.innerHTML =
            '<div style="font:700 22px/1.2 \'Space Grotesk\',system-ui,sans-serif">' +
              'All templates approved</div>' +
            '<div style="font:500 14px/1.4 \'Hanken Grotesk\',system-ui,sans-serif;color:#5E5E65">' +
              'Nothing left to review — you can download or close the studio.</div>';
          stage.appendChild(allApprovedEl);
        }
        allApprovedEl.style.display = "flex";
      }

      fetch("/pool-templates").then(function (r) { return r.json(); }).then(function (res) {
        if (!res || !res.ok || !res.templates) return;
        var pending = res.templates.filter(function (t) { return !t.approved; });
        if (!pending.length) { showAllApproved(); return; }
        ids = pending.map(function (t) { return t.id; });
        curIdx = ids.indexOf(res.active);
        if (curIdx < 0) curIdx = 0;  // active may have just been approved → land on first pending
        ready = true;
        applyVisibility();
      }).catch(function () {});

      // §5: called by the Approve handlers after a successful /approve. Removes the
      // approved id from the front's nav and advances to the next pending template
      // (via /select-template + reload). If none remain, shows the all-approved state.
      window.__tplNav = window.__tplNav || {};
      window.__tplNav.advanceAfterApprove = function (approvedId) {
        if (approvedId == null) approvedId = ids[curIdx];  // default: current front template
        var i = ids.indexOf(approvedId);
        if (i >= 0) ids.splice(i, 1);
        if (!ids.length) { showAllApproved(); return; }
        // Prefer the template that now occupies the approved slot (next in queue),
        // else step back to the new last one.
        var nextIdx = Math.min(i < 0 ? curIdx : i, ids.length - 1);
        if (nextIdx < 0) nextIdx = 0;
        post("/select-template", { template_id: ids[nextIdx] }).then(function (s) {
          if (s && s.ok) window.location.reload();
          else { curIdx = nextIdx; applyVisibility(); }
        }).catch(function () { curIdx = nextIdx; applyVisibility(); });
      };

      window.addEventListener("resize", reposition);
      if (window.ResizeObserver) { new ResizeObserver(reposition).observe(stage); }
      setTimeout(applyVisibility, 120); setTimeout(applyVisibility, 400);
    })();
  }

  function toast(msg, isErr) {
    status.style.display = "inline-block";
    status.style.background = isErr ? "rgba(150,30,30,.94)" : "rgba(27,28,27,.92)";
    status.textContent = msg;
    if (toast._t) clearTimeout(toast._t);
    toast._t = setTimeout(function () { status.style.display = "none"; }, 6000);
  }

  function getTweaks() { return (window.__getTweaks && window.__getTweaks()) || {}; }
  function getComments() { return (window.__getComments && window.__getComments()) || {}; }

  function post(path, body) {
    return fetch(path, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    }).then(function (r) { return r.json(); });
  }

  // ── Magic Layer loading overlay + in-flight lock (PRD: magic-layer-ux) ──────
  // While /decompose runs (~20s) a blocking overlay covers the WHOLE studio so
  // nothing is interactable, and window.__magicInFlight makes a second Magic Layer /
  // Apply / arrow-nav a no-op. The logo is the SAME header logo (/agentic-logo.png,
  // served by the studio); if it ever fails to load (onerror) we reveal the CSS
  // spinner element beside it as the asset-free fallback.
  window.__magicInFlight = false;
  var _magicOverlay = null;
  function ensureMagicOverlay() {
    if (_magicOverlay) return _magicOverlay;
    var o = document.createElement("div");
    o.id = "cs-magic-overlay";
    o.setAttribute("role", "status");
    o.setAttribute("aria-live", "polite");
    o.innerHTML =
      '<img class="cs-magic-logo" src="/agentic-logo.png" alt="Agentic OS" ' +
        'style="height:56px;width:auto"' +
        // If the logo asset fails, swap to the asset-free CSS spinner so the
        // overlay still shows clear motion.
        ' onerror="this.style.display=\'none\';' +
          'var s=this.parentNode.querySelector(\'.cs-magic-spin\');' +
          'if(s)s.style.display=\'block\';">' +
      '<div class="cs-magic-spin" aria-hidden="true" ' +
        'style="display:none"></div>' +
      '<div class="cs-magic-cap">Please wait… generating layers</div>';
    // Swallow every interaction while shown — belt-and-suspenders to __magicInFlight.
    ["click", "mousedown", "mouseup", "dblclick", "wheel", "keydown", "touchstart"]
      .forEach(function (ev) {
        o.addEventListener(ev, function (e) {
          e.stopPropagation();
          if (ev !== "wheel" && ev !== "touchstart") e.preventDefault();
        }, { capture: true });
      });
    (document.body || document.documentElement).appendChild(o);
    _magicOverlay = o;
    return o;
  }
  function showMagicOverlay() { ensureMagicOverlay().classList.add("on"); }
  function hideMagicOverlay() { if (_magicOverlay) _magicOverlay.classList.remove("on"); }

  // Implicit bake (FASE 5 §1): there is no "Apply" — Download/Publish bake the affected
  // slides on demand so the exported media are the full live composites (RNDR-04). Writes
  // slide-<NN>.png in the run folder. Resolves true on success.
  function bakeNow() {
    // Apply/bake is a no-op while a decompose is in flight (the overlay also blocks
    // the click; this guards the Download/Publish programmatic callers).
    if (window.__magicInFlight) {
      toast("Please wait — generating layers…", true);
      return Promise.resolve(false);
    }
    var tw = getTweaks();
    return post("/apply", { tweaks: tw }).then(function (res) {
      if (!res || !res.ok) return false;
      var failed = (res.results || []).filter(function (r) { return !r.ok; });
      if (failed.length) {
        toast("Some slides could not bake: " +
          failed.map(function (r) { return r.slide; }).join(", "), true);
      }
      return true;
    }).catch(function () { return false; });
  }

  // ── Free-transform (Konva canvas) toggle — label de-jargoned (Browse/Edit) ──
  window.__studioCanvasOn = true;
  canvasBtn.classList.add("on");
  canvasBtn.addEventListener("click", function () {
    window.__studioCanvasOn = !window.__studioCanvasOn;
    canvasBtn.textContent = window.__studioCanvasOn ? "Browse" : "Edit";
    canvasBtn.classList.toggle("on", window.__studioCanvasOn);
    if (window.__studioCanvas) {
      if (window.__studioCanvasOn) window.__studioCanvas.enable();
      else window.__studioCanvas.disable();
    }
  });

  // ── Download — implicit bake → zip the full composites (FASE 5 §1+§2) ──────
  downloadBtn.addEventListener("click", function () {
    toast("Baking slides…");
    downloadBtn.classList.add("on");
    bakeNow().then(function () {
      downloadBtn.classList.remove("on");
      toast("Downloading slides.zip…");
      window.location.href = "/download";
    });
  });

  // ── Load Konva (vendored) then the canvas overlay ─────────────
  function loadScript(src, cb) {
    var s = document.createElement("script");
    s.src = src; s.onload = cb;
    s.onerror = function () { toast("Could not load " + src + " — canvas disabled (panel editing still works).", true); };
    document.head.appendChild(s);
  }
  loadScript("/konva.min.js", function () { loadScript("/canvas.js", function () {}); });

  function getCaption() { return (window.__getCaption && window.__getCaption()) || ""; }
  function getFirstComment() { return window.__firstComment || ""; }

  // ── Save state (tweaks + comments + caption + first_comment) ─────────────
  saveBtn.addEventListener("click", function () {
    toast("Saving…");
    post("/save", { tweaks: getTweaks(), comments: getComments(), caption: getCaption(),
                    first_comment: getFirstComment() })
      .then(function (res) {
        if (res.ok) toast("Saved to the run folder" + (res.nComments ? " (incl. comments)" : "") + ".");
        else toast("Save failed: " + (res.error || "?"), true);
      })
      .catch(function (e) { toast("Save error: " + e, true); });
  });

  // ── Editable caption (FASE 6 §5) — persist to caption.md on blur so the edited
  // caption is what Zernio publishes. caption.md is read back at load → survives refresh.
  var capEl = document.getElementById("li-caption");
  if (capEl) {
    capEl.addEventListener("blur", function () {
      post("/save-caption", { caption: getCaption() })
        .then(function (res) { if (res && res.ok) toast("Caption saved."); })
        .catch(function () {});
    });
  }

  // ── Texture — GLOBAL topbar control with a readable custom dropdown (§4+§5) ──
  var texPop = null, texState = { name: "", blend: "multiply", intensity: 0.55 };
  var TEX = window.__TEXTURES || {};
  var BLENDS = [["multiply", "Multiply"], ["overlay", "Overlay"], ["screen", "Screen"],
                ["soft-light", "Soft light"], ["darken", "Darken"], ["normal", "Normal"]];

  function pushTexture() {
    var sid = window.__activeSlide;
    if (sid && window.__setTexture) {
      window.__setTexture(sid, texState.name, texState.blend, texState.intensity);
    }
    texBtn.classList.toggle("on", !!texState.name);
  }
  function syncTextureFromSlide() {
    var sid = window.__activeSlide;
    var cur = (sid && window.__getTexture) ? window.__getTexture(sid) : null;
    texState = cur ? { name: cur.name, blend: cur.blend, intensity: cur.intensity }
                   : { name: "", blend: "multiply", intensity: 0.55 };
    texBtn.classList.toggle("on", !!texState.name);
    if (texPop) renderTexPop();
  }
  function renderTexPop() {
    if (!texPop) return;
    texPop.innerHTML = "";
    var h1 = document.createElement("h4"); h1.textContent = "Texture overlay"; texPop.appendChild(h1);
    function opt(name, label, uri) {
      var b = document.createElement("button");
      b.className = "cs-opt" + (texState.name === name ? " sel" : "");
      var sw = document.createElement("span"); sw.className = "sw";
      if (uri) sw.style.backgroundImage = "url(" + uri + ")"; else sw.style.background = "#E7E4DF";
      var t = document.createElement("span"); t.textContent = label;
      b.appendChild(sw); b.appendChild(t);
      b.onclick = function () { texState.name = name; pushTexture(); renderTexPop(); };
      texPop.appendChild(b);
    }
    opt("", "None", "");
    Object.keys(TEX).forEach(function (n) { opt(n, TEX[n].label || n, TEX[n].uri); });
    var h2 = document.createElement("h4"); h2.textContent = "Blend"; texPop.appendChild(h2);
    var chips = document.createElement("div"); chips.className = "cs-chips";
    BLENDS.forEach(function (bl) {
      var c = document.createElement("button");
      c.className = "cs-chip" + (texState.blend === bl[0] ? " sel" : "");
      c.textContent = bl[1];
      c.onclick = function () { texState.blend = bl[0]; pushTexture(); renderTexPop(); };
      chips.appendChild(c);
    });
    texPop.appendChild(chips);
    var h3 = document.createElement("h4"); h3.textContent = "Intensity"; texPop.appendChild(h3);
    var row = document.createElement("div"); row.className = "cs-range";
    var r = document.createElement("input");
    r.type = "range"; r.min = "0"; r.max = "100"; r.value = String(Math.round(texState.intensity * 100));
    var val = document.createElement("span"); val.textContent = r.value + "%";
    r.oninput = function () { texState.intensity = parseFloat(r.value) / 100; val.textContent = r.value + "%"; pushTexture(); };
    row.appendChild(r); row.appendChild(val); texPop.appendChild(row);
  }
  function toggleTexPop() {
    if (texPop) { texPop.remove(); texPop = null; return; }
    texPop = document.createElement("div"); texPop.className = "cs-pop";
    document.body.appendChild(texPop);
    var rb = texBtn.getBoundingClientRect();
    texPop.style.left = Math.round(rb.left) + "px";
    texPop.style.top = Math.round(rb.bottom + 8) + "px";
    texPop.style.display = "block";
    syncTextureFromSlide();
    renderTexPop();
  }
  texBtn.addEventListener("click", function (e) { e.stopPropagation(); toggleTexPop(); });
  document.addEventListener("click", function (e) {
    if (texPop && !texPop.contains(e.target) && e.target !== texBtn) { texPop.remove(); texPop = null; }
  });

  // ── Magic Layer — "Break into layers" button (FASE 2) ────────────────────
  // Show/hide based on whether the active slide is full-AI (no template_dir).
  // Fetches /slide-info once on load; updates on every slide change.
  var fullAiSlides = {};  // {slide_id: bool}
  var hasFalKey = false;  // informational only (from /slide-info); the Magic Layer
                          // buttons are NOT gated on it — the key is checked at use time.
  var decomposableHero = {};  // {sid: true} templated slides with a baked-text AI hero
  function updateLayersBtnVisibility() {
    var sid = window.__activeSlide;
    var isFullAi = !!(sid && fullAiSlides[sid]);
    window.__activeSlideIsFullAI = isFullAi;
    // The global top-bar button stays for FULL-AI slides (the whole slide is one
    // image). Templated slides decompose per-image via the "Magic Layer" button
    // injected into each image control-group (see injectMagicButtons).
    layersBtn.style.display = isFullAi ? "inline-block" : "none";
    layersBtn.textContent = "Magic Layer";
    if (isFullAi) {
      // Always clickable (like Publish/Zernio) — the FAL key is checked at USE time,
      // not gated on load. /decompose fail-safes + toasts if the key is missing.
      layersBtn.disabled = false;
      layersBtn.style.opacity = "1";
      layersBtn.title = "Break this image into editable layers.";
    }
  }
  // Fetch slide info once on load.
  fetch("/slide-info").then(function (r) { return r.json(); }).then(function (res) {
    if (res && res.ok && res.slides) {
      Object.keys(res.slides).forEach(function (sid) {
        fullAiSlides[sid] = !!(res.slides[sid] && res.slides[sid].is_full_ai);
        decomposableHero[sid] = !!(res.slides[sid] && res.slides[sid].decomposable_hero);
      });
    }
    if (res) hasFalKey = !!res.hasFalKey;
    // AI-edit provider presence (layer-image-ai-edit): the same {gpt,gemini}
    // booleans the server-rendered image groups use, so a LAYER_NN's injected
    // group can offer Edit-with-AI for exactly the available providers.
    if (res && res.aiEditProviders) window.__aiEditProviders = res.aiEditProviders;
    updateLayersBtnVisibility();
    // hasFalKey just resolved — refresh the per-image Magic Layer buttons so any
    // injected before this fetch returned get enabled (template mode).
    if (window.__injectMagicButtons) window.__injectMagicButtons();
  }).catch(function () {});
  window.__decomposableHero = decomposableHero;
  // Hook into slide navigation (preview_editor.py exposes __onSlideChange).
  var _origOnSlideChange = window.__onSlideChange;
  window.__onSlideChange = function (activeId) {
    if (_origOnSlideChange) _origOnSlideChange(activeId);
    updateLayersBtnVisibility();
  };

  // ── Shared layer-asset machinery (§2 + §3) ───────────────────────────────
  // Both "Break into layers" (decompose) and "Add image" drop a LAYER_NN asset
  // through the SAME three client steps, so the live DOM matches the bake DOM
  // byte-for-byte (RNDR-04): inject the EXACT <img data-slot> markup
  // render_template._materialize_layers emits, seed __SLOT_BBOXES, add a layer row.

  function frameDoc(sid) {
    var f = document.getElementById("frame-" + sid);
    if (!f) return null;
    try { return f.contentDocument || (f.contentWindow && f.contentWindow.document); }
    catch (e) { return null; }
  }

  // Promote a full-AI slide's flat <img class="fullai-img"> viewer into an
  // iframe-backed layer canvas: a <div class="slide"> with the original PNG as the
  // BACKGROUND, mirroring the synthesized BAKE template (content_studio
  // _ensure_layer_canvas_template) so preview == bake. Idempotent: if an iframe
  // for this slide already exists, do nothing.
  function promoteToLayerCanvas(sid) {
    if (document.getElementById("frame-" + sid)) return true;
    var viewer = document.querySelector('.slide-viewer[data-slide="' + sid + '"]');
    if (!viewer) return false;
    var img = viewer.querySelector("img.fullai-img");
    var bgUri = img ? img.getAttribute("src") : "";
    // Size the layer-canvas wrap to the ORIGINAL image's aspect (mirrors how the
    // flat fullai-img displayed at 555×auto, and matches the bake which runs at the
    // PNG's native resolution). Replacing the viewer's innerHTML drops the img that
    // gave the wrap its height, so we must set an explicit px height — height:100%
    // would collapse against the height-less .slide-viewer (black/clipped preview).
    var nw = (img && img.naturalWidth) || 1080;
    var nh = (img && img.naturalHeight) || 1350;
    // Size the promoted layer canvas to MATCH the slide as currently DISPLAYED.
    // The editor canvas is fit-to-viewport (fitToViewport sizes .slide-frame-wrap /
    // .fullai-img to the available stage), so the old hardcoded 555 shrank the
    // layers area. Read the current displayed width (the fitted wrap, else the flat
    // image's rendered box) and derive height from the image's native aspect; fall
    // back to 555 only when nothing measurable exists yet.
    var wrapW = 0;
    var existingWrap = (viewer.querySelector(".slide-frame-wrap")) ||
                       (img && (document.querySelector(".slide-frame-wrap")));
    if (existingWrap && existingWrap.clientWidth) wrapW = existingWrap.clientWidth;
    if (!wrapW && img) {
      var ir = img.getBoundingClientRect();
      if (ir && ir.width) wrapW = Math.round(ir.width);
    }
    if (!wrapW) wrapW = 555;
    var wrapH = Math.round(wrapW * nh / nw);
    var srcdoc =
      "<!doctype html><html><head><meta charset='utf-8'>" +
      // html,body MUST be height:100% or the height:100% .slide collapses to 0
      // and the absolutely-positioned layers get clipped (black preview) — the
      // bake sizes its own container, so this only bit the live promote path.
      "<style>html,body{margin:0;padding:0;height:100%}" +
      ".slide{position:relative;width:100%;height:100%;overflow:hidden}</style>" +
      "</head><body>" +
      "<div class=\"slide\" style=\"position:relative;width:100%;height:100%\">" +
      // Recolorable solid colour FLOOR (AIOS-139 Bug 2) — BYTE-IDENTICAL to the bake's
      // _ensure_layer_canvas_template floor so preview == PNG (RNDR-04). Lowest z-index
      // (0, first child), default transparent: hiding the BACKGROUND image above it
      // reveals this floor, and BGFILL bgColor recolours it.
      "<div data-slot=\"BGFILL\" " +
      "style=\"position:absolute;inset:0;background:transparent;z-index:0\"></div>" +
      "<img data-slot=\"BACKGROUND\" src=\"" + bgUri + "\" " +
      "style=\"position:absolute;inset:0;width:100%;height:100%;object-fit:fill;z-index:1\">" +
      "</div></body></html>";
    viewer.innerHTML =
      '<div class="slide-frame-wrap" style="position:relative;width:' + wrapW +
      'px;height:' + wrapH + 'px;overflow:hidden">' +
      '<iframe id="frame-' + sid + '" ' +
      'style="width:100%;height:100%;border:0;display:block" ' +
      'sandbox="allow-scripts allow-same-origin"></iframe>' +
      '</div>';
    var f = document.getElementById("frame-" + sid);
    if (f) f.srcdoc = srcdoc;
    // The slide is no longer read-only — drop the cached fullAI flag so canvas /
    // applyToSlide treat it like a templated slide from here on.
    fullAiSlides[sid] = false;
    window.__activeSlideIsFullAI = false;
    // Expose the recolorable colour FLOOR control (AIOS-139 Bug 2): the srcdoc above
    // carries a BGFILL floor beneath the BACKGROUND image, so wire its Fill + row so
    // the user can recolour it and hiding the image reveals it.
    buildBgFillControlGroup(sid);
    return true;
  }
  window.__promoteToLayerCanvas = promoteToLayerCanvas;

  // Next free LAYER_NN index for a slide (scans both the live tweaks and any
  // already-present layer rows so decompose + add-image never collide).
  function nextLayerHandle(sid) {
    var max = -1, tw = getTweaks()[sid] || {};
    Object.keys(tw).forEach(function (k) {
      var m = /^LAYER_(\d+)$/.exec(k); if (m) max = Math.max(max, parseInt(m[1], 10));
    });
    var panel = document.querySelector('.slide-panel[data-slide="' + sid + '"]');
    if (panel) panel.querySelectorAll('.layer-row[data-handle^="LAYER_"]').forEach(function (r) {
      var m = /^LAYER_(\d+)$/.exec(r.getAttribute("data-handle"));
      if (m) max = Math.max(max, parseInt(m[1], 10));
    });
    return "LAYER_" + ("0" + (max + 1)).slice(-2);
  }
  window.__nextLayerHandle = nextLayerHandle;

  // Inject the live <img data-slot="LAYER_NN"> into the slide iframe (matching the
  // bake markup), seed __SLOT_BBOXES[sid], append a .layer-row, and drive the
  // initial geometry through applyToSlide so the live element is positioned exactly
  // as the bake will position it. geom = {x,y,w,h,opacity,tilt}. Returns the handle.
  function addLayerAsset(sid, handle, dataUri, geom) {
    geom = geom || {};
    var g = {
      x: geom.x != null ? geom.x : 0, y: geom.y != null ? geom.y : 0,
      w: geom.w != null ? geom.w : 100, h: geom.h != null ? geom.h : 100,
      opacity: geom.opacity != null ? geom.opacity : 1,
      tilt: geom.tilt != null ? geom.tilt : 0,
    };
    // 1) record the tweak entry (img + geometry) — this is what bakes.
    var tw = getTweaks();
    tw[sid] = tw[sid] || {};
    tw[sid][handle] = { img: dataUri, x: g.x, y: g.y, w: g.w, h: g.h, opacity: g.opacity, tilt: g.tilt };

    // 2) inject the live <img> — BYTE-IDENTICAL to _materialize_layers (RNDR-04):
    //    <img data-slot="LAYER_NN" src="<uri>" style="position:absolute;max-width:none;" />
    var doc = frameDoc(sid);
    if (doc) {
      var slide = doc.querySelector(".slide") || doc.body;
      if (slide && !doc.querySelector('[data-slot="' + handle + '"]')) {
        var holder = doc.createElement("div");
        holder.innerHTML = '<img data-slot="' + handle + '" src="' + dataUri +
          '" style="position:absolute;max-width:none;" />';
        slide.appendChild(holder.firstChild);
      }
    }

    // 3) seed __SLOT_BBOXES so the Konva canvas draws a transformable rect for it.
    window.__SLOT_BBOXES = window.__SLOT_BBOXES || {};
    window.__SLOT_BBOXES[sid] = window.__SLOT_BBOXES[sid] || [];
    var bb = window.__SLOT_BBOXES[sid];
    var existing = null;
    bb.forEach(function (e) { if (e.handle === handle) existing = e; });
    if (existing) { existing.x = g.x; existing.y = g.y; existing.w = g.w; existing.h = g.h; }
    else bb.push({ handle: handle, x: g.x, y: g.y, w: g.w, h: g.h });

    // 4) drive the live element's geometry through applyToSlide (same path the
    //    panel + canvas use) so preview position == bake position.
    if (window.applyToSlide) {
      window.applyToSlide(sid, handle, "x", g.x);
      window.applyToSlide(sid, handle, "y", g.y);
      window.applyToSlide(sid, handle, "w", g.w);
      window.applyToSlide(sid, handle, "opacity", g.opacity);
      window.applyToSlide(sid, handle, "tilt", g.tilt);
    }

    // 5) append a .layer-row so the Layers panel can select/lock/hide/remove it,
    //    and an inspector control-group so it is editable from the PANEL (§3).
    addLayerRow(sid, handle);
    buildImageControlGroup(sid, handle, g);
    return handle;
  }
  window.__addLayerAsset = addLayerAsset;

  // Append a Layers-panel row for an asset handle (mirrors _build_layers_list's
  // markup: grip + image icon + name + lock + eye). No-op if it exists.
  function addLayerRow(sid, handle) {
    var list = document.querySelector('.layers-list[data-slide="' + sid + '"]');
    if (!list) return;
    if (list.querySelector('.layer-row[data-handle="' + handle + '"]')) return;
    var hint = list.querySelector(".no-slots");
    if (hint) hint.remove();
    var row = document.createElement("div");
    row.className = "layer-row";
    row.setAttribute("draggable", "true");
    row.setAttribute("data-slide", sid);
    row.setAttribute("data-handle", handle);
    row.setAttribute("data-locked", "0");
    row.setAttribute("onclick", "selectZone('" + sid + "','" + handle + "')");
    row.innerHTML =
      '<span class="layer-grip" aria-hidden="true">&#8942;&#8942;</span>' +
      '<span class="layer-ico"></span>' +
      '<span class="layer-name">' + handle + '</span>' +
      '<span class="layer-actions">' +
      '<button type="button" class="actbtn actbtn--lk" data-on="0" aria-label="lock layer" ' +
      'onclick="event.stopPropagation();if(window.toggleLock)toggleLock(\'' + sid + '\',\'' + handle + '\',this)">L</button>' +
      '<button type="button" class="actbtn layer-eye" data-on="1" aria-label="toggle visibility" ' +
      'onclick="event.stopPropagation();if(window.toggleVisible)toggleVisible(\'' + sid + '\',\'' + handle + '\',this)">&#128065;</button>' +
      // FASE 6 §3: no per-layer trash/delete affordance (eye/hide is enough).
      '</span>';
    list.insertBefore(row, list.firstChild);  // front-most on top (matches _build_layers_list)
  }
  window.__addLayerRow = addLayerRow;

  // Inject an inspector control-group for an asset layer (add-image / decompose) so it
  // is editable from the PANEL — X/Y/W + opacity — like any introspected zone, not only
  // draggable on the canvas (Addendum 5 Fix #3). Mirrors the server's image control-group
  // markup (data-slot + data-prop wired to applyToSlide), so selectZone reveals it and
  // edits land on the SAME tweaks keys the bake reads (RNDR-04). Idempotent.
  function symUse(id, size) {
    size = size || 14;
    return '<svg class="ic" width="' + size + '" height="' + size +
      '" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.45" ' +
      'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><use href="#' + id + '"/></svg>';
  }
  function numField(sid, handle, prop, iconId, val) {
    return '<div class="field" title="' + prop + '">' + symUse(iconId, 14) +
      '<input type="number" data-prop="' + prop + '" value="' + val + '" ' +
      'oninput="applyToSlide(\'' + sid + '\',\'' + handle + '\',\'' + prop +
      '\',parseFloat(this.value))"><span class="unit">%</span></div>';
  }
  // The "Image" sub-block injected into a LAYER_NN group (layer-image-ai-edit):
  // Replace image + Edit-with-AI per AVAILABLE provider — the SAME affordances the
  // server renders for template image slots, routed to the SAME openAiEdit /
  // pickReplaceImage handlers (so save/bake/parity are inherited). Returns "" only
  // if the helpers aren't present (defensive); Replace alone otherwise.
  var AI_PROVIDER_BTN = [["gpt", "Edit with GPT"], ["gemini", "Edit with Gemini"]];
  function imageActionsHtml(sid, handle) {
    var html = '<div class="sec-sub"><span class="label">Image</span>' +
      '<button type="button" class="replace-img-btn" ' +
      'onclick="if(window.pickReplaceImage)pickReplaceImage(\'' + sid + '\',\'' + handle + '\')">' +
      '<span>Replace image…</span></button></div>';
    var provs = window.__aiEditProviders || {};
    var btns = "";
    AI_PROVIDER_BTN.forEach(function (pl) {
      if (!provs[pl[0]]) return;
      btns += '<button type="button" class="ai-edit-btn" data-provider="' + pl[0] + '" ' +
        'onclick="if(window.openAiEdit)openAiEdit(\'' + sid + '\',\'' + handle + '\',\'' + pl[0] + '\')">' +
        '<span>' + pl[1] + '</span></button>';
    });
    if (btns) {
      html += '<div class="sec-sub ai-edit-sub"><span class="label">Edit with AI</span>' +
        btns + '</div>';
    }
    return html;
  }
  function buildImageControlGroup(sid, handle, g) {
    var panel = document.querySelector('.slide-panel[data-slide="' + sid + '"]');
    var insp = panel && panel.querySelector('.inspector');
    if (!insp) return;
    if (insp.querySelector('.control-group[data-slot="' + handle + '"]')) return;  // idempotent
    g = g || {};
    var x = g.x != null ? g.x : 0, y = g.y != null ? g.y : 0,
        w = g.w != null ? g.w : 100, op = g.opacity != null ? g.opacity : 1,
        tilt = g.tilt != null ? g.tilt : 0;
    var grp = document.createElement("div");
    grp.className = "control-group";
    grp.setAttribute("data-control-type", "image");
    grp.setAttribute("data-slide", sid);
    grp.setAttribute("data-slot", handle);
    // An "image-layer" (layer-image-ai-edit): the layer controls (Position/Size/
    // Tilt/Scale/Opacity) STAY, and the IMAGE group (Replace + Edit-with-AI) is
    // ADDED — the slot is layer AND image, never a relabel that strips one.
    grp.innerHTML =
      '<div class="control-group-header">' + symUse("ic-corner", 14) +
        '<span class="cg-name">' + handle + '</span></div>' +
      '<div class="sec-sub"><span class="label">Position</span>' +
        '<div class="grid2">' + numField(sid, handle, "x", "ic-arrh", x) +
        numField(sid, handle, "y", "ic-arrv", y) + '</div>' +
        '<span class="label" style="margin-top:12px">Size</span>' +
        '<div class="grid2">' + numField(sid, handle, "w", "ic-w", w) + '</div>' +
      '</div>' +
      imageActionsHtml(sid, handle) +
      '<div class="sec-sub"><span class="label">Appearance</span>' +
        '<div class="ctrl-row"><span class="ctrl-name">Rotate</span>' +
        '<input type="range" data-prop="tilt" min="-180" max="180" step="1" value="' + tilt + '" ' +
        'oninput="applyToSlide(\'' + sid + '\',\'' + handle + '\',\'tilt\',parseFloat(this.value));' +
        'this.nextElementSibling.textContent=this.value">' +
        '<span class="range-val">' + tilt + '</span></div>' +
        '<div class="ctrl-row"><span class="ctrl-name">Opacity</span>' +
        '<input type="range" data-prop="opacity" min="0" max="1" step="0.05" value="' + op + '" ' +
        'oninput="applyToSlide(\'' + sid + '\',\'' + handle + '\',\'opacity\',parseFloat(this.value));' +
        'this.nextElementSibling.textContent=this.value">' +
        '<span class="range-val">' + op + '</span></div>' +
      '</div>';
    insp.appendChild(grp);
  }
  window.__buildImageControlGroup = buildImageControlGroup;

  // Inject the recolorable colour-FLOOR control (AIOS-139 Bug 2) for a layer-canvas
  // (full-AI / decomposed) slide. The floor element (data-slot="BGFILL") lives at the
  // lowest z-index beneath the BACKGROUND image in both the live srcdoc and the bake
  // template (_ensure_layer_canvas_template). This adds a Fill control + a Layers row
  // so the user can recolour it; hiding the BACKGROUND image above reveals the colour.
  // bgColor lands on the SAME BGFILL tweak key the bake reads (RNDR-04). Idempotent.
  function buildBgFillControlGroup(sid) {
    var panel = document.querySelector('.slide-panel[data-slide="' + sid + '"]');
    var insp = panel && panel.querySelector('.inspector');
    if (!insp) return;
    if (insp.querySelector('.control-group[data-slot="BGFILL"]')) return;  // idempotent
    var grp = document.createElement("div");
    grp.className = "control-group";
    grp.setAttribute("data-control-type", "shape");
    grp.setAttribute("data-slot", "BGFILL");
    grp.innerHTML =
      '<div class="control-group-header">' + symUse("ic-corner", 14) +
        '<span class="cg-name">Background fill</span></div>' +
      '<div class="sec-sub"><span class="label">Fill (revealed when the image is hidden)</span>' +
        '<div class="colorrow" style="margin-top:10px">' +
        '<span class="swatch" style="background:#ffffff"><input type="color" value="#ffffff" ' +
          'oninput="applyToSlide(\'' + sid + '\',\'BGFILL\',\'bgColor\',this.value); if(window.syncHex)syncHex(this)"></span>' +
        '<div class="hex"><span class="hash">#</span><input value="ffffff" maxlength="6" ' +
          'oninput="if(window.applyHex)applyHex(\'' + sid + '\',\'BGFILL\',\'bgColor\',this)"></div>' +
        '</div>' +
      '</div>';
    insp.appendChild(grp);
    // Layers-panel row so BGFILL is selectable + eye-toggleable like any layer.
    addLayerRow(sid, "BGFILL");
  }
  window.__buildBgFillControlGroup = buildBgFillControlGroup;

  // Break a full-AI image into editable layers. Exposed as
  // window.__studioBreakIntoLayers so the in-editor magic-pencil (rendered by
  // preview_editor._build_fullai_layer_panel) and the legacy topbar button share
  // ONE code path. sid defaults to the active slide.
  function breakIntoLayers(sid, slot) {
    // In-flight lock: a second Magic Layer click while a decompose is running is a
    // no-op (the overlay also blocks the click; this guards programmatic callers).
    if (window.__magicInFlight) return;
    sid = sid || window.__activeSlide;
    if (!sid) { toast("No active slide — navigate to a slide first.", true); return; }
    // Eligible when: a specific image slot was picked (per-image Magic Layer), OR
    // it's a full-AI slide, OR a template with a decomposable AI hero.
    if (!slot && !fullAiSlides[sid] && !(window.__decomposableHero && window.__decomposableHero[sid])) {
      toast("Magic Layer needs a full-AI slide or a template with an AI hero.", true);
      return;
    }
    // No pre-flight FAL-key gate: the key is checked at USE time (like Publish/Zernio).
    // /decompose fail-safes (ok:false / status:"skipped") when FAL_KEY is absent —
    // handled below with a clear toast. The overlay + lock go up now.
    window.__magicInFlight = true;
    layersBtn.disabled = true;
    showMagicOverlay();
    function finishMagic() {
      window.__magicInFlight = false;
      layersBtn.disabled = false;
      hideMagicOverlay();
    }
    toast("Decomposing " + (slot ? slot : "slide") + " into layers (this may take ~20s)…");
    post("/decompose", slot ? { slide_id: sid, slot: slot } : { slide_id: sid })
      .then(function (res) {
        if (!res.ok) {
          finishMagic();
          var msg = res.status === "skipped"
            ? "Magic Layer unavailable — FAL_KEY not found in .env"
            : "Decompose failed: " + (res.error || "?");
          toast(msg, true);
          return;
        }
        // Drop each returned layer as a live, movable, bakeable canvas asset.
        var layers = res.layers || [];
        if (!layers.length) { finishMagic(); toast("No layers returned.", true); return; }

        // §2: promote the flat full-AI viewer to an iframe-backed layer canvas
        // (mirrors the bake template), then inject each layer through the shared
        // __addLayerAsset helper once the iframe has its .slide container.
        promoteToLayerCanvas(sid);

        function dropLayers() {
          layers.forEach(function (layer, i) {
            var handle = "LAYER_" + ("0" + i).slice(-2);
            var bbox = layer.bbox || {};
            // Decomposed layers are FULL-FRAME RGBA cutouts (no spatial bbox), so
            // default to x:0,y:0,w:100,h:100 — the first Apply reproduces the
            // original composition exactly; the user nudges from there. (§1D / §2-5)
            window.__addLayerAsset(sid, handle, layer.data_uri || layer.file || "", {
              x:   bbox.x !== undefined ? bbox.x : 0,
              y:   bbox.y !== undefined ? bbox.y : 0,
              w:   bbox.w !== undefined ? bbox.w : 100,
              h:   bbox.h !== undefined ? bbox.h : 100,
              opacity: 1, tilt: 0,
            });
          });
          // §4: the decomposed layers now reproduce the composition, so the ORIGINAL
          // flat image underneath must not intercept interaction — otherwise it sits
          // under the layers and captures clicks, making the navigable layers feel
          // dead. Make the promoted BACKGROUND img non-interactive, and (template
          // mode) HIDE the un-decomposed source slot (e.g. PHOTO_MAIN) so it doesn't
          // double-render beneath its own cutouts. Tweaks (which bake) live on the
          // LAYER_NN assets, so this is preview-only and does NOT affect the bake.
          var fdoc2 = frameDoc(sid);
          if (fdoc2) {
            var bg = fdoc2.querySelector('img[data-slot="BACKGROUND"]');
            if (bg) bg.style.pointerEvents = "none";
            if (slot) {
              var src = fdoc2.querySelector('[data-slot="' + slot + '"]');
              if (src) { src.style.visibility = "hidden"; src.style.pointerEvents = "none"; }
            }
          }
          if (window.__studioCanvas) window.__studioCanvas.rebuild();
          finishMagic();
          toast("" + layers.length + " layer(s) added — move them on the canvas, then Apply to rebake.");
        }

        // The promoted iframe's srcdoc loads async; wait for its .slide container
        // before injecting (poll, since onload timing on srcdoc varies by browser).
        var f = document.getElementById("frame-" + sid);
        var fdoc = f && (f.contentDocument || (f.contentWindow && f.contentWindow.document));
        if (fdoc && fdoc.querySelector(".slide")) { dropLayers(); }
        else {
          var tries = 0;
          (function waitSlide() {
            var d = f && (f.contentDocument || (f.contentWindow && f.contentWindow.document));
            if (d && d.querySelector(".slide")) { dropLayers(); return; }
            if (++tries > 40) { dropLayers(); return; }  // give up the wait, still seed tweaks/rows
            setTimeout(waitSlide, 25);
          })();
        }
      })
      .catch(function (e) { finishMagic(); toast("Decompose error: " + e, true); });
  }
  window.__studioBreakIntoLayers = breakIntoLayers;
  layersBtn.addEventListener("click", function () { breakIntoLayers(window.__activeSlide); });

  // Per-image Magic Layer (template mode): inject a "Magic Layer" button into every
  // image control-group in the inspector, so ANY image slot (esp. the hero photo_main)
  // can be decomposed into editable layers right where it lives — not via the global
  // top-bar button. Decomposes that specific slot's PNG.
  window.__studioMagicLayer = function (sid, handle) { breakIntoLayers(sid, handle); };
  if (isTemplateMode) {
    var injectMagicButtons = function () {
      var groups = document.querySelectorAll('.control-group[data-control-type="image"]');
      Array.prototype.forEach.call(groups, function (grp) {
        var sid = grp.getAttribute("data-slide");
        var handle = grp.getAttribute("data-slot");
        if (!sid || !handle) return;
        var b = grp.querySelector(".ts-magic-btn");
        if (!b) {
          b = document.createElement("button");
          b.type = "button"; b.className = "ts-magic-btn"; b.textContent = "✦ Magic Layer";
          b.addEventListener("click", function () { window.__studioMagicLayer(sid, handle); });
          grp.appendChild(b);
        }
        // Always clickable (like Publish/Zernio) — never pre-disabled on a missing
        // FAL key. The key is checked at click time: /decompose fail-safes and the
        // click path shows a clear toast if FAL_KEY is absent.
        b.disabled = false;
        b.title = "Break this image into editable layers (AI).";
        b.style.cssText = "margin-top:10px;width:100%;border:none;border-radius:8px;" +
          "padding:8px 12px;cursor:pointer;" +
          "font-weight:700;font-size:12px;color:#fff;opacity:1;" +
          "background:linear-gradient(135deg,#7c3aed 0%,#4F52E0 100%);";
      });
    };
    window.__injectMagicButtons = injectMagicButtons;
    var _injRaf = 0;
    var injectDebounced = function () {
      if (_injRaf) return;
      _injRaf = requestAnimationFrame(function () { _injRaf = 0; injectMagicButtons(); });
    };
    injectMagicButtons();
    setTimeout(injectMagicButtons, 200); setTimeout(injectMagicButtons, 600);
    // Re-inject when the inspector for a newly-selected slide is built.
    var _prevOSC = window.__onSlideChange;
    window.__onSlideChange = function (activeId) {
      if (_prevOSC) _prevOSC(activeId);
      setTimeout(injectMagicButtons, 30);
    };
    new MutationObserver(injectDebounced).observe(document.body, { childList: true, subtree: true });
  }

  // ── Add image — upload a new positioned, editable, bakeable asset (§3) ────
  // Reuses the LAYER_NN asset model end-to-end, so it composes with §1/§2: on a
  // full-AI slide we first promote to an iframe layer-canvas, then drop the asset
  // through the SAME __addLayerAsset helper decompose uses (parity by construction).
  var addImageInput = el("input", { type: "file", accept: "image/*",
    style: "display:none;" });
  document.body.appendChild(addImageInput);

  addImageBtn.addEventListener("click", function () {
    var sid = window.__activeSlide;
    if (!sid) { toast("No active slide — navigate to a slide first.", true); return; }
    addImageInput.value = "";   // allow re-picking the same file
    addImageInput.click();
  });

  addImageInput.addEventListener("change", function () {
    var sid = window.__activeSlide;
    var file = addImageInput.files && addImageInput.files[0];
    if (!sid || !file) return;
    var reader = new FileReader();
    reader.onload = function () {
      var dataUri = reader.result;  // "data:image/...;base64,..."
      // Collect the live LAYER handles so the server picks a non-colliding index
      // (decomposed-but-unsaved layers live only in the client tweaks).
      var tw = getTweaks()[sid] || {};
      var existing = Object.keys(tw).filter(function (k) { return /^LAYER_\d+$/.test(k); });
      toast("Uploading image…");
      addImageBtn.disabled = true;
      post("/add-image", { slide_id: sid, data_uri: dataUri, existing_handles: existing })
        .then(function (res) {
          addImageBtn.disabled = false;
          if (!res.ok) { toast("Add image failed: " + (res.error || "?"), true); return; }
          var handle = res.handle, uri = res.data_uri || dataUri;
          // Full-AI slide: promote to an iframe layer-canvas first (§1/§2).
          if (window.__activeSlideIsFullAI && window.__promoteToLayerCanvas) {
            window.__promoteToLayerCanvas(sid);
          }
          // Centered, half-frame default — the user drags/resizes from there.
          var geom = { x: 25, y: 25, w: 50, h: 50, opacity: 1, tilt: 0 };
          function drop() {
            window.__addLayerAsset(sid, handle, uri, geom);
            if (window.__studioCanvas) window.__studioCanvas.rebuild();
            // Select the new layer so its Position/Size/Opacity controls show at once.
            if (window.selectZone) window.selectZone(sid, handle);
            toast("Image added as " + handle + " — drag it or use the panel, then Apply.");
          }
          // Wait for a promoted iframe's .slide before injecting.
          var f = document.getElementById("frame-" + sid);
          var d = f && (f.contentDocument || (f.contentWindow && f.contentWindow.document));
          if (d && d.querySelector(".slide")) { drop(); }
          else {
            var tries = 0;
            (function waitSlide() {
              var dd = f && (f.contentDocument || (f.contentWindow && f.contentWindow.document));
              if (dd && dd.querySelector(".slide")) { drop(); return; }
              if (++tries > 40) { drop(); return; }
              setTimeout(waitSlide, 25);
            })();
          }
        })
        .catch(function (e) { addImageBtn.disabled = false; toast("Add image error: " + e, true); });
    };
    reader.readAsDataURL(file);
  });

  // ── Publish modal (inline panel) ─────────────────────────────
  var publishPanel = null;

  function closePublishPanel() {
    if (publishPanel) { publishPanel.remove(); publishPanel = null; }
  }

  publishBtn.addEventListener("click", function () {
    // Publish is ALWAYS enabled. FASE 6 §2: check the key FRESH on click (re-reads .env
    // per request) so a credential added after launch works without a restart.
    if (publishPanel) { closePublishPanel(); return; }
    fetch("/zernio-key").then(function (r) { return r.json(); }).then(function (res) {
      window.__hasZernioKey = !!(res && res.hasKey);
      if (!window.__hasZernioKey) {
        toast("To publish with Zernio you need the ZERNIO_API_KEY credential in your .env.", true);
        return;
      }
      openPublishPanel();
    }).catch(function () {
      // network hiccup → still let the user try; /post re-checks the key server-side.
      openPublishPanel();
    });
  });

  function openPublishPanel() {
    if (publishPanel) return;
    publishPanel = el("div", { id: "studio-publish-panel", style:
      "position:fixed;top:54px;right:14px;z-index:99998;" +
      "background:#18181f;border-radius:12px;padding:18px 20px;min-width:260px;" +
      "box-shadow:0 4px 24px rgba(0,0,0,.45);font-family:system-ui,sans-serif;" +
      "font-size:13px;color:#e8e8f0;display:flex;flex-direction:column;gap:10px;" });

    function lbl(text) { return el("label", { style: "display:flex;flex-direction:column;gap:4px;font-size:12px;color:#aaa;", text: text }); }
    function inp(attrs) { var i = el("input", Object.assign({ style: "background:#28283a;border:1px solid #44445a;border-radius:6px;padding:5px 8px;color:#e8e8f0;font-size:13px;" }, attrs)); return i; }

    var platformWrap = lbl("Platform");
    var platformSel = el("select", { style: "background:#28283a;border:1px solid #44445a;border-radius:6px;padding:5px 8px;color:#e8e8f0;font-size:13px;" });
    ["linkedin", "instagram", "twitter", "facebook", "threads", "tiktok"].forEach(function (p) {
      platformSel.appendChild(el("option", { value: p, text: p }));
    });
    platformWrap.appendChild(platformSel);

    var accountWrap = lbl("Account ID (optional)");
    var accountInp = inp({ type: "text", placeholder: "auto-resolve" });
    accountWrap.appendChild(accountInp);

    var modeWrap = el("div", { style: "display:flex;flex-direction:column;gap:4px;" });
    modeWrap.appendChild(el("span", { style: "font-size:12px;color:#aaa;", text: "Mode" }));
    var modeRow = el("div", { style: "display:flex;gap:6px;" });
    var modes = ["publishNow", "schedule", "draft"];
    var modeLabels = ["Publish now", "Schedule", "Draft"];
    var modeRadios = {};
    modes.forEach(function (m, i) {
      var rb = el("input", { type: "radio", name: "studio-publish-mode", value: m });
      if (m === "publishNow") rb.checked = true;
      modeRadios[m] = rb;
      var lw = el("label", { style: "display:flex;align-items:center;gap:3px;cursor:pointer;font-size:12px;" });
      lw.appendChild(rb);
      lw.appendChild(el("span", { text: modeLabels[i] }));
      modeRow.appendChild(lw);
    });
    modeWrap.appendChild(modeRow);

    var scheduleWrap = el("div", { style: "display:none;" });
    var scheduleInp = inp({ type: "datetime-local" });
    // AIOS-139 Addendum 9 #3 — datetime-local is the user's LOCAL wall-clock; we
    // convert it to UTC exactly once (new Date(local).toISOString()) for Zernio.
    // Label it local + show both so the UTC Zernio displays is never a surprise.
    var scheduleLbl = lbl("Schedule for (your local time)");
    scheduleLbl.appendChild(scheduleInp);
    var schedHint = el("div", {
      id: "sched-hint",
      style: "margin-top:6px;font-size:12px;color:#9a9aa2;min-height:16px;",
    });
    scheduleWrap.appendChild(scheduleLbl);
    scheduleWrap.appendChild(schedHint);
    function fmtSchedHint() {
      if (!scheduleInp.value) { schedHint.textContent = ""; return; }
      var d = new Date(scheduleInp.value);          // local wall-clock
      if (isNaN(d.getTime())) { schedHint.textContent = ""; return; }
      var local = d.toLocaleString([], { dateStyle: "medium", timeStyle: "short" });
      var utc = d.toISOString().slice(0, 16).replace("T", " ");  // YYYY-MM-DD HH:MM (UTC)
      schedHint.textContent = "Posts " + local + " your time · " + utc + " UTC";
    }
    scheduleInp.addEventListener("input", fmtSchedHint);
    scheduleInp.addEventListener("change", fmtSchedHint);

    modeRadios["schedule"].addEventListener("change", function () {
      scheduleWrap.style.display = modeRadios["schedule"].checked ? "block" : "none";
    });
    modeRadios["publishNow"].addEventListener("change", function () {
      scheduleWrap.style.display = "none";
    });
    modeRadios["draft"].addEventListener("change", function () {
      scheduleWrap.style.display = "none";
    });

    var pdfWrap = el("label", { style: "display:flex;align-items:center;gap:6px;font-size:12px;color:#aaa;cursor:pointer;" });
    var pdfCb = el("input", { type: "checkbox" });
    pdfWrap.appendChild(pdfCb);
    pdfWrap.appendChild(el("span", { text: "LinkedIn PDF carousel" }));

    var pdfHint = el("div", {
      style: "font-size:11px;color:#7a7a8a;",
      text: "PDF = swipeable carousel — slide numbers, download, ~3x reach. Off = image gallery (max 9 images, lower reach).",
    });

    // Warning shown when the user turns PDF off on a carousel with >9 slides.
    var pdfWarnWrap = el("div", {
      style: "display:none;font-size:11px;color:#e27c4a;background:rgba(226,124,74,.12);" +
             "border-radius:6px;padding:6px 8px;",
      text: "LinkedIn image gallery supports up to 9 images. This carousel has more — enable PDF carousel or the extra slides will be dropped by LinkedIn.",
    });

    function syncPdfDefaults() {
      var slideCount = (window.slideIds || []).length;
      var isLinkedin = platformSel.value === "linkedin";
      var isCarousel = slideCount > 1;
      // Default PDF ON for linkedin carousel; user may toggle off.
      if (isLinkedin && isCarousel) pdfCb.checked = true;
      // Show warning when PDF is off and slide count exceeds the 9-image limit.
      pdfWarnWrap.style.display =
        (isLinkedin && !pdfCb.checked && slideCount > 9) ? "block" : "none";
    }

    pdfCb.addEventListener("change", function () {
      var slideCount = (window.slideIds || []).length;
      pdfWarnWrap.style.display =
        (platformSel.value === "linkedin" && !pdfCb.checked && slideCount > 9) ? "block" : "none";
    });
    platformSel.addEventListener("change", syncPdfDefaults);
    // Set default immediately when the panel opens.
    syncPdfDefaults();

    var docTitleWrap = lbl("PDF document title (optional)");
    var docTitleInp = inp({ type: "text", placeholder: "inferred from folder name" });
    docTitleWrap.appendChild(docTitleInp);

    // First comment (AIOS-131) — always visible; persists to post.yaml on blur.
    var firstCommentWrap = el("div", { style: "display:flex;flex-direction:column;gap:4px;" });
    firstCommentWrap.appendChild(el("span", { style: "font-size:12px;color:#aaa;", text: "First comment (LinkedIn)" }));
    firstCommentWrap.appendChild(el("div", {
      style: "font-size:11px;color:#7a7a8a;",
      text: "Posted as the first comment right after publishing — put links/CTAs here to avoid LinkedIn’s reach penalty for links in the post body.",
    }));
    var firstCommentTa = document.createElement("textarea");
    firstCommentTa.rows = 3;
    firstCommentTa.placeholder = "Links, CTAs, hashtags…";
    firstCommentTa.style = "width:100%;box-sizing:border-box;margin-top:4px;" +
      "background:#28283a;border:1px solid #44445a;border-radius:6px;" +
      "padding:5px 8px;color:#e8e8f0;font-size:13px;resize:vertical";
    firstCommentTa.value = window.__firstComment || "";
    firstCommentTa.addEventListener("blur", function () {
      window.__firstComment = firstCommentTa.value;
      post("/save-first-comment", { first_comment: firstCommentTa.value })
        .then(function (res) { if (res && res.ok) toast("First comment saved."); })
        .catch(function () {});
    });
    firstCommentWrap.appendChild(firstCommentTa);

    var btnRow = el("div", { style: "display:flex;gap:8px;margin-top:4px;" });
    var confirmBtn = el("button", { style:
      "flex:1;border:none;border-radius:8px;padding:8px 0;cursor:pointer;" +
      "font-weight:600;color:#fff;background:#5B57D6;", text: "Confirm" });
    var cancelBtn = el("button", { style:
      "border:none;border-radius:8px;padding:8px 14px;cursor:pointer;" +
      "font-weight:600;color:#aaa;background:#28283a;", text: "Cancel" });
    cancelBtn.addEventListener("click", closePublishPanel);
    btnRow.appendChild(confirmBtn);
    btnRow.appendChild(cancelBtn);

    confirmBtn.addEventListener("click", function () {
      var platform = platformSel.value;
      var slideCount = (window.slideIds || []).length;
      // Block publish when LinkedIn image gallery would silently truncate slides.
      if (platform === "linkedin" && !pdfCb.checked && slideCount > 9) {
        toast("Enable PDF carousel — LinkedIn image gallery supports up to 9 images and this carousel has " + slideCount + ".", true);
        return;
      }
      var accountId = accountInp.value.trim();
      var mode = (function () {
        for (var k in modeRadios) { if (modeRadios[k].checked) return k; }
        return "publishNow";
      })();
      var scheduleFor = (mode === "schedule" && scheduleInp.value)
        ? new Date(scheduleInp.value).toISOString() : "";
      var pdf = pdfCb.checked;
      var documentTitle = docTitleInp.value.trim();
      confirmBtn.disabled = true;
      // Implicit bake first (FASE 5 §1) so the published media are the live composites.
      toast("Baking slides…");
      bakeNow().then(function () {
      toast("Publishing…");
      // Pass the current tweaks so /post can guarantee a fresh server-side rebake
      // of the edited slides even if the client bake raced (Addendum 9 #2).
      var curTweaks = (typeof window.__getTweaks === "function") ? window.__getTweaks() : null;
      return post("/post", { platform: platform, accountId: accountId, mode: mode,
                      scheduleFor: scheduleFor, pdf: pdf, documentTitle: documentTitle,
                      tweaks: curTweaks, firstComment: firstCommentTa.value })
        .then(function (res) {
          confirmBtn.disabled = false;
          if (res.ok) {
            var msg = "Published!";
            if (res.post_url) msg = "Published: " + res.post_url;
            else if (res.scheduled_for) msg = "Scheduled for " + res.scheduled_for;
            else if (res.status) msg = "Status: " + res.status;
            toast(msg);
            closePublishPanel();
          } else {
            toast((res.reason || res.error || "Publish failed"), true);
          }
        })
        .catch(function (e) { confirmBtn.disabled = false; toast("Publish error: " + e, true); });
      });  // end bakeNow().then
    });

    publishPanel.appendChild(platformWrap);
    publishPanel.appendChild(accountWrap);
    publishPanel.appendChild(modeWrap);
    publishPanel.appendChild(scheduleWrap);
    publishPanel.appendChild(pdfWrap);
    publishPanel.appendChild(pdfHint);
    publishPanel.appendChild(pdfWarnWrap);
    publishPanel.appendChild(docTitleWrap);
    publishPanel.appendChild(firstCommentWrap);
    publishPanel.appendChild(btnRow);
    document.body.appendChild(publishPanel);
  }

  // ── Template Studio — Conference panel (pool-walk, side-by-side ref|render) ──
  // Replaces the old tabbed /compare panel. Walks N templates from the pool
  // one-by-one with XX/XX counter + lateral arrows + per-template Approve.
  // The /compare shim (back-compat) accepts these mode values for single-template
  // compares: "side-by-side", "overlay", "diff", "grid".
  var _COMPARE_MODES = ["side-by-side", "overlay", "diff", "grid"];
  var conferencePanel = null;
  var confBackdrop = null;

  function closeConference() {
    if (conferencePanel) { conferencePanel.remove(); conferencePanel = null; }
    if (confBackdrop) { confBackdrop.remove(); confBackdrop = null; }
    document.removeEventListener("keydown", confKeyHandler);
  }

  var confKeyHandler = function () {};

  if (isTemplateMode && compareBtn) {
    compareBtn.addEventListener("click", function () {
      if (conferencePanel) { closeConference(); return; }
      openConference();
    });
  }

  function openConference() {
    if (conferencePanel) return;

    // Centered modal: the comparison (ref | render) of the current template.
    confBackdrop = el("div", { id: "ts-compare-backdrop", style:
      "position:fixed;inset:0;z-index:99997;background:rgba(0,0,0,.45);" });
    confBackdrop.addEventListener("click", closeConference);
    document.body.appendChild(confBackdrop);
    conferencePanel = el("div", { id: "ts-compare-panel", style:
      "position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);z-index:99998;" +
      "background:#18181f;border-radius:12px;padding:18px 20px;" +
      "width:min(900px,92vw);max-height:calc(100vh - 60px);overflow-y:auto;" +
      "box-shadow:0 8px 40px rgba(0,0,0,.55);font-family:system-ui,sans-serif;" +
      "font-size:13px;color:#e8e8f0;display:flex;flex-direction:column;gap:12px;" });

    // Header
    var hdr = el("div", { style: "display:flex;justify-content:space-between;align-items:center;" });
    hdr.appendChild(el("span", { style:
      "font:700 10px/1 'Space Grotesk',sans-serif;letter-spacing:.1em;text-transform:uppercase;color:#9a9aa8;",
      text: "Template Conference — Ref | Render" }));
    var closeX = el("button", { style:
      "border:none;background:none;color:#9a9aa8;font-size:16px;cursor:pointer;padding:0 4px;",
      text: "×" });
    closeX.addEventListener("click", closeConference);
    hdr.appendChild(closeX);
    conferencePanel.appendChild(hdr);

    // Side-by-side image row (labels + images)
    var imgRow = el("div", { style:
      "display:flex;gap:10px;align-items:flex-start;" });
    function mkImgCol(label) {
      var wrap = el("div", { style: "flex:1;min-width:0;" });
      var lbl = el("div", { style:
        "font:700 10px/1 'Space Grotesk',sans-serif;letter-spacing:.08em;" +
        "text-transform:uppercase;color:#9a9aa8;margin-bottom:5px;", text: label });
      var img = document.createElement("img");
      img.style.cssText = "width:100%;border-radius:6px;display:block;min-height:80px;" +
        "max-height:46vh;background:#28283a;object-fit:contain;";
      wrap.appendChild(lbl); wrap.appendChild(img);
      return { wrap: wrap, img: img };
    }
    var refCol = mkImgCol("Reference");
    var renderCol = mkImgCol("Render");
    imgRow.appendChild(refCol.wrap);
    imgRow.appendChild(renderCol.wrap);
    conferencePanel.appendChild(imgRow);

    // Status / error line
    var confStatus = el("div", { style: "font-size:12px;color:#9a9aa8;min-height:16px;" });
    conferencePanel.appendChild(confStatus);

    // Builder rationale / review notes (Template Card from instructions.md) —
    // shown beneath the compare panes so the reviewer sees WHY the builder shaped
    // the template this way (form · per-block treatment · edit_mode · extraction)
    // as improvement-suggestion context (AIOS-190 W1, Gustavo's ask). Collapsed by
    // default to keep the compare the focus; populated per template in loadTemplate.
    var confNotes = el("details", { style:
      "background:#13131a;border:1px solid #2a2a3a;border-radius:8px;" +
      "padding:8px 12px;font-size:12px;color:#c8c8d4;display:none;" });
    var confNotesSummary = el("summary", { style:
      "cursor:pointer;font:700 10px/1 'Space Grotesk',sans-serif;letter-spacing:.08em;" +
      "text-transform:uppercase;color:#9a9aa8;outline:none;",
      text: "Builder notes — why this template" });
    var confNotesBody = el("pre", { style:
      "white-space:pre-wrap;word-break:break-word;margin:8px 0 0;font:inherit;" +
      "max-height:30vh;overflow-y:auto;color:#c8c8d4;" });
    confNotes.appendChild(confNotesSummary);
    confNotes.appendChild(confNotesBody);
    conferencePanel.appendChild(confNotes);

    // ── Bottom bar: ← counter → + per-template Approve ───────────────────
    var bottomBar = el("div", { style:
      "display:flex;align-items:center;gap:8px;border-top:1px solid #2a2a3a;" +
      "margin-top:4px;padding-top:10px;" });
    function navBtn(label) {
      var b = el("button", { type: "button", style:
        "border:1px solid #44445a;background:#28283a;color:#e8e8f0;border-radius:8px;" +
        "width:34px;height:34px;cursor:pointer;font-size:18px;line-height:1;font-weight:400;" +
        "display:flex;align-items:center;justify-content:center;", text: label });
      return b;
    }
    var prevBtn = navBtn("←");
    var counterSpan = el("span", { id: "ts-conf-counter", style:
      "flex:1;text-align:center;font:700 13px/1 'Space Grotesk',sans-serif;color:#9a9aa8;" });
    var nextBtn = navBtn("→");
    var confApproveBtn = el("button", { type: "button", style:
      "border:none;border-radius:8px;padding:8px 16px;cursor:pointer;font-weight:700;" +
      "font-size:12px;color:#fff;background:linear-gradient(135deg,#4F52E0 0%,#6366f1 100%);" +
      "box-shadow:0 4px 12px rgba(79,82,224,.25);", text: "Approve template" });
    // P1 #3: the Conference already shows the ACTIVE template, and the ‹ › arrows
    // are the navigation, so the old per-template edit button was dead UI (built
    // then force-hidden) — removed entirely.
    var closePanelBtn = el("button", { type: "button", style:
      "border:none;border-radius:8px;padding:8px 14px;cursor:pointer;font-weight:600;" +
      "color:#aaa;background:#28283a;font-size:12px;", text: "Close" });
    closePanelBtn.addEventListener("click", closeConference);
    bottomBar.appendChild(prevBtn);
    bottomBar.appendChild(counterSpan);
    bottomBar.appendChild(nextBtn);
    bottomBar.appendChild(confApproveBtn);
    bottomBar.appendChild(closePanelBtn);
    conferencePanel.appendChild(bottomBar);

    document.body.appendChild(conferencePanel);

    // ── Pool-walk state ───────────────────────────────────────────────────
    var tplList = [];    // [{id, status}, …] from /pool-templates
    var tplIdx = 0;      // current position in tplList
    var activeId = "";   // id of the currently displayed template
    var approved = {};   // {id: true} locally-tracked approvals this session

    function updateCounter() {
      counterSpan.textContent = tplList.length
        ? (tplIdx + 1) + " / " + tplList.length
        : "— / —";
      prevBtn.disabled = tplIdx === 0;
      nextBtn.disabled = tplIdx >= tplList.length - 1;
    }

    function setStatus(msg, isErr) {
      confStatus.textContent = msg || "";
      confStatus.style.color = isErr ? "#e27c4a" : "#9a9aa8";
    }

    function loadTemplate(idx) {
      if (!tplList.length) return;
      tplIdx = Math.max(0, Math.min(idx, tplList.length - 1));
      activeId = tplList[tplIdx].id;
      // Snapshot current tweaks into the per-template map BEFORE changing template.
      window.__tplTweaks[activeId] = (window.__getTweaks && window.__getTweaks()) || {};
      updateCounter();
      // Clear images + notes while loading
      refCol.img.src = ""; renderCol.img.src = "";
      confNotesBody.textContent = ""; confNotes.style.display = "none";
      setStatus("Loading " + activeId + "…");
      confApproveBtn.disabled = true;
      post("/compare-images", { template_id: activeId }).then(function (res) {
        confApproveBtn.disabled = false;
        if (!res || !res.ok) {
          setStatus((res && res.error) || "compare-images failed", true);
          return;
        }
        var msgs = [];
        if (res.ref) {
          refCol.img.src = res.ref;
        } else {
          refCol.img.src = "";
          msgs.push("Reference missing for " + activeId);
        }
        if (res.render) {
          // Cache-buster: append ?v=<render_version> so the browser never serves a
          // cached stale render after an edit re-bakes preview.png. A data: URI is
          // inline (uncacheable) so the param is only meaningful — and only valid —
          // on a real URL; guard so we never corrupt a data: URI.
          var renderSrc = res.render;
          if (res.render_version && renderSrc.indexOf("data:") !== 0) {
            renderSrc += (renderSrc.indexOf("?") >= 0 ? "&" : "?") + "v=" +
              encodeURIComponent(res.render_version);
          }
          renderCol.img.src = renderSrc;
        } else {
          renderCol.img.src = "";
          msgs.push("No render yet for " + activeId);
        }
        if (res.notes) {
          confNotesBody.textContent = res.notes;
          confNotes.style.display = "block";
        } else {
          confNotesBody.textContent = "";
          confNotes.style.display = "none";
        }
        if (res.error) msgs.push(res.error);
        setStatus(msgs.join(" · ") || (approved[activeId] ? "Approved" : ""), !msgs.length ? false : true);
      }).catch(function (e) {
        confApproveBtn.disabled = false;
        setStatus("Error: " + e, true);
      });
    }

    // Per-template Approve — reads ACTIVE template's live tweaks via
    // __getTweaks() so edits applied without a template-switch are captured.
    confApproveBtn.addEventListener("click", function () {
      var tw = (window.__getTweaks && window.__getTweaks()) || {};
      confApproveBtn.disabled = true;
      setStatus("Baking template…");
      bakeNow().then(function () {
        setStatus("Saving…");
        return post("/approve", { template_id: activeId, tweaks: tw });
      }).then(function (res) {
        confApproveBtn.disabled = false;
        if (res && res.ok) {
          approved[activeId] = true;
          setStatus("Template approved");
          // §5: drop the approved template from the conference queue and advance to
          // the next pending one (or show the all-approved state).
          var ai = activeId, ri = -1;
          for (var q = 0; q < tplList.length; q++) {
            if (tplList[q].id === ai) { ri = q; break; }
          }
          if (ri >= 0) tplList.splice(ri, 1);
          if (!tplList.length) {
            refCol.img.src = ""; renderCol.img.src = "";
            setStatus("All templates approved", false);
            updateCounter();
          } else {
            loadTemplate(Math.min(ri < 0 ? tplIdx : ri, tplList.length - 1));
          }
        } else {
          setStatus((res && res.error) || "Approve failed", true);
        }
      }).catch(function (e) {
        confApproveBtn.disabled = false;
        setStatus("Approve error: " + e, true);
      });
    });

    prevBtn.addEventListener("click", function () { loadTemplate(tplIdx - 1); });
    nextBtn.addEventListener("click", function () { loadTemplate(tplIdx + 1); });

    // Optional arrow-key navigation while the panel is open
    confKeyHandler = function (e) {
      if (!conferencePanel) return;
      if (e.key === "ArrowLeft")  { e.preventDefault(); loadTemplate(tplIdx - 1); }
      if (e.key === "ArrowRight") { e.preventDefault(); loadTemplate(tplIdx + 1); }
    };
    document.addEventListener("keydown", confKeyHandler);

    // Conference is now INDIVIDUAL per template: it shows only the ACTIVE
    // template's compare (ref | render). Pool navigation lives on the main-screen
    // ‹ › arrows, so the in-panel walk (prev/next/counter) + Edit button are hidden.
    prevBtn.style.display = "none";
    nextBtn.style.display = "none";
    counterSpan.style.display = "none";
    fetch("/pool-templates").then(function (r) { return r.json(); }).then(function (res) {
      if (!res || !res.ok || !res.templates || !res.templates.length) {
        setStatus((res && res.error) || "No templates found in pool", true);
        return;
      }
      // §5: the Conference is part of the front — show only templates still needing
      // work (filter out approved:true).
      tplList = res.templates.filter(function (t) { return !t.approved; });
      if (!tplList.length) { setStatus("All templates approved", false); return; }
      var ai = 0;
      for (var k = 0; k < tplList.length; k++) {
        if (tplList[k].id === res.active) { ai = k; break; }
      }
      loadTemplate(ai);
    }).catch(function (e) {
      setStatus("Could not load pool templates: " + e, true);
    });
  }

  // ── Template Studio — topbar Approve (single-template quick-approve) ─────
  // Kept for single-template runs where the conference is not needed; reads
  // current ambient tweaks (no per-template map needed — only one template).
  if (isTemplateMode && approveBtn) {
    approveBtn.addEventListener("click", function () {
      toast("Baking template…");
      approveBtn.disabled = true;
      bakeNow().then(function () {
        toast("Saving template…");
        return post("/approve", { tweaks: getTweaks() });
      }).then(function (res) {
        if (res && res.ok) {
          toast("Template approved");
          // §5: drop it from the front's nav and advance to the next pending template.
          // Keep the button DISABLED through the advance — it triggers a page reload,
          // and re-enabling here opens a window where a second click lands on the
          // freshly-loaded NEXT template and approves it by accident (the "it approved
          // all" bug). The reload resets the button state.
          if (window.__tplNav && window.__tplNav.advanceAfterApprove) {
            window.__tplNav.advanceAfterApprove();
          } else {
            approveBtn.disabled = false;
          }
        } else {
          approveBtn.disabled = false;
          toast((res && res.error) || "Approve failed", true);
        }
      }).catch(function (e) {
        approveBtn.disabled = false;
        toast("Approve error: " + e, true);
      });
    });
  }

  // Keep the texture dropdown in sync with the active slide as the user swipes (FASE 5 §4).
  var _prevTexSync = window.__onSlideChange;
  window.__onSlideChange = function (activeId) {
    if (_prevTexSync) _prevTexSync(activeId);
    syncTextureFromSlide();
  };

  // ── Undo (Ctrl/Cmd+Z) — P1 #7 ──────────────────────────────────────────────
  // There is no native undo for canvas/panel slot edits. We WRAP window.applyToSlide
  // (defined in preview_editor.py — not edited here) so that, before every change,
  // we record the PREVIOUS value of (slideId, slotName, prop) read from the live
  // tweaks (window.__getTweaks(), which mirrors each slot's recorded state). On
  // Ctrl+Z we pop the last entry and re-apply that previous value WITHOUT pushing a
  // new history entry. Undo is intentionally coarse (one step per applyToSlide call).
  (function installUndo() {
    var stack = [];          // [{slideId, slotName, prop, prev}]
    var MAX = 200;           // cap so a long session can't grow unbounded
    var replaying = false;   // suppress history capture while re-applying

    // Read the current value of a prop for a slot from the live tweaks; returns
    // undefined when the slot/prop is still at the template default (not yet tweaked).
    function readPrev(slideId, slotName, prop) {
      var tw = getTweaks();
      var slide = tw && tw[slideId];
      var slot = slide && slide[slotName];
      return (slot && Object.prototype.hasOwnProperty.call(slot, prop))
        ? slot[prop] : undefined;
    }

    function wrap() {
      if (typeof window.applyToSlide !== "function" || window.applyToSlide.__csUndoWrapped) {
        return typeof window.applyToSlide === "function";
      }
      var orig = window.applyToSlide;
      var wrapped = function (slideId, slotName, prop, value) {
        if (!replaying) {
          var prev = readPrev(slideId, slotName, prop);
          stack.push({ slideId: slideId, slotName: slotName, prop: prop, prev: prev });
          if (stack.length > MAX) stack.shift();
        }
        return orig.apply(this, arguments);
      };
      wrapped.__csUndoWrapped = true;
      window.applyToSlide = wrapped;
      return true;
    }
    // applyToSlide exists by the time the shim runs (editor script precedes /studio.js),
    // but retry a few times in case of an unusual load order.
    if (!wrap()) {
      var tries = 0;
      var iv = setInterval(function () {
        if (wrap() || ++tries > 20) clearInterval(iv);
      }, 50);
    }

    function undo() {
      var e = stack.pop();
      if (!e) { toast("Nothing to undo."); return; }
      // e.prev === undefined means the prop was at its template default before this
      // edit; re-applying undefined resets the inline style on most branches (a
      // best-effort revert — undo is intentionally coarse).
      replaying = true;
      try {
        window.applyToSlide(e.slideId, e.slotName, e.prop, e.prev);
      } finally {
        replaying = false;
      }
      // Keep the Konva canvas rects in sync with the reverted geometry.
      if (window.__studioCanvas && window.__studioCanvas.rebuild) {
        try { window.__studioCanvas.rebuild(); } catch (e2) {}
      }
      toast("Undo.");
    }

    document.addEventListener("keydown", function (ev) {
      var key = (ev.key || "").toLowerCase();
      if (key !== "z" || ev.shiftKey || !(ev.ctrlKey || ev.metaKey)) return;
      // Let native field undo win when typing in a textarea/input (e.g. caption,
      // text slots, inspector number fields) — only intercept on the canvas/page.
      var t = ev.target;
      var tag = t && t.tagName ? t.tagName.toLowerCase() : "";
      if (tag === "textarea" || tag === "input" || (t && t.isContentEditable)) return;
      ev.preventDefault();
      undo();
    });
  })();

  // ── Resume: pull saved state on open. Records the Zernio-key flag for the Publish
  // click message — the button is NEVER disabled (FASE 5 §3). ─
  fetch("/load").then(function (r) { return r.json(); }).then(function (res) {
    if (res && res.ok && (res.hasTweaks || res.hasComments)) {
      toast("Restored saved session" +
        (res.hasTweaks ? " · tweaks" : "") + (res.hasComments ? " · comments" : "") + ".");
    }
    window.__hasZernioKey = !!(res && res.hasZernioKey);
    window.__firstComment = (res && res.firstComment) || "";
  }).catch(function () { window.__hasZernioKey = false; });
  syncTextureFromSlide();
})();
"""


# ──────────────────────────────────────────────────────────────────────────
# Canvas overlay — Konva free-transform layer over the live slide (server-only).
# Draws a selectable/transformable rect per editable zone (from window.__SLOT_BBOXES),
# and serializes drag/resize/rotate into the SAME tweaks keys the panel writes
# (x/y/w/tilt), driving the live iframe via window.applyToSlide. Rotation pivots at
# the rect CENTER to match the bake's `transform: rotate()` (center origin) — RNDR-04.
# Height is NOT serialized (the bake honors `h` but the live preview's applyToSlide
# does not, so writing it would break preview==bake); resize edits width only.
# ──────────────────────────────────────────────────────────────────────────
CANVAS_JS = r"""
(function () {
  "use strict";
  if (typeof Konva === "undefined" || location.protocol === "file:") return;

  var ACCENT = "#6366F1";  // command-centre indigo accent
  var stage = null, layer = null, tr = null, container = null;
  var rectByHandle = {};
  var selecting = false;   // re-entrancy guard for selection echo (panel <-> canvas)

  function round(v) { return Math.round(v * 1000) / 1000; }
  function activeSid() { return window.__activeSlide; }
  function bboxes(sid) { return (window.__SLOT_BBOXES && window.__SLOT_BBOXES[sid]) || []; }
  function curTweaks() { return (window.__getTweaks && window.__getTweaks()) || {}; }

  // The editable-zone list for the canvas = declared numeric bboxes (instructions.md
  // bbox:) UNION every [data-slot] element actually present in the live slide. Older
  // templates position zones via semantic CSS (position: center) with NO numeric bbox,
  // so __SLOT_BBOXES is empty and nothing was selectable; the live element IS the source
  // of truth and measureEl() reads its real geometry, so a DOM-discovered handle (x/y/w/h
  // = 0 placeholders) still gets a correctly-sized rect.
  function editableHandles(sid) {
    var seen = {}, out = [];
    bboxes(sid).forEach(function (b) { seen[b.handle] = 1; out.push(b); });
    var f = document.getElementById("frame-" + sid);
    try {
      var d = f && (f.contentDocument || (f.contentWindow && f.contentWindow.document));
      if (d) {
        var nodes = d.querySelectorAll("[data-slot]");
        for (var i = 0; i < nodes.length; i++) {
          var h = nodes[i].getAttribute("data-slot");
          if (h && !seen[h]) { seen[h] = 1; out.push({ handle: h, x: 0, y: 0, w: 0, h: 0 }); }
        }
      }
    } catch (e) {}
    return out;
  }

  function activeWrap() {
    var sid = activeSid();
    return sid ? document.querySelector('.slide-viewer[data-slide="' + sid + '"] .slide-frame-wrap') : null;
  }
  function stageSize() {
    var w = activeWrap();
    return w ? { w: w.clientWidth, h: w.clientHeight } : { w: 555, h: 694 };
  }
  function isLocked(sid, h) {
    var row = document.querySelector('.slide-panel[data-slide="' + sid + '"] .layer-row[data-handle="' + h + '"]');
    return !!(row && row.getAttribute("data-locked") === "1");
  }
  function liveEl(sid, h) {
    var f = document.getElementById("frame-" + sid);
    if (!f) return null;
    try {
      var d = f.contentDocument || (f.contentWindow && f.contentWindow.document);
      return d ? d.querySelector('[data-slot="' + h + '"]') : null;
    } catch (e) { return null; }
  }
  function isHidden(sid, h) {
    var el = liveEl(sid, h);
    return !!(el && el.style.display === "none");
  }

  // Total rendered rotation (deg) of an element — composes the CSS `rotate` property
  // and any `transform` matrix, so a tweak-driven OR template-driven tilt is captured.
  function rotationOf(el) {
    var cs = getComputedStyle(el), ang = 0, m;
    if (cs.rotate && cs.rotate !== "none") { m = cs.rotate.match(/(-?[0-9.]+)deg/); if (m) ang += parseFloat(m[1]); }
    if (cs.transform && cs.transform !== "none") {
      m = cs.transform.match(/matrix\(([^)]+)\)/);
      if (m) { var v = m[1].split(","); ang += Math.atan2(parseFloat(v[1]), parseFloat(v[0])) * 180 / Math.PI; }
    }
    return Math.round(ang * 100) / 100;
  }
  // Measure the LIVE element's real geometry (canvas %): unrotated top-left + size +
  // rotation. The iframe's internal coord space is 1080x1350 (its clientWidth/Height);
  // getBoundingClientRect's centre is rotation-invariant, offsetWidth/Height give the
  // unrotated border box. This makes the rect hug whatever is actually rendered —
  // images, rotated zones, auto-height text — instead of the declared bbox.
  function measureEl(sid, h) {
    var el = liveEl(sid, h);
    if (!el || el.style.display === "none") return null;
    var f = document.getElementById("frame-" + sid);
    var IW = (f && f.clientWidth) || 1080, IH = (f && f.clientHeight) || 1350;
    var r = el.getBoundingClientRect();
    if (!r.width && !r.height) return null;
    var cx = r.left + r.width / 2, cy = r.top + r.height / 2;   // centre (rotation-invariant)
    var ow = el.offsetWidth, oh = el.offsetHeight;             // unrotated border box
    return {
      x: (cx - ow / 2) / IW * 100, y: (cy - oh / 2) / IH * 100,
      w: ow / IW * 100, h: oh / IH * 100, rot: rotationOf(el),
    };
  }

  // ── Build / rebuild the stage for the active slide ────────────
  function teardown() {
    if (stage) { stage.destroy(); stage = null; }
    if (container && container.parentNode) container.parentNode.removeChild(container);
    container = null; layer = null; tr = null; rectByHandle = {};
  }

  function rebuild() {
    teardown();
    if (!window.__studioCanvasOn) return;
    var wrap = activeWrap();
    if (!wrap) return;
    var sz = stageSize();

    container = document.createElement("div");
    container.className = "studio-canvas";
    container.setAttribute("style",
      "position:absolute;inset:0;z-index:60;" +
      (window.__studioCanvasOn ? "" : "pointer-events:none;"));
    if (getComputedStyle(wrap).position === "static") wrap.style.position = "relative";
    wrap.appendChild(container);

    stage = new Konva.Stage({ container: container, width: sz.w, height: sz.h });
    layer = new Konva.Layer();
    stage.add(layer);

    // In free-transform (ON) mode the canvas owns all pointer drags so editing never
    // flips the slide — navigate with the arrows / dots / arrow-keys. Stop the DOM
    // event here so the swipe handler on #li-viewer never arms. (Konva's own listeners
    // on this same container already ran, so selection/drag/transform still work.)
    // Toggle OFF (pointer-events:none on the container) restores swipe-by-drag.
    container.addEventListener("pointerdown", function (e) {
      if (window.__studioCanvasOn) e.stopPropagation();
    });

    tr = new Konva.Transformer({
      rotateEnabled: true, borderStroke: ACCENT, anchorStroke: ACCENT,
      anchorFill: "#fff", anchorSize: 9, borderDash: [3, 3],
      keepRatio: false, ignoreStroke: true,
    });
    layer.add(tr);

    var sid = activeSid();
    var tw = curTweaks()[sid] || {};
    // Measure every editable zone first, then build rects BIGGEST-area-first so the
    // smaller foreground zones land ON TOP in the Konva hit graph. Without this a
    // full-bleed BACKGROUND rect intercepts every click meant for the content stacked
    // above it (a click on the headline would select BACKGROUND).
    var entries = [];
    editableHandles(sid).forEach(function (b) {
      if (isLocked(sid, b.handle) || isHidden(sid, b.handle)) return;
      // Prefer the LIVE measured geometry (hugs the real rendered element, rotation
      // included); fall back to the declared bbox + any tweak override.
      var m = measureEl(sid, b.handle);
      var ov = tw[b.handle] || {};
      // The stored x/y are translate DELTAS already applied to the live element, so the
      // measured absolute position = natural + delta. Carry the deltas so the natural
      // origin can be recovered (natural = measured - delta) and a drag serializes a new
      // delta, not an absolute %.
      var e = { handle: b.handle, ovx: (+ov.x || 0), ovy: (+ov.y || 0) };
      if (m) {
        e.x = m.x; e.y = m.y; e.w = m.w; e.h = m.h; e.tilt = m.rot;
      } else {
        e.x = e.ovx; e.y = e.ovy;
        e.w = (ov.w != null) ? ov.w : b.w;
        e.h = b.h;
        e.tilt = (ov.tilt != null) ? ov.tilt : 0;
      }
      entries.push(e);
    });
    entries.sort(function (a, c) { return (c.w * c.h) - (a.w * a.h); });  // big -> small (small on top)
    entries.forEach(function (b) {
      var xPct = b.x, yPct = b.y, wPct = b.w, hPct = b.h, tilt = b.tilt;
      var rw = Math.max(6, wPct / 100 * sz.w);
      var rh = Math.max(6, hPct / 100 * sz.h);
      var rect = new Konva.Rect({
        x: xPct / 100 * sz.w + rw / 2,   // (x,y) = CENTER (offset below) → rotate/scale pivot = center
        y: yPct / 100 * sz.h + rh / 2,
        width: rw, height: rh, offsetX: rw / 2, offsetY: rh / 2,
        rotation: tilt, draggable: true,
        // invisible by default (no permanent box over the slide) but still hit-testable
        // — the fill is in the hit graph regardless of its near-zero alpha; selection
        // shows the Transformer, hover shows a faint outline for discoverability.
        stroke: ACCENT, strokeWidth: 0, fill: "rgba(91,87,214,0.001)",
        hitStrokeWidth: 12,
      });
      rect.__handle = b.handle;
      // natural origin (absolute % with NO translate) = measured - applied delta. A drag
      // serializes the NEW delta = current absolute - natural. __init keeps the starting
      // values (deltas for x/y) so serialize only writes props the user actually moved
      // (a pure drag must not bake the element's base width/rotation).
      rect.__natural = { x: xPct - b.ovx, y: yPct - b.ovy };
      rect.__init = { x: b.ovx, y: b.ovy, w: wPct, tilt: tilt };
      function selected() { return tr && tr.nodes()[0] === rect; }
      rect.on("mouseenter", function () {
        container.style.cursor = "move";
        if (!selected()) { rect.strokeWidth(1); rect.stroke("rgba(91,87,214,0.55)"); layer.draw(); }
      });
      rect.on("mouseleave", function () {
        container.style.cursor = "default";
        if (!selected()) { rect.strokeWidth(0); layer.draw(); }
      });
      rect.on("mousedown touchstart", function (e) { e.cancelBubble = true; });
      rect.on("click tap", function (e) { e.cancelBubble = true; pick(b.handle); });
      rect.on("dragmove", function () { serializeLive(rect); });
      rect.on("dragend", function () { serialize(rect); syncRectToElement(rect); });
      rect.on("transform", function () { serializeLive(rect); });
      rect.on("transformend", function () { normalize(rect); serialize(rect); syncRectToElement(rect); });
      layer.add(rect);
      rectByHandle[b.handle] = rect;
    });

    // click empty space → deselect
    stage.on("click tap", function (e) {
      if (e.target === stage) { tr.nodes([]); layer.draw(); }
    });
    layer.draw();

    // keep selection if the active slide already had one
    var selH = window.__studioSelected && window.__studioSelected[sid];
    if (selH && rectByHandle[selH]) attach(rectByHandle[selH]);
  }

  // ── Selection (canvas → panel) ────────────────────────────────
  window.__studioSelected = window.__studioSelected || {};
  function attach(rect) {
    if (!tr || !rect) return;
    // clear any leftover hover outline; the Transformer is the selection affordance
    Object.keys(rectByHandle).forEach(function (h) { rectByHandle[h].strokeWidth(0); });
    tr.nodes([rect]);
    tr.moveToTop();          // anchors MUST sit above the rects or grabs hit the rect
                             // (drag) instead of the handles (resize/rotate)
    layer.draw();
  }
  function pick(handle) {
    var sid = activeSid();
    window.__studioSelected[sid] = handle;
    attach(rectByHandle[handle]);
    selecting = true;                       // suppress the echo from selectZone
    try { if (window.selectZone) window.selectZone(sid, handle); } finally { selecting = false; }
  }

  // ── Selection (panel → canvas) ────────────────────────────────
  window.__onSelect = function (sid, handle) {
    if (selecting) return;                  // ignore our own canvas-origin call
    if (sid !== activeSid()) return;
    window.__studioSelected[sid] = handle;
    if (rectByHandle[handle]) attach(rectByHandle[handle]);
  };

  // ── Serialize a rect → tweaks (x/y/w/tilt), driving the live slide ──
  function geom(rect, live) {
    // live=true reads the in-flight scaled size without mutating the node.
    var rw = live ? rect.width() * rect.scaleX() : rect.width();
    var rh = live ? rect.height() * rect.scaleY() : rect.height();
    rw = Math.max(6, rw); rh = Math.max(6, rh);
    var cx = rect.x(), cy = rect.y();        // pivot = center (offset = size/2)
    return { rw: rw, rh: rh, leftPx: cx - rw / 2, topPx: cy - rh / 2, tilt: rect.rotation() };
  }
  function write(rect, g) {
    var sz = stageSize(), sid = activeSid(), h = rect.__handle;
    // x/y are translate DELTAS = current absolute position - the element's natural
    // origin (recovered at build). So preview == bake: the bake applies the same delta
    // to the same natural position. w/tilt stay absolute (width %, rotation deg).
    var nat = rect.__natural || { x: 0, y: 0 };
    var x = round(g.leftPx / sz.w * 100 - nat.x), y = round(g.topPx / sz.h * 100 - nat.y);
    var w = round(g.rw / sz.w * 100), t = round(g.tilt);
    var init = rect.__init || {};
    // Only write a prop the user actually moved off its starting value, so a pure
    // drag doesn't bake in the element's base width/rotation (epsilon absorbs the
    // sub-px measure noise).
    function chg(a, b) { return Math.abs(a - b) > 0.05; }
    if (chg(x, init.x)) window.applyToSlide(sid, h, "x", x);
    if (chg(y, init.y)) window.applyToSlide(sid, h, "y", y);
    if (chg(w, init.w)) window.applyToSlide(sid, h, "w", w);
    if (chg(t, init.tilt)) window.applyToSlide(sid, h, "tilt", t);
    syncPanel(sid, h, x, y, w, t);
  }
  function serializeLive(rect) { write(rect, geom(rect, true)); }
  function serialize(rect) { write(rect, geom(rect, false)); }

  // normalize an after-transform node: fold scale into width/height, keep center.
  function normalize(rect) {
    var rw = Math.max(6, rect.width() * rect.scaleX());
    var rh = Math.max(6, rect.height() * rect.scaleY());
    var cx = rect.x(), cy = rect.y();
    rect.setAttrs({ width: rw, height: rh, scaleX: 1, scaleY: 1, offsetX: rw / 2, offsetY: rh / 2, x: cx, y: cy });
    if (layer) layer.draw();
  }

  // After a commit, snap the rect back onto the element's ACTUAL rendered box. The
  // bake only honors width (height is CSS/auto), so a 2D resize makes the rect diverge
  // from an image whose height didn't follow — re-measuring glues the selector to what
  // the slide really shows. Also re-bases __init so the next edit diffs from the truth.
  function syncRectToElement(rect) {
    var sid = activeSid(), m = measureEl(sid, rect.__handle);
    if (!m) return;
    var sz = stageSize();
    var rw = Math.max(6, m.w / 100 * sz.w), rh = Math.max(6, m.h / 100 * sz.h);
    rect.setAttrs({
      width: rw, height: rh, offsetX: rw / 2, offsetY: rh / 2,
      x: m.x / 100 * sz.w + rw / 2, y: m.y / 100 * sz.h + rh / 2,
      rotation: m.rot, scaleX: 1, scaleY: 1,
    });
    rect.__init = { x: m.x, y: m.y, w: m.w, tilt: m.rot };
    if (tr && tr.nodes()[0] === rect) tr.forceUpdate();
    if (layer) layer.draw();
  }

  // Mirror the new values into the panel fields so the two stay in sync.
  function syncPanel(sid, h, x, y, w, tilt) {
    var grp = document.querySelector('.slide-panel[data-slide="' + sid + '"] .control-group[data-slot="' + h + '"]');
    if (!grp) return;
    function set(prop, val) {
      var inp = grp.querySelector('input[data-prop="' + prop + '"]');
      if (inp && document.activeElement !== inp) inp.value = val;
    }
    set("x", x); set("y", y); set("w", w); set("tilt", tilt);
  }

  // ── Enable / disable (toolbar toggle) ─────────────────────────
  window.__studioCanvas = {
    enable: function () { rebuild(); },
    disable: function () { teardown(); },
    rebuild: rebuild,
  };
  // Chain (do NOT clobber) so studio.js's slide-change hooks (e.g. texture sync) survive.
  var _prevOnSlideChange = window.__onSlideChange;
  window.__onSlideChange = function (activeId) {
    if (_prevOnSlideChange) { try { _prevOnSlideChange(activeId); } catch (e) {} }
    rebuild();
  };

  // ── Delete the selected layer (§4) ────────────────────────────
  // Delete / Backspace on the selected Konva rect removes that layer via the same
  // removeLayer path the trash button uses (LAYER_NN → hard delete; template zone →
  // removed:true). Guarded so it never fires while typing in a panel input.
  function deleteSelected() {
    var sid = activeSid();
    var handle = window.__studioSelected && window.__studioSelected[sid];
    if (!handle || !window.removeLayer) return false;
    window.removeLayer(sid, handle);
    if (tr) { tr.nodes([]); }
    if (window.__studioSelected) window.__studioSelected[sid] = null;
    rebuild();
    return true;
  }
  window.__studioDeleteSelected = deleteSelected;
  document.addEventListener("keydown", function (e) {
    if (e.key !== "Delete" && e.key !== "Backspace") return;
    var ae = document.activeElement;
    if (ae && /^(INPUT|TEXTAREA|SELECT)$/.test(ae.tagName)) return;  // don't hijack typing
    if (!window.__studioCanvasOn) return;
    if (deleteSelected()) e.preventDefault();
  });

  // a zone rect's centre + size in CONTAINER (stage) px — for tests / external probes.
  window.__studioRectInfo = function (handle) {
    var r = rectByHandle[handle];
    if (!r) return null;
    var cr = r.getClientRect();
    return { cx: cr.x + cr.width / 2, cy: cr.y + cr.height / 2, w: cr.width, h: cr.height };
  };

  // Initial build. The element geometry the rects mirror is only final once each
  // iframe has loaded AND any imported tweaks.json has been replayed onto it, so
  // build on load and re-measure shortly after to catch that settle.
  function boot() { if (window.__studioCanvasOn) { rebuild(); setTimeout(rebuild, 250); } }
  if (document.readyState === "complete") setTimeout(boot, 0);
  else window.addEventListener("load", boot);
})();
"""


def _free_port(preferred: int = 0) -> int:
    """Bind to a free port and return it. ``preferred=0`` lets the OS pick."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            s.bind(("127.0.0.1", preferred))
        except OSError:
            s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def _inject_shim(html: str, mode: str = "post") -> str:
    """Insert mode sentinel + <script src="/studio.js"> just before </body> (or append).

    In template mode also injects a <style> override that enlarges the canvas from the
    post-mode 440px/scale-0.407 to ~555px/scale-0.514, giving more working space when
    there is no social chrome.  Rationale: 555/1080 = 0.5139; height = 555*(1350/1080)
    = 693.75 ≈ 694px.  The !important declarations win over preview_editor.py's inline
    stylesheet without touching that file (constraint: preview_editor.py stays
    framing-agnostic).
    """
    tag = (
        f'<script>window.__studioMode={json.dumps(mode)};</script>'
        '<script src="/studio.js"></script>'
    )
    # Template-mode canvas enlargement — injected into <head> before first paint.
    canvas_override = (
        "<style>"
        ".slide-frame-wrap { width: 555px !important; height: 694px !important; }"
        ".slide-frame { transform: scale(0.514) !important; }"
        ".li-post { width: 555px !important; }"
        "</style>"
    ) if mode == "template" else ""

    low = html.lower()
    head_end = low.rfind("</head>")
    if canvas_override and head_end != -1:
        html = html[:head_end] + canvas_override + html[head_end:]
        low = html.lower()  # recompute after injection

    idx = low.rfind("</body>")
    if idx == -1:
        return html + tag
    return html[:idx] + tag + html[idx:]


# ─── THE MANIFEST ALIAS CONTRACT ──────────────────────────────────────────────
# The canonical manifest schema is ``{"id": ..., "file": "<pool-relative html>"}``
# (build_manifest.py / Phase 4.5 / Phase 5). The AI-first ``ssc-template-builder``
# instead hand-writes ``{"slug": ..., "template_html": <abs/rooted>, "template_dir":
# <abs/rooted>}`` (see ssc-template-builder.md Step 7) and never calls build_manifest.py.
# These two helpers normalize either shape to the canonical id/file at the READ
# boundary so the Studio resolves each template to its own dir instead of collapsing
# everything to the pool root.
#
# An IDENTICAL pair lives in viz-image-gen/scripts/render_template.py. The two
# readers sit in different skills with no shared import path, so the rule is
# duplicated verbatim — KEEP THE TWO COPIES IN SYNC.
def _manifest_entry_id(entry: dict) -> str:
    """Canonical id for a manifest entry, tolerant of the builder's native schema.

    Order: ``id`` (canonical) → ``slug`` (builder) → ``name`` → basename of
    ``template_dir``. Idempotent: a canonical entry returns its own ``id``.
    """
    explicit = entry.get("id") or entry.get("slug") or entry.get("name")
    if explicit:
        return explicit
    template_dir = entry.get("template_dir") or ""
    return Path(str(template_dir).replace("\\", "/")).name


def _manifest_entry_file(entry: dict, pool_name: str) -> str:
    """Pool-relative path to the entry's template HTML, tolerant of both schemas.

    Order: ``file`` (canonical, already pool-relative) → ``template_html`` →
    ``template_dir`` + ``/template.html`` → ``<id>/template.html``. Every candidate
    is made pool-relative by stripping everything up to and including
    ``templates/<pool>/`` (so a brand_context-rooted builder path like
    ``brand_context/templates/<pool>/cover-r01/template.html`` collapses to
    ``cover-r01/template.html``). Idempotent: a canonical ``file`` passes through.
    """
    def _pool_relative(raw: str) -> str:
        p = str(raw).replace("\\", "/")
        marker = f"templates/{pool_name}/"
        idx = p.rfind(marker)
        return p[idx + len(marker):] if idx != -1 else p

    file_field = entry.get("file")
    if file_field:
        return _pool_relative(file_field)
    template_html = entry.get("template_html")
    if template_html:
        return _pool_relative(template_html)
    template_dir = entry.get("template_dir")
    if template_dir:
        rel_dir = _pool_relative(template_dir).rstrip("/")
        return f"{rel_dir}/template.html"
    return f"{_manifest_entry_id(entry)}/template.html"


def _resolve_pool_templates(run: Path) -> list[dict]:
    """Walk the pool manifest to return renderable templates in manifest order.

    Each record contains:
      {"id": str, "template_dir": str, "ref": str, "render": str, "status": str}

    Discovery:
    - The pool dir is the nearest ancestor of ``run`` (up to 4 levels) that
      contains a ``manifest.json``.  This handles both the case where ``run`` IS
      a template_dir (manifest is in its parent) and the case where it is the
      pool dir itself.
    - If no manifest is found, falls back to a single record for ``run`` itself
      so that a lone template_dir still works (single-template pool).

    Manifest normalization mirrors render_template.py lines 390-421:
    - Accepts both ``templates[]`` and ``variations[]`` keys (Phase 4.5 / 5).
    - Accepts dict-keyed or list-keyed entries.
    - Strips the redundant ``templates/<pool>/`` prefix from ``file`` paths
      exactly as render_template does.

    Entries with ``status in {"ready", "approved", "needs-user-decision"}`` are
    included. ``needs-user-decision`` is a builder gate FALSE-POSITIVE flag that the
    user is meant to confirm IN the Studio — excluding it created a catch-22 (the
    template never appeared, so it could never be reviewed/approved). It surfaces
    flagged (``status`` is passed through to the UI) but is NOT auto-promoted; the
    user's /approve flips it to ``ready`` (see the /approve handler).
    """
    pool_dir: Path | None = None
    for d in [run, *list(run.parents)[:4]]:
        if (d / "manifest.json").is_file():
            pool_dir = d
            break

    if pool_dir is None:
        # No manifest → single-template fallback (run itself IS the template_dir)
        ref = run / "assets" / "ref-canonical.png"
        render = run / "preview.png"
        return [{
            "id": run.name,
            "template_dir": str(run),
            "ref": str(ref),
            "render": str(render),
            "status": "ready",
        }]

    try:
        manifest = json.loads(
            (pool_dir / "manifest.json").read_text(encoding="utf-8")
        )
    except (OSError, ValueError):
        ref = run / "assets" / "ref-canonical.png"
        render = run / "preview.png"
        return [{
            "id": run.name,
            "template_dir": str(run),
            "ref": str(ref),
            "render": str(render),
            "status": "ready",
        }]

    # Support bare-list manifests (legacy format) as well as the canonical
    # {"templates": [...]} dict form.  A bare list is treated as if it were
    # {"templates": [...]}.
    if isinstance(manifest, list):
        manifest = {"templates": manifest}

    entries = manifest.get("templates") or manifest.get("variations") or []
    if isinstance(entries, dict):
        entries = [
            {**v, "id": v.get("id", k)}
            for k, v in entries.items()
            if isinstance(v, dict)
        ]

    pool_name = pool_dir.name
    result: list[dict] = []
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        status = entry.get("status", "")
        if status not in {"ready", "approved", "needs-user-decision"}:
            continue
        # Normalize either schema (canonical id/file or builder slug/template_html/
        # template_dir) to canonical id/file — see THE MANIFEST ALIAS CONTRACT above.
        entry_id = _manifest_entry_id(entry)
        file_field = _manifest_entry_file(entry, pool_name)
        # Strip redundant templates/<pool>/ prefix (Phase 5 factory paths). The
        # alias helper already returns a pool-relative path, so this is a no-op for
        # builder/canonical entries — kept for any legacy path that slips through.
        redundant = f"templates/{pool_name}/"
        if file_field.startswith(redundant):
            file_field = file_field[len(redundant):]
        template_dir = (pool_dir / file_field).parent if file_field else pool_dir
        template_dir = template_dir.resolve()
        ref = template_dir / "assets" / "ref-canonical.png"
        render = template_dir / "preview.png"
        result.append({
            "id": entry_id,
            "template_dir": str(template_dir),
            "ref": str(ref),
            "render": str(render),
            "status": status,
            # Approval is a separate marker from status (status stays "ready");
            # surfaced so the conference UI can show which templates are approved.
            "approved": bool(entry.get("approved", False)),
        })

    if not result:
        # Manifest found but no renderable entries — fall back to single record
        ref = run / "assets" / "ref-canonical.png"
        render = run / "preview.png"
        return [{
            "id": run.name,
            "template_dir": str(run),
            "ref": str(ref),
            "render": str(render),
            "status": "ready",
        }]

    return result


def _read_template_card(template_dir: Path) -> str | None:
    """Return the builder's Template Card rationale for a template, if present.

    The ``ssc-template-builder`` writes its rationale (form, the identification-tree
    path it took, per-block AI-vs-HTML treatment + why, edit mode, extraction notes,
    safe-zone notes) into the template's ``instructions.md`` (see
    references/template-authoring/identification-tree.md "After identification").
    The Template Studio conference panel surfaces this next to the ref↔render
    compare as review notes / improvement suggestions (AIOS-190 W1, Gustavo's ask).

    Read-only: never mutates the template. Returns the markdown text or ``None``.
    """
    try:
        instr = (Path(template_dir) / "instructions.md")
        if not instr.is_file():
            return None
        text = instr.read_text(encoding="utf-8").strip()
        return text or None
    except (OSError, UnicodeDecodeError):
        return None


def _setup_template_run(run: Path) -> None:
    """Ensure a template directory (template.html at root) has a single-slide
    ``_slides/<id>/`` structure that _find_slides_info expects, so build_editor_html
    can open it without any changes to preview_editor.py.

    The builder's ``render_template.py --emit-edit-slide`` already writes a RICH
    slide dir (metadata.json carrying the authored ``data`` — text slots + the hero
    ``PHOTO_MAIN_PATH``). Its id is the output stem (e.g. ``preview``), NOT
    ``slide-01``. Adopt that emitted slide as-is so the editor shows the authored
    photo + sample text. Only when NO emitted slide exists do we fall back to a bare
    ``slide-01`` (sample-text-only). Seeding a bare slide-01 when a rich slide is
    present was the "template opens without the photo" bug.
    """
    if not (run / "template.html").is_file():
        return
    slides_root = run / "_slides"
    preview = run / "preview.png"
    # Prefer an already-emitted rich slide (metadata.json with a non-empty `data`).
    if slides_root.is_dir():
        for sd in sorted(p for p in slides_root.iterdir()
                         if p.is_dir() and p.name != "_shared"):
            meta_f = sd / "metadata.json"
            if not meta_f.is_file():
                continue
            try:
                m = json.loads(meta_f.read_text(encoding="utf-8"))
            except ValueError:
                continue
            if isinstance(m, dict) and m.get("data"):
                slide_png = run / f"{sd.name}.png"
                if preview.is_file() and not slide_png.is_file():
                    shutil.copy2(preview, slide_png)
                # Also seed a canonical slide-01.png baseline from the generated
                # preview so Approve-as-is (which resolves slide-01.png) always has a
                # baked slide even when the rich slide's id is NOT "slide-01" and the
                # user approves without editing (P0 #2 — approve the generated
                # template as v1). Idempotent: never overwrites an existing bake.
                baseline = run / "slide-01.png"
                if preview.is_file() and not baseline.is_file():
                    shutil.copy2(preview, baseline)
                return
    # Fallback: no emitted slide → bare slide-01 (sample-text-only render).
    slides_dir = slides_root / "slide-01"
    if not slides_dir.is_dir():
        slides_dir.mkdir(parents=True, exist_ok=True)
        meta = {"template_dir": str(run)}
        (slides_dir / "metadata.json").write_text(
            json.dumps(meta), encoding="utf-8"
        )
    slide_png = run / "slide-01.png"
    if preview.is_file() and not slide_png.is_file():
        shutil.copy2(preview, slide_png)


class StudioState:
    """Shared, immutable-ish config handed to every request handler."""

    def __init__(self, run: Path, brand_context: Path | None, mode: str = "post"):
        self.run = run
        self.brand_context = brand_context
        self.mode = mode
        self._editor_html_cache: str | None = None
        # Coarse lock serializing state mutations (/select-template) against the
        # bake-critical reads/writes of /apply, /approve, /decompose, /save so a
        # template swap can't redirect an in-flight bake to the wrong dir (P2 #12).
        # User-serial actions, not a hot path — a single coarse lock is fine.
        self.lock = threading.Lock()
        self._shutdown_fn = None  # set by serve() after httpd is created
        if mode == "template":
            # Pool-dir launch: when `run` is the POOL dir (manifest.json, no root
            # template.html), there is no editable slide to open — _setup_template_run
            # would early-return and the screen would be blank. Resolve the FIRST
            # renderable template from the manifest and retarget `run` to its dir so
            # the studio opens that template editable (P2 #13).
            if not (run / "template.html").is_file() and (run / "manifest.json").is_file():
                pool = _resolve_pool_templates(run)
                # Prefer a ready/approved template as the landing slide, but fall
                # back to ANY renderable entry (incl. needs-user-decision) so a pool
                # whose only entries await a user decision still opens editable.
                first = next((t for t in pool
                              if t.get("status") in {"ready", "approved"}), None)
                if first is None:
                    first = next(iter(pool), None)
                if first is not None:
                    cand = Path(first["template_dir"])
                    if (cand / "template.html").is_file():
                        self.run = cand
            _setup_template_run(self.run)
            # Resolve the pool's renderable templates once at startup; used by
            # /pool-templates (GET) and /compare-images (POST).
            self.pool_templates: list[dict] = _resolve_pool_templates(self.run)

    def editor_html(self) -> str:
        # Rebuilt fresh on every full GET so a re-save of tweaks.json is reflected
        # on reload; cheap relative to a bake. Cache only within a single request
        # isn't needed (one build per load).
        # AI-edit provider availability (studio-ai-edit) is re-resolved here too —
        # presence booleans only — so a key added to .env mid-session is one F5
        # away. The booleans gate the per-provider buttons in the build.
        html = build_editor_html(self.run, brand_context=self.brand_context,
                                 ai_edit_providers=_ai_edit_providers(self.run))
        return _inject_shim(html, self.mode)

    def slide_map(self) -> dict[str, dict]:
        out = {}
        for info in _find_slides_info(self.run):
            out[info["slide_id"]] = info
        return out


def _png_data_uri(path: Path) -> str:
    b = path.read_bytes()
    return "data:image/png;base64," + base64.b64encode(b).decode("ascii")


def _png_dimensions(path: Path) -> tuple[int, int] | None:
    """Read a PNG's (width, height) from its IHDR chunk using stdlib ``struct``.

    Full-AI slide PNGs are NOT a fixed size (the composed slide is 928x1152, the
    decompose layers 576x704, etc.), so the layer-canvas bake MUST run at the
    slide's TRUE resolution — never a hardcoded 1080x1350. The IHDR is always the
    first chunk after the 8-byte signature: 4-byte length, 4-byte type "IHDR",
    then width (uint32 BE) + height (uint32 BE). Returns None on any malformed
    read so the caller falls back gracefully.
    """
    try:
        with path.open("rb") as fh:
            sig = fh.read(8)
            if sig != b"\x89PNG\r\n\x1a\n":
                return None
            fh.read(8)  # length(4) + type(4); IHDR data begins at byte 16
            data = fh.read(8)
            if len(data) < 8:
                return None
            w, h = struct.unpack(">II", data)
            if w <= 0 or h <= 0:
                return None
            return int(w), int(h)
    except (OSError, struct.error):
        return None


def _ensure_layer_canvas_template(slide_id: str, info: dict, slide_tweaks: dict) -> Path | None:
    r"""Synthesize a throwaway template dir for a full-AI slide that carries layers.

    Returns a temp directory containing a ``template.html`` whose body is the
    original flat slide PNG as a full-frame ``<img data-slot="BACKGROUND">`` inside
    a ``<div class="slide">`` container. The decomposed ``LAYER_NN`` ``<img>``
    elements are NOT hand-written here — ``render_template._materialize_layers``
    injects them at bake time into the ``.slide`` container, using the data URIs
    already stored in each tweak's ``img`` key. This keeps the bake path identical
    to the templated case (RNDR-04: same injector, same data URI, same positioning).

    Returns None when the slide has no usable PNG or no ``LAYER_\d+`` tweak with an
    ``img`` (nothing to composite) — the caller then reports "not rebakable".

    Caller owns cleanup of the returned directory.
    """
    png_path = info.get("png_path")
    if not png_path:
        return None
    png_path = Path(png_path)
    if not png_path.is_file():
        return None

    # Bake the layer-canvas when the slide carries either a decomposed/added layer
    # OR a post-production texture overlay (Addendum 5) — both composite over the
    # original full-AI pixels. Without either there is nothing to add, so bail and let
    # the caller report it.
    has_layer = any(
        re.fullmatch(r"LAYER_\d+", str(name)) and isinstance(t, dict) and t.get("img")
        for name, t in (slide_tweaks or {}).items()
    )
    _tex = (slide_tweaks or {}).get("__texture")
    has_texture = isinstance(_tex, dict) and bool(_tex.get("tex"))
    if not has_layer and not has_texture:
        return None

    tdir = Path(tempfile.mkdtemp(prefix=f"cs-layercanvas-{slide_id}-"))
    bg_uri = _png_data_uri(png_path)
    # The BACKGROUND <img> preserves the un-decomposed pixels (a layer covering them
    # simply paints on top). width/height:100% lock it to the slide canvas whatever
    # the PNG's native size — the viewport is set to the real dims via --canvas.
    template_html = (
        "<!doctype html><html><head><meta charset='utf-8'>"
        # html,body MUST be height:100% — otherwise the height:100% .slide collapses
        # to 0, the absolutely-positioned BACKGROUND + injected layers get clipped,
        # and the bake comes out BLANK (verified: a 17 KB white PNG). Mirrors the
        # live promote srcdoc fix so preview == bake.
        "<style>html,body{margin:0;padding:0;height:100%}"
        ".slide{position:relative;width:100%;height:100%;overflow:hidden}</style>"
        "</head><body>"
        "<div class=\"slide\" style=\"position:relative;width:100%;height:100%\">"
        # Recolorable solid colour FLOOR (AIOS-139 Bug 2). The full-AI / decomposed
        # backdrop IS the BACKGROUND image, so without this there is no recolorable
        # surface beneath it: hiding the image (eye toggle → visible:false) revealed
        # nothing and `bgColor` had no element to land on. The floor sits at the LOWEST
        # z-index (z-index:0, first child), default TRANSPARENT (invisible until the
        # user recolours it via the BGFILL Fill control), and is revealed when the
        # image BACKGROUND above it is hidden. `bgColor` on BGFILL recolours it via the
        # standard _build_tweaks_css rule. MUST stay byte-identical to the live
        # promoteToLayerCanvas srcdoc (RNDR-04: preview == PNG).
        "<div data-slot=\"BGFILL\" "
        "style=\"position:absolute;inset:0;background:transparent;z-index:0\"></div>"
        f"<img data-slot=\"BACKGROUND\" src=\"{bg_uri}\" "
        "style=\"position:absolute;inset:0;width:100%;height:100%;object-fit:fill;z-index:1\">"
        "</div></body></html>"
    )
    (tdir / "template.html").write_text(template_html, encoding="utf-8")
    return tdir


def _rebake_template_preview(
    run: Path,
    tpl_dir: Path,
    brand_context: Path | None,
    *,
    slide_id: str = "slide-01",
    timeout: float = 60.0,
) -> dict:
    """Re-bake ``<tpl_dir>/preview.png`` from ``<tpl_dir>/tweaks.json``.

    THE single template-preview bake path — shared by ``/approve`` (save) and
    ``/compare-images`` (conference load) so the displayed render and the
    approved/baked PNG are produced the SAME way (preview == bake). Mirrors the
    proven ``_rebake_slide`` contract: render_template is invoked with the saved
    tweaks file passed EXPLICITLY (``--tweaks``) plus ``--tweaks-slide`` so
    ``_slide_id`` resolves to the canonical single-slide id (not the "preview"
    output stem, which never matches a slide-keyed tweaks file → white
    <img src="">), and ``--data`` from the slide's persisted metadata so
    PHOTO_MAIN_PATH resolves even with no imgSrc tweak.

    No-op-safe: when ``tweaks.json`` is absent there is nothing to honour, so the
    existing preview.png is left untouched and ``{"ok": True, "baked": False}``
    is returned (the caller then reads whatever preview already exists).

    Returns ``{"ok": bool, "baked": bool, "error"?: str}``. ``baked`` is True
    only when render_template actually re-rendered preview.png.
    """
    preview_png = tpl_dir / "preview.png"
    tweaks_file = tpl_dir / "tweaks.json"
    if not tweaks_file.is_file():
        return {"ok": True, "baked": False}

    # --data from the slide's persisted metadata (same resolution as /approve and
    # _rebake_slide) so image slots resolve without an explicit imgSrc tweak.
    data_path: str | None = None
    try:
        info = {i["slide_id"]: i for i in _find_slides_info(run)}.get(slide_id)
        data = (info or {}).get("data")
        if isinstance(data, dict) and data:
            with tempfile.NamedTemporaryFile(
                "w", suffix=".json", delete=False, encoding="utf-8"
            ) as df:
                json.dump(data, df)
                data_path = df.name
    except Exception:
        data_path = None

    _uv = shutil.which("uv")
    if _uv:
        cmd = [_uv, "run", "--no-project", str(RENDER_TEMPLATE)]
    else:
        cmd = [sys.executable, str(RENDER_TEMPLATE)]
    cmd += [
        "--template-dir", str(tpl_dir),
        "--output", str(preview_png),
        "--use-sample-text",
        "--tweaks", str(tweaks_file),
        "--tweaks-slide", slide_id,
    ]
    if data_path is not None:
        cmd += ["--data", data_path]
    if brand_context:
        cmd += ["--brand-context", str(brand_context)]

    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return {"ok": False, "baked": False, "error": "preview re-bake timed out"}
    finally:
        if data_path is not None:
            try:
                Path(data_path).unlink()
            except OSError:
                pass

    if proc.returncode != 0:
        err = (proc.stderr or proc.stdout or "render_template failed").strip()
        return {"ok": False, "baked": False,
                "error": _clean_subprocess_error(err, what="re-bake")}
    if not preview_png.is_file():
        return {"ok": False, "baked": False,
                "error": "preview re-bake produced no output"}
    return {"ok": True, "baked": True}


def _copy_preview_to_pool(pool_dir: Path, template_id: str, preview_png: Path) -> None:
    """Copy a freshly-baked preview to ``<pool_dir>/_preview/<id>.png`` — the path
    the gallery reads — so the conference and the gallery agree. Best-effort."""
    try:
        preview_dir = pool_dir / "_preview"
        preview_dir.mkdir(exist_ok=True)
        shutil.copy2(preview_png, preview_dir / f"{template_id}.png")
    except OSError:
        pass


def _find_pool_dir(run: Path) -> Path:
    """The nearest of ``run`` / its ancestors (≤4 levels) holding a manifest.json —
    the pool dir. Falls back to ``run.parent`` (mirrors /approve's discovery)."""
    for d in [run, *list(run.parents)[:4]]:
        if (d / "manifest.json").is_file():
            return d
    return run.parent


def _preview_version(preview_png: Path) -> str:
    """A short cache-buster token derived from preview.png's bytes — changes
    whenever the baked preview changes, so the conference image URL can append
    ``?v=<token>`` and the browser never shows a cached stale image."""
    try:
        import hashlib
        return hashlib.sha1(preview_png.read_bytes()).hexdigest()[:12]
    except OSError:
        return "0"


def _rebake_slide(state: StudioState, slide_id: str, tweaks: dict) -> dict:
    """Run render_template.py --tweaks for one slide; return {slide, ok, png|error}.

    Mirrors the Phase 7.6 apply-back invocation exactly — the server adds no bake
    logic of its own (RNDR-04 parity is inherited from render_template).
    """
    info = state.slide_map().get(slide_id)
    if not info:
        return {"slide": slide_id, "ok": False, "error": "unknown slide"}
    tdir = info.get("template_dir")

    # Full-AI slide (no template): if its tweaks carry decomposed/added LAYER_NN
    # assets, synthesize a throwaway "layer-canvas" template (original PNG as the
    # BACKGROUND <img>, layers injected by _materialize_layers at bake) and bake
    # THAT at the slide's native resolution via --canvas WxH. This is the §1 path
    # that unblocks Magic Layer / Add-Image on full-AI slides. Without layers there
    # is genuinely nothing to rebake, so report it.
    layer_tdir: Path | None = None
    extra_args: list[str] = []
    if not tdir:
        slide_tweaks = tweaks.get(slide_id, {}) if isinstance(tweaks, dict) else {}
        layer_tdir = _ensure_layer_canvas_template(slide_id, info, slide_tweaks)
        if layer_tdir is None:
            return {
                "slide": slide_id, "ok": False,
                "error": "no template and no layers/texture — not rebakable",
            }
        tdir = layer_tdir
        png_path = info.get("png_path")
        dims = _png_dimensions(Path(png_path)) if png_path else None
        if dims:
            extra_args = ["--canvas", f"{dims[0]}x{dims[1]}"]

    # r5f F2 — self-heal an OLDER emit that isn't self-contained: emit_edit_slide
    # used to copy only assets/ + _ai_bg/, so a template-root ref (bg.png) was left
    # behind and the --template-dir rebake baked without it (white background).
    # Copy any still-missing relative ref from metadata.json's source_template_dir
    # into the slide dir before baking. Best-effort: never blocks the bake.
    if tdir is not None and layer_tdir is None:
        try:
            meta_file = Path(tdir) / "metadata.json"
            tmpl_file = Path(tdir) / "template.html"
            if meta_file.is_file() and tmpl_file.is_file():
                meta = json.loads(meta_file.read_text(encoding="utf-8"))
                std = meta.get("source_template_dir")
                if std and Path(std).is_dir() and Path(std).resolve() != Path(tdir).resolve():
                    from render_template import copy_template_relative_assets  # type: ignore[import]
                    copy_template_relative_assets(
                        tmpl_file.read_text(encoding="utf-8", errors="ignore"),
                        Path(std), Path(tdir))
        except Exception:
            pass

    out_png = state.run / f"{slide_id}.png"
    # Write the full tweaks object to a temp file; --tweaks-slide selects the
    # per-slide sub-dict (same contract as the documented Phase 7.6 command).
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as tf:
        json.dump(tweaks, tf)
        tweaks_path = tf.name

    # AIOS-139 Addendum 8 #1 — when the slide carries its REAL persisted copy
    # (metadata.json `data`), rebake against THAT (not sample text), so the baked
    # PNG matches the editor's live preview of the actual post. --use-sample-text
    # stays as the floor: render_template merges samples only for slots the real
    # data doesn't set. Fixtures/demo without `data` keep the sample-text path.
    data_path: str | None = None
    real_data = info.get("data") if isinstance(info, dict) else None
    if isinstance(real_data, dict) and real_data:
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as df:
            json.dump(real_data, df)
            data_path = df.name

    # render_template.py declares playwright via PEP-723 inline metadata, so it MUST
    # run under `uv run` (which resolves it in an ephemeral env) — exactly like the
    # decompose path. A bare `sys.executable` runs it in the studio's own env, which
    # is stdlib-only and has NO playwright → every bake fails "playwright not
    # installed". Prefer uv; fall back to the current interpreter only when uv is
    # absent (then playwright must already be importable).
    _uv = shutil.which("uv")
    if _uv:
        cmd = [_uv, "run", "--no-project", str(RENDER_TEMPLATE)]
    else:
        cmd = [sys.executable, str(RENDER_TEMPLATE)]
    cmd += [
        "--template-dir", str(tdir),
        "--use-sample-text",
        "--output", str(out_png),
        "--tweaks", tweaks_path,
        "--tweaks-slide", slide_id,
    ]
    if data_path is not None:
        cmd += ["--data", data_path]
    cmd += extra_args
    if state.brand_context:
        cmd += ["--brand-context", str(state.brand_context)]

    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    except subprocess.TimeoutExpired:
        return {"slide": slide_id, "ok": False, "error": "bake timed out"}
    finally:
        try:
            Path(tweaks_path).unlink()
        except OSError:
            pass
        if data_path is not None:
            try:
                Path(data_path).unlink()
            except OSError:
                pass
        # Clean up the synthesized layer-canvas template dir (§1).
        if layer_tdir is not None:
            shutil.rmtree(layer_tdir, ignore_errors=True)

    if proc.returncode != 0:
        # Route raw subprocess stderr through _clean_subprocess_error so the toast
        # never leaks a Python traceback / stderr tail (parity with /post) — P2 #5.
        err = (proc.stderr or proc.stdout or "render_template failed").strip()
        return {"slide": slide_id, "ok": False,
                "error": _clean_subprocess_error(err, what="bake")}
    if not out_png.is_file():
        return {"slide": slide_id, "ok": False, "error": "no PNG produced"}
    return {"slide": slide_id, "ok": True, "png": _png_data_uri(out_png)}


def _affected_slides(tweaks: dict) -> list[str]:
    """Slide ids in the tweaks object (every top-level key except 'global')."""
    return [k for k in tweaks.keys() if k != "global" and isinstance(tweaks.get(k), dict)]


def _publishable_media(run: Path) -> list[Path]:
    """Resolve the baked slide PNGs to publish, sorted by slide index.

    Content Studio bakes EVERY slide — full-AI / template / hybrid — to the same
    ``slide-<NN>.png`` name in the run folder, so the production method is invisible
    here by design. publish_rest.py's ``autodetect_media`` only finds these for a
    ``format: carousel`` post (its ``single`` branch looks for ``image.png``), which
    left a SINGLE full-AI image (``slide-01.png``, format inferred ``single``)
    silently un-publishable — the real "full-AI publish is blocked" symptom. By
    resolving the media here and passing it via ``--media``, Publish works regardless
    of how the image was produced or whether the post is single or carousel.
    Returns [] when no baked slide exists (caller then falls back to autodetect).
    """
    def _idx(p: Path) -> int:
        m = re.search(r"(\d+)", p.stem)
        return int(m.group(1)) if m else 0

    return sorted(run.glob("slide-*.png"), key=_idx)


def _next_layer_handle(run: Path, slide_id: str, extra_handles: list[str] | None = None) -> str:
    """Pick the next free ``LAYER_NN`` index for a slide (§3 Add-Image).

    Scans, in order of authority:
      * the live handles the client passes (``extra_handles``) — these include
        freshly-decomposed-but-unsaved LAYER_NN entries,
      * the saved ``tweaks.json`` for that slide,
      * the persisted ``run/_assets/<slide_id>/asset-N.png`` backups,
    and returns ``LAYER_<max+1>`` (zero-padded to 2) so a new asset never collides
    with an existing layer on the same slide.
    """
    max_idx = -1

    def _scan(names) -> None:
        nonlocal max_idx
        for name in names or []:
            m = re.fullmatch(r"LAYER_(\d+)", str(name))
            if m:
                max_idx = max(max_idx, int(m.group(1)))

    _scan(extra_handles)

    saved = run / "tweaks.json"
    if saved.is_file():
        try:
            data = json.loads(saved.read_text(encoding="utf-8"))
            _scan((data.get(slide_id) or {}).keys())
        except (ValueError, OSError, AttributeError):
            pass

    assets_dir = run / "_assets" / slide_id
    if assets_dir.is_dir():
        # asset-N.png backups map 1:1 onto LAYER indices written so far.
        for p in assets_dir.glob("asset-*.png"):
            m = re.fullmatch(r"asset-(\d+)", p.stem)
            if m:
                max_idx = max(max_idx, int(m.group(1)))

    return "LAYER_" + f"{max_idx + 1:02d}"


def _save_added_asset(run: Path, slide_id: str, index: int, data_uri: str) -> Path | None:
    """Persist an added image to ``run/_assets/<slide_id>/asset-<index>.png``.

    The data URI is the canonical, parity-safe ``img`` source the bake reads
    verbatim; this on-disk copy is a durable backup (survives save/load, useful
    for export). Returns the written path, or None if the data URI is unusable.
    Best-effort: never raises.
    """
    m = re.match(r"data:image/[^;]+;base64,(.*)$", data_uri or "", re.DOTALL)
    if not m:
        return None
    try:
        raw = base64.b64decode(m.group(1), validate=False)
    except (ValueError, base64.binascii.Error):  # type: ignore[attr-defined]
        return None
    try:
        adir = run / "_assets" / slide_id
        adir.mkdir(parents=True, exist_ok=True)
        out = adir / f"asset-{index:02d}.png"
        out.write_bytes(raw)
        return out
    except OSError:
        return None


def _yaml_scalar(v) -> str:
    """Quote a scalar for the human-readable publish-log.yaml line (no PyYAML dep).

    Wraps in double quotes and escapes embedded quotes/newlines so the appended
    line stays valid YAML for anything (URLs, error tails) the publisher returns.
    """
    s = "" if v is None else str(v)
    s = s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ").replace("\r", " ")
    return f'"{s}"'


def _read_post_yaml_key(run: Path, key: str) -> str | None:
    """Read a simple scalar from post.yaml by key name. Best-effort; never raises."""
    p = run / "post.yaml"
    if not p.is_file():
        return None
    prefix = key + ":"
    try:
        for line in p.read_text(encoding="utf-8").splitlines():
            s = line.strip()
            if not s.startswith(prefix):
                continue
            val = s[len(prefix):].strip()
            if not val:
                return None
            if len(val) >= 2 and val[0] == '"' and val[-1] == '"':
                val = val[1:-1].replace('\\"', '"').replace("\\\\", "\\")
            elif len(val) >= 2 and val[0] == "'" and val[-1] == "'":
                val = val[1:-1]
            return val or None
    except OSError:
        pass
    return None


def _patch_first_comment_yaml(run: Path, value: str) -> None:
    """Set or remove first_comment: in post.yaml (line-based, no PyYAML). Best-effort.

    Preserves all other keys. Removes the key when value is empty so publish_rest
    gets None and skips the first comment, matching the CLI no-arg behaviour.
    """
    try:
        p = run / "post.yaml"
        existing = p.read_text(encoding="utf-8").splitlines() if p.is_file() else []
        kept = [ln for ln in existing if not re.match(r"^first_comment\s*:", ln)]
        if value:
            kept.append(f"first_comment: {_yaml_scalar(value)}")
        text = "\n".join(kept)
        if kept and not text.endswith("\n"):
            text += "\n"
        p.write_text(text, encoding="utf-8")
    except OSError:
        pass


def _ensure_post_yaml(run: Path, platform: str) -> None:
    """Make sure a minimal ``post.yaml`` exists for publish_rest.py.

    publish_rest.py's ``parse_post_yaml`` hard-fails when ``post.yaml`` is absent,
    but a Content Studio run may only have ``caption.md`` + the baked ``slide-*.png``.
    Synthesize a minimal manifest (platform + format inferred from slide count) so
    the Publish flow is self-sufficient. Never overwrites an existing post.yaml.
    Best-effort — a write failure surfaces later as a clean publish_rest error.
    """
    p = run / "post.yaml"
    if p.is_file():
        return
    try:
        n = len(list(run.glob("slide-*.png")))
        fmt = "carousel" if n > 1 else "single"
        lines = []
        if platform:
            lines.append(f"platform: {platform}")
        lines.append(f"format: {fmt}")
        p.write_text("\n".join(lines) + "\n", encoding="utf-8")
    except OSError:
        pass


def _persist_publish_result(run: Path, platform: str, mode: str, result: dict) -> None:
    """Persist a /post outcome to the run folder so it "goes to logs/yaml".

    Writes/overwrites ``run/post-result.json`` (the full last result) AND appends a
    human-readable entry to ``run/publish-log.yaml`` (timestamp, platform, mode,
    status, post_id/url or error). Best-effort: any failure is swallowed so it
    NEVER crashes the /post response.
    """
    try:
        (run / "post-result.json").write_text(
            json.dumps(result, indent=2), encoding="utf-8")
    except (OSError, TypeError, ValueError):
        pass

    try:
        ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        ok = bool(result.get("ok", False))
        status = result.get("status") or ("ok" if ok else "failed")
        post_id = result.get("post_id") or result.get("postId") or ""
        url = result.get("post_url") or result.get("postUrl") or result.get("scheduled_for") or ""
        err = result.get("error") or result.get("reason") or ""
        line = (
            f"- timestamp: {_yaml_scalar(ts)}\n"
            f"  platform: {_yaml_scalar(platform)}\n"
            f"  mode: {_yaml_scalar(mode)}\n"
            f"  ok: {'true' if ok else 'false'}\n"
            f"  status: {_yaml_scalar(status)}\n"
        )
        if post_id:
            line += f"  post_id: {_yaml_scalar(post_id)}\n"
        if url:
            line += f"  url: {_yaml_scalar(url)}\n"
        if err:
            line += f"  error: {_yaml_scalar(err)}\n"
        with (run / "publish-log.yaml").open("a", encoding="utf-8") as fh:
            fh.write(line)
    except OSError:
        pass

    # AIOS-139 Addendum 8 #2 — on a successful publish, also patch post.yaml and
    # append the aggregated {output_base}/publish-log.md row (what the MCP flow
    # automated; Content Studio now does it for the REST path).
    if bool(result.get("ok", False)):
        _patch_post_yaml(run, result)
        _append_publish_log_md(run, platform, result)


def _patch_post_yaml(run: Path, result: dict) -> None:
    """Set ``status: published`` + a ``publish:`` block on the run's post.yaml
    (AIOS-139 Addendum 8 #2 / zernio-rest-fallback.md). Stdlib only — line-based
    patch, no PyYAML. Best-effort; never raises."""
    try:
        p = run / "post.yaml"
        existing = p.read_text(encoding="utf-8").splitlines() if p.is_file() else []
        # Drop any prior top-level `status:` and the whole prior `publish:` block.
        kept: list[str] = []
        in_publish = False
        for ln in existing:
            if re.match(r"^status\s*:", ln):
                continue
            if re.match(r"^publish\s*:\s*$", ln):
                in_publish = True
                continue
            if in_publish:
                if ln.strip() == "" or ln[:1] in (" ", "\t"):
                    continue  # still inside the indented publish block
                in_publish = False
            kept.append(ln)
        published_at = (result.get("published_at") or result.get("publishedAt")
                        or time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
        post_id = (result.get("platform_post_id") or result.get("post_id")
                   or result.get("postId") or "")
        url = result.get("post_url") or result.get("postUrl") or ""
        body = [ln for ln in kept if ln.strip() != ""]
        block = [
            "status: published",
            "",
            *body,
            "",
            "publish:",
            "  status: published",
            f"  published_at: {_yaml_scalar(published_at)}",
        ]
        if post_id:
            block.append(f"  platform_post_id: {_yaml_scalar(str(post_id))}")
        if url:
            block.append(f"  post_url: {_yaml_scalar(url)}")
        block.append("  error: ~")
        p.write_text("\n".join(block).rstrip() + "\n", encoding="utf-8")
    except OSError:
        pass


def _append_publish_log_md(run: Path, platform: str, result: dict) -> None:
    """Append the pipe-row to the system-wide ``{output_base}/publish-log.md``
    (run = {output_base}/{date}/{slug}). The documented aggregated history."""
    try:
        slug = run.name
        output_base = run.parent.parent  # …/{output_base}/{date}/{slug}
        ts = time.strftime("%Y-%m-%dT%H:%M", time.gmtime())
        status = result.get("status") or "published"
        url = result.get("post_url") or result.get("postUrl") or result.get("scheduled_for") or ""
        log = output_base / "publish-log.md"
        row = f"| {ts} | {platform or '-'} | {slug} | {status} | {url} |\n"
        header = ""
        if not log.is_file():
            header = ("# Publish log\n\n"
                      "| timestamp | platform | slug | status | url |\n"
                      "|---|---|---|---|---|\n")
        with log.open("a", encoding="utf-8") as fh:
            fh.write(header + row)
    except OSError:
        pass


def make_handler(state: StudioState):
    class Handler(BaseHTTPRequestHandler):
        # Quiet logging — one studio, low traffic.
        def log_message(self, fmt, *args):  # noqa: N802
            pass

        # ── helpers ──────────────────────────────────────────
        def _send(self, code: int, body: bytes, ctype: str):
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)

        def _json(self, code: int, obj: dict):
            self._send(code, json.dumps(obj).encode("utf-8"), "application/json")

        def _read_json(self) -> dict:
            n = int(self.headers.get("Content-Length", 0) or 0)
            if not n:
                return {}
            raw = self.rfile.read(n)
            try:
                return json.loads(raw.decode("utf-8"))
            except (ValueError, UnicodeDecodeError):
                return {}

        # ── GET ──────────────────────────────────────────────
        def do_GET(self):  # noqa: N802
            path = self.path.split("?", 1)[0]
            if path in ("/", "/index.html"):
                try:
                    html = state.editor_html()
                except Exception as e:  # surfacing build errors beats a blank page
                    self._send(500, f"editor build failed: {e}".encode("utf-8"), "text/plain")
                    return
                self._send(200, html.encode("utf-8"), "text/html; charset=utf-8")
                return
            if path == "/studio.js":
                self._send(200, STUDIO_JS.encode("utf-8"), "application/javascript")
                return
            if path == "/canvas.js":
                self._send(200, CANVAS_JS.encode("utf-8"), "application/javascript")
                return
            if path == "/konva.min.js":
                if KONVA_JS.is_file():
                    self._send(200, KONVA_JS.read_bytes(), "application/javascript")
                else:
                    self._send(404, b"konva not vendored", "text/plain")
                return
            if path == "/zernio-logo.png":
                if ZERNIO_LOGO.is_file():
                    self._send(200, ZERNIO_LOGO.read_bytes(), "image/png")
                else:
                    self._send(404, b"zernio logo not vendored", "text/plain")
                return
            if path == "/agentic-logo.png":
                if AGENTIC_LOGO.is_file():
                    self._send(200, AGENTIC_LOGO.read_bytes(), "image/png")
                else:
                    self._send(404, b"agentic logo not vendored", "text/plain")
                return
            if path == "/healthz":
                self._send(200, b"ok", "text/plain")
                return
            if path == "/shutdown":
                self._json(200, {"ok": True})
                if state._shutdown_fn:
                    threading.Thread(target=state._shutdown_fn, daemon=True).start()
                return
            # /fonts/<filename> — serve brand font files so srcdoc @font-face
            # resolves them via HTTP (fix #3: fonts in Studio canvas).
            # Only serves from brand_context/visual-identity/fonts/; rejects
            # path-traversal attempts by checking the resolved parent.
            if path.startswith("/fonts/"):
                _fname = path[len("/fonts/"):]
                if state.brand_context and _fname and ".." not in _fname:
                    _font_path = (state.brand_context / "visual-identity"
                                  / "fonts" / _fname).resolve()
                    _font_root = (state.brand_context / "visual-identity"
                                  / "fonts").resolve()
                    if (_font_path.parent == _font_root
                            and _font_path.is_file()):
                        _ext = _font_path.suffix.lower()
                        _mime = ("font/woff2" if _ext == ".woff2"
                                 else "font/ttf" if _ext == ".ttf"
                                 else "application/octet-stream")
                        self._send(200, _font_path.read_bytes(), _mime)
                        return
                self._send(404, b"font not found", "text/plain")
                return
            if path == "/slide-info":
                # Return {slides: {slide_id: {is_full_ai: bool}}, hasFalKey} so the
                # client can gate the "Break into layers" button by both the slide
                # type (Refinement 1) and FAL_KEY presence (mirrors the Publish
                # button's ZERNIO_API_KEY gating — same per-run .env source).
                slide_map = state.slide_map()
                info_out = {}
                for sid, info in slide_map.items():
                    is_full_ai = not bool(info.get("template_dir"))
                    info_out[sid] = {
                        "is_full_ai": is_full_ai,
                        # Templated slide whose AI hero (photo_main) can be broken into
                        # layers — drives the Magic Layer suggestion on e.g. the C
                        # "integrated headline" template (text baked into the scene).
                        "decomposable_hero": (not is_full_ai)
                                             and _resolve_hero_image(info) is not None,
                    }
                self._json(200, {
                    "ok": True,
                    "slides": info_out,
                    "hasFalKey": bool(_fal_key(state.run)),
                    # studio-ai-edit: presence-only provider booleans (hasFalKey
                    # precedent) so the client can re-check availability without
                    # a reload. The editor BUILD remains the gate that renders
                    # the per-provider buttons.
                    "aiEditProviders": _ai_edit_providers(state.run),
                })
                return
            if path == "/zernio-key":
                # FASE 6 §2: re-read ZERNIO_API_KEY from the .env on EVERY request (no
                # caching) so a credential added after launch works without a restart.
                # _zernio_key_present walks the run folder's .env fresh each call.
                self._json(200, {"ok": True, "hasKey": _zernio_key_present(state.run)})
                return
            if path == "/download":
                # Stream the baked slide PNGs as a zip (the topbar Download action).
                # Apply writes the live rebake to slide-<NN>.png, so this is always the
                # current output regardless of how each slide was produced.
                import io as _io
                import zipfile as _zip
                pngs = _publishable_media(state.run)
                if not pngs:
                    self._send(404, b"no baked slides to download yet", "text/plain")
                    return
                buf = _io.BytesIO()
                with _zip.ZipFile(buf, "w", _zip.ZIP_DEFLATED) as zf:
                    for p in pngs:
                        zf.write(p, arcname=p.name)
                data = buf.getvalue()
                self.send_response(200)
                self.send_header("Content-Type", "application/zip")
                self.send_header("Content-Disposition", 'attachment; filename="slides.zip"')
                self.send_header("Content-Length", str(len(data)))
                self.send_header("Cache-Control", "no-store")
                self.end_headers()
                self.wfile.write(data)
                return
            if path == "/load":
                t = state.run / "tweaks.json"
                c = state.run / "comments.json"
                payload = {
                    "ok": True,
                    "hasTweaks": t.is_file(),
                    "hasComments": c.is_file(),
                    # Piggyback key-presence so the Publish button can disable cleanly
                    # without a second round-trip.
                    "hasZernioKey": _zernio_key_present(state.run),
                    # first_comment survives refresh — panel pre-populates from this.
                    "firstComment": _read_post_yaml_key(state.run, "first_comment") or "",
                }
                try:
                    if t.is_file():
                        payload["tweaks"] = json.loads(t.read_text(encoding="utf-8"))
                    if c.is_file():
                        payload["comments"] = json.loads(c.read_text(encoding="utf-8"))
                except ValueError as e:
                    payload = {"ok": False, "error": f"corrupt state file: {e}"}
                self._json(200, payload)
                return
            if path == "/pool-templates":
                # Template mode: return ordered list of renderable templates for the
                # conference UI (id + status only — no absolute paths exposed).
                if state.mode != "template":
                    self._json(400, {"ok": False, "error": "pool-templates only available in template mode"})
                    return
                slim = [{"id": t["id"], "status": t["status"],
                         "approved": t.get("approved", False)}
                        for t in state.pool_templates]
                # The currently-active editing template (state.run) — lets the main
                # screen's prev/next arrows compute the next/prev template id.
                _active = None
                for t in state.pool_templates:
                    try:
                        if Path(t["template_dir"]).resolve() == state.run.resolve():
                            _active = t["id"]; break
                    except (KeyError, OSError):
                        continue
                self._json(200, {"ok": True, "templates": slim, "active": _active})
                return
            self._send(404, b"not found", "text/plain")

        # ── POST ─────────────────────────────────────────────
        def do_POST(self):  # noqa: N802
            path = self.path.split("?", 1)[0]
            body = self._read_json()

            if path == "/select-template":
                # Multi-template editing: switch the ACTIVE editing template within
                # one session so the editor canvas, Apply and Approve all retarget
                # the chosen template (the client reloads to rebuild the editor).
                if state.mode != "template":
                    self._json(400, {"ok": False, "error": "select-template only in template mode"})
                    return
                tid = body.get("template_id") or ""
                rec = None
                if hasattr(state, "pool_templates"):
                    rec = next((t for t in state.pool_templates if t["id"] == tid), None)
                if rec is None:
                    self._json(200, {"ok": False, "error": f"unknown template_id: {tid!r}"})
                    return
                new_run = Path(rec["template_dir"])
                if not (new_run / "template.html").is_file():
                    self._json(200, {"ok": False, "error": f"{tid}: no editable template.html"})
                    return
                # Hold the lock around the state swap so an in-flight /apply,
                # /approve, /decompose or /save can't read a half-swapped state.run
                # and bake into the wrong template dir (P2 #12).
                with state.lock:
                    state.run = new_run
                    _setup_template_run(new_run)
                    state.pool_templates = _resolve_pool_templates(new_run)
                    state._editor_html_cache = None
                self._json(200, {"ok": True, "active": tid})
                return

            if path == "/save":
                tweaks = body.get("tweaks") or {}
                comments = body.get("comments") or {}
                caption = body.get("caption")
                n_comments = sum(len(v or []) for v in comments.values()) if isinstance(comments, dict) else 0
                # Serialize against /select-template so a save targets a stable
                # state.run, never one being swapped mid-write (P2 #12).
                with state.lock:
                    try:
                        (state.run / "tweaks.json").write_text(
                            json.dumps(tweaks, indent=2), encoding="utf-8")
                        if n_comments:
                            (state.run / "comments.json").write_text(
                                json.dumps(comments, indent=2), encoding="utf-8")
                        # FASE 6 §5: persist the edited caption to caption.md (the Zernio
                        # publish `content`). Only write when provided so a tweaks-only save
                        # never clobbers the caption.
                        if isinstance(caption, str):
                            (state.run / "caption.md").write_text(caption, encoding="utf-8")
                        # AIOS-131: persist first_comment to post.yaml when provided.
                        first_comment = body.get("first_comment")
                        if isinstance(first_comment, str):
                            _patch_first_comment_yaml(state.run, first_comment)
                    except OSError as e:
                        self._json(200, {"ok": False, "error": str(e)})
                        return
                self._json(200, {"ok": True, "nComments": n_comments})
                return

            if path == "/save-caption":
                # Lightweight per-blur caption persist (FASE 6 §5) → caption.md is the
                # Zernio POST `content`, so editing the caption changes what's posted.
                caption = body.get("caption")
                if not isinstance(caption, str):
                    self._json(400, {"ok": False, "error": "caption (string) required"})
                    return
                try:
                    (state.run / "caption.md").write_text(caption, encoding="utf-8")
                except OSError as e:
                    self._json(200, {"ok": False, "error": str(e)})
                    return
                self._json(200, {"ok": True})
                return

            if path == "/save-first-comment":
                # Lightweight per-blur first-comment persist (AIOS-131) →
                # post.yaml first_comment: is the single source for CLI and front.
                first_comment = body.get("first_comment")
                if not isinstance(first_comment, str):
                    self._json(400, {"ok": False, "error": "first_comment (string) required"})
                    return
                _patch_first_comment_yaml(state.run, first_comment)
                self._json(200, {"ok": True})
                return

            if path == "/apply":
                tweaks = body.get("tweaks") or {}
                slides = body.get("slides") or _affected_slides(tweaks)
                if not slides:
                    self._json(200, {"ok": True, "results": []})
                    return
                # Hold the lock across the whole bake so a /select-template can't
                # swap state.run mid-bake → never writes to the wrong template dir
                # (P2 #12). _rebake_slide reads state.run; it never re-acquires.
                with state.lock:
                    results = [_rebake_slide(state, sid, tweaks) for sid in slides]
                self._json(200, {"ok": True, "results": results})
                return

            # ── /decompose (FASE 2 — Magic Layer) ──────────────────────────
            if path == "/decompose":
                slide_id = body.get("slide_id") or ""
                if not slide_id:
                    self._json(400, {"ok": False, "error": "slide_id required"})
                    return

                # Snapshot state.run under the lock so a /select-template swap can't
                # redirect this decompose's slide lookup, scratch dir or .env mid-flight
                # (P2 #12). Snapshot-and-release (vs holding through the ~180s subprocess)
                # keeps the UI responsive while still pinning the target dir.
                with state.lock:
                    run = state.run
                    info = {i["slide_id"]: i
                            for i in _find_slides_info(run)}.get(slide_id)
                if not info:
                    self._json(404, {"ok": False, "error": f"unknown slide: {slide_id}"})
                    return

                # Source image to decompose:
                #  • full-AI slide  → the flat slide PNG.
                #  • templated slide → the AI HERO (photo_main) baked into it, so a
                #    template like the C "integrated headline" (text baked into the
                #    scene) can be broken into editable text layers. Reject only when
                #    a templated slide has no AI hero to work on.
                if info.get("template_dir"):
                    slot = body.get("slot") or body.get("handle") or ""
                    png_path = (_resolve_slot_image(info, slot) if slot
                                else _resolve_hero_image(info))
                    if png_path is None:
                        self._json(200, {
                            "ok": False,
                            "error": (f"no resolvable image for slot {slot!r}" if slot
                                      else "no AI hero (photo_main) on this template to decompose"),
                        })
                        return
                else:
                    png_path = info.get("png_path")
                if not png_path or not Path(png_path).is_file():
                    self._json(200, {
                        "ok": False,
                        "error": f"source image not found for {slide_id}",
                    })
                    return

                # Fail-soft when the sibling skill is missing (no import-time assert;
                # parity with RENDER_TEMPLATE / PUBLISH_REST). Clean error, never a crash.
                if not DECOMPOSE.is_file():
                    self._json(200, {
                        "ok": False,
                        "status": "error",
                        "error": "layer decomposition unavailable — decompose.py not found in install",
                    })
                    return

                # Write decompose output to a per-run scratch dir.
                scratch = run / "_decompose" / slide_id
                scratch.mkdir(parents=True, exist_ok=True)

                # decompose.py declares its fal-client/requests deps via PEP-723
                # inline metadata, so it MUST run under `uv run` (which resolves
                # them in an ephemeral env) — plain `sys.executable` would fail
                # with "fal-client not installed" since fal-client is optional and
                # not a main pack dependency. Prefer uv; fall back to the current
                # interpreter only when uv is absent (then fal-client must already
                # be importable, else decompose fail-safes to status:error).
                _uv = shutil.which("uv")
                if _uv:
                    cmd = [_uv, "run", "--no-project", str(DECOMPOSE)]
                else:
                    cmd = [sys.executable, str(DECOMPOSE)]
                cmd += ["--image", str(png_path), "--output-dir", str(scratch)]
                # decompose.py reads FAL_KEY from os.environ. Resolve it the same
                # way as the Zernio key (nearest .env walked up from the run folder)
                # and inject it into the child env, so a single per-run .env serves
                # both credentials. A skipped status still flows through fail-safe.
                sub_env = os.environ.copy()
                fal_key = _fal_key(run)
                if fal_key:
                    sub_env["FAL_KEY"] = fal_key
                try:
                    proc = subprocess.run(
                        cmd, capture_output=True, text=True, timeout=180, env=sub_env
                    )
                except subprocess.TimeoutExpired:
                    self._json(200, {"ok": False, "status": "error",
                                     "error": "layer decomposition timed out — please try again"})
                    return

                manifest_path = scratch / "manifest.json"
                manifest = {}
                if manifest_path.is_file():
                    try:
                        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                    except ValueError:
                        pass

                status_val = manifest.get("status", "error")
                if status_val == "skipped":
                    self._json(200, {
                        "ok": False,
                        "status": "skipped",
                        "error": "decomposition unavailable — FAL_KEY not set",
                    })
                    return
                if status_val != "ok" or proc.returncode != 0:
                    reason = manifest.get("reason") or _clean_subprocess_error(
                        proc.stderr or "decompose failed", what="layer decomposition")
                    self._json(200, {"ok": False, "status": "error", "error": reason})
                    return

                # Build the layer list with data URIs for client use.
                layers_out = []
                for entry in manifest.get("layers", []):
                    fpath = scratch / entry.get("file", "")
                    data_uri = ""
                    if fpath.is_file():
                        data_uri = _png_data_uri(fpath)
                    layers_out.append({
                        "index": entry.get("index", 0),
                        "data_uri": data_uri,
                        "file": entry.get("file", ""),
                        "width": entry.get("width", 0),
                        "height": entry.get("height", 0),
                        "source_url": entry.get("source_url", ""),
                        "bbox": {},  # spatial bbox from model (empty when not provided)
                    })

                self._json(200, {"ok": True, "layers": layers_out})
                return

            # ── /add-image (§3 — Add Image) ────────────────────────────────
            if path == "/add-image":
                slide_id = body.get("slide_id") or ""
                data_uri = body.get("data_uri") or ""
                if not slide_id:
                    self._json(400, {"ok": False, "error": "slide_id required"})
                    return
                if not data_uri.startswith("data:image/"):
                    self._json(400, {"ok": False, "error": "data_uri (data:image/...) required"})
                    return
                # Pick the next free LAYER index for this slide (live handles the
                # client knows about + saved tweaks + persisted asset backups), so
                # the new asset never collides with a decomposed layer.
                extra = body.get("existing_handles") or []
                handle = _next_layer_handle(state.run, slide_id, extra)
                idx = int(re.fullmatch(r"LAYER_(\d+)", handle).group(1))
                # Durable backup (best-effort) — the data URI is the canonical img
                # source for the bake (parity-safe, no base URL), so a failed disk
                # write never blocks the response.
                _save_added_asset(state.run, slide_id, idx, data_uri)
                self._json(200, {"ok": True, "handle": handle, "data_uri": data_uri})
                return

            # ── /ai-edit (studio-ai-edit — "Edit with GPT/Gemini") ─────────
            # Mirrors the proven subprocess pattern (_rebake_slide /
            # render_template.call_ai_image_gen): decode the data-URI payload to a
            # temp file → `uv run generate_image_<provider>.py --input-image` →
            # parse the MEDIA: token → answer with the result as a data URI. The
            # APPLY of the result happens client-side through the exact Replace-
            # image imgSrc path — this endpoint never touches tweaks or the bake.
            if path == "/ai-edit":
                provider = body.get("provider") or ""
                meta = _AI_EDIT_PROVIDERS.get(provider)
                if meta is None:
                    self._json(400, {"ok": False,
                                     "error": f"unknown provider: {provider!r}"})
                    return
                slide_id = body.get("slide") or ""
                handle = body.get("handle") or ""
                prompt = (body.get("prompt") or "").strip()
                if not slide_id or not handle:
                    self._json(400, {"ok": False,
                                     "error": "slide and handle required"})
                    return
                if not prompt:
                    self._json(400, {"ok": False, "error": "prompt required"})
                    return
                # Payload is a LIST of data URIs: [0] is the slot image being
                # edited, extras are reference images in the order the user added
                # them (ai-edit-multi-input MUST 2). Retrocompat: a singular
                # `image` is accepted as a one-element list. ONLY data URIs are
                # accepted (decode → temp files) — no path/URL resolution
                # server-side, killing traversal by construction.
                images_payload = body.get("images")
                if images_payload is None:
                    single = body.get("image")
                    images_payload = [single] if single is not None else []
                if not isinstance(images_payload, list) or not images_payload:
                    self._json(400, {"ok": False,
                                     "error": "images must be a non-empty list of "
                                              "base64 data URIs (data:image/...;base64,)"})
                    return
                # Per-provider cap on the TOTAL (slot + extras): over the limit →
                # clean error, never a silent drop or a provider-side failure.
                cap = _AI_EDIT_IMAGE_CAP.get(provider)
                if cap is not None and len(images_payload) > cap:
                    self._json(400, {"ok": False,
                                     "error": f"{meta['label']} accepts at most {cap} "
                                              f"images (got {len(images_payload)}) — "
                                              "remove some reference images"})
                    return
                decoded_all: list[tuple[bytes, str]] = []
                for item in images_payload:
                    dec = _decode_image_data_uri(item or "")
                    if dec is None:
                        # Human-language second line of defense: the client guard
                        # (preview_editor aiIsRasterDataUri) already blocks SVG /
                        # vector inputs before submit, but if something non-raster
                        # still reaches here, speak plainly instead of dev-speak
                        # (ai-edit-live-fixes Fix 2). Accepted set = PNG/JPG/WebP/GIF.
                        self._json(400, {"ok": False,
                                         "error": "Couldn't use one of the images as an AI "
                                                  "input — it must be a PNG, JPG, WebP or GIF "
                                                  "(SVG/vector images aren't supported)."})
                        return
                    decoded_all.append(dec)
                # Snapshot state.run under the lock (P2 #12 parity with /decompose):
                # snapshot-and-release — never hold the lock through a 300s subprocess.
                with state.lock:
                    run = state.run
                # Key gating re-resolved per request (presence only; the key NAME in
                # the error tells the user what to configure — the VALUE never
                # leaves the server). No silent fallback to the other provider:
                # the user chose this button (spec MUST 6).
                if not _ai_edit_providers(run).get(provider):
                    self._json(403, {"ok": False,
                                     "error": f"{meta['label']} editing unavailable — "
                                              f"{meta['key']} not found in .env"})
                    return
                script = GEN_IMAGE_GPT if provider == "gpt" else GEN_IMAGE_GEMINI
                if not script.is_file():
                    # Fail-soft on a missing sibling skill (DECOMPOSE parity).
                    self._json(200, {"ok": False,
                                     "error": f"AI edit unavailable — {script.name} "
                                              "not found in install"})
                    return

                tmp_ins: list[Path] = []
                try:
                    for raw, ext in decoded_all:
                        with tempfile.NamedTemporaryFile(
                                "wb", suffix=ext, prefix="cs-aiedit-",
                                delete=False) as tf:
                            tf.write(raw)
                            tmp_ins.append(Path(tf.name))
                    # Aspect/transparency follow the slot image [0] (the one being
                    # edited); the extras are references and never change it.
                    dims = _image_dimensions(tmp_ins[0])
                    out_png = _next_ai_edit_output(run, slide_id, handle, provider)
                    # The gen scripts declare their deps via PEP-723 inline metadata,
                    # so they MUST run under `uv run` (sys.executable fallback when uv
                    # is absent) — exactly like _rebake_slide / decompose. --api-key is
                    # NEVER passed: the script resolves the key itself, and its .env
                    # walk-up starts at the subprocess cwd, which we pin to the run
                    # folder so the project .env wins (same file the gating read).
                    _uv = shutil.which("uv")
                    if _uv:
                        cmd = [_uv, "run", "--no-project", str(script)]
                    else:
                        cmd = [sys.executable, str(script)]
                    cmd += ["--prompt", prompt,
                            "--filename", str(out_png)]
                    # [0] first, extras after — preserves the user's order so the
                    # scripts (and their alpha auto-detect on [0]) see it right.
                    for p in tmp_ins:
                        cmd += ["--input-image", str(p)]
                    if provider == "gpt":
                        cmd += ["--size", _nearest_gpt_size(dims), "--quality", "high"]
                    else:
                        cmd += ["--aspect-ratio", _nearest_gemini_aspect(dims)]
                    try:
                        proc = subprocess.run(
                            cmd, capture_output=True, text=True, timeout=300,
                            cwd=str(run),
                        )
                    except subprocess.TimeoutExpired:
                        self._json(200, {"ok": False,
                                         "error": "AI edit timed out — please try again"})
                        return
                    except Exception as exc:  # noqa: BLE001
                        self._json(200, {"ok": False,
                                         "error": _clean_subprocess_error(
                                             str(exc), what="AI edit")})
                        return
                finally:
                    for p in tmp_ins:
                        try:
                            p.unlink()
                        except OSError:
                            pass

                if proc.returncode != 0:
                    # Clean, user-facing error (never a raw traceback), scrubbed of
                    # any key VALUE a provider might have echoed back.
                    tail = (proc.stderr or proc.stdout or "image generation failed").strip()
                    self._json(200, {"ok": False,
                                     "error": _scrub_key_values(
                                         _clean_subprocess_error(tail, what="AI edit"),
                                         run)})
                    return
                # Success contract of both scripts: `MEDIA:<abs path>` on stdout.
                media: Path | None = None
                for line in (proc.stdout or "").splitlines():
                    if line.startswith("MEDIA:"):
                        cand = Path(line[len("MEDIA:"):].strip())
                        if cand.is_file():
                            media = cand
                if media is None and out_png.is_file():
                    media = out_png  # belt-and-braces: the file we asked for exists
                if media is None:
                    self._json(200, {"ok": False,
                                     "error": "no image produced — please try again"})
                    return
                # ai-edit-fit-result: the provider emits a fixed size (nearest, not
                # exact) that rarely matches the slot — center-crop the result to the
                # input [0] aspect (cover, no distortion) so it enters the canvas with
                # the right footprint. No-op when aspects already match; preserves
                # alpha; best-effort (never loses a successful generation).
                _center_crop_to_aspect(media, dims)
                self._json(200, {"ok": True, "png": _png_data_uri(media)})
                return

            if path == "/post":
                # ── Zernio publish (AIOS-139 Addendum 4) ─────────────────
                # Thin wrapper around tool-publisher/scripts/publish_rest.py.
                # Key fail-safe: missing key → HTTP 200 ok:false (NEVER 500).
                if not _zernio_key_present(state.run):
                    self._json(200, {
                        "ok": False,
                        "reason": (
                            "ZERNIO_API_KEY credential was not found in .env"
                            " — Publish is unavailable."
                        ),
                    })
                    return

                platform = body.get("platform") or ""
                account_id = body.get("accountId") or ""
                mode = body.get("mode") or "publishNow"
                schedule_for = body.get("scheduleFor") or ""
                use_pdf = bool(body.get("pdf"))
                doc_title = body.get("documentTitle") or ""
                # AIOS-131: body-provided value wins; fall back to post.yaml so CLI
                # and front share the same source (parity guarantee).
                first_comment = (
                    body.get("firstComment")
                    or _read_post_yaml_key(state.run, "first_comment")
                    or ""
                )

                # AIOS-139 Addendum 9 #2 — publish the EDITED slides, not the stale
                # originals. The client bakes before /post, but make it a server-side
                # guarantee too: if the request carries pending tweaks (or a tweaks.json
                # is on disk), rebake the affected slides NOW so _publishable_media picks
                # up the composited output. Ties to the run-folder contract (#1): with
                # _slides/ present, templated slides actually rebake here.
                pending_tweaks = body.get("tweaks")
                if not isinstance(pending_tweaks, dict):
                    tj = state.run / "tweaks.json"
                    if tj.is_file():
                        try:
                            pending_tweaks = json.loads(tj.read_text(encoding="utf-8"))
                        except ValueError:
                            pending_tweaks = None
                if isinstance(pending_tweaks, dict) and pending_tweaks:
                    for sid in _affected_slides(pending_tweaks):
                        _rebake_slide(state, sid, pending_tweaks)

                # Persist EVERY attempted outcome to the run folder (logs/yaml) so the
                # result "goes to logs", then send. Best-effort persistence — never
                # crashes the response.
                def _respond(result: dict):
                    _persist_publish_result(state.run, platform, mode, result)
                    self._json(200, result)

                # publish_rest.py requires a post.yaml; a Content Studio run may only
                # have caption.md + slide PNGs, so synthesize a minimal one if absent.
                _ensure_post_yaml(state.run, platform)

                argv = [sys.executable, str(PUBLISH_REST), str(state.run)]
                # Pin publish_rest.py to the SAME project-bounded .env we gated on,
                # so its own unbounded find_env() can't pick up a stray .env from the
                # dev/test cwd or the user's home dir (AIOS-139 Addendum 9 #1).
                env_file = _env_file(state.run)
                if env_file is not None:
                    argv += ["--env-file", str(env_file)]
                if platform:
                    argv += ["--platform", platform]
                if account_id:
                    argv += ["--account-id", account_id]
                if use_pdf and platform == "linkedin":
                    argv.append("--pdf")
                    if doc_title:
                        argv += ["--document-title", doc_title]
                else:
                    # Resolve the baked slide PNGs explicitly and pass them via --media
                    # so Publish is independent of how each image was produced (full-AI /
                    # template / hybrid) and of the single-vs-carousel format inference.
                    # Without this, a single full-AI image (slide-01.png, format "single")
                    # falls through publish_rest's autodetect (which seeks image.png) and
                    # the post is silently blocked. Empty list → fall back to autodetect.
                    media = _publishable_media(state.run)
                    if media:
                        argv += ["--media", *[str(p) for p in media]]
                if mode == "draft":
                    # publish_rest.py now supports --draft (omits both publishNow and
                    # scheduledFor; Zernio defaults the post to draft).
                    argv.append("--draft")
                elif mode == "schedule" and schedule_for:
                    argv += ["--schedule-for", schedule_for]
                # mode == "publishNow": no extra flag — publish_rest.py defaults
                # to publishNow=True when --schedule-for / --draft are absent.
                # media: rely on publish_rest.py autodetect of slide-*.png in run/.
                if first_comment:
                    argv += ["--first-comment", first_comment]

                try:
                    proc = subprocess.run(
                        argv, capture_output=True, text=True, timeout=300
                    )
                except subprocess.TimeoutExpired:
                    _respond({"ok": False, "error": "Zernio publish timed out — please try again"})
                    return
                except Exception as exc:  # noqa: BLE001
                    _respond({"ok": False, "error": _clean_subprocess_error(str(exc), what="Zernio publish")})
                    return

                if proc.returncode != 0:
                    tail = (proc.stderr or proc.stdout or "publish_rest.py failed")
                    _respond({"ok": False, "error": _clean_subprocess_error(tail, what="Zernio publish")})
                    return

                try:
                    result = json.loads(proc.stdout)
                except (ValueError, TypeError):
                    tail = (proc.stdout or proc.stderr or "no output").strip()
                    _respond({"ok": False, "error": f"unparseable output: {tail[-300:]}"})
                    return

                _respond(result)
                return

            # ── /compare-images (Template Studio — per-template ref+render data-URIs) ──
            if path == "/compare-images":
                if state.mode != "template":
                    self._json(400, {"ok": False, "error": "compare-images only available in template mode"})
                    return
                template_id = body.get("template_id") or ""
                if not template_id:
                    self._json(400, {"ok": False, "error": "template_id required"})
                    return
                # Look up the record by id from the pre-resolved pool list.
                tpl_rec = next(
                    (t for t in state.pool_templates if t["id"] == template_id), None
                )
                if tpl_rec is None:
                    self._json(200, {"ok": False,
                                     "error": f"unknown template_id: {template_id!r}"})
                    return
                # Read CURRENT bytes each call — no caching — so a recent edit is reflected.
                ref_path = Path(tpl_rec["ref"])
                render_path = Path(tpl_rec["render"])
                tpl_dir = Path(tpl_rec["template_dir"])
                # FRESH PREVIEW on conference load — the render column must reflect the
                # CURRENT edited state, not the last-saved preview.png. Edits live in
                # tweaks.json but were never re-baked into the displayed image, so the
                # reviewer saw the pre-edit version. Re-bake preview.png from tweaks.json
                # through the SAME path /approve uses (preview == bake), then copy the
                # result to the pool _preview/<id>.png the gallery reads, so the
                # conference and gallery agree. No-op when tweaks.json is absent.
                rebake = _rebake_template_preview(
                    state.run, tpl_dir, state.brand_context)
                if rebake.get("baked"):
                    _copy_preview_to_pool(
                        _find_pool_dir(state.run), template_id, tpl_dir / "preview.png")
                # Prefer the freshest bake: a live Apply writes slide-01.png in the
                # template dir, while preview.png only updates on Approve / the rebake
                # above. Without this the Compare shows the pre-edit (last-approved)
                # image even after the user has Applied an edit. slide-01.png exists for
                # the actively edited template; others fall through to preview.png.
                _live = tpl_dir / "slide-01.png"
                if _live.is_file() and (not render_path.is_file()
                        or _live.stat().st_mtime >= render_path.stat().st_mtime):
                    render_path = _live
                ref_uri: str | None = None
                render_uri: str | None = None
                render_version: str | None = None
                error_msg: str | None = None
                if ref_path.is_file():
                    ref_uri = _png_data_uri(ref_path)
                else:
                    error_msg = f"ref-canonical.png missing for {template_id!r}"
                if render_path.is_file():
                    render_uri = _png_data_uri(render_path)
                    # Cache-buster: a short hash of the baked bytes the client appends
                    # to the render image URL (?v=<token>) so the browser never serves a
                    # cached stale image. Changes whenever the preview changes.
                    render_version = _preview_version(render_path)
                if rebake.get("ok") is False and rebake.get("error"):
                    error_msg = rebake["error"] if error_msg is None else \
                        f"{error_msg} · {rebake['error']}"
                # Surface the builder's Template Card rationale (instructions.md) as
                # review notes next to the compare panes (AIOS-190 W1). Read-only.
                notes = _read_template_card(tpl_dir)
                # Respond immediately — never hang regardless of missing files.
                self._json(200, {
                    "ok": True,
                    "ref": ref_uri,
                    "render": render_uri,
                    **({"render_version": render_version} if render_version else {}),
                    **({"notes": notes} if notes else {}),
                    **({"error": error_msg} if error_msg else {}),
                })
                return

            # ── /compare (Template Studio — legacy single-template compare) ────
            # INTENTIONAL backward-compat shim — retained deliberately (reviewer
            # decision, AIOS-139): the modal-with-tabs UI is fully removed (the
            # live conference uses openConference + /compare-images), but the
            # /compare route and _COMPARE_MODES are kept so the 4 legacy tests
            # that exercise this contract stay green.  Do NOT delete.
            if path == "/compare":
                if state.mode != "template":
                    self._json(400, {"ok": False, "error": "compare only available in template mode"})
                    return
                mode = body.get("mode", "")
                _valid_modes = {"side-by-side", "overlay", "diff", "grid"}
                if mode not in _valid_modes:
                    self._json(400, {"ok": False,
                                     "error": f"invalid mode {mode!r}; expected one of {sorted(_valid_modes)}"})
                    return
                ref = state.run / "assets" / "ref-canonical.png"
                if not ref.is_file():
                    self._json(200, {"ok": False, "error": "assets/ref-canonical.png not found"})
                    return
                ref_uri = _png_data_uri(ref)
                render = state.run / "preview.png"
                render_uri = _png_data_uri(render) if render.is_file() else None
                self._json(200, {"ok": True, "ref": ref_uri, "render": render_uri})
                return

            # ── /approve (Template Studio — save approved template) ──────────
            if path == "/approve":
                if state.mode != "template":
                    self._json(400, {"ok": False, "error": "approve only available in template mode"})
                    return
                # Snapshot the shared state once under the lock so a /select-template
                # swap can't move state.run / pool_templates mid-approve and write the
                # active template's bake into another template's dir (P2 #12). The body
                # below is disk-only (no long subprocess), so snapshot-and-release.
                with state.lock:
                    run = state.run
                    pool_templates = getattr(state, "pool_templates", None)
                # Resolve per-template directory: when template_id is provided and
                # the pool has multiple templates, write tweaks into THAT template's
                # own dir (not always state.run) so each template's canonical tweaks
                # are isolated (cross-template attribution safety).
                template_id = body.get("template_id") or run.name
                tpl_record = None
                if pool_templates is not None:
                    tpl_record = next(
                        (t for t in pool_templates if t["id"] == template_id), None
                    )
                tpl_dir = Path(tpl_record["template_dir"]) if tpl_record else run
                preview_png = tpl_dir / "preview.png"
                # Versioned output: v1 = the template-generated baseline (snapshotted
                # once, before the re-bake overwrites preview.png); v2 = the
                # user-edited result, saved ONLY when it differs from v1.
                v1_png = tpl_dir / "preview.v1.png"
                v2_png = tpl_dir / "preview.v2.png"
                saved_version = "v1"
                # Capture the original preview as v1 baseline before re-baking.
                if not v1_png.is_file() and preview_png.is_file():
                    try:
                        shutil.copy2(preview_png, v1_png)
                    except OSError:
                        pass
                # Persist canonical tweaks FIRST so the blocking re-bake below
                # renders from the exact saved state (seam fix — guarantees
                # tweaks.json ↔ preview.png consistency).
                # Storage format: the tweaks are written as-is from the client.
                # _load_canonical_tweaks handles both slide-keyed dicts and
                # __canonical__-sentinel files.  Zone-level tweaks (bare dict of
                # handles) are wrapped so render_template can re-key them.
                tweaks = body.get("tweaks") or {}
                try:
                    if isinstance(tweaks, dict) and tweaks:
                        # Detect whether tweaks are already slide-keyed: any key
                        # whose value is a dict with slide-level content.
                        _slide_like = [
                            k for k in tweaks
                            if isinstance(tweaks.get(k), dict)
                        ]
                        if _slide_like:
                            to_write: dict = tweaks
                        else:
                            # Zone-level — wrap so render_template re-keys.
                            to_write = {"__canonical__": tweaks}
                    else:
                        to_write = {}
                    (tpl_dir / "tweaks.json").write_text(
                        json.dumps(to_write, indent=2), encoding="utf-8")
                except OSError:
                    pass
                # Blocking re-bake: render preview.png from the just-written
                # tweaks.json via the SHARED _rebake_template_preview helper — the
                # SAME path /compare-images uses on conference load, so the displayed
                # render and the approved/baked PNG are produced identically
                # (preview == bake). Replaces the old shutil.copy2 from slide-01.png
                # which was the source of stale previews.
                #
                # r5f-followups Fix 1 (now inside the helper) — the output is
                # preview.png, so its stem is "preview", which NEVER matches a
                # slide-keyed tweaks file ({"slide-01": {...}}): render derives
                # _slide_id = output.stem and looks up tweaks["preview"] → {} → the
                # imgSrc/text swap never runs → white <img src="">. The helper mirrors
                # the proven _rebake_slide contract: passes the tweaks file EXPLICITLY
                # plus --tweaks-slide slide-01 (so _slide_id resolves to the canonical
                # single-slide id and re-keys a __canonical__-wrapped file) and --data
                # from the slide's persisted metadata so PHOTO_MAIN_PATH resolves even
                # with no imgSrc tweak.
                _rebake = _rebake_template_preview(run, tpl_dir, state.brand_context)
                if _rebake.get("ok") is False:
                    self._json(200, {"ok": False,
                                     "error": _rebake.get("error", "preview re-bake failed")})
                    return
                if not preview_png.is_file():
                    self._json(200, {"ok": False, "error": "preview re-bake produced no output"})
                    return
                # Compare re-baked result against v1 to detect user edits.
                try:
                    if (v1_png.is_file()
                            and preview_png.read_bytes() != v1_png.read_bytes()):
                        shutil.copy2(preview_png, v2_png)
                        saved_version = "v2"
                except OSError:
                    pass
                # Try to update the pool manifest.json and copy to _preview/.
                # Discover the pool dir the SAME way _walk_pool_templates does:
                # the nearest of run / its ancestors (≤4 levels) holding a
                # manifest.json. Hardcoding `state.run.parent` silently no-op'd
                # the approve when the studio was launched against the pool dir
                # itself (manifest one level too high) — the pool-dir footgun.
                manifest_updated = False
                pool_dir = run.parent
                for _d in [run, *list(run.parents)[:4]]:
                    if (_d / "manifest.json").is_file():
                        pool_dir = _d
                        break
                manifest_path = pool_dir / "manifest.json"
                try:
                    if manifest_path.is_file():
                        raw_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                        # Normalize exactly like resolve_pool_template: accept templates[]
                        # (Phase 4.5) or variations[] (Phase 5 factory); accept dict or list.
                        _was_bare_list = isinstance(raw_manifest, list)
                        if _was_bare_list:
                            manifest = {"templates": raw_manifest}
                        else:
                            manifest = raw_manifest
                        entries = manifest.get("templates") or manifest.get("variations") or []
                        was_dict = isinstance(entries, dict)
                        if was_dict:
                            norm = [{**v, "id": v.get("id", k)}
                                    for k, v in entries.items() if isinstance(v, dict)]
                        else:
                            norm = entries
                        matched = None
                        for e in norm:
                            if not isinstance(e, dict):
                                continue
                            # Match by id, slug, or name — support all legacy formats.
                            _eid = e.get("id") or e.get("slug") or e.get("name") or ""
                            if _eid == template_id:
                                # Record approval as a SEPARATE marker — do NOT
                                # overwrite status. The template stays status="ready"
                                # so it keeps counting toward the brand-context
                                # visual_state ready_count gate (SKILL.md:121,
                                # pipeline-phases.md:162). Flipping status to
                                # "approved" drops it from that count, so approving a
                                # whole pool would zero ready_count and block content
                                # generation downstream.
                                e["approved"] = True
                                e["approved_at"] = time.strftime(
                                    "%Y-%m-%dT%H:%M:%SZ", time.gmtime())
                                e["preview_path"] = str(preview_png)
                                # A needs-user-decision entry is a builder gate
                                # FALSE-POSITIVE the user just confirmed IN the Studio.
                                # Promote it to "ready" so it counts toward the
                                # brand-context ready_count gate (it was excluded
                                # while flagged). Other statuses are left untouched.
                                if e.get("status") == "needs-user-decision":
                                    e["status"] = "ready"
                                matched = e
                                break
                        # Write back into whichever key held the list
                        if matched is not None:
                            if was_dict:
                                # Rebuild the dict form preserving keys
                                src = (manifest.get("templates")
                                       if "templates" in manifest
                                       else manifest.get("variations"))
                                for k, v in list(src.items()):
                                    if isinstance(v, dict) and v.get("id", k) == template_id:
                                        # Separate marker, status untouched (see above).
                                        v["approved"] = True
                                        v["approved_at"] = time.strftime(
                                            "%Y-%m-%dT%H:%M:%SZ", time.gmtime())
                                        v["preview_path"] = str(preview_png)
                                        # See list-form branch: confirm the gate
                                        # false-positive by promoting to "ready".
                                        if v.get("status") == "needs-user-decision":
                                            v["status"] = "ready"
                            # Preserve original structure: bare list manifests are
                            # written back as a list (not wrapped in {"templates": [...]})
                            to_save = raw_manifest if _was_bare_list else manifest
                            manifest_path.write_text(json.dumps(to_save, indent=2),
                                                     encoding="utf-8")
                            manifest_updated = True
                except (OSError, ValueError):
                    pass
                # Copy preview to pool/_preview/{template_id}.png — the gallery's path
                # (shared helper, same as /compare-images, so conference == gallery).
                _copy_preview_to_pool(pool_dir, template_id, preview_png)
                self._json(200, {"ok": True, "preview_path": str(preview_png),
                                 "manifest_updated": manifest_updated,
                                 "saved_version": saved_version})
                return

            self._send(404, b"not found", "text/plain")

    return Handler


def _wait_ready(port: int, timeout: float = 5.0) -> bool:
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.3):
                return True
        except OSError:
            time.sleep(0.05)
    return False


def serve(run: Path, brand_context: Path | None, port: int, open_browser: bool,
          mode: str = "post") -> int:
    state = StudioState(run, brand_context, mode)
    httpd = ThreadingHTTPServer(("127.0.0.1", port), make_handler(state))
    actual_port = httpd.server_address[1]
    url = f"http://127.0.0.1:{actual_port}/"

    # _stop is set either by Ctrl+C or by the /shutdown endpoint (Close Studio button).
    _stop = threading.Event()
    state._shutdown_fn = lambda: (_stop.set(), httpd.shutdown())

    t = threading.Thread(target=httpd.serve_forever, daemon=True)
    t.start()

    app_name = "Template Studio" if mode == "template" else "Content Studio"
    if _wait_ready(actual_port):
        print(f"{app_name} running at {url}")
        print(f"  run folder : {run}")
        if mode == "template":
            print("  Mode: template authoring — Approve saves preview.png + updates manifest")
            print("  Compare = ref<->render diff | Line check = pixel line-count QA")
        else:
            print("  Apply = live rebake (render_template --tweaks) | Save = persist state")
        print("  Press Ctrl+C to stop.")
        if open_browser:
            try:
                webbrowser.open(url)
            except Exception:
                print(f"  (could not auto-open a browser — open {url} manually)")
    else:
        print(f"ERROR: server did not become ready on port {actual_port}", file=sys.stderr)
        return 1

    try:
        _stop.wait()
    except KeyboardInterrupt:
        pass
    print("\nStopping Content Studio.")
    httpd.shutdown()
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Content Studio — local-server wrapper around the carousel editor.")
    ap.add_argument("run_folder")
    ap.add_argument("--brand-context", default=None)
    ap.add_argument("--port", type=int, default=0,
                    help="Port to bind (default: auto-pick a free port).")
    ap.add_argument("--no-open", action="store_true",
                    help="Do not auto-open the browser (print the URL only).")
    ap.add_argument("--mode", choices=["post", "template"], default="post",
                    help="Studio mode: 'post' (default) for carousel editing, "
                         "'template' for authoring a new template.")
    args = ap.parse_args()

    run = Path(args.run_folder).resolve()
    if not run.is_dir():
        print(f"ERROR: run folder not found: {run}", file=sys.stderr)
        return 1

    bc = _resolve_brand_context(run, args.brand_context)
    port = _free_port(args.port) if args.port else _free_port(0)
    return serve(run, bc, port, open_browser=not args.no_open, mode=args.mode)


if __name__ == "__main__":
    raise SystemExit(main())
