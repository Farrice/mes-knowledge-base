#!/usr/bin/env python3
"""
Routing Audit — Identifies agents missing from routing layers.

Checks 3 routing layers:
1. Intent Pipeline domain detection table
2. Domain Registry swim lanes
3. Invocation cards

Produces a gap report and routing test suite.
"""
import os
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).parent.parent
AGENTS_DIR = ROOT / "agents"
DOMAIN_REGISTRY = ROOT / "DOMAIN_REGISTRY.md"
INTENT_PIPELINE = ROOT / "directives" / "intent-pipeline.md"
INVOCATION_CARDS = ROOT / "agents" / "_framework" / "invocation-cards.md"
WORKFLOWS_DIR = ROOT / ".agent" / "workflows"
LIVE_SKILLS_DIR = ROOT / ".agents" / "skills"
COLD_SKILLS_DIR = ROOT / ".agents" / "cold-skills" / "source-command-wrappers"

CONTROL_PLANE_ROUTES = {
    "operator-autopilot": "autopilot",
    "antigravity-orchestrator": "orchestrate",
    "knowledge-librarian": "knowledge-librarian",
    "quality-judge": "quality-judge",
}

PRIMARY_EXECUTION_AGENTS = {
    "ideation-agent",
    "content-media-agent",
    "marketing-agent",
    "creative-design-agent",
    "copywriting-agent",
    "writing-agent",
    "messaging-positioning-agent",
    "revenue-offer-agent",
    "client-delivery-agent",
    "proof-case-study-agent",
    "extraction-governor-agent",
    "research-intelligence-agent",
    "data-analysis-agent",
    "ground-truth-agent",
    "red-team-agent",
    "evolution-agent",
}


def read_file(path):
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


def get_all_agents():
    """Get all agent slugs from the agents/ directory."""
    agents = []
    for item in sorted(os.listdir(AGENTS_DIR)):
        if item.startswith("_") or item.startswith("."):
            continue
        if (AGENTS_DIR / item).is_dir():
            agents.append(item)
    return agents


def extract_agents_from_registry(content):
    """Find all agent names/slugs mentioned in the Domain Registry."""
    found = set()
    # Match **Name** patterns in tables and code blocks
    for match in re.findall(r'\*\*([^*]+)\*\*', content):
        name = match.strip()
        if len(name) > 2 and len(name) < 60:
            found.add(name.lower())
    # Match slug patterns in backticks
    for match in re.findall(r'`([a-z][a-z0-9-]+)`', content):
        found.add(match.lower())
    # Match [Name] patterns in code blocks
    for match in re.findall(r'\[([A-Z][^\]]+)\]', content):
        found.add(match.lower())
    return found


def normalize(text):
    """Remove apostrophes, periods, spaces, and special chars for fuzzy matching."""
    return re.sub(r"['.() \-&]", "", text).lower().strip()


def slug_matches_text(slug, text_set):
    """Check if an agent slug matches any text in the set."""
    norm_slug = normalize(slug.replace("-", " "))
    # Direct slug match
    if slug in text_set:
        return True
    # Normalized name match
    for text in text_set:
        norm_text = normalize(text)
        if norm_slug == norm_text or norm_slug in norm_text or norm_text in norm_slug:
            return True
    # Partial name match (last name or key part)
    parts = slug.split("-")
    for part in parts:
        if len(part) > 4:  # Only match on substantial name parts
            for text in text_set:
                if part in normalize(text):
                    return True
    return False


def extract_domain_sections(content):
    """Extract domain sections and their agents from Domain Registry."""
    domains = {}
    current_domain = None

    for line in content.split("\n"):
        # Match domain headers
        domain_match = re.match(r'^## Domain \d+:\s*(.+)', line)
        if domain_match:
            current_domain = domain_match.group(1).strip()
            domains[current_domain] = []
            continue

        if current_domain:
            # Match agent names in tables
            table_match = re.match(r'\|\s*\*\*([^*]+)\*\*\s*\|', line)
            if table_match:
                domains[current_domain].append(table_match.group(1).strip())

            # Match agents in code blocks [Name]
            code_matches = re.findall(r'\[([A-Z][^\]]+)\]', line)
            for name in code_matches:
                if name not in domains[current_domain]:
                    domains[current_domain].append(name)

    return domains


def extract_invocation_card_agents(content):
    """Extract agent names from invocation cards."""
    agents = []
    for match in re.findall(r'^AGENT:\s*(.+)', content, re.MULTILINE):
        agents.append(match.strip())
    return agents


def map_slug_to_card_name(slug, card_agents):
    """Find the invocation card name for a given slug."""
    name_parts = slug.replace("-", " ").lower()
    for card_name in card_agents:
        if name_parts in card_name.lower() or card_name.lower() in name_parts:
            return card_name
        # Check last name match
        slug_parts = slug.split("-")
        card_parts = card_name.lower().split()
        for sp in slug_parts:
            if len(sp) > 3 and sp in card_parts:
                return card_name
    return None


def extract_intent_pipeline_agents(content):
    """Extract agent names from the intent pipeline domain detection table."""
    found = set()
    for match in re.findall(r'\*\*([^*]+)\*\*', content):
        found.add(match.strip().lower())
    # Also check for names after | in table rows
    for match in re.findall(r'\|\s*([^|]+)\s*\|', content):
        for name in re.findall(r'[A-Z][a-z]+ [A-Z][a-z]+', match):
            found.add(name.lower())
    return found


def build_routing_coverage_report():
    """Build comprehensive routing coverage analysis."""
    all_agents = get_all_agents()

    # Read all routing files
    registry_content = read_file(DOMAIN_REGISTRY)
    pipeline_content = read_file(INTENT_PIPELINE)
    cards_content = read_file(INVOCATION_CARDS)

    # Extract data from each layer
    registry_mentions = extract_agents_from_registry(registry_content)
    domain_sections = extract_domain_sections(registry_content)
    card_agents = extract_invocation_card_agents(cards_content)
    pipeline_mentions = extract_intent_pipeline_agents(pipeline_content)

    # Map each agent to routing layers
    coverage = []
    for slug in all_agents:
        in_registry = slug_matches_text(slug, registry_mentions)
        in_cards = map_slug_to_card_name(slug, card_agents) is not None
        in_pipeline = slug_matches_text(slug, pipeline_mentions)
        card_name = map_slug_to_card_name(slug, card_agents)

        # Find which domain(s) the agent is in
        domains_found = []
        for domain, agents in domain_sections.items():
            for agent_name in agents:
                if slug_matches_text(slug, {agent_name.lower()}):
                    domains_found.append(domain)
                    break

        coverage.append({
            "slug": slug,
            "card_name": card_name or "(no card)",
            "in_registry": in_registry,
            "in_pipeline": in_pipeline,
            "in_cards": in_cards,
            "domains": domains_found,
            "layers": sum([in_registry, in_pipeline, in_cards])
        })

    return coverage, domain_sections, card_agents


def has_routing_interop(slug: str) -> bool:
    return "## Routing Interop" in read_file(AGENTS_DIR / slug / "AGENT.md")


def route_for_agent(slug: str) -> str:
    if slug in CONTROL_PLANE_ROUTES:
        return CONTROL_PLANE_ROUTES[slug]
    return slug


def workflow_exists(route: str) -> bool:
    return (WORKFLOWS_DIR / f"{route}.md").exists()


def bridge_exists(route: str) -> bool:
    bridge = f"source-command-{route}"
    return (LIVE_SKILLS_DIR / bridge).exists() or (COLD_SKILLS_DIR / bridge).exists()


def command_route_available(route: str) -> bool:
    return workflow_exists(route) and bridge_exists(route)


def classify_tier(row: dict[str, Any]) -> str:
    slug = row["slug"]
    if slug in CONTROL_PLANE_ROUTES:
        return "control-plane-operator"
    if slug in PRIMARY_EXECUTION_AGENTS:
        return "primary-execution"
    if row["layers"] == 0:
        return "cold/source-only" if has_routing_interop(slug) else "unclassified-cold"
    return "expert/persona"


def tier_compliance(row: dict[str, Any]) -> tuple[bool, str]:
    slug = row["slug"]
    tier = row["tier"]
    if tier == "control-plane-operator":
        route = route_for_agent(slug)
        missing = []
        if not has_routing_interop(slug):
            missing.append("Routing Interop")
        if not workflow_exists(route):
            missing.append(f".agent/workflows/{route}.md")
        if not bridge_exists(route):
            missing.append(f"source-command-{route} bridge")
        if missing:
            return False, "missing " + ", ".join(missing)
        return True, f"full operator route via /{route}"

    if tier == "primary-execution":
        if row["in_registry"] or row["in_cards"]:
            return True, "registry/card coverage present"
        return False, "primary execution agent lacks registry or invocation-card coverage"

    if tier == "cold/source-only":
        return True, "classified cold/source-only with Routing Interop; no full routing required"

    if tier == "unclassified-cold":
        return False, "unrouted agent lacks cold/source-only classification"

    return True, "expert/persona coverage is sufficient"


def build_tiered_routing_report() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    coverage, domain_sections, card_agents = build_routing_coverage_report()
    rows: list[dict[str, Any]] = []
    for item in coverage:
        row = dict(item)
        row["tier"] = classify_tier(row)
        row["route"] = route_for_agent(row["slug"])
        row["has_routing_interop"] = has_routing_interop(row["slug"])
        row["workflow_exists"] = workflow_exists(row["route"])
        row["bridge_exists"] = bridge_exists(row["route"])
        compliant, reason = tier_compliance(row)
        row["tier_compliant"] = compliant
        row["tier_reason"] = reason
        rows.append(row)

    summary = {
        "total": len(rows),
        "legacy_fully_routed": sum(1 for row in rows if row["layers"] == 3),
        "legacy_unrouted": sum(1 for row in rows if row["layers"] == 0),
        "tier_compliant": sum(1 for row in rows if row["tier_compliant"]),
        "tier_noncompliant": sum(1 for row in rows if not row["tier_compliant"]),
        "control_plane": sum(1 for row in rows if row["tier"] == "control-plane-operator"),
        "primary_execution": sum(1 for row in rows if row["tier"] == "primary-execution"),
        "expert_persona": sum(1 for row in rows if row["tier"] == "expert/persona"),
        "cold_source_only": sum(1 for row in rows if row["tier"] == "cold/source-only"),
        "unclassified_cold": sum(1 for row in rows if row["tier"] == "unclassified-cold"),
        "domain_sections": domain_sections,
        "card_agents": card_agents,
    }
    return rows, summary


def suggest_domain_for_agent(slug, cards_content):
    """Suggest a domain category for an unrouted agent based on its card."""
    # Extract the card for this agent
    card_match = None
    for block in re.split(r'```', cards_content):
        if slug.replace("-", " ") in block.lower() or any(
            part in block.lower() for part in slug.split("-") if len(part) > 3
        ):
            card_match = block
            break

    if not card_match:
        return "Unknown"

    content_lower = card_match.lower()

    # Domain classification heuristics
    if any(kw in content_lower for kw in ["copy", "conversion", "sales page", "headline", "direct response", "rhetoric", "proof"]):
        return "Copywriting"
    if any(kw in content_lower for kw in ["linkedin", "personal brand", "positioning", "authority", "magnetic"]):
        return "Personal Brand"
    if any(kw in content_lower for kw in ["tiktok", "viral", "content", "storytelling", "hook", "dopamine"]):
        return "Content & Viral"
    if any(kw in content_lower for kw in ["sales", "persuasion", "objection", "close", "identity selling", "belief change"]):
        return "Sales & Persuasion"
    if any(kw in content_lower for kw in ["research", "intelligence", "strategy", "philosophy", "finance", "economics"]):
        return "Strategy & Research"
    if any(kw in content_lower for kw in ["ai", "agent", "workflow", "automation", "prompt", "context engineering"]):
        return "AI & Systems"
    if any(kw in content_lower for kw in ["product", "offer", "pricing", "launch", "monetization", "revenue"]):
        return "Products & Monetization"
    if any(kw in content_lower for kw in ["seo", "search", "rank", "traffic", "affiliate", "keyword"]):
        return "SEO & Search"
    if any(kw in content_lower for kw in ["design", "visual", "website", "motion", "typography", "aesthetic"]):
        return "Design & Web"
    if any(kw in content_lower for kw in ["video", "media", "production", "cinematic", "storyboard"]):
        return "Video & Media"
    if any(kw in content_lower for kw in ["writing", "literary", "prose", "narrative", "essay", "story"]):
        return "Writing & Storytelling"
    if any(kw in content_lower for kw in ["mindset", "identity", "transformation", "coaching", "psychology"]):
        return "Mindset & Transformation"
    if any(kw in content_lower for kw in ["newsletter", "audience", "growth", "community", "subscriber"]):
        return "Audience & Growth"
    if any(kw in content_lower for kw in ["communications", "pr", "messaging", "culture", "reputation"]):
        return "Communications & Messaging"
    if any(kw in content_lower for kw in ["consulting", "leverage", "scaling"]):
        return "Consulting & Services"
    if any(kw in content_lower for kw in ["real estate"]):
        return "Industry-Specific"
    if any(kw in content_lower for kw in ["humor", "comedy", "funny"]):
        return "Creative & Humor"

    return "Uncategorized"


def main():
    coverage, domain_sections, card_agents = build_routing_coverage_report()
    tiered_rows, tiered_summary = build_tiered_routing_report()
    cards_content = read_file(INVOCATION_CARDS)

    # Summary stats
    total = len(coverage)
    in_registry = sum(1 for c in coverage if c["in_registry"])
    in_pipeline = sum(1 for c in coverage if c["in_pipeline"])
    in_cards = sum(1 for c in coverage if c["in_cards"])
    fully_routed = sum(1 for c in coverage if c["layers"] == 3)
    partially_routed = sum(1 for c in coverage if 0 < c["layers"] < 3)
    unrouted = sum(1 for c in coverage if c["layers"] == 0)

    print(f"\n{'='*60}")
    print(f"ROUTING COVERAGE AUDIT")
    print(f"{'='*60}")
    print(f"\nTotal agents: {total}")
    print(f"In Domain Registry:  {in_registry}/{total}")
    print(f"In Intent Pipeline:  {in_pipeline}/{total}")
    print(f"In Invocation Cards: {in_cards}/{total}")
    print(f"\nFully routed (all 3 layers):  {fully_routed}")
    print(f"Partially routed (1-2):       {partially_routed}")
    print(f"Not routed at all:            {unrouted}")
    print(f"\nTiered compliant:             {tiered_summary['tier_compliant']}/{total}")
    print(f"Tiered noncompliant:          {tiered_summary['tier_noncompliant']}")
    print(f"Cold/source-only classified:  {tiered_summary['cold_source_only']}")

    # Write detailed report
    output_path = ROOT / ".tmp" / "routing-audit.md"
    output_path.parent.mkdir(exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# Routing Coverage Audit\n\n")
        f.write(f"**Generated**: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")

        f.write("## Summary\n\n")
        f.write("### Legacy All-Layers Coverage\n\n")
        f.write(f"| Layer | Coverage |\n")
        f.write(f"|-------|----------|\n")
        f.write(f"| Domain Registry | {in_registry}/{total} |\n")
        f.write(f"| Intent Pipeline | {in_pipeline}/{total} |\n")
        f.write(f"| Invocation Cards | {in_cards}/{total} |\n")
        f.write(f"| **Fully Routed (3/3)** | **{fully_routed}/{total}** |\n\n")

        f.write("### Tiered Routing Standard\n\n")
        f.write("| Tier | Count | Requirement |\n")
        f.write("|---|---:|---|\n")
        f.write(f"| Control-plane operators | {tiered_summary['control_plane']} | Routing Interop + workflow + source-command bridge |\n")
        f.write(f"| Primary execution agents | {tiered_summary['primary_execution']} | Domain registry or invocation-card coverage |\n")
        f.write(f"| Expert/persona agents | {tiered_summary['expert_persona']} | Expertise context coverage; no full routing required |\n")
        f.write(f"| Cold/source-only agents | {tiered_summary['cold_source_only']} | Routing Interop classification; stay cold until needed |\n")
        f.write(f"| Unclassified cold agents | {tiered_summary['unclassified_cold']} | Must be classified or routed |\n\n")
        f.write(f"**Tiered compliant:** {tiered_summary['tier_compliant']}/{total}\n\n")
        f.write(f"**Tiered noncompliant:** {tiered_summary['tier_noncompliant']}\n\n")

        f.write("## Tiered Coverage Matrix\n\n")
        f.write("| Agent | Tier | Route | Layers | Compliant | Reason |\n")
        f.write("|---|---|---|---:|---|---|\n")
        for row in tiered_rows:
            ok = "Y" if row["tier_compliant"] else "N"
            reason = str(row["tier_reason"]).replace("|", "\\|")
            f.write(f"| `{row['slug']}` | {row['tier']} | `/{row['route']}` | {row['layers']} | {ok} | {reason} |\n")
        f.write("\n")

        # Current Domain Registry structure
        f.write("## Current Domain Registry Structure\n\n")
        for domain, agents in domain_sections.items():
            f.write(f"### {domain}\n")
            f.write(f"Agents: {', '.join(agents)}\n\n")

        # Agents missing from Domain Registry
        missing_from_registry = [c for c in coverage if not c["in_registry"]]
        f.write(f"\n## Agents Missing from Domain Registry ({len(missing_from_registry)})\n\n")

        # Group by suggested domain
        domain_suggestions = {}
        for c in missing_from_registry:
            suggested = suggest_domain_for_agent(c["slug"], cards_content)
            if suggested not in domain_suggestions:
                domain_suggestions[suggested] = []
            domain_suggestions[suggested].append(c)

        for domain in sorted(domain_suggestions.keys()):
            agents = domain_suggestions[domain]
            f.write(f"\n### Suggested: {domain}\n")
            for c in agents:
                f.write(f"- `{c['slug']}` ({c['card_name']})\n")

        # Agents missing from Intent Pipeline
        missing_from_pipeline = [c for c in coverage if not c["in_pipeline"]]
        f.write(f"\n## Agents Missing from Intent Pipeline ({len(missing_from_pipeline)})\n\n")
        for c in missing_from_pipeline:
            f.write(f"- `{c['slug']}` — suggested domain: {suggest_domain_for_agent(c['slug'], cards_content)}\n")

        # Full coverage matrix
        f.write("\n## Full Coverage Matrix\n\n")
        f.write("| Agent | Card | Registry | Pipeline | Domains |\n")
        f.write("|-------|------|----------|----------|----------|\n")
        for c in coverage:
            reg = "Y" if c["in_registry"] else "-"
            pip = "Y" if c["in_pipeline"] else "-"
            card = "Y" if c["in_cards"] else "-"
            domains = ", ".join(c["domains"]) if c["domains"] else "-"
            f.write(f"| `{c['slug']}` | {card} | {reg} | {pip} | {domains} |\n")

    print(f"\nDetailed report -> {output_path}")
    return coverage, domain_sections


if __name__ == "__main__":
    main()
