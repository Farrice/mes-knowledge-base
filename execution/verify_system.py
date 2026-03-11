#!/usr/bin/env python3
"""
Universal System Verification Suite — Antigravity Structural Integrity Audit

Cross-references ALL registries against the filesystem and reports every discrepancy.
Unlike system_health.py (operational status) or system-audit.md (bash one-liners),
this script performs a comprehensive 6-phase structural audit.

Usage:
    python execution/verify_system.py              # Full report
    python execution/verify_system.py --json        # Machine-readable JSON
    python execution/verify_system.py --errors-only # Only show errors

Exit codes: 0 = clean, 1 = errors found, 2 = warnings only
"""

import os
import re
import sys
import json
import argparse
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).parent.parent
SKILLS_DIR = ROOT / "skills"
AGENTS_DIR = ROOT / "agents"
WORKFLOWS_DIR = ROOT / ".agent" / "workflows"
SKILL_INDEX = ROOT / "SKILL_INDEX.md"
AGENT_INDEX = ROOT / "AGENT_INDEX.md"
SLASH_COMMANDS = ROOT / "SLASH_COMMANDS.md"
COUNCIL_FILE = ROOT / "COUNCIL.md"
DOMAIN_REGISTRY = ROOT / "DOMAIN_REGISTRY.md"


# ---------------------------------------------------------------------------
# Severity levels
# ---------------------------------------------------------------------------
ERROR = "ERROR"
WARNING = "WARNING"
INFO = "INFO"


class Finding:
    """A single verification finding."""
    def __init__(self, severity, phase, message, detail=None):
        self.severity = severity
        self.phase = phase
        self.message = message
        self.detail = detail

    def __repr__(self):
        prefix = {"ERROR": "❌", "WARNING": "⚠️", "INFO": "ℹ️"}.get(self.severity, "?")
        return f"{prefix} [{self.severity}] {self.message}"

    def to_dict(self):
        d = {"severity": self.severity, "phase": self.phase, "message": self.message}
        if self.detail:
            d["detail"] = self.detail
        return d


findings: list[Finding] = []


def add(severity, phase, message, detail=None):
    findings.append(Finding(severity, phase, message, detail))


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def parse_index_slugs(index_path):
    """Extract slugs from a markdown table index file."""
    slugs = set()
    if not index_path.exists():
        return slugs
    content = index_path.read_text(encoding="utf-8")
    # Match rows like: | `some-slug` | ...
    for m in re.finditer(r'^\|\s*`([^`]+)`', content, re.MULTILINE):
        slugs.add(m.group(1))
    return slugs


def parse_slash_commands(path):
    """Extract slash command names from SLASH_COMMANDS.md."""
    commands = set()
    if not path.exists():
        return commands
    content = path.read_text(encoding="utf-8")
    # Only match `/command` entries inside markdown table rows (lines starting with |)
    for line in content.splitlines():
        if not line.strip().startswith("|"):
            continue
        for m in re.finditer(r'`/([a-z0-9][a-z0-9-]*)`', line):
            commands.add(m.group(1))
    return commands


def get_filesystem_dirs(parent_dir, skip_prefixes=("_", ".")):
    """List subdirectories in a parent, skipping prefixed ones."""
    dirs = set()
    if not parent_dir.exists():
        return dirs
    for item in parent_dir.iterdir():
        if item.is_dir() and not any(item.name.startswith(p) for p in skip_prefixes):
            dirs.add(item.name)
    return dirs


def get_workflow_files():
    """List workflow .md files (without extension)."""
    names = set()
    if not WORKFLOWS_DIR.exists():
        return names
    for item in WORKFLOWS_DIR.iterdir():
        if item.is_file() and item.suffix == ".md":
            names.add(item.stem)
    return names


def extract_expert_refs_from_council(path):
    """Extract expert names/slugs referenced in COUNCIL.md."""
    refs = set()
    if not path.exists():
        return refs
    content = path.read_text(encoding="utf-8")
    # Look for patterns like `@expert-name` or `expert-name` in table rows
    for m in re.finditer(r'`@?([a-z][a-z0-9-]+)`', content):
        slug = m.group(1)
        # Filter out non-expert slugs (common words, commands, council config names)
        if len(slug) > 3 and slug not in {"the", "and", "for", "with", "from", "this", "that"}:
            # Skip council configuration names (e.g., ai-council, brand-council)
            if slug.endswith("-council"):
                continue
            refs.add(slug)
    return refs


def extract_expert_refs_from_domain_registry(path):
    """Extract expert slug references from DOMAIN_REGISTRY.md."""
    refs = set()
    if not path.exists():
        return refs
    content = path.read_text(encoding="utf-8")
    # Match backtick-quoted slugs that look like expert references
    for m in re.finditer(r'`([a-z][a-z0-9-]+(?:-[a-z0-9]+)+)`', content):
        slug = m.group(1)
        if len(slug) > 5:
            refs.add(slug)
    return refs


# ---------------------------------------------------------------------------
# Phase 1: Skill Integrity
# ---------------------------------------------------------------------------
def phase_skill_integrity():
    """Check every skill directory for required files."""
    phase = "skill-integrity"
    fs_skills = get_filesystem_dirs(SKILLS_DIR)
    count = 0

    for slug in sorted(fs_skills):
        skill_path = SKILLS_DIR / slug
        skill_md = skill_path / "SKILL.md"
        workflows_dir = skill_path / "workflows"
        prompts_dir = skill_path / "references" / "prompts"
        genius_md = skill_path / "genius.md"

        if not skill_md.exists():
            add(WARNING, phase, f"Skill `{slug}` missing SKILL.md", str(skill_path))
            count += 1

        # Check if skill has any content
        has_workflows = workflows_dir.exists() and any(workflows_dir.iterdir())
        has_prompts = prompts_dir.exists() and any(prompts_dir.iterdir())
        has_genius = genius_md.exists()

        if not has_workflows and not has_prompts and not has_genius and not skill_md.exists():
            add(WARNING, phase, f"Skill `{slug}` is empty (no SKILL.md, workflows, prompts, or genius.md)", str(skill_path))

    return count


# ---------------------------------------------------------------------------
# Phase 2: Agent Integrity
# ---------------------------------------------------------------------------
def phase_agent_integrity():
    """Check every agent directory for required files."""
    phase = "agent-integrity"
    fs_agents = get_filesystem_dirs(AGENTS_DIR)
    count = 0

    for slug in sorted(fs_agents):
        agent_path = AGENTS_DIR / slug
        agent_md = agent_path / "AGENT.md"
        memory_dir = agent_path / "memory"

        if not agent_md.exists():
            add(WARNING, phase, f"Agent `{slug}` missing AGENT.md", str(agent_path))
            count += 1

        if not memory_dir.exists():
            add(INFO, phase, f"Agent `{slug}` missing memory/ directory", str(agent_path))

    return count


# ---------------------------------------------------------------------------
# Phase 3: Index ↔ Filesystem Sync
# ---------------------------------------------------------------------------
def phase_index_sync():
    """Bidirectional sync check between indexes and filesystem."""
    phase = "index-sync"
    count = 0

    # --- Skills ---
    index_skills = parse_index_slugs(SKILL_INDEX)
    fs_skills = get_filesystem_dirs(SKILLS_DIR)

    # In index but not on filesystem
    for slug in sorted(index_skills - fs_skills):
        add(ERROR, phase, f"SKILL_INDEX lists `{slug}` but no directory exists at skills/{slug}")
        count += 1

    # On filesystem but not in index (only count those with SKILL.md)
    for slug in sorted(fs_skills - index_skills):
        skill_md = SKILLS_DIR / slug / "SKILL.md"
        if skill_md.exists():
            add(ERROR, phase, f"Skill `{slug}` has SKILL.md but is NOT in SKILL_INDEX.md (run sync_registries.py)")
            count += 1
        else:
            add(WARNING, phase, f"Directory skills/{slug} exists but has no SKILL.md and is not indexed")

    # --- Agents ---
    index_agents = parse_index_slugs(AGENT_INDEX)
    fs_agents = get_filesystem_dirs(AGENTS_DIR)

    for slug in sorted(index_agents - fs_agents):
        add(ERROR, phase, f"AGENT_INDEX lists `{slug}` but no directory exists at agents/{slug}")
        count += 1

    for slug in sorted(fs_agents - index_agents):
        agent_md = AGENTS_DIR / slug / "AGENT.md"
        if agent_md.exists():
            add(ERROR, phase, f"Agent `{slug}` has AGENT.md but is NOT in AGENT_INDEX.md (run sync_registries.py)")
            count += 1
        else:
            add(WARNING, phase, f"Directory agents/{slug} exists but has no AGENT.md and is not indexed")

    return count


# ---------------------------------------------------------------------------
# Phase 4: Slash Command → Workflow Mapping
# ---------------------------------------------------------------------------
def phase_slash_workflow_mapping():
    """Check that every slash command has a matching workflow file and vice versa."""
    phase = "slash-workflow"
    count = 0

    commands = parse_slash_commands(SLASH_COMMANDS)
    workflow_files = get_workflow_files()

    # Commands without workflow files
    for cmd in sorted(commands - workflow_files):
        add(ERROR, phase, f"Slash command `/{cmd}` listed in SLASH_COMMANDS.md but no workflow file at .agent/workflows/{cmd}.md")
        count += 1

    # Workflow files not listed in SLASH_COMMANDS.md
    for wf in sorted(workflow_files - commands):
        # Skip special files
        if wf in {"references", "writers-room", "content-sprint"}:
            continue
        add(WARNING, phase, f"Workflow file `.agent/workflows/{wf}.md` exists but `/{wf}` is not in SLASH_COMMANDS.md")

    return count


# ---------------------------------------------------------------------------
# Phase 5: COUNCIL & DOMAIN_REGISTRY Cross-Check
# ---------------------------------------------------------------------------
def phase_council_domain_check():
    """Verify expert references in COUNCIL.md and DOMAIN_REGISTRY.md resolve to real assets."""
    phase = "council-domain"
    count = 0

    fs_skills = get_filesystem_dirs(SKILLS_DIR)
    fs_agents = get_filesystem_dirs(AGENTS_DIR)
    all_assets = fs_skills | fs_agents

    # COUNCIL.md
    council_refs = extract_expert_refs_from_council(COUNCIL_FILE)
    for ref in sorted(council_refs):
        # Check if the ref matches any skill or agent slug (or is a prefix)
        if ref not in all_assets and not any(a.startswith(ref) for a in all_assets):
            add(WARNING, phase, f"COUNCIL.md references `{ref}` but no matching skill or agent directory found")

    # DOMAIN_REGISTRY.md
    registry_refs = extract_expert_refs_from_domain_registry(DOMAIN_REGISTRY)
    for ref in sorted(registry_refs):
        if ref not in all_assets and not any(a.startswith(ref) for a in all_assets):
            add(INFO, phase, f"DOMAIN_REGISTRY.md references `{ref}` — no exact matching skill/agent directory")

    return count


# ---------------------------------------------------------------------------
# Phase 6: Duplicate Detection
# ---------------------------------------------------------------------------
def phase_duplicate_detection():
    """Detect duplicate or suspiciously similar directory names."""
    phase = "duplicates"
    count = 0

    fs_skills = sorted(get_filesystem_dirs(SKILLS_DIR))
    fs_agents = sorted(get_filesystem_dirs(AGENTS_DIR))

    # Check for exact duplicates (shouldn't happen in fs, but check index)
    index_skills = []
    if SKILL_INDEX.exists():
        content = SKILL_INDEX.read_text(encoding="utf-8")
        for m in re.finditer(r'^\|\s*`([^`]+)`', content, re.MULTILINE):
            index_skills.append(m.group(1))
    seen = set()
    for s in index_skills:
        if s in seen:
            add(ERROR, phase, f"Duplicate slug `{s}` in SKILL_INDEX.md")
            count += 1
        seen.add(s)

    index_agents = []
    if AGENT_INDEX.exists():
        content = AGENT_INDEX.read_text(encoding="utf-8")
        for m in re.finditer(r'^\|\s*`([^`]+)`', content, re.MULTILINE):
            index_agents.append(m.group(1))
    seen = set()
    for a in index_agents:
        if a in seen:
            add(ERROR, phase, f"Duplicate slug `{a}` in AGENT_INDEX.md")
            count += 1
        seen.add(a)

    # Check for skill dirs with similar prefixes (potential consolidation)
    prefix_groups = defaultdict(list)
    for slug in fs_skills:
        # Use first two segments as prefix (e.g. "luke-iha")
        parts = slug.split("-")
        if len(parts) >= 2:
            prefix = "-".join(parts[:2])
            prefix_groups[prefix].append(slug)

    for prefix, members in sorted(prefix_groups.items()):
        if len(members) > 3:
            add(INFO, phase,
                f"Expert `{prefix}` has {len(members)} skill directories — consider if consolidation needed",
                ", ".join(sorted(members)))

    return count


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------
def generate_report(output_json=False, errors_only=False):
    """Run all phases and generate the report."""

    # Run all phases
    phase_skill_integrity()
    phase_agent_integrity()
    phase_index_sync()
    phase_slash_workflow_mapping()
    phase_council_domain_check()
    phase_duplicate_detection()

    # Filter
    if errors_only:
        filtered = [f for f in findings if f.severity == ERROR]
    else:
        filtered = findings

    # Stats
    errors = sum(1 for f in findings if f.severity == ERROR)
    warnings = sum(1 for f in findings if f.severity == WARNING)
    infos = sum(1 for f in findings if f.severity == INFO)

    # Count assets
    fs_skills = get_filesystem_dirs(SKILLS_DIR)
    fs_agents = get_filesystem_dirs(AGENTS_DIR)
    workflow_files = get_workflow_files()
    slash_cmds = parse_slash_commands(SLASH_COMMANDS)

    if output_json:
        result = {
            "summary": {
                "skills": len(fs_skills),
                "agents": len(fs_agents),
                "workflows": len(workflow_files),
                "slash_commands": len(slash_cmds),
                "errors": errors,
                "warnings": warnings,
                "info": infos,
            },
            "findings": [f.to_dict() for f in filtered],
        }
        print(json.dumps(result, indent=2))
    else:
        print("# Antigravity System Verification Report\n")
        print(f"**Skills**: {len(fs_skills)} | **Agents**: {len(fs_agents)} | "
              f"**Workflows**: {len(workflow_files)} | **Slash Commands**: {len(slash_cmds)}\n")

        # Summary bar
        if errors == 0 and warnings == 0:
            print("✅ **ALL CLEAR** — No errors or warnings found.\n")
        else:
            print(f"{'❌' if errors else '⚠️'} **{errors} errors** | **{warnings} warnings** | **{infos} info**\n")

        # Group by phase
        phases = {}
        for f in filtered:
            phases.setdefault(f.phase, []).append(f)

        phase_labels = {
            "skill-integrity": "Phase 1: Skill Integrity",
            "agent-integrity": "Phase 2: Agent Integrity",
            "index-sync": "Phase 3: Index ↔ Filesystem Sync",
            "slash-workflow": "Phase 4: Slash Command → Workflow Mapping",
            "council-domain": "Phase 5: COUNCIL & DOMAIN_REGISTRY Cross-Check",
            "duplicates": "Phase 6: Duplicate Detection",
        }

        for phase_key in ["skill-integrity", "agent-integrity", "index-sync",
                          "slash-workflow", "council-domain", "duplicates"]:
            items = phases.get(phase_key, [])
            label = phase_labels.get(phase_key, phase_key)
            e = sum(1 for i in items if i.severity == ERROR)
            w = sum(1 for i in items if i.severity == WARNING)
            inf = sum(1 for i in items if i.severity == INFO)

            if not items:
                print(f"## {label} — ✅ Clean\n")
            else:
                status = "❌" if e else "⚠️"
                print(f"## {label} — {status} {e}E / {w}W / {inf}I\n")
                for f in items:
                    print(f"  {f}")
                print()

        # Auto-fix suggestions
        if errors > 0:
            print("---\n## Suggested Fixes\n")
            if any(f.phase == "index-sync" for f in findings if f.severity == ERROR):
                print("- Run `python execution/sync_registries.py` to rebuild SKILL_INDEX.md and AGENT_INDEX.md")
            if any(f.phase == "slash-workflow" for f in findings if f.severity == ERROR):
                print("- Create missing workflow files or remove stale entries from SLASH_COMMANDS.md")
            if any(f.phase == "skill-integrity" for f in findings if f.severity == WARNING):
                print("- Add SKILL.md to incomplete skill directories, or delete empty ones")
            print()

    # Exit code
    if errors > 0:
        return 1
    elif warnings > 0:
        return 2
    return 0


def main():
    parser = argparse.ArgumentParser(description="Antigravity Universal System Verification")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--errors-only", action="store_true", help="Only show errors")
    args = parser.parse_args()
    exit_code = generate_report(output_json=args.json, errors_only=args.errors_only)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
