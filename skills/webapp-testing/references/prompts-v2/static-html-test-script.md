---
name: "Webapp Testing — Static HTML Test Script"
source_prompt: born-v2
skill: webapp-testing
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are running the **webapp-testing** toolkit's static-HTML path. Per the skill's decision
tree, the first branch on any task is "Is it static HTML?" — if yes, the correct move is to
read the HTML file directly to identify selectors before touching a browser, because static
markup doesn't require JS execution to reveal its structure. Only if that read fails or is
incomplete does the task get treated as dynamic. You are the practitioner operating that
first branch honestly — reading the file, not assuming its structure.

## Input Required

- `[HTML_FILE_PATH]` — path to the local `.html` file (relative or absolute)
- `[TASK]` — the interaction(s) to automate or verify (e.g., "fill and submit the contact
  form," "confirm the nav links point to the right anchors")
- `[SUCCESS_CRITERIA]` — the observable proof the task worked (post-submit DOM state,
  screenshot, absence/presence of an element)

## Execution Protocol

**1. Read the HTML file directly first.** Before writing any Playwright code, read
`[HTML_FILE_PATH]` to identify real selectors (ids, names, classes, `type` attributes,
button text) from the actual markup — this is the skill's stated first move for static HTML,
distinct from the dynamic-webapp reconnaissance pattern which inspects a *rendered* page.

**2. Decide if the static path still holds.** If the file relies on JS to build meaningful
structure at load (e.g., a client-side template that renders into an empty `<div id="root">`),
the direct-read approach will fail or be incomplete — stop and route to the dynamic-webapp
deliverable instead, per the skill's explicit fallback rule.

**3. Build the file:// URL correctly** — always resolve to an absolute path first:
```python
import os
html_file_path = os.path.abspath('[HTML_FILE_PATH]')
file_url = f'file://{html_file_path}'
```

**4. Launch chromium headless with an explicit viewport** when visual fidelity matters for
screenshots — the skill's own static-HTML example sets `viewport={'width': 1920, 'height': 1080}`
rather than relying on the default.

**5. Navigate and act using the selectors confirmed in step 1** — text selectors
(`text=Click Me`), id selectors (`#name`), or attribute selectors
(`button[type="submit"]`), matching what step 1 actually found in the markup.

**6. Screenshot before and after the interaction** when the task involves state change (form
fill, submit, toggle) — a before/after pair is the pattern in the skill's own example
(`static_page.png` pre-submit, `after_submit.png` post-submit), and it gives verifiable
evidence rather than an assertion of success.

**7. Add a short wait after state-changing actions** (`page.wait_for_timeout()`) even on
static HTML if the interaction triggers any client-side JS (form validation, a toggle
animation) before the after-screenshot is taken.

**8. Always close the browser.**

## Output Contract

- One self-contained Python file using `sync_playwright()` and a `file://` URL built from
  `os.path.abspath()` — never a relative or bare path passed to `page.goto()`
- Selectors in the script are traceable to a direct read of `[HTML_FILE_PATH]` performed in
  this session — not assumed
- If the task involves any state change, a before-action and after-action screenshot, both
  with explicit file paths
- `browser.close()` on every exit path
- A short result note confirming `[SUCCESS_CRITERIA]`, or a note that the file requires
  JS-rendered content and should be re-routed to the dynamic-webapp deliverable

## Output Skeleton

```python
from playwright.sync_api import sync_playwright
import os

html_file_path = os.path.abspath('<HTML_FILE_PATH>')
file_url = f'file://{html_file_path}'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1920, 'height': 1080})

    page.goto(file_url)

    # <before-screenshot, if state will change>

    # <action(s) using selectors confirmed by reading HTML_FILE_PATH directly>

    # <after-screenshot / evidence capture tied to SUCCESS_CRITERIA>

    browser.close()
```

RESULT: <met / not met — or: reroute to dynamic-webapp-test-script, reason: <why>>

## Quality Gate

- [ ] Was `[HTML_FILE_PATH]` actually read before selectors were chosen — not inferred?
- [ ] Is `file_url` built from `os.path.abspath()`, never a bare relative path?
- [ ] If the task changes page state, are there both before- and after-action screenshots?
- [ ] Does `browser.close()` run on every path?
- [ ] If the file turned out to depend on JS rendering, was it explicitly re-routed to the
      dynamic-webapp deliverable rather than forced through the static path?

## Deploy When

The target is a local `.html` file with no server required — landing pages, static prototypes,
email templates, or any markup whose structure is fully present without JS execution.
