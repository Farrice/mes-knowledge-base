#!/usr/bin/env node
// Poster frame: npm run still -- --manifest manifests/jcked-hookB.json
import { parseArgs } from "node:util";
import { mkdtempSync, writeFileSync } from "node:fs";
import { dirname, join, resolve, isAbsolute } from "node:path";
import { fileURLToPath } from "node:url";
import { tmpdir } from "node:os";
import { spawnSync } from "node:child_process";
import { resolveManifest, resolveManifestPath, reportMissing } from "./resolve-manifest.mjs";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");

// Fixed at 30 across the whole pipeline (see src/Ad.tsx FPS). Duplicated
// here because this is a plain Node script, not a TS import from Ad.tsx.
const FPS = 30;

const { values } = parseArgs({
  options: {
    manifest: { type: "string" },
    out: { type: "string" },
    frame: { type: "string" }, // absolute frame number; defaults into the end card
  },
});

if (!values.manifest) {
  console.error(
    "Usage: npm run still -- --manifest manifests/<file>.json [--out out/<name>-poster.png] [--frame 120]"
  );
  process.exit(1);
}

const manifestPath = resolveManifestPath(values.manifest, ROOT);
let manifest, missing;
try {
  ({ manifest, missing } = resolveManifest(manifestPath, ROOT));
} catch (err) {
  console.error(err.message);
  process.exit(1);
}
reportMissing(missing);

// Mirrors Ad.tsx's computeClipTimeline/computeEndCardStartFrame — keep in
// sync if that math changes. Only used to pick a sensible default poster
// frame (inside the end card, product visible); --frame always overrides it.
function endCardStartFrame(clips, crossfadeFrames) {
  let cursor = 0;
  clips.forEach((clip, i) => {
    const duration = Math.round(clip.targetDurationSeconds * FPS);
    const start = i === 0 ? 0 : cursor - crossfadeFrames;
    cursor = start + duration;
  });
  return cursor;
}

const defaultFrame =
  manifest.posterFrame ?? endCardStartFrame(manifest.clips, manifest.crossfadeFrames ?? 0) + 15;
const frame = values.frame ? parseInt(values.frame, 10) : defaultFrame;

const tmpDir = mkdtempSync(join(tmpdir(), "ad-pipeline-"));
const propsPath = join(tmpDir, "props.json");
writeFileSync(propsPath, JSON.stringify(manifest));

const outPath = values.out
  ? isAbsolute(values.out)
    ? values.out
    : join(ROOT, values.out)
  : join(ROOT, "out", `${manifest.adName}-poster.png`);

const args = [
  "remotion",
  "still",
  "src/index.ts",
  "Ad",
  outPath,
  `--props=${propsPath}`,
  `--frame=${frame}`,
];

console.log(`\n[still] ${manifest.adName} frame ${frame} -> ${outPath}\n`);

const result = spawnSync("npx", args, { cwd: ROOT, stdio: "inherit" });
process.exit(result.status ?? 1);
