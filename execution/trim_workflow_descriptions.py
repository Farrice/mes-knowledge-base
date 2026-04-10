#!/usr/bin/env python3
"""
Trim workflow descriptions to ≤8 words for context window efficiency.

Each workflow description appears in the system prompt. At 463 workflows,
every word saved across all files reduces context overhead substantially.

Usage:
    python3 execution/trim_workflow_descriptions.py --audit          # show stats only
    python3 execution/trim_workflow_descriptions.py --trim           # trim and show diff
    python3 execution/trim_workflow_descriptions.py --trim --apply   # trim and write
"""

import os
import re
import sys
import argparse
from pathlib import Path

WF_DIR = Path(".agent/workflows")
MAX_WORDS = 8

def parse_description(content):
    """Extract description from YAML frontmatter."""
    m = re.search(r'^description:\s*(.+)$', content, re.MULTILINE)
    if m:
        desc = m.group(1).strip().strip('"').strip("'")
        return desc
    return None

def smart_trim(desc, max_words=MAX_WORDS):
    """Intelligently shorten a description while preserving meaning."""
    words = desc.split()
    if len(words) <= max_words:
        return desc
    
    # Remove filler/connector words that don't add routing value
    filler = {'a', 'an', 'the', 'and', 'or', 'for', 'with', 'from', 'into',
              'that', 'which', 'using', 'via', 'through', 'any', 'all', 'your'}
    
    # First pass: remove fillers
    cleaned = [w for w in words if w.lower() not in filler]
    
    if len(cleaned) <= max_words:
        return ' '.join(cleaned)
    
    # Second pass: cut at natural break points
    # Look for em-dash, comma, or parenthetical
    text = desc
    for sep in [' — ', ' - ', ', ', ' (']:
        if sep in text:
            before = text.split(sep)[0]
            before_words = before.split()
            if 3 <= len(before_words) <= max_words:
                return before.strip()
    
    # Final fallback: take first max_words
    return ' '.join(words[:max_words])


def audit(wf_dir):
    """Audit all workflow descriptions and report stats."""
    files = sorted(f for f in os.listdir(wf_dir) if f.endswith('.md'))
    
    total_words = 0
    entries = []
    
    for f in files:
        path = wf_dir / f
        content = path.read_text()
        desc = parse_description(content)
        if desc:
            wc = len(desc.split())
            total_words += wc
            entries.append((f, desc, wc))
    
    print(f"Total workflows: {len(entries)}")
    print(f"Total description words: {total_words}")
    print(f"Average words/description: {total_words / len(entries):.1f}")
    print(f"Over {MAX_WORDS} words: {sum(1 for _, _, wc in entries if wc > MAX_WORDS)}")
    print(f"Estimated tokens from descriptions: ~{total_words * 1.3:.0f}")
    print()
    
    return entries


def trim(wf_dir, apply=False):
    """Trim descriptions and optionally apply changes."""
    files = sorted(f for f in os.listdir(wf_dir) if f.endswith('.md'))
    
    changes = []
    total_saved = 0
    
    for f in files:
        path = wf_dir / f
        content = path.read_text()
        desc = parse_description(content)
        if not desc:
            continue
        
        wc = len(desc.split())
        if wc <= MAX_WORDS:
            continue
        
        trimmed = smart_trim(desc)
        new_wc = len(trimmed.split())
        saved = wc - new_wc
        
        if saved > 0:
            changes.append((f, desc, trimmed, wc, new_wc, saved))
            total_saved += saved
            
            if apply:
                # Replace in file
                new_content = content.replace(
                    f'description: {desc}',
                    f'description: {trimmed}'
                ).replace(
                    f'description: "{desc}"',
                    f'description: {trimmed}'
                ).replace(
                    f"description: '{desc}'",
                    f'description: {trimmed}'
                )
                # Handle quoted descriptions
                old_patterns = [
                    f'description: {desc}',
                    f'description: "{desc}"',
                    f"description: '{desc}'"
                ]
                for pattern in old_patterns:
                    if pattern in content:
                        new_content = content.replace(pattern, f'description: {trimmed}')
                        break
                
                path.write_text(new_content)
    
    if changes:
        print(f"\n{'APPLIED' if apply else 'PROPOSED'} CHANGES ({len(changes)} files):")
        print("-" * 70)
        for f, old, new, old_wc, new_wc, saved in changes:
            print(f"  {f}")
            print(f"    OLD [{old_wc}w]: {old}")
            print(f"    NEW [{new_wc}w]: {new}")
            print()
        
        print(f"Total words saved: {total_saved}")
        print(f"Estimated tokens saved: ~{int(total_saved * 1.3)}")
    else:
        print("No changes needed — all descriptions are within limits.")
    
    return changes


def main():
    global MAX_WORDS
    parser = argparse.ArgumentParser(description="Trim workflow descriptions")
    parser.add_argument('--audit', action='store_true', help='Show stats only')
    parser.add_argument('--trim', action='store_true', help='Show proposed trims')
    parser.add_argument('--apply', action='store_true', help='Apply trims to files')
    parser.add_argument('--max-words', type=int, default=MAX_WORDS, help='Max words per description')
    args = parser.parse_args()
    
    MAX_WORDS = args.max_words
    
    if args.audit:
        audit(WF_DIR)
    elif args.trim:
        trim(WF_DIR, apply=args.apply)
    else:
        audit(WF_DIR)
        print("\nUse --trim to see proposed changes, --trim --apply to execute.")


if __name__ == '__main__':
    main()
