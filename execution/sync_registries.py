#!/usr/bin/env python3
"""
Sync Registries — Populates AGENT_INDEX.md and SKILL_INDEX.md
Enhanced to extract keywords from file content, not just frontmatter.
"""
import os
import re

SKILLS_DIR = "skills"
AGENTS_DIR = "agents"
SKILL_INDEX = "SKILL_INDEX.md"
AGENT_INDEX = "AGENT_INDEX.md"


def read_file(path):
    """Read a file and return its contents."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return ""


def extract_frontmatter_and_content(file_path):
    """Extract YAML frontmatter (if any) and the body content."""
    content = read_file(file_path)
    if not content:
        return {}, ""

    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if match:
        fm_text = match.group(1)
        body = match.group(2)
        # Simple key-value parsing (avoids PyYAML dependency)
        fm = {}
        for line in fm_text.split("\n"):
            line = line.strip()
            if ":" in line and not line.startswith("#"):
                key, _, val = line.partition(":")
                key = key.strip()
                val = val.strip().strip('"').strip("'")
                if val and not val.startswith("[") and not val.startswith("{"):
                    fm[key] = val
        return fm, body
    return {}, content


def extract_agent_name(fm, body, slug):
    """Extract the agent's display name from frontmatter or heading."""
    # Try frontmatter fields
    for field in ["name", "expert"]:
        if fm.get(field):
            return fm[field]

    # Try first H1 heading
    heading_match = re.search(r'^#\s+(.+)', body, re.MULTILINE)
    if heading_match:
        heading = heading_match.group(1).strip()
        # Clean up common patterns like "# April Dunford — B2B Positioning Expert"
        if "—" in heading:
            return heading.split("—")[0].strip()
        if " - " in heading:
            return heading.split(" - ")[0].strip()
        # If heading is just "Agent Name Agent", clean it
        heading = re.sub(r'\s+Agent$', '', heading)
        return heading

    # Fallback: humanize slug
    return slug.replace("-", " ").title()


def extract_agent_keywords(fm, body, slug):
    """Extract domain keywords from agent file content."""
    keywords = set()

    # 1. Frontmatter domain field
    if fm.get("domain"):
        for kw in re.split(r'[,;&]+', fm["domain"]):
            kw = kw.strip()
            if kw and len(kw) > 2:
                keywords.add(kw.lower())

    # 2. Frontmatter keywords field
    if fm.get("keywords"):
        for kw in re.split(r'[,;&]+', fm["keywords"]):
            kw = kw.strip()
            if kw and len(kw) > 2:
                keywords.add(kw.lower())

    # 3. First heading — often contains the domain
    heading_match = re.search(r'^#\s+(.+)', body, re.MULTILINE)
    if heading_match:
        heading = heading_match.group(1)
        # Extract domain part after name separator
        for sep in ["—", " - ", ":"]:
            if sep in heading:
                domain_part = heading.split(sep, 1)[1].strip()
                for kw in re.split(r'[,;&]+', domain_part):
                    kw = kw.strip()
                    if kw and len(kw) > 2:
                        keywords.add(kw.lower())

    # 4. Domain/invocation line patterns
    domain_match = re.search(r'\*\*Domain\*\*:\s*(.+)', body, re.IGNORECASE)
    if domain_match:
        for kw in re.split(r'[,;&]+', domain_match.group(1)):
            kw = kw.strip().strip("*")
            if kw and len(kw) > 2:
                keywords.add(kw.lower())

    # 5. Competency section — extract high-level terms
    comp_match = re.search(
        r'##\s*(?:Core\s+)?Competenc(?:ies|y)(.*?)(?=\n##|\Z)',
        body, re.DOTALL | re.IGNORECASE
    )
    if comp_match:
        comp_text = comp_match.group(1)
        # Extract bold terms (often the competency names)
        bold_terms = re.findall(r'\*\*([^*]+)\*\*', comp_text)
        for term in bold_terms[:8]:  # Cap at 8 to avoid noise
            term = term.strip().rstrip(":")
            if len(term) > 2 and len(term) < 60:
                keywords.add(term.lower())

    # 6. Core Philosophy / Core Method
    for pattern in [
        r'\*\*Core (?:Philosophy|Method)\*\*[:\s]*(.+)',
        r'##\s*Core Philosophy\n+(.*?)(?=\n##|\Z)',
    ]:
        match = re.search(pattern, body, re.DOTALL | re.IGNORECASE)
        if match:
            text = match.group(1)[:200]  # First 200 chars
            # Extract quoted or bolded key terms
            for term in re.findall(r'\*\*([^*]+)\*\*', text):
                if len(term) > 2 and len(term) < 40:
                    keywords.add(term.lower())

    # Deduplicate and clean
    cleaned = set()
    for kw in keywords:
        kw = kw.strip().rstrip(".")
        # Skip overly generic terms
        if kw in {"the", "and", "for", "you", "are", "this", "that", "with"}:
            continue
        if len(kw) > 2:
            cleaned.add(kw)

    return sorted(cleaned)


def extract_skill_keywords(fm, body, slug):
    """Extract domain keywords from skill file content."""
    keywords = []

    # 1. Frontmatter description — richest source for skills
    if fm.get("description"):
        desc = fm["description"]
        # Clean pipe chars that break markdown tables
        desc = desc.replace("|", "")
        # Split on periods/semicolons for distinct phrases
        for segment in re.split(r'[.;]+', desc):
            segment = segment.strip()
            if len(segment) > 5 and len(segment) < 80:
                keywords.append(segment.lower())

    # 2. First heading domain part (after name separator)
    heading_match = re.search(r'^#\s+(.+)', body, re.MULTILINE)
    if heading_match:
        heading = heading_match.group(1).replace("|", "")
        for sep in [":", "—", " - "]:
            if sep in heading:
                domain_part = heading.split(sep, 1)[1].strip()
                if len(domain_part) > 3:
                    keywords.append(domain_part.lower())

    # Deduplicate while preserving order, cap at 3 for table readability
    seen = set()
    unique = []
    for kw in keywords:
        if kw not in seen:
            seen.add(kw)
            unique.append(kw)
    return unique[:3]


def sync_agents():
    """Sync AGENT_INDEX.md with content-extracted keywords."""
    print("Syncing AGENT_INDEX.md...")
    agents = []

    for item in sorted(os.listdir(AGENTS_DIR)):
        if item.startswith("_") or item.startswith("."):
            continue
        agent_path = os.path.join(AGENTS_DIR, item)
        if not os.path.isdir(agent_path):
            continue
        agent_md = os.path.join(agent_path, "AGENT.md")
        if not os.path.isfile(agent_md):
            continue

        fm, body = extract_frontmatter_and_content(agent_md)
        name = extract_agent_name(fm, body, item)
        keywords = extract_agent_keywords(fm, body, item)
        keyword_str = ", ".join(keywords)

        agents.append({
            "slug": item,
            "name": name,
            "keywords": keyword_str
        })

    with open(AGENT_INDEX, "w", encoding="utf-8") as f:
        f.write("# Agent Registry Directory\n\n")
        f.write("> Auto-generated by sync_registries.py. **Do not edit manually**.\n>\n")
        f.write("> Use this index to find the right expert alias for a specific task. ")
        f.write("Remember, agents embody methodologies.\n\n")
        f.write("| Agent Slug | Persona | Domain/Keywords |\n")
        f.write("|------------|---------|-----------------|\n")
        for a in agents:
            f.write(f"| `{a['slug']}` | **{a['name']}** | {a['keywords']} |\n")

    populated = sum(1 for a in agents if a["keywords"])
    print(f"✅ Synced {len(agents)} agents to AGENT_INDEX.md ({populated} with keywords).")


def sync_skills():
    """Sync SKILL_INDEX.md with content-extracted keywords and workflow counts."""
    print("Syncing SKILL_INDEX.md...")
    skills = []

    for item in sorted(os.listdir(SKILLS_DIR)):
        if item.startswith("_") or item.startswith("."):
            continue
        skill_path = os.path.join(SKILLS_DIR, item)
        if not os.path.isdir(skill_path):
            continue
        skill_md = os.path.join(skill_path, "SKILL.md")
        if not os.path.isfile(skill_md):
            continue

        fm, body = extract_frontmatter_and_content(skill_md)

        # Name from frontmatter or slug
        name = fm.get("name", item.replace("-", " ").title())

        # Count workflows (completion engine) instead of legacy prompts
        workflows_dir = os.path.join(skill_path, "workflows")
        workflow_count = 0
        if os.path.isdir(workflows_dir):
            workflow_count = len([f for f in os.listdir(workflows_dir) if f.endswith(".md")])

        # Also count legacy prompts for reference
        prompts_dir = os.path.join(skill_path, "references", "prompts")
        prompt_count = 0
        if os.path.isdir(prompts_dir):
            prompt_count = len([f for f in os.listdir(prompts_dir) if f.endswith(".md")])

        # Extract keywords
        keywords = extract_skill_keywords(fm, body, item)
        keyword_str = ", ".join(keywords)

        skills.append({
            "slug": item,
            "name": name,
            "keywords": keyword_str,
            "workflow_count": workflow_count,
            "prompt_count": prompt_count
        })

    with open(SKILL_INDEX, "w", encoding="utf-8") as f:
        f.write("# Skill Registry Directory\n\n")
        f.write("> Auto-generated by sync_registries.py. **Do not edit manually**.\n>\n")
        f.write("> Use this index to identify the correct skill for a specific task. ")
        f.write("Read the skill's `SKILL.md` to load its methodology into context.\n\n")
        f.write("| Skill Slug | Expert Name | Domain/Keywords | Workflows | Legacy Prompts |\n")
        f.write("|------------|-------------|-----------------|-----------|----------------|\n")
        for s in skills:
            f.write(f"| `{s['slug']}` | **{s['name']}** | {s['keywords']} | {s['workflow_count']} | {s['prompt_count']} |\n")

    populated = sum(1 for s in skills if s["keywords"])
    print(f"✅ Synced {len(skills)} skills to SKILL_INDEX.md ({populated} with keywords).")


if __name__ == "__main__":
    if not os.path.exists(SKILLS_DIR) or not os.path.exists(AGENTS_DIR):
        print("Run this from the workspace root.")
        exit(1)

    sync_agents()
    sync_skills()
