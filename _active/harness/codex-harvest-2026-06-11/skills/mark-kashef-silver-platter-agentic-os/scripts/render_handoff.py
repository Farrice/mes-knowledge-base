"""Render a deterministic builder handoff from data_map.json."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

try:
    from jinja2 import Environment
except ImportError as exc:
    Environment = None


SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
DEFAULT_TEMPLATE = SKILL_DIR / "references" / "claude_code_handoff_template.md"


def extract_template(text: str) -> str:
    match = re.search(r"```(?:\n|\r\n)(.*?)(?:\n|\r\n)```", text, re.DOTALL)
    if not match:
        return text
    return match.group(1)


def title_to_slug(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return value.strip("_") or "item"


def derive_folder_structure(data_map: dict) -> list[str]:
    folders = [
        ".claude/skills/",
        ".claude/agents/",
        ".claude/rules/",
        ".claude/commands/",
        "data/raw_dropzone/",
        "data/converted/",
        "silver_platters/",
        "outputs/audit_log.md",
    ]
    for prep in data_map.get("prep", []):
        name = prep.get("name", "")
        if "/" in name:
            folders.append(name.rsplit("/", 1)[0] + "/")
    return sorted(dict.fromkeys(folders))


def opportunities_with_feature(data_map: dict, token: str) -> list[dict]:
    matches = []
    for op in data_map.get("opportunities", []):
        feature = str(op.get("claude_code_feature", "")).lower()
        type_name = str(op.get("type", "")).lower()
        if token in feature or token in type_name:
            matches.append(op)
    return matches


def derive_skills(data_map: dict) -> list[dict]:
    skills = []
    for op in opportunities_with_feature(data_map, "skill"):
        name = op.get("feature_name") or title_to_slug(op.get("title", "skill"))
        skills.append({"name": name, "purpose": op.get("explanation", "Support the silver-platter system.")})
    return skills


def derive_subagents(data_map: dict) -> list[dict]:
    seen = set()
    agents = []
    for plate in data_map.get("plate", []):
        name = plate.get("agent")
        if name and name not in seen:
            seen.add(name)
            agents.append({"name": name, "role": plate.get("explanation", "Read the relevant silver platter and draft the human-facing output.")})
    for op in opportunities_with_feature(data_map, "subagent"):
        name = op.get("feature_name") or op.get("title") or "specialist"
        if name not in seen:
            seen.add(name)
            agents.append({"name": name, "role": op.get("explanation", "Specialist role for the mapped operating system.")})
    return agents


def derive_rules(data_map: dict) -> list[dict]:
    rules = []
    for op in data_map.get("opportunities", []):
        feature = str(op.get("claude_code_feature", "")).lower()
        surface = str(op.get("surface", ""))
        if "rule" in feature or surface.startswith("rules/"):
            name = op.get("feature_name") or surface or title_to_slug(op.get("title", "rule"))
            rules.append({"name": name, "paths": ["data/**", "silver_platters/**"]})
    for prep in data_map.get("prep", []):
        excerpt = str(prep.get("governing_rule_excerpt", ""))
        if "paths:" in excerpt:
            name = title_to_slug(prep.get("domain", prep.get("id", "rule"))) + "_rule.md"
            rules.append({"name": name, "paths": prep.get("sources", []) or ["silver_platters/**"]})
    return rules


def join_values(values: list | None) -> str:
    if not values:
        return "None listed"
    return ", ".join(str(value) for value in values)


def render_list(items: list[str], indent: str = "") -> str:
    if not items:
        return f"{indent}- None identified"
    return "\n".join(f"{indent}- {item}" for item in items)


def render_plain_handoff(data_map: dict, cwd_path: str) -> str:
    business = data_map.get("business", {})
    pantry = data_map.get("pantry", [])
    prep = data_map.get("prep", [])
    plate = data_map.get("plate", [])
    folder_structure = derive_folder_structure(data_map)
    skills_to_write = derive_skills(data_map)
    subagents_to_write = derive_subagents(data_map)
    rules_to_write = derive_rules(data_map)

    pantry_rows = []
    for item in pantry:
        pantry_rows.append(
            f"- {item.get('tool')} - {item.get('format')}, {item.get('cadence')} cadence, {item.get('volume')} volume\n"
            f"  - Status: {item.get('status')}\n"
            f"  - Feeds: {join_values(item.get('feeds'))}"
        )

    prep_rows = []
    for item in prep:
        prep_rows.append(
            f"- {item.get('name')} ({item.get('domain')} domain)\n"
            f"  - Sources: {join_values(item.get('sources'))}\n"
            f"  - Schedule: {item.get('schedule')}\n"
            f"  - Status: {item.get('status')}"
        )

    plate_rows = []
    for item in plate:
        plate_rows.append(
            f"- {item.get('name')} (drafted by {item.get('agent')})\n"
            f"  - Consumers: {join_values(item.get('consumers'))}\n"
            f"  - Approval gate: {item.get('approval_gate')}"
        )

    skill_rows = [f"{item.get('name')} - {item.get('purpose')}" for item in skills_to_write]
    agent_rows = [f"{item.get('name')} - {item.get('role')}" for item in subagents_to_write]
    rule_rows = [f"{item.get('name')} - paths: {join_values(item.get('paths'))}" for item in rules_to_write]

    return f"""@claude-code-guide

I just ran /silver-platter on my repo. Here's what we mapped together. I want you to scaffold the .claude/ folder so the architecture matches.

# Business

- Name: {business.get('name')}
- Archetype: {business.get('archetype')}
- One-line: {business.get('stack_summary')}

# Data map

## Pantry, what data sources I have

{chr(10).join(pantry_rows) if pantry_rows else "- None identified"}

## Prep table, silver platters I need

{chr(10).join(prep_rows) if prep_rows else "- None identified"}

## Plate, outputs that go to humans

{chr(10).join(plate_rows) if plate_rows else "- None identified"}

# What I want you to build

1. Create the folder structure:
{render_list(folder_structure, "   ")}

2. Write a lean root CLAUDE.md, target under 200 lines, that states the business one-liner, names the hierarchy, lists hard rules, and references path-scoped rules.

3. Write {len(skills_to_write)} skills under .claude/skills/:
{render_list(skill_rows, "   ")}

4. Write {len(subagents_to_write)} subagents under .claude/agents/:
{render_list(agent_rows, "   ")}

5. Write {len(rules_to_write)} rules under .claude/rules/:
{render_list(rule_rows, "   ")}

6. Configure .claude/settings.json with three hooks:
   - SessionStart: convert_dropzone.sh
   - PostToolUse Edit|Write: audit_action.sh
   - Stop: check_acknowledgment.sh, warn-on-unsigned-draft, exit 0

# Hard constraints I need you to honor

- Plain English voice. Operators are not engineers. Translate every jargon term inline.
- Every output that goes to a human requires an approval gate.
- All silver platters get committed to git. Raw data exports do not.
- Hooks are non-blocking by default.
- The orchestrator is a hierarchy, not a flat row. Specialists report to the orchestrator.

# What you should not do

- Do not pull in external dependencies beyond standard local tools.
- Do not write tests right now. Get the scaffolding right first.
- Do not push anything to git or modify my main branch.
- Do not auto-run anything. I will review every file you create.

# Working directory

{cwd_path}

When you're done, tell me:
1. What files you created
2. What I should open first to verify
3. Any open questions you could not answer from this brief
"""


def render(data_map: dict, template_path: Path, cwd_path: str) -> str:
    if Environment is None:
        return render_plain_handoff(data_map, cwd_path).strip() + "\n"

    template_text = extract_template(template_path.read_text(encoding="utf-8"))
    env = Environment(trim_blocks=True, lstrip_blocks=True)
    template = env.from_string(template_text)
    context = {
        "business": data_map.get("business", {}),
        "pantry": data_map.get("pantry", []),
        "prep": data_map.get("prep", []),
        "plate": data_map.get("plate", []),
        "folder_structure": derive_folder_structure(data_map),
        "skills_to_write": derive_skills(data_map),
        "subagents_to_write": derive_subagents(data_map),
        "rules_to_write": derive_rules(data_map),
        "cwd_path": cwd_path,
    }
    return template.render(**context).strip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a builder handoff from data_map.json")
    parser.add_argument("--input", "-i", required=True)
    parser.add_argument("--output", "-o", required=True)
    parser.add_argument("--template", default=str(DEFAULT_TEMPLATE))
    parser.add_argument("--cwd-path", default=str(Path.cwd()))
    args = parser.parse_args()

    data_map = json.loads(Path(args.input).read_text(encoding="utf-8"))
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(render(data_map, Path(args.template), args.cwd_path), encoding="utf-8")
    print(f"[ok] wrote {out_path} ({out_path.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
