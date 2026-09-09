#!/bin/bash
# One approved Gemini Deep Research pass for the Jen Engine v2 retool (2026-09-02). Output lands next to this file.
cd "$(dirname "$0")/../../../.." || exit 1
OUT="_active/clients/jen-listings/06-system/2026-09-02-deep-research-what-works-valley-agents.md"
python3 execution/research.py \
  "What Instagram content is actually generating buyer and seller leads for residential real estate agents in Los Angeles and the San Fernando Valley in 2026, for a solo agent serving buyers and sellers in the 800K to 1.2M dollar band: (1) named local agent accounts (Sherman Oaks, Studio City, Woodland Hills, Van Nuys, Encino, Burbank, Tarzana) with reels or carousels showing visible view or share counts, and the formats and hooks they use; (2) evidence on place-led positioning (city plus price band) versus buyer-type niches for agents who fear being pigeonholed; (3) share-driven local formats (local guides, send-this-to-a-future-X, neighborhood POV, what-X-dollars-buys) and whether they produce DMs from people with money and a timeline rather than just reach; (4) legibility and design conventions of the best-performing serif-over-photo agent posts; (5) what Coffee and Contracts members report actually working and how long it took. Cite real posts and numbers; label anything inferred." \
  --depth deep \
  --task-context "Jen Santulan, @_jiing, San Fernando Valley realtor. Retooling her content system after she rejected a line-drawing design system and a weekly voice memo. She wants her own full-bleed-photo white-serif look, will experiment with talking reels, wants buyers and sellers, no account access (she posts). The working thesis to test: the niche is the place plus price band, the Valley at 800K and up, not the buyer type." \
  > "$OUT" 2>&1
echo "research done: $OUT ($(wc -c < "$OUT") bytes)"
