# Authenticated AI Research Orchestration

Use this reference only when authenticated AI services can materially improve a social-media research decision. AI output creates leads, hypotheses, clusters, and critiques; it does not become evidence until checked against an original or authoritative source.

## Choose tools by branch

Select the smallest useful set. These are default roles, not permanent claims about model quality; reassign a branch when current features or access make another service better.

| Service | Default research role | Required operating note |
| --- | --- | --- |
| Perplexity | Discover current sources, locate Reddit threads and objections, assemble source-linked leads | When available, select Kimi K3 and enable thinking mode. If unavailable, record the actual model/mode used. Open and inspect material Reddit threads and cited pages directly. |
| Gemini | Run a broad Deep Research branch for market structure, competitors, policy, and long-form source synthesis | Select Deep Research when the branch needs it. Confirm that the active Google account matches the account specified by the user; switch only if that account is already available in the account chooser. If authentication, 2FA, or credentials are required, hand control to the user. |
| Grok | Surface current X conversations, creator patterns, vocabulary, controversy, and fast-moving hypotheses | Verify important findings against the original X posts, accounts, dates, comments, and visible metrics. |
| ChatGPT | Cluster evidence, pressure-test positioning, generate counter-hypotheses, and audit contradictions | Supply a bounded evidence packet. Do not use its unsourced recollection as a market fact. |
| Doubao | Explore China-market language, creator framing, domestic audience questions, and culturally native content hypotheses | Use for China-facing branches; validate platform and market claims against native sources. |
| DeepSeek | Decompose strategic or technical questions, compare hypotheses, and challenge causal reasoning | Ask for explicit assumptions and disconfirming evidence; verify every external claim. |
| ChatGLM | Analyze Chinese-language material, long-form context, and domestic-market hypotheses | Preserve native terminology and check cited or quoted material at its source. |
| Qwen | Support Chinese/multilingual synthesis, platform translation, and structured comparison | Use original-language sources when meaning could shift in translation. |
| Kimi | Read long source packets and synthesize Chinese-language research trails | Ask it to retain source-to-claim mappings and inspect those sources directly. |

Do not ask multiple systems the same generic question. A valid multi-tool plan names the distinct decision or uncertainty owned by every branch.

## Operate through EGO

1. Read and follow the `ego-browser` skill.
2. Create one isolated EGO task space for the research goal and reuse it across rounds so the user's authenticated state is available without disturbing normal browser tabs.
3. Open only the services selected for the branch. Inspect the page state before acting and confirm the visible account, model, mode, and research feature.
4. Switch accounts only through an already available account chooser and only when the target account is specified by the user or this reference. Never type or expose passwords, recovery codes, one-time codes, API keys, or other secrets.
5. If login, CAPTCHA, 2FA, payment, consent, or a sensitive account choice requires the user, hand off the task space and state the exact action needed. Resume only after explicit confirmation.
6. Keep scratch tabs under control. At completion, retain only pages the user explicitly needs to see; otherwise complete and close the task space according to the EGO skill.

## Use a multi-round conversation protocol

Give each service a compact research brief containing the product, decision, audience, market, time window, constraints, known evidence, and assigned branch. Then use these rounds:

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

Apply the parent skill's ten-second anti-blocking rule. Preserve the task-space ID, conversation URL, current mode, and visible job state; continue independent branches; and poll only at convergence points. Never submit a duplicate Deep Research job while the first remains active.

## Record the branch result

Store this minimum metadata for every AI-assisted branch:

```text
Service/model/mode:
Account verified:
Conversation URL:
Observed date:
Assigned question:
Decision affected:
Useful source URLs:
Evidence recovered:
Hypotheses only:
Conflicts and gaps:
Included or excluded, with reason:
```

Exclude the branch from evidence if direct sources cannot be recovered. It may remain as a labeled hypothesis for a future experiment.
