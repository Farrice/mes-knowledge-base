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


# ── content class ─────────────────────────────────────────────────────────
# Copy/prose deliverables. Byte checks are the FLOOR (always run, deterministic);
# the ban-bank classifier is a labeled second layer — when it can't run, the
# detail SAYS so instead of silently passing (prose_classifier.py is the SOLE
# ban canon per the slop-ban block in CLAUDE.md).
_PLACEHOLDER = re.compile(r"TODO:|FIXME|\[PLACEHOLDER\]|\[TK\]|lorem ipsum|^<{7} |^={7}$|^>{7} ",
                          re.I | re.M)
_MIN_CONTENT_BYTES = 300


def content_predicate(content: str) -> tuple[bool, str]:
    body = content.split("---", 2)[-1] if content.startswith("---") else content
    if len(body.strip()) < _MIN_CONTENT_BYTES:
        return False, f"stub — {len(body.strip())} bytes of body (floor {_MIN_CONTENT_BYTES})"
    hits = _PLACEHOLDER.findall(body)
    if hits:
        return False, f"{len(hits)} unresolved placeholder/conflict marker(s): {sorted(set(h.strip() for h in hits))[:3]}"
    # layer 2: ban-bank classifier, honestly labeled either way
    import subprocess as _sp
    clf = ROOT / "execution" / "prose_classifier.py"
    try:
        r = _sp.run(["python3", str(clf), "check", "/dev/stdin"],
                    input=content, capture_output=True, text=True, timeout=25)
        if r.returncode != 0:
            tail = (r.stdout or r.stderr).strip().splitlines()
            return False, f"ban-bank fail — {tail[-1][:120] if tail else 'nonzero exit'}"
        return True, "clean (bytes + ban-bank)"
    except Exception:
        return True, "clean (bytes only — classifier unavailable, NOT run)"


# ── code class ────────────────────────────────────────────────────────────
# Scripts must at least be parseable, conflict-free, and non-hollow. compile()
# only — never import: importing arbitrary modules at Stop would run their
# side effects, and a verifier must not mutate what it grades.
_CONFLICT = re.compile(r"^(<{7} |={7}$|>{7} )", re.M)


def code_predicate(content: str) -> tuple[bool, str]:
    if _CONFLICT.search(content):
        return False, "merge-conflict markers present"
    try:
        import warnings
        with warnings.catch_warnings():
            # a scanned file's own SyntaxWarnings (bad escapes) are its
            # problem, not this report's noise — only failure to PARSE fails
            warnings.simplefilter("ignore", SyntaxWarning)
            compile(content, "<artifact>", "exec")
    except SyntaxError as e:
        return False, f"does not parse — SyntaxError line {e.lineno}: {str(e.msg)[:80]}"
    code_lines = [l for l in content.splitlines()
                  if l.strip() and not l.strip().startswith("#")]
    if len(code_lines) < 3:
        return False, f"hollow — {len(code_lines)} code line(s)"
    return True, f"parses clean ({len(code_lines)} code lines)"


FLOORS = {
    "rendered": {
        "description": "HTML surfaces: boards, briefs, rendered markdown",
        "roots": [".agent/", "deliverables/", "_active/"],
        "suffixes": (".html",),
        "predicate": rendered_predicate,
        "fixture": FIXTURES / "rendered_bad.html",
        "fixture_good": FIXTURES / "rendered_good.html",
    },
    "content": {
        "description": "prose deliverables: copy, briefs-as-md, client content",
        "roots": ["deliverables/", "_active/farrice-brand/content/", "_active/clients/"],
        "suffixes": (".md",),
        "predicate": content_predicate,
        "fixture": FIXTURES / "content_bad.md",
        "fixture_good": FIXTURES / "content_good.md",
    },
    "code": {
        "description": "harness scripts",
        "roots": ["execution/"],
        "suffixes": (".py",),
        "predicate": code_predicate,
        "fixture": FIXTURES / "code_bad.py",
        "fixture_good": FIXTURES / "code_good.py",
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
