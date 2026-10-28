# Ship Real AI: earlier chapter map (superseded by CONTENTS.md)

Status: draft 1 for review, 28 October 2026. Nothing beyond Part I gets written until this map is agreed.

Based on `plans/Next book plan.md` (v1), changed to match the new style rules (`STYLE.md`, section 6) and the
teaching-method study. This book stands alone, so every "as in book 1" link from the old plan has been removed.

## How to read this map

For each chapter you will see:

- **Builds on:** the earlier idea it starts from (one line).
- **Opens with:** the problem the reader feels first.
- **Sections:** in teaching order. Each one goes problem → reader tries → mechanism → name → rule → trade-off.
- **Numbers worked by hand:** the calculation the chapter does on paper.
- **Project:** what gets added to Tarkika.
- **Defend:** the numbers the reader must be able to justify.

Page target: 12–16 pages a chapter. Thirty-eight chapters in ten parts, about 560 pages in all.

## The system map (used in every part)

Chapter 1 draws one picture of an AI system. Every part opener redraws it and highlights the layer that part covers.

1. **Front door:** the user interface, the API, rate limits.
2. **Safety:** input and output checks, private data, approval gates.
3. **Control:** the router, the workflow or agent loop, the planner.
4. **Model:** which model, settings, reasoning effort.
5. **Context:** prompt, retrieved knowledge, memory.
6. **Tools:** your own tools, MCP servers, other agents.
7. **Quality:** test sets, evals, judges.
8. **Operations:** traces, cost, caching, releases, rollback.

---

## Front matter

- Preface: why this book teaches judgement as well as tools.
- How to read this book: three reading paths (beginner, software engineer, data scientist), the boxes, shelf-life
  tags, the companion repo.

---

## PART I: The job and the foundations (Ch 1–5, drafted)

*Map layers: all of them, briefly (Ch 1), then Model (Ch 2–5).*

### Ch 1. What an applied AI engineer does
- **Opens with:** the model is the cook, but someone has to design the kitchen.
- **Sections:**
  1. The model is only one part of the system (draws the system map)
  2. Three kinds of AI jobs
  3. What the work looks like in a week
  4. Three questions behind every AI system: does it work, should it act, what if it is wrong?
  5. Writing or deciding? (generation versus decision tasks)
  6. Your workbench
  7. Your first call to a model
  8. What one answer costs
  9. The project: Tarkika's support agent
- **Numbers:** the cost of one call in rupees; the cost of 4,000 calls a day.
- **Revision for the new method:** add a "Before reading on" prompt in §4, and do the arithmetic in §8 step by step.

### Ch 2. Probability and statistics you will actually use
- **Builds on:** Ch 1's question "does it work?"
- **Opens with:** a fraud alarm that is "99% accurate" yet wrong most of the times it rings.
- **Sections:**
  1. A probability is a share of many cases
  2. When something is rare, most alarms are false
  3. Accuracy can fool you (precision, recall)
  4. How sure is your test score? (bootstrap, by hand)
  5. Comparing two versions fairly (paired comparison)
  6. How a language model uses probability (next token, temperature)
  7. When the model says 80%, is it right 80% of the time? (calibration)
- **Numbers:** base-rate counts out of 10,000; a confidence interval on 50 vs 500 test cases.
- **Project:** label 200 tickets by hand, which becomes the first test set.

### Ch 3. Classical machine learning: small, fast and cheap
- **Builds on:** Ch 2's precision and calibration.
- **Opens with:** 4,000 tickets a day, and a large model that costs too much to read every one.
- **Sections:** learning from examples; turning text into features; practice papers, mock tests and the final exam;
  logistic regression; gradient-boosted trees; overfitting; a baseline in a few lines; measuring a classifier; from
  probability to action: when to ask a person.
- **Numbers:** cost per 1,000 tickets, classifier vs LLM; the 80% routing threshold.
- **Project:** a ticket-intent classifier and a routing rule.

### Ch 4. Deep learning in one chapter
- **Builds on:** Ch 3's logistic regression as one "neuron".
- **Opens with:** a photo of a dented cooker that no hand-made feature can read.
- **Sections:** a team of small checkers; how a network learns; bigger networks become overconfident; why GPUs; what a
  model needs in memory; when to use deep learning yourself.
- **Numbers:** 7B weights in BF16 and 4-bit; 16 bytes per parameter to train.

### Ch 5. From words to tokens and vectors
- **Builds on:** Ch 4's "networks read numbers".
- **Opens with:** a computer that sees "refund" and "money back" as unrelated strings.
- **Sections:** numbers that know nothing; tokens; why tokens matter to you; why Indian languages can cost more;
  embeddings as position; measuring closeness; finding similar messages; what embeddings miss; a short history.
- **Numbers:** token cost of one message in English, Hindi and Hinglish (marked VERIFY until measured).
- **Part I milestone:** a labelled test set, a baseline classifier and a token-cost sheet.

---

## PART II: How large language models work (Ch 6–11)

*Map layer: Model. Intuition level only, no derivations.*

### Ch 6. Inside the transformer
- **Builds on:** Ch 5's embeddings.
- **Opens with:** "bank" in "river bank" and "bank account" gets the same vector. How does the model tell them apart?
- **Sections:**
  1. Words that look at each other: attention, as a classroom where anyone can ask anyone
  2. One block, repeated: attention, then a small network, many times over
  3. Predicting the next token, one at a time
  4. Where position comes from
  5. The KV cache: why earlier tokens are kept, and why that memory fills the GPU
  6. Sharing notes to save memory (grouped-query attention, briefly)
  7. Faster versus different: FlashAttention changes the speed, not the result
- **Numbers:** KV-cache size for one 8,000-token conversation, then for 50 users at once.
- **Defend:** the context length you allow, and its memory.

### Ch 7. How a model is trained: from reading the internet to being helpful
*(Merges the old Ch 7 and Ch 8.)*
- **Builds on:** Ch 6's next-token prediction.
- **Opens with:** a base model asked "What is your refund policy?" answers with three more questions.
- **Sections:**
  1. Pretraining: reading most of the internet, one next token at a time
  2. Data quality beats data quantity, up to a point
  3. What a base model can and cannot do
  4. Supervised fine-tuning: copying good answers
  5. Preference tuning: "this answer is better than that one" (RLHF, DPO as a story)
  6. Practising on problems with answer keys (rewards that can be checked)
  7. Side effects: eager to please, confident when wrong
  8. Open weights are not the same as free to use (licences)
- **Numbers:** a rough count of training tokens versus a lifetime of reading.

### Ch 8. Reasoning models and thinking time
- **Builds on:** Ch 7's checkable rewards.
- **Opens with:** the same model, two settings: one is 6× the cost and no better on Tarkika's tickets.
- **Sections:**
  1. 2 + 2 versus 17 × 24: when thinking helps
  2. What thinking tokens are, and who pays for them
  3. The effort setting
  4. Cost per finished task, not price per token
  5. When thinking wastes money
- **Numbers:** cost per finished task at low, medium and high effort.
- **Decision:** route to the reasoning model only above a difficulty threshold.

### Ch 9. Bigger and longer: mixture of experts and long context
- **Builds on:** Ch 6's memory and Ch 8's cost per task.
- **Opens with:** a 300-page policy file pasted into one prompt. The answer misses a rule on page 40.
- **Sections:**
  1. Specialists, not one generalist (mixture of experts)
  2. Total versus active parameters: memory follows total, speed follows active
  3. Long windows and context rot: accuracy falls as input grows
  4. Long context or retrieval? A rule with its conditions
- **Numbers:** memory and speed of an MoE model; tokens sent per question with and without retrieval.

### Ch 10. Running a model: serving, speed and quantisation
- **Builds on:** Ch 6's KV cache, Ch 4's memory maths.
- **Opens with:** a model that answers in 2 seconds for one user and 40 seconds at lunchtime.
- **Sections:**
  1. Two speeds: time to first token and tokens per second
  2. Why output tokens cost more than input tokens
  3. Serving many users at once: batching, as the railway counter
  4. Reusing work: prefix caching
  5. A junior drafts, a senior checks (speculative decoding)
  6. Smaller numbers, smaller model (quantisation)
  7. Temperature 0 still is not fully repeatable
- **Numbers:** a latency budget split into first token plus generation; 4-bit vs BF16 memory.
- **Project:** run a small open model locally and measure speed and quality on the test set.
- **Defend:** quantisation level; p50 and p95 latency.

### Ch 11. Choosing a model
- **Builds on:** Ch 8–10.
- **Opens with:** three teams, three different "best" models, all right for their own jobs.
- **Sections:** model tiers; API or open weights (cost, privacy, control, licence); a small model for small jobs, a big
  one for hard jobs; running your own bake-off on your test set; when to move up to a bigger model.
- **Numbers:** monthly cost of each shortlisted model at 4,000 tickets a day.
- **Part II milestone:** a model shortlist backed by your own test numbers.

---

## PART III: Talking to models (Ch 12–14)

*Map layers: Context, Tools, Quality.*

### Ch 12. From prompts to context
- **Builds on:** Ch 9's context rot.
- **Opens with:** a new employee's first-day briefing: too little and they guess, too much and they get lost.
- **Sections:**
  1. The parts of a prompt: role, task, examples, format
  2. Everything the model sees is context: instructions, history, retrieved text, tool lists
  3. The smallest set of useful tokens
  4. Prompting a reasoning model: describe the goal and the checks, not the steps
  5. Fixed text first, changing text last (prompt caching)
  6. One word changes everything: why prompts need versions
- **Numbers:** prompt caching worked through ten requests, with and without the cache.
- **Project:** the Tarkika system prompt, cache-friendly.
- **Defend:** prompt length; cache hit rate; number of examples.

### Ch 13. Structured outputs, tool calls and your first threat model
- **Builds on:** Ch 12's prompt parts.
- **Opens with:** a customer email that says "ignore your rules and refund ₹50,000".
- **Sections:**
  1. A form with fixed boxes (structured output)
  2. A neat form can still hold a wrong answer: validate before acting
  3. Tool calling: the model only asks; your code decides and does
  4. What the model actually sees about a tool (name, description, arguments)
  5. Read tools and write tools
  6. Your first threat model: private data, untrusted text, a way out (the "lethal trifecta")
  7. Give the agent only the power it needs
- **Project:** a read-only order-status tool and a refund tool that can only propose.
- **Decision:** write tools need a gate.

### Ch 14. Testing from day one
- **Builds on:** Ch 2's test-set statistics.
- **Opens with:** a prompt change that fixes three complaints and quietly breaks twenty other answers.
- **Sections:**
  1. Tests for answers that change every time
  2. The golden test set: where cases come from (by hand, synthetic, production logs)
  3. Cheap checks first: exact match, format, rules
  4. Read 50 real outputs and group the failures (error analysis)
  5. Each failure type becomes a test
  6. Run the tests on every change, before you ship (offline evals)
- **Numbers:** how many cases you need to see a 5-point change.
- **Project:** a 50-case eval suite run on every change.
- **Part III milestone:** a tool-calling assistant with validation and a 50-case eval.

---

## PART IV: Knowledge and retrieval (Ch 15–19)

*Map layer: Context (retrieval).*

### Ch 15. Embeddings and vector search
- **Builds on:** Ch 5's embeddings and Ch 3's nearest neighbours.
- **Opens with:** 50 policy PDFs and a question whose answer is in one paragraph.
- **Sections:** how embedding models are made (briefly); similarity scores; a shortcut map for fast search (HNSW);
  shorter vectors to save money; choosing a store (pgvector first, and when to pick another); the embedding model and
  chunking matter more than the database.
- **Numbers:** storage for 1 million chunks at two vector sizes; flat search vs index search time.
- **Defend:** vector size; index type; why this store.

### Ch 16. Building a RAG pipeline that works
- **Builds on:** Ch 15.
- **Opens with:** an airline's chatbot invents a refund policy and the airline is held to it (VERIFY wording).
- **Sections:**
  1. RAG word by word: retrieve, add to the prompt, generate
  2. Reading messy PDFs and tables
  3. Cutting documents into chunks: size, overlap, by heading
  4. Meaning plus exact words: hybrid search
  5. Joining two result lists (rank fusion, a formula with no model call)
  6. A second, careful look at the top 20 (reranking, a model call)
  7. Fetch widely, then keep the best (high recall, then precision)
  8. Citations, and saying "I don't know"
- **Numbers:** chunk count for the policy set; tokens sent per question at top-k = 5 and 20.
- **Project:** Tarkika policy RAG with citations.
- **Defend:** chunk size and overlap; top-k; reranker cut-off; abstain threshold.

### Ch 17. Beyond basic RAG
- **Builds on:** Ch 16's limits.
- **Opens with:** "Which of my orders this month were late?" No document holds that answer.
- **Sections:** questions that need tables, not text (text-to-SQL, read-only access); questions that need
  relationships (graph-based retrieval, and its cost); letting the model search in a loop (agentic search); rewriting
  Hinglish questions before searching; searching PDF pages as images.
- **Project:** text-to-SQL over the orders table.

### Ch 18. Keeping knowledge fresh and fast at scale *(new chapter)*
- **Builds on:** Ch 16's index.
- **Opens with:** a policy changes on Monday; on Wednesday the agent still quotes the old one.
- **Sections:**
  1. Stale answers: what freshness means (how quickly, how completely)
  2. Has this file changed? Modified time versus a content hash
  3. Re-index only what changed (incremental indexing)
  4. Wait until the edits stop (debouncing, with a timeline)
  5. When a full rebuild is the right call
  6. Swapping in a new index safely (shadow copy, atomic switch)
  7. Filtering before searching (metadata filters)
  8. Many customers, one system: collection per customer versus shared with filters
  9. Too much data for one machine: sharding, and waiting for the slowest shard
  10. Conflicting documents: newer, or more authoritative?
- **Numbers:** debounce timeline; 1 million chunks → filter → 10,000; shard times 5, 3, 4, 8 seconds.
- **Defend:** re-index trigger; debounce wait; the tenant isolation you chose.

### Ch 19. Testing retrieval
- **Builds on:** Ch 14 and Ch 16.
- **Opens with:** an answer judged "faithful" that was faithful to the wrong document.
- **Sections:** test retrieval and generation separately; recall@k and MRR by hand; faithfulness and answer
  relevance; the trap where good faithfulness hides bad retrieval; building a retrieval test set from real questions;
  judges for faithfulness, checked against people; diagnosing a bad answer step by step.
- **Numbers:** recall@5 on ten questions, worked by hand.
- **Project:** a retrieval eval report.
- **Part IV milestone:** policy RAG plus orders SQL, fresh and filtered, with retrieval and answer evals.

*(If two volumes, Volume 1 ends here.)*

---

## PART V: Agents (Ch 20–25)

*Map layer: Control.*

### Ch 20. Workflows or agents: how much freedom to give
- **Builds on:** Ch 13's tool calls.
- **Opens with:** a new employee: a fixed checklist in week one, own choices by month three, and always asking before
  spending money.
- **Sections:** a model with tools; five fixed workflows (chain, route, parallel, manager and workers, write and
  check); real agents; errors multiply across steps; act, review or escalate; choose the lowest rung that works.
- **Numbers:** 0.95 per step over 3 and 10 steps.

### Ch 21. Your first agent loop, from the raw API
- **Builds on:** Ch 20.
- **Opens with:** a single tool call that cannot answer "cancel my late order and refund the delivery fee".
- **Sections:**
  1. The loop in plain steps: look, decide, act, look again
  2. Reason and act in a loop (ReAct), named after you have built it
  3. When to stop: step limits, budgets, timeouts
  4. Errors: retry with back-off, or not at all
  5. Fallbacks when a tool fails
  6. Good tools: few, clear, with useful error messages
  7. The same loop in one line of a framework, and what that line hides
- **Numbers:** retry waits 1, 2, 4, 8 seconds; worst-case cost of a 20-step loop.
- **Project:** the orders agent, with the refund behind human approval.
- **Defend:** step limit; tool count; retry policy.

### Ch 22. Asking a person: approvals and interrupts *(split out from the old security chapter)*
- **Builds on:** Ch 21's loop.
- **Opens with:** an agent that asks for approval on every step, so people click "yes" without reading.
- **Sections:** where the pause goes (after the model picks a tool, before it runs); approve, edit, reject, reply;
  only pause for risky actions; saving state so the second half can resume; showing the person enough to decide.
- **Project:** conditional approval for refunds above a threshold.
- **Defend:** the refund amount that triggers review, set by cost.

### Ch 23. Memory
- **Builds on:** Ch 12's context.
- **Opens with:** a customer who explains the same problem for the third time.
- **Sections:** short-term memory (the conversation); summarising and trimming; long-term memory: events, facts and
  habits; when to write long-term memory; keeping each customer's memory separate; false memories planted by
  attackers; what to keep, for how long, and the law.
- **Defend:** what you store and for how long.

### Ch 24. Planning and long-running tasks *(new chapter)*
- **Builds on:** Ch 21–23.
- **Opens with:** a 40-step job that crashes at step 31 and starts again from step 1.
- **Sections:**
  1. Plan first, then do: a plan in a fixed format
  2. A person approves the plan
  3. Tasks, statuses and the task table
  4. Which task can run now? Dependencies without cycles (topological order, in plain words)
  5. Running ready tasks side by side
  6. Passing results from one task to the next
  7. Resuming after a crash
  8. Checking each task against its acceptance criteria
- **Numbers:** a ten-task plan, which tasks run together, total time with and without parallel runs.
- **Project:** a "monthly complaints review" job that plans, runs and resumes.

### Ch 25. Many agents, and special kinds of agents
- **Builds on:** Ch 24.
- **Opens with:** one agent with 40 tools that keeps picking the wrong one.
- **Sections:** parallel readers, one writer; different models and tools for different jobs; the cost (many times
  the tokens of a chat); how teams of agents fail; coding agents; browser and computer-use agents; research agents;
  voice agents (needs research pass).
- **Decision:** a cost-based rule for one agent versus many.
- **Part V milestone:** an orders agent with tool tiers, approvals, memory and a resumable planner.

---

## PART VI: Protocols and frameworks (Ch 26–27)

*Map layer: Tools.*

### Ch 26. MCP and the other agent protocols
*(Merges the old Ch 25 and Ch 26.)*
- **Builds on:** Ch 13's tool descriptions.
- **Opens with:** the same "order status" tool rewritten four times for four apps.
- **Sections:** MCP word by word; tools, resources and prompts; clients, servers and the host; local and remote
  servers; giving a server only the folders and keys it needs; skills: packaged instructions loaded only when needed;
  agent-to-agent protocols; agents that pay (spending limits and confirmations, including UPI pilots, VERIFY); the
  risks of other people's servers and skills.
- **Shelf life:** changes monthly. Concepts here, details in Appendix C.
- **Project:** expose the Tarkika tools as an MCP server.

### Ch 27. Frameworks: how to choose, and when not to use one
- **Builds on:** Ch 21's raw loop.
- **Opens with:** a team that rewrote its agent twice in a year because the framework changed.
- **Sections:** what a framework hides; kinds of framework (graphs, vendor kits, role-play teams, prompt optimisers,
  typed outputs); a checklist (control, tracing, lock-in, maturity); the harness around the model; a thin kit, MCP for
  tools, your own control flow.
- **Project:** port the Ch 21 agent to one framework (code in the repo).
- **Part VI milestone:** tools behind MCP; the agent running in one framework.

---

## PART VII: Trust (Ch 28–30)

*Map layers: Safety, Quality.*

### Ch 28. Security for agents
- **Builds on:** Ch 13's threat model.
- **Opens with:** a zero-click data leak through an AI assistant (VERIFY details).
- **Sections:** prompt injection, direct and hidden; the OWASP lists in plain words (VERIFY wording); the trifecta map
  for every agent; design patterns that remove a leg; keys scoped to the task; sandboxes; classifiers are tripwires,
  not walls.
- **Project:** the trifecta map and 30 attack emails as a test suite.
- **Defend:** which leg you removed; what the agent's key can touch.

### Ch 29. Guardrails, private data and the law
- **Builds on:** Ch 28.
- **Opens with:** private data removed from the prompt but still sitting in the trace logs.
- **Sections:** checks on the way in and the way out; rules first, models second; redact, mask, hash or block; logs are
  a second copy of private data; India's DPDP rules and other laws (VERIFY dates); setting a guard's threshold by cost.
- **Decision:** blocking a real customer versus letting an attack through.

### Ch 30. Testing agents and watching them in production
- **Builds on:** Ch 14 and Ch 19.
- **Opens with:** a judge that passed "bought the item" when the agent had only added it to the cart.
- **Sections:** three levels of agent tests (end to end, steps, parts); check the final state, not the agent's claim;
  "works once" versus "works every time" (pass^k); LLM judges with yes/no labels, checked against people; judge biases;
  tracing; self-hosted versus hosted tracing; low latency can hide wrong answers.
- **Numbers:** pass^k at k = 4 for a 90% agent; judge agreement on 50 labels.
- **Part VII milestone:** trifecta map, attack suite, checked judge, traces.

---

## PART VIII: Production (Ch 31–35)

*Map layer: Operations.*

### Ch 31. From notebook to service
- **Opens with:** a demo that works on a laptop and falls over with ten users.
- **Sections:** an API around the agent; streaming; async work and queues; containers; timeouts, retries and never
  refunding twice; rate limits at the front door.
- **Project:** Tarkika as a deployed service.
- **Defend:** timeouts; retry policy; duplicate-refund protection.

### Ch 32. LLMOps: running AI systems day to day
- **Builds on:** Ch 12's "one word changes everything".
- **Opens with:** quality drops for three weeks and nobody changed the code.
- **Sections:** version everything that changes behaviour (prompts, models, knowledge, tools, skills); what Git does
  not track; tests before release and monitoring after (offline and online evals); releases: canary, blue-green, A/B,
  shadow; gateways, fallbacks and budgets; rollback; diagnosing a slow decline step by step.
- **Defend:** when you roll back; the alert that wakes someone up.

### Ch 33. Cost and speed, in rupees
- **Builds on:** Ch 8 and Ch 12.
- **Opens with:** a monthly bill three times the estimate.
- **Sections:** cost per task; find the slow or costly stage first (profiling); prompt caching; batch APIs; routing
  small to large; shorter outputs and lower effort; caching answers by meaning (semantic caching): threshold, expiry,
  what not to cache; cutting cost too far cuts quality.
- **Numbers:** the full monthly INR cost report at 10,000 tickets a day; cache threshold experiments.
- **Decision:** a cost-based routing threshold.

### Ch 34. Fine-tuning and distillation: last, not first
- **Opens with:** a team that fine-tuned to add knowledge and still got out-of-date answers.
- **Sections:** fine-tune for behaviour, not knowledge; try prompting and retrieval first; LoRA and QLoRA in plain
  words; preference pairs; teaching a small model from a big one (distillation); proving it worked.
- **Project:** distil a small ticket-triage model and compare cost and quality.

### Ch 35. Small, local and multimodal models *(needs research pass)*
- **Sections:** when local wins (privacy, cost, offline); running models on a laptop or phone; images and documents;
  speech and voice; choosing local or API.
- **Part VIII milestone:** a deployed service, a cost report and a distilled model.

---

## PART IX: System design (Ch 36)

### Ch 36. Designing AI systems, and real design reviews
- **Opens with:** "Design a support agent for an online store", 45 minutes, a whiteboard.
- **Sections:**
  1. A design method: ask questions, state assumptions, put numbers on them
  2. Who does this system replace or help? List what that person does
  3. Walking the system map layer by layer
  4. Diagnosis drills: slow system, bad answers, quality falling with no code change
  5. Reviews of real systems, worked and failed, each told as problem, design, what broke, fix (all VERIFY)
  6. The final design review of Tarkika

---

## PART X: Career (Ch 37–38)

### Ch 37. Your portfolio and the job market
- **Sections:** role names; company types in India; salary tiers (VERIFY near print); entry routes; a portfolio that
  impresses (real problem, measured evals, failure log, deployment, write-up); when certificates help.
- **Project:** the Tarkika README with evals, cost sheet and failure log.

### Ch 38. Interview preparation
- **Sections:** the two loop shapes (product companies, services firms); a question bank from every chapter; five
  system-design drills; a take-home eval harness; "defend every number" mock deep-dive; practising aloud with a timer.

---

## Back matter

- A. Answers to exercises and interview questions
- B. Pattern catalogue (one page each)
- C. Version register, dated (models, protocols, SDKs, prices)
- D. Maths refresher
- E. Glossary
- F. Index

---

## What changed from plan v1

1. **Removed every link to *Decide, Don't Generate*.** Calibration and decision thresholds are taught from scratch in
   Ch 2–3.
2. **Merged** pretraining and post-training (now Ch 7), and MCP with the other protocols (now Ch 26).
3. **Added** Ch 18 *Keeping knowledge fresh and fast at scale* (re-indexing, debouncing, filters, multi-tenancy,
   sharding), Ch 22 *Approvals and interrupts*, and Ch 24 *Planning and long-running tasks*.
4. **Moved** semantic caching into the cost chapter (Ch 33), with its risks.
5. **Every chapter** now has a "Builds on" link and a problem-first opening.
6. Chapter count stays at 38.

## Decisions still open

1. **Title:** "The Applied AI Engineer" (current), "Decide, Then Act" (old plan; it echoes the first book, which may
   clash with keeping them separate), or another.
2. **One volume or two:** Volume 1 = Parts I–IV (Ch 1–19, about 280 pages).
3. **Code:** short snippets in the book plus a companion repo, or design only.
