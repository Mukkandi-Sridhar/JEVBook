# Teaching-method analysis

Source: a 15-day live course transcript on agentic AI system design (30,119 lines, read in full; running notes in
`notes.md`). The transcript is someone else's paid course. **We take only the method from it:** how the teacher
builds sentences, makes points stick, makes hard ideas easy and links topics. We take none of its content,
examples, code, project briefs, structure or order. The book's material stays our own (Kaveri Kart, our examples,
our chapter plan).

## 1. The method in one paragraph

Every topic starts from a problem the learner can feel. The learner is asked how they would solve it before anything
is named. The teacher draws the flow as numbered steps, runs it, lets it fail, traces the failure and changes one
thing at a time. The concept's name comes last, once the learner already understands it. Numbers are worked out by
hand. Each new idea is tied to one the learner already has (an earlier lesson, ordinary software engineering, or
daily life). Every design question ends with "it depends", followed by the conditions that decide it. Recaps are
short questions asked again and again.

## 2. How sentences and phrases are built

1. **Short, spoken sentences.** One claim per sentence, often under ten words. "Everything we send to an LLM is
   text." "Agent is LLM plus tools."
2. **Definition by equation.** A new thing is written as a sum of known things: agent = LLM + tools; skill =
   instructions + references + examples (+ scripts), packaged; agentic system design = normal HLD + agentic parts.
3. **"Fancy term, simple idea."** She says outright that a term only sounds hard: "tenants is just a fancy word for
   customers", "harness: if you're not the model, you're the harness". This takes the fear out before the definition.
4. **Close terms told apart.** Indexing vs incremental re-indexing; concurrency vs parallelism; prompt caching vs
   semantic caching; fusion vs reranking; offline vs online evals; MLOps vs LLMOps. Each pair is split by one
   question ("does fusion make a model call?").
5. **Acronyms unpacked word by word** before use (RAG, MCP, ReAct, TTL, TTFT, mtime), and checked later: "what does
   ReAct stand for?"
6. **Exact state words.** She corrects "in progress" to "pending" for a task that has not started. Precise nouns for
   states, statuses and errors.
7. **Interview vocabulary taught on purpose:** "say *destructive tasks*, *critical tasks*"; "say *debouncing*
   whenever you say re-indexing". The term is given as something to *use*, not just know.
8. **Conditional rules.** "If changing a component changes AI behaviour, give it a version." "If the data changes
   fast, keep the TTL low." A rule is always stated with its trigger.

## 3. How strong points are made

1. **One memorable rule per topic**, said more than once: "version everything"; "static content first"; "no one
   correct design"; "profile before you cache".
2. **A failure story first.** Rename `OrderManager` to `OrderHandler`, ask about it, the agent says it doesn't exist:
   now re-indexing matters. Cache one wrong web result and every similar question gets the wrong answer, fast.
3. **Arithmetic as proof.** Price sheet → 10 requests → with and without cache, worked line by line. 0.95 × 0.95 ×
   0.95 ≈ 85% to show errors compound. Four shards at 5, 3, 4 and 8 seconds → you wait 8. The number does the
   persuading.
4. **Prediction before each run.** "Hit or miss?" → run → "change one word: now?" → run. The learner commits to an
   answer, so the result sticks.
5. **Same input, one knob changed.** Approve vs reject; threshold 0.8 vs 0.75; TTL 2 s vs 10 s; small vs large model.
   Only one variable moves.
6. **Pros and cons, always.** "Just because we can cache doesn't mean we should." Each option comes with when it
   fits and when it is a nightmare. Real vendors with opposite designs are shown so learners see trade-offs are
   normal.
7. **Turning the design on itself.** "When would my code be a nightmare?" Learners attack the teacher's own design.
8. **"It's not the model."** When a demo misbehaves because of state or wiring, she says so ("that is not an LLM
   problem"), which teaches the learner where to look.

## 4. How hard things are made easy

1. **Learners invent it first.** "Don't read the docs. How would you implement human approval?" "Notice every skill
   file starts with a name and description. What must be happening?" Learners reach progressive disclosure, a query
   classifier, or a hybrid design before she names it.
2. **What happens inside, then the one-liner.** Build the mechanism by hand (task table, result hand-off, debouncer),
   then show that a framework does it in one line. "If you only want to use it, it's one line. We build it to
   understand it."
3. **Theory skipped where it isn't needed.** Topological sort without data structures: "every task you depend on
   comes before you." KV cache in one line, "for those who know internals".
4. **Concrete timelines for time-based ideas.** Debouncing: change at 0 s, wait 5 s; change at 3 s resets; index at
   8 s. Told twice, then mapped onto code.
5. **Shrinking numbers for search ideas.** 1 million documents → filter by team → 10,000.
6. **Everyday analogies, kept short.** Book index → index; unit tests → golden dataset/offline evals; YouTube
   thumbnails → A/B testing; Git merge conflicts → many people editing an indexed codebase.
7. **Drop to a diagram when code loses people.** "Everyone's code is hard to follow until you debug it yourself."
   The test she sets: can you say why this is in this layer and why this step follows that one?
8. **Honest mistakes in front of learners.** Version mix-ups, an agent confused by duplicate tools, a token limit too
   low. She finds the cause aloud. Learners see debugging as normal.

## 5. How topics are connected

1. **Bridges back to earlier topics:** deterministic vs model-based guardrails mirror formula metrics vs
   LLM-as-judge; ReAct explains the repeated calls that needed call limits; short-term memory is implicit caching;
   the planner's task table is also caching.
2. **Bridges to ordinary engineering:** rate limits, atomic updates, retries with backoff, sharding, canary and
   blue-green are named as "normal HLD", and only the agent-specific part is taught in depth.
3. **One architecture map, grown over time** (context, agent, safety, quality, observability, freshness, caching).
   Each new topic is placed on the map.
4. **One checklist carried into new domains.** The same questions (actions, RAG sources, search type, skills, tools,
   classifier, memory, freshness triggers, context, observability, evals, guardrails, model per job) are asked for a
   different product. Learners see the method transfers.
5. **"Who are we replacing?"** A coding agent replaces a developer; an infra agent replaces an SRE. List what that
   person does, and the requirements follow.
6. **Cliffhangers and planted terms.** Topics are named early ("we'll need this for X later") so they feel expected
   when they arrive.

## 6. How terms are introduced

The order is steady:

1. a problem or a failing run;
2. the learner's own idea of a fix;
3. the mechanism, in plain words or a timeline;
4. the name of the concept;
5. the formal word, if there is one (cycle → directed acyclic graph);
6. a one-line rule for when to use it;
7. the interview phrasing;
8. a recall question in a later lesson.

## 7. Interview framing, used throughout

- Vague questions are vague on purpose: ask follow-ups and **call out assumptions** ("can I assume chapters, sections,
  four or five paragraphs a page?").
- Answer in a structure, not with a reflex. "System slow" → time each stage → then decide. "Bad answers" →
  retrieval or generation? "Quality fell with no code change" → measure, confirm the stage, compare query logs,
  check every non-code version.
- Put numbers on the assumptions (10,000 pages × 4–5 paragraphs = 40–50k chunks) and say whether that is workable.

## 8. What does not carry over to a book

- Live energy prompts ("yes?", "are you awake?"), pep talks, feedback requests, course promotion, personal stories
  about the teacher's own career.
- Long, unedited code walk-throughs.
- Repetition that only works aloud. In print, say it once well, then use one recall question later.
- Frequent rhetorical questions. A book can ask one question and give the reader a moment ("Before reading on, …"),
  but not a string of them.

## 9. What changes in our book

The concrete rules are in `STYLE.md`, section 6 ("Teaching method"). Part I will be revised against them, and every
new chapter will be checked against them.
