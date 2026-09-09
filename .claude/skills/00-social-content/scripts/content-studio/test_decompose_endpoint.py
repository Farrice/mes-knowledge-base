#!/usr/bin/env python3
"""test_decompose_endpoint.py -- Tests for the Content Studio /decompose endpoint.

Verifies:
  1. POST /decompose on a full-AI slide with a stubbed-ok decompose.py returns
     ok:true + a layer list (paths + bboxes).
  2. POST /decompose when decompose.py returns the skipped stub (no FAL_KEY) →
     {ok:false, status:"skipped"} HTTP 200, no exception.
  3. POST /decompose on a NON-full-AI (templated) slide is rejected with a clear
     error (Refinement 1 guard).
  4. Post-merge integration: POST /post (FASE 3) is live and fails safe (HTTP 200
     ok:false naming ZERNIO_API_KEY) — both endpoints ship in the same drop.

The subprocess call to decompose.py is stubbed so no real FAL_KEY is needed.

Run: python test_decompose_endpoint.py
"""
from __future__ import annotations

import json
import os
import sys
import tempfile
import threading
import time
import unittest
from http.client import HTTPConnection
from pathlib import Path
from unittest.mock import MagicMock, patch

# ── sys.path injection ──────────────────────────────────────────────────────
_CONTENT_STUDIO = Path(__file__).resolve().parent
sys.path.insert(0, str(_CONTENT_STUDIO))

import content_studio  # noqa: E402
from content_studio import StudioState, make_handler, _free_port  # noqa: E402

# ── Helpers ─────────────────────────────────────────────────────────────────

def _make_run(full_ai_slides=None, templated_slides=None):
    """Create a temporary run folder with the requested slide layout.

    full_ai_slides: list of slide ids that are FULL_AI (no template.html)
    templated_slides: list of slide ids that have a template.html

    Returns (run_dir, Path-to-run, cleanup function).
    """
    tmp = tempfile.mkdtemp()
    run = Path(tmp)

    for sid in (full_ai_slides or []):
        sd = run / sid
        sd.mkdir()
        # Full-AI slide: has a PNG but no template.html
        png = run / f"{sid}.png"
        png.write_bytes(b"\x89PNG\r\n\x1a\n" + b"\x00" * 8)

    for sid in (templated_slides or []):
        sd = run / sid
        sd.mkdir()
        # Templated slide: has a template.html
        (sd / "template.html").write_text(
            "<!DOCTYPE html><html><body><div class='slide'></div></body></html>",
            encoding="utf-8",
        )
        png = run / f"{sid}.png"
        png.write_bytes(b"\x89PNG\r\n\x1a\n" + b"\x00" * 8)

    import shutil
    return run, lambda: shutil.rmtree(tmp, ignore_errors=True)


def _make_ok_decompose(scratch_dir: Path, n_layers: int = 2):
    """Write a fake decompose ok manifest + layer PNGs to scratch_dir."""
    layers_dir = scratch_dir / "layers"
    layers_dir.mkdir(parents=True, exist_ok=True)
    layers = []
    for i in range(n_layers):
        fname = f"{i:02d}.png"
        (layers_dir / fname).write_bytes(b"\x89PNG\r\n\x1a\n" + bytes([i]) * 8)
        layers.append({
            "index": i,
            "file": f"layers/{fname}",
            "width": 1080,
            "height": 1350,
            "source_url": f"https://cdn.fake/layer{i}.png",
        })
    manifest = {
        "tool": "decompose.py",
        "model": "fal-ai/qwen-image-layered",
        "source_image": "slide-01.png",
        "status": "ok",
        "layer_count": n_layers,
        "seed": 42,
        "has_nsfw_concepts": [False] * n_layers,
        "params": {"num_layers": 4, "num_inference_steps": 28,
                   "guidance_scale": 5.0, "output_format": "PNG"},
        "cost_usd_estimate": 0.05,
        "layers": layers,
    }
    (scratch_dir / "manifest.json").write_text(
        json.dumps(manifest), encoding="utf-8"
    )
    return manifest


def _make_skipped_decompose(scratch_dir: Path):
    """Write a fake decompose skipped manifest."""
    scratch_dir.mkdir(parents=True, exist_ok=True)
    manifest = {
        "tool": "decompose.py",
        "model": "fal-ai/qwen-image-layered",
        "source_image": "",
        "status": "skipped",
        "reason": "no_fal_key",
        "layers": [],
    }
    (scratch_dir / "manifest.json").write_text(
        json.dumps(manifest), encoding="utf-8"
    )
    return manifest


class _StubSubprocess:
    """Intercepts subprocess.run calls to decompose.py and writes a canned response."""

    def __init__(self, manifest_factory):
        """manifest_factory(scratch_dir) should write manifest + layers to scratch_dir."""
        self._factory = manifest_factory
        self.returncode = 0
        self.stderr = ""
        self.stdout = ""

    def __call__(self, cmd, **kwargs):
        # Find --output-dir argument in cmd
        try:
            idx = cmd.index("--output-dir")
            out_dir = Path(cmd[idx + 1])
        except (ValueError, IndexError):
            out_dir = Path(tempfile.mkdtemp())
        self._factory(out_dir)
        m = MagicMock()
        m.returncode = self.returncode
        m.stderr = self.stderr
        m.stdout = self.stdout
        return m


class _LiveServer:
    """Spins up a real ThreadingHTTPServer for one test, tears it down after."""

    def __init__(self, state: StudioState):
        from http.server import ThreadingHTTPServer
        self.port = _free_port(0)
        self.httpd = ThreadingHTTPServer(("127.0.0.1", self.port), make_handler(state))
        self._t = threading.Thread(target=self.httpd.serve_forever, daemon=True)
        self._t.start()
        # Wait for readiness
        deadline = time.time() + 3
        while time.time() < deadline:
            try:
                c = HTTPConnection("127.0.0.1", self.port, timeout=0.3)
                c.request("GET", "/healthz")
                c.getresponse()
                break
            except OSError:
                time.sleep(0.05)

    def request(self, method: str, path: str, body: dict | None = None):
        c = HTTPConnection("127.0.0.1", self.port, timeout=10)
        if body is not None:
            raw = json.dumps(body).encode("utf-8")
            c.request(method, path, raw, {"Content-Type": "application/json",
                                          "Content-Length": str(len(raw))})
        else:
            c.request(method, path)
        resp = c.getresponse()
        data = resp.read()
        return resp.status, json.loads(data.decode("utf-8"))

    def stop(self):
        self.httpd.shutdown()


# ────────────────────────────────────────────────────────────────────────────
# Tests
# ────────────────────────────────────────────────────────────────────────────

class TestDecomposeEndpointOk(unittest.TestCase):
    """POST /decompose on a full-AI slide with a stubbed ok decompose.py."""

    def setUp(self):
        self.run, self._cleanup = _make_run(full_ai_slides=["slide-01"])
        self.state = StudioState(self.run, None)
        self.server = _LiveServer(self.state)

    def tearDown(self):
        self.server.stop()
        self._cleanup()

    def _stub_ok(self, scratch):
        _make_ok_decompose(scratch, n_layers=2)

    def test_ok_returns_layer_list(self):
        stub = _StubSubprocess(self._stub_ok)
        with patch("content_studio.subprocess.run", side_effect=stub):
            status, body = self.server.request("POST", "/decompose",
                                               {"slide_id": "slide-01"})
        self.assertEqual(status, 200)
        self.assertTrue(body.get("ok"), f"Expected ok:true, got {body}")
        layers = body.get("layers", [])
        self.assertEqual(len(layers), 2, "Expected 2 layers in response")

    def test_ok_layer_has_required_keys(self):
        stub = _StubSubprocess(self._stub_ok)
        with patch("content_studio.subprocess.run", side_effect=stub):
            _, body = self.server.request("POST", "/decompose", {"slide_id": "slide-01"})
        for layer in body.get("layers", []):
            for key in ("index", "data_uri", "file", "width", "height"):
                self.assertIn(key, layer, f"Layer missing key: {key}")

    def test_ok_layer_has_data_uri(self):
        stub = _StubSubprocess(self._stub_ok)
        with patch("content_studio.subprocess.run", side_effect=stub):
            _, body = self.server.request("POST", "/decompose", {"slide_id": "slide-01"})
        for layer in body.get("layers", []):
            self.assertTrue(
                layer.get("data_uri", "").startswith("data:"),
                f"Layer data_uri is not a data: URI: {layer.get('data_uri', '')[:50]}"
            )


class TestFalKeyResolution(unittest.TestCase):
    """FAL_KEY is resolved from the per-run .env (same source as the Zernio key)
    and injected into the decompose.py subprocess env; /slide-info reports it."""

    def setUp(self):
        self.run, self._cleanup = _make_run(full_ai_slides=["slide-01"])
        self.state = StudioState(self.run, None)
        self.server = _LiveServer(self.state)

    def tearDown(self):
        self.server.stop()
        self._cleanup()

    def test_fal_key_from_run_env_injected_into_subprocess(self):
        (self.run / ".env").write_text("FAL_KEY=test-fal-123\n", encoding="utf-8")
        captured = {}

        def capturing_run(cmd, **kwargs):
            captured["env"] = kwargs.get("env") or {}
            try:
                idx = cmd.index("--output-dir")
                _make_ok_decompose(Path(cmd[idx + 1]), n_layers=1)
            except (ValueError, IndexError):
                pass
            m = MagicMock()
            m.returncode = 0
            m.stderr = ""
            m.stdout = ""
            return m

        with patch("content_studio.subprocess.run", side_effect=capturing_run):
            status, _ = self.server.request("POST", "/decompose", {"slide_id": "slide-01"})
        self.assertEqual(status, 200)
        self.assertEqual(
            captured.get("env", {}).get("FAL_KEY"), "test-fal-123",
            "FAL_KEY from the run .env must be injected into the decompose subprocess env",
        )

    def test_slide_info_has_fal_key_true_with_env(self):
        (self.run / ".env").write_text("FAL_KEY=abc\n", encoding="utf-8")
        _, body = self.server.request("GET", "/slide-info")
        self.assertTrue(body.get("hasFalKey"))

    def test_slide_info_has_fal_key_false_without_env(self):
        # No .env in the run tree AND no exported FAL_KEY → false.
        with patch.dict(os.environ):
            os.environ.pop("FAL_KEY", None)
            _, body = self.server.request("GET", "/slide-info")
        self.assertFalse(body.get("hasFalKey"))


class TestDecomposeEndpointSkipped(unittest.TestCase):
    """POST /decompose when decompose.py returns the skipped stub (no FAL_KEY)."""

    def setUp(self):
        self.run, self._cleanup = _make_run(full_ai_slides=["slide-01"])
        self.state = StudioState(self.run, None)
        self.server = _LiveServer(self.state)

    def tearDown(self):
        self.server.stop()
        self._cleanup()

    def test_skipped_returns_ok_false_status_skipped(self):
        def stub_skipped(scratch):
            _make_skipped_decompose(scratch)

        sub = _StubSubprocess(stub_skipped)
        sub.returncode = 3  # EXIT_SKIPPED

        with patch("content_studio.subprocess.run", side_effect=sub):
            status, body = self.server.request("POST", "/decompose",
                                               {"slide_id": "slide-01"})
        self.assertEqual(status, 200, "Skipped should return HTTP 200 (not 5xx)")
        self.assertFalse(body.get("ok"), f"Expected ok:false, got {body}")
        self.assertEqual(body.get("status"), "skipped",
                         f"Expected status:skipped, got {body}")
        self.assertIn("FAL_KEY", body.get("error", ""),
                      f"Error message should mention FAL_KEY: {body}")


class TestDecomposeEndpointTemplatedRejected(unittest.TestCase):
    """POST /decompose on a templated slide with NO AI hero (photo_main) is rejected.
    Templated slides that DO carry a baked-text hero are now decomposable (the hero
    is the decompose source) — see the Magic-Layer integration pass."""

    def setUp(self):
        self.run, self._cleanup = _make_run(templated_slides=["slide-01"])
        self.state = StudioState(self.run, None)
        self.server = _LiveServer(self.state)

    def tearDown(self):
        self.server.stop()
        self._cleanup()

    def test_templated_slide_without_hero_rejected(self):
        status, body = self.server.request("POST", "/decompose",
                                           {"slide_id": "slide-01"})
        self.assertEqual(status, 200)
        self.assertFalse(body.get("ok"), f"Templated slide w/o hero should be rejected: {body}")
        err = body.get("error", "")
        self.assertIn("hero", err.lower(), f"Error should mention the missing hero: {err}")


class TestPostEndpointLive(unittest.TestCase):
    """Post-merge integration: /post (FASE 3 Zernio) is live next to /decompose.
    With no ZERNIO_API_KEY in the run folder it fails safe (HTTP 200, ok:false)
    rather than returning a 501 reserved stub."""

    def setUp(self):
        self.run, self._cleanup = _make_run(full_ai_slides=["slide-01"])
        self.state = StudioState(self.run, None)
        self.server = _LiveServer(self.state)

    def tearDown(self):
        self.server.stop()
        self._cleanup()

    def test_post_is_live_and_failsafe(self):
        status, body = self.server.request("POST", "/post", {})
        self.assertEqual(status, 200, f"POST /post should fail safe at 200, got {status}")
        self.assertFalse(body.get("ok"))
        self.assertIn("ZERNIO_API_KEY", (body.get("reason") or body.get("error") or ""))


if __name__ == "__main__":
    unittest.main(verbosity=2)
