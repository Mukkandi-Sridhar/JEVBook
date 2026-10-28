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
