---
date: 2026-07-25
session: jen-listings
problem_class: scraping / voice-extraction / blocked-pipeline
tags: [instagram, playwright, voice-profile, watch, yt-dlp, client-voice]
---

# Extracting a client's real voice from Instagram when downloads are blocked

## The problem

A client's content register was wrong in our skill — it encoded a hype voice ("real talk," "unicorn," "smart money") that Farrice flagged as "not naturally her style." The fix required her *actual* words, which live on Instagram. Two walls:

1. **yt-dlp is blocked anonymously on IG** — "Instagram sent an empty media response." `--cookies-from-browser chrome` hung indefinitely (Chrome's cookie DB is locked while Chrome runs; the command backgrounded and died at exit 144).
2. **No Whisper key configured** — `/watch` reports `status: needs_key`, so no audio transcription path.

Net effect: the obvious pipeline (`/watch <reel-url>` → transcript) fails completely at both stages.

## The crack

**Three independent sources, none of which require downloading anything.**

1. **Captions via `og:description` meta tags.** Instagram serves full post captions in page metadata to logged-out requests. From an already-navigated Playwright page, same-origin `fetch()` each post URL and regex the meta tag — 20 captions in one tool call:
   ```js
   const r = await fetch('/_jiing/reel/DYkn2gBPWJq/', {credentials: 'same-origin'});
   const html = await r.text();
   const m = html.match(/<meta name="description" content="([^"]*)"/);
   ```
   Returns likes, comments, date, and the complete caption text. HTML-entity-encoded; decode before quoting.

2. **Frames via canvas seek-capture.** The `<video>` element's `src` is a `blob:` URL (unusable externally), but the pixels are readable in-page. Play muted, pause, then seek-and-draw to a canvas:
   ```js
   vid.currentTime = t;
   await new Promise(r => { const h = () => {vid.removeEventListener('seeked', h); r();}; vid.addEventListener('seeked', h); setTimeout(r, 3000); });
   canvas.getContext('2d').drawImage(vid, 0, 0, w, h);
   frames.push({t, d: canvas.toDataURL('image/jpeg', 0.7)});
   ```
   Return the array as a JSON string via `browser_evaluate`'s `filename` param (must be **inside the workspace root** — /tmp is rejected), then decode base64 → JPEGs and `Read` them.
   Gotcha: the saved file is a JSON-encoded *string*, so parse twice: `json.loads(json.loads(open(f).read()))`.

3. **Burned-in captions ARE the transcript.** Short-form creators caption every spoken word for silent autoplay. Reading those from frames gave the spoken script with zero transcription cost — and cross-checking against the posted caption proved the two match nearly verbatim, which is itself a voice finding (caption register == spoken register).

## Why it's better than the "correct" path

Even with a Whisper key and working downloads, this is faster for *voice profiling* specifically: 20 captions in one call beats 20 downloads, and frames deliver what audio can't — on-camera formula (she fronts 15-20s then cuts to b-roll), cadence (one word per caption beat), and wardrobe/staging. The transcript alone would have missed that the hook must be **walkable**.

## Reusable procedure

1. `mcp__playwright__browser_navigate` to the profile → evaluate for bio + post links (also `/reels/` tab, scroll to load more).
2. One `browser_evaluate` loop fetching every post URL → `og:description` → captions corpus. Write the voice profile from THIS first; it's cheap and high-yield.
3. Pick 2-3 posts representing distinct formats (talking-head, meme, listing tour) → navigate → canvas seek-capture → decode → Read frames.
4. Write the profile to `skills/<skill>/references/<name>-real-voice-profile.md` and state explicitly that it **wins over genius.md** on register conflicts — otherwise a Tier-2 load silently reverts to the old voice.

## Honest edges

- Logged-out access only reaches public accounts; a private account still needs real auth.
- `--cookies-from-browser chrome` will hang while Chrome is open — don't retry it, it's not a transient failure.
- Frame capture costs image tokens (~11-14 frames per reel at 480px is reasonable; don't sweep a whole grid).
- Playwright MCP writes only inside the workspace root — clean up `.playwright-mcp/` artifacts after decoding.

## Related

Wrong-voice-encoded-in-skill is the deeper failure this fixes: our own golden reference (`6853-willis-SHOOT-SHEET.md`) had calibrated *format* correctly but *voice* wrongly, because we wrote it rather than sourcing it from the client. See `2026-07-07-transcript-only-extraction-generic-output.md` — same family: secondhand source material yields a mechanically-right, humanly-wrong result.
