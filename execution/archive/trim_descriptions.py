#!/usr/bin/env python3
"""
Trim workflow description frontmatter to 8 words max.
Saves full backup before any modifications.

Usage:
    python3 execution/trim_descriptions.py --dry-run    # Report only, no writes
    python3 execution/trim_descriptions.py --execute    # Backup + trim + write
    python3 execution/trim_descriptions.py --rollback   # Restore all originals from backup
    python3 execution/trim_descriptions.py --verify     # Check all files have valid descriptions
"""

import os
import sys
import json
import re
import glob
import argparse
from pathlib import Path

WORKFLOWS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.agent', 'workflows')
BACKUP_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'description_backup.json')
MAX_WORDS = 8


def extract_description(filepath):
    """Extract description from YAML frontmatter."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Match YAML frontmatter
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return None, content
    
    frontmatter = match.group(1)
    desc_match = re.search(r'^description:\s*["\']?(.*?)["\']?\s*$', frontmatter, re.MULTILINE)
    if not desc_match:
        return None, content
    
    return desc_match.group(1).strip().strip('"').strip("'"), content


def write_description(filepath, original_content, new_desc):
    """Write new description back to file, preserving everything else."""
    # Match and replace the description line in frontmatter
    def replacer(match):
        frontmatter = match.group(1)
        # Replace the description line
        new_fm = re.sub(
            r'^description:\s*.*$',
            f'description: {new_desc}',
            frontmatter,
            flags=re.MULTILINE
        )
        return f'---\n{new_fm}\n---'
    
    new_content = re.sub(r'^---\s*\n(.*?)\n---', replacer, original_content, count=1, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)


def smart_trim(description, max_words=MAX_WORDS):
    """
    Intelligently trim a description to max_words while preserving meaning.
    
    Strategy:
    1. Strip attribution clauses ("using X's framework", "via Y methodology")
    2. Strip elaboration after em-dash if core meaning is before it
    3. Strip platform lists
    4. Strip "fully operationalized", "end-to-end", etc.
    5. Keep verb + core action + target
    6. NEVER return empty — fall back to first max_words of original
    """
    if not description:
        return description
    
    original = description.strip()
    text = original
    
    # Already short enough
    if len(text.split()) <= max_words:
        return text
    
    # Remove common filler patterns (safe — these are always trailing)
    patterns_to_strip = [
        r"\s*—\s*fully operationalized\.?",
        r"\s*fully operationalized\.?",
        r"\s*using\s+\w+(?:'s)?\s+methodology\.?$",
        r"\s*using\s+\w+(?:'s)?\s+framework\.?$",
        r"\s*using\s+\w+(?:'s)?\s+\w+\s+methodology\.?$",
        r"\s*using\s+\w+\s+\w+(?:'s)?\s+methodology\.?$",
        r"\s*Enforces a mandatory.*$",
        r"\s*Feeds directly into.*$",
    ]
    
    for pattern in patterns_to_strip:
        text = re.sub(pattern, '', text, flags=re.IGNORECASE)
    
    # Only strip "Includes/Outputs/Produces" if they start a NEW sentence (after period or at sentence boundary)
    text = re.sub(r'\.\s+(?:Includes?|Outputs?|Produces?)\s+.*$', '', text, flags=re.IGNORECASE)
    
    # Strip parenthetical platform lists
    text = re.sub(r'\s*\([^)]*\)\s*', ' ', text)
    
    # Normalize whitespace after stripping
    text = ' '.join(text.split())
    
    # If there's an em-dash, try keeping just the part before it
    if ' — ' in text:
        parts = text.split(' — ', 1)
        before = parts[0].strip()
        after = parts[1].strip()
        before_len = len(before.split())
        after_len = len(after.split())
        # If the part before the dash is short enough and meaningful, use it
        if 2 <= before_len <= max_words:
            text = before
        # If after-dash is just a short label (≤4 words), prefer truncating before-dash
        # to preserve the action verb (e.g. "Generate the single most important..." > "the StoryBrand one-liner")
        elif after_len <= 4:
            text = before  # will be truncated below
        # If the part after is more descriptive, try that
        elif 2 <= after_len <= max_words:
            text = after
        else:
            # Take the shorter one and we'll truncate below
            text = before if before_len <= after_len else after
    
    # Strip trailing preposition phrases if still too long
    while len(text.split()) > max_words:
        shortened = re.sub(r'\s+(?:with|for|from|via|across|through|using|into|between|after|before|during)\s+.*$', '', text, count=1)
        if shortened != text and len(shortened.split()) >= 3:
            text = shortened
        else:
            break
    
    # Final truncation if still over limit
    words = text.split()
    if len(words) > max_words:
        text = ' '.join(words[:max_words])
        # Clean up trailing articles/prepositions
        text = re.sub(r'\s+(?:a|an|the|and|or|to|for|with|in|on|at|by|of)\s*$', '', text, flags=re.IGNORECASE)
    
    # Clean up trailing punctuation artifacts
    text = text.strip().rstrip('.,;:—–-')
    text = text.strip()
    
    # SAFETY: Never return empty — fall back to first max_words of original
    if not text or len(text) < 3:
        fallback_words = original.split()[:max_words]
        text = ' '.join(fallback_words).rstrip('.,;:—–-').strip()
    
    return text


def backup_descriptions(workflows):
    """Save all original descriptions to backup file."""
    backup = {}
    for filepath in workflows:
        desc, _ = extract_description(filepath)
        if desc is not None:
            basename = os.path.basename(filepath)
            backup[basename] = desc
    
    with open(BACKUP_FILE, 'w', encoding='utf-8') as f:
        json.dump(backup, f, indent=2)
    
    return backup


def dry_run(workflows):
    """Report what would be changed without modifying files."""
    total_before = 0
    total_after = 0
    changes = []
    unchanged = []
    
    for filepath in sorted(workflows):
        desc, _ = extract_description(filepath)
        if desc is None:
            continue
        
        basename = os.path.basename(filepath).replace('.md', '')
        trimmed = smart_trim(desc)
        before_words = len(desc.split())
        after_words = len(trimmed.split())
        total_before += before_words
        total_after += after_words
        
        if trimmed != desc:
            changes.append({
                'file': basename,
                'before': desc,
                'after': trimmed,
                'saved': before_words - after_words
            })
        else:
            unchanged.append(basename)
    
    # Print report
    print("=" * 80)
    print("SLASH COMMAND DESCRIPTION TRIMMING — DRY RUN REPORT")
    print("=" * 80)
    print(f"\nTotal workflows: {len(workflows)}")
    print(f"Would change: {len(changes)}")
    print(f"Already optimal: {len(unchanged)}")
    print(f"\nTotal words before: {total_before} (~{total_before * 4 // 3} tokens)")
    print(f"Total words after:  {total_after} (~{total_after * 4 // 3} tokens)")
    print(f"Savings: {total_before - total_after} words (~{(total_before - total_after) * 4 // 3} tokens per message)")
    print(f"Reduction: {((total_before - total_after) / total_before * 100):.1f}%")
    
    print(f"\n{'─' * 80}")
    print("CHANGES (showing top 30 by words saved):")
    print(f"{'─' * 80}")
    
    for c in sorted(changes, key=lambda x: x['saved'], reverse=True)[:30]:
        print(f"\n/{c['file']}  (-{c['saved']} words)")
        print(f"  BEFORE: {c['before']}")
        print(f"  AFTER:  {c['after']}")
    
    if len(changes) > 30:
        print(f"\n... and {len(changes) - 30} more changes")
    
    return changes


def execute(workflows):
    """Backup, trim, and write all descriptions."""
    # Step 1: Backup
    print("Step 1: Backing up all descriptions...")
    backup = backup_descriptions(workflows)
    print(f"  Backed up {len(backup)} descriptions to {BACKUP_FILE}")
    
    # Step 2: Trim and write
    print("\nStep 2: Trimming descriptions...")
    changed = 0
    errors = []
    
    for filepath in sorted(workflows):
        desc, content = extract_description(filepath)
        if desc is None:
            continue
        
        trimmed = smart_trim(desc)
        if trimmed != desc:
            try:
                write_description(filepath, content, trimmed)
                changed += 1
            except Exception as e:
                errors.append((filepath, str(e)))
    
    print(f"  Modified {changed} files")
    if errors:
        print(f"  ERRORS ({len(errors)}):")
        for fp, err in errors:
            print(f"    {fp}: {err}")
    
    print("\nDone. Run with --verify to check results.")


def rollback():
    """Restore all descriptions from backup."""
    if not os.path.exists(BACKUP_FILE):
        print("ERROR: No backup file found at", BACKUP_FILE)
        sys.exit(1)
    
    with open(BACKUP_FILE, 'r', encoding='utf-8') as f:
        backup = json.load(f)
    
    restored = 0
    for basename, original_desc in backup.items():
        filepath = os.path.join(WORKFLOWS_DIR, basename)
        if not os.path.exists(filepath):
            print(f"  SKIP (file missing): {basename}")
            continue
        
        _, content = extract_description(filepath)
        write_description(filepath, content, f'"{original_desc}"' if "'" in original_desc else original_desc)
        restored += 1
    
    print(f"Restored {restored} descriptions from backup.")


def verify(workflows):
    """Verify all files have valid descriptions."""
    valid = 0
    empty = 0
    missing = 0
    over_limit = 0
    
    for filepath in sorted(workflows):
        desc, _ = extract_description(filepath)
        basename = os.path.basename(filepath).replace('.md', '')
        
        if desc is None:
            missing += 1
            print(f"  MISSING FRONTMATTER: /{basename}")
        elif desc.strip() == '':
            empty += 1
            print(f"  EMPTY DESCRIPTION: /{basename}")
        elif len(desc.split()) > MAX_WORDS:
            over_limit += 1
            print(f"  OVER LIMIT ({len(desc.split())}w): /{basename} — {desc}")
        else:
            valid += 1
    
    print(f"\n{'─' * 40}")
    print(f"Valid (≤{MAX_WORDS} words): {valid}")
    print(f"Over limit: {over_limit}")
    print(f"Empty: {empty}")
    print(f"Missing frontmatter: {missing}")
    print(f"Total: {len(workflows)}")


def main():
    parser = argparse.ArgumentParser(description='Trim workflow descriptions for token efficiency')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--dry-run', action='store_true', help='Report changes without modifying files')
    group.add_argument('--execute', action='store_true', help='Backup, trim, and write')
    group.add_argument('--rollback', action='store_true', help='Restore from backup')
    group.add_argument('--verify', action='store_true', help='Check all files')
    
    args = parser.parse_args()
    
    if args.rollback:
        rollback()
        return
    
    workflows = sorted(glob.glob(os.path.join(WORKFLOWS_DIR, '*.md')))
    print(f"Found {len(workflows)} workflow files in {WORKFLOWS_DIR}\n")
    
    if args.dry_run:
        dry_run(workflows)
    elif args.execute:
        execute(workflows)
    elif args.verify:
        verify(workflows)


if __name__ == '__main__':
    main()
