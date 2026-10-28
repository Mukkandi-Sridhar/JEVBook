# Running notes: 15-day Agentic AI course transcript

Notes written while reading every line, in order. Line numbers refer to the transcript file.

## Day 1 (lines 1–2650)

### Lines 1–1300
- Opening: sets purpose, asks learners *why* they joined, promises "after this there is nothing to know".
- Core frame repeated: **problem statement first** ("without this concept, what is the problem?"), then how it works, why it works, then code. "There is never one correct solution": everything is **trade-offs**, like HLD.
- Separates three AI roles: model creation, inference engineering, agentic applications. States what the course is NOT (no internals), which sets scope.
- Builds definitions by contradiction with misconceptions: "OpenAI is not an LLM, it is a model provider; ChatGPT is an application."
- LLM limitations listed one at a time, each with an everyday probe question: knowledge cutoff ("who won IPL 2026?"), stateless (follow-up "when was she born?"), fixed context window, **probabilistic / non-deterministic** (contrast with HTTP API that always returns the same shape), cannot act.
- Agent definition built from two complementary weaknesses: "LLM understands language but cannot act; a tool can act but cannot understand language; together they form an agent." Very strong pairing device.
- Then the evolution of definitions: agent = LLM + tool → LLM + context → model + harness.
- RAG = when the tool fetches information. Unpacks the acronym word by word ("augment is a fancy term for adding").
- Tool-calling flow drawn as numbered steps 1–6 (query → query+tool list → LLM says which tool → app calls tool → tool response → back to LLM → final answer). Redraws when the diagram gets messy ("let me do this once more").
- Answers learner doubts with a counter-question (Jignesh: "Do you want JSON with a 4xx in your chat reply?").
- Semantic meaning example: "why are payment failures happening?" vs code named `CheckoutException`.
- Chunking problem framed with failure scenarios: split mid-class, mid-function, same function name in different classes; then the **user-experience test**: "would you use Claude Code again if it can't answer that?"
- Frequent check-ins ("Is everyone with me?"), names learners, invites doubts, promises to answer later instead of derailing.
- Frameworks: "only the APIs change; the concepts are the same". Decides for the learner what to worry about.
- Capstone: build a Claude-Code-like coding agent; second group project (stock trading app, deep-research agent).

### Lines 1301–2650
- Explains a mechanism twice when asked, the second time more slowly and with a drawn example (recursive splitter: by class, then by function, until every chunk ≤ 256).
- **Run it, see it fail, then fix it.** Demo answers "what does AuthService do?" well, then fails "what functions are in AuthService?". Opens the trace (LangSmith) to show exactly what went to the model, which chunk came back, and why `__init__` was the last thing seen.
- Turns one knob at a time and narrates the trade-off: chunk 256 → 1500 → 2500 (fewer chunks, more tokens, more complete answer). Shows token and cost counts in the trace.
- Surprises become lessons: the 6-times tool loop → retry middleware → "who decides to retry? The LLM, because only it can judge whether the answer is good enough."
- Short definitions while answering questions: tokens vs chunks; embedding dimension trade-off (more meaning, more space); chunk size is a setting, not a standard.
- "Do not memorise code; memorise the concept and the pros and cons." Code and frameworks change.
- Plants hooks for later: "tomorrow I'll show how adding the class name to each function chunk fixes this."
- Q&A section: interview story (a fintech asking "how can I trust you with our data?") answered as 1) redact PII before the LLM, 2) self-hosted open models, 3) compare with trusting any cloud vendor.
- Career advice: interviews care less about Python, more about concepts and trade-offs; "AI cannot replace you yet on judging trade-offs".
- "Same model, different application, different results": the application's chunking, context, prompt and harness make the difference.

### Who is teaching
- Learners address the instructor as "Kirti"/"Keerti" (Keerti Purswani), with teaching assistant Amit. The instructor's own example: "Who is Keerti Purswani... what is her company's name?". Course states the material is for paid students only and asks that it not be shared outside.

## Day 2 (lines 2651–4800)

### Lines 2651–4050
- Opens with motivation and a promise: "I could tell you the types of RAG in half an hour, but that would be only theory; I want you to see the impact of every small change."
- Picks up yesterday's failed query again and fixes it a new way (adding "this function belongs to AuthService" in the docstring), showing that **the data itself is a factor** too. Builds the list: data, chunking, chunk size, embedding, model, query.
- Overlap explained with a concrete split: "5-week course" split into "5" | "week" so neither chunk knows; then "how big should overlap be? Depends on sentence length — look at your data."
- Goes one step outside scope on purpose (AST: how compilers/linters/IDE autocomplete read code), says clearly that it is optional and why it is included. Shows the tree for `x = 1 + 2` before a class.
- Contrast pairs: recursive splitter = text patterns; AST = structure and relationships.
- Removes an unfair advantage when a learner spots it ("that comment would be cheating") — honesty in demos.
- Sets demo settings to the strictest (k=1) to expose differences on a small codebase, and says why.
- Cost/latency made concrete from the trace: "5 model calls, 1.8k tokens, 12 seconds — is 12 seconds good?" → limit model calls and tool calls; result 3.4 s. Then the rule: "accuracy does not come from calling again and again; improve the input instead." "The best balance of accuracy, latency and cost — that is agentic system design."
- Learns from a live mistake (tool-call limit did nothing because the tool name was wrong) and turns it into a lesson ("limits are per tool name").
- Semantic vs exact match: "order handler" among many order functions; "would you grep 10,000 files?"; inverted index explained with a simple sentence example and a hash map.
- BM25 taught as intuition, not formula, three ideas each with a probe: term frequency with diminishing returns (200 times is not twice as important as 100), word rarity ("agent" in every doc vs "rag"), length penalty (a word in a 10-word doc vs a 1,000-word doc).
- **Concept bridges**: the length penalty idea reused to explain context rot (long context dilutes the user's query).
- Frequent mid-class revision: redraws the full flow, numbered, step by step; separates ingestion vs retrieval ("putting data into the vector DB is not RAG; it's preparing your data").
- Asks the class to classify queries ("why are my payments failing?" → semantic; "PaymentException" → lexical) before showing code.
- "Forget the fancy terms: if you had both, what would you do?" → learners invent the two answers, then names them: call both and rerank = hybrid; let an LLM decide = agentic. Corrects a common misconception (hybrid ≠ only vector + BM25; any multiple retrievers).

### Lines 4051–4800 (end of Day 2)
- **"Just because we can make an LLM call doesn't mean we should."** Each extra call costs latency, money and compute; if you always need both retrievers, skip the deciding call.
- Hybrid is "an architecture, not a technique": how to combine strategies.
- Shows the limit of each method with a pair of queries: "generate bill" gets a BM25 score of 0 against "create invoice" (no shared word), though they mean the same. Asks learners to find their own queries where each method wins or loses and post screenshots.
- Q&A clears two-different-things confusion with a clear separation: vector DB stores embeddings and does similarity; BM25 lives elsewhere (Elasticsearch); BM25's internal ranking ≠ the reranking after hybrid retrieval.
- Admits a gap in her own explanation openly: "I made some mistake in explanation; I'll make it clear tomorrow." Then opens Day 3 by fixing it.
- Answers "what is a document?" plainly: every chunk is called a document (that is LangChain's word).

## Day 3 (lines 4800–7716)

### Lines 4800–5450
- Starts by naming the confusion from the previous day and clearing it in two lines with a drawn split (vector DB | inverted index).
- Deflates hype: "people post '20 types of RAG' to sound smart; understand the core and the rest is clear."
- **Taxonomy built from one question per stage.** "Where is the knowledge stored?" → vector, lexical (sparse), graph, SQL, web, hybrid. "How do we make sure the answer is correct?" → add a validation step: corrective RAG (a separate model/session checks it), self-RAG (same model checks). "The names are stupid; it's one extra validation layer." "How do we fix weak user queries?" → query transformation (HyDE example: generate a hypothetical answer, search with that). "Too many chunks?" → summarise (RAPTOR).
- **Master frame**: draw the pipeline once; optimisation can happen at every point (ingestion, chunking, retrieval, before the LLM, after the answer); "do an extra step at any point and you have another type of RAG". Each adds latency and cost.
- Graph use cases elicited from learners first (social connections, maps), then mapped to the project (call chains, "who calls this function", UML is a graph). Movie example: "all movies by this director and producer" → which DB?
- Evidence from her own bill: shows the trace of yesterday's last call (huge tokens and money from an unbounded loop) to motivate graph and limits.
- Clarifies who writes the graph query: the LLM writes it from the schema we send; the app runs it.
- Respectful bluntness: "let's assume users write bad queries; not everyone writes good English."

### Lines 5451–6900 (evaluation)
- Introduces evaluation by quoting the class's own earlier answer back: "we said 'this looks better, this feels better' — in production, how will we know?" Moves the learner from feeling to number.
- **Analogy to something the audience already trusts**: golden dataset = unit tests for AI systems. Every change (chunking, embedding, reranking, prompt, model) must pass it.
- Builds the golden dataset in layers: query + answer is not enough → add the expected documents, so retrieval and generation can be checked separately. Then variety: summarisation, comparison, procedure, fact, ambiguous queries (with an e-commerce example for each).
- Asks the class how to create it before telling: human-written, production logs, synthetic (LLM-generated), and a mix with human review.
- **Interview question woven in**: "your evals are great but production is bad — what do you do?" → mine failed production queries, human review, add to the golden set, all future versions must pass.
- Asks the class to pause questions for 10–15 minutes while she builds the foundation; manages attention openly.
- Precision and recall taught with **one fixed scenario and changing numbers** (1,000 docs, 100 relevant; retrieve 50, 10 relevant), then several fresh numeric examples, each answered by a named learner. Plain anchors: precision = correctness ("how precise were you"), recall = completeness ("did you get everything?").
- Extreme cases to show the trade-off: fetch all 1,000 → recall 100%, precision 10%; fetch 1 → precision 100%, recall 1%. Then ties both extremes back to RAG pain (garbage = cost, latency, hallucination; too little = missing information). Domain stakes: legal and medical need completeness.
- Explains "@K" from the reason it exists (we only send K documents to the LLM).
- New metrics anchored to known terms: hit rate ← cache hit; MRR ← "how early do we find the first good one?" with four small examples and the mean.
- Admits overload and switches mode: "this is getting too much; let me show code." Pastes code piece by piece after TA feedback.
- Ends with a **summary table built live**: metric | what it measures | needs an LLM? | needs golden data? | which layer.
- Misconception contrast: faithfulness ≠ correctness (an answer can be right but unfaithful to the retrieved context: "cannot refund" retrieved, "can refund" answered).
- Ends with a fast spoken recap of all RAG types, one line each.

### Lines 6900–7716 (end of Day 3)
- Recap says the quiet part: "when I listed RAG types it felt long; now it feels normal — I was setting intuition." Tells learners that overwhelm on first exposure is expected and repetition will fix it.
- TA adds a parallel the audience knows: TDD → **EDD (eval-driven development)**.
- Q&A answers keep separating storage by query type: vector DB for meaning, inverted index for exact words, graph for relationships; "it will work in one DB, but it's not optimised for that, and the extra results become noise for the LLM".
- "Can precision and recall both be 100%? Mathematically yes, realistically rarely."
- Practical tool advice in passing (grep/wildcard search as an exact-match option; coding agents use grep heavily).
- Admits limits honestly (doesn't know Copilot's verbose option).

## Day 4 (lines 7717–9893)

### Lines 7717–8350
- Opens with rapid-fire recall questions on last week's formulas before new material (retrieval practice).
- Motivates a library by pain: "will we write these formulas again and again? No."
- "Can every evaluation be done with maths? Is 'is the answer relevant?' a formula?" → LLM-as-judge; same or different judge model; same model can be biased.
- Did the long runs before class and pasted the results into a comparison table, because live runs are slow; runs one live so learners see it is real. Sets the goal: "understand *why* precision went up when chunk size changed".
- Builds code in small pieces and marks "till here it is the same as before; this is the new part".
- Explains where each evaluation input comes from with a labelled list: question (golden set), reference (ground truth), context (what the retriever returned), answer (agent's final message).
- Notes that evaluation is offline and part of CI/CD, so latency matters less; production queries feed the golden set.
- Repeats the "evals good, production bad" interview question a second time in a new setting (spaced repetition).

### Lines 8351–9450
- **Predict, then check**: "If I change chunk size from 256 to 1500, should precision go up or down? If k goes from 4 to 1?" Learners predict, then the table confirms. Numbers back up what they saw by eye the week before.
- Reads the results table per query type: "which file imports Task and Status?" fails in semantic, shines in graph; exact error names shine in lexical; "trace the call" fails in semantic and lexical, wins in graph. Lesson: "no one solution fits all queries".
- Asks the class to choose the order of teaching ("graph RAG with or without evaluation first?").
- Graph RAG introduced as a data shape the class already knows: nodes, edges, and a triple (from, to, relationship). Asks for a yes from "every single person" at the key point.
- Shows the generated relationships ("main imports AuthService") so the abstract graph becomes concrete; acknowledges the token cost a learner points out and turns it into "understand trade-offs, then improve".
- **Ranking taught by location**: inside the database (we don't control it) vs in the application: fusion (merge ranks, no rereading, no LLM call; RRF) vs reranking (read the text again with a model; cross-encoder). Draws the production pipeline: multiple retrievers → fusion → top 100 → rerank → top 5 → answer, then says every step is optional.
- Recap by asking the class for each line (what is it good for, how is it stored).
- **Reframes the taxonomy as questions to ask yourself**: where does the information come from (retrieval), how do I improve the query, how do I validate, how do I orchestrate. "Hybrid is a retrieval strategy, self-RAG a validation strategy, agentic RAG an orchestration strategy" — one system can be all three.
- Mild humour and honesty about effort ("I spent a lot of dollars running these").

### Lines 9451–9893 (Day 4 Q&A)
- Time-series question answered with the general pattern: let the LLM write the query for the user's question, run it yourself, send the rows back to the LLM for a natural-language answer. Contrast: fixed APIs are safe but restrictive.
- Honest comparison of real products: one coding tool uses heavy RAG, another mostly grep; "both designs are possible; we'll learn both and their pros and cons."
- Storage duplication question → "quality of the system versus storage; that is the trade-off", and agentic routing to query only the needed store.
- Promises to answer a hard question ("when do we stop increasing chunk size?") the next day in depth, after collecting doubts.
- Advises: write the code yourself to understand "what happens in this function, what are the steps", not syntax.

## Day 5 (lines 9894–11736)

### Lines 9894–10550
- Opening tells learners to **notice her words and how she explains**, so they can explain it in interviews and at work. (Meta-teaching.)
- Opens with quick recall: "where all do we rank?"
- RRF built from a problem in the numbers: plain reciprocal ranks drop too fast (1 → 0.5 → 0.1), so add a smoothing constant (60). Then shows that a chunk found by both retrievers gets boosted ("rank and agreement"). Ends with three plain advantages (simple, no training, no LLM call).
- Agentic RAG: guesses from the name first, then the reason (data spread across stores; let the model pick), then a broad rule: "any extra LLM call that makes a decision → agentic". Distinguishes it from hybrid with "not every agentic RAG is hybrid, and the reverse".
- When confusion remains, refuses to move on: redraws the nested structure (outer agent → retrieval tool that is itself an agent → two retrievers), slowly, step by step. Explains the design choice (single responsibility) but tells learners not to fixate on architecture yet.
- Query rewriting motivated by contrast pairs of weak vs strong questions ("explain search algorithm" vs "explain binary search with code"; "how does auth work" vs "how does JWT work") and by refusing to blame users: "we can't make the system depend on users writing good queries."
- HyDE explained from the paper's own figure, step by step; clarifies that the hypothetical text is only for searching and the answer still comes from real documents. Shows that papers prove claims with evaluation tables (recall@k, NDCG) — ties back to the metrics week.
- "These are possible solutions; whether they help *you* depends on your queries and your evals."

### Lines 10551–11650
- Admits when an example is a poor fit ("HyDE is not a good use case for code; I'm still showing how you'd do it").
- New idea from a problem the learner can picture: "too many chunks, slow search — what would you do?" → group similar chunks, then group the groups → a tree → names it RAPTOR only at the end.
- **Contrast pairs to separate look-alikes**: tree vs graph (grouping similar things vs relationships between entities, cycles allowed); RAPTOR vs vectorless/PageIndex (both trees; one searches summaries by embedding similarity, the other lets the LLM reason over a table of contents, no vectors).
- Everyday analogy for vectorless search: using a book's index — "searching about SQL, you open the databases chapter, not networking". Key line: "similarity doesn't mean relevance".
- Uses what is trending (GitHub stars) to raise interest, then grounds it with a small code example and the trace.
- Revision as rapid Q&A, including "is fusion necessary before reranking? what's the cost if you skip it?" and a learner's analogy (fusion = first interview round) accepted and reused.
- Agentic RAG definition widened by example: an extra LLM call for routing, query decomposition, planning — all agentic.
- **Context engineering opener**: lists what will be covered (what to send, structure, evaluating context, token budgeting, memory). Links token budgeting to HLD capacity estimates (QPS, storage) the audience knows.
- Elicits the parts of context from the class (system prompt, history/memory, tool outputs, retrieved context, user query) and asks "why manage history?" → "LLMs are stateless" (callback to Day 1).
- "Does order matter? start or end?" → shows the *Lost in the Middle* paper → explains the intuition twice: recency (next-token prediction weighs recent words) and primacy (training data puts instructions/titles first). Humour ("middle class") kept light.
- Builds context designs as a ladder: system + query → + history → + retrieved chunks → + tool outputs → all together.
- Introduces operations as named verbs with one example each: expansion (pull helper functions with a function), compression (summarise), selection (top 10 of 100 after fusion/rerank), pruning (dedupe, stale, irrelevant), ordering (put key items at start/end).
- Short- vs long-term memory with the ChatGPT example ("it remembers in a new chat that you're learning AI").
- Advice on using AI to learn new topics: give it the paper or repo link, cross-check, otherwise it invents answers ("hypothetical document instead of real document" — reuses HyDE as a joke).

### Lines 11651–11736 (Day 5 Q&A)
- Cost objection to PageIndex answered with a drill-down picture (projects → modules → submodules → class): "five or six calls still beat reading lakhs of lines". Use-case fit: legal documents with clause references.

## Day 6 (lines 11737–14060): Memory

### Lines 11737–12750
- Opens with a long rapid-fire revision of the previous two days in question form, including "why is the end of the context important?" — the learners must give the reason, not just the fact. Asks "is revision useful?" for feedback.
- **Demonstrates the problem first with the smallest possible code**: ask "who is Dhoni?" then "when was he born?" — it fails. "Let's do it in class so you know I'm not making it up."
- Tells learners the aim is "what must be happening inside the framework", not the framework's one-liner; if no framework existed, how would you build it?
- Corrects a naming misconception: short-term memory ≠ RAM; both short- and long-term memory should be persisted ("close ChatGPT and come back — it still remembers").
- **Builds memory in steps, each run live and traced**: stateless → Python list in RAM (lost on restart) → SQLite with thread IDs (switch threads, restart, delete the DB) → too big → solutions. Each step shows token counts growing in the trace, so cost is felt, not stated.
- Uses learner-suggested scenarios live ("talk about three people, restart, ask 'tell me more about her'" → it picks the latest: recency again).
- Recap as numbered list of what was built.
- Problem "context too long" → asks for solutions, then evaluates each: trim/sliding window (FIFO; shows how a name in message 1 gets lost), summarisation (one LLM call; can't keep everything in 200 tokens), both together (recent messages are most relevant), RAG over messages (learner's idea, credited by name; more context but more latency/cost), hierarchical summaries (callback to RAPTOR). Ends with a goal sentence: "store the history and send the most relevant part with the query, in the most optimised way."
- Middleware introduced as hooks before/after agent and model calls; asks learners to invent uses (call limits, validation, guardrails, trimming, caching) before listing the built-ins. Human-in-the-loop tied to the project ("would you let generated code edit your file without approval?").
- "Guardrails sound hard, but the code is simple; that's why this course is about logic, not syntax."

### Lines 12751–13850
- **De-mystifying names**: "Everything seems fancy, but a tool is a function, and a middleware is a function called before the model." Says this repeatedly so jargon stops being scary.
- Shows the framework's own diagram of the loop (before-model → model → tool → before-model again) and explains why the hook runs again after every tool call (tool output is also a message, so the window grows).
- Pattern: first write it by hand ("what must be happening inside"), then show the framework's one-line version (checkpointer, summarisation middleware) and connect the two.
- Admits live mistakes plainly ("sorry, I was showing the previous code; nobody told me").
- Summarisation demo: shows the actual summarisation prompt in the trace and points to where it lives in the code. Invites learners to change the numbers (summarise after 6, keep 4) and watch what changes.
- A learner's concern ("summaries get weaker over time") becomes the bridge to the next topic (long-term memory).
- Long-term memory motivated with everyday cross-chat examples: "I prefer SQL" told in one project should carry to the next; Apple Watch for fitness; resume and projects. Then names the kinds: preferences (semantic facts), episodes (events), procedures (how I like things done).
- Live test of conflicting facts (learner's idea): "I like C++ not Python" → updates → code language changes. Shows it is not guaranteed ("it depends on the LLM call") and names the fix (structured output with a schema).
- **Pairs to remember the framework concepts**: checkpointer (short-term, per thread_id) vs store (long-term, per user_id).
- Shows a live failure honestly ("it should have remembered bullet points across threads; I'll check why") rather than hiding it.
- Group project briefing and accountability (quizzes tracked, start projects this weekend; "you will face issues; remember them, we'll cover them").
- Q&A: helps a learner probe an edge case in her own summarisation demo live, accepts "you are correct, that part is tricky", then checks how the framework handles it (trigger by messages or tokens).

### Lines 13851–14060 (Day 6 Q&A)
- When a back-and-forth doesn't resolve, takes it offline and promises a clearer demo next class instead of confusing everyone.
- "What to keep in long-term memory" answered by analogy to people: "even humans don't remember everything from class; we're mimicking human behaviour" — honest about non-determinism.

## Day 7 (lines 14061–15925): Capstone project begins

### Lines 14061–14950
- Starts by naming students who did the homework (positive reinforcement) and asking who didn't.
- Frames the shift: "demo code puts retriever and indexer in one place; production needs modular, extensible code where adding a new retriever changes the least code."
- **Design by asking the class**: "How would you divide this? Where does logging belong? If we switch OpenAI to Anthropic, should we edit everywhere?" Learners arrive at layers: config, LLM, context (indexers, retrievers, memory), agents, tools, MCP/skills, safety, freshness, observability, evals, caching. Refuses buzzwords: "don't give me terms like LLD, HLD; tell me how you would approach it."
- Explains each setup choice by its job, not by name: poetry (dependency and packaging), pipx (install a CLI globally but isolated), .env vs config ("secrets are never pushed; config is pushed and lets you switch the model"), factory for creating LLM clients ("factories produce").
- Draws the line on detail openly: "chunk size could go in config too; I have to draw the line somewhere."
- Shows the payoff of packaging in another folder: type the command anywhere and it runs.
- Writes every step in the notes so learners can follow even if lost: "literally every line I'm running is written down."
- Live setup failure (missing `__init__.py`) handled by giving learners a short break and letting the TA take questions; returns and explains the cause in one line.
- Project brief from TA: build a sellable product, not a demo ("not demo-able — sellable").

### Lines 14951–15925
- Builds the pipeline **one module at a time, each answering "what's missing now?"**: indexer exists → "do we have retrieval yet? no" → retriever → "do we have an agent yet? no" → tool wrapping the retriever → factory → orchestrator (and why: future planning, multi-agent, agentic RAG) → main calls handle_query. Then traces one question through every layer.
- Invites disagreement on design: "this is not the only way; tell me what you'd do differently and why."
- Production tool choice explained by comparison (Chroma for local/hackathons vs Qdrant for scale; Qdrant also does sparse/lexical and hybrid with RRF — callback to RRF day).
- Makes an abstract number concrete: "why is every embedding 1,536 long? It's the model's dimension — just a list of 1,536 numbers, nothing fancy."
- **Shows the payoff of the design**: switch Chroma ↔ Qdrant by editing one line of config; "adding graph indexing changes only two places." Asks learners to say where a web retriever would go.
- Catches herself skipping a step ("I indexed but never added the retriever — everyone pause") and fixes it in front of the class.
- When learners seem lost, draws the whole module diagram slowly on the iPad, then explains why she didn't start with the diagram: "you'd have been overwhelmed; with steps I can show why each part is needed."
- Project Q&A: clarifies target user by role (someone who knows traffic needs but not infra), insists on drilling requirements down, values a sellable product.

## Day 8 (lines 15926–17480): Project, MCP

### Lines 15926–15950
- Frames the course like HLD learning: first learn the parts (databases, networking), then stitch them into an end-to-end design — which is what interviews expect.
