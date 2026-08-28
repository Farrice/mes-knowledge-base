#!/usr/bin/env python3
"""Diff the intake-pack's ## section headers against the FROZEN baseline shape.

Stems are compared (parentheticals are per-document source-notes; the baseline's
'he watches' normalizes to 'they watch' for a client pack). Order matters.
Usage: verify_intake_shape.py <intake-pack.md>
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASELINE = ROOT / "extractions" / "kallaway" / "baseline-input-pack.md"


def stems(path, stop_at=None):
    out = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        m = re.match(r"^## (.+)$", line)
        if not m:
            continue
        h = m.group(1)
        if stop_at and h.startswith(stop_at):
            break
        h = re.sub(r"\s*\(.*\)\s*$", "", h)          # drop trailing parenthetical source-note
        h = h.replace("he watches", "they watch")     # baseline is Farrice-specific
        out.append(h.strip())
    return out


base = stems(BASELINE)
pack = stems(sys.argv[1], stop_at="Engagement routing")

print(f"baseline sections ({len(base)}):")
ok = True
for i in range(max(len(base), len(pack))):
    b = base[i] if i < len(base) else "<MISSING>"
    p = pack[i] if i < len(pack) else "<MISSING>"
    mark = "OK " if b == p else "DIFF"
    if b != p:
        ok = False
    print(f"  {i + 1}. [{mark}] baseline: {b!r:55s} pack: {p!r}")
print("SHAPE MATCH: section-for-section" if ok else "SHAPE MISMATCH")
sys.exit(0 if ok else 1)
