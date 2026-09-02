#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow>=10.0.0", "numpy>=1.26.0"]
# ///
"""SEAL-GLYPH-PRESENT — a HONOR check: a contracted seal/badge GLYPH must visibly RENDER.

Sibling of check_treatment_contract.py Check 14 (seal/logo provenance). Where Check 14
verifies the seal ASSET exists / is not destroyed by CSS, and the rationale/provenance gates
verify a logo was RESOLVED, NONE of them verifies the glyph actually LANDED in the badge
region of the rendered preview. The run-08 overlay-cover miss: the Claude logo asset existed
in commons (provenance passed), but the badge authored `<img src="assets/sunburst.svg"
style="color: var(--brand-accent)">` + a `<img src="{{BRAND_LOGO_PATH}}">` whose path was
broken AND whose `color:` cannot pierce an `<img>`'s SVG `currentColor` → an EMPTY starburst
shipped. The contract was "a glyph badge"; the OUTPUT honored only "a shape".

This gate closes "resolved/authored ≠ rendered". For every badge/seal region the template
declares (a positioned element whose selector or data-slot reads logo/badge/seal/emblem/
starburst) that CONTRACTS a glyph inside it, it runs two HONOR reads:

  (1) GLYPH-ASSET-RESOLVES (the hard, deterministic catch — the run-08 root cause): the badge's
      nested glyph `<img src>` must resolve to an EXISTING file relative to the template dir
      (template `{{SLOT}}` placeholders substituted from the slide metadata.json data). The
      overlay-cover miss: the glyph `<img>`'s `BRAND_LOGO_PATH` resolved to
      `.claude/skills/viz-image-gen/references/icons/commons/ai/claude.svg` — a path that does
      NOT exist relative to the template dir (the correct asset was `assets/claude.svg`), so the
      `<img>` rendered NOTHING. A broken glyph path = the glyph cannot render = an empty shell
      ships. This is brand-agnostic + deterministic, so it BLOCKS.
  (2) GLYPH-RENDERED-IN-PIXELS (a secondary advisory read): crop the inner glyph sub-region of
      the badge from the preview and confirm it is not near-empty / single-color. A coarse pixel
      confirmation — advisory (a busy decorative shell can mask a missing inner glyph), surfaced
      but not blocking on its own.

It is GENERAL to any template: badge regions + glyph srcs come from the authored HTML (no slug,
no per-template constant); a missing glyph asset is a filesystem fact; the pixel read is a
brand-agnostic property. The seal asset existing in commons (provenance) is NOT enough — the
glyph the badge POINTS AT must resolve and the mark must be SEEN.

Posture: read (1) is a HARD deterministic read (a broken glyph path is not a judgment call), so
it BLOCKS by default (exit 2) + feeds the 3-try ladder, mirroring the seal-provenance hard-fail.
`--no-enforce` downgrades to advisory (exit 0, WARN). The pixel read (2) is advisory regardless.

A badge region is JUDGED only when the template+rationale CONTRACT a glyph inside it: the
element is a seal/badge/logo selector AND (a) it nests a logo/glyph child (an inner `<img>` /
`<svg>` / a data-slot reading logo/glyph/mark), or (b) the rationale §2 declares a glyph/logo/
wordmark inside the seal. A purely decorative shape (a plain accent starburst the rationale
calls ornamental, no glyph contracted) is NOT judged — it is allowed to be a flat fill.

Exit codes:
  0  -> every contracted seal glyph rendered (or advisory mode).
  1  -> usage / file-not-found error.
  2  -> a contracted seal glyph did not render (empty/single-color badge) AND enforcing.

Usage:
    uv run check_seal_glyph.py --template-html <dir>/template.html \
        --preview <dir>/preview.png --rationale <dir>/rationale.md
"""
import argparse
import json
import re
import sys
from pathlib import Path

import numpy as np
from PIL import Image

# A selector / data-slot naming a brand seal / badge / logo region (same family as Check 14).
SEAL_SELECTOR_RE = re.compile(
    r"(logo|badge|seal|brandmark|brand-mark|wordmark|emblem|starburst|sunburst|stamp|sticker)",
    re.IGNORECASE)
# A child element that IS the glyph contracted to live inside the badge: an inner image/svg, or
# a data-slot naming a logo/glyph/mark/icon.
GLYPH_CHILD_SLOT_RE = re.compile(r"(logo|glyph|mark|icon|wordmark|emblem)", re.IGNORECASE)
# Rationale §2 phrasing that contracts a glyph/logo INSIDE the seal.
GLYPH_IN_SEAL_RE = re.compile(
    r"(claude|logo|glyph|wordmark|tool\s+(?:icon|mark|logo)|brand\s+mark|"
    r"the\s+\w+\s+mark|icon\s+(?:inside|within|in)\s+the\s+(?:seal|badge|starburst))",
    re.IGNORECASE)

# A geometry % is read from inline style (left/top/width/height as NN% of canvas).
_PCT_RE = {k: re.compile(rf"{k}\s*:\s*(-?\d+(?:\.\d+)?)\s*%", re.IGNORECASE)
           for k in ("left", "top", "width", "height")}

# --- thresholds (brand-agnostic, deterministic) ------------------------------------------
# A badge region's internal EDGE density (fraction of pixels on a strong luminance edge). A
# rendered glyph has edges (letterforms / mark strokes); an empty single-fill shell has ~none.
GLYPH_MIN_EDGE_FRAC = 0.010
# A badge region's tonal SPREAD beyond a single dominant fill: the fraction of pixels whose
# luminance is far from BOTH the two most-common tones (the shell fill + the background behind
# the shape). A glyph paints a third tone family across a non-trivial area; an empty shell does
# not. This is the "more than one flat fill" signal that survives even a low-contrast glyph.
GLYPH_MIN_OFFTONE_FRAC = 0.020
# Edge = neighbour luminance jump above this (0-255). Coarse Sobel-free gradient.
EDGE_LUMA_DELTA = 28
# A tone is "near" a dominant tone within this luminance band (0-255).
TONE_NEAR_BAND = 22.0
# Downscale longest badge side to this for the read — coarse, deterministic, jitter-free.
BADGE_GRID_MAX = 96


def _force_utf8_streams() -> None:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except (ValueError, OSError):
                pass


def _section_body(text: str, header_re: str) -> str | None:
    """Body of the first markdown section whose header matches header_re (header→next header)."""
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        m = re.match(r"^\s{0,3}#{1,6}\s+(.*\S)\s*$", line)
        if m and re.search(header_re, m.group(1), re.IGNORECASE):
            start = i + 1
            break
    if start is None:
        return None
    end = len(lines)
    for j in range(start, len(lines)):
        if re.match(r"^\s{0,3}#{1,6}\s+\S", lines[j]):
            end = j
            break
    return "\n".join(lines[start:end])


def per_block_section(text: str) -> str:
    body = _section_body(text, r"per[\s-]?block|block breakdown|block treatment")
    return body if body is not None else text


def _parse_pct_geometry(style: str) -> dict | None:
    """Parse left/top/width/height as canvas fractions [0,1] from an inline style. None if any
    of the four is missing (we only judge regions with a known bbox)."""
    out: dict = {}
    for k, rx in _PCT_RE.items():
        m = rx.search(style)
        if not m:
            return None
        out[k] = float(m.group(1)) / 100.0
    if out["width"] <= 0 or out["height"] <= 0:
        return None
    return out


# A glyph-bearing inner <img>/<svg> child: capture its src (may be a {{SLOT}} placeholder).
_GLYPH_IMG_RE = re.compile(r"<img\b[^>]*\bsrc\s*=\s*\"([^\"]*)\"[^>]*>", re.IGNORECASE)
_SLOT_PLACEHOLDER_RE = re.compile(r"\{\{+\s*([A-Z0-9_]+)\s*\}\}+")
# The starburst SHELL itself (the decorative shape) — NOT the glyph. A glyph child is an inner
# img whose src is NOT the shell shape. Shell-name hints in the src.
_SHELL_SRC_RE = re.compile(r"(sunburst|starburst|burst|shell|seal-bg|badge-bg)", re.IGNORECASE)


def _substitute_slots(src: str, data: dict) -> str:
    """Replace {{SLOT}} placeholders in an img src with the slide metadata.json data values."""
    def repl(m):
        key = m.group(1)
        val = data.get(key)
        return str(val) if isinstance(val, str) else m.group(0)
    return _SLOT_PLACEHOLDER_RE.sub(repl, src)


def parse_seal_regions(html: str, rationale_text: str, data: dict) -> list[dict]:
    """Find badge/seal regions in template.html that CONTRACT a glyph inside them.

    Returns [{name, bbox:(l,t,w,h) in [0,1], glyph_src}]. A region qualifies when:
      - its opening tag's class/id/data-slot matches a seal/badge/logo selector, AND
      - it has a parsable %-geometry inline style, AND
      - a glyph is contracted inside it — either a nested glyph child (inner <img>/<svg>/a glyph
        data-slot) within the same element block, OR the rationale §2 declares a glyph in the seal.

    glyph_src is the resolved (slot-substituted) src of the inner GLYPH img (the non-shell inner
    image), or None when no concrete glyph img src is found. A purely decorative accent shape with
    NO contracted glyph is skipped."""
    rationale_contracts_glyph = bool(GLYPH_IN_SEAL_RE.search(per_block_section(rationale_text)))
    regions: list[dict] = []
    seen: set[tuple] = set()
    for m in re.finditer(r"<(div|span|figure|a)\b([^>]*)>", html, re.IGNORECASE):
        attrs = m.group(2)
        if not SEAL_SELECTOR_RE.search(attrs):
            continue
        style_m = re.search(r'style\s*=\s*"([^"]*)"', attrs, re.IGNORECASE)
        if not style_m:
            continue
        bbox = _parse_pct_geometry(style_m.group(1))
        if bbox is None:
            continue
        tail = html[m.end():m.end() + 1200]
        img_srcs = _GLYPH_IMG_RE.findall(tail)
        nested_glyph = bool(re.search(r"<(img|svg)\b", tail, re.IGNORECASE)
                            or GLYPH_CHILD_SLOT_RE.search(
                                " ".join(re.findall(r'data-slot\s*=\s*"([^"]*)"', tail[:600],
                                                    re.IGNORECASE))))
        if not (nested_glyph or rationale_contracts_glyph):
            continue
        # The GLYPH src = the first inner img whose src is NOT the decorative shell shape.
        glyph_src = None
        for s in img_srcs:
            if _SHELL_SRC_RE.search(s):
                continue
            glyph_src = _substitute_slots(s, data)
            break
        name_m = re.search(r'(?:class|id)\s*=\s*"([^"]*)"', attrs, re.IGNORECASE)
        name = (name_m.group(1) if name_m else "seal")[:48]
        key = (round(bbox["left"], 3), round(bbox["top"], 3),
               round(bbox["width"], 3), round(bbox["height"], 3))
        if key in seen:
            continue
        seen.add(key)
        regions.append({"name": name, "glyph_src": glyph_src,
                        "bbox": (bbox["left"], bbox["top"], bbox["width"], bbox["height"])})
    return regions


def _luma(arr: np.ndarray) -> np.ndarray:
    a = arr.astype(np.float32)
    return 0.2126 * a[..., 0] + 0.7152 * a[..., 1] + 0.0722 * a[..., 2]


def glyph_present(crop: Image.Image) -> dict:
    """Read whether a glyph rendered inside a badge crop. Returns {edge_frac, offtone_frac,
    present}. A glyph carries internal EDGES + a third tone family beyond shell+background; an
    empty shell is one flat fill (optionally over one background)."""
    w, h = crop.size
    scale = BADGE_GRID_MAX / max(w, h) if max(w, h) > BADGE_GRID_MAX else 1.0
    small = crop.convert("RGB").resize((max(2, round(w * scale)), max(2, round(h * scale))))
    lum = _luma(np.asarray(small))
    n = lum.size
    if n < 9:
        return {"edge_frac": 0.0, "offtone_frac": 0.0, "present": False}

    # Edge density: max neighbour luminance jump per pixel above EDGE_LUMA_DELTA.
    dx = np.abs(np.diff(lum, axis=1))
    dy = np.abs(np.diff(lum, axis=0))
    edge = np.zeros_like(lum, dtype=bool)
    edge[:, :-1] |= dx > EDGE_LUMA_DELTA
    edge[:-1, :] |= dy > EDGE_LUMA_DELTA
    edge_frac = float(edge.mean())

    # Off-tone fraction: histogram luminance into 16 bins, take the TWO heaviest bins as the
    # shell-fill + background tone families; the off-tone fraction is everything far from both.
    hist, edges = np.histogram(lum, bins=16, range=(0, 255))
    centers = (edges[:-1] + edges[1:]) / 2
    top2 = centers[np.argsort(hist)[-2:]]
    d = np.minimum(np.abs(lum[..., None] - top2[None, None, :]).min(axis=-1), 999)
    offtone_frac = float((d > TONE_NEAR_BAND).mean())

    # A rendered glyph carries internal EDGES (letterform/mark strokes). A third tone family
    # beyond shell+background is corroborating but NOT required (a crisp two-tone mark has none).
    # An empty single-fill shell has neither. Edge density is the primary signal.
    present = edge_frac >= GLYPH_MIN_EDGE_FRAC or offtone_frac >= GLYPH_MIN_OFFTONE_FRAC
    return {"edge_frac": round(edge_frac, 4),
            "offtone_frac": round(offtone_frac, 4), "present": present}


def glyph_asset_resolves(glyph_src: str | None, template_dir: Path) -> tuple[bool, str]:
    """The hard read: does the badge's glyph <img src> resolve to an existing file relative to
    the template dir? Returns (resolves, resolved_path_str). A still-unresolved {{SLOT}}
    placeholder, an empty src, or a non-existent path = does NOT resolve. A remote URL
    (http/https) or data: URI is treated as resolvable (out of scope for a filesystem read)."""
    if not glyph_src:
        return True, ""  # no concrete glyph src to verify (pixel read still applies)
    s = glyph_src.strip()
    if _SLOT_PLACEHOLDER_RE.search(s):
        return False, s  # an unresolved placeholder cannot render
    if s.startswith(("http://", "https://", "data:")):
        return True, s
    p = (template_dir / s).resolve()
    return p.is_file(), str(p)


def evaluate(html: str, rationale_text: str, preview: Image.Image | None,
             template_dir: Path, data: dict) -> dict:
    """Verdict dict. Skips cleanly (ok=True) when no seal region contracts a glyph."""
    regions = parse_seal_regions(html, rationale_text, data)
    flags: list[str] = []          # blocking (when enforcing)
    advisories: list[str] = []     # never-blocking pixel notes
    judged: list[dict] = []
    pw = ph = 0
    if preview is not None:
        pw, ph = preview.size
    for reg in regions:
        l, t, w, h = reg["bbox"]
        # --- read (1): glyph asset resolves (HARD) ---
        resolves, resolved = glyph_asset_resolves(reg["glyph_src"], template_dir)
        rec = {"name": reg["name"], "bbox": reg["bbox"], "glyph_src": reg["glyph_src"],
               "glyph_resolves": resolves}
        if not resolves:
            flags.append(
                f"empty seal (broken glyph path): the badge region '{reg['name']}' "
                f"({l:.0%},{t:.0%}) contracts a glyph, but its glyph <img src> "
                f"('{(reg['glyph_src'] or '')[:70]}') does NOT resolve to an existing file "
                f"relative to the template dir — the <img> renders nothing, so an empty shell "
                f"ships (the run-08 overlay-cover miss: BRAND_LOGO_PATH pointed at a "
                f"`.claude/skills/...` path that did not exist; the asset sat at "
                f"`assets/claude.svg`). Provenance (asset-exists-in-commons) passing is NOT "
                f"enough — fix the glyph src to a path that resolves so the mark renders into "
                f"the badge.")
        # --- read (2): glyph rendered in pixels (ADVISORY) — inner glyph sub-region ---
        if preview is not None:
            # The glyph nests centered inside the shell — read the inner 50% sub-region so the
            # decorative shell's own edges don't masquerade as a rendered glyph.
            bw, bh = (l + w - l) * pw, (t + h - t) * ph
            ix0 = int((l + 0.25 * w) * pw); iy0 = int((t + 0.25 * h) * ph)
            ix1 = int((l + 0.75 * w) * pw); iy1 = int((t + 0.75 * h) * ph)
            ix0, iy0 = max(0, ix0), max(0, iy0)
            ix1, iy1 = min(pw, ix1), min(ph, iy1)
            if ix1 - ix0 >= 4 and iy1 - iy0 >= 4:
                read = glyph_present(preview.crop((ix0, iy0, ix1, iy1)))
                rec.update(read)
                if not read["present"] and resolves:
                    advisories.append(
                        f"seal pixel-read: the inner glyph region of badge '{reg['name']}' reads "
                        f"near-empty / single-color (edge {read['edge_frac']:.3f}, off-tone "
                        f"{read['offtone_frac']:.3f}) — the glyph may not have visibly rendered "
                        f"even though its asset path resolves. Advisory (a busy decorative shell "
                        f"can also read low) — eyeball the badge.")
        judged.append(rec)
    ok = not flags
    return {"ok": ok, "regions_found": len(regions), "judged": judged, "flags": flags,
            "advisories": advisories,
            "reason": "all contracted seal glyphs resolve" if ok else "; ".join(flags)}


def main() -> int:
    _force_utf8_streams()
    ap = argparse.ArgumentParser(description="SEAL-GLYPH-PRESENT — a contracted seal glyph "
                                             "must visibly render into the badge region.")
    ap.add_argument("--template-html", required=True, type=Path)
    ap.add_argument("--preview", type=Path, default=None,
                    help="rendered preview.png. Without it the check is a no-op (exit 0).")
    ap.add_argument("--rationale", type=Path, default=None,
                    help="rationale.md — lets a §2 glyph-in-seal declaration contract a glyph "
                         "even when the HTML has no nested glyph child.")
    ap.add_argument("--metadata", type=Path, default=None,
                    help="_slides/<slide>/metadata.json — supplies the data slot values to "
                         "substitute {{SLOT}} placeholders in the glyph <img src> before "
                         "resolving it. Default: auto-discover <template-dir>/_slides/*/metadata.json.")
    ap.add_argument("--enforce", dest="enforce", action="store_true", default=True,
                    help="block (exit 2) on an empty seal (DEFAULT — deterministic hard read).")
    ap.add_argument("--no-enforce", dest="enforce", action="store_false",
                    help="advisory: WARN only, exit 0 (inspection runs).")
    args = ap.parse_args()

    if not args.template_html.exists():
        print(f"Error: template.html not found: {args.template_html}", file=sys.stderr)
        return 1
    html = args.template_html.read_text(encoding="utf-8")
    rationale_text = ""
    if args.rationale and args.rationale.exists():
        rationale_text = args.rationale.read_text(encoding="utf-8")

    preview = None
    if args.preview and args.preview.exists():
        preview = Image.open(args.preview).convert("RGB")
    elif args.preview:
        print(f"Error: --preview given but not found: {args.preview}", file=sys.stderr)
        return 1

    template_dir = args.template_html.resolve().parent
    # Load the slide data (for {{SLOT}} → glyph src substitution): explicit --metadata, else
    # auto-discover the first <template-dir>/_slides/*/metadata.json.
    data: dict = {}
    meta_path = args.metadata
    if meta_path is None:
        cands = sorted((template_dir / "_slides").glob("*/metadata.json"))
        meta_path = cands[0] if cands else None
    if meta_path is not None and meta_path.exists():
        try:
            md = json.loads(meta_path.read_text(encoding="utf-8"))
            data = md.get("data", md) if isinstance(md, dict) else {}
        except (OSError, ValueError):
            print(f"  note: metadata.json unreadable ({meta_path})", file=sys.stderr)

    res = evaluate(html, rationale_text, preview, template_dir, data)
    print(f"SEAL-GLYPH-PRESENT on {template_dir.name}:")
    print(f"  seal-regions-contracting-a-glyph={res['regions_found']}  "
          f"judged={len(res['judged'])}")
    for j in res["judged"]:
        extra = (f" edge={j.get('edge_frac', float('nan')):.3f} "
                 f"offtone={j.get('offtone_frac', float('nan')):.3f}"
                 if "edge_frac" in j else "")
        print(f"  [{j['name']}] glyph_resolves={j['glyph_resolves']} "
              f"src='{(j['glyph_src'] or '')[:50]}'{extra}")
    for a in res["advisories"]:
        print(f"[warn] {a}", file=sys.stderr)
    print(f"  verdict = {'PASS' if res['ok'] else ('FAIL' if args.enforce else 'WARN')} — "
          f"{res['reason']}")
    if res["ok"]:
        return 0
    for f in res["flags"]:
        tag = "fail" if args.enforce else "warn"
        print(f"[{tag}] {f}", file=sys.stderr)
    return 2 if args.enforce else 0


if __name__ == "__main__":
    sys.exit(main())
