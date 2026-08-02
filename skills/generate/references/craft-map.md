# Craft Map — which master loads before which generation (BINDING, Farrice 2026-08-02)

**The rule: no generation — paid or free, draft or final — fires with a freehand prompt.**
Every prompt is authored through the matching craft layer below, then gets a doctor pass.
Scar this exists for: the 2026-08-02 Seedance teaser take 1 — prompt written freehand while
`cinema-worldbuilder-pro` sat extracted on the shelf; output was slop. Take 2 through the
grammar, same model, same price: production-usable. The knowledge was never the gap;
loading it mechanically is.

| Output | Load FIRST | Doctor pass |
|---|---|---|
| Seedance video (any) | `skills/cinema-worldbuilder-pro/SKILL.md` — mode select (M1–M5), Write-the-Visible, FOV table, block structure | Read the prompt back as the shot: every word renders a pixel or gets cut |
| Kling video / multi-shot | `skills/fantastic-posters/workflows/kling-multishot.md` + cinema-worldbuilder cut grammar | Cut list explicit, continuity held across cuts |
| AI-video direction / film craft | `/pj-accetturo-ai-video` · `/tao-prompts-ai-video` | Story beat before shot beat |
| Stylized image (catalog style) | `skills/fantastic-posters/SKILL.md` style picker + the style's own build notes | Style fields (title/subtitle/footer/subject) filled deliberately, never defaulted |
| Open art direction (direct lane) | `/art-direct` or `/creative-prompt` (creative-direction skill) + relevant style card from `skills/generate/styles/` | Prompt is a full production document: subject, composition, light source+direction+temp, lens language, palette anchored to surfaces, finish register |
| Photoreal people | `higgsfield-soul` lane via `creative_router.py` (BINDING) + `/banana-pro` for character builds | Face/identity locked to reference, never freehand |
| Persistent character/world | `/jcin-pipeline` (bible → locks → plates) + `jcin-prompt-doctor` | Canon checked against the bible |
| Anime/manga (his lane) | direct lane + his style cards (`manga-ink`, `shonen-ui-glow`, `alchemist-blaze`, …) + character ref once locked | Register named (which anime grammar), text minimal and intentional |
| Vector/text-heavy (recraft) | recraft recipe notes + `/kittl` typography judgment for lockups | Text content exact, style param deliberate ($0.04 vs $0.08 vector) |
| Audio TTS/music | recipe notes; voice/tone brief written like a VO director's note (pace, register, where the emphasis lands) | Read the text aloud mentally — punctuation drives the read |
| Mood boards / visual development | `/mood-board` (creative-direction skill) | Board argues ONE direction, not a collage of maybes |

**Intent mirror (creative asks):** before generating from a raw dump, reflect back in ≤5 lines:
deliverable + format, felt standard ("cinematic macro, matte, no gloss"), references in play,
budget, and the ONE thing that would make it his ("what's the detail that makes this yours?").
Proceed on his confirm or visible non-objection; never silently guess taste on new ground.

**Show craft with the quote:** for paid video, the crafted prompt is presented WITH the cost
quote — one look approves money and craft together.

This map extends as masters are extracted (see the master-hunt mission). New master → new row.
