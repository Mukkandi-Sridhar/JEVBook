"""Quarto pre-render hook: make sure every chapter has its 'you are here' map and QR code."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from jevkit import figs  # noqa: E402
from jevkit.figs.bookmap import CHAPTERS  # noqa: E402

for ch in CHAPTERS:
    d = ROOT / "figures" / ch
    if not (d / "map.pdf").exists():
        figs.save(figs.you_are_here(ch), ch, "map")
    if not (d / "qr.pdf").exists():
        figs.qr(ch)
