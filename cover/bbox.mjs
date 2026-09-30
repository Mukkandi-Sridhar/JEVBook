// Measure laid-out boxes in a rendered cover SVG, in the SVG's own units (points).
// usage: node cover/bbox.mjs page.html "css selector"  -> JSON [{tag, cls, text, x, y, w, h}]
import { createRequire } from "node:module";
import { resolve } from "node:path";
const require = createRequire("/opt/node22/lib/node_modules/");
const { chromium } = require("playwright");

const [src, selector] = process.argv.slice(2);
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1600, height: 1200 } });
await page.goto("file://" + resolve(src));
await page.evaluate(() => document.fonts.ready);
const boxes = await page.evaluate((sel) => {
  const svg = document.querySelector("svg");
  const r0 = svg.getBoundingClientRect();
  const k = svg.viewBox.baseVal.width / r0.width;
  return [...document.querySelectorAll(sel)].map((el) => {
    const r = el.getBoundingClientRect();
    return { tag: el.tagName, cls: el.getAttribute("class") || "", text: el.textContent,
             x: (r.left - r0.left) * k, y: (r.top - r0.top) * k, w: r.width * k, h: r.height * k };
  });
}, selector);
console.log(JSON.stringify(boxes));
await browser.close();
