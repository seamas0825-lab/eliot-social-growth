# Authenticated AI Research Orchestration

Use this reference only when authenticated AI services can materially improve a social-media research decision. AI output creates leads, hypotheses, clusters, and critiques; it does not become evidence until checked against an original or authoritative source.

## Match capability before service

Select the smallest useful capability set before naming any vendor:

| Capability required | Use when | Minimum verification |
| --- | --- | --- |
| Live social search | Current posts, discourse, creator language, controversy, or visible social signals could change the decision | Confirm platform coverage, recency, direct URLs, and whether inaccessible posts are reconstructed or omitted |
| Deep research | A broad source-backed dossier, policy scan, analogy validation, or market structure is genuinely needed | Confirm research mode, source traceability, completion state, and export/readback path |
| Source discovery | The branch needs primary pages, Reddit threads, reviews, studies, or authoritative leads | Open the cited sources; reject circular or inaccessible citations |
| Authenticated platform access | Public open-web search cannot expose the necessary dynamic page, account, comments, or feature | Confirm account, browser adapter, permissions, and user-handoff path |
| Long-context synthesis | A supplied source packet is too large for efficient manual clustering | Preserve source-to-claim mappings and excluded evidence |
| Multilingual native reasoning | Translation, local vocabulary, or non-English source discovery could change meaning | Preserve original-language excerpts, direct links, and translation-risk notes |
| Adversarial review | A major belief, positioning choice, or causal story needs contradiction and reversal testing | Supply the evidence packet, retrieval limits, and explicit reversal condition |
| Structured extraction | The convergence point needs a ledger, schema, matrix, or normalized case set | Specify exact fields and verify a sample against original sources |

Then select a current adapter. Service mappings are runtime hypotheses, not system facts:

| Current adapter example | Likely useful capabilities | Runtime check, limitation, and fallback |
| --- | --- | --- |
| Grok | Live X search and current discourse | Verify direct X access, date, visible metrics, and post context; fall back to native X inspection or another live-social adapter |
| Perplexity | Source discovery, Reddit leads, source-linked synthesis | Verify requested model/thinking mode and open cited threads directly; fall back to search plus manual source inspection |
| Gemini Deep Research | Deep research and broad source-backed dossiers | Verify Deep Research mode, active account, and completion/export state; fall back to another deep-research adapter or bounded manual branches |
| ChatGPT | Adversarial review, belief audit, prioritization, structured synthesis | Supply evidence rather than relying on recollection; fall back to another reasoning adapter or an explicit manual audit |
| Doubao, DeepSeek, ChatGLM, Qwen, or Kimi | Chinese-language, multilingual, long-context, or structured reasoning branches | Verify the exact current feature and source access; use original-language sources and another adapter when traceability is weak |

For every selected adapter, record `verified date`, `verified capability`, `known limitation`, and `fallback` in run state. Do not ask multiple systems the same generic question. A valid multi-tool plan names the distinct decision or uncertainty owned by every branch.

## Select and operate the browser adapter

1. Read [platform-compatibility.md](platform-compatibility.md) and select the operating-system path before acting.
2. Pass [browser-capability-gate.md](browser-capability-gate.md) before opening a research conversation. Do not rely on documentation, helper registries, a prior run, or a fixed editor selector.
3. On macOS, read and follow the `ego-browser` skill. Create one isolated EGO task space for the research goal and reuse it across rounds so authenticated state is available without disturbing normal browser tabs.
4. On Windows, require Browser Use plus the `eze-is/web-access` skill. Follow their current setup instructions, connect only to the intended Chrome or Edge instance, and verify every meaningful action with fresh page state. Do not imitate EGO helper names when the host exposes different tools.
5. Open only the services selected for the branch. Discover the live visible editor, disposable-write/readback/clear it, then confirm the visible account, model, mode, and research feature before submitting the real prompt.
6. Switch accounts only through an already available account chooser and only when the target account is specified by the user. Never type or expose passwords, recovery codes, one-time codes, API keys, or other secrets.
7. If login, CAPTCHA, 2FA, payment, consent, or a sensitive account choice requires the user, hand browser control to the user and state the exact action needed. Resume only after explicit confirmation.
8. Keep scratch tabs under control. At completion, retain only pages the user explicitly needs to see; otherwise close the agent-owned browser session or task space according to the active browser adapter.

## Use a multi-round conversation protocol

Read [ai-prompt-quality.md](ai-prompt-quality.md) and pass the prompt quality gate before submission. Give each service a compact research brief containing the product, official URLs, verified product facts, decision, audience, market, time window, constraints, known evidence, and assigned branch. Then use these rounds:

1. **Discovery:** Ask the bounded question and request direct source URLs, publication or observation dates, and claim-level confidence.
2. **Interrogation:** Ask which important evidence is missing, what would falsify the initial synthesis, and which findings are observation versus inference.
3. **Contradiction:** Provide contrary evidence or competing explanations and ask the service to reconcile them without averaging away real disagreement.
4. **Extraction:** Request a compact ledger with `claim`, `source URL`, `source type`, `date`, `evidence or inference`, `confidence`, `conflict`, and `decision affected`.

Continue only while another round could change a decision. Do not prolong a conversation merely to accumulate prose.

## Reconcile with primary research

For every material AI-generated lead:

- open the cited original post, comment thread, product page, documentation, study, policy, or authoritative report;
- record the direct URL and observation date;
- capture native context, visible metrics, comment patterns, and relevant limitations;
- reject invented, inaccessible, circular, or irrelevant citations;
- distinguish a single user's view from a repeated pattern;
- label any conclusion that remains inference;
- use the original source in the final deliverable whenever possible.

For Reddit research, sample across relevant communities and thread contexts. Separate original posters from commenters, problem-aware users from buyers, and repeated objections from highly upvoted but isolated anecdotes. Never summarize “Reddit thinks” from one thread.

## Handle long-running research jobs

Apply the parent skill's ten-second anti-blocking rule. Preserve the browser session or task-space ID, conversation URL, current mode, exact prompt, and visible job state; continue independent branches; and poll only at convergence points. Never submit a duplicate Deep Research job while the first remains active.

## Record the branch result

Store this minimum metadata for every AI-assisted branch:

```text
Service/model/mode:
Capability required:
Capability verified date:
Known limitation and fallback:
Account verified:
Browser adapter:
Conversation URL:
Observed date:
Assigned question:
Exact prompt saved:
Decision affected:
Useful source URLs:
Evidence recovered:
Hypotheses only:
Conflicts and gaps:
Included or excluded, with reason:
```

Exclude the branch from evidence if direct sources cannot be recovered. It may remain as a labeled hypothesis for a future experiment.

## Pass the cross-service convergence gate

When two or more AI services were used, fill [../templates/multi-ai-convergence.md](../templates/multi-ai-convergence.md) before strategy selection. Register each branch, map claims to original source URLs, deduplicate shared sources, preserve conflicts, and classify claims as verified consensus, verified divergence, unverified consensus, or single-branch leads. Model agreement without independent verified sources cannot raise a claim above hypothesis status.
