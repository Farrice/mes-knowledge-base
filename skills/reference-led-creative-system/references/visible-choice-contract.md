# Visible Choice Contract

## Purpose

Prevent a user from choosing among visual directions they cannot actually see.

## Required choice surface

Every direction must include:

| Field | Requirement |
|---|---|
| ID and name | Stable, distinct, human-readable |
| Primary reference | Title, source URL, Refero UUID, preview provenance |
| Local preview | Readable local image with absolute display path |
| Image receipt | Dimensions, format, byte size, SHA-256, capture status |
| Thesis | One sentence naming the creative bet |
| Preserve | 3–5 traits |
| Borrow | At most 2 bounded details |
| Media strategy | Real, generated, stock, screenshot, code-native, or honest placeholder |
| Reject | At least 3 collapse risks |
| Strategic tradeoff | Strength, risk, and system impact |

The pack must also include one local contact-sheet PNG containing every direction and one `receipt.json` proving all preview files were opened successfully.

## Display rule

- Show the contact sheet first.
- Show each direction as an individual local image when detail matters.
- Use absolute local paths in the user-facing message.
- Keep remote Refero preview URLs as provenance links only.
- Do not rely on browser hotlinks, Markdown remote-image rendering, or the user opening an HTML file.

## Failure behavior

If one preview fails capture or inspection:

1. mark that direction `PREVIEW BLOCKED`;
2. retain its semantic research as `TEXT EVIDENCE ONLY`;
3. do not ask for a visual choice;
4. retry through an approved local capture path or replace the reference;
5. record the failure in the receipt.

Never silently substitute a different image after the direction has been named.

## Distinctness gate

Three directions must materially differ on at least four of these six axes:

1. canvas and palette roles;
2. typography personality and scale;
3. composition and layout rhythm;
4. media or imagery strategy;
5. density and surface treatment;
6. energy, motion, or interaction character.

At least two axes must be structural, not merely color or naming. Each direction needs a different primary reference. A renamed variant or minor token swap fails.

## Selection states

- `VISIBLE · UNCHOSEN`: locally verified; ready for human judgment.
- `RECOMMENDED · UNCHOSEN`: Codex recommends it; Farrice has not selected it.
- `SELECTED`: Farrice chose after seeing the options, or explicitly authorized the recommended verdict after visibility passed.
- `TEXT EVIDENCE ONLY`: research exists; visual evidence is missing.
- `PREVIEW BLOCKED`: capture or inspection failed; no visual choice permitted.

## Negative control

The prior failure used remote Markdown images such as:

```text
https://images.refero.design/styles/<site>/<uuid>/preview_0.jpg
```

That URL may remain in provenance. It may never be the only display artifact again.
