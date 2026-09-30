# Release v1.0.1: *Decide, Don't Generate*

Built 30 September 2026 from branch `claude/compassionate-planck-ao0jvq`, tag `v1.0.1` (the folder keeps its v1.0
name so links to it don't break). What changed since v1.0 is under "v1.0.1: polish pass" below. Every check below was run on
the files in this folder; the raw results are in `checks.json`.

## What's here

| File | What it is | Size |
|---|---|---:|
| `print/Decide-Dont-Generate-interior.pdf` | Interior for KDP, paperback and hardcover. 7 × 10 in, no bleed, 256 pages. | 4.0 MB |
| `print/cover-paperback.pdf` | Paperback full wrap, 14.8508 × 10.25 in (0.125 in bleed), guides off. | 92 KB |
| `print/cover-hardcover.pdf` | Hardcover case-laminate wrap, 16.3646 × 11.4173 in, guides off. | 92 KB |
| `print/guides/cover-*-guides.pdf` | The same wraps with trim, spine, safe-area, hinge and barcode guides. For checking only; don't upload. | 252 KB |
| `print/cover-dimensions.json` | Page count, paper, spine and wrap sizes used for the covers. | 4 KB |
| `ebook/book.epub` | Reflowable EPUB 3. Passes EPUBCheck 5.3 with no errors or warnings. | 11 MB |
| `ebook/ebook-cover.jpg` | Ebook cover, front only, 1600 × 2560 px. | 324 KB |
| `preview/Decide-Dont-Generate-COMPLETE.pdf` | Front cover + full interior + back cover, 257 pages, bookmarked by part and chapter. For you and beta readers; not for KDP. | 4.0 MB |
| `preview/sample-chapters.pdf` | Front cover, contents, Chapter 3, Chapter 13 and a closing page with the repository link. 25 pages. | 702 KB |
| `marketing/mockup-3d.png` | 3D book mockup, 2000 × 1400 px. | 168 KB |
| `marketing/post-square-1080.png` | Square post, 1080 × 1080 px. | 92 KB |
| `marketing/banner-1200x628.png` | Link banner, 1200 × 628 px. | 84 KB |
| `print-shop/` | Front, back and spine as separate panels with 0.125 in bleed (PDF and 300 dpi PNG), and the full paperback wrap as a PNG, for a local printer. | 1.4 MB |
| `KDP-UPLOAD.md` | What to choose on each KDP screen, and which file goes where. | |
| `checks.json` | Output of `tools/release_check.py`. | |

## Step 1: the manuscript

**Pre-print fix pass (A–F).** All done in earlier commits and re-checked for this build:

| Section | Check this build | Result |
|---|---|---|
| A. Numbering (29 → 22 chapters) | Search for chapter or part numbers beyond 22 / VI | none |
| B. Honesty and voice | `tools/voice_check.py` on every chapter | 0 issues in all 22 chapters (two style notes on the Part IV opener and glossary: list density in 56 and 1,468 words; left as written) |
| C. Contradictions and reasoning | `tools/check_numbers.py` (every number in the text comes from `results/`) | 0 missing |
| D. Typos and listings | `tools/check_listings.py` (every code listing runs) | all pass |
| E. Layout | Margin, blank-page and overflow checks below | pass |
| F. Publishing matter | Copyright page, index, about the author | done (see below) |

Items the fix pass left for the author are listed under "Decisions for you" at the end.

**Copyright page.** The approved text, word for word: independently published, first edition 2026, no ISBN.

**Placeholders.** Searched for `[[`, `TODO`, `VERIFY` and `placeholder` in the manuscript sources, the interior
PDF, both preview PDFs, both cover PDFs and the EPUB: **zero** left. (The word `placeholder=` appears in three code
listings as an argument of Python's `textwrap.shorten`; that is code, not a gap, and the check allows it.) To get
there:

- The 37 `[[VERIFY]]` and 20 `[[AUTHOR STORY]]` markers were draft notes, hidden in print. They were removed from
  the source; the printed text is unchanged (a word-by-word comparison of the PDF text before and after showed no
  difference apart from the two pages below). What they marked is recorded in `docs/verify-ledger.md`.
- The Acknowledgements page held only a placeholder, and no acknowledgements text has been approved, so the page is
  out of this edition. To add one, create `front/acknowledgements.qmd` and list it in `_quarto.yml` after
  `index.qmd`.
- About the Author now uses the approved back-cover bio and email.

**Cover and interior agree** (checked by `tools/release_check.py`): title, subtitle, author "Sridhar Mukkandi",
case-study numbers and figure count. The book has 138 numbered figures; the cover says "130+". The case study reads
**54% → 89%** in both places (see "Decisions for you").

**Tests and labs.** `pytest`: 15 passed, 1 skipped (the live-API test, which runs only with a TypeSafe key). All 22
labs run end to end in mock mode (`tools/run_labs.py`). All listings pass.

## Step 2: interior PDF

- **Trim** 7 × 10 in, full colour. **No bleed:** nothing is printed to the page edge (the title page's colour bars
  sit 0.72 in inside it).
- **Margins:** inside 0.9 in, outside 0.9 in, top 0.8 in, bottom 0.85 in. KDP's minimums (from its help pages; the
  site itself couldn't be reached from this build): inside 0.375 in for 24–150 pages, **0.5 in for 151–300**, 0.625
  in for 301–500, 0.75 in for 501–700, 0.875 in for 701–828; outside at least 0.25 in without bleed (0.375 in with
  bleed). At 256 pages the rule is 0.5 in inside; the book uses 0.9 in on both sides.
- **Openings:** every part opens on a right-hand page, and so does each part's first chapter; other chapters open
  on either page (D-63). Front matter is numbered i–xvi in roman; Chapter 1 is page 1.
- **Fonts:** all 458 font objects embedded (subsets of Source Serif 4, Inter and JetBrains Mono).
- **Images:** the figures are vector. The four raster pieces (heatmaps in Figures 5.3, 5.4 and 19.4) were 150 ppi;
  the figure style now exports rasters at 300 ppi, and all four are 300 ppi.
- **Overflow:** no word of text sits outside the text block anywhere in the book (a few points of hanging
  punctuation allowed). Three-digit page numbers of the part entries in the contents stuck out 6 pt; fixed.
- **Blank pages:** 12, all intentional: the half-title verso (page 2), versos before part openers or a part's first
  chapter (pages 14, 16, 60, 88, 90, 136, 138, 174, 176, 230), and a closing blank page 256.
- **Page count: 256** (the book ends on page 255; one blank page makes the count even so the file matches the spine
  calculation). KDP allows 24–828 pages for a 7 × 10 premium-colour paperback and 75–550 for a hardcover.
- PDF bookmarks carry part and chapter numbers, with curly quotes.

## Step 3: covers

Rebuilt for 256 pages on KDP **premium colour** paper (0.002347 in per page), for both editions.

| | Spine | Full wrap | Notes |
|---|---:|---:|---|
| Paperback | **0.6008 in** | 14.8508 × 10.25 in | 0.125 in bleed; spine text allowed (79+ pages) |
| Hardcover (case laminate) | **0.7898 in** | 16.3646 × 11.4173 in | boards 7.1969 × 10.2362 in, 0.591 in wrap, 0.394 in hinge |

KDP's cover calculator is blocked from this build (the proxy refuses kdp.amazon.com), so the sizes come from KDP's
published formulas (D-75): paperback width = bleed + back + spine + front + bleed; hardcover per KDP's case-laminate
specification. **Before uploading, download KDP's template for 256 pages, premium colour, and lay it over
`print/guides/`.** The barcode area (2 × 1.2 in, bottom right of the back) is empty for KDP's free-ISBN barcode.
Every back-cover item sits inside the 0.25 in safe area, clear of the barcode area and of each other
(`cover/check.py`).

## Step 4: ebook

- Reflowable EPUB 3 with a navigable table of contents; internal links and cross-references validated by
  EPUBCheck.
- Figures are 300 dpi PNGs (1,100–1,800 px wide), rendered from the print figures (`tools/epub_figures.py`).
- Every one of the 138 figure images has alt text: its caption, without the "Figure N" label
  (`tools/epub_post.py`).
- Code blocks wrap instead of overflowing; wide figures, long URLs and one wide equation stay inside the screen.
  Checked by rendering every chapter at 360 px wide: no horizontal overflow.
- **EPUBCheck 5.3.0: 0 fatals, 0 errors, 0 warnings.**

## Step 5–6: previews and marketing

As listed above. The complete PDF opens with the bookmarks panel showing: Front cover, the front matter, Parts I–VI
with their chapters, the appendices, Back cover.

## Step 8: visual check

Rendered and looked at: pages 1–10, ten random pages (37, 41, 68, 92, 139, 142, 176, 231, 237, 240), the last five
pages (252–256), both cover wraps, the preview's front and back cover pages and the sample's closing page. Nothing
needed fixing beyond the items above.

## How to rebuild

```bash
python3 -m pytest -q && python3 tools/run_labs.py && python3 tools/check_listings.py
python3 tools/epub_figures.py                 # 300 dpi PNGs for the ebook
quarto render --to pdf && cp "_book/Decide,-Don-t-Generate.pdf" /tmp/interior.pdf
quarto render --to epub && python3 tools/epub_post.py "_book/Decide,-Don-t-Generate.epub" /tmp/book.epub
cp /tmp/interior.pdf _book/                   # the cover scripts read the page count from it
python3 cover/wrap.py && python3 cover/mockup.py && python3 cover/check.py
python3 tools/release.py /tmp/interior.pdf /tmp/book.epub v1.0
python3 cover/print_shop.py
python3 tools/release_check.py release/v1.0
```

## Changes made in the v1.0 build

Content is unchanged except where a check required it:

- Removed the hidden draft markers (ledger in `docs/verify-ledger.md`); filled About the Author with the approved bio;
  dropped the placeholder Acknowledgements page.
- Paperback paper switched from standard to premium colour, as specified; spine 0.5585 → 0.5821 in.
- Figure rasters exported at 300 ppi (`jevkit/figs/style.py`).
- Contents: wider page-number box for part entries. PDF bookmarks numbered.
- EPUB: PNG figures, alt text, wrapping code, full-width figures, breaking URLs.
- New tools: `tools/epub_figures.py`, `tools/epub_post.py`, `tools/release.py`, `tools/release_check.py`; banner in
  `cover/mockup.py`.

## v1.0.1: polish pass

Content changes in this release, all logged: wording in `SIMPLIFY.md`, judgement calls in `DECISIONS.md` (D-86).

- **Spacing.** Justified lines had loose, uneven gaps on a few pages. The body font now has a fixed word-space
  range (`WordSpace = {1.0, 1.4, 0.55}`), microtype font expansion is off (protrusion stays on), `\tolerance=800` and
  `\emergencystretch=3em` (`assets/latex/preamble.tex`). Printed pages 45, 87, 92, 151, 171, 203, 209 and 228 were
  rendered at 200% and looked at; the spacing is even.
- **Missing spaces.** "question.You", "outloud" and "metin" are not in the sources or in the PDF's text layer
  (`pdftotext`, raw and layout modes, whole book). They appear when a PDF viewer joins the end of one line to the
  start of the next while copying. The only joined words `pdftotext` finds are hyphenated line breaks
  ("sign-in", "how-to"), code and one URL. Nothing to fix in the sources.
- **Text fixes.** The repeated "The rest of the chapter is detail." (Chapter 4) is gone. Chapter 18 opens
  "No. That's the point of a case study." and says "about 718 alerts a day in the live week". SIEM (Chapter 13),
  DLP and F1 (Chapter 3), epoch (Chapter 5) and CISO (Chapter 18) are explained at first use and are in the
  glossary, with Threshold and Triage.
- **Index.** Main terms now show the page ranges where they are taught (for example Calibration 23–33, 101–109;
  Agent 63–71, 170–177; LLM 54–62), not every page that uses the word. The pages differ from the examples in the
  request because the book grew by eight pages.
- **New appendix, "The Python you'll see"** (4 pages, PDF pp. 238–241; the listings' printed output makes it a page
  longer than the 2–3 asked for): NumPy arrays and masks, pandas filtering and `groupby`,
  `lambda` and f-strings, on Kestrel examples. It is in the contents and linked from "How to read this book". Its
  eight listings run.
- **Plain language, whole book.** Written for a first-year student with basic Python who reads English as a second
  language. Short sentences, no idioms, common words, a definition at each new term, and one term for each idea
  ("calibrated", explained as probabilities that match what really happens; "threshold", not "line"). Numbers,
  code, figures, citations, quotations and structure are unchanged. 906 before/after pairs are in `SIMPLIFY.md`.
  Grade levels (Flesch-Kincaid, prose only, `tools/readability.py`): whole book 6.3 → 5.7; every chapter 6.9 or
  lower; the glossary 9.7 → 8.4. Sentences over 25 words: 4–18% of each chapter before, 0–4.5% after. Chapter 19
  has no sentence over 30 words.
- **Back cover and KDP description** use the same wording ("thresholds", "calibrated").

**Checks on this build.** `pytest` 15 passed, 1 skipped; 22 labs and 23 listing files pass (the appendix included);
`check_numbers` 0 missing; voice check clean. Interior 256 pages (255 plus a closing blank), all 458 fonts embedded,
no raster under 300 ppi, no text outside the text block, 12 intentional blank pages. Placeholders: 0 in the
interior, both previews, both covers and the EPUB (pandas `[["col"]]` in the appendix is code and is allowed).
EPUBCheck: 0 fatals, 0 errors, 0 warnings; 138 images, all with alt text; no overflow at 360 px. Covers rebuilt for
256 pages: spine 0.6008 in (paperback) and 0.7898 in (hardcover); `cover/check.py` passes; cover and interior agree
on the case study (54% → 89%) and the figure count (138, "130+").

## Decisions for you

1. **54% or 57%.** The book's Chapter 18 prints 54% → 89% (real threats seen by a person, same six analysts), and
   the cover matches it. 57% was the figure before the queue-simulation fix (D-68), which stopped the old queue
   working an extra day it didn't have. Nothing in the book says 57% for this number, so I left 54%. Changing it
   means changing the simulation, not the cover.
2. **37 claims are still unverified.** The markers are gone but the checks aren't done: vendor numbers (latency,
   price, speed-ups), the Doom demo, attributed quotations and epigraphs. `docs/verify-ledger.md` lists each one.
3. **The companion website printed in the book doesn't exist yet.** "How to read this book" names
   mukkandi-sridhar.github.io/JEVBook. Turn on GitHub Pages for the rendered site, or change that line to the
   repository URL before printing.
4. **No LICENSE file.** The copyright page says the code is released under the MIT licence at the repository, but
   the repository has no `LICENSE` file. Add one before release.
5. **Acknowledgements.** Left out of this edition (no approved text). Add it if you want one.
6. **KDP templates.** Check both covers against KDP's own templates for 256 pages, premium colour (see Step 3).
7. **Permissions for longer epigraphs** from works still in copyright (listed in `docs/originality-check.md`).
8. **AI disclosure.** See `KDP-UPLOAD.md`. The book itself doesn't mention how it was written; you may want a line
   in the preface or copyright page.
