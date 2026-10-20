# Agentic AI System Design, Agent Protocols and Agent Frameworks (state as of ~20 Oct 2026)

Source-quality legend used below:
- **[fetched]**: primary page read in full this session.
- **[search]**: the claim comes from search-result summaries. Usually secondary sources, so verify before printing.
- **[TK]**: training knowledge (cutoff June 2026), with the canonical primary URL. It was **not re-fetched this session**, so check the date and wording before publication.

Several late-2026 search results came from low-quality or AI-generated blogs and contain claims I could not verify, such as model names, acquisitions and revenue. These are flagged inline.

---

## 1. What are the canonical agent design patterns and when should each be used?

### Takeaway
The working vocabulary is still set by Anthropic's "Building effective agents" (19 Dec 2024). Its building block is the augmented LLM. It defines five workflows: prompt chaining, routing, parallelization, orchestrator-workers and evaluator-optimizer. Beyond those sit autonomous agents, meaning an LLM calling tools in a loop with feedback from the environment. The guiding rule is to use the simplest pattern that works and to add autonomy only when the steps cannot be predicted. Research-era patterns (ReAct, plan-and-execute, Reflexion/self-refine) are now mostly built into the model or the harness rather than hand-coded. Since 2025 the frontier of practice has moved to context engineering, harness design for long-running agents, memory, and specialised agent types (coding, computer-use, deep research).

### Cited Findings
**Anthropic taxonomy (canonical)**
- Published 19 Dec 2024. The page now carries a note that much of the tooling has changed. — [Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) [fetched]
- Workflows vs agents: "Workflows are systems where LLMs and tools are orchestrated through predefined code paths. Agents, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage." — [Anthropic](https://www.anthropic.com/engineering/building-effective-agents) [fetched]
- Building block: "an LLM enhanced with augmentations such as retrieval, tools, and memory" (the "augmented LLM"). — [Anthropic](https://www.anthropic.com/engineering/building-effective-agents) [fetched]
- **Prompt chaining** is for tasks that split cleanly into fixed subtasks; the goal is "to trade off latency for higher accuracy". **Routing** suits "distinct categories that are better handled separately". **Parallelization** has two forms: *sectioning* (independent subtasks run in parallel) and *voting* (the same task run several times). **Orchestrator-workers** is "well-suited for complex tasks where you can't predict the subtasks needed". **Evaluator-optimizer** is effective "when we have clear evaluation criteria, and when iterative refinement provides measurable value". — [Anthropic](https://www.anthropic.com/engineering/building-effective-agents) [fetched]
- Agents are for open-ended problems where the number of steps can't be hardcoded. "The autonomous nature of agents means higher costs, and the potential for compounding errors"; test them in sandboxes with guardrails. — [Anthropic](https://www.anthropic.com/engineering/building-effective-agents) [fetched]
- Three principles: simplicity; transparency ("explicitly showing the agent's planning steps"); and a carefully crafted agent-computer interface (ACI) "through thorough tool documentation and testing". On frameworks: start with LLM APIs directly, and "if you do use a framework, ensure you understand the underlying code". — [Anthropic](https://www.anthropic.com/engineering/building-effective-agents) [fetched]

**Research-lineage patterns**
- **ReAct** (Yao et al., Oct 2022) interleaves reasoning traces with actions and observations. It is the ancestor of the standard tool-calling loop. — [arXiv 2210.03629](https://arxiv.org/abs/2210.03629) [TK]
- **Reflexion** (Shinn et al., Mar 2023) feeds verbal self-reflection back into later attempts. **Self-Refine** (Madaan et al., Mar 2023) iterates on its own output using its own feedback. Both are forerunners of evaluator-optimizer. — [arXiv 2303.11366](https://arxiv.org/abs/2303.11366); [arXiv 2303.17651](https://arxiv.org/abs/2303.17651) [TK]
- **Plan-and-execute / Plan-and-Solve** (Wang et al., May 2023) makes an explicit plan first, then executes the steps, with optional replanning. It became popular in LangGraph tutorials. — [arXiv 2305.04091](https://arxiv.org/abs/2305.04091) [TK]
- **Memory taxonomy (CoALA, Sumers et al., 2023):** working memory, plus long-term episodic, semantic and procedural memory. It is widely reused to classify agent memory. — [arXiv 2309.02427](https://arxiv.org/abs/2309.02427) [TK]

**Context engineering, long-running agents and memory (2025-2026)**
- Anthropic's "Effective context engineering for AI agents" treats context as a finite "attention budget". It recommends just-in-time retrieval: keep lightweight references such as file paths and load data via tools at runtime. In Claude Code, CLAUDE.md is loaded up front while glob/grep fetch on demand. — summarised by [agentic-ai.readthedocs.io](https://agentic-ai.readthedocs.io/en/latest/ContextEngineering/anthropic/) [search]; primary: [anthropic.com/engineering](https://www.anthropic.com/engineering) [TK, Sept 2025]
- "Effective harnesses for long-running agents" (Anthropic engineering) addresses agents working across many context windows. Secondary write-ups describe the pattern: an initializer session sets things up; each fresh session reads a progress file plus recent git history, makes incremental progress, runs tests and verification, and leaves a clean commit and a structured handoff. — [dev.to summary](https://dev.to/claudiuspapirus/why-ai-agents-fail-long-projects-and-the-anthropic-fix-3029); [Anthropic engineering index](https://www.anthropic.com/engineering?album=45) [search, primary not fetched; TK: published ~Nov 2025]
- Anthropic's memory tool combined with context editing is reported to give +39% on an internal agentic eval (context editing alone +29%). — [aceverse blog](https://www.aceverse.co/en/blog/ai-employees-context-not-memory-2026) [search, unverified secondary; TK: originally from Anthropic's Sept 2025 "context management" announcement]

**Human-in-the-loop**
- HITL is now a first-class framework primitive. LangChain 1.0 ships built-in human-in-the-loop middleware (along with summarization and PII-redaction middleware). — [LangChain blog, 1.0](https://blog.langchain.com/langchain-langgraph-1dot0) [search]
- AP2 (agent payments) uses signed "mandates" to record a user's approval of agent-initiated transactions: HITL authorisation built into a protocol. Google's Auto Browse is gated, with approval required on sensitive steps. — [Wikipedia, Agentic commerce](https://en.wikipedia.org/wiki/Agentic_commerce); [codercops](https://blog.codercops.com/blog/ai-browser-agents-comet-atlas-mariner-2026) [search]

**Specialised agent types (dated)**
- *Computer use:* Anthropic computer-use beta (22 Oct 2024); OpenAI Operator (23 Jan 2025); ChatGPT agent (17 Jul 2025); ChatGPT Atlas browser (21 Oct 2025); Claude for Chrome research preview (Aug 2025). — [Anthropic news](https://www.anthropic.com/news/3-5-models-and-computer-use); [OpenAI Operator](https://openai.com/index/introducing-operator/); [OpenAI ChatGPT agent](https://openai.com/index/introducing-chatgpt-agent/) [TK]
- 2026 browser-agent churn (all **[search]**, single or secondary sources): OpenAI reportedly announced Atlas's retirement on 9 Jul 2026, with shutdown on 9 Aug 2026, and agentic browsing moving into the ChatGPT desktop app and a Chrome extension. Google Project Mariner reportedly shut down as a standalone product on 4 May 2026. Gemini "Auto Browse" has reportedly been in desktop preview since Jan 2026 and reached Android at the end of June 2026. OpenAI reportedly launched "ChatGPT Work" on 9 Jul 2026 for hours-long sandboxed projects. — [codercops](https://blog.codercops.com/blog/ai-browser-agents-comet-atlas-mariner-2026); [freeacademy](https://freeacademy.ai/lessons/the-2026-ai-browser-landscape); [nerdleveltech](https://nerdleveltech.com/en/ai-browser-agents-claude-chatgpt-gemini) **(UNVERIFIED; check primary OpenAI/Google announcements)**
- Benchmarks: Anthropic models are reported to lead OSWorld-Verified. A harder "OSWorld 2.0" (108 long-horizon tasks) is reported to have a best full-completion rate of 20.6% ("Claude Opus 4.8"). — [fast.io](https://www.fast.io/resources/best-computer-use-ai-agents-2026.md); [simular.ai](https://www.simular.ai/alternatives/computer-use-agents) [search, **single secondary source; model name unverified**]
- *Coding agents:* Claude Code research preview (24 Feb 2025), GA with Claude 4 (22 May 2025); OpenAI Codex CLI (16 Apr 2025) and cloud Codex agent (16 May 2025); GitHub Copilot coding agent (May 2025); Cursor background agents (mid-2025) and Cursor 2.0 with its Composer model (Oct 2025). — [Anthropic Claude 3.7/Claude Code](https://www.anthropic.com/news/claude-3-7-sonnet); [OpenAI Codex](https://openai.com/index/introducing-codex/) [TK]
- 2026 coding-agent market (all **[search], conflicting and secondary**). JetBrains survey data (May-Jul 2026) reportedly gives workplace use as Claude Code 39%, GitHub Copilot 21%, OpenAI Codex 16%, Cursor 12%. Cursor's ARR was reported at $2B by Feb-Mar 2026 (Bloomberg-reported, not company-disclosed). Claude Code run-rate was reported at >$500M in Sept 2025 (Anthropic) and ">$2.5B" by Feb 2026 (attributed to Anthropic's Series G). Cursor reportedly runs up to 8 parallel agents with automatic judging. All three major tools have reportedly moved to usage-based billing (Claude Code metered pricing in mid-June 2026). One blog claims SpaceX acquired Cursor in Aug 2026 (price disputed). **This acquisition claim is highly unusual and unverified; do not print without a primary source.** — [ajayk.sh](https://www.ajayk.sh/blog/coding-agents-market-2026-share-productivity/); [uvik](https://uvik.net/blog/claude-code-vs-cursor-vs-copilot-vs-codex-2026/); [turingcollege](https://www.turingcollege.com/blog/best-ai-coding-agents-2026-claude-code-codex-cursor)
- Interaction styles: Codex is described as "fire-and-review-later" (cloud/background), Claude Code as a terminal agent on the dev machine, and Cursor as steering in the editor. — [turingcollege](https://www.turingcollege.com/blog/best-ai-coding-agents-2026-claude-code-codex-cursor) [search]
- *Deep research agents:* Google Gemini Deep Research (Dec 2024); OpenAI deep research (2 Feb 2025); Anthropic Research (Apr 2025), built as an orchestrator-worker multi-agent system. Deep research and MCP are now built-in tools of OpenAI's Responses API. — [OpenAI deep research](https://openai.com/index/introducing-deep-research/) [TK]; [OpenAI community: Assistants sunset notice](https://community.openai.com/t/assistants-api-beta-deprecation-august-26-2026-sunset/1354666) [search]

### Inferences
- For the book, use a ladder: single LLM call, then augmented LLM, then a workflow (one of the five), then a single agent loop, then multi-agent. Justify each rung by measured eval gains. That is the consensus from Anthropic's guidance and practitioner debates.
- ReAct, reflection and plan-and-execute are now best taught as *behaviours of reasoning models inside a harness*, not as prompt templates. Native "thinking", tool calling and todo/plan tools (as in Claude Code) absorb them.
- "Context engineering" and "harness engineering" have replaced "prompt engineering" as the key skills for agents in 2025-2026.

### Gaps
- I did not fetch the primary Anthropic posts on context engineering, long-running harnesses or multi-agent research this session. Exact dates and figures should be checked at anthropic.com/engineering.
- The 2026 browser-agent product changes (Atlas retirement, ChatGPT Work, Mariner shutdown) and the OSWorld 2.0 numbers rest on secondary blogs only.
- I found no reliable 2026 figures on production adoption of specific memory architectures (e.g. Mem0, Letta, Zep).

---

## 2. What is the current status of MCP and A2A (versions, governance, adoption, security)?

### Takeaway
MCP is the de facto agent-to-tool standard. Its current spec is **2026-07-28** (final 28 Jul 2026), a major rewrite to a **stateless** core. It is governed by the **Agentic AI Foundation (AAIF)** under the Linux Foundation (formed 9 Dec 2025). Its SDKs see about 0.5B downloads a month, and the registry lists tens of thousands of servers. Its security record is poor: tool poisoning, prompt injection via tool output, and dozens of 2026 CVEs, many of them shell or command injection. A2A (Google, Apr 2025) went to the Linux Foundation in June 2025, reached v1.0 in early 2026 (sources conflict: Jan vs Mar), and moved into the AAIF on about 17-20 Aug 2026 alongside MCP. Over 150 organisations backed it as of April 2026.

### Cited Findings
**MCP timeline and spec versions**
- Announced by Anthropic on 25 Nov 2024. — [Anthropic news](https://www.anthropic.com/news/model-context-protocol) [TK]
- Spec versions: **2024-11-05** (initial; stdio + HTTP+SSE); **2025-03-26** (Streamable HTTP transport, OAuth 2.1 authorization, tool annotations); **2025-06-18** (structured tool output, elicitation, resource links, OAuth Resource Server classification with RFC 8707 resource indicators, JSON-RPC batching removed); **2025-11-25** (first-anniversary release: experimental Tasks, Client ID Metadata Documents, among others). — [MCP spec changelog](https://modelcontextprotocol.io/specification) [TK]; 2025-11-25 confirmed as the predecessor in [MCP blog](https://blog.modelcontextprotocol.io/posts/2026-07-28/) [fetched]
- **2026-07-28 spec (current):** released 28 Jul 2026 with updated Tier 1 SDKs. — [MCP blog](https://blog.modelcontextprotocol.io/posts/2026-07-28/) [fetched]
  - **Stateless core:** the `initialize`/`initialized` handshake and the `Mcp-Session-Id` header are retired. Each request carries its protocol version, client identity and capabilities in `_meta`. An optional `server/discover` RPC is added, so any request can hit any instance behind a round-robin load balancer. — [MCP blog](https://blog.modelcontextprotocol.io/posts/2026-07-28/) [fetched]; see also [Google Developers Blog](https://developers.googleblog.com/scaling-ai-agent-infrastructure-with-the-mcp-stateless-updates/) [search]
  - **Header routing:** Streamable HTTP requests must carry `Mcp-Method` and `Mcp-Name`, so gateways can route and meter without parsing the body. — [MCP blog](https://blog.modelcontextprotocol.io/posts/2026-07-28/) [fetched]
  - **Multi Round-Trip Requests (MRTR)** replace server-initiated `elicitation/create`, `sampling/createMessage` and `roots/list`. The server returns `resultType: "input_required"` and the client retries with `inputResponses`. — [MCP blog](https://blog.modelcontextprotocol.io/posts/2026-07-28/) [fetched]
  - **Cacheable lists:** list and read responses carry `ttlMs` and `cacheScope`, with a deterministic order. — [MCP blog](https://blog.modelcontextprotocol.io/posts/2026-07-28/) [fetched]
  - **Auth hardening:** `iss` validation per RFC 9207 (SEP-2468); `application_type` in Dynamic Client Registration for localhost redirects (SEP-837); credentials bound to their issuer (SEP-2352). **DCR is deprecated in favour of Client ID Metadata Documents (CIMD).** — [MCP blog](https://blog.modelcontextprotocol.io/posts/2026-07-28/) [fetched]
  - **Extensions framework** formally adopted. Named extensions: **Tasks** (moved out of core to `io.modelcontextprotocol/tasks`, with poll-based `tasks/get` and new `tasks/update`, SEP-2663), **MCP Apps** (interactive UI), and **Enterprise Managed Authorization (EMA)**. Notifications are consolidated into an opt-in `subscriptions/listen` stream. — [MCP blog](https://blog.modelcontextprotocol.io/posts/2026-07-28/) [fetched]
  - **Deprecations:** Roots, Sampling and Logging (SEP-2577); the legacy HTTP+SSE transport; DCR. There is now a formal 12-month minimum deprecation window. — [MCP blog](https://blog.modelcontextprotocol.io/posts/2026-07-28/) [fetched]
  - SDKs supporting 2026-07-28: TypeScript, Python, Go, C# (Rust in beta). — [MCP blog](https://blog.modelcontextprotocol.io/posts/2026-07-28/) [fetched]
- Migration commentary describes this as a breaking change for any code that relied on session identifiers. — [AAIF blog](https://aaif.io/blog/mcp-2026-07-28-whats-changing-and-how-to-migrate); [developersdigest](https://www.developersdigest.tech/blog/mcp-2026-07-28-breaking-changes) [search]
- MCP Apps: OpenAI, Anthropic and the MCP-UI maintainers proposed it (SEP-1865) in Nov 2025, generalising OpenAI's Apps SDK (Oct 2025) UI-in-chat pattern. — [MCP blog](https://blog.modelcontextprotocol.io/) [TK]; named as an extension in the 2026-07-28 post [fetched]

**MCP adoption**
- Tier 1 SDKs see "close to half-a-billion downloads a month". The TypeScript and Python SDKs have each passed 1 billion total downloads. — [MCP blog, 2026-07-28](https://blog.modelcontextprotocol.io/posts/2026-07-28/) [fetched]
- Official MCP Registry launched in preview on 8 Sep 2025. — [MCP blog, registry preview](https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/) [search]
- Registry size: 9,652 latest server records (28,959 server/version records) in a 24 May 2026 API pull; about 30,375 servers by 10 Sep 2026, with about a third published by around 50 accounts. — [Digital Applied](https://digitalapplied.com/blog/mcp-adoption-statistics-2026); [dev.to](https://dev.to/amareswer/the-mcp-registry-by-the-numbers-38nc) [search, independent snapshots]. I found no GA announcement for the registry.
- Supported by Claude, ChatGPT, Cursor and others. OpenAI adopted MCP in the Agents SDK and Responses API (Mar-May 2025). — [SD Times](https://sdtimes.com/ai/linux-foundation-forms-agentic-ai-foundation-to-be-new-home-for-mcp-goose-and-agents-md/) [search]

**Governance: the Agentic AI Foundation (AAIF)**
- The Linux Foundation formed the AAIF on **9 Dec 2025**. Founding projects: **MCP** (donated by Anthropic), **goose** (Block) and **AGENTS.md** (OpenAI). It is structured as a directed fund. Listed platinum members include AWS, Google, Microsoft, Bloomberg and Cloudflare, plus Anthropic, Block and OpenAI (lists differ between sources). — [InfoQ](https://infoq.com/news/2025/12/agentic-ai-foundation/); [The New Stack](https://thenewstack.io/anthropic-donates-the-mcp-protocol-to-the-agentic-ai-foundation/); [SD Times](https://sdtimes.com/ai/linux-foundation-forms-agentic-ai-foundation-to-be-new-home-for-mcp-goose-and-agents-md/) [search]
- The AAIF reportedly grew from fewer than 40 members to more than 250 by Aug 2026, including Google, Microsoft, Amazon, Anthropic, OpenAI, Bloomberg, Shopify and Block. — [Axios, 17 Aug 2026](https://axios.com/2026/08/17/a2a-agentic-ai-foundation-open-ai-standards) [search]
- MCP's own technical governance runs through Spec Enhancement Proposals (SEPs, e.g. SEP-2468, SEP-2577, SEP-2663) and core maintainers. — [MCP blog](https://blog.modelcontextprotocol.io/posts/2026-07-28/) [fetched]

**MCP security problems**
- *Tool poisoning:* malicious instructions are hidden in tool descriptions, invisible to users but read by the model (term from Invariant Labs, 2025). — [hol.org](https://hol.org/blog/mcp-tool-poisoning-ai-agent-protocol-attack-surface); [glasp](https://glasp.ai/articles/mcp-security-tool-poisoning-supply-chain) [search]
- *Prompt injection via tool output:* the MCPTox benchmark reports that even the strongest commercial agents failed about half of its scenarios. — [godberrystudios](https://godberrystudios.com/posts/mcp-security-tool-poisoning-prompt-injection-2026/) [search]
- *"Lethal trifecta"* (Simon Willison, Jun 2025): private data, plus untrusted content, plus an exfiltration channel. This is the standard framing for MCP tool combinations. — [simonwillison.net](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) [TK]
- CVE wave: 30+ CVEs against MCP implementations in about 60 days in early 2026. One breakdown puts about 43% as shell or command injection. — [heyuan110](https://www.heyuan110.com/posts/ai/2026-03-10-mcp-security-2026/); [noqta](https://noqta.tn/en/blog/securite-serveurs-mcp-vulnerabilites-protection-guide-2026) [search]
- Specific CVEs [search; verify on NVD]:
  - **CVE-2025-6514**: mcp-remote OS command injection, CVSS 9.6.
  - **CVE-2025-54135** ("CurXecute"): a prompt injection in a Slack message makes Cursor rewrite its MCP config to add an attacker's server.
  - **CVE-2026-30623**: a STDIO-transport config-driven command execution disclosed by OX Security on 15 Apr 2026. One source says over 200,000 vulnerable instances and "Anthropic won't fix", which I could not verify.
  - **CVE-2026-33032** ("MCPwn"): auth bypass in the nginx-ui MCP server, CVSS 9.8, reported as actively exploited.
  - **CVE-2026-27896**: case-insensitive JSON parsing in the Go SDK allowing a validation bypass.
  - **CVE-2026-5058**: aws-mcp-server RCE, CVSS 9.8.
  — [mcp.directory](https://mcp.directory/blog/mcp-security-200000-exposed-servers-owasp-mcp-top-10-cves); [dev.to](https://dev.to/gentic_news/mcps-cve-2026-30623-anthropic-wont-fix-stdio-command-injection-mh6); [practical-devsecops](https://www.practical-devsecops.com/mcp-security-statistics-2026-report/)
- An OWASP MCP Top 10 now exists. MCP scanners have high false-positive rates (one audit found about 78% for YARA-based scanners). — [mcp.directory](https://mcp.directory/blog/mcp-security-200000-exposed-servers-owasp-mcp-top-10-cves) [search]
- Earlier incidents: the GitHub MCP "toxic agent flow" (Invariant, May 2025); the malicious `postmark-mcp` npm package (Sept 2025, the first known malicious MCP server in the wild); and the MCP Inspector RCE CVE-2025-49596. — [TK; verify]

**A2A (Agent2Agent)**
- Announced by Google on 9 Apr 2025 with 50+ partners. — [Google Developers Blog](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/) [TK]
- Donated to the Linux Foundation in June 2025 (Open Source Summit NA, ~23 Jun 2025). — [Wikipedia, Agent2Agent](https://en.wikipedia.org/wiki/Agent2Agent) [search]
- IBM's Agent Communication Protocol (ACP, from BeeAI) merged into A2A in Aug 2025. — [TK; verify at lfaidata/A2A blog]. Note that the "ACP" acronym clashes with the OpenAI/Stripe **Agentic Commerce Protocol** and with Zed's **Agent Client Protocol** (editor-to-coding-agent, Aug 2025).
- v0.3 (Jul 2025) added gRPC and signed Agent Cards [TK]. **v1.0:** one arXiv paper dates it to **Jan 2026**, with signed Agent Cards marking production-readiness; the Axios-era coverage says the first stable spec shipped in **March 2026**. **Unresolved conflict.** v1.0.1 (May 2026) is reported to add an extension mechanism. — [arXiv A2ABreak 2609.10871](https://arxiv.org/pdf/2609.10871); [arXiv 2606.31498](https://arxiv.org/pdf/2606.31498); [aimagazine](https://aimagazine.com/news/why-did-googles-a2a-join-the-agentic-ai-foundation) [search]
- Linux Foundation press release, 9 Apr 2026 (A2A's first anniversary): over 150 supporting organisations, integration across Google, Microsoft and AWS platforms, and enterprise production use. — [PR Newswire / LF](https://www.prnewswire.com/news-releases/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year-302737641.html) [search; the page failed to fetch]
- **A2A joined the AAIF:** Axios exclusive dated 17 Aug 2026; one outlet gives the formal transfer as 20 Aug 2026. A2A now sits alongside MCP, with MCP covering agent-to-tool and A2A covering agent-to-agent. — [Axios](https://axios.com/2026/08/17/a2a-agentic-ai-foundation-open-ai-standards); [Techzine](https://www.techzine.eu/news/devops/143659/google-transfers-a2a-to-the-agentic-ai-foundation/); [AAIF project page](https://aaif.io/projects/agent2agent); [AAIF blog](https://aaif.io/blog/a2a-joins-aaif) [search]
- Adoption reality check: practitioner commentary describes A2A as widely endorsed but far less deployed than MCP. Academic work (A2ABreak, Sept 2026) systematically analyses A2A security weaknesses. — [glukhov.org](https://www.glukhov.org/ai-systems/comparisons/a2a-protocol-2026-adoption/); [arXiv 2609.10871](https://arxiv.org/pdf/2609.10871) [search]

### Inferences
- The 2026-07-28 stateless rewrite marks MCP's shift from a "local tool plug-in" (stdio, desktop apps) to a "distributed, gateway-friendly protocol". Books written against 2025 specs (sessions, sampling, roots, SSE) are now out of date.
- By late 2026 the AAIF is the de facto neutral home for the open agent stack (MCP, A2A, AGENTS.md, goose), with all the major labs as members. The "protocol wars" ended mainly by consolidation, not by a winner-take-all outcome.
- Security is MCP's biggest weakness. For the book, teach: treat all tool descriptions and outputs as untrusted; avoid the lethal trifecta; pin and sign servers; use registries and gateways; apply least-privilege OAuth; and sandbox stdio servers.

### Gaps
- I found no official MCP Registry GA date or official server count; the numbers above are independent snapshots.
- The A2A v1.0 release date conflicts between sources (Jan vs Mar 2026). The LF and PR Newswire primary pages could not be fetched (DNS failure).
- CVE details and CVSS scores come from secondary blogs; check them on NVD.
- No independent data on what share of MCP servers are remote vs local in 2026.

---

## 3. Which frameworks lead in late 2026 and what are their trade-offs? (including "framework vs no framework")

### Takeaway
Frameworks have consolidated around a few stable (1.0+) options. **LangGraph/LangChain 1.0** (Oct 2025) is the default for stateful, controllable, model-agnostic orchestration. Vendor SDKs (OpenAI Agents SDK, Claude Agent SDK, Google ADK, Microsoft Agent Framework 1.0 from Apr 2026) are the natural choice when you are committed to that vendor's models or cloud. TypeScript teams use Vercel AI SDK or Mastra. Pydantic AI, DSPy and smolagents fill type-safety, prompt-optimisation and minimalist niches. Anthropic's "start with the raw API" advice still shapes the debate. In 2026 the practical answer is often "use a thin SDK or harness, plus MCP for tools, plus your own control flow".

### Cited Findings
**LangChain / LangGraph**
- LangChain 1.0 and LangGraph 1.0 were released on 22 Oct 2025, with no breaking changes promised until 2.0. LangGraph is the low-level runtime; LangChain is the higher-level API on top. — [LangChain blog](https://blog.langchain.com/langchain-langgraph-1dot0) [search]
- `create_agent` replaces LangGraph's deprecated `create_react_agent`. **Middleware** hooks into the agent loop, with built-in human-in-the-loop, summarization and PII redaction. Other 1.0 additions: standard content blocks (provider-agnostic) and structured output inside the loop. The legacy chains and `AgentExecutor` moved to `langchain-classic`. — [LangChain blog](https://blog.langchain.com/langchain-langgraph-1dot0); [clickittech](https://www.clickittech.com/ai/langchain-1-0-vs-langgraph-1-0/) [search]
- Comparison blogs generally call LangGraph the most mature option for stateful, complex production workflows with HITL and durable execution. — [LangChain resource page](https://www.langchain.com/resources/ai-agent-frameworks) (vendor); [morphllm](https://www.morphllm.com/ai-agent-framework) [search]

**OpenAI Agents SDK, Responses API and AgentKit**
- The Responses API and Agents SDK launched on 11 Mar 2025 (the Agents SDK succeeded the experimental Swarm). Primitives: agents, handoffs, guardrails, sessions and tracing. — [OpenAI, New tools for building agents](https://openai.com/index/new-tools-for-building-agents/) [TK]
- AgentKit (Agent Builder visual canvas, ChatKit, Connector Registry, evals) was announced at DevDay on 6 Oct 2025. — [OpenAI DevDay 2025](https://openai.com/index/introducing-agentkit/) [TK]
- The **Assistants API sunset was set for 26 Aug 2026**. The Responses API (with Conversations) reached feature parity, and its built-in tools include deep research, MCP and computer use. Concept mapping: Assistants become Prompts, Threads become Conversations, Runs become Responses. Azure OpenAI was said not to be affected. — [OpenAI community](https://community.openai.com/t/assistants-api-beta-deprecation-august-26-2026-sunset/1354666); [Microsoft Q&A](https://learn.microsoft.com/en-us/answers/questions/5571874/openai-assistants-api-will-be-deprecated-in-august) [search]. I could not confirm whether the shutdown happened on schedule.
- Comparison blogs say the Agents SDK suits OpenAI-committed teams, centres on handoffs and guardrails, and lacks native A2A. — [morphllm](https://www.morphllm.com/ai-agent-framework) [search]

**Claude Agent SDK**
- Claude Code's harness was exposed as the Claude Code SDK (2025), then renamed the **Claude Agent SDK** on 29 Sep 2025 with Claude Sonnet 4.5. It provides the same agent loop, tools, context compaction, subagents, hooks, MCP and Skills as Claude Code. — [Anthropic engineering, Building agents with the Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk) [TK]; primitive reference in [morphllm](https://www.morphllm.com/ai-agent-framework) [search]

**Google ADK**
- Launched at Cloud Next on 9 Apr 2025 (Python), alongside A2A. Java and Go 1.0 releases are reported for early 2026. It has native A2A support, is often linked with multimodal and Gemini work, and has joined the AG-UI ecosystem. — [morphllm](https://www.morphllm.com/ai-agent-framework); [CopilotKit](https://www.copilotkit.ai/blog/ag-ui-is-redefining-the-agent-user-interaction-layer) [search]; launch date [TK]

**Microsoft Agent Framework**
- It merges AutoGen and Semantic Kernel. Public preview was Oct 2025 [TK]. The release candidate for .NET and Python came on 19 Feb 2026, and **1.0 GA on 3 Apr 2026** (GA date from secondary sources only). AutoGen is now in maintenance mode and community-managed; Semantic Kernel gets only critical fixes, with new features going into Agent Framework. It supports MCP and A2A natively. — [MS devblogs, RC migration post](https://devblogs.microsoft.com/agent-framework/migrate-your-semantic-kernel-and-autogen-projects-to-microsoft-agent-framework-release-candidate/); [rywalker.com](https://rywalker.com/research/microsoft-agent-framework); [atlan](https://atlan.com/know/ai-agent/microsoft/semantic-kernel/) [search]

**Others (mostly [TK]; check versions)**
- **CrewAI**: role- and task-based "crews" plus event-driven "Flows". Popular for quick multi-agent prototypes; often criticised as harder to control in production than graph runtimes. — [agentmelt comparison](https://agentmelt.com/blog/ai-agent-frameworks-compared-2026/) [search]
- **LlamaIndex**: data and RAG-centric, with event-driven Workflows and agent abstractions. It has an official AG-UI/CopilotKit integration (Jun 2025). — [CopilotKit blog](https://www.copilotkit.ai/blog/introducing-llamaindex-integration-with-copilotkit) [search]
- **DSPy** (Stanford): "programming, not prompting". Declarative signatures and modules with optimizers (MIPROv2, GEPA, etc.) that compile prompts and few-shot examples against a metric. It suits teams with eval sets that want automatic prompt optimisation. — [dspy.ai](https://dspy.ai) [TK]
- **Pydantic AI**: type-safe, Python-first agent framework from the Pydantic team; v1.0 Sept 2025 [TK]; integrates with Logfire for observability. — [ai.pydantic.dev](https://ai.pydantic.dev) [TK]
- **smolagents** (Hugging Face, Dec 2024): a minimalist library centred on "code agents" that write Python actions instead of JSON tool calls. — [huggingface.co/blog/smolagents](https://huggingface.co/blog/smolagents) [TK]
- **Mastra**: TypeScript agent framework from the Gatsby founders, with agents, workflows, memory, evals and MCP. — [mastra.ai](https://mastra.ai) [TK; 1.0 date not verified]
- **Vercel AI SDK**: the dominant TypeScript LLM/UI toolkit. AI SDK 5 (Jul 2025) added agent-loop control; AI SDK 6 added an `Agent` abstraction (late 2025). — [vercel.com/blog](https://vercel.com/blog) [TK; check versions]
- **goose** (Block): an open-source local agent, now an AAIF project. — [SD Times](https://sdtimes.com/ai/linux-foundation-forms-agentic-ai-foundation-to-be-new-home-for-mcp-goose-and-agents-md/) [search]

**Framework vs no framework**
- Anthropic: frameworks "add layers of abstraction that can obscure the underlying prompts and responses, making them harder to debug". Start with LLM APIs directly. — [Anthropic](https://www.anthropic.com/engineering/building-effective-agents) [fetched]
- Comparison blogs advise choosing by your existing cloud and model commitment first, then by how much state management and HITL you need. One unverified benchmark found LangGraph had the smallest footprint and fewest lines of code compared with the OpenAI Agents SDK and ADK. — [agentmail](https://www.agentmail.to/blog/best-ai-agent-frameworks-2026); [agentlist.top](https://www.agentlist.top/en/articles/best-ai-agent-framework-2026/) [search, low-quality sources]

### Inferences
- Taxonomy for the book:
  - **Orchestration runtimes**: LangGraph, Microsoft Agent Framework workflows, Mastra workflows, LlamaIndex Workflows.
  - **Vendor agent SDKs / harnesses**: OpenAI Agents SDK, Claude Agent SDK, Google ADK.
  - **Role-play multi-agent**: CrewAI, the AutoGen lineage.
  - **Optimisation / typing layers**: DSPy, Pydantic AI.
  - **UI / TypeScript toolkits**: Vercel AI SDK, AG-UI/CopilotKit.
- The trend is that protocols (MCP, A2A, AG-UI) commoditise integration, so framework lock-in matters less. The value moves to durable execution, observability and tracing, evals, and HITL.
- The Assistants-to-Responses migration and the AutoGen and Semantic Kernel consolidation are cautionary tales about API churn. Pin versions and keep business logic out of framework abstractions.

### Gaps
- I did not retrieve reliable late-2026 GitHub star counts or download metrics for these frameworks. Pull them live via the GitHub API before publication.
- Current versions and dates for Mastra, Vercel AI SDK 6, CrewAI, DSPy 3.x and Pydantic AI are from training knowledge only.
- There is no official Microsoft source for the 3 Apr 2026 GA date.

---

## 4. What new agent capabilities and products were introduced in 2025-2026 (with dates)?

### Takeaway
2025 was the year of agent infrastructure. It brought agent SDKs, the Responses API, MCP everywhere, A2A, Agent Skills, AGENTS.md, the AAIF, commerce and payment protocols, coding agents going GA, and computer-use agents in consumer products. 2026 has been about consolidation and hardening: A2A v1.0, the stateless MCP 2026-07-28 rewrite, Microsoft Agent Framework 1.0, the Assistants API sunset, A2A joining the AAIF, AG-UI growth, and churn among browser agents.

### Cited Findings (chronological; items marked [TK] need a date check)
- **Dec 2024**: Anthropic "Building effective agents" (19 Dec) [fetched, [link](https://www.anthropic.com/engineering/building-effective-agents)]; Hugging Face smolagents [TK].
- **Jan 2025**: OpenAI Operator (23 Jan) [TK, [link](https://openai.com/index/introducing-operator/)].
- **Feb 2025**: OpenAI deep research (2 Feb); Claude Code research preview (24 Feb) [TK].
- **Mar 2025**: OpenAI Responses API and Agents SDK (11 Mar) [TK, [link](https://openai.com/index/new-tools-for-building-agents/)]; MCP spec 2025-03-26 (Streamable HTTP, OAuth) [TK]; OpenAI announces MCP support (late Mar) [TK].
- **Apr 2025**: Google A2A and ADK (9 Apr) [TK]; OpenAI Codex CLI (16 Apr) [TK].
- **May 2025**: Codex cloud agent (16 May); GitHub Copilot coding agent; Claude Code GA with Claude 4 (22 May) [TK].
- **Jun 2025**: A2A donated to the Linux Foundation [search, [Wikipedia](https://en.wikipedia.org/wiki/Agent2Agent)]; MCP spec 2025-06-18 [TK]; LlamaIndex AG-UI integration [search, [CopilotKit](https://www.copilotkit.ai/blog/introducing-llamaindex-integration-with-copilotkit)]; Cognition "Don't build multi-agents" and Anthropic multi-agent research system post [TK].
- **Jul 2025**: ChatGPT agent (17 Jul) [TK].
- **Aug 2025**: IBM ACP merges into A2A; Claude for Chrome preview; AGENTS.md promoted as a cross-vendor convention [TK].
- **Sep 2025**: Google AP2 agent payments protocol [search, [Wikipedia](https://en.wikipedia.org/wiki/Agentic_commerce)]; MCP Registry preview (8 Sep) [search, [MCP blog](https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/)]; OpenAI and Stripe **Agentic Commerce Protocol** with ChatGPT Instant Checkout (~29 Sep) [search for existence, [Wikipedia](https://en.wikipedia.org/wiki/Agentic_commerce); date TK]; Claude Agent SDK rename (29 Sep) [TK].
- **Oct 2025**: OpenAI AgentKit and Apps SDK, DevDay (6 Oct) [TK]; **Agent Skills** launched in Claude (16 Oct; Claude Code 2.0.22 on 17 Oct) [search, [unite.ai](https://www.unite.ai/anthropic-opens-agent-skills-standard-continuing-its-pattern-of-building-industry-infrastructure/); [ai.miraheze](https://ai.miraheze.org/wiki/Agent_Skills)]; ChatGPT Atlas (21 Oct) [TK]; LangChain/LangGraph 1.0 (22 Oct) [search]; Microsoft Agent Framework public preview [TK].
- **Nov 2025**: MCP spec 2025-11-25 [fetched as the predecessor]; MCP Apps proposal (SEP-1865) [TK].
- **Dec 2025**: **AAIF formed (9 Dec)** with MCP, goose and AGENTS.md [search, [InfoQ](https://infoq.com/news/2025/12/agentic-ai-foundation/)]; **Agent Skills released as an open standard (18 Dec)** at agentskills.io, with a reference SDK and the `skills-ref` validator [search, [unite.ai](https://www.unite.ai/anthropic-opens-agent-skills-standard-continuing-its-pattern-of-building-industry-infrastructure/)].
- **Jan-Mar 2026**: A2A v1.0 (Jan or Mar; conflicting) [search]; Gemini Auto Browse desktop preview (Jan) [search, unverified]; MS Agent Framework RC (19 Feb) [search, [MS devblogs](https://devblogs.microsoft.com/agent-framework/migrate-your-semantic-kernel-and-autogen-projects-to-microsoft-agent-framework-release-candidate/)]; MCP CVE wave [search]; agentskills.io lists 32 adopters (Mar 2026) [search, [agentman](https://agentman.ai/blog/agent-skills-ecosystem-report-2026)].
- **Apr 2026**: MS Agent Framework 1.0 GA (3 Apr) [search]; A2A passes 150 organisations (9 Apr, LF) [search]; CVE-2026-30623 disclosed (15 Apr) [search].
- **May 2026**: A2A v1.0.1 extension mechanism [search, [arXiv](https://arxiv.org/pdf/2606.31498)]; Project Mariner shut down as a standalone product (4 May) [search, unverified].
- **Jun 2026**: Claude Code moves to metered pricing (mid-June) [search, unverified].
- **Jul 2026**: **MCP spec 2026-07-28 (stateless core, MRTR, extensions, Tasks extension, CIMD over DCR)** [fetched]; OpenAI announces Atlas retirement and "ChatGPT Work" (9 Jul) [search, unverified].
- **Aug 2026**: Assistants API sunset date (26 Aug) [search]; **A2A joins the AAIF** (Axios, 17 Aug) [search, [Axios](https://axios.com/2026/08/17/a2a-agentic-ai-foundation-open-ai-standards)].
- **AG-UI** (CopilotKit; launched ~May 2025 [TK]) is an event-based protocol for agent-to-user/app front-end sync, complementing MCP and A2A. Google ADK, LlamaIndex and Microsoft Agent Framework integrate with it. CopilotKit raised $27M ($20M Series A + $7M seed; GeekWire 2026). Company-reported usage figures: 120k weekly installs and 9k+ GitHub stars (late 2025); a claimed 2.3M weekly downloads is unverified. — [CopilotKit](https://www.copilotkit.ai/ag-ui); [GeekWire](https://www.geekwire.com/2026/seattles-copilotkit-raises-27m-as-some-of-the-biggest-names-in-tech-adopt-its-ai-agent-protocol/) [search]
- Agent Skills also brought a new supply-chain risk: malicious skills packages. — [prplbx](https://www.prplbx.com/blog/agent-skills-supply-chain) [search]

### Inferences
- The protocol stack for the book:
  - agent to tool/data: **MCP**
  - agent to agent: **A2A**
  - agent to user/front-end: **AG-UI**, **MCP Apps**
  - agent to commerce/payments: **ACP** (OpenAI/Stripe), **AP2** (Google)
  - agent to procedural knowledge: **Agent Skills**
  - agent to repo instructions: **AGENTS.md**
  - editor to coding agent: **Agent Client Protocol** (Zed)
- Watch out for acronym collisions: "ACP" refers to three different things.

### Gaps
- I could not verify the AG-UI launch date or Agentic Commerce Protocol date from primary sources this session.
- Model-release dates for 2026 (e.g. names like "Opus 4.7/4.8" seen in blogs) were not verified and are out of scope here; do not cite them from these notes.

---

## 5. How do production teams structure multi-agent vs single-agent systems, and what are the reported failure modes?

### Takeaway
The dominant production pattern is a single agent loop with good tools and context management. Teams use **orchestrator plus isolated subagents** (read-mostly, parallelisable work, results summarised back) only when the work is breadth-first and parallelisable, as in research and search. They avoid peer-to-peer "agent societies" for tightly coupled work such as coding. Multi-agent systems cost far more tokens (about 15x chat) and fail often. Coordination and context-loss failures dominate.

### Cited Findings
- **Anthropic multi-agent research system** (Jun 2025): a lead agent (orchestrator) spawns parallel subagents with separate context windows. "Multi-agent systems work mainly because they help spend enough tokens to solve the problem." Agents use about 4x the tokens of chat, and multi-agent systems about 15x. The widely repeated "90.2% improvement over single-agent Opus" figure was on an internal research eval. Limitations: synchronous waves (one slow subagent stalls the rest) and hard evaluation for open-ended tasks. — [theaiengineer substack summary](https://theaiengineer.substack.com/p/how-anthropic-built-multi-agent-deep) [search]; primary: [anthropic.com/engineering/multi-agent-research-system](https://www.anthropic.com/engineering/multi-agent-research-system) [TK]
- **Cognition, "Don't Build Multi-Agents"** (Jun 2025): parallel subagents make independent decisions without shared context, so their outputs conflict. Example: a Flappy Bird clone where one subagent builds a Mario-style background and another a mismatched bird. The core issue is loss of context fidelity at each handoff. Principles: share full context/traces and recognise that "actions carry implicit decisions". — [danorlando.com](https://www.danorlando.com/blog/genai/single-agent-vs-multi-agent); [Medium](https://medium.com/@maureesewilliams/the-agent-architecture-wars-why-two-ai-giants-completely-disagree-on-multi-agent-systems-d19a53364200) [search]; primary: [cognition.ai/blog/dont-build-multi-agents](https://cognition.ai/blog/dont-build-multi-agents) [TK]
- Reconciliation: Anthropic's case is parallelisable research with natural independence boundaries. Cognition's is tightly coupled work needing shared context and coordinated decisions. — [danorlando.com](https://www.danorlando.com/blog/genai/single-agent-vs-multi-agent) [search]
- **MAST taxonomy** (Cemri et al., "Why Do Multi-Agent LLM Systems Fail?", UC Berkeley, NeurIPS 2025): 14 failure modes in 3 categories (specification/system design, inter-agent misalignment, task verification/termination), from 1,642 annotated traces across 7 frameworks. Failure rates were reported at 41-87%. — [dev.to](https://dev.to/tuomo_pisama/do-you-actually-need-a-multi-agent-system-3a3j); [agnt.gg](https://agnt.gg/articles/engineering/single-agent-vs-multi-agent) [search]; primary [arXiv 2503.13657](https://arxiv.org/abs/2503.13657) [TK]
- Model upgrades can fundamentally change multi-agent behaviour, which is a governance and regression risk. — [arXiv 2508.05687](https://arxiv.org/pdf/2508.05687) [search]
- Memory and state loss across agents is a frequently reported production failure ("they forget"). — [Medium](https://sriram-narasim.medium.com/why-multi-agent-systems-fail-in-production-they-forget-bc8105b2e9e6) [search]
- Coding agents in practice: Claude Code uses subagents mainly for context isolation (search/exploration), not for parallel writers. Cursor runs up to 8 parallel agents on the *same* task and judges the best result, which is "voting" parallelisation rather than division of labour. — [turingcollege](https://www.turingcollege.com/blog/best-ai-coding-agents-2026-claude-code-codex-cursor) [search]
- Productivity caution: one 2026 market analysis notes that the only RCT (METR, Jul 2025) found experienced open-source developers were *slower* with AI tools. — [ajayk.sh](https://www.ajayk.sh/blog/coding-agents-market-2026-share-productivity/) [search]; primary [METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) [TK]
- Interop-protocol governance gaps: MCP, A2A and ACP cannot express certain governance constraints (delegation, accountability). — [arXiv 2606.31498](https://arxiv.org/pdf/2606.31498) [search]
- Long-running agent failures (Anthropic harness post, via secondary sources): declaring the job done too early, trying to do everything at once and running out of context, and leaving broken state. Fixes: feature lists and progress files, incremental commits, and end-to-end tests before marking a task done. — [dev.to](https://dev.to/claudiuspapirus/why-ai-agents-fail-long-projects-and-the-anthropic-fix-3029) [search]

### Inferences
- Default architecture to teach: **one agent, one loop, a good ACI (tools), context management (compaction, memory, just-in-time retrieval), plus HITL checkpoints**. Escalate to an orchestrator with subagents only for (a) breadth-first parallel search or research, (b) context isolation, or (c) voting or best-of-N. Each subagent should return a compact summary, and the orchestrator should own all write actions.
- Failure-mode checklist for the book:
  - specification ambiguity
  - context loss at handoffs
  - conflicting parallel decisions
  - premature termination or false "done"
  - infinite loops and runaway cost (about 15x tokens)
  - weak verification
  - prompt injection propagating across agents and tools
  - behaviour drift after model upgrades
- Evaluation must be trajectory-level (traces), not only final-answer checks. This links to observability tooling such as LangSmith, Logfire and OpenAI tracing.

### Gaps
- I found no large-scale, independent 2026 survey on the share of production agent systems that are single-agent vs multi-agent; the evidence is mostly vendor posts and commentary.
- The primary Anthropic and Cognition posts were not re-fetched this session; quotes and figures came via secondary summaries. Verify them before quoting.
- I found no rigorous public data on A2A-based cross-organisation multi-agent deployments in production beyond LF's claim of "enterprise production use".
