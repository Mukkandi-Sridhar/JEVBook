"""Tile PDF pages into one image for quick visual review.
usage: python tools/contact.py PDF first last out.png [dpi] [cols]"""
import subprocess, sys, tempfile, glob
from PIL import Image
pdf, a, b, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
dpi = int(sys.argv[5]) if len(sys.argv) > 5 else 50
cols = int(sys.argv[6]) if len(sys.argv) > 6 else 4
with tempfile.TemporaryDirectory() as d:
    subprocess.run(["pdftoppm", "-r", str(dpi), "-png", "-f", str(a), "-l", str(b), pdf, f"{d}/p"], check=True)
    ims = [Image.open(f) for f in sorted(glob.glob(f"{d}/p-*.png"))]
    w, h = ims[0].size
    rows = (len(ims) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * (w + 8), rows * (h + 8)), (120, 120, 120))
    for i, im in enumerate(ims):
        sheet.paste(im, ((i % cols) * (w + 8), (i // cols) * (h + 8)))
    sheet.save(out)
print(out)
