"""Three front-cover concepts, each a function that draws a front panel of any size (in points).

python cover/concepts.py  -> cover/concepts/concept-{a,b,c}.svg/.png, thumbnails, greyscale versions, and a report.
"""
from __future__ import annotations

import json
import math
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from coverlib import (C, AUTHOR, COVER, PT, circle, contrast, fit, line, measure, mix, rect, strapline, svg_doc,  # noqa
                      text, to_png, wrap_lines)

SUB_LINES = ["Jev, System One Models, and the", "Decision Layer of Agentic AI"]


def _footer(W, H, m, ink, sub, faint, strap, sub_size=None):
    """Subtitle, the strap line and the author, shared by all three concepts."""
    out = []
    ss = sub_size or W * 0.034
    y = H * 0.745
    for i, s in enumerate(SUB_LINES):
        out.append(text(m, y + i * ss * 1.32, s, ss, sub, weight=500))
    out.append(text(m, H - m * 1.62, strap, W * 0.0195, faint, family="JetBrains Mono", weight=400))
    out.append(text(m, H - m * 0.9, AUTHOR, W * 0.036, ink, weight=600, ls=W * 0.0006))
    return out


def zone_bar(x, y, w, h, labels=True, label_fill="#8A919C", size=8.0):
    """The act / review / escalate bar: the book's three doors, in its purple ramp."""
    parts = [("act", 0.56, C["act"]), ("review", 0.30, C["review"]), ("escalate", 0.14, C["escalate"])]
    out, cx = [], x
    for name, share, col in parts:
        sw = w * share
        out.append(rect(cx, y, sw - 2, h, col, rx=h / 2))
        if labels:
            out.append(text(cx, y + h + size * 1.6, name, size, label_fill, family="JetBrains Mono"))
        cx += sw
    return out


# ---------------------------------------------------------------- (a) typographic
def front_a(W, H, strap):
    bg, m = C["night"], W * 0.078
    tw = W - 2 * m
    out = [rect(0, 0, W, H, bg)]
    s1 = fit("Decide,", tw, "Inter", 800, ls_em=-0.03)
    y1 = H * 0.285
    out.append(text(m - s1 * 0.04, y1, "Decide,", s1, C["jev_on_dark"], weight=800, ls=-0.03 * s1))
    s2 = s1 * 0.60
    y2 = y1 + s2 * 1.18
    out.append(text(m - s2 * 0.03, y2, "Don\u2019t", s2, C["text_on_dark"], weight=800, ls=-0.025 * s2))
    # "Generate" comes apart into tokens, each boxed as a tokenizer would split it, drifting up and fading
    y3 = y2 + s2 * 1.10
    toks = [("Gen", 0, 0, 0.0), ("er", s2 * 0.10, -s2 * 0.10, 0.18), ("ate", s2 * 0.24, -s2 * 0.26, 0.40)]
    x = m - s2 * 0.03
    last = None
    for tok, dx, dy, fade in toks:
        col = mix(C["llm_on_dark"], bg, fade)
        w = measure(tok, s2, "Inter", 800, ls=-0.025 * s2)
        bx, by = x + dx, y3 + dy
        out.append(rect(bx - s2 * 0.06, by - s2 * 0.80, w + s2 * 0.12, s2 * 1.0, "none", rx=s2 * 0.10,
                        stroke=mix(C["llm_on_dark"], bg, 0.55 + fade * 0.6), sw=max(1.0, s2 * 0.018)))
        out.append(text(bx, by, tok, s2, col, weight=800, ls=-0.025 * s2))
        x += w + s2 * 0.14
        last = (bx + w, by)
    # a trail of smaller token chips carrying on up and to the right, into the space beside "Don\u2019t"
    trail = ["ated", "the", "likely", "Sure!", "it", "seems", "maybe", "…"]
    rnd = random.Random(7)
    tx, ty = last[0] + s2 * 0.12, last[1] - s2 * 0.55
    for i, tok in enumerate(trail):
        size = s2 * (0.24 - i * 0.015)
        fade = 0.50 + i * 0.06
        w = measure(tok, size, "JetBrains Mono", 500)
        if tx + w > W - m * 0.4:
            break
        out.append(rect(tx - size * 0.3, ty - size * 0.95, w + size * 0.6, size * 1.35, "none", rx=size * 0.25,
                        stroke=mix(C["llm_on_dark"], bg, fade + 0.12), sw=0.8))
        out.append(text(tx, ty, tok, size, mix(C["llm_on_dark"], bg, fade), family="JetBrains Mono", weight=500))
        tx += w + size * (1.2 + rnd.random() * 0.6)
        ty -= size * (1.1 + rnd.random() * 0.8)
    # the three doors underneath: a decision ends in an action
    by = y3 + s2 * 0.62
    out += zone_bar(m, by, tw, H * 0.011, label_fill=C["faint_on_dark"], size=W * 0.017)
    out += _footer(W, H, m, C["text_on_dark"], C["sub_on_dark"], C["faint_on_dark"], strap)
    return "\n".join(out)


# ---------------------------------------------------------------- (b) streams converging
STREAM_TEXT = ["Sure! Based on the alert, it seems likely that this could be a",
               "I think this is probably malicious, although it might also be",
               "Here is my analysis of the sign-in: the pattern suggests that",
               "It's hard to say for certain, but given the context I would",
               "The request looks suspicious. However, it is also possible",
               "Let me think step by step about whether this alert is real",
               "Confidence: high. Verdict: benign? Actually, on reflection",
               "This appears to be a phishing attempt, or perhaps a test",
               "Great question! There are several factors to consider here",
               "In summary, the alert may or may not warrant escalation, and"]


def front_b(W, H, strap):
    bg, m = C["night"], W * 0.078
    tw = W - 2 * m
    out = [rect(0, 0, W, H, bg)]
    s1 = fit("Decide,", tw * 0.80, "Inter", 800, ls_em=-0.03)
    y1 = H * 0.175
    out.append(text(m - s1 * 0.04, y1, "Decide,", s1, C["jev_on_dark"], weight=800, ls=-0.03 * s1))
    s2 = fit("Don\u2019t Generate", tw, "Inter", 800, ls_em=-0.02)
    y2 = y1 + s2 * 1.25
    out.append(text(m - s2 * 0.03, y2, "Don\u2019t Generate", s2, C["text_on_dark"], weight=800, ls=-0.02 * s2))
    # many streams of LLM text converge on one point, and one clean typed answer comes out
    fx, fy = W * 0.5, H * 0.575
    rnd = random.Random(3)
    defs, paths = [], []
    n = 14
    for i in range(n):
        sx = -W * 0.05 + (W * 1.10) * i / (n - 1)
        sy = H * (0.30 + 0.035 * rnd.random())
        c1 = (sx, sy + H * 0.12)
        c2 = (fx + (sx - fx) * 0.18, fy - H * 0.10)
        pid = f"s{i}"
        defs.append(f'<path id="{pid}" d="M {sx:.1f} {sy:.1f} C {c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} '
                    f'{fx:.1f} {fy:.1f}"/>')
        fade = 0.28 + 0.45 * abs(i - (n - 1) / 2) / ((n - 1) / 2)
        col = mix(C["llm_on_dark"], bg, fade)
        paths.append(f'<text font-family="JetBrains Mono" font-size="{W * 0.0125:.2f}" fill="{col}">'
                     f'<textPath href="#{pid}">{STREAM_TEXT[i % len(STREAM_TEXT)]}</textPath></text>')
    out.append("<defs>" + "".join(defs) + "</defs>")
    out += paths
    out.append(circle(fx, fy, W * 0.012, C["jev_on_dark"]))
    # the answer card
    cw, ch = W * 0.62, H * 0.105
    cx, cy = fx - cw / 2, fy + H * 0.035
    out.append(rect(cx, cy, cw, ch, C["night2"], rx=W * 0.014, stroke=C["jev_on_dark"], sw=1.4))
    ms = W * 0.030
    out.append(text(cx + ms * 0.8, cy + ch * 0.42, "attack", ms, C["sub_on_dark"], family="JetBrains Mono", weight=500))
    bar_x, bar_w = cx + ms * 5.2, cw * 0.36
    out.append(rect(bar_x, cy + ch * 0.42 - ms * 0.55, bar_w, ms * 0.5, mix(C["jev_on_dark"], C["night2"], 0.8),
                    rx=ms * 0.25))
    out.append(rect(bar_x, cy + ch * 0.42 - ms * 0.55, bar_w * 0.02 + 2, ms * 0.5, C["jev_on_dark"], rx=ms * 0.25))
    out.append(text(cx + cw - ms * 0.8, cy + ch * 0.42, "0.02", ms, C["jev_on_dark"], family="JetBrains Mono",
                    weight=700, anchor="end"))
    px, py, ps = cx + ms * 0.8, cy + ch * 0.80, W * 0.022
    for name, col, filled in (("act", C["act"], True), ("review", C["review"], False), ("escalate", C["escalate"], False)):
        w = measure(name, ps, "JetBrains Mono", 500) + ps * 1.4
        out.append(rect(px, py - ps * 1.05, w, ps * 1.5, col if filled else "none", rx=ps * 0.75,
                        stroke=col, sw=1.1))
        out.append(text(px + w / 2, py, name, ps, C["night"] if filled else col, family="JetBrains Mono",
                        weight=500, anchor="middle"))
        px += w + ps * 0.7
    out += _footer(W, H, m, C["text_on_dark"], C["sub_on_dark"], C["faint_on_dark"], strap)
    return "\n".join(out)


# ---------------------------------------------------------------- (c) calm reliability diagram
def front_c(W, H, strap):
    bg, m = C["paper"], W * 0.078
    tw = W - 2 * m
    out = [rect(0, 0, W, H, bg)]
    s = fit("Don\u2019t Generate", tw, "Source Serif 4", 600, ls_em=-0.01)
    y1 = H * 0.16
    out.append(text(m, y1, "Decide,", s, C["jev"], family="Source Serif 4", weight=600, ls=-0.01 * s))
    out.append(text(m, y1 + s * 1.08, "Don\u2019t Generate", s, C["ink"], family="Source Serif 4", weight=600,
                    ls=-0.01 * s))
    side = W * 0.56
    ox, oy = W - m - side, H * 0.34 + side         # origin at bottom left of the plot
    out.append(line(ox, oy, ox + side, oy, C["rule"], 0.8))
    out.append(line(ox, oy, ox, oy - side, C["rule"], 0.8))
    out.append(line(ox, oy, ox + side, oy - side, C["muted"], 0.9, dash="3 3"))
    rnd = random.Random(11)
    for i in range(22):
        p = (i + 0.5) / 22
        q = min(0.98, max(0.02, p + rnd.uniform(-0.22, 0.22)))
        x0, y0 = ox + p * side, oy - q * side
        x1, y1_ = ox + p * side, oy - p * side
        out.append(line(x0, y0, x1, y1_, mix(C["llm"], bg, 0.72), 0.7))
        out.append(circle(x0, y0, W * 0.0055, mix(C["llm"], bg, 0.55)))
        out.append(circle(x1, y1_, W * 0.0075, C["jev"]))
    out.append(text(ox, oy + W * 0.032, "what it said", W * 0.018, C["muted"], family="JetBrains Mono"))
    out.append(text(ox - W * 0.012, oy - side, "what happened", W * 0.018, C["muted"], family="JetBrains Mono",
                    anchor="end"))
    out += _footer(W, H, m, C["ink"], C["ink2"], C["muted"], strap)
    return "\n".join(out)


CONCEPTS = {"a": ("Typographic: Generate breaks into tokens", front_a, C["night"], C["jev_on_dark"]),
            "b": ("Streams of LLM text converge on one typed answer", front_b, C["night"], C["jev_on_dark"]),
            "c": ("A reliability diagram settling on its diagonal", front_c, C["paper"], C["jev"])}


def main():
    from PIL import Image, ImageStat
    d = COVER / "concepts"
    strap = strapline()
    W, H = 7 * PT, 10 * PT
    report = {}
    for key, (name, fn, bg, title_col) in CONCEPTS.items():
        svg = svg_doc(7, 10, fn(W, H, strap))
        (d / f"concept-{key}.svg").write_text(svg)
        png = d / f"concept-{key}.png"
        to_png(svg, png, 1050, 1500)
        im = Image.open(png).convert("RGB")
        thumb = im.resize((150, round(150 * im.height / im.width)), Image.LANCZOS)
        thumb.save(d / f"concept-{key}-thumb150.png")
        im.convert("L").save(d / f"concept-{key}-grey.png")
        g = thumb.convert("L")
        g.save(d / f"concept-{key}-thumb150-grey.png")
        report[key] = dict(name=name,
                           title_vs_ground_wcag=round(contrast(title_col, bg), 2),
                           thumb_grey_rms_contrast=round(ImageStat.Stat(g).stddev[0], 1))
    (d / "report.json").write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
