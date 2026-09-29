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
| 1 | What “learning” means | 2,780 | 14 | 6 + summary | ok | pass | 1 |
| 2 | Probability is the language of decisions | 1,899 | 12 | 6 + summary | ok | pass | 0 |
| 3 | Data, loss and gradient descent | 1,862 | 12 | 7 + summary | ok | pass | 0 |
| 4 | Calibration: when 0.8 really means 80% | 2,076 | 12 | 6 + summary | ok | pass | 0 |
| 5 | From probabilities to actions | 1,683 | 12 | 6 + summary | ok | pass | 0 |
| 6 | Neurons to networks | 1,588 | 10 | 6 + summary | ok | pass | 0 |
| 7 | Embeddings: meaning as geometry | 1,564 | 12 | 6 + summary | ok | pass | 0 |
| 8 | Attention and transformers, visually | 1,539 | 10 | 6 + summary | ok | pass | 1 |
| 9 | Training at scale, and why big models are overconfident | 1,581 | 12 | 6 + summary | ok | pass | 0 |
| 10 | How an LLM writes, one token at a time | 1,611 | 10 | 5 + summary | ok | pass | 0 |
| 11 | Structured outputs and JSON mode | 1,680 | 12 | 6 + summary | ok | pass | 0 |
| 12 | RAG and memory | 1,507 | 10 | 6 + summary | ok | pass | 1 |
| 13 | Agents: Observe, Decide, Act | 1,500 | 10 | 6 + summary | ok | pass | 0 |
| 14 | Where agents break | 1,568 | 12 | 5 + summary | ok | pass | 0 |
| 15 | System 1 and System 2 | 1,527 | 10 | 5 + summary | ok | pass | 1 |
| 16 | Inside Jev: what we know and what we don’t | 1,606 | 10 | 6 + summary | ok | pass | 8 |
| 17 | The type system: choice, score, noul | 1,282 | 10 | 6 + summary | ok | pass | 0 |
| 18 | Testing Jev’s calibration yourself | 1,501 | 10 | 6 + summary | ok | pass | 2 |
| 19 | The Jevons paradox of decisions | 1,941 | 14 | 6 + summary | ok | pass | 5 |
| 20 | The bake-off: six ways to make a decision | 1,876 | 12 | 7 + summary | ok | pass | 2 |
| 21 | Act, review, or escalate | 2,655 | 16 | 7 + summary | ok | pass | 0 |
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
6. `python tools/progress.py --pdf _book/*.pdf` rewrites the chapter table above.
