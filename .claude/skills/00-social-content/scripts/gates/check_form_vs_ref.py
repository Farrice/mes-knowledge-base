#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow>=10.0.0", "numpy>=1.26.0"]
# ///
"""FORM-VS-REF SIGNATURE — a HONOR check: don't trust the rationale's self-declared form;
read the REF's own composition signature and flag a flat-isolated mis-route.

Sibling of check_treatment_contract.py (which binds the OUTPUT to the treatment the RATIONALE
declared). That trust is the gap RC-C names: when the rationale mis-reads the ref and
SELF-DECLARES a flat form (B2 — axis-aligned isolated HTML chips), every downstream gate checks
the output against THAT self-declared form, so a mis-route passes. The run-08 highlight-pills
miss: the ref's defining signature is tilted / overlapping / icon-bearing pills WOVEN through the
headline (a Form C composition signature). The rationale argued its way to B2 ("the brand
text_policy is html-overlay, so reproduce the woven look with z-index"), and the output shipped
FLAT axis-aligned isolated chips off in the right margin. Check B trusts the B2 declaration and
passes. THIS gate reads the REF's signature directly and flags the mismatch.

It compares the OUTPUT against the REF's SIGNATURE, not the rationale's self-declared form:

  REF woven signature (read from ref-canonical PIXELS, brand-agnostic):
    - multiple substantial brand-ACCENT device blobs (the woven label-pills) sitting in the
      central headline band, AND
    - those blobs read as TILTED / overlapping (a low fill-ratio inside their bounding box — an
      axis-aligned rounded pill fills its bbox densely; a tilted or headline-overlapping pill
      does not), i.e. the composition WEAVES devices through the headline.

  OUTPUT flat-isolated signature (read from template.html GEOMETRY, brand-agnostic):
    - the pill/callout containers are axis-aligned (NO `transform: rotate`), AND
    - they sit in clear margins, NOT overlapping the headline data-slot's bbox — isolated chips.

REF=woven AND OUTPUT=flat-isolated → FLAG the mis-route (the ref's woven signature was shipped
as flat containers). GENERAL: no slug, no per-template constant; the accent is RESOLVED from the
brand tokens (never a hardcoded hue), the headline band + pill geometry come from the authored
HTML, and "woven" is a pixel property of the ref.

POSTURE: form routing is a JUDGMENT call (the rationale may have a legitimate brand reason to
reproduce a woven look in HTML — but it must then actually weave, not ship isolated chips). So
this is ADVISORY by default (exit 0, WARN — mirrors the image-medium / palette conferences),
surfacing the mis-route for the human; `--enforce` makes it BLOCK (exit 2) + feed the 3-try
ladder for a pool that wants a hard signature floor.

Exit codes:
  0  -> no mis-route detected, OR advisory mode, OR indeterminate (no ref / no accent / etc.).
  1  -> usage / file-not-found error.
  2  -> a woven ref shipped as flat isolated containers AND enforcing.

Usage:
    uv run check_form_vs_ref.py --template-html <dir>/template.html \
        --ref <dir>/assets/ref-canonical.png [--accent '#rrggbb'] [--enforce]
"""
import argparse
import colorsys
import json
import re
import sys
from pathlib import Path

import numpy as np
from PIL import Image

DEFAULT_ACCENT_HEX = "#d05344"
# Vividness floors for a pill device (background-agnostic — reads the RAW ref, any hue).
VIVID_SAT_FLOOR = 0.45
VIVID_VAL_FLOOR = 0.45

GRID_W = 200                      # ref downscale width for the woven read
# A central band (top..bottom fraction of canvas) where the HEADLINE lives — the zone where a
# woven composition threads its devices. Devices outside it (corner seals, footer chrome) are
# not "woven through the headline".
HEADLINE_BAND = (0.10, 0.85)
# A woven label-pill's canvas-fraction band: above speckle, below a vivid background field. A
# single large vivid region (a vivid bg) lands ABOVE this range and is not counted as a pill.
PILL_FRAC_RANGE = (0.0020, 0.080)
# How many substantial vivid pill devices in the band before the ref reads as "device-woven".
WOVEN_MIN_DEVICES = 2
# A device whose filled-pixels / bbox-area is BELOW this reads as tilted / headline-overlapping
# (an axis-aligned solid pill fills its bbox densely, ~0.7-0.85; a tilted or text-overlapped one
# leaves large empty bbox corners).
WOVEN_MAX_FILL = 0.68
# At least this many of the substantial devices must read tilted/overlapping for "woven".
WOVEN_MIN_TILTED = 1


def _force_utf8_streams() -> None:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except (ValueError, OSError):
                pass


# ---------------------------------------------------------------------------------------
# Accent resolution (RESOLVED, never hardcoded) — mirrors check_treatment_contract.resolve_accent.
# ---------------------------------------------------------------------------------------
def _hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    s = hex_color.strip().lstrip("#")
    if len(s) == 3:
        s = "".join(ch * 2 for ch in s)
    if len(s) != 6 or any(c not in "0123456789abcdefABCDEF" for c in s):
        raise ValueError(f"invalid accent hex: {hex_color!r}")
    return int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16)


def accent_hue(hex_color: str) -> float:
    r, g, b = (c / 255.0 for c in _hex_to_rgb(hex_color))
    h, _, _ = colorsys.rgb_to_hsv(r, g, b)
    return h * 360.0


def _accent_from_tokens(tokens_path: Path) -> str | None:
    try:
        data = json.loads(tokens_path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    colors = data.get("colors") or {}
    for key in ("accent", "primary_accent", "primary-accent"):
        val = colors.get(key)
        if isinstance(val, str):
            try:
                _hex_to_rgb(val)
            except ValueError:
                continue
            return val
    return None


def resolve_accent(cli_accent: str | None, *anchors: Path) -> tuple[str, str]:
    if cli_accent:
        _hex_to_rgb(cli_accent)
        return cli_accent, "--accent"
    for anchor in anchors:
        if anchor is None:
            continue
        for anc in anchor.resolve().parents:
            candidates = [anc / "brand_context" / "visual-identity" / "tokens.json"]
            if anc.name == "brand_context":
                candidates.insert(0, anc / "visual-identity" / "tokens.json")
            for tok in candidates:
                if tok.is_file():
                    accent = _accent_from_tokens(tok)
                    if accent is not None:
                        return accent, str(tok)
    print(f"  WARN: accent not resolved; using coral default ({DEFAULT_ACCENT_HEX}) — pass "
          f"--accent or ensure brand tokens.json is reachable", file=sys.stderr)
    return DEFAULT_ACCENT_HEX, "default"


# ---------------------------------------------------------------------------------------
# REF woven-signature read (pixels).
# ---------------------------------------------------------------------------------------
def _label_grid(mask: np.ndarray) -> list[dict]:
    """Pure-python 4-connectivity components: {frac, x0,x1,y0,y1, fill} in [0,1]/ratio."""
    h, w = mask.shape
    total = h * w
    seen = [[False] * w for _ in range(h)]
    m = mask.tolist()
    comps: list[dict] = []
    for sy in range(h):
        for sx in range(w):
            if not m[sy][sx] or seen[sy][sx]:
                continue
            stack = [(sy, sx)]
            seen[sy][sx] = True
            xs0 = xs1 = sx
            ys0 = ys1 = sy
            cnt = 0
            while stack:
                cy, cx = stack.pop()
                cnt += 1
                xs0 = min(xs0, cx); xs1 = max(xs1, cx)
                ys0 = min(ys0, cy); ys1 = max(ys1, cy)
                for ny, nx in ((cy - 1, cx), (cy + 1, cx), (cy, cx - 1), (cy, cx + 1)):
                    if 0 <= ny < h and 0 <= nx < w and m[ny][nx] and not seen[ny][nx]:
                        seen[ny][nx] = True
                        stack.append((ny, nx))
            bw = (xs1 - xs0 + 1)
            bh = (ys1 - ys0 + 1)
            comps.append({"frac": cnt / total, "x0": xs0 / w, "x1": (xs1 + 1) / w,
                          "y0": ys0 / h, "y1": (ys1 + 1) / h,
                          "fill": cnt / (bw * bh), "cy": (ys0 + ys1) / 2 / h})
    return comps


def ref_woven_signature(ref: Image.Image, accent_hex: str | None = None) -> dict:
    """Read the ref's woven signature: multiple small, similarly-sized VIVID device blobs (the
    woven label-pills) in the headline band, reading tilted/overlapping (low bbox fill).

    The pills are detected by VIVIDNESS (high saturation distinct from the field), NOT by the
    brand accent hue — the RAW ref is read BEFORE any brand remap (the run-08 ref pills are lime
    green, not the coral brand accent; the whole point of FORM-VS-REF is to read the ref's own
    signature, not the post-remap palette). A `--accent` hint, if given, is recorded but does not
    restrict detection. A SINGLE large vivid field (a vivid background) is NOT a pill — devices
    are bounded to the small/mid PILL_FRAC_RANGE; the gate further only fires when the OUTPUT
    declares pill containers, so a vivid-bg ref with no output pills can never trip it.

    Returns {is_woven, n_devices, n_tilted, vivid_frac, devices}."""
    grid_w = GRID_W
    grid_h = max(8, round(grid_w * ref.height / ref.width))
    small = np.asarray(ref.convert("RGB").resize((grid_w, grid_h))).astype(np.float32) / 255.0
    mx = small.max(-1); mn = small.min(-1)
    sat = (mx - mn) / (mx + 1e-6)
    mask = (sat >= VIVID_SAT_FLOOR) & (mx >= VIVID_VAL_FLOOR)
    comps = _label_grid(mask)
    band_lo, band_hi = HEADLINE_BAND
    lo, hi = PILL_FRAC_RANGE
    devices = [c for c in comps
               if lo <= c["frac"] <= hi and band_lo <= c["cy"] <= band_hi]
    devices.sort(key=lambda c: c["frac"], reverse=True)
    n_tilted = sum(1 for c in devices if c["fill"] < WOVEN_MAX_FILL)
    is_woven = (len(devices) >= WOVEN_MIN_DEVICES and n_tilted >= WOVEN_MIN_TILTED)
    return {"is_woven": is_woven, "n_devices": len(devices), "n_tilted": n_tilted,
            "vivid_frac": round(float(mask.mean()), 4),
            "devices": [{"frac": round(c["frac"], 4), "fill": round(c["fill"], 2)}
                        for c in devices[:6]]}


# ---------------------------------------------------------------------------------------
# OUTPUT flat-isolated read (template.html geometry).
# ---------------------------------------------------------------------------------------
PILL_SELECTOR_RE = re.compile(r"(pill|callout|chip|tag|lozenge|label-box)", re.IGNORECASE)
ROTATE_RE = re.compile(r"transform\s*:[^;{}]*rotate\s*\(", re.IGNORECASE)
_PCT_RE = {k: re.compile(rf"(?<![\w-]){k}\s*:\s*(-?\d+(?:\.\d+)?)\s*%", re.IGNORECASE)
           for k in ("left", "right", "top", "bottom", "width", "height")}


def _headline_bbox(html: str) -> tuple[float, float, float, float] | None:
    """The HEADLINE data-slot's bbox (l,t,w,h fractions) from its inline style, or None."""
    m = re.search(r'<[^>]*data-slot\s*=\s*"HEADLINE"[^>]*style\s*=\s*"([^"]*)"', html,
                  re.IGNORECASE)
    if not m:
        m = re.search(r'<[^>]*class\s*=\s*"[^"]*headline[^"]*"[^>]*style\s*=\s*"([^"]*)"', html,
                      re.IGNORECASE)
    if not m:
        return None
    s = m.group(1)

    def pct(key):
        mm = _PCT_RE[key].search(s)
        return float(mm.group(1)) / 100.0 if mm else None
    l, t, w, h = pct("left"), pct("top"), pct("width"), pct("height")
    if None in (l, t, w, h):
        return None
    return (l, t, w, h)


def output_flat_isolated(html: str) -> dict:
    """Read the output's pill/callout containers: are they axis-aligned (no rotate) AND isolated
    (not overlapping the headline bbox)? Returns {flat_isolated, n_pills, n_overlapping,
    n_rotated}."""
    head = _headline_bbox(html)
    pills: list[dict] = []
    for m in re.finditer(r"<(div|span|a|figure)\b([^>]*)>", html, re.IGNORECASE):
        attrs = m.group(2)
        cls = re.search(r'class\s*=\s*"([^"]*)"', attrs, re.IGNORECASE)
        slot = re.search(r'data-slot\s*=\s*"([^"]*)"', attrs, re.IGNORECASE)
        ident = (cls.group(1) if cls else "") + " " + (slot.group(1) if slot else "")
        if not PILL_SELECTOR_RE.search(ident):
            continue
        style_m = re.search(r'style\s*=\s*"([^"]*)"', attrs, re.IGNORECASE)
        style = style_m.group(1) if style_m else ""
        rotated = bool(ROTATE_RE.search(style)) or bool(ROTATE_RE.search(attrs))

        def pct(key):
            mm = _PCT_RE[key].search(style)
            return float(mm.group(1)) / 100.0 if mm else None
        left, right, top = pct("left"), pct("right"), pct("top")
        # Approx horizontal position of the pill: left edge, or (1-right) when right-anchored.
        x = left if left is not None else (1.0 - right if right is not None else None)
        overlaps_head = False
        if head is not None and top is not None and x is not None:
            hl, ht, hw, hh = head
            overlaps_head = (ht <= top <= ht + hh) and (hl <= x <= hl + hw)
        pills.append({"rotated": rotated, "overlaps_head": overlaps_head,
                      "ident": ident.strip()[:32]})
    n_rot = sum(1 for p in pills if p["rotated"])
    n_overlap = sum(1 for p in pills if p["overlaps_head"])
    # Flat-isolated when there ARE pills and NONE is rotated/tilted. Reproducing a WOVEN ref look
    # in HTML requires tilt (transform: rotate) — axis-aligned pills are flat chips by definition,
    # regardless of where they sit. (The bbox-overlap count is recorded for info but is noisy: a
    # headline div legitimately spans most of the canvas, so a pill in clear space at the bottom
    # still falls "inside" the headline bbox — overlap alone does not prove a true weave.)
    flat_isolated = bool(pills) and n_rot == 0
    return {"flat_isolated": flat_isolated, "n_pills": len(pills),
            "n_overlapping": n_overlap, "n_rotated": n_rot}


def evaluate(html: str, ref: Image.Image | None, accent_hex: str) -> dict:
    """Verdict dict. Indeterminate (ok=True) when no ref, no accent signal, or no pills."""
    base = {"ok": True, "mis_route": False, "indeterminate": True, "ref": None, "output": None,
            "reason": ""}
    if ref is None:
        base["reason"] = "no ref-canonical — cannot read the ref's signature (indeterminate)"
        return base
    ref_sig = ref_woven_signature(ref, accent_hex)
    out_sig = output_flat_isolated(html)
    base["ref"] = ref_sig
    base["output"] = out_sig
    if out_sig["n_pills"] == 0:
        base["reason"] = "no pill/callout containers in the output — gate not applicable"
        return base
    if not ref_sig["is_woven"]:
        base["indeterminate"] = False
        base["reason"] = (f"ref signature is NOT woven (accent devices in band="
                          f"{ref_sig['n_devices']}, tilted={ref_sig['n_tilted']}) — no woven→flat "
                          f"mis-route to flag")
        return base
    base["indeterminate"] = False
    if out_sig["flat_isolated"]:
        base["mis_route"] = True
        base["ok"] = False
        base["reason"] = (
            f"woven→flat mis-route: ref-canonical shows a WOVEN composition signature "
            f"({ref_sig['n_devices']} vivid device pills in the headline band, "
            f"{ref_sig['n_tilted']} reading tilted/overlapping — Form C signature: pills woven "
            f"THROUGH the headline), but the output shipped {out_sig['n_pills']} FLAT "
            f"axis-aligned isolated container(s) (none rotated/tilted — flat chips, not woven "
            f"type). The gates trusted the "
            f"rationale's self-declared flat form and checked the output against THAT; this "
            f"reads the REF's signature directly (the run-08 highlight-pills mis-route). If the "
            f"woven look is intended in HTML, the pills must actually overlap/tilt across the "
            f"headline (z-index over the headline bbox, transform: rotate, icon-anchored) — not "
            f"sit isolated in the right margin. Else re-read the ref (this is a Form C "
            f"composition).")
    else:
        base["reason"] = (f"ref is woven and the output reproduces the weave "
                          f"({out_sig['n_overlapping']} pill(s) overlap the headline, "
                          f"{out_sig['n_rotated']} rotated) — no mis-route")
    return base


def main() -> int:
    _force_utf8_streams()
    ap = argparse.ArgumentParser(
        description="FORM-VS-REF SIGNATURE — flag a woven ref shipped as flat isolated chips.")
    ap.add_argument("--template-html", required=True, type=Path)
    ap.add_argument("--ref", type=Path, default=None,
                    help="ref-canonical.png. Default: <template-dir>/assets/ref-canonical.png.")
    ap.add_argument("--accent", type=str, default=None,
                    help="brand accent #rrggbb. Default: auto-discover from brand tokens.json.")
    ap.add_argument("--enforce", dest="enforce", action="store_true", default=False,
                    help="block (exit 2) on a mis-route + feed the ladder. Default: advisory.")
    ap.add_argument("--no-enforce", dest="enforce", action="store_false")
    args = ap.parse_args()

    if not args.template_html.exists():
        print(f"Error: template.html not found: {args.template_html}", file=sys.stderr)
        return 1
    html = args.template_html.read_text(encoding="utf-8")
    ref_path = args.ref or (args.template_html.parent / "assets" / "ref-canonical.png")
    ref = Image.open(ref_path).convert("RGB") if ref_path.exists() else None
    if ref is None:
        print(f"  note: ref-canonical not found ({ref_path}) — indeterminate", file=sys.stderr)

    try:
        accent_hex, accent_source = resolve_accent(args.accent, args.template_html)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    if accent_source != "default":
        print(f"  note: accent {accent_hex} ({accent_source})", file=sys.stderr)

    res = evaluate(html, ref, accent_hex)
    print(f"FORM-VS-REF SIGNATURE on {args.template_html.parent.name}:")
    if res["ref"] is not None:
        print(f"  ref: woven={res['ref']['is_woven']} devices={res['ref']['n_devices']} "
              f"tilted={res['ref']['n_tilted']} vivid_frac={res['ref']['vivid_frac']}")
    if res["output"] is not None:
        print(f"  output: flat_isolated={res['output']['flat_isolated']} "
              f"pills={res['output']['n_pills']} overlapping={res['output']['n_overlapping']} "
              f"rotated={res['output']['n_rotated']}")
    verdict = ("INDETERMINATE" if res["indeterminate"] else
               ("PASS" if res["ok"] else ("FAIL" if args.enforce else "WARN")))
    print(f"  verdict = {verdict} — {res['reason']}")
    if res["ok"]:
        return 0
    tag = "fail" if args.enforce else "warn"
    print(f"[{tag}] {res['reason']}", file=sys.stderr)
    return 2 if args.enforce else 0


if __name__ == "__main__":
    sys.exit(main())
