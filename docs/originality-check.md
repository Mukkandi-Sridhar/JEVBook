# Originality check

A plagiarism and attribution check of *Decide, Don't Generate*, run on 30 September 2026 over the whole text:
22 chapters, the six part openers, the preface, prologue and "How to read this book", the glossary and the cheat
sheets. That's about 52,000 words of prose, with code excluded. It isn't a commercial plagiarism report (no
Turnitin-style database was available); what it did check is set out below.

## Result

No copied passages were found. Two runs of the vendor's documentation had been reproduced word for word, and three
lines were close to published phrasings; all five were rewritten. Every quotation is attributed.

## What was checked

**1. Repetition inside the book.** Every 10-word run was compared across files. There were 13 shared runs in 52,000
words, all deliberate: the glossary and cheat sheets restating chapter definitions, two "Set the threshold" boxes
(Chapters 18 and 21) restating the same cost assumptions, and the phishing-campaign week described in Chapters 14 and
18.

**2. Overlap with the sources the book draws on.** The text was compared, six words at a time, with the source excerpts
gathered while writing: TypeSafe's documentation and launch post, the Jev-Mem abstract, DataCamp, regolo.ai, Alex
Molas's post and the Doom-demo coverage.

- Found: Chapter 9 reproduced two runs from TypeSafe's documentation, "every question is evaluated in parallel and in
  isolation against the same state" and "adding questions barely changes the response time". It was cited but not in
  quotation marks. **Rewritten** as a paraphrase, citation kept.
- The Jev-Mem summary (Chapter 15), the `confidence` definition (Chapter 9, the glossary and `docs/mock-design.md`)
  and the Molas argument (Chapter 11) are paraphrased, with no run of six words in common, and each is cited.

**3. Web search for distinctive sentences.** 20 sentences were searched as exact phrases, chosen from the explanatory
passages most likely to echo textbooks or articles (overfitting, thresholds, neurons, calibration and ECE, agents,
reasoning models, the Jevons paradox, retries, monitoring, injection, constrained decoding). None matched word for
word. Three were close to published phrasings and were **reworded** to be safe:

| Chapter | Was | Close to | Now |
|---|---|---|---|
| 6 (key idea) | "Constrained decoding guarantees the shape of the answer, never its truth." | "constrained decoding guarantees structure, not truth" (TMLS) | "Constrained decoding makes the answer parse. It doesn't make it right." |
| 21 | "a monitor that cries wolf gets ignored" | the same stock phrase in public GitHub issues | "a monitor that raises false alarms soon stops being read" |
| 22 | "Somebody has to say what a mistake costs, where the lines go" | a search engine claimed a match in an Insigniam article, but the text it quoted didn't contain the line (probably a false match) | "Someone still has to decide what a mistake costs, where the lines go" |

Ideas the book shares with the wider literature (0.5 is only right when both mistakes cost the same; an agent is a
model in a loop; retries can hide failures) are standard teaching points, explained in the book's own words and
examples.

**4. Quotations.** All 45 epigraphs and pull quotes carry an attribution, and the ones from papers and books are in
the bibliography. Quoted phrases in the running text are the book's own dialogue and examples, apart from one short
phrase from the SDK's schema ("currently free of charge"), attributed to it.

**5. Code, figures and fonts.** Every figure is drawn by the book's own code. `jevkit` contains no vendored or copied
code; the mock follows the public `typesafe-sdk` interface (MIT) without copying its source. Fonts are under the SIL
Open Font License. The code licence (MIT) is declared in `pyproject.toml` and on the copyright page, but the repository has no
`LICENSE` file yet; add one before release.

## For the author before publishing

- **Permissions for longer quotations.** Short quotations used for comment are normally fair use or fair dealing, but
  publishers often ask for permission for epigraphs from works still in copyright. The longest are Christopher
  Alexander, *A Pattern Language* (47 words, Chapter 15), C. A. R. Hoare's Turing lecture (39, Chapter 13), Richard
  Sutton, "The Bitter Lesson" (30, Chapter 5), Fred Brooks, *The Mythical Man-Month* (29, Chapter 10), John Tukey
  (27, Chapter 19), the Greshake et al. abstract (Chapter 7) and the Saint-Exupéry translation (Chapter 10). Jevons,
  Adam Smith, Laplace, Hume and Butler are public domain.
- **Your stories.** The [[AUTHOR STORY]] passages you add will be your own experience; nothing to check there.
- **A commercial check.** If your publisher wants a Turnitin or iThenticate report, run it on the final PDF. This check
  covers the web through a search engine, not subscription databases.

## AI-writing check

A separate question from copying: does the text read as machine-written? No AI detector could be run here (the
services and the model weights they need are blocked in this environment), so this is a stylometric check of the
patterns detectors and editors react to. Figures are per 10,000 words of prose.

**What's absent.** Stock AI vocabulary is nearly gone: 14 hits in 52,000 words ("it's worth" 4, "genuinely" 4, a
few singles), and three of those sit inside quotations (Sutton, Wolpert). There are no em dashes, no "delve",
"tapestry", "landscape", "robust" or "seamless", no "Moreover/Furthermore/In conclusion", and only one
question-then-answer reveal.

**What's there: the drafting model's own habits.**

| Tic | Count | Per 10k words |
|---|---:|---:|
| sentences starting "That's …" | 93 | 17.9 |
| "honest", "honestly", "honesty" | 89 | 17.2 |
| sentences starting "It's …" | 63 | 12.1 |
| "exactly" | 54 | 10.4 |
| "Here's …" | 37 | 7.1 |
| "the whole" | 29 | 5.6 |
| "quiet", "quietly" | 16 | 3.1 |
| "turns out" | 12 | 2.3 |
| "not X, it's Y" and "isn't X. It's Y" | 11 | 2.1 |

"Honest" is partly the book's subject (honest probabilities), but at this rate it reads as a verbal tic.

**Rhythm.** Sentences average 13 to 16 words, and their lengths vary by about half their mean (coefficient of
variation 0.5 to 0.6) in almost every chapter. That evenness, the same short-sentence "reveal" rhythm in every
chapter, is the kind of regularity detectors pick up.

**The plain answer.** This text was drafted with an AI model, so an AI detector is likely to flag much of it,
whatever the style. Two things matter more than any score:

1. **Disclosure.** Amazon KDP asks whether a book's text is AI-generated, and many publishers and journals ask too.
   Answer it truthfully: AI-assisted drafting, with the author's direction, facts and review.
2. **Your voice.** The 20 [[AUTHOR STORY]] passages, your own edits, and your judgement on what to keep are what make
   the book yours. Cutting the tics above improves the prose, but it isn't a substitute for that.
