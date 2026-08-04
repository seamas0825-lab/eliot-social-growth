---
name: social-media-deep-research
description: Conduct evidence-backed deep research for social-media marketing in any product category, then translate user psychology and cross-category content mechanisms into executable positioning, content systems, experiments, and measurement plans. Use for overseas or domestic social strategy, audience insight, competitor and analogous-account research, content benchmarking, platform case analysis, first-month launch plans, low-resource production systems, or when the user asks to research products across TikTok, Instagram, YouTube, X, Reddit, Facebook, Douyin, Xiaohongshu, forums, reviews, and authenticated AI research tools through EGO.
---

# Social Media Deep Research

Build the shortest defensible path from real user evidence to an executable social-media experiment. Optimize for decisions and action, not research volume.

## Core model

Use this chain throughout the task:

```text
Business objective + operating constraints
→ user tensions and desired progress
→ direct and analogous evidence
→ psychological mechanism
→ product/market translation
→ minimum viable content experiments
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
- Read [references/ai-research-orchestration.md](references/ai-research-orchestration.md) before using authenticated AI services through EGO, including Grok, Perplexity, Gemini, ChatGPT, Doubao, DeepSeek, ChatGLM, Qwen, or Kimi.

## Start with the decision, not the browsing

Before researching, determine:

1. What business decision the research must change.
2. The target audience, market, languages, and platforms.
3. The desired outcome: awareness, followers, qualified traffic, trials, revenue, retention, or reputation.
4. Production constraints: people, time, budget, access, assets, approvals, and publishing cadence.
5. Brand, legal, cultural, and operational boundaries.
6. The smallest time horizon in which a useful signal can be observed.

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
- **Native social platforms:** observe real hooks, formats, public metrics, comments, recurring series, and creator behavior.
- **Reviews, Reddit, forums, communities:** find anxieties, objections, workarounds, switching triggers, vocabulary, and unmet needs.
- **Search and authoritative sources:** validate market facts, laws, platform policies, product claims, and technical constraints.
- **AI research tools:** generate hypotheses, cluster evidence, expose gaps, and stress-test conclusions.

Do not ask several AI systems the same broad question. Give each a bounded role, such as:

- source-backed synthesis;
- current conversational signals;
- long-form market or regulatory validation;
- final contradiction audit.

Treat AI output as a lead until checked against source material.

### Route authenticated AI research through EGO

When authenticated browser access is available and AI research could materially reduce uncertainty, use the `ego-browser` skill and the routing procedure in [references/ai-research-orchestration.md](references/ai-research-orchestration.md). Select only the smallest set of services with distinct jobs; do not open every service by default.

For overseas work, prefer a complementary mix such as Perplexity for source discovery and Reddit leads, Gemini Deep Research for a broad source-backed dossier, Grok for current X discourse, and ChatGPT for synthesis or contradiction testing. For China-focused work, route suitable branches to Doubao, DeepSeek, ChatGLM, Qwen, or Kimi according to the research question and available features.

Run multi-round, bounded conversations rather than one broad prompt. Preserve the conversation URL, model or mode, date, useful source links, unresolved conflicts, and the decision each branch could change. Return to original posts, comments, product pages, papers, or authoritative documents before treating a claim as evidence. Cite the original source, not the AI conversation, whenever possible.

Verify the active account and requested research mode before submission. Never enter passwords, one-time codes, or other secrets on the user's behalf. If login, CAPTCHA, 2FA, or an unavailable account blocks the required configuration, hand the EGO task space to the user and resume only after explicit confirmation.

When real-browser interaction is available, use it for authenticated or dynamic platforms and inspect actual posts and comments. Preserve direct URLs and the date observed.

## Choose benchmarks by psychological equivalence

Research two benchmark sets:

1. **Direct benchmarks:** same category, customer, use case, or business model.
2. **Analogous benchmarks:** different surface category but the same audience tension, proof structure, identity dynamic, or follow reason.

Ask:

- What makes the audience stop?
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
- first-frame or first-line hook;
- tension or promised progress;
- visible proof or payoff;
- comment psychology;
- share/save/follow reason;
- repeatable structure;
- production cost and prerequisites;
- brand/compliance risk;
- translation hypothesis for the target product;
- direct source and observation date.

Use the full schema and scoring model in [references/research-schema.md](references/research-schema.md).

Do not create a large idea list before identifying a small set of repeatable mechanisms.

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
- reusable hook and CTA variants.

One source asset may create multiple platform packages. Change the opening, length, caption, cover, CTA, and context—not necessarily the shoot.

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
- spreadsheet or Base ready for weekly operation.

If the user requests Feishu delivery, use Feishu CLI skills and commands rather than browser editing. Create a clean import-specific workbook with field headers on row 1; keep decorative spreadsheets separate because Base schema inference may misread title bands and merged cells. Import serially into the same destination, retain task tickets, and verify tables, fields, and sample records after conversion.

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
- files or external deliverables have been verified after creation or import.

Do not equate a long report with completed research. Completion means the next experiment can start without another strategy meeting.
