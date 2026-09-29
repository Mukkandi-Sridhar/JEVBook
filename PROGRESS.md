# Progress

Resume from here. Each chapter row is updated after its lab runs, it renders, and it passes the voice check.

## Build order

| Step | What | Status |
|---|---|---|
| 1 | Repo: Quarto book (PDF/HTML/EPUB), `jevkit` + tests, SOC generator, figure system, CI, this file | done |
| 2 | Ch 1 (voice + design benchmark), then Ch 21 | done |
| 3 | Remaining chapters in plan order | in progress |
| 4 | Front/back matter, widgets, full render ≥ 250 pages | not started |

## Chapters

| Ch | Title | Words | Pages | Figures | Lab | Voice | Open [[VERIFY]] |
|---|---|---|---|---|---|---|---|
| 1 | What “learning” means | 2,790 | 12 (incl. summary) | 6 + summary | ok | pass | 1 (TypeSafe release date) |
| 2 | Probability is the language of decisions | – | – | – | – | – | – |
| 3 | Data, loss and gradient descent | – | – | – | – | – | – |
| 4 | Calibration: when 0.8 really means 80% | – | – | – | – | – | – |
| 5 | From probabilities to actions | – | – | – | – | – | – |
| 6 | Neurons to networks | – | – | – | – | – | – |
| 7 | Embeddings: meaning as geometry | – | – | – | – | – | – |
| 8 | Attention and transformers, visually | – | – | – | – | – | – |
| 9 | Training at scale, and why big models are overconfident | – | – | – | – | – | – |
| 10 | How an LLM writes, one token at a time | – | – | – | – | – | – |
| 11 | Structured outputs and JSON mode | – | – | – | – | – | – |
| 12 | RAG and memory | – | – | – | – | – | – |
| 13 | Agents: Observe, Decide, Act | – | – | – | – | – | – |
| 14 | Where agents break | – | – | – | – | – | – |
| 15 | System 1 and System 2 | – | – | – | – | – | – |
| 16 | Inside Jev: what we know and what we don’t | – | – | – | – | – | – |
| 17 | The type system: choice, score, noul | – | – | – | – | – | – |
| 18 | Testing Jev’s calibration yourself | – | – | – | – | – | – |
| 19 | The Jevons paradox of decisions | – | – | – | – | – | – |
| 20 | The bake-off: six ways to make a decision | – | – | – | – | – | – |
| 21 | Act, review, or escalate | 2,660 | 15 (incl. summary) | 7 + summary | ok | pass | 0 |
| 22 | A catalog of decision patterns | – | – | – | – | – | – |
| 23 | First calls, and the mock that makes them free | – | – | – | – | – | – |
| 24 | A hybrid agent: Jev decides, the LLM reasons | – | – | – | – | – | – |
| 25 | Case study: SOC alert triage | – | – | – | – | – | – |
| 26 | An applications gallery | – | – | – | – | – | – |
| 27 | Build your own System One model | – | – | – | – | – | – |
| 28 | Capstone: a production decision service | – | – | – | – | – | – |
| 29 | What changes now | – | – | – | – | – | – |

## How to resume

1. `pip install -r requirements.txt && pip install -e . && make fonts`
2. `make test` then `python tools/build_figures.py chNN` for the chapter in progress.
3. Write `chapters/chNN.qmd`, `labs/chNN.py`, `figures/src/chNN.py`.
4. `python tools/run_labs.py chNN`, `python tools/check_listings.py chNN`, `python tools/voice_check.py chapters/chNN.qmd`.
5. `quarto render --to pdf`, then look at the pages (`python tools/contact.py _book/*.pdf A B out.png`).
