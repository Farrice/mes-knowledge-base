#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow>=10.0.0", "numpy>=1.26.0", "pyyaml>=6.0"]
# ///
"""Dead-space / proportion gate for template previews (AIOS-190 quality gate).

Sibling of measure_text_contrast.py: a SCRIPT-measured gate criterion (not the AI judging
itself). It approximates the "text crammed at the top, half the canvas empty below" failure
that the AI-first builder is prone to.

Two measurements, combined into one verdict:
  1. empty_fraction      — the largest contiguous near-uniform region of the preview, as a
                           fraction of the canvas. A big flat empty band → high value.
  2. text_height_fraction — the union of the vertical extents of the text elements (from
                           _measurements.yaml, the same file the contrast gate reads), as a
                           fraction of canvas height. Text squeezed into a thin band → low value.

FAIL rule (defaults, the AIOS-190 "moderate" thresholds resolved with Gustavo 2026-06-08):
  text_height_fraction < 0.25  AND  empty_fraction > 0.55   -> FAIL (dead space)
Either alone is fine — a deliberately minimal cover with one big centered headline can have a
high empty_fraction but its text band is tall, and a dense slide has low empty_fraction.

When --measurements is omitted (AI-placed text, no authored bboxes) the script reports
empty_fraction only and emits a WARN (not a hard fail) when it exceeds the empty threshold.

LIMITATION — AI-placed (baked) text (AIOS-190):
  This gate measures only the HTML/bbox text zones it is told about (via _measurements.yaml)
  plus the pixel-level "largest near-uniform region". It CANNOT see text the AI baked into the
  image. On a clean full-canvas C (integrated text) or B1 (in-scene surface) layout over a
  uniform background, the baked headline reads as part of the flat region, so the script
  over-counts empty space and would FALSE-FAIL an otherwise good slide. A full vision-read of
  baked text is OUT of scope for v1. Mitigation: dead-space is ADVISORY-ONLY for C / B1 forms —
  pass `--form C` (or `--form B1`) and a would-be FAIL is downgraded to an ADVISORY (exit 0).
  The form is known from the identification tree; the builder passes it through. When the form
  is unknown/omitted, behaviour is unchanged (C/B1 are NOT auto-detected here).

Usage:
    uv run dead_space.py --preview <path>/preview.png [--measurements <path>/_measurements.yaml]
                         [--form C|B1|B2|A|solid]
"""
import argparse
import sys
from pathlib import Path

import numpy as np
from PIL import Image


# Forms whose text is typically baked into the image (AI-placed), so the bbox/pixel
# dead-space heuristic cannot see it → advisory-only, never a hard fail.
ADVISORY_FORMS = {"c", "b1"}


def _force_utf8_streams() -> None:
    """Make stdout/stderr UTF-8 so the `->` / `-` reason glyphs don't crash a cp1252 console.

    On Windows the default console encoding is often cp1252, which has no codepoint for the
    en-dash / arrow glyphs used in the reason strings; printing them raises
    UnicodeEncodeError. reconfigure() (py3.7+) is the robust fix; errors='replace' is a
    belt-and-braces fallback for any glyph still outside the target encoding.
    """
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except (ValueError, OSError):
                pass


# --------------------------------------------------------------------------------------
# Measurement primitives (pure functions — unit-tested in test_dead_space.py)
# --------------------------------------------------------------------------------------

def downscale(arr: np.ndarray, max_dim: int = 160) -> np.ndarray:
    """Downscale an HxWx3 uint8 array so the longest side is <= max_dim (nearest, cheap)."""
    h, w = arr.shape[:2]
    scale = min(1.0, max_dim / max(h, w))
    if scale >= 1.0:
        return arr
    nh, nw = max(1, int(round(h * scale))), max(1, int(round(w * scale)))
    img = Image.fromarray(arr).resize((nw, nh), Image.NEAREST)
    return np.array(img)


def dominant_color(arr: np.ndarray, quant: int = 16) -> np.ndarray:
    """Most frequent color after coarse quantization → the presumed background color (RGB)."""
    flat = (arr.reshape(-1, 3).astype(int) // quant) * quant
    # pack to a single int per pixel for fast counting
    keys = (flat[:, 0] << 16) | (flat[:, 1] << 8) | flat[:, 2]
    vals, counts = np.unique(keys, return_counts=True)
    top = int(vals[int(np.argmax(counts))])
    return np.array([(top >> 16) & 0xFF, (top >> 8) & 0xFF, top & 0xFF], dtype=int)


def uniform_mask(arr: np.ndarray, bg: np.ndarray, tolerance: int = 24) -> np.ndarray:
    """Boolean HxW mask: True where the pixel is within `tolerance` (per-channel max-abs) of bg."""
    diff = np.abs(arr.astype(int) - bg.astype(int))
    return diff.max(axis=2) <= tolerance


def largest_component_fraction(mask: np.ndarray) -> float:
    """Fraction of the canvas occupied by the largest 4-connected True component of `mask`."""
    h, w = mask.shape
    total = h * w
    if total == 0:
        return 0.0
    visited = np.zeros_like(mask, dtype=bool)
    best = 0
    # iterative flood fill with an explicit stack (no scipy dependency)
    for sy in range(h):
        for sx in range(w):
            if not mask[sy, sx] or visited[sy, sx]:
                continue
            size = 0
            stack = [(sy, sx)]
            visited[sy, sx] = True
            while stack:
                y, x = stack.pop()
                size += 1
                if y > 0 and mask[y - 1, x] and not visited[y - 1, x]:
                    visited[y - 1, x] = True
                    stack.append((y - 1, x))
                if y + 1 < h and mask[y + 1, x] and not visited[y + 1, x]:
                    visited[y + 1, x] = True
                    stack.append((y + 1, x))
                if x > 0 and mask[y, x - 1] and not visited[y, x - 1]:
                    visited[y, x - 1] = True
                    stack.append((y, x - 1))
                if x + 1 < w and mask[y, x + 1] and not visited[y, x + 1]:
                    visited[y, x + 1] = True
                    stack.append((y, x + 1))
            if size > best:
                best = size
    return best / total


def empty_fraction(arr: np.ndarray, tolerance: int = 24, max_dim: int = 160) -> float:
    """End-to-end: largest contiguous near-background region of an image, as a canvas fraction."""
    small = downscale(arr, max_dim)
    bg = dominant_color(small)
    return largest_component_fraction(uniform_mask(small, bg, tolerance))


def text_height_fraction(elements: list) -> float:
    """Union of the vertical extents (t..t+h, in %) of text elements / 100.

    Mirrors measure_text_contrast.py: each element has bbox_pct = [l, t, w, h]. Non-text
    elements (own-fill pills/badges/seals, logos) are excluded — they aren't body content
    and shouldn't count toward "is the text band tall enough".
    """
    OWN_FILL_TYPES = {"pill", "badge", "card", "seal", "callout-card"}
    OWN_FILL_ID_HINTS = ("pill", "badge", "seal", "numeral", "card", "callout", "logo")
    intervals = []
    for el in elements or []:
        bb = el.get("bbox_pct") or []
        if len(bb) != 4:
            continue
        el_type = str(el.get("type", "")).lower()
        eid_l = str(el.get("id", "")).lower()
        if el_type in OWN_FILL_TYPES or any(h in eid_l for h in OWN_FILL_ID_HINTS):
            continue
        _, t, _, h = bb
        top = max(0.0, float(t))
        bot = min(100.0, float(t) + float(h))
        if bot > top:
            intervals.append((top, bot))
    if not intervals:
        return 0.0
    # union of intervals
    intervals.sort()
    union = 0.0
    cur_lo, cur_hi = intervals[0]
    for lo, hi in intervals[1:]:
        if lo <= cur_hi:
            cur_hi = max(cur_hi, hi)
        else:
            union += cur_hi - cur_lo
            cur_lo, cur_hi = lo, hi
    union += cur_hi - cur_lo
    return union / 100.0


def evaluate(empty_frac: float, text_frac, empty_thresh: float = 0.55,
             text_thresh: float = 0.25, form: str | None = None) -> dict:
    """Combine the two measurements into a verdict dict.

    text_frac may be None (no measurements) -> empty-only WARN path.

    form (optional): the identification-tree form (C, B1, B2, A, solid, ...). For C / B1
    the text is typically baked into the image, which this heuristic cannot see, so a
    would-be FAIL or WARN is downgraded to "ADVISORY" (a non-blocking note, exit 0). Other
    forms (or form=None) keep the original blocking behaviour.
    """
    advisory = (form or "").strip().lower() in ADVISORY_FORMS

    if text_frac is None:
        if empty_frac > empty_thresh:
            base = "large empty region; no text bboxes to confirm proportion"
            if advisory:
                return {"verdict": "ADVISORY", "empty_fraction": empty_frac,
                        "text_height_fraction": None,
                        "reason": (f"{base} (advisory only for form {form.upper()}: "
                                   "baked text not measurable here)")}
            return {"verdict": "WARN", "empty_fraction": empty_frac,
                    "text_height_fraction": None, "reason": base}
        return {"verdict": "OK", "empty_fraction": empty_frac,
                "text_height_fraction": None, "reason": "within bounds"}

    fail = (text_frac < text_thresh) and (empty_frac > empty_thresh)
    if not fail:
        return {"verdict": "OK", "empty_fraction": empty_frac,
                "text_height_fraction": text_frac, "reason": "within bounds"}

    reason = (f"text band {text_frac:.0%} < {text_thresh:.0%} of height AND empty region "
              f"{empty_frac:.0%} > {empty_thresh:.0%} -> dead space")
    if advisory:
        return {"verdict": "ADVISORY", "empty_fraction": empty_frac,
                "text_height_fraction": text_frac,
                "reason": (f"{reason} (advisory only for form {form.upper()}: baked text not "
                           "measurable here, not a hard fail)")}
    return {"verdict": "FAIL", "empty_fraction": empty_frac,
            "text_height_fraction": text_frac, "reason": reason}


# --------------------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------------------

def main() -> int:
    _force_utf8_streams()
    ap = argparse.ArgumentParser()
    ap.add_argument("--preview", required=True, type=Path)
    ap.add_argument("--measurements", type=Path, default=None)
    ap.add_argument("--empty-threshold", type=float, default=0.55)
    ap.add_argument("--text-threshold", type=float, default=0.25)
    ap.add_argument("--tolerance", type=int, default=24)
    ap.add_argument("--form", type=str, default=None,
                    help="identification-tree form (C, B1, B2, A, solid). For C / B1 the "
                         "dead-space verdict is advisory-only: baked AI text is not measurable "
                         "by this heuristic, so a would-be FAIL is downgraded to ADVISORY.")
    args = ap.parse_args()

    if not args.preview.exists():
        print(f"Error: preview not found: {args.preview}", file=sys.stderr)
        return 1

    arr = np.array(Image.open(args.preview).convert("RGB"))
    ef = empty_fraction(arr, tolerance=args.tolerance)

    text_frac = None
    if args.measurements and args.measurements.exists():
        import yaml
        meas = yaml.safe_load(args.measurements.read_text(encoding="utf-8")) or {}
        text_frac = text_height_fraction(meas.get("elements", []))

    res = evaluate(ef, text_frac, args.empty_threshold, args.text_threshold, form=args.form)

    print(f"Dead-space audit on {args.preview.name}:")
    print(f"  empty_fraction       = {res['empty_fraction']:.3f}  (threshold {args.empty_threshold:.2f})")
    if res["text_height_fraction"] is None:
        print(f"  text_height_fraction = n/a  (no --measurements)")
    else:
        print(f"  text_height_fraction = {res['text_height_fraction']:.3f}  (floor {args.text_threshold:.2f})")
    print(f"  verdict = {res['verdict']}  — {res['reason']}")

    if res["verdict"] == "FAIL":
        print(f"[fail] dead space: {res['reason']}", file=sys.stderr)
        return 2
    if res["verdict"] == "ADVISORY":
        print(f"[advisory] {res['reason']}", file=sys.stderr)
        return 0
    if res["verdict"] == "WARN":
        print(f"[warn] {res['reason']}", file=sys.stderr)
        return 0
    print("[ok] proportion within bounds")
    return 0


if __name__ == "__main__":
    sys.exit(main())
