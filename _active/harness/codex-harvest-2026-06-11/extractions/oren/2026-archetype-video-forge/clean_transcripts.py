#!/usr/bin/env python3
"""Normalize YouTube auto-caption transcript overlap for this extraction package."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2] / "video-context"
OUT = Path(__file__).resolve().parent / "cleaned-transcripts"

VIDEOS = {
    "tcqf6sgw_Ho": "01-archetype-social-strategy.txt",
    "l3inbx2jeZU": "02-pricing-psychology.txt",
    "IdmtqdoZTBA": "03-content-operations.txt",
    "1YVi3iFk3V0": "04-marketing-plan.txt",
    "8gvCc5jvcH0": "05-short-form-monetization.txt",
    "QHPmOgnc96E": "06-creative-systems.txt",
}


def words_for(line: str) -> list[str]:
    text = re.sub(r"^\[[^\]]+\]\s*", "", line).strip()
    return text.split()


def append_with_overlap(output: list[str], words: list[str]) -> None:
    if not words:
        return
    tail = " ".join(output[-len(words) - 8 :])
    phrase = " ".join(words)
    if phrase and phrase in tail:
        return
    max_overlap = min(len(output), len(words))
    for size in range(max_overlap, 0, -1):
        if output[-size:] == words[:size]:
            output.extend(words[size:])
            return
    output.extend(words)


def sentence_wrap(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"(?<=[.!?])\s+", "\n", text)
    return text + "\n"


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    for video_id, filename in VIDEOS.items():
        source = ROOT / video_id / "transcript.txt"
        output_words: list[str] = []
        for line in source.read_text(encoding="utf-8").splitlines():
            append_with_overlap(output_words, words_for(line))
        (OUT / filename).write_text(sentence_wrap(" ".join(output_words)), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
