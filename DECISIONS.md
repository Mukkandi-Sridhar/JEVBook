# Decisions log

Every judgement call made while building the book, so it can be reviewed and reversed.
Newest decisions are appended at the bottom of each section.

## Facts and sourcing

- **D-01 · No access to the Jev API.** Everything about Jev's *behaviour* in this book is synthetic, produced by
  `jev-mock-synthetic`. Jev's *interface* is copied from the real, public `typesafe-sdk` 0.7.2 on PyPI (MIT),
  which I installed and read. Facts about the company come from web search result summaries only (the proxy
  blocked the articles themselves), so each one carries `[[VERIFY]]` in the text until checked against a
  primary source.
- **D-02 · The real response schema wins over the brief.** The brief says every answer has
  `{type, choice|score|noul, confidence, probabilities, legend}`. The SDK's generated OpenAPI models show that
  `noul` answers carry only `{type, noul}`; `choice` answers have `{choice, confidence, probabilities}`;
  `score` answers have `{score, confidence, legend, probabilities}`. The mock follows the SDK exactly.
- **D-03 · `confidence` semantics.** The API describes `confidence` only as "confidence in the selected choice,
  from 0 to 1". The mock sets it to the probability of the top option (choice) or of the modal level (score).
  The book says this is the mock's definition and that the real definition is not documented [[VERIFY]].
- **D-04 · Model names.** Requests use the SDK default `jev-latest`; the mock answers as
  `jev-mock-synthetic` (the API documents that the response model may differ from the requested alias).
- **D-05 · Vendor claims.** Speed (40–200×), price ($0.042 per million input tokens on OpenRouter for "Jev 1.13"),
  the "RLCD" training method and the "parallel sampler" are presented as *vendor-reported* with [[VERIFY]].
- **D-06 · Name origin.** Search summaries disagree: one says Jev is named after the economist William Stanley
  Jevons; another ties "System One" (not "Jev") to Kahneman. The book states the Jevons link as reported and
  marks it [[VERIFY]]. The Jevons paradox chapter stands on its own economics either way.
- **D-07 · Quotes.** Only quotes whose wording I am confident of are used (Laplace, Box, Feynman, Jevons,
  de Finetti, Sutton, Hamming, Tukey, Goodhart/Strathern). Any quote whose exact wording is not certain carries
  [[VERIFY]]. No invented quotes, no paraphrase inside quotation marks.

## The synthetic world

- **D-10 · Kestrel Logistics.** A fictional mid-size freight company. 20,000 synthetic alerts over 28 days
  (seed 7), from 16 detection rules across EDR, email, identity, network, cloud and DLP sources.
- **D-11 · Known truth.** Features are sampled first; the label is drawn from `sigmoid(true_logit)`, so every alert
  has an exact true probability `p_true`. Base rate ≈ 7.6% malicious; the oracle AUC is 0.90. This is what makes
  honest calibration lessons possible.
- **D-12 · How the mock is imperfect (on purpose).** For SOC alerts the mock uses the true logit, then applies a
  bias of +0.10, multiplies by 1.18 (overconfident at the extremes) and adds seeded noise (σ = 0.35; σ = 0.55
  more when the state is raw text only). Result: AUC ≈ 0.895, ECE ≈ 0.013 on structured state, a bit worse on raw
  text. These are properties of the mock, not claims about Jev.
- **D-13 · Default SOC costs** (illustrative, not industry data): a missed attack that automation closed costs
  $10,000 in expected loss; an analyst review is 12 minutes at $75/hour ($15); analysts miss 5% of attacks they
  review; a false page costs $400. Chapters that use different numbers say so.
- **D-14 · Latency and cost in the mock are simulated** by a stated formula (`simulated_latency_ms`). Charts that
  use them carry the synthetic label.

## Design

- **D-20 · Palette.** Validated with the dataviz CVD checker. The brief's red/green pair failed for deuteranopia
  (ΔE 4.1), so Jev green moved to `#3B9C6E` and failure red to `#B8323A` (all pairs pass, worst ΔE 8.2).
  Act/review/escalate use a single-hue purple ordinal ramp (`#B7A6E0`, `#8468C9`, `#4B2C8F`) so they never clash
  with the four meaning colours.
- **D-21 · Page.** 7 × 10 in, twoside, 4.7 in text block, 1.1 in outer margin column for QR codes, notes and icons.
  Body Source Serif 4 at 10.25 pt; headings Inter; code JetBrains Mono at 8.3 pt. Fonts are static instances
  cut from the Google Fonts variable fonts (OFL) so LaTeX and Matplotlib select weights reliably.
- **D-22 · Sections are unnumbered**; only chapters, figures and tables carry numbers. Numbered sections read
  like a textbook; this book should read like a teacher.
- **D-23 · Figures** are Matplotlib (charts *and* diagrams) so every figure shares one look and is generated from
  code; exported as PDF (print) and SVG (web). Graphviz/Mermaid were considered; Matplotlib gave tighter control
  of type and colour at print size.
- **D-24 · No emoji in print.** Box types carry small TikZ icons instead.

## Tooling

- **D-30 · Labs** are written as `labs/chNN.py` in jupytext percent format (reviewable diffs) and synced to
  `labs/chNN.ipynb` (for Colab/QR codes). CI executes every notebook in mock mode.
- **D-31 · Listings** in chapters are executable Quarto cells, so the printed output under each listing is real
  output from the mock. `tools/check_listings.py` runs them all in CI.
- **D-32 · Numbers quoted in the prose** come from `results/chNN.json` through the `{{< num >}}` shortcode, written
  by the figure/lab code, so text and code cannot drift apart.
- **D-33 · Author name** on the title page is "Sridhar Mukkandi", inferred from the repository owner. Change in
  `_quarto.yml` and `assets/latex/before-body.tex`.
- **D-34 · QR codes** point to `colab.research.google.com/github/Mukkandi-Sridhar/JEVBook/blob/main/labs/chNN.ipynb`;
  they work once the notebooks are on `main`.

## Chapter-level decisions

- **D-40 · Ch 21 split.** Weeks 1–3 (1–21 Sept) are "history" for fitting calibration and thresholds; week 4 is
  "live". Per-day numbers divide the live week by 7. A fifth "campaign week" (seed 11) boosts link-alert
  frequency ×3 (lookalike ×2) and shifts their true logit by +1.6 (+1.2) to show drift.
- **D-41 · Capacity.** An analyst clears 40 reviews per 8-hour shift (12 min each); Kestrel has 6 on the queue
  (240/day); on-call can absorb 40 pages/day. The capacity search fills the review queue exactly, because moving an
  alert from act to review always lowers expected cost under our cost model.
- **D-42 · "Real threat" wording.** A malicious alert is called a "real threat", not a "breach": most would be
  stopped by other defences, which is why the expected loss per missed one is $10k, not millions.
- **D-43 · Calibration figure** uses cross-fitting (fit Platt on even days, apply to odd days and vice versa) over all
  four weeks, so the curve is not noisy and no alert calibrates itself.
- **D-44 · Chapter 19's economics are an illustrative model** (`jevkit/econ.py`): six decision pools with stated
  volumes, value distributions and time budgets. It is labelled "illustrative model · assumptions, not measurements"
  on every figure. Jev's price and latency are vendor-reported; the LLM's are the book's illustrative figures.
  The model deliberately shows the bill *falling* within Kestrel's existing jobs, and rising only when a new job is
  added, because that is what the assumptions give and it is the honest reading of the rebound literature.
- **D-45 · Jev's name.** "Named after Jevons" is recorded as reported (search summary of TypeSafe's statements),
  marked [[VERIFY]] in the text. The early-2025 "Jevons paradox" commentary around cheaper AI models is mentioned
  without quotation, also [[VERIFY]].
- **D-46 · Bake-off contestants.** The "fine-tuned classifier" is a TF-IDF + logistic-regression text classifier,
  stated in the text as a floor for trained text models (no GPU or PyTorch in this build). Each method reads its
  natural input; Jev reads the fields as JSON so it sees the same information as the logistic regression. The text
  says plainly that the LLM-vs-Jev accuracy gap is built into the mocks (D-48) and is not evidence.
- **D-47 · Wide figures don't float.** Inside `{.wide}` the LaTeX `figure` environment is redefined as non-floating,
  so the figure takes the widened line (a float would reset to the text width).
- **D-48 · The mock LLM's design** (`jevkit/llm.py`, `MockLLM`). Its internal belief is mock Jev's text-mode
  probability plus extra logit noise (sd 0.45): it is deliberately a noisier reader than mock Jev. Its label-token
  probability is sharpened (temperature 0.45), so it is overconfident. Its stated confidence snaps to a few round
  values, mostly 0.9–0.99. At temperature > 0 it samples. About 2% of free-text JSON answers are wrapped or
  truncated and 1.5% add an invented field. Latency 0.45 s + tokens/60 s, price $1/M in and $4/M out: all
  illustrative. Any accuracy comparison between the mock LLM and mock Jev reflects these choices, and the book says so.
- **D-49 · Pattern catalogue measurements.** Only patterns with a meaningful synthetic test are measured (extract then
  decide, the gate via Chapter 14's result, the router). "Check the writer" and "memory controller" are shown as
  runnable shapes, with an explicit note that the mock's number means nothing there.
- **D-50 · Batch cache key covers content.** `score_alerts` now keys its cache on every column the state is built
  from, not only alert IDs, so alerts with edited fields (for example LLM-extracted ones) are scored afresh.
- **D-51 · Case-study baseline.** "Before" at Kestrel is one queue worked at capacity (240/day), rule-flagged alerts
  first, then first come first served, with alerts unreached after 24 h ageing out unseen. On-call responds to a page
  in 15 minutes (assumption). Both are stated in the chapter; the median-wait row that favours "before" is shown and
  explained rather than hidden.
- **D-52 · Chapter 13's agent bug is kept, not silently fixed.** The first agent never chose threat intel (the mock's
  lexical choice engine). Chapter 24 uses it as the teaching case for monitoring decision-step distributions; the
  fix (`always=("threat_intel",)`) is an explicit option, so Chapter 13's numbers still reproduce.
- **D-53 · TinyJev (Chapter 27)** reads structured fields only (numeric fields + a rule embedding), not text, so it
  trains in seconds on a laptop with autograd. Heads: sigmoid noul, softmax choice, cumulative-logit ordinal score
  with thresholds kept in order by softplus gaps. Trained on weeks 1–2, temperatures fitted on week 3, tested on
  week 4. The chapter states plainly that this is a design suggested by the interface, not Jev's architecture.
- **D-54 · Gallery (Chapter 26)** uses an illustrative domain table and synthetic support tickets. The mock's general
  engine does poorly on them (about 74% routing, urgency AUC about 0.6); the chapter shows this rather than tuning the
  mock, because "measure before you trust" is the lesson.
- **D-55 · Capstone service** (`jevkit/service.py`) is framework-agnostic (no web framework installed): a pydantic
  DecisionRecord, a frozen Config with a fingerprint, fallback-to-review on any SDK error, a deterministic hash-based
  3% audit draw, a daily monitor with bands chosen by eye from the live week and a 10% tolerance on capacity, and a
  shadow comparison. `fit_config` fits the lines with the critical-asset rule included.
- **D-56 · Index of terms** is generated (`tools/make_index.py`) from the glossary plus names, and lists chapters rather
  than page numbers, so it never goes stale between renders. Set in two columns in print.
- **D-57 · Companion widgets** (`site/`) are dependency-free HTML + JS reading `site/data.js`, exported by
  `tools/export_widget_data.py` from the same synthetic data as the book. Tested headless at 900 px and 390 px, light
  and dark, with no page-level horizontal scroll.
- **D-58 · Restructured to 22 chapters and 6 parts for a 200–250 page print book.** Old chapters 2+3 merged into
  Chapter 2; old 6–9 into Chapter 5 (deep learning in one chapter); old 10–11 into Chapter 6; old 12–14 into Chapter 7.
  Parts I and II are labelled prerequisites; calibration (3) and costs (4) stay full chapters because everything from
  Jev onward depends on them. Chapter files, labs and every "Chapter N"/"Part N" reference use the new numbering.
  Figure sources, figure folders and results files keep the first draft's ids (figures/src/chNN.py,
  figures/chNN/, results/chNN.json) and are referenced from chapters by those ids; they never appear in print.
  Old → new chapter map: 1→1, 2–3→2, 4→3, 5→4, 6–9→5, 10–11→6, 12–14→7, 15–29→8–22.
- **D-59 · Print layout.** 7×10 in trim, 5.2 in text block with a 0.95 in binding gutter, no margin column, 10.5 pt
  body, chapters open on any page. Removed: QR codes, chapter-opener progress maps, one-page summaries (they repeated
  "Where we are"). Draft markers ([[VERIFY]], [[AUTHOR STORY]]) render only with BOOK_DRAFT=1.
- **D-60 · Epigraphs.** Eighteen chapters open with a short quotation. Only well-documented wording is used; lines
  that circulate in several forms or are only attributed say so, and carry a [[VERIFY]] in the draft build.
- **D-61 · Boxes don't split.** Try it, Where this breaks, Set the threshold and Key idea boxes are short, and a split
  one leaves its tail on the next page with no label. They are now unbreakable and move whole to the next page.
  Going deeper and sidebars can run long, so they may still break, but only with seven lines free at the start.
- **D-62 · Equal margins.** Inner and outer margins are both 0.9in, so the text block sits in the same place on every
  page, including in PDF viewers that show one page at a time. 0.9in is ample gutter for a 250-page binding.
- **D-63 · Parts open on the right; roman front matter.** Every part page is a right-hand page, and the part's first
  chapter opens on the next right-hand page (a blank verso sits between). Other chapters still open on either page:
  forcing all of them right would add about a dozen blank pages and break the 250-page ceiling. Everything before
  Chapter 1 is numbered in roman; Chapter 1 is page 1 (Quarto's `\mainmatter` call is a no-op and `parts/p1.qmd`
  starts the main matter).
- **D-64 · A page index.** The print index is built by makeindex from `\index` entries that `filters/book.lua` adds:
  where a paragraph defines a term in bold and, for specific terms, at its first mention in each chapter. Ordinary
  words ("label", "state", "policy") are indexed only where they're defined, so the index points at explanations,
  not at every use. Terms and patterns live in `tools/make_index.py`. The web edition keeps a chapter list.
- **D-65 · Real spaces in the PDF.** LaTeX doesn't write space characters, so text copied or extracted from the PDF
  could lose word gaps on tight lines. `tagpdf`'s `interwordspace` (with `\DocumentMetadata`) writes real ones.
- **D-66 · No QR codes or Colab links.** The pre-print review briefly brought back one QR code per chapter, linking to
  its Colab notebook. The author asked again for none, so the print book has no QR codes and the web edition no Colab
  links. The labs are still in `labs/` and run anywhere Jupyter does.
- **D-67 · Results always recorded.** Some figure sources wrote their numbers only from the (now skipped) summary
  figure. `tools/build_figures.py` now calls each source's `record()` before drawing, so `results/` stays current.
- **D-68 · The queue stops at the end of the week.** `ops.serve` used to keep working the queue for a day after the
  last arrival, which counted eight days of reviews over seven and showed 274 a day against a capacity of 240. It
  now stops at the end of the last day; anything still waiting counts as never reached.
- **D-69 · One source of truth for shared numbers.** Chapter 15's "LLM decides" row reuses the bake-off's JSON
  answers (AUC 0.708), the injection listing uses the figure's 400 threats, and Chapter 13 counts distinct *stated*
  confidences (6, as in Chapter 6) rather than distinct probabilities.
- **D-70 · Sources seen through search only.** The proxy blocked docs.typesafe.ai, typesafe.ai, arxiv.org and every
  article host. The Chapter 9 rewrite, the confidence definition, the Jev-Mem summary and the bibliography URLs rely
  on search-engine excerpts of those pages, consistent across queries. PROGRESS.md lists them under NEEDS AUTHOR.
- **D-71 · Cover concept: typographic.** Three fronts were drawn and tested at 150 px wide, in greyscale and for
  contrast (`cover/concepts/report.json`). A, "Generate" breaking into orange tokens under a solid green "Decide,",
  kept its title readable at thumbnail size (title 7.27:1, thumbnail RMS contrast 39.9). B, streams of LLM text
  converging on a typed answer, blurred into texture at 150 px. C, a reliability diagonal on paper, was the quietest
  (3.26:1) and vanished on a white store page. A is the cover; B and C stay in `cover/concepts/`.
- **D-72 · A dark ground, lifted accents.** The cover is on a near-black blue (#141925) so it stands out among white
  and pale covers. The interior's green and orange are too dark on it, so the cover uses lighter steps of the same
  hues (#4FBA85, #F08C35); the purples, fonts and zone bar are the interior's. Every text colour is at least 5:1
  against its ground (`cover/checks.json`).
- **D-73 · How the cover is drawn.** Python writes SVG; Chromium (through Playwright) renders it to vector PDF and PNG,
  with the book's fonts embedded through `@font-face`. Chromium rounds page sizes, so pypdf then sets the media, trim
  and bleed boxes to the exact inches. Tints are solid mixed colours, not transparency, so the PDFs carry no
  transparency groups for the printer to flatten.
- **D-74 · Paper.** Paperback: standard colour (the cover's green and orange echo colour figures inside), 0.002252 in
  per page. Hardcover: premium colour, the only colour option KDP offers for hardcovers, 0.002347 in per page. Page
  count is read from the interior PDF (247) and rounded up to even (248), since a printed book has whole sheets.
  Paperback spine 0.5585 in, wrap 14.8085 × 10.25 in. Hardcover spine 0.7710 in (including KDP's 4.8 mm allowance),
  wrap 16.3458 × 11.4173 in.
- **D-75 · KDP geometry, and what couldn't be checked.** KDP's cover calculator and help pages are blocked by this
  build's proxy. The paper thicknesses, the paperback formula (bleed + back + spine + front + bleed), the hardcover
  case-laminate numbers (15 mm wrap, 10 mm hinge, boards 5 mm wider and 6 mm taller than trim, spine plus 4.8 mm) and
  the 79-page minimum for spine text come from KDP help excerpts found through search, agreeing with third-party
  calculators. The author should lay KDP's own template for the final page count over the guides PDF before upload.
- **D-76 · Case-study numbers on the back.** The back cover's before/after card reads `results/ch25.json`: 54% → 89%
  of real threats seen by a person, same six analysts. The brief said 57%; that was the figure before D-68 fixed the
  queue, and the cover follows the book. It's labelled as the book's synthetic case study.
- **D-77 · Strap line and QR code.** The front says "130+ figures" (138 numbered figures in the interior PDF, rounded
  down to a round number that stays true after small edits). The back's QR code points to the GitHub repository and
  prints its URL beneath, since the companion site isn't deployed yet. This is the only QR code; D-66 covers the
  interior.
- **D-78 · Barcode area left empty.** The bottom-right 2 × 1.2 in of the back, 0.25 in inside the trim, is kept clear
  for KDP's ISBN barcode and drawn only on the guides layer. On the hardcover it sits left of the hinge.
- **D-79 · No borrowed authority.** No TypeSafe logo or branding, no endorsement implied, and no invented praise: the
  praise, bio, photo and price are visible placeholders. The EPUB now uses `cover/ebook/cover.jpg`, and the old
  placeholder in `assets/cover/` is gone.
- **D-80 · Cover revision.** Front: the drifting LLM words ("ated", "the", "likely", …) are gone; three small, faint
  pieces of "Generate" ("ne", "ra", "te") step down to the right of "ate", below "Decide,". The "er" and "ate" chips
  sit closer and fade less, so "Generate" reads as one word at 150 px and in greyscale. The zone bar sits lower and
  the subtitle is larger (0.052 of the width, from 0.044), filling the lower half. Back: no price on the cover (set in
  KDP); the praise box is off behind `SHOW_PRAISE` until real quotes exist; the QR, URL and category sit inside the
  0.25 in safe area; "An independent guide. Not affiliated with TypeSafe AI." sits above the barcode area; blurb and
  bullet 3 reworded. The stat card still reads `results/ch25.json`, the file behind Chapter 18's table, which prints
  54% → 89%; `cover/check.py` now fails if the card and the book disagree, and measures every back-cover item
  against the safe area, the barcode area and its neighbours.
- **D-81 · Author block without a photo.** At the author's request the back cover has no photo, and the bio is one
  line built only from what the author gave: "Sridhar Mukkandi is an applied AI engineer who builds agents and the
  decision systems behind them." (`AUTHOR_BIO` in `cover/wrap.py`).
- **D-82 · Cover revision 3.** The bio is a `[[FINAL BIO]]` placeholder for the author's own text (replacing D-81's
  line). The independence line moved under the author block, left-aligned; the QR block now sits a short step below it
  instead of at the foot of the panel. The blurb's last sentence was reworded as the author gave it. The stat card
  still reads `results/ch25.json`, the file behind Chapter 18's table; the rendered book prints 54% → 89%, and
  `check.py` confirms the cover matches it.
- **D-83 · Final back-cover bio.** The author supplied the bio: "Sridhar Mukkandi is an applied AI engineer who builds
  agents and the decision systems behind them. He writes for engineers who want AI systems they can trust." The email
  stays beneath it. No photo or photo placeholder appears anywhere on the cover.
- **D-84 · Final copyright page.** The author supplied the copyright page text, now in `assets/latex/before-body.tex`
  as given: independently published, first edition 2026, MIT code licence, TypeSafe AI independence and trademark
  notice, the synthetic-numbers note (now naming Harbor Pharma too), no-warranty and no-advice notice, fonts, and
  contact email. The ISBN and printing lines are gone; with a KDP-assigned ISBN, KDP prints it in the cover barcode.
- **D-85 · Release v1.0.** Built into `release/v1.0/` (see its RELEASE.md and KDP-UPLOAD.md). Choices made there:
  the hidden [[VERIFY]] and [[AUTHOR STORY]] markers were removed from the source with the printed text unchanged,
  and recorded in `docs/verify-ledger.md`; the placeholder Acknowledgements page is out of this edition; About the
  Author uses the approved bio; the paperback moves to premium colour paper (spine 0.5821 in at 248 pages), which
  supersedes D-74's standard colour; the interior is padded to an even 248 pages with a final blank; figure rasters
  export at 300 ppi; the EPUB uses 300 dpi PNG figures with captions as alt text, and its CSS wraps code, URLs and
  wide maths. No bleed: nothing prints to the page edge. KDP's calculator and help pages stayed blocked, so margins
  and cover sizes follow KDP's published rules (D-75) and the author should check KDP's templates.
- **D-86 · v1.0.1 polish pass.** Justification: a fixed word-space range on the body font, microtype expansion off,
  `\tolerance=800` and `\emergencystretch=3em`, so justified lines stay even without stretching letters. The missing
  spaces reported ("question.You", "outloud", "metin") are not in the sources or the PDF text layer; they come from
  viewers joining lines on copy, so no source change. Index: main terms (the `TAUGHT` list in `tools/make_index.py`)
  get page ranges only in the chapters that teach them, built from the first to the last paragraph that mentions the
  term there; other uses are left out. New appendix "The Python you'll see" before the glossary. Plain-language pass
  for a first-year, ESL reader (rules at the top of `SIMPLIFY.md`, every change logged there): "calibrated" is the
  one term for honest probabilities and "threshold" the one term for a cut-off on the probability scale ("Cost line"
  in the glossary and index became "Cost-based threshold"); idioms replaced with plain words; long sentences split.
  Numbers, code, figures, citations, quotations and structure unchanged. The one-new-term-per-paragraph rule was
  applied by reading, not by a script. The book grew from 248 to 256 pages; spines 0.6008 in (paperback) and
  0.7898 in (hardcover).
