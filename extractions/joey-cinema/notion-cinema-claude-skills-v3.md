# The AI Cinema Claude skills got a BUFF! (Keyword: Consistency)

> Source: https://pyrite-mallow-3b0.notion.site/cinema-claude-skills-v3 (public Notion page, harvested 2026-07-13 via Playwright)
> Companion doc to "Joey's Skill Files v3.0" — the three Claude skills: banana-pro-director-30, cinema-worldbuilder-pro-30, story-bible-builder.
> Harvest notes: full page rendered (68 blocks), all toggles expanded, no same-site sub-pages linked from this page. The intro references "the contest brief at the bottom," but no contest section exists anywhere in the rendered page — apparently removed or leftover copy from a prior drop. The single sample prompt code block appears twice in the DOM with identical content; captured once.

> **[callout]** Watch the full video here: [https://youtu.be/x5nP-3t6R9o](https://youtu.be/x5nP-3t6R9o)

> **[callout]** Download the Claude Skills [here](https://www.dropbox.com/scl/fo/uameeu1arouw7esu5xdj0/AJB8ctYDF-IDkzyUKOdAWL4?rlkey=uc7r9nwi9lixfpnmfp9gzcxzf&st=zm29qy3e&dl=0)

If you watched the video, you already know what these do. This is the doc for the people who want to actually use them. No course. No upsell. Three skills to download, the prompts they write, and the contest brief at the bottom.

Same deal as last time: I've burned a stupid amount of credits figuring out what breaks so you don't have to. These aren't perfect. They're closer.

---

### What's actually in this drop

Three Claude skills. Download them, drop them into Claude, they work together.

- banana-pro-director-3.0 — every still. Character faces, outfits, character sheets, scene plates, detail shots, outfit swaps.
- cinema-worldbuilder-pro-3.0 — every Seedance video. Cinematography grammar, frame control, audio rules, character locks.
- story-bible-builder — the new one. Interview-driven. It walks you through your world and spits out a canon doc as an installable skill, so every future prompt already knows your characters, their voices, their movement, your tone, your rules. This is the one that makes the other two stop drifting.

They stack. The bible carries who and why. Banana Pro carries what it looks like. Cinema Worldbuilder carries how it's shot. You stop re-explaining your world every single prompt.

---

## What changed

#### Character sheets went from 6 panels to 3

This is the biggest one and the reason is dumb-simple: a sheet is one image with a fixed pixel budget.

Six panels splits that budget six ways. The face — the entire reason the sheet exists — lands in cells too small to hold real identity. Then you feed that sheet into a video generation and the model has to lock onto a face it can barely see, and you get drift. Not because the model's bad. Because you handed it a thumbnail.

Three panels roughly doubles the resolution per cell. The new default:

1. LEFT — full body front, head removed. Isolates the garment, the silhouette, the proportions. Zero facial data competing for attention.
2. CENTER — full body rear, head attached. Hair fall, back construction, hem, footwear.
3. RIGHT — tight chest-up face lock. Chest-up. Not waist-up. This is the identity anchor and it needs the pixels.

![image: three-panel character sheet example](https://pyrite-mallow-3b0.notion.site/image/attachment%3A64c6f66d-c4c4-40aa-b71a-c898e06ea2d4%3Ahf_20260712_173217_1c8706fc-9ab9-4e6a-a86f-e01158b3ad11.png)

The 6-panel still exists in the skill if you want it. It just won't get offered anymore, and if you ask for it, the skill tells you what you're giving up first.

#### "Wait — where'd the head go?"

Yeah. That's the point.

When you're pulling a character reference into a video prompt, you want the model looking at one face, at maximum size, with nothing to argue with. A full-body panel with a tiny head in it gives the model a second, worse copy of the face to average against. Cut the head off the body panel and the only face in the sheet is the one in the close-up. Drift drops.

The skill picks the cut for you based on what the character's wearing:

- Ghost mannequin — for structured necklines. Tees, tanks, collars, hoods, keyholes. The collar holds its own shape and the opening reads as an empty hollow looking down into the shirt. Like an invisible person is wearing it.
- Clean neck cut — for dresses, halters, strapless, spaghetti straps, plunging necklines. Nothing to hollow out, so the neck terminates in a flat sculptural edge like a dress-form mannequin.

Both ship with the same suppression stack — no fade, no blur, no ghosting, no gore, no stump. Clean. And the hair goes with the head.

---

## Cinema Worldbuilder got tighter, not bigger

The prompt box is not linear. More detail isn't automatically better. It's a bell curve, and the job is finding the top of it.

Past a certain density the model starts dropping things — and worse, you lose the ability to tell which thing you lost. So CWB 3.0 cut fat and added control where control actually pays:

- Frame Map anchors screen position before identity ever enters. Left third, right third, x%, depth layer, what's foreground, what's negative space. The model can't drift a character to the wrong side of the frame if the frame is locked first.
- FOV in degrees, not just millimeters. Seedance treats degrees as a discrete snap value and treats millimeters as a suggestion. 47° (50mm) holds. 50mm drifts.
- Write the visible. Every abstraction gets converted to something the model can physically render. Not "she looks stressed" — "shoulders lift, jaw locks, exhales through the nose." Not "fast" — km/h. Not "hazy" — % density and meter visibility.
- Element tags instead of image numbers. @sol_ref, @berlin_plate. Name them for what they are.

And when you're 14 iterations deep and it's gotten worse instead of better: reset the prompt. Ask your LLM to strip it back to basics. Let it breathe. Add back only what's necessary. Stacking fixes on top of fixes is how you end up with a prompt that's fighting itself.

### Story Bible Builder — the new one

The problem it solves: you've got 30 memory slots and a world that needs 300. So you spend every conversation re-explaining who Sol is, how Zara moves, what the bunker looks like, why NULL exists.

The bible builder interviews you — premise, timeline, factions, locations, characters with voice and movement locks, ensemble dynamics, plot engines, production rules — and outputs a SKILL.md you install. After that, every image prompt, every video prompt, every lyric, every line of dialogue already knows your world. No memory tax. No re-explaining.

This is the one I'd install first if I were starting over.

---

### Real talk, again

You'll still regenerate. Just less. The skills move you from 8–10 takes per shot down to 2–3 to pick from. Different problem. Cheaper problem. Not zero.

Consistency is still the hardest thing in this medium. Locked reference sheets help. Separating identity from styling helps. Killing the head in the body panel helps. You will still get drift on long sequences. The fix is more reference passes and tighter locks — there's no prompt that solves it for you.

Hit rate scales with prep. Every shot that worked first try had locked references, locked wardrobe, and a locked environment plate before the video prompt ever ran. Every shot that took six tries was one where I skipped a step. Every single time. The pipeline is what makes the prompt cheap.

These encode my taste. Not yours. Fork them. Break them. Make them yours. They're a starting point, not a final answer.

---

### The sample prompts

Straight from this week's pipeline. Read them once. Then read them again paying attention to what's not there — no fixture names, no character names, no lyric references, no aspect ratios. The model doesn't render those. It renders the behavior behind them, so the skill writes the behavior directly.

---

![image: rendered sample output](https://pyrite-mallow-3b0.notion.site/image/attachment%3A49aa8334-1018-4383-9278-46168a65602f%3Ahf_20260712_173422_b4f8d0fa-71bb-4190-a690-d5c4bee40a69.png)

```
A three-panel character reference sheet composed as one horizontal frame, divided into three equal vertical panels side by side, thin clean separation between panels, the same figure and the same outfit rendered identically across all three.

The figure is a slim woman with warm fair skin and natural warmth, dark brown-black hair swept up into a high messy topknot with loose wispy strands falling around the face and temples. Soft neutral makeup, groomed brows, muted nude lip, model face-card neutral expression, lips closed. Short nails painted a deep red.

She wears a translucent transparent PVC rain coat in a warm amber-brown tint — glossy, wet-looking vinyl with visible crinkle and fold creases, worn open, knee-length, with a soft crushed hood, snap-button placket, curved patch pockets, and fuchsia-pink piping trim running along every edge, the hood, the placket, the pockets, and the cuffs. The coat is fully see-through, so everything beneath it and the backdrop behind it read clearly through the amber tint. Beneath it, a black ribbed knit cropped top with a keyhole split at the round neckline, long sleeves, cropped high to expose the midriff and navel, and a short black leather mini skirt sitting low on the hips with a visible center seam. Black leather knee-high stiletto boots with pointed toes. Several chunky silver rings stacked across the fingers of both hands.

LEFT PANEL — full body front view, no head and no neck. The body stands squared to camera from the shoulders down to the boots, arms relaxed at the sides, hands open and loose, weight even across both feet. There is no head and no neck at all — nothing rises above the shoulder line. The round keyhole neckline of the black ribbed top holds its own shape at the top of the garment and its opening is an empty dark hollow looking down into the inside of the knit, with the inner back of the fabric faintly visible inside the opening. The soft PVC hood sits collapsed and empty behind the shoulders, holding its own crushed shape with nothing inside it. The garments read as if worn by an invisible body — full three-dimensional shape, natural drape, real fabric and vinyl tension across the chest and shoulders, but nothing emerging from the neckline. No stump, no skin, no cut edge, no anatomy, no blood, no fade, no blur, no ghosting, no transparency in the body. The panel keeps full headroom, generous empty mid-gray backdrop above the shoulders, so the figure sits at the same scale and position in the frame as a normal full-body portrait.

CENTER PANEL — full body rear view, head attached. The same figure photographed from directly behind, standing straight, the messy topknot and loose strands visible at the back of the head, the empty crushed PVC hood hanging against the upper back, the transparent amber coat falling open down the back with its fuchsia piping tracing the hem and cuffs, the black ribbed top and low black leather mini skirt visible through the translucent vinyl, arms relaxed at the sides, hands loose, weight even across both feet, from the top of the head down to the boots.

RIGHT PANEL — chest-up front portrait, identity lock. The same figure framed from the top of the topknot down to the upper chest, face filling most of the panel, body squared to camera, head level, eyes directly to camera, lips closed and relaxed, neutral controlled expression. The loose wispy strands, the collar of the transparent amber PVC coat with its fuchsia piping, and the keyhole neckline of the black ribbed top all clearly readable.

Mid-gray seamless studio backdrop applied uniformly across all three panels — even neutral mid-gray, no seam line, no gradient, no falloff to black or white. Relight from scratch overriding any reference lighting: one broad diffused source from camera-left and slightly above in every panel, gentle wrap onto the figure, no harsh shadows, no rim light, no hair light, no kicker, only the gentlest lifted shadow on the off-light side. Skin reads matte and velvety in a low-contrast milky look, no shine, no oily T-zone, while the PVC coat and the leather skirt and boots hold their own natural surface sheen — soft rolling specular highlights across the vinyl creases and the leather grain, never blown out, never hard glare. Skin renders at its true natural warm fair tone, identical in value and hue across the face, midriff, legs, and hands in every panel, never darkened, never tanned, never pale or washed-out or cool-shifted by the background. The coat renders at its true warm amber-brown translucency with true fuchsia-pink piping, the knit and leather at true black, consistent across all three panels. Real peach fuzz at the jaw and hairline, real fine even pore texture, subsurface scattering reading as semi-translucent biology, real ribbed knit texture, real leather grain, real vinyl crinkle and fold structure with true see-through transparency, visible fine metal surface detail on the silver rings, never plastic-looking skin, never waxy, never harsh. Photographed on a 50mm prime at a wide aperture, natural round bokeh, even sharpness, soft natural film grain. Photographed not generated.
```

---

### Housekeeping

The outfit builder skill is in the oven. KY's been dialing it in and it's going to make wardrobe work slot straight into the other three. Coming soon.

I'll keep updating these as I learn. When the next version drops it'll be posted the same way — free, here, with the prompts.

And lastly, thank you. Genuinely from the bottom of my heart. Twenty-five thousand of you. We started this a couple months ago and I still don't fully believe it.

If you can dream it, you can prompt it.

Peace, love, and AI.
