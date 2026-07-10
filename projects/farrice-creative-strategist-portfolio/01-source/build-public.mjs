import { mkdir, readFile, rm, writeFile, cp } from "node:fs/promises";
import { join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL(".", import.meta.url)));
const dist = join(root, "dist");

await rm(dist, { recursive: true, force: true });
await mkdir(dist, { recursive: true });

let index = await readFile(join(root, "index.html"), "utf8");
index = index.replace(/\n\s*<script src="edit-mode\.js"><\/script>/, "");

await writeFile(join(dist, "index.html"), index);
await cp(join(root, "styles.css"), join(dist, "styles.css"));
await cp(join(root, "script.js"), join(dist, "script.js"));
await cp(join(root, "content-overrides.js"), join(dist, "content-overrides.js"));
await cp(join(root, "site-edits.json"), join(dist, "site-edits.json"));
await cp(join(root, "assets"), join(dist, "assets"), { recursive: true });

console.log(`Public site build ready: ${dist}`);
