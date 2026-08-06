#!/usr/bin/env python3
"""pulse_serve.py — on-demand live server for the Pulse board (Readout OS
phase 4, 2026-08-06). Stdlib only, localhost only, idle auto-exit — a session
tool, not a daemon.

GET  /            regenerate the board (always fresh) and serve it
POST /action      {"action": "...", "args": {...}} → pulse_actions dispatch →
                  regenerate → {"ok": true}; the page reloads itself

Usage:
    python3 execution/pulse_serve.py [--port 8765] [--idle 7200] [--open]

If the port is already serving a healthy pulse (GET /ping ok), --open just
opens the existing server instead of starting a second one.
"""
import argparse
import json
import os
import subprocess
import sys
import threading
import time
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOARD = os.path.join(ROOT, ".agent", "pulse", "pulse-board.html")
PY = sys.executable or "python3"

LAST_HIT = time.time()


def regen():
    try:
        subprocess.run([PY, os.path.join(ROOT, "execution", "pulse_dashboard.py")],
                       capture_output=True, text=True, timeout=90)
    except Exception as e:
        print(f"[pulse_serve] WARN regen failed: {e}", file=sys.stderr)


ACTIONS = {"done", "park", "outcome", "outcome-dismiss", "outcome-snooze", "thread-archive", "open-path"}


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
    sys.path.insert(0, os.path.join(ROOT, "execution"))
    import pulse_actions as pa
    if action == "done":
        return pa.act_done(args.get("slug", ""), args.get("outcome", ""))
    if action == "park":
        return pa.act_park(args.get("slug", ""), args.get("reason", ""))
    if action == "outcome":
        return pa.act_outcome(args.get("deliverable", ""), args.get("revenue", 0), args.get("outcome", ""))
    if action == "outcome-dismiss":
        return pa.act_outcome_dismiss(args.get("deliverable", ""))
    if action == "outcome-snooze":
        return pa.act_outcome_snooze(args.get("deliverable", ""))
    if action == "thread-archive":
        return pa.act_thread_archive(args.get("thread", ""))
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
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        self._touch()
        if self.path.startswith("/ping"):
            self._send(200, '{"pulse": true}', "application/json")
            return
        regen()
        try:
            self._send(200, open(BOARD, encoding="utf-8").read())
        except OSError as e:
            self._send(500, f"board missing: {e}")

    def do_POST(self):
        self._touch()
        if self.path != "/action":
            self._send(404, '{"ok": false}', "application/json")
            return
        try:
            length = int(self.headers.get("Content-Length") or 0)
            payload = json.loads(self.rfile.read(length) or b"{}")
            action = payload.get("action")
            if action not in ACTIONS:
                self._send(400, json.dumps({"ok": False, "error": "unknown action"}), "application/json")
                return
            ok = dispatch(action, payload.get("args") or {})
            self._send(200, json.dumps({"ok": bool(ok)}), "application/json")
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
    ap.add_argument("--idle", type=int, default=7200, help="idle seconds before clean exit (default 2h)")
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

    threading.Thread(target=watchdog, daemon=True).start()
    print(f"[pulse_serve] live → {url}  (idle-exit after {args.idle}s)")
    if args.open:
        subprocess.run(["open", url], check=False)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()


if __name__ == "__main__":
    main()
