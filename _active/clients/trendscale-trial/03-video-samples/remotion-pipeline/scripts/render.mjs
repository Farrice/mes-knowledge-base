#!/usr/bin/env node
// Hands-off render: npm run render -- --manifest manifests/jcked-hookB.json
import { parseArgs } from "node:util";
import { mkdtempSync, writeFileSync } from "node:fs";
import { dirname, join, resolve, isAbsolute } from "node:path";
import { fileURLToPath } from "node:url";
import { tmpdir } from "node:os";
import { spawnSync } from "node:child_process";
import { resolveManifest, resolveManifestPath, reportMissing } from "./resolve-manifest.mjs";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");

const { values } = parseArgs({
  options: {
    manifest: { type: "string" },
    out: { type: "string" },
    // Optional Remotion frame range for quick test renders, e.g. 0-299 (~10s @ 30fps).
    frames: { type: "string" },
  },
});

if (!values.manifest) {
  console.error(
    "Usage: npm run render -- --manifest manifests/<file>.json [--out out/<name>.mp4] [--frames 0-299]"
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

const tmpDir = mkdtempSync(join(tmpdir(), "ad-pipeline-"));
const propsPath = join(tmpDir, "props.json");
writeFileSync(propsPath, JSON.stringify(manifest));

const outPath = values.out
  ? isAbsolute(values.out)
    ? values.out
    : join(ROOT, values.out)
  : join(ROOT, "out", `${manifest.adName}.mp4`);

const args = ["remotion", "render", "src/index.ts", "Ad", outPath, `--props=${propsPath}`];
if (values.frames) args.push(`--frames=${values.frames}`);

console.log(
  `\n[render] ${manifest.adName} -> ${outPath}${values.frames ? ` (frames ${values.frames})` : ""}\n`
);

const result = spawnSync("npx", args, { cwd: ROOT, stdio: "inherit" });
process.exit(result.status ?? 1);
