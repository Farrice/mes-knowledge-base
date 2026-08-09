#!/usr/bin/env python3
"""The standard floor — what "done" must mean, per artifact class.

Shape borrowed from Anthropic's own harness guidance
(anthropic.com/engineering/effective-harnesses-for-long-running-agents):
their fix for "Claude declares victory too early" was not a better prompt, it
was a declarative file of acceptance criteria where every item starts FAILING
and the agent may only flip a status field.

And from Nate B. Jones' 2026-08-07 "AI Agent False Success": five LLM judges
scored WORSE THAN A COIN FLIP at telling false success from honest failure —
"the answer is evidence rather than a smarter reviewer." So every floor here is
a deterministic predicate over an artifact's own bytes. No model judges anything.

A floor is a triple:
    roots      — where this class of artifact lands
    predicate  — a function over the artifact's CONTENT, not its existence
    fixture    — a known-bad file the predicate MUST reject.
                 NO FIXTURE, NO FLOOR: the class degrades to UNKNOWN rather
                 than passing. An unexercised predicate is an untested one.

Increment 1 ships ONE class: `rendered`. It is the class that failed on
2026-08-08 — mdview.py emitted raw markdown inside <pre> when its dependency
was missing, every existence check went green, and the operator found it by
clicking.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIXTURES = ROOT / "execution" / "homework_fixtures"

# Strip tags/scripts/styles so we test the layer a HUMAN reads.
_TAG = re.compile(r"<(script|style)\b[^>]*>.*?</\1>", re.S | re.I)
_ANYTAG = re.compile(r"<[^>]+>")
_ENT = {"&lt;": "<", "&gt;": ">", "&amp;": "&", "&quot;": '"', "&#39;": "'", "&nbsp;": " "}

# Markdown that survived into rendered output = the render did not happen.
_HEADING = re.compile(r"^\s{0,3}#{1,6}\s+\S", re.M)
_BOLD = re.compile(r"\*\*[^*\n]{1,80}\*\*")
_TABLE_RULE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*\|", re.M)
_FENCE = re.compile(r"^\s*```", re.M)

# A handful of tokens can be legitimate (a page ABOUT markdown). A wall of them
# is a failed render. Tuned against the real 2026-08-08 specimen: 45 bold +
# 12 headings + 13 table rows.
TRIP = 5


def visible_text(html: str) -> str:
    s = _TAG.sub(" ", html)
    s = _ANYTAG.sub("\n", s)
    for k, v in _ENT.items():
        s = s.replace(k, v)
    return s


def rendered_predicate(content: str) -> tuple[bool, str]:
    """PASS when no wall of raw markdown survived into the visible text."""
    text = visible_text(content)
    counts = {
        "headings": len(_HEADING.findall(text)),
        "bold": len(_BOLD.findall(text)),
        "table-rules": len(_TABLE_RULE.findall(text)),
        "fences": len(_FENCE.findall(text)),
    }
    total = sum(counts.values())
    if total >= TRIP:
        detail = ", ".join(f"{v} {k}" for k, v in counts.items() if v)
        return False, f"{total} unescaped markdown tokens in rendered output ({detail})"
    return True, f"clean ({total} stray token(s), trip at {TRIP})"


FLOORS = {
    "rendered": {
        "description": "HTML surfaces: boards, briefs, rendered markdown",
        "roots": [".agent/", "deliverables/", "_active/"],
        "suffixes": (".html",),
        "predicate": rendered_predicate,
        "fixture": FIXTURES / "rendered_bad.html",
        "fixture_good": FIXTURES / "rendered_good.html",
    },
}


def classify(path: Path) -> str | None:
    rel = str(path).replace(str(ROOT) + "/", "")
    for name, floor in FLOORS.items():
        if path.suffix in floor["suffixes"] and any(rel.startswith(r) for r in floor["roots"]):
            return name
    return None


def check(path: Path) -> tuple[str, str, str]:
    """-> (class, verdict, detail). Verdicts: PROVEN | PARTIAL | UNKNOWN."""
    klass = classify(path)
    if not klass:
        return "", "UNKNOWN", "no floor declared for this artifact class"
    floor = FLOORS[klass]
    fx = floor.get("fixture")
    if not fx or not Path(fx).exists():
        # NO FIXTURE, NO FLOOR — refuse to pass a predicate nothing has exercised.
        return klass, "UNKNOWN", "floor has no fixture — predicate unexercised, refusing to grade"
    try:
        content = path.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        return klass, "UNKNOWN", f"unreadable: {type(e).__name__}"
    ok, detail = floor["predicate"](content)
    return klass, ("PROVEN" if ok else "PARTIAL"), detail


def self_test() -> int:
    """Every predicate must REJECT its bad fixture and ACCEPT its good one."""
    ok, bad = 0, []
    for name, floor in FLOORS.items():
        fx, fg = Path(floor["fixture"]), Path(floor["fixture_good"])
        if not fx.exists() or not fg.exists():
            bad.append(f"{name}: fixture missing ({fx.name} / {fg.name})")
            continue
        passed, d = floor["predicate"](fx.read_text())
        if passed:
            bad.append(f"{name}: predicate ACCEPTED its known-bad fixture — vacuous ({d})")
        else:
            ok += 1
        passed, d = floor["predicate"](fg.read_text())
        if not passed:
            bad.append(f"{name}: predicate REJECTED its known-good fixture — false red ({d})")
        else:
            ok += 1
    print(f"standard_floor self-test: {'OK' if not bad else 'FAILED'} "
          f"({ok} passed, {len(bad)} failed)")
    for b in bad:
        print(f"  FAIL: {b}")
    return 0 if not bad else 1


if __name__ == "__main__":
    import sys
    raise SystemExit(self_test())
