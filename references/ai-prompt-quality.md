# AI Prompt Quality

Use this reference before submitting any prompt to a web AI service. Compile prompts for the assigned research decision and the service's distinct role; do not paste the same generic request into several systems.

## Contents

- [Submission gate](#submission-gate)
- [Prompt packet](#prompt-packet)
- [Grok template](#grok-template)
- [Perplexity template](#perplexity-template)
- [Gemini Deep Research template](#gemini-deep-research-template)
- [ChatGPT templates](#chatgpt-templates)
- [Belief audit round](#belief-audit-round)
- [Other web AI services](#other-web-ai-services)
- [Multi-round control](#multi-round-control)
- [Reject these prompts](#reject-these-prompts)

## Submission gate

Do not submit until the prompt satisfies every applicable item:

1. **Decision:** name the business or strategy decision the answer could change.
2. **Verified subject:** include official URLs and separate verified product facts from working assumptions.
3. **Audience and market:** specify segments, countries or regions, languages, and platforms.
4. **Time window:** define recency; include older material only when explicitly useful as evergreen evidence.
5. **Assigned source role:** state why this service is being used and which branch it owns.
6. **Bounded questions:** ask a finite set of non-overlapping research questions.
7. **Evidence contract:** require direct source URLs, dates, source types, and visible metrics only when actually observable.
8. **Epistemic labels:** require observed fact, reported claim, inference, uncertainty, and contradiction to remain distinct.
9. **Operating constraints:** include team, budget, production, access, cadence, legal, cultural, or editorial limits that affect recommendations.
10. **Output schema:** specify the table, memo, case count, fields, and prioritization method needed at the convergence point.
11. **Anti-fabrication rule:** forbid invented metrics, inaccessible citations, synthetic quotes, unsupported prevalence claims, and false precision.
12. **Round objective:** state whether this is discovery, contradiction, decision, or extraction; do not ask one prompt to finish the entire strategy when later rounds depend on evidence.
13. **Reversal condition:** for a material belief, state what evidence could reverse it and why the team may be motivated to keep believing it.

If an item cannot be supplied, state the gap in the prompt and ask the service to preserve it as uncertainty rather than fill it by guessing.

## Prompt packet

Build each prompt from this compact packet:

```text
Role:
Product/topic and official URLs:
Verified facts:
Working hypotheses to test:
Why we may want them to be true:
Evidence that would reverse them:
Decision affected:
Audience/market/languages/platforms:
Time window:
Assigned research branch:
Questions:
Required primary or behavioral sources:
Operating constraints:
Output schema:
Fact/inference/uncertainty rules:
Prohibited behavior:
Round objective:
```

Prefer precise prose over keyword piles. Give enough product context to prevent category confusion, but do not pre-bias the system with conclusions disguised as facts.

## Grok template

Use Grok for current X discourse, launch threads, creator vocabulary, controversy, and fast-moving hypotheses.

```text
Use your live X search strength. Act as a senior social-growth analyst for [PRODUCT], using [OFFICIAL SITE] and [OFFICIAL REPOSITORY/ACCOUNT]. First verify the product facts below against public sources; label any unverified statement as a working assumption.

Decision: [DECISION].
Audience/market: [SEGMENTS, REGIONS, LANGUAGES].
Time window: [DATES].
Research [SPECIFIC CATEGORY/CONVERSATION] and identify [N] concrete X posts or launch threads.

For each case return: direct x.com URL, account, date, visible engagement if available, first-line attention entry, creative format, proof, CTA, audience response, and why it appears to work or fail. Compare [RELEVANT CONTRAST, such as founder-led vs brand account].

Then map recurring audience language, emotional drivers, objections, and content mechanisms to [DECISION]. Separate observation from inference, flag uncertainty, and do not invent metrics or reconstruct inaccessible posts. Round 1: evidence and pattern map only.
```

For bilingual or cultural research, name both languages, require direct post URLs for each pattern, and request political, cultural, factual, privacy, and identity risks. Avoid generic tourism lists, official-slogan language, or claims about an entire culture from one post.

## Perplexity template

Use Perplexity for source discovery, Reddit evidence, objections, jobs-to-be-done, and competing viewpoints. Select the requested model and thinking mode when available, and record the actual configuration.

```text
Act as a senior consumer-insights researcher. Research current Reddit discussions and credible primary web sources about [CATEGORY] for [PRODUCT/OFFICIAL URLS].

Decision: [DECISION].
Audiences: [SEGMENTS].
Time window: [DATES, plus rule for older evergreen threads].

Focus on: (1) recurring jobs-to-be-done; (2) emotional motivations and desired identity; (3) objections and fears; (4) user language, clearly marked as quote or paraphrase; (5) supportive, skeptical, and hostile viewpoints; (6) audience segments and switching triggers; (7) content angles likely to earn [COMMENTS/SAVES/TRIALS].

For every material theme provide 2-4 direct Reddit thread or comment URLs, dates, community context, evidence strength, and sample-bias warning. Separate sourced evidence from inference. Do not invent statistics, consensus, quotes, or prevalence. Round 1: broad evidence map.
```

Never accept “Reddit users think” without multiple relevant threads or an explicit single-thread limitation.

## Gemini Deep Research template

Use Gemini Deep Research for a broad source-backed dossier, analogy validation, market structure, policy, compliance, and long-form synthesis.

```text
Deep Research task: validate and stress-test [STRATEGY OR WORKING HYPOTHESIS] for [PRODUCT/TOPIC and OFFICIAL URLS].

Decision: [DECISION].
Target market and audience: [REGIONS/SEGMENTS/LANGUAGES].
Channels: [PLATFORMS].
Operating constraints: [TEAM, BUDGET, FILMING DAYS, ACCESS, CADENCE].

Working hypothesis:
- [HYPOTHESIS 1]
- [HYPOTHESIS 2]

Research and return:
1. whether the analogy or hypothesis is valid and where it breaks;
2. [N] directly linked benchmark examples or documented patterns;
3. audience tensions most likely to change the target behavior, separating evidence from inference;
4. the smallest viable content and production system under the stated constraints;
5. platform-specific packaging that reuses source assets;
6. legal, privacy, cultural, compliance, consent, and credibility risks;
7. a prioritized experiment plan with hypotheses and stop/continue rules;
8. a source appendix with direct URL, date, claim supported, source type, and confidence.

Avoid generic plans, broad demographic summaries, official-slogan language, invented benchmarks, and sources you cannot open. Prefer official product pages, original posts, platform guidance, primary data, Reddit threads, and reputable authoritative sources. Flag conflicts and gaps. Round 1: source-backed validation.
```

For a 90-day operating plan, add explicit requests for ICP/JTBD, white space, platform roles, concrete cases, creator/community map, paid-organic loops, KPI tree, UTM taxonomy, resource tiers, and claim discipline. Do not request them unless they affect the named decision.

## ChatGPT templates

Use ChatGPT primarily for red-team review, synthesis, hard prioritization, experiment design, and contradiction audit. Provide an evidence packet instead of asking it to recall the market from memory.

### Red-team round

```text
Act as a skeptical VP of Growth and product-marketing reviewer. Stress-test the proposed strategy for [PRODUCT/OFFICIAL URLS].

Decision: [DECISION].
Verified product facts: [FACTS].
Evidence packet: [SOURCE-LINKED FINDINGS AND OBSERVED BASELINE].
Proposed channel and positioning choices: [CHOICES].
Resources and constraints: [TEAM/BUDGET/TIME].

Identify unsupported assumptions, missing segments or funnel steps, category traps, claim/compliance risks, resource bottlenecks, and evidence that would reverse the recommendation. Then propose a corrected [TIME HORIZON] operating model with explicit priorities, kill criteria, KPI tree, and experiment design using relative baselines rather than invented benchmarks. Separate facts, assumptions, and decisions. Round 1: red-team critique.
```

### Decision round

```text
Round 2. Make the hard choices using the evidence packet and critique above. Choose one primary acquisition wedge and one expansion narrative. Define the exact ICP, trigger, promise, activation event, proof stack, onboarding path, channel roles, weekly cadence, funnel events, KPI tree, UTM taxonomy, and kill/scale rules. Reject weaker alternatives and explain the tradeoff. Then provide the requested content-system framework without repeating one concept in different wording. Keep claims conservative and label assumptions.
```

## Belief audit round

Run this before the decision round for any primary ICP, positioning wedge, channel priority, brand-defining editorial choice, or costly operating model.

```text
Act as an adversarial belief auditor. Do not merely criticize the strategy; test whether the research question, sampling, retrieval coverage, and interpretation were constructed to confirm what the team already wanted.

Working belief: [BELIEF].
Why we want it to be true: [INCENTIVE, IDENTITY, CONVENIENCE, OR PRIOR COMMITMENT].
Decision affected: [DECISION].
Evidence packet: [SOURCE-LINKED SUPPORTING AND DISCONFIRMING EVIDENCE].
Known retrieval limits: [LANGUAGES, PLATFORMS, PAYWALLS, ACCOUNT ACCESS, SAMPLE BIAS].

Return only:
1. strongest supporting evidence;
2. strongest disconfirming evidence;
3. plausible alternative explanations;
4. whether “no counterevidence found” may reflect weak retrieval;
5. the smallest evidence that would reverse the decision;
6. what remains strategically useful if the belief is false;
7. one recommendation: retain, narrow, test, or reject.

Separate observation, reported claim, inference, and missing evidence. Do not average away real conflict or reward the most verbose source.
```

When current external facts are required, explicitly enable or request web search and retain inline source links. When the job is only to critique a supplied evidence packet, do not add unnecessary web research.

## Other web AI services

For Doubao, DeepSeek, ChatGLM, Qwen, Kimi, or another service, use the same submission gate and assign one bounded role. Examples:

- Chinese platform language and culturally native framing;
- long-context source-packet synthesis;
- multilingual comparison and translation-risk audit;
- causal decomposition and disconfirming evidence;
- domestic market, creator, or community hypotheses.

Require original-language sources when translation could change meaning. Never treat a service's model knowledge as a substitute for current platform evidence.

## Multi-round control

Use rounds only when each round has a distinct decision role:

1. **Evidence map:** collect cases, links, user language, conflicts, and gaps.
2. **Contradiction audit:** test sample bias, alternative explanations, missing segments, and evidence that would falsify the pattern.
3. **Belief audit:** test motivated reasoning, retrieval limits, reversal evidence, and what survives if the belief fails.
4. **Decision:** force prioritization, rejected alternatives, resource allocation, and risk controls.
5. **Extraction:** return the exact source ledger, experiment backlog, calendar, or measurement schema needed by the main workflow.

At the start of every later round, provide the relevant evidence packet and unresolved questions. Do not assume the web AI accurately remembers a prior long response. Save the exact prompt and response URL for every material branch.

## Reject these prompts

Rewrite before sending when the prompt:

- asks for “a complete social strategy” without naming the decision or constraints;
- lists many platforms but assigns none a role;
- asks for trends or competitors without a time window and direct URLs;
- provides product claims without official sources or verification instructions;
- requests “viral ideas” before extracting audience tension and proof mechanisms;
- asks several AI systems the same broad question;
- requests exact metrics that the service cannot observe;
- mixes evidence collection, final strategy, calendar, budget, and copywriting into one unbounded round;
- invites stereotypes, political generalization, or cultural claims from thin evidence;
- omits how uncertainty, inaccessible sources, conflicting evidence, and sample bias must be handled.
- asks for a material commitment without disconfirming evidence or a reversal condition.
