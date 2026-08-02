# Model Recipes

One JSON file per model. `generate_media.py` reads these for routing, quoting, and generation.

## Schema

```json
{
  "id": "recraft-v3",                    // recipe id — the --model value
  "provider": "fal",                     // key into generate_media.py PROVIDERS
  "media_type": "image|video|audio",
  "endpoint": "fal-ai/recraft/v3/text-to-image",   // Fal queue endpoint (wrapper-less recipes)
  "defaults": {"image_size": "square_hd"},         // params merged under --param overrides
  "prompt_param": "prompt",              // where the prompt goes in the payload
  "ref_param": "image_url",              // where --ref data-URIs go (absent = refs refused)
  "ref_list": false,                     // true → list of refs, false → single
  "pricing": {"unit": "per_image|per_second|per_1k_chars|per_generation",
               "table": {"default": 0.04}},        // param VALUES may key overrides
  "guard": {"gate": "fal_budget_guard", "mode": "generic",
             "hard_blocked": false},
  "wrapper": null,                       // non-null → run refuses, prints this command
  "quote_required": false,               // true for ALL paid video
  "timeout_s": 300,
  "status": "deferred",                  // optional: stub — run refuses until verified + removed
  "notes": "…"
}
```

## Rules

- **Wrapper-backed models** (`wrapper` non-null) keep their existing script as the ONLY code
  path — the recipe is metadata for routing/quoting. Index outputs via `generate_media.py index`.
- **Wrapper-less recipes** run through the generic guard mode: $1.00/call ceiling. A model that
  needs more must graduate to its own named mode in `fal_budget_guard.py` (deliberate friction).
- **Adding a model**: verify endpoint id + price on fal.ai/models (never from memory), write the
  recipe, run `generate_media.py quote` before the first real call.
- **`seedance-1080p`** stays `hard_blocked` — documented refusal, no override.
- New provider (Kie/WaveSpeed/Replicate): add an adapter to `PROVIDERS` in `generate_media.py`
  + recipes with that `provider`. Each new provider = new account + spend line = Farrice's
  cost-gate decision first.
