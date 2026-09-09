#!/usr/bin/env python3
"""test_decompose.py -- Unit tests for decompose.py (fal.ai/Qwen layer wrapper).

Tests run WITHOUT fal-client installed in CI (no FAL_KEY, no network).
All external calls are mocked via monkeypatching the module's _get_fal_client
function and the requests module.

Run: python test_decompose.py
"""
import json
import os
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

# Ensure the scripts directory is on the path.
_SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_SCRIPTS_DIR))

import decompose  # noqa: E402


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_fal_result(n_layers: int = 2, seed: int = 42) -> dict:
    """Return a minimal fal subscribe result mimicking qwen-image-layered.

    The REAL ``fal_client.subscribe`` returns a plain **dict** (not an attribute
    object) — `{"images": [{"url","width","height"}], "seed", "has_nsfw_concepts"}`.
    Mirroring that here is what catches dict-vs-attribute access regressions
    (an earlier MagicMock-with-attributes mock hid a real `'dict' has no
    attribute images' crash against the live API).
    """
    return {
        "images": [
            {"url": f"https://fake.cdn/layer_{i:02d}.png", "width": 576, "height": 704}
            for i in range(n_layers)
        ],
        "has_nsfw_concepts": [False] * n_layers,
        "seed": seed,
    }


def _fake_requests_get(url, timeout=30):
    """Fake requests.get that returns fake PNG bytes."""
    # Extract index from url pattern "layer_NN.png"
    import re
    m = re.search(r"layer_(\d+)\.png", url)
    idx = int(m.group(1)) if m else 0
    resp = MagicMock()
    resp.content = b"\x89PNG\r\n\x1a\n" + bytes([idx]) * 8
    resp.raise_for_status = MagicMock()
    return resp


def _run_main(argv, env_extra=None, fal_result=None, subscribe_raises=None):
    """Helper: run decompose.main() with mocked fal + requests.

    Returns (exit_code, manifest_dict_or_None, layers_exists_bool, fake_fal, tmp_path).
    NOTE: tmp_path is a persistent TemporaryDirectory that the caller MUST NOT
    use after the helper returns (it is kept alive only long enough to collect
    the results inside this function).
    """
    tmp_dir = tempfile.TemporaryDirectory()  # NOT used as context-manager here
    tmp_path = Path(tmp_dir.name)

    try:
        # Build argv: replace placeholder "--image __placeholder__" with a real file
        processed_argv = []
        i = 0
        while i < len(argv):
            if argv[i] == "--image" and i + 1 < len(argv):
                if argv[i + 1] == "__placeholder__":
                    src = tmp_path / "source.png"
                    src.write_bytes(b"\x89PNG\r\n\x1a\n" + b"\x00" * 16)
                    processed_argv.extend(["--image", str(src)])
                else:
                    processed_argv.extend([argv[i], argv[i + 1]])
                i += 2
            else:
                processed_argv.append(argv[i])
                i += 1

        if "--output-dir" not in processed_argv:
            processed_argv.extend(["--output-dir", str(tmp_path)])

        env = {k: v for k, v in os.environ.items()}
        env.update(env_extra or {})

        if fal_result is None and subscribe_raises is None:
            fal_result = _make_fal_result()

        if subscribe_raises is not None:
            fake_fal = types.SimpleNamespace(
                upload_file=MagicMock(return_value="https://fake.cdn/up.png"),
                subscribe=MagicMock(side_effect=subscribe_raises),
            )
        else:
            fake_fal = types.SimpleNamespace(
                upload_file=MagicMock(return_value="https://fake.cdn/up.png"),
                subscribe=MagicMock(return_value=fal_result),
            )

        exit_code = None
        with patch.dict(os.environ, env, clear=True):
            with patch.object(decompose, "_get_fal_client", return_value=fake_fal):
                with patch("decompose.requests") as mock_req:
                    mock_req.get.side_effect = _fake_requests_get
                    try:
                        decompose.main(processed_argv)
                        exit_code = 0
                    except SystemExit as e:
                        exit_code = e.code

        # Collect ALL results BEFORE the temp dir is cleaned up.
        manifest = None
        mf = tmp_path / "manifest.json"
        if mf.is_file():
            manifest = json.loads(mf.read_text(encoding="utf-8"))

        layers_dir = tmp_path / "layers"
        layers_exists = layers_dir.is_dir()
        # Snapshot layer filenames (sorted) while the dir is still alive
        layer_files = sorted(p.name for p in layers_dir.iterdir()) if layers_exists else []

        return exit_code, manifest, layers_exists, fake_fal, layer_files

    finally:
        tmp_dir.cleanup()


# ---------------------------------------------------------------------------
# Test: exit-code constants
# ---------------------------------------------------------------------------

class TestExitCodeConstants(unittest.TestCase):
    """EXIT_OK, EXIT_SKIPPED, EXIT_ERROR must be three distinct non-negative ints."""

    def test_constants_defined(self):
        self.assertTrue(hasattr(decompose, "EXIT_OK"))
        self.assertTrue(hasattr(decompose, "EXIT_SKIPPED"))
        self.assertTrue(hasattr(decompose, "EXIT_ERROR"))

    def test_constants_are_integers(self):
        self.assertIsInstance(decompose.EXIT_OK, int)
        self.assertIsInstance(decompose.EXIT_SKIPPED, int)
        self.assertIsInstance(decompose.EXIT_ERROR, int)

    def test_constants_are_distinct(self):
        codes = {decompose.EXIT_OK, decompose.EXIT_SKIPPED, decompose.EXIT_ERROR}
        self.assertEqual(
            len(codes), 3,
            "EXIT_OK, EXIT_SKIPPED, EXIT_ERROR must be three distinct values"
        )

    def test_exit_ok_is_zero(self):
        self.assertEqual(decompose.EXIT_OK, 0, "EXIT_OK must be 0 (POSIX success)")


# ---------------------------------------------------------------------------
# Test: fail-safe (no FAL_KEY)
# ---------------------------------------------------------------------------

class TestFailSafeNoKey(unittest.TestCase):
    """With FAL_KEY unset, main() exits EXIT_SKIPPED, writes skipped manifest,
    leaves NO layers/ dir, and prints no traceback."""

    def _run_no_key(self):
        env_no_key = {k: v for k, v in os.environ.items() if k != "FAL_KEY"}
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            env_no_key["FAL_KEY"] = ""  # explicitly unset by setting empty
            # Actually remove it
            env_only = {k: v for k, v in env_no_key.items() if k != "FAL_KEY"}
            exit_code = None
            manifest = None
            layers_exists = False
            stderr_buf = []

            import io
            old_stderr = sys.stderr
            sys.stderr = io.StringIO()

            # chdir into the (empty) temp dir so decompose._load_env_file() finds
            # no stray .env up the tree — keeps the no-key path hermetic.
            old_cwd = os.getcwd()
            os.chdir(tmp_path)
            try:
                with patch.dict(os.environ, env_only, clear=True):
                    try:
                        decompose.main(["--image", "/nonexistent.png",
                                        "--output-dir", str(tmp_path)])
                        exit_code = 0
                    except SystemExit as e:
                        exit_code = e.code
            finally:
                os.chdir(old_cwd)

            captured_stderr = sys.stderr.getvalue()
            sys.stderr = old_stderr

            mf = tmp_path / "manifest.json"
            if mf.is_file():
                manifest = json.loads(mf.read_text(encoding="utf-8"))
            layers_exists = (tmp_path / "layers").is_dir()
            return exit_code, manifest, layers_exists, captured_stderr

    def test_exits_with_skipped_code(self):
        code, _, _, _ = self._run_no_key()
        self.assertEqual(code, decompose.EXIT_SKIPPED,
                         f"Expected EXIT_SKIPPED ({decompose.EXIT_SKIPPED}), got {code}")

    def test_writes_skipped_manifest(self):
        _, manifest, _, _ = self._run_no_key()
        self.assertIsNotNone(manifest, "manifest.json not written on skip")
        self.assertEqual(manifest["status"], "skipped")
        self.assertEqual(manifest["reason"], "no_fal_key")
        self.assertEqual(manifest["layers"], [])

    def test_no_layers_dir(self):
        _, _, layers_exists, _ = self._run_no_key()
        self.assertFalse(layers_exists, "layers/ dir must NOT exist on skip")

    def test_clean_stderr_no_traceback(self):
        _, _, _, stderr = self._run_no_key()
        self.assertGreater(len(stderr.strip()), 0, "No stderr output on skip")
        self.assertNotIn("Traceback", stderr, "Traceback on skip — must not raise")
        self.assertIn("FAL_KEY", stderr, "Stderr must mention FAL_KEY")


# ---------------------------------------------------------------------------
# Test: manifest schema (ok path)
# ---------------------------------------------------------------------------

class TestManifestSchema(unittest.TestCase):
    """Full manifest schema on the ok path (all external calls mocked)."""

    def test_manifest_has_required_top_level_keys(self):
        exit_code, manifest, _, _, _ = _run_main(
            ["--image", "__placeholder__"],
            env_extra={"FAL_KEY": "test-key"},
            fal_result=_make_fal_result(n_layers=2),
        )
        self.assertEqual(exit_code, decompose.EXIT_OK)
        for key in ("tool", "model", "source_image", "status", "layer_count",
                    "seed", "has_nsfw_concepts", "params", "cost_usd_estimate", "layers"):
            self.assertIn(key, manifest, f"Manifest missing key: {key}")

    def test_manifest_status_ok(self):
        _, manifest, _, _, _ = _run_main(
            ["--image", "__placeholder__"],
            env_extra={"FAL_KEY": "test-key"},
        )
        self.assertEqual(manifest["status"], "ok")

    def test_manifest_params_schema(self):
        _, manifest, _, _, _ = _run_main(
            ["--image", "__placeholder__"],
            env_extra={"FAL_KEY": "test-key"},
        )
        for key in ("num_layers", "num_inference_steps", "guidance_scale", "output_format"):
            self.assertIn(key, manifest["params"], f"params missing key: {key}")

    def test_manifest_layers_schema(self):
        _, manifest, _, _, _ = _run_main(
            ["--image", "__placeholder__"],
            env_extra={"FAL_KEY": "test-key"},
            fal_result=_make_fal_result(n_layers=2),
        )
        self.assertEqual(manifest["layer_count"], 2)
        self.assertEqual(len(manifest["layers"]), 2)
        for layer in manifest["layers"]:
            for key in ("index", "file", "width", "height", "source_url"):
                self.assertIn(key, layer, f"Layer entry missing key: {key}")

    def test_layers_written_to_disk_in_order(self):
        _, _, layers_exists, _, layer_files = _run_main(
            ["--image", "__placeholder__"],
            env_extra={"FAL_KEY": "test-key"},
            fal_result=_make_fal_result(n_layers=2),
        )
        self.assertTrue(layers_exists, "layers/ dir not created on ok path")
        self.assertEqual(len(layer_files), 2)
        self.assertEqual(layer_files[0], "00.png")
        self.assertEqual(layer_files[1], "01.png")

    def test_cost_usd_estimate_present(self):
        _, manifest, _, _, _ = _run_main(
            ["--image", "__placeholder__"],
            env_extra={"FAL_KEY": "test-key"},
        )
        self.assertIsInstance(manifest["cost_usd_estimate"], (int, float))
        self.assertGreater(manifest["cost_usd_estimate"], 0)


# ---------------------------------------------------------------------------
# Test: arg mapping
# ---------------------------------------------------------------------------

class TestArgMapping(unittest.TestCase):
    """CLI flags map to the correct model argument keys."""

    def _get_subscribe_args(self, extra_argv):
        _, _, _, fake_fal, _ = _run_main(
            ["--image", "__placeholder__"] + extra_argv,
            env_extra={"FAL_KEY": "test-key"},
        )
        return fake_fal.subscribe.call_args[1]["arguments"]

    def test_num_layers_flag(self):
        args = self._get_subscribe_args(["--num-layers", "6"])
        self.assertEqual(args["num_layers"], 6)

    def test_steps_flag(self):
        args = self._get_subscribe_args(["--steps", "20"])
        self.assertEqual(args["num_inference_steps"], 20)

    def test_guidance_flag(self):
        args = self._get_subscribe_args(["--guidance", "3.5"])
        self.assertAlmostEqual(args["guidance_scale"], 3.5, places=4)

    def test_format_flag_is_lowercased(self):
        # The fal model requires a lowercase enum ('png'|'webp'); the CLI takes
        # upper/mixed case. Sending "PNG" verbatim is a real 422 from the API.
        args = self._get_subscribe_args(["--format", "WEBP"])
        self.assertEqual(args["output_format"], "webp")

    def test_format_default_is_lowercased(self):
        args = self._get_subscribe_args([])
        self.assertEqual(args["output_format"], "png")

    def test_seed_flag(self):
        args = self._get_subscribe_args(["--seed", "1234"])
        self.assertEqual(args["seed"], 1234)

    def test_prompt_flag(self):
        args = self._get_subscribe_args(["--prompt", "vivid layers"])
        self.assertEqual(args["prompt"], "vivid layers")

    def test_negative_prompt_flag(self):
        args = self._get_subscribe_args(["--negative-prompt", "blurry"])
        self.assertEqual(args["negative_prompt"], "blurry")

    def test_defaults_used_when_flags_absent(self):
        """Omitted flags use model defaults: num_layers=4, steps=28, guidance=5.0, format=PNG."""
        args = self._get_subscribe_args([])
        self.assertEqual(args.get("num_layers", 4), 4)
        self.assertEqual(args.get("num_inference_steps", 28), 28)
        self.assertAlmostEqual(args.get("guidance_scale", 5.0), 5.0, places=4)
        self.assertEqual(args.get("output_format", "png"), "png")


# ---------------------------------------------------------------------------
# Test: --image-url passthrough skips upload
# ---------------------------------------------------------------------------

class TestImageUrlPassthrough(unittest.TestCase):
    """--image-url skips the upload call entirely and is passed to subscribe."""

    def test_image_url_skips_upload(self):
        _, _, _, fake_fal, _ = _run_main(
            ["--image-url", "https://user.cdn/slide.png"],
            env_extra={"FAL_KEY": "test-key"},
        )
        fake_fal.upload_file.assert_not_called()

    def test_image_url_used_in_subscribe(self):
        _, _, _, fake_fal, _ = _run_main(
            ["--image-url", "https://user.cdn/slide.png"],
            env_extra={"FAL_KEY": "test-key"},
        )
        subscribe_args = fake_fal.subscribe.call_args[1]["arguments"]
        self.assertEqual(subscribe_args["image_url"], "https://user.cdn/slide.png")


# ---------------------------------------------------------------------------
# Test: atomic error — no partial layers/ dir on failure
# ---------------------------------------------------------------------------

class TestAtomicError(unittest.TestCase):
    """When subscribe raises, main() exits EXIT_ERROR, writes error manifest,
    and leaves NO partial layers/ dir."""

    def test_subscribe_error_exits_error_code(self):
        exit_code, _, _, _, _ = _run_main(
            ["--image", "__placeholder__"],
            env_extra={"FAL_KEY": "test-key"},
            subscribe_raises=RuntimeError("API error"),
        )
        self.assertEqual(exit_code, decompose.EXIT_ERROR)

    def test_subscribe_error_no_partial_layers_dir(self):
        _, _, layers_exists, _, _ = _run_main(
            ["--image", "__placeholder__"],
            env_extra={"FAL_KEY": "test-key"},
            subscribe_raises=RuntimeError("API error"),
        )
        self.assertFalse(layers_exists, "layers/ must NOT exist after error (atomicity)")

    def test_subscribe_error_writes_error_manifest(self):
        _, manifest, _, _, _ = _run_main(
            ["--image", "__placeholder__"],
            env_extra={"FAL_KEY": "test-key"},
            subscribe_raises=RuntimeError("network timeout"),
        )
        self.assertIsNotNone(manifest, "manifest.json not written on error")
        self.assertEqual(manifest["status"], "error")
        self.assertIn("reason", manifest)


# ---------------------------------------------------------------------------
# Test: point-of-use credential revalidation (AIOS-139 Addendum 10 #2)
# ---------------------------------------------------------------------------

class TestEnvRevalidation(unittest.TestCase):
    """A FAL_KEY written into .env AFTER import (mid-run) is picked up at the
    point of use — decompose re-reads .env in main(), never a cached verdict."""

    def test_load_env_file_picks_up_key_written_after_import(self):
        """_load_env_file() reads a .env created after module import."""
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            (tmp_path / ".env").write_text(
                'FAL_KEY="key-pasted-mid-run"\n', encoding="utf-8"
            )
            old_cwd = os.getcwd()
            os.chdir(tmp_path)
            try:
                env_only = {k: v for k, v in os.environ.items() if k != "FAL_KEY"}
                with patch.dict(os.environ, env_only, clear=True):
                    self.assertNotIn("FAL_KEY", os.environ)
                    decompose._load_env_file()
                    self.assertEqual(os.environ.get("FAL_KEY"), "key-pasted-mid-run")
            finally:
                os.chdir(old_cwd)

    def test_main_uses_env_key_with_no_env_var(self):
        """main() reaches the OK path using a FAL_KEY from .env alone (no
        FAL_KEY in the process env) — proving point-of-use revalidation, not
        the start-of-run os.environ snapshot, governs the run."""
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            (tmp_path / ".env").write_text("FAL_KEY=from-dot-env\n", encoding="utf-8")
            src = tmp_path / "source.png"
            src.write_bytes(b"\x89PNG\r\n\x1a\n" + b"\x00" * 16)

            fake_fal = types.SimpleNamespace(
                upload_file=MagicMock(return_value="https://fake.cdn/up.png"),
                subscribe=MagicMock(return_value=_make_fal_result(n_layers=2)),
            )

            old_cwd = os.getcwd()
            os.chdir(tmp_path)
            try:
                env_only = {k: v for k, v in os.environ.items() if k != "FAL_KEY"}
                exit_code = None
                with patch.dict(os.environ, env_only, clear=True):
                    with patch.object(decompose, "_get_fal_client", return_value=fake_fal):
                        with patch("decompose.requests") as mock_req:
                            mock_req.get.side_effect = _fake_requests_get
                            try:
                                decompose.main(["--image", str(src),
                                                "--output-dir", str(tmp_path)])
                                exit_code = 0
                            except SystemExit as e:
                                exit_code = e.code
            finally:
                os.chdir(old_cwd)

            self.assertEqual(
                exit_code, decompose.EXIT_OK,
                "main() should reach OK using a FAL_KEY read fresh from .env, "
                "not skip as if no key were present",
            )

    def test_injected_env_var_wins_over_dot_env(self):
        """An already-set FAL_KEY (e.g. injected by Content Studio) is NOT
        overwritten by .env — os.environ wins."""
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            (tmp_path / ".env").write_text("FAL_KEY=from-dot-env\n", encoding="utf-8")
            old_cwd = os.getcwd()
            os.chdir(tmp_path)
            try:
                env = {k: v for k, v in os.environ.items()}
                env["FAL_KEY"] = "injected-by-parent"
                with patch.dict(os.environ, env, clear=True):
                    decompose._load_env_file()
                    self.assertEqual(os.environ.get("FAL_KEY"), "injected-by-parent")
            finally:
                os.chdir(old_cwd)


if __name__ == "__main__":
    unittest.main(verbosity=2)
