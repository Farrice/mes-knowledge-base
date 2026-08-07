"""Render OPPORTUNITIES.md from a silver-platter data_map.json."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from datetime import date
from pathlib import Path


SECTION_ORDER = [
    ("data_engineering", "Data Engineering Work First (The 80%)"),
    ("skill", "Skills To Write"),
    ("subagent", "Subagents To Scaffold"),
    ("rule", "Path-Scoped Rules To Add"),
    ("hook", "Hooks To Wire"),
    ("cli", "CLIs You Can Install Today"),
    ("external", "External Or Compliance Work"),
    ("deferred", "Deferred"),
]


def classify(opportunity: dict) -> str:
    feature = str(opportunity.get("claude_code_feature", "")).lower()
    type_name = str(opportunity.get("type", "")).lower()
    surface = str(opportunity.get("surface", "")).lower()
    title = str(opportunity.get("title", "")).lower()

    if "hook" in feature or "hook" in type_name or "hook" in title:
        return "hook"
    if "rule" in feature or "rule" in type_name or surface.startswith("rules/"):
        return "rule"
    if "subagent" in feature:
        return "subagent"
    if "skill" in feature:
        return "skill"
    if "cli" in feature or "cli" in type_name:
        return "cli"
    if "external" in feature or "bedrock" in title or "compliance" in title:
        return "external"
    if any(token in type_name for token in ["automate", "extraction", "summary", "silver", "data"]):
        return "data_engineering"
    return "deferred"


def render(data_map: dict) -> str:
    business = data_map.get("business", {})
    name = business.get("name", "the operator")
    archetype = business.get("archetype", "unknown")

    grouped: dict[str, list[dict]] = defaultdict(list)
    for opportunity in data_map.get("opportunities", []):
        grouped[classify(opportunity)].append(opportunity)

    lines = [
        f"# Opportunities, {name}",
        "",
        f"Generated {date.today().isoformat()} by /silver-platter for archetype `{archetype}`.",
        "",
        "## Data Engineering Work First (The 80%)",
        "",
        "The hardest part is back-of-house. Before any AI layer goes on top, make the data readable, scoped, summarized, and reviewable.",
        "",
    ]

    emitted_data_section = True
    for key, heading in SECTION_ORDER:
        if key == "data_engineering":
            ops = grouped.get(key, [])
        else:
            if emitted_data_section:
                emitted_data_section = False
            lines.extend(["", f"## {heading}", ""])
            ops = grouped.get(key, [])

        if not ops:
            lines.append("_No high-priority items detected._")
            continue

        for op in ops:
            title = op.get("title") or op.get("feature_name") or "Untitled opportunity"
            explanation = op.get("explanation") or "No explanation provided."
            impact = op.get("estimated_impact")
            suffix = f" _Impact: {impact}._" if impact else ""
            lines.append(f"- **{title}.** {explanation}{suffix}")

    lines.extend(
        [
            "",
            "---",
            "",
            "## What These Words Mean",
            "",
            "- **Skill** = a reusable mini-tool with one clear job.",
            "- **Subagent** = a specialist role the orchestrator can route work to.",
            "- **Hook** = an auto-trigger that runs at a moment like session start, file write, or session stop.",
            "- **Rule** = a guardrail that applies automatically, often inside one folder.",
            "- **MCP** = a pre-built bridge to a service.",
            "- **CLI** = a command-line wrapper for a service or workflow.",
            "- **API** = direct service access, usually more flexible and more code-heavy.",
            "",
            "## Next Step",
            "",
            "Open `data_map.html` for the visual map, then use `builder_handoff.txt` to scaffold the operating system.",
            "",
        ]
    )

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Render OPPORTUNITIES.md from data_map.json")
    parser.add_argument("--input", "-i", required=True)
    parser.add_argument("--output", "-o", required=True)
    args = parser.parse_args()

    data_map = json.loads(Path(args.input).read_text(encoding="utf-8"))
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(render(data_map), encoding="utf-8")
    print(f"[ok] wrote {out_path} ({out_path.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

