# Workflow Control and Branch Completeness

Use this reference for every substantial Standard or Deep run. Its purpose is to prevent branch loss, context drift, duplicated browsing, and premature strategy writing.

The companion `scripts/workflow_guard.py` is the executable contract. A prose checklist does not count as a gate. Run it against persisted state before browsing, after every branch, before convergence, before calendar drafting, and before delivery; a non-zero exit is a hard stop.

## Run the startup preflight before scope initialization

1. Detect the operating system and required browser/Skill path from [platform-compatibility.md](platform-compatibility.md). On macOS, perform one harmless live EGO invocation; on Windows, perform the Browser Use/Web Access adapter detection. Documentation or catalog presence alone does not pass. Record present and missing components. Stay silent when everything is available; remind the user only about missing components.
2. Assess difficulty, risk, platform count, language count, evidence access, and cost of error.
3. Present Light, Standard, and Deep with task-specific effort and evidence differences. Recommend one and wait for the user's selection unless the request already selected it.
4. Identify only the social platforms needed for the task. Check visible login state when safe; remind once for relevant platforms that are not logged in. Never request credentials.
5. Present optional web-AI services with distinct recommended jobs. Let the user select or decline them, then check login only for selected services.
6. Show the proposed dependency flow and parallel browser plan before broad research.

Persist these outcomes under `preflight`. The Blueprint Gate rejects a missing mode confirmation, browser detection, relevant-platform login decision, or AI-service choice record.

## Treat run state as the workflow source of truth

Before browsing, copy `schemas/run-state.yaml` into the task workspace and fill the project, workflow, branch inventory, dependencies, fallbacks, and checkpoints. Do not keep the only copy of the plan in conversation memory.

On every continuation, compaction, handoff, or return from a long-running branch:

1. Read the current run state first.
2. Restate the active decision and current stage internally.
3. Reconcile completed, active, waiting, excluded, and missing branches.
4. Resume the next dependency-ready branch; do not rebuild the workflow from memory.

## Build the branch blueprint before research

For Light runs, record the decision, two source roles, one contradiction path, and one experiment. For Standard and Deep runs, consider every branch family below and give it one explicit disposition:

- `required`: hard dependency; strategy cannot proceed without completion or a defensible degraded result;
- `planned`: useful soft or independent branch;
- `excluded_by_user`: outside explicit user scope;
- `excluded_by_value_gate`: cannot change the decision or a cheaper truth owner exists;
- `not_applicable`: structurally irrelevant, with a reason.

Never leave a candidate branch absent or silently unexecuted.

| Branch family | Default consideration | Typical evidence or decision role |
| --- | --- | --- |
| Official website/product baseline | Required unless unavailable, irrelevant, or excluded by the user | Official website/product reality, first-party documents, current offer, brand claims |
| Official social accounts | Required for social/account work unless unavailable, irrelevant, or excluded by the user | First-party profile promise, cadence, current creative and conversion surfaces |
| Target native-account performance | Required for account/content audits when access exists | Original posts, formats, public metrics, comments, cadence, profile promise, conversion path |
| Search-intent and keyword map | Required consideration for editorial, SEO, discovery, trend, or content-planning work | Audience jobs, anxieties, questions, native-language queries, autocomplete/platform search terms |
| Native high-performing cases | Required consideration for content strategy | Search keywords on the target platform, open original posts, compare visible performance in context |
| Direct competitors | Required consideration for positioning and content-system decisions | Same buyer, category, offer, market, or business model |
| Analogous mechanisms | Required consideration when direct cases are thin or repetitive | Same tension, proof, trust, identity, or follow reason in another category |
| User voice and community | Include when vocabulary, objection, anxiety, or buyer intent could change the decision | Comments, Reddit, forums, reviews, interviews, sales/support language |
| Authoritative facts | Required when law, policy, safety, technical limits, pricing, or unstable facts affect the claim | First-party or authoritative sources |
| Internal evidence or one real user | Prefer when it owns conversion, product truth, constraints, or execution reality | Insights, CRM, DMs, interviews, performance data, team capacity |
| AI research | Include only after the AI Value Gate | Bounded source discovery, contradiction, multilingual coverage, long-context synthesis, structured extraction |

For `social_content_strategy`, direct competitors, analogous mechanisms, search-intent keywords, and native high-performing cases are mandatory included families. Evidence access may degrade a branch, but the branch cannot silently disappear or be replaced by generic model knowledge.

For every included branch record:

```text
Branch ID and family:
Question and decision affected:
Source role and target surface:
Required capability:
Dependency: hard / soft / independent / asynchronous external
Owner or execution path:
Time or source budget:
Entry condition and stop rule:
Fallback ladder:
Expected artifact:
Status and stable session/job IDs:
```

## Build search intent before searching for hits

When the task concerns content, discovery, positioning, or trends, create a bounded search map before collecting examples:

1. Name the audience roles and decision situations.
2. Generate query families from desired progress, anxieties, objections, alternatives, geography, product/category terms, and native platform vocabulary.
3. Translate only after identifying the evidence language; preserve original-language queries.
4. Probe a small set through search-engine discovery, platform-native search/autocomplete/hashtags, and community language where available.
5. Probe at least one relevant supplemental social platform when access permits—for example TikTok for an Instagram plan or YouTube/Reddit for tutorial and objection language. Keep target and supplemental results separate.
6. Use validated queries to find original high-performing social cases. Open each original post and record query, URL, date, account context, first frame/line, visible metrics, comments, and access limits.
7. Call a case `high-performing` only relative to observable account or comparable context. Do not invent an absolute viral threshold or infer saves, shares, reach, conversion, or target-platform demand from cross-platform attention.

Stop expanding keywords when new queries repeat the same mechanisms or cannot change the experiment.

## Plan browser parallelism explicitly

EGO supports multiple isolated task spaces and tabs. Use that capability only for independent work.

Before browsing, group branches into:

- `parallel_now`: independent, no shared mutable surface, and safe under account/rate limits;
- `parallel_after_gate`: start after a shared adapter or authentication gate passes;
- `sequential_dependency`: requires another branch's output;
- `single_surface_only`: same editor/account flow or action state; do not race.

When the host supports concurrency, give each independent branch its own EGO task space, tab set, owner, and stable ID. Never let two agents control the same task space. When concurrency is unavailable, round-robin across preserved task spaces instead of reopening or duplicating work.

Before every research wave, run `workflow_guard.py audit`. When the audit identifies two or more dependency-ready, account-safe branches, either parallelize them in separate task spaces or record why shared authentication, rate limits, or a sequential dependency makes parallelism unsafe. Re-run the audit after each branch, user update, external-job return, and before convergence/delivery.

Use a two-wave default. Wave 1 is the sequential official brand/account/native baseline. Wave 2 may run three independent EGO task spaces when safe: (1) direct competitors plus analogous mechanisms, (2) user-selected bounded AI services, and (3) keyword families traced to target-native and supplemental-platform performance. Keep authentication handoffs, sensitive actions, belief convergence, and final strategy selection sequential.

## Run the same workflow with fewer round trips

Efficiency is an execution property, not a reason to weaken the blueprint. Preserve every branch disposition, branch-exit gate, audit, prerequisite, belief gate, and delivery gate.

### 1. Budget the evidence before opening pages

Translate every branch's time or source budget into a bounded retrieval plan. For example:

```text
Official baseline: 3 first-party pages
Target account: 12 recent originals + up to 3 outliers
Direct competitors: 3 verified accounts × 2 originals
Adjacent or analogous cases: 2–3 originals
Native keyword families: 3–6
Supplemental-platform originals: 2–4
Authoritative facts: 2–4 first-party sources
Visual inspections: only decision-relevant covers, layouts, or shot structures
Fallback attempts: no more than the predeclared ladder requires
```

These are task-specific examples, not new universal minimums. Stop earlier when the declared stop rule is satisfied.

### 2. Use a discovery pass and an extraction pass

During discovery, capture only canonical URLs, account identity, classification lead, query path, and why the source may change the decision. Deduplicate before opening originals.

During extraction, process the selected originals as a batch. Capture a compact row per source:

```text
source_id | canonical_url | author/account | date | format |
caption/topic | visible labelled metrics | first-frame/line mechanism |
decision use | conflict/limitation
```

Do not narrate or synthesize after every URL. Finish the bounded batch, then write one observation/inference/decision synthesis for the branch.

### 3. Match observation cost to the decision

- Use semantic/DOM or structured metadata for text and public labels.
- Add a screenshot only when visual packaging, first-frame legibility, subtitle treatment, layout, or authenticity affects the mechanism judgment.
- Use first-party direct text retrieval for static official pages; reserve interactive browser work for dynamic or authenticated surfaces.
- If live DOM and metadata disagree, record the discrepancy once and apply the declared preference rule across the batch.

### 4. Batch safely inside preserved task spaces

Reuse one stable task space per branch/subtask. In EGO, loop across the deduplicated URL list inside one coherent heredoc and emit structured rows with `cliLog`. In another host, use its nearest safe batch equivalent. Do not batch login, CAPTCHA, consent, publication, payment, shared-editor writes, or any interaction where one page's state changes another.

Keep browser rounds substantial: observe, act if authorized, extract, verify, and log several independent sources. Use a tiny round only for a capability probe, error diagnosis, authentication handoff, or ambiguous visual state.

### 5. Reconcile once per branch or completed wave

Write raw observations once in the owning branch artifact. Reuse stable evidence IDs in the belief audit, evidence limits, and research-to-calendar change log.

When several independent branches finish in the same wave, prepare each branch's sources, conflicts, limitations, changed beliefs, and final status first. Then run each required `branch-exit` gate and `audit` in order inside one shell/tool batch. This reduces interface latency without collapsing checkpoints or hiding a failed gate.

### 6. Scaffold output fields without drafting early

After the blueprint, create only a blank schema when it prevents later formatting work—for example date, format, topic, on-asset copy, caption, hashtags, CTA, evidence ID, production requirement, and metric. Populate recommendations or calendar content only after the applicable `assert --action strategy` or `assert --action calendar` succeeds.

### 7. Stop when evidence stops changing the decision

Close a branch when each new source repeats an existing mechanism and cannot reasonably:

- reverse or narrow a first-order belief;
- change a topic, opening, proof type, format, CTA, cadence, or metric;
- introduce a new factual, cultural, legal, or operational risk; or
- change the cheapest next experiment.

Record the saturation reason and remaining uncertainty. Do not continue browsing to make an already-reversible decision feel certain.

## Lock social content calendars behind the research contract

Before writing a final social content calendar, complete and record all five artifacts:

1. **Competitor data:** direct/adjacent account basis, original profiles/posts, dates, visible labelled metrics, mechanisms, and comparison limitations.
2. **Keyword psychology:** audience role, decision situation, desired progress, anxiety/objection, and query family.
3. **Keyword-to-native performance:** query-to-original-post path on the target platform, plus a relevant supplemental-platform probe or explicit degraded access record.
4. **Evidence limitations:** inaccessible metrics, private analytics, personalization, language transfer, sample bias, account-relative comparison, and high-risk factual claims.
5. **Research-to-calendar change log:** each material finding mapped to the topics, openings, proof, formats, CTA, cadence, or measurement it will change.

Set the five `content_strategy_contract` flags and artifact paths, pass the Pre-Convergence Completeness Gate, then run `workflow_guard.py assert --action calendar`. Do not draft the final calendar from a partial branch, search snippets, or AI prose.

## Pass four workflow integrity checkpoints

### Checkpoint 1: Blueprint gate

Before broad research:

- decision, risk, success signal, constraints, and reversal condition exist;
- every branch family has a disposition and reason;
- every included branch records its owned question/decision, dependency, owner or execution path, time or source budget, entry condition, stop rule, fallback ladder, expected artifact, and parallel group;
- hard dependencies and stable session/job identifiers are planned;
- explicit user exclusions are preserved.

If any included branch omits one of these fields, the Blueprint Gate is `FAIL`; do not start broad browsing. A branch-name list or generic research checklist is not a valid blueprint.

### Checkpoint 2: Branch-exit gate

After every branch:

- save direct sources, dates, evidence/inference separation, conflicts, and limitations;
- set status to complete, degraded, excluded, or waiting;
- record whether the branch changed another branch, belief, or experiment;
- audit the blueprint for newly missing or obsolete work.

Do not start strategy drafting merely because one productive branch finished.

Run `workflow_guard.py gate --gate branch-exit --branch BRANCH_ID`, then `workflow_guard.py audit`.

### Checkpoint 3: Pre-convergence completeness gate

Before belief audit or strategy selection:

- every hard dependency is complete, defensibly degraded, or explicitly blocked;
- every planned branch is complete or excluded with a reason;
- official baseline, target-native behavior, keyword/high-performing-case discovery, direct competitors, analogous mechanisms, internal/user truth, and AI were each either handled or explicitly ruled out;
- long-running jobs have a stable ID, current state, timeout/hedge decision, and inclusion plan;
- multi-AI sources are ready for deduplication.

If a branch was forgotten, reopen it. If it no longer has decision value, exclude it explicitly. Do not silently skip it.

Run `workflow_guard.py gate --gate pre-convergence`. For a social content calendar, this gate also checks the cross-platform probe and five contract artifacts. Run `workflow_guard.py assert --action calendar` immediately before drafting.

### Checkpoint 4: Pre-delivery gate

Before final delivery:

- every material recommendation traces to evidence or is labelled a test;
- the belief gate, convergence artifact, experiment, owners, metrics, risks, and stop rules are complete;
- created artifacts and external links are verified;
- run state contains no active or unexplained planned branch.

Run `workflow_guard.py audit`, `workflow_guard.py gate --gate pre-delivery`, and `workflow_guard.py assert --action delivery` immediately before final output.

## Use the branch ledger to control scope, not inflate it

Completeness means every branch was considered and dispositioned. It does not mean every branch must run. Exclude branches when they cannot change the decision, duplicate stronger evidence, violate the user's scope, or cost more than the next reversible test. Record the reason so that efficiency is distinguishable from forgetting.
