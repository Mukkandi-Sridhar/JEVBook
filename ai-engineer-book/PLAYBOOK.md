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

Our material is Tarkika and examples invented for this book. The transcript's *devices* (section 7.2) are
used freely; its *sentences and examples* never are.

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

## 7. The soul of the book: insight on every page

This is not a fact book. Facts are the floor, not the goal. The goal is that a reader keeps having small moments of
"oh, so *that's* what it is", and wants the next one. The transcript did this again and again. Its best line on
agents put two weaknesses side by side: the model can think but cannot act, a tool can act but cannot think. Put
them together and the agent explains itself. Nothing was memorised; the reader *saw* it.

Every module is written for those moments.

### 7.1 The big idea of each module

Each module is built around one idea that changes how the reader sees the topic, stated in the opener as a short
paradox or question, and paid off by the end. Examples of the kind of idea (our own wording):

| Module | The big idea |
|---|---|
| What AI engineering is | A model is a brain in a jar. A tool is a pair of hands with nobody to guide them. Wire the two together and you have an agent. |
| Tokens | The model never reads words. It reads pieces, and you pay by the piece. |
| Embeddings | Two sentences can share no words and mean the same thing. An embedding is how a machine notices. |
| The decision layer | Making the model answer is easy. Knowing when it should stay quiet is the job. |
| Calibration | A confident model and a correct model are two different machines. |
| Prompts and context | The model knows only what is on the page in front of it, at this moment. |
| Prompt caching | You pay again for words the model read a second ago, unless you put them in exactly the same place. |
| RAG | The closest paragraph is not always the right one. |
| Hallucination | The model is not lying. It is completing the sentence. That is the problem. |
| Evals | Without a test set, "it feels better" is the only number you have. |
| Memory | The model forgets you the moment it answers. Every memory is text the system chose to send back. |
| Agents | Ten steps that are each 95% right finish correctly only six times in ten. |
| MCP | Every company used to make its own plug. MCP is an agreement on the shape of the socket. |
| Planning | A long task is many short tasks that remember each other. |
| Caching | A cache that remembers a wrong answer serves it faster. |
| LLMOps | Change one word in a prompt and you have shipped a new product. |

### 7.2 Insight devices (the transcript's methods, with our own content)

Use these on purpose. Each module uses at least four of them.

1. **Two halves make a whole.** Show two things that each fail alone and succeed together (model + tool;
   keyword search + meaning search).
2. **Strip the fancy word.** Show that an impressive term is a plain thing underneath: a tool is a function; a skill
   is instructions in a folder; a summariser is one more model call. The reader loses their fear of the jargon.
3. **Everything is text.** Bring each new feature back to the one truth: the model only ever sees text. Memory,
   tools, retrieval, skills are all ways of choosing which text to send.
4. **Just because you can.** Every extra model call costs time, money and a new way to fail. Ask whether it is
   needed before adding it.
5. **The obvious is wrong.** State what most people assume, then show the case where it breaks (more context makes
   answers worse; the most similar text is not the most relevant; temperature 0 still varies).
6. **The question behind the list.** Instead of listing ten types, ask the one question that produces them
   ("where does the knowledge live?" gives vector, keyword, graph and SQL search).
7. **The human mirror.** Compare the system with how people behave (a new employee, a doctor's case file, someone
   taking notes), then show where the comparison stops.
8. **The number that surprises.** A small calculation whose result the reader did not expect.
9. **Same model, different system.** Show that the difference between a weak and a strong product is everything
   around the model.
10. **Build it, then name it.** The reader builds the mechanism in their head before learning what the world calls it.

### 7.3 Threads that run through the whole book

Five ideas return in every part, so the book reads as one argument and not as 23 separate lessons:

1. **The model only sees text.** Everything else is choosing which text.
2. **The model proposes; your code decides.** Nothing acts without passing through your rules.
3. **Every call has a price.** In rupees, in seconds and in new ways to fail.
4. **Trust is measured, never assumed.** If you have not tested it, you do not know it.
5. **Systems break at the joins.** Between retrieval and generation, between the model and the tool, between the
   agent and the person.

When a module touches one of these, it says so ("This is the first thread again: …"). By the end, the reader owns
a way of thinking, not a pile of facts.

### 7.4 Page-turner rules

- **Every page gives something new**: a mechanism, a number, a reversal or a connection. A page that only repeats
  is cut or merged.
- **Every section ends on its insight line**, the one sentence a reader would underline. It is short, concrete
  and in our own words. It becomes the section's Rule block.
- **Open a question before closing one.** Each section ends by raising the problem the next section solves.
- **Each module ends with a puzzle** that the next module answers.
- **Section titles make a claim or ask a real question** ("Why the model forgets you", "The closest paragraph is
  wrong"), never a bare label ("Memory", "Retrieval").
- **No lecture.** Every abstract paragraph is followed within a page by Tarkika, a number or a picture.

### 7.5 What "philosophical" means here, and what it does not

It means: ideas that make the reader think about *why* systems behave as they do, and how a good engineer judges.
It does not mean: vague musing, grand statements, quotes from famous people, or opinions without a case behind
them. Every big idea is earned by a concrete example on the same page.

## 8. Order of work

1. Build the design sample (module opener, one section with every block, module end). Get approval.
2. Write **Module 2** (*What AI engineering is*) first, as the voice sample for the whole book. Get approval.
3. Then Module 1 (Python), and onward in order, one module per review.
4. Part I drafts that already exist are rewritten into Modules 2 and 3 under these rules, not patched.
