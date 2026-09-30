"""Shared pieces for the cover: palette, fonts, KDP dimensions, SVG helpers and the Chromium renderer.

Everything here is parametric: the page count comes from the rendered interior PDF, and every size is computed
from the trim, the bleed and KDP's per-page paper thickness. See DECISIONS.md (D-71 onwards).
"""
from __future__ import annotations

import json
import math
import re
import subprocess
from dataclasses import dataclass
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COVER = ROOT / "cover"
PT = 72.0                                   # SVG user units are points: 72 per inch

# ---------------------------------------------------------------- palette (the interior's, jevkit/figs/style.py)
C = dict(
    data="#2F6DB5", llm="#E07A1F", jev="#3B9C6E", fail="#B8323A",
    ink="#1F2430", ink2="#4B5563", muted="#8A919C", grid="#E4E7EB", rule="#C9CED6", paper="#FBFAF7",
    act="#B7A6E0", review="#8468C9", escalate="#4B2C8F",
    # the dark cover ground, and the green and orange lifted for it (same hues, higher lightness)
    night="#141925", night2="#1C2230", jev_on_dark="#4FBA85", llm_on_dark="#F08C35", text_on_dark="#F3F4F6",
    sub_on_dark="#C9CED6", faint_on_dark="#8A919C",
)


def mix(a: str, b: str, t: float) -> str:
    """Solid colour t of the way from a to b. Used instead of transparency, which print files shouldn't rely on."""
    pa = [int(a[i:i + 2], 16) for i in (1, 3, 5)]
    pb = [int(b[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(x + (y - x) * t):02X}" for x, y in zip(pa, pb))


def luminance(h: str) -> float:
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (int(h[i:i + 2], 16) for i in (1, 3, 5))
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def contrast(a: str, b: str) -> float:
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


# ---------------------------------------------------------------- book facts, read from the build
TITLE = "Decide, Don\u2019t Generate"
SUBTITLE = "Jev, System One Models, and the Decision Layer of Agentic AI"
AUTHOR = "Sridhar Mukkandi"                 # exactly as on the title page (assets/latex/before-body.tex)


def interior_pages() -> int:
    """Pages in the rendered interior PDF, rounded up to even: a printed book has two sides to every leaf."""
    pdf = next((ROOT / "_book").glob("*.pdf"))
    out = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True, check=True).stdout
    n = int(re.search(r"Pages:\s+(\d+)", out).group(1))
    return n + (n % 2)


def figure_count() -> int:
    pdf = next((ROOT / "_book").glob("*.pdf"))
    text = subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True, text=True, check=True).stdout
    return len(set(re.findall(r"^Figure (\d+(?:\.\d+)?)\.\s", text, re.M)))


def labs_count() -> int:
    return len(list((ROOT / "labs").glob("ch*.py")))


def strapline() -> str:
    figs = figure_count()
    return f"Runnable labs · {figs // 10 * 10}+ figures · no API key needed"


# ---------------------------------------------------------------- KDP geometry
# Paper thickness per page (inches), from KDP's "Create a Paperback Cover" help page.
PAPER = {"bw_white": 0.002252, "bw_cream": 0.0025, "standard_color": 0.002252, "premium_color": 0.002347}


@dataclass
class Wrap:
    kind: str            # "paperback" or "hardcover"
    trim_w: float = 7.0
    trim_h: float = 10.0
    pages: int = 0
    paper: str = "standard_color"
    bleed: float = 0.125       # paperback: bleed on every outside edge
    safe: float = 0.25         # keep text at least this far inside the trim (paperback) or board edge (hardcover)
    # hardcover (case laminate), KDP: 15 mm wrap, 10 mm hinge, boards 5 mm wider and 6 mm taller than the trim,
    # 4.8 mm added to the spine for the case
    wrap: float = 15 / 25.4
    hinge: float = 10 / 25.4
    board_dw: float = 5 / 25.4
    board_dh: float = 6 / 25.4
    case_spine: float = 4.8 / 25.4

    @property
    def spine(self) -> float:
        s = self.pages * PAPER[self.paper]
        return s + self.case_spine if self.kind == "hardcover" else s

    @property
    def edge(self) -> float:              # what sits outside each panel: bleed (paperback) or wrap (hardcover)
        return self.bleed if self.kind == "paperback" else self.wrap

    @property
    def panel_w(self) -> float:           # printed width of the back or the front
        return self.trim_w if self.kind == "paperback" else self.trim_w + self.board_dw

    @property
    def panel_h(self) -> float:
        return self.trim_h if self.kind == "paperback" else self.trim_h + self.board_dh

    @property
    def width(self) -> float:
        return 2 * self.edge + 2 * self.panel_w + self.spine

    @property
    def height(self) -> float:
        return 2 * self.edge + self.panel_h

    # x positions (inches from the left edge of the file)
    @property
    def back_x(self) -> float: return self.edge
    @property
    def spine_x(self) -> float: return self.edge + self.panel_w
    @property
    def front_x(self) -> float: return self.edge + self.panel_w + self.spine
    @property
    def top_y(self) -> float: return self.edge

    def spine_text_ok(self) -> bool:
        return self.pages >= 79             # KDP prints spine text from 79 pages

    def summary(self) -> dict:
        return dict(kind=self.kind, pages=self.pages, paper=self.paper, paper_in_per_page=PAPER[self.paper],
                    trim=f"{self.trim_w} x {self.trim_h} in", spine_in=round(self.spine, 4),
                    width_in=round(self.width, 4), height_in=round(self.height, 4),
                    edge_in=round(self.edge, 4), panel_in=f"{self.panel_w:.4f} x {self.panel_h:.4f}",
                    spine_text=self.spine_text_ok())


# ---------------------------------------------------------------- SVG helpers (units: points)
def svg_doc(w_in: float, h_in: float, body: str) -> str:
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w_in}in" height="{h_in}in" '
            f'viewBox="0 0 {w_in * PT:.3f} {h_in * PT:.3f}">\n{body}\n</svg>\n')


def text(x, y, s, size, fill, family="Inter", weight=400, anchor="start", ls=0.0, style="normal", extra=""):
    return (f'<text x="{x:.2f}" y="{y:.2f}" font-family="\'{family}\'" font-size="{size:.2f}" font-weight="{weight}" '
            f'font-style="{style}" fill="{fill}" text-anchor="{anchor}" letter-spacing="{ls:.2f}" {extra}>'
            f'{escape(s)}</text>')


def rect(x, y, w, h, fill, rx=0.0, stroke="none", sw=0.0, extra=""):
    return (f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{rx:.2f}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw:.2f}" {extra}/>')


def line(x1, y1, x2, y2, stroke, sw=1.0, dash=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{stroke}" stroke-width="{sw:.2f}"{d}/>'


def circle(cx, cy, r, fill, stroke="none", sw=0.0):
    return f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw:.2f}"/>'


# ---------------------------------------------------------------- rendering
FACES = [("Inter", 400, "normal", "Inter-Regular"), ("Inter", 500, "normal", "Inter-Medium"),
         ("Inter", 600, "normal", "Inter-SemiBold"), ("Inter", 700, "normal", "Inter-Bold"),
         ("Inter", 800, "normal", "Inter-ExtraBold"), ("Inter", 400, "italic", "Inter-Italic"),
         ("Source Serif 4", 400, "normal", "SourceSerif4-Regular"), ("Source Serif 4", 600, "normal", "SourceSerif4-Semibold"),
         ("Source Serif 4", 700, "normal", "SourceSerif4-Bold"), ("Source Serif 4", 400, "italic", "SourceSerif4-Italic"),
         ("JetBrains Mono", 400, "normal", "JetBrainsMono-Regular"), ("JetBrains Mono", 500, "normal", "JetBrainsMono-Medium"),
         ("JetBrains Mono", 700, "normal", "JetBrainsMono-Bold")]
# every face is loaded from assets/fonts, so nothing depends on how the system names its fonts
FONT_CSS = "".join(f"@font-face{{font-family:'{f}';font-weight:{w};font-style:{s};"
                   f"src:url('{(ROOT / 'assets' / 'fonts' / (n + '.ttf')).as_uri()}')}}" for f, w, s, n in FACES)
PAGE_CSS = FONT_CSS + "html,body{margin:0;padding:0;background:#fff}svg{display:block}"


def html_page(svg: str, w: str, h: str) -> str:
    """Wrap an SVG in a page of exactly w x h (CSS lengths), for Chromium."""
    svg = re.sub(r'width="[^"]+" height="[^"]+"', f'width="{w}" height="{h}"', svg, count=1)
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{PAGE_CSS}"
            f"@page{{size:{w} {h};margin:0}}</style></head><body>{svg}</body></html>")


def render(jobs: list[dict]):
    jf = COVER / "src" / "_jobs.json"
    jf.write_text(json.dumps(jobs))
    subprocess.run(["node", str(COVER / "render.mjs"), str(jf)], check=True, capture_output=True)
    jf.unlink()


def to_png(svg: str, out: Path, width_px: int, height_px: int):
    src = COVER / "src" / (out.stem + ".html")
    src.write_text(html_page(svg, f"{width_px}px", f"{height_px}px"))
    render([dict(src=str(src), out=str(out), type="png", width=width_px, height=height_px)])
    src.unlink()


def to_pdf(svg: str, out: Path, w_in: float, h_in: float, keep_src: Path | None = None):
    src = keep_src or COVER / "src" / (out.stem + ".html")
    src.write_text(html_page(svg, f"{w_in}in", f"{h_in}in"))
    render([dict(src=str(src), out=str(out), type="pdf", width=f"{w_in}in", height=f"{h_in}in")])
    if keep_src is None:
        src.unlink()
    exact_page(out, w_in, h_in)


def exact_page(pdf: Path, w_in: float, h_in: float):
    """Chromium rounds PDF page sizes; KDP wants the cover exactly the calculated size. Crop the page box to it,
    anchored at the top left where the artwork starts, and record the same box as trim and bleed box."""
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import RectangleObject
    r = PdfReader(str(pdf))
    page = r.pages[0]
    top = float(page.mediabox.top)
    box = RectangleObject([0, top - h_in * PT, w_in * PT, top])
    page.mediabox = box
    page.cropbox = box
    page.bleedbox = box
    page.trimbox = box
    w = PdfWriter()
    w.add_page(page)
    w.add_metadata({"/Title": TITLE + " (cover)", "/Author": AUTHOR})
    with open(pdf, "wb") as f:
        w.write(f)


# ---------------------------------------------------------------- measuring text with the real font files
FONT_FILES = {
    ("Inter", 400): "Inter-Regular.ttf", ("Inter", 500): "Inter-Medium.ttf", ("Inter", 600): "Inter-SemiBold.ttf",
    ("Inter", 700): "Inter-Bold.ttf", ("Inter", 800): "Inter-ExtraBold.ttf",
    ("Source Serif 4", 400): "SourceSerif4-Regular.ttf", ("Source Serif 4", 600): "SourceSerif4-Semibold.ttf",
    ("Source Serif 4", 700): "SourceSerif4-Bold.ttf", ("Source Serif 4 italic", 400): "SourceSerif4-Italic.ttf",
    ("JetBrains Mono", 400): "JetBrainsMono-Regular.ttf", ("JetBrains Mono", 500): "JetBrainsMono-Medium.ttf",
    ("JetBrains Mono", 700): "JetBrainsMono-Bold.ttf",
}
_font_cache: dict = {}


def measure(s: str, size: float, family="Inter", weight=400, ls=0.0) -> float:
    """Advance width of s in points (the same units as the SVG), plus letter spacing."""
    from PIL import ImageFont
    key = (family, weight, round(size * 10))
    if key not in _font_cache:
        _font_cache[key] = ImageFont.truetype(str(ROOT / "assets" / "fonts" / FONT_FILES[(family, weight)]),
                                              size=max(1, round(size * 10)))
    return _font_cache[key].getlength(s) / 10 + ls * max(0, len(s) - 1)


def fit(s: str, width: float, family="Inter", weight=400, ls_em=0.0, max_size=400.0) -> float:
    """Largest size (pt) at which s fits in width."""
    base = measure(s, 100, family, weight, ls=ls_em * 100)
    return min(max_size, 100 * width / base)


def wrap_lines(s: str, width: float, size: float, family="Inter", weight=400) -> list[str]:
    words, lines, cur = s.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if measure(t, size, family, weight) <= width or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w
    return lines + ([cur] if cur else [])
