#!/usr/bin/env python3
"""
Generate Council Report - Generate status of all experts and councils.

Usage:
    python generate_council_report.py
    python generate_council_report.py --output report.md
    python generate_council_report.py --json
"""

import os
import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple


# Base paths
BASE_PATH = Path(__file__).parent.parent
AGENTS_PATH = BASE_PATH / "agents"
SKILLS_PATH = BASE_PATH / "skills"
EXTRACTIONS_PATH = BASE_PATH / "knowledge" / "extractions"


# Expert registry
EXPERTS = {
    'jeremy-miner': {'domain': 'Sales, Identity Persuasion, NEPQ', 'tier': 'Revenue'},
    'michael-bernoff': {'domain': 'Identity Engineering, Mindset', 'tier': 'Revenue'},
    'harry-dry': {'domain': 'Copywriting, Marketing Examples', 'tier': 'Revenue'},
    'cardinal-mason': {'domain': 'AI Copywriting, Conversion', 'tier': 'Revenue'},
    'samuel-thompson': {'domain': 'AI Info Products, Launches', 'tier': 'Revenue'},
    'shaan-puri': {'domain': 'Storytelling, Content Strategy', 'tier': 'Content'},
    'caleb-ralston': {'domain': 'Personal Brand, Differentiation', 'tier': 'Content'},
    'dai-media': {'domain': 'Consumer Psychology, Posture', 'tier': 'Content'},
    'mitch-albom': {'domain': 'Writing Mastery, Storytelling', 'tier': 'Craft'},
    'dan-wang': {'domain': 'Writing, Observation, Analysis', 'tier': 'Craft'},
    'oscar-hoglund': {'domain': 'Sound, Storytelling, Media', 'tier': 'Craft'},
    'futurepedia': {'domain': 'Prompt Engineering, AI Tools', 'tier': 'AI'},
    'nate-b-jones': {'domain': 'AI Implementation, JARVIS', 'tier': 'AI'},
    'darrel-wilson': {'domain': 'AI Automation, Workflows', 'tier': 'AI'},
    'kittl': {'domain': 'Graphic Design, Visual', 'tier': 'Design'},
    'erica-mallet': {'domain': 'Brand Magnetism, Attraction', 'tier': 'Design'},
    'seena-rez': {'domain': 'TikTok Commerce, Viral Content', 'tier': 'Content'},
    'jim-oshaughnessy': {'domain': 'Philosophy, Finance, Synthesis', 'tier': 'Strategy'},
    'lulu-cheng-meservey': {'domain': 'Communications, PR Strategy', 'tier': 'Strategy'},
}


COUNCILS = {
    'revenue-council': ['jeremy-miner', 'michael-bernoff', 'cardinal-mason', 'samuel-thompson'],
    'content-council': ['shaan-puri', 'harry-dry', 'mitch-albom', 'dan-wang'],
    'brand-council': ['dai-media', 'caleb-ralston', 'lulu-cheng-meservey', 'erica-mallet'],
    'ai-council': ['futurepedia', 'nate-b-jones', 'darrel-wilson'],
    'creative-council': ['kittl', 'oscar-hoglund', 'seena-rez'],
}


def check_agent_status(expert: str) -> Dict:
    """Check the status of an agent."""
    agent_path = AGENTS_PATH / expert
    agent_md = agent_path / "AGENT.md"
    memory_context = agent_path / "memory" / "context.md"

    status = {
        'has_folder': agent_path.exists(),
        'has_agent_md': agent_md.exists(),
        'has_memory': memory_context.exists(),
        'agent_md_size': agent_md.stat().st_size if agent_md.exists() else 0,
    }

    # Calculate overall status
    if status['has_agent_md'] and status['has_memory']:
        status['status'] = 'Active'
    elif status['has_folder']:
        status['status'] = 'Partial'
    else:
        status['status'] = 'Missing'

    return status


def check_skill_status(expert: str) -> Dict:
    """Check skills associated with an expert."""
    skills = []
    prompt_count = 0

    for skill_dir in SKILLS_PATH.iterdir():
        if skill_dir.is_dir() and expert in skill_dir.name:
            skill_md = skill_dir / "SKILL.md"
            prompts_dir = skill_dir / "references" / "prompts"

            skill_info = {
                'name': skill_dir.name,
                'has_skill_md': skill_md.exists(),
                'prompt_count': len(list(prompts_dir.glob('*.md'))) if prompts_dir.exists() else 0,
            }

            skills.append(skill_info)
            prompt_count += skill_info['prompt_count']

    return {
        'skills': skills,
        'total_prompts': prompt_count,
    }


def check_extraction_status(expert: str) -> Dict:
    """Check extractions for an expert."""
    extractions = []

    for subdir in ['inbox', 'processed', 'reference']:
        extract_dir = EXTRACTIONS_PATH / subdir
        if extract_dir.exists():
            for file in extract_dir.glob('*.md'):
                # Check if expert name appears in filename (case-insensitive)
                if expert.replace('-', ' ').lower() in file.name.lower() or \
                   expert.replace('-', '').lower() in file.name.lower():
                    extractions.append({
                        'file': file.name,
                        'location': subdir,
                        'size': file.stat().st_size,
                    })

    return {
        'extractions': extractions,
        'count': len(extractions),
    }


def generate_report() -> Dict:
    """Generate full council report."""
    report = {
        'generated': datetime.now().isoformat(),
        'experts': {},
        'councils': {},
        'summary': {
            'total_experts': len(EXPERTS),
            'active_agents': 0,
            'total_prompts': 0,
            'total_extractions': 0,
        }
    }

    # Check each expert
    for expert, info in EXPERTS.items():
        agent_status = check_agent_status(expert)
        skill_status = check_skill_status(expert)
        extraction_status = check_extraction_status(expert)

        report['experts'][expert] = {
            'domain': info['domain'],
            'tier': info['tier'],
            'agent': agent_status,
            'skills': skill_status,
            'extractions': extraction_status,
        }

        if agent_status['status'] == 'Active':
            report['summary']['active_agents'] += 1
        report['summary']['total_prompts'] += skill_status['total_prompts']
        report['summary']['total_extractions'] += extraction_status['count']

    # Check councils
    for council, members in COUNCILS.items():
        active_members = sum(1 for m in members if report['experts'].get(m, {}).get('agent', {}).get('status') == 'Active')
        report['councils'][council] = {
            'members': members,
            'active_members': active_members,
            'total_members': len(members),
            'status': 'Full' if active_members == len(members) else 'Partial',
        }

    return report


def format_markdown_report(report: Dict) -> str:
    """Format report as markdown."""
    lines = [
        "# Expert Council Status Report",
        f"\n*Generated: {report['generated']}*\n",
        "---",
        "\n## Summary\n",
        f"- **Total Experts:** {report['summary']['total_experts']}",
        f"- **Active Agents:** {report['summary']['active_agents']}",
        f"- **Total Prompts:** {report['summary']['total_prompts']}",
        f"- **Total Extractions:** {report['summary']['total_extractions']}",
        "\n---",
        "\n## Expert Status\n",
        "| Expert | Domain | Agent | Prompts | Extractions |",
        "|--------|--------|-------|---------|-------------|",
    ]

    for expert, data in sorted(report['experts'].items()):
        status = "✅" if data['agent']['status'] == 'Active' else "⚠️" if data['agent']['status'] == 'Partial' else "❌"
        lines.append(f"| {expert} | {data['domain'][:30]} | {status} | {data['skills']['total_prompts']} | {data['extractions']['count']} |")

    lines.extend([
        "\n---",
        "\n## Council Status\n",
        "| Council | Members | Active | Status |",
        "|---------|---------|--------|--------|",
    ])

    for council, data in report['councils'].items():
        status = "✅" if data['status'] == 'Full' else "⚠️"
        lines.append(f"| {council} | {data['total_members']} | {data['active_members']} | {status} |")

    lines.extend([
        "\n---",
        "\n## Detailed Expert Breakdown\n",
    ])

    for expert, data in sorted(report['experts'].items()):
        lines.append(f"\n### {expert}")
        lines.append(f"- **Domain:** {data['domain']}")
        lines.append(f"- **Tier:** {data['tier']}")
        lines.append(f"- **Agent Status:** {data['agent']['status']}")

        if data['skills']['skills']:
            lines.append(f"- **Skills:** {', '.join(s['name'] for s in data['skills']['skills'])}")
            lines.append(f"- **Prompts:** {data['skills']['total_prompts']}")

        if data['extractions']['extractions']:
            lines.append(f"- **Extractions:** {data['extractions']['count']}")

    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description='Generate expert council status report')
    parser.add_argument('--output', '-o', help='Output file path')
    parser.add_argument('--json', '-j', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    print("📊 Generating council report...")
    report = generate_report()

    if args.json:
        output = json.dumps(report, indent=2)
    else:
        output = format_markdown_report(report)

    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)
        print(f"✅ Report saved to: {args.output}")
    else:
        print(output)

    # Print quick summary
    print(f"\n📈 Quick Summary:")
    print(f"   Active Agents: {report['summary']['active_agents']}/{report['summary']['total_experts']}")
    print(f"   Total Prompts: {report['summary']['total_prompts']}")
    print(f"   Total Extractions: {report['summary']['total_extractions']}")


if __name__ == '__main__':
    main()
