# How this book gets written

This is the working agreement for every page of *Ship Real AI*. `STYLE.md` holds the sentence rules, `DESIGN.md`
the page design, `CONTENTS.md` the topics. This file says how a module goes from nothing to finished, and the strict
rules that apply on the way. When two files disagree, this one wins.

## 1. The standard

- **Quality over quantity.** No module is long because there was more to say. It is as short as the idea allows.
  Target: 8 to 14 B5 pages a module, about 250 to 320 pages for the whole book.
- **Every page earns its place.** If a reader could skip a paragraph and lose nothing, it is cut.
- **Every claim is right on the day of printing.** Checked against a primary source or worked out on the page.
- **A reader should finish each module able to do something**, and to explain it to an interviewer.

## 2. The backbone: how the transcript is used

The 15-day course transcript is the model for *how to teach*. For every topic, before drafting, I re-read the part
of `teaching-analysis/notes.md` that covers it and ask:

1. What problem did the teacher show first, and how did she make the learner feel it?
2. Where did she ask the learner to guess before telling?
3. What did she build by hand before showing the library?
4. What did she run, break and fix, changing one thing at a time?
5. Which close terms did she separate, and with what question?
6. What number did she work out on the board?
7. What earlier idea did she connect it to?
8. What interview phrasing did she give?

The module must answer the same eight questions **with our own problem, our own example and our own words**.

**Never reused from the transcript** (they belong to that course):
- its examples and running jokes: the cricketer questions, the "who is she" follow-ups, AuthService,
  OrderManager/OrderHandler, the to-do app, the portfolio site, the movie director graph, the "middle class" joke;
- its project briefs (the coding-agent capstone, the trading agent, the infra SaaS);
- its code, file names, folder layout, slide order and day order;
- any sentence, even a short one.

Our material is Tarkika and examples invented for this book.

## 3. How each module is made (the seven steps)

1. **Research.** Read the primary sources for the topic: original papers, official documentation, engineering
   write-ups from teams that run it in production. Notes go in `research/<module>.md` with links. Two sources at
   least for every fact that will be printed. Anything that changes monthly goes to the version register, not the
   main text.
2. **Map.** Write the module's section map in `CONTENTS.md` style: for each section the problem, the "try first"
   question, the mechanism, the name, the rule and the trade-off. Choose the worked numbers and the visuals here.
3. **Visuals first.** Draw the figures before writing the prose. If the idea cannot be drawn, it is not yet
   understood well enough to write about.
4. **Draft.** Write in one pass, following `STYLE.md`.
5. **Check.** Run every check in section 6. Run every code block.
6. **Render.** Build the PDF in colour and in greyscale; look at every page.
7. **Review.** Send the module to the author. Nothing moves to the next module until it is approved.

## 4. Sentence rules (the short version of `STYLE.md`)

1. **Say one thing per sentence.** Most sentences under 20 words. Vary the length so the text has a natural rhythm.
2. **The next sentence follows from this one.** If a sentence could be moved anywhere, it does not belong.
3. **Concrete before abstract.** A number, a name or a message from Tarkika comes before any general rule.
4. **Name the thing after the reader understands it**, never before.
5. **Define a term in one plain sentence** the first time it appears. One new term per paragraph at most.
6. **Talk to the reader as "you".** Use "we" only for "you and I, working through this".
7. **Use the words an engineer says out loud.** "Use", not "utilise". "About", not "approximately".
8. **Every "it depends" names what it depends on.**
9. **State limits plainly.** If something fails, say when and why.
10. **No sentence exists to sound good.** If it does not inform, it goes.

### Sounding human, not machine-written

These patterns are banned because readers now recognise them as AI writing:

- "Not X, but Y" punchlines; "It's not just X — it's Y".
- Colon reveals ("The answer: context.").
- Groups of three for rhythm ("fast, cheap and reliable") when only one matters.
- Opening with a question and answering it at once, more than once a module.
- Announcing ("In this section, we will explore…"), summarising what was just said, grand closing lines.
- Stacked hedges ("may potentially help in some cases").
- Words: delve, crucial, landscape, leverage, robust, seamless, unlock, game-changer, cutting-edge, journey, realm,
  tapestry, testament, pivotal, foster, elevate, "it's worth noting", "in today's world", "let's dive in".
- Em dashes. Exclamation marks in body text.
- Perfectly balanced paragraphs that all have the same length and shape.

What human technical writing has instead: specific numbers, a real opinion ("I would start with BM25"),
an admission when something is messy, a short sentence after a long one, and the occasional dry aside.

### Example of the difference

> **Machine-sounding:** Retrieval-augmented generation is a powerful technique that leverages external knowledge to
> enhance the accuracy and reliability of large language models, unlocking new possibilities for enterprise AI.
>
> **Our voice:** A customer asks whether opened earbuds can be returned. The model has never seen Tarkika's return
> policy, so it guesses. RAG fixes this by finding the right paragraph of the policy and putting it in front of the
> model before it answers.

## 5. Visual rules

Each module has, at minimum:

- **The system map** on its opener, with the module's layer shaded.
- **One pipeline or architecture diagram**: numbered boxes and arrows, drawn the same way across the book.
- **One comparison visual**: two approaches side by side, or a before/after from a real run.
- **One worked-numbers block** set out line by line.
- Where a tool's output matters: a **real screenshot or trace from our own runs** (never from someone else's
  product page or course), redrawn cleanly if the original is cluttered.

Every figure:
- is our own drawing, made with the book's figure tools;
- has a caption that says what to notice, not what the figure is;
- reads in greyscale (labels and shapes, not colour alone);
- is referred to in the text before it appears.

## 6. Checks before a module is sent

**Accuracy**
- [ ] Every fact has a source in `references.bib`, or is worked out on the page.
- [ ] Every number about Tarkika is marked as an assumed example.
- [ ] No model name, price or spec version in the main text (they go to the version register).
- [ ] Every code block runs as printed, on the stated versions.

**Originality**
- [ ] No sentence is copied or closely paraphrased from any source, including the transcript.
- [ ] No transcript example, project or code appears (list in section 2).
- [ ] Quotations are short, marked and cited.

**Teaching**
- [ ] Each section follows problem → try first → mechanism → name → rule → trade-off.
- [ ] Each new term is defined in one sentence at first use.
- [ ] The module opens by naming the earlier idea it builds on.
- [ ] Worked numbers can be followed with a pen.

**Voice**
- [ ] Banned words and patterns search returns nothing.
- [ ] Read-aloud test: every paragraph sounds like a person explaining to a colleague.
- [ ] Average sentence length under 18 words; no paragraph over 5 sentences.

**Layout**
- [ ] No heading at the foot of a page; no code block split across pages.
- [ ] Colour and greyscale PDFs both checked page by page.

## 7. Order of work

1. Build the design sample (module opener, one section with every block, module end). Get approval.
2. Write **Module 2** (*What AI engineering is*) first, as the voice sample for the whole book. Get approval.
3. Then Module 1 (Python), and onward in order, one module per review.
4. Part I drafts that already exist are rewritten into Modules 2 and 3 under these rules, not patched.
