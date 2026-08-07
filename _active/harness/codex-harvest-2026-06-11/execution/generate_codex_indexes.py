#!/usr/bin/env python3
"""Generate compact Codex-facing indexes for the Antigravity library sweep."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
WORKFLOW_DIR = ROOT / ".agent" / "workflows"
COMMAND_DIR = ROOT / ".claude" / "commands"
HOT_SKILL_DIR = ROOT / ".agents" / "skills"
COLD_SKILL_DIR = ROOT / ".agents" / "cold-skills" / "source-command-wrappers"
AGENTS_DIR = ROOT / "agents"
CLAUDE_AGENTS_DIR = ROOT / ".claude" / "agents"
OUT_DIR = ROOT / "semantic_libraries" / "antigravity" / "indexes"

COMMAND_GRADE_HINTS = (
    "usage",
    "output",
    "run",
    "workflow",
    "deliverable",
    "verification",
    "quality gate",
)
INTERNAL_HINTS = (
    "internal",
    "source-only",
    "source only",
    "helper",
    "do not invoke",
)
EXPERIMENTAL_HINTS = (
    "experiment",
    "experimental",
    "prototype",
    "draft",
    "sandbox",
    "wip",
)
ARCHIVE_HINTS = (
    "deprecated",
    "archived",
    "archive",
    "stale",
    "legacy only",
)

SUBAGENT_CANDIDATES = {
    "adversarial-reviewer",
    "competitive-intel",
    "content-finalizer",
    "deep-research",
    "fact-verifier",
    "icp-deep-canvasser",
    "prose-doctor",
}


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_md(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def clean_inline(value: str) -> str:
    value = value.strip().strip("\"'")
    return re.sub(r"\s+", " ", value)


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    data: dict[str, str] = {}
    for line in parts[1].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = clean_inline(value)
    return data


def heading(text: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    return clean_inline(match.group(1)) if match else fallback.replace("-", " ").title()


def description(text: str, fallback: str) -> str:
    fm = frontmatter(text)
    if fm.get("description"):
        return fm["description"]
    title = heading(text, fallback)
    if " — " in title:
        return title.split(" — ", 1)[1].strip()
    return title


def bridge_status(name: str) -> str:
    has_workflow = (WORKFLOW_DIR / f"{name}.md").exists()
    has_command = (COMMAND_DIR / f"{name}.md").exists()
    has_hot = (HOT_SKILL_DIR / f"source-command-{name}" / "SKILL.md").exists()
    has_cold = (COLD_SKILL_DIR / f"source-command-{name}" / "SKILL.md").exists()
    if has_workflow and has_hot:
        return "hot bridge"
    if has_workflow and has_cold:
        return "cold bridge"
    if has_workflow and has_command:
        return "source-command only"
    if has_workflow:
        return "workflow-only"
    if has_command or has_hot or has_cold:
        return "broken/stale bridge"
    return "missing"


def workflow_classification(name: str, text: str, status: str) -> str:
    haystack = f"{name}\n{text}".lower()
    if status == "broken/stale bridge" or any(hint in haystack for hint in ARCHIVE_HINTS):
        return "archive"
    if any(hint in haystack for hint in INTERNAL_HINTS):
        return "internal"
    if any(hint in haystack for hint in EXPERIMENTAL_HINTS):
        return "experimental"
    if re.search(r"^#\s+/", text, re.MULTILINE) or any(hint in haystack for hint in COMMAND_GRADE_HINTS):
        return "command-grade"
    return "internal"


def workflows() -> list[dict[str, Any]]:
    rows = []
    for path in sorted(WORKFLOW_DIR.glob("*.md")):
        name = path.stem
        text = read_text(path)
        status = bridge_status(name)
        rows.append(
            {
                "name": name,
                "path": rel(path),
                "title": heading(text, f"/{name}"),
                "description": description(text, name),
                "bridge_status": status,
                "classification": workflow_classification(name, text, status),
                "has_workflow": True,
                "has_source_command": (COMMAND_DIR / f"{name}.md").exists(),
                "has_hot_codex_skill": (HOT_SKILL_DIR / f"source-command-{name}" / "SKILL.md").exists(),
                "has_cold_codex_skill": (COLD_SKILL_DIR / f"source-command-{name}" / "SKILL.md").exists(),
            }
        )
    return rows


def stale_bridges(workflow_names: set[str]) -> list[dict[str, str]]:
    rows = []
    command_names = {path.stem for path in COMMAND_DIR.glob("*.md")}
    hot_names = {path.parent.name.removeprefix("source-command-") for path in HOT_SKILL_DIR.glob("source-command-*/SKILL.md")}
    cold_names = {path.parent.name.removeprefix("source-command-") for path in COLD_SKILL_DIR.glob("source-command-*/SKILL.md")}
    for name in sorted((command_names | hot_names | cold_names) - workflow_names):
        rows.append(
            {
                "name": name,
                "bridge_status": "broken/stale bridge",
                "classification": "archive",
                "source_command": rel(COMMAND_DIR / f"{name}.md") if name in command_names else "",
                "hot_codex_skill": rel(HOT_SKILL_DIR / f"source-command-{name}" / "SKILL.md") if name in hot_names else "",
                "cold_codex_skill": rel(COLD_SKILL_DIR / f"source-command-{name}" / "SKILL.md") if name in cold_names else "",
            }
        )
    return rows


def family_for(name: str) -> str:
    parts = name.split("-")
    if len(parts) >= 2 and parts[0] in {"ai", "anti", "blue", "client", "codex", "content", "creative", "deep", "expert", "ground", "high", "knowledge", "mission", "parallel", "publishable", "revenue", "routing", "skill", "source", "system", "video", "zero"}:
        return "-".join(parts[:2])
    return parts[0]


def build_workflow_family_index(workflow_rows: list[dict[str, Any]]) -> dict[str, Any]:
    families: dict[str, dict[str, Any]] = {}
    for row in workflow_rows:
        family = family_for(row["name"])
        item = families.setdefault(
            family,
            {
                "family": family,
                "count": 0,
                "bridge_status_counts": Counter(),
                "classification_counts": Counter(),
                "sample_routes": [],
            },
        )
        item["count"] += 1
        item["bridge_status_counts"][row["bridge_status"]] += 1
        item["classification_counts"][row["classification"]] += 1
        if len(item["sample_routes"]) < 8:
            item["sample_routes"].append(row["name"])

    normalized = []
    for item in families.values():
        normalized.append(
            {
                "family": item["family"],
                "count": item["count"],
                "bridge_status_counts": dict(item["bridge_status_counts"]),
                "classification_counts": dict(item["classification_counts"]),
                "sample_routes": item["sample_routes"],
            }
        )
    normalized.sort(key=lambda item: (-item["count"], item["family"]))
    return {
        "schema_version": "1.0",
        "index_kind": "workflow_family_index",
        "generated_at": now(),
        "generated_by": "execution/generate_codex_indexes.py",
        "source": rel(WORKFLOW_DIR),
        "sources": [".agent/workflows/*.md", ".claude/commands/*.md", ".agents/skills/source-command-*/SKILL.md", ".agents/cold-skills/source-command-wrappers/source-command-*/SKILL.md"],
        "families": normalized,
    }


def parse_agent_skills(text: str) -> list[str]:
    match = re.search(r"^skills:\s*\n((?:\s+-\s+.+\n?)+)", text, re.MULTILINE)
    if not match:
        return []
    return [clean_inline(line.split("-", 1)[1]) for line in match.group(1).splitlines() if "-" in line]


def build_agent_route_cards() -> dict[str, Any]:
    cards = []
    for path in sorted(AGENTS_DIR.glob("*/AGENT.md")):
        text = read_text(path)
        fm = frontmatter(text)
        slug = path.parent.name
        cards.append(
            {
                "slug": slug,
                "path": rel(path),
                "name": fm.get("name") or heading(text, slug),
                "expert": fm.get("expert", ""),
                "domain": fm.get("domain", ""),
                "skills": parse_agent_skills(text),
                "routing_policy": "cold expertise card; load full agent only when routed",
            }
        )
    return {
        "schema_version": "1.0",
        "index_kind": "agent_route_cards",
        "generated_at": now(),
        "generated_by": "execution/generate_codex_indexes.py",
        "source": rel(AGENTS_DIR),
        "sources": ["agents/*/AGENT.md"],
        "count": len(cards),
        "cards": cards,
    }


def build_subagent_candidates() -> dict[str, Any]:
    rows = []
    for path in sorted(CLAUDE_AGENTS_DIR.glob("*.md")):
        text = read_text(path)
        fm = frontmatter(text)
        slug = path.stem
        candidate = slug in SUBAGENT_CANDIDATES
        rows.append(
            {
                "slug": slug,
                "path": rel(path),
                "name": fm.get("name", slug),
                "description": fm.get("description", ""),
                "codex_verdict": "subagent candidate" if candidate else "keep as workflow/protocol",
                "activation_boundary": "requires explicit user authorization for real Codex subagents",
            }
        )
    return {
        "schema_version": "1.0",
        "index_kind": "codex_subagent_candidates",
        "generated_at": now(),
        "generated_by": "execution/generate_codex_indexes.py",
        "source": rel(CLAUDE_AGENTS_DIR),
        "sources": [".claude/agents/*.md"],
        "candidate_count": sum(1 for row in rows if row["codex_verdict"] == "subagent candidate"),
        "count": len(rows),
        "items": rows,
    }


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def build_inventory() -> dict[str, Any]:
    workflow_rows = workflows()
    workflow_names = {row["name"] for row in workflow_rows}
    stale = stale_bridges(workflow_names)
    bridge_counts = Counter(row["bridge_status"] for row in workflow_rows)
    class_counts = Counter(row["classification"] for row in workflow_rows)
    return {
        "schema_version": "1.0",
        "index_kind": "full_library_inventory",
        "generated_at": now(),
        "generated_by": "execution/generate_codex_indexes.py",
        "sources": [".agent/workflows/*.md", ".claude/commands/*.md", ".agents/skills/source-command-*/SKILL.md", ".agents/cold-skills/source-command-wrappers/source-command-*/SKILL.md"],
        "policy": "Keep hot surface small; preserve cold arsenal; classify before promotion or archive.",
        "counts": {
            "workflows": len(workflow_rows),
            "legacy_source_commands": len(list(COMMAND_DIR.glob("*.md"))),
            "hot_source_command_wrappers": len(list(HOT_SKILL_DIR.glob("source-command-*/SKILL.md"))),
            "cold_source_command_wrappers": len(list(COLD_SKILL_DIR.glob("source-command-*/SKILL.md"))),
            "agent_profiles": len(list(AGENTS_DIR.glob("*/AGENT.md"))),
            "claude_subagent_specs": len(list(CLAUDE_AGENTS_DIR.glob("*.md"))),
        },
        "bridge_status_counts": dict(bridge_counts),
        "classification_counts": dict(class_counts),
        "workflow_only": [row for row in workflow_rows if row["bridge_status"] == "workflow-only"],
        "broken_or_stale_bridges": stale,
        "workflows": workflow_rows,
    }


def write_inventory_markdown(inventory: dict[str, Any]) -> None:
    lines = [
        "# Codex Full Library Sweep Inventory",
        "",
        f"Generated: {inventory['generated_at']}",
        "",
        "## Counts",
        "",
        "| Surface | Count |",
        "|---|---:|",
    ]
    for key, value in inventory["counts"].items():
        lines.append(f"| {key.replace('_', ' ')} | {value} |")
    lines.extend(["", "## Bridge Status", "", "| Status | Count |", "|---|---:|"])
    for key, value in sorted(inventory["bridge_status_counts"].items()):
        lines.append(f"| {key} | {value} |")
    lines.extend(["", "## Workflow-Only Classification", "", "| Class | Count |", "|---|---:|"])
    class_counts = Counter(row["classification"] for row in inventory["workflow_only"])
    for key, value in sorted(class_counts.items()):
        lines.append(f"| {key} | {value} |")
    lines.extend(["", "## Broken Or Stale Bridges", ""])
    if inventory["broken_or_stale_bridges"]:
        for item in inventory["broken_or_stale_bridges"]:
            lines.append(f"- `{item['name']}` -> archive ({item.get('source_command') or item.get('cold_codex_skill') or item.get('hot_codex_skill')})")
    else:
        lines.append("None.")
    lines.extend(["", "## Workflow-Only Sample", ""])
    for row in inventory["workflow_only"][:40]:
        lines.append(f"- `/{row['name']}` -> {row['classification']}")
    write_md(OUT_DIR / "full-library-inventory.md", lines)


def write_family_markdown(index: dict[str, Any]) -> None:
    lines = [
        "# Workflow Family Index",
        "",
        f"Generated: {index['generated_at']}",
        "",
        "| Family | Count | Bridge Status | Classification | Sample Routes |",
        "|---|---:|---|---|---|",
    ]
    for item in index["families"]:
        bridge = ", ".join(f"{key}: {value}" for key, value in item["bridge_status_counts"].items())
        classes = ", ".join(f"{key}: {value}" for key, value in item["classification_counts"].items())
        samples = ", ".join(f"`/{route}`" for route in item["sample_routes"])
        lines.append(f"| `{item['family']}` | {item['count']} | {bridge} | {classes} | {samples} |")
    write_md(OUT_DIR / "workflow-family-index.md", lines)


def write_agent_markdown(index: dict[str, Any]) -> None:
    lines = [
        "# Agent Route Cards",
        "",
        f"Generated: {index['generated_at']}",
        "",
        "| Agent | Domain | Skills | Policy |",
        "|---|---|---|---|",
    ]
    for card in index["cards"]:
        skills = ", ".join(f"`{skill}`" for skill in card["skills"][:5]) or "None listed"
        lines.append(f"| `{card['slug']}` | {card['domain']} | {skills} | {card['routing_policy']} |")
    write_md(OUT_DIR / "agent-route-cards.md", lines)


def write_subagent_markdown(index: dict[str, Any]) -> None:
    lines = [
        "# Codex Subagent Candidates",
        "",
        f"Generated: {index['generated_at']}",
        "",
        "| Spec | Verdict | Boundary |",
        "|---|---|---|",
    ]
    for item in index["items"]:
        lines.append(f"| `{item['slug']}` | {item['codex_verdict']} | {item['activation_boundary']} |")
    write_md(OUT_DIR / "codex-subagent-candidates.md", lines)


def generate() -> dict[str, Any]:
    inventory = build_inventory()
    family = build_workflow_family_index(inventory["workflows"])
    agents = build_agent_route_cards()
    subagents = build_subagent_candidates()
    write_json(OUT_DIR / "full-library-inventory.json", inventory)
    write_json(OUT_DIR / "workflow-family-index.json", family)
    write_json(OUT_DIR / "agent-route-cards.json", agents)
    write_json(OUT_DIR / "codex-subagent-candidates.json", subagents)
    write_inventory_markdown(inventory)
    write_family_markdown(family)
    write_agent_markdown(agents)
    write_subagent_markdown(subagents)
    return {
        "inventory": inventory,
        "family": family,
        "agents": agents,
        "subagents": subagents,
    }


def verify() -> tuple[bool, list[str]]:
    required = [
        OUT_DIR / "full-library-inventory.json",
        OUT_DIR / "workflow-family-index.json",
        OUT_DIR / "agent-route-cards.json",
        OUT_DIR / "codex-subagent-candidates.json",
        OUT_DIR / "full-library-inventory.md",
        OUT_DIR / "workflow-family-index.md",
        OUT_DIR / "agent-route-cards.md",
        OUT_DIR / "codex-subagent-candidates.md",
    ]
    failures = [f"missing output: {rel(path)}" for path in required if not path.exists()]
    if failures:
        return False, failures
    try:
        inventory = json.loads(read_text(OUT_DIR / "full-library-inventory.json"))
        agents = json.loads(read_text(OUT_DIR / "agent-route-cards.json"))
        subagents = json.loads(read_text(OUT_DIR / "codex-subagent-candidates.json"))
    except json.JSONDecodeError as exc:
        return False, [f"invalid JSON: {exc}"]
    expected_workflows = len(list(WORKFLOW_DIR.glob("*.md")))
    if inventory.get("counts", {}).get("workflows") != expected_workflows:
        failures.append("workflow count mismatch")
    expected_agents = len(list(AGENTS_DIR.glob("*/AGENT.md")))
    if agents.get("count") != expected_agents:
        failures.append("agent card count mismatch")
    expected_subagents = len(list(CLAUDE_AGENTS_DIR.glob("*.md")))
    if subagents.get("count") != expected_subagents:
        failures.append("subagent candidate count mismatch")
    return not failures, failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate compact Codex Antigravity semantic indexes.")
    parser.add_argument("--verify", action="store_true", help="Verify generated indexes instead of regenerating them.")
    args = parser.parse_args()
    if args.verify:
        ok, failures = verify()
        if not ok:
            print("Codex semantic index verification: FAIL")
            for failure in failures:
                print(f"- {failure}")
            return 1
        print("Codex semantic index verification: PASS")
        return 0
    data = generate()
    print("# Codex Semantic Indexes")
    print(f"- workflows: {data['inventory']['counts']['workflows']}")
    print(f"- workflow-only: {data['inventory']['bridge_status_counts'].get('workflow-only', 0)}")
    print(f"- broken/stale bridges: {len(data['inventory']['broken_or_stale_bridges'])}")
    print(f"- agent route cards: {data['agents']['count']}")
    print(f"- subagent specs: {data['subagents']['count']} ({data['subagents']['candidate_count']} candidates)")
    print(f"Indexes written to: {rel(OUT_DIR)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
