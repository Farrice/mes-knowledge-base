---
name: "Webapp Testing — DOM Element Reconnaissance"
source_prompt: born-v2
skill: webapp-testing
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are running the **webapp-testing** toolkit's reconnaissance-then-action pattern as a
standalone deliverable: a discovery pass over a rendered page that inventories what's
actually interactable before any test script tries to act on it. The skill states this
directly — "Identify selectors from rendered state" is step 3 of the reconnaissance pattern,
and the Common Pitfall it names by name is skipping this step (or running it before
`networkidle`). This deliverable exists because writing action scripts against assumed
selectors is the generic failure mode this toolkit is built to prevent.

## Input Required

- `[BASE_URL]` — the URL of the running app to inspect (server must already be running, or
  started separately via `scripts/with_server.py`)
- `[SCOPE]` — what to inventory: "full page," or a narrower target (e.g., "the settings
  modal," "the nav bar only")
- `[POST_LOAD_ACTION]` (optional) — any interaction needed to reach `[SCOPE]` before
  inspection (e.g., "click the 'Settings' link first")

## Execution Protocol

**1. Navigate and wait for `networkidle` before any inspection call** — this is the skill's
Common Pitfall rule verbatim: "Don't inspect the DOM before waiting for networkidle on
dynamic apps." Every inventory action below happens only after this wait resolves.

**2. If `[POST_LOAD_ACTION]` is set, perform it now**, then re-settle
(`page.wait_for_load_state('networkidle')` again if the action triggers async rendering)
before inventorying — the scope may only exist post-interaction.

**3. Inventory buttons.** For each, record visibility and text:
```python
buttons = page.locator('button').all()
for i, button in enumerate(buttons):
    text = button.inner_text() if button.is_visible() else "[hidden]"
```

**4. Inventory links.** For each, record display text and `href`:
```python
links = page.locator('a[href]').all()
for link in links:
    text = link.inner_text().strip()
    href = link.get_attribute('href')
```

**5. Inventory input fields** (`input`, `textarea`, `select`). For each, record its
identifying attribute and type, falling back through name → id → "[unnamed]" exactly as the
skill's own discovery example does — do not invent a name when neither attribute is present:
```python
inputs = page.locator('input, textarea, select').all()
for input_elem in inputs:
    name = input_elem.get_attribute('name') or input_elem.get_attribute('id') or "[unnamed]"
    input_type = input_elem.get_attribute('type') or 'text'
```

**6. Capture a full-page screenshot as the visual reference** for the inventory —
`page.screenshot(path=..., full_page=True)` — so the selector list can be cross-checked
against what's actually on screen.

**7. Report the inventory as a structured list**, not prose — this deliverable's entire
purpose is to hand a downstream test-writing step a reliable selector menu.

## Output Contract

- A Python script (or script output, if already run) that produces three inventories:
  buttons, links, input fields — each with count and per-item identifying detail
- One full-page screenshot path as the visual cross-reference
- Every reported selector is something the script actually located — no selector appears in
  the output that wasn't produced by a `.locator(...).all()` call in this session
- If `[SCOPE]` narrows to a sub-region (e.g., a modal), the locator calls are scoped
  accordingly (e.g., `page.locator('#modal button')`) rather than inventorying the whole page
  and manually filtering after the fact

## Output Skeleton

```
SCREENSHOT: <path>

BUTTONS (<count> found):
  [<index>] "<visible text or [hidden]>"
  ...

LINKS (<count> found):
  - "<link text>" -> <href>
  ...

INPUT FIELDS (<count> found):
  - <name/id or [unnamed]> (<type>)
  ...
```

## Quality Gate

- [ ] Did `page.wait_for_load_state('networkidle')` run before the first inventory call?
- [ ] Is every button/link/input in the report backed by an actual `.locator().all()` result
      from this session — none inferred or assumed?
- [ ] Does the input-field naming fall back name → id → "[unnamed]" rather than fabricating
      a label?
- [ ] Is there a full-page screenshot path included as visual cross-reference?
- [ ] If `[SCOPE]` was a sub-region, are the locators actually scoped to it (not the whole
      page filtered manually after)?

## Deploy When

Before writing any selector-dependent test/automation script against a dynamic webapp —
whenever the actual rendered structure of a page (or a sub-region of it) is unknown or
suspected to differ from the source code's apparent structure.
