"""run_log.py: sabotage tests both directions (IMPORT-LIST.md #1, 2026-09-09).

Pins:
  - a receipt APPENDS; a second receipt never overwrites the first
  - a skipped step is recorded as `skipped (why)`, never silence
  - the manifest merges (a second write keeps the first write's keys)
  - the manifest write is atomic (a crash before rename leaves the old file intact)
  - the YAML subset the writer emits round-trips through BOTH readers
    (PyYAML and the built-in subset parser) to the same dict, captions included
  - `check` FAILS when a receipt is missing, when receipts are out of order,
    or when a required manifest key is absent, and PASSES once repaired
  - the sabotage twin: a naive in-place manifest write that dies mid-write
    leaves a half file, and `check` catches it (proves the gate is not vacuous)
  - the CLI works under bare `python3` with the same commands the doors use
"""
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

import run_log as rl  # noqa: E402

JEN = ["LOAD", "READ", "RESEARCH", "WRITE", "AMPLIFY", "CHECK", "RENDER", "DELIVER", "LEARN"]


def _manifest(run: Path, **extra):
    base = {"brand": "jen", "door": "jen", "kind": "week", "status": "draft"}
    base.update(extra)
    return rl.write_manifest(run, base, steps=JEN)


# ── receipts ────────────────────────────────────────────────────────────
def test_receipt_appends_never_overwrites(tmp_path):
    run = tmp_path / "week-of-2026-09-14"
    rl.receipt(run, "LOAD", "8/8 · voice source = jen-real-voice-profile.md", door="jen",
               brand_lock="BRAND LOCK: jen")
    rl.receipt(run, "READ", "slots = attract / position / attract", reason="CONTENT-MIX shares")
    text = (run / "pipeline-log.md").read_text()
    assert text.startswith("# pipeline-log · week-of-2026-09-14 · jen")
    assert "BRAND LOCK: jen" in text
    rec = rl.read_receipts(run)
    assert [r["step"] for r in rec] == ["LOAD", "READ"]
    assert rec[1]["reason"] == "CONTENT-MIX shares"
    assert not rec[0]["skipped"]


def test_skipped_step_is_recorded_not_silent(tmp_path):
    run = tmp_path / "r"
    rl.receipt(run, "RESEARCH", "no new claims this week", skip=True)
    rec = rl.read_receipts(run)
    assert rec[0]["skipped"] and rec[0]["text"] == "skipped (no new claims this week)"


# ── manifest ────────────────────────────────────────────────────────────
def test_manifest_merges_and_orders_required_keys_first(tmp_path):
    run = tmp_path / "week-of-2026-09-14"
    _manifest(run, label="Week 2")
    rl.write_manifest(run, {"status": "delivered", "cost_usd": 0})
    data = rl.load(run / "run.yaml")
    assert data["label"] == "Week 2"           # first write survived the second
    assert data["status"] == "delivered"       # second write won on the shared key
    assert data["steps"] == JEN
    keys = list(data)
    assert keys[: len(rl.REQUIRED_KEYS)] == list(rl.REQUIRED_KEYS)


def test_manifest_write_is_atomic(tmp_path, monkeypatch):
    run = tmp_path / "r"
    _manifest(run, label="first")
    before = (run / "run.yaml").read_text()

    def boom(self, target):
        raise OSError("simulated crash before rename")

    monkeypatch.setattr(Path, "replace", boom)
    with pytest.raises(OSError):
        rl.write_manifest(run, {"label": "second"})
    assert (run / "run.yaml").read_text() == before


def test_naive_in_place_write_is_caught_by_check(tmp_path):
    """The sabotage twin: prove `check` is not vacuous by handing it a half file."""
    run = tmp_path / "r"
    _manifest(run)
    for s in JEN:
        rl.receipt(run, s, "ok")
    ok, _ = rl.check(run)
    assert ok
    full = (run / "run.yaml").read_text()
    (run / "run.yaml").write_text(full[: len(full) // 3])   # a crash mid in-place write
    ok, problems = rl.check(run)
    assert not ok and any("missing key" in p for p in problems)


# ── the YAML subset ─────────────────────────────────────────────────────
SAMPLE = {
    "schema": rl.SCHEMA, "brand": "jen", "door": "jen", "run": "week-of-2026-09-14", "kind": "week",
    "status": "draft", "built": "2026-09-09", "cost_usd": 0, "label": "Week 2 · drop Sun Sept 13",
    "brand_lock": "BRAND LOCK: jen (client) · brand_context=_active/clients/jen-listings/brand_context",
    "message": "week 2 is in the folder: three posts, tue / thu / sat.\nreply here if a line isn't you 🤍",
    "empty": None, "flag": True, "ratio": 0.75,
    "posts": [
        {"id": "04-attract-900k-two-zips", "district": "attract", "format": "reel", "secs": 23.0,
         "day": "tue sept 15 · 7:30am",
         "hook": "$900K in sherman oaks. $900K in van nuys. same week.",
         "caption": "line one: with a colon\n\nline three after a blank\n#tag",
         "photos": ["vannuys-blvd-2024", "jen-porch-vannuys"], "photo_source": "placeholder",
         "reply": "a zip or a number → saved reply 3. an address → saved reply 1."},
        {"id": "06-position-tarzana-median-sellers", "district": "position", "format": "card", "slides": 3,
         "hook": "tarzana sold for 14.5% less this july than last july.", "photos": [], "notes": {}},
    ],
    "steps": JEN,
}


def test_subset_roundtrip_matches_pyyaml():
    yaml = pytest.importorskip("yaml")
    text = rl.dump(SAMPLE)
    via_pyyaml = yaml.safe_load(text)
    via_subset = rl._load_subset(text)
    assert via_pyyaml == SAMPLE
    assert via_subset == SAMPLE


def test_subset_reader_is_the_fallback_when_pyyaml_is_absent(tmp_path, monkeypatch):
    p = tmp_path / "run.yaml"
    p.write_text(rl.dump(SAMPLE))
    real_import = __import__

    def no_yaml(name, *a, **k):
        if name == "yaml":
            raise ImportError("simulated: no PyYAML on this interpreter")
        return real_import(name, *a, **k)

    monkeypatch.setattr("builtins.__import__", no_yaml)
    assert rl.load(p) == SAMPLE


# ── the gate ────────────────────────────────────────────────────────────
def test_check_fails_on_missing_receipt_then_passes_when_repaired(tmp_path):
    run = tmp_path / "r"
    _manifest(run)
    for s in JEN:
        if s != "CHECK":
            rl.receipt(run, s, "ok")
    ok, problems = rl.check(run)
    assert not ok and any("missing receipt(s) CHECK" in p for p in problems)
    # repair: the log is append-only, so the repair lands out of order → still FAIL
    rl.receipt(run, "CHECK", "fair-housing PASS")
    ok, problems = rl.check(run)
    assert not ok and any("out of order" in p for p in problems)


def test_check_passes_in_order_and_accepts_skips(tmp_path):
    run = tmp_path / "r"
    _manifest(run)
    for s in JEN:
        rl.receipt(run, s, "not due on a Tuesday" if s == "LEARN" else "ok", skip=(s == "LEARN"))
    ok, problems = rl.check(run)
    assert ok, problems


def test_check_fails_on_missing_manifest_key(tmp_path):
    run = tmp_path / "r"
    rl.write_manifest(run, {"door": "jen", "kind": "week"}, steps=JEN)   # no brand
    for s in JEN:
        rl.receipt(run, s, "ok")
    ok, problems = rl.check(run)
    assert not ok and any("missing key `brand`" in p for p in problems)


def test_check_needs_a_step_list_for_an_unknown_door(tmp_path):
    run = tmp_path / "r"
    rl.write_manifest(run, {"brand": "farrice", "door": "social-carousel", "kind": "carousel"})
    ok, problems = rl.check(run)
    assert not ok and any("no step list" in p for p in problems)
    rl.receipt(run, "LOCK", "ok")
    rl.receipt(run, "RENDER", "ok")
    ok, _ = rl.check(run, steps=["LOCK", "RENDER"])
    assert ok


# ── the CLI, bare python3, the same lines the doors use ────────────────
def test_cli_end_to_end_under_bare_python3(tmp_path):
    run = tmp_path / "week-of-2026-09-14"
    script = str(ROOT / "execution" / "run_log.py")

    def sh(*args):
        return subprocess.run(["python3", script, *args], capture_output=True, text=True)

    r = sh("manifest", str(run), "--set", "brand=jen", "--set", "door=jen", "--set", "kind=week",
           "--set", "cost_usd=0", "--steps", ",".join(JEN))
    assert r.returncode == 0, r.stderr
    for s in JEN:
        r = sh("receipt", str(run), s, f"{s} ok", "--reason", "test")
        assert r.returncode == 0 and r.stdout.startswith("- ")
    posts = tmp_path / "posts.json"
    posts.write_text(json.dumps({"posts": [{"id": "x", "hook": "y: z"}], "status": "delivered"}))
    assert sh("manifest", str(run), "--from-json", str(posts)).returncode == 0
    r = sh("check", str(run))
    assert r.returncode == 0 and "PASS" in r.stdout, r.stdout
    data = rl.load(run / "run.yaml")
    assert data["posts"][0]["hook"] == "y: z" and data["status"] == "delivered" and data["cost_usd"] == 0
    r = sh("status", str(run))
    assert "gate=PASS" in r.stdout and "LOAD → READ" in r.stdout
