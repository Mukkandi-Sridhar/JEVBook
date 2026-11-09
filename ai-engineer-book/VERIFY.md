# Check before print

Claims and sources in the draft that must be checked against a primary source before printing.

| Where | What to check |
|---|---|
| Ch 1, references | Exact titles and dates of the Nakrani and Alian Software posts (titles taken from their URLs). |
| Ch 1 | Shawn Wang's wording on where the ML engineer's work stops and the AI engineer's starts. |
| Ch 5 | How many more tokens Indian scripts need on current tokenisers; find a primary study or measure and cite. |
| Module 12.4 | Replit incident (Fortune, 23 Jul 2025): record counts, the agent's "panicked" and rollback statements, the fixes Replit announced (dev/prod separation, planning-only mode). Sources differ on counts and on whether the rollback claim was false. |
| Module 12.3 | Nasr et al. 2025: 12 defences, most above 90% attack success, 500-person human competition broke all; authors' affiliations (OpenAI, Anthropic, Google DeepMind). |
| Module 12.3 | Meta's Agents Rule of Two wording ("human-in-the-loop approval or another reliable means of validation"). |
| Module 12.2 | Presidio's Aadhaar recogniser uses pattern, Verhoeff checksum and context words; check against the presidio-analyzer source. |
| Module 12.7 | DPDP Rules 2025: Rule 6 one-year log retention, Rule 7 breach report within 72 hours, both from 13 May 2027; check the Gazette text. |
| Module 12.9 | EU AI Act Article 50(1) disclosure duty for chatbots, and whether its start date (2 Aug 2026) was changed by the Digital Omnibus. |
| Module 13.4 | MCP 2026-07-28: `input_required` results (multi round-trip requests) and the tasks extension, against the published specification. |
| Module 13.1, 13.9 | Dates: MCP to the Agentic AI Foundation (Dec 2025); A2A to the Linux Foundation (June 2025) and v1.0 (2026); AP2 and ACP (Sept 2025); NPCI-Razorpay-OpenAI pilot (Oct 2025). |
| Module 13.8 | postmark-mcp: version 1.0.16, about 1,500 weekly downloads (Koi Security). |
| Module 14.7 | Anthropic multi-agent post: 90.2% over single agent on internal eval; about 4x (agent) and 15x (multi-agent) tokens of a chat. Cognition's example of two subagents clashing. |
| Module 14.6 | Anthropic long-running harness: JSON feature list with a passes field, progress file, reason for JSON over Markdown. |
| All | Every `[[VERIFY]]` marker (shown only in draft builds: `BOOK_DRAFT=1 quarto render`). |
