"""jen_os_page.py reads the run folder, never a hand-edited table (IMPORT-LIST.md #1, 2026-09-09).

Pins:
  - the generator has no POSTS / MEMOS / HERS / OTHER tables left in its source
  - it builds a page from a synthetic tree holding only run.yaml + pipeline-log.md + the assets file
    (no thumbs at all) and every post id, hook, receipt and gate verdict from those files appears
  - the sabotage twin: delete one receipt line → the page shows `gate fail` for that week
  - a week folder without run.yaml is ignored, not crashed on
"""
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))
import run_log as rl  # noqa: E402

SRC = ROOT / "execution" / "jen_os_page.py"
JEN = ["LOAD", "READ", "RESEARCH", "WRITE", "AMPLIFY", "CHECK", "RENDER", "DELIVER", "LEARN"]


def test_no_hand_edited_post_tables_remain():
    src = SRC.read_text()
    for name in ("POSTS = [", "MEMOS = [", "HERS = [", "OTHER = [", "POOL_USED = {"):
        assert name not in src, f"{name} is back in jen_os_page.py; the run folder is the state"
    assert "run_log" in src and "run.yaml" in src


def _tree(tmp_path: Path, weeks: int = 2, break_week: str | None = None) -> Path:
    """A fake lane: execution/ (real scripts copied), the Jen deliverables tree with run.yaml + logs, the assets file."""
    lane = tmp_path / "lane"
    (lane / "execution").mkdir(parents=True)
    for f in ("jen_os_page.py", "run_log.py"):
        (lane / "execution" / f).write_text((ROOT / "execution" / f).read_text())
    jen = lane / "_active/clients/jen-listings"
    weeks_dir = jen / "04-deliverables/2026-09-06-engine-v2-weeks-1-2"
    (weeks_dir / "reels").mkdir(parents=True)
    (jen / "06-system/pulse").mkdir(parents=True)
    (jen / "06-system/pulse/latest.md").write_text("# pulse · @_jiing · 2026-09-02\n\nmedian views **2,642**\n")
    (weeks_dir / "FACTS.md").write_text("| used in | claim |\n|---|---|\n| 04 | a |\n| 05 | b |\n")
    assets = {"schema": "valley-os-assets/1",
              "memos": [{"memo": "1", "lines": "x", "where": "y", "state": "used"}],
              "photos": [{"file": "jen-headshot-studio", "what": "headshot", "used": "Edition 01"},
                         {"file": "listing-home-gym-pool", "what": "gym", "used": "none: would mislead"}],
              "pool": [{"file": "valley-street-01", "used": "posts 01"}],
              "other": [{"asset": "Stories", "state": "none", "note": "zero"}]}
    (jen / "06-system/VALLEY-OS-ASSETS.yaml").write_text(rl.dump(assets))
    for i in range(weeks):
        w = weeks_dir / f"week-of-2026-09-{7 + 7 * i:02d}"
        w.mkdir()
        (w / "saved-replies.txt").write_text("1 · hi\n")
        rl.write_manifest(w, {"brand": "jen", "door": "jen", "kind": "week", "label": f"Week {i + 1}",
                              "message": f"msg {i + 1}: with a colon",
                              "posts": [{"id": f"0{i}-post", "district": "attract", "format": "reel", "format_note": "reel · 20 s",
                                         "day": "tue · 7:30am", "hook": f"hook {i + 1}: opens on you", "thumb": f"0{i}-post-cover",
                                         "slides": 0, "photos": ["valley-street-01"], "photo_source": "placeholder",
                                         "caption": "cap\n\n#tag", "reply": "a zip → saved reply 3"}]},
                         steps=JEN)
        for s in JEN:
            if break_week == w.name and s == "CHECK":
                continue
            rl.receipt(w, s, f"{s} receipt {i + 1}", reason="why")
    (weeks_dir / "week-of-2026-10-05").mkdir()   # a folder with no run.yaml: must be ignored
    return lane


def _build(lane: Path, tmp_path: Path) -> str:
    thumbs = tmp_path / "thumbs"
    thumbs.mkdir(exist_ok=True)
    out = tmp_path / "page.html"
    r = subprocess.run(["python3", str(lane / "execution" / "jen_os_page.py"), str(thumbs), str(out)],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return out.read_text()


def test_page_is_built_from_run_yaml_and_receipts_only(tmp_path):
    lane = _tree(tmp_path)
    html = _build(lane, tmp_path)
    for needle in ("00-post", "01-post", "hook 1: opens on you", "hook 2: opens on you", "Week 1", "Week 2",
                   "msg 2: with a colon", "AMPLIFY receipt 1", "LEARN receipt 2", "gate pass", "2 weeks",
                   "1 / 2", "Edition 01", "would mislead"):
        assert needle in html, needle
    assert "week-of-2026-10-05" not in html
    assert html.count('class="post"') == 2
    assert ">gate fail<" not in html


def test_sabotage_missing_receipt_shows_gate_fail(tmp_path):
    lane = _tree(tmp_path, break_week="week-of-2026-09-14")
    html = _build(lane, tmp_path)
    assert "gate fail" in html and "missing receipt(s) CHECK" in html
    assert html.count(">gate pass<") == 1


def test_real_tree_builds_and_week_2_carries_its_receipts(tmp_path):
    """Integration on the real deliverables tree (skipped if it is not on this checkout)."""
    weeks = ROOT / "_active/clients/jen-listings/04-deliverables/2026-09-06-engine-v2-weeks-1-2"
    if not (weeks / "week-of-2026-09-14" / "run.yaml").exists():
        pytest.skip("real Jen tree not present")
    thumbs = tmp_path / "t"
    thumbs.mkdir()
    out = tmp_path / "real.html"
    r = subprocess.run(["python3", str(SRC), str(thumbs), str(out)], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    html = out.read_text()
    data = rl.load(weeks / "week-of-2026-09-14" / "run.yaml")
    for p in data["posts"]:
        assert p["id"] in html and p["hook"] in html
    assert "AMPLIFY" in html
