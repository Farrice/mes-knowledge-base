#!/usr/bin/env python3
"""Run prose classification on each publishable copy unit, not Markdown tables."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "execution"))
from prose_classifier import classify_prose  # noqa: E402


HERE = Path(__file__).resolve().parent


def section(text: str, start: str, end: str | None) -> str:
    body = text.split(start, 1)[1]
    if end and end in body:
        body = body.split(end, 1)[0]
    return body.strip()


def main() -> int:
    linkedin = (HERE / "linkedin-launch-kit.md").read_text()
    outreach = (HERE / "distribution-outreach-kit.md").read_text()
    units: dict[str, str] = {
        "profile_about": section(linkedin, "**About**", "## Pinned post"),
        "pinned_post": section(linkedin, "## Pinned post", "## Ten publication-ready posts"),
    }
    post_block = section(linkedin, "## Ten publication-ready posts", "## Three short demonstration-video scripts")
    parts = re.split(r"^### ", post_block, flags=re.MULTILINE)
    for item in parts:
        if item.strip():
            title, _, body = item.partition("\n")
            units[f"post_{title.strip()}"] = body.strip()

    msg_block = section(outreach, "## Message structures", "## Five-minute Loom teardown")
    parts = re.split(r"^### ", msg_block, flags=re.MULTILINE)
    for item in parts:
        if item.strip():
            title, _, body = item.partition("\n")
            units[f"message_{title.strip()}"] = body.strip()

    results = {name: classify_prose(body) for name, body in units.items()}
    flagged = {name: result for name, result in results.items() if result["verdict"] == "FLAGGED"}
    receipt = {
        "verdict": "PASS" if not flagged else "FAIL",
        "method": "Each outward-facing copy unit classified separately; worksheets and Markdown table scaffolding excluded.",
        "units": len(results),
        "flagged": flagged,
        "results": results,
    }
    (HERE / "copy-quality-receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"verdict": receipt["verdict"], "units": len(results), "flagged": list(flagged)}, indent=2))
    return 0 if not flagged else 1


if __name__ == "__main__":
    raise SystemExit(main())
