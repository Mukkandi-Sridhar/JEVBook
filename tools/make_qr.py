"""QR codes for each chapter's lab in Google Colab: python tools/make_qr.py (writes figures/qr/chNN.pdf and .svg).

The print book shows one beside each chapter's exercises. The links point at the repository's main branch."""
from pathlib import Path

import segno

ROOT = Path(__file__).resolve().parents[1]
COLAB = "https://colab.research.google.com/github/Mukkandi-Sridhar/JEVBook/blob/main/labs/{ch}.ipynb"


def main():
    out = ROOT / "figures" / "qr"
    out.mkdir(parents=True, exist_ok=True)
    labs = sorted(p.stem for p in (ROOT / "labs").glob("ch*.py"))
    for ch in labs:
        q = segno.make(COLAB.format(ch=ch), error="m")
        q.save(out / f"{ch}.pdf", scale=2, border=0, dark="#1F2328")
        q.save(out / f"{ch}.svg", scale=2, border=0, dark="#1F2328")
    print(f"{len(labs)} QR codes")


if __name__ == "__main__":
    main()
