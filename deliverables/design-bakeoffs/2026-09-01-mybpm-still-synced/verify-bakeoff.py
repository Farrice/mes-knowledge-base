#!/usr/bin/env python3
"""Deterministic parity and render checks for the blind composition bake-off."""

from __future__ import annotations

import json
import re
import struct
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REQUIRED_COPY = (
    "Week 1 / Still Synced",
    "Met strangers.",
    "Found family.",
    "03:17 / 128 BPM",
    "Night Society",
)


def png_size(path: Path) -> tuple[int, int]:
    payload = path.read_bytes()
    if payload[:8] != b"\x89PNG\r\n\x1a\n":
        raise AssertionError(f"not a PNG: {path.name}")
    return struct.unpack(">II", payload[16:24])


def normalized_words(value: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", re.sub(r"<[^>]+>", " ", value).lower())


def candidate_html(document: str, candidate: str) -> str:
    match = re.search(
        rf'<section class="candidate" id="design-{candidate}-board">(.*?)</section>',
        document,
        flags=re.DOTALL,
    )
    if not match:
        raise AssertionError(f"missing candidate {candidate.upper()}")
    return match.group(1)


def main() -> None:
    document = (ROOT / "blind-bakeoff.html").read_text(encoding="utf-8")
    a_words = normalized_words(candidate_html(document, "a"))
    b_words = normalized_words(candidate_html(document, "b"))

    for phrase in REQUIRED_COPY:
        phrase_words = normalized_words(phrase)
        expected = 3
        for label, words in (("A", a_words), ("B", b_words)):
            count = sum(
                words[index : index + len(phrase_words)] == phrase_words
                for index in range(len(words) - len(phrase_words) + 1)
            )
            if count != expected:
                raise AssertionError(f"{label}: {phrase!r} appears {count}, expected {expected}")

    key = json.loads((ROOT / "blind-key.json").read_text(encoding="utf-8"))
    if set(key["assignment"]) != {"A", "B"}:
        raise AssertionError("blind key must contain A and B")
    if key["assignment"]["A"] == key["assignment"]["B"]:
        raise AssertionError("routes must differ")

    expected_sizes = {
        "blind-bakeoff.png": (2200, 2100),
        "design-a.png": (1920, 712),
        "design-b.png": (1920, 712),
    }
    for filename, expected in expected_sizes.items():
        actual = png_size(ROOT / filename)
        if actual != expected:
            raise AssertionError(f"{filename}: {actual}, expected {expected}")

    print("PASS: copy parity, sealed assignment, and 3 rendered boards verified")


if __name__ == "__main__":
    main()
