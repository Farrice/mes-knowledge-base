#!/usr/bin/env python3
"""
Session Workspace Manager
Creates, indexes, searches, and archives per-conversation session folders.

Usage:
    python execution/session_workspace.py create "Domain" "Label" [--conv-id ID]
    python execution/session_workspace.py list [--last N]
    python execution/session_workspace.py search "keyword"
    python execution/session_workspace.py archive --before YYYY-MM-DD
    python execution/session_workspace.py log-asset "/path/to/file" --type TYPE --desc "Description" [--session PATH]
    python execution/session_workspace.py finalize [--session PATH]
"""

import argparse
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# --- Configuration ---
PROJECT_ROOT = Path(__file__).resolve().parent.parent
SESSIONS_DIR = PROJECT_ROOT / "sessions"
SESSION_INDEX = SESSIONS_DIR / "SESSION_INDEX.md"
ARCHIVE_DIR = SESSIONS_DIR / "_archive"

SUBFOLDERS = ["assets", "drafts", "deliverables", "research"]

# --- Helpers ---

def slugify(text: str) -> str:
    """Convert text to a filesystem-safe slug."""
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')[:60]


def get_timestamp() -> tuple[str, str, str]:
    """Return (date_str, time_str, iso_str) in local time."""
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H-%M")
    iso_str = now.strftime("%Y-%m-%d %H:%M %Z").strip()
    return date_str, time_str, iso_str


def ensure_sessions_dir():
    """Create sessions/ and SESSION_INDEX.md if they don't exist."""
    SESSIONS_DIR.mkdir(parents=True, exist_ok=True)
    if not SESSION_INDEX.exists():
        SESSION_INDEX.write_text(
            "# Session Index\n\n"
            "> Master registry of all conversation workspaces. Auto-updated by `/session-kickoff`.\n\n"
            "| Date | Time | Domain | Label | Folder | Status |\n"
            "|------|------|--------|-------|--------|--------|\n"
        )


def find_latest_session() -> Path | None:
    """Find the most recently created session folder."""
    if not SESSIONS_DIR.exists():
        return None
    folders = sorted(
        [d for d in SESSIONS_DIR.iterdir() if d.is_dir() and not d.name.startswith(('_', '.'))],
        reverse=True
    )
    return folders[0] if folders else None


# --- Commands ---

def cmd_create(domain: str, label: str, conv_id: str = None):
    """Create a new session workspace folder."""
    ensure_sessions_dir()

    date_str, time_str, iso_str = get_timestamp()
    domain_slug = slugify(domain)
    label_slug = slugify(label)
    folder_name = f"{date_str}_{time_str}_{domain_slug}--{label_slug}"
    session_path = SESSIONS_DIR / folder_name

    # Handle collision (two sessions in the same minute)
    if session_path.exists():
        counter = 2
        while (SESSIONS_DIR / f"{folder_name}-{counter}").exists():
            counter += 1
        folder_name = f"{folder_name}-{counter}"
        session_path = SESSIONS_DIR / folder_name

    # Create folder structure
    session_path.mkdir(parents=True)
    for sub in SUBFOLDERS:
        (session_path / sub).mkdir()

    # Generate _manifest.md
    manifest_content = (
        f"# Session: {domain} — {label}\n"
        f"**Date**: {iso_str}\n"
    )
    if conv_id:
        manifest_content += f"**Conversation ID**: {conv_id}\n"
    manifest_content += (
        f"**Status**: 🟢 Active\n\n"
        f"## Assets Produced\n"
        f"| # | Type | Filename | Description |\n"
        f"|---|------|----------|-------------|\n\n"
        f"## Key Decisions\n"
        f"- *(auto-populated during session)*\n\n"
        f"## Related Sessions\n"
        f"- *(link related session folders here)*\n"
    )
    (session_path / "_manifest.md").write_text(manifest_content)

    # Update SESSION_INDEX.md
    rel_path = session_path.name
    index_line = f"| {date_str} | {time_str.replace('-', ':')} | {domain} | {label} | [{rel_path}](file:///{session_path}) | 🟢 Active |\n"
    with open(SESSION_INDEX, "a") as f:
        f.write(index_line)

    # Output for workflow consumption
    print(f"SESSION_PATH={session_path}")
    print(f"SESSION_FOLDER={folder_name}")
    print(f"✅ Created session workspace: {folder_name}/")
    print(f"   Subfolders: {', '.join(SUBFOLDERS)}")
    return session_path


def cmd_list(last_n: int = 10):
    """List recent session folders."""
    ensure_sessions_dir()

    folders = sorted(
        [d for d in SESSIONS_DIR.iterdir() if d.is_dir() and not d.name.startswith(('_', '.'))],
        reverse=True
    )

    if not folders:
        print("No sessions found.")
        return

    print(f"📋 Recent Sessions (showing {min(last_n, len(folders))} of {len(folders)}):\n")
    for folder in folders[:last_n]:
        # Parse folder name for display
        parts = folder.name.split('_', 2)
        if len(parts) >= 3:
            date_part = parts[0]
            time_part = parts[1]
            label_part = parts[2].replace('--', ' → ').replace('-', ' ')
        else:
            date_part = folder.name
            time_part = ""
            label_part = ""

        # Check status from manifest
        manifest = folder / "_manifest.md"
        status = "🟢"
        if manifest.exists():
            content = manifest.read_text()
            if "✅ Complete" in content:
                status = "✅"
            elif "📦 Archived" in content:
                status = "📦"

        # Count assets
        asset_count = sum(1 for sub in SUBFOLDERS for f in (folder / sub).glob("*") if f.is_file()) if all((folder / sub).exists() for sub in SUBFOLDERS) else 0

        print(f"  {status} {date_part} {time_part.replace('-', ':')}  {label_part}  ({asset_count} assets)")
        print(f"     └─ {folder.name}/")


def cmd_search(keyword: str):
    """Search sessions by keyword in folder name and manifest."""
    ensure_sessions_dir()
    keyword_lower = keyword.lower()
    results = []

    all_dirs = [d for d in SESSIONS_DIR.iterdir() if d.is_dir() and not d.name.startswith(('_', '.'))]
    # Also check archive
    if ARCHIVE_DIR.exists():
        for month_dir in ARCHIVE_DIR.iterdir():
            if month_dir.is_dir():
                all_dirs.extend(d for d in month_dir.iterdir() if d.is_dir())

    for folder in sorted(all_dirs, reverse=True):
        # Search folder name
        if keyword_lower in folder.name.lower():
            results.append((folder, "folder name"))
            continue

        # Search manifest content
        manifest = folder / "_manifest.md"
        if manifest.exists():
            content = manifest.read_text().lower()
            if keyword_lower in content:
                results.append((folder, "manifest"))

    if not results:
        print(f"🔍 No sessions found matching '{keyword}'")
        return

    print(f"🔍 Found {len(results)} session(s) matching '{keyword}':\n")
    for folder, match_location in results:
        label_part = folder.name.split('_', 2)[-1].replace('--', ' → ').replace('-', ' ') if '_' in folder.name else folder.name
        print(f"  📁 {label_part}")
        print(f"     └─ {folder}  (matched in {match_location})")


def cmd_log_asset(file_path: str, asset_type: str = "Asset", description: str = "", session_path: str = None):
    """Log an asset to a session's manifest."""
    if session_path:
        session = Path(session_path)
    else:
        session = find_latest_session()

    if not session or not session.exists():
        print("❌ No active session found. Run 'create' first.", file=sys.stderr)
        sys.exit(1)

    manifest = session / "_manifest.md"
    if not manifest.exists():
        print(f"❌ No _manifest.md in {session}", file=sys.stderr)
        sys.exit(1)

    # Count existing assets to get next number
    content = manifest.read_text()
    existing_rows = [line for line in content.split('\n') if line.startswith('|') and not line.startswith('| #') and not line.startswith('|---')]
    next_num = len(existing_rows) + 1

    filename = Path(file_path).name
    new_row = f"| {next_num} | {asset_type} | {filename} | {description} |"

    # Insert the row after the table header
    lines = content.split('\n')
    insert_idx = None
    for i, line in enumerate(lines):
        if line.startswith('|---|'):
            insert_idx = i + 1
            break

    if insert_idx is not None:
        lines.insert(insert_idx, new_row)
        manifest.write_text('\n'.join(lines))
        print(f"✅ Logged asset #{next_num}: {filename} ({asset_type})")
    else:
        print("❌ Could not find asset table in manifest", file=sys.stderr)
        sys.exit(1)


def cmd_finalize(session_path: str = None):
    """Mark a session as complete."""
    if session_path:
        session = Path(session_path)
    else:
        session = find_latest_session()

    if not session or not session.exists():
        print("❌ No active session found.", file=sys.stderr)
        sys.exit(1)

    # Update manifest status
    manifest = session / "_manifest.md"
    if manifest.exists():
        content = manifest.read_text()
        content = content.replace("🟢 Active", "✅ Complete")
        manifest.write_text(content)

    # Update SESSION_INDEX.md
    if SESSION_INDEX.exists():
        index_content = SESSION_INDEX.read_text()
        index_content = index_content.replace(
            f"| [{session.name}]",
            f"| [{session.name}]"
        ).replace(
            f"{session.name}) | 🟢 Active |",
            f"{session.name}) | ✅ Complete |"
        )
        SESSION_INDEX.write_text(index_content)

    print(f"✅ Session finalized: {session.name}")


def cmd_archive(before_date: str):
    """Archive sessions older than a given date."""
    ensure_sessions_dir()
    cutoff = datetime.strptime(before_date, "%Y-%m-%d")
    archived = 0

    for folder in sorted(SESSIONS_DIR.iterdir()):
        if not folder.is_dir() or folder.name.startswith(('_', '.')):
            continue

        # Parse date from folder name
        try:
            folder_date = datetime.strptime(folder.name[:10], "%Y-%m-%d")
        except ValueError:
            continue

        if folder_date >= cutoff:
            continue

        # Check if still active
        manifest = folder / "_manifest.md"
        if manifest.exists() and "🟢 Active" in manifest.read_text():
            print(f"  ⚠️  Skipping active session: {folder.name}")
            continue

        # Move to archive
        month_key = folder_date.strftime("%Y-%m")
        archive_month = ARCHIVE_DIR / month_key
        archive_month.mkdir(parents=True, exist_ok=True)

        dest = archive_month / folder.name
        folder.rename(dest)

        # Update manifest
        if (dest / "_manifest.md").exists():
            content = (dest / "_manifest.md").read_text()
            content = content.replace("✅ Complete", "📦 Archived")
            (dest / "_manifest.md").write_text(content)

        archived += 1
        print(f"  📦 Archived: {folder.name} → _archive/{month_key}/")

    # Update index
    if SESSION_INDEX.exists():
        index_content = SESSION_INDEX.read_text()
        # Note: archived sessions stay in the index but with updated status
        SESSION_INDEX.write_text(index_content.replace("✅ Complete |", "📦 Archived |"))

    print(f"\n📦 Archived {archived} session(s) older than {before_date}")


# --- CLI ---

def main():
    parser = argparse.ArgumentParser(description="Session Workspace Manager")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # create
    p_create = subparsers.add_parser("create", help="Create a new session workspace")
    p_create.add_argument("domain", help="Domain category (e.g., LinkedIn, System, Research)")
    p_create.add_argument("label", help="Short descriptive label")
    p_create.add_argument("--conv-id", help="Conversation ID", default=None)

    # list
    p_list = subparsers.add_parser("list", help="List recent sessions")
    p_list.add_argument("--last", type=int, default=10, help="Number of recent sessions")

    # search
    p_search = subparsers.add_parser("search", help="Search sessions by keyword")
    p_search.add_argument("keyword", help="Search term")

    # archive
    p_archive = subparsers.add_parser("archive", help="Archive old sessions")
    p_archive.add_argument("--before", required=True, help="Archive sessions before this date (YYYY-MM-DD)")

    # log-asset
    p_log = subparsers.add_parser("log-asset", help="Log an asset to the current session")
    p_log.add_argument("file_path", help="Path to the asset file")
    p_log.add_argument("--type", default="Asset", help="Asset type (e.g., Script, Deliverable, Research)")
    p_log.add_argument("--desc", default="", help="Description of the asset")
    p_log.add_argument("--session", default=None, help="Session folder path (defaults to latest)")

    # finalize
    p_final = subparsers.add_parser("finalize", help="Mark a session as complete")
    p_final.add_argument("--session", default=None, help="Session folder path (defaults to latest)")

    args = parser.parse_args()

    if args.command == "create":
        cmd_create(args.domain, args.label, args.conv_id)
    elif args.command == "list":
        cmd_list(args.last)
    elif args.command == "search":
        cmd_search(args.keyword)
    elif args.command == "archive":
        cmd_archive(args.before)
    elif args.command == "log-asset":
        cmd_log_asset(args.file_path, args.type, args.desc, args.session)
    elif args.command == "finalize":
        cmd_finalize(args.session)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
