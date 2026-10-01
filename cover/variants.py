"""The front cover: v0 (the first release's front, kept as the fallback) and three refinements of it.

python cover/variants.py  -> cover/concepts/v{0,1,2,3}-front.svg/.png, thumbnails at 150 and 80 px, greyscale
                             versions, variants.json (the test numbers) and compare.png (all four side by side)

All four keep the typographic title: green "Decide,", white "Don't", orange "Generate" split into token boxes. The
refinements replace v0's purple act / review / escalate bar with one picture of the book: many small orange token
fragments drift away from "Generate", get smaller and fainter, and stop at one thin green line; one solid green
typed answer comes out the other side. Only the dark ground, green, orange, and white or grey are used.

  v1  the fragments flow left to right into a vertical gate; the answer sits to its right
  v2  the fragments fall from "Generate" onto a horizontal line; the answer sits below it
  v3  the minimal one: three fragments, a short gate and the answer
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from coverlib import AUTHOR, C, COVER, PT, contrast, fit, line, luminance, measure, mix, rect, strapline, svg_doc  # noqa
from coverlib import text, to_png  # noqa: E402
from concepts import SUB_LINES, zone_bar  # noqa: E402

BG = C["night"]
GREEN, ORANGE = C["jev_on_dark"], C["llm_on_dark"]
CHIP = "attack 0.03 → act"         # the one typed answer: P(attack) and the action it leads to
MONO = "JetBrains Mono"


# ---------------------------------------------------------------- v0: the first release's front, unchanged
def front_v0(W, H, strap):
    m = W * 0.078
    tw = W - 2 * m
    out = [rect(0, 0, W, H, BG)]
    s1 = fit("Decide,", tw, "Inter", 800, ls_em=-0.03)
    extra = max(0.0, H - W * 10 / 7)
    y1 = m + s1 * 0.95 + H * 0.095 + extra * 0.30
    out.append(text(m - s1 * 0.04, y1, "Decide,", s1, GREEN, weight=800, ls=-0.03 * s1))
    s2 = s1 * 0.60
    y2 = y1 + s2 * 1.18
    out.append(text(m - s2 * 0.03, y2, "Don’t", s2, C["text_on_dark"], weight=800, ls=-0.025 * s2))
    y3 = y2 + s2 * 1.10
    toks = [("Gen", 0, 0, 0.0), ("er", s2 * 0.05, -s2 * 0.035, 0.08), ("ate", s2 * 0.10, -s2 * 0.07, 0.16)]
    x, last = m - s2 * 0.03, None
    for tok, dx, dy, fade in toks:
        w = measure(tok, s2, "Inter", 800, ls=-0.025 * s2)
        bx, by = x + dx, y3 + dy
        out.append(rect(bx - s2 * 0.06, by - s2 * 0.80, w + s2 * 0.12, s2 * 1.0, "none", rx=s2 * 0.10,
                        stroke=mix(ORANGE, BG, 0.30 + fade * 1.2), sw=max(1.0, s2 * 0.022)))
        out.append(text(bx, by, tok, s2, mix(ORANGE, BG, fade), weight=800, ls=-0.025 * s2))
        x += w + s2 * 0.13
        last = (bx + w + s2 * 0.06, by)
    fx, fy = last[0] + s2 * 0.13, last[1] - s2 * 0.46
    for i, tok in enumerate(["ne", "ra", "te"]):
        size = s2 * (0.22 - i * 0.025)
        w = measure(tok, size, MONO, 500)
        if fx + w + size * 0.3 > W - m:
            break
        out.append(rect(fx - size * 0.3, fy - size * 0.95, w + size * 0.6, size * 1.35, "none", rx=size * 0.25,
                        stroke=mix(ORANGE, BG, 0.62 + i * 0.08), sw=0.8))
        out.append(text(fx, fy, tok, size, mix(ORANGE, BG, 0.50 + i * 0.08), family=MONO, weight=500,
                        extra='class="frag"'))
        fx += w * 0.55 + size * 0.35
        fy += s2 * 0.31
    by = y3 + s2 * 0.95 + extra * 0.08
    out += zone_bar(m, by, tw, H * 0.012, label_fill=C["faint_on_dark"], size=W * 0.018)
    ss = W * 0.052
    sy = by + H * 0.145 + extra * 0.22
    for i, s in enumerate(SUB_LINES):
        out.append(text(m, sy + i * ss * 1.28, s, ss, C["sub_on_dark"], weight=500))
    out.append(text(m, H - m * 1.62, strap, W * 0.0195, C["faint_on_dark"], family=MONO))
    out.append(text(m, H - m * 0.9, AUTHOR, W * 0.036, C["text_on_dark"], weight=600, ls=W * 0.0006))
    return "\n".join(out)


# ---------------------------------------------------------------- shared parts of v1 to v3
def calibration_grid(W, H, opacity=0.05):
    """A fine grid with one diagonal (a reliability diagram's 'perfectly calibrated' line), barely there."""
    col = mix(C["text_on_dark"], BG, 1 - opacity)
    step = W / 24
    out = ['<g class="grid">']
    for i in range(1, 24):
        out.append(line(i * step, 0, i * step, H, col, 0.35))
    j = 1
    while j * step < H:
        out.append(line(0, H - j * step, W, H - j * step, col, 0.35))
        j += 1
    out.append(line(0, H, W, H - W * 1.0, mix(C["text_on_dark"], BG, 1 - opacity * 1.25), 0.6))
    out.append("</g>")
    return out


def title(W, H, m, top):
    """The title, its cap top at `top`. Returns the parts, the boxes of the three "Generate" tokens
    (x0, y0, x1, y1) and the y of the title block's bottom edge."""
    tw = W - 2 * m
    s1 = fit("Decide,", tw, "Inter", 800, ls_em=-0.03)
    out = []
    y1 = top + s1 * 0.727
    out.append(text(m - s1 * 0.04, y1, "Decide,", s1, GREEN, weight=800, ls=-0.03 * s1))

    def gen_width(s2):
        x = 0.0
        for tok in ("Gen", "er", "ate"):
            x += measure(tok, s2, "Inter", 800, ls=-0.025 * s2) + s2 * 0.13
        return x - s2 * 0.13 + s2 * 0.10 + s2 * 0.06
    s2 = s1 * 0.70
    while gen_width(s2) > tw * 0.97:
        s2 *= 0.99
    y2 = y1 + s2 * 1.24
    out.append(text(m - s2 * 0.03, y2, "Don’t", s2, C["text_on_dark"], weight=800, ls=-0.025 * s2))
    y3 = y2 + s2 * 1.15
    toks = [("Gen", 0, 0, 0.0), ("er", s2 * 0.05, -s2 * 0.035, 0.08), ("ate", s2 * 0.10, -s2 * 0.07, 0.16)]
    x, boxes = m - s2 * 0.03, []
    for tok, dx, dy, fade in toks:
        w = measure(tok, s2, "Inter", 800, ls=-0.025 * s2)
        bx, by = x + dx, y3 + dy
        box = (bx - s2 * 0.06, by - s2 * 0.80, bx + w + s2 * 0.06, by + s2 * 0.20)
        out.append(rect(box[0], box[1], box[2] - box[0], box[3] - box[1], "none", rx=s2 * 0.10,
                        stroke=mix(ORANGE, BG, 0.30 + fade * 1.2), sw=max(1.0, s2 * 0.022)))
        out.append(text(bx, by, tok, s2, mix(ORANGE, BG, fade), weight=800, ls=-0.025 * s2,
                        extra='class="gen"'))
        boxes.append(box)
        x += w + s2 * 0.13
    return out, boxes, max(b[3] for b in boxes), s2


def fragment(x, y, tok, size, fade):
    """One token fragment: an orange outlined box with the token in mono; (x, y) is the text baseline start.
    Returns the parts and the box."""
    w = measure(tok, size, MONO, 500)
    px, py = size * 0.30, size * 0.95
    box = (x - px, y - py, x + w + px, y - py + size * 1.35)
    return ([rect(box[0], box[1], box[2] - box[0], box[3] - box[1], "none", rx=size * 0.25,
                  stroke=mix(ORANGE, BG, min(0.92, fade + 0.12)), sw=max(0.5, size * 0.06)),
             text(x, y, tok, size, mix(ORANGE, BG, fade), family=MONO, weight=500, extra='class="frag"')], box)


def chip(x, y, size, anchor="start"):
    """The one typed answer: solid green, dark mono text. (x, y) is the box's top-left (or top-right for 'end').
    Returns the parts and the box."""
    w = measure(CHIP, size, MONO, 700)
    pw, h = size * 0.75, size * 1.85
    bw = w + 2 * pw
    if anchor == "end":
        x -= bw
    return ([rect(x, y, bw, h, GREEN, rx=size * 0.38),
             text(x + pw, y + h / 2 + size * 0.36, CHIP, size, BG, family=MONO, weight=700, extra='class="chip"')],
            (x, y, x + bw, y + h))


def chip_width(size):
    return measure(CHIP, size, MONO, 700) + 1.5 * size


def gate(x1, y1, x2, y2, sw):
    """The thin green line the fragments stop at, with a small dot at each end so it reads as a gate."""
    return [line(x1, y1, x2, y2, GREEN, sw),
            f'<circle cx="{x1:.2f}" cy="{y1:.2f}" r="{sw * 1.6:.2f}" fill="{GREEN}"/>',
            f'<circle cx="{x2:.2f}" cy="{y2:.2f}" r="{sw * 1.6:.2f}" fill="{GREEN}"/>']


def lower(W, H, m, motif_bottom, strap):
    """Subtitle, strap line and author. The subtitle sits so the space above it (from the motif) and below it (to
    the strap line) are in a fixed 2 : 3 ratio, which keeps the bottom of the cover from looking left over."""
    out = []
    ss = W * 0.050
    sub_h = ss * 0.727 + ss * 1.30              # cap top of line 1 to the baseline of line 2
    a_size = W * 0.044
    ay = H - m * 0.92                            # the author's baseline
    st_size = W * 0.0195
    sty = ay - a_size * 1.55                     # the strap line's baseline
    free = (sty - st_size * 0.75) - motif_bottom - sub_h
    top = motif_bottom + free * 0.40
    y = top + ss * 0.727
    for i, s in enumerate(SUB_LINES):
        out.append(text(m, y + i * ss * 1.30, s, ss, C["sub_on_dark"], weight=500))
    out.append(text(m, sty, strap, st_size, C["faint_on_dark"], family=MONO))
    out.append(text(m, ay, AUTHOR, a_size, C["text_on_dark"], weight=700, ls=W * 0.0004))
    return out


def _layout(W, H):
    m = W * 0.078
    extra = max(0.0, H - W * 10 / 7)             # a taller canvas (the ebook) spreads its extra height through it
    return m, extra, H * 0.125 + extra * 0.30


# ---------------------------------------------------------------- v1: left to right, vertical gate, answer right
V1_FRAGS = [  # token, progress toward the gate (0..1), lane (-1 top .. 1 bottom)
    ("the", 0.00, -0.75), ("ne", 0.03, 0.80), ("is", 0.17, 0.02), ("ra", 0.29, -0.80), ("0.", 0.36, 0.78),
    ("te", 0.50, -0.20), ("the", 0.61, 0.55), ("\u2026", 0.73, -0.50), ("ra", 0.82, 0.22), ("is", 0.92, -0.12),
]


def hits(a, b, pad):
    return not (a[2] + pad <= b[0] or b[2] + pad <= a[0] or a[3] + pad <= b[1] or b[3] + pad <= a[1])


def front_v1(W, H, strap):
    m, extra, top = _layout(W, H)
    out = [rect(0, 0, W, H, BG)] + calibration_grid(W, H)
    parts, gen, bottom, s2 = title(W, H, m, top)
    out += parts
    cs = W * 0.030
    band_top, band_h = bottom + H * 0.045 + extra * 0.06, H * 0.105
    cy = band_top + band_h / 2
    gx = W - m - chip_width(cs) - W * 0.035
    x0, placed = m + W * 0.004, []
    for tok, t, lane in V1_FRAGS:
        while True:                              # step along the stream until the piece is clear of the others
            size = s2 * (0.21 - 0.12 * t)
            x = x0 + t * (gx - x0 - W * 0.045)
            y = cy + lane * (band_h / 2 - size * 0.55) * (1 - 0.60 * t) + size * 0.36
            p, box = fragment(x, y, tok, size, 0.15 + 0.62 * t)
            if not any(hits(box, b, W * 0.008) for b in placed):
                break
            t += 0.01
        placed.append(box)
        out += p
    gh = band_h * 0.66
    out += gate(gx, cy - gh / 2, gx, cy + gh / 2, max(1.0, W * 0.0028))
    out += chip(W - m, cy - cs * 1.85 / 2, cs, anchor="end")[0]
    out += lower(W, H, m, band_top + band_h, strap)
    return "\n".join(out)


# ---------------------------------------------------------------- v2: falling from "Generate", horizontal line
V2_FRAGS = [  # token, which Generate token it falls from (0..2), horizontal position in it (0..1), progress (0..1)
    ("ne", 0, 0.25, 0.10), ("the", 0, 0.80, 0.42), ("is", 0, 0.35, 0.78),
    ("ra", 1, 0.30, 0.18), ("0.", 1, 0.75, 0.62),
    ("te", 2, 0.20, 0.08), ("…", 2, 0.65, 0.35), ("the", 2, 0.35, 0.70), ("ra", 2, 0.85, 0.90),
]


def front_v2(W, H, strap):
    m, extra, top = _layout(W, H)
    out = [rect(0, 0, W, H, BG)] + calibration_grid(W, H)
    parts, gen, bottom, s2 = title(W, H, m, top)
    out += parts
    ly = bottom + H * 0.115 + extra * 0.06       # the green line
    fall0 = bottom + H * 0.020
    cs = W * 0.030
    cw = chip_width(cs)
    target = m + cw / 2                          # the fragments drift toward the answer as they fall
    for tok, k, u, t in V2_FRAGS:
        x0g, _, x1g, _ = gen[k]
        size = s2 * (0.24 - 0.14 * t)
        fade = 0.20 + 0.62 * t
        sx = x0g + u * (x1g - x0g)
        x = sx + (target - sx) * t * 0.35 - measure(tok, size, MONO, 500) / 2
        y = fall0 + t * (ly - fall0 - size * 0.9) + size * 0.95
        out += fragment(x, y, tok, size, fade)[0]
    out += gate(m, ly, W - m, ly, max(1.0, W * 0.0028))
    cy = ly + H * 0.022
    out += chip(m, cy, cs)[0]
    out += lower(W, H, m, cy + cs * 1.85, strap)
    return "\n".join(out)


# ---------------------------------------------------------------- v3: minimal
def front_v3(W, H, strap):
    m, extra, top = _layout(W, H)
    out = [rect(0, 0, W, H, BG)] + calibration_grid(W, H)
    parts, gen, bottom, s2 = title(W, H, m, top)
    out += parts
    cs = W * 0.030
    cy = bottom + H * 0.085 + extra * 0.06      # the row's centre line
    x = m
    for i, tok in enumerate(("ne", "ra", "te")):
        size = s2 * (0.22 - 0.045 * i)
        fade = 0.22 + 0.22 * i
        parts_, box = fragment(x + size * 0.30, cy + size * 0.36, tok, size, fade)
        out += parts_
        x = box[2] + W * 0.022
    gx = x + W * 0.012
    gh = cs * 2.6
    out += gate(gx, cy - gh / 2, gx, cy + gh / 2, max(1.0, W * 0.0028))
    out += chip(gx + W * 0.034, cy - cs * 1.85 / 2, cs)[0]
    out += lower(W, H, m, cy + gh / 2, strap)
    return "\n".join(out)


FRONTS = {"v0": front_v0, "v1": front_v1, "v2": front_v2, "v3": front_v3}


# ---------------------------------------------------------------- tests and the comparison sheet
def title_share(W=7 * PT, H=10 * PT):
    """The title block's height (cap top of "Decide," to the bottom of the "Generate" boxes) as a share of H."""
    m, extra, top = _layout(W, H)
    _, _, bottom, _ = title(W, H, m, top)
    return (bottom - top) / H


def v0_title_share(W=7 * PT, H=10 * PT):
    m = W * 0.078
    s1 = fit("Decide,", W - 2 * m, "Inter", 800, ls_em=-0.03)
    y1 = m + s1 * 0.95 + H * 0.095
    s2 = s1 * 0.60
    bottom = y1 + s2 * 1.18 + s2 * 1.10 + s2 * 0.20
    return (bottom - (y1 - s1 * 0.727)) / H


def main():
    from PIL import Image, ImageDraw, ImageFont
    d = COVER / "concepts"
    strap = strapline()
    W, H = 7 * PT, 10 * PT
    report = {}
    imgs = {}
    for key, fn in FRONTS.items():
        svg = svg_doc(7, 10, fn(W, H, strap))
        (d / f"{key}-front.svg").write_text(svg)
        png = d / f"{key}-front.png"
        to_png(svg, png, 1400, 2000)
        im = Image.open(png).convert("RGB")
        imgs[key] = im
        for px in (150, 80):
            t = im.resize((px, round(px * 10 / 7)), Image.LANCZOS)
            t.save(d / f"{key}-thumb{px}.png")
            t.convert("L").save(d / f"{key}-thumb{px}-grey.png")
        im.convert("L").save(d / f"{key}-grey.png")
        report[key] = {"title_share_of_height": round(v0_title_share() if key == "v0" else title_share(), 3)}
    grey = lambda h: round(luminance(h) ** (1 / 2.2) * 255)  # noqa: E731  (approximate L of the sRGB colour)
    report["contrast_vs_ground"] = {k: round(contrast(v, BG), 2) for k, v in {
        "title green": GREEN, "title white": C["text_on_dark"], "Generate orange": ORANGE,
        "subtitle": C["sub_on_dark"], "strap line": C["faint_on_dark"], "author": C["text_on_dark"]}.items()}
    report["contrast_chip_text_on_green"] = round(contrast(BG, GREEN), 2)
    report["v0_zone_labels"] = round(contrast(C["faint_on_dark"], BG), 2)
    for k in FRONTS:
        report[k]["five_second_test"] = FIVE_SECONDS[k]
    report["fragments_note"] = ("the fading token fragments are decoration (WCAG 1.4.3's exception for pure "
                                "decoration); every piece of text that carries meaning is listed above")
    report["greyscale_levels"] = {"green": grey(GREEN), "orange": grey(ORANGE), "ground": grey(BG)}
    (d / "variants.json").write_text(json.dumps(report, indent=2) + "\n")
    compare(imgs, d / "compare.png")
    print(json.dumps(report, indent=2))


NOTES = {
    "v0": "current: purple bar, a second idea",
    "v1": "stream \u2192 gate \u2192 answer, left to right",
    "v2": "falls from Generate onto a line",
    "v3": "minimal: three fragments, gate, answer",
}
# the 5-second test: one sentence from the cover alone, written after looking at each render
FIVE_SECONDS = {
    "v0": "Decide, don't generate, and something with three purple zones. (Passes on the title; the bar is a "
          "second idea that needs the book to explain it.)",
    "v1": "Lots of generated text goes in, one clean answer comes out: LLMs generate, this book is about deciding. "
          "(Passes.)",
    "v2": "Generated pieces fall onto a line and one answer sits below it. (Passes, but the full-width line also "
          "reads as a plain divider.)",
    "v3": "Decide, don't generate, with a small answer chip. (Passes on the title; three pieces don't say "
          "'lots of text'.)",
}
VERDICT = [
    "Strongest: v1. It reads in the order the eye moves, left to right: many fading orange pieces, one green gate,",
    "one solid green answer, which is the book in one picture. The title is still read first at 150 and 80 px, and",
    "at 80 px the motif shrinks to a faint speckle and a green bar rather than clutter. v2 tells the same story, but",
    "its full-width line reads as a divider. v3 is the cleanest, but at thumbnail size it no longer says 'lots of",
    "text in'. Greyscale: the green and the orange have the same grey (both about 165 of 255), in every version,",
    "so they separate by shape, not tone: solid 'Decide,' and a solid answer against hollow, boxed, fading tokens.",
]


def compare(imgs, out):
    """All four side by side at full size, then at 150 px and 80 px wide, colour and greyscale, with notes."""
    from PIL import Image, ImageDraw, ImageFont
    font = lambda w, s: ImageFont.truetype(str(COVER.parent / "assets" / "fonts" / w), s)  # noqa: E731
    big, small, mono = font("Inter-Bold.ttf", 34), font("Inter-Regular.ttf", 22), font("JetBrainsMono-Regular.ttf", 20)
    keys = list(imgs)
    cw, ch, gap, pad = 560, 800, 40, 60
    thumbs_h = 260
    Wt = pad * 2 + len(keys) * cw + (len(keys) - 1) * gap
    Ht = pad + 50 + ch + 60 + thumbs_h + 40 + len(VERDICT) * 34 + pad
    sheet = Image.new("RGB", (Wt, Ht), "#F4F5F7")
    dr = ImageDraw.Draw(sheet)
    for i, k in enumerate(keys):
        x = pad + i * (cw + gap)
        dr.text((x, pad), k + ("  (fallback)" if k == "v0" else ""), fill="#1F2430", font=big)
        dr.text((x, pad + 42), NOTES[k], fill="#4B5563", font=small)
        sheet.paste(imgs[k].resize((cw, ch), Image.LANCZOS), (x, pad + 80))
        ty = pad + 80 + ch + 30
        t150 = imgs[k].resize((150, 214), Image.LANCZOS)
        t80 = imgs[k].resize((80, 114), Image.LANCZOS)
        sheet.paste(t150, (x, ty))
        sheet.paste(t150.convert("L").convert("RGB"), (x + 160, ty))
        sheet.paste(t80, (x + 320, ty))
        sheet.paste(t80.convert("L").convert("RGB"), (x + 410, ty))
        dr.text((x, ty + 220), "150 px  ·  grey  ·  80 px  ·  grey", fill="#4B5563", font=mono)
    y = pad + 80 + ch + 30 + thumbs_h + 30
    for ln in VERDICT:
        dr.text((pad, y), ln, fill="#1F2430", font=small)
        y += 34
    sheet.save(out, optimize=True)


if __name__ == "__main__":
    main()
