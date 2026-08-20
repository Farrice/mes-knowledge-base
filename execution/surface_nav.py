#!/usr/bin/env python3
"""surface_nav — ONE nav for every branded surface. No more dead pages.

WHY (Farrice, 2026-08-08): "I don't want it to just be a dead page where I
can't navigate back to anything... work fluently through these different home
bases." Measured that day: pulse-board (4 links), mission-control (3), oracle
(3) each carried a HAND-COPIED homenav; assets-board had ZERO; every brief and
every mdview page had ZERO — render_brief.py and mdview.py passed only a title
into {{NAV}}. The pattern existed three times and was never centralized, so two
surfaces missed it and every document was a cul-de-sac.

This module is the single source of truth. Surfaces call nav_html() and never
hand-write the link set again. Adding a home base here adds it EVERYWHERE on
the next render.

Contract:
  - nav_html(current=...) -> one <span class="homenav" data-surface-nav="1">.
    The data attribute is the assertion hook: verify step greps for it across
    .agent/**/*.html. `current` (a key below) renders that link dimmed/unlinked.
  - Self-contained: ships its own guarded <style> so it looks right even on a
    page whose CSS never heard of .homenav (briefs, mdview).
  - links() -> [(key, label, Path)] for tests: every target must exist on disk.
    A nav pointing at a missing board is the same dead channel in a new costume.
"""
from __future__ import annotations

import html as _html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# key -> (label, target path). ORDER IS THE DISPLAY ORDER.
HOME_BASES = {
    "homebase": ("🏠 homebase",      ROOT / ".agent" / "homebase" / "homebase.html"),
    "pulse":   ("⚡ pulse",         ROOT / ".agent" / "pulse" / "pulse-board.html"),
    "missions": ("🎯 mission control", ROOT / ".agent" / "missions" / "mission-control.html"),
    "briefs":  ("📋 briefing room",  ROOT / "deliverables" / "research-briefs" / "index.html"),
    "assets":  ("🎨 asset board",    ROOT / ".agent" / "assets" / "assets-board.html"),
    "oracle":  ("🔮 oracle",         ROOT / ".agent" / "oracle" / "oracle-dashboard.html"),
    "docs":    ("📄 docs",           ROOT / ".agent" / "mdview" / "index.html"),
}

# key -> pulse_serve route. When a surface is opened over http, file:// links
# in the nav are dead (browsers refuse the scheme hop) — worse, routing them
# through open-path pops a STATIC file:// copy and silently drops the operator
# out of live mode. The nav script below rewrites hrefs to these routes on
# http pages, so navigation between home bases stays inside the live server.
ROUTES = {
    "homebase": "/",
    "pulse": "/pulse",
    "missions": "/missions",
    "briefs": "/room",
    "assets": "/assets",
    "oracle": "/oracle",
    "docs": "/repo/.agent/mdview/index.html",
}

# Guarded style: injected once per page, namespaced, so briefs/mdview render the
# nav correctly without depending on each surface's own CSS. Boards that already
# define .homenav simply override nothing — same class, same look.
_STYLE = (
    '<style data-surface-nav-style="1">'
    '.homenav{margin-left:auto;display:flex;gap:6px;align-items:center;flex-wrap:wrap}'
    '.homenav a,.homenav .here{font-family:"SF Mono",Menlo,monospace;font-size:9px;'
    'letter-spacing:.14em;text-transform:uppercase;text-decoration:none;'
    'border:1px solid rgba(127,127,127,.35);border-radius:99px;padding:4px 11px;'
    'color:inherit;opacity:.75}'
    '.homenav a:hover{opacity:1;border-color:currentColor}'
    '.homenav .here{opacity:.45;border-style:dashed}'
    '</style>'
)


def links() -> list[tuple[str, str, Path]]:
    return [(k, label, path) for k, (label, path) in HOME_BASES.items()]


# Guarded script: on an http page, swap each nav link's file:// href for its
# live server route (data-route). Idempotent per page; file:// pages untouched.
_LIVE_SCRIPT = (
    '<script data-surface-nav-live="1">'
    "if(location.protocol.indexOf('http')===0){"
    "document.querySelectorAll('.homenav a[data-route]').forEach(function(a){"
    "a.href=a.dataset.route;});}"
    '</script>'
)


def nav_html(current: str | None = None, style: bool = True) -> str:
    parts = []
    for key, (label, path) in HOME_BASES.items():
        lab = _html.escape(label) + " ↗"
        if key == current:
            parts.append(f'<span class="here">{_html.escape(label)}</span>')
        else:
            route = f' data-route="{_html.escape(ROUTES[key])}"' if key in ROUTES else ""
            parts.append(f'<a href="{_html.escape(path.as_uri())}"{route}>{lab}</a>')
    return ((_STYLE if style else "")
            + f'<span class="homenav" data-surface-nav="1">{"".join(parts)}</span>'
            + _LIVE_SCRIPT)


def self_test() -> int:
    ok, bad = 0, []

    def check(name, cond):
        nonlocal ok
        ok += 1 if cond else 0
        if not cond:
            bad.append(name)

    h = nav_html()
    check("marker attribute present", 'data-surface-nav="1"' in h)
    check("all bases linked", all(k in ("docs",) or HOME_BASES[k][0].split(" ", 1)[1] in h
                                  for k in HOME_BASES))
    check("current renders unlinked", '<span class="here">' in nav_html(current="pulse"))
    check("current is not also a link",
          nav_html(current="pulse").count("pulse-board.html") == 0)
    # every target must exist on disk — a nav to a missing board is a dead channel
    missing = [k for k, _, p in links() if not p.exists()]
    check(f"every target exists on disk (missing: {missing})", not missing)
    check("live-route script shipped", 'data-surface-nav-live="1"' in h)
    stray = [k for k in ROUTES if k not in HOME_BASES]
    check(f"every route maps a real base (stray: {stray})", not stray)
    unrouted = [k for k in HOME_BASES if k not in ROUTES]
    check(f"every base has a live route (unrouted: {unrouted})", not unrouted)
    print(f"surface_nav self-test: {'OK' if not bad else 'FAILED'} ({ok} passed, {len(bad)} failed)")
    for b in bad:
        print(f"  FAIL: {b}")
    return 0 if not bad else 1


if __name__ == "__main__":
    raise SystemExit(self_test())
