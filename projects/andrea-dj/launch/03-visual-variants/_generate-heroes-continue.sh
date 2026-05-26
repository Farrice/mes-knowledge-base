#!/usr/bin/env bash
# Continue: generate remaining 7 posters (B2-B4, C1-C4) with 70s sleep between calls.
set -uo pipefail

PROJECT_ROOT="/Users/farricecain/Google Antigravity"
SKILL_DIR="$PROJECT_ROOT/skills/fantastic-posters"
TARGET_DIR="$PROJECT_ROOT/projects/andrea-dj/launch/03-visual-variants"
GUARD="$PROJECT_ROOT/execution/fal_budget_guard.py"
LOG_FILE="$TARGET_DIR/_generation-log.txt"

export FAL_KEY="$(grep -E '^FAL_KEY=' "$PROJECT_ROOT/.env" | head -1 | cut -d= -f2-)"

PALETTE_B="#B8492E,#4A6B3F,#8C6526,#F5EFE3"
PALETTE_C="#1A1814,#7A9B6F,#8C6526,#FBF7F0"

gen_one() {
  local label="$1"; local size="$2"; local palette="$3"; local target_subdir="$4"; local brief="$5"
  echo "=========================================" | tee -a "$LOG_FILE"
  echo "[$label] $(date -u +'%H:%M:%SZ')" | tee -a "$LOG_FILE"

  if ! python3 "$GUARD" check --mode=poster --quality=medium --n=1 >>"$LOG_FILE" 2>&1; then
    echo "[$label] BUDGET GUARD BLOCK — sleeping 90s and retrying once" | tee -a "$LOG_FILE"
    sleep 90
    if ! python3 "$GUARD" check --mode=poster --quality=medium --n=1 >>"$LOG_FILE" 2>&1; then
      echo "[$label] STILL BLOCKED — skipping" | tee -a "$LOG_FILE"; return 1
    fi
  fi

  cd "$SKILL_DIR"
  local before=$(ls -t out/*.png 2>/dev/null | head -1 || echo "")
  if node generate.js "$brief" --style=editorial-fashion --palette="$palette" --size="$size" --quality=medium --n=1 --yes >> "$LOG_FILE" 2>&1 < /dev/null; then
    local newest=$(ls -t out/*.png 2>/dev/null | head -1)
    if [[ -n "$newest" && "$newest" != "$before" ]]; then
      cp "$newest" "$TARGET_DIR/$target_subdir/${label}.png"
      echo "[$label] OK -> $target_subdir/${label}.png" | tee -a "$LOG_FILE"
      python3 "$GUARD" log --mode=poster --quality=medium --n=1 --status=success --actual-cost=0.14 --output-path="$TARGET_DIR/$target_subdir/${label}.png" >> "$LOG_FILE" 2>&1 || true
    fi
  else
    echo "[$label] GEN FAILED" | tee -a "$LOG_FILE"
    python3 "$GUARD" log --mode=poster --quality=medium --n=1 --status=failed --actual-cost=0 >> "$LOG_FILE" 2>&1 || true
  fi
  sleep 70  # Stay under 5 calls / 5 min (effective rate: ~4/min)
}

gen_one "B2-body-in-room" "1024x1536" "$PALETTE_B" "variant-b-hero-shots" \
"Full-bleed architectural documentary photograph of a single body dancing in a Chicago converted-loft at 2pm, photographed wide so body occupies central third and room is the second protagonist. Behind body: terracotta brick wall. Left: deep-moss-green ceramic plant. Right: south-facing window with natural daylight cutting across wood floor. Body age 30-40, natural-range ethnicity and gender. Photographed three-quarter back, face not the subject. Real motion blur. Architectural composition on 12-column grid. Documentary photography, warm Latin-American daylight. Magazine masthead in modern editorial serif: RESONANCE. Subtitle: LA MÚSICA HACE EL TRABAJO EMOCIONAL · DAYTIME · CHICAGO. Cover line: \"THE ROOM I CAME TO CHICAGO LOOKING FOR\". Bottom right: JULIO 2026. No kitsch-Latin, no marigold, no posed."

gen_one "B3-tile-brick-corner" "1536x1024" "$PALETTE_B" "variant-b-hero-shots" \
"Full-bleed architectural still-life documentary photograph — deep-moss-green ceramic tile on one wall, terracotta brick on perpendicular wall, warm hardwood floor below, south-facing window casting natural daylight across both walls at 2pm. No people. Architectural study, strict 12-column grid composition. Documentary photography, warm yellow-undertone of Latin-American daylight. Editorial masthead in modern serif: RESONANCE. Subtitle: A ROOM BUILT FOR ADULTS LOOKING FOR A PARTNER · CHICAGO. Cover lines: \"DAYTIME · SOBER · CURATED · BODY-FIRST · JULY 2026\". Tracked-caps footer: HEART ENCOUNTERS · NOT HEAD ENCOUNTERS. No kitsch-Latin, no Aztec, no woven texture, no club."

gen_one "B4-group-architectural" "1536x1024" "$PALETTE_B" "variant-b-hero-shots" \
"Full-bleed documentary photograph of a group of adults aged 30-40 dancing in Chicago converted-loft at 2pm, entirely from behind — backs and raised forearms — room as second protagonist: terracotta brick wall behind, deep-moss-green plant in corner of frame, south-facing window light cutting across wood floor. Mixed body types, mixed gender presentation, mixed ethnicity visible from back. Real motion, slight blur. Architectural composition on 12-column grid. Documentary photography, warm Latin-American daylight color temperature. Editorial masthead in modern serif: RESONANCE. Subtitle: COUPLES FORMED · NOT FOLLOWERS · CHICAGO. Cover line: \"EL CUARTO QUE EL ORQUESTA NACIONAL ME ENSEÑÓ\". Bottom right tracked: JULIO 2026. No faces visible (all from behind). No kitsch-Latin, no posed, no alcohol."

gen_one "C1-empty-cream-room" "1024x1536" "$PALETTE_C" "variant-c-hero-shots" \
"Full-bleed intimate-essayistic documentary photograph of an empty Chicago apartment room at 2pm — cool-cream walls, light hardwood floor, single sage-green ceramic plant pot with small olive plant in deep-left corner, slim ray of natural daylight from north-facing window cutting across floor at right. No people. The room itself is the subject. Documentary photography, minimal color grading, slight blue-undertone of overcast Chicago daylight. Cleared cream-and-light fills most of frame. Restrained magazine masthead in light modern serif at top: RESONANCE. Subtitle in small tracked caps: A QUIET ROOM IN DAYLIGHT · CHICAGO. Cover line in italic light serif: \"the room that trusts you to read it\". Footer: JULY 2026. No quiet-luxury cliché, no marble, no champagne, no cashmere, no warm-orange tones."

gen_one "C2-hand-resting-fader" "1024x1536" "$PALETTE_C" "variant-c-hero-shots" \
"Full-bleed intimate-essayistic documentary photograph — tight crop on hand and lower forearm resting on a vintage DJ fader at 2pm in a Chicago apartment. Real natural daylight from north-facing window. Light wood booth, cool-cream wall in very soft out-of-focus background. Hand still, fingers resting — caught between gestures, not mid-gesture. Documentary photography, minimal color grading, slight blue-undertone of overcast Chicago daylight. Generous negative space above. Restrained masthead in light modern serif at top: RESONANCE. Subtitle in small tracked caps: THE MUSIC DOES THE EMOTIONAL LABOR. Cover line italic light serif: \"by the time you speak, your body has already made the introductions\". Footer: CHICAGO · JULY 2026. No warm-orange tones, no luxury cliché."

gen_one "C3-two-shoulders" "1024x1536" "$PALETTE_C" "variant-c-hero-shots" \
"Full-bleed intimate-essayistic documentary photograph of two adults aged 30-40 standing near each other in a Chicago apartment at 2pm, photographed from waist up, from the side. Shoulders almost touching but not yet. Real natural daylight from north-facing window. Cool-cream wall behind. Both bodies from side-back angle, faces obscured. Mixed body types and gender. Documentary photography, generous negative space above shoulders, body-detail in lower two-thirds. Slight blue-undertone of overcast Chicago daylight. Restrained masthead in light modern serif: RESONANCE. Subtitle small tracked caps: SHOULDERS BEFORE WORDS. Cover line italic light serif: \"a daytime room for people who want to meet someone\". Footer: CHICAGO · JULY 2026. Faces obscured. No romantic-cliché, no warm-orange."

gen_one "C4-side-of-face" "1024x1024" "$PALETTE_C" "variant-c-hero-shots" \
"Full-bleed intimate-essayistic documentary photograph of the side of a single adult's face — ear, jawline, suggestion of an eye looking off-frame — listening intently to something out of frame, at 2pm in a Chicago apartment. Real natural daylight from north-facing window. Cool-cream wall behind, very soft focus. Face in profile, partially obscured by hair or shoulder, age 30-40, natural-range ethnicity. Documentary photography, generous negative space, body-detail in right third, cleared cream-and-light in left two-thirds. Slight blue-undertone of overcast Chicago daylight. Restrained masthead in light modern serif: RESONANCE. Subtitle small tracked caps: HEART ENCOUNTERS · NOT HEAD ENCOUNTERS. Footer: CHICAGO · JULY 2026. Profile face only, mostly obscured. No warm-orange, no posed."

echo "=========================================" | tee -a "$LOG_FILE"
echo "Continue complete — $(date -u +'%Y-%m-%dT%H:%M:%SZ')" | tee -a "$LOG_FILE"
ls -la "$TARGET_DIR/variant-b-hero-shots" "$TARGET_DIR/variant-c-hero-shots" | tee -a "$LOG_FILE"
python3 "$GUARD" status 2>&1 | tee -a "$LOG_FILE"
