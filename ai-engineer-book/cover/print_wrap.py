"""India print edition: the interior and a one-piece paperback cover (back, spine, front) with 3 mm bleed.

Run after `quarto render --to pdf` and `python3 cover/final_book.py`:
    python3 cover/print_wrap.py [--spine-mm 9.5]

Writes release/print-india/: interior-india-color.pdf, cover-india-<spine>mm.pdf and a -guides.pdf copy that marks
the trim, spine and safe area (for checking only). The spine depends on the printer's paper: ask for the exact width
for 193 pages and rerun with --spine-mm.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

from pypdf import PageObject, PdfReader, PdfWriter, Transformation

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "cover"))
import covers3 as c3  # noqa: E402

TW, TH, B = 176, 250, 3          # trim and bleed, mm
MM = 72 / 25.4                    # points per mm
FINAL = ROOT / "cover" / "final"
DEST = ROOT / "release" / "print-india"

ap = argparse.ArgumentParser()
ap.add_argument("--spine-mm", type=float, default=9.5)
S = ap.parse_args().spine_mm
DEST.mkdir(parents=True, exist_ok=True)
tmp = FINAL / "wrap"
tmp.mkdir(exist_ok=True)

# Back with bleed: the trimmed back page placed 3 mm in from the left, top and bottom of a larger canvas that
# carries the same background out to the bleed edge (the spine side needs none).
back = (FINAL / "back.html").read_text()
bg = re.search(r"\.page\{[^}]*?(background:[^}]*?);?\}", back, re.S).group(1)
back = back.replace("</style>", f""".bleed{{position:relative;width:{TW + B}mm;height:{TH + 2 * B}mm;overflow:hidden;{bg}}}
.page{{position:absolute!important;left:{B}mm;top:{B}mm;background:none!important}}
@page {{ size: {TW + B}mm {TH + 2 * B}mm; margin: 0 }}</style>""", 1)
back = back.replace('<div class="page">', '<div class="bleed"><div class="page">', 1).replace("</body>", "</div></body>", 1)
(tmp / "back.html").write_text(back)

# Front with bleed: the cover canvas already has 3 mm at the top, bottom and right.
(tmp / "front.html").write_text(c3.neural_ship(c3.PAPER))

# Spine: indigo, title and author reading top to bottom.
fonts = back[:back.index("</style>")].split("<style>", 1)[1].split(".page{", 1)[0]
spine = f"""<!doctype html><html><head><meta charset="utf-8"><style>{fonts}
@page {{ size: {S}mm {TH + 2 * B}mm; margin: 0 }} html,body{{margin:0}}
.s{{width:{S}mm;height:{TH + 2 * B}mm;background:#10163A;position:relative;overflow:hidden}}
.r{{position:absolute;left:50%;top:{B + 16}mm;width:{TH - 32}mm;height:{S}mm;transform-origin:0 0;
   transform:rotate(90deg) translate(0,-50%);display:flex;align-items:center;justify-content:space-between;
   font-family:'Work Sans';white-space:nowrap}}
.t{{font-weight:700;font-size:{min(13, S * 1.15):.1f}pt;color:#F4EFE3;letter-spacing:.06em}}
.t span{{color:#E8780A}}
.a{{font-weight:700;font-size:{min(7.5, S * 0.7):.1f}pt;color:#C9CDE3;letter-spacing:.22em}}
</style></head><body><div class="s"><div class="r"><div class="t">SHIP REAL <span>AI</span></div>
<div class="a">SRIDHAR MUKKANDI</div></div></div></body></html>"""
(tmp / "spine.html").write_text(spine)

jobs = [{"src": str(tmp / "back.html"), "out": str(tmp / "back.pdf"), "type": "pdf",
         "width": f"{TW + B}mm", "height": f"{TH + 2 * B}mm"},
        {"src": str(tmp / "front.html"), "out": str(tmp / "front.pdf"), "type": "pdf",
         "width": f"{c3.W}mm", "height": f"{c3.H}mm"},
        {"src": str(tmp / "spine.html"), "out": str(tmp / "spine.pdf"), "type": "pdf",
         "width": f"{S}mm", "height": f"{TH + 2 * B}mm"}]
(tmp / "jobs.json").write_text(json.dumps(jobs))
subprocess.run(["node", str(ROOT / "cover" / "render.mjs"), str(tmp / "jobs.json")], check=True,
               stdout=subprocess.DEVNULL)

W, H = 2 * (TW + B) + S, TH + 2 * B


def wrap(guides):
    page = PageObject.create_blank_page(width=W * MM, height=H * MM)
    for name, x in [("back", 0), ("spine", TW + B), ("front", TW + B + S)]:
        page.merge_transformed_page(PdfReader(tmp / f"{name}.pdf").pages[0], Transformation().translate(x * MM, 0))
    if guides:
        page.merge_page(guide_layer())
    return page


def guide_layer():
    """Trim (red), spine folds (blue) and 6 mm safe area (green) as a thin-line overlay."""
    def rect(x, y, w, h):
        return f"{x * MM:.2f} {y * MM:.2f} {w * MM:.2f} {h * MM:.2f} re S\n"
    ops = "0.3 w 1 0 0 RG\n" + rect(B, B, W - 2 * B, TH)
    ops += "0 0 1 RG\n" + rect(TW + B, B, S, TH)
    ops += "0 0.6 0 RG\n" + rect(B + 6, B + 6, TW - 12, TH - 12) + rect(TW + B + S + 6, B + 6, TW - 12, TH - 12)
    w = PdfWriter()
    p = w.add_blank_page(width=W * MM, height=H * MM)
    from pypdf.generic import DecodedStreamObject, NameObject
    st = DecodedStreamObject()
    st.set_data(ops.encode())
    p[NameObject("/Contents")] = w._add_object(st)
    return p


tag = f"{S:g}"
for guides, name in [(False, f"cover-india-{tag}mm.pdf"), (True, f"cover-india-{tag}mm-guides.pdf")]:
    w = PdfWriter()
    w.add_page(wrap(guides))
    w.add_metadata({"/Title": "Ship Real AI (cover)", "/Author": "Sridhar Mukkandi"})
    with open(DEST / name, "wb") as f:
        w.write(f)

shutil.copy(ROOT / "_book" / "Ship-Real-AI.pdf", DEST / "interior-india-color.pdf")
shutil.rmtree(tmp)
print(f"cover {W:.1f} x {H} mm (spine {S:g} mm), interior {len(PdfReader(DEST / 'interior-india-color.pdf').pages)} pages")
