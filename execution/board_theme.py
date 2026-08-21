#!/usr/bin/env python3
"""board_theme.py — ONE palette for every Readout OS surface (2026-08-21).

WHY (Homebase 2.0 / Agentic OS build): the Ink + Steel Blue token block was
hand-copied across ~8 board generators (homebase, catalog, pulse, mission,
oracle, assets, brief library, mdview). Same scar as surface_nav: the pattern
existed N times and drifted. This module is the single source of truth —
generators interpolate theme_css() into their inline <style> block.

Contract:
  - theme_css() -> the :root / prefers-color-scheme / data-theme CSS text.
    Interpolated as a STRING into each generator's self-contained HTML —
    NEVER a linked stylesheet: boards must render over file:// too
    (dual-mode is load-bearing, see homebase_board.py docstring).
  - TOKENS holds the raw values (light + dark) so a client reskin is one
    alternate dict passed to theme_css(tokens=...) — the "agentic OS for
    clients" path (video harvest 2026-08-21): same OS, swapped skin.
  - Canon: _active/farrice-brand/premium-minimal/REPORT-DIALECT.md +
    package/tokens/design-tokens.json. Do not invent hues here.
"""
from __future__ import annotations

# Farrice Cain Premium Minimal — report dialect (Ink + Steel Blue).
# Values verbatim from templates/research-brief/template.html (implementation
# of record) and the pre-2.0 homebase_board.py block they were extracted from.
TOKENS = {
    "light": {
        "ground": "#f3f3f0", "panel": "#fafaf8", "ink": "#101010",
        "muted": "#8c8c82", "soft": "#555553", "line": "#d8d8d3",
        "accent": "#3d5a94", "ok": "#3e7d5f", "warn": "#a8853e", "crit": "#a85454",
    },
    "dark": {
        "ground": "#0e0e0d", "panel": "#181817", "ink": "#fafaf8",
        "muted": "#8c8c82", "soft": "#b9b9b2", "line": "#2c2c2a",
        "accent": "#7c9fd9", "ok": "#6fae8c", "warn": "#c9a868", "crit": "#c97b73",
    },
    "fonts": {
        "mono": "'JetBrains Mono',ui-monospace,\"SF Mono\",Menlo,Consolas,monospace",
        "sans": "'Helvetica Neue','Neue Haas Grotesk Text Pro',Helvetica,Inter,system-ui,sans-serif",
        "serif": "'Source Serif 4',Georgia,serif",
    },
}


def _vars(mode: dict) -> str:
    return " ".join(f"--{k}:{v};" for k, v in mode.items())


def theme_css(tokens: dict | None = None) -> str:
    """The complete token block: light on :root, dark under the media query
    (guarded so an explicit light choice wins) and under data-theme="dark".
    Single braces — safe to interpolate into f-string templates as a value."""
    t = tokens or TOKENS
    fonts = " ".join(f"--{k}:{v};" for k, v in t["fonts"].items())
    return (
        "/* ── Farrice Cain Premium Minimal — report dialect (board_theme.py) ── */\n"
        f":root {{ {_vars(t['light'])} {fonts} }}\n"
        f"@media (prefers-color-scheme: dark) {{ :root:not([data-theme=\"light\"]) {{ {_vars(t['dark'])} }} }}\n"
        f":root[data-theme=\"dark\"] {{ {_vars(t['dark'])} }}\n"
        f":root[data-theme=\"light\"] {{ {_vars(t['light'])} }}\n"
    )


def self_test() -> int:
    css = theme_css()
    checks = [
        ("steel blue light", "#3d5a94" in css),
        ("steel blue dark", "#7c9fd9" in css),
        ("no unformatted braces pairs", "{{" not in css),
        ("dark media guarded for explicit light", ':not([data-theme="light"])' in css),
        ("fonts shipped", "--mono:" in css and "--sans:" in css and "--serif:" in css),
    ]
    bad = [n for n, ok in checks if not ok]
    print(f"board_theme self-test: {'OK' if not bad else 'FAILED'} "
          f"({len(checks) - len(bad)} passed, {len(bad)} failed)")
    for b in bad:
        print(f"  FAIL: {b}")
    return 0 if not bad else 1


if __name__ == "__main__":
    raise SystemExit(self_test())
