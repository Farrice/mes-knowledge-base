#!/usr/bin/env python3
"""
Search Experts - Search across all extractions and agents by keyword/domain.

Usage:
    python search_experts.py "keyword"
    python search_experts.py "keyword" --domain sales
    python search_experts.py "keyword" --files-only
    python search_experts.py "keyword" --context 3
"""

import os
import re
import argparse
from pathlib import Path
from typing import List, Dict, Tuple


# Base paths
BASE_PATH = Path(__file__).parent.parent
EXTRACTIONS_PATH = BASE_PATH / "knowledge" / "extractions"
AGENTS_PATH = BASE_PATH / "agents"
SKILLS_PATH = BASE_PATH / "skills"


def search_file(filepath: Path, keyword: str, context_lines: int = 2) -> List[Dict]:
    """Search a single file for keyword matches."""
    matches = []
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()

        pattern = re.compile(re.escape(keyword), re.IGNORECASE)

        for i, line in enumerate(lines):
            if pattern.search(line):
                # Get context lines
                start = max(0, i - context_lines)
                end = min(len(lines), i + context_lines + 1)
                context = ''.join(lines[start:end]).strip()

                matches.append({
                    'file': str(filepath.relative_to(BASE_PATH)),
                    'line_number': i + 1,
                    'line': line.strip(),
                    'context': context
                })
    except Exception as e:
        pass  # Skip files that can't be read

    return matches


def search_directory(directory: Path, keyword: str, context_lines: int = 2) -> List[Dict]:
    """Search all markdown files in a directory recursively."""
    all_matches = []

    if not directory.exists():
        return all_matches

    for filepath in directory.rglob('*.md'):
        matches = search_file(filepath, keyword, context_lines)
        all_matches.extend(matches)

    return all_matches


def filter_by_domain(matches: List[Dict], domain: str) -> List[Dict]:
    """Filter matches by domain keyword in filepath."""
    domain_lower = domain.lower()
    return [m for m in matches if domain_lower in m['file'].lower()]


def get_expert_mapping() -> Dict[str, str]:
    """Get mapping of expert names to their domains."""
    return {
        'jeremy-miner': 'sales, persuasion, NEPQ, objections',
        'michael-bernoff': 'identity, mindset, transformation',
        'harry-dry': 'copywriting, marketing, examples',
        'cardinal-mason': 'conversion, copywriting, direct response',
        'shaan-puri': 'storytelling, content, hooks, audience',
        'caleb-ralston': 'personal brand, differentiation, trust',
        'dai-media': 'consumer psychology, posture, personas',
        'mitch-albom': 'writing, storytelling, theme, emotion',
        'dan-wang': 'writing, observation, essays, long-form',
        'oscar-hoglund': 'sound, audio, emotion, storytelling',
        'futurepedia': 'prompts, AI, optimization, expert anchor',
        'nate-b-jones': 'AI agents, intent, JARVIS, architecture',
        'darrel-wilson': 'automation, workflows, monetization',
        'kittl': 'design, typography, visual, AI images',
        'erica-mallet': 'brand magnetism, beliefs, enemy effect',
        'seena-rez': 'TikTok, viral, hooks, commerce',
        'samuel-thompson': 'info products, launches, economics',
        'jim-oshaughnessy': 'philosophy, finance, synthesis',
        'lulu-cheng-meservey': 'communications, PR, narrative',
    }


def suggest_experts(keyword: str) -> List[str]:
    """Suggest relevant experts based on keyword."""
    suggestions = []
    keyword_lower = keyword.lower()

    for expert, domains in get_expert_mapping().items():
        if keyword_lower in domains.lower():
            suggestions.append(expert)

    return suggestions


def main():
    parser = argparse.ArgumentParser(description='Search across expert extractions and agents')
    parser.add_argument('keyword', help='Keyword to search for')
    parser.add_argument('--domain', '-d', help='Filter by domain (e.g., sales, writing, AI)')
    parser.add_argument('--files-only', '-f', action='store_true', help='Only show filenames, not content')
    parser.add_argument('--context', '-c', type=int, default=2, help='Number of context lines (default: 2)')
    parser.add_argument('--extractions', '-e', action='store_true', help='Search only extractions')
    parser.add_argument('--agents', '-a', action='store_true', help='Search only agents')
    parser.add_argument('--skills', '-s', action='store_true', help='Search only skills')

    args = parser.parse_args()

    # Determine which directories to search
    search_dirs = []
    if args.extractions or (not args.extractions and not args.agents and not args.skills):
        search_dirs.append(('Extractions', EXTRACTIONS_PATH))
    if args.agents or (not args.extractions and not args.agents and not args.skills):
        search_dirs.append(('Agents', AGENTS_PATH))
    if args.skills or (not args.extractions and not args.agents and not args.skills):
        search_dirs.append(('Skills', SKILLS_PATH))

    all_matches = []

    print(f"\n🔍 Searching for: '{args.keyword}'")
    print("=" * 60)

    # Search each directory
    for name, directory in search_dirs:
        matches = search_directory(directory, args.keyword, args.context)
        if args.domain:
            matches = filter_by_domain(matches, args.domain)
        all_matches.extend(matches)
        print(f"📁 {name}: {len(matches)} matches")

    print("=" * 60)
    print(f"📊 Total matches: {len(all_matches)}")

    # Suggest relevant experts
    suggestions = suggest_experts(args.keyword)
    if suggestions:
        print(f"\n💡 Suggested experts for '{args.keyword}':")
        for expert in suggestions:
            print(f"   @{expert}")

    # Display results
    if all_matches:
        print(f"\n📄 Results:\n")

        if args.files_only:
            # Group by file
            files = sorted(set(m['file'] for m in all_matches))
            for f in files:
                count = len([m for m in all_matches if m['file'] == f])
                print(f"  {f} ({count} matches)")
        else:
            # Show full results
            for i, match in enumerate(all_matches[:20], 1):  # Limit to 20
                print(f"--- Match {i} ---")
                print(f"File: {match['file']}")
                print(f"Line {match['line_number']}: {match['line'][:100]}...")
                if args.context > 0:
                    print(f"Context:\n{match['context'][:300]}...")
                print()

            if len(all_matches) > 20:
                print(f"... and {len(all_matches) - 20} more matches. Use --files-only for overview.")
    else:
        print("\n❌ No matches found.")


if __name__ == '__main__':
    main()
