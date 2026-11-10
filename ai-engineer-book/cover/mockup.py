"""A 3D mockup of the paperback from a rendered front cover. Run: python3 cover/mockup.py <front.png> <out.png>

The spine here is only for the picture (title and author on the cover's darkest colour); the print spine is built
with the wrap, from the final page count and paper.
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
FONT = str(ROOT / "assets" / "fonts" / "WorkSans-Bold.ttf")


def coeffs(src, dst):
    a = []
    for (x, y), (u, v) in zip(dst, src):
        a.append([x, y, 1, 0, 0, 0, -u * x, -u * y])
        a.append([0, 0, 0, x, y, 1, -v * x, -v * y])
    b = np.array([c for pt in src for c in pt], dtype=float)
    return np.linalg.solve(np.array(a, dtype=float), b).tolist()


def warp(img, quad, size):
    w, h = img.size
    out = img.convert("RGBA").transform(size, Image.PERSPECTIVE, coeffs([(0, 0), (w, 0), (w, h), (0, h)], quad),
                                        Image.BICUBIC)
    mask = Image.new("L", size, 0)
    ImageDraw.Draw(mask).polygon(quad, fill=255)
    out.putalpha(mask)
    return out


def spine_image(front, height=2400, width=150, ink="#FFFFFF", accent="#FFB23E"):
    """A picture of the spine: the cover's top-left colour, the title reading down, the author below it."""
    bg = front.resize((1, 1), Image.BOX, box=(0, 0, 40, 40)).getpixel((0, 0))
    strip = Image.new("RGB", (height, width), bg)                       # drawn lying down, then turned
    d = ImageDraw.Draw(strip)
    f1, f2 = ImageFont.truetype(FONT, 78), ImageFont.truetype(FONT, 40)
    d.text((150, width / 2), "SHIP REAL ", font=f1, fill=ink, anchor="lm")
    x = 150 + d.textlength("SHIP REAL ", font=f1)
    d.text((x, width / 2), "AI", font=f1, fill=accent, anchor="lm")
    d.text((height - 150, width / 2), "SRIDHAR MUKKANDI", font=f2, fill=ink, anchor="rm")
    return strip.rotate(-90, expand=True)


def mockup(front_png, out_png, bg=("#F3F1EC", "#D8D4CC"), ink="#FFFFFF", accent="#FFB23E"):
    W, H = 2000, 1500
    canvas = Image.new("RGB", (W, H), bg[0])
    canvas = Image.composite(Image.new("RGB", (W, H), bg[1]), canvas, Image.linear_gradient("L").resize((W, H)))
    front = Image.open(front_png).convert("RGB")
    front = front.crop((0, 35, front.width - 35, front.height - 35))     # trim the bleed
    sp = spine_image(front, ink=ink, accent=accent)
    sp = Image.fromarray((np.asarray(sp, dtype=float) * 0.72).clip(0, 255).astype("uint8"))
    x0, x1 = W * 0.36, W * 0.69                                          # front: near edge, far edge
    t0, b0, t1, b1 = H * 0.085, H * 0.915, H * 0.125, H * 0.875
    sx = x0 - W * 0.035                                                  # spine, turned away
    st, sb = H * 0.105, H * 0.895
    fq = [(x0, t0), (x1, t1), (x1, b1), (x0, b0)]
    sq = [(sx, st), (x0, t0), (x0, b0), (sx, sb)]
    shadow = Image.new("L", (W, H), 0)
    ImageDraw.Draw(shadow).polygon([(sx - 10, sb - 20), (x1 + 120, b1 + 25), (x1 + 40, b1 + 70), (sx + 30, sb + 55)], fill=150)
    ImageDraw.Draw(shadow).polygon([(sx + 40, st + 60), (x1 + 70, t1 + 60), (x1 + 70, b1 + 30), (sx + 40, sb + 20)], fill=90)
    shadow = shadow.filter(ImageFilter.GaussianBlur(38))
    canvas = Image.composite(Image.new("RGB", (W, H), "#3B3A36"), canvas, shadow)
    for img, quad in [(sp, sq), (front, fq)]:
        layer = warp(img, quad, (W, H))
        canvas.paste(layer, (0, 0), layer)
    gloss = Image.new("L", (W, H), 0)                                    # light falling across the front
    g = ImageDraw.Draw(gloss)
    g.polygon([(x0, t0), (x0 + (x1 - x0) * 0.42, t0 + (t1 - t0) * 0.42), (x0 + (x1 - x0) * 0.16, b0 - (b0 - b1) * 0.16),
               (x0, b0)], fill=26)
    canvas = Image.composite(Image.new("RGB", (W, H), "#FFFFFF"), canvas, gloss.filter(ImageFilter.GaussianBlur(60)))
    ImageDraw.Draw(canvas).line([(x0, t0), (x0, b0)], fill=(255, 255, 255), width=1)
    canvas.save(out_png)


if __name__ == "__main__":
    mockup(sys.argv[1], sys.argv[2])
