// Render cover sources with Chromium (Playwright): real text shaping, every font weight, vector PDF.
// usage: node cover/render.mjs jobs.json
// jobs: [{src: "file.html", out: "file.png", type: "png", width: px, height: px}
//        {src: "file.html", out: "file.pdf", type: "pdf", width: "14.8in", height: "10.25in"}]
import { readFileSync } from "node:fs";
import { createRequire } from "node:module";
import { resolve } from "node:path";
const require = createRequire("/opt/node22/lib/node_modules/");
const { chromium } = require("playwright");

const jobs = JSON.parse(readFileSync(process.argv[2], "utf8"));
const browser = await chromium.launch();
for (const j of jobs) {
  const page = await browser.newPage(j.type === "png"
    ? { viewport: { width: j.width, height: j.height }, deviceScaleFactor: j.scale || 1 }
    : {});
  await page.goto("file://" + resolve(j.src));
  await page.evaluate(() => document.fonts.ready);
  if (j.type === "png") {
    await page.screenshot({ path: j.out, clip: { x: 0, y: 0, width: j.width, height: j.height } });
  } else {
    await page.pdf({ path: j.out, width: j.width, height: j.height, printBackground: true,
                     margin: { top: 0, right: 0, bottom: 0, left: 0 }, preferCSSPageSize: false });
  }
  await page.close();
  console.log("wrote", j.out);
}
await browser.close();
