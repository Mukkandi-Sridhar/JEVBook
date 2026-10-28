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

Our material is Tarkika and examples invented for this book. The transcript's *method* (section 7) is
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

## 7. The soul of the book: understanding, step by step

The reader should keep having the feeling "now I understand why", and want the next one. That feeling does **not**
come from clever lines, metaphors or slogans. Lines like "a model is a brain in a jar" or "the closest paragraph is
not always the right one" sound smart and teach nothing; a reader can repeat them without understanding anything.
They are banned.

### 7.1 How the transcript actually does it

Look at how the transcript explains an agent. There is no metaphor. There is a chain of plain questions, each with
an obvious answer:

1. What does the model do? It takes text and answers in text. That is all.
2. Can it search the web, read a database, send an email? No. It cannot do any action.
3. What can do an action? Code. A function. That is all a tool is.
4. Can that code understand a sentence typed by a person? No.
5. So the model understands language but cannot act, and the tool can act but cannot understand language.
6. Put them together, and you have an agent.

Then the next idea grows out of this one: if the tool's job is to *fetch information*, the agent is doing
retrieval-augmented generation. The name is unpacked word by word, and RAG stops being a new subject. It is the
same agent with a particular kind of tool.

The understanding comes from three things:
- **each step is too simple to doubt**, so the reader agrees at every step;
- **the conclusion is reached by the reader**, a moment before the book states it;
- **each new idea is built from the one before**, so the book feels like one line of thought.

### 7.2 Our version of the method

Every concept is introduced as a short reasoning chain in this order:

1. **Start from what the reader already knows** (an earlier module, ordinary software, everyday life).
2. **Ask plain questions with plain answers** ("Can it…? No." "What can? …"), each one a short sentence.
3. **Reach the gap**: the thing that is missing or breaking.
4. **Let the reader fill the gap**, then state the solution in ordinary words.
5. **Only then give the name** of the concept, and unpack the name if it is a phrase or an acronym.
6. **Grow the next idea from this one.**

Example in our own words, for short-term memory:

> A Tarkika customer asks, "Where is my order?" The system looks it up and answers. The customer then types, "Okay,
> and can I return it?" The model replies, "Return what?" Why does it not know? Each call to the model is separate.
> The model receives only the text in that one call, and nothing else. The earlier question is not in that text, so
> for the model it never happened. Then how does any chat app remember? It sends the earlier messages again, every
> time, together with the new one. That is all short-term memory is: the conversation so far, sent again.

Nothing in it is clever. Every sentence is obvious. The understanding at the end is the reader's own.

### 7.3 Devices that support the chain

Use these when they help the chain. They are ways of reasoning, not ways of decorating sentences.

1. **Two things that each fail alone** and work together (model and tool; keyword search and meaning search).
2. **Remove the jargon**: show that an impressive term is a plain thing ("a tool is a function"; "a skill is a set
   of instructions kept in a folder"; "a summariser is one more call to the model").
3. **Come back to text**: the model only receives text, so memory, tools, retrieval and skills are all ways of
   deciding which text to send.
4. **Ask whether a step is needed**: every extra model call adds time, cost and one more thing that can fail.
5. **Show the case where the common belief breaks** (more context can make answers worse; the most similar text is
   not always relevant), and show it with a real example, not a slogan.
6. **One question instead of a list**: "where is the information stored?" leads to vector, keyword, graph and SQL
   search, instead of a list of ten RAG types.
7. **Compare with people** (a new employee, a doctor's notes), then say where the comparison stops.
8. **Work out a number** the reader can check with a pen.
9. **Build it, then name it.**

### 7.4 Threads that run through the book

These are stated plainly when they come up, never as catchphrases:

1. The model only receives text; most engineering is deciding which text to send.
2. The model suggests an action; your code checks it and decides whether it happens.
3. Each extra model call adds cost, waiting time and a new place to fail.
4. You only know a system works if you have tested it on cases you wrote down.
5. Most failures happen where two parts meet: retrieval and the model, the model and a tool, the agent and a person.

### 7.5 Keeping the reader reading

- **Every page moves the reasoning forward**: a new step, a new case, a number, or the next idea growing from the
  last. A page that only repeats is cut.
- **End each section with the question the next section answers**, in plain words ("The answer is right, but it
  took nine seconds. Where did the time go?").
- **End each module with a real problem the reader cannot yet solve**, which the next module solves.
- **Section titles are plain questions or plain statements of the topic** ("Why does the model forget the earlier
  message?"), not catchy phrases.
- **No paragraph without a case**: every general statement is followed within a few lines by Tarkika, a number or a
  picture.

### 7.6 What "philosophical" means here

It means the reader understands *why* things work, and learns to judge like an engineer. It does not mean
metaphors, aphorisms, grand statements or quotations. The depth comes from the reasoning, not from the wording.

## 8. Order of work

1. Build the design sample (module opener, one section with every block, module end). Get approval.
2. Write **Module 2** (*What AI engineering is*) first, as the voice sample for the whole book. Get approval.
3. Then Module 1 (Python), and onward in order, one module per review.
4. Part I drafts that already exist are rewritten into Modules 2 and 3 under these rules, not patched.
