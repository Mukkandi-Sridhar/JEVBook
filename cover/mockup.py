"""Marketing images: a 3D mockup of the paperback at an angle, and a square 1080 x 1080 post.

python cover/mockup.py  (after cover/wrap.py, which writes cover/src/front.png)
"""
from __future__ import annotations

import base64
import io
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, str(Path(__file__).parent))
from coverlib import C, COVER, PT, Wrap, interior_pages, rect, svg_doc, text, to_png  # noqa: E402
from wrap import BG, HOOK, spine  # noqa: E402


POST_BG = "#2A3346"      # a lighter slate than the cover, so the book stands off it


def perspective_coeffs(src, dst):
    """Coefficients for PIL's PERSPECTIVE transform that map the dst quad back onto the src quad."""
    a = []
    for (x, y), (u, v) in zip(dst, src):
        a.append([x, y, 1, 0, 0, 0, -u * x, -u * y])
        a.append([0, 0, 0, x, y, 1, -v * x, -v * y])
    b = np.array([c for pt in src for c in pt], dtype=float)
    return np.linalg.solve(np.array(a, dtype=float), b).tolist()


def warp(img, quad, size):
    w, h = img.size
    co = perspective_coeffs([(0, 0), (w, 0), (w, h), (0, h)], quad)
    out = img.convert("RGBA").transform(size, Image.PERSPECTIVE, co, Image.BICUBIC)
    mask = Image.new("L", size, 0)
    ImageDraw.Draw(mask).polygon(quad, fill=255)
    out.putalpha(mask)
    return out


def shade(img, factor):
    arr = np.asarray(img.convert("RGB"), dtype=float) * factor
    return Image.fromarray(arr.clip(0, 255).astype("uint8"))


def book_3d(front_png: Path, spine_png: Path, size=(2000, 1400), bg=("#EEF0F3", "#D9DEE5"),
            shadows=("#8C94A0", "#6B7380")):
    W, H = size
    canvas = Image.new("RGB", size, bg[0])
    grad = Image.linear_gradient("L").resize(size)
    canvas = Image.composite(Image.new("RGB", size, bg[1]), canvas, grad)
    front = Image.open(front_png).convert("RGB")
    sp = shade(Image.open(spine_png), 0.78)
    # the book, seen from a little to the left: the right edge recedes, the spine shows
    fx0, fx1 = W * 0.39, W * 0.70
    top0, bot0 = H * 0.10, H * 0.90                      # near (spine) edge
    top1, bot1 = H * 0.14, H * 0.86                      # far edge, shorter
    sx0 = fx0 - W * 0.042
    front_q = [(fx0, top0), (fx1, top1), (fx1, bot1), (fx0, bot0)]
    spine_q = [(sx0, top0 - H * 0.012), (fx0, top0), (fx0, bot0), (sx0, bot0 + H * 0.012)]
    # soft shadow on the ground
    sh = Image.new("L", size, 0)
    ImageDraw.Draw(sh).polygon([(sx0 + 30, bot0 + 10), (fx1 + 60, bot1 + 30), (fx1 + 140, bot1 + 60),
                                (sx0 + 60, bot0 + 50)], fill=150)
    sh = sh.filter(ImageFilter.GaussianBlur(40))
    canvas = Image.composite(Image.new("RGB", size, shadows[0]), canvas, sh)
    lift = Image.new("L", size, 0)
    ImageDraw.Draw(lift).polygon(front_q, fill=90)
    lift = lift.filter(ImageFilter.GaussianBlur(28))
    canvas = Image.composite(Image.new("RGB", size, shadows[1]), canvas, lift)
    canvas = canvas.convert("RGBA")
    canvas.alpha_composite(warp(sp, spine_q, size))
    fr = warp(front, front_q, size)
    # a gentle light falling from the left across the front
    light = Image.linear_gradient("L").rotate(90, expand=True).resize(size).point(lambda v: int(v * 0.16))
    dark = Image.new("RGBA", size, (0, 0, 0, 0))
    dark.putalpha(Image.composite(light, Image.new("L", size, 0), fr.getchannel("A")))
    canvas.alpha_composite(fr)
    canvas.alpha_composite(dark)
    # a thin highlight where the front meets the spine
    ImageDraw.Draw(canvas).line([(fx0, top0), (fx0, bot0)], fill=(255, 255, 255, 28), width=2)
    return canvas.convert("RGB")


def main():
    front_png = COVER / "src" / "front.png"
    wr = Wrap("paperback", pages=interior_pages())
    sw = wr.spine * PT
    svg = svg_doc(round(wr.spine, 4), 10, spine(sw, 10 * PT, wr))
    spine_png = COVER / "src" / "spine.png"
    to_png(svg, spine_png, max(8, round(2000 * wr.spine / 10)), 2000)
    mock = book_3d(front_png, spine_png)
    mock.save(COVER / "marketing" / "mockup-3d.png", optimize=True)
    # the square post: the hook on top, the book below, on the cover's own dark ground
    small = book_3d(front_png, spine_png, size=(1600, 1120), bg=(POST_BG, POST_BG), shadows=("#0B0E14", "#111520"))
    buf = io.BytesIO()
    small.save(buf, "PNG")
    uri = "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()
    S = 7.5 * PT                                          # a 7.5 in square, rendered at 1080 px
    parts = [rect(0, 0, S, S, POST_BG),
             f'<image href="{uri}" x="{S * 0.03:.1f}" y="{S * 0.26:.1f}" width="{S * 0.94:.1f}" '
             f'height="{S * 0.94 * 1120 / 1600:.1f}"/>']
    hs = S * 0.058
    parts.append(text(S * 0.07, S * 0.12, HOOK[0], hs, C["text_on_dark"], weight=800, ls=-0.01 * hs))
    parts.append(text(S * 0.07, S * 0.12 + hs * 1.2, HOOK[1].split("It")[0], hs, C["text_on_dark"], weight=800,
                      ls=-0.01 * hs))
    from coverlib import measure
    x2 = S * 0.07 + measure(HOOK[1].split("It")[0], hs, "Inter", 800, ls=-0.01 * hs)
    parts.append(text(x2, S * 0.12 + hs * 1.2, "It" + HOOK[1].split("It", 1)[1], hs, C["jev_on_dark"], weight=800,
                      ls=-0.01 * hs))
    to_png(svg_doc(7.5, 7.5, "\n".join(parts)), COVER / "marketing" / "post-square-1080.png", 1080, 1080)
    print("mockups written")


if __name__ == "__main__":
    main()
