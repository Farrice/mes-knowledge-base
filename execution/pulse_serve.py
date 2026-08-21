#!/usr/bin/env python3
"""pulse_serve.py — live server for every Readout OS board (2026-08-06;
always-on + repo routes 2026-08-07). Stdlib only, 127.0.0.1 only.

GET  /            Pulse board          — regenerated on every hit
GET  /room        Briefing Room
GET  /missions    Mission Control
GET  /oracle      Oracle
GET  /repo/<repo-relative-path>
                  Any file inside the repo, ROOT-jailed. This is what makes the
                  boards actually navigable: brief pages, thumbnails, md mirrors
                  and context packs are all written as absolute file:// URIs
                  (render_brief._file_href), and a browser refuses to load a
                  file: URL from an http: page. Served over this route they
                  resolve, so a brief opened from a board behaves like a page
                  instead of a dead link.
GET  /ping        {"pulse": true, "<surface>_mtime": ...} — liveness probe AND
                  the mtime source every board polls for side-window reload
POST /action      {"action": "...", "args": {...}} → dispatch → regen → {"ok"}

Anything unmatched is a 404. It used to fall through to the Pulse board, so a
mistyped or unrouted URL answered 200 with the wrong page — which reads as
"the link worked and the page is wrong" instead of "there is no such route".

Usage:
    python3 execution/pulse_serve.py [--port 8765] [--idle 7200] [--open]
    --idle 0   never exit (the always-on launchd daemon uses this)

If the port is already serving a healthy pulse (GET /ping ok), --open just
opens the existing server instead of starting a second one.
"""
import argparse
import json
import mimetypes
import os
import subprocess
import sys
import threading
import time
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOARD = os.path.join(ROOT, ".agent", "pulse", "pulse-board.html")
ROOM = os.path.join(ROOT, "deliverables", "research-briefs", "index.html")
ORACLE = os.path.join(ROOT, ".agent", "oracle", "oracle-dashboard.html")
MISSIONS = os.path.join(ROOT, ".agent", "missions", "mission-control.html")
HOMEBASE = os.path.join(ROOT, ".agent", "homebase", "homebase.html")
ASSETS = os.path.join(ROOT, ".agent", "assets", "assets-board.html")
LIBRARY = os.path.join(ROOT, ".agent", "catalog", "library.html")
BRAIN = os.path.join(ROOT, ".agent", "brain", "brain.html")
INTEL = os.path.join(ROOT, "_active", "farrice-brand", "intelligence", "index.html")
PY = sys.executable or "python3"

LAST_HIT = time.time()

# Root serves the Homebase hub (2026-08-20); the Pulse console lives at /pulse.
HOME_PATHS = {"", "/", "/index.html", "/home", "/homebase"}

# ROOT-jailing keeps /repo/ inside the repo — but the repo itself holds secrets
# (.env carries NOTION_API_KEY) and history (.git). "Inside the repo" is not the
# same as "safe to hand to a browser page", so hidden directories are denied by
# default. .agent is the one exception: the boards live there and briefs link
# into .agent/handoffs/, so denying it would break the thing this route exists
# for. Deny-by-default on dotfiles, allow one known-safe tree.
REPO_ALLOWED_DOTDIRS = {".agent"}
REPO_DENIED_SUFFIXES = (".pem", ".key", ".p12", ".pfx", ".keystore")
REPO_DENIED_NAMES = {".env", ".netrc", ".htpasswd", "id_rsa", "id_ed25519", "credentials"}


def _repo_path_allowed(rel):
    """True if this repo-relative path may be served. Denies dotfiles/dirs
    (except .agent), credential-shaped names, and key material anywhere."""
    parts = [p for p in rel.replace("\\", "/").split("/") if p and p != "."]
    if not parts:
        return False
    for i, part in enumerate(parts):
        low = part.lower()
        if low in REPO_DENIED_NAMES or low.startswith(".env"):
            return False
        if part.startswith(".") and not (i == 0 and part in REPO_ALLOWED_DOTDIRS):
            return False
    return not parts[-1].lower().endswith(REPO_DENIED_SUFFIXES)


def regen(which="pulse"):
    script = {"pulse": "pulse_dashboard.py", "room": "brief_library.py",
              "oracle": "oracle_dashboard.py", "homebase": "homebase_board.py",
              "assets": "asset_gallery.py", "library": "catalog_board.py",
              "missions": "mission_board.py", "brain": "brain_graph.py",
              "intelligence": "intelligence_layer.py"}.get(
                  which, "pulse_dashboard.py")
    # brain rebuilds only when its source fingerprint changed — O(1) when fresh
    extra = ["--if-stale"] if which == "brain" else []
    try:
        subprocess.run([PY, os.path.join(ROOT, "execution", script)] + extra,
                       capture_output=True, text=True, timeout=90)
    except Exception as e:
        print(f"[pulse_serve] WARN regen failed: {e}", file=sys.stderr)


def _mtime(p):
    try:
        return os.stat(p).st_mtime
    except OSError:
        return 0


ACTIONS = {"done", "park", "reopen", "outcome", "outcome-dismiss", "outcome-snooze",
           "thread-archive", "open-path", "brief-archive", "brief-unarchive",
           "oracle-closes", "oracle-gate", "oracle-note", "refresh", "kill",
           "run_skill"}


def _run_skill(args):
    """Spawn one guarded headless deck run, detached (same pattern as
    _refresh_async — a claude run takes minutes; the POST must not block).
    Validation happens twice: here for an immediate UI error, and again inside
    skill_deck_runner.py which re-reads the curated deck file server-side —
    the POST payload is treated as untrusted indices, never as text."""
    card_id = str(args.get("card_id") or "")
    model = str(args.get("model") or "")
    effort = str(args.get("effort") or "")
    try:
        import skill_deck_runner as sdr
        card, err = sdr.validate(card_id, model, effort)
        if err:
            return {"ok": False, "error": err}
        lock = subprocess.run([PY, os.path.join(ROOT, "execution", "session_lock.py"),
                               "check"], capture_output=True, text=True, timeout=10)
        if lock.returncode != 0:
            return {"ok": False, "error": "session lock held — another run is live"}
        subprocess.Popen([PY, os.path.join(ROOT, "execution", "skill_deck_runner.py"),
                          "run", card_id, "--model", model, "--effort", effort],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                         start_new_session=True)
        return {"ok": True}
    except Exception as e:
        return {"ok": False, "error": str(e)[:200]}


def _refresh_async():
    """Kick the honest CLI (pulse_actions.py refresh) as a detached process.
    A sweep over 240 sessions takes real seconds; blocking the POST would make
    the button feel broken — the exact defect this hub exists to end. The CLI
    regenerates the homebase last, so /ping's mtime flips and the open page
    reloads itself when the data is actually fresh."""
    try:
        subprocess.Popen([PY, os.path.join(ROOT, "execution", "pulse_actions.py"), "refresh"],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                         start_new_session=True)
        return True
    except Exception as e:
        print(f"[pulse_serve] refresh spawn failed: {e}", file=sys.stderr)
        return False


def _brief_lifecycle(action, slug):
    verb = "archive" if action == "brief-archive" else "unarchive"
    r = subprocess.run([PY, os.path.join(ROOT, "execution", "brief_library.py"), verb, str(slug)],
                       capture_output=True, text=True, timeout=60)
    out = (r.stdout or "").strip() or (r.stderr or "").strip()
    print(out[-200:] if out else f"{verb}: {slug}")
    return r.returncode == 0


def _open_path(uri):
    """Open a repo-internal file with the OS opener. http pages cannot navigate
    to file:// URLs, so live-mode link clicks route here instead. ROOT-jailed."""
    import urllib.parse
    p = str(uri or "")
    if p.startswith("file://"):
        p = urllib.parse.unquote(p[len("file://"):])
    real = os.path.realpath(p)
    if not real.startswith(os.path.realpath(ROOT) + os.sep):
        print(f"[pulse_serve] refused open outside repo: {real}", file=sys.stderr)
        return False
    subprocess.run(["open", real], check=False)
    return True


def dispatch(action, args):
    if action == "open-path":
        return _open_path(args.get("uri", ""))
    if action == "refresh":
        return _refresh_async()
    if action == "run_skill":
        return _run_skill(args)
    if action in ("brief-archive", "brief-unarchive"):
        return _brief_lifecycle(action, args.get("slug", ""))
    sys.path.insert(0, os.path.join(ROOT, "execution"))
    import pulse_actions as pa
    if action == "done":
        return pa.act_done(args.get("slug", ""), args.get("outcome", ""))
    if action == "park":
        return pa.act_park(args.get("slug", ""), args.get("reason", ""))
    if action == "reopen":
        return pa.act_reopen(args.get("slug", ""))
    if action == "kill":
        return pa.act_kill(args.get("slug", ""), args.get("reason", ""))
    if action == "outcome":
        return pa.act_outcome(args.get("deliverable", ""), args.get("revenue", 0), args.get("outcome", ""))
    if action == "outcome-dismiss":
        return pa.act_outcome_dismiss(args.get("deliverable", ""))
    if action == "outcome-snooze":
        return pa.act_outcome_snooze(args.get("deliverable", ""))
    if action == "thread-archive":
        return pa.act_thread_archive(args.get("thread", ""))
    if action == "oracle-closes":
        return pa.act_oracle_closes()
    if action == "oracle-gate":
        return pa.act_oracle_gate()
    if action == "oracle-note":
        return pa.act_oracle_note(args.get("text", ""))
    return False


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *a):  # quiet
        pass

    def _touch(self):
        global LAST_HIT
        LAST_HIT = time.time()

    def _send(self, code, body, ctype="text/html; charset=utf-8"):
        data = body.encode("utf-8") if isinstance(body, str) else body
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(data)

    def _serve_repo(self, path):
        """Serve one file from inside the repo. ROOT-jailed, read-only, GET-only.

        The jail is the same realpath-prefix check _open_path() uses. It must
        stay that way: this route is the one place the server hands file bytes
        to a page, so a traversal here would expose anything the user can read.
        `..` is normalised away by realpath BEFORE the prefix test, so the test
        sees the true destination rather than the requested spelling.
        """
        rel = urllib.parse.unquote(path[len("/repo/"):]).split("?", 1)[0].split("#", 1)[0]
        if not rel:
            self._send(404, "not found", "text/plain; charset=utf-8")
            return
        if not _repo_path_allowed(rel):
            print(f"[pulse_serve] refused sensitive path: {rel}", file=sys.stderr)
            self._send(403, "not served", "text/plain; charset=utf-8")
            return
        real = os.path.realpath(os.path.join(ROOT, rel))
        if not real.startswith(os.path.realpath(ROOT) + os.sep):
            print(f"[pulse_serve] refused repo read outside root: {real}", file=sys.stderr)
            self._send(403, "outside repo", "text/plain; charset=utf-8")
            return
        if not os.path.isfile(real):
            self._send(404, f"no such file: {rel}", "text/plain; charset=utf-8")
            return
        ctype = mimetypes.guess_type(real)[0] or "application/octet-stream"
        if ctype.startswith("text/") or ctype in ("application/json", "image/svg+xml"):
            ctype += "; charset=utf-8" if "charset" not in ctype else ""
        try:
            with open(real, "rb") as f:
                self._send(200, f.read(), ctype)
        except OSError as e:
            self._send(500, f"read failed: {e}", "text/plain; charset=utf-8")

    def _serve_board(self, which, path, label):
        regen(which)
        try:
            self._send(200, open(path, encoding="utf-8").read())
        except OSError as e:
            self._send(500, f"{label} missing: {e} — try: python3 execution/"
                            f"{ {'missions': 'mission_board.py'}.get(which, 'pulse_dashboard.py') }")

    def do_GET(self):
        self._touch()
        if not self._same_origin():
            self._send(403, "cross-origin", "text/plain; charset=utf-8")
            return
        route = self.path.split("?", 1)[0]
        if route.startswith("/ping"):
            self._send(200, json.dumps({"pulse": True,
                                        "board_mtime": _mtime(BOARD),
                                        "room_mtime": _mtime(ROOM),
                                        "oracle_mtime": _mtime(ORACLE),
                                        "missions_mtime": _mtime(MISSIONS),
                                        "homebase_mtime": _mtime(HOMEBASE),
                                        "assets_mtime": _mtime(ASSETS),
                                        "library_mtime": _mtime(LIBRARY),
                                        "brain_mtime": _mtime(BRAIN),
                                        "intel_mtime": _mtime(INTEL)}), "application/json")
            return
        if route.startswith("/repo/"):
            self._serve_repo(route)
            return
        if route.startswith("/room"):
            self._serve_board("room", ROOM, "room")
            return
        if route.startswith("/oracle"):
            self._serve_board("oracle", ORACLE, "oracle board")
            return
        if route.startswith("/assets"):
            self._serve_board("assets", ASSETS, "asset board")
            return
        if route.startswith("/library"):
            self._serve_board("library", LIBRARY, "library")
            return
        if route.startswith("/brain"):
            self._serve_board("brain", BRAIN, "second brain")
            return
        if route.startswith("/intelligence"):
            self._serve_board("intelligence", INTEL, "intelligence layer")
            return
        if route.startswith(("/pulse", "/missions")):
            # Retired surfaces (two-surfaces collapse, 2026-08-20). Muscle
            # memory and old links land on the Homebase instead of a 404.
            self.send_response(302)
            self.send_header("Location", "/")
            self.send_header("Content-Length", "0")
            self.end_headers()
            return
        if route in HOME_PATHS:
            self._serve_board("homebase", HOMEBASE, "homebase")
            return
        self._send(404, f"no route: {route}\n\ntry / · /brain · /intelligence · /room · /library · /assets · /oracle · /repo/<path>",
                   "text/plain; charset=utf-8")

    def _same_origin(self):
        """Reject requests a page on ANOTHER site caused the browser to send.

        The server has no auth and now runs permanently, so any website open in
        a tab can address it. Browsers block cross-origin READS, but a plain
        form-style POST still fires — which was enough to trigger done / park /
        thread-archive / open-path on this repo from a page the operator merely
        visited. Two locks: an Origin that isn't ours is refused outright, and
        /action demands application/json, which forces a CORS preflight this
        server never answers. Same-origin XHR sends no Origin on GET and the
        board's own fetch() always sets the JSON content type, so the real UI is
        unaffected — as is curl, which sends neither header.
        """
        origin = self.headers.get("Origin")
        if not origin:
            return True
        host = f"127.0.0.1:{self.server.server_address[1]}"
        return origin in (f"http://{host}", f"http://localhost:{self.server.server_address[1]}")

    def do_POST(self):
        self._touch()
        if not self._same_origin():
            print(f"[pulse_serve] refused cross-origin POST from {self.headers.get('Origin')}",
                  file=sys.stderr)
            self._send(403, json.dumps({"ok": False, "error": "cross-origin"}), "application/json")
            return
        if self.path != "/action":
            self._send(404, '{"ok": false}', "application/json")
            return
        ctype = (self.headers.get("Content-Type") or "").split(";")[0].strip().lower()
        if ctype != "application/json":
            self._send(415, json.dumps({"ok": False, "error": "application/json required"}),
                       "application/json")
            return
        try:
            length = int(self.headers.get("Content-Length") or 0)
            payload = json.loads(self.rfile.read(length) or b"{}")
            action = payload.get("action")
            if action not in ACTIONS:
                self._send(400, json.dumps({"ok": False, "error": "unknown action"}), "application/json")
                return
            ok = dispatch(action, payload.get("args") or {})
            # dict results carry their own ok/error (run_skill); bools wrap
            body = ok if isinstance(ok, dict) else {"ok": bool(ok)}
            self._send(200, json.dumps(body), "application/json")
        except Exception as e:
            self._send(500, json.dumps({"ok": False, "error": str(e)[:200]}), "application/json")


def already_serving(port):
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/ping", timeout=2) as r:
            return b"pulse" in r.read()
    except Exception:
        return False


def main():
    ap = argparse.ArgumentParser(description="Serve the Pulse board live.")
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--idle", type=int, default=7200,
                    help="idle seconds before clean exit; 0 = always-on daemon (no exit)")
    ap.add_argument("--open", action="store_true")
    args = ap.parse_args()

    url = f"http://127.0.0.1:{args.port}/"
    if already_serving(args.port):
        print(f"[pulse_serve] already live → {url}")
        if args.open:
            subprocess.run(["open", url], check=False)
        return

    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)

    def watchdog():
        while True:
            time.sleep(min(30, max(1, args.idle // 4)))
            if time.time() - LAST_HIT > args.idle:
                print("[pulse_serve] idle — exiting clean")
                server.shutdown()
                return

    def heartbeat():
        """Always-on mode has no idle exit and would otherwise print nothing
        for days. detect_dead_launchd() reads the log's mtime as its only
        liveness evidence, so a permanently silent daemon reads as a dead job —
        one line an hour is what keeps the alarm honest."""
        while True:
            time.sleep(3600)
            print(f"[pulse_serve] alive → {url}  "
                  f"(last hit {int(time.time() - LAST_HIT)}s ago)", flush=True)

    if args.idle > 0:
        threading.Thread(target=watchdog, daemon=True).start()
        print(f"[pulse_serve] live → {url}  (idle-exit after {args.idle}s)", flush=True)
    else:
        threading.Thread(target=heartbeat, daemon=True).start()
        print(f"[pulse_serve] live → {url}  (always-on: no idle exit)", flush=True)
    if args.open:
        subprocess.run(["open", url], check=False)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()


if __name__ == "__main__":
    main()
