#!/usr/bin/env python3
"""
voice_evaluator.py — the felt-verdict loop closure (hg-verdict-to-evaluator, minted).

WHY (apex W2, 2026-07-29): 38 felt verdicts sat in calibration-log.md with ZERO
programmatic readers. The tool specified to fix this (hg-verdict-to-evaluator,
built 07-28) never fired; the next day the log took its largest FAIL in history
(profile-copy v3) — the exact failure class it existed to prevent. This module
IS the mint: the log's Column A/B data becomes a fireable check.

Two layers, honest about what each can do:
  1. TELL CLASSES (deterministic) — stable, machine-checkable patterns distilled
     from logged FAILs, each carrying its log citation. These catch the *letter*.
  2. LIVE BAR (data-driven, zero hand-sync) — the most recent FAIL/RULE rows
     parsed from calibration-log.md verbatim, printed for the pen. New verdicts
     strengthen the evaluator the moment voice_ratchet writes them. This
     carries the *spirit* — including the un-regexable rules (reader-turn,
     ban-list-vs-architecture, owned visuals).

Compass: reports and nudges, never blocks. Exit 0 always (--strict exits 1 on
tell hits, for pipelines that opt in).

Usage:
  python3 execution/voice_evaluator.py check <file> [--strict]
  python3 execution/voice_evaluator.py bar [--n 8]     # print the live bar only
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAL_LOG = ROOT / "_active" / "farrice-brand" / "voice" / "calibration-log.md"

# Layer 1 — tell classes. Each: (name, regex, log citation).
TELLS = [
    ("room-abstraction",
     re.compile(r"\b(the only room|in a room where|the room where)\b", re.I),
     "2026-07-28/29: 'room' as abstraction — he says the plain named place"),
    ("grand-noun-labeling",
     re.compile(r"\b(That'?s where the \w+ comes from|The work (usually |always )?(starts|begins)|the exact distance between)\b", re.I),
     "2026-07-29: grand-noun labeling reads false prestige"),
    ("theatrical-repetition",
     re.compile(r"\bIt (doesn'?t|never) \w+\. It never (once )?\w+", re.I),
     "2026-07-28: 'It doesn't speak. It never once spoke' — writing-performance"),
    ("setup-phrase",
     re.compile(r"\b(So watch what (actually )?happens|Here'?s (what|why|how|the (part|thing)))\b", re.I),
     "2026-07-22: setup phrases announce; the piece goes straight in"),
    ("not-x-but-y-reveal",
     re.compile(r"\bIt'?s not (a |an |the )?\w+([\w\s]{0,20})?\. It'?s (a |an |the )?\w+", re.I),
     "ban bank: 'It's not X. It's Y.' reveal"),
    ("em-dash-density", None,  # counted, not regexed
     "voice law: no em-dashes in his register (voice_ratchet FAILs 2026-07-29)"),
    ("exclamation", re.compile(r"!"),
     "voice law: quiet defiance — no exclamation marks"),
    ("generic-question-close",
     re.compile(r"\?(\s*)$"),
     "2026-05-05 RULE-CHANGE: generic question closes banned (earned questions ok — judgment)"),
]


def parse_log_rows():
    """Yield (date, verdict, line, why) from calibration-log.md table rows."""
    if not CAL_LOG.exists():
        return []
    rows = []
    for raw in CAL_LOG.read_text().splitlines():
        if not raw.startswith("|") or raw.startswith("|-") or raw.startswith("| Date"):
            continue
        cells = [c.strip() for c in raw.strip("|").split("|")]
        if len(cells) >= 4 and re.match(r"\d{4}-\d{2}-\d{2}", cells[0]):
            rows.append(tuple(cells[:4]))
    return rows


def live_bar(n: int = 8) -> str:
    rows = [r for r in parse_log_rows() if r[1].upper() in ("FAIL", "RULE", "RULE-CHANGE")]
    rows = rows[-n:]
    out = [f"LIVE BAR — the {len(rows)} most recent FAIL/RULE verdicts (calibration-log.md, read live):"]
    for date, verdict, line, why in rows:
        out.append(f"  [{date} {verdict}] {line[:110]}")
        out.append(f"      why: {why[:130]}")
    return "\n".join(out)


def check(path: Path, strict: bool) -> int:
    text = path.read_text(errors="replace")
    hits = []
    for name, rx, cite in TELLS:
        if name == "em-dash-density":
            n = text.count("—")
            if n > 2:
                hits.append((name, f"{n} em-dashes", cite))
            continue
        if rx is None:
            continue
        m = rx.search(text)
        if m:
            if name == "generic-question-close":
                # only flag if the final non-empty line ends with ?
                last = [l for l in text.splitlines() if l.strip()][-1] if text.strip() else ""
                if not last.rstrip().endswith("?"):
                    continue
                m_txt = last.strip()[:60]
            else:
                m_txt = m.group(0)[:60]
            hits.append((name, m_txt, cite))
    print(f"VOICE EVALUATOR — {path.name}")
    if hits:
        print(f"  {len(hits)} tell-class hit(s) (deterministic layer):")
        for name, frag, cite in hits:
            print(f"  ✗ {name}: \"{frag}\"")
            print(f"      scar: {cite}")
    else:
        print("  ✓ no deterministic tell-class hits")
    print()
    print(live_bar())
    print()
    print("Judgment checks the pen answers itself (un-regexable, from the log):")
    print("  · Reader-turn present? ('why should the inbound lead care' — the v10-v14/v3 killer)")
    print("  · Owned visual over abstraction? (the shelf of half-used tubs beats any clever line)")
    print("  · At least one flat sentence doing ordinary work? (every-sentence-a-gem IS the tell)")
    print("  · Briefed from an architecture, not a ban list? (v3 scar, 2026-07-29)")
    return 1 if (strict and hits) else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check")
    c.add_argument("file")
    c.add_argument("--strict", action="store_true")
    b = sub.add_parser("bar")
    b.add_argument("--n", type=int, default=8)
    args = ap.parse_args()
    if args.cmd == "bar":
        print(live_bar(args.n))
        return 0
    return check(Path(args.file), args.strict)


if __name__ == "__main__":
    sys.exit(main())
