# Progress

Resume from here. Each chapter row is updated after its lab runs, it renders, and it passes the voice check.

## Build order

| Step | What | Status |
|---|---|---|
| 1 | Repo: Quarto book (PDF/HTML/EPUB), `jevkit` + tests, SOC generator, figure system, CI, this file | done |
| 2 | Ch 1 (voice + design benchmark), then Ch 21 | done |
| 3 | Remaining chapters in plan order | done |
| 4 | Front/back matter, widgets, full render | done (first draft: 29 chapters, 364 pages) |
| 5 | Print edition: 22 chapters in six parts, prerequisites merged, QR codes and summary pages removed, epigraphs, 200–250 pages | done: 238 pages, all 22 labs and every listing pass, every chapter passes the voice check |

## Chapters

| Ch | Title | Words | Pages | Figures | Lab | Voice | Open [[VERIFY]] |
|---|---|---|---|---|---|---|---|
| 1 | What “learning” means | 2,662 | 12 | 5 | ok | pass | 1 |
| 2 | Probability, and how a machine learns it | 2,083 | 11 | 7 | ok | pass | 0 |
| 3 | Calibration: when 0.8 really means 80% | 2,077 | 11 | 6 | ok | pass | 0 |
| 4 | From probabilities to actions | 1,683 | 10 | 6 | ok | pass | 0 |
| 5 | Deep learning in one chapter | 1,860 | 8 | 5 | ok | pass | 0 |
| 6 | How an LLM writes, and structured outputs | 1,644 | 9 | 6 | ok | pass | 0 |
| 7 | RAG, agents, and where they break | 1,799 | 10 | 6 | ok | pass | 0 |
| 8 | System 1 and System 2 | 1,527 | 8 | 5 | ok | pass | 2 |
| 9 | Inside Jev: what we know and what we don’t | 1,612 | 9 | 6 | ok | pass | 7 |
| 10 | The type system: choice, score, noul | 1,282 | 8 | 6 | ok | pass | 0 |
| 11 | Testing Jev’s calibration yourself | 1,501 | 9 | 6 | ok | pass | 2 |
| 12 | The Jevons paradox of decisions | 1,941 | 11 | 6 | ok | pass | 6 |
| 13 | The bake-off: six ways to make a decision | 1,878 | 9 | 7 | ok | pass | 2 |
| 14 | Act, review, or escalate | 2,655 | 14 | 7 | ok | pass | 0 |
| 15 | A catalogue of decision patterns | 1,932 | 12 | 8 | ok | pass | 2 |
| 16 | First calls, and the mock that makes them free | 1,552 | 9 | 6 | ok | pass | 3 |
| 17 | A hybrid agent: Jev decides, the LLM reasons | 1,363 | 8 | 6 | ok | pass | 1 |
| 18 | Case study: SOC alert triage | 1,644 | 8 | 6 | ok | pass | 2 |
| 19 | An applications gallery | 1,505 | 9 | 6 | ok | pass | 3 |
| 20 | Build your own System One model | 1,576 | 9 | 6 | ok | pass | 2 |
| 21 | Capstone: a production decision service | 1,552 | 10 | 7 | ok | pass | 3 |
| 22 | What changes now | 1,172 | 7 | 6 | ok | pass | 2 |

## How to resume

1. `pip install -r requirements.txt && pip install -e . && make fonts`
2. `make test` then `python tools/build_figures.py chNN` for the chapter in progress.
3. Write `chapters/chNN.qmd`, `labs/chNN.py`, `figures/src/chNN.py`.
4. `python tools/run_labs.py chNN`, `python tools/check_listings.py chNN`, `python tools/voice_check.py chapters/chNN.qmd`.
5. `quarto render --to pdf`, then look at the pages (`python tools/contact.py _book/*.pdf A B out.png`).
6. `python tools/progress.py --pdf _book/*.pdf` rewrites the chapter table above.

## NEEDS AUTHOR

Everything below needs you, or access this build didn't have. `BOOK_DRAFT=1 quarto render --to pdf` shows every
[[VERIFY]] and [[AUTHOR STORY]] marker in place; `[[AUTHOR: …]]` placeholders show in every build.

**Placeholders to fill (visible in print until you do)**

- Copyright page (`assets/latex/before-body.tex`): publisher or imprint and city, ISBN for the paperback, ISBN for the
  ebook, and the month of the first edition. The printing line (10 9 8 … 1) is in place.
- Acknowledgements (`front/acknowledgements.qmd`) and About the Author (`back/about-author.qmd`).
- Back cover (`cover/wrap.py`): [[AUTHOR BIO]] and [[AUTHOR PHOTO]]. KDP prints the ISBN barcode in the empty
  bottom-right area. Praise is switched off (`SHOW_PRAISE`) until there are real quotes. Then rebuild
  (`cover/README.md`) and lay KDP's cover template for the final page count over `cover/print/cover-*-guides.pdf`.

**Your stories** — [[AUTHOR STORY]] markers: 20, hidden in print. They mark where AttendX, the police
FIR agent, SIGNAL, VMG-RAG or leading the intern team belongs. `grep -n "AUTHOR STORY" chapters/*.qmd index.qmd`
lists them with their topics.

**Checks against sources this build couldn't open.** The network blocked docs.typesafe.ai, typesafe.ai, arxiv.org,
huggingface.co and every article host, so these rest on search-engine excerpts that agreed across several queries:

- Chapter 9 and the glossary: TypeSafe's docs say `confidence` is computed from the shape of the probabilities (not
  the top probability), that `noul` answers carry no confidence, and that questions are evaluated in parallel and in
  isolation against the same state; the quick-start example shows confidence 0.78 beside a top probability of 0.85.
  Read docs.typesafe.ai (Quick start, Primitives, Confidence) and confirm the wording.
- Chapter 15: Jev-Mem (Jiang, Li and Li, UT Dallas, arXiv 2609.23986): method, LoCoMo LLM-as-judge 0.777 (+11.0%),
  memory construction 158 s (6.6× faster), query latency 0.93 s (−36.7%). Check against the paper.
- Bibliography: URLs and the access date (29 September 2026) for TypeSafe's blog and docs, DataCamp, regolo.ai and
  Alex Molas. Search results show the DataCamp article under two titles ("…That Never Hallucinates" and
  "…Explained"); the book uses the first. Confirm on the page.
- The Doom demo (Chapter 9: about ten decisions a second, about \$7 an hour) keeps its [[VERIFY]]: find TypeSafe's
  own post or video and cite it.
- [[VERIFY]] marks in total: 36, mostly vendor numbers (latency, price, speed-ups) and attributed quotes
  (Simon, Amara, Tyson, Gibson, "Hope is not a strategy"). `docs/jev-facts.md` is the ledger.

**Things to switch on**

- The companion site: the book prints https://mukkandi-sridhar.github.io/JEVBook/ (from `_quarto.yml`), but no
  GitHub Pages deployment exists yet. Turn on Pages for the rendered `_book/` (or change the URL in
  `front/how-to-read.qmd` and `_quarto.yml`).

**Not done here**

- A fine-tuned MiniLM for the bake-off's text-classifier row. It needs model weights from huggingface.co (blocked) and
  PyTorch (not installed). The row stays a TF-IDF classifier and the text says it's a floor, not a transformer.
- Live check: with a TypeSafe key, set `JEVKIT_LIVE=1` and re-run the labs for Chapters 9–11, 13 and 16 against real
  Jev; every synthetic number there has a real counterpart to measure.
- Chapters other than each part's first still open on either page (D-63): all on the right would push the book
  past 250 pages.
