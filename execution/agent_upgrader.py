#!/usr/bin/env python3
"""
Agent Upgrader — Clean DF/AP/VD template sections from AGENT.md files and
add genius.md cross-references linking each agent to its savant-level calibration.

Usage:
  python execution/agent_upgrader.py --plan-only          # Audit without changes
  python execution/agent_upgrader.py --all                # Upgrade all agents
  python execution/agent_upgrader.py --agent agents/eric-roth  # Single agent
"""

import os
import re
import sys
import glob
import argparse
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
AGENTS_DIR = PROJECT_ROOT / "agents"
SKILLS_DIR = PROJECT_ROOT / "skills"

# Sections to remove (template bloat)
TEMPLATE_SECTIONS = ["## Decision Framework", "## Anti-Patterns", "## Voice DNA"]

# Section to inject
CROSS_REF_HEADER = "## Savant Calibration"


def find_matching_skills(agent_name: str) -> list[dict]:
    """Find all skill directories that match an agent name by prefix."""
    matches = []
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue
        if skill_dir.name.startswith(agent_name):
            genius_path = skill_dir / "genius.md"
            if genius_path.exists():
                # Check which savant sections exist
                content = genius_path.read_text()
                has_exemplars = "## Hall of Fame Exemplars" in content
                has_moves = "## Signature Moves" in content
                has_rubric = "## Expert-Specific Quality Rubric" in content
                matches.append({
                    "skill_dir": skill_dir.name,
                    "genius_path": f"skills/{skill_dir.name}/genius.md",
                    "has_exemplars": has_exemplars,
                    "has_moves": has_moves,
                    "has_rubric": has_rubric,
                })
    return matches


def find_template_sections(content: str) -> list[dict]:
    """Find DF/AP/VD template sections and their line ranges."""
    lines = content.split("\n")
    sections_found = []

    for section_header in TEMPLATE_SECTIONS:
        for i, line in enumerate(lines):
            if line.strip() == section_header:
                # Find the end of this section (next ## header or end of file)
                end = len(lines)

                # Look backward for a `---` separator above this section          
                separator_above = None
                for j in range(i - 1, max(i - 3, -1), -1):
                    if lines[j].strip() == "---":
                        separator_above = j
                        break

                # Find the next section
                for j in range(i + 1, len(lines)):
                    stripped = lines[j].strip()
                    if stripped.startswith("## ") and stripped not in TEMPLATE_SECTIONS:
                        # Check for --- separator before next section
                        if j > 0 and lines[j - 1].strip() == "---":
                            end = j - 1
                        else:
                            end = j
                        break
                    elif stripped == "---" and j > i + 2:
                        # A --- might be the separator between this section and the next
                        # Check if the next non-empty line after --- is a new header
                        for k in range(j + 1, min(j + 3, len(lines))):
                            if lines[k].strip().startswith("## "):
                                if lines[k].strip() not in TEMPLATE_SECTIONS:
                                    end = j
                                    break
                        if end == j:
                            break

                start = separator_above if separator_above is not None else i
                sections_found.append({
                    "header": section_header,
                    "start_line": start,
                    "end_line": end,
                })
                break

    return sections_found


def remove_template_sections(content: str) -> tuple[str, int]:
    """Remove DF/AP/VD template sections. Returns (cleaned content, count removed)."""
    sections = find_template_sections(content)
    if not sections:
        return content, 0

    lines = content.split("\n")
    # Remove in reverse order to preserve line numbers
    sections.sort(key=lambda s: s["start_line"], reverse=True)
    for section in sections:
        start = section["start_line"]
        end = section["end_line"]
        del lines[start:end]

    # Clean up double blank lines
    cleaned = "\n".join(lines)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)

    return cleaned, len(sections)


def build_cross_reference(skills: list[dict]) -> str:
    """Build the Savant Calibration cross-reference section."""
    if not skills:
        return ""

    lines = [
        "",
        "---",
        "",
        f"{CROSS_REF_HEADER}",
        "",
        "This agent's expert calibration — Hall of Fame Exemplars, Signature Moves, and Quality Rubric — lives in the genius.md files loaded at deployment:",
        "",
    ]

    for skill in skills:
        sections = []
        if skill["has_exemplars"]:
            sections.append("Exemplars")
        if skill["has_moves"]:
            sections.append("Moves")
        if skill["has_rubric"]:
            sections.append("Rubric")

        status = " + ".join(sections) if sections else "⚠️ pending enrichment"
        lines.append(f"- [`{skill['skill_dir']}`]({skill['genius_path']}) — {status}")

    lines.append("")
    lines.append("> These sections set the quality ceiling for all output. The Context Engine loads them at Tier 1+ automatically.")
    lines.append("")

    return "\n".join(lines)


def has_cross_reference(content: str) -> bool:
    """Check if the agent already has a Savant Calibration section."""
    return CROSS_REF_HEADER in content


def find_insertion_point(content: str) -> int:
    """Find the best place to insert the cross-reference section.

    Strategy: Insert before the last metadata block (Memory Reference, Invocation,
    or Last updated). If none found, append at end.
    """
    lines = content.split("\n")

    # Look for trailing sections to insert before
    trailing_patterns = [
        "## Memory Reference",
        "## Invocation",
        "*Last updated:",
    ]

    earliest_trailing = len(lines)
    for pattern in trailing_patterns:
        for i, line in enumerate(lines):
            if line.strip().startswith(pattern):
                # Include the --- separator above if present
                check_from = max(0, i - 2)
                for j in range(i - 1, check_from - 1, -1):
                    if lines[j].strip() == "---":
                        earliest_trailing = min(earliest_trailing, j)
                        break
                else:
                    earliest_trailing = min(earliest_trailing, i)
                break

    return earliest_trailing


def upgrade_agent(agent_dir: Path, dry_run: bool = False) -> dict:
    """Upgrade a single agent's AGENT.md file."""
    agent_md = agent_dir / "AGENT.md"
    if not agent_md.exists():
        return {"name": agent_dir.name, "status": "no AGENT.md", "changes": []}

    agent_name = agent_dir.name
    content = agent_md.read_text()
    changes = []

    # 1. Remove template sections
    cleaned, removed_count = remove_template_sections(content)
    if removed_count > 0:
        changes.append(f"removed {removed_count} template section(s)")
        content = cleaned

    # 2. Find matching skills
    skills = find_matching_skills(agent_name)

    # 3. Add cross-reference if not already present and skills exist
    if skills and not has_cross_reference(content):
        cross_ref = build_cross_reference(skills)
        insertion_point = find_insertion_point(content)
        lines = content.split("\n")
        lines.insert(insertion_point, cross_ref)
        content = "\n".join(lines)
        # Clean up excessive blank lines
        content = re.sub(r"\n{3,}", "\n\n", content)
        changes.append(f"added cross-ref to {len(skills)} skill(s)")
    elif has_cross_reference(content):
        changes.append("cross-ref already exists")

    if not changes:
        return {"name": agent_name, "status": "already clean", "changes": []}

    if not dry_run:
        agent_md.write_text(content)

    return {"name": agent_name, "status": "upgraded", "changes": changes}


def discover_agents() -> list[Path]:
    """Find all agent directories (excluding _framework)."""
    agents = []
    for d in sorted(AGENTS_DIR.iterdir()):
        if d.is_dir() and d.name != "_framework" and (d / "AGENT.md").exists():
            agents.append(d)
    return agents


def main():
    parser = argparse.ArgumentParser(description="Agent Upgrader — clean + cross-reference")
    parser.add_argument("--all", action="store_true", help="Upgrade all agents")
    parser.add_argument("--agent", type=str, help="Path to a single agent directory")
    parser.add_argument("--plan-only", action="store_true", help="Audit without making changes")
    args = parser.parse_args()

    if not args.all and not args.agent:
        parser.print_help()
        sys.exit(1)

    if args.agent:
        agent_path = Path(args.agent)
        if not agent_path.is_absolute():
            agent_path = PROJECT_ROOT / agent_path
        agents = [agent_path]
    else:
        agents = discover_agents()

    print(f"\n📂 Discovered {len(agents)} agent(s)")

    # Audit phase
    need_template_cleanup = 0
    need_cross_ref = 0
    already_clean = 0
    no_skills = 0

    audit_results = []
    for agent_dir in agents:
        name = agent_dir.name
        agent_md = agent_dir / "AGENT.md"
        if not agent_md.exists():
            continue

        content = agent_md.read_text()
        sections = find_template_sections(content)
        skills = find_matching_skills(name)
        has_ref = has_cross_reference(content)

        needs_work = bool(sections) or (bool(skills) and not has_ref)
        if needs_work:
            bits = []
            if sections:
                need_template_cleanup += 1
                headers = [s["header"].replace("## ", "") for s in sections]
                bits.append(f"clean {'/'.join(headers)}")
            if skills and not has_ref:
                need_cross_ref += 1
                bits.append(f"link {len(skills)} skill(s)")
            elif not skills:
                no_skills += 1
            audit_results.append((name, bits, len(skills)))
        else:
            already_clean += 1

    print(f"\n📋 Assessment:")
    print(f"   Need template cleanup: {need_template_cleanup}")
    print(f"   Need cross-reference: {need_cross_ref}")
    print(f"   No matching skills: {no_skills}")
    print(f"   Already clean: {already_clean}")

    if audit_results:
        print(f"\n📋 Targets:")
        for name, bits, skill_count in audit_results:
            skill_info = f"({skill_count} skills)" if skill_count > 0 else "(no skills)"
            print(f"   → {name}: {', '.join(bits)} {skill_info}")

    if args.plan_only:
        print(f"\n🔍 Plan-only mode — no changes made.")
        return

    # Execute upgrades
    print(f"\n{'='*60}")
    print(f"  AGENT UPGRADER — {len(agents)} targets")
    print(f"{'='*60}\n")

    upgraded = 0
    skipped = 0
    for agent_dir in agents:
        result = upgrade_agent(agent_dir, dry_run=False)
        if result["changes"]:
            print(f"  ✅ {result['name']}: {', '.join(result['changes'])}")
            upgraded += 1
        else:
            skipped += 1

    print(f"\n{'='*60}")
    print(f"  AGENT UPGRADER COMPLETE")
    print(f"{'='*60}")
    print(f"  ✅ Upgraded: {upgraded}")
    print(f"  ✓  Already clean: {skipped}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
