const { chromium } = require('playwright');
const path = require('path');

async function main() {
  const root = __dirname;
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({
    viewport: { width: 2200, height: 2100 },
    deviceScaleFactor: 1,
  });

  await page.goto(`file://${path.join(root, 'blind-bakeoff.html')}`, {
    waitUntil: 'networkidle',
  });
  await page.screenshot({
    path: path.join(root, 'blind-bakeoff.png'),
    fullPage: true,
  });
  await page.locator('#design-a-board').screenshot({
    path: path.join(root, 'design-a.png'),
  });
  await page.locator('#design-b-board').screenshot({
    path: path.join(root, 'design-b.png'),
  });
  await browser.close();
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
