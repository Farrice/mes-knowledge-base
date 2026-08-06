# Solution Card — the Live Local Board pattern (static HTML that can act)

**Problem**: a static `file://` dashboard can show state but can't change it — buttons can't write to logs (no server), and once served over http, the browser blocks its `file://` links to sibling surfaces. Result: boards decay into "lists I have no association with" (Farrice, 2026-08-06).

**Solution (shipped in the Pulse, 2026-08-06)** — three parts, all stdlib, $0:

1. **Writers first** (`execution/pulse_actions.py`): every board action is a small deterministic CLI a session could equally type — done/park/reopen append mission lines, outcome log/dismiss shell to `revenue_tracker.py`, snooze does an atomic `os.replace` JSON edit. The writer existing is what makes the board "live"; the server is just a trigger.
2. **On-demand server, not a daemon** (`execution/pulse_serve.py`): stdlib `ThreadingHTTPServer`, 127.0.0.1 only, regenerates the page on every GET (always fresh), `POST /action` dispatches to the writers, idle watchdog exits clean (default 2h), `--open` reuses an already-running instance via `/ping`.
3. **Dual-mode JS contract**: `PULSE_LIVE = location.protocol.startsWith('http')`. Live → POST + reload; `file://` → the same buttons copy the exact CLI command (graceful, nothing breaks). **Gotcha**: http pages cannot navigate to `file://` URLs — route those clicks through a ROOT-jailed `open-path` server action (macOS `open`).

**When to reuse**: any board/surface that needs click-to-act (the Briefing Room the day it needs archiving; the assets board for keep/kill verdicts). Copy the three-part shape; never skip part 1 — a server without honest CLI writers is just hidden state mutation.

**Verify pattern**: scratch-data selftest (scratch mission slug, scratch pending entry, scratch handoff), jail test (`open-path` on `/etc/hosts` → refused), unknown action → 400, idle-exit with short `--idle`.
