"""Verify a release folder: python3 tools/release_check.py [release/v1.0]  -> release/<v>/checks.json

Placeholders left anywhere, fonts embedded in every PDF, raster resolution in the interior, text inside the
margins, blank pages, page sizes, the EPUB's figures and alt text, cover/interior agreement, every cover's size
against the interior's page count and its paper (both editions), the black-and-white interior being true greyscale,
and code lines that wrap (tools/check_code_wrap.py).
"""
from __future__ import annotations

import html
import json
import re
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "cover"))
from coverlib import AUTHOR, SUBTITLE, TITLE, Wrap, figure_count  # noqa: E402
from wrap import case_study  # noqa: E402

PATTERNS = [r"\[\[", r"TODO", r"VERIFY", r"[Pp]laceholder"]
# Code, not gaps: Python's textwrap.shorten(..., placeholder=" …") in three listings, and pandas column selection
# such as alerts[["p", "zone"]] in the Python appendix
ALLOWED = [r"placeholder\s*=\s*['\"]", r"\[\[\s*[\"']"]


def run(*cmd):
    return subprocess.run(cmd, capture_output=True, text=True).stdout


def pdf_text(p: Path) -> str:
    return run("pdftotext", "-layout", str(p), "-")


def scan(text: str) -> list[str]:
    hits = []
    for pat in PATTERNS:
        for m in re.finditer(pat, text):
            ctx = text[max(0, m.start() - 40):m.end() + 40].replace("\n", " ")
            if not any(re.search(a, ctx) for a in ALLOWED):
                hits.append(ctx.strip())
    return hits


def fonts_ok(p: Path) -> tuple[int, list[str]]:
    rows = run("pdffonts", str(p)).splitlines()[2:]
    bad = [r for r in rows if r.split()[-5] != "yes"]
    return len(rows), bad


def size_in(p: Path) -> list[float]:
    w, h = map(float, re.search(r"Page size:\s+([\d.]+) x ([\d.]+)", run("pdfinfo", str(p))).groups())
    return [round(w / 72, 4), round(h / 72, 4)]


def pages(p: Path) -> int:
    return int(re.search(r"Pages:\s+(\d+)", run("pdfinfo", str(p))).group(1))


def margins(p: Path, margin_in=0.9, tol_pt=3.5) -> dict:
    """Words outside the text block (a few points allowed for hanging punctuation), and pages with no words."""
    html = run("pdftotext", "-bbox", str(p), "/dev/stdout")
    pgs = re.findall(r'<page width="([\d.]+)" height="([\d.]+)">(.*?)</page>', html, re.S)
    out, blank = [], []
    for n, (w, h, body) in enumerate(pgs, 1):
        w, h = float(w), float(h)
        words = re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', body)
        if not words:
            blank.append(n)
        for x0, y0, x1, y1, t in words:
            x0, y0, x1, y1 = map(float, (x0, y0, x1, y1))
            if x0 < margin_in * 72 - tol_pt or x1 > w - margin_in * 72 + tol_pt or y0 < 18 or y1 > h - 18:
                out.append(f"p{n}: {t}")
    return dict(outside=out, blank_pages=blank)


def covers_match(rel: Path, n_pages: int) -> dict:
    """Each cover wrap's size must equal the size KDP's formula gives for this interior's page count and paper."""
    dims = json.loads((rel / "print-color" / "cover-dimensions.json").read_text())
    out = {}
    for name, f in (("paperback", rel / "print-color" / "cover-paperback-color.pdf"), ("hardcover", rel / "print-color" / "cover-hardcover-color.pdf"),
                    ("paperback-bw", rel / "print-bw" / "cover-paperback-bw.pdf"),
                    ("paperback-standard-color", rel / "print-color" / "cover-paperback-standard-color.pdf")):
        d = dims[name]
        w = Wrap(d["kind"], pages=n_pages, paper=d["paper"])
        got = size_in(f)
        out[name] = dict(paper=d["paper"], pages_used=d["pages"], interior_pages=n_pages, spine_in=round(w.spine, 4),
                         expected_in=[round(w.width, 4), round(w.height, 4)], pdf_in=got,
                         ok=d["pages"] == n_pages and abs(got[0] - w.width) < 0.002 and abs(got[1] - w.height) < 0.002)
    return out


def greyscale_ok(p: Path) -> dict:
    """True greyscale: every rendered page has no coloured pixel, and every embedded image is grey."""
    import tempfile
    import numpy as np
    from PIL import Image
    with tempfile.TemporaryDirectory() as d:
        run("pdftoppm", "-r", "30", "-png", str(p), f"{d}/p")
        coloured = []
        for i, f in enumerate(sorted(Path(d).glob("p*.png")), 1):
            a = np.asarray(Image.open(f).convert("RGB"), dtype=int)
            if (a.max(axis=2) - a.min(axis=2)).max() > 3:
                coloured.append(i)
    imgs = [l.split() for l in run("pdfimages", "-list", str(p)).splitlines()[2:]]
    return dict(coloured_pages=coloured, image_colour_spaces=sorted({r[5] for r in imgs}))


def main(rel="release/v1.0"):
    rel = ROOT / rel
    res: dict = {}
    interior = rel / "print-color" / "interior-color.pdf"
    itext = pdf_text(interior)
    res["interior"] = dict(pages=pages(interior), size_in=size_in(interior))
    n, bad = fonts_ok(interior)
    res["interior"]["fonts"] = dict(count=n, not_embedded=bad)
    imgs = [l.split() for l in run("pdfimages", "-list", str(interior)).splitlines()[2:]]
    res["interior"]["raster_images"] = [dict(page=int(r[0]), px=f"{r[3]}x{r[4]}", ppi=[int(r[12]), int(r[13])])
                                        for r in imgs]
    res["interior"]["raster_below_300ppi"] = [i for i in res["interior"]["raster_images"] if min(i["ppi"]) < 300]
    res["interior"].update(margins(interior))
    # placeholders everywhere
    hits = {"interior": scan(itext)}
    for f in sorted((rel / "preview").glob("*.pdf")):
        hits[f.name] = scan(pdf_text(f))
    for f in sorted((rel / "print-color").glob("cover-*.pdf")) + sorted((rel / "print-bw").glob("*.pdf")):
        hits[f.name] = scan(pdf_text(f))
    with zipfile.ZipFile(rel / "ebook" / "book.epub") as z:
        etext = " ".join(html.unescape(re.sub(r"<[^>]+>", "", z.read(n).decode("utf-8", "ignore")))
                         for n in z.namelist() if n.endswith((".xhtml", ".ncx", ".opf")))
        imgs = [m for n in z.namelist() if n.endswith(".xhtml") for m in re.findall(r"<img[^>]*>", z.read(n).decode())]
    hits["book.epub"] = scan(etext)
    res["placeholders"] = hits
    res["epub"] = dict(images=len(imgs), empty_alt=sum('alt=""' in i for i in imgs),
                       png=sum(".png" in i for i in imgs))
    # fonts in every other PDF
    res["fonts"] = {}
    for f in sorted(list((rel / "print-color").rglob("*.pdf")) + list((rel / "print-bw").rglob("*.pdf"))
                    + list((rel / "preview").glob("*.pdf"))):
        n, bad = fonts_ok(f)
        res["fonts"][str(f.relative_to(rel))] = dict(count=n, not_embedded=len(bad), size_in=size_in(f), pages=pages(f))
    # cover and interior agree
    ctext = pdf_text(rel / "print-color" / "cover-paperback-color.pdf")
    flat = lambda s: re.sub(r"\s+", " ", s.replace("’", "'"))  # noqa: E731
    before, after, _ = case_study()
    figs = figure_count()          # numbered figure captions in the rendered book (_book/*.pdf)
    res["agreement"] = {
        "title in interior": flat(TITLE) in flat(itext), "subtitle in interior": flat(SUBTITLE) in flat(itext),
        "author on cover and interior": AUTHOR in ctext and AUTHOR in itext,
        "case study on cover": [f"{before:.0%}", f"{after:.0%}"],
        "case study in Chapter 18": re.findall(r"(\d+%)", itext[itext.find("real threats a person sees"):][:200])[:2],
        "figures in interior": figs, "cover strap": "130+ figures" if "130+ figures" in ctext else "missing",
    }
    res["agreement"]["case study matches"] = (res["agreement"]["case study on cover"]
                                             == res["agreement"]["case study in Chapter 18"])
    res["agreement"]["strap true"] = figs >= 130
    # covers against the page count, for both editions; the black-and-white interior
    res["covers"] = covers_match(rel, res["interior"]["pages"])
    bw = rel / "print-bw" / "interior-bw.pdf"
    bimgs = [l.split() for l in run("pdfimages", "-list", str(bw)).splitlines()[2:]]
    res["bw_interior"] = dict(pages=pages(bw), size_in=size_in(bw), fonts_not_embedded=fonts_ok(bw)[1],
                              raster_below_300ppi=[r[0] for r in bimgs if min(int(r[12]), int(r[13])) < 300],
                              **greyscale_ok(bw))
    res["colour_interior_has_colour"] = bool(greyscale_ok(interior)["coloured_pages"])
    cw = subprocess.run([sys.executable, str(ROOT / "tools" / "check_code_wrap.py"), str(interior)],
                        capture_output=True, text=True)
    res["code_wrap"] = dict(ok=cw.returncode == 0, summary=cw.stdout.strip().splitlines()[-1])
    (rel / "checks.json").write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n")
    short = dict(interior={k: v for k, v in res["interior"].items() if k != "raster_images"},
                 placeholders={k: len(v) for k, v in hits.items()}, epub=res["epub"], agreement=res["agreement"],
                 covers=res["covers"], bw_interior=res["bw_interior"], code_wrap=res["code_wrap"],
                 fonts={k: (v["not_embedded"], v["size_in"], v["pages"]) for k, v in res["fonts"].items()})
    print(json.dumps(short, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main(*sys.argv[1:])
