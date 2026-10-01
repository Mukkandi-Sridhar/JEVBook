"""Black-and-white tests: python3 tools/bw_test.py figures OUTDIR | pages BOOK.pdf OUTDIR

Two versions of every image: greyscale (luma, as a black-and-white printer sees it), and a harsh "photocopy"
(greyscale, contrast stretched 1.6x around mid-grey, then a slight blur). `figures` makes contact sheets of every
figure the book uses, each shown in colour, greyscale and photocopy, for inspection. `pages` makes contact sheets
of every page of a PDF in the photocopy version (add --grey for greyscale sheets too), plus one overview sheet of
the whole book, for release/v1.0/checks/.
"""
from __future__ import annotations

import re
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FONT = ROOT / "assets" / "fonts" / "Inter-Regular.ttf"


def grey(im: Image.Image) -> Image.Image:
    return im.convert("RGB").convert("L")          # ITU-R 601 luma, the usual printer conversion


def photocopy(im: Image.Image, blur: float = 0.7) -> Image.Image:
    g = np.asarray(grey(im), dtype=float) / 255
    g = np.clip((g - 0.55) * 1.6 + 0.55, 0, 1)
    return Image.fromarray((g * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(blur))


def used_figures() -> list[Path]:
    seen, out = set(), []
    for q in sorted(ROOT.glob("**/*.qmd")):
        if "_book" in q.parts or "labs" in q.parts:
            continue
        for m in re.finditer(r"\]\((/?figures/[^)]+?\.pdf)\)", q.read_text()):
            p = ROOT / m.group(1).lstrip("/")
            if p not in seen and p.exists():
                seen.add(p)
                out.append(p)
    return out


def raster(pdf: Path, dpi: int, page: int | None = None) -> list[Image.Image]:
    with tempfile.TemporaryDirectory() as d:
        args = ["pdftoppm", "-r", str(dpi), "-png"]
        if page:
            args += ["-f", str(page), "-l", str(page)]
        subprocess.run(args + [str(pdf), f"{d}/p"], check=True)
        return [Image.open(f).convert("RGB") for f in sorted(Path(d).glob("p*.png"))]


def sheet(tiles: list[tuple[str, Image.Image]], cols: int, cell_w: int, out: Path, title: str):
    font = ImageFont.truetype(str(FONT), 18)
    small = ImageFont.truetype(str(FONT), 13)
    rows = [tiles[i:i + cols] for i in range(0, len(tiles), cols)]
    heights = [max(t.height * cell_w // t.width for _, t in r) + 24 for r in rows]
    W, H = cols * (cell_w + 12) + 12, sum(heights) + 50
    s = Image.new("L", (W, H), 255)
    dr = ImageDraw.Draw(s)
    dr.text((12, 12), title, fill=0, font=font)
    y = 46
    for r, h in zip(rows, heights):
        for i, (name, t) in enumerate(r):
            t = t.resize((cell_w, t.height * cell_w // t.width), Image.LANCZOS)
            x = 12 + i * (cell_w + 12)
            s.paste(t.convert("L"), (x, y + 18))
            dr.rectangle([x - 1, y + 17, x + t.width, y + 18 + t.height], outline=170)
            dr.text((x, y), name, fill=60, font=small)
        y += h
    s.save(out, optimize=True)


def figures(outdir: Path):
    outdir.mkdir(parents=True, exist_ok=True)
    figs = used_figures()
    per = 6
    for k in range(0, len(figs), per):
        tiles = []
        for p in figs[k:k + per]:
            im = raster(p, 110)[0]
            both = Image.new("RGB", (im.width * 2 + 10, im.height), "white")
            both.paste(grey(im).convert("RGB"), (0, 0))
            both.paste(photocopy(im).convert("RGB"), (im.width + 10, 0))
            tiles.append((f"{p.parent.name}/{p.stem}   (left: greyscale, right: photocopy)", both))
        sheet(tiles, 2, 1100, outdir / f"figures-{k // per + 1:02d}.png", f"Figures {k + 1}-{k + len(tiles)} of {len(figs)}")
    print(f"{len(figs)} figures -> {outdir}")


def pages(pdf: Path, outdir: Path, per_sheet: int = 32, dpi: int = 40, with_grey: bool = False):
    outdir.mkdir(parents=True, exist_ok=True)
    ims = raster(pdf, dpi)
    kinds = (("photocopy", photocopy), ("greyscale", grey)) if with_grey else (("photocopy", photocopy),)
    for kind, fn in kinds:
        for k in range(0, len(ims), per_sheet):
            tiles = [(f"p. {k + i + 1}", fn(im)) for i, im in enumerate(ims[k:k + per_sheet])]
            sheet(tiles, 8, 230, outdir / f"{kind}-pages-{k + 1:03d}-{k + len(tiles):03d}.png",
                  f"{kind.capitalize()} test: {pdf.name}, pages {k + 1}-{k + len(tiles)} of {len(ims)}")
    # one overview of the whole book in the photocopy version, small enough to send around
    tiles = [(f"{i + 1}", photocopy(im)) for i, im in enumerate(ims)]
    sheet(tiles, 18, 110, outdir / "photocopy-contact-sheet.png",
          f"Photocopy test, every page of {pdf.name} ({len(ims)} pages): greyscale, contrast x1.6, slight blur")
    print(f"{len(ims)} pages -> {outdir}")


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "figures":
        figures(Path(sys.argv[2]))
    else:
        pages(Path(sys.argv[2]), Path(sys.argv[3]), with_grey="--grey" in sys.argv)
