"""Author's-copy print files for a local printer (not Amazon): python3 tools/local_print.py [--spine-mm 13]

Writes release/v1.0/print-local/:
  interior-local-color.pdf, interior-local-bw.pdf   the release interiors with a small footer on every printed page
                                                    ("Author's copy, printed in India. Not for resale.") and a note
                                                    on the copyright page
  cover-local-<spine>mm.pdf (+ -guides.pdf)         the paperback cover with the spine the printer gives you and an
                                                    "Author's copy" label where Amazon prints its barcode

Local copies carry no ISBN: the free KDP ISBN may only be used on copies Amazon prints. The spine depends on the
printer's paper, so ask them for it (in mm, for 270 pages) and rerun with --spine-mm.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "cover"))
from coverlib import (AUTHOR, C, PAPER, PT, Wrap, exact_page, html_page, interior_pages, rect, render,  # noqa: E402
                      strapline, svg_doc, text)
from wrap import barcode_box, guides, wrap_svg  # noqa: E402

OUT = ROOT / "release" / "v1.0" / "print-local"
FOOTER = "© 2026 Sridhar Mukkandi  ·  Author’s copy, printed in India  ·  Not for resale"
NOTE = ["AUTHOR’S COPY", "Printed in India for the author, for personal, gift and library use.",
        "Not for resale. This print has no ISBN; the retail edition is sold on Amazon."]


def overlay_pdf(svg: str, out: Path, w_in: float, h_in: float):
    """Render an SVG to a PDF page with a transparent background, so it can sit under or over another page."""
    src = out.with_suffix(".html")
    src.write_text(html_page(svg, f"{w_in}in", f"{h_in}in").replace("background:#fff", "background:transparent"))
    render([dict(src=str(src), out=str(out), type="pdf", width=f"{w_in}in", height=f"{h_in}in")])
    src.unlink()
    exact_page(out, w_in, h_in)


def blank_pages(pdf: Path) -> set[int]:
    """1-based numbers of pages with no text and no images (the deliberate blanks between parts)."""
    from pypdf import PdfReader
    blanks = set()
    for i, page in enumerate(PdfReader(str(pdf)).pages, 1):
        res = page.get("/Resources") or {}
        xo = res.get("/XObject") if hasattr(res, "get") else None
        if not page.extract_text().strip() and not xo:
            blanks.add(i)
    return blanks


def stamp_interior(src: Path, dst: Path, tmp: Path, grey: bool):
    from pypdf import PdfReader, PdfWriter
    W, H = 7 * PT, 10 * PT
    ink = "#6B7280"
    foot = tmp / "footer.pdf"
    overlay_pdf(svg_doc(7, 10, text(W / 2, H - 0.42 * PT, FOOTER, 6.6, ink, anchor="middle")), foot, 7, 10)
    x, y = 0.95 * PT, 1.15 * PT
    parts = [rect(x - 8, y - 16, 5.45 * PT, 56, "none", rx=3, stroke="#111827" if grey else C["jev"], sw=0.8),
             text(x, y, NOTE[0], 9.5, "#111827", weight=700, ls=0.8),
             text(x, y + 15, NOTE[1], 8, "#374151"), text(x, y + 27, NOTE[2], 8, "#374151")]
    note = tmp / "note.pdf"
    overlay_pdf(svg_doc(7, 10, "\n".join(parts) + text(W / 2, H - 0.42 * PT, FOOTER, 6.6, ink, anchor="middle")),
                note, 7, 10)
    reader = PdfReader(str(src))
    blanks = blank_pages(src)
    copyright_page = next(i for i, p in enumerate(reader.pages, 1) if "All rights reserved" in p.extract_text())
    w = PdfWriter()
    for i, page in enumerate(reader.pages, 1):
        if i not in blanks:
            ov = PdfReader(str(note if i == copyright_page else foot)).pages[0]
            page.merge_page(ov)
        w.add_page(page)
    w.add_metadata({"/Title": "Decide, Don't Generate (author's copy, not for resale)", "/Author": AUTHOR})
    with open(dst, "wb") as f:
        w.write(f)
    return len(reader.pages), len(blanks), copyright_page


def label(wr: Wrap) -> str:
    """The 'Author's copy' label, in the 2 x 1.2 in box where Amazon prints its barcode."""
    x, y, bw, bh = barcode_box(wr)
    cx = x + bw / 2
    return "\n".join([
        rect(x, y, bw, bh, C["night2"], rx=5, stroke=C["faint_on_dark"], sw=0.6),
        text(cx, y + 0.36 * PT, "AUTHOR’S COPY", 10, C["text_on_dark"], weight=700, anchor="middle", ls=1.0),
        text(cx, y + 0.62 * PT, "Printed in India", 8, C["sub_on_dark"], anchor="middle"),
        text(cx, y + 0.80 * PT, "Not for resale", 8, C["sub_on_dark"], anchor="middle"),
        text(cx, y + 1.02 * PT, "Retail edition on Amazon", 6.8, C["faint_on_dark"], anchor="middle"),
    ])


def local_cover(spine_mm: float, pages: int):
    PAPER["local"] = spine_mm / 25.4 / pages
    wr = Wrap("paperback", pages=pages, paper="local")
    strap = strapline()
    outs = []
    for g in (False, True):
        svg = wrap_svg(wr, strap, with_guides=False)
        extra = (guides(wr) if g else "") + label(wr)          # the label sits over the barcode guide
        svg = svg.replace("\n</svg>\n", "\n" + extra + "\n</svg>\n")
        name = f"cover-local-{spine_mm:g}mm" + ("-guides" if g else "") + ".pdf"
        src = OUT / (name[:-4] + ".html")
        src.write_text(html_page(svg, f"{round(wr.width, 4)}in", f"{round(wr.height, 4)}in"))
        render([dict(src=str(src), out=str(OUT / name), type="pdf", width=f"{round(wr.width, 4)}in",
                     height=f"{round(wr.height, 4)}in")])
        src.unlink()
        exact_page(OUT / name, round(wr.width, 4), round(wr.height, 4))
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
    for src, dst, grey in ((rel / "print-color" / "interior-color.pdf", OUT / "interior-local-color.pdf", False),
                           (rel / "print-bw" / "interior-bw.pdf", OUT / "interior-local-bw.pdf", True)):
        n, b, cp = stamp_interior(src, dst, tmp, grey)
        print(f"{dst.name}: {n} pages, footer on {n - b} (blanks left blank), note on page {cp}")
    wr, outs = local_cover(a.spine_mm, interior_pages())
    print(f"cover: spine {a.spine_mm:g} mm ({wr.spine:.4f} in), {wr.width:.4f} x {wr.height:.4f} in with 0.125 in bleed:",
          ", ".join(outs))
    shutil.rmtree(tmp)
    subprocess.run(["pdfinfo", str(OUT / outs[0])], check=True, capture_output=True)


if __name__ == "__main__":
    main()
