#!/usr/bin/env python3
"""
Generate Invocation Cards — Creates card stubs for agents missing from invocation-cards.md
Reads each AGENT.md and extracts structured card fields.
"""

import os
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
AGENTS_DIR = ROOT / "agents"
INVOCATION_CARDS = ROOT / "agents" / "_framework" / "invocation-cards.md"
SKILLS_DIR = ROOT / "skills"


def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return ""


def get_existing_card_agents():
    """Get set of agent slugs already covered by invocation cards."""
    content = read_file(INVOCATION_CARDS)
    covered = set()
    content_lower = content.lower()

    for item in sorted(os.listdir(AGENTS_DIR)):
        if item.startswith("_") or item.startswith("."):
            continue
        agent_path = AGENTS_DIR / item
        if not agent_path.is_dir():
            continue
        # Fuzzy match: check if slug or name appears in cards
        slug_parts = item.split("-")
        name_pattern = " ".join(slug_parts)
        if name_pattern in content_lower or item in content_lower:
            covered.add(item)

    return covered


def extract_frontmatter_and_content(file_path):
    content = read_file(file_path)
    if not content:
        return {}, ""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if match:
        fm = {}
        for line in match.group(1).split("\n"):
            if ":" in line:
                key, _, val = line.partition(":")
                fm[key.strip()] = val.strip().strip('"').strip("'")
        return fm, match.group(2)
    return {}, content


def extract_agent_name(fm, body, slug):
    """Extract clean display name."""
    for field in ["name", "expert"]:
        if fm.get(field):
            val = fm[field]
            if val.lower() != slug:
                return val

    heading_match = re.search(r'^#\s+(.+)', body, re.MULTILINE)
    if heading_match:
        heading = heading_match.group(1).strip()
        for sep in ["—", " - ", ":"]:
            if sep in heading:
                return heading.split(sep)[0].strip()
        heading = re.sub(r'\s+Agent$', '', heading)
        if heading.lower() != slug:
            return heading

    return slug.replace("-", " ").title()


def extract_domain(fm, body):
    """Extract domain description."""
    if fm.get("domain"):
        return fm["domain"]

    # Try heading after separator
    heading_match = re.search(r'^#\s+(.+)', body, re.MULTILINE)
    if heading_match:
        heading = heading_match.group(1)
        for sep in ["—", " - ", ":"]:
            if sep in heading:
                return heading.split(sep, 1)[1].strip()

    # Try **Domain**: pattern
    domain_match = re.search(r'\*\*Domain\*\*:\s*(.+)', body, re.IGNORECASE)
    if domain_match:
        return domain_match.group(1).strip().strip("*")

    return ""


def extract_core_method(body):
    """Extract the core methodology or philosophy."""
    # Try Core Philosophy section
    for pattern in [
        r'##\s*Core Philosophy\n+(.*?)(?=\n##|\Z)',
        r'##\s*Core Method(?:ology)?\n+(.*?)(?=\n##|\Z)',
        r'\*\*Core (?:Philosophy|Method)\*\*[:\s]*(.+)',
    ]:
        match = re.search(pattern, body, re.DOTALL | re.IGNORECASE)
        if match:
            text = match.group(1).strip()
            # Get first bullet or first meaningful line
            lines = [l.strip().lstrip("-*• ").strip() for l in text.split("\n") if l.strip() and not l.strip().startswith("#")]
            if lines:
                # Take first substantive line, clean it up
                first = lines[0]
                # Remove markdown bold
                first = re.sub(r'\*\*([^*]+)\*\*', r'\1', first)
                if len(first) > 120:
                    first = first[:117] + "..."
                return first

    # Try first bold statement after identity
    bold_match = re.search(r'\*\*([^*]{15,100})\*\*', body)
    if bold_match:
        return bold_match.group(1)

    return ""


def extract_best_for(body):
    """Extract what the agent is best for."""
    # Try Competencies section — get first 3-4 competency names
    comp_match = re.search(
        r'##\s*(?:Core\s+)?Competenc(?:ies|y)(.*?)(?=\n##|\Z)',
        body, re.DOTALL | re.IGNORECASE
    )
    if comp_match:
        bold_terms = re.findall(r'\*\*([^*]+)\*\*', comp_match.group(1))
        cleaned = [t.strip().rstrip(":") for t in bold_terms if len(t) > 3 and len(t) < 50]
        if cleaned:
            return ", ".join(cleaned[:4])

    # Try Available Skills section
    skills_match = re.search(
        r'##\s*Available Skills(.*?)(?=\n##|\Z)',
        body, re.DOTALL | re.IGNORECASE
    )
    if skills_match:
        caps = re.findall(r'\|\s*([^|]+?)\s*\|', skills_match.group(1))
        cleaned = [c.strip() for c in caps if len(c) > 3 and len(c) < 50 and not c.startswith("-")]
        if cleaned:
            return ", ".join(cleaned[:4])

    return ""


def find_matching_skill(slug):
    """Find the best matching skill entry prompt for an agent."""
    # Direct match patterns
    if os.path.isdir(SKILLS_DIR):
        for skill_dir in os.listdir(SKILLS_DIR):
            if slug in skill_dir:
                return f"skills/{skill_dir}/SKILL.md"
    return ""


def generate_card(slug):
    """Generate an invocation card for a single agent."""
    agent_md = AGENTS_DIR / slug / "AGENT.md"
    if not agent_md.exists():
        return None

    fm, body = extract_frontmatter_and_content(agent_md)

    name = extract_agent_name(fm, body, slug)
    domain = extract_domain(fm, body)
    core_method = extract_core_method(body)
    best_for = extract_best_for(body)
    entry_prompt = find_matching_skill(slug)

    if not domain and not core_method:
        return None

    card = f"AGENT: {name}\n"
    card += f"DOMAIN: {domain}\n" if domain else "DOMAIN: (needs manual entry)\n"
    card += f"CORE METHOD: {core_method}\n" if core_method else "CORE METHOD: (needs manual entry)\n"
    card += f"BEST FOR: {best_for}\n" if best_for else "BEST FOR: (needs manual entry)\n"
    card += f"ENTRY PROMPT: {entry_prompt}\n" if entry_prompt else "ENTRY PROMPT: (needs manual entry)\n"
    card += f"PAIRS WITH: (needs manual entry)"

    return card


def main():
    covered = get_existing_card_agents()
    all_agents = sorted([
        item for item in os.listdir(AGENTS_DIR)
        if (AGENTS_DIR / item).is_dir()
        and not item.startswith("_")
        and not item.startswith(".")
    ])

    missing = [a for a in all_agents if a not in covered]
    print(f"Found {len(missing)} agents without invocation cards.\n")

    generated_cards = []
    skipped = []

    for slug in missing:
        card = generate_card(slug)
        if card:
            generated_cards.append((slug, card))
        else:
            skipped.append(slug)

    # Output to file
    output_path = ROOT / ".tmp" / "new-invocation-cards.md"
    output_path.parent.mkdir(exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# Generated Invocation Cards\n\n")
        f.write(f"> {len(generated_cards)} cards generated for agents missing from invocation-cards.md\n")
        f.write(f"> Review and append to `agents/_framework/invocation-cards.md`\n\n")

        # Group by approximate category
        f.write("---\n\n## New Cards (Auto-Generated)\n\n")
        for slug, card in generated_cards:
            f.write(f"```\n{card}\n```\n\n")

        if skipped:
            f.write(f"\n---\n\n## Skipped ({len(skipped)} agents — insufficient content)\n\n")
            for slug in skipped:
                f.write(f"- `{slug}`\n")

    print(f"✅ Generated {len(generated_cards)} invocation cards → {output_path}")
    if skipped:
        print(f"⚠️  Skipped {len(skipped)} agents (insufficient content to generate card)")
    print(f"\nNext: Review the cards, then append to agents/_framework/invocation-cards.md")


if __name__ == "__main__":
    main()
