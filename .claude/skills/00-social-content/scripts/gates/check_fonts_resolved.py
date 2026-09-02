#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Gate hook A (SPEC-C C3) — assert the brand display @font-face actually loaded.

Sibling of check_rationale.py / measure_text_contrast.py. Guards the decisive
test-09-06 plumbing bug from silently regressing: the pool's `_shared/styles.css`
carries the brand `@font-face` with RELATIVE urls, and Playwright's set_content()
bakes against `about:blank` (no base URL) — so an un-inlined sheet leaves the brand
display family unresolved and every HTML headline falls back to system sans. A PNG
diff doesn't catch it (the layout looks "fine"); only `document.fonts.check` does.

HOW IT WORKS: render_template.py, after `document.fonts.ready`, evaluates
`document.fonts.check('400 100px "<brand-display>"')` and writes the verdict to a
sidecar `<output>.fontcheck.json` next to the baked PNG. This script reads that
sidecar — it does NOT re-render (it asserts against the artifact the real bake
produced, exactly like measure_text_contrast.py reads the produced preview.png).

PRINCIPLE (SPEC-r5g): **a gate must never be satisfiable by ADDING visible
elements.** `document.fonts.check` only reports a face as loaded when something in
the page actually USED it — so a template with NO HTML text in the display family
could never pass, and the run-06 builder "fixed" that by injecting a visible ghost
word (monitor-surface-cover's DECORATIVE_WORD) just to make the face load. That is
the perverse incentive this gate must not create. Therefore: when the template has
no HTML text in the display family, the unresolved verdict is NOT a failure —

  - if the sidecar carries `probe_resolved` (a renderer that force-loads the face
    via the invisible `document.fonts.load()` probe, no DOM text involved), that
    verdict is used;
  - otherwise the gate SKIPS (exit 0) with an explicit note. It never demands
    visible text.

Pass `--template-html <dir>/template.html` to enable the not-applicable detection;
without it the script auto-discovers `template.html` next to the baked PNG (the
standard template-dir layout), so the existing gate invocation gets the fix free.

Exit codes:
  0  -> brand display family resolved (or no display-font HTML text to check -> SKIP).
  1  -> usage / sidecar-not-found error.
  2  -> the template USES the display family in HTML text and it did NOT resolve
        -> BLOCK (re-roll / fix @font-face inlining).

Usage:
    uv run check_fonts_resolved.py --render-output <path>/slide.png
    uv run check_fonts_resolved.py --fontcheck <path>/slide.png.fontcheck.json
    uv run check_fonts_resolved.py --render-output <path>/preview.png \
        --template-html <path>/template.html
"""
import argparse
import json
import re
import sys
from pathlib import Path

# CSS custom-property names a template uses to reference the brand display face
# (`font-family: var(--brand-display, ...)` / `var(--font-display, ...)`).
DISPLAY_FONT_VAR_HINTS = ("--brand-display", "--font-display", "--display-font")

_FONT_FACE_BLOCK_RE = re.compile(r"@font-face\s*\{[^}]*\}", re.IGNORECASE | re.DOTALL)
_FONT_FAMILY_DECL_RE = re.compile(r"font-family\s*:\s*([^;}{]+)", re.IGNORECASE)


def template_uses_display_font(html: str, family: str | None) -> bool:
    """True when template.html has a font-family declaration that USES the display face —
    by literal family name or via a display-font custom property. @font-face blocks are
    stripped first (declaring a face is not using it)."""
    html_wo_faces = _FONT_FACE_BLOCK_RE.sub("", html)
    for m in _FONT_FAMILY_DECL_RE.finditer(html_wo_faces):
        decl = m.group(1).lower()
        if family and family.lower() in decl:
            return True
        if any(hint in decl for hint in DISPLAY_FONT_VAR_HINTS):
            return True
    return False


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--render-output", type=Path,
        help="Path to the baked PNG; its sidecar <output>.fontcheck.json is read.",
    )
    ap.add_argument(
        "--fontcheck", type=Path,
        help="Path to the .fontcheck.json sidecar directly (overrides --render-output).",
    )
    ap.add_argument(
        "--template-html", type=Path, default=None,
        help="template.html for the not-applicable detection (no display-font HTML text -> "
             "SKIP instead of fail). Defaults to template.html next to --render-output.",
    )
    args = ap.parse_args()

    sidecar = args.fontcheck
    if sidecar is None and args.render_output is not None:
        sidecar = args.render_output.with_suffix(args.render_output.suffix + ".fontcheck.json")
    if sidecar is None:
        print("Error: pass --render-output <png> OR --fontcheck <json>", file=sys.stderr)
        return 1
    if not sidecar.is_file():
        print(
            f"Error: font-check sidecar not found: {sidecar}\n"
            f"  Re-bake with the current render_template.py (it writes "
            f"<output>.fontcheck.json after document.fonts.ready).",
            file=sys.stderr,
        )
        return 1

    try:
        data = json.loads(sidecar.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        print(f"Error: cannot read sidecar {sidecar}: {e}", file=sys.stderr)
        return 1

    fam = data.get("family")
    resolved = bool(data.get("resolved"))
    if resolved:
        print(f"[ok] brand display font \"{fam}\" resolved in the bake")
        return 0

    # Invisible-probe verdict (a renderer that force-loads the face via
    # document.fonts.load() — no DOM text involved) wins over the usage-based check.
    if "probe_resolved" in data:
        if bool(data.get("probe_resolved")):
            print(f"[ok] brand display font \"{fam}\" resolved via the invisible "
                  f"document.fonts.load() probe (no visible text required)")
            return 0
        print(
            f"[fail] brand display font \"{fam}\" did NOT resolve under the invisible "
            f"document.fonts.load() probe — the @font-face itself is broken (url/inlining). "
            f"Fix the @font-face; do NOT add visible text.",
            file=sys.stderr,
        )
        return 2

    # `document.fonts.check` is usage-based: with no display-font HTML text the face never
    # loads and the verdict is a false negative. SKIP — never demand visible text (a gate
    # must never be satisfiable by ADDING visible elements).
    template_html = args.template_html
    if template_html is None and args.render_output is not None:
        candidate = args.render_output.parent / "template.html"
        if candidate.is_file():
            template_html = candidate
    if template_html is not None and template_html.is_file():
        html = template_html.read_text(encoding="utf-8")
        if not template_uses_display_font(html, fam):
            print(
                f"[skip] brand display font \"{fam}\": the template has NO HTML text in the "
                f"display family, so document.fonts.check cannot observe a load — gate not "
                f"applicable. Do NOT add visible text to satisfy this gate (a gate must "
                f"never be satisfiable by ADDING visible elements). To assert the @font-face "
                f"itself, re-bake with a renderer that probes via document.fonts.load() "
                f"(writes probe_resolved to the sidecar)."
            )
            return 0

    print(
        f"[fail] brand display font \"{fam}\" did NOT load — HTML headlines render in "
        f"system sans. The shared @font-face url(...) must be inlined to base64 before "
        f"add_style_tag (SPEC-C C1). Re-roll after fixing.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())
