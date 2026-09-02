#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Check E — the palette-token gate (the brand-substitution leak check, RC-A leak channel 1).

Sibling of check_rationale.py / check_treatment_contract.py. A SCRIPT-measured floor the builder
runs AT the gate (Step 6). Where Check B binds the per-block TREATMENT to the rationale, Check E
binds the per-block PALETTE to the BRAND TOKENS — it catches the leak where the reference image's
own colours survive into the rationale/template instead of being REMAPPED to brand tokens.

WHAT IT VERIFIES (deterministic, accent-agnostic, no hardcoded brand hexes):
  Every literal hex colour (`#rgb` / `#rrggbb` / `#rrggbbaa`) that appears in rationale.md or
  template.html MUST be a colour the BRAND declares in tokens.json (the `colors` map — any of
  primary / accent / bg_* / text_* / border_* …), within a small per-channel tolerance. A literal
  hex that is NOT a brand token is a LEAK: it describes the REF, not the template (the run-08
  list-on-object miss — the ref's lime-green `#b5e853` kept as the template palette; a
  fullbleed-photo-cover headline `fill: white` copied from a ref against the brand "ink for headlines"
  rule). Authoring brand colour the right way is `var(--brand-*)` / a token NAME (accent/ink/paper/…)
  — never a baked literal hex (`template-conventions.md`: "Hardcoding hex colors in template.html ❌").

WHY (the run-08 RC-A lesson): the builder reads the ref correctly for FORM, then lets the ref's
literal CONTENT — its palette — leak through. "Preserve the surface structure" must EXCLUDE
preserving the ref's palette: the ref's colours describe the ref, the template's colours are the
brand's tokens, chosen for legibility against their background. This check is the deterministic
catch for that leak — it does NOT judge whether the remap is tasteful (that is by-eye); it only
refuses a literal off-token hex that proves the ref's palette was transcribed, not re-derived.

NOT in scope: a near-white headline `fill` that IS a brand token (e.g. paper/text-on-dark) on a
DARK surface is legitimate and passes — legibility-against-background is the by-eye + contrast gate's
job (measure_text_contrast.py), not this token check. This check answers only "is every literal hex
a brand token?".

ADVISORY vs BLOCKING: mirrors the existing PALETTE posture (`shared/quality-gate.md`: palette is
"flag-only in v1" — the gate WARNS, never auto-recolors). Default is ADVISORY (exit 0, prints
`[warn]`). Pass `--enforce` to make a leak BLOCK (exit 2) and feed the 3-try ladder — the gate
sequence wires it advisory-by-default so it surfaces the leak without halting an otherwise-good build,
exactly like the palette-stray flag and the image-medium conference.

Exit codes:
  0  -> no off-token hex (or advisory mode: leaks found but not enforced) -> proceed.
  1  -> usage / file-not-found error.
  2  -> --enforce AND >=1 off-token hex found -> BLOCK.

Usage:
    uv run check_palette_tokens.py --tokens {brand_context}/visual-identity/tokens.json \
        --rationale {template_dir}/rationale.md --template-html {template_dir}/template.html [--enforce]
"""
import argparse
import json
import re
import sys
from pathlib import Path


def _force_utf8_streams() -> None:
    """UTF-8 stdout/stderr so reason glyphs never crash a cp1252 Windows console."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except (ValueError, OSError):
                pass


# A literal hex colour: #rgb, #rrggbb, or #rrggbbaa. Word-bounded so a longer token isn't split.
HEX_RE = re.compile(r"#[0-9a-fA-F]{3,8}\b")

# Per-channel tolerance (0-255) — a brand token authored with a 1-2 step rounding still counts as
# the token, but a genuinely different colour (the ref's lime-green vs the brand coral) does not.
DEFAULT_TOLERANCE = 6


def expand_hex(h: str) -> tuple[int, int, int] | None:
    """Normalize a hex string to an (r, g, b) tuple (0-255); drop alpha. None if unparseable."""
    s = h.lstrip("#")
    if len(s) == 3:  # #rgb -> #rrggbb
        s = "".join(c * 2 for c in s)
    elif len(s) == 8:  # #rrggbbaa -> drop alpha
        s = s[:6]
    elif len(s) == 4:  # #rgba -> drop alpha, expand
        s = "".join(c * 2 for c in s[:3])
    if len(s) != 6:
        return None
    try:
        return (int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16))
    except ValueError:
        return None


def load_brand_hexes(tokens: dict) -> set[tuple[int, int, int]]:
    """Collect every (r,g,b) the brand declares under tokens.json `colors` (values may carry a
    suffix like '#FFFFFF (bg)' in ai-image-style.md style — extract the hex). Accent-agnostic:
    it reads whatever the brand declares, never a hardcoded brand hue."""
    rgbs: set[tuple[int, int, int]] = set()
    colors = tokens.get("colors", {})
    if isinstance(colors, dict):
        values = list(colors.values())
    elif isinstance(colors, list):
        values = list(colors)
    else:
        values = []
    for v in values:
        if not isinstance(v, str):
            continue
        for m in HEX_RE.findall(v):
            rgb = expand_hex(m)
            if rgb is not None:
                rgbs.add(rgb)
    return rgbs


def is_brand_token(rgb: tuple[int, int, int], brand: set[tuple[int, int, int]], tol: int) -> bool:
    """True when rgb matches any brand token within per-channel tolerance."""
    for br, bg, bb in brand:
        if abs(rgb[0] - br) <= tol and abs(rgb[1] - bg) <= tol and abs(rgb[2] - bb) <= tol:
            return True
    return False


def find_leaks(text: str, brand: set[tuple[int, int, int]], tol: int) -> list[str]:
    """Return the sorted unique off-token literal hexes found in `text`."""
    leaks: set[str] = set()
    for raw in HEX_RE.findall(text):
        rgb = expand_hex(raw)
        if rgb is None:
            continue
        if not is_brand_token(rgb, brand, tol):
            leaks.add(raw.lower())
    return sorted(leaks)


def evaluate(sources: dict[str, str], brand: set[tuple[int, int, int]], tol: int) -> dict:
    """Pure verdict: scan each named source for off-token hexes (unit-tested)."""
    per_source: dict[str, list[str]] = {}
    for name, text in sources.items():
        leaks = find_leaks(text, brand, tol)
        if leaks:
            per_source[name] = leaks
    all_leaks = sorted({h for hs in per_source.values() for h in hs})
    ok = not all_leaks
    if ok:
        reason = "every literal hex is a brand token (no ref-palette leak)"
    else:
        parts = [f"{name}: {', '.join(hs)}" for name, hs in per_source.items()]
        reason = ("off-token hex(es) — the ref's palette leaked instead of being remapped to brand "
                  "tokens (author brand colour as var(--brand-*) / a token, never a literal ref hex): "
                  + " · ".join(parts))
    return {"ok": ok, "leaks": all_leaks, "per_source": per_source, "reason": reason}


def main() -> int:
    _force_utf8_streams()
    ap = argparse.ArgumentParser(description="Check E — palette-token (ref-palette leak) gate.")
    ap.add_argument("--tokens", required=True, type=Path, help="brand tokens.json")
    ap.add_argument("--rationale", type=Path, help="template rationale.md")
    ap.add_argument("--template-html", type=Path, help="template.html")
    ap.add_argument("--tolerance", type=int, default=DEFAULT_TOLERANCE,
                    help=f"per-channel match tolerance 0-255 (default {DEFAULT_TOLERANCE})")
    ap.add_argument("--enforce", action="store_true",
                    help="BLOCK (exit 2) on a leak instead of the default advisory WARN (exit 0)")
    args = ap.parse_args()

    if not args.tokens.exists():
        print(f"[error] tokens.json not found: {args.tokens}", file=sys.stderr)
        return 1
    if not args.rationale and not args.template_html:
        print("[error] pass at least one of --rationale / --template-html", file=sys.stderr)
        return 1

    try:
        tokens = json.loads(args.tokens.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        print(f"[error] cannot read tokens.json: {e}", file=sys.stderr)
        return 1

    brand = load_brand_hexes(tokens)
    if not brand:
        print("[error] tokens.json declares no `colors` hexes — cannot resolve brand palette",
              file=sys.stderr)
        return 1

    sources: dict[str, str] = {}
    for label, path in (("rationale.md", args.rationale), ("template.html", args.template_html)):
        if path is None:
            continue
        if not path.exists():
            print(f"[error] not found: {path}", file=sys.stderr)
            return 1
        sources[label] = path.read_text(encoding="utf-8")

    res = evaluate(sources, brand, args.tolerance)

    print("Check E — palette-token (ref-palette leak) gate:")
    print(f"  verdict = {'PASS' if res['ok'] else ('BLOCK' if args.enforce else 'WARN')} — {res['reason']}")
    if res["ok"]:
        return 0
    if args.enforce:
        print(f"[block] {res['reason']}", file=sys.stderr)
        return 2
    print(f"[warn] {res['reason']}", file=sys.stderr)
    print("  (advisory — palette is flag-only by default; pass --enforce to block + feed the ladder)",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
