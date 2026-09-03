"""Studio Preview wrapper — sabotage tests both directions.

Pins (2026-09-03):
  - GET / lists every template in the pool; each PNG is served as image/png
  - a comment lands in <template>/comments.json in the VENDOR shape
    (id / xPct / yPct / zone / text, keyed by the template or slide id) and a
    second comment APPENDS — the sabotage twin that overwrites is caught
  - Approve flips status + stamps approved_by / approved_on, and the
    scrapes_brand ready count goes up by one
  - Retire flips status, stores the reason, and strips the id from every
    styles.json list
  - the atomic write survives a crash before the rename; the naive in-place
    write does NOT — proving the manifest check is not vacuous
  - run mode keys comments by slide id at <run>/comments.json
"""
import json
import struct
import sys
import threading
import zlib
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

import scrapes_brand as sb  # noqa: E402
import studio_preview as sp  # noqa: E402

VENDOR_KEYS = {"id", "xPct", "yPct", "zone", "text"}


# ── fixtures ────────────────────────────────────────────────────────────
def _png_bytes(w: int, h: int) -> bytes:
    """A minimal valid PNG (grey) — no Pillow needed for the fixture."""
    raw = b"".join(b"\x00" + bytes([200, 200, 200]) * w for _ in range(h))

    def chunk(tag: bytes, data: bytes) -> bytes:
        return (struct.pack(">I", len(data)) + tag + data
                + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF))

    ihdr = struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0)
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr)
            + chunk(b"IDAT", zlib.compress(raw, 6)) + chunk(b"IEND", b""))


@pytest.fixture
def pool(tmp_path: Path) -> Path:
    d = tmp_path / "linkedin-carousel"
    (d / "_preview").mkdir(parents=True)
    (d / "t-alpha").mkdir()
    (d / "t-beta").mkdir()
    (d / "_preview" / "t-alpha.png").write_bytes(_png_bytes(8, 10))
    (d / "_preview" / "t-beta.png").write_bytes(_png_bytes(8, 10))
    (d / "manifest.json").write_text(json.dumps({
        "pool": "linkedin-carousel",
        "brand": "farrice",
        "templates": [
            {"id": "t-alpha", "file": "t-alpha/template.html", "role": "cover",
             "status": "draft", "style": "editorial", "needs": ["HEADLINE"], "optional": []},
            {"id": "t-beta", "file": "t-beta/template.html", "role": "body",
             "status": "ready", "style": "editorial", "needs": ["HEADLINE"], "optional": []},
        ],
        "styles_file": "styles.json",
    }, indent=2), encoding="utf-8")
    (d / "styles.json").write_text(json.dumps({
        "version": 1,
        "platform_pool": "linkedin-carousel",
        "styles": [
            {"name": "editorial", "template_ids": ["t-alpha", "t-beta"]},
            {"name": "typographic", "template_ids": ["t-beta"]},
        ],
    }, indent=2), encoding="utf-8")
    return d


@pytest.fixture
def run_dir(tmp_path: Path) -> Path:
    d = tmp_path / "blind-bar-test"
    d.mkdir()
    for n in (1, 2):
        (d / f"slide-0{n}.png").write_bytes(_png_bytes(8, 10))
        (d / f"slide-0{n}.data.json").write_text("{}", encoding="utf-8")
    (d / "manifest.json").write_text(json.dumps({
        "take": "T", "brand": "farrice",
        "slides": [
            {"n": 1, "template_id": "t-alpha", "path": "slide-01.png", "render_mode": "TEMPLATE"},
            {"n": 2, "template_id": "t-beta", "path": "slide-02.png", "render_mode": "TEMPLATE"},
        ],
    }, indent=2), encoding="utf-8")
    return d


class Live:
    def __init__(self, source):
        self.httpd = sp.build_server(source)
        self.base = f"http://127.0.0.1:{self.httpd.server_address[1]}"
        self.thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)
        self.thread.start()

    def get(self, path="/"):
        with urlopen(self.base + path) as r:
            return r.status, r.headers.get("Content-Type", ""), r.read()

    def post(self, path, payload):
        req = Request(self.base + path, data=json.dumps(payload).encode(),
                      headers={"Content-Type": "application/json"}, method="POST")
        try:
            with urlopen(req) as r:
                return r.status, json.loads(r.read())
        except HTTPError as e:
            return e.code, json.loads(e.read())

    def close(self):
        self.httpd.shutdown()
        self.httpd.server_close()


@pytest.fixture
def live_pool(pool):
    srv = Live(sp.PoolSource(pool))
    yield srv
    srv.close()


@pytest.fixture
def live_run(run_dir):
    srv = Live(sp.RunSource(run_dir))
    yield srv
    srv.close()


def _manifest(pool: Path) -> dict:
    return json.loads((pool / "manifest.json").read_text())


def _entry(pool: Path, tid: str) -> dict:
    return next(e for e in _manifest(pool)["templates"] if e["id"] == tid)


# ── page + assets ───────────────────────────────────────────────────────
def test_index_lists_every_template_in_both_frames(live_pool):
    status, ctype, body = live_pool.get("/")
    page = body.decode()
    assert status == 200 and ctype.startswith("text/html")
    assert "t-alpha" in page and "t-beta" in page
    # both platform frames, and the 4:5 box that guarantees the true crop
    assert page.count("LinkedIn · document post") == 2
    assert page.count("Instagram · carousel") == 2
    assert "aspect-ratio:4/5" in page
    # the header counts read off real statuses
    assert "1 ready" in page and "0 approved" in page


def test_each_png_is_served_with_the_right_content_type(live_pool, pool):
    for tid in ("t-alpha", "t-beta"):
        status, ctype, body = live_pool.get(f"/png/{tid}")
        assert status == 200
        assert ctype == "image/png"
        assert body == (pool / "_preview" / f"{tid}.png").read_bytes()


def test_unknown_png_is_404(live_pool):
    with pytest.raises(HTTPError) as exc:
        live_pool.get("/png/nope")
    assert exc.value.code == 404


# ── comments ────────────────────────────────────────────────────────────
def test_comment_writes_one_record_with_the_vendor_keys(live_pool, pool):
    code, res = live_pool.post("/comment", {"key": "t-alpha", "text": "kern the cover word"})
    assert code == 200 and res["ok"] is True
    data = json.loads((pool / "t-alpha" / "comments.json").read_text())
    assert list(data) == ["t-alpha"]          # keyed by the template id, vendor style
    assert len(data["t-alpha"]) == 1
    rec = data["t-alpha"][0]
    assert set(rec) == VENDOR_KEYS            # no invented keys, none missing
    assert rec["text"] == "kern the cover word"
    assert rec["zone"] is None
    assert rec["id"].startswith("c1-")
    assert sp.comment_time(rec)               # the id suffix decodes to a real time


def test_second_comment_appends_and_never_overwrites(live_pool, pool):
    live_pool.post("/comment", {"key": "t-alpha", "text": "first"})
    live_pool.post("/comment", {"key": "t-alpha", "text": "second"})
    bucket = json.loads((pool / "t-alpha" / "comments.json").read_text())["t-alpha"]
    assert [c["text"] for c in bucket] == ["first", "second"]
    assert bucket[0]["id"] != bucket[1]["id"]


def test_sabotage_an_overwriting_comment_writer_is_caught(pool, monkeypatch):
    """Direction 2: if append_comment overwrote instead of appending, the
    append assertion above must fail. Prove it does."""
    path = pool / "t-alpha" / "comments.json"

    def overwriting(comments_path, key, text):
        sp._write_json(comments_path, {key: [sp._vendor_comment(text, 1)]})
        return sp.read_comments(comments_path, key)

    monkeypatch.setattr(sp, "append_comment", overwriting)
    srv = Live(sp.PoolSource(pool))
    try:
        srv.post("/comment", {"key": "t-alpha", "text": "first"})
        srv.post("/comment", {"key": "t-alpha", "text": "second"})
    finally:
        srv.close()
    bucket = json.loads(path.read_text())["t-alpha"]
    assert [c["text"] for c in bucket] != ["first", "second"]   # the sabotage lands
    assert [c["text"] for c in bucket] == ["second"]            # first was lost


def test_empty_comment_is_refused(live_pool, pool):
    code, res = live_pool.post("/comment", {"key": "t-alpha", "text": "   "})
    assert code == 400 and res["ok"] is False
    assert not (pool / "t-alpha" / "comments.json").exists()


def test_run_mode_keys_comments_by_slide_id_at_the_run_root(live_run, run_dir):
    code, res = live_run.post("/comment", {"key": "slide-02", "text": "crop is tight"})
    assert code == 200
    data = json.loads((run_dir / "comments.json").read_text())
    assert list(data) == ["slide-02"]
    assert set(data["slide-02"][0]) == VENDOR_KEYS


def test_run_mode_refuses_approve(live_run):
    code, res = live_run.post("/approve", {"key": "slide-01"})
    assert code == 400 and res["ok"] is False


# ── approve ─────────────────────────────────────────────────────────────
def test_approve_flips_status_stamps_fields_and_lifts_the_ready_count(live_pool, pool):
    before, total = sb._pool_ready_count(pool)
    assert (before, total) == (1, 2)

    code, res = live_pool.post("/approve", {"key": "t-alpha"})
    assert code == 200 and res["status"] == "approved"

    e = _entry(pool, "t-alpha")
    assert e["status"] == "approved"
    assert e["approved_by"] == "Farrice"
    assert e["approved_on"] == sp.date.today().isoformat()

    after, _ = sb._pool_ready_count(pool)
    assert after == before + 1


# ── retire ──────────────────────────────────────────────────────────────
def test_retire_flips_status_stores_reason_and_strips_the_id_from_styles(live_pool, pool):
    code, res = live_pool.post("/retire", {"key": "t-beta", "reason": "boxed crop reads cheap"})
    assert code == 200 and res["status"] == "retired"

    e = _entry(pool, "t-beta")
    assert e["status"] == "retired"
    assert "boxed crop reads cheap" in e["retired_reason"]
    assert "approved_by" not in e and "approved_on" not in e

    styles = json.loads((pool / "styles.json").read_text())
    for style in styles["styles"]:
        assert "t-beta" not in style["template_ids"], style["name"]
    assert "t-alpha" in styles["styles"][0]["template_ids"]   # nothing else touched

    ready, _ = sb._pool_ready_count(pool)
    assert ready == 0


def test_retire_without_a_reason_is_refused(live_pool, pool):
    code, res = live_pool.post("/retire", {"key": "t-beta", "reason": "  "})
    assert code == 400 and res["ok"] is False
    assert _entry(pool, "t-beta")["status"] == "ready"


# ── atomic write, sabotaged both directions ─────────────────────────────
def test_atomic_write_survives_a_crash_before_the_rename(pool, monkeypatch):
    """Direction 1: the shipped write must leave the manifest whole."""
    src = sp.PoolSource(pool)

    def boom():
        raise RuntimeError("power cut mid-write")

    monkeypatch.setattr(sp, "_WRITE_INTERRUPT", boom)
    with pytest.raises(RuntimeError):
        src.set_status("t-alpha", "approved")

    data = json.loads((pool / "manifest.json").read_text())     # still parses
    assert _entry(pool, "t-alpha")["status"] == "draft"          # unchanged
    assert len(data["templates"]) == 2


def test_sabotage_a_naive_in_place_write_leaves_a_half_written_manifest(pool, monkeypatch):
    """Direction 2: swap in the non-atomic writer and confirm the check above
    would actually have caught it — otherwise that test proves nothing."""
    src = sp.PoolSource(pool)

    def boom():
        raise RuntimeError("power cut mid-write")

    monkeypatch.setattr(sp, "_WRITE_INTERRUPT", boom)

    def naive_json(path, data):
        sp._naive_write(path, json.dumps(data, indent=2) + "\n")

    with pytest.raises(RuntimeError):
        src.set_status("t-alpha", "approved", writer=naive_json)

    with pytest.raises(json.JSONDecodeError):
        json.loads((pool / "manifest.json").read_text())


def test_atomic_write_leaves_no_stray_temp_file(pool):
    src = sp.PoolSource(pool)
    src.set_status("t-alpha", "approved")
    strays = [p.name for p in pool.iterdir() if ".tmp-" in p.name]
    assert strays == []
    assert _entry(pool, "t-alpha")["status"] == "approved"
