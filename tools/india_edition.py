"""India print edition, with the RRRNA ISBN: python3 tools/india_edition.py [--spine-mm 13]

Writes release/v1.0/print-india/:
  interior-india-color.pdf, interior-india-bw.pdf   the release interiors with the India ISBN on the copyright page
  cover-india-<spine>mm.pdf (+ -guides.pdf)         the paperback cover with an EAN-13 ISBN barcode where Amazon
                                                    prints its own

This ISBN (978-93-345-4878-5, paperback, allotted by RRRNA on 8 Oct 2026) is for copies printed in India. Amazon's
paperback keeps its own KDP ISBN, which Amazon prints on its copies. The spine depends on the printer's paper, so
ask them for it (in mm, for 270 pages) and rerun with --spine-mm.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "cover"))
sys.path.insert(0, str(ROOT / "tools"))
from coverlib import AUTHOR, PAPER, PT, Wrap, exact_page, html_page, interior_pages, rect, render, strapline, svg_doc, text  # noqa: E402
from wrap import barcode_box, guides, wrap_svg  # noqa: E402
from local_print import overlay_pdf  # noqa: E402

ISBN = "978-93-345-4878-5"
OUT = ROOT / "release" / "v1.0" / "print-india"

# EAN-13: left-half digit patterns (L and G codes), chosen by the first digit; right half uses R codes.
L = ["0001101", "0011001", "0010011", "0111101", "0100011", "0110001", "0101111", "0111011", "0110111", "0001011"]
G = ["0100111", "0110011", "0011011", "0100001", "0011101", "0111001", "0000101", "0010001", "0001001", "0010111"]
R = ["1110010", "1100110", "1101100", "1000010", "1011100", "1001110", "1010000", "1000100", "1001000", "1110100"]
PARITY = ["LLLLLL", "LLGLGG", "LLGGLG", "LLGGGL", "LGLLGG", "LGGLLG", "LGGGLL", "LGLGLG", "LGLGGL", "LGGLGL"]


def check_digit(d12: str) -> int:
    return (10 - sum(int(c) * (3 if i % 2 else 1) for i, c in enumerate(d12)) % 10) % 10


def ean13_bits(digits: str) -> str:
    assert len(digits) == 13 and check_digit(digits[:12]) == int(digits[12]), "bad ISBN check digit"
    first, left, right = int(digits[0]), digits[1:7], digits[7:]
    bits = "101"
    for p, c in zip(PARITY[first], left):
        bits += (L if p == "L" else G)[int(c)]
    bits += "01010"
    for c in right:
        bits += R[int(c)]
    return bits + "101"


def barcode(x, y, bw, bh) -> str:
    """A white box with the ISBN above and an EAN-13 barcode (guard bars longer, digits below), sized to KDP's box."""
    digits = ISBN.replace("-", "")
    bits = ean13_bits(digits)                       # 95 modules
    mod = 0.0130 * PT                               # 0.33 mm, EAN-13 at 100%
    width = 95 * mod
    x0 = x + (bw - width) / 2
    top = y + 0.30 * PT
    bar_h = 0.62 * PT
    guard = {0, 1, 2, 45, 46, 47, 48, 49, 92, 93, 94}
    parts = [rect(x + 0.05 * PT, y + 0.05 * PT, bw - 0.10 * PT, bh - 0.10 * PT, "#FFFFFF"),
             text(x + bw / 2, y + 0.24 * PT, f"ISBN {ISBN}", 8.2, "#000000", family="Inter", weight=500,
                  anchor="middle", ls=0.3)]
    i = 0
    while i < 95:                                   # merge runs of dark modules into one rect each
        if bits[i] == "1":
            j = i
            while j < 95 and bits[j] == "1" and ((j in guard) == (i in guard)):
                j += 1
            h = bar_h + (0.06 * PT if i in guard else 0)
            parts.append(rect(x0 + i * mod, top, (j - i) * mod, h, "#000000"))
            i = j
        else:
            i += 1
    fy = top + bar_h + 0.13 * PT
    parts.append(text(x0 - 7 * mod, fy, digits[0], 8, "#000000", family="JetBrains Mono", anchor="middle"))
    parts.append(text(x0 + 24 * mod, fy, digits[1:7], 8, "#000000", family="JetBrains Mono", anchor="middle", ls=0.9))
    parts.append(text(x0 + 71 * mod, fy, digits[7:], 8, "#000000", family="JetBrains Mono", anchor="middle", ls=0.9))
    return "\n".join(parts)


def copyright_title_y(pdf: Path, page: int) -> float:
    """Top of the copyright page's first line (the bold book title), in points from the page top."""
    out = subprocess.run(["pdftotext", "-bbox", "-f", str(page), "-l", str(page), str(pdf), "-"],
                         capture_output=True, text=True, check=True).stdout
    for line in out.splitlines():
        if "<word" in line and ">Decide," in line:
            return float(line.split('yMin="')[1].split('"')[0])
    raise SystemExit("copyright page title not found")


def stamp_interior(src: Path, dst: Path, tmp: Path):
    from pypdf import PdfReader, PdfWriter
    reader = PdfReader(str(src))
    cp = next(i for i, p in enumerate(reader.pages, 1) if "All rights reserved" in p.extract_text())
    y = copyright_title_y(src, cp)
    words = subprocess.run(["pdftotext", "-bbox", "-f", str(cp), "-l", str(cp), str(src), "-"],
                           capture_output=True, text=True, check=True).stdout.splitlines()
    x = min(float(l.split('xMin="')[1].split('"')[0]) for l in words if "<word" in l)   # the text's left edge
    ov = tmp / "isbn.pdf"
    body = (text(x, y - 22, f"ISBN {ISBN} (paperback, India edition)", 7.2, "#111827", weight=700) +
            text(x, y - 12, "Published by Sridhar Mukkandi, Proddatur, Andhra Pradesh, India.", 7.2, "#374151"))
    overlay_pdf(svg_doc(7, 10, body), ov, 7, 10)
    w = PdfWriter()
    for i, page in enumerate(reader.pages, 1):
        if i == cp:
            page.merge_page(PdfReader(str(ov)).pages[0])
        w.add_page(page)
    w.add_metadata({"/Title": "Decide, Don't Generate", "/Author": AUTHOR, "/Subject": f"ISBN {ISBN}"})
    with open(dst, "wb") as f:
        w.write(f)
    return len(reader.pages), cp


def india_cover(spine_mm: float, pages: int):
    PAPER["india"] = spine_mm / 25.4 / pages
    wr = Wrap("paperback", pages=pages, paper="india")
    strap = strapline()
    outs = []
    for g in (False, True):
        svg = wrap_svg(wr, strap, with_guides=False)
        extra = (guides(wr) if g else "") + barcode(*barcode_box(wr))
        svg = svg.replace("\n</svg>\n", "\n" + extra + "\n</svg>\n")
        name = f"cover-india-{spine_mm:g}mm" + ("-guides" if g else "") + ".pdf"
        src = OUT / (name[:-4] + ".html")
        w_in, h_in = round(wr.width, 4), round(wr.height, 4)
        src.write_text(html_page(svg, f"{w_in}in", f"{h_in}in"))
        render([dict(src=str(src), out=str(OUT / name), type="pdf", width=f"{w_in}in", height=f"{h_in}in")])
        src.unlink()
        exact_page(OUT / name, w_in, h_in)
        outs.append(name)
    return wr, outs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--spine-mm", type=float, default=13.0,
                    help="spine width the printer gives for 270 pages on their paper (default 13 mm: ~70-80 GSM)")
    a = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    tmp = OUT / "_tmp"
    tmp.mkdir(exist_ok=True)
    rel = ROOT / "release" / "v1.0"
    for src, dst in ((rel / "print-color" / "interior-color.pdf", OUT / "interior-india-color.pdf"),
                     (rel / "print-bw" / "interior-bw.pdf", OUT / "interior-india-bw.pdf")):
        n, cp = stamp_interior(src, dst, tmp)
        print(f"{dst.name}: {n} pages, ISBN on page {cp}")
    wr, outs = india_cover(a.spine_mm, interior_pages())
    print(f"cover: spine {a.spine_mm:g} mm, {wr.width:.4f} x {wr.height:.4f} in with bleed:", ", ".join(outs))
    shutil.rmtree(tmp)


if __name__ == "__main__":
    main()
