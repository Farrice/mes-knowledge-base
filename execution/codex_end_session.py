#!/usr/bin/env python3
"""Codex-native coordinator for the canonical /end-session workflow.

The Python layer owns deterministic filesystem, handoff, verification, Git,
and retrieval receipts. Codex app actions (rename, pin, archive) stay in the
skill because only the app tool surface can perform them.

Usage:
    python3 execution/codex_end_session.py run --manifest closeout.json
    python3 execution/codex_end_session.py run --manifest closeout.json --dry-run
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
EXEC = ROOT / "execution"
SCHEMA = "codex-end-session/v1"
STATUSES = {"active", "blocked", "ready", "mid-build", "done"}
PIN_STATUSES = {"active", "blocked", "ready", "mid-build"}
TITLE_RE = re.compile(r"^[^:\n]{2,32}:\s+.+\s-\s.+$")
SECRET_PATH_RE = re.compile(
    r"(^|/)(?:\.env(?:\.|$)|credentials?(?:\.|$)|secrets?(?:\.|$)|"
    r"id_rsa(?:\.|$)|.*\.(?:pem|p12|pfx|key)$)", re.IGNORECASE,
)
SECRET_LINE_RE = re.compile(
    r"(?i)^\+[^+].*\b(?:api[_-]?key|secret|token|password|private[_-]?key)\b\s*[:=]\s*"
    r"[\"']?[A-Za-z0-9_./+=-]{20,}"
)
REQUIRED_HANDOFF_PATTERNS = {
    "title": re.compile(r"(?m)^#\s+\S"),
    "completed": re.compile(r"(?im)^(?:##+\s+.*completed|\*\*\s*completed\s*\*\*)"),
    "remaining": re.compile(
        r"(?im)^(?:##+\s+(?:remaining priority|next session focus|next steps?)|"
        r"\*\*\s*(?:remaining priorit\w*|next session focus|next steps?)\s*\*\*)"
    ),
    "core_paths": re.compile(
        r"(?im)^##+\s+(?:core (?:context )?paths|load first|essential context paths)\s*$"
    ),
    "do_not_rebuild": re.compile(r"(?im)^##+\s+.*(?:do\s*n[o']?t|not)\s+rebuild"),
}


class CloseoutError(RuntimeError):
    pass


@dataclass
class CommandResult:
    returncode: int
    stdout: str
    stderr: str


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", (value or "").lower()).strip("-")


def normalized(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n").rstrip() + "\n"


def sha256_text(text: str) -> str:
    return hashlib.sha256(normalized(text).encode("utf-8")).hexdigest()


def lane_operation_lock_path(project: Path) -> Path:
    """Return the shared main-repo lock used by closeout and lane sealing."""
    result = git(project, "rev-parse", "--git-common-dir")
    if result.returncode != 0 or not result.stdout.strip():
        return project / ".git" / "lane-operation.lock"
    common = Path(result.stdout.strip())
    if not common.is_absolute():
        common = (project / common).resolve()
    return common / "lane-operation.lock"


def acquire_lane_operation_lock(project: Path) -> int:
    """Hold the lane lifecycle lock before closeout can create tracked changes."""
    import fcntl

    lockfile = lane_operation_lock_path(project)
    lockfile.parent.mkdir(parents=True, exist_ok=True)
    lock_fd = os.open(lockfile, os.O_CREAT | os.O_RDWR)
    try:
        fcntl.flock(lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError as exc:
        os.close(lock_fd)
        raise CloseoutError(
            "lane merge or another closeout is already active; retry after it finishes"
        ) from exc
    return lock_fd


def release_lane_operation_lock(lock_fd: int | None) -> None:
    if lock_fd is None:
        return
    import fcntl

    try:
        fcntl.flock(lock_fd, fcntl.LOCK_UN)
    finally:
        os.close(lock_fd)


def run_command(command: list[str], cwd: Path, timeout: int = 180) -> CommandResult:
    completed = subprocess.run(
        command, cwd=str(cwd), text=True, capture_output=True, timeout=timeout,
    )
    return CommandResult(completed.returncode, completed.stdout or "", completed.stderr or "")


def git(project: Path, *args: str, timeout: int = 60) -> CommandResult:
    return run_command(["git", "-C", str(project), *args], project, timeout)


def inside(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def resolve_project_path(project: Path, value: str) -> Path:
    path = Path(value).expanduser()
    return path.resolve() if path.is_absolute() else (project / path).resolve()


def relative_project_path(project: Path, value: str) -> str:
    path = resolve_project_path(project, value)
    if not inside(path, project):
        raise CloseoutError(f"task-owned path escapes project root: {value}")
    return path.relative_to(project.resolve()).as_posix()


def validate_handoff_source(path: Path) -> list[str]:
    if not path.exists() or not path.is_file():
        return [f"handoff source not found: {path}"]
    text = path.read_text(encoding="utf-8")
    missing = [name for name, pattern in REQUIRED_HANDOFF_PATTERNS.items() if not pattern.search(text)]
    return [f"handoff source missing required section: {name}" for name in missing]


def handoff_title(text: str) -> str:
    match = re.search(r"(?m)^#\s+(.+?)\s*$", text)
    return match.group(1).strip() if match else ""


def handoff_core_paths(text: str) -> list[str]:
    section = re.search(
        r"(?ims)^##+\s+(?:core (?:context )?paths|load first|essential context paths)\s*$"
        r"(.*?)(?=^##+\s|\Z)",
        text,
    )
    if not section:
        return []
    values: list[str] = []
    for candidate in re.findall(r"`([^`]+)`", section.group(1)):
        value = candidate.strip()
        if not value or value.startswith(("/resume", "http://", "https://")):
            continue
        values.append(value)
    return values


def load_manifest(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CloseoutError(f"manifest unreadable: {exc}") from exc
    required = (
        "schema_version", "task_id", "title", "slug", "status",
        "project_root", "handoff_source", "core_paths", "task_owned_paths",
    )
    missing = [key for key in required if key not in data]
    if missing:
        raise CloseoutError("manifest missing fields: " + ", ".join(missing))
    if data["schema_version"] != SCHEMA:
        raise CloseoutError(f"schema_version must be {SCHEMA!r}")
    if not str(data["task_id"]).strip():
        raise CloseoutError("task_id must not be empty")
    task_title = str(data["title"]).strip()
    if not TITLE_RE.match(task_title):
        raise CloseoutError("title must match '[Domain]: [Specific Object] - [Outcome]'")
    slug = slugify(str(data["slug"]))
    if not slug or slug != data["slug"]:
        raise CloseoutError("slug must be non-empty kebab-case")
    if data["status"] not in STATUSES:
        raise CloseoutError(f"status must be one of {sorted(STATUSES)}")
    if not isinstance(data["core_paths"], list) or not data["core_paths"]:
        raise CloseoutError("core_paths must be a non-empty list")
    if not isinstance(data["task_owned_paths"], list):
        raise CloseoutError("task_owned_paths must be a list")
    if not isinstance(data.get("artifact_moves", []), list):
        raise CloseoutError("artifact_moves must be a list when provided")
    if not isinstance(data.get("review_items", []), list):
        raise CloseoutError("review_items must be a list when provided")
    project = Path(data["project_root"]).expanduser().resolve()
    if not project.exists():
        raise CloseoutError(f"project_root not found: {project}")
    handoff = resolve_project_path(project, data["handoff_source"])
    if not inside(handoff, project):
        raise CloseoutError("handoff_source must stay inside project_root")
    errors = validate_handoff_source(handoff)
    source_text = handoff.read_text(encoding="utf-8") if handoff.exists() else ""
    source_title = handoff_title(source_text)
    if source_title and source_title != task_title:
        errors.append(
            f"handoff title does not match manifest title: {source_title!r} != {task_title!r}"
        )
    manifest_core_paths: set[str] = set()
    for value in data["core_paths"]:
        target = resolve_project_path(project, str(value))
        if not target.exists():
            errors.append(f"core path not found: {value}")
        manifest_core_paths.add(str(target))
    source_core_paths = {
        str(resolve_project_path(project, value)) for value in handoff_core_paths(source_text)
    }
    if source_core_paths != manifest_core_paths:
        errors.append(
            "handoff core paths do not match manifest core paths: "
            f"handoff={sorted(source_core_paths)} manifest={sorted(manifest_core_paths)}"
        )
    if errors:
        raise CloseoutError("; ".join(errors))
    data["project_root"] = str(project)
    data["handoff_source"] = str(handoff)
    data["task_owned_paths"] = sorted({relative_project_path(project, str(v)) for v in data["task_owned_paths"]})
    owned = set(data["task_owned_paths"])
    protected = {str(handoff.resolve())} | manifest_core_paths
    normalized_moves: list[dict[str, str]] = []
    for index, row in enumerate(data.get("artifact_moves", [])):
        if not isinstance(row, dict) or not row.get("source") or not row.get("destination"):
            raise CloseoutError(f"artifact_moves[{index}] requires source and destination")
        source = resolve_project_path(project, str(row["source"]))
        destination = resolve_project_path(project, str(row["destination"]))
        source_rel = relative_project_path(project, str(source))
        destination_rel = relative_project_path(project, str(destination))
        if source_rel not in owned or destination_rel not in owned:
            raise CloseoutError("artifact move source and destination must both be task-owned")
        if str(source) in protected:
            raise CloseoutError("handoff source and core paths cannot move during closeout")
        if not source.exists() or not source.is_file():
            raise CloseoutError(f"artifact move source not found: {source_rel}")
        if destination.exists():
            raise CloseoutError(f"artifact move destination already exists: {destination_rel}")
        normalized_moves.append({"source": source_rel, "destination": destination_rel})
    data["artifact_moves"] = normalized_moves
    data["review_items"] = data.get("review_items", [])
    return data


def organize_task_artifacts(manifest: dict[str, Any], dry_run: bool,
                            held: bool = False) -> dict[str, Any]:
    project = Path(manifest["project_root"])
    moves = manifest.get("artifact_moves", [])
    receipt: dict[str, Any] = {"status": "clean", "moved": [], "review": []}
    if held and moves:
        receipt["status"] = "held"
        receipt["review"].extend(
            f"organization held pending Git policy review: {row['source']} -> {row['destination']}"
            for row in moves
        )
        return receipt
    for row in moves:
        if dry_run:
            receipt["status"] = "dry-run"
            receipt["moved"].append(row)
            continue
        source = project / row["source"]
        destination = project / row["destination"]
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(source), str(destination))
        receipt["moved"].append(row)
    moved_sources = {row["source"] for row in moves}
    try:
        status = parse_status(project)
        git_status_available = True
    except CloseoutError:
        status = {}
        git_status_available = False
    for value in manifest["task_owned_paths"]:
        path = Path(value)
        is_loose = (status.get(value) == "??" if git_status_available
                    else (project / value).exists())
        if len(path.parts) == 1 and value not in moved_sources and is_loose:
            receipt["review"].append(
                f"task-owned loose root artifact needs an explicit destination: {value}"
            )
    if receipt["review"] and receipt["status"] == "clean":
        receipt["status"] = "review"
    return receipt


def parse_status(project: Path) -> dict[str, str]:
    result = git(project, "status", "--porcelain=v1", "--untracked-files=all")
    if result.returncode != 0:
        raise CloseoutError(f"git status failed: {result.stderr.strip()}")
    rows: dict[str, str] = {}
    for line in result.stdout.splitlines():
        if len(line) < 4:
            continue
        code = line[:2]
        raw = line[3:]
        path = raw.split(" -> ", 1)[-1]
        rows[path] = code
    return rows


def git_context(project: Path) -> dict[str, Any]:
    inside_repo = git(project, "rev-parse", "--is-inside-work-tree")
    if inside_repo.returncode != 0 or inside_repo.stdout.strip() != "true":
        return {"is_git": False, "status": {}}
    branch = git(project, "branch", "--show-current").stdout.strip()
    head = git(project, "rev-parse", "HEAD").stdout.strip()
    git_dir = Path(git(project, "rev-parse", "--git-dir").stdout.strip())
    common_dir = Path(git(project, "rev-parse", "--git-common-dir").stdout.strip())
    if not git_dir.is_absolute():
        git_dir = (project / git_dir).resolve()
    if not common_dir.is_absolute():
        common_dir = (project / common_dir).resolve()
    remote_ref = git(project, "rev-parse", "--verify", f"refs/remotes/origin/{branch}")
    ahead = behind = 0
    if remote_ref.returncode == 0:
        counts = git(project, "rev-list", "--left-right", "--count", f"HEAD...origin/{branch}")
        if counts.returncode == 0:
            parts = counts.stdout.split()
            if len(parts) == 2:
                ahead, behind = int(parts[0]), int(parts[1])
    return {
        "is_git": True,
        "branch": branch,
        "head": head,
        "dedicated_worktree": git_dir != common_dir,
        "remote_branch_exists": remote_ref.returncode == 0,
        "ahead": ahead,
        "behind": behind,
        "status": parse_status(project),
    }


def foreign_tool_lock(project: Path, ttl: int = 600) -> str:
    path = project / ".agent" / "active-tool.lock"
    try:
        row = json.loads(path.read_text(encoding="utf-8"))
        age = time.time() - float(row.get("ts", 0))
        tool = str(row.get("tool", ""))
        if tool and tool != "codex" and 0 <= age < ttl:
            return f"recent same-tree activity from {tool} ({int(age)}s ago)"
    except (OSError, ValueError, TypeError, json.JSONDecodeError):
        pass
    return ""


def fresh_session_lock(project: Path, ttl: int = 45 * 60) -> str:
    path = project / ".agent" / "session.lock"
    try:
        row = json.loads(path.read_text(encoding="utf-8"))
        age = time.time() - float(row.get("heartbeat", 0))
        if 0 <= age < ttl:
            return f"fresh session lock for '{row.get('mission', 'unknown')}' ({int(age)}s old)"
    except (OSError, ValueError, TypeError, json.JSONDecodeError):
        pass
    return ""


def git_policy_blockers(manifest: dict[str, Any], context: dict[str, Any],
                        initial_status: dict[str, str]) -> list[str]:
    if not context.get("is_git"):
        return []
    project = Path(manifest["project_root"])
    blockers = []
    branch = context.get("branch", "")
    if not branch:
        blockers.append("detached HEAD")
    elif branch == "main" or not branch.startswith("codex/"):
        blockers.append("automatic Git is allowed only on codex/* branches; main is never auto-committed or pushed")
    if not context.get("dedicated_worktree"):
        blockers.append("automatic Git requires a dedicated linked worktree")
    if context.get("behind", 0):
        blockers.append(f"remote branch is {context['behind']} commit(s) ahead")
    owned = set(manifest["task_owned_paths"])
    retry_receipts = {
        path for path in initial_status
        if is_closeout_generated(path, manifest["slug"])
    }
    unowned = sorted(set(initial_status) - owned - retry_receipts)
    if unowned:
        blockers.append("pre-existing dirty paths are not task-owned: " + ", ".join(unowned))
    deletions = sorted(path for path, code in initial_status.items() if "D" in code)
    if deletions:
        blockers.append("unexpected deletions are never auto-staged: " + ", ".join(deletions))
    secret_paths = sorted(path for path in owned if SECRET_PATH_RE.search(path))
    if secret_paths:
        blockers.append("secret-like paths are never auto-staged: " + ", ".join(secret_paths))
    lock = foreign_tool_lock(project)
    if lock:
        blockers.append(lock)
    session = fresh_session_lock(project)
    if session:
        blockers.append(session)
    return blockers


def global_home() -> Path:
    override = os.environ.get("CODEX_END_SESSION_HOME")
    return Path(override).expanduser().resolve() if override else Path.home() / ".codex" / "end-session"


def write_global_handoff(source: Path, slug: str) -> dict[str, Any]:
    home = global_home()
    destination = home / "handoffs" / f"{datetime.now().date().isoformat()}-{slug}.md"
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    source_text = source.read_text(encoding="utf-8")
    stored_text = destination.read_text(encoding="utf-8")
    return {
        "schema_version": "handoff-save/v1",
        "source_path": str(source.resolve()),
        "stored_path": str(destination.resolve()),
        "source_sha256": sha256_text(source_text),
        "stored_sha256": sha256_text(stored_text),
        "valid": sha256_text(source_text) == sha256_text(stored_text),
    }


def save_antigravity_handoff(manifest: dict[str, Any], dry_run: bool) -> dict[str, Any]:
    project = Path(manifest["project_root"])
    source = Path(manifest["handoff_source"])
    if dry_run:
        return {
            "schema_version": "handoff-save/v1", "dry_run": True,
            "source_path": str(source),
            "stored_path": str(project / ".agent" / "handoffs" /
                               f"{datetime.now().date().isoformat()}-{manifest['slug']}.md"),
        }
    command = [
        sys.executable, str(project / "execution" / "handoff_store.py"), "save", str(source),
        "--thread", manifest["slug"], "--slug", manifest["slug"],
        "--status", manifest["status"], "--json",
    ]
    if manifest["status"] in PIN_STATUSES:
        command.append("--pin")
    saved = run_command(command, project)
    if saved.returncode != 0:
        raise CloseoutError(f"handoff save failed: {(saved.stderr or saved.stdout).strip()}")
    try:
        receipt = json.loads(saved.stdout)
    except json.JSONDecodeError as exc:
        raise CloseoutError(f"handoff save did not return JSON: {saved.stdout}") from exc
    verified = run_command([
        sys.executable, str(project / "execution" / "handoff_store.py"), "verify",
        manifest["slug"], "--source", str(source), "--json",
    ], project)
    try:
        verify_receipt = json.loads(verified.stdout)
    except json.JSONDecodeError as exc:
        raise CloseoutError(f"handoff verify did not return JSON: {verified.stdout}") from exc
    if verified.returncode != 0 or not verify_receipt.get("valid"):
        raise CloseoutError("handoff identity verification failed: " + "; ".join(verify_receipt.get("errors", [])))
    receipt["verification"] = verify_receipt
    return receipt


def run_shared_spine(manifest: dict[str, Any], stored_path: str, dry_run: bool) -> dict[str, Any]:
    project = Path(manifest["project_root"])
    exact_path = manifest["handoff_source"] if dry_run else stored_path
    command = [
        sys.executable, str(project / "execution" / "end_session_closeout.py"), "run",
        "--slug", manifest["slug"], "--handoff", exact_path,
        "--git-policy", "codex-owned",
    ]
    if dry_run:
        command.append("--dry-run")
    result = run_command(command, project, timeout=600)
    lines = [line for line in result.stdout.splitlines() if line.startswith("CLOSEOUT ")]
    failures = [line for line in lines if ": FAIL " in line]
    resolved = any(line.startswith("CLOSEOUT resolve-handoff: OK ") for line in lines)
    return {
        "returncode": result.returncode,
        "lines": lines,
        "failures": failures,
        "valid": result.returncode == 0 and not failures and resolved,
        "stderr": result.stderr.strip(),
    }


def run_verifiers(project: Path, commands: Iterable[list[str]]) -> list[dict[str, Any]]:
    receipts = []
    for command in commands:
        result = run_command(command, project, timeout=600)
        output = (result.stdout or result.stderr).strip()
        receipts.append({
            "command": command, "returncode": result.returncode,
            "valid": result.returncode == 0,
            "summary": output.splitlines()[-1] if output else "(no output)",
        })
    return receipts


def default_verifiers(project: Path) -> list[list[str]]:
    if not (project / "execution" / "verify_codex_end_session.py").exists():
        return []
    return [
        [sys.executable, "execution/verify_codex_end_session.py"],
        [sys.executable, "execution/verify_operator_core_end_session.py"],
        [sys.executable, "execution/verify_system_control_plane.py", "--section", "end-session"],
        [sys.executable, "execution/sync_operator_core_end_session.py", "--check"],
        [sys.executable, "execution/verify_operator_core_system_audit.py"],
        [sys.executable, "execution/verify_operator_core_source_to_skill_system.py"],
        [sys.executable, "execution/verify_codex_authority.py"],
        [sys.executable, "execution/codex_live_surface_audit.py", "--strict"],
    ]


def is_closeout_generated(path: str, slug: str) -> bool:
    date = datetime.now().date().isoformat()
    exact = {
        ".agent/handoffs/index.md",
        ".agent/handoffs/LATEST.md",
        ".agent/sessions/end-session-memory-ledger.jsonl",
        ".agent/sessions/notion-session-memory-outbox.jsonl",
        ".agent/sessions/notion-session-memory-events.jsonl",
        ".agent/sessions/closeout-intelligence-guard.jsonl",
        ".agent/routing-feedback-inbox.jsonl",
        ".agent/performance-log.jsonl",
        ".agent/performance-log-inbox.jsonl",
        "guides/INDEX.md",
    }
    if path in exact:
        return True
    if path.startswith(".agent/handoffs/") and slug in Path(path).name:
        return True
    if path.startswith(".agent/recurring-reports/") and "/archive/" not in path:
        return bool(re.fullmatch(
            rf"{re.escape(date)}T\d{{6}}-session-closeout-intelligence\.md",
            Path(path).name,
        ))
    if path.startswith(".agent/cos/journal/") and slug in Path(path).name:
        return True
    if path.startswith(".agent/sessions/state-archive/") and slug in Path(path).name:
        return True
    if path == f"guides/{date}-{slug}.md":
        return True
    return False


def collect_self_heal_review(project: Path) -> list[dict[str, Any]]:
    script = project / "execution" / "self_heal.py"
    if not script.exists():
        return []
    result = run_command(
        [sys.executable, str(script), "report", "--json", "--no-cache"],
        project, timeout=180,
    )
    if result.returncode != 0:
        return [{"id": "self-heal-report", "class": "ERROR",
                 "what": (result.stderr or result.stdout).strip()[-240:]}]
    try:
        rows = json.loads(result.stdout or "[]")
        return rows if isinstance(rows, list) else []
    except json.JSONDecodeError:
        return [{"id": "self-heal-report", "class": "ERROR",
                 "what": "self-heal report did not return JSON"}]


def staged_secret_findings(project: Path) -> list[str]:
    diff = git(project, "diff", "--cached", "--unified=0", "--no-color")
    if diff.returncode != 0:
        return ["could not inspect staged diff for secrets"]
    findings = []
    for line in diff.stdout.splitlines():
        if SECRET_LINE_RE.search(line):
            findings.append(line[:160])
    return findings


def commit_and_push(manifest: dict[str, Any], allowed_paths: list[str],
                    verifier_receipts: list[dict[str, Any]]) -> dict[str, Any]:
    project = Path(manifest["project_root"])
    branch = git(project, "branch", "--show-current").stdout.strip()
    receipt: dict[str, Any] = {"status": "held", "branch": branch, "paths": []}
    if any(not row["valid"] for row in verifier_receipts):
        receipt["blockers"] = ["one or more required verifiers failed"]
        return receipt
    status_paths = set(parse_status(project))
    stage_paths = sorted(set(allowed_paths) & status_paths)
    receipt["paths"] = stage_paths
    if not stage_paths:
        commit_sha = git(project, "rev-parse", "HEAD").stdout.strip()
        remote = git(project, "ls-remote", "origin", f"refs/heads/{branch}", timeout=120)
        remote_sha = remote.stdout.split()[0] if remote.returncode == 0 and remote.stdout.split() else ""
        receipt.update({"status": "clean", "commit": commit_sha, "remote_sha": remote_sha})
        if remote_sha != commit_sha:
            receipt["status"] = "push-unverified"
            receipt["blockers"] = ["clean local branch does not match its remote SHA"]
        return receipt
    staged = run_command(["git", "-C", str(project), "add", "--", *stage_paths], project)
    if staged.returncode != 0:
        receipt["blockers"] = [f"git add failed: {staged.stderr.strip()}"]
        return receipt
    staged_names = git(project, "diff", "--cached", "--name-only").stdout.splitlines()
    unexpected = sorted(set(staged_names) - set(stage_paths))
    if unexpected:
        git(project, "restore", "--staged", "--", *staged_names)
        receipt["blockers"] = ["unexpected staged paths: " + ", ".join(unexpected)]
        return receipt
    check = git(project, "diff", "--cached", "--check")
    secret_findings = staged_secret_findings(project)
    if check.returncode != 0 or secret_findings:
        if staged_names:
            git(project, "restore", "--staged", "--", *staged_names)
        blockers = []
        if check.returncode != 0:
            blockers.append("git diff --cached --check failed")
        if secret_findings:
            blockers.append("secret-like added lines detected")
        receipt["blockers"] = blockers
        return receipt
    if not staged_names:
        receipt.update({"status": "clean", "commit": git(project, "rev-parse", "HEAD").stdout.strip()})
        return receipt
    message = manifest.get("commit_message") or f"chore(codex): close {manifest['slug']}"
    committed = git(project, "commit", "-m", message, timeout=180)
    if committed.returncode != 0:
        receipt["blockers"] = [f"git commit failed: {(committed.stderr or committed.stdout).strip()}"]
        return receipt
    commit_sha = git(project, "rev-parse", "HEAD").stdout.strip()
    pushed = git(project, "push", "-u", "origin", branch, timeout=300)
    if pushed.returncode != 0:
        receipt.update({
            "status": "committed-local", "commit": commit_sha,
            "blockers": [f"push failed: {(pushed.stderr or pushed.stdout).strip()}"],
        })
        return receipt
    remote = git(project, "ls-remote", "origin", f"refs/heads/{branch}", timeout=120)
    remote_sha = remote.stdout.split()[0] if remote.returncode == 0 and remote.stdout.split() else ""
    receipt.update({
        "status": "pushed" if remote_sha == commit_sha else "push-unverified",
        "commit": commit_sha, "remote_sha": remote_sha,
    })
    if remote_sha != commit_sha:
        receipt["blockers"] = ["remote SHA does not match local commit"]
    return receipt


def write_global_receipts(manifest: dict[str, Any], handoff: dict[str, Any],
                          spine: dict[str, Any], git_receipt: dict[str, Any],
                          verifiers: list[dict[str, Any]], organization: dict[str, Any],
                          review_items: list[Any], task_actions: dict[str, Any],
                          dry_run: bool) -> dict[str, str]:
    home = global_home()
    integration = home / "integration-queue" / f"{datetime.now().date().isoformat()}-{manifest['slug']}.md"
    review_queue = home / "review-queue" / f"{datetime.now().date().isoformat()}-{manifest['slug']}.json"
    registry = home / "registry.jsonl"
    index = home / "INDEX.md"
    if dry_run:
        return {"home": str(home), "integration_packet": str(integration),
                "review_queue": str(review_queue), "registry": str(registry),
                "index": str(index)}
    home.mkdir(parents=True, exist_ok=True)
    integration.parent.mkdir(parents=True, exist_ok=True)
    review_queue.parent.mkdir(parents=True, exist_ok=True)
    blockers = git_receipt.get("blockers", []) + spine.get("failures", [])
    changed = git_receipt.get("paths", [])
    check_lines = [
        f"- `{Path(' '.join(row['command'])).name if row.get('command') else 'check'}`: "
        f"{'PASS' if row.get('valid') else 'FAIL'} - {row.get('summary', '')}"
        for row in verifiers
    ]
    spine_lines = [f"- {line}" for line in spine.get("lines", [])]
    integration.write_text(
        "\n".join([
            f"# Integration Packet: {manifest['title']}", "",
            f"- **Task ID:** `{manifest['task_id']}`",
            f"- **Project:** `{manifest['project_root']}`",
            f"- **Branch:** `{git_receipt.get('branch', '')}`",
            f"- **Base:** `{git_receipt.get('base', '')}`",
            f"- **Commit:** `{git_receipt.get('commit', '')}`",
            f"- **Remote SHA:** `{git_receipt.get('remote_sha', '')}`",
            f"- **Git status:** `{git_receipt.get('status', 'held')}`",
            f"- **Handoff:** `{handoff.get('stored_path', '')}`", "",
            "## Changed Paths", "",
            *([f"- `{path}`" for path in changed] or ["- (none)"]), "",
            "## Checks", "",
            *(check_lines or ["- No project verifiers configured"]),
            *(spine_lines or ["- No shared spine lines"]), "",
            "## Organization", "",
            f"- Status: `{organization.get('status', 'unknown')}`",
            *([f"- Moved `{row['source']}` -> `{row['destination']}`"
               for row in organization.get("moved", [])] or ["- No artifact moves"]),
            f"- Review queue: `{review_queue}`", "",
            "## Blockers", "",
            *([f"- {item}" for item in blockers] or ["- None"]), "",
            "## Safe Merge Route", "",
            "- Review this branch against current `main` from a fresh integration worktree.",
            "- Require expected-diff and verifier proof before merging.",
            "- Never merge or push `main` automatically from `/end-session`.", "",
        ]), encoding="utf-8",
    )
    review_queue.write_text(json.dumps({
        "schema_version": "codex-end-session-review/v1",
        "task_id": manifest["task_id"],
        "title": manifest["title"],
        "slug": manifest["slug"],
        "items": review_items,
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    row = {
        "schema_version": "codex-end-session-pointer/v1", "ts": now_iso(),
        "task_id": manifest["task_id"], "title": manifest["title"],
        "slug": manifest["slug"], "status": manifest["status"],
        "project_root": manifest["project_root"],
        "handoff_path": handoff.get("stored_path", ""),
        "integration_packet": str(integration),
        "review_queue": str(review_queue),
        "branch": git_receipt.get("branch", ""),
        "commit": git_receipt.get("commit", ""),
        "git_status": git_receipt.get("status", "held"),
        "task_actions": task_actions,
    }
    with registry.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, sort_keys=True) + "\n")
    latest: dict[str, dict[str, Any]] = {}
    for line in registry.read_text(encoding="utf-8").splitlines():
        try:
            item = json.loads(line)
        except json.JSONDecodeError:
            continue
        latest[item.get("task_id") or item.get("slug", "")] = item
    lines = ["# Codex End-Session Registry", "", "Newest pointer per task. Project handoffs remain canonical.", ""]
    for item in sorted(latest.values(), key=lambda value: value.get("ts", ""), reverse=True):
        lines.append(
            f"- **{item.get('title', item.get('slug'))}** — `{item.get('status')}` — "
            f"[handoff]({item.get('handoff_path')}) — `{item.get('branch')}`"
        )
    index.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"home": str(home), "integration_packet": str(integration),
            "review_queue": str(review_queue), "registry": str(registry),
            "index": str(index)}


def task_actions_for(status: str, title: str, closeout_valid: bool, dry_run: bool) -> dict[str, Any]:
    return {
        "rename": True,
        "title": title,
        "pin": status in PIN_STATUSES,
        "archive": status == "done" and closeout_valid and not dry_run,
        "reason": ("archive only after verified done closeout" if status == "done"
                   else "unfinished tasks stay visible and pinned"),
    }


def coordinate(manifest: dict[str, Any], dry_run: bool) -> dict[str, Any]:
    project = Path(manifest["project_root"])
    antigravity_adapter = (project / "execution" / "handoff_store.py").exists() and \
        (project / "execution" / "end_session_closeout.py").exists()
    initial_context = git_context(project)
    initial_status = dict(initial_context.get("status", {}))
    recognized_initial = sorted(
        path for path in initial_status
        if is_closeout_generated(path, manifest["slug"])
    )
    blockers = git_policy_blockers(manifest, initial_context, initial_status)
    organization = organize_task_artifacts(manifest, dry_run, held=bool(blockers))

    if antigravity_adapter:
        handoff = save_antigravity_handoff(manifest, dry_run)
    elif dry_run:
        handoff = {"dry_run": True, "source_path": manifest["handoff_source"],
                   "stored_path": str(global_home() / "handoffs" /
                                      f"{datetime.now().date().isoformat()}-{manifest['slug']}.md")}
    else:
        handoff = write_global_handoff(Path(manifest["handoff_source"]), manifest["slug"])
        if not handoff.get("valid"):
            raise CloseoutError("global fallback handoff checksum mismatch")

    spine = ({"valid": True, "lines": [], "failures": [], "skipped": "generic adapter"}
             if not antigravity_adapter else
             run_shared_spine(manifest, handoff["stored_path"], dry_run))

    final_status = initial_status if dry_run else git_context(project).get("status", {})
    generated = sorted(set(final_status) - set(initial_status))
    recognized_generated = sorted(
        path for path in generated if is_closeout_generated(path, manifest["slug"])
    )
    unexpected_generated = sorted(
        set(generated) - set(recognized_generated) - set(manifest["task_owned_paths"])
    )
    if unexpected_generated:
        blockers.append(
            "unexpected closeout-generated paths require review: " + ", ".join(unexpected_generated)
        )
    allowed = sorted(
        set(manifest["task_owned_paths"]) |
        set(recognized_initial) |
        set(recognized_generated)
    )
    expected_move_deletions = {row["source"] for row in organization.get("moved", [])}
    deletions = sorted(
        path for path, code in final_status.items()
        if path in allowed and "D" in code and path not in expected_move_deletions
    )
    if deletions:
        blockers.append("unexpected deletions are never auto-staged: " + ", ".join(deletions))
    secret_paths = sorted(path for path in allowed if SECRET_PATH_RE.search(path))
    if secret_paths:
        blockers.append("secret-like paths are never auto-staged: " + ", ".join(secret_paths))
    if not spine.get("valid"):
        blockers.append("shared closeout spine reported failure")

    verifier_commands = default_verifiers(project) if antigravity_adapter else []
    verifiers = ([{"command": command, "returncode": 0, "valid": True,
                   "summary": "dry-run: would execute"} for command in verifier_commands]
                 if dry_run else run_verifiers(project, verifier_commands))
    if any(not row["valid"] for row in verifiers):
        blockers.append("one or more required verifiers failed")

    if dry_run:
        git_receipt = {"status": "dry-run", "branch": initial_context.get("branch", ""),
                       "paths": allowed, "blockers": blockers}
    elif blockers:
        git_receipt = {"status": "held", "branch": initial_context.get("branch", ""),
                       "paths": allowed, "blockers": sorted(set(blockers))}
    elif not initial_context.get("is_git"):
        git_receipt = {"status": "not-applicable", "branch": "", "paths": []}
    else:
        git_receipt = commit_and_push(manifest, allowed, verifiers)
    git_receipt.setdefault("base", initial_context.get("head", ""))

    closeout_valid = bool(spine.get("valid")) and not git_receipt.get("blockers") and \
        git_receipt.get("status") in {"pushed", "clean", "not-applicable", "dry-run"}
    task_actions = task_actions_for(
        manifest["status"], manifest["title"], closeout_valid, dry_run,
    )
    review_items: list[Any] = []
    review_items.extend({"type": "manifest-review", "detail": item}
                        for item in manifest.get("review_items", []))
    review_items.extend({"type": "organization", "detail": item}
                        for item in organization.get("review", []))
    review_items.extend({"type": "unowned-path", "path": path}
                        for path in sorted(
                            set(initial_status) -
                            set(manifest["task_owned_paths"]) -
                            set(recognized_initial)
                        ))
    review_items.extend({"type": "unexpected-generated-path", "path": path}
                        for path in unexpected_generated)
    review_items.extend({"type": "blocker", "detail": item}
                        for item in sorted(set(blockers)))
    if not dry_run:
        review_items.extend({"type": "self-heal", "finding": row}
                            for row in collect_self_heal_review(project))
    global_receipts = write_global_receipts(
        manifest, handoff, spine, git_receipt, verifiers, organization,
        review_items, task_actions, dry_run,
    )
    return {
        "schema_version": "codex-end-session-receipt/v1", "ts": now_iso(),
        "valid": closeout_valid, "dry_run": dry_run,
        "manifest": manifest, "handoff": handoff, "spine": spine,
        "verifiers": verifiers, "organization": organization,
        "review_items": review_items, "git": git_receipt,
        "global_receipts": global_receipts, "task_actions": task_actions,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Codex-native End-session coordinator")
    sub = parser.add_subparsers(dest="command", required=True)
    run = sub.add_parser("run")
    run.add_argument("--manifest", required=True)
    run.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    lock_fd: int | None = None
    try:
        manifest = load_manifest(Path(args.manifest).expanduser())
        if not args.dry_run:
            lock_fd = acquire_lane_operation_lock(Path(manifest["project_root"]))
        receipt = coordinate(manifest, args.dry_run)
        print(json.dumps(receipt, indent=2, sort_keys=True))
        return 0 if receipt["valid"] else 1
    except (CloseoutError, subprocess.TimeoutExpired) as exc:
        print(json.dumps({
            "schema_version": "codex-end-session-receipt/v1", "valid": False,
            "error": str(exc), "ts": now_iso(),
        }, indent=2, sort_keys=True))
        return 1
    finally:
        release_lane_operation_lock(lock_fd)


if __name__ == "__main__":
    raise SystemExit(main())
