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
| Made-up numbers presented as measurements | Every number about Kaveri Kart is an assumed example and is written that way ("Suppose…", "In our example…"). Prices are example prices unless cited. Real figures from outside get a citation. |

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

## 4. Chapter shape

1. Title, then a short opening: a real incident or an everyday picture (half a page).
2. `{.glance}` box: three plain bullets.
3. Numbered sections that build from the example to the idea.
4. `{.remember}` notes: two or three per chapter, one line each. They are collected into the chapter checklist.
5. `{.project}` box: what we add to Kaveri Kart.
6. `{.decision}` box where the chapter has a real choice to make.
7. `{.production}` box: what goes wrong in production.
8. `{.defend}` box: the numbers the reader chose and how to justify them.
9. `{.practice}`, then `{.interview}`; answers in `back/answers.qmd`.
10. `{.nexthook}`: one line.

## 5. Facts

- Every claim about a product, model, protocol, price or company gets a source in `references.bib`.
- Version numbers, model names and prices stay out of the main text where possible. They go in the dated version
  register (Appendix C), because they change monthly.
- Anything not yet checked carries `[[VERIFY]]`. It shows only in draft builds and must be gone before print.
