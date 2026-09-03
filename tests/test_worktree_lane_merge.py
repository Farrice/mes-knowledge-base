"""worktree_lane.py merge + preserve — regression tests (verification spine).

Scar 2026-09-02: main sat mid-merge (MERGE_HEAD + 40 UU files) after a lane
PARKED on conflicts; every other lane then parked on it for hours. The tool
ran `git merge --abort` but never checked it. These tests pin:
  - a conflict PARK leaves NO MERGE_HEAD on main
  - a crash inside the merge body still aborts and parks (never a traceback
    with main half-merged)
  - a pre-existing foreign MERGE_HEAD is refused, never stacked
  - `preserve` moves human work off main loss-free (Law 3) and leaves
    untracked files alone

Sabotage record (run once during the build, 2026-09-02): with `_abort_merge`
replaced by a no-op, test_conflict_park_leaves_main_clean and
test_crash_inside_merge_body_still_aborts FAIL; restored, all pass.
"""
import json
import subprocess
import sys
import types
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

import worktree_lane as wl  # noqa: E402


def git(cwd, *args):
    return subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True)


def _commit_all(cwd, msg):
    git(cwd, "add", "-A")
    r = git(cwd, "commit", "-q", "-m", msg)
    assert r.returncode == 0, r.stderr


@pytest.fixture
def repo(tmp_path, monkeypatch):
    """main + one lane worktree, both with a shared history and a bare origin."""
    main = tmp_path / "main"
    main.mkdir()
    git(main, "init", "-q", "-b", "main")
    git(main, "config", "user.email", "t@t")
    git(main, "config", "user.name", "t")
    (main / "doc.md").write_text("line 1\nline 2\n")
    (main / "other.md").write_text("o\n")
    (main / ".gitignore").write_text(".agent/lanes.json\n.agent/lane-merge.lock\n.claude/worktrees/\n")
    (main / ".agent").mkdir()
    _commit_all(main, "init")
    origin = tmp_path / "origin.git"
    git(tmp_path, "init", "-q", "--bare", str(origin))
    git(main, "remote", "add", "origin", str(origin))
    git(main, "push", "-q", "-u", "origin", "main")
    lane = tmp_path / "lane"
    git(main, "worktree", "add", "-q", str(lane), "-b", "worktree-t")
    git(lane, "config", "user.email", "t@t")
    git(lane, "config", "user.name", "t")
    # no session-lock noise, no auto-push hooks
    monkeypatch.setattr(wl, "fresh_main_writer", lambda *a, **k: None)
    monkeypatch.setattr(wl, "GENERATORS", [])
    return types.SimpleNamespace(main=main, lane=lane, branch="worktree-t")


def merge_args(branch, **kw):
    base = dict(lane=branch, no_teardown=True, no_push=True, dry_run=False,
                lock_token=None, exclude_session=None)
    base.update(kw)
    return types.SimpleNamespace(**base)


def _conflict(repo):
    (repo.lane / "doc.md").write_text("LANE line 1\nline 2\n")
    _commit_all(repo.lane, "lane edit")
    (repo.main / "doc.md").write_text("MAIN line 1\nline 2\n")
    _commit_all(repo.main, "main edit")


def _mid_merge(main):
    return git(main, "rev-parse", "-q", "--verify", "MERGE_HEAD").returncode == 0


def run_merge(repo, monkeypatch, **kw):
    monkeypatch.chdir(repo.lane)
    monkeypatch.setattr(wl, "main_root", lambda cwd=None: repo.main)
    return wl.cmd_merge(merge_args(repo.branch, **kw))


def test_conflict_park_leaves_main_clean(repo, monkeypatch):
    _conflict(repo)
    rc = run_merge(repo, monkeypatch)
    assert rc == 0
    assert not _mid_merge(repo.main), "main left mid-merge after a PARK"
    reg = json.loads((repo.main / ".agent" / "lanes.json").read_text())
    entry = reg[repo.branch]
    assert entry["status"] == "parked"
    assert entry["reason"].startswith("conflict in doc.md")
    assert "merge_in_flight" not in entry
    assert git(repo.main, "status", "--porcelain").stdout.strip() == ""


def test_abort_failure_is_surfaced_not_swallowed(repo, monkeypatch):
    _conflict(repo)
    real_git = wl._git

    def flaky(cwd, *args, **kw):
        if args[:2] == ("merge", "--abort"):
            return 1, "", "simulated abort failure"
        return real_git(cwd, *args, **kw)

    monkeypatch.setattr(wl, "_git", flaky)
    run_merge(repo, monkeypatch)
    # fallback `reset --merge` must have concluded it
    assert not _mid_merge(repo.main)
    reg = json.loads((repo.main / ".agent" / "lanes.json").read_text())
    assert reg[repo.branch]["status"] == "parked"


def test_abort_and_fallback_both_failing_is_loud(repo, monkeypatch, capsys):
    _conflict(repo)
    real_git = wl._git

    def dead(cwd, *args, **kw):
        if args[:2] in (("merge", "--abort"), ("reset", "--merge")):
            return 1, "", "simulated"
        return real_git(cwd, *args, **kw)

    monkeypatch.setattr(wl, "_git", dead)
    run_merge(repo, monkeypatch)
    reg = json.loads((repo.main / ".agent" / "lanes.json").read_text())
    assert "abort failed" in reg[repo.branch]["reason"]
    assert "MAIN MID-MERGE" in capsys.readouterr().err
    # clean up the deliberately stranded merge so the tmp repo can be deleted
    git(repo.main, "merge", "--abort")


def test_crash_inside_merge_body_still_aborts(repo, monkeypatch):
    _conflict(repo)

    def boom(*a, **k):
        raise RuntimeError("simulated crash in conflict resolution")

    monkeypatch.setattr(wl, "_theirs_is_stale", boom)
    rc = run_merge(repo, monkeypatch)
    assert rc == 0
    assert not _mid_merge(repo.main)
    reg = json.loads((repo.main / ".agent" / "lanes.json").read_text())
    assert reg[repo.branch]["reason"].startswith("merge crashed: RuntimeError")


def test_foreign_mid_merge_is_refused_not_stacked(repo, monkeypatch):
    # a third branch conflicts with main and is left mid-merge by a "foreign actor"
    git(repo.main, "branch", "foreign")
    foreign = repo.main.parent / "foreign"
    git(repo.main, "worktree", "add", "-q", str(foreign), "foreign")
    (foreign / "other.md").write_text("F\n")
    _commit_all(foreign, "foreign edit")
    (repo.main / "other.md").write_text("M\n")
    _commit_all(repo.main, "main other")
    git(repo.main, "merge", "foreign")
    assert _mid_merge(repo.main)
    (repo.lane / "doc.md").write_text("clean lane change\nline 2\n")
    _commit_all(repo.lane, "lane clean")
    # the dirty-tree gate would park first; bypass it to reach the pre-flight
    real_git = wl._git

    def hide_dirty(cwd, *args, **kw):
        if args == ("status", "--porcelain") and Path(cwd) == repo.main:
            return 0, "", ""
        return real_git(cwd, *args, **kw)

    monkeypatch.setattr(wl, "_git", hide_dirty)
    run_merge(repo, monkeypatch)
    reg = json.loads((repo.main / ".agent" / "lanes.json").read_text())
    assert reg[repo.branch]["reason"].startswith("main already mid-merge")
    assert _mid_merge(repo.main), "tool must not touch a foreign actor's merge"
    git(repo.main, "merge", "--abort")


def test_clean_merge_clears_in_flight_marker(repo, monkeypatch):
    (repo.lane / "new.md").write_text("n\n")
    _commit_all(repo.lane, "lane add")
    rc = run_merge(repo, monkeypatch)
    assert rc == 0
    assert (repo.main / "new.md").exists()
    reg = json.loads((repo.main / ".agent" / "lanes.json").read_text())
    assert "merge_in_flight" not in reg.get(repo.branch, {})
    assert not _mid_merge(repo.main)


def test_preserve_moves_tracked_work_off_main_loss_free(repo, monkeypatch):
    # staged new file, unstaged edit, staged deletion, untracked scratch
    (repo.main / "deliverable.md").write_text("human work\n")
    git(repo.main, "add", "deliverable.md")
    (repo.main / "doc.md").write_text("edited on main\n")
    git(repo.main, "rm", "-q", "other.md")
    (repo.main / "scratch.txt").write_text("untracked\n")
    monkeypatch.chdir(repo.main)
    monkeypatch.setattr(wl, "main_root", lambda cwd=None: repo.main)
    args = types.SimpleNamespace(slug="Test Slug", dry_run=False, push=False, lock_token=None)
    assert wl.cmd_preserve(args) == 0
    status = git(repo.main, "status", "--porcelain").stdout.splitlines()
    assert status == ["?? scratch.txt"], status
    reg = json.loads((repo.main / ".agent" / "lanes.json").read_text())
    branch = next(b for b in reg if b.startswith("worktree-main-dirty-preserve-"))
    assert branch.endswith("-test-slug")
    lane = Path(reg[branch]["path"])
    assert (lane / "deliverable.md").read_text() == "human work\n"
    assert (lane / "doc.md").read_text() == "edited on main\n"
    assert not (lane / "other.md").exists()
    show = git(lane, "show", "--stat", "--name-only", "HEAD").stdout
    for rel in ("deliverable.md", "doc.md", "other.md"):
        assert rel in show
    assert (repo.main / "other.md").exists(), "main restored to HEAD, not to the lane"
    assert wl.cmd_preserve(types.SimpleNamespace(slug="again", dry_run=True, push=False,
                                                 lock_token=None)) == 0


def test_preserve_refuses_when_main_mid_merge(repo, monkeypatch, capsys):
    _conflict(repo)
    git(repo.main, "merge", repo.branch)
    assert _mid_merge(repo.main)
    monkeypatch.chdir(repo.main)
    monkeypatch.setattr(wl, "main_root", lambda cwd=None: repo.main)
    rc = wl.cmd_preserve(types.SimpleNamespace(slug=None, dry_run=False, push=False, lock_token=None))
    assert rc == 1
    assert "mid-merge" in capsys.readouterr().err
    git(repo.main, "merge", "--abort")
