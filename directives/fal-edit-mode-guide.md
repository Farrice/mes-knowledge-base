# Fal Edit Mode Guide (`fantastic-posters --mode=edit`)

> **Source:** Patterns harvested from [`robonuggets/gpt-image-2-skill`](https://github.com/robonuggets/gpt-image-2-skill) (MIT) into `skills/fantastic-posters/generate.js` (2026-04-30).
> **Companion:** `directives/fal-usage-policy.md` for budget-gating rules.

GPT Image 2's edit endpoint (`openai/gpt-image-2/edit`) is the strongest text-preserving image-edit model on Fal. This guide answers: *when should you edit instead of regenerating, and how do you do it without burning budget?*

---

## When to edit vs. regenerate

| Situation | Pick | Why |
|---|---|---|
| User wants the same poster but with a different headline | **edit** | Preserves layout, palette, typography. Regenerating starts from scratch and you'll get a similar-but-different design. |
| User wants the same poster with a different photo subject | **edit** with `--input=<existing>` + `--refs=<new-photo>` | Templates the layout from the original. |
| User wants "the same vibe but as a portrait instead of landscape" | **regenerate** | Aspect change forces re-composition. Edit can't reflow that elegantly. |
| User says "change just the sky" / "swap the logo" / "replace the headline" | **edit** with `--mask=<url>` | Mask-constrained edit preserves everything outside the mask. |
| User wants 4 variants of the same idea | **regenerate** with `--variants=4` | Edit reinterprets the input — variants come out too similar. |
| User wants to iteratively refine ("now make it darker", "now move the logo down") | **edit** chained | Each edit feeds the previous output URL back as input. |
| User wants strict style preservation (logo, brand colors, exact font) | **regenerate** with `--logo=<file>` + `--refs=<brand-book.pdf>` | Edit endpoint reinterprets style more than it preserves. For logo lock-in, the existing logo-anchor pipeline beats edit. |

**Rule of thumb:** *edit changes content; regenerate changes design.* If the design needs to stay the same and the content should change, edit. If the design should change, regenerate.

---

## How to invoke

### Pure edit (no style template — just an instruction)

```bash
./gen.sh "Same scene but everyone is on their phone now. One taking a selfie, one annoyed on a call." \
  --input=https://v3b.fal.media/files/b/.../original.png \
  --quality=medium
```

The brief here is the **edit instruction**, not a poster brief. Describe the *change*, not the whole scene.

### Mask-constrained edit (surgical region)

```bash
./gen.sh "Replace the headline text with 'TODAY'S SPECIAL — Lobster Roll $24'" \
  --input=https://v3b.fal.media/files/b/.../poster.png \
  --mask=https://example.com/headline-mask.png \
  --quality=medium
```

The mask is a B/W image where **white = edit, black = preserve**. Same dimensions as the input image. If your mask is in `/Users/.../mask.png`, the script auto-uploads it via the same `refToImageUrl` helper that handles `--refs`.

### Style-templated edit

When the chosen style requires a photo input (`needsPhoto: true` in `styles.js` — currently `luxury-real-estate`), passing `--refs` triggers edit-endpoint mode automatically. This is the existing behavior — no change needed.

---

## Reference-image hosting

The Fal edit endpoint requires `image_urls` to be **publicly accessible URLs**. Options the script supports:

1. **Pass a Fal-hosted URL directly** — e.g., a previous Fal output URL. No upload step.
2. **Pass a public HTTPS URL** — S3, GitHub raw, your own server. No upload step.
3. **Pass a local file path** — the script reads the bytes and uploads:
   - **If `KIE_KEY` is set in `.env`**: uploads to Kie AI storage, returns a hosted URL.
   - **If not**: encodes as a base64 data URI inline (works for small images; not recommended for >2MB).
4. **PDF first page** — if the path ends in `.pdf`, page 1 is auto-rendered to PNG at 2x DPI before upload (requires `pdfjs-dist` + `canvas` deps).

**Fal output URLs expire** — download immediately if you want a permanent copy. The script always saves the bytes locally to `./out/`.

---

## Mask format requirements

When `--mask=<url|path>` is set:

- Format: PNG, RGB or grayscale
- Dimensions: **exactly match the input image** (otherwise Fal rejects or produces garbage)
- Content: **white pixels (255,255,255) = edit this region; black pixels (0,0,0) = preserve**
- Anti-aliasing: gray values are interpreted as partial edits (smooth transitions)
- Common gotcha: a JPEG mask compresses gray values and softens edges → use PNG

If you don't have a mask handy, regenerate without `--mask` first to see what the model picks. If it reinterprets too much, generate a quick mask in any image editor (paint white over the region you want changed) and re-run with `--mask`.

---

## Cost notes

- Edit pricing matches text-to-image: `low` ~$0.011, `medium` ~$0.04, `high` ~$0.17 per output image.
- **The mask itself is free** — it's just metadata, not a billed API call.
- `--variants=N` works on edit endpoint same as text-to-image (N images per single API call).
- `--rembg` works on edit output same as text-to-image (chained `fal-ai/imageutils/rembg` ~$0.005/call).

Always pre-flight via `python3 execution/fal_budget_guard.py check --mode=edit --quality=<...> --n=<...>` per `directives/fal-usage-policy.md`.

---

## Prompt patterns for edits (from upstream skill)

GPT Image 2's edit endpoint preserves more when you describe the **change**, not the whole scene:

✅ **Good**: "Same workers on the beam — but they're all on phones now. One taking a selfie."
✅ **Good**: "Same poster, same layout — but the headline now reads 'TONIGHT' in red."
✅ **Good**: "Add three small chalk-drawn stars in the upper-right corner. Don't change anything else."

❌ **Bad** (re-describes the whole image): "A vintage diner chalkboard reading TODAY SPECIAL — Lobster Roll $24, hand-lettered in white chalk on a black slate board, photographed at golden hour, with chalk dust at the base of the lettering. Now make it say TONIGHT instead of TODAY."

The model's job is to find the delta. If you re-describe the whole scene, it treats the request as "regenerate using these specs as a reference," which produces a similar-but-different image rather than a surgical edit.

---

## Failure modes & recovery

| Symptom | Cause | Fix |
|---|---|---|
| "No images returned: {detail: 'Invalid image URL'}" | `--input` URL not publicly accessible | Re-host on Fal/S3/Kie or use a public URL |
| Output reinterprets the entire scene | Prompt re-described the scene instead of the delta | Rewrite prompt as "Same X — but Y change" |
| Output ignores the mask | Mask dimensions don't match input | Verify mask is exact same WxH as input |
| Output text is wrong / has typos in the unchanged region | Edit endpoint regenerated text the model couldn't read in the input | Use `--mask` to constrain change to non-text region; or regenerate from scratch |
| Logo subtly redrawn | Edit endpoint reinterprets logos | Use the existing `--logo=<file>` pipeline (passes logo as separate ref with explicit "do not redraw" clause) instead of edit |

---

## Scope (what this guide does NOT cover)

- **Video edits**: Use Kling/Seedance pipelines, not this guide.
- **Style transfer**: GPT Image 2 edit reinterprets style. For tight style transfer, use Flux on Fal.
- **Photoreal portrait edits**: Edit endpoint can produce uncanny faces. For portraits, use Nano Banana Pro.
- **Vector / SVG output**: PNG only. Convert externally if needed.
