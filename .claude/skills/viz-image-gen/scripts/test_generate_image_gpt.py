# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pillow>=10.0.0",
#     "openai>=1.0.0",
# ]
# ///
"""
Tests for generate_image_gpt.py — the EDIT-mode transparency contract
(gpt-edit-transparent).

The OpenAI client is fully mocked (NO network, NO key needed): we patch
``openai.OpenAI`` so ``client.images.edit`` / ``client.images.generate`` just
record the kwargs they were called with and hand back a 1x1 PNG. Input-image
fixtures are real Pillow PNGs (genuinely transparent vs. fully opaque) so the
alpha auto-detection runs against true bytes.

Contract under test:
  - EDIT mode forwards ``background`` + ``output_format`` (today it dropped both).
  - Transparent input (alpha < 255) → default background=transparent + format=png.
  - Opaque input (or RGBA-but-opaque) → NOT transparent → today's exact call
    (no background/output_format kwargs) — no regression.
  - Explicit ``--background opaque`` overrides the auto-detect.
  - The non-edit GENERATE path is untouched.

Runs via: uv run test_generate_image_gpt.py
          or: python test_generate_image_gpt.py
"""

import base64
import sys
import unittest
from io import BytesIO
from pathlib import Path
from unittest import mock

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import generate_image_gpt as gen  # noqa: E402

from PIL import Image  # noqa: E402


# --- fixtures ---------------------------------------------------------------

def _png_1x1_b64() -> str:
    """A minimal valid PNG, base64 — what the mocked API hands back."""
    buf = BytesIO()
    Image.new("RGBA", (1, 1), (0, 0, 0, 0)).save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode("ascii")


def _write_png(path: Path, mode: str, color) -> None:
    Image.new(mode, (4, 4), color).save(str(path), format="PNG")


def _write_transparent(path: Path) -> None:
    # RGBA with at least one fully-transparent pixel.
    img = Image.new("RGBA", (4, 4), (255, 0, 0, 255))
    img.putpixel((0, 0), (0, 0, 0, 0))
    img.save(str(path), format="PNG")


def _write_opaque_rgba(path: Path) -> None:
    # RGBA but every pixel fully opaque → no real transparency to preserve.
    _write_png(path, "RGBA", (10, 20, 30, 255))


def _write_opaque_rgb(path: Path) -> None:
    _write_png(path, "RGB", (10, 20, 30))


# --- harness ----------------------------------------------------------------

class _Recorder:
    """Stands in for the OpenAI client; records the edit/generate call kwargs."""

    def __init__(self):
        self.edit_kwargs = None
        self.generate_kwargs = None
        outer = self

        class _Images:
            def edit(self, **kwargs):
                outer.edit_kwargs = kwargs
                return outer._response()

            def generate(self, **kwargs):
                outer.generate_kwargs = kwargs
                return outer._response()

        self.images = _Images()

    @staticmethod
    def _response():
        data_item = mock.Mock()
        data_item.b64_json = _png_1x1_b64()
        resp = mock.Mock()
        resp.data = [data_item]
        return resp


def _run_main(argv, recorder):
    """Drive generate_image_gpt.main() with a mocked OpenAI client + argv."""
    with mock.patch.object(sys, "argv", ["generate_image_gpt.py", *argv]), \
            mock.patch.dict("os.environ", {"OPENAI_API_KEY": "sk-test"}, clear=False), \
            mock.patch("openai.OpenAI", return_value=recorder):
        gen.main()


# --- alpha detection (the primitive) ---------------------------------------

class TestAlphaDetection(unittest.TestCase):
    def setUp(self):
        self._td = Path(__import__("tempfile").mkdtemp())

    def test_transparent_png_detected(self):
        p = self._td / "t.png"
        _write_transparent(p)
        self.assertTrue(gen._input_has_transparency(str(p)))

    def test_opaque_rgba_not_detected(self):
        p = self._td / "o.png"
        _write_opaque_rgba(p)
        self.assertFalse(gen._input_has_transparency(str(p)))

    def test_opaque_rgb_not_detected(self):
        p = self._td / "rgb.png"
        _write_opaque_rgb(p)
        self.assertFalse(gen._input_has_transparency(str(p)))

    def test_missing_file_is_false(self):
        self.assertFalse(gen._input_has_transparency(str(self._td / "nope.png")))


# --- EDIT mode contract -----------------------------------------------------

class TestEditTransparency(unittest.TestCase):
    def setUp(self):
        self._td = Path(__import__("tempfile").mkdtemp())
        self._out = self._td / "out.png"

    def test_transparent_input_forwards_transparent_png(self):
        src = self._td / "src.png"
        _write_transparent(src)
        rec = _Recorder()
        _run_main(["-p", "edit it", "-f", str(self._out), "-i", str(src)], rec)
        self.assertIsNotNone(rec.edit_kwargs, "edit endpoint was not called")
        self.assertEqual(rec.edit_kwargs.get("background"), "transparent")
        self.assertEqual(rec.edit_kwargs.get("output_format"), "png")

    def test_opaque_input_no_transparency_kwargs(self):
        # No-regression: opaque input → the call carries NEITHER background NOR
        # output_format (byte-identical to the pre-change behaviour).
        src = self._td / "src.png"
        _write_opaque_rgba(src)
        rec = _Recorder()
        _run_main(["-p", "edit it", "-f", str(self._out), "-i", str(src)], rec)
        self.assertIsNotNone(rec.edit_kwargs)
        self.assertNotIn("background", rec.edit_kwargs)
        self.assertNotIn("output_format", rec.edit_kwargs)

    def test_explicit_opaque_overrides_autodetect(self):
        # Transparent source BUT caller forces --background opaque → opaque wins,
        # no transparency kwargs forwarded.
        src = self._td / "src.png"
        _write_transparent(src)
        rec = _Recorder()
        _run_main(
            ["-p", "edit it", "-f", str(self._out), "-i", str(src),
             "--background", "opaque"],
            rec,
        )
        self.assertIsNotNone(rec.edit_kwargs)
        self.assertNotIn("background", rec.edit_kwargs)

    def test_explicit_transparent_on_opaque_input_forwards_transparent(self):
        # Explicit --background transparent wins even when the source is opaque
        # (caller's choice beats auto-detect), and forces an alpha-capable format.
        src = self._td / "src.png"
        _write_opaque_rgba(src)
        rec = _Recorder()
        _run_main(
            ["-p", "edit it", "-f", str(self._out), "-i", str(src),
             "--background", "transparent", "--format", "jpeg"],
            rec,
        )
        self.assertEqual(rec.edit_kwargs.get("background"), "transparent")
        self.assertEqual(rec.edit_kwargs.get("output_format"), "png")

    def test_transparent_input_webp_format_preserved(self):
        # webp is alpha-capable → honoured instead of being forced to png.
        src = self._td / "src.png"
        _write_transparent(src)
        rec = _Recorder()
        _run_main(
            ["-p", "edit it", "-f", str(self._td / "out.webp"), "-i", str(src),
             "--format", "webp"],
            rec,
        )
        self.assertEqual(rec.edit_kwargs.get("background"), "transparent")
        self.assertEqual(rec.edit_kwargs.get("output_format"), "webp")


# --- EDIT mode: quality forwarding (gpt-edit-transparent desvio #4) ----------

class TestEditQualityForwarding(unittest.TestCase):
    def setUp(self):
        self._td = Path(__import__("tempfile").mkdtemp())
        self._out = self._td / "out.png"

    def test_quality_forwarded_default_high(self):
        # The edit endpoint honours quality; the script default is "high".
        # Previously dropped in edit mode (same class as the background bug).
        src = self._td / "src.png"
        _write_opaque_rgb(src)
        rec = _Recorder()
        _run_main(["-p", "edit it", "-f", str(self._out), "-i", str(src)], rec)
        self.assertIsNotNone(rec.edit_kwargs)
        self.assertEqual(rec.edit_kwargs.get("quality"), "high")

    def test_quality_forwarded_explicit(self):
        src = self._td / "src.png"
        _write_opaque_rgb(src)
        rec = _Recorder()
        _run_main(
            ["-p", "edit it", "-f", str(self._out), "-i", str(src),
             "--quality", "low"],
            rec,
        )
        self.assertEqual(rec.edit_kwargs.get("quality"), "low")


# --- EDIT mode: multi-image -------------------------------------------------

class TestEditMultiImage(unittest.TestCase):
    def setUp(self):
        self._td = Path(__import__("tempfile").mkdtemp())
        self._out = self._td / "out.png"

    def test_single_image_passed_as_bare_file(self):
        # No-regression: one --input-image → image kwarg is the single file
        # object, NOT a list (byte-identical to the original call).
        src = self._td / "src.png"
        _write_opaque_rgb(src)
        rec = _Recorder()
        _run_main(["-p", "edit it", "-f", str(self._out), "-i", str(src)], rec)
        self.assertIsNotNone(rec.edit_kwargs)
        self.assertNotIsInstance(rec.edit_kwargs.get("image"), list)

    def test_multiple_images_passed_as_list_in_order(self):
        # Several --input-image → the full list reaches the API, in order.
        srcs = []
        for i in range(3):
            p = self._td / f"src{i}.png"
            _write_opaque_rgb(p)
            srcs.append(p)
        rec = _Recorder()
        argv = ["-p", "combine these", "-f", str(self._out)]
        for p in srcs:
            argv += ["-i", str(p)]
        _run_main(argv, rec)
        self.assertIsNotNone(rec.edit_kwargs)
        img = rec.edit_kwargs.get("image")
        self.assertIsInstance(img, list)
        self.assertEqual(len(img), 3)

    def test_transparency_follows_first_input(self):
        # With multiple images, alpha auto-detect looks ONLY at image [0].
        # First transparent → transparent forwarded even if extras are opaque.
        first = self._td / "a.png"
        _write_transparent(first)
        second = self._td / "b.png"
        _write_opaque_rgb(second)
        rec = _Recorder()
        _run_main(
            ["-p", "edit", "-f", str(self._out),
             "-i", str(first), "-i", str(second)],
            rec,
        )
        self.assertEqual(rec.edit_kwargs.get("background"), "transparent")

    def test_first_opaque_extra_transparent_stays_opaque(self):
        # First image opaque, an EXTRA transparent → still opaque (only [0] counts).
        first = self._td / "a.png"
        _write_opaque_rgb(first)
        second = self._td / "b.png"
        _write_transparent(second)
        rec = _Recorder()
        _run_main(
            ["-p", "edit", "-f", str(self._out),
             "-i", str(first), "-i", str(second)],
            rec,
        )
        self.assertNotIn("background", rec.edit_kwargs)


# --- EDIT mode: transparent model routing (ai-edit-live-fixes Fix 1) ---------

class _RaisingOnceRecorder(_Recorder):
    """Like _Recorder, but the first edit() call raises *exc*; the second
    succeeds. Records BOTH calls' kwargs so a retry's kwargs can be asserted."""

    def __init__(self, exc):
        super().__init__()
        self.edit_calls = []
        self._exc = exc
        outer = self

        class _Images:
            def edit(self, **kwargs):
                outer.edit_calls.append(dict(kwargs))
                outer.edit_kwargs = kwargs
                if len(outer.edit_calls) == 1:
                    raise outer._exc
                return outer._response()

            def generate(self, **kwargs):
                outer.generate_kwargs = kwargs
                return outer._response()

        self.images = _Images()


class _BackgroundUnsupported400(Exception):
    """Stand-in for the OpenAI 400 the API returns when a model can't do
    background=transparent. Matched by message text, like the real one."""


class TestEditTransparentModelRouting(unittest.TestCase):
    """Fix 1: a transparent edit on the gpt-image-2 family (default) must be
    rerouted to gpt-image-1.5, which supports transparency; opaque edits keep the
    selected model; a 400 'background not supported' degrades to opaque via a
    single retry."""

    def setUp(self):
        self._td = Path(__import__("tempfile").mkdtemp())
        self._out = self._td / "out.png"

    def test_transparent_input_reroutes_default_to_image_1_5(self):
        # Default model is gpt-image-2 (can't do transparent). A transparent input
        # → the edit must switch THIS call to gpt-image-1.5, keeping transparent.
        src = self._td / "src.png"
        _write_transparent(src)
        rec = _Recorder()
        _run_main(["-p", "edit it", "-f", str(self._out), "-i", str(src)], rec)
        self.assertIsNotNone(rec.edit_kwargs)
        self.assertEqual(rec.edit_kwargs.get("model"), "gpt-image-1.5")
        self.assertEqual(rec.edit_kwargs.get("background"), "transparent")
        self.assertEqual(rec.edit_kwargs.get("output_format"), "png")

    def test_opaque_input_keeps_default_model(self):
        # Opaque → no transparency, no reroute: the default gpt-image-2 stands.
        src = self._td / "src.png"
        _write_opaque_rgb(src)
        rec = _Recorder()
        _run_main(["-p", "edit it", "-f", str(self._out), "-i", str(src)], rec)
        self.assertEqual(rec.edit_kwargs.get("model"), "gpt-image-2")
        self.assertNotIn("background", rec.edit_kwargs)

    def test_transparent_capable_model_not_rerouted(self):
        # An explicitly-selected transparent-capable model is left as-is.
        src = self._td / "src.png"
        _write_transparent(src)
        rec = _Recorder()
        _run_main(
            ["-p", "edit it", "-f", str(self._out), "-i", str(src),
             "--model", "gpt-image-1.5"],
            rec,
        )
        self.assertEqual(rec.edit_kwargs.get("model"), "gpt-image-1.5")
        self.assertEqual(rec.edit_kwargs.get("background"), "transparent")

    def test_400_background_unsupported_retries_without_transparent(self):
        # Safety net: a 400 whose message says transparent background is
        # unsupported → retry ONCE without the transparent background (opaque).
        src = self._td / "src.png"
        _write_transparent(src)
        exc = _BackgroundUnsupported400(
            "Error code: 400 - Transparent background is not supported for this "
            "model, param: background")
        rec = _RaisingOnceRecorder(exc)
        _run_main(["-p", "edit it", "-f", str(self._out), "-i", str(src)], rec)
        self.assertEqual(len(rec.edit_calls), 2, "expected exactly one retry")
        # First call carried transparent; the retry dropped it (degrade to opaque).
        self.assertEqual(rec.edit_calls[0].get("background"), "transparent")
        self.assertNotIn("background", rec.edit_calls[1])
        self.assertNotIn("output_format", rec.edit_calls[1])

    def test_other_400_is_not_retried(self):
        # A DIFFERENT error must NOT trigger the transparent-retry — it propagates.
        src = self._td / "src.png"
        _write_transparent(src)
        exc = _BackgroundUnsupported400("Error code: 400 - content policy violation")
        rec = _RaisingOnceRecorder(exc)
        with self.assertRaises(_BackgroundUnsupported400):
            _run_main(["-p", "edit it", "-f", str(self._out), "-i", str(src)], rec)
        self.assertEqual(len(rec.edit_calls), 1, "must not retry on unrelated 400")


# --- GENERATE mode untouched ------------------------------------------------

class TestGenerateUntouched(unittest.TestCase):
    def setUp(self):
        self._td = Path(__import__("tempfile").mkdtemp())

    def test_generate_path_used_when_no_input_image(self):
        rec = _Recorder()
        _run_main(["-p", "make one", "-f", str(self._td / "g.png")], rec)
        self.assertIsNone(rec.edit_kwargs, "edit must not run without --input-image")
        self.assertIsNotNone(rec.generate_kwargs, "generate path must run")
        # Generate still forwards output_format as it always did.
        self.assertEqual(rec.generate_kwargs.get("output_format"), "png")
        # Default background=auto → not forwarded (unchanged behaviour).
        self.assertNotIn("background", rec.generate_kwargs)


if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    runner = unittest.TextTestRunner(verbosity=2, stream=sys.stdout)
    result = runner.run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)
