#!/usr/bin/env python3
"""Isolated behavior proof for the Codex-native End-session control plane."""
from __future__ import annotations

import contextlib
import io
import json
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

import codex_end_session as codex_close  # noqa: E402
import end_session_closeout as spine  # noqa: E402
import handoff_store  # noqa: E402


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def run(command: list[str], cwd: Path) -> str:
    completed = subprocess.run(command, cwd=str(cwd), text=True, capture_output=True)
    if completed.returncode != 0:
        raise AssertionError(
            f"command failed ({completed.returncode}): {' '.join(command)}\n"
            f"{completed.stdout}\n{completed.stderr}"
        )
    return completed.stdout.strip()


def init_repo(path: Path, branch: str = "codex/test") -> None:
    path.mkdir(parents=True, exist_ok=True)
    run(["git", "init", "-b", branch], path)
    run(["git", "config", "user.name", "Codex Test"], path)
    run(["git", "config", "user.email", "codex-test@example.invalid"], path)
    (path / "README.md").write_text("fixture\n", encoding="utf-8")
    run(["git", "add", "README.md"], path)
    run(["git", "commit", "-m", "fixture"], path)


def handoff_text(thread: str, title: str = "System: Fixture - Verified") -> str:
    return f"""---
thread: {thread}
status: ready
---

# {title}

## Completed

- Exact handoff identity fixture completed.

## Remaining Priority

- Resume from the verified core path.

## Core Paths

- `core.txt` - fixture source of truth

## Do Not Rebuild

- Preserve the verified handoff contract.
"""


def save_args(source: Path, thread: str) -> SimpleNamespace:
    return SimpleNamespace(
        from_temp=False, source=str(source), thread=thread, status="ready",
        hint="Resume the fixture", unfinished="", branch=None, slug=thread,
        date=None, json=False, pin=True, overwrite=False, new_thread=True,
    )


def check_handoff_identity(tmp: Path) -> list[str]:
    repo = tmp / "handoff-repo"
    init_repo(repo)
    (repo / "core.txt").write_text("core\n", encoding="utf-8")
    run(["git", "add", "core.txt"], repo)
    run(["git", "commit", "-m", "core"], repo)
    source_dir = repo / ".tmp"
    source_dir.mkdir()
    alex = source_dir / "alex.md"
    alex.write_text(handoff_text("alex-closeout"), encoding="utf-8")

    original = {
        "ROOT": handoff_store.ROOT, "STORE": handoff_store.STORE,
        "ARCHIVE": handoff_store.ARCHIVE, "INDEX": handoff_store.INDEX,
        "LATEST": handoff_store.LATEST,
    }
    handoff_store.ROOT = repo
    handoff_store.STORE = repo / ".agent" / "handoffs"
    handoff_store.ARCHIVE = handoff_store.STORE / "archive"
    handoff_store.INDEX = handoff_store.STORE / "index.md"
    handoff_store.LATEST = handoff_store.STORE / "LATEST.md"
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            require(handoff_store.cmd_save(save_args(alex, "alex-closeout")) == 0,
                    "explicit source save should pass")
        verified = handoff_store.verify_handoff("alex-closeout", alex)
        require(verified["valid"], f"exact source verification failed: {verified['errors']}")
        stored = Path(verified["stored_path"])

        angle = source_dir / "angle.md"
        angle.write_text(handoff_text("angle-map", "Content: Angle Map - Closed"), encoding="utf-8")
        with contextlib.redirect_stdout(io.StringIO()):
            require(handoff_store.cmd_save(save_args(angle, "angle-map")) == 0,
                    "unrelated handoff save should pass")
        time.sleep(0.01)
        angle.touch()
        resolved, detail = spine.resolve_content_source(False, stored)
        require(resolved is not None and resolved["thread"] == "alex-closeout",
                f"exact spine source was hijacked: {detail}")

        original_alex = alex.read_text(encoding="utf-8")
        alex.write_text(original_alex.replace("System: Fixture - Verified", "System: Wrong - Title"), encoding="utf-8")
        mismatch = handoff_store.verify_handoff("alex-closeout", alex)
        require(not mismatch["valid"] and not mismatch["checks"]["title"],
                "title/body mismatch should fail")
        alex.write_text(original_alex, encoding="utf-8")

        run(["git", "switch", "-c", "codex/other"], repo)
        branch_mismatch = handoff_store.verify_handoff("alex-closeout", alex)
        require(not branch_mismatch["valid"] and not branch_mismatch["checks"]["branch"],
                "branch mismatch should fail")
    finally:
        for key, value in original.items():
            setattr(handoff_store, key, value)

    candidates = tmp / "temp-handoffs"
    candidates.mkdir()
    (candidates / "handoff-alex-closeout.md").write_text("alex", encoding="utf-8")
    time.sleep(0.01)
    (candidates / "handoff-angle-map.md").write_text("angle", encoding="utf-8")
    old_tempdir = tempfile.tempdir
    tempfile.tempdir = str(candidates)
    try:
        selected, reason = handoff_store._newest_temp("alex-closeout")
        require(selected is not None and "alex-closeout" in selected.name and reason == "thread-filtered",
                "thread-filtered temp lookup selected the wrong handoff")
        ambiguous, _reason = handoff_store._newest_temp()
        require(ambiguous is None, "unscoped --from-temp should refuse multiple candidates")
    finally:
        tempfile.tempdir = old_tempdir
    return [
        "explicit source save and semantic verification pass",
        "exact spine source defeats newer unrelated handoff",
        "title, body, and branch mismatches fail",
        "from-temp filters by thread and refuses unscoped ambiguity",
    ]


def make_linked_fixture(tmp: Path) -> tuple[Path, Path]:
    source = tmp / "source-repo"
    init_repo(source, "main")
    linked = tmp / "linked"
    run(["git", "worktree", "add", "-b", "codex/fixture", str(linked), "main"], source)
    return source, linked


def manifest_for(project: Path, source: Path, status: str = "ready") -> dict:
    return {
        "schema_version": codex_close.SCHEMA,
        "task_id": "fixture-task",
        "title": "System: Codex Closeout - Verified",
        "slug": "codex-closeout-fixture",
        "status": status,
        "project_root": str(project),
        "handoff_source": str(source),
        "core_paths": ["core.txt"],
        "task_owned_paths": [source.relative_to(project).as_posix()],
    }


def check_manifest_and_policy(tmp: Path) -> list[str]:
    _source, linked = make_linked_fixture(tmp)
    (linked / "core.txt").write_text("core\n", encoding="utf-8")
    run(["git", "add", "core.txt"], linked)
    run(["git", "commit", "-m", "core"], linked)
    handoff = linked / "handoff.md"
    handoff.write_text(
        handoff_text("codex-closeout-fixture", "System: Codex Closeout - Verified"),
        encoding="utf-8",
    )
    manifest_path = tmp / "manifest.json"
    manifest_path.write_text(json.dumps(manifest_for(linked, handoff)), encoding="utf-8")
    manifest = codex_close.load_manifest(manifest_path)
    wrong_title = manifest_for(linked, handoff)
    wrong_title["title"] = "System: Wrong Task - Verified"
    wrong_title_path = tmp / "wrong-title.json"
    wrong_title_path.write_text(json.dumps(wrong_title), encoding="utf-8")
    try:
        codex_close.load_manifest(wrong_title_path)
    except codex_close.CloseoutError as exc:
        require("handoff title does not match manifest title" in str(exc),
                "manifest and handoff title mismatch should fail")
    else:
        raise AssertionError("manifest and handoff title mismatch unexpectedly passed")

    wrong_core = manifest_for(linked, handoff)
    extra = linked / "extra.txt"
    extra.write_text("extra\n", encoding="utf-8")
    wrong_core["core_paths"] = ["extra.txt"]
    wrong_core_path = tmp / "wrong-core.json"
    wrong_core_path.write_text(json.dumps(wrong_core), encoding="utf-8")
    try:
        codex_close.load_manifest(wrong_core_path)
    except codex_close.CloseoutError as exc:
        require("handoff core paths do not match manifest core paths" in str(exc),
                "manifest and handoff core path mismatch should fail")
    else:
        raise AssertionError("manifest and handoff core path mismatch unexpectedly passed")
    extra.unlink()
    context = codex_close.git_context(linked)
    blockers = codex_close.git_policy_blockers(manifest, context, context["status"])
    require(not blockers, f"dedicated codex worktree should pass policy: {blockers}")
    dry = codex_close.coordinate(manifest, True)
    require(dry["valid"] and dry["git"]["status"] == "dry-run",
            f"cold-start dry run should pass: {dry['git']}")

    main_context = dict(context, branch="main", dedicated_worktree=False)
    main_blockers = codex_close.git_policy_blockers(manifest, main_context, context["status"])
    require(any("main" in item for item in main_blockers), "main must be blocked")
    dirty = dict(context["status"])
    dirty["unrelated.txt"] = " M"
    dirty_blockers = codex_close.git_policy_blockers(manifest, context, dirty)
    require(any("not task-owned" in item for item in dirty_blockers), "unowned dirty path must block")
    retry_dirty = dict(context["status"])
    retry_dirty[".agent/handoffs/2026-08-01-codex-closeout-fixture.md"] = "??"
    retry_dirty[".agent/handoffs/index.md"] = " M"
    retry_blockers = codex_close.git_policy_blockers(manifest, context, retry_dirty)
    require(not retry_blockers, f"recognized retry receipts should remain stageable: {retry_blockers}")
    behind_blockers = codex_close.git_policy_blockers(manifest, dict(context, behind=1), context["status"])
    require(any("remote branch" in item for item in behind_blockers), "remote divergence must block")
    deletion_blockers = codex_close.git_policy_blockers(
        manifest, context, {handoff.name: " D"},
    )
    require(any("deletions" in item for item in deletion_blockers), "deletion must block")

    ready_actions = codex_close.task_actions_for("ready", manifest["title"], True, False)
    done_actions = codex_close.task_actions_for("done", manifest["title"], True, False)
    failed_done = codex_close.task_actions_for("done", manifest["title"], False, False)
    require(ready_actions["pin"] and not ready_actions["archive"], "ready task lifecycle incorrect")
    require(done_actions["archive"] and not done_actions["pin"], "verified done task should archive")
    require(not failed_done["archive"], "failed done task must remain unarchived")
    return [
        "manifest identity and dedicated-worktree cold start pass",
        "main, unowned dirt, divergence, and deletion states block Git",
        "ready tasks pin; only verified done tasks archive",
    ]


def check_local_push(tmp: Path) -> list[str]:
    tmp.mkdir(parents=True, exist_ok=True)
    remote = tmp / "origin.git"
    run(["git", "init", "--bare", str(remote)], tmp)
    base = tmp / "push-base"
    run(["git", "clone", str(remote), str(base)], tmp)
    run(["git", "config", "user.name", "Codex Test"], base)
    run(["git", "config", "user.email", "codex-test@example.invalid"], base)
    run(["git", "switch", "-c", "main"], base)
    (base / "README.md").write_text("base\n", encoding="utf-8")
    run(["git", "add", "README.md"], base)
    run(["git", "commit", "-m", "base"], base)
    run(["git", "push", "-u", "origin", "main"], base)
    linked = tmp / "push-linked"
    run(["git", "worktree", "add", "-b", "codex/push-fixture", str(linked), "main"], base)
    (linked / "feature.txt").write_text("safe fixture\n", encoding="utf-8")
    manifest = {
        "slug": "push-fixture", "project_root": str(linked),
        "commit_message": "test: codex end-session push fixture",
    }
    receipt = codex_close.commit_and_push(
        manifest, ["feature.txt"],
        [{"valid": True, "command": ["fixture"], "summary": "PASS"}],
    )
    require(receipt["status"] == "pushed", f"local remote push failed: {receipt}")
    require(receipt["commit"] == receipt["remote_sha"], "remote SHA must match local commit")
    main_sha = run(["git", "rev-parse", "main"], base)
    require(main_sha != receipt["commit"], "Codex branch push must not move main")
    return ["owned-path commit pushes codex branch and verifies remote SHA without moving main"]


def check_organization(tmp: Path) -> list[str]:
    tmp.mkdir(parents=True, exist_ok=True)
    loose = tmp / "loose-report.md"
    loose.write_text("report\n", encoding="utf-8")
    manifest = {
        "project_root": str(tmp),
        "slug": "organization-fixture",
        "task_owned_paths": ["loose-report.md", "outputs/organization-fixture/report.md"],
        "artifact_moves": [{
            "source": "loose-report.md",
            "destination": "outputs/organization-fixture/report.md",
        }],
    }
    dry = codex_close.organize_task_artifacts(manifest, True)
    require(loose.exists() and dry["status"] == "dry-run", "organization dry-run mutated source")
    applied = codex_close.organize_task_artifacts(manifest, False)
    destination = tmp / "outputs" / "organization-fixture" / "report.md"
    require(destination.exists() and not loose.exists(), "explicit owned artifact move failed")
    require(not applied["review"], f"explicit move should not require review: {applied}")
    unscoped = {
        "project_root": str(tmp), "slug": "organization-fixture",
        "task_owned_paths": ["uncertain.md"], "artifact_moves": [],
    }
    (tmp / "uncertain.md").write_text("uncertain\n", encoding="utf-8")
    uncertain = codex_close.organize_task_artifacts(unscoped, True)
    require(uncertain["review"], "loose artifact without an explicit destination must be queued")
    require(codex_close.is_closeout_generated(
        ".agent/handoffs/2026-08-01-organization-fixture.md", "organization-fixture"
    ), "known handoff receipt should be recognized")
    require(codex_close.is_closeout_generated(
        ".agent/recurring-reports/2026-08-01T120000-session-closeout-intelligence.md",
        "organization-fixture",
    ), "same-day closeout report should be recognized")
    require(not codex_close.is_closeout_generated(
        ".agent/recurring-reports/archive/2026-07-01T120000-session-closeout-intelligence.md",
        "organization-fixture",
    ), "archived reports must not be treated as current closeout receipts")
    require(not codex_close.is_closeout_generated(
        "execution/unrelated_generated.py", "organization-fixture"
    ), "unrelated generated path must not be recognized as closeout-owned")
    self_heal = (ROOT / "execution" / "self_heal.py").read_text(encoding="utf-8")
    require('"--no-cache" not in sys.argv' in self_heal,
            "Codex self-heal review requires a non-mutating report mode")
    commands = codex_close.default_verifiers(ROOT)
    require(any("--section" in row and "end-session" in row for row in commands),
            "Codex Git gate must use the scoped End-session control-plane verifier")
    return ["explicit owned artifact moves apply; uncertain files queue for review"]


def main() -> int:
    receipts: list[str] = []
    with tempfile.TemporaryDirectory(prefix="verify-codex-end-session-") as raw:
        tmp = Path(raw)
        receipts.extend(check_handoff_identity(tmp / "identity"))
        receipts.extend(check_manifest_and_policy(tmp / "policy"))
        receipts.extend(check_organization(tmp / "organization"))
        receipts.extend(check_local_push(tmp / "push"))
    print("CODEX END-SESSION VERIFICATION PASS")
    for receipt in receipts:
        print(f"- {receipt}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
