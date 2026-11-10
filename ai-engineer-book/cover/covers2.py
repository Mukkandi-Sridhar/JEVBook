"""Second round of front covers for Ship Real AI: one bold idea each. Run: python3 cover/covers2.py

B5 trim (176 x 250 mm) plus 3 mm bleed; SVG in millimetres, rendered by Chromium at 300 dpi to cover/round2/.
"""
import json
import math
import random
import subprocess
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "cover" / "round2"
FONTS = ROOT / "assets" / "fonts"
OUT.mkdir(parents=True, exist_ok=True)

W, H = 179, 256
SUB1 = "The AI Engineer Bootcamp for LLMs, RAG, MCP, AI Agents and Evals,"
SUB2 = "from First Principles to Production and Interviews"
AUTHOR = "SRIDHAR MUKKANDI"
WS, SERIF, MONO = "Work Sans", "Plex Serif", "Plex Mono"


def page(body, bg, defs=""):
    fonts = "".join(
        f"@font-face{{font-family:'{fam}';src:url('file://{FONTS / f}');font-weight:{wt};font-style:{st};}}"
        for fam, f, wt, st in [(WS, "WorkSans-Regular.ttf", 400, "normal"), (WS, "WorkSans-Bold.ttf", 700, "normal"),
                               (SERIF, "IBMPlexSerif-Bold.ttf", 700, "normal"),
                               (SERIF, "IBMPlexSerif-Italic.ttf", 400, "italic"),
                               (SERIF, "IBMPlexSerif-Regular.ttf", 400, "normal"),
                               (MONO, "IBMPlexMono-Regular.ttf", 400, "normal"),
                               (MONO, "IBMPlexMono-Bold.ttf", 700, "normal")])
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{fonts}
html,body{{margin:0;background:{bg}}} svg{{display:block}}</style></head><body>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}"><defs>{defs}</defs>
{body}</svg></body></html>"""


def t(x, y, s, size, fill, fam=WS, wt=700, anchor="start", ls=0, extra=""):
    return (f'<text x="{x}" y="{y}" font-family="{fam}" font-weight="{wt}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" letter-spacing="{ls}" {extra}>{s}</text>')


def fit(x, y, s, size, fill, width):
    return t(x, y, s, size, fill, extra=f'textLength="{width}" lengthAdjust="spacingAndGlyphs"')


def sub(x, y, fill, size=4.1, wt=400, anchor="start"):
    return t(x, y, SUB1, size, fill, wt=wt, anchor=anchor) + t(x, y + size * 1.35, SUB2, size, fill, wt=wt, anchor=anchor)


def author(x, y, fill, anchor="start", size=5.4):
    return t(x, y, AUTHOR, size, fill, ls=1.6, anchor=anchor)


# ---------------------------------------------------------------- 1. Paper boat
def boat(dark=True):
    if dark:
        bg, ink, soft, wave = "#0A1030", "#FFFFFF", "#B9C2E8", "#3D4FB8"
        f1, f2, f3, f4 = "#FFB23E", "#F08A0C", "#C96A00", "#FFD08A"
        defs = ('<radialGradient id="g" cx="50%" cy="62%" r="75%"><stop offset="0" stop-color="#2A3A9E"/>'
                '<stop offset="0.55" stop-color="#121B55"/><stop offset="1" stop-color="#070B22"/></radialGradient>')
    else:
        bg, ink, soft, wave = "#F3EEE3", "#10163A", "#454C6E", "#9AA5DD"
        f1, f2, f3, f4 = "#3B4BA8", "#2A3789", "#1B2566", "#6878D6"
        defs = ('<radialGradient id="g" cx="50%" cy="62%" r="75%"><stop offset="0" stop-color="#FFFBF2"/>'
                '<stop offset="1" stop-color="#E9E1D0"/></radialGradient>')
    s = [f'<rect width="{W}" height="{H}" fill="url(#g)"/>']
    wy = 178
    for i in range(9):                                   # the water: widening ripples
        y = wy + 6 + i * 6.2
        a = 2.2 + i * 0.25
        d = f"M-5 {y}" + "".join(f" q 8 {-a} 16 0 t 16 0" for _ in range(7))
        s.append(f'<path d="{d}" fill="none" stroke="{wave}" stroke-width="{0.9 - i * 0.07}" opacity="{0.95 - i * 0.09}"/>')
    cx = 90                                              # the boat: four folded faces
    s.append(f'<polygon points="{cx},96 {cx - 30},168 {cx},168" fill="{f1}"/>'
             f'<polygon points="{cx},96 {cx + 30},168 {cx},168" fill="{f2}"/>'
             f'<polygon points="{cx - 62},160 {cx},168 {cx - 30},168 {cx - 34},190 {cx},190 {cx},168" fill="{f4}"/>'
             f'<polygon points="{cx - 62},160 {cx - 30},168 {cx},168 {cx},190 {cx - 34},190" fill="{f1}"/>'
             f'<polygon points="{cx + 62},160 {cx + 30},168 {cx},168 {cx},190 {cx + 34},190" fill="{f3}"/>'
             f'<polygon points="{cx - 30},168 {cx + 30},168 {cx},176" fill="{f3}" opacity="0.55"/>')
    s.append(f'<ellipse cx="{cx}" cy="192" rx="46" ry="2.2" fill="{wave}" opacity="0.5"/>')
    s.append(fit(14, 50, "SHIP REAL AI", 26.5, ink, 151))
    s.append(sub(14.5, 62, soft, 4.25))
    s.append(t(cx, 226, "Anyone can fold the demo.", 6.4, ink, SERIF, 400, "middle", extra='font-style="italic"'))
    s.append(t(cx, 235, "This book gets it across the water.", 6.4, f1 if dark else f1, SERIF, 400, "middle",
               extra='font-style="italic"'))
    s.append(author(cx, 248, ink, "middle"))
    return page("".join(s), bg, defs)


# ---------------------------------------------------------------- 2. Shipping label
def label():
    random.seed(7)
    org, ink, red = "#F2820A", "#111111", "#C8261B"
    s = [f'<rect width="{W}" height="{H}" fill="{org}"/>']
    for i in range(-10, 40):                             # hazard stripes, top and bottom
        for y in (0, 244):
            s.append(f'<polygon points="{i * 12},{y} {i * 12 + 6},{y} {i * 12 + 12},{y + 12} {i * 12 + 6},{y + 12}" fill="{ink}"/>')
    s.append(f'<g transform="rotate(-3 90 128)"><rect x="17" y="33" width="149" height="186" fill="#000" opacity="0.22"/>'
             f'<rect x="14" y="30" width="149" height="186" fill="#FBF8F1"/>'
             f'<rect x="14" y="30" width="149" height="13" fill="{ink}"/>'
             + t(19, 39, "PRIORITY · PRODUCTION FREIGHT", 4.6, "#FBF8F1", ls=0.8)
             + t(158, 39, "17 MODULES", 4.6, org, anchor="end", ls=0.8)
             + fit(19, 82, "SHIP", 46, ink, 138) + fit(19, 122, "REAL AI", 46, ink, 138)
             + f'<line x1="14" y1="130" x2="163" y2="130" stroke="{ink}" stroke-width="0.9"/>'
             + t(19, 138, "FROM", 3.4, "#666", wt=700, ls=0.6) + t(19, 147, "First principles", 7.2, ink, SERIF)
             + t(92, 138, "TO", 3.4, "#666", wt=700, ls=0.6) + t(92, 147, "Production", 7.2, ink, SERIF)
             + f'<line x1="87" y1="130" x2="87" y2="153" stroke="{ink}" stroke-width="0.5"/>'
             + f'<line x1="14" y1="153" x2="163" y2="153" stroke="{ink}" stroke-width="0.9"/>'
             + t(19, 161, "CONTENTS", 3.4, "#666", ls=0.6)
             + t(19, 170, "LLMs · RAG · MCP · AI Agents · Evals", 5.0, ink, MONO, 700)
             + t(19, 178, "The AI Engineer Bootcamp, from First", 4.3, "#333", wt=400)
             + t(19, 184, "Principles to Production and Interviews", 4.3, "#333", wt=400)
             + f'<line x1="14" y1="189" x2="163" y2="189" stroke="{ink}" stroke-width="0.9"/>')
    x = 19
    while x < 96:                                        # barcode
        w = random.choice([0.5, 0.5, 0.9, 1.4])
        s.append(f'<rect x="{x}" y="193" width="{w}" height="15" fill="{ink}"/>')
        x += w + random.choice([0.5, 0.8, 1.2])
    s.append(t(19, 213, "SRAI-2026-0017-PROD", 3.0, ink, MONO, 400, ls=0.8))
    s.append(t(158, 201, "HANDLE WITH", 4.2, ink, anchor="end", ls=0.6) + t(158, 209, "EVALS", 8.5, ink, anchor="end", ls=0.5))
    s.append(f'<g transform="rotate(-10 135 180)" opacity="0.9"><rect x="110" y="171" width="50" height="19" rx="2" fill="none" '
             f'stroke="{red}" stroke-width="1.5"/>' + t(135, 180, "TESTED", 7, red, anchor="middle", ls=1.2)
             + t(135, 186.5, "EVERY LINE OF CODE RUNS", 2.6, red, anchor="middle", ls=0.3) + "</g></g>")
    s.append(author(89.5, 236, ink, "middle", 5.6))
    return page("".join(s), org)


# ---------------------------------------------------------------- 3. The switch
def switch():
    bg, grn = "#07080B", "#35E08C"
    defs = ('<filter id="glow" x="-50%" y="-80%" width="200%" height="260%"><feGaussianBlur stdDeviation="9"/></filter>'
            '<linearGradient id="knob" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/>'
            '<stop offset="1" stop-color="#C9D2D8"/></linearGradient>'
            '<linearGradient id="track" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#0E3D28"/>'
            '<stop offset="1" stop-color="#22C777"/></linearGradient>')
    s = [f'<rect width="{W}" height="{H}" fill="{bg}"/>']
    y = 152
    s.append(f'<rect x="34" y="{y - 26}" width="112" height="52" rx="26" fill="{grn}" opacity="0.55" filter="url(#glow)"/>'
             f'<rect x="30" y="{y - 27}" width="119" height="54" rx="27" fill="url(#track)" stroke="#48F0A0" stroke-width="0.6"/>'
             f'<circle cx="122" cy="{y}" r="22.5" fill="url(#knob)"/>'
             f'<circle cx="122" cy="{y}" r="22.5" fill="none" stroke="#FFFFFF" stroke-width="0.5"/>')
    s.append(t(30, y + 42, "DEMO", 6.5, "#4A4F58", ls=2.2) + t(149, y + 42, "PRODUCTION", 6.5, grn, anchor="end", ls=2.2))
    s.append(f'<line x1="60" y1="{y + 39.8}" x2="84" y2="{y + 39.8}" stroke="#2A2E35" stroke-width="0.5" stroke-dasharray="1.2 1.6"/>')
    s.append(fit(14, 52, "SHIP", 44, "#FFFFFF", 86) + fit(14, 92, "REAL AI", 44, "#FFFFFF", 151))
    s.append(f'<rect x="106" y="20" width="59" height="32" fill="{bg}"/>'
             + t(165, 30, "LLMs", 5, "#7B828E", MONO, 400, "end") + t(165, 37.5, "RAG · MCP", 5, "#7B828E", MONO, 400, "end")
             + t(165, 45, "Agents · Evals", 5, "#7B828E", MONO, 400, "end"))
    s.append(sub(14.5, 104, "#A9B0BC", 4.25))
    s.append(t(14, 222, "Anyone can build the demo.", 7, "#FFFFFF", SERIF, 400, extra='font-style="italic"'))
    s.append(t(14, 231.5, "This book is about what comes after.", 7, grn, SERIF, 400, extra='font-style="italic"'))
    s.append(author(14, 247, "#FFFFFF"))
    return page("".join(s), bg, defs)


# ---------------------------------------------------------------- 4. Colour field, giant type
def field():
    defs = '<filter id="b" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="26"/></filter>'
    s = [f'<rect width="{W}" height="{H}" fill="#12082E"/>',
         '<g filter="url(#b)"><circle cx="30" cy="40" r="70" fill="#4338F0"/><circle cx="165" cy="95" r="62" fill="#E0218A"/>'
         '<circle cx="110" cy="215" r="78" fill="#FF8A00"/><circle cx="0" cy="230" r="55" fill="#B01C6E"/>'
         '<circle cx="180" cy="0" r="40" fill="#2B7BFF"/></g>']
    s.append(fit(13, 78, "SHIP", 70, "#FFFFFF", 153) + fit(13, 137, "REAL", 70, "#FFFFFF", 153))
    s.append(t(11, 196, "AI", 70, "#FFFFFF", ls=-2))
    s.append(f'<line x1="78" y1="150" x2="166" y2="150" stroke="#FFFFFF" stroke-width="0.5"/>')
    for i, l in enumerate(["The AI Engineer Bootcamp", "for LLMs, RAG, MCP,", "AI Agents and Evals,", "from First Principles",
                           "to Production", "and Interviews"]):
        s.append(t(78, 159 + i * 6.6, l, 5.0, "#FFFFFF", wt=700 if i == 0 else 400))
    s.append(f'<line x1="13" y1="232" x2="166" y2="232" stroke="#FFFFFF" stroke-width="0.5"/>')
    s.append(author(13, 244, "#FFFFFF") + t(166, 244, "17 modules · every line of code runs", 3.6, "#FFFFFF", wt=400, anchor="end"))
    return page("".join(s), "#12082E", defs)


# ---------------------------------------------------------------- 5. Blueprint
def blueprint():
    bg, ln = "#0F3FA6", "#DCE8FF"
    s = [f'<rect width="{W}" height="{H}" fill="{bg}"/>']
    for i in range(0, 180, 4):
        s.append(f'<line x1="{i}" y1="0" x2="{i}" y2="{H}" stroke="#2A58BD" stroke-width="{0.35 if i % 20 == 0 else 0.12}"/>')
    for i in range(0, 260, 4):
        s.append(f'<line x1="0" y1="{i}" x2="{W}" y2="{i}" stroke="#2A58BD" stroke-width="{0.35 if i % 20 == 0 else 0.12}"/>')
    s.append(f'<rect x="9" y="9" width="158" height="238" fill="none" stroke="{ln}" stroke-width="0.7"/>')
    cx, cy = 88, 150                                     # the agent loop as a drawing
    st = f'fill="none" stroke="{ln}" stroke-width="0.55"'
    s.append(f'<circle cx="{cx}" cy="{cy}" r="38" {st}/><circle cx="{cx}" cy="{cy}" r="27" {st} stroke-dasharray="1.5 1.5"/>'
             f'<line x1="{cx - 52}" y1="{cy}" x2="{cx + 52}" y2="{cy}" stroke="{ln}" stroke-width="0.25" stroke-dasharray="6 1.5 1 1.5"/>'
             f'<line x1="{cx}" y1="{cy - 52}" x2="{cx}" y2="{cy + 52}" stroke="{ln}" stroke-width="0.25" stroke-dasharray="6 1.5 1 1.5"/>')
    for lab, a in [("MODEL", -90), ("TOOLS", 30), ("CHECKS", 150)]:
        r = math.radians(a)
        x, y = cx + 38 * math.cos(r), cy + 38 * math.sin(r)
        s.append(f'<rect x="{x - 13}" y="{y - 5.5}" width="26" height="11" fill="{bg}" stroke="{ln}" stroke-width="0.7"/>'
                 + t(x, y + 1.6, lab, 4.2, ln, MONO, 700, "middle"))
        r2 = math.radians(a + 62)
        ax, ay = cx + 38 * math.cos(r2), cy + 38 * math.sin(r2)
        s.append(f'<polygon points="-2.4,-2 2.6,0 -2.4,2" transform="translate({ax},{ay}) rotate({a + 152})" fill="{ln}"/>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="9" fill="#FFB23E"/>' + t(cx, cy + 1.3, "AGENT", 3.6, "#0B2A6E", anchor="middle"))
    s.append(f'<line x1="{cx - 38}" y1="{cy + 50}" x2="{cx + 38}" y2="{cy + 50}" stroke="{ln}" stroke-width="0.3"/>'
             f'<line x1="{cx - 38}" y1="{cy + 47}" x2="{cx - 38}" y2="{cy + 53}" stroke="{ln}" stroke-width="0.3"/>'
             f'<line x1="{cx + 38}" y1="{cy + 47}" x2="{cx + 38}" y2="{cy + 53}" stroke="{ln}" stroke-width="0.3"/>'
             + t(cx, cy + 56, "ONE LOOP · EVERY GUARDRAIL", 3.2, ln, MONO, 400, "middle", 0.5))
    s.append(fit(15, 48, "SHIP REAL AI", 25.5, "#FFFFFF", 146))
    s.append(sub(15.5, 59, ln, 4.1))
    y0 = 223                                             # title block
    s.append(f'<rect x="9" y="{y0}" width="158" height="24" fill="{bg}" stroke="{ln}" stroke-width="0.7"/>'
             f'<line x1="92" y1="{y0}" x2="92" y2="{y0 + 24}" stroke="{ln}" stroke-width="0.4"/>'
             f'<line x1="130" y1="{y0}" x2="130" y2="{y0 + 24}" stroke="{ln}" stroke-width="0.4"/>'
             + t(13, y0 + 6, "DRAWN BY", 2.6, ln, MONO, 400, ls=0.4) + t(13, y0 + 16, AUTHOR, 5.2, "#FFFFFF", ls=1.0)
             + t(95, y0 + 6, "SCALE", 2.6, ln, MONO, 400, ls=0.4) + t(95, y0 + 16, "production", 5, "#FFFFFF", MONO, 700)
             + t(133, y0 + 6, "SHEETS", 2.6, ln, MONO, 400, ls=0.4) + t(133, y0 + 16, "17 modules", 5, "#FFFFFF", MONO, 700))
    return page("".join(s), bg)


CONCEPTS = {"1-paper-boat": boat, "2-paper-boat-light": lambda: boat(False), "3-shipping-label": label,
            "4-switch": switch, "5-colour-field": field, "6-blueprint": blueprint}

if __name__ == "__main__":
    css_w, css_h = round(W / 25.4 * 96), round(H / 25.4 * 96)
    scale = round(W / 25.4 * 300) / css_w
    jobs = []
    for name, fn in CONCEPTS.items():
        (OUT / f"{name}.html").write_text(fn())
        jobs.append({"src": str(OUT / f"{name}.html"), "out": str(OUT / f"{name}.png"), "type": "png",
                     "width": css_w, "height": css_h, "scale": scale})
    (OUT / "jobs.json").write_text(json.dumps(jobs))
    subprocess.run(["node", str(ROOT / "cover" / "render.mjs"), str(OUT / "jobs.json")], check=True,
                   stdout=subprocess.DEVNULL)
    (OUT / "jobs.json").unlink()
    ims = [Image.open(OUT / f"{n}.png").convert("RGB") for n in CONCEPTS]
    for half, name in [(ims[:3], "compare-1.png"), (ims[3:], "compare-2.png")]:
        big = [im.resize((700, round(700 * im.height / im.width)), Image.LANCZOS) for im in half]
        sheet = Image.new("RGB", (len(big) * 720 + 20, big[0].height + 40), "#D9D9D9")
        for i, b in enumerate(big):
            sheet.paste(b, (20 + i * 720, 20))
        sheet.save(OUT / name)
    th = [im.resize((160, 229), Image.LANCZOS) for im in ims]
    sheet = Image.new("RGB", (len(th) * 175 + 15, 2 * 240 + 20), "white")
    for i, x in enumerate(th):
        sheet.paste(x, (15 + i * 175, 10))
        sheet.paste(ImageOps.grayscale(x).convert("RGB"), (15 + i * 175, 250))
    sheet.save(OUT / "thumbs.png")
