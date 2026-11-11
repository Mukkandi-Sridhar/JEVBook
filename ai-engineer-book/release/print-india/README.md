# India print edition (ISBN 978-93-346-0447-4)

Files for printing *Ship Real AI* in India with the ISBN allotted by RRRNA (November 2026, paperback, English,
publisher Mukkandi Sridhar). Built by `quarto render --to pdf`, `python3 cover/final_book.py` and
`python3 cover/print_wrap.py`.

| File | What it is |
|---|---|
| `interior-india-color.pdf` | 193-page colour interior, B5 (176 x 250 mm), ISBN on the copyright page (page 4) |
| `cover-india-9.5mm.pdf` | one-piece paperback cover (back, spine, front), 367.5 x 256 mm, EAN-13 barcode on the back (scan-tested) |
| `cover-india-9.5mm-guides.pdf` | the same with trim (red), spine (blue) and 6 mm safe area (green) marked, for checking only |

These copies may be sold. If you also publish the paperback on Amazon KDP, it gets its own free KDP ISBN: do not
use that number on copies printed here, and do not use this one on Amazon.

## Tell the printer

- Trim size **B5, 176 x 250 mm**, **193 pages** (they will round up to 194 or 196 with a blank), colour,
  perfect binding, 300 GSM matte or gloss laminated cover.
- The interior has no bleed; the cover has 3 mm bleed on every side.
- **Spine:** this cover assumes **9.5 mm**, about right for 193 pages on 70–80 GSM paper. Ask the printer for the
  exact spine width on their paper and rebuild: `python3 cover/print_wrap.py --spine-mm 10.2`.
- Ask for a **single proof copy** first: check the barcode scans, the colours, and that the spine text is centred.

## Legal deposit

Under the Delivery of Books Act, send one printed copy each to the four public libraries (National Library
Kolkata, Connemara Chennai, Asiatic Society Mumbai, Delhi Public Library) within 30 days of publication.
