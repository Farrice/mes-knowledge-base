---
name: "Webapp Testing — Console Log Capture"
source_prompt: born-v2
skill: webapp-testing
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are running the **webapp-testing** toolkit's console-log capture pattern — the skill's
description names "viewing browser logs" as one of its four core supported tasks (alongside
verifying functionality, debugging UI behavior, and capturing screenshots), and ships a
dedicated example (`examples/console_logging.py`) for it. This deliverable is for debugging:
surfacing what the app's own JS is logging (errors, warnings, custom debug output) during a
specific interaction, not for asserting UI state directly.

## Input Required

- `[BASE_URL]` — URL of the running app to inspect
- `[TRIGGER_ACTION]` — the interaction expected to produce the console activity under
  investigation (e.g., "click Dashboard," "submit the form with an invalid email")
- `[LOG_FOCUS]` (optional) — specific log types of interest (`error`, `warning`, `log`, etc.);
  default is to capture all types
- `[OUTPUT_PATH]` (optional) — where to save the captured log; default the skill's own
  example convention (`/mnt/user-data/outputs/console.log`)

## Execution Protocol

**1. Register the console listener before navigation** — the handler must be attached prior
to `page.goto()` so no early log lines are missed:
```python
console_logs = []

def handle_console_message(msg):
    console_logs.append(f"[{msg.type}] {msg.text}")
    print(f"Console: [{msg.type}] {msg.text}")

page.on("console", handle_console_message)
```

**2. Set an explicit viewport** on the page (`new_page(viewport={'width': 1920, 'height': 1080})`)
to match rendering conditions consistently across runs — the skill's own example does this
even though the deliverable's focus is console output, not visuals.

**3. Navigate and wait for `networkidle`** before triggering `[TRIGGER_ACTION]` — load-time
console output (init errors, warnings) needs to be captured cleanly before interaction-time
output is added to the same stream.

**4. Perform `[TRIGGER_ACTION]`**, then add a short settle wait
(`page.wait_for_timeout(1000)` in the skill's example) so asynchronous console output
triggered by the action has time to arrive before the browser closes.

**5. If `[LOG_FOCUS]` narrows the scope, filter at report time, not capture time** — keep the
handler capturing every message type, then filter the `console_logs` list when writing the
report, so nothing relevant is silently dropped by an over-narrow listener.

**6. Persist the full capture to `[OUTPUT_PATH]`** as newline-joined log lines, and report a
count of messages captured — the skill's example writes the joined log and prints
`f"Captured {len(console_logs)} console messages"` as confirmation.

**7. Always close the browser after capture**, even if `[TRIGGER_ACTION]` errors — logs
captured up to the point of failure are still useful evidence.

## Output Contract

- A Python script that registers the console handler before `page.goto()`, not after
- The full ordered log (type-tagged, `[type] text` format) written to `[OUTPUT_PATH]`
- A console-message count reported alongside the saved path
- If `[LOG_FOCUS]` was set, a filtered view included in the report in addition to (not
  instead of) the full saved log
- Any `error`-type messages called out explicitly in the summary, since these are the
  highest-signal debugging output regardless of whether `[LOG_FOCUS]` was set

## Output Skeleton

```python
from playwright.sync_api import sync_playwright

console_logs = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1920, 'height': 1080})

    def handle_console_message(msg):
        console_logs.append(f"[{msg.type}] {msg.text}")

    page.on("console", handle_console_message)

    page.goto('<BASE_URL>')
    page.wait_for_load_state('networkidle')

    # <TRIGGER_ACTION>
    page.wait_for_timeout(1000)

    browser.close()

with open('<OUTPUT_PATH>', 'w') as f:
    f.write('\n'.join(console_logs))
```

SUMMARY:
Captured: <count> messages -> <OUTPUT_PATH>
Errors: <count> — <list, or "none">
[If LOG_FOCUS set] Filtered (<LOG_FOCUS>): <matching lines>

## Quality Gate

- [ ] Is `page.on("console", ...)` registered before `page.goto()`?
- [ ] Does the capture include every message type (filtering, if any, happens at report time
      only)?
- [ ] Is there a settle wait after `[TRIGGER_ACTION]` before the browser closes?
- [ ] Is the full log actually persisted to `[OUTPUT_PATH]`, not just printed?
- [ ] Are `error`-type messages explicitly surfaced in the summary rather than buried in the
      raw log dump?

## Deploy When

Debugging unexpected UI behavior where the cause is suspected to be a JS error, a failed
network call logged to console, or custom app-level debug output — any time the fix requires
seeing what the browser's own JS runtime is reporting, not just what's visually rendered.
