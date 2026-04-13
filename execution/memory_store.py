#!/usr/bin/env python3
"""
Sovereign Memory Store — Persistent cross-session memory with Ebbinghaus decay.

Three-tier memory architecture:
  Tier 1 (Episodic): Raw interaction records with timestamps
  Tier 2 (Semantic): Distilled patterns, preferences, and insights
  Tier 3 (Procedural): Operational configs and workflow patterns

All data stored in local SQLite (zero infrastructure). Upgradeable to
PostgreSQL + pgvector when scale demands it.

Usage:
    python3 execution/memory_store.py store --tier semantic --category preference --content "User prefers table output for comparisons"
    python3 execution/memory_store.py store --tier episodic --category decision --content "Chose PostgreSQL over Redis for memory" --meta '{"expert":"nate-b-jones","session":"abc123"}'
    python3 execution/memory_store.py recall --tier semantic --top 5
    python3 execution/memory_store.py search "context compression" --top 5
    python3 execution/memory_store.py decay                    # Run Ebbinghaus decay cycle
    python3 execution/memory_store.py pin <memory_id>          # Freeze decay
    python3 execution/memory_store.py boost <memory_id> 2.0    # Add freshness
    python3 execution/memory_store.py stats
    python3 execution/memory_store.py export --format json     # Sovereignty: full export
"""

import sys
import os
import json
import math
import sqlite3
import argparse
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path
from collections import Counter, defaultdict

# ─────────────────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────────────────

DB_DIR = Path(__file__).parent.parent / ".memory"
DB_PATH = DB_DIR / "sovereign.db"

# Freshness thresholds (Ebbinghaus-inspired)
FRESHNESS_ACTIVE = 3.0     # Actively served in context retrieval
FRESHNESS_DORMANT = 1.0    # Served only on direct query
FRESHNESS_ARCHIVE = 0.3    # Flagged for review
FRESHNESS_COLD = 0.1       # Moved to cold storage

# Decay rate constant (higher = faster decay)
DECAY_K = 0.1

# Initial freshness for new memories by tier
INITIAL_FRESHNESS = {
    "episodic": 5.0,
    "semantic": 7.0,
    "procedural": 9.0,   # Procedural memories decay slowest
}

# Valid categories by tier
VALID_CATEGORIES = {
    "episodic": ["message", "tool_call", "decision", "error", "milestone"],
    "semantic": ["preference", "pattern", "rule", "insight", "error_pattern"],
    "procedural": ["config", "workflow", "routing_rule", "template"],
}


# ─────────────────────────────────────────────────────────
# DATABASE SETUP
# ─────────────────────────────────────────────────────────

def get_db():
    """Get database connection, creating schema if needed."""
    DB_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")

    # Create tables
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS memories (
            id TEXT PRIMARY KEY,
            tier TEXT NOT NULL CHECK(tier IN ('episodic', 'semantic', 'procedural')),
            category TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TEXT NOT NULL,
            last_accessed TEXT NOT NULL,
            access_count INTEGER DEFAULT 1,
            freshness REAL NOT NULL,
            pinned INTEGER DEFAULT 0,
            metadata TEXT DEFAULT '{}',
            source_ids TEXT DEFAULT '[]'
        );

        CREATE INDEX IF NOT EXISTS idx_memories_tier ON memories(tier);
        CREATE INDEX IF NOT EXISTS idx_memories_freshness ON memories(freshness);
        CREATE INDEX IF NOT EXISTS idx_memories_category ON memories(category);
        CREATE INDEX IF NOT EXISTS idx_memories_created ON memories(created_at);
        CREATE INDEX IF NOT EXISTS idx_memories_accessed ON memories(last_accessed);
    """)
    conn.commit()
    return conn


# ─────────────────────────────────────────────────────────
# CORE OPERATIONS
# ─────────────────────────────────────────────────────────

def store_memory(tier, category, content, metadata=None, source_ids=None):
    """Store a new memory in the specified tier."""
    if tier not in VALID_CATEGORIES:
        print(f"Error: Invalid tier '{tier}'. Valid: {list(VALID_CATEGORIES.keys())}")
        return None

    if category not in VALID_CATEGORIES[tier]:
        print(f"Error: Invalid category '{category}' for tier '{tier}'.")
        print(f"Valid categories: {VALID_CATEGORIES[tier]}")
        return None

    conn = get_db()
    memory_id = str(uuid.uuid4())[:8]
    now = datetime.now(timezone.utc).isoformat()
    freshness = INITIAL_FRESHNESS[tier]

    conn.execute(
        """INSERT INTO memories (id, tier, category, content, created_at, last_accessed,
           access_count, freshness, pinned, metadata, source_ids)
           VALUES (?, ?, ?, ?, ?, ?, 1, ?, 0, ?, ?)""",
        (
            memory_id, tier, category, content, now, now,
            freshness,
            json.dumps(metadata or {}),
            json.dumps(source_ids or []),
        )
    )
    conn.commit()
    conn.close()

    print(f"Stored [{tier}/{category}] id={memory_id} freshness={freshness}")
    return memory_id


def recall_memories(tier=None, category=None, top_k=10, include_dormant=False):
    """Recall active memories, optionally filtered by tier/category."""
    conn = get_db()

    query = "SELECT * FROM memories WHERE 1=1"
    params = []

    if tier:
        query += " AND tier = ?"
        params.append(tier)

    if category:
        query += " AND category = ?"
        params.append(category)

    if not include_dormant:
        query += " AND freshness >= ?"
        params.append(FRESHNESS_DORMANT)

    query += " ORDER BY freshness DESC, last_accessed DESC LIMIT ?"
    params.append(top_k)

    rows = conn.execute(query, params).fetchall()

    # Touch accessed memories (spaced repetition reinforcement)
    now = datetime.now(timezone.utc).isoformat()
    for row in rows:
        conn.execute(
            "UPDATE memories SET last_accessed = ?, access_count = access_count + 1 WHERE id = ?",
            (now, row["id"])
        )
    conn.commit()
    conn.close()

    return [dict(r) for r in rows]


def search_memories(query_text, top_k=5, tier=None):
    """Search memories by content similarity (keyword-based for MVP)."""
    conn = get_db()

    sql = "SELECT * FROM memories WHERE freshness >= ?"
    params = [FRESHNESS_COLD]

    if tier:
        sql += " AND tier = ?"
        params.append(tier)

    rows = conn.execute(sql, params).fetchall()
    conn.close()

    if not rows:
        return []

    # Simple keyword scoring
    query_words = set(query_text.lower().split())
    scored = []

    for row in rows:
        content_lower = row["content"].lower()
        content_words = set(content_lower.split())

        # Exact substring bonus
        substring_score = sum(3 for w in query_words if w in content_lower and len(w) > 3)

        # Word overlap
        overlap = len(query_words & content_words)

        # Category/metadata bonus
        meta = json.loads(row["metadata"]) if row["metadata"] else {}
        meta_str = json.dumps(meta).lower()
        meta_bonus = sum(1 for w in query_words if w in meta_str)

        total_score = substring_score + overlap + meta_bonus

        # Weight by freshness
        total_score *= (0.5 + row["freshness"] / 10.0)

        if total_score > 0:
            scored.append((total_score, dict(row)))

    scored.sort(key=lambda x: -x[0])
    return scored[:top_k]


# ─────────────────────────────────────────────────────────
# EBBINGHAUS DECAY ENGINE
# ─────────────────────────────────────────────────────────

def calculate_freshness(base_value, days_since_access, k=DECAY_K):
    """
    Ebbinghaus-inspired decay: freshness drops logarithmically.
    Accessing a memory resets the clock (spaced repetition).
    """
    return base_value * (1 / (1 + k * days_since_access))


def run_decay_cycle():
    """Run decay across all non-pinned memories. Returns summary."""
    conn = get_db()
    now = datetime.now(timezone.utc)

    rows = conn.execute(
        "SELECT id, tier, freshness, last_accessed, pinned FROM memories WHERE pinned = 0"
    ).fetchall()

    changes = {"decayed": 0, "active": 0, "dormant": 0, "archive": 0, "cold": 0}

    for row in rows:
        last_accessed = datetime.fromisoformat(row["last_accessed"])
        if last_accessed.tzinfo is None:
            last_accessed = last_accessed.replace(tzinfo=timezone.utc)
        days_since = (now - last_accessed).total_seconds() / 86400

        new_freshness = calculate_freshness(row["freshness"], days_since)

        # Classify
        if new_freshness >= FRESHNESS_ACTIVE:
            changes["active"] += 1
        elif new_freshness >= FRESHNESS_DORMANT:
            changes["dormant"] += 1
        elif new_freshness >= FRESHNESS_ARCHIVE:
            changes["archive"] += 1
        else:
            changes["cold"] += 1

        if abs(new_freshness - row["freshness"]) > 0.01:
            conn.execute(
                "UPDATE memories SET freshness = ? WHERE id = ?",
                (round(new_freshness, 4), row["id"])
            )
            changes["decayed"] += 1

    conn.commit()
    conn.close()
    return changes


def pin_memory(memory_id):
    """Pin a memory — freeze decay, always active."""
    conn = get_db()
    result = conn.execute(
        "UPDATE memories SET pinned = 1 WHERE id = ?", (memory_id,)
    )
    conn.commit()
    if result.rowcount:
        print(f"Pinned memory {memory_id} — decay frozen.")
    else:
        print(f"Memory {memory_id} not found.")
    conn.close()


def boost_memory(memory_id, amount):
    """Boost a memory's freshness score."""
    conn = get_db()
    result = conn.execute(
        "UPDATE memories SET freshness = MIN(freshness + ?, 10.0) WHERE id = ?",
        (amount, memory_id)
    )
    conn.commit()
    if result.rowcount:
        row = conn.execute("SELECT freshness FROM memories WHERE id = ?", (memory_id,)).fetchone()
        print(f"Boosted memory {memory_id} by +{amount} → freshness: {row['freshness']:.2f}")
    else:
        print(f"Memory {memory_id} not found.")
    conn.close()


# ─────────────────────────────────────────────────────────
# SOVEREIGNTY — EXPORT / IMPORT
# ─────────────────────────────────────────────────────────

def export_memories(format_type="json"):
    """Export all memories for sovereignty/portability."""
    conn = get_db()
    rows = conn.execute("SELECT * FROM memories ORDER BY tier, created_at").fetchall()
    conn.close()

    memories = [dict(r) for r in rows]

    if format_type == "json":
        output = json.dumps({
            "exported_at": datetime.now(timezone.utc).isoformat(),
            "count": len(memories),
            "memories": memories,
        }, indent=2)
        print(output)
    elif format_type == "csv":
        import csv
        import io
        buf = io.StringIO()
        if memories:
            writer = csv.DictWriter(buf, fieldnames=memories[0].keys())
            writer.writeheader()
            writer.writerows(memories)
        print(buf.getvalue())


# ─────────────────────────────────────────────────────────
# DISPLAY & STATS
# ─────────────────────────────────────────────────────────

def freshness_label(f):
    """Human-readable freshness label."""
    if f >= FRESHNESS_ACTIVE:
        return f"🟢 active ({f:.1f})"
    elif f >= FRESHNESS_DORMANT:
        return f"🟡 dormant ({f:.1f})"
    elif f >= FRESHNESS_ARCHIVE:
        return f"🟠 archive ({f:.1f})"
    else:
        return f"🔴 cold ({f:.1f})"


def format_memory(mem, rank=None):
    """Format a single memory for display."""
    prefix = f"[{rank}] " if rank else ""
    pin = " 📌" if mem.get("pinned") else ""
    meta = json.loads(mem["metadata"]) if isinstance(mem["metadata"], str) else mem["metadata"]
    meta_str = ""
    if meta:
        meta_parts = [f"{k}={v}" for k, v in meta.items() if v]
        if meta_parts:
            meta_str = f"  Meta: {', '.join(meta_parts[:3])}"

    created = mem["created_at"][:10]
    accessed = mem["last_accessed"][:10]

    print(f"{prefix}[{mem['id']}] {mem['tier']}/{mem['category']}{pin}")
    print(f"  {freshness_label(mem['freshness'])}  accessed: {mem['access_count']}x  created: {created}  last: {accessed}")
    print(f"  {mem['content'][:150]}{'...' if len(mem['content']) > 150 else ''}")
    if meta_str:
        print(meta_str)
    print()


def show_stats():
    """Show memory store statistics."""
    conn = get_db()
    rows = conn.execute("SELECT * FROM memories").fetchall()
    conn.close()

    if not rows:
        print("Memory store is empty. Use 'store' to add memories.")
        return

    total = len(rows)
    by_tier = Counter(r["tier"] for r in rows)
    by_category = Counter(r["category"] for r in rows)
    by_status = Counter()

    for r in rows:
        f = r["freshness"]
        if f >= FRESHNESS_ACTIVE:
            by_status["active"] += 1
        elif f >= FRESHNESS_DORMANT:
            by_status["dormant"] += 1
        elif f >= FRESHNESS_ARCHIVE:
            by_status["archive"] += 1
        else:
            by_status["cold"] += 1

    pinned = sum(1 for r in rows if r["pinned"])
    avg_freshness = sum(r["freshness"] for r in rows) / total
    avg_access = sum(r["access_count"] for r in rows) / total

    print(f"Database: {DB_PATH}")
    print(f"Total memories: {total}")
    print(f"Pinned: {pinned}")
    print(f"Avg freshness: {avg_freshness:.2f}")
    print(f"Avg access count: {avg_access:.1f}")
    print()

    print("By tier:")
    for tier in ["episodic", "semantic", "procedural"]:
        print(f"  {tier:12s}  {by_tier.get(tier, 0):4d}")

    print("\nBy status:")
    for status in ["active", "dormant", "archive", "cold"]:
        icon = {"active": "🟢", "dormant": "🟡", "archive": "🟠", "cold": "🔴"}[status]
        print(f"  {icon} {status:10s}  {by_status.get(status, 0):4d}")

    print("\nBy category:")
    for cat, count in sorted(by_category.items(), key=lambda x: -x[1]):
        print(f"  {cat:20s}  {count:4d}")

    # Size on disk
    if DB_PATH.exists():
        size_kb = DB_PATH.stat().st_size / 1024
        print(f"\nDisk usage: {size_kb:.1f} KB")


# ─────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Sovereign Memory Store — Persistent cross-session memory")
    sub = parser.add_subparsers(dest="command")

    # store
    store_p = sub.add_parser("store", help="Store a new memory")
    store_p.add_argument("--tier", "-t", required=True, choices=["episodic", "semantic", "procedural"])
    store_p.add_argument("--category", "-c", required=True)
    store_p.add_argument("--content", required=True)
    store_p.add_argument("--meta", default="{}", help="JSON metadata")
    store_p.add_argument("--sources", default="[]", help="JSON array of source memory IDs")

    # recall
    recall_p = sub.add_parser("recall", help="Recall active memories")
    recall_p.add_argument("--tier", "-t", choices=["episodic", "semantic", "procedural"])
    recall_p.add_argument("--category", "-c")
    recall_p.add_argument("--top", "-n", type=int, default=10)
    recall_p.add_argument("--all", action="store_true", help="Include dormant/archived")

    # search
    search_p = sub.add_parser("search", help="Search memories by content")
    search_p.add_argument("query")
    search_p.add_argument("--top", "-n", type=int, default=5)
    search_p.add_argument("--tier", "-t", choices=["episodic", "semantic", "procedural"])

    # decay
    sub.add_parser("decay", help="Run Ebbinghaus decay cycle")

    # pin
    pin_p = sub.add_parser("pin", help="Pin a memory (freeze decay)")
    pin_p.add_argument("memory_id")

    # boost
    boost_p = sub.add_parser("boost", help="Boost a memory's freshness")
    boost_p.add_argument("memory_id")
    boost_p.add_argument("amount", type=float)

    # stats
    sub.add_parser("stats", help="Show memory statistics")

    # export
    export_p = sub.add_parser("export", help="Export all memories (sovereignty)")
    export_p.add_argument("--format", "-f", default="json", choices=["json", "csv"])

    args = parser.parse_args()

    if args.command == "store":
        meta = json.loads(args.meta) if args.meta else {}
        sources = json.loads(args.sources) if args.sources else []
        store_memory(args.tier, args.category, args.content, meta, sources)

    elif args.command == "recall":
        memories = recall_memories(
            tier=args.tier, category=args.category,
            top_k=args.top, include_dormant=args.all
        )
        if memories:
            print(f"Recalled {len(memories)} memories:\n")
            for i, m in enumerate(memories, 1):
                format_memory(m, rank=i)
        else:
            print("No active memories found.")

    elif args.command == "search":
        results = search_memories(args.query, top_k=args.top, tier=args.tier)
        if results:
            print(f"Search: \"{args.query}\" → {len(results)} results\n")
            for i, (score, mem) in enumerate(results, 1):
                print(f"  Score: {score:.2f}")
                format_memory(mem, rank=i)
        else:
            print(f"No memories match '{args.query}'")

    elif args.command == "decay":
        changes = run_decay_cycle()
        print("Decay cycle complete:")
        print(f"  Memories decayed:  {changes['decayed']}")
        print(f"  🟢 Active:         {changes['active']}")
        print(f"  🟡 Dormant:        {changes['dormant']}")
        print(f"  🟠 Archive:        {changes['archive']}")
        print(f"  🔴 Cold:           {changes['cold']}")

    elif args.command == "pin":
        pin_memory(args.memory_id)

    elif args.command == "boost":
        boost_memory(args.memory_id, args.amount)

    elif args.command == "stats":
        show_stats()

    elif args.command == "export":
        export_memories(format_type=args.format)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
