#!/usr/bin/env python3
"""Tests for content_studio.py — the local-server wrapper (AIOS-139, Content Studio).

Fast tests (no browser): server routing, shim injection, /save, /load, /apply
slide-selection logic, the canvas->tweaks serialization mapping. The real bake
(/apply producing a PNG) is gated behind Playwright availability so the suite
stays green in headless CI without browsers.
"""
import base64
import json
import threading
import unittest
import urllib.request
from http.server import ThreadingHTTPServer
from pathlib import Path

import content_studio as CS
import test_preview_editor as T


def _playwright_ready() -> bool:
    try:
        from playwright.sync_api import sync_playwright  # noqa: F401
        return True
    except Exception:
        return False


class _ServerFixture:
    """Spin up a studio server on a fixture run folder for the duration of a test."""

    def __init__(self):
        self.td = T._make_run_folder()
        self.run = Path(self.td.name)
        self.state = CS.StudioState(self.run, None)
        self.httpd = ThreadingHTTPServer(("127.0.0.1", 0), CS.make_handler(self.state))
        self.port = self.httpd.server_address[1]
        self.thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)
        self.thread.start()

    @property
    def base(self):
        return f"http://127.0.0.1:{self.port}"

    def get(self, path):
        with urllib.request.urlopen(self.base + path, timeout=10) as r:
            return r.status, r.read().decode()

    def post(self, path, obj):
        req = urllib.request.Request(
            self.base + path,
            data=json.dumps(obj).encode(),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=200) as r:
            return r.status, json.loads(r.read().decode())

    def close(self):
        self.httpd.shutdown()
        self.httpd.server_close()
        self.td.cleanup()


class TestRoutingAndShim(unittest.TestCase):
    def setUp(self):
        self.srv = _ServerFixture()

    def tearDown(self):
        self.srv.close()

    def test_healthz(self):
        code, body = self.srv.get("/healthz")
        self.assertEqual(code, 200)
        self.assertEqual(body, "ok")

    def test_editor_html_has_shim_and_tweaks_hook(self):
        _, html = self.srv.get("/")
        self.assertIn('<script src="/studio.js"></script>', html)
        # the editor must expose __getTweaks for the shim (preview_editor.py)
        self.assertIn("__getTweaks", html)

    def test_studio_js_served(self):
        code, js = self.srv.get("/studio.js")
        self.assertEqual(code, 200)
        self.assertIn("/apply", js)
        self.assertIn("/save", js)

    def test_unknown_path_404(self):
        with self.assertRaises(urllib.error.HTTPError) as ctx:
            self.srv.get("/nope")
        self.assertEqual(ctx.exception.code, 404)

    def test_decompose_endpoint_is_live(self):
        # /decompose is implemented (FASE 2 Magic Layer) — no longer a 501 stub.
        # With an empty body (no slide_id) it validates input → 400, proving the
        # endpoint is dispatched rather than reserved.
        with self.assertRaises(urllib.error.HTTPError) as ctx:
            self.srv.post("/decompose", {})
        self.assertEqual(ctx.exception.code, 400)


class TestSaveLoad(unittest.TestCase):
    def setUp(self):
        self.srv = _ServerFixture()

    def tearDown(self):
        self.srv.close()

    def test_load_empty(self):
        _, body = self.srv.get("/load")
        self.assertTrue(body.startswith("{"))
        data = json.loads(body)
        self.assertTrue(data["ok"])
        self.assertFalse(data["hasTweaks"])
        self.assertFalse(data["hasComments"])

    def test_save_writes_files_and_load_restores(self):
        tweaks = {"global": {}, "slide-01": {"HERO": {"fontSize": 9}}}
        comments = {"slide-01": [{"id": 1, "text": "tighten"}]}
        code, res = self.srv.post("/save", {"tweaks": tweaks, "comments": comments})
        self.assertEqual(code, 200)
        self.assertTrue(res["ok"])
        self.assertEqual(res["nComments"], 1)
        self.assertTrue((self.srv.run / "tweaks.json").is_file())
        self.assertTrue((self.srv.run / "comments.json").is_file())
        # round-trip
        _, body = self.srv.get("/load")
        data = json.loads(body)
        self.assertEqual(data["tweaks"], tweaks)
        self.assertEqual(data["comments"], comments)

    def test_save_without_comments_skips_comments_file(self):
        self.srv.post("/save", {"tweaks": {"slide-01": {"HERO": {"x": 5}}}, "comments": {}})
        self.assertTrue((self.srv.run / "tweaks.json").is_file())
        self.assertFalse((self.srv.run / "comments.json").is_file())


class TestApplyLogic(unittest.TestCase):
    def test_affected_slides_excludes_global(self):
        tweaks = {"global": {"accent": "#000"}, "slide-01": {"HERO": {"x": 5}}, "slide-02": {}}
        self.assertEqual(
            sorted(CS._affected_slides(tweaks)), ["slide-01", "slide-02"])

    def test_apply_no_tweaks_returns_empty(self):
        srv = _ServerFixture()
        try:
            _, res = srv.post("/apply", {"tweaks": {"global": {}}})
            self.assertTrue(res["ok"])
            self.assertEqual(res["results"], [])
        finally:
            srv.close()

    def test_canvas_to_tweaks_maps_existing_keys(self):
        # The canvas serialization (Konva free-transform -> tweaks) must land on the
        # SAME keys the panel writes, so the proven rebake path is unchanged.
        CW, CH = 1080, 1350
        node = {"x": 54, "y": 135, "width": 540, "rotation": 7}
        tw = {
            "x": round(node["x"] / CW * 100, 3),
            "y": round(node["y"] / CH * 100, 3),
            "w": round(node["width"] / CW * 100, 3),
            "tilt": round(node["rotation"], 3),
        }
        self.assertEqual(tw, {"x": 5.0, "y": 10.0, "w": 50.0, "tilt": 7})

    @unittest.skipUnless(_playwright_ready(), "Playwright/Chromium not available")
    def test_apply_bakes_real_png(self):
        srv = _ServerFixture()
        try:
            _, res = srv.post(
                "/apply", {"tweaks": {"slide-01": {"HERO": {"fontSize": 9, "x": 5}}}})
            self.assertTrue(res["ok"])
            r = res["results"][0]
            self.assertEqual(r["slide"], "slide-01")
            self.assertTrue(r["ok"], r.get("error"))
            self.assertTrue(r["png"].startswith("data:image/png;base64,"))
            self.assertTrue((srv.run / "slide-01.png").is_file())
        finally:
            srv.close()


class TestCanvasOverlay(unittest.TestCase):
    """The Konva canvas overlay (server-only): routes + serialization parity gate.

    These mirror canvas.js's geom()/write() math in Python so the center-origin
    rotation + center->top-left conversion is locked by a test, independent of a
    browser. The gate: a canvas transform must serialize to the EXACT tweaks keys
    (x/y/w/tilt) the bake honors, with rotation pivoting at center (matching the
    bake's `transform: rotate()`), so canvas-edit == panel-edit == rebake.
    """

    # ── mirror of canvas.js geometry ──────────────────────────────
    @staticmethod
    def _bbox_to_center(bx, by, bw, bh, sw, sh):
        rw = bw / 100 * sw
        rh = bh / 100 * sh
        cx = bx / 100 * sw + rw / 2   # canvas.js sets x,y = CENTER (offset = size/2)
        cy = by / 100 * sh + rh / 2
        return cx, cy, rw, rh

    @staticmethod
    def _serialize(cx, cy, rw, rh, tilt, sw, sh):
        # mirror of geom() + write(): pivot = center, left/top = center - size/2
        left_px = cx - rw / 2
        top_px = cy - rh / 2
        return {
            "x": round(left_px / sw * 100, 3),
            "y": round(top_px / sh * 100, 3),
            "w": round(rw / sw * 100, 3),
            "tilt": round(tilt, 3),
        }

    def test_routes_served(self):
        srv = _ServerFixture()
        try:
            code, _ = srv.get("/canvas.js")
            self.assertEqual(code, 200)
            kcode, kbody = srv.get("/konva.min.js")
            self.assertEqual(kcode, 200)
            self.assertGreater(len(kbody), 50_000)  # the vendored UMD is ~170 KB
        finally:
            srv.close()

    def test_editor_exposes_canvas_hooks(self):
        srv = _ServerFixture()
        try:
            _, html = srv.get("/")
            for hook in ("__SLOT_BBOXES", "__onSlideChange", "__onSelect"):
                self.assertIn(hook, html)
        finally:
            srv.close()

    def test_identity_roundtrip(self):
        # No transform: a rect built from a bbox serializes back to that bbox.
        sw, sh = 555, 694
        cx, cy, rw, rh = self._bbox_to_center(10, 20, 50, 8, sw, sh)
        out = self._serialize(cx, cy, rw, rh, 0, sw, sh)
        self.assertEqual(out, {"x": 10.0, "y": 20.0, "w": 50.0, "tilt": 0})

    def test_pure_rotation_keeps_position(self):
        # CRITICAL parity: rotating around the CENTER must NOT move x/y (the box
        # position is invariant under center rotation, matching CSS transform:rotate).
        sw, sh = 555, 694
        cx, cy, rw, rh = self._bbox_to_center(10, 20, 50, 8, sw, sh)
        out = self._serialize(cx, cy, rw, rh, 15, sw, sh)
        self.assertEqual(out, {"x": 10.0, "y": 20.0, "w": 50.0, "tilt": 15})

    def test_drag_moves_x_only(self):
        sw, sh = 555, 694
        cx, cy, rw, rh = self._bbox_to_center(10, 20, 50, 8, sw, sh)
        cx += 0.10 * sw   # drag right by 10% of the stage width
        out = self._serialize(cx, cy, rw, rh, 0, sw, sh)
        self.assertEqual(out["x"], 20.0)
        self.assertEqual(out["y"], 20.0)
        self.assertEqual(out["w"], 50.0)

    def test_resize_left_anchored_grows_width(self):
        # Widen to 60% keeping the left edge fixed (transformer left-anchor): the
        # center shifts right by half the delta, but serialization recovers x=10,w=60.
        sw, sh = 555, 694
        _, _, _, rh = self._bbox_to_center(10, 20, 50, 8, sw, sh)
        left_px = 10 / 100 * sw
        rw2 = 60 / 100 * sw
        cx = left_px + rw2 / 2
        cy = 20 / 100 * sh + rh / 2
        out = self._serialize(cx, cy, rw2, rh, 0, sw, sh)
        self.assertEqual(out["x"], 10.0)
        self.assertEqual(out["w"], 60.0)

    def test_scale_independent(self):
        # Same canvas transform on a 2x-larger displayed stage yields identical %.
        a = self._serialize(*self._bbox_to_center(10, 20, 50, 8, 555, 694), 7, 555, 694)
        b = self._serialize(*self._bbox_to_center(10, 20, 50, 8, 1110, 1388), 7, 1110, 1388)
        self.assertEqual(a, b)

    def test_bake_consumes_canvas_keys_center_origin(self):
        # The bake must turn x/y into a translate delta, w into width, tilt into a
        # center-origin rotate (translate property applies before transform).
        import render_template as RT  # noqa: PLC0415
        css = RT._build_tweaks_css({"HERO": {"x": 10, "y": 20, "w": 50, "tilt": 15}})
        self.assertIn("translate: 108px 270px", css)  # x=10,y=20 of 1080x1350
        self.assertIn("width: 50%", css)
        # transform: rotate() pivots at transform-origin's default (50% 50% = center)
        self.assertIn("transform: rotate(15deg)", css)

    @unittest.skipUnless(_playwright_ready(), "Playwright/Chromium not available")
    def test_canvas_tweaks_bake_real(self):
        # End-to-end: canvas-serialized tweaks rebake through /apply to a real PNG.
        srv = _ServerFixture()
        try:
            sw, sh = 555, 694
            cx, cy, rw, rh = self._bbox_to_center(10, 22, 92, 7, sw, sh)
            cx += 0.05 * sw
            tw = self._serialize(cx, cy, rw, rh, 6, sw, sh)
            _, res = srv.post("/apply", {"tweaks": {"slide-01": {"HERO": tw}}})
            self.assertTrue(res["ok"])
            r = res["results"][0]
            self.assertTrue(r["ok"], r.get("error"))
            self.assertTrue(r["png"].startswith("data:image/png;base64,"))
        finally:
            srv.close()


def _make_two_slide_run():
    """A 2-slide run folder (carousel swipe needs >1 slide) used by the canvas browser
    tests. The template positions the zone ABSOLUTELY per its bbox — exactly how real
    templates work — so the measured rect matches the bbox and there's no overlap."""
    import tempfile
    from pathlib import Path
    td = tempfile.TemporaryDirectory()
    root = Path(td.name)
    shared = root / "_shared"
    shared.mkdir()
    (shared / "styles.css").write_text("body{margin:0}", encoding="utf-8")
    (shared / "stub.ttf").write_bytes(T._make_minimal_ttf())
    tmpl = (
        "<!doctype html><html><head><meta charset='utf-8'><style>"
        "html,body{margin:0;width:1080px;height:1350px;position:relative}"
        "[data-slot]{position:absolute}"
        ".hero{left:30%;top:40%;width:40%;height:12%}"
        "</style></head><body>"
        '<div class="hero" data-slot="HERO">{{{HERO}}}</div></body></html>'
    )
    instr = (
        "# Slide\n\n## Slots\n\n- **HERO** — headline\n"
        "  - bbox: 30% 40% 40% 12%\n  - style: display, 8cqw\n  - sample: \"Hi\"\n"
    )
    for n in ("slide-01", "slide-02"):
        sd = root / n
        sd.mkdir()
        (sd / "template.html").write_text(tmpl, encoding="utf-8")
        (sd / "instructions.md").write_text(instr, encoding="utf-8")
    return td


class TestCanvasSwipeGuard(unittest.TestCase):
    """Playwright-gated: in free-transform (ON) mode NO drag flips the carousel slide
    (the reported bug — editing must never swipe). Toggling OFF restores swipe-by-drag."""

    @unittest.skipUnless(_playwright_ready(), "Playwright/Chromium not available")
    def test_on_mode_never_swipes_off_mode_restores(self):
        from playwright.sync_api import sync_playwright  # noqa: PLC0415
        from http.server import ThreadingHTTPServer
        import threading

        td = _make_two_slide_run()
        from pathlib import Path
        run = Path(td.name)
        httpd = ThreadingHTTPServer(("127.0.0.1", 0), CS.make_handler(CS.StudioState(run, None)))
        port = httpd.server_address[1]
        threading.Thread(target=httpd.serve_forever, daemon=True).start()
        try:
            with sync_playwright() as p:
                b = p.chromium.launch()
                pg = b.new_page()
                pg.goto(f"http://127.0.0.1:{port}/")
                pg.wait_for_timeout(1500)
                self.assertEqual(pg.evaluate("window.__activeSlide"), "slide-01")

                g = pg.evaluate(
                    """() => {
                      var c=document.querySelector('.studio-canvas'), r=c.getBoundingClientRect();
                      var bb=(window.__SLOT_BBOXES['slide-01']||[])[0];
                      var ri=window.__studioRectInfo(bb.handle);   // real (measured) rect centre
                      return {left:r.left, top:r.top, w:r.width, h:r.height,
                              hx:r.left+ri.cx, hy:r.top+ri.cy};
                    }"""
                )

                def hdrag(x, y):
                    pg.mouse.move(x, y); pg.mouse.down()
                    pg.mouse.move(x - g["w"] * 0.6, y, steps=12); pg.mouse.up()
                    pg.wait_for_timeout(300)

                # ON: dragging an element does NOT swipe
                hdrag(g["hx"], g["hy"])
                self.assertEqual(pg.evaluate("window.__activeSlide"), "slide-01",
                                 "element drag wrongly flipped the slide")
                # ON: dragging empty canvas also does NOT swipe (canvas owns drags)
                hdrag(g["left"] + g["w"] * 0.04, g["top"] + g["h"] * 0.04)
                self.assertEqual(pg.evaluate("window.__activeSlide"), "slide-01",
                                 "empty-canvas drag should not swipe while editing (ON)")

                # toggle edit OFF (the de-jargoned mode button: "Browse"/"Edit") →
                # the swipe carousel works again
                pg.evaluate("""() => {
                  var btns=[].slice.call(document.querySelectorAll('#topbar-actions .cs-pill, #studio-bar .cs-pill'));
                  var t=btns.filter(function(b){return /^(Browse|Edit)$/.test(b.textContent.trim());})[0];
                  if (t) t.click();
                }""")
                pg.wait_for_timeout(200)
                self.assertFalse(pg.evaluate("window.__studioCanvasOn"))
                hdrag(g["left"] + g["w"] * 0.5, g["top"] + g["h"] * 0.5)
                self.assertEqual(pg.evaluate("window.__activeSlide"), "slide-02",
                                 "with editing toggled off, drag should swipe")
                b.close()
        finally:
            httpd.shutdown(); httpd.server_close(); td.cleanup()


class TestCanvasDomSeed(unittest.TestCase):
    """AIOS-139 FASE 7 — the canvas seeds its selectable rects from the live
    [data-slot] elements (not only declared numeric bboxes), so older templates that
    position zones via semantic CSS (no `bbox:` in instructions.md) are still
    selectable on the canvas."""

    def test_canvas_js_has_editable_handles_from_dom(self):
        self.assertIn("function editableHandles", CS.CANVAS_JS)
        # the build loop iterates the DOM-augmented list, not the raw bbox seed
        self.assertIn("editableHandles(sid).forEach", CS.CANVAS_JS)
        # it scans the live iframe for [data-slot] zones
        self.assertIn('querySelectorAll("[data-slot]")', CS.CANVAS_JS)


class TestCanvasTransform(unittest.TestCase):
    """Playwright-gated: the Transformer sits above the rects (so its anchors are
    grabbable) and an anchor-drag actually resizes (writes `w`). Regression guard for
    the 'only move works, resize/rotate blocked' bug (rects were drawn over the tr)."""

    @unittest.skipUnless(_playwright_ready(), "Playwright/Chromium not available")
    def test_transformer_on_top_and_resize_writes_w(self):
        from playwright.sync_api import sync_playwright  # noqa: PLC0415
        from http.server import ThreadingHTTPServer
        import threading
        from pathlib import Path

        td = _make_two_slide_run()
        run = Path(td.name)
        httpd = ThreadingHTTPServer(("127.0.0.1", 0), CS.make_handler(CS.StudioState(run, None)))
        port = httpd.server_address[1]
        threading.Thread(target=httpd.serve_forever, daemon=True).start()
        try:
            with sync_playwright() as p:
                b = p.chromium.launch()
                pg = b.new_page()
                pg.goto(f"http://127.0.0.1:{port}/")
                pg.wait_for_timeout(1500)
                g = pg.evaluate(
                    """() => {
                      var c=document.querySelector('.studio-canvas'), r=c.getBoundingClientRect();
                      var bb=(window.__SLOT_BBOXES['slide-01']||[])[0];
                      var ri=window.__studioRectInfo(bb.handle);   // measured rect geometry
                      return {cx:r.left+ri.cx, cy:r.top+ri.cy,
                              brx:r.left+ri.cx+ri.w/2, bry:r.top+ri.cy+ri.h/2};
                    }"""
                )
                pg.mouse.click(g["cx"], g["cy"])
                pg.wait_for_timeout(200)
                self.assertEqual(pg.evaluate("window.__studioSelected['slide-01']"), "HERO")

                # the transformer must be above the rect in the layer's child order
                order = pg.evaluate(
                    """() => {
                      var st=Konva.stages[Konva.stages.length-1], kids=st.getLayers()[0].getChildren();
                      var tr=-1, rect=-1;
                      for (var i=0;i<kids.length;i++){var n=kids[i].className;
                        if(n==='Transformer')tr=i; else if(n==='Rect')rect=Math.max(rect,i);}
                      return {tr:tr, rect:rect};
                    }"""
                )
                self.assertGreater(order["tr"], order["rect"], "transformer must sit above the rects")

                # drag the bottom-right anchor outward → width grows (w written, > bbox 40)
                pg.mouse.move(g["brx"], g["bry"])
                pg.mouse.down()
                pg.mouse.move(g["brx"] + 50, g["bry"] + 20, steps=10)
                pg.mouse.up()
                pg.wait_for_timeout(300)
                slot = pg.evaluate("(a) => (window.__getTweaks()['slide-01']||{})[a]||{}", "HERO")
                self.assertIn("w", slot)
                self.assertGreater(slot["w"], 40.0)

                # AFTER the resize the selector must still hug the element (syncRect):
                # the rect's measured box matches the live element's box (the reported
                # 'selector bugs / wrong size after enlarging an image' regression).
                fit = pg.evaluate(
                    """() => {
                      var sid=window.__activeSlide, d=document.getElementById('frame-'+sid).contentDocument;
                      var ri=window.__studioRectInfo('HERO');
                      var el=d.querySelector('[data-slot="HERO"]'), er=el.getBoundingClientRect();
                      var c=document.querySelector('.studio-canvas').getBoundingClientRect();
                      var f=document.getElementById('frame-'+sid), sx=c.width/f.clientWidth, sy=c.height/f.clientHeight;
                      return {rw:ri.w, rh:ri.h, ew:er.width*sx, eh:er.height*sy};
                    }"""
                )
                self.assertLess(abs(fit["rw"] - fit["ew"]), 3, "rect width must match element after resize")
                self.assertLess(abs(fit["rh"] - fit["eh"]), 3, "rect height must match element after resize")
                b.close()
        finally:
            httpd.shutdown(); httpd.server_close(); td.cleanup()


class TestCanvasBrowser(unittest.TestCase):
    """Playwright-gated: the Konva overlay actually builds and a real drag serializes
    to tweaks. Locks the interaction layer (the part the unit tests can't reach)."""

    @unittest.skipUnless(_playwright_ready(), "Playwright/Chromium not available")
    def test_overlay_builds_and_drag_writes_tweaks(self):
        from playwright.sync_api import sync_playwright  # noqa: PLC0415
        from http.server import ThreadingHTTPServer
        import threading
        from pathlib import Path

        td = _make_two_slide_run()
        run = Path(td.name)
        httpd = ThreadingHTTPServer(("127.0.0.1", 0), CS.make_handler(CS.StudioState(run, None)))
        port = httpd.server_address[1]
        threading.Thread(target=httpd.serve_forever, daemon=True).start()

        class _S:
            base = f"http://127.0.0.1:{port}"
            def close(self):
                httpd.shutdown(); httpd.server_close(); td.cleanup()
        srv = _S()
        try:
            url = srv.base + "/"
            with sync_playwright() as p:
                b = p.chromium.launch()
                pg = b.new_page()
                errors = []
                pg.on("pageerror", lambda e: errors.append(str(e)))
                pg.goto(url)
                pg.wait_for_timeout(1500)

                # Konva loaded, overlay API present, stage container built for slide-01
                self.assertEqual(pg.evaluate("typeof Konva"), "object")
                self.assertEqual(pg.evaluate("typeof window.__studioCanvas"), "object")
                self.assertEqual(pg.evaluate('document.querySelectorAll(".studio-canvas").length'), 1)
                self.assertEqual(pg.evaluate('document.querySelectorAll(".studio-canvas canvas").length'), 1)

                info = pg.evaluate(
                    """(function(){
                      var sid=window.__activeSlide, bb=(window.__SLOT_BBOXES[sid]||[])[0];
                      var c=document.querySelector('.studio-canvas'), r=c.getBoundingClientRect();
                      var ri=window.__studioRectInfo(bb.handle);   // real rect centre (measured)
                      return {sid:sid, handle:bb.handle, cx:r.left+ri.cx, cy:r.top+ri.cy};
                    })()"""
                )
                pg.mouse.move(info["cx"], info["cy"])
                pg.mouse.down()
                pg.mouse.move(info["cx"] + 50, info["cy"] + 25, steps=10)
                pg.mouse.up()
                pg.wait_for_timeout(300)

                slot = pg.evaluate(
                    "(a) => (window.__getTweaks()[a.sid]||{})[a.handle]||{}",
                    {"sid": info["sid"], "handle": info["handle"]},
                )
                # a drag changes position → x/y appear in the exported diff. (w/tilt
                # equal their bbox defaults so diffTweaks correctly drops them —
                # additive-by-default; a resize/rotate would surface them.)
                self.assertIn("x", slot)
                self.assertIn("y", slot)
                # tweak value IS the element style (applyToSlide writes the CSS
                # `translate` delta): parity. x% -> px on the 1080-wide slide.
                el_tr = pg.evaluate(
                    """(a) => {
                      var f=document.getElementById('frame-'+a.sid);
                      var d=f && (f.contentDocument||f.contentWindow.document);
                      var el=d && d.querySelector('[data-slot="'+a.handle+'"]');
                      return el ? el.style.translate : null;
                    }""",
                    {"sid": info["sid"], "handle": info["handle"]},
                )
                self.assertIsNotNone(el_tr)
                self.assertIn("px", el_tr)
                self.assertAlmostEqual(float(el_tr.split("px")[0]),
                                       slot["x"] / 100 * 1080, places=1)
                self.assertEqual(errors, [])
                b.close()
        finally:
            srv.close()


class TestPostEndpoint(unittest.TestCase):
    """Tests for the /post endpoint (AIOS-139 Addendum 4 — Zernio publish).

    All tests mock subprocess.run and the .env probe so no real network
    calls or file I/O beyond the temp run folder are made.
    """

    def setUp(self):
        self.srv = _ServerFixture()

    def tearDown(self):
        self.srv.close()

    def test_post_no_key_returns_ok_false(self):
        """No .env in the run folder → HTTP 200, ok:false, reason names ZERNIO_API_KEY."""
        # The fixture run folder has no .env and no parent .env that contains the key.
        # Monkeypatch _zernio_key_present to simulate key absence.
        orig = CS._zernio_key_present
        CS._zernio_key_present = lambda run: False
        try:
            code, res = self.srv.post("/post", {"mode": "publishNow"})
            self.assertEqual(code, 200)
            self.assertFalse(res["ok"])
            self.assertIn("ZERNIO_API_KEY", res.get("reason", ""))
        finally:
            CS._zernio_key_present = orig

    def test_post_key_present_invokes_publish_rest(self):
        """Key present → subprocess called, post_dir = state.run, ok:true returned."""
        import subprocess as _sp

        success_json = json.dumps({"ok": True, "post_id": "abc", "platform": "linkedin",
                                   "status": "published", "post_url": "https://li.test/p/abc",
                                   "scheduled_for": None, "transport": "rest",
                                   "media_count": 3, "optimized": 3})

        orig_key = CS._zernio_key_present
        CS._zernio_key_present = lambda run: True

        captured = {}

        def fake_run(argv, **kwargs):
            captured["argv"] = argv
            return _sp.CompletedProcess(argv, 0, stdout=success_json, stderr="")

        orig_run = _sp.run
        _sp.run = fake_run
        try:
            code, res = self.srv.post("/post", {"mode": "publishNow"})
            self.assertEqual(code, 200)
            self.assertTrue(res.get("ok"), res)
            # post_dir must equal state.run (passed as first positional arg after the script)
            self.assertIn(str(self.srv.state.run), captured["argv"])
        finally:
            CS._zernio_key_present = orig_key
            _sp.run = orig_run

    def test_post_rebakes_pending_tweaks_before_publish(self):
        """Addendum 9 #2 — /post must publish the EDITED slides. When the request
        carries pending tweaks, the affected slides are rebaked server-side BEFORE
        media is collected, so the posted carousel reflects the user's edits even if
        the client bake raced."""
        import subprocess as _sp

        success_json = json.dumps({"ok": True, "status": "published", "platform": "linkedin"})
        orig_key = CS._zernio_key_present
        orig_rebake = CS._rebake_slide
        CS._zernio_key_present = lambda run: True
        rebaked = []
        CS._rebake_slide = lambda state, sid, tweaks: rebaked.append(sid) or {"slide": sid, "ok": True}

        def fake_run(argv, **kwargs):
            return _sp.CompletedProcess(argv, 0, stdout=success_json, stderr="")

        orig_run = _sp.run
        _sp.run = fake_run
        try:
            tweaks = {"slide-01": {"HEADLINE": {"text": "edited"}},
                      "slide-03": {"BODY": {"x": 5}}}
            code, res = self.srv.post("/post", {"mode": "publishNow", "tweaks": tweaks})
            self.assertEqual(code, 200)
            self.assertTrue(res.get("ok"), res)
            # Both edited slides were rebaked before the publish subprocess ran.
            self.assertEqual(sorted(rebaked), ["slide-01", "slide-03"])
        finally:
            CS._zernio_key_present = orig_key
            CS._rebake_slide = orig_rebake
            _sp.run = orig_run

    def test_post_passes_baked_slides_as_media(self):
        """Publish resolves the baked slide-*.png explicitly and passes them via
        --media (sorted by index), so the production method (full-AI / template /
        hybrid) and the single-vs-carousel inference never gate which media ship."""
        import subprocess as _sp

        (self.srv.run / "slide-02.png").write_bytes(b"x")
        (self.srv.run / "slide-01.png").write_bytes(b"x")

        captured = {}
        orig_key = CS._zernio_key_present
        CS._zernio_key_present = lambda run: True

        def fake_run(argv, **kwargs):
            captured["argv"] = argv
            return _sp.CompletedProcess(argv, 0, stdout=json.dumps(
                {"ok": True, "status": "published", "post_url": "https://li.test/p/x"}),
                stderr="")

        orig_run = _sp.run
        _sp.run = fake_run
        try:
            code, res = self.srv.post("/post", {"platform": "linkedin", "mode": "publishNow"})
            self.assertEqual(code, 200)
            self.assertTrue(res.get("ok"), res)
            argv = captured["argv"]
            self.assertIn("--media", argv)
            media = argv[argv.index("--media") + 1:]
            # both baked slides present, slide-01 before slide-02 (sorted by index)
            self.assertTrue(media[0].endswith("slide-01.png"), media)
            self.assertTrue(any(m.endswith("slide-02.png") for m in media), media)
        finally:
            CS._zernio_key_present = orig_key
            _sp.run = orig_run

    def test_post_full_ai_single_image_publishable(self):
        """REGRESSION (Addendum 5 §Fix1): a SINGLE full-AI image (only slide-01.png,
        no template dir) must be publishable. The production method must not gate
        Publish — there is no full-AI gate, and /post resolves the baked PNG via
        --media so publish_rest's single-format autodetect (which seeks image.png,
        never slide-01.png) can't silently drop a lone full-AI slide."""
        import subprocess as _sp

        td = _tempfile.TemporaryDirectory()
        run = _Path(td.name)
        (run / "slide-01.png").write_bytes(_real_png(928, 1152))   # full-AI: bare PNG, no template
        (run / "caption.md").write_text("caption", encoding="utf-8")
        state = CS.StudioState(run, None)
        httpd = ThreadingHTTPServer(("127.0.0.1", 0), CS.make_handler(state))
        port = httpd.server_address[1]
        threading.Thread(target=httpd.serve_forever, daemon=True).start()

        captured = {}
        orig_key, orig_run = CS._zernio_key_present, _sp.run
        CS._zernio_key_present = lambda r: True

        def fake_run(argv, **kwargs):
            captured["argv"] = argv
            return _sp.CompletedProcess(argv, 0, stdout=json.dumps(
                {"ok": True, "status": "published", "post_url": "https://li.test/p/ai"}),
                stderr="")
        _sp.run = fake_run
        try:
            req = urllib.request.Request(
                f"http://127.0.0.1:{port}/post",
                data=json.dumps({"platform": "linkedin", "mode": "publishNow"}).encode(),
                headers={"Content-Type": "application/json"}, method="POST")
            with urllib.request.urlopen(req, timeout=60) as r:
                res = json.loads(r.read().decode())
            self.assertTrue(res.get("ok"), res)            # NOT blocked for a full-AI image
            argv = captured["argv"]
            self.assertIn("--media", argv)
            self.assertTrue(any(a.endswith("slide-01.png") for a in argv), argv)
        finally:
            CS._zernio_key_present = orig_key
            _sp.run = orig_run
            httpd.shutdown(); httpd.server_close(); td.cleanup()

    def test_post_arg_derivation_schedule(self):
        """mode=schedule + platform + accountId → correct flags in derived argv."""
        import subprocess as _sp

        captured = {}

        orig_key = CS._zernio_key_present
        CS._zernio_key_present = lambda run: True

        def fake_run(argv, **kwargs):
            captured["argv"] = argv
            result_json = json.dumps({"ok": True, "post_id": "x", "platform": "linkedin",
                                      "status": "scheduled", "post_url": None,
                                      "scheduled_for": "2026-07-01T14:00:00Z",
                                      "transport": "rest", "media_count": 0, "optimized": 0})
            return _sp.CompletedProcess(argv, 0, stdout=result_json, stderr="")

        orig_run = _sp.run
        _sp.run = fake_run
        try:
            self.srv.post("/post", {
                "platform": "linkedin",
                "accountId": "X",
                "mode": "schedule",
                "scheduleFor": "2026-07-01T14:00:00Z",
            })
            argv = captured["argv"]
            self.assertIn("--platform", argv)
            self.assertEqual(argv[argv.index("--platform") + 1], "linkedin")
            self.assertIn("--account-id", argv)
            self.assertEqual(argv[argv.index("--account-id") + 1], "X")
            self.assertIn("--schedule-for", argv)
            self.assertEqual(argv[argv.index("--schedule-for") + 1], "2026-07-01T14:00:00Z")
        finally:
            CS._zernio_key_present = orig_key
            _sp.run = orig_run

    def test_post_no_schedule_flag_when_publish_now(self):
        """mode=publishNow → no --schedule-for in argv."""
        import subprocess as _sp

        captured = {}

        orig_key = CS._zernio_key_present
        CS._zernio_key_present = lambda run: True

        def fake_run(argv, **kwargs):
            captured["argv"] = argv
            result_json = json.dumps({"ok": True, "post_id": "y", "platform": "instagram",
                                      "status": "published", "post_url": "https://ig.test/p/y",
                                      "scheduled_for": None, "transport": "rest",
                                      "media_count": 1, "optimized": 1})
            return _sp.CompletedProcess(argv, 0, stdout=result_json, stderr="")

        orig_run = _sp.run
        _sp.run = fake_run
        try:
            self.srv.post("/post", {"platform": "instagram", "mode": "publishNow"})
            self.assertNotIn("--schedule-for", captured["argv"])
        finally:
            CS._zernio_key_present = orig_key
            _sp.run = orig_run

    def test_post_pdf_selection(self):
        """pdf:true + platform:linkedin → --pdf in argv; pdf:false → no --pdf."""
        import subprocess as _sp

        orig_key = CS._zernio_key_present
        CS._zernio_key_present = lambda run: True

        def make_fake(cap_key):
            def fake_run(argv, **kwargs):
                cap[cap_key] = argv
                result_json = json.dumps({"ok": True, "post_id": "z", "platform": "linkedin",
                                          "status": "published", "post_url": None,
                                          "scheduled_for": None, "transport": "rest",
                                          "media_count": 1, "optimized": 0})
                return _sp.CompletedProcess(argv, 0, stdout=result_json, stderr="")
            return fake_run

        orig_run = _sp.run
        cap = {}
        try:
            _sp.run = make_fake("with_pdf")
            self.srv.post("/post", {"platform": "linkedin", "mode": "publishNow", "pdf": True})
            self.assertIn("--pdf", cap["with_pdf"])

            _sp.run = make_fake("no_pdf")
            self.srv.post("/post", {"platform": "linkedin", "mode": "publishNow", "pdf": False})
            self.assertNotIn("--pdf", cap["no_pdf"])

            _sp.run = make_fake("non_linkedin")
            self.srv.post("/post", {"platform": "instagram", "mode": "publishNow", "pdf": True})
            self.assertNotIn("--pdf", cap["non_linkedin"])
        finally:
            CS._zernio_key_present = orig_key
            _sp.run = orig_run

    def test_decompose_endpoint_live_alongside_post(self):
        """Post-merge integration: /decompose (FASE 2) is live next to /post (FASE 3).
        Empty body → 400 (slide_id required), not a 501 reserved stub."""
        with self.assertRaises(urllib.error.HTTPError) as ctx:
            self.srv.post("/decompose", {})
        self.assertEqual(ctx.exception.code, 400)

    def test_post_draft_passes_draft_flag(self):
        """mode=draft → --draft passed to publish_rest.py (now supported), no
        --schedule-for. Returns the publisher's result."""
        import subprocess as _sp

        captured = {}
        orig_key = CS._zernio_key_present
        CS._zernio_key_present = lambda run: True

        def fake_run(argv, **kwargs):
            captured["argv"] = argv
            result_json = json.dumps({"ok": True, "post_id": "d1", "platform": "linkedin",
                                      "status": "draft", "post_url": None,
                                      "scheduled_for": None, "transport": "rest",
                                      "media_count": 2, "optimized": 2})
            return _sp.CompletedProcess(argv, 0, stdout=result_json, stderr="")

        orig_run = _sp.run
        _sp.run = fake_run
        try:
            code, res = self.srv.post("/post", {"platform": "linkedin", "mode": "draft"})
            self.assertEqual(code, 200)
            self.assertTrue(res.get("ok"), res)
            self.assertIn("--draft", captured["argv"])
            self.assertNotIn("--schedule-for", captured["argv"])
        finally:
            CS._zernio_key_present = orig_key
            _sp.run = orig_run

    def test_post_synthesizes_post_yaml_when_missing(self):
        """publish_rest.py hard-fails without a post.yaml; /post must synthesize a
        minimal one (platform + format) from the run's slides so the flow works."""
        import subprocess as _sp
        orig_key = CS._zernio_key_present
        CS._zernio_key_present = lambda run: True

        def fake_run(argv, **kw):
            return _sp.CompletedProcess(argv, 0, stdout=json.dumps({"ok": True}), stderr="")

        orig_run = _sp.run
        _sp.run = fake_run
        try:
            py = self.srv.run / "post.yaml"
            if py.is_file():
                py.unlink()
            self.srv.post("/post", {"platform": "instagram", "mode": "publishNow"})
            self.assertTrue(py.is_file(), "/post must synthesize post.yaml")
            self.assertIn("platform: instagram", py.read_text(encoding="utf-8"))
        finally:
            CS._zernio_key_present = orig_key
            _sp.run = orig_run

    def test_ensure_post_yaml_helper(self):
        import tempfile as _tf
        from pathlib import Path as _P
        with _tf.TemporaryDirectory() as d:
            run = _P(d)
            (run / "slide-01.png").write_bytes(b"x")
            (run / "slide-02.png").write_bytes(b"x")
            CS._ensure_post_yaml(run, "linkedin")
            t = (run / "post.yaml").read_text(encoding="utf-8")
            self.assertIn("platform: linkedin", t)
            self.assertIn("format: carousel", t)  # 2 slides → carousel
            # never overwrites an existing manifest
            (run / "post.yaml").write_text("platform: custom\n", encoding="utf-8")
            CS._ensure_post_yaml(run, "instagram")
            self.assertIn("custom", (run / "post.yaml").read_text(encoding="utf-8"))

    def test_post_persists_result_to_logs_yaml(self):
        """Every /post outcome writes post-result.json + appends publish-log.yaml
        (best-effort persistence — "goes to logs/yaml")."""
        import subprocess as _sp

        orig_key = CS._zernio_key_present
        CS._zernio_key_present = lambda run: True

        def fake_run(argv, **kwargs):
            result_json = json.dumps({"ok": True, "post_id": "p9", "platform": "linkedin",
                                      "status": "published",
                                      "post_url": "https://li.test/p/p9"})
            return _sp.CompletedProcess(argv, 0, stdout=result_json, stderr="")

        orig_run = _sp.run
        _sp.run = fake_run
        try:
            self.srv.post("/post", {"platform": "linkedin", "mode": "publishNow"})
            run = self.srv.state.run
            pr = run / "post-result.json"
            log = run / "publish-log.yaml"
            self.assertTrue(pr.is_file())
            self.assertEqual(json.loads(pr.read_text(encoding="utf-8"))["post_id"], "p9")
            self.assertTrue(log.is_file())
            text = log.read_text(encoding="utf-8")
            self.assertIn("platform: \"linkedin\"", text)
            self.assertIn("mode: \"publishNow\"", text)
            self.assertIn("https://li.test/p/p9", text)
        finally:
            CS._zernio_key_present = orig_key
            _sp.run = orig_run

    def test_post_persists_even_on_failure(self):
        """A failed publish still logs (status/error) so the PM can see attempts."""
        import subprocess as _sp

        orig_key = CS._zernio_key_present
        CS._zernio_key_present = lambda run: True

        def fake_run(argv, **kwargs):
            return _sp.CompletedProcess(argv, 1, stdout="", stderr="boom")

        orig_run = _sp.run
        _sp.run = fake_run
        try:
            self.srv.post("/post", {"platform": "instagram", "mode": "publishNow"})
            log = (self.srv.state.run / "publish-log.yaml").read_text(encoding="utf-8")
            self.assertIn("ok: false", log)
            self.assertIn("boom", log)
        finally:
            CS._zernio_key_present = orig_key
            _sp.run = orig_run


class TestPublishUI(unittest.TestCase):
    """Tests for the Publish button in STUDIO_JS and /load hasZernioKey."""

    def setUp(self):
        self.srv = _ServerFixture()

    def tearDown(self):
        self.srv.close()

    def test_studio_js_has_publish_button(self):
        """GET /studio.js contains a Publish button and fetch to /post."""
        code, js = self.srv.get("/studio.js")
        self.assertEqual(code, 200)
        self.assertIn("Publish", js)
        self.assertIn("/post", js)

    def test_studio_js_has_both_layers_and_publish_buttons(self):
        """Post-merge integration: STUDIO_JS carries BOTH the FASE 2 Magic Layer
        button (/decompose) and the FASE 3 Publish button (/post) — both ship in
        the same drop."""
        _, js = self.srv.get("/studio.js")
        # FASE 2 Magic Layer
        self.assertIn("/decompose", js)
        self.assertIn("layersBtn", js)
        # FASE 3 Zernio publish
        self.assertIn("/post", js)
        self.assertIn("publishBtn", js)

    def test_studio_js_schedule_is_local_with_utc_preview(self):
        """Addendum 9 #3: the schedule input is labeled the user's LOCAL time (not
        UTC), shows a 'your time · UTC' preview, and converts to UTC exactly once
        (new Date(local).toISOString()) — no double-conversion."""
        _, js = self.srv.get("/studio.js")
        self.assertIn("Schedule for (your local time)", js)
        self.assertNotIn("Schedule for (UTC)", js)
        self.assertIn("your time", js)
        self.assertIn("UTC", js)
        # single conversion local->UTC for the wire value
        self.assertEqual(js.count("scheduleInp.value).toISOString()"), 1)

    def test_studio_js_has_comment_mode_toggle(self):
        """Addendum 9 #4: Comment is a dedicated topbar toggle that flips
        window.__commentMode (default off) and notifies the editor via
        __setCommentMode — so caption/canvas editing is clean unless armed."""
        _, js = self.srv.get("/studio.js")
        self.assertIn('mkPill("Comment")', js)
        self.assertIn("window.__commentMode", js)
        self.assertIn("__setCommentMode", js)
        # the Comment pill is part of the topbar cluster
        self.assertIn("commentBtn", js)

    def test_studio_js_exposes_break_into_layers(self):
        """Addendum 5 Fix #2: the decompose flow is exposed as
        window.__studioBreakIntoLayers so the in-editor magic-pencil (rendered by
        preview_editor) and the topbar button share one code path."""
        _, js = self.srv.get("/studio.js")
        self.assertIn("function breakIntoLayers", js)
        self.assertIn("window.__studioBreakIntoLayers = breakIntoLayers", js)

    def test_studio_js_added_layer_gets_panel_controls(self):
        """Addendum 5 Fix #3: an added image becomes a NORMAL editable layer — it
        gets an inspector control-group (X/Y/W + opacity), not just a canvas rect.
        __addLayerAsset (shared by add-image + decompose) must build that group."""
        _, js = self.srv.get("/studio.js")
        self.assertIn("function buildImageControlGroup", js)
        # wired into the shared asset path so add-image AND decompose both get controls
        self.assertIn("buildImageControlGroup(sid, handle, g)", js)
        # the controls drive the same tweaks props the bake reads (x/y/w via numField, opacity)
        self.assertIn('numField(sid, handle, "x", "ic-arrh"', js)
        self.assertIn('numField(sid, handle, "w", "ic-w"', js)
        self.assertIn('data-prop="opacity"', js)

    def test_studio_js_layer_group_gets_image_actions(self):
        """layer-image-ai-edit: a LAYER_NN ('image-layer') control group gets the
        IMAGE actions (Replace image + Edit-with-AI per provider) IN ADDITION to
        the layer controls (position/size/tilt/opacity), routed to the same
        openAiEdit / pickReplaceImage handlers — never stripping layer controls."""
        _, js = self.srv.get("/studio.js")
        self.assertIn("function imageActionsHtml", js)
        self.assertIn("buildImageControlGroup", js)
        # Replace image + Edit-with-AI wired to the existing handlers
        self.assertIn("window.pickReplaceImage", js)
        self.assertIn("window.openAiEdit", js)
        self.assertIn('class="ai-edit-btn"', js)
        # AI buttons gated on the server-resolved provider presence map
        self.assertIn("window.__aiEditProviders", js)
        # layer controls preserved alongside (tilt is the new one added to the group)
        self.assertIn('data-prop="tilt"', js)
        self.assertIn('data-prop="opacity"', js)

    def test_studio_js_stores_ai_edit_providers_from_slide_info(self):
        """The provider presence map flows from /slide-info into a global the
        injected LAYER group reads (so Edit-with-AI offers exactly the available
        providers)."""
        _, js = self.srv.get("/studio.js")
        self.assertIn("window.__aiEditProviders = res.aiEditProviders", js)

    def test_studio_js_magic_layer_not_pre_disabled_on_fal_key(self):
        """PRD magic-layer-ux §3: the Magic Layer buttons are ALWAYS clickable (like
        Publish/Zernio) — never pre-disabled/greyed on a missing FAL key at load. The
        key is checked at USE time: /decompose fail-safes and the click path shows a
        clear English toast. Replaces the old load-time hasFalKey gating."""
        _, js = self.srv.get("/studio.js")
        # The old load-time gating is gone (both the per-image and global buttons).
        self.assertNotIn("b.disabled = !hasFalKey", js)
        self.assertNotIn("layersBtn.disabled = !hasFalKey", js)
        # The key-missing condition surfaces only as a toast on use.
        self.assertIn("FAL_KEY not found in .env", js)

    def test_studio_js_magic_layer_overlay_and_lock(self):
        """PRD magic-layer-ux §1+§2: a blocking loading overlay covers the studio
        during /decompose and a single in-flight flag makes a second Magic Layer /
        Apply / arrow-nav a no-op until it resolves."""
        _, js = self.srv.get("/studio.js")
        self.assertIn("cs-magic-overlay", js)          # the overlay element + CSS
        self.assertIn("showMagicOverlay", js)
        self.assertIn("hideMagicOverlay", js)
        self.assertIn("window.__magicInFlight", js)    # the interaction lock
        self.assertIn("Please wait… generating layers", js)  # English caption
        # cleanup runs on every exit path (success + error + skip)
        self.assertIn("function finishMagic", js)

    def test_magic_overlay_uses_header_logo_not_inline_svg(self):
        """UX #2: the loading overlay shows the SAME header logo (/agentic-logo.png)
        as an <img class="cs-magic-logo">, not the old inline <text>scrapes</text> SVG.
        The asset-free CSS spinner stays as the onerror fallback."""
        _, js = self.srv.get("/studio.js")
        self.assertIn('class="cs-magic-logo" src="/agentic-logo.png"', js)
        self.assertNotIn(">scrapes</text>", js)   # old inline wordmark gone
        self.assertIn("cs-magic-spin", js)        # spinner fallback kept
        self.assertIn("onerror=", js)             # logo failure reveals the spinner

    def test_front_filters_approved_and_advances(self):
        """UX #5: the Studio front (arrows + counter + Conference) filters out
        approved templates from /pool-templates, exposes a post-approve advance hook,
        and shows an All-templates-approved state when none remain."""
        _, js = self.srv.get("/studio.js")
        # front filters approved templates out of the nav
        self.assertIn("filter(function (t) { return !t.approved; })", js)
        # post-approve advance hook the Approve handlers call
        self.assertIn("advanceAfterApprove", js)
        # the Approve handler emits the required toast and advances
        self.assertIn('toast("Template approved")', js)
        # empty-state instead of broken/empty nav
        self.assertIn("All templates approved", js)

    def test_load_reports_zernio_key_false(self):
        """GET /load returns hasZernioKey:false when no .env/key in run folder."""
        orig = CS._zernio_key_present
        CS._zernio_key_present = lambda run: False
        try:
            _, body = self.srv.get("/load")
            data = json.loads(body)
            self.assertIn("hasZernioKey", data)
            self.assertFalse(data["hasZernioKey"])
        finally:
            CS._zernio_key_present = orig

    def test_load_reports_zernio_key_true_when_key_present(self):
        """GET /load returns hasZernioKey:true when key probe returns True."""
        orig = CS._zernio_key_present
        CS._zernio_key_present = lambda run: True
        try:
            _, body = self.srv.get("/load")
            data = json.loads(body)
            self.assertIn("hasZernioKey", data)
            self.assertTrue(data["hasZernioKey"])
        finally:
            CS._zernio_key_present = orig


class TestHelpers(unittest.TestCase):
    def test_inject_shim_before_body_close(self):
        html = "<html><body><h1>x</h1></body></html>"
        out = CS._inject_shim(html)
        self.assertIn('<script src="/studio.js"></script></body>', out)

    def test_inject_shim_appends_when_no_body(self):
        out = CS._inject_shim("<div>no body tag</div>")
        self.assertTrue(out.rstrip().endswith("</script>"))

    def test_free_port_returns_int(self):
        p = CS._free_port(0)
        self.assertIsInstance(p, int)
        self.assertGreater(p, 0)

    def test_clean_error_maps_timeout(self):
        # AIOS-139 Addendum 9 #5 — a read-timeout traceback must become a clean line.
        tb = ("Traceback (most recent call last):\n"
              '  File "/x/ssl.py", line 1, in recv_into\n'
              "TimeoutError: The read operation timed out\n")
        msg = CS._clean_subprocess_error(tb, what="Zernio publish")
        self.assertIn("timed out", msg)
        self.assertNotIn("Traceback", msg)
        self.assertNotIn("ssl.py", msg)

    def test_clean_error_collapses_generic_traceback(self):
        tb = ("Traceback (most recent call last):\n"
              '  File "/x/publish_rest.py", line 9, in main\n'
              "ValueError: bad post.yaml shape\n")
        msg = CS._clean_subprocess_error(tb, what="Zernio publish")
        self.assertNotIn("Traceback", msg)
        self.assertNotIn('File "', msg)
        self.assertIn("bad post.yaml shape", msg)

    def test_clean_error_passes_clean_text(self):
        msg = CS._clean_subprocess_error("ERROR: no platform set", what="Zernio publish")
        self.assertIn("no platform", msg)


class TestPublishWriteback(unittest.TestCase):
    """AIOS-139 Addendum 8 #2 — a successful publish patches post.yaml and appends
    the aggregated {output_base}/publish-log.md row."""

    def setUp(self):
        self._td = _tempfile.TemporaryDirectory()
        # run = {output_base}/{date}/{slug}
        self.run = _Path(self._td.name) / "out" / "2026-06-05" / "claude-code-agent-view"
        self.run.mkdir(parents=True)
        (self.run / "post.yaml").write_text("platform: linkedin\nformat: carousel\n", encoding="utf-8")
        self.result = {
            "ok": True, "status": "published",
            "post_url": "https://linkedin.com/posts/abc",
            "platform_post_id": "post_123",
            "published_at": "2026-06-05T17:32:00Z",
        }

    def tearDown(self):
        self._td.cleanup()

    def test_patches_post_yaml(self):
        CS._persist_publish_result(self.run, "linkedin", "publishNow", self.result)
        txt = (self.run / "post.yaml").read_text(encoding="utf-8")
        self.assertIn("status: published", txt)
        self.assertIn("publish:", txt)
        self.assertIn("published_at:", txt)
        self.assertIn("2026-06-05T17:32:00Z", txt)
        self.assertIn("post_123", txt)
        self.assertIn("https://linkedin.com/posts/abc", txt)
        self.assertIn("platform: linkedin", txt)  # original keys preserved
        self.assertEqual(txt.count("status: published"), 2)  # top-level + publish block

    def test_appends_publish_log_md(self):
        CS._persist_publish_result(self.run, "linkedin", "publishNow", self.result)
        log = self.run.parent.parent / "publish-log.md"
        self.assertTrue(log.is_file())
        txt = log.read_text(encoding="utf-8")
        self.assertIn("| linkedin | claude-code-agent-view | published |", txt)
        self.assertIn("https://linkedin.com/posts/abc", txt)
        # header written once; a second publish appends a row, not a new header
        CS._persist_publish_result(self.run, "linkedin", "publishNow", self.result)
        txt2 = log.read_text(encoding="utf-8")
        self.assertEqual(txt2.count("# Publish log"), 1)
        self.assertEqual(txt2.count("claude-code-agent-view"), 2)

    def test_no_writeback_on_failure(self):
        CS._persist_publish_result(self.run, "linkedin", "publishNow",
                                   {"ok": False, "error": "401"})
        txt = (self.run / "post.yaml").read_text(encoding="utf-8")
        self.assertNotIn("status: published", txt)
        self.assertFalse((self.run.parent.parent / "publish-log.md").is_file())
        # but the per-run yaml log still records the attempt
        self.assertTrue((self.run / "publish-log.yaml").is_file())


class TestEnvProjectRootResolution(unittest.TestCase):
    """AIOS-139 Addendum 9 #1 — .env resolves from the install/project root, never
    from a stray .env higher up (dev cwd / home). _env_file walks run→root inclusive
    and stops at the project root; with no install root it stays inside the run."""

    def setUp(self):
        self._td = _tempfile.TemporaryDirectory()
        # A fake project tree: <home>/.env (the stray credential) > <proj>/.env
        # (the real one, at the install root) > <proj>/out/<date>/<slug>/ (the run).
        self.home = _Path(self._td.name).resolve()
        (self.home / ".env").write_text("ZERNIO_API_KEY=stray-from-home\n", encoding="utf-8")
        self.proj = (self.home / "myproject").resolve()
        (self.proj / ".claude").mkdir(parents=True)
        (self.proj / ".env").write_text("ZERNIO_API_KEY=real-project-key\n", encoding="utf-8")
        self.run = (self.proj / "out" / "2026-06-05" / "slug")
        self.run.mkdir(parents=True)
        self.run = self.run.resolve()

    def tearDown(self):
        self._td.cleanup()

    def test_project_env_wins_over_stray_ancestor(self):
        env = CS._env_file(self.run, install_root=self.proj)
        self.assertEqual(env, self.proj / ".env")
        # And the value read is the project's, not the stray home one.
        self.assertEqual(_read_key(env), "real-project-key")

    def test_walk_stops_at_install_root(self):
        # Even though <home>/.env exists one level above the root, it is never
        # reached because the walk halts at the project root.
        env = CS._env_file(self.run, install_root=self.proj)
        self.assertNotEqual(env, self.home / ".env")

    def test_no_install_root_stays_in_run(self):
        # Dev/test tree: no install root → only the run folder's own .env counts,
        # so the stray ancestor .env is ignored (hermetic fail-safe).
        self.assertIsNone(CS._env_file(self.run, install_root=None))
        (self.run / ".env").write_text("ZERNIO_API_KEY=local-run\n", encoding="utf-8")
        self.assertEqual(CS._env_file(self.run, install_root=None), self.run / ".env")

    def test_run_outside_root_falls_back_to_run_only(self):
        # A run folder that is NOT under the install root must not climb into it.
        outside = (self.home / "elsewhere" / "run")
        outside.mkdir(parents=True)
        self.assertIsNone(CS._env_file(outside.resolve(), install_root=self.proj))


def _read_key(env_path):
    for raw in env_path.read_text(encoding="utf-8").splitlines():
        if raw.strip().startswith("ZERNIO_API_KEY="):
            return raw.split("=", 1)[1].strip()
    return None


# ── §1 full-AI layer rebake ──────────────────────────────────────────────────
import struct as _struct  # noqa: E402
import zlib as _zlib      # noqa: E402
import tempfile as _tempfile  # noqa: E402
from pathlib import Path as _Path  # noqa: E402


def _real_png(width: int, height: int) -> bytes:
    """A minimal but byte-valid PNG of the requested dimensions (solid white).

    Used so _png_dimensions() reads a real IHDR (not a stub) and so a real bake
    can read the BACKGROUND <img> data URI.
    """
    def chunk(typ: bytes, data: bytes) -> bytes:
        return (_struct.pack(">I", len(data)) + typ + data
                + _struct.pack(">I", _zlib.crc32(typ + data) & 0xFFFFFFFF))
    sig = b"\x89PNG\r\n\x1a\n"
    ihdr = chunk(b"IHDR", _struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0))
    # one white RGBA row per scanline, each prefixed with filter byte 0
    row = b"\x00" + (b"\xff\xff\xff\xff" * width)
    idat = chunk(b"IDAT", _zlib.compress(row * height))
    iend = chunk(b"IEND", b"")
    return sig + ihdr + idat + iend


def _varied_png(width: int, height: int, mode: int = 0) -> bytes:
    """A byte-valid PNG with high colour variance (diagonal RGBA stripes).

    `_real_png` is solid WHITE, which masked the blank-bake bug (a white bake of a
    white fixture looks correct). A varied fixture lets a real bake assert the
    composited output is NON-blank.

    ``mode`` selects the stripe slope so two calls produce visibly distinct
    images (e.g. a RENDER pane vs a REF pane) with no shipped sample asset.
    ``mode=0`` (default) keeps the original diagonal pattern.
    """
    def chunk(typ: bytes, data: bytes) -> bytes:
        return (_struct.pack(">I", len(data)) + typ + data
                + _struct.pack(">I", _zlib.crc32(typ + data) & 0xFFFFFFFF))
    sig = b"\x89PNG\r\n\x1a\n"
    ihdr = chunk(b"IHDR", _struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0))
    raw = bytearray()
    for y in range(height):
        raw.append(0)  # filter byte
        for x in range(width):
            v = (x + 2 * y) % 3 if mode else (x + y) % 3
            raw += bytes((255 if v == 0 else 0, 255 if v == 1 else 0,
                          255 if v == 2 else 0, 255))
    idat = chunk(b"IDAT", _zlib.compress(bytes(raw)))
    iend = chunk(b"IEND", b"")
    return sig + ihdr + idat + iend


def _png_data_uri(raw: bytes) -> str:
    """Encode raw PNG bytes as a data: URI (what the editor sends as an imgSrc tweak)."""
    import base64 as _b64
    return "data:image/png;base64," + _b64.b64encode(raw).decode("ascii")


def _pil_ready() -> bool:
    try:
        from PIL import Image  # noqa: F401
        return True
    except Exception:
        return False


def _png_mean_and_std(path) -> tuple[float, float]:
    """(mean luminance, stddev) of a PNG over RGB, 0..255, via Pillow.

    A near-white blank bake has mean≈255 and std≈0; a real background photo has a
    markedly lower mean and a non-trivial std (colour variance).
    """
    from PIL import Image, ImageStat
    with Image.open(path) as im:
        st = ImageStat.Stat(im.convert("RGB"))
    mean = sum(st.mean) / len(st.mean)
    std = sum(st.stddev) / len(st.stddev)
    return mean, std


class TestPngDimensions(unittest.TestCase):
    def test_reads_real_ihdr(self):
        td = _tempfile.TemporaryDirectory()
        try:
            p = _Path(td.name) / "x.png"
            p.write_bytes(_real_png(928, 1152))
            self.assertEqual(CS._png_dimensions(p), (928, 1152))
        finally:
            td.cleanup()

    def test_rejects_non_png(self):
        td = _tempfile.TemporaryDirectory()
        try:
            p = _Path(td.name) / "x.png"
            p.write_bytes(b"not a png")
            self.assertIsNone(CS._png_dimensions(p))
        finally:
            td.cleanup()


class TestLayerCanvasTemplate(unittest.TestCase):
    def setUp(self):
        self.td = _tempfile.TemporaryDirectory()
        self.run = _Path(self.td.name)
        self.png = self.run / "slide-01.png"
        self.png.write_bytes(_real_png(928, 1152))
        self.info = {"png_path": self.png, "template_dir": None}
        self.made = []

    def tearDown(self):
        import shutil
        for d in self.made:
            shutil.rmtree(d, ignore_errors=True)
        self.td.cleanup()

    def test_returns_none_without_layers(self):
        # No LAYER_* with img → nothing to composite.
        self.assertIsNone(CS._ensure_layer_canvas_template(
            "slide-01", self.info, {"HERO": {"x": 5}}))

    def test_returns_none_layer_without_img(self):
        self.assertIsNone(CS._ensure_layer_canvas_template(
            "slide-01", self.info, {"LAYER_00": {"x": 0}}))

    def test_synthesizes_template_with_background_and_slide(self):
        tdir = CS._ensure_layer_canvas_template(
            "slide-01", self.info,
            {"LAYER_00": {"img": "data:image/png;base64,AAAA", "x": 0, "y": 0, "w": 100}})
        self.assertIsNotNone(tdir)
        self.made.append(tdir)
        html = (tdir / "template.html").read_text(encoding="utf-8")
        # The .slide container is required so _materialize_layers lands layers inside it.
        self.assertIn('class="slide"', html)
        # BACKGROUND img preserves the original pixels.
        self.assertIn('data-slot="BACKGROUND"', html)
        # The original PNG is embedded as a data URI (parity-safe, no base URL).
        self.assertIn("data:image/png;base64,", html)
        # Regression (BLANK bake bug): html,body MUST be height:100% or the
        # height:100% .slide collapses to 0 and the BACKGROUND + injected layers are
        # clipped — the bake came out a 17 KB white PNG. Locked here + by the real
        # bake non-blank assertion in TestApplyLogic.
        self.assertIn("html,body{margin:0;padding:0;height:100%}", html)

    def test_synthesizes_recolorable_bgfill_floor(self):
        # AIOS-139 Bug 2: a recolorable colour FLOOR (data-slot="BGFILL") must sit at
        # the LOWEST z-index beneath the BACKGROUND image, so hiding the image reveals
        # the floor and BGFILL bgColor recolours it. Default transparent (invisible
        # until recoloured). Must precede the BACKGROUND img in the DOM (lower z-index).
        tdir = CS._ensure_layer_canvas_template(
            "slide-01", self.info,
            {"LAYER_00": {"img": "data:image/png;base64,AAAA", "x": 0, "y": 0, "w": 100}})
        self.assertIsNotNone(tdir)
        self.made.append(tdir)
        html = (tdir / "template.html").read_text(encoding="utf-8")
        self.assertIn('data-slot="BGFILL"', html)
        self.assertIn("background:transparent", html)
        self.assertIn("z-index:0", html)
        # floor is the LOWEST layer: BGFILL appears BEFORE the BACKGROUND img
        self.assertLess(html.index('data-slot="BGFILL"'), html.index('data-slot="BACKGROUND"'))


class TestFullAiRebakeRouting(unittest.TestCase):
    """_rebake_slide reroutes full-AI slides with layers through the synthesized
    template; without layers it reports 'not rebakable'."""

    def _state_with_fullai(self):
        td = _tempfile.TemporaryDirectory()
        run = _Path(td.name)
        (run / "slide-01.png").write_bytes(_real_png(928, 1152))
        state = CS.StudioState(run, None)
        return td, state

    def test_fullai_no_layers_not_rebakable(self):
        td, state = self._state_with_fullai()
        try:
            res = CS._rebake_slide(state, "slide-01", {"slide-01": {"HERO": {"x": 5}}})
            self.assertFalse(res["ok"])
            self.assertIn("not rebakable", res["error"])
        finally:
            td.cleanup()

    def test_fullai_texture_only_synthesizes_canvas(self):
        """Addendum 5: a texture-only full-AI slide (no layers) is still rebakable —
        the layer-canvas is synthesized so _materialize_texture can composite over the
        original pixels at bake."""
        td, state = self._state_with_fullai()
        try:
            info = state.slide_map()["slide-01"]
            tdir = CS._ensure_layer_canvas_template(
                "slide-01", info,
                {"__texture": {"tex": "data:image/png;base64,QUJD", "blend": "multiply", "intensity": 0.5}})
            self.assertIsNotNone(tdir)
            self.assertTrue((tdir / "template.html").is_file())
            import shutil as _sh
            _sh.rmtree(tdir, ignore_errors=True)
        finally:
            td.cleanup()

    @unittest.skipUnless(_playwright_ready(), "Playwright/Chromium not available")
    def test_fullai_layer_bake_is_not_blank(self):
        # Regression for the BLANK bake bug: a full-AI slide with a layer must rebake
        # to a PNG with real content (BACKGROUND + layers), not a white canvas. Uses a
        # VARIED fixture so a blank-white bake is detectable (solid-white _real_png
        # masked this — a white bake of a white fixture looked correct).
        try:
            from PIL import Image, ImageStat  # noqa: PLC0415
        except Exception:
            self.skipTest("Pillow not available")
        import base64
        td = _tempfile.TemporaryDirectory()
        run = _Path(td.name)
        (run / "slide-01.png").write_bytes(_varied_png(200, 250))
        state = CS.StudioState(run, None)
        layer_uri = "data:image/png;base64," + base64.b64encode(_varied_png(200, 250)).decode()
        try:
            res = CS._rebake_slide(
                state, "slide-01",
                {"slide-01": {"LAYER_00": {"img": layer_uri, "x": 0, "y": 0,
                                           "w": 100, "h": 100, "opacity": 1}}})
            self.assertTrue(res["ok"], res.get("error"))
            out = run / "slide-01.png"
            self.assertTrue(out.is_file())
            st = ImageStat.Stat(Image.open(out).convert("RGB"))
            self.assertGreater(
                sum(st.stddev), 15.0,
                f"baked full-AI layer PNG looks blank (stddev={st.stddev}, mean={st.mean})")
        finally:
            td.cleanup()

    @unittest.skipUnless(_playwright_ready(), "Playwright/Chromium not available")
    def test_fullai_hidden_bg_reveals_recolored_floor(self):
        # AIOS-139 Bug 2 (the bug this fix closes): on a full-AI/decomposed slide whose
        # backdrop IS the BACKGROUND image, hiding that image (visible:false) + setting
        # a BGFILL floor colour must bake to a PNG painted in that colour — the floor is
        # revealed and recoloured. Before the floor existed the PNG came out blank.
        try:
            from PIL import Image  # noqa: PLC0415
        except Exception:
            self.skipTest("Pillow not available")
        import base64
        td = _tempfile.TemporaryDirectory()
        run = _Path(td.name)
        (run / "slide-01.png").write_bytes(_varied_png(200, 250))
        state = CS.StudioState(run, None)
        # A LAYER_00 (with img) makes the slide rebakable via the layer-canvas path.
        layer_uri = "data:image/png;base64," + base64.b64encode(_varied_png(200, 250)).decode()
        try:
            res = CS._rebake_slide(
                state, "slide-01",
                {"slide-01": {
                    "LAYER_00": {"img": layer_uri, "visible": False, "x": 0, "y": 0,
                                 "w": 100, "h": 100, "opacity": 1},
                    "BACKGROUND": {"visible": False},      # hide the image backdrop
                    "BGFILL": {"bgColor": "#00cc44"},      # recolour the revealed floor (GREEN)
                }})
            self.assertTrue(res["ok"], res.get("error"))
            out = run / "slide-01.png"
            self.assertTrue(out.is_file())
            im = Image.open(out).convert("RGB")
            r, g, b = im.getpixel((im.width // 2, im.height // 2))
            # The centre must be the chosen GREEN floor — not the hidden image, not blank.
            self.assertTrue(g > 150 and r < 120 and b < 120,
                            f"floor not revealed/recoloured: centre pixel = {(r, g, b)}")
        finally:
            td.cleanup()

    def test_fullai_with_layers_invokes_render(self):
        # Stub subprocess.run so we assert the COMMAND is built (template-dir +
        # --canvas WxH from the real PNG IHDR) without needing a browser.
        td, state = self._state_with_fullai()
        captured = {}

        class _Done:
            returncode = 0
            stderr = ""
            stdout = ""

        def fake_run(cmd, **kw):
            captured["cmd"] = cmd
            # Simulate render_template writing the output PNG.
            oi = cmd.index("--output")
            _Path(cmd[oi + 1]).write_bytes(_real_png(928, 1152))
            return _Done()

        try:
            from unittest.mock import patch
            with patch.object(CS.subprocess, "run", side_effect=fake_run):
                res = CS._rebake_slide(
                    state, "slide-01",
                    {"slide-01": {"LAYER_00": {
                        "img": "data:image/png;base64,AAAA",
                        "x": 0, "y": 0, "w": 100, "h": 100}}})
            self.assertTrue(res["ok"], res.get("error"))
            self.assertTrue(res["png"].startswith("data:image/png;base64,"))
            cmd = captured["cmd"]
            self.assertIn("--canvas", cmd)
            self.assertEqual(cmd[cmd.index("--canvas") + 1], "928x1152")
            self.assertIn("--tweaks-slide", cmd)
        finally:
            td.cleanup()

    @unittest.skipUnless(_playwright_ready(), "Playwright/Chromium not available")
    def test_fullai_real_bake_native_size(self):
        # End-to-end: synthesize a layer-canvas template from a real PNG + a real
        # layer data URI, bake it, assert a real non-empty PNG at the native size.
        td, state = self._state_with_fullai()
        try:
            layer_uri = "data:image/png;base64," + base64.b64encode(
                _real_png(928, 1152)).decode("ascii")
            res = CS._rebake_slide(
                state, "slide-01",
                {"slide-01": {"LAYER_00": {
                    "img": layer_uri, "x": 0, "y": 0, "w": 100, "h": 100, "opacity": 1}}})
            self.assertTrue(res["ok"], res.get("error"))
            out = state.run / "slide-01.png"
            self.assertTrue(out.is_file())
            # render_template bakes at device_scale_factor=2, so the output PNG is
            # exactly 2x the --canvas (CSS px) dims — the slide's native aspect ratio
            # and resolution are preserved (NOT a hardcoded 1080x1350).
            dims = CS._png_dimensions(out)
            self.assertEqual(dims, (1856, 2304))
            self.assertEqual(dims[0] / dims[1], 928 / 1152)  # native aspect ratio held
            self.assertGreater(out.stat().st_size, 100)
        finally:
            td.cleanup()


# ── §2 layer usability (served JS contract) ──────────────────────────────────
class TestLayerUsabilityJS(unittest.TestCase):
    """The shared layer-asset machinery lives in STUDIO_JS and must expose the
    helpers + inject the EXACT markup _materialize_layers emits (RNDR-04)."""

    def test_shared_helper_present(self):
        js = CS.STUDIO_JS
        self.assertIn("__addLayerAsset", js)
        self.assertIn("__promoteToLayerCanvas", js)
        self.assertIn("__nextLayerHandle", js)

    def test_inject_markup_byte_identical_to_materialize_layers(self):
        # The client injection style must match render_template._materialize_layers
        # so preview DOM == bake DOM. The bake emits:
        #   <img data-slot="NAME" src="<uri>" style="position:absolute;max-width:none;" />
        js = CS.STUDIO_JS
        self.assertIn('data-slot="\' + handle + \'"', js)
        self.assertIn("position:absolute;max-width:none;", js)

    def test_decompose_defaults_are_full_frame_not_staircase(self):
        # The decompose handler must default LAYER_NN to full-frame (x:0,y:0,w:100,
        # h:100) so the first Apply reproduces the original composition exactly —
        # NOT the old staircase (10 + i*5 / w:80) which scrambled the image.
        js = CS.STUDIO_JS
        self.assertNotIn("10 + i * 5", js)
        self.assertNotIn("(10 + i * 5)", js)
        # full-frame defaults flow through __addLayerAsset
        self.assertIn("bbox.x !== undefined ? bbox.x : 0", js)
        self.assertIn("bbox.w !== undefined ? bbox.w : 100", js)

    def test_promote_builds_slide_container_with_background(self):
        # The promoted iframe must carry a .slide container + BACKGROUND img so the
        # _materialize_layers injector (and addLayerAsset) land layers inside it.
        js = CS.STUDIO_JS
        self.assertIn('class=\\"slide\\"', js)
        self.assertIn('data-slot=\\"BACKGROUND\\"', js)

    def test_addLayerRow_has_no_trash_button(self):
        # FASE 6 §3: no per-layer trash/delete icon — the eye (hide) stays.
        self.assertNotIn("layer-trash", CS.STUDIO_JS)
        self.assertIn("layer-eye", CS.STUDIO_JS)

    def test_promote_srcdoc_carries_recolorable_bgfill_floor(self):
        # AIOS-139 Bug 2: the promoted layer-canvas srcdoc must carry the SAME BGFILL
        # colour floor the bake template (_ensure_layer_canvas_template) injects, so
        # preview == PNG (RNDR-04). Lowest z-index, transparent default; BACKGROUND img
        # explicitly above it (z-index:1). A Fill control is wired so the user recolours.
        js = CS.STUDIO_JS
        self.assertIn('data-slot=\\"BGFILL\\"', js)
        self.assertIn("background:transparent;z-index:0", js)
        # the BACKGROUND img must explicitly sit ABOVE the floor in the promoted srcdoc
        self.assertIn("object-fit:fill;z-index:1", js)
        # the editor must expose a Fill control wired to applyToSlide BGFILL/bgColor
        self.assertIn("__buildBgFillControlGroup", js)
        self.assertIn("\\'BGFILL\\',\\'bgColor\\'", js)

    def test_promote_srcdoc_gives_html_body_full_height(self):
        # Regression (live-preview black bug): without html,body{height:100%} the
        # height:100% .slide collapses to 0 and the absolutely-positioned layers are
        # clipped — the preview renders black while the bake (sized by render_template)
        # is correct. Verified visually in a real browser; locked here.
        js = CS.STUDIO_JS
        self.assertIn("html,body{margin:0;padding:0;height:100%}", js)

    def test_promote_sizes_wrap_to_image_aspect_not_100pct(self):
        # Regression (live-preview clipped bug): replacing the viewer's innerHTML drops
        # the fullai-img that gave the wrap its height, so the layer-canvas wrap MUST
        # get an explicit px height from the original image's aspect — height:100% on
        # the wrap collapses against the height-less .slide-viewer (was 555×150).
        js = CS.STUDIO_JS
        self.assertIn("naturalHeight", js)        # reads the original image dims
        self.assertIn("wrapH", js)                # computes an explicit px height
        # the wrap must NOT be forced to height:100% (the collapse bug)
        self.assertNotIn('class="slide-frame-wrap" style="position:relative;width:100%;height:100%"', js)

    def test_promote_sizes_to_displayed_slide_not_hardcoded_555(self):
        # UX #3: the editor canvas is fit-to-viewport, so the promoted layer canvas
        # must match the CURRENT displayed slide size — read the existing fitted
        # .slide-frame-wrap (or the flat image's rendered box) rather than the old
        # hardcoded var wrapW = 555. 555 survives only as the last-resort fallback.
        js = CS.STUDIO_JS
        self.assertNotIn("var wrapW = 555;", js)          # no longer hardcoded
        self.assertIn("existingWrap", js)                  # reads the fitted wrap
        self.assertIn("getBoundingClientRect", js)         # falls back to image box
        self.assertIn("if (!wrapW) wrapW = 555;", js)      # 555 only as fallback

    def test_decompose_hides_flat_original_so_layers_take_clicks(self):
        # UX #4: once layers are dropped, the original flat image underneath must stop
        # capturing clicks (pointer-events:none on BACKGROUND; the un-decomposed source
        # slot is hidden) so the navigable layers are the click target. Preview-only —
        # the bake is driven by the LAYER_NN tweaks, not these flat elements.
        js = CS.STUDIO_JS
        self.assertIn('img[data-slot="BACKGROUND"]', js)
        self.assertIn('pointerEvents = "none"', js)


# ── §3 add image ─────────────────────────────────────────────────────────────
class TestAddImageEndpoint(unittest.TestCase):
    def setUp(self):
        self.srv = _ServerFixture()

    def tearDown(self):
        self.srv.close()

    def _data_uri(self, w=8, h=8):
        return "data:image/png;base64," + base64.b64encode(_real_png(w, h)).decode("ascii")

    def test_add_image_returns_layer_handle_and_persists(self):
        uri = self._data_uri()
        code, res = self.srv.post("/add-image", {"slide_id": "slide-01", "data_uri": uri})
        self.assertEqual(code, 200)
        self.assertTrue(res["ok"])
        self.assertEqual(res["handle"], "LAYER_00")
        self.assertEqual(res["data_uri"], uri)
        # durable backup written
        self.assertTrue((self.srv.run / "_assets" / "slide-01" / "asset-00.png").is_file())

    def test_add_image_index_avoids_existing_handles(self):
        uri = self._data_uri()
        # client reports a live LAYER_00..LAYER_02 (e.g. from a decompose) → next is 03
        _, res = self.srv.post("/add-image", {
            "slide_id": "slide-01", "data_uri": uri,
            "existing_handles": ["LAYER_00", "LAYER_01", "LAYER_02"]})
        self.assertEqual(res["handle"], "LAYER_03")

    def test_add_image_requires_slide_id(self):
        with self.assertRaises(urllib.error.HTTPError) as ctx:
            self.srv.post("/add-image", {"data_uri": self._data_uri()})
        self.assertEqual(ctx.exception.code, 400)

    def test_add_image_rejects_non_image_data_uri(self):
        with self.assertRaises(urllib.error.HTTPError) as ctx:
            self.srv.post("/add-image", {"slide_id": "slide-01", "data_uri": "not-a-data-uri"})
        self.assertEqual(ctx.exception.code, 400)


class TestNextLayerHandle(unittest.TestCase):
    def setUp(self):
        self.td = _tempfile.TemporaryDirectory()
        self.run = _Path(self.td.name)

    def tearDown(self):
        self.td.cleanup()

    def test_empty_run_starts_at_00(self):
        self.assertEqual(CS._next_layer_handle(self.run, "slide-01"), "LAYER_00")

    def test_scans_saved_tweaks(self):
        (self.run / "tweaks.json").write_text(
            json.dumps({"slide-01": {"LAYER_00": {}, "LAYER_01": {}}}), encoding="utf-8")
        self.assertEqual(CS._next_layer_handle(self.run, "slide-01"), "LAYER_02")

    def test_scans_asset_backups(self):
        adir = self.run / "_assets" / "slide-01"
        adir.mkdir(parents=True)
        (adir / "asset-00.png").write_bytes(b"x")
        (adir / "asset-04.png").write_bytes(b"x")
        self.assertEqual(CS._next_layer_handle(self.run, "slide-01"), "LAYER_05")

    def test_extra_handles_win(self):
        self.assertEqual(
            CS._next_layer_handle(self.run, "slide-01", ["LAYER_09"]), "LAYER_10")


class TestAddImageJS(unittest.TestCase):
    def test_add_image_button_and_endpoint_in_js(self):
        js = CS.STUDIO_JS
        self.assertIn("Add image", js)
        self.assertIn("/add-image", js)
        self.assertIn("readAsDataURL", js)
        # composes via the shared helper
        self.assertIn("__addLayerAsset", js)


# ── §4 remove asset (canvas delete) ──────────────────────────────────────────
class TestRemoveAssetCanvasJS(unittest.TestCase):
    def test_delete_key_wired_to_removeLayer(self):
        js = CS.CANVAS_JS
        self.assertIn("__studioDeleteSelected", js)
        self.assertIn("window.removeLayer", js)
        # Delete/Backspace keys are bound and guarded against typing in inputs.
        self.assertIn('e.key !== "Delete"', js)
        self.assertIn("INPUT|TEXTAREA|SELECT", js)


class TestFase6(unittest.TestCase):
    """FASE 6 (Addendum 7) — publish key fresh-check, editable caption, layer-row trim."""

    def setUp(self):
        self.srv = _ServerFixture()

    def tearDown(self):
        self.srv.close()

    def test_zernio_key_checked_fresh_per_request(self):
        """GET /zernio-key re-reads the .env each call (no caching), so a key added after
        launch is seen without a restart (FASE 6 §2)."""
        orig = CS._zernio_key_present
        try:
            CS._zernio_key_present = lambda run: False
            _, r1 = self.srv.get("/zernio-key")
            self.assertEqual(json.loads(r1), {"ok": True, "hasKey": False})
            CS._zernio_key_present = lambda run: True   # credential added "later"
            _, r2 = self.srv.get("/zernio-key")
            self.assertTrue(json.loads(r2)["hasKey"])    # seen on the very next request
        finally:
            CS._zernio_key_present = orig

    def test_publish_click_checks_key_endpoint(self):
        _, js = self.srv.get("/studio.js")
        self.assertIn('fetch("/zernio-key")', js)        # fresh check on click
        self.assertNotIn("if (window.__hasZernioKey === false)", js)  # not the cached gate

    def test_save_caption_writes_caption_md(self):
        code, res = self.srv.post("/save-caption", {"caption": "Edited post copy #x"})
        self.assertEqual(code, 200)
        self.assertTrue(res["ok"])
        self.assertEqual((self.srv.run / "caption.md").read_text(encoding="utf-8"),
                         "Edited post copy #x")

    def test_save_includes_caption(self):
        self.srv.post("/save", {"tweaks": {}, "comments": {}, "caption": "Via save"})
        self.assertEqual((self.srv.run / "caption.md").read_text(encoding="utf-8"), "Via save")

    def test_save_without_caption_does_not_clobber(self):
        (self.srv.run / "caption.md").write_text("keep me", encoding="utf-8")
        self.srv.post("/save", {"tweaks": {"slide-01": {"HERO": {"x": 5}}}})
        self.assertEqual((self.srv.run / "caption.md").read_text(encoding="utf-8"), "keep me")


class TestFase5LiveWysiwyg(unittest.TestCase):
    """FASE 5 — live WYSIWYG + topbar redesign v2 (Addendum 6)."""

    def setUp(self):
        self.srv = _ServerFixture()

    def tearDown(self):
        self.srv.close()

    def test_apply_mode_removed(self):
        """The "Apply" / "Back to live edit" / baked-status mode is gone — the preview
        is the truth; the bake is implicit on Download/Publish."""
        _, js = self.srv.get("/studio.js")
        self.assertNotIn("Back to live edit", js)
        self.assertNotIn("live rebake", js)
        self.assertNotIn("studio-baked", js)
        self.assertNotIn("Baked ", js)
        # implicit bake helper drives Download/Publish
        self.assertIn("function bakeNow", js)

    def test_download_bakes_before_zip(self):
        """Download bakes (implicit) then fetches the zip → full composites, not bg-only."""
        _, js = self.srv.get("/studio.js")
        self.assertIn("downloadBtn.addEventListener", js)
        self.assertIn("bakeNow().then", js)
        self.assertIn('"/download"', js)

    def test_publish_always_enabled_with_exact_message(self):
        """Publish is never disabled; missing key → the exact English message (FASE 5 §3)."""
        _, js = self.srv.get("/studio.js")
        self.assertNotIn("publishBtn.disabled = true", js)
        self.assertIn(
            "To publish with Zernio you need the ZERNIO_API_KEY credential in your .env.", js)

    def test_texture_is_global_custom_dropdown(self):
        """Texture is a GLOBAL topbar control with a custom (readable) dropdown, not a
        native select on the dark panel (FASE 5 §4+§5)."""
        _, js = self.srv.get("/studio.js")
        self.assertIn('id = "tex-trigger"', js)
        self.assertIn("cs-pop", js)              # custom popover (not a native <select>)
        self.assertIn("window.__setTexture", js)
        self.assertIn("syncTextureFromSlide", js)  # reflects the active slide as you swipe

    def test_agentic_logo_served(self):
        with urllib.request.urlopen(self.srv.base + "/agentic-logo.png", timeout=10) as r:
            self.assertEqual(r.status, 200)
            self.assertEqual(r.headers.get("Content-Type"), "image/png")
            self.assertTrue(r.read(8).startswith(b"\x89PNG"))


class TestRedesignTopbar(unittest.TestCase):
    """FASE 4 redesign — command-centre topbar: Publish-with-Zernio CTA + logo,
    de-jargoned mode toggle, in-editor magic-pencil (no topbar layers button),
    plus the /zernio-logo.png and /download routes."""

    def setUp(self):
        self.srv = _ServerFixture()

    def tearDown(self):
        self.srv.close()

    def test_publish_with_zernio_cta_and_logo(self):
        _, js = self.srv.get("/studio.js")
        self.assertIn("Publish with Zernio", js)
        self.assertIn("/zernio-logo.png", js)
        # terracotta gradient CTA (command-centre primary)
        self.assertIn("#93452A", js)

    def test_free_transform_jargon_removed(self):
        _, js = self.srv.get("/studio.js")
        self.assertNotIn("Free transform", js)
        # behavior kept via a de-jargoned mode toggle
        self.assertIn('mkPill("Browse")', js)

    def test_layers_button_not_in_topbar(self):
        # The magic-pencil is in-editor (Fix #2); the topbar no longer appends layersBtn.
        _, js = self.srv.get("/studio.js")
        self.assertNotIn("bar.appendChild(layersBtn)", js)
        # but the shared decompose path is still exposed for the in-editor pencil
        self.assertIn("window.__studioBreakIntoLayers", js)

    def test_zernio_logo_served(self):
        with urllib.request.urlopen(self.srv.base + "/zernio-logo.png", timeout=10) as r:
            self.assertEqual(r.status, 200)
            self.assertEqual(r.headers.get("Content-Type"), "image/png")
            self.assertTrue(r.read(8).startswith(b"\x89PNG"))

    def test_download_zips_baked_slides(self):
        import io as _io
        import zipfile as _zip
        (self.srv.run / "slide-01.png").write_bytes(_real_png(40, 50))
        (self.srv.run / "slide-02.png").write_bytes(_real_png(40, 50))
        with urllib.request.urlopen(self.srv.base + "/download", timeout=10) as r:
            self.assertEqual(r.status, 200)
            self.assertEqual(r.headers.get("Content-Type"), "application/zip")
            data = r.read()
        names = _zip.ZipFile(_io.BytesIO(data)).namelist()
        self.assertEqual(sorted(names), ["slide-01.png", "slide-02.png"])

    def test_download_404_when_no_slides(self):
        with self.assertRaises(urllib.error.HTTPError) as ctx:
            self.srv.get("/download")
        self.assertEqual(ctx.exception.code, 404)


# ── AIOS-131 front: first comment ────────────────────────────────────────────
class TestFirstCommentHelpers(unittest.TestCase):
    """Unit tests for _read_post_yaml_key and _patch_first_comment_yaml."""

    def setUp(self):
        self._td = _tempfile.TemporaryDirectory()
        self.run = _Path(self._td.name)

    def tearDown(self):
        self._td.cleanup()

    def test_read_key_missing_file(self):
        self.assertIsNone(CS._read_post_yaml_key(self.run, "first_comment"))

    def test_read_key_present_quoted(self):
        (self.run / "post.yaml").write_text(
            'platform: linkedin\nfirst_comment: "hello world"\n', encoding="utf-8")
        self.assertEqual(CS._read_post_yaml_key(self.run, "first_comment"), "hello world")

    def test_read_key_missing_key(self):
        (self.run / "post.yaml").write_text("platform: linkedin\n", encoding="utf-8")
        self.assertIsNone(CS._read_post_yaml_key(self.run, "first_comment"))

    def test_patch_adds_key_preserving_others(self):
        (self.run / "post.yaml").write_text("platform: linkedin\nformat: carousel\n",
                                            encoding="utf-8")
        CS._patch_first_comment_yaml(self.run, "Link in first comment")
        txt = (self.run / "post.yaml").read_text(encoding="utf-8")
        self.assertIn("first_comment", txt)
        self.assertIn("Link in first comment", txt)
        self.assertIn("platform: linkedin", txt)
        self.assertIn("format: carousel", txt)

    def test_patch_updates_existing_key(self):
        (self.run / "post.yaml").write_text('first_comment: "old"\n', encoding="utf-8")
        CS._patch_first_comment_yaml(self.run, "new value")
        txt = (self.run / "post.yaml").read_text(encoding="utf-8")
        self.assertIn("new value", txt)
        self.assertNotIn('"old"', txt)
        self.assertEqual(txt.count("first_comment"), 1)

    def test_patch_removes_key_when_empty(self):
        (self.run / "post.yaml").write_text(
            'platform: linkedin\nfirst_comment: "old"\n', encoding="utf-8")
        CS._patch_first_comment_yaml(self.run, "")
        txt = (self.run / "post.yaml").read_text(encoding="utf-8")
        self.assertNotIn("first_comment", txt)
        self.assertIn("platform: linkedin", txt)

    def test_patch_creates_file_when_missing(self):
        CS._patch_first_comment_yaml(self.run, "test value")
        self.assertTrue((self.run / "post.yaml").is_file())
        self.assertIn("test value", (self.run / "post.yaml").read_text(encoding="utf-8"))

    def test_roundtrip(self):
        CS._patch_first_comment_yaml(self.run, "https://example.com/post")
        self.assertEqual(
            CS._read_post_yaml_key(self.run, "first_comment"), "https://example.com/post")


class TestFirstComment(unittest.TestCase):
    """AIOS-131 front — first comment persists to post.yaml and reaches /post."""

    def setUp(self):
        self.srv = _ServerFixture()

    def tearDown(self):
        self.srv.close()

    def test_save_first_comment_endpoint_persists_to_post_yaml(self):
        code, res = self.srv.post("/save-first-comment", {"first_comment": "Check the link below"})
        self.assertEqual(code, 200)
        self.assertTrue(res["ok"])
        py = self.srv.run / "post.yaml"
        self.assertTrue(py.is_file())
        txt = py.read_text(encoding="utf-8")
        self.assertIn("first_comment", txt)
        self.assertIn("Check the link below", txt)

    def test_save_first_comment_clears_when_empty(self):
        (self.srv.run / "post.yaml").write_text('first_comment: "old"\n', encoding="utf-8")
        code, res = self.srv.post("/save-first-comment", {"first_comment": ""})
        self.assertEqual(code, 200)
        self.assertTrue(res["ok"])
        txt = (self.srv.run / "post.yaml").read_text(encoding="utf-8")
        self.assertNotIn("first_comment", txt)

    def test_save_first_comment_requires_string(self):
        with self.assertRaises(urllib.error.HTTPError) as ctx:
            self.srv.post("/save-first-comment", {})
        self.assertEqual(ctx.exception.code, 400)

    def test_load_returns_first_comment_from_post_yaml(self):
        (self.srv.run / "post.yaml").write_text(
            'platform: linkedin\nfirst_comment: "My CTA link"\n', encoding="utf-8")
        _, body = self.srv.get("/load")
        data = json.loads(body)
        self.assertEqual(data.get("firstComment"), "My CTA link")

    def test_load_returns_empty_string_when_no_first_comment(self):
        _, body = self.srv.get("/load")
        data = json.loads(body)
        self.assertEqual(data.get("firstComment"), "")

    def test_save_general_persists_first_comment(self):
        self.srv.post("/save", {"tweaks": {}, "comments": {},
                                "caption": "cap", "first_comment": "Save path"})
        txt = (self.srv.run / "post.yaml").read_text(encoding="utf-8")
        self.assertIn("Save path", txt)

    def test_save_general_without_first_comment_does_not_clobber(self):
        (self.srv.run / "post.yaml").write_text('first_comment: "keep me"\n', encoding="utf-8")
        self.srv.post("/save", {"tweaks": {}, "comments": {}})
        txt = (self.srv.run / "post.yaml").read_text(encoding="utf-8")
        self.assertIn("keep me", txt)

    def test_post_passes_first_comment_flag_from_body(self):
        import subprocess as _sp
        captured = {}
        orig_key = CS._zernio_key_present
        CS._zernio_key_present = lambda run: True

        def fake_run(argv, **kwargs):
            captured["argv"] = argv
            return _sp.CompletedProcess(argv, 0,
                stdout=json.dumps({"ok": True, "status": "published"}), stderr="")
        orig_run = _sp.run
        _sp.run = fake_run
        try:
            self.srv.post("/post", {"platform": "linkedin", "mode": "publishNow",
                                    "firstComment": "https://example.com"})
            self.assertIn("--first-comment", captured["argv"])
            idx = captured["argv"].index("--first-comment")
            self.assertEqual(captured["argv"][idx + 1], "https://example.com")
        finally:
            CS._zernio_key_present = orig_key
            _sp.run = orig_run

    def test_parity_post_yaml_is_shared_source(self):
        """PARITY: when firstComment not in body, /post reads post.yaml directly —
        same source as CLI (publish_rest.py first_comment fallback)."""
        import subprocess as _sp
        (self.srv.run / "post.yaml").write_text(
            'platform: linkedin\nformat: carousel\nfirst_comment: "yaml-source"\n',
            encoding="utf-8")
        captured = {}
        orig_key = CS._zernio_key_present
        CS._zernio_key_present = lambda run: True

        def fake_run(argv, **kwargs):
            captured["argv"] = argv
            return _sp.CompletedProcess(argv, 0,
                stdout=json.dumps({"ok": True, "status": "published"}), stderr="")
        orig_run = _sp.run
        _sp.run = fake_run
        try:
            self.srv.post("/post", {"platform": "linkedin", "mode": "publishNow"})
            self.assertIn("--first-comment", captured["argv"])
            idx = captured["argv"].index("--first-comment")
            self.assertEqual(captured["argv"][idx + 1], "yaml-source")
        finally:
            CS._zernio_key_present = orig_key
            _sp.run = orig_run

    def test_post_omits_first_comment_flag_when_absent(self):
        """No body firstComment and no post.yaml first_comment → no --first-comment."""
        import subprocess as _sp
        captured = {}
        orig_key = CS._zernio_key_present
        CS._zernio_key_present = lambda run: True

        def fake_run(argv, **kwargs):
            captured["argv"] = argv
            return _sp.CompletedProcess(argv, 0,
                stdout=json.dumps({"ok": True, "status": "published"}), stderr="")
        orig_run = _sp.run
        _sp.run = fake_run
        try:
            self.srv.post("/post", {"platform": "linkedin", "mode": "publishNow"})
            self.assertNotIn("--first-comment", captured["argv"])
        finally:
            CS._zernio_key_present = orig_key
            _sp.run = orig_run


class TestFirstCommentJS(unittest.TestCase):
    """AIOS-131 front — first comment textarea in STUDIO_JS publish panel."""

    def setUp(self):
        self.srv = _ServerFixture()

    def tearDown(self):
        self.srv.close()

    def test_first_comment_field_label_in_js(self):
        _, js = self.srv.get("/studio.js")
        self.assertIn("First comment", js)

    def test_first_comment_save_endpoint_wired(self):
        _, js = self.srv.get("/studio.js")
        self.assertIn("/save-first-comment", js)

    def test_first_comment_textarea_variable_present(self):
        _, js = self.srv.get("/studio.js")
        self.assertIn("firstCommentTa", js)

    def test_first_comment_passed_in_post_payload(self):
        _, js = self.srv.get("/studio.js")
        self.assertIn("firstComment: firstCommentTa.value", js)

    def test_first_comment_loaded_from_load_response(self):
        _, js = self.srv.get("/studio.js")
        self.assertIn("window.__firstComment", js)
        self.assertIn("res.firstComment", js)


# ── AIOS-139 Template mode ────────────────────────────────────────────────────


def _make_template_run():
    """Minimal template directory: template.html + instructions.md + preview.png."""
    td = _tempfile.TemporaryDirectory()
    root = _Path(td.name)
    tmpl = (
        "<!doctype html><html><head><meta charset='utf-8'><style>"
        "html,body{margin:0;width:1080px;height:1350px}"
        "</style></head><body>"
        '<div data-slot="HEADLINE">{{HEADLINE}}</div></body></html>'
    )
    instr = (
        "# Cover template\n\n## Slots\n\n"
        '- **HEADLINE** — headline text\n'
        '  - bbox: 10% 20% 80% 15%\n  - style: text\n  - sample: "Hello"\n'
    )
    (root / "template.html").write_text(tmpl, encoding="utf-8")
    (root / "instructions.md").write_text(instr, encoding="utf-8")
    (root / "preview.png").write_bytes(_real_png(1080, 1350))
    assets_dir = root / "assets"
    assets_dir.mkdir()
    (assets_dir / "ref-canonical.png").write_bytes(_real_png(1080, 1350))
    return td


class TestSetupTemplateRun(unittest.TestCase):
    """_setup_template_run creates the _slides/slide-01/ layout expected by
    _find_slides_info, seeding slide-01.png from preview.png."""

    def test_creates_slides_dir_and_metadata(self):
        td = _make_template_run()
        run = _Path(td.name)
        try:
            CS._setup_template_run(run)
            meta_path = run / "_slides" / "slide-01" / "metadata.json"
            self.assertTrue(meta_path.is_file())
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            self.assertEqual(meta["template_dir"], str(run))
        finally:
            td.cleanup()

    def test_seeds_slide_png_from_preview(self):
        td = _make_template_run()
        run = _Path(td.name)
        try:
            CS._setup_template_run(run)
            self.assertTrue((run / "slide-01.png").is_file())
        finally:
            td.cleanup()

    def test_idempotent(self):
        td = _make_template_run()
        run = _Path(td.name)
        try:
            CS._setup_template_run(run)
            CS._setup_template_run(run)   # second call must not raise or corrupt
            meta = json.loads(
                (run / "_slides" / "slide-01" / "metadata.json").read_text(encoding="utf-8"))
            self.assertEqual(meta["template_dir"], str(run))
        finally:
            td.cleanup()

    def test_no_op_when_no_template_html(self):
        td = _tempfile.TemporaryDirectory()
        run = _Path(td.name)
        try:
            CS._setup_template_run(run)
            self.assertFalse((run / "_slides").exists())
        finally:
            td.cleanup()

    def test_does_not_overwrite_existing_slide_png(self):
        td = _make_template_run()
        run = _Path(td.name)
        sentinel = b"existing-sentinel"
        (run / "slide-01.png").write_bytes(sentinel)
        try:
            CS._setup_template_run(run)
            self.assertEqual((run / "slide-01.png").read_bytes(), sentinel)
        finally:
            td.cleanup()

    def test_rich_slide_path_seeds_slide01_baseline(self):
        """P0 #2: when a RICH emitted slide exists (id != 'slide-01'),
        _setup_template_run still seeds a slide-01.png baseline from preview.png so
        Approve-as-is (which resolves slide-01.png) finds the generated v1 even when
        the active slide id differs and the user approves without editing."""
        td = _make_template_run()
        run = _Path(td.name)
        # Emit a RICH slide named 'preview' carrying non-empty `data` (the real
        # builder path), NOT 'slide-01'.
        rich = run / "_slides" / "preview"
        rich.mkdir(parents=True)
        (rich / "metadata.json").write_text(
            json.dumps({"template_dir": str(run), "data": {"HEADLINE": "Hi"}}),
            encoding="utf-8")
        try:
            CS._setup_template_run(run)
            self.assertTrue((run / "preview.png").is_file())
            self.assertTrue((run / "slide-01.png").is_file(),
                            "rich-slide path must seed a slide-01.png baseline")
        finally:
            td.cleanup()


class TestInjectShimMode(unittest.TestCase):
    def test_post_mode_embeds_post_sentinel(self):
        out = CS._inject_shim("<html><body></body></html>", "post")
        self.assertIn('window.__studioMode="post"', out)
        self.assertIn('<script src="/studio.js"></script>', out)

    def test_template_mode_embeds_template_sentinel(self):
        out = CS._inject_shim("<html><body></body></html>", "template")
        self.assertIn('window.__studioMode="template"', out)

    def test_default_mode_is_post(self):
        out = CS._inject_shim("<html><body></body></html>")
        self.assertIn('window.__studioMode="post"', out)

    def test_mode_script_before_studio_js(self):
        out = CS._inject_shim("<html><body></body></html>", "template")
        mode_pos = out.index("__studioMode")
        js_pos = out.index("/studio.js")
        self.assertLess(mode_pos, js_pos)


class TestTemplateModeServer(unittest.TestCase):
    """Template mode server: correct HTML, mode guards on new endpoints."""

    def setUp(self):
        td = _make_template_run()
        self._td = td
        run = _Path(td.name)
        self.run = run
        state = CS.StudioState(run, None, mode="template")
        self.httpd = ThreadingHTTPServer(("127.0.0.1", 0), CS.make_handler(state))
        self.port = self.httpd.server_address[1]
        import threading
        threading.Thread(target=self.httpd.serve_forever, daemon=True).start()

    def tearDown(self):
        self.httpd.shutdown(); self.httpd.server_close(); self._td.cleanup()

    @property
    def base(self):
        return f"http://127.0.0.1:{self.port}"

    def _get(self, path):
        with urllib.request.urlopen(self.base + path, timeout=10) as r:
            return r.status, r.read().decode()

    def _post(self, path, obj):
        req = urllib.request.Request(
            self.base + path, data=json.dumps(obj).encode(),
            headers={"Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=10) as r:
            return r.status, json.loads(r.read().decode())

    def test_html_injects_template_mode_sentinel(self):
        _, html = self._get("/")
        self.assertIn('window.__studioMode="template"', html)

    def test_compare_endpoint_mode_guard_in_post_mode(self):
        """POST /compare on a post-mode server returns 400."""
        td2 = T._make_run_folder()
        run2 = _Path(td2.name)
        state2 = CS.StudioState(run2, None, mode="post")
        httpd2 = ThreadingHTTPServer(("127.0.0.1", 0), CS.make_handler(state2))
        port2 = httpd2.server_address[1]
        import threading
        threading.Thread(target=httpd2.serve_forever, daemon=True).start()
        try:
            req = urllib.request.Request(
                f"http://127.0.0.1:{port2}/compare",
                data=json.dumps({"mode": "overlay"}).encode(),
                headers={"Content-Type": "application/json"}, method="POST")
            with self.assertRaises(urllib.error.HTTPError) as ctx:
                urllib.request.urlopen(req, timeout=5)
            self.assertEqual(ctx.exception.code, 400)
        finally:
            httpd2.shutdown(); httpd2.server_close(); td2.cleanup()

    def test_approve_endpoint_mode_guard_in_post_mode(self):
        """POST /approve on a post-mode server returns 400."""
        td2 = T._make_run_folder()
        run2 = _Path(td2.name)
        state2 = CS.StudioState(run2, None, mode="post")
        httpd2 = ThreadingHTTPServer(("127.0.0.1", 0), CS.make_handler(state2))
        port2 = httpd2.server_address[1]
        import threading
        threading.Thread(target=httpd2.serve_forever, daemon=True).start()
        try:
            req = urllib.request.Request(
                f"http://127.0.0.1:{port2}/approve",
                data=json.dumps({}).encode(),
                headers={"Content-Type": "application/json"}, method="POST")
            with self.assertRaises(urllib.error.HTTPError) as ctx:
                urllib.request.urlopen(req, timeout=5)
            self.assertEqual(ctx.exception.code, 400)
        finally:
            httpd2.shutdown(); httpd2.server_close(); td2.cleanup()

    def test_compare_no_ref_returns_error(self):
        """POST /compare when ref-canonical.png is missing returns ok:false."""
        import shutil as _sh
        _sh.rmtree(self.run / "assets", ignore_errors=True)
        _, res = self._post("/compare", {"mode": "side-by-side"})
        self.assertFalse(res["ok"])
        self.assertIn("ref-canonical.png", res["error"])

    def test_compare_invalid_mode_returns_400(self):
        req = urllib.request.Request(
            self.base + "/compare", data=json.dumps({"mode": "bogus"}).encode(),
            headers={"Content-Type": "application/json"}, method="POST")
        with self.assertRaises(urllib.error.HTTPError) as ctx:
            urllib.request.urlopen(req, timeout=5)
        self.assertEqual(ctx.exception.code, 400)

    def test_approve_copies_slide_to_preview(self):
        """POST /approve copies slide-01.png to preview.png and persists tweaks."""
        (self.run / "slide-01.png").write_bytes(_real_png(1080, 1350))
        tweaks = {"slide-01": {"HEADLINE": {"text": "Approved"}}}
        _, res = self._post("/approve", {"tweaks": tweaks})
        self.assertTrue(res["ok"])
        self.assertTrue((self.run / "preview.png").is_file())
        self.assertTrue((self.run / "tweaks.json").is_file())
        saved = json.loads((self.run / "tweaks.json").read_text(encoding="utf-8"))
        self.assertEqual(saved, tweaks)

    def test_approve_updates_manifest_when_present(self):
        """POST /approve marks the parent pool manifest entry approved (separate
        marker) while KEEPING status='ready' so it still counts as renderable."""
        (self.run / "slide-01.png").write_bytes(_real_png(1080, 1350))
        slug = self.run.name
        pool_dir = self.run.parent
        manifest = [{"slug": slug, "status": "ready", "preview_path": "old.png"}]
        (pool_dir / "manifest.json").write_text(
            json.dumps(manifest), encoding="utf-8")
        _, res = self._post("/approve", {"tweaks": {}})
        self.assertTrue(res["ok"])
        self.assertTrue(res["manifest_updated"])
        updated = json.loads(
            (pool_dir / "manifest.json").read_text(encoding="utf-8"))
        entry = next(e for e in updated if e.get("slug") == slug)
        self.assertEqual(entry["status"], "ready")
        self.assertTrue(entry.get("approved"))

    def test_approve_copies_preview_to_pool_preview_dir(self):
        """POST /approve copies preview.png to pool/_preview/{slug}.png."""
        (self.run / "slide-01.png").write_bytes(_real_png(1080, 1350))
        _, res = self._post("/approve", {"tweaks": {}})
        self.assertTrue(res["ok"])
        slug = self.run.name
        preview_copy = self.run.parent / "_preview" / f"{slug}.png"
        self.assertTrue(preview_copy.is_file())

    def test_approve_no_slide_returns_error(self):
        """POST /approve without a baked slide returns ok:false."""
        # _setup_template_run seeds slide-01.png from preview.png; remove it
        # so this test exercises the "not yet baked" branch.
        (self.run / "slide-01.png").unlink(missing_ok=True)
        _, res = self._post("/approve", {})
        self.assertFalse(res["ok"])
        self.assertIn("baked", res["error"].lower())


def _make_image_template_run(slug: str = "one-page-system-cover"):
    """A template whose ONLY content is a full-bleed slotted <img> with an EMPTY
    src — so a no-tweak bake is white, and the bg only appears when the parity
    script swaps img.src from an imgSrc tweak. The dir is named *slug* so the
    /approve repro matches the run-07 case (one-page-system-cover) exactly:
    preview.png shares the dir, and the pool _preview copy is keyed by it.
    """
    td = _tempfile.TemporaryDirectory()
    parent = _Path(td.name)
    root = parent / slug
    root.mkdir()
    tmpl = (
        "<!doctype html><html><head><meta charset='utf-8'><style>"
        "html,body{margin:0;width:1080px;height:1350px;background:#fff}"
        ".bg{position:absolute;inset:0;width:1080px;height:1350px;object-fit:cover}"
        "</style></head><body>"
        '<img class="bg" data-slot="PHOTO_MAIN" src="" alt="cover">'
        '<div data-slot="HEADLINE">{{HEADLINE}}</div>'
        "</body></html>"
    )
    instr = (
        "# Cover template\n\n## Slots\n\n"
        '- **PHOTO_MAIN** — background photo\n'
        '  - bbox: 0% 0% 100% 100%\n  - style: image\n'
        '- **HEADLINE** — headline text\n'
        '  - bbox: 10% 20% 80% 15%\n  - style: text\n  - sample: "Hello"\n'
    )
    (root / "template.html").write_text(tmpl, encoding="utf-8")
    (root / "instructions.md").write_text(instr, encoding="utf-8")
    (root / "preview.png").write_bytes(_real_png(1080, 1350))
    (root / "assets").mkdir()
    (root / "assets" / "ref-canonical.png").write_bytes(_real_png(1080, 1350))
    # A pool manifest in the parent pins pool_dir to THIS dir during /approve's
    # ancestor walk (otherwise a stray manifest.json higher in the OS temp tree
    # would redirect the _preview copy out of the fixture — test-isolation only).
    (parent / "manifest.json").write_text(
        json.dumps([{"slug": slug, "status": "ready",
                     "template_html": f"{slug}/template.html"}]),
        encoding="utf-8")
    return td, root


class TestApproveBgHonorsSlideTweaks(unittest.TestCase):
    """r5f-followups Fix 1 — /approve rebakes preview.png honouring slide-keyed
    tweaks (was: white <img src=""> because the rebake omitted --tweaks-slide, so
    render keyed the tweaks by the "preview" output stem and the imgSrc swap never
    ran). Repro of run-07 `one-page-system-cover` (cold conf 0.97)."""

    def _serve(self, run):
        state = CS.StudioState(run, None, mode="template")
        httpd = ThreadingHTTPServer(("127.0.0.1", 0), CS.make_handler(state))
        port = httpd.server_address[1]
        threading.Thread(target=httpd.serve_forever, daemon=True).start()
        return httpd, port

    def _post(self, port, path, obj):
        req = urllib.request.Request(
            f"http://127.0.0.1:{port}{path}", data=json.dumps(obj).encode(),
            headers={"Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=200) as r:
            return r.status, json.loads(r.read().decode())

    @unittest.skipUnless(_playwright_ready() and _pil_ready(),
                         "Playwright/Chromium + Pillow required for the bg bake assertion")
    def test_approve_preview_contains_bg_from_imgsrc_tweak(self):
        td, run = _make_image_template_run("one-page-system-cover")
        httpd, port = self._serve(run)
        try:
            # A colourful background, sent exactly as the editor sends a Replace-image
            # tweak: an imgSrc data: URI keyed by the SLIDE id (slide-01), NOT "preview".
            bg_uri = _png_data_uri(_varied_png(1080, 1350))
            tweaks = {"slide-01": {"PHOTO_MAIN": {"imgSrc": bg_uri}}}
            _, res = self._post(port, "/approve", {"tweaks": tweaks})
            self.assertTrue(res["ok"], res.get("error"))

            preview = run / "preview.png"
            self.assertTrue(preview.is_file())
            mean, std = _png_mean_and_std(preview)
            # The bg landed: NOT a near-white blank (mean≈255, std≈0). The varied
            # fixture composites to a markedly darker, high-variance image.
            self.assertLess(mean, 230.0,
                            f"preview.png looks near-white (mean={mean:.1f}) — bg dropped on Save")
            self.assertGreater(std, 10.0,
                               f"preview.png has no colour variance (std={std:.1f}) — bg not applied")

            # The pool _preview/<slug>.png copy must carry the SAME bg (content_studio
            # copies preview.png there; a white copy would ship a blank thumbnail).
            preview_copy = run.parent / "_preview" / "one-page-system-cover.png"
            self.assertTrue(preview_copy.is_file())
            cmean, cstd = _png_mean_and_std(preview_copy)
            self.assertLess(cmean, 230.0,
                            f"_preview copy near-white (mean={cmean:.1f}) — bg dropped")
            self.assertGreater(cstd, 10.0)
        finally:
            httpd.shutdown(); httpd.server_close(); td.cleanup()

    @unittest.skipUnless(_playwright_ready() and _pil_ready(),
                         "Playwright/Chromium + Pillow required for the bg bake assertion")
    def test_approve_without_imgsrc_stays_white_and_slide_unaffected(self):
        """Control + no-regression: approving the SAME template with NO imgSrc tweak
        bakes the (white) baseline — confirming the bg in the test above comes from
        the honoured tweak — while a per-slide bake of slide-01 with its own imgSrc
        still composites correctly (the proven _rebake_slide path is untouched)."""
        td, run = _make_image_template_run("one-page-system-cover")
        httpd, port = self._serve(run)
        try:
            # (a) approve with empty tweaks → preview stays near-white (no bg to add).
            _, res = self._post(port, "/approve", {"tweaks": {}})
            self.assertTrue(res["ok"], res.get("error"))
            mean, std = _png_mean_and_std(run / "preview.png")
            self.assertGreater(mean, 245.0,
                               f"empty-tweak approve unexpectedly non-white (mean={mean:.1f})")

            # (b) the slide-01 rebake path (used by post-mode /apply + /save) still
            # honours an imgSrc and composites the bg — proving Fix 1 left it intact.
            state = CS.StudioState(run, None, mode="template")
            bg_uri = _png_data_uri(_varied_png(1080, 1350))
            r = CS._rebake_slide(
                state, "slide-01", {"slide-01": {"PHOTO_MAIN": {"imgSrc": bg_uri}}})
            self.assertTrue(r["ok"], r.get("error"))
            smean, sstd = _png_mean_and_std(run / "slide-01.png")
            self.assertLess(smean, 230.0,
                            f"slide-01.png near-white (mean={smean:.1f}) — rebake regressed")
            self.assertGreater(sstd, 10.0)
        finally:
            httpd.shutdown(); httpd.server_close(); td.cleanup()


class TestConferenceFreshPreview(unittest.TestCase):
    """studio-conference-fresh-preview — the conference render column must reflect
    the CURRENT edited state. Edits live in tweaks.json but were never re-baked into
    the displayed preview.png, so /compare-images served the pre-edit image. The fix
    re-bakes preview.png from tweaks.json on conference load (same path as /approve),
    copies it to the gallery's _preview/<id>.png, and returns a render_version
    cache-buster that changes when the preview changes."""

    def _serve(self, run):
        state = CS.StudioState(run, None, mode="template")
        httpd = ThreadingHTTPServer(("127.0.0.1", 0), CS.make_handler(state))
        port = httpd.server_address[1]
        threading.Thread(target=httpd.serve_forever, daemon=True).start()
        return httpd, port

    def _post(self, port, path, obj):
        req = urllib.request.Request(
            f"http://127.0.0.1:{port}{path}", data=json.dumps(obj).encode(),
            headers={"Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=200) as r:
            return r.status, json.loads(r.read().decode())

    @staticmethod
    def _datauri_to_tmp(uri: str) -> _Path:
        raw = base64.b64decode(uri.split(",", 1)[1])
        f = _tempfile.NamedTemporaryFile(suffix=".png", delete=False)
        f.write(raw); f.close()
        return _Path(f.name)

    @unittest.skipUnless(_playwright_ready() and _pil_ready(),
                         "Playwright/Chromium + Pillow required for the bg bake assertion")
    def test_compare_images_rebakes_stale_preview_from_tweaks(self):
        """RED→GREEN: a stale (white) preview.png + a tweaks.json carrying an imgSrc
        bg → /compare-images must return a render that HAS the bg (re-baked), not the
        stale white preview. The _preview/<slug>.png gallery copy must carry it too."""
        td, run = _make_image_template_run("one-page-system-cover")
        # The on-disk preview.png is the stale, pre-edit, near-WHITE image.
        self.assertGreater(_png_mean_and_std(run / "preview.png")[0], 245.0)
        # The user's edit lives ONLY in tweaks.json (slide-keyed imgSrc) — never baked.
        bg_uri = _png_data_uri(_varied_png(1080, 1350))
        (run / "tweaks.json").write_text(
            json.dumps({"slide-01": {"PHOTO_MAIN": {"imgSrc": bg_uri}}}),
            encoding="utf-8")
        httpd, port = self._serve(run)
        try:
            _, res = self._post(port, "/compare-images",
                                {"template_id": "one-page-system-cover"})
            self.assertTrue(res["ok"], res.get("error"))
            self.assertIsNotNone(res.get("render"), "render data-URI should be present")
            tmp = self._datauri_to_tmp(res["render"])
            try:
                mean, std = _png_mean_and_std(tmp)
            finally:
                tmp.unlink(missing_ok=True)
            self.assertLess(mean, 230.0,
                            f"conference render still near-white (mean={mean:.1f}) — "
                            "tweaks.json not re-baked on load")
            self.assertGreater(std, 10.0,
                               f"conference render has no colour variance (std={std:.1f})")
            # The on-disk preview.png was re-baked in place (preview == bake).
            pmean, _ = _png_mean_and_std(run / "preview.png")
            self.assertLess(pmean, 230.0, "preview.png on disk was not re-baked")
            # The gallery copy carries the SAME bg (conference == gallery).
            copy = run.parent / "_preview" / "one-page-system-cover.png"
            self.assertTrue(copy.is_file(), "_preview/<slug>.png copy not written")
            cmean, cstd = _png_mean_and_std(copy)
            self.assertLess(cmean, 230.0,
                            f"_preview copy near-white (mean={cmean:.1f})")
            self.assertGreater(cstd, 10.0)
        finally:
            httpd.shutdown(); httpd.server_close(); td.cleanup()

    @unittest.skipUnless(_playwright_ready() and _pil_ready(),
                         "Playwright/Chromium + Pillow required for the bg bake assertion")
    def test_compare_images_render_version_changes_with_preview(self):
        """The cache-buster (render_version) must differ before vs after the preview
        content changes, so the browser never serves a cached stale image."""
        td, run = _make_image_template_run("one-page-system-cover")
        httpd, port = self._serve(run)
        try:
            # (1) No tweaks → render is the (white) baseline; capture its version.
            _, res0 = self._post(port, "/compare-images",
                                 {"template_id": "one-page-system-cover"})
            self.assertTrue(res0["ok"], res0.get("error"))
            v0 = res0.get("render_version")
            self.assertTrue(v0, "render_version missing on baseline")
            # (2) The user edits (imgSrc bg) → re-bake on next load changes the preview.
            bg_uri = _png_data_uri(_varied_png(1080, 1350))
            (run / "tweaks.json").write_text(
                json.dumps({"slide-01": {"PHOTO_MAIN": {"imgSrc": bg_uri}}}),
                encoding="utf-8")
            _, res1 = self._post(port, "/compare-images",
                                 {"template_id": "one-page-system-cover"})
            self.assertTrue(res1["ok"], res1.get("error"))
            v1 = res1.get("render_version")
            self.assertTrue(v1, "render_version missing after edit")
            self.assertNotEqual(v0, v1,
                                "render_version did not change after the preview changed "
                                "— cache-buster is stale")
        finally:
            httpd.shutdown(); httpd.server_close(); td.cleanup()

    def test_compare_images_no_tweaks_is_noop(self):
        """No tweaks.json → /compare-images must NOT re-bake (leaves preview.png
        byte-identical) and still return the render. Cheap (no browser)."""
        td, run = _make_image_template_run("one-page-system-cover")
        before = (run / "preview.png").read_bytes()
        httpd, port = self._serve(run)
        try:
            _, res = self._post(port, "/compare-images",
                                {"template_id": "one-page-system-cover"})
            self.assertTrue(res["ok"], res.get("error"))
            self.assertIsNotNone(res.get("render"))
            after = (run / "preview.png").read_bytes()
            self.assertEqual(before, after,
                             "preview.png changed with no tweaks.json — bake should be a no-op")
        finally:
            httpd.shutdown(); httpd.server_close(); td.cleanup()

    def test_studio_js_appends_cache_buster_to_render(self):
        """The conference client appends ?v=<render_version> to the render URL (and
        guards against corrupting a data: URI)."""
        self.assertIn("render_version", CS.STUDIO_JS)
        self.assertIn('renderSrc.indexOf("data:")', CS.STUDIO_JS)


class TestTemplateModeJS(unittest.TestCase):
    """STUDIO_JS carries all template-mode chrome."""

    def test_studio_js_has_is_template_mode_check(self):
        self.assertIn("isTemplateMode", CS.STUDIO_JS)
        self.assertIn('window.__studioMode === "template"', CS.STUDIO_JS)

    def test_studio_js_has_approve_button(self):
        self.assertIn("approveBtn", CS.STUDIO_JS)
        self.assertIn("Approve template", CS.STUDIO_JS)

    def test_studio_js_has_compare_button(self):
        self.assertIn("compareBtn", CS.STUDIO_JS)
        self.assertIn("Compare", CS.STUDIO_JS)
        self.assertIn("/compare", CS.STUDIO_JS)

    def test_studio_js_conference_has_no_line_check(self):
        # The "Run line check" section was removed from the Conference per design
        # (AIOS-190 integration pass) — the Conference is now a focused per-template
        # ref|render comparison, nothing else.
        self.assertNotIn("Run line check", CS.STUDIO_JS)

    def test_studio_js_has_approve_endpoint(self):
        self.assertIn("/approve", CS.STUDIO_JS)

    def test_studio_js_hides_social_chrome(self):
        self.assertIn(".li-head", CS.STUDIO_JS)
        self.assertIn(".li-react", CS.STUDIO_JS)
        self.assertIn(".li-actions", CS.STUDIO_JS)
        self.assertIn("hideSocialChrome", CS.STUDIO_JS)

    def test_studio_js_has_template_studio_badge(self):
        self.assertIn("Template Studio", CS.STUDIO_JS)
        self.assertIn("ts-badge", CS.STUDIO_JS)

    def test_studio_js_publish_not_shown_in_template_mode(self):
        self.assertIn("isTemplateMode", CS.STUDIO_JS)
        # In template mode the buttons array includes approveBtn not publishBtn
        self.assertIn("compareBtn, approveBtn", CS.STUDIO_JS)

    def test_studio_js_compare_panel_modes(self):
        self.assertIn('"side-by-side"', CS.STUDIO_JS)
        self.assertIn('"overlay"', CS.STUDIO_JS)
        self.assertIn('"diff"', CS.STUDIO_JS)
        self.assertIn('"grid"', CS.STUDIO_JS)

    def test_studio_js_arrow_switch_autosaves_first(self):
        """P0 #1: the ‹ › arrow switch path must AUTOSAVE before /select-template so
        unsaved edits survive the reload. The /save call must precede /select-template
        inside go()."""
        js = CS.STUDIO_JS
        go_start = js.index("function go(dir)")
        go_end = js.index("function arrow(", go_start)
        body = js[go_start:go_end]
        self.assertIn('post("/save"', body)
        self.assertIn('post("/select-template"', body)
        self.assertLess(body.index('post("/save"'),
                        body.index('post("/select-template"'),
                        "/save must run before /select-template in the arrow switch")

    def test_studio_js_no_dead_edit_this_template_button(self):
        """P1 #3: the force-hidden 'Edit this template' Conference button is removed."""
        self.assertNotIn("Edit this template", CS.STUDIO_JS)

    def test_studio_js_has_undo(self):
        """P1 #7: Ctrl/Cmd+Z undo wraps applyToSlide and listens for keydown."""
        self.assertIn("installUndo", CS.STUDIO_JS)
        self.assertIn("__csUndoWrapped", CS.STUDIO_JS)
        self.assertIn("metaKey", CS.STUDIO_JS)


class TestTemplateModeMain(unittest.TestCase):
    """CLI --mode argument wires through to serve()."""

    def test_argparse_has_mode_choices(self):
        import io
        import argparse
        # Verify the parser is built correctly by triggering --help.
        # We just check that the STUDIO_JS and serve() accept the parameter.
        self.assertIn("mode", CS.serve.__code__.co_varnames)

    def test_serve_accepts_mode_post(self):
        td = T._make_run_folder()
        run = _Path(td.name)
        try:
            state = CS.StudioState(run, None, mode="post")
            self.assertEqual(state.mode, "post")
        finally:
            td.cleanup()

    def test_serve_accepts_mode_template(self):
        td = _make_template_run()
        run = _Path(td.name)
        try:
            state = CS.StudioState(run, None, mode="template")
            self.assertEqual(state.mode, "template")
            # _setup_template_run was called
            self.assertTrue((run / "_slides" / "slide-01").is_dir())
        finally:
            td.cleanup()

    def test_first_comment_included_in_general_save(self):
        self.assertIn("getFirstComment", CS.STUDIO_JS)
        self.assertIn("first_comment: getFirstComment()", CS.STUDIO_JS)

    def test_first_comment_blur_persists(self):
        self.assertIn("firstCommentTa.addEventListener", CS.STUDIO_JS)
        self.assertIn('"blur"', CS.STUDIO_JS)


class TestPdfCarouselDefaults(unittest.TestCase):
    """Adjust 2: PDF carousel default + 9-image limit enforcement.

    These are structural / JS-source checks (no browser needed):
    • studio.js must contain the logic to auto-enable PDF for linkedin + carousel.
    • studio.js must contain a guard that blocks publish when >9 slides without PDF.
    • The hint copy is present so users understand the reach difference.
    • zernio-rest-fallback.md must document the correct 9-image limit.
    """

    def setUp(self):
        self.srv = _ServerFixture()

    def tearDown(self):
        self.srv.close()

    def test_pdf_toggle_default_enabled_for_linkedin_carousel(self):
        """studio.js must auto-enable PDF when platform=linkedin and carousel (>1 slide)."""
        _, js = self.srv.get("/studio.js")
        self.assertIn("syncPdfDefaults", js,
                      "syncPdfDefaults() function not found in studio.js")
        self.assertIn("pdfCb.checked = true", js,
                      "PDF toggle must default to checked for linkedin carousel")

    def test_nine_image_limit_guard_blocks_publish(self):
        """studio.js must block the Confirm click when >9 slides without PDF on linkedin."""
        _, js = self.srv.get("/studio.js")
        self.assertIn("slideCount > 9", js,
                      "9-image limit check missing from studio.js publish handler")
        self.assertIn("LinkedIn image gallery supports up to 9", js,
                      "9-image limit error message missing from studio.js")

    def test_pdf_hint_text_present(self):
        """studio.js must include the reach-hint explaining PDF vs image-gallery."""
        _, js = self.srv.get("/studio.js")
        self.assertIn("PDF = swipeable carousel", js,
                      "PDF hint copy missing from studio.js")
        self.assertIn("max 9 images", js,
                      "9-image mention missing from PDF hint in studio.js")

    def test_pdf_warn_element_present(self):
        """studio.js must create the pdfWarnWrap element for >9-slide warnings."""
        _, js = self.srv.get("/studio.js")
        self.assertIn("pdfWarnWrap", js,
                      "pdfWarnWrap element not found in studio.js")

    def test_zernio_ref_says_nine_not_twenty(self):
        """zernio-rest-fallback.md must document 9 (not 20) as the image-gallery limit."""
        from pathlib import Path
        ref = (
            Path(__file__).resolve()
            .parent.parent.parent.parent.parent
            / "tool-publisher" / "references" / "zernio-rest-fallback.md"
        )
        if ref.exists():
            text = ref.read_text(encoding="utf-8")
            self.assertIn("up to 9", text,
                          "zernio-rest-fallback.md must say 'up to 9', not 'up to 20'")
            self.assertNotIn("up to 20", text,
                             "stale 'up to 20' still present in zernio-rest-fallback.md")


# ── AIOS-139 Template Pool Conference (Plan 04) ──────────────────────────────

import struct as _struct2  # noqa: E402 (aliased to avoid collision with earlier _struct)
import zlib as _zlib2       # noqa: E402


def _tiny_png_bytes() -> bytes:
    """Return a minimal but decodable 2x2 solid-white RGBA PNG (stdlib only, no Pillow).

    Used to provide a real ``assets/ref-canonical.png`` in the pool fixture so that
    /compare-images can read it and assert a non-empty data-URI, and so the PNG
    signature (\\x89PNG) can be verified.
    """
    def chunk(typ: bytes, data: bytes) -> bytes:
        crc = _zlib2.crc32(typ + data) & 0xFFFFFFFF
        return _struct2.pack(">I", len(data)) + typ + data + _struct2.pack(">I", crc)

    sig = b"\x89PNG\r\n\x1a\n"
    ihdr = chunk(b"IHDR", _struct2.pack(">IIBBBBB", 2, 2, 8, 6, 0, 0, 0))
    # filter byte 0 + 2 white RGBA pixels per row, 2 rows
    row = b"\x00" + (b"\xff\xff\xff\xff" * 2)
    idat = chunk(b"IDAT", _zlib2.compress(row * 2))
    iend = chunk(b"IEND", b"")
    return sig + ihdr + idat + iend


def _make_template_pool(tmp: "_Path", *, real_assets: bool = False) -> dict:
    """Build a 2-template pool fixture inside ``tmp``.

    When ``real_assets`` is True the per-template ``preview.png`` (RENDER pane)
    and ``assets/ref-canonical.png`` (REF pane) are written with genuine,
    visibly-distinct artwork instead of 2x2 placeholders:

      * RENDER ← a high-variance colour PNG (``_varied_png(.., mode=1)``, 1024x1536).
      * REF    ← a high-variance colour PNG (``_varied_png``) at the same size,
        with a different stripe slope, so the two compare panes show distinct images.

    This is what the Playwright gate uses so screenshot 01 genuinely proves a
    side-by-side of two real images (not blank white).  Unit tests keep the
    fast 2x2 placeholders (``real_assets=False``, the default).

    Layout::

        tmp/
          templates/
            test-pool/
              manifest.json      {"templates": [{id:"hero",...}, {id:"body",...}]}
              _shared/
                styles.css
              hero/
                template.html
                preview.png
                assets/ref-canonical.png   (real 2x2 RGBA PNG)
              body/
                template.html
                preview.png
                assets/ref-canonical.png   (real 2x2 RGBA PNG)

    Returns a dict with keys:
      pool_dir, hero_dir, body_dir, brand_context

    Use ``brand_context`` as the ``brand_context`` argument to
    ``render_template.resolve_pool_dir`` so the pool can be located.
    """
    brand_ctx = tmp / "templates" / "test-pool"
    brand_ctx.mkdir(parents=True, exist_ok=True)
    shared = brand_ctx / "_shared"
    shared.mkdir(exist_ok=True)
    (shared / "styles.css").write_text("body{margin:0}", encoding="utf-8")

    tmpl_html = (
        "<!doctype html><html><head><meta charset='utf-8'><style>"
        "html,body{margin:0;width:1080px;height:1350px}"
        "</style></head><body>"
        '<div data-slot="HEADLINE">{{{HEADLINE}}}</div></body></html>'
    )
    instr = (
        "# Template\n\n## Slots\n\n"
        "- **HEADLINE** — headline text\n"
        "  - bbox: 10% 20% 80% 15%\n  - style: text\n  - sample: \"Hello\"\n"
    )
    if real_assets:
        # RENDER + REF panes: two distinct high-variance colour images at the same
        # size so the panes differ visibly (proves a real side-by-side, not a
        # re-used render). Different stripe slopes via the mode arg — no shipped
        # sample asset required.
        render_bytes = _varied_png(1024, 1536, mode=1)
        ref_bytes = _varied_png(1024, 1536)
    else:
        render_bytes = _tiny_png_bytes()
        ref_bytes = _tiny_png_bytes()

    hero_dir = brand_ctx / "hero"
    hero_dir.mkdir(exist_ok=True)
    (hero_dir / "template.html").write_text(tmpl_html, encoding="utf-8")
    (hero_dir / "instructions.md").write_text(instr, encoding="utf-8")
    (hero_dir / "preview.png").write_bytes(render_bytes)
    assets_h = hero_dir / "assets"
    assets_h.mkdir(exist_ok=True)
    (assets_h / "ref-canonical.png").write_bytes(ref_bytes)

    body_dir = brand_ctx / "body"
    body_dir.mkdir(exist_ok=True)
    (body_dir / "template.html").write_text(tmpl_html, encoding="utf-8")
    (body_dir / "instructions.md").write_text(instr, encoding="utf-8")
    (body_dir / "preview.png").write_bytes(render_bytes)
    assets_b = body_dir / "assets"
    assets_b.mkdir(exist_ok=True)
    (assets_b / "ref-canonical.png").write_bytes(ref_bytes)

    manifest = {
        "templates": [
            {"id": "hero", "file": "hero/template.html", "status": "ready"},
            {"id": "body", "file": "body/template.html", "status": "ready"},
        ]
    }
    (brand_ctx / "manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8")

    return {
        "pool_dir": brand_ctx,
        "hero_dir": hero_dir,
        "body_dir": body_dir,
        "brand_context": tmp,
    }


def _rewrite_manifest_builder_native(pool_info: dict) -> None:
    """Rewrite a pool's manifest.json into the ssc-template-builder's NATIVE shape.

    The AI-first builder (ssc-template-builder.md Step 7) hand-writes each entry as
    ``{slug, status, template_dir, template_html, ...}`` — NO ``id``, NO ``file`` —
    with brand_context-rooted paths. This is the off-contract manifest the readers
    must tolerate (AIOS-190). Reuses the dirs ``_make_template_pool`` already created.
    """
    pool_dir = pool_info["pool_dir"]
    pool_name = pool_dir.name
    templates = []
    for tid in ("hero", "body"):
        # Mirror the live builder manifest: brand_context-rooted, full templates/<pool>/ segment.
        base = f"brand_context/templates/{pool_name}/{tid}"
        templates.append({
            "slug": tid,
            "status": "ready",
            "template_dir": base,
            "template_html": f"{base}/template.html",
            "template_card": f"{base}/instructions.md",
            "preview_png": f"{base}/preview.png",
            "ref_canonical": f"{base}/assets/ref-canonical.png",
        })
    (pool_dir / "manifest.json").write_text(
        json.dumps({"pool": pool_name, "templates": templates}, indent=2),
        encoding="utf-8")


class _BuilderNativeManifestTests(unittest.TestCase):
    """AIOS-190 — the reader must tolerate the builder's native manifest schema
    (slug/template_html/template_dir, NO id/file) and resolve each template to its
    OWN dir, not collapse everything to the pool root.
    """

    def setUp(self):
        self.td = _tempfile.TemporaryDirectory()
        self.pool = _make_template_pool(_Path(self.td.name))
        _rewrite_manifest_builder_native(self.pool)
        self.pool_dir = self.pool["pool_dir"]
        self.hero_dir = self.pool["hero_dir"]

    def tearDown(self):
        self.td.cleanup()

    def test_builder_native_returns_one_record_per_template(self):
        recs = CS._resolve_pool_templates(self.hero_dir)
        self.assertEqual(len(recs), 2, "should resolve both builder-native templates")

    def test_builder_native_id_comes_from_slug(self):
        recs = CS._resolve_pool_templates(self.hero_dir)
        self.assertEqual({r["id"] for r in recs}, {"hero", "body"},
                         "id must alias from slug when canonical id is absent")

    def test_builder_native_each_resolves_to_own_dir_not_pool_root(self):
        recs = CS._resolve_pool_templates(self.hero_dir)
        dirs = {r["id"]: _Path(r["template_dir"]) for r in recs}
        # Each points at its own dir, NOT the pool root (the collapse bug).
        self.assertEqual(dirs["hero"], self.pool["hero_dir"].resolve())
        self.assertEqual(dirs["body"], self.pool["body_dir"].resolve())
        self.assertNotEqual(dirs["hero"], self.pool_dir.resolve())
        self.assertNotEqual(dirs["body"], self.pool_dir.resolve())

    def test_builder_native_ref_and_render_paths_exist(self):
        recs = CS._resolve_pool_templates(self.hero_dir)
        for r in recs:
            self.assertTrue(_Path(r["ref"]).is_file(), f"{r['id']}: ref missing")
            self.assertTrue(_Path(r["render"]).is_file(), f"{r['id']}: render missing")

    def test_idempotent_with_canonical_resolution(self):
        """A canonical (id/file) pool and a builder-native (slug/template_html) pool
        over the same dirs must resolve to identical (id, dir, ref) records."""
        canon_td = _tempfile.TemporaryDirectory()
        try:
            canon = _make_template_pool(_Path(canon_td.name))  # canonical id/file manifest

            def _norm(pool):
                recs = CS._resolve_pool_templates(pool["hero_dir"])
                return sorted(
                    (r["id"], _Path(r["template_dir"]).name, _Path(r["ref"]).name)
                    for r in recs
                )

            self.assertEqual(_norm(self.pool), _norm(canon),
                             "builder-native and canonical manifests must resolve identically")
        finally:
            canon_td.cleanup()


class TestNeedsUserDecisionWalk(unittest.TestCase):
    """Bug B — a ``needs-user-decision`` template (builder gate false-positive the
    user confirms IN the Studio) must SURFACE in the pool walk (flagged, not
    auto-promoted), and /approve must flip it to ``ready`` so it counts toward the
    ready_count gate. Excluding it created a catch-22 (never shown → never approved).
    """

    def setUp(self):
        self.td = _tempfile.TemporaryDirectory()
        self.pool = _make_template_pool(_Path(self.td.name))
        self.pool_dir = self.pool["pool_dir"]
        self.hero_dir = self.pool["hero_dir"]
        self.body_dir = self.pool["body_dir"]
        # Flag the body template as needs-user-decision (the gate false-positive).
        mf = self.pool_dir / "manifest.json"
        data = json.loads(mf.read_text(encoding="utf-8"))
        for e in data["templates"]:
            if e["id"] == "body":
                e["status"] = "needs-user-decision"
        mf.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def tearDown(self):
        self.td.cleanup()

    def test_needs_user_decision_template_is_included_in_walk(self):
        recs = CS._resolve_pool_templates(self.hero_dir)
        by_id = {r["id"]: r for r in recs}
        self.assertIn("body", by_id, "needs-user-decision template must surface")
        # Flagged, NOT auto-promoted: status passes through as-is for the UI.
        self.assertEqual(by_id["body"]["status"], "needs-user-decision")

    def test_approve_promotes_needs_user_decision_to_ready(self):
        # Seed a baked slide so /approve can re-bake.
        (self.body_dir / "slide-01.png").write_bytes(
            (self.body_dir / "preview.png").read_bytes())
        state = CS.StudioState(self.hero_dir, None, mode="template")
        httpd = ThreadingHTTPServer(("127.0.0.1", 0), CS.make_handler(state))
        port = httpd.server_address[1]
        threading.Thread(target=httpd.serve_forever, daemon=True).start()
        try:
            req = urllib.request.Request(
                f"http://127.0.0.1:{port}/approve",
                data=json.dumps({"template_id": "body", "tweaks": {}}).encode(),
                headers={"Content-Type": "application/json"}, method="POST")
            with urllib.request.urlopen(req, timeout=30) as r:
                res = json.loads(r.read().decode())
            self.assertTrue(res.get("ok"), res)
        finally:
            httpd.shutdown(); httpd.server_close()
        # Manifest entry is now ready + approved (gate false-positive confirmed).
        data = json.loads((self.pool_dir / "manifest.json").read_text(encoding="utf-8"))
        body = next(e for e in data["templates"] if e["id"] == "body")
        self.assertEqual(body["status"], "ready",
                         "approving a needs-user-decision template must promote it")
        self.assertTrue(body.get("approved"))


class TestSrcdocAutosizeParity(unittest.TestCase):
    """Bug A — the live editor srcdoc must carry the SAME autosize text-fit net the
    bake runs (render_template.autosize_text_fit), so a long headline shrinks to its
    box in the canvas EXACTLY as in the PNG (preview == bake). Without it the live
    headline rendered at the authored cqw size and overflowed onto the photo subject.
    """

    def test_srcdoc_includes_autosize_script_with_bake_constants(self):
        import preview_editor as PE  # noqa: PLC0415
        import render_template as RT  # noqa: PLC0415
        td = _tempfile.TemporaryDirectory()
        try:
            tdir = _Path(td.name)
            tmpl = tdir / "template.html"
            tmpl.write_text(
                "<!DOCTYPE html><html><head></head><body>"
                "<div class='slide' style='width:1080px;height:1350px'>"
                "<div class='headline-zone' data-slot='HEADLINE' "
                "style='position:absolute;height:78%'>"
                "<div class='headline-display'>{{{HEADLINE}}}</div></div>"
                "</div></body></html>",
                encoding="utf-8")
            srcdoc = PE._build_srcdoc(tmpl, {"HEADLINE": "A LONG HEADLINE"}, "", "")
            # The autosize parity script is present…
            self.assertIn("__autosizeRun", srcdoc)
            self.assertIn("document.fonts", srcdoc)
            # …and uses the SAME constants as the bake (parity, not a guess).
            self.assertIn(str(RT.AUTOSIZE_TOL_PX), srcdoc)
            self.assertIn(str(RT.AUTOSIZE_FLOOR_FRAC), srcdoc)
            self.assertIn(str(RT.AUTOSIZE_FLOOR_ABS_PX), srcdoc)
        finally:
            td.cleanup()


class _PoolServerFixture:
    """Start a template-mode server with a 2-template pool, state.run = hero_dir."""

    def __init__(self):
        self.td = _tempfile.TemporaryDirectory()
        self.root = _Path(self.td.name)
        self.pool = _make_template_pool(self.root)
        self.hero_dir = self.pool["hero_dir"]
        self.body_dir = self.pool["body_dir"]
        self.pool_dir = self.pool["pool_dir"]
        # state.run = hero_dir; _resolve_pool_templates will walk up to pool_dir
        self.state = CS.StudioState(self.hero_dir, None, mode="template")
        self.httpd = ThreadingHTTPServer(
            ("127.0.0.1", 0), CS.make_handler(self.state))
        self.port = self.httpd.server_address[1]
        self.thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)
        self.thread.start()

    @property
    def base(self):
        return f"http://127.0.0.1:{self.port}"

    def get(self, path):
        with urllib.request.urlopen(self.base + path, timeout=10) as r:
            return r.status, r.read().decode()

    def post(self, path, obj):
        req = urllib.request.Request(
            self.base + path,
            data=json.dumps(obj).encode(),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, json.loads(r.read().decode())

    def close(self):
        self.httpd.shutdown()
        self.httpd.server_close()
        self.td.cleanup()


# Stable absolute path for the 4 gate screenshots.
_SCREENSHOT_DIR = _Path(__file__).resolve().parent.parent.parent.parent.parent.parent.parent / "_reports" / "assets" / "aios-139-iter2"


class TestConferencePlaywrightGate(unittest.TestCase):
    """Playwright-gated: conference renders real images + pool walk + approved edit persists.

    Captures 4 named screenshots into ``_reports/assets/aios-139-iter2/``:
      01-side-by-side.png  — both ref/render images have naturalWidth > 0 (no Baking hang)
      02-pool-nav.png      — 1/2 -> 2/2 counter transition + Approve on template[1]
      03-edit-persist.png  — tweaks persisted on disk after approve (canonical tweaks file)
      04-canvas.png        — .slide-frame-wrap computed width > 500px (template-mode canvas)

    Skipped cleanly if Chromium/Playwright is unavailable.
    """

    @classmethod
    def setUpClass(cls):
        _SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

    @unittest.skipUnless(_playwright_ready(), "Playwright/Chromium not available")
    def test_conference_4_screenshots(self):
        from playwright.sync_api import sync_playwright  # noqa: PLC0415

        td = _tempfile.TemporaryDirectory()
        root = _Path(td.name)
        # real_assets=True ⇒ RENDER pane gets the genuine repo gpt-image render
        # and REF pane a distinct high-variance image, so the compare panes show
        # real, visibly-different artwork (not blank 2x2 placeholders).
        pool = _make_template_pool(root, real_assets=True)
        hero_dir = pool["hero_dir"]
        body_dir = pool["body_dir"]

        # Seed slide-01.png in both template dirs so /approve has a baked slide.
        # Use the real render bytes (preview.png) so the baked-slide pane also
        # shows genuine content if surfaced.
        _real_slide = (hero_dir / "preview.png").read_bytes()
        (hero_dir / "slide-01.png").write_bytes(_real_slide)
        (body_dir / "slide-01.png").write_bytes((body_dir / "preview.png").read_bytes())

        state = CS.StudioState(hero_dir, None, mode="template")
        httpd = ThreadingHTTPServer(("127.0.0.1", 0), CS.make_handler(state))
        port = httpd.server_address[1]
        threading.Thread(target=httpd.serve_forever, daemon=True).start()
        url = f"http://127.0.0.1:{port}/"

        try:
            with sync_playwright() as p:
                b = p.chromium.launch()
                # Wide + tall viewport so the side-by-side conference panel
                # (two 1024x1536 real images) fits fully in frame.
                pg = b.new_page(viewport={"width": 1500, "height": 1100})
                pg.goto(url)
                pg.wait_for_timeout(1500)

                # ── Open the conference panel ─────────────────────────────────
                pg.evaluate("""() => {
                  var btn = document.getElementById('ts-compare-btn');
                  if (btn) btn.click();
                }""")

                conf_panel = pg.query_selector("#ts-compare-panel")
                self.assertIsNotNone(
                    conf_panel, "conference panel #ts-compare-panel must be open")

                # Poll until BOTH compare panes have decoded real artwork rather than
                # relying on a fixed sleep: the real-asset data-URIs are 1MB+ and can
                # take well over 2s for the browser to fetch (/pool-templates +
                # /compare-images) and decode.  wait_for_function retries until at
                # least two #ts-compare-panel <img> elements report naturalWidth > 100
                # (i.e. genuine images, not 2x2 placeholders or still-loading panes).
                pg.wait_for_function(
                    """() => {
                      var imgs = Array.from(
                        document.querySelectorAll('#ts-compare-panel img'));
                      var ready = imgs.filter(function (im) {
                        return im.complete && im.naturalWidth > 100;
                      });
                      return ready.length >= 2;
                    }""",
                    timeout=15000,
                )

                # ── Screenshot 01: side-by-side ───────────────────────────────
                # Assert both ref and render images are real (naturalWidth > 0)
                img_info = pg.evaluate("""() => {
                  var imgs = document.querySelectorAll('#ts-conf-panel img, .ts-conf-img, img[class*="conf"]');
                  // Fallback: any img inside a div that contains 'Ref' or 'Render' text
                  var all = Array.from(document.querySelectorAll('img'));
                  return all.map(function(im) {
                    return {src: im.src ? im.src.slice(0, 30) : '', nw: im.naturalWidth, nh: im.naturalHeight};
                  });
                }""")
                # The conference loads ref + render as data-URIs.  With real_assets
                # the panes carry genuine artwork, so we require at least TWO loaded
                # data-URI images (ref + render), each clearly larger than a 2x2
                # placeholder (naturalWidth > 100) — this proves a real side-by-side,
                # not a blank/hung pane.
                data_uri_imgs = [i for i in img_info if i.get("src", "").startswith("data:")]
                loaded_imgs = [i for i in data_uri_imgs if i.get("nw", 0) > 0]
                self.assertGreater(
                    len(loaded_imgs), 0,
                    f"At least one conference image must have naturalWidth > 0 (got img_info={img_info!r})")
                real_imgs = [i for i in data_uri_imgs if i.get("nw", 0) > 100]
                self.assertGreaterEqual(
                    len(real_imgs), 2,
                    "Both compare panes must carry real artwork (naturalWidth > 100); "
                    f"got real_imgs={real_imgs!r} of data_uri_imgs={data_uri_imgs!r}")

                ss1 = _SCREENSHOT_DIR / "01-side-by-side.png"
                # Clip to the conference panel so both Reference + Render panes
                # are framed together — proves a genuine side-by-side of real art.
                _panel = pg.query_selector("#ts-compare-panel")
                if _panel:
                    _panel.screenshot(path=str(ss1))
                else:
                    pg.screenshot(path=str(ss1))
                self.assertTrue(ss1.is_file() and ss1.stat().st_size > 0,
                                "01-side-by-side.png must be non-empty")

                # ── Screenshot 02: pool navigation (1/2 -> 2/2) + Approve ────
                counter_text = pg.evaluate("""() => {
                  var c = document.getElementById('ts-conf-counter');
                  return c ? c.textContent.trim() : '';
                }""")
                self.assertIn("1", counter_text,
                              f"Counter should show '1 / 2' but got {counter_text!r}")

                # Click the right-arrow (next template)
                pg.evaluate("""() => {
                  var panel = document.querySelector('[id*="conf"], [class*="conf"]');
                  // Find the '→' button
                  var btns = Array.from(document.querySelectorAll('button'));
                  var next = btns.find(function(b) { return b.textContent.trim() === '→'; });
                  if (next) next.click();
                }""")
                pg.wait_for_timeout(1500)

                counter_text2 = pg.evaluate("""() => {
                  var c = document.getElementById('ts-conf-counter');
                  return c ? c.textContent.trim() : '';
                }""")
                self.assertIn("2", counter_text2,
                              f"Counter should show '2 / 2' after navigation but got {counter_text2!r}")

                # Screenshot 02: capture the counter at 2/2 + right-arrow visible.
                # Clip to the panel so the "2 / 2" counter + nav arrows are in frame.
                ss2 = _SCREENSHOT_DIR / "02-pool-nav.png"
                _panel2 = pg.query_selector("#ts-compare-panel")
                if _panel2:
                    _panel2.screenshot(path=str(ss2))
                else:
                    pg.screenshot(path=str(ss2))
                self.assertTrue(ss2.is_file() and ss2.stat().st_size > 0,
                                "02-pool-nav.png must be non-empty")

                # Drive /approve on the SECOND template (template[1] = body) via fetch
                # (bypasses bakeNow() which requires a real render_template Playwright run,
                # but exercises the /approve endpoint directly as the conference UI would).
                body_tweaks = {"slide-01": {"zones": {"HEADLINE": {"fontSize": 44}}}}
                approve_res = pg.evaluate(
                    """async (args) => {
                      var r = await fetch('/approve', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({template_id: args.template_id, tweaks: args.tweaks})
                      });
                      return await r.json();
                    }""",
                    {"template_id": "body", "tweaks": body_tweaks})
                self.assertTrue(approve_res.get("ok"),
                                f"/approve body failed: {approve_res}")

                # ── Screenshot 03: edit persisted on disk (canonical tweaks file) ──
                # Verify that approving body wrote the tweaks file to body_dir
                body_tweaks_file = body_dir / "tweaks.json"
                self.assertTrue(body_tweaks_file.is_file(),
                                "body/tweaks.json must exist after approving template[1]")

                # Reload the conference view for the body template so the panel
                # reflects the just-approved template (status line / panes refresh).
                pg.wait_for_timeout(600)
                ss3 = _SCREENSHOT_DIR / "03-edit-persist.png"
                _panel3 = pg.query_selector("#ts-compare-panel")
                if _panel3:
                    _panel3.screenshot(path=str(ss3))
                else:
                    pg.screenshot(path=str(ss3))
                self.assertTrue(ss3.is_file() and ss3.stat().st_size > 0,
                                "03-edit-persist.png must be non-empty")

                # ── Screenshot 04: canvas width > 500px (template-mode enlargement) ──
                canvas_width = pg.evaluate("""() => {
                  var wrap = document.querySelector('.slide-frame-wrap');
                  if (!wrap) return 0;
                  return parseFloat(window.getComputedStyle(wrap).width) || wrap.getBoundingClientRect().width;
                }""")
                self.assertGreater(
                    canvas_width, 500,
                    f".slide-frame-wrap computed width must be > 500px in template mode (got {canvas_width})")

                # Close the conference panel so the canvas (with the real render)
                # is captured cleanly for the canvas-size proof shot.
                pg.evaluate("""() => {
                  var pn = document.getElementById('ts-compare-panel');
                  if (pn) {
                    var x = pn.querySelector('button');
                    var btn = document.getElementById('ts-compare-btn');
                    if (btn) btn.click();  // toggle closes the panel
                  }
                }""")
                pg.wait_for_timeout(600)
                ss4 = _SCREENSHOT_DIR / "04-canvas.png"
                pg.screenshot(path=str(ss4))
                self.assertTrue(ss4.is_file() and ss4.stat().st_size > 0,
                                "04-canvas.png must be non-empty")

                b.close()
        finally:
            httpd.shutdown()
            httpd.server_close()
            td.cleanup()


class TestTemplatePoolConference(unittest.TestCase):
    """Multi-template pool fixture + unit tests for pool walk, /compare-images,
    fixed /approve writer, cross-template attribution, and B2 auto-load.

    All server tests use a 2-template pool (hero + body) built in a temp dir.
    The cross-template attribution test proves that approving ``body`` writes
    tweaks under body's OWN directory and never pollutes hero's directory.
    """

    def setUp(self):
        self.srv = _PoolServerFixture()

    def tearDown(self):
        self.srv.close()

    # ── Fixture integrity ─────────────────────────────────────────────────────

    def test_fixture_has_real_ref_canonical_png(self):
        """Each template dir must have a non-empty ref-canonical.png with a valid PNG sig."""
        for name, tdir in [("hero", self.srv.hero_dir), ("body", self.srv.body_dir)]:
            ref = tdir / "assets" / "ref-canonical.png"
            self.assertTrue(ref.is_file(), f"{name}: ref-canonical.png not found")
            data = ref.read_bytes()
            self.assertGreater(len(data), 0, f"{name}: ref-canonical.png is empty")
            self.assertTrue(data[:4] == b"\x89PNG",
                            f"{name}: ref-canonical.png lacks PNG signature")

    # ── Pool walk (_resolve_pool_templates) ───────────────────────────────────

    def test_pool_walk_returns_two_records_in_manifest_order(self):
        """_resolve_pool_templates returns hero then body — manifest order preserved."""
        recs = CS._resolve_pool_templates(self.srv.hero_dir)
        self.assertEqual(len(recs), 2)
        self.assertEqual(recs[0]["id"], "hero")
        self.assertEqual(recs[1]["id"], "body")

    def test_pool_walk_ref_paths_point_to_correct_dirs(self):
        """Each record's ref path points to assets/ref-canonical.png inside its own dir."""
        recs = CS._resolve_pool_templates(self.srv.hero_dir)
        hero_rec = next(r for r in recs if r["id"] == "hero")
        body_rec = next(r for r in recs if r["id"] == "body")
        self.assertTrue(_Path(hero_rec["ref"]).is_file(), "hero ref path not found on disk")
        self.assertTrue(_Path(body_rec["ref"]).is_file(), "body ref path not found on disk")
        # Paths must point to DIFFERENT directories
        self.assertNotEqual(hero_rec["template_dir"], body_rec["template_dir"])

    def test_pool_walk_approved_status_included(self):
        """Entries with status 'approved' are included (not filtered out)."""
        # Patch the manifest to mark hero as approved
        manifest_path = self.srv.pool_dir / "manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["templates"][0]["status"] = "approved"
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        recs = CS._resolve_pool_templates(self.srv.hero_dir)
        ids = [r["id"] for r in recs]
        self.assertIn("hero", ids, "approved hero should be included in pool walk")
        self.assertIn("body", ids)

    def test_pool_walk_broken_status_excluded(self):
        """Entries with status 'broken' are excluded from pool walk."""
        manifest_path = self.srv.pool_dir / "manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["templates"][0]["status"] = "broken"
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        recs = CS._resolve_pool_templates(self.srv.hero_dir)
        ids = [r["id"] for r in recs]
        self.assertNotIn("hero", ids, "broken hero should NOT be in pool walk")
        self.assertIn("body", ids)

    # ── GET /pool-templates ───────────────────────────────────────────────────

    def test_pool_templates_returns_two_in_order(self):
        """GET /pool-templates returns ok:true + two templates in manifest order."""
        _, body = self.srv.get("/pool-templates")
        res = json.loads(body)
        self.assertTrue(res["ok"])
        tpls = res.get("templates", [])
        self.assertEqual(len(tpls), 2)
        self.assertEqual(tpls[0]["id"], "hero")
        self.assertEqual(tpls[1]["id"], "body")

    def test_pool_templates_exposes_status(self):
        """GET /pool-templates entries include a status field."""
        _, body = self.srv.get("/pool-templates")
        res = json.loads(body)
        for t in res["templates"]:
            self.assertIn("status", t)

    def test_pool_templates_exposes_approved_for_front_filter(self):
        """UX #5: /pool-templates must expose `approved` per template so the front
        (arrows + counter + Conference) can filter out already-approved templates."""
        _, body = self.srv.get("/pool-templates")
        res = json.loads(body)
        for t in res["templates"]:
            self.assertIn("approved", t)
        # baseline: nothing approved yet → both entries pending
        self.assertEqual([t for t in res["templates"] if t.get("approved")], [])

    def test_pool_templates_reflects_approved_on_fresh_state(self):
        """UX #5: once a template is approved (manifest marker set), a fresh
        StudioState surfaces approved:true via /pool-templates, so the client front
        filter (return !t.approved) drops it and the user only works the rest."""
        (self.srv.hero_dir / "slide-01.png").write_bytes(_tiny_png_bytes())
        self.srv.post("/approve", {"template_id": "hero", "tweaks": {}})
        # Build a fresh state so pool_templates re-reads the just-written manifest.
        state = CS.StudioState(self.srv.hero_dir, None, mode="template")
        httpd2 = ThreadingHTTPServer(("127.0.0.1", 0), CS.make_handler(state))
        port2 = httpd2.server_address[1]
        threading.Thread(target=httpd2.serve_forever, daemon=True).start()
        try:
            with urllib.request.urlopen(
                    f"http://127.0.0.1:{port2}/pool-templates", timeout=10) as r:
                res = json.loads(r.read().decode())
            by_id = {t["id"]: t for t in res["templates"]}
            self.assertTrue(by_id["hero"].get("approved"))
            self.assertFalse(by_id["body"].get("approved", False))
            pending = [t["id"] for t in res["templates"] if not t.get("approved")]
            self.assertEqual(pending, ["body"],
                             "only the unapproved template remains pending")
        finally:
            httpd2.shutdown()
            httpd2.server_close()

    # ── POST /compare-images ─────────────────────────────────────────────────

    def test_compare_images_happy_hero(self):
        """POST /compare-images {template_id:'hero'} returns non-empty data-URI for ref."""
        code, res = self.srv.post("/compare-images", {"template_id": "hero"})
        self.assertEqual(code, 200)
        self.assertTrue(res["ok"])
        self.assertIsNotNone(res.get("ref"), "ref data-URI should be present")
        self.assertTrue(
            res["ref"].startswith("data:image/png;base64,"),
            "ref should be a PNG data-URI")

    def test_compare_images_happy_body(self):
        """POST /compare-images {template_id:'body'} returns ref data-URI from body's dir."""
        code, res = self.srv.post("/compare-images", {"template_id": "body"})
        self.assertEqual(code, 200)
        self.assertTrue(res["ok"])
        self.assertIsNotNone(res.get("ref"))
        self.assertTrue(res["ref"].startswith("data:image/png;base64,"))

    def test_compare_images_missing_ref_returns_clear_error(self):
        """POST /compare-images when ref-canonical.png is missing returns a clear error, no hang."""
        import shutil as _sh
        _sh.rmtree(self.srv.hero_dir / "assets", ignore_errors=True)
        # Rebuild StudioState to refresh pool_templates (ref path now gone)
        state = CS.StudioState(self.srv.hero_dir, None, mode="template")
        httpd2 = ThreadingHTTPServer(("127.0.0.1", 0), CS.make_handler(state))
        port2 = httpd2.server_address[1]
        threading.Thread(target=httpd2.serve_forever, daemon=True).start()
        try:
            req = urllib.request.Request(
                f"http://127.0.0.1:{port2}/compare-images",
                data=json.dumps({"template_id": "hero"}).encode(),
                headers={"Content-Type": "application/json"}, method="POST")
            with urllib.request.urlopen(req, timeout=10) as r:
                res = json.loads(r.read().decode())
            # Must respond immediately (no hang) with a clear error mentioning hero
            self.assertTrue(res.get("ok") or "error" in res,
                            "should either succeed or give a clear error")
            if not res.get("ok"):
                self.assertIn("hero", res.get("error", ""),
                              "error should mention the template id")
            else:
                # ref is None when the file is absent (ok:true but ref=null)
                self.assertIsNone(res.get("ref"), "ref should be null when file is absent")
        finally:
            httpd2.shutdown()
            httpd2.server_close()

    def test_compare_images_unknown_template_id_returns_error(self):
        """POST /compare-images with an unknown template_id returns ok:false."""
        _, res = self.srv.post("/compare-images", {"template_id": "nonexistent"})
        self.assertFalse(res["ok"])
        self.assertIn("nonexistent", res.get("error", ""))

    # ── POST /approve (fixed id match, templates dict-normalization) ──────────

    def test_approve_hero_marks_approved_without_changing_status(self):
        """POST /approve {template_id:'hero'} adds an `approved` marker but KEEPS
        status='ready' so the template still counts toward the brand-context
        ready_count gate. Approving must NOT flip status to 'approved'."""
        (self.srv.hero_dir / "slide-01.png").write_bytes(_tiny_png_bytes())
        _, res = self.srv.post("/approve", {"template_id": "hero", "tweaks": {}})
        self.assertTrue(res["ok"])
        manifest = json.loads(
            (self.srv.pool_dir / "manifest.json").read_text(encoding="utf-8"))
        hero_entry = next(
            e for e in manifest["templates"] if e["id"] == "hero")
        body_entry = next(
            e for e in manifest["templates"] if e["id"] == "body")
        # status is UNCHANGED — approval is a separate marker
        self.assertEqual(hero_entry["status"], "ready")
        self.assertTrue(hero_entry.get("approved"),
                        "hero should carry an approved=True marker")
        self.assertIn("approved_at", hero_entry)
        # body entry must remain untouched — not approved, still ready
        self.assertEqual(body_entry["status"], "ready")
        self.assertFalse(body_entry.get("approved", False))

    def test_approve_manifest_updated_true(self):
        """POST /approve returns manifest_updated:true when manifest found and entry matched."""
        (self.srv.hero_dir / "slide-01.png").write_bytes(_tiny_png_bytes())
        _, res = self.srv.post("/approve", {"template_id": "hero", "tweaks": {}})
        self.assertTrue(res["ok"])
        self.assertTrue(res.get("manifest_updated"),
                        "manifest_updated should be True when manifest entry matched")

    def test_approving_whole_pool_keeps_ready_count_nonzero(self):
        """REGRESSION GATE: approving EVERY template in the pool must NOT zero the
        ready_count. The brand-context visual_state gate (SKILL.md:121,
        pipeline-phases.md:162) counts templates with status=='ready'; if /approve
        flipped status to 'approved', approving the whole pool would drop ready_count
        to 0 and block content generation. Approval is a separate marker, so every
        entry stays status=='ready'."""
        # Seed a baked slide for each template so /approve can resolve previews.
        (self.srv.hero_dir / "slide-01.png").write_bytes(_tiny_png_bytes())
        (self.srv.body_dir / "slide-01.png").write_bytes(_tiny_png_bytes())

        manifest_before = json.loads(
            (self.srv.pool_dir / "manifest.json").read_text(encoding="utf-8"))
        all_ids = [e["id"] for e in manifest_before["templates"]]
        self.assertGreaterEqual(len(all_ids), 2, "fixture needs >=2 templates")

        # Approve EVERY template in the pool.
        for tid in all_ids:
            _, res = self.srv.post("/approve", {"template_id": tid, "tweaks": {}})
            self.assertTrue(res["ok"], f"/approve failed for {tid}: {res}")

        manifest_after = json.loads(
            (self.srv.pool_dir / "manifest.json").read_text(encoding="utf-8"))
        ready_count = sum(
            1 for e in manifest_after["templates"] if e.get("status") == "ready")
        approved_count = sum(
            1 for e in manifest_after["templates"] if e.get("approved"))

        self.assertEqual(ready_count, len(all_ids),
                         "every template must stay status='ready' after approval")
        self.assertGreaterEqual(ready_count, 1,
                                "ready_count must never reach 0 — gate would block")
        self.assertEqual(approved_count, len(all_ids),
                         "every approved template must carry the approved marker")

    # ── Cross-template attribution (no silent corruption) ────────────────────

    def test_cross_template_attribution_body_tweaks_land_in_body_dir_only(self):
        """Approving body writes its tweaks under body's OWN dir, not hero's dir.

        This is the deterministic proof that per-template approve cannot corrupt
        a sibling template's tweaks file.

        Steps:
          1. Seed a baked slide-01.png in hero_dir (required by /approve).
          2. POST /approve {template_id:'body', tweaks:{<body-specific fontSize:77>}}.
          3. Read body_dir/tweaks.json — MUST contain fontSize 77.
          4. Read hero_dir/tweaks.json — MUST NOT contain 77 (file absent, or no 77).
        """
        # Seed a baked slide in hero_dir (server's state.run) AND body_dir so /approve
        # can find slide-01.png for the approved template.
        (self.srv.hero_dir / "slide-01.png").write_bytes(_tiny_png_bytes())
        (self.srv.body_dir / "slide-01.png").write_bytes(_tiny_png_bytes())

        body_tweaks = {"slide-01": {"zones": {"HEADLINE": {"fontSize": 77}}}}
        _, res = self.srv.post("/approve",
                               {"template_id": "body", "tweaks": body_tweaks})
        self.assertTrue(res["ok"], f"/approve failed: {res}")

        # Assertion A: body_dir/tweaks.json exists and contains fontSize 77
        body_tweaks_file = self.srv.body_dir / "tweaks.json"
        self.assertTrue(body_tweaks_file.is_file(),
                        "body/tweaks.json must exist after approving body")
        body_text = body_tweaks_file.read_text(encoding="utf-8")
        self.assertIn("77", body_text,
                      "body/tweaks.json must contain the body edit (fontSize:77)")
        body_data = json.loads(body_text)
        # The value 77 must appear somewhere in the serialized dict
        self.assertIn("77", json.dumps(body_data),
                      "body/tweaks.json must contain '77' as a JSON value")

        # Assertion B: hero_dir/tweaks.json either does NOT exist, or does NOT contain 77
        hero_tweaks_file = self.srv.hero_dir / "tweaks.json"
        if hero_tweaks_file.is_file():
            hero_text = hero_tweaks_file.read_text(encoding="utf-8")
            self.assertNotIn("77", hero_text,
                             "hero/tweaks.json must NOT contain body's edit (fontSize:77)")

    def test_cross_template_attribution_reverse_direction(self):
        """Approving hero does NOT write to body's dir."""
        (self.srv.hero_dir / "slide-01.png").write_bytes(_tiny_png_bytes())
        hero_tweaks = {"slide-01": {"zones": {"HEADLINE": {"fontSize": 99}}}}
        _, res = self.srv.post("/approve",
                               {"template_id": "hero", "tweaks": hero_tweaks})
        self.assertTrue(res["ok"])
        # body/tweaks.json must not contain 99
        body_tweaks_file = self.srv.body_dir / "tweaks.json"
        if body_tweaks_file.is_file():
            self.assertNotIn("99", body_tweaks_file.read_text(encoding="utf-8"))

    # ── Approved-is-renderable ────────────────────────────────────────────────

    def test_approved_template_still_renderable_with_ready_status(self):
        """After approving hero, resolve_pool_template must not raise: status stays
        'ready' (always renderable) and the approval is carried as a separate marker."""
        import render_template as RT  # noqa: PLC0415

        (self.srv.hero_dir / "slide-01.png").write_bytes(_tiny_png_bytes())
        self.srv.post("/approve", {"template_id": "hero", "tweaks": {}})

        # resolve_pool_template needs (pool_name, template_id, brand_context).
        # brand_context is the parent of templates/: self.srv.root
        brand_ctx = self.srv.root
        try:
            entry, html_path, _, _ = RT.resolve_pool_template(
                "test-pool", "hero", brand_context=brand_ctx)
            self.assertEqual(entry.get("status"), "ready",
                             "status must stay 'ready' after approval")
            self.assertTrue(entry.get("approved"),
                            "approval is carried as a separate marker")
        except SystemExit as exc:
            self.fail(f"resolve_pool_template raised SystemExit for approved template: {exc}")

    # ── B2 auto-load (_load_canonical_tweaks + _merge_tweaks) ────────────────

    def test_b2_autoload_canonical_sentinel_rekeys_to_slide(self):
        """_load_canonical_tweaks with __canonical__ sentinel re-keys to the target slide."""
        import render_template as RT  # noqa: PLC0415

        td = _tempfile.TemporaryDirectory()
        try:
            tdir = _Path(td.name)
            (tdir / "tweaks.json").write_text(
                json.dumps({"__canonical__": {"zones": {"HEADLINE": {"fontSize": 88}}}}),
                encoding="utf-8")

            class _FakeArgs:
                template_dir = str(tdir)
                template_pool = None
                template_id = None
                tweaks = None

            canonical = RT._load_canonical_tweaks(_FakeArgs(), "slide-01", "slide-01")
            self.assertIsNotNone(canonical)
            self.assertIn("slide-01", canonical)
            slide_data = canonical["slide-01"]
            self.assertEqual(
                slide_data["zones"]["HEADLINE"]["fontSize"], 88,
                "_load_canonical_tweaks must re-key __canonical__ to the target slide")
        finally:
            td.cleanup()

    def test_b2_merge_tweaks_canonical_no_run_override(self):
        """_merge_tweaks(canonical, None) returns the canonical slide data unchanged."""
        import render_template as RT  # noqa: PLC0415

        canonical = {"slide-01": {"zones": {"HEADLINE": {"fontSize": 88}}}}
        merged = RT._merge_tweaks(canonical, None)
        self.assertEqual(merged["slide-01"]["zones"]["HEADLINE"]["fontSize"], 88)

    def test_b2_merge_tweaks_run_wins_over_canonical(self):
        """_merge_tweaks: run-level --tweaks override wins key-by-key over canonical."""
        import render_template as RT  # noqa: PLC0415

        canonical = {"slide-01": {"zones": {"HEADLINE": {"fontSize": 88}}}}
        run_override = {"slide-01": {"zones": {"HEADLINE": {"fontSize": 120}}}}
        merged = RT._merge_tweaks(canonical, run_override)
        self.assertEqual(
            merged["slide-01"]["zones"]["HEADLINE"]["fontSize"], 120,
            "run-level --tweaks must win over canonical base")

    def test_b2_merge_tweaks_both_none_returns_none(self):
        """_merge_tweaks(None, None) returns None (preserves byte-identical behavior)."""
        import render_template as RT  # noqa: PLC0415

        self.assertIsNone(RT._merge_tweaks(None, None))


class TestP2Robustness(unittest.TestCase):
    """P2 robustness fixes — #12 lock, #13 pool-dir launch, #16 decompose fail-soft."""

    # ── #13: launching against the POOL dir opens the first template editable ──
    def test_pool_dir_launch_resolves_first_template(self):
        td = _tempfile.TemporaryDirectory()
        self.addCleanup(td.cleanup)
        pool = _make_template_pool(_Path(td.name))
        pool_dir = pool["pool_dir"]
        # state.run starts at the POOL dir (manifest.json, no root template.html).
        self.assertFalse((pool_dir / "template.html").is_file())
        state = CS.StudioState(pool_dir, None, mode="template")
        # It must retarget to the first ready template's dir (hero), not stay on pool.
        self.assertEqual(state.run.resolve(), pool["hero_dir"].resolve())
        self.assertTrue((state.run / "template.html").is_file())

    def test_template_dir_launch_unchanged(self):
        """Launching against a concrete template dir still targets that dir."""
        td = _tempfile.TemporaryDirectory()
        self.addCleanup(td.cleanup)
        pool = _make_template_pool(_Path(td.name))
        state = CS.StudioState(pool["body_dir"], None, mode="template")
        self.assertEqual(state.run.resolve(), pool["body_dir"].resolve())

    # ── #12: StudioState carries a lock; concurrent /apply + /select serialize ──
    def test_state_has_lock(self):
        td = _tempfile.TemporaryDirectory()
        self.addCleanup(td.cleanup)
        pool = _make_template_pool(_Path(td.name))
        state = CS.StudioState(pool["hero_dir"], None, mode="template")
        self.assertTrue(hasattr(state, "lock"))
        # Reentrant acquire would deadlock — confirm a plain (non-reentrant) lock.
        self.assertTrue(state.lock.acquire(blocking=False))
        state.lock.release()

    # ── #16: missing decompose.py fails soft (no import-time assert) ──
    def test_no_import_time_assert_on_missing_decompose(self):
        """Importing the module must not assert even if DECOMPOSE is missing."""
        # The module already imported cleanly at test-collection time; assert the
        # path object exists as an attribute but is NOT asserted to be a real file.
        self.assertTrue(hasattr(CS, "DECOMPOSE"))

    def test_decompose_failsoft_when_script_missing(self):
        import unittest.mock as _mock
        td = _tempfile.TemporaryDirectory()
        self.addCleanup(td.cleanup)
        run = _Path(td.name)
        # Full-AI slide layout (id dir + sibling PNG) so _find_slides_info resolves
        # 'slide-01' and the handler reaches the DECOMPOSE-missing fail-soft branch.
        (run / "slide-01").mkdir()
        (run / "slide-01.png").write_bytes(_real_png(1080, 1350))
        state = CS.StudioState(run, None, mode="post")
        httpd = ThreadingHTTPServer(("127.0.0.1", 0), CS.make_handler(state))
        port = httpd.server_address[1]
        threading.Thread(target=httpd.serve_forever, daemon=True).start()
        try:
            # Force DECOMPOSE to a non-existent path → /decompose must 200 ok:false.
            with _mock.patch.object(CS, "DECOMPOSE", _Path(td.name) / "nope.py"):
                req = urllib.request.Request(
                    f"http://127.0.0.1:{port}/decompose",
                    data=json.dumps({"slide_id": "slide-01"}).encode(),
                    headers={"Content-Type": "application/json"}, method="POST")
                res = json.loads(urllib.request.urlopen(req, timeout=5).read())
            self.assertFalse(res["ok"])
            self.assertIn("decompose.py", res["error"])
        finally:
            httpd.shutdown(); httpd.server_close()


class TestR5fContainerSlotFixes(unittest.TestCase):
    """r5f F1a/F1b/F5 — in-browser (Playwright) assertions mirroring the L5/run-02
    diagnostics: a container slot (callout pill carrying the handle while a styled
    child holds the type) must survive a text edit; text-ish props must land on the
    inner text node; fill controls seed from computed colour; imgSrc swaps the
    placeholder's image; duplicated handles get box tweaks applied ONCE."""

    PILL_TEMPLATE = """<!doctype html><html><head><meta charset='utf-8'>
<style>
.slide { width:1080px; height:1350px; position:relative; background:#fff; }
.bottom-pill { position:absolute; left:6%; bottom:6%; background:#5B57D6;
  border-radius:60px; padding:18px 28px; display:flex; align-items:center; gap:14px; }
.bottom-pill-text { font-family: Arial, sans-serif; font-size:2.5926cqw; color:#fff; }
.pill-arrow { width:34px; height:34px; border-radius:50%; background:#e2403a; color:#fff; }
.photo-zone { position:absolute; top:10%; left:10%; width:40%; height:30%; }
.photo-zone img { width:100%; height:100%; object-fit:cover; }
</style></head><body>
<div class="slide">
  <div class="photo-zone" data-slot="PHOTO_MAIN"><img src="photo.png" alt=""></div>
  <div class="bottom-pill" data-slot="CALLOUT_TEXT">
    <div class="bottom-pill-text">{{{CALLOUT_TEXT}}}</div>
    <div class="pill-arrow">&#8594;</div>
  </div>
</div>
</body></html>"""

    PILL_INSTRUCTIONS = """# Slide 01

## Slots

- **CALLOUT_TEXT** — bottom callout
  - bbox: 6% 86% 60% 8%
  - style: pill, brand-accent fill, white text, 2.6cqw
  - sample: "Save this for later"

- **PHOTO_MAIN** — photo
  - bbox: 10% 10% 40% 30%
  - style: image, cover
"""

    @classmethod
    def _make_pill_run(cls):
        import tempfile
        td = tempfile.TemporaryDirectory()
        sd = Path(td.name) / "slide-01"
        sd.mkdir()
        (sd / "template.html").write_text(cls.PILL_TEMPLATE, encoding="utf-8")
        (sd / "instructions.md").write_text(cls.PILL_INSTRUCTIONS, encoding="utf-8")
        return td

    def _open_editor(self, p):
        from preview_editor import build_editor_html
        self._td = self._make_pill_run()
        run = Path(self._td.name)
        out = run / "editor.html"
        out.write_text(build_editor_html(run), encoding="utf-8")
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1600, "height": 1000})
        page.goto(out.as_uri())
        page.wait_for_timeout(500)
        return browser, page

    _PROBE = """() => {
      var d = document.getElementById('frame-slide-01').contentDocument;
      var pill = d.querySelector('[data-slot="CALLOUT_TEXT"]');
      var txt = d.querySelector('.bottom-pill-text');
      var arrow = d.querySelector('.pill-arrow');
      var cs = txt ? d.defaultView.getComputedStyle(txt) : null;
      return { hasText: !!txt, hasArrow: !!arrow,
               fontFamily: cs ? cs.fontFamily : null,
               fontSize: cs ? cs.fontSize : null,
               pillText: pill ? pill.textContent.trim() : null };
    }"""

    @unittest.skipUnless(_playwright_ready(), "Playwright/Chromium not available")
    def test_f1a_container_text_edit_preserves_children_and_font(self):
        """The reproduced defect: one keystroke on a container slot used to wipe
        .bottom-pill-text + .pill-arrow (Inter 28px → Times New Roman 16px)."""
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            browser, page = self._open_editor(p)
            try:
                before = page.evaluate(self._PROBE)
                self.assertTrue(before["hasText"] and before["hasArrow"])
                page.evaluate(
                    "() => applyToSlide('slide-01','CALLOUT_TEXT','text','New copy.')")
                after = page.evaluate(self._PROBE)
                self.assertTrue(after["hasText"], "styled text child destroyed")
                self.assertTrue(after["hasArrow"], "pill arrow destroyed")
                self.assertEqual(after["fontFamily"], before["fontFamily"],
                                 "font fell back to browser default")
                self.assertEqual(after["fontSize"], before["fontSize"])
                self.assertIn("New copy.", after["pillText"])
            finally:
                browser.close()
                self._td.cleanup()

    @unittest.skipUnless(_playwright_ready(), "Playwright/Chromium not available")
    def test_f1c_fontsize_lands_on_inner_text_node(self):
        """fontSize must beat the inner node's own font-size declaration (the pill
        text declares its own cqw — a rule on the container would lose)."""
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            browser, page = self._open_editor(p)
            try:
                page.evaluate(
                    "() => applyToSlide('slide-01','CALLOUT_TEXT','fontSize',5)")
                res = page.evaluate(self._PROBE)
                # 5cqw of the rendered slide width — must differ from the class's
                # 2.5926cqw computed value; assert the inline style landed inner.
                inner_inline = page.evaluate(
                    "() => document.getElementById('frame-slide-01').contentDocument"
                    ".querySelector('.bottom-pill-text').style.fontSize")
                self.assertEqual(inner_inline, "5cqw")
                self.assertTrue(res["hasArrow"])
            finally:
                browser.close()
                self._td.cleanup()

    @unittest.skipUnless(_playwright_ready(), "Playwright/Chromium not available")
    def test_f1b_fill_controls_seed_from_computed_colour(self):
        """Selecting the pill must seed Fill with the REAL background (#5B57D6 from
        the stylesheet) and Text color with the inner text's colour (#fff) — not
        whatever hardcoded defaults the panel was generated with."""
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            browser, page = self._open_editor(p)
            try:
                page.evaluate("() => selectZone('slide-01','CALLOUT_TEXT')")
                vals = page.evaluate(
                    """() => {
                      var g = document.querySelector(
                        '.control-group[data-control-type="pill"][data-slot="CALLOUT_TEXT"]');
                      var bg = g.querySelector('input[type="color"][data-prop="bgColor"]');
                      var fg = g.querySelector('input[type="color"][data-prop="color"]');
                      return { bg: bg && bg.value, fg: fg && fg.value };
                    }""")
                self.assertEqual(vals["bg"].lower(), "#5b57d6")
                self.assertEqual(vals["fg"].lower(), "#ffffff")
            finally:
                browser.close()
                self._td.cleanup()

    @unittest.skipUnless(_playwright_ready(), "Playwright/Chromium not available")
    def test_f5_imgsrc_swaps_image_in_place(self):
        """Replace image: imgSrc swaps the inner <img src> while geometry and
        object-fit stay untouched."""
        from playwright.sync_api import sync_playwright
        red_px = ("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAA"
                  "fFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==")
        with sync_playwright() as p:
            browser, page = self._open_editor(p)
            try:
                res = page.evaluate(
                    """(uri) => {
                      var d = document.getElementById('frame-slide-01').contentDocument;
                      var zone = d.querySelector('[data-slot="PHOTO_MAIN"]');
                      var img = zone.querySelector('img');
                      var beforeRect = zone.getBoundingClientRect();
                      applyToSlide('slide-01','PHOTO_MAIN','imgSrc', uri);
                      var afterRect = zone.getBoundingClientRect();
                      return {
                        src: img.src,
                        fit: d.defaultView.getComputedStyle(img).objectFit,
                        sameW: beforeRect.width === afterRect.width,
                        sameH: beforeRect.height === afterRect.height,
                      };
                    }""", red_px)
                self.assertEqual(res["src"], red_px)
                self.assertEqual(res["fit"], "cover", "object-fit must be untouched")
                self.assertTrue(res["sameW"] and res["sameH"], "geometry changed")
                # and it persists through the tweaks export (the bake's input)
                tweaks = page.evaluate("() => window.__getTweaks()")
                self.assertEqual(
                    tweaks["slide-01"]["PHOTO_MAIN"]["imgSrc"], red_px)
            finally:
                browser.close()
                self._td.cleanup()

    @unittest.skipUnless(_playwright_ready(), "Playwright/Chromium not available")
    def test_tweaks_css_applies_once_on_duplicated_handles(self):
        """Bake side of F1a sibling b: with a legacy dup (same handle on container
        AND descendant), the translate rule must move ONE element (the outermost) —
        not both (2x offset in the bake vs 1x in the editor)."""
        import sys as _sys
        _sys.path.insert(0, str(Path(CS.RENDER_TEMPLATE).parent))
        from render_template import _build_tweaks_css as _btc
        from playwright.sync_api import sync_playwright
        css = _btc({"CALLOUT_TEXT": {"x": 10, "y": 0}})
        html = (
            "<!doctype html><html><head><style>" + css + "</style></head><body>"
            '<div class="slide" style="width:1080px;height:1350px;position:relative">'
            '<div data-slot="CALLOUT_TEXT" style="position:absolute;left:0;top:0">'
            '<div data-slot="CALLOUT_TEXT" class="inner">text</div>'
            "</div></div></body></html>"
        )
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": 1080, "height": 1350})
            page.set_content(html)
            res = page.evaluate(
                """() => {
                  var els = document.querySelectorAll('[data-slot="CALLOUT_TEXT"]');
                  var cs = getComputedStyle;
                  return { outer: cs(els[0]).translate, inner: cs(els[1]).translate };
                }""")
            browser.close()
        self.assertEqual(res["outer"], "108px", "outermost must carry the delta")
        self.assertIn(res["inner"], ("none", ""), "inner duplicate must NOT re-apply")

    @unittest.skipUnless(_playwright_ready(), "Playwright/Chromium not available")
    def test_parity_script_mirrors_editor_targeting_at_bake(self):
        """Bake side of F1a/F5: the parity script applies fontSize to the inner
        text node and swaps the slot's <img src> — same targeting as the editor."""
        import sys as _sys
        _sys.path.insert(0, str(Path(CS.RENDER_TEMPLATE).parent))
        from render_template import _build_parity_script as _bps
        from playwright.sync_api import sync_playwright
        red_px = ("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAA"
                  "fFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==")
        script = _bps({
            "CALLOUT_TEXT": {"fontSize": 5, "color": "#112233"},
            "PHOTO_MAIN": {"imgSrc": red_px},
        })
        self.assertTrue(script)
        html = (
            "<!doctype html><html><head></head><body>"
            '<div class="slide" style="width:1080px;height:1350px;position:relative;container-type:inline-size">'
            '<div data-slot="PHOTO_MAIN"><img src="x.png" style="object-fit:cover"></div>'
            '<div data-slot="CALLOUT_TEXT" class="bottom-pill">'
            '<div class="bottom-pill-text" style="font-size:28px">Save this</div>'
            '<div class="pill-arrow">&#8594;</div>'
            "</div></div>" + script + "</body></html>"
        )
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": 1080, "height": 1350})
            page.set_content(html)
            res = page.evaluate(
                """() => {
                  var txt = document.querySelector('.bottom-pill-text');
                  var img = document.querySelector('[data-slot="PHOTO_MAIN"] img');
                  return {
                    inlineFs: txt.style.fontSize,
                    color: getComputedStyle(txt).color,
                    arrow: !!document.querySelector('.pill-arrow'),
                    src: img.src,
                    fit: getComputedStyle(img).objectFit,
                  };
                }""")
            browser.close()
        self.assertEqual(res["inlineFs"], "5cqw")
        self.assertEqual(res["color"], "rgb(17, 34, 51)")
        self.assertTrue(res["arrow"])
        self.assertEqual(res["src"], red_px)
        self.assertEqual(res["fit"], "cover")


# ---------------------------------------------------------------------------
# studio-ai-edit — provider detection + POST /ai-edit (mocked subprocess:
# ZERO real API calls, ZERO network)
# ---------------------------------------------------------------------------

class _AiEditServer:
    """A studio server on a minimal run folder, with an optional run-local .env
    (the only .env the dev-tree walk-up considers — hermetic by construction)."""

    def __init__(self, env_text: str | None = None, run_td=None):
        self.td = run_td or _tempfile.TemporaryDirectory()
        self.run = _Path(self.td.name)
        if not (self.run / "slide-01").is_dir() and not list(self.run.glob("slide-*")):
            (self.run / "slide-01").mkdir()
            (self.run / "slide-01.png").write_bytes(_real_png(1080, 1350))
        if env_text is not None:
            (self.run / ".env").write_text(env_text, encoding="utf-8")
        self.state = CS.StudioState(self.run, None)
        self.httpd = ThreadingHTTPServer(("127.0.0.1", 0), CS.make_handler(self.state))
        self.port = self.httpd.server_address[1]
        threading.Thread(target=self.httpd.serve_forever, daemon=True).start()

    def get(self, path):
        with urllib.request.urlopen(
                f"http://127.0.0.1:{self.port}{path}", timeout=10) as r:
            return r.status, r.read().decode()

    def post_ai_edit(self, obj):
        """POST /ai-edit; returns (status, json) for 2xx AND 4xx responses."""
        req = urllib.request.Request(
            f"http://127.0.0.1:{self.port}/ai-edit",
            data=json.dumps(obj).encode(),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.status, json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            return e.code, json.loads(e.read().decode())

    def close(self):
        self.httpd.shutdown()
        self.httpd.server_close()
        self.td.cleanup()


def _ai_fake_gen(calls: list, *, returncode: int = 0, stderr: str = "",
                 write_output: bool = True, media_line: bool = True):
    """A subprocess.run stand-in for generate_image_*.py: records the call,
    optionally writes the --filename PNG and prints the MEDIA: token. No
    network, no API usage — the endpoint's subprocess contract is what's
    under test, never the providers."""
    def _run(cmd, **kwargs):
        argv = [str(c) for c in cmd]
        calls.append((argv, kwargs))
        out = _Path(argv[argv.index("--filename") + 1])
        stdout = ""
        if returncode == 0 and write_output:
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(_real_png(1024, 1536))
            stdout = f"Image saved: {out}\n"
            if media_line:
                stdout += f"MEDIA:{out}\n"

        class _P:  # minimal CompletedProcess stand-in
            pass

        p = _P()
        p.returncode = returncode
        p.stdout = stdout
        p.stderr = stderr
        return p
    return _run


class _AiEditEnvHermetic(unittest.TestCase):
    """Base: scrub the REAL provider keys from os.environ for the test's
    duration, so detection sees only what the test writes to the run .env."""

    def setUp(self):
        import unittest.mock as _mock
        self.mock = _mock
        envpatch = _mock.patch.dict(CS.os.environ)
        envpatch.start()
        self.addCleanup(envpatch.stop)
        CS.os.environ.pop("OPENAI_API_KEY", None)
        CS.os.environ.pop("GEMINI_API_KEY", None)

    def _srv(self, env_text=None, run_td=None) -> _AiEditServer:
        srv = _AiEditServer(env_text, run_td=run_td)
        self.addCleanup(srv.close)
        return srv


class TestAiEditProviderDetection(_AiEditEnvHermetic):
    """Presence-only detection matrix (spec DoD 3): só OPENAI · só GEMINI ·
    ambos · nenhum — plus the wiring into the served editor and /slide-info."""

    def test_detection_matrix(self):
        td = _tempfile.TemporaryDirectory()
        self.addCleanup(td.cleanup)
        run = _Path(td.name)
        cases = [
            (None, {"gpt": False, "gemini": False}),
            ("OPENAI_API_KEY=sk-test-1\n", {"gpt": True, "gemini": False}),
            ("GEMINI_API_KEY=g-test-1\n", {"gpt": False, "gemini": True}),
            ("OPENAI_API_KEY=sk-test-1\nGEMINI_API_KEY=g-test-1\n",
             {"gpt": True, "gemini": True}),
        ]
        for env_text, expected in cases:
            env = run / ".env"
            if env_text is None:
                if env.exists():
                    env.unlink()
            else:
                env.write_text(env_text, encoding="utf-8")
            self.assertEqual(CS._ai_edit_providers(run), expected,
                             f".env={env_text!r}")

    def test_exported_env_var_counts_as_present(self):
        # The scripts honor an exported var over .env, so detection must too.
        td = _tempfile.TemporaryDirectory()
        self.addCleanup(td.cleanup)
        CS.os.environ["GEMINI_API_KEY"] = "g-exported"
        provs = CS._ai_edit_providers(_Path(td.name))
        self.assertTrue(provs["gemini"])
        self.assertFalse(provs["gpt"])

    def test_served_editor_renders_only_available_provider(self):
        # Templated run (image slot) so the IMAGE control group exists; only the
        # GEMINI key present → only its button is in the served editor HTML.
        run_td = T._make_run_folder()
        srv = self._srv("GEMINI_API_KEY=g-test-1\n", run_td=run_td)
        _, html = srv.get("/")
        self.assertIn('data-provider="gemini"', html)
        self.assertNotIn('data-provider="gpt"', html)
        self.assertIn('id="ai-edit-modal"', html)

    def test_served_editor_no_keys_no_ai_markup(self):
        run_td = T._make_run_folder()
        srv = self._srv(None, run_td=run_td)
        _, html = srv.get("/")
        self.assertNotIn('class="ai-edit-btn"', html)
        self.assertNotIn('id="ai-edit-modal"', html)

    def test_slide_info_exposes_ai_edit_providers(self):
        srv = self._srv("OPENAI_API_KEY=sk-test-1\n")
        _, body = srv.get("/slide-info")
        data = json.loads(body)
        self.assertEqual(data["aiEditProviders"], {"gpt": True, "gemini": False})


class TestAiEditEndpoint(_AiEditEnvHermetic):
    """POST /ai-edit contract: validation → 4xx; key gating without fallback;
    mocked subprocess success/failure; audit files under _ai_edits/; key VALUES
    never in any response."""

    PNG_URI = ("data:image/png;base64,"
               + base64.b64encode(_real_png(1080, 1350)).decode("ascii"))

    def _body(self, **over):
        body = {"slide": "slide-01", "handle": "PHOTO", "provider": "gpt",
                "prompt": "make the background blue", "image": self.PNG_URI}
        body.update(over)
        return body

    # ── validation ────────────────────────────────────────────
    def test_unknown_provider_400(self):
        srv = self._srv("OPENAI_API_KEY=sk-test-1\n")
        code, res = srv.post_ai_edit(self._body(provider="dalle"))
        self.assertEqual(code, 400)
        self.assertFalse(res["ok"])

    def test_provider_unavailable_4xx(self):
        srv = self._srv(None)  # no .env, exported keys scrubbed
        code, res = srv.post_ai_edit(self._body())
        self.assertEqual(code, 403)
        self.assertFalse(res["ok"])
        # The key NAME tells the user what to configure (values never appear).
        self.assertIn("OPENAI_API_KEY", res["error"])

    def test_no_silent_fallback_to_other_provider(self):
        # GEMINI configured, GPT requested → 4xx. NEVER served by the other
        # provider (spec MUST 6: the user chose the button).
        srv = self._srv("GEMINI_API_KEY=g-test-1\n")
        code, res = srv.post_ai_edit(self._body(provider="gpt"))
        self.assertEqual(code, 403)
        self.assertFalse(res["ok"])

    def test_non_data_uri_payload_400(self):
        srv = self._srv("OPENAI_API_KEY=sk-test-1\n")
        for bad in ("C:/run/slide-01.png", "../../etc/passwd",
                    "http://127.0.0.1/x.png", "file:///etc/hosts",
                    "data:text/html;base64,PGI+aGk8L2I+", ""):
            code, res = srv.post_ai_edit(self._body(image=bad))
            self.assertEqual(code, 400, f"payload {bad!r} must be rejected")
            self.assertFalse(res["ok"])

    def test_svg_payload_400_human_message(self):
        # ai-edit-live-fixes Fix 2: an SVG/vector data URI is rejected (the server
        # accepts only raster png/jpg/webp/gif) — and the error speaks human
        # language, not dev-speak ("base64 data URI … paths and URLs"). The client
        # blocks this before submit; this is the second line of defense.
        srv = self._srv("OPENAI_API_KEY=sk-test-1\n")
        svg = ("data:image/svg+xml;base64,"
               + base64.b64encode(b"<svg xmlns='http://www.w3.org/2000/svg'/>")
               .decode("ascii"))
        code, res = srv.post_ai_edit(self._body(image=svg))
        self.assertEqual(code, 400)
        self.assertFalse(res["ok"])
        err = res["error"]
        # Human language, not dev-speak.
        self.assertNotIn("data URI", err)
        self.assertNotIn("paths and", err)
        # Names the accepted formats + the SVG/vector caveat in plain words.
        self.assertIn("PNG", err)
        self.assertIn("SVG", err)

    def test_blank_prompt_400(self):
        srv = self._srv("OPENAI_API_KEY=sk-test-1\n")
        code, res = srv.post_ai_edit(self._body(prompt="   "))
        self.assertEqual(code, 400)
        self.assertFalse(res["ok"])

    # ── mocked success ────────────────────────────────────────
    def test_mocked_success_returns_png_and_audit_file(self):
        srv = self._srv("OPENAI_API_KEY=sk-test-1\n")
        calls = []
        with self.mock.patch.object(CS.subprocess, "run",
                                    side_effect=_ai_fake_gen(calls)):
            code, res = srv.post_ai_edit(self._body())
        self.assertEqual(code, 200)
        self.assertTrue(res["ok"])
        self.assertTrue(res["png"].startswith("data:image/png;base64,"))
        # audit file written under run/_ai_edits/, never elsewhere
        outs = list((srv.run / "_ai_edits").glob("slide-01-PHOTO-gpt-*.png"))
        self.assertEqual(len(outs), 1)
        # subprocess contract (mirrors call_ai_image_gen / _rebake_slide)
        argv, kwargs = calls[0]
        self.assertTrue(any(a.endswith("generate_image_gpt.py") for a in argv))
        self.assertIn("--input-image", argv)
        self.assertIn("--size", argv)
        # 1080x1350 input → nearest GPT size is portrait 1024x1536
        self.assertEqual(argv[argv.index("--size") + 1], "1024x1536")
        self.assertIn("--quality", argv)
        self.assertEqual(argv[argv.index("--quality") + 1], "high")
        self.assertNotIn("--api-key", argv)  # script resolves the key itself
        self.assertEqual(kwargs.get("cwd"), str(srv.state.run))  # .env walk-up base
        self.assertEqual(kwargs.get("timeout"), 300)

    def test_mocked_success_gemini_uses_aspect_ratio(self):
        srv = self._srv("GEMINI_API_KEY=g-test-1\n")
        calls = []
        with self.mock.patch.object(CS.subprocess, "run",
                                    side_effect=_ai_fake_gen(calls)):
            code, res = srv.post_ai_edit(self._body(provider="gemini"))
        self.assertEqual(code, 200)
        self.assertTrue(res["ok"])
        argv, _ = calls[0]
        self.assertTrue(any(a.endswith("generate_image_gemini.py") for a in argv))
        self.assertIn("--aspect-ratio", argv)
        # 1080x1350 input → nearest Gemini ratio is 4:5
        self.assertEqual(argv[argv.index("--aspect-ratio") + 1], "4:5")
        self.assertNotIn("--size", argv)
        self.assertNotIn("--api-key", argv)
        outs = list((srv.run / "_ai_edits").glob("slide-01-PHOTO-gemini-*.png"))
        self.assertEqual(len(outs), 1)

    def test_generations_never_overwrite(self):
        srv = self._srv("OPENAI_API_KEY=sk-test-1\n")
        calls = []
        with self.mock.patch.object(CS.subprocess, "run",
                                    side_effect=_ai_fake_gen(calls)):
            srv.post_ai_edit(self._body())
            srv.post_ai_edit(self._body())
        names = sorted(p.name for p in (srv.run / "_ai_edits").glob("*.png"))
        self.assertEqual(names, ["slide-01-PHOTO-gpt-00.png",
                                 "slide-01-PHOTO-gpt-01.png"])

    def test_handle_and_slide_sanitized_in_audit_name(self):
        srv = self._srv("OPENAI_API_KEY=sk-test-1\n")
        calls = []
        with self.mock.patch.object(CS.subprocess, "run",
                                    side_effect=_ai_fake_gen(calls)):
            code, res = srv.post_ai_edit(
                self._body(slide="../evil", handle="PHOTO MAIN/.."))
        self.assertEqual(code, 200)
        self.assertTrue(res["ok"])
        outs = list((srv.run / "_ai_edits").glob("*.png"))
        self.assertEqual(len(outs), 1)
        # reduced to a filename-safe token — no separator survives
        self.assertNotIn("/", outs[0].name)
        self.assertNotIn("..", outs[0].name)
        self.assertEqual(outs[0].parent, srv.run / "_ai_edits")

    # ── mocked failure ────────────────────────────────────────
    def test_mocked_failure_clean_error_no_traceback(self):
        secret = "sk-test-SUPER-SECRET-VALUE-42"
        srv = self._srv(f"OPENAI_API_KEY={secret}\n")
        stderr = (
            "Traceback (most recent call last):\n"
            '  File "generate_image_gpt.py", line 192, in main\n'
            "    result = client.images.edit(\n"
            "openai.RateLimitError: Error code: 429 - billing hard limit reached\n"
        )
        calls = []
        with self.mock.patch.object(
                CS.subprocess, "run",
                side_effect=_ai_fake_gen(calls, returncode=1, stderr=stderr)):
            code, res = srv.post_ai_edit(self._body())
        # Fail-soft contract (decompose//post parity): HTTP 200, ok:false.
        self.assertEqual(code, 200)
        self.assertFalse(res["ok"])
        self.assertNotIn("Traceback", res["error"])
        self.assertNotIn('File "', res["error"])
        self.assertIn("billing", res["error"].lower())
        # the key VALUE appears NOWHERE in the response
        self.assertNotIn(secret, json.dumps(res))

    def test_key_value_scrubbed_even_when_echoed_by_provider(self):
        secret = "sk-test-LEAKED-VALUE-99"
        srv = self._srv(f"OPENAI_API_KEY={secret}\n")
        calls = []
        with self.mock.patch.object(
                CS.subprocess, "run",
                side_effect=_ai_fake_gen(calls, returncode=1,
                                         stderr=f"error: key {secret} was rejected")):
            code, res = srv.post_ai_edit(self._body())
        self.assertEqual(code, 200)
        self.assertFalse(res["ok"])
        self.assertNotIn(secret, json.dumps(res))

    def test_timeout_clean_error(self):
        srv = self._srv("OPENAI_API_KEY=sk-test-1\n")

        def _raise(cmd, **kwargs):
            raise CS.subprocess.TimeoutExpired(cmd, 300)

        with self.mock.patch.object(CS.subprocess, "run", side_effect=_raise):
            code, res = srv.post_ai_edit(self._body())
        self.assertEqual(code, 200)
        self.assertFalse(res["ok"])
        self.assertIn("timed out", res["error"])

    def test_missing_script_fails_soft(self):
        srv = self._srv("OPENAI_API_KEY=sk-test-1\n")
        with self.mock.patch.object(CS, "GEN_IMAGE_GPT",
                                    srv.run / "nope" / "generate_image_gpt.py"):
            code, res = srv.post_ai_edit(self._body())
        self.assertEqual(code, 200)
        self.assertFalse(res["ok"])
        self.assertIn("generate_image_gpt.py", res["error"])


def _ai_fake_gen_writing(calls: list, png_bytes: bytes):
    """Like ``_ai_fake_gen`` but writes a CALLER-SUPPLIED PNG as the generated
    output (so a test controls the output aspect / pixels / transparency under
    test). Records the call; prints the MEDIA: token. No network."""
    def _run(cmd, **kwargs):
        argv = [str(c) for c in cmd]
        calls.append((argv, kwargs))
        out = _Path(argv[argv.index("--filename") + 1])
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(png_bytes)

        class _P:
            pass

        p = _P()
        p.returncode = 0
        p.stdout = f"Image saved: {out}\nMEDIA:{out}\n"
        p.stderr = ""
        return p
    return _run


def _pil_from_data_uri(uri: str):
    """Decode a ``data:image/png;base64,...`` URI into a Pillow Image."""
    import base64 as _b64
    import io as _io
    from PIL import Image
    raw = _b64.b64decode(uri.split(",", 1)[1])
    return Image.open(_io.BytesIO(raw))


def _transparent_png(width: int, height: int) -> bytes:
    """A byte-valid RGBA PNG with a real (non-opaque) alpha channel: an opaque
    centre square on a fully transparent field. Lets a test assert the crop
    preserves transparency (the transparent-routing path)."""
    from PIL import Image
    import io as _io
    im = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    cw, ch = max(1, width // 2), max(1, height // 2)
    cx, cy = (width - cw) // 2, (height - ch) // 2
    for y in range(cy, cy + ch):
        for x in range(cx, cx + cw):
            im.putpixel((x, y), (200, 50, 50, 255))
    buf = _io.BytesIO()
    im.save(buf, format="PNG")
    return buf.getvalue()


@unittest.skipUnless(_pil_ready(), "Pillow required for the center-crop")
class TestAiEditFitResult(_AiEditEnvHermetic):
    """ai-edit-fit-result: the /ai-edit result is center-cropped (cover, no
    distortion) to the aspect of input image [0] before it is returned. No-op
    when aspects already match (bytes preserved); alpha survives the crop."""

    # Input slot image [0] is 1080x1350 (4:5). The mocked generator emits a
    # DIFFERENT aspect → the returned image must come back at 4:5.
    PNG_URI = ("data:image/png;base64,"
               + base64.b64encode(_real_png(1080, 1350)).decode("ascii"))

    def _body(self, **over):
        body = {"slide": "slide-01", "handle": "PHOTO", "provider": "gpt",
                "prompt": "make the background blue", "image": self.PNG_URI}
        body.update(over)
        return body

    @staticmethod
    def _ar(im) -> float:
        return im.size[0] / im.size[1]

    def test_output_cropped_to_input_aspect(self):
        # Generator returns 1024x1536 (2:3 ≈ 0.667); input [0] is 4:5 (0.8).
        # After the fix the returned image must be 4:5 (within tolerance) — and
        # cropped, not stretched (full width kept, height trimmed).
        srv = self._srv("OPENAI_API_KEY=sk-test-1\n")
        gen = _varied_png(1024, 1536)
        calls = []
        with self.mock.patch.object(
                CS.subprocess, "run",
                side_effect=_ai_fake_gen_writing(calls, gen)):
            code, res = srv.post_ai_edit(self._body())
        self.assertEqual(code, 200)
        self.assertTrue(res["ok"])
        im = _pil_from_data_uri(res["png"])
        self.assertAlmostEqual(self._ar(im), 1080 / 1350, delta=0.01)
        # cover/center-crop: too-tall source → full width kept, height trimmed.
        self.assertEqual(im.size[0], 1024)
        self.assertEqual(im.size[1], round(1024 / (1080 / 1350)))  # 1280

    def test_central_pixels_preserved(self):
        # The centre of the cropped image must equal the centre of the source —
        # a center-crop keeps the middle (zone of interest), trims only edges.
        srv = self._srv("OPENAI_API_KEY=sk-test-1\n")
        gen = _varied_png(1024, 1536)
        calls = []
        with self.mock.patch.object(
                CS.subprocess, "run",
                side_effect=_ai_fake_gen_writing(calls, gen)):
            code, res = srv.post_ai_edit(self._body())
        self.assertTrue(res["ok"])
        import io as _io
        from PIL import Image
        src = Image.open(_io.BytesIO(gen)).convert("RGBA")
        out = _pil_from_data_uri(res["png"]).convert("RGBA")
        sx, sy = src.size[0] // 2, src.size[1] // 2
        ox, oy = out.size[0] // 2, out.size[1] // 2
        self.assertEqual(src.getpixel((sx, sy)), out.getpixel((ox, oy)))

    def test_matching_aspect_is_noop_bytes_preserved(self):
        # Generator already emits 4:5 (864x1080) → no reencode: the returned
        # bytes are byte-for-byte the generated file (the on-disk audit PNG).
        srv = self._srv("OPENAI_API_KEY=sk-test-1\n")
        gen = _varied_png(864, 1080)  # 4:5, same aspect as the 1080x1350 input
        calls = []
        with self.mock.patch.object(
                CS.subprocess, "run",
                side_effect=_ai_fake_gen_writing(calls, gen)):
            code, res = srv.post_ai_edit(self._body())
        self.assertTrue(res["ok"])
        out_file = next((srv.run / "_ai_edits").glob("*.png"))
        # No reencode → returned URI == raw audit file bytes == the generated bytes.
        self.assertEqual(out_file.read_bytes(), gen)
        returned = base64.b64decode(res["png"].split(",", 1)[1])
        self.assertEqual(returned, gen)

    def test_transparent_output_keeps_alpha(self):
        # Transparent-routing path: a transparent PNG (2:3) must come back 4:5
        # AND still carry a real alpha channel (transparent corners preserved).
        srv = self._srv("OPENAI_API_KEY=sk-test-1\n")
        gen = _transparent_png(1024, 1536)
        calls = []
        with self.mock.patch.object(
                CS.subprocess, "run",
                side_effect=_ai_fake_gen_writing(calls, gen)):
            code, res = srv.post_ai_edit(self._body())
        self.assertTrue(res["ok"])
        im = _pil_from_data_uri(res["png"])
        self.assertEqual(im.mode, "RGBA")
        self.assertAlmostEqual(self._ar(im), 1080 / 1350, delta=0.01)
        # A corner is still fully transparent (alpha survived the crop).
        self.assertEqual(im.getpixel((0, 0))[3], 0)

    def test_gemini_provider_also_cropped(self):
        # The crop is provider-agnostic (MUST 5): same fit for the Gemini path.
        srv = self._srv("GEMINI_API_KEY=g-test-1\n")
        gen = _varied_png(1536, 1024)  # 3:2 landscape, input is 4:5 portrait
        calls = []
        with self.mock.patch.object(
                CS.subprocess, "run",
                side_effect=_ai_fake_gen_writing(calls, gen)):
            code, res = srv.post_ai_edit(self._body(provider="gemini"))
        self.assertTrue(res["ok"])
        im = _pil_from_data_uri(res["png"])
        self.assertAlmostEqual(self._ar(im), 1080 / 1350, delta=0.01)
        # too-wide source → full height kept, width trimmed.
        self.assertEqual(im.size[1], 1024)


class TestAiEditMultiInput(_AiEditEnvHermetic):
    """POST /ai-edit with a list of images (ai-edit-multi-input MUST 2/4/5):
    [0] is the slot image, extras follow in order; per-provider caps; aspect
    and transparency follow [0]; singular `image` stays retro-compatible."""

    PNG_URI = ("data:image/png;base64,"
               + base64.b64encode(_real_png(1080, 1350)).decode("ascii"))
    SQUARE_URI = ("data:image/png;base64,"
                  + base64.b64encode(_real_png(512, 512)).decode("ascii"))

    def _body(self, **over):
        body = {"slide": "slide-01", "handle": "PHOTO", "provider": "gpt",
                "prompt": "combine these"}
        body.update(over)
        return body

    def test_images_list_passes_all_input_images_in_order(self):
        srv = self._srv("OPENAI_API_KEY=sk-test-1\n")
        calls = []
        with self.mock.patch.object(CS.subprocess, "run",
                                    side_effect=_ai_fake_gen(calls)):
            code, res = srv.post_ai_edit(
                self._body(images=[self.PNG_URI, self.SQUARE_URI, self.SQUARE_URI]))
        self.assertEqual(code, 200)
        self.assertTrue(res["ok"])
        argv, _ = calls[0]
        # three --input-image flags, one per supplied image
        self.assertEqual(argv.count("--input-image"), 3)

    def test_singular_image_still_accepted(self):
        # Retrocompat: the old singular `image` field maps to a one-image list.
        srv = self._srv("OPENAI_API_KEY=sk-test-1\n")
        calls = []
        with self.mock.patch.object(CS.subprocess, "run",
                                    side_effect=_ai_fake_gen(calls)):
            code, res = srv.post_ai_edit(self._body(image=self.PNG_URI))
        self.assertEqual(code, 200)
        self.assertTrue(res["ok"])
        argv, _ = calls[0]
        self.assertEqual(argv.count("--input-image"), 1)

    def test_aspect_follows_slot_image_zero(self):
        # [0] is portrait 1080x1350, an extra is square — the GPT size picks 4:5
        # off [0], unaffected by the square reference.
        srv = self._srv("OPENAI_API_KEY=sk-test-1\n")
        calls = []
        with self.mock.patch.object(CS.subprocess, "run",
                                    side_effect=_ai_fake_gen(calls)):
            srv.post_ai_edit(
                self._body(images=[self.PNG_URI, self.SQUARE_URI]))
        argv, _ = calls[0]
        self.assertEqual(argv[argv.index("--size") + 1], "1024x1536")

    def test_over_cap_gpt_clean_400(self):
        srv = self._srv("OPENAI_API_KEY=sk-test-1\n")
        code, res = srv.post_ai_edit(
            self._body(images=[self.SQUARE_URI] * 17))
        self.assertEqual(code, 400)
        self.assertFalse(res["ok"])
        self.assertIn("16", res["error"])

    def test_over_cap_gemini_clean_400(self):
        srv = self._srv("GEMINI_API_KEY=g-test-1\n")
        code, res = srv.post_ai_edit(
            self._body(provider="gemini", images=[self.SQUARE_URI] * 15))
        self.assertEqual(code, 400)
        self.assertFalse(res["ok"])
        self.assertIn("14", res["error"])

    def test_at_cap_gpt_ok(self):
        # Exactly 16 is allowed for GPT (boundary).
        srv = self._srv("OPENAI_API_KEY=sk-test-1\n")
        calls = []
        with self.mock.patch.object(CS.subprocess, "run",
                                    side_effect=_ai_fake_gen(calls)):
            code, res = srv.post_ai_edit(
                self._body(images=[self.SQUARE_URI] * 16))
        self.assertEqual(code, 200)
        self.assertTrue(res["ok"])
        argv, _ = calls[0]
        self.assertEqual(argv.count("--input-image"), 16)

    def test_empty_images_list_400(self):
        srv = self._srv("OPENAI_API_KEY=sk-test-1\n")
        code, res = srv.post_ai_edit(self._body(images=[]))
        self.assertEqual(code, 400)
        self.assertFalse(res["ok"])

    def test_one_bad_uri_in_list_rejects_400(self):
        srv = self._srv("OPENAI_API_KEY=sk-test-1\n")
        code, res = srv.post_ai_edit(
            self._body(images=[self.PNG_URI, "../../etc/passwd"]))
        self.assertEqual(code, 400)
        self.assertFalse(res["ok"])


class TestAiEditHelpers(_AiEditEnvHermetic):
    """Pure-helper coverage: aspect nearest-pick + input-dimension sniffing."""

    def test_nearest_gpt_size(self):
        self.assertEqual(CS._nearest_gpt_size((1080, 1350)), "1024x1536")
        self.assertEqual(CS._nearest_gpt_size((1920, 1080)), "1536x1024")
        self.assertEqual(CS._nearest_gpt_size((800, 800)), "1024x1024")
        self.assertEqual(CS._nearest_gpt_size(None), "1024x1024")

    def test_nearest_gemini_aspect(self):
        self.assertEqual(CS._nearest_gemini_aspect((1080, 1350)), "4:5")
        self.assertEqual(CS._nearest_gemini_aspect((1920, 1080)), "16:9")
        self.assertEqual(CS._nearest_gemini_aspect((500, 1000)), "9:16")
        self.assertEqual(CS._nearest_gemini_aspect(None), "1:1")

    def test_image_dimensions_png_and_jpeg(self):
        td = _tempfile.TemporaryDirectory()
        self.addCleanup(td.cleanup)
        png = _Path(td.name) / "x.png"
        png.write_bytes(_real_png(640, 480))
        self.assertEqual(CS._image_dimensions(png), (640, 480))
        # minimal JPEG: SOI + SOF0 segment carrying 1080x1350
        jpg = _Path(td.name) / "x.jpg"
        jpg.write_bytes(
            b"\xff\xd8\xff\xc0" + (11).to_bytes(2, "big") + b"\x08"
            + (1350).to_bytes(2, "big") + (1080).to_bytes(2, "big")
            + b"\x03\x01\x11\x00"
        )
        self.assertEqual(CS._image_dimensions(jpg), (1080, 1350))
        # unknown format → None (caller degrades to square output)
        other = _Path(td.name) / "x.bin"
        other.write_bytes(b"RIFFxxxxWEBPVP8 ")
        self.assertIsNone(CS._image_dimensions(other))


class TestResolveHeroImage(unittest.TestCase):
    """_resolve_hero_image (Magic Layer source) resolves the hero robustly across
    template naming: canonical photo_main.png, the single _ai_bg/*.png, or root bg.png."""

    def test_canonical_photo_main(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            d = _Path(d)
            (d / "_ai_bg").mkdir()
            (d / "_ai_bg" / "photo_main.png").write_bytes(b"x")
            self.assertEqual(
                CS._resolve_hero_image({"template_dir": d}).name, "photo_main.png")

    def test_single_ai_bg_bg_png(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            d = _Path(d)
            (d / "_ai_bg").mkdir()
            (d / "_ai_bg" / "bg.png").write_bytes(b"x")
            self.assertEqual(
                CS._resolve_hero_image({"template_dir": d}).name, "bg.png")

    def test_root_bg_fallback(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            d = _Path(d)
            (d / "bg.png").write_bytes(b"x")
            self.assertEqual(
                CS._resolve_hero_image({"template_dir": d}).name, "bg.png")

    def test_genuinely_missing_returns_none(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            self.assertIsNone(CS._resolve_hero_image({"template_dir": _Path(d)}))


if __name__ == "__main__":
    unittest.main(verbosity=2)
