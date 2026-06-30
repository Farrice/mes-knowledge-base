import { createServer } from "node:http";
import { readFile, writeFile } from "node:fs/promises";
import { createReadStream } from "node:fs";
import { extname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { spawn } from "node:child_process";

const root = resolve(fileURLToPath(new URL(".", import.meta.url)));
const port = Number.parseInt(process.env.PORT || "8766", 10);
const host = process.env.HOST || "127.0.0.1";
const cmsToken = process.env.CMS_TOKEN || "";
const chromePath = process.env.CHROME_PATH || "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const pdfPath = join(root, "Farrice-Cain-Creative-Strategist-Portfolio.pdf");

const mimes = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".png": "image/png",
  ".webp": "image/webp",
  ".pdf": "application/pdf",
  ".svg": "image/svg+xml"
};

function safePath(urlPath) {
  const cleanPath = decodeURIComponent(urlPath.split("?")[0]);
  const requested = cleanPath === "/" ? "/index.html" : cleanPath;
  const fullPath = resolve(join(root, requested));
  if (!fullPath.startsWith(root)) return null;
  return fullPath;
}

async function readBody(request) {
  let body = "";
  for await (const chunk of request) {
    body += chunk;
    if (body.length > 1_000_000) throw new Error("Request body too large");
  }
  return body;
}

async function handleSave(request, response) {
  if (!isAuthorized(request, response)) return;

  try {
    const body = await readBody(request);
    const parsed = JSON.parse(body || "{}");
    await writeFile(join(root, "site-edits.json"), `${JSON.stringify(parsed, null, 2)}\n`);
    response.writeHead(200, { "Content-Type": "application/json" });
    response.end(JSON.stringify({ ok: true }));
  } catch (error) {
    response.writeHead(400, { "Content-Type": "application/json" });
    response.end(JSON.stringify({ ok: false, error: error.message }));
  }
}

function isAuthorized(request, response) {
  if (!cmsToken) return true;

  const header = request.headers.authorization || "";
  if (header === `Bearer ${cmsToken}`) return true;

  response.writeHead(401, { "Content-Type": "application/json" });
  response.end(JSON.stringify({ ok: false, error: "Unauthorized" }));
  return false;
}

function runChromePdf() {
  return new Promise((resolvePdf, rejectPdf) => {
    const url = `http://${host === "0.0.0.0" ? "127.0.0.1" : host}:${port}/`;
    const child = spawn(chromePath, [
      "--headless=new",
      "--disable-gpu",
      "--no-first-run",
      "--no-default-browser-check",
      "--run-all-compositor-stages-before-draw",
      "--virtual-time-budget=3000",
      "--print-to-pdf-no-header",
      `--print-to-pdf=${pdfPath}`,
      url
    ], { stdio: "ignore" });

    child.on("error", rejectPdf);
    child.on("close", (code) => {
      if (code === 0) resolvePdf();
      else rejectPdf(new Error(`Chrome PDF export exited with code ${code}`));
    });
  });
}

async function handleExportPdf(request, response) {
  if (!isAuthorized(request, response)) return;

  try {
    await runChromePdf();
    response.writeHead(200, { "Content-Type": "application/json" });
    response.end(JSON.stringify({
      ok: true,
      pdf: "Farrice-Cain-Creative-Strategist-Portfolio.pdf"
    }));
  } catch (error) {
    response.writeHead(500, { "Content-Type": "application/json" });
    response.end(JSON.stringify({ ok: false, error: error.message }));
  }
}

const server = createServer(async (request, response) => {
  if (request.method === "POST" && request.url === "/save-edits") {
    await handleSave(request, response);
    return;
  }

  if (request.method === "POST" && request.url === "/export-pdf") {
    await handleExportPdf(request, response);
    return;
  }

  const fullPath = safePath(request.url || "/");
  if (!fullPath) {
    response.writeHead(403);
    response.end("Forbidden");
    return;
  }

  try {
    await readFile(fullPath);
    response.writeHead(200, {
      "Content-Type": mimes[extname(fullPath)] || "application/octet-stream",
      "Cache-Control": "no-store"
    });
    createReadStream(fullPath).pipe(response);
  } catch (_error) {
    response.writeHead(404);
    response.end("Not found");
  }
});

server.listen(port, host, () => {
  console.log(`Portfolio editor running at http://${host === "0.0.0.0" ? "127.0.0.1" : host}:${port}/editor.html`);
  if (cmsToken) console.log("CMS write endpoints require Authorization: Bearer <CMS_TOKEN>");
});
