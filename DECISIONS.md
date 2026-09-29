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
- **D-49 · Pattern catalog measurements.** Only patterns with a meaningful synthetic test are measured (extract then
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
