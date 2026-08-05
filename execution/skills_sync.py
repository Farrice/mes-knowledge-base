#!/usr/bin/env python3
"""
Matt Pocock skills suite weekly sync orchestrator.
Checks for upstream drift and applies updates deterministically.
Writes health receipt for self-heal monitoring (Compass Doctrine — reports, never blocks).
"""

import subprocess
import json
import os
import shutil
from datetime import datetime
from pathlib import Path

# Repo root
REPO_ROOT = Path(__file__).parent.parent

# Matt Pocock skills directories
AGENTS_SKILLS_DIR = Path.home() / ".agents" / "skills"
CLAUDE_SKILLS_DIR = Path.home() / ".claude" / "skills"
LOCKFILE = Path.home() / ".agents" / ".skill-lock.json"

# Health monitoring
HEALTH_DIR = REPO_ROOT / ".agent" / "health"
HEALTH_RECEIPT = HEALTH_DIR / "skills-sync.json"

# Log file at user level (shared with launchd job)
LOG_FILE = Path.home() / ".agents" / "skill-sync-detailed.log"


def log_msg(msg):
    """Log with timestamp to both stdout and file."""
    timestamp = datetime.now().isoformat()
    line = f"[{timestamp}] {msg}"
    print(line)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")


def run_cmd(cmd, description, timeout=300):
    """Run a shell command and return (success, output)."""
    log_msg(f"Running: {description}")
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=str(Path.home() / ".agents"),
        )
        if result.returncode == 0:
            log_msg(f"✓ {description}")
            return True, result.stdout
        else:
            log_msg(f"✗ {description}: {result.stderr}")
            return False, result.stderr
    except subprocess.TimeoutExpired:
        log_msg(f"✗ {description}: timeout after {timeout}s")
        return False, "timeout"
    except Exception as e:
        log_msg(f"✗ {description}: {str(e)}")
        return False, str(e)


def check_drift():
    """Run npx skills check -g and return True if drift detected."""
    cmd = "npx skills@latest check -g 2>&1"
    success, output = run_cmd(cmd, "npx skills@latest check -g")

    if not success:
        log_msg("Drift check command failed; skipping update")
        return False

    # Detect drift from output
    if "up to date" in output.lower():
        log_msg("No drift detected; skills are up to date")
        return False

    log_msg("Drift detected; will proceed with update")
    return True


def apply_updates():
    """Apply skill updates using npx skills update."""
    cmd = "npx skills@latest update --yes -g 2>&1"
    success, output = run_cmd(cmd, "npx skills@latest update --yes -g")

    if success:
        log_msg(f"Updates applied (first 500 chars): {output[:500]}")
        return True
    else:
        log_msg(f"Update command failed: {output[:500]}")
        return False


def get_installed_skills():
    """Return set of currently installed skill names from lockfile."""
    if not LOCKFILE.exists():
        return set()
    try:
        with open(LOCKFILE) as f:
            data = json.load(f)
        return set(data.get("skills", {}).keys())
    except Exception as e:
        log_msg(f"⚠ Failed to read lockfile: {e}")
        return set()


def archive_deprecated_skills():
    """
    Archive skills that are no longer in mattpocock/skills.
    This is a heuristic: if a skill folder exists in .agents/skills but is NOT in the lockfile,
    it was likely archived upstream. Move it and remove its symlink.
    """
    try:
        skills_on_disk = set(
            p.name for p in AGENTS_SKILLS_DIR.iterdir()
            if p.is_dir() and not p.name.startswith(".")
        )
        skills_in_lockfile = get_installed_skills()

        to_archive = skills_on_disk - skills_in_lockfile
        if not to_archive:
            log_msg("No deprecated skills to archive")
            return True

        # Create dated archive directory
        archive_dir = Path.home() / ".agents" / f"skills-archive-{datetime.now().strftime('%Y-%m-%d')}"
        archive_dir.mkdir(exist_ok=True)
        log_msg(f"Archiving deprecated skills to {archive_dir}")

        for skill in to_archive:
            src = AGENTS_SKILLS_DIR / skill
            dst = archive_dir / skill
            if src.exists():
                shutil.move(str(src), str(dst))
                log_msg(f"  Archived: {skill}")

                # Remove symlink if it exists
                symlink = CLAUDE_SKILLS_DIR / skill
                if symlink.is_symlink():
                    symlink.unlink()
                    log_msg(f"  Removed symlink: {skill}")

        return True
    except Exception as e:
        log_msg(f"⚠ Error during deprecation archive: {e}")
        return True  # Don't fail the whole run


def reconcile_symlinks():
    """
    Ensure all skills in .agents/skills have symlinks in .claude/skills.
    Create missing symlinks; leave non-skill directories and other entries alone.
    """
    try:
        # Known non-suite entries to skip
        skip = {
            "last30days",  # intentionally a real directory, not symlinked
            "source-command-video-context-audit",
            "source-command-video-context-ledger",
            "source-command-video-creative-reference",
            "source-command-video-frame-ledger",
            "source-command-video-multi-compare",
            "source-command-video-source-extract",
            "source-command-video-transcript-ledger",
            "source-command-video-visual-ocr",
            "youtube-video-context-analysis",
            ".skill-lock.json",
        }

        agents_skills = {
            p.name for p in AGENTS_SKILLS_DIR.iterdir()
            if p.is_dir() and p.name not in skip
        }

        log_msg(f"Reconciling {len(agents_skills)} symlinks in .claude/skills/")

        for skill in agents_skills:
            symlink = CLAUDE_SKILLS_DIR / skill
            if symlink.exists():
                # Already exists (symlink or otherwise)
                if symlink.is_symlink() and not symlink.resolve().exists():
                    log_msg(f"  Removing dangling symlink: {skill}")
                    symlink.unlink()
                continue

            # Create relative symlink
            target = f"../../.agents/skills/{skill}"
            symlink.symlink_to(target)
            log_msg(f"  Created symlink: {skill}")

        return True
    except Exception as e:
        log_msg(f"⚠ Error during symlink reconciliation: {e}")
        return True  # Don't fail the whole run


def verify_lockfile():
    """Verify lockfile integrity."""
    if not LOCKFILE.exists():
        log_msg("✗ Lockfile missing!")
        return False

    try:
        with open(LOCKFILE) as f:
            data = json.load(f)
        count = len(data.get("skills", {}))
        log_msg(f"✓ Lockfile verified: {count} skills tracked")
        return True
    except Exception as e:
        log_msg(f"✗ Lockfile invalid: {e}")
        return False


def write_health_receipt(status, count_updated=0):
    """Write health receipt for self-heal monitoring."""
    try:
        HEALTH_DIR.mkdir(parents=True, exist_ok=True)
        receipt = {
            "timestamp": datetime.now().isoformat(),
            "status": status,
            "count_updated": count_updated,
            "lockfile_count": len(get_installed_skills()),
        }
        with open(HEALTH_RECEIPT, "w") as f:
            json.dump(receipt, f, indent=2)
        log_msg(f"✓ Health receipt written: {status} ({receipt['lockfile_count']} skills)")
    except Exception as e:
        log_msg(f"✗ Failed to write health receipt: {e}")


def main():
    """Main orchestration — checks, updates, archives, reconciles, reports."""
    log_msg("=== SKILLS SYNC STARTED ===")

    # Check for drift
    if not check_drift():
        log_msg("=== SKILLS SYNC COMPLETE: no drift ===")
        write_health_receipt("no_drift")
        return

    # Apply updates
    if not apply_updates():
        log_msg("=== SKILLS SYNC FAILED: update error ===")
        write_health_receipt("update_failed")
        return

    # Archive deprecated skills
    archive_deprecated_skills()

    # Reconcile symlinks
    reconcile_symlinks()

    # Verify lockfile
    if not verify_lockfile():
        log_msg("=== SKILLS SYNC COMPLETE: verification failed ===")
        write_health_receipt("verification_failed")
        return

    log_msg("=== SKILLS SYNC COMPLETE: updates applied ===")
    write_health_receipt("success")


if __name__ == "__main__":
    main()
