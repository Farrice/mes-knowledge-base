# 00-social-content — quality gates & Magic Layer

Scripts da **pipeline de geração do 00-social-content** que antes viviam, por acoplamento
histórico, dentro de `mkt-visual-identity/scripts/`. Movidos para cá (AIOS — mkt-vi agnostic
refactor) para que a `mkt-visual-identity` permaneca uma skill de identidade de marca
**agnostica e identica** nos tres sistemas que a consomem (00-social-content, 00-slides,
00-youtube-to-ebook).

Os gates (`check_*.py`, `dead_space.py`) sao invocados pelo agent `ssc-template-builder` via
`references/template-authoring/shared/quality-gate.md`. `migrate_data_slots.py` e
`decompose.py` sao utilitarios da pipeline/Studio.

---

## decompose.py (Magic Layer — AIOS-139 Addendum 4)

Script: `scripts/decompose.py`

Decomposes a flat full-AI slide image into RGBA layers using
`fal-ai/qwen-image-layered` (~$0.05 per image). Part of the Content Studio
"Magic Layer" feature — turns a flat image into editable, re-bakeable layers
without re-prompting.

### Fail-safe contract (REQUIRED by all consumers)

`FAL_KEY` is OPTIONAL. When absent the script:
- Writes `{output_dir}/manifest.json` with `{"status": "skipped", "reason": "no_fal_key", "layers": []}`
- Prints one stderr line: `decompose: FAL_KEY not set — decomposition skipped`
- Exits with `EXIT_SKIPPED` (3)
- Does NOT raise, does NOT leave a partial `layers/` dir

Consumers MUST check for exit code 3 / manifest `status == "skipped"` and
surface "decomposition unavailable" gracefully — do not crash.

### Exit codes

| Constant     | Value | Meaning |
|---|---|---|
| `EXIT_OK`      | 0 | Success — `layers/` + `manifest.json` written |
| `EXIT_ERROR`   | 1 | API / network / safety error — error manifest, no `layers/` |
| `EXIT_SKIPPED` | 3 | `FAL_KEY` not set — skipped-stub manifest, no `layers/` |

### CLI

```
decompose.py (--image PATH | --image-url URL)
             [--output-dir DIR]
             [--num-layers N]   default 4
             [--steps N]        default 28
             [--guidance F]     default 5.0
             [--format {PNG,JPEG,WEBP}]  default PNG
             [--seed N]
             [--prompt TEXT]
             [--negative-prompt TEXT]
```

`--image PATH` uploads the file via `fal_client.upload_file()`.
`--image-url URL` uses a pre-hosted URL directly (skips upload).

### Manifest schema (status: ok)

```json
{
  "tool": "decompose.py",
  "model": "fal-ai/qwen-image-layered",
  "source_image": "<path or url>",
  "status": "ok",
  "layer_count": 4,
  "seed": 42,
  "has_nsfw_concepts": [false, false, false, false],
  "params": {
    "num_layers": 4,
    "num_inference_steps": 28,
    "guidance_scale": 5.0,
    "output_format": "PNG"
  },
  "cost_usd_estimate": 0.05,
  "layers": [
    {"index": 0, "file": "layers/00.png", "width": 1080, "height": 1350,
     "source_url": "https://cdn.fal.ai/..."}
  ]
}
```

### Atomicity guarantee

Downloads go to a temp dir; only on full success the temp dir is moved to
`{output_dir}/layers/`. An error at any point leaves NO partial `layers/` dir.
