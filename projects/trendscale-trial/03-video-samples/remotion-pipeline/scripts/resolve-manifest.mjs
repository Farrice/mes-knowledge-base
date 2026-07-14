// Shared by render.mjs and still.mjs. This is the ONLY place fs touches a
// manifest — it stamps a `resolvedExists` flag onto every asset reference so
// the Remotion composition (src/Ad.tsx) can stay a pure function of props
// and behave identically in Studio preview and CLI render.
import { existsSync, readFileSync } from "node:fs";
import { join, isAbsolute } from "node:path";

export function resolveManifest(manifestPath, rootDir) {
  if (!existsSync(manifestPath)) {
    throw new Error(`Manifest not found: ${manifestPath}`);
  }
  const manifest = JSON.parse(readFileSync(manifestPath, "utf-8"));
  const assetsDir = join(rootDir, "assets");

  const resolveOne = (relPath) => {
    // Manifest paths read as "assets/clips/H3.mp4" (the folder-drop
    // convention) but our public dir IS assets/ itself — see
    // remotion.config.ts + Ad.tsx normalizeAssetPath().
    const stripped = relPath.replace(/^assets\//, "");
    return existsSync(join(assetsDir, stripped));
  };

  const missing = [];

  manifest.clips = (manifest.clips || []).map((clip) => {
    const exists = resolveOne(clip.path);
    if (!exists) missing.push(`clip  ${clip.id}: ${clip.path}`);
    return { ...clip, resolvedExists: exists };
  });

  manifest.overlays = (manifest.overlays || []).map((o, i) => {
    const exists = resolveOne(o.path);
    if (!exists) missing.push(`overlay[${i}]: ${o.path}`);
    return { ...o, resolvedExists: exists };
  });

  manifest.vo = (manifest.vo || []).map((v, i) => {
    const exists = resolveOne(v.path);
    if (!exists) missing.push(`vo[${i}]: ${v.path}`);
    return { ...v, resolvedExists: exists };
  });

  if (manifest.music) {
    const exists = resolveOne(manifest.music.path);
    if (!exists) missing.push(`music: ${manifest.music.path}`);
    manifest.music.resolvedExists = exists;
  }

  if (manifest.endCard) {
    const exists = resolveOne(manifest.endCard.productImage);
    if (!exists) missing.push(`end-card image: ${manifest.endCard.productImage}`);
    manifest.endCard.productImageExists = exists;
  }

  if (manifest.theme?.fontFilePath) {
    manifest.theme.fontFileExists = resolveOne(manifest.theme.fontFilePath);
  }

  return { manifest, missing };
}

export function resolveManifestPath(manifestArg, rootDir) {
  if (!manifestArg) return null;
  return isAbsolute(manifestArg) ? manifestArg : join(rootDir, manifestArg);
}

export function reportMissing(missing) {
  if (missing.length === 0) return;
  console.warn("\n[render] Missing assets — rendering with slates/silence for:");
  missing.forEach((m) => console.warn(`  - ${m}`));
  console.warn("(drop the real files in and re-render — no manifest changes needed)\n");
}
