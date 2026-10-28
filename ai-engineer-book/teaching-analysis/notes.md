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

### Lines 15951–16950
- Promises interview questions on scaling now that the parts are known; explains why plain cosine similarity over millions of vectors is too slow with **back-of-envelope arithmetic** (10 million vectors × 1,536 numbers ≈ thousands of operations each → seconds) — "a common interview question".
- HNSW intuition via a **linked list with express lanes** (jump 1→20→40, step down a level when you overshoot; ~log n jumps, "like binary search"), then maps it to vectors (similar vectors clustered in layers). Shows the real diagram after the intuition. "The vector DB does this for you; you can tune a bit."
- Recaps the architecture as a quiz (context: indexing, retrieval, memory; agents: tools, factory, orchestrator; LLM layer; observability; later safety, cost, evals, freshness — and *why* freshness).
- Calls out latecomers directly (strictness as care).
- Hybrid with Qdrant: goes faster on familiar ideas ("it's just a different API"), then **proves the value with a before/after query** from the golden set: an exact event name is found in hybrid mode, not found in semantic mode.
- Short-term memory in the project: three small changes (checkpointer in factory, thread ID in orchestrator, session commands in main). Restarts, switches sessions, shows it persists. When a reply looks like memory loss, opens the trace to prove the history was sent — "that's LLM unpredictability, not memory loss; that's why tracing is great."
- **Tools moment**: "Can it create a file? It tells you how — but we're lazy." Adds terminal and file tools, then generates a to-do app in an empty folder for a "wow".
- **Lets the system misbehave to teach safety**: asks it to delete everything; it deletes via the file tool; removes that tool; it deletes via `rm -f` because only `rm -rf` was blocked. "You're getting the importance of guardrails." Real failure > warning.
- Redraws the tool-calling loop once more on the iPad (query + tool list → which tool → app runs it → result back to LLM → answer), asking each step.
- **MCP motivated by repetition and by companies**: "why should everyone rewrite file and GitHub tools?" + "companies exposed APIs; now they'll expose tools" + "APIs needed a standard (headers, status codes) — tools need one too" → MCP.
- Respects mixed audience: some revision for returning learners, but "we have to respect the newcomers"; asks newcomers to type "new".

### Lines 16951–17480 (MCP)
- **Unpacks a name word by word to make it obvious**: HTTP's P = protocol = rules → MCP = Model Context Protocol: protocol (rules), context (tools give the model more context), model. Same move as RAG on Day 1.
- Common analogy used and attributed as common ("people say it's like a USB-C port").
- Architecture built from what's known: an agent's tools → companies expose *tool sets* (GitHub: list, create PR, push…) → each tool set is a server → our app is the host → one client per server. Shows the official diagram after.
- Practical warning from her own mistake: don't name your file `mcp.py` (clashes with the package).
- "Demo first, then integrate into the project" becomes the stated rhythm for every new topic, and the same rhythm is asked of learners' own projects.
- Shows the GitHub server's tool list (names, descriptions, arguments) to make clear that this metadata is what the LLM reads.
- **Transport explained by the question "where does the code run?"** — on your machine as a separate process (stdio; needs Node for npx) or elsewhere over HTTP. "Code has to run somewhere."
- Proof by contrast: without the file-system server it says it can't create local files; add a few config lines → it creates the file.
- Ends with a cliffhanger (browser automation on your LinkedIn).
- Apologises warmly after a learner felt hurt by being corrected; explains corrections are not personal.

## Day 9 (lines 17481–19496): MCP, Skills, long-running tasks

### Lines 17481–17950
- Opens by setting expectations for the week ("the hardest, most thought-heavy topics; after this it's stitching small things") and asking what's left in Claude Code (planning, browser automation, skills).
- Revision chain in one breath: tools are functions → companies exposed APIs, now tools → need a standard → protocol → MCP like HTTP; host, clients, servers, one-to-one; stdio vs streamable HTTP; adding a server = one config entry.
- Integration in the project with only the tricky part explained (environment variables inside the JSON must be substituted). Factory doesn't change when servers are added. Credits a learner who added tool filtering and a Gmail server.
- Custom MCP server shown as "the same functions we already wrote, plus FastMCP" — reuse of known code makes the new idea small.
- Rule of thumb for transport: stdio when the tools can run where the host runs; HTTP with a URL otherwise.

### Lines 17951–18950 (Skills, long-running tasks intro)
- Browser automation demo with an explicit warning learned from experience: set call limits or it loops and burns tokens; bigger/newer models behave noticeably better for such tasks.
- Warns that without practice topics "become khichdi in your head"; credits a learner who learned most from bugs. "My job is concepts, code, quizzes; the last step — writing it yourself — is yours."
- **Skills built from first principles**: "In the end, everything we send to an LLM is text." Everyday repeated tasks (make a PPT with these slides/theme; a PDF with header/footer; quizzes with four options) → "instructions + references + examples, sometimes scripts, packaged" → that's a skill. "Fancy term, simple idea."
- Shows real skill files and their popularity (stars) to signal industry weight.
- **Learner question drives the key concept**: "this is too long to be a prompt" → "can I send ten of these? No" → "notice every file starts with name and description — what must be happening?" → learners infer *progressive disclosure* before she names it. Then the three levels with rough token sizes (~100 metadata, ~5k instructions, resources on demand).
- Format stated as a simple standard: folder per skill, SKILL.md required, front matter with name/description, everything else optional.
- "If you only want to use skills, it's one line (deep agents). We'll build what happens inside so you really understand it." Explicit distinction between using and understanding.
- Answers "LLMs already know PDFs" with: LLMs are generic — they can explain in two lines or a hundred, for a beginner or a scientist; instructions pin down what *you* want.
- Live code breaks due to version mix-ups; she stops, apologises, switches to theory and promises to show the working code tomorrow rather than burn class time.
- Long-running tasks introduced through the familiar plan mode in coding tools, then **learners list the problems** (permissions, deviation, memory, losing context); she adds crash-in-the-middle and parallel steps, then names the requirements: resumability, crash safety, human approval, dependency ordering, parallelism, visibility, timeouts, retries. Flags it as a common interview question.
- Gives the high-level architecture before tomorrow's code so the code is easier to follow.

### Lines 18951–19496 (end of Day 9)
- Long-running design explained as a flow first (plan vs ask → task orchestrator → LLM returns a plan in a fixed structure → tasks with type and status stored in a DB), then a live demo of a 15-task plan with human approval as a "cliffhanger" to make people come on time.
- Q&A shows clear reasoning on trade-offs: skills vs custom multi-agent workflows ("skills for repeated workflows; build your own when you need structured output, verification, guardrails, control"); skill security ("third-party instructions can contain anything — prompt injection; use verified, well-starred ones or write your own").
- On non-deterministic behaviour: "agentic applications are never fully deterministic; that's why guardrails, structured output, retries and planning exist."
- Admits when a question is out of scope and points to the right place (OAuth is general system design).

## Day 10 (lines 19497–21480): Safety, long-running tasks

### Lines 19497–19950
- **Pep talk with substance**: frameworks and APIs change (shows her own year-old video is out of date); "concepts don't change", so the course spends time on what happens inside rather than syntax. Tells learners where *not* to spend energy (Python syntax, model choice) at this stage.
- Revision as a contrast: MCP vs skills — "should we even compare them? No: one is a protocol for tools, the other is packaged instructions for repeated tasks."
- Owns yesterday's bug and explains it in two lines before moving on.
- Before/after demo for skills: to-do app without the skill, then with a front-end design skill; shows in the trace that only names/descriptions were sent first, then the full skill. Notes that a stronger model alone improved the first version — honest about confounders. Homework: try the PDF skill.
- Swaps hand-written file tools for the file-system MCP server with one subtle point explained: give access only to the current project folder (substitute the current working directory like the env vars).
- **Teaches interview vocabulary deliberately**: "say 'critical tasks', 'destructive tasks' — using the right terms in 45 minutes is impressive."
- Human-in-the-loop by design-it-yourself: "Don't read the docs yet. How would you implement it?" Draws the current loop and asks where the interruption goes (after the model chooses a tool, before it runs), then three parts: interrupt, read the human's response, decide what next. "Logically it's simple; let's see how frameworks do it."

### Lines 19951–20950 (HITL, guardrails, planner)
- HITL taught as a small decision table: per tool, which responses are allowed (approve / edit / reject / respond). Then a conditional version ("only interrupt for write SQL or a dangerous shell command") so learners see that blanket approval is bad design.
- Explains *why* a checkpointer is needed with one plain sentence: resuming is a second call carrying the human's decision, so state must be saved between the two calls.
- Demo in two runs: approve first, then reject with a reason, and shows in the trace how the reason reaches the model. Same input, one knob changed.
- Guardrails start with the question "how would you protect PII?" and collect answers before naming redact / mask / hash / block. Each strategy is shown on the same example string so the difference is visible.
- Draws a parallel back to evals: deterministic guardrails (regex, rules) vs model-based guardrails mirror formula metrics vs LLM-as-judge. Reusing an earlier mental model instead of teaching a new one.
- ReAct named only after learners have already seen repeated tool calls: "remember why we needed call limits? This is why: reason, act, observe, repeat." Naming arrives after the experience.
- Long-running planner shown as files with one job each (orchestrator, planner, task store, recovery, judge) before any code is opened. The plan prompt is read line by line and each requirement is justified (why 5–20 tasks, why dependencies must form a DAG, why acceptance criteria).
- Uses plain terms for graph ideas: "no task can depend on itself, even through others", then gives the formal word (cycle, topological order).

### Lines 20951–21480 (end of Day 10)
- Live run narrated against the database: "Do you see task.db? Any rows? No. Approve. Now open it again: ten rows, the first in progress." The learner watches state change, not just output.
- Each column of the task table is read out and tied to a design need (type, status, depends-on, retries, timestamps). Tables are explained column by column.
- Small, plain mechanism stated once: "as I finish a task I summarise its result and pass it to the next task." No jargon for handoff.
- Live failure again (file access denied); she debugs aloud, finds her own mistake while answering a learner (duplicate file tools beside the MCP server confused the agent) and says so openly.
- Honest scoping in Q&A: "we are building this in five weeks; it is not a replacement for the real product." Learner asked "why can explaining the code first help?" → answer reuses the course idea "small tasks perform better; that is why we plan."
- Deflects off-topic questions to the right tool ("look at how Grafana works, then ask again").

## Day 11 (lines 21481–23634): Design review of a coding agent

### Lines 21481–22000
- Opens with the interview frame: "if asked to design this on a whiteboard, how would you approach it?" The whole day is synthesis.
- Starts with requirements, and makes learners list them (functional first: debug, answer, add features, create from scratch; then basic tools: web search, file CRUD, terminal, GitHub, database).
- "Agentic system design is normal HLD plus agentic-specific things" — ties new topic to known system design (gateway, rate limiter), then adds the agentic parts (injection detector, PII scanner, content filter).
- Accepts a learner correction publicly ("rate limiting applies to the cloud version, not local; you are right"). Models that mistakes in discussion are fine.
- "Should the user have to say ask or plan? How would you do it yourself?" → classifier → "can plain code understand the query? No. Who understands queries? The LLM." Leads to a query-classifier agent by elimination.
- Distinguishes close terms precisely: indexing at start-up vs incremental indexing as changes happen.
- Builds the architecture as layers, asking for each piece: context (indexers, retrievers, memory), agent (orchestrator, factory, ReAct agent with tools: custom, MCP via a multi-server client, retriever tool; skills), safety, quality assurance, observability, freshness. Acronym check: "ReAct stands for?"
- Then walks one concrete flow through the layers (a debug query: retrieve → model finds the bug → file tool writes → result back → response).
- Rapid recall drills: "three types of long-term memory?" (episodic, procedural, semantic).
- Plants future topics as cliffhangers (Langfuse for local tracing, caching, freshness, token budgeting) and says where each belongs in the layer map.

### Lines 22001–23100 (planner flow, executor, re-indexing)
- Planner flow redrawn as numbered steps, each one asked for before it is drawn: plan (structured output) → human approval → persist (task store) → executor loop. Recall questions inside the flow ("what did we use to get a fixed format?").
- Corrects a learner's word choice gently: "if a task hasn't started, do you call it in progress? Pending / to do." Precision of state names matters.
- Lists every status (pending, in progress, completed, failed, blocked, skipped) with a one-line reason for each.
- Topological sort taught without DSA: "it's okay if you never did DSA. It just means every task you depend on comes before you." Then the formal name (directed acyclic graph). Says how it is enforced in practice: "through the prompt; the LLM writes depends-on."
- Handles a hard learner question (two parallel tasks writing the same row) by naming it as plain HLD, not agentic: atomic updates. Marks which ideas are general engineering and which are agent-specific.
- Shows the simple path and the internal path: "a checkpointer would be the easy way; we do it by hand to understand internals" (store a result summary per task, pass dependents' results into the next task's prompt).
- Multi-agent introduced before its chapter: "different task types want different models and tools (reasoning model for design, small model for tests, read-only tools for review). Notice you are already using multi-agent." Redefines agent as "LLM plus tools" to settle "different agent or different LLM?"
- Names over-engineering when a learner proposes choosing a model per task: "per type yes, per task is over-engineering."
- Code walk-through rule stated: "if syntax is hard, that's not the point; can you say why this is in this layer and why this step comes after that one?" Then drops to a flow chart when the class is lost: "everyone's code is hard to follow until you debug it yourself."
- Edge case taught with numbers: task 7 depends on 2, 3, 4; 4 is still running; so nothing is ready → sleep and re-check. Learner links it to a task scheduler; she agrees and says it is really LLD.
- Shows why acceptance criteria exist: used once in planning and again by the LLM judge after each task. One field, two uses.
- Re-indexing taught from a failure story: rename OrderManager to OrderHandler, ask about OrderHandler, agent says it doesn't exist. Then four triggers (start-up, explicit command, file watcher, after a large planned feature).
- Debouncing with a timeline: change at second 0, wait 5 s; another change at second 3 resets the timer; index at second 8. Repeated a second time for a confused learner using the typing example.
- Flags interview answers explicitly: "if asked what happens when files change: re-indexing, then debouncing, then incremental."

### Lines 23101–23633 (prompt caching, end of Day 11)
- Prompt caching taught through **worked arithmetic on a real price sheet**: input $3/M, cache write $3.75/M, cache hit $0.30/M. Static part 100k (system 40k + tools 20k + retrieved 40k), dynamic 1k, 10 requests. Without cache $3.03; with cache first call $0.378 then $0.033 each. Learners compute each line aloud.
- First notices the odd fact ("writing to cache costs *more* than normal input — did you notice?"), then explains why it still pays.
- Demo as a sequence of predictions: "first call: hit or miss?" → run → "run again: now?" → "change one word in the system prompt: now?" → "change the cache key: now?" → "shrink the prompt below 1,024 tokens: now?" Each run tests one variable.
- Separates provider behaviour honestly: one provider caches implicitly, another needs explicit cache-control markers; "this part is not in our hands; what we can cache ourselves is next week."
- Ties to known internals in one line (KV cache, time to live) for those who know it, without making it required.
- Q&A gives practical edges: "the sad case is 1,023 tokens"; parallel requests don't share a cache that isn't written yet → send one warm-up call first.
- Query-classifier trade-off: "sounds good, but every extra step is another model call; the first response must be fast — that's why products give explicit plan/ask modes."
- Owns a failing demo plainly (token limit too low for a bigger model) and tells learners which setting to try instead.

## Day 12 (lines 23635–24420): Applying the design to new projects

### Lines 23635–24200
- Responds to feedback ("we can follow the design but can't apply it to a new project") by reusing one checklist across new domains (finance advisor, infra SaaS, then nutrition, legal, recruiting, CRM).
- The checklist, asked in the same order each time: user actions → where RAG fits (what documents, how often they change) → which search (hybrid, because stock symbols / instance names need exact match) → fusion → skills → MCP servers → query classifier → simple vs planning path → memory (STM, LTM types with domain examples) → freshness triggers → context building → observability → evals → guardrails/HITL → model per job.
- Vague requirements are deliberate: "interviewers do this; you are expected to ask cross-questions."
- "Who are we replacing?" frame: coding agent → developer; infra agent → SRE/DevOps engineer. Then list what that person does.
- Domain twist on a known concept: freshness in finance has different triggers (user transactions, market changes, watchers on held stocks, scheduled weekly rebalancing). Shows the same idea with a new trigger list.
- Calls out what is *most* important per domain: "for money, safety and human approval matter most; otherwise the agent goes rogue with money."
- Gives a low-effort way to practise the hard project (dummy service with a health API and a random-sleep load API on free instances).
- Pros and cons insisted on: "just because we can cache doesn't mean we should." Full vs incremental re-indexing argued both ways (few files or schema change → full; large corpus, frequent small changes → incremental).
- Production pattern named after the problem is felt: half-applied changes → shadow collection and atomic swap (blue-green).
- Change detection as two named options with expansions: mtime (modified time) vs content hash.

### Lines 24201–24420 (end of Day 12)
- Recap as rapid-fire questions before new material: triggers? two change checks? the key concept (debouncing)?
- Debounce code read beside the timeline again (change at 2 s → index at 7 s; change at 4 s cancels and resets → 9 s). Same example, now mapped line by line to the code.
- "When would my code be a nightmare?" — invites learners to break her own design (huge files, many files, five people editing at once) and links the last to Git merge conflicts they already know.
- Uses the gaps as the bridge to the next topic (scaling, sharding, multi-tenancy, metadata filtering).

## Day 13 (lines 24421–26238): Semantic caching, Langfuse, scaling RAG

### Lines 24421–25300
- Starts by showing an interview-question bank with key points per answer; promises to discuss only the hard ones in class.
- Caching opened with why (cost, latency), then where (every layer?), then "should I cache everywhere? What are the cons?" Learners list stale data, memory, invalidation complexity, over-engineering.
- Recaps prompt caching with the placement rule that follows from it: static content first. "If asked whether placement matters: yes."
- Draws the plain RAG pipeline (query → retrieve → generate) and asks "where can I cache?" Two answers: retrieved chunks or the generated answer.
- Why caching is different for agents: "users never type the same thing twice — 'what are neural networks' vs 'explain neural networks'." Semantic caching follows from that.
- Caching framed as three questions to discuss in any design: when to write and what to store; how to match (hit/miss by similarity threshold); when to invalidate (TTL, flush).
- Contrast that makes the difference clear: prompt caching still generates a new (different) answer each time; semantic caching returns the stored answer, so the response is identical.
- Code shown as three verbs: get, put, invalidate. Similarity = 1 − cosine distance stated in one line.
- Demo as threshold experiments: 0.82 (hit), 0.16 (miss, but not zero — "neural networks are usually coded in Python"), 0.7979 against 0.8 ("just missed; at 0.75 it would hit"). TTL experiment: 2 s then 10 s, asking "hit or miss?" before each run.
- Draws the general rule from the runs: threshold too low → wrong answers; too high → no hits. Similarity depends on the embedding model, so tune on your own queries. TTL low for fast-changing data, high for stable data.
- Design choice justified: cache ask queries, not plan queries (plans are new work each time).
- Self-referential demo: the coding agent explains its own planner correctly and writes its own README. Strong motivator.
- Leaves deliberate homework gaps (retrieval caching, re-indexing in the other vector store, adding HITL and guardrails to the capstone): "same code, different trigger."
- Subtle point taught with a step-by-step trace: with short-term memory, a repeated question never reaches the retrieval tool, so a retrieval cache there would never be hit. "Caching everywhere is not always useful."

### Lines 25301–26238 (caching edges, scaling, multi-tenancy, local tracing, end of Day 13)
- Compresses the previous trace into one memorable line: "short-term memory is implicit caching." Then draws the boundary: context-dependent queries ("when was *he* born?") must not be cached.
- Widens the idea so learners see caching everywhere: embeddings can be cached; the planner's task table is "also caching — stored state we don't redo."
- Failure-mode question: "a web search returns a wrong answer and you cache it. Implication?" Every similar query now gets the wrong answer fast. Then the production lesson: low latency can hide wrong answers, so never judge a system on one metric; watch relevance/faithfulness and user feedback too.
- Scaling split into two kinds before any solution: more data (millions of chunks) vs more queries per second.
- States scope: "HLD-common ideas we skim; agent-specific ones we go deep on."
- Sharding keys collected from learners (time, region, semantic topic, hot/cold), then "it depends on the queries": logs by time range → shard by time; region-heavy queries → by geography.
- Problem with numbers: shards take 5, 3, 4, 8 s → even in parallel you wait 8 s. Named afterwards: scatter-gather. Fixes reasoned from the cause (better shard key, cache the slow shard, replicate hot shards: 4 replicas for a hot one, 1–2 for a cold one).
- **Profiling over reflex**: "system slow — will you directly say caching? At which layer?" Time each stage (embed, retrieve, rerank, generate) first. Same for bad RAG answers: is it retrieval or generation? "Always give a structured response; don't jump to a common solution."
- Defines jargon plainly before using it: "tenants are just a fancy word for customers"; "a collection is like a table."
- Multi-tenancy as a spectrum with when-to-use for each: collection per tenant (few tenants, zero leakage), shared collection + metadata filter (scale, but filter bugs leak), namespaces, dedicated cluster (a handful of large enterprise customers).
- Metadata filtering explained by shrinking numbers: 1 million documents → filter by team → 10,000, so search is faster as well as safer. Demo: unfiltered query about rollbacks returns payments and mobile docs; filtered returns only the two SRE docs even though four were asked for.
- Answers the earlier "data still goes to the tracing SaaS" worry by showing a self-hosted tracer. Calls it "the same thing" as the hosted one: env keys, a callback handler, pass it on invoke.
- Interview coaching from her own story: mock interviews, timed 45-minute explain-aloud drills, recording yourself ("you'll go: what am I talking"). Normalises fear ("everyone starts with shaking legs").
- Learner's real interview report used as evidence: production architecture, POC-to-production evaluation, and safety/PII are the three common question areas.

## Day 14 (lines 26239–28408): Interview questions, LLMOps

### Lines 26239–26300
- Opens from day-one definition (agent = LLM + tools in a loop), then compounding errors with arithmetic: 0.95 × 0.95 ≈ 90%, three tools ≈ 85%. "Errors amplify across steps."
- Moves straight to "are all errors the same?" — learners list 403, 404, 429, 500 — to set up per-error handling.
