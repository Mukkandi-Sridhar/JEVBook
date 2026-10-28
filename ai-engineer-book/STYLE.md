# Style guide for this book

This book is separate from *Decide, Don't Generate* (the JEV book). It does not mention Jev, TypeSafe AI, Kestrel or
Harbor. It does not lean on that book either: every idea is taught here from the start.

The rules below come from the problems readers and the author found in the JEV book's drafts. Check every chapter
against them before it is called done.

## 1. Problems we had before, and the rule that fixes each one

| Problem in the JEV drafts | Rule for this book |
|---|---|
| Sentences that stood alone like slogans, with no link to the sentence before ("meaningless lines") | Each sentence follows from the one before. If a sentence could be moved anywhere in the chapter, rewrite it or cut it. |
| Key-idea boxes that were short but hard to understand | No bold headline boxes. A `{.remember}` note is one plain line (two at most) with concrete words. Read it aloud to someone outside the field. |
| Copying the JEV look (green boxes, bold key-idea headlines, the same fonts and heading style) | This book has its own design: indigo and saffron, IBM Plex Serif / Work Sans / Plex Mono, numbered sections, a large chapter number, open boxes. Never reuse JEV's colours, fonts, box names or labels. |
| Terms used before they were explained (for example "regression") | Define a term in one short, plain sentence the first time it appears. At most one new term per paragraph. |
| Results stated with nothing under them ("building rocks on air") | Build up first: an example with real numbers, then the general rule. Never state a rule the reader has not seen working. |
| Long blocks of explanation with no shape | Use numbered steps for processes, bullets for lists of three or more, and short paragraphs (2 to 4 sentences). |
| Too many tables | A table only when the reader must compare several things across the same columns. At most two tables in a chapter. Everything else is prose, steps or bullets. |
| Research-level detail, especially in probability | Teach what an applied AI engineer uses at work. If an idea is not used later in the book or in a job, cut it. No proofs, no formulas the reader cannot compute by hand. |
| Abstract explanations | Every new idea gets an everyday example first: cricket, the railway counter, a kirana shop, monsoon, exams, a bank form. Then the AI example. |
| Text that sounded machine-written | See the banned patterns in section 3. |
| Claims about the author | The author is an applied AI engineer. Do not write "I built", "I invented", "my program", or that the author is a student. Examples are presented as examples. |
| Made-up numbers presented as measurements | Every number about Tarkika is an assumed example and is written that way ("Suppose…", "In our example…"). Prices are example prices unless cited. Real figures from outside get a citation. |

## 2. Voice

- Plain Indian English. Speak to the reader as "you". The author may use "we" for "you and I, working through this
  together".
- Lakh and crore are fine for Indian amounts, with the digits written the Indian way (1,00,000). Use rupees for
  costs. Use dollars only when quoting a vendor's own price.
- Short sentences: most under 20 words, one idea each.
- Common words: "use", not "utilise"; "show", not "demonstrate"; "about", not "approximately".
- Code is short (under 15 lines), runs as printed, and every line is explained or obvious.

## 3. Banned patterns (they make text sound machine-written)

- The "not X, but Y" punchline: "The fix was not a smarter model; it was a change in where the facts come from."
  Say the positive point directly.
- Dramatic colon reveals: "The answer: context." Write a normal sentence.
- Groups of three adjectives or phrases for rhythm: "fast, cheap and reliable" when only one matters.
- Rhetorical questions in a row. One question to open a section is fine.
- These words: delve, crucial, landscape, leverage, robust, seamless, unlock, harness, game-changer, cutting-edge,
  journey, realm, tapestry, navigate (except for real navigation), "it's worth noting", "in today's world",
  "here's the thing", "let's dive in".
- Em dashes. Use a comma, a full stop or brackets.
- Sentences that only announce: "In this section, we will explore…". Just start.
- Closing lines that repeat the paragraph in grand words.

## 4. Module shape

1. A short opening: a real problem at Tarkika that the reader can feel.
2. Sections, each a plain question as its title, each built as a reasoning chain (see `PLAYBOOK.md` section 7).
3. Figures and short code where they show the idea.
4. A short close that says what changed and names the next problem.

No boxes for summaries, checklists, "remember" lines, practice, interview questions, production failures or
numbers to defend. If something matters, it is part of the reasoning in the text.

## 5. Teaching method

These rules come from studying how a strong live teacher explains agentic systems (see
`teaching-analysis/analysis.md`). We use the *method* only. All content, examples and structure are our own.

### 5.1 Order inside a section

1. Start with a problem the reader can feel: a failure, a cost, a customer complaint at Tarkika.
2. Give the reader a chance to solve it: one line, in italics, starting "Before reading on, …". At most one per
   section.
3. Explain the mechanism in plain words, as numbered steps or a timeline.
4. Only now name the concept. Then the formal term, if there is one.
5. State the rule with its trigger: "If X, do Y."
6. Show where it breaks or what it costs (the other side of the trade-off).

### 5.2 Making a point stick

- **Work the numbers.** Every cost, latency, memory or accuracy claim gets a small calculation the reader can follow
  by hand (assumed example values, marked as such).
- **One knob at a time.** When showing a change, keep everything else the same and say so.
- **Predict, then show.** Before a result, ask the reader what they expect in one short sentence.
- **Failure first.** Show the thing going wrong before showing the fix.
- **One memorable rule per section.** It becomes the section's `{.remember}` note, so it is said once in the text and
  once in the note. No more repetition than that.

### 5.3 Making hard things easy

- Define a new thing as a sum of things the reader knows ("an agent is a model plus tools, in a loop").
- Say when a term only sounds hard ("A *tenant* is just a customer").
- Split close terms with one deciding question ("Does it call the model? Then it is reranking, not fusion").
- Spell out acronyms word by word on first use.
- Build the mechanism by hand first, then show the library call that does it.
- Skip theory the reader does not need, and say you are skipping it.
- Use a timeline for anything time-based, and shrinking numbers for anything about search or filtering.
- Analogies: one short everyday picture, then straight to the AI case. Do not stretch an analogy past one paragraph.

### 5.4 Linking topics

- Each chapter opens by naming the earlier idea it builds on, in one sentence.
- When an idea mirrors an earlier one, say so ("This is the same split you saw in Chapter 3: rules versus a model").
- Ordinary engineering ideas (retries, sharding, canary releases) are named as such and covered briefly. Depth goes to
  the parts specific to AI systems.
- Keep one architecture map across the book. Each new part shows where its topic sits on that map.
- Plant terms before they are needed ("we will need this in Part VI"), but never use a term before defining it.

### 5.5 Interview and decision habits

- In `{.decision}` and `{.defend}` boxes, start with the assumptions, put numbers on them, then choose.
- Every design choice ends with "it depends on …" followed by the actual conditions. Never a choice with no
  conditions.
- Diagnosis questions are answered in a fixed order: measure, find the stage, check what changed (including
  versions that are not code), then fix.
- Teach the exact words engineers use, in plain sentences the reader can say out loud in an interview.

### 5.6 Honesty

- When an example fails for a boring reason (state, wiring, a limit), say so plainly and say where to look.
- Name the trade-offs of every approach, including the ones the book recommends.
- Show that respected teams choose differently, and why, when a real source supports it.

### 5.7 Fit with section 3

The live-teaching habits of constant questions and repetition do not carry over. One "Before reading on" line per
section is allowed. Rhetorical questions in a row are still banned. "Harness" is allowed only as the technical term
("the harness around the model"), never as a verb meaning "use".

## 6. Facts

- Every claim about a product, model, protocol, price or company gets a source in `references.bib`.
- Version numbers, model names and prices stay out of the main text where possible. They go in the dated version
  register (Appendix C), because they change monthly.
- Anything not yet checked carries `[[VERIFY]]`. It shows only in draft builds and must be gone before print.
