# Ship Real AI: final content list

*The AI Engineer Bootcamp for LLMs, RAG, MCP, AI Agents and Evals, from First Principles to Production and Interviews*

Status: final draft, 28 October 2026. Covers every topic from the transcript study, plus lasting foundations.
Fast-changing material (model names, prices, spec versions, CVE lists, year-numbered rankings, law dates) is left out.

## Module 1: Python for AI engineers
- Async calls
- Type hints and data models
- Environments and dependencies
- Error handling
- Testing

## Module 2: What AI engineering is
- Model provider, model and application
- What LLMs can't do: knowledge cutoff, no memory, fixed context window, different answers each run
- What an agent is: LLM + tools → LLM + context → model + harness
- Three kinds of AI work: building models, serving models, building applications
- Product thinking: which problems AI should solve, success metrics, build vs buy, is it worth the cost
- The system map
- First API call and what it costs
- Capstone brief

## Module 3: Foundations
- Probability as shares of many cases
- Rare events and false alarms (base rates)
- Precision, recall and the confusion matrix
- How sure is a test score: bootstrap confidence intervals
- Comparing two versions fairly
- Calibration: when 80% means 80%
- Classical ML: features, train/validate/test, leakage, baselines, overfitting
- Deep learning: neurons, layers, loss, gradient descent, backpropagation
- GPU memory maths
- Tokens and token cost (English vs Hindi vs Hinglish)
- Embeddings, similarity, the trade-off in embedding size

## Module 4: How LLMs work
- Attention and the transformer block
- Next-token prediction
- Position
- KV cache and its memory
- Pretraining, supervised fine-tuning, preference tuning, checkable rewards
- Why models are eager to please and confident when wrong
- Reasoning models and thinking effort
- Mixture of experts: total vs active parameters
- Long context and context rot
- Multimodal basics: how models read images, documents and speech
- Time to first token vs tokens per second
- Why output costs more than input
- Batching, prefix caching, speculative decoding, quantisation
- Why temperature 0 still varies
- Open weights vs licence
- How to choose a model

## Module 5: The decision layer
- Generating vs deciding
- Act, review or escalate
- Thresholds set by the cost of each kind of mistake
- Trusting a confidence score only after calibration
- Small fast models for easy cases, big models for hard ones
- Saying "I don't know"

## Module 6: Prompts and context engineering
- Parts of a prompt
- Everything the model sees is context
- The smallest useful set of tokens
- Lost in the middle: start and end matter most
- Context operations: expand, compress, select, prune, order
- Token budgeting
- Prompting reasoning models: the goal and the checks, not the steps
- Fixed text first (prompt caching), worked in rupees
- Compaction for long runs
- Fetching data just in time through tools
- One word changes everything: prompt versions

## Module 7: Tools and structured output
- Structured output
- Validate before acting
- Tool calling step by step: the model asks, code acts
- What the model sees about a tool: name, description, arguments
- Read tools vs write tools
- Call limits and tool loops
- Dynamic tool selection
- Too many tools blur the model's choice
- First threat model: private data, untrusted text, a way out

## Module 8: Search inside out
- Semantic vs exact-match search
- Inverted index
- BM25: term frequency, rare words, length penalty
- Vector search and HNSW
- Flat vs index search cost
- Choosing a vector store
- Similar is not the same as relevant

## Module 9: RAG
- RAG word by word
- Ingestion vs retrieval
- Reading messy PDFs and tables
- Chunking: size, overlap, by heading
- Chunking code: by class and function, AST
- Adding a short context to each chunk
- Hybrid search
- Fusion (RRF) vs reranking
- High recall first, then precision
- Hallucination: why it happens, kinds, detection, grounding
- Citations and "I don't know"
- When to skip RAG and send the whole document

## Module 10: Advanced RAG
- The RAG family: corrective, self-RAG, adaptive, agentic
- Query rewriting and decomposition
- HyDE
- Graph RAG
- Tree retrieval (RAPTOR)
- Index-style retrieval without vectors
- Text-to-SQL
- Agentic search: grep, search and SQL in a loop
- Searching pages as images

## Module 11: Data and evals
- Data work: collecting, cleaning, labelling, checking synthetic data, versioning datasets
- Evals as unit tests
- Golden datasets: by hand, synthetic, from production logs
- Reading real outputs and grouping failures (error analysis)
- Cheap code checks first
- Retrieval metrics: precision@k, recall@k, hit rate, MRR, NDCG
- Faithfulness vs correctness
- LLM as judge with yes/no labels
- Checking the judge against people
- Judge biases
- "Evals good, production bad": what to do

## Module 12: Memory
- Why the model forgets
- Building memory by hand: list → database with thread IDs
- Trimming and summarising
- Middleware and hooks
- Long-term memory: facts, events, habits
- Conflicting facts
- When to write long-term memory
- Keeping each user separate
- False memories planted by attackers

## Module 13: Agents
- Workflows vs agents
- Five workflows: chain, route, parallel, manager and workers, write and check
- Errors multiply across steps
- The agent loop from scratch
- ReAct
- Stop rules and budgets
- Retryable vs non-retryable errors, back-off, fallbacks
- Good tool design
- Query classifier: ask path vs plan path

## Module 14: Human approval, safety and responsible AI
- Where the pause goes
- Approve, edit, reject, reply
- Pause only for risky actions
- Saving state to resume
- Guardrails on input and output
- Private data: redact, mask, hash, block
- Rules-based vs model-based guards
- Prompt injection, direct and hidden
- Too much power given to an agent
- Safe patterns: plan-then-execute, dual model, action selector
- Scoped keys, sandboxes, backups out of reach
- Plain-language instructions are not permissions
- Logs are a second copy of private data
- Responsible AI: bias and fairness, showing uncertainty, undo and confirmation, telling users it is AI

## Module 15: Tool protocols and skills
- Why tools need a standard
- MCP word by word
- Host, client, server
- Local vs remote servers
- Writing your own server
- Browser automation
- Skills and progressive disclosure
- Risks of other people's servers and skills
- Agent-to-agent communication (concept)
- Agents that spend money: limits and confirmations

## Module 16: Planning and long-running tasks
- Plan first, in a fixed format
- Approving the plan
- Task table and statuses
- Dependencies without cycles
- Running ready tasks side by side
- Passing results on
- Resuming after a crash
- Progress files
- Acceptance criteria checked by a judge

## Module 17: Many agents and frameworks
- When many agents pay off
- Parallel readers, single writer
- Different models and tools for different jobs
- How agent teams fail
- Subagents
- Coding, browser and research agents
- What a framework hides
- How to choose a framework
- Harness engineering

## Module 18: Capstone architecture
- Project layers: config, LLM factory, context, agents, tools, safety, observability
- Secrets vs config
- Packaging as a command-line tool
- Index the code or grep it: two designs

## Module 19: Freshness and scale
- Stale answers
- Modified time vs content hash
- Incremental re-indexing
- Debouncing
- Full rebuild vs incremental
- Shadow index and atomic swap
- Metadata filtering
- Multi-tenancy
- Sharding, scatter-gather, hot shards
- Conflicting documents

## Module 20: Caching and cost
- Where to cache, and where not to
- Prompt caching vs semantic caching
- Threshold, expiry, cache keys
- Cache warm-up
- Short-term memory as implicit caching
- Never cache wrong answers
- Profile before you optimise
- Batch processing
- Routing small to large
- Cost per task in rupees
- Cutting cost too far cuts quality

## Module 21: Testing agents, observability and LLMOps
- Three levels of agent tests
- Check the final state, not the agent's claim
- "Works once" vs "works every time"
- User simulators
- Tracing, hosted vs self-hosted
- Low latency can hide wrong answers
- Version everything that changes behaviour
- What Git doesn't track
- Offline vs online evals
- Canary, blue-green, A/B, shadow releases
- Evals in CI
- Silent changes by the model provider
- Rollback

## Module 22: Production and fine-tuning
- API service, streaming, queues, containers
- Timeouts and no double refunds
- Rate limits and gateways
- Fine-tune for behaviour, not knowledge
- LoRA and QLoRA
- Preference pairs
- Distillation
- Reward hacking
- Local vs API models

## Module 23: System design and interviews
- Design method: ask questions, state assumptions, put numbers on them
- Who does the system replace?
- Walking the system map
- Moving a design to a new domain
- Diagnosis drills: slow system, bad answers, quality falling with no code change
- Interview drills: 10,000-page PDF, output vs input token cost, scaling RAG
- Capstone demo
- Portfolio
- Mock interviews
