---
name: social-media-deep-research
description: Turn real user and market evidence into social-growth decisions and executable experiments, with human judgment, belief audits, cross-category mechanism transfer, production constraints, and measurable stop/scale rules. Use with any Agent Skills-compatible AI agent for overseas or domestic social strategy, audience insight, positioning, competitor or analogous-account research, content benchmarking, product-led social loops, launch planning, low-resource production systems, or research across TikTok, Instagram, YouTube, X, Reddit, Facebook, Douyin, Xiaohongshu, forums, reviews, and authenticated web AI tools.
---

# Social Media Deep Research

Build the shortest defensible path from real user evidence to an executable social-growth experiment. Optimize for decisions, judgment, and reality-tested action, not research volume.

Start every substantial task with three questions:

```text
What decision are we trying to make?
What evidence could reverse that decision?
What is the cheapest experiment that can resolve the remaining uncertainty?
```

## Core model

Use this chain throughout the task:

```text
Business objective + operating constraints
→ AI value and decision-risk gate
→ user tensions and desired progress
→ direct and analogous evidence
→ belief audit + human judgment
→ psychological mechanism
→ product/market translation
→ product outcome or minimum viable content experiment
→ production and measurement loop
```

Treat facts, interpretations, and decisions as separate layers:

- **Evidence:** observable product behavior, original posts, metrics, comments, reviews, interviews, or authoritative documents.
- **Inference:** the proposed reason a pattern works.
- **Decision:** what to test, continue, change, or stop.

Never present inference as observed fact.

## Read supporting references

Read only the references needed for the current request:

- Read [references/research-schema.md](references/research-schema.md) when collecting, scoring, or comparing cases and user comments.
- Read [references/category-transfer.md](references/category-transfer.md) when translating mechanisms between products, markets, platforms, or creator types.
- Read [references/deliverables.md](references/deliverables.md) when producing a strategy document, research database, content calendar, experiment plan, spreadsheet, or Feishu deliverable.
- Read [references/platform-compatibility.md](references/platform-compatibility.md) before selecting the host agent, operating-system path, or authenticated-browser adapter.
- Read [references/ai-research-orchestration.md](references/ai-research-orchestration.md) before using authenticated AI services through an agent-controlled browser, including Grok, Perplexity, Gemini, ChatGPT, Doubao, DeepSeek, ChatGLM, Qwen, or Kimi.
- Read [references/ai-prompt-quality.md](references/ai-prompt-quality.md) before composing or submitting prompts to any web AI service.
- Read [references/decision-protocols.md](references/decision-protocols.md) before starting a costly, multi-branch, reputation-sensitive, or hard-to-reverse research program.
- Read [references/human-harness.md](references/human-harness.md) when taste, strategic commitment, contradiction, credentials, consent, or execution reality requires human judgment.
- Read [references/editorial-judgment.md](references/editorial-judgment.md) when selecting benchmark content, defining content modes, or protecting brand taste and authenticity.
- Read [references/product-led-social.md](references/product-led-social.md) when the product can generate user outcomes, shareable artifacts, templates, or community-led use cases.
- Read [references/source-diversity.md](references/source-diversity.md) when evidence is thin, culturally concentrated, multilingual, or likely to benefit from a bounded serendipity branch.
- Use [schemas/run-state.yaml](schemas/run-state.yaml) for substantial work with multiple branches, long-running external jobs, or decisions that may be revised.
- Use [templates/research-brief.md](templates/research-brief.md), [templates/belief-audit.md](templates/belief-audit.md), [templates/human-checkpoint.md](templates/human-checkpoint.md), or [templates/convergence-memo.md](templates/convergence-memo.md) when a reusable decision artifact is needed.

## Adapt to the host agent and operating system

Follow the open Agent Skills structure: treat `SKILL.md` and its relative references as the source of truth, and map capability names to the tools actually exposed by the host agent. Do not assume Codex-specific tool names, task primitives, or UI metadata.

Select the authenticated-browser path before opening research branches:

- **macOS — preferred:** use EGO Browser with the installed `ego-browser` skill. Reuse isolated task spaces and the user's existing authenticated browser state.
- **Windows — supported fallback:** require Browser Use plus the `eze-is/web-access` skill. Use Chrome or Edge with the required remote-debugging configuration. Treat this path as lower-confidence than macOS plus EGO for complex authenticated and dynamic sites; allow more setup time, smaller action batches, and stricter readback verification.
- **Other environments:** use an equivalent browser adapter only when it exposes observation, interaction, authenticated state, handoff, and verification. Otherwise limit the branch to open-web research and label the missing authenticated evidence.

Read [references/platform-compatibility.md](references/platform-compatibility.md) for installation and capability mapping for Claude Code, Codex, WorkBuddy, OpenClaw, Hermes Agent, and other Agent Skills-compatible hosts.

## Start with the decision, not the browsing

Before researching, determine:

1. What business decision the research must change.
2. The target audience, market, languages, and platforms.
3. The desired outcome: awareness, followers, qualified traffic, trials, revenue, retention, or reputation.
4. Production constraints: people, time, budget, access, assets, approvals, and publishing cadence.
5. Brand, legal, cultural, and operational boundaries.
6. The smallest time horizon in which a useful signal can be observed.

Also state what would reverse the current working belief and what would remain true if that belief is false.

Infer missing details when the assumption is low-risk. Ask only when different answers would materially change the strategy or authorize an external action.

Write a compact research brief before opening research branches:

```text
Decision:
Audience:
Market/platforms:
Success signal:
Constraints:
Non-negotiables:
Known evidence:
Unknowns that could change the decision:
```

Classify the decision as **reversible**, **costly but reversible**, or **hard to reverse / reputation-sensitive**. Increase evidence and human-review requirements with decision risk; do not make low-risk tests wait for high-risk proof standards.

For substantial work, copy [schemas/run-state.yaml](schemas/run-state.yaml) into the working directory and update it at branch start, material evidence changes, contradictions, exclusions, and convergence. Treat it as cognitive version control, not administrative reporting.

## Pass the AI value gate

Before opening AI or multi-agent research branches, ask whether the uncertainty can be resolved faster by:

1. inspecting one primary source;
2. asking one real user;
3. checking internal product or performance data;
4. publishing one cheap reversible test;
5. making a reversible judgment call.

Use AI only when it adds source access, synthesis, contradiction, multilingual coverage, structured extraction, or useful scale. Skip or shrink AI research when the answer cannot change action, direct inspection is faster, internal data owns the truth, experimentation is cheaper, or the decision is primarily taste. Record the gate outcome in run state. Use [references/decision-protocols.md](references/decision-protocols.md) for the full protocol.

## Build a dependency graph, not a rigid checklist

Split the task into branches such as:

- product and positioning audit;
- direct competitors;
- analogous cross-category benchmarks;
- user psychology and objections;
- platform-native cases and comments;
- market, policy, or compliance validation;
- content-system design;
- production planning;
- measurement and experiment design;
- deliverable construction and verification.

Optionally reserve 10%–15% of the research budget for one **serendipity branch** across an adjacent audience, unexpected category, non-default language, or non-obvious platform. Keep it out of the main evidence chain unless it changes a decision.

Classify each branch:

- **Hard dependency:** another action would be unsafe or fundamentally misdirected without it.
- **Soft dependency:** proceed with an explicit provisional assumption and reconcile later.
- **Independent:** execute immediately.
- **Asynchronous external branch:** start it, preserve its task/session/ticket state, and keep working elsewhere.

### Ten-second anti-blocking rule

When a browser research task, Deep Research job, import, export, render, API job, or other external operation has not returned after about 10 seconds:

1. Record its stable identifier, URL, ticket, session, or current state.
2. Move it off the critical path unless it is a hard dependency.
3. Continue the highest-value independent or soft-dependent branch.
4. Poll only at natural milestones, not continuously.
5. Do not submit duplicate jobs while the original is active.
6. Reconcile the result at the next convergence point:
   - consistent result → add evidence only;
   - useful increment → update the affected section;
   - material conflict → revisit only dependent decisions;
   - weak or unsupported result → exclude or label it.

Do not wait idly merely because a nominal “previous step” is unfinished.

## Research in parallel by source role

Prefer primary and behavioral sources. Assign each source a distinct job:

- **Product/website/app:** confirm actual positioning, workflow, features, price, and proof.
- **Native social platforms:** observe real attention entries, formats, public metrics, comments, recurring series, and creator behavior.
- **Reviews, Reddit, forums, communities:** find anxieties, objections, workarounds, switching triggers, vocabulary, and unmet needs.
- **Search and authoritative sources:** validate market facts, laws, platform policies, product claims, and technical constraints.
- **AI research tools:** generate hypotheses, cluster evidence, expose gaps, and stress-test conclusions.

Do not ask several AI systems the same broad question. Give each a bounded role, such as:

- source-backed synthesis;
- current conversational signals;
- long-form market or regulatory validation;
- final contradiction audit.

Treat AI output as a lead until checked against source material.

### Route authenticated AI research through the browser adapter

When authenticated browser access is available and AI research could materially reduce uncertainty, use the operating-system path selected above and the routing procedure in [references/ai-research-orchestration.md](references/ai-research-orchestration.md). Select only the smallest set of services with distinct jobs; do not open every service by default.

Select AI tools by required capability first: live social search, deep research, source discovery, authenticated platform access, long-context synthesis, multilingual native reasoning, adversarial review, or structured extraction. Then choose the smallest currently available service set and verify the capability, mode, limitation, and fallback at runtime. Treat named services as current adapters, not permanent truths. Read [references/ai-research-orchestration.md](references/ai-research-orchestration.md).

Compile and pass every outbound prompt through [references/ai-prompt-quality.md](references/ai-prompt-quality.md). Do not submit a vague request, an unverified product brief, or a prompt without a decision, target audience, market, time window, source requirements, output schema, uncertainty rule, and anti-fabrication rule appropriate to the branch.

Run multi-round, bounded conversations rather than one broad prompt. Preserve the conversation URL, model or mode, date, exact prompt, useful source links, unresolved conflicts, and the decision each branch could change. Return to original posts, comments, product pages, papers, or authoritative documents before treating a claim as evidence. Cite the original source, not the AI conversation, whenever possible.

Verify the active account and requested research mode before submission. Never enter passwords, one-time codes, or other secrets on the user's behalf. If login, CAPTCHA, 2FA, or an unavailable account blocks the required configuration, hand browser control to the user and resume only after explicit confirmation.

When real-browser interaction is available, use it for authenticated or dynamic platforms and inspect actual posts and comments. Preserve direct URLs and the date observed.

## Choose benchmarks by psychological equivalence

Research two benchmark sets:

1. **Direct benchmarks:** same category, customer, use case, or business model.
2. **Analogous benchmarks:** different surface category but the same audience tension, proof structure, identity dynamic, or follow reason.

Ask:

- What is the attention entry, and does it fit the intended brand relationship?
- What unresolved tension keeps them watching?
- What visible proof resolves the tension?
- What makes someone comment, share, save, click, or follow?
- Which relationship or recurring promise sustains a series?
- What production primitive makes the format repeatable?

Copy the mechanism, not the topic, aesthetics, or creator persona.

Reject an analogy when it depends on conditions the product cannot or should not reproduce: deception, unsafe filming, unavailable access, excessive production, incompatible culture, legal risk, or credibility damage.

## Extract mechanisms before creating ideas

For every material case, capture at least:

- audience and context;
- first-frame or first-line attention entry;
- tension or promised progress;
- visible proof or payoff;
- comment psychology;
- share/save/follow reason;
- repeatable structure;
- production cost and prerequisites;
- brand/compliance risk;
- translation hypothesis for the target product;
- direct source and observation date.

Use the full schema and contextual comparison model in [references/research-schema.md](references/research-schema.md).

Do not create a large idea list before identifying a small set of repeatable mechanisms. Do not rank cases by an unexamined total score: strategic fit, evidence credibility, executability, brand acceptability, and fatal vetoes are not interchangeable.

## Audit major beliefs and use human judgment

Before committing to a primary ICP, positioning wedge, channel priority, brand-defining content mode, or costly production system, run the belief audit in [templates/belief-audit.md](templates/belief-audit.md). Examine why the team wants the belief to be true, the strongest supporting and disconfirming evidence, alternative explanations, reversal conditions, and what remains useful if the belief fails.

Do not confuse “no counterevidence found” with “counterevidence does not exist.” Consider retrieval limits, language bias, platform access, and sample construction.

Use the four human checkpoints in [references/human-harness.md](references/human-harness.md): decision, taste, contradiction, and reality. Pause only when a human judgment could materially redirect strategy or authorize a sensitive action; otherwise record a provisional judgment and keep progressing.

## Convert psychology into a content system

Cluster evidence into two to five dominant audience motives, such as:

- identity confirmation;
- correction impulse;
- competence or automation fantasy;
- risk reduction;
- social currency;
- curiosity about an outcome;
- relationship projection;
- participation in what happens next;
- stereotype reversal;
- progress tracking.

Then define three to five recurring content pillars. Each pillar needs:

- a named audience tension;
- a repeatable narrative structure;
- a visible proof type;
- a follow reason;
- a production template;
- a platform-specific packaging rule;
- a hypothesis and stop/continue rule.

Choose an editorial mode intentionally: direct proof, narrative tension, quiet authority, founder thinking, documentary observation, community participation, search utility, or trust repair. Do not default to exaggerated contrast, fake surprise, artificial countdowns, “you won't believe” framing, or saturated keyword-comment bait. Use [references/editorial-judgment.md](references/editorial-judgment.md).

Prefer production primitives over isolated ideas. Examples:

- “I believed X; a user or expert corrected me; I tested it.”
- “Can the product complete Y with one instruction, ten minutes, or a fixed budget?”
- “Old workflow versus new workflow, measured visibly.”
- “One user question, three user types, three answers.”
- “A comment determines the next test.”
- “The polished output versus what happened behind it.”

## Design around constraints

Use constraints as architecture inputs. If the team has three filming days, limited presenters, no public filming permission, or one editor, design the system around those facts before proposing formats.

Batch by shared resources:

- location;
- participant;
- props or product state;
- lighting and camera setup;
- approval type;
- common B-roll;
- reusable attention-entry and CTA variants.

One source asset may create multiple platform packages. Change the opening, length, caption, cover, CTA, and context—not necessarily the shoot.

## Connect product value to social proof

When the product creates a visible user outcome, design the loop in [references/product-led-social.md](references/product-led-social.md):

```text
Audience problem → product use case → successful user outcome
→ privacy-safe shareable artifact → social proof
→ new-user activation → new outcome
```

Do not force product-led sharing when the artifact exposes sensitive data, weakens user trust, or fails to prove value. Feed recurring social questions and user-created outcomes back into demos, templates, onboarding, and product discovery.

## Translate strategy into experiments

Turn every major recommendation into a falsifiable experiment:

```text
Hypothesis:
Audience:
Mechanism:
Content variants:
Controlled variables:
Primary metric:
Secondary diagnostic metrics:
Observation window:
Continue rule:
Revise rule:
Stop rule:
Risk trigger:
```

Avoid universal benchmark thresholds for new accounts. Use directional external benchmarks only until the account has enough posts to establish its own median and percentile ranges.

Separate diagnosis:

- weak early retention → opening problem;
- good retention but weak sharing → payoff lacks social value;
- strong comments but weak follows → profile or series promise is unclear;
- strong profile visits but weak conversion → positioning or pinned content problem;
- repeated negative cultural correction → research, framing, or consent problem;
- no behavioral signal after two fair tests → stop or radically reframe.

## Protect evidence and credibility

- Prefer original posts and comments over commentary about them.
- Record public metrics as observed snapshots, not timeless facts.
- Attribute claims as platform-reported, creator-reported, user-reported, inferred, or independently verified.
- Verify current laws, product specifications, platform rules, pricing, and other unstable facts with authoritative sources.
- Do not convert one user, friend, family, comment, or creator into a claim about an entire culture or market.
- Verify important non-default-language evidence in the original language or record translation risk; use [references/source-diversity.md](references/source-diversity.md).
- Treat consent, privacy, sponsorship disclosure, employment policy, and editorial independence as design constraints.
- Keep commercial content distinct from editorial or journalistic content when applicable.

## Communicate while executing

Keep commentary concise and decision-focused:

- state the current conclusion or assumption;
- identify the branch now running;
- mention when a slow branch was backgrounded and what work continued;
- surface only conflicts that may change the result;
- avoid narrating every click or repeated poll.

The user should see continued forward progress even while external jobs run.

## Finish with operational deliverables

Select the smallest deliverable set that lets the user act. Typical outputs:

- strategic decision memo;
- source-linked benchmark database;
- audience tension and psychology map;
- recurring content-system definitions;
- first-month experiment backlog;
- batch production plan;
- platform packaging matrix;
- measurement and decision table;
- compliance checklist;
- belief audit and convergence memo when the decision is material;
- product-led social loop when shareable outcomes exist;
- spreadsheet or Base ready for weekly operation.

If the user requests Feishu delivery, use an installed Feishu CLI, connector, or Feishu-specific skill rather than browser editing. Create a clean import-specific workbook with field headers on row 1; keep decorative spreadsheets separate because Base schema inference may misread title bands and merged cells. Import serially into the same destination, retain task tickets, and verify tables, fields, and sample records after conversion.

Use the exact output structures in [references/deliverables.md](references/deliverables.md).

## Completion criteria

Finish only when:

- every material decision is supported by evidence or clearly labeled inference;
- direct and analogous benchmarks have been distinguished;
- the strategy respects actual resource and compliance constraints;
- recommendations have become executable experiments;
- production, publishing, and measurement form a closed loop;
- sources are directly accessible and observation dates are recorded;
- slow external branches have been reconciled or explicitly excluded;
- major beliefs preserve supporting evidence, disconfirming evidence, and reversal conditions;
- the human reality checkpoint confirms the next experiment is genuinely executable;
- files or external deliverables have been verified after creation or import.

Do not equate a long report with completed research. Completion means the next experiment can start without another strategy meeting.
