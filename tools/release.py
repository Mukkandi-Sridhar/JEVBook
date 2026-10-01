"""Assemble the release: python3 tools/release.py INTERIOR.pdf BOOK.epub [version]

Run after the book, EPUB and cover are built (see RELEASE.md). Writes release/<version>/:

  print-color/ the colour edition: interior-color.pdf for KDP (padded to an even page count), the paperback and
             hardcover cover wraps (cover-paperback-color.pdf, cover-hardcover-color.pdf), and guides/ with the
             with-guides versions for checking
  ebook/     book.epub (figure alt text added, see tools/epub_post.py) and ebook-cover.jpg
  preview/   Decide-Dont-Generate-COMPLETE.pdf (front cover + interior + back cover, bookmarked)
             and sample-chapters.pdf (cover, contents, Chapters 3 and 13, closing page)
  print-bw/  the black-and-white edition, in the same layout: interior-bw.pdf (the same interior converted to true greyscale with
             `mutool recolor -c gray`) and the paperback cover wrap with its spine sized for KDP's white
             black-and-white paper (guides/ has the with-guides version)
  marketing/ 3D mockup, square post, 1200 x 628 banner
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "cover"))

from pypdf import PdfReader, PdfWriter  # noqa: E402
from pypdf.generic import NameObject, TextStringObject  # noqa: E402

from coverlib import AUTHOR, C, PT, TITLE, SUBTITLE, Wrap, interior_pages, rect, svg_doc, text, to_pdf  # noqa: E402
from wrap import BG, EMAIL, PAPERBACK_PAPER, REPO_LABEL, back, front  # noqa: E402
from coverlib import strapline  # noqa: E402

REPO = "https://github.com/Mukkandi-Sridhar/JEVBook"


def clean_titles(w: PdfWriter):
    """LaTeX quotes reach the bookmarks as ``...''; make them curly quotes."""
    def walk(node):
        while node is not None:
            node = node.get_object()
            t = str(node["/Title"])
            nt = t.replace("``", "“").replace("''", "”").replace("`", "‘")
            if nt != t:
                node[NameObject("/Title")] = TextStringObject(nt)
            if "/First" in node:
                walk(node["/First"])
            node = node.get("/Next")
    if "/Outlines" in w._root_object and "/First" in w._root_object["/Outlines"]:
        walk(w._root_object["/Outlines"]["/First"])


def outline_pages(reader: PdfReader) -> list[tuple[int, str, int]]:
    """(depth, title, 0-based page) for the top two outline levels."""
    out = []

    def walk(items, depth):
        for it in items:
            if isinstance(it, list):
                walk(it, depth + 1)
            elif depth <= 1:
                out.append((depth, it.title, reader.get_destination_page_number(it)))
    walk(reader.outline, 0)
    return out


def interior(src: Path, dst: Path) -> int:
    w = PdfWriter(clone_from=str(src))
    clean_titles(w)
    if len(w.pages) % 2:
        box = w.pages[0].mediabox
        w.add_blank_page(width=float(box.width), height=float(box.height))
    w.add_metadata({"/Title": f"{TITLE}: {SUBTITLE}", "/Author": AUTHOR})
    with open(dst, "wb") as f:
        w.write(f)
    return len(w.pages)


def cover_pages(tmp: Path) -> tuple[Path, Path]:
    """The front and back panels as 7 x 10 in pages, for the preview PDFs."""
    wr = Wrap("paperback", pages=interior_pages(), paper=PAPERBACK_PAPER)
    f, b = tmp / "front.pdf", tmp / "back.pdf"
    to_pdf(svg_doc(7, 10, front(7 * PT, 10 * PT, strapline())), f, 7, 10)
    to_pdf(svg_doc(7, 10, back(7 * PT, 10 * PT, wr)), b, 7, 10)
    return f, b


def closing_page(tmp: Path) -> Path:
    W, H = 7 * PT, 10 * PT
    m = 0.9 * PT
    ink, ink2 = "#1F2430", "#4B5563"
    parts = [rect(0, 0, W, H, "#FFFFFF"),
             rect(m, 2.2 * PT, 0.5 * PT, 0.06 * PT, C["jev"]),
             rect(m + 0.54 * PT, 2.2 * PT, 0.22 * PT, 0.06 * PT, C["llm"]),
             rect(m + 0.80 * PT, 2.2 * PT, 0.12 * PT, 0.06 * PT, C["data"]),
             text(m, 2.9 * PT, "That’s the end of the sample.", 20, ink, weight=700),
             text(m, 3.35 * PT, f"The full book has 22 chapters, runnable labs for every one of them,", 10.5, ink2),
             text(m, 3.58 * PT, "and a free mock of Jev that needs no API key.", 10.5, ink2),
             text(m, 4.4 * PT, "Code, labs and figures", 11, ink, weight=700),
             text(m, 4.68 * PT, REPO, 11, C["data"], family="JetBrains Mono"),
             text(m, 5.4 * PT, "Contact", 11, ink, weight=700),
             text(m, 5.68 * PT, EMAIL, 11, ink2, family="JetBrains Mono"),
             text(m, H - 1.0 * PT, f"{TITLE} · {AUTHOR}", 8.5, "#8A919C")]
    out = tmp / "closing.pdf"
    to_pdf(svg_doc(7, 10, "\n".join(parts)), out, 7, 10)
    return out


def complete(interior_pdf: Path, fpdf: Path, bpdf: Path, dst: Path):
    w = PdfWriter()
    w.append(str(fpdf), import_outline=False)
    w.add_outline_item("Front cover", 0)
    w.append(str(interior_pdf), import_outline=True)
    w.append(str(bpdf), import_outline=False)
    w.add_outline_item("Back cover", len(w.pages) - 1)
    clean_titles(w)
    w.add_metadata({"/Title": f"{TITLE}: {SUBTITLE} (complete preview)", "/Author": AUTHOR})
    w.page_mode = "/UseOutlines"
    with open(dst, "wb") as f:
        w.write(f)


def sample(interior_pdf: Path, fpdf: Path, closing: Path, dst: Path):
    r = PdfReader(str(interior_pdf))
    marks = outline_pages(r)
    tops = [(t, p) for d, t, p in marks]

    def span(title_start):
        i = next(k for k, (t, _) in enumerate(tops) if t.startswith(title_start))
        start = tops[i][1]
        end = next((p for _, p in tops[i + 1:] if p > start), len(r.pages)) - 1
        return start, end

    toc_start = next(p for p in range(len(r.pages)) if "Table of contents" in (r.pages[p].extract_text() or "")[:200])
    toc_end = min(p for _, p in tops) - 1
    ch3 = span("3 ")
    ch13 = span("13 ")
    w = PdfWriter()
    w.append(str(fpdf))
    w.add_outline_item("Front cover", 0)
    n = len(w.pages)
    w.append(str(interior_pdf), pages=(toc_start, toc_end + 1), import_outline=False)
    w.add_outline_item("Table of contents", n)
    n = len(w.pages)
    w.append(str(interior_pdf), pages=(ch3[0], ch3[1] + 1), import_outline=False)
    w.add_outline_item(next(t for t, p in tops if p == ch3[0] and t.startswith("3 ")), n)
    n = len(w.pages)
    w.append(str(interior_pdf), pages=(ch13[0], ch13[1] + 1), import_outline=False)
    w.add_outline_item(next(t for t, p in tops if p == ch13[0] and t.startswith("13 ")), n)
    n = len(w.pages)
    w.append(str(closing))
    w.add_outline_item("Where to find the rest", n)
    clean_titles(w)
    w.add_metadata({"/Title": f"{TITLE}: sample chapters", "/Author": AUTHOR})
    w.page_mode = "/UseOutlines"
    with open(dst, "wb") as f:
        w.write(f)
    return dict(toc=(toc_start + 1, toc_end + 1), ch3=(ch3[0] + 1, ch3[1] + 1), ch13=(ch13[0] + 1, ch13[1] + 1),
                pages=len(w.pages))


def greyscale(src: Path, dst: Path):
    """True greyscale copy of a PDF: every colour in text, vector art and images becomes a grey level."""
    subprocess.run(["mutool", "recolor", "-c", "gray", "-o", str(dst), str(src)], check=True, capture_output=True)


def main(interior_src: str, epub: str, version: str = "v1.0"):
    out = ROOT / "release" / version
    for sub in ("print-color/guides", "print-bw/guides", "ebook", "preview", "marketing"):
        (out / sub).mkdir(parents=True, exist_ok=True)
    tmp = out / "_tmp"
    tmp.mkdir(exist_ok=True)
    cov = ROOT / "cover"
    pages = interior(Path(interior_src), out / "print-color" / "interior-color.pdf")
    for kind in ("paperback", "hardcover"):
        shutil.copy(cov / "print" / f"cover-{kind}.pdf", out / "print-color" / f"cover-{kind}-color.pdf")
        shutil.copy(cov / "print" / f"cover-{kind}-guides.pdf", out / "print-color" / "guides" / f"cover-{kind}-color-guides.pdf")
    shutil.copy(cov / "print" / "dimensions.json", out / "print-color" / "cover-dimensions.json")
    greyscale(out / "print-color" / "interior-color.pdf", out / "print-bw" / "interior-bw.pdf")
    shutil.copy(cov / "print" / "cover-paperback-bw.pdf", out / "print-bw" / "cover-paperback-bw.pdf")
    shutil.copy(cov / "print" / "cover-paperback-bw-guides.pdf", out / "print-bw" / "guides" / "cover-paperback-bw-guides.pdf")
    shutil.copy(cov / "print" / "dimensions.json", out / "print-bw" / "cover-dimensions.json")
    shutil.copy(epub, out / "ebook" / "book.epub")
    shutil.copy(cov / "ebook" / "cover.jpg", out / "ebook" / "ebook-cover.jpg")
    fpdf, bpdf = cover_pages(tmp)
    complete(Path(interior_src), fpdf, bpdf, out / "preview" / "Decide-Dont-Generate-COMPLETE.pdf")
    info = sample(Path(interior_src), fpdf, closing_page(tmp), out / "preview" / "sample-chapters.pdf")
    for f in ("mockup-3d.png", "post-square-1080.png", "banner-1200x628.png"):
        shutil.copy(cov / "marketing" / f, out / "marketing" / f)
    shutil.rmtree(tmp)
    print(dict(interior_pages=pages, sample=info))


if __name__ == "__main__":
    main(*sys.argv[1:])
