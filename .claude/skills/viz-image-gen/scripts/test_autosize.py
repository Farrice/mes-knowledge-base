# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Tests for the text-fit autosize net in render_template.py (r6h leg-2) — the hard
NO-OVERFLOW guarantee at the bake: every text slot is shrunk to fit its
dimension-locked box before the screenshot, so no per-post value spills/clips its
box regardless of template (the highlight-headline-render "Workflow" overflow).

Two layers:
  * TestAutosizeContract — pure Python, no browser: the helper/constants exist,
    defaults are sane, and autosize_text_fit() delegates to page.evaluate with the
    JS + the floor/tolerance options. Always runs.
  * TestAutosizeBake — real Playwright bake: a fixed-dimension box with a
    guaranteed-overflow word ends up with ZERO residual overflow after the net,
    a box that already fits is left untouched (no-regression), and a value too
    long even at the floor is clamped+clipped and reported (needs-user-decision).
    Skipped automatically if Playwright/chromium is unavailable.

Runs via: uv run test_autosize.py
          or: python test_autosize.py
"""

import sys
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from render_template import (  # noqa: E402
    AUTOSIZE_FLOOR_ABS_PX,
    AUTOSIZE_FLOOR_FRAC,
    AUTOSIZE_TOL_PX,
    _AUTOSIZE_JS,
    autosize_text_fit,
)


# ---------------------------------------------------------------------------
# Contract — pure Python (no browser)
# ---------------------------------------------------------------------------

class _StubPage:
    """Minimal Playwright Page stand-in: records the evaluate() call and returns
    a canned result, so we can assert how autosize_text_fit drives the page."""

    def __init__(self, result):
        self._result = result
        self.calls = []

    def evaluate(self, script, arg=None):
        self.calls.append((script, arg))
        return self._result


class TestAutosizeContract(unittest.TestCase):
    def test_defaults_are_sane(self):
        # tolerance small (sub-pixel ink-bleed), fraction a real shrink range, abs a
        # legibility backstop. These are the calibration knobs of the shrink floor.
        self.assertGreater(AUTOSIZE_TOL_PX, 0)
        self.assertLess(AUTOSIZE_TOL_PX, 6)
        self.assertGreater(AUTOSIZE_FLOOR_FRAC, 0)
        self.assertLess(AUTOSIZE_FLOOR_FRAC, 1)
        self.assertGreaterEqual(AUTOSIZE_FLOOR_ABS_PX, 12)

    def test_js_constant_is_a_runnable_arrow(self):
        # the JS must take the opts object and reference the three knobs + the
        # box-anchored measurement (lockedBox) — the contract the helper passes.
        self.assertIn("(opts)", _AUTOSIZE_JS)
        self.assertIn("opts.tolPx", _AUTOSIZE_JS)
        self.assertIn("opts.floorFrac", _AUTOSIZE_JS)
        self.assertIn("opts.floorAbsPx", _AUTOSIZE_JS)
        self.assertIn("lockedBox", _AUTOSIZE_JS)
        self.assertIn("font-size", _AUTOSIZE_JS)

    def test_helper_passes_js_and_options(self):
        page = _StubPage([{"slot": "HEADLINE", "action": "fit"}])
        out = autosize_text_fit(page)
        self.assertEqual(len(page.calls), 1)
        script, arg = page.calls[0]
        self.assertIs(script, _AUTOSIZE_JS)
        self.assertEqual(arg["tolPx"], AUTOSIZE_TOL_PX)
        self.assertEqual(arg["floorFrac"], AUTOSIZE_FLOOR_FRAC)
        self.assertEqual(arg["floorAbsPx"], AUTOSIZE_FLOOR_ABS_PX)
        self.assertEqual(out, [{"slot": "HEADLINE", "action": "fit"}])

    def test_helper_honours_overrides(self):
        page = _StubPage([])
        autosize_text_fit(page, tol_px=1.0, floor_frac=0.4, floor_abs_px=30.0)
        _, arg = page.calls[0]
        self.assertEqual(arg, {"tolPx": 1.0, "floorFrac": 0.4, "floorAbsPx": 30.0})

    def test_helper_none_result_is_empty_list(self):
        # page.evaluate may return None; the helper must normalise to [].
        self.assertEqual(autosize_text_fit(_StubPage(None)), [])


# ---------------------------------------------------------------------------
# Bake — real Playwright (skipped if browser unavailable)
# ---------------------------------------------------------------------------

def _playwright_available() -> bool:
    try:
        from playwright.sync_api import sync_playwright  # noqa: F401
    except Exception:
        return False
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            b = p.chromium.launch()
            b.close()
        return True
    except Exception:
        return False


# A 1080x1350 slide with fixed-dimension boxes (mirrors the highlight-headline-render
# shape: positioned box with explicit % height, a flex-centered .display child with a
# fixed font-size). One box gets a long word that MUST overflow; one gets a short word
# that fits; one gets a value so long even the floor can't hold it (clamp+clip).
_FIXTURE_HTML = """<!DOCTYPE html><html><head><meta charset="utf-8"><style>
  body { margin:0; padding:0; }
  .slide { position:relative; width:1080px; height:1350px; overflow:hidden; background:#efeeee; }
  .box { position:absolute; display:flex; align-items:center; justify-content:center;
         border:6px solid #1f1816; box-sizing:border-box; }
  .box .display { font-family:Arial, sans-serif; line-height:0.92; letter-spacing:-0.02em;
                  text-align:center; width:100%; }
</style></head><body>
  <div class="slide" data-surface="light">
    <div class="box" data-slot="FITS"     style="left:7%;  top:6%;  width:86%; height:13.5%;">
      <div class="display" data-role="display" style="font-size:13cqw;">OK</div></div>
    <div class="box" data-slot="OVERFLOW" style="left:18%; top:26%; width:64%; height:13.5%;">
      <div class="display" data-role="display" style="font-size:12cqw;">Internationalization</div></div>
    <div class="box" data-slot="TOOLONG"  style="left:7%;  top:46%; width:40%; height:7%;">
      <div class="display" data-role="display" style="font-size:11cqw;">Antidisestablishmentarianism Supercalifragilistic</div></div>
  </div>
</body></html>"""

# Measure residual overflow per box AFTER the net has run — same box-anchored,
# probe-based measurement the net uses, reported independently for assertion.
_RESIDUAL_JS = r"""
() => {
  const lockedBox = (leaf) => {
    let el = leaf;
    while (el && el !== document.body) {
      const cs = getComputedStyle(el);
      const fixedH = (el.style && el.style.height && el.style.height.indexOf('%') >= 0) ||
                     (cs.position === 'absolute' && cs.height !== 'auto');
      if (fixedH) return el; el = el.parentElement;
    }
    return leaf;
  };
  const measure = (leaf, box) => {
    const bcs = getComputedStyle(box);
    const availW = box.clientWidth  - parseFloat(bcs.paddingLeft) - parseFloat(bcs.paddingRight);
    const availH = box.clientHeight - parseFloat(bcs.paddingTop)  - parseFloat(bcs.paddingBottom);
    const lcs = getComputedStyle(leaf);
    const probe = document.createElement('span');
    probe.innerHTML = leaf.innerHTML;
    Object.assign(probe.style, { position:'absolute', left:'-99999px', top:'0', visibility:'hidden',
      whiteSpace:'nowrap', display:'inline-block', margin:'0', padding:'0',
      fontFamily:lcs.fontFamily, fontSize:lcs.fontSize, fontWeight:lcs.fontWeight,
      fontStyle:lcs.fontStyle, letterSpacing:lcs.letterSpacing, lineHeight:lcs.lineHeight,
      textTransform:lcs.textTransform });
    document.body.appendChild(probe);
    const natW = probe.getBoundingClientRect().width;
    probe.style.whiteSpace='normal'; probe.style.width=Math.max(0,availW)+'px';
    const wrapH = probe.getBoundingClientRect().height;
    document.body.removeChild(probe);
    return { overW:+(natW-availW).toFixed(1), overH:+(wrapH-availH).toFixed(1),
             font:+parseFloat(lcs.fontSize).toFixed(1) };
  };
  const r = {};
  document.querySelectorAll('[data-slot]').forEach((z) => {
    const leaf = z.querySelector('.display, [data-role="display"]') || z;
    r[z.getAttribute('data-slot')] = measure(leaf, lockedBox(leaf));
  });
  return r;
};
"""


@unittest.skipUnless(_playwright_available(), "Playwright/chromium not available")
class TestAutosizeBake(unittest.TestCase):
    """Drive a real headless page through autosize_text_fit and assert no overflow."""

    @classmethod
    def setUpClass(cls):
        from playwright.sync_api import sync_playwright
        cls._pw = sync_playwright().start()
        cls._browser = cls._pw.chromium.launch()

    @classmethod
    def tearDownClass(cls):
        cls._browser.close()
        cls._pw.stop()

    def _bake(self, *, tol=AUTOSIZE_TOL_PX, frac=AUTOSIZE_FLOOR_FRAC, floor=AUTOSIZE_FLOOR_ABS_PX):
        ctx = self._browser.new_context(viewport={"width": 1080, "height": 1350}, device_scale_factor=2)
        page = ctx.new_page()
        page.set_content(_FIXTURE_HTML, wait_until="domcontentloaded")
        page.evaluate("() => document.fonts.ready")
        report = autosize_text_fit(page, tol_px=tol, floor_frac=frac, floor_abs_px=floor)
        residual = page.evaluate(_RESIDUAL_JS)
        by_slot = {r["slot"]: r for r in report}
        ctx.close()
        return by_slot, residual

    def test_overflow_box_fits_after_net(self):
        by_slot, residual = self._bake()
        # the long single word was shrunk and now fits both axes (within tolerance)
        self.assertEqual(by_slot["OVERFLOW"]["action"], "shrunk")
        self.assertLess(by_slot["OVERFLOW"]["final"], by_slot["OVERFLOW"]["orig"])
        self.assertLessEqual(residual["OVERFLOW"]["overW"], AUTOSIZE_TOL_PX)
        self.assertLessEqual(residual["OVERFLOW"]["overH"], AUTOSIZE_TOL_PX)

    def test_fitting_box_untouched(self):
        # no-regression: a short value that already fits is reported "fit" and its
        # font-size is unchanged (the net is a no-op for correct content).
        by_slot, _ = self._bake()
        self.assertEqual(by_slot["FITS"]["action"], "fit")
        self.assertAlmostEqual(by_slot["FITS"]["orig"], by_slot["FITS"]["final"], places=1)

    def test_too_long_value_is_clamped_and_clipped(self):
        # a value too long even at the floor → clamped to floor, box overflow:hidden,
        # reported as the "value too long for slot" signal (needs-user-decision).
        by_slot, _ = self._bake()
        self.assertEqual(by_slot["TOOLONG"]["action"], "clamped-clip")
        floor = max(AUTOSIZE_FLOOR_ABS_PX, by_slot["TOOLONG"]["orig"] * AUTOSIZE_FLOOR_FRAC)
        self.assertAlmostEqual(by_slot["TOOLONG"]["final"], floor, delta=0.6)

    def test_short_word_not_inflated_above_authored(self):
        # Shrink-only invariant (the "giant AI over the face" bug): a 2-char word in
        # a box whose font-size was AUTHORED for a long word must render AT (never
        # above) its authored size. The net only shrinks overflow; it never grows
        # underflowing text to fill the box. Caps at the authored CSS value.
        by_slot, _ = self._bake()
        self.assertEqual(by_slot["FITS"]["action"], "fit")
        self.assertLessEqual(
            by_slot["FITS"]["final"], by_slot["FITS"]["orig"] + AUTOSIZE_TOL_PX,
            "short word was inflated above its authored font-size",
        )

    def test_no_slot_grows_above_authored(self):
        # Global ceiling: NO slot ends larger than authored. Any growth past orig is
        # the grow-to-fit regression this test guards against.
        by_slot, _ = self._bake()
        for slot, r in by_slot.items():
            self.assertLessEqual(
                r["final"], r["orig"] + AUTOSIZE_TOL_PX,
                f"{slot} grew above its authored font-size ({r['final']} > {r['orig']})",
            )

    def test_no_box_exceeds_its_frame(self):
        # the headline contract: after the net, NO box has text exceeding its frame
        # beyond the clip backstop. Shrunk/fit boxes have zero residual; a clamped box
        # is allowed residual ONLY because overflow:hidden clips it (the escape valve).
        by_slot, residual = self._bake()
        for slot, res in residual.items():
            action = by_slot[slot]["action"]
            if action in ("fit", "shrunk"):
                self.assertLessEqual(res["overW"], AUTOSIZE_TOL_PX, f"{slot} width spills")
                self.assertLessEqual(res["overH"], AUTOSIZE_TOL_PX, f"{slot} height spills")


if __name__ == "__main__":
    unittest.main()
