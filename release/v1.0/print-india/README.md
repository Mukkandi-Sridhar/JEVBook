# India print edition (ISBN 978-93-345-4878-5)

Files for printing *Decide, Don't Generate* in India with the ISBN allotted by RRRNA (8 Oct 2026, paperback,
English, publisher Mukkandi Sridhar). Built by `python3 tools/india_edition.py`.

| File | What it is |
|---|---|
| `interior-india-color.pdf` | 270-page interior, colour, ISBN on the copyright page (page 4) |
| `interior-india-bw.pdf` | the same in black and white (cheaper to print) |
| `cover-india-13mm.pdf` | paperback cover with an EAN-13 ISBN barcode on the back (scan-tested) |
| `cover-india-13mm-guides.pdf` | the same with trim, bleed, spine and safe-area guides, for checking only |

These copies may be sold. The Amazon paperback keeps its own KDP ISBN (979-8-17825-770-8); do not use that
number on copies printed here, and do not use this one on Amazon.

## Tell the printer

- Trim size **7 x 10 in** (178 x 254 mm), **270 pages**, perfect binding, 300 GSM matte cover.
- Interior PDFs have no bleed; the cover has 0.125 in (3.2 mm) bleed on every side.
- **Spine:** this cover assumes **13 mm**, right for 270 pages on 70–80 GSM paper. Ask the printer for the exact
  spine on their paper and rebuild: `python3 tools/india_edition.py --spine-mm 14.5`.
- Ask for a **single proof copy** first; check the barcode scans and the spine text is centred.

## Legal deposit

Under the Delivery of Books Act, send one printed copy each to the four public libraries (National Library
Kolkata, Connemara Chennai, Asiatic Society Mumbai, Delhi Public Library) within 30 days of publication.
