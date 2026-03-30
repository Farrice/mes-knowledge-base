#!/usr/bin/env python3
"""
conversation_index.py — Scans all conversation directories in brain/ and builds
a searchable master index (JSON + Markdown).

Usage:
    python execution/conversation_index.py build          # Full rebuild
    python execution/conversation_index.py update <id>    # Update single conversation
    python execution/conversation_index.py stats          # Summary stats
"""

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BRAIN_DIR = Path.home() / ".gemini" / "antigravity" / "brain"
INDEX_DIR = BRAIN_DIR / "_index"
INDEX_JSON = INDEX_DIR / "conversations.json"
INDEX_MD = INDEX_DIR / "conversations.md"

# Directories to skip when scanning
SKIP_DIRS = {"_index", "tempmediaStorage"}

# Artifact filenames we care about
ARTIFACT_NAMES = [
    "task.md",
    "implementation_plan.md",
    "walkthrough.md",
]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _read_text(path: Path, max_chars: int = 0) -> str:
    """Read a text file, optionally truncating."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        if max_chars > 0:
            return text[:max_chars]
        return text
    except Exception:
        return ""


def _read_json(path: Path) -> dict:
    """Read a JSON file, returning empty dict on failure."""
    try:
        return json.loads(path.read_text(encoding="utf-8", errors="replace"))
    except Exception:
        return {}


def _extract_title_from_text(text: str) -> str:
    """Extract a likely title from markdown content (first H1 or first line)."""
    for line in text.split("\n"):
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
        if line and not line.startswith("---"):
            return line[:100]
    return ""


def _extract_domains(text: str) -> list:
    """Extract domain tags from content based on keyword matching."""
    domain_keywords = {
        "LinkedIn": ["linkedin", "profile", "engagement", "dwell time", "carousel"],
        "Ghostwriting": ["ghostwriting", "ghostwrite", "voice matching", "voice capture"],
        "Extraction": ["extraction", "extract", "skill.md", "genius.md", "completion engine"],
        "Strategy": ["strategy", "revenue", "monetization", "business model", "pricing"],
        "Content": ["content", "newsletter", "substack", "blog", "article", "post"],
        "System": ["system", "audit", "workflow", "protocol", "agent", "skill"],
        "Research": ["research", "perplexity", "deep research", "swarm"],
        "Copywriting": ["copy", "vsl", "headline", "hook", "cta", "ad script"],
        "SEO": ["seo", "keyword", "ranking", "search"],
        "Branding": ["brand", "positioning", "identity", "naming"],
        "Video": ["video", "youtube", "script", "thumbnail"],
        "Website": ["website", "landing page", "web", "html", "css"],
        "Offer Design": ["offer", "product", "pricing", "funnel"],
        "Client Acquisition": ["client", "outreach", "proposal", "freelance", "upwork"],
    }
    text_lower = text.lower()
    found = []
    for domain, keywords in domain_keywords.items():
        if any(kw in text_lower for kw in keywords):
            found.append(domain)
    return found[:5]  # cap at 5 domains


def _extract_experts(text: str) -> list:
    """Extract expert names mentioned in content."""
    known_experts = [
        "Lara Acosta", "Nicolas Cole", "Luke Iha", "Dan Koe", "Seth Godin",
        "Grace Andrews", "Kieran Flanagan", "Caleb Ralston", "Diandra Escobar",
        "Tom Noske", "Kallaway", "Oren", "Seena Rez", "Samuel Thompson",
        "Dan Martell", "David Placek", "Nick Saraev", "Nathan Gotch",
        "Joanna Wiebe", "Dai Media", "Ocean Vuong", "Eric Roth",
        "Steven Pressfield", "Michael Connelly", "Marc Andreessen",
        "Ben Horowitz", "Donald Miller", "Greg Hoffman", "Joscha Bach",
        "Cardinal Mason", "Harry Dry", "Darrel Wilson", "Shaan Puri",
        "Jeremy Haynes", "Jen Santulan",
    ]
    found = []
    for expert in known_experts:
        if expert.lower() in text.lower():
            found.append(expert)
    return found


def _extract_topics(text: str) -> list:
    """Extract key topics from content via simple keyword frequency."""
    # Remove markdown syntax
    clean = re.sub(r'[#*\-\[\]`>|]', ' ', text.lower())
    
    topic_signals = [
        "ghostwriting", "linkedin", "content strategy", "revenue",
        "extraction", "skill", "agent", "workflow", "offer", "funnel",
        "copywriting", "newsletter", "substack", "branding", "seo",
        "monetization", "client acquisition", "proof ladder", "hooks",
        "voice matching", "ai brain", "deep research", "parallel swarm",
        "carousel", "engagement", "profile optimization", "outreach",
        "case study", "testimonial", "mechanism", "vsl", "ad script",
        "quality gate", "system audit", "health check",
        "personal brand", "thought leadership", "coaching",
        "website", "landing page", "video", "youtube",
    ]
    
    found = []
    for topic in topic_signals:
        if topic in clean:
            found.append(topic)
    return found[:10]  # cap at 10


def _get_dir_date(conv_dir: Path) -> str:
    """Get the modification date of a conversation directory."""
    try:
        mtime = conv_dir.stat().st_mtime
        return datetime.fromtimestamp(mtime).isoformat()
    except Exception:
        return ""


def _infer_status(text: str) -> str:
    """Infer conversation status from task.md content."""
    if not text:
        return "unknown"
    
    lines = text.split("\n")
    has_incomplete = False
    has_complete = False
    for line in lines:
        if "[x]" in line.lower() or "[X]" in line:
            has_complete = True
        if "[ ]" in line or "[/]" in line:
            has_incomplete = True
    
    if has_complete and not has_incomplete:
        return "completed"
    elif has_incomplete:
        return "in-progress"
    elif has_complete:
        return "completed"
    return "unknown"


# ---------------------------------------------------------------------------
# Core indexing
# ---------------------------------------------------------------------------

def index_conversation(conv_id: str, conv_dir: Path ) -> dict:
    """Index a single conversation directory."""
    entry = {
        "id": conv_id,
        "title": "",
        "date": _get_dir_date(conv_dir),
        "domains": [],
        "experts": [],
        "artifacts": [],
        "topics": [],
        "status": "unknown",
    }
    
    all_text = ""
    
    # Read known artifacts
    for artifact_name in ARTIFACT_NAMES:
        artifact_path = conv_dir / artifact_name
        if artifact_path.exists():
            content = _read_text(artifact_path)
            meta_path = conv_dir / f"{artifact_name}.metadata.json"
            meta = _read_json(meta_path)
            
            summary = meta.get("Summary", "")
            if not summary:
                # Use first 200 chars of content as summary
                summary = content[:200].replace("\n", " ").strip()
            
            entry["artifacts"].append({
                "name": artifact_name,
                "summary": summary[:300],
                "path": str(artifact_path),
            })
            
            all_text += content + "\n"
    
    # Read any other .md files in the directory (non-resolved, non-metadata)
    for md_file in conv_dir.glob("*.md"):
        if md_file.name in ARTIFACT_NAMES:
            continue
        if ".resolved" in md_file.name or ".metadata" in md_file.name:
            continue
        content = _read_text(md_file, max_chars=1000)
        if content:
            entry["artifacts"].append({
                "name": md_file.name,
                "summary": content[:200].replace("\n", " ").strip(),
                "path": str(md_file),
            })
            all_text += content + "\n"
    
    # Read system-generated step outputs for topic extraction (first 500 chars each)
    steps_dir = conv_dir / ".system_generated" / "steps"
    if steps_dir.exists():
        for step_dir in sorted(steps_dir.iterdir()):
            output_file = step_dir / "output.txt"
            if output_file.exists():
                step_text = _read_text(output_file, max_chars=500)
                all_text += step_text + "\n"
    
    # Extract metadata from aggregated text
    if all_text:
        entry["title"] = _extract_title_from_text(all_text) or f"Conversation {conv_id[:8]}"
        entry["domains"] = _extract_domains(all_text)
        entry["experts"] = _extract_experts(all_text)
        entry["topics"] = _extract_topics(all_text)
    else:
        entry["title"] = f"Empty conversation {conv_id[:8]}"
    
    # Infer status from task.md
    task_path = conv_dir / "task.md"
    if task_path.exists():
        entry["status"] = _infer_status(_read_text(task_path))
    
    return entry


def build_full_index() -> list:
    """Scan all conversation directories and build the full index."""
    conversations = []
    
    for item in sorted(BRAIN_DIR.iterdir()):
        if not item.is_dir():
            continue
        if item.name in SKIP_DIRS:
            continue
        # Skip non-UUID directories
        if len(item.name) < 30:
            continue
        
        try:
            entry = index_conversation(item.name, item)
            conversations.append(entry)
        except Exception as e:
            print(f"  ⚠️  Error indexing {item.name}: {e}", file=sys.stderr)
    
    # Sort by date descending
    conversations.sort(key=lambda c: c.get("date", ""), reverse=True)
    return conversations


def update_single(conv_id: str, existing_index: list) -> list:
    """Update a single conversation in an existing index."""
    conv_dir = BRAIN_DIR / conv_id
    if not conv_dir.exists():
        print(f"❌ Conversation directory not found: {conv_id}")
        return existing_index
    
    entry = index_conversation(conv_id, conv_dir)
    
    # Replace or append
    updated = False
    for i, existing in enumerate(existing_index):
        if existing["id"] == conv_id:
            existing_index[i] = entry
            updated = True
            break
    
    if not updated:
        existing_index.append(entry)
    
    # Re-sort
    existing_index.sort(key=lambda c: c.get("date", ""), reverse=True)
    return existing_index


def load_index() -> list:
    """Load existing index from JSON file."""
    if INDEX_JSON.exists():
        try:
            return json.loads(INDEX_JSON.read_text())
        except Exception:
            return []
    return []


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def save_index(conversations: list):
    """Save index as JSON and Markdown."""
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    
    # Save JSON
    INDEX_JSON.write_text(
        json.dumps(conversations, indent=2, default=str),
        encoding="utf-8"
    )
    
    # Generate Markdown
    md_lines = [
        "# 📚 Conversation Index",
        "",
        f"*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*",
        f"*Total conversations: {len(conversations)}*",
        "",
        "---",
        "",
    ]
    
    # Group by domain
    domain_groups = {}
    for conv in conversations:
        primary_domain = conv["domains"][0] if conv["domains"] else "Uncategorized"
        domain_groups.setdefault(primary_domain, []).append(conv)
    
    # Sort domains alphabetically
    for domain in sorted(domain_groups.keys()):
        convs = domain_groups[domain]
        md_lines.append(f"## {domain} ({len(convs)})")
        md_lines.append("")
        
        for conv in convs:
            date_short = conv["date"][:10] if conv["date"] else "unknown"
            status_icon = {"completed": "✅", "in-progress": "🔄", "unknown": "⬜"}.get(conv["status"], "⬜")
            experts_str = ", ".join(conv["experts"][:3]) if conv["experts"] else ""
            
            md_lines.append(f"### {status_icon} {conv['title']}")
            md_lines.append(f"- **ID**: `{conv['id']}`")
            md_lines.append(f"- **Date**: {date_short}")
            if experts_str:
                md_lines.append(f"- **Experts**: {experts_str}")
            if conv["topics"]:
                md_lines.append(f"- **Topics**: {', '.join(conv['topics'][:5])}")
            
            if conv["artifacts"]:
                md_lines.append("- **Artifacts**:")
                for art in conv["artifacts"]:
                    md_lines.append(f"  - [{art['name']}]({art['path']})")
            
            md_lines.append("")
    
    INDEX_MD.write_text("\n".join(md_lines), encoding="utf-8")


def print_stats(conversations: list):
    """Print summary statistics."""
    total = len(conversations)
    completed = sum(1 for c in conversations if c["status"] == "completed")
    in_progress = sum(1 for c in conversations if c["status"] == "in-progress")
    with_artifacts = sum(1 for c in conversations if c["artifacts"])
    empty = sum(1 for c in conversations if not c["artifacts"])
    
    # Domain distribution
    domain_counts = {}
    for conv in conversations:
        for d in conv["domains"]:
            domain_counts[d] = domain_counts.get(d, 0) + 1
    
    # Expert distribution
    expert_counts = {}
    for conv in conversations:
        for e in conv["experts"]:
            expert_counts[e] = expert_counts.get(e, 0) + 1
    
    print("=" * 60)
    print("📊 CONVERSATION INDEX STATS")
    print("=" * 60)
    print(f"  Total conversations:    {total}")
    print(f"  ✅ Completed:           {completed}")
    print(f"  🔄 In progress:         {in_progress}")
    print(f"  📄 With artifacts:      {with_artifacts}")
    print(f"  ⬜ Empty:               {empty}")
    print()
    
    print("📂 TOP DOMAINS:")
    for domain, count in sorted(domain_counts.items(), key=lambda x: -x[1])[:10]:
        bar = "█" * min(count, 30)
        print(f"  {domain:20s} {count:3d}  {bar}")
    print()
    
    print("👤 TOP EXPERTS:")
    for expert, count in sorted(expert_counts.items(), key=lambda x: -x[1])[:10]:
        bar = "█" * min(count, 30)
        print(f"  {expert:20s} {count:3d}  {bar}")
    print()
    
    print(f"📁 Index location: {INDEX_DIR}")
    print("=" * 60)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == "build":
        print("🔨 Building full conversation index...")
        print(f"   Scanning: {BRAIN_DIR}")
        conversations = build_full_index()
        save_index(conversations)
        print(f"✅ Indexed {len(conversations)} conversations")
        print(f"   JSON: {INDEX_JSON}")
        print(f"   Markdown: {INDEX_MD}")
        print()
        print_stats(conversations)
    
    elif command == "update":
        if len(sys.argv) < 3:
            print("Usage: conversation_index.py update <conversation-id>")
            sys.exit(1)
        conv_id = sys.argv[2]
        print(f"🔄 Updating conversation: {conv_id}")
        existing = load_index()
        if not existing:
            print("   No existing index found, building full index first...")
            existing = build_full_index()
        updated = update_single(conv_id, existing)
        save_index(updated)
        print(f"✅ Updated. Total conversations: {len(updated)}")
    
    elif command == "stats":
        conversations = load_index()
        if not conversations:
            print("No index found. Run 'build' first.")
            sys.exit(1)
        print_stats(conversations)
    
    else:
        print(f"Unknown command: {command}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
