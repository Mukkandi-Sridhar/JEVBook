# Release v1.0.4: *Decide, Don't Generate*

Built 1 October 2026 from branch `claude/compassionate-planck-ao0jvq`, tag `v1.0.4` (the folder keeps its v1.0
name so links to it don't break). What changed since v1.0 is under "v1.0.1: polish pass", "v1.0.2: code listings"
and "v1.0.3: key ideas, and a book that works in black and white" below. Every check below was run on
the files in this folder; the raw results are in `checks.json`.

## What's here

| File | What it is | Size |
|---|---|---:|
| `print-color/interior-color.pdf` | Interior for KDP, colour paperback and hardcover. 7 × 10 in, no bleed, 270 pages. | 4.3 MB |
| `print-color/cover-paperback-color.pdf` | Paperback full wrap, 14.8837 × 10.25 in (0.125 in bleed), guides off. | 92 KB |
| `print-color/cover-hardcover-color.pdf` | Hardcover case-laminate wrap, 16.3975 × 11.4173 in, guides off. | 96 KB |
| `print-bw/interior-bw.pdf` | The black-and-white edition's interior: the same 270 pages in true greyscale (no colour anywhere, images grey). | 4.1 MB |
| `print-bw/cover-paperback-bw.pdf` | Black-and-white paperback wrap, 14.858 × 10.25 in: spine sized for KDP's white black-and-white paper. The cover itself is in colour. | 92 KB |
| `print-color/guides/cover-*-color-guides.pdf` | The same wraps with trim, spine, safe-area, hinge and barcode guides. For checking only; don't upload. | 252 KB |
| `print-color/cover-dimensions.json` | Page count, paper, spine and wrap sizes used for the covers. | 4 KB |
| `ebook/book.epub` | Reflowable EPUB 3. Passes EPUBCheck 5.3 with no errors or warnings. | 12 MB |
| `ebook/ebook-cover.jpg` | Ebook cover, front only, 1600 × 2560 px. | 324 KB |
| `preview/Decide-Dont-Generate-COMPLETE.pdf` | Front cover + full interior + back cover, 271 pages, bookmarked by part and chapter. For you and beta readers; not for KDP. | 4.3 MB |
| `preview/sample-chapters.pdf` | Front cover, contents, Chapter 3, Chapter 13 and a closing page with the repository link. 26 pages. | 720 KB |
| `marketing/mockup-3d.png` | 3D book mockup, 2000 × 1400 px. | 168 KB |
| `marketing/post-square-1080.png` | Square post, 1080 × 1080 px. | 92 KB |
| `marketing/banner-1200x628.png` | Link banner, 1200 × 628 px. | 84 KB |
| `print-shop/` | Front, back and spine as separate panels with 0.125 in bleed (PDF and 300 dpi PNG), and the full paperback wrap as a PNG, for a local printer. | 1.4 MB |
| `KDP-UPLOAD.md` | What to choose on each KDP screen, and which file goes where. | |
| `checks.json` | Output of `tools/release_check.py`. | |
| `checks/` | The photocopy test: every page in greyscale with the contrast pushed up and a slight blur. `photocopy-contact-sheet.png` shows all 270 pages; the other sheets show 32 pages each, larger. | 5.3 MB |

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
  bleed). At 270 pages the rule is 0.5 in inside; the book uses 0.9 in on both sides.
- **Openings:** every part opens on a right-hand page, and so does each part's first chapter; other chapters open
  on either page (D-63). Front matter is numbered i–xvi in roman; Chapter 1 is page 1.
- **Fonts:** all 463 font objects embedded (subsets of Source Serif 4, Inter and JetBrains Mono).
- **Images:** the figures are vector. The four raster pieces (heatmaps in Figures 5.3, 5.4 and 19.4) were 150 ppi;
  the figure style now exports rasters at 300 ppi, and all four are 300 ppi.
- **Overflow:** no word of text sits outside the text block anywhere in the book (a few points of hanging
  punctuation allowed). Three-digit page numbers of the part entries in the contents stuck out 6 pt; fixed.
- **Blank pages:** 10, all intentional: the half-title verso (page 2), versos before part openers or a part's first
  chapter (pages 16, 62, 92, 140, 180, 182, 238, 240), and a closing blank page 270.
- **Page count: 270** (the book ends on page 269; one blank page makes the count even so the file matches the spine
  calculation). KDP allows 24–828 pages for a 7 × 10 premium-colour paperback and 75–550 for a hardcover.
- PDF bookmarks carry part and chapter numbers, with curly quotes.

## Step 3: covers

Rebuilt for 270 pages. The colour editions use KDP **premium colour** paper (0.002347 in per page); the
black-and-white paperback uses KDP's **white black-and-white** paper (0.002252 in per page).

| | Spine | Full wrap | Notes |
|---|---:|---:|---|
| Paperback, colour | **0.6337 in** | 14.8837 × 10.25 in | 0.125 in bleed; spine text allowed (79+ pages) |
| Hardcover (case laminate) | **0.8227 in** | 16.3975 × 11.4173 in | boards 7.1969 × 10.2362 in, 0.591 in wrap, 0.394 in hinge |
| Paperback, black and white | **0.6080 in** | 14.8580 × 10.25 in | 0.125 in bleed; `print-bw/` |

KDP's cover calculator is blocked from this build (the proxy refuses kdp.amazon.com), so the sizes come from KDP's
published formulas (D-75): paperback width = bleed + back + spine + front + bleed; hardcover per KDP's case-laminate
specification. **Before uploading, download KDP's templates for 270 pages (premium colour, and black-and-white white paper) and lay them over
`print-color/guides/`.** The barcode area (2 × 1.2 in, bottom right of the back) is empty for KDP's free-ISBN barcode.
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
python3 tools/release_check.py release/v1.0     # also checks code wrap, both editions' covers, and greyscale
python3 tools/bw_test.py pages release/v1.0/print-color/interior-color.pdf release/v1.0/checks
python3 tools/bw_test.py figures /tmp/bw-figures  # every figure in greyscale and photocopy, for inspection
```

`tools/make_key_ideas.py` rewrites the Key ideas appendix from the chapters; run it after changing a key idea box
(`--check` fails if the appendix is out of date).

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

## v1.0.2: code listings

- **No code line wraps.** `tools/check_code_wrap.py` compares every listing line in the kept LaTeX file with the
  monospace lines of the PDF, and lists any line that doesn't fit on one printed line. Before this release, three code
  lines wrapped. In the Python appendix (printed p. 222), two long end-of-line comments now sit on their own line
  above the code. In Chapter 17, the trace printout's `shorten(...)` call moved to its own line, and the output is
  unchanged. All 117 listings and outputs were checked: 0 code lines wrap. Four *output* lines still wrap, because
  each is one long record: an alert's description (Chapter 1) and three JSON decision records (Chapter 14). They are
  data printed one per line, so they are left as they are.
- **Indentation.** The printed layout was already right: in the Chapter 5 `softmax` / `self_attention` listing,
  `return` sits under `e =` and `weights =`. But the PDF's text layer held no leading spaces, so text copied from
  the PDF lost its indentation (`e` got one space, `return` none) and pasted Python failed. Spaces in code are now
  real space characters of the same width (`\fvset{showspaces}` with a plain space glyph, in
  `assets/latex/preamble.tex`). Copied code keeps its indentation, and the printed layout doesn't change.
- **Text.** Python appendix: "`groupby` splits the table into groups and summarises each one." Chapter 5, after the
  cosine output: "Real text would give something like 0.7 to 0.9. Our synthetic notes use these words almost
  interchangeably, so they come out identical." Both are logged in `SIMPLIFY.md`.

**Checks on this build.** `pytest` 15 passed, 1 skipped; every listing runs (23 files); voice check clean on the
changed files. Interior still **256 pages** (255 plus a closing blank), so both covers stay as built: spine 0.6008
in (paperback, 256 × 0.002347 in) and 0.7898 in (hardcover). All 458 fonts are embedded, no raster is under
300 ppi, no text sits outside the text block, and there are 12 intentional blank pages. Placeholders: 0 in the
interior, both previews, both covers and the EPUB. EPUBCheck: 0 fatals, 0 errors, 0 warnings; 138 images, all with
alt text. Cover and interior agree (54% → 89%; 138 figures, "130+").

## v1.0.3: key ideas, and a book that works in black and white

**Key ideas.** 62 key ideas, 2–4 per chapter, each one sentence of 20 words or fewer, taken from the existing key
lines and bold statements (no new claims; every one is listed in the reply that came with this build and in the
appendix). Key lines that didn't make the cut went back to normal text. The wording changes are logged in
`SIMPLIFY.md` under "Key ideas (v1.0.3)".

- **Style, the same everywhere:** a 5 pt dark green bar down the left (`keybar`, 26% grey when printed), a light green
  tint, a small bold "KEY IDEA" label with a dot, and text at 11.5 pt bold, larger than the 10.5 pt body. The bar
  and label carry the meaning on their own: in the photocopy test the tint disappears and the box is still
  obvious. Boxes never split across pages (`unbreakable` in print, `break-inside: avoid` in the EPUB).
- **Keep these:** before each chapter's exercises, one framed box with the same bar lists that chapter's key ideas.
  `filters/book.lua` builds it from the chapter's own key idea boxes, so the two can't disagree.
- **Key ideas appendix:** 3 pages (printed pp. 233–235), first in the back matter and in the contents. Each key
  idea, by chapter, with dotted leaders to its page; in the ebook each line links to its box. Made by
  `tools/make_key_ideas.py`.
- **How to read this book:** the box legend (Figure 2) now leads with KEY IDEA and KEEP THESE, drawn as they
  look in the book, and the text explains both.

**Black-and-white safe.** The colour edition is unchanged apart from these fixes.

- *Boxes and text.* Body text and code text are pure black. Every box tint is at least 15% darker than white in
  greyscale (luma 83–85%; it was 95–97%), and every box has a bar or border dark enough to survive a photocopy
  (the sidebar and code blocks gained one; borders went from 81–91% grey to 51–63%). Code inside a Try it box
  sits on white so it stands apart from the box's tint. In code, keywords are bold and comments italic, as well as
  coloured; other token colours are dark enough to print as near-black.
- *Figures.* Hue is never the only cue. Lines differ by dash pattern and marker, bars and areas that touch by
  pattern, and every legend names the pattern ("solid", "striped"). Every fill is at least 15% darker than white.
  The act/review/escalate bar is plain, striped and cross-hatched as well as light, mid and dark purple, and a
  zone too narrow for its name gets a label above it. 39 figures needed a specific fix, 3 more show the zone bar
  and changed with it, and 7 changed only a word ("lines" to "thresholds", "honest" to "calibrated"): all 49 are
  listed below.
- *Text.* Every colour word in the prose, captions and exercises that identifies part of a figure now also names
  a cue the figure really has: "the red crosses", "the green dashed curve", "the red cell, outlined in black and
  striped". 41 changes, logged in `SIMPLIFY.md`.
- *Tests.* Every figure was rendered in greyscale and as a harsh photocopy (greyscale, contrast ×1.6 around
  mid-grey, 0.7 px blur at 110 dpi) and inspected; then every page of the book, and every box type at reading
  size. The photocopy contact sheets are in `checks/`. `tools/bw_test.py` makes both.

Figures changed for black and white (book numbering):

| Figure | Fix |
|---|---|
| Figure 3 (Prologue, the night shift) | Real alerts taller, thicker and marked on top; label says so |
| Figure 2 (How to read, the boxes) | KEY IDEA and KEEP THESE added, drawn with their thick bar |
| 1.2 Threshold search | Fixed line styles: total solid, false alarms dashed, misses dash-dot, "flag nothing" dotted |
| 2.5 Log loss | Attack curve solid, harmless curve dashed |
| 3.4 Rebalanced | Solid line with squares vs dashed line with circles; direct labels instead of a legend |
| 4.3 Cost curve | Calibrated solid, rebalanced dashed |
| 4.4 Precision and recall | Solid, dashed and dotted, named in the legend |
| 4.5 Coverage and risk | Solid vs dashed, named in the legend |
| 4.6 Three doors | Zone bar: plain, striped, cross-hatched |
| 5.1 Line limit | Attacks are crosses, normal activity dots |
| 5.2 Word map | Groups by border: thick, thin, dashed; legend shows the borders |
| 6.2 Latency | Waiting part of each bar striped |
| 6.3 Variance | Threats solid, harmless striped; real legend replaces two identical squares |
| 6.4 JSON failures | JSON mode striped; legend moved off the bars |
| 6.5 Three confidences | Dotted/triangles, dashed/squares, solid/circles, named in the legend |
| 7.2 Abstain | "It doesn't" drawn as a striped outline over solid bars; "threshold" label |
| 7.5 Injection | Solid line, dashed line, dotted fill; "act threshold" label |
| 8.4 Routing curve | Solid vs dashed, named in the legend |
| 10.3 Choice distributions | Top label solid, the rest light and striped |
| 10.4 Forced choice | Second histogram striped and outlined |
| 11.3 Harbor fixes | Solid/squares, dashed/circles, dotted/triangles, named in the legend |
| 11.4 ECE noise | The 90% band has dotted edges, so it survives without its tint |
| 12.3 Pools | Range bars darker, with end ticks |
| 12.6 Flags | Second bar of each pair striped |
| 14.1 Zones strip | Real threats are crosses, harmless alerts open circles; legend with the shapes |
| 14.2 Cost lines | Act solid, review dashed, escalate dotted; the "grey band" is wider and darker |
| 14.3 Calibration zones | Solid/squares vs dashed/circles; act zone has a visible edge; "perfectly calibrated" |
| 14.4 One vs three | Zones plain, striped, cross-hatched; "One threshold at 0.5" |
| 14.5 Capacity | Solid/squares vs dashed/circles, named on the lines |
| 14.6 Production loop | "move the thresholds" |
| 14.7 Drift watch | Campaign week has dotted edges; lines solid and dashed, named on the lines |
| 15.2 Extract, then decide | "policy thresholds" |
| 15.5 Gate | Zone bar: plain, striped, cross-hatched |
| 16.3 Errors | Success rows italic and dark green, not only light green |
| 16.4 Retries | Measured lines solid, the formula dotted (fixed, not left to the default cycle) |
| 17.1 Architecture | Zone bar: plain, striped, cross-hatched |
| 17.4 Trace | Observe plain, decide striped, generate dotted, act crossed; legend names them |
| 17.6 Labour | Same patterns as 17.4; labels on a solid patch so they stay readable |
| 18.1 Routes | Every part has its own pattern, named in the legend |
| 18.3 Shadow | The "missed" cell is outlined in black, striped and labelled |
| 19.2 Domains | Squares where a person decides, circles where the model decides |
| 19.3 Thresholds by domain | "passes this threshold" |
| 19.4 Tickets | Text colour follows the cell's darkness; grid lines removed from the heatmap |
| 21.3 Dry run | Second bar of each pair striped; "thresholds fitted" |
| 21.5 Monitor | Flagged days striped; campaign start marked; lines solid/circles and dashed/squares |
| 21.7 Checklist | "calibration, thresholds and rules" |
| 22.1 Stack | "calibrated probabilities", "thresholds" |
| 22.5 Monday | "set thresholds" |
| 22.6 Journey | "make them calibrated", "set thresholds from costs" |

Every figure also changed through the shared style: darker tints, black text, darker rules, and a default series
cycle in which colour, dash pattern and marker change together.

**Two editions, one layout.** `print-color/` and `print-bw/` hold the same kinds of file with matching names:
`interior-color.pdf` / `interior-bw.pdf`, `cover-paperback-color.pdf` / `cover-paperback-bw.pdf`, each folder's
`guides/` and `cover-dimensions.json`. Only the colour folder has a hardcover (`cover-hardcover-color.pdf`): KDP
prints hardcovers in premium colour only.

**Black-and-white edition.** `print-bw/interior-bw.pdf` is the colour interior converted to true greyscale with
`mutool recolor -c gray` (MuPDF 1.23): text, vector art and images are all grey. Same 270 pages, fonts embedded,
images still 300 ppi. Its paperback cover is the same design with a spine for KDP's white black-and-white paper:
270 × 0.002252 in = 0.6080 in. Settings for both editions are in `KDP-UPLOAD.md`.

**Checks on this build.** `pytest` 15 passed, 1 skipped; every listing runs; `check_numbers` 0 missing; voice check
clean (one note on the Key ideas appendix: the key ideas themselves contain a three-item list). Colour interior:
**270 pages** (269 plus a closing blank), 463 fonts all embedded, no raster under 300 ppi, no text outside the text
block, 10 intentional blank pages, no `??` from an unresolved page reference. Black-and-white interior: 270 pages,
no coloured pixel on any page, every image grey, fonts embedded, rasters 300 ppi. Code: 0 wrapped code lines (4
long output records wrap, as before). Placeholders: 0 in both interiors, both previews, all three covers and the
EPUB. EPUBCheck: 0 fatals, 0 errors, 0 warnings; 138 images with alt text; 62 key idea boxes, 22 Keep these boxes,
62 working links from the appendix. Covers, checked against the interior's page count and their paper: colour
paperback 0.6337 in spine, hardcover 0.8227 in, black-and-white paperback 0.6080 in, each wrap the size KDP's
formula gives. Cover and interior agree (54% → 89%; 138 figures, "130+").

## v1.0.4: the companion repository

The book now points readers to the public companion repository, **github.com/Mukkandi-Sridhar/decide-dont-generate**,
and its website, **mukkandi-sridhar.github.io/decide-dont-generate**, instead of the private working repository.
Changed in five places: the copyright page, the install command in "How to read this book" and Chapter 16 (where
the comment moved to its own line so the longer address doesn't wrap), the widgets link, the back cover's address
and QR code (all three paperback covers and the hardcover), and the sample's closing page. The companion repository
holds the toolkit, all 22 labs, the four browser tools, the code behind every figure, `results/`, the two `docs/`
pages the book cites, tests and CI, under the MIT licence; the chapters, covers and release files stay here. Both
earlier open items are fixed by it: the website exists once its workflow has run, and the code has a LICENSE file.

Checks: the same as v1.0.3, all passing, on the rebuilt files: 270 pages; fonts embedded; rasters 300 ppi; nothing
outside the margins; 0 placeholders; 0 wrapped code lines; EPUBCheck clean; all four cover sizes match their paper
(colour paperback 0.6337 in, standard-colour paperback 0.6080 in, black-and-white paperback 0.6080 in, hardcover
0.8227 in); the black-and-white interior has no colour.

## Decisions for you

1. **54% or 57%.** The book's Chapter 18 prints 54% → 89% (real threats seen by a person, same six analysts), and
   the cover matches it. 57% was the figure before the queue-simulation fix (D-68), which stopped the old queue
   working an extra day it didn't have. Nothing in the book says 57% for this number, so I left 54%. Changing it
   means changing the simulation, not the cover.
2. **37 claims are still unverified.** The markers are gone but the checks aren't done: vendor numbers (latency,
   price, speed-ups), the Doom demo, attributed quotations and epigraphs. `docs/verify-ledger.md` lists each one.
3. **~~The companion website printed in the book doesn't exist yet.~~** Fixed in v1.0.4 (see above). "How to read this book" names
   mukkandi-sridhar.github.io/JEVBook. Turn on GitHub Pages for the rendered site, or change that line to the
   repository URL before printing.
4. **~~No LICENSE file.~~** Fixed in v1.0.4: the companion repository is MIT-licensed. The copyright page says the code is released under the MIT licence at the repository, but
   the repository has no `LICENSE` file. Add one before release.
5. **Acknowledgements.** Left out of this edition (no approved text). Add it if you want one.
6. **KDP templates.** Check both covers against KDP's own templates for 270 pages, premium colour (see Step 3).
7. **Permissions for longer epigraphs** from works still in copyright (listed in `docs/originality-check.md`).
8. **AI disclosure.** See `KDP-UPLOAD.md`. The book itself doesn't mention how it was written; you may want a line
   in the preface or copyright page.
