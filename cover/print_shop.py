"""Cover files for a local print shop: python3 cover/print_shop.py  -> release/v1.0/print-shop/

Front and back as separate panels, 7 x 10 in trim plus 0.125 in bleed on every side (7.25 x 10.25 in), as a vector
PDF and a 300 dpi PNG; the spine on its own; and the full paperback wrap as a 300 dpi PNG.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from PIL import Image  # noqa: E402

from coverlib import PT, ROOT, Wrap, interior_pages, rect, strapline, svg_doc, to_pdf, to_png  # noqa: E402
from wrap import BG, PAPERBACK_PAPER, back, front, spine, wrap_svg  # noqa: E402

BLEED = 0.125
DPI = 300
OUT = ROOT / "release" / "v1.0" / "print-shop"


def panel(body: str, w_in: float, h_in: float) -> str:
    """A panel drawn at trim size, placed inside a page with bleed on all four sides; the ground runs to the edge."""
    b = BLEED * PT
    return svg_doc(w_in + 2 * BLEED, h_in + 2 * BLEED,
                   rect(0, 0, (w_in + 2 * BLEED) * PT, (h_in + 2 * BLEED) * PT, BG)
                   + f'\n<g transform="translate({b:.2f},{b:.2f})">{body}</g>')


def save(svg: str, stem: str, w_in: float, h_in: float, pdf=True):
    png = OUT / f"{stem}-300dpi.png"
    to_png(svg, png, round(w_in * DPI), round(h_in * DPI))
    Image.open(png).convert("RGB").save(png, dpi=(DPI, DPI), optimize=True)
    if pdf:
        to_pdf(svg, OUT / f"{stem}.pdf", w_in, h_in)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    wr = Wrap("paperback", pages=interior_pages(), paper=PAPERBACK_PAPER)
    W, H = 7.0, 10.0
    save(panel(front(W * PT, H * PT, strapline()), W, H), "front", W + 2 * BLEED, H + 2 * BLEED)
    save(panel(back(W * PT, H * PT, wr), W, H), "back", W + 2 * BLEED, H + 2 * BLEED)
    sw = round(wr.spine, 4)
    save(panel(spine(sw * PT, H * PT, wr), sw, H), "spine", sw + 2 * BLEED, H + 2 * BLEED)
    save(wrap_svg(wr, strapline()), "full-wrap-paperback", round(wr.width, 4), round(wr.height, 4), pdf=False)
    for f in sorted(OUT.iterdir()):
        print(f.name, f.stat().st_size // 1024, "KB")


if __name__ == "__main__":
    main()
