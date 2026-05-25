#!/usr/bin/env python3
"""
Memory Ops — Backup, Restore, Mirror Freshness for the sovereign memory store.

Sprint 0 of the Antigravity memory architecture: operational hygiene before
features. Without backup + restore + staleness detection, more memory features
amplify the silent-failure surface area.

Commands:
    python3 execution/memory_ops.py backup              # gzipped backup, retain 14
    python3 execution/memory_ops.py backup --dest /path # custom destination
    python3 execution/memory_ops.py restore <path.gz>   # restore drill (--force to overwrite)
    python3 execution/memory_ops.py restore --dry-run <path.gz>  # integrity-check only
    python3 execution/memory_ops.py restore --target /tmp/test.db <path.gz>  # restore to alternate path
    python3 execution/memory_ops.py check-mirror        # staleness across mirror sources
    python3 execution/memory_ops.py check-mirror --json # machine-readable
    python3 execution/memory_ops.py prune-backups       # enforce retention manually

Exit codes:
    0 = OK
    1 = error
    2 = backup OK but pruning failed (non-fatal)
    3 = mirror staleness exceeds threshold (HALT signal — only with --strict)
"""
from __future__ import annotations

import argparse
import gzip
import json
import os
import shutil
import sqlite3
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# ─────────────────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = REPO_ROOT / ".memory" / "sovereign.db"
BACKUP_DIR = REPO_ROOT / ".memory" / "backups"
EVENTS_DIR = REPO_ROOT / ".memory" / "events"
LOG_FILE = BACKUP_DIR / "launchd.log"

# Mirror sources.
# Each source has:
#   kind: "file_mtime" → freshness from filesystem mtime of `path`
#         "sqlite_max" → freshness from MAX(<column>) in a sqlite table
#   blocking: True  → check_mirror_freshness().halt fires if this source is stale
#             False → contributes only to warn (sovereign.db is not a true mirror)
# Recall mirror is intentionally absent — see directives/recall-mirror-deferred.md
MIRROR_SOURCES: Dict[str, Dict[str, Any]] = {
    "sovereign_db": {
        "kind": "file_mtime",
        "path": DB_PATH,
        "blocking": False,
    },
    "notion_mirror": {
        "kind": "sqlite_max",
        "db_path": DB_PATH,
        "query": "SELECT MAX(mirrored_at) FROM notion_mirror",
        "blocking": True,
    },
}

# Staleness thresholds (hours)
STALE_WARN_HOURS = 36
STALE_HALT_HOURS = 72

# Retention
BACKUP_RETAIN_COUNT = 14


# ─────────────────────────────────────────────────────────
# BACKUP
# ─────────────────────────────────────────────────────────

def backup_db(dest_dir: Optional[Path] = None) -> Tuple[Path, int]:
    """Online SQLite backup → gzipped file. Returns (backup_path, bytes_written).

    Uses sqlite3 backup API which is lock-safe (does not block readers/writers).
    Verifies integrity_check on the backup before declaring success.
    """
    dest = Path(dest_dir) if dest_dir else BACKUP_DIR
    dest.mkdir(parents=True, exist_ok=True)

    if not DB_PATH.exists():
        raise RuntimeError(f"Source DB does not exist: {DB_PATH}")

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    raw_backup = dest / f"sovereign_{ts}.db"
    gz_backup = dest / f"sovereign_{ts}.db.gz"

    # Step 1: online backup via SQLite backup API
    src = sqlite3.connect(str(DB_PATH))
    dst = sqlite3.connect(str(raw_backup))
    try:
        src.backup(dst)
    finally:
        dst.close()
        src.close()

    # Step 2: integrity check on the backup
    check = sqlite3.connect(str(raw_backup))
    try:
        result = check.execute("PRAGMA integrity_check").fetchone()
        if not result or result[0] != "ok":
            raw_backup.unlink(missing_ok=True)
            raise RuntimeError(f"Backup failed integrity check: {result}")
        # Smoke test: count memories
        count = check.execute("SELECT count(*) FROM memories").fetchone()[0]
    finally:
        check.close()

    # Step 3: gzip
    with open(raw_backup, "rb") as f_in:
        with gzip.open(gz_backup, "wb", compresslevel=6) as f_out:
            shutil.copyfileobj(f_in, f_out)
    raw_backup.unlink()

    bytes_written = gz_backup.stat().st_size
    _log(f"backup OK: {gz_backup.name} ({bytes_written:,} bytes, {count} memories)")
    return gz_backup, bytes_written


def prune_backups(retain: int = BACKUP_RETAIN_COUNT) -> int:
    """Keep the most recent `retain` backups; delete the rest. Returns count deleted."""
    if not BACKUP_DIR.exists():
        return 0
    backups = sorted(BACKUP_DIR.glob("sovereign_*.db.gz"), key=lambda p: p.stat().st_mtime)
    if len(backups) <= retain:
        return 0
    to_delete = backups[: len(backups) - retain]
    for p in to_delete:
        p.unlink()
        _log(f"prune: removed {p.name}")
    return len(to_delete)


# ─────────────────────────────────────────────────────────
# RESTORE
# ─────────────────────────────────────────────────────────

def restore_db(backup_path: Path, target: Optional[Path] = None, force: bool = False,
               dry_run: bool = False) -> Dict[str, Any]:
    """Restore a gzipped backup. Atomic swap only after integrity + smoke pass.

    Returns dict with restore stats. Raises on any failure.
    """
    backup_path = Path(backup_path).resolve()
    target_path = Path(target).resolve() if target else DB_PATH

    if not backup_path.exists():
        raise RuntimeError(f"Backup not found: {backup_path}")
    if target_path.exists() and not force and not dry_run:
        raise RuntimeError(f"Target exists: {target_path} (use --force to overwrite)")

    # Step 1: gunzip to temp
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as tmp:
        tmp_path = Path(tmp.name)
    try:
        with gzip.open(backup_path, "rb") as f_in:
            with open(tmp_path, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)

        # Step 2: integrity check
        check = sqlite3.connect(str(tmp_path))
        try:
            integrity = check.execute("PRAGMA integrity_check").fetchone()
            if not integrity or integrity[0] != "ok":
                raise RuntimeError(f"Backup integrity check failed: {integrity}")
            # Step 3: smoke test
            count = check.execute("SELECT count(*) FROM memories").fetchone()[0]
            tier_counts = dict(check.execute(
                "SELECT tier, count(*) FROM memories GROUP BY tier"
            ).fetchall())
        finally:
            check.close()

        stats = {
            "backup_path": str(backup_path),
            "target_path": str(target_path),
            "memory_count": count,
            "tier_counts": tier_counts,
            "integrity": "ok",
            "dry_run": dry_run,
        }

        if dry_run:
            stats["restored"] = False
            return stats

        # Step 4: atomic swap
        if target_path.exists():
            backup_of_target = target_path.with_suffix(target_path.suffix + ".pre-restore")
            shutil.move(str(target_path), str(backup_of_target))
            stats["overwrote_existing"] = True
            stats["pre_restore_backup"] = str(backup_of_target)
        target_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(tmp_path), str(target_path))
        stats["restored"] = True
        _log(f"restore OK: {backup_path.name} → {target_path} ({count} memories)")
        return stats
    finally:
        if tmp_path.exists():
            tmp_path.unlink(missing_ok=True)


# ─────────────────────────────────────────────────────────
# MIRROR FRESHNESS
# ─────────────────────────────────────────────────────────

def _source_age(source: Dict[str, Any]) -> Tuple[Optional[float], Optional[datetime], Optional[str]]:
    """Returns (age_hours, last_modified_dt, error_or_none)."""
    now = datetime.now(timezone.utc)
    kind = source.get("kind", "file_mtime")

    if kind == "file_mtime":
        path: Path = source["path"]
        if not path.exists():
            return None, None, "missing"
        mtime = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
        age_hours = (now - mtime).total_seconds() / 3600.0
        return age_hours, mtime, None

    if kind == "sqlite_max":
        db_path: Path = source["db_path"]
        if not db_path.exists():
            return None, None, "missing"
        try:
            conn = sqlite3.connect(str(db_path))
            row = conn.execute(source["query"]).fetchone()
            conn.close()
        except sqlite3.OperationalError as e:
            return None, None, f"query failed: {e}"
        if not row or not row[0]:
            return None, None, "empty"
        try:
            # ISO 8601 — handles both naive and tz-aware timestamps
            ts_str = row[0]
            if ts_str.endswith("Z"):
                ts_str = ts_str[:-1] + "+00:00"
            mtime = datetime.fromisoformat(ts_str)
            if mtime.tzinfo is None:
                mtime = mtime.replace(tzinfo=timezone.utc)
        except (ValueError, TypeError) as e:
            return None, None, f"unparseable timestamp: {e}"
        age_hours = (now - mtime).total_seconds() / 3600.0
        return age_hours, mtime, None

    return None, None, f"unknown kind: {kind}"


def check_mirror_freshness() -> Dict[str, Any]:
    """Report staleness across mirror sources. Returns dict with per-source ages.

    `warn`           → any source past WARN threshold (advisory)
    `halt`           → any source past HALT threshold
    `blocking_halt`  → any **blocking** source past HALT threshold (production gate)
    """
    now = datetime.now(timezone.utc)
    report: Dict[str, Any] = {
        "checked_at": now.isoformat(),
        "sources": {},
        "max_age_hours": 0.0,
        "warn": False,
        "halt": False,
        "blocking_halt": False,
        "stale_blocking_sources": [],
    }
    max_age = 0.0
    for name, source in MIRROR_SOURCES.items():
        blocking = bool(source.get("blocking"))
        age_hours, mtime, err = _source_age(source)

        if err is not None:
            entry = {
                "exists": False,
                "age_hours": None,
                "status": err,
                "blocking": blocking,
            }
            # An empty or missing BLOCKING mirror is treated as max-stale to fail safe
            if blocking:
                report["blocking_halt"] = True
                report["stale_blocking_sources"].append(name)
            report["sources"][name] = entry
            continue

        max_age = max(max_age, age_hours)
        if age_hours > STALE_HALT_HOURS:
            status = "halt"
            if blocking:
                report["blocking_halt"] = True
                report["stale_blocking_sources"].append(name)
        elif age_hours > STALE_WARN_HOURS:
            status = "warn"
        else:
            status = "ok"
        report["sources"][name] = {
            "exists": True,
            "age_hours": round(age_hours, 2),
            "last_modified": mtime.isoformat() if mtime else None,
            "status": status,
            "blocking": blocking,
        }
    report["max_age_hours"] = round(max_age, 2)
    report["warn"] = max_age > STALE_WARN_HOURS
    report["halt"] = max_age > STALE_HALT_HOURS
    return report


# ─────────────────────────────────────────────────────────
# UTILITIES
# ─────────────────────────────────────────────────────────

def _log(msg: str) -> None:
    """Append to launchd log + print to stderr."""
    try:
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        ts = datetime.now().isoformat(timespec="seconds")
        with open(LOG_FILE, "a") as f:
            f.write(f"[{ts}] {msg}\n")
    except Exception:
        pass
    print(msg, file=sys.stderr)


def ensure_dirs() -> None:
    """Create .memory/{backups,events} directories if missing."""
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    EVENTS_DIR.mkdir(parents=True, exist_ok=True)


# ─────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(description="Memory Ops — backup, restore, staleness checks")
    sub = parser.add_subparsers(dest="command")

    backup_p = sub.add_parser("backup", help="Create gzipped backup of sovereign.db")
    backup_p.add_argument("--dest", help="Destination directory (default: .memory/backups)")
    backup_p.add_argument("--no-prune", action="store_true", help="Skip retention pruning")

    restore_p = sub.add_parser("restore", help="Restore from backup")
    restore_p.add_argument("backup_path", help="Path to .db.gz backup file")
    restore_p.add_argument("--target", help="Target DB path (default: .memory/sovereign.db)")
    restore_p.add_argument("--force", action="store_true", help="Overwrite existing target")
    restore_p.add_argument("--dry-run", action="store_true", help="Integrity check only")

    check_p = sub.add_parser("check-mirror", help="Report mirror source staleness")
    check_p.add_argument("--json", action="store_true", help="Machine-readable output")
    check_p.add_argument("--strict", action="store_true", help="Exit 3 if any source exceeds HALT threshold")

    sub.add_parser("prune-backups", help="Enforce backup retention (keep last N)")
    sub.add_parser("ensure-dirs", help="Create .memory/{backups,events} directories")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    try:
        if args.command == "backup":
            ensure_dirs()
            path, size = backup_db(dest_dir=Path(args.dest) if args.dest else None)
            print(f"Backup: {path}")
            print(f"Size:   {size:,} bytes")
            if not args.no_prune:
                deleted = prune_backups()
                if deleted:
                    print(f"Pruned: {deleted} old backup(s)")
            return 0

        elif args.command == "restore":
            stats = restore_db(
                backup_path=Path(args.backup_path),
                target=Path(args.target) if args.target else None,
                force=args.force,
                dry_run=args.dry_run,
            )
            print(json.dumps(stats, indent=2))
            return 0

        elif args.command == "check-mirror":
            report = check_mirror_freshness()
            if args.json:
                print(json.dumps(report, indent=2))
            else:
                print("─" * 60)
                print("MIRROR FRESHNESS")
                print("─" * 60)
                for name, info in report["sources"].items():
                    flag = " [BLOCKING]" if info.get("blocking") else ""
                    if not info.get("exists"):
                        print(f"  ❌ {name}{flag}: {info.get('status', 'missing').upper()}")
                        continue
                    icon = {"ok": "🟢", "warn": "🟡", "halt": "🔴"}.get(info["status"], "⚪")
                    print(f"  {icon} {name}{flag}: {info['age_hours']:.1f}h old ({info['status']})")
                print(f"\nMax age: {report['max_age_hours']:.1f}h")
                print(f"Warn threshold: {STALE_WARN_HOURS}h")
                print(f"Halt threshold: {STALE_HALT_HOURS}h")
                if report["blocking_halt"]:
                    print(f"\n🔴 BLOCKING HALT: {', '.join(report['stale_blocking_sources'])}")
            if args.strict and report["blocking_halt"]:
                return 3
            return 0

        elif args.command == "prune-backups":
            deleted = prune_backups()
            print(f"Pruned {deleted} backup(s)")
            return 0

        elif args.command == "ensure-dirs":
            ensure_dirs()
            print(f"OK: {BACKUP_DIR}")
            print(f"OK: {EVENTS_DIR}")
            return 0

        else:
            parser.print_help()
            return 1

    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
