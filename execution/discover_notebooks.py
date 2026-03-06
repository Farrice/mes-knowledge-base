#!/usr/bin/env python3
"""
Auto-discover NotebookLM notebooks and register them.

Uses browser automation to:
1. Open NotebookLM home page
2. Scrape list of notebooks (names and IDs)
3. Auto-register in notebooks.md

Usage:
    python execution/discover_notebooks.py
    python execution/discover_notebooks.py --dry-run  # Show what would be added
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

# Paths
BASE_PATH = Path(__file__).parent.parent
NOTEBOOKS_MD = BASE_PATH / "mcp-servers" / "notebooklm" / "notebooks.md"
CHROME_PROFILE = BASE_PATH / "mcp-servers" / "notebooklm" / "chrome_profile_notebooklm"


def discover_notebooks_cli():
    """
    Discover notebooks using notebooklm-mcp CLI test command.

    The CLI may list available notebooks when testing connection.
    """
    print("Attempting to discover notebooks via notebooklm-mcp CLI...")

    try:
        # Try the test command which might list notebooks
        result = subprocess.run(
            ["uv", "run", "notebooklm-mcp", "test"],
            cwd=BASE_PATH / "mcp-servers" / "notebooklm",
            capture_output=True,
            text=True,
            timeout=30,
        )

        print(f"CLI output:\n{result.stdout}\n{result.stderr}")

        # Parse any notebook IDs from output
        notebook_ids = re.findall(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',
                                  result.stdout + result.stderr)

        if notebook_ids:
            print(f"\nFound {len(notebook_ids)} potential notebook IDs:")
            for nb_id in notebook_ids:
                print(f"  • {nb_id}")
            return notebook_ids
        else:
            print("No notebook IDs found in CLI output.")
            return []

    except Exception as e:
        print(f"CLI discovery failed: {e}")
        return []


def discover_notebooks_manual():
    """
    Manual discovery - open NotebookLM and guide user to get URLs.
    """
    print("\n" + "="*60)
    print("Manual Notebook Discovery")
    print("="*60)

    print("\nTo discover notebooks, please:")
    print("1. Open https://notebooklm.google.com in your browser")
    print("2. You'll see a list of all your notebooks")
    print("3. For each notebook:")
    print("   - Click on it")
    print("   - Copy the URL (https://notebooklm.google.com/notebook/XXXXXXXX)")
    print("   - Note the notebook name")

    print("\nThen run this script again with --add flag:")
    print("  python execution/discover_notebooks.py --add")

    return []


def read_current_notebooks():
    """Read currently registered notebooks from notebooks.md."""
    if not NOTEBOOKS_MD.exists():
        return {}

    content = NOTEBOOKS_MD.read_text()
    notebooks = {}

    # Parse markdown table
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("|") and "`" in line and line.count("|") >= 3:
            parts = [p.strip() for p in line.split("|")[1:-1]]
            if len(parts) >= 3 and parts[1].startswith("`"):
                name = parts[0].replace("**", "").strip()
                notebook_id = parts[1].strip("`").strip()
                purpose = parts[2].strip()

                if notebook_id and len(notebook_id) > 10:
                    notebooks[notebook_id] = {
                        "name": name,
                        "purpose": purpose,
                    }

    return notebooks


def add_notebook_interactive():
    """Interactive mode to add notebooks."""
    print("\n" + "="*60)
    print("Add Notebook")
    print("="*60)

    # Get URL
    url = input("\nNotebook URL: ").strip()

    # Extract ID
    match = re.search(r'notebook/([0-9a-f-]+)', url)
    if not match:
        print("❌ Invalid URL. Expected format: https://notebooklm.google.com/notebook/XXXXXXXX")
        return False

    notebook_id = match.group(1)

    # Get name
    name = input("Notebook name: ").strip()
    if not name:
        print("❌ Name is required")
        return False

    # Get purpose
    purpose = input("Purpose (brief description): ").strip()
    if not purpose:
        purpose = "NotebookLM research notebook"

    # Check if already registered
    current = read_current_notebooks()
    if notebook_id in current:
        print(f"\n⚠️  Notebook already registered as: {current[notebook_id]['name']}")
        overwrite = input("Overwrite? (y/n): ").strip().lower()
        if overwrite != 'y':
            return False

    # Add to registry
    add_to_registry(notebook_id, name, purpose)

    print(f"\n✓ Added: {name}")
    print(f"  ID: {notebook_id}")
    print(f"  Purpose: {purpose}")

    return True


def add_to_registry(notebook_id: str, name: str, purpose: str):
    """Add a notebook to the registry file."""
    content = NOTEBOOKS_MD.read_text()

    # Find the table section
    lines = content.splitlines()

    # Find where to insert (after last notebook entry, before "---")
    insert_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith("| **") and "`" in line:
            insert_idx = i + 1

    if insert_idx is None:
        print("❌ Could not find insertion point in notebooks.md")
        return False

    # Create new entry
    new_entry = f"| **{name}** | `{notebook_id}` | {purpose} |"

    # Insert
    lines.insert(insert_idx, new_entry)

    # Write back
    NOTEBOOKS_MD.write_text("\n".join(lines))

    return True


def list_notebooks():
    """List currently registered notebooks."""
    notebooks = read_current_notebooks()

    print("\n" + "="*60)
    print(f"Registered Notebooks ({len(notebooks)})")
    print("="*60)

    for nb_id, info in notebooks.items():
        print(f"\n• {info['name']}")
        print(f"  ID: {nb_id}")
        print(f"  Purpose: {info['purpose']}")


def main():
    parser = argparse.ArgumentParser(description="Discover and register NotebookLM notebooks")
    parser.add_argument("--add", action="store_true", help="Add a notebook interactively")
    parser.add_argument("--list", action="store_true", help="List registered notebooks")
    parser.add_argument("--discover", action="store_true", help="Attempt auto-discovery")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be added (with --discover)")

    args = parser.parse_args()

    if args.list:
        list_notebooks()
    elif args.add:
        while True:
            if not add_notebook_interactive():
                break
            another = input("\nAdd another? (y/n): ").strip().lower()
            if another != 'y':
                break
    elif args.discover:
        print("Auto-discovery is not yet fully implemented.")
        print("The notebooklm-mcp CLI doesn't expose a list command.\n")
        discover_notebooks_manual()
    else:
        # Default: show usage
        parser.print_help()
        print("\n" + "="*60)
        print("Quick Start")
        print("="*60)
        print("\n1. List current notebooks:")
        print("   python execution/discover_notebooks.py --list")
        print("\n2. Add a notebook:")
        print("   python execution/discover_notebooks.py --add")
        print("\n3. Attempt auto-discovery:")
        print("   python execution/discover_notebooks.py --discover")


if __name__ == "__main__":
    main()
