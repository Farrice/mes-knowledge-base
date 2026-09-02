#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""preview_editor.py — live-HTML carousel editor for the 00-social-content pipeline.

Generates a self-contained ``editor.html`` where each slide is rendered as the
real ``template.html`` inside an ``<iframe srcdoc>`` (fonts + CSS inlined for
parity with the baked PNG), with a generated control panel that introspects each
slide's ``## Slots`` definition and produces per-type controls (text / pill /
image / chrome).  Controls update the iframe DOM live via vanilla JS.  An
``Export tweaks.json`` button downloads the per-slide + global overrides JSON
consumed by ``render_template.py --tweaks``.

Usage:
    python preview_editor.py <run_folder> [--brand-context DIR]

Reads from <run_folder> (same layout the carousel pipeline creates):
    slide-*.png              — for FULL_AI slides that have no template.html
    _slides/slide-N/         — per-slide metadata dirs (template_dir, slide_id ...)
    brand_context/...        — resolved automatically (or via --brand-context)

Writes:
    <run_folder>/preview/editor.html   — self-contained editable preview

Prints the absolute path to stdout on success.

Import contract (testable without opening a browser):
    build_editor_html(run, brand_context, shared_css_override) -> str
"""

from __future__ import annotations

import argparse
import base64
import html
import json
import re
import sys
from pathlib import Path

# ──────────────────────────────────────────────────────────────
# Cross-skill import: pull fill(), build_brand_tokens_css(),
# _inline_relative_urls(), parse_slots_from_instructions() from
# viz-image-gen/scripts/render_template.py.
# The two skills live under the same pack root so we can resolve
# the sibling path at import time.
# ──────────────────────────────────────────────────────────────
_SCRIPT_DIR = Path(__file__).resolve().parent
# Walk up from 00-social-content/scripts/content-studio/ to the skills root, then
# descend into viz-image-gen/scripts/. (_SCRIPT_DIR=.../skills/00-social-content/
# scripts/content-studio, so .parent.parent.parent=.../skills — one extra hop vs the
# old mkt-visual-identity/scripts location because content-studio/ is one level deeper.)
RENDER_SCRIPTS = _SCRIPT_DIR.parent.parent.parent / "viz-image-gen" / "scripts"
sys.path.insert(0, str(RENDER_SCRIPTS))

try:
    from render_template import (  # type: ignore[import]
        fill,
        build_brand_tokens_css,
        _inline_relative_urls,
        parse_slots_from_instructions,
        embed_paths_as_data_uris,
        build_google_fonts_link,
        css_font_value,
        CURATED_FONTS,
    )
    _IMPORT_OK = True
except ImportError:
    _IMPORT_OK = False

if not _IMPORT_OK:
    # Fallback: inline minimal Mustache fill (covers the parity core without
    # Playwright / argparse plumbing).  Note: if this branch is hit, the
    # brand-tokens CSS and slot-type inference will also be unavailable.
    import html as _html_mod

    def _html_escape(s: str) -> str:
        s = _html_mod.unescape(s)
        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

    def render_sections(raw: str, data: dict) -> str:
        section_re = re.compile(r"\{\{([#^])([A-Za-z_][A-Za-z0-9_]*)\}\}([\s\S]*?)\{\{/\2\}\}")
        while True:
            m = section_re.search(raw)
            if not m:
                break
            kind, key, content = m.group(1), m.group(2), m.group(3)
            val = data.get(key)
            if kind == "#":
                replacement = content if val else ""
            else:
                replacement = "" if val else content
            raw = raw[: m.start()] + replacement + raw[m.end() :]
        return raw

    def substitute(raw: str, data: dict) -> str:
        raw = re.sub(r"\{\{\{\s*([A-Za-z_][A-Za-z0-9_]*)\s*\}\}\}", lambda m: str(data.get(m.group(1).strip(), "")), raw)
        raw = re.sub(r"\{\{\s*([A-Za-z_][A-Za-z0-9_]*)\s*\}\}", lambda m: _html_escape(str(data.get(m.group(1).strip(), ""))), raw)
        return raw

    def fill(raw: str, data: dict) -> str:  # type: ignore[misc]
        return substitute(render_sections(raw, data), data)

    def build_brand_tokens_css(brand_kit: dict, target_canvas: dict | None = None) -> str:  # type: ignore[misc]
        return ""

    CURATED_FONTS = [  # type: ignore[misc]
        ("Inter", "sans-serif"), ("Geist", "sans-serif"), ("Manrope", "sans-serif"),
        ("DM Sans", "sans-serif"), ("Space Grotesk", "sans-serif"), ("Sora", "sans-serif"),
        ("Hanken Grotesk", "sans-serif"), ("Fraunces", "serif"),
        ("Playfair Display", "serif"), ("Archivo", "sans-serif"), ("JetBrains Mono", "monospace"),
    ]
    _FONT_GENERIC = {n: g for n, g in CURATED_FONTS}

    def css_font_value(family: str) -> str:  # type: ignore[misc]
        fam = (family or "").strip().strip('"').strip("'")
        return f'"{fam}", {_FONT_GENERIC.get(fam, "sans-serif")}' if fam else ""

    def build_google_fonts_link(extra_families=None) -> str:  # type: ignore[misc]
        names = [n for n, _ in CURATED_FONTS]
        for fam in (extra_families or []):
            if fam and fam not in names:
                names.append(fam)
        specs = []
        for n in names:
            wght = "wght@400;500" if n == "JetBrains Mono" else "wght@400;500;600;700"
            specs.append(f"family={n.replace(' ', '+')}:{wght}")
        href = "https://fonts.googleapis.com/css2?" + "&".join(specs) + "&display=swap"
        return ('<link rel="preconnect" href="https://fonts.googleapis.com">'
                '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
                f'<link rel="stylesheet" href="{href}">')

    _RELATIVE_URL_RE = re.compile(r"""url\(\s*['"]?(?P<path>[^'")\s]+)['"]?\s*\)""")
    _MEDIA_TYPE_BY_EXT = {
        ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
        ".webp": "image/webp", ".gif": "image/gif", ".svg": "image/svg+xml",
        ".woff2": "font/woff2", ".ttf": "font/ttf",
    }

    _IMG_SRC_RE = re.compile(
        r"""(?P<lead><img\b[^>]*?\bsrc\s*=\s*)(?P<quote>['"])(?P<path>[^'"\s>]+)(?P=quote)""",
        re.IGNORECASE,
    )

    def _inline_relative_urls(html_text: str, base_dir: Path) -> str:  # type: ignore[misc]
        def _resolve(path_str: str) -> str | None:
            if path_str.startswith(("http://", "https://", "data:", "//", "#")):
                return None
            candidate = (base_dir / path_str).resolve()
            if not candidate.is_file():
                return None
            ext = candidate.suffix.lower()
            media = _MEDIA_TYPE_BY_EXT.get(ext)
            if not media:
                return None
            b64 = base64.b64encode(candidate.read_bytes()).decode("ascii")
            return f"data:{media};base64,{b64}"
        def replace_css(m: re.Match) -> str:
            uri = _resolve(m.group("path"))
            return f"url('{uri}')" if uri else m.group(0)
        def replace_img(m: re.Match) -> str:
            uri = _resolve(m.group("path"))
            if not uri:
                return m.group(0)
            return f"{m.group('lead')}{m.group('quote')}{uri}{m.group('quote')}"
        html_text = _RELATIVE_URL_RE.sub(replace_css, html_text)
        return _IMG_SRC_RE.sub(replace_img, html_text)

    def embed_paths_as_data_uris(data: dict, brand_context, template_dir=None) -> dict:  # type: ignore[misc]
        """Fallback mirror of render_template.embed_paths_as_data_uris: base64-inline
        every ``*_PATH`` data value that resolves to a local image file."""
        out = dict(data)
        for key in list(out.keys()):
            if not key.endswith("_PATH"):
                continue
            val = out[key]
            if not isinstance(val, str) or not val or val.startswith(("data:", "http://", "https://")):
                continue
            path = Path(val)
            if not path.is_absolute():
                for base in (template_dir, brand_context):
                    if base is None:
                        continue
                    cand = (Path(base) / val).resolve()
                    if cand.is_file():
                        path = cand
                        break
            if not path.is_file():
                continue
            media = _MEDIA_TYPE_BY_EXT.get(path.suffix.lower(), "image/png")
            out[key] = f"data:{media};base64,{base64.b64encode(path.read_bytes()).decode('ascii')}"
        return out

    _slot_re   = re.compile(r"^[-*]\s+\*?\*?([A-Z][A-Z0-9_]+)\*?\*?\s*[—\-]")
    _bbox_re   = re.compile(r"bbox\s*:\s*([\d.]+)%\s+([\d.]+)%\s+([\d.]+)%\s+([\d.]+)%", re.IGNORECASE)
    _style_re  = re.compile(r"^\s*[-*]?\s*style\s*:\s*(.+)$", re.IGNORECASE)
    _sample_re = re.compile(r"^[-*]?\s*sample\s*:\s*(.*)$", re.IGNORECASE)
    _maxch_re  = re.compile(r"max_chars\s*:\s*(\d+)", re.IGNORECASE)

    def _infer_type(style: str | None) -> str:
        if not style:
            return "text"
        sl = style.lower()
        if any(kw in sl for kw in ("photo", "ai-image", "image")):
            return "image"
        if "pill" in sl:
            return "pill"
        if any(kw in sl for kw in ("masthead", "dots", "chrome")):
            return "chrome"
        return "text"

    def parse_slots_from_instructions(path: Path) -> list[dict]:  # type: ignore[misc]
        text = path.read_text(encoding="utf-8", errors="ignore")
        results: list[dict] = []
        current: dict | None = None
        in_slots = False
        for line in text.splitlines():
            s = line.strip()
            if re.match(r"^#{1,3}\s+Slots\s*$", s, re.IGNORECASE):
                in_slots = True; continue
            if in_slots and re.match(r"^#{1,3}\s+\S", s):
                in_slots = False
                if current:
                    current["type"] = _infer_type(current.get("style")); results.append(current); current = None
                continue
            if not in_slots:
                continue
            m = _slot_re.match(s)
            if m:
                if current:
                    current["type"] = _infer_type(current.get("style")); results.append(current)
                current = {"name": m.group(1), "bbox": None, "style": None, "sample": None, "max_chars": None, "type": "text"}
                continue
            if current is None:
                continue
            mb = _bbox_re.search(s)
            if mb:
                current["bbox"] = {"x": float(mb.group(1)), "y": float(mb.group(2)), "w": float(mb.group(3)), "h": float(mb.group(4))}; continue
            ms = _style_re.match(s)
            if ms:
                current["style"] = ms.group(1).strip(); continue
            msa = _sample_re.match(s)
            if msa:
                raw = msa.group(1).strip()
                if (raw.startswith('"') and raw.endswith('"')) or (raw.startswith("'") and raw.endswith("'")):
                    raw = raw[1:-1]
                current["sample"] = raw or None; continue
            mmc = _maxch_re.search(s)
            if mmc:
                current["max_chars"] = int(mmc.group(1))
        if current:
            current["type"] = _infer_type(current.get("style")); results.append(current)
        return results


# ──────────────────────────────────────────────────────────────
# Helper utilities (mirror preview_carousel.py patterns)
# ──────────────────────────────────────────────────────────────

def _b64_img(path: Path) -> str:
    suffix = path.suffix.lower().lstrip(".")
    mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "webp": "webp", "svg": "svg+xml"}.get(suffix, "png")
    return f"data:image/{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


# Curated post-production texture set (AIOS-139 Addendum 5). The PNGs are vendored
# beside this script; each is embedded as a data URI so the chosen texture's bytes go
# straight into the tweak and the bake re-applies the SAME image (RNDR-04 parity, no
# asset-path dependency). Order = picker order. _generate.py documents provenance.
_TEXTURE_DIR = Path(__file__).resolve().parent / "vendor" / "textures"
_TEXTURE_SET = [
    ("paper", "Paper"), ("film-grain", "Film grain"), ("halftone", "Halftone"),
    ("grunge", "Grunge"), ("canvas", "Canvas"), ("riso", "Riso"),
]


def _load_textures() -> list[dict]:
    """Return ``[{name, label, uri}]`` for each vendored texture PNG that exists."""
    out: list[dict] = []
    for name, label in _TEXTURE_SET:
        p = _TEXTURE_DIR / f"{name}.png"
        if p.is_file():
            out.append({"name": name, "label": label, "uri": _b64_img(p)})
    return out


def _resolve_brand_context(run: Path, override: str | None) -> Path | None:
    # Walk OUTWARD from the run and return the CLOSEST brand_context. Starts at the
    # run itself (depth 0) and its immediate parents — the earlier range(3, 7) skipped
    # depths 0-2, so a brand_context sitting next to the run (e.g. <demo>/brand_context
    # with the run at <demo>/run) was never found and the editor rendered with no brand
    # palette/fonts. Closest-wins is also more correct for nested project layouts.
    if override:
        bc = Path(override)
        return bc if bc.is_dir() else None
    for up in range(0, 7):
        cand = run
        for _ in range(up):
            cand = cand.parent
        bc = cand / "brand_context"
        if bc.is_dir():
            return bc
    return None


def _load_brand_kit(bc: Path | None) -> dict:
    if bc is None:
        return {}
    tok = bc / "visual-identity" / "tokens.json"
    if not tok.is_file():
        tok = bc / "tokens.json"
    if tok.is_file():
        try:
            return json.loads(tok.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    return {}


_HEX_RE = re.compile(r"^#?[0-9a-fA-F]{3}([0-9a-fA-F]{3})?$")


def _brand_palette(brand_kit: dict) -> list[tuple[str, str]]:
    """Ordered, de-duplicated ``(label, hex)`` palette pulled from the brand's
    ``colors`` (AIOS-139 Stage A). Replaces the old hardcoded ``#e25a45`` accent.
    Reads the v3 schema keys with legacy fallbacks; any ``accents[]`` extras append
    after the named roles."""
    colors = (brand_kit.get("colors") if isinstance(brand_kit, dict) else None) or {}
    ordered = [
        ("Accent", colors.get("accent")),
        ("Accent 2", colors.get("accent_secondary")),
        ("Primary", colors.get("primary")),
        ("Secondary", colors.get("secondary")),
        ("Background", colors.get("background") or colors.get("bg_light")),
        ("BG dark", colors.get("bg_dark")),
        ("Text", colors.get("text") or colors.get("text_on_light")),
        ("Text on dark", colors.get("text_on_dark")),
    ]
    extras = colors.get("accents") or []
    for i, hx in enumerate(extras):
        ordered.append((f"Accent {i + 3}", hx))
    out: list[tuple[str, str]] = []
    seen: set[str] = set()
    for label, hx in ordered:
        if not isinstance(hx, str) or not _HEX_RE.match(hx.strip()):
            continue
        norm = hx.strip()
        if not norm.startswith("#"):
            norm = "#" + norm
        key = norm.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append((label, norm))
    return out


def _brand_fonts(brand_kit: dict) -> list[str]:
    """Brand font families (display/body/micro, v3 + legacy), de-duplicated, in
    priority order — pinned at the TOP of every per-layer font selector so the
    brand's own type is one click away."""
    fonts = (brand_kit.get("fonts") if isinstance(brand_kit, dict) else None) or {}
    out: list[str] = []
    seen: set[str] = set()

    def _add(fam):
        if isinstance(fam, str) and fam.strip() and fam.strip().lower() not in seen:
            seen.add(fam.strip().lower())
            out.append(fam.strip())

    for role in ("display", "body", "micro", "headline"):
        cfg = fonts.get(role)
        if isinstance(cfg, dict):
            _add(cfg.get("family"))
    _add(fonts.get("headline_family"))
    _add(fonts.get("body_family"))
    return out


def _find_slides_info(run: Path) -> list[dict]:
    """Return a list of slide info dicts.

    Each dict has:
      slide_id  : str (e.g. "slide-01")
      png_path  : Path | None
      template  : Path | None  (template.html)
      template_dir : Path | None
      instructions : Path | None
    """
    slides_dir = run / "_slides"
    result = []

    if slides_dir.is_dir():
        seen: set[str] = set()
        # A RICH slide dir whose name is NOT slide-NN (e.g. an emitted output stem
        # like `preview`) carrying real `data`/template.html — see #11. We collect
        # it here and graft it onto a stable slide id below, so its hero+text data
        # is not silently dropped by the slide-NN-only filter.
        rich_alias: dict | None = None
        # Pipeline-created per-slide dirs: _slides/slide-N/. Only real slide dirs —
        # _slides/_shared/ (the copied styles.css + fonts, AIOS-139 Addendum 8 #1)
        # and any other non-slide entry must NOT be treated as a slide.
        for sd in sorted(slides_dir.iterdir(), key=lambda p: p.name):
            if not sd.is_dir() or not re.match(r"slide-\d+$", sd.name):
                # #11 — a non-slide-NN dir may still be a rich, editable slide
                # (legacy/edge emit named after the output stem). Recognize the
                # first one carrying a metadata.json{data} and/or template.html.
                # _shared is never a slide; malformed metadata.json is skipped.
                if (sd.is_dir() and sd.name != "_shared" and rich_alias is None):
                    r_data: dict | None = None
                    r_tdir: Path | None = None
                    r_meta = sd / "metadata.json"
                    if r_meta.is_file():
                        try:
                            m = json.loads(r_meta.read_text(encoding="utf-8"))
                            if isinstance(m.get("data"), dict) and m["data"]:
                                r_data = m["data"]
                            rtd = m.get("template_dir") or m.get("templateDir")
                            if rtd:
                                r_tdir = Path(rtd)
                        except Exception:
                            pass
                    if (sd / "template.html").is_file():
                        r_tdir = sd
                    elif not (r_tdir and (r_tdir / "template.html").is_file()):
                        r_tdir = None
                    if r_data or r_tdir:
                        rich_alias = {"data": r_data, "template_dir": r_tdir}
                continue
            slide_id = sd.name
            # Look for a metadata.json or template_dir marker
            meta_file = sd / "metadata.json"
            template_dir: Path | None = None
            slide_data: dict | None = None
            source_template_dir: Path | None = None
            if meta_file.is_file():
                try:
                    meta = json.loads(meta_file.read_text(encoding="utf-8"))
                    td = meta.get("template_dir") or meta.get("templateDir")
                    if td:
                        template_dir = Path(td)
                    # AIOS-139 Addendum 8 #1 — the run's REAL slot copy, persisted by
                    # render_template --emit-edit-slide. Used as the live + rebake
                    # baseline so the editor shows the actual post (not sample text).
                    if isinstance(meta.get("data"), dict):
                        slide_data = meta["data"]
                    # r5f F2b — emit_edit_slide's absolute pointer back to the source
                    # template dir: the asset-resolution fallback for refs an older
                    # emit left behind (root-loose bg.png → white editor bg).
                    std = meta.get("source_template_dir")
                    if std:
                        source_template_dir = Path(std)
                except Exception:
                    pass
            # Also check a template.html directly in the slide dir
            tmpl = sd / "template.html"
            if tmpl.is_file():
                template_dir = sd
            elif template_dir and (template_dir / "template.html").is_file():
                pass  # already set
            else:
                template_dir = None
            png = run / f"{slide_id}.png"
            instructions = (template_dir / "instructions.md") if template_dir else None
            result.append({
                "slide_id": slide_id,
                "png_path": png if png.is_file() else None,
                "template": (template_dir / "template.html") if template_dir else None,
                "template_dir": template_dir,
                "instructions": instructions if (instructions and instructions.is_file()) else None,
                "data": slide_data,
                "source_template_dir": source_template_dir,
            })
            seen.add(slide_id)
        # Union with flat slide-*.png in the run root that have NO _slides/ entry —
        # in a real run only the templated slides get a _slides/ dir, so the full-AI
        # slides must still appear (and in slide-number order) or the carousel drops
        # them. (AIOS-139 Addendum 8 #1 — regression guard.)
        for p in run.glob("slide-*.png"):
            m = re.search(r"(slide-\d+)", p.stem)
            sid = m.group(1) if m else p.stem
            if sid in seen:
                continue
            result.append({
                "slide_id": sid, "png_path": p, "template": None,
                "template_dir": None, "instructions": None, "data": None,
            })
            seen.add(sid)
        # #11 — graft the rich non-slide-NN dir onto a stable slide id. Prefer an
        # existing slide-NN already in `result` (don't double-count); else treat
        # the rich dir as slide-01. Enrich an existing flat-only entry with the
        # rich data/template_dir so its hero + text become editable.
        if rich_alias is not None:
            target = next((d for d in result if re.match(r"slide-\d+$", d["slide_id"])),
                          None)
            sid = target["slide_id"] if target is not None else "slide-01"
            r_tdir = rich_alias["template_dir"]
            instructions = (r_tdir / "instructions.md") if r_tdir else None
            if target is None:
                png = run / f"{sid}.png"
                result.append({
                    "slide_id": sid,
                    "png_path": png if png.is_file() else None,
                    "template": (r_tdir / "template.html") if r_tdir else None,
                    "template_dir": r_tdir,
                    "instructions": instructions if (instructions and instructions.is_file()) else None,
                    "data": rich_alias["data"],
                })
                seen.add(sid)
            else:
                if rich_alias["data"] and not target.get("data"):
                    target["data"] = rich_alias["data"]
                if r_tdir and not target.get("template_dir"):
                    target["template_dir"] = r_tdir
                    target["template"] = (r_tdir / "template.html")
                    target["instructions"] = (
                        instructions if (instructions and instructions.is_file()) else None
                    )
        if result:
            result.sort(key=lambda d: int(re.search(r"slide-(\d+)", d["slide_id"]).group(1))
                        if re.search(r"slide-(\d+)", d["slide_id"]) else 0)
            return result

    # Second fallback: scan for slide-N/ directories directly under run/
    # (used by the test fixture and by minimal run layouts without _slides/).
    slide_dirs = sorted(
        [d for d in run.iterdir() if d.is_dir() and re.match(r"slide-\d+", d.name)],
        key=lambda d: d.name,
    )
    if slide_dirs:
        for sd in slide_dirs:
            slide_id = sd.name
            template = sd / "template.html"
            instructions = sd / "instructions.md"
            png = run / f"{slide_id}.png"
            result.append({
                "slide_id": slide_id,
                "png_path": png if png.is_file() else None,
                "template": template if template.is_file() else None,
                "template_dir": sd if template.is_file() else None,
                "instructions": instructions if instructions.is_file() else None,
            })
        return result

    # Final fallback: just find slide-*.png files (FULL_AI / no template dir info)
    pngs = sorted(
        run.glob("slide-*.png"),
        key=lambda p: int(re.search(r"slide-(\d+)", p.name).group(1)) if re.search(r"slide-(\d+)", p.name) else 0,
    )
    for p in pngs:
        m = re.search(r"(slide-\d+)", p.stem)
        slide_id = m.group(1) if m else p.stem
        result.append({
            "slide_id": slide_id,
            "png_path": p,
            "template": None,
            "template_dir": None,
            "instructions": None,
        })
    return result


# Hero image slots bound by the template via ``src="{{X_PATH}}"`` or
# ``background-image:url('{{X_PATH}}')``. In TEMPLATE mode (not a post) the run's
# data dict never pins these (a template isn't a post), so fill() would substitute
# them to empty → ``src=""`` / ``url('')`` → the "missing image" placeholder fires
# on every template even though the template's AI hero asset exists on disk under
# ``_ai_bg/``. _resolve_hero_slots resolves each unfilled hero ``*_PATH`` to the REAL
# ``_ai_bg`` asset BEFORE fill, so the photo shows; the placeholder then fires ONLY
# for a genuinely-missing asset (truly unwired). Mirrors the bake's hero resolution.
#
# SCOPE BY ROLE, not by ``_PATH`` suffix. The earlier regex matched ANY ``{{*_PATH}}``
# bound via ``src=``/``background-image:url(`` and resolved EVERY one to the single
# ``_ai_bg`` hero — so the logo badge (``<img src="{{BRAND_LOGO_PATH}}">``) got the
# hero photo instead of the brand mark, and any icon/svg slot would too. A hero slot
# is identified by ROLE: its slot name is a hero name (``PHOTO_MAIN`` / ``BG`` /
# ``PHOTO_*`` / ``HERO_*``, with optional ``_PATH``) OR the bound element carries
# ``data-zone="photo"`` / ``data-slot="PHOTO_MAIN"``. LOGO / ICON / SVG / BRAND
# slots are NEVER hero — they resolve from the brand (``_resolve_brand_asset_slots``),
# never from ``_ai_bg``.
_HERO_SLOT_IN_HTML_RE = re.compile(
    r"""(?:src\s*=\s*['"]|background-image\s*:\s*url\(\s*['"]?)\s*"""
    r"""\{\{\s*(?P<slot>[A-Z][A-Z0-9_]*_PATH)\s*\}\}""",
    re.IGNORECASE,
)
_HERO_MEDIA_TYPE_BY_EXT = {
    ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
    ".webp": "image/webp", ".gif": "image/gif",
}

# Brand-asset slot roles — a slot whose name contains any of these tokens is brand
# chrome (logo / icon / vector mark), NEVER the AI hero. It resolves from the brand,
# not from ``_ai_bg``. Checked on the slot name with the ``_PATH`` suffix stripped.
_BRAND_ASSET_SLOT_TOKENS = ("LOGO", "ICON", "SVG", "BRAND", "WORDMARK", "MARK")
# Hero slot roles by NAME (``_PATH`` stripped). A bound element with
# ``data-zone="photo"`` / ``data-slot="PHOTO_MAIN"`` also qualifies (see
# ``_is_hero_binding``), covering the bg-image-div hero.
_HERO_SLOT_NAMES = ("PHOTO_MAIN", "BG", "HERO", "PHOTO", "BACKGROUND")
# Photo-zone markers on the element bearing the binding (``data-zone="photo"`` /
# ``data-slot="PHOTO_MAIN"``). Quote- and whitespace-tolerant so a MULTI-LINE
# ``<img …>`` whose attributes use single quotes or extra spacing (or sit on
# separate lines) still classifies as hero. The tag window already spans newlines;
# this makes the marker match robust to authoring style too.
_HERO_ZONE_ATTR_RE = re.compile(
    r"""data-(?:zone\s*=\s*['"]\s*photo\s*['"]"""
    r"""|slot\s*=\s*['"]\s*photo_main\s*['"])""",
    re.IGNORECASE,
)


def _slot_role_is_brand(slot_name: str) -> bool:
    """True when the slot name marks brand chrome (logo/icon/svg/brand mark) — must
    NEVER resolve to the ``_ai_bg`` hero. Suffix-agnostic (``_PATH`` stripped)."""
    base = slot_name.upper()
    for suf in ("_PATH", "_SRC", "_HTML"):
        if base.endswith(suf):
            base = base[: -len(suf)]
            break
    return any(tok in base for tok in _BRAND_ASSET_SLOT_TOKENS)


def _slot_role_is_hero(slot_name: str) -> bool:
    """True when the slot name marks the AI hero/photo zone. Brand tokens win
    (a ``LOGO`` slot is never hero even if it somehow also matched a hero token)."""
    if _slot_role_is_brand(slot_name):
        return False
    base = slot_name.upper()
    for suf in ("_PATH", "_SRC", "_HTML"):
        if base.endswith(suf):
            base = base[: -len(suf)]
            break
    return base in _HERO_SLOT_NAMES or base.startswith(("PHOTO_", "HERO_"))


def _is_hero_binding(raw_html: str, match: re.Match) -> bool:
    """Decide whether the matched ``{{*_PATH}}`` binding is the AI hero/photo.

    Hero iff: the slot NAME is a hero role (``_slot_role_is_hero``) OR the element
    that carries the binding declares ``data-zone="photo"`` / ``data-slot="PHOTO_MAIN"``.
    Brand-asset names (logo/icon/svg/brand) are excluded up front so a logo binding is
    never treated as hero even if it sits in a photo-zoned wrapper."""
    slot = match.group("slot")
    if _slot_role_is_brand(slot):
        return False
    if _slot_role_is_hero(slot):
        return True
    # Inspect the element bearing the binding: walk back to the opening '<' and
    # forward to the closing '>' of the SAME tag (the binding lives inside a
    # start-tag — either an <img src=…> or a <div style="background-image:…">).
    start = raw_html.rfind("<", 0, match.start())
    end = raw_html.find(">", match.start())
    if start == -1 or end == -1:
        return False
    tag = raw_html[start : end + 1]
    return _HERO_ZONE_ATTR_RE.search(tag) is not None


def _resolve_ai_bg_asset(template_dir: Path) -> Path | None:
    """Resolve a template's AI hero asset on disk, robust to naming.

    Resolution order (templates name the file differently):
      1. canonical ``_ai_bg/photo_main.png`` if present;
      2. else the single ``_ai_bg/*.png`` when there is exactly one
         (e.g. ``numbered-body`` ships ``_ai_bg/bg.png``);
      3. else a conventional template-root ``bg.png``.
    Returns None when no asset exists (genuinely unwired)."""
    if template_dir is None:
        return None
    ai_bg = template_dir / "_ai_bg"
    canonical = ai_bg / "photo_main.png"
    if canonical.is_file():
        return canonical
    if ai_bg.is_dir():
        pngs = sorted(p for p in ai_bg.glob("*.png") if p.is_file())
        if len(pngs) == 1:
            return pngs[0]
    root_bg = template_dir / "bg.png"
    return root_bg if root_bg.is_file() else None


def _resolve_hero_slots(raw_html: str, data: dict, template_dir: Path | None) -> dict:
    """For each hero image slot bound in ``raw_html`` (``src="{{X_PATH}}"`` /
    ``background-image:url('{{X_PATH}}')``) that is NOT already filled in ``data``,
    resolve it to the template's real ``_ai_bg`` asset (base64 data-URI) so the live
    Studio canvas shows the photo — instead of an empty src that the placeholder would
    flag as "missing image". No-op when the slot is already filled (a real post pins
    it) or when no asset exists (truly unwired → placeholder fires, correctly)."""
    if template_dir is None:
        return data
    out = dict(data)
    asset: Path | None = None  # resolve lazily, reuse across slots
    resolved = False
    for m in _HERO_SLOT_IN_HTML_RE.finditer(raw_html):
        # SCOPE: resolve ONLY the hero/photo binding to _ai_bg. A LOGO/ICON/SVG/BRAND
        # slot — or any non-hero {{*_PATH}} — is skipped here so it is never clobbered
        # with the hero photo (the "logo got replaced by the preview image" bug).
        if not _is_hero_binding(raw_html, m):
            continue
        slot = m.group("slot").upper()
        existing = out.get(slot)
        # Already filled to a real asset (data-URI / http / on-disk) → leave it.
        if isinstance(existing, str) and existing and existing.startswith(("data:", "http://", "https://")):
            continue
        if not resolved:
            asset = _resolve_ai_bg_asset(Path(template_dir))
            resolved = True
        if asset is None:
            continue
        media = _HERO_MEDIA_TYPE_BY_EXT.get(asset.suffix.lower(), "image/png")
        out[slot] = f"data:{media};base64,{base64.b64encode(asset.read_bytes()).decode('ascii')}"
    return out


def _resolve_brand_logo_asset(template_dir: Path | None, brand_context: Path | None) -> Path | None:
    """Resolve the brand mark on disk for an unfilled brand-asset slot.

    Resolution order (closest-wins, template-local before brand-global):
      1. ``<template_dir>/assets/*logo*`` (the template ships its own mark);
      2. ``<brand_context>/visual-identity/logos/*-transparent.{png,svg}``;
      3. ``<brand_context>/visual-identity/logos/*.{png,svg,jpg,jpeg,webp}``.
    Returns None when no brand asset exists (slot then stays empty → handled by the
    empty-image flow, never given the hero photo)."""
    exts = (".png", ".svg", ".jpg", ".jpeg", ".webp")
    if template_dir is not None:
        adir = Path(template_dir) / "assets"
        if adir.is_dir():
            cands = sorted(p for p in adir.iterdir()
                           if p.is_file() and "logo" in p.name.lower()
                           and p.suffix.lower() in exts)
            if cands:
                return cands[0]
    if brand_context is not None:
        logos = Path(brand_context) / "visual-identity" / "logos"
        if logos.is_dir():
            for pat in ("*-transparent.png", "*-transparent.svg"):
                for c in sorted(logos.glob(pat)):
                    if c.is_file():
                        return c
            for c in sorted(logos.iterdir()):
                if c.is_file() and c.suffix.lower() in exts:
                    return c
    return None


def _resolve_brand_asset_slots(
    raw_html: str, data: dict, template_dir: Path | None, brand_context: Path | None
) -> dict:
    """For each BRAND-asset image slot bound in ``raw_html`` (logo/icon/svg/brand mark)
    that is NOT already filled, resolve it to the brand's logo on disk (base64
    data-URI) — NEVER to the ``_ai_bg`` hero. Mirrors the bake, which fills
    ``BRAND_LOGO_PATH`` from the post data + brand. No-op when the slot is already
    filled or when no brand asset exists (slot stays empty, correctly)."""
    out = dict(data)
    asset: Path | None = None
    resolved = False
    for m in _HERO_SLOT_IN_HTML_RE.finditer(raw_html):
        slot = m.group("slot").upper()
        if not _slot_role_is_brand(slot):
            continue
        existing = out.get(slot)
        if isinstance(existing, str) and existing and existing.startswith(("data:", "http://", "https://")):
            continue
        if not resolved:
            asset = _resolve_brand_logo_asset(template_dir, brand_context)
            resolved = True
        if asset is None:
            continue
        media = _HERO_MEDIA_TYPE_BY_EXT.get(asset.suffix.lower(),
                                            "image/svg+xml" if asset.suffix.lower() == ".svg" else "image/png")
        out[slot] = f"data:{media};base64,{base64.b64encode(asset.read_bytes()).decode('ascii')}"
    return out


def _build_srcdoc(
    template_path: Path,
    data: dict,
    tokens_css: str,
    shared_css_content: str,
    shared_css_dir: Path | None = None,
    source_template_dir: Path | None = None,
    brand_context: Path | None = None,
) -> str:
    """Produce a font-correct, Mustache-filled srcdoc string for one template slide.

    ``source_template_dir`` (metadata.json's absolute pointer back to the source
    template, recorded by ``emit_edit_slide``) is a SECOND base for relative-URL
    inlining (r5f F2b): a ref the emitted slide dir doesn't carry (e.g. a
    template-root ``bg.png`` left behind by an older emit) gets resolved against
    the source template dir instead of 404ing white — heals already-emitted runs.

    Steps (mirrors render_template.py but without Playwright):
    1. Read raw HTML.
    2. Fill Mustache placeholders with ``fill()``.
    3. Inline relative URLs in shared CSS (base64 @font-face .ttf) relative to
       shared_css_dir so that font URLs in the style block become data URIs.
    4. Prepend inlined ``_shared/styles.css`` as a ``<style>`` block (Pitfall 1).
    5. Run ``_inline_relative_urls()`` on the filled HTML so @font-face ttf +
       bg.png + <img src> references in the template itself become base64.
    6. Inject brand tokens CSS after the shared sheet so brand vars win.
    7. Inject ``.slide { container-type: inline-size; }`` for cqw resolution.
    """
    raw_html = template_path.read_text(encoding="utf-8", errors="ignore")
    template_dir = template_path.parent

    # 0. Resolve unfilled hero image slots to the template's real _ai_bg asset
    #    BEFORE fill (template mode: a template isn't a post, so its data dict never
    #    pins PHOTO_MAIN_PATH / BG_PATH). Without this, fill() leaves src=""/url('')
    #    and _placeholder_empty_images flags every template "missing image" even
    #    though the AI hero exists on disk. After this, the placeholder fires ONLY
    #    when the asset is genuinely absent. No-op when the slot is already filled.
    data = _resolve_hero_slots(raw_html, data, template_dir)

    # 0b. Resolve unfilled BRAND-asset slots (logo/icon/svg/brand mark) from the
    #     BRAND — never from _ai_bg. Scoped by role so the logo badge shows the
    #     brand mark, not the hero photo (the cross-contamination bug). No-op when
    #     the slot is filled or no brand asset exists.
    data = _resolve_brand_asset_slots(raw_html, data, template_dir, brand_context)

    # 1. Mustache fill (same data dict the bake uses)
    filled = fill(raw_html, data)

    # 1b. Auto-tag decorative elements (bg rect, frame, logo, svg) so they become
    #     editable layers — same deterministic tagging the bake uses (parity).
    filled = _tag_decor(filled)

    # 2. Prepare shared CSS for the srcdoc <style> block.
    #    Font @font-face urls are rewritten to /fonts/<basename> so the Studio
    #    HTTP server resolves them (fix #3: fonts in canvas). The srcdoc has
    #    allow-same-origin, so absolute paths like /fonts/… resolve to the
    #    Studio's localhost origin. Non-font urls are left for _inline_relative_urls.
    #    Fallback: if _inline_relative_urls CAN resolve a font (base64), it still
    #    wins because the regex below only touches unresolved relative paths.
    _FONT_URL_RE = re.compile(
        r"""url\(\s*['"]?(?P<p>[^'")\s]+\.(?:woff2|ttf))['"]?\s*\)""",
        re.IGNORECASE,
    )
    shared_style_block = ""
    if shared_css_content:
        # Rewrite font paths to /fonts/<basename> for HTTP serving.
        def _to_server_font(m: re.Match) -> str:
            basename = Path(m.group("p")).name
            return f"url('/fonts/{basename}')"
        css_server_fonts = _FONT_URL_RE.sub(_to_server_font, shared_css_content)
        # Still run _inline_relative_urls to base64-encode any remaining
        # non-font relative urls (bg references, etc.) in the CSS.
        css_inlined = css_server_fonts
        if shared_css_dir and shared_css_dir.is_dir():
            css_inlined = _inline_relative_urls(css_server_fonts, shared_css_dir)
        shared_style_block = f"<style>\n/* inlined _shared/styles.css */\n{css_inlined}\n</style>\n"

    # 3. Base64-inline relative URLs in the filled template HTML
    #    (@font-face .ttf in <style> tags, bg.png url(), <img src>)
    filled = _inline_relative_urls(filled, template_dir)

    # 3a. Second pass against the SOURCE template dir (r5f F2b): refs the slide
    #     dir doesn't carry (root-loose bg.png from an older emit) resolve against
    #     metadata.json's source_template_dir. The first pass already consumed
    #     everything resolvable locally, so this only touches leftovers.
    if (
        source_template_dir
        and source_template_dir.is_dir()
        and source_template_dir.resolve() != template_dir.resolve()
    ):
        filled = _inline_relative_urls(filled, source_template_dir)

    # 3b. Empty image slots (no generated image yet) -> canonical ref placeholder
    #     so the AI zone reads as the intended composition, not a broken <img>.
    filled = _placeholder_empty_images(filled, template_dir)

    # 4. Inject brand tokens CSS AFTER shared sheet (brand wins)
    brand_style = ""
    if tokens_css:
        brand_style = f"<style>:root {{ {tokens_css} }}</style>\n"

    # 5. Inject container-type for cqw resolution (Open Q3, RESEARCH.md)
    container_style = "<style>.slide { container-type: inline-size; }</style>\n"

    # 5a1. Hero-photo fit floor (front == bake): a hero <img> in an absolutely-sized
    #      box must fill its box (object-fit:cover). When the template omits object-fit
    #      the browser default stretches/mis-frames it (subject "pushed to the bottom").
    #      IDENTICAL rule to render_template.HERO_FIT_CSS so the editor canvas and the
    #      rebaked PNG agree. Inline object-fit on the element wins, so authored
    #      templates (e.g. boxed-headline-cover) are unchanged.
    hero_fit_style = (
        '<style>img[data-slot="PHOTO_MAIN"],img[data-zone="photo"]'
        '{object-fit:cover;object-position:center center;}</style>\n'
    )

    # 5a2. Autosize text-fit parity (Bug A — preview == bake).
    #     The bake (render_template.autosize_text_fit) shrinks every text slot to fit
    #     its dimension-locked box BEFORE the screenshot, so a long headline never
    #     spills its zone in the PNG. The live editor canvas had NO equivalent, so it
    #     rendered the headline at the authored cqw size — overflowing its zone and
    #     landing on the photo subject (the "headline lands ON the person" report on
    #     fullbleed-photo-cover). Run the SAME algorithm in-iframe after fonts resolve
    #     so the editable canvas positions/sizes text IDENTICALLY to the bake. Mirrors
    #     render_template._AUTOSIZE_JS + its constants (TOL 2.0 / floor 0.5×|22px).
    autosize_script = _AUTOSIZE_SRCDOC_SCRIPT

    # 5b. Curated Google Fonts <link> — SAME builder the bake uses, so a per-layer
    #     fontFamily override renders identically in this iframe and in the rebaked
    #     PNG (AIOS-139 Stage A parity). Non-brand fonts require network (accepted
    #     trade-off); brand @font-face fonts in the shared CSS still work offline.
    fonts_link = build_google_fonts_link() + "\n"

    # 6. Assemble: prepend the style blocks inside <head>, or at the top.
    injection = fonts_link + shared_style_block + brand_style + container_style + hero_fit_style
    if "<head>" in filled:
        filled = filled.replace("<head>", "<head>\n" + injection, 1)
    else:
        filled = injection + filled

    # 7. Append the autosize parity script at end of <body> (after the DOM exists),
    #    so it runs on the laid-out slide once fonts resolve — same net as the bake.
    if "</body>" in filled:
        filled = filled.replace("</body>", autosize_script + "</body>", 1)
    else:
        filled = filled + autosize_script

    return filled


# Autosize text-fit, ported 1:1 from render_template._AUTOSIZE_JS so the live editor
# iframe shrinks overflowing text to its dimension-locked box EXACTLY as the headless
# bake does (Bug A — preview == bake). Self-contained <script> for the sandboxed
# srcdoc (allow-scripts); waits for document.fonts.ready so it measures at the real
# brand-font metrics, never fallback metrics. Idempotent: content that already fits
# reports "fit" and no style is mutated (no regression for correct templates).
# Constants mirror render_template.AUTOSIZE_{TOL_PX,FLOOR_FRAC,FLOOR_ABS_PX}.
_AUTOSIZE_SRCDOC_SCRIPT = r"""
<script>
(function () {
  var OPTS = { tolPx: 2.0, floorFrac: 0.5, floorAbsPx: 22.0 };
  function autosize(opts) {
    var TOL = opts.tolPx, FLOOR_FRAC = opts.floorFrac, FLOOR_ABS = opts.floorAbsPx;
    var lockedBox = function (leaf) {
      var el = leaf;
      while (el && el !== document.body) {
        var cs = getComputedStyle(el);
        var fixedH = (el.style && el.style.height && el.style.height.indexOf('%') >= 0) ||
                     (cs.position === 'absolute' && cs.height !== 'auto');
        if (fixedH) return el;
        el = el.parentElement;
      }
      return leaf;
    };
    var measure = function (leaf, box) {
      var bcs = getComputedStyle(box);
      var availW = box.clientWidth  - parseFloat(bcs.paddingLeft) - parseFloat(bcs.paddingRight);
      var availH = box.clientHeight - parseFloat(bcs.paddingTop)  - parseFloat(bcs.paddingBottom);
      var lcs = getComputedStyle(leaf);
      var probe = document.createElement('span');
      probe.innerHTML = leaf.innerHTML;
      Object.assign(probe.style, {
        position: 'absolute', left: '-99999px', top: '0', visibility: 'hidden',
        whiteSpace: 'nowrap', display: 'inline-block', margin: '0', padding: '0',
        fontFamily: lcs.fontFamily, fontSize: lcs.fontSize, fontWeight: lcs.fontWeight,
        fontStyle: lcs.fontStyle, letterSpacing: lcs.letterSpacing,
        lineHeight: lcs.lineHeight, textTransform: lcs.textTransform
      });
      document.body.appendChild(probe);
      var natW = probe.getBoundingClientRect().width;
      probe.style.whiteSpace = 'normal';
      probe.style.width = Math.max(0, availW) + 'px';
      var wrapH = probe.getBoundingClientRect().height;
      document.body.removeChild(probe);
      return { overW: natW - availW, overH: wrapH - availH, availW: availW, availH: availH };
    };
    var leaves = [];
    document.querySelectorAll('[data-slot]').forEach(function (z) {
      var disp = z.querySelector('.display, [data-role="display"]');
      var leaf = disp || z;
      if ((leaf.textContent || '').trim().length) leaves.push(leaf);
    });
    leaves.forEach(function (leaf) {
      var box = lockedBox(leaf);
      var orig = parseFloat(getComputedStyle(leaf).fontSize);
      if (!isFinite(orig) || orig <= 0) return;
      var floor = Math.max(FLOOR_ABS, orig * FLOOR_FRAC);
      var m = measure(leaf, box);
      // SHRINK-ONLY: underflowing text is LEFT AT its authored size — never grown to
      // fill the box. A 2-char word in a slot authored for a long word stays at the
      // authored size, not inflated. hi is hard-capped at orig (the ceiling) below.
      if (m.overW <= TOL && m.overH <= TOL) return;
      var lo = floor, hi = orig, best = null;
      for (var i = 0; i < 24 && hi - lo > 0.4; i++) {
        var mid = (lo + hi) / 2;
        leaf.style.setProperty('font-size', mid + 'px', 'important');
        m = measure(leaf, box);
        if (m.overW <= TOL && m.overH <= TOL) { best = mid; lo = mid; } else { hi = mid; }
      }
      var size = best !== null ? best : orig;
      for (var j = 0; j < 200; j++) {
        leaf.style.setProperty('font-size', size + 'px', 'important');
        m = measure(leaf, box);
        if (m.overW <= TOL && m.overH <= TOL) { best = size; break; }
        if (size - 1 < floor) { size = floor; leaf.style.setProperty('font-size', floor + 'px', 'important'); m = measure(leaf, box); break; }
        size -= 1;
      }
      if (m.overW > TOL || m.overH > TOL) box.style.setProperty('overflow', 'hidden');
    });
  }
  function run() { try { autosize(OPTS); } catch (e) {} }
  // Expose so the editor can re-fit after a live text edit (parity with the bake,
  // which always autosizes on the FINAL filled DOM). The editor calls this through
  // the iframe's contentWindow after changing text.
  window.__autosizeRun = run;
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(run);
    // Belt-and-suspenders: fonts.ready can resolve before late web fonts swap in
    // certain engines — re-run shortly after so the final metrics win.
    setTimeout(run, 250);
  } else {
    run();
  }
})();
</script>
"""


def _html_attr_escape(s: str) -> str:
    """Escape a string for use as an HTML attribute value (double-quoted)."""
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")


_HANDLE_SUFFIXES = ("_PATH", "_HTML", "_SRC")


def _slot_handle(name: str) -> tuple[str, bool]:
    """Map an instructions slot name to the template's ``data-slot`` handle.

    Image/asset slots are written in instructions.md WITH a ``_PATH``/``_HTML``/
    ``_SRC`` suffix (e.g. ``PHOTO_MAIN_PATH``, ``ANNOTATION_SVG_PATH``), but the
    template's editable ``data-slot`` has the suffix STRIPPED (the authoring rule
    enforced by ``migrate_data_slots``: ``PHOTO_MAIN``, ``ANNOTATION_SVG``). The
    editor MUST target the stripped handle or every image/asset control silently
    edits a non-existent element (the root cause of "image edits do nothing").

    Returns ``(handle, is_asset)`` — ``is_asset`` is True when a suffix was
    stripped (the slot is an image/asset zone, not a text/pill zone)."""
    for suf in _HANDLE_SUFFIXES:
        if name.endswith(suf) and len(name) > len(suf):
            return name[: -len(suf)], True
    return name, False


def _present_handles(html_text: str) -> set[str]:
    """All ``data-slot`` handles actually present in a rendered slide's HTML — used
    to skip controls for slots that aren't real editable zones in the DOM (e.g. a
    prompt-only slot like ``PHOTO_SUBJECT``, or an optional ``{{#…}}`` overlay that
    wasn't supplied)."""
    return set(re.findall(r'data-slot="([^"]+)"', html_text))


def _present_order(html_text: str) -> list[str]:
    """``data-slot`` handles in DOM order (deduped, first occurrence). DOM order
    approximates stacking order — earlier = behind, later = in front."""
    seen, order = set(), []
    for h in re.findall(r'data-slot="([^"]+)"', html_text):
        if h not in seen:
            seen.add(h); order.append(h)
    return order


# Decorative elements that templates ship WITHOUT a data-slot (background rects,
# the dot-grid svg, the logo stamp, frame cards). Auto-tag them so they become
# editable layers too. (tag, class-keyword regex, synthetic handle).
_DECOR_RULES = [
    ("div", r"\bbg\b", "BACKGROUND"),
    ("div", r"frame", "FRAME"),
    ("img", r"logo", "LOGO"),
]


def _inject_first_slot(html_text: str, tag: str, kw: str, handle: str) -> str:
    """Add ``data-slot="handle"`` to the FIRST <tag> that has a class matching *kw*
    and no existing data-slot. Idempotent (skips tags that already carry one)."""
    pat = re.compile(
        r'(<' + tag + r'\b(?![^>]*\bdata-slot=)[^>]*?\bclass="[^"]*' + kw + r'[^"]*"[^>]*?)(>)',
        re.IGNORECASE,
    )
    return pat.sub(lambda m: f'{m.group(1)} data-slot="{handle}"{m.group(2)}', html_text, count=1)


# A wrapper div that visually IS one full-bleed AI image (the whole slide is a single
# generated composition) is, by the authoring rule, the editable PHOTO_MAIN image layer
# — NOT a decorative "frame". Some legacy templates were authored the wrong way: the
# full-bleed AI <img> sits inside a ``frame``-class wrapper (which the FRAME decor rule
# would mis-tag as a non-editable shape) while a SECOND, redundant ``data-slot="PHOTO_MAIN"``
# zone binds the SAME path (an invisible marker → phantom empty slot in the editor).
# ``_collapse_fullbleed_ai`` repairs that BEFORE decor-tagging so the editor exposes
# exactly ONE editable image layer.
#
# An <img> is treated as the full-bleed AI image when it carries an ``ai-render``-style
# class OR binds the PHOTO_MAIN path. Matching is case-agnostic and run-agnostic.
_FULLBLEED_AI_IMG_RE = re.compile(
    r'<img\b(?=[^>]*\bclass="[^"]*\b(?:ai-render|ai-image|fullbleed|full-bleed)\b[^"]*")'
    r'[^>]*\bsrc="\{\{?\s*PHOTO_MAIN(?:_PATH)?\s*\}?\}"[^>]*>'
    r'|<img\b[^>]*\bsrc="\{\{?\s*PHOTO_MAIN(?:_PATH)?\s*\}?\}"[^>]*\bclass="[^"]*\bai-render\b[^"]*"[^>]*>',
    re.IGNORECASE,
)
# A frame-class wrapper holding an <img> whose src is the PHOTO_MAIN path.
_FRAME_WITH_PHOTO_RE = re.compile(
    r'(<div\b(?![^>]*\bdata-slot=)[^>]*\bclass="[^"]*\bframe\b[^"]*"[^>]*>)'
    r'(\s*<img\b[^>]*\bsrc="\{\{?\s*PHOTO_MAIN(?:_PATH)?\s*\}?\}"[^>]*>\s*)'
    r'(</div>)',
    re.IGNORECASE,
)
# A standalone PHOTO_MAIN slot div binding the PHOTO_MAIN path (the redundant marker).
_PHOTO_MAIN_SLOT_DIV_RE = re.compile(
    r'<div\b[^>]*\bdata-slot="PHOTO_MAIN"[^>]*>\s*'
    r'<img\b[^>]*\bsrc="\{\{?\s*PHOTO_MAIN(?:_PATH)?\s*\}?\}"[^>]*>\s*</div>',
    re.IGNORECASE,
)


def _collapse_fullbleed_ai(html_text: str) -> str:
    """Repair the full-bleed-AI authoring anti-pattern so the editor sees ONE editable
    image layer (no non-editable frame, no phantom empty PHOTO_MAIN slot).

    When a ``frame``-class wrapper holds the full-bleed AI image (``src`` = PHOTO_MAIN
    path) AND a separate ``data-slot="PHOTO_MAIN"`` element binds the SAME path:
      (a) promote the wrapper to ``data-slot="PHOTO_MAIN"`` so the live full-bleed image
          becomes the editable PHOTO_MAIN layer (Edit-with-AI / replace / magiclayer), and
      (b) drop the redundant PHOTO_MAIN marker so no phantom empty slot remains.

    Deterministic + idempotent (runs before ``_tag_decor`` → preview parity). No-op for
    templates authored the canonical way (single full-bleed PHOTO_MAIN, no frame wrapper).
    """
    # Only act when there IS a frame-wrapped PHOTO_MAIN image to promote.
    if not _FRAME_WITH_PHOTO_RE.search(html_text):
        return html_text
    # (b) FIRST drop the redundant standalone PHOTO_MAIN marker, so the promotion in (a)
    #     can't re-match it. (The marker is the invisible zone-div; the frame wrapper is
    #     the one that visually renders the AI image and must become editable.)
    html_text = _PHOTO_MAIN_SLOT_DIV_RE.sub("", html_text, count=1)
    # (a) Promote the frame wrapper → editable PHOTO_MAIN image layer.
    m = _FRAME_WITH_PHOTO_RE.search(html_text)
    if m and 'data-slot=' not in m.group(1).lower():
        promoted = m.group(1)[:-1] + ' data-slot="PHOTO_MAIN" data-zone="photo">'
        html_text = html_text[:m.start(1)] + promoted + html_text[m.end(1):]
    return html_text


_BG_LAYER_DIV = (
    '<div data-slot="BACKGROUND" '
    'style="position:absolute;inset:0;background:inherit;z-index:0"></div>'
)


def _tag_root_bg(html_text: str) -> str:
    """Root-background fallback: when no element carries BACKGROUND (the bg lives on the
    slide root / a CSS rule, not a ``div.bg``), make the backdrop a REAL **stackable**
    BACKGROUND layer (FASE 6 fix #1). A container can't be z-indexed above its own
    children, so instead of tagging the root ``.slide`` we inject a dedicated inset:0
    child: ``background:inherit`` renders the SAME backdrop, ``z-index:0`` keeps it behind
    content by default — and reordering it applies a real z-index (live via applyToSlide,
    baked via _build_tweaks_css) so raising it overlaps the layers below. Mirror of
    render_template._tag_root_bg → preview/rebake parity. No-op if a BACKGROUND already
    exists (e.g. a real div.bg or the full-AI layer-canvas <img>)."""
    if 'data-slot="BACKGROUND"' in html_text:
        return html_text
    # Inject as the FIRST child of the first .slide container…
    slide_pat = re.compile(
        r'(<div\b[^>]*\bclass="[^"]*\bslide\b[^"]*"[^>]*>)', re.IGNORECASE)
    out, n = slide_pat.subn(lambda m: m.group(1) + _BG_LAYER_DIV, html_text, count=1)
    if n:
        return out
    # …else as the first child of <body>.
    out, n = re.subn(
        r'(<body\b[^>]*>)', lambda m: m.group(1) + _BG_LAYER_DIV,
        html_text, count=1, flags=re.IGNORECASE)
    return out if n else html_text


def _tag_decor(html_text: str) -> str:
    """Auto-tag untagged decorative elements (background rect, frame, logo, inline
    svg graphics) with synthetic ``data-slot`` handles so the editor and the rebake
    both see them as editable layers. Deterministic + idempotent → preview/rebake
    parity holds. Preview/bake-shared (mirrored in render_template)."""
    # First: repair the full-bleed-AI anti-pattern (frame-wrapped AI image + duplicate
    # PHOTO_MAIN). After this, the AI wrapper carries data-slot="PHOTO_MAIN", so the
    # FRAME decor rule below skips it (it requires NO existing data-slot) and the image
    # is exposed as ONE editable layer instead of a non-editable frame + phantom slot.
    out = _collapse_fullbleed_ai(html_text)
    for tag, kw, handle in _DECOR_RULES:
        out = _inject_first_slot(out, tag, kw, handle)
    # decorative inline <svg> (e.g. dot-grid) — tag each one GRAPHIC, GRAPHIC2, ...
    n = [0]
    def _svg(m):
        n[0] += 1
        h = "GRAPHIC" if n[0] == 1 else f"GRAPHIC{n[0]}"
        return f'{m.group(1)} data-slot="{h}"{m.group(2)}'
    out = re.sub(r'(<svg\b(?![^>]*\bdata-slot=)[^>]*?)(>)', _svg, out, flags=re.IGNORECASE)
    return _tag_root_bg(out)


def _decor_type(handle: str) -> str:
    """Infer a control type for an auto-tagged decorative handle."""
    h = handle.upper()
    if h.startswith("GRAPHIC") or "SVG" in h:
        return "svg"
    if "LOGO" in h or "IMG" in h or "PHOTO" in h:
        return "image"
    return "shape"   # BACKGROUND, FRAME — colored boxes


def _synthetic_slots(present: set[str], covered: set[str]) -> list[dict]:
    """Slot dicts for DOM handles that no instructions slot covers (the auto-tagged
    decoration). Ordering/positioning is unknown, so bbox is None."""
    out = []
    for h in present:
        if h in covered or h.startswith("__"):
            continue
        if h not in {r[2] for r in _DECOR_RULES} and not h.startswith("GRAPHIC"):
            continue
        out.append({"name": h, "type": _decor_type(h), "bbox": None, "sample": "", "style": ""})
    return out


def _range_row(sid: str, handle: str, prop: str, label: str, lo, hi, step, val) -> str:
    """One control row: [name] [slider] [value]. Aligned 3-column grid (Figma-like)."""
    return (
        f'    <div class="ctrl-row">\n'
        f'      <span class="ctrl-name">{label}</span>\n'
        f'      <input type="range" data-prop="{prop}" min="{lo}" max="{hi}" step="{step}" value="{val}"\n'
        f'             oninput="applyToSlide(\'{sid}\',\'{handle}\',\'{prop}\',parseFloat(this.value)); '
        f'this.nextElementSibling.textContent=this.value">\n'
        f'      <span class="range-val">{val}</span>\n'
        f'    </div>'
    )


def _num_field(sid: str, handle: str, prop: str, icon_id: str, val, unit: str = "%") -> str:
    """A mockup-style boxed number field: [icon] [number] [unit]. data-prop lets the
    nudge pad sync the matching X/Y field after an arrow press."""
    return (
        f'      <div class="field" title="{prop}">\n'
        f'        {_sym(icon_id, 14)}\n'
        f'        <input type="number" data-prop="{prop}" value="{val}" '
        f'oninput="applyToSlide(\'{sid}\',\'{handle}\',\'{prop}\',parseFloat(this.value))">\n'
        f'        <span class="unit">{unit}</span>\n'
        f'      </div>'
    )


def _position_size_section(sid: str, handle: str, x, y, w, h=None) -> str:
    """Mockup "Position & Size" section: X/Y number fields, W (+ optional H) number
    fields, and a friendly directional nudge pad with a 1/8/24px step toggle. Position
    stays in % (parity with the rebake's left/top%); the px step is converted to % in
    JS against the 1080x1350 slide so nudging feels pixel-accurate."""
    def pad_btn(axis, direction, icon_id, aria):
        return (
            f'<button type="button" class="pad-btn p{aria[0]}" aria-label="{aria}" '
            f'onclick="nudge(\'{sid}\',\'{handle}\',\'{axis}\',{direction})">{_sym(icon_id, 14)}</button>'
        )
    size_fields = _num_field(sid, handle, "w", "ic-w", w)
    if h is not None:
        size_fields += "\n" + _num_field(sid, handle, "h", "ic-h", h)
    step_name = f"step-{sid}-{handle}"
    return f"""    <div class="sec-sub">
      <span class="label">Position</span>
      <div class="grid2">
{_num_field(sid, handle, "x", "ic-arrh", x)}
{_num_field(sid, handle, "y", "ic-arrv", y)}
      </div>
      <span class="label" style="margin-top:12px">Size</span>
      <div class="grid2">
{size_fields}
      </div>
      <div class="move">
        <div class="pad">
          {pad_btn("y", -1, "ic-up", "up")}
          {pad_btn("x", -1, "ic-left", "left")}
          <span class="pad-dot">{_sym("ic-dot", 12)}</span>
          {pad_btn("x", 1, "ic-right", "right")}
          {pad_btn("y", 1, "ic-down", "down")}
        </div>
        <div class="move-meta">
          <span class="mlabel">Move &middot; step</span>
          <div class="step">
            <label><input type="radio" name="{step_name}" checked onchange="setStep(1)">1<span class="su">px</span></label>
            <label><input type="radio" name="{step_name}" onchange="setStep(8)">8<span class="su">px</span></label>
            <label><input type="radio" name="{step_name}" onchange="setStep(24)">24<span class="su">px</span></label>
          </div>
        </div>
      </div>
    </div>"""


def _font_select(sid: str, handle: str, brand_fonts: list[str] | None) -> str:
    """Per-layer font-family selector (AIOS-139 Stage A): brand fonts pinned on top,
    then the curated free set. Live-applies via ``applyToSlide(...,'fontFamily',...)``
    and survives the rebake (``render_template`` honors ``fontFamily``).

    Uses a custom dropdown (not a native <select>) so it stays readable in the dark
    panel and each option renders in its own typeface."""
    bf = [f for f in (brand_fonts or []) if f]
    # Build a JSON-serialisable options list consumed by openEditorDrop() in JS.
    # Groups use {"g": label}; items use {"v": value, "l": label, "f": font-family}.
    dd_opts: list[dict] = [{"v": "", "l": "— template default —", "f": ""}]
    if bf:
        dd_opts.append({"g": "Brand"})
        dd_opts += [{"v": f, "l": f, "f": f} for f in bf]
    else:
        dd_opts.append({"g": "Library"})
        dd_opts += [{"v": n, "l": n, "f": n} for n, _ in CURATED_FONTS]
    opts_attr = html.escape(json.dumps(dd_opts))
    return f"""    <div class="sec-sub">
      <span class="label">Font</span>
      <button type="button" class="csel-trigger"
        data-sid="{sid}" data-handle="{handle}" data-prop="fontFamily"
        data-opts="{opts_attr}"
        onclick="openEditorDrop(this)">
        <span class="csel-val">— template default —</span>
        <span class="chev" style="flex:none;pointer-events:none">{_sym('ic-down', 13)}</span>
      </button>
    </div>"""


def _build_panel_controls(slots: list[dict], slide_id: str,
                          present_handles: set[str] | None = None,
                          brand_fonts: list[str] | None = None,
                          live_data: dict | None = None,
                          ai_providers: dict | None = None) -> str:
    """Generate HTML control groups for one slide's slots.

    Each control group div carries ``data-control-type`` (text/pill/image/svg/
    chrome) so the distinction is grep-verifiable. Image/asset slots are matched to
    the template by their stripped ``data-slot`` handle (see ``_slot_handle``); a
    slot whose handle is not in ``present_handles`` (when given) is skipped, so the
    panel never shows a control that targets a zone the DOM doesn't have.

    ``live_data`` (handle → live rendered value) seeds the Content textarea from
    the ACTUAL copy on the canvas (the run's persisted post data) instead of the
    instructions.md sample, so the panel matches what's rendered and what rebakes
    (audit #1/#9). Inline markup (``<mark>``/``<br>``) is shown verbatim as the
    editable source — the live iframe renders it as innerHTML and the bake renders
    it raw, so all three agree.

    ``ai_providers`` (studio-ai-edit) is the server-resolved ``{gpt, gemini}``
    presence map — image control groups get one "Edit with <provider>" button per
    AVAILABLE provider, next to Replace image. Absent key → no button (never a
    disabled one); no providers / static build → no AI section at all."""
    parts = []
    sid = slide_id
    for slot in slots:
        name = slot["name"]
        handle, is_asset = _slot_handle(name)
        if present_handles is not None and handle not in present_handles:
            continue
        stype = slot.get("type", "text")
        if is_asset:
            stype = "svg" if "SVG" in name.upper() else "image"
        bbox = slot.get("bbox") or {}
        sample = slot.get("sample") or ""
        # Seed the Content textarea from the LIVE rendered copy (the run's real post
        # data) when available, falling back to the instructions sample. This is what
        # the canvas shows and what `/apply` rebakes — so panel == canvas == PNG
        # (audit #1/#9). live_data is keyed by the stripped data-slot handle.
        live_text = None
        if live_data is not None and handle in live_data:
            lv = live_data.get(handle)
            if isinstance(lv, str):
                live_text = lv
        content_seed = live_text if live_text is not None else sample
        x = bbox.get("x", 0)
        y = bbox.get("y", 0)
        w = bbox.get("w", 30 if stype == "pill" else 100)
        h = bbox.get("h", 60)

        def content_sub(rows=2):
            return (
                f'    <div class="sec-sub">\n'
                f'      <span class="label">Content</span>\n'
                f'      <textarea class="content-area" rows="{rows}" '
                f'oninput="applyToSlide(\'{sid}\',\'{handle}\',\'text\',this.value)">{html.escape(content_seed)}</textarea>\n'
                f'    </div>'
            )

        def opacity_sub(default=100):
            return f"""    <div class="sec-sub">
      <span class="label">Opacity</span>
      <div class="opacity-row">
        <div class="slider" style="--p:{default}%"><input type="range" data-prop="opacityPct" min="0" max="100" value="{default}"
          oninput="applyToSlide('{sid}','{handle}','opacity',this.value/100); syncOpacity('{sid}','{handle}',this)"></div>
        <div class="pct"><input type="number" data-prop="opacityPct" value="{default}"
          oninput="applyToSlide('{sid}','{handle}','opacity',this.value/100); syncOpacity('{sid}','{handle}',this)"><span class="unit">%</span></div>
      </div>
    </div>"""

        def corner_sub(default=0):
            return f"""    <div class="sec-sub corner-field">
      <span class="label">Corner radius</span>
      <div class="field">
        {_sym('ic-corner', 14)}
        <input type="number" data-prop="radius" value="{default}"
          oninput="applyToSlide('{sid}','{handle}','radius',parseFloat(this.value))">
        <span class="unit">px</span>
      </div>
    </div>"""

        def fill_sub(prop, default, label="Fill"):
            # `default` is only the pre-selection placeholder — selectZone reseeds the
            # input from the zone's COMPUTED colour via data-prop (r5f F1b), so the
            # swatch shows the slide's real colour, not a hardcoded guess.
            hexval = default.lstrip("#").upper()
            return f"""    <div class="sec-sub">
      <span class="label">{label}</span>
      <div class="colorrow">
        <span class="swatch" style="background:{default}"><input type="color" value="{default}" data-prop="{prop}"
          oninput="applyToSlide('{sid}','{handle}','{prop}',this.value); syncHex(this)"></span>
        <div class="hex"><span class="hash">#</span><input value="{hexval}" maxlength="6"
          oninput="applyHex('{sid}','{handle}','{prop}',this)"></div>
      </div>
    </div>"""

        def header(badge_cls, icon_name, badge_label):
            return (
                f'    <div class="control-group-header">\n'
                f'      <span class="slot-badge {badge_cls}">{_icon(icon_name, 11)}{badge_label}</span>\n'
                f'      <strong>{html.escape(handle)}</strong>\n'
                f'    </div>'
            )

        if stype == "text":
            style_str = slot.get("style") or ""
            fs_match = re.search(r"(\d+(?:\.\d+)?)\s*cqw", style_str)
            default_fs = float(fs_match.group(1)) if fs_match else 5.0
            typography = f"""    <div class="sec-sub typography">
      <span class="sec-title">Typography</span>
{_font_select(sid, handle, brand_fonts)}
{_range_row(sid, handle, "fontSize", "Font size", 1, 72, 0.5, default_fs)}
{_range_row(sid, handle, "tilt", "Tilt", -45, 45, 1, 0)}
    </div>"""
            body = "\n".join([
                content_sub(2),
                f'    <span class="sec-title">Position &amp; Size</span>',
                _position_size_section(sid, handle, x, y, w),
                f'    <span class="sec-title">Appearance</span>',
                opacity_sub(),
                fill_sub("color", "#1b1b1b", "Fill (text color)"),
                typography,
            ])
            parts.append(
                f'\n  <div class="control-group" data-control-type="text" '
                f'data-slide="{sid}" data-slot="{handle}">\n'
                f'{header("slot-badge--text", "type", "TEXT")}\n{body}\n  </div>'
            )

        elif stype == "pill":
            # A real CALLOUT_PILL (template-conventions.md) is a coloured badge with
            # text — "pill, brand-accent fill, white text" — so it needs fill + text
            # colour, not just content + position (the old too-thin control).
            # r5f F1c: + Typography (font select / size), default parsed from the
            # slot's cqw style — same regex as the text branch. The fontSize lands on
            # the pill's inner text node (F1a innermost targeting), which declares
            # its own font-size, so a plain container rule would never win.
            pill_style = slot.get("style") or ""
            pill_fs_match = re.search(r"(\d+(?:\.\d+)?)\s*cqw", pill_style)
            pill_fs = float(pill_fs_match.group(1)) if pill_fs_match else 2.5
            pill_typography = f"""    <div class="sec-sub typography">
      <span class="sec-title">Typography</span>
{_font_select(sid, handle, brand_fonts)}
{_range_row(sid, handle, "fontSize", "Font size", 1, 72, 0.5, pill_fs)}
    </div>"""
            body = "\n".join([
                content_sub(1),
                f'    <span class="sec-title">Appearance</span>',
                fill_sub("bgColor", "#5B57D6", "Fill"),
                fill_sub("color", "#ffffff", "Text color"),
                opacity_sub(),
                pill_typography,
                f'    <span class="sec-title">Position &amp; Size</span>',
                _position_size_section(sid, handle, x, y, w),
            ])
            parts.append(
                f'\n  <div class="control-group" data-control-type="pill" '
                f'data-slide="{sid}" data-slot="{handle}">\n'
                f'{header("slot-badge--pill", "tag", "PILL")}\n{body}\n  </div>'
            )

        elif stype in ("image", "svg"):
            is_svg = stype == "svg"
            blocks = [
                f'    <span class="sec-title">Position &amp; Size</span>',
                _position_size_section(sid, handle, x, y, w, h),
                _range_row(sid, handle, "tilt", "Rotate", -180, 180, 1, 0),
                f'    <span class="sec-title">Appearance</span>',
                opacity_sub(),
            ]
            if is_svg:
                blocks.append(fill_sub("color", "#e2403a", "Color"))
            else:
                # Replace image (r5f F5): file picker → data URL → imgSrc tweak. The
                # new image occupies the SAME placeholder (geometry/object-fit kept);
                # the bake honors it via render_template's parity script.
                blocks.append(f"""    <div class="sec-sub">
      <span class="label">Image</span>
      <button type="button" class="replace-img-btn"
        onclick="pickReplaceImage('{sid}','{handle}')">
        {_icon("image", 13)}<span>Replace image&hellip;</span>
      </button>
    </div>""")
                # AI edit (studio-ai-edit): "Edit with GPT/Gemini" next to Replace
                # image — same imgSrc destination, AI-generated origin. The section
                # renders ONLY for providers the server resolved (presence booleans;
                # key values never reach this build). Empty string when none.
                ai_sub = _ai_edit_buttons(sid, handle, ai_providers)
                if ai_sub:
                    blocks.append(ai_sub)
                blocks.append(corner_sub(0))
                _scale_opts = html.escape(json.dumps([
                    {"v": "cover", "l": "cover", "f": ""},
                    {"v": "square", "l": "square", "f": ""},
                    {"v": "crop", "l": "crop", "f": ""},
                ]))
                blocks.append(f"""    <div class="sec-sub">
      <span class="label">Scale</span>
      <button type="button" class="csel-trigger"
        data-sid="{sid}" data-handle="{handle}" data-prop="scale"
        data-opts="{_scale_opts}"
        onclick="openEditorDrop(this)">
        <span class="csel-val">cover</span>
        <span class="chev" style="flex:none;pointer-events:none">{_sym('ic-down', 13)}</span>
      </button>
    </div>""")
                blocks.append(f"""    <details class="sec-sub stroke-sub">
      <summary><span class="sec-title">Stroke</span></summary>
      <div class="colorrow" style="margin-top:10px">
        <span class="swatch" style="background:#000"><input type="color" value="#000000"
          oninput="applyToSlide('{sid}','{handle}','strokeColor',this.value); syncHex(this)"></span>
        <div class="hex"><span class="hash">#</span><input value="000000" maxlength="6"
          oninput="applyHex('{sid}','{handle}','strokeColor',this)"></div>
      </div>
{_range_row(sid, handle, "strokeW", "Weight", 0, 24, 1, 0)}
    </details>""")
            badge_label = "SVG" if is_svg else "IMAGE"
            ctrl_type = "svg" if is_svg else "image"
            parts.append(
                f'\n  <div class="control-group" data-control-type="{ctrl_type}" '
                f'data-slide="{sid}" data-slot="{handle}">\n'
                f'{header("slot-badge--image", "image", badge_label)}\n'
                + "\n".join(blocks) + "\n  </div>"
            )

        elif stype == "shape":
            body = "\n".join([
                f'    <span class="sec-title">Appearance</span>',
                fill_sub("bgColor", "#f4f2ee", "Fill"),
                opacity_sub(),
                corner_sub(0),
                f'    <span class="sec-title">Position &amp; Size</span>',
                _position_size_section(sid, handle, x, y, w),
            ])
            parts.append(
                f'\n  <div class="control-group" data-control-type="shape" '
                f'data-slide="{sid}" data-slot="{handle}">\n'
                f'{header("slot-badge--shape", "layout", "SHAPE")}\n{body}\n  </div>'
            )

        elif stype == "chrome":
            parts.append(
                f'\n  <div class="control-group" data-control-type="chrome" '
                f'data-slide="{sid}" data-slot="{handle}">\n'
                f'{header("slot-badge--chrome", "layout", "CHROME")}\n'
                f'    <label class="toggle-label">\n'
                f'      <input type="checkbox" checked '
                f'onchange="applyToSlide(\'{sid}\',\'{handle}\',\'visible\',this.checked)">\n'
                f'      Visible (global toggle)\n'
                f'    </label>\n  </div>'
            )

    return "\n".join(parts)


def _build_layers_list(slots: list[dict], slide_id: str,
                       present_handles: set[str] | None = None,
                       order: list[str] | None = None) -> str:
    """Build the Canva-style layers list for one slide — one row per editable zone
    (drag handle + type icon + content preview + visibility eye). Rows are ordered by
    DOM stacking (``order``) then reversed, so the front-most layer sits at the top
    and the background sinks to the bottom. Clicking a row selects the zone (opens
    its inspector); dragging reorders z."""
    rows = []  # (handle, html)
    sid = slide_id
    for slot in slots:
        name = slot["name"]
        handle, is_asset = _slot_handle(name)
        if present_handles is not None and handle not in present_handles:
            continue
        stype = slot.get("type", "text")
        if is_asset:
            stype = "svg" if "SVG" in name.upper() else "image"
        sample = (slot.get("sample") or "").strip()
        if stype in ("image", "svg"):
            ico, preview = _icon("image", 13), html.escape(handle)
        elif stype in ("shape", "chrome"):
            ico, preview = _icon("layout", 13), html.escape(handle)
        elif stype == "pill":
            ico = _icon("tag", 13)
            preview = html.escape(sample[:42]) if sample else html.escape(handle)
        else:
            ico = _icon("type", 13)
            preview = html.escape(sample[:42]) if sample else html.escape(handle)
        rows.append((handle,
            f'  <div class="layer-row" draggable="true" data-slide="{sid}" data-handle="{handle}" '
            f'data-locked="0" onclick="selectZone(\'{sid}\',\'{handle}\')">'
            f'<span class="layer-grip" aria-hidden="true">&#8942;&#8942;</span>'
            f'<span class="layer-ico">{ico}</span>'
            f'<span class="layer-name">{preview}</span>'
            f'<span class="layer-actions">'
            f'<button type="button" class="actbtn actbtn--lk" data-on="0" aria-label="lock layer" '
            f'onclick="event.stopPropagation();toggleLock(\'{sid}\',\'{handle}\',this)">'
            f'<span class="lk-off">{_icon("unlock", 14)}</span><span class="lk-on">{_icon("lock", 14)}</span></button>'
            f'<button type="button" class="actbtn layer-eye" data-on="1" aria-label="toggle visibility" '
            f'onclick="event.stopPropagation();toggleVisible(\'{sid}\',\'{handle}\',this)">'
            f'<span class="eye-on">{_icon("eye", 14)}</span><span class="eye-off">{_icon("eye-off", 14)}</span></button>'
            # FASE 6 §3: no per-layer trash/delete affordance — hiding (the eye) is enough.
            f'</span>'
            f'</div>'
        ))
    if order:
        pos = {h: i for i, h in enumerate(order)}
        rows.sort(key=lambda hr: pos.get(hr[0], len(pos)))
    rows.reverse()  # front-most (last in DOM) first; background sinks to the bottom
    return "\n".join(html_ for _, html_ in rows)


def _build_fullai_layer_panel(slide_id: str) -> tuple[str, str]:
    """Layers row + inspector for a full-AI (flat) image slide.

    A full-AI image has no introspectable zones, but it must still APPEAR as a
    selectable layer (Addendum 5 Fix #2): one row carrying the magic-pencil
    "break into layers" affordance. Direct per-element editing stays gated behind
    decompose — selecting the row shows only a disclaimer + the same pencil. The
    handle is ``BACKGROUND`` to match the data-slot the layer-canvas synthesizes on
    decompose, so the layer identity is consistent before and after promotion.
    Returns ``(layers_html, controls_html)``.
    """
    sid = slide_id
    handle = "BACKGROUND"
    pencil_row = (
        f'<button type="button" class="actbtn layer-magic" aria-label="break into layers" '
        f'title="Break this AI image into editable layers" '
        f'onclick="event.stopPropagation();if(window.__studioBreakIntoLayers)'
        f'window.__studioBreakIntoLayers(\'{sid}\')">{_icon("wand", 14)}</button>'
    )
    layers_html = (
        f'  <div class="layer-row layer-fullai" draggable="false" data-slide="{sid}" '
        f'data-handle="{handle}" data-fullai="1" data-locked="0" '
        f'onclick="selectZone(\'{sid}\',\'{handle}\')">'
        f'<span class="layer-grip" aria-hidden="true">&#8942;&#8942;</span>'
        f'<span class="layer-ico">{_icon("image", 13)}</span>'
        f'<span class="layer-name">AI image</span>'
        f'<span class="layer-actions">{pencil_row}</span>'
        f'</div>'
    )
    controls_html = (
        f'  <div class="control-group control-fullai" data-control-type="image" '
        f'data-slot="{handle}">'
        f'<div class="fullai-note">'
        f'<div class="fullai-note-ico">{_icon("wand", 18)}</div>'
        f'<p>This image is fully AI-generated, so it edits as a single layer. '
        f'To move or restyle parts of it, <strong>break it into layers</strong> first.</p>'
        f'</div>'
        f'<button type="button" class="magic-break-btn" '
        f'onclick="if(window.__studioBreakIntoLayers)window.__studioBreakIntoLayers(\'{sid}\')">'
        f'{_icon("wand", 15)}<span>Break into layers</span></button>'
        f'</div>'
    )
    return layers_html, controls_html


def _texture_section(slide_id: str, textures: list[dict]) -> str:
    """Per-slide post-production Texture section (Addendum 5): overlay picker +
    blend-mode select + intensity slider. Per-slide (not global) — each control calls
    ``applyTexture(sid)`` which writes the reserved ``__texture`` tweak + live overlay.
    Returns "" when no texture assets are vendored (purely additive)."""
    if not textures:
        return ""
    sid = slide_id
    tex_opts = ['<option value="">&mdash; none &mdash;</option>']
    tex_opts += [
        f'<option value="{t["name"]}">{html.escape(t["label"])}</option>' for t in textures
    ]
    blends = [
        ("multiply", "Multiply"), ("overlay", "Overlay"), ("screen", "Screen"),
        ("soft-light", "Soft light"), ("darken", "Darken"), ("lighten", "Lighten"),
        ("normal", "Normal"),
    ]
    blend_opts = [f'<option value="{v}">{lbl}</option>' for v, lbl in blends]
    return (
        f'<div class="section texture-section" data-slide="{sid}">'
        f'<div class="sec-head"><span class="sec-title">Texture</span></div>'
        f'<div class="sec-sub"><span class="label">Overlay</span>'
        f'<div class="select"><select class="tex-name" onchange="applyTexture(\'{sid}\')">'
        f'{"".join(tex_opts)}</select><span class="chev">{_sym("ic-down", 13)}</span></div></div>'
        f'<div class="sec-sub"><span class="label">Blend</span>'
        f'<div class="select"><select class="tex-blend" onchange="applyTexture(\'{sid}\')">'
        f'{"".join(blend_opts)}</select><span class="chev">{_sym("ic-down", 13)}</span></div></div>'
        f'<div class="ctrl-row"><span class="ctrl-name">Intensity</span>'
        f'<input type="range" class="tex-intensity" min="0" max="100" value="55" '
        f'oninput="applyTexture(\'{sid}\'); this.nextElementSibling.textContent=this.value">'
        f'<span class="range-val">55</span></div>'
        f'</div>'
    )


def _slot_bboxes(slots: list[dict], present_handles: set[str] | None) -> list[dict]:
    """Per-slide ``[{handle, x, y, w, h}]`` (canvas %) for the editable zones — fed to
    the comment module so a dropped pin resolves to the nearest zone (Stage B). Mirrors
    the panel's handle/skip rules so the JS sees the same set of zones."""
    out: list[dict] = []
    for slot in slots:
        handle, _is_asset = _slot_handle(slot["name"])
        if present_handles is not None and handle not in present_handles:
            continue
        bb = slot.get("bbox") or {}
        if not bb:
            continue
        out.append({
            "handle": handle,
            "x": float(bb.get("x", 0)), "y": float(bb.get("y", 0)),
            "w": float(bb.get("w", 0)), "h": float(bb.get("h", 0)),
        })
    return out


def _nearest_zone(bboxes: list[dict], x: float, y: float) -> str | None:
    """Resolve canvas-% point ``(x, y)`` to the nearest editable zone handle: the
    SMALLEST bbox that contains the point, else the zone whose centre is closest.
    Returns None when there are no zones. The comment module mirrors this in JS so a
    pin carries a semantic anchor (``zone``) Claude can act on without vision."""
    contained = [
        b for b in bboxes
        if b["x"] <= x <= b["x"] + b["w"] and b["y"] <= y <= b["y"] + b["h"]
    ]
    if contained:
        return min(contained, key=lambda b: (b["w"] * b["h"]) or 1e9)["handle"]
    if not bboxes:
        return None

    def _d(b: dict) -> float:
        cx, cy = b["x"] + b["w"] / 2, b["y"] + b["h"] / 2
        return (cx - x) ** 2 + (cy - y) ** 2

    return min(bboxes, key=_d)["handle"]


# ──────────────────────────────────────────────────────────────
# JS block (embedded via sentinel-replace to avoid {} clashes)
# Uses __TWEAKS_INIT_JSON__ sentinel for the initial state blob.
# ──────────────────────────────────────────────────────────────
_EDITOR_JS = r"""<script>
(function() {
  // ── State ─────────────────────────────────────────────────
  var tweaksState = __TWEAKS_INIT_JSON__;
  var SLOT_BBOXES = __SLOT_BBOXES_JSON__;        // {slide: [{handle,x,y,w,h}]} canvas %
  // Content Studio's Konva canvas overlay (served only by content_studio.py) reads
  // these bboxes to draw selectable/transformable rects over the live slide. Exposed
  // read-only — the static editor never touches it (no-op there).
  window.__SLOT_BBOXES = SLOT_BBOXES;
  var INITIAL_COMMENTS = __INITIAL_COMMENTS_JSON__;  // {slide: [{id,xPct,yPct,zone,text}]}
  // ONLY tweaks loaded from a saved tweaks.json get re-applied to the live slides on
  // open (import/resume) — never the computed defaults, which would force the
  // template off its natural rendering and break a fresh run's parity.
  var IMPORTED_TWEAKS = __IMPORTED_TWEAKS_JSON__;
  // Template's natural per-zone state — the export diffs against this so ONLY real
  // edits ship (an unchanged default must NOT be applied, or the rebake drifts from
  // what the editor showed).
  var DEFAULTS = __DEFAULTS_JSON__;

  // ── DOM refs ──────────────────────────────────────────────
  function getFrame(slideId) {
    return document.getElementById('frame-' + slideId);
  }

  function getEl(slideId, slotName) {
    var iframe = getFrame(slideId);
    if (!iframe) return null;
    var doc = iframe.contentDocument || iframe.contentWindow.document;
    if (!doc) return null;
    // Reflect the CURRENT state, not a stale early read: an applyToSlide that fires while
    // the iframe srcdoc is still loading (e.g. replaying saved tweaks) would otherwise
    // flip the "no data-slot handles" banner on and never turn it off. Toggle it both
    // ways so the banner self-corrects once the slots exist.
    var hasSlots = doc.querySelectorAll('[data-slot]').length > 0;
    var banner = document.getElementById('no-slot-banner-' + slideId);
    if (banner) banner.style.display = hasSlots ? 'none' : 'block';
    if (!hasSlots) return null;
    return doc.querySelector('[data-slot="' + slotName + '"]');
  }

  function slotState(slideId, slotName) {
    if (!tweaksState[slideId]) tweaksState[slideId] = {};
    if (!tweaksState[slideId][slotName]) tweaksState[slideId][slotName] = {};
    return tweaksState[slideId][slotName];
  }

  // ── Text-target resolution (r5f F1a) ──────────────────────
  // Text-ish props (text/fontSize/fontFamily/color) must land on the TEXT, not the
  // zone's box: a container slot (e.g. a callout pill carrying the handle while a
  // styled .bottom-pill-text child holds the type) would otherwise lose its children
  // to one innerHTML write (font falls to browser default, the arrow dies).
  var TEXTISH_PROPS = { text: 1, fontSize: 1, fontFamily: 1, color: 1 };
  // Inline-markup tags are CONTENT (the editable <mark>/<br> the textarea shows
  // verbatim) — never descend through them. Anything else is structure.
  var INLINE_MARKUP = { MARK:1, BR:1, B:1, I:1, EM:1, STRONG:1, SPAN:1, A:1,
                        SMALL:1, SUP:1, SUB:1, U:1, S:1, WBR:1 };

  // Innermost occurrence of the handle: legacy emits may carry the SAME data-slot
  // on a container AND a descendant — querySelectorAll is document-order, so the
  // last node is the innermost of a nested pair.
  function getInnermostEl(slideId, slotName) {
    var iframe = getFrame(slideId);
    if (!iframe) return null;
    var doc = iframe.contentDocument || iframe.contentWindow.document;
    if (!doc) return null;
    var els = doc.querySelectorAll('[data-slot="' + slotName + '"]');
    return els.length ? els[els.length - 1] : null;
  }

  // Deepest text-bearing descendant: walk down through STRUCTURAL children (divs
  // etc.) into the first one with real text; stop when the children are only
  // inline markup (innerHTML belongs at that level) or there is no text below.
  //
  // r5f-followups Fix 2 — one exception to "stop at inline markup": a slot whose
  // text is wrapped in a SINGLE inline child (e.g. .callout-pill > span.pill-text)
  // where THAT child declares its own font-size. Styling the container then loses
  // to the child's own rule, so the slider/colour is a no-op. Descend into the
  // lone inline wrapper that carries the text — but ONLY when it is the sole child
  // (mixed inline markup like `<mark>a</mark> b <b>c</b>` stays at the container so
  // an innerHTML text edit keeps it verbatim; a lone empty <br> has no text to
  // style and is skipped).
  function textTarget(el) {
    var cur = el, guard = 0;
    while (cur && guard++ < 20) {
      var kids = cur.children || [], i, structural = false, next = null;
      for (i = 0; i < kids.length; i++) {
        if (!INLINE_MARKUP[kids[i].tagName]) { structural = true; break; }
      }
      if (!structural) {
        // No structural child: descend into a lone inline text-bearing wrapper
        // (the pill-text case); otherwise this IS the text node — stop here.
        if (kids.length === 1 && INLINE_MARKUP[kids[0].tagName]
            && kids[0].textContent && kids[0].textContent.replace(/\s+/g, '')) {
          cur = kids[0];
          continue;
        }
        break;
      }
      for (i = 0; i < kids.length; i++) {
        var k = kids[i];
        if (!INLINE_MARKUP[k.tagName] && k.textContent && k.textContent.replace(/\s+/g, '')) {
          next = k; break;
        }
      }
      if (!next) break;
      cur = next;
    }
    return cur;
  }

  // Make an element a positioning/stacking context WITHOUT disturbing its layout:
  // only promote a *static* element to relative (an already-absolute background
  // stays absolute, so moving/reordering it never yanks it on top of everything).
  function ensurePositioned(el) {
    var win = el.ownerDocument.defaultView || window;
    if (win.getComputedStyle(el).position === 'static') el.style.position = 'relative';
  }

  // ── Apply per-slot change to the live iframe ──────────────
  function applyToSlide(slideId, slotName, prop, value) {
    var el = getEl(slideId, slotName);
    if (!el) return;
    var st = slotState(slideId, slotName);

    // Text-ish props target the innermost occurrence's deepest text-bearing
    // descendant (r5f F1a); geometry/box props keep the outermost element. The
    // bake mirrors this targeting (render_template._build_parity_script).
    var tEl = el;
    if (TEXTISH_PROPS[prop]) {
      tEl = textTarget(getInnermostEl(slideId, slotName) || el);
    }

    if (prop === 'text') {
      tEl.innerHTML = value;                      // editor trusts its own input
      // Re-fit after a live text edit so the canvas matches the bake (which always
      // autosizes the FINAL filled DOM). The autosize sets an !important px size;
      // clear it first so the slot re-measures from its authored cqw size, then
      // re-run the in-iframe autosize. No-op for slots that still fit.
      try {
        tEl.style.removeProperty('font-size');
        var _w = (getFrame(slideId) || {}).contentWindow;
        if (_w && _w.__autosizeRun) _w.__autosizeRun();
      } catch (e) {}
    } else if (prop === 'fontSize') {
      // A user-chosen size is authoritative — beat the autosize's !important px.
      tEl.style.setProperty('font-size', value + 'cqw', 'important');
    } else if (prop === 'fontFamily') {
      // empty = revert to the template's own font; otherwise the chosen family
      // (loaded via the curated Google Fonts <link>). Matches the bake's css_font_value.
      tEl.style.fontFamily = value ? ('"' + value + '"') : '';
    } else if (prop === 'opacity') {
      el.style.opacity = value;
    } else if (prop === 'bgColor') {
      el.style.background = value;
    } else if (prop === 'x' || prop === 'y') {
      // Position is a translate DELTA (slide %), applied via the CSS `translate`
      // property — it moves the element regardless of its positioning context, so a
      // `relative` text zone nested in an auto-height card moves on BOTH axes (the old
      // top:% computed to 0 there). `translate` composes natively with the `rotate`
      // property (tilt) and with any template `transform`. The bake emits the same
      // `translate:` so preview == PNG (the element's natural position is identical in
      // both → natural+delta matches). 1080x1350 = the brand carousel canvas.
      st[prop] = value;
      var _dx = (+st.x || 0) / 100 * 1080, _dy = (+st.y || 0) / 100 * 1350;
      el.style.translate = _dx + 'px ' + _dy + 'px';
    } else if (prop === 'w') {
      el.style.width = value + '%';
    } else if (prop === 'tilt') {
      el.style.rotate = value + 'deg';            // composes with existing transform
    } else if (prop === 'scale') {
      var fit = value === 'crop' ? 'none' : 'cover';
      var ar  = value === 'square' ? '1 / 1' : '';
      el.style.objectFit = fit; el.style.aspectRatio = ar;
      var sImg = el.querySelector('img');
      if (sImg) { sImg.style.objectFit = fit; sImg.style.aspectRatio = ar; }
    } else if (prop === 'color') {
      // text colour (on the text target) + SVG recolour on the zone itself
      // (currentColor + explicit child stroke/fill).
      tEl.style.color = value;
      el.querySelectorAll('svg *').forEach(function(s) {
        var stk = s.getAttribute('stroke'); if (stk && stk !== 'none') s.style.stroke = value;
        var fl = s.getAttribute('fill');    if (fl && fl !== 'none') s.style.fill = value;
      });
    } else if (prop === 'imgSrc') {
      // Replace image (r5f F5): swap the slot's <img src> — or the zone's
      // background-image when it has no <img> — keeping geometry/object-fit
      // untouched. Persisted in tweaks; the bake mirrors it (parity script).
      var rImg = (el.tagName === 'IMG') ? el : el.querySelector('img');
      if (rImg) {
        rImg.src = value;
        rImg.removeAttribute('srcset');
        rImg.removeAttribute('data-ph');   // no longer the "missing image" placeholder
      } else {
        el.style.backgroundImage = 'url("' + value + '")';
        if (!el.style.backgroundSize) el.style.backgroundSize = 'cover';
        if (!el.style.backgroundPosition) el.style.backgroundPosition = 'center';
      }
    } else if (prop === 'strokeColor' || prop === 'strokeW') {
      st[prop] = value;                           // record first, then compose border
      var sw = (st.strokeW != null ? st.strokeW : 0);
      var sc = (st.strokeColor || '#000000');
      el.style.boxSizing = 'border-box';
      el.style.border = sw > 0 ? (sw + 'px solid ' + sc) : '';
    } else if (prop === 'radius') {
      el.style.borderRadius = value + 'px';
      el.style.overflow = 'hidden';               // clip inner <img> to the radius
    } else if (prop === 'z') {
      ensurePositioned(el);
      el.style.zIndex = value;
    } else if (prop === 'visible') {
      el.style.display = value ? '' : 'none';
    } else if (prop === 'removed') {
      // Remove asset (§4, Case B): a real template zone can't be deleted from the
      // tweak object (template.html still ships it), so we flag removed:true and
      // hide it live — the bake honors the flag with display:none, so it round-trips.
      el.style.display = value ? 'none' : '';
    }

    st[prop] = value;
  }

  // ── Apply global control to ALL iframes ───────────────────
  function applyGlobal(cssVar, value) {
    var frames = document.querySelectorAll('iframe[id^="frame-"]');
    frames.forEach(function(iframe) {
      var doc = iframe.contentDocument || iframe.contentWindow.document;
      if (doc && doc.documentElement) {
        doc.documentElement.style.setProperty(cssVar, value);
      }
    });
    if (!tweaksState.global) tweaksState.global = {};
    // Map css var name to tweaksState.global key. (The old global display-font
    // control was removed in Stage A — font editing is per-layer now.)
    if (cssVar === '--brand-accent') tweaksState.global.accent = value;
    else tweaksState.global[cssVar] = value;
  }

  // ── Post-production texture overlay (Addendum 5) ──────────
  // A per-slide overlay (picker + blend mode + intensity) composited over EVERYTHING
  // on the slide. Stored under the reserved tweaks key __texture = {tex,blend,intensity}
  // and re-applied at bake by render_template._materialize_texture from the SAME data
  // URI/blend/intensity, so the live preview equals the baked PNG (RNDR-04).
  var TEXTURES = window.__TEXTURES || {};
  function texOverlayStyle(uri, blend, intensity) {
    return 'position:absolute;inset:0;background-image:url("' + uri + '");' +
      'background-repeat:repeat;mix-blend-mode:' + blend + ';opacity:' + intensity +
      ';pointer-events:none;z-index:99999';
  }
  function texTarget(slideId) {
    // Prefer the iframe .slide (templated / promoted full-AI) so preview == bake;
    // fall back to the flat full-AI viewer.
    var f = getFrame(slideId);
    if (f) {
      try {
        var d = f.contentDocument || f.contentWindow.document;
        if (d) return { root: d.querySelector('.slide') || d.body, doc: d };
      } catch (e) {}
    }
    var v = document.querySelector('.slide-viewer[data-slide="' + slideId + '"]');
    return v ? { root: v, doc: document } : null;
  }
  function renderTexOverlay(slideId, tex) {
    var t = texTarget(slideId);
    if (!t || !t.root) return;
    var old = t.root.querySelector('[data-texture="1"]');
    if (!tex || !tex.tex) { if (old) old.remove(); return; }
    var ov = old || t.doc.createElement('div');
    ov.setAttribute('data-texture', '1');
    ov.setAttribute('style', texOverlayStyle(
      tex.tex, tex.blend || 'multiply', tex.intensity != null ? tex.intensity : 1));
    if (!old) {
      var win = t.root.ownerDocument.defaultView || window;
      if (win.getComputedStyle(t.root).position === 'static') t.root.style.position = 'relative';
      t.root.appendChild(ov);
    }
  }
  // FASE 5: the texture control lives in the GLOBAL topbar (studio.js), not a per-slide
  // panel. These are the parameterized entry points it drives. __setTexture writes the
  // active slide's reserved __texture tweak (preserving the per-slide data model + bake
  // parity) and applies the live overlay; __getTexture reflects the current value back
  // so the topbar dropdown can show the active slide's state as you swipe.
  function setTexture(slideId, name, blend, intensity) {
    if (!slideId) return;
    if (!tweaksState[slideId]) tweaksState[slideId] = {};
    if (!name || !TEXTURES[name]) {        // "none" → drop the overlay
      delete tweaksState[slideId].__texture;
      renderTexOverlay(slideId, null);
      return;
    }
    var tex = {
      tex: TEXTURES[name].uri,
      blend: blend || 'multiply',
      intensity: intensity != null ? intensity : 0.55,
      name: name,
    };
    tweaksState[slideId].__texture = tex;  // exported/applied as-is by diffTweaks
    renderTexOverlay(slideId, tex);
  }
  function getTexture(slideId) {
    var t = slideId && tweaksState[slideId] && tweaksState[slideId].__texture;
    return t ? { name: t.name || '', blend: t.blend || 'multiply',
                 intensity: t.intensity != null ? t.intensity : 0.55 } : null;
  }
  window.__setTexture = setTexture;
  window.__getTexture = getTexture;
  window.__textureNames = Object.keys(TEXTURES);
  // Resume: re-apply the live overlay for any imported __texture (iframes load async).
  function bootTextures() {
    Object.keys(tweaksState).forEach(function (sid) {
      if (sid === 'global') return;
      var tex = tweaksState[sid] && tweaksState[sid].__texture;
      if (tex && tex.tex) renderTexOverlay(sid, tex);
    });
  }
  window.addEventListener('load', function () { setTimeout(bootTextures, 400); });

  // ── Brand-palette swatch: GLOBAL brand accent only ───────
  // Decoupled from per-layer fill (two scopes, PRD): clicking a brand-palette swatch
  // sets the brand-wide accent var and NEVER rewrites the selected layer's fill;
  // conversely, editing a layer's Fill in the inspector never changes the palette.
  function applySwatch(hex) { applyGlobal('--brand-accent', hex); }
  window.applySwatch = applySwatch;

  // Masthead is NOT synthetically injected (PM decision 2026-06-04): the editor
  // only edits a masthead that the template actually ships (its real masthead
  // slot shows up as a layer via the normal slot introspection). The old global
  // "Masthead bar" toggle that injected a placeholder bar conflicted with
  // templates that own their top chrome, so it was removed.

  // ── Download a JSON blob ──────────────────────────────────
  function downloadJSON(obj, filename) {
    var blob = new Blob([JSON.stringify(obj, null, 2)], {type: 'application/json'});
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url; a.download = filename;
    document.body.appendChild(a); a.click(); document.body.removeChild(a);
    setTimeout(function(){ URL.revokeObjectURL(url); }, 4000);
  }

  // ── Diff tweaksState vs DEFAULTS → only the user's real edits ──
  // Applying an unchanged default (e.g. fontSize=5) would force the template off its
  // natural rendering and break editor==rebake parity, so the export carries ONLY
  // props the user actually changed (additive — empty when nothing was edited).
  function diffTweaks() {
    var out = {};
    var g = {};
    if (tweaksState.global) Object.keys(tweaksState.global).forEach(function(k) {
      var v = tweaksState.global[k];
      if (v !== '' && v != null && v !== false) g[k] = v;
    });
    if (Object.keys(g).length) out.global = g;
    Object.keys(tweaksState).forEach(function(sid) {
      if (sid === 'global') return;
      var zones = tweaksState[sid] || {}, defz = DEFAULTS[sid] || {}, zout = {};
      Object.keys(zones).forEach(function(h) {
        var props = zones[h]; if (!props || typeof props !== 'object') return;
        var dp = defz[h] || {}, pout = {};
        Object.keys(props).forEach(function(p) {
          if (JSON.stringify(props[p]) !== JSON.stringify(dp[p])) pout[p] = props[p];
        });
        if (Object.keys(pout).length) zout[h] = pout;
      });
      if (Object.keys(zout).length) out[sid] = zout;
    });
    return out;
  }

  // ── Export tweaks.json (+ comments.json) ──────────────────
  // tweaks.json drives the rebake; comments.json is the anchored annotations Claude
  // reads (slide + zone + text). Pins are NEVER inside tweaksState, so the rebake
  // never sees them. tweaks.json is also copied to the clipboard (paste-back path).
  // FASE 5: edits are now LIVE + saved server-side (studio.js → /save, implicit bake on
  // Download/Publish), so the stale "export changes (tweaks.json) to paste into Claude"
  // round-trip is gone. What still adds value is the COMMENTS round-trip — slide-anchored
  // notes Claude can act on — so this exports comments.json only.
  function exportComments() {
    var comments = (window.__getComments && window.__getComments()) || {};
    var nComments = Object.keys(comments).reduce(function(n, s) { return n + (comments[s] || []).length; }, 0);
    var note = document.getElementById('export-note');
    if (!nComments) { if (note) note.textContent = 'No comments yet — click a slide to drop a note first.'; return; }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(JSON.stringify(comments, null, 2)).catch(function(){});
    }
    downloadJSON(comments, 'comments.json');
    if (note) note.textContent = 'Downloaded comments.json (' + nComments + ' note' +
      (nComments > 1 ? 's' : '') + ') — drop it into Claude. (also copied to clipboard)';
  }

  // (PNG download removed — the editor is 100% static HTML and can't run the bake
  // engine; rasterizing live cqw/CDN-font slides in-browser wouldn't match the final
  // PNG. Edited PNGs come from the apply-back rebake: export the changes below, hand
  // them to Claude, and render_template --tweaks regenerates the slides pixel-perfect.)

  // ── Expose to inline event handlers ──────────────────────
  window.applyToSlide = applyToSlide;
  window.applyGlobal = applyGlobal;
  window.exportComments = exportComments;
  // The edited caption (FASE 6 #5) — studio.js persists it to caption.md, which is the
  // Zernio POST `content`. innerText preserves the user's line breaks.
  window.__getCaption = function () {
    var c = document.getElementById('li-caption');
    return c ? c.innerText.replace(/ /g, ' ').replace(/\s+$/,'') : '';
  };
  // Content Studio (local-server) reads the live tweaks/comments without forcing a
  // file download — the server shim (studio.js) POSTs these to /save and /apply.
  // No-op when the editor is opened as a plain static file. __getComments already
  // exists (set by the comment-pin module); __getTweaks mirrors the export diff.
  window.__getTweaks = diffTweaks;

  // ── Selection chip: reflect the selected layer's type + name ──
  // The mockup drives section/chip switching with a CSS :has(radio:checked) hack;
  // the real editor keeps it JS-driven against the live slide DOM (PRD addendum).
  var CHIP_LABEL = { text: 'Text', pill: 'Pill', image: 'Image', svg: 'SVG icon',
                     shape: 'Shape', chrome: 'Chrome', bg: 'Background' };
  function updateSelChip(slideId, handle, ctype) {
    var panel = document.querySelector('.slide-panel[data-slide="' + slideId + '"]');
    if (!panel) return;
    var chip = panel.querySelector('.selbar');
    if (!chip) return;
    chip.style.display = 'flex';
    var nm = chip.querySelector('.sel-name'); if (nm) nm.textContent = handle;
    var sub = chip.querySelector('.sel-sub'); if (sub) sub.textContent = (CHIP_LABEL[ctype] || ctype);
  }

  // ── Fill-control seeding (r5f F1b) ────────────────────────
  // The inspector's Fill / Text-color swatches were generated with HARDCODED hex
  // defaults (#5B57D6 / #1b1b1b / …) — they showed the panel's guess, not the
  // slide's real colour. On selection, read the zone's computed colour and seed
  // the inputs — unless the user already tweaked that prop (user wins). Gradients
  // and transparent backgrounds are skipped (no plain colour to show).
  function rgbToHex(raw) {
    var m = /^rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*([\d.]+)\s*)?\)$/.exec(raw || '');
    if (!m) return null;                                  // not a plain colour
    if (m[4] != null && parseFloat(m[4]) < 1) return null; // transparent-ish → skip
    function h(n) { var s = (+n).toString(16); return s.length === 1 ? '0' + s : s; }
    return '#' + h(m[1]) + h(m[2]) + h(m[3]);
  }
  function seedFillControls(slideId, handle, group) {
    if (!group) return;
    var st = (tweaksState[slideId] || {})[handle] || {};
    group.querySelectorAll('.colorrow input[type="color"][data-prop]').forEach(function(ci) {
      var prop = ci.getAttribute('data-prop');
      if (prop !== 'bgColor' && prop !== 'color') return;
      if (st[prop] != null && st[prop] !== '') return;    // a user tweak wins
      var el = getEl(slideId, handle);
      if (!el) return;
      if (prop === 'color') el = textTarget(getInnermostEl(slideId, handle) || el);
      var win = el.ownerDocument.defaultView || window;
      var cs = win.getComputedStyle(el);
      // bgColor: skip when a background-image/gradient paints the zone — the
      // computed backgroundColor underneath is not what the user sees.
      if (prop === 'bgColor' && cs.backgroundImage && cs.backgroundImage !== 'none') return;
      var hex = rgbToHex(prop === 'bgColor' ? cs.backgroundColor : cs.color);
      if (!hex) return;
      ci.value = hex;
      syncHex(ci);
    });
  }

  // ── Selection: click a layer -> show ONLY its inspector sections ──
  // The editor NEVER draws anything on the slide itself (selection is panel-only).
  var selected = {};  // slideId -> handle
  function selectZone(slideId, handle) {
    var panel = document.querySelector('.slide-panel[data-slide="' + slideId + '"]');
    var row = panel && panel.querySelector('.layer-row[data-handle="' + handle + '"]');
    if (row && row.getAttribute('data-locked') === '1') return;  // locked = not selectable
    selected[slideId] = handle;
    var ctype = 'text';
    if (panel) {
      panel.querySelectorAll('.inspector .control-group').forEach(function(g) {
        var on = g.getAttribute('data-slot') === handle;
        g.style.display = on ? 'block' : 'none';
        if (on) {
          ctype = g.getAttribute('data-control-type') || 'text';
          seedFillControls(slideId, handle, g);   // r5f F1b — live colour seeding
        }
      });
      panel.querySelectorAll('.layer-row').forEach(function(r) {
        r.classList.toggle('sel', r.dataset.handle === handle);
      });
      var hint = panel.querySelector('.inspector-hint');
      if (hint) hint.style.display = 'none';
    }
    updateSelChip(slideId, handle, ctype);
    // Notify the Konva canvas overlay so panel-click selection highlights the rect
    // (bidirectional sync). The overlay guards against echo loops on its side.
    if (window.__onSelect) window.__onSelect(slideId, handle, ctype);
  }
  window.selectZone = selectZone;

  // ── Layer visibility (eye) ────────────────────────────────
  function toggleVisible(slideId, handle, btn) {
    var on = btn.getAttribute('data-on') !== '0';
    on = !on;
    btn.setAttribute('data-on', on ? '1' : '0');
    btn.classList.toggle('off', !on);
    applyToSlide(slideId, handle, 'visible', on);
  }
  window.toggleVisible = toggleVisible;

  // ── Per-layer lock (new in v2) ────────────────────────────
  // Locked = not selectable + its inspector inputs disabled. Persisted in
  // tweaksState.locked (render_template ignores unknown keys, so the rebake is
  // unaffected). Eye visibility already existed; lock is the new sibling control.
  function toggleLock(slideId, handle, btn) {
    var locked = btn.getAttribute('data-on') !== '1';  // toggle
    btn.setAttribute('data-on', locked ? '1' : '0');
    var st = slotState(slideId, handle);
    st.locked = locked;
    var panel = document.querySelector('.slide-panel[data-slide="' + slideId + '"]');
    if (!panel) return;
    var row = panel.querySelector('.layer-row[data-handle="' + handle + '"]');
    if (row) { row.setAttribute('data-locked', locked ? '1' : '0'); row.classList.toggle('locked', locked); }
    var group = panel.querySelector('.inspector .control-group[data-slot="' + handle + '"]');
    if (group) {
      group.classList.toggle('locked', locked);
      group.querySelectorAll('input,select,textarea,button.pad-btn').forEach(function(el) {
        el.disabled = locked;
      });
    }
    if (locked && selected[slideId] === handle) {  // deselect a freshly-locked layer
      if (group) group.style.display = 'none';
      if (row) row.classList.remove('sel');
    }
  }
  window.toggleLock = toggleLock;

  // ── Remove a layer / zone (§4) ────────────────────────────
  // Two cases:
  //  A) LAYER_NN asset (decomposed/added) → HARD delete: the tweak entry, the live
  //     <img> node, the Layers row, and the __SLOT_BBOXES entry. Because
  //     _materialize_layers only injects layers PRESENT with an img, a deleted entry
  //     is simply never injected at bake — clean omission, no flag, round-trips.
  //  B) Template zone (a real data-slot in template.html) → can't be deleted from
  //     the tweak object (the element is authored in), so flag removed:true (the
  //     bake honors it with display:none) + hide live + grey the row.
  function removeLayer(slideId, handle) {
    var isAsset = /^LAYER_\d+$/.test(handle);
    var panel = document.querySelector('.slide-panel[data-slide="' + slideId + '"]');
    var row = panel && panel.querySelector('.layer-row[data-handle="' + handle + '"]');
    if (isAsset) {
      // live <img> node
      var el = getEl(slideId, handle);
      if (el && el.parentNode) el.parentNode.removeChild(el);
      // tweak entry
      if (tweaksState[slideId]) delete tweaksState[slideId][handle];
      // __SLOT_BBOXES entry
      if (window.__SLOT_BBOXES && window.__SLOT_BBOXES[slideId]) {
        window.__SLOT_BBOXES[slideId] = window.__SLOT_BBOXES[slideId].filter(
          function (b) { return b.handle !== handle; });
      }
      // Layers row + inspector group
      if (row && row.parentNode) row.parentNode.removeChild(row);
      var grp = panel && panel.querySelector('.inspector .control-group[data-slot="' + handle + '"]');
      if (grp && grp.parentNode) grp.parentNode.removeChild(grp);
      if (selected[slideId] === handle) selected[slideId] = null;
    } else {
      // Case B — flag + hide + grey (keep the row so it can be restored).
      applyToSlide(slideId, handle, 'removed', true);
      if (row) {
        row.classList.add('removed');
        row.style.opacity = '0.45';
        row.setAttribute('data-removed', '1');
      }
    }
    if (window.__studioCanvas) window.__studioCanvas.rebuild();
  }
  window.removeLayer = removeLayer;

  // ── Nudge step (1 / 8 / 24 px) ────────────────────────────
  var nudgeStep = 1;   // px; shared across the active layer's pad
  function setStep(px) { nudgeStep = px; }
  window.setStep = setStep;

  // ── Nudge: arrow buttons move x/y by the active px step ───
  // Positions stay in % (parity with the rebake's left/top%); the px step is
  // converted against the 1080x1350 slide so the nudge feels pixel-accurate.
  var SLIDE_W = 1080, SLIDE_H = 1350;
  function nudge(slideId, handle, axis, dir) {
    var st = slotState(slideId, handle);
    var cur = (st[axis] != null) ? parseFloat(st[axis]) : 0;
    var base = axis === 'x' ? SLIDE_W : SLIDE_H;
    var deltaPct = (nudgeStep / base) * 100 * dir;
    var next = Math.round(Math.max(0, Math.min(100, cur + deltaPct)) * 100) / 100;
    applyToSlide(slideId, handle, axis, next);
    var panel = document.querySelector('.slide-panel[data-slide="' + slideId + '"]');
    if (panel) {
      var inp = panel.querySelector('.control-group[data-slot="' + handle + '"] input[data-prop="' + axis + '"]');
      if (inp) inp.value = next;
    }
  }
  window.nudge = nudge;

  // ── Opacity slider <-> % field sync (0..100 UI, 0..1 engine) ──
  function syncOpacity(slideId, handle, src) {
    var v = Math.max(0, Math.min(100, parseFloat(src.value) || 0));
    var panel = document.querySelector('.slide-panel[data-slide="' + slideId + '"]');
    var group = panel && panel.querySelector('.control-group[data-slot="' + handle + '"]');
    if (!group) return;
    group.querySelectorAll('input[data-prop="opacityPct"]').forEach(function(el) {
      if (el !== src) el.value = v;
    });
    var slider = group.querySelector('.slider');
    if (slider) slider.style.setProperty('--p', v + '%');
  }
  window.syncOpacity = syncOpacity;

  // ── Fill swatch <-> hex field sync ────────────────────────
  function syncHex(colorInput) {
    var row = colorInput.closest('.colorrow');
    if (!row) return;
    row.querySelector('.swatch').style.background = colorInput.value;
    var hx = row.querySelector('.hex input');
    if (hx) hx.value = colorInput.value.replace('#', '').toUpperCase();
  }
  window.syncHex = syncHex;
  function applyHex(slideId, handle, prop, hexInput) {
    var v = hexInput.value.replace(/[^0-9a-fA-F]/g, '').slice(0, 6);
    if (v.length !== 3 && v.length !== 6) return;   // wait for a complete hex
    var color = '#' + v;
    applyToSlide(slideId, handle, prop, color);
    var row = hexInput.closest('.colorrow');
    if (row) {
      row.querySelector('.swatch').style.background = color;
      var ci = row.querySelector('input[type="color"]'); if (ci) ci.value = color;
    }
  }
  window.applyHex = applyHex;

  // ── Replace image (r5f F5) ────────────────────────────────
  // One hidden shared <input type=file>; the picked file becomes a data URL stored
  // as the slot's `imgSrc` tweak (same parity-safe canonical form the Add-Image
  // LAYER assets use), so /save persists it and the rebake honors it — while the
  // live swap keeps the placeholder's geometry/object-fit untouched.
  var _replInput = null, _replTarget = null;
  function pickReplaceImage(slideId, handle) {
    if (!_replInput) {
      _replInput = document.createElement('input');
      _replInput.type = 'file';
      _replInput.accept = 'image/*';
      _replInput.style.display = 'none';
      document.body.appendChild(_replInput);
      _replInput.addEventListener('change', function() {
        var f = _replInput.files && _replInput.files[0];
        var t = _replTarget; _replTarget = null;
        if (!f || !t) return;
        var reader = new FileReader();
        reader.onload = function() {
          applyToSlide(t.slide, t.handle, 'imgSrc', reader.result);
        };
        reader.readAsDataURL(f);
      });
    }
    _replTarget = { slide: slideId, handle: handle };
    _replInput.value = '';   // allow re-picking the same file
    _replInput.click();
  }
  window.pickReplaceImage = pickReplaceImage;

  // ── AI edit (studio-ai-edit) ──────────────────────────────
  // "Edit with GPT/Gemini" buttons (server-rendered only for providers whose key
  // exists) open a modal: current-image thumbnail + prompt → POST /ai-edit (data
  // URI in, data URI out) → before/after preview → Apply routes through the SAME
  // applyToSlide imgSrc path as Replace image, so live preview, tweaksState,
  // /save and the bake parity are inherited — never re-implemented. Generation is
  // slow (10-60s+) and paid: ONE request in flight per modal, controls locked,
  // spinner + elapsed shown, and the result is never applied without confirm.
  var AI_PROVIDER_LABEL = { gpt: 'Edit with GPT', gemini: 'Edit with Gemini' };
  // Per-provider total-image cap (slot [0] + references) — mirrors the server's
  // _AI_EDIT_IMAGE_CAP so the modal can show "N/16" and block before submitting.
  var AI_PROVIDER_CAP = { gpt: 16, gemini: 14 };
  var aiEdit = { slide: null, handle: null, provider: null, source: null,
                 sourceTransparent: false, refs: [],
                 result: null, prompt: '', busy: false, timer: null, t0: 0, abort: null };

  function aiEl(id) { return document.getElementById(id); }

  // The friendly, human message shown when an input can't be used as an AI-edit
  // source because it isn't a raster image (SVG/vector, or a canvas that came
  // back empty). Mirrors the server's accepted set (png/jpeg/webp/gif) but spoken
  // in user language — the server's "base64 data URI … paths and URLs are not
  // accepted" is dev-speak the user should never see (ai-edit-live-fixes Fix 2).
  var AI_NON_RASTER_MSG =
    'Não consigo usar esta imagem como entrada de IA ' +
    '(SVG/vetor não é suportado — use PNG ou JPG).';

  // A data URI is usable as an AI-edit input ONLY if it's a real raster image the
  // server accepts. SVG (data:image/svg+xml) is vector → rejected; an empty
  // "data:," or "data:image/png;base64," with no payload (what a 0x0 canvas
  // produces for a dimensionless SVG) is also rejected. Kept in lock-step with
  // content_studio._IMAGE_DATA_URI_RE so the client blocks exactly what the
  // server would 400 on — but BEFORE the request, with a human message.
  function aiIsRasterDataUri(uri) {
    return /^data:image\/(png|jpe?g|webp|gif);base64,[A-Za-z0-9+/=\s]+$/i.test(uri || '');
  }

  // Uniformize the layer's CURRENT image to a data URI — the ONLY payload
  // /ai-edit accepts (no path resolution server-side): an <img> is drawn to a
  // canvas (toDataURL → PNG); a background-image div is fetched same-origin →
  // blob → FileReader; a src that is already a data URI (post-Replace /
  // post-AI-edit) passes through untouched.
  function aiCurrentImage(slideId, handle, cb, errCb) {
    var el = getEl(slideId, handle);
    if (!el) { errCb('layer not found on the slide'); return; }
    var img = (el.tagName === 'IMG') ? el : el.querySelector('img');
    if (img && img.getAttribute('src')) {
      var src = img.src;
      // An already-uniform data URI passes through ONLY if it's a real raster;
      // an SVG data URI (data:image/svg+xml) is vector → blocked with a human
      // message instead of being shipped to a server that would 400 on it.
      if (/^data:image\//.test(src)) {
        if (aiIsRasterDataUri(src)) { cb(src); }
        else { errCb(AI_NON_RASTER_MSG); }
        return;
      }
      var probe = new Image();
      probe.onload = function () {
        try {
          var c = document.createElement('canvas');
          c.width = probe.naturalWidth || probe.width;
          c.height = probe.naturalHeight || probe.height;
          c.getContext('2d').drawImage(probe, 0, 0);
          var uri = c.toDataURL('image/png');
          // A dimensionless SVG renders to a 0x0 canvas → toDataURL yields an
          // empty/invalid URI. Treat anything that isn't a real raster as a
          // non-raster input (same human message as a vector source).
          if (aiIsRasterDataUri(uri)) { cb(uri); }
          else { errCb(AI_NON_RASTER_MSG); }
        } catch (e) { errCb('could not read this image (cross-origin source)'); }
      };
      probe.onerror = function () { errCb('could not load the layer image'); };
      probe.src = src;
      return;
    }
    var win = el.ownerDocument.defaultView || window;
    var bg = win.getComputedStyle(el).backgroundImage || '';
    var m = /url\(["']?([^"')]+)["']?\)/.exec(bg);
    if (!m) { errCb('this layer has no image to edit'); return; }
    if (/^data:image\//.test(m[1])) {
      if (aiIsRasterDataUri(m[1])) { cb(m[1]); }
      else { errCb(AI_NON_RASTER_MSG); }
      return;
    }
    fetch(m[1]).then(function (r) {
      if (!r.ok) throw new Error('HTTP ' + r.status);
      return r.blob();
    }).then(function (b) {
      var fr = new FileReader();
      fr.onload = function () {
        var uri = String(fr.result);
        // A fetched SVG background reads back as data:image/svg+xml (vector) →
        // block it before submit with the human message.
        if (aiIsRasterDataUri(uri)) { cb(uri); }
        else { errCb(AI_NON_RASTER_MSG); }
      };
      fr.onerror = function () { errCb('could not read the layer image'); };
      fr.readAsDataURL(b);
    }).catch(function () { errCb('could not fetch the layer image'); });
  }

  // Does a data-URI image carry a genuinely transparent pixel (alpha < 255)?
  // Decodes once to a canvas and scans the alpha channel. Any decode/read failure
  // → false (degrade to "opaque", same conservative default as the motor). Used
  // ONLY to decide the Gemini transparency tag — never blocks the edit.
  function aiDetectAlpha(uri, cb) {
    if (!/^data:image\//.test(uri || '')) { cb(false); return; }
    var im = new Image();
    im.onload = function () {
      try {
        var c = document.createElement('canvas');
        c.width = im.naturalWidth || im.width;
        c.height = im.naturalHeight || im.height;
        var ctx = c.getContext('2d');
        ctx.drawImage(im, 0, 0);
        var data = ctx.getImageData(0, 0, c.width, c.height).data;
        for (var i = 3; i < data.length; i += 4) {
          if (data[i] < 255) { cb(true); return; }
        }
        cb(false);
      } catch (e) { cb(false); }
    };
    im.onerror = function () { cb(false); };
    im.src = uri;
  }

  // Show/hide the Gemini "no transparency" tag: only when the slot image [0] is
  // transparent AND the selected provider is Gemini (GPT preserves it; an opaque
  // input has nothing to lose, so no tag in any provider).
  function aiUpdateGeminiTag() {
    var tag = aiEl('ai-edit-gemini-tag');
    if (!tag) return;
    var show = aiEdit.provider === 'gemini' && !!aiEdit.sourceTransparent;
    tag.style.display = show ? '' : 'none';
  }

  // ── Reference images (ai-edit-multi-input) ────────────────
  // Upload-only extras (pulling from the post/template is out of scope). One
  // hidden shared <input type=file multiple>; each picked file becomes a data URI
  // (same canonical form the slot image uses) and rides along after [0].
  var _aiRefInput = null;
  function addAiRef() {
    if (aiEdit.busy) return;
    var cap = AI_PROVIDER_CAP[aiEdit.provider];
    if (cap && (1 + aiEdit.refs.length) >= cap) {
      aiSetStatus('reached the ' + cap + '-image limit for ' +
                  (AI_PROVIDER_LABEL[aiEdit.provider] || 'this provider'), true, false);
      return;
    }
    if (!_aiRefInput) {
      _aiRefInput = document.createElement('input');
      _aiRefInput.type = 'file';
      _aiRefInput.accept = 'image/*';
      _aiRefInput.multiple = true;
      _aiRefInput.style.display = 'none';
      document.body.appendChild(_aiRefInput);
      _aiRefInput.addEventListener('change', function () {
        var files = _aiRefInput.files ? Array.prototype.slice.call(_aiRefInput.files) : [];
        var capNow = AI_PROVIDER_CAP[aiEdit.provider];
        files.forEach(function (f) {
          if (capNow && (1 + aiEdit.refs.length) >= capNow) return;  // stop at the cap
          var fr = new FileReader();
          fr.onload = function () {
            var uri = String(fr.result);
            // A reference upload must also be a real raster: an SVG/vector file
            // reads back as data:image/svg+xml and would 400 server-side. Block
            // it here with the human message and DON'T add it (ai-edit-live-fixes
            // Fix 2 — guard the references, not just the slot image).
            if (!aiIsRasterDataUri(uri)) {
              aiSetStatus(AI_NON_RASTER_MSG, true, false);
              return;
            }
            aiEdit.refs.push(uri); aiRenderRefs();
          };
          fr.readAsDataURL(f);
        });
      });
    }
    _aiRefInput.value = '';
    _aiRefInput.click();
  }

  function removeAiRef(idx) {
    if (aiEdit.busy) return;
    aiEdit.refs.splice(idx, 1);
    aiRenderRefs();
  }

  function aiRenderRefs() {
    var wrap = aiEl('ai-edit-refthumbs');
    if (wrap) {
      wrap.innerHTML = '';
      aiEdit.refs.forEach(function (uri, i) {
        var fig = document.createElement('span');
        fig.className = 'ai-ref-thumb';
        var img = document.createElement('img');
        img.src = uri; img.alt = 'reference ' + (i + 1);
        var x = document.createElement('button');
        x.type = 'button'; x.className = 'ai-ref-x'; x.setAttribute('aria-label', 'remove');
        x.innerHTML = '&#10005;';
        x.onclick = function () { removeAiRef(i); };
        fig.appendChild(img); fig.appendChild(x);
        wrap.appendChild(fig);
      });
    }
    var cap = AI_PROVIDER_CAP[aiEdit.provider];
    var cnt = aiEl('ai-edit-refcount');
    if (cnt) cnt.textContent = cap ? ('(' + (1 + aiEdit.refs.length) + '/' + cap + ')') : '';
    var add = aiEl('ai-edit-addref');
    if (add) add.disabled = !!(cap && (1 + aiEdit.refs.length) >= cap);
  }

  function aiSetStatus(text, isErr, spin) {
    var s = aiEl('ai-edit-status');
    if (!s) return;
    s.classList.toggle('err', !!isErr);
    s.innerHTML = '';
    if (spin) {
      var sp = document.createElement('span');
      sp.className = 'ai-spinner';
      s.appendChild(sp);
    }
    s.appendChild(document.createTextNode(text || ''));
  }

  function aiSetBusy(busy) {
    aiEdit.busy = busy;
    ['ai-edit-generate', 'ai-edit-apply', 'ai-edit-retry', 'ai-edit-addref'].forEach(function (id) {
      var b = aiEl(id); if (b) b.disabled = busy;
    });
    var p = aiEl('ai-edit-prompt'); if (p) p.disabled = busy;
    // Lock the per-thumbnail remove buttons while a request is in flight.
    var thumbs = aiEl('ai-edit-refthumbs');
    if (thumbs) thumbs.querySelectorAll('.ai-ref-x').forEach(function (x) { x.disabled = busy; });
  }

  function openAiEdit(slideId, handle, provider) {
    var ov = aiEl('ai-edit-modal');
    if (!ov || aiEdit.busy) return;
    aiEdit.slide = slideId; aiEdit.handle = handle; aiEdit.provider = provider;
    aiEdit.source = null; aiEdit.result = null; aiEdit.prompt = '';
    aiEdit.sourceTransparent = false; aiEdit.refs = [];
    var t = aiEl('ai-edit-title');
    if (t) t.textContent = (AI_PROVIDER_LABEL[provider] || 'Edit with AI') + ' — ' + handle;
    var before = aiEl('ai-edit-before'); if (before) before.removeAttribute('src');
    var wrap = aiEl('ai-edit-after-wrap'); if (wrap) wrap.style.display = 'none';
    var ap = aiEl('ai-edit-apply'); if (ap) ap.style.display = 'none';
    var rt = aiEl('ai-edit-retry'); if (rt) rt.style.display = 'none';
    var gen = aiEl('ai-edit-generate'); if (gen) { gen.style.display = ''; gen.disabled = false; }
    var p = aiEl('ai-edit-prompt'); if (p) { p.disabled = false; p.value = ''; }
    aiSetStatus('', false, false);
    aiUpdateGeminiTag();
    aiRenderRefs();
    ov.style.display = 'flex';
    aiCurrentImage(slideId, handle, function (uri) {
      aiEdit.source = uri;
      var b = aiEl('ai-edit-before'); if (b) b.src = uri;
      // Detect alpha on the slot image [0] for the Gemini tag (SHOULD: one decode).
      aiDetectAlpha(uri, function (isTransp) {
        aiEdit.sourceTransparent = isTransp;
        aiUpdateGeminiTag();
      });
    }, function (err) {
      aiSetStatus(err, true, false);
    });
    if (p) setTimeout(function () { p.focus(); }, 50);
  }

  // Cancel / ✕ — closes with NO effect on the slide. An in-flight request is
  // aborted client-side (the server response, if any, is simply dropped).
  function closeAiEdit() {
    var ov = aiEl('ai-edit-modal');
    if (!ov) return;
    if (aiEdit.abort) { try { aiEdit.abort.abort(); } catch (e) {} aiEdit.abort = null; }
    if (aiEdit.timer) { clearInterval(aiEdit.timer); aiEdit.timer = null; }
    aiSetBusy(false);
    aiEdit.result = null; aiEdit.source = null;
    aiEdit.refs = []; aiEdit.sourceTransparent = false;
    ov.style.display = 'none';
  }

  function aiFinish() {
    if (aiEdit.timer) { clearInterval(aiEdit.timer); aiEdit.timer = null; }
    aiEdit.abort = null;
    aiSetBusy(false);
  }

  function runAiEdit() {
    if (aiEdit.busy) return;                  // one request in flight per modal
    if (!aiEdit.source) { aiSetStatus('no source image on this layer', true, false); return; }
    var p = aiEl('ai-edit-prompt');
    var promptText = p ? p.value.replace(/^\s+|\s+$/g, '') : '';
    if (!promptText) {
      aiSetStatus('describe the edit first', true, false);
      if (p) p.focus();
      return;
    }
    aiEdit.prompt = promptText;
    aiSetBusy(true);
    aiEdit.t0 = Date.now();
    aiSetStatus('Generating… 0s', false, true);
    aiEdit.timer = setInterval(function () {
      var secs = Math.round((Date.now() - aiEdit.t0) / 1000);
      aiSetStatus('Generating… ' + secs + 's (10–60s is normal)', false, true);
    }, 1000);
    var ctrl = (typeof AbortController !== 'undefined') ? new AbortController() : null;
    aiEdit.abort = ctrl;
    fetch('/ai-edit', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      // images[0] = the slot image being edited; the rest are the user's
      // reference uploads, in order (ai-edit-multi-input MUST 2).
      body: JSON.stringify({ slide: aiEdit.slide, handle: aiEdit.handle,
                             provider: aiEdit.provider, prompt: promptText,
                             images: [aiEdit.source].concat(aiEdit.refs) }),
      signal: ctrl ? ctrl.signal : undefined
    }).then(function (r) {
      // 4xx responses still carry the {ok:false, error} JSON body.
      return r.json().catch(function () { return { ok: false, error: 'HTTP ' + r.status }; });
    }).then(function (res) {
      aiFinish();
      if (!res || !res.ok || !res.png) {
        // Visible error, NO silent fallback to the other provider (the user
        // chose this button) — re-prompt or switch provider manually.
        aiSetStatus((res && res.error) || 'generation failed — please try again', true, false);
        return;
      }
      aiEdit.result = res.png;
      var after = aiEl('ai-edit-after'); if (after) after.src = res.png;
      var wrap = aiEl('ai-edit-after-wrap'); if (wrap) wrap.style.display = '';
      var gen = aiEl('ai-edit-generate'); if (gen) gen.style.display = 'none';
      var ap = aiEl('ai-edit-apply'); if (ap) ap.style.display = '';
      var rt = aiEl('ai-edit-retry'); if (rt) rt.style.display = '';
      var secs = Math.round((Date.now() - aiEdit.t0) / 1000);
      aiSetStatus('Done in ' + secs + 's — apply it or try again.', false, false);
    }).catch(function (e) {
      aiFinish();
      if (e && e.name === 'AbortError') return;   // user cancelled — modal closed
      aiSetStatus('request failed — is the studio server still running?', true, false);
    });
  }

  // Try again — back to the prompt WITHOUT applying (the result is dropped).
  function retryAiEdit() {
    if (aiEdit.busy) return;
    aiEdit.result = null;
    var wrap = aiEl('ai-edit-after-wrap'); if (wrap) wrap.style.display = 'none';
    var ap = aiEl('ai-edit-apply'); if (ap) ap.style.display = 'none';
    var rt = aiEl('ai-edit-retry'); if (rt) rt.style.display = 'none';
    var gen = aiEl('ai-edit-generate'); if (gen) gen.style.display = '';
    aiSetStatus('', false, false);
    var p = aiEl('ai-edit-prompt'); if (p) p.focus();
  }

  // Apply — EXACTLY the Replace-image path: applyToSlide imgSrc (live swap +
  // tweaksState) → /save persists → bake honors it via the parity script. Revert
  // afterwards = the slot's existing trash/revert mechanism (no new undo stack).
  function applyAiEdit() {
    if (!aiEdit.result) return;
    applyToSlide(aiEdit.slide, aiEdit.handle, 'imgSrc', aiEdit.result);
    // Traceability: record what produced the slot's current image in the tweak
    // itself ({provider, prompt} → tweaks.json; the bake ignores unknown keys).
    var st = slotState(aiEdit.slide, aiEdit.handle);
    st.aiEdit = { provider: aiEdit.provider, prompt: aiEdit.prompt };
    closeAiEdit();
  }

  window.openAiEdit = openAiEdit;
  window.closeAiEdit = closeAiEdit;
  window.runAiEdit = runAiEdit;
  window.retryAiEdit = retryAiEdit;
  window.applyAiEdit = applyAiEdit;
  window.addAiRef = addAiRef;
  window.removeAiRef = removeAiRef;

  // ── Custom dropdown for in-panel selects (font-family, scale) ──────────────
  // Native <select> renders options with OS/browser colours that can produce
  // white-on-white in the dark panel. These use a fixed-position popup styled
  // independently, matching the topbar texture dropdown pattern.
  var _edPop = null, _edTrigger = null;
  function closeEditorDrop() {
    if (_edPop) { _edPop.remove(); _edPop = null; _edTrigger = null; }
  }
  function openEditorDrop(trigger) {
    if (_edTrigger === trigger && _edPop) { closeEditorDrop(); return; }
    closeEditorDrop();
    var opts = JSON.parse(trigger.getAttribute('data-opts') || '[]');
    var sid = trigger.getAttribute('data-sid');
    var handle = trigger.getAttribute('data-handle');
    var prop = trigger.getAttribute('data-prop') || 'fontFamily';
    var curLabel = (trigger.querySelector('.csel-val') || {}).textContent || '';
    var pop = document.createElement('div');
    pop.className = 'ed-pop';
    opts.forEach(function(o) {
      if (o.g) {
        var h = document.createElement('h4'); h.textContent = o.g; pop.appendChild(h); return;
      }
      var b = document.createElement('button'); b.type = 'button'; b.className = 'ed-opt';
      if (o.l === curLabel) b.classList.add('sel');
      b.textContent = o.l;
      if (o.f) b.style.fontFamily = '"' + o.f + '", sans-serif';
      b.onclick = function() {
        var val = trigger.querySelector('.csel-val');
        if (val) val.textContent = o.l;
        applyToSlide(sid, handle, prop, o.v);
        closeEditorDrop();
      };
      pop.appendChild(b);
    });
    document.body.appendChild(pop);
    var rb = trigger.getBoundingClientRect();
    pop.style.display = 'block';
    var left = Math.max(4, Math.round(rb.left));
    var top = Math.round(rb.bottom + 4);
    if (top + 280 > window.innerHeight) top = Math.max(4, Math.round(rb.top - Math.min(280, pop.scrollHeight) - 4));
    pop.style.left = left + 'px';
    pop.style.top = top + 'px';
    _edPop = pop; _edTrigger = trigger;
    setTimeout(function() {
      document.addEventListener('click', function _once(e) {
        if (_edPop && !_edPop.contains(e.target) && e.target !== trigger && !trigger.contains(e.target)) {
          closeEditorDrop();
          document.removeEventListener('click', _once);
        }
      });
    }, 0);
  }
  window.openEditorDrop = openEditorDrop;
  window.closeEditorDrop = closeEditorDrop;

  // ── Layers drag-to-reorder (top row = front-most = highest z) ─
  function applyLayerOrder(list) {
    var rows = [].slice.call(list.querySelectorAll('.layer-row'));
    var slideId = list.dataset.slide;
    var n = rows.length;
    rows.forEach(function(r, i) { applyToSlide(slideId, r.dataset.handle, 'z', n - i); });
  }
  function initLayerDnd() {
    document.querySelectorAll('.layers-list').forEach(function(list) {
      var dragRow = null;
      list.querySelectorAll('.layer-row').forEach(function(row) {
        row.addEventListener('dragstart', function() { dragRow = row; row.classList.add('drag'); });
        row.addEventListener('dragend', function() {
          row.classList.remove('drag'); dragRow = null; applyLayerOrder(list);
        });
        row.addEventListener('dragover', function(e) {
          e.preventDefault();
          if (!dragRow || dragRow === row) return;
          var rect = row.getBoundingClientRect();
          var after = (e.clientY - rect.top) > rect.height / 2;
          list.insertBefore(dragRow, after ? row.nextSibling : row);
        });
      });
    });
  }
  window.addEventListener('DOMContentLoaded', initLayerDnd);
  initLayerDnd();

  // ── Horizontal swipe carousel ─────────────────────────────
  // All slides live in one flex track loaded with their images; the user moves
  // between them by dragging sideways, by the prev/next arrows, or by clicking a
  // dot — and edits the *active* slide one at a time (its panel swaps in).
  // NOT tabs, NOT a vertical stack (PRD REFINED 2026-06-03).
  var track   = document.getElementById('carousel-track');
  var viewer  = document.getElementById('li-viewer');
  var viewers = track ? [].slice.call(track.querySelectorAll('.slide-viewer')) : [];
  var slideIds = viewers.map(function(v) { return v.dataset.slide; });
  var idx = 0;
  var dragging = false, startX = 0, dx = 0, width = 0;

  function setTransform(px) {
    if (track) track.style.transform = 'translateX(' + px + 'px)';
  }

  function goToSlide(i) {
    if (!viewers.length) return;
    idx = Math.max(0, Math.min(viewers.length - 1, i));
    width = viewer ? viewer.clientWidth : 0;
    if (track) track.classList.remove('dragging');
    setTransform(-idx * width);
    var activeId = slideIds[idx];
    window.__activeSlide = activeId;   // for palette swatch -> selected-layer fill
    // edit one slide at a time: only the active slide's panel is shown
    document.querySelectorAll('.slide-panel').forEach(function(p) {
      p.style.display = p.dataset.slide === activeId ? 'block' : 'none';
    });
    document.querySelectorAll('[data-slide-dot]').forEach(function(d, di) {
      d.classList.toggle('on', di === idx);
    });
    var prev = document.getElementById('nav-prev');
    var next = document.getElementById('nav-next');
    if (prev) prev.disabled = (idx === 0);
    if (next) next.disabled = (idx === viewers.length - 1);
    var cur = document.getElementById('slide-counter-cur');
    if (cur) cur.textContent = (idx + 1);
    if (window.__renderPins) window.__renderPins();   // active slide's comment pins
    if (window.__onSlideChange) window.__onSlideChange(activeId);  // Konva canvas overlay
  }
  window.goToSlide = goToSlide;
  window.navSlide = function(delta) { goToSlide(idx + delta); };

  // ── Pointer drag (mouse + touch via Pointer Events) ───────
  // The slide <iframe> has pointer-events:none, so drags land on the viewer.
  if (viewer && viewers.length > 1) {
    function endDrag() {
      if (!dragging) return;
      dragging = false;
      var threshold = width * 0.18;
      if (dx <= -threshold) goToSlide(idx + 1);
      else if (dx >= threshold) goToSlide(idx - 1);
      else goToSlide(idx);   // snap back
      dx = 0;
    }
    viewer.addEventListener('pointerdown', function(e) {
      if (e.target.closest('.nav-arrow')) return;   // arrows have their own handler
      dragging = true; startX = e.clientX; dx = 0;
      width = viewer.clientWidth;
      if (track) track.classList.add('dragging');
      try { viewer.setPointerCapture(e.pointerId); } catch (err) {}
    });
    viewer.addEventListener('pointermove', function(e) {
      if (!dragging) return;
      dx = e.clientX - startX;
      // edge resistance past the first / last slide
      if ((idx === 0 && dx > 0) || (idx === viewers.length - 1 && dx < 0)) dx *= 0.35;
      setTransform(-idx * width + dx);
    });
    viewer.addEventListener('pointerup', endDrag);
    viewer.addEventListener('pointercancel', endDrag);
    window.addEventListener('keydown', function(e) {
      if (e.key === 'ArrowLeft') goToSlide(idx - 1);
      else if (e.key === 'ArrowRight') goToSlide(idx + 1);
    });
    window.addEventListener('resize', function() { goToSlide(idx); });
  }

  goToSlide(0);

  // ── Import / resume: re-apply a SAVED tweaks.json to the live slides ──
  // Only IMPORTED_TWEAKS (the file) is replayed — never the computed defaults — so a
  // fresh run renders the template untouched. Applied per-iframe once it loads.
  function applySavedTweaks(sid) {
    var zones = IMPORTED_TWEAKS[sid]; if (!zones) return;
    Object.keys(zones).forEach(function(handle) {
      var props = zones[handle]; if (!props || typeof props !== 'object') return;
      Object.keys(props).forEach(function(prop) { applyToSlide(sid, handle, prop, props[prop]); });
    });
  }
  if (Object.keys(IMPORTED_TWEAKS).length) {
    document.querySelectorAll('iframe[id^="frame-"]').forEach(function(f) {
      var sid = f.id.replace('frame-', '');
      f.addEventListener('load', function() { applySavedTweaks(sid); });
      try { if (f.contentDocument && f.contentDocument.readyState === 'complete') applySavedTweaks(sid); } catch (e) {}
    });
  }

  // ── Comment pins — slide-anchored, preview-only (Stage B) ─
  // A pin BELONGS to a slide and stores canvas % of the 1080x1350 (same space as the
  // slot bboxes), resolved to the nearest data-slot zone; only the active slide's
  // pins render (they ride the carousel). Persisted in localStorage + exportable as
  // comments.json — they NEVER touch tweaks.json or the bake. A drag (swipe)
  // suppresses the pin so the two gestures don't collide.
  (function() {
    var canvas = document.getElementById('comment-stage');
    var layer = document.getElementById('commentLayer');
    var hint = document.getElementById('comment-hint');
    if (!canvas || !layer) return;
    var KEY = 'editor.comments.' + (window.__EDITOR_RUN_ID__ || 'default');
    var comments = {};
    try { var ls = JSON.parse(localStorage.getItem(KEY)); if (ls && typeof ls === 'object') comments = ls; } catch (e) {}
    // an imported comments.json (from the run folder) wins over localStorage
    var impHas = Object.keys(INITIAL_COMMENTS || {}).some(function(s) { return (INITIAL_COMMENTS[s] || []).length; });
    if (impHas) comments = INITIAL_COMMENTS;
    var composer = null, downX = 0, downY = 0, moved = false, seq = 0;

    function clamp(v, lo, hi) { return Math.max(lo, Math.min(hi, v)); }
    function r1(v) { return Math.round(v * 10) / 10; }
    function total() { return Object.keys(comments).reduce(function(n, s) { return n + (comments[s] || []).length; }, 0); }
    function persist() { try { localStorage.setItem(KEY, JSON.stringify(comments)); } catch (e) {} updateHint(); }
    // The hint guides the user ONLY while comment mode is armed (Addendum 9 #4) —
    // off by default so the caption + canvas are directly editable without a pin-drop.
    function updateHint() { if (hint) hint.style.display = window.__commentMode ? '' : 'none'; }
    // The topbar Comment toggle (studio.js) flips window.__commentMode then calls this.
    window.__setCommentMode = function(on) { if (!on) closeComposer(); updateHint(); };
    function esc(s) { return String(s).replace(/[&<>"]/g, function(m) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[m]; }); }
    function closeComposer() { if (composer) { composer.remove(); composer = null; } }

    function activeWrap() {
      var sid = window.__activeSlide;
      return sid ? document.querySelector('.slide-viewer[data-slide="' + sid + '"] .slide-frame-wrap') : null;
    }
    // Resolve a canvas-% point to the nearest zone handle (mirrors _nearest_zone).
    function nearestZone(sid, x, y) {
      var bbs = SLOT_BBOXES[sid] || [];
      var inside = bbs.filter(function(b) { return b.x <= x && x <= b.x + b.w && b.y <= y && y <= b.y + b.h; });
      if (inside.length) { inside.sort(function(a, b) { return (a.w * a.h) - (b.w * b.h); }); return inside[0].handle; }
      if (!bbs.length) return null;
      var best = null, bd = Infinity;
      bbs.forEach(function(b) { var cx = b.x + b.w / 2, cy = b.y + b.h / 2, d = (cx - x) * (cx - x) + (cy - y) * (cy - y); if (d < bd) { bd = d; best = b.handle; } });
      return best;
    }
    // canvas-% (xPct,yPct) -> pixel offset inside the comment layer, via the active frame.
    function toScreen(xPct, yPct) {
      var wrap = activeWrap(); if (!wrap) return null;
      var wr = wrap.getBoundingClientRect(), lr = layer.getBoundingClientRect();
      return { left: (wr.left - lr.left) + xPct / 100 * wr.width, top: (wr.top - lr.top) + yPct / 100 * wr.height };
    }

    function makePin(c) {
      var pos = toScreen(c.xPct, c.yPct); if (!pos) return null;
      var p = document.createElement('button');
      p.className = 'pin'; p.type = 'button'; p.setAttribute('data-id', c.id);
      p.style.left = pos.left + 'px'; p.style.top = pos.top + 'px';
      p.title = (c.zone ? '[' + c.zone + '] ' : '') + c.text;
      p.innerHTML = '<svg class="ic" width="15" height="15" viewBox="0 0 16 16" fill="none" ' +
        'stroke="currentColor" stroke-width="1.45" stroke-linecap="round" stroke-linejoin="round">' +
        '<use href="#ic-comment"/></svg>';
      p.addEventListener('click', function(ev) { ev.stopPropagation(); openComposer(c); });
      return p;
    }
    function renderPins() {
      var old = layer.querySelectorAll('.pin');
      for (var i = 0; i < old.length; i++) old[i].remove();
      var sid = window.__activeSlide;
      (comments[sid] || []).forEach(function(c) { var pin = makePin(c); if (pin) layer.appendChild(pin); });
      updateHint();
    }
    window.__renderPins = renderPins;        // goToSlide calls this on slide change
    window.__getComments = function() { return comments; };  // for exportTweaks

    function openComposer(c) {
      closeComposer();
      var existing = !!c.id;
      var pos = toScreen(c.xPct, c.yPct) || { left: 20, top: 20 };
      var el = document.createElement('div');
      el.className = 'composer';
      el.style.left = clamp(pos.left + 16, 8, canvas.clientWidth - 246) + 'px';
      el.style.top = clamp(pos.top - 6, 8, canvas.clientHeight - 150) + 'px';
      el.innerHTML =
        '<textarea placeholder="Add a comment…">' + (existing ? esc(c.text) : '') + '</textarea>' +
        '<div class="composer-actions">' +
          (existing ? '<button class="cbtn cbtn--del" data-act="delete" title="Delete">✕</button>' : '') +
          (c.zone ? '<span class="composer-zone">' + esc(c.zone) + '</span>' : '') +
          '<span class="cspring"></span>' +
          '<button class="cbtn cbtn--ghost" data-act="cancel">Cancel</button>' +
          '<button class="cbtn cbtn--primary" data-act="ok">' + (existing ? 'Save' : 'Comment') + '</button>' +
        '</div>';
      el.addEventListener('click', function(e) { e.stopPropagation(); });
      el.addEventListener('pointerdown', function(e) { e.stopPropagation(); });
      layer.appendChild(el);
      composer = el;
      var ta = el.querySelector('textarea');
      ta.focus(); ta.setSelectionRange(ta.value.length, ta.value.length);
      el.querySelector('[data-act="cancel"]').onclick = closeComposer;
      el.querySelector('[data-act="ok"]').onclick = function() {
        var text = ta.value.trim();
        if (!text) { closeComposer(); return; }
        if (existing) { c.text = text; }
        else {
          var sid = c.slide;
          comments[sid] = comments[sid] || [];
          comments[sid].push({ id: 'c' + (++seq) + '-' + Date_now(), xPct: c.xPct, yPct: c.yPct,
            zone: nearestZone(sid, c.xPct, c.yPct), text: text });
        }
        persist(); renderPins(); closeComposer();
      };
      var del = el.querySelector('[data-act="delete"]');
      if (del) del.onclick = function() {
        var sid = c.slide || window.__activeSlide;
        comments[sid] = (comments[sid] || []).filter(function(k) { return k.id !== c.id; });
        persist(); renderPins(); closeComposer();
      };
      ta.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && (e.metaKey || e.ctrlKey)) el.querySelector('[data-act="ok"]').click();
        else if (e.key === 'Escape') closeComposer();
      });
    }
    // a tiny monotonic id suffix (Date.now isn't allowed at build time, fine at runtime)
    function Date_now() { return (new Date()).getTime().toString(36); }

    // A click drops a pin on the ACTIVE slide; a drag (swipe) does not. Skip clicks
    // on interactive chrome so only the slide/stage surface accepts pins.
    canvas.addEventListener('pointerdown', function(e) { downX = e.clientX; downY = e.clientY; moved = false; });
    canvas.addEventListener('pointermove', function(e) {
      if (Math.abs(e.clientX - downX) > 6 || Math.abs(e.clientY - downY) > 6) moved = true;
    });
    canvas.addEventListener('click', function(e) {
      if (moved) return;
      // Only drop pins in explicit comment mode (Addendum 9 #4) — otherwise clicks go
      // to the caption / canvas / chrome cleanly, with no accidental composer.
      if (!window.__commentMode) return;
      if (e.target.closest('.pin, .composer, .nav-arrow, .li-act, .li-dot, button, a, input, textarea, select')) return;
      var sid = window.__activeSlide, wrap = activeWrap(); if (!sid || !wrap) return;
      var wr = wrap.getBoundingClientRect();
      var xPct = clamp(((e.clientX - wr.left) / wr.width) * 100, 0, 100);
      var yPct = clamp(((e.clientY - wr.top) / wr.height) * 100, 0, 100);
      openComposer({ slide: sid, xPct: r1(xPct), yPct: r1(yPct) });
    });
    document.addEventListener('keydown', function(e) { if (e.key === 'Escape') closeComposer(); });
    window.addEventListener('resize', function() { closeComposer(); renderPins(); });

    renderPins();
  })();
})();
</script>"""


def _build_initial_tweaks_state(
    slides_info: list[dict],
    present_by_slide: dict | None = None,
) -> dict:
    """Build the initial tweaksState dict (global + one dict per slide).

    ``present_by_slide`` maps slide_id -> set of data-slot handles in the rendered
    slide. When given, only those handles get a state entry — so the exported
    tweaks.json carries no phantom keys for prompt-only / absent-optional slots."""
    state: dict = {"global": {"accent": "", "fontDisplay": "", "masthead": ""}}
    for info in slides_info:
        sid = info["slide_id"]
        present = (present_by_slide or {}).get(sid)
        slots = []
        if info.get("instructions"):
            try:
                slots = parse_slots_from_instructions(info["instructions"])
            except Exception:
                slots = []
        slide_state: dict = {}
        for slot in slots:
            name = slot["name"]
            handle, is_asset = _slot_handle(name)
            if present is not None and handle not in present:
                continue
            stype = slot.get("type", "text")
            if is_asset:
                stype = "svg" if "SVG" in name.upper() else "image"
            bbox = slot.get("bbox") or {}
            entry: dict = {}
            if stype == "text":
                entry = {
                    "text": slot.get("sample") or "",
                    "x": bbox.get("x", 0),
                    "y": bbox.get("y", 0),
                    "w": bbox.get("w", 100),
                    "fontSize": 5.0,
                    "opacity": 1.0,
                    "tilt": 0,
                }
            elif stype == "pill":
                entry = {
                    "text": slot.get("sample") or "",
                    "x": bbox.get("x", 0),
                    "y": bbox.get("y", 0),
                    "w": bbox.get("w", 30),
                }
            elif stype in ("image", "svg"):
                entry = {
                    "x": bbox.get("x", 0),
                    "y": bbox.get("y", 0),
                    "w": bbox.get("w", 100),
                    "h": bbox.get("h", 60),
                    "tilt": 0,
                    "opacity": 1.0,
                    "scale": "cover",
                    "layers": [],   # CONS-02: layer-ready slot
                }
                if stype == "svg":
                    entry["color"] = ""
            elif stype == "chrome":
                entry = {"visible": True}
            slide_state[handle] = entry
        state[sid] = slide_state
    return state


def _blank_unresolved_assets(data: dict) -> dict:
    """Preview-only: blank a ``*_PATH``/``*_SRC`` slot that did NOT resolve to a real
    asset. ``embed_paths_as_data_uris`` turns real files into ``data:`` URIs; anything
    still left as a plain string is leftover sample/descriptive text (e.g.
    ``ANNOTATION_SVG_PATH`` carrying its own description). Left in place it makes an
    optional ``{{#…_PATH}}`` section render a BROKEN ``<img>``. Blanking it collapses
    the section / yields ``src=""`` (then the transparent placeholder), never a broken
    image. Bake is untouched (this is the editor's own data dict)."""
    out = dict(data)
    for k, v in list(out.items()):
        if (k.endswith("_PATH") or k.endswith("_SRC")) and isinstance(v, str):
            if v and not v.startswith(("data:", "http://", "https://")):
                out[k] = ""
    return out


# Match a whole empty <img src=""> tag so we can read its data-slot (the zone's
# handle) and stamp a labelled placeholder. Group 1 = the full tag text.
_EMPTY_IMG_TAG_RE = re.compile(r'<img\b[^>]*?\bsrc=""[^>]*?>', re.IGNORECASE)
_IMG_SLOT_RE = re.compile(r"""\bdata-slot=["']([^"']+)["']""", re.IGNORECASE)

# Match an opening div/section/figure tag whose inline style carries a
# background-image:url() that resolved EMPTY (the Mustache slot was unfilled →
# url(''), url(), or url("")) — the bg-image counterpart of <img src="">.
# Group 0 = the full opening tag.
_BG_IMG_OPEN_TAG_RE = re.compile(
    r'<(?:div|section|figure)\b[^>]*\bstyle\s*=\s*"[^"]*'
    r"background-image\s*:\s*url\(\s*['\"]?\s*['\"]?\s*\)"
    r'[^"]*"[^>]*>',
    re.IGNORECASE,
)
# The empty url() token inside an inline style (any quoting / whitespace).
_EMPTY_BG_URL_RE = re.compile(
    r"background-image\s*:\s*url\(\s*['\"]?\s*['\"]?\s*\)", re.IGNORECASE)


def _placeholder_empty_images(html_text: str, template_dir: Path | None = None) -> str:
    """Preview-only: flag a broken ``<img src="">`` (an image/photo slot that did NOT
    resolve to a real asset) with a VISIBLE dashed placeholder labelled "missing
    image: <HANDLE>", so an unwired hero (e.g. PHOTO_MAIN) is obviously broken
    instead of an invisible transparent zone that looks "by design" (audit #3/#10).

    Runs AFTER fill, ONLY in the editor preview (``_build_srcdoc``) — the real bake
    (``render_template.py``) never calls this, so a real post never ships the hint.
    The placeholder is a self-contained inline data-URI SVG carrying the label, so it
    fills the zone and reads at any size.

    Also heals a ``background-image:url('')`` DIV (the bg-image counterpart of an
    empty ``<img>``): a hero/AI zone painted by an inline
    ``style="background-image:url('{{PHOTO_MAIN_PATH}}')"`` whose slot is unfilled
    resolves to ``url('')`` and shows BLANK — before any render exists, the editor
    would see no image and "Edit-with-AI" would report the layer has nothing to edit
    (the prop-scene-cover empty-state miss). It gets the SAME labelled placeholder
    injected as its background-image so the empty zone reads as an editable
    (replaceable) image slot, consistent with how an empty ``<img>`` is handled.

    Deterministic + idempotent: a FILLED slot (``url('data:…')`` / a real path) is
    left untouched, and re-running on already-healed HTML is a no-op (the empty
    ``url()`` token is gone after the first pass).

    ``template_dir`` is accepted for call-site compatibility but is unused (the
    placeholder is fully inline)."""
    new = html_text

    # --- 1. empty <img src=""> elements ---
    if 'src=""' in new:
        def _sub(m: re.Match) -> str:
            tag = m.group(0)
            slot_m = _IMG_SLOT_RE.search(tag)
            handle = slot_m.group(1) if slot_m else "image"
            uri = "data:image/svg+xml;base64," + base64.b64encode(
                _missing_img_placeholder_svg(handle).encode("utf-8")
            ).decode("ascii")
            # Replace the empty src and tag it; keep all other attributes (data-slot, etc.)
            return tag.replace('src=""', f'src="{uri}" data-ph="1"', 1)
        new = _EMPTY_IMG_TAG_RE.sub(_sub, new)

    # --- 2. background-image:url('') divs (the bg-image counterpart) ---
    def _sub_bg(m: re.Match) -> str:
        tag = m.group(0)
        slot_m = _IMG_SLOT_RE.search(tag)
        handle = slot_m.group(1) if slot_m else "image"
        uri = "data:image/svg+xml;base64," + base64.b64encode(
            _missing_img_placeholder_svg(handle).encode("utf-8")
        ).decode("ascii")
        # Swap the empty url() for the placeholder data-URI and tag the element so the
        # CSS backdrop tint applies. Keep all other style/attributes intact.
        healed = _EMPTY_BG_URL_RE.sub(
            f"background-image:url('{uri}')", tag, count=1)
        if "data-ph=" not in healed:
            healed = re.sub(r"(<\w+)", r'\1 data-ph="1"', healed, count=1)
        return healed
    new = _BG_IMG_OPEN_TAG_RE.sub(_sub_bg, new)

    if new == html_text:
        return html_text
    # The placeholder SVG already carries the dashed border + label; a faint backdrop
    # tint makes it read even over a dark full-bleed zone. The bg-image variant also
    # gets background-size:contain so the dashed box is fully visible (not cropped).
    style = (
        '<style>img[data-ph="1"]{background:rgba(255,255,255,.04);'
        'object-fit:contain!important}'
        '[data-ph="1"]:not(img){background-color:rgba(255,255,255,.04)!important;'
        'background-size:contain!important;background-repeat:no-repeat!important;'
        'background-position:center!important}</style>'
    )
    if "<head>" in new:
        return new.replace("<head>", "<head>" + style, 1)
    return style + new


def _missing_img_placeholder_svg(handle: str) -> str:
    """A self-contained dashed-box placeholder SVG labelled with the slot handle —
    the editor's visible "this image zone is empty/unwired" hint (audit #3)."""
    import html as _html
    label = _html.escape(f"missing image: {handle}")
    return (
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 400 300' "
        "preserveAspectRatio='xMidYMid meet'>"
        "<rect x='6' y='6' width='388' height='288' rx='10' fill='rgba(120,120,140,0.10)' "
        "stroke='#9aa0b4' stroke-width='3' stroke-dasharray='12 9'/>"
        "<g fill='#9aa0b4'>"
        "<rect x='168' y='118' width='64' height='50' rx='6' fill='none' stroke='#9aa0b4' stroke-width='3'/>"
        "<circle cx='186' cy='136' r='6'/>"
        "<path d='M174 162 L194 142 L210 158 L222 148 L226 162 Z'/>"
        "</g>"
        f"<text x='200' y='205' text-anchor='middle' "
        "font-family='-apple-system,Segoe UI,Roboto,sans-serif' font-size='20' "
        f"font-weight='600' fill='#c5cad8'>{label}</text>"
        "</svg>"
    )


# Inline lucide-style icons (24x24, stroke=currentColor) so the editor stays a
# self-contained static file (CONS-01) while borrowing the command-centre icon set.
_ICON_PATHS = {
    "sliders": '<line x1="21" x2="14" y1="4" y2="4"/><line x1="10" x2="3" y1="4" y2="4"/><line x1="21" x2="12" y1="12" y2="12"/><line x1="8" x2="3" y1="12" y2="12"/><line x1="21" x2="16" y1="20" y2="20"/><line x1="12" x2="3" y1="20" y2="20"/><line x1="14" x2="14" y1="2" y2="6"/><line x1="8" x2="8" y1="10" y2="14"/><line x1="16" x2="16" y1="18" y2="22"/>',
    "type": '<polyline points="4 7 4 4 20 4 20 7"/><line x1="9" x2="15" y1="20" y2="20"/><line x1="12" x2="12" y1="4" y2="20"/>',
    "tag": '<path d="M12.586 2.586A2 2 0 0 0 11.172 2H4a2 2 0 0 0-2 2v7.172a2 2 0 0 0 .586 1.414l8.704 8.704a2.426 2.426 0 0 0 3.42 0l6.58-6.58a2.426 2.426 0 0 0 0-3.42z"/><circle cx="7.5" cy="7.5" r=".5" fill="currentColor"/>',
    "image": '<rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"/>',
    "layout": '<rect width="7" height="7" x="3" y="3" rx="1"/><rect width="7" height="7" x="14" y="3" rx="1"/><rect width="7" height="7" x="14" y="14" rx="1"/><rect width="7" height="7" x="3" y="14" rx="1"/>',
    "palette": '<circle cx="13.5" cy="6.5" r=".5" fill="currentColor"/><circle cx="17.5" cy="10.5" r=".5" fill="currentColor"/><circle cx="8.5" cy="7.5" r=".5" fill="currentColor"/><circle cx="6.5" cy="12.5" r=".5" fill="currentColor"/><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10c.926 0 1.648-.746 1.648-1.688 0-.437-.18-.835-.437-1.125-.29-.289-.438-.652-.438-1.125a1.64 1.64 0 0 1 1.668-1.668h1.996c3.051 0 5.555-2.503 5.555-5.555C21.965 6.012 17.461 2 12 2z"/>',
    "at": '<circle cx="12" cy="12" r="4"/><path d="M16 8v5a3 3 0 0 0 6 0v-1a10 10 0 1 0-4 8"/>',
    "download": '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" x2="12" y1="15" y2="3"/>',
    "layers": '<path d="M12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83z"/><path d="m22 17.65-9.17 4.16a2 2 0 0 1-1.66 0L2 17.65"/><path d="m22 12.65-9.17 4.16a2 2 0 0 1-1.66 0L2 12.65"/>',
    # wand-2 — the "magic pencil" break-into-layers affordance for full-AI images.
    "wand": '<path d="m21.64 3.64-1.28-1.28a1.21 1.21 0 0 0-1.72 0L2.36 18.64a1.21 1.21 0 0 0 0 1.72l1.28 1.28a1.2 1.2 0 0 0 1.72 0L21.64 5.36a1.2 1.2 0 0 0 0-1.72"/><path d="m14 7 3 3"/><path d="M5 6v4"/><path d="M19 14v4"/><path d="M10 2v2"/><path d="M7 8H3"/><path d="M21 16h-4"/><path d="M11 3H9"/>',
    "thumbsup": '<path d="M7 10v12"/><path d="M15 5.88 14 10h5.83a2 2 0 0 1 1.92 2.56l-2.33 8A2 2 0 0 1 17.5 22H4a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2h2.76a2 2 0 0 0 1.79-1.11L12 2a3.13 3.13 0 0 1 3 3.88z"/>',
    "comment": '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22z"/>',
    "repeat": '<path d="m17 2 4 4-4 4"/><path d="M3 11v-1a4 4 0 0 1 4-4h14"/><path d="m7 22-4-4 4-4"/><path d="M21 13v1a4 4 0 0 1-4 4H3"/>',
    "send": '<path d="M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z"/><path d="m21.854 2.147-10.94 10.939"/>',
    "chevron-left": '<path d="m15 18-6-6 6-6"/>',
    "chevron-right": '<path d="m9 18 6-6-6-6"/>',
    "eye": '<path d="M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0"/><circle cx="12" cy="12" r="3"/>',
    "eye-off": '<path d="M10.733 5.076a10.744 10.744 0 0 1 11.205 6.575 1 1 0 0 1 0 .696 10.747 10.747 0 0 1-1.444 2.49"/><path d="M14.084 14.158a3 3 0 0 1-4.242-4.242"/><path d="M17.479 17.499a10.75 10.75 0 0 1-15.417-5.151 1 1 0 0 1 0-.696 10.75 10.75 0 0 1 4.446-5.143"/><path d="m2 2 20 20"/>',
    "lock": '<rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "unlock": '<rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 9.9-1"/>',
    "trash": '<path d="M3 6h18"/><path d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6"/><path d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"/><line x1="10" x2="10" y1="11" y2="17"/><line x1="14" x2="14" y1="11" y2="17"/>',
    "play": '<polygon points="6 3 20 12 6 21 6 3"/>',
    "layers2": '<path d="M12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83z"/><path d="m22 17.65-9.17 4.16a2 2 0 0 1-1.66 0L2 17.65"/><path d="m22 12.65-9.17 4.16a2 2 0 0 1-1.66 0L2 12.65"/>',
}


def _icon(name: str, size: int = 14, cls: str = "") -> str:
    """Return an inline lucide SVG (stroke=currentColor) for a self-contained file."""
    paths = _ICON_PATHS.get(name, "")
    klass = f"ic {cls}".strip()
    return (
        f'<svg class="{klass}" width="{size}" height="{size}" viewBox="0 0 24 24" '
        f'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
        f'stroke-linejoin="round" aria-hidden="true">{paths}</svg>'
    )


# ── AI edit (studio-ai-edit): provider logos as inline SVG constants ──────────
# Same self-contained philosophy as _ICON_PATHS (no vendor files), but these are
# FILLED brand marks, so the stroke-based _icon() factory doesn't fit — they are
# kept as complete <svg> snippets instead. fill=currentColor so they inherit the
# button's text colour like every other panel icon.
_OPENAI_LOGO_SVG = (
    '<svg class="ic" width="13" height="13" viewBox="0 0 24 24" fill="currentColor" '
    'aria-hidden="true"><path d="M22.2819 9.8211a5.9847 5.9847 0 0 0-.5157-4.9108 '
    '6.0462 6.0462 0 0 0-6.5098-2.9A6.0651 6.0651 0 0 0 4.9807 4.1818a5.9847 5.9847 '
    '0 0 0-3.9977 2.9 6.0462 6.0462 0 0 0 .7427 7.0966 5.98 5.98 0 0 0 .511 4.9107 '
    '6.051 6.051 0 0 0 6.5146 2.9001A5.9847 5.9847 0 0 0 13.2599 24a6.0557 6.0557 0 '
    '0 0 5.7718-4.2058 5.9894 5.9894 0 0 0 3.9977-2.9001 6.0557 6.0557 0 0 0-.7475'
    '-7.073zm-9.022 12.6081a4.4755 4.4755 0 0 1-2.8764-1.0408l.1419-.0804 4.7783'
    '-2.7582a.7948.7948 0 0 0 .3927-.6813v-6.7369l2.02 1.1686a.071.071 0 0 1 .038.052'
    'v5.5826a4.504 4.504 0 0 1-4.4945 4.4944zm-9.6607-4.1254a4.4708 4.4708 0 0 1'
    '-.5346-3.0137l.142.0852 4.783 2.7582a.7712.7712 0 0 0 .7806 0l5.8428-3.3685v2.3324'
    'a.0804.0804 0 0 1-.0332.0615L9.74 19.9502a4.4992 4.4992 0 0 1-6.1408-1.6464zM2.3408 '
    '7.8956a4.485 4.485 0 0 1 2.3655-1.9728V11.6a.7664.7664 0 0 0 .3879.6765l5.8144 '
    '3.3543-2.0201 1.1685a.0757.0757 0 0 1-.071 0l-4.8303-2.7865A4.504 4.504 0 0 1 '
    '2.3408 7.8956zm16.5963 3.8558L13.1038 8.364 15.1192 7.2a.0757.0757 0 0 1 .071 0'
    'l4.8303 2.7913a4.4944 4.4944 0 0 1-.6765 8.1042v-5.6772a.79.79 0 0 0-.407-.667z'
    'm2.0107-3.0231l-.142-.0852-4.7735-2.7818a.7759.7759 0 0 0-.7854 0L9.409 9.2297V'
    '6.8974a.0662.0662 0 0 1 .0284-.0615l4.8303-2.7866a4.4992 4.4992 0 0 1 6.6802 '
    '4.66zM8.3065 12.8631l-2.02-1.1638a.0804.0804 0 0 1-.038-.0567V6.0742a4.4992 '
    '4.4992 0 0 1 7.3757-3.4537l-.142.0805L8.704 5.4592a.7948.7948 0 0 0-.3927.6813z'
    'm1.0976-2.3654l2.602-1.4998 2.6069 1.4998v2.9994l-2.5974 1.4997-2.6067-1.4997Z"/>'
    '</svg>'
)
_GEMINI_LOGO_SVG = (
    '<svg class="ic" width="13" height="13" viewBox="0 0 24 24" fill="currentColor" '
    'aria-hidden="true"><path d="M11.04 19.32Q12 21.51 12 24q0-2.49.93-4.68.96-2.19 '
    '2.58-3.81t3.81-2.55Q21.51 12 24 12q-2.49 0-4.68-.93a12.3 12.3 0 0 1-3.81-2.58 '
    '12.3 12.3 0 0 1-2.58-3.81Q12 2.49 12 0q0 2.49-.96 4.68-.93 2.19-2.55 3.81a12.3 '
    '12.3 0 0 1-3.81 2.58Q2.49 12 0 12q2.49 0 4.68.96 2.19.93 3.81 2.55t2.55 3.81"/>'
    '</svg>'
)

# Render order + labels for the per-provider buttons. The booleans that gate them
# come from the SERVER (content_studio resolves key presence; values never flow).
_AI_EDIT_PROVIDER_META = (
    ("gpt", "Edit with GPT", _OPENAI_LOGO_SVG),
    ("gemini", "Edit with Gemini", _GEMINI_LOGO_SVG),
)


def _ai_edit_buttons(sid: str, handle: str, ai_providers: dict | None) -> str:
    """The "Edit with AI" sec-sub for one IMAGE control group (studio-ai-edit).

    One button per provider whose presence boolean is truthy. A provider with no
    key gets NO button (not a disabled one); when no provider is available the
    whole section is absent (empty string) — the editor looks exactly as before.
    """
    if not ai_providers:
        return ""
    btns = []
    for prov, label, logo in _AI_EDIT_PROVIDER_META:
        if not ai_providers.get(prov):
            continue
        btns.append(
            f"""      <button type="button" class="ai-edit-btn" data-provider="{prov}"
        onclick="openAiEdit('{sid}','{handle}','{prov}')">
        {logo}<span>{label}</span>
      </button>"""
        )
    if not btns:
        return ""
    return (
        '    <div class="sec-sub ai-edit-sub">\n'
        '      <span class="label">Edit with AI</span>\n'
        + "\n".join(btns) + "\n    </div>"
    )


def _build_ai_edit_modal() -> str:
    """The AI-edit modal shell (studio-ai-edit) — one per editor, reused across
    slides/providers/layers. Emitted ONLY when at least one provider is available,
    so a no-key editor carries zero AI markup. The JS (openAiEdit / runAiEdit /
    applyAiEdit) fills the thumbnails and drives state; Apply routes through the
    EXISTING applyToSlide imgSrc path (same as Replace image), so save/bake/parity
    are inherited, never re-implemented."""
    return (
        '<div id="ai-edit-modal" class="ai-modal-overlay" role="dialog" aria-modal="true">\n'
        '  <div class="ai-modal">\n'
        '    <div class="ai-modal-head">\n'
        '      <span class="ai-modal-title" id="ai-edit-title">Edit with AI</span>\n'
        '      <button type="button" class="ai-modal-close" aria-label="Close"\n'
        '        onclick="closeAiEdit()">&#10005;</button>\n'
        '    </div>\n'
        '    <div class="ai-modal-imgs">\n'
        '      <figure><img id="ai-edit-before" alt="Current image">'
        '<figcaption>Current</figcaption></figure>\n'
        '      <figure id="ai-edit-after-wrap" style="display:none">'
        '<img id="ai-edit-after" alt="AI result"><figcaption>Result</figcaption></figure>\n'
        '    </div>\n'
        # Reference images (ai-edit-multi-input): upload-only extras that ride along
        # with the slot image. Thumbnails render here, each with a remove (x); the
        # submit packs them into the `images` array after [0] (the slot image).
        '    <div class="ai-ref-block">\n'
        '      <div class="ai-ref-head">\n'
        '        <span class="ai-ref-label">Reference images '
        '<span class="ai-ref-count" id="ai-edit-refcount"></span></span>\n'
        '        <button type="button" class="ai-btn ai-btn--ghost ai-ref-add" '
        'id="ai-edit-addref" onclick="addAiRef()">+ Add reference</button>\n'
        '      </div>\n'
        '      <div class="ai-ref-thumbs" id="ai-edit-refthumbs"></div>\n'
        '    </div>\n'
        # Gemini transparency warning (layer-image-ai-edit MUST 4): shown only when
        # the slot image [0] is genuinely transparent AND the provider is Gemini.
        '    <div class="ai-gemini-tag" id="ai-edit-gemini-tag" style="display:none">'
        'O Gemini não preserva transparência — o resultado virá com fundo.</div>\n'
        '    <textarea id="ai-edit-prompt" rows="3" '
        'placeholder="Describe the edit (e.g. make the background a soft studio grey)"></textarea>\n'
        '    <div class="ai-modal-status" id="ai-edit-status"></div>\n'
        '    <div class="ai-modal-actions">\n'
        '      <button type="button" class="ai-btn ai-btn--ghost" id="ai-edit-cancel" '
        'onclick="closeAiEdit()">Cancel</button>\n'
        '      <button type="button" class="ai-btn ai-btn--ghost" id="ai-edit-retry" '
        'style="display:none" onclick="retryAiEdit()">Try again</button>\n'
        '      <button type="button" class="ai-btn ai-btn--primary" id="ai-edit-generate" '
        'onclick="runAiEdit()">Generate</button>\n'
        '      <button type="button" class="ai-btn ai-btn--primary" id="ai-edit-apply" '
        'style="display:none" onclick="applyAiEdit()">Apply</button>\n'
        '    </div>\n'
        '  </div>\n'
        '</div>'
    )


# The v2 mockup's icon sprite (16x16 line glyphs) — ported verbatim so the panel
# field/pad chrome matches the design contract. Emitted once per editor; referenced
# via <use> by _sym(). Kept separate from the lucide _ICON_PATHS set used elsewhere.
_MOCKUP_SPRITE = (
    '<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>'
    '<symbol id="ic-arrh" viewBox="0 0 16 16"><path d="M2.6 8h10.8M4.6 5.6 2.1 8l2.5 2.4M11.4 5.6 13.9 8l-2.5 2.4"/></symbol>'
    '<symbol id="ic-arrv" viewBox="0 0 16 16"><path d="M8 2.6v10.8M5.6 4.6 8 2.1l2.4 2.5M5.6 11.4 8 13.9l2.4-2.5"/></symbol>'
    '<symbol id="ic-w" viewBox="0 0 16 16"><path d="M2.6 4v8M13.4 4v8M5 8h6M6.1 6.7 4.7 8l1.4 1.3M9.9 6.7 11.3 8l-1.4 1.3"/></symbol>'
    '<symbol id="ic-h" viewBox="0 0 16 16"><path d="M4 2.6h8M4 13.4h8M8 5v6M6.7 6.1 8 4.7l1.3 1.4M6.7 9.9 8 11.3l1.3-1.4"/></symbol>'
    '<symbol id="ic-corner" viewBox="0 0 16 16"><path d="M3.5 13V8A4.5 4.5 0 0 1 8 3.5h5"/></symbol>'
    '<symbol id="ic-up" viewBox="0 0 16 16"><path d="M8 12V4.2M4.6 7.6 8 4.2l3.4 3.4"/></symbol>'
    '<symbol id="ic-down" viewBox="0 0 16 16"><path d="M8 4v7.8M4.6 8.4 8 11.8l3.4-3.4"/></symbol>'
    '<symbol id="ic-left" viewBox="0 0 16 16"><path d="M12 8H4.2M7.6 4.6 4.2 8l3.4 3.4"/></symbol>'
    '<symbol id="ic-right" viewBox="0 0 16 16"><path d="M4 8h7.8M8.4 4.6 11.8 8l-3.4 3.4"/></symbol>'
    '<symbol id="ic-dot" viewBox="0 0 16 16"><circle cx="8" cy="8" r="1.7" fill="currentColor" stroke="none"/></symbol>'
    '<symbol id="ic-comment" viewBox="0 0 16 16"><path d="M2.4 4.6a1.6 1.6 0 0 1 1.6-1.6h8a1.6 1.6 0 0 1 1.6 1.6v4a1.6 1.6 0 0 1-1.6 1.6H7l-3 2.4v-2.4a1.6 1.6 0 0 1-1.6-1.6Z"/></symbol>'
    '</defs></svg>'
)


def _sym(sym_id: str, size: int = 14) -> str:
    """Reference a glyph from the ported mockup sprite (_MOCKUP_SPRITE)."""
    return (
        f'<svg class="ic" width="{size}" height="{size}" viewBox="0 0 16 16" '
        f'fill="none" stroke="currentColor" stroke-width="1.45" stroke-linecap="round" '
        f'stroke-linejoin="round" aria-hidden="true"><use href="#{sym_id}"/></svg>'
    )


def build_editor_html(
    run: Path,
    brand_context: Path | None = None,
    shared_css_override: str | None = None,
    shared_css_dir_override: Path | None = None,
    ai_edit_providers: dict | None = None,
) -> str:
    """Build and return the editor HTML string (testable without a browser).

    Parameters
    ----------
    run:
        The run folder (must exist and contain slides).
    brand_context:
        Override path to ``brand_context/`` directory.  Auto-detected if None.
    shared_css_override:
        If provided, use this string as the ``_shared/styles.css`` content
        instead of reading from disk (used in unit tests).
    shared_css_dir_override:
        If provided, use this Path as the base directory for resolving url()
        references inside the shared CSS content (used in unit tests alongside
        shared_css_override so font @font-face src gets base64-encoded).
    ai_edit_providers:
        studio-ai-edit: ``{"gpt": bool, "gemini": bool}`` presence map resolved
        SERVER-SIDE (content_studio reads the project ``.env`` / os.environ —
        only these booleans ever reach the build). Truthy entries render the
        "Edit with <provider>" buttons in image control groups + the AI modal.
        None / all-false (incl. the standalone static build, which has no server
        to call) → zero AI markup in the output.
    """
    bc = brand_context or _resolve_brand_context(run, None)
    brand_kit = _load_brand_kit(bc)
    tokens_css = build_brand_tokens_css(brand_kit)
    brand_fonts = _brand_fonts(brand_kit)      # pinned on top of per-layer font menus
    palette = _brand_palette(brand_kit)        # global section swatches (Stage A)
    textures = _load_textures()                # per-slide post-production overlays (Addendum 5)

    slides_info = _find_slides_info(run)

    # ── Find _shared/styles.css ──────────────────────────────
    shared_css_content = shared_css_override
    shared_css_dir: Path | None = shared_css_dir_override
    if shared_css_content is None and bc:
        # Check common locations: brand_context/templates/*/shared/ or pack _shared/
        for cand in [
            bc / "templates" / "_shared" / "styles.css",
            bc.parent / "_shared" / "styles.css",
        ]:
            if cand.is_file():
                shared_css_content = cand.read_text(encoding="utf-8", errors="ignore")
                shared_css_dir = cand.parent
                break
    # Also check for _shared/ directly under run/ (test fixture layout)
    if shared_css_content is None:
        run_shared = run / "_shared" / "styles.css"
        if run_shared.is_file():
            shared_css_content = run_shared.read_text(encoding="utf-8", errors="ignore")
            shared_css_dir = run_shared.parent
    if shared_css_content is None:
        shared_css_content = ""

    # ── Build per-slide viewer + panel sections ──────────────
    viewer_sections = []
    panel_sections = []
    present_by_slide: dict[str, set[str]] = {}  # slide_id -> data-slots in its DOM
    slot_bboxes_by_slide: dict[str, list[dict]] = {}  # slide_id -> [{handle,x,y,w,h}] (Stage B)

    for idx, info in enumerate(slides_info):
        sid = info["slide_id"]
        has_template = info.get("template") and info["template"].is_file()
        has_instructions = info.get("instructions") and info["instructions"].is_file()
        present_handles: set[str] | None = None  # data-slots in the rendered slide
        present_order: list[str] = []             # ...in DOM (stacking) order
        data: dict = {}                           # live slot values (set when has_template)

        # Viewer: either iframe srcdoc (template slide) or base64 img (FULL_AI)
        if has_template:
            # Build data dict for fill(). Sample text is the floor (fills any slot
            # the post didn't set); the run's REAL persisted copy (metadata.json
            # `data`, AIOS-139 Addendum 8 #1) overrides it so the editor shows the
            # actual post — matching what `/apply` rebakes (parity).
            data = {}
            if has_instructions:
                try:
                    from render_template import parse_sample_text_from_instructions as _parse_sample  # type: ignore[import]
                    data.update(_parse_sample(info["instructions"]))
                except ImportError:
                    pass
            if isinstance(info.get("data"), dict):
                data.update(info["data"])
            if tokens_css:
                data["BRAND_TOKENS_CSS"] = tokens_css

            # Base64-inline data-driven image slots (keys ending in _PATH, e.g.
            # {{LOGO_PATH}} / {{BG_SOURCE_PATH}}) BEFORE fill(), mirroring
            # render_template.py line ~1050. <iframe srcdoc> has no base URL, so
            # a raw relative path leaks as a broken image; static <img src="..">
            # are handled later by _inline_relative_urls, but a path arriving
            # through a Mustache slot is only resolved here.
            data = embed_paths_as_data_uris(data, bc, info.get("template_dir"))
            # Drop descriptive/unresolved asset paths so optional {{#…_PATH}} blocks
            # collapse instead of rendering a broken <img> (slide-2 ANNOTATION bug).
            data = _blank_unresolved_assets(data)

            # Resolve the shared CSS for THIS slide from its pool's _shared/
            # (template_dir.parent/_shared/styles.css) — the same location
            # render_template.py uses. This carries the brand @font-face, so
            # missing it breaks font parity (Pitfall 1). Fall back to the
            # globally-resolved shared CSS when the pool layout isn't present.
            slide_shared_css = shared_css_content
            slide_shared_dir = shared_css_dir
            _tdir = info.get("template_dir")
            if _tdir is not None:
                _pool_shared = _tdir.parent / "_shared" / "styles.css"
                if _pool_shared.is_file():
                    slide_shared_css = _pool_shared.read_text(encoding="utf-8", errors="ignore")
                    slide_shared_dir = _pool_shared.parent

            try:
                srcdoc_raw = _build_srcdoc(
                    template_path=info["template"],
                    data=data,
                    tokens_css=tokens_css,
                    shared_css_content=slide_shared_css,
                    shared_css_dir=slide_shared_dir,
                    source_template_dir=info.get("source_template_dir"),
                    brand_context=bc,
                )
            except Exception as exc:
                srcdoc_raw = f"<body><p>Error rendering template: {html.escape(str(exc))}</p></body>"

            present_handles = _present_handles(srcdoc_raw)
            present_order = _present_order(srcdoc_raw)
            present_by_slide[sid] = present_handles
            srcdoc_escaped = _html_attr_escape(srcdoc_raw)
            no_slot_banner = (
                f'<div id="no-slot-banner-{sid}" class="no-slot-banner" style="display:none">'
                f'This template has no data-slot handles &mdash; run migrate_data_slots.py'
                f'</div>'
            )
            viewer_html = (
                f'{no_slot_banner}'
                f'<div class="slide-frame-wrap">'
                f'<iframe id="frame-{sid}" class="slide-frame" '
                f'srcdoc="{srcdoc_escaped}" '
                f'sandbox="allow-scripts allow-same-origin" '
                f'title="Slide {sid}"></iframe>'
                f'</div>'
            )
        else:
            # FULL_AI / no template — show base64 PNG as read-only
            if info.get("png_path"):
                img_uri = _b64_img(info["png_path"])
                viewer_html = (
                    f'<div class="read-only-badge">Read-only (full-AI slide)</div>'
                    f'<img class="fullai-img" src="{img_uri}" alt="{sid}">'
                )
            else:
                viewer_html = f'<div class="missing-slide">No slide data for {sid}</div>'

        viewer_sections.append(
            f'<div class="slide-viewer" data-slide="{sid}">'
            f'{viewer_html}'
            f'</div>'
        )

        # Panel: either introspected controls or read-only message
        if has_instructions:
            try:
                slots = parse_slots_from_instructions(info["instructions"])
            except Exception:
                slots = []
            # Add synthetic slots for auto-tagged decoration (bg / svg / logo / frame)
            # that no instructions slot covers, so they get controls + layers too.
            _covered = {_slot_handle(s["name"])[0] for s in slots}
            slots = slots + _synthetic_slots(present_handles or set(), _covered)
            controls_html = _build_panel_controls(slots, sid, present_handles, brand_fonts,
                                                  live_data=data if has_template else None,
                                                  ai_providers=ai_edit_providers)
            layers_html = _build_layers_list(slots, sid, present_handles, present_order)
            slot_bboxes_by_slide[sid] = _slot_bboxes(slots, present_handles)
            if not controls_html.strip():
                controls_html = '<p class="no-slots">No slots found in instructions.md</p>'
            if not layers_html.strip():
                layers_html = '<p class="no-slots">No editable layers on this slide.</p>'
        elif has_template:
            controls_html = (
                '<p class="no-slots">No instructions.md found — '
                'controls cannot be generated for this slide.</p>'
            )
            layers_html = '<p class="no-slots">No layers — add instructions.md.</p>'
        else:
            # Full-AI (flat image) slide: surface the image as ONE selectable layer
            # with the magic-pencil break-into-layers affordance (Addendum 5 Fix #2).
            layers_html, controls_html = _build_fullai_layer_panel(sid)

        panel_sections.append(
            f'<div class="slide-panel" data-slide="{sid}" style="display:none">'
            # selection chip — updated in JS on select (hidden until then)
            f'<div class="selbar" style="display:none">'
            f'<div class="sel-ico">{_icon("layout", 16)}</div>'
            f'<div class="sel-meta"><div class="sel-name">&mdash;</div>'
            f'<div class="sel-sub">Nothing selected</div></div>'
            f'</div>'
            # Layers section
            f'<div class="section">'
            f'<div class="sec-head"><span class="sec-title">Layers</span></div>'
            f'<div class="layers-list layers" data-slide="{sid}">{layers_html}</div>'
            f'</div>'
            # Texture moved to the GLOBAL topbar control (FASE 5) — no longer per-slide here.
            # Inspector — single-scroll, only the selected layer\'s sections show
            f'<div class="inspector">'
            f'<p class="inspector-hint">Select a layer to edit it.</p>'
            f'{controls_html}'
            f'</div>'
            f'</div>'
        )

    viewers_html = "\n".join(viewer_sections)
    panels_html = "\n".join(panel_sections)

    # Initial tweaksState — built now that we know which handles each slide's DOM
    # actually has, so the exported tweaks.json carries no phantom keys.
    # ``pure_defaults`` is the template's natural state; ``initial_state`` is the live
    # tweaksState (defaults + any imported edits). The export diffs against DEFAULTS so
    # only the user's ACTUAL edits ship — applying an unchanged default would force the
    # template off its natural rendering (e.g. shrink a headline to the default cqw)
    # and break the editor==rebake parity. (AIOS-139 review fix)
    pure_defaults = _build_initial_tweaks_state(slides_info, present_by_slide)
    initial_state = json.loads(json.dumps(pure_defaults))   # deep copy

    # Import / resume (Stage B): merge an existing tweaks.json over the computed
    # defaults so re-opening the editor restores prior edits; load comments.json so
    # the pins come back. Both are read from the run folder (the apply-back loop
    # drops them there). Malformed/missing files are ignored.
    def _load_json(name: str):
        p = run / name
        if p.is_file():
            try:
                return json.loads(p.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                return None
        return None

    _saved_tweaks = _load_json("tweaks.json")
    if isinstance(_saved_tweaks, dict):
        for sid, zones in _saved_tweaks.items():
            if not isinstance(zones, dict):
                continue
            base = initial_state.setdefault(sid, {})
            for handle, props in zones.items():
                if isinstance(props, dict):
                    base.setdefault(handle, {}).update(props)
                else:
                    base[handle] = props
    initial_state_json = json.dumps(initial_state, ensure_ascii=False)
    defaults_json = json.dumps(pure_defaults, ensure_ascii=False)

    imported_tweaks_json = json.dumps(
        _saved_tweaks if isinstance(_saved_tweaks, dict) else {}, ensure_ascii=False
    )
    _saved_comments = _load_json("comments.json")
    initial_comments_json = json.dumps(
        _saved_comments if isinstance(_saved_comments, dict) else {}, ensure_ascii=False
    )
    slot_bboxes_json = json.dumps(slot_bboxes_by_slide, ensure_ascii=False)

    # Prev/next nav arrows (only meaningful with >1 slide). prev starts disabled.
    if len(slides_info) > 1:
        nav_html = (
            f'<button id="nav-prev" class="nav-arrow nav-prev" disabled '
            f'onclick="navSlide(-1)" aria-label="Previous slide">'
            f'{_icon("chevron-left", 20)}</button>'
            f'<button id="nav-next" class="nav-arrow nav-next" '
            f'onclick="navSlide(1)" aria-label="Next slide">'
            f'{_icon("chevron-right", 20)}</button>'
        )
    else:
        nav_html = ""

    # LinkedIn-mock chrome: author + caption + carousel dots (mirrors preview_carousel.py)
    brand_name = (brand_kit.get("name") if isinstance(brand_kit, dict) else None) or "Your Brand"
    brand_title = (brand_kit.get("tagline") if isinstance(brand_kit, dict) else None) or "Building in public with Agentic OS"
    # author avatar from the brand's transparent logo, else a gradient chip
    avatar_html = '<div class="li-avatar"></div>'
    if bc is not None:
        _logos_dir = bc / "visual-identity" / "logos"
        if _logos_dir.is_dir():
            _logos = list(_logos_dir.glob("*-transparent.png")) or list(_logos_dir.glob("*.png"))
            if _logos:
                avatar_html = f'<img class="li-avatar" src="{_b64_img(_logos[0])}" alt="" style="object-fit:contain;background:#1a1818">'
    # post caption from caption.md, else a helpful placeholder (still reads like LinkedIn)
    _cap_file = run / "caption.md"
    if _cap_file.is_file():
        _raw = _cap_file.read_text(encoding="utf-8", errors="ignore").strip()
        caption_html = re.sub(r"(#\w+)", r'<span class="tag">\1</span>',
                              html.escape(html.unescape(_raw), quote=False))
    else:
        caption_html = ('Add your post copy to <strong>caption.md</strong> and it renders here, '
                        'just like the real LinkedIn post. <span class="tag">#AgenticOS</span> '
                        '<span class="tag">#BuildInPublic</span>')
    if len(slides_info) > 1:
        _dots = "".join(
            f'<span class="li-dot{" on" if i == 0 else ""}" data-slide-dot="{info["slide_id"]}" '
            f'onclick="goToSlide({i})"></span>'
            for i, info in enumerate(slides_info)
        )
        dots_html = f'<div class="li-dots">{_dots}</div>'
    else:
        dots_html = ""

    # ── Global section: brand palette swatches (Stage A) ─────
    # rounded square + hex beside each, click-to-apply (selected layer's fill, else
    # the global accent), plus a free custom picker. Replaces the hardcoded accent.
    _chips = "".join(
        f'<button type="button" class="swatch-chip" title="{html.escape(label)}" '
        f'onclick="applySwatch(\'{hx}\')">'
        f'<span class="swatch-sq" style="background:{hx}"></span>'
        f'<span class="swatch-hex">{hx.upper()}</span></button>'
        for label, hx in palette
    )
    _custom_default = palette[0][1] if palette else "#5B57D6"
    palette_html = (
        f'<div class="swatch-grid">{_chips}'
        f'<label class="swatch-chip swatch-chip--custom" title="Custom color">'
        f'<span class="swatch-sq swatch-sq--picker"><input type="color" value="{_custom_default}" '
        f'oninput="applySwatch(this.value)"></span>'
        f'<span class="swatch-hex">Custom</span></label>'
        f'</div>'
    )
    if not palette:
        palette_html = (
            '<p class="no-slots" style="padding:0">No brand palette found '
            '(add colors to tokens.json) — use the custom picker.</p>' + palette_html
        )

    # Per-run id so two carousels opened from file:// don't share comment pins.
    run_id = re.sub(r"[^A-Za-z0-9_-]+", "-", run.name) or "run"

    # ── AI edit modal (studio-ai-edit) ────────────────────────
    # Emitted only when the server resolved at least one provider key — a no-key
    # (or static file://) editor carries no AI markup whatsoever.
    ai_modal_html = (
        _build_ai_edit_modal() if any((ai_edit_providers or {}).values()) else ""
    )

    # ── Inject initial state into JS via sentinel replace ────
    editor_js = (
        _EDITOR_JS
        .replace("__TWEAKS_INIT_JSON__", initial_state_json)
        .replace("__SLOT_BBOXES_JSON__", slot_bboxes_json)
        .replace("__INITIAL_COMMENTS_JSON__", initial_comments_json)
        .replace("__IMPORTED_TWEAKS_JSON__", imported_tweaks_json)
        .replace("__DEFAULTS_JSON__", defaults_json)
    )

    # ──────────────────────────────────────────────────────────
    # Final HTML assembly
    # ──────────────────────────────────────────────────────────
    _shell_fonts_link = build_google_fonts_link()
    out = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Live Editor</title>
{_shell_fonts_link}
<style>
  :root {{
    /* Editor v2 panel identity (mockup contract: clean neutrals + indigo accent).
       Panel UI fonts are panel-only system-fallback stacks (Hanken Grotesk / DM
       Mono if installed, else system UI / mono) — no network <link>, and the slide
       lives in an isolated <iframe> so these never bleed into the composition. */
    --bg: #FCF9F7;          /* stage = command-centre cream */
    --surface: #ffffff;     /* topbar / chrome shell (panel overrides this dark) */
    --card: #ffffff;        /* control cards */
    --card-hi: #faf9f7;
    --line: #E7E4DF;        /* border */
    --line-soft: #EDEBE6;   /* hairline */
    --ink: #1B1C1B;         /* command-centre ink */
    --muted: #6E6A63;       /* secondary text */
    --faint: #A29D94;
    --accent: #6366F1;      /* command-centre indigo accent (selection) */
    --accent-press: #4F52E0;
    --accent-soft: #ECEBFB;
    --terra-a: #93452A;     /* command-centre terracotta — primary CTA gradient */
    --terra-b: #B25D3F;
    --shadow: 0 12px 32px rgba(147,69,42,.06);  /* soft command-centre shadow */
    --danger: #C7493B;
    --field: #F6F5F2;       /* input background */
    --field-2: #F0EEEA;
    --field-focus: #ffffff; /* input bg on focus (panel overrides this dark) */
    --pad-bg: #ffffff;      /* nudge-pad button bg (panel overrides this dark) */
    --hover: rgba(0,0,0,.05);
    --field-h: 30px;
    --sans: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    --label: "Space Grotesk", "Inter", -apple-system, "Segoe UI", sans-serif;
    --ui: "Hanken Grotesk", -apple-system, system-ui, "Segoe UI", sans-serif;
    --mono: "DM Mono", ui-monospace, "SFMono-Regular", Consolas, monospace;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: var(--sans); background: var(--bg); color: var(--ink); -webkit-font-smoothing: antialiased; }}
  .ic {{ vertical-align: middle; flex: 0 0 auto; }}
  ::-webkit-scrollbar {{ width: 10px; height: 10px; }}
  ::-webkit-scrollbar-thumb {{ background: #d8d0ca; border-radius: 6px; border: 2px solid var(--surface); }}
  ::-webkit-scrollbar-track {{ background: transparent; }}

  .app {{ display: grid; grid-template-rows: 64px 1fr; height: 100vh; overflow: hidden; }}
  /* ── Top bar (command-centre: cream, logo left, left-clustered pill actions) ── */
  .topbar {{ display: flex; align-items: center; gap: 14px; padding: 0 18px;
             border-bottom: 1px solid var(--line); background: var(--bg); }}
  .brand {{ display: flex; align-items: center; flex: 0 0 auto; }}
  .brand-logo {{ width: 28px; height: 28px; display: block; }}
  /* the action pills (studio.js fills this) sit immediately after the logo, left-clustered */
  .topbar-actions {{ display: flex; align-items: center; gap: 6px; padding-left: 6px;
                     border-left: 1px solid var(--line); margin-left: 4px; }}
  .slide-counter {{ margin-left: auto; font-family: var(--label); font-size: 12px; font-weight: 600;
                    letter-spacing: .04em; color: var(--muted); }}
  .slide-counter #slide-counter-cur {{ color: var(--terra-a); }}

  .workspace {{ display: grid; grid-template-columns: 1fr 400px; height: calc(100vh - 64px); overflow: hidden; }}
  /* ── Stage (LinkedIn mock) ────────────────────────────── */
  /* center the mock both axes; `safe center` keeps the top (the caption) scroll-reachable
     when the mock is taller than the stage (FASE 6 #4) instead of clipping it. */
  .stage {{ overflow: auto; display: flex; align-items: safe center; justify-content: center;
            padding: 20px 28px; background: var(--bg); }}
  .li-post {{ width: 440px; background: #fff; color: #1b1b1b; border-radius: 14px; overflow: hidden;
              box-shadow: var(--shadow), 0 10px 30px rgba(27,28,27,.10);
              font-family: var(--sans); flex: 0 0 auto; }}
  .li-head {{ display: flex; align-items: center; gap: 8px; padding: 12px 16px; }}
  .li-avatar {{ width: 48px; height: 48px; border-radius: 50%; flex: 0 0 auto;
                background: linear-gradient(135deg, #cf6a47 0%, #7a2f1a 100%); }}
  .li-who {{ line-height: 1.25; }}
  .li-name {{ font-weight: 600; font-size: 14px; color: #1b1b1b; }}
  .li-sub {{ color: #666; font-size: 12px; }}
  .li-viewer {{ position: relative; background: #000; line-height: 0; overflow: hidden;
                touch-action: pan-y; cursor: grab; }}
  .li-viewer:active {{ cursor: grabbing; }}
  .carousel-track {{ display: flex; transition: transform 340ms cubic-bezier(.22,.61,.36,1);
                     will-change: transform; }}
  .carousel-track.dragging {{ transition: none; }}
  .slide-viewer {{ flex: 0 0 100%; position: relative; }}
  .slide-frame-wrap {{ width: 440px; height: 550px; overflow: hidden; position: relative;
                       background: #000; margin: 0 auto; }}
  .slide-frame {{ width: 1080px; height: 1350px; border: none; display: block; background: #fff;
                  transform-origin: top left; transform: scale(0.407407); pointer-events: none; }}
  /* prev/next arrows over the slide (mirrors preview_carousel.py .nav) */
  .nav-arrow {{ position: absolute; top: 50%; transform: translateY(-50%); width: 38px; height: 38px;
                border-radius: 50%; border: none; background: rgba(255,255,255,.92); color: #1b1b1b;
                display: flex; align-items: center; justify-content: center; cursor: pointer;
                box-shadow: 0 1px 6px rgba(0,0,0,.35); z-index: 4; transition: opacity 120ms ease; }}
  .nav-arrow:hover {{ background: #fff; }}
  .nav-arrow[disabled] {{ opacity: .28; cursor: default; }}
  .nav-prev {{ left: 12px; }}
  .nav-next {{ right: 12px; }}
  .fullai-img {{ width: 440px; height: auto; display: block; }}
  .li-dots {{ display: flex; gap: 6px; justify-content: center; padding: 10px; background: #fff; }}
  .li-dot {{ width: 7px; height: 7px; border-radius: 50%; background: #c9c7c3; cursor: pointer;
             transition: background 120ms ease, transform 120ms ease; }}
  .li-dot:hover {{ transform: scale(1.25); }}
  .li-dot.on {{ background: #0a66c2; }}
  .li-title {{ color: #666; font-size: 12px; }}
  .li-meta {{ color: #666; font-size: 12px; display: flex; align-items: center; gap: 3px; }}
  .li-deg {{ color: #666; font-weight: 400; }}
  /* editable caption (FASE 6 #5) — feeds the Zernio publish `content`. */
  .li-caption[contenteditable] {{ outline: none; border-radius: 8px; transition: box-shadow .15s, background .15s; }}
  .li-caption[contenteditable]:hover {{ background: #faf9f7; }}
  .li-caption[contenteditable]:focus {{ background: #fff; box-shadow: 0 0 0 2px rgba(99,102,241,.35); }}
  .li-caption:empty::before {{ content: attr(data-ph); color: #9aa0a6; }}
  .li-caption {{ padding: 4px 16px 12px; font-size: 14px; line-height: 1.45; color: #1b1b1b;
                 background: #fff; white-space: pre-wrap; }}
  .li-caption .tag {{ color: #0a66c2; font-weight: 600; }}
  .li-react {{ display: flex; justify-content: space-between; padding: 10px 16px 8px;
               color: #666; font-size: 13px; background: #fff; }}
  .li-actions {{ display: flex; padding: 4px 8px 8px; background: #fff; border-top: 1px solid #e6e4e1; }}
  .li-act {{ flex: 1; display: flex; align-items: center; justify-content: center; gap: 7px;
             padding: 10px 4px; border: none; background: transparent; color: #5f6368;
             font-size: 14px; font-weight: 600; cursor: pointer; border-radius: 6px; }}
  .li-act:hover {{ background: #f3f2ef; }}
  .li-act .ic {{ color: #5f6368; }}
  .read-only-badge {{ font-size: 11px; color: #fff; background: rgba(0,0,0,.55); line-height: 1.4;
                      padding: 4px 10px; text-align: center; }}
  .missing-slide {{ color: #fff; font-size: 13px; padding: 40px; text-align: center; }}
  .no-slot-banner {{ background: #fff3cd; border: 1px solid #ffc107; border-radius: 6px;
                     padding: 8px 12px; font-size: 12px; color: #856404; margin: 8px; }}

  /* ── Panel shell (v2 mockup dock) ────────────────────── */
  /* command-centre: cream stage + a floating, vertically-centered, DETACHED dark panel
     (per the sketch). The panel re-maps the semantic vars to a dark scheme so every
     descendant card/field/label flips with no per-element rewrite. */
  .panel {{ overflow-y: auto; overflow-x: hidden; display: flex; flex-direction: column;
            font-family: var(--ui);
            align-self: center; margin: 0 20px; max-height: calc(100vh - 96px);
            border-radius: 18px;
            --surface: #1F2020; --card: #272826; --card-hi: #2F302D;
            --field: #2A2B28; --field-2: #34352F; --field-focus: #3A3B37; --pad-bg: #34352F;
            --line: #3A3B36; --line-soft: #2F302C; --hover: rgba(255,255,255,.07);
            --ink: #F3EFEA; --muted: #BDB7AC; --faint: #8C877D;
            --accent-soft: rgba(99,102,241,.22);
            /* depth + glow (FASE 5): vertical sheen, hairline indigo ring, layered drop
               shadow with a warm + indigo cast, and a soft outer glow. */
            background: linear-gradient(180deg, #242523 0%, #1B1C1B 100%);
            box-shadow:
              inset 0 1px 0 rgba(255,255,255,.05),
              0 0 0 1px rgba(99,102,241,.10),
              0 28px 64px -16px rgba(27,28,27,.50),
              0 10px 28px rgba(147,69,42,.10),
              0 0 48px -10px rgba(99,102,241,.20); }}
  .panel-head {{ display: flex; align-items: center; gap: 8px; padding: 12px 14px;
                 border-bottom: 1px solid var(--line-soft); font-size: 13px; font-weight: 700;
                 letter-spacing: -.01em; color: var(--ink); }}
  .panel-head .ic {{ color: var(--accent); }}
  .panel input, .panel select, .panel textarea {{ font-family: var(--ui); color: var(--ink); }}
  select {{ appearance: none; -webkit-appearance: none; cursor: pointer; }}

  /* ── Global section ──────────────────────────────────── */
  .global-section {{ padding: 12px 14px; border-bottom: 1px solid var(--line-soft);
                     display: flex; flex-direction: column; gap: 10px; }}
  .card-label {{ display: flex; align-items: center; gap: 6px; font-family: var(--label);
                 font-size: 10px; font-weight: 700; letter-spacing: .1em; text-transform: uppercase;
                 color: var(--faint); }}
  .card-label .ic {{ color: var(--faint); }}
  .global-section > label {{ display: block; font-size: 11px; color: var(--muted); }}
  .global-section input[type=text], .global-section select {{ width: 100%; height: var(--field-h);
                 margin-top: 5px; background: var(--field); border: 1px solid transparent; border-radius: 6px;
                 padding: 0 9px; font-size: 12px; }}
  .global-section input[type=text]:focus, .global-section select:focus {{ outline: none;
                 background: var(--field-focus); border-color: var(--accent); box-shadow: 0 0 0 2.5px var(--accent-soft); }}
  .global-section input[type=color] {{ width: 100%; height: 30px; margin-top: 5px; padding: 2px;
                 border: 1px solid var(--line); border-radius: 6px; cursor: pointer; background: var(--field); }}
  .toggle-label {{ display: flex; align-items: center; gap: 9px; font-size: 12px; color: var(--ink); cursor: pointer; }}
  .toggle-label input {{ width: auto; margin: 0; accent-color: var(--accent); }}
  /* brand palette swatches (Stage A) */
  .swatch-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 6px; }}
  .swatch-chip {{ display: flex; align-items: center; gap: 8px; height: 30px; padding: 0 8px;
                  background: var(--field); border: 1px solid transparent; border-radius: 6px;
                  cursor: pointer; transition: border-color .12s, background .12s; font-family: var(--ui); }}
  .swatch-chip:hover {{ background: var(--field-2); border-color: var(--line); }}
  .swatch-sq {{ position: relative; width: 18px; height: 18px; border-radius: 5px; flex: none; overflow: hidden;
                box-shadow: inset 0 0 0 1px rgba(0,0,0,.12); }}
  .swatch-sq--picker {{ background-image: conic-gradient(from 0deg, #f00, #ff0, #0f0, #0ff, #00f, #f0f, #f00); }}
  .swatch-sq--picker input[type=color] {{ position: absolute; inset: -4px; width: calc(100% + 8px);
                height: calc(100% + 8px); border: none; padding: 0; margin: 0; cursor: pointer; background: transparent; }}
  .swatch-hex {{ font-family: var(--mono); font-size: 11px; color: var(--muted); letter-spacing: .2px;
                 white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}

  /* ── Selection chip ──────────────────────────────────── */
  .selbar {{ display: flex; align-items: center; gap: 9px; padding: 10px 14px;
             border-bottom: 1px solid var(--line-soft); }}
  .sel-ico {{ width: 28px; height: 28px; border-radius: 7px; flex: none; background: var(--accent-soft);
              color: var(--accent); display: flex; align-items: center; justify-content: center; }}
  .sel-name {{ font-size: 13px; font-weight: 600; color: var(--ink); line-height: 1.2; }}
  .sel-sub {{ font-size: 11px; color: var(--faint); margin-top: 1px; font-family: var(--mono); }}

  /* ── Sections + fields ───────────────────────────────── */
  .section {{ padding: 14px; border-bottom: 1px solid var(--line-soft); }}
  .sec-head {{ display: flex; align-items: center; justify-content: space-between; margin-bottom: 11px; }}
  .sec-title {{ display: block; font-size: 13px; font-weight: 600; letter-spacing: -.2px; color: var(--ink); margin: 8px 0 9px; }}
  .control-group > .sec-title:first-of-type {{ margin-top: 0; }}
  .label {{ font-size: 11px; font-weight: 500; color: var(--faint); letter-spacing: .2px; margin-bottom: 6px; display: block; }}
  .sec-sub {{ margin-bottom: 8px; }}
  .grid2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }}
  .field {{ display: flex; align-items: center; gap: 6px; height: var(--field-h); background: var(--field);
            border: 1px solid transparent; border-radius: 6px; padding: 0 9px; color: var(--muted);
            transition: border-color .12s, background .12s; }}
  .field:hover {{ background: var(--field-2); }}
  .field:focus-within {{ background: var(--field-focus); border-color: var(--accent); box-shadow: 0 0 0 2.5px var(--accent-soft); }}
  .field .ic {{ color: var(--faint); }}
  .field:focus-within .ic {{ color: var(--accent); }}
  .field input {{ border: none; background: transparent; outline: none; width: 100%; min-width: 0;
                  font-family: var(--mono); font-size: 12px; font-weight: 500; color: var(--ink); letter-spacing: -.2px; padding: 0; }}
  .field .unit {{ font-family: var(--mono); font-size: 11px; color: var(--faint); flex: none; }}
  input[type=number] {{ -moz-appearance: textfield; }}
  input[type=number]::-webkit-inner-spin-button, input[type=number]::-webkit-outer-spin-button {{ -webkit-appearance: none; margin: 0; }}
  .content-area {{ width: 100%; background: var(--field); border: 1px solid transparent; border-radius: 6px;
                   padding: 7px 9px; font-size: 12px; font-family: var(--ui); color: var(--ink); resize: vertical; line-height: 1.45; }}
  .content-area:focus {{ outline: none; background: var(--field-focus); border-color: var(--accent); box-shadow: 0 0 0 2.5px var(--accent-soft); }}
  .select {{ position: relative; display: flex; align-items: center; height: var(--field-h); background: var(--field);
             border: 1px solid transparent; border-radius: 6px; }}
  .select:hover {{ background: var(--field-2); }}
  .select:focus-within {{ background: var(--field-focus); border-color: var(--accent); box-shadow: 0 0 0 2.5px var(--accent-soft); }}
  .select select {{ border: none; background: transparent; outline: none; width: 100%; height: 100%;
                    padding: 0 26px 0 10px; cursor: pointer; font-size: 12.5px; font-weight: 500; color: var(--ink); }}
  .select .chev {{ position: absolute; right: 8px; color: var(--faint); pointer-events: none; display: flex; }}
  /* custom select trigger — readable in the dark panel, replaces native <select> */
  .csel-trigger {{ display: flex; align-items: center; width: 100%; height: var(--field-h);
                   background: var(--field); border: 1px solid transparent; border-radius: 6px;
                   padding: 0 6px 0 10px; cursor: pointer; font-size: 12.5px; font-weight: 500;
                   color: var(--ink); font-family: var(--ui); text-align: left; gap: 4px; }}
  .csel-trigger:hover {{ background: var(--field-2); }}
  .csel-trigger:focus {{ outline: none; background: var(--field-focus); border-color: var(--accent);
                          box-shadow: 0 0 0 2.5px var(--accent-soft); }}
  .csel-val {{ flex: 1; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}
  /* floating popup for editor custom dropdowns */
  .ed-pop {{ position: fixed; z-index: 100001; background: #fff; color: #1B1C1B; border-radius: 12px;
             padding: 8px; box-shadow: 0 12px 36px rgba(27,28,27,.22),0 0 0 1px rgba(27,28,27,.07);
             font: 500 13px 'Hanken Grotesk',system-ui,sans-serif;
             max-height: 280px; overflow-y: auto; width: 220px; display: none; }}
  .ed-pop h4 {{ margin: 4px 0 6px; font: 700 10px/1 'Space Grotesk',sans-serif;
                letter-spacing: .12em; text-transform: uppercase; color: #A29D94; padding: 0 4px; }}
  .ed-pop h4:not(:first-child) {{ margin-top: 12px; }}
  .ed-opt {{ display: block; width: 100%; text-align: left; border: none; background: transparent;
             padding: 7px 9px; border-radius: 8px; cursor: pointer; color: #1B1C1B;
             font: 500 13px 'Hanken Grotesk',system-ui,sans-serif; }}
  .ed-opt:hover {{ background: #F4F2EE; }}
  .ed-opt.sel {{ background: #ECEBFB; color: #4F52E0; }}

  /* ── Move pad + step ─────────────────────────────────── */
  .move {{ display: flex; align-items: center; gap: 12px; margin-top: 10px; background: var(--field); border-radius: 8px; padding: 9px 11px; }}
  .pad {{ display: grid; grid-template-columns: repeat(3, 24px); grid-template-rows: repeat(3, 24px); gap: 2px; flex: none; }}
  .pad-btn {{ border: none; background: var(--pad-bg); border-radius: 5px; color: var(--muted); cursor: pointer;
              display: flex; align-items: center; justify-content: center; padding: 0; box-shadow: 0 1px 0 rgba(0,0,0,.02); }}
  .pad-btn:hover {{ background: var(--accent); color: #fff; }}
  .pad-btn:active {{ background: var(--accent-press); transform: translateY(.5px); }}
  .pad-btn:disabled {{ opacity: .4; cursor: default; background: var(--pad-bg); color: var(--faint); }}
  .pad .pu {{ grid-area: 1/2; }} .pad .pl {{ grid-area: 2/1; }} .pad .pr {{ grid-area: 2/3; }} .pad .pd {{ grid-area: 3/2; }}
  .pad-dot {{ grid-area: 2/2; display: flex; align-items: center; justify-content: center; color: var(--faint); }}
  .move-meta {{ display: flex; flex-direction: column; gap: 7px; min-width: 0; }}
  .mlabel {{ font-size: 11px; color: var(--faint); font-weight: 500; }}
  .step {{ display: flex; gap: 2px; background: var(--field-2); border-radius: 7px; padding: 2px; }}
  .step label {{ flex: 1; text-align: center; font-family: var(--mono); font-size: 11px; color: var(--muted);
                 padding: 4px 0; border-radius: 5px; cursor: pointer; position: relative; font-weight: 500; }}
  .step label:hover {{ color: var(--ink); }}
  .step input {{ position: absolute; opacity: 0; width: 0; height: 0; }}
  .step label:has(:checked) {{ background: var(--field-focus); color: var(--accent); box-shadow: 0 1px 2px rgba(0,0,0,.06); }}
  .step .su {{ opacity: .5; }}

  /* ── Opacity slider + pct ────────────────────────────── */
  .opacity-row {{ display: flex; align-items: center; gap: 9px; }}
  .slider {{ flex: 1 1 auto; position: relative; height: var(--field-h); display: flex; align-items: center; }}
  .slider input[type=range] {{ -webkit-appearance: none; appearance: none; width: 100%; height: 5px; border-radius: 4px;
            outline: none; margin: 0; box-shadow: inset 0 0 0 1px var(--line);
            background: linear-gradient(90deg, var(--accent) 0 var(--p,100%), var(--field-2) var(--p,100%) 100%); }}
  .slider input[type=range]::-webkit-slider-thumb {{ -webkit-appearance: none; width: 15px; height: 15px; border-radius: 50%;
            background: #fff; cursor: pointer; box-shadow: 0 1px 3px rgba(0,0,0,.22), 0 0 0 1px rgba(0,0,0,.06); }}
  .pct {{ width: 64px; flex: none; display: flex; align-items: center; gap: 3px; height: var(--field-h);
          background: var(--field); border: 1px solid transparent; border-radius: 6px; padding: 0 9px; }}
  .pct:focus-within {{ background: var(--field-focus); border-color: var(--accent); box-shadow: 0 0 0 2.5px var(--accent-soft); }}
  .pct input {{ border: none; background: transparent; outline: none; width: 100%; font-family: var(--mono);
                font-size: 12px; font-weight: 500; color: var(--ink); padding: 0; }}
  .pct .unit {{ font-family: var(--mono); font-size: 11px; color: var(--faint); }}

  /* ── Generic range rows (font-size / tilt / stroke weight) ── */
  .ctrl-row {{ display: grid; grid-template-columns: 74px 1fr 32px; align-items: center; gap: 10px; margin-bottom: 11px; }}
  .ctrl-row:last-child {{ margin-bottom: 0; }}
  .ctrl-name {{ font-size: 11px; color: var(--muted); white-space: nowrap; }}
  .ctrl-row input[type=range] {{ -webkit-appearance: none; appearance: none; width: 100%; height: 5px; border-radius: 4px;
            background: var(--field-2); box-shadow: inset 0 0 0 1px var(--line); outline: none; cursor: pointer; }}
  .ctrl-row input[type=range]::-webkit-slider-thumb {{ -webkit-appearance: none; width: 14px; height: 14px; border-radius: 50%;
            background: #fff; border: 2px solid var(--accent); box-shadow: 0 1px 2px rgba(0,0,0,.18); }}
  .range-val {{ font-size: 11px; color: var(--faint); text-align: right; font-variant-numeric: tabular-nums; font-family: var(--mono); }}

  /* ── Fill / colour rows ──────────────────────────────── */
  .colorrow {{ display: flex; align-items: center; gap: 8px; height: var(--field-h); }}
  .swatch {{ position: relative; width: 24px; height: 24px; border-radius: 6px; flex: none; overflow: hidden;
             box-shadow: inset 0 0 0 1px rgba(0,0,0,.12); cursor: pointer; }}
  .swatch input[type=color] {{ position: absolute; inset: -4px; width: calc(100% + 8px); height: calc(100% + 8px);
             border: none; padding: 0; margin: 0; cursor: pointer; background: transparent; }}
  .hex {{ flex: 1 1 auto; display: flex; align-items: center; height: var(--field-h); background: var(--field);
          border: 1px solid transparent; border-radius: 6px; padding: 0 9px; }}
  .hex:focus-within {{ background: var(--field-focus); border-color: var(--accent); box-shadow: 0 0 0 2.5px var(--accent-soft); }}
  .hex .hash {{ font-family: var(--mono); font-size: 12px; color: var(--faint); margin-right: 2px; }}
  .hex input {{ border: none; background: transparent; outline: none; width: 100%; font-family: var(--mono);
                font-size: 12px; font-weight: 500; color: var(--ink); text-transform: uppercase; letter-spacing: .3px; padding: 0; }}
  .corner-field .field {{ max-width: 55%; }}

  /* ── Slot badge + header ─────────────────────────────── */
  .control-group-header {{ display: flex; align-items: center; gap: 8px; margin-bottom: 12px;
                           font-size: 12px; font-weight: 700; color: var(--ink); }}
  .slot-badge {{ display: inline-flex; align-items: center; gap: 4px; font-family: var(--label); font-size: 9px;
                 padding: 3px 8px; border-radius: 6px; font-weight: 700; text-transform: uppercase; letter-spacing: .06em;
                 background: var(--accent-soft); color: var(--accent); }}
  .slot-badge .ic {{ width: 11px; height: 11px; }}
  details.stroke-sub {{ border-top: 1px solid var(--line-soft); padding-top: 10px; margin-top: 4px; }}
  details.stroke-sub > summary {{ list-style: none; cursor: pointer; }}
  details.stroke-sub > summary::-webkit-details-marker {{ display: none; }}

  /* ── Layers list (lock + eye) ────────────────────────── */
  .layers-list {{ display: flex; flex-direction: column; gap: 1px; }}
  .layer-row {{ display: flex; align-items: center; gap: 9px; border-radius: 7px; padding: 0 4px 0 7px;
                height: 32px; cursor: pointer; transition: background .12s; }}
  .layer-row:hover {{ background: var(--field); }}
  .layer-row.sel {{ background: var(--accent-soft); }}
  .layer-row.sel .layer-ico, .layer-row.sel .layer-name {{ color: var(--accent); }}
  .layer-row.sel .layer-name {{ font-weight: 600; }}
  .layer-row.drag {{ opacity: .4; }}
  .layer-row.locked {{ opacity: .6; }}
  .layer-grip {{ color: #cdc8c0; font-size: 11px; letter-spacing: -4px; cursor: grab; user-select: none; flex: none; }}
  .layer-ico {{ color: var(--faint); display: flex; flex: none; }}
  .layer-name {{ flex: 1; font-size: 12.5px; color: var(--muted); font-weight: 500; white-space: nowrap;
                 overflow: hidden; text-overflow: ellipsis; }}
  .layer-actions {{ display: flex; align-items: center; gap: 1px; flex: none; opacity: 0; transition: opacity .1s; }}
  .layer-row:hover .layer-actions, .layer-row.sel .layer-actions,
  .layer-row[data-locked="1"] .layer-actions, .layer-row:has(.layer-eye.off) .layer-actions {{ opacity: 1; }}
  .actbtn {{ width: 24px; height: 24px; border-radius: 6px; display: flex; align-items: center; justify-content: center;
             color: var(--faint); cursor: pointer; background: transparent; border: none; padding: 0; }}
  .actbtn:hover {{ background: var(--hover); color: var(--ink); }}
  .actbtn .eye-off, .actbtn .lk-on {{ display: none; }}
  .layer-eye.off .eye-on {{ display: none; }} .layer-eye.off .eye-off {{ display: flex; }}
  .actbtn--lk[data-on="1"] {{ color: var(--accent); }}
  .actbtn--lk[data-on="1"] .lk-off {{ display: none; }} .actbtn--lk[data-on="1"] .lk-on {{ display: flex; }}

  /* ── Inspector (selection-driven) ────────────────────── */
  .inspector-hint {{ color: var(--faint); font-size: 12px; padding: 14px; }}
  .control-group {{ padding: 14px; border-bottom: 1px solid var(--line-soft); }}
  .inspector .control-group {{ display: none; }}   /* only the selected layer's sections show */
  .control-group.locked {{ opacity: .55; pointer-events: none; }}

  /* ── Full-AI image: layer row magic-pencil + decompose-only disclaimer ── */
  .layer-magic {{ color: var(--accent); }}
  .layer-magic:hover {{ background: rgba(91,87,214,.10); color: var(--accent); }}
  .fullai-note {{ display: flex; gap: 10px; align-items: flex-start;
                  background: rgba(91,87,214,.06); border: 1px solid rgba(91,87,214,.18);
                  border-radius: 10px; padding: 12px; margin-bottom: 12px; }}
  .fullai-note-ico {{ color: var(--accent); flex: 0 0 auto; margin-top: 1px; }}
  .fullai-note p {{ margin: 0; font-size: 12px; line-height: 1.45; color: var(--ink); }}
  .magic-break-btn {{ display: flex; align-items: center; gap: 8px; width: 100%;
                      justify-content: center; border: none; border-radius: 9px;
                      padding: 9px 12px; cursor: pointer; font-weight: 600; font-size: 13px;
                      color: #fff; background: var(--accent); }}
  .magic-break-btn:hover {{ filter: brightness(1.06); }}

  /* ── Replace image (r5f F5) ──────────────────────────── */
  .replace-img-btn {{ display: flex; align-items: center; gap: 8px; width: 100%;
                      justify-content: center; border: 1px solid var(--line);
                      border-radius: 9px; padding: 8px 12px; cursor: pointer;
                      font-family: var(--ui); font-weight: 600; font-size: 12.5px;
                      color: var(--ink); background: var(--surface); }}
  .replace-img-btn:hover {{ border-color: var(--accent); color: var(--accent); }}

  /* ── AI edit (studio-ai-edit): provider buttons + modal ── */
  .ai-edit-sub {{ display: flex; flex-direction: column; gap: 6px; }}
  .ai-edit-btn {{ display: flex; align-items: center; gap: 8px; width: 100%;
                  justify-content: center; border: 1px solid var(--line);
                  border-radius: 9px; padding: 8px 12px; cursor: pointer;
                  font-family: var(--ui); font-weight: 600; font-size: 12.5px;
                  color: var(--ink); background: var(--surface); }}
  .ai-edit-btn:hover {{ border-color: var(--accent); color: var(--accent); }}
  /* the modal sits on the LIGHT stage (above ed-pop), so its colours are fixed */
  .ai-modal-overlay {{ position: fixed; inset: 0; z-index: 100002; display: none;
                       align-items: center; justify-content: center;
                       background: rgba(27,28,27,.55); }}
  .ai-modal {{ width: 560px; max-width: calc(100vw - 48px); max-height: calc(100vh - 48px);
               overflow-y: auto; background: #fff; color: #1B1C1B; border-radius: 16px;
               box-shadow: 0 24px 64px rgba(27,28,27,.35); padding: 18px;
               font-family: var(--ui); }}
  .ai-modal-head {{ display: flex; align-items: center; justify-content: space-between;
                    margin-bottom: 12px; }}
  .ai-modal-title {{ display: flex; align-items: center; gap: 8px; font-size: 15px;
                     font-weight: 700; }}
  .ai-modal-close {{ border: none; background: transparent; cursor: pointer; color: #6E6A63;
                     font-size: 15px; line-height: 1; padding: 5px 9px; border-radius: 7px; }}
  .ai-modal-close:hover {{ background: #F4F2EE; color: #1B1C1B; }}
  .ai-modal-imgs {{ display: flex; gap: 12px; margin-bottom: 12px; }}
  .ai-modal-imgs figure {{ flex: 1; min-width: 0; margin: 0; }}
  .ai-modal-imgs img {{ width: 100%; border-radius: 10px; border: 1px solid #E7E4DF;
                        background: #F6F5F2; display: block; min-height: 40px; }}
  .ai-modal-imgs figcaption {{ font-size: 11px; color: #6E6A63; margin-top: 5px;
                               text-align: center; }}
  #ai-edit-prompt {{ width: 100%; min-height: 64px; resize: vertical; border: 1px solid #E7E4DF;
                     border-radius: 9px; padding: 9px 11px; font-family: var(--ui);
                     font-size: 13px; color: #1B1C1B; background: #fff; }}
  #ai-edit-prompt:focus {{ outline: none; border-color: var(--accent);
                           box-shadow: 0 0 0 2.5px var(--accent-soft); }}
  #ai-edit-prompt:disabled {{ background: #F6F5F2; color: #6E6A63; }}
  .ai-modal-status {{ display: flex; align-items: center; gap: 8px; min-height: 22px;
                      font-size: 12px; color: #6E6A63; margin: 8px 0 4px; }}
  .ai-modal-status.err {{ color: var(--danger); }}
  .ai-spinner {{ width: 14px; height: 14px; border-radius: 50%; flex: none;
                 border: 2px solid #E7E4DF; border-top-color: var(--accent);
                 animation: ai-spin .8s linear infinite; }}
  @keyframes ai-spin {{ to {{ transform: rotate(360deg); }} }}
  .ai-modal-actions {{ display: flex; gap: 8px; justify-content: flex-end; margin-top: 10px; }}
  .ai-btn {{ height: 32px; border-radius: 8px; border: none; cursor: pointer;
             font-family: var(--ui); font-size: 13px; font-weight: 600; padding: 0 14px; }}
  .ai-btn:disabled {{ opacity: .5; cursor: default; }}
  .ai-btn--primary {{ background: var(--accent); color: #fff; }}
  .ai-btn--primary:hover:not(:disabled) {{ background: var(--accent-press); }}
  .ai-btn--ghost {{ background: transparent; color: #6E6A63; }}
  .ai-btn--ghost:hover:not(:disabled) {{ background: #F4F2EE; color: #1B1C1B; }}
  /* reference images (ai-edit-multi-input) */
  .ai-ref-block {{ margin: 4px 0 10px; }}
  .ai-ref-head {{ display: flex; align-items: center; justify-content: space-between; }}
  .ai-ref-label {{ font-size: 11px; color: #6E6A63; font-weight: 600; }}
  .ai-ref-count {{ color: #9b958c; font-weight: 500; }}
  .ai-ref-add {{ height: 26px; padding: 0 10px; font-size: 12px; }}
  .ai-ref-thumbs {{ display: flex; flex-wrap: wrap; gap: 7px; margin-top: 8px; }}
  .ai-ref-thumb {{ position: relative; width: 52px; height: 52px; }}
  .ai-ref-thumb img {{ width: 52px; height: 52px; object-fit: cover; border-radius: 8px;
                       border: 1px solid #E7E4DF; background: #F6F5F2; display: block; }}
  .ai-ref-x {{ position: absolute; top: -6px; right: -6px; width: 18px; height: 18px;
               border-radius: 50%; border: none; cursor: pointer; background: #1B1C1B;
               color: #fff; font-size: 9px; line-height: 1; padding: 0;
               display: flex; align-items: center; justify-content: center; }}
  .ai-ref-x:hover:not(:disabled) {{ background: var(--danger); }}
  .ai-ref-x:disabled {{ opacity: .5; cursor: default; }}
  .ai-gemini-tag {{ font-size: 12px; color: #8a5a00; background: #FFF4DE;
                    border: 1px solid #F2D89B; border-radius: 8px; padding: 8px 11px;
                    margin: 2px 0 10px; line-height: 1.4; }}

  /* ── Export bar ──────────────────────────────────────── */
  .export-bar {{ margin-top: auto; border-top: 1px solid var(--line); padding: 14px; background: var(--surface);
                 position: sticky; bottom: 0; }}
  .export-btn {{ display: flex; align-items: center; justify-content: center; gap: 8px; width: 100%; padding: 11px;
                 background: var(--accent); color: #fff; border: none; border-radius: 9px; font-family: var(--ui);
                 font-size: 13px; font-weight: 600; cursor: pointer; transition: background .12s, transform .08s; }}
  .export-btn:hover {{ background: var(--accent-press); }}
  .export-btn:active {{ transform: scale(.99); }}
  #export-note {{ font-size: 11px; color: var(--muted); margin-top: 8px; min-height: 16px; line-height: 1.4; }}
  .composer-zone {{ font-family: var(--mono); font-size: 10px; color: var(--accent); background: var(--accent-soft);
                    padding: 2px 6px; border-radius: 5px; letter-spacing: .04em; }}
  .no-slots, .read-only-note {{ color: var(--faint); font-size: 12px; padding: 14px; }}

  /* ── Comment pins (preview-only) ─────────────────────── */
  .comment-stage {{ position: relative; flex: 1 1 auto; min-height: 100%; display: flex;
                    justify-content: center; align-items: flex-start; }}
  .comment-layer {{ position: absolute; inset: 0; pointer-events: none; z-index: 30; }}
  /* hint floats at the BOTTOM-centre of the stage column (never over the post
     header / profile, never over the panel) and hides once a comment exists. */
  .comment-hint {{ position: fixed; bottom: 18px; left: calc((100vw - 380px) / 2); transform: translateX(-50%);
                   display: flex; align-items: center; gap: 7px; padding: 7px 14px; border-radius: 999px;
                   background: rgba(255,255,255,.94); border: 1px solid var(--line); color: var(--muted);
                   font-size: 11.5px; font-weight: 500; font-family: var(--ui); pointer-events: none; z-index: 41;
                   box-shadow: 0 4px 16px rgba(40,36,30,.16); }}
  .comment-hint .ic {{ color: var(--accent); }}
  .pin {{ position: absolute; width: 28px; height: 28px; transform: translateY(-100%); border: none; cursor: pointer;
          background: var(--accent); padding: 0; border-radius: 50% 50% 50% 3px; pointer-events: auto;
          box-shadow: 0 5px 14px -3px rgba(91,87,214,.55), 0 0 0 2px #fff; display: flex; align-items: center;
          justify-content: center; color: #fff; }}
  .pin:hover {{ background: var(--accent-press); }}
  .pin .ic {{ margin-bottom: 1px; }}
  .composer {{ position: absolute; z-index: 60; width: 238px; background: #fff; border: 1px solid var(--line);
               border-radius: 12px; box-shadow: 0 18px 44px -12px rgba(40,36,30,.42); padding: 10px; pointer-events: auto;
               font-family: var(--ui); }}
  .composer textarea {{ width: 100%; border: none; outline: none; resize: none; min-height: 52px; max-height: 160px;
               font-family: var(--ui); font-size: 13px; color: var(--ink); line-height: 1.45; padding: 2px; background: #fff; }}
  .composer-actions {{ display: flex; align-items: center; gap: 6px; margin-top: 6px; border-top: 1px solid var(--line-soft); padding-top: 8px; }}
  .composer-actions .cspring {{ flex: 1; }}
  .cbtn {{ height: 28px; border-radius: 7px; border: none; cursor: pointer; font-family: var(--ui); font-size: 12.5px;
           font-weight: 600; padding: 0 12px; display: flex; align-items: center; justify-content: center; }}
  .cbtn--ghost {{ background: transparent; color: var(--muted); }}
  .cbtn--ghost:hover {{ background: var(--field); color: var(--ink); }}
  .cbtn--primary {{ background: var(--accent); color: #fff; }}
  .cbtn--primary:hover {{ background: var(--accent-press); }}
  .cbtn--del {{ width: 28px; padding: 0; color: var(--faint); font-size: 14px; }}
  .cbtn--del:hover {{ background: #FBEBE8; color: var(--danger); }}
</style>
</head>
<body>
{_MOCKUP_SPRITE}
<script>window.__EDITOR_RUN_ID__ = {json.dumps(run_id)};</script>
<script>window.__TEXTURES = {json.dumps({t["name"]: {"label": t["label"], "uri": t["uri"]} for t in textures})};</script>
<div class="app">
  <header class="topbar">
    <div class="brand"><img src="/agentic-logo.png" alt="Agentic OS" class="brand-logo"
         onerror="this.style.display='none'"></div>
    <!-- studio.js (server) injects the left-clustered action pill cluster here -->
    <div id="topbar-actions" class="topbar-actions"></div>
    <div class="slide-counter"><span id="slide-counter-cur">1</span> / {len(slides_info)}</div>
  </header>
  <div class="workspace">
    <!-- ── Stage: LinkedIn post mock + comment layer ──── -->
    <main class="stage">
      <div class="comment-stage" id="comment-stage">
        <div class="li-post">
          <div class="li-head">
            {avatar_html}
            <div class="li-who">
              <div class="li-name">{brand_name} <span class="li-deg">&middot; 1st</span></div>
              <div class="li-title">{brand_title}</div>
              <div class="li-meta">now &middot; Edited &middot; &#127760;</div>
            </div>
          </div>
          <div class="li-caption" id="li-caption" contenteditable="true" spellcheck="false"
               data-ph="Write your post caption…" title="Editable — this is what Zernio publishes">{caption_html}</div>
          <div class="li-viewer" id="li-viewer">
            <div class="carousel-track" id="carousel-track">
              {viewers_html}
            </div>
            {nav_html}
          </div>
          {dots_html}
          <div class="li-react"><span>&#128077;&#10084;&#65039;&#128161; 247</span><span>31 comments &middot; 12 reposts</span></div>
          <div class="li-actions">
            <button class="li-act">{_icon('thumbsup', 18)}<span>Like</span></button>
            <button class="li-act">{_icon('comment', 18)}<span>Comment</span></button>
            <button class="li-act">{_icon('repeat', 18)}<span>Repost</span></button>
            <button class="li-act">{_icon('send', 18)}<span>Send</span></button>
          </div>
        </div>
        <div class="comment-hint" id="comment-hint">{_sym('ic-comment', 14)}<span>Click anywhere to leave a comment &mdash; it stays after refresh</span></div>
        <div class="comment-layer" id="commentLayer"></div>
      </div>
    </main>

    <!-- ── Panel: single-scroll inspector ────────────── -->
    <aside class="panel">
      <div class="panel-head">{_icon('sliders', 16)}<span>Editor</span></div>

      <div class="global-section">
        <div class="card-label">{_icon('palette', 12)}<span>Brand palette</span></div>
        {palette_html}
      </div>

      {panels_html}

      <div class="export-bar">
        <button class="export-btn" onclick="exportComments()">{_icon('comment', 15)}<span>Send comments to Claude</span></button>
        <div id="export-note"></div>
      </div>
    </aside>
  </div>
</div>
{ai_modal_html}
{editor_js}
</body>
</html>"""

    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate a live-HTML carousel editor.")
    ap.add_argument("run_folder")
    ap.add_argument("--brand-context", default=None)
    args = ap.parse_args()

    run = Path(args.run_folder).resolve()
    if not run.is_dir():
        print(f"ERROR: run folder not found: {run}", file=sys.stderr)
        return 1

    bc = _resolve_brand_context(run, args.brand_context)
    html_str = build_editor_html(run, brand_context=bc)

    out_dir = run / "preview"
    out_dir.mkdir(exist_ok=True)
    out = out_dir / "editor.html"
    out.write_text(html_str, encoding="utf-8")

    print(str(out.resolve()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
