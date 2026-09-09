#!/bin/zsh
set -euo pipefail

BATCH="/Users/farricecain/.Trash/storage-recovery-batch-001"

if [[ -e "$BATCH" ]]; then
  print -u2 "Refusing to reuse existing Trash batch: $BATCH"
  exit 2
fi

mkdir -p "$BATCH"

move_one() {
  local source="$1"
  local destination="$2"
  if [[ ! -e "$source" ]]; then
    print -u2 "Missing approved source: $source"
    exit 3
  fi
  if [[ -e "$destination" ]]; then
    print -u2 "Refusing to overwrite Trash destination: $destination"
    exit 4
  fi
  mv "$source" "$destination"
}

move_one "/Users/farricecain/Downloads/02_Design_Assets/Style Bender For Photoshop.zip" "$BATCH/style-bender-zip-extra"
move_one "/Users/farricecain/Downloads/02_Design_Assets/9592d114-2a17-4ebc-8d80-17c7a87043ab.zip" "$BATCH/kalypso-uuid-zip-extra"
move_one "/Users/farricecain/Downloads/Claude (1).dmg" "$BATCH/claude-installer-1-extra"
move_one "/Users/farricecain/Downloads/Claude (2).dmg" "$BATCH/claude-installer-2-extra"
move_one "/Users/farricecain/Downloads/02_Design_Assets/Templates/Style Bender Template For Photoshop-1696955105011/Style Bender For Photoshop 2/Style 1.psd" "$BATCH/style-bender-psd-1-extra"
move_one "/Users/farricecain/Downloads/02_Design_Assets/Templates/Style Bender Template For Photoshop-1696955105011/Style Bender For Photoshop 2/Style 2.psd" "$BATCH/style-bender-psd-2-extra"
move_one "/Users/farricecain/Downloads/02_Design_Assets/Templates/Style Bender Template For Photoshop-1696955105011/Style Bender For Photoshop 2/Style 3.psd" "$BATCH/style-bender-psd-3-extra"
move_one "/Users/farricecain/Downloads/02_Design_Assets/Mockups/Modelled-Oversized-T-Shirt-Mockup-By-Studio-Innate-2.1-o42fxj (1)" "$BATCH/modelled-oversized-tshirt-tree-extra"
move_one "/Users/farricecain/Downloads/02_Design_Assets/Mockups/closeup-texture-tshirt-mockup-with-color-changeable (1)" "$BATCH/closeup-tshirt-tree-extra"
move_one "/Users/farricecain/Downloads/02_Design_Assets/Mockups/editable-mockup-realist-printed-catton (1)" "$BATCH/printed-cotton-tree-extra"
move_one "/Users/farricecain/Downloads/02_Design_Assets/Mockups/editable-extreme-closeup-mockup-screen-printing-looks (1)" "$BATCH/screen-printing-closeup-tree-extra"

print "MOVED batch=storage-recovery-batch-001 items=11"
