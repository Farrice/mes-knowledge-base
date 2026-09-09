#!/usr/bin/env python3
"""Build a deterministic masked comparison packet; does not score or reveal a verdict."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


TESTS = Path(__file__).resolve().parent
BASELINES = TESTS / "baselines/frozen-baselines.md"
CANDIDATES = TESTS / "candidates/greer-candidates.md"
OUTPUT = TESTS / "masked-verdicts"
CASE_IDS = ("FIC-01", "FIC-02", "DOM-01", "DOM-02", "DOM-03", "DOM-04", "DOM-05")


def sections(path: Path) -> dict[str, str]:
    text = path.read_text()
    matches = list(re.finditer(r"^## ((?:FIC|DOM)-\d{2})\s*$", text, re.M))
    return {
        match.group(1): text[match.end():matches[index + 1].start() if index + 1 < len(matches) else len(text)].strip()
        for index, match in enumerate(matches)
    }


def digest(value: str) -> str:
    return hashlib.sha256(value.encode()).hexdigest()


def main() -> int:
    baselines = sections(BASELINES)
    candidates = sections(CANDIDATES)
    lines = [
        "# Greer Masked Comparison Packet", "",
        "Score each case without opening `label-map.json`. Apply the Greer rubric and host vetoes. Labels are deterministic for reproducibility, not a claim of evaluator independence.", "",
    ]
    label_map: dict[str, dict] = {}
    for case_id in CASE_IDS:
        baseline, candidate = baselines[case_id], candidates[case_id]
        candidate_first = int(hashlib.sha256(case_id.encode()).hexdigest(), 16) % 2 == 0
        x, y = (candidate, baseline) if candidate_first else (baseline, candidate)
        label_map[case_id] = {
            "X": "candidate" if candidate_first else "baseline",
            "Y": "baseline" if candidate_first else "candidate",
            "X_sha256": digest(x), "Y_sha256": digest(y),
        }
        lines.extend([
            f"## {case_id}", "", "### Version X", "", x, "", "### Version Y", "", y, "",
            "### Human Score — NO EVENT", "",
            "- Preference: `[preferred X / tie / preferred Y]`",
            "- Greer rubric: `[scores and rationale]`",
            "- Host veto: `[PASS / FAIL + reason]`",
            "- Tell or failure: `[what exposed the weaker version]`", "",
        ])
    packet = "\n".join(lines).rstrip() + "\n"
    (OUTPUT / "masked-packet.md").write_text(packet)
    mapping = {
        "status": "SEALED_FOR_HUMAN_REVIEW_NO_EVENT",
        "packet_sha256": digest(packet),
        "cases": label_map,
        "warning": "Opening this file before scoring breaks evaluator blinding. No verdict exists yet."
    }
    (OUTPUT / "label-map.json").write_text(json.dumps(mapping, indent=2) + "\n")
    print(f"GREER MASKED PACKET BUILT: {len(CASE_IDS)} pairs; human verdict NO EVENT")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
