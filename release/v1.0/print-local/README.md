# Author's copies from a local printer

These files are for copies printed in India by a local press: your own copies, gifts, and copies for the college
library and department. They carry **no ISBN**, because the free KDP ISBN may only be used on copies Amazon prints.
They're marked "Author's copy, printed in India · Not for resale" in a small footer on every page, in a box on the
copyright page, and in the label on the back cover where Amazon puts its barcode.

| File | Use |
|---|---|
| `interior-local-bw.pdf` | inside pages, black and white (much cheaper) |
| `interior-local-color.pdf` | inside pages, colour |
| `cover-local-13mm.pdf` | the cover: back, spine and front, 0.125 in (3 mm) bleed on every side |
| `cover-local-13mm-guides.pdf` | the same with trim, spine and safe-area lines, to show the printer; don't print it |

## Tell the printer

- **Trim size:** 7 × 10 in (178 × 254 mm). The interior PDF is exactly this size, with no bleed.
- **Pages:** 270 (135 sheets), printed on both sides.
- **Binding:** perfect binding (glued paperback).
- **Cover:** printed in colour on 250–300 GSM card, matte lamination; trim 3 mm off every edge of the cover file.
- **The spine is 13 mm in this file.** Ask the printer what spine width they need for 270 pages on their paper.
  If it's different, rebuild the cover: `python3 tools/local_print.py --spine-mm <their number>`.

Give them only the PDFs, and ask them to delete the files after the job. Keep the invoice: it records how many
copies were printed.
