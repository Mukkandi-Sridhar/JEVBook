"""Render every figure PDF to a 300 dpi PNG for the EPUB: python3 tools/epub_figures.py

The print book uses the vector PDFs and the web edition the SVGs; e-readers (and Kindle's converter) handle PNG
most reliably. The PNGs are build output and are not committed.
"""
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

n = 0
for pdf in sorted((ROOT / "figures").rglob("*.pdf")):
    png = pdf.with_suffix(".png")
    if png.exists() and png.stat().st_mtime >= pdf.stat().st_mtime:
        continue
    subprocess.run(["pdftoppm", "-r", "300", "-png", "-singlefile", "-cropbox", str(pdf), str(pdf.with_suffix(""))],
                   check=True)
    n += 1
print(f"rendered {n} figure PNGs")
