"""Build the cover: front, spine and back as one print-ready wrap (paperback and hardcover), the ebook cover and the
marketing mockups.

python cover/wrap.py

Every dimension comes from coverlib.Wrap: the page count is read from the rendered interior PDF and the spine from
KDP's per-page paper thickness. The chosen front is concept (a); see cover/README.md and DECISIONS.md.
"""
from __future__ import annotations

import json
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import segno  # noqa: E402

from coverlib import (AUTHOR, C, COVER, PT, ROOT, Wrap, circle, contrast, fit, interior_pages, line,  # noqa: E402
                      measure, mix, rect, render, strapline, svg_doc, text, to_pdf, to_png, wrap_lines, html_page)
from concepts import SUB_LINES, zone_bar  # noqa: E402

REPO_URL = "https://github.com/Mukkandi-Sridhar/JEVBook"
REPO_LABEL = "github.com/Mukkandi-Sridhar/JEVBook"
EMAIL = "sridhar.authorhub@gmail.com"
BG = C["night"]
# KDP paper: standard colour suits a text-heavy book with colour charts; hardcovers are only offered in premium colour
PAPERBACK_PAPER = "standard_color"
HARDCOVER_PAPER = "premium_color"
BODY = "#D5D9DF"            # body text on the dark ground


# ---------------------------------------------------------------- front (concept a, refined)
def front(W, H, strap):
    m = W * 0.078
    tw = W - 2 * m
    out = [rect(0, 0, W, H, BG)]
    s1 = fit("Decide,", tw, "Inter", 800, ls_em=-0.03)
    extra = max(0.0, H - W * 10 / 7)       # a taller canvas (the ebook) spreads its extra height through the layout
    y1 = m + s1 * 0.95 + H * 0.095 + extra * 0.30
    out.append(text(m - s1 * 0.04, y1, "Decide,", s1, C["jev_on_dark"], weight=800, ls=-0.03 * s1))
    s2 = s1 * 0.60
    y2 = y1 + s2 * 1.18
    out.append(text(m - s2 * 0.03, y2, "Don’t", s2, C["text_on_dark"], weight=800, ls=-0.025 * s2))
    # "Generate" comes apart into the tokens an LLM would write it with, drifting and fading
    y3 = y2 + s2 * 1.10
    toks = [("Gen", 0, 0, 0.0), ("er", s2 * 0.10, -s2 * 0.10, 0.18), ("ate", s2 * 0.24, -s2 * 0.26, 0.38)]
    x, last = m - s2 * 0.03, None
    for tok, dx, dy, fade in toks:
        w = measure(tok, s2, "Inter", 800, ls=-0.025 * s2)
        bx, by = x + dx, y3 + dy
        out.append(rect(bx - s2 * 0.06, by - s2 * 0.80, w + s2 * 0.12, s2 * 1.0, "none", rx=s2 * 0.10,
                        stroke=mix(C["llm_on_dark"], BG, 0.55 + fade * 0.6), sw=max(1.0, s2 * 0.018)))
        out.append(text(bx, by, tok, s2, mix(C["llm_on_dark"], BG, fade), weight=800, ls=-0.025 * s2))
        x += w + s2 * 0.14
        last = (bx + w, by - s2 * 0.80)
    # the rest of the generation keeps drifting off "ate", up and back towards "Don't", smaller and fainter
    trail = ["ated", "the", "likely", "Sure", "!", "it", "seems", "\u2026"]
    rnd = random.Random(5)
    x0, y0 = last[0], last[1] - s2 * 0.20                 # just above the right end of "ate"
    x1, y1_ = W * 0.43, y2 - s2 * 0.62                    # the space right of "Don't"
    cur = x0
    for i, tok in enumerate(trail):
        size = s2 * (0.215 - i * 0.011)
        fade = 0.42 + i * 0.062
        w = measure(tok, size, "JetBrains Mono", 500)
        right = cur
        left = right - w
        if left < x1:
            break
        t_ = (x0 - (left + right) / 2) / (x0 - x1)
        ty = y0 + (y1_ - y0) * t_ + rnd.uniform(-0.12, 0.12) * s2
        out.append(rect(left - size * 0.3, ty - size * 0.95, w + size * 0.6, size * 1.35, "none", rx=size * 0.25,
                        stroke=mix(C["llm_on_dark"], BG, min(0.92, fade + 0.14)), sw=0.8))
        out.append(text(left, ty, tok, size, mix(C["llm_on_dark"], BG, fade), family="JetBrains Mono", weight=500))
        cur = left - size * (0.75 + rnd.random() * 0.5)
    # the three doors: a decision ends in an action
    by = y3 + s2 * 0.62
    out += zone_bar(m, by, tw, H * 0.011, label_fill=C["faint_on_dark"], size=W * 0.017)
    ss = W * 0.044
    sy = by + H * 0.125 + extra * 0.25
    for i, s in enumerate(SUB_LINES):
        out.append(text(m, sy + i * ss * 1.30, s, ss, C["sub_on_dark"], weight=500))
    out.append(text(m, H - m * 1.62, strap, W * 0.0195, C["faint_on_dark"], family="JetBrains Mono"))
    out.append(text(m, H - m * 0.9, AUTHOR, W * 0.036, C["text_on_dark"], weight=600, ls=W * 0.0006))
    return "\n".join(out)


# ---------------------------------------------------------------- spine
def spine(sw, H, wr: Wrap):
    """Title and author reading top to bottom (letter tops toward the front), kept 1/16 in off each spine edge."""
    out = [rect(0, 0, sw, H, BG)]
    if not wr.spine_text_ok():
        return "\n".join(out)
    edge_gap = 0.0625 * PT
    cap = 0.727                                         # Inter's cap height, as a share of the font size
    size = min(18.0, (sw - 2 * edge_gap - 0.06 * PT) / (cap * 1.18))
    top, bottom = 0.45 * PT, H - 0.45 * PT
    cy = sw / 2
    g = [f'<g transform="translate({cy + size * cap / 2:.2f},{top:.2f}) rotate(90)">']
    d = measure("Decide, ", size, "Inter", 800)
    g.append(text(0, 0, "Decide,", size, C["jev_on_dark"], weight=800))
    g.append(text(d, 0, "Don’t Generate", size, C["text_on_dark"], weight=800))
    g.append("</g>")
    a = size * 0.72
    alen = measure(AUTHOR, a, "Inter", 600)
    mark = 0.34 * PT
    g.append(f'<g transform="translate({cy + a * cap / 2:.2f},{bottom - mark - 0.2 * PT - alen:.2f}) rotate(90)">')
    g.append(text(0, 0, AUTHOR, a, C["sub_on_dark"], weight=600))
    g.append("</g>")
    # a small imprint mark: the act / review / escalate bar, standing on end
    bw = max(3.0, sw * 0.14)
    yy = bottom - mark
    for share, col in ((0.56, C["act"]), (0.30, C["review"]), (0.14, C["escalate"])):
        g.append(rect(cy - bw / 2, yy, bw, mark * share - 1.2, col, rx=bw / 2))
        yy += mark * share
    return "\n".join(out + g)


# ---------------------------------------------------------------- back
HOOK = ["Most of what an AI agent does", "isn’t writing. It’s deciding."]
BLURB = [
    "Is this alert real? Which team gets this ticket? Is this action safe? Most agents hand every one of those "
    "small decisions to a large language model, then dig the answer out of a paragraph. It works, slowly and "
    "expensively, and the model sounds just as sure when it’s wrong.",
    "This book shows you a better way to build the decision layer. You’ll get probabilities you can trust, "
    "lines drawn from what each mistake costs, and a clear rule for when to hand a case to a person. Every step is "
    "built with runnable code, on a synthetic but realistic security team, using Jev, a new System One model, and "
    "a free mock that needs no API key.",
]
LEARN = [
    "Check whether a model’s probabilities mean what they say, and fix them when they don’t",
    "Turn a probability into act, review or escalate, with lines drawn from real costs and real capacity",
    "Run a fair six-way bake-off: rules, logistic regression, a text classifier, two LLM methods and Jev",
    "Build a hybrid agent in which Jev decides and the LLM reads and writes",
    "Build your own small System One model, with typed heads and calibration built in",
]
FOR_LINE = "For students, engineers building agents, and tech leads deciding what to build."
CATEGORY = "Artificial Intelligence / Machine Learning"


def case_study():
    r = json.loads((ROOT / "results" / "ch25.json").read_text())
    return r["old"]["threats_seen_share"], r["new"]["threats_seen_share"], 6


def qr_svg(x, y, size, url, dark, light):
    q = segno.make(url, error="m")
    mat = list(q.matrix)
    n = len(mat)
    cell = size / n
    parts = [rect(x - cell * 2, y - cell * 2, size + cell * 4, size + cell * 4, light, rx=cell)]
    for r_, row in enumerate(mat):
        run = None
        for c_, v in enumerate(list(row) + [0]):
            if v and run is None:
                run = c_
            elif not v and run is not None:
                parts.append(rect(x + run * cell, y + r_ * cell, (c_ - run) * cell + 0.05, cell + 0.05, dark))
                run = None
    return "\n".join(parts)


def back(W, H, wr: Wrap):
    m = 0.56 * PT
    tw = W - 2 * m
    out = [rect(0, 0, W, H, BG)]
    y = m + 0.30 * PT
    hs = min(fit(HOOK[0], tw, "Inter", 800), fit(HOOK[1], tw, "Inter", 800), 25.0)
    out.append(text(m, y + hs * 0.8, HOOK[0], hs, C["text_on_dark"], weight=800, ls=-0.01 * hs))
    y += hs * 0.8 + hs * 1.18
    split = HOOK[1].index("It’s")
    out.append(text(m, y, HOOK[1][:split], hs, C["text_on_dark"], weight=800, ls=-0.01 * hs))
    out.append(text(m + measure(HOOK[1][:split], hs, "Inter", 800, ls=-0.01 * hs), y, HOOK[1][split:], hs,
                    C["jev_on_dark"], weight=800, ls=-0.01 * hs))
    # the blurb
    bs, lh = 10.6, 15.0
    y += hs * 0.95
    for para in BLURB:
        for ln in wrap_lines(para, tw, bs, "Source Serif 4", 400):
            y += lh
            out.append(text(m, y, ln, bs, BODY, family="Source Serif 4"))
        y += lh * 0.45
    # the praise slot, left empty for real quotes only
    y += 6
    ph = 30
    out.append(rect(m, y, tw, ph, "none", rx=4, stroke=mix(C["faint_on_dark"], BG, 0.35), sw=0.8,
                    extra='stroke-dasharray="3 3"'))
    out.append(text(m + tw / 2, y + ph / 2 + 3.2, "[[PRAISE]]", 8.5, C["faint_on_dark"], family="JetBrains Mono",
                    anchor="middle"))
    y += ph + 22
    # two columns: what you'll learn, and one result from the book
    colw = tw * 0.60
    out.append(text(m, y, "Inside, you’ll learn to:", 10.5, C["jev_on_dark"], weight=700))
    ly = y + 4
    ls_, llh = 9.3, 12.6
    for item in LEARN:
        lines = wrap_lines(item, colw - 12, ls_, "Inter", 400)
        ly += llh * 0.35
        for k, ln in enumerate(lines):
            ly += llh
            if k == 0:
                out.append(circle(m + 3, ly - ls_ * 0.33, 1.9, C["jev_on_dark"]))
            out.append(text(m + 12, ly, ln, ls_, BODY))
    # the case-study card
    cx, cw = m + colw + 0.20 * PT, tw - colw - 0.20 * PT
    before, after, analysts = case_study()
    ch = 118
    out.append(rect(cx, y - 12, cw, ch, C["night2"], rx=5))
    ix, iw = cx + 11, cw - 22
    out.append(text(ix, y + 6, "Real threats seen by a person", 8.4, C["text_on_dark"], weight=600))
    out.append(text(ix, y + 17, f"same {['', 'one', 'two', 'three', 'four', 'five', 'six'][analysts]} analysts",
                    7.6, C["faint_on_dark"]))
    for k, (lab, val, col) in enumerate((("before", before, C["faint_on_dark"]), ("after", after, C["jev_on_dark"]))):
        by = y + 36 + k * 27
        out.append(text(ix, by, lab, 7.6, C["sub_on_dark"], family="JetBrains Mono"))
        out.append(rect(ix, by + 4, iw, 7, mix(col, C["night2"], 0.78), rx=3.5))
        out.append(rect(ix, by + 4, iw * val, 7, col, rx=3.5))
        out.append(text(ix + iw, by, f"{val:.0%}", 9.5, col, weight=700, anchor="end"))
    out.append(text(ix, y + ch - 20, "From the book’s synthetic", 6.8, C["faint_on_dark"], style="italic"))
    out.append(text(ix, y + ch - 11.5, "case study (Chapter 18)", 6.8, C["faint_on_dark"], style="italic"))
    y = max(ly, y + ch - 12) + 20
    out.append(text(m, y, FOR_LINE, 9.3, C["sub_on_dark"], weight=500))
    y += 16
    out.append(line(m, y, m + tw, y, mix(C["faint_on_dark"], BG, 0.55), 0.6))
    # about the author
    y += 14
    photo = 46
    out.append(rect(m, y, photo, photo, "none", rx=3, stroke=mix(C["faint_on_dark"], BG, 0.3), sw=0.8,
                    extra='stroke-dasharray="2 2"'))
    out.append(text(m + photo / 2, y + photo / 2 - 1, "[[AUTHOR", 5.4, C["faint_on_dark"], family="JetBrains Mono",
                    anchor="middle"))
    out.append(text(m + photo / 2, y + photo / 2 + 6, "PHOTO]]", 5.4, C["faint_on_dark"], family="JetBrains Mono",
                    anchor="middle"))
    ax = m + photo + 12
    out.append(text(ax, y + 9, "About the author", 9.0, C["text_on_dark"], weight=700))
    out.append(text(ax, y + 22, f"{AUTHOR} [[AUTHOR BIO]]", 8.6, BODY))
    out.append(text(ax, y + 36, EMAIL, 8.0, C["sub_on_dark"], family="JetBrains Mono"))
    # bottom row: QR, category and price; the barcode box on the right stays empty
    qs = 0.62 * PT
    qy = H - (0.25 * PT + 0.12 * PT) - qs - 11
    out.append(qr_svg(m, qy, qs, REPO_URL, BG, C["text_on_dark"]))
    out.append(text(m - 2, qy + qs + 12, REPO_LABEL, 6.3, C["sub_on_dark"], family="JetBrains Mono"))
    kx = m + qs + 0.28 * PT
    out.append(text(kx, qy + 8, "Labs, figures and code", 7.6, C["text_on_dark"], weight=600))
    out.append(text(kx, qy + 19, "Scan for the companion repository", 7.2, C["faint_on_dark"]))
    out.append(text(kx, qy + qs - 12, CATEGORY, 7.6, C["sub_on_dark"], weight=600))
    out.append(text(kx, qy + qs - 1, "[[PRICE INR]]  \u00b7  [[PRICE USD]]", 7.6, C["sub_on_dark"],
                    family="JetBrains Mono"))
    return "\n".join(out)


# ---------------------------------------------------------------- guides layer
def barcode_box(wr: Wrap):
    """KDP places the barcode 0.25 in inside the back cover's bottom-right corner (on the spine side): 2 x 1.2 in."""
    bw, bh = 2.0 * PT, 1.2 * PT
    x = (wr.back_x + wr.panel_w) * PT - 0.25 * PT - bw
    if wr.kind == "hardcover":
        x -= wr.hinge * PT
    y = (wr.top_y + wr.panel_h) * PT - 0.25 * PT - bh
    return x, y, bw, bh


def guides(wr: Wrap):
    W, H = wr.width * PT, wr.height * PT
    cy, mg, yl, gy = "#00A6D6", "#E0198A", "#E0B000", "#7F8C99"
    g = ['<g id="guides" font-family="JetBrains Mono">']
    e = wr.edge * PT
    # trim (paperback) or board edge (hardcover): where the cover folds or is cut
    g.append(rect(e, e, W - 2 * e, H - 2 * e, "none", stroke=cy, sw=0.6))
    for xs in (wr.spine_x, wr.front_x):
        g.append(line(xs * PT, 0, xs * PT, H, cy, 0.6))
    # spine text zone: 1/16 in off each spine edge
    si = 0.0625 * PT
    g.append(rect(wr.spine_x * PT + si, e, wr.spine * PT - 2 * si, H - 2 * e, "none", stroke=mg, sw=0.5,
                  extra='stroke-dasharray="2 2"'))
    # safe areas: text and faces at least 0.25 in inside the trim (and outside the hinge on a hardcover)
    s = wr.safe * PT
    hinge = wr.hinge * PT if wr.kind == "hardcover" else 0
    g.append(rect(wr.back_x * PT + s, e + s, wr.panel_w * PT - 2 * s - hinge, wr.panel_h * PT - 2 * s, "none",
                  stroke=mg, sw=0.5, extra='stroke-dasharray="4 3"'))
    g.append(rect(wr.front_x * PT + s + hinge, e + s, wr.panel_w * PT - 2 * s - hinge, wr.panel_h * PT - 2 * s,
                  "none", stroke=mg, sw=0.5, extra='stroke-dasharray="4 3"'))
    if wr.kind == "hardcover":
        for hx in (wr.spine_x * PT - hinge, wr.front_x * PT):
            g.append(rect(hx, e, hinge, H - 2 * e, "none", stroke=gy, sw=0.5, extra='stroke-dasharray="1 2"'))
        g.append(text(wr.front_x * PT + 3, e + 12, "hinge", 6, gy))
    x, y, bw, bh = barcode_box(wr)
    g.append(rect(x, y, bw, bh, "#FFF6CC", stroke=yl, sw=0.8))
    g.append(text(x + bw / 2, y + bh / 2 - 4, "BARCODE AREA", 8, "#6B5800", anchor="middle"))
    g.append(text(x + bw / 2, y + bh / 2 + 8, "2 x 1.2 in, keep clear", 6.5, "#6B5800", anchor="middle"))
    lbl = f"{wr.kind}  {wr.width:.4f} x {wr.height:.4f} in  spine {wr.spine:.4f} in  {wr.pages} pages  {wr.paper}"
    g.append(text(e + 4, e - 3 if e > 9 else H - 3, lbl, 6.5, cy))
    g.append("</g>")
    return "\n".join(g)


def wrap_svg(wr: Wrap, strap, with_guides=False):
    W, H = wr.width * PT, wr.height * PT
    e = wr.edge * PT
    parts = [rect(0, 0, W, H, BG)]                    # the ground runs through bleed/wrap, spine and both panels
    pw, ph = wr.panel_w * PT, wr.panel_h * PT
    hinge = wr.hinge * PT if wr.kind == "hardcover" else 0
    # back: laid out on the panel minus the hinge, so no text sits on the fold
    parts.append(f'<g transform="translate({e:.2f},{e:.2f})"><svg width="{pw - hinge:.2f}" height="{ph:.2f}" '
                 f'overflow="visible">{back(pw - hinge, ph, wr)}</svg></g>')
    parts.append(f'<g transform="translate({wr.spine_x * PT:.2f},{e:.2f})">{spine(wr.spine * PT, ph, wr)}</g>')
    parts.append(f'<g transform="translate({wr.front_x * PT + hinge:.2f},{e:.2f})"><svg width="{pw - hinge:.2f}" '
                 f'height="{ph:.2f}" overflow="visible">{front(pw - hinge, ph, strap)}</svg></g>')
    if with_guides:
        parts.append(guides(wr))
    return svg_doc(round(wr.width, 4), round(wr.height, 4), "\n".join(parts))


# ---------------------------------------------------------------- outputs
def build_wraps(strap):
    pages = interior_pages()
    wraps = {"paperback": Wrap("paperback", pages=pages, paper=PAPERBACK_PAPER),
             "hardcover": Wrap("hardcover", pages=pages, paper=HARDCOVER_PAPER)}
    report = {}
    for name, wr in wraps.items():
        for g in (False, True):
            svg = wrap_svg(wr, strap, with_guides=g)
            stem = f"cover-{name}" + ("-guides" if g else "")
            (COVER / "src" / f"{stem}.svg").write_text(svg)
            to_pdf(svg, COVER / "print" / f"{stem}.pdf", round(wr.width, 4), round(wr.height, 4))
            px_w = 1800
            to_png(svg, COVER / "print" / f"{stem}-preview.png", px_w, round(px_w * wr.height / wr.width))
        report[name] = wr.summary()
    (COVER / "print" / "dimensions.json").write_text(json.dumps(report, indent=2) + "\n")
    return wraps, report


def build_ebook(strap):
    W, H = 7 * PT, 7 * PT * 2560 / 1600
    svg = svg_doc(7, round(7 * 2560 / 1600, 4), front(W, H, strap))
    (COVER / "src" / "ebook-front.svg").write_text(svg)
    png = COVER / "src" / "_ebook.png"
    to_png(svg, png, 1600, 2560)
    from PIL import Image
    Image.open(png).convert("RGB").save(COVER / "ebook" / "cover.jpg", quality=92, subsampling=0, dpi=(300, 300))
    png.unlink()


def front_png(strap, width_px=1400):
    svg = svg_doc(7, 10, front(7 * PT, 10 * PT, strap))
    (COVER / "src" / "front.svg").write_text(svg)
    out = COVER / "src" / "front.png"
    to_png(svg, out, width_px, round(width_px * 10 / 7))
    return out


def main():
    strap = strapline()
    wraps, report = build_wraps(strap)
    build_ebook(strap)
    front_png(strap)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
