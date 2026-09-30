# Unverified claims and story slots (release v1.0)

Before the v1.0 build, the manuscript carried two kinds of draft marker, both hidden in print: `[[VERIFY]]` after a
claim nobody had checked against its source, and `[[AUTHOR STORY: …]]` where a first-hand story from the author
belongs. The release needed zero markers in the source, so they were removed without changing a word of the printed
text. This file is the record of what they marked. The claims are **still unverified**: the printed book reads
exactly as it did. Most are cited, attributed or labelled vendor-reported in the text; a few are not (for example
"some early critics" in Chapter 21). Check them against their sources, or soften them, before a second printing.

## Claims marked [[VERIFY]] (37)

Line numbers are from the manuscript before the markers were removed. The text is what came just before the marker.

| File | Line | Claim (text before the marker) |
|---|---:|---|
| `index.qmd` | 9 | … class of **System One models**: models that don't write at all, only answer typed questions with probabilities, in a single fast pass [@typesafe2026] |
| `chapters/ch01.qmd` | 222 | …In September 2026, a start-up called TypeSafe AI released a model built for those checkbox moments |
| `chapters/ch08.qmd` | 4 | …Intuition is nothing more and nothing less than recognition. |
| `chapters/ch08.qmd` | 14 | …When TypeSafe AI released Jev, it didn't call it a better LLM. It called it the first of a new class: a **System One model** [@typesafe2026] |
| `chapters/ch09.qmd` | 16 | …When I wrote this book, Jev had been public for a couple of weeks, in early access, and I didn't have an API key |
| `chapters/ch09.qmd` | 95 | …nd its launch coverage report end-to-end latency of roughly 70 to 500 milliseconds, and "two orders of magnitude" faster than LLMs on System One tasks |
| `chapters/ch09.qmd` | 99 | …dramatic speed multipliers in the launch material compare Jev with slow *reasoning* models, which think for a long time before answering [@regolo2026] |
| `chapters/ch09.qmd` | 101 | …The price is where the story gets interesting. The listed price is \$0.042 per million input tokens, with output free |
| `chapters/ch09.qmd` | 111 | …ying the video game Doom, making decisions from a text description of the game state about ten times a second, at a reported cost of about \$7 an hour |
| `chapters/ch09.qmd` | 121 | …s move. And by design, it gives no reasons, only probabilities. Some early critics called that a compliance problem for regulated uses [@datacamp2026] |
| `chapters/ch11.qmd` | 16 | …TypeSafe's: Jev returns *calibrated* probabilities. Its training method, RLCD, is named after that goal [@typesafe2026] |
| `chapters/ch11.qmd` | 18 | …rated": useful, yes, but treat its outputs as scores, not probabilities, because calibration depends on *your* data, which Jev never sees [@molas2026] |
| `chapters/ch12.qmd` | 4 | …We tend to overestimate the effect of a technology in the short run and underestimate the effect in the long run. |
| `chapters/ch12.qmd` | 22 | …A model whose name is short for Jevons |
| `chapters/ch12.qmd` | 42 | …keep a candle's worth of light. They lit streets and buildings and kept them lit all night, and use grew far faster than the price fell [@fouquet2006] |
| `chapters/ch12.qmd` | 54 | …reserve "backfire" for the case where it more than cancels the saving. How often full backfire happens with energy is still argued over [@sorrell2009] |
| `chapters/ch12.qmd` | 60 | …TypeSafe has said the name nods to Jevons: that cheaper intelligence leads to wider use, not less of it |
| `chapters/ch12.qmd` | 60 | …en cheaper AI models briefly rattled investors and several technology leaders reached for Jevons to argue that cheaper AI would mean more AI, not less |
| `chapters/ch13.qmd` | 98 | …babilities arrive as numbers in a fixed shape. The mock always gives the same answer to the same question. Whether real Jev does is something to check |
| `chapters/ch13.qmd` | 145 | …Wolpert and Macready proved that about search and optimisation [@wolpert1997] |
| `chapters/ch15.qmd` | 188 | …Alexander was an architect writing about towns and buildings [@alexander1977] |
| `chapters/ch16.qmd` | 129 | …These are the mock's token counts, not the real tokeniser's |
| `chapters/ch16.qmd` | 158 | …leaves to the server, such as exact rate limits, timeouts under load and the precise meaning of `confidence`, can only be learned against the real API |
| `chapters/ch16.qmd` | 171 | …Dijkstra's point [@dijkstra1970] |
| `chapters/ch17.qmd` | 114 | …Knuth was warning programmers against tuning code before measuring it [@knuth1974] |
| `chapters/ch18.qmd` | 4 | …Everybody has a plan until they get punched in the mouth. |
| `chapters/ch18.qmd` | 128 | …Deming said something like this often, in talks and seminars |
| `chapters/ch19.qmd` | 75 | …'s mock is a simple word-matcher, and "I can't log in" shares words with "the app isn't working". Real Jev would do better or worse; I can't say which |
| `chapters/ch19.qmd` | 87 | …egal weight. Lending, hiring, benefits and medical decisions face rules in many places about automated decision-making and the right to a human review |
| `chapters/ch19.qmd` | 111 | …Maslow was talking about scientists and their methods [@maslow1966] |
| `chapters/ch20.qmd` | 76 | …his is the most likely way a model like Jev is trained to be calibrated, and in Chapter 9 I guessed that TypeSafe's RLCD might build on a rule like it |
| `chapters/ch20.qmd` | 157 | …Feynman's blackboard |
| `chapters/ch21.qmd` | 4 | …Hope is not a strategy. |
| `chapters/ch21.qmd` | 69 | …Jev gives no reasons, only probabilities. Some early critics saw that as a problem for audits |
| `chapters/ch21.qmd` | 141 | …Vogels has said this in many talks |
| `chapters/ch22.qmd` | 4 | …The future is already here. It's just not very evenly distributed. |
| `chapters/ch22.qmd` | 79 | …Every item in @fig-unknowns is open |

## Places for the author's own stories (20)

None of these were written; the book reads complete without them. To add one, write it where the topic fits.

| File | Line | Topic |
|---|---:|---|
| `index.qmd` | 29 | why you wrote this book: the moment you realised most of your agent's work was small decisions |
| `chapters/ch01.qmd` | 40 | AttendX, a rule-based system you built or used, and the day it met a case its rules didn't cover |
| `chapters/ch03.qmd` | 129 | AttendX or SIGNAL: a model trained on rebalanced or filtered data, and what its probabilities looked like once it met the real mix |
| `chapters/ch07.qmd` | 63 | VMG-RAG: how you decided when the system should say "I don't know" rather than answer from a weak match |
| `chapters/ch07.qmd` | 103 | SIGNAL, or another agent you built: the moment you realised most of its steps were small decisions |
| `chapters/ch07.qmd` | 132 | the police FIR agent: a case where an automated step should never have been allowed to act alone |
| `chapters/ch11.qmd` | 105 | SIGNAL or the police FIR agent: where the first few hundred labels came from, and whose time they cost |
| `chapters/ch12.qmd` | 62 | a decision you once wanted a system to make on every item, but couldn't justify the cost or wait, e.g. in AttendX or SIGNAL |
| `chapters/ch13.qmd` | 129 | AttendX or VMG-RAG: a time you chose a simple rule or a classic model over something newer, and why that was the right call |
| `chapters/ch14.qmd` | 83 | the police FIR agent, and how you decided which complaints an officer had to read before anything else happened |
| `chapters/ch15.qmd` | 172 | which of these patterns you reached for first in a real system (the police FIR agent, SIGNAL or AttendX), and what went wrong before you did |
| `chapters/ch16.qmd` | 155 | the first time an API change or an unpinned model version broke something of yours in production, and how you found out |
| `chapters/ch17.qmd` | 66 | the police FIR agent or SIGNAL: a step that never crashed but quietly did the wrong thing, and how reading its answers, not its errors, found it |
| `chapters/ch17.qmd` | 98 | an agent you built where most of the LLM calls turned out to be small decisions, and what changed when you moved them out |
| `chapters/ch18.qmd` | 47 | what the first design review of a system like this looked like, and the question from a stakeholder you didn't expect |
| `chapters/ch19.qmd` | 89 | a decision in the police FIR agent or AttendX where you deliberately kept a person as the final decider, and what the model did instead |
| `chapters/ch20.qmd` | 141 | the first model you trained whose probabilities you had to fix before anyone could use them, and how you noticed |
| `chapters/ch21.qmd` | 71 | a time someone asked you to explain an automated decision long after it was made, and what you wished you had logged |
| `chapters/ch21.qmd` | 125 | leading an intern team: how you split a service like this into parts people could own, and which checklist item a newcomer caught or missed |
| `chapters/ch22.qmd` | 71 | how your own work changed once you started treating decisions and generation as different jobs, in SIGNAL or the FIR agent |
