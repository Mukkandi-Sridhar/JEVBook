# Production side of applied AI engineering (late 2026): guardrails & security, evals & observability, fine-tuning, LLMOps

Research note, compiled 2026-10-20. Method caveat: the sandbox's egress proxy blocked direct page fetches (simonwillison.net, hamel.dev, genai.owasp.org and labs.cloudsecurityalliance.org all failed), so most findings below come from web-search result summaries. Many of those are secondary or vendor blogs. Where a claim rests on a single secondary source, it is marked "(single secondary source)". The report writer should treat exact numbers and dates as "reported" unless a primary URL is cited.

## Q1. What are the top security risks for LLM/agent apps now, and the recommended mitigations?

### Takeaway
Prompt injection is still #1 and still unsolved. As agents gain tools, the risk has shifted from "the model says something bad" to "the agent does something bad": Excessive Agency rose to #3 in OWASP's 2026 LLM list, and OWASP added a separate Agentic Top 10 in December 2025. The practical defence is architectural, not a better classifier. Break the "lethal trifecta" (private data + untrusted content + an exfiltration channel), give agents the least privilege they need, sandbox code execution, require human approval for irreversible "write" actions, and layer classifiers (Prompt Guard, Llama Guard, NeMo, Guardrails AI) as defence in depth only.

### Cited Findings

**OWASP Top 10 for LLM Applications, 2026 edition**
- Order: LLM01 Prompt Injection, LLM02 Sensitive Information Disclosure, LLM03 Excessive Agency, LLM04 Supply Chain, LLM05 Data and Model Poisoning, LLM06 Unbounded Consumption, LLM07 Misinformation, LLM08 Hidden Context Exposure, LLM09 Vector and Embedding Weaknesses, LLM10 Improper Output Handling — [Superwise summary](https://superwise.ai/learn/owasp-top-10-for-llm-applications/); [Aembit](https://aembit.io/blog/the-owasp-top-10-for-llm-applications-2026-what-changed-and-why-it-matters/). Some secondary pages word #10 differently, so check the official document at genai.owasp.org.
- Release date conflict: one summary gives 3 August 2026 ([Superwise](https://superwise.ai/learn/owasp-top-10-for-llm-applications/)) and others give 4 August 2026 ([Check Point](https://blog.checkpoint.com/ai-security/reading-the-signals-in-the-owasp-llm-top-10-2026/amp/); [Cycode](https://cycode.com/blog/owasp-top-10-llm-applications/)). Safe wording: "early August 2026".
- Excessive Agency climbed from #6 (2025) to #3, the biggest move on the list. Sources tie the rise to agents taking real actions in production. Its root causes are excessive functionality, excessive permissions and excessive autonomy. The recommended mitigation is "least agency", with human approval for irreversible actions — [Aembit](https://aembit.io/blog/the-owasp-top-10-for-llm-applications-2026-what-changed-and-why-it-matters/); [DeepStrike](https://deepstrike.io/blog/owasp-llm-top-10-vulnerabilities); [HackerDNA](https://hackerdna.com/blog/owasp-llm-top-10).
- "Hidden Context Exposure" (LLM08) replaces the 2025 entry "System Prompt Leakage". It widens the scope to tool schemas, policy logic and other operational material. Guidance: assume hidden context will eventually be discovered, and never put secrets or authorisation logic in prompts — [Forcepoint](https://www.forcepoint.com/blog/insights/owasp-llm-top-10); [Aembit](https://aembit.io/blog/the-owasp-top-10-for-llm-applications-2026-what-changed-and-why-it-matters/).
- Methodology: practitioner votes were reportedly weighted 75% and documented incidents 25%. An arXiv robustness study finds the Excessive Agency move robust against an incident corpus, but says the lower-ranked entries are not statistically separable — [arXiv 2608.19266](https://arxiv.org/pdf/2608.19266); [Check Point](https://blog.checkpoint.com/ai-security/reading-the-signals-in-the-owasp-llm-top-10-2026/amp/).
- The Cloud Security Alliance describes the 2026 list as arriving alongside a new OWASP "agent control" standard. I could not open the page to get the standard's name or contents — [CSA research note](https://labs.cloudsecurityalliance.org/research/csa-research-note-owasp-genai-top10-2026-agent-control-stand/).

**OWASP Top 10 for Agentic Applications (published 9 Dec 2025)**
- ASI01 Agent Goal Hijack; ASI02 Tool Misuse and Exploitation; ASI03 Identity and Privilege Abuse; ASI04 Agentic Supply Chain Vulnerabilities; ASI05 Unexpected Code Execution; ASI06 Memory and Context Poisoning; ASI07 Insecure Inter-Agent Communication; ASI08 Cascading Failures (sometimes written "Cascading Agent Failures"); ASI09 Human-Agent Trust Exploitation; ASI10 Rogue Agents — [Cycode](https://cycode.com/blog/owasp-top-10-agentic-applications/); [DeepTeam docs](https://www.trydeepteam.com/docs/frameworks-owasp-top-10-for-agentic-applications).
- MCP tool poisoning is classed under ASI01 Agent Goal Hijack — [CSA MCP best-practices guide](https://labs.cloudsecurityalliance.org/agentic/agentic-mcp-security-best-practices-v1/).

**Prompt injection and the lethal trifecta (Simon Willison)**
- Willison named the "lethal trifecta" in June 2025. Any agent that combines (1) access to private data, (2) exposure to untrusted content and (3) the ability to communicate externally can be tricked into leaking that data. His position is that the only reliable fix is to remove one of the three legs, and that the exfiltration leg is usually the easiest to cut — [Willison, lethal-trifecta tag](https://feeds.simonwillison.net/tags/lethal-trifecta/); [AI Weekly](https://aiweekly.co/alerts/willison-names-lethal-trifecta-behind-ai-agent-data-leaks). One page dates the term to 2024, but that page is less reliable.
- 2026 vendor responses:
  - OpenAI shipped a ChatGPT "Lockdown Mode" that restricts exfiltration routes. Willison notes that it does not stop injected text from reaching the model, and that its existence suggests the default settings are not robust.
  - Anthropic cited a third-party evaluation in which none of 720 attack attempts succeeded against Claude Code's auto mode. Willison is sceptical and has predicted "a Challenger disaster for coding agent security".
  - Source: [Willison blog tag summaries](https://simonwillison.net/tag/prompt-injection/), seen through search snippets only.
  - An unverified claim that a Claude model is "not prompt injectable anymore" appears on one page. I found no primary source, so do not use it.
- "Design Patterns for Securing LLM Agents against Prompt Injections" (arXiv 2506.08837, June 2025) proposes six patterns: action-selector, plan-then-execute, LLM map-reduce, dual-LLM, code-then-execute (CaMeL-style) and context-minimisation. The common idea is that once an agent has read untrusted input, that input must not be able to trigger consequential actions — [Willison write-up, 13 Jun 2025](https://simonwillison.net/2025/Jun/13/prompt-injection-design-patterns/).
- CaMeL (Google DeepMind, "Defeating Prompt Injections by Design"; published at SaTML 2026) works in three parts:
  - A privileged LLM writes a plan from the trusted user query only.
  - A quarantined LLM with no tool access parses the untrusted data.
  - A custom interpreter tracks data-flow tags (capabilities) and checks policy before every tool call, which blocks exfiltration.
  - Sources: [IEEE CSDL / SaTML 2026](https://www.computer.org/csdl/proceedings-article/satml/2026/785900a587/2jZks3ksGT6); [Atlan explainer](https://atlan.com/know/prompt-injection-attacks-ai-agents/).
- Practitioner consensus: no prompt, classifier or fine-tune reliably stops a determined adaptive attacker. Detection is one layer among several, not the boundary — [DEV, opinion](https://dev.to/indra_gustiprasetya_a80a/prompt-injection-defense-10-tips-that-hold-up-4513). Research continues to test "out-of-band" defences against adaptive attacks — [arXiv 2606.26479](https://arxiv.org/pdf/2606.26479).

**Data exfiltration via tools / MCP**
- How tool poisoning works: the model reads tool descriptions but the user usually does not, and MCP has no structural marker separating instructions from description text — [ITECS](https://itecsonline.com/post/mcp-tool-poisoning-enterprise-ai-agent-security-2026); [CSA research note, Jul 2026](https://labs.cloudsecurityalliance.org/research/csa-research-note-mcp-tool-poisoning-auto-execution-20260701/).
- Reported attack success rates for MCP tool poisoning: an average of 36.5% across models (CSA); MCPTox summaries report above 60%, with a maximum of 72%. These are secondary summaries — [CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-mcp-tool-poisoning-auto-execution-20260701/); [mcpplaygroundonline](https://mcpplaygroundonline.com/blog/mcp-security-tool-poisoning-owasp-top-10-mcp-scan).
- Example incidents:
  - April 2025: a proof of concept used a poisoned "calculator" tool description to exfiltrate an SSH key from Cursor.
  - CVE-2025-6514: a pre-auth RCE affecting MCP tooling.
  - February 2026 ("SANDWORM_MODE"): 19 npm packages installed a rogue MCP server.
  - May 2026: the Shai-Hulud/AntV supply-chain campaign hit 300+ packages.
  - These details come from vendor or blog sources — [CyberDesserts](https://blog.cyberdesserts.com/ai-agent-security-risks/); [Glasp](https://glasp.co/articles/mcp-security-tool-poisoning-supply-chain).
- CoSAI published an MCP security whitepaper in January 2026 covering 12 threat categories and about 40 threats — [ITECS](https://itecsonline.com/post/mcp-tool-poisoning-enterprise-ai-agent-security-2026) (single secondary source).

**Guardrail tools (stack them; they solve different problems)**
- Llama Guard 4: a 12B multimodal safe/unsafe classifier over the MLCommons hazard taxonomy. It merges the earlier 8B text and 11B vision variants and ships under the Llama 4 Community License — [Tech Jacks](https://techjacksolutions.com/ai-tools/meta-llama/mastering-llama-safety-and-guardrails/); [Particula](https://particula.tech/blog/ai-guardrails-compared-nemo-guardrails-ai-llama-guard).
- Prompt Guard 2 (86M and 22M): classifies inputs as benign, injection or jailbreak. It is cheap enough to run on every input and every retrieved chunk — [Tech Jacks](https://techjacksolutions.com/ai-tools/meta-llama/mastering-llama-safety-and-guardrails/).
- LlamaFirewall: Meta's orchestration layer combining Prompt Guard, an alignment/agent-goal checker and CodeShield. One competitor blog lists it as MIT licensed — [ClawMoat](https://clawmoat.com/blog/clawmoat-vs-llamafirewall-nemo-guardrails) (vendor-biased).
- NVIDIA NeMo Guardrails: Apache-2.0 "programmable rails" (input, dialog, retrieval, execution and output) written in the Colang DSL. Best suited to controlling conversation flow — [Particula](https://particula.tech/blog/ai-guardrails-compared-nemo-guardrails-ai-llama-guard); [Infrabase](https://infrabase.ai/blog/llm-guardrails-compared).
- Guardrails AI: open-core (Apache-2.0) validators from the Guardrails Hub that wrap LLM calls. Best suited to validating structured output, PII and format — [Particula](https://particula.tech/blog/ai-guardrails-compared-nemo-guardrails-ai-llama-guard); [DEV comparison](https://dev.to/agdex_ai/best-ai-agent-security-guardrails-tools-in-2026-llm-guard-vs-nemo-vs-guardrails-ai-5e5d).
- Most production systems layer input scanning, safety classification and output validation. Published latency and false-positive figures vary widely and are benchmark-specific, so measure on your own traffic — [General Analysis guide](https://generalanalysis.com/guides/best-ai-guardrails); [Cloudthrill](https://cloudthrill.ca/llm-guardrail-solutions).

**Sandboxing and permissions**
- Common controls: Docker or gVisor sandboxes for code execution, and permission systems that need manual approval for sensitive operations (for example Claude Code's permission prompts) — [MDPI review](https://www.mdpi.com/2078-2489/17/1/54). Academic work also covers browser-agent sandboxing — [ceLLMate, arXiv 2512.12594](https://arxiv.org/pdf/2512.12594).
- Separate read tools from write tools. "Write" tools (payments, configuration changes, patient messaging) carry higher consequences than "read" tools (search) and need stronger gates — [IEEE-USA comment to NIST agentic-AI RFI, 9 Mar 2026](https://ieeeusa.org/assets/public-policy/policy-log/2026/IEEE-USA-NIST-RFI-Agentic-AI-030926.pdf).
- NIST/CAISI: a CAISI presentation lists agent risks such as insecure agent protocols (MCP, A2A, ACP) and memory poisoning — [NIST CSRC slides 2026](https://csrc.nist.gov/csrc/media/presentations/2026/agentic-ai-emerging-threats,-mitigations,-and-cha/1.3-agentic_ai-sotiropoulos.pdf). One summary says a NIST "AI Agent Standards Initiative" launched in February 2026 — [ITECS](https://itecsonline.com/post/mcp-tool-poisoning-enterprise-ai-agent-security-2026) (single secondary source).

**Regulation (brief)**
- EU AI Act: the Digital Omnibus on AI (Regulation (EU) 2026/1744) was published on 24 July 2026 and entered into force on 27 July 2026 — [Orrick, Jul 2026](https://www.orrick.com/en/Insights/2026/07/EU-AI-Act-Update-Digital-Omnibus-Finalizes-8-Compliance-Changes); [AI Act Explorer](https://artificialintelligenceact.eu/ai-act-explorer/digital-omnibus/); [Cooley](https://cdp.cooley.com/digital-ai-omnibus-delays-key-deadlines-introduces-new-rules/). Key dates:
  - Annex III high-risk obligations moved from 2 Aug 2026 to 2 Dec 2027.
  - Annex I (AI in regulated products) moved to 2 Aug 2028.
  - GPAI obligations are unchanged and have applied since 2 Aug 2025.
  - Article 50 transparency obligations applied from 2 Aug 2026 for new systems, with a marking grace period to 2 Dec 2026 for systems already on the market.
  - New bans on AI-generated NCII and CSAM apply from 2 Dec 2026.
  - National sandboxes must be running by 2 Aug 2027.
  - Prohibited practices and AI literacy have applied since 2 Feb 2025. (This is the original Act timeline and is not re-verified here.)
- India:
  - MeitY's AI Governance Guidelines (reported 5 Nov 2025) are principles-based and not legally binding. They rely on existing law rather than a standalone AI Act — [ImpactLab policy radar](https://impactlabglobal.com/policy-radar/instrument/india-ai-governance-guidelines); [AI Policy Tracker](https://aipolicytracker.org/jurisdictions/india).
  - DPDP Rules 2025 were notified on 13 or 14 Nov 2025 (sources differ) and phase in over 18 months:
    - The Data Protection Board and definitions took effect immediately.
    - Consent-manager registration starts around 13 Nov 2026.
    - Substantive obligations (notice, consent, data-principal rights, breach reporting, children's data, SDF duties) apply around 13 or 14 May 2027.
  - Sources: [PIB DPDP Rules PDF](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf); [Veritect](https://veritect.ai/digital-data-ai-law/dpdp-rules-2025-phased-rollout); [Wikipedia](https://en.wikipedia.org/wiki/Digital_Personal_Data_Protection_Rules,_2025).

### Inferences
- For the book, the defensible mental model is: **treat the LLM as an untrusted component, and every token from tools, retrieved documents, emails or web pages as attacker-controlled.** Security comes from the system around the model (capabilities, data-flow control, sandboxing, approvals and egress limits), not from the model itself.
- A practical checklist that follows from these sources:
  - Draw a trifecta map for each agent.
  - Cut the exfiltration channel first: no arbitrary URL fetch or image rendering, and an allowlist for egress.
  - Scope credentials per task (short-lived, least privilege).
  - Require human approval for write or irreversible tools.
  - Run code in an isolated sandbox with no network by default.
  - Pin and review MCP servers and tool descriptions, as you would any supply-chain dependency.
  - Strip or tokenise PII before calls and before logging.
  - Run injection and jailbreak classifiers on inputs and retrieved chunks as a tripwire, not a wall.
  - Validate structured outputs before acting on them.
- PII handling: DPDP Act consent and purpose limitation, together with OWASP LLM02, imply redacting PII before it enters prompts, logs and traces, and adding output filters. Observability tools that capture prompt content create a second copy of personal data that needs governing (OpenTelemetry GenAI content capture is opt-in for this reason; see Q2).

### Gaps
- Could not open the official OWASP 2026 LLM Top 10 document or the CSA note on the new "agent control standard". The standard's name and contents are unknown.
- No primary text for Llama Guard 4 / Prompt Guard 2 model cards. Sizes come from secondary blogs.
- No primary source found for OpenAI Lockdown Mode's launch date or Anthropic's 720-attempt evaluation. Both are known only through Willison snippets.
- NIST AI 600-1 (GenAI Profile, July 2024) was not returned in searches. Its existence and date come from my background knowledge and are not verified here.
- Provider moderation endpoints (OpenAI omni-moderation, Google/Azure content safety) were not researched for 2026 changes.

## Q2. Which evaluation practices do respected practitioners recommend, and what pitfalls do they warn about?

### Takeaway
The consensus, led by Hamel Husain and Shreya Shankar, is error analysis first:
- Read real traces.
- Open-code the failures, then group them into a taxonomy (axial coding).
- Write cheap code-based checks for each failure mode.
- Use LLM judges only for subjective modes, with binary pass/fail labels, after validating the judge against human labels.

For agents, score the trajectory and the final state, not just the final answer. Generic off-the-shelf metrics and leaderboard benchmarks are weak proxies for product quality.

### Cited Findings
- Hamel Husain's LLM-as-judge method ("critique shadowing"):
  1. Find one domain expert.
  2. Have them make pass/fail judgments with written critiques.
  3. Build the judge prompt from those critiques as few-shot examples.
  4. Run error analysis: compute error rates across dimensions and find root causes.
  - Source: [AI News summary of Hamel's post](https://buttondown.com/ainews/archive/ainews-creating-a-llm-as-a-judge).
- Husain and Shankar teach error analysis as the "foundational first step" and the "best ROI" activity for AI engineers. Shankar's research ("Who Validates the Validators?", EvalGen) is about aligning LLM evaluators with human preferences, and about "criteria drift": people refine their criteria as they grade — [Maven lightning lesson](https://maven.com/p/0c0359/error-analysis-the-ai-engineer-s-best-roi).
- Their FAQ stresses product evals over base-model benchmarks — [aggregator summary of Hamel's evals FAQ](https://marketnews.xskill.com/a/7293?m=en). The primary FAQ at hamel.dev/blog/posts/evals-faq could not be fetched.
- Start from real traffic, especially failures. Collect 50–200 real cases and tag them by slice, because an average score can hide a feature that is broken for one segment. Build an error taxonomy from observed failures so evals measure "real risk, not imagined problems". Prefer binary labels over 1–5 scales because they reduce ambiguity and speed up annotation — [DEV: evals that catch regressions](https://dev.to/anukumar/llm-evaluation-evals-that-catch-regressions-and-when-to-trust-llm-as-a-judge-1mmn); [Latitude](https://latitude.so/blog/llm-agents-evaluate-practical-error-analysis).
- Code before judges. Check schema validity, correct tool and arguments, and that citations match retrieved documents. These checks are "fast, free and give the same result every run" — [DEV](https://dev.to/anukumar/llm-evaluation-evals-that-catch-regressions-and-when-to-trust-llm-as-a-judge-1mmn).
- LLM-as-judge pitfalls:
  - Position bias, verbosity bias and self-enhancement bias (a judge favouring its own model family).
  - Mitigations: specific rubrics, pass/fail or 3-point scales, hand-grading 50–100 cases, and measuring the judge's agreement with those labels.
  - Source: [DEV](https://dev.to/anukumar/llm-evaluation-evals-that-catch-regressions-and-when-to-trust-llm-as-a-judge-1mmn).
  - A 2026 mechanistic-interpretability paper studies where judge bias comes from — [arXiv 2607.11871](https://arxiv.org/pdf/2607.11871).
- Agent judges can be fooled by the agent's own narrative. In AgentRewardBench, a judge marked a VisualWebArena "buy cereal" task as successful when the agent had only added the item to the cart — [AgentRewardBench, arXiv 2504.08942](https://arxiv.org/pdf/2504.08942). A meta-evaluation dataset for agentic judges is also out — [Counsel, arXiv 2606.21627](https://arxiv.org/pdf/2606.21627).
- Trajectory evals:
  - An agent can reach the right answer and still fail trajectory evaluation through unnecessary tools, wrong parameters, repeated steps or convoluted paths.
  - Trajectory checks matter most when order matters, for example "verify identity before refund", where the final output looks the same either way.
  - Evaluate at three levels: end-to-end, trajectory and component (which retriever, tool or sub-agent broke).
  - Sources: [LangChain resource](https://www.langchain.com/resources/llm-evaluation-framework); [Confident AI](https://www.confident-ai.com/blog/llm-agent-evaluation-complete-guide).
- A limitation of trajectory-only judging: it cannot verify whether database state actually changed, so silent failures slip through. Check final environment state as well — [arXiv 2603.15483](https://arxiv.org/pdf/2603.15483). "Corrupt success" (right outcome, procedure-violating path) is a documented failure class — [arXiv 2603.03116](https://arxiv.org/pdf/2603.03116).
- Evaluation platforms are now expected to score whole agent runs: tool selection, arguments, path, error recovery, multi-turn behaviour and task success — [Atlan Braintrust alternatives](https://atlan.com/know/ai-agent/ai-agent-evals/braintrust-alternatives/).

**Tools (status as of 2026)**
- Langfuse: ClickHouse announced its acquisition of Langfuse on 16 Jan 2026, alongside a $400M Series D at a $15B valuation. Langfuse stays MIT-licensed and self-hostable, and a March 2026 data-model redesign leaned further into ClickHouse — [SiliconANGLE](https://siliconangle.com/2026/01/16/database-maker-clickhouse-raises-400m-acquires-ai-observability-startup-langfuse/); [InfoWorld](https://www.infoworld.com/article/4118621/clickhouse-buys-langfuse-as-data-platforms-race-to-own-the-ai-feedback-loop.html); [Orrick](https://www.orrick.com/en/News/2026/01/Open-source-LLM-Observability-Langfuse-Acquired-by-ClickHouse-Inc); [OpenObserve](https://openobserve.ai/blog/langfuse-vs-langsmith/).
- Positioning per Arize's own comparison (updated 13 Aug 2026; vendor-biased):
  - Arize AX: enterprise, with agent evals tied to production observability.
  - Arize Phoenix: open-source and self-hosted.
  - LangSmith: best fit for LangChain/LangGraph shops.
  - W&B Weave: best fit for teams already on W&B.
  - Also covered: Braintrust, Langfuse and Comet Opik.
  - Source: [Arize](https://arize.com/resources/llm-and-agent-evaluation-platforms/).
- Pricing models differ: Braintrust bills per score and LangSmith bills per trace. Entry prices quoted are LangSmith Plus at $39/seat and Braintrust Pro at $249/month — [Atlan](https://atlan.com/know/ai-agent/ai-agent-evals/braintrust-alternatives/); [MojoAuth](https://mojoauth.com/blog/top-9-ai-eval-observability-platforms). One source reports Braintrust confirmed an AWS breach exposing customer API keys in May 2026 (single secondary source; verify before use).
- OpenTelemetry GenAI semantic conventions:
  - Still "Development" (not stable) status. The GenAI conventions moved to a dedicated repository in June 2026, and there was no official release as of 21 Aug 2026 — [TrueFoundry, 22 Aug 2026](https://www.truefoundry.com/blog/opentelemetry-genai-semantic-conventions); [Greptime, 9 May 2026](https://greptime.com/blogs/2026-05-09-opentelemetry-genai-semantic-conventions). A June 2026 article claiming stabilisation looks AI-generated and conflicts with both — [Business Tech Navigator](https://businesstechnavigator.com/news/opentelemetry-genai-semantic-conventions-agents-2026).
  - Agent spans: create_agent, and invoke_agent split into CLIENT (remote agent) and INTERNAL (in-process) span kinds (semconv v1.38 to v1.41 per Greptime), plus execute_tool spans.
  - Content capture (prompts and completions) is opt-in, gated via OTEL_SEMCONV_STABILITY_OPT_IN and content-capture settings.
  - Sources: [Greptime](https://greptime.com/blogs/2026-05-09-opentelemetry-genai-semantic-conventions); [TraeAI learning guide](https://learn.traeai.com/t/ai-engineering/phases/14-agent-engineering/23-otel-genai-conventions.html).

### Inferences
- The recommended workflow for the book (eval-driven development):
  1. Instrument tracing from day one, OTel-compatible.
  2. Read 50–100+ traces and open-code the failures.
  3. Group failures into a taxonomy (axial coding) and count them.
  4. Fix the obvious prompt or spec bugs straight away, without building evals for them.
  5. Write assertions for each remaining failure mode: code checks first, then judges validated against expert labels (report TPR/TNR, not just accuracy).
  6. Freeze a golden set drawn from real and synthetic cases.
  7. Run it in CI on every prompt or model change.
  8. Sample production traffic for online scoring.
  9. Loop back to step 2.
- Benchmarks (MMLU, SWE-bench and similar) help with model shortlisting. Product evals decide shipping.
- Pick an observability tool by deployment constraint (self-host versus SaaS, data residency), framework fit and billing model, rather than by feature list. OTel GenAI conventions reduce lock-in, but their attribute names may still change.

### Gaps
- Could not access the primary Hamel/Shankar evals FAQ or Eugene Yan's posts, so specific numbers (for example "spend 60–80% of time on error analysis") are not verified here and are omitted.
- Did not find 2026 release or funding news for Braintrust, LangSmith, Phoenix or Weave beyond comparison pieces.
- No source found on golden-dataset sizing beyond the "50–200 real cases" heuristic.

## Q3. When does fine-tuning make sense in 2026, and what are the cheapest effective methods?

### Takeaway
Fine-tune last: after prompting, few-shot examples and RAG have stopped improving your evals. Fine-tuning changes behaviour (format, tone, a narrow skill, latency and cost through a smaller model), not knowledge, so freshly changing facts belong in RAG. The cheapest effective path is LoRA or QLoRA SFT on an open-weight model (Unsloth, Axolotl, TRL/PEFT, or the managed Tinker API). Distillation turns frontier-model outputs into a small, cheap model. RL fine-tuning (GRPO and variants) is worth it only when you have a verifiable reward. Watch provider fine-tuning APIs closely: OpenAI's docs now say its fine-tuning platform is closed to new users.

### Cited Findings
- Decision rules:
  - Fine-tune only when prompts and RAG plateau on your evals.
  - Fine-tuning locks in consistent format, tone or skill, while RAG handles changing or proprietary knowledge.
  - "Fine-tuning changes behaviour, not knowledge."
  - Sources: [FutureAGI guide](https://futureagi.com/blog/llm-fine-tuning-guide-2025/); [MyEngineeringPath](https://myengineeringpath.dev/genai-engineer/fine-tuning/); [Medium/techlatest](https://medium.com/@techlatest.net/when-to-fine-tune-an-llm-and-when-prompting-is-enough-c32d53261ac7); [AI Dev Day India, Jun 2026](https://aidevdayindia.org/blogs/fine-tuning-llms-lora-qlora/fine-tuning-llms-lora-qlora.html).
- LoRA versus QLoRA:
  - QLoRA (4-bit base model plus LoRA adapters) is the default for single-GPU fine-tuning of large open-weight models.
  - Use 16-bit LoRA when VRAM allows, so quantisation is ruled out as a suspect when debugging.
  - Plain LoRA is preferred on multi-GPU setups.
  - Common stacks: Unsloth, TRL, Axolotl and Hugging Face PEFT.
  - Sources: [Effloow](https://effloow.com/articles/llm-fine-tuning-lora-qlora-guide-2026); [DevStarsJ, Mar 2026](https://devstarsj.github.io/ai/2026/03/29/llm-fine-tuning-lora-qlora-practical-guide-2026/); [FutureAGI](https://futureagi.com/blog/fine-tuning-llms-unlocking-peak-performance/).
- Staged post-training recipe:
  1. SFT on a tight output contract.
  2. Preference tuning (DPO, ORPO or KTO) if you have preference pairs.
  3. GRPO or DAPO on verifiable tasks.
  - Skip any stage you lack data for. GRPO or RLHF is worthwhile "only if you have a real reward signal (verifier or preferences)".
  - Source: [FutureAGI techniques](https://futureagi.com/blog/llm-fine-tuning-techniques-i-ii/).
- Tinker (Thinking Machines Lab), launched 1 Oct 2025:
  - A managed training API on Thinking Machines' clusters.
  - Low-level primitives (forward_backward, optim_step, sample) let you write custom SFT, RL and preference loops.
  - LoRA only, not full fine-tuning. Thinking Machines argues LoRA matches full fine-tuning in many cases, especially RL.
  - Supports open-weight models from 1B to 1T+ parameters, dense and MoE (for example Qwen3-8B at rank 16).
  - The open-source tinker-cookbook covers RL and preference recipes.
  - Sources: [Thinking Machines announcement](https://thinkingmachines.ai/news/announcing-tinker/); [Tinker docs](https://tinker-docs.thinkingmachines.ai/tinker/); [InfoQ](https://www.infoq.com/news/2025/10/thinking-machines-tinker/); [tinker-cookbook](https://github.com/thinking-machines-lab/tinker-cookbook).
- OpenAI reinforcement fine-tuning (RFT):
  - Trains reasoning models (example: o4-mini-2025-04-16) against programmable graders rather than fixed answers. Multiple graders can be combined.
  - **OpenAI's current RFT guide reportedly says the fine-tuning platform is being wound down: it is no longer accessible to new users, existing users can create jobs "for the coming months", and fine-tuned models stay available for inference until their base models are deprecated.**
  - Sources: [OpenAI RFT guide](https://developers.openai.com/api/docs/guides/reinforcement-fine-tuning) (seen via search snippet, not fetched); [The Decoder, 2025](https://the-decoder.com/openai-adds-new-fine-tuning-options-for-o4-mini-and-gpt-4-1/); [Maginative](https://www.maginative.com/article/openai-introduces-reinforcement-fine-tuning-to-build-domain-specific-expert-ai-models/).
  - One third-party guide says RFT reached GA on o4-mini in October 2025, with GPT-5 in private beta — [youngju.dev](https://www.youngju.dev/transcribe/ai-platform/2026-04-12-openai-rft-custom-graders-guide) (unverified).
  - Azure OpenAI also offers RFT — [Microsoft Learn](https://learn.microsoft.com/ja-jp/azure/ai-services/openai/how-to/reinforcement-fine-tuning).
- Supervised fine-tuning on OpenAI (2025) was positioned for style adaptation (including GPT-4.1 nano), and RFT for targeted task optimisation — [The Decoder](https://the-decoder.com/openai-adds-new-fine-tuning-options-for-o4-mini-and-gpt-4-1/).

### Inferences
- Cheapest effective ladder for the book:
  1. Prompt plus few-shot examples plus RAG.
  2. Distil: generate labelled outputs with a frontier model on real inputs, filter them with your evals, then run LoRA SFT on a small open model (via Unsloth on a single GPU, or Tinker / a hosted service).
  3. Add DPO if you have preference pairs.
  4. Add GRPO/RFT only for tasks with automatic verifiers (code tests, math, schema or extraction correctness).
- Your eval suite is the prerequisite: you cannot fine-tune responsibly without a held-out golden set.
- The OpenAI platform wind-down (if confirmed) pushes teams towards open-weight fine-tuning (Tinker, Together, Fireworks, cloud Vertex/Bedrock) and towards prompt-level adaptation for closed models. The book should state this cautiously and date it.

### Gaps
- Could not verify the exact date or wording of OpenAI's fine-tuning wind-down notice, or whether DPO/SFT are also affected. Also unverified: Anthropic (Bedrock Haiku fine-tuning) and Google (Vertex Gemini tuning) fine-tuning status in 2026.
- No 2026 cost-per-run figures found for Unsloth, Axolotl or Tinker.
- No authoritative 2026 source on distillation specifically (for example provider "stored completions to distillation" features). That point rests on general practice, not a cited source.

## Q4. Which cost and latency techniques give the biggest wins in production?

### Takeaway
The biggest, most reliable wins are:
1. **Prompt caching**: put stable prefixes first. Cached reads cost about 10% of the input price on Anthropic, and caching cuts time-to-first-token.
2. **Batch APIs**: about 50% off for latency-tolerant work, and the discount stacks with caching.
3. **Model routing / cascades**: send easy traffic to small models.
4. **Output-token discipline**: shorter outputs, lower reasoning-effort settings, and structured outputs.

Semantic caching helps only narrow FAQ-style workloads, with care. A gateway (LiteLLM, Portkey, Kong, Bifrost and others) centralises routing, fallbacks, rate limits, budgets and caching.

### Cited Findings
- Anthropic prompt caching: cache reads cost about 0.1x the base input rate and cache writes about 1.25x (5-minute TTL), so caching breaks even after roughly two reads. OpenAI's caching is automatic. Sources disagree on OpenAI's discount (50% versus 90%, varying by model); one example lists $0.25/M cached against $2.50/M base — [DevToolLab](https://devtoollab.com/blog/prompt-caching-guide); [Techsy](https://techsy.io/en/blog/reduce-llm-api-costs-guide). Verify against the provider pricing pages.
- Batch APIs give about a 50% discount, and stacking batch with caching can reach roughly 95% savings on the repeated portion — [JobsByCulture](https://jobsbyculture.com/blog/llm-cost-optimization-guide-2026); [LLM Academy](https://llm-academy.dev/gateway/cost-optimization/).
- Model routing reportedly saves 40–70% on mixed workloads. RouteLLM's self-reported result is 85% cost reduction while keeping 95% of quality — [Kalvium Labs](https://www.kalviumlabs.ai/blog/model-cost-optimization-cutting-llm-bills/); [baeseokjae](https://baeseokjae.github.io/posts/llm-cost-reduction-strategies-2026/).
- Semantic caching shows about 25–35% hit rates on chatbot workloads. The risk is that similar prompts can need different answers, so use high similarity thresholds and treat the cache as probabilistic with a fallback — [KunalGanglani](https://www.kunalganglani.com/blog/reduce-llm-api-costs-production); [DEV: gateways](https://dev.to/nazar-boyko/llm-gateways-routing-fallbacks-and-semantic-caching-1n2b).
- Stacking 5–6 levers is claimed to cut bills by about 70%. These are marketing-grade estimates, so measure your own — [LLM Academy](https://llm-academy.dev/gateway/cost-optimization/); [AgentsCodex, Mar 2026](https://agentscodex.com/posts/2026-03-05-cutting-llm-agent-costs-by-50-a-production-engineers-playbook/).
- Gateways: LiteLLM is the most cited open-source, self-hosted gateway, and Portkey and Helicone are the main managed options. Kong AI Gateway and Bifrost also appear. Bifrost supports vLLM, SGLang and Ollama providers natively, with weighted balancing and fallback from self-hosted models to cloud — [Spheron](https://www.spheron.network/blog/ai-gateway-litellm-portkey-kong-gpu-cloud/); [Maxim](https://www.getmaxim.ai/articles/top-4-llm-gateways-for-self-hosted-models-vllm-sglang-and-ollama-2026/) (Maxim sells Bifrost).
- Fallbacks:
  - Trigger fallback chains on HTTP 429, 500 and 503 errors and on timeouts.
  - Keep retries (same provider, with backoff) separate from fallbacks (a different provider or model).
  - Self-hosted vLLM clusters have fixed concurrency. Without overflow to cloud, p99 latency can reach tens of seconds under spikes.
  - Sources: [Digital Applied](https://www.digitalapplied.com/blog/llm-gateway-architecture-2026-engineering-reference); [DEV](https://dev.to/kuldeep_paul/top-5-ai-gateways-for-routing-between-vllm-ollama-and-cloud-llms-2026-1i68).
- Rate limits and budgets: per-team virtual keys and RPM caps (for example 100 RPM for one team) on a shared backend pool — [Spheron](https://www.spheron.network/blog/ai-gateway-litellm-portkey-kong-gpu-cloud/).
- Versioning: pin inference-stack versions explicitly. sglang and sglang-router are versioned separately, and vLLM 0.28.0 reportedly moved bitsandbytes to an out-of-tree plugin, a breaking change — [MarkAICode](https://markaicode.com/integrate/sglang-with-vllm/) (single source).

### Inferences
- Order of operations for the book:
  1. Measure first: tokens in and out per feature, cache hit rate, p50/p95 latency and TTFT.
  2. Restructure prompts for caching: static system prompt, tools and documents first; dynamic user content last.
  3. Move offline jobs (evals, enrichment, backfills) to batch.
  4. Route or cascade by difficulty, and fine-tune or distil a small model for high-volume narrow tasks (see Q3).
  5. Cap output length and reasoning effort.
  6. Add semantic caching only where answers are truly reusable.
- Reliability patterns:
  - Pin dated model snapshots, not floating aliases, and re-run the golden set before switching.
  - Use a gateway for fallback chains, budgets and keys.
  - Use circuit breakers on 429/5xx errors.
  - Use idempotency for agent tool calls when retrying.
- Drift monitoring for LLM apps means tracking input distribution (topics and languages), online eval scores, judge pass rates, refusal rates, cost and latency over time, plus silent provider model updates when using aliases.

### Gaps
- No primary-source 2026 pricing tables (Anthropic, OpenAI, Gemini caching and batch rates). Numbers above come from blogs. The claude-api skill or provider pricing pages should be used to confirm.
- Found nothing authoritative on hosted-API snapshot pinning or deprecation policy for 2026, or on LLM drift-monitoring practice. The guidance above is inference.
- No data on latency techniques such as speculative decoding or prefix caching in vLLM/SGLang beyond gateway coverage.

## Q5. Which new tools and standards emerged in 2025–2026 (with dates)?

### Takeaway
Agent security frameworks dominated the period:
- The OWASP Agentic Top 10 (December 2025) and the OWASP LLM Top 10 2026 (August 2026).
- Formal MCP threat models (CoSAI, January 2026; CSA, 2026).
- CaMeL and the agent design-pattern work (2025).

On the tooling side, consolidation and standardisation continued: ClickHouse bought Langfuse (January 2026), and the OpenTelemetry GenAI conventions keep evolving but remain unstable. Fine-tuning moved towards managed LoRA/RL APIs (Tinker, October 2025), while OpenAI's own fine-tuning platform is being wound down. On regulation, the EU Digital Omnibus (July 2026) delayed high-risk obligations, and India issued principles-based AI guidelines plus phased DPDP Rules (November 2025).

### Cited Findings
- Jun 2025: "Design Patterns for Securing LLM Agents against Prompt Injections" (arXiv 2506.08837) — [Willison](https://simonwillison.net/2025/Jun/13/prompt-injection-design-patterns/). Mid-June 2025: Willison coins the "lethal trifecta" — [AI Weekly](https://aiweekly.co/alerts/willison-names-lethal-trifecta-behind-ai-agent-data-leaks).
- 2 Aug 2025: EU AI Act GPAI obligations apply (unchanged by the Omnibus) — [Cooley](https://cdp.cooley.com/digital-ai-omnibus-delays-key-deadlines-introduces-new-rules/).
- 1 Oct 2025: Tinker launched — [Thinking Machines](https://thinkingmachines.ai/news/announcing-tinker/).
- 5 Nov 2025: India AI Governance Guidelines — [ImpactLab](https://impactlabglobal.com/policy-radar/instrument/india-ai-governance-guidelines). 13/14 Nov 2025: DPDP Rules notified — [PIB](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf).
- 9 Dec 2025: OWASP Top 10 for Agentic Applications — [Cycode](https://cycode.com/blog/owasp-top-10-agentic-applications/).
- Jan 2026: CoSAI MCP security whitepaper — [ITECS](https://itecsonline.com/post/mcp-tool-poisoning-enterprise-ai-agent-security-2026). 16 Jan 2026: ClickHouse acquires Langfuse — [SiliconANGLE](https://siliconangle.com/2026/01/16/database-maker-clickhouse-raises-400m-acquires-ai-observability-startup-langfuse/).
- Feb 2026: NIST AI Agent Standards Initiative reported — [ITECS](https://itecsonline.com/post/mcp-tool-poisoning-enterprise-ai-agent-security-2026) (single secondary source). Mar 2026: NIST agentic-AI RFI comments, for example IEEE-USA — [IEEE-USA](https://ieeeusa.org/assets/public-policy/policy-log/2026/IEEE-USA-NIST-RFI-Agentic-AI-030926.pdf).
- Jun 2026: OTel GenAI conventions move to a dedicated repository, still in Development — [TrueFoundry](https://www.truefoundry.com/blog/opentelemetry-genai-semantic-conventions).
- 24/27 Jul 2026: EU Digital Omnibus on AI published and in force — [Orrick](https://www.orrick.com/en/Insights/2026/07/EU-AI-Act-Update-Digital-Omnibus-Finalizes-8-Compliance-Changes).
- Early Aug 2026 (3rd or 4th): OWASP Top 10 for LLM Applications 2026 — [Check Point](https://blog.checkpoint.com/ai-security/reading-the-signals-in-the-owasp-llm-top-10-2026/amp/); [Superwise](https://superwise.ai/learn/owasp-top-10-for-llm-applications/).
- 2026 (date unverified): OpenAI ChatGPT Lockdown Mode — [Willison](https://feeds.simonwillison.net/tags/lethal-trifecta/). OpenAI fine-tuning platform closed to new users (date unverified) — [OpenAI RFT guide](https://developers.openai.com/api/docs/guides/reinforcement-fine-tuning).
- Upcoming dates:
  - 13 Nov 2026: DPDP consent managers.
  - 2 Dec 2026: EU marking grace period ends and new bans apply.
  - 13/14 May 2027: DPDP substantive obligations.
  - 2 Dec 2027: EU Annex III high-risk obligations.
  - 2 Aug 2028: EU Annex I.
  - Sources: [Veritect](https://veritect.ai/digital-data-ai-law/dpdp-rules-2025-phased-rollout); [AI Act Explorer](https://artificialintelligenceact.eu/ai-act-explorer/digital-omnibus/).

### Inferences
- The field's centre of gravity moved from content safety (toxic outputs) to agent action safety (tools, identity, supply chain, MCP). The book's security chapter should be organised around agent capabilities, not around jailbreak prompts.
- Observability is converging on OTel-based traces, with eval platforms layered on top. Vendor consolidation (ClickHouse/Langfuse) suggests the book should teach concepts and OTel portability rather than one vendor's UI.

### Gaps
- Exact launch dates for Llama Guard 4 / Prompt Guard 2 / LlamaFirewall (believed to be around April–May 2025 with Llama 4, but not verified here), NeMo Guardrails releases, and OWASP's new "agent control standard".
- No verified 2026 dates for new provider features (Anthropic/OpenAI/Google caching TTL changes, new batch tiers, model-router products).
